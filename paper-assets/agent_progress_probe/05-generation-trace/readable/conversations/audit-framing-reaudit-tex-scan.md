# audit framing reaudit tex scan

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_audit_framing-reaudit-tex-scan_20260515T005515.jsonl`
- **Structured JSON:** [`dc877bea8249b4950a12.json`](../../sessions/dc/dc877bea8249b4950a12.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-15T00:59:03.501450+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T00:59:03.501800+00:00_

docs/paper/_acl_template/acl_lualatex.tex
docs/paper/_acl_template/acl_latex.tex
docs/paper/main.tex
docs/paper/sections/related_work.tex
docs/paper/sections/abstract.tex
docs/paper/sections/limitations.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/appendix.tex
docs/paper/sections/experiments.tex
docs/paper/sections/analysis.tex
docs/paper/sections/introduction.tex
docs/paper/sections/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T00:59:03.501981+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T00:59:03.502113+00:00_

docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T00:59:03.502230+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T00:59:03.502356+00:00_

1	% Abstract: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)
2	LLM-based agents deployed on software engineering tasks frequently exhibit semantic stagnation---executing diverse yet collectively unproductive action sequences that evade repetition detectors and overwhelm LLM-based judges. No systematic study has investigated what signals carry stagnation information or whether detection requires semantic understanding.
3	
4	We address this gap through a systematic empirical study using a weak supervision pipeline (3 labeling functions + majority vote) over 205K+ windows from two architecturally distinct SE agents, SWE-Agent and OpenHands. We compare 30 hand-crafted structural features, a GRU-based neural embedding probe, and an LLM-as-judge baseline.
5	
6	Our central finding is that stagnation signals are fundamentally structural: 30 features---command repetition rates, file operation counts, edit distances---achieve RF 0.9951 in-domain and GB 0.9674 cross-agent macro-F1, surpassing the neural probe (0.9055) and LLM-as-judge (0.6625) by wide margins. In-domain evaluation reflects circular agreement with LF-derived silver labels; cross-agent transfer and a pending gold set provide non-circular validation. Structural features are also extremely data-efficient, achieving $>$0.987 macro-F1 at just 10\% training data.
7	
8	Analysis of labeling function temporal dynamics reveals agent-specific roles: command repetition leads stagnation by 1.87 steps on SWE-Agent but reverses on OpenHands, where removing it improves fine-tuned F1 by 17.6 percentage points. Labeling functions validated on one agent can become adversarial on another.
9	
10	Despite these well-characterized temporal patterns, three temporal label models (time-varying weights, HMM, lag-aware HMM) fail to improve over majority vote---a negative result we attribute to insufficient inter-LF conflict in the 3-function regime.
11	
12	\goldset{Gold set validation (650 windows) pending.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T00:59:03.502486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T00:59:03.502650+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on multi-file codebases across dozens of editing rounds \citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.
5	As these deployments scale, a critical failure mode has emerged that is qualitatively different from crashes or syntax errors: the agent \emph{stagnates}---continuing to produce actions that appear purposeful while making no meaningful progress toward the task goal.
6	\citet{orlanski2026slopcodebench} document this degradation on SlopCodeBench, recording verbosity increases of 90\% and quality drops of 80\% in long-horizon coding trajectories, with no agent fully solving any benchmark problem end-to-end.
7	Crucially, the dominant failure pattern is not simple repetition but what we term \emph{semantic stagnation}: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.
8	This ``looks busy but going in circles'' pattern defeats existing monitoring tools, because surface-level action diversity masks the underlying lack of progress.
9	We observe this phenomenon at scale: across trajectories from two architecturally distinct agents---SWE-Agent \citep{yang2024sweagent} and OpenHands \citep{wang2025openhands}---on SWE-bench tasks \citep{jimenez2024swebench}, 28.5\% and 6.6\% of sliding windows exhibit stagnation under our silver labeling scheme, respectively, confirming that the failure mode is both prevalent and highly agent-dependent.
10	
11	Existing approaches address aspects of this problem but fall short in three ways.
12	First, \emph{repetition detectors} such as cycle detection \citep{george2025cycledetection} and SpecRA \citep{pipis2025reasoningloop} identify structural repetition---exact or near-exact loops in action sequences---but by design miss s
…[truncated 6421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T00:59:03.502864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T00:59:03.503055+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We frame stagnation detection as window-level binary classification over agent trajectories.
5	Silver labels are generated via weak supervision from three labeling functions, then used to train and evaluate three detection approaches: structural features, a neural embedding probe, and an LLM-as-judge baseline.
6	Figure~\ref{fig:pipeline} provides a system overview.
7	
8	\begin{figure*}[t]
9	\centering
10	\includegraphics[width=\textwidth]{../../figures/paper/fig_pipeline.pdf}
11	\caption{System overview. (Left) Agent trajectories are segmented into overlapping windows of $k{=}5$ steps. (Center) Three labeling functions vote on each window; majority vote produces silver labels with confidence 1--3. (Right) Three detection approaches compared: structural features (30-dim), NL embedding probe (GRU), and LLM-as-judge (eval only, not trained on silver labels).}
12	\label{fig:pipeline}
13	\end{figure*}
14	
15	%-------------------------------------------------------------------
16	\subsection{Problem Formulation}
17	\label{sec:problem}
18	
19	Given an agent trajectory $T = (a_1, a_2, \ldots, a_n)$ where each $a_t$ is an action (e.g., a shell command, file edit, or API call), we partition it into overlapping sliding windows $w_i = (a_i, \ldots, a_{i+k-1})$ with window size $k{=}5$ and stride 1.
20	The task is to assign each window a binary label $y_i \in \{0, 1\}$, where 0 denotes \emph{stagnation} (the agent is stuck or unproductive) and 1 denotes \emph{progress} (the agent is making meaningful headway toward the task goal).
21	
22	The window formulation offers two advantages over alternatives.
23	Compared to step-level scoring, windows capture short-range temporal patterns---such as a sequence of repeated failed attempts---that individual actions cannot express.
24	Compared to trajectory-level labeling, windows provide the granularity needed to pinpoint \emph{when} stagnation begins and ends within a single task attempt, enabli
…[truncated 9907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T00:59:03.503229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T00:59:03.503463+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.
5	All reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\S\ref{sec:method}).
6	
7	\paragraph{Circular evaluation caveat.}
8	Structural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.
9	Consequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.
10	The cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\S\ref{sec:cmd_rep_ablation}).
11	A human-annotated gold set provides the definitive non-circular evaluation (\S\ref{sec:gold_set}).
12	
13	%-------------------------------------------------------------------
14	\subsection{Experimental Setup}
15	\label{sec:setup}
16	
17	\paragraph{Datasets.}
18	We extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.
19	\textbf{SWE-Agent} trajectories from SWE-bench \citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\%.
20	\textbf{OpenHands} (OH) trajectories \citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 6.6\%.
21	Silver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).
22	Unless stated otherwise, evaluation uses the conf${\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\begin{tabu
…[truncated 14482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T00:59:03.503611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T00:59:03.503782+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Circular Evaluation and Its Implications}
5	\label{sec:circular}
6	
7	The structural RF's 0.9951 macro-F1 (\S\ref{sec:main_results}) is a predictable consequence of feature--label overlap, not a detection achievement.
8	The 30 structural features include repetition ratios and file operation counts---the same signals $\lambda_1$ and $\lambda_2$ consume to produce silver labels.
9	This score therefore represents an upper bound on LF reverse-engineering fidelity.
10	
11	Two evaluation settings break this circularity.
12	First, cross-agent transfer: GB trained on SWE-Agent LF distributions achieves 0.9674 macro-F1 on OpenHands, where LF firing patterns differ substantially (e.g., cmd\_rep votes stagnation on 92.2\% vs.\ 65.5\% of windows).
13	The model cannot memorize LF outputs when tested on a different agent's distribution.
14	Second, a human-annotated gold set (\S\ref{sec:gold_set}) will provide definitive non-circular ground truth.
15	Until then, all in-domain structural metrics should be interpreted as LF-agreement scores rather than detection accuracy.
16	
17	\subsection{Why Temporal Label Models Fail}
18	\label{sec:why_tlm_fail}
19	
20	Despite clear temporal structure in LF activations (\S\ref{sec:lf_temporal}), no temporal label model improves downstream detection over majority vote (\S\ref{sec:temporal_label_models}).
21	The root cause is low label conflict in the 3-LF regime: conf${\geq}$2 windows dominate the training set, leaving few ambiguous labels for temporal models to correct.
22	
23	TWV targets only conf${=}1$ windows, flipping 14.1\% of their labels.
24	These flips introduce noise rather than corrections---downstream probe F1 drops by 2.57\,pp relative to MV-trained.
25	HMM overpredicts stagnation (29,176 vs.\ 25,633 progress windows), producing a distorted label distribution that degrades the probe to 0.6564.
26	Lag-HMM, despite explicitly modeling per-LF temporal offsets, tracks MV within
…[truncated 2936 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T00:59:03.503928+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T00:59:03.504079+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Process Reward Models.}
5	Process reward models (PRMs) assign step-level quality scores to guide agent behavior during inference or training.
6	\citet{xi2025agentprm} introduce AgentPRM, training TD/GAE-based step-level rewards that evaluate both long-term promise and immediate progress in agent trajectories, requiring outcome labels and an RL pipeline.
7	\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels.
8	Evaluation benchmarks have emerged in parallel: \citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs outperform general-purpose ones, while \citet{wang2026planrewardbench} reveal that all reward model categories---generative, discriminative, and LLM-as-judge---degrade on long-horizon trajectories.
9	\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques, and \citet{qiu2026dataprm} introduce environment-aware probing for data analysis agents to detect silent errors.
10	Our work differs in operating at window level rather than step level, requiring no outcome labels or reward annotations at inference time---labeling functions use only observable structural signals---and targeting real-time monitoring ($<$5\,ms per window) rather than training signal generation.
11	
12	\paragraph{Agent Self-Reflection and Verification.}
13	Self-reflection methods prompt agents to diagnose and correct their own failures.
14	\citet{shinn2023reflexion} introduce verbal self-reflection loops, \citet{yao2023tot} propose tree-structured deliberation, and \citet{zhou2024lats} combine Monte Carlo tree search with LLM self-evaluation for language agents.
15	However, \citet{huang2024selfcorrect} demonstrate that LLMs cannot reliably self-correct reasoning without external feedback, and \citet{kamoi2024selfcorrection} confirm that self-corre
…[truncated 4765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T00:59:03.504218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T00:59:03.504343+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented a systematic study of progress stagnation detection in LLM coding agents, comparing structural features, neural embedding probes, and LLM-as-judge approaches.
5	Three findings emerge.
6	
7	First, stagnation signals are fundamentally structural.
8	Thirty lightweight features achieve 0.9951 in-domain and 0.9674 cross-agent macro-F1, surpassing neural probes (0.9055) and LLM judges (0.6625) by wide margins.
9	These features are also data-efficient, maintaining F1 above 0.987 with only 10\% of training data.
10	
11	Second, labeling functions exhibit agent-specific temporal dynamics.
12	Command repetition leads stagnation onset by 1.87 steps on SWE-Agent but reverses on OpenHands, where its high false-positive rate corrupts silver labels---removing it improves fine-tuned probe F1 by 17.6\,pp.
13	
14	Third, temporal label models fail to improve over majority vote.
15	Three temporal aggregation methods---TWV, HMM, and lag-aware HMM---all underperform majority vote, constrained by insufficient inter-LF conflict among three binary labeling functions.
16	
17	Agent monitoring should therefore prioritize lightweight structural features ({<}5\,ms per window, no GPU) over embedding or LLM approaches.
18	The circular evaluation caveat applies to in-domain results; cross-agent transfer provides stronger validation.
19	
20	Future work includes extending evaluation to non-software-engineering agent domains, online integration with early termination or strategy switching, scaling to {>}10 labeling functions to test whether temporal aggregation becomes useful, and validation against the pending 650-window gold set.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T00:59:03.504468+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T00:59:03.504624+00:00_

1	\section{Supplementary Results}
2	\label{sec:appendix}
3	
4	%-------------------------------------------------------------------
5	\subsection{Encoder Ablation}
6	\label{sec:app_encoder}
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	\textbf{Encoder} & \textbf{Dim} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} & \textbf{Best Ep.} \\
14	\midrule
15	Qwen3-0.6B & 1024 & 0.9055 & --- & --- & --- \\
16	E5-large-v2 & 1024 & 0.9363 & 0.9067 & 0.9660 & 4 \\
17	BGE-M3 & 1024 & \textbf{0.9413} & \textbf{0.9147} & \textbf{0.9679} & 5 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Encoder ablation on SWE-Agent conf${\geq}$2 ($N{=}1{,}824$). All models use the same GRU architecture (2-layer, hidden$=$256, dropout$=$0.1, lr$=$1e-3, batch$=$32, early stopping patience~5). All encoders exceed 0.90 macro-F1, confirming the probe's temporal architecture drives performance rather than a specific encoder. BGE-M3 achieves the highest score ($+$3.6\,pp over Qwen3), but the gap between encoders (0.5\,pp) is small relative to the structural--probe gap (8.96\,pp).}
21	\label{tab:encoder_ablation}
22	\end{table}
23	
24	%-------------------------------------------------------------------
25	\subsection{Window Size Ablation}
26	\label{sec:app_window}
27	
28	\begin{table}[h]
29	\centering
30	\small
31	\begin{tabular}{ccccc}
32	\toprule
33	\textbf{Window $k$} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} & \textbf{$\Delta$ vs.\ $k{=}5$} \\
34	\midrule
35	3 & 0.8721 & 0.7784 & 0.9659 & $-$5.9\,pp \\
36	\textbf{5} & \textbf{0.9309} & \textbf{0.8917} & \textbf{0.9701} & --- \\
37	7 & 0.9133 & 0.8791 & 0.9475 & $-$1.8\,pp \\
38	\bottomrule
39	\end{tabular}
40	\caption{Window size ablation on SWE-Agent conf${\geq}$2 using the Qwen3-0.6B encoder (seed~42). $k{=}5$ is optimal. $k{=}3$ lacks sufficient context for stagnation detection (F1\textsubscript{stag} drops 11.3\,pp). $k{=
…[truncated 3924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T00:59:03.504792+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T00:59:03.504918+00:00_

1	\label{sec:limitations}
2	
3	\paragraph{Scope.}
4	We evaluate two software engineering agents (SWE-Agent and OpenHands) on SWE-bench.
5	Generalization to non-SE domains---web navigation, data analysis, multi-agent collaboration---remains untested.
6	
7	\paragraph{Silver labels.}
8	All evaluation is against labeling-function-derived silver labels; the structural RF's 0.9951 macro-F1 reflects LF-reconstructibility rather than ground-truth detection accuracy.
9	A 650-window gold set with a validated annotation pipeline is prepared but human annotation is pending.
10	\goldset{Gold set validation pending.}
11	
12	\paragraph{Labeling function count.}
13	Three LFs produce insufficient inter-LF conflict (95.1\% agreement at conf${\geq}$2) for temporal label models to demonstrate value; scaling to {>}10 LFs with higher disagreement is needed.
14	
15	\paragraph{No online evaluation.}
16	All results are offline; no intervention or real-time deployment evaluation has been conducted.
17	
18	\paragraph{Outcome dependence.}
19	The outcome backpropagation labeling function ($\lambda_3$) requires task outcome, which is unavailable during inference.
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T00:59:03.505039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T00:59:03.505207+00:00_

1	# Paper Framing — agent_progress_probe
2	
3	## Target Venue
4	- Primary: EMNLP 2026 ARR (submission deadline: May 25, 2026; commitment: August 2, 2026)
5	- Format: Long paper (8 pages + appendix)
6	- Track: LLM Agents
7	- Paper type: **Empirical analysis paper**（D039 pivot: 从 method paper 转 empirical study）
8	- Fallback: ACL 2026 ARR August cycle (~August 15 deadline)
9	
10	## Core Claims (3 条) — D039 Pivot
11	
12	1. **Structural Features Dominate Zero-Shot Cross-Agent Transfer (primary contribution)**: 系统性对比发现结构特征在跨 agent 零样本迁移上具有压倒性优势——30 个结构特征在 in-domain (RF 0.9951) 和 cross-agent zero-shot (GB 0.967) 近完美预测停滞，零样本迁移上大幅领先 probe（zero-shot 0.598 vs 0.967, +36.9pp）和 LLM-as-judge（+24.3pp）。然而 probe 在少量目标域数据微调后迅速缩小差距：10% FT 0.918（-5pp），20% FT 0.948（-2pp），50% FT 0.968（追平）。Encoder-agnostic（3 个 encoder 均 >0.90）；最优窗口 k=5 (0.9309)。这揭示：(a) 结构特征天然跨 agent 迁移——不需要任何目标域数据即可部署；(b) probe 的语义信号在 domain adaptation 后能匹配结构特征——stagnation 信息在 embedding 中存在但需要适配提取；(c) 实际部署中，目标 agent 数据不可用时结构特征是明确首选；有少量标注数据时两种方法收敛。**改变社区对 agent monitoring 方法选型的认知：结构特征是零数据部署的默认选择，不需要昂贵的表示学习和域适配。** Gold set 验证 structural features 是否检测到真实 stagnation（非仅 circular eval artifact）是论文成立的关键。
13	
14	2. **LF Temporal Dynamics and Label Quality as Transfer Bottleneck (analytical contribution)**: 两层发现。**时序动态**：LFs 在 trajectory 上展现系统性但 agent-specific 的时序角色。SWE-Agent 上 cmd_rep leading (-1.87步)、file_diff concurrent (-1.2步)、OB lagging (+6.7步)；OH 上 cmd_rep 角色从 leading 变 lagging (+3.32步)，而 file_diff（leading, -4.9步）和 OB（lagging, +18.1步）跨域一致。不同 agent 架构产生不同的 LF 行为模式，但部分 LF（file_diff, OB）展现跨域稳定性。**标签质量瓶颈 + cmd_rep coverage 贡献**：通过标签审计发现，label quality 是 cross-agent transfer 的主导因素。修复 OH 标签版本偏差（stag_rate 6.56%→21.45%）后：(a) probe 5% FT 从 0.570 跃升到 0.850（+28pp），新 5% 超过旧 50%（0.688）；(b) cmd_rep 实际是高精度低召回检测器（precision 97.91%, FP 0.15%），旧 "71% FP 噪声源" 完全是标签 bug 产物。**Prevalence-matched ablation**（同一测试集 N=6122, stag=19.3%）揭示 cmd_rep 真实贡献是 **-29.4pp**（p≈0, McNemar chi²=1551）：移除 cmd_rep 不改变高置信标签质量（2-LF 与 3-LF 在交集上 100% 一致），但将可用训练数据从 43K 缩减到 
…[truncated 9338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T00:59:03.505358+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/writing_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T00:59:03.505602+00:00_

1	meta:
2	  venue: EMNLP 2026 ARR
3	  track: LLM Agents
4	  paper_type: "empirical analysis / Findings"
5	  template: null  # TODO: download latest *ACL / ARR template (acl2023.sty or newer)
6	  template_note: "EMNLP 2026 ARR uses standard *ACL format. Worker Step 2 前需先搜索下载最新模板。"
7	  page_limit: 8
8	  appendix: unlimited
9	  deadline: 2026-05-25
10	  core_claim: >
11	    Stagnation signals in LLM agents are fundamentally structural: 30 simple features
12	    achieve 0.995 in-domain and 0.967 cross-agent F1, decisively surpassing neural
13	    embedding probes (0.906/0.751) and LLM-as-judge (+24.3pp), while three temporal
14	    label model implementations all fail to improve over majority vote.
15	  created_at: 2026-05-14T19:30:00Z
16	  gold_set_status: pending  # 650 windows, 人工标注预计 5/17 完成, Patch 补入
17	
18	paper_outline:
19	  - section: abstract
20	    word_budget: 250
21	    core_bullets:
22	      - "Problem: LLM agents exhibit semantic stagnation—executing diverse but collectively unproductive action sequences that evade repetition detectors and overwhelm LLM-based judges"
23	      - "Approach: systematic empirical study via weak supervision pipeline (3 LFs + MV) on 2 SE agents (SWE-Agent 54K windows, OpenHands 150K windows), comparing structural features, NL embedding probe, and LLM-as-judge"
24	      - "Finding 1 (primary): stagnation signals are structural—30 features achieve RF 0.995 in-domain, GB 0.967 cross-agent, +24.3pp over LLM-judge, encoder-agnostic (3 encoders all >0.90)"
25	      - "Finding 2: LFs exhibit systematic but agent-specific temporal dynamics—cmd_rep leads by -1.87 steps on SWE-Agent but reverses on OpenHands; removing it improves OH F1 by +17.6pp"
26	      - "Finding 3: three TLM implementations (TWV/HMM/lag-HMM) all fail vs MV; TWV degrades downstream up to -21.7pp in low-conflict 3-LF regime"
27	      - "[GOLD_SET_PLACEHOLDER: gold set validation results pending 5/17]"
28	    dependencies: [experiments, method]
29	    tables: []
30	    
…[truncated 19688 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T00:59:03.505859+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T00:59:03.506011+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	\usepackage{enumitem}
19	
20	\newcommand{\todo}[1]{\textcolor{red}{[TODO: #1]}}
21	\newcommand{\goldset}[1]{\textcolor{blue}{[GOLD\_SET: #1]}}
22	
23	\title{Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{sections/abstract}
31	\input{sections/introduction}
32	\input{sections/related_work}
33	\input{sections/method}
34	\input{sections/experiments}
35	\input{sections/analysis}
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\input{sections/limitations}
40	
41	\bibliography{references}
42	\bibliographystyle{acl_natbib}
43	
44	\appendix
45	\input{sections/appendix}
46	
47	\end{document}
48	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T00:59:03.506139+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/framing-reaudit/ 2>/dev/null || echo \"DIR_NOT_EXIST\"",
  "description": "Check if framing-reaudit directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/framing-reaudit/ 2>/dev/null || echo \"DIR_NOT_EXIST\"",
    "description": "Check if framing-reaudit directory exists"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T00:59:03.506252+00:00_

DIR_NOT_EXIST

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T00:59:03.506360+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/framing-reaudit",
  "description": "Create framing-reaudit directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/framing-reaudit",
    "description": "Create framing-reaudit directory"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T00:59:03.506468+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T00:59:03.506614+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/framing-reaudit/inconsistency_list.md",
  "content": "# Full Re-Audit: Inconsistency List (D050+D051 Framing Update)\n\nGenerated: 2026-05-15\n\n---\n\n## [Abstract] (sections/abstract.tex)\n\n- **Line 6**: \"stagnation signals are fundamentally structural\" → 应改为 \"zero-shot transfer dominance\" framing [D039 pivot 已将 \"fundamentally structural\" 修正为 \"zero-shot transfer dominance\"，但 .tex 未更新]\n- **Line 8**: \"removing it improves fine-tuned F1 by 17.6 percentage points\" → **INVALID — 删除此 claim** [D051: 标签 bug 产物。新数据下去掉 cmd_rep 是 -6.5pp（反转）。替换叙事为 label quality as transfer bottleneck + prevalence-matched ablation -29.4pp]\n- **Line 8**: \"OpenHands, where removing it improves fine-tuned F1 by 17.6 percentage points\" → 整段关于 cmd_rep removal improving 的叙事需重写 [新叙事方向：label quality audit reveals cmd_rep's core value is coverage (-29.4pp when removed), precision 97.91%]\n\n---\n\n## [Introduction] (sections/introduction.tex)\n\n- **Line 9**: \"6.6\\% of sliding windows exhibit stagnation\" → 应改为 \"21.45\\%\" [OH stag rate 修正：旧 embeddings.pt 错误]\n- **Line 20**: \"OpenHands (150,652 windows, 6.6\\% stagnation)\" → 应改为 \"21.45\\% stagnation\" (或 20.87% excl abstain) [同上]\n- **Line 28**: \"Finding 1: Stagnation signals are fundamentally structural.\" → narrative 应修改为强调 \"zero-shot transfer dominance\" [framing pivot]\n- **Line 29**: \"0.751 after full fine-tuning on the target agent\" → 应改为 \"0.9763\" [旧标签 probe FT 结果]\n- **Line 29**: \"surpassing the GRU embedding probe...0.9055 in-domain, 0.751 after full fine-tuning\" → cross-agent gap 叙事需完全重写 [新值：probe FT = 0.9763，gap 仅 2.21pp 而非原来的巨大差距]\n- **Line 37**: \"92.2\\% stagnation-vote rate produces a 71\\% false positive rate on progress windows\" → 应改为 \"5.39\\% fire rate\" + \"2.3\\% FP rate / precision 97.91\\%\" [旧 embeddings 错误统计]\n- **Line 38**: \"Removing $\\lambda_1$ from the OpenHands labeling pipeline improves fine-tuned probe F1 by 17.6\\,pp\" → **INVALID — 删除此 claim** [同 abstract]\n- **Line 38**: \"demonstrating that labeling functions validated on one agent architecture can become adversarial on another\" → 叙事需修改 [cmd_rep 不再是 \"adversarial\"，而是高精度低召回检测器；旧结论完全是标签 bug 产物]\n\n---\n\n## [Method] (sections/method.tex)\n\n- **Line 44**: \"92.2\\% of OpenHands windows\" → 应改为 \"5.39\\%\" [cmd_rep OH fire rate 旧定义（stag vote %）vs 新定义（actual fire rate）]\n- **Line 65** (Table 1): OH Stag\\% for $\\lambda_1$ (cmd_rep) = \"92.2\" → 应改为 \"5.39\" (或 5.4) [同上]\n- **Line 44**: \"the elevated OH rate reflects differences in action distributions across agent architectures\" → 叙事需修改 [新数据下 cmd_rep 在 OH 不再异常高频]\n\n---\n\n## [Experiments] (sections/experiments.tex)\n\n- **Line 20**: \"stagnation ratio of 6.6\\%\" → 应改为 \"21.45\\%\" [OH stag rate 修正]\n- **Line 32** (Table): OH Stag\\% = \"6.6\" → 应改为 \"21.45\" (或 21.4) [同上]\n- **Line 67** (Table 2): ProgressProbe OH columns \"0.530\" and \"0.528\" → 应改为 \"0.5984\" [probe ZS 新标签结果]\n- **Line 68** (Table 2): \"+ full OH fine-tune\" = \"0.7510\" → 应改为 \"0.9763\" [probe FT 新标签结果]\n- **Line 88**: \"21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751)\" → 应改为 \"2.21\\,pp above the probe fine-tuned on 100\\% of OH data (0.9763)\" [cross-agent gap 计算错误——基于旧 probe FT]\n- **Line 88**: \"Structural GB transfers best, achieving 0.967 macro-F1\" → 如果 structural GB 也重跑了（0.9984），此处需更新 [待确认新 structural GB 值]\n- **Line 90**: \"Both structural models recover to $>$0.99 on conf${\\geq}$2 OH windows\" → 可能需更新 [取决于新实验结果]\n- **Line 92**: \"probe's zero-shot transfer (0.530 on all windows, 0.528 on conf${\\geq}$2) is near chance\" → 应改为 \"0.5984 on conf${\\geq}$2\" [新标签 ZS 结果]\n- **Line 92**: \"even full OH fine-tuning only reaches 0.751\" → 应改为 \"0.9763\" [新标签 FT 结果]\n- **Line 93**: \"This asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding\" → 叙事需修改 [新数据下 probe FT 0.9763 vs structural 0.9984，差距仅 2.21pp；asymmetry 在 zero-shot 仍存在但 FT 后消失]\n- **Line 170**: \"cmd\\_rep LF votes stagnation on 92.2\\% of OH windows (vs.\\ 65.5\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows\" → 应改为 \"5.39\\% of OH windows\" + \"2.3\\% FP rate / precision 97.91\\%\" [旧 embeddings 错误]\n- **Lines 171-195** (§5.5 Command Repetition Ablation): 整个 subsection 基于旧标签数据，需完全重写 [Table 3 数据全部无效：ZS 0.530→0.5984, FT 0.751→0.9763, +17.6pp→INVALID。新叙事：label quality as transfer bottleneck + prevalence-matched ablation -29.4pp + cmd_rep 是高精度低召回 coverage provider]\n\n---\n\n## [Analysis] (sections/analysis.tex)\n\n- **Line 12**: \"cmd\\_rep votes stagnation on 92.2\\% vs.\\ 65.5\\% of windows\" → OH 值应改为 \"5.39\\%\" [同上]\n\n---\n\n## [Conclusion] (sections/conclusion.tex)\n\n- **Line 7**: \"stagnation signals are fundamentally structural\" → 应改为 zero-shot transfer dominance framing [同 abstract]\n- **Line 12**: \"Command repetition leads stagnation onset by 1.87 steps on SWE-Agent but reverses on OpenHands, where its high false-positive rate corrupts silver labels---removing it improves fine-tuned probe F1 by 17.6\\,pp\" → **INVALID — 删除 \"high false-positive rate corrupts\" + \"removing improves 17.6pp\" claim** [新叙事方向：temporal dynamics reveal agent-specific LF roles; label quality audit shows transfer bottleneck is label version bias, not LF noise]\n\n---\n\n## [Appendix] (sections/appendix.tex)\n\n- **Line 67-68** (Table caption): references to cmd_rep having opposite effects → 叙事需更新以反映新标签结果\n- **Line 80** (Table subtable a): \"3-LF (w/ cmd\\_rep)\" ZS \"0.530\" → 应改为 \"0.5984\" [新标签]\n- **Line 80**: FT \"0.751\" → 应改为 \"0.9763\" [新标签]\n- **Line 81**: \"2-LF (no cmd\\_rep)\" FT \"0.927\" → 需新实验值 [旧标签结果无效]\n- **Line 83**: \"$\\Delta$\" \"+17.6\\,pp\" → **INVALID** [同上]\n- **Line 104** (Table caption): \"Removing \\texttt{cmd\\_rep} helps probe fine-tuning ($+$17.6\\,pp)\" → **INVALID**\n- **Line 108**: \"Removing \\texttt{cmd\\_rep} improves probe fine-tuned F1 by $+$17.6\\,pp\" → **INVALID**\n- **Lines 109-111**: \"divergence reveals that \\texttt{cmd\\_rep} noise requires learned adaptation: fine-tuning can filter it\" → 叙事完全基于旧标签，需重写 [cmd_rep 不是 noise source]\n\n---\n\n## [Limitations] (sections/limitations.tex)\n\n- 无旧数字问题。叙事一致。\n\n---\n\n## [Related Work] (sections/related_work.tex)\n\n- 无旧数字问题。叙事一致。\n\n---\n\n## [paper_framing.md]\n\npaper_framing.md 中旧数字多出现在变更说明语境中（描述\"从旧值到新值的修正\"），属于历史记录不需修改。但以下几处仍以旧值作为当前 claim：\n\n- **Core Claims 区域 Claim 2 段**: \"去掉 cmd_rep 从 +17.6pp 变为 -6.5pp\" — 这是变更记录，OK\n- **Headline result template** 段: 已更新，无残留旧值。OK\n- **writing_plan.yaml core_claim (line 11-15)**: \"fundamentally structural\" + \"embedding probes (0.906/0.751)\" → \"0.751\" 需改为 \"0.9763\"；\"fundamentally structural\" 需改为 \"zero-shot transfer dominance\" framing\n\n---\n\n## [writing_plan.yaml]\n\n- **Line 11-15** (meta.core_claim): \"fundamentally structural\" → 应改为 zero-shot transfer dominance\n- **Line 11-15** (meta.core_claim): \"0.751\" → 应改为 \"0.9763\"\n- **Line 26** (abstract bullet): \"removing it improves OH F1 by +17.6pp\" → **INVALID — 删除/替换**\n- **Line 36** (introduction hook): \"90% verbosity increase and 80% quality erosion\" → 应改为 \"77% / 75.5%\" [SlopCodeBench 原文数字修正，已在 paper_framing.md 记录但未应用]\n- **Line 37** (introduction bullet): \"removing it improves OH F1 by +17.6pp\" → **INVALID**\n- **Line 96** (experiments setup): \"20.9% stag\" → 应改为 \"21.45%\" [轻微偏差]\n- **Line 98** (experiments bullet): \"Probe 0.528 zero-shot (0.751 with 50% finetune)\" → 应改为 \"0.5984 zero-shot; 0.968 with 50% finetune\" [旧标签值]\n- **Line 101** (experiments bullet): \"92.3% firing rate + 71% FP on OH progress windows\" → 应改为 \"5.39% fire rate + 2.3% FP\" [旧 embeddings 错误]\n- **Line 215** (tab_oh_cmdrep caption): \"cmd_rep has 92.3% firing rate and 71% false positive rate on OH progress windows\" → 同上\n\n---\n\n## [Introduction] (sections/introduction.tex) — SlopCodeBench 数字\n\n- **Line 6**: \"recording verbosity increases of 90\\% and quality drops of 80\\%\" → 应改为 \"77\\%\" 和 \"75.5\\%\" [paper_framing.md 2026-05-15 修正记录：与原文 arXiv:2603.24755 一致]\n\n---\n\n## 叙事一致性问题汇总\n\n### INVALID 叙事（必须删除/重写）\n\n| 位置 | 旧叙事 | 问题 |\n|------|--------|------|\n| abstract L8 | \"removing it improves fine-tuned F1 by 17.6pp\" | 标签 bug 产物，新数据反转 |\n| intro L37-38 | \"71% FP + removing improves 17.6pp\" | 同上 |\n| experiments §5.5 全段 | cmd_rep 是 OH 噪声源 | 同上 |\n| conclusion L12 | \"removing it improves...17.6pp\" | 同上 |\n| appendix L104-111 | cmd_rep noise + removal helps | 同上 |\n\n### \"fundamentally structural\" → \"zero-shot transfer dominance\"\n\n| 位置 | 说明 |\n|------|------|\n| abstract L6 | Finding 1 标题 |\n| intro L28 | Finding 1 标题 |\n| conclusion L7 | Summary 段 |\n| writing_plan.yaml core_claim | meta 段 |\n\n### Cross-agent gap 重算\n\n旧叙事：structural GB 0.967 >> probe FT 0.751 (gap 21.6pp)\n新现实：structural GB ~0.9984 vs probe FT 0.9763 (gap 2.21pp)\n\n影响位置：\n- experiments.tex L88 (\"21.6pp above\")\n- experiments.tex L92-93 (\"even full OH fine-tuning only reaches 0.751\")\n- introduction.tex L29 (\"0.751 after full fine-tuning\")\n- The entire \"structural features transfer while embeddings do not\" narrative needs nuancing\n\n### OH stag rate 6.6% → 21.45%\n\n影响位置：\n- introduction.tex L9, L20\n- experiments.tex L20, Table L32\n- (method.tex 无直接提及 overall stag rate)\n\n---\n\n## 优先级排序\n\n1. **P0 — INVALID claims (必须删除)**: +17.6pp cmd_rep removal, 71% FP, \"cmd_rep corrupts labels\" 叙事\n2. **P0 — 核心数字错误**: OH stag rate 6.6%→21.45%, probe FT 0.751→0.9763, cmd_rep fire rate 92.2%→5.39%, cross-agent gap 21.6pp→2.21pp\n3. **P1 — Framing 更新**: \"fundamentally structural\" → \"zero-shot transfer dominance\"\n4. **P1 — probe ZS 值**: 0.528/0.530 → 0.5984\n5. **P2 — 支持文件**: writing_plan.yaml, paper_framing.md 残留旧值\n6. **P2 — SlopCodeBench 数字**: 90%/80% → 77%/75.5%\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/framing-reaudit/inconsistency_list.md",
    "content": "# Full Re-Audit: Inconsistency List (D050+D051 Framing Update)\n\nGenerated: 2026-05-15\n\n---\n\n## [Abstract] (sections/abstract.tex)\n\n- **Line 6**: \"stagnation signals are fundamentally structural\" → 应改为 \"zero-shot transfer dominance\" framing [D039 pivot 已将 \"fundamentally structural\" 修正为 \"zero-shot transfer dominance\"，但 .tex 未更新]\n- **Line 8**: \"removing it improves fine-tuned F1 by 17.6 percentage points\" → **INVALID — 删除此 claim** [D051: 标签 bug 产物。新数据下去掉 cmd_rep 是 -6.5pp（反转）。替换叙事为 label quality as transfer bottleneck + prevalence-matched ablation -29.4pp]\n- **Line 8**: \"OpenHands, where removing it improves fine-tuned F1 by 17.6 percentage points\" → 整段关于 cmd_rep removal improving 的叙事需重写 [新叙事方向：label quality audit reveals cmd_rep's core value is coverage (-29.4pp when removed), precision 97.91%]\n\n---\n\n## [Introduction] (sections/introduction.tex)\n\n- **Line 9**: \"6.6\\% of sliding windows exhibit stagnation\" → 应改为 \"21.45\\%\" [OH stag rate 修正：旧 embeddings.pt 错误]\n- **Line 20**: \"OpenHands (150,652 windows, 6.6\\% stagnation)\" → 应改为 \"21.45\\% stagnation\" (或 20.87% excl abstain) [同上]\n- **Line 28**: \"Finding 1: Stagnation signals are fundamentally structural.\" → narrative 应修改为强调 \"zero-shot transfer dominance\" [framing pivot]\n- **Line 29**: \"0.751 after full fine-tuning on the target agent\" → 应改为 \"0.9763\" [旧标签 probe FT 结果]\n- **Line 29**: \"surpassing the GRU embedding probe...0.9055 in-domain, 0.751 after full fine-tuning\" → cross-agent gap 叙事需完全重写 [新值：probe FT = 0.9763，gap 仅 2.21pp 而非原来的巨大差距]\n- **Line 37**: \"92.2\\% stagnation-vote rate produces a 71\\% false positive rate on progress windows\" → 应改为 \"5.39\\% fire rate\" + \"2.3\\% FP rate / precision 97.91\\%\" [旧 embeddings 错误统计]\n- **Line 38**: \"Removing $\\lambda_1$ from the OpenHands labeling pipeline improves fine-tuned probe F1 by 17.6\\,pp\" → **INVALID — 删除此 claim** [同 abstract]\n- **Line 38**: \"demonstrating that labeling functions validated on one agent architecture can become adversarial on another\" → 叙事需修改 [cmd_rep 不再是 \"adversarial\"，而是高精度低召回检测器；旧结论完全是标签 bug 产物]\n\n---\n\n## [Method] (sections/method.tex)\n\n- **Line 44**: \"92.2\\% of OpenHands windows\" → 应改为 \"5.39\\%\" [cmd_rep OH fire rate 旧定义（stag vote %）vs 新定义（actual fire rate）]\n- **Line 65** (Table 1): OH Stag\\% for $\\lambda_1$ (cmd_rep) = \"92.2\" → 应改为 \"5.39\" (或 5.4) [同上]\n- **Line 44**: \"the elevated OH rate reflects differences in action distributions across agent architectures\" → 叙事需修改 [新数据下 cmd_rep 在 OH 不再异常高频]\n\n---\n\n## [Experiments] (sections/experiments.tex)\n\n- **Line 20**: \"stagnation ratio of 6.6\\%\" → 应改为 \"21.45\\%\" [OH stag rate 修正]\n- **Line 32** (Table): OH Stag\\% = \"6.6\" → 应改为 \"21.45\" (或 21.4) [同上]\n- **Line 67** (Table 2): ProgressProbe OH columns \"0.530\" and \"0.528\" → 应改为 \"0.5984\" [probe ZS 新标签结果]\n- **Line 68** (Table 2): \"+ full OH fine-tune\" = \"0.7510\" → 应改为 \"0.9763\" [probe FT 新标签结果]\n- **Line 88**: \"21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751)\" → 应改为 \"2.21\\,pp above the probe fine-tuned on 100\\% of OH data (0.9763)\" [cross-agent gap 计算错误——基于旧 probe FT]\n- **Line 88**: \"Structural GB transfers best, achieving 0.967 macro-F1\" → 如果 structural GB 也重跑了（0.9984），此处需更新 [待确认新 structural GB 值]\n- **Line 90**: \"Both structural models recover to $>$0.99 on conf${\\geq}$2 OH windows\" → 可能需更新 [取决于新实验结果]\n- **Line 92**: \"probe's zero-shot transfer (0.530 on all windows, 0.528 on conf${\\geq}$2) is near chance\" → 应改为 \"0.5984 on conf${\\geq}$2\" [新标签 ZS 结果]\n- **Line 92**: \"even full OH fine-tuning only reaches 0.751\" → 应改为 \"0.9763\" [新标签 FT 结果]\n- **Line 93**: \"This asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding\" → 叙事需修改 [新数据下 probe FT 0.9763 vs structural 0.9984，差距仅 2.21pp；asymmetry 在 zero-shot 仍存在但 FT 后消失]\n- **Line 170**: \"cmd\\_rep LF votes stagnation on 92.2\\% of OH windows (vs.\\ 65.5\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows\" → 应改为 \"5.39\\% of OH windows\" + \"2.3\\% FP rate / precision 97.91\\%\" [旧 embeddings 错误]\n- **Lines 171-195** (§5.5 Command Repetition Ablation): 整个 subsection 基于旧标签数据，需完全重写 [Table 3 数据全部无效：ZS 0.530→0.5984, FT 0.751→0.9763, +17.6pp→INVALID。新叙事：label quality as transfer bottleneck + prevalence-matched ablation -29.4pp + cmd_rep 是高精度低召回 coverage provider]\n\n---\n\n## [Analysis] (sections/analysis.tex)\n\n- **Line 12**: \"cmd\\_rep votes stagnation on 92.2\\% vs.\\ 65.5\\% of windows\" → OH 值应改为 \"5.39\\%\" [同上]\n\n---\n\n## [Conclusion] (sections/conclusion.tex)\n\n- **Line 7**: \"stagnation signals are fundamentally structural\" → 应改为 zero-shot transfer dominance framing [同 abstract]\n- **Line 12**: \"Command repetition leads stagnation onset by 1.87 steps on SWE-Agent but reverses on OpenHands, where its high false-positive rate corrupts silver labels---removing it improves fine-tuned probe F1 by 17.6\\,pp\" → **INVALID — 删除 \"high false-positive rate corrupts\" + \"removing improves 17.6pp\" claim** [新叙事方向：temporal dynamics reveal agent-specific LF roles; label quality audit shows transfer bottleneck is label version bias, not LF noise]\n\n---\n\n## [Appendix] (sections/appendix.tex)\n\n- **Line 67-68** (Table caption): references to cmd_rep having opposite effects → 叙事需更新以反映新标签结果\n- **Line 80** (Table subtable a): \"3-LF (w/ cmd\\_rep)\" ZS \"0.530\" → 应改为 \"0.5984\" [新标签]\n- **Line 80**: FT \"0.751\" → 应改为 \"0.9763\" [新标签]\n- **Line 81**: \"2-LF (no cmd\\_rep)\" FT \"0.927\" → 需新实验值 [旧标签结果无效]\n- **Line 83**: \"$\\Delta$\" \"+17.6\\,pp\" → **INVALID** [同上]\n- **Line 104** (Table caption): \"Removing \\texttt{cmd\\_rep} helps probe fine-tuning ($+$17.6\\,pp)\" → **INVALID**\n- **Line 108**: \"Removing \\texttt{cmd\\_rep} improves probe fine-tuned F1 by $+$17.6\\,pp\" → **INVALID**\n- **Lines 109-111**: \"divergence reveals that \\texttt{cmd\\_rep} noise requires learned adaptation: fine-tuning can filter it\" → 叙事完全基于旧标签，需重写 [cmd_rep 不是 noise source]\n\n---\n\n## [Limitations] (sections/limitations.tex)\n\n- 无旧数字问题。叙事一致。\n\n---\n\n## [Related Work] (sections/related_work.tex)\n\n- 无旧数字问题。叙事一致。\n\n---\n\n## [paper_framing.md]\n\npaper_framing.md 中旧数字多出现在变更说明语境中（描述\"从旧值到新值的修正\"），属于历史记录不需修改。但以下几处仍以旧值作为当前 claim：\n\n- **Core Claims 区域 Claim 2 段**: \"去掉 cmd_rep 从 +17.6pp 变为 -6.5pp\" — 这是变更记录，OK\n- **Headline result template** 段: 已更新，无残留旧值。OK\n- **writing_plan.yaml core_claim (line 11-15)**: \"fundamentally structural\" + \"embedding probes (0.906/0.751)\" → \"0.751\" 需改为 \"0.9763\"；\"fundamentally structural\" 需改为 \"zero-shot transfer dominance\" framing\n\n---\n\n## [writing_plan.yaml]\n\n- **Line 11-15** (meta.core_claim): \"fundamentally structural\" → 应改为 zero-shot transfer dominance\n- **Line 11-15** (meta.core_claim): \"0.751\" → 应改为 \"0.9763\"\n- **Line 26** (abstract bullet): \"removing it improves OH F1 by +17.6pp\" → **INVALID — 删除/替换**\n- **Line 36** (introduction hook): \"90% verbosity increase and 80% quality erosion\" → 应改为 \"77% / 75.5%\" [SlopCodeBench 原文数字修正，已在 paper_framing.md 记录但未应用]\n- **Line 37** (introduction bullet): \"removing it improves OH F1 by +17.6pp\" → **INVALID**\n- **Line 96** (experiments setup): \"20.9% stag\" → 应改为 \"21.45%\" [轻微偏差]\n- **Line 98** (experiments bullet): \"Probe 0.528 zero-shot (0.751 with 50% finetune)\" → 应改为 \"0.5984 zero-shot; 0.968 with 50% finetune\" [旧标签值]\n- **Line 101** (experiments bullet): \"92.3% firing rate + 71% FP on OH progress windows\" → 应改为 \"5.39% fire rate + 2.3% FP\" [旧 embeddings 错误]\n- **Line 215** (tab_oh_cmdrep caption): \"cmd_rep has 92.3% firing rate and 71% false positive rate on OH progress windows\" → 同上\n\n---\n\n## [Introduction] (sections/introduction.tex) — SlopCodeBench 数字\n\n- **Line 6**: \"recording verbosity increases of 90\\% and quality drops of 80\\%\" → 应改为 \"77\\%\" 和 \"75.5\\%\" [paper_framing.md 2026-05-15 修正记录：与原文 arXiv:2603.24755 一致]\n\n---\n\n## 叙事一致性问题汇总\n\n### INVALID 叙事（必须删除/重写）\n\n| 位置 | 旧叙事 | 问题 |\n|------|--------|------|\n| abstract L8 | \"removing it improves fine-tuned F1 by 17.6pp\" | 标签 bug 产物，新数据反转 |\n| intro L37-38 | \"71% FP + removing improves 17.6pp\" | 同上 |\n| experiments §5.5 全段 | cmd_rep 是 OH 噪声源 | 同上 |\n| conclusion L12 | \"removing it improves...17.6pp\" | 同上 |\n| appendix L104-111 | cmd_rep noise + removal helps | 同上 |\n\n### \"fundamentally structural\" → \"zero-shot transfer dominance\"\n\n| 位置 | 说明 |\n|------|------|\n| abstract L6 | Finding 1 标题 |\n| intro L28 | Finding 1 标题 |\n| conclusion L7 | Summary 段 |\n| writing_plan.yaml core_claim | meta 段 |\n\n### Cross-agent gap 重算\n\n旧叙事：structural GB 0.967 >> probe FT 0.751 (gap 21.6pp)\n新现实：structural GB ~0.9984 vs probe FT 0.9763 (gap 2.21pp)\n\n影响位置：\n- experiments.tex L88 (\"21.6pp above\")\n- experiments.tex L92-93 (\"even full OH fine-tuning only reaches 0.751\")\n- introduction.tex L29 (\"0.751 after full fine-tuning\")\n- The entire \"structural features transfer while embeddings do not\" narrative needs nuancing\n\n### OH stag rate 6.6% → 21.45%\n\n影响位置：\n- introduction.tex L9, L20\n- experiments.tex L20, Table L32\n- (method.tex 无直接提及 overall stag rate)\n\n---\n\n## 优先级排序\n\n1. **P0 — INVALID claims (必须删除)**: +17.6pp cmd_rep removal, 71% FP, \"cmd_rep corrupts labels\" 叙事\n2. **P0 — 核心数字错误**: OH stag rate 6.6%→21.45%, probe FT 0.751→0.9763, cmd_rep fire rate 92.2%→5.39%, cross-agent gap 21.6pp→2.21pp\n3. **P1 — Framing 更新**: \"fundamentally structural\" → \"zero-shot transfer dominance\"\n4. **P1 — probe ZS 值**: 0.528/0.530 → 0.5984\n5. **P2 — 支持文件**: writing_plan.yaml, paper_framing.md 残留旧值\n6. **P2 — SlopCodeBench 数字**: 90%/80% → 77%/75.5%\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T00:59:03.506902+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/framing-reaudit/inconsistency_list.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T00:59:03.507048+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T00:59:03.507189+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T00:59:03.507325+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "framing-reaudit-inconsistency-list",
  "type": "report",
  "description": "Full re-audit of all .tex files after D050+D051 framing update: identifies 40+ instances of outdated numbers (OH stag rate 6.6%→21.45%, probe FT 0.751→0.9763, cmd_rep fire rate 92.2%→5.39%, +17.6pp INVALID claim, 71% FP→2.3%, cross-agent gap 21.6pp→2.21pp) and narrative inconsistencies across abstract, introduction, method, experiments, analysis, conclusion, appendix, writing_plan.yaml.",
  "project": "agent_progress_probe",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/framing-reaudit/inconsistency_list.md",
  "tags": "['paper', 'reaudit', 'D050', 'D051', 'framing']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "framing-reaudit-inconsistency-list",
    "type": "report",
    "description": "Full re-audit of all .tex files after D050+D051 framing update: identifies 40+ instances of outdated numbers (OH stag rate 6.6%→21.45%, probe FT 0.751→0.9763, cmd_rep fire rate 92.2%→5.39%, +17.6pp INVALID claim, 71% FP→2.3%, cross-agent gap 21.6pp→2.21pp) and narrative inconsistencies across abstract, introduction, method, experiments, analysis, conclusion, appendix, writing_plan.yaml.",
    "project": "agent_progress_probe",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/framing-reaudit/inconsistency_list.md",
    "tags": "['paper', 'reaudit', 'D050', 'D051', 'framing']"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T00:59:03.507478+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_e7cb22\", \"name\": \"framing-reaudit-inconsistency-list\", \"type\": \"report\", \"description\": \"Full re-audit of all .tex files after D050+D051 framing update: identifies 40+ instances of outdated numbers (OH stag rate 6.6%→21.45%, probe FT 0.751→0.9763, cmd_rep fire rate 92.2%→5.39%, +17.6pp INVALID claim, 71% FP→2.3%, cross-agent gap 21.6pp→2.21pp) and narrative inconsistencies across abstract, introduction, method, experiments, analysis, conclusion, appendix, writing_plan.yaml.\", \"path\": \"projects/agent_progress_probe/artifacts/_project/report/inconsistency_list.md\", \"url\": null, \"project\": \"agent_progress_probe\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T00:58:55.267313+00:00\", \"tags\": [\"paper\", \"reaudit\", \"D050\", \"D051\", \"framing\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-15T00:59:03.507647+00:00_

完成。报告已写入 `artifacts/framing-reaudit/inconsistency_list.md` 并注册。

**核心发现**：

- **P0 — 必须删除的 INVALID claims**: +17.6pp cmd_rep removal 效果（5处）、71% FP rate（3处）、"cmd_rep corrupts labels" 叙事链
- **P0 — 核心数字错误**: OH stag rate 6.6%→21.45%（4处）、probe FT 0.751→0.9763（5处）、cmd_rep fire rate 92.2%→5.39%（5处）、cross-agent gap 21.6pp→2.21pp（1处）
- **P1 — Framing**: "fundamentally structural" → "zero-shot transfer dominance"（4处）
- **P1 — probe ZS**: 0.528/0.530 → 0.5984（3处）
- **P2 — 支持文件**: writing_plan.yaml 8处旧值、SlopCodeBench 90%/80%→77%/75.5%

总计 40+ 处需修改，覆盖 abstract/introduction/method/experiments/analysis/conclusion/appendix 全部章节 + writing_plan.yaml。experiments.tex §5.5 (Command Repetition Ablation) 需整段重写。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_framing-reaudit-tex-scan_20260515T005515"
}
```

</details>

---
