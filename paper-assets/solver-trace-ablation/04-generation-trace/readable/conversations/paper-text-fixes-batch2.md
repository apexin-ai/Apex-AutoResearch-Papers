# paper text fixes batch2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_text-fixes-batch2_20260522T130648.jsonl`
- **Structured JSON:** [`9e495aa37e6a61654db7.json`](../../sessions/9e/9e495aa37e6a61654db7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-22T13:09:12.894072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T13:09:12.894575+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:ta
…[truncated 14582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T13:09:12.894844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T13:09:12.895066+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algor
…[truncated 4679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T13:09:12.895242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T13:09:12.895506+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 21254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T13:09:12.895662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T13:09:12.895844+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Neurosymbolic reasoning pipelines evaluate success by a single criterion: whether the generated formalization proves under a formal solver.
5	This treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	\paragraph{The evaluation gap.}
9	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.
11	Inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} addresses a complementary problem but offers no training-time diagnostic.
12	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
16	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
17	A formalization where every component is necessary receives $\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\text{ISR}{=}0$.
1
…[truncated 2338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T13:09:12.895999+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T13:09:12.896145+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\ref{app:8b-results},~\ref{app:llama-coldstart}), leaving cross-scale generalization untested.
5	Three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.
6	One of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\ref{app:detailed-results}).
7	ISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T13:09:12.896300+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p\\s*=\\s*0\\.10|p=0\\.10",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p\\s*=\\s*0\\.10|p=0\\.10",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T13:09:12.896420+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T13:09:12.896540+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ProofFOL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ProofFOL",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T13:09:12.896667+00:00_

11:Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
18:ProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory.
107:\textbf{ProofFOL exec-only: cross-dataset replication.}
109:The dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.
111:\textbf{ProofFOL ISR ($\beta{=}0.1$): dataset-dependent asymmetry.}
112:ISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory; Table~\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.
115:The asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\text{ISR}{\approx}0$ and rendering ISR reward effectively corrective.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T13:09:12.896819+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "regressional",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "tool_args": {
    "pattern": "regressional",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T13:09:12.896948+00:00_

docs/paper/related_work.tex:24:Our Goodhart effect follows the regressional pattern~\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\beta$; its application to a diagnostic designed to \emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.
docs/paper/experiments.tex:42:The result is a regressional Goodhart pattern~\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \emph{composition} of failure modes without reducing their aggregate prevalence.
docs/paper/experiments.tex:115:The asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\text{ISR}{\approx}0$ and rendering ISR reward effectively corrective.
docs/paper/appendix.tex:159:The dose-response pattern maps onto the Manheim \& Garrabrant taxonomy~\citep{manheim-goodhart-taxonomy}: $\beta{=}0.1$ on FOLIO instantiates \emph{regressional} Goodhart ($P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR erroneously rewards the shortcut); $\beta{\geq}0.2$ introduces \emph{extremal} elements (PR collapse to 18\% vs.\ 48\% random at $\beta{=}0.3$).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T13:09:12.897071+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ISR prevents|ISR mitigates|ISR eliminates|ISR is associated|ISR correlates",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ISR prevents|ISR mitigates|ISR eliminates|ISR is associated|ISR correlates",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T13:09:12.897192+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T13:09:12.897305+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "all seeds|universal|all converging",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "tool_args": {
    "pattern": "all seeds|universal|all converging",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T13:09:12.897422+00:00_

74:ISR reward amplifies TS convergence: $71\%$ of proved samples under ISR exhibit tautological shortcuts vs.\ $14\%$ under random ($\text{OR}_{\text{CMH}}{=}2.46$; Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
102:\textbf{Prolog: universal Goodhart.}
109:The dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T13:09:12.897536+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "folio|FOLIO",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "tool_args": {
    "pattern": "folio|FOLIO",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T13:09:12.897647+00:00_

147:@inproceedings{folio,
149:  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T13:09:12.897781+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "metr",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "tool_args": {
    "pattern": "metr",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T13:09:12.897894+00:00_

293:@misc{metr-reward-hacking,
298:  note         = {\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T13:09:12.898004+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "seed-dependent convergence|non-convergence|fail to converge|seeds.*converge",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "tool_args": {
    "pattern": "seed-dependent convergence|non-convergence|fail to converge|seeds.*converge",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T13:09:12.898147+00:00_

docs/paper/experiments.tex:30:Three seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\leq}7\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}; Appendix~\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2
docs/paper/experiments.tex:31:Two additional seeds under identical conditions fail to converge ($\text{PR}{\approx}14\%$; Appendix~\ref{app:seed-convergence}), retaining genuine reasoning and confirming that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\ref{app:llama-coldstart}).
docs/paper/experiments.md:53:[Omitted long matching line]
docs/paper/appendix.tex:628:The diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
docs/paper/appendix.tex:634:At $\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\% or near-100\% TS), confirming $\beta{\geq}0.2$ as the extremal Goodhart regime.
docs/paper/appendix.tex:721:Not all exec-only seeds converge.
docs/paper/appendix.tex:722:Of 6 seeds tested (s42--s46, s52), we observe three regimes: \emph{converging with degeneration} (s42: $\text{PR}{=}93\%$, genuine${=}7.5\%$; s44: $\text{PR}{=}96\%$, genuine${=}0\%$; s46: $\text{PR}{=}93\%$ at 500 steps), \emph{slow convergence with degeneration} (s43: $\text{PR}{=}14\%$ but $100\%$ hacking at 500 steps), and \emph{non-converging} (s45: $\text{PR}{=}15\%$, genuine${=}86.7\%$; s52: $\text{PR}{=}14\%$, genuine${=}85.7\%$).
docs/paper/appendix.tex:724:Extended training to 1000 steps for s45 confirms persistent non-convergence ($\text{PR}{=}15\%$, $\text{ISR}^*{=}0.592$, genuine${=}86.7\%$,
…[truncated 2225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T13:09:12.898379+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "offset": "715",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
    "offset": "715",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T13:09:12.898541+00:00_

715	This contrasts sharply with Qwen3-4B, where GRPO reaches $93\%$ PR but collapses to $8\%$ genuine with high cross-seed variance.
716	The result suggests structural degeneration is a byproduct of successful RL optimization, not of the training procedure \emph{per se}: when GRPO fails to amplify prove rate, the model retains structural integrity.
717	
718	\subsection{Seed-Dependent Convergence in Exec-Only GRPO}
719	\label{app:seed-convergence}
720	
721	Not all exec-only seeds converge.
722	Of 6 seeds tested (s42--s46, s52), we observe three regimes: \emph{converging with degeneration} (s42: $\text{PR}{=}93\%$, genuine${=}7.5\%$; s44: $\text{PR}{=}96\%$, genuine${=}0\%$; s46: $\text{PR}{=}93\%$ at 500 steps), \emph{slow convergence with degeneration} (s43: $\text{PR}{=}14\%$ but $100\%$ hacking at 500 steps), and \emph{non-converging} (s45: $\text{PR}{=}15\%$, genuine${=}86.7\%$; s52: $\text{PR}{=}14\%$, genuine${=}85.7\%$).
723	Non-converging seeds retain high genuine rates (85--87\%), indicating that structural degeneration is conditional on successful RL optimization: when GRPO fails to bootstrap prove rate beyond base-model levels, the model preserves structural integrity.
724	Extended training to 1000 steps for s45 confirms persistent non-convergence ($\text{PR}{=}15\%$, $\text{ISR}^*{=}0.592$, genuine${=}86.7\%$, $n{=}15$ proved); the model neither improves nor degenerates.
725	
726	This parallels the LLaMA-3.2-3B finding (Appendix~\ref{app:llama-coldstart}), where GRPO also fails to improve PR and retains structural quality.
727	Both cases support the interpretation that degeneration is a byproduct of reward optimization success, not of the training procedure per se.
728	
729	\subsection{Cross-Scale: Qwen3-8B Exec-Only GRPO}
730	\label{app:8b-results}
731	
732	To test whether structural degeneration generalizes beyond 4B scale, we apply exec-only GRPO to Qwen3-8B with $K{=}8$ rollouts per prompt ($K{=}4$ produces near-identical completions at 8B scale, yiel
…[truncated 369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T13:09:12.898758+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex",
  "old_string": "We distinguish two uses of ISR: as an \\emph{aggregate} metric (mean ISR across a test set, susceptible to premise-count inflation discussed in \\S\\ref{sec:goodhart}), and as a \\emph{per-sample} diagnostic (the LOO result for a single proof, unaffected by cross-sample length distributions).",
  "new_string": "We distinguish two uses of ISR: as an \\emph{aggregate} metric (mean ISR across a test set, susceptible to premise-count inflation discussed in \\S\\ref{sec:goodhart}), and as a \\emph{per-sample} diagnostic (the LOO result for a single proof, unaffected by cross-sample length distributions).\nAs a diagnostic, ISR most readily identifies CE, where removing fabricated expressions collapses the proof ($\\text{ISR}{\\approx}0$), but is less discriminative for TS, where tautological structures score high ISR by construction; detecting TS requires combining ISR with component-count thresholds (\\S\\ref{sec:taxonomy-method})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex",
    "old_string": "We distinguish two uses of ISR: as an \\emph{aggregate} metric (mean ISR across a test set, susceptible to premise-count inflation discussed in \\S\\ref{sec:goodhart}), and as a \\emph{per-sample} diagnostic (the LOO result for a single proof, unaffected by cross-sample length distributions).",
    "new_string": "We distinguish two uses of ISR: as an \\emph{aggregate} metric (mean ISR across a test set, susceptible to premise-count inflation discussed in \\S\\ref{sec:goodhart}), and as a \\emph{per-sample} diagnostic (the LOO result for a single proof, unaffected by cross-sample length distributions).\nAs a diagnostic, ISR most readily identifies CE, where removing fabricated expressions collapses the proof ($\\text{ISR}{\\approx}0$), but is less discriminative for TS, where tautological structures score high ISR by construction; detecting TS requires combining ISR with component-count thresholds (\\S\\ref{sec:taxonomy-method})."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T13:09:12.898956+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_text-fixes-batch2_20260522T130648",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-22T13:09:12.899129+00:00_

Done. Summary of all 8 items:

| Item | Status | Detail |
|------|--------|--------|
| 2a | No edit | Both `p=0.10` already tagged "exploratory" (lines 18, 112) |
| 2b | No edit | §4.2 language around `p=0.182` is descriptive ("indistinguishable", "compositional") |
| 2c | No edit | "all" on line 30 scoped to three seeds; "universal" refers to cross-dataset; appendix E.5 covers seed-dependent convergence |
| 2d | No edit | Regressional Goodhart usage accurate — ISR proxy-goal correlation breaks under optimization via TS |
| 2e | **Edited** | Added sentence to `method.tex:53` — ISR detects CE readily (ISR≈0) but is less discriminative for TS (high ISR by construction; needs component-count thresholds) |
| 2f | No edit | "Two additional seeds" matches appendix data (s45, s52 non-converging out of 6); appendix E.5 thoroughly documents |
| 2g | No edit | FOLIO bib year=2024 correct for EMNLP venue |
| 2h | No edit | URL already present in `note` field |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_text-fixes-batch2_20260522T130648"
}
```

</details>

---
