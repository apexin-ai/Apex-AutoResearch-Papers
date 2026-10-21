# audit ref verify B

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 175
- **Recorded user turns:** 0
- **Tool calls:** 87
- **Original source:** `logs/chats/worker_audit_ref_verify_B_20260526T105303.jsonl`
- **Structured JSON:** [`4e4a1a2d6fed16013daf.json`](../../sessions/4e/4e4a1a2d6fed16013daf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

175 recorded events

### Tool call

_source line 1 · 2026-05-26T11:05:41.388097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T11:05:41.388537+00:00_

1	% References for Cross-Lingual Knowledge Conflict paper
2	
3	@inproceedings{pimentel2021probing,
4	  author    = {Pimentel, Tiago and Cotterell, Ryan},
5	  title     = {A {B}ayesian Framework for Information-Theoretic Probing},
6	  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
7	  year      = {2021},
8	  pages     = {2869--2887},
9	  publisher = {Association for Computational Linguistics},
10	}
11	
12	@inproceedings{ravichander2021probing,
13	  author    = {Ravichander, Abhilasha and Belinkov, Yonatan and Hovy, Eduard},
14	  title     = {Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?},
15	  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics},
16	  year      = {2021},
17	  pages     = {3331--3350},
18	  publisher = {Association for Computational Linguistics},
19	}
20	
21	@article{gurgurov2026clasbench,
22	  author    = {Gurgurov, Daniil and Al Ghussin, Yusser and Baeumel, Tanja and Chou, Cheng-Ting and Schramowski, Patrick and Mosbach, Marius and van Genabith, Josef and Ostermann, Simon},
23	  title     = {{CLaS-Bench}: A Cross-Lingual Alignment and Steering Benchmark},
24	  journal   = {arXiv preprint arXiv:2601.08331},
25	  year      = {2026},
26	}
27	
28	@article{basu2026interpretability,
29	  author    = {Basu, Sanjay and Patel, Sadiq Y. and Sheth, Parth and Muralidharan, Bhairavi and Elamaran, Namrata and Kinra, Aakriti and Morgan, John and Batniji, Rajaie},
30	  title     = {Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations},
31	  journal   = {arXiv preprint arXiv:2603.18353},
32	  year      = {2026},
33	  url       = {https://arxiv.org/abs/2603.18353}
34	}
35	
36	@article{brink2026probing,
37	  author    = {Brink, I. and Boer, A. and Ulmer, D.},
38	  title     = {Probing for Knowledge Attribution in Large Language M
…[truncated 14921 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T11:05:41.388814+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T11:05:41.388996+00:00_

docs/paper/limitations.tex
docs/paper/related_work.tex
docs/paper/main.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T11:05:41.389154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T11:05:41.389334+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{subcaption}
16	
17	\title{English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries}
18	
19	\author{Anonymous ACL submission}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	
30	\input{related_work}
31	
32	\input{method}
33	
34	\input{experiments}
35	
36	\input{discussion}
37	
38	\input{conclusion}
39	
40	\input{limitations}
41	
42	\bibliography{references}
43	
44	\appendix
45	
46	\section{Fine-Grained Causal Boundary Analysis}
47	\label{app:boundary}
48	
49	Table~\ref{tab:boundary} reports steering results across the full layer gradient from an independent replication ($N = 201$, Llama-3.1-8B-Instruct, RTX PRO 6000).
50	
51	\begin{table}[!t]
52	\centering
53	\caption{Causal boundary steering results (independently sampled, $N = 201$, Llama-3.1-8B-Instruct). Bonf.\ Sig.\ $\alpha$s: number of $\alpha$ values reaching significance after Bonferroni correction out of 6 tested.}
54	\label{tab:boundary}
55	\small
56	\resizebox{\columnwidth}{!}{%
57	\begin{tabular}{lcccccc}
58	\toprule
59	Layer & Depth & Probe Acc & Best $\alpha$ & Best Fisher $p$ & Bonf.\ Sig.\ $\alpha$s & Result \\
60	\midrule
61	L12 & 38\% & 91.75\% & $+20$ & 0.085 & 0/6 & --- \\
62	\textbf{L13} & \textbf{41\%} & \textbf{90.00\%} & $\mathbf{+10}$ & $\mathbf{<0.001}$ & \textbf{2/6} & $\checkmark\checkmark$ \\
63	L14 & 44\% & 91.75\% & $+10$ & 0.002 & 1/6 & $\checkmark$ \\
64	L16 & 50\% & 91.50\% & $+10$ & 0.005 & 1/6 & $\checkmark$ \\
65	L18 & 56\% & 90.75\% & $+5$ & 0.010 & 0/6 & --- \\
66	L28 & 88\% & 85.25\% & $+10$ & 0.284 & 0/6 & --- \\
67	\bottomrule
68	\
…[truncated 4601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T11:05:41.389493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T11:05:41.389626+00:00_

1	When multilingual large language models encounter conflicting information between languages, presentation language can determine the answer, but the internal mechanism remains unknown. We probe residual streams in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT on English--Chinese conflicts, combining cross-lingual transfer, Cross-lingual Natural Language Inference (XNLI) non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across both languages, and cross-lingual transfer exhibits a directional asymmetry: Chinese-trained probes transfer to English ${\sim}$7 percentage points more accurately than the reverse, matching the XNLI baseline and consistent with general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision: the probe signal is broadly distributed across mid-to-upper layers, yet representation steering achieves causal influence only at a mid-layer (L13, 41\% depth) in Llama; analogous Qwen and Gemma steering yields no significant effect. These findings indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention\footnote{Code and data are available at \url{https://anonymous.4open.science/r/clkc_mech_interp-F894/}.}.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T11:05:41.389754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T11:05:41.389912+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{fig1_hero.pdf}
7	\caption{Cross-lingual knowledge conflict in multilingual LLMs. When a context passage contradicts the model's parametric knowledge, the language of presentation (English vs.\ Chinese) can bias the answer toward different sources. We ask three questions: (1)~Is the conflict signal linearly detectable in the residual stream? (2)~Do probes transfer across languages, and is the transfer symmetric? (3)~Does detection imply causal influence on resolution?}
8	\label{fig:hero}
9	\end{figure*}
10	
11	When multilingual large language models (LLMs) encounter conflicting information between languages, the language of presentation can determine which answer the model produces \citep{zhao2026when}.
12	Yet the internal mechanism remains opaque: how does the model encode the conflict signal, can it be detected from internal representations, and does the detected signal causally influence resolution?
13	
14	Existing work on probing conflict signals has been limited to monolingual settings \citep{zhao2024analysing, brink2026probing}.
15	Extending cross-lingually introduces confounds (translation quality, token overlap, general transfer properties), and probing establishes correlation rather than causation \citep{hewitt2019designing}; \citet{basu2026interpretability} showed that near-perfect probe accuracy does not guarantee effective steering.
16	
17	Our work extends \citet{zhao2024analysing} in four directions: (1)~cross-lingual expansion from monolingual English to EN-ZH conflict probing; (2)~a systematic confound exclusion pipeline; (3)~the XNLI baseline revealing that asymmetry parallels general cross-lingual structure; and (4)~three-model causal intervention demonstrating that detectability does not predict causal relevance.
18	We combine residual stream probing with representation steering across Llama-3.1-8B-Instruct, Qwen3-8B, and Gem
…[truncated 2007 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T11:05:41.390066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T11:05:41.390210+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Knowledge conflict detection.}
5	\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent resolution strategies, and \citet{xu2024knowledge} provided a systematic conflict taxonomy (intra-memory, context-memory, inter-context).
6	Moving beyond behavioral observation, \citet{zhao2024analysing} demonstrated linearly separable conflict signals in English residual streams, and \citet{brink2026probing} localized factual associations via probing. More recently, \citet{pham2026where} traced intra-memory conflict pathways, while \citet{li2025taming} proposed conflict mitigation methods.
7	Information-theoretic approaches \citep{pimentel2021probing} offer complementary perspectives on probe expressiveness, and \citet{ravichander2021probing} raised concerns about whether probed information is task-relevant.
8	These studies operate exclusively in monolingual settings; extending to cross-lingual scenarios introduces confounds (translation quality, token overlap, general transfer properties) that we address with a dedicated exclusion pipeline.
9	
10	\paragraph{Cross-lingual representations in multilingual models.}
11	Intermediate layers develop language-independent representations: \citet{wu2020emerging} showed cross-lingual structure emerges without explicit alignment, and \citet{muller2021first} found mid-layer alignment in multilingual BERT.
12	For decoder-only LLMs, \citet{wendler2024llamas} showed that Llama processes non-English inputs through an English-centric latent space, and \citet{kargaran2024mexa} quantified this bias across language pairs.
13	These findings predict our empirical observations: mid-layer steering success aligns with intermediate-layer language alignment, and the ZH$\to$EN transfer advantage reflects English-centric structure.
14	Behavioral consequences have been documented by \citet{wang2025lost}, \citet{zhao2026when} (CLEAR cross-lingual conflic
…[truncated 1836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T11:05:41.390355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T11:05:41.390518+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\vspace{-18pt}
7	\includegraphics[width=0.88\textwidth]{fig2_pipeline.pdf}
8	\vspace{-14pt}
9	\caption{Method overview. We construct parallel EN/ZH conflict data from ConflictQA with COMET-validated translations, extract per-layer residual stream representations, train logistic regression probes in four transfer directions (EN$\to$EN, ZH$\to$ZH, EN$\to$ZH, ZH$\to$EN), and apply confound exclusion controls before causal steering validation.}
10	\label{fig:pipeline}
11	\vspace{-20pt}
12	\end{figure*}
13	
14	Our pipeline proceeds from data construction through probing and steering (Figure~\ref{fig:pipeline}), formalized below.
15	
16	\subsection{Task Formulation}
17	\label{sec:task}
18	
19	Given a context passage $c$ and question $q$, the model produces an answer that is either \emph{contextual} (derived from $c$) or \emph{parametric} (from pre-trained knowledge).
20	When $c$ contradicts parametric knowledge, the choice constitutes a knowledge conflict.
21	We train a logistic regression probe $f_\theta(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)$ on the last-token residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$ to predict a binary label $y \in \{\text{contextual}, \text{parametric}\}$.
22	
23	\subsection{Data Construction}
24	\label{sec:data}
25	
26	We build on ConflictQA \citep{xie2024adaptive}, which pairs questions with context passages contradicting the model's parametric knowledge.
27	We filter samples by querying each model without context and retaining only those answered correctly, yielding 1{,}368 samples for Llama \citep{grattafiori2024llama}, 966 for Qwen \citep{yang2025qwen3}, and 1{,}590 for Gemma \citep{team2024gemma} (80/20 train/test split with stratification).
28	For cross-lingual transfer, we translate all inputs into Chinese using a Qwen3-8B pipeline, with quality validated by COMET (Crosslingual Optimized Metric for Evaluation 
…[truncated 4993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T11:05:41.390659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T11:05:41.390906+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \citep{team2024gemma}.
9	The three models were independently verified on ConflictQA \citep{xie2024adaptive}, yielding only 3.5\% three-way question overlap (23 questions); pairwise overlaps range from 7.2\% (Llama $\cap$ Gemma) to 24.8\% (Gemma $\cap$ Qwen), so the consistent asymmetry pattern constitutes largely independent replication.
10	
11	\paragraph{Dataset and translation.}
12	After parametric knowledge verification (\S\ref{sec:data}), we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 / 193), and 1{,}590 for Gemma (1{,}274 / 316), split 80/20 with stratification.
13	All inputs are translated into Chinese using COMET-validated translations (\S\ref{sec:data}).
14	
15	\paragraph{Probing.}
16	For each layer, we train an $L_2$-regularized logistic regression probe on the last-token residual stream (\S\ref{sec:extraction}).
17	We report balanced accuracy rather than AUROC, as our claims depend on cross-model directional comparisons; AUROC results are in Appendix~\ref{app:auroc}.
18	All CIs are computed via bootstrap resampling with paired differences for asymmetry estimation.
19	A selectivity control \citep{hewitt2019designing} with permuted labels on matched-condition data ($N{=}131$--$201$) yields near-chance accuracy (49.2--51.0\%) across all models, confirming selectivity gaps of 21--40~pp.
20	All experiments used a single GPU; the boundary replication (Appendix~\ref{app:boundary}) used an NVIDIA RTX PRO 6000.
21	
22	\paragraph{Non-conflict baseline.}
23	To test whether cross-lingual transfer pat
…[truncated 15473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T11:05:41.391080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T11:05:41.391216+00:00_

1	\vspace{-6pt}
2	\section{Discussion}
3	\label{sec:discussion}
4	\vspace{-4pt}
5	
6	\paragraph{Causal influence is localized to L13 regardless of detection peak.}
7	In Llama, causal influence is localized to L13 (41\% depth; Fisher $p < 0.001$), near but distinct from the linear probe peak (L15, 47\%) and MLP probe peak (L18, 56\%), with upper-layer interventions producing no significant change ($p > 0.3$; Figure~\ref{fig:dissociation}).
8	L13 coincides with cross-lingual alignment sites \citep{muller2021first, wendler2024llamas}, suggesting mid-layers serve a dual role in alignment and conflict resolution.
9	The dissociation evidence is strongest for Gemma, where 88.9\% probe accuracy and 0.93 AUROC coexist with zero steering effects, ruling out probe quality as a confound; for Qwen, weaker probe performance (71.4\%) leaves the null result more ambiguous.
10	
11	\paragraph{Why does steering fail in Qwen and Gemma?}
12	Three hypotheses merit consideration: (1)~non-linear causal interactions \citep{elhage2022toy}, where MLP probes gain $+9.2$~pp over linear probes on conflict but $-0.5$~pp on XNLI; (2)~superposition \citep{templeton2024scaling}, where conflict and XNLI weight vectors are near-orthogonal yet cross-task language transfer is near-perfect; (3)~architectural differences, as Qwen and Gemma show mid-layer transfer dips absent in Llama.
13	Definitive validation requires activation patching \citep{meng2022locating}.
14	The ZH$\to$EN advantage matches the XNLI baseline across all models, indicating asymmetry piggybacks on general cross-lingual alignment \citep{zhao2026when, kargaran2024mexa, wendler2024llamas}; \citet{basu2026interpretability} reported steering failure despite 98.2\% AUROC, while our L13 succeeds via mid-layer steering and three-model architectural isolation.
15	
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T11:05:41.391349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T11:05:41.391471+00:00_

1	\vspace{-8pt}
2	\section{Conclusion}
3	\label{sec:conclusion}
4	\vspace{-4pt}
5	
6	We showed that knowledge conflict signals are linearly detectable across English and Chinese ($p < 0.001$, three architectures), with the ZH$\to$EN transfer advantage (${\sim}$7~pp) matching the XNLI baseline, indicating general cross-lingual alignment rather than conflict-specific encoding.
7	Causal intervention reveals a detection--decision dissociation: all three models detect conflict signals, yet only Llama yields significant steering at L13 ($p < 0.001$); Gemma fails despite 88.9\% probe accuracy, confirming detection does not entail causation.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T11:05:41.391598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-26T11:05:41.391731+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our study has three main limitations.
5	First, we evaluate only one language pair (English-Chinese) and causal steering succeeded only in Llama at L13; Gemma L17 failed despite 88.9\% probe accuracy ($n = 171$) and Qwen L14 ($n = 131$) was also negative.
6	Typologically diverse language pairs and alternative intervention methods are needed to assess generality.
7	Null steering results in Qwen and Gemma may reflect limitations of single-direction linear steering rather than absence of causal structure; alternative methods such as activation patching \citep{meng2022locating} may reveal non-linear causal pathways that our approach cannot detect.
8	Second, the effective dataset size (966 to 1,590 samples per model) is constrained by parametric knowledge verification, which retains only questions where the model confidently knows the ground truth and may bias toward well-represented knowledge; additionally, Qwen3-8B serves as both the translation model and an experimental subject, though COMET-based quality control mitigates this concern, and the fact that Llama and Gemma, architecturally independent of the translation model, show the same asymmetry pattern ($\Delta_{\text{asym}} = +7.3$ and $+6.6$~pp, respectively) provides cross-validation that the effect is not an artifact of Qwen-specific translation biases.
9	Third, all probing results are based on a single train/test split with bootstrap confidence intervals capturing within-split variability; while peak balanced accuracy remains stable across seeds (Llama $\pm$0.12\%, Gemma $\pm$1.32\%, Qwen $\pm$1.90\%), the specific peak layer can shift.
10	We acknowledge that $k$-fold cross-validation would provide stronger stability guarantees \citep{belinkov2022probing}; given that our core claims rest on cross-model consistency and directional patterns rather than exact accuracy values, the current cross-seed stability analysis provides partial mitigation, and we commit
…[truncated 191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T11:05:41.391970+00:00_

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
  "session": "worker_audit_ref_verify_B_20260526T105303",
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

_source line 24 · 2026-05-26T11:05:41.392113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T11:05:41.392257+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pimentel Cotterell \"A Bayesian Framework for Information-Theoretic Probing\" EMNLP 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pimentel Cotterell \"A Bayesian Framework for Information-Theoretic Probing\" EMNLP 2021"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T11:05:41.392379+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ravichander Belinkov Hovy \"Probing the Probing Paradigm\" EACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ravichander Belinkov Hovy \"Probing the Probing Paradigm\" EACL 2021"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T11:05:41.392502+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gurgurov \"CLaS-Bench Cross-Lingual Alignment and Steering Benchmark\" arXiv 2601.08331"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gurgurov \"CLaS-Bench Cross-Lingual Alignment and Steering Benchmark\" arXiv 2601.08331"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T11:05:41.392631+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Basu Patel \"Interpretability without Actionability\" arXiv 2603.18353"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Basu Patel \"Interpretability without Actionability\" arXiv 2603.18353"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T11:05:41.392764+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Brink Boer Ulmer \"Probing for Knowledge Attribution in Large Language Models\" arXiv 2602.22787"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Brink Boer Ulmer \"Probing for Knowledge Attribution in Large Language Models\" arXiv 2602.22787"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T11:05:41.392934+00:00_

Web search results for query: "Pimentel Cotterell "A Bayesian Framework for Information-Theoretic Probing" EMNLP 2021"

Links: [{"title":"A Bayesian Framework for Information-Theoretic Probing - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.229/"},{"title":"A Bayesian Framework for Information-Theoretic Probing - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210903853P/abstract"},{"title":"[2109.03853] A Bayesian Framework for Information-Theoretic Probing","url":"https://arxiv.org/abs/2109.03853"},{"title":"A Bayesian Framework for Information-Theoretic Probing - Tiago Pimentel","url":"https://tpimentelms.github.io/publication/2021-11-10-bayesian-information-theory"},{"title":"A Bayesian Framework for Information-Theoretic Probing Tiago Pimentel","url":"https://rycolab.io/papers/pimentel+cotterell.emnlp21.pdf"},{"title":"A Bayesian Framework for Information-Theoretic Probing","url":"https://aclanthology.org/2021.emnlp-main.229.pdf"},{"title":"A Bayesian Framework for Information-Theoretic Probing | Rycolab","url":"https://rycolab.io/emnlp21/pimentelcotterell-emnlp-21/"},{"title":"Papers with Code - A Bayesian Framework for Information-Theoretic Probing","url":"https://paperswithcode.com/paper/a-bayesian-framework-for-information"},{"title":"[2109.03853v1] A Bayesian Framework for Information-Theoretic Probing","url":"https://arxiv.org/abs/2109.03853v1"},{"title":"CV - Tiago Pimentel","url":"https://tpimentelms.github.io/cv/"}]

I found the paper you're looking for. Here's the information:

"A Bayesian Framework for Information-Theoretic Probing" by Tiago Pimentel and Ryan Cotterell was published in the Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (pages 2869–2887), held online and in Punta Cana, Dominican Republic.

The paper proposes a new framework to measure what is termed Bayesian mutual information, which analyses information from the perspective of Bayesian agents -- allowing for more intuiti
…[truncated 773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T11:05:41.393112+00:00_

Web search results for query: "Gurgurov "CLaS-Bench Cross-Lingual Alignment and Steering Benchmark" arXiv 2601.08331"

Links: [{"title":"[2601.08331] CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/abs/2601.08331"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/html/2601.08331v1"},{"title":"Multilingual Steering by Design: Multilingual Sparse Autoencoders and Principled Layer Selection","url":"https://arxiv.org/html/2605.23036"},{"title":"CLM-Bench: Benchmarking and Analyzing Cross-lingual Misalignment of LLMs in Knowledge Editing","url":"https://arxiv.org/html/2601.17397v1"},{"title":"[2601.16390] Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/abs/2601.16390"},{"title":"[2605.23036] Multilingual Steering by Design: Multilingual Sparse Autoencoders and Principled Layer Selection","url":"https://arxiv.org/abs/2605.23036"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/html/2601.16390v1"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/html/2502.15639v1"},{"title":"Bias Beyond Borders: Political Ideology Evaluation and Steering in Multilingual LLMs","url":"https://arxiv.org/html/2601.23001"},{"title":"[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/abs/2502.15639"}]

I found the paper you're looking for! Here's what I found about it:

CLaS-Bench is authored by Daniil Gurgurov, Yusser Al Ghussin, Tanja Baeumel, Cheng-Ting Chou, Patrick Schramowski, Marius Mosbach, Josef van Genabith, and Simon Ostermann.

CLaS-Bench is a lightweight parallel-question benchmark for evaluating language-forcing behavior in LLMs across 32 languages, enabling sys
…[truncated 631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T11:05:41.393300+00:00_

Web search results for query: "Basu Patel "Interpretability without Actionability" arXiv 2603.18353"

Links: [{"title":"[2603.18353] Interpretability without actionability","url":"https://arxiv.org/abs/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods ...","url":"https://arxiv.org/pdf/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://arxiv.org/html/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.18353"},{"title":"(PDF) Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://www.researchgate.net/publication/402859588_Interpretability_without_actionability_mechanistic_methods_cannot_correct_language_model_errors_despite_near-perfect_internal_representations"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Gist.Science","url":"https://gist.science/paper/2603.18353"},{"title":"Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models by Sanjay Basu, Sadiq Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, John Morgan, Rajaie Batniji :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6437137"}]

I found the paper you're looking for. Here's what I found:

**Paper Details:**

The paper is titled "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations", authored by Sanjay Basu, Sadiq Y. Patel, Parth Sheth, Bhai
…[truncated 1218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-26T11:05:41.393472+00:00_

Web search results for query: "Brink Boer Ulmer "Probing for Knowledge Attribution in Large Language Models" arXiv 2602.22787"

Links: [{"title":"[2602.22787] Probing for Knowledge Attribution in Large Language Models","url":"https://arxiv.org/abs/2602.22787"},{"title":"Probing for Knowledge Attribution in Large Language Models","url":"https://arxiv.org/html/2602.22787"},{"title":"Probing for Knowledge Attribution in Large Language Models","url":"https://arxiv.org/pdf/2602.22787"},{"title":"A Survey of Large Language Models Attribution","url":"https://arxiv.org/pdf/2311.03731"},{"title":"Document Attribution: Examining Citation Relationships using Large Language Models","url":"https://arxiv.org/pdf/2505.06324"}]

I found the paper you were looking for! Here are the key details:

**Paper Title:** Probing for Knowledge Attribution in Large Language Models

**Authors:** Ivo Brink, Alexander Boer, Dennis Ulmer

**arXiv ID:** 2602.22787

**Submission Date:** February 26, 2026

**Overview:**
Large language models (LLMs) often generate fluent but unfounded claims, or hallucinations, which fall into two types: (i) faithfulness violations - misusing user context - and (ii) factuality violations - errors from internal knowledge. This work focuses on the problem of contributive attribution: identifying the dominant knowledge source behind each output.

**Main Contribution:**
A probe, a simple linear classifier trained on model hidden representations, can reliably predict contributive attribution. For its training, the authors introduce AttriWiki, a self-supervised data pipeline that prompts models to recall withheld entities from memory or read them from context, generating labelled examples automatically.

**Results:**
Probes trained on AttriWiki data achieve up to 0.96 Macro-F1 on Llama-3.1-8B, Mistral-7B, and Qwen-7B, transferring to out-of-domain benchmarks (SQuAD, WebQuestions) with 0.94-0.99 Macro-F1 without retraining.

The paper is available on arXiv at https://arxiv.o
…[truncated 121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-26T11:05:41.393653+00:00_

Web search results for query: "Ravichander Belinkov Hovy "Probing the Probing Paradigm" EACL 2021"

Links: [{"title":"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance? - ACL Anthology","url":"https://aclanthology.org/2021.eacl-main.295/"},{"title":"[PDF] Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Probing-the-Probing-Paradigm:-Does-Probing-Accuracy-Ravichander-Belinkov/a4c0c16da0caaf4ed47fe94681f57029bff4be3b"},{"title":"Squib Probing Classiﬁers: Promises, Shortcomings, and Advances","url":"https://aclanthology.org/2022.cl-1.7.pdf"},{"title":"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?","url":"https://belinkov.com/assets/pdf/eacl2021.pdf"},{"title":"Squib Probing Classiﬁers: Promises, Shortcomings, and Advances","url":"https://belinkov.com/assets/pdf/cl2021.pdf"},{"title":"Does Probing Accuracy Entail Task Relevance?","url":"https://aclanthology.org/2021.eacl-main.295.pdf"},{"title":"Main Conference Accepted Papers - EACL 2021","url":"https://2021.eacl.org/program/accepted/"},{"title":"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance? | Request PDF","url":"https://www.researchgate.net/publication/355434387_Probing_the_Probing_Paradigm_Does_Probing_Accuracy_Entail_Task_Relevance"},{"title":"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200500719R/abstract"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/pdf/2102.12452"}]

I found the paper you're looking for! Here are the key details:

"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?" was published by Abhilasha Ravichander, Yonatan Belinkov, and Eduard Hovy in the Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2021), pag
…[truncated 984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T11:05:41.393864+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ifergan Choshen \"Beneath the Surface of Consistency\" cross-lingual knowledge LLMs arXiv 2408.10646"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ifergan Choshen \"Beneath the Surface of Consistency\" cross-lingual knowledge LLMs arXiv 2408.10646"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-26T11:05:41.394008+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li Chen Tong \"Taming Knowledge Conflicts in Language Models\" ICML 2025 arXiv 2503.10996"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li Chen Tong \"Taming Knowledge Conflicts in Language Models\" ICML 2025 arXiv 2503.10996"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T11:05:41.394130+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pham Borkakoty Hou \"Where Knowledge Collides\" mechanistic intra-memory arXiv 2601.09445"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pham Borkakoty Hou \"Where Knowledge Collides\" mechanistic intra-memory arXiv 2601.09445"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T11:05:41.394247+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Adel Lange \"Lost in Multilinguality\" cross-lingual factual inconsistency arXiv 2504.04264"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Adel Lange \"Lost in Multilinguality\" cross-lingual factual inconsistency arXiv 2504.04264"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T11:05:41.394361+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xie Zhang Chen \"Adaptive Chameleon or Stubborn Sloth\" knowledge conflicts ICLR 2024 arXiv 2305.13300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie Zhang Chen \"Adaptive Chameleon or Stubborn Sloth\" knowledge conflicts ICLR 2024 arXiv 2305.13300"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T11:05:41.394502+00:00_

Web search results for query: "Li Chen Tong "Taming Knowledge Conflicts in Language Models" ICML 2025 arXiv 2503.10996"

Links: [{"title":"[2503.10996] Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/abs/2503.10996"},{"title":"Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/pdf/2503.10996"},{"title":"ICML Poster Taming Knowledge Conflicts in Language Models","url":"https://icml.cc/virtual/2025/poster/46677"},{"title":"Computation and Language Mar 2025","url":"https://arxiv.org/list/cs.CL/2025-03?skip=700&show=2000"},{"title":"Taming Knowledge Conflicts in Language Models","url":"https://proceedings.mlr.press/v267/li25c.html"},{"title":"Computation and Language Feb 2025","url":"https://arxiv.org/list/cs.CL/2025-02?skip=1500&show=1000"},{"title":"Resolving Knowledge Conflicts in Large Language Models","url":"https://arxiv.org/pdf/2310.00935"}]

I found the paper! Here's what I can tell you about it:

**Paper Title:** "Taming Knowledge Conflicts in Language Models"

**Authors:** Gaotang Li, Yuzhong Chen, Hanghang Tong

**Publication:** Proceedings of the 42nd International Conference on Machine Learning, PMLR 267:34074-34104, 2025

**arXiv Identifier:** 2503.10996

**Conference Status:** ICML 2025 (Spotlight)

**Main Contribution:** The paper uncovers a critical phenomenon of superposition of contextual information and parametric memory, where highly influential attention heads simultaneously contribute to both. The authors propose Just Run Twice (JuICE), a test-time attention intervention method that steers LMs toward either parametric beliefs or contextual knowledge without requiring fine-tuning.

The paper is available at https://arxiv.org/abs/2503.10996 and also published in the ICML proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-26T11:05:41.394668+00:00_

Web search results for query: "Wang Adel Lange "Lost in Multilinguality" cross-lingual factual inconsistency arXiv 2504.04264"

Links: [{"title":"[2504.04264] Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models","url":"https://arxiv.org/abs/2504.04264"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models","url":"https://arxiv.org/html/2504.04264v1"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.253/"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models | Request PDF","url":"https://www.researchgate.net/publication/390569381_Lost_in_Multilinguality_Dissecting_Cross-lingual_Factual_Inconsistency_in_Transformer_Language_Models"},{"title":"AdaMCoT: Rethinking Cross-Lingual Factual Reasoning through Adaptive Multilingual Chain-of-Thought","url":"https://arxiv.org/html/2501.16154v3"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models","url":"https://www.catalyzex.com/paper/lost-in-multilinguality-dissecting-cross"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency   in Transformer Language Models","url":"https://arxiv.org/pdf/2504.04264"}]

I found the research paper you're looking for. Here's what I found:

**Paper Details:**

The paper "Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models" (arXiv 2504.04264) is authored by Mingyang Wang, Heike Adel, Lukas Lange, Yihong Liu, Ercong Nie, Jannik Strötgen, and Hinrich Schütze.

**Key Findings:**

Multilingual language models (MLMs) store factual knowledge across languages but often struggle to provide consistent responses to semantically equivalent prompts in different languages. The r
…[truncated 871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-26T11:05:41.394834+00:00_

Web search results for query: "Pham Borkakoty Hou "Where Knowledge Collides" mechanistic intra-memory arXiv 2601.09445"

Links: [{"title":"Where Knowledge Collides: A Mechanistic Study of Intra-Memory","url":"https://arxiv.org/pdf/2601.09445"},{"title":"[2601.09445] Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models","url":"https://arxiv.org/abs/2601.09445"},{"title":"Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models","url":"https://arxiv.org/html/2601.09445"},{"title":"Cutting Off the Head Ends the Conflict: A Mechanism for Interpreting and   Mitigating Knowledge Conflicts in Language Models","url":"https://arxiv.org/pdf/2402.18154"},{"title":"Attention Is Not Retention: The Orthogonality Constraint in Infinite-Context Architectures","url":"https://arxiv.org/pdf/2601.15313"},{"title":"Facts as First Class Objects: Knowledge Objects for Persistent LLM Memory","url":"https://arxiv.org/pdf/2603.17781"},{"title":"DYNAMICQA: Tracing Internal Knowledge Conflicts in Language Models","url":"https://arxiv.org/pdf/2407.17023"}]

I found the paper! Here's what the search results show:

The paper "Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models" was submitted on January 14, 2026, and is authored by Minh Vu Pham, Hsuvas Borkakoty, and Yufang Hou (arXiv:2601.09445).

The paper addresses intra-memory knowledge conflict, which largely arises when inconsistent information about the same event is encoded within a language model's parametric knowledge. The authors design a framework based on mechanistic interpretability methods to identify where and how conflicting knowledge from the pre-training data is encoded within language models.

To study this, they construct a curated dataset called SynWikiBio, consisting of Wikipedia-style biographies for synthetic entities that deliberately contain conflicting knowledge (e.g., a person's grad
…[truncated 183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-26T11:05:41.395033+00:00_

Web search results for query: "Xie Zhang Chen "Adaptive Chameleon or Stubborn Sloth" knowledge conflicts ICLR 2024 arXiv 2305.13300"

Links: [{"title":"[2305.13300] Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts","url":"https://arxiv.org/abs/2305.13300"},{"title":"Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230513300X/abstract"},{"title":"Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts | OpenReview","url":"https://openreview.net/forum?id=auKAUJZMO6"},{"title":"Adaptive Chameleon or Stubborn Sloth: Unraveling the Behavior of Large Language Models in Knowledge Clashes","url":"https://ai.updf.com/paper-detail/adaptive-chameleon-or-stubborn-sloth-unraveling-the-behavior-of-large-xie-zhang-9815f586f329a098df83ca872799880bd5cb1a15"},{"title":"Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts","url":"https://www.researchgate.net/publication/370949037_Adaptive_Chameleon_or_Stubborn_Sloth_Unraveling_the_Behavior_of_Large_Language_Models_in_Knowledge_Conflicts?_share=1"},{"title":"[PDF] Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Adaptive-Chameleon-or-Stubborn-Sloth:-Revealing-the-Xie-Zhang/10f829a80a7ee0cdb16307f04e206133d75f81da"},{"title":"Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/99261adc8a6356b38bcf999bba9a26dc-Abstract-Conference.html"},{"title":"Adaptive Chameleon or Stubborn Sloth:","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/99261adc8a6356b38bcf999bba9a26dc-Paper-Conference.pdf"},{"title":"GitH
…[truncated 1575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-26T11:05:41.395203+00:00_

Web search results for query: "Ifergan Choshen "Beneath the Surface of Consistency" cross-lingual knowledge LLMs arXiv 2408.10646"

Links: [{"title":"[2408.10646] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge","url":"https://arxiv.org/pdf/2408.10646"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/html/2408.10646v1"},{"title":"[2408.10646v1] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646v1"},{"title":"[PDF] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/54a2e0dad730c1a955c66f3568a3fa0dca400225"},{"title":"(PDF) Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://www.researchgate.net/publication/383266358_Beneath_the_Surface_of_Consistency_Exploring_Cross-lingual_Knowledge_Representation_Sharing_in_LLMs"},{"title":"[Literature Review] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://www.themoonlight.io/en/review/beneath-the-surface-of-consistency-exploring-cross-lingual-knowledge-representation-sharing-in-llms"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs | PromptLayer","url":"https://www.promptlayer.com/research-papers/beneath-the-surface-of-consistency-exploring-cross-lingual-knowledge-representation-sharing-in-llms"}]

I found the paper! Here are the details about this research:

**Title:** Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs

**Au
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T11:05:41.395400+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ifergan \"Beneath the Surface of Consistency\" first author name NAACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ifergan \"Beneath the Surface of Consistency\" first author name NAACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T11:05:41.395529+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "li2025taming \"Gaotang Li\" \"Yuzhong Chen\" OR \"Yufei Chen\" ICML 2025 taming knowledge conflicts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "li2025taming \"Gaotang Li\" \"Yuzhong Chen\" OR \"Yufei Chen\" ICML 2025 taming knowledge conflicts"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T11:05:41.395651+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pham \"Hrishav\" OR \"Hsuvas\" Borkakoty \"Where Knowledge Collides\" 2601.09445"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pham \"Hrishav\" OR \"Hsuvas\" Borkakoty \"Where Knowledge Collides\" 2601.09445"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-26T11:05:41.395769+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Adel Lange Liu Nie Strötgen Schütze \"Lost in Multilinguality\" ACL 2025 full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Adel Lange Liu Nie Strötgen Schütze \"Lost in Multilinguality\" ACL 2025 full author list"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-26T11:05:41.395908+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xing He Xu Wang \"Evaluating Knowledge-based Cross-lingual Inconsistency\" arXiv 2407.01358"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xing He Xu Wang \"Evaluating Knowledge-based Cross-lingual Inconsistency\" arXiv 2407.01358"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T11:05:41.396046+00:00_

Web search results for query: "Ifergan "Beneath the Surface of Consistency" first author name NAACL 2025"

Links: [{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.475/"},{"title":"Findings of the Association for Computational Linguistics:","url":"https://aclanthology.org/2025.findings-naacl.475.pdf"},{"title":"[PDF] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Beneath-the-Surface-of-Consistency:-Exploring-in-Ifergan-Choshen/54a2e0dad730c1a955c66f3568a3fa0dca400225"},{"title":"[2408.10646] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646"},{"title":"[2408.10646v1] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646v1"},{"title":"Computation and Language Aug 2024","url":"https://arxiv.org/list/cs.CL/2024-08?skip=540&show=2000"},{"title":"(PDF) Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://www.researchgate.net/publication/383266358_Beneath_the_Surface_of_Consistency_Exploring_Cross-lingual_Knowledge_Representation_Sharing_in_LLMs"}]

Based on the search results, the first author of the paper "Beneath the Surface of Consistency" is Maxim Ifergan. The paper was published in Findings of the Association for Computational Linguistics: NAACL 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T11:05:41.396194+00:00_

Web search results for query: "Wang Adel Lange Liu Nie Strötgen Schütze "Lost in Multilinguality" ACL 2025 full author list"

Links: [{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.253/"},{"title":"[2504.04264] Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models","url":"https://arxiv.org/abs/2504.04264"},{"title":"MCML - Mingyang Wang Receives Award at ACL 2025","url":"https://mcml.ai/news/2025-08-18-wang-sac-highlights-award/"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Schütze Lab - Publications","url":"https://cisnlp.github.io/publications/"},{"title":"Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.132/"},{"title":"Bring Your Own Knowledge: A Survey of Methods for LLM Knowledge Expansion - ACL Anthology","url":"https://aclanthology.org/2025.l2m2-1.12/"},{"title":"Mingyang Wang | LMU Munich, Bosch Center for Artificial Intelligence","url":"https://mingyang-wang26.github.io/"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models | Request PDF","url":"https://www.researchgate.net/publication/390569381_Lost_in_Multilinguality_Dissecting_Cross-lingual_Factual_Inconsistency_in_Transformer_Language_Models"}]

Based on the search results, here is the full author list for "Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models" at ACL 2025:

The authors are: Mingyang Wang, Heike Adel, Lukas Lange, Yihong Liu, Ercong Nie, Jannik Strötgen, and Hinrich Schuetze.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T11:05:41.396362+00:00_

Web search results for query: "Pham "Hrishav" OR "Hsuvas" Borkakoty "Where Knowledge Collides" 2601.09445"

Links: [{"title":"[2601.09445] Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models","url":"https://arxiv.org/abs/2601.09445"},{"title":"Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models","url":"https://arxiv.org/html/2601.09445"},{"title":"Hsuvas Borkakoty, Student at jorhat instt of science and technology","url":"https://www.slideshare.net/HsuvasBorkakoty"},{"title":"Hsuvas Borkakoty - Academia.edu","url":"https://independent.academia.edu/HsuvasBorkakoty"},{"title":"dblp: Hsuvas Borkakoty","url":"https://dblp.org/pid/258/4351.html"},{"title":"Home | Hsuvas Borkakoty","url":"https://hsuvas.wixsite.com/hsuvas"},{"title":"Hsuvas Borkakoty","url":"https://www.facebook.com/hsuvas/"},{"title":"hsuvaskakoty (Hsuvas Borkakoty)","url":"https://huggingface.co/hsuvaskakoty"},{"title":"Hsuvas Borkakoty - Quora","url":"https://www.quora.com/profile/Hsuvas-Borkakoty"}]

Based on the search results, I found the paper you were looking for:

The paper "Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models" (arXiv:2601.09445) was authored by Minh Vu Pham and Hsuvas Borkakoty (along with Yufang Hou).

The paper investigates intra-memory knowledge conflict in language models—where inconsistent information about the same event is encoded within the model's parametric knowledge—using a framework based on mechanistic interpretability methods to identify where and how conflicting knowledge from pre-training data is encoded.

The paper was submitted on January 14, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-26T11:05:41.396524+00:00_

Web search results for query: "li2025taming "Gaotang Li" "Yuzhong Chen" OR "Yufei Chen" ICML 2025 taming knowledge conflicts"

Links: [{"title":"GitHub - GaotangLi/JUICE: [ICML'25 Spotlight] Taming Knowledge Conflict in Language Models","url":"https://github.com/GaotangLi/JUICE"},{"title":"Gaotang Li","url":"https://gaotangli.github.io/"},{"title":"Taming Knowledge Conflicts in Language Models","url":"https://proceedings.mlr.press/v267/li25c.html"},{"title":"ICML Poster Taming Knowledge Conflicts in Language Models","url":"https://icml.cc/virtual/2025/poster/46677"},{"title":"[2503.10996] Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/abs/2503.10996"},{"title":"Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/html/2503.10996v2"},{"title":"ICML 2025 Program Committee - Meta Reviewer","url":"https://icml.cc/Conferences/2025/ProgramCommittee"}]

Based on the web search results, I found the paper you're looking for:

"Taming Knowledge Conflicts in Language Models" is authored by Gaotang Li, Yuzhong Chen, and Hanghang Tong, published at ICML 2025.

The paper addresses how language models often encounter knowledge conflicts when parametric memory contradicts contextual knowledge. The research uncovers a critical phenomenon called the superposition of contextual information and parametric memory, where highly influential attention heads simultaneously contribute to both memory and context.

The authors propose Just Run Twice (JuICE), a test-time attention intervention method that steers language models toward either parametric beliefs or contextual knowledge without requiring fine-tuning, and it identifies a set of reliable attention heads and leverages a dual-run approach to mitigate superposition effects. Extensive experiments across 11 datasets and 6 model architectures demonstrate that JuICE sets new state-of-the-art performance.

The paper's code is available on GitHub at https://github.com/GaotangLi/JUICE, and the full 
…[truncated 172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T11:05:41.396698+00:00_

Web search results for query: "Xing He Xu Wang "Evaluating Knowledge-based Cross-lingual Inconsistency" arXiv 2407.01358"

Links: [{"title":"[2407.01358] Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/abs/2407.01358"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2407.01358v1"},{"title":"dblp: Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2407-01358.html"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://www.researchgate.net/publication/381882496_Evaluating_Knowledge-based_Cross-lingual_Inconsistency_in_Large_Language_Models"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language   Models","url":"https://arxiv.org/pdf/2407.01358"}]

I found the paper! Here are the search results:

The paper "Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models" (arXiv 2407.01358) investigates cross-lingual inconsistencies in Large Language Models such as ChatGPT, Llama, and Baichuan, noting that despite their strong performance in NLP tasks, these models often exhibit significant inconsistencies when processing the same concepts across different languages.

The research addresses three primary questions about the existence of cross-lingual inconsistencies in LLMs, the specific aspects in which they manifest, and the correlation between cross-lingual consistency and multilingual capabilities. The authors propose evaluation methods for Cross-lingual Semantic Consistency (xSC) using the LaBSE model, as well as metrics for Cross-lingual Accuracy Consistency (xAC) and Cross-lingual Timeliness Consistency (xTC).

The authors are Xiaolin Xing, Zhiwei He, Haoyu Xu, Xing Wang, Rui Wang, and Yu Hong, with affiliations including Soochow University, Shanghai Jiao Tong Uni
…[truncated 200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T11:05:41.396915+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xu Qi Guo \"Knowledge Conflicts for LLMs: A Survey\" EMNLP 2024 arXiv 2403.08319"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xu Qi Guo \"Knowledge Conflicts for LLMs: A Survey\" EMNLP 2024 arXiv 2403.08319"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T11:05:41.397052+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhao Du Hong \"Analysing the Residual Stream\" knowledge conflicts NeurIPS 2024 workshop arXiv 2410.16090"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhao Du Hong \"Analysing the Residual Stream\" knowledge conflicts NeurIPS 2024 workshop arXiv 2410.16090"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T11:05:41.397173+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhao Devoto \"Steering Knowledge Selection Behaviours\" SAE representation engineering NAACL 2025 arXiv 2410.15999"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhao Devoto \"Steering Knowledge Selection Behaviours\" SAE representation engineering NAACL 2025 arXiv 2410.15999"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T11:05:41.397290+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhao Huang Chen \"When Abundance Conceals Weakness\" knowledge conflict multilingual arXiv 2601.07041"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhao Huang Chen \"When Abundance Conceals Weakness\" knowledge conflict multilingual arXiv 2601.07041"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T11:05:41.397405+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "xing2024evaluating arXiv 2407.01358 dblp authors \"Xiaoling\" OR \"Xiaolin\" Xing cross-lingual inconsistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "xing2024evaluating arXiv 2407.01358 dblp authors \"Xiaoling\" OR \"Xiaolin\" Xing cross-lingual inconsistency"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T11:05:41.397550+00:00_

Web search results for query: "Xu Qi Guo "Knowledge Conflicts for LLMs: A Survey" EMNLP 2024 arXiv 2403.08319"

Links: [{"title":"[2403.08319] Knowledge Conflicts for LLMs: A Survey","url":"https://arxiv.org/abs/2403.08319"},{"title":"GitHub - pillowsofwind/Knowledge-Conflicts-Survey: [EMNLP 2024] The official GitHub repo for the survey paper \"Knowledge Conflicts for LLMs: A Survey\" · GitHub","url":"https://github.com/pillowsofwind/Knowledge-Conflicts-Survey"},{"title":"[2403.08319v2] Knowledge Conflicts for LLMs: A Survey","url":"https://arxiv.org/abs/2403.08319v2"},{"title":"Knowledge Conflicts for LLMs: A Survey - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.486/"},{"title":"[PDF] Knowledge Conflicts for LLMs: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Knowledge-Conflicts-for-LLMs:-A-Survey-Xu-Qi/ab8e6df5001dbb9b48445220099425aff536b3e8"},{"title":"Knowledge Conflicts for LLMs: A Survey (2403.08319v2)","url":"https://www.emergentmind.com/papers/2403.08319"},{"title":"Paper page - Knowledge Conflicts for LLMs: A Survey","url":"https://huggingface.co/papers/2403.08319"},{"title":"Knowledge Conflicts for LLMs: A Survey - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240308319X/abstract"}]

I found the paper! Here are the search results for the paper you're looking for:

**Paper Details:**

The paper "Knowledge Conflicts for LLMs: A Survey" by Xu et al. was published at the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024) in Miami, Florida, USA.

**Authors:** Rongwu Xu, Zehan Qi, Zhijiang Guo, Cunxiang Wang, Hongru Wang, Yue Zhang, and Wei Xu

**ArXiv Information:** The paper was submitted on March 13, 2024 (v1) and last revised on June 22, 2024 (v2) with arXiv identifier 2403.08319

**Overview:** The survey provides an in-depth analysis of knowledge conflicts for large language models (LLMs), highlighting the complex challenges they encounter when blending contextual and para
…[truncated 574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T11:05:41.397718+00:00_

Web search results for query: "Zhao Du Hong "Analysing the Residual Stream" knowledge conflicts NeurIPS 2024 workshop arXiv 2410.16090"

Links: [{"title":"Analysing the residual stream of language models under knowledge conflicts - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/analysing-the-residual-stream-of-language-models-under-knowledge-/"},{"title":"(PDF) Analysing the Residual Stream of Language Models Under Knowledge Conflicts","url":"https://www.researchgate.net/publication/385108205_Analysing_the_Residual_Stream_of_Language_Models_Under_Knowledge_Conflicts"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge Conflicts","url":"https://openreview.net/attachment?id=3Y0xm1q58x&name=pdf"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge Conflicts","url":"https://arxiv.org/html/2410.16090v1"},{"title":"[2410.16090] Analysing the Residual Stream of Language Models Under Knowledge Conflicts","url":"https://arxiv.org/abs/2410.16090"},{"title":"dblp: Analysing the Residual Stream of Language Models Under Knowledge Conflicts.","url":"https://dblp.org/rec/journals/corr/abs-2410-16090.html"},{"title":"Xiaotang Du's scientific contributions","url":"https://www.researchgate.net/scientific-contributions/Xiaotang-Du-2283752843"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge Conflicts | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/analysing-residual-stream-language-models-under-knowledge"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** "Analysing the Residual Stream of Language Models Under Knowledge Conflicts"

**Authors:** Yu Zhao, Xiaotang Du, Giwon Hong, Aryo Pradipta Gema, Alessio Devoto, Hongru Wang, Xuanli He, Kam-Fai Wong, Pasquale Minervini

**Publication Details:** Proceedings of the 38th Conference on Neural Information Processing Systems (NeurIPS), 2024. The paper was also 
…[truncated 617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-26T11:05:41.397922+00:00_

Web search results for query: "Zhao Devoto "Steering Knowledge Selection Behaviours" SAE representation engineering NAACL 2025 arXiv 2410.15999"

Links: [{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.264/"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"[2410.15999] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://arxiv.org/abs/2410.15999"},{"title":"Steering Knowledge Selection Behaviours in LLMs","url":"https://arxiv.org/pdf/2410.15999"},{"title":"GitHub - yuzhaouoe/SAE-based-representation-engineering: [NAACL'25 Oral] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://github.com/yuzhaouoe/SAE-based-representation-engineering"},{"title":"[PDF] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Steering-Knowledge-Selection-Behaviours-in-LLMs-via-Zhao-Devoto/d2c1b1a8ac40fbd45e8a91504b1a131f99bad02f"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/steering-knowledge-selection-behaviours-llms-via-sae"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://arxiv.org/html/2410.15999v1"},{"title":"Yu Zhao","url":"https://yuzhaouoe.github.io/"}]

I found the paper you're looking for. Here's what I found:

The paper "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering" by Yu Zhao, Alessio Devoto, Giwon Hong, Xiaotang Du, Aryo Pradipta Gema, Hongru Wang, Xuanli He, Kam-Fai Wong, and Pasquale Minervini was published at NAACL 2025 in Albuquerque, New Mexico.

The paper
…[truncated 753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-26T11:05:41.398092+00:00_

Web search results for query: "xing2024evaluating arXiv 2407.01358 dblp authors "Xiaoling" OR "Xiaolin" Xing cross-lingual inconsistency"

Links: [{"title":"[2407.01358] Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/abs/2407.01358"},{"title":"dblp: Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2407-01358.html"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2407.01358"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://www.researchgate.net/publication/381882496_Evaluating_Knowledge-based_Cross-lingual_Inconsistency_in_Large_Language_Models"},{"title":"Understanding Cross-Lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2505.13141v1"},{"title":"dblp: Xiaolin Shi (disambiguation)","url":"https://dblp.org/pid/64/546.html"}]

Based on the search results, I found the paper you're looking for:

**Paper Details:**

The paper "Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models" (arXiv 2407.01358) is authored by Xiaolin Xing, Zhiwei He, Haoyu Xu, Xing Wang, Rui Wang, and Yu Hong.

**Paper Overview:**

The paper investigates cross-lingual inconsistencies observed in Large Language Models (LLMs), such as ChatGPT, Llama, and Baichuan, which have shown exceptional performance in various Natural Language Processing (NLP) tasks, but often exhibit significant inconsistencies when processing the same concepts across different languages.

The study proposes an innovative evaluation method for Cross-lingual Semantic Consistency (xSC) using the LaBSE model, and introduces metrics for Cross-lingual Accuracy Consistency (xAC) and Cross-lingual Timeliness Consistency (xTC) to comprehensively assess the models' performance.

The authors are affiliated with Soochow U
…[truncated 198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T11:05:41.398252+00:00_

Web search results for query: "Zhao Huang Chen "When Abundance Conceals Weakness" knowledge conflict multilingual arXiv 2601.07041"

Links: [{"title":"[2601.07041] When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/abs/2601.07041"},{"title":"When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/html/2601.07041"},{"title":"When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/pdf/2601.07041"},{"title":"Study of the Hadronic Decays of \\chi_c States","url":"https://arxiv.org/pdf/hep-ex/9812016"},{"title":"Inclusive charged and neutral particle multiplicity distributions in   $\\chi_{cJ}$ and $J/\\psi$ decays","url":"https://arxiv.org/pdf/2006.05588"}]

Based on the search results, I found the paper you're looking for:

"When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models" is authored by Jiaqi Zhao, Qiang Huang, Haodong Chen, Xiaoxing You, and Jun Yu from Harbin Institute of Technology (Shenzhen) and Hangzhou Dianzi University.

The paper examines how Large Language Models (LLMs) encode vast world knowledge across multiple languages, though their internal beliefs are often unevenly distributed across linguistic spaces, and when external evidence contradicts these language-dependent memories, models encounter cross-lingual knowledge conflict.

The researchers introduce CLEAR, a Cross-Lingual knowlEdge conflict evAluation fRamework that systematically examines how multilingual LLMs reconcile conflicting internal beliefs and multilingual external evidence, decomposing conflict resolution into four progressive scenarios from multilingual parametric elicitation to competitive multi-source cross-lingual induction.

The study constructs multilingual versions of ConflictQA and ConflictingQA covering 10 typologically diverse languages and evaluates six representative LLMs. Key findings reveal that in reasoning
…[truncated 368 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T11:05:41.398439+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wu Conneau Li Zettlemoyer Stoyanov \"Emerging Cross-lingual Structure\" pretrained language models ACL 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wu Conneau Li Zettlemoyer Stoyanov \"Emerging Cross-lingual Structure\" pretrained language models ACL 2020"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-26T11:05:41.398573+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wendler Veselovsky Monea West \"Do Llamas Work in English\" latent language multilingual ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wendler Veselovsky Monea West \"Do Llamas Work in English\" latent language multilingual ACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-26T11:05:41.398704+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Muller Elazar Sagot Seddah \"First Align then Predict\" cross-lingual multilingual BERT EACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Muller Elazar Sagot Seddah \"First Align then Predict\" cross-lingual multilingual BERT EACL 2021"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-26T11:05:41.398821+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kargaran Modarressi \"MEXA Multilingual Evaluation English-Centric LLMs\" cross-lingual alignment arXiv 2410.05873"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kargaran Modarressi \"MEXA Multilingual Evaluation English-Centric LLMs\" cross-lingual alignment arXiv 2410.05873"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T11:05:41.398957+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Belinkov \"Probing Classifiers Promises Shortcomings Advances\" Computational Linguistics 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Belinkov \"Probing Classifiers Promises Shortcomings Advances\" Computational Linguistics 2022"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-26T11:05:41.399106+00:00_

Web search results for query: "Wu Conneau Li Zettlemoyer Stoyanov "Emerging Cross-lingual Structure" pretrained language models ACL 2020"

Links: [{"title":"Emerging Cross-lingual Structure in Pretrained Language Models - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.536/"},{"title":"Emerging Cross-lingual Structure in Pretrained Language ...","url":"https://aclanthology.org/2020.acl-main.536.pdf"},{"title":"[PDF] Emerging Cross-lingual Structure in Pretrained Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Emerging-Cross-lingual-Structure-in-Pretrained-Wu-Conneau/cfe8ec7a183ed548db1a862e38908343cefb94c7"},{"title":"[1911.01464] Emerging Cross-lingual Structure in Pretrained Language Models","url":"https://arxiv.org/abs/1911.01464"},{"title":"Unsupervised Cross-lingual Representation Learning at Scale - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.747/"},{"title":"Cross-lingual Language Model Pretraining for Retrieval | Proceedings of the Web Conference 2021","url":"https://dl.acm.org/doi/10.1145/3442381.3449830"},{"title":"Accepted Papers - ACL 2020","url":"https://acl2020.org/program/accepted/"},{"title":"(PDF) Emerging Cross-lingual Structure in Pretrained Language Models","url":"https://www.researchgate.net/publication/337048070_Emerging_Cross-lingual_Structure_in_Pretrained_Language_Models"}]

I found the paper you're looking for. Here are the details:

**Paper Title:** Emerging Cross-lingual Structure in Pretrained Language Models

**Authors:** Alexis Conneau, Shijie Wu, Haoran Li, Luke Zettlemoyer, and Veselin Stoyanov

**Publication:** Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 6022–6034, Online

**Research Focus:** The paper studies multilingual masked language modeling—the training of a single model on concatenated text from multiple languages—and presents a detailed study of several factors that influence why these models are so effective fo
…[truncated 492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-26T11:05:41.399295+00:00_

Web search results for query: "Wendler Veselovsky Monea West "Do Llamas Work in English" latent language multilingual ACL 2024"

Links: [{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.820/"},{"title":"[2402.10588] Do Llamas Work in English? On the Latent Language of Multilingual Transformers","url":"https://arxiv.org/abs/2402.10588"},{"title":"Do Llamas Work in English? On the Latent Language of ...","url":"https://aclanthology.org/2024.acl-long.820.pdf"},{"title":"[PDF] Do Llamas Work in English? On the Latent Language of Multilingual Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Do-Llamas-Work-in-English-On-the-Latent-Language-of-Wendler-Veselovsky/e88efdfc05d0d8832b2ded7af9c8ececdd03e58d"},{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/do-llamas-work-english-latent-language-multilingual"},{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers | Artificial Intelligence Hub","url":"https://aicitta.com/posts/do-llamas-work-in-english/"},{"title":"dblp: Do Llamas Work in English? On the Latent Language of Multilingual Transformers.","url":"https://dblp.org/rec/journals/corr/abs-2402-10588.html"},{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers - Consensus","url":"https://consensus.app/papers/details/b8aa720cd459550191960afe5413d726/"},{"title":"GitHub - epfl-dlab/llm-latent-language: Repo accompanying our paper \"Do Llamas Work in English? On the Latent Language of Multilingual Transformers\".","url":"https://github.com/epfl-dlab/llm-latent-language"},{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers - Paper Detail","url":"https://deeplearn.org/arxiv/459055/do-llamas-work-in-english"}]

Great! I found the pa
…[truncated 1538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-26T11:05:41.399451+00:00_

Web search results for query: "Muller Elazar Sagot Seddah "First Align then Predict" cross-lingual multilingual BERT EACL 2021"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. I'm unable to perform the search for the paper by Muller, Elazar, Sagot, and Seddah on "First Align then Predict" at this moment.

If you're looking for this paper, I'd recommend:
1. Visiting academic paper repositories like arXiv.org, ACL Anthology, or Google Scholar
2. Searching directly on the EACL 2021 proceedings page
3. Visiting the authors' institutional websites or research profiles

Is there anything else I can help you with regarding this paper or related topics?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-26T11:05:41.399589+00:00_

Web search results for query: "Kargaran Modarressi "MEXA Multilingual Evaluation English-Centric LLMs" cross-lingual alignment arXiv 2410.05873"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. I'm unable to perform the search for the arXiv paper by Kargaran Modarressi on "MEXA Multilingual Evaluation English-Centric LLMs" (arXiv 2410.05873) at this moment.

However, you can access this paper directly by:
1. Visiting **arXiv.org** and searching for the paper ID **2410.05873**
2. Searching for the authors and title directly on arXiv
3. Using Google Scholar with the paper ID or title

If you'd like to discuss the contents of this paper once you've accessed it, or if you have other questions, I'd be happy to help!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-26T11:05:41.399727+00:00_

Web search results for query: "Belinkov "Probing Classifiers Promises Shortcomings Advances" Computational Linguistics 2022"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. However, based on your query, you appear to be looking for a paper by Belinkov on probing classifiers in computational linguistics from 2022. This sounds like a research paper that would likely be available through:

1. **ACL Anthology** (acl-anthology.org) - where Computational Linguistics papers are published
2. **arXiv** (arxiv.org) - for preprints
3. **Google Scholar** (scholar.google.com) - for academic papers
4. **The author's academic webpage** - if Belinkov has a faculty or institutional page

You could try searching for these sources directly with the title and author information you have. If you'd like, you can try again later and I can attempt the search once the tool is available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-26T11:05:41.399913+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Muller Elazar Sagot Seddah \"First Align then Predict\" EACL 2021 multilingual BERT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Muller Elazar Sagot Seddah \"First Align then Predict\" EACL 2021 multilingual BERT"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-26T11:05:41.400044+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kargaran Modarressi MEXA multilingual evaluation cross-lingual alignment ACL 2025 Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kargaran Modarressi MEXA multilingual evaluation cross-lingual alignment ACL 2025 Findings"
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-26T11:05:41.400161+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Belinkov \"Probing Classifiers\" Computational Linguistics 2022 volume 48"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Belinkov \"Probing Classifiers\" Computational Linguistics 2022 volume 48"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-26T11:05:41.400276+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hewitt Liang \"Designing and Interpreting Probes with Control Tasks\" EMNLP 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hewitt Liang \"Designing and Interpreting Probes with Control Tasks\" EMNLP 2019"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-26T11:05:41.400389+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ulmer Hardmeier Frellsen \"deep-significance\" statistical significance neural networks arXiv 2204.06815"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ulmer Hardmeier Frellsen \"deep-significance\" statistical significance neural networks arXiv 2204.06815"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-26T11:05:41.400508+00:00_

Web search results for query: "Muller Elazar Sagot Seddah "First Align then Predict" EACL 2021 multilingual BERT"

No links found.

Based on the search results, I found relevant information about this paper. "First Align then Predict: Towards Precise and Stable Prediction with Alignment-Regularized BERT" is a paper that was presented at EACL 2021.

The paper focuses on using multilingual BERT and proposes an alignment-regularized approach. The work appears to address issues related to improving prediction stability and precision through alignment mechanisms in multilingual transformer models.

If you need more specific details about the paper's methodology, results, or contributions, I can perform additional searches with different queries to find more detailed information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-26T11:05:41.400638+00:00_

Web search results for query: "Kargaran Modarressi MEXA multilingual evaluation cross-lingual alignment ACL 2025 Findings"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. I'm unable to perform the search for information about Kargaran Modarressi's MEXA paper on multilingual evaluation and cross-lingual alignment from ACL 2025 Findings at this moment.

If you'd like, you could try:
- Visiting the ACL Anthology website directly (aclanthology.org)
- Searching on Google Scholar
- Checking arXiv.org for preprints
- Looking at the ACL 2025 Findings proceedings page

Would you like me to help you with anything else?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-26T11:05:41.400806+00:00_

Web search results for query: "Belinkov "Probing Classifiers" Computational Linguistics 2022 volume 48"

Web search error: unavailable

I apologize, but I'm unable to perform the web search at this moment as the web search tool is currently unavailable. 

However, based on the query you've provided, it appears you're looking for an academic paper by Belinkov about "Probing Classifiers" published in the Computational Linguistics journal in 2022, volume 48. 

If you'd like to find this paper, I'd recommend:
1. Searching directly on **ACL Anthology** (aclanthology.org) - the official repository for Computational Linguistics papers
2. Using **Google Scholar** (scholar.google.com) with these search terms
3. Checking the author's institutional page or GitHub profile
4. Searching on **arXiv** if a preprint version exists

Please try your search again later, or feel free to ask me other questions I might be able to help with!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-26T11:05:41.400961+00:00_

Web search results for query: "Ulmer Hardmeier Frellsen "deep-significance" statistical significance neural networks arXiv 2204.06815"

Web search error: unavailable

I apologize, but I'm unable to perform the web search at this moment as the search tool is currently unavailable. 

However, based on your query parameters, it appears you're looking for a research paper on arXiv. The arXiv identifier 2204.06815 suggests this is a paper from April 2022. If you'd like to access this paper directly, you can visit:

**https://arxiv.org/abs/2204.06815**

This will take you to the arXiv abstract page where you can view the paper details, download the PDF, and see more information about the authors (Ulmer, Hardmeier, and Frellsen) and their work on statistical significance testing in neural networks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-26T11:05:41.401121+00:00_

Web search results for query: "Hewitt Liang "Designing and Interpreting Probes with Control Tasks" EMNLP 2019"

Links: [{"title":"Designing and Interpreting Probes with Control Tasks - ACL Anthology","url":"https://aclanthology.org/D19-1275/"},{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"},{"title":"Designing and Interpreting Probes with Control Tasks | papers_we_read","url":"https://vlgiitr.github.io/papers_we_read/summaries/control_tasks.html"},{"title":"[PDF] Designing and Interpreting Probes with Control Tasks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Designing-and-Interpreting-Probes-with-Control-Hewitt-Liang/199ff73d2f728e997f860b62a2322823d3e3d9e8"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://bibbase.org/network/publication/hewitt-liang-designingandinterpretingprobeswithcontroltasks-2019"},{"title":"Designing and Interpreting Probes with Control Tasks Percy Liang John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/public/hewitt2019control_slides.pdf"},{"title":"[1909.03368] Designing and Interpreting Probes with Control Tasks","url":"https://arxiv.org/abs/1909.03368"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Designing+and+interpreting+probes+with+control+tasks&author=John+Hewitt&author=Percy+Liang&publication_year=2019&pages=2733-2743&doi=10.18653/v1/D19-1275"},{"title":"Designing and Interpreting Probes with Control Tasks. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1c7c8f6e4720c00cfb0b395c4827d7155"},{"title":"Designing and Interpreting Probes with Control Tasks John Hewitt","url":"https://nlp.stanford.edu/pubs/hewitt2019control.pdf"}]

I found comprehensive information about the paper. Here are the key details:

## Publication Information

The paper "Designing and Interpreting Probes with Control Tasks" by John Hewitt and Percy Liang was published in the Proceeding
…[truncated 1382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-26T11:05:41.401307+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"First Align, then Predict\" Benjamin Muller Yanai Elazar EACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"First Align, then Predict\" Benjamin Muller Yanai Elazar EACL 2021"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-26T11:05:41.401431+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MEXA Kargaran Modarressi arXiv 2410.05873 English-Centric LLMs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MEXA Kargaran Modarressi arXiv 2410.05873 English-Centric LLMs"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-26T11:05:41.401548+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Belinkov probing classifiers promises shortcomings advances Computational Linguistics 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Belinkov probing classifiers promises shortcomings advances Computational Linguistics 2022"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-26T11:05:41.401663+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ulmer Hardmeier Frellsen deep-significance easy meaningful statistical significance testing 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ulmer Hardmeier Frellsen deep-significance easy meaningful statistical significance testing 2022"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-26T11:05:41.401775+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li Patel Viegas Pfister Wattenberg \"Inference-Time Intervention\" truthful answers NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li Patel Viegas Pfister Wattenberg \"Inference-Time Intervention\" truthful answers NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-26T11:05:41.401948+00:00_

Web search results for query: ""First Align, then Predict" Benjamin Muller Yanai Elazar EACL 2021"

Links: [{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT - ACL Anthology","url":"https://aclanthology.org/2021.eacl-main.189/"},{"title":"[PDF] First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/First-Align,-then-Predict:-Understanding-the-of-Muller-Elazar/1cfd0f08bb7ab449bbccc3d69a62ffbf43a7eb7f"},{"title":"GitHub - benjamin-mlr/first-align-then-predict · GitHub","url":"https://github.com/benjamin-mlr/first-align-then-predict"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Request PDF","url":"https://www.researchgate.net/publication/355434439_First_Align_then_Predict_Understanding_the_Cross-Lingual_Ability_of_Multilingual_BERT"},{"title":"EACL2021: First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT","url":"https://www.virtual2021.eacl.org/paper_main.882.html"},{"title":"GitHub - benjamin-mlr/first-align-then-predict-w-RANDOM-INIT · GitHub","url":"https://github.com/benjamin-mlr/first-align-then-predict-w-RANDOM-INIT"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT - Inria - Institut national de recherche en sciences et technologies du numérique","url":"https://inria.hal.science/hal-03239087"},{"title":"[2101.11109] First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT","url":"https://arxiv.org/abs/2101.11109"},{"title":"Figure 5 from First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/First-Align,-then-Predict:-Understanding-the-of-Muller-Elazar/1cfd0f08bb7ab449bbccc3d69a62ffbf43a7eb7f/figure/9"},{"title":"First Align, then Predict: Understanding 
…[truncated 1599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-26T11:05:41.402130+00:00_

Web search results for query: "Belinkov probing classifiers promises shortcomings advances Computational Linguistics 2022"

Links: [{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology","url":"https://aclanthology.org/2022.cl-1.7/"},{"title":"[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/abs/2102.12452"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"Yonatan Belinkov | publications","url":"https://belinkov.com/publications/publicationstype/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"(PDF) Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"@article{belinkov-2022-probing,","url":"https://aclanthology.org/2022.cl-1.7.bib"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://aclanthology.org/2022.cl-1.7.pdf"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://scite.ai/reports/probing-classifiers-promises-shortcomings-and-kepAxaJ3"}]

I found the paper you're looking for. Here's what the search revealed:

Probing classifiers have emerged as one of the prominent methodologies for interpreting and analyzing deep neural network models of natural language processing. The basic idea is simple—a classifier is trained to predict some 
…[truncated 781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-26T11:05:41.402280+00:00_

Web search results for query: "MEXA Kargaran Modarressi arXiv 2410.05873 English-Centric LLMs"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable and I'm unable to perform the search for that query at this time. 

However, based on the query components you've provided, this appears to be asking about an arXiv paper (arXiv 2410.05873) related to "MEXA" by authors Kargaran and Modarressi, likely focused on English-centric Large Language Models (LLMs).

If you'd like to access this paper directly, I'd recommend:
1. Visiting arXiv.org and searching for paper ID 2410.05873
2. Searching for "MEXA Kargaran Modarressi" on arXiv's website

I apologize that I cannot retrieve the current information about this paper for you at this moment. Please try again later or access the paper directly through arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-26T11:05:41.402410+00:00_

Web search results for query: "Ulmer Hardmeier Frellsen deep-significance easy meaningful statistical significance testing 2022"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. I'm unable to complete the search you requested at this moment. Please try again in a few moments, or let me know if there's another way I can help you with information about this topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-26T11:05:41.402535+00:00_

Web search results for query: "Li Patel Viegas Pfister Wattenberg "Inference-Time Intervention" truthful answers NeurIPS 2023"

Web search error: unavailable

I apologize, but I'm unable to perform the web search at this moment as the tool is currently unavailable. However, I can tell you that based on the query parameters you've provided, you're looking for a research paper related to "Inference-Time Intervention" presented at NeurIPS 2023 by authors Li, Patel, Viegas, Pfister, and Wattenberg that appears to address methods for obtaining truthful answers from AI models.

To find this paper, you could try:
1. Visiting the NeurIPS 2023 conference proceedings directly
2. Searching on academic databases like ArXiv, Google Scholar, or Papers with Code
3. Searching directly on the paper title "Inference-Time Intervention" combined with the authors' names

If you'd like me to try the search again in a moment, please let me know!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-26T11:05:41.402694+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kenneth Li \"Inference-Time Intervention\" truthful answers language model NeurIPS 2023 arXiv 2306.03341"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kenneth Li \"Inference-Time Intervention\" truthful answers language model NeurIPS 2023 arXiv 2306.03341"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-26T11:05:41.402815+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dennis Ulmer deep-significance statistical significance testing neural networks arXiv 2204.06815"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dennis Ulmer deep-significance statistical significance testing neural networks arXiv 2204.06815"
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-26T11:05:41.402953+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zou Phan Chen \"Representation Engineering\" AI transparency arXiv 2310.01405"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zou Phan Chen \"Representation Engineering\" AI transparency arXiv 2310.01405"
  }
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-26T11:05:41.403066+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Turner Thiergart \"Activation Addition\" steering language models without optimization arXiv 2308.10248"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Turner Thiergart \"Activation Addition\" steering language models without optimization arXiv 2308.10248"
  }
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-26T11:05:41.403178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Marks Tegmark \"Geometry of Truth\" linear structure LLM representations true false ICLR arXiv 2310.06824"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Marks Tegmark \"Geometry of Truth\" linear structure LLM representations true false ICLR arXiv 2310.06824"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-26T11:05:41.403301+00:00_

Web search results for query: "Dennis Ulmer deep-significance statistical significance testing neural networks arXiv 2204.06815"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. However, I can tell you that arXiv 2204.06815 appears to be a paper identifier from arXiv (an open-access repository for preprints). You can access this paper directly by:

1. Going to https://arxiv.org/abs/2204.06815
2. Or searching for it on arXiv.org with the paper ID "2204.06815"

This will give you the full paper details, abstract, and download options. If you have specific questions about the content of this paper, feel free to ask and I can try to help based on general knowledge about statistical significance testing and neural networks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-26T11:05:41.403430+00:00_

Web search results for query: "Kenneth Li "Inference-Time Intervention" truthful answers language model NeurIPS 2023 arXiv 2306.03341"

Web search error: unavailable

I apologize, but I was unable to perform the web search at this time as the search tool is currently unavailable. However, I can provide you with information based on what you've mentioned:

Based on your query parameters, you're looking for research by Kenneth Li related to "Inference-Time Intervention," which appears to be a technique for improving the truthfulness of language model outputs. The paper details you've provided suggest:

- **Author**: Kenneth Li
- **Title**: "Inference-Time Intervention" (or similar)
- **Topic**: Making language models produce more truthful answers
- **Conference/Publication**: NeurIPS 2023
- **ArXiv ID**: 2306.03341

This arXiv ID (2306.03341) would correspond to a paper submitted in June 2023. If you'd like to access this paper directly, you can visit:
- arXiv.org at: https://arxiv.org/abs/2306.03341
- Or search for it on Google Scholar

When the web search tool becomes available again, I'd be happy to search for more detailed information about this research if you need it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-26T11:05:41.403559+00:00_

Web search results for query: "Zou Phan Chen "Representation Engineering" AI transparency arXiv 2310.01405"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. However, I can provide you with some context about what you're looking for:

You're searching for a paper on "Representation Engineering," which is a technique in AI interpretability and transparency. The arXiv identifier 2310.01405 suggests this is a paper from October 2023. "Representation Engineering" is an approach to understanding and modifying the internal representations of large language models to improve their behavior and transparency.

If you'd like to access this paper directly, you can visit arXiv.org and search for the paper ID 2310.01405, or you could try searching for "Representation Engineering" along with the authors' names on Google Scholar or other academic databases.

Is there anything else I can help you with regarding this research topic?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-26T11:05:41.403683+00:00_

Web search results for query: "Turner Thiergart "Activation Addition" steering language models without optimization arXiv 2308.10248"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. However, based on your query, I can tell you that you're looking for a paper on "Activation Addition" by Turner Thiergart and colleagues, with the arXiv identifier 2308.10248. This appears to be a research paper about steering language models without optimization.

To access this paper, you can:
1. Visit **arXiv.org** directly and search for the identifier "2308.10248"
2. Search for the paper title "Activation Addition: Steering Language Models Without Optimization" along with the authors' names
3. Visit the arXiv link directly: https://arxiv.org/abs/2308.10248

If you'd like, you can share any specific questions about the paper's content, and I may be able to help based on my training knowledge, though my information has a knowledge cutoff date.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-26T11:05:41.403813+00:00_

Web search results for query: "Marks Tegmark "Geometry of Truth" linear structure LLM representations true false ICLR arXiv 2310.06824"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. However, based on your query parameters, you're looking for a paper about the "Geometry of Truth" by Max Tegmark (note: it's Max Tegmark, not Marks). This appears to be a research paper about how large language models (LLMs) represent true and false statements through linear structures in their internal representations.

The paper identifier you provided (arXiv 2310.06824) indicates it was likely posted to arXiv in October 2023. This type of work typically investigates the geometric properties of how neural networks encode semantic information, particularly the distinction between true and false statements.

To access this paper directly, you can:
1. Visit https://arxiv.org/abs/2310.06824
2. Search for "Geometry of Truth Tegmark" on arXiv or Google Scholar
3. Check the ICLR 2024 proceedings if it was accepted there

If you have specific questions about the paper's contents or methodology, feel free to ask and I can try to help based on my existing knowledge.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-26T11:05:41.403985+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kenneth Li Oam Patel Inference-Time Intervention eliciting truthful answers NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kenneth Li Oam Patel Inference-Time Intervention eliciting truthful answers NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-26T11:05:41.404102+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Andy Zou representation engineering top-down approach AI transparency 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Andy Zou representation engineering top-down approach AI transparency 2023"
  }
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-26T11:05:41.404213+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Alexander Turner activation addition steering language models 2023 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Alexander Turner activation addition steering language models 2023 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-26T11:05:41.404322+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Samuel Marks Max Tegmark geometry of truth emergent linear structure ICLR 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Samuel Marks Max Tegmark geometry of truth emergent linear structure ICLR 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-26T11:05:41.404429+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MEXA multilingual evaluation English-centric LLMs Kargaran 2024 cross-lingual alignment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MEXA multilingual evaluation English-centric LLMs Kargaran 2024 cross-lingual alignment"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-26T11:05:41.404544+00:00_

Web search results for query: "Kenneth Li Oam Patel Inference-Time Intervention eliciting truthful answers NeurIPS 2023"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. However, I can tell you that based on my knowledge, this appears to be a reference to research on "Inference-Time Intervention" (ITI), a technique for improving the truthfulness of large language models. The work by Kenneth Li, Oam Patel, and colleagues was indeed presented at NeurIPS 2023 and focuses on methods to elicit more truthful answers from language models during inference without requiring retraining.

If you need current information about this paper or want to access the full details, I'd recommend:
1. Checking the NeurIPS 2023 proceedings directly
2. Visiting arXiv.org and searching for the paper
3. Checking the authors' institutional repositories

Would you like me to help you with anything else related to this research topic?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-26T11:05:41.404694+00:00_

Web search results for query: "MEXA multilingual evaluation English-centric LLMs Kargaran 2024 cross-lingual alignment"

Links: [{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://arxiv.org/pdf/2410.05873"},{"title":"Cross-Lingual Auto Evaluation for Assessing Multilingual LLMs","url":"https://arxiv.org/pdf/2410.13394"},{"title":"Do Large Language Models Have an English Accent? Evaluating and Improving the Naturalness of Multilingual LLMs","url":"https://arxiv.org/pdf/2410.15956"},{"title":"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual   Knowledge Alignment, But Only Shallowly","url":"https://arxiv.org/pdf/2404.04659"},{"title":"From Neurons to Semantics: Evaluating Cross-Linguistic Alignment Capabilities of Large Language Models via Neurons Alignment","url":"https://arxiv.org/pdf/2507.14900"}]

Based on the search results, here's what I found about MEXA:

MEXA is a method for assessing the multilingual capabilities of pre-trained English-centric LLMs using parallel sentences, introduced by Amir Hossein Kargaran and colleagues.

**Key Features:**

- MEXA leverages the fact that English-centric LLMs use English as a pivot language in their intermediate layers, computing alignment between English and non-English languages using parallel sentences to evaluate the transfer of language understanding from English to other languages.

- It uses parallel sentences, which are available for more languages than existing downstream tasks.

**Evaluation and Results:**

- The studies used various parallel datasets (FLORES-200 and Bible), models (Llama family, Gemma family, Mistral, and OLMo), and established downstream tasks (Belebele, m-MMLU, and m-ARC).

- MEXA achieved a statistically significant average Pearson correlation of 0.90 with three established downstream tasks across nine models and two parallel datasets.

The first search result is the full paper available on arXiv (https://arxiv.org/p
…[truncated 118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-26T11:05:41.404840+00:00_

Web search results for query: "Andy Zou representation engineering top-down approach AI transparency 2023"

Web search error: unavailable

I apologize, but I encountered an issue with the web search tool and it's currently unavailable. I'm unable to complete your search query at this moment. 

However, I can tell you that based on my training data, Andy Zou is a researcher who has worked on AI safety and alignment topics, and representation engineering is a technique related to understanding and manipulating neural network representations. If you'd like, you could try:

1. Searching directly on Google Scholar for "Andy Zou representation engineering"
2. Checking arxiv.org for recent papers on representation engineering
3. Looking at academic institution websites where Andy Zou may be affiliated

Would you like me to help you with something else, or would you like to try this search again later?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-26T11:05:41.404991+00:00_

Web search results for query: "Samuel Marks Max Tegmark geometry of truth emergent linear structure ICLR 2024 2025"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. I'm unable to perform the search for that query at this moment. 

If you'd like, you can try:
- Searching directly on Google or another search engine with that query
- Visiting the ICLR conference website or proceedings directly
- Checking academic repositories like arXiv or Scholar.google.com for papers by Samuel Marks and Max Tegmark

Would you like me to help you with anything else regarding this topic?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-26T11:05:41.405114+00:00_

Web search results for query: "Alexander Turner activation addition steering language models 2023 arXiv"

Web search error: unavailable

I apologize, but I'm unable to complete the web search at this moment as the web_search tool is currently unavailable. However, based on your query, you appear to be looking for a 2023 arXiv paper by Alexander Turner related to activation addition and steering language models.

To find this paper yourself, I recommend:
1. Visiting **arXiv.org** directly and searching for "Alexander Turner activation addition"
2. Searching for the paper on **Google Scholar**
3. Checking the **Anthropic website** or **Alignment Research Center** repositories, as these topics relate to AI safety research

If you can provide more specific details about the paper (such as the exact title or arXiv ID), I may be able to help you in other ways.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-26T11:05:41.405276+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Elhage Hume Olsson \"Toy Models of Superposition\" Transformer Circuits 2022 arXiv 2209.10652"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Elhage Hume Olsson \"Toy Models of Superposition\" Transformer Circuits 2022 arXiv 2209.10652"
  }
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-26T11:05:41.405395+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Templeton Conerly Marcus \"Scaling Monosemanticity\" Claude 3 Sonnet Anthropic 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Templeton Conerly Marcus \"Scaling Monosemanticity\" Claude 3 Sonnet Anthropic 2024"
  }
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-26T11:05:41.405516+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Feng Li Zhu \"Fine-Grained Activation Steering\" ICLR 2026 arXiv 2602.04428"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Feng Li Zhu \"Fine-Grained Activation Steering\" ICLR 2026 arXiv 2602.04428"
  }
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-26T11:05:41.405632+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Conneau Rinott Lample \"XNLI Evaluating Cross-lingual Sentence Representations\" EMNLP 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Conneau Rinott Lample \"XNLI Evaluating Cross-lingual Sentence Representations\" EMNLP 2018"
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-26T11:05:41.405742+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rei Stewart Farinha Lavie \"COMET Neural Framework MT Evaluation\" EMNLP 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rei Stewart Farinha Lavie \"COMET Neural Framework MT Evaluation\" EMNLP 2020"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-26T11:05:41.405902+00:00_

Web search results for query: "Rei Stewart Farinha Lavie "COMET Neural Framework MT Evaluation" EMNLP 2020"

Links: [{"title":"COMET: A Neural Framework for MT Evaluation - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.213/"},{"title":"[PDF] COMET: A Neural Framework for MT Evaluation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/COMET:-A-Neural-Framework-for-MT-Evaluation-Rei-Stewart/9e67b9758520e49016ab66bafb974d2e1ed762d1"},{"title":"COMET: A Neural Framework for MT Evaluation","url":"https://aclanthology.org/anthology-files/anthology-files/pdf/emnlp/2020.emnlp-main.213.pdf"},{"title":"(PDF) COMET: A Neural Framework for MT Evaluation","url":"https://www.researchgate.net/publication/347234911_COMET_A_Neural_Framework_for_MT_Evaluation"},{"title":"COMET: A Neural Framework for MT Evaluation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200909025R/abstract"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Ricardo+Rei%2C+Craig+Stewart%2C+Ana+C+Farinha%2C+and+Alon+Lavie.+2020.+COMET%3A+A+neural+framework+for+MT+evaluation.+arXiv+preprint+arXiv%3A2009.09025+%282020%29."},{"title":"[2009.09025] COMET: A Neural Framework for MT Evaluation","url":"https://arxiv.org/abs/2009.09025"},{"title":"[Quick Review] COMET: A Neural Framework for MT Evaluation","url":"https://liner.com/review/comet-neural-framework-for-mt-evaluation"},{"title":"Aclanthology","url":"https://aclanthology.org/2020.emnlp-main.213.bib"}]

I found the paper you're looking for. Here are the details:

**Citation:** Ricardo Rei, Craig Stewart, Ana C Farinha, and Alon Lavie. COMET: A Neural Framework for MT Evaluation. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 2685–2702, Online.

**Overview:** COMET is a neural framework for training multilingual machine translation evaluation models which obtains new state-of-the-art levels of correlation with human judgements. The framework le
…[truncated 866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-26T11:05:41.406062+00:00_

Web search results for query: "Templeton Conerly Marcus "Scaling Monosemanticity" Claude 3 Sonnet Anthropic 2024"

Web search error: unavailable

I apologize, but I encountered an error while attempting the web search. The search tool is currently unavailable. 

However, based on your query terms, this appears to be related to research from Anthropic about scaling monosemanticity in neural networks, potentially involving work by Templeton, Conerly, and Marcus on interpretability research with Claude 3 Sonnet. To find this information, I'd recommend:

1. Visiting Anthropic's official website or research page directly
2. Searching on arXiv.org for papers by these authors
3. Checking Anthropic's blog or publications section

Please try your search again in a moment, or let me know if you'd like help with anything else.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-26T11:05:41.406199+00:00_

Web search results for query: "Elhage Hume Olsson "Toy Models of Superposition" Transformer Circuits 2022 arXiv 2209.10652"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. However, I can provide some context about what you're searching for:

The query refers to a research paper on toy models of superposition in transformer neural networks. The arXiv identifier 2209.10652 indicates this is a paper from September 2022. The authors mentioned (Elhage, Hume, Olsson) are researchers associated with Anthropic who work on mechanistic interpretability—understanding how transformer models process and represent information internally.

The paper appears to be related to the Transformer Circuits research initiative, which focuses on reverse-engineering and understanding the mechanisms inside transformer models. The concept of "superposition" in this context refers to how neural networks can encode multiple features or concepts in overlapping ways within their internal representations.

If you need to access this specific paper, you can try:
1. Visiting arXiv directly at arxiv.org and searching for paper ID 2209.10652
2. Searching on Google Scholar
3. Visiting the Transformer Circuits website or Anthropic's research pages

Would you like help with anything else related to this research or topic?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-26T11:05:41.406341+00:00_

Web search results for query: "Feng Li Zhu "Fine-Grained Activation Steering" ICLR 2026 arXiv 2602.04428"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. However, based on your query, you're looking for information about a paper on "Fine-Grained Activation Steering" by Feng Li Zhu that appears to be associated with ICLR 2026 and has the arXiv identifier 2602.04428.

To find this paper, you could try:
1. **arXiv directly**: Visit arxiv.org and search for "2602.04428" or the full paper title
2. **ICLR 2026 conference site**: Check the official ICLR 2026 proceedings or accepted papers list
3. **Google Scholar**: Search for the paper title or arXiv ID
4. **Author's profile**: Look up the authors' pages on institutional websites or research platforms

If you have additional questions about the paper's content once you've found it, feel free to ask!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-26T11:05:41.406469+00:00_

Web search results for query: "Conneau Rinott Lample "XNLI Evaluating Cross-lingual Sentence Representations" EMNLP 2018"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. However, I can tell you that based on your query, you're looking for information about the XNLI dataset paper. This is a well-known paper by Alexis Conneau, Ruty Rinott, Holger Schwenk, and Guillaume Lample (note: Lample is one of the authors, though the exact author order may vary) that was published at EMNLP 2018.

The paper introduces XNLI (Cross-lingual Natural Language Inference), which is a dataset for evaluating cross-lingual sentence representations. If you need to access this paper, I'd recommend:

1. Searching directly on Google Scholar (scholar.google.com)
2. Checking the ACL Anthology (aclanthology.org)
3. Looking on arXiv for the preprint

These sources should have the full paper, citation information, and related details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-26T11:05:41.406639+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Grattafiori Dubey \"Llama 3 Herd of Models\" arXiv 2407.21783 Meta 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Grattafiori Dubey \"Llama 3 Herd of Models\" arXiv 2407.21783 Meta 2024"
  }
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-26T11:05:41.406768+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yang An \"Qwen3 Technical Report\" arXiv 2505.09388 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yang An \"Qwen3 Technical Report\" arXiv 2505.09388 2025"
  }
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-26T11:05:41.406903+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma Team Riviere \"Gemma 2 Improving Open Language Models\" arXiv 2408.00118"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma Team Riviere \"Gemma 2 Improving Open Language Models\" arXiv 2408.00118"
  }
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-26T11:05:41.407021+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Meng Bau Andonian Belinkov \"Locating and Editing Factual Associations in GPT\" NeurIPS 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Meng Bau Andonian Belinkov \"Locating and Editing Factual Associations in GPT\" NeurIPS 2022"
  }
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-26T11:05:41.407137+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pokharel Agrawal Nagar \"Cross-Lingual Activation Steering\" multilingual arXiv 2601.16390"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pokharel Agrawal Nagar \"Cross-Lingual Activation Steering\" multilingual arXiv 2601.16390"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-26T11:05:41.407285+00:00_

Web search results for query: "Meng Bau Andonian Belinkov "Locating and Editing Factual Associations in GPT" NeurIPS 2022"

Links: [{"title":"Locating and Editing Factual Associations in GPT","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html"},{"title":"Locating and Editing Factual Associations in GPT Kevin Meng⇤ MIT CSAIL","url":"https://proceedings.neurips.cc/paper_files/paper/2022/file/6f1d43d5a82a37e89b0665b33bf3a182-Paper-Conference.pdf"},{"title":"Locating and Editing Factual Associations in GPT","url":"https://rome.baulab.info/"},{"title":"[2202.05262] Locating and Editing Factual Associations in GPT","url":"https://arxiv.org/abs/2202.05262"},{"title":"[PDF] Locating and Editing Factual Associations in GPT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Locating-and-Editing-Factual-Associations-in-GPT-Meng-Bau/996445d847f06e99b0bd259345408a0cf1bce87e"},{"title":"Locating and Editing Factual Associations in GPT - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/locating-and-editing-factual-associations-in-gpt/"},{"title":"Locating and editing factual associations in GPT | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3600270.3601532"},{"title":"Locating and Editing Factual Associations in GPT Kevin Meng∗ MIT CSAIL","url":"https://arxiv.org/pdf/2202.05262"},{"title":"Locating and Editing Factual Associations in GPT - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2202.05262"},{"title":"GitHub - kmeng01/rome: Locating and editing factual associations in GPT (NeurIPS 2022) · GitHub","url":"https://github.com/kmeng01/rome"}]

I found the paper you're looking for! Here are the search results for "Locating and Editing Factual Associations in GPT" by Meng, Bau, Andonian, and Belinkov:

## Paper Overview

The paper analyzes the storage and reca
…[truncated 1229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-26T11:05:41.407437+00:00_

Web search results for query: "Pokharel Agrawal Nagar "Cross-Lingual Activation Steering" multilingual arXiv 2601.16390"

Links: [{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/pdf/2601.16390"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"},{"title":"SteerEval: Inference-time Interventions Strengthen Multilingual Generalization in Neural Summarization Metrics","url":"https://arxiv.org/pdf/2601.15809"},{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/pdf/2505.12584"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/pdf/2601.08331"}]

Based on the search results, I found the paper you were looking for:

**Cross-Lingual Activation Steering for Multilingual Language Models** by Rhitabrat Pokharel, Ameeta Agrawal, and Tanay Nagar

The paper addresses performance gaps between dominant and nondominant languages in large language models. The authors propose Cross-Lingual Activation Steering (CLAS), a training-free inference-time intervention that selectively modulates neuron activations. 

Their evaluation on classification and generation benchmarks achieved average improvements of 2.3% (Acc.) and 3.4% (F1) respectively, while maintaining high-resource language performance. The method unlocks latent multilingual capacity in existing models without modification to model weights.

The paper is available at: https://arxiv.org/pdf/2601.16390


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-26T11:05:41.407577+00:00_

Web search results for query: "Yang An "Qwen3 Technical Report" arXiv 2505.09388 2025"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. I'm unable to perform the search for the Yang An "Qwen3 Technical Report" arXiv 2505.09388 document at this moment.

If you're looking for this technical report, you can try accessing it directly through:
- **arXiv.org**: Visit arxiv.org and search for the paper ID 2505.09388
- **arXiv PDF**: Direct link format would be arxiv.org/pdf/2505.09388.pdf

Alternatively, you could try searching for "Qwen3 Technical Report" or the author name through academic search engines like Google Scholar.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-26T11:05:41.407704+00:00_

Web search results for query: "Grattafiori Dubey "Llama 3 Herd of Models" arXiv 2407.21783 Meta 2024"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. However, I can provide some context about what you're searching for based on my knowledge:

You're looking for a research paper about Meta's Llama 3 models. The citation you provided references:
- **Authors**: Grattafiori and Dubey (among others)
- **Title**: "Llama 3: A Herd of Models" 
- **arXiv ID**: 2407.21783
- **Year**: 2024
- **Organization**: Meta

This paper was published on arXiv in July 2024 and describes Meta's Llama 3 family of large language models. The "herd of models" refers to the multiple model variants released as part of the Llama 3 series.

If you need to access this paper directly, you can find it at: https://arxiv.org/abs/2407.21783

Unfortunately, I'm unable to retrieve the current web search results at this moment, but you should be able to access the full paper and citation information through the arXiv link above.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-26T11:05:41.407830+00:00_

Web search results for query: "Gemma Team Riviere "Gemma 2 Improving Open Language Models" arXiv 2408.00118"

Web search error: unavailable

I apologize, but I'm unable to complete the web search at this moment as the web search tool is temporarily unavailable. 

However, I can provide you with information about this paper based on my knowledge: The arXiv paper "Gemma 2: Improving Open Language Models" (2408.00118) is a research paper from the Gemma Team at Google that describes the Gemma 2 language model. The paper details improvements and architectural enhancements made to the open-source Gemma language model family.

If you need to access this paper directly, I recommend:
1. Visiting arXiv.org and searching for 2408.00118
2. Searching for the paper title on Google Scholar
3. Visiting the paper's page directly at arxiv.org/abs/2408.00118

Would you like me to help you with something else regarding this paper?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-26T11:05:41.408024+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sundar Williamson Metcalf \"Steering into New Embedding Spaces\" cross-lingual alignment ACL 2025 arXiv 2502.15639"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sundar Williamson Metcalf \"Steering into New Embedding Spaces\" cross-lingual alignment ACL 2025 arXiv 2502.15639"
  }
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-26T11:05:41.408147+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Geiger Wu Potts Icard Goodman \"Finding Alignments Between Interpretable Causal Variables\" CLeaR 2024 PMLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Geiger Wu Potts Icard Goodman \"Finding Alignments Between Interpretable Causal Variables\" CLeaR 2024 PMLR"
  }
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-26T11:05:41.408264+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Samuel Marks Max Tegmark \"Geometry of Truth\" ICLR 2024 OR 2025 which year accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Samuel Marks Max Tegmark \"Geometry of Truth\" ICLR 2024 OR 2025 which year accepted"
  }
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-26T11:05:41.408376+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kenneth Li inference-time intervention ITI truthful answers NeurIPS 2023 arXiv 2306.03341"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kenneth Li inference-time intervention ITI truthful answers NeurIPS 2023 arXiv 2306.03341"
  }
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-26T11:05:41.408487+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "deep-significance Ulmer Hardmeier Frellsen 2022 statistical testing neural networks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "deep-significance Ulmer Hardmeier Frellsen 2022 statistical testing neural networks"
  }
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-26T11:05:41.408630+00:00_

Web search results for query: "Geiger Wu Potts Icard Goodman "Finding Alignments Between Interpretable Causal Variables" CLeaR 2024 PMLR"

Links: [{"title":"[2303.02536] Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations","url":"https://arxiv.org/abs/2303.02536"},{"title":"Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations","url":"https://proceedings.mlr.press/v236/geiger24a.html"},{"title":"Finding Alignments Between Interpretable Causal Variables ...","url":"https://proceedings.mlr.press/v236/geiger24a/geiger24a.pdf"},{"title":"Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations","url":"https://arxiv.org/html/2303.02536v4"},{"title":"(PDF) Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations","url":"https://www.researchgate.net/publication/383739393_Finding_Alignments_Between_Interpretable_Causal_Variables_and_Distributed_Neural_Representations"},{"title":"[PDF] Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Finding-Alignments-Between-Interpretable-Causal-and-Geiger-Wu/cb1b5d949a1d711b1bd3a2924e045ad3f893252c"},{"title":"Atticus Geiger Stanford University atticusg@stanford.edu Education","url":"https://atticusg.github.io/assets/AtticusCV.pdf"},{"title":"dblp: Atticus Geiger","url":"https://dblp.org/pid/229/4086.html"},{"title":"dblp: Conference on Causal Learning and Reasoning","url":"https://dblp.org/db/conf/clear2/clear2024.html"},{"title":"C♥️LM @ NeurIPS 2024 | About - Causality and Large Models","url":"https://calm-workshop-2024.github.io/about/"}]

I found the paper you're looking for! Here are the details:

**"Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations"** by Atticus Geiger, Zhengxuan Wu, Christopher Potts, Thomas 
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-26T11:05:41.408799+00:00_

Web search results for query: "deep-significance Ulmer Hardmeier Frellsen 2022 statistical testing neural networks"

Links: [{"title":"A Sieve Quasi-likelihood Ratio Test for Neural Networks with   Applications to Genetic Association Studies","url":"https://arxiv.org/pdf/2212.08255"},{"title":"Testing for Normality with Neural Networks","url":"https://arxiv.org/pdf/2009.13831"},{"title":"deep-significance - Easy and Meaningful Statistical Significance Testing   in the Age of Neural Networks","url":"https://arxiv.org/pdf/2204.06815"},{"title":"Full Bayesian Significance Testing for Neural Networks","url":"https://arxiv.org/pdf/2401.13335"},{"title":"Feedforward neural networks as statistical models: Improving   interpretability through uncertainty quantification","url":"https://arxiv.org/pdf/2311.08139"},{"title":"Significance Tests for Neural Networks","url":"https://arxiv.org/pdf/1902.06021"}]

Based on the search results, I found the paper you're looking for:

**deep-significance** is a work by Dennis Ulmer, Christian Hardmeier, and Jes Frellsen from the Department of Computer Science at IT University of Copenhagen and the Department of Applied Mathematics and Computer Science at Technical University of Denmark.

The paper addresses the fact that statistical significance testing is still not widely used in Machine Learning and Deep Learning research, despite much of it being empirical in nature. The authors note that seeming improvements over baselines might be statistical flukes, and provide an easy-to-use package containing different significance tests and utility functions tailored towards research needs and usability.

The paper highlights a broader concern in the field: many proposed improvements in deep learning, such as enhancements to transformer architectures and new optimizers, have been found not to improve consistently over original models when benchmarked at scale.

You can access the full paper at: https://arxiv.org/pdf/2204.06815


REMINDER: You MUS
…[truncated 83 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-26T11:05:41.409001+00:00_

Web search results for query: "Sundar Williamson Metcalf "Steering into New Embedding Spaces" cross-lingual alignment ACL 2025 arXiv 2502.15639"

Links: [{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.118/"},{"title":"[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/abs/2502.15639"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/new-embedding-spaces"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/html/2502.15639v1"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://www.researchgate.net/publication/389274280_Steering_into_New_Embedding_Spaces_Analyzing_Cross-Lingual_Alignment_Induced_by_Model_Interventions_in_Multilingual_Language_Models"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/steering-into-new-embedding-spaces-analyzing-cross"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment","url":"https://arxiv.org/pdf/2502.15639"},{"title":"Computation and Language Feb 2025","url":"http://www.arxiv.org/list/cs.CL/2025-02?skip=1325&show=25"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - haebom",
…[truncated 1381 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-26T11:05:41.409156+00:00_

Web search results for query: "Kenneth Li inference-time intervention ITI truthful answers NeurIPS 2023 arXiv 2306.03341"

Web search error: unavailable

I apologize, but the web search tool is currently unavailable. However, I can provide some information based on my knowledge:

Kenneth Li is a researcher who worked on inference-time intervention (ITI), which is a technique for improving language model truthfulness. The paper you're referencing with arXiv ID 2306.03341 appears to be related to this work, presented at NeurIPS 2023. ITI is a method that intervenes during the inference process to help language models provide more truthful answers by manipulating internal activations.

To get the most current and detailed information about this specific paper, you could:
- Visit the arXiv website directly at arxiv.org/abs/2306.03341
- Check the NeurIPS 2023 conference proceedings
- Search for the paper title on Google Scholar

I apologize that I couldn't retrieve the live search results for you at this time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-26T11:05:41.409307+00:00_

Web search results for query: "Samuel Marks Max Tegmark "Geometry of Truth" ICLR 2024 OR 2025 which year accepted"

Links: [{"title":"Our Mathematical Universe?","url":"https://arxiv.org/pdf/1406.4348"},{"title":"The Geometry of Truth: Emergent Linear Structure in Large Language Model   Representations of True/False Datasets","url":"https://arxiv.org/pdf/2310.06824"},{"title":"How Context Shapes Truth: Geometric Transformations of Statement-level Truth Representations in LLMs","url":"https://arxiv.org/pdf/2601.06599"},{"title":"Refuting the Metaphysics of Wolfram and Tegmark","url":"https://arxiv.org/pdf/2411.12562"},{"title":"Gambling on the existence of other universes","url":"https://arxiv.org/pdf/1607.01775"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"The Geometries of Truth Are Orthogonal Across Tasks","url":"https://arxiv.org/pdf/2506.08572"}]

Based on the search results, I found that "The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets" is a paper by Samuel Marks and Max Tegmark. The paper is available on arxiv (arxiv ID: 2310.06824).

However, the search results do not explicitly state whether this paper was accepted to ICLR in 2024 or 2025. The arxiv version shows it was posted in October 2023 (based on the arxiv ID), but I cannot determine the ICLR acceptance year from these results. 

Let me search more specifically for the ICLR acceptance information:

Links: [{"title":"How Context Shapes Truth: Geometric Transformations of Statement-level Truth Representations in LLMs","url":"https://arxiv.org/pdf/2601.06599"},{"title":"Finding Belief Geometries with Sparse Autoencoders","url":"https://arxiv.org/pdf/2604.02685"},{"title":"The Geometries of Truth Are Orthogonal Across Tasks","url":"https://arxiv.org/pdf/2506.08572"},{"title":"The Confidence Manifold: Geometric Structure of Correctn
…[truncated 1046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-26T11:05:41.409489+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Marks Tegmark \"Geometry of Truth\" OpenReview ICLR 2024 accepted paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Marks Tegmark \"Geometry of Truth\" OpenReview ICLR 2024 accepted paper"
  }
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-26T11:05:41.409614+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Andy Zou representation engineering arXiv 2310.01405 top-down AI transparency 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Andy Zou representation engineering arXiv 2310.01405 top-down AI transparency 2023"
  }
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-26T11:05:41.409736+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Turner Thiergart Udell \"Activation Addition\" arXiv 2308.10248 steering language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Turner Thiergart Udell \"Activation Addition\" arXiv 2308.10248 steering language models"
  }
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-26T11:05:41.409867+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Elhage Hume Olsson \"Toy Models of Superposition\" arXiv 2209.10652 Anthropic transformer circuits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Elhage Hume Olsson \"Toy Models of Superposition\" arXiv 2209.10652 Anthropic transformer circuits"
  }
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-26T11:05:41.409987+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Templeton Conerly \"Scaling Monosemanticity\" extracting features Claude 3 Sonnet transformer circuits 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Templeton Conerly \"Scaling Monosemanticity\" extracting features Claude 3 Sonnet transformer circuits 2024"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-26T11:05:41.410133+00:00_

Web search results for query: "Andy Zou representation engineering arXiv 2310.01405 top-down AI transparency 2023"

Links: [{"title":"[2310.01405] Representation Engineering: A Top-Down Approach to AI Transparency","url":"https://arxiv.org/abs/2310.01405"},{"title":"GitHub - andyzoujm/representation-engineering: Representation Engineering: A Top-Down Approach to AI Transparency · GitHub","url":"https://github.com/andyzoujm/representation-engineering"},{"title":"Representation Engineering: A Top-Down Approach to AI Transparency - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231001405Z/abstract"},{"title":"dblp: Representation Engineering: A Top-Down Approach to AI Transparency.","url":"https://dblp.org/rec/journals/corr/abs-2310-01405.html"},{"title":"[PDF] Representation Engineering: A Top-Down Approach to AI Transparency | Semantic Scholar","url":"https://www.semanticscholar.org/paper/58fdf550600fc3873729d466601c5d08a51ba8a0"},{"title":"Paper page - Representation Engineering: A Top-Down Approach to AI Transparency","url":"https://huggingface.co/papers/2310.01405"},{"title":"‪Representation engineering: A top-down approach to ai transparency‬","url":"https://scholar.google.com/citations?view_op=view_citation&hl=en&user=tMYCvLAAAAAJ&citation_for_view=tMYCvLAAAAAJ:mWEH9CqjF64C"},{"title":"Representation Engineering: A Top-Down Approach to AI Transparency | Montreal AI Ethics Institute","url":"https://montrealethics.ai/representation-engineering-a-top-down-approach-to-ai-transparency/"},{"title":"[2310.01405v2] Representation Engineering: A Top-Down Approach to AI Transparency","url":"https://arxiv.org/abs/2310.01405v2"}]

Based on the search results, here's what I found about this paper:

## Representation Engineering: A Top-Down Approach to AI Transparency

The paper identifies and characterizes the emerging area of representation engineering (RepE), an approach to enhancing the transparency of AI systems that draws on insights from cognitive neuroscience.
…[truncated 946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-26T11:05:41.410292+00:00_

Web search results for query: "Marks Tegmark "Geometry of Truth" OpenReview ICLR 2024 accepted paper"

Links: [{"title":"The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets | OpenReview","url":"https://openreview.net/forum?id=CeJEfNKstt"},{"title":"[2310.06824] The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets","url":"https://arxiv.org/abs/2310.06824"},{"title":"[PDF] The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Geometry-of-Truth:-Emergent-Linear-Structure-in-Marks-Tegmark/d59523889679aee15992c4bf6e52b134186d07d3"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf"},{"title":"Published at Building Trust Workshop at ICLR 2025 UNDERSTANDING (UN)RELIABILITY","url":"https://openreview.net/pdf?id=JZiKuvIK1t"},{"title":"Under review as a conference paper at ICLR 2024 THE GEOMETRY OF TRUTH:","url":"https://openreview.net/pdf/ecf0f5b60fb4cd799686107990850d5666d15368.pdf"},{"title":"BELIEF DYNAMICS REVEAL THE DUAL NATURE OF IN- ...","url":"https://openreview.net/pdf/435745c61c9d0f08242a758ee05793c33a2f0d68.pdf"},{"title":"[2310.06824v3] The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets","url":"https://arxiv.org/abs/2310.06824v3"},{"title":"Probing the Geometry of Truth: Consistency and ...","url":"https://aclanthology.org/2025.findings-acl.38.pdf"}]

Based on the search results, I found information about the paper "The Geometry of Truth" by Samuel Marks and Max Tegmark:

The paper investigates how LLMs represent the difference between true and false statements, and improves techniques for extracting LLM beliefs.

The paper is authored by Sa
…[truncated 544 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-26T11:05:41.410464+00:00_

Web search results for query: "Turner Thiergart Udell "Activation Addition" arXiv 2308.10248 steering language models"

Links: [{"title":"[2308.10248] Steering Language Models With Activation Engineering","url":"https://arxiv.org/abs/2308.10248"},{"title":"Activation Addition: Steering Language Models Without Optimization","url":"https://arxiv.org/html/2308.10248v4"},{"title":"[2308.10248] Activation Addition: Steering Language Models Without Optimization","url":"https://ar5iv.labs.arxiv.org/html/2308.10248"},{"title":"Activation Addition: Steering Language Models Without Optimization - University of Bristol","url":"https://research-information.bris.ac.uk/en/publications/activation-addition-steering-language-models-without-optimization/"},{"title":"Paper page - Activation Addition: Steering Language Models Without Optimization","url":"https://huggingface.co/papers/2308.10248"},{"title":"(PDF) Activation Addition: Steering Language Models Without Optimization","url":"https://www.researchgate.net/publication/373262948_Activation_Addition_Steering_Language_Models_Without_Optimization"},{"title":"[2308.10248v3] Activation Addition: Steering Language Models Without Optimization","url":"https://arxiv.org/abs/2308.10248v3"},{"title":"[2308.10248v5] Steering Language Models With Activation Engineering","url":"http://arxiv.org/abs/2308.10248v5"}]

Based on the search results, here's what I found about this paper:

## Paper Overview

The paper is titled "Activation Addition: Steering Language Models Without Optimization", with arXiv ID 2308.10248. The authors are Alexander Matt Turner, Lisa Thiergart, David Udell, Gavin Leech, Ulisse Mini, and Monte MacDiarmid.

## Main Contribution

The paper investigates activation engineering—modifying activations at inference-time to predictably alter model behavior—and introduces the Activation Addition (ActAdd) method, which computes steering vectors by taking activation differences resulting from pairs of prompts.

## Key Features

Act
…[truncated 507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-26T11:05:41.410628+00:00_

Web search results for query: "Elhage Hume Olsson "Toy Models of Superposition" arXiv 2209.10652 Anthropic transformer circuits"

Links: [{"title":"[2209.10652] Toy Models of Superposition","url":"https://arxiv.org/abs/2209.10652"},{"title":"Toy Models of Superposition","url":"https://transformer-circuits.pub/2022/toy_model/index.html"},{"title":"Toy Models of Superposition - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220910652E/abstract"},{"title":"ToyModelsof Superposition","url":"https://arxiv.org/pdf/2209.10652"},{"title":"Paper page - Toy Models of Superposition","url":"https://huggingface.co/papers/2209.10652"},{"title":"[2209.10652v1] Toy Models of Superposition","url":"https://arxiv.org/abs/2209.10652v1"},{"title":"dblp: Toy Models of Superposition.","url":"https://dblp.org/rec/journals/corr/abs-2209-10652.html"},{"title":"Toy Models of Superposition","url":"https://www.researchgate.net/publication/363766017_Toy_Models_of_Superposition"},{"title":"[PDF] Toy Models of Superposition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Toy-Models-of-Superposition-Elhage-Hume/9d125f45b1d2dea01f05281470bc08e12b6c7cba"},{"title":"Toy Models of Superposition","url":"https://bibbase.org/network/publication/elhage-hume-olsson-schiefer-henighan-kravec-hatfielddodds-lasenby-etal-toymodelsofsuperposition-2022"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

"Toy Models of Superposition" is a paper by Nelson Elhage, Tristan Hume, Catherine Olsson, and other researchers, published in September 2022 with the arXiv identifier 2209.10652.

The paper provides a toy model where polysemanticity can be fully understood, arising as a result of models storing additional sparse features in "superposition." The research demonstrates the existence of a phase change, a surprising connection to the geometry of uniform polytopes, and evidence of a link to adversarial examples.

The paper addresses a fundament
…[truncated 513 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-26T11:05:41.410803+00:00_

Web search results for query: "Templeton Conerly "Scaling Monosemanticity" extracting features Claude 3 Sonnet transformer circuits 2024"

Links: [{"title":"Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet","url":"https://transformer-circuits.pub/2024/scaling-monosemanticity/"},{"title":"Reading: Scaling Monosemanticity -- Extracting Interpretable Features from Claude 3 Sonnet — Andrew Silva","url":"https://www.andrew-silva.com/blog/reading-scaling-monosemanticity-extracting-interpretable-features-from-claude-3-sonnet"},{"title":"Encourage or Inhibit Monosemanticity? Revisit Monosemanticity","url":"https://arxiv.org/pdf/2406.17969"},{"title":"Scaling Monosemanticity_ Extracting Interpretable Features from Claude 3 Sonnet","url":"https://www.scribd.com/document/757175658/Scaling-Monosemanticity-Extracting-Interpretable-Features-from-Claude-3-Sonnet"},{"title":"Scaling Monosemanticity: Extracting Interpretable Features From Claude 3 Sonnet","url":"https://www.pelayoarbues.com/literature-notes/Articles/Scaling-Monosemanticity-Extracting-Interpretable-Features-From-Claude-3-Sonnet"},{"title":"arXiv:2409.04478v1 [cs.LG] 5 Sep 2024","url":"https://arxiv.org/pdf/2409.04478"},{"title":"ArXiv Dives: Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet","url":"https://ghost.oxen.ai/scaling-monosemanticity-claude-3/"},{"title":"Scaling Monosemanticity and Feature Steering | Learn Mechanistic Interpretability","url":"https://learnmechinterp.com/topics/scaling-monosemanticity/"},{"title":"Automatically Interpreting Millions of Features in Large Language Models","url":"https://arxiv.org/pdf/2410.13928"}]

I found the research you're looking for. Here's what the search revealed:

"Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet" is a work by Adly Templeton, Tom Conerly, and many collaborators from Anthropic, which demonstrates extracting high-quality features from Claude 3 Sonnet. The researc
…[truncated 868 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-26T11:05:41.411071+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Feng Zihao Li Tian \"Fine-Grained Activation Steering\" ICLR 2026 arXiv 2602.04428"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Feng Zihao Li Tian \"Fine-Grained Activation Steering\" ICLR 2026 arXiv 2602.04428"
  }
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-26T11:05:41.411214+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Conneau Rinott Lample Williams Bowman XNLI cross-lingual sentence representations EMNLP 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Conneau Rinott Lample Williams Bowman XNLI cross-lingual sentence representations EMNLP 2018"
  }
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-26T11:05:41.411336+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Grattafiori \"Llama 3 Herd of Models\" Meta AI 2024 arXiv 2407.21783"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Grattafiori \"Llama 3 Herd of Models\" Meta AI 2024 arXiv 2407.21783"
  }
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-26T11:05:41.411451+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3 Technical Report arXiv 2505.09388 Yang 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3 Technical Report arXiv 2505.09388 Yang 2025"
  }
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-26T11:05:41.411565+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma Team \"Gemma 2 Improving Open Language Models Practical Size\" arXiv 2408.00118 Google 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma Team \"Gemma 2 Improving Open Language Models Practical Size\" arXiv 2408.00118 Google 2024"
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-26T11:05:41.411713+00:00_

Web search results for query: "Conneau Rinott Lample Williams Bowman XNLI cross-lingual sentence representations EMNLP 2018"

Links: [{"title":"XNLI: Evaluating Cross-lingual Sentence Representations - ACL Anthology","url":"https://aclanthology.org/D18-1269/"},{"title":"[1809.05053] XNLI: Evaluating Cross-lingual Sentence Representations","url":"https://arxiv.org/abs/1809.05053"},{"title":"XNLI","url":"https://cims.nyu.edu/~sbowman/xnli/"},{"title":"[Quick Review] XNLI: Evaluating Cross-lingual Sentence Representations","url":"https://liner.com/review/xnli-evaluating-crosslingual-sentence-representations"},{"title":"dblp: XNLI: Evaluating Cross-lingual Sentence Representations.","url":"https://dblp.org/rec/conf/emnlp/ConneauRLWBSS18.html"},{"title":"[PDF] XNLI: Evaluating Cross-lingual Sentence Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XNLI:-Evaluating-Cross-lingual-Sentence-Conneau-Lample/1c3112ef8a346b9817382ed34a8c146c53d5bcf5"},{"title":"GitHub - facebookresearch/XNLI: Evaluating Cross-lingual Sentence Representations · GitHub","url":"https://github.com/facebookresearch/XNLI"},{"title":"2018: XNLI: Evaluating Cross-lingual Sentence Representations · Issue #155 · jojonki/arXivNotes","url":"https://github.com/jojonki/arXivNotes/issues/155"},{"title":"Table 1 from XNLI: Evaluating Cross-lingual Sentence Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XNLI:-Evaluating-Cross-lingual-Sentence-Conneau-Lample/1c3112ef8a346b9817382ed34a8c146c53d5bcf5/figure/0"},{"title":"[1809.05053v1] XNLI: Evaluating Cross-lingual Sentence Representations","url":"https://arxiv.org/abs/1809.05053v1"}]

I found the paper! Here are the search results for the query about the XNLI cross-lingual sentence representations paper:

The paper "XNLI: Evaluating Cross-lingual Sentence Representations" was authored by Alexis Conneau, Ruty Rinott, Guillaume Lample, Adina Williams, Samuel Bowman, Holger Schwenk, and Veselin Stoyan
…[truncated 931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-26T11:05:41.411894+00:00_

Web search results for query: "Grattafiori "Llama 3 Herd of Models" Meta AI 2024 arXiv 2407.21783"

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"The Llama 3 Herd of Models Llama Team, AI @ Meta1","url":"https://arxiv.org/pdf/2407.21783v3"},{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"},{"title":"The Llama 3 herd of models - Archive ouverte HAL","url":"https://hal.science/hal-05414211"},{"title":"The Llama 3 Herd of Models. Paper Review | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/the-llama-3-herd-of-models-2f62252ce1c8"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=The+llama+3+herd+of+models&amp=&author=Grattafiori,+A.&amp=&author=Dubey,+A.&amp=&author=Jauhri,+A.&amp=&author=Pandey,+A.&amp=&author=Kadian,+A.&amp=&author=Al-Dahle,+A.&amp=&author=Letman,+A.&amp=&author=Mathur,+A.&amp=&author=Schelten,+A.&amp=&author=Vaughan,+A.&amp=&author=et+al.&amp=&publication_year=2024&amp=&journal=arXiv&amp=&doi=10.48550/arXiv.2407.21783"}]

I found the paper you're looking for! Here are the search results:

## "The Llama 3 Herd of Models" - arXiv 2407.21783

This paper presents a new set of foundation models, called Llama 3, which is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage. The largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens.

Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks.

The paper has multiple
…[truncated 594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-26T11:05:41.412067+00:00_

Web search results for query: "Gemma Team "Gemma 2 Improving Open Language Models Practical Size" arXiv 2408.00118 Google 2024"

Links: [{"title":"[2408.00118] Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/abs/2408.00118"},{"title":"Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/html/2408.00118v1"},{"title":"2024-06-27 Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/pdf/2408.00118"},{"title":"(PDF) Gemma 2: Improving Open Language Models at a Practical Size","url":"https://www.researchgate.net/publication/382797528_Gemma_2_Improving_Open_Language_Models_at_a_Practical_Size"},{"title":"Gemma 2: Improving Open Language Models at a Practical Size - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240800118G/abstract"},{"title":"[PDF] Gemma 2: Improving Open Language Models at a Practical Size | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Gemma-2:-Improving-Open-Language-Models-at-a-Size-Riviere-Pathak/ec2ce4e38af8bc82f1b8928ba51a84911bad0cc6"},{"title":"[2408.00118v1] Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/abs/2408.00118v1"},{"title":"[2408.00118] Gemma 2: Improving Open Language Models at a Practical Size","url":"http://export.arxiv.org/abs/2408.00118"},{"title":"[2408.00118v3] Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/abs/2408.00118v3"}]

I found the arXiv paper you were searching for. Here's what I found:

Gemma 2 is a new addition to the Gemma family of lightweight, state-of-the-art open models, ranging in scale from 2 billion to 27 billion parameters. The paper applies several known technical modifications to the Transformer architecture, such as interleaving local-global attentions and group-query attention. The 2B and 9B models are trained with knowledge distillation instead of next token prediction.

The resulting models deliver the
…[truncated 487 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-26T11:05:41.412231+00:00_

Web search results for query: "Qwen3 Technical Report arXiv 2505.09388 Yang 2025"

Links: [{"title":"[2505.09388] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388"},{"title":"Paper page - Qwen3 Technical Report","url":"https://huggingface.co/papers/2505.09388"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/391741196_Qwen3_Technical_Report"},{"title":"[2505.09388] Qwen3 Technical Report - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2505.09388"},{"title":"[2505.09388v1] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388v1"},{"title":"Qwen3-Omni Technical Report","url":"https://arxiv.org/html/2509.17765v1"}]

I found the Qwen3 Technical Report for you. Here's what I can tell you about this paper:

The Qwen3 Technical Report (arXiv:2505.09388) was submitted on May 14, 2025, authored by An Yang and 59 other co-authors.

Qwen3 is the latest version of the Qwen model family, comprising a series of large language models (LLMs) designed to advance performance, efficiency, and multilingual capabilities. The Qwen3 series includes models of both dense and Mixture-of-Expert (MoE) architectures, with parameter scales ranging from 0.6 to 235 billion.

Key innovations include:
- Integration of thinking mode (for complex, multi-step reasoning) and non-thinking mode (for rapid, context-driven responses) into a unified framework, eliminating the need to switch between different models
- A thinking budget mechanism allowing users to allocate computational resources adaptively during inference
- Expanded multilingual support from 29 to 119 languages and dialects compared to its predecessor Qwen2.5

Empirical evaluations demonstrate that Qwen3 achieves state-of-the-art results across diverse benchmarks, including tasks in code generation, mathematical reasoning, and agent task
…[truncated 172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-26T11:05:41.412411+00:00_

Web search results for query: "Feng Zihao Li Tian "Fine-Grained Activation Steering" ICLR 2026 arXiv 2602.04428"

Links: [{"title":"ICLR 2026 Thursday 04/23","url":"https://iclr.cc/virtual/2026/day/4/23"},{"title":"Zihao Li","url":"https://www.zihao.website/"},{"title":"ICLR 2025 Spotlights","url":"https://iclr.cc/virtual/2025/events/spotlight-posters"},{"title":"Cao, Yixin Homepage - Homepage","url":"https://taominer.github.io/"},{"title":"ICLR 2026 Saturday 04/25","url":"https://iclr.cc/virtual/2026/day/4/25"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"Computer Vision and Pattern Recognition May 2025","url":"https://arxiv.org/list/cs.CV/2025-05?skip=2125&show=1000"}]

Let me search more specifically for this paper with the arXiv ID:

Links: [{"title":"[2602.04428] Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/abs/2602.04428"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/html/2602.04428"},{"title":"[2604.04428] Delay-Controlled Heterogeneous Nucleation in Adaptive Dynamical Networks","url":"https://arxiv.org/abs/2604.04428"},{"title":"Evidence that short period AM CVn systems are diverse in ...","url":"https://arxiv.org/pdf/2102.04428"},{"title":"[2603.04428] Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices","url":"https://arxiv.org/abs/2603.04428"},{"title":"Arxiv","url":"http://arxiv.org/pdf/2409.04428"},{"title":"Quantum Physics May 2022","url":"https://arxiv.org/list/quant-ph/2022-05?skip=195&show=2000"},{"title":"[2507.04428] ARMR: Adaptively Responsive Network for Medication Recommendation","url":"https://arxiv.org/abs/2507.04428"},{"title":"DexH2R: Task-oriented Dexterous Manipulation from Human to Robots","url":"https://www.arxiv.org/pdf/2411.04428"},{"title":"[2406.04428] MoralBench: Moral Evaluation of LLMs","url":"https://arxiv.org/abs/2406.0
…[truncated 2115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-26T11:05:41.412608+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kenneth Li Oam Patel Fernanda Viegas \"Inference-Time Intervention\" NeurIPS 2023 truthful"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kenneth Li Oam Patel Fernanda Viegas \"Inference-Time Intervention\" NeurIPS 2023 truthful"
  }
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-26T11:05:41.412766+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kargaran Modarressi MEXA arXiv 2410.05873 venue ACL 2025 Findings published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kargaran Modarressi MEXA arXiv 2410.05873 venue ACL 2025 Findings published"
  }
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-26T11:05:41.412915+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Emerging Cross-lingual Structure\" Shijie Wu first author ACL 2020 aclanthology 2020.acl-main.536"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Emerging Cross-lingual Structure\" Shijie Wu first author ACL 2020 aclanthology 2020.acl-main.536"
  }
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-26T11:05:41.413038+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "sundar2025steering ACL 2025 \"Skyler Seto\" OR \"Skyler Zhao\" OR \"Dan Jurafsky\" OR \"Masha Fedzechkina\" authors steering embedding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "sundar2025steering ACL 2025 \"Skyler Seto\" OR \"Skyler Zhao\" OR \"Dan Jurafsky\" OR \"Masha Fedzechkina\" authors steering embedding"
  }
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-26T11:05:41.413156+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ravichander2021probing EACL 2021 pages \"3331\" OR \"3363\" probing paradigm"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ravichander2021probing EACL 2021 pages \"3331\" OR \"3363\" probing paradigm"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-26T11:05:41.413305+00:00_

Web search results for query: "Kargaran Modarressi MEXA arXiv 2410.05873 venue ACL 2025 Findings published"

Links: [{"title":"[2410.05873] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://arxiv.org/abs/2410.05873"},{"title":"arXiv:2410.05873v2 [cs.CL] 1 Jun 2025","url":"https://arxiv.org/pdf/2410.05873"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://arxiv.org/html/2410.05873"},{"title":"(PDF) MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://www.researchgate.net/publication/384771337_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1385/"},{"title":"publications | Amir Hossein Kargaran","url":"https://kargaranamir.github.io/publications/"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | Request PDF","url":"https://www.researchgate.net/publication/394303914_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"},{"title":"GitHub - cisnlp/MEXA: 🔍 Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://github.com/cisnlp/MEXA"}]

Based on the search results, I found the information you requested:

The paper "MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment" by Kargaran, Modarressi, Nikeghbal, Diesner, Yvon, and Schütze was published in the Findings of the Association for Computational Linguistics: ACL 2025 in Vienna, Austria.

The paper's arXiv identifier is 2410.05873, and it introduces MEXA, a method for assessing the multilingual capabilities of pre-trained English-centric LLMs using parallel sentences.


REMINDER: You MUST include the sources above in your response to the user usi
…[truncated 23 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-26T11:05:41.413496+00:00_

Web search results for query: "Kenneth Li Oam Patel Fernanda Viegas "Inference-Time Intervention" NeurIPS 2023 truthful"

Links: [{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/81b8390039b7302c909cb769f8b6cd93-Abstract-Conference.html"},{"title":"NeurIPS Poster Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://neurips.cc/virtual/2023/poster/71200"},{"title":"[2306.03341] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/abs/2306.03341"},{"title":"Inference-time intervention | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667919"},{"title":"[PDF] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Inference-Time-Intervention:-Eliciting-Truthful-a-Li-Patel/405f8f5f1c6df1b3343c812832479aad5180b65f"},{"title":"[2306.03341] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"http://export.arxiv.org/abs/2306.03341"},{"title":"[2306.03341v6] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/abs/2306.03341v6"},{"title":"(PDF) Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://www.researchgate.net/publication/371347185_Inference-Time_Intervention_Eliciting_Truthful_Answers_from_a_Language_Model"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230603341L/abstract"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | Request PDF","url":"https://www.researchgate.net/publication/401462667_Inference-Time_Intervention_Eliciting_Truthful_
…[truncated 1229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-26T11:05:41.413672+00:00_

Web search results for query: ""Emerging Cross-lingual Structure" Shijie Wu first author ACL 2020 aclanthology 2020.acl-main.536"

Links: [{"title":"Emerging Cross-lingual Structure in Pretrained Language Models - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.536/"},{"title":"Emerging Cross-lingual Structure in Pretrained Language Models - ACL Anthology","url":"https://www.aclweb.org/anthology/2020.acl-main.536/"},{"title":"[1911.01464] Emerging Cross-lingual Structure in Pretrained Language Models","url":"https://arxiv.org/abs/1911.01464"},{"title":"ACL2020: Emerging Cross-lingual Structure in Pretrained Language Models","url":"https://virtual.acl2020.org/paper_main.536.html"},{"title":"[PDF] Emerging Cross-lingual Structure in Pretrained Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Emerging-Cross-lingual-Structure-in-Pretrained-Wu-Conneau/cfe8ec7a183ed548db1a862e38908343cefb94c7"},{"title":"GitHub - shijie-wu/crosslingual-nlp: This repo supports various cross-lingual transfer learning & multilingual NLP models. · GitHub","url":"https://github.com/shijie-wu/crosslingual-nlp"},{"title":"Shijie Wu - ACL Anthology","url":"https://aclanthology.org/people/shijie-wu/"},{"title":"crosslingual-nlp/README.md at master · shijie-wu/crosslingual-nlp","url":"https://github.com/shijie-wu/crosslingual-nlp/blob/master/README.md"},{"title":"dblp: Shijie Wu","url":"https://dblp.org/pid/225/7822.html"}]

I found the paper you're looking for! Here are the details:

**Paper Title:** Emerging Cross-lingual Structure in Pretrained Language Models

**Authors:** Alexis Conneau, Shijie Wu, Haoran Li, Luke Zettlemoyer, and Veselin Stoyanov

**Publication:** Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 6022–6034, Online, 2020

**DOI:** 10.18653/v1/2020.acl-main.536

**URL:** https://aclanthology.org/2020.acl-main.536/

**Summary:** The paper studies multilingual masked language modeling—the tr
…[truncated 567 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-26T11:05:41.413861+00:00_

Web search results for query: "sundar2025steering ACL 2025 "Skyler Seto" OR "Skyler Zhao" OR "Dan Jurafsky" OR "Masha Fedzechkina" authors steering embedding"

Links: [{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.118/"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/abs/2502.15639"},{"title":"ExpertLens: Activation steering features are highly interpretable","url":"https://arxiv.org/html/2502.15090v4"},{"title":"Skyler Seto","url":"https://www.catalyzex.com/author/Skyler%20Seto"},{"title":"Masha Fedzechkina - ACL Anthology","url":"https://aclanthology.org/people/m/masha-fedzechkina/"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/new-embedding-spaces"},{"title":"Skyler Seto - ACL Anthology","url":"https://aclanthology.org/people/skyler-seto/"},{"title":"[2502.15090] ExpertLens: Activation steering features are highly interpretable","url":"https://arxiv.org/abs/2502.15090"}]

Based on the search results, I found the paper you're looking for:

The paper is titled "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models" by authors Anirudh Sundar, Sinead Williamson, Katherine Metcalf, Barry-John Theobald, Skyler Seto, and Masha Fedzechkina.

The paper was published in Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 2375–2401, Vienna, Austria.

The r
…[truncated 463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-26T11:05:41.414041+00:00_

Web search results for query: "ravichander2021probing EACL 2021 pages "3331" OR "3363" probing paradigm"

Links: [{"title":"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance? - ACL Anthology","url":"https://aclanthology.org/2021.eacl-main.295/"},{"title":"[PDF] Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Probing-the-Probing-Paradigm:-Does-Probing-Accuracy-Ravichander-Belinkov/922535984641f052d2530c8b68f9ebd7de38dfa5"},{"title":"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance? | BibSonomy","url":"https://www.bibsonomy.org/bibtex/15bec2b4359ea3220160a8cabf93f4b9d"},{"title":"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance? | Request PDF","url":"https://www.researchgate.net/publication/355434387_Probing_the_Probing_Paradigm_Does_Probing_Accuracy_Entail_Task_Relevance"},{"title":"Does Probing Accuracy Entail Task Relevance?","url":"https://aclanthology.org/2021.eacl-main.295.pdf"},{"title":"(PDF) Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?","url":"https://www.academia.edu/73427358/Probing_the_Probing_Paradigm_Does_Probing_Accuracy_Entail_Task_Relevance?uc-sb-sw=57295190"},{"title":"[2005.00719] Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?","url":"https://arxiv.org/abs/2005.00719"},{"title":"Probing via Prompting","url":"https://aclanthology.org/2022.naacl-main.84.pdf"}]

Based on the search results, I found the paper you're looking for:

The paper "Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?" by Ravichander, Belinkov, and Hovy was published in the Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics, pages 3363–3377.

Note that the page numbers in the published version are 3363–3377, not 3331. The paper examines the probing paradigm through a case study in 
…[truncated 265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_B_20260526T105303",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 175 · 2026-05-26T11:05:41.414361+00:00_

All searches complete. Now let me compile the full verification report. Every paper has been verified as real. I found 11 entries with issues.

## 引用核查报告（Worker B）

**总引用数**: 38 条
**问题数**: 10 条（ERROR: 7, WARNING: 3）

### 逐条结果

1. `pimentel2021probing`: Pimentel, Cotterell (2021). "A Bayesian Framework for Information-Theoretic Probing". EMNLP 2021.
   - 真实性: ✓
   - 作者: ✓
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **OK**

2. `ravichander2021probing`: Ravichander, Belinkov, Hovy (2021). "Probing the Probing Paradigm". EACL 2021.
   - 真实性: ✓
   - 作者: ✓
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - Pages: ✗ **bib 写 3331–3350，ACL Anthology 实际为 3363–3377**
   - cite 上下文: ✓
   - 综合: **WARNING**（页码错误，不影响识别但不严谨）

3. `gurgurov2026clasbench`: Gurgurov et al. (2026). "CLaS-Bench". arXiv 2601.08331.
   - 真实性: ✓
   - 作者: ✓
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **OK**

4. `basu2026interpretability`: Basu et al. (2026). "Interpretability without Actionability". arXiv 2603.18353.
   - 真实性: ✓
   - 作者: ✓
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **OK**

5. `brink2026probing`: Brink, Boer, Ulmer (2026). "Probing for Knowledge Attribution in LLMs". arXiv 2602.22787.
   - 真实性: ✓
   - 作者: ✓
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **OK**

6. `ifergan2024beneath`: Ifergan et al. "Beneath the Surface of Consistency". Findings NAACL 2025.
   - 真实性: ✓
   - 作者: ✗ **第一作者名 "Matan" 应为 "Maxim"**
   - 年份: ✗ **bib year=2024 但 venue 是 NAACL 2025，应为 2025**
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **ERROR**

7. `li2025taming`: Li, Chen, Tong (2025). "Taming Knowledge Conflicts in Language Models". ICML 2025.
   - 真实性: ✓
   - 作者: ✗ **第二作者 "Yufei" Chen 应为 "Yuzhong" Chen**（ICML proceedings 及 arXiv 确认）
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **ERROR**

8. `pham2026where`: Pham, Borkakoty, Hou (2026). "Where Knowledge Collides". arXiv 2601.09445.
   - 真实性: ✓
   - 作者: ✗ **第二作者 "Hrishav" Borkakoty 应为 "Hsuvas" Borkakoty**（dblp、个人主页、arXiv 确认）
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **ERROR**

9. `wang2025lost`: Wang et al. (2025). "Lost in Multilinguality". ACL 2025.
   - 真实性: ✓
   - 作者: ✗ **缺少 2 位作者：Yihong Liu、Ercong Nie**（ACL Anthology 确认共 7 位作者，bib 只列了 5 位）
   - 年份: ✓
   - 标题: ✓
   - Venue: ✓
   - cite 上下文: ✓
   - 综合: **WARNING**

10. `xie2024adaptive`: Xie et al. (2024). "Adaptive Chameleon or Stubborn Sloth". ICLR 2024.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

11. `xing2024evaluating`: Xing et al. (2024). "Evaluating Knowledge-based Cross-lingual Inconsistency". arXiv 2407.01358.
    - 真实性: ✓
    - 作者: ✗ **4/6 作者名严重错误**：Xiaoling→**Xiaolin**, Zhenhui→**Zhiwei**, Huiyun→**Haoyu**, Xin→**Xing**（arXiv 及 dblp 确认）
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **ERROR**（严重——大面积作者名错误）

12. `xu2024knowledge`: Xu et al. (2024). "Knowledge Conflicts for LLMs: A Survey". EMNLP 2024.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

13. `zhao2024analysing`: Zhao et al. (2024). "Analysing the Residual Stream...Under Knowledge Conflicts". NeurIPS 2024 Workshop.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

14. `zhao2025steering`: Zhao et al. (2025). "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering". NAACL 2025.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

15. `zhao2026when`: Zhao et al. (2026). "When Abundance Conceals Weakness". arXiv 2601.07041.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

16. `wu2020emerging`: Wu, Conneau et al. (2020). "Emerging Cross-lingual Structure in Pretrained Language Models". ACL 2020.
    - 真实性: ✓
    - 作者: ✓（Shijie Wu 确为第一作者）
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

17. `wendler2024llamas`: Wendler et al. (2024). "Do Llamas Work in English?". ACL 2024.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

18. `muller2021first`: Muller et al. (2021). "First Align, then Predict". EACL 2021.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

19. `kargaran2024mexa`: Kargaran et al. "MEXA". Findings ACL 2025.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✗ **bib year=2024 但 venue 是 Findings ACL 2025，应为 2025**
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **WARNING**（年份与 venue 不一致）

20. `belinkov2022probing`: Belinkov (2022). "Probing Classifiers: Promises, Shortcomings, and Advances". Computational Linguistics Vol.48 No.1.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

21. `hewitt2019designing`: Hewitt, Liang (2019). "Designing and Interpreting Probes with Control Tasks". EMNLP 2019.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

22. `ulmer2022deep`: Ulmer, Hardmeier, Frellsen (2022). "deep-significance". arXiv 2204.06815.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

23. `li2023iti`: Li et al. (2023). "Inference-Time Intervention". NeurIPS 2023.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

24. `zou2023representation`: Zou et al. (2023). "Representation Engineering". arXiv 2310.01405.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

25. `turner2023activation`: Turner et al. (2023). "Activation Addition: Steering Language Models Without Optimization". arXiv 2308.10248.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓（原始版本标题，后续版本改名为 "Steering Language Models With Activation Engineering"，但引用原标题有效）
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

26. `marks2024geometry`: Marks, Tegmark. "The Geometry of Truth". ICLR.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✗ **bib year=2024，但论文实际发表于 ICLR 2025**（OpenReview 确认 "Published as a conference paper at ICLR 2025"）。bib 中 "13th ICLR" 对应的是 ICLR 2025，与 year=2024 矛盾。
    - 标题: ✓
    - Venue: ✗ **应为 ICLR 2025（第 13 届），非 2024**
    - cite 上下文: ✓
    - 综合: **ERROR**

27. `elhage2022toy`: Elhage et al. (2022). "Toy Models of Superposition". Transformer Circuits Thread.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

28. `templeton2024scaling`: Templeton et al. (2024). "Scaling Monosemanticity". Transformer Circuits Thread.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

29. `feng2026finegrained`: Feng et al. (2026). "Fine-Grained Activation Steering: Steering Less, Achieving More". ICLR 2026.
    - 真实性: ✓
    - 作者: ✗ **几乎全部作者名错误，且缺少 3 位作者**。bib 列 7 人，实际 10 人。具体错误：Zihao→**Zijian**, Tian→**Tianjiao**, Zhengyu→**Zixiao**, Hao→**Hanzhang**, Junliang→**Junlang**, Lin→**Li** (Zhang), Kede→**Kezhi** (Mao)。缺少：Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng。
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **ERROR**（最严重——大面积作者名腐坏 + 漏人）

30. `conneau2018xnli`: Conneau et al. (2018). "XNLI: Evaluating Cross-lingual Sentence Representations". EMNLP 2018.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

31. `rei2020comet`: Rei et al. (2020). "COMET: A Neural Framework for MT Evaluation". EMNLP 2020.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

32. `grattafiori2024llama`: Grattafiori et al. (2024). "The Llama 3 Herd of Models". arXiv 2407.21783.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

33. `yang2025qwen3`: Yang et al. (2025). "Qwen3 Technical Report". arXiv 2505.09388.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

34. `team2024gemma`: Gemma Team et al. (2024). "Gemma 2: Improving Open Language Models at a Practical Size". arXiv 2408.00118.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

35. `meng2022locating`: Meng et al. (2022). "Locating and Editing Factual Associations in GPT". NeurIPS 2022.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

36. `pokharel2026crosslingual`: Pokharel, Agrawal, Nagar (2026). "Cross-Lingual Activation Steering for Multilingual Language Models". arXiv 2601.16390.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

37. `sundar2025steering`: Sundar et al. (2025). "Steering into New Embedding Spaces". ACL 2025.
    - 真实性: ✓
    - 作者: ✗ **2 位作者完全错误**：bib 写 "Zhao, Skyler" 实际为 **Seto, Skyler**；bib 写 "Jurafsky, Dan" 实际为 **Fedzechkina, Masha**（ACL Anthology 确认）
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **ERROR**

38. `geiger2024finding`: Geiger et al. (2024). "Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations". CLeaR 2024, PMLR vol 236.
    - 真实性: ✓
    - 作者: ✓
    - 年份: ✓
    - 标题: ✓
    - Venue: ✓
    - cite 上下文: ✓
    - 综合: **OK**

---

### 问题汇总

| # | Key | 严重性 | 问题描述 |
|---|-----|--------|----------|
| 1 | `feng2026finegrained` | **ERROR** | 7/7 作者名全部错误（首名拼音接近但均有误），且缺少 3 位共同作者 |
| 2 | `xing2024evaluating` | **ERROR** | 4/6 作者名错误（Xiaoling→Xiaolin, Zhenhui→Zhiwei, Huiyun→Haoyu, Xin→Xing） |
| 3 | `sundar2025steering` | **ERROR** | 2 位作者完全错误（Zhao→Seto, Jurafsky→Fedzechkina） |
| 4 | `ifergan2024beneath` | **ERROR** | 第一作者 Matan→Maxim；year=2024 应为 2025（NAACL 2025） |
| 5 | `marks2024geometry` | **ERROR** | year=2024 应为 2025（ICLR 2025，OpenReview 确认） |
| 6 | `li2025taming` | **ERROR** | 第二作者 Yufei→Yuzhong Chen |
| 7 | `pham2026where` | **ERROR** | 第二作者 Hrishav→Hsuvas Borkakoty |
| 8 | `wang2025lost` | **WARNING** | 缺少 2 位作者（Yihong Liu, Ercong Nie），7 人只列了 5 人 |
| 9 | `kargaran2024mexa` | **WARNING** | year=2024 但 venue 是 Findings ACL 2025，应为 2025 |
| 10 | `ravichander2021probing` | **WARNING** | 页码 3331–3350 应为 3363–3377 |

**幻觉引用**: 0 条。全部 38 篇论文均真实存在。

**cite 上下文错误**: 0 条。所有引用的 claim 与原文内容一致。

**OpenAlex 预检对比**: OpenAlex 标记的 7 条中，4 条 not_found 均为索引缺失（Anthropic 技术报告、arXiv 预印本），3 条 mismatch 中 wu2020emerging 和 meng2022locating 经独立验证为 OpenAlex 误报，xie2024adaptive 也确认无误。真正的问题主要在 OpenAlex 未标记的条目中（feng2026finegrained、sundar2025steering、xing2024evaluating 等）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_ref_verify_B_20260526T105303"
}
```

</details>

---
