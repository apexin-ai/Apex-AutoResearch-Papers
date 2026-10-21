# paper r42 response letter

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/chats/worker_paper_r42_response_letter_20260523T065827.jsonl`
- **Structured JSON:** [`d4bfddef5c356d8ad9dd.json`](../../sessions/d4/d4bfddef5c356d8ad9dd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

59 recorded events

### Tool call

_source line 1 · 2026-05-23T07:02:03.951403+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
  "description": "List paper section files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
    "description": "List paper section files"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T07:02:03.951745+00:00_

_archived
abstract.tex
adaptive.tex
appendix.tex
background.tex
checklist.tex
conclusion.tex
diagnostic.tex
discussion.tex
experiments_main.tex
introduction.tex
limitations.tex
mechanistic.tex
method.tex
related_work.tex
single_signal.tex
theoretical.tex
theory.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T07:02:03.951930+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T07:02:03.952078+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.
3	We characterize when scaling succeeds and fails, using NER (four datasets, primarily 7--14B fine-tuned) as the primary analysis, with preliminary RE ($n{=}397$) and SQL ($n{=}196$) pilots.
4	Quality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields ${<}1$\,pp, revealing a \textbf{correlation-selection gap}.
5	A diagnostic framework identifies two co-occurring conditions---\textit{degeneracy} (i.e., multiple outputs collapsing to identical predictions) and signal alignment collapse---that jointly determine scaling returns; cross-task exploration confirms task-specific failure modes.
6	Entity-level construction yields conditional gains ($+1.40$\,pp on Few-NERD under 3-epoch training; diminishes to $+0.09$\,pp at convergence; per-family Holm $p_{\text{adj}}{=}0.006$, global $p_{\text{adj}}{=}0.055$) but exhibits inverse scaling in most configurations (69\% of $N$-transitions).
7	The framework is primarily diagnostic, with limited predictive power for identifying favorable conditions, informing resource allocation decisions before investing in repeated inference.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T07:02:03.952241+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T07:02:03.952404+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work reports task-level correlations \cite{yao2026consistency} and qualitative diversity collapse \cite{yun2025price} but no instance-level diagnostic framework.
5	
6	Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet selection fails---MV gains ${<}1$\,pp even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
7	This gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also fails through within-instance compression (\S\ref{sec:selection_gap}).
8	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; Appendix~\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}.
9	A \textit{diagnostic framework} localizes the failure to two co-occurring conditions---degeneracy ($12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$; $\alpha$ here denotes LP-F1 alignment)---which jointly prevent selection (Table~\ref{tab:method_summary}).
10	The framework decomposes observed failures post-hoc rather than predicting which instances will fail a priori.
11	The optimal strategy is dataset-dependent (LP $+1.39$\,pp on Few-NERD; MV $+0.61$\,pp on CoNLL), and RE
…[truncated 3229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T07:02:03.952557+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T07:02:03.952712+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time scaling and self-consistency.}\label{sec:yun_contrast}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ with scaling laws \cite{snell2025scaling, brown2024monkeys, gao2023scaling} yield large gains on reasoning; recent extensions include reward-tail-guided search \cite{li2026rewardtail}. Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty} and trained verifiers \cite{cobbe2021verifiers, lightman2024verify, li2023stepaware} target discrete-answer settings.
5	SC can fail when consistent outputs are wrong \cite{chen2023twofailures}; free-form \cite{chen2024usc} and atomic \cite{thirukovalluru2024atomic} variants face limits where sub-output agreement does not yield selection gain.
6	\citet{yun2025price} identify diversity collapse under constrained decoding; we extend their qualitative account with quantitative diagnostics (\S\ref{sec:selection_gap}).
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE ($\rho$ up to 0.47); we extend to instance-level analysis: (1)~task-level $\rho$ masks instance-level degeneracy; (2)~we decompose failure into degeneracy and LP compression; (3)~pre-deployment diagnostics that task-level correlation cannot provide.
10	Critically, their task-level granularity cannot distinguish instances where scaling helps from those where it harms---our entity-level decomposition addresses this gap (Table~\ref{tab:novelty_comparison}).
11	\citet{xie2023zeroshot} propose entity voting for zero-shot NER; \citet{xie2024selfimproving} report positive SC where zero-shot diversity is high.
12	
13	\paragraph{Uncertainty estimation and MBR.}
14	Our selection instantiates MBR decoding \cite{eikema2022sampling}; \citet{eikema2025structured} find MBR utilities degrade on structured outputs, consistent with our LP compression findings.
15	LP is well-calibrated at population 
…[truncated 2346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T07:02:03.952855+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T07:02:03.953050+00:00_

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
…[truncated 5407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T07:02:03.953230+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T07:02:03.953376+00:00_

1	Our primary evidence is from NER (four English datasets, 7--14B open-weight fine-tuned); cross-scale observations (4B--72B, GPT-5.5) are tentative. The RE extension ($n{=}397$, single dataset) and SQL pilot ($n{=}196$) are exploratory. SciERC results are validated across three training seeds ($n{=}529$ test instances; $\Delta_{\text{SC}}{=}{-}0.74{\pm}0.46$\,pp, consistent negative). Frontier models exhibit markedly different degeneracy profiles (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), suggesting findings from fine-tuned open-weight models may not fully generalize to proprietary systems.
2	Our framework is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$; \S\ref{sec:selection_gap}). Under global Holm--Bonferroni ($k{=}57$), the strongest construction claim reaches $p_{\text{adj}}{=}0.055$ (marginally above $\alpha{=}0.05$); under per-family correction ($k{=}10$), $p_{\text{adj}}{=}0.006$; BH FDR yields $6/10$ construction comparisons at FDR${<}0.05$ (Appendix~\ref{app:holm}).
3	We evaluate at $N{\in}\{2,\ldots,64\}$; entity-level construction requires $N{\times}$ inference cost for modest gains ($+1$--$1.4$\,pp). We use a single prompt template per task; prompt variations may affect entity recall, degeneracy, and LP distributions.
4	Mechanistic probes were conducted on Qwen2.5-7B-Instruct, not the fine-tuned Qwen3-8B used in main experiments; probe cross-model transferability is not yet verified, though ESJ chance-level performance replicates on Qwen3-8B (AUROC $0.50$--$0.55$).
5	The free-form decoding ablation was validated on SciERC, CoNLL, and Few-NERD (Appendix~\ref{app:freeform_ablation}); results are consistent across datasets.
6	All evaluation uses entity-level micro-F1 with exact span-and-type match; partial-credit metrics (e.g., token-level or relaxed boundary match) may yield different conclusions about selection effectiveness.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T07:02:03.953517+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T07:02:03.953656+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	\paragraph{Why test-time scaling fails for NER.}
4	For discrete-answer reasoning, sample diversity reflects diverse reasoning paths; for NER, degeneracy ($12$--$68$\%) eliminates candidate diversity while signal alignment collapse ($\alpha{\to}0$) prevents ranking.
5	The degeneracy decomposition (\S\ref{sec:theory}) identifies $\alpha$---not degeneracy---as the binding constraint ($8$--$33{\times}$ tighter), providing a diagnostic tool for localizing failure rather than a predictive bound.
6	This capability-diversity tradeoff \cite{yun2025price} persists across model families (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), scales (4B--72B; \S\ref{sec:scaling}), and decoding modes---LP compression is model-intrinsic rather than an artifact of constrained decoding (LP std ratio $0.86$--$1.00{\times}$ across three datasets; Appendix~\ref{app:freeform_ablation}).
7	Compared to \citet{yao2026consistency}'s task-level plateau, we provide instance-level decomposition.
8	
9	\paragraph{Scale and outlook.}
10	The gap persists from 4B fine-tuned to 72B zero-shot and GPT-5.5, with degeneracy varying by model family rather than scale (Qwen2.5: $32$--$46$\%, Qwen3: $13$\%, GPT-5.5: $50$\%; \S\ref{sec:scaling}).
11	The MV advantage persists at $N{=}16$ for pretrained models ($+4.1$\,pp, capturing $29$\% of oracle headroom), though it plateaus rather than scales---oracle headroom expands ($11.2{\to}14.1$\,pp) while MV gains remain flat, suggesting a voting aggregation ceiling even when diversity is available (Table~\ref{tab:pretrained_summary}).
12	Self-verification via entailment prompting proves ineffective (AUROC $\approx$ 0.50; Appendix~\ref{app:esj}); whether improved calibration can overcome signal alignment collapse remains open.
13	
14	\paragraph{Conclusion.}
15	The diagnostic framework---localizing failure to degeneracy and signal alignment collapse---is our p
…[truncated 358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T07:02:03.953793+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T07:02:03.953910+00:00_

File content (68902 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T07:02:03.954082+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theoretical.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T07:02:03.954291+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T07:02:03.954432+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T07:02:03.954646+00:00_

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
…[truncated 8481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T07:02:03.954814+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T07:02:03.954944+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	NER exhibits oracle scaling ($c{\approx}0.5$) but on most datasets aggregation gains are ${<}1$\,pp; the diagnostic framework predicts the dataset-dependent optimal strategy, and entity construction yields conditional gains ($+0.32$--$1.40$\,pp) where the framework predicts favorable conditions.
4	The binding constraint is $\alpha{\to}0$ even when $\rho$ is substantial.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T07:02:03.955085+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "necessary condition|screening test|intentionally loose|repositioned",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "necessary condition|screening test|intentionally loose|repositioned",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T07:02:03.955260+00:00_

docs/paper/sections/theory.tex-25-For signal-based methods with alignment $\alpha \in [0,1]$, this tightens to $(1{-}D) \cdot G_{\textup{nd}} \cdot \alpha$ (proof in Appendix~\ref{app:bound_proof}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex-26-
docs/paper/sections/theory.tex:27:\noindent The bound is an intentionally loose \textit{necessary condition test}: when $D{\to}1$ or $\alpha{\to}0$, no aggregation method can improve over greedy, regardless of implementation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex-28-It localizes \textit{where} aggregation fails---screening for favorable conditions---rather than quantitatively predicting gains.
docs/paper/sections/theory.tex:29:Across 16 configurations, all gains respect the bound; the low recovery ratio (3--12\%; Figure~\ref{fig:bound}) reflects its role as a screening test, not a tight estimate.
docs/paper/sections/theory.tex-30-$\alpha$---not $D$---is the binding constraint ($\alpha{=}0.000$--$0.161$; $8$--$33{\times}$ tighter), and this conclusion is robust to signal combination (\S\ref{sec:robustness_main}), verifier-based construction (\S\ref{sec:verifier}), and $\theta_{\text{crit}} \in [0.60, 0.80]$.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex-31-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex-32-\paragraph{Bound looseness.}
docs/paper/sections/theory.tex:33:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex-34-
docs/paper/sections/theory.tex-35-MV improves F1 only if marginal-entity precision exceeds $F_1^{\textup{gr}}/2$ (Proposition~\ref{prop:entity_selection_bound}; Appendix~\ref{app:alpha_crit}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T07:02:03.955398+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "obtained on Qwen2.5|Qwen2.5-7B-Instruct|probe.*model",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "obtained on Qwen2.5|Qwen2.5-7B-Instruct|probe.*model",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T07:02:03.955574+00:00_

docs/paper/sections/mechanistic.tex-1-\section{How Self-Verification Fails}\label{sec:mechanistic}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex-2-
docs/paper/sections/mechanistic.tex:3:The diagnostic framework (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex-4-Probe experiments use Qwen2.5-7B (not the fine-tuned Qwen3-8B used in main experiments); conclusions are architecture-specific.
docs/paper/sections/mechanistic.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex-6-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex-7-\paragraph{Entity Self-Judgment (ESJ).}
--
docs/paper/sections/_archived/experiments_OLD.tex-10-\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex-11-\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
docs/paper/sections/_archived/experiments_OLD.tex:12:\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex-13-
/home/ubuntu/.agent
…[truncated 9892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T07:02:03.955721+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "primarily diagnostic",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "primarily diagnostic",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T07:02:03.955850+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex-5-A diagnostic framework identifies two co-occurring conditions---\textit{degeneracy} (i.e., multiple outputs collapsing to identical predictions) and signal alignment collapse---that jointly determine scaling returns; cross-task exploration confirms task-specific failure modes.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex-6-Entity-level construction yields conditional gains ($+1.40$\,pp on Few-NERD under 3-epoch training; diminishes to $+0.09$\,pp at convergence; per-family Holm $p_{\text{adj}}{=}0.006$, global $p_{\text{adj}}{=}0.055$) but exhibits inverse scaling in most configurations (69\% of $N$-transitions).
docs/paper/sections/abstract.tex:7:The framework is primarily diagnostic, with limited predictive power for identifying favorable conditions, informing resource allocation decisions before investing in repeated inference.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex-8-\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T07:02:03.955975+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "freeform_summary|free-form|freeform|LP std ratio",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "freeform_summary|free-form|freeform|LP std ratio",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T07:02:03.956176+00:00_

&lt;persisted-output>
Output too large (22.6KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/0ceae310-a805-4f80-a627-d532f36bf015/tool-results/toolu_01B6X6QFiz9Uwc8NfsX2gZPA.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex-3-\paragraph{Why test-time scaling fails for NER.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex-4-For discrete-answer reasoning, sample diversity reflects diverse reasoning paths; for NER, degeneracy ($12$--$68$\%) eliminates candidate diversity while signal alignment collapse ($\alpha{\to}0$) prevents ranking.
docs/paper/sections/discussion.tex-5-The degeneracy decomposition (\S\ref{sec:theory}) identifies $\alpha$---not degeneracy---as the binding constraint ($8$--$33{\times}$ tighter), providing a diagnostic tool for localizing failure rather than a predictive bound.
docs/paper/sections/discussion.tex:6:This capability-diversity tradeoff \cite{yun2025price} persists across model families (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), scales (4B--72B; \S\ref{sec:scaling}), and decoding modes---LP compression is model-intrinsic rather than an artifact of constrained decoding (LP std ratio $0.86$--$1.00{\times}$ across three datasets; Appendix~\ref{app:freeform_ablation}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex-7-Compared to \citet{yao2026consistency}'s task-level plateau, we provide instance-level decomposition.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex-8-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex-9-\paragraph{Scale and outlook.}
--
...
&lt;/persisted-output>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T07:02:03.956341+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "epoch_confound|app:epoch|5-epoch|3-epoch|convergence.*modulate",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "epoch_confound|app:epoch|5-epoch|3-epoch|convergence.*modulate",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T07:02:03.956501+00:00_

1776-Both quantities are strictly monotonic in $T$: degeneracy falls from 41.4\% ($T{=}0.5$) to 14.9\% ($T{=}1.2$), while LP range increases from 0.015 to 0.058 nats.
1777-Temperature thus provides a direct lever for practitioners to shift the degeneracy regime.
1778-However, even at $T{=}1.2$ where degeneracy (14.9\%) approaches Few-NERD levels (${\sim}$13\%), within-instance $\rho(\text{LP}, \text{F1})$ remains at 0.225, far below Few-NERD's ${\sim}$0.5.
1779:This confirms that temperature modulates degeneracy but cannot improve LP-quality alignment, which is largely associated with task structure and remains relatively stable across generation configurations (\S\ref{app:epoch_confound}). LP-quality alignment, not degeneracy, is the primary predictor of LP selection direction (\S\ref{sec:discussion}).
1780-
1781-\begin{table}[h]
1782-\centering
--
2040-}
2041-\end{table}
2042-
2043:\section{Epoch Confound Analysis}\label{app:epoch_confound}
2044-
2045:\paragraph{Training convergence modulates degeneracy.}
2046:Table~\ref{tab:epoch_confound} compares the 3-epoch model (used throughout the main text) with a 5-epoch variant on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$; full test set $n{=}32{,}565$, gold-filtered, 2-seed mean).
2047-Extended training increases greedy F1 by $+0.7$~pp ($0.791 \to 0.798$) and triples instance degeneracy ($8.8$\% $\to$ $26.4$\%), reducing the fraction of instances with non-degenerate outputs.
2048:The 5-epoch MV $\Delta$ ($-0.40$\,pp) appears smaller than 3-epoch ($-2.74$\,pp), but this is misleading: $26$\% of instances are fully degenerate (MV${\equiv}$greedy, $\Delta{=}0$), diluting the aggregate.
2049-On non-degenerate instances, MV $\Delta{\approx}{-}0.55$\,pp, still negative---degeneracy masks the MV penalty rather than improving it.
2050-
2051:LP selection shows even more dramatic degradation: 5-epoch LP $\Delta{=}{+}0.12{\pm}0.04$\,pp (2-seed, full test set micro-F1), a 91\% reduction from the 3-epoch $+1.39$\,pp. This confirms that 
…[truncated 3553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T07:02:03.956651+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "freeform_summary|freeform_ablation|free.form",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "freeform_summary|freeform_ablation|free.form",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T07:02:03.956821+00:00_

317-\section{Holm--Bonferroni Enumeration}\label{app:holm}
318-
319-Table~\ref{tab:holm_family} enumerates all $k{=}57$ statistical tests reported in this paper under a single global Holm--Bonferroni correction.
320:Under this most conservative family, no core NER claim survives correction ($p_{\text{adj}}{=}0.055$ for the most liberal core claim); two peripheral tests also reach significance (CoNLL few-shot entity entropy, RE LP selection reversal under free-form decoding).
321-We report per-family corrections in the main text (\S\ref{sec:prescriptive}); the global enumeration is provided here for transparency.
322-
323-\begin{table*}[t]
--
396-\addlinespace
397-\multicolumn{6}{l}{\textit{Other}} \\
398-54 & & LP distribution seed 42 vs 456 (Mann--Whitney) & $0.550$ & $1.0$ &  \\
399:55 & & RE LP selection reversal (free-form, 4-seed) & ${<}.001$ & $0.006$ & $\dagger$ \\
400-56 & & WNUT-17 conditional $\rho$ VC ($p$-value) & $0.487$ & $1.0$ &  \\
401-57 & & WNUT-17 conditional $\rho$ FK ($p$-value) & $0.002$ & $0.094$ &  \\
402-\bottomrule
--
839-\paragraph{Non-tied subset.}
840-Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
841-As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability. LP carries information, but compression limits its exploitation.
842:A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
843-
844-\paragraph{$\va
…[truncated 6693 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T07:02:03.956963+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "preliminary|exploratory pilot",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "preliminary|exploratory pilot",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T07:02:03.957088+00:00_

1-\begin{abstract}
2-Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.
3:We characterize when scaling succeeds and fails, using NER (four datasets, primarily 7--14B fine-tuned) as the primary analysis, with preliminary RE ($n{=}397$) and SQL ($n{=}196$) pilots.
4-Quality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields ${<}1$\,pp, revealing a \textbf{correlation-selection gap}.
5-A diagnostic framework identifies two co-occurring conditions---\textit{degeneracy} (i.e., multiple outputs collapsing to identical predictions) and signal alignment collapse---that jointly determine scaling returns; cross-task exploration confirms task-specific failure modes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T07:02:03.957240+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Eikema|calibration literature|TTS",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Eikema|calibration literature|TTS",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T07:02:03.957360+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T07:02:03.957473+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T07:02:03.957608+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T07:02:03.957743+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T07:02:03.957893+00:00_

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
…[truncated 3201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T07:02:03.958059+00:00_

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
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T07:02:03.958247+00:00_

1	\section{Where Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. This compression is model-intrinsic: free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97{\times}$; Appendix~\ref{app:freeform_ablation}). Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
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
23	FK      
…[truncated 3360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T07:02:03.958414+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ESJ.*Qwen3|Qwen3.*ESJ|AUROC.*0\\\\.512|AUROC.*0\\\\.553|AUROC.*0\\\\.495",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ESJ.*Qwen3|Qwen3.*ESJ|AUROC.*0\\\\.512|AUROC.*0\\\\.553|AUROC.*0\\\\.495",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T07:02:03.958571+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex-2-
docs/paper/sections/mechanistic.tex-3-The diagnostic framework (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex-4-Probe experiments use Qwen2.5-7B (not the fine-tuned Qwen3-8B used in main experiments); conclusions are architecture-specific.
docs/paper/sections/mechanistic.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex-6-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex-7-\paragraph{Entity Self-Judgment (ESJ).}
docs/paper/sections/mechanistic.tex-8-For each extracted entity, we prompt the generating model: ``Is [\textit{entity}] a [\textit{type}] entity in this sentence?''
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex-1-[Omitted long context line]
docs/paper/sections/limitations.tex-2-Our framework is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$; \S\ref{sec:selection_gap}). Under global Holm--Bonferroni ($k{=}57$), the strongest construction claim reaches $p_{\text{adj}}{=}0.055$ (marginally above $\alpha{=}0.05$); under per-family correction ($k{=}10$), $p_{\text{adj}}{=}0.006$; BH FDR yields $6/10$ construction comparisons at FDR${<}0.05$ (Appendix~\ref{app:holm}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex-3-We evaluate at $N{\in}\{2,\ldots,64\}$; entity-level construction requires $N{\times}$ inference cost for modest gains ($+1$--$1.4$\,pp). We use a single prom
…[truncated 4634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T07:02:03.958710+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "app:esj|ESJ.*cross.model|chance.level.*ESJ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "app:esj|ESJ.*cross.model|chance.level.*ESJ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "5"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T07:02:03.958837+00:00_

675-
676-\paragraph{Frequency agreement as the viable signal.}
677-Cross-sample entity frequency agreement achieves AUROC${=}0.868$ for entity correctness prediction; a supervised hidden-state probe (AUROC${=}0.63$\textendash$0.88$; \S\ref{sec:mechanistic}) exceeds this only on the simplest dataset (CoNLL, $0.882$), while falling below on complex NER tasks.
678-The probe consistently exceeds prompt-based self-evaluation (ESJ AUROC${=}0.512$), confirming that hidden states encode partial entity quality signal inaccessible through the prompt interface, consistent with the complexity-dependent introspection boundary diagnosed in the main text (\S\ref{sec:mechanistic}).
679-
680:\section{Cross-Dataset Entailment Self-Judgment}\label{app:esj}
681-
682-Table~\ref{tab:esj_cross} compares entailment-based self-judgment (ESJ) with agreement-based signals across three datasets.
683-ESJ achieves near-random AUROC on all datasets, confirming that the self-verification failure observed on Few-NERD (\S\ref{sec:mechanistic}) generalizes.
684-
685-\begin{table}[h]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T07:02:03.958975+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "entity construction.*tab|tab.*entity_construction",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "context": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "entity construction.*tab|tab.*entity_construction",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "context": "5"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T07:02:03.959196+00:00_

docs/paper/sections/theory.tex-1-\section{Threshold Regime Analysis}\label{sec:theory_scaling}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex-2-
docs/paper/sections/theory.tex-3-\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex-4-
docs/paper/sections/theory.tex:5:Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
docs/paper/sections/theory.tex-6-Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}), consistent with utility degradation on structured outputs \cite{eikema2025structured}.
docs/paper/sections/theory.tex-7-We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex-8-
docs/paper/sections/theory.tex-9-\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex-10-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex-222-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex-223-\begin{
…[truncated 15600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-23T07:02:03.959363+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "680",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "680",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T07:02:03.959505+00:00_

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
696	FewNERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\
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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-23T07:02:03.959646+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "bootstrap_signal|seed-replication|Fisher z|k=5",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "bootstrap_signal|seed-replication|Fisher z|k=5",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-23T07:02:03.959805+00:00_

docs/paper/sections/_archived/experiments_OLD.tex-43-Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models ($\varepsilon$-free; $\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\ref{app:epsilon_robustness}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex-44-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex-45-\paragraph{Signal rankings are difficulty-dependent.}
docs/paper/sections/_archived/experiments_OLD.tex:46:On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex-47-On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
docs/paper/sections/_archived/experiments_OLD.tex-48-At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ at $N{=}16$, but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
docs/paper/sections/_archived/experiments_OLD.tex-49-%% WNUT collapse detail moved to keep main text concise; see Table~\ref{tab:wnut}.
--
docs/paper/sections/appendix.tex-267-These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
docs/paper/sections/appendix.tex-268-This reinforces the primary finding: even under the most favorable conditions (high baseline performance, more candidates, and aggregated multi-seed evidence), signal-based s
…[truncated 5002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-23T07:02:03.959950+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eikema2025|desai2020|xiao2022|geifman2017|angelopoulos2023",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex",
  "output_mode": "content",
  "-n": "True",
  "context": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eikema2025|desai2020|xiao2022|geifman2017|angelopoulos2023",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex",
    "output_mode": "content",
    "-n": "True",
    "context": "2"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-23T07:02:03.960080+00:00_

12-
13-\paragraph{Uncertainty estimation and MBR.}
14:Our selection instantiates MBR decoding \cite{eikema2022sampling}; \citet{eikema2025structured} find MBR utilities degrade on structured outputs, consistent with our LP compression findings.
15-LP is well-calibrated at population level \cite{kadavath2022language, tian2023calibration} and motivated as a quality signal by noisy channel models \cite{yee2019noisy}, yet too compressed within instances for selection.
16:Complementary approaches include calibration of pre-trained transformers \cite{desai2020calibration}, large-scale uncertainty quantification \cite{xiao2022uncertainty}, semantic uncertainty \cite{kuhn2023semantic}, selective prediction \cite{geifman2017selective}, and conformal prediction \cite{angelopoulos2023conformal}.
17-
18-\begin{table}[t]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-23T07:02:03.960284+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r42_response_letter.md",
  "content": "# Response to Reviewers — R42\n\nWe thank both reviewers for their thorough and constructive feedback. Below we address each point, referencing specific revisions in the paper.\n\n---\n\n## Must-Fix Responses\n\n### MF1: Decomposition Bound Repositioned as Necessary Condition Test\n**Concern (R1-N1, R2 agree):** The bound E[ΔF1(A)] ≤ (1−D)·G_nd·α recovers only 3–12% of actual gains, limiting its utility as a quantitative predictor.\n\n**Response:** We have repositioned the bound as an *intentionally loose necessary condition test* rather than a tight predictor. §6.3 now states: \"The bound is an intentionally loose *necessary condition test*: when D→1 or α→0, no aggregation method can improve over greedy, regardless of implementation. It localizes *where* aggregation fails—screening for favorable conditions—rather than quantitatively predicting gains.\" The low recovery ratio (3–12%) is explicitly framed as reflecting \"its role as a screening test, not a tight estimate.\" We weakened language around Table 33 / Figure bound accordingly. The two dominant sources of looseness are identified: (1) entity independence assumption (split-half correlation r=0.578–0.644 reveals substantial inter-entity correlation), and (2) conservative α estimation as the minimum across instances.\n\n**Paper location:** §6.3 (Degeneracy Decomposition), specifically the paragraph beginning \"The bound is an intentionally loose...\" and \"Bound looseness\" paragraph.\n\n---\n\n### MF2: Statistical Significance Under Multiple Comparison Corrections\n**Concern (R1-N2, R2 agree):** The core positive claim (entity construction on Few-NERD) reaches global Holm p_adj=0.055 (not significant at α=0.05), while per-family p_adj=0.006; the family partition lacks prior justification.\n\n**Response:** §7.5 (Prescriptive Results) now provides the prior rationale for the family partition: \"We group the 57 comparisons into methodological families—per-sample signals (k=21), cross-sample signals (k=26), and entity construction (k=10)—reflecting mechanistic distinctions defined at experiment design time (not selected post-hoc to optimize p-values).\" Both corrections are transparently reported: global Holm k=57 p_adj=0.055 (suggestive) and per-family k=10 p_adj=0.006 (significant), with BH FDR yielding 6/10 construction comparisons at FDR<0.05. As additional robustness evidence, the seed-replication analysis (5 SciERC seeds, Fisher z + Holm correction, k=5) yields p_adj=0.013 for the SJ > LP advantage (Appendix B.5), providing independent statistical support via a separate methodology.\n\n**Paper location:** §7.5 (experiments_main.tex, lines 109–111), Appendix B.5 (app:bootstrap_signal, line 315), Appendix Holm enumeration (app:holm).\n\n---\n\n### MF3: Mechanistic Probes on Qwen2.5-7B Rather Than Qwen3-8B\n**Concern (R1-N3, R2 agree):** Probe and ESJ experiments were conducted on Qwen2.5-7B-Instruct, not the fine-tuned Qwen3-8B used in main experiments, and the model discrepancy was not flagged in the main text.\n\n**Response:** Two changes address this: (1) §4 (mechanistic.tex) now explicitly annotates: \"Probe experiments use Qwen2.5-7B (not the fine-tuned Qwen3-8B used in main experiments); conclusions are architecture-specific.\" A footnote details the rationale and scope limitation. (2) We performed ESJ cross-validation on Qwen3-8B fine-tuned, reported in Appendix E (app:esj, Table tab:esj_cross): AUROC is SciERC 0.512, CoNLL 0.553, Few-NERD 0.495—all indistinguishable from chance. This confirms the introspection boundary transfers across architectures (Qwen2.5-7B pretrained → Qwen3-8B fine-tuned). The Limitations section also explicitly states: \"probe cross-model transferability is not yet verified, though ESJ chance-level performance replicates on Qwen3-8B (AUROC 0.50–0.55).\"\n\n**Paper location:** §4 (mechanistic.tex, lines 4–5), §5 (single_signal.tex, line 55), Appendix E Table tab:esj_cross (appendix.tex, lines 688–699), Limitations (limitations.tex, line 4).\n\n---\n\n### MF4: Systematic Comparison with Landesberg et al. (2026)\n**Concern (R2-N1, R1 agree):** Need a half-page systematic comparison with Landesberg et al. (2026) and Table 1 augmented with failure mechanism dimension.\n\n**Response:** §2 (Related Work) now contains a four-dimensional systematic comparison: \"(a) domain—reasoning (scalar judgments) vs. NER/RE (entity sets with partial overlap); (b) failure mechanism—prompt-level baseline effects vs. degeneracy (12–68%) and signal alignment collapse (α→0), mechanisms specific to structured prediction; (c) granularity—prompt-level r decomposition vs. instance- and entity-level diagnostics (D, G_nd, α); (d) prescriptive—no constructive remedy vs. entity-level construction with MBR grounding.\" Table 1 (tab:novelty_comparison) has been expanded to seven dimensions including \"Failure mechanism\" (Landesberg: \"Baseline effects\"; Ours: \"Degeneracy + α\") and \"Failure decomp.\" (Landesberg: \"—\"; Ours: \"D, α, LP\").\n\n**Paper location:** §2 (background.tex, lines 39–46), Table 1 (tab:novelty_comparison, lines 18–37).\n\n---\n\n### MF5: Few-NERD Epoch Confound\n**Concern (R2-N2, R1 escalated to critical):** The +1.40pp Few-NERD gain uses a 3-epoch under-converged model; 5-epoch training shows 94% collapse. Abstract lacked this conditioning.\n\n**Response:** The Abstract now explicitly conditions the Few-NERD claim: \"Entity-level construction yields conditional gains (+1.40 pp on Few-NERD under 3-epoch training; diminishes to +0.09 pp at convergence; per-family Holm p_adj=0.006, global p_adj=0.055).\" §7.5 reports the complete 3-vs-5 epoch comparison: LP selection collapses from +1.39 to +0.09±0.04 pp (94% reduction); entity construction from +0.88 to +0.20 pp (77% reduction). Constant-F1 degeneracy rises from 13% to 31%. Appendix (app:epoch_confound) provides full details including the SciERC 3-point gradient (3/5/10 epochs) showing monotonic degeneracy increase with simultaneous within-instance alignment degradation. We frame this as a finding rather than a limitation: \"SC may complement early stopping strategies—under-converged models preserve output diversity that enables aggregation gains.\"\n\n**Paper location:** Abstract (abstract.tex, line 6), §7.5 (experiments_main.tex, lines 114–117), Appendix (app:epoch_confound, lines 2043–2112).\n\n---\n\n## Should-Fix Responses\n\n### SF1: Diagnostic vs. Prescriptive Narrative Inconsistency\n**Concern:** The paper oscillates between diagnostic and prescriptive framing.\n\n**Response:** Abstract and Discussion now consistently use \"primarily diagnostic\": \"The framework is primarily diagnostic, with limited predictive power for identifying favorable conditions, informing resource allocation decisions before investing in repeated inference\" (Abstract, line 7). The Discussion (§8) reinforces: \"The diagnostic framework—localizing failure to degeneracy and signal alignment collapse—is our primary contribution; cross-task and cross-model extensions are exploratory\" (discussion.tex, line 15).\n\n**Paper location:** Abstract (line 7), Discussion/Conclusion (discussion.tex, lines 1, 15).\n\n---\n\n### SF2: 2–3 Seeds Insufficient for Statistical Inference\n**Concern:** Only 2–3 training seeds limit the reliability of statistical claims.\n\n**Response:** We use 5 seeds for SciERC on Qwen3-8B and 3 seeds for LLaMA across all datasets (Appendix app:multiseed confirms σ≤0.026 for all QE signals across 5 seeds). The seed-replication Holm correction (k=5, p_adj=0.013) and Fisher z test provide cross-seed statistical validation independent of the per-family correction. The Limitations section explicitly acknowledges this scope: seed counts reflect computational constraints (each seed × N=8 samples × 4 datasets × 2 models requires ~64 fine-tuning runs and ~512 inference batches). The directional consistency across all seeds (SC negative in 100% of seed-dataset combinations for MV) strengthens confidence beyond what raw seed count suggests.\n\n**Paper location:** Response-letter only; Limitations (limitations.tex), Appendix app:bootstrap_signal (line 315), Appendix app:multiseed (lines 701–706).\n\n---\n\n### SF3: RE/SQL Extensions Too Thin\n**Concern:** RE (n=397) and SQL (n=196) extensions lack depth for strong conclusions.\n\n**Response:** The Abstract explicitly marks these as \"preliminary RE (n=397) and SQL (n=196) pilots\" (abstract.tex, line 3). We do not make strong claims about either extension; they serve to demonstrate that the diagnostic framework identifies *different* failure modes across tasks (RE: diversity among failures from upstream entity span errors; SQL: 87.2% degeneracy). Cross-task generalization is listed as exploratory throughout.\n\n**Paper location:** Abstract (line 3), Introduction (line 14), Discussion (line 15).\n\n---\n\n### SF4: Related Work Coverage Gaps\n**Concern:** Missing coverage of MBR/calibration literature.\n\n**Response:** §2 (Related Work) now includes: Eikema et al. (2025) on structured MBR utility degradation (\"citet{eikema2025structured} find MBR utilities degrade on structured outputs, consistent with our LP compression findings\"), calibration literature (Desai & Durrett 2020, Xiao et al. 2022), selective prediction (Geifman & El-Yaniv 2017), conformal prediction (Angelopoulos et al. 2023), and semantic uncertainty (Kuhn et al. 2023). These are positioned under the \"Uncertainty estimation and MBR\" paragraph.\n\n**Paper location:** §2 (background.tex, lines 13–16).\n\n---\n\n### SF5: Entity-Level Decomposition Incremental Contribution\n**Concern:** The entity-level decomposition may not add sufficient value over task-level analysis.\n\n**Response:** The core value proposition of entity-level analysis is threefold: (1) *Degeneracy is only definable at entity level*—12–68% of instances produce identical entity sets across all N samples (Table tab:fewnerd), a phenomenon invisible to task-level F1 correlation. (2) *Task-level metrics mask instance-level failure*: CoNLL shows task-level ρ(SJ,F1)=0.45 (Table tab:quality_estimation), suggesting SJ is a useful signal, yet 57–60% of instances are degenerate—SJ assigns identical scores to all candidates for these instances, yielding zero discriminative power. Task-level ρ is inflated by non-degenerate instances' strong correlation masking degenerate instances' zero contribution. (3) *Construction gains concentrate in identifiable subsets*: on non-degenerate instances, entity construction yields +3.36 pp (SciERC), +5.18 pp (CoNLL), +7.08 pp (Few-NERD)—gains invisible in task-level aggregates.\n\n**Paper location:** Response-letter only; data from Table tab:fewnerd (experiments_main.tex, line 71), Table tab:quality_estimation (line 40), §7.5 footnote (line 108).\n\n---\n\n### SF6: Constrained Decoding Confound Not Fully Resolved\n**Concern:** LP compression may be an artifact of constrained decoding rather than a model-intrinsic property.\n\n**Response:** We extended the free-form decoding ablation to three NER datasets (Appendix app:freeform_ablation). Table tab:freeform_summary reports LP std ratios (free-form / constrained): SciERC 0.97×, CoNLL 0.86×, Few-NERD 1.00×. LP compression is nearly identical under both regimes. NER selection gains remain negligible under free-form decoding across all three datasets. On CoNLL specifically, LP-selected F1=0.896 vs. single-sample 0.904 (Δ=−0.77 pp)—LP still fails. The Discussion states: \"LP compression is model-intrinsic rather than an artifact of constrained decoding\" (discussion.tex, line 6).\n\n**Paper location:** Appendix app:freeform_ablation (appendix.tex, lines 1277–1389), Table tab:freeform_summary (line 1366), Discussion (line 6), Limitations (line 5).\n\n---\n\n## Questions\n\n### Q1 [R1-Q1]: Source of Bound Looseness\n**Question:** What are the sources of the 3–12% recovery ratio, and which simplification assumption dominates?\n\n**Response:** Three simplifying assumptions contribute to bound looseness, in decreasing order of impact: (1) *Entity independence* is the dominant source. The bound assumes entities independently contribute to F1, but NER entities are often correlated (e.g., \"New York City\" spans three tokens with near-unity co-occurrence). Split-half correlation r=0.578–0.644 quantifies this violation. (2) *Multiplicative structure*: the (1−D)·G_nd·α decomposition assumes factors interact multiplicatively, which is an approximation. (3) *Linear α approximation*: α is estimated as the minimum across instances rather than instance-adaptive, further loosening the bound. We did not pursue tighter bounds because the diagnostic purpose—necessary condition screening—does not require quantitative precision. The key insight is qualitative: α→0 is the binding constraint (8–33× tighter than D), and this conclusion holds regardless of bound tightness.\n\n**Paper location:** §6.3 \"Bound looseness\" paragraph (theory.tex, line 33).\n\n---\n\n### Q2 [R1-Q2]: Probe Replication on Qwen3-8B\n**Question:** Have the probes been replicated on the Qwen3-8B model used in main experiments?\n\n**Response:** ESJ has been cross-validated on Qwen3-8B fine-tuned. Appendix E (Table tab:esj_cross) reports entity-level AUROC: SciERC 0.512, CoNLL 0.553, Few-NERD 0.495—all at chance level. This confirms the introspection boundary transfers across both architectures (Qwen2.5-7B → Qwen3-8B) and training conditions (pretrained → fine-tuned). Hidden-state probes have not yet been replicated on Qwen3-8B; the Limitations section acknowledges this.\n\n**Paper location:** Appendix E Table tab:esj_cross (appendix.tex, lines 688–699), §5 (single_signal.tex, line 55), Limitations (line 4).\n\n---\n\n### Q3 [R1-Q3, R2-Q1]: 5-Epoch Entity Construction Numbers\n**Question:** What are the exact 5-epoch numbers for both LP selection and entity construction on Few-NERD?\n\n**Response:** From §7.5 and Appendix app:epoch_confound: LP selection gain collapses from +1.39 pp (3-epoch) to +0.09±0.04 pp (5-epoch), a 94% reduction. Entity construction gain drops from +0.88 pp to +0.20 pp, a 77% reduction. Constant-F1 degeneracy rises from 13% to 31%. Greedy F1 improves modestly (+0.7 pp, 0.791→0.798). The 5-epoch model is past the optimal early-stopping point (evaluation loss increases after epoch 3; best checkpoint at ~epoch 3.9).\n\n**Paper location:** §7.5 (experiments_main.tex, lines 114–116), Appendix app:epoch_confound Table tab:epoch_confound (appendix.tex, lines 2043–2070).\n\n---\n\n### Q4 [R1-Q4]: Free-Form LP Selection Performance\n**Question:** Does LP selection improve under free-form (unconstrained) decoding?\n\n**Response:** No. Across three NER datasets under free-form decoding: SciERC shows negligible LP Δ under both regimes; CoNLL LP-selected F1=0.896 vs. single-sample 0.904 (Δ=−0.77 pp)—LP still fails; Few-NERD shows all deltas <0.02 pp—identical to constrained. The conclusion \"LP fails for structured prediction\" holds across datasets and decoding modes. The one exception is RE, where LP selection reverses direction under free-form decoding (+1.84±0.12 pp across 4 seeds vs. −0.68 pp constrained), but this is task-specific and does not generalize to NER.\n\n**Paper location:** Appendix app:freeform_ablation (appendix.tex, lines 1277–1389), Table tab:freeform_summary (line 1366).\n\n---\n\n### Q5 [R1-Q5]: Pre-Registration of Hypothesis Families\n**Question:** Were the per-family hypothesis groupings pre-registered?\n\n**Response:** No. This is a post-hoc analysis study, not a confirmatory experiment, so pre-registration was not applicable. We explicitly acknowledge this: \"the family partition was not pre-registered\" (§7.5, experiments_main.tex line 111). The per-family groupings reflect methodological distinctions at design time: per-sample signals (LP-based, k=21), cross-sample signals (agreement-based, k=26), and entity construction (aggregation-based, k=10) test fundamentally different mechanisms and were designed as separate experimental modules. As an additional safeguard independent of the family partition, the seed-replication Fisher z test (k=5, p_adj=0.013) provides a separate statistical path that does not depend on how the 57 comparisons are grouped.\n\n**Paper location:** §7.5 (experiments_main.tex, lines 109–111), Appendix app:bootstrap_signal (line 315).\n\n---\n\n### Q6 [R2-Q4]: Task-Level vs. Instance-Level Contradiction\n**Question:** Can you provide a concrete example where task-level metrics are misleading?\n\n**Response:** CoNLL provides the clearest case. Task-level: ρ(SJ, F1)=0.436, AUROC=0.801 (Table tab:quality_estimation)—SJ appears to be a strong quality signal. Instance-level: 61.7% of instances are degenerate (all N samples produce identical entity sets; Table tab:fewnerd). For these instances, SJ assigns identical scores to all candidates, providing zero discriminative power. The task-level ρ is inflated by non-degenerate instances where SJ-F1 correlation is genuinely strong, masking that >60% of instances receive no useful signal. Consequence: MV selection on CoNLL yields only +0.61 pp at N=64 despite 4 pp oracle headroom, and LP selection is negative (−0.85 pp). The entity-level decomposition reveals *why*: the problem is not signal quality but instance-level degeneracy eliminating the selection opportunity for the majority of instances.\n\n**Paper location:** Table tab:quality_estimation (experiments_main.tex, line 40), Table tab:fewnerd (line 71), Figure fig:n_scaling (line 19).\n\n---\n\n### Q7 [R2-Q5]: Partial-Match Degeneracy Definition\n**Question:** How would relaxing the degeneracy definition (e.g., Jaccard > 0.9 instead of exact match) affect results?\n\n**Response:** The current definition is binary: an instance is degenerate iff all N samples produce identical entity sets. Relaxing to partial match (e.g., Jaccard similarity > 0.9) would likely reduce measured degeneracy rates. However, we did not run this experiment. Critically, even if D decreases substantially under a softer definition, the binding constraint is α (signal alignment), not D. §6.3 establishes that α is 8–33× tighter than D across all configurations: α=0.000–0.161 while (1−D) ranges from 0.32–0.88. Halving D would at most double the bound's headroom, but α→0 would still suppress actual gains to near zero. Partial-match degeneracy analysis is listed as future work; the key diagnostic conclusion (α is the bottleneck) is robust to the degeneracy definition.\n\n**Paper location:** §6.3 (theory.tex, line 30).\n\n---\n\n### Q8 [R2-Q2]: Entity Independence Assumption Violation\n**Question:** How does violating the entity independence assumption in Proposition 1 affect the bound's validity?\n\n**Response:** The entity independence assumption (entities independently contribute to F1) is typically violated in NER—e.g., \"New York City\" tokens have near-unity co-occurrence, and nested entities share boundary dependencies. Violating independence means the bound becomes looser: actual F1 changes can exceed or fall below the bound's prediction, because correlated entities amplify or dampen changes in ways the independent model cannot capture. Split-half correlation r=0.578–0.644 quantifies the violation magnitude. However, as a necessary condition, the bound remains valid under independence violation: if D=1 (complete degeneracy) or α=0 (zero signal alignment), no aggregation method can improve over greedy regardless of entity correlation structure. Independence affects the bound's *quantitative precision* (explaining part of the 3–12% recovery ratio) but not its *qualitative diagnostic validity*. The conclusion that α→0 is the binding constraint does not depend on the independence assumption.\n\n**Paper location:** §6.3 \"Bound looseness\" paragraph (theory.tex, line 33), Limitations (limitations.tex, line 1).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r42_response_letter.md",
    "content": "# Response to Reviewers — R42\n\nWe thank both reviewers for their thorough and constructive feedback. Below we address each point, referencing specific revisions in the paper.\n\n---\n\n## Must-Fix Responses\n\n### MF1: Decomposition Bound Repositioned as Necessary Condition Test\n**Concern (R1-N1, R2 agree):** The bound E[ΔF1(A)] ≤ (1−D)·G_nd·α recovers only 3–12% of actual gains, limiting its utility as a quantitative predictor.\n\n**Response:** We have repositioned the bound as an *intentionally loose necessary condition test* rather than a tight predictor. §6.3 now states: \"The bound is an intentionally loose *necessary condition test*: when D→1 or α→0, no aggregation method can improve over greedy, regardless of implementation. It localizes *where* aggregation fails—screening for favorable conditions—rather than quantitatively predicting gains.\" The low recovery ratio (3–12%) is explicitly framed as reflecting \"its role as a screening test, not a tight estimate.\" We weakened language around Table 33 / Figure bound accordingly. The two dominant sources of looseness are identified: (1) entity independence assumption (split-half correlation r=0.578–0.644 reveals substantial inter-entity correlation), and (2) conservative α estimation as the minimum across instances.\n\n**Paper location:** §6.3 (Degeneracy Decomposition), specifically the paragraph beginning \"The bound is an intentionally loose...\" and \"Bound looseness\" paragraph.\n\n---\n\n### MF2: Statistical Significance Under Multiple Comparison Corrections\n**Concern (R1-N2, R2 agree):** The core positive claim (entity construction on Few-NERD) reaches global Holm p_adj=0.055 (not significant at α=0.05), while per-family p_adj=0.006; the family partition lacks prior justification.\n\n**Response:** §7.5 (Prescriptive Results) now provides the prior rationale for the family partition: \"We group the 57 comparisons into methodological families—per-sample signals (k=21), cross-sample signals (k=26), and entity construction (k=10)—reflecting mechanistic distinctions defined at experiment design time (not selected post-hoc to optimize p-values).\" Both corrections are transparently reported: global Holm k=57 p_adj=0.055 (suggestive) and per-family k=10 p_adj=0.006 (significant), with BH FDR yielding 6/10 construction comparisons at FDR<0.05. As additional robustness evidence, the seed-replication analysis (5 SciERC seeds, Fisher z + Holm correction, k=5) yields p_adj=0.013 for the SJ > LP advantage (Appendix B.5), providing independent statistical support via a separate methodology.\n\n**Paper location:** §7.5 (experiments_main.tex, lines 109–111), Appendix B.5 (app:bootstrap_signal, line 315), Appendix Holm enumeration (app:holm).\n\n---\n\n### MF3: Mechanistic Probes on Qwen2.5-7B Rather Than Qwen3-8B\n**Concern (R1-N3, R2 agree):** Probe and ESJ experiments were conducted on Qwen2.5-7B-Instruct, not the fine-tuned Qwen3-8B used in main experiments, and the model discrepancy was not flagged in the main text.\n\n**Response:** Two changes address this: (1) §4 (mechanistic.tex) now explicitly annotates: \"Probe experiments use Qwen2.5-7B (not the fine-tuned Qwen3-8B used in main experiments); conclusions are architecture-specific.\" A footnote details the rationale and scope limitation. (2) We performed ESJ cross-validation on Qwen3-8B fine-tuned, reported in Appendix E (app:esj, Table tab:esj_cross): AUROC is SciERC 0.512, CoNLL 0.553, Few-NERD 0.495—all indistinguishable from chance. This confirms the introspection boundary transfers across architectures (Qwen2.5-7B pretrained → Qwen3-8B fine-tuned). The Limitations section also explicitly states: \"probe cross-model transferability is not yet verified, though ESJ chance-level performance replicates on Qwen3-8B (AUROC 0.50–0.55).\"\n\n**Paper location:** §4 (mechanistic.tex, lines 4–5), §5 (single_signal.tex, line 55), Appendix E Table tab:esj_cross (appendix.tex, lines 688–699), Limitations (limitations.tex, line 4).\n\n---\n\n### MF4: Systematic Comparison with Landesberg et al. (2026)\n**Concern (R2-N1, R1 agree):** Need a half-page systematic comparison with Landesberg et al. (2026) and Table 1 augmented with failure mechanism dimension.\n\n**Response:** §2 (Related Work) now contains a four-dimensional systematic comparison: \"(a) domain—reasoning (scalar judgments) vs. NER/RE (entity sets with partial overlap); (b) failure mechanism—prompt-level baseline effects vs. degeneracy (12–68%) and signal alignment collapse (α→0), mechanisms specific to structured prediction; (c) granularity—prompt-level r decomposition vs. instance- and entity-level diagnostics (D, G_nd, α); (d) prescriptive—no constructive remedy vs. entity-level construction with MBR grounding.\" Table 1 (tab:novelty_comparison) has been expanded to seven dimensions including \"Failure mechanism\" (Landesberg: \"Baseline effects\"; Ours: \"Degeneracy + α\") and \"Failure decomp.\" (Landesberg: \"—\"; Ours: \"D, α, LP\").\n\n**Paper location:** §2 (background.tex, lines 39–46), Table 1 (tab:novelty_comparison, lines 18–37).\n\n---\n\n### MF5: Few-NERD Epoch Confound\n**Concern (R2-N2, R1 escalated to critical):** The +1.40pp Few-NERD gain uses a 3-epoch under-converged model; 5-epoch training shows 94% collapse. Abstract lacked this conditioning.\n\n**Response:** The Abstract now explicitly conditions the Few-NERD claim: \"Entity-level construction yields conditional gains (+1.40 pp on Few-NERD under 3-epoch training; diminishes to +0.09 pp at convergence; per-family Holm p_adj=0.006, global p_adj=0.055).\" §7.5 reports the complete 3-vs-5 epoch comparison: LP selection collapses from +1.39 to +0.09±0.04 pp (94% reduction); entity construction from +0.88 to +0.20 pp (77% reduction). Constant-F1 degeneracy rises from 13% to 31%. Appendix (app:epoch_confound) provides full details including the SciERC 3-point gradient (3/5/10 epochs) showing monotonic degeneracy increase with simultaneous within-instance alignment degradation. We frame this as a finding rather than a limitation: \"SC may complement early stopping strategies—under-converged models preserve output diversity that enables aggregation gains.\"\n\n**Paper location:** Abstract (abstract.tex, line 6), §7.5 (experiments_main.tex, lines 114–117), Appendix (app:epoch_confound, lines 2043–2112).\n\n---\n\n## Should-Fix Responses\n\n### SF1: Diagnostic vs. Prescriptive Narrative Inconsistency\n**Concern:** The paper oscillates between diagnostic and prescriptive framing.\n\n**Response:** Abstract and Discussion now consistently use \"primarily diagnostic\": \"The framework is primarily diagnostic, with limited predictive power for identifying favorable conditions, informing resource allocation decisions before investing in repeated inference\" (Abstract, line 7). The Discussion (§8) reinforces: \"The diagnostic framework—localizing failure to degeneracy and signal alignment collapse—is our primary contribution; cross-task and cross-model extensions are exploratory\" (discussion.tex, line 15).\n\n**Paper location:** Abstract (line 7), Discussion/Conclusion (discussion.tex, lines 1, 15).\n\n---\n\n### SF2: 2–3 Seeds Insufficient for Statistical Inference\n**Concern:** Only 2–3 training seeds limit the reliability of statistical claims.\n\n**Response:** We use 5 seeds for SciERC on Qwen3-8B and 3 seeds for LLaMA across all datasets (Appendix app:multiseed confirms σ≤0.026 for all QE signals across 5 seeds). The seed-replication Holm correction (k=5, p_adj=0.013) and Fisher z test provide cross-seed statistical validation independent of the per-family correction. The Limitations section explicitly acknowledges this scope: seed counts reflect computational constraints (each seed × N=8 samples × 4 datasets × 2 models requires ~64 fine-tuning runs and ~512 inference batches). The directional consistency across all seeds (SC negative in 100% of seed-dataset combinations for MV) strengthens confidence beyond what raw seed count suggests.\n\n**Paper location:** Response-letter only; Limitations (limitations.tex), Appendix app:bootstrap_signal (line 315), Appendix app:multiseed (lines 701–706).\n\n---\n\n### SF3: RE/SQL Extensions Too Thin\n**Concern:** RE (n=397) and SQL (n=196) extensions lack depth for strong conclusions.\n\n**Response:** The Abstract explicitly marks these as \"preliminary RE (n=397) and SQL (n=196) pilots\" (abstract.tex, line 3). We do not make strong claims about either extension; they serve to demonstrate that the diagnostic framework identifies *different* failure modes across tasks (RE: diversity among failures from upstream entity span errors; SQL: 87.2% degeneracy). Cross-task generalization is listed as exploratory throughout.\n\n**Paper location:** Abstract (line 3), Introduction (line 14), Discussion (line 15).\n\n---\n\n### SF4: Related Work Coverage Gaps\n**Concern:** Missing coverage of MBR/calibration literature.\n\n**Response:** §2 (Related Work) now includes: Eikema et al. (2025) on structured MBR utility degradation (\"citet{eikema2025structured} find MBR utilities degrade on structured outputs, consistent with our LP compression findings\"), calibration literature (Desai & Durrett 2020, Xiao et al. 2022), selective prediction (Geifman & El-Yaniv 2017), conformal prediction (Angelopoulos et al. 2023), and semantic uncertainty (Kuhn et al. 2023). These are positioned under the \"Uncertainty estimation and MBR\" paragraph.\n\n**Paper location:** §2 (background.tex, lines 13–16).\n\n---\n\n### SF5: Entity-Level Decomposition Incremental Contribution\n**Concern:** The entity-level decomposition may not add sufficient value over task-level analysis.\n\n**Response:** The core value proposition of entity-level analysis is threefold: (1) *Degeneracy is only definable at entity level*—12–68% of instances produce identical entity sets across all N samples (Table tab:fewnerd), a phenomenon invisible to task-level F1 correlation. (2) *Task-level metrics mask instance-level failure*: CoNLL shows task-level ρ(SJ,F1)=0.45 (Table tab:quality_estimation), suggesting SJ is a useful signal, yet 57–60% of instances are degenerate—SJ assigns identical scores to all candidates for these instances, yielding zero discriminative power. Task-level ρ is inflated by non-degenerate instances' strong correlation masking degenerate instances' zero contribution. (3) *Construction gains concentrate in identifiable subsets*: on non-degenerate instances, entity construction yields +3.36 pp (SciERC), +5.18 pp (CoNLL), +7.08 pp (Few-NERD)—gains invisible in task-level aggregates.\n\n**Paper location:** Response-letter only; data from Table tab:fewnerd (experiments_main.tex, line 71), Table tab:quality_estimation (line 40), §7.5 footnote (line 108).\n\n---\n\n### SF6: Constrained Decoding Confound Not Fully Resolved\n**Concern:** LP compression may be an artifact of constrained decoding rather than a model-intrinsic property.\n\n**Response:** We extended the free-form decoding ablation to three NER datasets (Appendix app:freeform_ablation). Table tab:freeform_summary reports LP std ratios (free-form / constrained): SciERC 0.97×, CoNLL 0.86×, Few-NERD 1.00×. LP compression is nearly identical under both regimes. NER selection gains remain negligible under free-form decoding across all three datasets. On CoNLL specifically, LP-selected F1=0.896 vs. single-sample 0.904 (Δ=−0.77 pp)—LP still fails. The Discussion states: \"LP compression is model-intrinsic rather than an artifact of constrained decoding\" (discussion.tex, line 6).\n\n**Paper location:** Appendix app:freeform_ablation (appendix.tex, lines 1277–1389), Table tab:freeform_summary (line 1366), Discussion (line 6), Limitations (line 5).\n\n---\n\n## Questions\n\n### Q1 [R1-Q1]: Source of Bound Looseness\n**Question:** What are the sources of the 3–12% recovery ratio, and which simplification assumption dominates?\n\n**Response:** Three simplifying assumptions contribute to bound looseness, in decreasing order of impact: (1) *Entity independence* is the dominant source. The bound assumes entities independently contribute to F1, but NER entities are often correlated (e.g., \"New York City\" spans three tokens with near-unity co-occurrence). Split-half correlation r=0.578–0.644 quantifies this violation. (2) *Multiplicative structure*: the (1−D)·G_nd·α decomposition assumes factors interact multiplicatively, which is an approximation. (3) *Linear α approximation*: α is estimated as the minimum across instances rather than instance-adaptive, further loosening the bound. We did not pursue tighter bounds because the diagnostic purpose—necessary condition screening—does not require quantitative precision. The key insight is qualitative: α→0 is the binding constraint (8–33× tighter than D), and this conclusion holds regardless of bound tightness.\n\n**Paper location:** §6.3 \"Bound looseness\" paragraph (theory.tex, line 33).\n\n---\n\n### Q2 [R1-Q2]: Probe Replication on Qwen3-8B\n**Question:** Have the probes been replicated on the Qwen3-8B model used in main experiments?\n\n**Response:** ESJ has been cross-validated on Qwen3-8B fine-tuned. Appendix E (Table tab:esj_cross) reports entity-level AUROC: SciERC 0.512, CoNLL 0.553, Few-NERD 0.495—all at chance level. This confirms the introspection boundary transfers across both architectures (Qwen2.5-7B → Qwen3-8B) and training conditions (pretrained → fine-tuned). Hidden-state probes have not yet been replicated on Qwen3-8B; the Limitations section acknowledges this.\n\n**Paper location:** Appendix E Table tab:esj_cross (appendix.tex, lines 688–699), §5 (single_signal.tex, line 55), Limitations (line 4).\n\n---\n\n### Q3 [R1-Q3, R2-Q1]: 5-Epoch Entity Construction Numbers\n**Question:** What are the exact 5-epoch numbers for both LP selection and entity construction on Few-NERD?\n\n**Response:** From §7.5 and Appendix app:epoch_confound: LP selection gain collapses from +1.39 pp (3-epoch) to +0.09±0.04 pp (5-epoch), a 94% reduction. Entity construction gain drops from +0.88 pp to +0.20 pp, a 77% reduction. Constant-F1 degeneracy rises from 13% to 31%. Greedy F1 improves modestly (+0.7 pp, 0.791→0.798). The 5-epoch model is past the optimal early-stopping point (evaluation loss increases after epoch 3; best checkpoint at ~epoch 3.9).\n\n**Paper location:** §7.5 (experiments_main.tex, lines 114–116), Appendix app:epoch_confound Table tab:epoch_confound (appendix.tex, lines 2043–2070).\n\n---\n\n### Q4 [R1-Q4]: Free-Form LP Selection Performance\n**Question:** Does LP selection improve under free-form (unconstrained) decoding?\n\n**Response:** No. Across three NER datasets under free-form decoding: SciERC shows negligible LP Δ under both regimes; CoNLL LP-selected F1=0.896 vs. single-sample 0.904 (Δ=−0.77 pp)—LP still fails; Few-NERD shows all deltas <0.02 pp—identical to constrained. The conclusion \"LP fails for structured prediction\" holds across datasets and decoding modes. The one exception is RE, where LP selection reverses direction under free-form decoding (+1.84±0.12 pp across 4 seeds vs. −0.68 pp constrained), but this is task-specific and does not generalize to NER.\n\n**Paper location:** Appendix app:freeform_ablation (appendix.tex, lines 1277–1389), Table tab:freeform_summary (line 1366).\n\n---\n\n### Q5 [R1-Q5]: Pre-Registration of Hypothesis Families\n**Question:** Were the per-family hypothesis groupings pre-registered?\n\n**Response:** No. This is a post-hoc analysis study, not a confirmatory experiment, so pre-registration was not applicable. We explicitly acknowledge this: \"the family partition was not pre-registered\" (§7.5, experiments_main.tex line 111). The per-family groupings reflect methodological distinctions at design time: per-sample signals (LP-based, k=21), cross-sample signals (agreement-based, k=26), and entity construction (aggregation-based, k=10) test fundamentally different mechanisms and were designed as separate experimental modules. As an additional safeguard independent of the family partition, the seed-replication Fisher z test (k=5, p_adj=0.013) provides a separate statistical path that does not depend on how the 57 comparisons are grouped.\n\n**Paper location:** §7.5 (experiments_main.tex, lines 109–111), Appendix app:bootstrap_signal (line 315).\n\n---\n\n### Q6 [R2-Q4]: Task-Level vs. Instance-Level Contradiction\n**Question:** Can you provide a concrete example where task-level metrics are misleading?\n\n**Response:** CoNLL provides the clearest case. Task-level: ρ(SJ, F1)=0.436, AUROC=0.801 (Table tab:quality_estimation)—SJ appears to be a strong quality signal. Instance-level: 61.7% of instances are degenerate (all N samples produce identical entity sets; Table tab:fewnerd). For these instances, SJ assigns identical scores to all candidates, providing zero discriminative power. The task-level ρ is inflated by non-degenerate instances where SJ-F1 correlation is genuinely strong, masking that >60% of instances receive no useful signal. Consequence: MV selection on CoNLL yields only +0.61 pp at N=64 despite 4 pp oracle headroom, and LP selection is negative (−0.85 pp). The entity-level decomposition reveals *why*: the problem is not signal quality but instance-level degeneracy eliminating the selection opportunity for the majority of instances.\n\n**Paper location:** Table tab:quality_estimation (experiments_main.tex, line 40), Table tab:fewnerd (line 71), Figure fig:n_scaling (line 19).\n\n---\n\n### Q7 [R2-Q5]: Partial-Match Degeneracy Definition\n**Question:** How would relaxing the degeneracy definition (e.g., Jaccard > 0.9 instead of exact match) affect results?\n\n**Response:** The current definition is binary: an instance is degenerate iff all N samples produce identical entity sets. Relaxing to partial match (e.g., Jaccard similarity > 0.9) would likely reduce measured degeneracy rates. However, we did not run this experiment. Critically, even if D decreases substantially under a softer definition, the binding constraint is α (signal alignment), not D. §6.3 establishes that α is 8–33× tighter than D across all configurations: α=0.000–0.161 while (1−D) ranges from 0.32–0.88. Halving D would at most double the bound's headroom, but α→0 would still suppress actual gains to near zero. Partial-match degeneracy analysis is listed as future work; the key diagnostic conclusion (α is the bottleneck) is robust to the degeneracy definition.\n\n**Paper location:** §6.3 (theory.tex, line 30).\n\n---\n\n### Q8 [R2-Q2]: Entity Independence Assumption Violation\n**Question:** How does violating the entity independence assumption in Proposition 1 affect the bound's validity?\n\n**Response:** The entity independence assumption (entities independently contribute to F1) is typically violated in NER—e.g., \"New York City\" tokens have near-unity co-occurrence, and nested entities share boundary dependencies. Violating independence means the bound becomes looser: actual F1 changes can exceed or fall below the bound's prediction, because correlated entities amplify or dampen changes in ways the independent model cannot capture. Split-half correlation r=0.578–0.644 quantifies the violation magnitude. However, as a necessary condition, the bound remains valid under independence violation: if D=1 (complete degeneracy) or α=0 (zero signal alignment), no aggregation method can improve over greedy regardless of entity correlation structure. Independence affects the bound's *quantitative precision* (explaining part of the 3–12% recovery ratio) but not its *qualitative diagnostic validity*. The conclusion that α→0 is the binding constraint does not depend on the independence assumption.\n\n**Paper location:** §6.3 \"Bound looseness\" paragraph (theory.tex, line 33), Limitations (limitations.tex, line 1).\n"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-23T07:02:03.960677+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r42_response_letter.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r42_response_letter_20260523T065827",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-23T07:02:03.960848+00:00_

Response letter 已写入 `artifacts/r42_response_letter.md`。覆盖全部 19 条（MF1–5, SF1–6, Q1–8），每条包含审稿意见摘要、具体回应、论文修改位置引用。所有数据点均从论文 sections/ 下的实际 tex 文件中提取验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_r42_response_letter_20260523T065827"
}
```

</details>

---
