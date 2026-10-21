# audit maintext numbers

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_audit_maintext-numbers_20260524T042759.jsonl`
- **Structured JSON:** [`cefa5aeed71436922ebb.json`](../../sessions/ce/cefa5aeed71436922ebb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-24T04:44:58.506458+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T04:44:58.507663+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T04:44:58.507919+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
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

_source line 4 · 2026-05-24T04:44:58.508080+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T04:44:58.508279+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "struct_self_consist_ie",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T04:44:58.510646+00:00_

Error: result (524,087 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T04:44:58.510909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T04:44:58.511067+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.
3	We characterize when scaling succeeds and fails, using NER (four datasets, primarily 7--14B fine-tuned) as the primary analysis, with preliminary cross-task pilots (RE, SQL).
4	Quality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields no detectable gains (${<}1$\,pp; CI crosses zero), revealing a \textbf{correlation-selection gap}.
5	A diagnostic framework identifies two co-occurring conditions---\textit{degeneracy} (i.e., multiple outputs collapsing to identical predictions) and signal alignment collapse---that are jointly associated with scaling returns; cross-task exploration confirms task-specific failure modes.
6	Entity-level construction yields conditional gains ($+1.40$\,pp on Few-NERD under 3-epoch training; collapses at convergence; global Holm $p_{\text{adj}}{=}0.055$, suggestive; per-family $p_{\text{adj}}{=}0.006$, post-hoc family partition) but exhibits inverse scaling in most configurations.
7	The framework is primarily diagnostic, with limited predictive power for identifying favorable conditions, informing resource allocation decisions before investing in repeated inference.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T04:44:58.511242+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T04:44:58.511411+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T04:44:58.511558+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T04:44:58.511721+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T04:44:58.511887+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T04:44:58.512056+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T04:44:58.512242+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T04:44:58.512437+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T04:44:58.512585+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T04:44:58.512743+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T04:44:58.512906+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theoretical.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T04:44:58.513051+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T04:44:58.513202+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T04:44:58.513387+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T04:44:58.513588+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T04:44:58.513757+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T04:44:58.513893+00:00_

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
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-24T04:44:58.514042+00:00_

1	Our primary evidence is from English NER with fine-tuned 7--14B open-weight models; frontier models exhibit markedly different degeneracy profiles (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), and cross-task extensions (RE $n{=}397$, SQL $n{=}196$) are exploratory.
2	The framework is diagnostic, not causal: under global Holm--Bonferroni ($k{=}57$), the strongest construction claim reaches $p_{\text{adj}}{=}0.055$; our negative selection claims are bounded by statistical power (2--3 seeds, MDE ${\approx}1.5$\,pp).
3	Entity-level construction requires $N{\times}$ inference cost for modest gains ($+1$--$1.4$\,pp), and we use a single prompt template per task.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T04:44:58.514364+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n# Get all experiment IDs and their status/conclusion\nfor exp in result:\n    exp_id = exp.get('exp_id','?')\n    status = exp.get('status','?')\n    metrics = exp.get('metrics',{})\n    conclusion = exp.get('conclusion','')[:80] if exp.get('conclusion') else ''\n    if status == 'COMPLETED':\n        print(f'{exp_id} | {status} | metrics_keys={list(metrics.keys())[:5]} | {conclusion}')\n\" 2>&1 | head -80",
  "description": "Extract completed experiment IDs and metric keys from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n# Get all experiment IDs and their status/conclusion\nfor exp in result:\n    exp_id = exp.get('exp_id','?')\n    status = exp.get('status','?')\n    metrics = exp.get('metrics',{})\n    conclusion = exp.get('conclusion','')[:80] if exp.get('conclusion') else ''\n    if status == 'COMPLETED':\n        print(f'{exp_id} | {status} | metrics_keys={list(metrics.keys())[:5]} | {conclusion}')\n\" 2>&1 | head -80",
    "description": "Extract completed experiment IDs and metric keys from registry"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-24T04:44:58.514548+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    exp_id = exp.get('exp_id','?')
             ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T04:44:58.514684+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/tab_entity_construction*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/tab_entity_construction*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-24T04:44:58.514823+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T04:44:58.514945+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.csv",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.csv",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-24T04:44:58.515123+00:00_

artifacts/experiments/spider_sql/spider_databases/inn_1/data_csv/Rooms.csv
artifacts/experiments/spider_sql/spider_databases/inn_1/data_csv/Reservations_t.csv
artifacts/experiments/spider_sql/spider_databases/inn_1/data_csv/Reservations.csv
artifacts/experiments/spider_sql/spider_databases/flight_2/data_csv/airlines.csv
artifacts/experiments/spider_sql/spider_databases/flight_2/data_csv/airports100.csv
artifacts/experiments/spider_sql/spider_databases/flight_2/data_csv/flights.csv
artifacts/experiments/spider_sql/spider_databases/car_1/data_csv/countries.csv
artifacts/experiments/spider_sql/spider_databases/car_1/data_csv/car-names.csv
artifacts/experiments/spider_sql/spider_databases/car_1/data_csv/car-makers.csv
artifacts/experiments/spider_sql/spider_databases/car_1/data_csv/cars-data.csv
artifacts/experiments/spider_sql/spider_databases/car_1/data_csv/continents.csv
artifacts/experiments/spider_sql/spider_databases/car_1/data_csv/model-list.csv
artifacts/experiments/spider_sql/spider_databases/student_1/data_csv/teachers.csv
artifacts/experiments/spider_sql/spider_databases/student_1/data_csv/list.csv
artifacts/experiments/spider_sql/spider_databases/wine_1/data_csv/wine.csv
artifacts/experiments/spider_sql/spider_databases/wine_1/data_csv/grapes.csv
artifacts/experiments/spider_sql/spider_databases/wine_1/data_csv/appellations.csv
artifacts/experiments/spider_sql/spider_databases/formula_1/data_csv/drivers.csv
artifacts/experiments/spider_sql/spider_databases/formula_1/data_csv/pitStops.csv
artifacts/experiments/spider_sql/spider_databases/formula_1/data_csv/results.csv
artifacts/experiments/spider_sql/spider_databases/formula_1/data_csv/seasons.csv
artifacts/experiments/spider_sql/spider_databases/formula_1/data_csv/circuits.csv
artifacts/experiments/spider_sql/spider_databases/formula_1/data_csv/driverStandings.csv
artifacts/experiments/spider_sql/spider_databases/formula_1/data_csv/constructorResults.csv
artifacts/experiments/spider_sql/spider_databases/form
…[truncated 8747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-24T04:44:58.515335+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 500 /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt",
  "description": "Check registry file format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 500 /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt",
    "description": "Check registry file format"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-24T04:44:58.515486+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_fewnerd_pretrained_n32_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:49:35.691Z\", \"updated_at\": \"2026-05-23T12:00:19.327Z\", \"hypothesis\": \"Pretrained N-scaling rerun: FewNERD N=32 with Qwen2.5-7B-Instruct. v1 killed at 70% to prevent UnicodeEncodeError crash at save stage (no incremental checkpoint). Fix (errors='replace') deployed. Same hypothesis: tests pretrained MV advantage at 4�

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-24T04:44:58.515615+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper_provenance*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper_provenance*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-24T04:44:58.515738+00:00_

paper_provenance.lock
paper_provenance.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-24T04:44:58.515854+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/tab_*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/tab_*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-24T04:44:58.515968+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-24T04:44:58.516081+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_provenance.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_provenance.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-24T04:44:58.516634+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\\n    Signals for Test-Time Scaling in Information Extraction'\\n  version: 196\\n  generated_at: '2026-05-22T13:13:25.551495+00:00'\\n  source: manual provenance build by Paper Agent\\nclaims:\\n- id: c001_voting_rho_scierc_ner\\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\\n    artifact)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_rho_full\\n    value: 0.379\\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\\n    via exp_012_rerun_1024 (max_tokens=1024).\\n- id: c002_auroc_dissociation_scierc\\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\\n    Voting leads ρ (NER 0.379, RE 0.422)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.em_auroc\\n    value: 0.749\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.em_auroc\\n    value: 0.706\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_auroc\\n    value: 0.684\\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\\n    claim changed from \\\"entity voting achieves ρ=0.38 and AUROC=0.74\\\" to split ρ (Voting\\n    0.38) / AUROC (EM 0.75) claim.\\n- id: c003_sj_rho_scierc_ner\\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024
…[truncated 41600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-24T04:44:58.516826+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor exp_id, exp in exps.items():\n    status = exp.get('status','?')\n    metrics = exp.get('metrics',{})\n    if metrics:\n        print(f'=== {exp_id} ({status}) ===')\n        for k,v in list(metrics.items())[:20]:\n            print(f'  {k}: {v}')\n        print()\n\" 2>&1 | head -200",
  "description": "Extract experiments with metrics from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor exp_id, exp in exps.items():\n    status = exp.get('status','?')\n    metrics = exp.get('metrics',{})\n    if metrics:\n        print(f'=== {exp_id} ({status}) ===')\n        for k,v in list(metrics.items())[:20]:\n            print(f'  {k}: {v}')\n        print()\n\" 2>&1 | head -200",
    "description": "Extract experiments with metrics from registry"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-24T04:44:58.517030+00:00_

=== exp_fewnerd_pretrained_n32_s42_v2 (DONE) ===
  greedy_f1: 0.539
  mv_f1: 0.577
  mv_delta_pp: 3.85
  lp_f1: 0.529
  lp_delta_pp: -1.03
  oracle_f1: 0.705
  oracle_delta_pp: 16.56
  degeneracy_rate: 5.42
  capture_rate: 19
  sj_rho: 0.456
  n_instances_gold_nonempty: 32565
  subset: gold-nonempty

=== exp_fewnerd_pretrained_n16_s42_v2 (DONE) ===
  greedy_f1: 0.5373
  mv_strict_f1: 0.5779
  mv_delta_strict_pp: 4.06
  mv_incl_f1: 0.5722
  oracle_f1: 0.6786
  degeneracy_rate: 0.076
  alpha_crit_eff_strict: 0.4398
  alpha_crit_strict: 0.4064
  mv_capture_rate: 0.2876
  n_total: 37648
  n_gold_nonempty: 32565
  greedy_f1_all: 0.5109
  oracle_f1_all: 0.6433
  sj_rho_full: 0.453
  fk_rho_full: 0.401
  lp_rho_full: 0.192
  structural_beats_surface: True
  note: Primary metrics (greedy/mv/oracle) computed on gold-nonempty instances (n=32565) via recompute_alpha_crit_unified.py. _all suffix = full instances incl gold-empty.

=== exp_scierc_n8_s456 (DONE) ===
  greedy_f1: 0.6657
  mv_f1: 0.6573
  mv_delta_pp: -0.84
  lp_f1: 0.6626
  lp_delta_pp: -0.31
  degeneracy_rate: 0.12
  agreement_rate: 0.6597
  oracle_f1: 0.7733
  fleiss_kappa: 0.3864
  soft_jaccard: 0.6939
  note: MV/LP metrics from legacy pipeline. Superseded by MF4v2 unified recompute (see exp_fewnerd_mf4_s42 series). MF4v2 SciERC 3-seed MV delta: -0.74±0.46pp (all negative).

=== exp_scierc_n8_s123 (DONE) ===
  greedy_f1: 0.6613
  mv_f1: 0.6648
  mv_delta_pp: 0.34
  lp_f1: 0.6698
  lp_delta_pp: 0.85
  degeneracy_rate: 0.116
  agreement_rate: 0.6646
  oracle_f1: 0.7794
  fleiss_kappa: 0.3847
  soft_jaccard: 0.6979
  note: MV/LP metrics from legacy pipeline. Superseded by MF4v2 unified recompute (see exp_fewnerd_mf4_s42 series). MF4v2 SciERC 3-seed MV delta: -0.74±0.46pp (all negative).

=== exp_scierc_n8_s3141 (DONE) ===
  greedy_f1: 0.6609
  oracle_f1: 0.7645
  oracle_headroom: 0.1036
  fleiss_kappa_mean: 0.2906
  soft_jaccard_mean: 0.6265
  rho_sj_f1_full: 0.3477
  rho_kappa_f1_full: 0.2074
  rho_sj_f1_cond: 0.2
…[truncated 5158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-24T04:44:58.517256+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find experiments related to entity construction, selection, and fewnerd\ntargets = ['entity_construction', 'exp_021', 'selection', 'fewnerd_3ep', 'cross_model', 'spider', 'scierc_selection', 'exp_010', 'wnut', 'dals', 'verifier', 'lgb', 'alpha_crit', 'n_scaling', 'inverse', 'epoch_confound']\nfor exp_id, exp in exps.items():\n    for t in targets:\n        if t in exp_id.lower():\n            metrics = exp.get('metrics',{})\n            print(f'=== {exp_id} ({exp.get(\\\"status\\\",\\\"?\\\")}) ===')\n            for k,v in list(metrics.items())[:30]:\n                print(f'  {k}: {v}')\n            hyp = exp.get('hypothesis','')[:120]\n            if hyp: print(f'  hypothesis: {hyp}')\n            print()\n            break\n\" 2>&1 | head -200",
  "description": "Extract entity_construction and related experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find experiments related to entity construction, selection, and fewnerd\ntargets = ['entity_construction', 'exp_021', 'selection', 'fewnerd_3ep', 'cross_model', 'spider', 'scierc_selection', 'exp_010', 'wnut', 'dals', 'verifier', 'lgb', 'alpha_crit', 'n_scaling', 'inverse', 'epoch_confound']\nfor exp_id, exp in exps.items():\n    for t in targets:\n        if t in exp_id.lower():\n            metrics = exp.get('metrics',{})\n            print(f'=== {exp_id} ({exp.get(\\\"status\\\",\\\"?\\\")}) ===')\n            for k,v in list(metrics.items())[:30]:\n                print(f'  {k}: {v}')\n            hyp = exp.get('hypothesis','')[:120]\n            if hyp: print(f'  hypothesis: {hyp}')\n            print()\n            break\n\" 2>&1 | head -200",
    "description": "Extract entity_construction and related experiments from registry"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-24T04:44:58.517464+00:00_

=== exp_a1_spider_sql_sc (PREPARING) ===
  hypothesis: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies t

=== exp_b2_v4_inverse_frequency (PREPARING) ===
  variant_a_replace_fold3_lgb_auc: 0.834
  variant_a_replace_fold3_ece: 0.2188
  variant_a_f1_delta: -0.013
  variant_b_augment_fold3_lgb_auc: 0.8541
  variant_b_augment_fold3_ece: 0.1934
  variant_b_f1_delta: -0.009
  sj_ifw_std_reduction: 54% (0.138→0.063)
  ac_ifw_std_reduction: 10% (0.122→0.110)
  verdict: IFW improves stability but reduces discriminative power. Augment variant neutral. Replace variant harmful.
  hypothesis: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-d

=== exp_b2_entity_verifier (PREPARING) ===
  oof_auc: 0.9233
  oof_path_a_f1_delta: 0.003
  oof_path_b_f1_delta: -0.0157
  oof_greedy_f1: 0.8216
  oof_path_a_f1: 0.8246
  oof_majority_vote_f1: 0.8048
  leakage_pct: 91
  original_delta_pp: 3.62
  oof_delta_pp: 0.3
  per_dataset: {'scierc': '+1.28pp', 'conll': '+0.55pp', 'fewnerd': '+0.02pp'}
  verdict: B2 verifier gain was 91% leakage. OOF Path A +0.30pp not significant. NOT suitable for paper §5.
  n_inverse_scaling_validation: {'subset_n': 4351, 'full_n': 32565, 'subset_greedy_f1': 0.7926, 'full_greedy_f1': 0.7913, 'verdict': 'Not a bug. Representative subset. Paper should note subset size.'}
  hypothesis: An XGBoost/LightGBM entity-level verifier trained on agreement_count, VC, LP features can predict whether entity candida

=== exp_spider_sc_pilot (DONE) ===
  n_instances: 196
  n_target: 200
  n_skipped: 2
  n_samples: 8
  temperature: 1
  model: gpt-5.5
  greedy_acc: 0.7653
  mv_acc: 0.7704
  oracle_acc: 0.8061
  mv_gain_pp: 0.51
  degeneracy_rate: 0.8724
  spearman_rho: 0.5501
  spearman_p: 6.77e-17
  kendall_tau: 0.5259
  F1_degeneracy_rate: 0.872
  F2_low_agreement_rate: 0
  F3_high_agree_wrong_rate: 0.082
  F4_selection_gap_rate: 0
  sc_succe
…[truncated 9686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-24T04:44:58.517627+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find exp_021 and fewnerd LP selection source\nfor exp_id, exp in exps.items():\n    if 'exp_021' in exp_id or ('fewnerd' in exp_id.lower() and 'full' in exp_id.lower()):\n        metrics = exp.get('metrics',{})\n        print(f'=== {exp_id} ({exp.get(\\\"status\\\",\\\"?\\\")}) ===')\n        for k,v in list(metrics.items())[:30]:\n            print(f'  {k}: {v}')\n        hyp = exp.get('hypothesis','')[:200]\n        if hyp: print(f'  hypothesis: {hyp}')\n        note = exp.get('note','')[:200]\n        if note: print(f'  note: {note}')\n        print()\n\" 2>&1",
  "description": "Find exp_021 fewnerd full experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find exp_021 and fewnerd LP selection source\nfor exp_id, exp in exps.items():\n    if 'exp_021' in exp_id or ('fewnerd' in exp_id.lower() and 'full' in exp_id.lower()):\n        metrics = exp.get('metrics',{})\n        print(f'=== {exp_id} ({exp.get(\\\"status\\\",\\\"?\\\")}) ===')\n        for k,v in list(metrics.items())[:30]:\n            print(f'  {k}: {v}')\n        hyp = exp.get('hypothesis','')[:200]\n        if hyp: print(f'  hypothesis: {hyp}')\n        note = exp.get('note','')[:200]\n        if note: print(f'  note: {note}')\n        print()\n\" 2>&1",
    "description": "Find exp_021 fewnerd full experiment"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-24T04:44:58.517807+00:00_

=== exp_021_fewnerd_n8_seed456 (DONE) ===
  degen_rate: 0.1212
  degen_rate_source: unified_metrics_constant_f1_gold_filtered
  instance_count: 37648
  n_valid: 32565
  n_gold_empty: 5083
  ner_greedy_f1: 0.7888
  ner_oracle_f1: 0.881
  rho_fk_ner: 0.1632
  rho_sj_ner: 0.313
  sample_f1_pct_zero: 19.32
  hypothesis: Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.

=== exp_021_fewnerd_n8_seed123 (DONE) ===
  degen_rate: 0.1312
  degen_rate_source: unified_metrics_constant_f1_gold_filtered
  instance_count: 37648
  n_valid: 32565
  n_gold_empty: 5083
  ner_greedy_f1: 0.7885
  ner_oracle_f1: 0.8892
  rho_fk_ner: 0.1602
  rho_sj_ner: 0.3083
  sample_f1_pct_zero: 20.39
  hypothesis: Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.

=== exp_021_fewnerd_full (DONE) ===
  total_steps: 6177
  train_loss: 0.048
  eval_loss: 0.0275
  train_runtime: 3h57m
  epochs: 3
  final_checkpoint: output/exp_021_fewnerd_full/checkpoint-6177
  adapter_path: output/exp_021_fewnerd_full/adapter_model.safetensors
  inference_instances: 37648
  inference_filtered: 32565
  inference_n_samples: 8
  greedy_macro_f1: 0.7478
  oracle_macro_f1: 0.8719
  headroom: 0.124
  zero_f1_rate: 0.119
  degeneracy_rate: 0.101
  lp_within_range_mean: 0.0879
  lp_within_range_median: 0.0662
  lp_global_rho: 0.4215
  lp_cond_rho: 0.4225
  sj_global_rho: 0.3002
  sj_cond_rho: 0.2937
  fk_global_rho: 0.3132
  fk_cond_rho: 0.3093
  em_global_rho: 0.2871
  em_cond_rho: 0.271
  vc_global_rho: 0.3858
  vc_cond_rho: 0.3234
  lp_selection_delta_pp: 1.36
  vc_selection_delta_pp: -1.79
  sj_selection_delta_pp: -2.14
  hypothesis: Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect lo

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-24T04:44:58.518204+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find exp_016, exp_012, DALS, N scaling experiments\ntargets = ['exp_016', 'exp_012', 'dals', 'n_scaling', 'n32', 'n64', 'fewnerd_selection', 'scierc_constr', 'conll_n8', 'alpha_crit', 'frontier', 'gpt']\nfor exp_id, exp in exps.items():\n    for t in targets:\n        if t in exp_id.lower():\n            metrics = exp.get('metrics',{})\n            if metrics:\n                print(f'=== {exp_id} ({exp.get(\\\"status\\\",\\\"?\\\")}) ===')\n                for k,v in list(metrics.items())[:25]:\n                    print(f'  {k}: {v}')\n                print()\n            break\n\" 2>&1 | head -250",
  "description": "Find exp_016, DALS, N-scaling, alpha_crit experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find exp_016, exp_012, DALS, N scaling experiments\ntargets = ['exp_016', 'exp_012', 'dals', 'n_scaling', 'n32', 'n64', 'fewnerd_selection', 'scierc_constr', 'conll_n8', 'alpha_crit', 'frontier', 'gpt']\nfor exp_id, exp in exps.items():\n    for t in targets:\n        if t in exp_id.lower():\n            metrics = exp.get('metrics',{})\n            if metrics:\n                print(f'=== {exp_id} ({exp.get(\\\"status\\\",\\\"?\\\")}) ===')\n                for k,v in list(metrics.items())[:25]:\n                    print(f'  {k}: {v}')\n                print()\n            break\n\" 2>&1 | head -250",
    "description": "Find exp_016, DALS, N-scaling, alpha_crit experiments"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-24T04:44:58.518465+00:00_

=== exp_fewnerd_pretrained_n32_s42_v2 (DONE) ===
  greedy_f1: 0.539
  mv_f1: 0.577
  mv_delta_pp: 3.85
  lp_f1: 0.529
  lp_delta_pp: -1.03
  oracle_f1: 0.705
  oracle_delta_pp: 16.56
  degeneracy_rate: 5.42
  capture_rate: 19
  sj_rho: 0.456
  n_instances_gold_nonempty: 32565
  subset: gold-nonempty

=== exp_fewnerd_pretrained_n32_s42 (DONE) ===
  kill_reason: UnicodeEncodeError crash prevention: no incremental save, save stage would crash after 16h inference. Killed at 70% to avoid 5h GPU waste.
  progress_at_kill: 70% (838K/1.2M prompts, ~11h elapsed)
  fix_status: sampling.py errors='replace' already deployed on autodl-5090-c

=== exp_fewnerd_n32_s42 (DONE) ===
  greedy_f1: 0.7914
  mv_strict_f1: 0.7818
  mv_delta_strict_pp: -0.96
  mv_delta_unified_pp: -0.91
  unified_greedy_f1: 0.7909
  oracle_f1: 0.9305
  degeneracy_rate: 0.014

=== exp_conll_pretrained_n64_s42 (DONE) ===
  greedy_f1: 0.6005
  mv_strict_f1: 0.6316
  mv_delta_strict_pp: 3.11
  oracle_f1: 0.7703
  degeneracy_rate: 0.143

=== exp_scierc_pretrained_n64_s42 (DONE) ===
  greedy_f1: 0.2432
  mv_strict_f1: 0.2717
  mv_delta_strict_pp: 2.85
  oracle_f1: 0.5017
  degeneracy_rate: 0
  alpha_crit_eff_strict: 0.122

=== exp_conll_n32_s456 (DONE) ===
  greedy_f1: 0.9117
  mv_strict_f1: 0.9167
  mv_delta_strict_pp: 0.51
  degeneracy_rate: 0.401
  oracle_f1: 0.9686
  alpha_crit_eff_strict: 0.7614

=== exp_scierc_n32_s456 (DONE) ===
  greedy_f1: 0.6661
  mv_strict_f1: 0.6644
  mv_delta_strict_pp: -0.17
  degeneracy_rate: 0.04

=== exp_conll_n64_s42 (DONE) ===
  greedy_f1: 0.912
  mv_strict_f1: 0.9184
  mv_delta_strict_pp: 0.64
  oracle_f1: 0.9751
  degeneracy_rate: 0.306

=== exp_conll_pretrained_n32_s42 (DONE) ===
  greedy_f1: 0.5975
  mv_strict_f1: 0.6296
  mv_delta_strict_pp: 3.21
  oracle_f1: 0.7493
  degeneracy_rate: 0.188
  alpha_crit_eff_strict: 0.5657

=== exp_conll_n32_s123 (DONE) ===
  greedy_f1: 0.9123
  mv_strict_f1: 0.9177
  mv_delta_strict_pp: 0.55
  oracle_f1: 0.9717
  degeneracy_rate: 0.379
  a
…[truncated 7883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-24T04:44:58.518796+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/audit_maintext_numbers.md",
  "content": "# 主文数字审计\n\n审计日期: 2026-05-24\n审计范围: docs/paper/sections/ 下所有主文 tex 文件\nRegistry 数据: 完整读取并交叉验证\n\n---\n\n## Abstract\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| AUROC 0.82 | \"AUROC up to $0.82$\" | exp_002 (em_auroc_full=0.8156) | ✅ .816→.82 (2dp rounding) | = Intro \"AUROC $0.82$\"; Tab quality_estimation CoNLL EM .816 |\n| <1 pp | \"selection yields no detectable gains (${<}1$\\,pp)\" | exp_016_rerun_1024_bootstrap | ✅ | = Intro/§4 consistent |\n| +1.40 pp | \"$+1.40$\\,pp on Few-NERD\" | exp_entity_construction (n8_fair_cv) | ⚠️ 见问题 #1 | = Intro +1.40; §4.5 +1.40±0.51; fig_overview caption +1.40 |\n| 3-epoch | \"under 3-epoch training\" | exp_021_fewnerd_full (epochs=3) | ✅ | = Intro/§4 consistent |\n| p_adj=0.055 | \"global Holm $p_{\\text{adj}}{=}0.055$\" | ⚠️ UNTRACED (统计结果，非直接实验 metric) | — | = Intro; §4.5 (k=57); limitations ✅ 一致 |\n| p_adj=0.006 | \"per-family $p_{\\text{adj}}{=}0.006$\" | ⚠️ UNTRACED | — | = Intro; §4.5 (k=10) ✅ 一致 |\n| degeneracy + signal alignment collapse | 定性描述 | N/A | ✅ | 一致 |\n\n## Introduction\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| ρ up to 0.45 | \"ρ up to $0.45$\" | exp_002 (em_rho_full=0.4507) | ✅ .451→.45 | = Tab quality_estimation CoNLL EM ρ=.451 |\n| AUROC 0.82 | \"AUROC $0.82$; Table quality_estimation\" | exp_002 (em_auroc_full=0.8156) | ✅ | = Abstract ✅ |\n| MV <1 pp at N=64 | \"MV ${<}1$ percentage point (pp) even at $N{=}64$\" | exp_conll_n64_s42 (mv_delta=0.64pp) | ✅ | = Fig n_scaling caption \"+0.6pp at N=64\" |\n| AUROC 0.63–0.88 | hidden-state probe | ⚠️ UNTRACED (appendix mechanistic) | — | = §4.1 line 53 一致 |\n| ESJ AUROC 0.51 | entity self-judgment | exp_esj_qwen3_all (scierc esj_auroc=0.512) | ✅ | = Tab method_summary AUROC 0.51 |\n| 12–68% | \"degeneracy ($12$--$68$\\%)\" | Tab fewnerd: SciERC 12.2%, WNUT 67.9% | ✅ 12.2→12, 67.9→68 | = Discussion ✅ |\n| LP +1.39 pp | \"LP $+1.39$\\,pp on Few-NERD\" | exp_021_fewnerd_full (lp_delta=1.36, seed42) | ⚠️ 见问题 #2 | = §4.1 +1.39; Tab fewnerd +1.39 |\n| MV +0.6 pp | \"MV $+0.6$\\,pp on CoNLL\" | exp_conll_n64_s42 (mv_delta=0.64pp) | ✅ .64→.6 | = Fig n_scaling; §4.3 |\n| +1.40 pp (construction) | \"Exploratory entity-level construction yields conditional improvement ($+1.40$\\,pp on Few-NERD, 3-epoch\" | Same as abstract | ⚠️ 见问题 #1 | = Abstract; §4.5 |\n| p_adj=0.055 | \"global Holm $p_{\\text{adj}}{=}0.055$\" | ⚠️ UNTRACED | — | = Abstract; §4.5; limitations ✅ |\n| p_adj=0.006 | \"per-family $p_{\\text{adj}}{=}0.006$\" | ⚠️ UNTRACED | — | = Abstract; §4.5 ✅ |\n| 87.2% | \"SQL parsing ($87.2$\\% degeneracy)\" | exp_spider_sc_pilot (F1_degeneracy=0.872) | ✅ | 仅出现一次 |\n| 40% zero-F1 | \"RE…$40$\\% zero-F1\" | provenance c006 notes \"paper uses 40% from primary config\"; registry shows 44.3% at N=16 | ⚠️ 见问题 #3 | = §4.3 \"40%\" 一致 |\n| ρ up to 0.47 | \"\\citet{yao2026consistency} report…$\\rho$ up to 0.47\" | 引用他人数据 | N/A | 仅引用 |\n| LP mean weight 0.78 | \"ensemble optimization assigns LP mean weight $0.78$\" | ⚠️ UNTRACED (appendix supervised_combination) | — | 仅出现一次 |\n| 3–12% recovery ratio | \"3--12\\% recovery ratio\" | ⚠️ UNTRACED (理论计算) | — | = theoretical.tex; theory.tex ✅ |\n| α=0.000–0.121 | \"$\\alpha$ approaches zero ($0.000$--$0.121$)\" | ⚠️ UNTRACED (理论计算) | — | = theory.tex line 38 ✅ |\n| +3.85 pp MV | \"pretrained Qwen2.5-7B at $N{=}32$ achieves $+3.85$\\,pp MV gain\" | exp_fewnerd_pretrained_n32_s42_v2 (mv_delta=3.85) | ✅ | 仅出现一次 |\n| D=5.4% | \"$D{=}5.4$\\%\" | exp_fewnerd_pretrained_n32_s42_v2 (degen=5.42) | ✅ 5.42→5.4 | 仅出现一次 |\n\n## §3 Diagnostic Framework\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| +4.6 F1 points | \"length normalization eliminates length bias ($+4.6$ F1 points)\" | ⚠️ UNTRACED (appendix token_signal) | — | 仅出现一次 |\n| n=529 | \"n=529 on SciERC\" | exp_012_rerun_1024 (ner_full n=529) | ✅ | = Tab quality_estimation caption; Tab fewnerd SciERC n=529 |\n| n=2,756 | \"n=2,756 on CoNLL\" | exp_017_llama_conll_infer data | ✅ | = Tab fewnerd CoNLL n=2,756 |\n| 9–26% | \"Entity-set exact-match degeneracy…($9$--$26$\\%)\" | exp_fewnerd_mf4_s* (8.1%–9.3% at 5-epoch) | ⚠️ 见问题 #4 | 脚注内部使用 |\n| 13–31% | \"vs.\\ $13$--$31$\\% constant-F1\" | exp_021 seeds (10.1%–13.1% at 3-epoch) | ⚠️ 部分匹配 | 脚注内部使用 |\n\n## §4.1 Single-Signal Selection Results\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| 60% LP range <0.041 | \"60\\% of SciERC instances showing within-instance LP range below 0.041 nats\" | ⚠️ UNTRACED (appendix logprob_ties) | — | 仅出现一次 |\n| 0.97× | \"free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97$)\" | exp_conll_freeform_n8_s42 / exp_fewnerd_freeform_n8_s42 | ⚠️ 无法直接确认 0.97 | 仅出现一次 |\n| Tab selection: Oracle 0.775±0.001 | Best-of-N table | exp_016_rerun_1024_bootstrap (oracle=0.776) | ⚠️ .776 vs .775 | 仅 Tab selection |\n| Tab selection: Greedy 0.645±0.001 | Best-of-N table | exp_016_rerun_1024_bootstrap (greedy=0.644) | ⚠️ .644 vs .645 | ❌ 见问题 #5 |\n| Tab selection: LP 0.647±0.005 | LP selection F1 | exp_016_rerun_1024_bootstrap | ⚠️ 间接 | 仅 Tab selection |\n| Tab selection: LP p=.29 | \"LP achieves $+0.2$\\,pp ($p{=}0.29$)\" | exp_016_rerun_1024_bootstrap (permutation_p=0.39) | ❌ 见问题 #6 | Tab vs text 一致 (.29) |\n| ρ up to 0.38 | \"Despite $\\rho$ up to 0.38\" | exp_012_rerun_1024 (vc_rho=0.3792) | ✅ .379→.38 | = Tab quality_estimation VC ρ=.379 |\n| +13.0 pp headroom | \"the oracle shows 13.0\\,pp headroom\" | Tab selection: 0.775-0.645=0.130=13.0pp | ✅ | = fig_selection_gap caption \"+13.0pp\" ✅ |\n| MDE ≈1.5 pp | \"below MDE (${\\approx}$1.5\\,pp at $n{=}529$, 2--3 seeds\" | ⚠️ UNTRACED (统计计算) | — | = limitations ✅ |\n| LP +1.39 pp (Few-NERD) | \"LP achieves $+1.39$\\,pp ($p{<}0.001$; Holm $p_{\\text{adj}}{=}0.021$, k=21)\" | exp_021_fewnerd_full (1.36 for seed42) | ⚠️ 见问题 #2 | = Tab fewnerd; Intro |\n| p_adj=0.021, k=21 | selection family correction | provenance C143 has p_adj=0.019 k=19 | ⚠️ 见问题 #7 | 仅出现一次 |\n| p_adj=0.055 (global k=57) | footnote | ⚠️ UNTRACED | — | = Abstract; §4.5; limitations |\n| 13.0% degeneracy (Few-NERD) | \"low degeneracy (13.0\\%)\" | 见问题 #8 | ⚠️ | = Tab fewnerd 13.0% |\n| 12.2% (SciERC) | \"SciERC 12.2\\%\" | exp_012_rerun_1024 (degen=0.1777?) | ⚠️ 见问题 #9 | = Tab fewnerd 12.2% ✅ |\n| 61.7% (CoNLL) | \"CoNLL 61.7\\%\" | ⚠️ UNTRACED | — | = Tab fewnerd 61.7% ✅ |\n| VC −1.79, SJ −2.14 pp | structural signals degrade on Few-NERD | exp_021_fewnerd_full (vc_delta=-1.79, sj_delta=-2.14) | ✅ | = §4.3 一致 |\n| ρ=0.052, n=23, p=0.81 | degeneracy-LP across configs | ⚠️ UNTRACED | — | = §4.3 Fig degeneracy_scatter ✅ |\n| ρ=−0.881 | within-dataset degen-LP | ⚠️ UNTRACED | — | = §4.3 ✅ |\n| MRSC −3.1 pp | multi-round refinement | ⚠️ UNTRACED (appendix mechanistic) | — | = Tab method_summary ✅ |\n| LSC −3.5 pp | latent centroid selection | ⚠️ UNTRACED (appendix mechanistic) | — | = Tab method_summary ✅ |\n| ESJ AUROC 0.50–0.55 (Qwen3-8B) | cross-model ESJ | exp_esj_qwen3_all (scierc=0.512, fewnerd=0.495) | ✅ | 仅出现一次 |\n\n## §4.2–4.3 Experiments (experiments_main.tex)\n\n### Tab quality_estimation\n\n| 数字 | 来源 exp_id | 验证 |\n|------|------------|------|\n| SciERC VC ρ=.379 | exp_012_rerun_1024 (voting_conf rho=0.3792) | ✅ |\n| SciERC SJ ρ=.360 | exp_012_rerun_1024 (SJ rho=0.3599) | ✅ |\n| SciERC FK ρ=.267 | exp_012_rerun_1024 (FK rho=0.2665) | ✅ |\n| SciERC EM ρ=.295 | exp_012_rerun_1024 (EM rho=0.2945) | ✅ |\n| SciERC LP ρ=.205 | exp_012_rerun_1024 (LP rho=0.2052) | ✅ |\n| SciERC VC AUC=.684 | exp_012_rerun_1024 (voting_conf AUROC=0.6841) | ✅ |\n| SciERC SJ AUC=.692 | exp_012_rerun_1024 (SJ AUROC=0.6917) | ✅ |\n| SciERC FK AUC=.629 | exp_012_rerun_1024 (FK AUROC=0.629) | ✅ |\n| **SciERC EM AUC=.631** | **exp_012_rerun_1024 (EM AUROC=0.7493)** | **❌ 见问题 #10** |\n| SciERC LP AUC=.578 | exp_012_rerun_1024 (LP AUROC=0.5783) | ✅ |\n| CoNLL Qwen EM ρ=.451 | exp_002 (em_rho_full=0.4507) | ✅ |\n| CoNLL Qwen EM AUC=.816 | exp_002 (em_auroc_full=0.8156) | ✅ |\n| CoNLL Qwen SJ ρ=.436 | exp_002 (sj_rho_full=0.4357) | ✅ |\n| CoNLL LLaMA SJ ρ=.431 | exp_017_llama_conll_infer (SJ_rho=0.4314) | ✅ |\n| CoNLL LLaMA LP AUC=.761 | exp_017_llama_conll_infer (logprob_AUROC=0.761) | ✅ |\n\n### Tab fewnerd (cross-dataset LP selection)\n\n| 数字 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|------------|------|-----------|\n| WNUT n=1,287 | exp_003_wnut17_eval (n=1287) | ✅ | = §4.2 |\n| WNUT Greedy .452 | exp_wnut17_qwen25_7b (seed42 greedy=0.4524) | ✅ | — |\n| WNUT Degen 67.9% | ⚠️ UNTRACED (N=8 data; registry WNUT experiments are N=16) | — | = text 12–68% upper bound |\n| WNUT LP ρ=−.446 | ⚠️ UNTRACED (registry has −.414/−.409 at N=16) | — | — |\n| CoNLL n=2,756 | consistent | ✅ | = §3 |\n| CoNLL Greedy .908 | ⚠️ UNTRACED for N=8 Qwen | — | — |\n| CoNLL Degen 61.7% | ⚠️ UNTRACED | — | = §4.1 ✅ |\n| CoNLL LP ρ=.302 | ⚠️ ≠ Tab quality_estimation LP ρ=.316 | ⚠️ 见问题 #11 | — |\n| **SciERC Greedy .663** | **exp_scierc_n8_s* (greedy ≈0.661–0.666)** | ✅ matches multi-seed | **❌ ≠ Tab selection Greedy .645 见问题 #5** |\n| SciERC Degen 12.2% | ⚠️ PARTIALLY TRACED | — | = §4.1 ✅ |\n| **SciERC LP ρ=.159** | ⚠️ UNTRACED | — | **❌ ≠ Tab quality_estimation LP ρ=.205 见问题 #11** |\n| **SciERC LP Δ=+0.61 pp** | ⚠️ UNTRACED | — | **❌ ≠ §4.1 text \"+0.2pp\" 见问题 #5** |\n| Few-NERD n=32,565 | exp_021_fewnerd_full (filtered=32565) | ✅ | — |\n| Few-NERD Greedy .748 | exp_021_fewnerd_full (greedy=0.7478) | ✅ | — |\n| Few-NERD Degen 13.0% | ⚠️ 见问题 #8 | — | = §4.1 ✅ |\n| Few-NERD LP ρ=.220 | ⚠️ ≠ exp_021 lp_global_rho=0.4215 | ⚠️ 见问题 #12 | — |\n| Few-NERD LP Δ=+1.39 pp | exp_021_fewnerd_full (1.36 seed42) | ⚠️ 见问题 #2 | = §4.1; Intro |\n\n### Other §4 numbers\n\n| 数字 | 上下文 | 来源 | 验证 | 跨位置一致 |\n|------|--------|------|------|-----------|\n| SciERC 551 instances, 6 types | §4.2 setup | ✅ 标准 | ✅ | = §3 n=529 (gold-filtered) consistent |\n| Few-NERD 37,648 instances, 8 types | §4.2 setup | exp_021 (instance_count=37648) | ✅ | — |\n| CoNLL 3,453 instances, 4 types | §4.2 setup | ✅ 标准 | ✅ | — |\n| WNUT-17 1,287 instances, 53.7% zero F1 | §4.2 setup | exp_003_wnut17_eval (53.7%) | ✅ | — |\n| SJ>LP Δρ=+0.151±0.006 | §4.2 QE results | ⚠️ UNTRACED (bootstrap) | — | 仅出现一次 |\n| p_adj=0.013 (k=5) | seed-replication SJ>LP | ⚠️ UNTRACED | — | 仅出现一次 |\n| CoNLL EM ρ=0.816 (AUROC) | §4.2 \"EM leads both ρ and AUROC ($0.816$)\" | exp_002 (em_auroc=0.8156) | ✅ | = Tab quality_estimation |\n| WNUT VC ρ=0.724 at N=16 | §4.2 | exp_003 系列 | ⚠️ UNTRACED | 仅出现一次 |\n| WNUT conditional ρ=0.038 | §4.2 | ⚠️ UNTRACED | — | 仅出现一次 |\n| LP conditional ρ=0.350 | §4.2 WNUT | exp_003_wnut17_eval (rho_logprob_cond=0.35) | ✅ | 仅出现一次 |\n| LP σ=0.04 vs SJ 2.02 pp | §4.3 seed stability | ⚠️ UNTRACED | — | 仅出现一次 |\n| 50× more seed-stable | 2.02/0.04=50.5≈50 | ✅ 算术一致 | — | 仅出现一次 |\n| ρ=0.90, p=0.002 (MV vs low-F1 types) | §4.3 | ⚠️ UNTRACED (appendix pertype) | — | 仅出现一次 |\n| MV −2.71 pp (Few-NERD) | §4.3 | ⚠️ UNTRACED | — | 仅出现一次 |\n| Qwen3-4B |Δρ|=0.042 | §4.4 robustness | ⚠️ UNTRACED | — | 仅出现一次 |\n| +1.40±0.51 pp (construction) | §4.5 | exp_entity_construction | ⚠️ 见问题 #1 | = Abstract; Intro |\n| +0.32 pp SciERC (n.s.) | §4.5 | ⚠️ 见问题 #13 | — | 仅出现一次 |\n| −0.39 pp CoNLL | §4.5 | exp_entity_construction (conll cv_uniform='-0.39pp') | ✅ | 仅出现一次 |\n| D=13%, headroom=12.4 pp | §4.5 Few-NERD | exp_021 (headroom=0.124=12.4pp) | ✅ | — |\n| p_adj=0.006 (k=10) | §4.5 | ⚠️ UNTRACED | — | = Abstract; Intro |\n| p_adj=0.055 (k=57) | §4.5 | ⚠️ UNTRACED | — | = Abstract; Intro; limitations |\n| ρ_adj=0.516 | §4.5 construction-selection correlation | ⚠️ UNTRACED | — | 仅出现一次 |\n| 5-epoch: +1.39→+0.12 pp (selection) | §4.5 epoch confound | exp_fewnerd_5epoch_lp_s42 (lp_delta=0.12) | ✅ (5-epoch end) | — |\n| **5-epoch: +0.88→+0.20 pp (construction)** | §4.5 epoch confound | exp_entity_construction (n8_fair_cv fewnerd lp_weighted_cv='+0.88pp') | ⚠️ 见问题 #1 | — |\n| 9%→26% degeneracy | §4.5 epoch confound | 见问题 #4 | ⚠️ | — |\n\n## §4.4 Adaptive Methods\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| +0.42 pp (cross-model) | Qwen+LLaMA on Few-NERD | exp_cross_model_consistency (delta=0.42, p=0, CI=[0.27,0.58]) | ✅ | = Tab method_summary |\n| CI [0.27, 0.58] | cross-model CI | exp_cross_model_consistency | ✅ | 仅出现一次 |\n| AUC=0.923±0.002 | LightGBM verifier | exp_b2_entity_verifier (oof_auc=0.9233) | ✅ | = Tab method_summary |\n| +0.30 pp (verifier) | LightGBM F1 gain | exp_b2_entity_verifier (oof_delta_pp=0.3) | ✅ | = Tab method_summary |\n| −0.76 to −1.02 pp | verifier cross-dataset transfer | ⚠️ UNTRACED (appendix verifier_transfer) | — | 仅出现一次 |\n| ESJ AUROC 0.51 | Tab method_summary | exp_esj_qwen3_all (esj_auroc=0.512) | ✅ | = §4.1 |\n| MRSC −3.1 pp | Tab method_summary | ⚠️ UNTRACED | — | = §4.1 |\n| LSC −3.5 pp | Tab method_summary | ⚠️ UNTRACED | — | = §4.1 |\n| DALS +0.71 pp (SciERC) | Tab method_summary | ⚠️ UNTRACED | — | 仅出现一次 |\n| −0.4 to −3.1 pp | Sup. combination LR/MLP/RF | ⚠️ 见问题 #14 | — | 仅出现一次 |\n\n## §Theoretical Analysis (theoretical.tex)\n\n| 数字 | 上下文 | 来源 | 验证 | 跨位置一致 |\n|------|--------|------|------|-----------|\n| G_nd≈14.8 pp | \"with $G_{\\textup{nd}}{\\approx}14.8$\\,pp\" | ⚠️ UNTRACED (理论计算) | — | 仅出现一次 |\n| α≈0.068 | \"$\\alpha{\\approx}0.068$\" | ⚠️ UNTRACED | — | = fig_bound caption |\n| θ_crit=0.70 | \"$\\theta_{\\textup{crit}}{=}0.70$\" | ✅ 算术验证: (1-0.70)×14.8×0.068=0.302≈0.3pp | = theory.tex θ_crit∈[0.60,0.80] 一致 |\n| 3–12% | recovery ratio | ⚠️ UNTRACED | — | = Intro; theory.tex ✅ |\n\n## §Threshold Regime Analysis (theory.tex)\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| R²>0.999 | oracle scaling fit | ⚠️ UNTRACED | — | 仅出现一次 |\n| c≈0.61 (Few-NERD) | scaling exponent | ⚠️ UNTRACED | — | 仅出现一次 |\n| c≈0.35 (SciERC) | scaling exponent | ⚠️ UNTRACED | — | 仅出现一次 |\n| 8B→14B: +1.2 pp oracle, +0.9 pp greedy | scale ablation | ⚠️ UNTRACED | — | 仅出现一次 |\n| GPT-5.5: 50% degen | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2 (degen=0.5) | ✅ | 仅出现一次 |\n| GPT-5.5: SJ ρ=0.346 | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2 (sj_rho=0.3461) | ✅ | 仅出现一次 |\n| GPT-5.5: MV +1.4 pp | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2: mv-greedy=0.6521-0.6382=0.0139=1.39pp→1.4 | ✅ | 仅出现一次 |\n| GPT-5.5: 6.8 pp unrealized | frontier SC | oracle-mv=0.7203-0.6521=0.0682=6.82pp→6.8 | ✅ | 仅出现一次 |\n| 10.1% empty entity sets | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |\n| 88% gold-empty | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |\n| 1.2% true parse failures (19/1600) | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |\n| Qwen2.5: 31.7–46.2% | cross-scale degen | ⚠️ UNTRACED | — | 仅出现一次 |\n| 40 of 58 transitions (p<0.05) | inverse scaling | ⚠️ UNTRACED | — | 仅出现一次 |\n| θ=2/N: −3.09 pp (N=8), −6.90 pp (N=16) | inverse scaling severity | ⚠️ UNTRACED | — | 仅出现一次 |\n| MV: −0.87/−0.60 pp | MV inverse scaling | ⚠️ UNTRACED | — | 仅出现一次 |\n| OR=0.109 (11.1% vs 1.3%) | degen vs inverse scaling | ⚠️ UNTRACED; 算术近似验证: (1.3/98.7)/(11.1/88.9)=0.1055≈0.109 | — | 仅出现一次 |\n| CoNLL SJ ρ .30→.44 | few-shot improvement | ⚠️ UNTRACED | — | 仅出现一次 |\n| α=0.000–0.121 | binding constraint | ⚠️ UNTRACED | — | = §4.1 ✅ |\n| 8–33× tighter | α vs D | ⚠️ UNTRACED | — | = Intro; Discussion ✅ |\n| split-half r=0.395–0.578 | FK independence | ⚠️ UNTRACED | — | 仅出现一次 |\n| bound ratio 0.13–0.63 | signal-adjusted bound | ⚠️ UNTRACED | — | 仅出现一次 |\n| α_crit,eff=1.148 (CoNLL) | MV impossibility | ⚠️ UNTRACED | — | 仅出现一次 |\n\n## §5 Discussion\n\n| 数字 | 上下文 | 验证 | 跨位置一致 |\n|------|--------|------|-----------|\n| 12–68% | degeneracy range | ✅ | = Intro; §4.5 ✅ |\n| α→0 | signal alignment collapse | ✅ | 全文一致 |\n| 8–33× tighter | α vs D | ✅ | = Intro; theory.tex ✅ |\n| >50% | high degeneracy threshold | ✅ | 全文一致 |\n\n## Limitations\n\n| 数字 | 上下文 | 验证 | 跨位置一致 |\n|------|--------|------|-----------|\n| 5.5–74% | frontier degeneracy | exp_frontier_sc_deepseek (5.5%), exp_frontier_sc_claude_sonnet4 (74%) | ✅ | 仅出现一次 |\n| p_adj=0.055 | strongest construction claim | ✅ | = Abstract; §4.5 ✅ |\n| MDE≈1.5 pp | statistical power | ✅ | = §4.1 ✅ |\n| RE n=397, SQL n=196 | cross-task sample sizes | exp_spider_sc_pilot (n=196) | ✅ SQL; RE ⚠️ UNTRACED | — |\n| +1–1.4 pp | construction gain range | ✅ 与 §4.5 一致 | — |\n\n---\n\n## 关键数字重点检查\n\n### 1. SciERC EM AUROC = .631（不是 .749）\n- **Tab quality_estimation: .631** ✅ 论文正确\n- **Registry exp_012_rerun_1024: EM AUROC = 0.7493** ❌ Registry 与论文不一致\n- **Provenance c002: \"EM leads AUROC (NER 0.749)\"** ❌ Provenance STALE\n- **结论**: 论文已正确修改为 .631，但 registry 和 provenance 仍保留旧值 .749。**paper_provenance.yaml 需要更新。**\n\n### 2. Headroom = 13.0pp（不是 11.4pp）\n- Tab selection: Oracle 0.775 − Greedy 0.645 = 0.130 = **13.0pp** ✅\n- fig_selection_gap caption: **+13.0pp** ✅\n- 全文无 11.4pp 出现。**PASS。**\n\n### 3. MV = +0.6pp（不是 +0.61pp）\n- Intro: \"MV $+0.6$\\,pp on CoNLL\" ✅\n- Fig n_scaling caption: \"+0.6pp at N=64\" ✅\n- §4.3 text: \"+0.6pp\" ✅\n- Registry exp_conll_n64_s42: mv_delta = 0.64pp → 0.6 (1dp rounded) ✅\n- 全文无 +0.61pp 出现（Tab fewnerd SciERC LP Δ = +0.61pp 是 LP 不是 MV）。**PASS。**\n\n### 4. α = 0.121\n- §4.1: \"$\\alpha$ approaches zero ($0.000$--$0.121$)\" ✅\n- theory.tex: \"$\\alpha{=}0.000$--$0.121$\" ✅\n- 上限一致。**PASS。**\n\n### 5. SciERC construction = +0.32pp n.s.\n- §4.5: \"a non-significant $+0.32$\\,pp on SciERC\" ✅ 论文内一致\n- **Registry discrepancy**: exp_entity_construction 显示 SciERC n8_fair_cv 多个变体均 >+1pp（见问题 #13）\n- **结论**: 论文内一致，但 registry 来源不清楚。可能来自不同配置或后续重算。\n\n### 6. Holm p_adj = 0.055 (global k=57) vs p_adj = 0.013 (seed-replication k=5)\n- **p_adj=0.055 (k=57)**: Abstract, Intro, §4.5, limitations — 全部一致 ✅\n- **p_adj=0.013 (k=5)**: §4.2 \"SJ>LP advantage reaches $p_{\\text{adj}}{=}0.013$\" — 这是信号比较的 seed-replication correction ✅\n- 两者是不同统计框架，论文正确区分了。**PASS。**\n\n### 7. fig_selection_gap caption Oracle = +13.0pp（不是 +13.1pp）\n- Caption: \"oracle headroom ($+13.0$\\,pp)\" ✅\n- Tab selection: 0.775 − 0.645 = 0.130 = 13.0pp ✅\n- 全文无 13.1pp 出现。**PASS。**\n\n---\n\n## 问题清单\n\n按严重程度排序：\n\n### 🔴 严重 (Cross-table inconsistency)\n\n**#5. SciERC 基线在两个表格间不一致**\n- Tab selection (§4.1): Greedy = 0.645±0.001, LP Δ = +0.2pp (p=0.29)\n- Tab fewnerd (§4.3): Greedy = 0.663, LP Δ = +0.61pp (p=0.193)\n- 两表均标注 \"SciERC, Qwen3-8B, N=8, T=1.0\"\n- **差异**: Greedy F1 差 1.8pp; LP Δ 差 0.41pp\n- **可能原因**: 不同训练种子 / 不同 model checkpoint（exp_016 系列 vs exp_scierc_n8_s* 系列），但论文未说明\n- **影响**: 读者会困惑为何同一设置有不同基线\n\n**#10. SciERC EM AUROC: 论文 .631 vs Registry .7493**\n- Tab quality_estimation 显示 .631\n- exp_012_rerun_1024 registry 显示 EM AUROC = 0.7493\n- Provenance c002 仍记录 0.749\n- **状态**: 论文值 .631 被指定为正确值（任务说明），但 **registry 和 provenance 从未更新**\n- **影响**: 后续引用 provenance 的操作会得到错误数据\n\n**#11. SciERC/CoNLL LP ρ 在 Tab quality_estimation vs Tab fewnerd 间不一致**\n- SciERC LP ρ: Tab quality_estimation = .205; Tab fewnerd = .159 (差 0.046)\n- CoNLL LP ρ: Tab quality_estimation = .316; Tab fewnerd = .302 (差 0.014)\n- Tab quality_estimation 是 primary seed=42; Tab fewnerd 是 3-seed mean\n- **差异可能合理**（不同种子均值），但未在文中说明\n\n### 🟡 中等 (Traceability / consistency concern)\n\n**#1. Construction +1.40pp vs +0.88pp 同一方法不同数字**\n- §4.5 主结果: LP-weighted construction = +1.40±0.51pp (4-seed mean, full test)\n- §4.5 epoch confound: \"construction: +0.88→+0.20pp\"\n- Registry: n8_fair_cv fewnerd LP-weighted CV = +0.88pp\n- **分析**: +1.40 是 4-seed non-CV; +0.88 是 5-fold CV。两种评估方法给出不同结果。论文在同一段落交替使用两种评估方法而未说明\n- **影响**: 读者可能误以为 3-epoch construction gain = +0.88pp 而非 +1.40pp\n\n**#2. LP selection +1.39pp: 主种子显示 1.36pp**\n- 论文: +1.39pp (标注 3-seed mean)\n- Registry exp_021_fewnerd_full (seed42): lp_selection_delta_pp = 1.36\n- 其他种子 LP delta 未在 registry summary 中找到\n- **影响**: 无法从 registry 直接验证 1.39 是否为正确的 3-seed mean\n\n**#6. Tab selection LP p-value: 论文 .29 vs Registry .39**\n- Tab selection: LP p=.29\n- exp_016_rerun_1024_bootstrap: permutation_p = 0.39\n- **可能原因**: Tab selection 可能用 paired bootstrap（2-seed），exp_016 用 permutation test；或来自不同实验版本\n- **影响**: p-value 不同但结论相同（均不显著）\n\n**#7. Holm p_adj: 论文 0.021 (k=21) vs Provenance 0.019 (k=19)**\n- §4.1 footnote: \"Holm $p_{\\text{adj}}{=}0.021$, selection family $k{=}21$\"\n- Provenance C143: \"p_adj=0.019 k=19\"\n- **分析**: 家族大小从 19 增至 21（加入更多比较），p_adj 相应增大。Provenance stale。\n- **影响**: 数值轻微差异，结论不变\n\n**#8. Few-NERD degeneracy 13.0%: 主种子 registry 显示 10.1%**\n- Tab fewnerd: 13.0% (标注 3-seed mean)\n- exp_021_fewnerd_full (seed42): degeneracy_rate = 0.101 (10.1%)\n- exp_021_fewnerd_n8_seed123: degen_rate = 0.1312 (13.1%)\n- exp_021_fewnerd_n8_seed456: degen_rate = 0.1212 (12.1%)\n- 3-seed mean: (10.1+13.1+12.1)/3 = 11.8%, not 13.0%\n- **可能原因**: seed42 的 0.101 可能不是 constant-F1 degeneracy（seed123/456 标注为 unified_metrics_constant_f1_gold_filtered，seed42 未标注）\n- **影响**: 无法确认 13.0% 的准确性\n\n**#3. RE 40% zero-F1: Registry 显示 44.3%**\n- 论文多处: \"40% zero-F1\"\n- Provenance c006: \"44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\"\n- 40% 的具体来源实验不在 registry summary 中\n- **影响**: 轻微，但 40 vs 44.3 的差异未解释\n\n**#9. SciERC degeneracy 12.2%: Registry exp_012 显示 17.77%**\n- Tab fewnerd: SciERC Degen.% = 12.2%\n- exp_012_rerun_1024: degen_rate = 0.1777 (17.77%)\n- exp_scierc_n8_s123: degeneracy_rate = 0.116 (11.6%)\n- exp_scierc_n8_s456: degeneracy_rate = 0.12 (12.0%)\n- **分析**: 12.2% 可能来自 s123/s456 的均值而非 exp_012，或 exp_012 的 17.77% 是不同度量\n- **影响**: 来源不清楚\n\n**#12. Few-NERD LP ρ=.220 in Tab fewnerd vs .4215 in Registry**\n- Tab fewnerd: LP ρ = .220\n- exp_021_fewnerd_full: lp_global_rho = 0.4215\n- 差异 2x，即使是 3-seed mean 也不太可能降到 .220\n- **可能原因**: Tab fewnerd 的 LP ρ 可能不是 global cross-instance ρ，而是某种 within-instance 或 conditional 度量\n- **影响**: 如果是不同度量，需要在表格或 caption 中注明\n\n**#13. SciERC construction +0.32pp vs Registry +1.12~+1.67pp**\n- 论文: \"+0.32pp on SciERC (non-significant)\"\n- Registry exp_entity_construction: SciERC n8_fair_cv 多个变体 = +1.12 to +1.67pp\n- **可能原因**: 不同 θ、不同评估方法、不同种子集\n- **影响**: 无法从 registry 追溯 +0.32pp 的来源\n\n**#14. Supervised combination \"-0.4 to -3.1pp\"**\n- Tab method_summary: \"LR/MLP/RF: −0.4 to −3.1pp\"\n- Registry exp_backup3_distill_verifier: per-fold deltas 最大 = −0.34pp\n- −3.1pp 在 registry 中找不到对应\n- **可能原因**: −3.1pp 可能来自另一个实验或特定配置\n- **影响**: 范围上界无法追溯\n\n### 🟢 轻微 (Rounding / precision)\n\n**#4. Degeneracy type mixing in epoch comparison**\n- §4.5: \"degeneracy rises from 9% to 26%\" — entity-set exact-match\n- 主表 (Tab fewnerd): 13.0% — constant-F1\n- 脚注已解释两种度量，但正文在不同位置使用不同度量未明确标注\n\n**\"LP-best +1.4pp\" 精度模糊**\n- §4.3: \"LP-best $+1.4$\\,pp on Few-NERD\" — 可能是 selection (+1.39→1.4) 或 construction (+1.40)\n- 建议明确是哪种方法\n\n**AUROC rounding**\n- Abstract/Intro: \"AUROC up to 0.82\" — 来自 .816 (2dp rounding)\n- 技术上正确但比表格精度低\n\n---\n\n## 精度一致性\n\n| 类别 | 精度 | 评估 |\n|------|------|------|\n| 表格 ρ 值 | 3 位小数 (.379, .360) | ✅ 表内一致 |\n| 正文 ρ 引用 | 2 位小数 (.38, .45) | ✅ 合理简化 |\n| pp 增益 | 1-2 位小数 (+1.39, +0.6, +0.2) | ⚠️ +0.6 vs +1.39 精度不统一 |\n| 百分比 (degeneracy) | 1 位小数 (12.2%, 13.0%) | ✅ 一致 |\n| p-values | 表格 2 位 (.29, .67); 正文混合 | ✅ 大致一致 |\n| AUROC | 表格 3 位 (.631, .816); 正文 2 位 (.82) | ⚠️ 正文与表格精度不同但可接受 |\n\n总体精度一致性：**合格**，无系统性精度不一致问题。\n\n---\n\n## 总结\n\n- **已验证数字**: ~60% 可追溯到 registry 实验或算术验证\n- **UNTRACED**: ~25% 来自 appendix 实验或统计计算，无法从 registry summary 直接验证\n- **发现问题**: 14 个，其中 3 个严重（跨表不一致）、11 个中等或轻微\n- **7 个 bug-prone 数字**: 论文中全部正确 ✅，但 registry/provenance 有 2 处 stale 数据\n\n**最需要关注的问题**:\n1. Tab selection vs Tab fewnerd SciERC 基线不一致 (问题 #5)\n2. Registry EM AUROC stale (问题 #10) — 需更新 registry 和 provenance\n3. Construction +1.40 vs +0.88 评估方法混用 (问题 #1)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/audit_maintext_numbers.md",
    "content": "# 主文数字审计\n\n审计日期: 2026-05-24\n审计范围: docs/paper/sections/ 下所有主文 tex 文件\nRegistry 数据: 完整读取并交叉验证\n\n---\n\n## Abstract\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| AUROC 0.82 | \"AUROC up to $0.82$\" | exp_002 (em_auroc_full=0.8156) | ✅ .816→.82 (2dp rounding) | = Intro \"AUROC $0.82$\"; Tab quality_estimation CoNLL EM .816 |\n| <1 pp | \"selection yields no detectable gains (${<}1$\\,pp)\" | exp_016_rerun_1024_bootstrap | ✅ | = Intro/§4 consistent |\n| +1.40 pp | \"$+1.40$\\,pp on Few-NERD\" | exp_entity_construction (n8_fair_cv) | ⚠️ 见问题 #1 | = Intro +1.40; §4.5 +1.40±0.51; fig_overview caption +1.40 |\n| 3-epoch | \"under 3-epoch training\" | exp_021_fewnerd_full (epochs=3) | ✅ | = Intro/§4 consistent |\n| p_adj=0.055 | \"global Holm $p_{\\text{adj}}{=}0.055$\" | ⚠️ UNTRACED (统计结果，非直接实验 metric) | — | = Intro; §4.5 (k=57); limitations ✅ 一致 |\n| p_adj=0.006 | \"per-family $p_{\\text{adj}}{=}0.006$\" | ⚠️ UNTRACED | — | = Intro; §4.5 (k=10) ✅ 一致 |\n| degeneracy + signal alignment collapse | 定性描述 | N/A | ✅ | 一致 |\n\n## Introduction\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| ρ up to 0.45 | \"ρ up to $0.45$\" | exp_002 (em_rho_full=0.4507) | ✅ .451→.45 | = Tab quality_estimation CoNLL EM ρ=.451 |\n| AUROC 0.82 | \"AUROC $0.82$; Table quality_estimation\" | exp_002 (em_auroc_full=0.8156) | ✅ | = Abstract ✅ |\n| MV <1 pp at N=64 | \"MV ${<}1$ percentage point (pp) even at $N{=}64$\" | exp_conll_n64_s42 (mv_delta=0.64pp) | ✅ | = Fig n_scaling caption \"+0.6pp at N=64\" |\n| AUROC 0.63–0.88 | hidden-state probe | ⚠️ UNTRACED (appendix mechanistic) | — | = §4.1 line 53 一致 |\n| ESJ AUROC 0.51 | entity self-judgment | exp_esj_qwen3_all (scierc esj_auroc=0.512) | ✅ | = Tab method_summary AUROC 0.51 |\n| 12–68% | \"degeneracy ($12$--$68$\\%)\" | Tab fewnerd: SciERC 12.2%, WNUT 67.9% | ✅ 12.2→12, 67.9→68 | = Discussion ✅ |\n| LP +1.39 pp | \"LP $+1.39$\\,pp on Few-NERD\" | exp_021_fewnerd_full (lp_delta=1.36, seed42) | ⚠️ 见问题 #2 | = §4.1 +1.39; Tab fewnerd +1.39 |\n| MV +0.6 pp | \"MV $+0.6$\\,pp on CoNLL\" | exp_conll_n64_s42 (mv_delta=0.64pp) | ✅ .64→.6 | = Fig n_scaling; §4.3 |\n| +1.40 pp (construction) | \"Exploratory entity-level construction yields conditional improvement ($+1.40$\\,pp on Few-NERD, 3-epoch\" | Same as abstract | ⚠️ 见问题 #1 | = Abstract; §4.5 |\n| p_adj=0.055 | \"global Holm $p_{\\text{adj}}{=}0.055$\" | ⚠️ UNTRACED | — | = Abstract; §4.5; limitations ✅ |\n| p_adj=0.006 | \"per-family $p_{\\text{adj}}{=}0.006$\" | ⚠️ UNTRACED | — | = Abstract; §4.5 ✅ |\n| 87.2% | \"SQL parsing ($87.2$\\% degeneracy)\" | exp_spider_sc_pilot (F1_degeneracy=0.872) | ✅ | 仅出现一次 |\n| 40% zero-F1 | \"RE…$40$\\% zero-F1\" | provenance c006 notes \"paper uses 40% from primary config\"; registry shows 44.3% at N=16 | ⚠️ 见问题 #3 | = §4.3 \"40%\" 一致 |\n| ρ up to 0.47 | \"\\citet{yao2026consistency} report…$\\rho$ up to 0.47\" | 引用他人数据 | N/A | 仅引用 |\n| LP mean weight 0.78 | \"ensemble optimization assigns LP mean weight $0.78$\" | ⚠️ UNTRACED (appendix supervised_combination) | — | 仅出现一次 |\n| 3–12% recovery ratio | \"3--12\\% recovery ratio\" | ⚠️ UNTRACED (理论计算) | — | = theoretical.tex; theory.tex ✅ |\n| α=0.000–0.121 | \"$\\alpha$ approaches zero ($0.000$--$0.121$)\" | ⚠️ UNTRACED (理论计算) | — | = theory.tex line 38 ✅ |\n| +3.85 pp MV | \"pretrained Qwen2.5-7B at $N{=}32$ achieves $+3.85$\\,pp MV gain\" | exp_fewnerd_pretrained_n32_s42_v2 (mv_delta=3.85) | ✅ | 仅出现一次 |\n| D=5.4% | \"$D{=}5.4$\\%\" | exp_fewnerd_pretrained_n32_s42_v2 (degen=5.42) | ✅ 5.42→5.4 | 仅出现一次 |\n\n## §3 Diagnostic Framework\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| +4.6 F1 points | \"length normalization eliminates length bias ($+4.6$ F1 points)\" | ⚠️ UNTRACED (appendix token_signal) | — | 仅出现一次 |\n| n=529 | \"n=529 on SciERC\" | exp_012_rerun_1024 (ner_full n=529) | ✅ | = Tab quality_estimation caption; Tab fewnerd SciERC n=529 |\n| n=2,756 | \"n=2,756 on CoNLL\" | exp_017_llama_conll_infer data | ✅ | = Tab fewnerd CoNLL n=2,756 |\n| 9–26% | \"Entity-set exact-match degeneracy…($9$--$26$\\%)\" | exp_fewnerd_mf4_s* (8.1%–9.3% at 5-epoch) | ⚠️ 见问题 #4 | 脚注内部使用 |\n| 13–31% | \"vs.\\ $13$--$31$\\% constant-F1\" | exp_021 seeds (10.1%–13.1% at 3-epoch) | ⚠️ 部分匹配 | 脚注内部使用 |\n\n## §4.1 Single-Signal Selection Results\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| 60% LP range <0.041 | \"60\\% of SciERC instances showing within-instance LP range below 0.041 nats\" | ⚠️ UNTRACED (appendix logprob_ties) | — | 仅出现一次 |\n| 0.97× | \"free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97$)\" | exp_conll_freeform_n8_s42 / exp_fewnerd_freeform_n8_s42 | ⚠️ 无法直接确认 0.97 | 仅出现一次 |\n| Tab selection: Oracle 0.775±0.001 | Best-of-N table | exp_016_rerun_1024_bootstrap (oracle=0.776) | ⚠️ .776 vs .775 | 仅 Tab selection |\n| Tab selection: Greedy 0.645±0.001 | Best-of-N table | exp_016_rerun_1024_bootstrap (greedy=0.644) | ⚠️ .644 vs .645 | ❌ 见问题 #5 |\n| Tab selection: LP 0.647±0.005 | LP selection F1 | exp_016_rerun_1024_bootstrap | ⚠️ 间接 | 仅 Tab selection |\n| Tab selection: LP p=.29 | \"LP achieves $+0.2$\\,pp ($p{=}0.29$)\" | exp_016_rerun_1024_bootstrap (permutation_p=0.39) | ❌ 见问题 #6 | Tab vs text 一致 (.29) |\n| ρ up to 0.38 | \"Despite $\\rho$ up to 0.38\" | exp_012_rerun_1024 (vc_rho=0.3792) | ✅ .379→.38 | = Tab quality_estimation VC ρ=.379 |\n| +13.0 pp headroom | \"the oracle shows 13.0\\,pp headroom\" | Tab selection: 0.775-0.645=0.130=13.0pp | ✅ | = fig_selection_gap caption \"+13.0pp\" ✅ |\n| MDE ≈1.5 pp | \"below MDE (${\\approx}$1.5\\,pp at $n{=}529$, 2--3 seeds\" | ⚠️ UNTRACED (统计计算) | — | = limitations ✅ |\n| LP +1.39 pp (Few-NERD) | \"LP achieves $+1.39$\\,pp ($p{<}0.001$; Holm $p_{\\text{adj}}{=}0.021$, k=21)\" | exp_021_fewnerd_full (1.36 for seed42) | ⚠️ 见问题 #2 | = Tab fewnerd; Intro |\n| p_adj=0.021, k=21 | selection family correction | provenance C143 has p_adj=0.019 k=19 | ⚠️ 见问题 #7 | 仅出现一次 |\n| p_adj=0.055 (global k=57) | footnote | ⚠️ UNTRACED | — | = Abstract; §4.5; limitations |\n| 13.0% degeneracy (Few-NERD) | \"low degeneracy (13.0\\%)\" | 见问题 #8 | ⚠️ | = Tab fewnerd 13.0% |\n| 12.2% (SciERC) | \"SciERC 12.2\\%\" | exp_012_rerun_1024 (degen=0.1777?) | ⚠️ 见问题 #9 | = Tab fewnerd 12.2% ✅ |\n| 61.7% (CoNLL) | \"CoNLL 61.7\\%\" | ⚠️ UNTRACED | — | = Tab fewnerd 61.7% ✅ |\n| VC −1.79, SJ −2.14 pp | structural signals degrade on Few-NERD | exp_021_fewnerd_full (vc_delta=-1.79, sj_delta=-2.14) | ✅ | = §4.3 一致 |\n| ρ=0.052, n=23, p=0.81 | degeneracy-LP across configs | ⚠️ UNTRACED | — | = §4.3 Fig degeneracy_scatter ✅ |\n| ρ=−0.881 | within-dataset degen-LP | ⚠️ UNTRACED | — | = §4.3 ✅ |\n| MRSC −3.1 pp | multi-round refinement | ⚠️ UNTRACED (appendix mechanistic) | — | = Tab method_summary ✅ |\n| LSC −3.5 pp | latent centroid selection | ⚠️ UNTRACED (appendix mechanistic) | — | = Tab method_summary ✅ |\n| ESJ AUROC 0.50–0.55 (Qwen3-8B) | cross-model ESJ | exp_esj_qwen3_all (scierc=0.512, fewnerd=0.495) | ✅ | 仅出现一次 |\n\n## §4.2–4.3 Experiments (experiments_main.tex)\n\n### Tab quality_estimation\n\n| 数字 | 来源 exp_id | 验证 |\n|------|------------|------|\n| SciERC VC ρ=.379 | exp_012_rerun_1024 (voting_conf rho=0.3792) | ✅ |\n| SciERC SJ ρ=.360 | exp_012_rerun_1024 (SJ rho=0.3599) | ✅ |\n| SciERC FK ρ=.267 | exp_012_rerun_1024 (FK rho=0.2665) | ✅ |\n| SciERC EM ρ=.295 | exp_012_rerun_1024 (EM rho=0.2945) | ✅ |\n| SciERC LP ρ=.205 | exp_012_rerun_1024 (LP rho=0.2052) | ✅ |\n| SciERC VC AUC=.684 | exp_012_rerun_1024 (voting_conf AUROC=0.6841) | ✅ |\n| SciERC SJ AUC=.692 | exp_012_rerun_1024 (SJ AUROC=0.6917) | ✅ |\n| SciERC FK AUC=.629 | exp_012_rerun_1024 (FK AUROC=0.629) | ✅ |\n| **SciERC EM AUC=.631** | **exp_012_rerun_1024 (EM AUROC=0.7493)** | **❌ 见问题 #10** |\n| SciERC LP AUC=.578 | exp_012_rerun_1024 (LP AUROC=0.5783) | ✅ |\n| CoNLL Qwen EM ρ=.451 | exp_002 (em_rho_full=0.4507) | ✅ |\n| CoNLL Qwen EM AUC=.816 | exp_002 (em_auroc_full=0.8156) | ✅ |\n| CoNLL Qwen SJ ρ=.436 | exp_002 (sj_rho_full=0.4357) | ✅ |\n| CoNLL LLaMA SJ ρ=.431 | exp_017_llama_conll_infer (SJ_rho=0.4314) | ✅ |\n| CoNLL LLaMA LP AUC=.761 | exp_017_llama_conll_infer (logprob_AUROC=0.761) | ✅ |\n\n### Tab fewnerd (cross-dataset LP selection)\n\n| 数字 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|------------|------|-----------|\n| WNUT n=1,287 | exp_003_wnut17_eval (n=1287) | ✅ | = §4.2 |\n| WNUT Greedy .452 | exp_wnut17_qwen25_7b (seed42 greedy=0.4524) | ✅ | — |\n| WNUT Degen 67.9% | ⚠️ UNTRACED (N=8 data; registry WNUT experiments are N=16) | — | = text 12–68% upper bound |\n| WNUT LP ρ=−.446 | ⚠️ UNTRACED (registry has −.414/−.409 at N=16) | — | — |\n| CoNLL n=2,756 | consistent | ✅ | = §3 |\n| CoNLL Greedy .908 | ⚠️ UNTRACED for N=8 Qwen | — | — |\n| CoNLL Degen 61.7% | ⚠️ UNTRACED | — | = §4.1 ✅ |\n| CoNLL LP ρ=.302 | ⚠️ ≠ Tab quality_estimation LP ρ=.316 | ⚠️ 见问题 #11 | — |\n| **SciERC Greedy .663** | **exp_scierc_n8_s* (greedy ≈0.661–0.666)** | ✅ matches multi-seed | **❌ ≠ Tab selection Greedy .645 见问题 #5** |\n| SciERC Degen 12.2% | ⚠️ PARTIALLY TRACED | — | = §4.1 ✅ |\n| **SciERC LP ρ=.159** | ⚠️ UNTRACED | — | **❌ ≠ Tab quality_estimation LP ρ=.205 见问题 #11** |\n| **SciERC LP Δ=+0.61 pp** | ⚠️ UNTRACED | — | **❌ ≠ §4.1 text \"+0.2pp\" 见问题 #5** |\n| Few-NERD n=32,565 | exp_021_fewnerd_full (filtered=32565) | ✅ | — |\n| Few-NERD Greedy .748 | exp_021_fewnerd_full (greedy=0.7478) | ✅ | — |\n| Few-NERD Degen 13.0% | ⚠️ 见问题 #8 | — | = §4.1 ✅ |\n| Few-NERD LP ρ=.220 | ⚠️ ≠ exp_021 lp_global_rho=0.4215 | ⚠️ 见问题 #12 | — |\n| Few-NERD LP Δ=+1.39 pp | exp_021_fewnerd_full (1.36 seed42) | ⚠️ 见问题 #2 | = §4.1; Intro |\n\n### Other §4 numbers\n\n| 数字 | 上下文 | 来源 | 验证 | 跨位置一致 |\n|------|--------|------|------|-----------|\n| SciERC 551 instances, 6 types | §4.2 setup | ✅ 标准 | ✅ | = §3 n=529 (gold-filtered) consistent |\n| Few-NERD 37,648 instances, 8 types | §4.2 setup | exp_021 (instance_count=37648) | ✅ | — |\n| CoNLL 3,453 instances, 4 types | §4.2 setup | ✅ 标准 | ✅ | — |\n| WNUT-17 1,287 instances, 53.7% zero F1 | §4.2 setup | exp_003_wnut17_eval (53.7%) | ✅ | — |\n| SJ>LP Δρ=+0.151±0.006 | §4.2 QE results | ⚠️ UNTRACED (bootstrap) | — | 仅出现一次 |\n| p_adj=0.013 (k=5) | seed-replication SJ>LP | ⚠️ UNTRACED | — | 仅出现一次 |\n| CoNLL EM ρ=0.816 (AUROC) | §4.2 \"EM leads both ρ and AUROC ($0.816$)\" | exp_002 (em_auroc=0.8156) | ✅ | = Tab quality_estimation |\n| WNUT VC ρ=0.724 at N=16 | §4.2 | exp_003 系列 | ⚠️ UNTRACED | 仅出现一次 |\n| WNUT conditional ρ=0.038 | §4.2 | ⚠️ UNTRACED | — | 仅出现一次 |\n| LP conditional ρ=0.350 | §4.2 WNUT | exp_003_wnut17_eval (rho_logprob_cond=0.35) | ✅ | 仅出现一次 |\n| LP σ=0.04 vs SJ 2.02 pp | §4.3 seed stability | ⚠️ UNTRACED | — | 仅出现一次 |\n| 50× more seed-stable | 2.02/0.04=50.5≈50 | ✅ 算术一致 | — | 仅出现一次 |\n| ρ=0.90, p=0.002 (MV vs low-F1 types) | §4.3 | ⚠️ UNTRACED (appendix pertype) | — | 仅出现一次 |\n| MV −2.71 pp (Few-NERD) | §4.3 | ⚠️ UNTRACED | — | 仅出现一次 |\n| Qwen3-4B |Δρ|=0.042 | §4.4 robustness | ⚠️ UNTRACED | — | 仅出现一次 |\n| +1.40±0.51 pp (construction) | §4.5 | exp_entity_construction | ⚠️ 见问题 #1 | = Abstract; Intro |\n| +0.32 pp SciERC (n.s.) | §4.5 | ⚠️ 见问题 #13 | — | 仅出现一次 |\n| −0.39 pp CoNLL | §4.5 | exp_entity_construction (conll cv_uniform='-0.39pp') | ✅ | 仅出现一次 |\n| D=13%, headroom=12.4 pp | §4.5 Few-NERD | exp_021 (headroom=0.124=12.4pp) | ✅ | — |\n| p_adj=0.006 (k=10) | §4.5 | ⚠️ UNTRACED | — | = Abstract; Intro |\n| p_adj=0.055 (k=57) | §4.5 | ⚠️ UNTRACED | — | = Abstract; Intro; limitations |\n| ρ_adj=0.516 | §4.5 construction-selection correlation | ⚠️ UNTRACED | — | 仅出现一次 |\n| 5-epoch: +1.39→+0.12 pp (selection) | §4.5 epoch confound | exp_fewnerd_5epoch_lp_s42 (lp_delta=0.12) | ✅ (5-epoch end) | — |\n| **5-epoch: +0.88→+0.20 pp (construction)** | §4.5 epoch confound | exp_entity_construction (n8_fair_cv fewnerd lp_weighted_cv='+0.88pp') | ⚠️ 见问题 #1 | — |\n| 9%→26% degeneracy | §4.5 epoch confound | 见问题 #4 | ⚠️ | — |\n\n## §4.4 Adaptive Methods\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| +0.42 pp (cross-model) | Qwen+LLaMA on Few-NERD | exp_cross_model_consistency (delta=0.42, p=0, CI=[0.27,0.58]) | ✅ | = Tab method_summary |\n| CI [0.27, 0.58] | cross-model CI | exp_cross_model_consistency | ✅ | 仅出现一次 |\n| AUC=0.923±0.002 | LightGBM verifier | exp_b2_entity_verifier (oof_auc=0.9233) | ✅ | = Tab method_summary |\n| +0.30 pp (verifier) | LightGBM F1 gain | exp_b2_entity_verifier (oof_delta_pp=0.3) | ✅ | = Tab method_summary |\n| −0.76 to −1.02 pp | verifier cross-dataset transfer | ⚠️ UNTRACED (appendix verifier_transfer) | — | 仅出现一次 |\n| ESJ AUROC 0.51 | Tab method_summary | exp_esj_qwen3_all (esj_auroc=0.512) | ✅ | = §4.1 |\n| MRSC −3.1 pp | Tab method_summary | ⚠️ UNTRACED | — | = §4.1 |\n| LSC −3.5 pp | Tab method_summary | ⚠️ UNTRACED | — | = §4.1 |\n| DALS +0.71 pp (SciERC) | Tab method_summary | ⚠️ UNTRACED | — | 仅出现一次 |\n| −0.4 to −3.1 pp | Sup. combination LR/MLP/RF | ⚠️ 见问题 #14 | — | 仅出现一次 |\n\n## §Theoretical Analysis (theoretical.tex)\n\n| 数字 | 上下文 | 来源 | 验证 | 跨位置一致 |\n|------|--------|------|------|-----------|\n| G_nd≈14.8 pp | \"with $G_{\\textup{nd}}{\\approx}14.8$\\,pp\" | ⚠️ UNTRACED (理论计算) | — | 仅出现一次 |\n| α≈0.068 | \"$\\alpha{\\approx}0.068$\" | ⚠️ UNTRACED | — | = fig_bound caption |\n| θ_crit=0.70 | \"$\\theta_{\\textup{crit}}{=}0.70$\" | ✅ 算术验证: (1-0.70)×14.8×0.068=0.302≈0.3pp | = theory.tex θ_crit∈[0.60,0.80] 一致 |\n| 3–12% | recovery ratio | ⚠️ UNTRACED | — | = Intro; theory.tex ✅ |\n\n## §Threshold Regime Analysis (theory.tex)\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| R²>0.999 | oracle scaling fit | ⚠️ UNTRACED | — | 仅出现一次 |\n| c≈0.61 (Few-NERD) | scaling exponent | ⚠️ UNTRACED | — | 仅出现一次 |\n| c≈0.35 (SciERC) | scaling exponent | ⚠️ UNTRACED | — | 仅出现一次 |\n| 8B→14B: +1.2 pp oracle, +0.9 pp greedy | scale ablation | ⚠️ UNTRACED | — | 仅出现一次 |\n| GPT-5.5: 50% degen | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2 (degen=0.5) | ✅ | 仅出现一次 |\n| GPT-5.5: SJ ρ=0.346 | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2 (sj_rho=0.3461) | ✅ | 仅出现一次 |\n| GPT-5.5: MV +1.4 pp | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2: mv-greedy=0.6521-0.6382=0.0139=1.39pp→1.4 | ✅ | 仅出现一次 |\n| GPT-5.5: 6.8 pp unrealized | frontier SC | oracle-mv=0.7203-0.6521=0.0682=6.82pp→6.8 | ✅ | 仅出现一次 |\n| 10.1% empty entity sets | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |\n| 88% gold-empty | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |\n| 1.2% true parse failures (19/1600) | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |\n| Qwen2.5: 31.7–46.2% | cross-scale degen | ⚠️ UNTRACED | — | 仅出现一次 |\n| 40 of 58 transitions (p<0.05) | inverse scaling | ⚠️ UNTRACED | — | 仅出现一次 |\n| θ=2/N: −3.09 pp (N=8), −6.90 pp (N=16) | inverse scaling severity | ⚠️ UNTRACED | — | 仅出现一次 |\n| MV: −0.87/−0.60 pp | MV inverse scaling | ⚠️ UNTRACED | — | 仅出现一次 |\n| OR=0.109 (11.1% vs 1.3%) | degen vs inverse scaling | ⚠️ UNTRACED; 算术近似验证: (1.3/98.7)/(11.1/88.9)=0.1055≈0.109 | — | 仅出现一次 |\n| CoNLL SJ ρ .30→.44 | few-shot improvement | ⚠️ UNTRACED | — | 仅出现一次 |\n| α=0.000–0.121 | binding constraint | ⚠️ UNTRACED | — | = §4.1 ✅ |\n| 8–33× tighter | α vs D | ⚠️ UNTRACED | — | = Intro; Discussion ✅ |\n| split-half r=0.395–0.578 | FK independence | ⚠️ UNTRACED | — | 仅出现一次 |\n| bound ratio 0.13–0.63 | signal-adjusted bound | ⚠️ UNTRACED | — | 仅出现一次 |\n| α_crit,eff=1.148 (CoNLL) | MV impossibility | ⚠️ UNTRACED | — | 仅出现一次 |\n\n## §5 Discussion\n\n| 数字 | 上下文 | 验证 | 跨位置一致 |\n|------|--------|------|-----------|\n| 12–68% | degeneracy range | ✅ | = Intro; §4.5 ✅ |\n| α→0 | signal alignment collapse | ✅ | 全文一致 |\n| 8–33× tighter | α vs D | ✅ | = Intro; theory.tex ✅ |\n| >50% | high degeneracy threshold | ✅ | 全文一致 |\n\n## Limitations\n\n| 数字 | 上下文 | 验证 | 跨位置一致 |\n|------|--------|------|-----------|\n| 5.5–74% | frontier degeneracy | exp_frontier_sc_deepseek (5.5%), exp_frontier_sc_claude_sonnet4 (74%) | ✅ | 仅出现一次 |\n| p_adj=0.055 | strongest construction claim | ✅ | = Abstract; §4.5 ✅ |\n| MDE≈1.5 pp | statistical power | ✅ | = §4.1 ✅ |\n| RE n=397, SQL n=196 | cross-task sample sizes | exp_spider_sc_pilot (n=196) | ✅ SQL; RE ⚠️ UNTRACED | — |\n| +1–1.4 pp | construction gain range | ✅ 与 §4.5 一致 | — |\n\n---\n\n## 关键数字重点检查\n\n### 1. SciERC EM AUROC = .631（不是 .749）\n- **Tab quality_estimation: .631** ✅ 论文正确\n- **Registry exp_012_rerun_1024: EM AUROC = 0.7493** ❌ Registry 与论文不一致\n- **Provenance c002: \"EM leads AUROC (NER 0.749)\"** ❌ Provenance STALE\n- **结论**: 论文已正确修改为 .631，但 registry 和 provenance 仍保留旧值 .749。**paper_provenance.yaml 需要更新。**\n\n### 2. Headroom = 13.0pp（不是 11.4pp）\n- Tab selection: Oracle 0.775 − Greedy 0.645 = 0.130 = **13.0pp** ✅\n- fig_selection_gap caption: **+13.0pp** ✅\n- 全文无 11.4pp 出现。**PASS。**\n\n### 3. MV = +0.6pp（不是 +0.61pp）\n- Intro: \"MV $+0.6$\\,pp on CoNLL\" ✅\n- Fig n_scaling caption: \"+0.6pp at N=64\" ✅\n- §4.3 text: \"+0.6pp\" ✅\n- Registry exp_conll_n64_s42: mv_delta = 0.64pp → 0.6 (1dp rounded) ✅\n- 全文无 +0.61pp 出现（Tab fewnerd SciERC LP Δ = +0.61pp 是 LP 不是 MV）。**PASS。**\n\n### 4. α = 0.121\n- §4.1: \"$\\alpha$ approaches zero ($0.000$--$0.121$)\" ✅\n- theory.tex: \"$\\alpha{=}0.000$--$0.121$\" ✅\n- 上限一致。**PASS。**\n\n### 5. SciERC construction = +0.32pp n.s.\n- §4.5: \"a non-significant $+0.32$\\,pp on SciERC\" ✅ 论文内一致\n- **Registry discrepancy**: exp_entity_construction 显示 SciERC n8_fair_cv 多个变体均 >+1pp（见问题 #13）\n- **结论**: 论文内一致，但 registry 来源不清楚。可能来自不同配置或后续重算。\n\n### 6. Holm p_adj = 0.055 (global k=57) vs p_adj = 0.013 (seed-replication k=5)\n- **p_adj=0.055 (k=57)**: Abstract, Intro, §4.5, limitations — 全部一致 ✅\n- **p_adj=0.013 (k=5)**: §4.2 \"SJ>LP advantage reaches $p_{\\text{adj}}{=}0.013$\" — 这是信号比较的 seed-replication correction ✅\n- 两者是不同统计框架，论文正确区分了。**PASS。**\n\n### 7. fig_selection_gap caption Oracle = +13.0pp（不是 +13.1pp）\n- Caption: \"oracle headroom ($+13.0$\\,pp)\" ✅\n- Tab selection: 0.775 − 0.645 = 0.130 = 13.0pp ✅\n- 全文无 13.1pp 出现。**PASS。**\n\n---\n\n## 问题清单\n\n按严重程度排序：\n\n### 🔴 严重 (Cross-table inconsistency)\n\n**#5. SciERC 基线在两个表格间不一致**\n- Tab selection (§4.1): Greedy = 0.645±0.001, LP Δ = +0.2pp (p=0.29)\n- Tab fewnerd (§4.3): Greedy = 0.663, LP Δ = +0.61pp (p=0.193)\n- 两表均标注 \"SciERC, Qwen3-8B, N=8, T=1.0\"\n- **差异**: Greedy F1 差 1.8pp; LP Δ 差 0.41pp\n- **可能原因**: 不同训练种子 / 不同 model checkpoint（exp_016 系列 vs exp_scierc_n8_s* 系列），但论文未说明\n- **影响**: 读者会困惑为何同一设置有不同基线\n\n**#10. SciERC EM AUROC: 论文 .631 vs Registry .7493**\n- Tab quality_estimation 显示 .631\n- exp_012_rerun_1024 registry 显示 EM AUROC = 0.7493\n- Provenance c002 仍记录 0.749\n- **状态**: 论文值 .631 被指定为正确值（任务说明），但 **registry 和 provenance 从未更新**\n- **影响**: 后续引用 provenance 的操作会得到错误数据\n\n**#11. SciERC/CoNLL LP ρ 在 Tab quality_estimation vs Tab fewnerd 间不一致**\n- SciERC LP ρ: Tab quality_estimation = .205; Tab fewnerd = .159 (差 0.046)\n- CoNLL LP ρ: Tab quality_estimation = .316; Tab fewnerd = .302 (差 0.014)\n- Tab quality_estimation 是 primary seed=42; Tab fewnerd 是 3-seed mean\n- **差异可能合理**（不同种子均值），但未在文中说明\n\n### 🟡 中等 (Traceability / consistency concern)\n\n**#1. Construction +1.40pp vs +0.88pp 同一方法不同数字**\n- §4.5 主结果: LP-weighted construction = +1.40±0.51pp (4-seed mean, full test)\n- §4.5 epoch confound: \"construction: +0.88→+0.20pp\"\n- Registry: n8_fair_cv fewnerd LP-weighted CV = +0.88pp\n- **分析**: +1.40 是 4-seed non-CV; +0.88 是 5-fold CV。两种评估方法给出不同结果。论文在同一段落交替使用两种评估方法而未说明\n- **影响**: 读者可能误以为 3-epoch construction gain = +0.88pp 而非 +1.40pp\n\n**#2. LP selection +1.39pp: 主种子显示 1.36pp**\n- 论文: +1.39pp (标注 3-seed mean)\n- Registry exp_021_fewnerd_full (seed42): lp_selection_delta_pp = 1.36\n- 其他种子 LP delta 未在 registry summary 中找到\n- **影响**: 无法从 registry 直接验证 1.39 是否为正确的 3-seed mean\n\n**#6. Tab selection LP p-value: 论文 .29 vs Registry .39**\n- Tab selection: LP p=.29\n- exp_016_rerun_1024_bootstrap: permutation_p = 0.39\n- **可能原因**: Tab selection 可能用 paired bootstrap（2-seed），exp_016 用 permutation test；或来自不同实验版本\n- **影响**: p-value 不同但结论相同（均不显著）\n\n**#7. Holm p_adj: 论文 0.021 (k=21) vs Provenance 0.019 (k=19)**\n- §4.1 footnote: \"Holm $p_{\\text{adj}}{=}0.021$, selection family $k{=}21$\"\n- Provenance C143: \"p_adj=0.019 k=19\"\n- **分析**: 家族大小从 19 增至 21（加入更多比较），p_adj 相应增大。Provenance stale。\n- **影响**: 数值轻微差异，结论不变\n\n**#8. Few-NERD degeneracy 13.0%: 主种子 registry 显示 10.1%**\n- Tab fewnerd: 13.0% (标注 3-seed mean)\n- exp_021_fewnerd_full (seed42): degeneracy_rate = 0.101 (10.1%)\n- exp_021_fewnerd_n8_seed123: degen_rate = 0.1312 (13.1%)\n- exp_021_fewnerd_n8_seed456: degen_rate = 0.1212 (12.1%)\n- 3-seed mean: (10.1+13.1+12.1)/3 = 11.8%, not 13.0%\n- **可能原因**: seed42 的 0.101 可能不是 constant-F1 degeneracy（seed123/456 标注为 unified_metrics_constant_f1_gold_filtered，seed42 未标注）\n- **影响**: 无法确认 13.0% 的准确性\n\n**#3. RE 40% zero-F1: Registry 显示 44.3%**\n- 论文多处: \"40% zero-F1\"\n- Provenance c006: \"44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\"\n- 40% 的具体来源实验不在 registry summary 中\n- **影响**: 轻微，但 40 vs 44.3 的差异未解释\n\n**#9. SciERC degeneracy 12.2%: Registry exp_012 显示 17.77%**\n- Tab fewnerd: SciERC Degen.% = 12.2%\n- exp_012_rerun_1024: degen_rate = 0.1777 (17.77%)\n- exp_scierc_n8_s123: degeneracy_rate = 0.116 (11.6%)\n- exp_scierc_n8_s456: degeneracy_rate = 0.12 (12.0%)\n- **分析**: 12.2% 可能来自 s123/s456 的均值而非 exp_012，或 exp_012 的 17.77% 是不同度量\n- **影响**: 来源不清楚\n\n**#12. Few-NERD LP ρ=.220 in Tab fewnerd vs .4215 in Registry**\n- Tab fewnerd: LP ρ = .220\n- exp_021_fewnerd_full: lp_global_rho = 0.4215\n- 差异 2x，即使是 3-seed mean 也不太可能降到 .220\n- **可能原因**: Tab fewnerd 的 LP ρ 可能不是 global cross-instance ρ，而是某种 within-instance 或 conditional 度量\n- **影响**: 如果是不同度量，需要在表格或 caption 中注明\n\n**#13. SciERC construction +0.32pp vs Registry +1.12~+1.67pp**\n- 论文: \"+0.32pp on SciERC (non-significant)\"\n- Registry exp_entity_construction: SciERC n8_fair_cv 多个变体 = +1.12 to +1.67pp\n- **可能原因**: 不同 θ、不同评估方法、不同种子集\n- **影响**: 无法从 registry 追溯 +0.32pp 的来源\n\n**#14. Supervised combination \"-0.4 to -3.1pp\"**\n- Tab method_summary: \"LR/MLP/RF: −0.4 to −3.1pp\"\n- Registry exp_backup3_distill_verifier: per-fold deltas 最大 = −0.34pp\n- −3.1pp 在 registry 中找不到对应\n- **可能原因**: −3.1pp 可能来自另一个实验或特定配置\n- **影响**: 范围上界无法追溯\n\n### 🟢 轻微 (Rounding / precision)\n\n**#4. Degeneracy type mixing in epoch comparison**\n- §4.5: \"degeneracy rises from 9% to 26%\" — entity-set exact-match\n- 主表 (Tab fewnerd): 13.0% — constant-F1\n- 脚注已解释两种度量，但正文在不同位置使用不同度量未明确标注\n\n**\"LP-best +1.4pp\" 精度模糊**\n- §4.3: \"LP-best $+1.4$\\,pp on Few-NERD\" — 可能是 selection (+1.39→1.4) 或 construction (+1.40)\n- 建议明确是哪种方法\n\n**AUROC rounding**\n- Abstract/Intro: \"AUROC up to 0.82\" — 来自 .816 (2dp rounding)\n- 技术上正确但比表格精度低\n\n---\n\n## 精度一致性\n\n| 类别 | 精度 | 评估 |\n|------|------|------|\n| 表格 ρ 值 | 3 位小数 (.379, .360) | ✅ 表内一致 |\n| 正文 ρ 引用 | 2 位小数 (.38, .45) | ✅ 合理简化 |\n| pp 增益 | 1-2 位小数 (+1.39, +0.6, +0.2) | ⚠️ +0.6 vs +1.39 精度不统一 |\n| 百分比 (degeneracy) | 1 位小数 (12.2%, 13.0%) | ✅ 一致 |\n| p-values | 表格 2 位 (.29, .67); 正文混合 | ✅ 大致一致 |\n| AUROC | 表格 3 位 (.631, .816); 正文 2 位 (.82) | ⚠️ 正文与表格精度不同但可接受 |\n\n总体精度一致性：**合格**，无系统性精度不一致问题。\n\n---\n\n## 总结\n\n- **已验证数字**: ~60% 可追溯到 registry 实验或算术验证\n- **UNTRACED**: ~25% 来自 appendix 实验或统计计算，无法从 registry summary 直接验证\n- **发现问题**: 14 个，其中 3 个严重（跨表不一致）、11 个中等或轻微\n- **7 个 bug-prone 数字**: 论文中全部正确 ✅，但 registry/provenance 有 2 处 stale 数据\n\n**最需要关注的问题**:\n1. Tab selection vs Tab fewnerd SciERC 基线不一致 (问题 #5)\n2. Registry EM AUROC stale (问题 #10) — 需更新 registry 和 provenance\n3. Construction +1.40 vs +0.88 评估方法混用 (问题 #1)\n"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-24T04:44:58.519399+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/audit_maintext_numbers.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-24T04:44:58.519669+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "audit_maintext_numbers",
  "type": "report",
  "description": "主文定量数字全面审计：检查每个数字的可追溯性、跨位置一致性、精度一致性。发现14个问题，3个严重（跨表不一致），7个bug-prone数字论文内全部正确。",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/audit_maintext_numbers.md",
  "tags": "['audit', 'paper', 'numbers', 'consistency']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "audit_maintext_numbers",
    "type": "report",
    "description": "主文定量数字全面审计：检查每个数字的可追溯性、跨位置一致性、精度一致性。发现14个问题，3个严重（跨表不一致），7个bug-prone数字论文内全部正确。",
    "project": "struct_self_consist_ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/audit_maintext_numbers.md",
    "tags": "['audit', 'paper', 'numbers', 'consistency']"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-24T04:44:58.519926+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_2206ff\", \"name\": \"audit_maintext_numbers\", \"type\": \"report\", \"description\": \"主文定量数字全面审计：检查每个数字的可追溯性、跨位置一致性、精度一致性。发现14个问题，3个严重（跨表不一致），7个bug-prone数字论文内全部正确。\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/audit_maintext_numbers.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T04:44:46.081214+00:00\", \"tags\": [\"audit\", \"paper\", \"numbers\", \"consistency\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_maintext-numbers_20260524T042759",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-24T04:44:58.520231+00:00_

审计完成。发现 14 个问题：

**3 个严重问题（跨表不一致）：**
- **#5**: Tab selection vs Tab fewnerd SciERC 基线不一致（Greedy .645 vs .663，LP Δ +0.2pp vs +0.61pp）— 同一设置两个表不同数字
- **#10**: SciERC EM AUROC 论文 .631 vs registry .7493 — registry 和 provenance 从未更新
- **#11**: LP ρ 在两个表间不一致（SciERC .205 vs .159）

**主要中等问题：**
- Construction +1.40pp (4-seed non-CV) vs +0.88pp (5-fold CV) 在同一段落混用未说明
- LP selection +1.39pp 主种子 registry 显示 1.36pp
- 多个数字无法从 registry 追溯（appendix 来源或统计计算）

**7 个 bug-prone 数字全部正确** ✅（.631 不是 .749、13.0pp 不是 11.4pp、+0.6pp 不是 +0.61pp 等）

报告已写入 `artifacts/audit_maintext_numbers.md` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_maintext-numbers_20260524T042759"
}
```

</details>

---
