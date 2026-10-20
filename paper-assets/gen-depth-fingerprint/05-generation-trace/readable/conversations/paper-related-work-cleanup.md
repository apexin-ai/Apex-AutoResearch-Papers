# paper related work cleanup

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_related-work-cleanup_20260515T175029.jsonl`
- **Structured JSON:** [`5fb7adae3d3002640dd8.json`](../../sessions/5f/5fb7adae3d3002640dd8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-15T17:53:05.522027+00:00_

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
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T17:53:05.522449+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests on token-level distributions \cite{gltr,grover,release_strategies} to zero-shot approaches exploiting reference-model likelihoods \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers over linguistic features \cite{feat_aug_transformer,reliable_detection,ld_score}.
8	Recent work has pursued diverse detection signals: \citet{intrinsic_dimension} use intrinsic dimensionality estimates, \citet{diveye} propose surprisal diversity features directly comparable to our shape-based measures, and \citet{generator_barrier} characterize the distributional gap between human and model outputs.
9	\citet{wu_survey_2025} provide the most comprehensive recent survey; see also \citet{jawahar_survey} for an earlier overview.
10	A persistent limitation is that all these methods produce binary (real vs.\ synthetic) decisions.
11	Recent efforts extend detection to multi-class settings: \citet{beyond_binary} propose role recognition and involvement measurement to distinguish collaborative human-LLM generation scenarios, and the SemEval-2024 shared task \cite{semeval2024_task8} evaluates multi-generator attribution across domains and languages.
12	These approaches discriminate among different \emph{sources} (human vs.\ specific models) rather than recursive generation \emph{depth} within a single generator's chain.
13	Even when detection scores correlate with generation depth, they exhibit high cross-generator variance when repurposed as ordinal predictors (per-generator F1 ranging from 0.42 to 0.81; \S\ref{sec:results-baselines}), because each score captures a single distributional property that generalizes inconsistently.
14	\citet{paraphrase_evades} and \citet{detection_possibilities} further demonstrate that detection robustness degrad
…[truncated 5497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T17:53:05.522729+00:00_

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
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T17:53:05.523080+00:00_

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
13	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
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
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detec
…[truncated 16718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T17:53:05.523407+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{sec:results-baselines\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{sec:results-baselines\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T17:53:05.523643+00:00_

artifacts/_project/paper/_backup/results_b30771.tex:92:\label{sec:results-baselines}
artifacts/_project/paper/results.tex:110:\label{sec:results-baselines}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T17:53:05.523850+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.42|0\\.81|per-generator F1",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.42|0\\.81|per-generator F1",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T17:53:05.524044+00:00_

19:Notably, adding Qwen3-8B data \emph{improves} classification on the original five generators (+1.1\,pp to 0.811), indicating that cross-scale diversity benefits rather than dilutes the training signal.
39:Pythia-2.8B     & Pythia & 2.8B & 0.804 & [0.793, 0.813] \\
41:Qwen3-0.6B     & Qwen   & 0.6B & 0.824 & [0.813, 0.834] \\
42:Qwen3-1.7B     & Qwen   & 1.7B & 0.806 & [0.796, 0.817] \\
57:Concordance index---an ordinal-specific metric rewarding correct ranking---yields XGBoost 0.821, CORAL 0.810, Frank-Hall 0.825; again, all CIs overlap.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T17:53:05.524182+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "shape-based",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Grep",
  "tool_args": {
    "pattern": "shape-based",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T17:53:05.524302+00:00_

artifacts/_project/paper/related_work.tex:8:Recent work has pursued diverse detection signals: \citet{intrinsic_dimension} use intrinsic dimensionality estimates, \citet{diveye} propose surprisal diversity features directly comparable to our shape-based measures, and \citet{generator_barrier} characterize the distributional gap between human and model outputs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T17:53:05.524452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "offset": "100",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
    "offset": "100",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T17:53:05.524635+00:00_

100	\bottomrule
101	\end{tabular}
102	\caption{Feature ablation (6-gen LOGO). Full $>$ surface = reference confirms complementarity between surface diversity features and reference-model distributional features.}
103	\label{tab:ablation}
104	\end{table}
105	
106	Leave-one-feature-out analysis confirms that 6 of 7 features contribute positively, with entropy\_max showing the largest marginal impact despite modest split frequency (Appendix~\ref{app:lofo}).
107	
108	
109	\subsection{Comparison with Detection Baselines}
110	\label{sec:results-baselines}
111	
112	\begin{figure}[t]
113	\centering
114	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.png}
115	\caption{LOGO macro-F1 with 95\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Per-generator held-out F1 varies more for single detectors than for the ensemble.}
116	\label{fig:baseline-ci}
117	\end{figure}
118	
119	We repurpose four existing detection scores as ordinal depth predictors by training the same classifier on each score as a single feature, using identical LOGO evaluation.
120	Because gen-0 seed texts are shared across generators (\S\ref{sec:generation}), 3-class LOGO evaluation creates a train--test overlap for the gen-0 class.
121	We therefore report both 3-class and binary (gen-1 vs.\ gen-2+) results; the binary metric is the primary measure of depth discrimination (Table~\ref{tab:baselines}).
122	
123	\begin{table}[t]
124	\centering
125	\small
126	\begin{tabular}{lccc}
127	\toprule
128	\textbf{Method} & \textbf{3-class F1} & \textbf{Binary F1} & \textbf{Per-gen std} \\
129	\midrule
130	7-feature ensemble    & 0.789 & \textbf{0.723} & 0.051 \\
131	4-det.\ + surface     & \textbf{0.805} & 0.724 & 0.049 \\
132	4-detector ens.\      & 0.796 & 0.712 & 0.044 \\
133	Avg-LogProb           & 0.737 & 0.712 & 0.044 \\
134	LD-Score              & 0.655 & 0.701 & 0.045 \\
135	FastDetectGPT         & 0.688 & 0.616 & 0.056 \\
136	Binoculars            & 0.417 & 0.5
…[truncated 3366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T17:53:05.524802+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "shape-based|shape based",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Grep",
  "tool_args": {
    "pattern": "shape-based|shape based",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T17:53:05.524928+00:00_

artifacts/_project/paper/related_work.tex:8:Recent work has pursued diverse detection signals: \citet{intrinsic_dimension} use intrinsic dimensionality estimates, \citet{diveye} propose surprisal diversity features directly comparable to our shape-based measures, and \citet{generator_barrier} characterize the distributional gap between human and model outputs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T17:53:05.525094+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "per.gen|per-gen|per_gen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Grep",
  "tool_args": {
    "pattern": "per.gen|per-gen|per_gen",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T17:53:05.525215+00:00_

21:We note that this gap may narrow with scale-matched training data; our current dataset contains $\sim$1{,}000 samples per generator regardless of scale.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T17:53:05.525330+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "shape.based|shape-based",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Grep",
  "tool_args": {
    "pattern": "shape.based|shape-based",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T17:53:05.525447+00:00_

Found 1 file
artifacts/_project/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T17:53:05.525557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T17:53:05.525720+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T17:53:05.525899+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex",
  "old_string": "\\citet{diveye} propose surprisal diversity features directly comparable to our shape-based measures",
  "new_string": "\\citet{diveye} propose surprisal diversity features directly comparable to our distributional features"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex",
    "old_string": "\\citet{diveye} propose surprisal diversity features directly comparable to our shape-based measures",
    "new_string": "\\citet{diveye} propose surprisal diversity features directly comparable to our distributional features"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T17:53:05.526044+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T17:53:05.526160+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex",
  "old_string": "they exhibit high cross-generator variance when repurposed as ordinal predictors (per-generator F1 ranging from 0.42 to 0.81; \\S\\ref{sec:results-baselines}), because each score captures a single distributional property that generalizes inconsistently.",
  "new_string": "they exhibit high cross-generator variance when repurposed as ordinal predictors (binary F1 from 0.52 to 0.71 across individual baselines; Table~\\ref{tab:baselines}), because each score captures a single distributional property that generalizes inconsistently."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex",
    "old_string": "they exhibit high cross-generator variance when repurposed as ordinal predictors (per-generator F1 ranging from 0.42 to 0.81; \\S\\ref{sec:results-baselines}), because each score captures a single distributional property that generalizes inconsistently.",
    "new_string": "they exhibit high cross-generator variance when repurposed as ordinal predictors (binary F1 from 0.52 to 0.71 across individual baselines; Table~\\ref{tab:baselines}), because each score captures a single distributional property that generalizes inconsistently."
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T17:53:05.526306+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T17:53:05.526431+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T17:53:05.526594+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests on token-level distributions \cite{gltr,grover,release_strategies} to zero-shot approaches exploiting reference-model likelihoods \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers over linguistic features \cite{feat_aug_transformer,reliable_detection,ld_score}.
8	Recent work has pursued diverse detection signals: \citet{intrinsic_dimension} use intrinsic dimensionality estimates, \citet{diveye} propose surprisal diversity features directly comparable to our shape-based measures, and \citet{generator_barrier} characterize the distributional gap between human and model outputs.
9	\citet{wu_survey_2025} provide the most comprehensive recent survey; see also \citet{jawahar_survey} for an earlier overview.
10	A persistent limitation is that all these methods produce binary (real vs.\ synthetic) decisions.
11	Recent efforts extend detection to multi-class settings: \citet{beyond_binary} propose role recognition and involvement measurement to distinguish collaborative human-LLM generation scenarios, and the SemEval-2024 shared task \cite{semeval2024_task8} evaluates multi-generator attribution across domains and languages.
12	These approaches discriminate among different \emph{sources} (human vs.\ specific models) rather than recursive generation \emph{depth} within a single generator's chain.
13	Even when detection scores correlate with generation depth, they exhibit high cross-generator variance when repurposed as ordinal predictors (per-generator F1 ranging from 0.42 to 0.81; \S\ref{sec:results-baselines}), because each score captures a single distributional property that generalizes inconsistently.
14	\citet{paraphrase_evades} and \citet{detection_possibilities} further demonstrate that detection robustness degrad
…[truncated 5497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T17:53:05.526752+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex",
  "old_string": "\\citet{diveye} propose surprisal diversity features directly comparable to our shape-based measures",
  "new_string": "\\citet{diveye} propose surprisal diversity features directly comparable to our distributional features"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex",
    "old_string": "\\citet{diveye} propose surprisal diversity features directly comparable to our shape-based measures",
    "new_string": "\\citet{diveye} propose surprisal diversity features directly comparable to our distributional features"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T17:53:05.526899+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T17:53:05.527021+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex",
  "old_string": "they exhibit high cross-generator variance when repurposed as ordinal predictors (per-generator F1 ranging from 0.42 to 0.81; \\S\\ref{sec:results-baselines}), because each score captures a single distributional property that generalizes inconsistently.",
  "new_string": "they exhibit high cross-generator variance when repurposed as ordinal predictors (binary F1 from 0.52 to 0.71 across individual baselines; Table~\\ref{tab:baselines}), because each score captures a single distributional property that generalizes inconsistently."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex",
    "old_string": "they exhibit high cross-generator variance when repurposed as ordinal predictors (per-generator F1 ranging from 0.42 to 0.81; \\S\\ref{sec:results-baselines}), because each score captures a single distributional property that generalizes inconsistently.",
    "new_string": "they exhibit high cross-generator variance when repurposed as ordinal predictors (binary F1 from 0.52 to 0.71 across individual baselines; Table~\\ref{tab:baselines}), because each score captures a single distributional property that generalizes inconsistently."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T17:53:05.527163+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work-cleanup_20260515T175029",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-15T17:53:05.527313+00:00_

两处修复完成，已同步到 `docs/paper/`。

**问题清单：**

| # | 位置 | 问题 | 修复 |
|---|------|------|------|
| 1 | line 8 | "shape-based measures" — 孤立术语，全文其他地方均未使用 | → "distributional features"，与 method/results 用语一致 |
| 2 | line 13 | "per-generator F1 ranging from 0.42 to 0.81" — 与当前 Table 5 不符（binary F1 实际范围 0.524–0.712），且原引用 `\S\ref{}` 指向无表格的小节 | → "binary F1 from 0.52 to 0.71 across individual baselines; Table~\ref{tab:baselines}"，引用改为具体表格 |

**验证通过项：**
- 全部 29 个 `\cite{}`/`\citet{}` key 均存在于 references.bib
- `\S\ref{sec:results-baselines}` 指向 results.tex:110，label 存在
- 无 novelty overclaim（line 15 明确说 "not a new detection method"）
- framing 一致：6 generators / 3 families / base models / LOGO / diagnostic tool

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_related-work-cleanup_20260515T175029"
}
```

</details>

---
