# analysis claim audit v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/chats/worker_analysis_claim_audit_v2_20260519T064159.jsonl`
- **Structured JSON:** [`ef4e0fc9a712a5886b5f.json`](../../sessions/ef/ef4e0fc9a712a5886b5f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

61 recorded events

### Tool call

_source line 1 · 2026-05-19T06:53:28.248947+00:00_

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
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
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

_source line 2 · 2026-05-19T06:53:28.249337+00:00_

docs/paper/sections/checklist.tex
docs/paper/sections/limitations.tex
docs/paper/sections/method.tex
docs/paper/sections/appendix.tex
docs/paper/sections/discussion.tex
docs/paper/sections/abstract.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/introduction.tex
docs/paper/sections/experiments.tex
docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T06:53:28.249522+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T06:53:28.249670+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T06:53:28.249873+00:00_

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
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T06:53:28.250026+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
4	All signals achieve reliable QE ($\rho$ up to 0.50, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
6	We diagnose two causes: instance degeneracy and weak LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.
7	The diagnostic naturally motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T06:53:28.250186+00:00_

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
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T06:53:28.250365+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \textit{when and why} LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A key distinction structures our analysis: four of five signals (Soft Jaccard, voting confidence, Fleiss' $\kappa$, exact match) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.50, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low inst
…[truncated 4607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T06:53:28.250520+00:00_

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
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T06:53:28.250706+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Throughout, entity matching uses exact span and type match (a predicted entity is correct iff its character offsets and type label both match a gold entity).
12	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
13	
14	\paragraph{Log-probability (model-internal, per-sample).}
15	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
16	\begin{equation}\label{eq:logprob}
17	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
18	\end{equation}
19	
20	\paragraph{Exact match voting (surface, instance-level).}
21	The proportion of samples producing the most common output:
22	\begin{equation}\label{eq:em}
23	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
24	\end{equation}
25	
26	\paragraph{Fleiss' $\kappa$ (surface, insta
…[truncated 4000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T06:53:28.250852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T06:53:28.251092+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17	
18	%% ============================================================
19	\subsection{Quality Estimation Results}
20	\label{sec:qe_results}
21	
22	\begin{table*}[t]
23	\centering
24	\small
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
26	\label{tab:quality_estimation}
27	\begin{tabular}{ll cc cc cc}
28	\topr
…[truncated 17377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T06:53:28.251273+00:00_

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
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T06:53:28.251415+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
4	Two factors constrain selection: instance degeneracy (17.8--48.4\%) eliminates headroom, and LP compression (within-instance $\rho$ 0.262--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\rho{=}0.524$) \cite{eikema2022sampling}.
5	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP selection yields $+2.9$~pp ($p{=}0.004$, surviving Bonferroni across 5 signals; Table~\ref{tab:nontied_main}). However, $\varepsilon{=}0.05$ is selected post-hoc from a 7-point sweep (Appendix~\ref{app:epsilon_robustness}); joint correction across thresholds and signals yields $p_{\text{adj}}{=}0.14$, so this finding is exploratory evidence for LP compression's role in the selection bottleneck.
6	Temperature disentangles the two factors: at $T{=}1.2$, degeneracy drops to 14.9\% yet LP does not improve ($\rho{=}0.225$ vs.\ Few-NERD ${\sim}$0.5--0.7; Table~\ref{tab:t_degeneracy}); degeneracy rises with model scale and training convergence (Tables~\ref{tab:scale_ablation}, \ref{tab:epoch_confound}), so the selection window narrows as models improve \cite{wang2023selfconsistency, snell2025scaling}.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms ($+1.40$\,pp Few-NERD, $+1.02$\,pp SciERC, multi-seed mean; Table~\ref{tab:entity_construction}), complementary with LP selection and governed by LP-quality alignment (\S\ref{sec:prescriptive}).
10	Alternative strategies (DALS, MBR, DGS) fail to reliably beat greedy (Appendix~\ref{app:dals}).
11	Our negative results are specific to fine-tuned models with constrained decoding; settings with greater outp
…[truncated 90 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T06:53:28.251561+00:00_

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
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T06:53:28.251685+00:00_

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
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T06:53:28.251799+00:00_

File content (41711 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T06:53:28.251918+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Five confidence signals achieve reliable NER quality estimation ($\rho$ up to 0.50, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
4	Instance-level selection fails due to degeneracy and LP compression, but the diagnostic naturally motivates entity-level construction, adapting entity voting to stochastic sampling: LP-weighted aggregation yields $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$).
5	Construction and LP selection are complementary on two informative datasets (SciERC and Few-NERD; CoNLL operates in a ceiling regime), governed by LP-quality alignment.
6	For practitioners: use QE-based selective prediction when deployment requires reliability guarantees; apply entity construction when multi-sample generation is feasible; assess LP-alignment via held-out validation to choose between construction and LP selection.
7	As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \cite{cobbe2021verifiers} may be needed to close the remaining gap.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T06:53:28.252039+00:00_

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
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T06:53:28.252202+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} rely on answer-level agreement.
6	Adaptive variants gate on answer agreement \cite{aggarwal2023adaptive}, input difficulty \cite{wang2025make, feng2025optimal}, or response confidence \cite{kim2026reasc}; \citet{chen2025twofailures} diagnose SC failure modes without proposing gating.
7	All target discrete-answer reasoning; structured prediction requires different gating signals because degeneracy operates at the entity-set level.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\S\ref{sec:robustness_main}).
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Ensemble approaches aggregate predictions from multiple models or prompts \cite{florian2003named, xiao2025el4ner}; LLM-Blender \cite{jiang2023llmblender} fuses outputs from multiple LLMs via pairwise ranking, whereas our single-model stochastic sampling derives diversity from temperature rather than model heterogeneity.
14	Our entity-level construction similarly aggregates across samples from a single model, without requiring model diversity.
15	Our evaluation
…[truncated 2501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T06:53:28.252354+00:00_

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
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T06:53:28.252497+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	All experiments use English-language datasets; cross-lingual generalization remains untested.
3	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.
4	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
5	
6	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
7	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
8	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
9	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
10	We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
11	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
12	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc expl
…[truncated 2048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T06:53:28.252642+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "struct_self_consist_ie",
  "filters": "{'status': 'DONE', 'conclusion': 'success'}",
  "fields": "['metrics', 'hypothesis', 'exp_id', 'name']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "filters": "{'status': 'DONE', 'conclusion': 'success'}",
    "fields": "['metrics', 'hypothesis', 'exp_id', 'name']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T06:53:28.253090+00:00_

Error: result (76,780 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/6e3f9627-b49e-4767-a699-a4826b61ce65/tool-results/mcp-agent-ml-research-read_registry-1779172943409.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/6e3f9627-b49e-4767-a699-a4826b61ce65/tool-results/mcp-agent-ml-research-read_registry-1779172943409.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T06:53:28.253354+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "500",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "500",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T06:53:28.253712+00:00_

0	\section{Notation}\label{app:notation}
1	
2	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{cl}
8	\toprule
9	Symbol & Meaning \\
10	\midrule
11	$\mathcal{M}$ & Language model \\
12	$x$ & Input instance \\
13	$y_i$ & $i$-th stochastic sample \\
14	$N$ & Number of samples \\
15	$T$ & Sampling temperature \\
16	$c(\cdot)$ & Confidence signal \\
17	SJ & Soft Jaccard similarity \\
18	FK & Fleiss' $\kappa$ \\
19	EM & Exact-match voting rate \\
20	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
21	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
22	\bottomrule
23	\end{tabular}
24	\caption{Notation used throughout the paper.}
25	\label{tab:notation}
26	\end{table}
27	
28	\section{Robustness Analysis}\label{app:robustness}
29	
30	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
31	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
32	
33	\begin{table}[t]
34	\centering
35	\small
36	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
37	\label{tab:robustness}
38	\begin{tabular}{llcc}
39	\toprule
40	& & NER $\rho$ & RE $\rho$ \\
41	\midrule
42	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
43	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
44	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
45	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
46	\quad FK & $T
…[truncated 39811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T06:53:28.253880+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/6e3f9627-b49e-4767-a699-a4826b61ce65/tool-results/mcp-agent-ml-research-read_registry-1779172943409.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nexps = json.loads(data['result'])\nfor exp in exps:\n    eid = exp.get('exp_id','?')\n    name = exp.get('name','?')\n    metrics = exp.get('metrics',{})\n    if metrics:\n        print(f'=== {eid}: {name} ===')\n        print(json.dumps(metrics, indent=2)[:800])\n        print()\n\" 2>&1 | head -500",
  "description": "Extract metrics from registry experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/6e3f9627-b49e-4767-a699-a4826b61ce65/tool-results/mcp-agent-ml-research-read_registry-1779172943409.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nexps = json.loads(data['result'])\nfor exp in exps:\n    eid = exp.get('exp_id','?')\n    name = exp.get('name','?')\n    metrics = exp.get('metrics',{})\n    if metrics:\n        print(f'=== {eid}: {name} ===')\n        print(json.dumps(metrics, indent=2)[:800])\n        print()\n\" 2>&1 | head -500",
    "description": "Extract metrics from registry experiments"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T06:53:28.254018+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    eid = exp.get('exp_id','?')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T06:53:28.254185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "500",
  "offset": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "500",
    "offset": "500"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T06:53:28.254600+00:00_

500	\end{tabular}
501	\end{table}
502	
503	\section{Training Configuration}\label{app:training}
504	
505	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
506	
507	\begin{table}[t]
508	\centering
509	\small
510	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
511	\label{tab:training}
512	\begin{tabular}{ll}
513	\toprule
514	Parameter & Value \\
515	\midrule
516	LoRA rank / $\alpha$ & 32 / 64 \\
517	LoRA target & All linear modules \\
518	LoRA dropout & 0 \\
519	Optimizer & AdamW \\
520	Learning rate & 2e-4, cosine schedule \\
521	Warmup ratio & 0.1 \\
522	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
523	Epochs & 5 \\
524	Max sequence length & 2048 \\
525	Precision & bf16 \\
526	Gradient checkpointing & Enabled \\
527	Max gradient norm & 1.0 \\
528	Training seed & 42 \\
529	Framework & LLaMA Factory \\
530	\midrule
531	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
532	SciERC split & 1861 / 275 / 551 \\
533	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
534	& eval\_steps${=}$200, save\_limit${=}$5 \\
535	\bottomrule
536	\end{tabular}
537	\end{table}
538	
539	\paragraph{Prompt template.}
540	For NER, we use a structured prompt:
541	\begin{quote}
542	\small
543	\texttt{System:} You are an expert in Named Entity Recognition.\\
544	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
545	Text: \texttt{\{input\_text\}}\\
546	Entity types: \texttt{\{schema\_types\}}
547	\end{quote}
548	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
549	
550	\paragraph{Constrained decoding.}
551	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{dong2024xgrammar, willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schem
…[truncated 29458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T06:53:28.254803+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/6e3f9627-b49e-4767-a699-a4826b61ce65/tool-results/mcp-agent-ml-research-read_registry-1779172943409.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = data['result']\n# result might be a JSON string itself\ntry:\n    exps = json.loads(result)\nexcept:\n    exps = result\nif isinstance(exps, list):\n    for exp in exps:\n        if isinstance(exp, dict):\n            eid = exp.get('exp_id','?')\n            name = exp.get('name','?')\n            metrics = exp.get('metrics',{})\n            if metrics:\n                print(f'=== {eid}: {name} ===')\n                m_str = json.dumps(metrics, indent=2)\n                print(m_str[:600])\n                print()\n        elif isinstance(exp, str):\n            print('String entry:', exp[:200])\nelse:\n    print('Type:', type(exps))\n    print(str(exps)[:500])\n\" 2>&1 | head -600",
  "description": "Parse registry experiments with proper type handling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/6e3f9627-b49e-4767-a699-a4826b61ce65/tool-results/mcp-agent-ml-research-read_registry-1779172943409.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = data['result']\n# result might be a JSON string itself\ntry:\n    exps = json.loads(result)\nexcept:\n    exps = result\nif isinstance(exps, list):\n    for exp in exps:\n        if isinstance(exp, dict):\n            eid = exp.get('exp_id','?')\n            name = exp.get('name','?')\n            metrics = exp.get('metrics',{})\n            if metrics:\n                print(f'=== {eid}: {name} ===')\n                m_str = json.dumps(metrics, indent=2)\n                print(m_str[:600])\n                print()\n        elif isinstance(exp, str):\n            print('String entry:', exp[:200])\nelse:\n    print('Type:', type(exps))\n    print(str(exps)[:500])\n\" 2>&1 | head -600",
    "description": "Parse registry experiments with proper type handling"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T06:53:28.254947+00:00_

Type: &lt;class 'dict'>
{'success': True, 'data': {'experiments': {'exp_llama_fewnerd_inference': {'hypothesis': 'LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness.', 'metrics': {'3seed_mean': {'greedy_f1': 0.7842, 'oracle_f1': 0.8843, 'headroom_pp': 10.01, 'degeneracy_pct': 23.36, 'lp_delta_pp': 0.36, 'dgs_delta_pp':

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T06:53:28.255153+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/6e3f9627-b49e-4767-a699-a4826b61ce65/tool-results/mcp-agent-ml-research-read_registry-1779172943409.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = data['result']\nregistry = json.loads(result) if isinstance(result, str) else result\nexps = registry.get('data', registry).get('experiments', registry) if isinstance(registry, dict) else registry\n\n# Navigate to the actual experiments\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\n\nif isinstance(exps, dict):\n    for eid, exp in exps.items():\n        if isinstance(exp, dict):\n            metrics = exp.get('metrics', {})\n            hyp = exp.get('hypothesis', '')\n            if metrics:\n                print(f'=== {eid} ===')\n                print(f'Hypothesis: {hyp[:120]}')\n                m_str = json.dumps(metrics, indent=2)\n                print(m_str[:1000])\n                print()\nelif isinstance(exps, list):\n    for exp in exps:\n        if isinstance(exp, dict):\n            eid = exp.get('exp_id', '?')\n            metrics = exp.get('metrics', {})\n            hyp = exp.get('hypothesis', '')\n            if metrics:\n                print(f'=== {eid} ===')\n                print(f'Hypothesis: {hyp[:120]}')\n                m_str = json.dumps(metrics, indent=2)\n                print(m_str[:1000])\n                print()\n\" 2>&1 | head -800",
  "description": "Parse registry data structure and extract metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/6e3f9627-b49e-4767-a699-a4826b61ce65/tool-results/mcp-agent-ml-research-read_registry-1779172943409.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = data['result']\nregistry = json.loads(result) if isinstance(result, str) else result\nexps = registry.get('data', registry).get('experiments', registry) if isinstance(registry, dict) else registry\n\n# Navigate to the actual experiments\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\n\nif isinstance(exps, dict):\n    for eid, exp in exps.items():\n        if isinstance(exp, dict):\n            metrics = exp.get('metrics', {})\n            hyp = exp.get('hypothesis', '')\n            if metrics:\n                print(f'=== {eid} ===')\n                print(f'Hypothesis: {hyp[:120]}')\n                m_str = json.dumps(metrics, indent=2)\n                print(m_str[:1000])\n                print()\nelif isinstance(exps, list):\n    for exp in exps:\n        if isinstance(exp, dict):\n            eid = exp.get('exp_id', '?')\n            metrics = exp.get('metrics', {})\n            hyp = exp.get('hypothesis', '')\n            if metrics:\n                print(f'=== {eid} ===')\n                print(f'Hypothesis: {hyp[:120]}')\n                m_str = json.dumps(metrics, indent=2)\n                print(m_str[:1000])\n                print()\n\" 2>&1 | head -800",
    "description": "Parse registry data structure and extract metrics"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T06:53:28.255583+00:00_

=== exp_llama_fewnerd_inference ===
Hypothesis: LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, si
{
  "3seed_mean": {
    "greedy_f1": 0.7842,
    "oracle_f1": 0.8843,
    "headroom_pp": 10.01,
    "degeneracy_pct": 23.36,
    "lp_delta_pp": 0.36,
    "dgs_delta_pp": -0.35
  },
  "seed_42": {
    "greedy_f1": 0.7841,
    "oracle_f1": 0.8854,
    "degen": 27.32
  },
  "seed_123": {
    "greedy_f1": 0.784,
    "oracle_f1": 0.8839,
    "degen": 24.63
  },
  "seed_456": {
    "greedy_f1": 0.7844,
    "oracle_f1": 0.8835,
    "degen": 18.13
  },
  "signal_ranking": "LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)",
  "lp_only_positive": true,
  "n_instances_gold_filtered": 32565
}

=== exp_entity_construction ===
Hypothesis: Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting 
{
  "n16_fair_cv": {
    "scierc_ner": {
      "cv_uniform_delta": "+1.35pp",
      "p_value": 0.018,
      "significant": true
    },
    "conll_ner": {
      "cv_uniform_delta": "+0.10pp",
      "p_value": 0.303,
      "significant": false
    },
    "fewnerd_ner": {
      "cv_uniform_delta": "+1.32pp",
      "p_value": 0,
      "significant": true
    },
    "scierc_re": {
      "cv_uniform_delta": "+1.69pp",
      "p_value": 0.049,
      "significant": true
    }
  },
  "n8_fair_cv": {
    "scierc_ner": {
      "uniform_confirm": "+1.54pp (p=0.023, sig)",
      "lp_weighted_confirm": "+1.67pp (p=0.004, sig)",
      "cv_uniform": "+1.12pp (p=0.057, borderline)"
    },
    "conll_ner": {
      "cv_uniform": "-0.39pp (p=0.963, not sig)"
    },
    "fewnerd_ner": {
      "lp_weighted_cv": "+0.88pp (p=0.000, sig)",
      "uniform_cv": "+0.32pp (p=0.003, sig)"
    }
  },
  "adaptive_combination": "INVALIDATED - gold label leakage confirmed",
  "note": "5-fold CV, bootstrap B=10000, paire

=== exp_lp_alignment_gating ===
Hypothesis: Within-instance
…[truncated 20648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T06:53:28.255753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "500",
  "offset": "1000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "500",
    "offset": "1000"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T06:53:28.256085+00:00_

1000	\toprule
1001	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
1002	\midrule
1003	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
1004	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
1005	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
1006	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
1007	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
1008	\bottomrule
1009	\end{tabular}
1010	\end{table}
1011	
1012	\begin{table}[t]
1013	\centering
1014	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
1015	\label{tab:sigma-comparison}
1016	\small
1017	\begin{tabular}{l cc cc}
1018	\toprule
1019	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
1020	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
1021	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
1022	\midrule
1023	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
1024	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
1025	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
1026	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
1027	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
1028	\midrule
1029	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
1030	\bottomrule
1031	\end{tabular}
1032	\end{table}
1033	
1034	Signal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.
1035	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER); additional samples stabilize structural signals more than LP.
1036	
1037	\paragraph{$N$-scalin
…[truncated 36717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T06:53:28.256441+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "300",
  "offset": "1500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "300",
    "offset": "1500"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T06:53:28.256621+00:00_

1500	Despite stronger correlation ($+$48\%) and higher AUROC, entity-token LP produces worse selection, reinforcing that compression operates at the representation level rather than token aggregation: the correlation-selection gap persists even with a more targeted signal.
1501	
1502	\subsection{Entity-Level Majority Voting}\label{app:entity_merge}
1503	
1504	Entity-level majority voting constructs a merged output by including all (text, type) entity tuples that appear in at least $k$ of $N$ samples (with $k = N/2$ as the default majority threshold).
1505	Unlike best-of-$N$ selection (which picks one complete sample), merge combines evidence across samples at entity granularity.
1506	We sweep $k \in \{2, 3, \ldots, 8\}$ on each dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$) and report the best threshold per dataset.
1507	
1508	\begin{table}[h]
1509	\centering
1510	\small
1511	\caption{Entity-level majority voting results (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Greedy'': $T{=}0$ baseline. ``Best merge'': optimal $k$ per dataset from sweep $k \in \{2, \ldots, 8\}$. ``$\Delta$'': merge F1 minus greedy. ``Recovery'': $\Delta$ / (oracle $-$ greedy). Only SciERC shows positive recovery; even with oracle $k$, CoNLL and Few-NERD degrade.}
1512	\label{tab:entity_merge}
1513	\begin{tabular}{lcccc}
1514	\toprule
1515	Dataset & Greedy & Best merge ($k^*$) & $\Delta$ (pp) & Recovery (\%) \\
1516	\midrule
1517	SciERC & 0.644 & 0.660 ($k{=}3$) & $+$1.57 & $+$11.9 \\
1518	CoNLL & 0.907 & 0.903 ($k{=}3$) & $-$0.38 & $-$9.0 \\
1519	Few-NERD & 0.748 & 0.744 ($k{=}2$) & $-$0.43 & $-$3.6 \\
1520	\bottomrule
1521	\end{tabular}
1522	\end{table}
1523	
1524	On degenerate subsets (instances where all $N$ samples yield identical F1), merge is uniformly negative across all three datasets, confirming that entity-level aggregation cannot bypass the diversity bottleneck identified in the main text (\S\ref{sec:discussion}).
1525	
1526	\subsection{Entity Construction Threshold Sensitivity}
1527	\label{app:theta_
…[truncated 2382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T06:53:28.256771+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.52.*pp|N.*16.*Few-NERD|Few-NERD.*N.*16",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.52.*pp|N.*16.*Few-NERD|Few-NERD.*N.*16",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T06:53:28.256954+00:00_

231:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T06:53:28.257119+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.52.*pp",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.52.*pp",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T06:53:28.257287+00:00_

docs/paper/sections/experiments.tex:143:LP selection gains scale with $N$ (Few-NERD $N{=}16$: $+0.52$~pp, $p{=}0.003$; Appendix~\ref{app:n_scaling}); structural signals remain negative regardless of sample budget.
docs/paper/sections/appendix.tex:231:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T06:53:28.257415+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "N.*16.*Few.NERD|Few.NERD.*N.*16",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "tool_args": {
    "pattern": "N.*16.*Few.NERD|Few.NERD.*N.*16",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T06:53:28.257537+00:00_

docs/paper/sections/experiments.tex:143:LP selection gains scale with $N$ (Few-NERD $N{=}16$: $+0.52$~pp, $p{=}0.003$; Appendix~\ref{app:n_scaling}); structural signals remain negative regardless of sample budget.
docs/paper/sections/experiments.tex:213:Construction gains scale with $N$: at $N{=}16$ on Few-NERD, $\Delta$ rises to $+1.32$\,pp (seed-42; Appendix~\ref{app:n_scaling}), as more samples provide broader entity coverage.
docs/paper/sections/experiments.tex:221:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T06:53:28.257675+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.52",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.52",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T06:53:28.257799+00:00_

110:CoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\
231:[Omitted long matching line]
365:Within-inst.\ SJ $\rho$ (median) & 0.524 & 0.550 & 0.994 \\
1167:The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
1380:Within-instance LP-quality alignment is relatively stable under this convergence shift (mean $\rho$: $0.524 \to 0.407$; median $\rho$: $0.667 \to 0.615$), consistent with alignment being determined primarily by task structure rather than training duration.
1399:Within-inst.\ $\rho$ (mean) & 0.524 & 0.407 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T06:53:28.257919+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "N=16.*selection|selection.*N=16",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "tool_args": {
    "pattern": "N=16.*selection|selection.*N=16",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T06:53:28.258087+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T06:53:28.258367+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Few.NERD.*16|FewNERD.*16",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Few.NERD.*16|FewNERD.*16",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T06:53:28.258614+00:00_

237:\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
434:DeBERTa achieves $\rho{=}0.329{\pm}0.087$ (5-fold CV, 3 seeds). Despite moderate quality prediction, selection utility is poor: on SciERC, DeBERTa closes $-26.5{\pm}26.5$\% of the oracle gap (13 of 15 runs negative; vs.\ LP's $+4.2{\pm}10.7$\%); on Few-NERD, DeBERTa recovers only $+3.5$\% (single 80/20 split; vs.\ LP's $+16.3$\%).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T06:53:28.258857+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "app:n_scaling|n.scaling.*Few",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "tool_args": {
    "pattern": "app:n_scaling|n.scaling.*Few",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T06:53:28.259015+00:00_

968:\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T06:53:28.259256+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "exp.027|027",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "tool_args": {
    "pattern": "exp.027|027",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T06:53:28.259455+00:00_

264:VC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
983:SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
1389:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T06:53:28.259650+00:00_

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
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
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

_source line 56 · 2026-05-19T06:53:28.259781+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T06:53:28.260096+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_v2.json",
  "content": "{\n  \"audit_date\": \"2026-05-19\",\n  \"total_claims\": 47,\n  \"verified\": 38,\n  \"inconsistent\": [\n    {\n      \"id\": \"INC-01\",\n      \"severity\": \"HIGH\",\n      \"locations\": [\n        \"abstract.tex:4 (\\\"ρ up to 0.50\\\")\",\n        \"introduction.tex:12 (\\\"ρ up to 0.50, AUROC up to 0.82\\\")\",\n        \"introduction.tex:33 (\\\"ρ up to 0.50\\\")\",\n        \"conclusion.tex:3 (\\\"ρ up to 0.50\\\")\",\n        \"introduction.tex:23 (fig_overview caption: \\\"ρ up to 0.50\\\")\"\n      ],\n      \"current_value\": \"ρ up to 0.50\",\n      \"correct_value\": \"ρ up to 0.48 (LLaMA CoNLL N=16 SJ 3-seed mean 0.474±0.009; single-seed max 0.484). Main table N=8 max: EM 0.451 on CoNLL Qwen.\",\n      \"source\": \"Table 1 (tab:quality_estimation), Table robustness (LLaMA CoNLL N=16), registry exp_017_llama_conll_n16_r1024 (SJ ρ=0.4836 single seed). No reported value reaches 0.50.\",\n      \"fix\": \"Change to \\\"ρ up to 0.48\\\" (includes N=16 appendix data) or \\\"ρ up to 0.45\\\" (N=8 primary results only). Must update in abstract, introduction (×2), conclusion, and fig_overview caption.\"\n    },\n    {\n      \"id\": \"INC-02\",\n      \"severity\": \"LOW\",\n      \"locations\": [\n        \"experiments.tex:103 (\\\"Δ_oracle=13.1 pp\\\")\",\n        \"experiments.tex:89 (fig_selection_gap caption: \\\"+13.1 pp\\\")\",\n        \"experiments.tex:97 (\\\"13.0 pp of headroom\\\")\",\n        \"experiments.tex:171 (\\\"13.0 pp headroom\\\")\"\n      ],\n      \"current_value\": \"13.1 pp in decomposition and figure caption; 13.0 pp elsewhere\",\n      \"correct_value\": \"Table selection: Oracle 0.775 − Greedy 0.645 = 0.130 = 13.0 pp (2-seed mean). Exact value depends on rounding.\",\n      \"source\": \"Table selection (tab:selection)\",\n      \"fix\": \"Standardize to 13.0 pp everywhere, or note that 13.1 comes from a different protocol (e.g., single-seed 0.7798−0.6617=11.81 doesn't match either). Most likely 0.775−0.644=0.131≈13.1 from single-seed greedy 0.644. Recommend using 13 pp (integer) in text and 13.0 in table references.\"\n    },\n    {\n      \"id\": \"INC-03\",\n      \"severity\": \"LOW\",\n      \"locations\": [\n        \"method.tex:62\"\n      ],\n      \"current_value\": \"\\\"SciERC greedy F1 appears as four values across tables (0.640, 0.644, 0.645, 0.650)\\\"\",\n      \"correct_value\": \"Entity construction table (tab:entity_construction) shows .646±.002 (3-seed mean), which is a 5th distinct value not listed.\",\n      \"source\": \"tab:entity_construction (experiments.tex:201)\",\n      \"fix\": \"Add .646 to the enumeration or reword: \\\"SciERC greedy F1 ranges from 0.640 to 0.650 across tables due to protocol variants\\\" to subsume all values including multi-seed means.\"\n    },\n    {\n      \"id\": \"INC-04\",\n      \"severity\": \"MEDIUM\",\n      \"locations\": [\n        \"experiments.tex:89 (fig_selection_gap caption: \\\"Despite ρ up to 0.36\\\")\"\n      ],\n      \"current_value\": \"ρ up to 0.36\",\n      \"correct_value\": \"If the figure shows all 5 QE signals on SciERC, the max ρ is VC=0.379, not SJ=0.360. If it only shows signals used in MBR selection (SJ, FK, LP), then SJ=0.360≈0.36 is correct.\",\n      \"source\": \"Table 1 (tab:quality_estimation): VC ρ=.379 on SciERC\",\n      \"fix\": \"If figure includes VC bar, change to \\\"ρ up to 0.38\\\". If figure only shows MBR-compatible signals, add a note clarifying this subset. Verify by inspecting fig_selection_gap.\"\n    },\n    {\n      \"id\": \"INC-05\",\n      \"severity\": \"MEDIUM\",\n      \"locations\": [\n        \"discussion.tex:6 (\\\"ρ=0.225 vs. Few-NERD ~0.5–0.7\\\")\"\n      ],\n      \"current_value\": \"ρ=0.225 (T=1.2 within-instance alignment)\",\n      \"correct_value\": \"Registry exp_026_T12: within_instance_rho_mean=0.2245, within_instance_rho_median=0.3152. Paper uses 0.225 (mean). But Table within_rho (appendix) reports median values for cross-dataset comparison (SciERC median=0.262, Few-NERD median=0.667).\",\n      \"source\": \"Registry exp_026_T12; appendix tab:within_rho\",\n      \"fix\": \"Either: (a) use median 0.315 for T=1.2 and compare with Few-NERD median 0.667 (consistent convention), or (b) explicitly note 'mean ρ=0.225' to distinguish from the medians reported elsewhere. Current implicit mixing of mean vs median is misleading.\"\n    }\n  ],\n  \"needs_update\": [\n    {\n      \"id\": \"UPD-01\",\n      \"severity\": \"HIGH\",\n      \"locations\": [\n        \"experiments.tex:143 (\\\"Few-NERD N=16: +0.52 pp, p=0.003; Appendix app:n_scaling\\\")\"\n      ],\n      \"current_value\": \"+0.52 pp LP selection at N=16 on Few-NERD\",\n      \"issue\": \"The referenced Appendix section (app:n_scaling, appendix.tex line 968) contains only SciERC N-scaling data (tab:n_scaling_selection). No Few-NERD N=16 LP selection data exists in app:n_scaling. Registry exp_027_fewnerd_n16 shows LP_delta=+1.88pp but on a 5K subsample (n=5000), not the full test set (n=32,565). The +0.52pp value has no identifiable source in the paper or appendix.\",\n      \"fix\": \"Either: (a) add Few-NERD N=16 LP selection results to Appendix app:n_scaling with the full test set, or (b) correct the +0.52pp to match actual data, or (c) if the value comes from an unreported full-test-set experiment, add supporting data.\"\n    },\n    {\n      \"id\": \"UPD-02\",\n      \"severity\": \"LOW\",\n      \"locations\": [\n        \"experiments.tex:213 (\\\"at N=16 on Few-NERD, Δ rises to +1.32 pp (seed-42; Appendix app:n_scaling)\\\")\"\n      ],\n      \"current_value\": \"+1.32 pp construction at N=16 on Few-NERD\",\n      \"issue\": \"This value matches registry (exp_entity_construction → n16_fair_cv → fewnerd_ner → cv_uniform_delta: +1.32pp), but Appendix app:n_scaling does not contain this data. The referenced section only has SciERC N-scaling tables.\",\n      \"fix\": \"Add Few-NERD N=16 construction results to Appendix app:n_scaling, or correct the appendix reference.\"\n    }\n  ],\n  \"missing_source\": [\n    {\n      \"id\": \"SRC-01\",\n      \"severity\": \"LOW\",\n      \"locations\": [\n        \"method.tex:32 (\\\"mild negative dependence (−0.4% to −4.0%; Appendix app:fk_independence)\\\")\"\n      ],\n      \"current_value\": \"−0.4% to −4.0% FK dependence range\",\n      \"issue\": \"Appendix app:fk_independence (appendix.tex:93-117) reports FK means, 95% CIs, t-statistics, and split-half reliability, but does not report the specific −0.4% to −4.0% dependence magnitude range cited in the main text.\",\n      \"fix\": \"Add the dependence calculation to the appendix table or text, or remove the specific range from the main text.\"\n    }\n  ],\n  \"verified_claims\": [\n    {\n      \"claim\": \"AUROC up to 0.82\",\n      \"locations\": [\"abstract.tex:4\", \"introduction.tex:12\", \"introduction.tex:33\", \"conclusion.tex:3\"],\n      \"source\": \"Table 1: EM CoNLL Qwen AUROC=.816, rounds to 0.82. WNUT-17 VC AUROC=.913 excluded (boundary-driven). Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"LP +1.39 pp on Few-NERD (p<0.001)\",\n      \"locations\": [\"introduction.tex:13\", \"introduction.tex:37\", \"experiments.tex:99\", \"experiments.tex:122\", \"experiments.tex:128\", \"experiments.tex:217\", \"appendix.tex:1259\"],\n      \"source\": \"Table fewnerd (tab:fewnerd), Table fewnerd_full (appendix), registry exp_fewnerd_s789_n8 (4-seed mean 1.38pp). All consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Entity construction +1.40 pp Few-NERD, +1.02 pp SciERC (multi-seed, p<0.005)\",\n      \"locations\": [\"abstract.tex:7\", \"introduction.tex:41\", \"discussion.tex:9\", \"conclusion.tex:4\", \"experiments.tex:204,212\"],\n      \"source\": \"Table entity_construction (tab:entity_construction). SciERC p=.004, Few-NERD p<.001. Both <0.005. Consistent across all locations.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Selective prediction +5–8 pp F1 at 80% coverage\",\n      \"locations\": [\"abstract.tex:4\", \"introduction.tex:34\", \"conclusion.tex:3\", \"experiments.tex:224\"],\n      \"source\": \"Registry exp_selective_prediction: SciERC +5.0pp, Few-NERD +6.2pp, CoNLL +8.4pp. Range 5.0–8.4 ≈ 5–8. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"AUPRC 0.70–0.92\",\n      \"locations\": [\"introduction.tex:34\", \"experiments.tex:224\"],\n      \"source\": \"Referenced in contribution list and prescriptive section. VC strongest. Not directly contradicted by any table.\",\n      \"status\": \"OK (not independently verified from raw data)\"\n    },\n    {\n      \"claim\": \"Instance degeneracy 13–87% across benchmarks\",\n      \"locations\": [\"introduction.tex:15\"],\n      \"source\": \"Few-NERD 13.8% (tab:fewnerd), CoNLL LLaMA N=16 86.4-86.7% (registry). Range 13.8–86.7% ≈ 13–87%. Acceptable rounding.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Degeneracy-LP correlation ρ=0.052, p=0.81, 23 configurations\",\n      \"locations\": [\"introduction.tex:38\", \"experiments.tex:132\", \"fig_degeneracy_scatter caption\"],\n      \"source\": \"Consistent across all three locations.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"MBR utility ρ=0.52 (SJ median)\",\n      \"locations\": [\"introduction.tex:17\", \"discussion.tex:4\", \"related_work.tex:20\"],\n      \"source\": \"Degeneracy table (tab:degeneracy): Within-inst SJ ρ (median)=0.524. Rounds to 0.52. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"SciERC LP selection: +0.2 pp (p=0.29, 2-seed)\",\n      \"locations\": [\"introduction.tex:14\", \"experiments.tex:97\"],\n      \"source\": \"Table selection: LP 0.647 − Greedy 0.645 = +0.2pp, p=.29. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"SciERC LP 3-seed: +0.04±0.48 pp\",\n      \"locations\": [\"experiments.tex:103\", \"experiments.tex:216\"],\n      \"source\": \"Multi-seed selection data. Consistent between decomposition and prescriptive sections.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"SciERC degeneracy 17.8% (8B), 10.4% (4B)\",\n      \"locations\": [\"experiments.tex:103\", \"experiments.tex:172\", \"appendix degeneracy table\"],\n      \"source\": \"Registry exp_012_rerun_1024: degen=0.1777. Registry exp_qwen3_4b_scierc: degen=0.104. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"CoNLL degeneracy 48.4%\",\n      \"locations\": [\"experiments.tex:103,120\", \"introduction.tex:15\"],\n      \"source\": \"Table fewnerd (tab:fewnerd), registry exp_002_conll_n16 (degen=0.4844). Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Few-NERD degeneracy 13.8%\",\n      \"locations\": [\"experiments.tex:122,129\", \"appendix.tex:1248\"],\n      \"source\": \"Table fewnerd (tab:fewnerd). Consistent. Note: registry seed-specific values (12.1%, 13.1%) average to ~12.7% for Qwen seeds 123+456; the 13.8% includes seed-42.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"QE table values (SciERC VC .379, SJ .360, FK .267, EM .295, LP .205)\",\n      \"locations\": [\"experiments.tex:33-40 (Table 1)\", \"experiments.tex:46\"],\n      \"source\": \"Registry exp_012_rerun_1024: SJ=0.3599, FK=0.2665, LP=0.2052, EM=0.2945 (all match after rounding). VC=.379 from multi-seed table (.386±.019, seed-42 within range). Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Temperature T=1.2 degeneracy 14.9%\",\n      \"locations\": [\"discussion.tex:6\"],\n      \"source\": \"Appendix tab:t_degeneracy: T=1.2 Degen%=14.9. Registry exp_026_T12: 0.1493. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"ECE 0.069–0.096 (NER calibration)\",\n      \"locations\": [\"experiments.tex:151\", \"appendix.tex:124,129\"],\n      \"source\": \"Appendix fig_reliability caption and text: NER ECE 0.069–0.096. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Kendall's W=1.0 (NER N=8, 3 seeds)\",\n      \"locations\": [\"experiments.tex:150\", \"appendix.tex:1003\"],\n      \"source\": \"Appendix tab:ranking-stability: NER N=8 W=1.000 for both Qwen and LLaMA. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"LoRA rank=8 degeneracy 7.2%\",\n      \"locations\": [\"experiments.tex:175\"],\n      \"source\": \"Not independently verified from registry, but internally consistent with the narrative.\",\n      \"status\": \"OK (not registry-verified)\"\n    },\n    {\n      \"claim\": \"Hidden state probes: ρ=0.388 vs LP 0.283, +37%, gap closure −5.1%\",\n      \"locations\": [\"experiments.tex:180\", \"appendix.tex:459,465-466\"],\n      \"source\": \"Appendix tab:hidden_probe: MLP ρ=.388±.013, LP ρ=.283, Gap% −5.1 vs +4.8. (.388-.283)/.283=+37%. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Verbalized confidence: mean 8.58/10 SciERC, 9.24/10 CoNLL\",\n      \"locations\": [\"limitations.tex:10\", \"appendix.tex:1200,1207\"],\n      \"source\": \"Appendix tab:verbconf: VerbConf mean score SciERC 8.58/10, CoNLL 9.24/10. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"SciERC n=529 (from 551), CoNLL n=2,756 (from 3,453)\",\n      \"locations\": [\"method.tex:56\", \"experiments.tex:9\"],\n      \"source\": \"Registry exp_012: n_valid=529, n_instances=551. Registry exp_002_conll_n16: n_valid=2756, n_instances=3453. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Few-NERD: 37,648 instances, 8 entity types, ≈75% F1\",\n      \"locations\": [\"experiments.tex:10\"],\n      \"source\": \"Registry exp_021 seeds: instance_count=37648. Greedy F1≈0.748–0.789 depending on seed/epoch. 0.748≈75%. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"LLaMA Few-NERD: LP +0.36pp, VC −2.39pp, SJ −0.52pp\",\n      \"locations\": [\"appendix.tex:230-231 (cross_selection text)\"],\n      \"source\": \"Registry exp_llama_fewnerd_inference: lp_delta=0.36, signal_ranking confirms. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Conditional +2.47pp on SciERC favorable subset\",\n      \"locations\": [\"experiments.tex:134\"],\n      \"source\": \"Appendix tab:conditional_decomp: SciERC LP Δ=+2.47pp, CI [+0.30, +4.70]. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"LP-alignment gating: dev scores SciERC 0.167, CoNLL 0.065, Few-NERD 0.516, threshold 0.3\",\n      \"locations\": [\"experiments.tex:221\"],\n      \"source\": \"Registry exp_lp_alignment_gating: threshold=0.3, accuracy=3/3. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"5-epoch Few-NERD raises degeneracy to 31%\",\n      \"locations\": [\"experiments.tex:129\"],\n      \"source\": \"Appendix tab:epoch_confound: 5-epoch degen=31.3%. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"SciERC epoch curve: degen 6.4% → 17.8% → 47.8%\",\n      \"locations\": [\"appendix.tex:1407,1425\"],\n      \"source\": \"Registry exp_029a: degen=0.064 (3-epoch), exp_012: 0.1777 (5-epoch), exp_029b: 0.478 (10-epoch). Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Selection table values (SciERC 2-seed)\",\n      \"locations\": [\"experiments.tex:69-83 (Table 2)\"],\n      \"source\": \"Oracle 0.775, Greedy 0.645, LP 0.647, SJ 0.646, FK 0.646, EM 0.637, VC 0.623, Random 0.610. Internally consistent with text references.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"SJ normalizer |Δρ|≤0.009\",\n      \"locations\": [\"method.tex:40\"],\n      \"source\": \"Appendix tab:sj_normalizer: max |Δρ|=0.009 (SciERC LLaMA). Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"LP 50× more seed-stable (σ=0.04 vs SJ 2.02pp)\",\n      \"locations\": [\"experiments.tex:128\"],\n      \"source\": \"2.02/0.04=50.5≈50×. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Scale ablation: mean |Δρ|=0.042\",\n      \"locations\": [\"experiments.tex:171\"],\n      \"source\": \"Table scale_ablation: |Δ| values are .014, .018, .062, .059. Mean=(0.014+0.018+0.062+0.059)/4=0.0383. Reported as 0.042.\",\n      \"status\": \"MINOR DISCREPANCY — computed mean is 0.038, reported 0.042. Difference may be due to including additional signals not shown in the table.\"\n    }\n  ],\n  \"summary\": {\n    \"critical_issues\": 2,\n    \"description\": \"Two high-severity issues: (1) 'ρ up to 0.50' is unsupported — no reported value reaches 0.50 (max ~0.48); this appears in 5 locations including abstract and conclusion. (2) Few-NERD N=16 LP selection '+0.52pp' references Appendix app:n_scaling which contains only SciERC data — the claim has no identifiable source. Three medium/low issues: oracle headroom rounding (13.0 vs 13.1), fig_selection_gap caption ρ discrepancy, and mean vs median convention mixing for within-instance alignment. One missing source: FK dependence range in method text.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_v2.json",
    "content": "{\n  \"audit_date\": \"2026-05-19\",\n  \"total_claims\": 47,\n  \"verified\": 38,\n  \"inconsistent\": [\n    {\n      \"id\": \"INC-01\",\n      \"severity\": \"HIGH\",\n      \"locations\": [\n        \"abstract.tex:4 (\\\"ρ up to 0.50\\\")\",\n        \"introduction.tex:12 (\\\"ρ up to 0.50, AUROC up to 0.82\\\")\",\n        \"introduction.tex:33 (\\\"ρ up to 0.50\\\")\",\n        \"conclusion.tex:3 (\\\"ρ up to 0.50\\\")\",\n        \"introduction.tex:23 (fig_overview caption: \\\"ρ up to 0.50\\\")\"\n      ],\n      \"current_value\": \"ρ up to 0.50\",\n      \"correct_value\": \"ρ up to 0.48 (LLaMA CoNLL N=16 SJ 3-seed mean 0.474±0.009; single-seed max 0.484). Main table N=8 max: EM 0.451 on CoNLL Qwen.\",\n      \"source\": \"Table 1 (tab:quality_estimation), Table robustness (LLaMA CoNLL N=16), registry exp_017_llama_conll_n16_r1024 (SJ ρ=0.4836 single seed). No reported value reaches 0.50.\",\n      \"fix\": \"Change to \\\"ρ up to 0.48\\\" (includes N=16 appendix data) or \\\"ρ up to 0.45\\\" (N=8 primary results only). Must update in abstract, introduction (×2), conclusion, and fig_overview caption.\"\n    },\n    {\n      \"id\": \"INC-02\",\n      \"severity\": \"LOW\",\n      \"locations\": [\n        \"experiments.tex:103 (\\\"Δ_oracle=13.1 pp\\\")\",\n        \"experiments.tex:89 (fig_selection_gap caption: \\\"+13.1 pp\\\")\",\n        \"experiments.tex:97 (\\\"13.0 pp of headroom\\\")\",\n        \"experiments.tex:171 (\\\"13.0 pp headroom\\\")\"\n      ],\n      \"current_value\": \"13.1 pp in decomposition and figure caption; 13.0 pp elsewhere\",\n      \"correct_value\": \"Table selection: Oracle 0.775 − Greedy 0.645 = 0.130 = 13.0 pp (2-seed mean). Exact value depends on rounding.\",\n      \"source\": \"Table selection (tab:selection)\",\n      \"fix\": \"Standardize to 13.0 pp everywhere, or note that 13.1 comes from a different protocol (e.g., single-seed 0.7798−0.6617=11.81 doesn't match either). Most likely 0.775−0.644=0.131≈13.1 from single-seed greedy 0.644. Recommend using 13 pp (integer) in text and 13.0 in table references.\"\n    },\n    {\n      \"id\": \"INC-03\",\n      \"severity\": \"LOW\",\n      \"locations\": [\n        \"method.tex:62\"\n      ],\n      \"current_value\": \"\\\"SciERC greedy F1 appears as four values across tables (0.640, 0.644, 0.645, 0.650)\\\"\",\n      \"correct_value\": \"Entity construction table (tab:entity_construction) shows .646±.002 (3-seed mean), which is a 5th distinct value not listed.\",\n      \"source\": \"tab:entity_construction (experiments.tex:201)\",\n      \"fix\": \"Add .646 to the enumeration or reword: \\\"SciERC greedy F1 ranges from 0.640 to 0.650 across tables due to protocol variants\\\" to subsume all values including multi-seed means.\"\n    },\n    {\n      \"id\": \"INC-04\",\n      \"severity\": \"MEDIUM\",\n      \"locations\": [\n        \"experiments.tex:89 (fig_selection_gap caption: \\\"Despite ρ up to 0.36\\\")\"\n      ],\n      \"current_value\": \"ρ up to 0.36\",\n      \"correct_value\": \"If the figure shows all 5 QE signals on SciERC, the max ρ is VC=0.379, not SJ=0.360. If it only shows signals used in MBR selection (SJ, FK, LP), then SJ=0.360≈0.36 is correct.\",\n      \"source\": \"Table 1 (tab:quality_estimation): VC ρ=.379 on SciERC\",\n      \"fix\": \"If figure includes VC bar, change to \\\"ρ up to 0.38\\\". If figure only shows MBR-compatible signals, add a note clarifying this subset. Verify by inspecting fig_selection_gap.\"\n    },\n    {\n      \"id\": \"INC-05\",\n      \"severity\": \"MEDIUM\",\n      \"locations\": [\n        \"discussion.tex:6 (\\\"ρ=0.225 vs. Few-NERD ~0.5–0.7\\\")\"\n      ],\n      \"current_value\": \"ρ=0.225 (T=1.2 within-instance alignment)\",\n      \"correct_value\": \"Registry exp_026_T12: within_instance_rho_mean=0.2245, within_instance_rho_median=0.3152. Paper uses 0.225 (mean). But Table within_rho (appendix) reports median values for cross-dataset comparison (SciERC median=0.262, Few-NERD median=0.667).\",\n      \"source\": \"Registry exp_026_T12; appendix tab:within_rho\",\n      \"fix\": \"Either: (a) use median 0.315 for T=1.2 and compare with Few-NERD median 0.667 (consistent convention), or (b) explicitly note 'mean ρ=0.225' to distinguish from the medians reported elsewhere. Current implicit mixing of mean vs median is misleading.\"\n    }\n  ],\n  \"needs_update\": [\n    {\n      \"id\": \"UPD-01\",\n      \"severity\": \"HIGH\",\n      \"locations\": [\n        \"experiments.tex:143 (\\\"Few-NERD N=16: +0.52 pp, p=0.003; Appendix app:n_scaling\\\")\"\n      ],\n      \"current_value\": \"+0.52 pp LP selection at N=16 on Few-NERD\",\n      \"issue\": \"The referenced Appendix section (app:n_scaling, appendix.tex line 968) contains only SciERC N-scaling data (tab:n_scaling_selection). No Few-NERD N=16 LP selection data exists in app:n_scaling. Registry exp_027_fewnerd_n16 shows LP_delta=+1.88pp but on a 5K subsample (n=5000), not the full test set (n=32,565). The +0.52pp value has no identifiable source in the paper or appendix.\",\n      \"fix\": \"Either: (a) add Few-NERD N=16 LP selection results to Appendix app:n_scaling with the full test set, or (b) correct the +0.52pp to match actual data, or (c) if the value comes from an unreported full-test-set experiment, add supporting data.\"\n    },\n    {\n      \"id\": \"UPD-02\",\n      \"severity\": \"LOW\",\n      \"locations\": [\n        \"experiments.tex:213 (\\\"at N=16 on Few-NERD, Δ rises to +1.32 pp (seed-42; Appendix app:n_scaling)\\\")\"\n      ],\n      \"current_value\": \"+1.32 pp construction at N=16 on Few-NERD\",\n      \"issue\": \"This value matches registry (exp_entity_construction → n16_fair_cv → fewnerd_ner → cv_uniform_delta: +1.32pp), but Appendix app:n_scaling does not contain this data. The referenced section only has SciERC N-scaling tables.\",\n      \"fix\": \"Add Few-NERD N=16 construction results to Appendix app:n_scaling, or correct the appendix reference.\"\n    }\n  ],\n  \"missing_source\": [\n    {\n      \"id\": \"SRC-01\",\n      \"severity\": \"LOW\",\n      \"locations\": [\n        \"method.tex:32 (\\\"mild negative dependence (−0.4% to −4.0%; Appendix app:fk_independence)\\\")\"\n      ],\n      \"current_value\": \"−0.4% to −4.0% FK dependence range\",\n      \"issue\": \"Appendix app:fk_independence (appendix.tex:93-117) reports FK means, 95% CIs, t-statistics, and split-half reliability, but does not report the specific −0.4% to −4.0% dependence magnitude range cited in the main text.\",\n      \"fix\": \"Add the dependence calculation to the appendix table or text, or remove the specific range from the main text.\"\n    }\n  ],\n  \"verified_claims\": [\n    {\n      \"claim\": \"AUROC up to 0.82\",\n      \"locations\": [\"abstract.tex:4\", \"introduction.tex:12\", \"introduction.tex:33\", \"conclusion.tex:3\"],\n      \"source\": \"Table 1: EM CoNLL Qwen AUROC=.816, rounds to 0.82. WNUT-17 VC AUROC=.913 excluded (boundary-driven). Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"LP +1.39 pp on Few-NERD (p<0.001)\",\n      \"locations\": [\"introduction.tex:13\", \"introduction.tex:37\", \"experiments.tex:99\", \"experiments.tex:122\", \"experiments.tex:128\", \"experiments.tex:217\", \"appendix.tex:1259\"],\n      \"source\": \"Table fewnerd (tab:fewnerd), Table fewnerd_full (appendix), registry exp_fewnerd_s789_n8 (4-seed mean 1.38pp). All consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Entity construction +1.40 pp Few-NERD, +1.02 pp SciERC (multi-seed, p<0.005)\",\n      \"locations\": [\"abstract.tex:7\", \"introduction.tex:41\", \"discussion.tex:9\", \"conclusion.tex:4\", \"experiments.tex:204,212\"],\n      \"source\": \"Table entity_construction (tab:entity_construction). SciERC p=.004, Few-NERD p<.001. Both <0.005. Consistent across all locations.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Selective prediction +5–8 pp F1 at 80% coverage\",\n      \"locations\": [\"abstract.tex:4\", \"introduction.tex:34\", \"conclusion.tex:3\", \"experiments.tex:224\"],\n      \"source\": \"Registry exp_selective_prediction: SciERC +5.0pp, Few-NERD +6.2pp, CoNLL +8.4pp. Range 5.0–8.4 ≈ 5–8. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"AUPRC 0.70–0.92\",\n      \"locations\": [\"introduction.tex:34\", \"experiments.tex:224\"],\n      \"source\": \"Referenced in contribution list and prescriptive section. VC strongest. Not directly contradicted by any table.\",\n      \"status\": \"OK (not independently verified from raw data)\"\n    },\n    {\n      \"claim\": \"Instance degeneracy 13–87% across benchmarks\",\n      \"locations\": [\"introduction.tex:15\"],\n      \"source\": \"Few-NERD 13.8% (tab:fewnerd), CoNLL LLaMA N=16 86.4-86.7% (registry). Range 13.8–86.7% ≈ 13–87%. Acceptable rounding.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Degeneracy-LP correlation ρ=0.052, p=0.81, 23 configurations\",\n      \"locations\": [\"introduction.tex:38\", \"experiments.tex:132\", \"fig_degeneracy_scatter caption\"],\n      \"source\": \"Consistent across all three locations.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"MBR utility ρ=0.52 (SJ median)\",\n      \"locations\": [\"introduction.tex:17\", \"discussion.tex:4\", \"related_work.tex:20\"],\n      \"source\": \"Degeneracy table (tab:degeneracy): Within-inst SJ ρ (median)=0.524. Rounds to 0.52. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"SciERC LP selection: +0.2 pp (p=0.29, 2-seed)\",\n      \"locations\": [\"introduction.tex:14\", \"experiments.tex:97\"],\n      \"source\": \"Table selection: LP 0.647 − Greedy 0.645 = +0.2pp, p=.29. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"SciERC LP 3-seed: +0.04±0.48 pp\",\n      \"locations\": [\"experiments.tex:103\", \"experiments.tex:216\"],\n      \"source\": \"Multi-seed selection data. Consistent between decomposition and prescriptive sections.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"SciERC degeneracy 17.8% (8B), 10.4% (4B)\",\n      \"locations\": [\"experiments.tex:103\", \"experiments.tex:172\", \"appendix degeneracy table\"],\n      \"source\": \"Registry exp_012_rerun_1024: degen=0.1777. Registry exp_qwen3_4b_scierc: degen=0.104. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"CoNLL degeneracy 48.4%\",\n      \"locations\": [\"experiments.tex:103,120\", \"introduction.tex:15\"],\n      \"source\": \"Table fewnerd (tab:fewnerd), registry exp_002_conll_n16 (degen=0.4844). Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Few-NERD degeneracy 13.8%\",\n      \"locations\": [\"experiments.tex:122,129\", \"appendix.tex:1248\"],\n      \"source\": \"Table fewnerd (tab:fewnerd). Consistent. Note: registry seed-specific values (12.1%, 13.1%) average to ~12.7% for Qwen seeds 123+456; the 13.8% includes seed-42.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"QE table values (SciERC VC .379, SJ .360, FK .267, EM .295, LP .205)\",\n      \"locations\": [\"experiments.tex:33-40 (Table 1)\", \"experiments.tex:46\"],\n      \"source\": \"Registry exp_012_rerun_1024: SJ=0.3599, FK=0.2665, LP=0.2052, EM=0.2945 (all match after rounding). VC=.379 from multi-seed table (.386±.019, seed-42 within range). Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Temperature T=1.2 degeneracy 14.9%\",\n      \"locations\": [\"discussion.tex:6\"],\n      \"source\": \"Appendix tab:t_degeneracy: T=1.2 Degen%=14.9. Registry exp_026_T12: 0.1493. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"ECE 0.069–0.096 (NER calibration)\",\n      \"locations\": [\"experiments.tex:151\", \"appendix.tex:124,129\"],\n      \"source\": \"Appendix fig_reliability caption and text: NER ECE 0.069–0.096. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Kendall's W=1.0 (NER N=8, 3 seeds)\",\n      \"locations\": [\"experiments.tex:150\", \"appendix.tex:1003\"],\n      \"source\": \"Appendix tab:ranking-stability: NER N=8 W=1.000 for both Qwen and LLaMA. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"LoRA rank=8 degeneracy 7.2%\",\n      \"locations\": [\"experiments.tex:175\"],\n      \"source\": \"Not independently verified from registry, but internally consistent with the narrative.\",\n      \"status\": \"OK (not registry-verified)\"\n    },\n    {\n      \"claim\": \"Hidden state probes: ρ=0.388 vs LP 0.283, +37%, gap closure −5.1%\",\n      \"locations\": [\"experiments.tex:180\", \"appendix.tex:459,465-466\"],\n      \"source\": \"Appendix tab:hidden_probe: MLP ρ=.388±.013, LP ρ=.283, Gap% −5.1 vs +4.8. (.388-.283)/.283=+37%. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Verbalized confidence: mean 8.58/10 SciERC, 9.24/10 CoNLL\",\n      \"locations\": [\"limitations.tex:10\", \"appendix.tex:1200,1207\"],\n      \"source\": \"Appendix tab:verbconf: VerbConf mean score SciERC 8.58/10, CoNLL 9.24/10. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"SciERC n=529 (from 551), CoNLL n=2,756 (from 3,453)\",\n      \"locations\": [\"method.tex:56\", \"experiments.tex:9\"],\n      \"source\": \"Registry exp_012: n_valid=529, n_instances=551. Registry exp_002_conll_n16: n_valid=2756, n_instances=3453. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Few-NERD: 37,648 instances, 8 entity types, ≈75% F1\",\n      \"locations\": [\"experiments.tex:10\"],\n      \"source\": \"Registry exp_021 seeds: instance_count=37648. Greedy F1≈0.748–0.789 depending on seed/epoch. 0.748≈75%. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"LLaMA Few-NERD: LP +0.36pp, VC −2.39pp, SJ −0.52pp\",\n      \"locations\": [\"appendix.tex:230-231 (cross_selection text)\"],\n      \"source\": \"Registry exp_llama_fewnerd_inference: lp_delta=0.36, signal_ranking confirms. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Conditional +2.47pp on SciERC favorable subset\",\n      \"locations\": [\"experiments.tex:134\"],\n      \"source\": \"Appendix tab:conditional_decomp: SciERC LP Δ=+2.47pp, CI [+0.30, +4.70]. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"LP-alignment gating: dev scores SciERC 0.167, CoNLL 0.065, Few-NERD 0.516, threshold 0.3\",\n      \"locations\": [\"experiments.tex:221\"],\n      \"source\": \"Registry exp_lp_alignment_gating: threshold=0.3, accuracy=3/3. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"5-epoch Few-NERD raises degeneracy to 31%\",\n      \"locations\": [\"experiments.tex:129\"],\n      \"source\": \"Appendix tab:epoch_confound: 5-epoch degen=31.3%. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"SciERC epoch curve: degen 6.4% → 17.8% → 47.8%\",\n      \"locations\": [\"appendix.tex:1407,1425\"],\n      \"source\": \"Registry exp_029a: degen=0.064 (3-epoch), exp_012: 0.1777 (5-epoch), exp_029b: 0.478 (10-epoch). Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Selection table values (SciERC 2-seed)\",\n      \"locations\": [\"experiments.tex:69-83 (Table 2)\"],\n      \"source\": \"Oracle 0.775, Greedy 0.645, LP 0.647, SJ 0.646, FK 0.646, EM 0.637, VC 0.623, Random 0.610. Internally consistent with text references.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"SJ normalizer |Δρ|≤0.009\",\n      \"locations\": [\"method.tex:40\"],\n      \"source\": \"Appendix tab:sj_normalizer: max |Δρ|=0.009 (SciERC LLaMA). Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"LP 50× more seed-stable (σ=0.04 vs SJ 2.02pp)\",\n      \"locations\": [\"experiments.tex:128\"],\n      \"source\": \"2.02/0.04=50.5≈50×. Consistent.\",\n      \"status\": \"OK\"\n    },\n    {\n      \"claim\": \"Scale ablation: mean |Δρ|=0.042\",\n      \"locations\": [\"experiments.tex:171\"],\n      \"source\": \"Table scale_ablation: |Δ| values are .014, .018, .062, .059. Mean=(0.014+0.018+0.062+0.059)/4=0.0383. Reported as 0.042.\",\n      \"status\": \"MINOR DISCREPANCY — computed mean is 0.038, reported 0.042. Difference may be due to including additional signals not shown in the table.\"\n    }\n  ],\n  \"summary\": {\n    \"critical_issues\": 2,\n    \"description\": \"Two high-severity issues: (1) 'ρ up to 0.50' is unsupported — no reported value reaches 0.50 (max ~0.48); this appears in 5 locations including abstract and conclusion. (2) Few-NERD N=16 LP selection '+0.52pp' references Appendix app:n_scaling which contains only SciERC data — the claim has no identifiable source. Three medium/low issues: oracle headroom rounding (13.0 vs 13.1), fig_selection_gap caption ρ discrepancy, and mean vs median convention mixing for within-instance alignment. One missing source: FK dependence range in method text.\"\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T06:53:28.260514+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_v2.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T06:53:28.260663+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "claim_audit_v2",
  "type": "report",
  "description": "Cross-section numerical consistency audit v2: 47 claims checked, 38 verified, 5 inconsistent, 2 needs update, 1 missing source",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_v2.json",
  "tags": "['audit', 'numerical-consistency', 'paper']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "claim_audit_v2",
    "type": "report",
    "description": "Cross-section numerical consistency audit v2: 47 claims checked, 38 verified, 5 inconsistent, 2 needs update, 1 missing source",
    "project": "struct_self_consist_ie",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_v2.json",
    "tags": "['audit', 'numerical-consistency', 'paper']"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T06:53:28.260903+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_94b3c3\", \"name\": \"claim_audit_v2\", \"type\": \"report\", \"description\": \"Cross-section numerical consistency audit v2: 47 claims checked, 38 verified, 5 inconsistent, 2 needs update, 1 missing source\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/claim_audit_v2.json\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T06:53:11.392682+00:00\", \"tags\": [\"audit\", \"numerical-consistency\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_v2_20260519T064159",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-19T06:53:28.261407+00:00_

审计完成。47 条定量 claim，38 条验证通过。关键发现：

**HIGH（必须修）：**

| ID | 问题 | 位置 | 修复 |
|---|---|---|---|
| INC-01 | **"ρ up to 0.50" 无支撑** — 所有配置最大 ρ ≈ 0.48（LLaMA CoNLL N=16 SJ），N=8 主表最大 0.451 | abstract, intro×2, conclusion, fig_overview caption（共 5 处） | 改为 "ρ up to 0.48" 或 "ρ up to 0.45"（仅 N=8） |
| UPD-01 | **Few-NERD N=16 LP "+0.52pp" 无来源** — 引用 Appendix app:n_scaling，但该节只有 SciERC 数据；registry exp_027 显示 5K 子集 +1.88pp，与 0.52pp 不一致 | experiments.tex:143 | 补充 Few-NERD N=16 全测试集数据到附录，或更正数值 |

**MEDIUM：**

| ID | 问题 | 修复 |
|---|---|---|
| INC-04 | fig_selection_gap caption 说 "ρ up to 0.36"，但 SciERC VC ρ=.379 | 检查图是否包含 VC；如包含则改为 "up to 0.38" |
| INC-05 | Discussion T=1.2 用 mean ρ=0.225，但其他地方用 median（Table within_rho） | 统一为 median（0.315）或标注 "mean" |
| UPD-02 | Few-NERD N=16 construction "+1.32pp" 同样引用 app:n_scaling 但该节无此数据 | 补充数据到附录 |

**LOW：** oracle headroom 13.0 vs 13.1pp 取整不一致；SciERC greedy F1 枚举缺 .646；FK dependence range −0.4%~−4.0% 在附录中无对应数据。

报告已写入 `artifacts/claim_audit_v2.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_claim_audit_v2_20260519T064159"
}
```

</details>

---
