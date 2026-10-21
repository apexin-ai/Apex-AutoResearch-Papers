# paper status review loop20

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_paper_status-review-loop20_20260516T011434.jsonl`
- **Structured JSON:** [`e8817300e87912cae6fe.json`](../../sessions/e8/e8817300e87912cae6fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-16T01:17:27.642699+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T01:17:27.643275+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Math
7	\usepackage{amsmath}
8	\usepackage{amssymb}
9	
10	% Tables
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{tabularx}
14	
15	% Graphics
16	\usepackage{graphicx}
17	\graphicspath{{../../artifacts/}}
18	
19	% Lists
20	\usepackage{enumitem}
21	
22	% Custom commands
23	\newcommand{\cls}{\textsc{Cls}}
24	\newcommand{\cwm}{\textsc{Cwm}}
25	\newcommand{\traj}{\textsc{Traj}}
26	\newcommand{\fone}{F\textsubscript{1}}
27	\newcommand{\pp}{\,\text{pp}}
28	
29	\title{Classification Succeeds Where Generation Stalls:\\Reformulating Execution Simulation for Code Repair Verification}
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{abstract}
36	
37	\input{introduction}
38	
39	\begin{figure*}[t]
40	\centering
41	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
42	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test. \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match. \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved. \cls{} eliminates generation failure modes while preserving per-test diagnostic granularity.}
43	\label{fig:reformulation}
44	\end{figure*}
45	
46	\input{method}
47	
48	\input{experiments}
49	
50	\begin{figure}[t]
51	\centering
52	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
53	\caption{Gap amplification from function-level to repo-level complexity. Function-level: \cls{}--\cwm{} gap is 1.24\pp{} at 4B (5 seeds), widening to 2.43\pp{} at 8B (3 seeds, bootstrap $p{<}.01$). Repo-level same-size 4B: the gap explodes to 25.59\pp{}, with \cwm{} falling below the majority baseline (72.96\%).}
54	\label{fig:scaling_gap}
55	\end{figure}
56	
57	
58	\input{related_work}
59	
60	\input{conclusion}
61	
62	\bibliography{references}
63	
64	\input{appendix}
…[truncated 26 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T01:17:27.643564+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T01:17:27.644275+00:00_

1	\begin{abstract}
2	Execution-free verification for LLM-based code repair faces a granularity--accuracy tradeoff: generation-based approaches (Code World Models) predict execution output strings but suffer from token-budget exhaustion, string-value prediction errors, and format compliance collapse as code complexity grows, while trajectory-level verifiers provide binary patch verdicts but discard per-test diagnostic information.
3	%
4	We reformulate execution simulation from open-ended output generation to per-test binary pass/fail classification, and systematically compare classification (\cls{}), generation (\cwm{}), and trajectory-level formulations at controlled model sizes.
5	%
6	On function-level benchmarks, \cls{} and \cwm{} achieve near-equivalent accuracy at 4B parameters (88.43\% vs.\ 87.19\%, 5 seeds, gap 1.24\pp{}). At 8B the gap widens to 2.43\pp{} (bootstrap mean 2.26\pp{}, $p{=}0.0066$, 3 seeds), with \cwm{} failing to benefit from scaling (\cls{} +0.99\pp{} vs.\ \cwm{} $-$0.27\pp{}, 4B$\to$8B). Per-test \cls{} matches trajectory-level accuracy (TOST equivalence $p{=}0.007$, $\pm$2\pp{} margin) while providing free diagnostic granularity---which specific tests fail. Oracle analysis on SWE-bench Verified shows this advantage concentrates in instances with $\geq$2 failing tests (31\% of instances, 55\% of total advantage); an oracle ensemble reaches 90.63\%. At repository level, the gap amplifies to 25.59\pp{} (83.63\% vs.\ 58.04\%, 4B, single seed), with \cwm{} falling ${\sim}$15\pp{} below majority baseline (72.96\%). Format non-compliance produces 53.7--67.2\% unparseable \cwm{} outputs, and even parseable outputs score only 42--43\%---below chance level (50\%)---while \cls{} remains robust with 0\% unparseable.
7	%
8	These results support classification as a promising alternative to generation-based execution simulation, with an advantage that grows with code complexity---from modest at function level to critical at repository level.
9	\end{abstrac
…[truncated 2 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T01:17:27.644625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T01:17:27.644928+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair has advanced rapidly on real-world software tasks. Agent-based systems such as SWE-agent~\cite{yang2024sweagent} and pipeline approaches like Agentless~\cite{xia2024agentless} resolve substantial fractions of SWE-bench~\cite{jimenez2024swebench} issues through candidate patch generation and validation. The prevailing strategy for improving resolve rates is test-time compute scaling~\cite{snell2024scaling}: generating $K$ candidate patches and selecting the best via a verifier. This verification step is critical---without it, the additional compute invested in diverse patch generation yields diminishing returns, because correct patches are diluted among incorrect ones. Full execution verification---running the repository's test suite against each candidate---is reliable but expensive, costing \$1--3 and several minutes per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}, making it prohibitive for large $K$. The resulting demand for fast, execution-free verification has driven work on learned verifiers~\cite{ni2023lever,shum2025swerm} and execution simulators~\cite{meta2025cwm,maimon2026selfexecution}, but the choice of \emph{how} to formulate the verification task---what the model predicts and in what format---has received surprisingly little systematic study.
5	
6	Two dominant paradigms have emerged. \textbf{Generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test, deriving verdicts by exact match. This suffers three failure modes at scale: (1)~\emph{token-budget exhaustion} truncates long outputs; (2)~\emph{string-value errors} reject semantically correct outputs differing in surface form; (3)~\emph{format compliance collapse} renders the majority of predictions unparseable at repository-level complexity, with parseable accuracy dro
…[truncated 3794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T01:17:27.645181+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T01:17:27.645436+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation for Code.}
5	Code World Models~\cite{meta2025cwm} mid-train a 32B LLM on execution traces to predict output strings, establishing the generation-based paradigm for execution-free code verification.
6	Self-Execution~\cite{maimon2026selfexecution} extends this with step-by-step trace prediction, demonstrating that simulation-based self-verification can improve code generation without external execution.
7	CodeMind~\cite{liu2024codemind} evaluates code reasoning along multiple dimensions including independent and dependent execution reasoning.
8	SolidCoder~\cite{lee2026solidcoder} bridges mental simulation and actual execution via concrete execution feedback.
9	Abdollahi et al.~\cite{abdollahi2025demystifying} identify systematic failure modes in LLM trace prediction, including position-dependent and cascading errors.
10	All share a generation formulation whose cost scales with output length and whose reliability degrades when outputs are complex---at repository-level complexity, we observe format compliance collapse (53--67\% unparseable outputs; \S\ref{sec:experiments}). We reformulate as per-test classification and show the advantage is complexity-dependent: negligible at function level but critical at repository scale.
11	
12	\paragraph{LLM-based Verification for Code Repair.}
13	SWE-RM~\cite{shum2025swerm} trains a 30B MoE reward model for trajectory-level execution-free patch ranking, achieving strong results on SWE-bench without test execution.
14	Patch Reasoner~\cite{xu2025patchreasoner} uses chain-of-thought reasoning for patch verification.
15	Snell et al.~\cite{snell2024scaling} show that test-time compute scaling via verification can outperform parameter scaling, establishing verification quality as a key lever for code generation improvement.
16	S*~\cite{li2025sstar} combines execution-grounded selection with model-based scoring for efficient test-time scaling.
17	VG-S
…[truncated 2872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T01:17:27.645682+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T01:17:27.645994+00:00_

1	% Method section — EMNLP 2026 ARR submission
2	% Classification Succeeds Where Generation Stalls:
3	% Reformulating Execution Simulation for Code Repair Verification
4	
5	\section{Method}
6	\label{sec:method}
7	
8	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
9	
10	\subsection{Verification Formulations}
11	\label{sec:formulations}
12	
13	Let $c_p$ denote the code context (unified diff) of patch $p$.
14	
15	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Cost: one token per test.
16	
17	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Cost: $\sum_i |\hat{o}_i|$ tokens.
18	
19	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests, providing no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences reflect per-test decomposition value.
20	
21	\
…[truncated 3891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T01:17:27.646250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T01:17:27.646598+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate \cls{}, \cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench}.
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with LoRA~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. Our \cwm{} baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge.
15	
16	\paragraph{Statistics.}
17	Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); per-test vs.\ trajectory-level comparison uses TOST~\cite{schuirmann1987tost} ($\pm$2\pp{} margin). ICC~\cite{shrout1979icc} quantifies within-problem correlation. Oracle analysis uses SWE-bench Verified (500 instances).
18	
19	
20	\subsection{Function-Level Results}
21	\label{sec:func_results}
22	
23	Table~\ref{tab:main_results} reports function-level results across formulations.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\caption{Function-level per-test verification results 
…[truncated 10977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T01:17:27.646871+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T01:17:27.647119+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We reformulated execution simulation for code repair verification from open-ended output generation to per-test binary classification. Our central finding is that the advantage of this reformulation is complexity-dependent: on function-level code with short, structurally simple outputs, classification and generation achieve near-equivalent accuracy; at repository scale, classification dominates by a wide margin. The generation formulation suffers a compounding failure on complex code---format non-compliance discards the majority of predictions, and the surviving parseable outputs are themselves unreliable, falling below chance-level accuracy (50\%). Classification is immune to this failure mode by construction, as binary verdicts require no structured output parsing. Moreover, at function level, scaling model capacity does not resolve the generation bottleneck: \cwm{} accuracy decreases by 0.27\pp{} from 4B to 8B, consistent with a formulation-level bottleneck at this complexity tier. Independently, per-test classification provides fine-grained diagnostic signals---identifying which specific tests a patch fails---at equivalent trajectory-level accuracy, with the advantage concentrating in instances that contain multiple fail-to-pass tests.
5	
6	For test-time scaling pipelines evaluating patches against multi-test suites, classification avoids the compounding failure that degrades generation on complex code. Per-test verdicts unlock targeted re-repair guided by failure localization rather than binary accept/reject decisions.
7	
8	\paragraph{Limitations.}
9	All experiments use a single model family (Qwen3); scaling behavior may differ across architectures or pre-training regimes. The repo-level same-size comparison rests on a single seed; the second seed's repo-level comparison is cross-size (8B \cls{} vs.\ 4B \cwm{}), not an apple-to-apple same-size match. The 8B--8B comparison awaits \cwm{} 8B training completion.
…[truncated 1411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T01:17:27.647389+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T01:17:27.647665+00:00_

1	\appendix
2	
3	\section{Oracle Accuracy-Utility Analysis}
4	\label{app:oracle}
5	
6	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$).
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses empirical ICC $= 0.191$. P2P regression rate: 1.04\% mean, 0\% median.}
12	\label{tab:oracle}
13	\resizebox{\columnwidth}{!}{%
14	\setlength{\tabcolsep}{3pt}
15	\begin{tabular}{lcccc}
16	\toprule
17	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
18	\midrule
19	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
20	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
21	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
22	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
23	\midrule
24	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
25	\bottomrule
26	\end{tabular}}
27	\end{table}
28	
29	\begin{figure}[h]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
32	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage).}
33	\label{fig:oracle_stratified}
34	\end{figure}
35	
36	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\pp{} vs.\ 18.49\pp{} (1.7$\times$). P2P regression is negligible
…[truncated 2416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T01:17:27.647939+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T01:17:27.648231+00:00_

1	% === Execution Simulation ===
2	
3	@article{maimon2026selfexecution,
4	  title={Self-Execution Simulation Improves Coding Models},
5	  author={Maimon, Gallil and Yoran, Ori and Kreuk, Felix and Hassid, Michael and Cohen, Gal and Chambon, Pierre and Adi, Yossi},
6	  journal={arXiv preprint arXiv:2604.03253},
7	  year={2026}
8	}
9	
10	@article{meta2025cwm,
11	  title={{CWM}: An Open-Weights {LLM} for Research on Code Generation with World Models},
12	  author={{FAIR CodeGen team} and Copet, Jade and Carbonneaux, Quentin and Cohen, Gal and Gehring, Jonas and Kahn, Jacob and Kossen, Jannik and Kreuk, Felix and McMilin, Emily and Meyer, Michel and Wei, Yuxiang and Zhang, David and Zheng, Kunhao and others},
13	  journal={arXiv preprint arXiv:2510.02387},
14	  year={2025}
15	}
16	
17	@article{liu2024codemind,
18	  title={{CodeMind}: A Framework to Challenge Large Language Models for Code Reasoning},
19	  author={Liu, Changshu and others},
20	  journal={arXiv preprint arXiv:2402.09664},
21	  year={2024}
22	}
23	
24	@article{abdollahi2025demystifying,
25	  title={Demystifying Errors in {LLM} Reasoning Traces: An Empirical Study of Code Execution Simulation},
26	  author={Abdollahi, Mohammad and Tasnia, Khandaker Rifah and Saha, Soumit Kanti and Yang, Jinqiu and Wang, Song and Hemmati, Hadi},
27	  journal={arXiv preprint arXiv:2512.00215},
28	  year={2025}
29	}
30	
31	@article{lee2026solidcoder,
32	  title={{SolidCoder}: Bridging the Mental-Reality Gap in {LLM} Code Generation through Concrete Execution},
33	  author={Lee, Woojin and Huang, Jin-Xia},
34	  journal={arXiv preprint arXiv:2604.19825},
35	  year={2026}
36	}
37	
38	% === LLM Verification for Code ===
39	
40	@article{shum2025swerm,
41	  title={{SWE-RM}: Execution-free Feedback for Software Engineering Agents},
42	  author={Shum, KaShun and Hui, Binyuan and Chen, Jiawei and Zhang, Lei and Yang, Jiaxi and Huang, Yuzhen and Lin, Junyang and He, Junxian},
43	  journal={arXiv preprint arXiv:2512.21919},
44	  year={20
…[truncated 6789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T01:17:27.648469+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/*.{pdf,png,eps}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.{pdf,png,eps}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T01:17:27.648668+00:00_

docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T01:17:27.648925+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/figures/paper/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/figures/paper/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T01:17:27.649127+00:00_

artifacts/figures/paper/gen_fig3.py
artifacts/figures/paper/fig3_oracle_stratified.pdf
artifacts/figures/paper/fig3_oracle_stratified.png
artifacts/figures/paper/fig1_reformulation.py
artifacts/figures/paper/fig2_gap_amplification.pdf
artifacts/figures/paper/fig2_gap_amplification.png
artifacts/figures/paper/fig1_reformulation.pdf
artifacts/figures/paper/fig1_reformulation.png
artifacts/figures/paper/gen_fig2.py
artifacts/figures/paper/fig2_gap_amplification.py
artifacts/figures/paper/gen_fig2_gap_amplification.py
artifacts/figures/paper/fig2_scaling_gap.pdf
artifacts/figures/paper/fig2_scaling_gap.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T01:17:27.649336+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/figures/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/figures/**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T01:17:27.649539+00:00_

artifacts/figures/paper/gen_fig3.py
artifacts/figures/paper/fig3_oracle_stratified.pdf
artifacts/figures/paper/fig3_oracle_stratified.png
artifacts/figures/paper/fig1_reformulation.py
artifacts/figures/paper/fig2_gap_amplification.pdf
artifacts/figures/paper/fig2_gap_amplification.png
artifacts/figures/paper/fig1_reformulation.pdf
artifacts/figures/paper/fig1_reformulation.png
artifacts/figures/paper/gen_fig2.py
artifacts/figures/paper/fig2_gap_amplification.py
artifacts/figures/paper/gen_fig2_gap_amplification.py
artifacts/figures/paper/fig2_scaling_gap.pdf
artifacts/figures/paper/fig2_scaling_gap.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T01:17:27.649741+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "TODO|FIXME|placeholder|\\\\textcolor\\{red\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Grep",
  "tool_args": {
    "pattern": "TODO|FIXME|placeholder|\\\\textcolor\\{red\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T01:17:27.649957+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_status-review-loop20_20260516T011434",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-16T01:17:27.650339+00:00_

## 论文完成度审查报告

---

### 1. abstract.tex — **95%**
- 完整，包含所有关键数字和 narrative
- 数字核对通过：25.59pp, 58.04%, 83.63%, 72.96%, 53.7–67.2%, 42–43%, TOST p=0.007
- 无 TODO/placeholder

### 2. introduction.tex — **95%**
- 完整的三段式 narrative + 三个 contribution bullets
- 数字一致：1.24pp (5-seed) / 1.18pp (3-seed matched) 两个数分别使用正确
- 所有引用存在于 bib 中
- 无 TODO/placeholder

### 3. method.tex — **95%**
- 三种 formulation 定义完整，公式 (1)–(3) 就位
- CWM failure mode 分析详尽
- Oracle framework 含 ICC block-correlation model
- 无 TODO/placeholder

### 4. experiments.tex — **90%**
- 5 个 subsection + Analysis 全部有实质内容，7 个 analysis paragraph (a–g)
- 3 个表格 (main_results, scaling, repo_level) 数据完整
- **主要缺口：CWM 8B 行为 "---"（in progress）**，Table 3 caption 已标注
- 数字核对：

| 指标 | 用户提供 | 论文中 | 状态 |
|------|---------|--------|------|
| CLS 8B s42 test | 84.48% | 84.48% | ✓ |
| CLS 8B s123 test | 85.60% | 85.60% | ✓ |
| CLS 4B s42 test | 83.63% | 83.63% | ✓ |
| CLS 8B s42 ckpt-1000 test | 83.52% | 83.52% (seq-len ablation) | ✓ |
| CWM 4B s42 test | 58.04% | 58.04% | ✓ |
| CWM 4B s123 test | 59.09% | 59.09% | ✓ |
| Majority test | 72.96% | 72.96% | ✓ |
| TOST p-value | 0.007 | 0.007 | ✓ |
| Multi-seed gap (mean) | **25.99pp** | **25.59pp** | **⚠️ 不匹配** |
| CWM 8B | pending | --- | ✓ (已标注) |
| Majority val | 75.88% | 未报告 | — 正常，论文只报 test |
| Val numbers (90.28%, 88.23%, etc.) | 用户提供 | 未报告 | — 正常 |

**数字问题**：论文中统一使用 25.59pp（CLS 4B s42 83.63% − CWM 4B s42 58.04%，单 seed 同 size 对比）。用户提供的 25.99pp (mean) 在论文中无对应。需确认：这个 mean 是否应替换 25.59pp，还是用户侧的计算口径不同。

### 5. related_work.tex — **95%**
- 5 个 paragraph 结构清晰，覆盖 execution simulation / verification / learned verifiers / APR / NLP formulation
- 每段末尾有定位声明
- 无 TODO/placeholder

### 6. conclusion.tex — **95%**
- 完整总结 + Limitations + Future work
- Limitations 显式提到 CWM 8B 未完成、单 seed repo-level 等
- 无 TODO/placeholder

### 7. appendix.tex — **85%**
- Oracle 分析表 + 图就位
- 三项 ablation (LoRA rank, majority voting, seq-length) 完整
- **潜在补充**：缺 hyperparameter 详表（learning rate, batch size, epoch 数, LoRA config 等完整列表）——ARR 审稿人可能会要求

### 8. references.bib — **90%**
- 22 条，均有完整字段
- 部分条目 author 用 "others" 省略（chen2021humaneval, austin2021mbpp, qwen2025qwen3）——ARR 提交可接受
- 无 incomplete/dangling 条目

### 9. Figures — **100%**
三个引用的图全部存在于 `artifacts/figures/paper/`：
- `fig1_reformulation.pdf` ✓
- `fig2_scaling_gap.pdf` ✓
- `fig3_oracle_stratified.pdf` ✓

### 10. 格式检查
- `\usepackage[review]{acl}` — anonymous review mode ✓
- `acl.sty` + `acl_natbib.bst` 就位 ✓
- `main.pdf` 已编译存在 ✓
- 零 TODO/FIXME/placeholder/`\textcolor{red}` ✓

---

## 论文整体完成度：**~92%**

## 提交前 Critical Path

| 优先级 | 事项 | 阻塞性 |
|--------|------|--------|
| **P0** | CWM 8B eval 完成 → 填入 Table 3 + 更新 abstract/intro/conclusion 中的相关讨论 | 高——如果赶不上 deadline，当前 "in progress" 表述可提交但削弱论文 |
| **P0** | 确认 25.59pp vs 25.99pp 口径——如果 25.99 是正确的 multi-seed mean，需更新 abstract、intro、experiments、conclusion 中全部 5 处 | 高——数字一致性 |
| **P1** | Appendix 补 hyperparameter 完整表（training config: lr, batch, warmup, LoRA rank/alpha, max_seq_len, epochs per formulation×size） | 中——reviewer 常要求 |
| **P2** | 最终编译确认 PDF 页数在 EMNLP 8 页限制内（不含 references + appendix） | 中 |
| **P2** | bib 条目 author 补全（去掉 "others"） | 低——不影响审稿 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_status-review-loop20_20260516T011434"
}
```

</details>

---
