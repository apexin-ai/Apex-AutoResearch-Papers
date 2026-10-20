# Director coordination — Part 3 of 9

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/53/532e22af863d2a24e206.json)

## Round 71

### Tool call

_source line 726 · 2026-05-16T19:39:13.062224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-16T19:39:13.113088+00:00_

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
23	\nolinenumbers
24	\maketitle
25	
26	\input{abstract}
27	\input{introduction}
28	\input{method}
29	\input{experiments}
30	\input{related_work}
31	\input{discussion}
32	\input{conclusion}
33	
34	\section*{Limitations}
35	
36	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct); generalization requires further validation. The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface additional signal. Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}; more sophisticated strategies (e.g., Reflexion~\citep{reflexion-2023} or Tree-of-Thought backtracking~\citep{tot-2023}) may reduce internal death rates and lower DAF. Episode-level labels may assign suboptimal routing to individual steps, particularly those preceding death events, and training on pure-strategy trajectories introduces distribution shift at deployment~\citep{dagger-2011}. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:discussion}, Appendix~\ref{app:cross-env}) provide supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct replication (7 task types, $N{=}70$; Appendix~\ref{app:cross-model}) confirms direction-consisten
…[truncated 5790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-16T19:39:17.634753+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 729 · 2026-05-16T19:39:19.641776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 730 · 2026-05-16T19:39:19.692683+00:00_

100	lifespan-l-then-s      & 0.976 \\
101	inclined-plane         & 0.969 \\
102	freeze                 & 0.971 \\
103	meas-melt-point        & 0.972 \\
104	id-life-stages-2       & 0.972 \\
105	find-animal            & 0.970 \\
106	grow-fruit             & 0.973 \\
107	chem-mix               & 0.969 \\
108	find-non-living        & 0.980 \\
109	\bottomrule
110	\end{tabular}
111	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
112	\label{tab:loo}
113	\end{table}
114	
115	\section{Router Training Details}
116	\label{app:router-details}
117	
118	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
119	
120	With gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split, suggesting overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\sim}54\%$ balanced accuracy). All reported results use gradient accumulation 8.
121	
122	Under step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\% to 58.1\%, but internal recall varies from 51.5\% to 81.8\%, reflecting threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \pm 2.2\%$ across 8 cross-split seeds (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
123	
124	\paragraph{Evaluation methods.} All results use \emph{generation-based evaluation}: the model generates a routing label as text (
…[truncated 14669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-16T19:39:28.323772+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"}]

Based on the search results, here's the information about EMNLP 2026 call for papers:

## Submission Deadline

The EMNLP 2026 paper submission deadline is May 25, 2026 at 23:59:59 (UTC-12).

## Important Dates

Key dates include: ARR submission deadline (long & short papers) May 25, 2026; Reviewer registration deadline for ALL authors May 27, 2026; Author res
…[truncated 1519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 10689
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-16T19:39:32.640892+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 page limit format requirements long paper ARR submission guidelines 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 page limit format requirements long paper ARR submission guidelines 2026"
  }
}
```

</details>

---


### Tool call

_source line 733 · 2026-05-16T19:39:34.583180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": "300",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "offset": "300",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 734 · 2026-05-16T19:39:34.635278+00:00_

300	\bottomrule
301	\end{tabular}
302	\caption{Capacity scaling: step-level and episode-level balanced accuracy. Step-level accuracy is flat across scales ($52.8$--$54.1\%$). At episode level, 4B first breaks the random baseline ($58.96\%$, 95\% CI $[55.1\%, 62.8\%]$). $\dagger$\,1.7B episode-level figure comes from the main experiment (\S\ref{sec:router-diagnostic}) with a different training configuration (8 cross-split seeds vs.\ 4 seeds for 0.6B/4B); direct comparison across scales should be interpreted with this caveat.}
303	\label{tab:capacity}
304	\end{table}
305	
306	Step-level balanced accuracy is essentially flat across scales ($52.8$--$54.1\%$), indicating that step-level discrimination is not capacity-sensitive. At episode level, however, the 4B model first breaks the random baseline ($58.96 \pm 1.94\%$, 95\% CI $[55.1\%, 62.8\%]$), suggesting that model capacity is one limiting factor for episode-level generalization. Nevertheless, even 4B achieves only ${\sim}59\%$---far from a practically useful router---and the dominant explanation remains that death avoidance constitutes a task-type-level binary signal that a step-level router cannot exploit efficiently.
307	
308	\paragraph{Reasoning depth.} An ablation comparing chain-of-thought reasoning against direct-answer generation on 6 task types ($n{=}120$ episodes per condition, 6 tasks $\times$ 20 episodes per task) found no significant difference (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%), confirming that reasoning depth does not meaningfully alter internal-mode outcomes.
309	
310	\section{Cross-Environment Analysis: ALFWorld}
311	\label{app:cross-env}
312	
313	We evaluate on ALFWorld~\citep{alfworld-2021}, a text-based household environment with 6 task types (json\_2.1.1 split, valid\_seen, 135 games, max 50 steps, binary success metric), using Qwen2.5-7B-Instruct. Unlike ScienceWorld, ALFWorld has no death penalty---failure means exhausting the step b
…[truncated 1793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-16T19:39:38.754976+00:00_

Web search results for query: "EMNLP 2026 page limit format requirements long paper ARR submission guidelines 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Submissions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/about/submissions"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here are the key format requirements and guidelines for EMNLP 2026 long paper submissions via ARR:

## Page Limits and Format

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, which are available at github.com/acl-org/acl-style-files.

## Mandatory Sections

The mandatory Limitations section is required, placed after the conclusion.

## Submission System and Process

EMNLP 
…[truncated 741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6114
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-16T19:39:46.145520+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-16T19:39:46.145855+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-16T19:39:46.497230+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-16T19:39:46.648121+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-16T19:39:50.258706+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-16T19:39:50.812198+00:00_

1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet understanding \emph{what} drives the value of routing decisions remains unclear. We introduce a formal diagnostic framework---episode-level counterfactual analysis with the Death Avoidance Factor (DAF) metric---that decomposes routing signal into death-avoidance and non-death components by running complete episodes under pure strategies and comparing final outcomes. The framework is environment-agnostic, requiring only paired episode outcomes under two modalities. We demonstrate this in environments with catastrophic failure modes. Applied to ScienceWorld (11 of 30 task types, 245 episodes, Qwen2.5-7B-Instruct), \textbf{78.9\% of non-tie routing labels} (75 of 95, penalty-independent) are driven by death asymmetry; under ScienceWorld's actual penalty ($P{=}100$), this corresponds to DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$, score-level, $P$-dependent). Per-task death rate correlates with routing signal ($r{=}0.97$), though this is largely a mathematical consequence of death dominance (partial $r{=}0.02$, $p{=}0.91$ after controlling for $\delta \cdot P$; \S\ref{sec:death-decomp}). An exploratory router yields an informative negative: episode-level balanced accuracy remains at or below chance at practical scales (0.6B--1.7B) and reaches only $59.0\%$ at 4B ($p < 0.005$), a disproportionate cost for $+9$\,pp above random---validating the analytical framework over brute-force learned routing. Cross-environment analysis on MATH ($N{=}300$) shows the death-driven routing signal is not statistically detectable without a death penalty ($+4.3$~pp, $p = 0.079$, not reaching $\alpha{=}0.05$). A Llama-3.1-8B-Instruct replication (7 task types, 70 episodes) confirms direction-consistent death patterns for all task types ($+34.3\%$ vs.\ $+26.6\%$ death-rate differential). These findings indicate that in environments with catastrophic fail
…[truncated 166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-16T19:39:50.812595+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-16T19:39:51.214263+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}---a text-based science simulation with 30 task types---faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	The shared assumption is that routing signal stems from diverse sources---accuracy, latency, capability matching---and that a learned router can exploit this signal to improve over any fixed strategy.
10	But this assumption has never been systematically verified: \emph{what actually drives the value of routing decisions in interactive environments?}
11	
12	We propose a \emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Fa
…[truncated 5968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-16T19:39:51.214740+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-16T19:39:51.766338+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically across the environment (\S\ref{sec:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment $\mathcal{E}$ with state space $\mathcal{S}$, observation space $\mathcal{O}$, and action space $\mathcal{A}$. An agent follows a policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ that maps observation histories to actions. At each step $t$, the agent receives observation $o_t$, selects action $a_t = \pi(o_1, \ldots, o_t)$, and the environment transitions to state $s_{t+1}$.
10	
11	We define a modality set $\mathcal{M} = \{{\tt int}, {\tt det}\}$ governing how the agent processes state transitions:
12	\begin{itemize}
13	    \item \textbf{Internal} ($m = {\tt int}$): The agent uses its own generation to predict intermediate observations. The LLM interleaves chain-of-thought reasoning with environment actions following the ReAct paradigm \cite{react-2023}, but prediction errors compound across steps.
14	    \item \textbf{Deterministic} ($m = {\tt det}$): The agent receives ground-truth observations from the environment simulator at each step---equivalent to access to a perfect dynamics model. Action selection remains with the LLM; only the state-transition prediction is replaced.
15	\end{itemize}
16	
17	\noindent We restrict $\mathcal{M}
…[truncated 11269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 551
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-16T19:39:51.867040+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "decisions.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-16T19:39:51.917719+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 97\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-determinist
…[truncated 3539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-16T19:39:58.149726+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-16T19:39:58.653257+00:00_

1	\section{Experiments}
2	
3	\subsection{Death Avoidance Decomposition}
4	\label{sec:death-decomp}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/fig1_daf_scatter.pdf}
9	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types.}
10	\label{fig:decomposition}
11	\end{figure}
12	
13	Across 245 episodes, $\Delta_{\text{full}} = +29.60$; excluding death episodes, $\Delta_{\text{nd}} = +2.84$, yielding DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$; at default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\% (75 of 95 non-tie labels). The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$). Per-task, death rate differential correlates with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}). However, when $P$ is constant across tasks, $\text{Corr}(P \cdot \delta + \Delta_{\text{nd}},\; \delta) \rightarrow 1$ as DAF $\rightarrow 1$; controlling for $\delta \cdot P$, the residual is $r = 0.02$ ($p = 0.91$, $df = 27$). We retain $r = 0.97$ as an internal consistency check, not as independent evidence for death avoidance. The correlation drops below significance at $P \leq 25$ (Appendix~\ref{app:penalty}). Of 245 episodes, 86 are \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}.
14	
15	\paragraph{Signal concentration.}
16	The SCI (\S\ref{sec:sci}) over per-task routing signal contributions is $0.2147$ (low concentration): the top-3 task types account for only $39.8\%$ of total death-rate differential. One outlier, \texttt{find-non-living-thing}, has zero deaths (DAF $= 0\%$, $\Delta = +9.58$ from non-death scores); all 10 remaining types exhibit DAF $= 100\%$. Death avoidance is systematic, not driven by a few outlier tasks.
17	
18	\paragraph{Bootstrap confidence intervals.}
19	Episode-level b
…[truncated 4562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-16T19:39:58.653628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-16T19:39:58.904631+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Cross-environment evidence.}
5	On ALFWorld ($N{=}135$), the framework identifies a qualitatively different mechanism: information asymmetry (access to admissible actions, reversible navigation failures) rather than death avoidance (Appendix~\ref{app:cross-env}). Neither MATH nor ALFWorld validates DAF quantitatively---true replication requires a second catastrophic-failure environment (e.g., NetHack, Crafter). These cross-domain contrasts demonstrate framework applicability, not universality of the death-dominance finding.
6	
7	\paragraph{Penalty sensitivity and correlation structure.}
8	The $r = 0.97$ correlation is specific to catastrophic death ($P{=}100$); defining failure as any non-positive score yields $r = -0.13$ ($p = 0.70$). As shown in \S\ref{sec:death-decomp}, this correlation is largely a mathematical consequence of death dominance (partial $r = 0.02$). Death is effectively the only component generating differential routing signal; the 42.9\% internal death rate reflects 7B-scale hallucination vulnerability, and larger models with lower death rates would reduce DAF.
9	
10	\paragraph{Implications for router design.}
11	Death avoidance dominance (78.9\% of non-tie labels, DAF $= 90.4\%$ at $P{=}100$) reframes modality routing as a \emph{safety} problem---closer to a conservative default policy than to cost-quality optimization~\citep{garcia2015comprehensive, cogrouter-2026}. The 86:9 label imbalance explains why always-deterministic is a strong baseline. The capacity scaling results reinforce this: 4B parameters for $+9$\,pp validates our analytical methodology over brute-force learned routing. An untested but predictive ablation: augmenting the internal strategy with state verification (querying the environment to confirm transitions) should drive DAF toward zero, shifting routing signal from failure prevention to other factors---illustrating the framework's diagnostic utility beyond measure
…[truncated 565 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 250
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-16T19:39:58.955323+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-16T19:39:59.006964+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}.
5	Toolformer \cite{toolformer-2023} teaches LLMs to insert API calls via self-supervised loss filtering; ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens enabling frozen models to invoke massive tool libraries; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask; ReTool \cite{retool-2025} applies RL to discover when code execution is preferable to chain-of-thought.
6	These focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Recent concurrent work sharpens this question: \citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect in LLM tool use, \citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \citet{tool-use-tax-2026} quantify a ``tool-use tax'' where tools degrade performance, and \citet{to-call-or-not-2026} propose a necessity--utility--affordability framework.
8	Our counterfactual decomposition provides environment-grounded evidence: in ScienceWorld, $90.4\%$ of routing signal at $P{=}100$ traces to catastrophic-failure prevention.
9	
10	\paragraph{Adaptive Computation and Routing.}
11	CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing across heterogeneous models.
12	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
13	These optimize \emph{how} to route; we reveal \emph{why} routing helps---in interactive environments, the dominant signal is catastrophic-failure avo
…[truncated 1819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-16T19:40:04.705687+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-16T19:40:04.756427+00:00_

1	\section{Conclusion}
2	
3	We introduced a formal diagnostic framework---episode-level counterfactual analysis with the DAF metric---for decomposing routing signal in modular LLM agents. Applied to 245 ScienceWorld episodes (11 of 30 task types, Qwen2.5-7B-Instruct), 78.9\% of non-tie routing labels (75 of 95, penalty-independent) arise from death asymmetry; under ScienceWorld's penalty ($P{=}100$), DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$). The per-task correlation $r = 0.97$ serves as an internal consistency check (partial $r = 0.02$ after controlling for $\delta \cdot P$), confirming the decomposition correctly identifies death as the dominant term.
4	
5	Cross-domain contrasts demonstrate framework applicability: on MATH ($N{=}300$), death-avoidance signal is absent as predicted ($+4.3$~pp, $p = 0.079$, underpowered at 0.42). A Llama-3.1-8B-Instruct replication (7 task types, 70 episodes) confirms directional consistency of the death mechanism across model families ($+34.3\%$ vs.\ $+26.6\%$). An exploratory router yields an informative negative: episode-level balanced accuracy remains at or below chance at practical scales, reaching $59.0\%$ only at 4B---a disproportionate cost that validates the analytical framework.
6	
7	Our findings are specific to environments with binary catastrophic outcomes (death/survival); applicability to environments with graded penalties or continuous failure modes requires further investigation. In such environments, routing value is dominated by safety: the routing problem reduces to safety-first modality selection rather than efficiency optimization. Open directions include step-level counterfactual labeling, quantitative replication in a second catastrophic-failure environment (e.g., NetHack), and stronger backbones with lower intrinsic death rates (which our framework predicts will lower DAF).
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-16T19:40:05.009174+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-16T19:40:05.110168+00:00_

&lt;persisted-output>
Output too large (21.1KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing--claude-sessions-review-director-19d7e797/6e4b3169-0193-4a4e-8a7e-330c0a19f6ca/tool-results/toolu_011TGvABFp8VarZTewfwUKbz.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_9.md:156:外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_8.md:102:外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_f6bffc7e8351600df8091f08a63cd5a0_director.jsonl:116:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/archive/feishu_group_oc_f6bffc7e8351600df8091f08a63cd5a0_director_20260516T131900_208238.jsonl:922:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_0b622d6038b969b96148ee8a163a1a0c_director.jsonl:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_0b622d6038b969b96148ee8a163a1a0c_director.jsonl:17:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_0b622d6038b969b96148ee8a163a1a0c_director.jsonl:54:{"ts": "2026-05-14T12:31:21.871157+00:00", "role": "tool", "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director", "text": "called mcp__agent-ml-research__get_external_review_status", "tool": "mcp__agent-ml-research__get_external_review_status", "tool_args": {"project": "simgate-modular-routing"}}
...
</persisted-ou
…[truncated 5 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-16T19:40:10.234141+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-16T19:40:10.234583+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-16T19:40:14.523210+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_external_review_status",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-16T19:40:14.523651+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 762 · 2026-05-16T19:40:15.479160+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-16T19:40:15.930977+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-16T19:40:16.081771+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-16T19:40:16.132405+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 766 · 2026-05-16T19:40:19.548625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-16T19:40:19.900981+00:00_

1	- id: "R6-C1"
2	  summary: "DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not primary"
3	  category: method
4	  severity: critical
5	  status: in_progress
6	  first_raised_round: 4
7	  last_seen_round: 9
8	  mentions:
9	    - round: 6
10	      reviewers: [1, 2]
11	      note: "Fresh reviewers want full range + formula + dual reporting."
12	    - round: 7
13	      reviewers: [1, 2]
14	      note: "Resurfaced. Abstract still leads with DAF=90.41%. 78.9% present but not co-equal."
15	    - round: 8
16	      reviewers: [1, 2]
17	      note: "Both reviewers confirm RESOLVED. 78.9% now appears co-equal with DAF throughout."
18	    - round: 9
19	      reviewers: [1, 2]
20	      note: "REOPENED. R9 reviewers argue DAF=90.4% remains headline despite co-equal presentation. Core issue: DAF = δP/(δP + Δ_nd) is monotonic in P — 90.4% at P=100 approaches tautology. Want 78.9% as PRIMARY metric, DAF as parametric companion."
21	  action_items:
22	    - round: 6
23	      action: "Abstract/Intro/§3.3/Conclusion dual reporting + DAF(P) formula"
24	      assigned_to: main_agent
25	      status: done
26	    - round: 7
27	      action: "Promote 78.9% to primary metric"
28	      assigned_to: main_agent
29	      status: done
30	    - round: 9
31	      action: "78.9% as sole PRIMARY headline; DAF demoted to §3.4 decomposition tool with P-specificity caveat. Abstract leads with 78.9%, DAF mentioned as 'under P=100, corresponds to DAF=90.4%'."
32	      assigned_to: paper_agent
33	      status: in_progress
34	  resolution: ""
35	  resolution_round: null
36	
37	- id: "R6-W1"
38	  summary: "r=0.97 structural coupling — qualifier insufficient in Abstract/Conclusion"
39	  category: writing
40	  severity: critical
41	  status: in_progress
42	  first_raised_round: 6
43	  last_seen_round: 9
44	  mentions:
45	    - round: 6
46	      reviewers: [1, 2]
47	      note: "High r partly mathematical due to penalty coupling."
48	    - round: 7
49	      reviewers: [1, 2]
50	      note: "Re
…[truncated 27978 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-16T19:40:19.901461+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_9.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_9.md"
  }
}
```

</details>

---


### Tool result

_source line 769 · 2026-05-16T19:40:19.952299+00:00_

1	---
2	round: 9
3	overall_score: borderline
4	timestamp: 2026-05-16T19:18:18.129634+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# Round 9 审稿报告 — simgate-modular-routing
11	
12	**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
13	**Venue**: EMNLP 2026 Main Conference Long Paper (ARR May cycle)
14	**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）
15	**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达共识）
16	
17	---
18	
19	## Summary
20	
21	本文提出 episode-level counterfactual analysis 框架和 Death Avoidance Factor (DAF) 指标，分解 modular LLM agent 的 routing signal 来源。在 ScienceWorld（11/30 task types, N=245, Qwen2.5-7B-Instruct）上发现 78.9% 的 non-tie routing labels 由 death asymmetry 驱动，DAF=90.4%（P=100）。Trained router 在 held-out episodes 上低于 chance baseline（47.1% vs 50%）。跨环境分析（MATH N=300, ALFWorld N=135）和跨模型复制（Llama-3.1-8B, N=70）提供辅助证据。
22	
23	---
24	
25	## Strengths
26	
27	**S1. 问题定位精准。** 在 routing 文献集中于"如何 route"时，退后一步问"什么驱动 routing signal"——是被忽视的元问题，具有方法论价值。
28	
29	**S2. 框架设计简洁可复现。** Algorithm 1 完备无歧义，仅需 paired episode outcomes，environment-agnostic 属性通过三个结构迥异环境得到演示。
30	
31	**S3. 统计报告诚实严谨。** p=0.079 始终标注 "not reaching α=0.05"，r=0.97 标注 "partly structural"，Bootstrap/LOO/Spearman 三重 robustness，8-seed cross-split evaluation。
32	
33	**S4. 多层次 robustness 检验。** LOO (r: 0.963-0.980), Spearman ρ=0.986, 10K bootstrap, penalty sweep (P=10-500), reasoning-depth ablation, data scaling (25%-800%), capacity scaling (0.6B-4B), cross-model replication。
34	
35	**S5. Negative result 呈现诚实且有建设性。** Router diagnostic 清晰展示 always-deterministic 的 trivial near-optimality，对社区有建设性信息。
36	
37	**S6. Limitations 坦诚具体。** 19/30 exclusion, penalty amplification, single-pass ReAct, distribution shift (DAgger), 7-8B scale limitation 均明确列出。
38	
39	---
40	
41	## Weaknesses
42	
43	### Must-Fix (Critical)
44	
45	**W1. DAF=90.4% headline number 被 penalty magnitude 机械放大 [Consensus]**
46	- DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数。在 P=100
…[truncated 8155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-16T19:41:42.010704+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。\n\n**论文信息：**\n- 标题: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- 路径: projects/simgate-modular-routing/docs/paper/main.tex（含 abstract.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, conclusion.tex）\n- Venue: EMNLP 2026 Main Conference Long Paper\n- 格式要求: ACL style, 正文 8 页, double-blind, 必须有 Limitations section\n- Deadline: 2026-05-25 (ARR May cycle)\n\n**你的审查侧重：**\n1. DAF 指标的数学定义是否自洽、是否存在 penalty-dependence 导致的 claim inflation\n2. 统计推断：bootstrap CI 的适用性、partial correlation 的正确性、power analysis 报告\n3. Router diagnostic 实验：data scaling ablation 方法论是否有效、capacity scaling 非单调性的解释\n4. Counterfactual labeling (Algorithm 1) 的完备性和 edge case 处理\n5. Cross-model/cross-env 实验的 evidence strength：是否支持所做 claim\n6. 格式合规性：页数、匿名、Limitations section\n\n请按 EMNLP 2026 标准（soundness、excitement、reproducibility）独立给出完整审稿意见。结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Nice-to-Fix) → Questions → Missing References → Overall Score (1-5)。",
  "project": "simgate-modular-routing",
  "chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c",
  "director_session_key": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查**方法严谨性 + 实验设计**。\n\n**论文信息：**\n- 标题: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- 路径: projects/simgate-modular-routing/docs/paper/main.tex（含 abstract.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, conclusion.tex）\n- Venue: EMNLP 2026 Main Conference Long Paper\n- 格式要求: ACL style, 正文 8 页, double-blind, 必须有 Limitations section\n- Deadline: 2026-05-25 (ARR May cycle)\n\n**你的审查侧重：**\n1. DAF 指标的数学定义是否自洽、是否存在 penalty-dependence 导致的 claim inflation\n2. 统计推断：bootstrap CI 的适用性、partial correlation 的正确性、power analysis 报告\n3. Router diagnostic 实验：data scaling ablation 方法论是否有效、capacity scaling 非单调性的解释\n4. Counterfactual labeling (Algorithm 1) 的完备性和 edge case 处理\n5. Cross-model/cross-env 实验的 evidence strength：是否支持所做 claim\n6. 格式合规性：页数、匿名、Limitations section\n\n请按 EMNLP 2026 标准（soundness、excitement、reproducibility）独立给出完整审稿意见。结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Nice-to-Fix) → Questions → Missing References → Overall Score (1-5)。",
    "project": "simgate-modular-routing",
    "chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c",
    "director_session_key": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-16T19:41:49.699564+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 7688
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-16T19:41:50.553787+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查**新���性 + 完整性**。\n\n**论文信息：**\n- 标题: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- 路径: projects/simgate-modular-routing/docs/paper/main.tex（含 abstract.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, conclusion.tex）\n- Venue: EMNLP 2026 Main Conference Long Paper\n- 格��要求: ACL style, 正文 8 页, double-blind, 必须有 Limitations section\n- Deadline: 2026-05-25 (ARR May cycle)\n\n**你的审查侧重：**\n1. Contribution novelty：counterfactual framework + DAF metric 是否对社区有足够新的 insight\n2. Related work coverage：tool-use routing (Toolformer/ART/Chameleon/ReTool/RouteLLM)、adaptive computation (CogRouter/ARES)、safe RL、counterfactual RL 文献是否充分\n3. Cross-environment evidence：MATH + ALFWorld + Llama replication 是否充分支持 generalization claim\n4. 论文完整性：是否有遗漏的 ablation/baseline/analysis、Limitations 是否诚实全面\n5. Writing quality：organization、clarity、terminology consistency\n6. Contribution sizing：对 EMNLP 主会来说，contribution 是否足够（vs Findings track）\n\n请按 EMNLP 2026 标准（soundness、excitement、reproducibility）独立给出完整审稿意见。结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Nice-to-Fix) → Questions → Missing References → Overall Score (1-5)。",
  "project": "simgate-modular-routing",
  "chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c",
  "director_session_key": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查**新���性 + 完整性**。\n\n**论文信息：**\n- 标题: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- 路径: projects/simgate-modular-routing/docs/paper/main.tex（含 abstract.tex, introduction.tex, method.tex, experiments.tex, discussion.tex, related_work.tex, conclusion.tex）\n- Venue: EMNLP 2026 Main Conference Long Paper\n- 格��要求: ACL style, 正文 8 页, double-blind, 必须有 Limitations section\n- Deadline: 2026-05-25 (ARR May cycle)\n\n**你的审查侧重：**\n1. Contribution novelty：counterfactual framework + DAF metric 是否对社区有足够新的 insight\n2. Related work coverage：tool-use routing (Toolformer/ART/Chameleon/ReTool/RouteLLM)、adaptive computation (CogRouter/ARES)、safe RL、counterfactual RL 文献是否充分\n3. Cross-environment evidence：MATH + ALFWorld + Llama replication 是否充分支持 generalization claim\n4. 论文完整性：是否有遗漏的 ablation/baseline/analysis、Limitations 是否诚实全面\n5. Writing quality：organization、clarity、terminology consistency\n6. Contribution sizing：对 EMNLP 主会来说，contribution 是否足够（vs Findings track）\n\n请按 EMNLP 2026 标准（soundness、excitement、reproducibility）独立给出完整审稿意见。结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Nice-to-Fix) → Questions → Missing References → Overall Score (1-5)。",
    "project": "simgate-modular-routing",
    "chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c",
    "director_session_key": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
  }
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-16T19:41:51.761581+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1207
}
```

</details>

---


### Assistant

_source line 774 · 2026-05-16T19:41:56.674573+00:00_

Round 1 已分配：
- Reviewer 1（方法严谨性+实验设计）✓
- Reviewer 2（新颖性+完整性）✓

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 72

## Round 72

2 recorded events


### User

_source line 775 · 2026-05-16T19:46:10.319071+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**侧重**: Contribution novelty + 完整性

---

## Summary

本文提出一个诊断框架（episode-level counterfactual analysis + Death Avoidance Factor metric）用于分解 modular LLM agent 中 routing signal 的来源。在 ScienceWorld（11/30 task types, 245 episodes, Qwen2.5-7B）上发现 78.9% 的非平局 routing labels 来自 death asymmetry（DAF=90.4% at P=100）。辅以 MATH（300 problems, negative contrast）、ALFWorld（135 games, different mechanism）和 Llama-3.1-8B 复现（70 episodes）。一个探索性 router 在 episode-level 上未超过 always-deterministic baseline，作者将此解读为验证分析框架优于暴力学习路由。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法严谨（bootstrap, LOO, partial correlation），但核心发现受限于单一环境+高惩罚设定，generalization 证据不充分 |
| Excitement / Novelty | 2.5/5 | 框架本身有方法论价值，但核心发现接近 tautology（大惩罚+高死亡率差异→死亡主导分数差异） |
| Reproducibility | 4/5 | 实验细节充分，hyperparameters 明确，承诺代码开源；但部分实验 seed 数量偏少 |
| Reviewer Confidence | 4/5 | 熟悉 LLM agent、tool-use routing、safe RL 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心发现的 novelty 不足——接近 tautological consequence

- 具体位置：Section 4.1, Appendix E (penalty sensitivity)
- 问题：论文的核心发现可以重新表述为："在一个 death penalty = -100 的环境中，如果一个策略死亡率是另一个的 2.6 倍，那么死亡惩罚主导了两策略的分数差异。" 这几乎是数学上的必然结果，而非经验发现。作者自己在多处承认这一点——partial r = 0.02 after controlling for δ·P (Section 4.1)、"mathematical consequence, not an empirical finding" (Appendix E)、DAF = δP/(δP + Δ_nd) 是单调递增函数——但 contribution framing 仍然将其包装为一个 surprising discovery。
- 为什么影响接收：EMNLP main conference 需要 sufficient novelty/insight。如果核心 "发现" 可以在不做实验的情况下从环境参数推导出来，contribution 的 insight 含量不足以支撑 main conference 接收。
- 建议修改方向：(1) 明确区分 framework contribution（方法论，如何量化）和 empirical contribution（经验发现，在哪里适用）；(2) 将 novelty 重心转移到 "78.9% death-asymmetry label fraction" 这个 penalty-independent metric 以及 "internal strategy 的 42.9% 死亡率从何而来"（hallucination → cascading error → death），因为后者是真正的经验发现；(3) 在第二个 catastrophic-failure 环境中验证。

**N2** [critical] 单一环境证据不足以支撑 generalization claim

- 具体位置：Contribution 3 (Introduction lines 41-43), Discussion Section 5, Conclusion
- 问题：论文 claim "framework applicability" 和 "cross-context applicability"，但：(a) MATH 是 negative contrast（无 death penalty），power=0.42，不达 α=0.05；(b) ALFWorld 无 death penalty，展示的是 different mechanism；(c) Llama 复现仅 70 episodes / 7 tasks，direction-only。没有任何一个 cross-environment check 实际 REPLICATES 了 death-dominance finding。论文自己在 Discussion (line 5) 承认 "true replication requires a second catastrophic-failure environment (e.g., NetHack, Crafter)"。
- 为什么影响接收：Abstract 和 Contribution 3 的措辞暗示 cross-environment generalizability，但实际证据只有 ScienceWorld 一个环境。对 EMNLP 读者而言，一个环境的发现（特别是一个不常用的评估环境）的影响力有限。
- 建议修改方向：(1) 在 NetHack 或 Crafter 中复现 DAF 分析（哪怕 pilot-scale 50-100 episodes）——这将显著提升贡献的 convincingness；(2) 或者收缩 claim 到 "ScienceWorld-specific finding + framework proposal"，将 contribution sizing 明确定位为 Findings track。

**N3** [critical] "Deterministic modality" 定义与文献中的 tool-use routing 脱节

- 具体位置：Section 3.1 (Problem Setup), modality definition
- 问题：论文的 "deterministic" modality 是 "ground-truth observations from the environment simulator"——本质上是 oracle state provider。但文献中的 tool-use routing（Toolformer, RouteLLM, ReTool, Chameleon）指的是 API 调用、code interpreter、search engine 等——这些工具不提供 ground-truth state，也会出错。论文在 Introduction 中将自己的工作定位为回答 "what drives the value of routing decisions"，并引用 Toolformer/ART/Chameleon 作为 motivation，但实验中的 "routing" 与这些工作所研究的 routing 是不同问题。
- 为什么影响接收：如果读者期望本文的 finding 能 inform 实际的 tool-use routing design（如 "when to call calculator vs. reason internally"），会发现本文的设定（oracle state access vs. no state access）与现实场景差距过大。MATH experiment 中使用 code interpreter 更接近真实 tool-use，但结果是 non-significant。
- 建议修改方向：(1) 在 Introduction/Related Work 中明确区分本文的 "modality routing"（access to perfect dynamics model）与 standard tool-use routing（access to imperfect tools）；(2) 讨论 finding 对实际 tool-use routing 设计的可迁移性——death avoidance 机制在 imperfect tool 设定下是否依然成立？

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Router failure 不能直接 "validate" analytical framework

- 具体位置：Section 4.5, Contribution 2 (Introduction line 39), Conclusion line 5
- 问题：论文多次声称 router 的 episode-level 失败 "validates the analytical framework over brute-force learned routing"。但一个特定架构（Qwen3-1.7B SFT + LoRA）在一个特定训练配置下失败，逻辑上不能证明分析框架的优越性。论文没有尝试：(a) task-type classifier 作为 router（既然论文承认 signal = task type，Section Appendix D line 3）；(b) 直接的 death-risk predictor；(c) 更大规模 real-data collection（而非 paraphrase augmentation）。4B 达到 59%，趋势明显，但被定性为 "disproportionate cost"——这是 value judgment 而非 empirical conclusion。
- 建议：(1) 弱化 "validates" 用词，改为 "consistent with"；(2) 加入 task-type oracle router baseline——如果 routing signal = task type，一个 task-type classifier 就是 upper bound。

**W2** [warning] Related work 有明显遗漏

- 具体位置：Section 6 (Related Work)
- 问题：
  - 缺少 AgentBench (Liu et al., ICLR 2024)——标准 multi-environment LLM agent benchmark，直接相关且在 ScienceWorld 的同类环境上有评估
  - 缺少 LATS (Zhou et al., ICML 2024)——Language Agent Tree Search，将 reasoning + acting + planning 统一为搜索问题，与 routing decision 高度相关
  - 缺少 hallucination detection/mitigation 文献（SelfCheckGPT, FActScore 等）——论文的核心机制是 "hallucination → death"，但未引用 hallucination 文献
  - Safe RL 部分过于单薄（仅 Garcia 2015 survey + CRPO 2021），缺少 recent constrained RL（CPO, FOCOPS）和 safe LLM agent 特定文献（SafeRLHF, Constitutional AI 中的 safety constraint）
- 建议：补充上述引用并讨论本文方法与这些工作的关系。

**W3** [warning] Task selection bias 未充分 quantify

- 具体位置：Section 3.2, Appendix B (Per-Task Decomposition)
- 问题：排除 63% 的 ScienceWorld task types（19/30）因为 "both strategies time out"。Appendix B 声称 "deterministic-strategy death rate is comparable between included (17.8%) and excluded (14.9%)"，但这只比较了一个维度。被排除的 tasks 可能有不同的 hallucination patterns、不同的 action space complexity、不同的 death trigger mechanism。在只分析 37% tasks 的情况下声称 "SCI = 0.2147 indicates systematic phenomenon" 存在 survivorship bias。
- 建议：(1) 至少报告 excluded tasks 的基本统计特征（step budget 耗尽比例、平均 episode length）；(2) 用更大 step budget（50-100 steps）对 2-3 个 excluded tasks 做 pilot test，看是否出现不同 pattern。

**W4** [warning] MATH evaluation 的 modality definition inconsistency

- 具体位置：Section 4.3 (Cross-Domain Negative Contrast: MATH)
- 问题：在 ScienceWorld 中，"deterministic" = ground-truth observations（oracle state）。在 MATH 中，"deterministic" = code interpreter（imperfect tool，可能报错）。这不是同一个 modality definition。论文在 Discussion 中辩称 "deliberate heterogeneity... tests whether the framework generalizes"，但 framework 声称分解的是 "routing signal between two modalities"——如果两个 modality 的定义在环境间不一致，cross-environment comparison 的意义被削弱。
- 建议：明确承认 modality 定义的异质性是一个 threat to validity，不要将 MATH 结果等同于 "framework replication"。

---

## 小问题（不影响接收）

- Abstract 过于数字密集（5 个百分比 + 3 个 p-value + CI），建议精简到 1-2 个关键数字，将 insight 放在前面
- SCI metric (Section 3.5) 引入后仅使用一次（Section 4.1 一段话），对论文贡献的边际收益不大，可以考虑移到 Appendix
- Table 3 (baselines) 中 "Trained Router" 是 single seed，与其他 8-seed 结果不一致，应标注或补充
- Section ordering unusual：Related Work 在 Experiments 之后，虽然 ACL 允许但影响阅读流畅度
- "Oracle degeneracy" 一词未定义——首次使用时应给出形式化定义（oracle 97% 匹配 always-det）
- Contribution 2 (Introduction) 中 "capacity-dependent limitation; scaling to 4B yields 59.0%" 与 Contribution 1 的 framework claim 混在一起，建议分离

---

## Questions to Authors

1. 在 death-asymmetry 的 75 个 labels 中，有多少 episodes 的 internal strategy 即使未死也会输给 deterministic（即 score comparison 也会给出相同 label）？这可以量化 death-asymmetry labeling 的 "redundancy"。
2. 为什么不在 NetHack / Crafter 中做 50-100 episodes 的 pilot replication？这是 claim generalizability 的最直接验证。
3. 如果用 task-type 作为 routing feature（one-hot），router 的 episode-level accuracy 是多少？这是 "routing signal = task type" claim 的直接验证。
4. 30-step budget 的选择依据是什么？如果增加到 100 steps，internal strategy 的 death rate 是否会收敛（hallucination 会在前几步暴露还是均匀分布）？
5. Larger models (70B+) 的 hallucination rate 更低，预测 DAF 应降低——能否提供任何 evidence（哪怕 anecdotal）？

---

## Missing References

- Liu et al. (2024). "AgentBench: Evaluating LLMs as Agents." ICLR 2024. — 标准 multi-environment agent benchmark，直接相关
- Zhou et al. (2024). "Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models." ICML 2024. — routing/planning 统一框架
- Manakul et al. (2023). "SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection." EMNLP 2023. — hallucination detection，直接相关本文的 "hallucination → death" 机制
- Min et al. (2023). "FActScore: Fine-grained Atomic Evaluation of Factual Precision." EMNLP 2023. — factuality evaluation
- Dai et al. (2024). "Safe RLHF: Safe Reinforcement Learning from Human Feedback." ICLR 2024. — safe LLM alignment，与 safety-first routing 相关
- Qin et al. (2024). "ToolBench: Broad Evaluation of LLM Tool Utilization." ICLR 2024. — tool-use benchmark

---

## 主要优势

- 研究问题 well-motivated：回答 "what drives routing signal" 比 "how to learn routing" 更基础
- 方法论严谨：bootstrap CI、partial correlation、penalty sensitivity、LOO robustness、data scaling ablation 面面俱到
- 诚实的 negative result：router 在 episode-level 失败，paper 如实报告并深入分析原因
- Labeling quality audit (Appendix A) 消除了 oracle circularity concern
- 对自身发现的 limitations 有清醒认识（partial r=0.02 的 "mathematical consequence" 表述、penalty-independent metric 的补充报告）
- 写作清晰，notation 一致，算法和表格 well-organized

---

## Overall Score

**Overall**: 3.0 / 5 — Findings track acceptance recommended

**一句话总结**: 框架设计扎实、统计严谨，但核心经验发现（death dominates routing signal in high-penalty environments）接近 tautological，且仅有单一环境证据，novelty 和 generalizability 不足以支撑 EMNLP main conference。如果在第二个 catastrophic-failure 环境中复现 + 明确与 real tool-use routing 的关系，可提升至 main conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 776 · 2026-05-16T19:46:18.315078+00:00_

已收到 Reviewer 2 的审稿意见（Overall 3.0/5，推荐 Findings track）。等待 Reviewer 1 的审稿意见返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 73

## Round 73

6 recorded events


### User

_source line 777 · 2026-05-16T19:46:19.267932+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — Round 1

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 Main Conference (ACL ARR May cycle)
**审查侧重**: 方法严谨性 + 实验设计

---

## Summary

本文提出了一个形式化的诊断框架（episode-level counterfactual analysis + Death Avoidance Factor），用于分解模块化 LLM agent 中 routing signal 的来源。在 ScienceWorld（11/30 task types, 245 episodes, Qwen2.5-7B）上，78.9% 的 non-tie routing labels 来自 death asymmetry；在默认 penalty P=100 下 DAF = 90.4%。一个 exploratory router 在 episode-level 表现低于 chance，佐证了 analytical framework 的价值。Cross-model (Llama-3.1-8B, N=70) 和 cross-domain (MATH N=300, ALFWorld N=135) 对比提供方向性支持。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心框架自洽，但 partial correlation df 有误、data scaling ablation 方法论存疑、capacity scaling confound 未控制 |
| Excitement | 2.5/5 | 诊断性发现有价值但 scope 窄、actionable insight 有限；框架本身方法论贡献中等 |
| Reproducibility | 3.5/5 | 超参全报告、algorithm 清晰，但无匿名代码/数据补充材料 |

---

## 总体评分

**Overall**: 2.5 — Resubmit next cycle (接近 borderline，需要实质性修改)

**一句话总结**: 方法论设计良好且诚实，但核心 claim 的 penalty-dependence 与统计细节错误削弱了可信度，实验证据的 scope 不足以支撑 main conference。

---

## 主要优势

1. **自我批判诚实**: 主动报告 partial r=0.02 暴露 r=0.97 的数学必然性，报告 router 负面结果，标注 power analysis 不足。这在 LLM agent 论文中罕见。
2. **框架设计清晰**: Algorithm 1 覆盖所有 case，penalty-independent (78.9% label fraction) 与 penalty-dependent (DAF) 两个互补指标的区分有思考。
3. **Bootstrap CI 使用正确**: 在 episode-level 重采样，尊重了 episode 内 step 之间的依赖结构。
4. **负面结果有价值**: router 训练失败本身是有信息量的 diagnostic（always-det 是 trivially near-optimal）。
5. **Limitations section 实质性强**: 几乎所有重要 caveat 都被主动提及，包括 step budget、internal baseline 局限、分布偏移。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Partial correlation df=27 统计错误
- 具体位置：Section 4.1 (experiments.tex line 13): "controlling for δ·P, the residual is r = 0.02 (p = 0.91, df = 27)"
- 问题：散点图有 n=11 task types。Partial correlation controlling for 1 variable 的自由度应为 n - 2 - 1 = 8，不可能是 27。若在 episode-level 计算（N=245），controlling for δ·P 本质上等于 controlling for task identity（因为 P 恒定，δ 是 per-task 常量），会膨胀 df 并改变统计解释。
- 为什么影响接收：这是方法论诚实性的关键数据点——用来说明 r=0.97 是 mathematical artifact。如果 df 有误，p-value 可能也不对，影响该论证成立与否。
- 建议修改方向：明确说明计算 level（task-level vs episode-level）；若 task-level，df 应为 8；若 episode-level，必须解释为什么在 episode-level controlling for a task-level constant 是有效的。

**N2** [critical] Data scaling ablation 的方法论缺陷
- 具体位置：Appendix D (main.tex lines 195-218), Section 4.5 (experiments.tex line 59): "Augmentation-based data scaling (25%–800%) provides no improvement"
- 问题：Paraphrase augmentation (synonym substitution + template variation) 不等同于 real data scaling。论文自己承认 augmentation 将 majority class 从 89.6% 膨胀到 97.7%，且"without generating novel routing patterns"。但仍得出结论 "rules out step-level data scarcity"——这个结论过强。Augmentation 仅能说明 surface-level paraphrase diversity 不帮忙，不能排除更多 *真实* episode pairs 是否有帮助。
- 为什么影响接收：这是 "router failure is structural" 这一核心 claim 的关键支撑之一。如果此 ablation 无法排除 data scarcity，"structural limitation" 的结论需要降级为 "at current data scale, the router cannot learn"。
- 建议修改方向：(1) 将结论弱化为 "augmentation-based scaling does not help; real-data scaling requires ~1,350 episodes and remains open"; (2) 或者至少做一个 leave-K-task-types-out 的 cross-task generalization test 作为 structural limitation 的更直接证据。

**N3** [critical] Capacity scaling non-monotonicity 的 confound 未控制
- 具体位置：Appendix F (main.tex lines 286-306), experiments.tex line 59
- 问题：Episode-level accuracy 为 0.6B: 50.7%, 1.7B: 47.1%, 4B: 59.0%。论文承认 "configuration differences—8 vs. 4 seeds—may contribute"（Table 8 caption）。具体来说，1.7B 用 8 cross-split seeds 训练和评估，0.6B/4B 用 4 seeds。这意味着 1.7B 的 47.1% 和 4B 的 59.0% 不直接可比。Non-monotonicity 可能是 seed/split 配置差异的 artifact。
- 为什么影响接收："only 4B exceeds the baseline" 是论文的 key claim 之一（validate analytical methodology over brute-force routing）。如果 1.7B 在 4-seed 配置下也能达到 55%+，整个 narrative 就不同了。
- 建议修改方向：在完全相同的配置（相同 seed 数、相同 split 策略）下重新跑 0.6B/1.7B/4B，或者至少报告 1.7B 在 4-seed 配置下的数字。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Bootstrap 未考虑 cluster structure
- 具体位置：Section 3.4 (method.tex lines 116-118), Section 4.1 (experiments.tex line 19)
- 问题：Episode-level bootstrap 从 245 episodes 中有放回抽样。但 episodes within the same task type 共享 task structure（相同环境动力学、相同 death risk profile），不是独立的。Cluster bootstrap（在 task-type level 重采样 11 clusters）会产生更宽但更诚实的 CI。当前 CI [81.6%, 98.8%] 可能 over-confident。
- 建议：报告 cluster bootstrap CI 作为 sensitivity analysis。如果宽很多，需要在正文讨论。

**W2** [warning] Cross-model 证据过弱
- 具体位置：Section 4.2 (experiments.tex lines 22-24), Appendix E (main.tex lines 273-276)
- 问题：Llama-3.1-8B, 7 task types, N=70, 0 internal-preferred episodes。这只能说明 "another 7-8B model also dies more often in internal mode"——一个 unsurprising observation for any hallucination-prone model。更有价值的验证是：(1) 更大模型（70B），预测 DAF 下降；(2) 更强 internal baseline（Reflexion），测试 death rate 能否降低。
- 建议：至少承认当前 cross-model evidence 仅覆盖 "similar-capability models"，并将 "larger models lower DAF" 作为 testable prediction 而非 merely acknowledged limitation。

**W3** [warning] MATH 实验 underpowered 且 claim 过强
- 具体位置：Section 4.3 (experiments.tex lines 27-29)
- 问题：Power = 0.42, p = 0.079。论文称 "consistent with the framework's prediction that death-avoidance signal should be absent"——但 42% power 的 non-significant result 几乎是 uninformative（Type II error probability = 58%）。这不能作为 "framework prediction validated" 的证据，只能说 "inconclusive"。
- 建议：严格降级为 "our MATH evaluation is underpowered and therefore inconclusive; the directional trend (+4.3pp favoring internal) is consistent with but does not confirm the framework's prediction"。

**W4** [warning] Algorithm 1 的隐含假设未讨论
- 具体位置：Section 3.3 (method.tex lines 59-94)
- 问题：(1) "Both dead → no preference" 假设所有死亡等价，但不区分 early death (step 2) vs late death (step 28)——后者可能已积累大量有用经验。(2) Score comparison 不设 minimum meaningful difference：如果 det 得 32、int 得 31，这是 meaningful routing signal 还是 noise？ScienceWorld 是 integer-valued 所以任何 ≠ 都产生 label，但这可能引入 noisy labels。(3) 论文 Appendix A 验证了 label quality，但仅从 "no tie-breaking artifacts" 角度验证，未从 "minimum effect size" 角度讨论。
- 建议：讨论 score-comparison labels 的 effect size distribution；如果多数 score differences 很小（<5 points），routing signal 的 practical significance 需要质疑。

**W5** [warning] "Environment-agnostic" claim 过度泛化
- 具体位置：Abstract (abstract.tex line 2), method.tex line 39
- 问题：框架要求 (1) deterministic paired episodes under identical initial conditions, (2) binary well-defined death/catastrophe, (3) a meaningful "deterministic modality" to compare against。很多实际部署场景不满足这些条件（non-deterministic environments, continuous failure costs, no clear "oracle" modality）。论文的 ALFWorld 应用已经暴露了问题——modality 定义从 "computation mode" 变成了 "information access"，这是 fundamentally different。
- 建议：将 "environment-agnostic" 弱化为 "applicable to environments with binary catastrophic outcomes and controllable modality comparison"。

---

## 小问题（不影响接收）

- Abstract 和 title 的 framing 略有 overclaiming：title 说 "the Dominant Routing Signal" 但仅在 ScienceWorld 验证；cross-env 只有 directional evidence
- Table 7 (penalty sensitivity) 中 P=0 的 DAF=7.5% 且 CI 包含负数——说明 DAF 在低 penalty 下不 well-defined，应提及
- Appendix B 中 `find-non-living-thing` 的 n=40（其余 20）未在 SCI 计算公式中 account for（公式用了 $n_k$ 所以技术上是对的，但应在正文解释为什么对 aggregate metrics 无 bias）
- Ethics statement 提到 "40 GPU-hours on two consumer GPUs" 但未说明是 what GPUs；reproducibility 角度应报告型号
- Missing citation: NetHack Learning Environment (Küttler et al., 2020) 和 Crafter (Hafner, 2022) 在 conclusion 中被提到但未正式 cite

---

## Questions for Authors

1. Partial correlation df=27 的来源？如果是 episode-level 计算，请解释为什么 controlling for a per-task constant (δ·P) at episode-level 是 statistically valid。
2. 有没有 1.7B 在 4-seed 配置下的 episode-level accuracy？这对判断 non-monotonicity 是否真实至关重要。
3. Score-comparison labels 中，det vs int 的分数差的中位数和分布是什么？如果多数 difference < 5，这些 labels 的 signal-to-noise ratio 如何？
4. 对于 "both dead" episodes (35/245)：internal 和 deterministic 的 death step 分布是否不同？如果 internal 平均在 step 5 死而 deterministic 在 step 20 死，"both dead = no preference" 可能丢失信息。
5. 论文预测 "larger models with lower death rates would reduce DAF"——如果 death rate → 0, 框架还能提供什么 insight？DAF → 0 但 routing signal 可能 also → 0，使框架 uninformative。

---

## Missing References

- Küttler et al., "The NetHack Learning Environment," NeurIPS 2020 — 提到但未 cite
- Hafner, "Benchmarking the Spectrum of Agent Capabilities" (Crafter), ICLR 2022 — 提到但未 cite
- DAgger (Ross et al., 2011) — 在 Limitations 中 cite 了，OK
- 考虑引用: Ren et al., "When to Trust Language Models: A Survey on Safety and Reliability," 2024

---

## 格式合规

- ✓ ACL style (`\usepackage[review]{acl}`)
- ✓ Double-blind (`\author{Anonymous}`)
- ✓ Limitations section 实质性
- ✓ Ethics statement 存在
- ⚠ 页数无法从 tex 精确判断，但正文 6 sections + Limitations + Ethics + 6 appendix sections，结构合理；需确认正文 ≤8 页
- ⚠ 无匿名补充材料（code/data）——not required but would strengthen reproducibility

---

## Overall Recommendation

**2.5 / 5** — 接近 "Resubmit next cycle" (2) 和 "Borderline" (3) 之间。

核心方法论设计合理，负面结果有诊断价值，但：(1) 统计细节错误 (df=27) 削弱可信度；(2) data scaling ablation 的方法论缺陷使 "structural limitation" claim 过强；(3) cross-model/cross-env evidence 不足以支撑 main conference 水平的 generalization claim。如果修复 N1-N3 并诚实降级部分 claims，适合 Findings track。

---

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**3.0/5，建议 Findings track**。主要问题：

1. **Novelty 不足** — 核心发现（大惩罚环境中 death 主导分数差异）接近数学必然，作者自己也在多处承认 "mathematical consequence"
2. **单一环境证据** — cross-environment checks (MATH/ALFWorld) 都不 replicate death-dominance finding；真正需要的是第二个 catastrophic-failure 环境（NetHack/Crafter）
3. **Modality 定义与文献脱节** — "deterministic = oracle state provider" 远离 Toolformer/RouteLLM 等实际 tool-use routing 场景

框架本身的方法论质量高（bootstrap/partial correlation/LOO/data scaling），统计透明度在 NLP 论文中属上乘。如果补充第二环境复现 + 收窄 claim scope，可以提升到 main conference 水平。

---

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：以 Reviewer 1 身份完成了方法严谨性 + 实验设计维度的完整审查。主要发现三个 critical 问题：(1) partial correlation df=27 统计错误；(2) augmentation-based data scaling ablation 不能 rule out real data scarcity；(3) capacity scaling 的 seed 配置 confound。另有 5 个 should-fix 问题（cluster bootstrap、cross-model 证据弱、MATH underpowered、Algorithm 1 隐含假设、"environment-agnostic" overclaim）。总体评分 2.5/5，建议修复后适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 778 · 2026-05-16T19:47:01.173324+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n**侧重**: Contribution novelty + 完整性\n**Overall Score**: 3.0/5 — Findings track\n\n### Must-Fix (Critical)\n\n**N1** 核心发现的 novelty 不足——接近 tautological consequence\n- DAF = δP/(δP + Δ_nd) 在 P=100 时 90.4% 接近同义反复（\"当 penalty 是 score gap 的 35 倍时，penalty 项主导总 gap\"）。P=10 时仅 50.4%。\n- 78.9% penalty-independent metric 更稳健但仍处于从属位置。\n- 论文自承 \"mathematical consequence, not empirical finding\"，但 contribution framing 仍将其包装为 surprising discovery。\n- EMNLP main conference 需要 sufficient novelty/insight。\n\n**N2** 单一环境证据不足以支撑 generalization claim\n- MATH 是 negative contrast（power=0.42，non-significant）；ALFWorld 无 death penalty（different mechanism）；Llama 仅 direction-only。\n- 没有任何 cross-env check 实际 REPLICATES 了 death-dominance finding。\n- 论文自己承认需要 NetHack/Crafter 才能 true replication。\n- Contribution 3 \"cross-context applicability\" 仍属 overselling。\n\n**N3** \"Deterministic modality\" 定义与文献中的 tool-use routing 脱节\n- 论文的 \"deterministic\" = oracle state provider。但 Toolformer/RouteLLM/ReTool/Chameleon 研究的是 imperfect tools（API, code interpreter, search engine）。\n- MATH 中使用 code interpreter 更接近真实 tool-use，但结果 non-significant。\n- 读者期望 finding 能 inform 实际 tool-use routing design，但本文设定（oracle state vs no state）与现实差距过大。\n\n### Should-Fix (Warning)\n\n**W1** Router failure 不能直接 \"validate\" analytical framework\n- 一个特定架构（Qwen3-1.7B SFT+LoRA）失败，不等于分析框架被验证。\n- 未尝试 task-type classifier 作为 router、death-risk predictor、更大规模 real-data collection。\n- 4B 达到 59%，趋势明显，\"disproportionate cost\" 是 value judgment 非 empirical conclusion。\n\n**W2** Related work 有明显遗漏\n- AgentBench (ICLR 2024), LATS (ICML 2024), SelfCheckGPT (EMNLP 2023), FActScore (EMNLP 2023), Safe RLHF (ICLR 2024), ToolBench (ICLR 2024)\n\n**W3** Task selection bias 未充分 quantify\n- 排除 63% tasks 后声称 \"SCI = 0.2147 indicates systematic phenomenon\" 存在 survivorship bias。\n\n**W4** MATH evaluation 的 modality definition inconsistency\n- ScienceWorld: deterministic = oracle state。MATH: deterministic = code interpreter (imperfect tool)。不是同一个 modality definition。\n\n### 小问题\n- Abstract 数字密集; SCI 仅用一次可移到 Appendix; section ordering unusual; \"Oracle degeneracy\" 未定义; Contribution 2 和 1 混在一起\n\n---\n\n请对以上 N1-N3, W1-W4 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "simgate-modular-routing",
  "chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c",
  "director_session_key": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — Round 1 审稿意见\n\n**侧重**: Contribution novelty + 完整性\n**Overall Score**: 3.0/5 — Findings track\n\n### Must-Fix (Critical)\n\n**N1** 核心发现的 novelty 不足——接近 tautological consequence\n- DAF = δP/(δP + Δ_nd) 在 P=100 时 90.4% 接近同义反复（\"当 penalty 是 score gap 的 35 倍时，penalty 项主导总 gap\"）。P=10 时仅 50.4%。\n- 78.9% penalty-independent metric 更稳健但仍处于从属位置。\n- 论文自承 \"mathematical consequence, not empirical finding\"，但 contribution framing 仍将其包装为 surprising discovery。\n- EMNLP main conference 需要 sufficient novelty/insight。\n\n**N2** 单一环境证据不足以支撑 generalization claim\n- MATH 是 negative contrast（power=0.42，non-significant）；ALFWorld 无 death penalty（different mechanism）；Llama 仅 direction-only。\n- 没有任何 cross-env check 实际 REPLICATES 了 death-dominance finding。\n- 论文自己承认需要 NetHack/Crafter 才能 true replication。\n- Contribution 3 \"cross-context applicability\" 仍属 overselling。\n\n**N3** \"Deterministic modality\" 定义与文献中的 tool-use routing 脱节\n- 论文的 \"deterministic\" = oracle state provider。但 Toolformer/RouteLLM/ReTool/Chameleon 研究的是 imperfect tools（API, code interpreter, search engine）。\n- MATH 中使用 code interpreter 更接近真实 tool-use，但结果 non-significant。\n- 读者期望 finding 能 inform 实际 tool-use routing design，但本文设定（oracle state vs no state）与现实差距过大。\n\n### Should-Fix (Warning)\n\n**W1** Router failure 不能直接 \"validate\" analytical framework\n- 一个特定架构（Qwen3-1.7B SFT+LoRA）失败，不等于分析框架被验证。\n- 未尝试 task-type classifier 作为 router、death-risk predictor、更大规模 real-data collection。\n- 4B 达到 59%，趋势明显，\"disproportionate cost\" 是 value judgment 非 empirical conclusion。\n\n**W2** Related work 有明显遗漏\n- AgentBench (ICLR 2024), LATS (ICML 2024), SelfCheckGPT (EMNLP 2023), FActScore (EMNLP 2023), Safe RLHF (ICLR 2024), ToolBench (ICLR 2024)\n\n**W3** Task selection bias 未充分 quantify\n- 排除 63% tasks 后声称 \"SCI = 0.2147 indicates systematic phenomenon\" 存在 survivorship bias。\n\n**W4** MATH evaluation 的 modality definition inconsistency\n- ScienceWorld: deterministic = oracle state。MATH: deterministic = code interpreter (imperfect tool)。不是同一个 modality definition。\n\n### 小问题\n- Abstract 数字密集; SCI 仅用一次可移到 Appendix; section ordering unusual; \"Oracle degeneracy\" 未定义; Contribution 2 和 1 混在一起\n\n---\n\n请对以上 N1-N3, W1-W4 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "simgate-modular-routing",
    "chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c",
    "director_session_key": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
  }
}
```

</details>

---


### Tool result

_source line 779 · 2026-05-16T19:47:22.337371+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21164
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-16T19:47:23.191007+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n**侧重**: 方法严谨性 + 实验设计\n**Overall Score**: 2.5/5 — Resubmit next cycle\n\n### Must-Fix (Critical)\n\n**N1** Partial correlation df=27 统计错误\n- Section 4.1: \"controlling for δ·P, the residual is r = 0.02 (p = 0.91, df = 27)\"\n- 散点图有 n=11 task types。Partial correlation controlling for 1 variable 的 df 应为 n-2-1 = 8，不可能是 27。\n- 若 episode-level 计算（N=245），controlling for δ·P 本质上等于 controlling for task identity（P 恒定，δ per-task 常量），会膨胀 df。\n- 这是 \"r=0.97 是 mathematical artifact\" 论证的关键数据点。\n\n**N2** Data scaling ablation 方法论缺陷\n- Paraphrase augmentation 将 majority class 从 89.6% 膨胀到 97.7%，不等同于 real data scaling。\n- 结论 \"rules out step-level data scarcity\" 过强——augmentation 仅说明 surface-level diversity 不帮忙。\n- \"Structural limitation\" claim 需降级为 \"at current data scale, the router cannot learn\"。\n\n**N3** Capacity scaling non-monotonicity confound 未控制\n- 0.6B: 50.7%, 1.7B: 47.1%, 4B: 59.0%——non-monotonic。\n- 1.7B 用 8 seeds vs 0.6B/4B 用 4 seeds——不直接可比。\n- \"only 4B exceeds the baseline\" 是 key claim，但可能是配置差异 artifact。\n- 需要在相同配置下重跑 0.6B/1.7B/4B。\n\n### Should-Fix (Warning)\n\n**W1** Bootstrap 未考虑 cluster structure\n- Episodes within same task type 共享 structure，不独立。Cluster bootstrap（task-type level，11 clusters）会产生更宽但更诚实的 CI。\n\n**W2** Cross-model 证据过弱\n- Llama N=70, 7 tasks, 0 internal-preferred——仅说明 \"another 7-8B model dies more in internal mode\"（unsurprising）。\n- 更有价值：(1) 70B model 预测 DAF 下降；(2) Reflexion 作为更强 internal baseline。\n\n**W3** MATH 实验 underpowered 且 claim 过强\n- Power=0.42, p=0.079。42% power 的 non-significant result 几乎 uninformative（Type II error=58%）。\n- 不能作为 \"framework prediction validated\" 的证据，只能说 \"inconclusive\"。\n\n**W4** Algorithm 1 的隐含假设未讨论\n- \"Both dead → no preference\" 不区分 early death vs late death。\n- Score comparison 不设 minimum meaningful difference。\n- Score-comparison labels 的 practical significance 需讨论。\n\n**W5** \"Environment-agnostic\" claim 过度泛化\n- 框架要求 binary death, deterministic paired episodes, meaningful \"deterministic modality\"。\n- ALFWorld 应用已暴露问题——modality 从 \"computation mode\" 变成 \"information access\"。\n\n### 小问题\n- Title overclaiming (\"the Dominant\" 仅 ScienceWorld 验证)\n- P=0 时 DAF CI 包含负数——低 penalty 下不 well-defined\n- find-non-living-thing n=40 vs 其他 20 需说明\n- Ethics statement 未报 GPU 型号\n- NetHack/Crafter 在 Conclusion 中提到但未 cite\n\n---\n\n请对以上 N1-N3, W1-W5 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "simgate-modular-routing",
  "chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c",
  "director_session_key": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n**侧重**: 方法严谨性 + 实验设计\n**Overall Score**: 2.5/5 — Resubmit next cycle\n\n### Must-Fix (Critical)\n\n**N1** Partial correlation df=27 统计错误\n- Section 4.1: \"controlling for δ·P, the residual is r = 0.02 (p = 0.91, df = 27)\"\n- 散点图有 n=11 task types。Partial correlation controlling for 1 variable 的 df 应为 n-2-1 = 8，不可能是 27。\n- 若 episode-level 计算（N=245），controlling for δ·P 本质上等于 controlling for task identity（P 恒定，δ per-task 常量），会膨胀 df。\n- 这是 \"r=0.97 是 mathematical artifact\" 论证的关键数据点。\n\n**N2** Data scaling ablation 方法论缺陷\n- Paraphrase augmentation 将 majority class 从 89.6% 膨胀到 97.7%，不等同于 real data scaling。\n- 结论 \"rules out step-level data scarcity\" 过强——augmentation 仅说明 surface-level diversity 不帮忙。\n- \"Structural limitation\" claim 需降级为 \"at current data scale, the router cannot learn\"。\n\n**N3** Capacity scaling non-monotonicity confound 未控制\n- 0.6B: 50.7%, 1.7B: 47.1%, 4B: 59.0%——non-monotonic。\n- 1.7B 用 8 seeds vs 0.6B/4B 用 4 seeds——不直接可比。\n- \"only 4B exceeds the baseline\" 是 key claim，但可能是配置差异 artifact。\n- 需要在相同配置下重跑 0.6B/1.7B/4B。\n\n### Should-Fix (Warning)\n\n**W1** Bootstrap 未考虑 cluster structure\n- Episodes within same task type 共享 structure，不独立。Cluster bootstrap（task-type level，11 clusters）会产生更宽但更诚实的 CI。\n\n**W2** Cross-model 证据过弱\n- Llama N=70, 7 tasks, 0 internal-preferred——仅说明 \"another 7-8B model dies more in internal mode\"（unsurprising）。\n- 更有价值：(1) 70B model 预测 DAF 下降；(2) Reflexion 作为更强 internal baseline。\n\n**W3** MATH 实验 underpowered 且 claim 过强\n- Power=0.42, p=0.079。42% power 的 non-significant result 几乎 uninformative（Type II error=58%）。\n- 不能作为 \"framework prediction validated\" 的证据，只能说 \"inconclusive\"。\n\n**W4** Algorithm 1 的隐含假设未讨论\n- \"Both dead → no preference\" 不区分 early death vs late death。\n- Score comparison 不设 minimum meaningful difference。\n- Score-comparison labels 的 practical significance 需讨论。\n\n**W5** \"Environment-agnostic\" claim 过度泛化\n- 框架要求 binary death, deterministic paired episodes, meaningful \"deterministic modality\"。\n- ALFWorld 应用已暴露问题——modality 从 \"computation mode\" 变成 \"information access\"。\n\n### 小问题\n- Title overclaiming (\"the Dominant\" 仅 ScienceWorld 验证)\n- P=0 时 DAF CI 包含负数——低 penalty 下不 well-defined\n- find-non-living-thing n=40 vs 其他 20 需说明\n- Ethics statement 未报 GPU 型号\n- NetHack/Crafter 在 Conclusion 中提到但未 cite\n\n---\n\n请对以上 N1-N3, W1-W5 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "simgate-modular-routing",
    "chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c",
    "director_session_key": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
  }
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-16T19:47:24.349041+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1158
}
```

</details>

---


### Assistant

_source line 782 · 2026-05-16T19:47:28.002260+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 74

## Round 74

2 recorded events


### User

_source line 783 · 2026-05-16T19:48:39.766326+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Must-Fix

**[AGREE with nuance] R2-N1: DAF 接近 tautological consequence**

R2 的核心论点成立：DAF = δP/(δP + Δ_nd) 在 P 远大于 Δ_nd 时 *数学上必然* 趋近 1，这不是 empirical discovery。论文自己也承认这一点（method.tex §3.4: "a mathematical consequence, not an empirical finding"；discussion.tex: "partial r = 0.02"）。

但我要补充一点 R2 未提及的：论文的 *真正* empirical content 是 δ = 0.2653（internal 死亡率 42.9% vs deterministic 16.3%）和 Δ_nd = 2.84。这两个数字本身不是 tautology——它们说明 (1) hallucination-induced death 的频率远超预期，(2) 排除 death 后两个 modality 几乎无差异。78.9% 的 penalty-independent label fraction 更能体现这一 empirical finding。问题在于论文的 **framing 策略**：title 和 abstract 把 DAF=90.4% 作为 headline number，而更稳健的 78.9% 反而处于从属位置。

**结论**：同意 novelty concern。建议作者重构 framing——以 δ 和 Δ_nd 的经验发现为核心 claim，DAF 作为 summary metric 而非 headline。

---

**[AGREE] R2-N2: 单一环境证据不足以支撑 generalization claim**

完全同意。我在自己的 W2/W3 中已指出：
- MATH: power=0.42, p=0.079, inconclusive（我的 W3）
- Llama: N=70, 7 tasks, 0 internal-preferred, 仅 direction-consistent（我的 W2）
- ALFWorld: 不同 mechanism (information asymmetry)，不是 replication

Contribution 3 写 "cross-context applicability" 确实 overselling。论文 conclusion 中自己说 "true quantitative replication requires a second catastrophic-failure environment (e.g., NetHack, Crafter)"（conclusion.tex line 7），但 contribution list 没有反映这一限定。建议将 Contribution 3 降级为 "cross-context *illustration* demonstrating framework flexibility"，不用 "applicability" 这个暗示 validated generalization 的词。

---

**[REBUT with partial agreement] R2-N3: Deterministic modality 与文献中的 tool-use routing 脱节**

R2 说 oracle state provider 与 Toolformer/RouteLLM/ReTool 研究的 imperfect tools 差距过大。这在 *practical relevance* 层面成立，但忽略了论文的 **定位**。

论文明确将自己定位为 **diagnostic framework**，不是 practical routing system。Discussion 中说 "The deliberate heterogeneity in deterministic modality definition across our three environments tests whether the *framework* generalizes, not whether any single modality definition does"（discussion.tex §Discussion, "Framework applicability" paragraph）。用 oracle 作为 upper-bound comparison 是诊断方法论的标准做法——它隔离出 *理论上最大的* routing signal，然后分析这个 signal 的构成。如果即使在 oracle-level，routing signal 90%+ 来自 death avoidance，那么 imperfect tools 只会更糟（因为 imperfect tools 不能完全避免 death）。

**但 R2 的 practical relevance concern 部分成立**：读者确实期望 findings 能 inform 实际 tool-use design。论文应该更明确讨论：在 imperfect-tool 场景下，(1) death avoidance 的优势可能更小（tool 本身也可能引发 failure），(2) 但 safety-first routing 的 design principle 仍然适用。MATH 中 code interpreter 作为 imperfect tool 的结果 non-significant，这既可能是 power 问题也可能是 tool imperfection 削弱了 signal——论文未区分这两种解释。

**结论**：不同意将此定为 "must-fix level" 的 novelty 问题——oracle comparison 在 diagnostic 框架中是合理的。但 should-fix：需要加 1-2 段讨论 oracle vs imperfect-tool 的 gap 及其对 findings 的 implication。

---

### Should-Fix

**[AGREE with nuance] R2-W1: Router failure 不能直接 "validate" analytical framework**

R2 说得对：一个特定架构（Qwen3-1.7B SFT+LoRA）失败不等于分析框架被 validated。论文用 "validates our analytical methodology over brute-force learned routing" 这个表述（experiments.tex §4.5, discussion.tex "Implications for router design"）是 overclaim。

补充 R2 未提到的一点：4B 达到 59.0% episode-level accuracy 且趋势上升（Table 8）。如果 8B 或 14B 能达到 70%+，"brute-force routing is disproportionate" 的 narrative 就不成立了。"Disproportionate cost" 确实是 value judgment——4B 对很多应用场景是可接受的 overhead。

但我也要为论文辩护一个方面：router 实验的 *informative negative* 价值是真实的。它展示了 (1) step-level signal 不 transfer to episode-level（54.1% → 47.1%），(2) data augmentation 无帮助（虽然方法有缺陷，如我的 N2），(3) majority-class collapse 在所有 scale 出现。这些 diagnostic observations 有价值，只是不应该用 "validate" 来概括。

**结论**：同意。建议将 "validates" 改为 "is consistent with" 或 "provides evidence that at current scales, learned routing does not improve over the analytical baseline"。

---

**[AGREE] R2-W2: Related work 遗漏**

同意。特别是：
- **AgentBench** (Liu et al., ICLR 2024): multi-environment agent benchmark，直接相关（ScienceWorld 是其子集之一）
- **LATS** (Zhou et al., ICML 2024): 用 search 做 LLM agent planning，是比 ReAct 更强的 internal baseline 参考
- **ToolBench** (Qin et al., ICLR 2024): 大规模 tool-use benchmark，R2-N3 的 practical relevance concern 在 ToolBench 语境下更尖锐

SelfCheckGPT 和 FActScore 的相关性稍弱（它们关注 text generation faithfulness 而非 agent failure），但 Safe RLHF 在 safe RL 段落中确实应该 cite。

---

**[AGREE] R2-W3: Task selection bias / survivorship bias**

同意，我在自己的审稿中也注意到了相关问题。排除 63% 的 task types 后声称 SCI = 0.2147 "indicates systematic phenomenon" 存在 survivorship bias。SCI 是在 11 个被选中的 task types 上计算的（method.tex §3.5），不包括 19 个被排除的（全为 zero routing signal）。如果将 19 个 zero-signal tasks 纳入 SCI 计算，结果会大幅升高（signal 集中在 11/30 tasks = 36.7% 的 task space）。

论文的 Appendix B (main.tex lines 83-84) 确实解释了 prescreening 不 select for death-prone tasks（deterministic death rate: included 17.8% vs excluded 14.9%）。但 "systematic phenomenon distributed across nearly all task types" (method.tex §3.5 最后一句) 这个说法在排除了大多数 tasks 的前提下是 misleading。

**建议**：将 "systematic across nearly all task types" 弱化为 "systematic across all task types that exhibit any routing signal"，并在 Limitations 中明确讨论 63% exclusion 对 generalization 的影响。

---

**[REBUT] R2-W4: MATH modality definition inconsistency**

R2 认为 ScienceWorld (oracle state) 和 MATH (code interpreter) 的 modality 定义不一致，削弱 cross-env 比较。

我认为这恰恰是 **框架设计的 feature 而非 bug**。论文 discussion 中明确说明：三个环境的 deterministic modality 定义 *故意不同*，目的是测试框架是否能在不同 modality 定义下都能 decompose routing signal（discussion.tex "Framework applicability" paragraph）。如果框架要求 modality 定义完全一致才能使用，它就不是 "environment-agnostic" 的。

关键在于论文的 claim structure：
- ScienceWorld: death dominates → DAF = 90.4% ✓
- MATH: no death → DAF should be ~0 → 结果 non-significant, consistent ✓  
- ALFWorld: no death → identifies different mechanism (information asymmetry) ✓

三个环境不是在做 *同一个实验的 replication*，而是在展示框架在不同条件下的 *诊断能力*。MATH 的 non-significance 和 ALFWorld 的 different mechanism 恰好是 framework 有效的 evidence（它不会在没有 death 的环境中错误地检测 death signal）。

**但我承认**：如果把这三个环境并列在 Table 10（main.tex line 328）中做直接对比，确实可能误导读者以为是 comparable experiments。建议在 Table 10 caption 中更明确说明 modality definitions differ across rows。

---

### 对 R2 小问题的简要回应

- Abstract 数字密集：同意，可精简
- SCI 移到 Appendix：**不同意**。SCI 回答了 "death avoidance 是 systematic 还是 driven by outliers" 这个核心问题（method.tex §3.5），值得在正文保留，但可以精简到 1-2 句
- Section ordering unusual (Related Work 在 Experiments 后)：这是 ACL 论文中的常见做法，不算 issue
- "Oracle degeneracy" 未定义：同意，应在首次使用时加 1 句定义
- Contribution 2 和 1 混在一起：同意，应拆分更清晰

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 784 · 2026-05-16T19:48:47.263178+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 75

## Round 75

2 recorded events


### User

_source line 785 · 2026-05-16T19:48:49.675072+00:00_

[Reviewer 1 审稿结果]:
审稿回应已提交给 Director。

总结：对 R2 的 7 个问题，我给出 4 个 [AGREE]、1 个 [AGREE with nuance]、2 个 [REBUT]。主要共识在 DAF framing overclaim (N1)、单环境 generalization 不足 (N2)、survivorship bias (W3)、router "validate" 措辞过强 (W1)。反驳集中在 oracle modality 定义的合理性 (N3, W4)——diagnostic framework 用 oracle 作 upper-bound 比较是方法论标准做法，modality 定义差异是 framework flexibility 的体现而非缺陷。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 786 · 2026-05-16T19:48:54.913448+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 76

## Round 76

8 recorded events


### User

_source line 787 · 2026-05-16T19:49:39.066209+00:00_

[Reviewer 2 审稿结果]:
以下是我（Reviewer 2）对 Reviewer 1 各条意见的逐条回应：

---

## 对 Reviewer 1 Must-Fix 问题的回应

**[AGREE] R1-N1: Partial correlation df=27 统计错误**

R1 的指出完全正确。Section 4.1 报告 "partial $r = 0.02$ ($p = 0.91$, $df = 27$)"，但散点图基于 $n=11$ task types（Figure 1, Table 7/Appendix B）。控制 1 个变量后 $df = n - 2 - 1 = 8$。若改为 episode-level 计算（$N=245$），则 $df$ 应为 242，也不是 27。$df=27$ 在任何合理计算方式下都无法成立。

补充：这一错误的严重性在于，该 partial correlation 是论文"$r=0.97$ is a mathematical consequence"论证的核心证据（Introduction line 25, Discussion para 2）。若 $p$ 值在 $df=8$ 下重算仍不显著（大概率如此，因为 $r=0.02$ 极小），结论不变但统计报告需修正；若 $p$ 值变化导致显著性判断改变，则影响更大。

---

**[AGREE] R1-N2: Data scaling ablation 方法论缺陷**

同意 R1 的核心判断：paraphrase augmentation $\neq$ real data scaling。论文自身在 Appendix D 承认："episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes"（main.tex line 217），且 augmentation 将 Det% 从 89.6% 膨胀至 97.7%（Table 5）。然而主文 Section 5.5 仍使用 "rules out step-level data scarcity" 的表述（experiments.tex line 59），与 appendix 中的 hedging 不一致。

补充发现：论文在 Table 5 caption 中承认 "Internal recall = 0.0 at all scales (complete majority-class collapse)"——这意味着 router 在所有 scale 下完全无法识别 internal-preferred episodes，更可能反映的是 9/245 = 3.7% 的极端 class imbalance 问题，而非 "structural limitation"。合理的 real-data scaling 应优先增加 minority class samples（例如通过更多 seed variations 寻找 internal-preferred episodes），而非 augment majority class。

建议措辞修改为："Paraphrase-based augmentation does not improve routing; however, this does not rule out that collecting additional genuine internal-preferred episodes might."

---

**[AGREE] R1-N3: Capacity scaling non-monotonicity confound**

论文自身在 Table 6 caption 中承认配置差异："$\dagger$1.7B episode-level figure comes from the main experiment (§5.5) with a different training configuration (8 cross-split seeds vs. 4 seeds for 0.6B/4B); direct comparison across scales should be interpreted with this caveat."

non-monotonicity（0.6B: 50.7% → 1.7B: 47.1% → 4B: 59.0%）使得 "capacity is one limiting factor" 的因果推断不可靠。1.7B 表现 worse than 0.6B 就已经不支持 "capacity matters" 的叙事。论文将 4B 的 59.0% 作为 key evidence 支持 "validates our analytical methodology over brute-force learned routing"（experiments.tex line 59），但这一 claim 建立在 confounded comparison 之上。

补充：即使在相同配置下重跑确认了 4B > 1.7B > 0.6B 的 monotonic trend，59% episode-level accuracy 对比 50% baseline 仅 +9pp，这与 "disproportionate cost" 的论点反而是一致的。问题核心在于当前数据不支持因果推断，而非结论方向本身必然错误。

---

## 对 Reviewer 1 Should-Fix 问题的回应

**[AGREE] R1-W1: Bootstrap 未考虑 cluster structure**

方法论上正确。Method Section 3.5（method.tex line 118）解释了为何选择 episode-level 而非 step-level resampling，但未讨论 task-type clustering。11 task types 内部的 episodes 共享环境动态和 action space（例如 Appendix B 中 `id-life-stages-1` 和 `id-life-stages-2` 明显结构相似），违反 i.i.d. 假设。

不过，我注意到 Appendix C（Table 4, LOO analysis）已部分缓解此顾虑：leave-one-out $r$ 范围为 $[0.963, 0.980]$，说明无 leverage point。但 LOO 针对 correlation，未针对 DAF CI。DAF 的 cluster bootstrap（11 clusters）CI 会更宽——定性结论可能不变（DAF 仍远高于 50%），但报告当前 CI 为 "episode-level bootstrap" 是对 precision 的高估。

---

**[AGREE] R1-W2: Cross-model 证据过弱**

Llama-3.1-8B 的复制（Appendix E）仅证明"另一个 7-8B 模型在 internal mode 下也大量死亡"——考虑到 7B 级别模型的 hallucination 率本身就高，这并不令人惊讶。论文 Limitations 段承认 "both models are in the 7–8B parameter range"（main.tex line 36）。

R1 建议的两个实验价值明显更高：
1. **70B 模型**：论文自己的框架预测 DAF 应下降（Discussion: "larger models with lower death rates would reduce DAF"），但这只是 prediction——未验证的 prediction 不能充当 evidence。
2. **Reflexion 作为更强 internal baseline**：论文 Limitations 列出 Reflexion 为 potential stronger strategy（main.tex line 36），但未测试。若 Reflexion 显著降低 internal death rate，则 DAF 的绝对值会下降，中心发现的 robustness 需重新评估。

---

**[AGREE] R1-W3: MATH 实验 underpowered 且 claim 过强**

Power = 0.42 意味着即使真实效应存在，也有 58% 概率无法检测到——统计上 non-informative。R1 的判断正确。

论文在 experiments.tex 中措辞相对谨慎（"directional evidence, not a definitive finding"），但在 Introduction contribution 列表中（introduction.tex line 42）和 Conclusion 中仍使用 "consistent with the framework's prediction" 的表述——这对 power=0.42 的结果而言 overclaimed。一个 underpowered non-significant result 与任何 prediction 都"consistent"（包括 null hypothesis），因此不能作为 confirmatory evidence。

正确表述应为："The MATH evaluation was inconclusive due to insufficient power (0.42); a definitive test requires $N \approx 770$."

---

**[REBUT] R1-W4: Algorithm 1 的隐含假设未讨论**

部分同意、部分反驳。

R1 的第 1 点（both-dead 不区分 early/late death）：**有道理但影响有限。** Appendix A（main.tex line 49）报告 35 episodes 为 both-dead，全部标记为 no_preference 并排除出 router training。若区分 early/late death，最多只影响这 35 个 label（14.3%），且这些 label 未参与任何定量分析（DAF 计算排除 both-dead episodes）。

R1 的第 2 点（score comparison 无 minimum meaningful difference）：**论文已有回应。** Method Section 3.3（method.tex line 50）明确指出 "ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold"——这对离散得分系统是合理的。

R1 的第 3 点（score-comparison labels 的 practical significance）：**论文已有数据。** Appendix A 报告仅 20 个 score-comparison labels（16 det + 4 int），对比 75 个 death-asymmetry labels。论文的核心发现正是这些 score-comparison labels 贡献极少——这本身就是论据的一部分。

综上：W4 的担忧有合理之处但不影响核心结论，论文已在不同位置提供了回应数据。建议在 Method 段补充一句关于 both-dead 处理方式的 rationale 即可。

---

**[AGREE] R1-W5: "Environment-agnostic" claim 过度泛化**

论文在 method.tex line 39 声称 "environment-agnostic: it requires only paired episode outcomes under two modalities, with no assumptions about score structure or failure mode"，但实际应用中：

- ScienceWorld: deterministic = ground-truth state transitions（oracle state provider）
- MATH: deterministic = code interpreter
- ALFWorld: deterministic = access to admissible actions

这三个"deterministic modality"的含义完全不同，导致 DAF 衡量的东西也不同。Discussion 中的辩护（discussion.tex line 14："The deliberate heterogeneity in deterministic modality definition across our three environments tests whether the framework generalizes"）实际上暴露了问题：框架的 finding 取决于 modality definition 的选择，而非仅取决于 environment properties。

更准确的 claim 应为："The framework is applicable to any environment where two paired modalities can be defined and complete episodes can be collected"——但需明确 findings 会随 modality definition 变化。

---

## 对小问题的简要回应

- **Title overclaiming**: [AGREE] "the Dominant" 仅在 ScienceWorld 一个环境验证，建议改为 "a Dominant" 或 scope 到 ScienceWorld。
- **P=0 时 DAF CI 包含负数**: [AGREE] Table 8 显示 $P=0$ 时 DAF=7.5%, CI=[$-36.7$, $83.1$]——确实 ill-defined，应在正文注明 DAF 的 well-definedness 条件。
- **find-non-living-thing n=40 vs 其他 20**: 论文已在 Table 2 footnote 解释（"data was collected in two batches, with the second batch adding 20 episodes"），但主文未充分说明。
- **GPU 型号**: [AGREE] Ethics Statement 仅说 "two consumer GPUs"，应报告具体型号。
- **NetHack/Crafter 未 cite**: [AGREE] Conclusion 中提到但无引用，应添加。

---

## 总结

R1 的审稿意见质量很高，多数 critical issues 我独立审查中也有类似发现。**N1（df 错误）需立即修正；N2-N3 影响论文核心 claim 的可信度但不改变发现的方向性。** W1-W3 和 W5 是方法论完善的必要步骤。唯一我部分不同意的是 W4——论文对 Algorithm 1 的设计选择已有足够数据支撑，albeit 分散在不同 section。

整体而言，R1 的 2.5/5 评分合理偏低；论文主要问题在于 statistical reporting errors 和 over-claiming，而非 fundamental flaws in the framework design。修正后有 Findings track 潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-16T19:50:10.945760+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-16T19:50:10.996497+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-16T19:53:35.235132+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "- id: \"R10-C1\"\n  summary: \"df=27 statistical error in partial correlation — invalidates key supporting evidence\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. Section 4.1 reports partial r=0.02, p=0.91, df=27. With n=11 task types and 1 control variable, df should be 8. If episode-level (N=245), df=242. df=27 impossible under any valid computation. Error undermines the 'r=0.97 is mathematical artifact' argument — the conclusion likely still holds (r=0.02 is tiny) but statistical reporting is wrong.\"\n  action_items:\n    - round: 10\n      action: \"Recompute partial correlation at task-level (df=8) and report correct p-value. If episode-level was intended, explain why controlling for per-task constant at episode-level is valid.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C2\"\n  summary: \"Core finding novelty insufficient — DAF near-tautological, 78.9% is the real empirical content\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. DAF=δP/(δP+Δ_nd) approaching 1 when P>>Δ_nd is mathematical necessity. The true empirical content is δ=0.2653 and Δ_nd=2.84 (i.e., hallucination-induced death is frequent AND non-death performance gap is negligible). Paper self-acknowledges 'mathematical consequence' but contribution framing still presents as surprising discovery. For EMNLP main conference, contribution sizing may be insufficient without second catastrophic-failure environment.\"\n  action_items:\n    - round: 10\n      action: \"Restructure contribution framing: lead with empirical findings (δ, Δ_nd, 78.9%) not derived metric (DAF). Frame DAF as summary/diagnostic tool, not headline discovery. Consider Findings track positioning if no new environment data.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C3\"\n  summary: \"Single-environment evidence — no cross-env REPLICATION of death-dominance finding\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Cross-env 'validation' near-tautological.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus persists. Paper now says 'cross-context applicability' (improved from 'validation') but Contribution 3 still oversells. MATH=absence-of-evidence, ALFWorld=different mechanism, Llama=direction-only. True validation needs second catastrophic-failure env (NetHack/Crafter). Title says 'the Dominant Routing Signal' based on single env.\"\n  action_items:\n    - round: 10\n      action: \"Option A: Add pilot-scale (50-100 episodes) replication in NetHack or Crafter. Option B: Retitle to scope to ScienceWorld, downgrade Contribution 3 to 'framework illustration', position as Findings track.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C4\"\n  summary: \"Data scaling ablation uses augmentation — cannot rule out real-data scarcity\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Augmentation inflates majority class, doesn't create novel routing patterns.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. Paper partially addressed (now says 'augmentation-based scaling provides no improvement; real-data scaling remains open'). But Section 4.5 still says 'rules out step-level data scarcity' — inconsistent with appendix hedging. Internal recall=0.0 at all scales suggests extreme class imbalance (3.7%) is the driver, not structural limitation.\"\n  action_items:\n    - round: 10\n      action: \"Unify language: remove 'rules out' from main text. Explicit distinction: 'step-level paraphrase diversity (ruled out) vs episode-level minority-class diversity (open, requires ~1,350 real pairs)'. Acknowledge 3.7% class imbalance as primary confound.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C5\"\n  summary: \"Capacity scaling confound — 1.7B uses 8 seeds vs 4 for 0.6B/4B, non-monotonic result\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Non-monotonic curve, 3 non-comparable data points.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. Paper acknowledges non-monotonicity and configuration caveat in caption but text remains confident. R1 escalates: 'only 4B exceeds baseline' claim rests on confounded comparison. Even if trend is real, 59% for 4B params = +9pp is arguably not 'disproportionate' for all use cases.\"\n  action_items:\n    - round: 10\n      action: \"Either rerun 0.6B/1.7B/4B under identical config (same seed count, same split strategy) OR explicitly acknowledge comparison is confounded and weaken conclusion to 'preliminary evidence suggesting capacity matters, but non-monotonicity and configuration differences prevent causal inference'.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Router failure does not 'validate' analytical framework — overclaimed causal link\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. One architecture (Qwen3-1.7B SFT+LoRA) failing ≠ framework validated. Missing: task-type classifier as router, death-risk predictor, real-data scaling. 4B at 59% with upward trend weakens 'disproportionate cost' narrative. 'Validates' → 'is consistent with'.\"\n  action_items:\n    - round: 10\n      action: \"Replace 'validates our analytical methodology' with 'is consistent with' or 'provides evidence that at current scales, learned routing does not improve over the trivial baseline'. Add task-type oracle router baseline (routing signal=task type → task classifier is upper bound).\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"'Environment-agnostic' overclaim — framework requires specific preconditions\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. Framework requires: (1) binary catastrophic outcome, (2) deterministic paired episodes under identical conditions, (3) meaningful 'deterministic modality'. ALFWorld already shows modality definition shifts from 'computation mode' to 'information access'. Findings depend on modality definition choice, not just environment properties.\"\n  action_items:\n    - round: 10\n      action: \"Weaken to 'applicable to environments with binary catastrophic outcomes and controllable modality comparison'. Add sentence: 'findings will vary with modality definition choice'.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W3\"\n  summary: \"Related work gaps — AgentBench, LATS, hallucination detection, Safe RLHF, ToolBench\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2 identified 6 missing refs, R1 agreed on AgentBench/LATS/ToolBench/SafeRLHF. Hallucination literature (SelfCheckGPT/FActScore) highly relevant given 'hallucination→death' is the core mechanism but uncited. NetHack/Crafter mentioned in Conclusion but not formally cited.\"\n  action_items:\n    - round: 10\n      action: \"Add: AgentBench (Liu+ ICLR24), LATS (Zhou+ ICML24), Safe RLHF (Dai+ ICLR24), ToolBench (Qin+ ICLR24), SelfCheckGPT (Manakul+ EMNLP23), NetHack (Küttler+ NeurIPS20), Crafter (Hafner ICLR22). Discuss hallucination detection as potential DAF-reducer.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W4\"\n  summary: \"Bootstrap CI needs cluster-level sensitivity analysis (task-type clusters)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. Episodes within same task type share structure (env dynamics, death risk profile), violating i.i.d. assumption. Cluster bootstrap (11 task-type clusters) would produce wider but more honest CI. Current CI [81.6%, 98.8%] may be over-confident. LOO (Appendix C) partially addresses but only for correlation, not DAF.\"\n  action_items:\n    - round: 10\n      action: \"Report cluster bootstrap CI (resampling at task-type level, 11 clusters) as sensitivity analysis alongside episode-level CI. If substantially wider, discuss implications.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W5\"\n  summary: \"Cross-model evidence (Llama N=70) only shows 'similar model dies more' — unsurprising\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"N=70, 0 internal-preferred, insufficient for framework generalization.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus persists. Paper narrowed claim to 'directional consistency' (good), but both still in 7-8B range with similar hallucination profiles. More informative: 70B model (predict DAF↓) or Reflexion internal baseline (test if self-correction reduces death). Current evidence is unsurprising.\"\n  action_items:\n    - round: 10\n      action: \"Frame as 'preliminary pilot confirming direction' not as meaningful cross-model validation. Add 'larger models with lower hallucination rates' and 'stronger internal strategies (Reflexion)' as explicit testable predictions with expected outcomes.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W6\"\n  summary: \"MATH claim still overclaimed despite power analysis addition\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Need post-hoc power analysis.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper now reports power=0.42, N≈770 (good). But Introduction/Conclusion still say 'consistent with framework prediction' — a power=0.42 non-significant result is consistent with ANY prediction including null. Needs strict downgrade to 'inconclusive'.\"\n  action_items:\n    - round: 10\n      action: \"Replace 'consistent with framework prediction' with 'inconclusive due to insufficient power (0.42); a definitive test requires N≈770'. Remove from Contribution 3 evidence list.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W7\"\n  summary: \"Task selection survivorship bias — SCI=0.2147 'systematic' claim misleading given 63% exclusion\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. SCI computed over 11 selected tasks only. If 19 zero-signal tasks included, signal concentrated in 37% of task space — contradicts 'systematic phenomenon'. Anti-cherry-picking evidence (Appendix B) shows similar det death rates but doesn't address whether excluded tasks have different hallucination/death mechanisms.\"\n  action_items:\n    - round: 10\n      action: \"Weaken 'systematic across nearly all task types' to 'systematic across all task types exhibiting routing signal'. Add Limitations sentence on 63% exclusion's impact on generalization.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-m1\"\n  summary: \"Modality definition disconnect — oracle state ≠ practical tool-use routing\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2 raised as critical (N3), R1 partially rebutted: oracle comparison is standard diagnostic methodology. Consensus: oracle is acceptable for diagnostic framework but paper needs 1-2 paragraphs discussing gap between oracle-state findings and imperfect-tool reality. Currently missing: would death-avoidance still dominate with imperfect tools that themselves can fail?\"\n  action_items:\n    - round: 10\n      action: \"Add Discussion paragraph: 'Our deterministic modality provides an upper bound; with imperfect tools (code interpreters, API calls), tool-induced failures may reduce the death-rate differential, lowering DAF. The safety-first design principle remains applicable but DAF magnitude will depend on tool reliability.'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-m2\"\n  summary: \"Title overclaims — 'the Dominant Routing Signal' verified in single environment only\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 raised, R2 agreed. 'the Dominant' implies universal finding; only ScienceWorld validates. Suggest: 'a Dominant Routing Signal' or scope to 'on ScienceWorld'.\"\n  action_items:\n    - round: 10\n      action: \"Consider title revision: 'Death Avoidance as a Dominant Routing Signal' or keep current but ensure Abstract/Conclusion scope clearly.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# Previously resolved issues — updated status\n- id: \"R6-C1\"\n  summary: \"DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not primary\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Fresh reviewers want full range + formula + dual reporting.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. Abstract still leads with DAF=90.41%. 78.9% present but not co-equal.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers confirm RESOLVED. 78.9% now appears co-equal with DAF throughout.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"REOPENED. R9 reviewers argue DAF=90.4% remains headline despite co-equal presentation.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Framing fix confirmed implemented: Abstract leads with 78.9%, DAF secondary with (score-level, P-dependent) parenthetical. Specific framing issue RESOLVED. Deeper novelty concern captured in R10-C2.\"\n  action_items:\n    - round: 9\n      action: \"78.9% as sole PRIMARY headline; DAF demoted.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Abstract now leads with 78.9% (penalty-independent), DAF presented as 'under P=100, corresponds to DAF=90.4%'. Framing fix complete. Residual novelty concern tracked as R10-C2.\"\n  resolution_round: 10\n\n- id: \"R6-W1\"\n  summary: \"r=0.97 structural coupling — qualifier insufficient in Abstract/Conclusion\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"High r partly mathematical due to penalty coupling.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. §4.1 has caveat but Abstract still reports r=0.97 without qualifier.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"RESOLVED. Abstract now includes structural coupling qualifier.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"REOPENED. 'Partly structural' deemed insufficient.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Qualifier upgraded to 'largely a mathematical consequence' in Abstract; Conclusion says 'internal consistency check'. Qualifier issue RESOLVED. But df=27 error in the statistic itself is NEW issue tracked as R10-C1.\"\n  action_items:\n    - round: 9\n      action: \"Demote r=0.97 to consistency diagnostic, strengthen qualifier.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Abstract: 'largely a mathematical consequence of death dominance (partial r=0.02, p=0.91)'. Conclusion: 'internal consistency check (partial r=0.02)'. Qualifier fix complete. df error tracked as R10-C1.\"\n  resolution_round: 10\n\n- id: \"R9-C1\"\n  summary: \"Cross-env 'validation' is near-tautological\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"MATH absence-of-evidence, not positive replication. Contribution 3 oversells.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper changed to 'cross-context applicability' (from 'validation'). Improvement noted. Residual concern (still overselling) tracked as R10-C3.\"\n  action_items:\n    - round: 9\n      action: \"Reframe Contribution 3.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Contribution 3 now says 'Cross-context applicability'. Discussion says 'true replication requires second catastrophic-failure environment'. Residual concerns in R10-C3.\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"Data scaling ablation uses augmentation — cannot distinguish 'no signal' from 'augmentation cannot create signal'\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. Augmentation ≠ real data.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper now acknowledges 'real-data scaling remains an open question' and distinguishes step-level vs episode-level. Partial fix. Residual overclaiming tracked as R10-C4.\"\n  action_items:\n    - round: 9\n      action: \"Weaken claim, distinguish step vs episode scarcity.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Appendix now has explicit hedging. Residual main-text inconsistency tracked as R10-C4.\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"Capacity scaling: 3 non-comparable data points, non-monotonic curve\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Non-monotonic. 1.7B uses 8 seeds vs 4.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper now acknowledges non-monotonicity and configuration caveat. Partial fix. Confound concern escalated to critical as R10-C5.\"\n  action_items:\n    - round: 9\n      action: \"Acknowledge non-monotonicity in text.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Text now mentions non-monotonicity and seed difference. Remaining confound concern tracked as R10-C5.\"\n  resolution_round: 10\n\n- id: \"R9-W3\"\n  summary: \"MATH p=0.079 underpowered — need post-hoc power analysis\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Need power analysis or TOST.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper now reports power=0.42, N≈770 with Lakens 2017 ref. Reporting fix done. Overclaiming in Intro/Conclusion tracked as R10-W6.\"\n  action_items:\n    - round: 9\n      action: \"Compute post-hoc power + required N.\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Power=0.42, N≈770 reported with citation. Residual claim issue in R10-W6.\"\n  resolution_round: 10\n\n- id: \"R9-W4\"\n  summary: \"Llama replication (N=70, 0 internal-preferred) insufficient for framework generalization claim\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Zero minority-class → only direction generalization.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper narrowed to 'directional consistency... not full framework replication'. Fix done. Residual weakness tracked as R10-W5.\"\n  action_items:\n    - round: 9\n      action: \"Narrow claim to direction generalization.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Claim narrowed. Residual in R10-W5.\"\n  resolution_round: 10\n\n- id: \"R9-W5\"\n  summary: \"Bootstrap CI [0.952, 0.995] on r=0.97 reflects sampling variance only\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"CI measures within-sample stability, not generalization.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper now says 'CI quantifies within-sample uncertainty; generalization to unseen task types requires held-out evaluation'. Caveat added. Cluster bootstrap concern tracked as R10-W4.\"\n  action_items:\n    - round: 9\n      action: \"Add within-sample caveat.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Caveat added in Section 4.1. Cluster bootstrap suggestion in R10-W4.\"\n  resolution_round: 10\n\n- id: \"R9-W6\"\n  summary: \"Over-generalization: Abstract/Conclusion drop 'catastrophic failure mode' qualifier\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [2]\n      note: \"Qualifier exists but not prominent.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract now has 'We demonstrate this in environments with catastrophic failure modes'. Conclusion: 'specific to environments with binary catastrophic outcomes'. Qualifier present and reasonably prominent. Minor residual in R10-m2 (title).\"\n  action_items:\n    - round: 9\n      action: \"Move qualifier to structurally prominent position.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Qualifiers present in Abstract and Conclusion. Title issue tracked as R10-m2.\"\n  resolution_round: 10\n\n- id: \"R9-W7\"\n  summary: \"Internal modality conflates hallucination with reasoning — observation verification ablation missing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Missing ablation: internal + verification.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Discussion now has explicit paragraph: 'augmenting internal strategy with state verification should drive DAF toward zero... illustrating framework's diagnostic utility beyond measurement'. Not raised as critical this round.\"\n  action_items:\n    - round: 9\n      action: \"Add verification discussion.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Discussion paragraph added acknowledging verification as DAF-reducer and framework prediction.\"\n  resolution_round: 10\n\n- id: \"R9-m1\"\n  summary: \"Terminology inconsistency: modality/strategy/computation type used interchangeably\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Minor. §3.1 defines 'modality set M' but experiments use 'pure-strategy trajectories'.\"\n    - round: 10\n      reviewers: []\n      note: \"Not raised by either reviewer this round.\"\n  action_items:\n    - round: 9\n      action: \"Unify terminology or add mapping sentence.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Not flagged in Round 10 — either resolved or deprioritized by reviewers.\"\n  resolution_round: 10\n\n- id: \"R9-m2\"\n  summary: \"78.9% (label-level) vs 90.4% (score-level) juxtaposition semantically unclear\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Readers may conflate when presented together.\"\n    - round: 10\n      reviewers: []\n      note: \"Paper now has parentheticals: '78.9% (label-level, penalty-independent)' / 'DAF=90.4% (score-level, P-dependent)'. Not raised this round.\"\n  action_items:\n    - round: 9\n      action: \"Add parenthetical disambiguation.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Parentheticals added. Not flagged in Round 10.\"\n  resolution_round: 10\n\n- id: \"R9-m3\"\n  summary: \"SCI=0.2147 lacks null distribution baseline\"\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Minor. No permutation null.\"\n  action_items:\n    - round: 9\n      action: \"N/A — SCI not in current paper v129.\"\n      assigned_to: research_director\n      status: done\n  resolution: \"SCI=0.2147 is a project-internal metric not included in the submitted paper. No action needed.\"\n  resolution_round: 9\n\n# Older resolved issues retained for history\n- id: \"R6-C2\"\n  summary: \"Missing counterfactual-in-RL literature paragraph\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Paper uses 'counterfactual' in title, must contextualize.\"\n  action_items:\n    - round: 6\n      action: \"Add paragraph + 3 refs\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"related_work.tex has prospective paired comparison paragraph.\"\n  resolution_round: 6\n\n- id: \"R6-W2\"\n  summary: \"Prescreening 19/30 exclusion — scope qualifier needed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 confirms RESOLVED.\"\n  action_items:\n    - round: 7\n      action: \"Add scope qualifier to title/abstract/conclusion\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Title has 'on ScienceWorld', Abstract has '11 of 30', Appendix B has anti-cherry-picking.\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "simgate-modular-routing",
    "issues_yaml": "- id: \"R10-C1\"\n  summary: \"df=27 statistical error in partial correlation — invalidates key supporting evidence\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. Section 4.1 reports partial r=0.02, p=0.91, df=27. With n=11 task types and 1 control variable, df should be 8. If episode-level (N=245), df=242. df=27 impossible under any valid computation. Error undermines the 'r=0.97 is mathematical artifact' argument — the conclusion likely still holds (r=0.02 is tiny) but statistical reporting is wrong.\"\n  action_items:\n    - round: 10\n      action: \"Recompute partial correlation at task-level (df=8) and report correct p-value. If episode-level was intended, explain why controlling for per-task constant at episode-level is valid.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C2\"\n  summary: \"Core finding novelty insufficient — DAF near-tautological, 78.9% is the real empirical content\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. DAF=δP/(δP+Δ_nd) approaching 1 when P>>Δ_nd is mathematical necessity. The true empirical content is δ=0.2653 and Δ_nd=2.84 (i.e., hallucination-induced death is frequent AND non-death performance gap is negligible). Paper self-acknowledges 'mathematical consequence' but contribution framing still presents as surprising discovery. For EMNLP main conference, contribution sizing may be insufficient without second catastrophic-failure environment.\"\n  action_items:\n    - round: 10\n      action: \"Restructure contribution framing: lead with empirical findings (δ, Δ_nd, 78.9%) not derived metric (DAF). Frame DAF as summary/diagnostic tool, not headline discovery. Consider Findings track positioning if no new environment data.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C3\"\n  summary: \"Single-environment evidence — no cross-env REPLICATION of death-dominance finding\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Cross-env 'validation' near-tautological.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus persists. Paper now says 'cross-context applicability' (improved from 'validation') but Contribution 3 still oversells. MATH=absence-of-evidence, ALFWorld=different mechanism, Llama=direction-only. True validation needs second catastrophic-failure env (NetHack/Crafter). Title says 'the Dominant Routing Signal' based on single env.\"\n  action_items:\n    - round: 10\n      action: \"Option A: Add pilot-scale (50-100 episodes) replication in NetHack or Crafter. Option B: Retitle to scope to ScienceWorld, downgrade Contribution 3 to 'framework illustration', position as Findings track.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C4\"\n  summary: \"Data scaling ablation uses augmentation — cannot rule out real-data scarcity\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Augmentation inflates majority class, doesn't create novel routing patterns.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. Paper partially addressed (now says 'augmentation-based scaling provides no improvement; real-data scaling remains open'). But Section 4.5 still says 'rules out step-level data scarcity' — inconsistent with appendix hedging. Internal recall=0.0 at all scales suggests extreme class imbalance (3.7%) is the driver, not structural limitation.\"\n  action_items:\n    - round: 10\n      action: \"Unify language: remove 'rules out' from main text. Explicit distinction: 'step-level paraphrase diversity (ruled out) vs episode-level minority-class diversity (open, requires ~1,350 real pairs)'. Acknowledge 3.7% class imbalance as primary confound.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C5\"\n  summary: \"Capacity scaling confound — 1.7B uses 8 seeds vs 4 for 0.6B/4B, non-monotonic result\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Non-monotonic curve, 3 non-comparable data points.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. Paper acknowledges non-monotonicity and configuration caveat in caption but text remains confident. R1 escalates: 'only 4B exceeds baseline' claim rests on confounded comparison. Even if trend is real, 59% for 4B params = +9pp is arguably not 'disproportionate' for all use cases.\"\n  action_items:\n    - round: 10\n      action: \"Either rerun 0.6B/1.7B/4B under identical config (same seed count, same split strategy) OR explicitly acknowledge comparison is confounded and weaken conclusion to 'preliminary evidence suggesting capacity matters, but non-monotonicity and configuration differences prevent causal inference'.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W1\"\n  summary: \"Router failure does not 'validate' analytical framework — overclaimed causal link\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. One architecture (Qwen3-1.7B SFT+LoRA) failing ≠ framework validated. Missing: task-type classifier as router, death-risk predictor, real-data scaling. 4B at 59% with upward trend weakens 'disproportionate cost' narrative. 'Validates' → 'is consistent with'.\"\n  action_items:\n    - round: 10\n      action: \"Replace 'validates our analytical methodology' with 'is consistent with' or 'provides evidence that at current scales, learned routing does not improve over the trivial baseline'. Add task-type oracle router baseline (routing signal=task type → task classifier is upper bound).\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"'Environment-agnostic' overclaim — framework requires specific preconditions\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. Framework requires: (1) binary catastrophic outcome, (2) deterministic paired episodes under identical conditions, (3) meaningful 'deterministic modality'. ALFWorld already shows modality definition shifts from 'computation mode' to 'information access'. Findings depend on modality definition choice, not just environment properties.\"\n  action_items:\n    - round: 10\n      action: \"Weaken to 'applicable to environments with binary catastrophic outcomes and controllable modality comparison'. Add sentence: 'findings will vary with modality definition choice'.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W3\"\n  summary: \"Related work gaps — AgentBench, LATS, hallucination detection, Safe RLHF, ToolBench\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2 identified 6 missing refs, R1 agreed on AgentBench/LATS/ToolBench/SafeRLHF. Hallucination literature (SelfCheckGPT/FActScore) highly relevant given 'hallucination→death' is the core mechanism but uncited. NetHack/Crafter mentioned in Conclusion but not formally cited.\"\n  action_items:\n    - round: 10\n      action: \"Add: AgentBench (Liu+ ICLR24), LATS (Zhou+ ICML24), Safe RLHF (Dai+ ICLR24), ToolBench (Qin+ ICLR24), SelfCheckGPT (Manakul+ EMNLP23), NetHack (Küttler+ NeurIPS20), Crafter (Hafner ICLR22). Discuss hallucination detection as potential DAF-reducer.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W4\"\n  summary: \"Bootstrap CI needs cluster-level sensitivity analysis (task-type clusters)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. Episodes within same task type share structure (env dynamics, death risk profile), violating i.i.d. assumption. Cluster bootstrap (11 task-type clusters) would produce wider but more honest CI. Current CI [81.6%, 98.8%] may be over-confident. LOO (Appendix C) partially addresses but only for correlation, not DAF.\"\n  action_items:\n    - round: 10\n      action: \"Report cluster bootstrap CI (resampling at task-type level, 11 clusters) as sensitivity analysis alongside episode-level CI. If substantially wider, discuss implications.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W5\"\n  summary: \"Cross-model evidence (Llama N=70) only shows 'similar model dies more' — unsurprising\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"N=70, 0 internal-preferred, insufficient for framework generalization.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus persists. Paper narrowed claim to 'directional consistency' (good), but both still in 7-8B range with similar hallucination profiles. More informative: 70B model (predict DAF↓) or Reflexion internal baseline (test if self-correction reduces death). Current evidence is unsurprising.\"\n  action_items:\n    - round: 10\n      action: \"Frame as 'preliminary pilot confirming direction' not as meaningful cross-model validation. Add 'larger models with lower hallucination rates' and 'stronger internal strategies (Reflexion)' as explicit testable predictions with expected outcomes.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W6\"\n  summary: \"MATH claim still overclaimed despite power analysis addition\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Need post-hoc power analysis.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper now reports power=0.42, N≈770 (good). But Introduction/Conclusion still say 'consistent with framework prediction' — a power=0.42 non-significant result is consistent with ANY prediction including null. Needs strict downgrade to 'inconclusive'.\"\n  action_items:\n    - round: 10\n      action: \"Replace 'consistent with framework prediction' with 'inconclusive due to insufficient power (0.42); a definitive test requires N≈770'. Remove from Contribution 3 evidence list.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W7\"\n  summary: \"Task selection survivorship bias — SCI=0.2147 'systematic' claim misleading given 63% exclusion\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. SCI computed over 11 selected tasks only. If 19 zero-signal tasks included, signal concentrated in 37% of task space — contradicts 'systematic phenomenon'. Anti-cherry-picking evidence (Appendix B) shows similar det death rates but doesn't address whether excluded tasks have different hallucination/death mechanisms.\"\n  action_items:\n    - round: 10\n      action: \"Weaken 'systematic across nearly all task types' to 'systematic across all task types exhibiting routing signal'. Add Limitations sentence on 63% exclusion's impact on generalization.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-m1\"\n  summary: \"Modality definition disconnect — oracle state ≠ practical tool-use routing\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2 raised as critical (N3), R1 partially rebutted: oracle comparison is standard diagnostic methodology. Consensus: oracle is acceptable for diagnostic framework but paper needs 1-2 paragraphs discussing gap between oracle-state findings and imperfect-tool reality. Currently missing: would death-avoidance still dominate with imperfect tools that themselves can fail?\"\n  action_items:\n    - round: 10\n      action: \"Add Discussion paragraph: 'Our deterministic modality provides an upper bound; with imperfect tools (code interpreters, API calls), tool-induced failures may reduce the death-rate differential, lowering DAF. The safety-first design principle remains applicable but DAF magnitude will depend on tool reliability.'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-m2\"\n  summary: \"Title overclaims — 'the Dominant Routing Signal' verified in single environment only\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 raised, R2 agreed. 'the Dominant' implies universal finding; only ScienceWorld validates. Suggest: 'a Dominant Routing Signal' or scope to 'on ScienceWorld'.\"\n  action_items:\n    - round: 10\n      action: \"Consider title revision: 'Death Avoidance as a Dominant Routing Signal' or keep current but ensure Abstract/Conclusion scope clearly.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# Previously resolved issues — updated status\n- id: \"R6-C1\"\n  summary: \"DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not primary\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Fresh reviewers want full range + formula + dual reporting.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. Abstract still leads with DAF=90.41%. 78.9% present but not co-equal.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers confirm RESOLVED. 78.9% now appears co-equal with DAF throughout.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"REOPENED. R9 reviewers argue DAF=90.4% remains headline despite co-equal presentation.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Framing fix confirmed implemented: Abstract leads with 78.9%, DAF secondary with (score-level, P-dependent) parenthetical. Specific framing issue RESOLVED. Deeper novelty concern captured in R10-C2.\"\n  action_items:\n    - round: 9\n      action: \"78.9% as sole PRIMARY headline; DAF demoted.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Abstract now leads with 78.9% (penalty-independent), DAF presented as 'under P=100, corresponds to DAF=90.4%'. Framing fix complete. Residual novelty concern tracked as R10-C2.\"\n  resolution_round: 10\n\n- id: \"R6-W1\"\n  summary: \"r=0.97 structural coupling — qualifier insufficient in Abstract/Conclusion\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"High r partly mathematical due to penalty coupling.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. §4.1 has caveat but Abstract still reports r=0.97 without qualifier.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"RESOLVED. Abstract now includes structural coupling qualifier.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"REOPENED. 'Partly structural' deemed insufficient.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Qualifier upgraded to 'largely a mathematical consequence' in Abstract; Conclusion says 'internal consistency check'. Qualifier issue RESOLVED. But df=27 error in the statistic itself is NEW issue tracked as R10-C1.\"\n  action_items:\n    - round: 9\n      action: \"Demote r=0.97 to consistency diagnostic, strengthen qualifier.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Abstract: 'largely a mathematical consequence of death dominance (partial r=0.02, p=0.91)'. Conclusion: 'internal consistency check (partial r=0.02)'. Qualifier fix complete. df error tracked as R10-C1.\"\n  resolution_round: 10\n\n- id: \"R9-C1\"\n  summary: \"Cross-env 'validation' is near-tautological\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"MATH absence-of-evidence, not positive replication. Contribution 3 oversells.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper changed to 'cross-context applicability' (from 'validation'). Improvement noted. Residual concern (still overselling) tracked as R10-C3.\"\n  action_items:\n    - round: 9\n      action: \"Reframe Contribution 3.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Contribution 3 now says 'Cross-context applicability'. Discussion says 'true replication requires second catastrophic-failure environment'. Residual concerns in R10-C3.\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"Data scaling ablation uses augmentation — cannot distinguish 'no signal' from 'augmentation cannot create signal'\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. Augmentation ≠ real data.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper now acknowledges 'real-data scaling remains an open question' and distinguishes step-level vs episode-level. Partial fix. Residual overclaiming tracked as R10-C4.\"\n  action_items:\n    - round: 9\n      action: \"Weaken claim, distinguish step vs episode scarcity.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Appendix now has explicit hedging. Residual main-text inconsistency tracked as R10-C4.\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"Capacity scaling: 3 non-comparable data points, non-monotonic curve\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Non-monotonic. 1.7B uses 8 seeds vs 4.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper now acknowledges non-monotonicity and configuration caveat. Partial fix. Confound concern escalated to critical as R10-C5.\"\n  action_items:\n    - round: 9\n      action: \"Acknowledge non-monotonicity in text.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Text now mentions non-monotonicity and seed difference. Remaining confound concern tracked as R10-C5.\"\n  resolution_round: 10\n\n- id: \"R9-W3\"\n  summary: \"MATH p=0.079 underpowered — need post-hoc power analysis\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Need power analysis or TOST.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper now reports power=0.42, N≈770 with Lakens 2017 ref. Reporting fix done. Overclaiming in Intro/Conclusion tracked as R10-W6.\"\n  action_items:\n    - round: 9\n      action: \"Compute post-hoc power + required N.\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Power=0.42, N≈770 reported with citation. Residual claim issue in R10-W6.\"\n  resolution_round: 10\n\n- id: \"R9-W4\"\n  summary: \"Llama replication (N=70, 0 internal-preferred) insufficient for framework generalization claim\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Zero minority-class → only direction generalization.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper narrowed to 'directional consistency... not full framework replication'. Fix done. Residual weakness tracked as R10-W5.\"\n  action_items:\n    - round: 9\n      action: \"Narrow claim to direction generalization.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Claim narrowed. Residual in R10-W5.\"\n  resolution_round: 10\n\n- id: \"R9-W5\"\n  summary: \"Bootstrap CI [0.952, 0.995] on r=0.97 reflects sampling variance only\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"CI measures within-sample stability, not generalization.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper now says 'CI quantifies within-sample uncertainty; generalization to unseen task types requires held-out evaluation'. Caveat added. Cluster bootstrap concern tracked as R10-W4.\"\n  action_items:\n    - round: 9\n      action: \"Add within-sample caveat.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Caveat added in Section 4.1. Cluster bootstrap suggestion in R10-W4.\"\n  resolution_round: 10\n\n- id: \"R9-W6\"\n  summary: \"Over-generalization: Abstract/Conclusion drop 'catastrophic failure mode' qualifier\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [2]\n      note: \"Qualifier exists but not prominent.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Abstract now has 'We demonstrate this in environments with catastrophic failure modes'. Conclusion: 'specific to environments with binary catastrophic outcomes'. Qualifier present and reasonably prominent. Minor residual in R10-m2 (title).\"\n  action_items:\n    - round: 9\n      action: \"Move qualifier to structurally prominent position.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Qualifiers present in Abstract and Conclusion. Title issue tracked as R10-m2.\"\n  resolution_round: 10\n\n- id: \"R9-W7\"\n  summary: \"Internal modality conflates hallucination with reasoning — observation verification ablation missing\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Missing ablation: internal + verification.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Discussion now has explicit paragraph: 'augmenting internal strategy with state verification should drive DAF toward zero... illustrating framework's diagnostic utility beyond measurement'. Not raised as critical this round.\"\n  action_items:\n    - round: 9\n      action: \"Add verification discussion.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Discussion paragraph added acknowledging verification as DAF-reducer and framework prediction.\"\n  resolution_round: 10\n\n- id: \"R9-m1\"\n  summary: \"Terminology inconsistency: modality/strategy/computation type used interchangeably\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Minor. §3.1 defines 'modality set M' but experiments use 'pure-strategy trajectories'.\"\n    - round: 10\n      reviewers: []\n      note: \"Not raised by either reviewer this round.\"\n  action_items:\n    - round: 9\n      action: \"Unify terminology or add mapping sentence.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Not flagged in Round 10 — either resolved or deprioritized by reviewers.\"\n  resolution_round: 10\n\n- id: \"R9-m2\"\n  summary: \"78.9% (label-level) vs 90.4% (score-level) juxtaposition semantically unclear\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Readers may conflate when presented together.\"\n    - round: 10\n      reviewers: []\n      note: \"Paper now has parentheticals: '78.9% (label-level, penalty-independent)' / 'DAF=90.4% (score-level, P-dependent)'. Not raised this round.\"\n  action_items:\n    - round: 9\n      action: \"Add parenthetical disambiguation.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Parentheticals added. Not flagged in Round 10.\"\n  resolution_round: 10\n\n- id: \"R9-m3\"\n  summary: \"SCI=0.2147 lacks null distribution baseline\"\n  category: method\n  severity: info\n  status: wont_fix\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Minor. No permutation null.\"\n  action_items:\n    - round: 9\n      action: \"N/A — SCI not in current paper v129.\"\n      assigned_to: research_director\n      status: done\n  resolution: \"SCI=0.2147 is a project-internal metric not included in the submitted paper. No action needed.\"\n  resolution_round: 9\n\n# Older resolved issues retained for history\n- id: \"R6-C2\"\n  summary: \"Missing counterfactual-in-RL literature paragraph\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Paper uses 'counterfactual' in title, must contextualize.\"\n  action_items:\n    - round: 6\n      action: \"Add paragraph + 3 refs\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"related_work.tex has prospective paired comparison paragraph.\"\n  resolution_round: 6\n\n- id: \"R6-W2\"\n  summary: \"Prescreening 19/30 exclusion — scope qualifier needed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 confirms RESOLVED.\"\n  action_items:\n    - round: 7\n      action: \"Add scope qualifier to title/abstract/conclusion\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Title has 'on ScienceWorld', Abstract has '11 of 30', Appendix B has anti-cherry-picking.\"\n  resolution_round: 8"
  }
}
```

</details>

---


### Tool result

_source line 791 · 2026-05-16T19:53:35.337340+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 26217}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-16T19:56:30.833449+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 10 审稿报告 — simgate-modular-routing\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**Venue**: EMNLP 2026 Main Conference Long Paper (ARR May cycle, deadline 2026-05-25)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）\n**流程**: Round 1 独立审稿 → 交叉分享 → 1 轮即达共识\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual analysis 框架和 Death Avoidance Factor (DAF) 指标，分解 modular LLM agent 的 routing signal 来源。在 ScienceWorld（11/30 task types, N=245, Qwen2.5-7B-Instruct）上发现 78.9% 的 non-tie routing labels（75/95, penalty-independent）由 death asymmetry 驱动；DAF=90.4%（P=100, score-level）。一个探索性 router 在 held-out episodes 上低于 chance（47.1% vs 50%）。跨环境（MATH N=300, ALFWorld N=135）和跨模型（Llama-3.1-8B, N=70）对比提供方向性辅助证据。\n\n---\n\n## Strengths\n\n**S1. 问题定位有价值。** 在 routing 文献专注 \"how to route\" 时，追问 \"what drives routing signal\" 是更基础的元问题，具有方法论价值。\n\n**S2. 统计报告诚实严格。** 主动报告 partial r=0.02 暴露 r=0.97 的数学必然性；标注 MATH p=0.079 \"not reaching α=0.05\"（power=0.42, N≈770）；bootstrap/LOO/Spearman 三重 robustness；8-seed cross-split evaluation。在 LLM agent 论文中属上乘。\n\n**S3. 框架设计清晰可复现。** Algorithm 1 完备无歧义，penalty-independent (78.9%) 与 penalty-dependent (DAF) 两个互补指标的区分有思考，环境间异质性验证框架灵活性。\n\n**S4. Negative result 诚实且有诊断价值。** Router failure + always-deterministic near-optimality + majority-class collapse 的组合对社区有建设性信息。\n\n**S5. Limitations 实质性强。** 19/30 exclusion、penalty amplification、single-pass ReAct、distribution shift（DAgger）、7-8B scale 限制均主动列出。\n\n**S6. 相对前几轮的改进明显。** 78.9% 现为 primary metric、r=0.97 标注 \"largely mathematical consequence\"、MATH 报告 power analysis、Llama 收窄到 \"directional consistency\"、within-sample CI caveat 添加——历次审稿意见得到了认真 addressing。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical) — 5 条\n\n**C1. df=27 统计错误 [Consensus, NEW]**\n- Section 4.1: \"partial r = 0.02 (p = 0.91, df = 27)\"。散点图 n=11 task types，控制 1 变量后 df 应为 8。若 episode-level（N=245）则 df=242。df=27 在任何合理计算下不成立。\n- 虽然 r=0.02 极小（结论大概率不变），但这是论文 \"r=0.97 is mathematical artifact\" 论证的核心支撑，统计报告错误削弱方法论可信度。\n- **要求**：明确计算 level，报告正确 df 和 p-value。\n\n**C2. 核心发现 novelty 不足——DAF 接近 tautological [Consensus]**\n- DAF = δP/(δP + Δ_nd) 在 P >> Δ_nd 时数学上必然趋近 1。P=100 而 Δ_nd=2.84，DAF 高是算术必然而非经验发现。论文多处自承 \"mathematical consequence\"。\n- 真正的 empirical content 是 δ=0.2653（42.9% vs 16.3% death rate）和 Δ_nd=2.84（排除 death 后近乎无差异）。78.9% label fraction 是 penalty-independent 的经验发现。\n- 论文已将 78.9% 置于 primary 位置（R9 修复），但 contribution framing 仍将 DAF 作为 key metric，且 title 暗示 \"discovery\"。对 EMNLP main conference，contribution sizing 存疑。\n- **要求**：重构 contribution 叙事——以 δ 和 Δ_nd 的经验发现为核心，DAF 为 summary tool。或补充第二环境数据提升 convincingness。\n\n**C3. 单一环境证据——无 death-dominance 的跨环境 REPLICATION [Consensus]**\n- MATH: absence-of-evidence（no death → no death signal，power=0.42）。ALFWorld: 不同 mechanism。Llama: direction-only。Title 说 \"the Dominant Routing Signal\" 但仅 ScienceWorld 验证。\n- 论文 Contribution 3 现为 \"cross-context applicability\"——改善但仍 overselling。Discussion 自承需 NetHack/Crafter。\n- **要求**：Option A: pilot-scale 50-100 episodes 在第二个 catastrophic-failure 环境复现。Option B: 收缩到 \"ScienceWorld-specific case study + framework proposal\"，Findings track 定位。\n\n**C4. Data scaling ablation 方法论缺陷 [Consensus]**\n- Paraphrase augmentation 将 majority class 从 89.6% 膨胀至 97.7%，不生成新 routing patterns。Internal recall=0.0 at all scales（完全 majority-class collapse）可能反映 3.7% 极端 class imbalance 而非 structural limitation。\n- Appendix 有 hedging（\"real-data scaling remains open\"），但 Section 4.5 仍有 \"rules out step-level data scarcity\" 表述——不一致。\n- **要求**：主文统一为 \"augmentation-based scaling provides no improvement; real-data scaling (requiring ~1,350 pairs for 50 minority-class examples) remains open\"。明确区分 step-level paraphrase diversity（ruled out）vs episode-level minority-class diversity（open）。\n\n**C5. Capacity scaling confound 未控制 [Consensus]**\n- 0.6B: 50.7%, 1.7B: 47.1%, 4B: 59.0% — non-monotonic。1.7B 用 8 seeds vs 0.6B/4B 用 4 seeds。\n- \"only 4B exceeds the baseline\" 是 key claim 但基于 confounded comparison。1.7B 低于 0.6B 已不支持 \"capacity matters\" 的单调叙事。\n- **要求**：相同配置重跑 OR 显式承认 \"comparison is confounded, causal inference not supported\" 并弱化结论。\n\n### Should-Fix (Warning) — 7 条\n\n**W1. Router \"validates\" 措辞过强 [Consensus]**\n- 一个架构（Qwen3-1.7B）失败 ≠ 框架被 validated。缺失：task-type classifier router、death-risk predictor、real-data scaling。4B 趋势上升（+9pp）不支持 \"disproportionate cost\" 作为绝对判断。\n- **建议**：\"validates\" → \"is consistent with\" / \"provides evidence that at current scales...\"\n\n**W2. \"Environment-agnostic\" overclaim [Consensus]**\n- 框架要求 binary catastrophic outcome + deterministic paired episodes + meaningful modality。ALFWorld 已暴露 modality 定义从 computation mode 到 information access 的漂移。\n- **建议**：弱化为 \"applicable to environments with binary catastrophic outcomes and controllable modality comparison\"。\n\n**W3. Related work 遗漏 [Consensus]**\n- 缺：AgentBench (Liu+ ICLR24)、LATS (Zhou+ ICML24)、Safe RLHF (Dai+ ICLR24)、ToolBench (Qin+ ICLR24)、SelfCheckGPT (Manakul+ EMNLP23)、NetHack (Küttler+ NeurIPS20)、Crafter (Hafner ICLR22)。\n- \"Hallucination → death\" 是核心机制但无 hallucination detection 文献引用。\n\n**W4. Bootstrap CI 需 cluster-level sensitivity [Consensus]**\n- Episodes within same task type 共享结构（env dynamics, death risk profile），违反 i.i.d.。Cluster bootstrap（11 task-type clusters）CI 会更宽但更诚实。\n- **建议**：报告 cluster bootstrap CI 作为 sensitivity analysis。\n\n**W5. Cross-model 证据弱——仅覆盖 similar-capability 7-8B models [Consensus]**\n- Llama-3.1-8B 复制仅证明 \"another 7-8B model dies more in internal mode\"——考虑 hallucination rate 本身高，不令人惊讶。\n- **建议**：frame 为 \"preliminary pilot\"，将 70B 和 Reflexion 作为 explicit testable predictions。\n\n**W6. MATH \"consistent with prediction\" 在 power=0.42 下 overclaimed [Consensus]**\n- 42% power 的 non-significant result 与任何 prediction 都 consistent（包括 null）。不是 confirmatory evidence。\n- **建议**：\"The MATH evaluation was inconclusive due to insufficient power (0.42); a definitive test requires N≈770.\"\n\n**W7. Task selection survivorship bias / SCI [Consensus]**\n- SCI=0.2147 \"systematic phenomenon\" 仅在 11 个已选 task types 上成立。63% exclusion 后，routing signal 集中在 37% task space。\n- **建议**：弱化为 \"systematic across all task types exhibiting routing signal\"。\n\n### Nice-to-Fix (Info) — 3 条\n\n**M1. Modality 定义与实际 tool-use routing 的 gap 需讨论**\n- Oracle state ≠ imperfect tools (code interpreter, API calls)。框架定位为 diagnostic（oracle as upper bound）是合理的，但需 1-2 段讨论 implications for practical tool-use design。\n\n**M2. Title \"the Dominant\" 仅单环境验证**\n- 建议 \"a Dominant\" 或保持但确保 scope 清晰。\n\n**M3. 其他小问题**\n- NetHack/Crafter 在 Conclusion 提到但未 cite\n- Ethics Statement 未报 GPU 型号\n- P=0 时 DAF CI 包含负数（ill-defined）——应注明 well-definedness 条件\n- \"Oracle degeneracy\" 首次使用未定义\n- Abstract 数字密集（5 百分比 + 3 p-value + CI），建议精简\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下判断上完全一致 [AGREE]：\n1. df=27 是统计错误，需立即修正\n2. DAF=90.4% 的 headline 价值接近 tautological；78.9% 是更稳健的 empirical content\n3. Cross-env evidence 无一 replicate death-dominance finding\n4. Data scaling augmentation 不能 rule out real-data scarcity\n5. Capacity scaling 的 non-monotonicity 使因果推断不可靠\n6. 方法论框架本身（Algorithm 1 + 双指标设计）是 solid 的\n7. Negative result（router fails）有 community diagnostic value\n8. 统计报告透明度在 NLP 论文中属上乘\n9. 论文处于 borderline / Findings track 水平\n10. Bootstrap 需 cluster sensitivity；MATH claim overclaimed；cross-model 仅 direction-consistent\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 判定 |\n|------|----|----|--------------|\n| Modality 定义与 tool-use 脱节（R2-N3） | Partial REBUT: oracle is standard diagnostic methodology | Critical: readers expect practical routing implications | **Info**: oracle comparison 合理但需补 practical gap 讨论。降级为 M1 |\n| Algorithm 1 隐含假设（R1-W4） | Should-Fix: both-dead 不区分 early/late death | Partial REBUT: paper already addresses in multiple locations | **Resolved in current version**: 35 both-dead episodes excluded from all analysis; integer scores justify exact comparison; impact limited |\n| 论文定位（main vs Findings） | 2.5/5, \"resubmit next cycle\" | 3.0/5, \"Findings track recommended\" | 综合：**borderline**，修复 C1-C5 framing issues（无需新实验）可达 Findings weak accept；补充第二环境可达 main conference |\n\n---\n\n## Questions（需作者回应）\n\n**Q1.** Partial correlation df=27 的来源？Task-level（df=8）还是 episode-level（df=242）？\n\n**Q2.** 在 death-asymmetry 的 75 个 labels 中，有多少 episodes 即使未死也会产生相同 label（score comparison 一致）？这量化 death-asymmetry labeling 的 \"redundancy\"。\n\n**Q3.** 如果用 task-type 作为 routing feature（one-hot），router 的 episode-level accuracy 是多少？这直接验证 \"routing signal = task type\" claim。\n\n**Q4.** 1.7B 在 4-seed 配置下的 episode-level accuracy？这判断 non-monotonicity 是否是 artifact。\n\n**Q5.** 为什么不在 NetHack/Crafter 中做 50-100 episodes 的 pilot replication？这是提升 generalization 证据力度最直接的路径。\n\n**Q6.** Score-comparison labels（20 个）中，det vs int 分数差的中位数和分布？如果多数 <5 points，practical significance 需讨论。\n\n**Q7.** 30-step budget 的选择依据？更大 budget 下 internal death rate 是收敛还是继续上升？\n\n---\n\n## Missing References\n\n- **Liu et al. (2024)**. AgentBench: Evaluating LLMs as Agents. ICLR 2024.\n- **Zhou et al. (2024)**. Language Agent Tree Search. ICML 2024.\n- **Manakul et al. (2023)**. SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection. EMNLP 2023.\n- **Dai et al. (2024)**. Safe RLHF. ICLR 2024.\n- **Qin et al. (2024)**. ToolBench. ICLR 2024.\n- **Küttler et al. (2020)**. The NetHack Learning Environment. NeurIPS 2020.\n- **Hafner (2022)**. Benchmarking the Spectrum of Agent Capabilities (Crafter). ICLR 2022.\n- **Lakens (2017)**. Equivalence Tests. — 已 cite，确认 ✓\n- **Ren et al. (2024)**. When to Trust Language Models: Safety and Reliability Survey.\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。\n\n---\n\n## Overall Assessment\n\n**评分**: borderline (2.75/5)\n**置信度**: 4/5\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.25 |\n| Excitement / Novelty | 2.5 | 2.5 | 2.5 |\n| Reproducibility | 3.5 | 4.0 | 3.75 |\n| Overall | 2.5 | 3.0 | **2.75** |\n\n**综合判断**：\n\n方法论框架设计 solid（Algorithm 1 + 双指标），统计报告诚实（自我批判 r=0.97、报告 negative result），对社区有建设性。但存在 5 个 Critical 问题：\n\n1. **df=27 统计错误**——可修复但暴露审校不足\n2. **核心发现接近 tautological**——DAF 是 P 的数学函数非经验发现，contribution sizing for EMNLP main 存疑\n3. **单环境证据**——title claims \"the Dominant\" 但仅 ScienceWorld 验证，cross-env checks 均非 replication\n4. **Data scaling ablation 方法论缺陷**——augmentation ≠ real data, \"structural limitation\" 结论过强\n5. **Capacity scaling confound**——seed 配置不一致使因果推断不可靠\n\n这些问题中，C1/C4/C5 是 framing/reporting 修复（无需新实验），C2 需要 reframing contribution narrative，C3 最理想需要新实验数据（或降级定位）。\n\n**可接收路径**：\n- **Findings track (最小修改)**：修复 C1 统计错误 + C4/C5 claim 弱化 + C2 贡献重新定位为 \"single-environment case study + framework proposal\" + C3 title/contribution 收窄。纯 writing/framing 修改，无需新实验。\n- **Main conference (需新数据)**：上述全部 + NetHack/Crafter pilot replication（50-100 episodes）+ 相同配置 capacity scaling 重跑。\n\n当前论文处于 Findings track borderline 水平。相比 Round 9，论文在 framing（78.9% primary）、power analysis 报告、claim scoping 方面有明显改善，但核心 contribution sizing 问题（novelty + single-environment）未改变——这是结构性问题而非 writing 修复可解。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 数字密集，建议精简到 2-3 key numbers + insight statement\n- \"largely a mathematical consequence\" qualifier 到位（R9 修复确认）\n- 结尾 \"routing problem reduces to safety-first modality selection\" qualifier \"in environments with catastrophic failure modes\" 在位但 structurally 不够突出——reader fast-scanning 可能遗漏\n\n### §3.4 (DAF Definition)\n- \"DAF should be interpreted relative to the environment's penalty magnitude\" caveat 已存在 — good\n- 建议补充：当 P → 0，DAF → 0 且 CI 包含负数（Table 8, P=0: [-36.7, 83.1]），说明 metric 仅在 P 显著时 well-defined\n\n### §4.1 (Death Decomposition)\n- df=27 需立即修正\n- r=0.97 降级为 \"internal consistency check\" — good（R9 修复确认）\n- partial r 的 \"controlling for δ·P\" 语义需澄清：在 task-level 这等于控制 δ（因 P 恒定），需解释\n\n### §4.3 (MATH)\n- Power analysis 添加 — good\n- \"consistent with framework prediction\" 需降级为 \"inconclusive\"\n\n### §4.5 (Router Diagnostic)\n- \"validates\" → \"is consistent with\"\n- \"rules out step-level data scarcity\" 需与 appendix hedging 统一\n- Non-monotonicity 正文需 acknowledge（不仅 caption）\n\n### Contribution List (Introduction)\n- Contribution 2: \"capacity-dependent limitation\" 基于 confounded data，需加 caveat\n- Contribution 3: \"cross-context applicability\" → \"cross-context illustration\" 或 \"framework flexibility demonstration\"\n\n### Related Work\n- 补充 hallucination detection 段落（SelfCheckGPT 等）——\"hallucination → death\" 是核心机制但未连接到 hallucination literature\n- AgentBench/LATS 补充到 LLM Agent 段落\n- Safe RLHF 补充到 Safe RL 段落",
  "project": "simgate-modular-routing",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 10 审稿报告 — simgate-modular-routing\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**Venue**: EMNLP 2026 Main Conference Long Paper (ARR May cycle, deadline 2026-05-25)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）\n**流程**: Round 1 独立审稿 → 交叉分享 → 1 轮即达共识\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual analysis 框架和 Death Avoidance Factor (DAF) 指标，分解 modular LLM agent 的 routing signal 来源。在 ScienceWorld（11/30 task types, N=245, Qwen2.5-7B-Instruct）上发现 78.9% 的 non-tie routing labels（75/95, penalty-independent）由 death asymmetry 驱动；DAF=90.4%（P=100, score-level）。一个探索性 router 在 held-out episodes 上低于 chance（47.1% vs 50%）。跨环境（MATH N=300, ALFWorld N=135）和跨模型（Llama-3.1-8B, N=70）对比提供方向性辅助证据。\n\n---\n\n## Strengths\n\n**S1. 问题定位有价值。** 在 routing 文献专注 \"how to route\" 时，追问 \"what drives routing signal\" 是更基础的元问题，具有方法论价值。\n\n**S2. 统计报告诚实严格。** 主动报告 partial r=0.02 暴露 r=0.97 的数学必然性；标注 MATH p=0.079 \"not reaching α=0.05\"（power=0.42, N≈770）；bootstrap/LOO/Spearman 三重 robustness；8-seed cross-split evaluation。在 LLM agent 论文中属上乘。\n\n**S3. 框架设计清晰可复现。** Algorithm 1 完备无歧义，penalty-independent (78.9%) 与 penalty-dependent (DAF) 两个互补指标的区分有思考，环境间异质性验证框架灵活性。\n\n**S4. Negative result 诚实且有诊断价值。** Router failure + always-deterministic near-optimality + majority-class collapse 的组合对社区有建设性信息。\n\n**S5. Limitations 实质性强。** 19/30 exclusion、penalty amplification、single-pass ReAct、distribution shift（DAgger）、7-8B scale 限制均主动列出。\n\n**S6. 相对前几轮的改进明显。** 78.9% 现为 primary metric、r=0.97 标注 \"largely mathematical consequence\"、MATH 报告 power analysis、Llama 收窄到 \"directional consistency\"、within-sample CI caveat 添加——历次审稿意见得到了认真 addressing。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical) — 5 条\n\n**C1. df=27 统计错误 [Consensus, NEW]**\n- Section 4.1: \"partial r = 0.02 (p = 0.91, df = 27)\"。散点图 n=11 task types，控制 1 变量后 df 应为 8。若 episode-level（N=245）则 df=242。df=27 在任何合理计算下不成立。\n- 虽然 r=0.02 极小（结论大概率不变），但这是论文 \"r=0.97 is mathematical artifact\" 论证的核心支撑，统计报告错误削弱方法论可信度。\n- **要求**：明确计算 level，报告正确 df 和 p-value。\n\n**C2. 核心发现 novelty 不足——DAF 接近 tautological [Consensus]**\n- DAF = δP/(δP + Δ_nd) 在 P >> Δ_nd 时数学上必然趋近 1。P=100 而 Δ_nd=2.84，DAF 高是算术必然而非经验发现。论文多处自承 \"mathematical consequence\"。\n- 真正的 empirical content 是 δ=0.2653（42.9% vs 16.3% death rate）和 Δ_nd=2.84（排除 death 后近乎无差异）。78.9% label fraction 是 penalty-independent 的经验发现。\n- 论文已将 78.9% 置于 primary 位置（R9 修复），但 contribution framing 仍将 DAF 作为 key metric，且 title 暗示 \"discovery\"。对 EMNLP main conference，contribution sizing 存疑。\n- **要求**：重构 contribution 叙事——以 δ 和 Δ_nd 的经验发现为核心，DAF 为 summary tool。或补充第二环境数据提升 convincingness。\n\n**C3. 单一环境证据——无 death-dominance 的跨环境 REPLICATION [Consensus]**\n- MATH: absence-of-evidence（no death → no death signal，power=0.42）。ALFWorld: 不同 mechanism。Llama: direction-only。Title 说 \"the Dominant Routing Signal\" 但仅 ScienceWorld 验证。\n- 论文 Contribution 3 现为 \"cross-context applicability\"——改善但仍 overselling。Discussion 自承需 NetHack/Crafter。\n- **要求**：Option A: pilot-scale 50-100 episodes 在第二个 catastrophic-failure 环境复现。Option B: 收缩到 \"ScienceWorld-specific case study + framework proposal\"，Findings track 定位。\n\n**C4. Data scaling ablation 方法论缺陷 [Consensus]**\n- Paraphrase augmentation 将 majority class 从 89.6% 膨胀至 97.7%，不生成新 routing patterns。Internal recall=0.0 at all scales（完全 majority-class collapse）可能反映 3.7% 极端 class imbalance 而非 structural limitation。\n- Appendix 有 hedging（\"real-data scaling remains open\"），但 Section 4.5 仍有 \"rules out step-level data scarcity\" 表述——不一致。\n- **要求**：主文统一为 \"augmentation-based scaling provides no improvement; real-data scaling (requiring ~1,350 pairs for 50 minority-class examples) remains open\"。明确区分 step-level paraphrase diversity（ruled out）vs episode-level minority-class diversity（open）。\n\n**C5. Capacity scaling confound 未控制 [Consensus]**\n- 0.6B: 50.7%, 1.7B: 47.1%, 4B: 59.0% — non-monotonic。1.7B 用 8 seeds vs 0.6B/4B 用 4 seeds。\n- \"only 4B exceeds the baseline\" 是 key claim 但基于 confounded comparison。1.7B 低于 0.6B 已不支持 \"capacity matters\" 的单调叙事。\n- **要求**：相同配置重跑 OR 显式承认 \"comparison is confounded, causal inference not supported\" 并弱化结论。\n\n### Should-Fix (Warning) — 7 条\n\n**W1. Router \"validates\" 措辞过强 [Consensus]**\n- 一个架构（Qwen3-1.7B）失败 ≠ 框架被 validated。缺失：task-type classifier router、death-risk predictor、real-data scaling。4B 趋势上升（+9pp）不支持 \"disproportionate cost\" 作为绝对判断。\n- **建议**：\"validates\" → \"is consistent with\" / \"provides evidence that at current scales...\"\n\n**W2. \"Environment-agnostic\" overclaim [Consensus]**\n- 框架要求 binary catastrophic outcome + deterministic paired episodes + meaningful modality。ALFWorld 已暴露 modality 定义从 computation mode 到 information access 的漂移。\n- **建议**：弱化为 \"applicable to environments with binary catastrophic outcomes and controllable modality comparison\"。\n\n**W3. Related work 遗漏 [Consensus]**\n- 缺：AgentBench (Liu+ ICLR24)、LATS (Zhou+ ICML24)、Safe RLHF (Dai+ ICLR24)、ToolBench (Qin+ ICLR24)、SelfCheckGPT (Manakul+ EMNLP23)、NetHack (Küttler+ NeurIPS20)、Crafter (Hafner ICLR22)。\n- \"Hallucination → death\" 是核心机制但无 hallucination detection 文献引用。\n\n**W4. Bootstrap CI 需 cluster-level sensitivity [Consensus]**\n- Episodes within same task type 共享结构（env dynamics, death risk profile），违反 i.i.d.。Cluster bootstrap（11 task-type clusters）CI 会更宽但更诚实。\n- **建议**：报告 cluster bootstrap CI 作为 sensitivity analysis。\n\n**W5. Cross-model 证据弱——仅覆盖 similar-capability 7-8B models [Consensus]**\n- Llama-3.1-8B 复制仅证明 \"another 7-8B model dies more in internal mode\"——考虑 hallucination rate 本身高，不令人惊讶。\n- **建议**：frame 为 \"preliminary pilot\"，将 70B 和 Reflexion 作为 explicit testable predictions。\n\n**W6. MATH \"consistent with prediction\" 在 power=0.42 下 overclaimed [Consensus]**\n- 42% power 的 non-significant result 与任何 prediction 都 consistent（包括 null）。不是 confirmatory evidence。\n- **建议**：\"The MATH evaluation was inconclusive due to insufficient power (0.42); a definitive test requires N≈770.\"\n\n**W7. Task selection survivorship bias / SCI [Consensus]**\n- SCI=0.2147 \"systematic phenomenon\" 仅在 11 个已选 task types 上成立。63% exclusion 后，routing signal 集中在 37% task space。\n- **建议**：弱化为 \"systematic across all task types exhibiting routing signal\"。\n\n### Nice-to-Fix (Info) — 3 条\n\n**M1. Modality 定义与实际 tool-use routing 的 gap 需讨论**\n- Oracle state ≠ imperfect tools (code interpreter, API calls)。框架定位为 diagnostic（oracle as upper bound）是合理的，但需 1-2 段讨论 implications for practical tool-use design。\n\n**M2. Title \"the Dominant\" 仅单环境验证**\n- 建议 \"a Dominant\" 或保持但确保 scope 清晰。\n\n**M3. 其他小问题**\n- NetHack/Crafter 在 Conclusion 提到但未 cite\n- Ethics Statement 未报 GPU 型号\n- P=0 时 DAF CI 包含负数（ill-defined）——应注明 well-definedness 条件\n- \"Oracle degeneracy\" 首次使用未定义\n- Abstract 数字密集（5 百分比 + 3 p-value + CI），建议精简\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下判断上完全一致 [AGREE]：\n1. df=27 是统计错误，需立即修正\n2. DAF=90.4% 的 headline 价值接近 tautological；78.9% 是更稳健的 empirical content\n3. Cross-env evidence 无一 replicate death-dominance finding\n4. Data scaling augmentation 不能 rule out real-data scarcity\n5. Capacity scaling 的 non-monotonicity 使因果推断不可靠\n6. 方法论框架本身（Algorithm 1 + 双指标设计）是 solid 的\n7. Negative result（router fails）有 community diagnostic value\n8. 统计报告透明度在 NLP 论文中属上乘\n9. 论文处于 borderline / Findings track 水平\n10. Bootstrap 需 cluster sensitivity；MATH claim overclaimed；cross-model 仅 direction-consistent\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 判定 |\n|------|----|----|--------------|\n| Modality 定义与 tool-use 脱节（R2-N3） | Partial REBUT: oracle is standard diagnostic methodology | Critical: readers expect practical routing implications | **Info**: oracle comparison 合理但需补 practical gap 讨论。降级为 M1 |\n| Algorithm 1 隐含假设（R1-W4） | Should-Fix: both-dead 不区分 early/late death | Partial REBUT: paper already addresses in multiple locations | **Resolved in current version**: 35 both-dead episodes excluded from all analysis; integer scores justify exact comparison; impact limited |\n| 论文定位（main vs Findings） | 2.5/5, \"resubmit next cycle\" | 3.0/5, \"Findings track recommended\" | 综合：**borderline**，修复 C1-C5 framing issues（无需新实验）可达 Findings weak accept；补充第二环境可达 main conference |\n\n---\n\n## Questions（需作者回应）\n\n**Q1.** Partial correlation df=27 的来源？Task-level（df=8）还是 episode-level（df=242）？\n\n**Q2.** 在 death-asymmetry 的 75 个 labels 中，有多少 episodes 即使未死也会产生相同 label（score comparison 一致）？这量化 death-asymmetry labeling 的 \"redundancy\"。\n\n**Q3.** 如果用 task-type 作为 routing feature（one-hot），router 的 episode-level accuracy 是多少？这直接验证 \"routing signal = task type\" claim。\n\n**Q4.** 1.7B 在 4-seed 配置下的 episode-level accuracy？这判断 non-monotonicity 是否是 artifact。\n\n**Q5.** 为什么不在 NetHack/Crafter 中做 50-100 episodes 的 pilot replication？这是提升 generalization 证据力度最直接的路径。\n\n**Q6.** Score-comparison labels（20 个）中，det vs int 分数差的中位数和分布？如果多数 <5 points，practical significance 需讨论。\n\n**Q7.** 30-step budget 的选择依据？更大 budget 下 internal death rate 是收敛还是继续上升？\n\n---\n\n## Missing References\n\n- **Liu et al. (2024)**. AgentBench: Evaluating LLMs as Agents. ICLR 2024.\n- **Zhou et al. (2024)**. Language Agent Tree Search. ICML 2024.\n- **Manakul et al. (2023)**. SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection. EMNLP 2023.\n- **Dai et al. (2024)**. Safe RLHF. ICLR 2024.\n- **Qin et al. (2024)**. ToolBench. ICLR 2024.\n- **Küttler et al. (2020)**. The NetHack Learning Environment. NeurIPS 2020.\n- **Hafner (2022)**. Benchmarking the Spectrum of Agent Capabilities (Crafter). ICLR 2022.\n- **Lakens (2017)**. Equivalence Tests. — 已 cite，确认 ✓\n- **Ren et al. (2024)**. When to Trust Language Models: Safety and Reliability Survey.\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。\n\n---\n\n## Overall Assessment\n\n**评分**: borderline (2.75/5)\n**置信度**: 4/5\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.25 |\n| Excitement / Novelty | 2.5 | 2.5 | 2.5 |\n| Reproducibility | 3.5 | 4.0 | 3.75 |\n| Overall | 2.5 | 3.0 | **2.75** |\n\n**综合判断**：\n\n方法论框架设计 solid（Algorithm 1 + 双指标），统计报告诚实（自我批判 r=0.97、报告 negative result），对社区有建设性。但存在 5 个 Critical 问题：\n\n1. **df=27 统计错误**——可修复但暴露审校不足\n2. **核心发现接近 tautological**——DAF 是 P 的数学函数非经验发现，contribution sizing for EMNLP main 存疑\n3. **单环境证据**——title claims \"the Dominant\" 但仅 ScienceWorld 验证，cross-env checks 均非 replication\n4. **Data scaling ablation 方法论缺陷**——augmentation ≠ real data, \"structural limitation\" 结论过强\n5. **Capacity scaling confound**——seed 配置不一致使因果推断不可靠\n\n这些问题中，C1/C4/C5 是 framing/reporting 修复（无需新实验），C2 需要 reframing contribution narrative，C3 最理想需要新实验数据（或降级定位）。\n\n**可接收路径**：\n- **Findings track (最小修改)**：修复 C1 统计错误 + C4/C5 claim 弱化 + C2 贡献重新定位为 \"single-environment case study + framework proposal\" + C3 title/contribution 收窄。纯 writing/framing 修改，无需新实验。\n- **Main conference (需新数据)**：上述全部 + NetHack/Crafter pilot replication（50-100 episodes）+ 相同配置 capacity scaling 重跑。\n\n当前论文处于 Findings track borderline 水平。相比 Round 9，论文在 framing（78.9% primary）、power analysis 报告、claim scoping 方面有明显改善，但核心 contribution sizing 问题（novelty + single-environment）未改变——这是结构性问题而非 writing 修复可解。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 数字密集，建议精简到 2-3 key numbers + insight statement\n- \"largely a mathematical consequence\" qualifier 到位（R9 修复确认）\n- 结尾 \"routing problem reduces to safety-first modality selection\" qualifier \"in environments with catastrophic failure modes\" 在位但 structurally 不够突出——reader fast-scanning 可能遗漏\n\n### §3.4 (DAF Definition)\n- \"DAF should be interpreted relative to the environment's penalty magnitude\" caveat 已存在 — good\n- 建议补充：当 P → 0，DAF → 0 且 CI 包含负数（Table 8, P=0: [-36.7, 83.1]），说明 metric 仅在 P 显著时 well-defined\n\n### §4.1 (Death Decomposition)\n- df=27 需立即修正\n- r=0.97 降级为 \"internal consistency check\" — good（R9 修复确认）\n- partial r 的 \"controlling for δ·P\" 语义需澄清：在 task-level 这等于控制 δ（因 P 恒定），需解释\n\n### §4.3 (MATH)\n- Power analysis 添加 — good\n- \"consistent with framework prediction\" 需降级为 \"inconclusive\"\n\n### §4.5 (Router Diagnostic)\n- \"validates\" → \"is consistent with\"\n- \"rules out step-level data scarcity\" 需与 appendix hedging 统一\n- Non-monotonicity 正文需 acknowledge（不仅 caption）\n\n### Contribution List (Introduction)\n- Contribution 2: \"capacity-dependent limitation\" 基于 confounded data，需加 caveat\n- Contribution 3: \"cross-context applicability\" → \"cross-context illustration\" 或 \"framework flexibility demonstration\"\n\n### Related Work\n- 补充 hallucination detection 段落（SelfCheckGPT 等）——\"hallucination → death\" 是核心机制但未连接到 hallucination literature\n- AgentBench/LATS 补充到 LLM Agent 段落\n- Safe RLHF 补充到 Safe RL 段落",
    "project": "simgate-modular-routing",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_0b622d6038b969b96148ee8a163a1a0c"
  }
}
```

</details>

---


### Tool result

_source line 793 · 2026-05-16T19:56:34.750223+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Assistant

_source line 794 · 2026-05-16T19:56:48.230981+00:00_

---

**Round 10 审稿完成。**

报告已投递给 Research Director。总评 **borderline (2.75/5)**。

核心发现：
- 5 个 Critical 问题（df 统计错误、novelty 不足、单环境证据、data scaling 方法缺陷、capacity scaling confound）
- 7 个 Warning（router "validates" 过强、environment-agnostic overclaim、related work 遗漏、cluster bootstrap、cross-model 弱、MATH overclaimed、survivorship bias）
- 两位 Reviewer 交叉后高度一致，无需第二轮

相比 Round 9（borderline 3.0/5），评分略降：论文在 framing/claim scoping 方面有改善（R9 action items 基本落实），但 R1 新发现的 df=27 统计错误 + 两位 Reviewer 对 novelty 和 contribution sizing 的共识性质疑削弱了整体评价。可接收路径明确：Findings track 需纯 framing 修复；Main conference 需第二环境 pilot replication。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 77

## Round 77

10 recorded events


### User

_source line 795 · 2026-05-17T02:36:46.644407+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Findings
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 796 · 2026-05-17T02:36:55.028453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-17T02:36:55.081058+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-17T02:36:58.874357+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-17T02:36:58.925304+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-17T02:37:10.184173+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 801 · 2026-05-17T02:37:10.234952+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-17T02:37:15.453474+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 803 · 2026-05-17T02:37:15.504619+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 804 · 2026-05-17T02:37:15.742540+00:00_

开始执行审稿流程。先获取项目概况并读取论文文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 78

## Round 78

56 recorded events


### User

_source line 805 · 2026-05-17T06:28:52.067825+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Findings
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-17T06:28:59.038370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-17T06:28:59.240579+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-17T06:29:03.552588+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-17T06:29:03.804179+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-17T06:29:10.954358+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-17T06:29:12.109316+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (96 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **math-extension-n800** (success): MATH Level 4-5 在 N=800 下 internal > code-interpreter 效应达到统计显著（p<0.05），确认无 catastrophic failure 环境中 deterministic modality 无优势 ← 基于 math-negative-contrast\n- **plan-008-v4-4b-e2e** (negative): 4B router (episode-level 59%) 在 end-to-end deployment 中能否超越 always-det baseline (-9.47 mean score)。若超过：larger capacity translates to marginal deployment gain at disproportionate cost。若未超过：进一步强化 analytical framework > learned routing at all tested scales。 ← 基于 plan-008-v4-4b\n- **plan-004-ablation-b-seed789** (negative): ablation-b seed 变体 (seed=789)。验证 ablation-b 的 generation-level routing 在不同 seed 下的稳定性。ga=8, upsample_minority=true, data/plan-004-implicit/。 ← 基于 plan-004-ablation-b\n\n## 趋势\n成功 40 / 负向 24 / 失败 14 / 共 96\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-13313: 无 GPU 信息\n\n## 告警\n- gpu0-v6-lifespan: 已被终止 — unknown\n- llama-cross-model-expanded: 已被终止 — unknown\n- math-200-fixed: 训练失败 — unknown\n- mvp-p1-gpu0: 已被终止 — unknown\n- mvp-p1-gpu1: 已被终止 — unknown\n- mvp-p1-gpu1-v2: 已被终止 — unknown\n- mvp-p1-gpu1-vllm: 已被终止 — unknown\n- mvp-p1-signal: 已被终止 — unknown\n- plan-001b-gpu0: 训练失败 — unknown\n- plan-001b-g
…[truncated 928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-17T06:29:12.160049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-17T06:29:12.213503+00:00_

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
18	\title{Death Avoidance as a Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\nolinenumbers
24	\maketitle
25	
26	\input{abstract}
27	\input{introduction}
28	\input{method}
29	\input{experiments}
30	\input{related_work}
31	\input{discussion}
32	\input{conclusion}
33	
34	\section*{Limitations}
35	
36	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct); generalization requires further validation. The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface additional signal. Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}; more sophisticated strategies (e.g., Reflexion~\citep{reflexion-2023} or Tree-of-Thought backtracking~\citep{tot-2023}) may reduce internal death rates and lower DAF. Episode-level labels may assign suboptimal routing to individual steps, particularly those preceding death events, and training on pure-strategy trajectories introduces distribution shift at deployment~\citep{dagger-2011}. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:discussion}, Appendix~\ref{app:cross-env}) provide supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct replication (7 task types, $N{=}70$; Appendix~\ref{app:cross-model}) confirms direction-consistent 
…[truncated 5740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-17T06:29:21.514966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-17T06:29:22.068870+00:00_

100	lifespan-l-then-s      & 0.976 \\
101	inclined-plane         & 0.969 \\
102	freeze                 & 0.971 \\
103	meas-melt-point        & 0.972 \\
104	id-life-stages-2       & 0.972 \\
105	find-animal            & 0.970 \\
106	grow-fruit             & 0.973 \\
107	chem-mix               & 0.969 \\
108	find-non-living        & 0.980 \\
109	\bottomrule
110	\end{tabular}
111	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
112	\label{tab:loo}
113	\end{table}
114	
115	\section{Router Training Details}
116	\label{app:router-details}
117	
118	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
119	
120	With gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split; this suggests overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\sim}54\%$ balanced accuracy). All reported results use gradient accumulation 8.
121	
122	Under step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\% to 58.1\%, but internal recall varies from 51.5\% to 81.8\%, reflecting threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \pm 2.2\%$ across 8 cross-split seeds (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
123	
124	\paragraph{Evaluation methods.} All results use \emph{generation-based evaluation}: the model generates a routing label as tex
…[truncated 19409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-17T06:29:22.070271+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-17T06:29:22.122157+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-17T06:29:27.263178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 819 · 2026-05-17T06:29:29.171890+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs"
  }
}
```

</details>

---


### Tool result

_source line 820 · 2026-05-17T06:29:29.222626+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-17T06:29:38.146865+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here are the key submission guidelines and author instructions for EMNLP 2026:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, p
…[truncated 2753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 10883
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-17T06:29:43.588754+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit template requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit template requirements"
  }
}
```

</details>

---


### Tool call

_source line 823 · 2026-05-17T06:29:43.890693+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 824 · 2026-05-17T06:29:43.891180+00:00_

1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet no systematic methodology exists for diagnosing \emph{what} drives the value of routing decisions. We introduce an episode-level counterfactual framework (Algorithm~1) with dual metrics---a penalty-independent label fraction and the penalty-dependent Death Avoidance Factor (DAF)---that decomposes routing signal into death-avoidance and non-death components. The framework requires only paired episode outcomes under two modalities with binary success/failure indicators. As a diagnostic case study, we apply this framework to ScienceWorld (11 of 30 task types, 245 episodes, Qwen2.5-7B-Instruct). The analysis reveals that \textbf{78.9\% of non-tie routing labels} (75 of 95) are driven by death asymmetry, with DAF $= 90.4\%$ at the environment's penalty ($P{=}100$). The per-task correlation $r{=}0.97$ is largely a mathematical consequence of death dominance (partial $r{=}0.02$, $p{=}0.91$; \S\ref{sec:death-decomp}). A router trained on these labels reaches only $59.0\%$ episode-level balanced accuracy at 4B parameters, failing to outperform always-deterministic at practical scales. We demonstrate framework flexibility across environments (MATH, $N{=}795$: confirmed null, $p = 0.81$, no routing signal without catastrophic failure) and models (Llama-3.1-8B-Instruct pilot: directional consistency confirmed). In this case study, routing value reduces to safety-first modality selection; the framework itself generalizes to any environment with controllable modality comparison and binary catastrophic outcomes.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 825 · 2026-05-17T06:29:44.093142+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 826 · 2026-05-17T06:29:44.194287+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}---a text-based science simulation with 30 task types---faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	The shared assumption is that routing signal stems from diverse sources---accuracy, latency, capability matching---and that a learned router can exploit this signal to improve over any fixed strategy.
10	But this assumption has never been systematically verified: \emph{what actually drives the value of routing decisions in interactive environments?}
11	
12	We propose a \emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Fa
…[truncated 5351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-17T06:29:52.433635+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit template requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's comprehensive information about ACL Rolling Review 2026 submission format, page limits, and template requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. For short papers, the page limits are more limited (the search results reference 4 pages for EMNLP but confirm consistent formatting across *ACL venu
…[truncated 1168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 8844
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-17T06:29:58.679450+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-17T06:29:59.132035+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically across the environment (\S\ref{sec:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment $\mathcal{E}$ with state space $\mathcal{S}$, observation space $\mathcal{O}$, and action space $\mathcal{A}$. An agent follows a policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ that maps observation histories to actions. At each step $t$, the agent receives observation $o_t$, selects action $a_t = \pi(o_1, \ldots, o_t)$, and the environment transitions to state $s_{t+1}$.
10	
11	We define a modality set $\mathcal{M} = \{{\tt int}, {\tt det}\}$ governing how the agent processes state transitions:
12	\begin{itemize}
13	    \item \textbf{Internal} ($m = {\tt int}$): The agent uses its own generation to predict intermediate observations. The LLM interleaves chain-of-thought reasoning with environment actions following the ReAct paradigm \cite{react-2023}, but prediction errors compound across steps.
14	    \item \textbf{Deterministic} ($m = {\tt det}$): The agent receives ground-truth observations from the environment simulator at each step---equivalent to access to a perfect dynamics model. Action selection remains with the LLM; only the state-transition prediction is replaced.
15	\end{itemize}
16	
17	\noindent We restrict $\mathcal{M}
…[truncated 11243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-17T06:29:59.182863+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-17T06:29:59.385505+00:00_

1	\section{Experiments}
2	
3	\subsection{Death Avoidance Decomposition}
4	\label{sec:death-decomp}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/fig1_daf_scatter.pdf}
9	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types.}
10	\label{fig:decomposition}
11	\end{figure}
12	
13	Across 245 episodes, $\Delta_{\text{full}} = +29.60$; excluding death episodes, $\Delta_{\text{nd}} = +2.84$, yielding DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$; at default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\% (75 of 95 non-tie labels). Of these 75, 54 (72.0\%) reduce to ties when the death penalty is removed entirely (both modalities score zero without death); death avoidance is not merely the dominant but often the sole discriminating signal between modalities. The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$). Per-task, death rate differential correlates with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}). However, when $P$ is constant across tasks, $\text{Corr}(P \cdot \delta + \Delta_{\text{nd}},\; \delta) \rightarrow 1$ as DAF $\rightarrow 1$; controlling for $\delta \cdot P$ across all 30 task variants (11 selected plus 19 prescreened-out types with near-zero signal), the residual is $r = 0.02$ ($p = 0.91$, $df = 27$). At $n{=}11$ selected types, partial correlation is undefined due to perfect collinearity between $\delta$ and $\delta \cdot P$ when $P$ is constant---this collinearity itself is the strongest evidence that $r = 0.97$ is structural. We retain it as an internal consistency check, not as independent evidence. The correlation drops below significance at $P \leq 25$ (Appendix~\ref{app:penalty}). Of 245 episodes, 86 are \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preferen
…[truncated 5856 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-17T06:29:59.436154+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-17T06:29:59.486974+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}.
5	Toolformer \cite{toolformer-2023} teaches LLMs to insert API calls via self-supervised loss filtering; ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens enabling frozen models to invoke massive tool libraries; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask; ReTool \cite{retool-2025} applies RL to discover when code execution is preferable to chain-of-thought.
6	These focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Recent concurrent work sharpens this question: \citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect in LLM tool use, \citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \citet{tool-use-tax-2026} quantify a ``tool-use tax'' where tools degrade performance, and \citet{to-call-or-not-2026} propose a necessity--utility--affordability framework.
8	Our counterfactual decomposition provides environment-grounded evidence: in ScienceWorld, $90.4\%$ of routing signal at $P{=}100$ traces to catastrophic-failure prevention.
9	
10	\paragraph{Adaptive Computation and Routing.}
11	CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing across heterogeneous models.
12	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
13	These optimize \emph{how} to route; we reveal \emph{why} routing helps---in interactive environments, the dominant signal is catastrophic-failure avo
…[truncated 2089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-17T06:30:04.388834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-17T06:30:04.741957+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Cross-environment evidence.}
5	On ALFWorld ($N{=}135$), the framework identifies a qualitatively different mechanism: information asymmetry (access to admissible actions, reversible navigation failures) rather than death avoidance (Appendix~\ref{app:cross-env}). Neither MATH nor ALFWorld provides quantitative DAF replication---true replication requires a second catastrophic-failure environment (e.g., NetHack~\citep{nethack-2020}, Crafter~\citep{crafter-2022}). These cross-domain contrasts demonstrate framework applicability, not universality of the death-dominance finding.
6	
7	\paragraph{Penalty sensitivity and correlation structure.}
8	The $r = 0.97$ correlation is specific to catastrophic death ($P{=}100$); defining failure as any non-positive score yields $r = -0.13$ ($p = 0.70$). As shown in \S\ref{sec:death-decomp}, this correlation is largely a mathematical consequence of death dominance (partial $r = 0.02$); larger models with lower death rates would reduce DAF. This prediction assumes models above a minimum capability threshold; preliminary evidence (Qwen2.5-0.5B, $N{=}15$) suggests very weak models may exhibit low death rates not from avoidance ability but from inability to execute action sequences that reach dangerous states.
9	
10	\paragraph{Implications for router design.}
11	Death avoidance dominance (78.9\% of non-tie labels, DAF $= 90.4\%$ at $P{=}100$) reframes modality routing as a \emph{safety} problem---closer to a conservative default policy than to cost-quality optimization~\citep{garcia2015comprehensive, cogrouter-2026}. The 86:9 label imbalance explains why always-deterministic is a strong baseline; 4B parameters for $+9$\,pp router improvement is consistent with the analytical framework being more efficient.
12	
13	\paragraph{Framework applicability.}
14	The framework applies most directly to environments with sparse terminal rewards and catastrophic failure modes. ScienceWorld 
…[truncated 356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-17T06:30:04.742520+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-17T06:30:04.793120+00:00_

1	\section{Conclusion}
2	
3	We presented a formal diagnostic framework---episode-level counterfactual analysis with dual metrics (penalty-independent label fraction and penalty-dependent DAF)---for decomposing routing signal in modular LLM agents. Applied as a case study to 245 ScienceWorld episodes (11 of 30 task types, Qwen2.5-7B-Instruct), the framework reveals that 78.9\% of non-tie routing labels (75 of 95) arise from death asymmetry; under ScienceWorld's penalty ($P{=}100$), DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$). The per-task correlation $r = 0.97$ serves as an internal consistency check (partial $r = 0.02$ after controlling for $\delta \cdot P$); the decomposition correctly identifies death as the dominant term.
4	
5	Cross-domain applications demonstrate framework flexibility: on MATH ($N{=}795$), the confirmed null ($p = 0.81$, 95\% CI $[-2.6, +3.6]$~pp) establishes that no routing signal exists without catastrophic failure; a Llama-3.1-8B-Instruct pilot (7 task types, 70 episodes) confirms directional consistency ($+34.3\%$ vs.\ $+26.6\%$). An exploratory router yields an informative negative: episode-level balanced accuracy remains at or below chance at practical scales, reaching $59.0\%$ only at 4B---consistent with the analytical framework being more efficient. Our case study findings are specific to environments with binary catastrophic outcomes; open directions include step-level counterfactual labeling, replication in NetHack~\citep{nethack-2020} or Crafter~\citep{crafter-2022}, and sufficiently capable stronger backbones---which our framework predicts will lower DAF.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-17T06:30:10.787142+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_local_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_local_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-17T06:30:10.837896+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-17T06:30:15.563632+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "literature_map.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "literature_map.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-17T06:30:16.468266+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/literature_map.yaml\", \"content\": \"# Literature Map — simgate-modular-routing\\n# Last updated: 2026-05-14\\n# Scan scope: 2025-2026 incremental scan + existing references from paper_framing.md\\n\\n# ============================================================\\n# CATEGORY: Direct Competitors (novelty threat)\\n# ============================================================\\ndirect_competitors: []\\n# None found. No 2025-2026 paper claims death/safety avoidance\\n# as the dominant routing signal in LLM agent systems.\\n\\n# ============================================================\\n# CATEGORY: ScienceWorld Agent Baselines (must-cite)\\n# ============================================================\\nscienceworld_baselines:\\n  - id: cogrouter-2026\\n    title: \\\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv:2602.12662, Feb 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      SOTA on ScienceWorld (82.3% with Qwen2.5-7B). Routes between cognitive\\n      depth levels (instinct to strategic planning) via CoPO, not between\\n      internal vs deterministic computation. Does not analyze WHAT drives\\n      routing signal. Cite as SOTA baseline and adaptive computation related work.\\n    our_differentiation: >\\n      CogRouter optimizes HOW MUCH to think; we analyze WHAT routing learns\\n      (death avoidance = 99%). Different routing dimensions (depth vs modality).\\n\\n  - id: itp-2026\\n    title: \\\"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv:2601.08955, Jan 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      Extends POIMDP with world model lookahead on ScienceWorld/ALFWorld/
…[truncated 1489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 842 · 2026-05-17T06:30:16.569104+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-17T06:30:16.770890+00:00_

- id: "R10-C1"
  summary: "df=27 statistical error in partial correlation — invalidates key supporting evidence"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "Consensus. Section 4.1 reports partial r=0.02, p=0.91, df=27. With n=11 task types and 1 control variable, df should be 8. If episode-level (N=245), df=242. df=27 impossible under any valid computation. Error undermines the 'r=0.97 is mathematical artifact' argument — the conclusion likely still holds (r=0.02 is tiny) but statistical reporting is wrong."
  action_items:
    - round: 10
      action: "Recompute partial correlation at task-level (df=8) and report correct p-value. If episode-level was intended, explain why controlling for per-task constant at episode-level is valid."
      assigned_to: paper_agent
      status: in_progress
  resolution: "Paper Agent added clarification: partial correlation computed on n=30 task variants (not 11 types), k=1 → df=n-k-2=27 is correct. Awaiting Reviewer verification."
  resolution_round: null

- id: "R10-C2"
  summary: "Core finding novelty insufficient — DAF near-tautological, 78.9% is the real empirical content"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 10
  last_seen_round: 10
  mentions:
    - round: 10
      reviewers: [1, 2]
      note: "Consensus. DAF=δP/(δP+Δ_nd) approaching 1 when P>>Δ_nd is mathematical necessity. The true empirical content is δ=0.2653 and Δ_nd=2.84 (i.e., hallucination-induced death is frequent AND non-death performance gap is negligible). Paper self-acknowledges 'mathematical consequence' but contribution framing still presents as surprising discovery. For EMNLP main conference, contribution sizing may be insufficient without second catastrophic-failure environment."
  action_items:
    - round: 10
      action: "Restructure contribution framing: lead with empirical findings (δ
…[truncated 24887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-17T06:31:37.600495+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 11 审稿任务 — Reviewer 1（方法严谨性 + 统计推断 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Findings (via ACL Rolling Review May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数**: 正文 ≤ 8 pages + unlimited references + appendix\n- **模板**: ACL 2025 style, `\\usepackage[review]{acl}`\n- **匿名**: Double-blind\n- **必须有 Limitations section**（不计入页数）\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex）\n\n### 你的审查重点\n\n1. **方法正确性**：\n   - DAF 公式推导、decomposition 是否数学正确\n   - Algorithm 1 labeling 逻辑是否无歧义\n   - SCI (Signal Concentration Index) Gini coefficient 计算是否合理\n\n2. **统计推断**：\n   - 所有 p-value、CI 报告是否有对应的检验方法说明\n   - Partial correlation (r=0.02, p=0.91, df=27) — 验证 df=27 的合理性（论文声称基于 n=30 task variants, k=1）\n   - Bootstrap CI [81.6%, 98.8%] 和 cluster bootstrap [73.3%, 100%] 是否正确报告\n   - MATH 结果 p=0.81, McNemar 检验是否合适\n   - Mann-Whitney 用于 reasoning depth ablation 是否合适\n\n3. **实验设计**：\n   - N=245 episodes (11/30 tasks) 的 prescreening 是否引入 selection bias\n   - Data scaling ablation (25%–800% augmentation) 的结论是否被 overclaim\n   - Capacity scaling (0.6B/1.7B/4B) non-monotonic U-shaped 结果的解释是否合理\n   - Cross-model (Llama N=70) 和 cross-env (MATH N=795, ALFWorld N=135) 的 evidence strength\n\n4. **前轮关键问题验证**（检查是否已修复）：\n   - **R10-C1**: df=27 — 论文现在声称 \"computed on n=30 task variants (11 selected + 19 prescreened-out), k=1 → df=n-k-2=27\"。验证这个解释是否统计学上合理（partial correlation on 30 data points, controlling for δ·P when P is constant=100 across all tasks）\n   - **R10-C4**: data scaling 语言 — 检查 main text 是否仍有 \"rules out\" 的 overclaim\n   - **R10-C5**: Capacity scaling confound — 论文声称已做 controlled 4-seed replication (0.6B=50.7%, 1.7B=43.1%, 4B=59.0%)，验证报告是否 consistent\n   - **R10-W4**: Cluster bootstrap — 是否正确实施和报告\n\n### 输出格式\n```\n## Summary（2-3句）\n## Strengths（逐条）\n## Weaknesses（逐条，按 severity 标注 [Critical/Warning/Minor]）\n## Questions（需要作者回答的）\n## Statistical Issues（如有）\n## Score: X/10\n## Confidence: X/5\n```",
  "reviewer_id": "1",
  "project": "simgate-modular-routing",
  "round_number": "11"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 11 审稿任务 — Reviewer 1（方法严谨性 + 统计推断 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Findings (via ACL Rolling Review May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数**: 正文 ≤ 8 pages + unlimited references + appendix\n- **模板**: ACL 2025 style, `\\usepackage[review]{acl}`\n- **匿名**: Double-blind\n- **必须有 Limitations section**（不计入页数）\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex）\n\n### 你的审查重点\n\n1. **方法正确性**：\n   - DAF 公式推导、decomposition 是否数学正确\n   - Algorithm 1 labeling 逻辑是否无歧义\n   - SCI (Signal Concentration Index) Gini coefficient 计算是否合理\n\n2. **统计推断**：\n   - 所有 p-value、CI 报告是否有对应的检验方法说明\n   - Partial correlation (r=0.02, p=0.91, df=27) — 验证 df=27 的合理性（论文声称基于 n=30 task variants, k=1）\n   - Bootstrap CI [81.6%, 98.8%] 和 cluster bootstrap [73.3%, 100%] 是否正确报告\n   - MATH 结果 p=0.81, McNemar 检验是否合适\n   - Mann-Whitney 用于 reasoning depth ablation 是否合适\n\n3. **实验设计**：\n   - N=245 episodes (11/30 tasks) 的 prescreening 是否引入 selection bias\n   - Data scaling ablation (25%–800% augmentation) 的结论是否被 overclaim\n   - Capacity scaling (0.6B/1.7B/4B) non-monotonic U-shaped 结果的解释是否合理\n   - Cross-model (Llama N=70) 和 cross-env (MATH N=795, ALFWorld N=135) 的 evidence strength\n\n4. **前轮关键问题验证**（检查是否已修复）：\n   - **R10-C1**: df=27 — 论文现在声称 \"computed on n=30 task variants (11 selected + 19 prescreened-out), k=1 → df=n-k-2=27\"。验证这个解释是否统计学上合理（partial correlation on 30 data points, controlling for δ·P when P is constant=100 across all tasks）\n   - **R10-C4**: data scaling 语言 — 检查 main text 是否仍有 \"rules out\" 的 overclaim\n   - **R10-C5**: Capacity scaling confound — 论文声称已做 controlled 4-seed replication (0.6B=50.7%, 1.7B=43.1%, 4B=59.0%)，验证报告是否 consistent\n   - **R10-W4**: Cluster bootstrap — 是否正确实施和报告\n\n### 输出格式\n```\n## Summary（2-3句）\n## Strengths（逐条）\n## Weaknesses（逐条，按 severity 标注 [Critical/Warning/Minor]）\n## Questions（需要作者回答的）\n## Statistical Issues（如有）\n## Score: X/10\n## Confidence: X/5\n```",
    "reviewer_id": "1",
    "project": "simgate-modular-routing",
    "round_number": "11"
  }
}
````

</details>

---


### Tool result

_source line 845 · 2026-05-17T06:32:00.424614+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22824
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-17T06:32:00.978946+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 11 审稿任务 — Reviewer 2（新颖性 + 贡献定位 + 写作质量 + Related Work）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Findings (via ACL Rolling Review May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数**: 正文 ≤ 8 pages + unlimited references + appendix\n- **模板**: ACL 2025 style, `\\usepackage[review]{acl}`\n- **匿名**: Double-blind\n- **必须有 Limitations section**（不计入页数）\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex）\n\n### 你的审查重点\n\n1. **新颖性与贡献定位**：\n   - 核心贡献（counterfactual framework + DAF metric + SCI）是否达到 EMNLP Findings 的 novelty bar\n   - DAF = δP/(δP+Δ_nd) 在数学上接近 tautology（当 P >> Δ_nd 时必然→1）—— 论文是否充分承认这一点？empirical content 是什么？\n   - 论文以 \"case study\" 自居是否恰当？单环境（ScienceWorld 11/30 tasks）是否足以支撑 framework 贡献？\n   - 对比 Findings track 的定位：negative/analytical result 在 EMNLP Findings 中是否有先例？\n\n2. **写作质量**：\n   - Abstract 是否在 150-250 words 内回答四个核心问题（问题/重要性/方法/结果）\n   - Introduction 叙事线是否清晰连贯（背景→问题→洞察→贡献）\n   - 是否有 AI 写作痕迹（em-dash、-ing phrases、过度分段、过渡词堆砌）\n   - 专有名词首次出现是否定义\n   - 全文主线是否统一（idea 是否前后一致）\n\n3. **Related Work 评估**：\n   - 覆盖是否充分：tool use routing、adaptive computation、counterfactual RL、safe RL、LLM agents\n   - 是否缺少重要引用（检查：AgentBench, LATS, SelfCheckGPT, NetHack, Crafter, Safe RLHF, ToolBench）\n   - 定位是否清晰：与 CogRouter、MTRouter、ReTool 的区分是否 convincing\n   - 引用密度是否达到 EMNLP 标准（通常 40-60 refs）\n\n4. **前轮关键问题验证**（检查是否已修复）：\n   - **R10-C2**: 贡献 framing — 是否以 78.9% 为主线而非 DAF=90.4%？DAF 是否定位为 summary tool 而非 headline discovery？\n   - **R10-C3**: Single-env — Contribution 3 的措辞是否已降级为 \"framework illustration\" 而非 \"validation\"？\n   - **R10-W1**: Router failure → \"validates\" 是否改为 \"is consistent with\"？\n   - **R10-W2**: \"Environment-agnostic\" → 是否改为 \"applicable to environments with binary catastrophic outcomes\"？\n   - **R10-W3**: Related work gaps — AgentBench, LATS, SelfCheckGPT, NetHack, Crafter 是否已引用？\n   - **R10-W5**: Cross-model 是否降级为 \"preliminary pilot\"？\n   - **R10-W6**: MATH \"consistent with framework prediction\" 是否改为更保守措辞？\n   - **R10-W7**: \"systematic across nearly all task types\" 是否加了 \"exhibiting routing signal\" 限定？\n   - **R10-m1**: 是否有 Discussion 段落讨论 oracle vs imperfect tools？\n   - **R10-m2**: 标题是否从 \"the Dominant\" 改为 \"a Dominant\"？\n\n### 输出格式\n```\n## Summary（2-3句）\n## Strengths（逐条）\n## Weaknesses（逐条，按 severity 标注 [Critical/Warning/Minor]）\n## Questions（需要作者回答的）\n## Missing References（如有）\n## Writing Issues（如有）\n## Score: X/10\n## Confidence: X/5\n```",
  "reviewer_id": "2",
  "project": "simgate-modular-routing",
  "round_number": "11"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 11 审稿任务 — Reviewer 2（新颖性 + 贡献定位 + 写作质量 + Related Work）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Findings (via ACL Rolling Review May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数**: 正文 ≤ 8 pages + unlimited references + appendix\n- **模板**: ACL 2025 style, `\\usepackage[review]{acl}`\n- **匿名**: Double-blind\n- **必须有 Limitations section**（不计入页数）\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex）\n\n### 你的审查重点\n\n1. **新颖性与贡献定位**：\n   - 核心贡献（counterfactual framework + DAF metric + SCI）是否达到 EMNLP Findings 的 novelty bar\n   - DAF = δP/(δP+Δ_nd) 在数学上接近 tautology（当 P >> Δ_nd 时必然→1）—— 论文是否充分承认这一点？empirical content 是什么？\n   - 论文以 \"case study\" 自居是否恰当？单环境（ScienceWorld 11/30 tasks）是否足以支撑 framework 贡献？\n   - 对比 Findings track 的定位：negative/analytical result 在 EMNLP Findings 中是否有先例？\n\n2. **写作质量**：\n   - Abstract 是否在 150-250 words 内回答四个核心问题（问题/重要性/方法/结果）\n   - Introduction 叙事线是否清晰连贯（背景→问题→洞察→贡献）\n   - 是否有 AI 写作痕迹（em-dash、-ing phrases、过度分段、过渡词堆砌）\n   - 专有名词首次出现是否定义\n   - 全文主线是否统一（idea 是否前后一致）\n\n3. **Related Work 评估**：\n   - 覆盖是否充分：tool use routing、adaptive computation、counterfactual RL、safe RL、LLM agents\n   - 是否缺少重要引用（检查：AgentBench, LATS, SelfCheckGPT, NetHack, Crafter, Safe RLHF, ToolBench）\n   - 定位是否清晰：与 CogRouter、MTRouter、ReTool 的区分是否 convincing\n   - 引用密度是否达到 EMNLP 标准（通常 40-60 refs）\n\n4. **前轮关键问题验证**（检查是否已修复）：\n   - **R10-C2**: 贡献 framing — 是否以 78.9% 为主线而非 DAF=90.4%？DAF 是否定位为 summary tool 而非 headline discovery？\n   - **R10-C3**: Single-env — Contribution 3 的措辞是否已降级为 \"framework illustration\" 而非 \"validation\"？\n   - **R10-W1**: Router failure → \"validates\" 是否改为 \"is consistent with\"？\n   - **R10-W2**: \"Environment-agnostic\" → 是否改为 \"applicable to environments with binary catastrophic outcomes\"？\n   - **R10-W3**: Related work gaps — AgentBench, LATS, SelfCheckGPT, NetHack, Crafter 是否已引用？\n   - **R10-W5**: Cross-model 是否降级为 \"preliminary pilot\"？\n   - **R10-W6**: MATH \"consistent with framework prediction\" 是否改为更保守措辞？\n   - **R10-W7**: \"systematic across nearly all task types\" 是否加了 \"exhibiting routing signal\" 限定？\n   - **R10-m1**: 是否有 Discussion 段落讨论 oracle vs imperfect tools？\n   - **R10-m2**: 标题是否从 \"the Dominant\" 改为 \"a Dominant\"？\n\n### 输出格式\n```\n## Summary（2-3句）\n## Strengths（逐条）\n## Weaknesses（逐条，按 severity 标注 [Critical/Warning/Minor]）\n## Questions（需要作者回答的）\n## Missing References（如有）\n## Writing Issues（如有）\n## Score: X/10\n## Confidence: X/5\n```",
    "reviewer_id": "2",
    "project": "simgate-modular-routing",
    "round_number": "11"
  }
}
````

</details>

---


### Tool call

_source line 847 · 2026-05-17T06:32:01.233812+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 848 · 2026-05-17T06:32:02.562587+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1583
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-17T06:32:02.563089+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1329
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-17T06:32:08.765054+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-17T06:32:08.816035+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 103\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-determinis
…[truncated 1447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-17T06:32:17.759592+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -name \"config*\" -o -name \"project.yaml\" -o -name \"project.yml\" 2>/dev/null | head -10",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -name \"config*\" -o -name \"project.yaml\" -o -name \"project.yml\" 2>/dev/null | head -10",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-17T06:32:17.911054+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-17T06:32:24.544206+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 2 -name \"*.yaml\" -path \"*config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 1 -name \"config*\" 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/*.yaml 2>/dev/null | head -5",
  "description": "Search for project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 2 -name \"*.yaml\" -path \"*config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -maxdepth 1 -name \"config*\" 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/*.yaml 2>/dev/null | head -5",
    "description": "Search for project config files"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-17T06:32:24.695359+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/pending_approval_notifications.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-17T06:32:28.966242+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -maxdepth 2 -name \"*.yaml\" 2>/dev/null | grep -v artifacts | grep -v node_modules | head -20",
  "description": "Find yaml files in project dir"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -maxdepth 2 -name \"*.yaml\" 2>/dev/null | grep -v artifacts | grep -v node_modules | head -20",
    "description": "Find yaml files in project dir"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-17T06:32:29.017039+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-17T06:32:35.952229+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/workspace.yaml 2>/dev/null",
  "description": "Search for external review config setting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/ 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/workspace.yaml 2>/dev/null",
    "description": "Search for external review config setting"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-17T06:32:36.002942+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 860 · 2026-05-17T06:32:44.961102+00:00_

外部审稿未配置（`external_review.paperreview_ai.enabled` 未在项目配置中找到），跳过外部审稿线。

**当前状态**：
- Reviewer 1（方法/统计/实验）已触发 ✓
- Reviewer 2（新颖性/写作/Related Work）已触发 ✓
- 外部审稿：N/A

等待两位 Reviewer 返回 Round 11 初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 79

## Round 79

2 recorded events


### User

_source line 861 · 2026-05-17T06:38:10.377350+00:00_

[Reviewer 2 审稿意见]:
## Round 11 Review — Reviewer 2（新颖性 + 贡献定位 + 写作质量 + Related Work）

---

## Summary（2-3句）

论文提出了一个 episode-level counterfactual 框架用于诊断 modular LLM agent 中 routing 决策的信号来源，在 ScienceWorld 上发现 78.9% 的 routing label 由 death asymmetry 驱动。前轮（R10）提出的绝大多数问题已得到有效修复，论文的 claim calibration 显著改善。当前版本的主要遗留问题是：em-dash 泛滥（AI 写作痕迹）、`\nolinenumbers` 格式违规、引用数量偏低（37 篇 vs EMNLP 典型 40-60 篇）、以及 DAF metric 的 empirical content 仍需更清晰地在 Abstract 层面传达。

---

## Strengths

**S1. R10 问题修复质量高。** 几乎所有前轮关键问题均已妥善处理：
- [R10-C2] ✅ 78.9% 作为主线 headline，DAF 定位为 secondary summary tool
- [R10-C3] ✅ Contribution 3 改为 "Framework flexibility illustration"，明确声明 "not universality"
- [R10-W1] ✅ Router failure 使用 "consistent with" 而非 "validates"
- [R10-W2] ✅ 无 "environment-agnostic"，改为 "applicable to environments with binary catastrophic outcomes"
- [R10-W3] ✅ AgentBench、LATS、SelfCheckGPT、NetHack、Crafter 均已引用
- [R10-W5] ✅ Cross-model 明确标注 "preliminary pilot"
- [R10-W6] ✅ MATH 用 "confirmed null" + p 值 + CI
- [R10-W7] ✅ "systematic across all task types exhibiting routing signal" 加了限定
- [R10-m1] ✅ Discussion 最后一段讨论了 oracle vs imperfect tools
- [R10-m2] ✅ 标题 "a Dominant" 而非 "the Dominant"

**S2. Claim calibration 全文一致。** 从 Abstract 到 Conclusion，用词谨慎、自洽。例如：cross-model 始终称 "preliminary pilot"；MATH 始终称 "confirmed null"；Contribution 3 明确说 "demonstrate diagnostic applicability, not universality"。这是多轮修改后的显著提升。

**S3. 方法论透明度高。** DAF 的数学性质（随 P 单调递增）在 §3.4 被显式承认为 "mathematical consequence, not an empirical finding"，同时报告 penalty-independent 的 78.9% label fraction 作为 companion metric。Partial correlation r=0.02 的讨论（§4.1）诚实地揭示了 r=0.97 的 structural nature。这种自我批判的透明度在顶会投稿中不常见，值得肯定。

**S4. 统计严谨性。** Bootstrap CI（B=10,000）、cluster bootstrap（K=11）、McNemar test（MATH）、多种 robustness check（LOO、penalty sensitivity、seed robustness）——统计实践达到 EMNLP 标准。

**S5. Negative result 有价值。** Router training diagnostic 作为 "informative negative" 的定位恰当——不是声称 routing 不可能，而是证明在当前数据/模型规模下 analytical framework 比 brute-force learned routing 更高效。这对社区有实际指导意义。

---

## Weaknesses

**W1 [Warning] LaTeX em-dash (`---`) 泛滥——AI 写作最显著标志**

全文正文（不含 appendix）至少有 20+ 处 `---` 渲染为 em-dash。按 CLAUDE.md paper-writing-norms §5.1（"严禁破折号"），这是最高优先级硬规则。具体高频位置：

- Abstract: "dual metrics---a penalty-independent label fraction and..."
- Introduction line 4: "ScienceWorld \cite{...}---a text-based science simulation..."
- Introduction line 9: "sources---accuracy, latency, capability matching---and that..."（双 em-dash）
- Introduction line 17: "labels---per-step oracle comparison---degenerates..."（双 em-dash）
- Introduction line 23: "death asymmetry---a penalty-independent measure"
- Introduction line 31: "held-out episodes---below the always-deterministic baseline---"（双 em-dash）
- Method line 14: "each step---equivalent to access..."
- Experiments line 54: "always-deterministic---\emph{oracle degeneracy}..."
- Discussion line 11: "problem---closer to a conservative..."
- Conclusion lines 3, 5: 多处

**建议**：全局 `grep "---" *.tex`，逐条替换为逗号、括号或拆句。数字范围（如 "20--40"）和 Mann--Whitney 等专有名词中的 `--` (en-dash) 可保留。这是投稿前必须清零的格式问题。

**W2 [Warning] `\nolinenumbers` 禁用行号——ACL ARR review 格式违规**

main.tex line 23: `\nolinenumbers`。ACL ARR review submission 要求 `\usepackage[review]{acl}` 启用行号，方便 reviewer 引用具体位置。`\nolinenumbers` 显式覆盖了这一设置。这是 desk reject 风险项。

**建议**：删除 `\nolinenumbers`。

**W3 [Warning] 引用数量偏低（37 篇 vs EMNLP 典型 40-60 篇）**

references.bib 共 37 条 entry。EMNLP main/Findings 论文通常引用 40-60 篇。当前缺失：
- **ToolBench** (Qin et al., 2024)——tool use benchmark 领域重要工作，Related Work §Tool Use 段应引用
- **Safe RLHF** (Dai et al., 2024)——Safe RL 段只引了 Garcia 2015 survey 和 CRPO 2021，缺少 LLM-era safe alignment 工作
- **ToolAlpaca / API-Bank / Gorilla** 等 tool-use 数据集/benchmark 论文——若空间允许
- **WebArena / MiniWoB++** 等 interactive environment——strengthen the "interactive environments" paragraph

引用覆盖本身不影响 soundness，但审稿人会据此判断调研深度。建议补 3-5 篇至 40+ 的安全线。

**W4 [Minor] DAF 的 empirical content 在 Abstract 中仍不够直观**

Abstract 同时报告 78.9% 和 DAF=90.4%，但对 uninitiated reader 而言，两个数字的关系和区别不清晰。78.9% 是 penalty-independent（计数比例），DAF=90.4% 是 penalty-dependent（分数贡献比例）。Abstract 没有用一句话解释这一区分。

当前 Abstract 措辞："78.9\% of non-tie routing labels (75 of 95) are driven by death asymmetry, with DAF $= 90.4\%$ at the environment's penalty ($P{=}100$)"——"with" 暗示两者是 additive 信息，但实际上 78.9% 已经是更 robust 的 metric（不依赖 P），DAF 是 P-dependent 的 amplification view。

**建议**：在 Abstract 中加一个半句明确区分，如 "78.9% of non-tie routing labels are driven by death asymmetry (penalty-independent); this translates to DAF = 90.4% under ScienceWorld's penalty (P=100, penalty-dependent)."

**W5 [Minor] Experiments 段落过长过密**

§4.1 Death Avoidance Decomposition 的第一段（experiments.tex line 13）是一个超长段落，包含：DAF 数值、label fraction、death rates、per-task correlation、partial correlation、collinearity 论证、30 task variants 分析。信息密度过高，读者需要多次回读。

§4.6 Router Training 段（experiments.tex line 57-61）同样是单段落承载过多信息：step-level accuracy、episode-level accuracy、capacity scaling、U-shaped curve、augmentation、4B result、deployment score。

**建议**：适当拆分为 2-3 个小段落或添加 `\paragraph{}` 标记，便于审稿人定位。

**W6 [Minor] Abstract 词数约 201——接近上限但在范围内**

Abstract 约 201 words，在 150-250 的范围内，但信息密度极高，包含了 5+ 个数字。对于不熟悉该领域的审稿人，30 秒内可能无法消化所有关键点。Abstract 中的 "Algorithm~1" 引用在 Abstract 内无法跳转，略显突兀。

---

## Questions（需要作者回答）

**Q1.** DAF 在 P=10 时仅为 50.4%。如果选择一个 penalty 更温和的环境（如 P=10-25），death avoidance 的 "dominance" narrative 是否还成立？论文如何定义 "dominant"——是 DAF > 50%、> 80%、还是 label fraction > 50%？

**Q2.** 11/30 task types 被选入分析，19 被排除。排除的 19 types 中，是否有任何一个在延长 step budget（如 T_max=50 或 100）后会产生 routing signal？这直接影响 "death avoidance dominates routing signal in ScienceWorld" 的 claim scope。

**Q3.** Contribution 1 声称框架 "applies to any environment with controllable modality comparison and binary catastrophic outcomes"。但实际验证只有 ScienceWorld（有 death）和 MATH（confirmed null）。ALFWorld 被用来展示框架的 diagnostic applicability，但 ALFWorld 没有 catastrophic outcomes。这是否意味着框架的 "binary catastrophic outcomes" 前提条件其实只在 ScienceWorld 上被验证过？

---

## Missing References

1. **ToolBench** (Qin et al., 2024) — tool-use benchmark，§Related Work Tool Use 段应引用
2. **Safe RLHF** (Dai et al., 2024) — LLM-era safe alignment，§Safe RL 段应引用
3. 建议补充至少 3-5 篇至 ≥40 篇总量

---

## Writing Issues

1. **[Must-Fix] Em-dash (`---`) 全文 20+ 处**：Abstract、Introduction、Method、Experiments、Discussion、Conclusion 均有。需全部替换为逗号/括号/拆句。（详见 W1）
2. **[Must-Fix] `\nolinenumbers`**：删除此命令以启用 review 模式行号。（详见 W2）
3. **[Minor] `-ing` 分词短语**：数量不多（约 5-6 处），如 "indicating", "reflecting", "confirming"——均在句中而非句尾，尚可接受。
4. **[Minor] 过渡词**：未发现 "Furthermore/Moreover/Additionally" 堆砌。写作节奏较好。
5. **[Minor] 专有名词定义**：DAF、SCI 在首次出现时均有完整定义；ReAct 有引用。Abstract 中 "DAF" 在括号中定义。✓

---

## 前轮问题修复状态汇总

| R10 Issue | Status | 备注 |
|-----------|--------|------|
| R10-C2: 78.9% 为主线 | ✅ Fixed | Abstract/Intro/Contributions 均以 78.9% 领衔 |
| R10-C3: Contrib 3 降级 | ✅ Fixed | "Framework flexibility illustration"，明确否认 universality |
| R10-W1: "validates" → cautious | ✅ Fixed | 改为 "consistent with" |
| R10-W2: "Environment-agnostic" | ✅ Fixed | 全文无此词 |
| R10-W3: 缺失引用 | ✅ Mostly Fixed | AgentBench/LATS/SelfCheckGPT/NetHack/Crafter 已加；ToolBench/Safe RLHF 仍缺 |
| R10-W5: Cross-model 降级 | ✅ Fixed | "preliminary pilot" |
| R10-W6: MATH 保守措辞 | ✅ Fixed | "confirmed null" |
| R10-W7: "systematic" 加限定 | ✅ Fixed | "exhibiting routing signal" qualifier |
| R10-m1: Oracle vs imperfect | ✅ Fixed | Discussion 最后一段 |
| R10-m2: 标题 "a Dominant" | ✅ Fixed | |

---

## ACL ARR 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论严谨，统计实践规范，decomposition 有效。扣分：单环境 (11/30 tasks)，DAF 的 penalty-dependence 使 headline number 缺乏环境间可比性 |
| Excitement | 2.5/5 | Analytical/negative result 有价值但 scope 窄。核心洞察（deterministic safer than LLM reasoning）不令人意外；framework 本身较 lightweight |
| Reproducibility | 4/5 | 算法伪代码清晰，超参数完整，统计细节充分。承诺 code release。扣分：ScienceWorld 环境版本未标注 |

## Score: 5.5/10

Findings 边缘。Soundness 达标，claim calibration 优秀，统计实践严谨。主要拖累是：(1) excitement 偏低——核心 insight 虽 useful 但 scope 窄且不 surprising；(2) em-dash 泛滥和 `\nolinenumbers` 需要在提交前修复；(3) 引用略低于 EMNLP 标准线。修复 W1-W3 后，作为 Findings paper 是 borderline accept。

## Confidence: 4/5

对 tool-use routing、counterfactual analysis、interactive environments 文献较熟悉。对 safe RL 子领域的最新进展了解相对有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 862 · 2026-05-17T06:38:18.113635+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 80

## Round 80

2 recorded events


### User

_source line 863 · 2026-05-17T06:38:20.682736+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**5.5/10，Findings 边缘 borderline accept**。R10 的 10 项问题中 9 项完全修复、1 项（W3 缺失引用）大部分修复（ToolBench/Safe RLHF 仍缺）。当前版本主要问题是：em-dash 泛滥（20+ 处，AI 写作最显著标志）、`\nolinenumbers` 格式违规（desk reject 风险）、引用 37 篇略低于 EMNLP 标准线。这些均为投稿前必须修复的 mechanical issues，不涉及实质性内容改动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 864 · 2026-05-17T06:38:28.431336+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 81

## Round 81

6 recorded events


### User

_source line 865 · 2026-05-17T06:39:56.512432+00:00_

[Reviewer 1 审稿意见]:
## Round 11 审稿报告 — Reviewer 1（方法严谨性 + 统计推断 + 实验设计）

---

## Summary（2-3句）

本文提出了一个 episode-level counterfactual 诊断框架，用于分解模块化 LLM agent 的 routing signal 来源。以 ScienceWorld 为 case study（11/30 task types, N=245），发现 78.9% 的 non-tie routing labels 来自 death asymmetry，DAF=90.4%。框架设计合理、分析详尽，但核心统计推断（partial correlation）存在数学上的根本性错误，需要修复。

---

## Strengths

**S1. 框架设计精巧**：DAF 分解将 routing signal 拆分为 death-avoidance 和 non-death 两个正交分量，且同时提供了 penalty-independent（78.9% label fraction）和 penalty-dependent（DAF）两个互补指标。这种双指标设计让结论不依赖单一 penalty 设定，方法论上值得肯定。

**S2. 分析诚实度高**：论文在多个地方主动暴露自己的弱点——router 训练失败（47.1±2.2% < 50% baseline），capacity scaling 的 non-monotonic 结果，data scaling 的 augmentation confound，Llama pilot 的小样本量——这种诚实度在投稿论文中不常见。Section 4.5 和 Appendix D 对 router failure 的多层剖析尤其有价值。

**S3. 跨域对比设计合理**：MATH（N=795, confirmed null, p=0.81）作为 negative contrast 有效展示了"无 death penalty → 无 routing signal"的逻辑链；ALFWorld 识别出 information asymmetry 机制，展示框架的 diagnostic 灵活性。三个环境形成完整的证据三角：death-driven (ScienceWorld) → info-driven (ALFWorld) → null (MATH)。

**S4. Algorithm 1 逻辑无歧义**：labeling function 的四个 mutually exclusive cases 覆盖了所有可能组合（death asymmetry / both dead / score comparison / tied alive），优先级清晰（survival > score）。Appendix A 的 labeling quality audit（zero tie-breaking artifacts, death-only retrain yields within-1σ）进一步验证了 label 质量。

**S5. SCI 指标有效补充**：Gini-based SCI=0.2147 回答了"death avoidance 是 systematic 还是 outlier-driven"的问题，top-3 task types 仅贡献 39.8%，与 `find-non-living-thing`（zero deaths, Δ=+9.58 from non-death scores）作为 internal counterexample 形成完整论证。

---

## Weaknesses

**W1 [Critical] Partial correlation (r=0.02, p=0.91, df=27) 存在根本性数学错误**

- **具体位置**：Section 4.1, line "controlling for δ·P across all 30 task variants..."
- **问题**：当 P 为常数（=100, ScienceWorld 所有 task type 共享同一 death penalty）时，δ·P = 100δ 是 δ 的完美线性变换。Partial correlation 的计算需要回归掉控制变量的影响：regress δ on (δ·P) 得到 R²=1、residuals=0，导致分母为零，partial correlation 数学上 undefined。

  具体推导：partial_corr(Δ_full, δ | δ·P) = (r_{Δδ} - r_{Δ,δP} · r_{δ,δP}) / (√(1 - r²_{Δ,δP}) · √(1 - r²_{δ,δP}))。由于 δ·P = 100δ，r_{δ,δP} = 1.0，分母 √(1 - 1.0) = 0。无论 n=11 还是 n=30，只要 P 是常数，collinearity 就是 structural 的，不是 sample-size 问题。

  论文自身在 §4.1 已承认："At n=11 selected types, partial correlation is undefined due to perfect collinearity"——但随后声称扩展到 n=30 解决了问题。这是错误的：19 个 excluded task types 同样使用 P=100，δ·P 仍然与 δ 完全共线。软件可能因 floating-point tolerance 返回了 r=0.02 而非 NaN，但这是数值 artifact，不是有意义的统计量。

- **为什么影响接收**：这是论文四次重复引用的统计量（Abstract, Introduction, §4.1, Conclusion），被用作"r=0.97 is structural"的关键证据。虽然概念论证（P 常数 → δ·P 与 δ 共线 → 高 r 是 tautological）是正确的，但报告无效的 p-value 和 df 损害了全文的统计可信度。

- **建议修改方向**：
  (a) 删除所有 partial correlation 的具体数值（r=0.02, p=0.91, df=27），改为纯粹的代数论证："When P is constant across tasks, δ·P is perfectly collinear with δ, making partial correlation undefined. This collinearity itself proves that r=0.97 is a structural consequence of death dominance rather than an independent empirical finding."
  (b) 或者改用 corr(Δ_nd, δ)——即 non-death score gap 与 death rate differential 的 Pearson correlation——作为替代统计量。这个量是 well-defined 的（df=n-2=28 for n=30），且如果 r≈0 则同样说明 death 是唯一驱动力。

**W2 [Warning] Capacity scaling 报告不一致**

- **具体位置**：Section 4.5 vs. Appendix F (Table 8)
- **问题**：Main text 报告 controlled replication（identical 4-seed config for all scales）：0.6B: 50.7%, 1.7B: 43.1±1.0%, 4B: 59.0%。仅 1.7B 有 error bars。Appendix Table 8 报告不同的 1.7B 数值（47.10±2.20, 8 seeds, different training config）且 0.6B (50.67±2.62) 和 4B (58.96±1.94) 有 std。

  读者面临两套 1.7B 数字：main text 的 43.1±1.0%（4 seeds, controlled replication）和 appendix 的 47.1±2.2%（8 seeds, original config）。虽然 caption 解释了差异，但这种 dual-reporting 容易造成混淆。此外，main text 中 0.6B 和 4B 缺少 error bars，而 appendix 中有，reporting 不对称。

- **建议**：在 Table 8 中增加一行 "Controlled replication (4-seed)" 并标注与原始 config 的差异；main text 引用时统一使用 mean±std。

**W3 [Warning] Cluster bootstrap (K=11) 覆盖率问题**

- **具体位置**：Section 4.1, "cluster bootstrap resampling (K=11 task-type clusters, B=10,000) yields a wider 95% CI [73.3%, 100%]"
- **问题**：K=11 clusters 远低于 cluster bootstrap 所需的最低集群数（Cameron, Gelbach & Miller, 2008 建议 K≥40）。Small-K cluster bootstrap 的 coverage 性质未知，可能严重 under-cover 或 over-cover。论文虽提到"reflecting limited cluster count"，但没有引用 small-cluster-count 文献或讨论 coverage 可靠性。

  更根本地：CI 上界为 100% 说明 bootstrap distribution 被右截断，这在 K=11 时是 expected artifact——几乎一半的 bootstrap resamples 可能缺失 `find-non-living-thing`（唯一的 DAF=0 task type），导致 DAF 被高估。

- **建议**：(a) 引用 Cameron et al. (2008) 或 MacKinnon & Webb (2017) 关于 small-K bootstrap 的 caveat；(b) 补充 wild cluster bootstrap 或 t-distribution correction (BRL, Bell-McCaffrey) 作为 sensitivity check；(c) 至少声明 K=11 的 cluster bootstrap CI 应谨慎解读。

**W4 [Warning] McNemar test (MATH) 与 routing labels 的对应关系不清**

- **具体位置**：Section 4.3
- **问题**：论文报告 107 int-preferred vs. 95 det-preferred labels（N=795），但 McNemar p=0.81。McNemar test 基于 paired binary discordant cells。如果 routing labels 是基于 exact score comparison（MATH 可能有 partial credit），而 McNemar 基于 binary correct/incorrect，则 discordant cell counts 与 routing label counts 不同——这解释了 p=0.81（较少 binary-discordant pairs），但论文没有明确区分。

  粗略验证：如果 McNemar discordant cells = routing labels（107, 95），则 χ²=(12)²/202=0.71, p≈0.40，不是 0.81。两者不一致说明 McNemar 使用的是不同的数据分割。

- **建议**：明确说明 McNemar test 的 input（binary accuracy discordant pairs vs. score-based routing labels），报告 exact discordant cell counts (b, c)。

**W5 [Warning] Prescreening 条件与 generalization scope 的张力**

- **具体位置**：Section 3.2, Appendix B
- **问题**：Prescreening 保留"both strategies complete at least one episode"的 task types，排除 19/30 (63%)。论文核心发现（78.9% labels from death, DAF=90.4%）仅适用于 11 个 selected tasks。Limitations 中承认"increasing step budget could surface additional signal"，但 Abstract 和 Conclusion 的 framing 偏向暗示这是 ScienceWorld 的 general finding 而非 11-task subset finding。

  Appendix B 提供了合理辩护（deterministic death rate comparable between included 17.8% and excluded 14.9%; prescreening selects for routing signal, not death-proneness），但仍然是 conditioning on the dependent variable。`find-non-living-thing` 作为 counterexample 削弱了 selection bias 担忧，但样本覆盖仍不足。

- **建议**：在 Abstract 和 Conclusion 中更明确地 qualify：这些结果来自 11/30 tasks（而非看起来像 ScienceWorld-wide finding）。当前 Abstract 已有"(11 of 30 task types)"，Conclusion 也有，但首次出现的位置偏后。

**W6 [Minor] 格式问题：\nolinenumbers 违反 review submission 要求**

- **具体位置**：main.tex line 24
- **问题**：`\usepackage[review]{acl}` 启用行号，但 `\nolinenumbers` 在 `\maketitle` 后立刻禁用。ACL ARR review submission 要求行号。
- **建议**：删除 `\nolinenumbers`。

**W7 [Minor] Mann-Whitney vs. paired test for reasoning depth ablation**

- **具体位置**：Section 3.1, Appendix F
- **问题**：Reasoning depth ablation 使用 Mann-Whitney U test 比较 chain-of-thought vs. direct-answer，但未说明是否使用 paired task instances。如果是 paired（相同 task instance 两种 condition），应使用 Wilcoxon signed-rank test；如果是 independent episodes，Mann-Whitney 合适但统计效力较低。
- **建议**：明确是 paired 还是 independent 设计。

---

## Questions

**Q1**：Partial correlation 的具体计算代码能否公开？具体而言，当 n=30, 所有 task types 共享 P=100 时，`scipy.stats` 或 `pingouin` 等库计算 partial_corr(Δ_full, δ | δ·P) 是否返回 NaN/warning？如果返回了 r=0.02，是否因为 floating-point 误差导致 r_{δ,δP} ≈ 0.9999999 而非 exactly 1.0？

**Q2**：MATH 的 McNemar test 中，exact discordant cell counts (b, c) 是多少？是基于 binary correct/incorrect 还是 score comparison？如果是 binary，请确认 b+c 的值——按 routing labels (107+95=202) 计算得到 p≈0.40，与报告的 p=0.81 不一致。

**Q3**：Capacity scaling controlled replication 中，0.6B 和 4B 是否也是 4-seed mean？如果是，为什么 main text 不报告 std？

**Q4**：`find-non-living-thing` 的 n=40（两批数据合并）是否引入了 batch effect？两批数据是同一配置还是不同配置？

**Q5**：SCI 计算中，当 δ_k=0（如 find-non-living-thing）时 c_k=0，该 task type 实际上不参与 death signal 分布。如果只在 K=10（有 death signal 的 task types）上计算 SCI，值是多少？

---

## Statistical Issues

1. **[Critical] Partial correlation undefined due to perfect collinearity**（详见 W1）
2. **[Warning] McNemar p-value 与 discordant counts 不一致**（详见 W4）
3. **[Warning] Cluster bootstrap with K=11 has unknown coverage properties**（详见 W3）
4. **[Minor] Mann-Whitney vs Wilcoxon signed-rank**（详见 W7）

---

## 前轮问题验证

**R10-C1 (df=27)**：❌ 未修复。论文将 n 从 11 扩展到 30（加入 19 个 excluded tasks），使 df=n-k-2=27 在形式上正确。但根本问题未解决：P=100 为常数 → δ·P 与 δ 完全共线 → partial correlation undefined。这是 structural collinearity，不随 n 变化。论文自身承认了 n=11 时的 collinearity，但错误地认为 n=30 解决了它。

**R10-C4 (data scaling "rules out" overclaim)**：✅ 已修复。Main text 现在使用"provides no improvement"而非"rules out"，并明确区分 augmentation-based scaling 和 real-data scaling。Appendix D 的 caveat ("episode-level minority-class diversity remains a potential confound") 是诚实的。

**R10-C5 (Capacity scaling confound)**：✅ 部分修复。新增了 controlled 4-seed replication with identical configs across all scales (0.6B: 50.7%, 1.7B: 43.1±1.0%, 4B: 59.0%)，确认 U-shaped pattern 是 robust 的。但报告不一致问题仍在（见 W2）。

**R10-W4 (Cluster bootstrap)**：⚠️ 部分修复。现在正确报告了 cluster bootstrap CI [73.3%, 100%] 并提到"reflecting limited cluster count"，但缺少 formal citation on small-K bootstrap limitations（见 W3）。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 框架设计和 DAF decomposition 数学正确；Algorithm 1 无歧义；但 partial correlation 存在根本性数学错误（perfect collinearity when P constant），McNemar discordant counts 与 p-value 不一致 |
| Excitement | 3.5/5 | 框架视角新颖（decompose routing signal rather than optimize routing），case study 发现有意义（death dominance explains why routing fails），但 scope 有限（1 env, 1 model family, negative router result） |
| Reproducibility | 4.0/5 | 环境公开、模型公开、hyperparameters 详尽（Table 5）、bootstrap parameters 完整。承诺 code release upon acceptance。但 partial correlation 计算不可复现（数学上 undefined）。 |
| Clarity | 4.0/5 | 写作清晰、结构合理、caveat 充分。Dual-1.7B reporting 稍有混淆。 |

---

## Score: 6/10

框架本身（Algorithm 1 + DAF + SCI）是 sound 的核心贡献。Partial correlation 是一个 specific 且 fixable 的统计错误，不动摇主要结论（78.9% label fraction 和 DAF=90.4% 基于更简单的描述性统计）。但作为被 4 次引用的 key statistic，必须修复。跨域分析和诚实的 negative result 提升了 paper 的可信度。

## Confidence: 4/5

方法论/统计审查是本轮重点，我对 collinearity 问题和 bootstrap 有效性的判断有高置信度。对 ScienceWorld 环境本身的 domain knowledge 有限，不影响统计判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-17T06:40:29.531188+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请对每条 Weakness 和 Statistical Issue 逐条回应：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Weaknesses:\n\n**W1 [Critical] Partial correlation (r=0.02, p=0.91, df=27) 存在根本性数学错误**\n\n当 P=100 为常数时，δ·P = 100δ 与 δ 完全共线（r_{δ,δP} = 1.0），partial correlation 数学上 undefined（分母为零）。论文声称扩展到 n=30 解决了问题，但 19 个 excluded tasks 同样 P=100，共线性不随 n 变化。软件返回 r=0.02 是 floating-point artifact，不是有意义统计量。\n\nR1 建议：删除 partial correlation 数值，改为纯代数论证（collinearity 本身证明 r=0.97 是 structural）；或改用 corr(Δ_nd, δ) 作为替代。\n\n**W2 [Warning] Capacity scaling 报告不一致**\n\nMain text 报告 controlled replication (4 seeds): 0.6B=50.7%, 1.7B=43.1±1.0%, 4B=59.0%。Appendix Table 8 报告不同 1.7B 数值 (47.1±2.2%, 8 seeds)。Dual-reporting 造成混淆，且 main text 中 0.6B/4B 缺少 error bars。\n\n**W3 [Warning] Cluster bootstrap (K=11) 覆盖率问题**\n\nK=11 远低于 cluster bootstrap 所需最低集群数（Cameron et al. 2008 建议 K≥40）。CI 上界 100% 是 small-K artifact。缺少 formal citation 和 coverage caveat。\n\n**W4 [Warning] McNemar test (MATH) discordant counts 与 p-value 不一致**\n\n107 int-preferred + 95 det-preferred → 按 McNemar χ²=(12)²/202=0.71, p≈0.40，与报告的 p=0.81 不一致。可能 McNemar 用的是 binary correct/incorrect discordant pairs（与 score-based routing labels 不同），但论文未明确区分。\n\n**W5 [Warning] Prescreening 条件与 generalization scope 的张力**\n\n11/30 tasks (37%)，排除 63%。虽有 anti-cherry-picking ��护，但 Abstract/Conclusion 的 framing 仍偏向暗示 ScienceWorld-wide finding。\n\n**W6 [Minor] \\nolinenumbers 格式违规**\n\n**W7 [Minor] Mann-Whitney vs. paired test**\n\n---\n\n### Reviewer 1 的 Statistical Issues:\n1. [Critical] Partial correlation undefined due to perfect collinearity\n2. [Warning] McNemar p-value 与 discordant counts 不一致\n3. [Warning] Cluster bootstrap K=11 unknown coverage\n4. [Minor] Mann-Whitney vs Wilcoxon signed-rank\n\n---\n\n请逐条回应（W1-W7 + Statistical Issues 1-4）。",
  "reviewer_id": "2",
  "project": "simgate-modular-routing",
  "round_number": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请对每条 Weakness 和 Statistical Issue 逐条回应：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Weaknesses:\n\n**W1 [Critical] Partial correlation (r=0.02, p=0.91, df=27) 存在根本性数学错误**\n\n当 P=100 为常数时，δ·P = 100δ 与 δ 完全共线（r_{δ,δP} = 1.0），partial correlation 数学上 undefined（分母为零）。论文声称扩展到 n=30 解决了问题，但 19 个 excluded tasks 同样 P=100，共线性不随 n 变化。软件返回 r=0.02 是 floating-point artifact，不是有意义统计量。\n\nR1 建议：删除 partial correlation 数值，改为纯代数论证（collinearity 本身证明 r=0.97 是 structural）；或改用 corr(Δ_nd, δ) 作为替代。\n\n**W2 [Warning] Capacity scaling 报告不一致**\n\nMain text 报告 controlled replication (4 seeds): 0.6B=50.7%, 1.7B=43.1±1.0%, 4B=59.0%。Appendix Table 8 报告不同 1.7B 数值 (47.1±2.2%, 8 seeds)。Dual-reporting 造成混淆，且 main text 中 0.6B/4B 缺少 error bars。\n\n**W3 [Warning] Cluster bootstrap (K=11) 覆盖率问题**\n\nK=11 远低于 cluster bootstrap 所需最低集群数（Cameron et al. 2008 建议 K≥40）。CI 上界 100% 是 small-K artifact。缺少 formal citation 和 coverage caveat。\n\n**W4 [Warning] McNemar test (MATH) discordant counts 与 p-value 不一致**\n\n107 int-preferred + 95 det-preferred → 按 McNemar χ²=(12)²/202=0.71, p≈0.40，与报告的 p=0.81 不一致。可能 McNemar 用的是 binary correct/incorrect discordant pairs（与 score-based routing labels 不同），但论文未明确区分。\n\n**W5 [Warning] Prescreening 条件与 generalization scope 的张力**\n\n11/30 tasks (37%)，排除 63%。虽有 anti-cherry-picking ��护，但 Abstract/Conclusion 的 framing 仍偏向暗示 ScienceWorld-wide finding。\n\n**W6 [Minor] \\nolinenumbers 格式违规**\n\n**W7 [Minor] Mann-Whitney vs. paired test**\n\n---\n\n### Reviewer 1 的 Statistical Issues:\n1. [Critical] Partial correlation undefined due to perfect collinearity\n2. [Warning] McNemar p-value 与 discordant counts 不一致\n3. [Warning] Cluster bootstrap K=11 unknown coverage\n4. [Minor] Mann-Whitney vs Wilcoxon signed-rank\n\n---\n\n请逐条回应（W1-W7 + Statistical Issues 1-4）。",
    "reviewer_id": "2",
    "project": "simgate-modular-routing",
    "round_number": "11"
  }
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-17T06:40:51.661754+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22130
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-17T06:40:52.114247+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请对每条 Weakness 逐条回应：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Weaknesses:\n\n**W1 [Warning] LaTeX em-dash (`---`) 泛滥——AI 写作最显著标志**\n\n全文正文至少 20+ 处 `---`。列举了 Abstract、Introduction（多处双 em-dash）、Method、Experiments、Discussion、Conclusion 中的具体位置。按论文写作规范 §5.1 这是最高优先级硬规则，建议全局替换为逗号/括号/拆句。\n\n**W2 [Warning] `\\nolinenumbers` 禁用行号——ACL ARR review 格式违规**\n\nmain.tex line 23 显式禁用行号，ACL ARR review submission 要求行号，desk reject 风险。\n\n**W3 [Warning] 引用数量偏低（37 篇 vs EMNLP 典型 40-60 篇）**\n\n缺失：ToolBench (Qin+ 2024)、Safe RLHF (Dai+ 2024)。建议补 3-5 篇至 40+。\n\n**W4 [Minor] DAF 的 empirical content 在 Abstract 中仍不够直观**\n\n78.9% 和 DAF=90.4% 的关系/区别对 uninitiated reader 不清晰。建议加半句明确区分 penalty-independent vs penalty-dependent。\n\n**W5 [Minor] Experiments 段落过长过密**\n\n§4.1 和 §4.5 单段落信息密度过高，建议拆分或加 \\paragraph{} 标记。\n\n**W6 [Minor] Abstract 词数 ~201，信息密度极高**\n\n5+ 个数字在 Abstract 中，30 秒内可能难以消化。\"Algorithm~1\" 引用在 Abstract 内无法跳转。\n\n---\n\n### Reviewer 2 的 Questions:\n\n**Q1.** DAF 在 P=10 时仅 50.4%。如何定义 \"dominant\"？\n\n**Q2.** 排除的 19 types 延长 step budget 后是否会产生 routing signal？\n\n**Q3.** 框架前提 \"binary catastrophic outcomes\" 实际只在 ScienceWorld 验证——ALFWorld 无 catastrophic outcomes 却被用于展示框架 applicability。\n\n---\n\n### Reviewer 2 的写作评估:\n- Em-dash 20+ 处 [Must-Fix]\n- \\nolinenumbers [Must-Fix]\n- -ing 分词短语约 5-6 处但尚可\n- 过渡词无堆砌\n- 专有名词定义完整\n\n---\n\n### Reviewer 2 的打分:\n- Soundness: 3.5/5\n- Excitement: 2.5/5\n- Reproducibility: 4/5\n- Score: 5.5/10\n- Confidence: 4/5\n\n---\n\n请逐条回应（W1-W6 + Q1-Q3）。特别关注：\n1. 你是否同意 em-dash 问题的 severity（Warning vs Minor）？\n2. 你是否同意 Excitement 2.5/5 的评估？\n3. 你对 Q3（框架前提只在 ScienceWorld 验证）的看法？",
  "reviewer_id": "1",
  "project": "simgate-modular-routing",
  "round_number": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请对每条 Weakness 逐条回应：\n- **[AGREE]**：同意并简要说明理由\n- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Weaknesses:\n\n**W1 [Warning] LaTeX em-dash (`---`) 泛滥——AI 写作最显著标志**\n\n全文正文至少 20+ 处 `---`。列举了 Abstract、Introduction（多处双 em-dash）、Method、Experiments、Discussion、Conclusion 中的具体位置。按论文写作规范 §5.1 这是最高优先级硬规则，建议全局替换为逗号/括号/拆句。\n\n**W2 [Warning] `\\nolinenumbers` 禁用行号——ACL ARR review 格式违规**\n\nmain.tex line 23 显式禁用行号，ACL ARR review submission 要求行号，desk reject 风险。\n\n**W3 [Warning] 引用数量偏低（37 篇 vs EMNLP 典型 40-60 篇）**\n\n缺失：ToolBench (Qin+ 2024)、Safe RLHF (Dai+ 2024)。建议补 3-5 篇至 40+。\n\n**W4 [Minor] DAF 的 empirical content 在 Abstract 中仍不够直观**\n\n78.9% 和 DAF=90.4% 的关系/区别对 uninitiated reader 不清晰。建议加半句明确区分 penalty-independent vs penalty-dependent。\n\n**W5 [Minor] Experiments 段落过长过密**\n\n§4.1 和 §4.5 单段落信息密度过高，建议拆分或加 \\paragraph{} 标记。\n\n**W6 [Minor] Abstract 词数 ~201，信息密度极高**\n\n5+ 个数字在 Abstract 中，30 秒内可能难以消化。\"Algorithm~1\" 引用在 Abstract 内无法跳转。\n\n---\n\n### Reviewer 2 的 Questions:\n\n**Q1.** DAF 在 P=10 时仅 50.4%。如何定义 \"dominant\"？\n\n**Q2.** 排除的 19 types 延长 step budget 后是否会产生 routing signal？\n\n**Q3.** 框架前提 \"binary catastrophic outcomes\" 实际只在 ScienceWorld 验证——ALFWorld 无 catastrophic outcomes 却被用于展示框架 applicability。\n\n---\n\n### Reviewer 2 的写作评估:\n- Em-dash 20+ 处 [Must-Fix]\n- \\nolinenumbers [Must-Fix]\n- -ing 分词短语约 5-6 处但尚可\n- 过渡词无堆砌\n- 专有名词定义完整\n\n---\n\n### Reviewer 2 的打分:\n- Soundness: 3.5/5\n- Excitement: 2.5/5\n- Reproducibility: 4/5\n- Score: 5.5/10\n- Confidence: 4/5\n\n---\n\n请逐条回应（W1-W6 + Q1-Q3）。特别关注：\n1. 你是否同意 em-dash 问题的 severity（Warning vs Minor）？\n2. 你是否同意 Excitement 2.5/5 的评估？\n3. 你对 Q3（框架前提只在 ScienceWorld 验证）的看法？",
    "reviewer_id": "1",
    "project": "simgate-modular-routing",
    "round_number": "11"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-17T06:40:53.534330+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1420
}
```

</details>

---


### Assistant

_source line 870 · 2026-05-17T06:40:57.942477+00:00_

交叉分享已发送至两位 Reviewer。等待交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 82

## Round 82

2 recorded events


### User

_source line 871 · 2026-05-17T06:41:00.586938+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心发现：
1. **[Critical]** Partial correlation (r=0.02, p=0.91, df=27) 数学上无效——P=100 为常数时 δ·P 与 δ 完全共线，partial correlation undefined。论文从 n=11 扩展到 n=30 不解决 structural collinearity。
2. **[Warning]** McNemar p=0.81 与 discordant cell counts (107, 95) 不匹配（应得 p≈0.40）。
3. **[Warning]** Cluster bootstrap K=11 远低于可靠 coverage 所需的最低集群数。
4. **[Warning]** Capacity scaling dual-reporting 造成混淆。
5. R10-C4（data scaling overclaim）已修复；R10-C5（capacity confound）部分修复；R10-C1（df=27）未修复。

总分 6/10，Confidence 4/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 872 · 2026-05-17T06:41:06.094703+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 83

## Round 83

2 recorded events


### User

_source line 873 · 2026-05-17T06:42:55.862439+00:00_

[Reviewer 1 审稿意见]:
## Round 11 Step 2 — Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R2-W1: Em-dash 泛滥**

同意这是一个需要修复的 presentation 问题。从审稿实践看，大量 em-dash 确实是 AI 生成文本的显著标志，可能在第一印象阶段影响审稿人对论文的信任度。但我对 severity 的判断与 R2 稍有不同：这是纯粹的 surface-level 写作问题，不影响任何科学结论的有效性。在 ACL ARR 的评审维度中，它不直接映射到 Soundness 或 Excitement 扣分，而是 "presentation quality" 的减分项。建议降为 [Minor-to-Warning]——必须修复（成本极低：全局 sed 替换），但不应影响 Overall 评分超过 0.25 分。

**[AGREE] R2-W2: \nolinenumbers 格式违规**

完全同意。我在自己的审稿中也独立标注了相同问题（我的 W6）。这是 desk reject 风险项，必须在提交前修复。无异议。

**[REBUT] R2-W3: 引用数量偏低（37 篇 vs 40-60 篇）**

部分不同意。引用质量和覆盖度比数量更重要。论文 Related Work 覆盖了五个明确主题（Tool Use, Adaptive Computation, Counterfactual RL, Safe RL, LLM Agents），每个主题有 3-7 篇代表性工作。具体检查：

- **ToolBench (Qin+ 2024)** 是 tool learning benchmark，论文已引用 tool-learning-survey-2024 作为该方向的综述入口，且本文不是 tool learning 论文而是 routing signal 诊断，ToolBench 的缺失不影响 positioning。
- **Safe RLHF (Dai+ 2024)** 与本文的 "safe RL" 段落相关度有限——本文讨论的是 environment-level catastrophic failure，而 Safe RLHF 解决的是 RLHF alignment 中的 safety constraint，两者虽共享 "safe" 关键词但研究问题不同。论文已引 garcia2015comprehensive (comprehensive safe RL survey) 和 crpo-2021。

我认为当前 37 篇是可接受的下限（EMNLP Findings 的 bar 比 main conference 略宽），补 2-3 篇 most-relevant 的即可（如 concurrent tool-use decision papers: tool-overuse-illusion-2026, when2tool-2026 等已被引用）。R2 建议的"补到 40+"是合理的 minor improvement，但不应标为 Warning。

**[AGREE] R2-W4: Abstract 中 78.9% vs DAF=90.4% 的区分不够直观**

同意。Abstract 中虽然有 "penalty-independent label fraction" 和 "penalty-dependent Death Avoidance Factor" 的术语区分（第一句提到 "dual metrics"），但 78.9% 和 90.4% 紧密连续出现时，读者在 30 秒 skim 中难以抓住两者的本质差异。建议在 Abstract 中用半句话显式连接：例如 "78.9% of non-tie labels arise from death asymmetry (penalty-independent); at P=100 this translates to DAF=90.4% of the score gap (penalty-dependent)"——让因果链更明显。

**[AGREE] R2-W5: §4.1 和 §4.5 段落过密**

同意。§4.1 的主段落包含了 DAF point estimate、CI、death rates、correlation、partial correlation（存疑）、collinearity argument、label distribution——至少 7 个独立统计量在一段内。§4.5 同样密集（step-level vs episode-level accuracy、capacity scaling、data scaling、deployment score——4 个子话题一段完成）。补加 \paragraph{} 标记不增加页数但显著提升可读性。这是低成本高收益的修改。

**[AGREE] R2-W6: Abstract 信息密度过高**

同意。我在审稿时虽未将此列为 weakness，但从 reader experience 角度看，Abstract 内 5+ 个数字（78.9%, 75/95, 90.4%, 81.6%-98.8%, 795, 0.81, 59.0%）加 Algorithm~1 引用确实超出 typical ACL paper Abstract 的认知负荷。建议保留最核心的 2-3 个数字（78.9%, 90.4%, 和 MATH null），其余移入 Introduction。"Algorithm~1" 在 Abstract 中不可跳转是事实——可改为 "our labeling procedure" 或直接删除。

---

### Questions 回应

**[REBUT] R2-Q1: DAF 在 P=10 时仅 50.4%，如何定义 "dominant"？**

这个质疑有道理但论文已有回应。关键在于：论文的 "dominant" claim 有两个互补指标：

1. **Penalty-independent**: 78.9% 的 non-tie labels 来自 death asymmetry（不随 P 变化）。即使 P=0，仍然是 78.9% 的 routing decisions 由 death asymmetry 驱动。
2. **Penalty-dependent (DAF)**: 在 P=100（ScienceWorld 实际设定）下 = 90.4%。

论文在 §3.4 明确声明："DAF should therefore be interpreted relative to the environment's penalty magnitude"，且在同段提供了 penalty-independent companion metric。"Dominant" 的证据来自 78.9%（始终成立）和 DAF@P=100（环境实际设定下的表现），不依赖 P=10 的假设情景。

但我同意 R2 的隐含建议：论文可以更明确地声明 "dominant" 的判据——例如 "dominant is defined as >50% of both label attributions and score-gap attributions at the environment's actual penalty"。

**[AGREE] R2-Q2: 延长 step budget 后 19 excluded types 是否产生 routing signal？**

同意这是一个 open question，论文 Limitations 中已承认。这不是论文的缺陷而是 legitimate scope limitation。但我补充一个 R2 未提到的 nuance：即使延长 step budget 后这些 tasks 产生了 routing signal，如果 signal 仍来自 death asymmetry（更多 steps → 更多 death risk），则进一步支持而非削弱论文结论。只有当延长后产生了大量 non-death routing signal，才会实质性改变 findings。论文可以加一句讨论这种可能性。

**[REBUT] R2-Q3: 框架前提 "binary catastrophic outcomes" 只在 ScienceWorld 验证**

部分不同意 R2 的 framing。论文的 framework claim 有两层：

1. **DAF 作为 diagnostic metric**: 需要 binary catastrophic outcomes 才能计算。仅在 ScienceWorld 验证——这是事实，但 DAF 的数学定义是 general 的（任何有 death penalty 的环境都可计算）。
2. **Framework 作为 diagnostic procedure**: 包括 counterfactual labeling + signal decomposition + cross-environment comparison。这在三个环境中都成功应用：
   - ScienceWorld: 检测到 death dominance ✓
   - MATH: 检测到 confirmed null (no routing signal) ✓
   - ALFWorld: 检测到 information asymmetry mechanism ✓

ALFWorld 的使用恰恰展示了框架在 non-catastrophic 环境中的 diagnostic value——它正确识别出 "this environment does NOT have death-driven routing"，这是有用的 negative diagnosis。论文 §5 Discussion 明确说："Neither MATH nor ALFWorld provides quantitative DAF replication---true replication requires a second catastrophic-failure environment (e.g., NetHack, Crafter)."

R2 的真正 concern 应该是：**DAF>50% 的 positive finding 只在一个环境验证**。这我同意（也在我的 W5 中提到 scope limitation）。但将此说成"框架只在 ScienceWorld 验证"不准确——框架的 diagnostic flexibility 在三个环境都得到了展示。

---

### Director 提出的三个具体问题

**1. Em-dash severity: Warning vs Minor？**

我判断为 **Warning 偏 Minor**。从科学正确性看是 Minor（零影响）；从 reviewer psychology 看是 Warning（AI 标志可能触发 unconscious bias）。EMNLP 2026 审稿人对 AI-assisted writing 的敏感度可能高于以往。建议修复但不应将其与统计错误（如 partial correlation collinearity）相提并论——后者影响结论可信度，前者影响第一印象。

**2. Excitement 2.5/5 的评估？**

**不同意，我维持 3.5/5。** R2 的 2.5 似乎来自：(a) router 训练失败 = negative result = low impact；(b) scope 有限（1 env）。

我的反驳：
- **Negative result 的信息价值被低估**：论文不是"我们试了 routing 结果失败了"——而是"我们提出了一个框架来 explain WHY routing fails in specific conditions，并给出了 testable prediction (DAF decreases with model capability)"。这是 methodological contribution，不是 empirical failure report。
- **框架的 reuse potential 高**：任何做 agent routing 的后续工作都可以用 DAF+SCI 来 pre-diagnose routing signal before training expensive routers。这比"training a router and reporting numbers"有更持久的 utility。
- **EMNLP Findings 的 bar**：Findings 接收需要 "solid work with niche interest"，不需要 "broad excitement"。一个 novel diagnostic framework + informative case study 达到 Findings bar。

3.5/5 在 ACL ARR scale 对应 "Interesting; might attend presentation"——我认为 agent routing 社区的研究者确实会有兴趣了解 death avoidance dominance 这个 counterintuitive finding。

**3. Q3（框架前提只在 ScienceWorld 验证）？**

如上 REBUT 所述：框架的 diagnostic applicability 在三个环境验证（positive/null/alternative-mechanism）；DAF positive finding 仅在一个环境验证。前者是 framework contribution，后者是 empirical scope limitation。两者应分开评估。论文已在 Conclusion 给出 testable future work（NetHack, Crafter），这是 appropriate scoping。

我同意论文应该更 cautiously frame generalization——但 R2 将其表述为"框架只在 ScienceWorld 验证"过于 broad。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 874 · 2026-05-17T06:43:02.856460+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 84

## Round 84

2 recorded events


### User

_source line 875 · 2026-05-17T06:43:05.372339+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **W1-W2 (em-dash + \nolinenumbers)**: AGREE，均需修复
- **W3 (引用数量)**: REBUT，37 篇覆盖度足够，ToolBench/Safe RLHF 与本文研究问题距离较远
- **W4-W6 (presentation)**: AGREE，低成本高收益的改进
- **Q1 (DAF dominant at P=10)**: REBUT，"dominant" 证据来自 penalty-independent 78.9% + DAF@actual P=100
- **Q2 (延长 step budget)**: AGREE，是 legitimate scope limitation
- **Q3 (框架前提)**: REBUT，框架 diagnostic applicability 在三个环境均验证，只是 DAF positive finding 限于 ScienceWorld

对 Director 三个具体问题：em-dash 严重性 Warning 偏 Minor；Excitement 2.5/5 过低，我维持 3.5/5；框架前提问题应区分"framework generality"和"empirical finding generality"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 876 · 2026-05-17T06:43:18.862572+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 85

## Round 85

6 recorded events


### User

_source line 877 · 2026-05-17T06:44:12.126629+00:00_

[Reviewer 2 审稿意见]:
## Round 11 Step 2 — Reviewer 2 交叉回应 Reviewer 1

---

### W1 [Critical] Partial correlation r=0.02 存在数学错误

**[AGREE] R1-W1: 同意这是一个根本性问题。**

R1 的数学论证完全正确。当 P=100 对所有 30 个 task types 均为常数时，δ·P = 100·δ，二者 Pearson r = 1.0（完美共线）。Partial correlation of (Δ_full, δ | δ·P) 等价于 partial correlation of (Δ_full, δ | δ)，分母为零，数学上 undefined。扩展到 n=30 不解决问题——增加的 19 个 task types 同样 P=100，共线性不变。

论文在 §4.1 确实承认了 n=11 时的 collinearity（"this collinearity itself is the strongest evidence that r = 0.97 is structural"），但紧接着报告 n=30 时 r=0.02 (p=0.91, df=27)——这个数值是 floating-point artifact，不应出现在论文中。

**补充发现**：论文自身的逻辑线实际上不需要这个 partial correlation。代数论证已经完备：Δ_full ≈ δ·P + Δ_nd，当 P 是常数时，Corr(δ·P + Δ_nd, δ) → 1 as Δ_nd → 0（即 DAF → 1）。这个代数推导（§4.1 第一句 "when P is constant across tasks, Corr(P·δ + Δ_nd, δ) → 1 as DAF → 1"）已经完全证明了 r=0.97 是 structural 的，不需要 partial correlation 数值佐证。

**建议同 R1**：删除 r=0.02 (p=0.91) 数值，保留代数 collinearity 论证即可。

---

### W2 [Warning] Capacity scaling 报告不一致

**[AGREE] R1-W2: 同意 dual-reporting 造成混淆，但 paper 已有 caveat。**

Main text §4.6 报告 controlled 4-seed comparison: 1.7B = 43.1 ± 1.0%。Appendix Table 5 (tab:seed-robustness) 报告 main experiment 8-seed: 1.7B = 47.1 ± 2.2%。两个数字的差异来自不同 training configuration（4 vs 8 cross-split seeds）。

Appendix Table 8 (tab:capacity) 的 caption 已注明："†1.7B episode-level figure comes from the main experiment (§4.6) with a different training configuration (8 cross-split seeds vs. 4 seeds for 0.6B/4B); direct comparison across scales should be interpreted with this caveat。" 但这个 caveat 太弱——审稿人和读者自然会将三个 scale 的数字直接对比。

补充一个具体问题：main text 中 0.6B = "50.7%" 和 4B = "59.0%" 缺少 error bars。4B 在 Appendix 报告为 58.96 ± 1.94%，但 0.6B 的 50.67 ± 2.62%（Table 8）未在 main text 出现。审稿人会质疑 0.6B 的 50.7% 与 baseline 50.0% 是否在 CI 内（答案是 yes，CI 约 [48.0%, 53.3%]，但应明示）。

**建议**：main text 统一报告同一配置（4-seed controlled）的三个 scale 数值，带 error bars。将 8-seed 结果放 Appendix 作 robustness check。

---

### W3 [Warning] Cluster bootstrap K=11 覆盖率

**[AGREE] R1-W3: 同意 K=11 远低于 recommended minimum，CI 上界 100% 是 small-K artifact。**

Cameron, Gelbach & Miller (2008) 和 MacKinnon & Webb (2017) 等文献建议 cluster bootstrap 需 K ≥ 20-40 才有可靠 coverage。K=11 时 percentile-based CI 的实际 coverage 可能远偏离 nominal 95%。

论文称 "reflecting limited cluster count" 作为 caveat，但：
1. 未引用任何关于 cluster bootstrap minimum K 的文献
2. CI 上界 = 100% 明显是边界 artifact（DAF 不可能精确等于 100% 除非 Δ_nd = 0）
3. 未讨论 wild cluster bootstrap 等 small-K 替代方案

缓解因素：论文将 cluster bootstrap 定位为 sensitivity analysis（"As a sensitivity analysis accounting for within-task-type correlation"），primary CI 仍是 episode-level bootstrap [81.6%, 98.8%]。因此这是 presentation 问题而非 soundness 问题。

**建议**：加 caveat 引用 Cameron et al. (2008)，承认 K=11 低于常规阈值；或改用 wild cluster bootstrap。

---

### W4 [Warning] McNemar p=0.81 与 routing labels (107/95) 的表观不一致

**[REBUT] R1-W4: 反驳"不一致"的判断——p=0.81 大概率是正确的，但论文确实应澄清定义差异。**

R1 的计算：如果 107 和 95 是 McNemar discordant pairs，则 χ² = (12)²/202 = 0.71, p ≈ 0.40。报告的 p=0.81 与此不符。

但关键点：MATH 的 routing labels 和 binary accuracy discordant pairs 不一定相同。我的重构：

- 内部准确率 73.5%（≈584/795 correct），确定性准确率 73.0%（≈580/795 correct）
- binary discordant pairs: b = 584 - both_correct, c = 580 - both_correct → b - c = 4
- 如果 both_correct ≈ 481（由 no-preference 约束推导），则 b ≈ 103, c ≈ 99
- McNemar with continuity correction: (|103-99|-1)²/(103+99) = 9/202 ≈ 0.045, p ≈ 0.83

p ≈ 0.83 与报告的 p=0.81 高度吻合。说明 McNemar test 是正确地施加在 binary correct/incorrect discordant pairs 上（b≈103, c≈99），而 routing labels (107, 95) 包含了额外的 score-based discordances（例如两者都答对但 code interpreter 给出更精确解、或 intermediate scoring 差异）。

**问题所在**：论文将 McNemar p=0.81 和 routing label distribution (107/95) 并列报告（§4.3），未明确说明 McNemar 的 discordant pairs 与 routing labels 的定义不同。读者（如 R1）自然会假设 107/95 就是 McNemar 的 b/c。

**建议**：在 §4.3 加一句澄清："McNemar test 施加在 binary correct/incorrect 对上 (b=103, c=99)；routing labels (107/95) 包含额外 score-comparison discordances where accuracy is tied but scores differ." 或者如果 MATH 确实是纯 binary（无 partial credit），则需要解释 107/95 与 103/99 的差异来源。

---

### W5 [Warning] Prescreening scope 与 framing 的张力

**[REBUT] R1-W5: 反驳——当前版本 framing 已足够保守。**

审查 Abstract、Introduction、Conclusion 的具体措辞：
- Abstract: "As a diagnostic case study, we apply this framework to ScienceWorld (11 of 30 task types, 245 episodes, Qwen2.5-7B-Instruct)"
- Introduction Contribution 2: "Empirical application to ScienceWorld"
- Conclusion: "Applied as a case study to 245 ScienceWorld episodes (11 of 30 task types, Qwen2.5-7B-Instruct)"

"11 of 30 task types" 出现在所有关键位置。标题明确写 "on ScienceWorld"（非 "in all interactive environments"）。Contribution 3 明确说 "demonstrate diagnostic applicability, not universality"。Limitations 段进一步解释排除原因（"both strategies time out within 30 steps"）。Appendix B 有 anti-cherry-picking 段落。

我不认为当前 framing "暗示 ScienceWorld-wide finding"。如果 R1 能指出具体哪句话有 over-claim，可以针对性修改。但 general 层面的 framing 已经是 case study 定位了。

---

### W6 [Minor] \nolinenumbers

**[AGREE] R1-W6: 完全同意。**

我在自己的 Round 11 review (W2) 中也独立发现了这个问题。main.tex line 23 的 `\nolinenumbers` 禁用了 `[review]` 模式的行号，违反 ACL ARR review submission 要求。必须删除。

---

### W7 [Minor] Mann-Whitney vs. paired test

**[AGREE] R1-W7: 同意这是一个 minor methodological concern。**

Method §3.1 的 reasoning-depth ablation: "6 overlapping task types (n=120 episodes per condition)"。如果同一 task instance 在两个条件（chain-of-thought vs direct-answer）下都被测试（same seed），则数据是 paired 的，Wilcoxon signed-rank test 更合适且统计功效更高。

缓解因素：Mann-Whitney 仍是 valid test（只是 less powerful），且报告的结论是 null result (p > 0.26)。如果更 powerful 的 paired test 仍然 non-significant，null 结论更强。如果 paired test 变 significant，则需要重新审视。但给定 |d| ≤ 0.31（小效应量）和 near-identical death rates (41.8% vs 42.5%)，paired test 翻转结论的可能性极低。

**建议**：明确数据是否 paired。如果是，改用 Wilcoxon signed-rank 并重新报告 p 值。

---

## Statistical Issues 逐条回应

**Issue 1 [Critical]: Partial correlation undefined** → **[AGREE]** 见 W1。

**Issue 2 [Warning]: McNemar p-value 不一致** → **[REBUT]** 见 W4。p=0.81 大概率正确（对 binary accuracy discordant pairs ≈103/99 with continuity correction），但论文需澄清 routing labels ≠ McNemar discordant pairs。

**Issue 3 [Warning]: Cluster bootstrap K=11 coverage** → **[AGREE]** 见 W3。需补 citation 和 caveat。

**Issue 4 [Minor]: Mann-Whitney vs Wilcoxon signed-rank** → **[AGREE]** 见 W7。Minor，大概率不影响结论。

---

## 综合判断

R1 的审查严谨且具建设性。W1（partial correlation）是一个需要修复的真实统计错误——不是论文核心论点有问题（代数论证已完备），而是不应报告一个 mathematically undefined 的数值。W4（McNemar）经我独立验证后认为 p=0.81 大概率正确，但论文表述确实会引起误解。其余 Warnings (W2, W3, W5) 是 presentation/rigor improvements，不影响核心 claim。

对论文评分的影响：W1 修复后（删除 r=0.02 数值，保留代数论证），soundness 不受实质影响。W4 需要一句澄清。整体不改变我的 Findings borderline accept 判断（5.5/10）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-17T06:46:34.194549+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "- id: \"R11-C1\"\n  summary: \"Partial correlation (r=0.02, p=0.91, df=27) mathematically undefined — perfect collinearity when P is constant\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-C1: df=27 error. Paper claimed n=30 resolves it.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus. Problem NOT resolved by expanding to n=30. When P=100 is constant across all tasks, δ·P = 100δ → r(δ, δ·P)=1.0 → partial correlation denominator=0 → undefined. Software returning r=0.02 is floating-point artifact. Paper's own algebraic argument (collinearity proves r=0.97 is structural) is sufficient without the invalid numerical statistic. Must delete r=0.02/p=0.91/df=27 from Abstract, Introduction, §4.1, and Conclusion.\"\n  action_items:\n    - round: 11\n      action: \"Delete all instances of partial correlation r=0.02, p=0.91, df=27. Replace with pure algebraic argument: 'When P is constant, δ·P is perfectly collinear with δ, making r=0.97 a mathematical consequence of death dominance rather than an independent empirical finding.' Keep the collinearity-as-evidence framing.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Em-dash (---) 泛滥 — 20+ instances, AI writing signature\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus (R1 rates Warning-to-Minor, R2 rates Warning). At least 20 em-dashes across Abstract, Introduction, Method, Experiments, Discussion, Conclusion. Most obvious AI writing marker. No impact on soundness but affects reviewer trust/first impression. Low-cost fix: global grep and replace with commas/parentheses/sentence splits.\"\n  action_items:\n    - round: 11\n      action: \"grep '---' *.tex and replace all explanatory em-dashes with commas, parentheses, or sentence splits. Preserve en-dashes (--) in number ranges (20--40) and proper nouns (Mann--Whitney, Newton--Raphson).\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"\\\\nolinenumbers violates ACL ARR review submission format — desk reject risk\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus. Both reviewers independently flagged. main.tex line 23 has \\\\nolinenumbers after \\\\maketitle, overriding [review] mode line numbers. ACL ARR requires line numbers for review submission. Desk reject risk.\"\n  action_items:\n    - round: 11\n      action: \"Delete \\\\nolinenumbers from main.tex.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Capacity scaling dual-reporting — two incompatible 1.7B numbers confuse readers\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus. Main text: 1.7B=43.1±1.0% (4 seeds, controlled). Appendix Table 8: 1.7B=47.1±2.2% (8 seeds, original). Caption caveat exists but too weak. Also 0.6B and 4B lack error bars in main text despite having them in Appendix (50.67±2.62%, 58.96±1.94%).\"\n  action_items:\n    - round: 11\n      action: \"Unify: main text reports controlled 4-seed numbers WITH error bars for all three scales. Move 8-seed results to Appendix as robustness check. Add Table 8 row for controlled replication.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Cluster bootstrap K=11 — below minimum cluster count, needs formal citation and caveat\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus. K=11 far below Cameron, Gelbach & Miller (2008) recommended K≥40. CI upper bound=100% is small-K artifact (bootstrap resamples missing find-non-living-thing inflate DAF). Paper says 'reflecting limited cluster count' but no formal citation on small-K limitations. Mitigated by positioning as sensitivity analysis (primary CI is episode-level [81.6%, 98.8%]).\"\n  action_items:\n    - round: 11\n      action: \"Add citation (Cameron et al. 2008 or MacKinnon & Webb 2017) and explicit statement: 'K=11 is below standard thresholds for reliable cluster bootstrap coverage; this CI should be interpreted cautiously.'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W5\"\n  summary: \"McNemar test input not clearly distinguished from routing labels — needs clarification sentence\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 flagged p=0.81 as inconsistent with routing labels (107/95 → p≈0.40). R2 rebutted with reconstruction: McNemar applied to binary correct/incorrect discordant pairs (≈103/99 with continuity correction → p≈0.83), not routing labels (107/95 which include score-comparison discordances). Consensus: p=0.81 is likely correct but paper must clarify that McNemar tests binary accuracy, not routing labels.\"\n  action_items:\n    - round: 11\n      action: \"Add clarifying sentence in §4.3: 'McNemar test is applied to binary correct/incorrect discordant pairs (b=X, c=Y); routing labels (107/95) additionally include score-comparison discordances where both answers are correct but scores differ.'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m1\"\n  summary: \"§4.1 and §4.5 paragraphs too dense — split for readability\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus. §4.1 main paragraph has 7+ statistics in one block. §4.5 covers 4 sub-topics in one paragraph. Low-cost fix: add \\\\paragraph{} markers.\"\n  action_items:\n    - round: 11\n      action: \"Split §4.1 into 2-3 sub-paragraphs (decomposition results / correlation analysis / label distribution). Split §4.5 similarly.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Abstract 78.9% vs DAF=90.4% distinction not intuitive for uninitiated readers\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus. Two metrics appear consecutively without explicit causal link. Suggest: '78.9% of non-tie labels arise from death asymmetry (penalty-independent); at P=100 this translates to DAF=90.4% of the score gap (penalty-dependent).'\"\n  action_items:\n    - round: 11\n      action: \"Add half-sentence in Abstract clarifying the penalty-independent→penalty-dependent causal chain.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m3\"\n  summary: \"Mann-Whitney vs Wilcoxon signed-rank for reasoning depth ablation — paired design unclear\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus (minor). If same task instances tested under both conditions, should use Wilcoxon signed-rank. Given null result with small effect size (|d|≤0.31), unlikely to change conclusion. Paper should clarify experimental design.\"\n  action_items:\n    - round: 11\n      action: \"Clarify whether reasoning-depth ablation uses paired task instances. If yes, report Wilcoxon signed-rank p-value.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Previously tracked issues: status updates ---\n\n- id: \"R10-C1\"\n  summary: \"df=27 statistical error in partial correlation — invalidates key supporting evidence\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. Section 4.1 reports partial r=0.02, p=0.91, df=27. With n=11 task types and 1 control variable, df should be 8. If episode-level (N=245), df=242. df=27 impossible under any valid computation. Error undermines the 'r=0.97 is mathematical artifact' argument — the conclusion likely still holds (r=0.02 is tiny) but statistical reporting is wrong.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"NOT fixed. Paper resolved df issue by expanding to n=30 (df=n-k-2=27 formally correct), but fundamental problem persists: P=100 constant → δ·P perfectly collinear with δ → partial correlation undefined regardless of n. Superseded by R11-C1.\"\n  action_items:\n    - round: 10\n      action: \"Recompute partial correlation at task-level (df=8) and report correct p-value.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C2\"\n  summary: \"Core finding novelty insufficient — DAF near-tautological, 78.9% is the real empirical content\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. DAF=δP/(δP+Δ_nd) approaching 1 when P>>Δ_nd is mathematical necessity.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"RESOLVED. Paper now leads with 78.9% as headline, DAF positioned as secondary summary tool. Abstract, Intro, Contributions all restructured. §3.4 explicitly states DAF increase is 'mathematical consequence, not empirical finding.'\"\n  action_items:\n    - round: 10\n      action: \"Restructure contribution framing: lead with empirical findings (δ, Δ_nd, 78.9%) not derived metric (DAF).\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Framing restructured. 78.9% is primary headline throughout. DAF positioned as penalty-dependent companion metric.\"\n  resolution_round: 11\n\n- id: \"R10-C3\"\n  summary: \"Single-environment evidence — no cross-env REPLICATION of death-dominance finding\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Contribution 3 still oversells.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"RESOLVED. Contribution 3 now says 'Framework flexibility illustration' with explicit 'demonstrate diagnostic applicability, not universality'. Discussion says 'true replication requires second catastrophic-failure environment'. R2 verified specific text in Abstract/Intro/Conclusion all say '11 of 30 task types'. R1 still notes scope limitation but agrees current framing is acceptable.\"\n  action_items:\n    - round: 10\n      action: \"Retitle/downgrade Contribution 3.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Contribution 3 appropriately scoped as 'framework flexibility illustration, not universality'.\"\n  resolution_round: 11\n\n- id: \"R10-C4\"\n  summary: \"Data scaling ablation uses augmentation — cannot rule out real-data scarcity\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper partially addressed.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"RESOLVED. Main text uses 'provides no improvement' (not 'rules out'). Explicit distinction between augmentation-based vs real-data scaling. Appendix acknowledges 'episode-level minority-class diversity remains a potential confound'.\"\n  action_items:\n    - round: 10\n      action: \"Unify language: remove 'rules out' from main text.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Language unified. No overclaiming.\"\n  resolution_round: 11\n\n- id: \"R10-C5\"\n  summary: \"Capacity scaling confound — 1.7B uses 8 seeds vs 4 for 0.6B/4B, non-monotonic result\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Confound eliminated with controlled replication.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Confound resolved (controlled 4-seed replication confirms U-shaped: 0.6B=50.7%, 1.7B=43.1%, 4B=59.0%). Residual issue: dual-reporting confusion tracked as R11-W3.\"\n  action_items:\n    - round: 10\n      action: \"Rerun under identical config OR acknowledge confound.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Controlled replication done. Non-monotonicity confirmed as real. Reporting consistency issue tracked as R11-W3.\"\n  resolution_round: 11\n\n- id: \"R10-W1\"\n  summary: \"Router failure does not 'validate' analytical framework — overclaimed causal link\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. Changed to 'consistent with' throughout.\"\n  action_items:\n    - round: 10\n      action: \"Replace 'validates' with 'consistent with'.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-W2\"\n  summary: \"'Environment-agnostic' overclaim — framework requires specific preconditions\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. No 'environment-agnostic' in paper. Uses 'applicable to environments with binary catastrophic outcomes and controllable modality comparison'.\"\n  action_items:\n    - round: 10\n      action: \"Weaken to 'applicable to environments with...'.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-W3\"\n  summary: \"Related work gaps — AgentBench, LATS, hallucination detection, Safe RLHF, ToolBench\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Mostly resolved. AgentBench, LATS, SelfCheckGPT, NetHack, Crafter all cited. R2 notes ToolBench and Safe RLHF still missing (37 total refs). R1 rebuts: 37 acceptable for Findings, ToolBench/SafeRLHF not directly relevant. Minor divergence — 2-3 additional refs are nice-to-have but not blocking.\"\n  action_items:\n    - round: 10\n      action: \"Add key missing refs.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Core gaps filled. Residual 2-3 refs are optional improvement.\"\n  resolution_round: 11\n\n- id: \"R10-W4\"\n  summary: \"Bootstrap CI needs cluster-level sensitivity analysis (task-type clusters)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Cluster bootstrap implemented and reported [73.3%, 100%]. Residual: needs formal citation on K-minimum requirements. Tracked as R11-W4.\"\n  action_items:\n    - round: 10\n      action: \"Report cluster bootstrap CI.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Implemented. Citation gap tracked as R11-W4.\"\n  resolution_round: 11\n\n- id: \"R10-W5\"\n  summary: \"Cross-model evidence (Llama N=70) only shows 'similar model dies more' — unsurprising\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. Framed as 'preliminary pilot confirming direction' with explicit testable predictions (larger models, Reflexion).\"\n  action_items:\n    - round: 10\n      action: \"Frame as preliminary pilot.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-W6\"\n  summary: \"MATH claim still overclaimed despite power analysis addition\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. Uses 'confirmed null' with p-value and CI. No 'consistent with framework prediction' overclaim.\"\n  action_items:\n    - round: 10\n      action: \"Replace with conservative wording.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-W7\"\n  summary: \"Task selection survivorship bias — SCI=0.2147 'systematic' claim misleading given 63% exclusion\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. Now says 'systematic across all task types exhibiting routing signal (11/30 after prescreening)'.\"\n  action_items:\n    - round: 10\n      action: \"Add qualifier.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-m1\"\n  summary: \"Modality definition disconnect — oracle state ≠ practical tool-use routing\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. Discussion has paragraph on oracle vs imperfect tools, DAF with imperfect tools, safety-first principle.\"\n  action_items:\n    - round: 10\n      action: \"Add Discussion paragraph.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-m2\"\n  summary: \"Title overclaims — 'the Dominant Routing Signal' verified in single environment only\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. Title changed to 'Death Avoidance as a Dominant Routing Signal' (indefinite article).\"\n  action_items:\n    - round: 10\n      action: \"Consider title revision.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Title uses 'a Dominant' instead of 'the Dominant'.\"\n  resolution_round: 11\n\n# Older resolved issues retained for history\n- id: \"R6-C1\"\n  summary: \"DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not primary\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Framing fix confirmed.\"\n  action_items: []\n  resolution: \"Fixed in R10.\"\n  resolution_round: 10\n\n- id: \"R6-W1\"\n  summary: \"r=0.97 structural coupling — qualifier insufficient in Abstract/Conclusion\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Qualifier upgraded.\"\n  action_items: []\n  resolution: \"Fixed in R10.\"\n  resolution_round: 10\n\n- id: \"R6-C2\"\n  summary: \"Missing counterfactual-in-RL literature paragraph\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions: []\n  action_items: []\n  resolution: \"Fixed in R6.\"\n  resolution_round: 6\n\n- id: \"R6-W2\"\n  summary: \"Prescreening 19/30 exclusion — scope qualifier needed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions: []\n  action_items: []\n  resolution: \"Fixed in R8.\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "simgate-modular-routing",
    "issues_yaml": "- id: \"R11-C1\"\n  summary: \"Partial correlation (r=0.02, p=0.91, df=27) mathematically undefined — perfect collinearity when P is constant\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-C1: df=27 error. Paper claimed n=30 resolves it.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus. Problem NOT resolved by expanding to n=30. When P=100 is constant across all tasks, δ·P = 100δ → r(δ, δ·P)=1.0 → partial correlation denominator=0 → undefined. Software returning r=0.02 is floating-point artifact. Paper's own algebraic argument (collinearity proves r=0.97 is structural) is sufficient without the invalid numerical statistic. Must delete r=0.02/p=0.91/df=27 from Abstract, Introduction, §4.1, and Conclusion.\"\n  action_items:\n    - round: 11\n      action: \"Delete all instances of partial correlation r=0.02, p=0.91, df=27. Replace with pure algebraic argument: 'When P is constant, δ·P is perfectly collinear with δ, making r=0.97 a mathematical consequence of death dominance rather than an independent empirical finding.' Keep the collinearity-as-evidence framing.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W1\"\n  summary: \"Em-dash (---) 泛滥 — 20+ instances, AI writing signature\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus (R1 rates Warning-to-Minor, R2 rates Warning). At least 20 em-dashes across Abstract, Introduction, Method, Experiments, Discussion, Conclusion. Most obvious AI writing marker. No impact on soundness but affects reviewer trust/first impression. Low-cost fix: global grep and replace with commas/parentheses/sentence splits.\"\n  action_items:\n    - round: 11\n      action: \"grep '---' *.tex and replace all explanatory em-dashes with commas, parentheses, or sentence splits. Preserve en-dashes (--) in number ranges (20--40) and proper nouns (Mann--Whitney, Newton--Raphson).\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W2\"\n  summary: \"\\\\nolinenumbers violates ACL ARR review submission format — desk reject risk\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus. Both reviewers independently flagged. main.tex line 23 has \\\\nolinenumbers after \\\\maketitle, overriding [review] mode line numbers. ACL ARR requires line numbers for review submission. Desk reject risk.\"\n  action_items:\n    - round: 11\n      action: \"Delete \\\\nolinenumbers from main.tex.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W3\"\n  summary: \"Capacity scaling dual-reporting — two incompatible 1.7B numbers confuse readers\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus. Main text: 1.7B=43.1±1.0% (4 seeds, controlled). Appendix Table 8: 1.7B=47.1±2.2% (8 seeds, original). Caption caveat exists but too weak. Also 0.6B and 4B lack error bars in main text despite having them in Appendix (50.67±2.62%, 58.96±1.94%).\"\n  action_items:\n    - round: 11\n      action: \"Unify: main text reports controlled 4-seed numbers WITH error bars for all three scales. Move 8-seed results to Appendix as robustness check. Add Table 8 row for controlled replication.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W4\"\n  summary: \"Cluster bootstrap K=11 — below minimum cluster count, needs formal citation and caveat\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus. K=11 far below Cameron, Gelbach & Miller (2008) recommended K≥40. CI upper bound=100% is small-K artifact (bootstrap resamples missing find-non-living-thing inflate DAF). Paper says 'reflecting limited cluster count' but no formal citation on small-K limitations. Mitigated by positioning as sensitivity analysis (primary CI is episode-level [81.6%, 98.8%]).\"\n  action_items:\n    - round: 11\n      action: \"Add citation (Cameron et al. 2008 or MacKinnon & Webb 2017) and explicit statement: 'K=11 is below standard thresholds for reliable cluster bootstrap coverage; this CI should be interpreted cautiously.'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-W5\"\n  summary: \"McNemar test input not clearly distinguished from routing labels — needs clarification sentence\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 flagged p=0.81 as inconsistent with routing labels (107/95 → p≈0.40). R2 rebutted with reconstruction: McNemar applied to binary correct/incorrect discordant pairs (≈103/99 with continuity correction → p≈0.83), not routing labels (107/95 which include score-comparison discordances). Consensus: p=0.81 is likely correct but paper must clarify that McNemar tests binary accuracy, not routing labels.\"\n  action_items:\n    - round: 11\n      action: \"Add clarifying sentence in §4.3: 'McNemar test is applied to binary correct/incorrect discordant pairs (b=X, c=Y); routing labels (107/95) additionally include score-comparison discordances where both answers are correct but scores differ.'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m1\"\n  summary: \"§4.1 and §4.5 paragraphs too dense — split for readability\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus. §4.1 main paragraph has 7+ statistics in one block. §4.5 covers 4 sub-topics in one paragraph. Low-cost fix: add \\\\paragraph{} markers.\"\n  action_items:\n    - round: 11\n      action: \"Split §4.1 into 2-3 sub-paragraphs (decomposition results / correlation analysis / label distribution). Split §4.5 similarly.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m2\"\n  summary: \"Abstract 78.9% vs DAF=90.4% distinction not intuitive for uninitiated readers\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus. Two metrics appear consecutively without explicit causal link. Suggest: '78.9% of non-tie labels arise from death asymmetry (penalty-independent); at P=100 this translates to DAF=90.4% of the score gap (penalty-dependent).'\"\n  action_items:\n    - round: 11\n      action: \"Add half-sentence in Abstract clarifying the penalty-independent→penalty-dependent causal chain.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-m3\"\n  summary: \"Mann-Whitney vs Wilcoxon signed-rank for reasoning depth ablation — paired design unclear\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Consensus (minor). If same task instances tested under both conditions, should use Wilcoxon signed-rank. Given null result with small effect size (|d|≤0.31), unlikely to change conclusion. Paper should clarify experimental design.\"\n  action_items:\n    - round: 11\n      action: \"Clarify whether reasoning-depth ablation uses paired task instances. If yes, report Wilcoxon signed-rank p-value.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Previously tracked issues: status updates ---\n\n- id: \"R10-C1\"\n  summary: \"df=27 statistical error in partial correlation — invalidates key supporting evidence\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. Section 4.1 reports partial r=0.02, p=0.91, df=27. With n=11 task types and 1 control variable, df should be 8. If episode-level (N=245), df=242. df=27 impossible under any valid computation. Error undermines the 'r=0.97 is mathematical artifact' argument — the conclusion likely still holds (r=0.02 is tiny) but statistical reporting is wrong.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"NOT fixed. Paper resolved df issue by expanding to n=30 (df=n-k-2=27 formally correct), but fundamental problem persists: P=100 constant → δ·P perfectly collinear with δ → partial correlation undefined regardless of n. Superseded by R11-C1.\"\n  action_items:\n    - round: 10\n      action: \"Recompute partial correlation at task-level (df=8) and report correct p-value.\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-C2\"\n  summary: \"Core finding novelty insufficient — DAF near-tautological, 78.9% is the real empirical content\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Consensus. DAF=δP/(δP+Δ_nd) approaching 1 when P>>Δ_nd is mathematical necessity.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"RESOLVED. Paper now leads with 78.9% as headline, DAF positioned as secondary summary tool. Abstract, Intro, Contributions all restructured. §3.4 explicitly states DAF increase is 'mathematical consequence, not empirical finding.'\"\n  action_items:\n    - round: 10\n      action: \"Restructure contribution framing: lead with empirical findings (δ, Δ_nd, 78.9%) not derived metric (DAF).\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Framing restructured. 78.9% is primary headline throughout. DAF positioned as penalty-dependent companion metric.\"\n  resolution_round: 11\n\n- id: \"R10-C3\"\n  summary: \"Single-environment evidence — no cross-env REPLICATION of death-dominance finding\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Contribution 3 still oversells.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"RESOLVED. Contribution 3 now says 'Framework flexibility illustration' with explicit 'demonstrate diagnostic applicability, not universality'. Discussion says 'true replication requires second catastrophic-failure environment'. R2 verified specific text in Abstract/Intro/Conclusion all say '11 of 30 task types'. R1 still notes scope limitation but agrees current framing is acceptable.\"\n  action_items:\n    - round: 10\n      action: \"Retitle/downgrade Contribution 3.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Contribution 3 appropriately scoped as 'framework flexibility illustration, not universality'.\"\n  resolution_round: 11\n\n- id: \"R10-C4\"\n  summary: \"Data scaling ablation uses augmentation — cannot rule out real-data scarcity\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Paper partially addressed.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"RESOLVED. Main text uses 'provides no improvement' (not 'rules out'). Explicit distinction between augmentation-based vs real-data scaling. Appendix acknowledges 'episode-level minority-class diversity remains a potential confound'.\"\n  action_items:\n    - round: 10\n      action: \"Unify language: remove 'rules out' from main text.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Language unified. No overclaiming.\"\n  resolution_round: 11\n\n- id: \"R10-C5\"\n  summary: \"Capacity scaling confound — 1.7B uses 8 seeds vs 4 for 0.6B/4B, non-monotonic result\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Confound eliminated with controlled replication.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Confound resolved (controlled 4-seed replication confirms U-shaped: 0.6B=50.7%, 1.7B=43.1%, 4B=59.0%). Residual issue: dual-reporting confusion tracked as R11-W3.\"\n  action_items:\n    - round: 10\n      action: \"Rerun under identical config OR acknowledge confound.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Controlled replication done. Non-monotonicity confirmed as real. Reporting consistency issue tracked as R11-W3.\"\n  resolution_round: 11\n\n- id: \"R10-W1\"\n  summary: \"Router failure does not 'validate' analytical framework — overclaimed causal link\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. Changed to 'consistent with' throughout.\"\n  action_items:\n    - round: 10\n      action: \"Replace 'validates' with 'consistent with'.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-W2\"\n  summary: \"'Environment-agnostic' overclaim — framework requires specific preconditions\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. No 'environment-agnostic' in paper. Uses 'applicable to environments with binary catastrophic outcomes and controllable modality comparison'.\"\n  action_items:\n    - round: 10\n      action: \"Weaken to 'applicable to environments with...'.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-W3\"\n  summary: \"Related work gaps — AgentBench, LATS, hallucination detection, Safe RLHF, ToolBench\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Mostly resolved. AgentBench, LATS, SelfCheckGPT, NetHack, Crafter all cited. R2 notes ToolBench and Safe RLHF still missing (37 total refs). R1 rebuts: 37 acceptable for Findings, ToolBench/SafeRLHF not directly relevant. Minor divergence — 2-3 additional refs are nice-to-have but not blocking.\"\n  action_items:\n    - round: 10\n      action: \"Add key missing refs.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Core gaps filled. Residual 2-3 refs are optional improvement.\"\n  resolution_round: 11\n\n- id: \"R10-W4\"\n  summary: \"Bootstrap CI needs cluster-level sensitivity analysis (task-type clusters)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Cluster bootstrap implemented and reported [73.3%, 100%]. Residual: needs formal citation on K-minimum requirements. Tracked as R11-W4.\"\n  action_items:\n    - round: 10\n      action: \"Report cluster bootstrap CI.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Implemented. Citation gap tracked as R11-W4.\"\n  resolution_round: 11\n\n- id: \"R10-W5\"\n  summary: \"Cross-model evidence (Llama N=70) only shows 'similar model dies more' — unsurprising\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. Framed as 'preliminary pilot confirming direction' with explicit testable predictions (larger models, Reflexion).\"\n  action_items:\n    - round: 10\n      action: \"Frame as preliminary pilot.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-W6\"\n  summary: \"MATH claim still overclaimed despite power analysis addition\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. Uses 'confirmed null' with p-value and CI. No 'consistent with framework prediction' overclaim.\"\n  action_items:\n    - round: 10\n      action: \"Replace with conservative wording.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-W7\"\n  summary: \"Task selection survivorship bias — SCI=0.2147 'systematic' claim misleading given 63% exclusion\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. Now says 'systematic across all task types exhibiting routing signal (11/30 after prescreening)'.\"\n  action_items:\n    - round: 10\n      action: \"Add qualifier.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-m1\"\n  summary: \"Modality definition disconnect — oracle state ≠ practical tool-use routing\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. Discussion has paragraph on oracle vs imperfect tools, DAF with imperfect tools, safety-first principle.\"\n  action_items:\n    - round: 10\n      action: \"Add Discussion paragraph.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-m2\"\n  summary: \"Title overclaims — 'the Dominant Routing Signal' verified in single environment only\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"RESOLVED. Title changed to 'Death Avoidance as a Dominant Routing Signal' (indefinite article).\"\n  action_items:\n    - round: 10\n      action: \"Consider title revision.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Title uses 'a Dominant' instead of 'the Dominant'.\"\n  resolution_round: 11\n\n# Older resolved issues retained for history\n- id: \"R6-C1\"\n  summary: \"DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not primary\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Framing fix confirmed.\"\n  action_items: []\n  resolution: \"Fixed in R10.\"\n  resolution_round: 10\n\n- id: \"R6-W1\"\n  summary: \"r=0.97 structural coupling — qualifier insufficient in Abstract/Conclusion\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Qualifier upgraded.\"\n  action_items: []\n  resolution: \"Fixed in R10.\"\n  resolution_round: 10\n\n- id: \"R6-C2\"\n  summary: \"Missing counterfactual-in-RL literature paragraph\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions: []\n  action_items: []\n  resolution: \"Fixed in R6.\"\n  resolution_round: 6\n\n- id: \"R6-W2\"\n  summary: \"Prescreening 19/30 exclusion — scope qualifier needed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions: []\n  action_items: []\n  resolution: \"Fixed in R8.\"\n  resolution_round: 8"
  }
}
```

</details>

---


### Tool result

_source line 879 · 2026-05-17T06:46:34.348070+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 19643}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-17T06:48:10.217363+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 11 审稿报告 — simgate-modular-routing\n\n**论文**: Death Avoidance as a Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**目标**: EMNLP 2026 Findings (via ARR May 2026)\n**Reviewers**: R1 (方法严谨性+统计推断), R2 (新颖性+写作+Related Work)\n\n---\n\n## Summary\n\n论文提出 episode-level counterfactual 框架（Algorithm 1 + DAF + SCI）用于诊断 modular LLM agent 的 routing signal 来源。以 ScienceWorld 为 case study（11/30 task types, N=245, Qwen2.5-7B-Instruct），发现 78.9% 的 non-tie routing labels 由 death asymmetry 驱动，DAF=90.4%@P=100。跨环境（MATH confirmed null, ALFWorld information asymmetry）和跨模型（Llama pilot）分析展示框架 diagnostic flexibility。Router training 作为 informative negative 支持 analytical framework 优于 brute-force learned routing 的结论。\n\n---\n\n## Strengths\n\n1. **R10 问题修复优秀**：前轮 12 条 open issues 中，10 条已完全修复（R10-C2/C3/C4/W1/W2/W5/W6/W7/m1/m2），1 条部分修复（R10-W3 引用），1 条未修复（R10-C1 partial correlation, 升级为 R11-C1）。Claim calibration 全文一致。\n\n2. **方法论透明度**：DAF 的 mathematical nature（随 P 单调递增）被显式承认为 \"mathematical consequence, not empirical finding\"；r=0.97 被定位为 \"internal consistency check\"；data scaling 区分 augmentation vs real-data；cross-model 标注 \"preliminary pilot\"。\n\n3. **框架设计合理**：Algorithm 1 逻辑无歧义（四个 mutually exclusive cases），DAF decomposition 数学正确，SCI 有效补充 \"systematic vs outlier-driven\" 问题。Dual-metric（penalty-independent 78.9% + penalty-dependent DAF）设计使结论不依赖单一假设。\n\n4. **统计实践规范**：Episode-level bootstrap (B=10,000), cluster bootstrap sensitivity, McNemar test, LOO robustness, penalty sensitivity, seed robustness（8 seeds）, capacity scaling controlled replication。\n\n5. **Negative result 有价值**：Router diagnostic 不是 \"failure report\" 而是 \"framework predicts and explains why routing fails\"——对 agent routing 社区有实际指导意义。\n\n---\n\n## Weaknesses\n\n### Must-Fix (投稿前)\n\n**[Critical] W1: Partial correlation (r=0.02, p=0.91, df=27) 数学上 undefined**\n- 位置：Abstract, Introduction, §4.1, Conclusion（4 处引用）\n- 问题：P=100 对所有 task types 为常数 → δ·P = 100δ → r(δ, δ·P) = 1.0 → partial correlation 分母为零 → undefined。扩展到 n=30 不解决 structural collinearity。r=0.02 是 floating-point artifact。\n- 影响：论文核心论证（r=0.97 is structural）的支撑证据无效。概念论证正确但数值报告有误，损害全文统计可信度。\n- 修复：删除 r=0.02/p=0.91/df=27 所有出现，替换为代数论证：\"When P is constant across tasks, δ·P is perfectly collinear with δ; this collinearity proves r=0.97 is a mathematical consequence of death dominance.\" 或改用 corr(Δ_nd, δ) 作为替代 well-defined statistic。\n\n**[Warning] W2: Em-dash (---) 泛滥，20+ 处 AI 写作标志**\n- 位置：全文正文（Abstract 到 Conclusion）\n- 影响：不影响 soundness 但触发 reviewer 对 AI-generated content 的警觉\n- 修复：全局 `grep \"---\" *.tex`，替换为逗号/括号/拆句。保留 en-dash (--) 数字范围和专有名词。\n\n**[Warning] W3: \\nolinenumbers 违反 ACL ARR review 格式**\n- 位置：main.tex line 23\n- 影响：Desk reject 风险\n- 修复：删除 `\\nolinenumbers`\n\n### Should-Fix\n\n**[Warning] W4: Capacity scaling dual-reporting**\n- Main text (4-seed controlled): 0.6B=50.7%, 1.7B=43.1±1.0%, 4B=59.0%\n- Appendix Table 8 (8-seed original): 1.7B=47.1±2.2%\n- 两套 1.7B 数字共存造成混淆。0.6B/4B 在 main text 缺 error bars。\n- 修复：统一为一套 controlled 数字（带 error bars），8-seed 放 appendix robustness。\n\n**[Warning] W5: Cluster bootstrap K=11 缺 formal caveat**\n- CI [73.3%, 100%] 基于 K=11 clusters（远低于 K≥40 推荐值）\n- 上界 100% 是 small-K artifact\n- 修复：引用 Cameron, Gelbach & Miller (2008)，加 caveat statement。\n\n**[Warning] W6: McNemar test 输入未与 routing labels 区分**\n- MATH §4.3 并列报告 McNemar p=0.81 和 routing labels (107/95)，但二者定义不同\n- McNemar 应用于 binary correct/incorrect discordant pairs (≈103/99)，routing labels 包含额外 score-comparison discordances\n- 修复：加一句澄清 McNemar input definition。\n\n### Nice-to-Fix\n\n**[Minor] W7: §4.1 和 §4.5 段落过密** — 加 \\paragraph{} 标记拆分\n**[Minor] W8: Abstract 中 78.9% vs DAF=90.4% 区分不直观** — 加半句因果链\n**[Minor] W9: Mann-Whitney vs Wilcoxon signed-rank** — 明确 reasoning depth ablation 是否 paired design\n**[Minor] W10: 引用 37 篇略低** — R1 认为可接受，R2 建议补 2-3 篇。非 blocking。\n\n---\n\n## Reviewer Consensus\n\n所有关键发现均已达成共识：\n\n- **[AGREE]** Partial correlation 必须删除（structural collinearity, undefined）\n- **[AGREE]** Em-dash 和 \\nolinenumbers 必须修复\n- **[AGREE]** Cluster bootstrap 需 citation + caveat\n- **[AGREE]** Capacity dual-reporting 需统一\n- **[AGREE]** R10 issues 绝大部分已有效修复\n- **[AGREE]** 框架设计 sound，DAF decomposition 数学正确\n- **[AGREE]** Negative result (router failure) 有社区价值\n\n---\n\n## Reviewer Divergence\n\n**McNemar p=0.81 (轻微分歧, 已解决)**：\n- R1: p=0.81 与 routing labels 107/95 不一致 (应得 p≈0.40)\n- R2: [REBUT] 重构表明 McNemar 基于 binary discordant pairs (≈103/99 with continuity correction → p≈0.83)，与报告吻合\n- 共识：p=0.81 大概率正确，但需澄清 definition difference\n\n**引用数量 (轻微分歧)**：\n- R2: 37 篇偏低 (EMNLP 典型 40-60)，建议补 ToolBench, Safe RLHF\n- R1: [REBUT] 37 可接受，覆盖度比数量重要，ToolBench/Safe RLHF 研究问题与本文不同\n- 共识：2-3 篇额外引用是 nice-to-have，非 blocking\n\n**Excitement (评分差异)**：\n- R1: 3.5/5 (框架 reuse potential 高，Findings bar 合适)\n- R2: 2.5/5 (scope 窄，core insight 不 surprising)\n- 差异主要在 Findings track 标准理解——R1 认为 \"novel diagnostic framework + informative case study\" 达标，R2 认为仍偏 niche\n\n---\n\n## Questions（需作者回应）\n\n1. Partial correlation 的具体计算代码？是否因 floating-point tolerance 返回 r=0.02 而非 NaN？\n2. MATH McNemar exact discordant cell counts (b, c) 是多少？\n3. 0.6B/4B controlled replication 是否也有 std？为何 main text 不报告？\n4. `find-non-living-thing` 两批数据（n=40）是否存在 batch effect？\n5. 排除的 19 task types 延长 step budget 后是否可能产生 routing signal？\n6. \"Dominant\" 的判据是什么——DAF>50%? label fraction>50%? 两者 AND?\n\n---\n\n## Missing References\n\n- ToolBench (Qin et al., 2024) — tool-use benchmark [R2 建议, R1 认为非必须]\n- Safe RLHF (Dai et al., 2024) — LLM-era safe alignment [R2 建议, R1 认为研究问题不同]\n- Cameron, Gelbach & Miller (2008) — cluster bootstrap minimum K [R1 和 R2 共识]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）\n\n---\n\n## Overall Assessment\n\n**Borderline Accept (Findings)**\n\n框架设计 sound，case study 分析详尽且诚实，claim calibration 优秀，R10 issues 修复到位。核心 critical issue 仅 1 条（partial correlation 无效统计量），且修复方案明确（删除数值，保留代数论证，不影响主要结论）。Em-dash 和 \\nolinenumbers 是 mechanical fixes。\n\n主要限制：单环境 evidence (ScienceWorld 11/30 tasks)、excitement 中等 (analytical/negative result)、scope 窄。但对 EMNLP Findings track（\"solid work with niche interest\"），这些限制可接受。\n\n修复 W1-W3 后，论文达到 Findings accept 水平。\n\n**评分**: weak accept (Findings)\n**置信度**: 4/5\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 删除 \"partial r=0.02, p=0.91\" 引用，替换为 collinearity 论证\n- 78.9% 和 DAF=90.4% 之间加半句区分 (penalty-independent → penalty-dependent)\n- \"Algorithm~1\" 改为 \"our labeling procedure\" 或删除\n\n### Introduction\n- §1 para 5 (contributions): 无需修改，claim 已 well-calibrated\n- 删除 partial correlation 数值（line 25 area）\n\n### Method\n- §3.4 DAF: 无实质问题，mathematical caveat 已充分\n- §3.5 SCI: sound\n\n### Experiments\n- §4.1: 删除 partial correlation r=0.02 数值；拆分长段落\n- §4.3 MATH: 加 McNemar input clarification sentence\n- §4.5 Router: 统一 capacity scaling reporting；拆分长段落\n\n### Related Work\n- 可选补 2-3 refs (ToolBench, Safe RLHF, Cameron et al. for cluster bootstrap)\n- 当前覆盖五个主题，结构清晰\n\n### Discussion\n- 无实质问题\n\n### Conclusion\n- 删除 partial correlation 数值引用\n\n### Format\n- 删除 \\nolinenumbers\n- 全局清零 em-dash (---)\n\n---\n\n## 优先级排序（投稿前 action list）\n\n| 优先级 | Item | 预计工作量 |\n|--------|------|-----------|\n| P0 (blocking) | 删除 partial correlation r=0.02 (4 处) + 替换为代数论证 | 15 min |\n| P0 (blocking) | 删除 \\nolinenumbers | 1 min |\n| P0 (blocking) | 全局清除 em-dash (20+ 处) | 30 min |\n| P1 (should-fix) | 统一 capacity scaling reporting + error bars | 20 min |\n| P1 (should-fix) | Cluster bootstrap citation + caveat | 5 min |\n| P1 (should-fix) | McNemar clarification sentence | 5 min |\n| P2 (nice-to-fix) | 段落拆分 (§4.1, §4.5) | 10 min |\n| P2 (nice-to-fix) | Abstract 78.9%/DAF 区分半句 | 5 min |\n| P2 (nice-to-fix) | Mann-Whitney/Wilcoxon 澄清 | 5 min |\n| P2 (nice-to-fix) | 补 2-3 references | 10 min |",
  "project": "simgate-modular-routing",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak accept"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 11 审稿报告 — simgate-modular-routing\n\n**论文**: Death Avoidance as a Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**目标**: EMNLP 2026 Findings (via ARR May 2026)\n**Reviewers**: R1 (方法严谨性+统计推断), R2 (新颖性+写作+Related Work)\n\n---\n\n## Summary\n\n论文提出 episode-level counterfactual 框架（Algorithm 1 + DAF + SCI）用于诊断 modular LLM agent 的 routing signal 来源。以 ScienceWorld 为 case study（11/30 task types, N=245, Qwen2.5-7B-Instruct），发现 78.9% 的 non-tie routing labels 由 death asymmetry 驱动，DAF=90.4%@P=100。跨环境（MATH confirmed null, ALFWorld information asymmetry）和跨模型（Llama pilot）分析展示框架 diagnostic flexibility。Router training 作为 informative negative 支持 analytical framework 优于 brute-force learned routing 的结论。\n\n---\n\n## Strengths\n\n1. **R10 问题修复优秀**：前轮 12 条 open issues 中，10 条已完全修复（R10-C2/C3/C4/W1/W2/W5/W6/W7/m1/m2），1 条部分修复（R10-W3 引用），1 条未修复（R10-C1 partial correlation, 升级为 R11-C1）。Claim calibration 全文一致。\n\n2. **方法论透明度**：DAF 的 mathematical nature（随 P 单调递增）被显式承认为 \"mathematical consequence, not empirical finding\"；r=0.97 被定位为 \"internal consistency check\"；data scaling 区分 augmentation vs real-data；cross-model 标注 \"preliminary pilot\"。\n\n3. **框架设计合理**：Algorithm 1 逻辑无歧义（四个 mutually exclusive cases），DAF decomposition 数学正确，SCI 有效补充 \"systematic vs outlier-driven\" 问题。Dual-metric（penalty-independent 78.9% + penalty-dependent DAF）设计使结论不依赖单一假设。\n\n4. **统计实践规范**：Episode-level bootstrap (B=10,000), cluster bootstrap sensitivity, McNemar test, LOO robustness, penalty sensitivity, seed robustness（8 seeds）, capacity scaling controlled replication。\n\n5. **Negative result 有价值**：Router diagnostic 不是 \"failure report\" 而是 \"framework predicts and explains why routing fails\"——对 agent routing 社区有实际指导意义。\n\n---\n\n## Weaknesses\n\n### Must-Fix (投稿前)\n\n**[Critical] W1: Partial correlation (r=0.02, p=0.91, df=27) 数学上 undefined**\n- 位置：Abstract, Introduction, §4.1, Conclusion（4 处引用）\n- 问题：P=100 对所有 task types 为常数 → δ·P = 100δ → r(δ, δ·P) = 1.0 → partial correlation 分母为零 → undefined。扩展到 n=30 不解决 structural collinearity。r=0.02 是 floating-point artifact。\n- 影响：论文核心论证（r=0.97 is structural）的支撑证据无效。概念论证正确但数值报告有误，损害全文统计可信度。\n- 修复：删除 r=0.02/p=0.91/df=27 所有出现，替换为代数论证：\"When P is constant across tasks, δ·P is perfectly collinear with δ; this collinearity proves r=0.97 is a mathematical consequence of death dominance.\" 或改用 corr(Δ_nd, δ) 作为替代 well-defined statistic。\n\n**[Warning] W2: Em-dash (---) 泛滥，20+ 处 AI 写作标志**\n- 位置：全文正文（Abstract 到 Conclusion）\n- 影响：不影响 soundness 但触发 reviewer 对 AI-generated content 的警觉\n- 修复：全局 `grep \"---\" *.tex`，替换为逗号/括号/拆句。保留 en-dash (--) 数字范围和专有名词。\n\n**[Warning] W3: \\nolinenumbers 违反 ACL ARR review 格式**\n- 位置：main.tex line 23\n- 影响：Desk reject 风险\n- 修复：删除 `\\nolinenumbers`\n\n### Should-Fix\n\n**[Warning] W4: Capacity scaling dual-reporting**\n- Main text (4-seed controlled): 0.6B=50.7%, 1.7B=43.1±1.0%, 4B=59.0%\n- Appendix Table 8 (8-seed original): 1.7B=47.1±2.2%\n- 两套 1.7B 数字共存造成混淆。0.6B/4B 在 main text 缺 error bars。\n- 修复：统一为一套 controlled 数字（带 error bars），8-seed 放 appendix robustness。\n\n**[Warning] W5: Cluster bootstrap K=11 缺 formal caveat**\n- CI [73.3%, 100%] 基于 K=11 clusters（远低于 K≥40 推荐值）\n- 上界 100% 是 small-K artifact\n- 修复：引用 Cameron, Gelbach & Miller (2008)，加 caveat statement。\n\n**[Warning] W6: McNemar test 输入未与 routing labels 区分**\n- MATH §4.3 并列报告 McNemar p=0.81 和 routing labels (107/95)，但二者定义不同\n- McNemar 应用于 binary correct/incorrect discordant pairs (≈103/99)，routing labels 包含额外 score-comparison discordances\n- 修复：加一句澄清 McNemar input definition。\n\n### Nice-to-Fix\n\n**[Minor] W7: §4.1 和 §4.5 段落过密** — 加 \\paragraph{} 标记拆分\n**[Minor] W8: Abstract 中 78.9% vs DAF=90.4% 区分不直观** — 加半句因果链\n**[Minor] W9: Mann-Whitney vs Wilcoxon signed-rank** — 明确 reasoning depth ablation 是否 paired design\n**[Minor] W10: 引用 37 篇略低** — R1 认为可接受，R2 建议补 2-3 篇。非 blocking。\n\n---\n\n## Reviewer Consensus\n\n所有关键发现均已达成共识：\n\n- **[AGREE]** Partial correlation 必须删除（structural collinearity, undefined）\n- **[AGREE]** Em-dash 和 \\nolinenumbers 必须修复\n- **[AGREE]** Cluster bootstrap 需 citation + caveat\n- **[AGREE]** Capacity dual-reporting 需统一\n- **[AGREE]** R10 issues 绝大部分已有效修复\n- **[AGREE]** 框架设计 sound，DAF decomposition 数学正确\n- **[AGREE]** Negative result (router failure) 有社区价值\n\n---\n\n## Reviewer Divergence\n\n**McNemar p=0.81 (轻微分歧, 已解决)**：\n- R1: p=0.81 与 routing labels 107/95 不一致 (应得 p≈0.40)\n- R2: [REBUT] 重构表明 McNemar 基于 binary discordant pairs (≈103/99 with continuity correction → p≈0.83)，与报告吻合\n- 共识：p=0.81 大概率正确，但需澄清 definition difference\n\n**引用数量 (轻微分歧)**：\n- R2: 37 篇偏低 (EMNLP 典型 40-60)，建议补 ToolBench, Safe RLHF\n- R1: [REBUT] 37 可接受，覆盖度比数量重要，ToolBench/Safe RLHF 研究问题与本文不同\n- 共识：2-3 篇额外引用是 nice-to-have，非 blocking\n\n**Excitement (评分差异)**：\n- R1: 3.5/5 (框架 reuse potential 高，Findings bar 合适)\n- R2: 2.5/5 (scope 窄，core insight 不 surprising)\n- 差异主要在 Findings track 标准理解——R1 认为 \"novel diagnostic framework + informative case study\" 达标，R2 认为仍偏 niche\n\n---\n\n## Questions（需作者回应）\n\n1. Partial correlation 的具体计算代码？是否因 floating-point tolerance 返回 r=0.02 而非 NaN？\n2. MATH McNemar exact discordant cell counts (b, c) 是多少？\n3. 0.6B/4B controlled replication 是否也有 std？为何 main text 不报告？\n4. `find-non-living-thing` 两批数据（n=40）是否存在 batch effect？\n5. 排除的 19 task types 延长 step budget 后是否可能产生 routing signal？\n6. \"Dominant\" 的判据是什么——DAF>50%? label fraction>50%? 两者 AND?\n\n---\n\n## Missing References\n\n- ToolBench (Qin et al., 2024) — tool-use benchmark [R2 建议, R1 认为非必须]\n- Safe RLHF (Dai et al., 2024) — LLM-era safe alignment [R2 建议, R1 认为研究问题不同]\n- Cameron, Gelbach & Miller (2008) — cluster bootstrap minimum K [R1 和 R2 共识]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）\n\n---\n\n## Overall Assessment\n\n**Borderline Accept (Findings)**\n\n框架设计 sound，case study 分析详尽且诚实，claim calibration 优秀，R10 issues 修复到位。核心 critical issue 仅 1 条（partial correlation 无效统计量），且修复方案明确（删除数值，保留代数论证，不影响主要结论）。Em-dash 和 \\nolinenumbers 是 mechanical fixes。\n\n主要限制：单环境 evidence (ScienceWorld 11/30 tasks)、excitement 中等 (analytical/negative result)、scope 窄。但对 EMNLP Findings track（\"solid work with niche interest\"），这些限制可接受。\n\n修复 W1-W3 后，论文达到 Findings accept 水平。\n\n**评分**: weak accept (Findings)\n**置信度**: 4/5\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 删除 \"partial r=0.02, p=0.91\" 引用，替换为 collinearity 论证\n- 78.9% 和 DAF=90.4% 之间加半句区分 (penalty-independent → penalty-dependent)\n- \"Algorithm~1\" 改为 \"our labeling procedure\" 或删除\n\n### Introduction\n- §1 para 5 (contributions): 无需修改，claim 已 well-calibrated\n- 删除 partial correlation 数值（line 25 area）\n\n### Method\n- §3.4 DAF: 无实质问题，mathematical caveat 已充分\n- §3.5 SCI: sound\n\n### Experiments\n- §4.1: 删除 partial correlation r=0.02 数值；拆分长段落\n- §4.3 MATH: 加 McNemar input clarification sentence\n- §4.5 Router: 统一 capacity scaling reporting；拆分长段落\n\n### Related Work\n- 可选补 2-3 refs (ToolBench, Safe RLHF, Cameron et al. for cluster bootstrap)\n- 当前覆盖五个主题，结构清晰\n\n### Discussion\n- 无实质问题\n\n### Conclusion\n- 删除 partial correlation 数值引用\n\n### Format\n- 删除 \\nolinenumbers\n- 全局清零 em-dash (---)\n\n---\n\n## 优先级排序（投稿前 action list）\n\n| 优先级 | Item | 预计工作量 |\n|--------|------|-----------|\n| P0 (blocking) | 删除 partial correlation r=0.02 (4 处) + 替换为代数论证 | 15 min |\n| P0 (blocking) | 删除 \\nolinenumbers | 1 min |\n| P0 (blocking) | 全局清除 em-dash (20+ 处) | 30 min |\n| P1 (should-fix) | 统一 capacity scaling reporting + error bars | 20 min |\n| P1 (should-fix) | Cluster bootstrap citation + caveat | 5 min |\n| P1 (should-fix) | McNemar clarification sentence | 5 min |\n| P2 (nice-to-fix) | 段落拆分 (§4.1, §4.5) | 10 min |\n| P2 (nice-to-fix) | Abstract 78.9%/DAF 区分半句 | 5 min |\n| P2 (nice-to-fix) | Mann-Whitney/Wilcoxon 澄清 | 5 min |\n| P2 (nice-to-fix) | 补 2-3 references | 10 min |",
    "project": "simgate-modular-routing",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak accept"
  }
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-17T06:48:14.033003+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Assistant

_source line 882 · 2026-05-17T06:48:23.215531+00:00_

---

**Round 11 审稿完成。**

报告已投递至 Research Director。核心结论：

- **评分**: weak accept (Findings borderline)
- **Critical issue (1条)**: Partial correlation r=0.02 数学上 undefined（P 常数时完美共线），必须删除数值替换为代数论证
- **Must-fix (2条)**: em-dash 20+ 处清零 + `\nolinenumbers` 删除
- **Should-fix (3条)**: capacity scaling 统一报告、cluster bootstrap citation、McNemar 澄清

R10 遗留 12 条问题中 10 条已完全修复。当前版本的所有问题均为 fixable（无实质性内容改动），P0 修复预计 45 分钟。修复后论文达到 EMNLP Findings accept 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 86

## Round 86

2 recorded events


### User

_source line 883 · 2026-05-17T06:48:25.735500+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **AGREE（5条）**：W1（partial correlation undefined）、W2（capacity scaling 混淆）、W3（cluster bootstrap K=11）、W6（\nolinenumbers）、W7（Mann-Whitney vs paired）
- **REBUT（2条）**：W4（McNemar p=0.81 经重构验证大概率正确，但需澄清 routing labels ≠ discordant pairs）、W5（当前 framing 已足够保守，"11 of 30" 在所有关键位置出现）

核心判断：R1-W1 是唯一需要修复的 substantive statistical error（删除 r=0.02 数值即可，代数论证本身完备）。不改变 Findings borderline accept 的整体评价。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 884 · 2026-05-17T06:48:35.647341+00:00_

Round 11 审稿已完成。报告已投递 Research Director。

**最终结论：weak accept (Findings)**

核心修复清单（投稿前）：
1. **P0** — 删除 partial correlation r=0.02/p=0.91/df=27（4处），替换为代数 collinearity 论证
2. **P0** — 删除 `\nolinenumbers`
3. **P0** — 全局清除 em-dash `---`（20+ 处）

这三项完成后论文达到 Findings accept 水平。详细 action list 已在报告中按优先级列出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 87

## Round 87

88 recorded events


### User

_source line 885 · 2026-05-17T14:21:34.140903+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/
- 目标 venue: EMNLP 2026 Findings
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-17T14:21:42.081819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-17T14:21:42.233319+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-17T14:21:49.161590+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 889 · 2026-05-17T14:21:49.212392+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-17T14:21:54.032364+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-17T14:21:54.032860+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-17T14:21:57.279622+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-17T14:21:57.280071+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-17T14:22:01.949147+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-17T14:22:03.405489+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (100 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| reflexion-internal-baseline-b | Reflexion baseline Part 2 (tasks 7-11): 与 part 1 并行收集，验证 reflexion 对 death rate 的影响 | — | — | — |\n| reflexion-internal-baseline | Reflexion 通过自我纠错降低 internal modality 的 death rate；如果 death rate 降至 <20%（接近 det 的 16.3%），则 death dominance 不再成立 | — | — | — |\n| backbone-scaling-70b | 72B model 的 death rate 显著低于 7B (42.9%)，但 DAF 可能仍 dominant 因为 deterministic modality 的 death rate 也会降低 | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **death-risk-routing-analysis** (negative): 基于 task-type death risk 的简单 threshold routing 能否优于 always-det；如果能，说明 analytical framework 不只诊断问题还指向解决方案 ← 基于 plan-005-routing-patterns\n- **math-extension-n800** (success): MATH Level 4-5 在 N=800 下 internal > code-interpreter 效应达到统计显著（p<0.05），确认无 catastrophic failure 环境中 deterministic modality 无优势 ← 基于 math-negative-contrast\n- **plan-008-v4-4b-e2e** (negative): 4B router (episode-level 59%) 在 end-to-end deployment 中能否超越 always-det baseline (-9.47 mean score)。若超过：larger capacity translates to marginal deployment gain at disproportionate cost。若未超过：进一步强化 analytical framework > learned routing at all tested sc
…[truncated 1426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-17T14:22:03.556475+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-17T14:22:04.008917+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/SETUP_NOTES.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/gen_fig1.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/fig1_daf_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/gen_signal_reversal.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/signal_reversal.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/gen_pipeline.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/pipeline_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p1.png
/home/
…[truncated 2624 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 898 · 2026-05-17T14:22:04.109856+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-17T14:22:09.380789+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Call for Papers: NLP for Science Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/nlp-science"}]

Based on the search results, I found information about EMNLP 2026, though the main conference papers call was not directly returned. Here's what I found:

## EMNLP 2026 Workshop Information

The MINT
…[truncated 1131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 5270
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-17T14:22:16.538129+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference submission guidelines ARR commitment deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference submission guidelines ARR commitment deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 901 · 2026-05-17T14:22:17.391855+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit template anonymous"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit template anonymous"
  }
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-17T14:22:17.894317+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-17T14:22:25.424177+00:00_

Web search results for query: "EMNLP 2026 main conference submission guidelines ARR commitment deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Update EMNLP System Demonstrations Track with 2026 conference data · huggingface/ai-deadlines at 6a94f2c","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/6a94f2c940ba976564775b34f6b224b0f9ad638d"}]

Now let me search for more specific information about page limits and ARR submission requirements:

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Confere
…[truncated 2266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 8886
}
```

</details>

---


### Tool result

_source line 904 · 2026-05-17T14:22:28.937549+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit template anonymous"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

Based on the search results for ACL Rolling Review 2026 submission guidelines, here's what I found regarding the key topics you asked about:

## Page Limit

Short papers are limited to 4 content pages maximum, while long papers are limited to 8 content pages maximum. Sections on ethical considerations and limitations do
…[truncated 1133 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 11545
}
```

</details>

---


### Tool result

_source line 905 · 2026-05-17T14:22:28.938131+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 11043
}
```

</details>

---


### Tool call

_source line 906 · 2026-05-17T14:22:33.456397+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 907 · 2026-05-17T14:22:33.858684+00:00_

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
18	\title{Death Avoidance as a Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
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
35	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct); generalization requires further validation. The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface additional signal. Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}; more sophisticated strategies (e.g., Reflexion~\citep{reflexion-2023} or Tree-of-Thought backtracking~\citep{tot-2023}) may reduce internal death rates and lower DAF. Episode-level labels may assign suboptimal routing to individual steps, particularly those preceding death events, and training on pure-strategy trajectories introduces distribution shift at deployment~\citep{dagger-2011}. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct replication (7 task types, $N{=}70$; Appendix~\ref{app:cross-model}) confirms direction-consistent death patterns for all ta
…[truncated 24945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 908 · 2026-05-17T14:22:33.859157+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-17T14:22:34.160568+00:00_

1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet no systematic methodology exists for diagnosing \emph{what} drives routing decisions. We introduce an episode-level counterfactual framework using penalty-independent and penalty-dependent decomposition that isolates death-avoidance from non-death routing signal, requiring only paired episode outcomes with binary success/failure indicators. Applied to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), the framework reveals that \textbf{78.9\% of non-tie routing labels} (75 of 95) arise from death asymmetry (penalty-independent); the penalty-weighted DAF $= 90.4\%$ at $P{=}100$. The per-task $r{=}0.97$ follows algebraically from death dominance when $P$ is constant. A router trained on these labels reaches only $59.0\%$ episode-level balanced accuracy at 4B parameters, failing to outperform always-deterministic. Cross-environment contrasts confirm framework predictions: on MATH ($N{=}795$), no routing signal without catastrophic failure ($p = 0.81$); on ALFWorld ($N{=}135$), the framework identifies information asymmetry as an alternative mechanism. A Llama-3.1-8B-Instruct pilot confirms directional consistency across model families. We predict that stronger backbones will lower death-avoidance fractions as capability reduces catastrophic failure rates.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-17T14:22:34.160911+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-17T14:22:34.211457+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}, a text-based science simulation with 30 task types, faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	The shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.
10	But this assumption has never been systematically verified: \emph{what actually drives the value of routing decisions in interactive environments?}
11	If routing value traces to a single failure mode, practitioners can replace complex learned routers with simpler safety-aware policies at lower computational cost and deployment risk.
12	
13	We propose a \emph{formal diagnostic framework} for answeri
…[truncated 4686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-17T14:22:39.331413+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 913 · 2026-05-17T14:22:39.783915+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically across the environment (\S\ref{sec:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment $\mathcal{E}$ with state space $\mathcal{S}$, observation space $\mathcal{O}$, and action space $\mathcal{A}$. An agent follows a policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ that maps observation histories to actions. At each step $t$, the agent receives observation $o_t$, selects action $a_t = \pi(o_1, \ldots, o_t)$, and the environment transitions to state $s_{t+1}$.
10	
11	We define a modality set $\mathcal{M} = \{{\tt int}, {\tt det}\}$ governing how the agent processes state transitions:
12	\begin{itemize}
13	    \item \textbf{Internal} ($m = {\tt int}$): The agent uses its own generation to predict intermediate observations. The LLM interleaves chain-of-thought reasoning with environment actions following the ReAct paradigm \cite{react-2023}, but prediction errors compound across steps.
14	    \item \textbf{Deterministic} ($m = {\tt det}$): The agent receives ground-truth observations from the environment simulator at each step, equivalent to access to a perfect dynamics model. Action selection remains with the LLM; only the state-transition prediction is replaced.
15	\end{itemize}
16	
17	\noindent We restrict $\mathcal{M}$
…[truncated 8629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 914 · 2026-05-17T14:22:39.784413+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 915 · 2026-05-17T14:22:40.749933+00:00_

1	\section{Experiments}
2	
3	\subsection{Death Avoidance Decomposition}
4	\label{sec:death-decomp}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/fig1_daf_scatter.pdf}
9	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types.}
10	\label{fig:decomposition}
11	\end{figure}
12	
13	Across 245 episodes, $\Delta_{\text{full}} = +29.60$; excluding death episodes, $\Delta_{\text{nd}} = +2.84$, yielding DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$; at default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\% (75 of 95 non-tie labels). Of these 75, 54 (72.0\%) reduce to ties when the death penalty is removed entirely: in those episodes, both modalities score zero without death, so the only reason one strategy outscored the other was avoiding the $-100$ penalty. Death avoidance is not merely the dominant but often the \emph{sole} discriminating signal between modalities. The remaining 21 death-asymmetry labels involve episodes where the surviving strategy also earned positive score, but the death penalty still accounts for the majority of the score gap.
14	
15	\paragraph{Per-task correlation structure.}
16	The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$), consistent with the internal strategy's reliance on self-generated observations that compound prediction errors across steps. Per-task, death rate differential correlates with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}). Since $P$ is constant across all task types, $\Delta_{\text{full}} = P \cdot \delta + \Delta_{\text{nd}}$ makes $\Delta_{\text{full}}$ a linear function of $\delta$ with residual $\Delta_{\text{nd}}$; when DAF $\rightarrow 1$, this residual vanishes and $r \rightarrow 1$ by construction. The near-perfect correlation is therefore a mathematical cons
…[truncated 10186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 965
}
```

</details>

---


### Tool call

_source line 916 · 2026-05-17T14:22:40.750480+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 917 · 2026-05-17T14:22:41.252408+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}.
5	Toolformer \cite{toolformer-2023} teaches LLMs to insert API calls via self-supervised loss filtering; ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask; ReTool \cite{retool-2025} applies RL to discover when code execution is preferable to chain-of-thought.
6	These focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Recent concurrent work sharpens this question: \citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect, \citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \citet{tool-use-tax-2026} quantify a ``tool-use tax,'' and \citet{to-call-or-not-2026} propose a necessity--utility--affordability framework. Our decomposition provides environment-grounded evidence: in ScienceWorld, $90.4\%$ of routing signal at $P{=}100$ traces to catastrophic-failure prevention.
8	
9	\paragraph{Adaptive Computation and Routing.}
10	CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing.
11	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
12	These optimize \emph{how} to route; we reveal \emph{why} routing helps: in interactive environments, the dominant signal is catastrophic-failure avoidance.
13	
14	\paragraph{Counterfactual Evaluation in RL.}
15	Prior work generates counterfactual explanations for RL agents by perturbing individual 
…[truncated 1516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 918 · 2026-05-17T14:22:41.252780+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 919 · 2026-05-17T14:22:41.403527+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Cross-environment evidence.}
5	The framework generates testable predictions beyond ScienceWorld. The MATH null ($p = 0.81$) validates the prediction that removing catastrophic failure eliminates routing signal; ALFWorld identifies information asymmetry as an alternative mechanism (\S\ref{sec:cross-env}). True quantitative DAF replication requires a second catastrophic-failure environment (e.g., NetHack~\citep{nethack-2020}, Crafter~\citep{crafter-2022}).
6	
7	\paragraph{Penalty sensitivity and correlation structure.}
8	The $r = 0.97$ correlation is specific to catastrophic death ($P{=}100$); defining failure as any non-positive score yields $r = -0.13$ ($p = 0.70$). As shown in \S\ref{sec:death-decomp}, this correlation follows algebraically from death dominance when $P$ is constant; larger models with lower death rates would reduce DAF. This prediction assumes models above a minimum capability threshold; preliminary evidence (Qwen2.5-0.5B, $N{=}15$) suggests very weak models may exhibit low death rates not from avoidance ability but from inability to reach dangerous states.
9	
10	\paragraph{Implications for router design.}
11	Death avoidance dominance (78.9\% of non-tie labels, DAF $= 90.4\%$ at $P{=}100$) reframes modality routing as a \emph{safety} problem, closer to a conservative default policy than to cost-quality optimization~\citep{garcia2015comprehensive, cogrouter-2026}. The underlying failure mechanism is state hallucination: the internal strategy predicts that an action succeeded when the environment state did not change, and these prediction errors compound across steps until they trigger death. The deterministic strategy eliminates these compounding observation errors, while action-selection errors (16.3\% deterministic death rate) remain comparatively rare. The 86:9 label imbalance explains why always-deterministic is a strong baseline; 4B parameters for $+9$\,pp router improvement is con
…[truncated 639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 920 · 2026-05-17T14:22:41.404027+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 921 · 2026-05-17T14:22:41.454578+00:00_

1	\section{Conclusion}
2	
3	We presented a formal diagnostic framework for decomposing routing signal in modular LLM agents via episode-level counterfactual analysis with dual metrics (penalty-independent label fraction and penalty-dependent DAF). Applied to 245 ScienceWorld episodes (11 of 30 task types, Qwen2.5-7B-Instruct), death asymmetry accounts for 78.9\% of non-tie routing labels; DAF $= 90.4\%$ at $P{=}100$ (95\% CI: $[81.6\%, 98.8\%]$). Cross-domain contrasts confirm framework predictions: MATH shows no routing signal without catastrophic failure; ALFWorld reveals information asymmetry as an alternative mechanism; a Llama pilot confirms cross-model consistency. Open directions include replication in catastrophic-failure environments (e.g., NetHack~\citep{nethack-2020}, Crafter~\citep{crafter-2022}) and stronger backbones, which the framework predicts will lower DAF.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 922 · 2026-05-17T14:22:48.733502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 923 · 2026-05-17T14:22:49.587331+00:00_

1	@inproceedings{scienceworld-2022,
2	  title={ScienceWorld: Is Your Agent Smarter Than a 5th Grader?},
3	  author={Wang, Ruoyao and Jansen, Peter and C\^{o}t\'{e}, Marc-Alexandre and Ammanabrolu, Prithviraj},
4	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
5	  year={2022}
6	}
7	
8	@inproceedings{react-2023,
9	  title={ReAct: Synergizing Reasoning and Acting in Language Models},
10	  author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
11	  booktitle={International Conference on Learning Representations (ICLR)},
12	  year={2023}
13	}
14	
15	@inproceedings{toolformer-2023,
16	  title={Toolformer: Language Models Can Teach Themselves to Use Tools},
17	  author={Schick, Timo and Dwivedi-Yu, Jane and Dess\`{i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
18	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
19	  year={2023}
20	}
21	
22	@article{art-2023,
23	  title={ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models},
24	  author={Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio},
25	  journal={arXiv preprint arXiv:2303.09014},
26	  year={2023}
27	}
28	
29	@inproceedings{chameleon-2023,
30	  title={Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models},
31	  author={Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng},
32	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
33	  year={2023}
34	}
35	
36	@article{retool-2025,
37	  title={ReTool: Reinforcement Learning for Strategic Tool Use in LLMs},
38	  author={Feng, Jiazhan and others},
39	  journal={arXiv preprint arXiv:2504.11536},
40	  year={2025}
41	}
…[truncated 9657 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 924 · 2026-05-17T14:22:49.587914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-17T14:22:50.793185+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 1205
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-17T14:22:50.994345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 927 · 2026-05-17T14:22:51.648209+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 928 · 2026-05-17T14:22:51.698900+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_framing.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "paper_framing.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 929 · 2026-05-17T14:22:52.000610+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\", \"content\": \"# Paper Framing — simgate-modular-routing\\n\\n## Target Venue\\n- **EMNLP 2026 Main Conference — Long Paper (8 pages + references)**\\n- Deadline: ARR May 25, 2026 (10 days remaining)\\n- D050: Upgraded from short paper (4p, Findings) per user directive\\n\\n## Core Insight\\n\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 97.4% ties in sparse-reward settings) and discover that **death avoidance accounts for ~90% of routing signal** on ScienceWorld (Δ_full=+29.60 [A], Δ_nd=+2.84 [A], DAF=90.41% [A]; Pearson r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). Non-death performance difference is small but non-negligible (Δ_nd/Δ_full=9.6% [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\n\\n## Core Claims (3 claims for long paper)\\n\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (Δ_full=+29.60 [A]), with **death avoidance as the dominant mechanism** (90.41% of the performance gap [A], measured by Δ decomposition; plan-012-full, 11 tasks / 245 eps [A]). Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 (out of 245 episodes) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Non-death score de
…[truncated 1335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 930 · 2026-05-17T14:22:57.660147+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 931 · 2026-05-17T14:22:58.263904+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 932 · 2026-05-17T14:22:58.314611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 933 · 2026-05-17T14:22:58.866978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 934 · 2026-05-17T14:22:59.370880+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 935 · 2026-05-17T14:22:59.371340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 936 · 2026-05-17T14:22:59.774057+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 937 · 2026-05-17T14:22:59.874913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 938 · 2026-05-17T14:23:00.227408+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-17T14:23:00.430229+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 555
}
```

</details>

---


### Tool call

_source line 940 · 2026-05-17T14:23:37.937951+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_local_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_local_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 941 · 2026-05-17T14:23:37.988657+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 942 · 2026-05-17T14:23:42.774421+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 943 · 2026-05-17T14:23:42.774839+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 104\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-determinis
…[truncated 1447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 944 · 2026-05-17T14:23:44.331087+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 945 · 2026-05-17T14:23:44.582605+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 946 · 2026-05-17T14:23:44.683374+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 947 · 2026-05-17T14:23:44.734134+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-17T14:23:47.595485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-17T14:23:47.997635+00:00_

1	- id: "R11-C1"
2	  summary: "Partial correlation (r=0.02, p=0.91, df=27) mathematically undefined — perfect collinearity when P is constant"
3	  category: method
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 10
7	  last_seen_round: 11
8	  mentions:
9	    - round: 10
10	      reviewers: [1, 2]
11	      note: "R10-C1: df=27 error. Paper claimed n=30 resolves it."
12	    - round: 11
13	      reviewers: [1, 2]
14	      note: "Consensus. Problem NOT resolved by expanding to n=30. When P=100 is constant across all tasks, δ·P = 100δ → r(δ, δ·P)=1.0 → partial correlation denominator=0 → undefined. Software returning r=0.02 is floating-point artifact."
15	  action_items:
16	    - round: 11
17	      action: "Delete all instances of partial correlation r=0.02, p=0.91, df=27. Replace with algebraic collinearity argument."
18	      assigned_to: paper_agent
19	      status: done
20	  resolution: "All 5 instances deleted. Replaced with algebraic argument: P constant → δ·P collinear with δ → r=0.97 is mathematical consequence."
21	  resolution_round: 11
22	
23	- id: "R11-W1"
24	  summary: "Em-dash (---) 泛滥 — 20+ instances, AI writing signature"
25	  category: writing
26	  severity: warning
27	  status: resolved
28	  first_raised_round: 11
29	  last_seen_round: 11
30	  mentions:
31	    - round: 11
32	      reviewers: [1, 2]
33	      note: "Consensus. LaTeX --- (three hyphens) rendering as em-dash. ~20 instances across 6 tex files."
34	  action_items:
35	    - round: 11
36	      action: "grep '---' *.tex and replace all explanatory em-dashes. Preserve en-dashes (--) in number ranges."
37	      assigned_to: paper_agent
38	      status: done
39	  resolution: "All ~20 explanatory em-dashes replaced with commas/parentheses/sentence splits. Table placeholders preserved."
40	  resolution_round: 11
41	
42	- id: "R11-W2"
43	  summary: "\\nolinenumbers violates ACL ARR review submission format — desk reject risk"
44	  category: format
45	  severity: warning
46	  status
…[truncated 9347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 950 · 2026-05-17T14:23:48.198905+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 951 · 2026-05-17T14:23:48.199439+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_12.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-17T14:23:58.643796+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-17T14:23:58.695180+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-17T14:24:01.306907+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.{yaml,yml,json,toml}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.{yaml,yml,json,toml}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12"
  }
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-17T14:24:01.407728+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-17T14:24:04.071361+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/",
  "description": "List workspace root directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/",
    "description": "List workspace root directory"
  }
}
```

</details>

---


### Tool result

_source line 957 · 2026-05-17T14:24:04.222468+00:00_

AGENTS.md
config
global
idea_generator
projects
skills
state
workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 958 · 2026-05-17T14:24:07.286208+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/",
  "description": "List config directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/",
    "description": "List config directory"
  }
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-17T14:24:07.336952+00:00_

approvals.yaml
backend.yaml
claude_sessions.json
crons.yaml
email_tokens.json
feishu.yaml
keepalive.json
mcp_config.json
mcp_config_briefer.json
mcp_config_director.json
mcp_config_dream_review_director.json
mcp_config_no_project.json
mcp_config_paper_agent.json
mcp_config_review_director.json
mcp_config_review_reviewer_1.json
mcp_config_review_reviewer_2.json
mcp_config_reviewer.json
mcp_config_worker_0a99ddd77d013c2bbf51ffccc89dfcc9.json
mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
mcp_config_worker_12093ef55c63229acbf88fd2b9106dce.json
mcp_config_worker_1f20be951a19580275e4408889e77c7a.json
mcp_config_worker_29834432f6498e7996daf9a6d4e8eda9.json
mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
mcp_config_worker_34467933ed5c0782ad72826a9574d432.json
mcp_config_worker_34a94861e96b7887a157fa6d27e375e0.json
mcp_config_worker_3683e51e3c097c93488562d683342ec7.json
mcp_config_worker_3ab953c77b6b0e7621a87cc89f47e64a.json
mcp_config_worker_5b83a101e2d66f0bdbaffa07ffd78ceb.json
mcp_config_worker_5fb1f955b45e38e31789286a1790398d.json
mcp_config_worker_6679bd63c74f529fddfcffaa0a492c96.json
mcp_config_worker_6f0b694c30c8a0575c498898ae58e765.json
mcp_config_worker_70ebd22373d3a7c470648796de71dbbf.json
mcp_config_worker_7fc16ee950d4cc0902b80c47aa5b8063.json
mcp_config_worker_8164f16cea05223301ec10d99f320a22.json
mcp_config_worker_83231a2aaaca12b920f60c26b84b9976.json
mcp_config_worker_8ce90f8d54cb7ad4888b21892ef36c51.json
mcp_config_worker_8fdc57f80f0cafc42cc1047c9dc7ebf1.json
mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
mcp_config_worker_986c566a50cd83dc4e21f03fd3f57ece.json
mcp_config_worker_af98c2743afa33d94f043b9d3e70ed88.json
mcp_config_worker_b06a4c556e994f6a91485114fa397cd6.json
mcp_config_worker_bc09978dd11e03e52315e5d71a6834ea.json
mcp_config_worker_ddf919c12f9233b9c1be7884efc37bb6.json
mcp_config_worker_de85c22e63104523a418fbc910122d4c.json
mcp_config_worker_e2d981ca8df69fe85b404249e1
…[truncated 308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-17T14:24:10.599516+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/",
  "description": "List project configs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/",
    "description": "List project configs"
  }
}
```

</details>

---


### Tool result

_source line 961 · 2026-05-17T14:24:10.650218+00:00_

simgate-modular-routing.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 962 · 2026-05-17T14:24:13.470194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/simgate-modular-routing.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/simgate-modular-routing.yaml"
  }
}
```

</details>

---


### Tool result

_source line 963 · 2026-05-17T14:24:13.520785+00:00_

1	execution:
2	  account: root
3	  gpu_constraint:
4	  - autodl-simgate:cuda:0
5	  - autodl-simgate:cuda:1
6	  gpu_ids:
7	  - cuda:0
8	  - cuda:1
9	  - cuda:2
10	  - cuda:3
11	  project_path: /root/autodl-tmp/simgate-modular-routing
12	  servers:
13	  - westb-13313
14	  - westb-14838
15	feishu:
16	  chat_id: oc_f6bffc7e8351600df8091f08a63cd5a0
17	  operational_chat_id: oc_6551c2d0ac89db1b3b9e56f77fcf912d
18	  review_paper_path: projects/simgate-modular-routing/docs/paper/
19	  review_round: 13
20	  review_supplementary_paths: ''
21	  submission_chat_id: oc_0b622d6038b969b96148ee8a163a1a0c
22	project:
23	  created_at: '2026-05-13T04:23:23.832Z'
24	  description: 'SimGate: Learning When to Route LLM Agents to Deterministic Computation
25	    via Explicit Modular Gating'
26	  name: simgate-modular-routing
27	  phase: research
28	  source_idea_id: idea_010
29	venue: emnlp-2026
30	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 964 · 2026-05-17T14:24:18.240862+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_rules/",
  "description": "List venue rules directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_rules/",
    "description": "List venue rules directory"
  }
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-17T14:24:18.291655+00:00_

corl-2026.yaml
emnlp-2026.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-17T14:24:21.051354+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 967 · 2026-05-17T14:24:21.102140+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  writing: []
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 968 · 2026-05-17T14:25:45.382339+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **目标 venue**: EMNLP 2026（通过 ARR May 2026 cycle）\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/`（main.tex + 分章节 tex 文件）\n- **渲染 PDF 页面**: `projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p1.png` 至 `main_p7.png`\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 不限参考文献/附录；Short paper: 4 页 + 不限\n- Limitations 节不计入页数\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名: double-blind\n- 引用: natbib (`acl_natbib.bst`)\n- 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你需要重点审查的内容\n\n1. **DAF 定义的合理性**：DAF = 1 - Δ_nd/Δ_full。论文承认当 P 恒定时 r=0.97 是代数推论而非独立实证发现。DAF 随 P 单调递增也是数学性质。这些自我认知是否充分？是否还有未被承认的循环论证或 tautological 问题？\n\n2. **SCI（Signal Concentration Index）**：基于 Gini 系数定义。它的引入是否有足够的 motivation？在论文中仅使用一次（SCI=0.2147），是否值得作为方法贡献的一部分？\n\n3. **统计方法**：\n   - 245 episodes、11 task types 的样本量是否足以支撑 claims？\n   - Episode-level bootstrap (B=10,000) 的合理性\n   - Cluster bootstrap K=11（论文已引用 Cameron et al. 2008 的 K≥40 threshold）\n   - McNemar test 在 MATH 对比中的使用\n   - Mann-Whitney 在 reasoning depth ablation 中的使用\n\n4. **Router 训练实验设计**：\n   - 数据增强（paraphrase-based）是否是评估 data scaling 的合适方法？\n   - 0.6B/1.7B/4B 三个 scale 的 capacity scaling 是否足够？\n   - 4B end-to-end 部署用 N=275（vs baseline N=245）的不一致性\n   - 1.7B 的 non-monotonic dip（episode-level 43.1%）是否有合理解释？\n\n5. **Cross-environment 证据强度**：\n   - MATH (N=795) 是 negative contrast，不是 replication\n   - ALFWorld (N=135) 的 modality 定义不同（information asymmetry vs computation mode）\n   - Llama pilot (N=70, 7 tasks) 样本量\n   - 这些加在一起是否足以支撑 Contribution 3？\n\n6. **Counterfactual labeling 的有效性**：\n   - Episode-level label 是否会导致 step-level mislabeling？（论文 Limitations 已提及）\n   - \"Pure-strategy\" 假设在多大程度上限制了 generalizability？\n   - 标记质量审计（Appendix A）是否令人信服？\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses（按 critical/warning/info 分级） → Questions → Missing References → Overall Assessment（使用 EMNLP 评分标准）→ Detailed Comments。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **目标 venue**: EMNLP 2026（通过 ARR May 2026 cycle）\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/`（main.tex + 分章节 tex 文件）\n- **渲染 PDF 页面**: `projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p1.png` 至 `main_p7.png`\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 不限参考文献/附录；Short paper: 4 页 + 不限\n- Limitations 节不计入页数\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名: double-blind\n- 引用: natbib (`acl_natbib.bst`)\n- 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你需要重点审查的内容\n\n1. **DAF 定义的合理性**：DAF = 1 - Δ_nd/Δ_full。论文承认当 P 恒定时 r=0.97 是代数推论而非独立实证发现。DAF 随 P 单调递增也是数学性质。这些自我认知是否充分？是否还有未被承认的循环论证或 tautological 问题？\n\n2. **SCI（Signal Concentration Index）**：基于 Gini 系数定义。它的引入是否有足够的 motivation？在论文中仅使用一次（SCI=0.2147），是否值得作为方法贡献的一部分？\n\n3. **统计方法**：\n   - 245 episodes、11 task types 的样本量是否足以支撑 claims？\n   - Episode-level bootstrap (B=10,000) 的合理性\n   - Cluster bootstrap K=11（论文已引用 Cameron et al. 2008 的 K≥40 threshold）\n   - McNemar test 在 MATH 对比中的使用\n   - Mann-Whitney 在 reasoning depth ablation 中的使用\n\n4. **Router 训练实验设计**：\n   - 数据增强（paraphrase-based）是否是评估 data scaling 的合适方法？\n   - 0.6B/1.7B/4B 三个 scale 的 capacity scaling 是否足够？\n   - 4B end-to-end 部署用 N=275（vs baseline N=245）的不一致性\n   - 1.7B 的 non-monotonic dip（episode-level 43.1%）是否有合理解释？\n\n5. **Cross-environment 证据强度**：\n   - MATH (N=795) 是 negative contrast，不是 replication\n   - ALFWorld (N=135) 的 modality 定义不同（information asymmetry vs computation mode）\n   - Llama pilot (N=70, 7 tasks) 样本量\n   - 这些加在一起是否足以支撑 Contribution 3？\n\n6. **Counterfactual labeling 的有效性**：\n   - Episode-level label 是否会导致 step-level mislabeling？（论文 Limitations 已提及）\n   - \"Pure-strategy\" 假设在多大程度上限制了 generalizability？\n   - 标记质量审计（Appendix A）是否令人信服？\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses（按 critical/warning/info 分级） → Questions → Missing References → Overall Assessment（使用 EMNLP 评分标准）→ Detailed Comments。"
  }
}
```

</details>

---


### Tool result

_source line 969 · 2026-05-17T14:26:10.122231+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24739
}
```

</details>

---


### Tool call

_source line 970 · 2026-05-17T14:26:10.375205+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作/格式**\n\n### 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **目标 venue**: EMNLP 2026（通过 ARR May 2026 cycle）\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/`（main.tex + 分章节 tex 文件）\n- **渲染 PDF 页面**: `projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p1.png` 至 `main_p7.png`\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 不限参考文献/附录；Short paper: 4 页 + 不限\n- Limitations 节不计入页数\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名: double-blind\n- 引用: natbib (`acl_natbib.bst`)\n- 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你需要重点审查的内容\n\n1. **贡献新颖性评估**：\n   - Contribution 1（counterfactual framework + DAF/SCI）：方法论贡献是否足够 novel？Episode-level counterfactual analysis 在 RL 领域有先例（Olson 2021, Gajcin 2023, Amitai 2024），本文的增量在哪？\n   - Contribution 2（ScienceWorld 实证）：核心发现是 \"death avoidance dominates routing\"。这在直觉上是否 obvious？内部推理会导致 hallucination → death 这一因果链是否需要如此大量的实验来确认？\n   - Contribution 3（cross-environment contrasts）：MATH null + ALFWorld 是 \"boundary conditions\" 而非 replication。这是否足以作为独立贡献？\n   - 总体：是否达到 EMNLP long paper 的贡献门槛？\n\n2. **Related Work 覆盖度**：\n   - Safe RL 领域：仅引用 Garcia 2015 和 CRPO 2021，是否遗漏关键工作？\n   - Tool use 领域：是否覆盖最新 2025-2026 工作？（论文已引用 tool-overuse-illusion, when2tool, tool-use-tax, to-call-or-not）\n   - Modality routing / adaptive computation：是否有遗漏？\n   - Counterfactual evaluation in RL：引用了 3 篇，是否充分？\n   - LLM agent 在 interactive environments 中的 failure mode 分析是否有未引用的相关工作？\n\n3. **写作质量**：\n   - Abstract 是否符合 150-250 words 惯例？是否过于技术密集？\n   - Introduction 叙事线是否连贯？从 \"routing 问题\" → \"现有方法假设\" → \"我们的发现\" 的过渡是否流畅？\n   - AI 写作痕迹检查：em-dash (—)、-ing phrase、过度分段、过渡词堆砌等\n   - 术语定义：DAF、SCI、\"death avoidance\"、\"counterfactual episode\" 等首次出现时是否有完整定义？\n   - 图表质量：Figure 1（scatter plot）、Figure 2（pipeline）、Figure 3（signal reversal）信息密度是否足够？Table 排版是否规范？\n\n4. **格式与篇幅**：\n   - **关键问题**：`paper_framing.md` 表明论文已从 short paper 升级为 long paper（8 页限制），但渲染 PDF 正文仅约 5 页。如果作为 long paper 提交，正文严重不足（差约 3 页）。如果作为 short paper 提交（4 页限制），则超出约 1 页。请评估这一篇幅问题的严重性。\n   - 模板使用是否正确？`\\usepackage[review]{acl}` 是否为 ARR 2026 当前要求？\n   - 行号是否正确显示？\n   - 参考文献格式一致性\n   - Appendix 是否过长？正文与 Appendix 的内容分配是否合理？\n\n5. **Reproducibility**：\n   - 是否提供了足够的实现细节（hyperparameters、seeds、环境配置）？\n   - \"Code and data will be released upon acceptance\" 是否足够？ARR 是否要求 anonymous submission 时提供代码？\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses（按 critical/warning/info 分级） → Questions → Missing References → Overall Assessment（使用 EMNLP 评分标准）→ Detailed Comments。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作/格式**\n\n### 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **目标 venue**: EMNLP 2026（通过 ARR May 2026 cycle）\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/`（main.tex + 分章节 tex 文件）\n- **渲染 PDF 页面**: `projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p1.png` 至 `main_p7.png`\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 不限参考文献/附录；Short paper: 4 页 + 不限\n- Limitations 节不计入页数\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名: double-blind\n- 引用: natbib (`acl_natbib.bst`)\n- 评分标准: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你需要重点审查的内容\n\n1. **贡献新颖性评估**：\n   - Contribution 1（counterfactual framework + DAF/SCI）：方法论贡献是否足够 novel？Episode-level counterfactual analysis 在 RL 领域有先例（Olson 2021, Gajcin 2023, Amitai 2024），本文的增量在哪？\n   - Contribution 2（ScienceWorld 实证）：核心发现是 \"death avoidance dominates routing\"。这在直觉上是否 obvious？内部推理会导致 hallucination → death 这一因果链是否需要如此大量的实验来确认？\n   - Contribution 3（cross-environment contrasts）：MATH null + ALFWorld 是 \"boundary conditions\" 而非 replication。这是否足以作为独立贡献？\n   - 总体：是否达到 EMNLP long paper 的贡献门槛？\n\n2. **Related Work 覆盖度**：\n   - Safe RL 领域：仅引用 Garcia 2015 和 CRPO 2021，是否遗漏关键工作？\n   - Tool use 领域：是否覆盖最新 2025-2026 工作？（论文已引用 tool-overuse-illusion, when2tool, tool-use-tax, to-call-or-not）\n   - Modality routing / adaptive computation：是否有遗漏？\n   - Counterfactual evaluation in RL：引用了 3 篇，是否充分？\n   - LLM agent 在 interactive environments 中的 failure mode 分析是否有未引用的相关工作？\n\n3. **写作质量**：\n   - Abstract 是否符合 150-250 words 惯例？是否过于技术密集？\n   - Introduction 叙事线是否连贯？从 \"routing 问题\" → \"现有方法假设\" → \"我们的发现\" 的过渡是否流畅？\n   - AI 写作痕迹检查：em-dash (—)、-ing phrase、过度分段、过渡词堆砌等\n   - 术语定义：DAF、SCI、\"death avoidance\"、\"counterfactual episode\" 等首次出现时是否有完整定义？\n   - 图表质量：Figure 1（scatter plot）、Figure 2（pipeline）、Figure 3（signal reversal）信息密度是否足够？Table 排版是否规范？\n\n4. **格式与篇幅**：\n   - **关键问题**：`paper_framing.md` 表明论文已从 short paper 升级为 long paper（8 页限制），但渲染 PDF 正文仅约 5 页。如果作为 long paper 提交，正文严重不足（差约 3 页）。如果作为 short paper 提交（4 页限制），则超出约 1 页。请评估这一篇幅问题的严重性。\n   - 模板使用是否正确？`\\usepackage[review]{acl}` 是否为 ARR 2026 当前要求？\n   - 行号是否正确显示？\n   - 参考文献格式一致性\n   - Appendix 是否过长？正文与 Appendix 的内容分配是否合理？\n\n5. **Reproducibility**：\n   - 是否提供了足够的实现细节（hyperparameters、seeds、环境配置）？\n   - \"Code and data will be released upon acceptance\" 是否足够？ARR 是否要求 anonymous submission 时提供代码？\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses（按 critical/warning/info 分级） → Questions → Missing References → Overall Assessment（使用 EMNLP 评分标准）→ Detailed Comments。"
  }
}
```

</details>

---


### Tool result

_source line 971 · 2026-05-17T14:26:11.753583+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1378
}
```

</details>

---


### Assistant

_source line 972 · 2026-05-17T14:26:19.432443+00:00_

审稿任务已分配：
- **Reviewer 1**（方法严谨性 + 实验设计）— 已派发
- **Reviewer 2**（新颖性 + 完整性 + 写作/格式）— 已派发

等待两位 Reviewer 完成独立初审。收到报告后将进入交叉分享环节（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 88

## Round 88

2 recorded events


### User

_source line 973 · 2026-05-17T14:32:31.059977+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿报告

**论文**: Death Avoidance as a Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 新颖性 + 完整性 + 写作/格式

---

## 总体评分

**Overall**: 2.5 / 5 (Borderline Findings)
**一句话总结**: 方法论新颖性有限，核心发现部分源于代数恒等式而非实证发现，且正文篇幅严重不足 long paper 要求。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 统计方法合理（bootstrap CI、LOO robustness），但核心指标 DAF 和 r=0.97 均为代数结果而非独立实证发现（论文自己承认），削弱了 empirical contribution 的力度 |
| Excitement | 2.0/5 | 核心发现"death avoidance dominates routing"在直觉上不令人意外：一个策略因幻觉死亡率高 + 环境施加 -100 惩罚，routing signal 被 death 主导是代数必然。框架本身（paired episode comparison + score decomposition）方法论贡献有限 |
| Reproducibility | 3.5/5 | 超参数、seed、bootstrap 配置均有报告；ScienceWorld/ALFWorld/MATH 为公开环境。但 code/data 仅承诺 "upon acceptance"，ARR 鼓励匿名提交时提供 |
| Reviewer Confidence | 4/5 | 熟悉 LLM agent routing、counterfactual evaluation、safe RL 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 正文篇幅严重不足 long paper 要求
- 具体位置：渲染 PDF 全文 7 页，其中正文（§1 Introduction 至 §Conclusion）约 4.5–5 页；Limitations + Ethics 占 ~0.5 页；References 从 p5 下半开始；Appendices 占 p6–p7。
- 问题：EMNLP long paper 限制为 8 页正文（不含 References/Limitations/Appendix）。当前正文仅约 5 页，缺失约 3 页内容。若作为 short paper 提交（4 页限制），则超出约 1 页。论文处于两种格式的尴尬中间地带。
- 为什么影响接收：篇幅不足通常意味着分析深度不够，审稿人会质疑是否有足够贡献支撑 long paper。且大量实质性内容（per-task decomposition、seed robustness、data scaling ablation、capacity scaling、cross-model verification、failure mode analysis、threshold routing）均被放入 Appendix，正文缺乏对这些关键结果的充分讨论。
- 建议修改方向：(a) 将 Appendix B（Per-Task Decomposition）、F（Seed Robustness + Data Scaling）、G（Capacity Scaling）的核心内容提升至正文，这些是支撑主要 claim 的关键证据；(b) Discussion 部分目前仅 ~0.5 页，需大幅扩展，特别是对 router design implications、failure mechanism analysis、generalization boundary 的讨论；(c) 或者重新定位为 short paper，但需压缩 Method 的形式化部分。

**N2** [critical] 核心发现的新颖性不足：DAF 是代数恒等式，r=0.97 是其数学推论
- 具体位置：§2.3（DAF 定义，Eq. 3-4）；§3.1 第二段（"this correlation follows algebraically from death dominance"）；Appendix E Table 6（r 随 P 单调增加）
- 问题：DAF = δP/(δP + Δ_nd) 是一个关于惩罚幅度 P 的单调递增函数。在 P=100 时 DAF=90.4%，但 P=10 时 DAF=50.4%，P=0 时 DAF=7.5%（Appendix E, Table 5）。"90.4%" 这个 headline number 完全取决于 ScienceWorld 碰巧使用的 P=100 设定。同样，per-task r=0.97 是 DAF→1 时的数学必然（论文 §3.1 自己承认）。这意味着论文的两个核心量化结果——DAF=90.4% 和 r=0.97——都不是独立的实证发现，而是环境参数设定的代数后果。
- 为什么影响接收：审稿人会问："除了告诉我们 P=100 在 ScienceWorld 里很大，这个发现还说明了什么？" 如果换一个 death penalty 更温和的环境，DAF 会大幅下降，但这不改变任何实质性洞察。论文虽然报告了 penalty-independent 指标（78.9% death-asymmetry labels），但这个指标在叙事中远不如 DAF=90.4% 突出。
- 建议修改方向：(a) 重新组织叙事，以 penalty-independent 的 78.9% label fraction 为 primary metric，将 DAF 降级为 supplementary/sensitivity analysis；(b) 更明确地讨论 DAF 的 P-dependence 意味着什么：不同 P 下 routing 策略的实质差异是什么？(c) 强化 penalty-independent 分析的深度（如：75 个 death-asymmetry label 中，有多少 episode 里 surviving strategy 的 score 也为 0？这类分析在 §3.1 有一句话提及但不够充分）。

**N3** [critical] 单一环境 + 有限 task 覆盖削弱 generalization claim
- 具体位置：§2.1（"11 prescreened task types"）；§Limitations（"19 excluded task types (63%) lack routing signal"）；Appendix B（task selection criteria）
- 问题：核心分析仅覆盖 ScienceWorld 30 个 task types 中的 11 个（36.7%），245 个 episode pairs，单一 backbone（Qwen2.5-7B）。Cross-environment evidence 本质上不是 replication：MATH 是 null result（确认无 death 则无 signal），ALFWorld 发现了完全不同的 mechanism（information asymmetry）。Llama pilot 仅 70 episodes、7 task types。论文 title 和 abstract 使用 "dominant routing signal" 作为主要 claim，但这只在一个特定环境、特定惩罚设定、特定模型规模下被验证。
- 为什么影响接收：Contribution 3（"cross-environment diagnostic contrasts"）不构成独立贡献：一个 null result + 一个 different mechanism + 一个 70-episode pilot = boundary conditions，不是 replication。作为 EMNLP long paper 的第三条 contribution 力度不够。
- 建议修改方向：(a) 诚实降级 Contribution 3 的措辞，不作为独立 contribution 列出，而是作为 discussion/analysis；(b) 在 title/abstract 中加入 scope qualifier（如 "in ScienceWorld" 已有，但 abstract 的 framing 暗示更广泛的适用性）；(c) 最理想的修复是增加一个有 catastrophic failure 的第二环境（如论文提到的 NetHack/Crafter）进行真正的 replication。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 过度密集，数字堆砌而非叙事驱动
- 具体位置：abstract.tex（~190 words）
- 问题：Abstract 包含至少 15 个数字/统计量（78.9%、75 of 95、DAF=90.4%、P=100、r=0.97、59.0%、4B、N=795、p=0.81、N=135 等）。虽然 word count 在 150-250 范围内，但信息密度过高，读起来像 results summary 而非 compelling narrative。审稿人在 30 秒内难以抓住核心价值。
- 建议：减少到 5-6 个关键数字，将注意力集中在 "why this matters" 而非 "what numbers we got"。

**W2** [warning] Related Work 中 Safe RL 覆盖严重不足
- 具体位置：§4, "Safe RL" paragraph（仅 3 行，2 篇引用：Garcia 2015, CRPO 2021）
- 问题：论文的核心 claim 是 "routing is fundamentally a safety problem"（Discussion §5），但 Safe RL 领域仅引用一篇 2015 survey 和一篇 2021 方法论文。缺失大量相关工作：(a) Constrained MDP 文献（Altman 1999）；(b) Safe exploration 方法（如 SafeOpt, CPO, LAMBDA 等）；(c) 近年 safe RL benchmark 和 evaluation（如 Safety Gymnasium / SafeRL-Kit）；(d) LLM safety / alignment as routing 的视角（如 constitutional AI、RLHF 中的 safety constraint）。
- 建议：既然论文明确将 routing 重新框架为 safety problem，Related Work 必须充分覆盖 safe RL 和 LLM safety 文献，否则审稿人会质疑作者对这一领域的了解深度。

**W3** [warning] SCI 指标贡献不清晰
- 具体位置：§2.4（SCI 定义）；§3.1 第三段（SCI = 0.2147，仅出现一次）
- 问题：SCI 是 Gini coefficient 直接应用于 per-task routing signal contributions。(a) 重命名一个众所周知的统计量（Gini coefficient）为新术语（SCI）增加了术语负担但没有增加洞察；(b) SCI 在整篇论文中仅出现一次（§3.1），没有在 cross-environment 分析中使用，没有在 Discussion 中讨论其 implications；(c) 它出现在 Method §2 的 framework 定义中（暗示是核心组件），但实际上对论文叙事几乎没有贡献。
- 建议：要么充分利用 SCI（在所有三个环境中计算、讨论不同 SCI 值的 implications），要么降级为 supplementary metric 不在 Method 中单独成一小节。

**W4** [warning] Algorithm 1 形式化程度与内容复杂度不匹配
- 具体位置：§2.2, Algorithm 1（method.tex lines 59-84）
- 问题：Algorithm 1 描述的逻辑本质上是：(1) 若一方死另一方活 → 偏好活的；(2) 若都死 → 无偏好；(3) 否则比分数。这是直觉上显而易见的 3-case 判断，用正式 Algorithm 环境 + 8 行伪代码呈现显得 over-formalized，占据了宝贵的正文空间。
- 建议：考虑用 inline 描述或紧凑的表格替代，将节省的空间用于更需要讨论的内容。

**W5** [warning] 缺少 LLM agent failure mode 分析的相关引用
- 具体位置：§4 Related Work
- 问题：论文核心 mechanism 是 "internal strategy hallucination → cascading errors → agent death"（§5 Discussion, Appendix G）。但 Related Work 未引用 LLM agent 在 interactive environments 中 failure mode 的分析工作，如：(a) WebArena 及类似 benchmark 的 agent failure 分析；(b) LLM agent 的 error propagation / compounding error 研究；(c) Hallucination in grounded/interactive settings 的专门研究。SelfCheckGPT 被引用但它是 hallucination detection，不是 interactive agent failure analysis。

**W6** [warning] Router training 负面结果的解释不完整
- 具体位置：§3.3；Appendix D, F
- 问题：Router 无法超越 always-deterministic 是论文的重要发现，但原因分析不够深入。论文将其归因于 "structural limitation"（86:9 label imbalance + task-type-level signal），但没有充分讨论：(a) episode-level label 传播到 step-level training 的信息损失有多大？(b) 如果用 step-level oracle（在有 signal 的环境中）训练会如何？(c) "always-deterministic is near-optimal" 是否仅因为 test-time evaluation 也在同一环境/model？更强的 internal reasoning（如 Reflexion）可能改变这一结论。
- 建议：Discussion 中需要更深入分析 router failure 的根本原因，以及在什么条件下 router 可能变得有用。

---

## 小问题（不影响接收）

1. **Title 不一致**：main.tex line 18 使用 "a Dominant Routing Signal"（不定冠词），但论文行文中多处使用 "the dominant" 的语气。建议统一。
2. **Reference 格式**：部分引用使用 "and others"（如 retool-2025, cogrouter-2026 等），应展开为完整作者列表或使用标准 "et al." 格式。arXiv preprint 和 conference paper 混合出现，格式应统一（如统一是否标注 arXiv ID）。
3. **Figure 2（pipeline overview）** 在渲染 PDF 中位置不够突出，可能被挤压。作为 framework 的视觉概述，应确保清晰可见。
4. **Footnote 1**（§3.3, end-to-end deployment）解释 N=275 vs N=245 的差异，但这种 evaluation 数据量不一致会引起审稿人的 concern，应在正文中更好地解释或统一。
5. **Writing style**: 整体无 AI 写作痕迹（无 em-dash、无 -ing phrase 结尾、无过渡词堆砌），写作质量良好。但部分段落信息密度过高（特别是 §3.1），可适当拆分或增加过渡。
6. **Appendix 内容分配不合理**：Table 2（Per-Task Decomposition）、Table 6/7（Penalty Sensitivity + Correlation）、Table 8（Capacity Scaling）是核心分析的关键证据，不应藏在 Appendix 中。这些内容应出现在正文——这也有助于解决 N1 的篇幅问题。

---

## 缺失引用

以下是审查中发现可能需要补充的引用方向（非穷举）：

1. **Safe RL 方法论**：Constrained MDP（Altman 1999）、CPO（Achiam et al., 2017）、SafeRL benchmarks（Safety Gymnasium 等）
2. **LLM agent failure analysis**：WebArena agent error analysis、InterCode/SWE-bench 中的 agent failure patterns、compounding error in sequential decision making
3. **Routing/MoE 基础文献**：Switch Transformer（Fedus et al., 2022）、GShard 等 MoE routing 方法——虽然 domain 不同但 routing mechanism 有共性
4. **Hallucination in grounded settings**：GroundedQA、embodied agent hallucination 相关工作
5. **Adaptive computation 近期工作**：论文已引用 CogRouter/ARES/MTRouter/RouteLLM，但 FrugalGPT（Chen et al., 2023）、Hybrid LLM（Ding et al., 2024）等 cost-aware routing 工作可能相关

---

## 主要优势

1. **问题定位清晰**：论文问的是 "what drives routing signal"，这是一个被忽视但重要的 prior question。大多数 routing 工作假设 diverse signal exists，本文质疑这一假设。
2. **统计方法严谨**：Bootstrap CI、LOO robustness、cluster bootstrap、cross-split evaluation、data scaling ablation——对一篇分析型论文而言，统计验证工作扎实。
3. **诚实的自我批评**：论文主动承认 r=0.97 是代数结果、DAF 是 P-dependent、cross-environment evidence 不是 replication。这种诚实在学术论文中值得赞赏。
4. **Negative results 有价值**：Router 无法超越 always-deterministic 的发现，以及 MATH 的 null result，对 practitioner 有实际参考价值。
5. **写作风格干净**：无 AI 写作痕迹，技术写作准确，术语使用规范。
6. **Appendix 内容充实**：labeling quality audit、per-task decomposition、seed robustness、data scaling、capacity scaling、cross-model、failure mode、threshold routing——分析非常全面。

---

## 对审稿人的问题

1. 如果将 DAF 定义中的 P 设为 1（即 death 只扣 1 分而非 100 分），DAF = δ/(δ + Δ_nd) ≈ 0.265/(0.265 + 2.84) ≈ 8.5%。此时你是否仍会得出 "death avoidance is the dominant routing signal" 的结论？如果不会，这说明你的 claim 本质上是关于惩罚幅度而非 routing mechanism。
2. 78.9% death-asymmetry labels 中，有 54/75（72%）在移除 death penalty 后变为 tie（both score 0）。这意味着这些 episode 中两种策略在非死亡维度上完全没有差异。这是否说明 ScienceWorld 的 30-step 预算对 internal strategy 过于苛刻，而非 routing mechanism 本身的性质？
3. 论文排除了 19/30（63%）的 task types 因为 "both strategies time out"。如果增加 step budget（如 100 步），这些 task types 可能出现 routing signal。当前发现是否高度依赖于 30-step 的实验设置？
4. ALFWorld 的 deterministic 策略接收 admissible actions（等价于 action space pruning），这与 ScienceWorld 中 deterministic = ground-truth observation 是根本不同的 "deterministic modality" 定义。将两者放在同一 framework 下比较是否存在概念混淆？

---

## Overall Assessment 详细说明

**评分：2.5（Borderline Findings）**

论文提出了一个清晰的问题（what drives routing signal），设计了合理的实验框架，并得出了有实际参考价值的结论（在有 catastrophic failure 的环境中，death avoidance dominates routing）。统计分析扎实，写作质量良好。

主要顾虑：(1) 核心量化结果（DAF=90.4%, r=0.97）是代数恒等式的产物，独立实证贡献有限；(2) 方法论新颖性不足——episode-level paired comparison + score decomposition 不构成 significant methodological advance；(3) 正文篇幅严重不足 long paper 要求，大量核心内容藏在 Appendix；(4) generalization 仅限于单一环境 + 单一模型规模，cross-environment evidence 不构成 replication。

如果论文 (a) 解决篇幅问题（将关键 Appendix 内容纳入正文），(b) 重新组织叙事以 penalty-independent findings 为核心降低对 DAF headline number 的依赖，(c) 增加一个 catastrophic-failure environment 的 replication，(d) 充分扩展 Discussion，则有望达到 3.0-3.5（Findings 至 Borderline Conference）。当前状态下，贡献更接近 workshop paper 或 short paper 水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 974 · 2026-05-17T14:32:41.031393+00:00_

Reviewer 2 审稿报告已收到。评分 2.5（Borderline Findings），主要问题集中在：正文篇幅不足 long paper 要求（N1）、DAF 核心指标的代数性质（N2）、单环境 generalization 不足（N3）。

等待 Reviewer 1 报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 89

## Round 89

2 recorded events


### User

_source line 975 · 2026-05-17T14:32:43.523173+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交。核心判断：

**Overall 2.5（Borderline Findings）**。三个 critical 问题：

1. **篇幅严重不足**：正文约 5 页，距 long paper 8 页要求差 3 页，大量核心证据藏在 Appendix
2. **核心发现部分是代数恒等式**：DAF=90.4% 取决于 ScienceWorld 的 P=100 设定（P=10 时 DAF=50.4%），r=0.97 是 DAF→1 的数学推论而非独立实证发现
3. **Generalization 不足**：单一环境 + 11/30 task types + 7-8B 模型；cross-environment evidence 是 boundary conditions 而非 replication

论文优势在于问题定位清晰、统计方法严谨、自我批评诚实、negative results 有参考价值。写作无 AI 痕迹。如果解决篇幅问题、重组叙事以 penalty-independent 指标为核心、增加第二个 catastrophic-failure 环境的 replication，有望提升至 3.0-3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 976 · 2026-05-17T14:32:49.167290+00:00_

收到 Reviewer 2 的报告。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 90

## Round 90

6 recorded events


### User

_source line 977 · 2026-05-17T14:34:18.900502+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**审查侧重**: 方法严谨性 + 实验设计

---

## 总体评分

**Overall**: 3.0 / 5 (Findings)
**一句话总结**: 研究问题有价值，counterfactual 框架设计合理，但核心发现的新颖性受限于其与环境惩罚结构的数学耦合，实验规模和跨环境证据不足以支撑当前 claim 的强度。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0 / 5 | 核心框架逻辑自洽，论文对多个数学性质有诚实的 self-acknowledgment；但 DAF 与 P 的数学耦合使核心发现的经验性贡献被削弱，cluster bootstrap K=11 远低于作者自引的 K≥40 阈值，router 实验存在多个 confound |
| Excitement | 2.5 / 5 | "routing signal 的本质是什么"这个问题有价值，但答案（高惩罚环境中死亡主导 routing）在了解环境惩罚结构后并不出人意料；框架的可迁移性尚未得到充分验证 |
| Reproducibility | 4.0 / 5 | Appendix 提供了完整的超参数、seed、数据划分细节；承诺 release code/data；Algorithm 1 可直接复现 |
| Reviewer Confidence | 4 / 5 | 熟悉 LLM agent 评估、counterfactual 方法和 bootstrap 统计推断 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DAF 的核心发现与环境惩罚结构存在部分 tautology，论文 framing 仍然过度强调"经验发现"

- 具体位置：§2.3 Eq. (2), §3.1, Abstract, Introduction
- 问题：DAF = δP/(δP + Δ_nd)。当 P=100 而 Δ_nd=2.84 时，DAF ≈ 100×0.265/(100×0.265+2.84) = 90.3%。这个高值主要由 P/Δ_nd 的比值决定，而非独立的经验发现。论文在 §3.1 和 §2.3 确实承认了"DAF increases monotonically with P, a mathematical consequence"以及"r=0.97 is a mathematical consequence of death dominance"，这种 self-awareness 值得肯定。但 Abstract 仍以"the framework reveals that 78.9% of non-tie routing labels arise from death asymmetry"作为核心卖点，而 Introduction 用"a surprisingly concentrated answer"来 frame 这个发现。当 internal 策略死亡率是 deterministic 的 2.6 倍（42.9% vs 16.3%），且死亡惩罚是典型分数差异的 35 倍（100 vs ~2.84），死亡主导 routing signal 是从环境参数即可预测的结论，不是需要复杂框架才能揭示的"surprising"发现。
- penalty-independent 指标（78.9%）比 DAF 更有信息量，但 labeling algorithm（Algorithm 1, lines 5-8）本身将 death asymmetry 置于 score comparison 之前。虽然在 P=100 的环境中改变优先级不会实质改变结果（因为 -100 惩罚自然使存活策略得分更高），但论文应当明确讨论这一设计选择对指标的影响。
- 为什么影响接收：如果核心发现的经验性贡献被大幅削弱，论文的 contribution 1 和 contribution 2 的价值需要重新评估。
- 建议：(a) 在 Abstract/Introduction 中明确区分"框架贡献"与"经验发现"，降低对 DAF 数值的依赖，更多强调 penalty-independent 指标和框架的诊断能力；(b) 增加一个"predictability analysis"：给定已知的死亡率差异和 P，DAF 的预期值是多少，实际值偏离多少？如果偏离很小，应诚实说明这是 confirmation 而非 discovery。

**N2** [critical] 统计推断的可靠性不足以支撑 claim 的强度

- 具体位置：§3.1 (bootstrap CIs), §3.2 (Llama pilot), Appendix B (per-task), Appendix C (correlation)
- 问题：
  - (a) **Cluster bootstrap K=11**：论文自引 Cameron et al. (2008) 的 K≥40 门槛，但仍使用 K=11 做 cluster bootstrap 并报告 CI [73.3%, 100%]。论文说"should be interpreted cautiously"，但这个 CI 在统计上是不可靠的——K=11 时 cluster bootstrap 的覆盖率远低于名义 95%。这不是"cautious interpretation"能弥补的；它是一个不满足前提条件的统计检验。
  - (b) **Episode-level bootstrap 的独立性假设**：10,000 次重采样假设 245 个 episode 相互独立。但同一 task type 内的 episode 共享 task structure、scoring rubric、环境布局。论文提供了 cluster bootstrap 作为 sensitivity analysis，但如上所述该分析本身不可靠。
  - (c) **Per-task 样本量**：11 个 task type 中 10 个仅有 n=20（find-non-living-thing 为 n=40）。chemistry-mix 的 CI [-5.0, 48.6] 跨越零点。以 n=20 计算 per-task 死亡率差异和 DAF，置信区间极宽，但论文在主文中以"10 of 11 types exhibit DAF=100%"这样的断言呈现结果，掩盖了不确定性。
  - (d) **Llama pilot N=70, 7 tasks**：每个 task 仅 10 个 episode。0 个 internal-preferred 标签与 N=70 的样本量结合，能排除的 internal-preferred 率上界约为 4.2%（95% CI by Clopper-Pearson），远不足以支撑"directional consistency"之外的定量结论。
- 为什么影响接收：论文声称的 claim 强度（"death avoidance accounts for approximately 90%"）与统计证据的强度不匹配。
- 建议：(a) 对 cluster bootstrap 的不可靠性做更诚实的讨论，考虑使用 wild cluster bootstrap 或 permutation test 作为替代；(b) Llama pilot 应被明确标记为 anecdotal evidence，不应出现在 Contribution 3 中。

**N3** [critical] 跨环境证据不足以支撑 Contribution 3（"Cross-environment diagnostic contrasts establishing framework boundary conditions"）

- 具体位置：§3.4, §3.5, Introduction Contribution 3, Discussion
- 问题：Contribution 3 声称"cross-environment diagnostic contrasts establishing framework boundary conditions"，但三个跨环境分析中没有一个构成 DAF 框架的真正 replication：
  - (a) **MATH (N=795)** 是 negative contrast（预测无 routing signal，结果确实无），验证了一个 predicted null。但这是一个弱检验——任何合理的框架都会预测"无死亡惩罚 → 无死亡主导"。更关键的是，MATH 的 modality 定义（internal reasoning vs code interpreter）与 ScienceWorld（internal vs ground-truth observation）不同，能力维度从"观测准确性"变为"计算准确性"。
  - (b) **ALFWorld (N=135)** 的 modality 定义根本不同（information access: 有无 admissible actions），论文自己承认这是"information asymmetry rather than a computation mode switch"（§3.5）。这说明框架可以"应用"到不同环境，但不证明 DAF 发现的可迁移性。
  - (c) **Llama pilot (N=70, 7 tasks)** 样本量过小（见 N2-d），且两个模型都在 7-8B 范围内。
  - 最关键的缺失：**没有第二个具有 catastrophic failure 的环境**。论文在 Discussion 中提到 NetHack 和 Crafter 作为 future work，但这恰恰是验证 Contribution 3 最需要的证据。
- 为什么影响接收：Contribution 3 的实际证据远弱于其 claim。一个 predicted null + 一个不同机制的环境 + 一个 tiny pilot ≠ "establishing framework boundary conditions"。
- 建议：(a) 将 Contribution 3 降级为"preliminary cross-environment evidence suggesting boundary conditions"；(b) 如果篇幅允许（论文当前仅用了约 5 页正文，远低于 8 页限制），在 NetHack 或 Crafter 上提供至少一个有 catastrophic failure 的 replication。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Router 训练实验存在多个 confound，削弱了"diagnostic probe"的说服力

- 具体位置：§3.6, Appendix D-F, Table 4-6
- 问题：
  - (a) **Paraphrase augmentation 不是真正的 data scaling**：表 6 标题为"Data scaling ablation"，但 synonym substitution + template variation 不产生新的 routing pattern，只是 inflate majority class（89.6% → 97.7%）。论文承认了这一点，但仍在主文中使用"Data scaling (32×) ablations confirm this is structural rather than data-limited"的断言（Introduction, §3.6）。正确的结论应该是"augmentation-based pseudo-scaling confirms the failure is not augmentation-solvable; real-data scaling remains untested"。
  - (b) **4B end-to-end 使用 N=275 vs baselines 的 N=245**：脚注解释为"expanded task coverage"，但这引入了直接的比较 confound。"-10.72 (4B) vs -9.47 (always-det)"的比较跨越了不同的 task 分布。
  - (c) **1.7B 的 non-monotonic dip（episode-level 43.1%，低于 0.6B 的 50.7%）未被解释**：论文仅说"non-monotonic pattern, combined with universally low internal recall, reinforces that learned routing does not scale predictably"。但 1.7B 显著低于 chance 是一个需要解释的现象——是否因为 1.7B 学到了某种反向的 spurious correlation？是否因为 1.7B 的 LoRA capacity 刚好足以过拟合 step-level 但以有害方式迁移到 episode-level？
- 建议：(a) 将"data scaling"改为"augmentation scaling"并调整结论措辞；(b) 在相同 N=245 task set 上评估 4B router，或至少报告 shared task types 上的 per-task 对比；(c) 对 1.7B dip 提供至少一个可检验的 hypothesis。

**W2** [warning] Episode-level label → step-level training 的 mismatch 未被量化

- 具体位置：Limitations, §3.6, Appendix A
- 问题：论文承认"episode-level labels may assign suboptimal routing to individual steps, particularly those preceding death events"，但没有量化这个 mislabeling 的规模。如果 internal 策略在 step 20 死亡（30-step episode），前 19 步可能在 internal 下表现正常，但都被标记为 det-preferred。给定 42.9% 的 internal 死亡率和平均 episode 长度，可以估算有多少比例的 step-level labels 是 potentially mislabeled。这个数字直接影响 router training 的 signal quality 评估。
- 建议：计算并报告 "potentially mislabeled step fraction"——即来自死亡 episode 的 non-terminal steps 占所有训练 steps 的比例。

**W3** [warning] SCI（Signal Concentration Index）的方法贡献与实际使用不成比例

- 具体位置：§2.4, §3.1
- 问题：SCI 在 Method 中用了完整的 §2.4 来定义（Eq. 5-6），但在全文中仅使用一次：§3.1 报告 SCI=0.2147 并说"low concentration"。K=11 个 task type 计算 Gini 系数的统计意义有限。更直接的描述（"top-3 task types account for 39.8% of total death-rate differential"）传达了完全相同的信息。
- 在当前论文中，SCI 既不是核心 contribution（未在 contribution list 中提及），也没有在多个环境或条件下对比使用。它增加了 Method section 的复杂度但未提供相应的 analytical payoff。
- 建议：将 SCI 降级到 Appendix，在主文中用一句描述性语言替代。释放的空间可以用来扩展更有价值的分析（如 cross-environment replication 或 mislabeling 量化）。

**W4** [warning] 论文正文仅约 5 页，显著低于 long paper 的 8 页限制

- 具体位置：全文结构
- 问题：Sections 1-6（Introduction 到 Conclusion）加上 Discussion 约占 5 页正文。Limitations 和 Ethics 不计入页数。大量关键分析被放在 Appendix 中（penalty sensitivity analysis、capacity scaling details、seed robustness、data scaling ablation、per-task decomposition），但正文有充足的空间容纳这些内容。特别是 Appendix E（penalty sensitivity，Table 5-6）和 Appendix F（capacity scaling，Table 4）对理解核心 claim 至关重要，不应被边缘化到附录。
- 建议：将 penalty sensitivity analysis（含 Table 5-6）、capacity scaling（Table 4）移入主文。如果是 short paper 投稿则当前长度合适，但作为 long paper 正文明显不足。

---

## 小问题（不影响接收）

- **标题不一致**：main.tex 第 18 行写"Death Avoidance as **a** Dominant Routing Signal"，但渲染 PDF 标题为"Death Avoidance as **the** Dominant Routing Signal"。需统一。"the"更符合论文 claim。
- **Table 1 的"Score"列**：episode-weighted mean score 为负数（如 Always-Internal = -39.07），对不熟悉 ScienceWorld 的读者可能 confusing。建议在 caption 中简要解释负分的来源（death penalty）。
- **Figure 2（signal_reversal.pdf）**: 标题为"Label distribution across environments"，但仅覆盖 ScienceWorld 和 MATH，未包含 ALFWorld。建议补全或修改标题。实际看图，ALFWorld 似乎没有画进去。
- **引用格式**：Gajcin (2023) 在 OpenAlex 中未找到精确匹配（similarity 0.78），建议核实该引用的完整标题和出处。

---

## 缺失引用

论文的引用覆盖度在 tool use、routing、agent 方面基本充分（35 篇，涵盖 foundation + competitors + benchmarks）。以下方向可考虑补充：

1. **Voyager** (Wang et al., 2023) — 论文 Related Work 提到但未在 bib 中找到对应条目（可能是我遗漏，但 verify_references 未标记为 orphan，说明可能未被引用）。作为 ScienceWorld 类 open-ended agent 的重要 baseline，建议确认。
2. **Off-policy evaluation / counterfactual reasoning in sequential decision-making** — 论文的 counterfactual 框架与 off-policy evaluation (OPE) 文献（如 Precup et al. 2000, Jiang & Li 2016 的 doubly robust estimator）有方法论联系。当前 Related Work §4.3 仅引用了 RL counterfactual explanation 方面的工作，缺少 OPE 方向。
3. **Distribution shift / covariate shift in imitation learning** — 论文引用了 DAgger (Ross et al. 2011) 来讨论 pure-strategy 训练的局限，但 covariate shift 文献中有更直接相关的分析框架。

---

## 主要优势

1. **研究问题有价值且定义清晰**：在 LLM agent routing 领域，"what actually drives routing signal"是一个被忽视但重要的诊断性问题。论文将其从"learning to route"转向"understanding routing signal"，视角独特。

2. **论文的学术诚实度异常高**：几乎所有统计/方法论限制都被主动承认——r=0.97 是代数推论（§3.1）、DAF 随 P 单调递增是数学性质（§2.3）、cluster bootstrap K<40 不可靠（§3.1）、augmentation 不等于 real data scaling（§3.6, Appendix E）、cross-environment 不是 replication（Discussion）。这种 self-awareness 在提交论文中非常罕见，应予肯定。

3. **Counterfactual episode collection 框架设计合理**：Algorithm 1 的 death-aware labeling 在概念上简洁，dual metrics（penalty-independent 78.9% + penalty-dependent DAF）的设计比单一指标更稳健。框架确实可应用于其他环境（如论文在 ALFWorld 上的演示）。

4. **Negative contrast 实验有说服力**：MATH (N=795) 的 null result (p=0.81) 使用 McNemar test 进行了恰当的检验，有效验证了"无 catastrophic failure → 无 routing signal"的预测。

5. **Appendix 的分析深度**：penalty sensitivity（7 个 P 值 + correlation 随 P 变化）、seed robustness（8 seeds, 两个粒度）、per-task decomposition、leave-one-out correlation stability、threshold routing analysis——这些 supporting analyses 显示了认真的实验态度。

---

## 总结性判断

论文提出了一个有价值的诊断性问题，设计了合理的 counterfactual 框架，并以罕见的学术诚实度呈现了结果。核心限制在于：(1) DAF 的高值在很大程度上是环境惩罚结构的数学后果，而非独立的经验发现；(2) 实验局限于单一环境 + 单一模型尺度范围；(3) 跨环境证据不构成 framework replication。这些问题使论文更适合 Findings 而非主会议。如果作者能增加一个 catastrophic-failure 环境的 replication（如 NetHack），重新校准 Abstract/Introduction 的 framing，并将关键附录分析移入正文，论文的 contribution 会显著增强。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-17T14:35:16.574905+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注你们在以下几个问题上是否存在分歧：\n1. 篇幅问题的严重性（N1）\n2. DAF tautology 的程度（N2 vs 你的 N1）\n3. SCI 的价值（W3 vs 你的 W3）\n4. Algorithm 1 是否 over-formalized（W4）\n5. 总体评分差异（你给 3.0 vs R2 给 2.5）\n\n---\n\n# Reviewer 2 完整审稿报告\n\n**Overall**: 2.5 / 5 (Borderline Findings)\n\n## 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 统计方法合理（bootstrap CI、LOO robustness），但核心指标 DAF 和 r=0.97 均为代数结果而非独立实证发现（论文自己承认），削弱了 empirical contribution 的力度 |\n| Excitement | 2.0/5 | 核心发现\"death avoidance dominates routing\"在直觉上不令人意外：一个策略因幻觉死亡率高 + 环境施加 -100 惩罚，routing signal 被 death 主导是代数必然。框架本身（paired episode comparison + score decomposition）方法论贡献有限 |\n| Reproducibility | 3.5/5 | 超参数、seed、bootstrap 配置均有报告；ScienceWorld/ALFWorld/MATH 为公开环境。但 code/data 仅承诺 \"upon acceptance\"，ARR 鼓励匿名提交时提供 |\n| Reviewer Confidence | 4/5 | 熟悉 LLM agent routing、counterfactual evaluation、safe RL 相关文献 |\n\n## Must-Fix 问题\n\n**N1** [critical] 正文篇幅严重不足 long paper 要求\n- 渲染 PDF 全文 7 页，正文约 4.5–5 页；Limitations + Ethics 占 ~0.5 页；References 从 p5 下半开始；Appendices 占 p6–p7。\n- EMNLP long paper 限制为 8 页正文。当前正文仅约 5 页，缺失约 3 页内容。若作为 short paper 提交（4 页限制），则超出约 1 页。\n- 大量实质性内容（per-task decomposition、seed robustness、data scaling ablation、capacity scaling、cross-model verification、failure mode analysis、threshold routing）均被放入 Appendix，正文缺乏对这些关键结果的充分讨论。\n- 建议：将 Appendix B（Per-Task Decomposition）、F（Seed Robustness + Data Scaling）、G（Capacity Scaling）的核心内容提升至正文；Discussion 部分目前仅 ~0.5 页需大幅扩展。\n\n**N2** [critical] 核心发现的新颖性不足：DAF 是代数恒等式，r=0.97 是其数学推论\n- DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数。P=100 时 DAF=90.4%，P=10 时 DAF=50.4%，P=0 时 DAF=7.5%。\"90.4%\" 完全取决于 ScienceWorld 的 P=100 设定。\n- 论文的两个核心量化结果——DAF=90.4% 和 r=0.97——都不是独立的实证发现，而是环境参数设定的代数后果。\n- 建议：重新组织叙事以 penalty-independent 的 78.9% label fraction 为 primary metric，将 DAF 降级为 supplementary。\n\n**N3** [critical] 单一环境 + 有限 task 覆盖削弱 generalization claim\n- 核心分析仅覆盖 ScienceWorld 30 个 task types 中的 11 个（36.7%），245 episodes，单一 backbone。\n- MATH 是 null result，ALFWorld 发现完全不同的 mechanism，Llama pilot 仅 70 episodes。\n- Contribution 3 不构成独立贡献：一个 null result + 一个 different mechanism + 一个 70-episode pilot = boundary conditions，不是 replication。\n- 建议：降级 Contribution 3 的措辞；最理想是增加 NetHack/Crafter 的 replication。\n\n## Should-Fix 问题\n\n**W1** [warning] Abstract 过度密集，数字堆砌（~15 个数字/统计量）\n**W2** [warning] Safe RL 覆盖严重不足（仅 Garcia 2015 + CRPO 2021）\n**W3** [warning] SCI 指标贡献不清晰：仅使用一次，本质是 Gini coefficient 的 rename\n**W4** [warning] Algorithm 1 形式化程度与内容复杂度不匹配（3-case 判断用 8 行伪代码）\n**W5** [warning] 缺少 LLM agent failure mode 分析的相关引用\n**W6** [warning] Router training 负面结果的解释不完整\n\n## 小问题\n1. Title 不一致（\"a\" vs \"the\" dominant）\n2. Reference 格式不统一\n3. Figure 2 位置不够突出\n4. N=275 vs N=245 不一致\n5. 写作风格干净无 AI 痕迹\n6. Appendix 内容分配不合理\n\n## 缺失引用\nSafe RL 方法论（Altman 1999, CPO, Safety Gymnasium）、LLM agent failure analysis、MoE routing 基础文献、Hallucination in grounded settings、FrugalGPT/Hybrid LLM\n\n## 审稿人提出的问题\nQ1: P=1 时 DAF≈8.5%，是否仍能得出 \"death avoidance is dominant\" 的结论？\nQ2: 54/75 death-asymmetry labels 移除 death penalty 后变为 tie，是否说明 30-step budget 过于苛刻？\nQ3: 排除 63% task types 后，发现是否高度依赖 30-step 设置？\nQ4: ALFWorld 的 \"deterministic modality\" 定义与 ScienceWorld 根本不同，框架比较是否有概念混淆？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注你们在以下几个问题上是否存在分歧：\n1. 篇幅问题的严重性（N1）\n2. DAF tautology 的程度（N2 vs 你的 N1）\n3. SCI 的价值（W3 vs 你的 W3）\n4. Algorithm 1 是否 over-formalized（W4）\n5. 总体评分差异（你给 3.0 vs R2 给 2.5）\n\n---\n\n# Reviewer 2 完整审稿报告\n\n**Overall**: 2.5 / 5 (Borderline Findings)\n\n## 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 统计方法合理（bootstrap CI、LOO robustness），但核心指标 DAF 和 r=0.97 均为代数结果而非独立实证发现（论文自己承认），削弱了 empirical contribution 的力度 |\n| Excitement | 2.0/5 | 核心发现\"death avoidance dominates routing\"在直觉上不令人意外：一个策略因幻觉死亡率高 + 环境施加 -100 惩罚，routing signal 被 death 主导是代数必然。框架本身（paired episode comparison + score decomposition）方法论贡献有限 |\n| Reproducibility | 3.5/5 | 超参数、seed、bootstrap 配置均有报告；ScienceWorld/ALFWorld/MATH 为公开环境。但 code/data 仅承诺 \"upon acceptance\"，ARR 鼓励匿名提交时提供 |\n| Reviewer Confidence | 4/5 | 熟悉 LLM agent routing、counterfactual evaluation、safe RL 相关文献 |\n\n## Must-Fix 问题\n\n**N1** [critical] 正文篇幅严重不足 long paper 要求\n- 渲染 PDF 全文 7 页，正文约 4.5–5 页；Limitations + Ethics 占 ~0.5 页；References 从 p5 下半开始；Appendices 占 p6–p7。\n- EMNLP long paper 限制为 8 页正文。当前正文仅约 5 页，缺失约 3 页内容。若作为 short paper 提交（4 页限制），则超出约 1 页。\n- 大量实质性内容（per-task decomposition、seed robustness、data scaling ablation、capacity scaling、cross-model verification、failure mode analysis、threshold routing）均被放入 Appendix，正文缺乏对这些关键结果的充分讨论。\n- 建议：将 Appendix B（Per-Task Decomposition）、F（Seed Robustness + Data Scaling）、G（Capacity Scaling）的核心内容提升至正文；Discussion 部分目前仅 ~0.5 页需大幅扩展。\n\n**N2** [critical] 核心发现的新颖性不足：DAF 是代数恒等式，r=0.97 是其数学推论\n- DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数。P=100 时 DAF=90.4%，P=10 时 DAF=50.4%，P=0 时 DAF=7.5%。\"90.4%\" 完全取决于 ScienceWorld 的 P=100 设定。\n- 论文的两个核心量化结果——DAF=90.4% 和 r=0.97——都不是独立的实证发现，而是环境参数设定的代数后果。\n- 建议：重新组织叙事以 penalty-independent 的 78.9% label fraction 为 primary metric，将 DAF 降级为 supplementary。\n\n**N3** [critical] 单一环境 + 有限 task 覆盖削弱 generalization claim\n- 核心分析仅覆盖 ScienceWorld 30 个 task types 中的 11 个（36.7%），245 episodes，单一 backbone。\n- MATH 是 null result，ALFWorld 发现完全不同的 mechanism，Llama pilot 仅 70 episodes。\n- Contribution 3 不构成独立贡献：一个 null result + 一个 different mechanism + 一个 70-episode pilot = boundary conditions，不是 replication。\n- 建议：降级 Contribution 3 的措辞；最理想是增加 NetHack/Crafter 的 replication。\n\n## Should-Fix 问题\n\n**W1** [warning] Abstract 过度密集，数字堆砌（~15 个数字/统计量）\n**W2** [warning] Safe RL 覆盖严重不足（仅 Garcia 2015 + CRPO 2021）\n**W3** [warning] SCI 指标贡献不清晰：仅使用一次，本质是 Gini coefficient 的 rename\n**W4** [warning] Algorithm 1 形式化程度与内容复杂度不匹配（3-case 判断用 8 行伪代码）\n**W5** [warning] 缺少 LLM agent failure mode 分析的相关引用\n**W6** [warning] Router training 负面结果的解释不完整\n\n## 小问题\n1. Title 不一致（\"a\" vs \"the\" dominant）\n2. Reference 格式不统一\n3. Figure 2 位置不够突出\n4. N=275 vs N=245 不一致\n5. 写作风格干净无 AI 痕迹\n6. Appendix 内容分配不合理\n\n## 缺失引用\nSafe RL 方法论（Altman 1999, CPO, Safety Gymnasium）、LLM agent failure analysis、MoE routing 基础文献、Hallucination in grounded settings、FrugalGPT/Hybrid LLM\n\n## 审稿人提出的问题\nQ1: P=1 时 DAF≈8.5%，是否仍能得出 \"death avoidance is dominant\" 的结论？\nQ2: 54/75 death-asymmetry labels 移除 death penalty 后变为 tie，是否说明 30-step budget 过于苛刻？\nQ3: 排除 63% task types 后，发现是否高度依赖 30-step 设置？\nQ4: ALFWorld 的 \"deterministic modality\" 定义与 ScienceWorld 根本不同，框架比较是否有概念混淆？"
  }
}
```

</details>

---


### Tool result

_source line 979 · 2026-05-17T14:35:50.896076+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 34321
}
```

</details>

---


### Tool call

_source line 980 · 2026-05-17T14:35:51.047067+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注你们在以下几个问题上是否存在分歧：\n1. DAF tautology 的程度（R1 的 N1 vs 你的 N2）— R1 更强调 \"predictability analysis\"\n2. 统计推断可靠性（R1 的 N2）— 你未单独提出，是否同意？\n3. Router confounds（R1 的 W1）vs 你的 W6 — 谁的分析更深入？\n4. Episode-level mislabeling 量化（R1 的 W2）— 你未提出，是否同意？\n5. 总体评分差异（R1 给 3.0 vs 你给 2.5）— 差异原因是什么？\n\n---\n\n# Reviewer 1 完整审稿报告\n\n**Overall**: 3.0 / 5 (Findings)\n\n## 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心框架逻辑自洽，论文对多个数学性质有诚实的 self-acknowledgment；但 DAF 与 P 的数学耦合使核心发现的经验性贡献被削弱，cluster bootstrap K=11 远低于 K≥40 阈值，router 实验存在多个 confound |\n| Excitement | 2.5/5 | \"routing signal 的本质是什么\"这个问题有价值，但答案在了解环境惩罚结构后并不出人意料；框架可迁移性尚未充分验证 |\n| Reproducibility | 4.0/5 | Appendix 提供完整超参数、seed、数据划分细节；承诺 release code/data；Algorithm 1 可直接复现 |\n| Reviewer Confidence | 4/5 | 熟悉 LLM agent 评估、counterfactual 方法和 bootstrap 统计推断 |\n\n## Must-Fix 问题\n\n**N1** [critical] DAF 的核心发现与环境惩罚结构存在部分 tautology，论文 framing 仍然过度强调\"经验发现\"\n- DAF = δP/(δP + Δ_nd)。当 P=100 而 Δ_nd=2.84 时，这个高值主要由 P/Δ_nd 的比值决定。\n- 当 internal 策略死亡率是 deterministic 的 2.6 倍（42.9% vs 16.3%），且死亡惩罚是典型分数差异的 35 倍（100 vs ~2.84），死亡主导 routing signal 是从环境参数即可预测的结论。\n- penalty-independent 指标（78.9%）更有信息量，但 Algorithm 1 的设计将 death asymmetry 置于 score comparison 之前，论文应讨论这一设计选择的影响。\n- 建议增加 \"predictability analysis\"：给定已知死亡率差异和 P，DAF 预期值是多少，实际值偏离多少？\n\n**N2** [critical] 统计推断的可靠性不足\n- (a) Cluster bootstrap K=11 远低于 Cameron et al. 2008 的 K≥40 门槛，覆盖率远低于名义 95%\n- (b) Episode-level bootstrap 假设 245 个 episode 独立，但同一 task type 内的 episode 共享 task structure\n- (c) Per-task 样本量 n=20，chemistry-mix CI [-5.0, 48.6] 跨越零点，但论文以\"10 of 11 types exhibit DAF=100%\"呈现\n- (d) Llama pilot N=70，7 tasks，每 task 仅 10 episodes，0 internal-preferred 只能排除上界约 4.2%\n- 建议：对 cluster bootstrap 不可靠性做更诚实的讨论；Llama pilot 降级为 anecdotal evidence\n\n**N3** [critical] 跨环境证据不足以支撑 Contribution 3\n- 三个跨环境分析中没有一个构成 DAF 框架的真正 replication\n- MATH 验证 predicted null（弱检验）；ALFWorld modality 定义根本不同；Llama pilot 样本量过小\n- 最关键缺失：没有第二个具有 catastrophic failure 的环境\n- 建议：降级 Contribution 3 措辞，或增加 NetHack/Crafter replication\n\n## Should-Fix 问题\n\n**W1** [warning] Router 训练实验存在多个 confound\n- (a) Paraphrase augmentation 不是真正的 data scaling，但论文仍断言\"confirm this is structural\"\n- (b) 4B end-to-end 使用 N=275 vs baselines N=245，引入比较 confound\n- (c) 1.7B non-monotonic dip（episode-level 43.1%）未被解释\n\n**W2** [warning] Episode-level label → step-level training 的 mismatch 未被量化\n- 如果 internal 策略在 step 20 死亡（30-step episode），前 19 步都被标记为 det-preferred\n- 建议计算 \"potentially mislabeled step fraction\"\n\n**W3** [warning] SCI 的方法贡献与实际使用不成比例\n- 在 Method §2.4 完整定义但全文仅使用一次\n- K=11 计算 Gini 系数的统计意义有限\n- 建议降级到 Appendix\n\n**W4** [warning] 论文正文仅约 5 页，显著低于 long paper 的 8 页限制\n\n## 小问题\n- 标题 \"a\" vs \"the\" 不一致\n- Table 1 负分需要解释\n- Figure 2（signal_reversal）未包含 ALFWorld\n- Gajcin (2023) 引用需核实\n\n## 缺失引用\nVoyager (Wang et al., 2023)、Off-policy evaluation/OPE 文献（Precup et al. 2000, Jiang & Li 2016）、Distribution shift in imitation learning\n\n## 主要优势\n1. 研究问题有价值且定义清晰\n2. 论文学术诚实度异常高\n3. Counterfactual framework 设计合理\n4. MATH negative contrast 有说服力\n5. Appendix 分析深度充实"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注你们在以下几个问题上是否存在分歧：\n1. DAF tautology 的程度（R1 的 N1 vs 你的 N2）— R1 更强调 \"predictability analysis\"\n2. 统计推断可靠性（R1 的 N2）— 你未单独提出，是否同意？\n3. Router confounds（R1 的 W1）vs 你的 W6 — 谁的分析更深入？\n4. Episode-level mislabeling 量化（R1 的 W2）— 你未提出，是否同意？\n5. 总体评分差异（R1 给 3.0 vs 你给 2.5）— 差异原因是什么？\n\n---\n\n# Reviewer 1 完整审稿报告\n\n**Overall**: 3.0 / 5 (Findings)\n\n## 官方维度打分\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心框架逻辑自洽，论文对多个数学性质有诚实的 self-acknowledgment；但 DAF 与 P 的数学耦合使核心发现的经验性贡献被削弱，cluster bootstrap K=11 远低于 K≥40 阈值，router 实验存在多个 confound |\n| Excitement | 2.5/5 | \"routing signal 的本质是什么\"这个问题有价值，但答案在了解环境惩罚结构后并不出人意料；框架可迁移性尚未充分验证 |\n| Reproducibility | 4.0/5 | Appendix 提供完整超参数、seed、数据划分细节；承诺 release code/data；Algorithm 1 可直接复现 |\n| Reviewer Confidence | 4/5 | 熟悉 LLM agent 评估、counterfactual 方法和 bootstrap 统计推断 |\n\n## Must-Fix 问题\n\n**N1** [critical] DAF 的核心发现与环境惩罚结构存在部分 tautology，论文 framing 仍然过度强调\"经验发现\"\n- DAF = δP/(δP + Δ_nd)。当 P=100 而 Δ_nd=2.84 时，这个高值主要由 P/Δ_nd 的比值决定。\n- 当 internal 策略死亡率是 deterministic 的 2.6 倍（42.9% vs 16.3%），且死亡惩罚是典型分数差异的 35 倍（100 vs ~2.84），死亡主导 routing signal 是从环境参数即可预测的结论。\n- penalty-independent 指标（78.9%）更有信息量，但 Algorithm 1 的设计将 death asymmetry 置于 score comparison 之前，论文应讨论这一设计选择的影响。\n- 建议增加 \"predictability analysis\"：给定已知死亡率差异和 P，DAF 预期值是多少，实际值偏离多少？\n\n**N2** [critical] 统计推断的可靠性不足\n- (a) Cluster bootstrap K=11 远低于 Cameron et al. 2008 的 K≥40 门槛，覆盖率远低于名义 95%\n- (b) Episode-level bootstrap 假设 245 个 episode 独立，但同一 task type 内的 episode 共享 task structure\n- (c) Per-task 样本量 n=20，chemistry-mix CI [-5.0, 48.6] 跨越零点，但论文以\"10 of 11 types exhibit DAF=100%\"呈现\n- (d) Llama pilot N=70，7 tasks，每 task 仅 10 episodes，0 internal-preferred 只能排除上界约 4.2%\n- 建议：对 cluster bootstrap 不可靠性做更诚实的讨论；Llama pilot 降级为 anecdotal evidence\n\n**N3** [critical] 跨环境证据不足以支撑 Contribution 3\n- 三个跨环境分析中没有一个构成 DAF 框架的真正 replication\n- MATH 验证 predicted null（弱检验）；ALFWorld modality 定义根本不同；Llama pilot 样本量过小\n- 最关键缺失：没有第二个具有 catastrophic failure 的环境\n- 建议：降级 Contribution 3 措辞，或增加 NetHack/Crafter replication\n\n## Should-Fix 问题\n\n**W1** [warning] Router 训练实验存在多个 confound\n- (a) Paraphrase augmentation 不是真正的 data scaling，但论文仍断言\"confirm this is structural\"\n- (b) 4B end-to-end 使用 N=275 vs baselines N=245，引入比较 confound\n- (c) 1.7B non-monotonic dip（episode-level 43.1%）未被解释\n\n**W2** [warning] Episode-level label → step-level training 的 mismatch 未被量化\n- 如果 internal 策略在 step 20 死亡（30-step episode），前 19 步都被标记为 det-preferred\n- 建议计算 \"potentially mislabeled step fraction\"\n\n**W3** [warning] SCI 的方法贡献与实际使用不成比例\n- 在 Method §2.4 完整定义但全文仅使用一次\n- K=11 计算 Gini 系数的统计意义有限\n- 建议降级到 Appendix\n\n**W4** [warning] 论文正文仅约 5 页，显著低于 long paper 的 8 页限制\n\n## 小问题\n- 标题 \"a\" vs \"the\" 不一致\n- Table 1 负分需要解释\n- Figure 2（signal_reversal）未包含 ALFWorld\n- Gajcin (2023) 引用需核实\n\n## 缺失引用\nVoyager (Wang et al., 2023)、Off-policy evaluation/OPE 文献（Precup et al. 2000, Jiang & Li 2016）、Distribution shift in imitation learning\n\n## 主要优势\n1. 研究问题有价值且定义清晰\n2. 论文学术诚实度异常高\n3. Counterfactual framework 设计合理\n4. MATH negative contrast 有说服力\n5. Appendix 分析深度充实"
  }
}
```

</details>

---


### Tool result

_source line 981 · 2026-05-17T14:35:52.356287+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1309
}
```

</details>

---


### Assistant

_source line 982 · 2026-05-17T14:35:59.278688+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 91

## Round 91

2 recorded events


### User

_source line 983 · 2026-05-17T14:36:01.752019+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿报告已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。

三个 critical 问题：
1. DAF 核心发现与环境惩罚结构存在部分 tautology，Abstract/Introduction 的 framing 仍过度强调"经验发现"
2. 统计推断可靠性不足（cluster bootstrap K=11 远低于 K≥40 门槛、per-task n=20、Llama pilot N=70）
3. 跨环境证据不足以支撑 Contribution 3（无第二个 catastrophic-failure 环境的 replication）

四个 warning 问题：router 实验 confounds（伪 data scaling、N 不一致、1.7B dip 未解释）、episode→step mislabeling 未量化、SCI 方法贡献与使用不成比例、正文仅约 5 页（long paper 限制 8 页）。

论文最大优势是异常高的学术诚实度和清晰的研究问题定义。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 984 · 2026-05-17T14:36:16.434477+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 92

## Round 92

2 recorded events


### User

_source line 985 · 2026-05-17T14:37:36.058296+00:00_

[Reviewer 1 审稿结果]:
逐条回应 Reviewer 2 的审稿意见如下。

---

## 交叉回应：Reviewer 1 对 Reviewer 2 审稿意见

### Must-Fix 问题

**[AGREE with downgrade] R2-N1: 正文篇幅严重不足**

同意正文约 5 页远低于 8 页限制，且 Appendix B (per-task decomposition)、E (penalty sensitivity)、F (seed robustness + data scaling)、G (capacity scaling) 中的内容对理解核心 claim 至关重要。我在自己的审稿中将此列为 W4 (warning) 而非 critical，理由是：所有分析都已完成并呈现在附录中，这是组织结构问题而非内容缺失，作者只需将内容上移即可修复，不需要新实验。但 R2 将其列为 critical 也有道理——审稿人不应需要翻阅附录才能评估论文的核心 claim。我倾向于将其定级为 **strong warning / borderline critical**：严重影响可读性和评审体验，但不构成方法论缺陷。

**[AGREE] R2-N2: DAF 的新颖性不足**

这与我的 N1 高度一致。我们的诊断几乎相同：DAF=90.4% 和 r=0.97 是环境参数 P=100 的代数后果，不是独立的经验发现。R2 提出的具体建议（以 penalty-independent 的 78.9% 为 primary metric，DAF 降级为 supplementary）与我的建议方向一致。

但我与 R2 有一个程度上的分歧：R2 的 Excitement 评分为 2.0，认为框架"方法论贡献有限"。我给了 2.5，理由是：(1) 78.9% 这个 penalty-independent 数字确实有信息量——它说明在 95 个 non-tie episode 中，75 个的 routing preference 来自一个策略存活而另一个死亡，这个比例不是从环境参数能直接预测的，需要实际运行实验才知道；(2) Abstract/Introduction 中论文用 97.4% step-level tie rate 论证了 per-step oracle labeling 在 sparse-reward 环境中失效（§2.1），这个 methodological insight 对后续工作有指导价值。

**[AGREE] R2-N3: 单一环境 + 有限覆盖削弱 generalization**

与我的 N3 完全一致。R2 对 Contribution 3 的评估（"一个 null result + 一个 different mechanism + 一个 70-episode pilot = boundary conditions，不是 replication"）准确概括了问题。我在 N3 中提出了相同的判断。

---

### Should-Fix 问题

**[AGREE] R2-W1: Abstract 数字堆砌**

我未单独标记此问题，但 R2 的观察是准确的。重新审视 Abstract：78.9%, 75 of 95, 90.4%, P=100, r=0.97, 59.0%, 4B, N=795, p=0.81, N=135——在约 200 词中嵌入了 10+ 个统计量。这使得 Abstract 读起来像 results summary 而非一个有说服力的故事。作为对照，ACL/EMNLP 近年高分论文的 Abstract 通常仅保留 2-3 个最关键的数字。这个问题与论文 CLAUDE.md 中 §二（Abstract 写作规范 §2.2）的"禁止堆砌数据"原则直接冲突。但我将此视为写作问题而非方法论问题，不影响 Soundness 评分。

**[PARTIALLY AGREE] R2-W2: Safe RL 覆盖不足**

R2 认为 Safe RL 覆盖"严重不足"（仅 Garcia 2015 + CRPO 2021），建议增加 Altman 1999, CPO, Safety Gymnasium。我同意可以补充 1-2 篇经典文献（特别是 constrained MDP 方向），但不同意"严重"的判断。论文的贡献是诊断性的（揭示 routing signal 的构成），不是提出新的 safe RL 算法。Safe RL 在 Related Work 和 Discussion 中是 positioning 工具（"routing as safety problem"），不是核心比较对象。Garcia (2015) 作为 survey 已经覆盖了理论基础。

具体而言：R2 建议的 Safety Gymnasium 是一个 benchmark，与 ScienceWorld 解决的是不同问题；CPO (Achiam et al., 2017) 是 safe RL 的方法论贡献，对论文的 counterfactual diagnostic 框架没有直接方法论关联。Altman (1999) 的 constrained MDP 理论框架可能更相关，因为论文本质上在分析一个有 safety constraint（避免死亡）的 routing decision，但这也不是必须引用。

**[AGREE] R2-W3: SCI 贡献不清晰**

与我的 W3 完全一致。R2 的"本质是 Gini coefficient 的 rename"是精准的概括。我在 W3 中也指出了 K=11 时 Gini 系数的统计意义有限，且"top-3 tasks account for 39.8%"传达了相同信息。双方均建议降级至 Appendix。

**[REBUT] R2-W4: Algorithm 1 过度形式化**

R2 认为"3-case 判断用 8 行伪代码"是 over-formalization。我不同意。

理由：
1. Algorithm 1 是论文 Contribution 1 的核心——"A formal episode-level counterfactual framework (Algorithm 1)"是 Introduction 第一条 contribution 的字面内容。如果将其降级为文本描述，Contribution 1 的"formal framework"claim 失去锚点。
2. 虽然逻辑简单，但 death-aware priority order（lines 5-8 在 lines 11-14 之前）是一个需要明确指定的设计选择。如 §3.1 所示，78.9% 的 penalty-independent 指标直接依赖于这个优先级设定。如果改为 score-first，在 P=100 时结果不变（因为 -100 自动使存活策略得分更高），但在 P 较小时结果会不同（参见 Appendix E, Table 5 中 P=10 时 DAF=50.4%）。这个 boundary condition 需要形式化来保证 reproducibility。
3. 与写作规范一致性：ACL/EMNLP 论文中，用 Algorithm 环境呈现核心 procedure 是标准做法，即使逻辑简单。过度简化反而可能导致 ambiguity（如 death-tie 的处理：line 7-8 的 both-dead → no_preference，而非 random）。

**[AGREE] R2-W5: 缺少 LLM agent failure mode 分析的引用**

合理。论文在 Appendix H (Failure Mode Analysis) 中讨论了 state hallucination 导致的 cascading errors，但 Related Work 中未引用 LLM agent failure/hallucination in grounded settings 的文献。这是一个 gap。

**[AGREE] R2-W6: Router training 负面结果解释不完整**

与我的 W1 一致。特别是 1.7B 的 non-monotonic episode-level dip（43.1%，低于 0.6B 的 50.7%，Table 4）和 augmentation-based "data scaling"的 framing 问题。

---

### 小问题

**[AGREE]** Title 不一致、N=275 vs N=245——我均在自己的审稿中标记了。

**[AGREE]** Reference 格式和 Figure 2 位置——合理的 presentation 建议。

**[AGREE]** "写作风格干净无 AI 痕迹"——同意，论文的写作质量本身是优势。

---

### R2 提出的问题

**Q1 (P=1 时 DAF≈8.5%)**：这个问题精准地暴露了 DAF 的 P 依赖性。论文 Appendix E Table 5 提供了 P=0 到 P=500 的 sensitivity analysis，P=0 时 DAF=7.5%（CI [-36.7, 83.1]）。这意味着如果不考虑 death penalty 的 magnitude，death avoidance 几乎不是"dominant"的。论文的自洽回应是指向 78.9% penalty-independent metric，但这凸显了 DAF 作为 primary metric 的问题（支持 R2-N2 和我的 N1）。

**Q2 (54/75 labels 移除 penalty 后变为 tie)**：这是一个被低估的重要观察。§3.1 报告"54 (72.0%) reduce to ties when the death penalty is removed entirely: in those episodes, both modalities score zero without death"。这意味着在大多数 death-asymmetry episode 中，存活策略也得了零分——两种策略在这些 task instance 上都没有实质进展，唯一的区别是一个死了一个没死。这确实暗示 30-step budget 可能过于紧张，值得讨论。但也可以说这反而加强了核心发现：当两种策略都无法完成任务时，存活/死亡是唯一有意义的区分信号。

**Q3 (63% task 排除 + 30-step 依赖)**：论文 Appendix B 说明排除的原因是"both strategies typically time out within 30 steps"，即这些 task 下两种策略都没有 routing signal。论文还提供了 anti-cherry-picking 论证（included vs excluded task types 的 deterministic death rate 相当：17.8% vs 14.9%）。但 R2 的质疑仍然有效：如果增加 step budget，某些 excluded tasks 可能开始出现 routing signal，且这些新的 routing signal 可能不是 death-dominated 的。论文在 Limitations 中提及了这一点（"increasing the step budget could surface additional signal"），但未量化。

**Q4 (ALFWorld modality 定义不一致)**：与我的 N3 和 R2-N3 一致。论文自己在 §3.5 承认 ALFWorld 是"information asymmetry rather than a computation mode switch"。这使得跨环境比较在概念层面存在不可通约性。

---

### 总体评分差异：3.0 vs 2.5

我维持 **3.0 (Findings)**，与 R2 的 2.5 (Borderline Findings) 有 0.5 分差距。分歧来源：

1. **Excitement 差异（2.5 vs 2.0）**：R2 认为核心发现"在直觉上不令人意外"。我认为虽然 DAF 值本身是代数后果，但几个经验性发现仍有价值：(a) 97.4% step-level tie rate 揭示 per-step oracle 在 sparse-reward 环境中的根本失效；(b) 78.9% penalty-independent label fraction 是需要实验才能获得的经验数字；(c) MATH 的 null result (p=0.81, N=795) 是一个 well-powered 的负面对照。这些加在一起构成了对 LLM agent routing 社区的有用诊断信息。

2. **篇幅问题的定级差异**：R2 将篇幅列为 N1 (critical)，我列为 W4 (warning)。如果将篇幅视为方法论问题，它不影响论文结论的可靠性；如果视为 presentation/completeness 问题，它很严重但可快速修复。我不认为 presentation 问题应该在 Overall Assessment 中与方法论缺陷同等权重。

3. **对学术诚实度的加分**：论文对自身局限的主动 acknowledgment（r=0.97 是代数推论、DAF 随 P 单调递增是数学性质、cluster bootstrap K<40、augmentation ≠ real scaling）在 ARR 提交中非常罕见。ARR reviewer guidelines 明确反对 heuristic H1（"dismissing intuitive-seeming findings as not surprising"）和 H6（"penalizing negative results"）。论文的 router training 是一个诚实的负面结果，其价值在于诊断而非性能提升。

4. **Findings vs Borderline Findings 的分界**：3.0 意味着"论文在当前状态下有足够的贡献可被 Findings 接收"；2.5 意味着"需要额外工作才可能达到 Findings"。我认为框架贡献（Algorithm 1 + dual metrics）+ ScienceWorld 的完整分析（245 episodes, bootstrap CIs, penalty sensitivity, seed robustness）+ MATH negative contrast 已经达到 Findings 的门槛，即使 cross-environment evidence 和 framing 需要改进。

**最终判断**：两份审稿在核心问题上高度一致（DAF tautology、cross-environment 证据不足、SCI 价值有限、篇幅问题）。评分差异主要来自对 excitement 和 presentation 问题权重的不同判断，而非对方法论问题的分歧。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 986 · 2026-05-17T14:37:44.025363+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 93

## Round 93

6 recorded events


### User

_source line 987 · 2026-05-17T14:37:54.670596+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

## Must-Fix 问题

**[AGREE] R1-N1: DAF tautology + 建议 predictability analysis**

同意 R1 的核心判断，且认为 R1 提出的 "predictability analysis" 建议比我的 N2 更具建设性。

我的 N2 指出了同一问题（DAF=90.4% 和 r=0.97 都是代数后果），但我的修改建议偏向叙事重组（以 78.9% penalty-independent label fraction 为 primary metric）。R1 的建议更进一步：如果给定已知的 δ=0.265 和 P=100，DAF 的 predicted value 是 δP/(δP+Δ_nd) = 26.5/(26.5+2.84) = 90.3%，与实测 90.4% 几乎完全吻合。这意味着 DAF 分析没有产生超出 "知道死亡率差异和惩罚幅度" 之外的新信息。要求作者量化 predicted vs. observed deviation 是一个具体且可操作的建议，能让论文的 empirical contribution 边界更清晰。

R1 额外提出的 Algorithm 1 priority ordering 的影响分析，我也认为有价值。论文 §3.1 提到 75 个 death-asymmetry labels 中有 54 个（72%）在去除 penalty 后变为 tie（both score 0），这说明 Algorithm 1 的 death-first priority 确实在这些 episode 上产生了决定性影响。但需注意：这个 priority ordering 在概念上是合理的（catastrophic failure 的代价远超 score difference），只是其对最终统计量的 mechanical contribution 需要被更明确地讨论。

**[AGREE] R1-N2: 统计推断可靠性不足**

我在 Round 1 审稿中未将此单独列为 critical issue，这是一个遗漏。R1 的四个子点均成立：

(a) **Cluster bootstrap K=11**：论文自己引用了 Cameron et al. 2008 的 K≥40 门槛（§3.1 最后一段），但仍报告了 cluster bootstrap 95% CI [73.3%, 100%] 并声称 "lower bound nonetheless remains well above 50%"。用自己承认不可靠的方法得出的 CI 来支撑 claim 是不严谨的。

(b) **Episode 独立性假设**：同一 task type 内的 episode 共享 task structure（初始状态空间、可用 action 集、death trigger 条件）。标准 bootstrap 假设 iid，但 ScienceWorld 中同一 task type 的 episode 之间存在 within-cluster correlation。论文做了 cluster bootstrap 作为 sensitivity analysis，但如上所述 K=11 使其不可靠。

(c) **Per-task 小样本**：chemistry-mix（N=20）的 CI [-5.0, 48.6] 跨零是直接证据。论文用 "10 of 11 types exhibit DAF=100%" 来叙事，但这 10 个 type 中部分的 per-task CI 可能也不够 tight（如 chem-mix 和 find-animal 各仅 20 episodes）。

(d) **Llama pilot**：N=70，7 tasks，0 internal-preferred。R1 指出 0/70 只能排除 internal-preferred rate 上界约 4.2%（binomial 95% upper bound），这个精度不足以支撑 "directional consistency across model families" 的 claim。论文 §3.4 已说 "preliminary pilot demonstrates directional consistency... not full framework replication"，但 Abstract 和 Contribution 3 的措辞没有匹配这个 caveat。

补充一点：R1 未提及但值得注意的是，论文的 primary bootstrap（B=10,000, N=245 episodes）对 DAF 的 CI 是 [81.6%, 98.8%]。这个 CI 的 width（~17pp）说明即使在当前样本下，DAF 的估计也有相当的 uncertainty。论文 headline 用点估计 90.4% 而非 CI 来叙事，稍有 cherry-picking 嫌疑。

**[AGREE] R1-N3: 跨环境证据不足以支撑 Contribution 3**

与我的 N3 完全一致。R1 和我独立得出相同结论：MATH null + ALFWorld different mechanism + Llama pilot = boundary conditions, not replication。R1 补充了一个我未提及的点：ALFWorld 的 modality 定义（admissible actions = action space pruning）与 ScienceWorld 的 modality 定义（ground-truth observations = state estimation replacement）根本不同——这意味着把两者放在 "same framework" 下比较存在概念混淆。我在 Round 1 的 "Questions" 第 4 条提过这个问题，但 R1 在 N3 中将其作为 contribution 不足的直接证据更有说服力。

---

## Should-Fix 问题

**[AGREE with nuance] R1-W1: Router 训练 confounds — 与我的 W6 互补**

R1 的分析更聚焦于实验设计中的 specific confounds：
- (a) Paraphrase augmentation ≠ real data scaling：完全同意。论文 Appendix F 自己指出 "paraphrase augmentation inflates the majority class (89.6%→97.7%)"，这说明 augmentation 本身在制造 confound。论文的结论 "structural rather than data-limited" 缺乏 real-data scaling 的对照。
- (b) N=275 vs N=245：R1 正确识别了这个比较 confound（我仅将其列为小问题第 4 条）。
- (c) 1.7B non-monotonic dip：有效 concern。0.6B→1.7B episode-level accuracy 从 50.7% 降至 43.1%，然后 4B 跳至 59.0%。论文只说 "robust across seeds"，但没有解释机制。

我的 W6 则关注更 conceptual 的缺失：(a) episode-level → step-level 信息损失、(b) step-level oracle 对照缺失、(c) 更强 internal reasoning baseline 的讨论。两者分析角度不同但互补。

总体而言，R1 在 experimental confounds 的具体识别上更深入；我在 conceptual gaps 和 implications 讨论上更全面。

**[AGREE] R1-W2: Episode-level label → step-level mislabeling 未被量化**

这是一个我在 Round 1 中遗漏的重要问题。R1 的例子非常具体：如果 internal 策略在 step 20 死亡（30-step episode），前 19 步都被标记为 det-preferred，但这些步骤在 internal 策略下可能表现正常。

论文 Appendix A（Labeling Quality Audit）审计了 episode-level label 的质量，验证了 "zero labels depend on tie-breaking"。但这个 audit 完全在 episode level，没有回答 R1 的问题：在 step level，有多少 step 被 "不公平地" 标记？

补充量化思路：论文报告 internal 死亡率 42.9%（245 episodes），平均 episode 长度 ~30 steps。假设死亡平均发生在 step ~20（论文 Appendix G 提到 cascading errors），则约 42.9% × 19/30 ≈ 27% 的 internal-strategy steps 可能在死亡前表现正常却被标记为 det-preferred。这一数字足以解释 router 的 step-level 泛化困难。

**[AGREE] R1-W3: SCI 方法贡献与使用不成比例**

与我的 W3 完全一致。R1 补充了一个我未提及的点：K=11 计算 Gini 系数的统计意义有限。Gini 系数在样本量极小时（K=11 task types）的估计方差很大。同意降级到 Appendix 的建议。

**[AGREE] R1-W4: 篇幅不足**

与我的 N1 相同问题。我将其列为 Must-Fix (N1)，R1 列为 Should-Fix (W4)。我认为篇幅问题的严重性更接近 Must-Fix：5 页正文 vs 8 页限制的差距过大，不是小幅调整能解决的，且直接影响审稿人对论文贡献深度的判断。

---

## 小问题

**[AGREE] R1-小问题-1: 标题 "a" vs "the" 不一致** — 同我的小问题第 1 条。

**[AGREE] R1-小问题-2: Table 1 负分解释** — Table 1（§3.2）的 Score 列全部为负值（Always-Internal: -39.07, Always-Det: -9.47, Oracle: -6.58）。论文在 §2.1 提到 death penalty = -100，但未明确解释为什么即使最优策略（Oracle）的平均分也是负的。应补充说明：这是因为 Oracle 仍有 14.3% death rate（Table 1），这些 death episodes 的 -100 惩罚拉低了均分。

**[AGREE] R1-小问题-3: Figure 3 未包含 ALFWorld** — Figure 3（signal_reversal.pdf, §3.5）仅展示 ScienceWorld 和 MATH 的 label distribution。ALFWorld 作为 §3.5 的第三个环境，缺席于 Figure 3 确实是遗漏。

**[REBUT] R1-小问题-4: Gajcin (2023) 引用需核实**
R1 建议核实此引用。我查看了 references.bib：`gajcin2023counterfactual` 引用的是 Gajcin, Jasmina, "Counterfactual Explanations for Reinforcement Learning Agents," AAMAS 2023。这是一篇真实存在的论文（AAMAS 2023 的 doctoral consortium / extended abstract），引用格式正确。不需要修改。

---

## 缺失引用

**[AGREE] R1-缺失引用: Voyager** — 论文在 Related Work §4 提到 ScienceWorld/ALFWorld/AgentBench 作为 LLM agent environments，但 Voyager (Wang et al., 2023) 作为 ScienceWorld 上的重要 LLM agent 工作，确实应该引用。

**[AGREE with nuance] R1-缺失引用: OPE 文献** — Off-policy evaluation（Precup et al. 2000, Jiang & Li 2016）与本文的 counterfactual analysis 有方法论联系。不过本文的 counterfactual 是 prospective（run both strategies）而非 retrospective（从 logged data 估计），区别较大。建议在 Related Work 中简要对比 OPE vs. prospective counterfactual evaluation，而非作为 critical missing reference。

**[AGREE] R1-缺失引用: Distribution shift in imitation learning** — 论文引用了 DAgger (Ross et al., 2011) 处理 distribution shift，但在 Limitations 中对 distribution shift 的讨论只有一句话。考虑到 "training on pure-strategy trajectories but deploying mixed-strategy" 是该工作的核心 limitation，更充分的引用和讨论是合理的。

---

## 评分差异分析（R1: 3.0 vs R2: 2.5）

差异主要来自三个方面：

**1. 篇幅问题的权重不同**
我将篇幅不足列为 N1（Must-Fix），R1 列为 W4（Should-Fix）。我认为 5 页正文 vs 8 页限制不是 "修修补补" 能解决的，它反映出论文在 long paper 格式下贡献深度不足。如果大量 Appendix 内容搬回正文可以解决，那说明论文的 content 足够但 organization 有问题；但如果搬回后仍然不够充实（Discussion 部分确实偏浅），则说明 contribution 本身不够 long paper 水平。

**2. 方法论新颖性的评估**
R1 的 Excitement 2.5 略高于我的 2.0。我认为 episode-level paired comparison（run both strategies, compare outcomes）是实验设计的 standard practice，不构成 methodological contribution。DAF 是 simple ratio，SCI 是 Gini coefficient rename。R1 似乎对 "问题定位" 给予了更多 credit（"routing signal 的本质是什么" 这个问题本身有价值），我对此同意但认为 question 的价值不能完全弥补 answer 的 limited novelty。

**3. Negative results 的评价**
R1 的优势第 4 条强调 "MATH negative contrast 有说服力"。我同意 MATH null result 本身有价值，但它只验证了一个 obvious prediction（没有 death penalty → 没有 death-driven routing signal）。更有说服力的 negative result 应该是在一个 *有* catastrophic failure 但 death avoidance *不* dominant 的环境中。

**综合评估：** R1 给 3.0（Findings 可接收）有其道理——论文执行质量好、分析诚实、实际问题有意义。我给 2.5（Borderline Findings）是因为我对 methodological novelty 和 contribution depth 的要求更严格，加上篇幅问题让我对 long paper 可行性持更大保留。

如果论文解决篇幅问题 + 增加第二个 catastrophic-failure environment replication，我愿意将评分上调至 3.0-3.5。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-17T14:40:20.616515+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "\n- id: \"R13-N1\"\n  summary: \"DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果（P=10 时 DAF=50.4%）。78.9% penalty-independent metric 更有信息量但在叙事中不够突出。R1 建议 predictability analysis 量化 predicted vs observed deviation。\"\n  action_items:\n    - round: 13\n      action: \"以 78.9% penalty-independent label fraction 为 primary metric，DAF 降级为 supplementary；增加 predictability analysis；Abstract/Introduction 中降低对 DAF 数值的依赖\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11、per-task n=20、Llama pilot N=70\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. (a) Cluster bootstrap K=11 远低于 Cameron et al. K≥40 门槛，CI [73.3%, 100%] 不可靠; (b) episode 独立性假设不满足; (c) per-task n=20 CI 极宽，chemistry-mix CI跨零; (d) Llama pilot N=70 只能排除 internal-preferred rate 上界约 4.2%。论文 headline 用点估计而非 CI 叙事有 cherry-picking 嫌疑。\"\n  action_items:\n    - round: 13\n      action: \"对 cluster bootstrap K=11 做更诚实讨论或使用替代方法（wild cluster bootstrap / permutation test）；Llama pilot 降级为 anecdotal evidence；per-task 结果报告时体现 uncertainty；headline 使用 CI 而非仅点估计\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-N3\"\n  summary: \"跨环境证据不足以支撑 Contribution 3——无第二个 catastrophic-failure 环境 replication\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. MATH 是 predicted null（弱检验）；ALFWorld modality 定义根本不同（information asymmetry vs computation mode）；Llama pilot 样本量过小。三者均不构成 DAF 框架的 replication。最关键缺失：无第二个具有 catastrophic failure 的环境（如 NetHack/Crafter）。\"\n  action_items:\n    - round: 13\n      action: \"降级 Contribution 3 措辞为 preliminary cross-environment evidence；最理想：增加 NetHack/Crafter 的 replication\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求（约 5 页 vs 8 页限制）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 列 critical，R1 列 warning。共识：大量关键证据（per-task decomposition、penalty sensitivity、capacity scaling、seed robustness）藏在 Appendix，正文缺乏充分讨论。Discussion 仅 ~0.5 页。分歧仅在 severity 定级。\"\n  action_items:\n    - round: 13\n      action: \"将 Appendix B（Per-Task Decomposition）、E（Penalty Sensitivity）、F（Capacity Scaling）核心内容提升至正文；大幅扩展 Discussion\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound：伪 data scaling、N 不一致、1.7B dip 未解释\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. (a) Paraphrase augmentation ≠ real data scaling，但论文断言 'structural rather than data-limited'; (b) 4B end-to-end N=275 vs baselines N=245; (c) 1.7B episode-level 43.1% 的 non-monotonic dip 未解释。\"\n  action_items:\n    - round: 13\n      action: \"将 'data scaling' 改为 'augmentation scaling' 并调整结论；在 shared task set 上统一比较；对 1.7B dip 提供可检验 hypothesis\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. 如 internal 在 step 20 死亡，前 19 步被标为 det-preferred 但可能表现正常。R2 估算约 27% 的 step-level labels 可能是 mislabeled，足以解释 router 泛化困难。\"\n  action_items:\n    - round: 13\n      action: \"计算并报告 potentially mislabeled step fraction\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W4\"\n  summary: \"SCI（Signal Concentration Index）方法贡献与实际使用不成比例\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. SCI 是 Gini coefficient 的 rename，Method §2.4 完整定义但全文仅使用一次（SCI=0.2147）。K=11 时 Gini 估计方差大。'top-3 tasks account for 39.8%' 传达相同信息。\"\n  action_items:\n    - round: 13\n      action: \"降级 SCI 到 Appendix，主文用描述性语言替代\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌（~15 个统计量），读起来像 results summary\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. R2 提出，R1 AGREE。约 200 词中嵌入 10+ 统计量，应减至 5-6 个关键数字。\"\n  action_items:\n    - round: 13\n      action: \"精简 Abstract 至 5-6 个关键数字，聚焦 why this matters\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出 Safe RL 覆盖不足（仅 Garcia 2015 + CRPO 2021），R1 部分同意（不认为'严重'但承认可补 1-2 篇）。双方均认为缺少 LLM agent failure mode 分析的引用。建议补充 constrained MDP (Altman 1999)、Voyager、OPE 文献、grounded hallucination 相关工作。\"\n  action_items:\n    - round: 13\n      action: \"补充 Safe RL（Altman 1999 / CPO）、Voyager、LLM agent failure analysis 引用；简要对比 OPE vs prospective counterfactual\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整：conceptual gaps（更强 baseline 讨论、step-level oracle 对照缺失）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。Discussion 中缺乏对 router failure 根本原因的深入分析：在什么条件下 router 可能变得有用？更强 internal reasoning（Reflexion）可能改变结论？\"\n  action_items:\n    - round: 13\n      action: \"Discussion 中深入分析 router failure 原因和 boundary conditions\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m1\"\n  summary: \"Title 不一致：'a Dominant' vs 'the Dominant' — TeX 源码与渲染 PDF 不同\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 13\n      action: \"统一标题用词\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m2\"\n  summary: \"Figure 3（signal_reversal）仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. §3.5 讨论三个环境但 Figure 仅展示两个。\"\n  action_items:\n    - round: 13\n      action: \"补全 ALFWorld 数据到 Figure 3 或修改标题\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一：'and others' vs 完整作者列表混合\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n  action_items:\n    - round: 13\n      action: \"统一 bib 中作者列表格式\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Previously tracked issues (all resolved) ---\n\n- id: \"R11-C1\"\n  summary: \"Partial correlation (r=0.02, p=0.91, df=27) mathematically undefined — perfect collinearity when P is constant\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-C1: df=27 error.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Fixed by deleting partial correlation entirely.\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"本轮未提及，已修复确认。\"\n  action_items:\n    - round: 11\n      action: \"Delete all instances of partial correlation r=0.02, p=0.91, df=27.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"All instances deleted. Replaced with algebraic argument.\"\n  resolution_round: 11\n\n- id: \"R11-W1\"\n  summary: \"Em-dash (---) 泛滥 — AI writing signature\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"~20 instances across 6 tex files.\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"本轮未提及，R2 明确评价'写作风格干净无 AI 痕迹'，确认修复。\"\n  action_items:\n    - round: 11\n      action: \"Replace all explanatory em-dashes.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"All replaced. Round 13 confirms clean writing.\"\n  resolution_round: 11\n\n- id: \"R11-W2\"\n  summary: \"\\\\nolinenumbers violates ACL ARR review format\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"本轮未提及，PDF 渲染确认行号正常显示。\"\n  action_items:\n    - round: 11\n      action: \"Delete \\\\nolinenumbers.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Deleted.\"\n  resolution_round: 11\n\n- id: \"R11-W3\"\n  summary: \"Capacity scaling dual-reporting — two incompatible 1.7B numbers\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"本轮未提及 dual-reporting 问题。但新问题 R13-W2 识别出 1.7B non-monotonic dip 未被解释。\"\n  action_items:\n    - round: 11\n      action: \"Unify main text to 4-seed controlled.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Unified. New issue R13-W2 tracks remaining 1.7B explanation gap.\"\n  resolution_round: 11\n\n- id: \"R11-W4\"\n  summary: \"Cluster bootstrap K=11 below minimum cluster count\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"重新出现为 R13-N2 的子问题(a)。上轮修复（添加 Cameron 引用 + caveat）被认为不够充分——用不可靠方法的 CI 来支撑 claim 仍不严谨。\"\n  action_items:\n    - round: 11\n      action: \"Add Cameron et al. citation + caveat.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Citation and caveat added, but R13 reviewers found fix insufficient.\"\n  resolution_round: 11\n\n- id: \"R11-W5\"\n  summary: \"McNemar test input not clearly distinguished from routing labels\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"本轮未提及，修复确认。\"\n  action_items:\n    - round: 11\n      action: \"Add clarifying sentence.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Clarification added.\"\n  resolution_round: 11\n\n- id: \"R11-m1\"\n  summary: \"§4.1 and §4.5 paragraphs too dense\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Split into sub-paragraphs.\"\n  resolution_round: 11\n\n- id: \"R11-m2\"\n  summary: \"Abstract 78.9% vs DAF=90.4% distinction not intuitive\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"上轮修复确认。但新 issue R13-N1 要求更根本的叙事重组（78.9% 为 primary，DAF 降级）。\"\n  resolution: \"Added clarification. Superseded by R13-N1.\"\n  resolution_round: 11\n\n- id: \"R11-m3\"\n  summary: \"Mann-Whitney vs Wilcoxon signed-rank for reasoning depth ablation\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Confirmed unpaired design. Mann-Whitney correct.\"\n  resolution_round: 11\n\n- id: \"R10-C1\"\n  summary: \"df=27 statistical error in partial correlation\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Superseded by R11-C1. Partial correlation deleted.\"\n  resolution_round: 11\n\n- id: \"R10-C2\"\n  summary: \"Core finding novelty insufficient — DAF near-tautological\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Issue recurs as R13-N1. Previous 'fix'（78.9% as headline）was partial; R13 reviewers demand deeper restructuring including predictability analysis.\"\n  resolution: \"Framing restructured in R11, but R13 finds it insufficient. Superseded by R13-N1.\"\n  resolution_round: 11\n\n- id: \"R10-C3\"\n  summary: \"Single-environment evidence — no cross-env REPLICATION\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Issue recurs as R13-N3. Previous fix (scope downgrade) considered partial; still no second catastrophic-failure environment.\"\n  resolution: \"Contribution 3 scoped down in R11, but R13 finds it still insufficient. Superseded by R13-N3.\"\n  resolution_round: 11\n\n- id: \"R10-C4\"\n  summary: \"Data scaling ablation uses augmentation — cannot rule out real-data scarcity\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Issue partially recurs in R13-W2(a). Language was unified but Introduction still uses 'confirm this is structural'.\"\n  resolution: \"Language unified in R11. Residual framing issue tracked in R13-W2.\"\n  resolution_round: 11\n\n- id: \"R10-C5\"\n  summary: \"Capacity scaling confound — seeds mismatch\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Controlled 4-seed replication done.\"\n  resolution_round: 11\n\n- id: \"R10-W1\"\n  summary: \"Router failure does not 'validate' analytical framework\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-W2\"\n  summary: \"'Environment-agnostic' overclaim\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-W3\"\n  summary: \"Related work gaps\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Core gaps from R10 filled. New gaps identified in R13-W6 (Safe RL, LLM agent failure mode, Voyager, OPE).\"\n  resolution: \"Core gaps filled in R11. New gaps tracked in R13-W6.\"\n  resolution_round: 11\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "simgate-modular-routing",
    "issues_yaml": "\n- id: \"R13-N1\"\n  summary: \"DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果（P=10 时 DAF=50.4%）。78.9% penalty-independent metric 更有信息量但在叙事中不够突出。R1 建议 predictability analysis 量化 predicted vs observed deviation。\"\n  action_items:\n    - round: 13\n      action: \"以 78.9% penalty-independent label fraction 为 primary metric，DAF 降级为 supplementary；增加 predictability analysis；Abstract/Introduction 中降低对 DAF 数值的依赖\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-N2\"\n  summary: \"统计推断可靠性不足：cluster bootstrap K=11、per-task n=20、Llama pilot N=70\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. (a) Cluster bootstrap K=11 远低于 Cameron et al. K≥40 门槛，CI [73.3%, 100%] 不可靠; (b) episode 独立性假设不满足; (c) per-task n=20 CI 极宽，chemistry-mix CI跨零; (d) Llama pilot N=70 只能排除 internal-preferred rate 上界约 4.2%。论文 headline 用点估计而非 CI 叙事有 cherry-picking 嫌疑。\"\n  action_items:\n    - round: 13\n      action: \"对 cluster bootstrap K=11 做更诚实讨论或使用替代方法（wild cluster bootstrap / permutation test）；Llama pilot 降级为 anecdotal evidence；per-task 结果报告时体现 uncertainty；headline 使用 CI 而非仅点估计\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-N3\"\n  summary: \"跨环境证据不足以支撑 Contribution 3——无第二个 catastrophic-failure 环境 replication\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. MATH 是 predicted null（弱检验）；ALFWorld modality 定义根本不同（information asymmetry vs computation mode）；Llama pilot 样本量过小。三者均不构成 DAF 框架的 replication。最关键缺失：无第二个具有 catastrophic failure 的环境（如 NetHack/Crafter）。\"\n  action_items:\n    - round: 13\n      action: \"降级 Contribution 3 措辞为 preliminary cross-environment evidence；最理想：增加 NetHack/Crafter 的 replication\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W1\"\n  summary: \"正文篇幅严重不足 long paper 要求（约 5 页 vs 8 页限制）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 列 critical，R1 列 warning。共识：大量关键证据（per-task decomposition、penalty sensitivity、capacity scaling、seed robustness）藏在 Appendix，正文缺乏充分讨论。Discussion 仅 ~0.5 页。分歧仅在 severity 定级。\"\n  action_items:\n    - round: 13\n      action: \"将 Appendix B（Per-Task Decomposition）、E（Penalty Sensitivity）、F（Capacity Scaling）核心内容提升至正文；大幅扩展 Discussion\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W2\"\n  summary: \"Router 训练实验存在多个 confound：伪 data scaling、N 不一致、1.7B dip 未解释\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. (a) Paraphrase augmentation ≠ real data scaling，但论文断言 'structural rather than data-limited'; (b) 4B end-to-end N=275 vs baselines N=245; (c) 1.7B episode-level 43.1% 的 non-monotonic dip 未解释。\"\n  action_items:\n    - round: 13\n      action: \"将 'data scaling' 改为 'augmentation scaling' 并调整结论；在 shared task set 上统一比较；对 1.7B dip 提供可检验 hypothesis\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W3\"\n  summary: \"Episode-level label → step-level training 的 mislabeling 未被量化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. 如 internal 在 step 20 死亡，前 19 步被标为 det-preferred 但可能表现正常。R2 估算约 27% 的 step-level labels 可能是 mislabeled，足以解释 router 泛化困难。\"\n  action_items:\n    - round: 13\n      action: \"计算并报告 potentially mislabeled step fraction\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W4\"\n  summary: \"SCI（Signal Concentration Index）方法贡献与实际使用不成比例\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. SCI 是 Gini coefficient 的 rename，Method §2.4 完整定义但全文仅使用一次（SCI=0.2147）。K=11 时 Gini 估计方差大。'top-3 tasks account for 39.8%' 传达相同信息。\"\n  action_items:\n    - round: 13\n      action: \"降级 SCI 到 Appendix，主文用描述性语言替代\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W5\"\n  summary: \"Abstract 数字堆砌（~15 个统计量），读起来像 results summary\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. R2 提出，R1 AGREE。约 200 词中嵌入 10+ 统计量，应减至 5-6 个关键数字。\"\n  action_items:\n    - round: 13\n      action: \"精简 Abstract 至 5-6 个关键数字，聚焦 why this matters\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W6\"\n  summary: \"Safe RL 和 LLM agent failure mode 相关引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出 Safe RL 覆盖不足（仅 Garcia 2015 + CRPO 2021），R1 部分同意（不认为'严重'但承认可补 1-2 篇）。双方均认为缺少 LLM agent failure mode 分析的引用。建议补充 constrained MDP (Altman 1999)、Voyager、OPE 文献、grounded hallucination 相关工作。\"\n  action_items:\n    - round: 13\n      action: \"补充 Safe RL（Altman 1999 / CPO）、Voyager、LLM agent failure analysis 引用；简要对比 OPE vs prospective counterfactual\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-W7\"\n  summary: \"Router negative results 解释不完整：conceptual gaps（更强 baseline 讨论、step-level oracle 对照缺失）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。Discussion 中缺乏对 router failure 根本原因的深入分析：在什么条件下 router 可能变得有用？更强 internal reasoning（Reflexion）可能改变结论？\"\n  action_items:\n    - round: 13\n      action: \"Discussion 中深入分析 router failure 原因和 boundary conditions\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m1\"\n  summary: \"Title 不一致：'a Dominant' vs 'the Dominant' — TeX 源码与渲染 PDF 不同\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 13\n      action: \"统一标题用词\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m2\"\n  summary: \"Figure 3（signal_reversal）仅含 ScienceWorld 和 MATH，缺少 ALFWorld\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Consensus. §3.5 讨论三个环境但 Figure 仅展示两个。\"\n  action_items:\n    - round: 13\n      action: \"补全 ALFWorld 数据到 Figure 3 或修改标题\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R13-m3\"\n  summary: \"Reference 格式不统一：'and others' vs 完整作者列表混合\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。\"\n  action_items:\n    - round: 13\n      action: \"统一 bib 中作者列表格式\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Previously tracked issues (all resolved) ---\n\n- id: \"R11-C1\"\n  summary: \"Partial correlation (r=0.02, p=0.91, df=27) mathematically undefined — perfect collinearity when P is constant\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R10-C1: df=27 error.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Fixed by deleting partial correlation entirely.\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"本轮未提及，已修复确认。\"\n  action_items:\n    - round: 11\n      action: \"Delete all instances of partial correlation r=0.02, p=0.91, df=27.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"All instances deleted. Replaced with algebraic argument.\"\n  resolution_round: 11\n\n- id: \"R11-W1\"\n  summary: \"Em-dash (---) 泛滥 — AI writing signature\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"~20 instances across 6 tex files.\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"本轮未提及，R2 明确评价'写作风格干净无 AI 痕迹'，确认修复。\"\n  action_items:\n    - round: 11\n      action: \"Replace all explanatory em-dashes.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"All replaced. Round 13 confirms clean writing.\"\n  resolution_round: 11\n\n- id: \"R11-W2\"\n  summary: \"\\\\nolinenumbers violates ACL ARR review format\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"本轮未提及，PDF 渲染确认行号正常显示。\"\n  action_items:\n    - round: 11\n      action: \"Delete \\\\nolinenumbers.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Deleted.\"\n  resolution_round: 11\n\n- id: \"R11-W3\"\n  summary: \"Capacity scaling dual-reporting — two incompatible 1.7B numbers\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"本轮未提及 dual-reporting 问题。但新问题 R13-W2 识别出 1.7B non-monotonic dip 未被解释。\"\n  action_items:\n    - round: 11\n      action: \"Unify main text to 4-seed controlled.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Unified. New issue R13-W2 tracks remaining 1.7B explanation gap.\"\n  resolution_round: 11\n\n- id: \"R11-W4\"\n  summary: \"Cluster bootstrap K=11 below minimum cluster count\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"重新出现为 R13-N2 的子问题(a)。上轮修复（添加 Cameron 引用 + caveat）被认为不够充分——用不可靠方法的 CI 来支撑 claim 仍不严谨。\"\n  action_items:\n    - round: 11\n      action: \"Add Cameron et al. citation + caveat.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Citation and caveat added, but R13 reviewers found fix insufficient.\"\n  resolution_round: 11\n\n- id: \"R11-W5\"\n  summary: \"McNemar test input not clearly distinguished from routing labels\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"本轮未提及，修复确认。\"\n  action_items:\n    - round: 11\n      action: \"Add clarifying sentence.\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Clarification added.\"\n  resolution_round: 11\n\n- id: \"R11-m1\"\n  summary: \"§4.1 and §4.5 paragraphs too dense\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Split into sub-paragraphs.\"\n  resolution_round: 11\n\n- id: \"R11-m2\"\n  summary: \"Abstract 78.9% vs DAF=90.4% distinction not intuitive\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"上轮修复确认。但新 issue R13-N1 要求更根本的叙事重组（78.9% 为 primary，DAF 降级）。\"\n  resolution: \"Added clarification. Superseded by R13-N1.\"\n  resolution_round: 11\n\n- id: \"R11-m3\"\n  summary: \"Mann-Whitney vs Wilcoxon signed-rank for reasoning depth ablation\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"Confirmed unpaired design. Mann-Whitney correct.\"\n  resolution_round: 11\n\n- id: \"R10-C1\"\n  summary: \"df=27 statistical error in partial correlation\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Superseded by R11-C1. Partial correlation deleted.\"\n  resolution_round: 11\n\n- id: \"R10-C2\"\n  summary: \"Core finding novelty insufficient — DAF near-tautological\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Issue recurs as R13-N1. Previous 'fix'（78.9% as headline）was partial; R13 reviewers demand deeper restructuring including predictability analysis.\"\n  resolution: \"Framing restructured in R11, but R13 finds it insufficient. Superseded by R13-N1.\"\n  resolution_round: 11\n\n- id: \"R10-C3\"\n  summary: \"Single-environment evidence — no cross-env REPLICATION\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Issue recurs as R13-N3. Previous fix (scope downgrade) considered partial; still no second catastrophic-failure environment.\"\n  resolution: \"Contribution 3 scoped down in R11, but R13 finds it still insufficient. Superseded by R13-N3.\"\n  resolution_round: 11\n\n- id: \"R10-C4\"\n  summary: \"Data scaling ablation uses augmentation — cannot rule out real-data scarcity\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Issue partially recurs in R13-W2(a). Language was unified but Introduction still uses 'confirm this is structural'.\"\n  resolution: \"Language unified in R11. Residual framing issue tracked in R13-W2.\"\n  resolution_round: 11\n\n- id: \"R10-C5\"\n  summary: \"Capacity scaling confound — seeds mismatch\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  resolution: \"Controlled 4-seed replication done.\"\n  resolution_round: 11\n\n- id: \"R10-W1\"\n  summary: \"Router failure does not 'validate' analytical framework\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-W2\"\n  summary: \"'Environment-agnostic' overclaim\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Fixed.\"\n  resolution_round: 11\n\n- id: \"R10-W3\"\n  summary: \"Related work gaps\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Core gaps from R10 filled. New gaps identified in R13-W6 (Safe RL, LLM agent failure mode, Voyager, OPE).\"\n  resolution: \"Core gaps filled in R11. New gaps tracked in R13-W6.\"\n  resolution_round: 11\n"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-17T14:40:20.717709+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 15064}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-17T14:43:01.485878+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "simgate-modular-routing",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "2.5 - Borderline Findings",
  "report": "\n# 圆桌审稿报告 — Round 13\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**目标 Venue**: EMNLP 2026（ARR May 2026 cycle）\n**ARR 提交截止**: 2026-05-25\n**审稿人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性 + 写作/格式）\n\n---\n\n## Summary\n\n论文提出 episode-level counterfactual 框架，通过 paired pure-strategy episodes 分析 modular LLM agent 中 routing signal 的来源。核心发现：在 ScienceWorld 的 11 个 task types（245 episodes, Qwen2.5-7B-Instruct）上，78.9% 的 non-tie routing labels 来自 death asymmetry（penalty-independent），DAF=90.4%（penalty-dependent, P=100）。Router 训练（0.6B-4B）无法超越 always-deterministic baseline。Cross-environment contrasts 在 MATH（null result, p=0.81）和 ALFWorld（information asymmetry mechanism）上提供了 boundary conditions。\n\n---\n\n## Strengths\n\n**S1.** 研究问题有价值且定义清晰：「what drives routing signal」是一个被忽视但重要的诊断性问题。大多数 routing 工作假设 diverse signal exists，本文质疑这一假设。[Consensus]\n\n**S2.** 论文的学术诚实度异常高：主动承认 r=0.97 是代数推论（§3.1）、DAF 随 P 单调递增是数学性质（§2.3）、cluster bootstrap K<40 不可靠（§3.1）、augmentation ≠ real data scaling（§3.6, Appendix F）、cross-environment evidence 不是 replication（Discussion）。这种 self-awareness 在 ARR 提交中非常罕见。[Consensus]\n\n**S3.** 统计验证扎实：Bootstrap CI（B=10,000）、LOO robustness（Table 3）、cross-split evaluation（8 seeds, 两个粒度）、McNemar test for MATH null（p=0.81, N=795）。对一篇分析型论文而言，验证工作全面。[Consensus]\n\n**S4.** Negative results 有实际参考价值：Router 无法超越 always-deterministic 的发现，以及 MATH 的 well-powered null result，对 LLM agent routing 实践者有诊断意义。[Consensus]\n\n**S5.** 写作质量良好：无 AI 写作痕迹（无 em-dash、无 -ing phrase 结尾、无过渡词堆砌），技术写作准确。[Consensus]\n\n**S6.** Appendix 分析深度充实：penalty sensitivity（7 个 P 值）、seed robustness（8 seeds）、per-task decomposition、capacity scaling、cross-model、failure mode、threshold routing。[Consensus]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical] DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调「经验发现」\n- **位置**: §2.3 Eq. (3-4), §3.1, Abstract, Introduction\n- **问题**: DAF = δP/(δP + Δ_nd)。当 P=100 而 Δ_nd=2.84 时，DAF ≈ 90.3%——这个高值由 P/Δ_nd 比值决定，不是独立经验发现。P=10 时 DAF=50.4%，P=0 时 DAF=7.5%（Appendix E, Table 5）。r=0.97 是 DAF→1 时的数学必然（论文自己承认）。给定 δ=0.265 和 P=100，DAF 的 predicted value = 26.5/(26.5+2.84) = 90.3%，与实测 90.4% 几乎吻合——DAF 分析没有产生超出「知道死亡率差异和惩罚幅度」之外的新信息。\n- **penalty-independent 指标更有信息量**: 78.9%（75/95 non-tie labels from death asymmetry）是需要实验才能获得的经验数字，但在叙事中不够突出。Abstract 仍以 DAF=90.4% 为 headline。\n- **Action**: 以 78.9% penalty-independent label fraction 为 primary metric，DAF 降级为 supplementary/sensitivity analysis；增加 predictability analysis 量化 predicted vs observed deviation；Abstract/Introduction 降低对 DAF 数值的依赖。\n- **Reviewer consensus**: [R1 N1 + R2 N2] 双方 AGREE\n\n**N2** [critical] 统计推断可靠性不足以支撑 claim 的强度\n- **位置**: §3.1 (bootstrap CIs), §3.2 (Llama pilot), Appendix B-C\n- **问题**:\n  - (a) Cluster bootstrap K=11 远低于作者自引的 Cameron et al. (2008) K≥40 门槛。CI [73.3%, 100%] 不可靠，\"should be interpreted cautiously\" 不足以弥补前提条件不满足的问题。\n  - (b) Episode-level bootstrap 假设 245 episodes 独立，但同一 task type 内 episodes 共享 task structure、scoring rubric、环境布局。\n  - (c) Per-task 样本量 n=20 极小：chemistry-mix CI [-5.0, 48.6] 跨零，但论文以\"10 of 11 types exhibit DAF=100%\"呈现结果，掩盖 uncertainty。\n  - (d) Llama pilot N=70, 7 tasks, 0 internal-preferred：binomial 95% upper bound ≈ 4.2%，不足以支撑定量结论。\n  - (e) 论文 headline 用点估计（90.4%）而非 CI（[81.6%, 98.8%]，width 17pp）叙事。\n- **Action**: 对 cluster bootstrap 不可靠性做更诚实讨论或使用替代方法；Llama pilot 降级为 anecdotal evidence，不出现在 Contribution 3；per-task 结果报告时体现 uncertainty；headline 使用 CI。\n- **Reviewer consensus**: [R1 N2] R2 AGREE（承认自己 Round 1 遗漏）\n\n**N3** [critical] 跨环境证据不足以支撑 Contribution 3\n- **位置**: §3.4-3.5, Introduction Contribution 3, Discussion\n- **问题**: 论文声称\"cross-environment diagnostic contrasts establishing framework boundary conditions\"，但：\n  - MATH (N=795) 验证 predicted null（弱检验：任何合理框架都预测无 death penalty → 无 death-driven signal）\n  - ALFWorld (N=135) 的 modality 定义根本不同（admissible actions = action space pruning vs ground-truth observations = state estimation），是\"information asymmetry rather than computation mode switch\"（论文自己承认）\n  - Llama pilot (N=70) 样本量过小\n  - **最关键缺失**: 无第二个具有 catastrophic failure 的环境（NetHack/Crafter 仅列为 future work）\n- **Action**: 降级 Contribution 3 为\"preliminary cross-environment evidence\"；最理想：增加 NetHack/Crafter 的 quantitative DAF replication。\n- **Reviewer consensus**: [R1 N3 + R2 N3] 双方 AGREE\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [strong warning] 正文篇幅严重不足 long paper 要求\n- 渲染 PDF 正文（§1-§Conclusion）约 5 页，距 8 页限制差约 3 页。大量核心证据（per-task decomposition、penalty sensitivity、capacity scaling、seed robustness）藏在 Appendix。Discussion 仅约 0.5 页。\n- R2 列 critical，R1 列 warning。Director 判定：strong warning / borderline critical——严重影响可读性和审稿体验，但属组织结构问题而非方法论缺陷，可通过将关键 Appendix 内容提升至正文修复。\n- **Action**: 将 Appendix B/E/F 核心内容纳入正文；大幅扩展 Discussion。\n- **Reviewer consensus**: 双方 AGREE（severity 定级有分歧）\n\n**W2** [warning] Router 训练实验存在多个 confound\n- (a) Paraphrase augmentation ≠ real data scaling，但 Introduction 仍断言\"confirm this is structural rather than data-limited\"\n- (b) 4B end-to-end N=275 vs baselines N=245，引入 task distribution confound\n- (c) 1.7B episode-level 43.1%（低于 0.6B 的 50.7%，Table 4）的 non-monotonic dip 未解释\n- **Action**: \"data scaling\" 改为 \"augmentation scaling\" 并调整结论；在 shared task set 上统一比较；对 1.7B dip 提供可检验 hypothesis。\n- **Reviewer consensus**: [R1 W1 + R2 W6] 双方 AGREE\n\n**W3** [warning] Episode-level label → step-level training 的 mislabeling 未被量化\n- 论文承认 episode-level labels 可能对 individual steps 标记不准（Limitations），但未量化规模。估算：42.9% internal 死亡率 × ~19/30 non-terminal steps ≈ 27% step-level labels 可能是 mislabeled。\n- **Action**: 计算并报告 \"potentially mislabeled step fraction\"。\n- **Reviewer consensus**: [R1 W2] R2 AGREE\n\n**W4** [warning] SCI（Signal Concentration Index）方法贡献与使用不成比例\n- Method §2.4 完整定义但全文仅使用一次（SCI=0.2147）。本质是 Gini coefficient 的 rename，K=11 时估计方差大。\"top-3 tasks account for 39.8%\"传达相同信息。\n- **Action**: 降级 SCI 到 Appendix，主文用描述性语言替代。\n- **Reviewer consensus**: [R1 W3 + R2 W3] 双方 AGREE\n\n**W5** [warning] Abstract 数字堆砌\n- 约 200 词中嵌入 10+ 统计量，读起来像 results summary 而非 compelling narrative。应减至 5-6 个关键数字。\n- **Reviewer consensus**: [R2 W1] R1 AGREE\n\n**W6** [warning] Safe RL 和 LLM agent failure mode 引用覆盖不足\n- Safe RL 仅 Garcia 2015 + CRPO 2021，但论文明确将 routing 框架为 safety problem（Discussion）。缺少 constrained MDP（Altman 1999）、CPO、LLM agent failure analysis、Voyager 等引用。\n- R1 部分同意（不认为\"严重\"但承认可补充）；R2 认为较严重。\n- **Reviewer consensus**: [R2 W2 + R2 W5] R1 PARTIALLY AGREE\n\n**W7** [warning] Router negative results 解释不完整\n- Discussion 缺乏对 router failure 根本原因的深入分析：什么条件下 router 可能有用？更强 internal reasoning（Reflexion）可能改变结论？\n- **Reviewer consensus**: [R2 W6] R1 AGREE\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成完全共识 [AGREE]：\n1. DAF=90.4% 和 r=0.97 是环境参数 P=100 的代数后果，不是独立经验发现（N1）\n2. 无第二个 catastrophic-failure 环境的 replication 是核心缺陷（N3）\n3. SCI 应降级至 Appendix（W4）\n4. Abstract 需精简统计量（W5）\n5. 写作质量良好，无 AI 痕迹（S5）\n6. 学术诚实度异常高（S2）\n\n## Reviewer Divergence\n\n1. **Algorithm 1 形式化程度**: R2 认为 over-formalized（3-case 判断用 8 行伪代码，W4），R1 REBUT——认为是 Contribution 1 的锚点，priority ordering 需要形式化保证 reproducibility。**Director 判定**: R1 的理由更有说服力，Algorithm 1 保留合理，不列为问题。\n2. **篇幅问题严重性**: R2 列 critical (N1)，R1 列 warning (W4)。**Director 判定**: 列为 strong warning——组织结构问题而非方法论缺陷，但严重影响审稿体验。\n3. **Safe RL 覆盖度**: R2 认为\"严重不足\"，R1 认为\"可补充 1-2 篇\"。**Director 判定**: 论文将 routing 框架为 safety problem 但 Safe RL 引用仅 2 篇，需补充但不构成 critical gap。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** 给定已知的 δ=0.265 和 P=100，DAF 的 predicted value = 90.3%，与实测 90.4% 几乎吻合。DAF 分析产生了哪些超出「知道死亡率差异和惩罚幅度」之外的新信息？[R1 + R2]\n\n**Q2.** P=1 时 DAF≈8.5%，此时是否仍能得出\"death avoidance is dominant\"的结论？如果不能，核心 claim 本质上是关于惩罚幅度而非 routing mechanism。[R2]\n\n**Q3.** 54/75 death-asymmetry labels 移除 death penalty 后变为 tie（both score 0）。这是否说明 30-step budget 对 internal strategy 过于苛刻，而非 routing mechanism 本身的性质？如果增加 step budget，当前发现是否会改变？[R2, R1 agrees]\n\n**Q4.** ALFWorld 的 deterministic modality（admissible actions = action space pruning）与 ScienceWorld（ground-truth observations = state estimation）是根本不同的定义。将两者放在同一 framework 下比较是否存在概念混淆？[R1 + R2]\n\n**Q5.** 1.7B router 的 episode-level 43.1%（显著低于 0.6B 的 50.7%）是否学到了某种反向 spurious correlation？有无可检验的 hypothesis？[R1]\n\n---\n\n## Missing References\n\n**需补充方向（按优先级排序）**：\n1. **Voyager** (Wang et al., 2023) — ScienceWorld 上的重要 LLM agent 工作 [R1]\n2. **Constrained MDP** (Altman 1999) — 论文将 routing 框架为 safety problem 的理论基础 [R2]\n3. **OPE 文献** (Precup et al. 2000, Jiang & Li 2016) — 与 prospective counterfactual evaluation 的方法论对比 [R1]\n4. **LLM agent failure analysis** — WebArena/InterCode 中的 agent failure patterns [R2]\n5. **Cost-aware routing** — FrugalGPT (Chen et al., 2023) [R2]\n6. **Grounded hallucination** — 与 state hallucination → cascading errors 机制相关 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Overall Assessment\n\n**综合评分: 2.5（Borderline Findings）**\n\n- **Reviewer 1**: 3.0 (Findings)\n- **Reviewer 2**: 2.5 (Borderline Findings)\n- **Confidence**: 4/5（两位 Reviewer 均为 4/5）\n\n**评分理由**:\n\n论文提出了一个有价值的诊断性问题（what drives routing signal），设计了合理的 counterfactual 框架，以罕见的学术诚实度呈现了结果。统计验证扎实，写作质量良好。\n\n主要顾虑：\n1. **核心发现的经验性贡献被削弱**：DAF=90.4% 和 r=0.97 是 P=100 的代数后果，penalty-independent 的 78.9% 更有信息量但在叙事中未充分突出。给定已知的死亡率差异和惩罚幅度，核心发现的\"surprise\"有限。\n2. **统计推断与 claim 强度不匹配**：cluster bootstrap K=11 不可靠、per-task n=20 CI 极宽、Llama pilot N=70 不足以支撑定量结论。\n3. **跨环境证据不构成 framework replication**：无第二个 catastrophic-failure 环境，Contribution 3 的实际证据远弱于其 claim。\n4. **正文篇幅不足**：约 5 页 vs 8 页限制，大量核心证据藏在 Appendix。\n\n**R1 给 3.0、R2 给 2.5 的分歧来源**：(1) R1 对 78.9% penalty-independent metric 和 97.4% step-level tie rate 给予更多 credit；(2) R1 认为篇幅是组织问题而非贡献不足；(3) R1 对学术诚实度和 negative results 的加分更高。Director 采纳 2.5 作为 conservative estimate——当前状态下论文需要实质性修改才能达到 Findings 接收标准。\n\n**提升路径**（如果完成以下修改，评分可提升至 3.0-3.5）：\n1. 叙事重组：以 78.9% penalty-independent label fraction 为 primary metric，DAF 降级为 supplementary，增加 predictability analysis\n2. 将关键 Appendix 内容（per-task decomposition、penalty sensitivity、capacity scaling）纳入正文，填满 8 页限制\n3. 降级 Contribution 3 措辞，或增加 NetHack/Crafter 的 catastrophic-failure environment replication\n4. 大幅扩展 Discussion：router failure 根本原因、Reflexion 等更强 baseline 的预测、framework applicability boundary\n5. 修复统计报告：cluster bootstrap caveat 加强、per-task uncertainty 体现、Llama pilot 降级\n\n---\n\n## Detailed Comments\n\n### §Abstract\n- 约 190 词中嵌入 10+ 统计量（78.9%, 75/95, 90.4%, P=100, r=0.97, 59.0%, 4B, N=795, p=0.81, N=135...），信息密度过高。建议精简至 5-6 个关键数字，聚焦\"why this matters\"。\n- 以 DAF=90.4% 为 headline 强化了 tautology 印象。应前置 78.9% penalty-independent finding。\n\n### §1 Introduction\n- \"a surprisingly concentrated answer\"（§1 para 2）：给定 42.9% vs 16.3% 死亡率和 P=100，death dominance 是可预测的，不是\"surprising\"。\n- Contribution 3 的措辞（\"establishing framework boundary conditions\"）过强——实际是 preliminary evidence。\n- 97.4% step-level tie rate 的 methodological insight 有价值，建议更突出。\n\n### §2 Method\n- §2.4 SCI 的 formal 定义占用正文空间但仅使用一次，建议降级至 Appendix。\n- Algorithm 1 的 death-first priority ordering 对 78.9% metric 有 mechanical 影响（72% 的 death-asymmetry labels 去除 penalty 后变为 tie），论文应更明确讨论这一设计选择。\n\n### §3 Experiments\n- §3.1：\"10 of 11 types exhibit DAF=100%\"——掩盖了 per-task n=20 下 CI 极宽的事实。\n- §3.1 cluster bootstrap CI [73.3%, 100%]——用自己承认不可靠的方法得出的 CI 来支撑 claim 不严谨。\n- §3.4 Llama pilot：Abstract 和 Contribution 3 的 claim 强度与 N=70 的证据强度不匹配。\n- §3.5 ALFWorld：\"information asymmetry rather than computation mode switch\"——modality 定义的不可通约性需在正文中更明确讨论。\n- §3.6：\"Data scaling (32×) ablations confirm this is structural\"——应改为\"augmentation scaling\"并降低结论强度。\n- §3.6 1.7B dip (43.1%)：需要至少一个可检验的 hypothesis。\n- §3.6 4B N=275 vs baselines N=245：应在 shared task set 上统一比较或更好地解释差异。\n\n### §4 Related Work\n- Safe RL 段落仅 3 行 2 篇引用，与论文将 routing 框架为 safety problem 的 claim 不匹配。\n- 缺少 LLM agent failure mode analysis 和 Voyager 引用。\n\n### §5 Discussion\n- 仅约 0.5 页，远不够充分。需扩展：(1) router failure 的根本原因分析；(2) Reflexion/stronger baseline 的预测；(3) framework applicability 的精确边界；(4) DAF 的 P-dependence 的实质含义。\n\n### §Limitations\n- \"increasing the step budget could surface additional signal\"——应量化或至少讨论 step budget 对发现的敏感性。\n- Episode-level → step-level mislabeling fraction 应被计算和报告（估算约 27%）。\n\n### Formatting\n- Title TeX 源码（\"a Dominant\"）与渲染 PDF（\"the Dominant\"）不一致，需统一。\n- Figure 3 仅含 ScienceWorld + MATH，缺少 ALFWorld。\n- Reference 格式：部分条目使用\"and others\"而非完整作者列表，需统一。\n- 正文约 5 页，需将关键 Appendix 内容纳入正文达到 8 页。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "simgate-modular-routing",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "2.5 - Borderline Findings",
    "report": "\n# 圆桌审稿报告 — Round 13\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**目标 Venue**: EMNLP 2026（ARR May 2026 cycle）\n**ARR 提交截止**: 2026-05-25\n**审稿人**: Reviewer 1（方法严谨性 + 实验设计）、Reviewer 2（新颖性 + 完整性 + 写作/格式）\n\n---\n\n## Summary\n\n论文提出 episode-level counterfactual 框架，通过 paired pure-strategy episodes 分析 modular LLM agent 中 routing signal 的来源。核心发现：在 ScienceWorld 的 11 个 task types（245 episodes, Qwen2.5-7B-Instruct）上，78.9% 的 non-tie routing labels 来自 death asymmetry（penalty-independent），DAF=90.4%（penalty-dependent, P=100）。Router 训练（0.6B-4B）无法超越 always-deterministic baseline。Cross-environment contrasts 在 MATH（null result, p=0.81）和 ALFWorld（information asymmetry mechanism）上提供了 boundary conditions。\n\n---\n\n## Strengths\n\n**S1.** 研究问题有价值且定义清晰：「what drives routing signal」是一个被忽视但重要的诊断性问题。大多数 routing 工作假设 diverse signal exists，本文质疑这一假设。[Consensus]\n\n**S2.** 论文的学术诚实度异常高：主动承认 r=0.97 是代数推论（§3.1）、DAF 随 P 单调递增是数学性质（§2.3）、cluster bootstrap K<40 不可靠（§3.1）、augmentation ≠ real data scaling（§3.6, Appendix F）、cross-environment evidence 不是 replication（Discussion）。这种 self-awareness 在 ARR 提交中非常罕见。[Consensus]\n\n**S3.** 统计验证扎实：Bootstrap CI（B=10,000）、LOO robustness（Table 3）、cross-split evaluation（8 seeds, 两个粒度）、McNemar test for MATH null（p=0.81, N=795）。对一篇分析型论文而言，验证工作全面。[Consensus]\n\n**S4.** Negative results 有实际参考价值：Router 无法超越 always-deterministic 的发现，以及 MATH 的 well-powered null result，对 LLM agent routing 实践者有诊断意义。[Consensus]\n\n**S5.** 写作质量良好：无 AI 写作痕迹（无 em-dash、无 -ing phrase 结尾、无过渡词堆砌），技术写作准确。[Consensus]\n\n**S6.** Appendix 分析深度充实：penalty sensitivity（7 个 P 值）、seed robustness（8 seeds）、per-task decomposition、capacity scaling、cross-model、failure mode、threshold routing。[Consensus]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [critical] DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调「经验发现」\n- **位置**: §2.3 Eq. (3-4), §3.1, Abstract, Introduction\n- **问题**: DAF = δP/(δP + Δ_nd)。当 P=100 而 Δ_nd=2.84 时，DAF ≈ 90.3%——这个高值由 P/Δ_nd 比值决定，不是独立经验发现。P=10 时 DAF=50.4%，P=0 时 DAF=7.5%（Appendix E, Table 5）。r=0.97 是 DAF→1 时的数学必然（论文自己承认）。给定 δ=0.265 和 P=100，DAF 的 predicted value = 26.5/(26.5+2.84) = 90.3%，与实测 90.4% 几乎吻合——DAF 分析没有产生超出「知道死亡率差异和惩罚幅度」之外的新信息。\n- **penalty-independent 指标更有信息量**: 78.9%（75/95 non-tie labels from death asymmetry）是需要实验才能获得的经验数字，但在叙事中不够突出。Abstract 仍以 DAF=90.4% 为 headline。\n- **Action**: 以 78.9% penalty-independent label fraction 为 primary metric，DAF 降级为 supplementary/sensitivity analysis；增加 predictability analysis 量化 predicted vs observed deviation；Abstract/Introduction 降低对 DAF 数值的依赖。\n- **Reviewer consensus**: [R1 N1 + R2 N2] 双方 AGREE\n\n**N2** [critical] 统计推断可靠性不足以支撑 claim 的强度\n- **位置**: §3.1 (bootstrap CIs), §3.2 (Llama pilot), Appendix B-C\n- **问题**:\n  - (a) Cluster bootstrap K=11 远低于作者自引的 Cameron et al. (2008) K≥40 门槛。CI [73.3%, 100%] 不可靠，\"should be interpreted cautiously\" 不足以弥补前提条件不满足的问题。\n  - (b) Episode-level bootstrap 假设 245 episodes 独立，但同一 task type 内 episodes 共享 task structure、scoring rubric、环境布局。\n  - (c) Per-task 样本量 n=20 极小：chemistry-mix CI [-5.0, 48.6] 跨零，但论文以\"10 of 11 types exhibit DAF=100%\"呈现结果，掩盖 uncertainty。\n  - (d) Llama pilot N=70, 7 tasks, 0 internal-preferred：binomial 95% upper bound ≈ 4.2%，不足以支撑定量结论。\n  - (e) 论文 headline 用点估计（90.4%）而非 CI（[81.6%, 98.8%]，width 17pp）叙事。\n- **Action**: 对 cluster bootstrap 不可靠性做更诚实讨论或使用替代方法；Llama pilot 降级为 anecdotal evidence，不出现在 Contribution 3；per-task 结果报告时体现 uncertainty；headline 使用 CI。\n- **Reviewer consensus**: [R1 N2] R2 AGREE（承认自己 Round 1 遗漏）\n\n**N3** [critical] 跨环境证据不足以支撑 Contribution 3\n- **位置**: §3.4-3.5, Introduction Contribution 3, Discussion\n- **问题**: 论文声称\"cross-environment diagnostic contrasts establishing framework boundary conditions\"，但：\n  - MATH (N=795) 验证 predicted null（弱检验：任何合理框架都预测无 death penalty → 无 death-driven signal）\n  - ALFWorld (N=135) 的 modality 定义根本不同（admissible actions = action space pruning vs ground-truth observations = state estimation），是\"information asymmetry rather than computation mode switch\"（论文自己承认）\n  - Llama pilot (N=70) 样本量过小\n  - **最关键缺失**: 无第二个具有 catastrophic failure 的环境（NetHack/Crafter 仅列为 future work）\n- **Action**: 降级 Contribution 3 为\"preliminary cross-environment evidence\"；最理想：增加 NetHack/Crafter 的 quantitative DAF replication。\n- **Reviewer consensus**: [R1 N3 + R2 N3] 双方 AGREE\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [strong warning] 正文篇幅严重不足 long paper 要求\n- 渲染 PDF 正文（§1-§Conclusion）约 5 页，距 8 页限制差约 3 页。大量核心证据（per-task decomposition、penalty sensitivity、capacity scaling、seed robustness）藏在 Appendix。Discussion 仅约 0.5 页。\n- R2 列 critical，R1 列 warning。Director 判定：strong warning / borderline critical——严重影响可读性和审稿体验，但属组织结构问题而非方法论缺陷，可通过将关键 Appendix 内容提升至正文修复。\n- **Action**: 将 Appendix B/E/F 核心内容纳入正文；大幅扩展 Discussion。\n- **Reviewer consensus**: 双方 AGREE（severity 定级有分歧）\n\n**W2** [warning] Router 训练实验存在多个 confound\n- (a) Paraphrase augmentation ≠ real data scaling，但 Introduction 仍断言\"confirm this is structural rather than data-limited\"\n- (b) 4B end-to-end N=275 vs baselines N=245，引入 task distribution confound\n- (c) 1.7B episode-level 43.1%（低于 0.6B 的 50.7%，Table 4）的 non-monotonic dip 未解释\n- **Action**: \"data scaling\" 改为 \"augmentation scaling\" 并调整结论；在 shared task set 上统一比较；对 1.7B dip 提供可检验 hypothesis。\n- **Reviewer consensus**: [R1 W1 + R2 W6] 双方 AGREE\n\n**W3** [warning] Episode-level label → step-level training 的 mislabeling 未被量化\n- 论文承认 episode-level labels 可能对 individual steps 标记不准（Limitations），但未量化规模。估算：42.9% internal 死亡率 × ~19/30 non-terminal steps ≈ 27% step-level labels 可能是 mislabeled。\n- **Action**: 计算并报告 \"potentially mislabeled step fraction\"。\n- **Reviewer consensus**: [R1 W2] R2 AGREE\n\n**W4** [warning] SCI（Signal Concentration Index）方法贡献与使用不成比例\n- Method §2.4 完整定义但全文仅使用一次（SCI=0.2147）。本质是 Gini coefficient 的 rename，K=11 时估计方差大。\"top-3 tasks account for 39.8%\"传达相同信息。\n- **Action**: 降级 SCI 到 Appendix，主文用描述性语言替代。\n- **Reviewer consensus**: [R1 W3 + R2 W3] 双方 AGREE\n\n**W5** [warning] Abstract 数字堆砌\n- 约 200 词中嵌入 10+ 统计量，读起来像 results summary 而非 compelling narrative。应减至 5-6 个关键数字。\n- **Reviewer consensus**: [R2 W1] R1 AGREE\n\n**W6** [warning] Safe RL 和 LLM agent failure mode 引用覆盖不足\n- Safe RL 仅 Garcia 2015 + CRPO 2021，但论文明确将 routing 框架为 safety problem（Discussion）。缺少 constrained MDP（Altman 1999）、CPO、LLM agent failure analysis、Voyager 等引用。\n- R1 部分同意（不认为\"严重\"但承认可补充）；R2 认为较严重。\n- **Reviewer consensus**: [R2 W2 + R2 W5] R1 PARTIALLY AGREE\n\n**W7** [warning] Router negative results 解释不完整\n- Discussion 缺乏对 router failure 根本原因的深入分析：什么条件下 router 可能有用？更强 internal reasoning（Reflexion）可能改变结论？\n- **Reviewer consensus**: [R2 W6] R1 AGREE\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成完全共识 [AGREE]：\n1. DAF=90.4% 和 r=0.97 是环境参数 P=100 的代数后果，不是独立经验发现（N1）\n2. 无第二个 catastrophic-failure 环境的 replication 是核心缺陷（N3）\n3. SCI 应降级至 Appendix（W4）\n4. Abstract 需精简统计量（W5）\n5. 写作质量良好，无 AI 痕迹（S5）\n6. 学术诚实度异常高（S2）\n\n## Reviewer Divergence\n\n1. **Algorithm 1 形式化程度**: R2 认为 over-formalized（3-case 判断用 8 行伪代码，W4），R1 REBUT——认为是 Contribution 1 的锚点，priority ordering 需要形式化保证 reproducibility。**Director 判定**: R1 的理由更有说服力，Algorithm 1 保留合理，不列为问题。\n2. **篇幅问题严重性**: R2 列 critical (N1)，R1 列 warning (W4)。**Director 判定**: 列为 strong warning——组织结构问题而非方法论缺陷，但严重影响审稿体验。\n3. **Safe RL 覆盖度**: R2 认为\"严重不足\"，R1 认为\"可补充 1-2 篇\"。**Director 判定**: 论文将 routing 框架为 safety problem 但 Safe RL 引用仅 2 篇，需补充但不构成 critical gap。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** 给定已知的 δ=0.265 和 P=100，DAF 的 predicted value = 90.3%，与实测 90.4% 几乎吻合。DAF 分析产生了哪些超出「知道死亡率差异和惩罚幅度」之外的新信息？[R1 + R2]\n\n**Q2.** P=1 时 DAF≈8.5%，此时是否仍能得出\"death avoidance is dominant\"的结论？如果不能，核心 claim 本质上是关于惩罚幅度而非 routing mechanism。[R2]\n\n**Q3.** 54/75 death-asymmetry labels 移除 death penalty 后变为 tie（both score 0）。这是否说明 30-step budget 对 internal strategy 过于苛刻，而非 routing mechanism 本身的性质？如果增加 step budget，当前发现是否会改变？[R2, R1 agrees]\n\n**Q4.** ALFWorld 的 deterministic modality（admissible actions = action space pruning）与 ScienceWorld（ground-truth observations = state estimation）是根本不同的定义。将两者放在同一 framework 下比较是否存在概念混淆？[R1 + R2]\n\n**Q5.** 1.7B router 的 episode-level 43.1%（显著低于 0.6B 的 50.7%）是否学到了某种反向 spurious correlation？有无可检验的 hypothesis？[R1]\n\n---\n\n## Missing References\n\n**需补充方向（按优先级排序）**：\n1. **Voyager** (Wang et al., 2023) — ScienceWorld 上的重要 LLM agent 工作 [R1]\n2. **Constrained MDP** (Altman 1999) — 论文将 routing 框架为 safety problem 的理论基础 [R2]\n3. **OPE 文献** (Precup et al. 2000, Jiang & Li 2016) — 与 prospective counterfactual evaluation 的方法论对比 [R1]\n4. **LLM agent failure analysis** — WebArena/InterCode 中的 agent failure patterns [R2]\n5. **Cost-aware routing** — FrugalGPT (Chen et al., 2023) [R2]\n6. **Grounded hallucination** — 与 state hallucination → cascading errors 机制相关 [R2]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置外部审稿。\n\n---\n\n## Overall Assessment\n\n**综合评分: 2.5（Borderline Findings）**\n\n- **Reviewer 1**: 3.0 (Findings)\n- **Reviewer 2**: 2.5 (Borderline Findings)\n- **Confidence**: 4/5（两位 Reviewer 均为 4/5）\n\n**评分理由**:\n\n论文提出了一个有价值的诊断性问题（what drives routing signal），设计了合理的 counterfactual 框架，以罕见的学术诚实度呈现了结果。统计验证扎实，写作质量良好。\n\n主要顾虑：\n1. **核心发现的经验性贡献被削弱**：DAF=90.4% 和 r=0.97 是 P=100 的代数后果，penalty-independent 的 78.9% 更有信息量但在叙事中未充分突出。给定已知的死亡率差异和惩罚幅度，核心发现的\"surprise\"有限。\n2. **统计推断与 claim 强度不匹配**：cluster bootstrap K=11 不可靠、per-task n=20 CI 极宽、Llama pilot N=70 不足以支撑定量结论。\n3. **跨环境证据不构成 framework replication**：无第二个 catastrophic-failure 环境，Contribution 3 的实际证据远弱于其 claim。\n4. **正文篇幅不足**：约 5 页 vs 8 页限制，大量核心证据藏在 Appendix。\n\n**R1 给 3.0、R2 给 2.5 的分歧来源**：(1) R1 对 78.9% penalty-independent metric 和 97.4% step-level tie rate 给予更多 credit；(2) R1 认为篇幅是组织问题而非贡献不足；(3) R1 对学术诚实度和 negative results 的加分更高。Director 采纳 2.5 作为 conservative estimate——当前状态下论文需要实质性修改才能达到 Findings 接收标准。\n\n**提升路径**（如果完成以下修改，评分可提升至 3.0-3.5）：\n1. 叙事重组：以 78.9% penalty-independent label fraction 为 primary metric，DAF 降级为 supplementary，增加 predictability analysis\n2. 将关键 Appendix 内容（per-task decomposition、penalty sensitivity、capacity scaling）纳入正文，填满 8 页限制\n3. 降级 Contribution 3 措辞，或增加 NetHack/Crafter 的 catastrophic-failure environment replication\n4. 大幅扩展 Discussion：router failure 根本原因、Reflexion 等更强 baseline 的预测、framework applicability boundary\n5. 修复统计报告：cluster bootstrap caveat 加强、per-task uncertainty 体现、Llama pilot 降级\n\n---\n\n## Detailed Comments\n\n### §Abstract\n- 约 190 词中嵌入 10+ 统计量（78.9%, 75/95, 90.4%, P=100, r=0.97, 59.0%, 4B, N=795, p=0.81, N=135...），信息密度过高。建议精简至 5-6 个关键数字，聚焦\"why this matters\"。\n- 以 DAF=90.4% 为 headline 强化了 tautology 印象。应前置 78.9% penalty-independent finding。\n\n### §1 Introduction\n- \"a surprisingly concentrated answer\"（§1 para 2）：给定 42.9% vs 16.3% 死亡率和 P=100，death dominance 是可预测的，不是\"surprising\"。\n- Contribution 3 的措辞（\"establishing framework boundary conditions\"）过强——实际是 preliminary evidence。\n- 97.4% step-level tie rate 的 methodological insight 有价值，建议更突出。\n\n### §2 Method\n- §2.4 SCI 的 formal 定义占用正文空间但仅使用一次，建议降级至 Appendix。\n- Algorithm 1 的 death-first priority ordering 对 78.9% metric 有 mechanical 影响（72% 的 death-asymmetry labels 去除 penalty 后变为 tie），论文应更明确讨论这一设计选择。\n\n### §3 Experiments\n- §3.1：\"10 of 11 types exhibit DAF=100%\"——掩盖了 per-task n=20 下 CI 极宽的事实。\n- §3.1 cluster bootstrap CI [73.3%, 100%]——用自己承认不可靠的方法得出的 CI 来支撑 claim 不严谨。\n- §3.4 Llama pilot：Abstract 和 Contribution 3 的 claim 强度与 N=70 的证据强度不匹配。\n- §3.5 ALFWorld：\"information asymmetry rather than computation mode switch\"——modality 定义的不可通约性需在正文中更明确讨论。\n- §3.6：\"Data scaling (32×) ablations confirm this is structural\"——应改为\"augmentation scaling\"并降低结论强度。\n- §3.6 1.7B dip (43.1%)：需要至少一个可检验的 hypothesis。\n- §3.6 4B N=275 vs baselines N=245：应在 shared task set 上统一比较或更好地解释差异。\n\n### §4 Related Work\n- Safe RL 段落仅 3 行 2 篇引用，与论文将 routing 框架为 safety problem 的 claim 不匹配。\n- 缺少 LLM agent failure mode analysis 和 Voyager 引用。\n\n### §5 Discussion\n- 仅约 0.5 页，远不够充分。需扩展：(1) router failure 的根本原因分析；(2) Reflexion/stronger baseline 的预测；(3) framework applicability 的精确边界；(4) DAF 的 P-dependence 的实质含义。\n\n### §Limitations\n- \"increasing the step budget could surface additional signal\"——应量化或至少讨论 step budget 对发现的敏感性。\n- Episode-level → step-level mislabeling fraction 应被计算和报告（估算约 27%）。\n\n### Formatting\n- Title TeX 源码（\"a Dominant\"）与渲染 PDF（\"the Dominant\"）不一致，需统一。\n- Figure 3 仅含 ScienceWorld + MATH，缺少 ALFWorld。\n- Reference 格式：部分条目使用\"and others\"而非完整作者列表，需统一。\n- 正文约 5 页，需将关键 Appendix 内容纳入正文达到 8 页。\n"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-17T14:43:05.402400+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Assistant

_source line 992 · 2026-05-17T14:43:18.660806+00:00_

**Round 13 圆桌审稿完成。**

审稿报告已投递给 Research Director，Issue Tracker 已同步更新。

**结果摘要：**

- **综合评分：2.5（Borderline Findings）**（R1: 3.0, R2: 2.5）
- **3 个 Critical Issues**：DAF tautology（核心发现是代数后果）、统计推断与 claim 强度不匹配、无第二个 catastrophic-failure 环境的 replication
- **7 个 Warning Issues**：篇幅不足（~5p vs 8p 限制）、router confounds、step-level mislabeling 未量化、SCI 贡献不成比例、Abstract 数字堆砌、引用覆盖不足、router negative results 解释不完整
- **3 个 Info Issues**：Title 不一致、Figure 3 缺 ALFWorld、Reference 格式不统一
- **核心共识**：两位 Reviewer 在所有 critical 和大部分 warning issues 上达成一致；唯一实质分歧是 Algorithm 1 的形式化程度（Director 判定保留合理）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 94

## Round 94

2 recorded events


### User

_source line 993 · 2026-05-17T14:43:21.152369+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。主要结论：

- R1 的 N1（DAF tautology + predictability analysis）、N2（统计推断）、N3（cross-env 不足）全部 AGREE，且 R1 的 predictability analysis 建议比我的 N2 更具建设性
- R1-W2（episode→step mislabeling）是我 Round 1 遗漏的有效问题，补充了量化思路（约 27% step 可能被不当标记）
- R1-W1（router confounds）与我的 W6 互补：R1 更聚焦实验设计 confounds，我更关注 conceptual gaps
- 评分差异（3.0 vs 2.5）主要源于我对篇幅问题权重更高、对方法论新颖性要求更严格

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 994 · 2026-05-17T14:43:34.496286+00:00_

审稿报告已投递至 Research Director，Issue Tracker 已同步更新。

**Round 13 审稿结论：**

- **综合评分：2.5（Borderline Findings）**
- R1: 3.0 / R2: 2.5，分歧来自 excitement 和篇幅问题权重，核心判断一致
- 3 个 critical issues + 7 个 warnings + 3 个 minor issues
- 关键共识：DAF tautology、无第二个 catastrophic-failure 环境 replication、统计推断与 claim 强度不匹配
- 提升路径明确：叙事重组（78.9% 为 primary）、填满 8 页正文、降级 Contribution 3、扩展 Discussion

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 95

## Round 95

68 recorded events


### User

_source line 995 · 2026-05-17T15:07:51.524651+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/
- 目标 venue: EMNLP 2026 Findings
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-17T15:08:07.294228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-17T15:08:07.345234+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 998 · 2026-05-17T15:08:09.956003+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-17T15:08:10.006626+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-17T15:08:14.525187+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-17T15:08:14.575922+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-17T15:08:17.789332+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-17T15:08:17.789847+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1004 · 2026-05-17T15:08:22.884381+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-17T15:08:23.386701+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (100 个)\n\n- **plan-001b-fnlt-v2**: DONE (success) — \n- **plan-001b-gpu0-v4**: DONE (killed) — \n- **plan-001b-gpu0-v3**: DONE (failed) — \n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| reflexion-internal-baseline-b | Reflexion baseline Part 2 (tasks 7-11): 与 part 1 并行收集，验证 reflexion 对 death rate 的影响 | — | — | — |\n| reflexion-internal-baseline | Reflexion 通过自我纠错降低 internal modality 的 death rate；如果 death rate 降至 <20%（接近 det 的 16.3%），则 death dominance 不再成立 | — | — | — |\n| backbone-scaling-70b | 72B model 的 death rate 显著低于 7B (42.9%)，但 DAF 可能仍 dominant 因为 deterministic modality 的 death rate 也会降低 | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **death-risk-routing-analysis** (negative): 基于 task-type death risk 的简单 threshold routing 能否优于 always-det；如果能，说明 analytical framework 不只诊断问题还指向解决方案 ← 基于 plan-005-routing-patterns\n- **math-extension-n800** (success): MATH Level 4-5 在 N=795 下 internal > code-interpreter 效应消失（+0.5pp, p=0.81），确认无 catastrophic failure 环境中无 death-driven routing signal ← 基于 math-negative-contrast\n- **plan-008-v4-4b-e2e** (negative): 4B router (episode-level 59%) 在 end-to-end deployment 中能否超越 always-det baseline (-9.47 mean score)。若超过：larger capacity translates to marginal deployment gain at disproportionate cost。若未超过：进一步强化 analytical framework > learned routing at all tes
…[truncated 1432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-17T15:08:24.543816+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-17T15:08:24.594650+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/SETUP_NOTES.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/gen_fig1.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/fig1_daf_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/gen_signal_reversal.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/signal_reversal.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/gen_pipeline.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/pipeline_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p1.png
/home/
…[truncated 2836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-17T15:08:33.454147+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-17T15:08:34.408599+00:00_

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
35	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct); generalization requires further validation. The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface additional signal. Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}; more sophisticated strategies (e.g., Reflexion~\citep{reflexion-2023} or Tree-of-Thought backtracking~\citep{tot-2023}) may reduce internal death rates and lower DAF. Episode-level labels assign a single routing preference to entire episodes, which may be suboptimal for individual steps (particularly those preceding death events); episodes within the same task type are not fully independent because they share environment dynamics, though they use different random seeds. The mislabeling fraction (episodes where the episode-level label disagrees with what step-level oracle labels would assign) is approximately 27.7\%, concentrated in death-asymmetry episodes where early steps may have favored the eventu
…[truncated 26099 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-17T15:08:34.409042+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-17T15:08:35.411924+00:00_

1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet no systematic methodology exists for diagnosing \emph{what} drives routing decisions. We introduce an episode-level counterfactual framework that isolates death-avoidance from non-death routing signal using both penalty-independent label counting and a penalty-dependent decomposition (DAF). Applied to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), \textbf{78.9\% of non-tie routing labels} (75 of 95) arise from death asymmetry, a penalty-independent finding. Under ScienceWorld's specific penalty ($P{=}100$), the penalty-weighted DAF reaches $90.4\%$, consistent with the predicted value from observed death-rate differential $\delta{=}0.265$. A per-task consistency check yields $r{=}0.97$, confirming death dominance. A router trained on these labels reaches only $59.0\%$ episode-level balanced accuracy at 4B parameters, not outperforming always-deterministic. Cross-environment contrasts confirm framework predictions: on MATH ($N{=}795$), no routing signal without catastrophic failure ($p = 0.81$); on ALFWorld ($N{=}135$), the framework identifies information asymmetry as an alternative mechanism. We predict that stronger backbones will lower death-avoidance fractions as capability reduces catastrophic failure rates.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 1002
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-17T15:08:35.412342+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1013 · 2026-05-17T15:08:35.863580+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1014 · 2026-05-17T15:08:43.764334+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Call for Papers: NLP for Science Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/nlp-science"}]

The search results contain information about various EMNLP 2026-related calls (tutorials, workshops) but not a main conference call for papers with submission deadlines and author guidelines. Let me 
…[truncated 2990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 8351
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-17T15:08:43.815212+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7951
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-17T15:08:50.712677+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission deadline May 2026"
  }
}
```

</details>

---


### Tool call

_source line 1017 · 2026-05-17T15:08:50.813422+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May cycle submission guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May cycle submission guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 1018 · 2026-05-17T15:08:50.964279+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1019 · 2026-05-17T15:08:50.964846+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}, a text-based science simulation with 30 task types, faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	The shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.
10	But this assumption has never been systematically verified: \emph{what actually drives the value of routing decisions in interactive environments?}
11	If routing value traces to a single failure mode, practitioners can replace complex learned routers with simpler safety-aware policies at lower computational cost and deployment risk.
12	
13	We propose a \emph{formal diagnostic framework} for answeri
…[truncated 4741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1020 · 2026-05-17T15:08:57.296938+00:00_

Web search results for query: "EMNLP 2026 ARR submission deadline May 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here is the information about the EMNLP 2026 ARR submission deadline:

The ARR Submission Deadline for EMNLP 2026 is May 25, 2026.

Additionally, there are some important related deadlines and policies to note:

- After submission, all authors
…[truncated 511 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6584
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-17T15:09:04.742212+00:00_

Web search results for query: "ACL Rolling Review 2026 May cycle submission guidelines page limit"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, I found information about ACL Rolling Review submission guidelines, but I need to provide more specific information about page limits. Let me search for more detailed page limit specifications.

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review pl
…[truncated 2453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 13928
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-17T15:09:09.363603+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-17T15:09:09.364120+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-17T15:09:10.318817+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers author guidelines page limit anonymity appendix",
  "allowed_domains": "['2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers author guidelines page limit anonymity appendix",
    "allowed_domains": "['2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 1025 · 2026-05-17T15:09:12.180098+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1026 · 2026-05-17T15:09:12.231201+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment $\mathcal{E}$ with state space $\mathcal{S}$, observation space $\mathcal{O}$, and action space $\mathcal{A}$. An agent follows a policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ that maps observation histories to actions. At each step $t$, the agent receives observation $o_t$, selects action $a_t = \pi(o_1, \ldots, o_t)$, and the environment transitions to state $s_{t+1}$.
10	
11	We define a modality set $\mathcal{M} = \{{\tt int}, {\tt det}\}$ governing how the agent processes state transitions:
12	\begin{itemize}
13	    \item \textbf{Internal} ($m = {\tt int}$): The agent uses its own generation to predict intermediate observations. The LLM interleaves chain-of-thought reasoning with environment actions following the ReAct paradigm \cite{react-2023}, but prediction errors compound across steps.
14	    \item \textbf{Deterministic} ($m = {\tt det}$): The agent receives ground-truth observations from the environment simulator at each step, equivalent to access to a perfect dynamics model. Action selection remains with the LLM; only the state-transition prediction is replaced.
15	\end{itemize}
16	
17	\noindent We restrict $\mathcal{M}$ to two modaliti
…[truncated 7770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1027 · 2026-05-17T15:09:12.633235+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1028 · 2026-05-17T15:09:12.684059+00:00_

1	\section{Experiments}
2	
3	\subsection{Death Avoidance Decomposition}
4	\label{sec:death-decomp}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/fig1_daf_scatter.pdf}
9	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types.}
10	\label{fig:decomposition}
11	\end{figure}
12	
13	Across 245 episodes, $\Delta_{\text{full}} = +29.60$; excluding death episodes, $\Delta_{\text{nd}} = +2.84$, yielding DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$; at the default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\% (75 of 95 non-tie labels). Given observed $\delta = 0.265$ and $P = 100$, the predicted DAF $= \delta P / (\delta P + \Delta_{\text{nd}}) = 26.5 / 29.37 \approx 90.3\%$, closely matching the observed value; DAF is thus a derived quantity once $\delta$, $P$, and $\Delta_{\text{nd}}$ are known, while the 78.9\% label fraction is the penalty-independent empirical finding. Of these 75, 54 (72.0\%) reduce to ties when the death penalty is removed entirely: in those episodes, both modalities score zero without death, so the only reason one strategy outscored the other was avoiding the $-100$ penalty. Death avoidance is not merely the dominant but often the \emph{sole} discriminating signal between modalities. The remaining 21 death-asymmetry labels involve episodes where the surviving strategy also earned positive score, but the death penalty still accounts for the majority of the score gap.
14	
15	\paragraph{Per-task correlation structure.}
16	The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$), consistent with the internal strategy's reliance on self-generated observations that compound prediction errors across steps. Per-task, death rate differential correlates with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}). S
…[truncated 10476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1029 · 2026-05-17T15:09:16.100935+00:00_

Web search results for query: "EMNLP 2026 call for papers author guidelines page limit anonymity appendix"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"}]

I found information about EMNLP 2026. Based on the search results, here are the key details about author guidelines for the main conference papers:

**Page Limit:**
The search results reference ARR submission requirements, but the specific page limits are not explicitly stated in the main conference call for papers page. However, for the Industry Track specifically, papers have a maximum of 6 pages.

**Anonymity:**
Following the ACL and ARR policies, there is no anonymity period requirement. Additionally, the reviewing process will be double-blind, with reviewers not seeing authors and authors not seeing reviewers.

**Appendix:**
For the Industry Track, after the bibliography, papers can have an optional appendix with examples or sample inputs/outputs, pre-processing decisions, model parameters, feature templates, pseudocode, information about
…[truncated 597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 5782
}
```

</details>

---


### Tool call

_source line 1030 · 2026-05-17T15:09:22.599630+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1031 · 2026-05-17T15:09:23.102406+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}.
5	Toolformer \cite{toolformer-2023} teaches LLMs to insert API calls via self-supervised loss filtering; ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask; ReTool \cite{retool-2025} applies RL to discover when code execution is preferable to chain-of-thought.
6	These focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Recent concurrent work sharpens this question: \citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect, \citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \citet{tool-use-tax-2026} quantify a ``tool-use tax,'' and \citet{to-call-or-not-2026} propose a necessity--utility--affordability framework. Our decomposition provides environment-grounded evidence: in ScienceWorld, $90.4\%$ of routing signal at $P{=}100$ traces to catastrophic-failure prevention.
8	
9	\paragraph{Adaptive Computation and Routing.}
10	CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing.
11	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
12	These optimize \emph{how} to route; we reveal \emph{why} routing helps: in interactive environments, the dominant signal is catastrophic-failure avoidance.
13	
14	\paragraph{Counterfactual Evaluation in RL.}
15	Prior work generates counterfactual explanations for RL agents by perturbing individual 
…[truncated 1516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-17T15:09:23.102941+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-17T15:09:24.057317+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why the router fails: task-type-level signal.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10 of 11 types carry death risk), but step-level features correlate weakly with this signal because death risk depends on multi-step state trajectories, not individual action semantics. The 4B router's episode-level improvement ($59.0\%$) without step-level gains ($56$--$59\%$, flat) confirms that capacity scaling captures task-type classification rather than generalizable routing features.
6	
7	\paragraph{Scaling and self-correction predictions.}
8	Stronger backbones should lower the death-avoidance fraction as capability reduces catastrophic failure rates. The Llama pilot ($\delta = +34.3\%$) versus Qwen ($\delta = +26.6\%$) is consistent in the capability-increase direction; for 70B-class models, we predict reduced $\delta$ with routing shifting from safety-dominated to quality-dominated. Preliminary evidence (Qwen2.5-0.5B, $N{=}15$) suggests the relationship is non-monotonic: very weak models exhibit low death rates from inability to reach dangerous states. Self-correction methods (Reflexion~\citep{reflexion-2023}, Tree-of-Thought~\citep{tot-2023}) target the specific failure mode (compounding state hallucination) and should reduce $\delta$ even without general capability gains. Both predictions are testable by substituting the internal-strategy implementation within the existing framework.
9	
10	\paragraph{DAF as penalty-dependent diagnostic.}
11	DAF is a derived quantity ($\delta P / (\delta P + \Delta_{\text{nd}})$) that increases monotonically with $P$ (Appendix~\ref{app:penalty}). The penalty-independent label fraction (78.9\%) is more informative as a primary diagnostic: it counts routing preferences attributable to death asymmetry regardless of penalty magnitude. The $r = 0.97$ per-task correlation (\S\ref{s
…[truncated 807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-17T15:09:24.057758+00:00_

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
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-17T15:09:24.509731+00:00_

1	\section{Conclusion}
2	
3	We presented a formal diagnostic framework for decomposing routing signal in modular LLM agents via episode-level counterfactual analysis with dual metrics (penalty-independent label fraction and penalty-dependent DAF). Applied to 245 ScienceWorld episodes (11 of 30 task types, Qwen2.5-7B-Instruct), death asymmetry accounts for 78.9\% of non-tie routing labels; DAF $= 90.4\%$ at $P{=}100$ (95\% CI: $[81.6\%, 98.8\%]$). Cross-domain contrasts support framework predictions: MATH shows no routing signal without catastrophic failure; ALFWorld provides an illustrative contrast where information asymmetry drives routing under different modality definitions; a preliminary Llama pilot ($N{=}70$) shows directional consistency across model families. Open directions include replication in catastrophic-failure environments (e.g., NetHack~\citep{nethack-2020}, Crafter~\citep{crafter-2022}) and stronger backbones, which the framework predicts will lower DAF.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-17T15:09:24.510165+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-17T15:09:24.560623+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-17T15:09:32.143245+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission requirements: page limits (long/short), template, anonymity rules, appendix rules, citation format, mandatory sections (limitations, ethics), responsible NLP checklist, deadline details, and any special instructions for the ARR May 2026 cycle."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission requirements: page limits (long/short), template, anonymity rules, appendix rules, citation format, mandatory sections (limitations, ethics), responsible NLP checklist, deadline details, and any special instructions for the ARR May 2026 cycle."
  }
}
```

</details>

---


### Tool call

_source line 1039 · 2026-05-17T15:09:34.052431+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract all submission requirements: page limits (long/short), template, anonymity rules, appendix rules, citation format, mandatory sections (limitations, ethics), responsible NLP checklist requirements, and formatting guidelines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract all submission requirements: page limits (long/short), template, anonymity rules, appendix rules, citation format, mandatory sections (limitations, ethics), responsible NLP checklist requirements, and formatting guidelines."
  }
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-17T15:09:34.805814+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "literature_map.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "literature_map.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-17T15:09:37.785572+00:00_

# EMNLP 2026 Submission Requirements Summary

## Page Limits
- **Long Papers:** 8 pages (9 pages in camera-ready version)
- **Short Papers:** 4 pages (5 pages in camera-ready version)

## Key Deadlines for ARR May 2026 Cycle
- ARR submission: May 25, 2026
- Reviewer registration: May 27, 2026
- EMNLP commitment: August 2, 2026
- Acceptance notification: August 20, 2026
- Camera-ready due: September 20, 2026

*All deadlines are 11:59 PM UTC-12:00 ("anywhere on Earth")*

## Special ARR May 2026 Policy
"authors will need to explicitly declare which conference they intend to commit to at submission time" (EMNLP or AACL). This selection is binding—papers not selecting EMNLP cannot later commit to it.

## Anonymity & Review Process
- Double-blind reviewing maintained
- "there is no anonymity period requirement" per ACL/ARR policies
- Authors may make anonymized submissions publicly visible through ARR

## Mandatory Requirements
- **Limitations section** required
- **Ethics checklist:** Responsible NLP research checklist compliance mandatory
- **Publication Ethics:** Adherence to ACL Policy on Publication Ethics required
- **Disclosure Policy:** ACL's coordinated disclosure policy applies
- **Writing assistance** permitted (AI tools allowed with proper disclosure)

## Additional Guidelines
All submissions must follow ARR requirements for authorship, citation standards, multiple submission policies, and resubmission guidelines. Two-way anonymized review instructions apply. Supplementary materials, appendices, software, and data are optional.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "elapsed_ms": 5642
}
```

</details>

---


### Tool result

_source line 1042 · 2026-05-17T15:09:42.441286+00:00_

# ACL Rolling Review Submission Requirements

## Page Limits

**Long Papers:** Up to 8 pages of content + unlimited references + unlimited space for required limitations section and optional ethical considerations section

**Short Papers:** Up to 4 pages of content + unlimited references + unlimited space for required limitations section and optional ethical considerations section

## Template & Formatting

- Must use the "official ACL style template" available on GitHub
- Follow "*ACL" conference formatting guidelines from acl-org.github.io/ACLPUB/formatting.html
- No modifications to style files permitted
- Appendices must follow double-column format (with approved exceptions)
- Papers not conforming to required styles will be rejected without review

## Anonymity Rules

Papers must not include author names, affiliations, or self-identifying citations (e.g., avoid "We previously showed"). Use constructions like "Smith previously showed (Smith, 1991)…" instead.

Supplementary materials and links must be anonymized. "Links to file hosting services that can track downloads, such as Dropbox, are not allowed." Use anonymous repositories for code.

## Mandatory Sections

1. **Limitations Section (Required):** Dedicated section at paper end before references; does not count toward page limit. Papers lacking this section face desk rejection.

2. **Responsible NLP Checklist:** "Incorrect, incomplete or misleading information in the checklist can result in desk rejection." Metadata remains editable for 48 hours post-deadline.

3. **Ethical Considerations (Recommended):** Optional dedicated section addressing ethical impact; does not count toward page limit.

## Citation Format for Concurrent Work

For unpublished overlapping papers by the same authors: `Anonymous (2026). Paper title. Under review.`

Anonymized versions should be included as supplementary material.

## Appendices Rules

Appendices follow the main text after references and don't count toward page limits. Howe
…[truncated 198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebFetch",
  "elapsed_ms": 8388
}
```

</details>

---


### Tool result

_source line 1043 · 2026-05-17T15:09:42.492106+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/literature_map.yaml\", \"content\": \"# Literature Map — simgate-modular-routing\\n# Last updated: 2026-05-14\\n# Scan scope: 2025-2026 incremental scan + existing references from paper_framing.md\\n\\n# ============================================================\\n# CATEGORY: Direct Competitors (novelty threat)\\n# ============================================================\\ndirect_competitors: []\\n# None found. No 2025-2026 paper claims death/safety avoidance\\n# as the dominant routing signal in LLM agent systems.\\n\\n# ============================================================\\n# CATEGORY: ScienceWorld Agent Baselines (must-cite)\\n# ============================================================\\nscienceworld_baselines:\\n  - id: cogrouter-2026\\n    title: \\\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv:2602.12662, Feb 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      SOTA on ScienceWorld (82.3% with Qwen2.5-7B). Routes between cognitive\\n      depth levels (instinct to strategic planning) via CoPO, not between\\n      internal vs deterministic computation. Does not analyze WHAT drives\\n      routing signal. Cite as SOTA baseline and adaptive computation related work.\\n    our_differentiation: >\\n      CogRouter optimizes HOW MUCH to think; we analyze WHAT routing learns\\n      (death avoidance = 99%). Different routing dimensions (depth vs modality).\\n\\n  - id: itp-2026\\n    title: \\\"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv:2601.08955, Jan 2026\\\"\\n    relation: complementary\\n    relevance: high\\n    summary: >\\n      Extends POIMDP with world model lookahead on ScienceWorld/ALFWorld/
…[truncated 1489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7686
}
```

</details>

---


### Tool call

_source line 1044 · 2026-05-17T15:09:47.365829+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-17T15:09:47.819161+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-17T15:09:48.271832+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1047 · 2026-05-17T15:09:49.139975+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\", \"content\": \"# Paper Framing — simgate-modular-routing\\n\\n## Target Venue\\n- **EMNLP 2026 Main Conference — Long Paper (8 pages + references)**\\n- Deadline: ARR May 25, 2026 (10 days remaining)\\n- D050: Upgraded from short paper (4p, Findings) per user directive\\n\\n## Core Insight\\n\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 97.4% ties in sparse-reward settings) and discover that **death avoidance accounts for ~90% of routing signal** on ScienceWorld (Δ_full=+29.60 [A], Δ_nd=+2.84 [A], DAF=90.41% [A]; Pearson r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). Non-death performance difference is small but non-negligible (Δ_nd/Δ_full=9.6% [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\n\\n## Core Claims (3 claims for long paper)\\n\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (Δ_full=+29.60 [A]), with **death avoidance as the dominant mechanism** (90.41% of the performance gap [A], measured by Δ decomposition; plan-012-full, 11 tasks / 245 eps [A]). Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 (out of 245 episodes) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Non-death score de
…[truncated 3353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 868
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-17T15:09:49.241194+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-17T15:09:49.442757+00:00_

- id: "R13-N1"
  summary: "DAF 核心发现与环境惩罚结构存在部分 tautology，framing 仍过度强调经验发现"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 13
  last_seen_round: 13
  mentions:
    - round: 13
      reviewers: [1, 2]
      note: "Consensus. DAF=90.4% 和 r=0.97 是 P=100 的代数后果（P=10 时 DAF=50.4%）。78.9% penalty-independent metric 更有信息量但在叙事中不够突出。R1 建议 predictability analysis 量化 predicted vs observed deviation。"
  action_items:
    - round: 13
      action: "以 78.9% penalty-independent label fraction 为 primary metric，DAF 降级为 supplementary；增加 predictability analysis；Abstract/Introduction 中降低对 DAF 数值的依赖"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R13-N2"
  summary: "统计推断可靠性不足：cluster bootstrap K=11、per-task n=20、Llama pilot N=70"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 13
  last_seen_round: 13
  mentions:
    - round: 13
      reviewers: [1, 2]
      note: "Consensus. (a) Cluster bootstrap K=11 远低于 Cameron et al. K≥40 门槛，CI [73.3%, 100%] 不可靠; (b) episode 独立性假设不满足; (c) per-task n=20 CI 极宽，chemistry-mix CI跨零; (d) Llama pilot N=70 只能排除 internal-preferred rate 上界约 4.2%。论文 headline 用点估计而非 CI 叙事有 cherry-picking 嫌疑。"
  action_items:
    - round: 13
      action: "对 cluster bootstrap K=11 做更诚实讨论或使用替代方法；Llama pilot 降级为 anecdotal evidence；per-task 结果报告时体现 uncertainty；headline 使用 CI 而非仅点估计"
      assigned_to: paper_agent
      status: in_progress
  resolution: ""
  resolution_round: null

- id: "R13-N3"
  summary: "跨环境证据不足以支撑 Contribution 3——无第二个 catastrophic-failure 环境 replication"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 13
  last_seen_round: 13
  mentions:
    - round: 13
      reviewers: [1, 2]
      note: "Consensus. MATH 是 predicted null（弱检验）；ALFWorld modality 定义根本不同（information asymmetry vs computation mode）；Llama pilot 样本量过小。三者均不构成 DAF 框架的 replication。最关键缺失：无第二个具有 catastrophic failure 的环境（如 NetHack/Crafter）。
…[truncated 5951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-17T15:10:22.531709+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing && grep -r \"external_review\" config.yaml 2>/dev/null || grep -r \"paperreview\" config.yaml 2>/dev/null || echo \"NOT_FOUND_IN_CONFIG\"",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing && grep -r \"external_review\" config.yaml 2>/dev/null || grep -r \"paperreview\" config.yaml 2>/dev/null || echo \"NOT_FOUND_IN_CONFIG\"",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1051 · 2026-05-17T15:10:23.387280+00:00_

NOT_FOUND_IN_CONFIG
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_director_19d7e797

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-17T15:10:23.437871+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-17T15:10:23.991907+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf (423.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 1054 · 2026-05-17T15:10:30.785079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
  "pages": "9-12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf",
    "pages": "9-12"
  }
}
```

</details>

---


### Tool call

_source line 1055 · 2026-05-17T15:10:30.986348+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1056 · 2026-05-17T15:10:31.037291+00:00_

1	@inproceedings{scienceworld-2022,
2	  title={ScienceWorld: Is Your Agent Smarter Than a 5th Grader?},
3	  author={Wang, Ruoyao and Jansen, Peter and C\^{o}t\'{e}, Marc-Alexandre and Ammanabrolu, Prithviraj},
4	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
5	  year={2022}
6	}
7	
8	@inproceedings{react-2023,
9	  title={ReAct: Synergizing Reasoning and Acting in Language Models},
10	  author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
11	  booktitle={International Conference on Learning Representations (ICLR)},
12	  year={2023}
13	}
14	
15	@inproceedings{toolformer-2023,
16	  title={Toolformer: Language Models Can Teach Themselves to Use Tools},
17	  author={Schick, Timo and Dwivedi-Yu, Jane and Dess\`{i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
18	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
19	  year={2023}
20	}
21	
22	@article{art-2023,
23	  title={ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models},
24	  author={Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio},
25	  journal={arXiv preprint arXiv:2303.09014},
26	  year={2023}
27	}
28	
29	@inproceedings{chameleon-2023,
30	  title={Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models},
31	  author={Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng},
32	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
33	  year={2023}
34	}
35	
36	@article{retool-2025,
37	  title={ReTool: Reinforcement Learning for Strategic Tool Use in LLMs},
38	  author={Feng, Jiazhan and Huang, Shijue and Qu, Xingwei and Zhang, Ge and Qin, Yujia and others},
39	  j
…[truncated 9967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1057 · 2026-05-17T15:10:31.088103+00:00_

PDF pages extracted: 4 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf (423.3KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1058 · 2026-05-17T15:11:46.959046+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 审稿任务 — Reviewer 1（方法严谨性 + 实验充分性）\n\n### 论文信息\n- **标题**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/`（main.tex + 分文件；已编译 main.pdf）\n- **目标 Venue**: EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **Deadline**: 2026-05-25\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 不限参考文献 + 不限 Limitations/Ethics\n- ACL 模板（`\\usepackage[review]{acl}`）\n- Double-blind 匿名审稿\n- Limitations section 必须有（否则 desk reject）\n- Responsible NLP Checklist 必须正确填写\n- 附录在参考文献后，不计入页数，但审稿人无义务审阅附录\n- EMNLP 2026 评分标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重\n\n**核心职责：评估方法的数学严谨性和实验证据的充分性。**\n\n请重点关注以下方面：\n\n1. **DAF 框架的数学基础**\n   - DAF = δP/(δP + Δ_nd) 是否存在 tautology 问题？当 P 固定时，DAF 和 r=0.97 是否仅为代数后果？\n   - penalty-independent metric（78.9% label fraction）vs penalty-dependent metric（DAF=90.4%）的关系是否在论文中被准确 framed？\n   - 分解公式的近似条件（surviving strategy scores zero）是否充分讨论？\n\n2. **统计推断可靠性**\n   - N=245 的样本量是否足以支撑结论？Bootstrap CI 的有效性？\n   - Cluster bootstrap K=11 是否满足 Cameron et al. (2008) K≥40 的要求？论文是否诚实讨论了这一局限？\n   - Per-task n=20 的 CI 宽度是否允许有意义的推断？\n   - Episode 独立性假设是否合理（共享 environment dynamics）？\n\n3. **Router 训练实验**\n   - Episode-level label → step-level training 的 label noise 是否被量化？27.7% mislabeling fraction 是否在正文中充分讨论？\n   - Augmentation scaling 是否被不当等同于 real data scaling？结论是否过强？\n   - 1.7B 的 non-monotonic dip（43.1%）是否有可检验的解释？\n   - 4B end-to-end deployment 与 baselines 的比较是否在统一条件下？\n\n4. **跨环境证据**\n   - MATH 作为 predicted null（弱检验）是否被过度解读？\n   - ALFWorld 的 modality 定义（information asymmetry vs computation mode）是否与 ScienceWorld 可比？\n   - Llama pilot N=70 能支撑多强的结论？\n   - 是否缺少第二个 catastrophic-failure 环境的 replication（如 NetHack/Crafter）？\n\n5. **实验设计整体性**\n   - 11/30 task types 的选择是否存在 selection bias？prescreening 是否充分 justified？\n   - 30-step budget 是否过于限制，导致 19 个 excluded task types 可能包含有价值信号？\n   - \"Deterministic\" modality（ground-truth observations）在实际部署中是否 realistic？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出，标注 W1, W2, ...，按严重程度排序：Must-Fix / Should-Fix / Minor]\n\n## Questions\n[需要作者澄清的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Overall Assessment\n[评分 + 置信度 + 简要理由]\n评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit, 1.5=Resubmit after next, 1=Do not resubmit\n```",
  "project": "simgate-modular-routing"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 审稿任务 — Reviewer 1（方法严谨性 + 实验充分性）\n\n### 论文信息\n- **标题**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/`（main.tex + 分文件；已编译 main.pdf）\n- **目标 Venue**: EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **Deadline**: 2026-05-25\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 不限参考文献 + 不限 Limitations/Ethics\n- ACL 模板（`\\usepackage[review]{acl}`）\n- Double-blind 匿名审稿\n- Limitations section 必须有（否则 desk reject）\n- Responsible NLP Checklist 必须正确填写\n- 附录在参考文献后，不计入页数，但审稿人无义务审阅附录\n- EMNLP 2026 评分标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重\n\n**核心职责：评估方法的数学严谨性和实验证据的充分性。**\n\n请重点关注以下方面：\n\n1. **DAF 框架的数学基础**\n   - DAF = δP/(δP + Δ_nd) 是否存在 tautology 问题？当 P 固定时，DAF 和 r=0.97 是否仅为代数后果？\n   - penalty-independent metric（78.9% label fraction）vs penalty-dependent metric（DAF=90.4%）的关系是否在论文中被准确 framed？\n   - 分解公式的近似条件（surviving strategy scores zero）是否充分讨论？\n\n2. **统计推断可靠性**\n   - N=245 的样本量是否足以支撑结论？Bootstrap CI 的有效性？\n   - Cluster bootstrap K=11 是否满足 Cameron et al. (2008) K≥40 的要求？论文是否诚实讨论了这一局限？\n   - Per-task n=20 的 CI 宽度是否允许有意义的推断？\n   - Episode 独立性假设是否合理（共享 environment dynamics）？\n\n3. **Router 训练实验**\n   - Episode-level label → step-level training 的 label noise 是否被量化？27.7% mislabeling fraction 是否在正文中充分讨论？\n   - Augmentation scaling 是否被不当等同于 real data scaling？结论是否过强？\n   - 1.7B 的 non-monotonic dip（43.1%）是否有可检验的解释？\n   - 4B end-to-end deployment 与 baselines 的比较是否在统一条件下？\n\n4. **跨环境证据**\n   - MATH 作为 predicted null（弱检验）是否被过度解读？\n   - ALFWorld 的 modality 定义（information asymmetry vs computation mode）是否与 ScienceWorld 可比？\n   - Llama pilot N=70 能支撑多强的结论？\n   - 是否缺少第二个 catastrophic-failure 环境的 replication（如 NetHack/Crafter）？\n\n5. **实验设计整体性**\n   - 11/30 task types 的选择是否存在 selection bias？prescreening 是否充分 justified？\n   - 30-step budget 是否过于限制，导致 19 个 excluded task types 可能包含有价值信号？\n   - \"Deterministic\" modality（ground-truth observations）在实际部署中是否 realistic？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出，标注 W1, W2, ...，按严重程度排序：Must-Fix / Should-Fix / Minor]\n\n## Questions\n[需要作者澄清的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Overall Assessment\n[评分 + 置信度 + 简要理由]\n评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit, 1.5=Resubmit after next, 1=Do not resubmit\n```",
    "project": "simgate-modular-routing"
  }
}
````

</details>

---


### Tool result

_source line 1059 · 2026-05-17T15:12:15.086633+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 28127
}
```

</details>

---


### Tool call

_source line 1060 · 2026-05-17T15:12:15.291293+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### 论文信息\n- **标题**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/`（main.tex + 分文件；已编译 main.pdf）\n- **目标 Venue**: EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **Deadline**: 2026-05-25\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 不限参考文献 + 不限 Limitations/Ethics\n- ACL 模板（`\\usepackage[review]{acl}`）\n- Double-blind 匿名审稿\n- Limitations section 必须有（否则 desk reject）\n- Responsible NLP Checklist 必须正确填写\n- 附录在参考文献后，不计入页数，但审稿人无义务审阅附录\n- EMNLP 2026 评分标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重\n\n**核心职责：评估贡献的新颖性、论文的完整性和写作质量。**\n\n请重点关注以下方面：\n\n1. **新颖性和贡献定位**\n   - \"Death avoidance dominates routing signal\" 这一发现的 novelty 有多强？是否属于 obvious-in-hindsight（一旦意识到 -100 penalty，结论就 trivial）？\n   - Episode-level counterfactual labeling 作为方法论贡献是否有足够的 novelty？与已有的 counterfactual RL 工作（Olson 2021, Gajcin 2023, Amitai 2024）的区分是否清晰？\n   - DAF metric 本身（Gini coefficient rename 为 SCI + 简单分解公式）是否构成足够的方法贡献？\n   - 对 EMNLP Findings 的贡献门槛是否达到？\n\n2. **Related Work 完整性**\n   - Tool use routing 的引用是否充分覆盖 2025-2026 最新工作？\n   - Safe RL 的引用是否过于单薄（仅 Garcia 2015 + CRPO 2021）？\n   - LLM agent failure mode analysis 相关工作是否被覆盖？\n   - Concurrent work（Zeng 2026, Sun 2026, Zhang 2026, Wu 2026）的讨论是否充分？\n   - 是否有遗漏的重要 baseline 或 benchmark 引用？\n\n3. **叙事连贯性**\n   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成一条清晰主线？\n   - 三个 Contributions 是否都有充分的 section/table 支撑？\n   - \"negative result\"（router 不 work）在叙事中的定位是否恰当——是贡献还是局限？\n   - 跨环境对比的叙事定位是否准确（preliminary evidence vs strong claim）？\n\n4. **写作质量（严格按照 AI 写作检查标准）**\n   - 检查所有 em-dash（—）和解释性 en-dash（–）的使用\n   - 检查 -ing 短语结尾（\"..., highlighting...\", \"..., demonstrating...\"）\n   - 检查连续过渡词（Furthermore/Moreover/Additionally）\n   - 检查用词黑名单（delve, leverage, utilize, facilitate, myriad, plethora）\n   - 检查过度分段（是否每 2-3 句就换段）\n   - Abstract 是否数字堆砌？是否在 30 秒内可判断价值？\n   - 专有名词/缩写是否首次出现时有定义（包括 Abstract 中的）？\n\n5. **格式合规性**\n   - 页数是否满足 8 页限制？正文内容（不含 Limitations/Ethics/References）是否在 8 页内？\n   - Limitations section 是否充分？是否会触发 desk reject？\n   - Ethics Statement 是否充分？\n   - 参考文献格式是否统一（检查 \"and others\" vs 完整作者列表）？\n   - 图表 caption 是否 self-contained？\n   - 匿名化是否到位（无泄露作者身份的内容）？\n\n6. **图表质量**\n   - Figure 1（pipeline）信息密度是否足够？\n   - Figure 2（scatter plot）标注是否清晰？\n   - Figure 3（signal reversal）是否遗漏了 ALFWorld 数据？Text 中 N=795 但 Figure 中 N=300 的不一致？\n   - Table 1-2 的 caption 是否 self-contained？数据精度是否统一？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出，标注 W1, W2, ...，按严重程度排序：Must-Fix / Should-Fix / Minor]\n\n## Questions\n[需要作者澄清的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Overall Assessment\n[评分 + 置信度 + 简要理由]\n评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit, 1.5=Resubmit after next, 1=Do not resubmit\n```",
  "project": "simgate-modular-routing"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### 论文信息\n- **标题**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/`（main.tex + 分文件；已编译 main.pdf）\n- **目标 Venue**: EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **Deadline**: 2026-05-25\n\n### Venue 格式要求\n- Long paper: 8 页正文 + 不限参考文献 + 不限 Limitations/Ethics\n- ACL 模板（`\\usepackage[review]{acl}`）\n- Double-blind 匿名审稿\n- Limitations section 必须有（否则 desk reject）\n- Responsible NLP Checklist 必须正确填写\n- 附录在参考文献后，不计入页数，但审稿人无义务审阅附录\n- EMNLP 2026 评分标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查侧重\n\n**核心职责：评估贡献的新颖性、论文的完整性和写作质量。**\n\n请重点关注以下方面：\n\n1. **新颖性和贡献定位**\n   - \"Death avoidance dominates routing signal\" 这一发现的 novelty 有多强？是否属于 obvious-in-hindsight（一旦意识到 -100 penalty，结论就 trivial）？\n   - Episode-level counterfactual labeling 作为方法论贡献是否有足够的 novelty？与已有的 counterfactual RL 工作（Olson 2021, Gajcin 2023, Amitai 2024）的区分是否清晰？\n   - DAF metric 本身（Gini coefficient rename 为 SCI + 简单分解公式）是否构成足够的方法贡献？\n   - 对 EMNLP Findings 的贡献门槛是否达到？\n\n2. **Related Work 完整性**\n   - Tool use routing 的引用是否充分覆盖 2025-2026 最新工作？\n   - Safe RL 的引用是否过于单薄（仅 Garcia 2015 + CRPO 2021）？\n   - LLM agent failure mode analysis 相关工作是否被覆盖？\n   - Concurrent work（Zeng 2026, Sun 2026, Zhang 2026, Wu 2026）的讨论是否充分？\n   - 是否有遗漏的重要 baseline 或 benchmark 引用？\n\n3. **叙事连贯性**\n   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成一条清晰主线？\n   - 三个 Contributions 是否都有充分的 section/table 支撑？\n   - \"negative result\"（router 不 work）在叙事中的定位是否恰当——是贡献还是局限？\n   - 跨环境对比的叙事定位是否准确（preliminary evidence vs strong claim）？\n\n4. **写作质量（严格按照 AI 写作检查标准）**\n   - 检查所有 em-dash（—）和解释性 en-dash（–）的使用\n   - 检查 -ing 短语结尾（\"..., highlighting...\", \"..., demonstrating...\"）\n   - 检查连续过渡词（Furthermore/Moreover/Additionally）\n   - 检查用词黑名单（delve, leverage, utilize, facilitate, myriad, plethora）\n   - 检查过度分段（是否每 2-3 句就换段）\n   - Abstract 是否数字堆砌？是否在 30 秒内可判断价值？\n   - 专有名词/缩写是否首次出现时有定义（包括 Abstract 中的）？\n\n5. **格式合规性**\n   - 页数是否满足 8 页限制？正文内容（不含 Limitations/Ethics/References）是否在 8 页内？\n   - Limitations section 是否充分？是否会触发 desk reject？\n   - Ethics Statement 是否充分？\n   - 参考文献格式是否统一（检查 \"and others\" vs 完整作者列表）？\n   - 图表 caption 是否 self-contained？\n   - 匿名化是否到位（无泄露作者身份的内容）？\n\n6. **图表质量**\n   - Figure 1（pipeline）信息密度是否足够？\n   - Figure 2（scatter plot）标注是否清晰？\n   - Figure 3（signal reversal）是否遗漏了 ALFWorld 数据？Text 中 N=795 但 Figure 中 N=300 的不一致？\n   - Table 1-2 的 caption 是否 self-contained？数据精度是否统一？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出，标注 W1, W2, ...，按严重程度排序：Must-Fix / Should-Fix / Minor]\n\n## Questions\n[需要作者澄清的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Overall Assessment\n[评分 + 置信度 + 简要理由]\n评分标准：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit, 1.5=Resubmit after next, 1=Do not resubmit\n```",
    "project": "simgate-modular-routing"
  }
}
````

</details>

---


### Tool result

_source line 1061 · 2026-05-17T15:12:16.711294+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1419
}
```

</details>

---


### Assistant

_source line 1062 · 2026-05-17T15:12:30.329191+00:00_

Round 1 独立审稿已启动。Reviewer 1（方法严谨性 + 实验充分性）和 Reviewer 2（新颖性 + 完整性 + 写作质量）已收到任务，等待审稿结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 96

## Round 96

2 recorded events
