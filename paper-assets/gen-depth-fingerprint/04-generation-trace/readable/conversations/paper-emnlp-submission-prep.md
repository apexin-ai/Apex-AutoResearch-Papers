# paper emnlp submission prep

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 0
- **Tool calls:** 36
- **Original source:** `logs/chats/worker_paper_emnlp-submission-prep_20260516T030521.jsonl`
- **Structured JSON:** [`f510ae12b8bcdccb1a4b.json`](../../sessions/f5/f510ae12b8bcdccb1a4b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

73 recorded events

### Tool call

_source line 1 · 2026-05-16T03:09:05.524644+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T03:09:05.524936+00:00_

artifacts/_project/paper/_backup/method_01fe38.tex
artifacts/_project/paper/_backup/ethics_7f2659.tex
artifacts/_project/paper/_backup/table1.tex
artifacts/_project/paper/_backup/table1_329527.tex
artifacts/_project/paper/_backup/table2.tex
artifacts/_project/paper/_backup/table2_373612.tex
artifacts/_project/paper/_backup/table3.tex
artifacts/_project/paper/_backup/table3_fc4017.tex
artifacts/_project/paper/_backup/discussion_d3a579.tex
artifacts/_project/paper/_backup/table4.tex
artifacts/_project/paper/_backup/table4_49aebb.tex
artifacts/_project/paper/ethics.tex
artifacts/_project/paper/_backup/ethics_25b81b.tex
artifacts/_project/paper/_backup/related_work_2ce9dd.tex
artifacts/_project/paper/_backup/main_53f11a.tex
artifacts/_project/paper/_backup/conclusion_b5f10d.tex
artifacts/_project/paper/_backup/introduction_4bbcfd.tex
artifacts/_project/paper/_backup/conclusion_70534e.tex
artifacts/_project/paper/_backup/discussion_c98572.tex
artifacts/_project/paper/appendix_length.tex
artifacts/_project/paper/_backup/abstract_014854.tex
artifacts/_project/paper/_backup/results_b30771.tex
artifacts/_project/paper/_backup/limitations_69ebec.tex
artifacts/_project/paper/_backup/limitations_b3d194.tex
artifacts/_project/paper/_backup/method_e59d28.tex
artifacts/_project/paper/appendix_prompt_type.tex
artifacts/_project/paper/appendix_confusion_matrix.tex
artifacts/_project/paper/appendix_lofo.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/appendix_human_edit.tex
artifacts/_project/paper/appendix_classifier.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/table4.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/appendix_qlora.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/appendix_finer_depth.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T03:09:05.525103+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T03:09:05.525236+00:00_

artifacts/_project/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T03:09:05.525401+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T03:09:05.525531+00:00_

docs/paper/appendix_confusion_matrix.tex
docs/paper/appendix_length.tex
docs/paper/appendix_lofo.tex
docs/paper/appendix_prompt_type.tex
docs/paper/ethics.tex
docs/paper/table3.tex
docs/paper/table4.tex
docs/paper/related_work.tex
docs/paper/appendix_classifier.tex
docs/paper/appendix_human_edit.tex
docs/paper/table1.tex
docs/paper/table2.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/results.tex
docs/paper/method.tex
docs/paper/appendix_qlora.tex
docs/paper/main.tex
docs/paper/appendix_finer_depth.tex
docs/paper/discussion.tex
docs/paper/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T03:09:05.525724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T03:09:05.525874+00:00_

1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	
11	\graphicspath{{../chart/}}
12	
13	\title{Depth Fingerprinting: Ordinal Generation Depth Estimation\\in Non-Paraphrastic LLM Text Chains}
14	
15	\author{Anonymous}
16	
17	\begin{document}
18	\maketitle
19	
20	\input{abstract}
21	
22	\input{introduction}
23	\input{related_work}
24	\input{method}
25	\input{results}
26	
27	\input{discussion}
28	\input{conclusion}
29	\input{limitations}
30	\input{ethics}
31	
32	\bibliography{references}
33	
34	\appendix
35	\section{Length Confound Analysis}
36	\label{app:length}
37	\input{appendix_length}
38	
39	\section{Prompt Type Generalization}
40	\label{app:prompt-type}
41	\input{appendix_prompt_type}
42	
43	\section{Finer-Grained Depth Classification}
44	\label{app:finer-depth}
45	\input{appendix_finer_depth}
46	
47	\section{End-to-End Depth Classification (QLoRA)}
48	\label{app:qlora}
49	\input{appendix_qlora}
50	
51	\section{Leave-One-Feature-Out Analysis}
52	\label{app:lofo}
53	\input{appendix_lofo}
54	
55	\section{Confusion Matrix}
56	\label{app:confusion}
57	\input{appendix_confusion_matrix}
58	
59	\section{Classifier Sensitivity}
60	\label{app:classifier}
61	\input{appendix_classifier}
62	
63	\section{Human-Edit Robustness}
64	\label{app:human-edit}
65	\input{appendix_human_edit}
66	
67	\end{document}
68	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T03:09:05.526008+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T03:09:05.526133+00:00_

1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	As LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.
4	We formulate \emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.
5	We characterize a \emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.
6	A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\% CI: [0.717, 0.729]) for gen-1 vs.\ gen-2+ depth discrimination---excluding gen-0 to avoid shared-seed overlap---($p < 0.001$ vs.\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\,=\,0.051).
7	In our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T03:09:05.526258+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T03:09:05.526413+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.
5	Estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.
6	The result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.
7	
8	Existing detectors \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.
9	This conflates qualitatively different material.
10	A first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.
11	A third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.
12	Treating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.
13	
14	We argue that a finer-grained characterization is needed: \emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\,/\,gen-1\,/\,gen-2+) rather than producing a binary label.
15	We refer to the overall framework---features, classifier, and evaluation protocol---as \emph{depth fingerprinting}, distinguishing the method from the task it addresses.
16	No existing method ad
…[truncated 3974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T03:09:05.526549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T03:09:05.526730+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests on token-level distributions \cite{gltr,grover,release_strategies} to zero-shot approaches exploiting reference-model likelihoods \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers over linguistic features \cite{feat_aug_transformer,reliable_detection,ld_score}.
8	Recent work has pursued diverse detection signals: \citet{intrinsic_dimension} use intrinsic dimensionality estimates, \citet{diveye} propose surprisal diversity features directly comparable to our distributional features, and \citet{generator_barrier} characterize the distributional gap between human and model outputs.
9	\citet{wu_survey_2025} provide the most comprehensive recent survey; see also \citet{jawahar_survey} for an earlier overview.
10	Commercial systems such as GPTZero provide trained-classifier detection but are non-reproducible due to proprietary model access, precluding controlled baseline comparison; we restrict evaluation to open methods.
11	A persistent limitation is that all these methods produce binary (real vs.\ synthetic) decisions.
12	Recent efforts extend detection to multi-class settings: \citet{beyond_binary} propose role recognition and involvement measurement to distinguish collaborative human-LLM generation scenarios, and the SemEval-2024 shared task \cite{semeval2024_task8} evaluates multi-generator attribution across domains and languages.
13	These approaches discriminate among different \emph{sources} (human vs.\ specific models) rather than recursive generation \emph{depth} within a single generator's chain.
14	Even when detection scores correlate with generation depth, they exhibit high cross-generator variance when repurposed as ordinal predictors (binary F1 from 0.52 to 0.71 across individual baselines; Table~\ref{
…[truncated 5725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T03:09:05.526874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T03:09:05.527048+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using six generators spanning three model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, and \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}.
17	This selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	The same pool of seed passages serves as gen-0 for all generators.
21	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
22	We address this with a supplementary binary evaluatio
…[truncated 8012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T03:09:05.527185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T03:09:05.527384+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate depth fingerprinting along four axes: cross-generator classification (\S\ref{sec:results-classification}), differential depth response of individual features (\S\ref{sec:results-differential}), comparison with existing detection baselines (\S\ref{sec:results-baselines}), and downstream utility for data curation (\S\ref{sec:results-downstream}).
5	
6	\subsection{Depth Classification Performance}
7	\label{sec:results-classification}
8	
9	Table~\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\,/\,gen-1\,/\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.
10	
11	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.789 (Table~\ref{tab:logo-results}). Because gen-0 seed texts are shared across generators (\S\ref{sec:generation}), the gen-0 class F1 (0.94) may be inflated; we therefore report a leak-free binary evaluation (gen-1 vs.\ gen-2+, F1\,=\,0.723) as the primary metric in \S\ref{sec:results-baselines}.
12	Per-generator held-out F1 ranges from 0.683 (Qwen3-8B) to 0.856 (Pythia-1B).
13	Per-class F1 varies by depth: gen-0\,=\,0.94, gen-2+\,=\,0.80, gen-1\,=\,0.64; the primary difficulty lies in distinguishing gen-1 from gen-2+, where feature margins narrow.
14	
15	\paragraph{Cross-scale transfer.}
16	The six-generator evaluation includes Qwen3-8B (8.2B parameters), confirming that depth signal persists at scales beyond the $\leq$2.8B training generators.
17	However, cross-scale transfer incurs a moderate gap: Qwen3-8B held-out F1\,=\,0.683 (CI [0.668, 0.694]), compared to 0.76--0.86 for $\leq$2.8B generators.
18	Text generated by larger models is more fluent, compressing feature margins and making depth distinctions harder.
19	Notably, adding Qwen3-8B data \emph{improves} classification on the original five generators (+0.8\,pp to 0.810), indicating that cross-scale diversity benefits rather than dilut
…[truncated 13231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T03:09:05.527531+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T03:09:05.527728+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why are shape features stationary?}
5	Distributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\S\ref{sec:results-differential}).
6	One \emph{speculative} explanation is that shape is primarily determined by the sampling mechanism (temperature, top-$p$ truncation) and the model's architecture-level output distribution, both of which are fixed across generation steps.
7	Recursive generation shifts \emph{what} the model talks about---steering toward higher-probability vocabulary regions---but does not alter \emph{how} the model distributes probability mass around its predictions.
8	If this account is correct, shape features should remain stationary even at much greater depths and across different prompt types, while level features should continue to drift until reaching a fixed point.
9	Sampling ablation supports this account: depth signal is robust to moderate sampling variation (F1 range ${\leq}0.3$\,pp for $t \in [0.5, 0.7]$) but degrades at extreme temperatures ($t = 1.0$, $-6$\,pp), consistent with shape features being determined by the sampling mechanism (Appendix~\ref{app:sampling-sensitivity}).
10	We flag this as a hypothesis for future investigation, not a conclusion supported by our current experiments.
11	
12	\paragraph{Relation to OOD detection.}
13	Reference-model entropy features are functionally NLL-based out-of-distribution scores---the same signal backbone underlying DetectGPT \cite{detectgpt}, GLTR \cite{gltr}, and Binoculars \cite{binoculars}.
14	Our contribution is not these features per se, but the \emph{ordinal} depth formulation and the empirical finding that they exhibit differential depth response under recursive generation.
15	This connection also offers a lens on shape stationarity: in the OOD detection literature, distributional location statistics (mean log-likel
…[truncated 10689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T03:09:05.527872+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T03:09:05.527997+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced ordinal generation depth estimation as a task beyond binary synthetic text detection, providing a framework for characterizing the provenance of web-crawled text at finer granularity.
5	Across six generators from three model families (0.6B--8.2B parameters), we documented differential depth response: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.
6	A 7-feature ensemble combining both feature types achieves binary macro-F1 of 0.723 (95\% CI: [0.717, 0.729]) for leak-free depth discrimination across six base-model generators, with per-generator std of 0.051.
7	Cross-model chains---where each generation step uses a different generator---yield comparable performance (3-class F1\,=\,0.809, binary F1\,=\,0.764), confirming that depth signal persists under the generator heterogeneity typical of real-world contamination.
8	We also reported that depth-aware data curation does not improve downstream language model quality over random subsampling, establishing that, in our experimental setting, depth fingerprinting functions as a diagnostic tool for provenance characterization rather than a curative tool for data selection.
9	
10	Future work should extend evaluation to instruction-tuned and RLHF models, frontier-scale generators (70B+), and multilingual settings.
11	All code, data, and trained models will be released upon publication to facilitate reproducibility.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T03:09:05.528117+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T03:09:05.528251+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All six generators are base (pretrained) models.
5	Web text is predominantly produced by instruction-tuned and RLHF-aligned models, whose generation distributions differ from base model continuations.
6	Preliminary instruct experiments show substantial depth-signal degradation: OLMo-2-1B-Instruct drops to 3-class LOGO F1\,=\,0.338 (vs.\ 0.764 for base OLMo-2-1B) and Qwen3-0.6B with chat template to F1\,=\,0.667 (vs.\ 0.816 base under the 7-generator LOGO split that includes the instruct variant; the base-only split yields 0.824, Table~\ref{tab:logo-results}).
7	Length-controlled analysis reveals that the effect of instruct tuning on surface features is model-dependent: Qwen models retain weakly positive TTR and hapax partial correlations with depth, while OLMo-Instruct exhibits negative correlations similar to base models.
8	Entropy-based depth signals show reversed partial correlations across all three instruct models (partial $\rho$ ranging from +0.103 to +0.364), though length-matched analysis for the smallest model yields near-zero correlations ($|\rho| < 0.02$) and binary classification is near chance (F1 $\approx$ 0.5), leaving the interpretation of these residuals ambiguous.
9	Disentangling architecture-dependent surface effects from the residual entropy sign change in instruct-tuned generation is a critical direction for future work.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale, but cross-scale classifier transfer incurs a moderate gap (held-out F1\,=\,0.683 vs.\ 0.76--0.86 for $\leq$2.8B generators).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	We evaluate three prompt types (continuation, elaboration, rewriting; Appendix~\ref{app:prompt-type}) but all share the same Pythia-2.8B generator.
16	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms the depth signal gener
…[truncated 1905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T03:09:05.528387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T03:09:05.528516+00:00_

1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage---how many recursive generation steps it has undergone---not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency---rather than content removal---is the objective.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T03:09:05.528652+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T03:09:05.528857+00:00_

1	% ===== Detection =====
2	
3	@inproceedings{detectgpt,
4	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
5	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
6	  booktitle = {Proceedings of the International Conference on Machine Learning},
7	  year = {2023},
8	}
9	
10	@inproceedings{gltr,
11	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
12	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
13	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
14	  year = {2019},
15	}
16	
17	@inproceedings{dna_gpt,
18	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
19	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
20	  booktitle = {Proceedings of the International Conference on Learning Representations},
21	  year = {2024},
22	}
23	
24	@inproceedings{binoculars,
25	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
26	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
27	  booktitle = {Proceedings of the International Conference on Machine Learning},
28	  year = {2024},
29	}
30	
31	@inproceedings{fast_detectgpt,
32	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
33	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
34	  booktitle = {Proceedings of the International Conference on Learning Representations},
35	  year = {2024},
36	}
37	
38	@article{ld_score,
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benc
…[truncated 17605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T03:09:05.529005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table4.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table4.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T03:09:05.529129+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\begin{tabular}{llccc}
5	\toprule
6	\textbf{Reference Model} & \textbf{Family} & \textbf{Params} & \textbf{LOGO F1} & \textbf{Entropy Drift Range} \\
7	\midrule
8	Pythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\
9	OLMo-2-1B  & OLMo   & 1.5B & 0.807 & [$-$0.61, $-$0.91] \\
10	Qwen3-0.6B & Qwen   & 0.6B & 0.816 & [$-$0.96, $-$1.35] \\
11	\bottomrule
12	\end{tabular}
13	\caption{Cross-family reference model validation.
14	Drift direction is consistent (negative) across all three reference models;
15	magnitude varies with reference model capacity.}
16	\label{tab:cross-ref}
17	\end{table}
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T03:09:05.529271+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T03:09:05.529405+00:00_

1	% Appendix A — Length Confound Analysis
2	% Data source: plan-013 (23,032 samples, 5 generators)
3	
4	Surface diversity features (TTR, hapax ratio) mechanically depend on text length:
5	shorter texts yield higher type-token ratios by construction.
6	If generation depth systematically shortens text, observed depth trends could be length artifacts rather than genuine distributional shifts.
7	We rule this out with three complementary analyses.
8	
9	\paragraph{(a) Length--depth correlation.}
10	We compute Spearman rank correlation between word count and depth across all five generators.
11	Correlations are weak and inconsistent in sign:
12	$\rho$ ranges from $-0.066$ (Pythia-1B) to $+0.134$ (OLMo-2-1B), with $|\rho| < 0.14$ in every case.
13	One generator (Qwen3-0.6B) shows no significant correlation ($\rho = 0.012$, $p = 0.43$).
14	Length and depth are thus near-independent in our corpus.
15	
16	\paragraph{(b) Length-normalized feature trends.}
17	To eliminate residual length effects, we recompute TTR and hapax ratio on fixed 200-word windows.
18	After normalization, monotonic depth trends are fully preserved for all generators; moreover, Spearman correlations between normalized features and depth \emph{increase} in absolute value (e.g., Pythia-2.8B TTR: $\rho = -0.633 \to -0.715$).
19	Length removal sharpens the depth signal rather than diminishing it, confirming that the signal is not a length artifact.
20	
21	\paragraph{(c) Length-matched classification.}
22	We subsample the dataset so that word-count distributions are equalized across depth classes, then retrain the 3-class XGBoost classifier (\S\ref{sec:results-classification}).
23	Macro-F1 changes by $\Delta = +0.041$ relative to the unmatched baseline---performance \emph{improves} when length variance is removed.
24	This is consistent with length acting as noise rather than signal.
25	
26	\paragraph{Conclusion.}
27	We observe a dropout bias: shorter texts are more likely to fall below the minimum-length thresh
…[truncated 242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T03:09:05.529544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_prompt_type.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_prompt_type.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T03:09:05.529687+00:00_

1	We evaluate depth fingerprinting under three prompt types using Pythia-2.8B: \emph{continuation} (``Continue the following text''), \emph{elaboration} (``Elaborate on the following text''), and \emph{inspired rewriting} (``Write a new passage inspired by the following text''). Each uses 995 seeds $\times$ 5 depths.
2	
3	\paragraph{Within-prompt-type classification.}
4	5-fold CV macro-F1: continuation 0.78, rewriting 0.74, elaboration 0.73. All three prompt types exhibit the same differential depth response pattern: drifting features (hapax ratio, TTR, entropy mean) show consistent monotonic trends, while stationary features (entropy std, tail decay) change by less than 5\%.
5	
6	\paragraph{Cross-prompt-type transfer (LOPTO).}
7	Leave-one-prompt-type-out evaluation yields average F1\,=\,0.753, confirming that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\% per depth step), followed by rewriting (6.1\%) and elaboration (1.4\%), consistent with continuation chains applying less semantic constraint on the output.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T03:09:05.529808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T03:09:05.529943+00:00_

1	We evaluate finer-grained 5-class depth classification (gen-0 through gen-4) using the same 7-feature ensemble and LOGO protocol described in \S\ref{sec:method}.
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\begin{tabular}{lcccc}
7	\toprule
8	\textbf{Held-out Generator} & \textbf{Macro F1} & \textbf{Weighted F1} & \textbf{Accuracy} \\
9	\midrule
10	OLMo-2-1B       & 0.484 & 0.506 & 0.524 \\
11	Pythia-1B        & 0.543 & 0.568 & 0.575 \\
12	Pythia-2.8B      & 0.523 & 0.540 & 0.560 \\
13	Qwen3-0.6B      & 0.513 & 0.521 & 0.546 \\
14	Qwen3-1.7B      & 0.510 & 0.536 & 0.548 \\
15	Qwen3-8B        & 0.434 & 0.455 & 0.493 \\
16	\midrule
17	\textbf{Average} & \textbf{0.501 $\pm$ 0.038} & \textbf{0.521} & \textbf{0.541} \\
18	\bottomrule
19	\end{tabular}
20	\caption{5-class LOGO evaluation. Each row holds out one generator for testing, training on the remaining five.}
21	\label{tab:5class-logo}
22	\end{table}
23	
24	\begin{table}[h]
25	\centering
26	\small
27	\begin{tabular}{lccccc}
28	\toprule
29	\textbf{Metric} & \textbf{Gen-0} & \textbf{Gen-1} & \textbf{Gen-2} & \textbf{Gen-3} & \textbf{Gen-4} \\
30	\midrule
31	Avg F1      & 0.921 & 0.634 & 0.268 & 0.259 & 0.423 \\
32	\bottomrule
33	\end{tabular}
34	\caption{Per-class F1 averaged across all six LOGO folds.}
35	\label{tab:5class-perclass}
36	\end{table}
37	
38	\paragraph{Analysis.}
39	Moving from 3-class (gen-0 / gen-1 / gen-2+) to 5-class classification reduces LOGO macro F1 from 0.789 to 0.501, a drop of 0.288.
40	The degradation is concentrated in the middle depths: gen-2 and gen-3 achieve only 0.268 and 0.259 F1, respectively.
41	The aggregated confusion matrix reveals that 36.5\% of true gen-2 samples are misclassified as gen-1, while 37.8\% of true gen-3 samples are predicted as gen-4.
42	Adjacent depths (gen-2$\leftrightarrow$gen-3, gen-3$\leftrightarrow$gen-4) account for the majority of errors, consistent with the intuition that deeper recursive generations converge in surface-level statistical fingerprints.
43
…[truncated 1713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T03:09:05.530082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T03:09:05.530217+00:00_

1	To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
2	
3	\paragraph{Setup.}
4	We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs on the same 6-generator dataset used throughout, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).
5	For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
6	All results use the same LOGO protocol as the main experiments.
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{QLoRA end-to-end depth classification vs.\ XGBoost on handcrafted features, under LOGO evaluation.}
12	\label{tab:qlora}
13	\begin{tabular}{lccc}
14	\toprule
15	\textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
16	\midrule
17	XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
18	QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
19	\bottomrule
20	\end{tabular}
21	\end{table}
22	
23	\paragraph{Results.}
24	QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003), a +11.6\,pp improvement over the XGBoost baseline (0.789).
25	On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
26	The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
27	
28	\paragraph{Hyperparameter robustness.}
29	A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), confirming stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).
30	
31	\paragraph{Implications.}
32	The substantial 3-class improvement demonstrates that raw token embeddings contain
…[truncated 664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T03:09:05.530350+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T03:09:05.530475+00:00_

1	We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.789).
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\begin{tabular}{lcc}
7	\toprule
8	\textbf{Dropped feature} & \textbf{LOGO F1} & $\boldsymbol{\Delta}$ \textbf{vs Full} \\
9	\midrule
10	entropy\_max    & 0.774 & $-$1.50\,pp \\
11	entropy\_mean   & 0.783 & $-$0.63\,pp \\
12	ttr             & 0.784 & $-$0.55\,pp \\
13	hapax\_ratio    & 0.785 & $-$0.42\,pp \\
14	tail\_decay     & 0.786 & $-$0.33\,pp \\
15	entropy\_std    & 0.786 & $-$0.29\,pp \\
16	entropy\_min    & 0.789 & $+$0.01\,pp \\
17	\midrule
18	Full (7 features) & 0.789 & --- \\
19	\bottomrule
20	\end{tabular}
21	\caption{Leave-one-feature-out ablation (6-gen LOGO). Each row drops one feature and re-evaluates with the LOGO protocol. Sorted by impact magnitude.}
22	\label{tab:lofo}
23	\end{table}
24	
25	\paragraph{Analysis.}
26	Entropy\_max causes the largest degradation when removed ($-$1.5\,pp), despite ranking only fourth in permutation importance (split frequency 0.063). This indicates that entropy\_max provides unique signal---capturing the most surprising token under the reference model---that is not redundant with other features.
27	Conversely, entropy\_min is fully redundant ($\Delta$\,=\,+0.01\,pp), consistent with its near-zero permutation importance (0.015).
28	Six of seven features contribute positively to the ensemble, confirming that the 7-feature design is not over-specified.
29	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T03:09:05.530622+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T03:09:05.530753+00:00_

1	Table~\ref{tab:confusion} reports the aggregated confusion matrix from 6-generator leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth $\geq$ 2).
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\begin{tabular}{lccc}
7	\toprule
8	& \textbf{Pred gen-0} & \textbf{Pred gen-1} & \textbf{Pred gen-2+} \\
9	\midrule
10	\textbf{True gen-0} & 5{,}937 (99.4\%) & 35 (0.6\%) & 0 (0.0\%) \\
11	\textbf{True gen-1} & 368 (6.2\%) & 4{,}437 (75.0\%) & 1{,}113 (18.8\%) \\
12	\textbf{True gen-2+} & 464 (3.0\%) & 3{,}646 (23.3\%) & 11{,}529 (73.7\%) \\
13	\bottomrule
14	\end{tabular}
15	\caption{Aggregated 3-class confusion matrix from 6-generator LOGO evaluation ($N=27{,}529$). Each cell shows count and row-normalized percentage. Gen-0 is near-perfectly identified. Gen-1 errors are asymmetric: misclassification as gen-2+ (18.8\%) is 3$\times$ more frequent than as gen-0 (6.2\%), indicating that gen-1 text already carries detectable recursive distortion.}
16	\label{tab:confusion}
17	\end{table}
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T03:09:05.530873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T03:09:05.531005+00:00_

1	To verify that the depth signal resides in the features rather than the classifier,
2	we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest
3	in place of XGBoost (Table~\ref{tab:alt-classifier}).
4	All other settings---the same 7 features, 3-class labels, and class-balanced downsampling---are
5	kept identical. For Logistic Regression we apply standard scaling to the features.
6	
7	\begin{table}[h]
8	\centering
9	\caption{LOGO macro-F1 across three classifiers. Each column shows the held-out generator F1.}
10	\label{tab:alt-classifier}
11	\small
12	\begin{tabular}{lc cccccc}
13	\toprule
14	Classifier & Avg F1 & OLMo-2 & Py-1B & Py-2.8B & Qw-0.6B & Qw-1.7B & Qw-8B \\
15	\midrule
16	XGBoost          & 0.789 & 0.764 & 0.856 & 0.804 & 0.824 & 0.806 & 0.683 \\
17	Random Forest    & 0.790 & 0.764 & 0.856 & 0.804 & 0.825 & 0.807 & 0.684 \\
18	Logistic Regr.   & 0.725 & 0.719 & 0.781 & 0.740 & 0.745 & 0.743 & 0.624 \\
19	\bottomrule
20	\end{tabular}
21	\end{table}
22	
23	Both tree-based classifiers achieve LOGO F1 $\approx 0.79$,
24	and even a linear model reaches $0.725$---well above the $0.33$ chance baseline for
25	three classes.
26	The per-generator ranking is also consistent across classifiers
27	(Pythia-1B easiest, Qwen3-8B hardest),
28	confirming that discriminative power originates in the entropy and lexical features,
29	not in classifier capacity.
30	
31	\subsection*{Sampling Sensitivity Analysis}
32	\label{app:sampling-sensitivity}
33	
34	To assess robustness to decoding hyperparameters, we regenerate the full chain set under three sampling configurations and re-evaluate the 3-class LOGO pipeline (Table~\ref{tab:sampling-ablation}).
35	
36	\begin{table}[h]
37	\centering
38	\caption{Depth classification under varying sampling parameters. All other settings match the default pipeline.}
39	\label{tab:sampling-ablation}
40	\small
41	\begin{tabular}{lcc ccc}
42	\toprule
43	Config & Temp.\ & Top-$p$ & 3-class F1 & Binary F1 & $\rho$(entr
…[truncated 1139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T03:09:05.531144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T03:09:05.531280+00:00_

1	To assess whether depth features are robust to post-generation human editing, we simulate two editing scenarios on the full generation chain dataset and re-evaluate the 6-generator LOGO pipeline (Table~\ref{tab:human-edit}).
2	
3	\paragraph{Random token replacement.}
4	We randomly replace 5\%, 10\%, or 20\% of tokens in each text with uniformly sampled vocabulary items, simulating unstructured human edits (typo corrections, word substitutions).
5	Classification degrades gracefully: 3-class F1 drops by 3.5\,pp at 5\% replacement and 6.0\,pp at 20\%, while binary F1 (gen-1 vs.\ gen-2+) remains nearly unchanged ($\Delta \leq 0.8$\,pp).
6	The asymmetry is expected---random edits primarily disrupt human-vs-machine separation (gen-0 classification) by injecting noise into surface features, but the depth-discriminative distributional signal between gen-1 and gen-2+ is distributed across enough tokens to survive moderate perturbation.
7	
8	\paragraph{LLM rephrase.}
9	We rephrase each text using an instruction-tuned LLM, simulating the common scenario where users lightly edit LLM-generated text with LLM assistance.
10	Three-class F1 drops modestly ($-3.4$\,pp), comparable to 5\% random replacement.
11	However, binary F1 drops substantially ($-6.3$\,pp), indicating that LLM rephrasing specifically erodes the distributional differences between generation depths---consistent with the rephraser imposing its own distributional signature that partially overwrites the depth fingerprint.
12	
13	\begin{table}[h]
14	\centering
15	\small
16	\caption{Human-edit robustness under 6-gen LOGO evaluation. Baseline uses unmodified generation chains.}
17	\label{tab:human-edit}
18	\begin{tabular}{lcccc}
19	\toprule
20	\textbf{Condition} & \textbf{3-class F1} & \textbf{Binary F1} & \textbf{$\Delta$ 3-class} & \textbf{$\Delta$ binary} \\
21	\midrule
22	Baseline          & 0.789 & 0.724 & ---       & ---       \\
23	Random 5\%        & 0.754 & 0.718 & $-3.5$\,pp & $-0.6$\,pp \\
24	Random 10\%   
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T03:09:05.531418+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(github\\.com|gitlab\\.com|huggingface\\.co|personal|university|institute|lab|acknowledge|thank|funding|grant|http[s]?://)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(github\\.com|gitlab\\.com|huggingface\\.co|personal|university|institute|lab|acknowledge|thank|funding|grant|http[s]?://)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T03:09:05.531603+00:00_

artifacts/_project/paper/related_work.tex:2:\label{sec:related}
artifacts/_project/paper/related_work.tex:5:\label{sec:related-detection}
artifacts/_project/paper/related_work.tex:12:Recent efforts extend detection to multi-class settings: \citet{beyond_binary} propose role recognition and involvement measurement to distinguish collaborative human-LLM generation scenarios, and the SemEval-2024 shared task \cite{semeval2024_task8} evaluates multi-generator attribution across domains and languages.
artifacts/_project/paper/related_work.tex:26:\label{sec:related-collapse}
artifacts/_project/paper/related_work.tex:40:\label{sec:related-diversity}
artifacts/_project/paper/related_work.tex:51:\label{sec:related-provenance}
artifacts/_project/paper/related_work.tex:53:Scalable data curation relies on quality signals to filter web-crawled corpora.
artifacts/_project/paper/appendix_prompt_type.tex:1:We evaluate depth fingerprinting under three prompt types using Pythia-2.8B: \emph{continuation} (``Continue the following text''), \emph{elaboration} (``Elaborate on the following text''), and \emph{inspired rewriting} (``Write a new passage inspired by the following text''). Each uses 995 seeds $\times$ 5 depths.
artifacts/_project/paper/appendix_prompt_type.tex:4:5-fold CV macro-F1: continuation 0.78, rewriting 0.74, elaboration 0.73. All three prompt types exhibit the same differential depth response pattern: drifting features (hapax ratio, TTR, entropy mean) show consistent monotonic trends, while stationary features (entropy std, tail decay) change by less than 5\%.
artifacts/_project/paper/appendix_prompt_type.tex:7:Leave-one-prompt-type-out evaluation yields average F1\,=\,0.753, confirming that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\% per depth step), followed by rewriting (6.1\%) and elaboration (1.4\%), consistent with continuation chains applying less semantic constraint on the output.
artif
…[truncated 9670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T03:09:05.531747+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{([^}]+)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{([^}]+)\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T03:09:05.531930+00:00_

artifacts/_project/paper/related_work.tex:7:Methods for distinguishing human-written from machine-generated text have evolved from statistical tests on token-level distributions \cite{gltr,grover,release_strategies} to zero-shot approaches exploiting reference-model likelihoods \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers over linguistic features \cite{feat_aug_transformer,reliable_detection,ld_score}.
artifacts/_project/paper/related_work.tex:12:Recent efforts extend detection to multi-class settings: \citet{beyond_binary} propose role recognition and involvement measurement to distinguish collaborative human-LLM generation scenarios, and the SemEval-2024 shared task \cite{semeval2024_task8} evaluates multi-generator attribution across domains and languages.
artifacts/_project/paper/related_work.tex:16:Our reference-model entropy features are functionally NLL-based out-of-distribution scores \cite{ood_baseline}; the contribution is not a new detection method but the task formulation (ordinal depth estimation) and the empirical finding that combining drifting and stationary features yields consistent cross-generator performance.
artifacts/_project/paper/related_work.tex:42:Declining lexical diversity in LLM-generated text is documented in both training \cite{curious_decline} and deployment \cite{writing_diversity} settings.
artifacts/_project/paper/related_work.tex:45:These features are classical stylometric measures with a long history in authorship attribution \cite{stamatatos_survey,koppel_authorship}.
artifacts/_project/paper/related_work.tex:57:An alternative approach is proactive provenance through watermarking \cite{watermark_llm,synthid_text,aaronson_watermark}, where identifiable patterns are embedded during generation.
artifacts/_project/paper/appendix_qlora.tex:1:To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora
…[truncated 15565 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T03:09:05.532124+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T03:09:05.532248+00:00_

artifacts/_project/chart/fig1_differential_response.pdf
artifacts/_project/chart/fig2_logo_performance.png
artifacts/_project/chart/fig3_baseline_comparison.png
artifacts/_project/chart/fig4_downstream_negative.pdf
artifacts/_project/chart/fig4_downstream_negative.png
artifacts/_project/chart/fig4_downstream_negative_20bbd0.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T03:09:05.532363+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\includegraphics",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\includegraphics",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T03:09:05.532485+00:00_

artifacts/_project/paper/results.tex:75:\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
artifacts/_project/paper/results.tex:122:\includegraphics[width=\columnwidth]{fig3_baseline_comparison.png}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T03:09:05.532615+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\ref\\{([^}]+)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "head_limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\ref\\{([^}]+)\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "head_limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T03:09:05.532813+00:00_

artifacts/_project/paper/related_work.tex:14:Even when detection scores correlate with generation depth, they exhibit high cross-generator variance when repurposed as ordinal predictors (binary F1 from 0.52 to 0.71 across individual baselines; Table~\ref{tab:baselines}), because each score captures a single distributional property that generalizes inconsistently.
artifacts/_project/paper/appendix_qlora.tex:26:The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
artifacts/_project/paper/appendix_confusion_matrix.tex:1:Table~\ref{tab:confusion} reports the aggregated confusion matrix from 6-generator leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth $\geq$ 2).
artifacts/_project/paper/appendix_human_edit.tex:1:To assess whether depth features are robust to post-generation human editing, we simulate two editing scenarios on the full generation chain dataset and re-evaluate the 6-generator LOGO pipeline (Table~\ref{tab:human-edit}).
artifacts/_project/paper/appendix_lofo.tex:1:We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.789).
artifacts/_project/paper/discussion.tex:5:Distributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\S\ref{sec:results-differential}).
artifacts/_project/paper/discussion.tex:9:Sampling ablation supports this account: depth signal is robust to moderate sampling variation (F1 range ${\leq}0.3$\,pp for $t \in [0.5, 0.7]$) but degrades at extreme temperatures ($t = 1.0$, $-6$\,pp), consistent with shape features being de
…[truncated 17307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T03:09:05.533013+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && grep -ohP '\\\\\\\\cite[tp]?\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex results.tex discussion.tex conclusion.tex limitations.tex ethics.tex appendix_*.tex table4.tex | grep -ohP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract all unique citation keys from non-backup .tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && grep -ohP '\\\\\\\\cite[tp]?\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex results.tex discussion.tex conclusion.tex limitations.tex ethics.tex appendix_*.tex table4.tex | grep -ohP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Extract all unique citation keys from non-backup .tex files"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T03:09:05.533141+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T03:09:05.533255+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -ohP '@\\w+\\{(\\w+),' references.bib | grep -ohP '\\{(\\w+),' | tr -d '{,' | sort -u",
  "description": "Extract all bib entry keys from references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -ohP '@\\w+\\{(\\w+),' references.bib | grep -ohP '\\{(\\w+),' | tr -d '{,' | sort -u",
    "description": "Extract all bib entry keys from references.bib"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T03:09:05.533376+00:00_

aaronson_watermark
beyond_binary
binoculars
broken_telephone
ccnet
chainwash
coral_ordinal
curious_decline
curse_of_recursion
detectgpt
detection_possibilities
diveye
dna_gpt
dsir
fast_detectgpt
feat_aug_transformer
frank_hall_ordinal
generator_barrier
gltr
grover
intrinsic_dimension
jawahar_survey
koppel_authorship
ld_score
mapping_llm_science
markovian_chains
min_k_percent
model_collapse_avoidable
monitoring_ai_review
munir_looking_glass
nucleus_sampling
olmo
ood_baseline
paraphrase_evades
pythia
qlora
qurating
qwen3
release_strategies
reliable_detection
self_consuming_mad
semeval2024_task8
stamatatos_survey
strong_model_collapse
synthid_text
uchendu_attribution
watermark_llm
writing_diversity
wu_survey_2025
xgboost

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T03:09:05.533492+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -ohP '\\\\cite[tp]?\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex results.tex discussion.tex conclusion.tex limitations.tex ethics.tex appendix_*.tex table4.tex | grep -ohP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract citation keys with escaped backslashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -ohP '\\\\cite[tp]?\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex results.tex discussion.tex conclusion.tex limitations.tex ethics.tex appendix_*.tex table4.tex | grep -ohP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Extract citation keys with escaped backslashes"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T03:09:05.533641+00:00_

aaronson_watermark
beyond_binary
binoculars
broken_telephone
ccnet
chainwash
coral_ordinal
curious_decline
curse_of_recursion
detectgpt
detection_possibilities
diveye
dna_gpt
dsir
fast_detectgpt
feat_aug_transformer
frank_hall_ordinal
generator_barrier
gltr
grover
intrinsic_dimension
jawahar_survey
koppel_authorship
ld_score
mapping_llm_science
markovian_chains
min_k_percent
model_collapse_avoidable
monitoring_ai_review
munir_looking_glass
nucleus_sampling
olmo
ood_baseline
paraphrase_evades
pythia
qlora
qurating
qwen3
release_strategies
reliable_detection
self_consuming_mad
semeval2024_task8
stamatatos_survey
strong_model_collapse
synthid_text
uchendu_attribution
watermark_llm
writing_diversity
wu_survey_2025
xgboost

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-16T03:09:05.533787+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "for f in abstract.tex introduction.tex related_work.tex method.tex results.tex discussion.tex conclusion.tex; do echo \"$f: $(wc -l < $f) lines\"; done && echo \"---\" && for f in limitations.tex ethics.tex; do echo \"$f (not counted): $(wc -l < $f) lines\"; done && echo \"---\" && for f in appendix_*.tex table4.tex; do echo \"$f: $(wc -l < $f) lines\"; done",
  "description": "Count lines per section to estimate page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Bash",
  "tool_args": {
    "command": "for f in abstract.tex introduction.tex related_work.tex method.tex results.tex discussion.tex conclusion.tex; do echo \"$f: $(wc -l < $f) lines\"; done && echo \"---\" && for f in limitations.tex ethics.tex; do echo \"$f (not counted): $(wc -l < $f) lines\"; done && echo \"---\" && for f in appendix_*.tex table4.tex; do echo \"$f: $(wc -l < $f) lines\"; done",
    "description": "Count lines per section to estimate page count"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T03:09:05.533907+00:00_

abstract.tex: 8 lines
introduction.tex: 42 lines
related_work.tex: 60 lines
method.tex: 95 lines
results.tex: 196 lines
discussion.tex: 86 lines
conclusion.tex: 11 lines
---
limitations.tex (not counted): 29 lines
ethics.tex (not counted): 8 lines
---
appendix_classifier.tex: 55 lines
appendix_confusion_matrix.tex: 17 lines
appendix_finer_depth.tex: 51 lines
appendix_human_edit.tex: 34 lines
appendix_length.tex: 29 lines
appendix_lofo.tex: 28 lines
appendix_prompt_type.tex: 7 lines
appendix_qlora.tex: 34 lines
table4.tex: 17 lines

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-16T03:09:05.534021+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "diff <(grep -ohP '\\\\cite[tp]?\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex results.tex discussion.tex conclusion.tex limitations.tex ethics.tex appendix_*.tex table4.tex | grep -ohP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u) <(grep -ohP '@\\w+\\{(\\w+),' references.bib | grep -ohP '\\{(\\w+),' | tr -d '{,' | sort -u)",
  "description": "Diff cited keys vs bib keys to find mismatches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Bash",
  "tool_args": {
    "command": "diff <(grep -ohP '\\\\cite[tp]?\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex results.tex discussion.tex conclusion.tex limitations.tex ethics.tex appendix_*.tex table4.tex | grep -ohP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u) <(grep -ohP '@\\w+\\{(\\w+),' references.bib | grep -ohP '\\{(\\w+),' | tr -d '{,' | sort -u)",
    "description": "Diff cited keys vs bib keys to find mismatches"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-16T03:09:05.534129+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-16T03:09:05.534260+00:00_

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
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
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

_source line 68 · 2026-05-16T03:09:05.534368+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-16T03:09:05.534498+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/emnlp_submission_checklist.md",
  "content": "# EMNLP 2026 ARR Submission Pre-flight Checklist\n\n**Paper**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains  \n**Date**: 2026-05-16  \n**Paper directory**: `artifacts/_project/paper/`\n\n---\n\n## 1. Anonymization\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 1.1 | Author field | ✅ | `\\author{Anonymous}` in `main.tex:15` |\n| 1.2 | No institutional affiliations | ✅ | None found |\n| 1.3 | No acknowledgments section | ✅ | Absent (correct for review) |\n| 1.4 | No GitHub/GitLab/personal URLs | ✅ | No repository or personal URLs in any .tex |\n| 1.5 | No funding/grant info | ✅ | None found |\n| 1.6 | Conclusion release statement | ✅ | `conclusion.tex:11` says \"will be released upon publication\" — no URL provided, safe |\n| 1.7 | PDF metadata | ⚠️ | **No compiled PDF found in paper directory. Compile and verify `pdfinfo` shows no author/creator metadata before submission.** |\n| 1.8 | `_backup/` directory | ❌ | `artifacts/_project/paper/_backup/` contains 24 old .tex files (some with `\\cite{placeholder}`). **Must exclude from submission package.** |\n\n---\n\n## 2. Page Count (8-page limit, excl. references + appendix)\n\nMain body line counts (source lines, not formatted):\n\n| Section | Lines | Tables | Figures |\n|---------|-------|--------|---------|\n| Abstract | 8 | 0 | 0 |\n| Introduction | 42 | 0 | 0 |\n| Related Work | 60 | 0 | 0 |\n| Method | 95 | 0 | 0 |\n| Results | 196 | 4 (+ table4.tex = 5) | 2 |\n| Discussion | 86 | 0 | 0 |\n| Conclusion | 11 | 0 | 0 |\n| **Total** | **498** | **5** | **2** |\n\nNot counted toward limit: Limitations (29 lines), Ethics (8 lines), References, Appendix (8 sections, 272 lines).\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 2.1 | Main body ≤ 8 pages | ⚠️ | **Estimated 7–9 pages. With 498 source lines + 5 tables + 2 figures in ACL two-column format, this is borderline. Must compile to verify.** Discussion section is substantial (86 lines, ~12 paragraphs). If over limit, Discussion is the primary candidate for trimming. |\n\n---\n\n## 3. Required Sections\n\n| # | Section | Status | Notes |\n|---|---------|--------|-------|\n| 3.1 | Abstract | ✅ | `abstract.tex`, included via `\\input` |\n| 3.2 | Introduction | ✅ | `introduction.tex`, `\\section{Introduction}` |\n| 3.3 | Related Work | ✅ | `related_work.tex`, `\\section{Related Work}` |\n| 3.4 | Method | ✅ | `method.tex`, `\\section{Method}` |\n| 3.5 | Results/Experiments | ✅ | `results.tex`, `\\section{Results}` |\n| 3.6 | Discussion | ✅ | `discussion.tex`, `\\section{Discussion}` |\n| 3.7 | Conclusion | ✅ | `conclusion.tex`, `\\section{Conclusion}` |\n| 3.8 | Limitations | ✅ | `limitations.tex`, `\\section*{Limitations}` (unnumbered, correct) |\n| 3.9 | Ethics Statement | ✅ | `ethics.tex`, `\\section*{Ethics Statement}` (unnumbered, correct) |\n\n---\n\n## 4. References\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 4.1 | .bib file exists | ✅ | `references.bib` — 50 entries |\n| 4.2 | All `\\cite{}` keys defined in .bib | ✅ | 50 unique cited keys, all present in .bib (diff is empty) |\n| 4.3 | All .bib entries cited | ✅ | 50 bib entries, all cited (no orphan entries) |\n| 4.4 | No `\\cite{placeholder}` in main files | ✅ | Only in `_backup/` (excluded from compilation) |\n| 4.5 | Bib entry completeness | ⚠️ | Some entries lack page numbers or DOIs (e.g., `stamatatos_survey`, `koppel_authorship`, `aaronson_watermark`). Acceptable for ARR but recommend filling in for camera-ready. |\n\n---\n\n## 5. Figures and Tables\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 5.1 | Figure files exist | ✅ | `fig1_differential_response.pdf` ✅, `fig3_baseline_comparison.png` ✅ (both in `../chart/`) |\n| 5.2 | `\\graphicspath` correct | ✅ | `main.tex:11`: `\\graphicspath{{../chart/}}` |\n| 5.3 | Unused figure files | ⚠️ | `fig2_logo_performance.png`, `fig4_downstream_negative.pdf/.png` exist in `chart/` but are not referenced. Clean up before submission to reduce package size. |\n| 5.4 | All `\\ref{}` targets defined | ✅ | All cross-references (sections, tables, figures, appendices) have matching `\\label{}` definitions |\n\n---\n\n## 6. Appendix / Supplementary Materials\n\n8 appendix sections in `main.tex`, ordered:\n\n| # | Appendix | Label | File |\n|---|----------|-------|------|\n| A | Length Confound Analysis | `app:length` | `appendix_length.tex` |\n| B | Prompt Type Generalization | `app:prompt-type` | `appendix_prompt_type.tex` |\n| C | Finer-Grained Depth Classification | `app:finer-depth` | `appendix_finer_depth.tex` |\n| D | End-to-End Depth Classification (QLoRA) | `app:qlora` | `appendix_qlora.tex` |\n| E | Leave-One-Feature-Out Analysis | `app:lofo` | `appendix_lofo.tex` |\n| F | Confusion Matrix | `app:confusion` | `appendix_confusion_matrix.tex` |\n| G | Classifier Sensitivity | `app:classifier` | `appendix_classifier.tex` |\n| H | Human-Edit Robustness | `app:human-edit` | `appendix_human_edit.tex` |\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 6.1 | All appendix files exist | ✅ | All 8 files present |\n| 6.2 | Sampling Sensitivity sub-section | ⚠️ | `app:sampling-sensitivity` is a `\\subsection*` inside Appendix G (`appendix_classifier.tex:32`). The label resolves to the parent section. Cross-refs from `discussion.tex:9` and `limitations.tex:27` will point to Appendix G, not the subsection header. Consider promoting to its own appendix section if precise cross-referencing is needed. |\n\n---\n\n## 7. ACL/EMNLP Format\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 7.1 | Document class | ✅ | `\\documentclass[11pt]{article}` |\n| 7.2 | ACL style package | ✅ | `\\usepackage[review]{acl}` — review mode enables anonymization + line numbers |\n| 7.3 | Bibliography style | ✅ | `\\bibliography{references}` — `acl.sty` sets `acl_natbib` style automatically |\n| 7.4 | Required packages | ✅ | `times`, `latexsym`, `graphicx`, `booktabs`, `amsmath` all loaded |\n| 7.5 | `acl.sty` in submission | ⚠️ | **Verify `acl.sty` (2023 version) is included in the submission directory or available. Not found in the paper directory — must be added.** |\n\n---\n\n## 8. Summary\n\n| Category | ✅ Pass | ❌ Fail | ⚠️ Verify |\n|----------|---------|---------|-----------|\n| Anonymization | 6 | 1 | 1 |\n| Page count | — | — | 1 |\n| Required sections | 9 | 0 | 0 |\n| References | 4 | 0 | 1 |\n| Figures/Tables | 2 | 0 | 2 |\n| Appendix | 1 | 0 | 1 |\n| Format | 4 | 0 | 1 |\n| **Total** | **26** | **1** | **6** |\n\n### Action Items (must fix)\n\n1. **❌ Remove `_backup/` directory** from submission package (`paper/_backup/` — 24 stale .tex files, some containing `\\cite{placeholder}`)\n\n### Action Items (verify before submission)\n\n1. **⚠️ Compile PDF and check page count** — estimated 7–9 pages, must be ≤ 8. If over, trim Discussion (86 lines, most expendable).\n2. **⚠️ Check PDF metadata** after compilation — ensure no author/creator info leaks via `pdfinfo`.\n3. **⚠️ Include `acl.sty`** — the ACL 2023 style file must be present in the submission directory.\n4. **⚠️ Clean up unused figures** — `fig2_logo_performance.png`, `fig4_downstream_negative.*` in `chart/`.\n5. **⚠️ `app:sampling-sensitivity` cross-ref precision** — currently a `\\subsection*` inside Appendix G; consider promoting to its own appendix.\n6. **⚠️ Fill missing bib metadata** for camera-ready (page numbers, DOIs for some entries).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/emnlp_submission_checklist.md",
    "content": "# EMNLP 2026 ARR Submission Pre-flight Checklist\n\n**Paper**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains  \n**Date**: 2026-05-16  \n**Paper directory**: `artifacts/_project/paper/`\n\n---\n\n## 1. Anonymization\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 1.1 | Author field | ✅ | `\\author{Anonymous}` in `main.tex:15` |\n| 1.2 | No institutional affiliations | ✅ | None found |\n| 1.3 | No acknowledgments section | ✅ | Absent (correct for review) |\n| 1.4 | No GitHub/GitLab/personal URLs | ✅ | No repository or personal URLs in any .tex |\n| 1.5 | No funding/grant info | ✅ | None found |\n| 1.6 | Conclusion release statement | ✅ | `conclusion.tex:11` says \"will be released upon publication\" — no URL provided, safe |\n| 1.7 | PDF metadata | ⚠️ | **No compiled PDF found in paper directory. Compile and verify `pdfinfo` shows no author/creator metadata before submission.** |\n| 1.8 | `_backup/` directory | ❌ | `artifacts/_project/paper/_backup/` contains 24 old .tex files (some with `\\cite{placeholder}`). **Must exclude from submission package.** |\n\n---\n\n## 2. Page Count (8-page limit, excl. references + appendix)\n\nMain body line counts (source lines, not formatted):\n\n| Section | Lines | Tables | Figures |\n|---------|-------|--------|---------|\n| Abstract | 8 | 0 | 0 |\n| Introduction | 42 | 0 | 0 |\n| Related Work | 60 | 0 | 0 |\n| Method | 95 | 0 | 0 |\n| Results | 196 | 4 (+ table4.tex = 5) | 2 |\n| Discussion | 86 | 0 | 0 |\n| Conclusion | 11 | 0 | 0 |\n| **Total** | **498** | **5** | **2** |\n\nNot counted toward limit: Limitations (29 lines), Ethics (8 lines), References, Appendix (8 sections, 272 lines).\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 2.1 | Main body ≤ 8 pages | ⚠️ | **Estimated 7–9 pages. With 498 source lines + 5 tables + 2 figures in ACL two-column format, this is borderline. Must compile to verify.** Discussion section is substantial (86 lines, ~12 paragraphs). If over limit, Discussion is the primary candidate for trimming. |\n\n---\n\n## 3. Required Sections\n\n| # | Section | Status | Notes |\n|---|---------|--------|-------|\n| 3.1 | Abstract | ✅ | `abstract.tex`, included via `\\input` |\n| 3.2 | Introduction | ✅ | `introduction.tex`, `\\section{Introduction}` |\n| 3.3 | Related Work | ✅ | `related_work.tex`, `\\section{Related Work}` |\n| 3.4 | Method | ✅ | `method.tex`, `\\section{Method}` |\n| 3.5 | Results/Experiments | ✅ | `results.tex`, `\\section{Results}` |\n| 3.6 | Discussion | ✅ | `discussion.tex`, `\\section{Discussion}` |\n| 3.7 | Conclusion | ✅ | `conclusion.tex`, `\\section{Conclusion}` |\n| 3.8 | Limitations | ✅ | `limitations.tex`, `\\section*{Limitations}` (unnumbered, correct) |\n| 3.9 | Ethics Statement | ✅ | `ethics.tex`, `\\section*{Ethics Statement}` (unnumbered, correct) |\n\n---\n\n## 4. References\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 4.1 | .bib file exists | ✅ | `references.bib` — 50 entries |\n| 4.2 | All `\\cite{}` keys defined in .bib | ✅ | 50 unique cited keys, all present in .bib (diff is empty) |\n| 4.3 | All .bib entries cited | ✅ | 50 bib entries, all cited (no orphan entries) |\n| 4.4 | No `\\cite{placeholder}` in main files | ✅ | Only in `_backup/` (excluded from compilation) |\n| 4.5 | Bib entry completeness | ⚠️ | Some entries lack page numbers or DOIs (e.g., `stamatatos_survey`, `koppel_authorship`, `aaronson_watermark`). Acceptable for ARR but recommend filling in for camera-ready. |\n\n---\n\n## 5. Figures and Tables\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 5.1 | Figure files exist | ✅ | `fig1_differential_response.pdf` ✅, `fig3_baseline_comparison.png` ✅ (both in `../chart/`) |\n| 5.2 | `\\graphicspath` correct | ✅ | `main.tex:11`: `\\graphicspath{{../chart/}}` |\n| 5.3 | Unused figure files | ⚠️ | `fig2_logo_performance.png`, `fig4_downstream_negative.pdf/.png` exist in `chart/` but are not referenced. Clean up before submission to reduce package size. |\n| 5.4 | All `\\ref{}` targets defined | ✅ | All cross-references (sections, tables, figures, appendices) have matching `\\label{}` definitions |\n\n---\n\n## 6. Appendix / Supplementary Materials\n\n8 appendix sections in `main.tex`, ordered:\n\n| # | Appendix | Label | File |\n|---|----------|-------|------|\n| A | Length Confound Analysis | `app:length` | `appendix_length.tex` |\n| B | Prompt Type Generalization | `app:prompt-type` | `appendix_prompt_type.tex` |\n| C | Finer-Grained Depth Classification | `app:finer-depth` | `appendix_finer_depth.tex` |\n| D | End-to-End Depth Classification (QLoRA) | `app:qlora` | `appendix_qlora.tex` |\n| E | Leave-One-Feature-Out Analysis | `app:lofo` | `appendix_lofo.tex` |\n| F | Confusion Matrix | `app:confusion` | `appendix_confusion_matrix.tex` |\n| G | Classifier Sensitivity | `app:classifier` | `appendix_classifier.tex` |\n| H | Human-Edit Robustness | `app:human-edit` | `appendix_human_edit.tex` |\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 6.1 | All appendix files exist | ✅ | All 8 files present |\n| 6.2 | Sampling Sensitivity sub-section | ⚠️ | `app:sampling-sensitivity` is a `\\subsection*` inside Appendix G (`appendix_classifier.tex:32`). The label resolves to the parent section. Cross-refs from `discussion.tex:9` and `limitations.tex:27` will point to Appendix G, not the subsection header. Consider promoting to its own appendix section if precise cross-referencing is needed. |\n\n---\n\n## 7. ACL/EMNLP Format\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 7.1 | Document class | ✅ | `\\documentclass[11pt]{article}` |\n| 7.2 | ACL style package | ✅ | `\\usepackage[review]{acl}` — review mode enables anonymization + line numbers |\n| 7.3 | Bibliography style | ✅ | `\\bibliography{references}` — `acl.sty` sets `acl_natbib` style automatically |\n| 7.4 | Required packages | ✅ | `times`, `latexsym`, `graphicx`, `booktabs`, `amsmath` all loaded |\n| 7.5 | `acl.sty` in submission | ⚠️ | **Verify `acl.sty` (2023 version) is included in the submission directory or available. Not found in the paper directory — must be added.** |\n\n---\n\n## 8. Summary\n\n| Category | ✅ Pass | ❌ Fail | ⚠️ Verify |\n|----------|---------|---------|-----------|\n| Anonymization | 6 | 1 | 1 |\n| Page count | — | — | 1 |\n| Required sections | 9 | 0 | 0 |\n| References | 4 | 0 | 1 |\n| Figures/Tables | 2 | 0 | 2 |\n| Appendix | 1 | 0 | 1 |\n| Format | 4 | 0 | 1 |\n| **Total** | **26** | **1** | **6** |\n\n### Action Items (must fix)\n\n1. **❌ Remove `_backup/` directory** from submission package (`paper/_backup/` — 24 stale .tex files, some containing `\\cite{placeholder}`)\n\n### Action Items (verify before submission)\n\n1. **⚠️ Compile PDF and check page count** — estimated 7–9 pages, must be ≤ 8. If over, trim Discussion (86 lines, most expendable).\n2. **⚠️ Check PDF metadata** after compilation — ensure no author/creator info leaks via `pdfinfo`.\n3. **⚠️ Include `acl.sty`** — the ACL 2023 style file must be present in the submission directory.\n4. **⚠️ Clean up unused figures** — `fig2_logo_performance.png`, `fig4_downstream_negative.*` in `chart/`.\n5. **⚠️ `app:sampling-sensitivity` cross-ref precision** — currently a `\\subsection*` inside Appendix G; consider promoting to its own appendix.\n6. **⚠️ Fill missing bib metadata** for camera-ready (page numbers, DOIs for some entries).\n"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-16T03:09:05.534737+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/emnlp_submission_checklist.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-16T03:09:05.534860+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "EMNLP 2026 ARR Submission Checklist",
  "type": "report",
  "description": "Pre-flight checklist for EMNLP 2026 ARR submission: anonymization, page count, required sections, references, figures, appendix, and ACL format verification. 26 pass, 1 fail (backup dir), 6 need human verification.",
  "project": "gen-depth-fingerprint",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/emnlp_submission_checklist.md",
  "tags": "['submission', 'emnlp2026', 'checklist']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "EMNLP 2026 ARR Submission Checklist",
    "type": "report",
    "description": "Pre-flight checklist for EMNLP 2026 ARR submission: anonymization, page count, required sections, references, figures, appendix, and ACL format verification. 26 pass, 1 fail (backup dir), 6 need human verification.",
    "project": "gen-depth-fingerprint",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/emnlp_submission_checklist.md",
    "tags": "['submission', 'emnlp2026', 'checklist']"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-16T03:09:05.535001+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_50b473\", \"name\": \"EMNLP 2026 ARR Submission Checklist\", \"type\": \"report\", \"description\": \"Pre-flight checklist for EMNLP 2026 ARR submission: anonymization, page count, required sections, references, figures, appendix, and ACL format verification. 26 pass, 1 fail (backup dir), 6 need human verification.\", \"path\": \"projects/gen-depth-fingerprint/artifacts/_project/report/emnlp_submission_checklist.md\", \"url\": null, \"project\": \"gen-depth-fingerprint\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T03:08:56.996261+00:00\", \"tags\": [\"submission\", \"emnlp2026\", \"checklist\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-16T03:09:05.535156+00:00_

Checklist 写入 `artifacts/emnlp_submission_checklist.md` 并已注册。

**结果**：26 项通过，1 项必须修复，6 项需人工确认。

**必须修复**：
- `paper/_backup/` 目录必须从提交包中删除（含 24 个过期 .tex，部分有 `\cite{placeholder}`）

**需编译验证**：
- 页数估计 7–9 页，必须编译确认 ≤ 8 页（Discussion 86 行是首选裁减对象）
- PDF metadata 无作者信息泄露
- `acl.sty` 需包含在提交目录中
- `chart/` 下有 3 个未引用图片文件可清理
- `app:sampling-sensitivity` 是 Appendix G 的 `\subsection*`，交叉引用指向父节点而非子标题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_emnlp-submission-prep_20260516T030521"
}
```

</details>

---
