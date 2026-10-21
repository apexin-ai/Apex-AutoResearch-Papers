# research check tex math data

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_research_check-tex-math-data_20260517T145024.jsonl`
- **Structured JSON:** [`ab2227a0c9be7a1c0b44.json`](../../sessions/ab/ab2227a0c9be7a1c0b44.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-17T14:51:55.408752+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T14:51:55.409145+00:00_

artifacts/dream_reports/dream_20260513T153257/best/paper.tex
artifacts/dream_reports/dream_20260513T153257/median/paper.tex
artifacts/dream_reports/dream_20260513T153257/worst/paper.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/main_b09c23.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/conclusion.tex
artifacts/penalty_sensitivity_table.tex
artifacts/plan-012-penalty-sensitivity/report/penalty_sensitivity_table.tex
artifacts/_project/paper/latex/experiments.tex
artifacts/_project/paper/latex/method.tex
artifacts/_project/paper/latex/abstract.tex
artifacts/_project/paper/latex/related_work.tex
artifacts/_project/paper/latex/introduction.tex
artifacts/_project/paper/latex/conclusion.tex
artifacts/_project/paper/latex/main.tex
artifacts/_project/paper/cross_env_summary_table.tex
artifacts/_project/paper/latex/discussion.tex
artifacts/plan-012-penalty-curve/data/penalty_sensitivity_table.tex
docs/paper/abstract.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/experiments.tex
docs/paper/related_work.tex
docs/paper/discussion.tex
docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T14:51:55.409336+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "MATH|N=300|N=795|N=800|4\\.3pp|0\\.079|p<0\\.05|p=0\\.81|death.driven|0\\.5pp",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Grep",
  "tool_args": {
    "pattern": "MATH|N=300|N=795|N=800|4\\.3pp|0\\.079|p<0\\.05|p=0\\.81|death.driven|0\\.5pp",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T14:51:55.409513+00:00_

artifacts/dream_reports/dream_20260513T153257/best/paper.tex:248:Preliminary results on MATH (Level 4--5) show SimGate-style routing to a code interpreter achieves 71.4\% accuracy (vs.\ 58.2\% always-internal, 64.8\% always-code; Appendix~\ref{app:math}), suggesting the framework generalizes to other forms of deterministic computation.
artifacts/dream_reports/dream_20260513T153257/best/paper.tex:409:\section{MATH Track: Code Interpreter Routing}
artifacts/dream_reports/dream_20260513T153257/best/paper.tex:412:To test framework generalization, we apply SimGate-style routing on 500 MATH Level 4--5 problems with 3-way routing: fast-internal / deep-internal / code-interpreter.
artifacts/dream_reports/dream_20260513T153257/best/paper.tex:429:\caption{MATH Level 4--5 results with code-interpreter routing.}
artifacts/dream_reports/dream_20260513T153257/worst/paper.tex:243:We evaluate on a single environment (ScienceWorld) with one backbone (Qwen2.5-7B). The counterfactual methodology is computationally expensive (35 GPU-hours for trajectory collection alone). Our task-type taxonomy (death-risk/marginal/low-risk) is manually defined; automated task categorization remains future work. We do not evaluate on mathematical reasoning (MATH with code interpreter routing), which may exhibit different task-dependency patterns.
artifacts/dream_reports/dream_20260513T153257/median/paper.tex:252:\subsection{Generalization: MATH Track}
artifacts/dream_reports/dream_20260513T153257/median/paper.tex:254:[Omitted long matching line]
artifacts/dream_reports/dream_20260513T153257/median/paper.tex:269:\caption{MATH Track (Level 4--5, $n{=}500$). Code\%: code interpreter invocation ratio. CompErr\%: computation error rate.}
artifacts/dream_reports/dream_20260513T153257/median/paper.tex:305:\paragraph{Limitations.} SimGate does not exceed CogRouter's 84.6 score, primarily because our SFT router lacks positive guidance signal---it prevents failures but does not steer toward better strategies. Th
…[truncated 3840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T14:51:55.409710+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/cross_env_summary_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/cross_env_summary_table.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T14:51:55.409857+00:00_

1	\begin{table}[t]
2	\centering
3	\caption{Cross-environment label distribution comparison. Signal direction reverses between ScienceWorld and MATH: deterministic routing dominates in environments with catastrophic failure (death penalty), while internal reasoning is preferred in purely logical domains.}
4	\label{tab:cross-env-summary}
5	\resizebox{\columnwidth}{!}{%
6	\begin{tabular}{lcccccl}
7	\toprule
8	\textbf{Environment} & \textbf{N} & \textbf{Det\%} & \textbf{Int\%} & \textbf{No-pref\%} & \textbf{Death?} & \textbf{Signal Direction} \\
9	\midrule
10	ScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) & det $\gg$ int \\
11	MATH         & 300 &  5.7 & 10.0 & 84.3 & No            & int $>$ det \\
12	ALFWorld     & 135 & 25.9 &  1.5 & 72.6 & No$^*$        & det $\gg$ int$^\dagger$ \\
13	\bottomrule
14	\end{tabular}%
15	}
16	\vspace{2pt}
17	{\footnotesize $^\dagger$\,ALFWorld signal driven by capability gap (3\% internal success rate), not death avoidance. \\
18	$^*$\,No explicit death penalty; deterministic preference reflects tool-use capability advantage.}
19	\end{table}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T14:51:55.410035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T14:51:55.410226+00:00_

1	\section{Conclusion}
2	
3	We presented an episode-level counterfactual analysis methodology for diagnosing routing behavior in modular LLM agent systems. Applied to 245 episodes across 11 ScienceWorld task types, our analysis reveals that death avoidance accounts for 90.41\% of the routing signal between internal LLM reasoning and deterministic computation ($\Delta_{\text{full}}$ = +29.60 vs.\ $\Delta_{\text{nd}}$ = +2.84). This concentration is corroborated by a near-perfect correlation between per-task death rate differentials and routing benefit ($r$ = 0.9698, $p$ = 8.12$\times$10$^{-7}$), the oracle router's 96.2\% agreement with always-deterministic, and a trained router's near-random balanced accuracy of 58.1\%.
4	
5	Our study has several limitations. The analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and the $-100$ death penalty may amplify the measured DAF. Future work should extend to step-level counterfactual labeling for finer-grained diagnostics, evaluate generalization to environments with different failure modes (e.g., MATH, ALFWorld), and investigate whether stronger backbones exhibit richer non-death routing signals.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T14:51:55.410363+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T14:51:55.410491+00:00_

1	\section{Conclusion}
2	
3	We presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Applied to 245 episodes across 11 ScienceWorld task types, death avoidance accounts for 90.41\% of the routing signal ($\Delta_{\text{full}}$ = +29.60 vs.\ $\Delta_{\text{nd}}$ = +2.84), corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.3\% agreement with always-deterministic), and near-random trained-router accuracy (58.1\%). A preliminary MATH pilot (50 problems) and an exploratory ALFWorld study (135 games) provide cross-environment evidence: MATH shows vanishing routing signal absent catastrophic failure, while ALFWorld exhibits the same deterministic-preferred asymmetry (25.9\% vs.\ 1.5\%)---consistent with death avoidance as the structural driver rather than a ScienceWorld artifact.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T14:51:55.410621+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T14:51:55.410750+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Cross-environment evidence.}
5	The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? An evaluation on 300 MATH Level~4--5 problems, using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 81.0\% accuracy versus 76.7\% for code interpreter (McNemar's test, $p=0.079$), with 84.3\% of problems showing no modality preference (label distribution: 17 deterministic-preferred, 30 internal-preferred, 253 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld.
6	
7	\paragraph{Scope and future directions.}
8	Our analysis is grounded in a single interactive environment with a specific failure mode (the $-100$ death penalty). Extending the counterfactual methodology to environments with graded failure costs, embodied agents with continuous action spaces, or multi-turn dialogue systems would clarify how broadly death avoidance---or analogous catastrophic-failure avoidance---accounts for apparent routing signal. Step-level counterfactual labeling, rather than episode-level, is a complementary direction that could reveal finer-grained routing structure masked by our current aggregation.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T14:51:55.410877+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T14:51:55.411082+00:00_

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
21	\input{conclusion}
22	
23	\section*{Limitations}
24	
25	Our analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold.
26	
27	\paragraph{Cross-environment evidence.}
28	A preliminary 50-problem MATH Level~4--5 pilot, using code interpreter as the deterministic modality, provides initial evidence beyond ScienceWorld. Internal reasoning achieved 80\% accuracy versus 72\% for code interpreter, with 88\% of problems showing no modality preference (1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver. An exploratory ALFWorld study (135 games, 6 task types) shows a similar asymmetry: 25.9\% of episodes are deterministic-preferred versus 1.5\% internal-preferred, with deterministic success rate (27.4\%) far exceeding internal (3.0\%). While ALFWorld lacks ScienceWorld's explicit death penalty, task failure under internal reasoning is near-total, suggesting that catastrophic failure avoidance generalizes beyond environments with formal death mechanics.
29	
30	\paragraph{Scope.}
31	Extending the counterfactual methodology to environments with graded failure costs, embodied a
…[truncated 3466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T14:51:55.411252+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T14:51:55.411451+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T14:51:55.411598+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T14:51:55.411734+00:00_

1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet no systematic methodology exists for diagnosing \emph{what} drives routing decisions. We introduce an episode-level counterfactual framework using penalty-independent and penalty-dependent decomposition that isolates death-avoidance from non-death routing signal, requiring only paired episode outcomes with binary success/failure indicators. Applied to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), the framework reveals that \textbf{78.9\% of non-tie routing labels} (75 of 95) arise from death asymmetry (penalty-independent); the penalty-weighted DAF $= 90.4\%$ at $P{=}100$. The per-task $r{=}0.97$ follows algebraically from death dominance when $P$ is constant. A router trained on these labels reaches only $59.0\%$ episode-level balanced accuracy at 4B parameters, failing to outperform always-deterministic. Cross-environment contrasts confirm framework predictions: on MATH ($N{=}795$), no routing signal without catastrophic failure ($p = 0.81$); on ALFWorld ($N{=}135$), the framework identifies information asymmetry as an alternative mechanism. A Llama-3.1-8B-Instruct pilot confirms directional consistency across model families. We predict that stronger backbones will lower death-avoidance fractions as capability reduces catastrophic failure rates.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T14:51:55.411866+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T14:51:55.412040+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T14:51:55.412199+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T14:51:55.412326+00:00_

1	\section{Conclusion}
2	
3	We presented a formal diagnostic framework for decomposing routing signal in modular LLM agents via episode-level counterfactual analysis with dual metrics (penalty-independent label fraction and penalty-dependent DAF). Applied to 245 ScienceWorld episodes (11 of 30 task types, Qwen2.5-7B-Instruct), death asymmetry accounts for 78.9\% of non-tie routing labels; DAF $= 90.4\%$ at $P{=}100$ (95\% CI: $[81.6\%, 98.8\%]$). Cross-domain contrasts confirm framework predictions: MATH shows no routing signal without catastrophic failure; ALFWorld reveals information asymmetry as an alternative mechanism; a Llama pilot confirms cross-model consistency. Open directions include replication in catastrophic-failure environments (e.g., NetHack~\citep{nethack-2020}, Crafter~\citep{crafter-2022}) and stronger backbones, which the framework predicts will lower DAF.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T14:51:55.412447+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T14:51:55.412580+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T14:51:55.412723+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T14:51:55.412914+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T14:51:55.413082+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T14:51:55.413356+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T14:51:55.413541+00:00_

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
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T14:51:55.413704+00:00_

1	\section{Experiments}
2	
3	\subsection{Death Avoidance Decomposition}
4	\label{sec:death-decomp}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{fig1_daf_scatter.pdf}
9	\caption{Per-task death rate differential (internal minus deterministic) vs.\ $\Delta_{\text{full}}$. Each point represents one of 11 task types. Regression: $r = 0.9698$ ($p = 8.12 \times 10^{-7}$).}
10	\label{fig:decomposition}
11	\end{figure}
12	
13	The full performance gap between deterministic and internal strategies across 245 episodes is $\Delta_{\text{full}} = +29.60$ points. Excluding all episodes where either strategy results in death, the gap collapses to $\Delta_{\text{nd}} = +2.84$. The resulting DAF (\S\ref{sec:daf}) is 90.41\%: approximately 90\% of the deterministic strategy's advantage is attributable to death avoidance.
14	
15	This concentration is consistent across task types (Appendix~\ref{app:per-task}). The Pearson correlation between per-task death rate differential and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$; Figure~\ref{fig:decomposition}). The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic---a 2.6$\times$ ratio driving the bulk of the score difference.
16	
17	The label distribution reflects this asymmetry: 86 \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, 150 \texttt{no\_preference}. When internal reasoning does not cause death, it performs comparably to deterministic computation.
18	
19	One task reveals residual non-death signal: \texttt{find-non-living-thing} ($n=40$) has zero deaths yet $\Delta_{\text{full}} = +9.58$, entirely from non-death differences. Among the 10 death-prone task types, however, death avoidance overwhelms non-death signal.
20	
21	\subsection{Baselines}
22	\label{sec:baselines}
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\begin{tabular}{@{}lccc@{}}
28	\toprule
29	Strategy & Score & 95\% CI & Death \% \\
30	\midrule
31	Always-Internal & $-39.07$ & [$-46
…[truncated 2609 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T14:51:55.413849+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T14:51:55.414037+00:00_

1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 98\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Applying this methodology to 245 episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, we find that death avoidance accounts for 90.41\% of the routing signal (Death Avoidance Fraction). Per-task death rate differentials correlate near-perfectly with routing benefit ($r$ = 0.9698, $p$ = 8.12$\times$10$^{-7}$). The oracle router agrees with always-deterministic on 96.2\% of decisions, and a trained router achieves only 58.1\% balanced accuracy---near random. These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T14:51:55.414189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T14:51:55.414316+00:00_

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
21	\input{conclusion}
22	
23	\bibliography{references}
24	
25	\end{document}
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T14:51:55.414477+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/main.tex",
  "offset": "25",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/main.tex",
    "offset": "25",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T14:51:55.414611+00:00_

25	Our analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold.
26	
27	\paragraph{Cross-environment evidence.}
28	A preliminary 50-problem MATH Level~4--5 pilot, using code interpreter as the deterministic modality, provides initial evidence beyond ScienceWorld. Internal reasoning achieved 80\% accuracy versus 72\% for code interpreter, with 88\% of problems showing no modality preference (1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver. An exploratory ALFWorld study (135 games, 6 task types) shows a similar asymmetry: 25.9\% of episodes are deterministic-preferred versus 1.5\% internal-preferred, with deterministic success rate (27.4\%) far exceeding internal (3.0\%). While ALFWorld lacks ScienceWorld's explicit death penalty, task failure under internal reasoning is near-total, suggesting that catastrophic failure avoidance generalizes beyond environments with formal death mechanics.
29	
30	\paragraph{Scope.}
31	Extending the counterfactual methodology to environments with graded failure costs, embodied agents, or multi-turn dialogue systems would clarify how broadly death avoidance accounts for apparent routing signal. Step-level labeling with denser rewards and the logit--generation gap in the implicit router are natural next steps. We audit labeling quality in Appendix~\ref{app:labeling}.
32	
33	\section*{Ethics Statement}
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_check-tex-math-data_20260517T145024",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-17T14:51:55.414809+00:00_

审计完成。以下是所有 MATH 相关引用的逐条结果。

---

## `docs/paper/`（最新版本）— 全部正确

| 文件:行号 | 当前值 | 正确? |
|---|---|---|
| `docs/paper/abstract.tex:2` | N=795, p=0.81 | **Y** |
| `docs/paper/introduction.tex:24` | N=795, 73.5% vs 73.0%, p=0.81 | **Y** |
| `docs/paper/introduction.tex:35` | N=795, p=0.81 | **Y** |
| `docs/paper/experiments.tex:32` | N=795, +0.5pp, p=0.81 | **Y** |
| `docs/paper/experiments.tex:50` | MATH & 795 (表格行) | **Y** |
| `docs/paper/experiments.tex:54` | caption 提及 MATH balanced labels | **Y** |
| `docs/paper/experiments.tex:61` | N=795, labels balanced (95:107) | **Y** |
| `docs/paper/experiments.tex:65` | summary 段, 95:107 | **Y** |
| `docs/paper/discussion.tex:5` | p=0.81 | **Y** |
| `docs/paper/conclusion.tex:3` | "no routing signal" (无具体数值) | **Y** |
| `docs/paper/method.tex:39` | 仅提及 MATH 名称 | **Y** |
| `docs/paper/main.tex:35` | Limitations 段, 无旧数据 | **Y** |

---

## `artifacts/_project/paper/latex/`（旧版本）— 3 处引用旧数据

| 文件:行号 | 当前值 | 正确? |
|---|---|---|
| `latex/discussion.tex:5` | **N=300, 81.0% vs 76.7% (+4.3pp), p=0.079** | **N** |
| `latex/conclusion.tex:3` | **N=50 ("preliminary MATH pilot 50 problems")** | **N** |
| `latex/main.tex:28` | **N=50, 80% vs 72%, 88% no-pref** | **N** |

---

## `artifacts/_project/paper/`（根目录版本）— 1 处旧数据

| 文件:行号 | 当前值 | 正确? |
|---|---|---|
| `cross_env_summary_table.tex:11` | **MATH & 300** (N=300, 5.7%, 10.0%, 84.3%) | **N** |
| `conclusion.tex:5` | 仅提及 MATH 作为 future work | **Y** |
| `abstract.tex:2` | 无 MATH 引用 | **Y** |

---

## `artifacts/dream_reports/`（自动生成草稿）— 非正式论文，数据均为虚构

| 文件:行号 | 值 | 备注 |
|---|---|---|
| `best/paper.tex:248` | 71.4% vs 58.2%, N=500 | dream report |
| `median/paper.tex:254,269` | n=500 | dream report |
| `worst/paper.tex:243` | 提及 MATH 作 future work | dream report |

---

## 总结

**`docs/paper/`（最新主版本）：12 处 MATH 引用全部正确，均使用 N=795 / +0.5pp / p=0.81。**

**仍引用旧数据的位置（4 处）：**

1. **`artifacts/_project/paper/latex/discussion.tex:5`** — N=300, +4.3pp, p=0.079
2. **`artifacts/_project/paper/latex/conclusion.tex:3`** — N=50
3. **`artifacts/_project/paper/latex/main.tex:28`** — N=50, 80% vs 72%
4. **`artifacts/_project/paper/cross_env_summary_table.tex:11`** — N=300

这 4 处均在 `artifacts/_project/paper/` 路径下（历史版本），不在 `docs/paper/`（当前主版本）中。如果 `artifacts/_project/paper/` 仍会被引用或编译，需要更新；如果仅作归档，可忽略。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_check-tex-math-data_20260517T145024"
}
```

</details>

---
