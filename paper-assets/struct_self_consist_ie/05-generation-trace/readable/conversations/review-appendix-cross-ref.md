# review appendix cross ref

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 0
- **Tool calls:** 44
- **Original source:** `logs/chats/worker_review_appendix-cross-ref_20260524T023114.jsonl`
- **Structured JSON:** [`2b4d4d4342d7189a3fda.json`](../../sessions/2b/2b4d4d4342d7189a3fda.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

89 recorded events

### Tool call

_source line 1 · 2026-05-24T02:36:20.519742+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T02:36:20.520109+00:00_

docs/paper/sections/theoretical.tex
docs/paper/sections/_archived/experiments_OLD.tex
docs/paper/sections/mechanistic.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/diagnostic.tex
docs/paper/sections/related_work.tex
docs/paper/sections/background.tex
docs/paper/sections/abstract.tex
docs/paper/sections/adaptive.tex
docs/paper/sections/method.tex
docs/paper/sections/discussion.tex
docs/paper/sections/limitations.tex
docs/paper/sections/theory.tex
docs/paper/sections/checklist.tex
docs/paper/sections/experiments_main.tex
docs/paper/sections/single_signal.tex
docs/paper/sections/appendix.tex
docs/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T02:36:20.520326+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T02:36:20.520505+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work reports task-level correlations \cite{yao2026consistency} and qualitative diversity collapse \cite{yun2025price} but no instance-level diagnostic framework.
5	
6	Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet selection yields no detectable gains---MV ${<}1$ percentage point (pp) even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
7	This gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also yields no gains, through within-instance compression (\S\ref{sec:selection_gap}).
8	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; Appendix~\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}.
9	A \textit{diagnostic framework} localizes the failure to two co-occurring conditions---degeneracy ($12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$; $\alpha$ here denotes LP-F1 alignment)---which co-occur with selection failure (Table~\ref{tab:method_summary}).
10	The framework decomposes observed failures post-hoc rather than predicting which instances will fail a priori; our analysis is observational and all reported associati
…[truncated 3561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T02:36:20.520658+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T02:36:20.520860+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	Of five signals, only LP scores each sample independently; the other four are instance-level aggregates assigning identical scores to all $N$ candidates.
8	Ensemble optimization assigns dominant weight to LP (mean $0.78$; Appendix~\ref{app:supervised_combination}); when LP fails (few-shot: $\rho{\to}0$; \S\ref{sec:scaling}), no alternative per-sample signal exists.
9	
10	\subsection{Confidence Signals}\label{sec:signals}
11	
12	Throughout, entity matching uses exact span and type match (a predicted entity is correct iff its character offsets and type label both match a gold entity).
13	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
14	
15	\paragraph{Log-probability (model-internal, per-sample).}
16	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
17	\begin{equation}\label{eq:logprob}
18	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
19	\end{equation}
20	
21	\paragraph{Exact match voting (surface, instance-level).}
22	The proportion of samples producing the most common output:
23	\begin{equation}\label{eq:em}
24	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
25	\end{equation}
26	
27	\paragraph{Fleiss' $\kappa$ (surface, instance-level
…[truncated 5404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T02:36:20.521024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T02:36:20.521249+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 53.7\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{figures/fig_n_scaling_mv.pdf}
19	\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
20	\label{fig:n_scaling}
21	\end{figure}
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}\label{sec:qe_results}
25	
26	\begin{table*}[t]
27	\centering
28	\small
29	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 5-seed
…[truncated 7783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T02:36:20.521466+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T02:36:20.521646+00:00_

1	\section{Single-Signal Selection Results}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), leaving insufficient variation for sample discrimination. This compression is model-intrinsic: free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97{\times}$; Appendix~\ref{app:freeform_ablation}). Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.775$, Greedy${=}0.645$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK           & $0.646 \pm 
…[truncated 3482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T02:36:20.521794+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T02:36:20.521951+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	We define the \textbf{capability ceiling} as the practical performance upper bound achievable through self-consistency at realistic sample budgets ($N{\leq}16$), beyond which diminishing returns render further scaling impractical.
14	
15	\subsection{Confidence Signals}\label{sec:signals}
16	
17	Entity matching uses exact span and type match.
18	We distinguish two signal families: four \textit{agreement signals} computed across samples---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal} signal, derived from generation probabilities and providing per-sample discrimination.
19	
20	\paragraph{Log-probability (per-sample).}
21	$c_{\text{lp}}(y_i)
…[truncated 2903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T02:36:20.522158+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T02:36:20.522339+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection yields no detectable gains (\S\ref{sec:selection_gap}), we present exploratory attempts informed by diagnostic findings to extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield a positive result, though on a single dataset.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond self-verification methods in Appendix~\ref{sec:mechanistic} and adaptive methods in this section). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}llrl@{}}
13	\toprule
14	Category & Method & $\Delta$F1 / metric & § \\
15	\midrule
16	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
17	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
18	Self-verif.\ (prompt) & ESJ & AUROC $0.51$ & App.~\ref{sec:mechanistic} \\
19	Multi-round refine. & MRSC & $-3.1$\,pp (FN) & App.~\ref{sec:mechanistic} \\
20	Latent aggregation & LSC & $-3.5$\,pp (FN) & App.~\ref{sec:mechanistic} \\
21	Adaptive gating & DALS & $+0.71$\,pp (SciERC)$^\ddagger$ & App.~\ref{app:dals} \\
22	Supervised verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
23	Sup.\ combination & LR/MLP/RF & $-0.4$ to $-3.1$\,pp & App.~\ref{app:supervised_combination} \\
24	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
25	\bottomrule
26	\end{tabular}}
27	{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
28	\end{table}
29	
30	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
31	
32	Mixing samples from architecturally d
…[truncated 926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T02:36:20.522491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T02:36:20.522624+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	\paragraph{When test-time scaling fails for NER.}
4	For discrete-answer reasoning, sample diversity reflects diverse reasoning paths; for NER, degeneracy ($12$--$68$\%) reduces candidate diversity while signal alignment collapse ($\alpha{\to}0$) limits ranking.
5	The degeneracy decomposition (\S\ref{sec:theory}) identifies $\alpha$---not degeneracy---as the binding constraint ($8$--$33{\times}$ tighter); this persists across families \cite{yun2025price}, scales (4B--72B), and decoding modes (Appendix~\ref{app:freeform_ablation}).
6	The diagnostic framework---identifying these co-occurring conditions---is our primary contribution.
7	At $N{=}8$, high degeneracy ($>50$\%) suggests scaling will not help; low degeneracy with strong LP-F1 alignment may warrant exploratory entity construction; otherwise, greedy decoding remains the default.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T02:36:20.522749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T02:36:20.522870+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	NER exhibits oracle scaling ($c{\approx}0.5$) but on most datasets aggregation gains are ${<}1$\,pp; the diagnostic framework predicts the dataset-dependent optimal strategy, and entity construction yields conditional gains ($+0.32$--$1.40$\,pp) where the framework predicts favorable conditions.
4	The binding constraint is $\alpha{\to}0$ even when $\rho$ is substantial.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T02:36:20.522985+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T02:36:20.523104+00:00_

1	Our primary evidence is from English NER with fine-tuned 7--14B open-weight models; frontier models exhibit markedly different degeneracy profiles (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), and cross-task extensions (RE $n{=}397$, SQL $n{=}196$) are exploratory.
2	The framework is diagnostic, not causal: under global Holm--Bonferroni ($k{=}57$), the strongest construction claim reaches $p_{\text{adj}}{=}0.055$; our negative selection claims are bounded by statistical power (2--3 seeds, MDE ${\approx}1.5$\,pp).
3	Entity-level construction requires $N{\times}$ inference cost for modest gains ($+1$--$1.4$\,pp), and we use a single prompt template per task.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T02:36:20.523265+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theoretical.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theoretical.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T02:36:20.523403+00:00_

1	\section{Theoretical Analysis}\label{sec:theory}
2	
3	\begin{theorem}[Degeneracy Upper Bound]\label{thm:degeneracy_bound}
4	For any aggregation method $A$: $\mathbb{E}[\Delta F_1(A)] \leq (1 - D) \cdot G_{\textup{nd}}$,
5	where $D$ is the degeneracy rate and $G_{\textup{nd}}$ the oracle gap on non-degenerate instances.
6	For signal-based methods with alignment $\alpha \in [0,1]$, this tightens to $(1{-}D) \cdot G_{\textup{nd}} \cdot \alpha$ (proof in Appendix~\ref{app:bound_proof}).
7	\end{theorem}
8	
9	\noindent With $G_{\textup{nd}}{\approx}14.8$\,pp and $\alpha{\approx}0.068$, the critical threshold is $\theta_{\textup{crit}}{=}0.70$: when $D{>}70$\%, SC gain falls below $0.3$\,pp.
10	Across 16 configurations, all gains respect the bound (ratio 3--12\%; Figure~\ref{fig:bound}); the bound is loose because $\alpha$---not $D$---is the bottleneck.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T02:36:20.523527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T02:36:20.523681+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}), consistent with utility degradation on structured outputs \cite{eikema2025structured}.
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{Of the 10.1\% of GPT-5.5 samples producing empty entity sets, 88\% correspond to gold-empty instances; true parse failures affect only 1.2\% of samples (19/1{,}600) and shift all reported metrics by ${<}0.5$\,pp. See Appendix~\ref{app:frontier_sc}.}
13	Degeneracy is mo
…[truncated 4308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T02:36:20.523819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-24T02:36:20.523938+00:00_

File content (69967 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T02:36:20.524051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-24T02:36:20.524234+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time scaling and self-consistency.}\label{sec:yun_contrast}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ with scaling laws \cite{snell2025scaling, brown2024monkeys, gao2023scaling} yield large gains on reasoning; recent extensions include reward-tail-guided search \cite{li2026rewardtail}. Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty} and trained verifiers \cite{cobbe2021verifiers, lightman2024verify, li2023stepaware} target discrete-answer settings.
5	SC can fail when consistent outputs are wrong \cite{chen2023twofailures}; free-form \cite{chen2024usc} and atomic \cite{thirukovalluru2024atomic} variants face limits where sub-output agreement does not yield selection gain. Iterative self-verification \cite{shinn2023reflexion} offers an alternative, but our ESJ and MRSC results (\S\ref{sec:selection_gap}) show such approaches also fail for NER.
6	\citet{yun2025price} identify diversity collapse under constrained decoding; we extend their qualitative account with quantitative diagnostics (\S\ref{sec:selection_gap}).
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE ($\rho$ up to 0.47); we extend to instance-level analysis: (1)~task-level $\rho$ masks instance-level degeneracy; (2)~we decompose failure into degeneracy and LP compression; (3)~pre-deployment diagnostics that task-level correlation cannot provide.
10	Critically, their task-level granularity cannot distinguish instances where scaling helps from those where it harms---our entity-level decomposition addresses this gap (Table~\ref{tab:novelty_comparison}).
11	\citet{xie2023zeroshot} propose entity voting for zero-shot NER; \citet{xie2024selfimproving} report positive SC where zero-shot diversity is high.
12	
13	\paragraph{Uncertainty estimation and MBR.}
14	Our selection instantiates MBR decoding \cite{eikema2022
…[truncated 2593 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T02:36:20.524389+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-24T02:36:20.524521+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling and best-of-$N$.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ with compute-optimal allocation \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code tasks.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty} and BoN scaling laws \cite{gao2023scaling} reduce or characterize inference cost, while trained verifiers \cite{cobbe2021verifiers, lightman2024verify} learn per-sample scoring.
6	All target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we diagnose degeneracy and LP compression as conditions associated with the failure of this correlation to yield selection gains.
10	\citet{xie2023zeroshot} propose entity voting for zero-shot NER, the closest prior work to our entity-level construction; our approach aggregates stochastic samples from a single fine-tuned model without prompt engineering.
11	\citet{yun2025price} show structured formats induce diversity collapse; our LP compression (median range 0.041 nats) corroborates this for NER.
12	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie} and constrained decoding \cite{willard2023guided, dong2024xgrammar}.
13	
14	\paragraph{Uncertainty estimation and MBR decoding.}
15	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling}; \citet{eikema2025structured} find MBR utilities degrade on structured outputs, while our diagnosis identifies degeneracy as the primary bottleneck.
16	Semantic uncertainty \cite{kuhn2023semantic} and confidence estimation \cite{geng2024confidence, xia2025survey} provide complementary model-internal alternatives; our QE signals with AUROC up to 0.82 connect to selective predic
…[truncated 92 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T02:36:20.524660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-24T02:36:20.524798+00:00_

1	\section{How Self-Verification Fails}\label{sec:mechanistic}
2	
3	The diagnostic framework (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
4	Probe experiments use Qwen2.5-7B (not the fine-tuned Qwen3-8B used in main experiments); conclusions are architecture-specific.
5	We evaluate self-verification and diagnostic probes on Qwen2.5-7B\footnote{ESJ, MRSC, and LSC use Qwen2.5-7B-Instruct (zero-shot self-verification capability) rather than the fine-tuned Qwen3-8B used in the main experiments. Conclusion direction is consistent with the main experiments' negative results across all fine-tuned selection strategies. The pattern---selection failure across all signals---is independently confirmed in the Qwen3-8B main experiments, making the introspection boundary a model-independent finding within our tested scale. Probe conclusions are limited to the Qwen2.5 architecture; linear probes may underestimate representational capacity (nonlinear alternatives are left to future work).} fine-tuned for NER on Few-NERD ($N{=}8$, seed 42; full results in Appendix~\ref{app:self_verification}).
6	
7	\paragraph{Entity Self-Judgment (ESJ).}
8	For each extracted entity, we prompt the generating model: ``Is [\textit{entity}] a [\textit{type}] entity in this sentence?''
9	Entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$.
10	ESJ-weighted construction degrades F1 to $0.711$ (vs.\ greedy $0.794$).
11	
12	\paragraph{Multi-Round Self-Consistency (MRSC).}
13	Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
14	MRSC best F1 ($0.763$) falls below greedy.
15	
16	\paragraph{Latent Self-Consistency (LSC).}
17	Mean-pool
…[truncated 1794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-24T02:36:20.524981+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-24T02:36:20.525365+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 36589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-24T02:36:20.525566+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{(app:|sec:)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{(app:|sec:)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-24T02:36:20.525732+00:00_

1:\section{Notation}\label{app:notation}
29:\section{Robustness Analysis}\label{app:robustness}
94:\paragraph{FK independence: instance-level permutation test.}\label{app:fk_independence}
122:\section{Calibration Analysis}\label{app:calibration}
134:\section{Additional Analyses}\label{app:additional}
270:\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
317:\section{Holm--Bonferroni Enumeration}\label{app:holm}
406:\section{Diversity and Selection Analysis}\label{app:diversity}
466:\paragraph{TOST equivalence testing.}\label{app:tost}
512:\paragraph{Multiple comparison considerations.}\label{app:multiple_comparisons}
518:\paragraph{When would consistency-based selection work?}\label{app:when_selection_works}
525:\section{Supervised and Model-Internal Signal Analysis}\label{app:supervised_combination}
537:\subsection{Entity-Level Verifier Transfer}\label{app:verifier_transfer}
545:\subsection{Hidden State Probes}\label{app:hidden_probe}
581:\subsection{Method Coverage Matrix}\label{app:method_coverage}
607:\section{How Self-Verification Fails}\label{sec:mechanistic}
636:\section{Entity-Level Self-Verification Probes}\label{app:self_verification}
680:\section{Cross-Dataset Entailment Self-Judgment}\label{app:esj}
701:\section{Multi-Seed Stability}\label{app:multiseed}
733:\section{Training Configuration}\label{app:training}
786:\section{Thinking Token Impact Analysis}\label{app:thinking_token}
805:\section{Log-Probability Score Compression}\label{app:logprob_ties}
869:\paragraph{$\varepsilon$ robustness of selection F1.}\label{app:epsilon_robustness}
917:\paragraph{Within-instance LP-quality alignment.}\label{app:within_instance_rho}
943:\paragraph{Few-NERD LP compression threshold sensitivity.}\label{app:fewnerd_epsilon}
989:\subsection{Token-Level Signal Comparison}\label{app:token_signal}
997:\section{Consistency-Stratified Selection Analysis}\label{app:vc_quartile}
1033:\section{Exploratory Extension to Relation Extraction}\label{app:re_ext
…[truncated 2711 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-24T02:36:20.525903+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{app:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "200",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{app:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "200",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-24T02:36:20.526142+00:00_

&lt;persisted-output>
Output too large (26.9KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/c9e55e26-2080-47d1-ae01-1314299ec49a/tool-results/toolu_014UocoUjRR2LeJSZvPXm3hA.txt

Preview (first 2KB):
docs/paper/sections/theoretical.tex:6:For signal-based methods with alignment $\alpha \in [0,1]$, this tightens to $(1{-}D) \cdot G_{\textup{nd}} \cdot \alpha$ (proof in Appendix~\ref{app:bound_proof}).
docs/paper/sections/experiments_main.tex:13:\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
docs/paper/sections/experiments_main.tex:14:$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
docs/paper/sections/experiments_main.tex:29:\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 5-seed $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf{bold}. RE in Appendix~\ref{app:re_extension}; $N{=}16$ in Table~\ref{tab:robustness}.}
docs/paper/sections/experiments_main.tex:50:On SciERC, structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.151{\pm}0.006$, 5 seeds; Appendix~\ref{app:bootstrap_signal}).
docs/paper/sections/experiments_main.tex:51:Under seed-replication Holm--Bonferroni correction ($k{=}5$ seeds), the SJ~${>}$~LP advantage reaches $p_{\text{adj}}{=}0.013$ (Appendix~\ref{app:bootstrap_signal}).
docs/paper/sections/experiments_main.tex:76:[Omitted long matching line]
docs/paper/sections/experiments_main.tex:78:Signal ranking is task-specific; per-type analysis shows MV degradation concentrates in low-F
…[truncated 89 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-24T02:36:20.526321+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Appendix~\\\\ref\\{sec:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "50",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Appendix~\\\\ref\\{sec:",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "50",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-24T02:36:20.526463+00:00_

docs/paper/sections/single_signal.tex:52:\paragraph{Mechanistic evidence (Appendix~\ref{sec:mechanistic}).}
docs/paper/sections/adaptive.tex:9:\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond self-verification methods in Appendix~\ref{sec:mechanistic} and adaptive methods in this section). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
docs/paper/sections/introduction.tex:8:A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; Appendix~\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}.
docs/paper/sections/introduction.tex:28:A diagnostic cascade---degeneracy, LP compression, signal alignment---quantifies failure mechanisms at entity level; \citet{yun2025price} describe diversity collapse qualitatively, we provide quantitative decomposition ($D$, $\alpha$, LP range). A necessary condition bound (\S\ref{sec:theory}) confirms $\alpha$ as the binding constraint (3--12\% recovery ratio). Hidden-state probes reveal an introspection boundary (AUROC $0.63$--$0.88$ vs.\ ESJ $\approx 0.50$; Appendix~\ref{sec:mechanistic}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-24T02:36:20.526593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/c9e55e26-2080-47d1-ae01-1314299ec49a/tool-results/toolu_014UocoUjRR2LeJSZvPXm3hA.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/c9e55e26-2080-47d1-ae01-1314299ec49a/tool-results/toolu_014UocoUjRR2LeJSZvPXm3hA.txt"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-24T02:36:20.526841+00:00_

1	docs/paper/sections/theoretical.tex:6:For signal-based methods with alignment $\alpha \in [0,1]$, this tightens to $(1{-}D) \cdot G_{\textup{nd}} \cdot \alpha$ (proof in Appendix~\ref{app:bound_proof}).
2	docs/paper/sections/experiments_main.tex:13:\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
3	docs/paper/sections/experiments_main.tex:14:$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
4	docs/paper/sections/experiments_main.tex:29:\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 5-seed $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf{bold}. RE in Appendix~\ref{app:re_extension}; $N{=}16$ in Table~\ref{tab:robustness}.}
5	docs/paper/sections/experiments_main.tex:50:On SciERC, structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.151{\pm}0.006$, 5 seeds; Appendix~\ref{app:bootstrap_signal}).
6	docs/paper/sections/experiments_main.tex:51:Under seed-replication Holm--Bonferroni correction ($k{=}5$ seeds), the SJ~${>}$~LP advantage reaches $p_{\text{adj}}{=}0.013$ (Appendix~\ref{app:bootstrap_signal}).
7	docs/paper/sections/experiments_main.tex:76:[Omitted long matching line]
8	docs/paper/sections/experiments_main.tex:78:Signal ranking is task-specific; per-type analysis shows MV degradation concentrates in low-F1 types ($\rho{=}0.90$, $p{=}0.002$; Appendix~\ref{app:pertype}).
9	docs/paper/sections/experiments_main.tex:81:Degeneracy does not predict LP gain across 23 configurations ($\rho{=}0.052$, $p{=}0.81$; $n{=}23$, insufficient for reliable correlation---we treat this as supplement
…[truncated 25838 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-24T02:36:20.527056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "525",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "525",
    "limit": "120"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-24T02:36:20.527276+00:00_

525	\section{Supervised and Model-Internal Signal Analysis}\label{app:supervised_combination}
526	
527	\subsection{Supervised Signal Combination}
528	
529	Supervised classifiers (logistic regression, MLP, random forest) trained on all five signals (5-fold CV, 3-seed mean, SciERC, $N{=}16$, $+17.9$~pp headroom) all perform at or below greedy (F1${=}0.644$; LR: $-0.4$~pp; MLP: $-1.6$~pp; RF: $-3.1$~pp).
530	Adding pairwise interaction features does not help (AUROC 0.634 vs.\ 0.638).
531	To test whether richer representations could close the gap, we train a DeBERTa-v3-base verifier that encodes input-output pairs and predicts per-sample F1.
532	DeBERTa achieves $\rho{=}0.329{\pm}0.087$ (5-fold CV, 3 seeds). Despite moderate quality prediction, selection utility is poor: on SciERC, DeBERTa closes $-26.5{\pm}26.5$\% of the oracle gap (13 of 15 runs negative; vs.\ LP's $+4.2{\pm}10.7$\%); on Few-NERD, DeBERTa recovers only $+3.5$\% (single 80/20 split; vs.\ LP's $+16.3$\%).
533	Cross-dataset transfer fails entirely ($-27$\% to $-72$\% gap closure).
534	Grid-search ensemble optimization over signal weights confirms LP dominance: across configurations, LP receives mean weight $0.78$, while FK and SJ receive zero weight; VC and EM serve only as secondary regularizers.
535	Neither handcrafted signal combinations nor learned text representations close the selection gap; only model-internal log-probability provides meaningful selection signal, consistent with an information asymmetry between the generating model and external observers.
536	
537	\subsection{Entity-Level Verifier Transfer}\label{app:verifier_transfer}
538	
539	A LightGBM entity-level verifier (5 features: agreement count, VC, LP, SJ, FK) achieves AUC${=}0.923{\pm}0.002$ under out-of-fold evaluation, confirming that entity correctness is learnable from the available signals.
540	In-domain OOF construction yields $+0.30$\,pp overall, with per-dataset gains of $+1.28$\,pp (SciERC), $+0.55$\,pp (CoNLL), and $+0.02$\,
…[truncated 9710 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-24T02:36:20.527426+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "607",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "607",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-24T02:36:20.527589+00:00_

607	\section{How Self-Verification Fails}\label{sec:mechanistic}
608	
609	The diagnostic framework (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
610	Probe experiments use Qwen2.5-7B (not the fine-tuned Qwen3-8B used in main experiments); conclusions are architecture-specific.
611	We evaluate self-verification and diagnostic probes on Qwen2.5-7B\footnote{ESJ, MRSC, and LSC use Qwen2.5-7B-Instruct (zero-shot self-verification capability) rather than the fine-tuned Qwen3-8B used in the main experiments. Conclusion direction is consistent with the main experiments' negative results across all fine-tuned selection strategies. The pattern---selection failure across all signals---is independently confirmed in the Qwen3-8B main experiments, making the introspection boundary a model-independent finding within our tested scale. Probe conclusions are limited to the Qwen2.5 architecture; linear probes may underestimate representational capacity (nonlinear alternatives are left to future work).} fine-tuned for NER on Few-NERD ($N{=}8$, seed 42; full results in Table~\ref{tab:self_verification}).
612	
613	\paragraph{Entity Self-Judgment (ESJ).}
614	For each extracted entity, we prompt the generating model: ``Is [\textit{entity}] a [\textit{type}] entity in this sentence?''
615	Entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$.
616	ESJ-weighted construction degrades F1 to $0.711$ (vs.\ greedy $0.794$).
617	
618	\paragraph{Multi-Round Self-Consistency (MRSC).}
619	Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
620	MRSC best F1 ($0.763$) falls below greedy.
621	
622	\paragraph{Latent Self-Consistenc
…[truncated 5141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-24T02:36:20.527736+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "680",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "680",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-24T02:36:20.527885+00:00_

680	\section{Cross-Dataset Entailment Self-Judgment}\label{app:esj}
681	
682	Table~\ref{tab:esj_cross} compares entailment-based self-judgment (ESJ) with agreement-based signals across three datasets.
683	ESJ achieves near-random AUROC on all datasets, confirming that the self-verification failure observed on Few-NERD (\S\ref{sec:mechanistic}) generalizes.
684	
685	\begin{table}[h]
686	\small
687	\centering
688	\caption{Entity-level self-verification: ESJ vs.\ agreement-based signals across datasets (Qwen3-8B, $N{=}8$). ESJ AUROC is indistinguishable from chance on all datasets.}
689	\label{tab:esj_cross}
690	\begin{tabular}{lcccc}
691	\toprule
692	Dataset & ESJ AUROC & ESJ $\rho$ & Agree.\ AUROC & Agree.\ $\rho$ \\
693	\midrule
694	SciERC  & 0.512 & 0.020 & 0.792 & 0.515 \\
695	CoNLL   & 0.553 & 0.087 & 0.941 & 0.777 \\
696	Few-NERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\
697	\bottomrule
698	\end{tabular}
699	\end{table}
700	
701	\section{Multi-Seed Stability}\label{app:multiseed}
702	
703	Table~\ref{tab:multiseed} reports quality estimation metrics across multiple seeds (Qwen: 5; LLaMA: 3) for both model families on SciERC ($N{=}8$, $T{=}1.0$).
704	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all model-seed combinations, with $\sigma{\leq}0.025$ for all signals (rankings are stable across all seeds).
705	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.
706	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
707	
708	\begin{table}[t]
709	\centering
710	\small
711	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$; Qwen: 5 seeds (42, 123, 456, 2024, 3141); LLaMA: 3 seeds (42, 123, 456)). NER: both models; RE:
…[truncated 1410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-24T02:36:20.528024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "733",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "733",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-24T02:36:20.528201+00:00_

733	\section{Training Configuration}\label{app:training}
734	
735	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
736	
737	\begin{table}[t]
738	\centering
739	\small
740	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
741	\label{tab:training}
742	\resizebox{\columnwidth}{!}{
743	\begin{tabular}{ll}
744	\toprule
745	Parameter & Value \\
746	\midrule
747	LoRA rank / $\alpha$ & 32 / 64 \\
748	LoRA target & All linear modules \\
749	LoRA dropout & 0 \\
750	Optimizer & AdamW \\
751	Learning rate & 2e-4, cosine schedule \\
752	Warmup ratio & 0.1 \\
753	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
754	Epochs & 5 \\
755	Max sequence length & 2048 \\
756	Precision & bf16 \\
757	Gradient checkpointing & Enabled \\
758	Max gradient norm & 1.0 \\
759	Training seed & 42 \\
760	Framework & LLaMA Factory \\
761	\midrule
762	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
763	SciERC split & 1861 / 275 / 551 \\
764	CoNLL / WNUT-17 & +\,load\_best\_model\_at\_end, \\
765	& eval\_steps${=}$200, save\_limit${=}$5 \\
766	\bottomrule
767	\end{tabular}
768	}
769	\end{table}
770	
771	\paragraph{Prompt template.}
772	For NER, we use a structured prompt:
773	\begin{quote}
774	\small
775	\texttt{System:} You are an expert in Named Entity Recognition.\\
776	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
777	Text: \texttt{\{input\_text\}}\\
778	Entity types: \texttt{\{schema\_types\}}
779	\end{quote}
780	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
781	
782	\paragraph{Constrained decoding.}
783	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{dong2024xgrammar, willard2023guided}, which constrains outputs to valid entity/relation structures matching the target sc
…[truncated 3313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-24T02:36:20.528353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "805",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "805",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-24T02:36:20.528521+00:00_

805	\section{Log-Probability Score Compression}\label{app:logprob_ties}
806	
807	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
808	The median within-instance LP range is only 0.041 nats; we use $\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.
809	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
810	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}); compression is a pervasive regime rather than a bimodal split.
811	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
812	Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$); the subtask change does not affect compression.
813	For comparison, SJ has only 12.5\% tied instances at the same threshold; SJ's advantage over LP for selection is one of score resolution, not information content.
814	
815	\begin{figure}[t]
816	\centering
817	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
818	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
819	\label{fig:lp_range_cdf}
820	\end{figure}
821	
822	\begin{table}[t]
823	\centering
824	\small
825	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
826	\label{tab:logprob_ties}
827	\begin{tab
…[truncated 5106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-24T02:36:20.528667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "989",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "989",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-24T02:36:20.528813+00:00_

989	\subsection{Token-Level Signal Comparison}\label{app:token_signal}
990	
991	We compared mean log-probability (length-normalized, used throughout) with sequence-level log-probability (cumulative sum of token log-probs).
992	Instance-level Spearman $\rho$ between the two rankings averages 0.85, with rankings diverging for 10.6\% of instances where token count coefficient of variation exceeds 0.10.
993	On these disagreement instances, mean LP selection achieves F1${=}0.643$ vs.\ cumulative LP F1${=}0.219$ ($+42.4$\,pp).
994	Overall, mean LP outperforms cumulative LP by $+4.6$ F1 points (Wilcoxon $p{<}0.001$).
995	The divergence is driven by structured output length variation: sequences with more extracted entities are longer but not necessarily higher quality, and length normalization prevents this bias.
996	
997	\section{Consistency-Stratified Selection Analysis}\label{app:vc_quartile}
998	
999	Table~\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\Delta$ (gain over single-sample) for LP and SJ.
1000	
1001	\begin{table}[t]
1002	\centering
1003	\small
1004	\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
1005	\label{tab:vc_quartile}
1006	\begin{tabular}{lcccc}
1007	\toprule
1008	Quartile & Mean VC & LP $\Delta$ & SJ $\Delta$ & Oracle (pp) \\
1009	\midrule
1010	\multicolumn{5}{l}{\textit{NER}} \\
1011	Q1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\
1012	Q2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\
1013	Q3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\
1014	Q4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\
1015	\midrule
1016	\multicolumn{5}{l}{\textit{$^\dagger$RE}} \\
1017	Q1 (low) & --- & $-$3.56 & --- & --- \\
1018	Q4 (high) & --- & $+$4.01 & --- & --- \\
1019	\bottomrule
1020	\end{tabular}
1021	\end{table}
1022	
1023	The NER pattern show
…[truncated 1589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-24T02:36:20.528978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1033",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1033",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-24T02:36:20.529139+00:00_

1033	\section{Exploratory Extension to Relation Extraction}\label{app:re_extension}
1034	
1035	We extend the NER evaluation to relation extraction (RE) on SciERC as an exploratory single-benchmark analysis.
1036	RE produces sets of (head, relation, tail) triples with partial overlap; 40\% of RE instances receive zero F1, and entity span errors account for 55.5\% of RE false negatives, a prerequisite failure that consistency signals cannot detect (\S\ref{app:additional}).
1037	All RE results use Qwen3-8B unless noted; single-seed ($\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.
1038	
1039	\paragraph{Diagnostic framework.}
1040	Applying the diagnostic framework to RE ($N{=}8$): instance degeneracy is $10.1$\%, comparable to SciERC NER ($13.4$\%), yet MV $\Delta{=}{-}5.90$\,pp---far worse than any NER dataset.
1041	The driver is RE's $40$\% zero-F1 rate (vs.\ ${\leq}5.4$\% in NER): diverse but \textit{incorrect} samples produce noise that MV amplifies.
1042	LP-best selection also fails ($\Delta{=}{-}0.94$\,pp), despite pooled LP-F1 $\rho{=}0.350$---above SciERC NER ($0.312$).
1043	Oracle headroom is $+18.1$\,pp (greedy $0.404$, oracle $0.585$), the largest of any configuration, confirming that correct answers exist among samples but no signal recovers them.
1044	
1045	\paragraph{Quality estimation.}
1046	RE quality estimation is reported in Table~\ref{tab:multiseed} (3-seed means).
1047	The signal ranking differs from NER: VC leads ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM, a reversal reflecting RE's higher sensitivity to per-sample scoring.
1048	RE miscalibration is more severe than NER (ECE 0.109--0.339; Figure~\ref{fig:reliability}).
1049	
1050	\paragraph{Selection.}
1051	Table~\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.
1052	At $
…[truncated 1938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-24T02:36:20.529300+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1164",
  "limit": "55"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1164",
    "limit": "55"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-24T02:36:20.529458+00:00_

1164	\subsection{Degeneracy Decomposition}\label{app:bound_proof}
1165	
1166	\begin{definition}[Instance-Level Degeneracy]
1167	Given model $\mathcal{M}$, input $x$, and $N$ i.i.d.\ samples $\{y_1, \ldots, y_N\}$, instance $x$ is \emph{degenerate} if $y_1 = \cdots = y_N$. The degeneracy rate is $D = |\mathcal{D}|^{-1} \sum_{x} \mathbb{1}[y_1(x) = \cdots = y_N(x)]$.
1168	\end{definition}
1169	
1170	\begin{definition}[Non-Degenerate Oracle Gap]
1171	$G_{\text{nd}} = \mathbb{E}[F_1^{\text{oracle}}(x) - F_1^{\text{greedy}}(x) \mid x \in \mathcal{D}_{\neg D}]$, where $\mathcal{D}_{\neg D}$ is the set of non-degenerate instances.
1172	\end{definition}
1173	
1174	\subsection{Proof of the Degeneracy Decomposition}
1175	
1176	Partition $\mathcal{D}$ into degenerate ($\mathcal{D}_D$, fraction $D$) and non-degenerate ($\mathcal{D}_{\neg D}$, fraction $1{-}D$). By total expectation:
1177	\begin{equation}\label{eq:bound_decomp}
1178	\mathbb{E}[\Delta F_1(A)] = D \cdot \mathbb{E}[\Delta F_1 \mid \mathcal{D}_D] + (1{-}D) \cdot \mathbb{E}[\Delta F_1 \mid \mathcal{D}_{\neg D}].
1179	\end{equation}
1180	For degenerate instances, all $N$ samples are identical and equal the greedy output, so $\Delta F_1 = 0$. For non-degenerate instances, $\Delta F_1(A,x) \leq F_1^{\text{oracle}}(x) - F_1^{\text{greedy}}(x)$, giving $\mathbb{E}[\Delta F_1 \mid \mathcal{D}_{\neg D}] \leq G_{\text{nd}}$. Substituting: $\mathbb{E}[\Delta F_1(A)] \leq (1{-}D) \cdot G_{\text{nd}}$.
1181	
1182	For signal-based methods, define alignment $\alpha = \mathbb{E}[\Delta F_1(A_s) \mid \mathcal{D}_{\neg D}] / G_{\text{nd}} \in [0,1]$. Direct substitution yields $\mathbb{E}[\Delta F_1(A_s)] = (1{-}D) \cdot G_{\text{nd}} \cdot \alpha$.
1183	
1184	\begin{corollary}[Critical Degeneracy Threshold]\label{cor:theta_crit}
1185	For SC gain to exceed significance threshold $\varepsilon$, the degeneracy rate must satisfy $D < 1 - \varepsilon / (G_{\text{nd}} \cdot \alpha) \stackrel{\text{def}}{=} \theta_{\text{crit}}$.
1186	Wit
…[truncated 2062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-24T02:36:20.529603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1273",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1273",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-24T02:36:20.529745+00:00_

1273	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
1274	
1275	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).
1276	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
1277	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
1278	RE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\ $-0.68$~pp constrained.
1279	The constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.
1280	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
1281	
1282	\begin{table*}[t]
1283	\centering
1284	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\pm}0.12$~pp).}
1285	\label{tab:freeform_ablation}
1286	
1287	\vspace{2pt}
1288	{\small\textsc{Panel A: Logprob Distribution}}
1289	\vspace{2pt}
1290	
1291	\begin{tabular}{lccc}
1292	\toprule
1293	Metric & Constrained & Free-form & $\Delta$ \\
1294	\midrule
1295	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
1296	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
1297	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
1298	\bottomrule
1299	\end{tabular}
1300	
1301	\vspace{8pt}
1302	
1303	{\small\textsc{Panel B: Selection F1}}
1304	\vspace{2pt}
1305	
1306	\begin{tabular}{llccc}
1307	\toprule
1308	Task & Method & Constrained & Free-
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-24T02:36:20.529884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1422",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1422",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-24T02:36:20.530040+00:00_

1422	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
1423	
1424	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
1425	
1426	\begin{table}[t]
1427	\centering
1428	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
1429	\label{tab:n-scaling}
1430	\small
1431	\resizebox{\columnwidth}{!}{
1432	\begin{tabular}{l ccc ccc}
1433	\toprule
1434	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
1435	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
1436	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
1437	\midrule
1438	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
1439	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
1440	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
1441	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
1442	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
1443	\midrule
1444	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
1445	\bottomrule
1446	\end{tabular}
1447	}
1448	\end{table}
1449	
1450	\begin{table}[t]
1451	\centering
1452	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
1453	\label{tab:ranking-stability}
1454	\small
1455	\resizebox{\columnwidth}{!}{
1456	\begin{tabular}{ll cc l}
1457	\toprule
1458	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
1459	\midrule
1460	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
1461	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-24T02:36:20.530211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1563",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1563",
    "limit": "35"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-24T02:36:20.530356+00:00_

1563	\paragraph{Degeneracy and inverse scaling.}\label{app:degen_inverse}
1564	Table~\ref{tab:degen_inverse} stratifies $N$-transitions by instance degeneracy status across all dataset--regime combinations.
1565	Degenerate instances exhibit near-zero inverse scaling ($1.3$\% vs.\ $11.1$\% for non-degenerate; OR${=}0.109$, $p{<}10^{-300}$, Fisher's exact test over $195{,}675$ transitions).
1566	This is expected: degenerate instances produce identical entity sets across all $N$ samples, so MV F1 is constant by construction---they cannot exhibit inverse scaling.
1567	The effect holds across all settings (Table~\ref{tab:degen_inverse}), with the sole exception of SciERC pretrained ($p{=}0.083$), where low degeneracy (${\leq}10$\%) yields too few degenerate transitions for adequate power.
1568	Pretrained models show a stronger protective effect (OR${=}0.066$ vs.\ $0.166$ for finetuned), consistent with higher overall inverse scaling rates creating more room for the degeneracy--stability association.
1569	
1570	\begin{table}[t]
1571	\centering
1572	\small
1573	\caption{Inverse scaling rate by degeneracy status. An $N{\to}N'$ transition is ``inverse'' if MV F1 at $N'$ is strictly lower than at $N$. OR: odds ratio (Fisher's exact test).}
1574	\label{tab:degen_inverse}
1575	\resizebox{\columnwidth}{!}{%
1576	\begin{tabular}{@{}lrrrrrc@{}}
1577	\toprule
1578	Setting & \multicolumn{2}{c}{Degenerate} & \multicolumn{2}{c}{Non-degenerate} & OR & $p$ \\
1579	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
1580	 & Trans. & Inv.\% & Trans. & Inv.\% & & \\
1581	\midrule
1582	SciERC FT & 485 & 0.8 & 2{,}160 & 9.6 & 0.078 & ${<}10^{-6}$ \\
1583	CoNLL FT & 8{,}256 & 0.3 & 5{,}524 & 4.1 & 0.060 & ${<}10^{-6}$ \\
1584	Few-NERD FT & 22{,}298 & 1.9 & 75{,}397 & 8.4 & 0.213 & ${<}10^{-6}$ \\
1585	SciERC PT & 81 & 3.7 & 2{,}564 & 9.9 & 0.350 & 0.083 \\
1586	CoNLL PT & 5{,}284 & 0.3 & 8{,}496 & 7.9 & 0.033 & ${<}10^{-6}$ \\
1587	Few-NERD PT & 18{,}007 & 1.4 & 47{,}123 & 16.8 & 0.071 & ${<}10^{-6}$ \\
15
…[truncated 329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-24T02:36:20.530500+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1594",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1594",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-24T02:36:20.530648+00:00_

1594	\section{Cross-Scale and Cross-Family Comparison}\label{app:cross_scale}
1595	
1596	\begin{table}[t]
1597	\centering
1598	\small
1599	\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\ref{tab:fewnerd}. $^\star$Qwen2.5; unmarked: Qwen3. $^\dagger$Not computed. $^\ddagger$200-instance subset; 10.1\% parse failures excluded.}
1600	\label{tab:scale_comparison}
1601	\resizebox{\columnwidth}{!}{%
1602	\begin{tabular}{@{}llccccccc@{}}
1603	\toprule
1604	Dataset & Regime & Greedy & Hdr. & Degen. & VC & SJ & FK & LP \\
1605	\midrule
1606	SciERC & 8B FT  & .667 & 11.4 & 12.2 & .326 & .324 & .177 & .159 \\
1607	       & 72B ZS$^\star$ & .399 & 15.0 & 21.0 & .277 & .217 & .227 & .081 \\
1608	\midrule
1609	Few-NERD & 7B FT$^\star$ & .784 & 9.2 & 31.7 & .404 & .388 & .315 & .346 \\
1610	         & 8B FT & .748 & 12.4 & 13.0 & .386 & .300 & .313 & .220 \\
1611	         & 14B FT & .798 & 8.1 & ---$^\dagger$ & ---$^\dagger$ & ---$^\dagger$ & ---$^\dagger$ & ---$^\dagger$ \\
1612	         & 72B ZS$^\star$ & .628 & ---$^\dagger$ & 46.2 & .416 & .345 & ---$^\dagger$ & .119 \\
1613	         & GPT-5.5 ZS$^\ddagger$ & .638 & 8.2 & 50.0 & ---$^\dagger$ & .346 & ---$^\dagger$ & ---$^\dagger$ \\
1614	\midrule
1615	CoNLL  & 8B FT  & .908 & ${\approx}$4 & 61.7 & .424 & .436 & .400 & .302 \\
1616	       & 72B ZS$^\star$ & .712 & 5.3 & 67.7 & .297 & .304 & .302 & $-$.002 \\
1617	\bottomrule
1618	\end{tabular}}
1619	\end{table}
1620	
1621	LP $\rho$ drops without fine-tuning (Table~\ref{tab:scale_comparison}) and LP selection fails on all 72B zero-shot datasets. Structural signals generalize better (Few-NERD VC $\rho{=}0.416$). Degeneracy increases at 72B (Few-NERD: $46.2$\% vs.\ $13.0$\%; CoNLL: $67.7$\% vs.\ $61.7$\%); the gap persists under this specific 72B zero-shot configuration, though scale, training r
…[truncated 1976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-24T02:36:20.530787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1696",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1696",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-24T02:36:20.530926+00:00_

1696	\subsection{Per-Type MV Analysis}\label{app:pertype}
1697	
1698	\begin{table}[t]
1699	\centering
1700	\small
1701	\caption{Per-entity-type MV gain on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, 3-seed mean). Strict MV ($\theta{>}N/2$). Types sorted by finetuned greedy F1. 7/8 types flip MV direction between pretrained and finetuned.}
1702	\label{tab:pertype_mv}
1703	\begin{tabular}{@{}lrccc@{}}
1704	\toprule
1705	& & & \multicolumn{2}{c}{MV $\Delta$ (pp)} \\
1706	\cmidrule(lr){4-5}
1707	Entity type & $n$ & Greedy F1 & Pretr. & Finetuned \\
1708	\midrule
1709	person & ${\sim}$7{,}200 & .820 & $+$4.17 & $-$0.67 \\
1710	location & ${\sim}$8{,}800 & .797 & $+$2.47 & $-$1.52 \\
1711	art & ${\sim}$1{,}250 & .755 & $+$0.73 & $-$1.51 \\
1712	organization & ${\sim}$6{,}700 & .725 & $+$3.15 & $-$2.65 \\
1713	building & ${\sim}$1{,}540 & .696 & $+$1.98 & $-$3.90 \\
1714	product & ${\sim}$2{,}260 & .657 & $+$1.78 & $-$3.38 \\
1715	event & ${\sim}$1{,}315 & .645 & $+$2.34 & $-$3.17 \\
1716	other & ${\sim}$3{,}485 & .639 & $-$0.45 & $-$3.02 \\
1717	\midrule
1718	\multicolumn{3}{@{}l}{$r$(greedy F1, MV\,$\Delta$)} & .86 & .90 \\
1719	\multicolumn{3}{@{}l}{$p$-value} & .006 & .002 \\
1720	\bottomrule
1721	\end{tabular}
1722	\end{table}
1723	MV direction flips between pretrained and finetuned decoding for 7 of 8 entity types (Table~\ref{tab:pertype_mv}): types that benefit from MV under pretrained decoding ($+0.73$ to $+4.17$\,pp) are uniformly harmed under finetuning ($-0.67$ to $-3.90$\,pp), with only \textit{other} (lowest-F1) remaining negative in both regimes.
1724	The correlation between greedy F1 and MV $\Delta$ is strong in both regimes ($r{=}0.86$, $p{=}0.006$ pretrained; $r{=}0.90$, $p{=}0.002$ finetuned), indicating entity-type difficulty predicts MV magnitude regardless of direction.
1725	This rules out entity-type-specific factors as the explanation for MV failure: the same types succeed with pretrained decoding and fail with finetuned decoding, implicating the finetun
…[truncated 771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-24T02:36:20.531069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1728",
  "limit": "45"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1728",
    "limit": "45"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-24T02:36:20.531237+00:00_

1728	\subsection{Frontier Model Self-Consistency}\label{app:frontier_sc}
1729	
1730	\begin{table}[h]
1731	\centering
1732	\small
1733	\caption{Cross-family frontier SC on Few-NERD ($N{=}8$, $T{=}1.0$, 200 instances, zero-shot). Parse failures excluded from all metrics; $N_{\textit{eff}}$: mean effective samples after exclusion. Selection gap $= $ oracle $-$ MV. Text-based entity matching (Appendix~\ref{app:frontier_sc}, entity matching paragraph). Qwen3-8B FT shown for reference.}
1734	\label{tab:frontier_sc_cross}
1735	\resizebox{\columnwidth}{!}{%
1736	\begin{tabular}{@{}lcccccc@{}}
1737	\toprule
1738	Model & Greedy & MV ($\Delta$) & Oracle & Degen.\% & Sel.\ gap & Parse\% \\
1739	\midrule
1740	DeepSeek & .399 & .424 ($+2.5$) & .714 & 5.5 & .290 & 46.9 \\
1741	Gemini 2.5 Pro & .630 & .645 ($+1.5$) & .758 & 28.5 & .113 & 11.9 \\
1742	GPT-5.5 & .638 & .652 ($+1.4$) & .720 & 50.0 & .068 & 10.1 \\
1743	Claude Son.~4 & .607 & .623 ($+1.6$) & .654 & 74.0 & .032 & 6.4 \\
1744	\midrule
1745	Qwen3-8B FT & .789 & .792 ($+0.3$) & .858 & 13.0 & .066 & ${\approx}$0 \\
1746	\bottomrule
1747	\end{tabular}}
1748	\end{table}
1749	
1750	All four frontier families exhibit the correlation-selection gap (Table~\ref{tab:frontier_sc_cross}): MV recovers only a fraction of oracle headroom regardless of model capability.
1751	Degeneracy and selection gap are negatively correlated across families: Claude Sonnet~4 (74\% degen, 0.032 gap) vs.\ DeepSeek (5.5\%, 0.290)---higher degeneracy eliminates the instances where aggregation could help.
1752	Gemini 2.5 Pro achieves the highest oracle F1 (.758) and the highest QE correlation ($\rho_{\textup{SJ}}{=}0.350$, $\rho_{\textup{agr}}{=}0.389$) among frontier models, with balanced degeneracy (28.5\%) preserving a 0.113 selection gap---the largest gap among models with ${\geq}85$\% parse success.
1753	DeepSeek's low degeneracy preserves the largest absolute gap (.290), but 47\% parse failures reduce effective $N$ to ${\approx}4.2$, limiting aggrega
…[truncated 1560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-24T02:36:20.531410+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1964",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1964",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-24T02:36:20.531570+00:00_

1964	\section{Per-Entity-Type LP Selection Analysis}\label{app:per_type_lp}
1965	
1966	Table~\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.
1967	The degeneracy-gating mechanism holds at entity-type granularity: 7 of 8 types show positive LP selection gains, and the sole negative type (Art, $-0.17$~pp) has the highest degeneracy (19.8\%).
1968	The correlation between per-type degeneracy and oracle headroom is strong and significant (Spearman $\rho{=}{-}0.881$, $p{=}0.004$; exact permutation $p{=}0.005$); degeneracy directly constrains the headroom available for selection.
1969	Under a conservative $\text{df}{=}4$ adjustment for within-type dependence, the correlation remains significant ($p{=}0.033$).
1970	Entity types show near-zero intra-class correlation (ICC $= -0.004$), supporting the independence assumption underlying per-type analysis.
1971	
1972	\begin{table}[h]
1973	\centering
1974	\small
1975	\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\Delta$; Art (highest degeneracy) is the sole exception.}
1976	\label{tab:per_type_lp}
1977	\resizebox{\columnwidth}{!}{
1978	\begin{tabular}{lrrrrrrr}
1979	\toprule
1980	Entity Type & $n$ & Degen.\% & Greedy & LP Sel & $\Delta$ (pp) & LP $\rho$ & Headroom \\
1981	\midrule
1982	Event & 1{,}306 & 6.0 & .655 & .662 & $+$0.65 & .457 & 16.1\,pp \\
1983	Other & 3{,}433 & 6.6 & .637 & .685 & $\mathbf{+4.73}$ & .491 & 19.4\,pp \\
1984	Organization & 6{,}647 & 6.7 & .720 & .732 & $+$1.21 & .509 & 13.3\,pp \\
1985	Building & 1{,}587 & 7.2 & .702 & .705 & $+$0.23 & .478 & 14.9\,pp \\
1986	Product & 2{,}276 & 8.2 & .656 & .677 & $+$2.01 & .483 & 15.8\,pp \\
1987	Location & 8{,}023 & 11.4 & .793 & .798 & $+$0.53 & .520 & 10.3\,pp \\
1988	Person & 8{,}016 & 13.4 & .822 & .835 & $+$1.25 & .544 & 9.2\,pp \\
1989	Art & 1{,}277 & 19.8 & .756 & .754 & 
…[truncated 3585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-24T02:36:20.531710+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "2066",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "2066",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-24T02:36:20.531876+00:00_

2066	\section{Epoch Confound Analysis}\label{app:epoch_confound}
2067	
2068	\paragraph{Training convergence modulates degeneracy.}
2069	Table~\ref{tab:epoch_confound} compares the 3-epoch model (used throughout the main text) with a 5-epoch variant on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$; gold-filtered $n{=}32{,}565$, 2-seed mean).
2070	Extended training increases greedy F1 by $+0.7$~pp ($0.791 \to 0.798$) and triples instance degeneracy ($8.8$\% $\to$ $26.4$\%), reducing the fraction of instances with non-degenerate outputs.
2071	The 5-epoch MV $\Delta$ ($-0.40$\,pp) appears smaller than 3-epoch ($-2.74$\,pp), but this is misleading: $26$\% of instances are fully degenerate (MV${\equiv}$greedy, $\Delta{=}0$), diluting the aggregate.
2072	On non-degenerate instances, MV $\Delta{\approx}{-}0.55$\,pp, still negative---degeneracy masks the MV penalty rather than improving it.
2073	
2074	LP selection shows even more dramatic degradation: 5-epoch LP $\Delta{=}{+}0.12{\pm}0.04$\,pp (2-seed mean), a 91\% reduction from the 3-epoch $+1.39$\,pp (both evaluated on the full test set under identical conditions; Table~\ref{tab:epoch_confound}). This confirms that training convergence not only increases degeneracy but also erodes LP's discriminative power within non-degenerate instances, consistent with the alignment degradation observed in SciERC (Table~\ref{tab:epoch_scierc}).
2075	
2076	Evaluation loss increases after epoch 3, and the best checkpoint by validation loss occurs at approximately epoch 3.9.
2077	Standard early stopping practice thus naturally selects the low-degeneracy regime.
2078	This finding refines the narrative: degeneracy is not a fixed property of datasets but is modulated by the degree of training convergence. Over-trained models compress their output distributions, collapsing diversity even on datasets that support it under well-regularized training.
2079	
2080	\begin{table}[t]
2081	\centering
2082	\small
2083	\caption{Training convergence confound on F
…[truncated 6320 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-24T02:36:20.532021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "2138",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "2138",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-24T02:36:20.532204+00:00_

2138	\subsection{Degeneracy-Aware LP Selection}\label{app:dals}
2139	
2140	The non-tied subset analysis (Table~\ref{tab:nontied_main}) identifies within-instance LP range (max minus min LP across $N$ samples) as a per-instance degeneracy proxy: instances with near-zero LP range carry no discriminative signal.
2141	Degeneracy-aware LP selection (DALS) operationalizes this: when LP range exceeds $\tau{=}0.05$ (the threshold independently motivated by the non-tied analysis; Appendix~\ref{app:epsilon_robustness}), select the highest-LP sample; otherwise fall back to greedy.
2142	On SciERC, DALS yields $+0.71{\pm}0.48$~pp (3-seed mean; individual seeds: $+0.19$ to $+1.14$~pp); on Few-NERD, $+0.30$~pp ($p{<}0.001$; gain remains positive across $\tau \in [0.01, 0.15]$); on CoNLL, where pure LP selection degrades F1 ($-0.85$~pp), DALS shows comparable degradation (Qwen: $-0.87$~pp; LLaMA: neutral).
2143	DALS improves over pure LP selection when degeneracy is moderate, provides partial damage control when LP selection is harmful, and defaults to greedy when LP range signals no information.
2144	While gains are modest and seed-sensitive, LP range serves as an operationally accessible degeneracy proxy, though the mixed cross-dataset results confirm that degeneracy gating alone cannot ensure positive selection outcomes.
2145	
2146	\paragraph{LOO $\tau$ sensitivity.}
2147	Leave-one-out (LOO) cross-validation across datasets shows that the optimal $\tau$ spans two orders of magnitude: $\tau^*{=}0.001$ on Few-NERD, $0.05$ on SciERC, and $0.10$ on CoNLL.
2148	LOO regret (the gap between oracle and LOO-selected $\tau$) ranges from 0.51 to 1.21~pp.
2149	The best single cross-dataset $\tau$ ($\tau{=}0.05$) matches the independently motivated non-tied threshold, but yields dataset-specific suboptimality: even with oracle $\tau$, CoNLL remains at $-0.31$~pp.
2150	This sensitivity reinforces the diagnostic framing of DALS: per-dataset $\tau$ tuning is required for positive gains, and eve
…[truncated 2476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-24T02:36:20.532370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "2255",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "2255",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-24T02:36:20.532531+00:00_

2255	\subsection{Entity Construction Results}\label{app:entity_construction_table}
2256	
2257	\begin{table}[h]
2258	\centering
2259	\small
2260	\caption{Entity construction vs.\ greedy ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$). $\theta{=}2/N$. $p$: paired bootstrap vs.\ greedy. $^\dagger$Survives per-family Holm--Bonferroni correction (construction, $k{=}10$); global correction ($k{=}57$) yields $p_{\text{adj}}{=}0.055$ (Appendix~\ref{app:holm}). $^\ddagger$LP-weighted not computed.}
2261	\label{tab:entity_construction}
2262	\resizebox{\columnwidth}{!}{%
2263	\begin{tabular}{@{}llcccc@{}}
2264	\toprule
2265	Dataset & Wt. & Greedy & Constr. & $\Delta$ & $p$ \\
2266	\midrule
2267	SciERC & LP & $.667{\pm}.001$ & $.670{\pm}.003$ & $+0.32$\,pp & n.s. \\
2268	       & Unif. & $.667{\pm}.001$ & $.660{\pm}.004$ & $-0.74$\,pp & n.s. \\
2269	\addlinespace
2270	Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001^\dagger$ \\
2271	         & Unif. & $.748$ & $\mathbf{.756{\pm}.006}$ & $+0.74{\pm}0.58$\,pp & .003 \\
2272	\addlinespace
2273	CoNLL$^\ddagger$ & Unif. & .908 & .904 & $-0.39$\,pp & n.s. \\
2274	\bottomrule
2275	\end{tabular}}
2276	\end{table}
2277	
2278	\subsection{Entity Construction Threshold Sensitivity}
2279	\label{app:theta_sweep}
2280	
2281	Table~\ref{tab:theta_sweep} reports entity construction F1 as a function of the confirmation threshold $\theta$ across three datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$). The default $\theta{=}2/N{=}0.25$ achieves the best LP-weighted $\Delta$F1 on Few-NERD and is within 0.04\,pp of the optimum on SciERC. Performance is stable across $\theta \in [0.15, 0.35]$; below 0.15, spurious entities degrade precision, and above 0.40, aggressive filtering removes correct low-frequency entities.
2282	
2283	\begin{table}[h]
2284	\caption{Entity construction threshold sensitivity ($N{=}8$, Qwen3-8B, $T{=}1.0$). $\Delta$: F1 difference vs.\ greedy in percentage points. Best $\
…[truncated 3053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-24T02:36:20.532678+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "2327",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "2327",
    "limit": "35"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-24T02:36:20.532821+00:00_

2327	\subsection{Few-Shot Error Correlation Analysis}\label{app:fs_error}
2328	
2329	We investigated whether few-shot demonstrations induce correlated entity-level errors that explain construction failure.
2330	Pairwise error overlap (Jaccard similarity of per-sample false-positive and false-negative entity sets) shows no significant difference between FS and ZS regimes (SciERC: $0.454$ vs.\ $0.452$, $p{=}0.84$; CoNLL: $0.103$ vs.\ $0.104$, $p{=}0.64$; permutation tests, 10{,}000 resamples).
2331	We additionally measure entity-level prediction entropy across $N{=}8$ samples per instance.
2332	On SciERC, FS and ZS entropies are indistinguishable ($0.483$ vs.\ $0.485$, $p{=}0.81$).
2333	On CoNLL, however, entity prediction entropy is significantly \emph{higher} under FS ($0.209$ vs.\ $0.184$, $p{<}10^{-9}$, $r{=}0.106$, small effect; Wilcoxon signed-rank test), contrary to the hypothesis that demonstrations concentrate predictions---they instead \emph{increase} output diversity on this dataset.
2334	The mechanism by which few-shot demonstrations undermine construction remains an open question; entity-level error overlap is preserved while prediction entropy may even rise, suggesting that the \emph{nature} rather than the \emph{diversity} of errors shifts in ways that defeat LP-weighted voting.
2335	
2336	\subsection{Construction Weighting Variants}\label{app:weighting_variants}
2337	
2338	Table~\ref{tab:weighting_variants} compares LP-weighted, VC-weighted, and SJ-weighted entity construction on LLaMA-3.1-8B (3-seed mean, $N{=}8$, $T{=}1.0$, $\theta{=}2/N$).
2339	All three weighting schemes beat greedy on SciERC, where degeneracy is low; LP and VC also improve Few-NERD, though gains are smaller than the Qwen results in Table~\ref{tab:entity_construction}.
2340	The optimal weighting scheme is model-dependent (VC leads on LLaMA SciERC; LP leads on Qwen), but the core finding is robust: entity-level voting improves F1 in low-degeneracy regimes regardless of the specific 
…[truncated 1215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-24T02:36:20.532966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "2550",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "2550",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-24T02:36:20.533096+00:00_

2550	\noindent These examples illustrate that the failure modes identified by the diagnostic framework are not statistical abstractions but manifest in individual instances. The LP and consensus failures frequently co-occur (e.g., ``Cramer'' instance), confirming that the signals share common blind spots rather than providing independent error detection.
2551	
2552	\section{Practical Recommendations}\label{app:recommendations}
2553	
2554	Measuring degeneracy and LP-F1 alignment at $N{=}8$ suffices: if ${>}50$\% degenerate, scaling provides no benefit; if degeneracy ${<}20$\% with $\rho{>}0.70$, construction may yield gains; otherwise prefer greedy.
2555	
2556	\section{Use of AI Assistants}
2557	\label{app:ai-assistants}
2558	
2559	We used Claude (Anthropic) as an AI coding and writing assistant
2560	throughout this work. Specifically:
2561	\begin{itemize}
2562	    \item \textbf{Code:} drafting experiment scripts, data-processing
2563	    pipelines, and analysis utilities; debugging and refactoring.
2564	    \item \textbf{Writing:} drafting and revising paper sections,
2565	    polishing prose, and reformatting LaTeX.
2566	    \item \textbf{Literature:} summarizing related papers to inform
2567	    related-work section.
2568	\end{itemize}
2569	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-24T02:36:20.533297+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-24T02:36:20.533421+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-24T02:36:20.533569+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/appendix_crossref_review.md",
  "content": "# Appendix 交叉引用审查\n\n## 统计\n- 主文引用 appendix 次数：64\n- 唯一 label 数：33\n- 所有 label 均存在：**是**\n\n## 逐条审查\n\n| # | 主文位置 | 引用 label | 主文语境 | Appendix 内容摘要 | 评估 |\n|---|---------|-----------|---------|-----------------|------|\n| 1 | introduction.tex:L8 | `sec:mechanistic` | \"hidden-state probe...AUROC 0.63–0.88; Appendix\" | §How Self-Verification Fails: ESJ/MRSC/LSC probes, hidden-state probe, introspection boundary（~30行正文 + Table） | ✅ 充分 |\n| 2 | introduction.tex:L11 | `app:re_extension` | \"RE reveals a distinct bottleneck (40% zero-F1)\" | §Exploratory Extension to RE: diagnostic framework, QE, selection, scale ablation, free-form decoding（~90行，多表） | ✅ 充分 |\n| 3 | introduction.tex:L14 | `app:re_extension` | \"RE F1 confounded by entity span errors\" | 同上 | ✅ 充分 |\n| 4 | introduction.tex:L28 | `sec:mechanistic` | \"Hidden-state probes reveal introspection boundary\" | 同#1 | ✅ 充分 |\n| 5 | method.tex:L6 | `app:notation` | \"notation in Appendix\" | §Notation: Table with all symbols（27行，完整符号表） | ✅ 充分 |\n| 6 | method.tex:L8 | `app:supervised_combination` | \"LP mean weight 0.78\" | §Supervised and Model-Internal Signal Analysis: LR/MLP/RF classifiers, DeBERTa verifier, grid-search（~12行详细分析） | ✅ 充分 |\n| 7 | method.tex:L33 | `app:fk_independence` | \"FK independence analysis\" | ¶FK independence permutation test: 3 configs, Table with t-stats, split-half r（~25行） | ✅ 充分 |\n| 8 | method.tex:L56 | `app:additional` | \"exclude instances with no gold annotations\" | §Additional Analyses: signal heatmap, per-relation diagnostic, capability stratification, length analysis, WNUT（~130行，多表多图） | ✅ 充分 |\n| 9 | method.tex:L80 | `app:mbr_proof` | \"proof in Appendix\" | §MBR Framework and Proof: formal proof of Proposition 1（~25行，完整证明） | ✅ 充分 |\n| 10 | diagnostic.tex:L8 | `app:notation` | \"notation in Appendix\" | 同#5 | ✅ 充分 |\n| 11 | diagnostic.tex:L10 | `app:supervised_combination` | \"LP mean weight 0.78, structural zero weight\" | 同#6 | ✅ 充分 |\n| 12 | diagnostic.tex:L22 | `app:token_signal` | \"length normalization +4.6 F1 points\" | §Token-Level Signal Comparison: mean vs cumulative LP, +4.6pp, Wilcoxon test（~8行） | ✅ 充分 |\n| 13 | diagnostic.tex:L34 | `app:fk_independence` | \"FK independence\" | 同#7 | ✅ 充分 |\n| 14 | diagnostic.tex:L41 | `app:additional` | \"instance exclusion\" | 同#8 | ✅ 充分 |\n| 15 | experiments_main.tex:L13 | `app:training` | \"LoRA fine-tuned...training details\" | §Training Configuration: Table with all hyperparameters, prompt template, constrained decoding details（~50行） | ✅ 充分 |\n| 16 | experiments_main.tex:L13 | `app:epoch_confound` | \"Few-NERD uses 3 epochs vs 5\" | §Epoch Confound Analysis: Few-NERD 3v5, SciERC 3/5/10 epoch curve, 2 tables（~70行） | ✅ 充分 |\n| 17 | experiments_main.tex:L14 | `app:n_scaling` | \"N∈{16,32,64} for scaling\" | §N-Scaling Detailed Analysis: signal quality vs N, ranking stability, inverse scaling, theta sweep tables（~140行，多表） | ✅ 充分 |\n| 18 | experiments_main.tex:L29 | `app:re_extension` | \"RE in Appendix\" | 同#2 | ✅ 充分 |\n| 19 | experiments_main.tex:L50 | `app:bootstrap_signal` | \"bootstrap CIs confirm the gap\" | §Bootstrap CI for Signal Comparisons: individual CIs, pairwise Δρ, seed-replication analysis（~45行，2 tables） | ✅ 充分 |\n| 20 | experiments_main.tex:L51 | `app:bootstrap_signal` | \"Holm-Bonferroni p_adj=0.013\" | 同#19 | ✅ 充分 |\n| 21 | experiments_main.tex:L76 | `app:epoch_confound` | \"5-epoch degeneracy 26%\" | 同#16 | ✅ 充分 |\n| 22 | experiments_main.tex:L78 | `app:pertype` | \"per-type MV degradation ρ=0.90\" | §Per-Type MV Analysis: 8 entity types, pretrained vs finetuned comparison, Table（~30行） | ✅ 充分 |\n| 23 | experiments_main.tex:L81 | `app:per_type_lp` | \"per-type LP ρ=-0.881\" | §Per-Entity-Type LP Selection: Few-NERD/CoNLL/SciERC per-type tables, degeneracy-headroom correlation（~70行，3 tables） | ✅ 充分 |\n| 24 | experiments_main.tex:L86 | `app:per_type_lp` | \"per-type LP (figure caption)\" | 同#23 | ✅ 充分 |\n| 25 | experiments_main.tex:L91 | `app:re_extension` | \"RE framework extends, 40% zero-F1\" | 同#2 | ✅ 充分 |\n| 26 | experiments_main.tex:L96 | `app:calibration` | \"signal rankings robust; calibration\" | §Calibration Analysis: reliability diagrams, ECE values（~12行 + figure） | ✅ 充分 |\n| 27 | experiments_main.tex:L103 | `app:theta_sweep` | \"θ stable in [0.15, 0.35]\" | §Entity Construction Threshold Sensitivity: 8-point sweep × 3 datasets, Table（~45行） | ✅ 充分 |\n| 28 | experiments_main.tex:L105 | `app:holm` | \"global k=57 Holm-Bonferroni\" | §Holm-Bonferroni Enumeration: complete 57-test table with raw p and p_adj（~90行） | ✅ 充分 |\n| 29 | experiments_main.tex:L107 | `app:epoch_confound` | \"5-epoch LP gains collapse\" | 同#16 | ✅ 充分 |\n| 30 | experiments_main.tex:L113 | `app:freeform_ablation` | \"decoding modes\" | §Free-Form Decoding Ablation: 3-panel table, LP distribution, selection F1, QE comparison（~110行） | ✅ 充分 |\n| 31 | experiments_main.tex:L114 | `app:n_scaling` | \"Qwen2.5-7B N=32 +3.85pp\" | 同#17 | ✅ 充分 |\n| 32 | single_signal.tex:L6 | `app:logprob_ties` | \"60% LP range below 0.041 nats\" | §Log-Probability Score Compression: CDF figure, tied fraction table, ε sweep, non-tied subset（~90行，多表多图） | ✅ 充分 |\n| 33 | single_signal.tex:L6 | `app:freeform_ablation` | \"free-form decoding yields identical LP\" | 同#30 | ✅ 充分 |\n| 34 | single_signal.tex:L39 | `app:bootstrap_signal` | \"MDE ≈1.5pp\" | 同#19 | ✅ 充分 |\n| 35 | single_signal.tex:L40 | `app:bootstrap_signal` | \"bootstrap CIs reported\" | 同#19 | ✅ 充分 |\n| 36 | single_signal.tex:L49 | `app:per_type_lp` | \"per-type ρ=-0.881\" | 同#23 | ✅ 充分 |\n| 37 | single_signal.tex:L52 | `sec:mechanistic` | \"Mechanistic evidence paragraph header\" | 同#1 | ✅ 充分 |\n| 38 | single_signal.tex:L53 | `app:esj` | \"ESJ AUROC 0.50–0.55 on Qwen3-8B\" | §Cross-Dataset Entailment Self-Judgment: 3-dataset ESJ vs agreement Table（~20行） | ✅ 充分 |\n| 39 | single_signal.tex:L56 | `app:esj` | \"cross-model ESJ validation\" | 同#38 | ✅ 充分 |\n| 40 | adaptive.tex:L9 | `sec:mechanistic` | \"self-verification methods in Appendix\" | 同#1 | ✅ 充分 |\n| 41 | adaptive.tex:L9 | `app:method_coverage` | \"Full coverage in Appendix\" | §Method Coverage Matrix: 7-method × 5-dataset/model table（~25行） | ✅ 充分 |\n| 42 | adaptive.tex:L21 | `app:dals` | \"DALS +0.71pp\" | §Degeneracy-Aware LP Selection: DALS algorithm, 3-dataset results, LOO τ sensitivity（~15行） | ✅ 充分 |\n| 43 | adaptive.tex:L23 | `app:supervised_combination` | \"LR/MLP/RF -0.4 to -3.1pp\" | 同#6 | ✅ 充分 |\n| 44 | adaptive.tex:L39 | `app:verifier_transfer` | \"cross-dataset transfer -0.76 to -1.02pp\" | §Entity-Level Verifier Transfer: LightGBM AUC, OOF gains, cross-dataset negative transfer（~8行） | ✅ 充分 |\n| 45 | discussion.tex:L5 | `app:freeform_ablation` | \"decoding modes\" | 同#30 | ✅ 充分 |\n| 46 | mechanistic.tex:L5 | `app:self_verification` | \"full results in Appendix\" | §Entity-Level Self-Verification Probes: ESJ/MRSC/LSC details, Table with metrics（~45行） | ✅ 充分 |\n| 47 | mechanistic.tex:L21 | `app:hidden_probe` | \"GroupKFold CV details\" | §Hidden State Probes: linear/MLP probe, cross-dataset, token-level aggregator（~35行 + Table） | ✅ 充分 |\n| 48 | mechanistic.tex:L24 | `app:hidden_probe` | \"MLP probe 13.9% oracle gap\" | 同#47 | ✅ 充分 |\n| 49 | theory.tex:L5 | `app:mbr_proof` | \"MBR proof\" | 同#9 | ✅ 充分 |\n| 50 | theory.tex:L7 | `app:fewnerd_epsilon` | \"LP compression threshold ε=0.05\" | ¶Few-NERD LP compression threshold sensitivity: elbow analysis（~45行） | ✅ 充分 |\n| 51 | theory.tex:L12 | `app:frontier_sc` | \"GPT-5.5 parse failures\" | §Frontier Model Self-Consistency: 4-model comparison table, parse failure handling, entity matching methodology（~40行） | ✅ 充分 |\n| 52 | theory.tex:L13 | `app:cross_scale` | \"degeneracy model-family-dependent\" | §Cross-Scale and Cross-Family Comparison: 10-row cross-scale table, few-shot analysis, degeneracy comparison, 4B ablation（~100行，多表） | ✅ 充分 |\n| 53 | theory.tex:L23 | `app:n_scaling` | \"40 of 58 inverse transitions\" | 同#17 | ✅ 充分 |\n| 54 | theory.tex:L25 | `app:degen_inverse` | \"degeneracy vs inverse scaling OR=0.109\" | ¶Degeneracy and inverse scaling: stratified table, 6 settings, Fisher exact test（~30行 + Table） | ✅ 充分 |\n| 55 | theory.tex:L26 | `app:fs_error` | \"few-shot QE improves but not construction\" | §Few-Shot Error Correlation Analysis: error overlap Jaccard, entity entropy comparison（~10行） | ✅ 充分 |\n| 56 | theory.tex:L33 | `app:bound_proof` | \"proof of degeneracy decomposition\" | §Degeneracy Decomposition: definitions, full proof, numerical verification table（~50行） | ✅ 充分 |\n| 57 | theory.tex:L50 | `app:alpha_crit` | \"Proposition entity selection bound\" | §Entity Selection Bound: Proof and Validation: proposition, proof, α_crit table（~60行） | ✅ 充分 |\n| 58 | theoretical.tex:L6 | `app:bound_proof` | \"proof in Appendix\" | 同#56 | ✅ 充分 |\n| 59 | checklist.tex:L24 | `app:training` | \"datasets cited, training framework\" | 同#15 | ✅ 充分 |\n| 60 | checklist.tex:L36 | `app:training` | \"dataset characteristics\" | 同#15 | ✅ 充分 |\n| 61 | checklist.tex:L48 | `app:training` | \"computing infrastructure\" | 同#15 | ✅ 充分 |\n| 62 | checklist.tex:L51 | `app:training` | \"hyperparameters\" | 同#15 | ✅ 充分 |\n| 63 | checklist.tex:L57 | `app:training` | \"LLaMA Factory, XGrammar\" | 同#15 | ✅ 充分 |\n| 64 | checklist.tex:L68 | `app:ai-assistants` | \"AI assistants disclosure\" | §Use of AI Assistants: Claude usage for code/writing/literature（~12行） | ✅ 充分 |\n\n## 问题列表（按严重程度排序）\n\n### 缺失的引用目标\n无。所有 33 个唯一 label 均在 appendix.tex 中定义。\n\n### 内容不足的 appendix 章节\n无。所有被引用的章节均包含实质性内容（表格、图表、证明或详细分析）。\n\n### 潜在注意事项\n\n1. **`sec:mechanistic` 使用 `sec:` 前缀而非 `app:` 前缀** — 该 section 位于 appendix.tex 内（L607），但 label 使用 `\\label{sec:mechanistic}` 而非 `\\label{app:mechanistic}`。这不会导致编译错误（LaTeX 不区分前缀），但与 appendix 其他 section 的命名惯例不一致。同时，mechanistic.tex 主文文件中也存在完全相同的内容（标题、段落、数据完全一致），说明该 section 既在主文中有独立文件，也在 appendix 中有副本。如果两者都被 `\\input` 编译，会产生 **duplicate label 警告**。需确认 main.tex 的 `\\input` 顺序中是否只引用了其中一个。\n\n2. **diagnostic.tex 与 method.tex 内容重叠** — diagnostic.tex 和 method.tex 均定义了 `\\section{...}\\label{sec:method}` 和 `\\label{sec:formulation}` 等 label，内容高度重叠但不完全相同。如果两个文件同时被编译，会产生 duplicate label。需确认只有一个被 `\\input`。\n\n3. **theoretical.tex 与 theory.tex 内容重叠** — theoretical.tex（9行，精简版 degeneracy bound）和 theory.tex（51行，完整 scaling analysis）均存在，且 theoretical.tex 定义了 `\\label{thm:degeneracy_bound}`，theory.tex L30 也定义了同名 label。需确认编译时只使用其中一个。\n\n### 建议\n- 确认 main.tex 的 `\\input` 列表中没有同时引用重叠文件（method/diagnostic、theoretical/theory、mechanistic 主文版/appendix 版）\n- 考虑将 `sec:mechanistic` 重命名为 `app:mechanistic` 以保持命名一致性（可选，不影响编译正确性）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/appendix_crossref_review.md",
    "content": "# Appendix 交叉引用审查\n\n## 统计\n- 主文引用 appendix 次数：64\n- 唯一 label 数：33\n- 所有 label 均存在：**是**\n\n## 逐条审查\n\n| # | 主文位置 | 引用 label | 主文语境 | Appendix 内容摘要 | 评估 |\n|---|---------|-----------|---------|-----------------|------|\n| 1 | introduction.tex:L8 | `sec:mechanistic` | \"hidden-state probe...AUROC 0.63–0.88; Appendix\" | §How Self-Verification Fails: ESJ/MRSC/LSC probes, hidden-state probe, introspection boundary（~30行正文 + Table） | ✅ 充分 |\n| 2 | introduction.tex:L11 | `app:re_extension` | \"RE reveals a distinct bottleneck (40% zero-F1)\" | §Exploratory Extension to RE: diagnostic framework, QE, selection, scale ablation, free-form decoding（~90行，多表） | ✅ 充分 |\n| 3 | introduction.tex:L14 | `app:re_extension` | \"RE F1 confounded by entity span errors\" | 同上 | ✅ 充分 |\n| 4 | introduction.tex:L28 | `sec:mechanistic` | \"Hidden-state probes reveal introspection boundary\" | 同#1 | ✅ 充分 |\n| 5 | method.tex:L6 | `app:notation` | \"notation in Appendix\" | §Notation: Table with all symbols（27行，完整符号表） | ✅ 充分 |\n| 6 | method.tex:L8 | `app:supervised_combination` | \"LP mean weight 0.78\" | §Supervised and Model-Internal Signal Analysis: LR/MLP/RF classifiers, DeBERTa verifier, grid-search（~12行详细分析） | ✅ 充分 |\n| 7 | method.tex:L33 | `app:fk_independence` | \"FK independence analysis\" | ¶FK independence permutation test: 3 configs, Table with t-stats, split-half r（~25行） | ✅ 充分 |\n| 8 | method.tex:L56 | `app:additional` | \"exclude instances with no gold annotations\" | §Additional Analyses: signal heatmap, per-relation diagnostic, capability stratification, length analysis, WNUT（~130行，多表多图） | ✅ 充分 |\n| 9 | method.tex:L80 | `app:mbr_proof` | \"proof in Appendix\" | §MBR Framework and Proof: formal proof of Proposition 1（~25行，完整证明） | ✅ 充分 |\n| 10 | diagnostic.tex:L8 | `app:notation` | \"notation in Appendix\" | 同#5 | ✅ 充分 |\n| 11 | diagnostic.tex:L10 | `app:supervised_combination` | \"LP mean weight 0.78, structural zero weight\" | 同#6 | ✅ 充分 |\n| 12 | diagnostic.tex:L22 | `app:token_signal` | \"length normalization +4.6 F1 points\" | §Token-Level Signal Comparison: mean vs cumulative LP, +4.6pp, Wilcoxon test（~8行） | ✅ 充分 |\n| 13 | diagnostic.tex:L34 | `app:fk_independence` | \"FK independence\" | 同#7 | ✅ 充分 |\n| 14 | diagnostic.tex:L41 | `app:additional` | \"instance exclusion\" | 同#8 | ✅ 充分 |\n| 15 | experiments_main.tex:L13 | `app:training` | \"LoRA fine-tuned...training details\" | §Training Configuration: Table with all hyperparameters, prompt template, constrained decoding details（~50行） | ✅ 充分 |\n| 16 | experiments_main.tex:L13 | `app:epoch_confound` | \"Few-NERD uses 3 epochs vs 5\" | §Epoch Confound Analysis: Few-NERD 3v5, SciERC 3/5/10 epoch curve, 2 tables（~70行） | ✅ 充分 |\n| 17 | experiments_main.tex:L14 | `app:n_scaling` | \"N∈{16,32,64} for scaling\" | §N-Scaling Detailed Analysis: signal quality vs N, ranking stability, inverse scaling, theta sweep tables（~140行，多表） | ✅ 充分 |\n| 18 | experiments_main.tex:L29 | `app:re_extension` | \"RE in Appendix\" | 同#2 | ✅ 充分 |\n| 19 | experiments_main.tex:L50 | `app:bootstrap_signal` | \"bootstrap CIs confirm the gap\" | §Bootstrap CI for Signal Comparisons: individual CIs, pairwise Δρ, seed-replication analysis（~45行，2 tables） | ✅ 充分 |\n| 20 | experiments_main.tex:L51 | `app:bootstrap_signal` | \"Holm-Bonferroni p_adj=0.013\" | 同#19 | ✅ 充分 |\n| 21 | experiments_main.tex:L76 | `app:epoch_confound` | \"5-epoch degeneracy 26%\" | 同#16 | ✅ 充分 |\n| 22 | experiments_main.tex:L78 | `app:pertype` | \"per-type MV degradation ρ=0.90\" | §Per-Type MV Analysis: 8 entity types, pretrained vs finetuned comparison, Table（~30行） | ✅ 充分 |\n| 23 | experiments_main.tex:L81 | `app:per_type_lp` | \"per-type LP ρ=-0.881\" | §Per-Entity-Type LP Selection: Few-NERD/CoNLL/SciERC per-type tables, degeneracy-headroom correlation（~70行，3 tables） | ✅ 充分 |\n| 24 | experiments_main.tex:L86 | `app:per_type_lp` | \"per-type LP (figure caption)\" | 同#23 | ✅ 充分 |\n| 25 | experiments_main.tex:L91 | `app:re_extension` | \"RE framework extends, 40% zero-F1\" | 同#2 | ✅ 充分 |\n| 26 | experiments_main.tex:L96 | `app:calibration` | \"signal rankings robust; calibration\" | §Calibration Analysis: reliability diagrams, ECE values（~12行 + figure） | ✅ 充分 |\n| 27 | experiments_main.tex:L103 | `app:theta_sweep` | \"θ stable in [0.15, 0.35]\" | §Entity Construction Threshold Sensitivity: 8-point sweep × 3 datasets, Table（~45行） | ✅ 充分 |\n| 28 | experiments_main.tex:L105 | `app:holm` | \"global k=57 Holm-Bonferroni\" | §Holm-Bonferroni Enumeration: complete 57-test table with raw p and p_adj（~90行） | ✅ 充分 |\n| 29 | experiments_main.tex:L107 | `app:epoch_confound` | \"5-epoch LP gains collapse\" | 同#16 | ✅ 充分 |\n| 30 | experiments_main.tex:L113 | `app:freeform_ablation` | \"decoding modes\" | §Free-Form Decoding Ablation: 3-panel table, LP distribution, selection F1, QE comparison（~110行） | ✅ 充分 |\n| 31 | experiments_main.tex:L114 | `app:n_scaling` | \"Qwen2.5-7B N=32 +3.85pp\" | 同#17 | ✅ 充分 |\n| 32 | single_signal.tex:L6 | `app:logprob_ties` | \"60% LP range below 0.041 nats\" | §Log-Probability Score Compression: CDF figure, tied fraction table, ε sweep, non-tied subset（~90行，多表多图） | ✅ 充分 |\n| 33 | single_signal.tex:L6 | `app:freeform_ablation` | \"free-form decoding yields identical LP\" | 同#30 | ✅ 充分 |\n| 34 | single_signal.tex:L39 | `app:bootstrap_signal` | \"MDE ≈1.5pp\" | 同#19 | ✅ 充分 |\n| 35 | single_signal.tex:L40 | `app:bootstrap_signal` | \"bootstrap CIs reported\" | 同#19 | ✅ 充分 |\n| 36 | single_signal.tex:L49 | `app:per_type_lp` | \"per-type ρ=-0.881\" | 同#23 | ✅ 充分 |\n| 37 | single_signal.tex:L52 | `sec:mechanistic` | \"Mechanistic evidence paragraph header\" | 同#1 | ✅ 充分 |\n| 38 | single_signal.tex:L53 | `app:esj` | \"ESJ AUROC 0.50–0.55 on Qwen3-8B\" | §Cross-Dataset Entailment Self-Judgment: 3-dataset ESJ vs agreement Table（~20行） | ✅ 充分 |\n| 39 | single_signal.tex:L56 | `app:esj` | \"cross-model ESJ validation\" | 同#38 | ✅ 充分 |\n| 40 | adaptive.tex:L9 | `sec:mechanistic` | \"self-verification methods in Appendix\" | 同#1 | ✅ 充分 |\n| 41 | adaptive.tex:L9 | `app:method_coverage` | \"Full coverage in Appendix\" | §Method Coverage Matrix: 7-method × 5-dataset/model table（~25行） | ✅ 充分 |\n| 42 | adaptive.tex:L21 | `app:dals` | \"DALS +0.71pp\" | §Degeneracy-Aware LP Selection: DALS algorithm, 3-dataset results, LOO τ sensitivity（~15行） | ✅ 充分 |\n| 43 | adaptive.tex:L23 | `app:supervised_combination` | \"LR/MLP/RF -0.4 to -3.1pp\" | 同#6 | ✅ 充分 |\n| 44 | adaptive.tex:L39 | `app:verifier_transfer` | \"cross-dataset transfer -0.76 to -1.02pp\" | §Entity-Level Verifier Transfer: LightGBM AUC, OOF gains, cross-dataset negative transfer（~8行） | ✅ 充分 |\n| 45 | discussion.tex:L5 | `app:freeform_ablation` | \"decoding modes\" | 同#30 | ✅ 充分 |\n| 46 | mechanistic.tex:L5 | `app:self_verification` | \"full results in Appendix\" | §Entity-Level Self-Verification Probes: ESJ/MRSC/LSC details, Table with metrics（~45行） | ✅ 充分 |\n| 47 | mechanistic.tex:L21 | `app:hidden_probe` | \"GroupKFold CV details\" | §Hidden State Probes: linear/MLP probe, cross-dataset, token-level aggregator（~35行 + Table） | ✅ 充分 |\n| 48 | mechanistic.tex:L24 | `app:hidden_probe` | \"MLP probe 13.9% oracle gap\" | 同#47 | ✅ 充分 |\n| 49 | theory.tex:L5 | `app:mbr_proof` | \"MBR proof\" | 同#9 | ✅ 充分 |\n| 50 | theory.tex:L7 | `app:fewnerd_epsilon` | \"LP compression threshold ε=0.05\" | ¶Few-NERD LP compression threshold sensitivity: elbow analysis（~45行） | ✅ 充分 |\n| 51 | theory.tex:L12 | `app:frontier_sc` | \"GPT-5.5 parse failures\" | §Frontier Model Self-Consistency: 4-model comparison table, parse failure handling, entity matching methodology（~40行） | ✅ 充分 |\n| 52 | theory.tex:L13 | `app:cross_scale` | \"degeneracy model-family-dependent\" | §Cross-Scale and Cross-Family Comparison: 10-row cross-scale table, few-shot analysis, degeneracy comparison, 4B ablation（~100行，多表） | ✅ 充分 |\n| 53 | theory.tex:L23 | `app:n_scaling` | \"40 of 58 inverse transitions\" | 同#17 | ✅ 充分 |\n| 54 | theory.tex:L25 | `app:degen_inverse` | \"degeneracy vs inverse scaling OR=0.109\" | ¶Degeneracy and inverse scaling: stratified table, 6 settings, Fisher exact test（~30行 + Table） | ✅ 充分 |\n| 55 | theory.tex:L26 | `app:fs_error` | \"few-shot QE improves but not construction\" | §Few-Shot Error Correlation Analysis: error overlap Jaccard, entity entropy comparison（~10行） | ✅ 充分 |\n| 56 | theory.tex:L33 | `app:bound_proof` | \"proof of degeneracy decomposition\" | §Degeneracy Decomposition: definitions, full proof, numerical verification table（~50行） | ✅ 充分 |\n| 57 | theory.tex:L50 | `app:alpha_crit` | \"Proposition entity selection bound\" | §Entity Selection Bound: Proof and Validation: proposition, proof, α_crit table（~60行） | ✅ 充分 |\n| 58 | theoretical.tex:L6 | `app:bound_proof` | \"proof in Appendix\" | 同#56 | ✅ 充分 |\n| 59 | checklist.tex:L24 | `app:training` | \"datasets cited, training framework\" | 同#15 | ✅ 充分 |\n| 60 | checklist.tex:L36 | `app:training` | \"dataset characteristics\" | 同#15 | ✅ 充分 |\n| 61 | checklist.tex:L48 | `app:training` | \"computing infrastructure\" | 同#15 | ✅ 充分 |\n| 62 | checklist.tex:L51 | `app:training` | \"hyperparameters\" | 同#15 | ✅ 充分 |\n| 63 | checklist.tex:L57 | `app:training` | \"LLaMA Factory, XGrammar\" | 同#15 | ✅ 充分 |\n| 64 | checklist.tex:L68 | `app:ai-assistants` | \"AI assistants disclosure\" | §Use of AI Assistants: Claude usage for code/writing/literature（~12行） | ✅ 充分 |\n\n## 问题列表（按严重程度排序）\n\n### 缺失的引用目标\n无。所有 33 个唯一 label 均在 appendix.tex 中定义。\n\n### 内容不足的 appendix 章节\n无。所有被引用的章节均包含实质性内容（表格、图表、证明或详细分析）。\n\n### 潜在注意事项\n\n1. **`sec:mechanistic` 使用 `sec:` 前缀而非 `app:` 前缀** — 该 section 位于 appendix.tex 内（L607），但 label 使用 `\\label{sec:mechanistic}` 而非 `\\label{app:mechanistic}`。这不会导致编译错误（LaTeX 不区分前缀），但与 appendix 其他 section 的命名惯例不一致。同时，mechanistic.tex 主文文件中也存在完全相同的内容（标题、段落、数据完全一致），说明该 section 既在主文中有独立文件，也在 appendix 中有副本。如果两者都被 `\\input` 编译，会产生 **duplicate label 警告**。需确认 main.tex 的 `\\input` 顺序中是否只引用了其中一个。\n\n2. **diagnostic.tex 与 method.tex 内容重叠** — diagnostic.tex 和 method.tex 均定义了 `\\section{...}\\label{sec:method}` 和 `\\label{sec:formulation}` 等 label，内容高度重叠但不完全相同。如果两个文件同时被编译，会产生 duplicate label。需确认只有一个被 `\\input`。\n\n3. **theoretical.tex 与 theory.tex 内容重叠** — theoretical.tex（9行，精简版 degeneracy bound）和 theory.tex（51行，完整 scaling analysis）均存在，且 theoretical.tex 定义了 `\\label{thm:degeneracy_bound}`，theory.tex L30 也定义了同名 label。需确认编译时只使用其中一个。\n\n### 建议\n- 确认 main.tex 的 `\\input` 列表中没有同时引用重叠文件（method/diagnostic、theoretical/theory、mechanistic 主文版/appendix 版）\n- 考虑将 `sec:mechanistic` 重命名为 `app:mechanistic` 以保持命名一致性（可选，不影响编译正确性）\n"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-24T02:36:20.533838+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/appendix_crossref_review.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-24T02:36:20.533973+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "appendix_crossref_review",
  "type": "report",
  "description": "Appendix 交叉引用完整性审查：33个唯一label全部存在，64处引用均有对应内容，无缺失或内容不足。附3个潜在duplicate label注意事项。",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/appendix_crossref_review.md",
  "tags": "['paper', 'appendix', 'crossref', 'review']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "appendix_crossref_review",
    "type": "report",
    "description": "Appendix 交叉引用完整性审查：33个唯一label全部存在，64处引用均有对应内容，无缺失或内容不足。附3个潜在duplicate label注意事项。",
    "project": "struct_self_consist_ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/appendix_crossref_review.md",
    "tags": "['paper', 'appendix', 'crossref', 'review']"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-24T02:36:20.534221+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_ca812f\", \"name\": \"appendix_crossref_review\", \"type\": \"report\", \"description\": \"Appendix 交叉引用完整性审查：33个唯一label全部存在，64处引用均有对应内容，无缺失或内容不足。附3个潜在duplicate label注意事项。\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/appendix_crossref_review.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T02:36:12.518213+00:00\", \"tags\": [\"paper\", \"appendix\", \"crossref\", \"review\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_appendix-cross-ref_20260524T023114",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 89 · 2026-05-24T02:36:20.534398+00:00_

审查完成。

**结果：所有 33 个唯一 appendix label 均存在，64 处主文引用全部有对应内容，无缺失或内容不足。**

3 个需注意的潜在问题：
1. `sec:mechanistic` 用了 `sec:` 前缀但实际位于 appendix 中，且 mechanistic.tex 主文文件与 appendix 内容重复——需确认编译时无 duplicate label
2. diagnostic.tex 与 method.tex 内容重叠（均定义 `sec:method`），需确认只编译其中一个
3. theoretical.tex 与 theory.tex 均定义 `thm:degeneracy_bound`，同理

报告已写入 `artifacts/appendix_crossref_review.md` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_appendix-cross-ref_20260524T023114"
}
```

</details>

---
