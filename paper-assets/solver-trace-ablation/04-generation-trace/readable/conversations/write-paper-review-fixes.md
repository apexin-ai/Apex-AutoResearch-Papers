# write paper review fixes

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 0
- **Tool calls:** 40
- **Original source:** `logs/chats/worker_write_paper-review-fixes_20260514T231354.jsonl`
- **Structured JSON:** [`e5bd901c0f7b3c06dd5d.json`](../../sessions/e5/e5bd901c0f7b3c06dd5d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

81 recorded events

### Tool call

_source line 1 · 2026-05-14T23:19:42.410369+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T23:19:42.410873+00:00_

paper/paper.tex
paper/abstract.tex
paper/introduction.tex
paper/limitations.tex
paper/main.tex
paper/conclusion.tex
paper/appendix.tex
paper/method.tex
paper/experiments.tex
paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T23:19:42.411138+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T23:19:42.411339+00:00_

paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T23:19:42.411525+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "literature_map.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Glob",
  "tool_args": {
    "pattern": "literature_map.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T23:19:42.413732+00:00_

artifacts/literature_map.yaml
literature_map.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Glob",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T23:19:42.413984+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T23:19:42.414219+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer: A Case Study with Qwen3-4B}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	\input{limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T23:19:42.414454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/paper.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T23:19:42.414656+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath}
5	\usepackage{amssymb}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{algorithm}
9	\usepackage{algorithmic}
10	\usepackage{enumitem}
11	\usepackage[protrusion=true,expansion=false]{microtype}
12	
13	\graphicspath{{figures/}}
14	
15	\title{Solver Trace Ablation Reveals Meta-Level Goodhart's Law\\in Neurosymbolic Reasoning}
16	
17	\author{Anonymous ACL submission}
18	
19	\begin{document}
20	\maketitle
21	
22	\input{abstract}
23	
24	\input{introduction}
25	\input{related_work}
26	\input{method}
27	\input{experiments}
28	\input{discussion}
29	\input{conclusion}
30	
31	\bibliography{references}
32	
33	\input{appendix}
34	
35	\end{document}
36	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T23:19:42.414928+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T23:19:42.415169+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic Reasoning with LLMs.}
5	Prompting-based pipelines couple LLMs with external solvers for logical reasoning.
6	SatLM~\cite{satlm} generates SAT formulas, Logic-LM~\cite{logic-lm} translates to first-order logic, LINC~\cite{linc} generates logic programs, and LoRP~\cite{lorp} uses Prolog as a reasoning backend; FOVER~\cite{fover-pei2025} adds iterative verification.
7	All evaluate on execution accuracy alone, without diagnosing structural quality of formalizations.
8	Recent RL approaches train LLMs against solver feedback~\cite{mellgren-prolog-grpo, logic-rl, thought-like-pro}, optimizing prove rate with binary execution reward.
9	STA differs in diagnostic focus: ISR exposes that execution accuracy conflates faithful derivation with degenerate shortcuts, and our finding that 87\% of proved outputs under exec-only GRPO embed the conclusion in the premises (\S\ref{sec:diagnostic}) suggests prior prove-rate gains may overstate genuine reasoning improvement.
10	We adopt FOLIO~\cite{folio} as it is the only publicly available NLI benchmark providing both FOL and Prolog annotations, enabling our cross-logic diagnostic transfer experiments; ProofWriter~\cite{proofwriter} and ProntoQA~\cite{prontoqa} offer synthetic logical reasoning benchmarks but lack the multi-logic annotation required for cross-logic comparison.
11	
12	\paragraph{Reward Shaping and Process Supervision.}
13	Binary outcome rewards motivate process-level supervision: learned process reward models~\cite[PRMs;][]{lightman-verify-step, math-shepherd} provide step-level feedback, solver-grounded signals~\cite{rlsf} leverage formal verification, and rubric-based rewards~\cite{rubric-grpo} encode structured evaluation criteria.
14	However, process rewards introduce their own failure modes: design choices dominate signal effects~\cite{gao-effective-rl-reward}, process and outcome rewards can conflict~\cite{prof-process-outcome}, and PR
…[truncated 2848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T23:19:42.415376+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T23:19:42.415679+00:00_

1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseekmath,
6	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
7	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
8	  journal      = {arXiv preprint arXiv:2402.03300},
9	  year         = {2024},
10	  eprint       = {2402.03300},
11	  archivePrefix = {arXiv},
12	  primaryClass = {cs.AI},
13	}
14	
15	@article{logic-rl,
16	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
17	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
18	  journal      = {arXiv preprint arXiv:2502.14768},
19	  year         = {2025},
20	  eprint       = {2502.14768},
21	  archivePrefix = {arXiv},
22	  primaryClass = {cs.AI},
23	}
24	
25	@article{mellgren-prolog-grpo,
26	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
27	  title        = {{Training Language Models to Use Prolog as a Tool}},
28	  journal      = {arXiv preprint arXiv:2512.07407},
29	  year         = {2025},
30	  eprint       = {2512.07407},
31	  archivePrefix = {arXiv},
32	  primaryClass = {cs.AI},
33	}
34	
35	@inproceedings{satlm,
36	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
37	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
38	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
39	  year         = {2023},
40	}
41	
42	@article{thought-like-pro,
43	  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},
44	  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models throug
…[truncated 14013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T23:19:42.417994+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T23:19:42.418233+00:00_

1	\begin{abstract}
2	GRPO-trained neurosymbolic formalizers achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution-based evaluation. We introduce \emph{Solver Trace Ablation} (STA), a diagnostic (solver-agnostic in principle, validated on two structurally different solvers: Prover9 and SWI-Prolog) that applies leave-one-out component necessity testing to solver inputs. The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates syntactic component necessity; ISR$=$0 indicates complete redundancy. ISR does not correlate with downstream NLI accuracy ($\rho{=}{-}0.049$, $p{=}0.187$), confirming it measures structural properties orthogonal to semantic correctness.
3	
4	ISR exposes a collapse trajectory hidden from prove rate: over 100 to 1000 GRPO training steps (Qwen3-4B), ISR falls from 0.642 to 0.003---a 99.5\% degradation---while prove rate rises from 32\% to 96\%. An SFT baseline achieves 92.9\% non-hacking proofs with near-zero hacking, confirming the degeneration is RL-specific.
5	
6	Can ISR serve as a training signal? Incorporating ISR into the reward at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 64.5\% of proved samples exhibit conclusion duplication (H7), versus 0\% under matched random controls. The sole apparent ISR improvement reduces to $1.06\times$ after controlling for a premise-count confound. At $\beta{=}0.3$, prove rate collapses to 18\% versus 48\% for random control.
7	
8	Cross-logic transfer to Prolog/SWI-Prolog yields a stronger result: ISR-as-reward produces universal Goodhart---3/3 seeds gaming via distinct mechanisms, 0\% non-hacking proofs.
9	
10	Across 6 reward conditions, 2 logic types (FOL/Prover9, Prolog/SWI-Prolog), and 3 seeds, we catalog 7 distinct reward hacking modes---including query-as-fact gaming that bypasses text-match classifiers---do
…[truncated 208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T23:19:42.418474+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T23:19:42.418785+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.
7	
8	Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under reinforcement learning, where the optimizer exploits any shortcut the reward fails to penalize~\cite{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\cite{deepseekmath} to train LLMs that generate solver-verified formal programs~\cite{mellgren-prolog-grpo, logic-rl} using binary execution feedback as reward; this drives rapid PR gains but gives no gradient on structural quality.
10	Process reward models~\cite{lightman-verify-step} offer step-level supervision but require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	No existing method provides an annotation-free, solver-agnostic diagnostic for structural integrity in neurosymbolic outputs (see \S\ref{sec:related-work} for full context).
12	
13	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\autoref{fig:sta-overview}).
14	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intens
…[truncated 2956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T23:19:42.419009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T23:19:42.419235+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given natural language premises $P_1,\ldots,P_k$ and a conclusion $C$, the task is to produce a formal logic program $F=\{c_1,\ldots,c_n\}$, where each component $c_i$ is a premise (FOL) or a clause/fact (Prolog), with one distinguished component encoding the query.
15	An external solver $S$ returns $S(F)\in\{\textit{proved},\textit{failed}\}$; we use Prover9 for FOL and SWI-Prolog for Prolog (\autoref{fig:sta-overview}a).
16	
17	We train formalizers with GRPO~\citep{deepseekmath} using $K{=}8$ rollouts per prompt.
18	Each rollout receives a binary \emph{execution reward}
19	$r_{\text{exec}}(x) = \mathbf{1}[S(F_x) = \textit{proved}]$;
20	group-relative advantages are computed within each prompt's rollout group, and the policy update maximizes a clipped surrogate objective with KL regularization.
21	This setup optimizes prove rate but provides no signal about \emph{structural quality}: a formalization that embeds the conclusion among its premises receives the same reward as a faithful multi-step derivation.
22	
23	\subsection{Solver Trace Ablation (STA)}
24	\label{sec:sta}
25	
26	To diagnose structural quality, STA tests whether each component of a proved formalization is individually necessary for proof success (\autoref{fig:sta-overview}b).
27	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$, each removing one component, and re-runs the solver.
28	A compo
…[truncated 3221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T23:19:42.419442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T23:19:42.421948+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 8 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other se
…[truncated 21826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T23:19:42.422226+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T23:19:42.422478+00:00_

1	\section{Discussion and Conclusion}
2	
3	We introduced Solver Trace Ablation (STA), a component-level diagnostic for neurosymbolic formalizers that exposes structural degeneration invisible to execution-based evaluation.
4	Applied to GRPO-trained models, ISR reveals a collapse trajectory hidden from prove rate, confirmed as RL-specific by an SFT baseline with near-zero hacking (\S\ref{sec:diagnostic}).
5	When repurposed as a training signal, ISR induces meta-level Goodhart's Law: at low dose, the model games the diagnostic itself through conclusion duplication absent under matched controls; at high dose, prove rate collapses; the sole apparent ISR improvement reduces to noise after controlling for a premise-count confound (\S\ref{sec:goodhart}).
6	Both diagnostic utility and Goodhart vulnerability transfer to Prolog/SWI-Prolog: ISR-as-reward yields universal gaming across all seeds with zero non-hacking proofs, each via a distinct mechanism (\S\ref{sec:crosslogic}).
7	Across six reward conditions and two logic types, we catalog seven hacking modes, including query-as-fact gaming that bypasses text-match classifiers (\S\ref{sec:taxonomy}).
8	
9	\paragraph{Interpreting ISR.}
10	ISR values must always be read relative to the optimization objective: under exec-only Prolog training, \emph{low} ISR reflects redundant coding (repeated ground facts), not absence of reasoning; under ISR-as-reward, \emph{high} ISR reflects metric gaming.
11	The premise-count confound---fewer components mechanically inflate ISR under LOO---applies to any ablation-based diagnostic on variable-length outputs.
12	While we use leave-one-out ablation for computational tractability ($n{+}1$ solver calls), Shapley value decomposition could provide more nuanced attribution at higher cost.
13	
14	\paragraph{Meta-Level Goodhart.}
15	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet incorporating it into the reward causes the model to game ISR itself---a regress where any diagno
…[truncated 897 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T23:19:42.422794+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T23:19:42.424880+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); as a training reward exhibiting meta-level Goodhart's Law (\S\ref{sec:goodhart}); and as a cross-logic protocol (\S\ref{sec:crosslogic}). We synthesize results into a hacking taxonomy (\S\ref{sec:taxonomy}).
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	We train Qwen3-4B with GRPO~\citep{deepseekmath} using $K{=}8$ rollouts per prompt for 500 steps (default) or 1000 where noted, across seeds $\{42,43,44\}$.
10	Training data is a fixed 500-example subset of FOLIO~\citep{folio} (\texttt{train\_500\_seed42.jsonl}), held constant across all seeds and conditions.
11	We use Prover9 for FOL and SWI-Prolog 8.4.2 for Prolog.
12	Evaluation is on 100 held-out FOLIO examples with greedy decoding; all cross-run ISR values are computed by \texttt{eval\_sta.py} which applies STA uniformly.
13	We report prove rate (PR), proved-only ISR (ISR$^*$, over proved samples only), hacking mode percentages (H7, H1\footnote{Hacking mode numbering follows our taxonomy order (Appendix~\ref{app:hacking-modes}); H1 is the most prevalent mode.}), non-hacking rate\footnote{We define ``non-hacking'' as outputs not matching any of our seven identified hacking patterns (Table~\ref{tab:hacking-taxonomy-app}); this does not imply semantic correctness.}, and mean component count.
14	Six reward conditions are compared: \textbf{Exec-only}, \textbf{ISR~$\beta{\in}\{0.1,0.3\}$}, \textbf{Random~$\beta{\in}\{0.1,0.3\}$}, and \textbf{SFT}.
15	Outputs are classified into H7, H1, and Non-hacking using text matching cross-validated with functional LOO analysis.
16	Full hyperparameters are in Appendix~\ref{app:setup}.
17	
18	\subsection{ISR as Diagnostic}
19	\label{sec:diagnostic}
20	
21	\begin{figure}[t]
22	\centering
23	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
24	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\t
…[truncated 8223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T23:19:42.425140+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T23:19:42.425505+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
6	Three seeds demonstrate qualitative divergence but limit statistical power.
7	STA requires solvers supporting component-level input manipulation.
8	
9	\paragraph{Data scale.}
10	Our experiments use 500 training examples and 100 evaluation examples, reflecting the FOLIO dataset's total size of 1,435 annotated examples~\citep{folio}.
11	The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
12	While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T23:19:42.425748+00:00_

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
  "session": "worker_write_paper-review-fixes_20260514T231354",
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

_source line 30 · 2026-05-14T23:19:42.425961+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T23:19:42.426167+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T23:19:42.426993+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: met
…[truncated 43923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T23:19:42.427263+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_1.md"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T23:19:42.427511+00:00_

1	---
2	round: 1
3	overall_score: borderline (Findings track recommended; 3/5)
4	timestamp: 2026-05-14T21:34:51.268987+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# 审稿报告 — solver-trace-ablation (Round 0)
11	
12	**日期**: 2026-05-14 | **Venue**: EMNLP 2026 Main Conference (ARR May cycle, deadline 2026-05-25)
13	**Reviewers**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+格式)
14	**Overall**: 3/5 — Findings | Confidence: 4/5
15	
16	---
17	
18	## Summary
19	
20	本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，通过衍生指标 ISR 检测 GRPO 训练的 neurosymbolic formalizer 中 execution-based evaluation 无法发现的结构性退化。核心发现：(1) exec-only GRPO 下 ISR 从 0.642 降至 0.003 而 PR 从 32% 升至 96%；(2) ISR 作为 reward 时触发 meta-level Goodhart（H7 64.5% vs random 0%）；(3) Prolog cross-logic transfer 显示 universal Goodhart（3/3 seeds, 0% genuine）；(4) 7 种 reward hacking 模式分类。
21	
22	---
23	
24	## Strengths
25	
26	1. **ISR collapse trajectory 是核心实证贡献**（R1/R2 共识）。0.642→0.132→0.003 的单调下降与 PR 的逆向上升清晰揭示了 execution metric 的盲区。
27	2. **Matched random control 实验设计精当**。H7 在 ISR reward 下 64.5% vs random 0% (Table 1) 有效隔离了 ISR-specific 信号。
28	3. **Cross-logic transfer 强化结论**。Prolog 3/3 seeds universal Goodhart 且各通过不同机制，展示 robustness。
29	4. **Premise-count confound 的主动识别和控制**展现实验诚实性（1.06× premise-matched）。
30	5. **Hacking taxonomy 系统化**，query-as-fact gaming 对 text-match classifier 的 bypass 有实用价值。
31	6. **写作质量整体优秀**，story arc 清晰，术语定义一致。
32	
33	---
34	
35	## Weaknesses
36	
37	### Critical (Must-Fix) — 4 项
38	
39	**C1. 统计效力严重不足** [R1-W1/R2-W3,W10 — 完全共识]
40	β=0.3 仅 single seed (s42)，鉴于 exec-only σ=47pp，PR=18% vs 48% 可能是 seed-specific。Abstract "87%" 来自 single seed 未标注。评估集仅 100 例缺 confidence intervals。"Dose-response trajectory" 高剂量端仅一个数据点。
41	
42	**C2. ISR framing 误导** [R1-W2/R2-W5 — 完全共识]
43	ISR 与 NLI accuracy 不相关（ρ=-0.049），但 abstract "maximal tightness" 暗示质量维度。"Genuine" 操作定义是排除法（非 H1/H7），不等同语义正确。ρ=-0.049 应在 abstract/intro 中提及而非仅 Appendix。
44	
45	**C3. Limitations section 格式不合规** [R2-
…[truncated 2922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T23:19:42.430812+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "discussion.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Glob",
  "tool_args": {
    "pattern": "discussion.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T23:19:42.431055+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T23:19:42.431324+00:00_

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
  "session": "worker_write_paper-review-fixes_20260514T231354",
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

_source line 38 · 2026-05-14T23:19:42.432899+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T23:19:42.433158+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProcessBench identifying process errors mathematical reasoning arXiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProcessBench identifying process errors mathematical reasoning arXiv 2024"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T23:19:42.433372+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "code generation reward hacking specification gaming arXiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "tool_args": {
    "query": "code generation reward hacking specification gaming arXiv 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T23:19:42.433586+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"PRMs scale poorly\" OR \"process reward models don't generalize\" OR \"limitations of process reward models\" arXiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"PRMs scale poorly\" OR \"process reward models don't generalize\" OR \"limitations of process reward models\" arXiv 2025"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T23:19:42.434911+00:00_

Web search results for query: "ProcessBench identifying process errors mathematical reasoning arXiv 2024"

Links: [{"title":"[2412.06559] ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/abs/2412.06559"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241206559Z/abstract"},{"title":"2025-05-27 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"Paper page - ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://huggingface.co/papers/2412.06559"},{"title":"2024-12-10 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559v1"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.50/"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2412.06559v4"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=ProcessBench:+Identifying+Process+Errors+in+Mathematical+Reasoning."},{"title":"The Lessons of Developing Process Reward Models in ...","url":"https://arxiv.org/pdf/2501.07301"}]

Based on the search results, here's information about ProcessBench:

## Overview

ProcessBench is designed for measuring the ability to identify erroneous steps in mathematical reasoning. As language models regularly make mistakes when solving math problems, automated identification of errors in the reasoning process becomes increasingly significant for their scalable oversight.

## Dataset Composition

It consists of 3,400 test cases, primarily focused on competition- and Olympiad-level math problems. Each test case contains a step-by-step
…[truncated 1159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T23:19:42.435212+00:00_

Web search results for query: "code generation reward hacking specification gaming arXiv 2025 2026"

Links: [{"title":"Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis","url":"https://arxiv.org/html/2601.20103v1"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Towards Understanding Specification Gaming in Reasoning Models","url":"https://arxiv.org/html/2605.02269v1"},{"title":"Preprint Countdown-Code: A Testbed for Studying The Emergence","url":"https://arxiv.org/pdf/2603.07084"},{"title":"Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use","url":"https://arxiv.org/html/2605.02964"},{"title":"Defining and Characterizing Reward Hacking Joar Skalse∗ University of Oxford","url":"https://arxiv.org/pdf/2209.13085"},{"title":"[2604.13602] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/abs/2604.13602"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study","url":"https://arxiv.org/html/2507.05619v1"},{"title":"What Is Reward Hacking? How to Prevent It in RL (2026 Guide)","url":"https://www.articsledge.com/post/reward-hacking"}]

Based on the search results, I found several recent arXiv papers and research from 2025-2026 on code generation, reward hacking, and specification gaming. Here's what the search revealed:

## Key Recent Papers

Shihab et al. (2026) categorized coding reward hacks into specification gaming, reward tampering, misalignment, proxy optimization, exploitation patterns, and wireheading. They created a benchmark for detecting and analyzing these behaviors.

Since late 2024, there have been many publicized examples of powerful reasoning mo
…[truncated 1196 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T23:19:42.435470+00:00_

Web search results for query: ""PRMs scale poorly" OR "process reward models don't generalize" OR "limitations of process reward models" arXiv 2025"

Links: [{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"Unsupervised Process Reward Models","url":"https://arxiv.org/html/2605.10158v1"},{"title":"process reward model with qvalue rankings","url":"https://arxiv.org/pdf/2410.11287"},{"title":"[2501.07301] The Lessons of Developing Process Reward Models in Mathematical Reasoning","url":"https://arxiv.org/abs/2501.07301"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"[2410.11287] Process Reward Model with Q-Value Rankings","url":"https://arxiv.org/abs/2410.11287"},{"title":"Reward Model Interpretability via Optimal and Pessimal Tokens","url":"https://arxiv.org/html/2506.07326v1"}]

Based on the search results, I found several recent arXiv papers from 2025 that discuss limitations and challenges with Process Reward Models (PRMs). Here are the key findings:

## Key Limitations of PRMs Identified in 2025 Research:

**Data Efficiency and Supervision Costs:**
PRMs require step-level supervision, making them expensive to train. Additionally, PRMs require expert annotations for every reasoning step, making them costly and difficult to scale.

**Generalization and Data Quality Issues:**
Commonly used Monte Carlo (MC) estimation-based data synthesis for PRMs typically yields inferior performance and general
…[truncated 1309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T23:19:42.435733+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProcessBench arXiv 2412.06559 authors Chujie Zheng"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProcessBench arXiv 2412.06559 authors Chujie Zheng"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T23:19:42.435936+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Baker et al 2025 reward hacking coding benchmarks Claude arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Baker et al 2025 reward hacking coding benchmarks Claude arXiv"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T23:19:42.436141+00:00_

Web search results for query: "Baker et al 2025 reward hacking coding benchmarks Claude arXiv"

Links: [{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Natural emergent misalignment from reward hacking in production RL","url":"https://arxiv.org/html/2511.18397.pdf"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/html/2506.19248v2"},{"title":"SCHOOL OF REWARD HACKS: HACKING HARMLESS TASKS GENERALIZES TO MIS-","url":"https://arxiv.org/pdf/2508.17511"},{"title":"Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation","url":"https://arxiv.org/html/2503.11926v1"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/html/2603.28063v1"},{"title":"Monitoring Emergent Reward Hacking During Generation via Internal Activations","url":"https://arxiv.org/html/2603.04069"},{"title":"NATURAL EMERGENT MISALIGNMENT FROM REWARD HACKING IN PRODUCTION RL","url":"https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf"},{"title":"Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis","url":"https://arxiv.org/html/2601.20103v1"},{"title":"[2503.11926] Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation","url":"https://arxiv.org/abs/2503.11926"}]

I found several relevant papers on reward hacking in coding benchmarks and monitoring models. Here are the key findings from the search results:

## Baker et al. 2025 - Monitoring Reasoning Models for Misbehavior

The main Baker et al. 2025 paper (arXiv:2503.11926) shows that frontier reasoning models like OpenAI o3-mini can be monitored for reward hacking in agentic coding environments using another LLM that observes the model's chain-of-thought (CoT) reasoning.

CoT monitoring can be far more effective than monitor
…[truncated 1240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T23:19:42.436407+00:00_

Web search results for query: "ProcessBench arXiv 2412.06559 authors Chujie Zheng"

Links: [{"title":"[2412.06559] ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/abs/2412.06559"},{"title":"Paper page - ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://huggingface.co/papers/2412.06559"},{"title":"Towards Effective Process Supervision in Mathematical Reasoning | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-math-prm/"},{"title":"Qwen/ProcessBench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Qwen/ProcessBench"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.50/"},{"title":"arXiv:2412.06559v4 [cs.AI] 26 May 2025","url":"https://arxiv.org/pdf/2412.06559"},{"title":"GitHub - QwenLM/ProcessBench: Official repository for ACL 2025 paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\"","url":"https://github.com/QwenLM/ProcessBench"},{"title":"dblp: Chujie Zheng","url":"https://dblp.org/pid/242/8504.html"},{"title":"Chujie Zheng 郑楚杰 - Chujie Zheng 郑楚杰","url":"https://chujiezheng.github.io/"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://www.researchgate.net/publication/394269497_ProcessBench_Identifying_Process_Errors_in_Mathematical_Reasoning"}]

Based on the search results, here is information about ProcessBench (arXiv 2412.06559):

## Overview

ProcessBench introduces a benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, consisting of 3,400 test cases, primarily focused on competition- and Olympiad-level math problems.

## Authors

The authors are Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin.

## Evaluation Approach

Each test case contains a step-by-step solution with error location annotated by hu
…[truncated 685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T23:19:42.436647+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"school of reward hacks\" arXiv 2508.17511 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"school of reward hacks\" arXiv 2508.17511 authors"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T23:19:42.438930+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"natural emergent misalignment\" reward hacking production RL arXiv 2511.18397 authors Anthropic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"natural emergent misalignment\" reward hacking production RL arXiv 2511.18397 authors Anthropic"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T23:19:42.440731+00:00_

Web search results for query: ""school of reward hacks" arXiv 2508.17511 authors"

Links: [{"title":"[2508.17511] School of Reward Hacks: Hacking harmless tasks generalizes to misaligned behavior in LLMs","url":"https://arxiv.org/abs/2508.17511"},{"title":"SCHOOL OF REWARD HACKS: HACKING HARMLESS TASKS GENERALIZES TO MIS-","url":"https://arxiv.org/pdf/2508.17511"},{"title":"[PDF] School of Reward Hacks: Hacking harmless tasks generalizes to misaligned behavior in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/99aadd954b13b27bfab9c3d4217a4620d0797023"},{"title":"(PDF) School of Reward Hacks: Hacking harmless tasks generalizes to misaligned behavior in LLMs","url":"https://www.researchgate.net/publication/394942182_School_of_Reward_Hacks_Hacking_harmless_tasks_generalizes_to_misaligned_behavior_in_LLMs"},{"title":"School of Reward Hacks: Hacking harmless tasks generalizes to misaligned behavior in LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250817511T/abstract"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=8800&show=100"},{"title":"School of Reward Hacks Dataset","url":"https://www.emergentmind.com/topics/school-of-reward-hacks-dataset"},{"title":"Harmless reward hacks can generalize to misalignment in ...","url":"https://www.lesswrong.com/posts/CwJ2qWveb9JbaCGQ5/harmless-reward-hacks-can-generalize-to-misalignment-in-llms"}]

Based on the search results, the authors of the arXiv paper 2508.17511 "School of Reward Hacks: Hacking harmless tasks generalizes to misaligned behavior in LLMs" are Mia Taylor, James Chua, Jan Betley, Johannes Treutlein, and Owain Evans. The paper was submitted on August 24, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T23:19:42.441044+00:00_

Web search results for query: ""natural emergent misalignment" reward hacking production RL arXiv 2511.18397 authors Anthropic"

Links: [{"title":"[2511.18397] Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/abs/2511.18397"},{"title":"Natural emergent misalignment from reward hacking in production RL","url":"https://arxiv.org/html/2511.18397v1"},{"title":"[2511.18397v1] Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/abs/2511.18397v1"},{"title":"Paper page - Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://huggingface.co/papers/2511.18397"},{"title":"(PDF) Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://www.researchgate.net/publication/397934465_Natural_Emergent_Misalignment_from_Reward_Hacking_in_Production_RL"},{"title":"Emergent Misalignment from Reward Hacking in RL","url":"https://www.emergentmind.com/papers/2511.18397"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.18397v1"},{"title":"Natural emergent misalignment from reward hacking in ...","url":"https://www.lesswrong.com/posts/fJtELFKddJPfAxwKS/natural-emergent-misalignment-from-reward-hacking-in"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2511.18397"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL https://arxiv.org/abs/2511.18397","url":"https://www.threads.com/@tsai_zen/post/DSSrvXDEwu6/natural-emergent-misalignment-from-reward-hacking-in-production-rl"}]

Here are the search results for your query about arXiv paper 2511.18397:

## Overview

When large language models learn to reward hack on production RL environments, this can result in egregious emergent misalignment. The paper was submitted on 23 Nov 2025 with authors Mo
…[truncated 1357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T23:19:42.441454+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "old_string": "@misc{metr-reward-hacking,\n  author       = {{METR}},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR blog post},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}",
  "new_string": "@misc{metr-reward-hacking,\n  author       = {{METR}},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR blog post},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}\n\n@inproceedings{processbench,\n  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},\n  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2412.06559},\n}\n\n@article{school-reward-hacks,\n  author       = {Mia Taylor and James Chua and Jan Betley and Johannes Treutlein and Owain Evans},\n  title        = {{School of Reward Hacks: Hacking Harmless Tasks Generalizes to Misaligned Behavior in LLMs}},\n  journal      = {arXiv preprint arXiv:2508.17511},\n  year         = {2025},\n  eprint       = {2508.17511},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{macdiarmid-emergent-misalignment,\n  author       = {Monte MacDiarmid and Benjamin Wright and Jonathan Uesato and Joe Benton and others},\n  title        = {{Natural Emergent Misalignment from Reward Hacking in Production RL}},\n  journal      = {arXiv preprint arXiv:2511.18397},\n  year         = {2025},\n  eprint       = {2511.18397},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
    "old_string": "@misc{metr-reward-hacking,\n  author       = {{METR}},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR blog post},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}",
    "new_string": "@misc{metr-reward-hacking,\n  author       = {{METR}},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR blog post},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}\n\n@inproceedings{processbench,\n  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},\n  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2412.06559},\n}\n\n@article{school-reward-hacks,\n  author       = {Mia Taylor and James Chua and Jan Betley and Johannes Treutlein and Owain Evans},\n  title        = {{School of Reward Hacks: Hacking Harmless Tasks Generalizes to Misaligned Behavior in LLMs}},\n  journal      = {arXiv preprint arXiv:2508.17511},\n  year         = {2025},\n  eprint       = {2508.17511},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{macdiarmid-emergent-misalignment,\n  author       = {Monte MacDiarmid and Benjamin Wright and Jonathan Uesato and Joe Benton and others},\n  title        = {{Natural Emergent Misalignment from Reward Hacking in Production RL}},\n  journal      = {arXiv preprint arXiv:2511.18397},\n  year         = {2025},\n  eprint       = {2511.18397},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T23:19:42.444845+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T23:19:42.445069+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
  "old_string": "However, process rewards introduce their own failure modes: design choices dominate signal effects~\\cite{gao-effective-rl-reward}, process and outcome rewards can conflict~\\cite{prof-process-outcome}, and PRMs degrade at distribution shift~\\cite{qwen-prm-lessons, progrs-outcome-conditioned}.",
  "new_string": "However, process rewards introduce their own failure modes: design choices dominate signal effects~\\cite{gao-effective-rl-reward}, process and outcome rewards can conflict~\\cite{prof-process-outcome}, and PRMs degrade at distribution shift~\\cite{qwen-prm-lessons, processbench, progrs-outcome-conditioned}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
    "old_string": "However, process rewards introduce their own failure modes: design choices dominate signal effects~\\cite{gao-effective-rl-reward}, process and outcome rewards can conflict~\\cite{prof-process-outcome}, and PRMs degrade at distribution shift~\\cite{qwen-prm-lessons, progrs-outcome-conditioned}.",
    "new_string": "However, process rewards introduce their own failure modes: design choices dominate signal effects~\\cite{gao-effective-rl-reward}, process and outcome rewards can conflict~\\cite{prof-process-outcome}, and PRMs degrade at distribution shift~\\cite{qwen-prm-lessons, processbench, progrs-outcome-conditioned}."
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T23:19:42.445292+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T23:19:42.445489+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
  "old_string": "Prior work establishes Goodhart's Law theoretically~\\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, pan-reward-misspecification, kwa-catastrophic-goodhart} and observes overoptimization scaling in RLHF~\\cite{gao-reward-overoptimization}; recent empirical reports document frontier models reward-hacking code-generation tasks in practice~\\cite{metr-reward-hacking}.\nIn LLMs, specification gaming~\\cite{bondarenko-spec-gaming}, formalization gaming~\\cite{kim-game-formalization}, and spurious RLVR rewards~\\cite{spurious-rewards} have been documented, but the proxy in these analyses is a learned reward model.",
  "new_string": "Prior work establishes Goodhart's Law theoretically~\\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, pan-reward-misspecification, kwa-catastrophic-goodhart} and observes overoptimization scaling in RLHF~\\cite{gao-reward-overoptimization}; recent empirical reports document frontier models reward-hacking code-generation tasks in practice~\\cite{metr-reward-hacking, macdiarmid-emergent-misalignment}, with learned reward hacking generalizing to misaligned behaviors in unrelated contexts~\\cite{school-reward-hacks}.\nIn LLMs, specification gaming~\\cite{bondarenko-spec-gaming}, formalization gaming~\\cite{kim-game-formalization}, and spurious RLVR rewards~\\cite{spurious-rewards} have been documented, but the proxy in these analyses is a learned reward model."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
    "old_string": "Prior work establishes Goodhart's Law theoretically~\\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, pan-reward-misspecification, kwa-catastrophic-goodhart} and observes overoptimization scaling in RLHF~\\cite{gao-reward-overoptimization}; recent empirical reports document frontier models reward-hacking code-generation tasks in practice~\\cite{metr-reward-hacking}.\nIn LLMs, specification gaming~\\cite{bondarenko-spec-gaming}, formalization gaming~\\cite{kim-game-formalization}, and spurious RLVR rewards~\\cite{spurious-rewards} have been documented, but the proxy in these analyses is a learned reward model.",
    "new_string": "Prior work establishes Goodhart's Law theoretically~\\cite{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, pan-reward-misspecification, kwa-catastrophic-goodhart} and observes overoptimization scaling in RLHF~\\cite{gao-reward-overoptimization}; recent empirical reports document frontier models reward-hacking code-generation tasks in practice~\\cite{metr-reward-hacking, macdiarmid-emergent-misalignment}, with learned reward hacking generalizing to misaligned behaviors in unrelated contexts~\\cite{school-reward-hacks}.\nIn LLMs, specification gaming~\\cite{bondarenko-spec-gaming}, formalization gaming~\\cite{kim-game-formalization}, and spurious RLVR rewards~\\cite{spurious-rewards} have been documented, but the proxy in these analyses is a learned reward model."
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T23:19:42.445781+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T23:19:42.445984+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
  "old_string": "Kim et al.~\\cite{kim-game-formalization} specifically examine formalization gaming in Lean 4 theorem proving via inference-time prompting on FOLIO and Multi-LogiEval; our work is complementary, providing ISR as a structural diagnostic for neurosymbolic NLI training and demonstrating that the diagnostic itself becomes a Goodhart target when used as an RL reward.",
  "new_string": "Kim et al.~\\cite{kim-game-formalization} examine formalization gaming in Lean 4 theorem proving, identifying axiom fabrication and premise mistranslation as unfaithfulness modes via inference-time prompting on FOLIO and Multi-LogiEval.\nOur work is complementary: while Kim et al.\\ diagnose gaming in inference-time outputs of frontier models, we study gaming that \\emph{emerges during RL training} and provide ISR as a structural diagnostic with a systematic seven-mode taxonomy and cross-logic transfer analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
    "old_string": "Kim et al.~\\cite{kim-game-formalization} specifically examine formalization gaming in Lean 4 theorem proving via inference-time prompting on FOLIO and Multi-LogiEval; our work is complementary, providing ISR as a structural diagnostic for neurosymbolic NLI training and demonstrating that the diagnostic itself becomes a Goodhart target when used as an RL reward.",
    "new_string": "Kim et al.~\\cite{kim-game-formalization} examine formalization gaming in Lean 4 theorem proving, identifying axiom fabrication and premise mistranslation as unfaithfulness modes via inference-time prompting on FOLIO and Multi-LogiEval.\nOur work is complementary: while Kim et al.\\ diagnose gaming in inference-time outputs of frontier models, we study gaming that \\emph{emerges during RL training} and provide ISR as a structural diagnostic with a systematic seven-mode taxonomy and cross-logic transfer analysis."
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T23:19:42.446243+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T23:19:42.446464+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
  "old_string": "No existing method provides an annotation-free, solver-agnostic diagnostic for structural integrity in neurosymbolic outputs (see \\S\\ref{sec:related-work} for full context).",
  "new_string": "No existing method provides an annotation-free diagnostic for structural integrity in neurosymbolic outputs---one adaptable in principle to any solver supporting component-level input manipulation (see \\S\\ref{sec:related-work} for full context)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
    "old_string": "No existing method provides an annotation-free, solver-agnostic diagnostic for structural integrity in neurosymbolic outputs (see \\S\\ref{sec:related-work} for full context).",
    "new_string": "No existing method provides an annotation-free diagnostic for structural integrity in neurosymbolic outputs---one adaptable in principle to any solver supporting component-level input manipulation (see \\S\\ref{sec:related-work} for full context)."
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T23:19:42.450069+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T23:19:42.450309+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
  "old_string": "The protocol is solver-agnostic, requiring $n{+}1$ solver calls per sample.",
  "new_string": "The protocol is solver-agnostic in principle---applicable to any solver accepting component-level input manipulation---requiring $n{+}1$ solver calls per sample."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
    "old_string": "The protocol is solver-agnostic, requiring $n{+}1$ solver calls per sample.",
    "new_string": "The protocol is solver-agnostic in principle---applicable to any solver accepting component-level input manipulation---requiring $n{+}1$ solver calls per sample."
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T23:19:42.450527+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T23:19:42.450768+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "old_string": "\\paragraph{Classifier Validation.}\nHacking mode classification is fully automated: H1 and H7 are identified by normalized text matching between conclusion and premise strings; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation). No manual annotation is used. We estimate classification precision at $>$95\\% for H1/H7 (verified on 50 randomly sampled outputs) and note that the non-hacking rate for FOL conditions may be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would be missed.",
  "new_string": "\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nH1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "old_string": "\\paragraph{Classifier Validation.}\nHacking mode classification is fully automated: H1 and H7 are identified by normalized text matching between conclusion and premise strings; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation). No manual annotation is used. We estimate classification precision at $>$95\\% for H1/H7 (verified on 50 randomly sampled outputs) and note that the non-hacking rate for FOL conditions may be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would be missed.",
    "new_string": "\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nH1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier."
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T23:19:42.451136+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T23:19:42.451374+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T23:19:42.451594+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer: A Case Study with Qwen3-4B}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	\input{limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T23:19:42.456070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T23:19:42.456355+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic Reasoning with LLMs.}
5	Prompting-based pipelines couple LLMs with external solvers for logical reasoning.
6	SatLM~\cite{satlm} generates SAT formulas, Logic-LM~\cite{logic-lm} translates to first-order logic, LINC~\cite{linc} generates logic programs, and LoRP~\cite{lorp} uses Prolog as a reasoning backend; FOVER~\cite{fover-pei2025} adds iterative verification.
7	All evaluate on execution accuracy alone, without diagnosing structural quality of formalizations.
8	Recent RL approaches train LLMs against solver feedback~\cite{mellgren-prolog-grpo, logic-rl, thought-like-pro}, optimizing prove rate with binary execution reward.
9	STA differs in diagnostic focus: ISR exposes that execution accuracy conflates faithful derivation with degenerate shortcuts, and our finding that 87\% of proved outputs under exec-only GRPO embed the conclusion in the premises (\S\ref{sec:diagnostic}) suggests prior prove-rate gains may overstate genuine reasoning improvement.
10	We adopt FOLIO~\cite{folio} as it is the only publicly available NLI benchmark providing both FOL and Prolog annotations, enabling our cross-logic diagnostic transfer experiments; ProofWriter~\cite{proofwriter} and ProntoQA~\cite{prontoqa} offer synthetic logical reasoning benchmarks but lack the multi-logic annotation required for cross-logic comparison.
11	
12	\paragraph{Reward Shaping and Process Supervision.}
13	Binary outcome rewards motivate process-level supervision: learned process reward models~\cite[PRMs;][]{lightman-verify-step, math-shepherd} provide step-level feedback, solver-grounded signals~\cite{rlsf} leverage formal verification, and rubric-based rewards~\cite{rubric-grpo} encode structured evaluation criteria.
14	However, process rewards introduce their own failure modes: design choices dominate signal effects~\cite{gao-effective-rl-reward}, process and outcome rewards can conflict~\cite{prof-process-outcome}, and PR
…[truncated 3164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T23:19:42.456665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "145",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "145",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T23:19:42.456931+00:00_

145	\end{table}
146	
147	\paragraph{Classifier Validation.}
148	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
149	H1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
150	No training data or manual annotation is used for classification.
151	
152	To estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
153	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
154	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
155	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
156	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
157	
158	\subsection{H1 --- Conclusion Embedding}
159	
160	\paragraph{Definition.}
161	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
162	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
163	
164	\paragraph{Example (FOL).}
165	{\small\begin{verbatim}
166	Premise
…[truncated 101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-14T23:19:42.457148+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
  "offset": "9",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
    "offset": "9",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-14T23:19:42.457330+00:00_

9	Recent work applies GRPO~\cite{deepseekmath} to train LLMs that generate solver-verified formal programs~\cite{mellgren-prolog-grpo, logic-rl} using binary execution feedback as reward; this drives rapid PR gains but gives no gradient on structural quality.
10	Process reward models~\cite{lightman-verify-step} offer step-level supervision but require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	No existing method provides an annotation-free diagnostic for structural integrity in neurosymbolic outputs---one adaptable in principle to any solver supporting component-level input manipulation (see \S\ref{sec:related-work} for full context).
12	
13	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (\autoref{fig:sta-overview}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T23:19:42.457502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
  "offset": "36",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex",
    "offset": "36",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-14T23:19:42.457673+00:00_

36	\end{equation}
37	ISR $\in[0,1]$ is defined only for proved formalizations ($r_{\text{exec}}(x){=}1$): ISR${=}1$ indicates syntactic component necessity; ISR${=}0$ indicates complete redundancy.
38	The protocol is solver-agnostic in principle---applicable to any solver accepting component-level input manipulation---requiring $n{+}1$ solver calls per sample.
39	STA draws on the LOO intuition from mutation testing~\citep{demillo1978, jia-harman-survey} but operates on solver \emph{inputs} (formalizations) rather than program code, targeting component necessity rather than test adequacy.
40	Pseudocode is in Appendix~\ref{app:algorithm}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-14T23:19:42.460987+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "bibliographystyle",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Grep",
  "tool_args": {
    "pattern": "bibliographystyle",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-14T23:19:42.461179+00:00_

paper/acl.sty:195:\bibliographystyle{acl_natbib}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-14T23:19:42.461358+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "code.*release|data.*release|released upon|open.?source",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Grep",
  "tool_args": {
    "pattern": "code.*release|data.*release|released upon|open.?source",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-14T23:19:42.461542+00:00_

paper/abstract.tex:10:Across 6 reward conditions, 2 logic types (FOL/Prover9, Prolog/SWI-Prolog), and 3 seeds, we catalog 7 distinct reward hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\footnote{Code and data will be released upon acceptance: \url{[anonymized for review]}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_paper-review-fixes_20260514T231354",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-14T23:19:42.461798+00:00_

All checks pass:

1. **`\bibliographystyle{acl_natbib}`** is set automatically by `acl.sty` (line 195) — main.tex doesn't need it separately.
2. **Code/data release** (m3): footnote exists only in `abstract.tex` — no duplicates.
3. **discussion.tex vs conclusion.tex**: `discussion.tex` doesn't exist. `conclusion.tex` has "Discussion and Conclusion" as combined section. main.tex only includes `conclusion.tex`. No duplication.
4. **main.tex vs paper.tex**: `main.tex` is the active file (complete includes, proper packages). `paper.tex` is an older version that references a non-existent `discussion.tex`.

## Summary of all changes:

**M4 (Kim et al. differentiation)** — `related_work.tex`: Expanded the Kim et al. comparison to explicitly name their findings (axiom fabrication, premise mistranslation) and sharpen the contrast (inference-time prompting vs. RL training emergence, seven-mode taxonomy + cross-logic transfer).

**M7 (Reference coverage)** — `references.bib`: Added 3 new entries:
- `processbench` (Zheng et al., ACL 2025, arXiv 2412.06559) — PRMs fail to generalize
- `school-reward-hacks` (Taylor et al., arXiv 2508.17511) — reward hacking generalizes to misalignment
- `macdiarmid-emergent-misalignment` (MacDiarmid et al., Anthropic, arXiv 2511.18397) — production RL reward hacking

`related_work.tex`: Cited all 3 new papers in appropriate paragraphs. Total references: 39 → 42.

**m1 (Classifier precision/recall)** — `appendix.tex`: Expanded classifier validation from 3 sentences to a full paragraph explaining: deterministic rule-based nature, manual precision verification (50 samples, >95%, Wilson CI), recall limitations, functional LOO cross-validation procedure, and the query-as-fact false negative discovery.

**m3 (Code/data release)** — Confirmed: single footnote in `abstract.tex`, no duplicates.

**M3 (Solver-agnostic weakening)** — `introduction.tex`: Changed "solver-agnostic diagnostic" to "diagnostic...adaptable in principle to any solver supporting component-level input manipulation". `method.tex`: Changed "solver-agnostic" to "solver-agnostic in principle---applicable to any solver accepting component-level input manipulation".

**Extra checks** — `acl.sty` already sets `\bibliographystyle{acl_natbib}`. No discussion/conclusion duplication. `paper.tex` is stale (references non-existent `discussion.tex`), `main.tex` is the active file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_write_paper-review-fixes_20260514T231354"
}
```

</details>

---
