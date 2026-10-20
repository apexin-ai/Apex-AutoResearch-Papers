# write 14b insertion audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_write_14b-insertion-audit_20260522T191841.jsonl`
- **Structured JSON:** [`331d085b6779bba9103d.json`](../../sessions/33/331d085b6779bba9103d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-22T19:20:36.026104+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T19:20:36.026425+00:00_

docs/paper/method.tex
docs/paper/checklist.tex
docs/paper/abstract.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/experiments.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T19:20:36.026594+00:00_

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
  "session": "worker_write_14b-insertion-audit_20260522T191841",
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

_source line 4 · 2026-05-22T19:20:36.026734+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T19:20:36.026915+00:00_

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
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T19:20:36.027062+00:00_

1	\begin{abstract}
2	LLM-based program repair increasingly leverages test-time compute scaling, generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares these formulations under matched conditions.
3	
4	We present the first systematic comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is model-dependent and not confirmed after multiple comparison correction. At repository level, a significant interaction ($z{=}-23.7$, DeepSeek-Coder) confirms this equivalence collapses: the \cls{}--\cwm{} gap widens to 18--26\pp{} across 3 seeds per model under our ${\leq}$8B LoRA protocol in variant-level evaluation, driven by format collapse in generation-based simulation. Gap magnitude depends on multiple confounds.
5	
6	Error complementarity and a failure mode taxonomy motivate complexity-aware formulation routing over uniform selection.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T19:20:36.027199+00:00_

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
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T19:20:36.027365+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We present the first systematic empirical comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our contribution is primarily methodological: a matched experimenta
…[truncated 2383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T19:20:36.027530+00:00_

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
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T19:20:36.027698+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation
…[truncated 3353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T19:20:36.027862+00:00_

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
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T19:20:36.028133+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss because repo-level execution traces often exceed the 2,048-token sequence length limit; after truncation, many samples have all target tokens removed (labels entirely $-$100), producing degenerate loss---a formulation-inherent weakness that classification and trajectory formulations avoid by design. NaN loss defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency chec
…[truncated 20991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T19:20:36.028288+00:00_

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
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T19:20:36.028441+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. CodeScaler~\cite{zhu2026codescaler} trains execution-free reward models for both RL and test-time scaling. Verification formulations span trajectory-level reward~\cite{shum2025swerm}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. GenRM~\cite{hosseini2025genrm} and GenPRM~\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formula
…[truncated 2025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T19:20:36.028586+00:00_

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
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T19:20:36.028728+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} equivalence is not confirmed after multiple comparison correction. Per-test classification achieves 217$\times$ higher throughput while providing diagnostic signal. Complementary errors (oracle: 90.63\%/95.83\%; single-seed) motivate complexity-aware routing. At repository level under ${\leq}$8B LoRA, divergence reaches 18--26\pp{} ($z{=}-23.7$, 3 seeds per model), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}). Three failure modes (format collapse, decision collapse, aggregation penalty) are consistent across families. \cls{} is recommended primarily for its throughput advantage and diagnostic capability; the accuracy advantage over \traj{} is directional but underpowered ($n{=}48$, MDE${\approx}$25\pp{}; Appendix~\ref{app:power}). All findings are conditioned on ${\leq}$8B LoRA fine-tuning; at larger scale, the generation bottleneck may diminish (\S\ref{sec:threats}).
5	
6	Three directions follow: (1)~oracle gains motivate complexity-aware routing using the failure mode taxonomy as routing features; (2)~the semantic generation bottleneck (four interventions fail; Appendix~\ref{app:extended_analysis}(g)) suggests capacity scaling or execution trace pretraining~\cite{meta2025cwm} is needed---testing at 32B+ would resolve the primary open question; (3)~larger-scale evaluation of per-test diagnostics for downstream repair ($n{=}44$ in our pilot) would test whether \cls{}'s throughput advantage extends to repair pipelines.
7	
8	\section*{Limitations}
9	
10	Repo-level \cwm{} uses 3 seeds per model; the gap (18--26\pp{}) exceeds any single confound (\S\ref{sec:threats}), but correlated confounds require further repl
…[truncated 840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T19:20:36.028890+00:00_

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
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T19:20:36.029318+00:00_

1	\appendix
2	
3	\noindent\textbf{Appendix overview.} A: Oracle resolve advantage. B: Ablation studies. C-F: Extended analysis (error complementarity, parseable accuracy, forced parsing, qualitative errors, failed interventions, mutation scaling, inference efficiency, re-repair, chain-of-thought). G: TOST sensitivity. G$'$: Bayesian ROPE. H: Effect sizes. I: Holm-Bonferroni. J: Mixed-effects regression. K: Parseable bias. L: CWM convergence. M: Few-shot. N: Threats. O: Downsample. P: Limitations.
4	
5	\section{Oracle Accuracy-Utility Analysis}
6	\label{app:oracle}
7	
8	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
14	\label{tab:oracle}
15	\resizebox{\columnwidth}{!}{%
16	\setlength{\tabcolsep}{3pt}
17	\begin{tabular}{lcccc}
18	\toprule
19	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
20	\midrule
21	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
22	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
23	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
24	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
25	\midrule
26	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
31	\begin{figure}[h]
32	\centering
33	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
34	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.
…[truncated 55682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T19:20:36.029482+00:00_

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
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T19:20:36.029643+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\graphicspath{{../../artifacts/}}
21	
22	% Lists
23	\usepackage{enumitem}
24	
25	% Custom commands
26	\newcommand{\cls}{\textsc{Cls}}
27	\newcommand{\cwm}{\textsc{Cwm}}
28	\newcommand{\traj}{\textsc{Traj}}
29	\newcommand{\fone}{F\textsubscript{1}}
30	\newcommand{\pp}{\,\text{pp}}
31	\newcommand{\tbd}{\textsc{tbd}}
32	
33	\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}
34	\author{Anonymous}
35	
36	\begin{document}
37	\maketitle
38	
39	\input{abstract}
40	
41	\input{introduction}
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
46	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
47	\label{fig:reformulation}
48	\end{figure*}
49	
50	\input{method}
51	
52	\input{experiments}
53	
54	\begin{figure}[t]
55	\centering
56	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
57	\caption{Gap amplification from function to repo level. At function level, the \cls{}--\cwm{} gap is 1--3\pp{}; at repo level, it widens to 18--26\pp{} with \cwm{} falling below majority baseline.}
58	\label{fig:scaling_gap}
59	\end{figure}
60	
61	
62	\input{related_work}
63	
64	\input{conclusion}
65
…[truncated 105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T19:20:36.029810+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T19:20:36.030002+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/paper_framing.md\", \"content\": \"# Paper Framing — exec-sim-repair-verifier\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Deadline: ARR May 25, 2026\\n\\n## Framing Evolution\\n- **D116 (2026-05-16)**: Pivoted from \\\"CLS scales where generation fails\\\" (advocacy) to \\\"The Formulation Design Space for Neural Code Verification\\\" (empirical characterization)\\n- **D155 (2026-05-20)**: DeepSeek repo-level data confirms CWM collapse is **complexity-dependent** (both models collapse at repo-level), NOT tokenizer-specific. Original D116 claim \\\"Qwen 93% vs DeepSeek 11.8%\\\" was function-level only; repo-level shows DeepSeek CWM also 51-74% unparseable.\\n- **N4 Reframe**: Function-level equivalence elevated to headline finding; phase transition (func→repo divergence) as differentiating contribution.\\n\\n## Core Claims (current — post D155/N4 Reframe)\\n\\n1. **Formulation Equivalence at Function-Level**: CLS, CWM, and TRAJ achieve statistically equivalent accuracy at function-level across two model families (≤1.3pp gap, TOST p=0.007). Per-test CLS provides diagnostic granularity (which tests fail) at comparable accuracy with 217× throughput over CWM, though downstream re-repair benefit is unvalidated (n=44, p=0.42).\\n\\n2. **Phase Transition: Complexity-Dependent Divergence**: Formulations diverge 19-26pp at repo-level, driven by CWM format collapse (51-74% unparseable outputs, 0% truncation). Direction consistent across both model families; magnitude varies (Qwen3 74% unparseable vs DeepSeek 51% at matched seq_length). This is NOT tokenizer-specific — both models collapse when outputs are long and structured.\\n\\n3. **Error Complementarity**: CLS and CWM exhibit partial complementarity from different fail-bias degrees (CLS 56.5% FP, CWM 70.3% FP), yielding oracle ensemble 90.63% (+2.80pp over be
…[truncated 3591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_14b-insertion-audit_20260522T191841",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-22T19:20:36.030271+00:00_

Now I have all the content. Let me compile the audit.

## 14B 数据插入点清单

### Tables

1. **Table 1 `tab:main_results`** (experiments.tex:25–58): Function-level per-test accuracy。当前有 Qwen3-4B / DeepSeek-6.7B。需要加 Qwen3-14B 行（CLS/CWM/TRAJ）。

2. **Table 2 `tab:scaling`** (experiments.tex:68–88): Model-size scaling，当前只有 4B 和 8B 两行。需要加 14B 行，并更新 $\Delta$ 列（新增 8B→14B 增量）。这是 14B 数据最核心的表。

3. **Table 3 `tab:repo_level`** (experiments.tex:112–135): Repo-level 跨 formulation 比较。当前有 Qwen3-4B / Qwen3-8B / DeepSeek-6.7B。需要加 Qwen3-14B 行。

4. **Table 4 `tab:taxonomy`** (experiments.tex:145–162): Failure mode taxonomy。如果 14B 的 CWM format collapse 率有变化，需要更新或增加 14B representative 行。

5. **Table `tab:variant_level`** (appendix.tex:159–193): Variant-level accuracy。需要加 Qwen3-14B 行（CLS/CWM/TRAJ）。

6. **Table `tab:mutation_breakdown`** (appendix.tex:109–127): Per-mutation accuracy。当前有 CLS 4B/8B 和 CWM 4B/8B 列。需要加 CLS 14B 和 CWM 14B 列。

7. **Table `tab:cwm_mutation_parse`** (appendix.tex:136–150): CWM parse rates per mutation。当前有 4B/8B。需要加 14B 列。

8. **Table `tab:hyperparams`** (appendix.tex:200–243): Training hyperparameters。Model-family-specific 表当前有 Qwen3-4B / Qwen3-8B / DS-6.7B 三列。需要加 Qwen3-14B 列。

9. **Table `tab:cwm_convergence`** (appendix.tex:533–549): CWM eval loss across training。如果跑了 14B CWM repo-level，需要加 14B 列。

10. **Table `tab:variant_power`** (appendix.tex:450–471): Variant-level bootstrap analysis。需要加 14B 相关的 CLS vs CWM / CLS vs TRAJ 行。

11. **Table `tab:rank_ablation`** (appendix.tex:49–64): LoRA rank ablation for CWM。当前只有 4B。如果 14B 也做了 rank ablation 需要加；否则可不改。

---

### Figures

1. **Figure 2 `fig:scaling_gap`** (main.tex:54–59, 引用 `figures/paper/fig2_scaling_gap.pdf`): Gap amplification 图。当前显示 4B→8B 两个点。需要加 14B 数据点，变成三点连线。**这是最重要的图更新。**

2. 可能需要检查 `figure2_v2.pdf` / `figure2_v2.png` 是否是 Figure 2 的新版本，需要同步更新。

---

### 正文段落

#### Abstract (abstract.tex)
- **Line 4**: `"under ${\leq}$8B LoRA fine-tuning"` → 需要改为 `≤14B` 或 `4–14B`
- **Line 4**: `"under our ${\leq}$8B LoRA protocol"` → 同上

#### Introduction (introduction.tex)
- **Line 8**: `"two representative code LLM families (Qwen3, DeepSeek-Coder)"` — 模型列表可能需要提及 14B
- **Line 8**: `"${\leq}$8B LoRA protocol"` → 更新
- **Line 8**: `"35--36\pp{} at repo level"` — 如果 14B 基线不同，需要更新
- **Line 13**: `"at repository level under ${\leq}$8B LoRA"` → 更新
- **Line 14**: `"We fine-tune Qwen3-4B and Qwen3-8B"` 间接引用（在 experiments 里），但 intro 也提到模型覆盖范围

#### Experiments — Setup (experiments.tex:14)
- **Line 14**: `"We fine-tune Qwen3-4B and Qwen3-8B"` → 加 `Qwen3-14B`
- **Line 14**: `"DeepSeek-Coder-6.7B"` 保持不变

#### Experiments — Scaling (experiments.tex:63–92)
- **Line 66**: `"Table~\ref{tab:scaling} compares all three formulations at 4B and 8B"` → 加 14B
- **Line 71**: Table caption `"accuracy (\%) at 4B and 8B"` → 加 14B
- **Line 90**: `"The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B"` → 需要加 14B 的 gap 数值
- **Line 92**: `"\cwm{} flat scaling ($-$0.03\pp{})"` → 看 14B 是否依然 flat
- **Line 92**: `"\traj{} also shows no scaling benefit at repo level (72.92\% at both 4B and 8B); only \cls{} scales positively"` → 更新 14B 数据

#### Experiments — Repo-level (experiments.tex:107–168)
- **Line 139**: `"the gap is 25.59\pp{} at 4B...and 18.35\pp{} at 8B"` → 加 14B gap
- **Line 164**: CWM default assignment artifact 的 4B→8B 趋势 → 加 14B
- **Line 166**: `"The \cls{}--\cwm{} gap widens from 1--3\pp{} (function) to 18--26\pp{} (repo)"` → 范围可能需要调整
- **Line 168**: 混合效应模型可能需要纳入 14B 数据重新拟合

#### Experiments — Analysis (experiments.tex:173–183)
- **Line 180**: `"217$\times$ higher throughput"` — 如果 14B 有不同的推理效率数据
- **Line 182**: oracle/complementarity 数字可能需要更新

#### Conclusion (conclusion.tex)
- **Line 4**: `"${\leq}$8B LoRA"` 出现两次 → 更新为 `≤14B`
- **Line 4**: `"All findings are conditioned on ${\leq}$8B LoRA fine-tuning"` → 更新
- **Line 6**: `"testing at 32B+ would resolve the primary open question"` → 如果 14B 缩小了 gap，这句可能需要修改

#### Limitations (conclusion.tex:8–10)
- **Line 8**: `"${\leq}$8B LoRA fine-tuning"` → 更新
- **Line 10**: `"Model coverage is limited to 6--8B code-specialized LLMs"` → 更新为 `6--14B`

#### Appendix — Threats (appendix.tex:522–559)
- **Line 557**: `"4--8B LoRA fine-tuning"` → `4--14B`
- **Line 557**: `"all repo-level \cwm{} conclusions conditional on the ${\leq}$8B LoRA regime"` → 更新
- **Line 559**: `"the repo-level \cls{}--\cwm{} gap (18--26\pp{}) exceeds any single assessed confound"` → 范围可能变化
- **Line 564**: `"6--8B code-specialized LLMs"` → `6--14B`

#### Appendix — Extended Analysis (appendix.tex:361–411)
- **Paragraph (g) Failed interventions**: `"Model scaling (4B→8B)"` → 如果 14B 改变了结论，需要重写或追加 8B→14B 结果
- **Paragraph (i) Inference efficiency**: throughput 数据可能需要加 14B
- **Paragraph (k) CoT**: `"Within the ${\leq}$8B LoRA regime"` → 更新

#### Appendix — Hyperparams (appendix.tex:253)
- **Line 253**: `"Total compute budget: ${\sim}$370 GPU-hours across 223 completed runs"` → 加上 14B runs 的 GPU 时间

#### Appendix — Interaction model (appendix.tex:505–514)
- 混合效应回归可能需要纳入 14B 数据重新拟合，或至少提及 14B 支持/改变现有结论

---

### paper_framing.md 更新点
- `"≤8B LoRA"` 贯穿全文 → 改为 `≤14B`
- `"Model coverage is limited to 6--8B"` → `6--14B`
- Story Spine 中 `"At ≤8B LoRA deployment scale"` → 更新
- Anticipated Reviewer Concerns 的 `"CWM comparison unfair (≤8B LoRA)"` → 14B 数据部分缓解此 concern

---

### 优先级排序

| 优先级 | 位置 | 原因 |
|--------|------|------|
| P0 | Table 2 (scaling) + Figure 2 | 14B 是第三个 scaling 数据点，直接影响 scaling story |
| P0 | Table 3 (repo_level) | repo-level 是论文核心差异化结论 |
| P0 | Abstract / Conclusion 中 `≤8B` 措辞 | 读者第一印象和最终结论 |
| P1 | Table 1 (main_results) | 如果 14B function-level 也跑了 |
| P1 | experiments.tex §Scaling 段落叙述 | 需要描述 14B 趋势 |
| P1 | experiments.tex §Repo-level 段落 gap 数值 | 更新 range |
| P2 | Appendix tables (variant_level, mutation_breakdown, cwm_parse, hyperparams) | 完整性 |
| P2 | Appendix threats / limitations 中 `≤8B` | 措辞一致性 |
| P3 | paper_framing.md | 内部文档，非论文本体 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_write_14b-insertion-audit_20260522T191841"
}
```

</details>

---
