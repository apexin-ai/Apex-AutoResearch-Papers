# paper citation expansion

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_paper_citation-expansion_20260519T111739.jsonl`
- **Structured JSON:** [`129eb6553a151f1ecaef.json`](../../sessions/12/129eb6553a151f1ecaef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-19T11:22:33.776301+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T11:22:33.776808+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T11:22:33.777069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T11:22:33.777341+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}.
6	\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.
7	\citet{amin2025escaping} show that weak-data curation can mitigate collapse, connecting to our filtering evaluation (Section~\ref{sec:filtering}).
8	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}; $\Kempirical = 2$ is therefore a conservative lower bound.
9	This literature establishes convergence but provides no per-text depth measurement, does not predict domain dependence of saturation (Wikipedia depth 1 vs.\ arXiv depth 3), and does not characterize the prompt-chain vs.\ retrain-chain gap ($\Kempirical{=}2$ vs.\ $7$).
10	
11	\paragraph{Beyond binary detection.}
12	Binary detectors~\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate; surveys~\cite{wu2023survey, tang2024science} consolidate this landscape but frame detection as binary.
13	DivEye~\cite{basani2026diveye} shares 4 of our 15 features but applies them to binary detection; our extended set captures cross-generational degradation.
14	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under 
…[truncated 1439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T11:22:33.777579+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T11:22:33.777964+00:00_

1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — verified 2026-05-15
3	
4	% === Must-Cite ===
5	
6	@inproceedings{drayson2025,
7	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
8	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
9	  booktitle={Proceedings of EMNLP},
10	  year={2025},
11	  url={https://arxiv.org/abs/2502.15654}
12	}
13	
14	@inproceedings{schaeffer2025position,
15	  title={Position: Model Collapse Does Not Mean What You Think},
16	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
17	  booktitle={Proceedings of ICML},
18	  year={2025},
19	  url={https://arxiv.org/abs/2503.03150}
20	}
21	
22	@inproceedings{kazdan2025collapse,
23	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
24	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
25	  booktitle={Proceedings of ICML},
26	  year={2025},
27	  url={https://arxiv.org/abs/2410.16713}
28	}
29	
30	@inproceedings{mitchell2023detectgpt,
31	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
32	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
33	  booktitle={Proceedings of ICML},
34	  year={2023}
35	}
36	
37	% === Should-Cite ===
38	
39	@article{basani2026diveye,
40	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
41	  author={Basani, Advik Raj and Chen, Pin-Yu},
42	  journal={Transactions on Machine Learning Research},
43	  issn={2835-8856},
44	  year={2026},
45	  url={https://arxiv.org/abs/2509.18880}
46	}
47	
48	@inproceedings{zawalski2026codec,
49	  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},
50	  author={Zawalski, Micha{\l} and Boubdir, Meriem and Ba{\l}azy, Klaudia and Nushi, Besmira an
…[truncated 14019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T11:22:33.778343+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T11:22:33.778562+00:00_

docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/appendix_extended.tex
docs/paper/introduction.tex
docs/paper/experiments_c1.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/experiments_c3.tex
docs/paper/conclusion.tex
docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T11:22:33.778791+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[tp]?\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[tp]?\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T11:22:33.779054+00:00_

docs/paper/related_work.tex:5:Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}.
docs/paper/related_work.tex:6:\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.
docs/paper/related_work.tex:7:\citet{amin2025escaping} show that weak-data curation can mitigate collapse, connecting to our filtering evaluation (Section~\ref{sec:filtering}).
docs/paper/related_work.tex:8:Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}; $\Kempirical = 2$ is therefore a conservative lower bound.
docs/paper/related_work.tex:12:Binary detectors~\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate; surveys~\cite{wu2023survey, tang2024science} consolidate this landscape but frame detection as binary.
docs/paper/related_work.tex:13:DivEye~\cite{basani2026diveye} shares 4 of our 15 features but applies them to binary detection; our extended set captures cross-generational degradation.
docs/paper/related_work.tex:14:Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
docs/paper/related_work.tex:15:Iterat
…[truncated 4456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T11:22:33.779411+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T11:22:33.779723+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: the original signal degrades monotonically.
17	Together with Markov chain convergence, this motivates a finite $\Ktheory$ beyond which adjacent generations become indistinguishable; DPI guarantees existence but does not bound $\Ktheory$, so the actual saturation depth must be measured empirically.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k}) > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k})$ is the lower bound of a 95\% bootstrap confidence interval (1{,}000 resamples\footnote{Boundary-pair results in Table~\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\theta = 0.60$ is a post-hoc operational threshold (motivated below).
25	This criterion ensures that $\Kempirical$ reflects statistically robust discriminability rather than sampling noise.
26	$\Kempirical$ characterizes a discriminability regime at a given $\theta$; t
…[truncated 5683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T11:22:33.779991+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T11:22:33.780242+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically and ignores the generational depth dimension.
9	
10	This gap cuts across multiple communities.
11	Binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}).
12	Membership inference~\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.
13	Data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.
14	No existing method estimates how many rounds of recursive generation a text has undergone.
15	
16	Knowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.
17	For data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principle
…[truncated 2289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T11:22:33.780488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T11:22:33.780737+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\begin{figure}[t]
11	\centering
12	\includegraphics[width=\columnwidth]{figures/fig_jsd_decay.pdf}
13	\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\Kempirical{=}2$; dashed purple: Mistral-7B ($\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\Kempirical{=}3$); dotted red: retrain-chain ($\Kempirical{=}7$). C4 models exhibit a sharp cliff ($\lambda \approx 2.2$--$3.5$), while arXiv decays gradually ($\lambda \approx 1.0$) and retrain-chain shows no cliff ($\lambda = 0.285$).}
14	\label{fig:jsd_decay}
15	\end{figure}
16	
17	\paragraph{One-wash laundering (web text).}
18	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$, so a single generation pass renders text indistinguishable from deeper content.
19	Neither frontier LLMs nor alternative classifiers improve depth recovery beyond this boundary (McNemar $p > 0.05$; Appendix).
20	
21	\paragraph{JSD decay and the discrimination boundary.}
22	Token-level JSD between adjacent generations reveals two decay regimes (Figure~\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\times$) followed by rapid convergence, while arXiv decays ${\sim}$3$\times$ slower ($\lambda \approx 1.0$ vs.\ $2.9$).
23	The retrain-chain ($\lambda = 0.285$, no cliff) reflects cumulative model-adaptation artifacts, extending $\Kempirical$ to 7 (Appendix~\ref{sec:jsd_extended}).
24	
25	\paragraph{Graduated filtering failure.}
26	For web text, 2v3 $\auc < \theta$ across all configurations, so depth assignments beyond $d{=}2$ approximate random labels; the strategy orde
…[truncated 1952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T11:22:33.781080+00:00_

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
  "session": "worker_paper_citation-expansion_20260519T111739",
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

_source line 18 · 2026-05-19T11:22:33.781409+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T11:22:33.781654+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DNA-GPT Yang et al 2024 divergent n-gram analysis machine-generated text detection venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DNA-GPT Yang et al 2024 divergent n-gram analysis machine-generated text detection venue"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T11:22:33.781879+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ghostbuster Verma et al 2024 feature-based machine-generated text detection venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ghostbuster Verma et al 2024 feature-based machine-generated text detection venue"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T11:22:33.782079+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Raffel et al 2020 \"Exploring the Limits of Transfer Learning\" T5 C4 JMLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Raffel et al 2020 \"Exploring the Limits of Transfer Learning\" T5 C4 JMLR"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T11:22:33.782263+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hale 2001 \"probabilistic earley parser\" surprisal NAACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hale 2001 \"probabilistic earley parser\" surprisal NAACL"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T11:22:33.782442+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Levy 2008 \"expectation-based syntactic comprehension\" Cognition surprisal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Levy 2008 \"expectation-based syntactic comprehension\" Cognition surprisal"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T11:22:33.782649+00:00_

Web search results for query: "Ghostbuster Verma et al 2024 feature-based machine-generated text detection venue"

Links: [{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/382631441_Ghostbuster_Detecting_Text_Ghostwritten_by_Large_Language_Models"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/ghostbuster-detecting-text-ghostwritten-by-large-language"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.95/"},{"title":"Detecting Text Ghostwritten by Large Language Models","url":"https://aclanthology.org/2024.naacl-long.95.pdf"},{"title":"[2305.15047] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/pdf/2305.15047"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma","url":"https://nlp.cs.berkeley.edu/pubs/Verma-Fleisig-Tomlin-Klein_2024_Ghostbuster_paper.pdf"},{"title":"Spotlights and Blindspots: Evaluating Machine-Generated Text Detection","url":"https://arxiv.org/html/2604.16607v1"}]

Based on the search results, the Ghostbuster paper by Verma et al. was published at the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2024), which took place in Mexico City, Mexico.

The venue is **NAACL 2024** (North American Chapter of the Association for Computational Linguistics: Human Language Technologies).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T11:22:33.782931+00:00_

Web search results for query: "DNA-GPT Yang et al 2024 divergent n-gram analysis machine-generated text detection venue"

Links: [{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.nec-labs.com/blog/dna-gpt-divergent-n-gram-analysis-for-training-free-detection-of-gpt-generated-text/"},{"title":"[PDF] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DNA-GPT:-Divergent-N-Gram-Analysis-for-Detection-of-Yang-Cheng/08145978da4c8912f4a05444a6bbf048778dc4af"},{"title":"[2305.17359] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://arxiv.org/abs/2305.17359"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | OpenReview","url":"https://openreview.net/forum?id=Xlayxj2fWp"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://paperreading.club/page?id=167623"},{"title":"dblp: DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text.","url":"https://dblp1.uni-trier.de/rec/conf/iclr/Yang0WPWC24.html"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | DeepAI","url":"https://deepai.org/publication/dna-gpt-divergent-n-gram-analysis-for-training-free-detection-of-gpt-generated-text"},{"title":"(PDF) DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.researchgate.net/publication/371136931_DNA-GPT_Divergent_N-Gram_Analysis_for_Training-Free_Detection_of_GPT-Generated_Text"}]

Based on the search results, here's information about the DNA-GPT paper by Yang et al. 2024:

## Venue

The paper was published at ICLR 2024 (International Conference on Learning Representations 2024).

## Key Information

DNA-GPT proposes a novel training-free detection s
…[truncated 1068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T11:22:33.783208+00:00_

Web search results for query: "Hale 2001 "probabilistic earley parser" surprisal NAACL"

Links: [{"title":"A probabilistic earley parser as a psycholinguistic model | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2d3d3f7530f21cceff57fe3b937691956/tmalsburg"},{"title":"Expectation-based syntactic comprehension Roger Levy","url":"https://www.mit.edu/~rplevy/papers/levy-2008-cognition.pdf"},{"title":"A Probabilistic Earley Parser as a Psycholinguistic Model - ACL Anthology","url":"https://aclanthology.org/N01-1021/"},{"title":"A Probabilistic Earley Parser as a Psycholinguistic Model | Request PDF","url":"https://www.researchgate.net/publication/2486217_A_Probabilistic_Earley_Parser_as_a_Psycholinguistic_Model"},{"title":"Expectation-based syntactic comprehension","url":"https://escholarship.org/uc/item/66v7520b"},{"title":"Expectation-based syntactic comprehension - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0010027707001436"},{"title":"A probabilistic earley parser as a psycholinguistic model | Proceedings of the second meeting of the North American Chapter of the Association for Computational Linguistics on Language technologies","url":"https://dl.acm.org/doi/10.3115/1073336.1073357"},{"title":"A Probabilistic Earley Parser as a Psycholinguistic Model John Hale","url":"https://aclanthology.org/N01-1021.pdf"}]

I found the paper you're looking for! Here's information about Hale's 2001 NAACL paper:

"A Probabilistic Earley Parser as a Psycholinguistic Model" was published by John Hale in 2001 at the Second Meeting of the North American Chapter of the Association for Computational Linguistics.

The paper considers a definition of cognitive load in terms of the total probability of structural options that have been disconfirmed at some point in a sentence: the surprisal of word w_i given its prefix w_0...i-1 on a phrase-structural language model. These loads can be efficiently calculated using a probabilistic Earley parser (Stolcke
…[truncated 551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T11:22:33.783565+00:00_

Web search results for query: "Levy 2008 "expectation-based syntactic comprehension" Cognition surprisal"

Links: [{"title":"[PDF] Expectation-based syntactic comprehension | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Expectation-based-syntactic-comprehension-Levy/2a92864d3f44e1b34da0fa17e13d5752d089eddf"},{"title":"Expectation-based syntactic comprehension - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/17662975/"},{"title":"Expectation-based syntactic comprehension Roger Levy","url":"https://www.mit.edu/~rplevy/papers/levy-2008-cognition.pdf"},{"title":"Expectation-Based syntactic comprehension | Request PDF","url":"https://www.researchgate.net/publication/6176117_Expectation-Based_syntactic_comprehension"},{"title":"Memory and surprisal in human sentence comprehension Roger Levy","url":"https://www.mit.edu/~rplevy/papers/levy-2013-memory-and-surprisal-corrected.pdf"},{"title":"Memory and surprisal in human sentence comprehension Roger Levy","url":"https://pages.ucsd.edu/~bkbergen/cogs200/sentence-processing-book-chapter.pdf"},{"title":"Full article: Expectation-based Comprehension: Modeling the Interaction of World Knowledge and Linguistic Experience","url":"https://www.tandfonline.com/doi/full/10.1080/0163853X.2018.1448677"},{"title":"Expectation-based syntactic comprehension - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0010027707001436"}]

Based on the search results, I found the paper you're looking for:

The 2008 paper "Expectation-based syntactic comprehension" by R. Levy was published in Cognition, volume 106, pages 1126-1177. 

The paper investigates the role of resource allocation as a source of processing difficulty in human sentence comprehension, proposing a simple information-theoretic characterization of processing difficulty as the work incurred by resource reallocation during parallel, incremental, probabilistic disambiguation.

The proposal characterizes processing difficulty based on surprisa
…[truncated 371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T11:22:33.783873+00:00_

Web search results for query: "Raffel et al 2020 "Exploring the Limits of Transfer Learning" T5 C4 JMLR"

Links: [{"title":"Paper Summary: Exploring the Limits of Transfer Learning with a Unified Text-to-text Transformer","url":"https://queirozf.com/entries/paper-summary-exploring-the-limits-of-transfer-learning-with-a-unified-text-to-text-transformer"},{"title":"T5: Exploring Transfer Learning Limits","url":"https://hunterheidenreich.com/notes/natural-language-processing/language-models/t5-text-to-text-transfer-transformer/"},{"title":"Digest – Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer","url":"https://yuyangyy.com/researchlog/nlp/2021/01/25/t5.html"},{"title":"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer | Request PDF","url":"https://www.researchgate.net/publication/336767865_Exploring_the_Limits_of_Transfer_Learning_with_a_Unified_Text-to-Text_Transformer"},{"title":"Journal of Machine Learning Research 21 (2020) 1-67","url":"https://arxiv.org/pdf/1910.10683"},{"title":"Exploring the Limits of Transfer Learning with a Unified ...","url":"https://www.cs.princeton.edu/courses/archive/fall22/cos597G/lectures/lec03.pdf"},{"title":"[1910.10683] Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer","url":"https://arxiv.org/abs/1910.10683"},{"title":"[PDF] Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Exploring-the-Limits-of-Transfer-Learning-with-a-Raffel-Shazeer/6c4b76232bb72897685d19b3d264c6ee3005bc2b"}]

I found the paper you're looking for! Here are the key details:

**Paper Information:**

"Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" by Raffel, Colin and colleagues, published in the Journal of Machine Learning Research, volume 21, number 140, pages 1-67, in 2020.

**Overview:**

The paper introduces a unified framework that
…[truncated 943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T11:22:33.784242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
  "offset": "365"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
    "offset": "365"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T11:22:33.784460+00:00_

365	  title     = {{CodeSearchNet} Challenge: Evaluating the State of Semantic Code Search},
366	  author    = {Husain, Hamel and Wu, Ho-Hsiang and Gazit, Tiferet and Allamanis, Miltiadis and Brockschmidt, Marc},
367	  journal   = {arXiv preprint arXiv:1909.09436},
368	  year      = {2019},
369	  url       = {https://arxiv.org/abs/1909.09436}
370	}
371	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T11:22:33.784676+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
  "old_string": "  url       = {https://arxiv.org/abs/1909.09436}\n}",
  "new_string": "  url       = {https://arxiv.org/abs/1909.09436}\n}\n\n% === New entries (added 2026-05-19, citation density expansion) ===\n\n@article{raffel2020t5,\n  title={Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},\n  author={Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and Liu, Peter J.},\n  journal={Journal of Machine Learning Research},\n  volume={21},\n  number={140},\n  pages={1--67},\n  year={2020}\n}\n\n@inproceedings{yang2024dnagpt,\n  title={{DNA-GPT}: Divergent {N}-Gram Analysis for Training-Free Detection of {GPT}-Generated Text},\n  author={Yang, Xianjun and Cheng, Wei and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2305.17359}\n}\n\n@inproceedings{verma2024ghostbuster,\n  title={Ghostbuster: Detecting Text Ghostwritten by Large Language Models},\n  author={Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  booktitle={Proceedings of NAACL},\n  pages={1702--1717},\n  year={2024}\n}\n\n@inproceedings{hale2001surprisal,\n  title={A Probabilistic {E}arley Parser as a Psycholinguistic Model},\n  author={Hale, John},\n  booktitle={Proceedings of the Second Meeting of the North American Chapter of the Association for Computational Linguistics},\n  pages={1--8},\n  year={2001}\n}\n\n@article{levy2008expectation,\n  title={Expectation-Based Syntactic Comprehension},\n  author={Levy, Roger},\n  journal={Cognition},\n  volume={106},\n  number={3},\n  pages={1126--1177},\n  year={2008}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
    "old_string": "  url       = {https://arxiv.org/abs/1909.09436}\n}",
    "new_string": "  url       = {https://arxiv.org/abs/1909.09436}\n}\n\n% === New entries (added 2026-05-19, citation density expansion) ===\n\n@article{raffel2020t5,\n  title={Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},\n  author={Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and Liu, Peter J.},\n  journal={Journal of Machine Learning Research},\n  volume={21},\n  number={140},\n  pages={1--67},\n  year={2020}\n}\n\n@inproceedings{yang2024dnagpt,\n  title={{DNA-GPT}: Divergent {N}-Gram Analysis for Training-Free Detection of {GPT}-Generated Text},\n  author={Yang, Xianjun and Cheng, Wei and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2305.17359}\n}\n\n@inproceedings{verma2024ghostbuster,\n  title={Ghostbuster: Detecting Text Ghostwritten by Large Language Models},\n  author={Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  booktitle={Proceedings of NAACL},\n  pages={1702--1717},\n  year={2024}\n}\n\n@inproceedings{hale2001surprisal,\n  title={A Probabilistic {E}arley Parser as a Psycholinguistic Model},\n  author={Hale, John},\n  booktitle={Proceedings of the Second Meeting of the North American Chapter of the Association for Computational Linguistics},\n  pages={1--8},\n  year={2001}\n}\n\n@article{levy2008expectation,\n  title={Expectation-Based Syntactic Comprehension},\n  author={Levy, Roger},\n  journal={Cognition},\n  volume={106},\n  number={3},\n  pages={1126--1177},\n  year={2008}\n}"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T11:22:33.785027+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T11:22:33.785289+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
  "old_string": "and predictable convergence~\\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}.",
  "new_string": "and predictable convergence~\\cite{bertrand2024stability, schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
    "old_string": "and predictable convergence~\\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}.",
    "new_string": "and predictable convergence~\\cite{bertrand2024stability, schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}."
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T11:22:33.785529+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T11:22:33.785737+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
  "old_string": "Binary detectors~\\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate; surveys~\\cite{wu2023survey, tang2024science} consolidate this landscape but frame detection as binary.\nDivEye~\\cite{basani2026diveye} shares 4 of our 15 features but applies them to binary detection; our extended set captures cross-generational degradation.",
  "new_string": "Binary detectors~\\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, yang2024dnagpt, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate; surveys~\\cite{wu2023survey, tang2024science} consolidate this landscape but frame detection as binary.\nGhostbuster~\\cite{verma2024ghostbuster} and DivEye~\\cite{basani2026diveye} use statistical features for binary detection; our 15-dimensional set extends beyond binary separation to capture cross-generational degradation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
    "old_string": "Binary detectors~\\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate; surveys~\\cite{wu2023survey, tang2024science} consolidate this landscape but frame detection as binary.\nDivEye~\\cite{basani2026diveye} shares 4 of our 15 features but applies them to binary detection; our extended set captures cross-generational degradation.",
    "new_string": "Binary detectors~\\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, yang2024dnagpt, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate; surveys~\\cite{wu2023survey, tang2024science} consolidate this landscape but frame detection as binary.\nGhostbuster~\\cite{verma2024ghostbuster} and DivEye~\\cite{basani2026diveye} use statistical features for binary detection; our 15-dimensional set extends beyond binary separation to capture cross-generational degradation."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T11:22:33.786012+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T11:22:33.786222+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
  "old_string": "DSIR~\\cite{xie2023dsir}, D4~\\cite{tirumala2023d4}, DoReMi~\\cite{xie2023doremi}, and FineWeb~\\cite{penedo2024fineweb} address corpus quality through domain-aware filtering and deduplication but are depth-agnostic;",
  "new_string": "DSIR~\\cite{xie2023dsir}, D4~\\cite{tirumala2023d4}, DoReMi~\\cite{xie2023doremi}, and FineWeb~\\cite{penedo2024fineweb} address corpus quality for large web corpora such as C4~\\cite{raffel2020t5} through domain-aware filtering and deduplication but are depth-agnostic;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
    "old_string": "DSIR~\\cite{xie2023dsir}, D4~\\cite{tirumala2023d4}, DoReMi~\\cite{xie2023doremi}, and FineWeb~\\cite{penedo2024fineweb} address corpus quality through domain-aware filtering and deduplication but are depth-agnostic;",
    "new_string": "DSIR~\\cite{xie2023dsir}, D4~\\cite{tirumala2023d4}, DoReMi~\\cite{xie2023doremi}, and FineWeb~\\cite{penedo2024fineweb} address corpus quality for large web corpora such as C4~\\cite{raffel2020t5} through domain-aware filtering and deduplication but are depth-agnostic;"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T11:22:33.786459+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T11:22:33.786667+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
  "old_string": "\\paragraph{Ordinal classification and probing.}\nOur OBD classifier follows Frank \\& Hall's~\\cite{frank2001ordinal} binary decomposition; CORAL~\\cite{cao2020coral} provides a rank-consistent neural alternative.\nOur neural probe extends probing~\\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.",
  "new_string": "\\paragraph{Ordinal classification and probing.}\nOur surprisal-based features build on the information-theoretic view that word-level processing cost is proportional to surprisal~\\cite{hale2001surprisal, levy2008expectation}; we repurpose this measure to track generational degradation rather than human processing load.\nOur OBD classifier follows Frank \\& Hall's~\\cite{frank2001ordinal} binary decomposition; CORAL~\\cite{cao2020coral} provides a rank-consistent neural alternative.\nOur neural probe extends probing~\\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
    "old_string": "\\paragraph{Ordinal classification and probing.}\nOur OBD classifier follows Frank \\& Hall's~\\cite{frank2001ordinal} binary decomposition; CORAL~\\cite{cao2020coral} provides a rank-consistent neural alternative.\nOur neural probe extends probing~\\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.",
    "new_string": "\\paragraph{Ordinal classification and probing.}\nOur surprisal-based features build on the information-theoretic view that word-level processing cost is proportional to surprisal~\\cite{hale2001surprisal, levy2008expectation}; we repurpose this measure to track generational degradation rather than human processing load.\nOur OBD classifier follows Frank \\& Hall's~\\cite{frank2001ordinal} binary decomposition; CORAL~\\cite{cao2020coral} provides a rank-consistent neural alternative.\nOur neural probe extends probing~\\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary."
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T11:22:33.786943+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T11:22:33.787174+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
  "old_string": "Each uses 5{,}000 C4 seeds truncated to 256 tokens",
  "new_string": "Each uses 5{,}000 C4~\\cite{raffel2020t5} seeds truncated to 256 tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
    "old_string": "Each uses 5{,}000 C4 seeds truncated to 256 tokens",
    "new_string": "Each uses 5{,}000 C4~\\cite{raffel2020t5} seeds truncated to 256 tokens"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T11:22:33.787439+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T11:22:33.787673+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T11:22:33.787939+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{bertrand2024stability, schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}.
6	\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.
7	\citet{amin2025escaping} show that weak-data curation can mitigate collapse, connecting to our filtering evaluation (Section~\ref{sec:filtering}).
8	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}; $\Kempirical = 2$ is therefore a conservative lower bound.
9	This literature establishes convergence but provides no per-text depth measurement, does not predict domain dependence of saturation (Wikipedia depth 1 vs.\ arXiv depth 3), and does not characterize the prompt-chain vs.\ retrain-chain gap ($\Kempirical{=}2$ vs.\ $7$).
10	
11	\paragraph{Beyond binary detection.}
12	Binary detectors~\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, yang2024dnagpt, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate; surveys~\cite{wu2023survey, tang2024science} consolidate this landscape but frame detection as binary.
13	Ghostbuster~\cite{verma2024ghostbuster} and DivEye~\cite{basani2026diveye} use statistical features for binary detection; our 15-dimensional set extends beyond binary separation to capture cross-generational degradation.
14	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite
…[truncated 1872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T11:22:33.788267+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper && grep -c '^@' references.bib",
  "description": "Count bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper && grep -c '^@' references.bib",
    "description": "Count bib entries"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T11:22:33.788465+00:00_

49

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T11:22:33.788656+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u | wc -l",
  "description": "Count unique citations in related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u | wc -l",
    "description": "Count unique citations in related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T11:22:33.788871+00:00_

48

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T11:22:33.789064+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u | wc -l",
  "description": "Count total unique citations across all tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u | wc -l",
    "description": "Count total unique citations across all tex files"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T11:22:33.789255+00:00_

55

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T11:22:33.789486+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "List all unique citation keys across tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "List all unique citation keys across tex files"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T11:22:33.789694+00:00_

alain2017understanding
alemohammad2024selfconsuming
amin2025escaping
bao2024fast
basani2026diveye
belinkov2022probing
bertrand2024stability
briesch2023selfconsuming
cao2020coral
cheng2025beyond
dohmatob2024model
dohmatob2025strong
drayson2025
frank2001ordinal
gambetta2024surplexity
gehrmann2019gltr
gerstgrasser2024model
guo2024curious
hale2001surprisal
hans2024binoculars
hao2025rewrite
husain2019codesearchnet
kazdan2025collapse
ke2017lightgbm
kirchenbauer2023watermark
krishna2023paraphrasing
levy2008expectation
mehta2025beyond
mitchell2023detectgpt
oren2024proving
padmakumar2024writing
penedo2024fineweb
raffel2020t5
sadasivan2023detect
schaeffer2025position
shi2025collapse
shumailov2024collapse
spennemann2025quantifying
sun2025aigt
tang2024science
tirumala2023d4
verma2024ghostbuster
wang2024semeval
wu2023survey
xie2023doremi
xie2023dsir
yang2024dnagpt
zawalski2026codec
zhang2024minkpp

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-expansion_20260519T111739",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-19T11:22:33.790025+00:00_

全部完成。汇总如下：

## 引用前/后对比

| | 修改前 | 修改后 |
|---|---|---|
| Bib 条目 | 44 | 49 |
| 全文唯一引用 | 44 | 49 |

## 新增 5 篇引用

| 引用键 | 作者 | 标题 | 会议/期刊 | 年份 |
|---|---|---|---|---|
| `raffel2020t5` | Raffel et al. | Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer | JMLR | 2020 |
| `yang2024dnagpt` | Yang et al. | DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | ICLR | 2024 |
| `verma2024ghostbuster` | Verma et al. | Ghostbuster: Detecting Text Ghostwritten by Large Language Models | NAACL | 2024 |
| `hale2001surprisal` | Hale | A Probabilistic Earley Parser as a Psycholinguistic Model | NAACL | 2001 |
| `levy2008expectation` | Levy | Expectation-Based Syntactic Comprehension | Cognition | 2008 |

## Related Work 修改摘要

1. **Model collapse 段** (line 5): 加入 `bertrand2024stability`（已在 bib 但未在 RW 正文引用）
2. **Beyond binary detection 段** (line 12-13): 加入 `yang2024dnagpt` 到检测器列表；用 Ghostbuster + DivEye 替代原 DivEye 单独描述，突出特征方法对比
3. **Data selection 段** (line 20): 加入 `raffel2020t5` 作为 C4 数据集引用
4. **Ordinal classification 段** (line 24): 新增 surprisal 理论基础句，引用 `hale2001surprisal` 和 `levy2008expectation`，说明论文 surprisal 特征的信息论根源

## 额外修改
- `method.tex` line 55: C4 首次出现处加入 `\cite{raffel2020t5}`

注：任务列表中的大部分论文（Shumailov, Alemohammad, Dohmatob, Gerstgrasser, DetectGPT, Fast-DetectGPT, Binoculars, GLTR, Kirchenbauer, DSIR, D4, DoReMi, CodeSearchNet 等）修改前已全部在 bib 和正文中。Bertrand 2024 在 bib 但仅被 appendix 引用，现已补入 Related Work。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_citation-expansion_20260519T111739"
}
```

</details>

---
