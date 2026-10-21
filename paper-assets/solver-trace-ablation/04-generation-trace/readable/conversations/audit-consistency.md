# audit consistency

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_audit_consistency_20260515T212538.jsonl`
- **Structured JSON:** [`0c9324e99b5888ef7cae.json`](../../sessions/0c/0c9324e99b5888ef7cae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

16 recorded events

### Tool call

_source line 1 · 2026-05-15T21:28:24.265902+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__check_paper_consistency",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__check_paper_consistency",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T21:28:24.266424+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T21:28:24.266692+00:00_

called mcp__agent-ml-research__check_paper_consistency

<details open><summary>🔧 Tool call — mcp__agent-ml-research__check_paper_consistency</summary>

```json
{
  "project": "solver-trace-ablation",
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "mcp__agent-ml-research__check_paper_consistency",
  "tool_args": {
    "project": "solver-trace-ablation",
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T21:28:24.273243+00:00_

{"result":"{\"success\": true, \"data\": {\"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper\", \"sections\": [{\"file\": \"abstract.tex\", \"role\": \"headline\", \"num_numbers\": 10, \"num_cites\": 0}, {\"file\": \"conclusion.tex\", \"role\": \"headline\", \"num_numbers\": 24, \"num_cites\": 0}, {\"file\": \"experiments.tex\", \"role\": \"result\", \"num_numbers\": 96, \"num_cites\": 5}, {\"file\": \"introduction.tex\", \"role\": \"intro\", \"num_numbers\": 16, \"num_cites\": 18}, {\"file\": \"limitations.tex\", \"role\": \"other\", \"num_numbers\": 2, \"num_cites\": 1}, {\"file\": \"method.tex\", \"role\": \"other\", \"num_numbers\": 6, \"num_cites\": 3}, {\"file\": \"related_work.tex\", \"role\": \"other\", \"num_numbers\": 0, \"num_cites\": 26}], \"critical\": [], \"warning\": [], \"info\": [{\"kind\": \"notation_per_section\", \"message\": \"Inline math symbols collected per section.\", \"data\": {\"abstract\": [\"\\\\beta\", \"\\\\cdot\", \"\\\\pm\", \"\\\\rho\", \"\\\\sim\", \"\\\\times\", \"\\\\to\"], \"conclusion\": [\"\\\\approx\", \"\\\\beta\", \"\\\\geq\", \"\\\\pm\", \"\\\\times\", \"\\\\to\"], \"experiments\": [\"\\\\P\", \"\\\\S\", \"\\\\approx\", \"\\\\beta\", \"\\\\boldsymbol\", \"\\\\cdot\", \"\\\\dagger\", \"\\\\ddagger\", \"\\\\geq\", \"\\\\leq\", \"\\\\pm\", \"\\\\sharp\", \"\\\\sigma\", \"\\\\sim\", \"\\\\times\", \"\\\\to\", \"\\\\uparrow\"], \"introduction\": [\"\\\\beta\", \"\\\\cdot\", \"\\\\pm\", \"\\\\rho\", \"\\\\sigma\", \"\\\\sim\", \"\\\\times\", \"\\\\to\"], \"limitations\": [\"\\\\rho\"], \"method\": [\"\\\\alpha\", \"\\\\beta\", \"\\\\cdot\", \"\\\\geq\", \"\\\\gets\", \"\\\\in\", \"\\\\ldots\", \"\\\\setminus\", \"\\\\sim\", \"\\\\textit\", \"\\\\to\"]}}], \"summary\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "mcp__agent-ml-research__check_paper_consistency",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T21:28:24.273532+00:00_

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
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T21:28:24.274009+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
10	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
11	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary but not sufficient condition for semantic correctness.
12	
13	\subsection{ISR as Diagnostic}
14	\label{sec:diagnostic}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
19	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples hav
…[truncated 18025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T21:28:24.274311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/gen_fig3.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/gen_fig3.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T21:28:24.274609+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import numpy as np
5	
6	plt.rcParams.update({'pdf.fonttype': 42, 'ps.fonttype': 42})
7	
8	C_H7a = '#D55E00'
9	C_H7b = '#CC79A7'
10	C_H1 = '#E69F00'
11	C_H8 = '#56B4E9'
12	C_GENUINE = '#009E73'
13	
14	conditions = [
15	    'ISR $\\beta$=0.3',
16	    'ISR $\\beta$=0.1',
17	    'Random $\\beta$=0.3',
18	    'Random $\\beta$=0.1',
19	    'Exec-only',
20	    'SFT',
21	]
22	
23	# Order: ISR b0.3, ISR b0.1, Random b0.3, Random b0.1, Exec-only, SFT
24	raw = {
25	    'h7a':     [99, 161,  11,  36,   0,  0],
26	    'h7b':     [ 0,   2,   0,   0,   0,  0],
27	    'h1':      [73,  42, 149, 187,  81,  3],
28	    'h8':      [ 3,  12,   0,  14,   5,  0],
29	    'genuine': [24,  14,   3,  25,   7, 36],
30	}
31	
32	totals = [sum(raw[k][i] for k in raw) for i in range(len(conditions))]
33	# Verify: [199, 231, 163, 262, 93, 39]
34	
35	h7a     = [raw['h7a'][i]     / totals[i] * 100 for i in range(len(conditions))]
36	h7b     = [raw['h7b'][i]     / totals[i] * 100 for i in range(len(conditions))]
37	h1      = [raw['h1'][i]      / totals[i] * 100 for i in range(len(conditions))]
38	h8      = [raw['h8'][i]      / totals[i] * 100 for i in range(len(conditions))]
39	genuine = [raw['genuine'][i] / totals[i] * 100 for i in range(len(conditions))]
40	
41	y = np.arange(len(conditions))
42	bar_h = 0.55
43	
44	fig, ax = plt.subplots(figsize=(8, 4))
45	
46	kw = dict(height=bar_h, edgecolor='white', linewidth=0.5, zorder=3)
47	
48	left = np.zeros(len(conditions))
49	ax.barh(y, h7a, left=left, color=C_H7a, label='H7a (tautological)', **kw)
50	left += h7a
51	ax.barh(y, h7b, left=left, color=C_H7b, label='H7b (ISR-specific)', **kw)
52	left += h7b
53	ax.barh(y, h1, left=left, color=C_H1, label='H1 (shortcut)', **kw)
54	left += h1
55	ax.barh(y, h8, left=left, color=C_H8, label='H8 (conjunction)', **kw)
56	left += h8
57	ax.barh(y, genuine, left=left, color=C_GENUINE, label='Genuine', **kw)
58	left += genuine
59	
60	for i in r
…[truncated 1396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T21:28:24.278997+00:00_

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
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T21:28:24.279280+00:00_

1	\begin{abstract}
2	GRPO-trained neurosymbolic formalizers achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
4	The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.
5	ISR is uncorrelated with downstream NLI accuracy ($\rho{=}{-}0.049$), confirming it measures structural---not semantic---integrity.
6	As a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\to}0.003$ while PR rises $32\%{\to}96\%$; an SFT baseline reaches 92.3\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.
7	As a reward, $r = r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 70.6\% conclusion duplication (H7) versus 13.7\% under matched random (Fisher $p{=}1.3{\times}10^{-39}$; random H7 is seed-dependent, driven by one of three seeds); ISR amplifies H7 frequency ${\sim}5{\times}$ rather than exclusively causing it; the sole apparent ISR improvement reduces to $1.06\times$ after controlling for a premise-count confound; $\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\pm}42\%$; random: $54{\pm}35\%$), with individual seeds collapsing to as low as $18\%$.
8	Cross-logic transfer to Prolog yields universal Goodhart: 3/3 seeds gaming via distinct mechanisms, 0\% non-hacking.
9	Across 6 reward conditions, 2 logic types, 3 seeds, we catalog 8 hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\footnote{Code and da
…[truncated 45 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T21:28:24.279550+00:00_

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
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T21:28:24.279867+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\ref{fig:sta-overview}).
16	For each proved formalization, STA removes each component individually and re-runs the solv
…[truncated 3431 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T21:28:24.280146+00:00_

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
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T21:28:24.280425+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	Solver Trace Ablation (STA) exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides; an SFT baseline with 92.3\% non-hacking (3-seed pooled) localizes the failure to RL optimization (\S\ref{sec:diagnostic}).
5	Repurposed as a training signal, ISR induces meta-level Goodhart's Law: the diagnostic for gaming becomes itself the target of gaming.
6	At $\beta{=}0.1$, conclusion duplication exploits the LOO definition (70.6\% vs.\ 13.7\% under matched random (Fisher $p{<}10^{-38}$); random H7 is seed-dependent (38.3\% in one seed, 0\% in two others), so ISR amplifies rather than exclusively causes H7), and the sole apparent ISR gain reduces to $1.06\times$ random once a premise-count confound is controlled; at $\beta{=}0.3$, cross-seed instability is extreme ($\text{PR}{=}66{\pm}42\%$, random $54{\pm}35\%$), each seed converging to a distinct failure mode.
7	The pattern transfers to Prolog, where ISR-as-reward yields universal gaming (3/3 seeds, 0\% non-hacking) via three distinct mechanisms including query-as-fact gaming, which bypasses text-match classifiers (\S\ref{sec:taxonomy}).
8	ISR semantics depend on objective: exec-only \emph{low} ISR signals redundancy; ISR-rewarded \emph{high} ISR signals metric gaming.
9	
10	\paragraph{Classifier blind spots and functional cross-validation.}
11	H7b (obfuscated tautology) demonstrates that text-match classifiers have systematic blind spots: the model learns vacuous quantifier wrapping to disguise tautologies, evading detection while simultaneously gaming ISR ($10/12$ samples at $\text{ISR}{\approx}0.8$).
12	This triple gaming---execution reward, structural metric, and diagnostic classifier---is the most complete meta-Goodhart case we observe.
13	Query-as-fact gaming in Prolog (\S\ref{sec:crosslogic}) independently confirms the blind spot: our strict classifier reported $100\%$ ge
…[truncated 1825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T21:28:24.280692+00:00_

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
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T21:28:24.285181+00:00_

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
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with GRPO~\citep{deepseekmath} ($K{=}8$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation testing and feature attribution; our no
…[truncated 5135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_consistency_20260515T212538",
  "tool": "Read",
  "elapsed_ms": 4
}
```

</details>

---
