# analysis claim audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 85
- **Recorded user turns:** 0
- **Tool calls:** 42
- **Original source:** `logs/chats/worker_analysis_claim_audit_20260519T133313.jsonl`
- **Structured JSON:** [`c90bbc51df4cfc7dae2e.json`](../../sessions/c9/c90bbc51df4cfc7dae2e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

85 recorded events

### Tool call

_source line 1 · 2026-05-19T13:46:31.787410+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T13:46:31.787741+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T13:46:31.787939+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T13:46:31.788443+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md\", \"content\": \"# Paper Framing — struct_self_consist_ie\\n\\n> Updated 2026-05-19 — D157+D160 TRIPLE CONTRIBUTION + SCALE UPGRADE. Title: \\\"Strong Predictors, Weak Selectors: Addressing the Correlation-Selection Gap in Self-Consistency for Named Entity Recognition\\\". Entity construction θ=2/N (+1.02pp SciERC, +1.40pp FewNERD, multi-seed N=8 mean). **72B zero-shot confirms gap is fundamental**: LP ρ=-0.002 (CoNLL) / 0.081 (SciERC); LP-weighted construction +1.53pp (SciERC ZS); θ=2/N fails in zero-shot (-0.52pp SciERC, -0.92pp CoNLL). Gating bootstrap CI: τ=0.3 stable in [0.2,0.4]. D162: Decomposition formula deleted (R²=-8.53). Scale: 7B→14B→32B→72B Qwen2.5 + 8B cross-family (Qwen3+LLaMA). 14B/32B training in progress.\\n\\n## Target Venue\\n- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)\\n- Deadline: ARR May cycle, 2026-05-25\\n\\n## Core Claims (D157 updated — TRIPLE CONTRIBUTION: QE + diagnostic + prescriptive)\\n\\n### Claim 1 (PRIMARY — Dual Contribution: QE Framework + Selection Diagnostic)\\n**Positive contribution (A)**: Confidence signals reliably predict structured IE output quality at the population level (AUROC up to 0.82, ρ up to 0.45), enabling practical QE/selective prediction.\\n**Diagnostic contribution (B)** (D154 revised): Selection viability depends on LP signal quality and dataset characteristics, not degeneracy alone:\\n- **Degeneracy as headroom predictor**: High degeneracy eliminates selection headroom (CoNLL 47.4% degen → 0 net gain). Within fixed dataset-model settings, degeneracy causally modulates LP effectiveness (SciERC epoch ablation: −1.18/+0.74/+0.99pp at 3/5/10 epochs; per-entity-type within Few-NERD ρ=−0.881). But across datasets, degeneracy alone does NOT predict LP selection direction (23-point cross-configuration ρ=0.052, p=0.81).\\n- **LP-quality alignment as 
…[truncated 34717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T13:46:31.788647+00:00_

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
  "session": "worker_analysis_claim_audit_20260519T133313",
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

_source line 6 · 2026-05-19T13:46:31.790044+00:00_

Error: result (265,254 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T13:46:31.790299+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T13:46:31.790461+00:00_

artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
artifacts/bootstrap_ci_tables.tex
artifacts/dream_reports/dream_20260515T092545/best/paper.tex
artifacts/dream_reports/dream_20260515T092545/median/paper.tex
artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
artifacts/_project/paper/freeform_ablation_appendix_table.tex
artifacts/freeform_ablation_appendix_table.tex
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
artifacts/n_scaling_appendix_tables.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/n_scaling_appendix_tables.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260516T092241/best/paper.tex
artifacts/dream_reports/dream_20260516T092241/median/paper.tex
artifacts/dream_reports/dream_20260516T092241/worst/paper.tex
artifacts/dream_reports/dream_20260516T113255/best/paper.tex
artifacts/dream_reports/dream_20260516T113255/median/paper.tex
artifacts/dream_reports/dream_20260516T113255/worst/paper.tex
artifacts/per_type_lp_table.tex
artifacts/exp_021_fewnerd_full/paper/per_type_lp_table.tex
docs/paper/sections/checklist.tex
docs/paper/main.tex
docs/paper/sections/appendix.tex
docs/paper/sections/method.tex
docs/paper/sections/related_work.tex
docs/paper/section
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T13:46:31.790610+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T13:46:31.790734+00:00_

docs/paper/sections/checklist.tex
docs/paper/sections/appendix.tex
docs/paper/sections/method.tex
docs/paper/sections/related_work.tex
docs/paper/sections/introduction.tex
docs/paper/sections/abstract.tex
docs/paper/sections/limitations.tex
docs/paper/sections/discussion.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T13:46:31.790861+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T13:46:31.790981+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T13:46:31.791143+00:00_

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
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T13:46:31.791287+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
4	All signals achieve reliable QE ($\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
6	We identify three qualitative factors: instance degeneracy, oracle headroom, and LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.
7	The diagnostic naturally motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T13:46:31.791415+00:00_

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
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T13:46:31.791578+00:00_

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
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low inst
…[truncated 4643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T13:46:31.791727+00:00_

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
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T13:46:31.792059+00:00_

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
…[truncated 4161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T13:46:31.792260+00:00_

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
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T13:46:31.792512+00:00_

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
…[truncated 18335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T13:46:31.792672+00:00_

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
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T13:46:31.792810+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
4	Three factors qualitatively constrain selection: instance degeneracy (17.8--67.9\%) compresses the candidate space, limited oracle headroom bounds achievable gains, and LP compression (within-instance $\rho$ 0.043--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\rho{=}0.524$) \cite{eikema2022sampling}.
5	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP selection yields $+2.9$~pp ($p{=}0.004$; Table~\ref{tab:nontied_main}), but $\varepsilon{=}0.05$ is post-hoc ($p_{\text{adj}}{=}0.14$ after joint correction; Appendix~\ref{app:epsilon_robustness}), so this is exploratory evidence.
6	Temperature disentangles degeneracy from alignment: at $T{=}1.2$, degeneracy drops to 14.9\% yet LP does not improve (median $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}); the selection window narrows as models improve \cite{wang2023selfconsistency, snell2025scaling}.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms (Table~\ref{tab:entity_construction}), complementary with LP selection and governed by LP-quality alignment (\S\ref{sec:prescriptive}).
10	Alternative strategies (DALS, MBR, DGS) fail to reliably beat greedy (Appendix~\ref{app:dals}); our negative results are specific to fine-tuned models with constrained decoding (Appendix~\ref{app:when_selection_works}).
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T13:46:31.792969+00:00_

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
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T13:46:31.793221+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	All experiments use English-language datasets; cross-lingual generalization remains untested.
3	Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
4	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples (potentially reducing degeneracy), but their LP-quality alignment behavior is unknown, and these two factors may shift in opposite directions.
5	Our supervised approaches (DeBERTa verifier, hidden state probes, MLP/RF on signal combinations) all fail to close the oracle gap; whether content-aware verifiers with access to task-specific structure could succeed remains open.
6	
7	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
8	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
9	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
10	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
11	We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
12	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$
…[truncated 2276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T13:46:31.793380+00:00_

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
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T13:46:31.793507+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Five confidence signals achieve reliable NER quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage). Instance-level selection fails due to degeneracy and LP compression; entity-level construction yields $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC ($p{<}0.005$), complementary with LP selection and governed by LP-quality alignment. For practitioners: use QE for selective prediction; apply construction when multi-sample generation is feasible; assess LP-alignment to route between strategies. As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \cite{cobbe2021verifiers} may be needed to close the remaining gap.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T13:46:31.793632+00:00_

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
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T13:46:31.793782+00:00_

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
13	Ensemble approaches aggregate predictions from multiple models or prompts \cite{florian2003named, xiao2025el4ner}; \citet{xie2023zeroshot} propose two-stage entity voting for zero-shot NER, the closest prior work to our entity-level construction.
14	LLM-Blender \cite{jiang2023llmblender} fuses outputs from multiple LLMs via pairwise ranking, whereas our single-model stochastic sampling derives diversity from temperature rather than model heterogeneity.
15	Our 
…[truncated 2659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T13:46:31.793922+00:00_

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
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T13:46:31.794038+00:00_

File content (41705 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T13:46:31.794207+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result.get('data', result.get('experiments', []))\ntarget_ids = [\n    'exp_012_logprob_baseline', 'exp_001_ner_n16_scierc', 'exp_006_v2',\n    'exp_016_signal_ensemble', 'exp_023_lora_rank8', 'exp_entity_construction',\n    'exp_llama_fewnerd_inference', 'exp_qwen25_72b_zeroshot',\n    'exp_016_rerun_1024', 'exp_021_fewnerd_full', 'exp_freeform_ablation',\n    'exp_012_rerun_1024', 'exp_016_rerun_1024_bootstrap',\n    'exp_scale_4b', 'exp_scale_ablation', 'exp_018'\n]\nfor exp in exps:\n    eid = exp.get('exp_id', '')\n    if any(t in eid for t in target_ids):\n        print(f'=== {eid} ===')\n        print(f'status: {exp.get(\\\"status\\\", \\\"?\\\")}')\n        print(f'conclusion: {exp.get(\\\"conclusion\\\", \\\"?\\\")}')\n        metrics = exp.get('metrics', {})\n        if metrics:\n            print(f'metrics: {json.dumps(metrics, indent=2)[:3000]}')\n        print()\n\" 2>&1 | head -500\n",
  "description": "Extract key experiment data from registry",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result.get('data', result.get('experiments', []))\ntarget_ids = [\n    'exp_012_logprob_baseline', 'exp_001_ner_n16_scierc', 'exp_006_v2',\n    'exp_016_signal_ensemble', 'exp_023_lora_rank8', 'exp_entity_construction',\n    'exp_llama_fewnerd_inference', 'exp_qwen25_72b_zeroshot',\n    'exp_016_rerun_1024', 'exp_021_fewnerd_full', 'exp_freeform_ablation',\n    'exp_012_rerun_1024', 'exp_016_rerun_1024_bootstrap',\n    'exp_scale_4b', 'exp_scale_ablation', 'exp_018'\n]\nfor exp in exps:\n    eid = exp.get('exp_id', '')\n    if any(t in eid for t in target_ids):\n        print(f'=== {eid} ===')\n        print(f'status: {exp.get(\\\"status\\\", \\\"?\\\")}')\n        print(f'conclusion: {exp.get(\\\"conclusion\\\", \\\"?\\\")}')\n        metrics = exp.get('metrics', {})\n        if metrics:\n            print(f'metrics: {json.dumps(metrics, indent=2)[:3000]}')\n        print()\n\" 2>&1 | head -500\n",
    "description": "Extract key experiment data from registry",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T13:46:31.794353+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 15, in &lt;module>
    eid = exp.get('exp_id', '')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T13:46:31.794476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\n# Check structure\nif isinstance(result, dict):\n    for k in result.keys():\n        v = result[k]\n        if isinstance(v, list):\n            print(f'key={k}, type=list, len={len(v)}, first_type={type(v[0]).__name__ if v else \\\"empty\\\"}')\n            if v and isinstance(v[0], dict):\n                print(f'  first keys: {list(v[0].keys())[:10]}')\n        elif isinstance(v, dict):\n            print(f'key={k}, type=dict, keys={list(v.keys())[:5]}')\n            for sk, sv in list(v.items())[:2]:\n                print(f'  {sk}: type={type(sv).__name__}')\n                if isinstance(sv, dict):\n                    print(f'    keys: {list(sv.keys())[:10]}')\n        else:\n            print(f'key={k}, type={type(v).__name__}, val={str(v)[:100]}')\n\" 2>&1\n",
  "description": "Check registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\n# Check structure\nif isinstance(result, dict):\n    for k in result.keys():\n        v = result[k]\n        if isinstance(v, list):\n            print(f'key={k}, type=list, len={len(v)}, first_type={type(v[0]).__name__ if v else \\\"empty\\\"}')\n            if v and isinstance(v[0], dict):\n                print(f'  first keys: {list(v[0].keys())[:10]}')\n        elif isinstance(v, dict):\n            print(f'key={k}, type=dict, keys={list(v.keys())[:5]}')\n            for sk, sv in list(v.items())[:2]:\n                print(f'  {sk}: type={type(sv).__name__}')\n                if isinstance(sv, dict):\n                    print(f'    keys: {list(sv.keys())[:10]}')\n        else:\n            print(f'key={k}, type={type(v).__name__}, val={str(v)[:100]}')\n\" 2>&1\n",
    "description": "Check registry data structure"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T13:46:31.794602+00:00_

key=success, type=bool, val=True
key=data, type=dict, keys=['experiments', 'count', 'total', 'baseline']
  experiments: type=dict
    keys: ['exp_qwen25_72b_zeroshot', 'exp_qwen25_14b_fewnerd', 'exp_qwen25_32b_fewnerd', 'exp_qwen25_7b_fewnerd', 'exp_wnut17_qwen25_7b', 'exp_llama_fewnerd_inference', 'exp_entity_construction', 'exp_lp_alignment_gating', 'exp_selective_prediction', 'exp_llama_fewnerd_lora']
  count: type=int
key=error, type=NoneType, val=None
key=metadata, type=dict, keys=['elapsed_seconds']
  elapsed_seconds: type=float

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T13:46:31.794721+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint('All experiment IDs:')\nfor eid in exps.keys():\n    print(f'  {eid}')\nprint(f'\\nTotal: {len(exps)}')\n\" 2>&1\n",
  "description": "List all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint('All experiment IDs:')\nfor eid in exps.keys():\n    print(f'  {eid}')\nprint(f'\\nTotal: {len(exps)}')\n\" 2>&1\n",
    "description": "List all experiment IDs"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T13:46:31.794868+00:00_

All experiment IDs:
  exp_qwen25_72b_zeroshot
  exp_qwen25_14b_fewnerd
  exp_qwen25_32b_fewnerd
  exp_qwen25_7b_fewnerd
  exp_wnut17_qwen25_7b
  exp_llama_fewnerd_inference
  exp_entity_construction
  exp_lp_alignment_gating
  exp_selective_prediction
  exp_llama_fewnerd_lora
  hidden_state_probe_conll_full
  hidden_state_probe_conll_v2
  exp_031_fewnerd_t12
  exp_030_conll_t12
  mbr_pilot
  dgs_pilot
  exp_fewnerd_s789_n8
  exp_026_t12_seed456
  exp_026_t12_seed123
  exp_026_t10_seed456
  exp_026_t10_seed123
  exp_026_t10_seed42
  exp_026_t08_seed456
  exp_026_t08_seed123
  exp_026_t05_seed456
  exp_026_t05_seed123
  exp_029b
  exp_029a
  exp_021_fewnerd_n8_seed456
  exp_021_fewnerd_n8_seed123
  exp_002_conll_n16_seed456
  exp_002_conll_n16_seed123
  exp_017_llama_conll_n16_s456_r1024
  exp_017_llama_conll_n16_r1024
  exp_018_llama_scierc_seed456_r1024
  exp_018_llama_scierc_seed42_r1024
  exp_002_conll_n16
  exp_012_rerun_1024
  exp_llama_scierc_seed456
  exp_007_llama_scierc_seed123
  exp_qwen3_4b_conll_scs_inference
  exp_qwen3_4b_conll_scs_inference_v2
  exp_qwen3_4b_scierc_scs_inference
  exp_027_fewnerd_n16
  exp_026_t12
  exp_026_t08
  exp_026_t05
  exp_026_T12
  exp_026_T08
  exp_026_T05
  exp_017_llama_conll_n16_s123_r1024
  exp_018_llama_scierc_seed123
  exp_018_qwen_scierc_seed456
  exp_018_qwen_scierc_seed123
  exp_epoch_dgs_analysis
  exp_diagnostic_calibration
  exp_adaptive_temperature
  exp_entity_consensus
  exp_ccs_selection
  exp_017_llama_conll
  exp_017_llama_conll_finetune
  exp_028_entity_token_lp
  exp_026_t12_scierc
  exp_026_t08_scierc
  exp_026_t05_scierc
  exp_027_mlp_verifier
  exp_028_fewnerd_5epoch
  exp_028
  exp_024_claim_audit
  exp_016_rerun_1024_bootstrap
  exp_verbalized_confidence
  exp_entity_token_lp
  exp_freeform_ablation
  exp_008_re_n16
  exp_001_ner_n16_seed123
  exp_007_ner_multi_model
  exp_003_ner_wnut17
  exp_001_seed456_t10_full
  exp_001_seed123_t10_full
  exp_008_re_n16_t10_full
  exp_007_llama_inference
  exp_003
…[truncated 2120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T13:46:31.795028+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\ntargets = [\n    'exp_012_rerun_1024', 'exp_016_rerun_1024_bootstrap', 'exp_016_signal_ensemble',\n    'exp_021_fewnerd_full', 'exp_023_lora_rank8', 'exp_entity_construction',\n    'exp_qwen25_72b_zeroshot', 'exp_freeform_ablation',\n    'exp_001_ner_n16_scierc', 'exp_012_logprob_baseline',\n    'exp_qwen3_4b_scierc_scs_inference', 'exp_qwen3_4b_conll_scs_inference_v2',\n    'exp_llama_fewnerd_inference', 'exp_selective_prediction',\n    'exp_lp_alignment_gating'\n]\nfor t in targets:\n    if t in exps:\n        e = exps[t]\n        print(f'=== {t} ===')\n        print(f'status: {e.get(\\\"status\\\",\\\"?\\\")}')\n        conc = e.get('conclusion','')\n        if conc:\n            print(f'conclusion: {conc[:500]}')\n        m = e.get('metrics', {})\n        if m:\n            ms = json.dumps(m, indent=2)\n            print(f'metrics: {ms[:2000]}')\n        print()\n\" 2>&1 | head -800\n",
  "description": "Extract metrics from key experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\ntargets = [\n    'exp_012_rerun_1024', 'exp_016_rerun_1024_bootstrap', 'exp_016_signal_ensemble',\n    'exp_021_fewnerd_full', 'exp_023_lora_rank8', 'exp_entity_construction',\n    'exp_qwen25_72b_zeroshot', 'exp_freeform_ablation',\n    'exp_001_ner_n16_scierc', 'exp_012_logprob_baseline',\n    'exp_qwen3_4b_scierc_scs_inference', 'exp_qwen3_4b_conll_scs_inference_v2',\n    'exp_llama_fewnerd_inference', 'exp_selective_prediction',\n    'exp_lp_alignment_gating'\n]\nfor t in targets:\n    if t in exps:\n        e = exps[t]\n        print(f'=== {t} ===')\n        print(f'status: {e.get(\\\"status\\\",\\\"?\\\")}')\n        conc = e.get('conclusion','')\n        if conc:\n            print(f'conclusion: {conc[:500]}')\n        m = e.get('metrics', {})\n        if m:\n            ms = json.dumps(m, indent=2)\n            print(f'metrics: {ms[:2000]}')\n        print()\n\" 2>&1 | head -800\n",
    "description": "Extract metrics from key experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T13:46:31.795305+00:00_

=== exp_012_rerun_1024 ===
status: DONE
conclusion: success
metrics: {
  "degen_rate": 0.1777,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
  "ner_full": {
    "n": 529,
    "SJ": {
      "rho": 0.3599,
      "tau": 0.2646,
      "AUROC": 0.6917,
      "ECE": 0.4531,
      "rho_ci95": [
        0.2732,
        0.4389
      ],
      "AUROC_ci95": [
        0.6304,
        0.7406
      ]
    },
    "FK": {
      "rho": 0.2665,
      "tau": 0.1974,
      "AUROC": 0.629,
      "ECE": 0.4512,
      "rho_ci95": [
        0.1743,
        0.3486
      ],
      "AUROC_ci95": [
        0.5612,
        0.6882
      ]
    },
    "logprob": {
      "rho": 0.2052,
      "tau": 0.1478,
      "AUROC": 0.5783,
      "ECE": 0.7064,
      "rho_ci95": [
        0.1171,
        0.2904
      ],
      "AUROC_ci95": [
        0.5179,
        0.6387
      ]
    },
    "EM": {
      "rho": 0.2945,
      "tau": 0.2208,
      "AUROC": 0.7493,
      "ECE": 0.3526,
      "rho_ci95": [
        0.2094,
        0.37
      ],
      "AUROC_ci95": [
        0.7002,
        0.7928
      ]
    },
    "voting_conf": {
      "rho": 0.3792,
      "tau": 0.2805,
      "AUROC": 0.6841,
      "ECE": 0.3807,
      "rho_ci95": [
        0.2972,
        0.4486
      ],
      "AUROC_ci95": [
        0.6249,
        0.7366
      ]
    }
  },
  "ner_cond": {
    "n": 477,
    "SJ": {
      "rho": 0.3113,
      "tau": 0.2257,
      "AUROC": 0.6772,
      "ECE": 0.4416,
      "rho_ci95": [
        0.2353,
        0.3959
      ],
      "AUROC_ci95": [
        0.621,
        0.7337
      ]
    },
    "FK": {
      "rho": 0.1761,
      "tau": 0.1284,
      "AUROC": 0.6078,
      "ECE": 0.4389,
      "rho_ci95": [
        0.0839,
        0.2665
      ],
      "AUROC_ci95": [
        0.5442,
        0.6709
      ]
    },
    "logprob": {
      "rho": 0.1538,
      "tau": 0.1111,
      "AUROC": 0.5633,
      "ECE": 0.6803,
      "rho_ci95": [
        0.0637,
        0.2424
      ],
      "AUROC_ci95"
…[truncated 10108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T13:46:31.795480+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\ntargets = [\n    'exp_qwen25_72b_zeroshot', 'exp_018_llama_scierc_seed42_r1024',\n    'exp_018_llama_scierc_seed456_r1024', 'exp_018_llama_scierc_seed123',\n    'exp_017_llama_conll_n16_r1024', 'exp_017_llama_conll_n16_s456_r1024',\n    'exp_002_conll_n16_r1024', 'exp_002_conll_n16',\n    'exp_006_v2', 'exp_001_seed42_v2_r1024',\n    'exp_021_fewnerd_n8_seed456', 'exp_021_fewnerd_n8_seed123',\n    'exp_fewnerd_s789_n8', 'exp_003_wnut17_v2',\n    'exp_wnut17_qwen25_7b'\n]\nfor t in targets:\n    if t in exps:\n        e = exps[t]\n        print(f'=== {t} ===')\n        print(f'status: {e.get(\\\"status\\\",\\\"?\\\")}')\n        m = e.get('metrics', {})\n        if m:\n            ms = json.dumps(m, indent=2)\n            print(f'metrics: {ms[:2000]}')\n        print()\n    else:\n        print(f'=== {t} === NOT FOUND')\n        print()\n\" 2>&1 | head -600\n",
  "description": "Extract more experiment data",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\ntargets = [\n    'exp_qwen25_72b_zeroshot', 'exp_018_llama_scierc_seed42_r1024',\n    'exp_018_llama_scierc_seed456_r1024', 'exp_018_llama_scierc_seed123',\n    'exp_017_llama_conll_n16_r1024', 'exp_017_llama_conll_n16_s456_r1024',\n    'exp_002_conll_n16_r1024', 'exp_002_conll_n16',\n    'exp_006_v2', 'exp_001_seed42_v2_r1024',\n    'exp_021_fewnerd_n8_seed456', 'exp_021_fewnerd_n8_seed123',\n    'exp_fewnerd_s789_n8', 'exp_003_wnut17_v2',\n    'exp_wnut17_qwen25_7b'\n]\nfor t in targets:\n    if t in exps:\n        e = exps[t]\n        print(f'=== {t} ===')\n        print(f'status: {e.get(\\\"status\\\",\\\"?\\\")}')\n        m = e.get('metrics', {})\n        if m:\n            ms = json.dumps(m, indent=2)\n            print(f'metrics: {ms[:2000]}')\n        print()\n    else:\n        print(f'=== {t} === NOT FOUND')\n        print()\n\" 2>&1 | head -600\n",
    "description": "Extract more experiment data",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T13:46:31.795718+00:00_

=== exp_qwen25_72b_zeroshot ===
status: RUNNING

=== exp_018_llama_scierc_seed42_r1024 ===
status: DONE
metrics: {
  "degen_rate": 0.2495,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
  "ner": {
    "full": {
      "SJ": {
        "rho": 0.3096,
        "tau": 0.2288,
        "auroc": 0.6683
      },
      "FK": {
        "rho": 0.2352,
        "tau": 0.1759,
        "auroc": 0.6069
      },
      "logprob": {
        "rho": 0.1503,
        "tau": 0.1087,
        "auroc": 0.5318
      },
      "EM": {
        "rho": 0.2587,
        "tau": 0.1966,
        "auroc": 0.7174
      },
      "voting_conf": {
        "rho": 0.4053,
        "tau": 0.3042,
        "auroc": 0.6967
      }
    },
    "conditional": {
      "SJ": {
        "rho": 0.2718,
        "tau": null,
        "auroc": 0.6565
      },
      "FK": {
        "rho": 0.1472,
        "tau": null,
        "auroc": 0.5866
      },
      "logprob": {
        "rho": 0.081,
        "tau": null,
        "auroc": 0.5129
      },
      "EM": {
        "rho": 0.3165,
        "tau": null,
        "auroc": 0.7244
      },
      "voting_conf": {
        "rho": 0.3078,
        "tau": null,
        "auroc": 0.6714
      }
    },
    "greedy_f1": 0.6607,
    "oracle_f1": 0.7781,
    "n_full": 529,
    "n_cond": 478
  },
  "re": {
    "full": {
      "SJ": {
        "rho": 0.2748,
        "tau": 0.2102,
        "auroc": 0.7244
      },
      "FK": {
        "rho": 0.3027,
        "tau": 0.2337,
        "auroc": 0.691
      },
      "logprob": {
        "rho": 0.3163,
        "tau": 0.233,
        "auroc": 0.6313
      },
      "EM": {
        "rho": 0.1681,
        "tau": 0.1275,
        "auroc": 0.7697
      },
      "voting_conf": {
        "rho": 0.384,
        "tau": 0.2965,
        "auroc": 0.7337
      }
    },
    "conditional": {
      "SJ": {
        "rho": 0.3461,
        "tau": null,
        "auroc": 0.7233
      },
      "FK": {
        "rho": 0.1969,
        "tau": null,
        "auroc": 0.6
…[truncated 6717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T13:46:31.795897+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Get the full 72B data\ne72b = exps.get('exp_qwen25_72b_zeroshot', {})\nprint('=== 72B zeroshot ===')\nprint(json.dumps(e72b, indent=2)[:4000])\n\" 2>&1\n",
  "description": "Extract 72B zeroshot experiment data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Get the full 72B data\ne72b = exps.get('exp_qwen25_72b_zeroshot', {})\nprint('=== 72B zeroshot ===')\nprint(json.dumps(e72b, indent=2)[:4000])\n\" 2>&1\n",
    "description": "Extract 72B zeroshot experiment data"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T13:46:31.796045+00:00_

=== 72B zeroshot ===
{
  "status": "RUNNING",
  "retry_count": 1,
  "created_at": "2026-05-19T06:19:28.597Z",
  "updated_at": "2026-05-19T12:48:36.347Z",
  "hypothesis": "A larger zero-shot model (72B) will show higher greedy F1 and wider oracle-greedy gap than fine-tuned smaller models, because increased capacity enables more diverse valid extractions per stochastic sample, making self-consistency signals (SJ, FK, VC, EM) more informative for quality estimation.",
  "server": "autodl-5090-b",
  "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
  "account": "root",
  "reproduce": {
    "server": "autodl-5090-b",
    "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
    "started_at": "2026-05-19T06:47:42.658Z"
  },
  "notes": "2026-05-19 12:47 UTC: RECOVERED from false-positive startup recovery failure. 289848/301184 prompts (96.2%). SciERC \u2705 (551) CoNLL \u2705 (3453) FewNERD ~96%. ETA ~10-15min. PID 59040, 4\u00d75090 100% util. Cron registered.",
  "failure_reason": "startup recovery: RUNNING with no cron and no server/pid info",
  "completed_at": "2026-05-19T12:44:26.198Z",
  "extra": {
    "previous_failure": {
      "conclusion": "failed",
      "notes": "2026-05-19 11:36 UTC: 69.8% complete (210352/301184 prompts). SciERC \u2705 CoNLL \u2705 FewNERD ~66%. ETA ~1h15m. vLLM PID 59040, 4\u00d75090 100% util."
    }
  },
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=0,1,2,3 python code/zeroshot_inference_72b.py --datasets scierc conll2003 fewnerd --output-dir output/72b_zeroshot --seed 42",
    "server": "autodl-5090-b",
    "data_path": "data/{scierc,conll2003,fewnerd}",
    "data_count": 41630,
    "model_name": "Qwen2.5-72B-Instruct-AWQ",
    "seed": 42,
    "gpu_ids": [
      "cuda:0",
      "cuda:1",
      "cuda:2",
      "cuda:3"
    ],
    "pid": 59040
  }
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T13:46:31.796230+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/72b*/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/72b*/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T13:46:31.796354+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T13:46:31.796471+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Look for multi-seed entity construction and selection data\ntargets = ['exp_entity_construction', 'exp_026_t12', 'exp_026_t12_scierc',\n           'exp_016_rerun_1024', 'exp_002_conll_n16_r1024',\n           'exp_003_wnut17_v2', 'exp_003_ner_wnut17']\nfor t in targets:\n    if t in exps:\n        e = exps[t]\n        print(f'=== {t} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:3000])\n        print()\n\" 2>&1 | head -400\n",
  "description": "Extract entity construction and WNUT metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Look for multi-seed entity construction and selection data\ntargets = ['exp_entity_construction', 'exp_026_t12', 'exp_026_t12_scierc',\n           'exp_016_rerun_1024', 'exp_002_conll_n16_r1024',\n           'exp_003_wnut17_v2', 'exp_003_ner_wnut17']\nfor t in targets:\n    if t in exps:\n        e = exps[t]\n        print(f'=== {t} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:3000])\n        print()\n\" 2>&1 | head -400\n",
    "description": "Extract entity construction and WNUT metrics"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T13:46:31.796616+00:00_

=== exp_entity_construction ===
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
  "note": "5-fold CV, bootstrap B=10000, paired one-sided"
}

=== exp_026_t12 ===
{
  "temperature": 1.2,
  "task": "T-ablation",
  "degen_rate": 0.1493,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"
}

=== exp_026_t12_scierc ===
{}

=== exp_002_conll_n16_r1024 ===
{}

=== exp_003_wnut17_v2 ===
{}

=== exp_003_ner_wnut17 ===
{
  "ner": {
    "greedy_f1": 0.525,
    "oracle_f1": 0.664,
    "headroom": 0.139,
    "rho_sj_full": 0.082,
    "rho_fk_full": 0.124,
    "rho_logprob_full": -0.414,
    "rho_sj_cond": 0.275,
    "rho_fk_cond": 0.164,
    "rho_logprob_cond": 0.352,
    "sj_beats_logprob_cond": false
  },
  "n_instances": 1287,
  "n_gold_empty": 598,
  "sample_f1_mean": 0.401,
  "sample_f1_pct_zero": 53.7,
  "N": 16,
  "T": 1,
  "seed": 42,
  "verdict": "FAIL",
  "verdict_note": ">30% samples F1=0; structural rho weak; logprob baseline stronger"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T13:46:31.796791+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get full exp_016_rerun_1024 with all selection data\ne = exps.get('exp_016_rerun_1024', {})\nprint('=== exp_016_rerun_1024 FULL ===')\nprint(json.dumps(e, indent=2)[:5000])\n\" 2>&1\n",
  "description": "Get full selection data from exp_016"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get full exp_016_rerun_1024 with all selection data\ne = exps.get('exp_016_rerun_1024', {})\nprint('=== exp_016_rerun_1024 FULL ===')\nprint(json.dumps(e, indent=2)[:5000])\n\" 2>&1\n",
    "description": "Get full selection data from exp_016"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T13:46:31.796923+00:00_

=== exp_016_rerun_1024 FULL ===
{}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T13:46:31.797042+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get multi-seed SciERC selection data\nfor eid in ['exp_018_qwen_scierc_seed456', 'exp_018_qwen_scierc_seed123', 'exp_001_seed456_v2_ner_r1024', 'exp_001_seed123_v2_r1024']:\n    e = exps.get(eid, {})\n    if e:\n        print(f'=== {eid} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:1500])\n        print()\n\" 2>&1\n",
  "description": "Get multi-seed SciERC QE data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get multi-seed SciERC selection data\nfor eid in ['exp_018_qwen_scierc_seed456', 'exp_018_qwen_scierc_seed123', 'exp_001_seed456_v2_ner_r1024', 'exp_001_seed123_v2_r1024']:\n    e = exps.get(eid, {})\n    if e:\n        print(f'=== {eid} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:1500])\n        print()\n\" 2>&1\n",
    "description": "Get multi-seed SciERC QE data"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T13:46:31.797195+00:00_

=== exp_018_qwen_scierc_seed456 ===
{
  "degen_rate": 0.2042,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"
}

=== exp_018_qwen_scierc_seed123 ===
{
  "degen_rate": 0.172,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"
}

=== exp_001_seed456_v2_ner_r1024 ===
{}

=== exp_001_seed123_v2_r1024 ===
{}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T13:46:31.797322+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get exp_002_conll_n16_r1024 and look for CoNLL N=8 data\nfor eid in ['exp_002_conll_n16_r1024', 'exp_002_conll_n16_seed456', 'exp_002_conll_n16_seed123', \n            'exp_002_conll_n16_seed456', 'exp_002_conll_n16_seed123']:\n    e = exps.get(eid, {})\n    if e:\n        print(f'=== {eid} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:1500])\n        print()\n        \n# Also check the hidden_state_probe experiments\nfor eid in ['hidden_state_probe_conll_full', 'hidden_state_probe_conll_v2']:\n    e = exps.get(eid, {})\n    if e:\n        print(f'=== {eid} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:1500])\n        print()\n\" 2>&1\n",
  "description": "Get CoNLL and hidden probe data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get exp_002_conll_n16_r1024 and look for CoNLL N=8 data\nfor eid in ['exp_002_conll_n16_r1024', 'exp_002_conll_n16_seed456', 'exp_002_conll_n16_seed123', \n            'exp_002_conll_n16_seed456', 'exp_002_conll_n16_seed123']:\n    e = exps.get(eid, {})\n    if e:\n        print(f'=== {eid} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:1500])\n        print()\n        \n# Also check the hidden_state_probe experiments\nfor eid in ['hidden_state_probe_conll_full', 'hidden_state_probe_conll_v2']:\n    e = exps.get(eid, {})\n    if e:\n        print(f'=== {eid} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:1500])\n        print()\n\" 2>&1\n",
    "description": "Get CoNLL and hidden probe data"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T13:46:31.797461+00:00_

=== exp_002_conll_n16_r1024 ===
{}

=== exp_002_conll_n16_seed456 ===
{
  "degen_rate": 0.5544,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
  "instance_count": 3453,
  "n_valid": 2756,
  "n_gold_empty": 697,
  "ner_greedy_f1": 0.9074,
  "ner_oracle_f1": 0.9549,
  "rho_fk_ner": 0.4718,
  "rho_sj_ner": 0.4819,
  "sample_f1_pct_zero": 7.02
}

=== exp_002_conll_n16_seed123 ===
{
  "degen_rate": 0.471,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
  "instance_count": 3453,
  "n_valid": 2756,
  "n_gold_empty": 697,
  "ner_greedy_f1": 0.9068,
  "ner_oracle_f1": 0.9633,
  "rho_fk_ner": 0.4524,
  "rho_sj_ner": 0.4621,
  "sample_f1_pct_zero": 7.54
}

=== exp_002_conll_n16_seed456 ===
{
  "degen_rate": 0.5544,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
  "instance_count": 3453,
  "n_valid": 2756,
  "n_gold_empty": 697,
  "ner_greedy_f1": 0.9074,
  "ner_oracle_f1": 0.9549,
  "rho_fk_ner": 0.4718,
  "rho_sj_ner": 0.4819,
  "sample_f1_pct_zero": 7.02
}

=== exp_002_conll_n16_seed123 ===
{
  "degen_rate": 0.471,
  "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
  "instance_count": 3453,
  "n_valid": 2756,
  "n_gold_empty": 697,
  "ner_greedy_f1": 0.9068,
  "ner_oracle_f1": 0.9633,
  "rho_fk_ner": 0.4524,
  "rho_sj_ner": 0.4621,
  "sample_f1_pct_zero": 7.54
}

=== hidden_state_probe_conll_full ===
{}

=== hidden_state_probe_conll_v2 ===
{}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T13:46:31.797628+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# WNUT LP rho\ne = exps.get('exp_003_ner_wnut17', {})\nprint('=== WNUT-17 (exp_003) ===')\nm = e.get('metrics', {})\nprint(f'LP full rho: {m.get(\\\"ner\\\",{}).get(\\\"rho_logprob_full\\\", \\\"?\\\")}')\nprint(f'LP cond rho: {m.get(\\\"ner\\\",{}).get(\\\"rho_logprob_cond\\\", \\\"?\\\")}')\nprint()\n\n# Get CoNLL QE N=8 data\nfor eid in ['exp_002', 'exp_002_ner_conll2003']:\n    e = exps.get(eid, {})\n    if e and e.get('metrics'):\n        print(f'=== {eid} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:2000])\n        print()\n\n# Also look for WNUT QE table data  \nfor eid in ['exp_003_wnut17_eval']:\n    e = exps.get(eid, {})\n    if e and e.get('metrics'):\n        print(f'=== {eid} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:2000])\n        print()\n\" 2>&1\n",
  "description": "Get WNUT and CoNLL QE baseline data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# WNUT LP rho\ne = exps.get('exp_003_ner_wnut17', {})\nprint('=== WNUT-17 (exp_003) ===')\nm = e.get('metrics', {})\nprint(f'LP full rho: {m.get(\\\"ner\\\",{}).get(\\\"rho_logprob_full\\\", \\\"?\\\")}')\nprint(f'LP cond rho: {m.get(\\\"ner\\\",{}).get(\\\"rho_logprob_cond\\\", \\\"?\\\")}')\nprint()\n\n# Get CoNLL QE N=8 data\nfor eid in ['exp_002', 'exp_002_ner_conll2003']:\n    e = exps.get(eid, {})\n    if e and e.get('metrics'):\n        print(f'=== {eid} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:2000])\n        print()\n\n# Also look for WNUT QE table data  \nfor eid in ['exp_003_wnut17_eval']:\n    e = exps.get(eid, {})\n    if e and e.get('metrics'):\n        print(f'=== {eid} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:2000])\n        print()\n\" 2>&1\n",
    "description": "Get WNUT and CoNLL QE baseline data"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T13:46:31.797774+00:00_

=== WNUT-17 (exp_003) ===
LP full rho: -0.414
LP cond rho: 0.352

=== exp_002 ===
{
  "sj_rho_full": 0.4357,
  "sj_tau_full": 0.3851,
  "sj_auroc_full": 0.8008,
  "sj_rho_cond": 0.4511,
  "fk_rho_full": 0.3998,
  "fk_tau_full": 0.3568,
  "fk_auroc_full": 0.7741,
  "fk_rho_cond": 0.4064,
  "logprob_rho_full": 0.3157,
  "logprob_tau_full": 0.2469,
  "logprob_auroc_full": 0.7532,
  "logprob_rho_cond": 0.3562,
  "em_rho_full": 0.4507,
  "em_tau_full": 0.4002,
  "em_auroc_full": 0.8156,
  "em_rho_cond": 0.4799,
  "ev_rho_full": 0.4237,
  "ev_tau_full": 0.3777,
  "ev_auroc_full": 0.7889,
  "ev_rho_cond": 0.4127,
  "greedy_f1": 0.9123,
  "oracle_f1": 0.9543,
  "voting_f1": 0.9141,
  "oracle_headroom": 0.042,
  "sj_vs_logprob_delta_rho": 0.12,
  "sj_vs_logprob_ci_low": 0.0881,
  "sj_vs_logprob_ci_high": 0.154,
  "sj_vs_logprob_significant": true,
  "n_instances": 3453,
  "n_valid": 2756,
  "n_samples": 8,
  "temperature": 1
}

=== exp_003_wnut17_eval ===
{
  "greedy_f1": 0.523,
  "oracle_f1": 0.664,
  "headroom": 0.141,
  "rho_fk": 0.125,
  "rho_sj": 0.089,
  "rho_fk_cond": 0.169,
  "rho_sj_cond": 0.288,
  "rho_logprob_full": -0.409,
  "rho_logprob_cond": 0.35,
  "structural_beats_surface": false,
  "sample_f1_pct_zero": 53.7,
  "n_instances": 1287,
  "N": 16,
  "T": 1,
  "seed": 42,
  "model": "Qwen3-8B",
  "n_gold_empty_filtered": 598,
  "verdict": "FAIL",
  "verdict_note": "structural_beats_surface=false; >50% samples F1=0"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T13:46:31.797910+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Find selection experiments with 2-seed means for SciERC (paper Table 2)\n# exp_016_rerun_1024 seems empty - check related experiments\nfor eid in ['exp_016_v2', 'exp_015_v2', 'exp_010_selection_curves']:\n    e = exps.get(eid, {})\n    if e and e.get('metrics'):\n        print(f'=== {eid} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:2000])\n        print()\n\" 2>&1\n",
  "description": "Get selection experiment data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/e21c3add-633d-4663-b1eb-e2854d1b8be8/tool-results/mcp-agent-ml-research-read_registry-1779197616177.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Find selection experiments with 2-seed means for SciERC (paper Table 2)\n# exp_016_rerun_1024 seems empty - check related experiments\nfor eid in ['exp_016_v2', 'exp_015_v2', 'exp_010_selection_curves']:\n    e = exps.get(eid, {})\n    if e and e.get('metrics'):\n        print(f'=== {eid} ===')\n        ms = json.dumps(e.get('metrics', {}), indent=2)\n        print(ms[:2000])\n        print()\n\" 2>&1\n",
    "description": "Get selection experiment data"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T13:46:31.798070+00:00_

=== exp_016_v2 ===
{
  "ner_conditional": {
    "n": 529,
    "best_single_signal_rho": {
      "soft_jaccard": 0.4412
    },
    "best_combo_rho": {
      "sj+vc_a0.55": 0.4552
    },
    "ensemble_auroc": 0.7141,
    "best_single_auroc": {
      "soft_jaccard": 0.7166
    },
    "selection_f1": {
      "greedy": 0.6442,
      "logprob_best": 0.6505,
      "ensemble_best": 0.6475,
      "sj_best": 0.6471,
      "oracle": 0.8442
    }
  },
  "re_conditional": {
    "n": 397,
    "best_single_signal_rho": {
      "voting_confidence": 0.3849
    },
    "best_combo_rho": {
      "logprob+vc_a0.25": 0.3936
    },
    "ensemble_auroc": 0.6916,
    "best_single_auroc": {
      "voting_confidence": 0.7023
    },
    "selection_f1": {
      "greedy": 0.403,
      "logprob_best": 0.4097,
      "ensemble_best": 0.4227,
      "oracle": 0.6306
    }
  },
  "re_full": {
    "ensemble_auroc": 0.8608,
    "best_single_auroc": {
      "voting_confidence": 0.8248
    }
  }
}

=== exp_015_v2 ===
{
  "scierc_ner_avg": {
    "sj_auroc": 0.7394,
    "fk_auroc": 0.6172,
    "em_auroc": 0.7873,
    "voting_auroc": 0.7367,
    "logprob_auroc": 0.5918
  },
  "scierc_re_avg": {
    "sj_auroc": 0.6746,
    "fk_auroc": 0.5939,
    "em_auroc": 0.715,
    "voting_auroc": 0.7234,
    "logprob_auroc": 0.5849
  }
}

=== exp_010_selection_curves ===
{
  "scierc_ner": {
    "n_instances": 551,
    "greedy_f1": 0.618,
    "N16": {
      "oracle": 0.787,
      "SJ": 0.62,
      "FK": 0.621,
      "logprob": 0.621,
      "voting_conf": 0.585,
      "EM": 0.606,
      "random": 0.595
    },
    "N8": {
      "oracle": 0.752,
      "SJ": 0.614,
      "FK": 0.614,
      "logprob": 0.619,
      "voting_conf": 0.591,
      "EM": 0.603,
      "random": 0.589
    },
    "N4": {
      "oracle": 0.714,
      "SJ": 0.607,
      "FK": 0.608,
      "logprob": 0.616,
      "voting_conf": 0.594,
      "EM": 0.6,
      "random": 0.587
    }
  },
  "scierc_re": {
    "n_instances": 397,
    "greedy_f1": 0.403,
    "N16
…[truncated 757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T13:46:31.798263+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T13:46:31.798483+00:00_

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
…[truncated 13587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T13:46:31.798817+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.1.*pp|0\\.4.*pp|\\+0\\.1|\\+0\\.4",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.1.*pp|0\\.4.*pp|\\+0\\.1|\\+0\\.4",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T13:46:31.798960+00:00_

5:Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP selection yields $+2.9$~pp ($p{=}0.004$; Table~\ref{tab:nontied_main}), but $\varepsilon{=}0.05$ is post-hoc ($p_{\text{adj}}{=}0.14$ after joint correction; Appendix~\ref{app:epsilon_robustness}), so this is exploratory evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T13:46:31.799084+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.1.*pp|0\\.4.*pp|\\+0\\.1|\\+0\\.4|single.sample|over greedy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.1.*pp|0\\.4.*pp|\\+0\\.1|\\+0\\.4|single.sample|over greedy",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T13:46:31.799227+00:00_

3:Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
12:Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
16:Our selection experiments use 3 training seeds for Few-NERD and CoNLL (stability $\sigma{\leq}0.04$~pp for LP selection); these confirm robustness on the key positive and negative datasets. SciERC uses 1 primary seed with high seed sensitivity ($\sigma{=}0.48$~pp, $n{=}529$), which reflects limited within-seed statistical power.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T13:46:31.799356+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.724|0\\.730|WNUT.*VC|VC.*WNUT",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.724|0\\.730|WNUT.*VC|VC.*WNUT",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T13:46:31.799478+00:00_

docs/paper/sections/experiments.tex:48:At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
docs/paper/sections/experiments.tex:104:Yet QE remains effective on WNUT-17 (VC $\rho{=}0.730$; Table~\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.
docs/paper/sections/appendix.tex:226:VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\rho{=}0.350$ is the highest among all signals on the non-zero subset, full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T13:46:31.799597+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "87\\\\\\\\%|87\\%|87.*degen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "tool_args": {
    "pattern": "87\\\\\\\\%|87\\%|87.*degen",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T13:46:31.799714+00:00_

docs/paper/sections/introduction.tex:15:Three factors qualitatively shape this gap: (a)~\textit{instance degeneracy} (13\textendash 87\% across our benchmarks) compresses the candidate space; (b)~\textit{oracle headroom} bounds the achievable gain; (c)~\textit{LP-quality alignment} (within-instance $\rho(\text{LP}, \text{F1})$) determines whether LP can discriminate candidates in non-degenerate instances (\S\ref{sec:selection_gap}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-19T13:46:31.799860+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "single.sample|\\+0\\.1[^0-9]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "tool_args": {
    "pattern": "single.sample|\\+0\\.1[^0-9]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T13:46:31.800024+00:00_

docs/paper/main.log:914:\T1/ptm/m/n/10.95 (+20) single-sample ($\OT1/cmr/m/n/10.95 +2\OML/cmm/m/it/10.9
docs/paper/sections/experiments.tex:47:On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
docs/paper/sections/experiments.tex:246:[Omitted long matching line]
docs/paper/sections/appendix.tex:230:On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
docs/paper/sections/appendix.tex:232:On CoNLL, 48--87\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
docs/paper/sections/appendix.tex:264:VC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
docs/paper/sections/appendix.tex:320:On CoNLL, diversity collapses: 59\% (Qwen) to 89\% (LLaMA) of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect where single-sample F1 already exceeds 0.90.
docs/paper/sections/appendix.tex:342:[Omitted long matching line]
docs/paper/sections/appendix.tex:346:On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP, the only per-sample signal, achieves merely $+$0.8~pp.
docs/paper/sections/appendix.tex:347:LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~p
…[truncated 8820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T13:46:31.800189+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "over greedy|\\+0\\.4[^0-9]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "tool_args": {
    "pattern": "over greedy|\\+0\\.4[^0-9]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T13:46:31.800322+00:00_

docs/paper/sections/experiments.tex:93:Instance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\ref{tab:selection}; Figure~\ref{fig:selection_gap}).
docs/paper/sections/experiments.tex:102:[Omitted long matching line]
docs/paper/sections/experiments.tex:246:[Omitted long matching line]
docs/paper/sections/limitations.tex:3:Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
docs/paper/sections/limitations.tex:12:Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
docs/paper/main.aux:2971:[Omitted long matching line]
docs/paper/main.aux:2972:[Omitted long matching line]
docs/paper/sections/appendix.tex:1065:No signal achieves significant improvement over greedy at $\alpha{=}0.05$ (LP: $p{=}0.091$; FK: $p{=}0.101$), while VC is significantly \textit{worse} ($-4.36$~pp, $p{=}1.0$).
docs/paper/sections/appendix.tex:1418:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T13:46:31.800493+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "tab:wnut|WNUT.*table|wnut.*rho|0\\\\.724|0\\\\.452",
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
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "tool_args": {
    "pattern": "tab:wnut|WNUT.*table|wnut.*rho|0\\\\.724|0\\\\.452",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-19T13:46:31.800617+00:00_

206:Table~\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\rho$.
212:\label{tab:wnut}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-19T13:46:31.800734+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "tab:degeneracy|degeneracy.*table|48.*87",
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
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "tool_args": {
    "pattern": "tab:degeneracy|degeneracy.*table|48.*87",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T13:46:31.800863+00:00_

232:On CoNLL, 48--87\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
351:Table~\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.
357:\label{tab:degeneracy}
1122:This confirms that temperature controls degeneracy but cannot improve LP-quality alignment, which is largely determined by task structure and remains relatively stable across generation configurations (\S\ref{app:epoch_confound}). LP-quality alignment, not degeneracy, is the primary predictor of LP selection direction (\S\ref{sec:discussion}).
1265:\multicolumn{3}{l}{Greedy: 0.748 \quad Oracle: 0.872} & \multicolumn{2}{l}{Headroom: 12.4\,pp} \\
1444:On SciERC, DALS yields $+0.71{\pm}0.48$~pp (3-seed mean; individual seeds: $+0.19$ to $+1.14$~pp); on Few-NERD, $+0.30$~pp ($p{<}0.001$; gain remains positive across $\tau \in [0.01, 0.15]$); on CoNLL, where pure LP selection degrades F1 ($-0.85$~pp), DALS shows comparable degradation (Qwen: $-0.87$~pp; LLaMA: neutral).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-19T13:46:31.800992+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "206",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "206",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-19T13:46:31.801160+00:00_

206	Table~\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\rho$.
207	
208	\begin{table}[t]
209	\centering
210	\small
211	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
212	\label{tab:wnut}
213	\begin{tabular}{lcccc}
214	\toprule
215	Signal & $\rho$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
216	\midrule
217	VC      & .724 & .913 & .038 & .487 \\
218	FK      & .125 & .555 & .169 & .002 \\
219	SJ      & .089 & .517 & .288 & ${<}$1e-7 \\
220	EM      & .050 & .487 & .333 & ${<}$1e-9 \\
221	LP & $-$.410 & .219 & .350 & ${<}$1e-10 \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	The full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.
226	VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\rho{=}0.350$ is the highest among all signals on the non-zero subset, full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
227	
228	\paragraph{Cross-configuration selection analysis.}
229	Table~\ref{tab:cross_selection} extends the selection analysis to five additional configurations.
230	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
231	On LLaMA FewNERD ($n{=}32{,}565$, 3-seed mean), LP is the only signal with positive selection ($+0.36$~pp), confirming LP as the most robust selection signal across model families (Qwen FewNERD: $+1.39$~pp, Table~\ref{tab:fewnerd}).
…[truncated 1635 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-19T13:46:31.801314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "351",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "351",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-19T13:46:31.801460+00:00_

351	Table~\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.
352	
353	\begin{table}[t]
354	\centering
355	\small
356	\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}
357	\label{tab:degeneracy}
358	\begin{tabular}{lccc}
359	\toprule
360	& \shortstack{SciERC 8B\\($N{=}8$)} & \shortstack{SciERC 4B\\($N{=}8$)} & \shortstack{CoNLL 8B\\($N{=}16$)} \\
361	\midrule
362	Constant F1 & 17.8\% & 10.4\% & 48.4\% \\
363	Constant utility & 13\% & 7.0\% & 49\% \\
364	Oracle gap closed (non-deg.) & 23\% & 25.2\% & 41\% \\
365	Within-inst.\ SJ $\rho$ (median) & 0.524 & 0.550 & 0.994 \\
366	\bottomrule
367	\end{tabular}
368	\end{table}
369	
370	\paragraph{TOST equivalence testing.}\label{app:tost}
371	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
372	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\delta$.
373	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
374	These proportions use the same test data that defines the headroom, introducing circularity: $\delta$ is anchored to the very quantity it contextualizes.
375	We address this below with externally anchored equivalence margins.
376	The breakpoint $\delta^*$, the minimum e
…[truncated 1337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-19T13:46:31.801656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "234",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "234",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-19T13:46:31.801809+00:00_

234	\begin{table*}[t]
235	\centering
236	\small
237	\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
238	\label{tab:cross_selection}
239	\begin{tabular}{llccccccc}
240	\toprule
241	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
242	\midrule
243	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
244	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
245	\addlinespace
246	LLaMA/FewNERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \textbf{.788} & .760 \\
247	\addlinespace
248	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .957 & \textbf{.899} & .893 & .898 & .897 & .895 \\
249	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
250	\bottomrule
251	\end{tabular}
252	\end{table*}
253	
254	\paragraph{Diminishing returns of $N$-scaling.}
255	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
256	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
257	Structural signals use $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, each additional comparison yields d
…[truncated 2435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-19T13:46:31.802047+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
  "content": "# Claim Audit Report — struct_self_consist_ie\n\n**Date**: 2026-05-19  \n**Scope**: All quantitative claims in `docs/paper/sections/` cross-verified against experiment registry and paper_framing.md  \n**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.\n\n---\n\n## ❌ Inconsistencies Requiring Fix\n\n### 1. WNUT VC ρ inconsistency within paper (0.724 vs 0.730)\n\n| Location | Value |\n|----------|-------|\n| experiments.tex:48 | VC ρ=0.724 |\n| experiments.tex:104 | VC ρ=0.730 |\n| appendix.tex:217 (tab:wnut) | VC .724 |\n| appendix.tex:226 | VC ρ=0.724 |\n\n**Verdict**: 0.724 is the tabulated value, used 3× consistently. The 0.730 on line 104 is a **typo**.  \n**Fix**: Change experiments.tex:104 from `VC $\\rho{=}0.730$` to `VC $\\rho{=}0.724$`.\n\n### 2. SciERC AUROC in Table 1 vs registry (systematic offset)\n\nPaper Table 1 SciERC AUROC vs registry `exp_012_rerun_1024` (same ρ values, so same data):\n\n| Signal | Paper AUC | Registry AUROC | Δ |\n|--------|-----------|---------------|-----|\n| VC | .663 | .684 | -2.1pp |\n| SJ | .650 | .692 | -4.2pp |\n| FK | .602 | .629 | -2.7pp |\n| EM | .614 | .749 | **-13.5pp** |\n| LP | .578 | .578 | 0pp |\n\nρ values match to 3 decimal places (confirming same source data), but AUROC diverges except for LP. The EM gap (0.614 vs 0.749) is extreme. CoNLL AUROC values match the registry within 1pp.\n\n**Hypothesis**: Different AUROC binarization threshold or pipeline for SciERC. The SciERC median F1 may have tied instances handled differently.  \n**Action required**: Verify which AUROC pipeline produced Table 1. If the registry values are correct, Table 1 SciERC AUROC column needs updating. This also affects:\n- Abstract/Introduction \"AUROC up to 0.82\" → still valid (CoNLL EM 0.816 matches registry)\n- But SciERC EM AUROC should be ~0.749, not 0.614\n\n### 3. CoNLL LP selection Δ: Table 3 vs Appendix cross-selection table\n\n| Source | Greedy | LP F1 | LP Δ |\n|--------|--------|-------|------|\n| Table 3 (experiments.tex:122) | .908 | — | **-0.85pp** |\n| Appendix tab:cross_selection (appendix.tex:248) | .908 | .897 | **-1.1pp** |\n\nBoth claim 3-seed means, Qwen/CoNLL N=8. The Δ values (-0.85pp vs -1.1pp) are inconsistent.  \n**Fix**: Reconcile these two tables. Check whether different seed combinations or averaging methods were used.\n\n### 4. WNUT-17 zero-F1 rate inconsistency within paper\n\n| Location | Value |\n|----------|-------|\n| experiments.tex:12 (dataset description) | \"52% zero F1\" |\n| experiments.tex:103 | \"51% of instances yield F1=0\" |\n| limitations.tex:3 | \"51% F1=0\" |\n\n**Fix**: Unify to one value. If it's N=8 data, verify the exact percentage and use consistently.\n\n---\n\n## ⚠️ Ambiguous/Unverifiable Claims\n\n### 5. \"13–87% degeneracy\" in Introduction (line 15)\n\nThe introduction says \"instance degeneracy (13–87% across our benchmarks).\"\n\n- 13% ≈ FewNERD (10.1–13.1% depending on seed) ✓\n- 87% = LLaMA CoNLL N=16 (registry: 86.5–86.7%) — this is a specific **model×dataset×N** configuration, not a benchmark\n\nThe appendix (line 232) confirms: \"On CoNLL, 48–87% of instances produce identical outputs\" — spanning Qwen N=8 (48%) to LLaMA N=16 (87%).\n\n**Issue**: \"across our benchmarks\" suggests cross-dataset variation, but 87% comes from a specific model+N configuration within CoNLL. The dataset-only range is ~10–68% (FewNERD to WNUT).  \n**Recommendation**: Change to \"across our experimental configurations\" or specify: \"(13% on Few-NERD to 87% on CoNLL under LLaMA at N=16)\".\n\n### 6. CoNLL degeneracy 48.4% labeled as N=8 in Table 3\n\nTable 3 caption: \"Qwen3-8B, N=8, T=1.0\". CoNLL Degen.% = 48.4%.\n\nBut `tab:degeneracy` (appendix.tex:362) shows: \"CoNLL 8B (N=16)\" = 48.4%.\n\nRegistry `exp_002_conll_n16` (N=16, seed 42): degen_rate = 0.4844 (48.4%).\n\nNo N=8 CoNLL degeneracy rate found in registry. With fewer samples (N=8), ALL having identical F1 is easier, so N=8 degeneracy should be **higher** than N=16's 48.4%.\n\n**Risk**: Table 3 may be using the N=16 degeneracy value in an N=8 context.  \n**Action**: Verify the N=8 CoNLL degeneracy from the actual N=8 experiment data.\n\n### 7. FewNERD degeneracy 13.8% vs registry data\n\nPaper Table 3: FewNERD degen = 13.8%.\n\nRegistry individual seeds (all N=8):\n- Seed 42 (exp_021_fewnerd_full): 10.1%\n- Seed 123: 13.1%\n- Seed 456: 12.1%\n- Seed 789: 11.8%\n\n3-seed mean (42/123/456): (10.1 + 13.1 + 12.1) / 3 = **11.8%** ≠ 13.8%  \n4-seed mean: (10.1 + 13.1 + 12.1 + 11.8) / 4 = **11.8%** ≠ 13.8%\n\n**Source of 13.8% unclear.** No seed combination produces this value. Could be from a different computation or epoch checkpoint.\n\n### 8. FewNERD LP global ρ = .220 in Table 3 vs seed 42 = 0.422\n\nTable 3 says LP ρ = .220 (3-seed mean). Registry seed 42: lp_global_rho = 0.4215. Seed 789: lp_rho_global = 0.1788.\n\nThis implies seeds 123/456 have very low LP ρ (~0.12 each) for the 3-seed mean to be 0.22. The seed variance (0.18–0.42) is extremely high for Spearman ρ, which is unusual.\n\n**Cannot verify** from available registry data (seeds 123/456 lack LP ρ).  \n**Recommendation**: Verify the 3-seed LP ρ values and consider reporting seed-specific values to acknowledge this variance.\n\n### 9. WNUT LP ρ: paper -0.446 vs registry -0.410\n\nPaper Table 3: LP ρ = -.446 (claimed N=8).  \nRegistry exp_003_ner_wnut17 (N=16): rho_logprob_full = -0.414.  \nRegistry exp_003_wnut17_eval (N=16): rho_logprob_full = -0.409.\n\nDifferent N values (paper N=8, registry N=16), so some difference is expected. But no N=8 WNUT data found in registry to verify.\n\n### 10. Entity construction Δ: paper vs registry (protocol mismatch)\n\nPaper (multi-seed mean) vs registry (5-fold CV):\n\n| Dataset | Paper LP Δ | Registry LP Δ | Paper Unif Δ | Registry Unif Δ |\n|---------|-----------|--------------|-------------|----------------|\n| SciERC | +1.02pp | +1.67pp | +0.74pp | +1.12pp |\n| FewNERD | +1.40pp | +0.88pp | +0.74pp | +0.32pp |\n| CoNLL | -0.39pp | -0.39pp | — | — |\n\nLarge differences on SciERC and FewNERD. The paper uses \"multi-seed mean±σ\" (averaging results from different training seeds), while the registry uses \"5-fold CV, bootstrap B=10000\" (within one model). These are legitimately different evaluation protocols, so direct comparison is invalid.\n\n**However**: The direction of difference is inconsistent — registry is higher than paper on SciERC but lower on FewNERD. This means multi-seed averaging isn't simply scaling all values down.  \n**Recommendation**: Source the individual seed construction results to verify the multi-seed means match.\n\n---\n\n## ⚠️ Known Contradiction (from task description)\n\n**\"Discussion '+0.1pp over single-sample' vs Limitations '+0.4pp over greedy'\"**\n\n**Status**: Not found in current paper text.\n\nThe closest matches are:\n- Experiments §5.5 (scaling): \"LP selection fails (SciERC −0.1pp, CoNLL −0.4pp)\" — these are 72B zero-shot LP selection results, different datasets, both negative. Not contradictory.\n- TOST appendix table: SJ NER Δ = +0.1pp (vs single-sample) — this is in the appendix, not Discussion.\n- Limitations: \"LP×VC combinations yield at most +0.2pp over greedy\" — 0.2pp, not 0.4pp.\n\n**Conclusion**: The contradiction may have been resolved in the current paper version, or the task description references numbers from an earlier draft. The current paper does not contain this specific conflict.\n\n---\n\n## ✅ Verified Claims\n\n### Abstract & Introduction\n| Claim | Source | Registry/Verified Value | Status |\n|-------|--------|------------------------|--------|\n| ρ up to 0.45 | CoNLL EM | exp_002: EM rho=0.4507 → 0.45 | ✅ |\n| AUROC up to 0.82 | CoNLL EM | exp_002: EM AUROC=0.8156 → 0.82 | ✅ |\n| +5–8pp F1 at 80% coverage | Selective pred. | exp_selective_prediction: SciERC +5.0, CoNLL +8.4, FewNERD +6.2 | ✅ |\n| LP +1.39pp on FewNERD (p<0.001) | LP selection | 4-seed mean = 1.38pp (CI [1.32, 1.44]) | ✅ (rounds) |\n| SciERC LP +0.2pp, p=0.29 | Table 2 (2-seed) | 0.647 - 0.645 = 0.2pp | ✅ |\n| ρ=0.052 (23 configs, p=0.81) | Degen vs LP | paper_framing confirms | ✅ |\n| MBR SJ median ρ=0.524 | Discussion | tab:degeneracy: 0.524 | ✅ |\n\n### Table 1 (QE) — Spearman ρ\n| Signal | Paper | Registry (exp_012_rerun_1024) | Status |\n|--------|-------|-------------------------------|--------|\n| SciERC VC ρ | .379 | 0.3792 | ✅ |\n| SciERC SJ ρ | .360 | 0.3599 | ✅ |\n| SciERC FK ρ | .267 | 0.2665 | ✅ |\n| SciERC EM ρ | .295 | 0.2945 | ✅ |\n| SciERC LP ρ | .205 | 0.2052 | ✅ |\n| CoNLL SJ ρ | .436 | exp_002: 0.4357 | ✅ |\n| CoNLL EM ρ | .451 | exp_002: 0.4507 | ✅ |\n| CoNLL LP ρ | .316 | exp_002: 0.3157 | ✅ |\n\n### Table 2 (SciERC Selection)\n| Method | Paper | Notes | Status |\n|--------|-------|-------|--------|\n| Oracle | .775±.001 | exp_012_rerun_1024: oracle F1=0.7758 (framing) | ✅ |\n| Greedy | .645±.001 | Consistent with framing 0.6439/0.6442 | ✅ |\n| LP | .647±.005 | 2-seed mean | ✅ |\n| Random | .610±.003 | exp_016_rerun_1024 framing: 0.6077 | ✅ |\n\n### Table 3 (Cross-dataset)\n| Dataset | Greedy | Degen | LP ρ | LP Δ | Status |\n|---------|--------|-------|------|------|--------|\n| SciERC | .644 | 17.8% | .205 | +0.61pp | ✅ all match single-seed exp_012 |\n| FewNERD | .748 | 13.8% | .220 | +1.39pp | ⚠️ degen 13.8% unverifiable; LP ρ unverifiable |\n| CoNLL | .908 | 48.4% | .302 | -0.85pp | ⚠️ degen might be N=16; LP Δ conflicts with appendix |\n| WNUT | .452 | 67.9% | -.446 | -0.45pp | ⚠️ LP ρ unverifiable at N=8 |\n\n### Scale Ablation (Table in experiments.tex)\n| Metric | Paper | Registry | Status |\n|--------|-------|----------|--------|\n| CoNLL 8B SJ ρ | .436 | exp_002: 0.4357 | ✅ |\n| CoNLL 4B SJ ρ | .422 | exp_qwen3_4b_conll: 0.4217 | ✅ |\n| SciERC 8B SJ ρ | .360 | exp_012_rerun_1024: 0.3599 | ✅ |\n| SciERC 4B SJ ρ | .422 | exp_qwen3_4b_scierc: 0.4221 | ✅ |\n| SciERC 8B degen | 17.8% | 0.1777 | ✅ |\n| SciERC 4B degen | 10.4% | 0.104 | ✅ |\n\n### 72B Zero-shot (Table in experiments.tex)\n| Metric | Paper | Source | Status |\n|--------|-------|--------|--------|\n| SciERC 72B LP ρ | .081 | paper_framing: 0.081 | ✅ |\n| CoNLL 72B LP ρ | -.002 | paper_framing: -0.002 | ✅ |\n| SciERC 72B constr. +1.5pp | +1.5pp | paper_framing: +1.53pp | ✅ (rounded) |\n| CoNLL 72B constr. -0.37pp | -0.37pp | paper_framing: -0.37pp | ✅ |\n\nNote: 72B experiment is still RUNNING in registry — no final metrics to cross-verify. Paper values sourced from framing doc only.\n\n### LoRA Rank Ablation\n| Metric | Paper | Registry (exp_023_lora_rank8) | Status |\n|--------|-------|-------------------------------|--------|\n| Rank=8 degen | 7.2% | 0.072 | ✅ |\n| VC ρ | .394 (text) | 0.394 | ✅ |\n| SJ ρ | .365 (text) | 0.3649 | ✅ |\n\n### Other Verified Claims\n| Claim | Source | Status |\n|-------|--------|--------|\n| T=1.2 degen 14.9% | exp_026_t12: 0.1493 | ✅ |\n| Non-tied LP +2.9pp | Discussion | ✅ (p-value differs: paper 0.004 vs framing 0.01 — check which is post-correction) |\n| Bootstrap CI [-3.0, +4.2]pp | exp_016_rerun_1024_bootstrap: [-0.030, 0.042] | ✅ |\n| Cohen's d = 0.038 | exp_016_rerun_1024_bootstrap: 0.038 | ✅ |\n| Freeform std ratio 0.97 | exp_freeform_ablation: 0.97 | ✅ |\n| Parse rate 99.95% | exp_freeform_ablation: 0.9995 | ✅ |\n| FewNERD LP CI [1.02, 1.34] paper vs [1.18, 1.53] registry | Abstract says [1.02, 1.34]; registry says [1.18, 1.53] | ⚠️ see below |\n\n### Abstract LP CI discrepancy\nAbstract line 7: \"p<0.005\" (Table 5 shows p=.004 for SciERC and p<.001 for FewNERD — both < 0.005). The \"(multi-seed mean, p<0.005)\" applies to the joint claim. ✅\n\nBut the **bootstrap CI** for FewNERD LP selection:\n- Abstract: implied from \"p<0.005\"\n- Registry exp_021_fewnerd_full: lp_bootstrap_ci_95_pp = [1.18, 1.53]\n- Paper Table 3: not shown explicitly\n- Paper framing: LP selection CI [+1.02, +1.34] (for the 4-seed mean)\n\nThe CI [1.02, 1.34] (framing) vs [1.18, 1.53] (registry) represent different computations: framing uses 4-seed bootstrap of means, registry uses single-seed bootstrap. Not an error, but worth documenting.\n\n---\n\n## Summary of Required Actions\n\n| Priority | Issue | Action |\n|----------|-------|--------|\n| **P0** | ❌ WNUT VC ρ typo (0.730 → 0.724) | Fix experiments.tex:104 |\n| **P0** | ❌ SciERC AUROC pipeline discrepancy | Verify Table 1 AUROC computation; if registry is correct, update table |\n| **P0** | ❌ CoNLL LP Δ mismatch (-0.85 vs -1.1pp) | Reconcile Table 3 and Appendix cross-selection table |\n| **P0** | ❌ WNUT zero-F1 rate (51% vs 52%) | Unify within paper |\n| **P1** | ⚠️ \"13–87%\" in intro | Change to \"across configurations\" or give dataset-specific range |\n| **P1** | ⚠️ CoNLL degen 48.4% N=8 vs N=16 | Verify the N=8 value |\n| **P1** | ⚠️ FewNERD degen 13.8% source | Document or correct |\n| **P2** | ⚠️ FewNERD LP ρ seed variance | Consider reporting seed-level values |\n| **P2** | ⚠️ Non-tied LP p-value (0.004 vs 0.01) | Verify: one is pre-correction, one post? |\n| **INFO** | Known contradiction from task | Not found in current version; appears resolved |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
    "content": "# Claim Audit Report — struct_self_consist_ie\n\n**Date**: 2026-05-19  \n**Scope**: All quantitative claims in `docs/paper/sections/` cross-verified against experiment registry and paper_framing.md  \n**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.\n\n---\n\n## ❌ Inconsistencies Requiring Fix\n\n### 1. WNUT VC ρ inconsistency within paper (0.724 vs 0.730)\n\n| Location | Value |\n|----------|-------|\n| experiments.tex:48 | VC ρ=0.724 |\n| experiments.tex:104 | VC ρ=0.730 |\n| appendix.tex:217 (tab:wnut) | VC .724 |\n| appendix.tex:226 | VC ρ=0.724 |\n\n**Verdict**: 0.724 is the tabulated value, used 3× consistently. The 0.730 on line 104 is a **typo**.  \n**Fix**: Change experiments.tex:104 from `VC $\\rho{=}0.730$` to `VC $\\rho{=}0.724$`.\n\n### 2. SciERC AUROC in Table 1 vs registry (systematic offset)\n\nPaper Table 1 SciERC AUROC vs registry `exp_012_rerun_1024` (same ρ values, so same data):\n\n| Signal | Paper AUC | Registry AUROC | Δ |\n|--------|-----------|---------------|-----|\n| VC | .663 | .684 | -2.1pp |\n| SJ | .650 | .692 | -4.2pp |\n| FK | .602 | .629 | -2.7pp |\n| EM | .614 | .749 | **-13.5pp** |\n| LP | .578 | .578 | 0pp |\n\nρ values match to 3 decimal places (confirming same source data), but AUROC diverges except for LP. The EM gap (0.614 vs 0.749) is extreme. CoNLL AUROC values match the registry within 1pp.\n\n**Hypothesis**: Different AUROC binarization threshold or pipeline for SciERC. The SciERC median F1 may have tied instances handled differently.  \n**Action required**: Verify which AUROC pipeline produced Table 1. If the registry values are correct, Table 1 SciERC AUROC column needs updating. This also affects:\n- Abstract/Introduction \"AUROC up to 0.82\" → still valid (CoNLL EM 0.816 matches registry)\n- But SciERC EM AUROC should be ~0.749, not 0.614\n\n### 3. CoNLL LP selection Δ: Table 3 vs Appendix cross-selection table\n\n| Source | Greedy | LP F1 | LP Δ |\n|--------|--------|-------|------|\n| Table 3 (experiments.tex:122) | .908 | — | **-0.85pp** |\n| Appendix tab:cross_selection (appendix.tex:248) | .908 | .897 | **-1.1pp** |\n\nBoth claim 3-seed means, Qwen/CoNLL N=8. The Δ values (-0.85pp vs -1.1pp) are inconsistent.  \n**Fix**: Reconcile these two tables. Check whether different seed combinations or averaging methods were used.\n\n### 4. WNUT-17 zero-F1 rate inconsistency within paper\n\n| Location | Value |\n|----------|-------|\n| experiments.tex:12 (dataset description) | \"52% zero F1\" |\n| experiments.tex:103 | \"51% of instances yield F1=0\" |\n| limitations.tex:3 | \"51% F1=0\" |\n\n**Fix**: Unify to one value. If it's N=8 data, verify the exact percentage and use consistently.\n\n---\n\n## ⚠️ Ambiguous/Unverifiable Claims\n\n### 5. \"13–87% degeneracy\" in Introduction (line 15)\n\nThe introduction says \"instance degeneracy (13–87% across our benchmarks).\"\n\n- 13% ≈ FewNERD (10.1–13.1% depending on seed) ✓\n- 87% = LLaMA CoNLL N=16 (registry: 86.5–86.7%) — this is a specific **model×dataset×N** configuration, not a benchmark\n\nThe appendix (line 232) confirms: \"On CoNLL, 48–87% of instances produce identical outputs\" — spanning Qwen N=8 (48%) to LLaMA N=16 (87%).\n\n**Issue**: \"across our benchmarks\" suggests cross-dataset variation, but 87% comes from a specific model+N configuration within CoNLL. The dataset-only range is ~10–68% (FewNERD to WNUT).  \n**Recommendation**: Change to \"across our experimental configurations\" or specify: \"(13% on Few-NERD to 87% on CoNLL under LLaMA at N=16)\".\n\n### 6. CoNLL degeneracy 48.4% labeled as N=8 in Table 3\n\nTable 3 caption: \"Qwen3-8B, N=8, T=1.0\". CoNLL Degen.% = 48.4%.\n\nBut `tab:degeneracy` (appendix.tex:362) shows: \"CoNLL 8B (N=16)\" = 48.4%.\n\nRegistry `exp_002_conll_n16` (N=16, seed 42): degen_rate = 0.4844 (48.4%).\n\nNo N=8 CoNLL degeneracy rate found in registry. With fewer samples (N=8), ALL having identical F1 is easier, so N=8 degeneracy should be **higher** than N=16's 48.4%.\n\n**Risk**: Table 3 may be using the N=16 degeneracy value in an N=8 context.  \n**Action**: Verify the N=8 CoNLL degeneracy from the actual N=8 experiment data.\n\n### 7. FewNERD degeneracy 13.8% vs registry data\n\nPaper Table 3: FewNERD degen = 13.8%.\n\nRegistry individual seeds (all N=8):\n- Seed 42 (exp_021_fewnerd_full): 10.1%\n- Seed 123: 13.1%\n- Seed 456: 12.1%\n- Seed 789: 11.8%\n\n3-seed mean (42/123/456): (10.1 + 13.1 + 12.1) / 3 = **11.8%** ≠ 13.8%  \n4-seed mean: (10.1 + 13.1 + 12.1 + 11.8) / 4 = **11.8%** ≠ 13.8%\n\n**Source of 13.8% unclear.** No seed combination produces this value. Could be from a different computation or epoch checkpoint.\n\n### 8. FewNERD LP global ρ = .220 in Table 3 vs seed 42 = 0.422\n\nTable 3 says LP ρ = .220 (3-seed mean). Registry seed 42: lp_global_rho = 0.4215. Seed 789: lp_rho_global = 0.1788.\n\nThis implies seeds 123/456 have very low LP ρ (~0.12 each) for the 3-seed mean to be 0.22. The seed variance (0.18–0.42) is extremely high for Spearman ρ, which is unusual.\n\n**Cannot verify** from available registry data (seeds 123/456 lack LP ρ).  \n**Recommendation**: Verify the 3-seed LP ρ values and consider reporting seed-specific values to acknowledge this variance.\n\n### 9. WNUT LP ρ: paper -0.446 vs registry -0.410\n\nPaper Table 3: LP ρ = -.446 (claimed N=8).  \nRegistry exp_003_ner_wnut17 (N=16): rho_logprob_full = -0.414.  \nRegistry exp_003_wnut17_eval (N=16): rho_logprob_full = -0.409.\n\nDifferent N values (paper N=8, registry N=16), so some difference is expected. But no N=8 WNUT data found in registry to verify.\n\n### 10. Entity construction Δ: paper vs registry (protocol mismatch)\n\nPaper (multi-seed mean) vs registry (5-fold CV):\n\n| Dataset | Paper LP Δ | Registry LP Δ | Paper Unif Δ | Registry Unif Δ |\n|---------|-----------|--------------|-------------|----------------|\n| SciERC | +1.02pp | +1.67pp | +0.74pp | +1.12pp |\n| FewNERD | +1.40pp | +0.88pp | +0.74pp | +0.32pp |\n| CoNLL | -0.39pp | -0.39pp | — | — |\n\nLarge differences on SciERC and FewNERD. The paper uses \"multi-seed mean±σ\" (averaging results from different training seeds), while the registry uses \"5-fold CV, bootstrap B=10000\" (within one model). These are legitimately different evaluation protocols, so direct comparison is invalid.\n\n**However**: The direction of difference is inconsistent — registry is higher than paper on SciERC but lower on FewNERD. This means multi-seed averaging isn't simply scaling all values down.  \n**Recommendation**: Source the individual seed construction results to verify the multi-seed means match.\n\n---\n\n## ⚠️ Known Contradiction (from task description)\n\n**\"Discussion '+0.1pp over single-sample' vs Limitations '+0.4pp over greedy'\"**\n\n**Status**: Not found in current paper text.\n\nThe closest matches are:\n- Experiments §5.5 (scaling): \"LP selection fails (SciERC −0.1pp, CoNLL −0.4pp)\" — these are 72B zero-shot LP selection results, different datasets, both negative. Not contradictory.\n- TOST appendix table: SJ NER Δ = +0.1pp (vs single-sample) — this is in the appendix, not Discussion.\n- Limitations: \"LP×VC combinations yield at most +0.2pp over greedy\" — 0.2pp, not 0.4pp.\n\n**Conclusion**: The contradiction may have been resolved in the current paper version, or the task description references numbers from an earlier draft. The current paper does not contain this specific conflict.\n\n---\n\n## ✅ Verified Claims\n\n### Abstract & Introduction\n| Claim | Source | Registry/Verified Value | Status |\n|-------|--------|------------------------|--------|\n| ρ up to 0.45 | CoNLL EM | exp_002: EM rho=0.4507 → 0.45 | ✅ |\n| AUROC up to 0.82 | CoNLL EM | exp_002: EM AUROC=0.8156 → 0.82 | ✅ |\n| +5–8pp F1 at 80% coverage | Selective pred. | exp_selective_prediction: SciERC +5.0, CoNLL +8.4, FewNERD +6.2 | ✅ |\n| LP +1.39pp on FewNERD (p<0.001) | LP selection | 4-seed mean = 1.38pp (CI [1.32, 1.44]) | ✅ (rounds) |\n| SciERC LP +0.2pp, p=0.29 | Table 2 (2-seed) | 0.647 - 0.645 = 0.2pp | ✅ |\n| ρ=0.052 (23 configs, p=0.81) | Degen vs LP | paper_framing confirms | ✅ |\n| MBR SJ median ρ=0.524 | Discussion | tab:degeneracy: 0.524 | ✅ |\n\n### Table 1 (QE) — Spearman ρ\n| Signal | Paper | Registry (exp_012_rerun_1024) | Status |\n|--------|-------|-------------------------------|--------|\n| SciERC VC ρ | .379 | 0.3792 | ✅ |\n| SciERC SJ ρ | .360 | 0.3599 | ✅ |\n| SciERC FK ρ | .267 | 0.2665 | ✅ |\n| SciERC EM ρ | .295 | 0.2945 | ✅ |\n| SciERC LP ρ | .205 | 0.2052 | ✅ |\n| CoNLL SJ ρ | .436 | exp_002: 0.4357 | ✅ |\n| CoNLL EM ρ | .451 | exp_002: 0.4507 | ✅ |\n| CoNLL LP ρ | .316 | exp_002: 0.3157 | ✅ |\n\n### Table 2 (SciERC Selection)\n| Method | Paper | Notes | Status |\n|--------|-------|-------|--------|\n| Oracle | .775±.001 | exp_012_rerun_1024: oracle F1=0.7758 (framing) | ✅ |\n| Greedy | .645±.001 | Consistent with framing 0.6439/0.6442 | ✅ |\n| LP | .647±.005 | 2-seed mean | ✅ |\n| Random | .610±.003 | exp_016_rerun_1024 framing: 0.6077 | ✅ |\n\n### Table 3 (Cross-dataset)\n| Dataset | Greedy | Degen | LP ρ | LP Δ | Status |\n|---------|--------|-------|------|------|--------|\n| SciERC | .644 | 17.8% | .205 | +0.61pp | ✅ all match single-seed exp_012 |\n| FewNERD | .748 | 13.8% | .220 | +1.39pp | ⚠️ degen 13.8% unverifiable; LP ρ unverifiable |\n| CoNLL | .908 | 48.4% | .302 | -0.85pp | ⚠️ degen might be N=16; LP Δ conflicts with appendix |\n| WNUT | .452 | 67.9% | -.446 | -0.45pp | ⚠️ LP ρ unverifiable at N=8 |\n\n### Scale Ablation (Table in experiments.tex)\n| Metric | Paper | Registry | Status |\n|--------|-------|----------|--------|\n| CoNLL 8B SJ ρ | .436 | exp_002: 0.4357 | ✅ |\n| CoNLL 4B SJ ρ | .422 | exp_qwen3_4b_conll: 0.4217 | ✅ |\n| SciERC 8B SJ ρ | .360 | exp_012_rerun_1024: 0.3599 | ✅ |\n| SciERC 4B SJ ρ | .422 | exp_qwen3_4b_scierc: 0.4221 | ✅ |\n| SciERC 8B degen | 17.8% | 0.1777 | ✅ |\n| SciERC 4B degen | 10.4% | 0.104 | ✅ |\n\n### 72B Zero-shot (Table in experiments.tex)\n| Metric | Paper | Source | Status |\n|--------|-------|--------|--------|\n| SciERC 72B LP ρ | .081 | paper_framing: 0.081 | ✅ |\n| CoNLL 72B LP ρ | -.002 | paper_framing: -0.002 | ✅ |\n| SciERC 72B constr. +1.5pp | +1.5pp | paper_framing: +1.53pp | ✅ (rounded) |\n| CoNLL 72B constr. -0.37pp | -0.37pp | paper_framing: -0.37pp | ✅ |\n\nNote: 72B experiment is still RUNNING in registry — no final metrics to cross-verify. Paper values sourced from framing doc only.\n\n### LoRA Rank Ablation\n| Metric | Paper | Registry (exp_023_lora_rank8) | Status |\n|--------|-------|-------------------------------|--------|\n| Rank=8 degen | 7.2% | 0.072 | ✅ |\n| VC ρ | .394 (text) | 0.394 | ✅ |\n| SJ ρ | .365 (text) | 0.3649 | ✅ |\n\n### Other Verified Claims\n| Claim | Source | Status |\n|-------|--------|--------|\n| T=1.2 degen 14.9% | exp_026_t12: 0.1493 | ✅ |\n| Non-tied LP +2.9pp | Discussion | ✅ (p-value differs: paper 0.004 vs framing 0.01 — check which is post-correction) |\n| Bootstrap CI [-3.0, +4.2]pp | exp_016_rerun_1024_bootstrap: [-0.030, 0.042] | ✅ |\n| Cohen's d = 0.038 | exp_016_rerun_1024_bootstrap: 0.038 | ✅ |\n| Freeform std ratio 0.97 | exp_freeform_ablation: 0.97 | ✅ |\n| Parse rate 99.95% | exp_freeform_ablation: 0.9995 | ✅ |\n| FewNERD LP CI [1.02, 1.34] paper vs [1.18, 1.53] registry | Abstract says [1.02, 1.34]; registry says [1.18, 1.53] | ⚠️ see below |\n\n### Abstract LP CI discrepancy\nAbstract line 7: \"p<0.005\" (Table 5 shows p=.004 for SciERC and p<.001 for FewNERD — both < 0.005). The \"(multi-seed mean, p<0.005)\" applies to the joint claim. ✅\n\nBut the **bootstrap CI** for FewNERD LP selection:\n- Abstract: implied from \"p<0.005\"\n- Registry exp_021_fewnerd_full: lp_bootstrap_ci_95_pp = [1.18, 1.53]\n- Paper Table 3: not shown explicitly\n- Paper framing: LP selection CI [+1.02, +1.34] (for the 4-seed mean)\n\nThe CI [1.02, 1.34] (framing) vs [1.18, 1.53] (registry) represent different computations: framing uses 4-seed bootstrap of means, registry uses single-seed bootstrap. Not an error, but worth documenting.\n\n---\n\n## Summary of Required Actions\n\n| Priority | Issue | Action |\n|----------|-------|--------|\n| **P0** | ❌ WNUT VC ρ typo (0.730 → 0.724) | Fix experiments.tex:104 |\n| **P0** | ❌ SciERC AUROC pipeline discrepancy | Verify Table 1 AUROC computation; if registry is correct, update table |\n| **P0** | ❌ CoNLL LP Δ mismatch (-0.85 vs -1.1pp) | Reconcile Table 3 and Appendix cross-selection table |\n| **P0** | ❌ WNUT zero-F1 rate (51% vs 52%) | Unify within paper |\n| **P1** | ⚠️ \"13–87%\" in intro | Change to \"across configurations\" or give dataset-specific range |\n| **P1** | ⚠️ CoNLL degen 48.4% N=8 vs N=16 | Verify the N=8 value |\n| **P1** | ⚠️ FewNERD degen 13.8% source | Document or correct |\n| **P2** | ⚠️ FewNERD LP ρ seed variance | Consider reporting seed-level values |\n| **P2** | ⚠️ Non-tied LP p-value (0.004 vs 0.01) | Verify: one is pre-correction, one post? |\n| **INFO** | Known contradiction from task | Not found in current version; appears resolved |\n"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-19T13:46:31.802375+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-19T13:46:31.802514+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "claim_audit_report",
  "type": "report",
  "description": "Full quantitative claim audit of the paper: cross-verified all numerical claims against experiment registry. Found 4 inconsistencies requiring fix, 6 ambiguous/unverifiable claims, and confirmed ~30 claims as correct.",
  "project": "struct_self_consist_ie",
  "exp_id": "exp_024_claim_audit",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
  "tags": "['audit', 'paper', 'claim-verification']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "claim_audit_report",
    "type": "report",
    "description": "Full quantitative claim audit of the paper: cross-verified all numerical claims against experiment registry. Found 4 inconsistencies requiring fix, 6 ambiguous/unverifiable claims, and confirmed ~30 claims as correct.",
    "project": "struct_self_consist_ie",
    "exp_id": "exp_024_claim_audit",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md",
    "tags": "['audit', 'paper', 'claim-verification']"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-19T13:46:31.802669+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_146f83\", \"name\": \"claim_audit_report\", \"type\": \"report\", \"description\": \"Full quantitative claim audit of the paper: cross-verified all numerical claims against experiment registry. Found 4 inconsistencies requiring fix, 6 ambiguous/unverifiable claims, and confirmed ~30 claims as correct.\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_024_claim_audit/report/claim_audit_report.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_024_claim_audit\", \"skill\": \"\", \"created_at\": \"2026-05-19T13:46:18.176541+00:00\", \"tags\": [\"audit\", \"paper\", \"claim-verification\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_claim_audit_20260519T133313",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-19T13:46:31.802841+00:00_

审计报告已写入 `artifacts/claim_audit_report.md` 并注册。

核心发现：

**4 个需修复的不一致 (❌)**：
1. WNUT VC ρ 打字错误：experiments.tex:104 写了 0.730，应为 0.724
2. Table 1 SciERC AUROC 列与 registry 系统性偏离（EM: 0.614 vs 0.749），疑似 AUROC 计算管线不同
3. CoNLL LP 选择 Δ：Table 3 写 -0.85pp，附录 cross-selection 表算出 -1.1pp
4. WNUT zero-F1 率在论文内不统一（51% vs 52%）

**6 个存疑/无法验证的声明 (⚠️)**：
- "13–87% degeneracy" 跨 benchmarks → 87% 来自特定 model×N 配置，非跨数据集
- CoNLL 退化率 48.4% 可能是 N=16 值误用于 N=8 表格
- FewNERD 退化率 13.8% 无法从 registry seed 数据复现（3-seed 均值约 11.8%）
- FewNERD LP ρ=.220 种子间方差极大，无法从现有数据验证
- Entity construction 数值因评估协议不同（multi-seed vs 5-fold CV）无法直接对比

**已知矛盾状态**：当前论文版本中未找到 "Discussion +0.1pp" vs "Limitations +0.4pp" 冲突，可能已在编辑中修复。72B 节中 SciERC -0.1pp 和 CoNLL -0.4pp 是不同数据集的结果，非矛盾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_claim_audit_20260519T133313"
}
```

</details>

---
