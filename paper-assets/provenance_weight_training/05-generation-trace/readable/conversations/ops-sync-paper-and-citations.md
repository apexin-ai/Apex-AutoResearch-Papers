# ops sync paper and citations

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 111
- **Recorded user turns:** 0
- **Tool calls:** 55
- **Original source:** `logs/chats/worker_ops_sync_paper_and_citations_20260515T234454.jsonl`
- **Structured JSON:** [`808d3b55217ddf13aa9b.json`](../../sessions/80/808d3b55217ddf13aa9b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

111 recorded events

### Tool call

_source line 1 · 2026-05-15T23:57:27.468201+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/",
  "description": "List docs/paper/sections/ files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/",
    "description": "List docs/paper/sections/ files"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T23:57:27.468528+00:00_

total 44
drwxr-xr-x 2 ubuntu ubuntu  4096 May 15 23:42 .
drwxr-xr-x 3 ubuntu ubuntu  4096 May 15 23:42 ..
-rw-r--r-- 1 ubuntu ubuntu     0 May 15 20:19 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu     0 May 15 20:19 appendix.tex
-rw-r--r-- 1 ubuntu ubuntu  2434 May 15 22:20 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu     0 May 15 20:19 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  3179 May 15 23:42 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu  4831 May 15 22:16 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu     0 May 15 20:19 limitations.tex
-rw-r--r-- 1 ubuntu ubuntu 10939 May 15 21:29 method.tex
-rw-r--r-- 1 ubuntu ubuntu  5760 May 15 22:17 related_work.tex
-rw-r--r-- 1 ubuntu ubuntu     0 May 15 20:19 results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T23:57:27.468699+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/",
  "description": "List artifacts/_project/paper/ files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/",
    "description": "List artifacts/_project/paper/ files"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T23:57:27.468843+00:00_

total 176
drwxr-xr-x 2 ubuntu ubuntu  4096 May 15 23:41 .
drwxr-xr-x 6 ubuntu ubuntu  4096 May 14 16:14 ..
-rw-r--r-- 1 ubuntu ubuntu  3010 May 15 22:08 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu  3010 May 15 22:08 conclusion_386ecc.tex
-rw-r--r-- 1 ubuntu ubuntu  8537 May 14 16:13 experiment_setup_draft.md
-rw-r--r-- 1 ubuntu ubuntu  2692 May 15 23:39 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu  2621 May 15 21:35 experiments_1613c9.tex
-rw-r--r-- 1 ubuntu ubuntu  2692 May 15 23:39 experiments_86dfd1.tex
-rw-r--r-- 1 ubuntu ubuntu  5845 May 15 22:10 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  5845 May 15 22:10 introduction_a663ee.tex
-rw-r--r-- 1 ubuntu ubuntu  4821 May 15 23:38 introduction_c6a67f.tex
-rw-r--r-- 1 ubuntu ubuntu  5822 May 15 23:36 introduction_draft.md
-rw-r--r-- 1 ubuntu ubuntu  9257 May 15 21:23 method.tex
-rw-r--r-- 1 ubuntu ubuntu 11093 May 15 23:37 method_3f5a58.tex
-rw-r--r-- 1 ubuntu ubuntu  9257 May 15 21:23 method_76a694.tex
-rw-r--r-- 1 ubuntu ubuntu  7148 May 14 17:05 method_section_draft.md
-rw-r--r-- 1 ubuntu ubuntu  5442 May 15 20:26 related_work.tex
-rw-r--r-- 1 ubuntu ubuntu  5567 May 15 23:39 related_work_0b6096.tex
-rw-r--r-- 1 ubuntu ubuntu  5442 May 15 20:26 related_work_963aec.tex
-rw-r--r-- 1 ubuntu ubuntu  5700 May 15 23:35 related_work_draft.md
-rw-r--r-- 1 ubuntu ubuntu  5700 May 15 23:35 related_work_draft_0db5c4.md
-rw-r--r-- 1 ubuntu ubuntu  4462 May 15 23:39 results.tex
-rw-r--r-- 1 ubuntu ubuntu  4478 May 15 21:35 results_819b43.tex
-rw-r--r-- 1 ubuntu ubuntu   415 May 15 20:14 writing_plan_v1_info.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T23:57:27.469038+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T23:57:27.469200+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced Minimum Intervention Reweighting, a dual-constrained framework for contamination-aware pretraining that selects per-batch exponents $b^*$ without validation data.
5	The method finds the smallest $b$ satisfying $\alpha_{\mathrm{eff}}(b) \geq \tau$ subject to $\mathrm{ESS}(b) \geq n_{\min}$, enforcing a minimum-intervention principle: apply only as much downweighting as needed to meet a quality floor, no more.
6	This stands in direct contrast to ESS-only (maximum-intervention) strategies, which we show degrade performance below even uniform baselines by over-downweighting contaminated samples.
7	
8	Across three seeds at 0.6B scale with 40\% synthetic contamination, adaptive $b^*$ matches grid-search-optimal PPL (17.651 vs.\ 17.646) within seed variance, eliminating the $|\mathcal{B}|$-run grid search entirely.
9	The quality threshold $\tau$ is robust across $[0.5, 0.8]$---all values in this range outperform uniform weighting.
10	A lightweight TF-IDF + logistic regression detector (AUC\,0.94) suffices when post-hoc calibrated (ECE\,0.048); score calibration matters more than raw discriminative power.
11	The batch-level constraint regime---49.9\% clean (no reweighting needed), 20.2\% $\alpha_{\mathrm{eff}}$-binding, 30.0\% ESS-binding---confirms that both constraints are active and complementary in practice.
12	
13	\section*{Limitations}
14	\label{sec:limitations}
15	
16	\paragraph{Scale.}
17	All experiments use a single model size (Qwen3-0.6B) with batch size 4.
18	Batch-level $q$-score statistics concentrate differently at larger batch sizes typical of 3B+ training; the optimal $\tau$ range and constraint dynamics may shift at scale.
19	
20	\paragraph{Contamination distribution.}
21	We inject synthetic data via uniform random mixing at a controlled ratio ($\rho{=}0.4$).
22	Real web-scale contamination is domain-skewed, which may alter within-batch $\alpha_{\mathrm{eff}}$ distributions and require domai
…[truncated 1118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T23:57:27.469361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T23:57:27.469509+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\paragraph{Training Data.}
5	We sample a 132M-token subset of FineWeb~\citep{penedo_2024_fineweb} as the real-data source.
6	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang_2025_qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\rho = 0.4$ via uniform random mixing.
7	This self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.
8	
9	\paragraph{Detector.}
10	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\,=\,0.939 with calibrated ECE\,=\,0.048 after temperature scaling ($T = 0.204$).
11	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
12	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson_2025_detection_collapse}) to test whether score \emph{calibration} matters more than raw discrimination for reweighting.
13	
14	\paragraph{Training.}
15	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
16	All main comparisons use three random seeds (42, 123, 456).
17	
18	\paragraph{Evaluation.}
19	We report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).
20	All evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.
21	
22	\paragraph{Methods.}
23	We compare five approaches:
24	\begin{itemize}[nosep,leftmargin=*]
25	  \item \textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).
26	  \it
…[truncated 782 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T23:57:27.469655+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T23:57:27.469808+00:00_

1	Web corpora increasingly contain machine-generated text.
2	Recent estimates place the synthetic fraction at 20--60\% of crawled data~\citep{cheng_2025_contamination_survey}, and this share grows as language models are deployed for content production at scale.
3	Training on such contaminated data has concrete consequences: \citet{shumailov_2024_model_collapse} show that recursive training on model outputs leads to irreversible quality degradation---\emph{model collapse}---and \citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.
4	A central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.
5	The prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.
6	
7	A natural response is \emph{detect-and-reweight}: train a classifier to estimate each sample's synthetic probability $q(x)$, then suppress likely-synthetic samples via the weighting function $w(x) = (1 - q(x))^b$.
8	\citet{drayson_2025_detection_collapse} demonstrate this approach for model collapse prevention and show that the exponent $b$ critically determines outcomes---their optimal values range from $b{=}10$ for models at ${\leq}360$M parameters to $b{=}1$ at 1.7B, and misspecification degrades results substantially.
9	Selecting $b$ therefore requires per-model validation-set grid search, with computational cost scaling linearly in the number of candidates (six training runs in a typical sweep).
10	Other approaches assume even stronger supervision: \citet{he_2025_golden_ratio} derive theoretically optimal weights from convergence analysis but require the exact contamination ratio $\rho$, which is precisely what is unavailable in practice.
11	Hard detection-and-removal strategies
…[truncated 3953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T23:57:27.469970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T23:57:27.470160+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Setup}
5	\label{sec:setup}
6	
7	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
8	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown---a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng_2025_contamination_survey}.
9	
10	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
11	Following \citet{drayson_2025_detection_collapse}, we weight each sample as
12	\begin{equation}
13	  w(x) = (1 - q(x))^{b},
14	  \label{eq:weight}
15	\end{equation}
16	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
17	\citet{drayson_2025_detection_collapse} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
18	We instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.
19	
20	\subsection{Dual-Constraint Framework}
21	\label{sec:dual}
22	
23	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
24	
25	\paragraph{Effective real proportion.}
26	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
27	The \emph{effective real proportion}
28	\begin{equation}
29	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
30	  \label{eq:alpha}
31	\end{equation}
32	measures the share of total weight allocated to likely-real samples.
33	At $b = 0$, $\alpha_{\mathrm{eff}}$ equals the raw real fraction in the batch; in
…[truncated 7701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T23:57:27.470315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T23:57:27.470518+00:00_

1	\section{Related Work}
2	
3	\paragraph{Synthetic Contamination and Model Collapse.}
4	Training on recursively generated data leads to irreversible quality degradation---\emph{model collapse}~\citep{shumailov_2024_model_collapse}.
5	\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
6	More critically, \citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
7	\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
8	These results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
9	
10	\paragraph{Detection and Filtering of Machine-Generated Text.}
11	Given the severity of contamination, a natural response is to detect and remove synthetic content.
12	DetectGPT~\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\% Prob~\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\% tokens as a reference-free signal.
13	Both produce continuous confidence scores suitable as input to downstream weighting---including ours.
14	On the mitigation side, \citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.
15	\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.
16	Hard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.
17	
18	Most directly related to our work, \citet{drayson_2025_detection_collapse} propose $w_j = (
…[truncated 3553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T23:57:27.470694+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T23:57:27.470884+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Main Comparison}
5	
6	Table~\ref{tab:main} reports held-out perplexity across methods and seeds.
7	Adaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).
8	This parity comes at zero validation cost---grid search requires $|\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.
9	
10	The grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\ref{app:grid}), confirming that exponent selection is consequential.
11	The optimal $b{=}0.5$ differs from the $b{=}10$ reported by \citet{drayson_2025_detection_collapse} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.
12	
13	ESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \emph{worse} than uniform (17.694) by 0.029.
14	Removing $\alpha_{\mathrm{eff}}$ and maximizing $b$ subject only to $\mathrm{ESS} \geq n_{\min}$ leads to over-downweighting that degrades training, providing direct evidence for the minimum-intervention principle.
15	
16	The Golden Ratio oracle~\citep{he_2025_golden_ratio} achieves PPL 17.654 on seed 42 using known provenance labels.
17	Adaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.
18	
19	The adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.
20	The constraint regime breakdown in \S\ref{sec:algorithm} shows that $\alpha_{\mathrm{eff}}$ prevents over-intervention in the 40\% of reweighted batches where moderate $b$ already meets the quality target.
21	
22	\begin{table}[t]
23	\centering
24	\small
…[truncated 2687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T23:57:27.471072+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T23:57:27.471227+00:00_

1	Web pretraining corpora are increasingly contaminated by machine-generated text, with recent estimates placing the synthetic fraction between 20\% and 60\%.
2	This poses a fundamental threat to model quality: \citet{shumailov2024model} demonstrate that training on recursively generated data leads to irreversible model collapse, and \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger degradation, ruling out data scaling as a remedy.
3	As synthetic content becomes ubiquitous, \emph{contamination-aware training}---strategies that explicitly account for data provenance during optimization---is necessary for maintaining pretraining quality.
4	
5	A natural mitigation is detect-and-reweight: assign each sample a weight $w(x) = (1 - q(x))^b$ based on a detector's estimated synthetic probability $q(x)$, where larger $b$ downweights suspected synthetic text more aggressively \citep{drayson2025detection}.
6	However, the exponent $b$ is a sensitive per-model hyperparameter whose optimal value varies by an order of magnitude across scales: $b = 1$ for SmolLM-1.7B versus $b = 10$ for GPT-2 124M.
7	Selecting $b$ requires a clean validation set and grid search costing up to $6{\times}$ the base training budget.
8	The practical question is immediate: \emph{how should $b$ be chosen without validation data?}
9	
10	We propose a \emph{dual-constraint framework} that derives the exponent adaptively per batch from two diagnostics computed on the detector scores alone.
11	The effective real proportion $\aeff(b)$ measures the weighted fraction of gradient signal attributable to real data and imposes a \emph{quality floor}: $\aeff(b) \geq \tau$---at least enough cleaning.
12	Kish's effective sample size $\mathrm{ESS}(b)$ \citep{vehtari2024psis} quantifies weight concentration and imposes a \emph{stability ceiling}: $\mathrm{ESS}(b) \geq \nmin$---not so much cleaning that gradient signal degrades.
13	A key structura
…[truncated 2927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T23:57:27.471373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T23:57:27.471523+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation---\emph{model collapse}~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
5	Independent estimates suggest that synthetic content now constitutes 20--60\% of web corpora, making this threat increasingly urgent.
6	These results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
7	
8	\paragraph{Detection and Filtering of Machine-Generated Text.}
9	Given the severity of contamination, a natural response is to detect and remove synthetic content.
10	DetectGPT~\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\% Prob~\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\% tokens as a reference-free signal.
11	Both produce continuous confidence scores suitable as input to reweighting frameworks such as ours.
12	On the mitigation side, \citet{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.
13	\citet{guo2025escaping} similarly rely on verification-based selection.
14	Hard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.
15	
16	Most directly related to our work, \citet{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic probability.
17	We adopt the s
…[truncated 3880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T23:57:27.471660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T23:57:27.471799+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}---the same model we continue pretraining---and inject them at ratio $\rho = 0.4$ via uniform random mixing.
4	This self-contamination design---where the model's own outputs are mixed back into its training data---creates a particularly challenging detection scenario, as generator and trainee share identical pretrained weights.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\,=\,0.939 with calibrated ECE\,=\,0.048 after temperature scaling ($T = 0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	
11	\paragraph{Training.}
12	We continue pretraining Qwen3-0.6B for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
13	The pretrained checkpoint starts at PPL\,=\,22.97 on our held-out set; after continued pretraining, the best method (adaptive $\bstar$) reaches $17.651 {\pm} 0.007$ across three seeds ($\Delta$PPL\,=\,$-5.319$, $-23.2\%$).
14	All main comparisons use three random seeds (42, 123, 456).
15	We note that method-level differences (${\sim}0.04$ PPL between adaptive and uniform) are small in absolute terms but arise in a regime where the model is already well-optimized; the $5{+}$ PPL drop from pretraining absorbs the easy gains, making further improvement from data curation increasingly 
…[truncated 1266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T23:57:27.471996+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/",
  "description": "List docs/paper/ directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/",
    "description": "List docs/paper/ directory"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T23:57:27.472127+00:00_

total 372
drwxr-xr-x 3 ubuntu ubuntu   4096 May 15 23:42 .
drwxr-xr-x 4 ubuntu ubuntu   4096 May 15 05:23 ..
-rw-r--r-- 1 ubuntu ubuntu  11615 May 15 20:19 acl.sty
-rw-r--r-- 1 ubuntu ubuntu  45186 May 15 20:19 acl_natbib.bst
-rw-r--r-- 1 ubuntu ubuntu   4136 May 15 23:42 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu   4821 May 15 23:38 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  15429 May 15 22:17 main.aux
-rw-r--r-- 1 ubuntu ubuntu   6506 May 15 22:17 main.bbl
-rw-r--r-- 1 ubuntu ubuntu   1463 May 15 22:17 main.blg
-rw-r--r-- 1 ubuntu ubuntu  27225 May 15 22:17 main.log
-rw-r--r-- 1 ubuntu ubuntu   1276 May 15 22:17 main.out
-rw-r--r-- 1 ubuntu ubuntu 192299 May 15 22:17 main.pdf
-rw-r--r-- 1 ubuntu ubuntu   1554 May 15 21:49 main.tex
-rw-r--r-- 1 ubuntu ubuntu  13295 May 15 23:43 method.tex
-rw-r--r-- 1 ubuntu ubuntu   6034 May 15 21:48 references.bib
-rw-r--r-- 1 ubuntu ubuntu   5567 May 15 23:39 related_work.tex
drwxr-xr-x 2 ubuntu ubuntu   4096 May 15 23:42 sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T23:57:27.472249+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T23:57:27.472360+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T23:57:27.472488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T23:57:27.472621+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{amsthm}
12	\usepackage{algorithm}
13	\usepackage{algorithmic}
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{enumitem}
18	\usepackage{hyperref}
19	
20	\newtheorem{proposition}{Proposition}
21	\newtheorem{definition}{Definition}
22	
23	\newcommand{\bstar}{b^*}
24	\newcommand{\aeff}{\alpha_{\mathrm{eff}}}
25	\newcommand{\nmin}{n_{\min}}
26	\newcommand{\btau}{b_{\tau}}
27	\newcommand{\bess}{b_{\mathrm{ESS}}}
28	
29	\title{Minimum Intervention Reweighting: Adaptive Exponent Selection\\for Contamination-Aware Pretraining}
30	
31	\author{Anonymous}
32	
33	\begin{document}
34	\maketitle
35	
36	\begin{abstract}
37	\input{sections/abstract}
38	\end{abstract}
39	
40	\section{Introduction}
41	\label{sec:intro}
42	\input{sections/introduction}
43	
44	\section{Related Work}
45	\label{sec:related}
46	\input{sections/related_work}
47	
48	\section{Method}
49	\label{sec:method}
50	\input{sections/method}
51	
52	\section{Experimental Setup}
53	\label{sec:experiments}
54	\input{sections/experiments}
55	
56	\section{Results}
57	\label{sec:results}
58	\input{sections/results}
59	
60	\section{Discussion}
61	\label{sec:discussion}
62	\input{sections/discussion}
63	
64	\section{Conclusion}
65	\label{sec:conclusion}
66	\input{sections/conclusion}
67	
68	\section*{Limitations}
69	\label{sec:limitations}
70	\input{sections/limitations}
71	
72	\bibliography{references}
73	\bibliographystyle{acl_natbib}
74	
75	\appendix
76	\input{sections/appendix}
77	
78	\end{document}
79	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T23:57:27.472743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T23:57:27.472909+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@article{drayson2025detection,
5	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
6	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
7	  journal={arXiv preprint arXiv:2502.15654},
8	  year={2025}
9	}
10	
11	@article{he2025golden,
12	  title={Golden Ratio Weighting Prevents Model Collapse},
13	  author={He, Hengzhi and Xu, Shirong and Cheng, Guang},
14	  journal={arXiv preprint arXiv:2502.18049},
15	  year={2025}
16	}
17	
18	@article{wang2026survive,
19	  title={Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training},
20	  author={Wang, Kevin and Niu, Hongqian and Li, Didong},
21	  journal={arXiv preprint arXiv:2602.16065},
22	  year={2026}
23	}
24	
25	@article{shumailov2024model,
26	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
27	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
28	  journal={Nature},
29	  volume={631},
30	  pages={755--759},
31	  year={2024}
32	}
33	
34	@inproceedings{dohmatob2025strong,
35	  title={Strong Model Collapse},
36	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
37	  booktitle={ICLR},
38	  year={2025}
39	}
40	
41	@article{vehtari2024psis,
42	  title={Pareto Smoothed Importance Sampling},
43	  author={Vehtari, Aki and Simpson, Daniel and Gelman, Andrew and Yao, Yuling and Gabry, Jonah},
44	  journal={JMLR},
45	  year={2024}
46	}
47	
48	@inproceedings{sow2025dynamic,
49	  title={Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining},
50	  author={Sow, Daouda and Woisetschl{\"a}ger, Herbert and Bulusu, Saikiran and Wang, Shiqiang and Jacobsen, Hans-Arno and Liang, Yingbin},
51	  booktitle={ICLR},
52	  year={2025}
53	
…[truncated 4590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T23:57:27.473229+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex",
  "content": "Web corpora increasingly contain machine-generated text.\nRecent estimates place the synthetic fraction at 20--60\\% of crawled data~\\citep{cheng2025contamination}, and this share grows as language models are deployed for content production at scale.\nTraining on such contaminated data has concrete consequences: \\citet{shumailov2024model} show that recursive training on model outputs leads to irreversible quality degradation---\\emph{model collapse}---and \\citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.\nA central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.\nThe prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.\n\nA natural response is \\emph{detect-and-reweight}: train a classifier to estimate each sample's synthetic probability $q(x)$, then suppress likely-synthetic samples via the weighting function $w(x) = (1 - q(x))^b$.\n\\citet{drayson2025detection} demonstrate this approach for model collapse prevention and show that the exponent $b$ critically determines outcomes---their optimal values range from $b{=}10$ for models at ${\\leq}360$M parameters to $b{=}1$ at 1.7B, and misspecification degrades results substantially.\nSelecting $b$ therefore requires per-model validation-set grid search, with computational cost scaling linearly in the number of candidates (six training runs in a typical sweep).\nOther approaches assume even stronger supervision: \\citet{he2025golden} derive theoretically optimal weights from convergence analysis but require the exact contamination ratio $\\rho$, which is precisely what is unavailable in practice.\nHard detection-and-removal strategies~\\citep{feng2025beyond} discard borderline samples entirely, sacrificing the smooth reweighting that continuous $q$-scores enable.\n\nGiven per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?\nWe formulate this as a dual-constrained optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\\aeff(b)$ reaches a quality threshold $\\tau$, while keeping Kish's effective sample size $\\mathrm{ESS}(b)$ above a stability floor $\\nmin$.\nThe quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effective real-data fraction~\\citep{wang2026survive}, motivating a lower bound on $\\aeff$.\nThe stability constraint prevents extreme weight concentration that degrades gradient quality.\nThese two requirements exhibit a natural opposition.\n$\\aeff(b)$ increases monotonically in $b$ (Proposition~\\ref{prop:monotone}), yielding a lower bound $\\btau$---the minimum exponent needed to achieve the target quality.\n$\\mathrm{ESS}(b)$ decreases monotonically, yielding an upper bound $\\bess$---the maximum exponent before gradient stability degrades.\nThe adaptive exponent $\\bstar = \\btau$ when the feasible region $[\\btau, \\bess]$ is non-empty, embodying a \\emph{minimum intervention principle}: apply the least downweighting sufficient to meet the quality target, preserving as much effective training data as possible.\nWhen the constraints conflict ($\\btau > \\bess$), the stability ceiling takes precedence.\n\nThis minimum-intervention semantics distinguishes the method from the alternative of maximizing $b$ subject only to ESS stability.\nAmong batches that require reweighting, the dual-constraint solver selects $\\bstar$ via the $\\aeff$ bound in 40\\% of cases, with mean $\\bstar{=}1.67$; the ESS-only variant would choose $b{=}4.15$ in these same batches, 2.5$\\times$ more aggressive.\nThe remaining 49.9\\% of batches have sufficient real-data content to skip reweighting entirely ($\\bstar{=}0$).\nThe per-batch $\\bstar$ distribution (median 0.87, mean 1.40) adapts continuously to each batch's contamination composition without any held-out signal.\n\nOn Qwen3-0.6B continued pretraining with 40\\% synthetic contamination (132M+ tokens from FineWeb), adaptive reweighting achieves mean held-out perplexity of 17.651 across three seeds, matching the grid-searched optimum ($b{=}0.5$, mean 17.646) within seed-to-seed variance (\\S\\ref{sec:results}).\nThe grid sweep requires six complete training runs to identify this optimum; the adaptive method requires one.\nThe ESS-only variant (maximum intervention) yields mean PPL 17.722---worse than the uniform baseline (17.694)---confirming that maximum intervention degrades training while minimum intervention improves it.\nA lightweight TF-IDF + Logistic Regression detector (AUC\\,=\\,0.939, calibrated ECE\\,=\\,0.048) suffices throughout, suggesting that score calibration matters more than raw classification accuracy for provenance-based reweighting.\n\nOur contributions:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item A dual-constrained framework for adaptive exponent selection: $\\bstar = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\}$ subject to $\\mathrm{ESS}(b) \\geq \\nmin$, computed per-batch from detector scores with minimum-intervention semantics (\\S\\ref{sec:method}).\n\\item Empirical evidence that adaptive $\\bstar$ matches grid-searched best within seed variance at zero validation cost, and that minimum intervention (dual constraint) outperforms maximum intervention (ESS-only) across three seeds (\\S\\ref{sec:results}).\n\\item A demonstration that a lightweight TF-IDF + LR detector with calibrated $q$-scores supports effective reweighting, achieving results comparable to stronger neural detectors (\\S\\ref{sec:experiments}).\n\\end{itemize}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex",
    "content": "Web corpora increasingly contain machine-generated text.\nRecent estimates place the synthetic fraction at 20--60\\% of crawled data~\\citep{cheng2025contamination}, and this share grows as language models are deployed for content production at scale.\nTraining on such contaminated data has concrete consequences: \\citet{shumailov2024model} show that recursive training on model outputs leads to irreversible quality degradation---\\emph{model collapse}---and \\citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.\nA central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.\nThe prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.\n\nA natural response is \\emph{detect-and-reweight}: train a classifier to estimate each sample's synthetic probability $q(x)$, then suppress likely-synthetic samples via the weighting function $w(x) = (1 - q(x))^b$.\n\\citet{drayson2025detection} demonstrate this approach for model collapse prevention and show that the exponent $b$ critically determines outcomes---their optimal values range from $b{=}10$ for models at ${\\leq}360$M parameters to $b{=}1$ at 1.7B, and misspecification degrades results substantially.\nSelecting $b$ therefore requires per-model validation-set grid search, with computational cost scaling linearly in the number of candidates (six training runs in a typical sweep).\nOther approaches assume even stronger supervision: \\citet{he2025golden} derive theoretically optimal weights from convergence analysis but require the exact contamination ratio $\\rho$, which is precisely what is unavailable in practice.\nHard detection-and-removal strategies~\\citep{feng2025beyond} discard borderline samples entirely, sacrificing the smooth reweighting that continuous $q$-scores enable.\n\nGiven per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?\nWe formulate this as a dual-constrained optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\\aeff(b)$ reaches a quality threshold $\\tau$, while keeping Kish's effective sample size $\\mathrm{ESS}(b)$ above a stability floor $\\nmin$.\nThe quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effective real-data fraction~\\citep{wang2026survive}, motivating a lower bound on $\\aeff$.\nThe stability constraint prevents extreme weight concentration that degrades gradient quality.\nThese two requirements exhibit a natural opposition.\n$\\aeff(b)$ increases monotonically in $b$ (Proposition~\\ref{prop:monotone}), yielding a lower bound $\\btau$---the minimum exponent needed to achieve the target quality.\n$\\mathrm{ESS}(b)$ decreases monotonically, yielding an upper bound $\\bess$---the maximum exponent before gradient stability degrades.\nThe adaptive exponent $\\bstar = \\btau$ when the feasible region $[\\btau, \\bess]$ is non-empty, embodying a \\emph{minimum intervention principle}: apply the least downweighting sufficient to meet the quality target, preserving as much effective training data as possible.\nWhen the constraints conflict ($\\btau > \\bess$), the stability ceiling takes precedence.\n\nThis minimum-intervention semantics distinguishes the method from the alternative of maximizing $b$ subject only to ESS stability.\nAmong batches that require reweighting, the dual-constraint solver selects $\\bstar$ via the $\\aeff$ bound in 40\\% of cases, with mean $\\bstar{=}1.67$; the ESS-only variant would choose $b{=}4.15$ in these same batches, 2.5$\\times$ more aggressive.\nThe remaining 49.9\\% of batches have sufficient real-data content to skip reweighting entirely ($\\bstar{=}0$).\nThe per-batch $\\bstar$ distribution (median 0.87, mean 1.40) adapts continuously to each batch's contamination composition without any held-out signal.\n\nOn Qwen3-0.6B continued pretraining with 40\\% synthetic contamination (132M+ tokens from FineWeb), adaptive reweighting achieves mean held-out perplexity of 17.651 across three seeds, matching the grid-searched optimum ($b{=}0.5$, mean 17.646) within seed-to-seed variance (\\S\\ref{sec:results}).\nThe grid sweep requires six complete training runs to identify this optimum; the adaptive method requires one.\nThe ESS-only variant (maximum intervention) yields mean PPL 17.722---worse than the uniform baseline (17.694)---confirming that maximum intervention degrades training while minimum intervention improves it.\nA lightweight TF-IDF + Logistic Regression detector (AUC\\,=\\,0.939, calibrated ECE\\,=\\,0.048) suffices throughout, suggesting that score calibration matters more than raw classification accuracy for provenance-based reweighting.\n\nOur contributions:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item A dual-constrained framework for adaptive exponent selection: $\\bstar = \\inf\\{b \\geq 0 : \\aeff(b) \\geq \\tau\\}$ subject to $\\mathrm{ESS}(b) \\geq \\nmin$, computed per-batch from detector scores with minimum-intervention semantics (\\S\\ref{sec:method}).\n\\item Empirical evidence that adaptive $\\bstar$ matches grid-searched best within seed variance at zero validation cost, and that minimum intervention (dual constraint) outperforms maximum intervention (ESS-only) across three seeds (\\S\\ref{sec:results}).\n\\item A demonstration that a lightweight TF-IDF + LR detector with calibrated $q$-scores supports effective reweighting, achieving results comparable to stronger neural detectors (\\S\\ref{sec:experiments}).\n\\end{itemize}\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T23:57:27.473417+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T23:57:27.473572+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex",
  "content": "\n\\subsection{Problem Setup}\n\\label{sec:setup}\n\nLet $\\mathcal{D} = \\mathcal{D}_{\\mathrm{real}} \\cup \\mathcal{D}_{\\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.\nThe contamination ratio $\\rho = |\\mathcal{D}_{\\mathrm{synth}}| / |\\mathcal{D}|$ is unknown---a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\\citep{cheng2025contamination}.\n\nA pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \\in [0,1]$.\nFollowing \\citet{drayson2025detection}, we weight each sample as\n\\begin{equation}\n  w(x) = (1 - q(x))^{b},\n  \\label{eq:weight}\n\\end{equation}\nwhere $b \\geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.\n\\citet{drayson2025detection} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\\leq}360$M parameters, $b{=}1$ for 1.7B).\nWe instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.\n\n\\subsection{Dual-Constraint Framework}\n\\label{sec:dual}\n\nGiven a batch $\\mathcal{B} = \\{x_1, \\ldots, x_B\\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.\n\n\\paragraph{Effective real proportion.}\nLet $r_i = \\mathbf{1}[q_i \\leq 0.5]$ estimate whether sample $x_i$ is human-authored.\nThe \\emph{effective real proportion}\n\\begin{equation}\n  \\alpha_{\\mathrm{eff}}(b) = \\frac{\\sum_{i=1}^{B} w_i(b) \\cdot r_i}{\\sum_{i=1}^{B} w_i(b)}\n  \\label{eq:alpha}\n\\end{equation}\nmeasures the share of total weight allocated to likely-real samples.\nAt $b = 0$, $\\alpha_{\\mathrm{eff}}$ equals the raw real fraction in the batch; increasing $b$ shifts weight toward low-$q$ samples, raising $\\alpha_{\\mathrm{eff}}$.\n\n\\paragraph{Effective sample size.}\nKish's effective sample size~\\citep{vehtari2024psis}\n\\begin{equation}\n  \\mathrm{ESS}(b) = \\frac{\\bigl(\\sum_{i=1}^{B} w_i(b)\\bigr)^{2}}{\\sum_{i=1}^{B} w_i(b)^{2}}\n  \\label{eq:ess}\n\\end{equation}\nquantifies how many equally-weighted samples the weighted batch is equivalent to.\n$\\mathrm{ESS}(0) = B$; as $b$ grows, a few high-$(1{-}q)$ samples dominate and $\\mathrm{ESS}$ drops toward~1.\n\n\\paragraph{Monotonicity.}\nThe two diagnostics exhibit opposing monotonicity in $b$:\n\n\\begin{proposition}\n\\label{prop:monotone}\nFor any batch containing both real and synthetic samples with distinct $q$-values, $\\alpha_{\\mathrm{eff}}(b)$ is strictly increasing in $b$.\n\\end{proposition}\n\n\\begin{proof}[Proof sketch]\nLet $\\pi_i(b) = w_i / \\sum_j w_j$ denote normalized weights.\nDifferentiating $\\alpha_{\\mathrm{eff}} = \\sum_i \\pi_i r_i$ yields\n$\\frac{d\\alpha_{\\mathrm{eff}}}{db} = \\mathrm{Cov}_{\\pi}\\!\\bigl(r_i,\\, \\ln(1{-}q_i)\\bigr)$.\nReal samples ($r_i = 1$) have $q_i \\leq 0.5$ and thus higher $\\ln(1{-}q_i)$, so this covariance is non-negative for any detector with better-than-random discrimination.\nFull derivation in Appendix~\\ref{app:proofs}.\n\\end{proof}\n\n\\noindent $\\mathrm{ESS}(b)$ is monotonically decreasing in $b$---larger exponents concentrate the weight distribution, a standard property of exponential tilting~\\citep{kimura2024iw}.\n\n\\paragraph{Dual constraints.}\nWe impose two requirements on $b$:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{Quality floor}: $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$.\n  Convergence under contaminated training improves with the effective real fraction~\\citep{wang2026survive}; $\\tau$ sets the minimum acceptable quality level.\n  By Proposition~\\ref{prop:monotone}, this constraint defines a \\emph{lower bound} $b_\\tau = \\inf\\{b \\geq 0 : \\alpha_{\\mathrm{eff}}(b) \\geq \\tau\\}$.\n  \\item \\textbf{Stability ceiling}: $\\mathrm{ESS}(b) \\geq n_{\\min}$.\n  Overly concentrated weights yield high-variance gradients; $n_{\\min}$ prevents the batch from degenerating into a single effective sample.\n  Since $\\mathrm{ESS}$ is decreasing, this defines an \\emph{upper bound} $b_{\\mathrm{ESS}} = \\sup\\{b \\geq 0 : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$.\n\\end{enumerate}\nThe optimal exponent is\n\\begin{equation}\n  b^{*} = \\inf\\bigl\\{b \\geq 0 : \\alpha_{\\mathrm{eff}}(b) \\geq \\tau\\bigr\\} \\;\\;\\text{s.t.}\\;\\; \\mathrm{ESS}(b) \\geq n_{\\min}.\n  \\label{eq:bstar}\n\\end{equation}\nThis is the \\emph{minimum intervention principle}: apply the smallest $b$ that achieves the quality floor.\nBorderline samples---those with moderate $q$-values---still carry useful training signal; over-downweighting discards this signal unnecessarily.\nWhen both constraints are satisfiable ($b_\\tau \\leq b_{\\mathrm{ESS}}$), $b^{*} = b_\\tau$ and $\\alpha_{\\mathrm{eff}}$ is the binding constraint---$b^{*}$ lies well below the ESS ceiling.\nWhen they conflict ($b_\\tau > b_{\\mathrm{ESS}}$), the stability ceiling takes precedence: $b^{*} = b_{\\mathrm{ESS}}$, accepting a lower $\\alpha_{\\mathrm{eff}}$ to preserve gradient stability.\nFigure~\\ref{fig:dual_constraint} illustrates the feasible region and the three regimes.\n\n\\subsection{Algorithm}\n\\label{sec:algorithm}\n\nAlgorithm~\\ref{alg:bstar} computes $b^{*}$ for each training batch via bisection on the monotone functions $\\alpha_{\\mathrm{eff}}$ and $\\mathrm{ESS}$.\nEach batch falls into one of three regimes:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{Clean} ($\\alpha_{\\mathrm{eff}}(0) \\geq \\tau$): the quality floor holds at $b = 0$; no reweighting needed.\n  \\item \\textbf{$\\alpha_{\\mathrm{eff}}$-binding} ($b_\\tau \\leq b_{\\mathrm{ESS}}$): the quality constraint determines $b^{*} = b_\\tau$; $\\mathrm{ESS}$ remains above $n_{\\min}$ with margin.\n  \\item \\textbf{ESS-binding} ($b_\\tau > b_{\\mathrm{ESS}}$): the stability ceiling caps $b^{*} = b_{\\mathrm{ESS}}$.\n\\end{enumerate}\nAcross 51{,}913 micro-batches in our main experiment ($\\rho{=}0.4$, $\\tau{=}0.8$, $n_{\\min}{=}2$), 49.9\\% are clean, 20.2\\% are $\\alpha_{\\mathrm{eff}}$-binding, and 30.0\\% are ESS-binding.\nIn $\\alpha_{\\mathrm{eff}}$-binding batches, the solver selects $b^{*} = 1.67$ on average, while an ESS-only strategy would choose $b = 4.15$ on the same batches---2.5$\\times$ more aggressive.\nThe residual $\\mathrm{ESS} = 2.60$ in these batches (vs.\\ $n_{\\min} = 2.0$) confirms that the dual constraint prevents unnecessary over-downweighting.\n\n\\begin{algorithm}[t]\n\\caption{Per-batch adaptive $b^{*}$ selection}\n\\label{alg:bstar}\n\\begin{algorithmic}[1]\n\\Require Batch scores $\\{q_i\\}_{i=1}^{B}$, indicators $\\{r_i\\}$, quality threshold~$\\tau$, ESS floor~$n_{\\min}$, search bound~$b_{\\max}$, tolerance~$\\varepsilon$\n\\Ensure Optimal exponent $b^{*}$\n\\If{$\\alpha_{\\mathrm{eff}}(0) \\geq \\tau$}\n  \\State \\Return $0$ \\Comment{clean batch}\n\\EndIf\n\\State $b_\\tau \\gets \\Call{Bisect}{\\alpha_{\\mathrm{eff}}(\\cdot){=}\\tau,\\; [0, b_{\\max}],\\; \\varepsilon}$\n\\If{$\\mathrm{ESS}(b_\\tau) \\geq n_{\\min}$}\n  \\State \\Return $b_\\tau$ \\Comment{$\\alpha_{\\mathrm{eff}}$-binding}\n\\Else\n  \\State $b_{\\mathrm{ESS}} \\gets \\Call{Bisect}{\\mathrm{ESS}(\\cdot){=}n_{\\min},\\; [0, b_{\\max}],\\; \\varepsilon}$\n  \\State \\Return $b_{\\mathrm{ESS}}$ \\Comment{ESS-binding}\n\\EndIf\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Implementation.}\nGiven $b^{*}$, we compute normalized weights $\\pi_i = w_i(b^{*}) / \\sum_j w_j(b^{*})$ and form the weighted loss $\\mathcal{L} = \\sum_i \\pi_i \\ell_i$, where $\\ell_i$ is the per-sample cross-entropy.\nThis \\emph{loss reweighting} maintains continuous gradients, unlike the SIR resampling of \\citet{drayson2025detection} which introduces discrete sampling noise by drawing a subset proportional to $w_i$.\nEach bisection requires $\\mathcal{O}(B \\log(b_{\\max}/\\varepsilon))$ operations---with $B{=}4$, $b_{\\max}{=}20$, and $\\varepsilon{=}0.01$, roughly 44 floating-point operations per batch, negligible beside the forward and backward passes.\n\n\\subsection{Hyperparameters}\n\\label{sec:hyperparameters}\n\nThe framework introduces two hyperparameters, both with principled defaults set once across all experiments.\n\n\\paragraph{Quality threshold $\\tau$.}\nConvergence theory for contaminated training shows that convergence rate improves with the effective real fraction~\\citep{wang2026survive}, motivating a lower bound on $\\alpha_{\\mathrm{eff}}$.\nThe specific value of $\\tau$ is set empirically.\nWe find a wide safe range: $\\tau \\in [0.5, 0.8]$ consistently outperforms uniform training (Section~\\ref{sec:results}), with $\\tau = 0.8$ achieving the best perplexity.\nAbove 0.8, $b^{*}$ inflates rapidly (mean $b^{*} = 3.08$ at $\\tau = 0.95$), causing over-downweighting.\nWe use $\\tau = 0.8$ as the default throughout.\n\n\\paragraph{ESS floor $n_{\\min}$.}\nWe set $n_{\\min} = 2$ for batch size $B = 4$.\nThe constraint $n_{\\min} < B$ is necessary: $n_{\\min} \\geq B$ forces $b^{*} = 0$ on every batch, recovering uniform training.\nAt the other extreme, $n_{\\min} = 1$ effectively removes the stability constraint---mean $b^{*}$ rises to 7.20, with 46.7\\% of batches hitting the search ceiling at $b_{\\max}{=}20$, and perplexity degrades by $+0.14$ relative to $n_{\\min} = 2$.\nIn practice, $n_{\\min} \\in \\{2, 3\\}$ yields stable results across seeds (Section~\\ref{sec:results}).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex",
    "content": "\n\\subsection{Problem Setup}\n\\label{sec:setup}\n\nLet $\\mathcal{D} = \\mathcal{D}_{\\mathrm{real}} \\cup \\mathcal{D}_{\\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.\nThe contamination ratio $\\rho = |\\mathcal{D}_{\\mathrm{synth}}| / |\\mathcal{D}|$ is unknown---a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\\citep{cheng2025contamination}.\n\nA pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \\in [0,1]$.\nFollowing \\citet{drayson2025detection}, we weight each sample as\n\\begin{equation}\n  w(x) = (1 - q(x))^{b},\n  \\label{eq:weight}\n\\end{equation}\nwhere $b \\geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.\n\\citet{drayson2025detection} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\\leq}360$M parameters, $b{=}1$ for 1.7B).\nWe instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.\n\n\\subsection{Dual-Constraint Framework}\n\\label{sec:dual}\n\nGiven a batch $\\mathcal{B} = \\{x_1, \\ldots, x_B\\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.\n\n\\paragraph{Effective real proportion.}\nLet $r_i = \\mathbf{1}[q_i \\leq 0.5]$ estimate whether sample $x_i$ is human-authored.\nThe \\emph{effective real proportion}\n\\begin{equation}\n  \\alpha_{\\mathrm{eff}}(b) = \\frac{\\sum_{i=1}^{B} w_i(b) \\cdot r_i}{\\sum_{i=1}^{B} w_i(b)}\n  \\label{eq:alpha}\n\\end{equation}\nmeasures the share of total weight allocated to likely-real samples.\nAt $b = 0$, $\\alpha_{\\mathrm{eff}}$ equals the raw real fraction in the batch; increasing $b$ shifts weight toward low-$q$ samples, raising $\\alpha_{\\mathrm{eff}}$.\n\n\\paragraph{Effective sample size.}\nKish's effective sample size~\\citep{vehtari2024psis}\n\\begin{equation}\n  \\mathrm{ESS}(b) = \\frac{\\bigl(\\sum_{i=1}^{B} w_i(b)\\bigr)^{2}}{\\sum_{i=1}^{B} w_i(b)^{2}}\n  \\label{eq:ess}\n\\end{equation}\nquantifies how many equally-weighted samples the weighted batch is equivalent to.\n$\\mathrm{ESS}(0) = B$; as $b$ grows, a few high-$(1{-}q)$ samples dominate and $\\mathrm{ESS}$ drops toward~1.\n\n\\paragraph{Monotonicity.}\nThe two diagnostics exhibit opposing monotonicity in $b$:\n\n\\begin{proposition}\n\\label{prop:monotone}\nFor any batch containing both real and synthetic samples with distinct $q$-values, $\\alpha_{\\mathrm{eff}}(b)$ is strictly increasing in $b$.\n\\end{proposition}\n\n\\begin{proof}[Proof sketch]\nLet $\\pi_i(b) = w_i / \\sum_j w_j$ denote normalized weights.\nDifferentiating $\\alpha_{\\mathrm{eff}} = \\sum_i \\pi_i r_i$ yields\n$\\frac{d\\alpha_{\\mathrm{eff}}}{db} = \\mathrm{Cov}_{\\pi}\\!\\bigl(r_i,\\, \\ln(1{-}q_i)\\bigr)$.\nReal samples ($r_i = 1$) have $q_i \\leq 0.5$ and thus higher $\\ln(1{-}q_i)$, so this covariance is non-negative for any detector with better-than-random discrimination.\nFull derivation in Appendix~\\ref{app:proofs}.\n\\end{proof}\n\n\\noindent $\\mathrm{ESS}(b)$ is monotonically decreasing in $b$---larger exponents concentrate the weight distribution, a standard property of exponential tilting~\\citep{kimura2024iw}.\n\n\\paragraph{Dual constraints.}\nWe impose two requirements on $b$:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{Quality floor}: $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$.\n  Convergence under contaminated training improves with the effective real fraction~\\citep{wang2026survive}; $\\tau$ sets the minimum acceptable quality level.\n  By Proposition~\\ref{prop:monotone}, this constraint defines a \\emph{lower bound} $b_\\tau = \\inf\\{b \\geq 0 : \\alpha_{\\mathrm{eff}}(b) \\geq \\tau\\}$.\n  \\item \\textbf{Stability ceiling}: $\\mathrm{ESS}(b) \\geq n_{\\min}$.\n  Overly concentrated weights yield high-variance gradients; $n_{\\min}$ prevents the batch from degenerating into a single effective sample.\n  Since $\\mathrm{ESS}$ is decreasing, this defines an \\emph{upper bound} $b_{\\mathrm{ESS}} = \\sup\\{b \\geq 0 : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$.\n\\end{enumerate}\nThe optimal exponent is\n\\begin{equation}\n  b^{*} = \\inf\\bigl\\{b \\geq 0 : \\alpha_{\\mathrm{eff}}(b) \\geq \\tau\\bigr\\} \\;\\;\\text{s.t.}\\;\\; \\mathrm{ESS}(b) \\geq n_{\\min}.\n  \\label{eq:bstar}\n\\end{equation}\nThis is the \\emph{minimum intervention principle}: apply the smallest $b$ that achieves the quality floor.\nBorderline samples---those with moderate $q$-values---still carry useful training signal; over-downweighting discards this signal unnecessarily.\nWhen both constraints are satisfiable ($b_\\tau \\leq b_{\\mathrm{ESS}}$), $b^{*} = b_\\tau$ and $\\alpha_{\\mathrm{eff}}$ is the binding constraint---$b^{*}$ lies well below the ESS ceiling.\nWhen they conflict ($b_\\tau > b_{\\mathrm{ESS}}$), the stability ceiling takes precedence: $b^{*} = b_{\\mathrm{ESS}}$, accepting a lower $\\alpha_{\\mathrm{eff}}$ to preserve gradient stability.\nFigure~\\ref{fig:dual_constraint} illustrates the feasible region and the three regimes.\n\n\\subsection{Algorithm}\n\\label{sec:algorithm}\n\nAlgorithm~\\ref{alg:bstar} computes $b^{*}$ for each training batch via bisection on the monotone functions $\\alpha_{\\mathrm{eff}}$ and $\\mathrm{ESS}$.\nEach batch falls into one of three regimes:\n\\begin{enumerate}[nosep,leftmargin=*]\n  \\item \\textbf{Clean} ($\\alpha_{\\mathrm{eff}}(0) \\geq \\tau$): the quality floor holds at $b = 0$; no reweighting needed.\n  \\item \\textbf{$\\alpha_{\\mathrm{eff}}$-binding} ($b_\\tau \\leq b_{\\mathrm{ESS}}$): the quality constraint determines $b^{*} = b_\\tau$; $\\mathrm{ESS}$ remains above $n_{\\min}$ with margin.\n  \\item \\textbf{ESS-binding} ($b_\\tau > b_{\\mathrm{ESS}}$): the stability ceiling caps $b^{*} = b_{\\mathrm{ESS}}$.\n\\end{enumerate}\nAcross 51{,}913 micro-batches in our main experiment ($\\rho{=}0.4$, $\\tau{=}0.8$, $n_{\\min}{=}2$), 49.9\\% are clean, 20.2\\% are $\\alpha_{\\mathrm{eff}}$-binding, and 30.0\\% are ESS-binding.\nIn $\\alpha_{\\mathrm{eff}}$-binding batches, the solver selects $b^{*} = 1.67$ on average, while an ESS-only strategy would choose $b = 4.15$ on the same batches---2.5$\\times$ more aggressive.\nThe residual $\\mathrm{ESS} = 2.60$ in these batches (vs.\\ $n_{\\min} = 2.0$) confirms that the dual constraint prevents unnecessary over-downweighting.\n\n\\begin{algorithm}[t]\n\\caption{Per-batch adaptive $b^{*}$ selection}\n\\label{alg:bstar}\n\\begin{algorithmic}[1]\n\\Require Batch scores $\\{q_i\\}_{i=1}^{B}$, indicators $\\{r_i\\}$, quality threshold~$\\tau$, ESS floor~$n_{\\min}$, search bound~$b_{\\max}$, tolerance~$\\varepsilon$\n\\Ensure Optimal exponent $b^{*}$\n\\If{$\\alpha_{\\mathrm{eff}}(0) \\geq \\tau$}\n  \\State \\Return $0$ \\Comment{clean batch}\n\\EndIf\n\\State $b_\\tau \\gets \\Call{Bisect}{\\alpha_{\\mathrm{eff}}(\\cdot){=}\\tau,\\; [0, b_{\\max}],\\; \\varepsilon}$\n\\If{$\\mathrm{ESS}(b_\\tau) \\geq n_{\\min}$}\n  \\State \\Return $b_\\tau$ \\Comment{$\\alpha_{\\mathrm{eff}}$-binding}\n\\Else\n  \\State $b_{\\mathrm{ESS}} \\gets \\Call{Bisect}{\\mathrm{ESS}(\\cdot){=}n_{\\min},\\; [0, b_{\\max}],\\; \\varepsilon}$\n  \\State \\Return $b_{\\mathrm{ESS}}$ \\Comment{ESS-binding}\n\\EndIf\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Implementation.}\nGiven $b^{*}$, we compute normalized weights $\\pi_i = w_i(b^{*}) / \\sum_j w_j(b^{*})$ and form the weighted loss $\\mathcal{L} = \\sum_i \\pi_i \\ell_i$, where $\\ell_i$ is the per-sample cross-entropy.\nThis \\emph{loss reweighting} maintains continuous gradients, unlike the SIR resampling of \\citet{drayson2025detection} which introduces discrete sampling noise by drawing a subset proportional to $w_i$.\nEach bisection requires $\\mathcal{O}(B \\log(b_{\\max}/\\varepsilon))$ operations---with $B{=}4$, $b_{\\max}{=}20$, and $\\varepsilon{=}0.01$, roughly 44 floating-point operations per batch, negligible beside the forward and backward passes.\n\n\\subsection{Hyperparameters}\n\\label{sec:hyperparameters}\n\nThe framework introduces two hyperparameters, both with principled defaults set once across all experiments.\n\n\\paragraph{Quality threshold $\\tau$.}\nConvergence theory for contaminated training shows that convergence rate improves with the effective real fraction~\\citep{wang2026survive}, motivating a lower bound on $\\alpha_{\\mathrm{eff}}$.\nThe specific value of $\\tau$ is set empirically.\nWe find a wide safe range: $\\tau \\in [0.5, 0.8]$ consistently outperforms uniform training (Section~\\ref{sec:results}), with $\\tau = 0.8$ achieving the best perplexity.\nAbove 0.8, $b^{*}$ inflates rapidly (mean $b^{*} = 3.08$ at $\\tau = 0.95$), causing over-downweighting.\nWe use $\\tau = 0.8$ as the default throughout.\n\n\\paragraph{ESS floor $n_{\\min}$.}\nWe set $n_{\\min} = 2$ for batch size $B = 4$.\nThe constraint $n_{\\min} < B$ is necessary: $n_{\\min} \\geq B$ forces $b^{*} = 0$ on every batch, recovering uniform training.\nAt the other extreme, $n_{\\min} = 1$ effectively removes the stability constraint---mean $b^{*}$ rises to 7.20, with 46.7\\% of batches hitting the search ceiling at $b_{\\max}{=}20$, and perplexity degrades by $+0.14$ relative to $n_{\\min} = 2$.\nIn practice, $n_{\\min} \\in \\{2, 3\\}$ yields stable results across seeds (Section~\\ref{sec:results}).\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T23:57:27.473773+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T23:57:27.473923+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex",
  "content": "\n\\paragraph{Training Data.}\nWe sample a 132M-token subset of FineWeb~\\citep{penedo2024fineweb} as the real-data source.\nTo simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\\citep{yang2025qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\\rho = 0.4$ via uniform random mixing.\nThis self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.\n\n\\paragraph{Detector.}\nWe train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\\,=\\,0.939 with calibrated ECE\\,=\\,0.048 after temperature scaling ($T = 0.204$).\nThe resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\\% of samples in the uncertain range $[0.2, 0.8]$.\nWe use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\\,${\\geq}$\\,0.98 in \\citealt{drayson2025detection}) to test whether score \\emph{calibration} matters more than raw discrimination for reweighting.\n\n\\paragraph{Training.}\nWe continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\\,=\\,$5{\\times}10^{-5}$), max sequence length 2048, and bf16 precision.\nAll main comparisons use three random seeds (42, 123, 456).\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).\nAll evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.\n\n\\paragraph{Methods.}\nWe compare five approaches:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).\n  \\item \\textbf{Grid-$b$}: fixed $b \\in \\{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\}$, best selected post-hoc by held-out PPL.\n        Represents validation-based selection~\\citep{drayson2025detection}.\n  \\item \\textbf{ESS-only}: $b^* = \\max\\{b : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\\alpha_{\\mathrm{eff}}$.\n  \\item \\textbf{Golden Ratio}: $w = 1/\\varphi \\approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\\citep{he2025golden}.\n        Requires known provenance labels (oracle).\n  \\item \\textbf{Adaptive} (ours): per-batch $b^*$ from the dual-constraint formulation (\\S\\ref{sec:method}), with $\\tau = 0.8$ and $n_{\\min} = 2$ (half the micro-batch size).\n\\end{itemize}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex",
    "content": "\n\\paragraph{Training Data.}\nWe sample a 132M-token subset of FineWeb~\\citep{penedo2024fineweb} as the real-data source.\nTo simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\\citep{yang2025qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\\rho = 0.4$ via uniform random mixing.\nThis self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.\n\n\\paragraph{Detector.}\nWe train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\\,=\\,0.939 with calibrated ECE\\,=\\,0.048 after temperature scaling ($T = 0.204$).\nThe resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\\% of samples in the uncertain range $[0.2, 0.8]$.\nWe use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\\,${\\geq}$\\,0.98 in \\citealt{drayson2025detection}) to test whether score \\emph{calibration} matters more than raw discrimination for reweighting.\n\n\\paragraph{Training.}\nWe continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\\,=\\,$5{\\times}10^{-5}$), max sequence length 2048, and bf16 precision.\nAll main comparisons use three random seeds (42, 123, 456).\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).\nAll evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.\n\n\\paragraph{Methods.}\nWe compare five approaches:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).\n  \\item \\textbf{Grid-$b$}: fixed $b \\in \\{0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\}$, best selected post-hoc by held-out PPL.\n        Represents validation-based selection~\\citep{drayson2025detection}.\n  \\item \\textbf{ESS-only}: $b^* = \\max\\{b : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$, the maximum-intervention variant retaining only the stability constraint, ablating $\\alpha_{\\mathrm{eff}}$.\n  \\item \\textbf{Golden Ratio}: $w = 1/\\varphi \\approx 0.618$ for synthetic ($q_j > 0.5$), $w = 1$ otherwise~\\citep{he2025golden}.\n        Requires known provenance labels (oracle).\n  \\item \\textbf{Adaptive} (ours): per-batch $b^*$ from the dual-constraint formulation (\\S\\ref{sec:method}), with $\\tau = 0.8$ and $n_{\\min} = 2$ (half the micro-batch size).\n\\end{itemize}\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T23:57:27.474068+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T23:57:27.474198+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex",
  "content": "\n\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation---\\emph{model collapse}~\\citep{shumailov2024model}.\n\\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\nMore critically, \\citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.\n\\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\\% of web corpora.\nThese results motivate \\emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.\n\n\\paragraph{Detection and Filtering of Machine-Generated Text.}\nGiven the severity of contamination, a natural response is to detect and remove synthetic content.\nDetectGPT~\\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\% Prob~\\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\\% tokens as a reference-free signal.\nBoth produce continuous confidence scores suitable as input to downstream weighting---including ours.\nOn the mitigation side, \\citet{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.\n\\citet{guo2025escaping} similarly rely on verification-based selection.\nHard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.\n\nMost directly related to our work, \\citet{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic probability.\nWe adopt the same weighting formula but differ in several fundamental ways.\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\leq}360$M, $b{=}1$ for 1.7B), making the choice \\emph{per-model} and expensive.\nOur $b^*$ is derived per-batch from dual constraints ($\\alpha_{\\mathrm{eff}} \\geq \\tau$, $\\mathrm{ESS} \\geq n_{\\min}$) at zero validation cost.\n\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradients.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\,=\\,0.939) suffices on FineWeb-scale data (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.\n\n\\paragraph{Data Mixing and Instance-Level Reweighting.}\nA parallel line of work optimizes data composition without targeting synthetic contamination.\nAt the \\emph{domain} level, DoReMi~\\citep{xie2023doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\\citep{xie2023dsir} performs importance resampling with $n$-gram features, and \\citet{ye2025mixing} discover predictable functional forms relating mixing ratios to performance.\nAIOLI~\\citep{chen2025aioli} unifies these into an online adaptive framework, while \\citet{yang2026mixing} train an RL agent for domain-weight selection.\nThese methods do not address instance-level contamination within a domain.\nAt the \\emph{instance} level, SoftDedup~\\citep{he2024softdedup} downweights high-frequency samples via $n$-gram commonness, \\citet{sow2025dynamic} derive sample weights from per-sample loss with convergence guarantees, and \\citet{kuo2024weighting} show that differentiated weighting of LLM-generated data improves downstream classification.\nOur reweighting differs from all of these in being driven by \\emph{provenance}---detector scores estimating human vs.\\ synthetic origin---rather than loss, frequency, or domain membership.\n\n\\paragraph{Theoretical Foundations.}\n\\citet{he2025golden} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\\approx}0.62$) optimal when both sources are equally sized.\nTheir result requires the contamination ratio $k$, unavailable in web-scale settings; we use it as an oracle baseline.\n\\citet{wang2026survive} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ guarantees a convergence-rate lower bound.\nWe operationalize this without the known-proportion assumption, estimating $\\alpha_{\\mathrm{eff}}$ from batch-level statistics online.\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \\citet{vehtari2024psis}.\n\\citet{kimura2024iw} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as a special case of covariate-shift correction where the covariate is synthetic origin probability.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex",
    "content": "\n\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation---\\emph{model collapse}~\\citep{shumailov2024model}.\n\\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.\nMore critically, \\citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.\n\\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\\% of web corpora.\nThese results motivate \\emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.\n\n\\paragraph{Detection and Filtering of Machine-Generated Text.}\nGiven the severity of contamination, a natural response is to detect and remove synthetic content.\nDetectGPT~\\citep{mitchell2023detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\\% Prob~\\citep{shi2024minkprob} uses the average log-probability of the lowest-$k$\\% tokens as a reference-free signal.\nBoth produce continuous confidence scores suitable as input to downstream weighting---including ours.\nOn the mitigation side, \\citet{feng2025beyond} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.\n\\citet{guo2025escaping} similarly rely on verification-based selection.\nHard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.\n\nMost directly related to our work, \\citet{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight, where $q_j$ is the detector's synthetic probability.\nWe adopt the same weighting formula but differ in several fundamental ways.\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search and fix it throughout training; different model scales require different values ($b{=}10$ for ${\\leq}360$M, $b{=}1$ for 1.7B), making the choice \\emph{per-model} and expensive.\nOur $b^*$ is derived per-batch from dual constraints ($\\alpha_{\\mathrm{eff}} \\geq \\tau$, $\\mathrm{ESS} \\geq n_{\\min}$) at zero validation cost.\n\\textbf{(ii)}~Their SIR resampling discretizes the weight distribution; we apply direct loss reweighting with continuous gradients.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF+LR detector (AUC\\,=\\,0.939) suffices on FineWeb-scale data (132M+ tokens), suggesting that score calibration matters more than raw detection accuracy.\n\n\\paragraph{Data Mixing and Instance-Level Reweighting.}\nA parallel line of work optimizes data composition without targeting synthetic contamination.\nAt the \\emph{domain} level, DoReMi~\\citep{xie2023doremi} learns mixture weights via Group DRO with a proxy model, DSIR~\\citep{xie2023dsir} performs importance resampling with $n$-gram features, and \\citet{ye2025mixing} discover predictable functional forms relating mixing ratios to performance.\nAIOLI~\\citep{chen2025aioli} unifies these into an online adaptive framework, while \\citet{yang2026mixing} train an RL agent for domain-weight selection.\nThese methods do not address instance-level contamination within a domain.\nAt the \\emph{instance} level, SoftDedup~\\citep{he2024softdedup} downweights high-frequency samples via $n$-gram commonness, \\citet{sow2025dynamic} derive sample weights from per-sample loss with convergence guarantees, and \\citet{kuo2024weighting} show that differentiated weighting of LLM-generated data improves downstream classification.\nOur reweighting differs from all of these in being driven by \\emph{provenance}---detector scores estimating human vs.\\ synthetic origin---rather than loss, frequency, or domain membership.\n\n\\paragraph{Theoretical Foundations.}\n\\citet{he2025golden} derive the optimal real-data weight under known mixture proportions, finding the golden-ratio reciprocal (${\\approx}0.62$) optimal when both sources are equally sized.\nTheir result requires the contamination ratio $k$, unavailable in web-scale settings; we use it as an oracle baseline.\n\\citet{wang2026survive} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$, providing the theoretical motivation for our quality threshold: ensuring $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ guarantees a convergence-rate lower bound.\nWe operationalize this without the known-proportion assumption, estimating $\\alpha_{\\mathrm{eff}}$ from batch-level statistics online.\nFor the stability constraint, we build on Kish's effective sample size and the Pareto-smoothed importance sampling framework of \\citet{vehtari2024psis}.\n\\citet{kimura2024iw} provide a broader treatment of importance weighting under distribution shift, within which our provenance-based reweighting can be viewed as a special case of covariate-shift correction where the covariate is synthetic origin probability.\n"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T23:57:27.474354+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T23:57:27.474485+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex",
  "content": "\n\\subsection{Main Comparison}\n\nTable~\\ref{tab:main} reports held-out perplexity across methods and seeds.\nAdaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).\nThis parity comes at zero validation cost---grid search requires $|\\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.\n\nThe grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\\ref{app:grid}), confirming that exponent selection is consequential.\nThe optimal $b{=}0.5$ differs from the $b{=}10$ reported by \\citet{drayson2025detection} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.\n\nESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \\emph{worse} than uniform (17.694) by 0.029.\nRemoving $\\alpha_{\\mathrm{eff}}$ and maximizing $b$ subject only to $\\mathrm{ESS} \\geq n_{\\min}$ leads to over-downweighting that degrades training, providing direct evidence for the minimum-intervention principle.\n\nThe Golden Ratio oracle~\\citep{he2025golden} achieves PPL 17.654 on seed 42 using known provenance labels.\nAdaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.\n\nThe adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.\nThe constraint regime breakdown in \\S\\ref{sec:algorithm} shows that $\\alpha_{\\mathrm{eff}}$ prevents over-intervention in the 40\\% of reweighted batches where moderate $b$ already meets the quality target.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 456} & \\textbf{Mean} \\\\\n\\midrule\nUniform               & 17.694 & 17.686 & 17.702 & 17.694 \\\\\nGrid-best ($b{=}0.5$) & \\textbf{17.651} & \\textbf{17.638} & \\textbf{17.650} & \\textbf{17.646} \\\\\nESS-only               & 17.730 & 17.720 & 17.719 & 17.723 \\\\\nGolden Ratio$^\\dagger$ & 17.654 & --     & --     & --     \\\\\n\\midrule\nAdaptive (ours)        & 17.653 & 17.643 & 17.657 & 17.651 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Held-out perplexity (PPL, $\\downarrow$).\nGrid-best selects the optimal fixed $b$ post-hoc from six candidates.\n$^\\dagger$Evaluated on seed 42 only.\nBest per column in \\textbf{bold}.}\n\\label{tab:main}\n\\end{table}\n\n\\subsection{Sensitivity Analysis}\n\n\\paragraph{Quality threshold $\\tau$.}\nTable~\\ref{tab:tau} varies $\\tau$ while holding $n_{\\min} = 2$ (seed 42).\nAll values in $\\tau \\in [0.5, 0.8]$ improve over uniform, with $\\tau = 0.8$ achieving the lowest PPL (17.653).\nHigher $\\tau$ demands greater $\\alpha_{\\mathrm{eff}}$, forcing the solver to increase $b^*$: mean $\\bar{b}^*$ rises monotonically from 0.39 at $\\tau{=}0.5$ to 3.08 at $\\tau{=}0.95$.\nBelow 0.8, reweighting is too gentle to fully exploit the detector signal; above, $b^*$ inflates past diminishing returns and PPL degrades.\nThe range $[0.5, 0.8]$ provides a wide safe operating region, with $\\tau = 0.8$ as the recommended default.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\tau$ & \\textbf{PPL} & $\\Delta_{\\mathrm{unif}}$ & $\\bar{b}^*$ \\\\\n\\midrule\n0.50 & 17.688 & $-$0.006 & 0.39 \\\\\n0.60 & 17.681 & $-$0.013 & 0.59 \\\\\n0.70 & 17.679 & $-$0.015 & 0.89 \\\\\n\\textbf{0.80} & \\textbf{17.653} & $\\mathbf{-0.041}$ & \\textbf{1.40} \\\\\n0.90 & 17.712 & $+$0.018 & 2.36 \\\\\n0.95 & 17.723 & $+$0.029 & 3.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to $\\tau$ (seed 42, $n_{\\min}{=}2$, $\\rho{=}0.4$).\n$\\Delta_{\\mathrm{unif}}$: PPL change vs.\\ uniform baseline (17.694).\n$\\bar{b}^*$: mean adaptive exponent across batches.}\n\\label{tab:tau}\n\\end{table}\n\n\\paragraph{Minimum ESS $n_{\\min}$.}\nRemoving the ESS floor ($n_{\\min} = 1$) allows $b^*$ to inflate to mean 7.20, degrading PPL to 17.789---0.095 worse than uniform.\nAt $n_{\\min} = 2$ ($= \\lfloor B/2 \\rfloor$ for batch size $B{=}4$), PPL stabilizes at 17.653; $n_{\\min} = 3$ yields a comparable 17.644.\nThe coupling $n_{\\min} = \\lfloor B/2 \\rfloor$ provides a configuration-aware default that balances reweighting headroom against gradient stability.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex",
    "content": "\n\\subsection{Main Comparison}\n\nTable~\\ref{tab:main} reports held-out perplexity across methods and seeds.\nAdaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).\nThis parity comes at zero validation cost---grid search requires $|\\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.\n\nThe grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\\ref{app:grid}), confirming that exponent selection is consequential.\nThe optimal $b{=}0.5$ differs from the $b{=}10$ reported by \\citet{drayson2025detection} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.\n\nESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \\emph{worse} than uniform (17.694) by 0.029.\nRemoving $\\alpha_{\\mathrm{eff}}$ and maximizing $b$ subject only to $\\mathrm{ESS} \\geq n_{\\min}$ leads to over-downweighting that degrades training, providing direct evidence for the minimum-intervention principle.\n\nThe Golden Ratio oracle~\\citep{he2025golden} achieves PPL 17.654 on seed 42 using known provenance labels.\nAdaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.\n\nThe adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.\nThe constraint regime breakdown in \\S\\ref{sec:algorithm} shows that $\\alpha_{\\mathrm{eff}}$ prevents over-intervention in the 40\\% of reweighted batches where moderate $b$ already meets the quality target.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 456} & \\textbf{Mean} \\\\\n\\midrule\nUniform               & 17.694 & 17.686 & 17.702 & 17.694 \\\\\nGrid-best ($b{=}0.5$) & \\textbf{17.651} & \\textbf{17.638} & \\textbf{17.650} & \\textbf{17.646} \\\\\nESS-only               & 17.730 & 17.720 & 17.719 & 17.723 \\\\\nGolden Ratio$^\\dagger$ & 17.654 & --     & --     & --     \\\\\n\\midrule\nAdaptive (ours)        & 17.653 & 17.643 & 17.657 & 17.651 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Held-out perplexity (PPL, $\\downarrow$).\nGrid-best selects the optimal fixed $b$ post-hoc from six candidates.\n$^\\dagger$Evaluated on seed 42 only.\nBest per column in \\textbf{bold}.}\n\\label{tab:main}\n\\end{table}\n\n\\subsection{Sensitivity Analysis}\n\n\\paragraph{Quality threshold $\\tau$.}\nTable~\\ref{tab:tau} varies $\\tau$ while holding $n_{\\min} = 2$ (seed 42).\nAll values in $\\tau \\in [0.5, 0.8]$ improve over uniform, with $\\tau = 0.8$ achieving the lowest PPL (17.653).\nHigher $\\tau$ demands greater $\\alpha_{\\mathrm{eff}}$, forcing the solver to increase $b^*$: mean $\\bar{b}^*$ rises monotonically from 0.39 at $\\tau{=}0.5$ to 3.08 at $\\tau{=}0.95$.\nBelow 0.8, reweighting is too gentle to fully exploit the detector signal; above, $b^*$ inflates past diminishing returns and PPL degrades.\nThe range $[0.5, 0.8]$ provides a wide safe operating region, with $\\tau = 0.8$ as the recommended default.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\tau$ & \\textbf{PPL} & $\\Delta_{\\mathrm{unif}}$ & $\\bar{b}^*$ \\\\\n\\midrule\n0.50 & 17.688 & $-$0.006 & 0.39 \\\\\n0.60 & 17.681 & $-$0.013 & 0.59 \\\\\n0.70 & 17.679 & $-$0.015 & 0.89 \\\\\n\\textbf{0.80} & \\textbf{17.653} & $\\mathbf{-0.041}$ & \\textbf{1.40} \\\\\n0.90 & 17.712 & $+$0.018 & 2.36 \\\\\n0.95 & 17.723 & $+$0.029 & 3.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity to $\\tau$ (seed 42, $n_{\\min}{=}2$, $\\rho{=}0.4$).\n$\\Delta_{\\mathrm{unif}}$: PPL change vs.\\ uniform baseline (17.694).\n$\\bar{b}^*$: mean adaptive exponent across batches.}\n\\label{tab:tau}\n\\end{table}\n\n\\paragraph{Minimum ESS $n_{\\min}$.}\nRemoving the ESS floor ($n_{\\min} = 1$) allows $b^*$ to inflate to mean 7.20, degrading PPL to 17.789---0.095 worse than uniform.\nAt $n_{\\min} = 2$ ($= \\lfloor B/2 \\rfloor$ for batch size $B{=}4$), PPL stabilizes at 17.653; $n_{\\min} = 3$ yields a comparable 17.644.\nThe coupling $n_{\\min} = \\lfloor B/2 \\rfloor$ provides a configuration-aware default that balances reweighting headroom against gradient stability.\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T23:57:27.474637+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T23:57:27.474756+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex",
  "content": "\nWe introduced Minimum Intervention Reweighting, a dual-constrained framework for contamination-aware pretraining that selects per-batch exponents $b^*$ without validation data.\nThe method finds the smallest $b$ satisfying $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ subject to $\\mathrm{ESS}(b) \\geq n_{\\min}$, enforcing a minimum-intervention principle: apply only as much downweighting as needed to meet a quality floor, no more.\nThis stands in direct contrast to ESS-only (maximum-intervention) strategies, which we show degrade performance below even uniform baselines by over-downweighting contaminated samples.\n\nAcross three seeds at 0.6B scale with 40\\% synthetic contamination, adaptive $b^*$ matches grid-search-optimal PPL (17.651 vs.\\ 17.646) within seed variance, eliminating the $|\\mathcal{B}|$-run grid search entirely.\nThe quality threshold $\\tau$ is robust across $[0.5, 0.8]$---all values in this range outperform uniform weighting.\nA lightweight TF-IDF + logistic regression detector (AUC\\,0.94) suffices when post-hoc calibrated (ECE\\,0.048); score calibration matters more than raw discriminative power.\nThe batch-level constraint regime---49.9\\% clean (no reweighting needed), 20.2\\% $\\alpha_{\\mathrm{eff}}$-binding, 30.0\\% ESS-binding---confirms that both constraints are active and complementary in practice.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex",
    "content": "\nWe introduced Minimum Intervention Reweighting, a dual-constrained framework for contamination-aware pretraining that selects per-batch exponents $b^*$ without validation data.\nThe method finds the smallest $b$ satisfying $\\alpha_{\\mathrm{eff}}(b) \\geq \\tau$ subject to $\\mathrm{ESS}(b) \\geq n_{\\min}$, enforcing a minimum-intervention principle: apply only as much downweighting as needed to meet a quality floor, no more.\nThis stands in direct contrast to ESS-only (maximum-intervention) strategies, which we show degrade performance below even uniform baselines by over-downweighting contaminated samples.\n\nAcross three seeds at 0.6B scale with 40\\% synthetic contamination, adaptive $b^*$ matches grid-search-optimal PPL (17.651 vs.\\ 17.646) within seed variance, eliminating the $|\\mathcal{B}|$-run grid search entirely.\nThe quality threshold $\\tau$ is robust across $[0.5, 0.8]$---all values in this range outperform uniform weighting.\nA lightweight TF-IDF + logistic regression detector (AUC\\,0.94) suffices when post-hoc calibrated (ECE\\,0.048); score calibration matters more than raw discriminative power.\nThe batch-level constraint regime---49.9\\% clean (no reweighting needed), 20.2\\% $\\alpha_{\\mathrm{eff}}$-binding, 30.0\\% ESS-binding---confirms that both constraints are active and complementary in practice.\n"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T23:57:27.474902+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T23:57:27.475026+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex",
  "content": "\n\\paragraph{Scale.}\nAll experiments use a single model size (Qwen3-0.6B) with batch size 4.\nBatch-level $q$-score statistics concentrate differently at larger batch sizes typical of 3B+ training; the optimal $\\tau$ range and constraint dynamics may shift at scale.\n\n\\paragraph{Contamination distribution.}\nWe inject synthetic data via uniform random mixing at a controlled ratio ($\\rho{=}0.4$).\nReal web-scale contamination is domain-skewed, which may alter within-batch $\\alpha_{\\mathrm{eff}}$ distributions and require domain-aware extensions.\n\n\\paragraph{Detector coverage.}\nWe evaluate one detector family (TF-IDF + logistic regression).\nAlthough our results suggest calibration dominates discrimination for reweighting quality, a systematic ablation across detector architectures and quality levels is needed.\n\n\\paragraph{Threshold.}\n$\\tau$ is an empirical hyperparameter.\nThe convergence theory of \\citet{wang2026survive} assumes a known contamination proportion $\\alpha$, which we do not require; bridging this gap to derive $\\tau$ from first principles remains open.\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity only.\nDownstream task evaluation (MMLU, HellaSwag) would strengthen the practical case, particularly at scales where PPL differences translate more reliably to task performance.\n\n\\paragraph{Effect size.}\nThe PPL improvement over uniform weighting is 0.043 at 0.6B/40\\% contamination.\nWhile consistent across seeds, this effect is modest; we expect amplification at higher contamination ratios and larger model scales, but verification is ongoing.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex",
    "content": "\n\\paragraph{Scale.}\nAll experiments use a single model size (Qwen3-0.6B) with batch size 4.\nBatch-level $q$-score statistics concentrate differently at larger batch sizes typical of 3B+ training; the optimal $\\tau$ range and constraint dynamics may shift at scale.\n\n\\paragraph{Contamination distribution.}\nWe inject synthetic data via uniform random mixing at a controlled ratio ($\\rho{=}0.4$).\nReal web-scale contamination is domain-skewed, which may alter within-batch $\\alpha_{\\mathrm{eff}}$ distributions and require domain-aware extensions.\n\n\\paragraph{Detector coverage.}\nWe evaluate one detector family (TF-IDF + logistic regression).\nAlthough our results suggest calibration dominates discrimination for reweighting quality, a systematic ablation across detector architectures and quality levels is needed.\n\n\\paragraph{Threshold.}\n$\\tau$ is an empirical hyperparameter.\nThe convergence theory of \\citet{wang2026survive} assumes a known contamination proportion $\\alpha$, which we do not require; bridging this gap to derive $\\tau$ from first principles remains open.\n\n\\paragraph{Evaluation.}\nWe report held-out perplexity only.\nDownstream task evaluation (MMLU, HellaSwag) would strengthen the practical case, particularly at scales where PPL differences translate more reliably to task performance.\n\n\\paragraph{Effect size.}\nThe PPL improvement over uniform weighting is 0.043 at 0.6B/40\\% contamination.\nWhile consistent across seeds, this effect is modest; we expect amplification at higher contamination ratios and larger model scales, but verification is ongoing.\n"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T23:57:27.475150+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T23:57:27.475285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T23:57:27.475430+00:00_

1	Web corpora increasingly contain machine-generated text.
2	Recent estimates place the synthetic fraction at 20--60\% of crawled data~\citep{cheng_2025_contamination_survey}, and this share grows as language models are deployed for content production at scale.
3	Training on such contaminated data has concrete consequences: \citet{shumailov_2024_model_collapse} show that recursive training on model outputs leads to irreversible quality degradation---\emph{model collapse}---and \citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.
4	A central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.
5	The prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.
6	
7	A natural response is \emph{detect-and-reweight}: train a classifier to estimate each sample's synthetic probability $q(x)$, then suppress likely-synthetic samples via the weighting function $w(x) = (1 - q(x))^b$.
8	\citet{drayson_2025_detection_collapse} demonstrate this approach for model collapse prevention and show that the exponent $b$ critically determines outcomes---their optimal values range from $b{=}10$ for models at ${\leq}360$M parameters to $b{=}1$ at 1.7B, and misspecification degrades results substantially.
9	Selecting $b$ therefore requires per-model validation-set grid search, with computational cost scaling linearly in the number of candidates (six training runs in a typical sweep).
10	Other approaches assume even stronger supervision: \citet{he_2025_golden_ratio} derive theoretically optimal weights from convergence analysis but require the exact contamination ratio $\rho$, which is precisely what is unavailable in practice.
11	Hard detection-and-removal strategies
…[truncated 3953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T23:57:27.475571+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T23:57:27.475762+00:00_

1	\subsection{Problem Setup}
2	\label{sec:setup}
3	
4	Let $\mathcal{D} = \mathcal{D}_{\mathrm{real}} \cup \mathcal{D}_{\mathrm{synth}}$ denote a pretraining corpus containing both human-authored and machine-generated text.
5	The contamination ratio $\rho = |\mathcal{D}_{\mathrm{synth}}| / |\mathcal{D}|$ is unknown---a realistic assumption for web-scale corpora where synthetic content enters from diverse, uncoordinated sources~\citep{cheng_2025_contamination_survey}.
6	
7	A pre-trained detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$.
8	Following \citet{drayson_2025_detection_collapse}, we weight each sample as
9	\begin{equation}
10	  w(x) = (1 - q(x))^{b},
11	  \label{eq:weight}
12	\end{equation}
13	where $b \geq 0$ controls downweighting intensity: $b = 0$ recovers uniform training, while larger $b$ progressively suppresses high-$q$ samples.
14	\citet{drayson_2025_detection_collapse} select $b$ via validation-set grid search, obtaining different optimal values for different model scales ($b{=}10$ for ${\leq}360$M parameters, $b{=}1$ for 1.7B).
15	We instead derive $b$ per-batch from the batch's own $q$-score distribution, requiring no held-out validation data.
16	
17	\subsection{Dual-Constraint Framework}
18	\label{sec:dual}
19	
20	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with detector scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$, we define two batch-level diagnostics that jointly determine $b$.
21	
22	\paragraph{Effective real proportion.}
23	Let $r_i = \mathbf{1}[q_i \leq 0.5]$ estimate whether sample $x_i$ is human-authored.
24	The \emph{effective real proportion}
25	\begin{equation}
26	  \alpha_{\mathrm{eff}}(b) = \frac{\sum_{i=1}^{B} w_i(b) \cdot r_i}{\sum_{i=1}^{B} w_i(b)}
27	  \label{eq:alpha}
28	\end{equation}
29	measures the share of total weight allocated to likely-real samples.
30	At $b = 0$, $\alpha_{\mathrm{eff}}$ equals the raw real fraction in the batch; increasing $b$ shifts weight toward low-$q$ samp
…[truncated 7652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T23:57:27.475933+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T23:57:27.476081+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo_2024_fineweb} as the real-data source.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang_2025_qwen3}---the same architecture used for continued pretraining---and inject them at ratio $\rho = 0.4$ via uniform random mixing.
4	This self-contamination design creates a challenging detection scenario where generator and trainee share the same distribution.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split, achieving AUC\,=\,0.939 with calibrated ECE\,=\,0.048 after temperature scaling ($T = 0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson_2025_detection_collapse}) to test whether score \emph{calibration} matters more than raw discrimination for reweighting.
10	
11	\paragraph{Training.}
12	We continue pretraining Qwen3-0.6B from its pretrained weights for 6{,}103 steps (batch size 4, gradient accumulation 4, effective batch 16) with AdamW, cosine schedule (peak lr\,=\,$5{\times}10^{-5}$), max sequence length 2048, and bf16 precision.
13	All main comparisons use three random seeds (42, 123, 456).
14	
15	\paragraph{Evaluation.}
16	We report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).
17	All evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.
18	
19	\paragraph{Methods.}
20	We compare five approaches:
21	\begin{itemize}[nosep,leftmargin=*]
22	  \item \textbf{Uniform}: $w_j = 1$ for all $j$ (no contamination handling).
23	  \item \textbf{Grid-$b$}: fixed $b \in \{0.5, 1.0, 1.5, 2.0, 3.0, 5
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T23:57:27.476220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T23:57:27.476368+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation---\emph{model collapse}~\citep{shumailov_2024_model_collapse}.
3	\citet{alemohammad_2024_mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
4	More critically, \citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
5	\citet{cheng_2025_contamination_survey} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
6	These results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.
7	
8	\paragraph{Detection and Filtering of Machine-Generated Text.}
9	Given the severity of contamination, a natural response is to detect and remove synthetic content.
10	DetectGPT~\citep{mitchell_2023_detectgpt} performs zero-shot detection via probability curvature, while Min-$k$\% Prob~\citep{shi_2024_minkprob} uses the average log-probability of the lowest-$k$\% tokens as a reference-free signal.
11	Both produce continuous confidence scores suitable as input to downstream weighting---including ours.
12	On the mitigation side, \citet{feng_2025_beyond_collapse} prove that even an imperfect verifier prevents collapse, but apply hard binary filtering that discards borderline samples.
13	\citet{guo_2025_escaping_collapse} similarly rely on verification-based selection.
14	Hard filtering requires a precision--recall threshold; soft reweighting avoids this trade-off by assigning continuous weights.
15	
16	Most directly related to our work, \citet{drayson_2025_detection_collapse} propose $w_j = (1{-}q_j)^b$ for collapse preve
…[truncated 3523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T23:57:27.476509+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T23:57:27.476663+00:00_

1	\subsection{Main Comparison}
2	
3	Table~\ref{tab:main} reports held-out perplexity across methods and seeds.
4	Adaptive reweighting achieves mean PPL 17.651, matching grid-best ($b{=}0.5$, mean 17.646) within seed-to-seed variance: the per-seed gap never exceeds 0.007, less than half the cross-seed range of the uniform baseline (17.686--17.702).
5	This parity comes at zero validation cost---grid search requires $|\mathcal{B}|$ complete training runs (six in our sweep), whereas adaptive requires one.
6	
7	The grid-$b$ sweep reveals monotonically increasing PPL from $b{=}0.5$ to $b{=}5.0$ (17.651 to 17.818 on seed 42; full sweep in Appendix~\ref{app:grid}), confirming that exponent selection is consequential.
8	The optimal $b{=}0.5$ differs from the $b{=}10$ reported by \citet{drayson_2025_detection_collapse} at comparable model scale, underscoring the model-dependence of fixed-exponent selection.
9	
10	ESS-only (maximum intervention) yields mean PPL 17.723 across three seeds, \emph{worse} than uniform (17.694) by 0.029.
11	Removing $\alpha_{\mathrm{eff}}$ and maximizing $b$ subject only to $\mathrm{ESS} \geq n_{\min}$ leads to over-downweighting that degrades training, providing direct evidence for the minimum-intervention principle.
12	
13	The Golden Ratio oracle~\citep{he_2025_golden_ratio} achieves PPL 17.654 on seed 42 using known provenance labels.
14	Adaptive reaches within 0.001 of this upper bound without provenance access, suggesting the dual constraint recovers near-optimal weights from noisy detector scores alone.
15	
16	The adaptive $b^*$ distribution (median 0.87, IQR $[0.54, 1.51]$, mean 1.40) confirms that most batches need only moderate intervention.
17	The constraint regime breakdown in \S\ref{sec:algorithm} shows that $\alpha_{\mathrm{eff}}$ prevents over-intervention in the 40\% of reweighted batches where moderate $b$ already meets the quality target.
18	
19	\begin{table}[t]
20	\centering
21	\small
22	\begin{tabular}{@{}lcccc@{}}
23	\toprule
24	
…[truncated 2639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T23:57:27.476806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T23:57:27.476981+00:00_

1	We introduced Minimum Intervention Reweighting, a dual-constrained framework for contamination-aware pretraining that selects per-batch exponents $b^*$ without validation data.
2	The method finds the smallest $b$ satisfying $\alpha_{\mathrm{eff}}(b) \geq \tau$ subject to $\mathrm{ESS}(b) \geq n_{\min}$, enforcing a minimum-intervention principle: apply only as much downweighting as needed to meet a quality floor, no more.
3	This stands in direct contrast to ESS-only (maximum-intervention) strategies, which we show degrade performance below even uniform baselines by over-downweighting contaminated samples.
4	
5	Across three seeds at 0.6B scale with 40\% synthetic contamination, adaptive $b^*$ matches grid-search-optimal PPL (17.651 vs.\ 17.646) within seed variance, eliminating the $|\mathcal{B}|$-run grid search entirely.
6	The quality threshold $\tau$ is robust across $[0.5, 0.8]$---all values in this range outperform uniform weighting.
7	A lightweight TF-IDF + logistic regression detector (AUC\,0.94) suffices when post-hoc calibrated (ECE\,0.048); score calibration matters more than raw discriminative power.
8	The batch-level constraint regime---49.9\% clean (no reweighting needed), 20.2\% $\alpha_{\mathrm{eff}}$-binding, 30.0\% ESS-binding---confirms that both constraints are active and complementary in practice.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T23:57:27.477126+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T23:57:27.477260+00:00_

1	\paragraph{Scale.}
2	All experiments use a single model size (Qwen3-0.6B) with batch size 4.
3	Batch-level $q$-score statistics concentrate differently at larger batch sizes typical of 3B+ training; the optimal $\tau$ range and constraint dynamics may shift at scale.
4	
5	\paragraph{Contamination distribution.}
6	We inject synthetic data via uniform random mixing at a controlled ratio ($\rho{=}0.4$).
7	Real web-scale contamination is domain-skewed, which may alter within-batch $\alpha_{\mathrm{eff}}$ distributions and require domain-aware extensions.
8	
9	\paragraph{Detector coverage.}
10	We evaluate one detector family (TF-IDF + logistic regression).
11	Although our results suggest calibration dominates discrimination for reweighting quality, a systematic ablation across detector architectures and quality levels is needed.
12	
13	\paragraph{Threshold.}
14	$\tau$ is an empirical hyperparameter.
15	The convergence theory of \citet{wang_2026_survive_contamination} assumes a known contamination proportion $\alpha$, which we do not require; bridging this gap to derive $\tau$ from first principles remains open.
16	
17	\paragraph{Evaluation.}
18	We report held-out perplexity only.
19	Downstream task evaluation (MMLU, HellaSwag) would strengthen the practical case, particularly at scales where PPL differences translate more reliably to task performance.
20	
21	\paragraph{Effect size.}
22	The PPL improvement over uniform weighting is 0.043 at 0.6B/40\% contamination.
23	While consistent across seeds, this effect is modest; we expect amplification at higher contamination ratios and larger model scales, but verification is ongoing.
24	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T23:57:27.477454+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections && python3 -c \"\nimport os, re\n\n# Citation key mapping: artifact_format -> bib_format\nmapping = {\n    'cheng_2025_contamination_survey': 'cheng2025contamination',\n    'shumailov_2024_model_collapse': 'shumailov2024model',\n    'dohmatob_2025_strong_collapse': 'dohmatob2025strong',\n    'drayson_2025_detection_collapse': 'drayson2025detection',\n    'he_2025_golden_ratio': 'he2025golden',\n    'wang_2026_survive_contamination': 'wang2026survive',\n    'vehtari_2024_psis': 'vehtari2024psis',\n    'feng_2025_beyond_collapse': 'feng2025beyond',\n    'guo_2025_escaping_collapse': 'guo2025escaping',\n    'mitchell_2023_detectgpt': 'mitchell2023detectgpt',\n    'shi_2024_minkprob': 'shi2024minkprob',\n    'alemohammad_2024_mad': 'alemohammad2024mad',\n    'xie_2023_doremi': 'xie2023doremi',\n    'xie_2023_dsir': 'xie2023dsir',\n    'ye_2025_data_mixing_laws': 'ye2025mixing',\n    'chen_2025_aioli': 'chen2025aioli',\n    'yang_2026_data_mixing_agent': 'yang2026mixing',\n    'he_2024_softdedup': 'he2024softdedup',\n    'sow_2025_dynamic_reweighting': 'sow2025dynamic',\n    'kuo_2024_data_weighting': 'kuo2024weighting',\n    'kimura_2024_iw_survey': 'kimura2024iw',\n    'penedo_2024_fineweb': 'penedo2024fineweb',\n    'yang_2025_qwen3': 'yang2025qwen3',\n}\n\nfor fname in os.listdir('.'):\n    if not fname.endswith('.tex'):\n        continue\n    with open(fname, 'r') as f:\n        content = f.read()\n    original = content\n    for old, new in mapping.items():\n        content = content.replace(old, new)\n    if content != original:\n        with open(fname, 'w') as f:\n            f.write(content)\n        # Count replacements\n        count = sum(original.count(old) for old in mapping)\n        print(f'{fname}: {count} citation keys fixed')\n    else:\n        print(f'{fname}: no changes needed')\n\"\n",
  "description": "Fix all underscore-format citation keys to match bib format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections && python3 -c \"\nimport os, re\n\n# Citation key mapping: artifact_format -> bib_format\nmapping = {\n    'cheng_2025_contamination_survey': 'cheng2025contamination',\n    'shumailov_2024_model_collapse': 'shumailov2024model',\n    'dohmatob_2025_strong_collapse': 'dohmatob2025strong',\n    'drayson_2025_detection_collapse': 'drayson2025detection',\n    'he_2025_golden_ratio': 'he2025golden',\n    'wang_2026_survive_contamination': 'wang2026survive',\n    'vehtari_2024_psis': 'vehtari2024psis',\n    'feng_2025_beyond_collapse': 'feng2025beyond',\n    'guo_2025_escaping_collapse': 'guo2025escaping',\n    'mitchell_2023_detectgpt': 'mitchell2023detectgpt',\n    'shi_2024_minkprob': 'shi2024minkprob',\n    'alemohammad_2024_mad': 'alemohammad2024mad',\n    'xie_2023_doremi': 'xie2023doremi',\n    'xie_2023_dsir': 'xie2023dsir',\n    'ye_2025_data_mixing_laws': 'ye2025mixing',\n    'chen_2025_aioli': 'chen2025aioli',\n    'yang_2026_data_mixing_agent': 'yang2026mixing',\n    'he_2024_softdedup': 'he2024softdedup',\n    'sow_2025_dynamic_reweighting': 'sow2025dynamic',\n    'kuo_2024_data_weighting': 'kuo2024weighting',\n    'kimura_2024_iw_survey': 'kimura2024iw',\n    'penedo_2024_fineweb': 'penedo2024fineweb',\n    'yang_2025_qwen3': 'yang2025qwen3',\n}\n\nfor fname in os.listdir('.'):\n    if not fname.endswith('.tex'):\n        continue\n    with open(fname, 'r') as f:\n        content = f.read()\n    original = content\n    for old, new in mapping.items():\n        content = content.replace(old, new)\n    if content != original:\n        with open(fname, 'w') as f:\n            f.write(content)\n        # Count replacements\n        count = sum(original.count(old) for old in mapping)\n        print(f'{fname}: {count} citation keys fixed')\n    else:\n        print(f'{fname}: no changes needed')\n\"\n",
    "description": "Fix all underscore-format citation keys to match bib format"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T23:57:27.477595+00:00_

results.tex: 2 citation keys fixed
introduction.tex: 7 citation keys fixed
appendix.tex: no changes needed
abstract.tex: no changes needed
limitations.tex: 1 citation keys fixed
method.tex: 8 citation keys fixed
discussion.tex: no changes needed
conclusion.tex: no changes needed
experiments.tex: 5 citation keys fixed
related_work.tex: 21 citation keys fixed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T23:57:27.477738+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -3 introduction.tex",
  "description": "Verify introduction.tex citation near \"20--60%\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "head -3 introduction.tex",
    "description": "Verify introduction.tex citation near \"20--60%\""
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T23:57:27.477873+00:00_

Web corpora increasingly contain machine-generated text.
Recent estimates place the synthetic fraction at 20--60\% of crawled data~\citep{cheng2025contamination}, and this share grows as language models are deployed for content production at scale.
Training on such contaminated data has concrete consequences: \citet{shumailov2024model} show that recursive training on model outputs leads to irreversible quality degradation---\emph{model collapse}---and \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T23:57:27.478009+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -6 related_work.tex",
  "description": "Verify related_work.tex citation near \"20--60%\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "head -6 related_work.tex",
    "description": "Verify related_work.tex citation near \"20--60%\""
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T23:57:27.478131+00:00_

\paragraph{Synthetic Contamination and Model Collapse.}
Training on recursively generated data leads to irreversible quality degradation---\emph{model collapse}~\citep{shumailov2024model}.
\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality or diversity inevitably degrades without fresh real data, even when original training data is retained.
More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction (e.g., $1/1000$) suffices to trigger collapse, ruling out data scaling as a remedy.
\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora.
These results motivate \emph{contamination-aware} training strategies that explicitly account for synthetic provenance rather than treating all tokens equally.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T23:57:27.478249+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "sed -n '15,18p' experiments.tex",
  "description": "Check experiments.tex line 16 for held-out FineWeb and human-authored"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "sed -n '15,18p' experiments.tex",
    "description": "Check experiments.tex line 16 for held-out FineWeb and human-authored"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T23:57:27.478361+00:00_

\paragraph{Evaluation.}
We report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\sim$4M tokens) containing only human-authored text, via sliding-window evaluation (stride 1024).
All evaluations are post-hoc with a unified pipeline; training involves no inline evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-15T23:57:27.478473+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "for f in *.tex; do size=$(wc -c < \"$f\"); lines=$(wc -l < \"$f\"); if [ \"$size\" -eq 0 ] || [ \"$lines\" -eq 0 ]; then echo \"EMPTY: $f ($size bytes, $lines lines)\"; fi; done",
  "description": "Check for empty .tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "for f in *.tex; do size=$(wc -c < \"$f\"); lines=$(wc -l < \"$f\"); if [ \"$size\" -eq 0 ] || [ \"$lines\" -eq 0 ]; then echo \"EMPTY: $f ($size bytes, $lines lines)\"; fi; done",
    "description": "Check for empty .tex files"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T23:57:27.478585+00:00_

EMPTY: abstract.tex (0 bytes, 0 lines)
EMPTY: appendix.tex (0 bytes, 0 lines)
EMPTY: discussion.tex (0 bytes, 0 lines)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-15T23:57:27.478692+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -c *.tex | sort -n",
  "description": "List all .tex file sizes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -c *.tex | sort -n",
    "description": "List all .tex file sizes"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T23:57:27.478801+00:00_

    0 abstract.tex
    0 appendix.tex
    0 discussion.tex
 1324 conclusion.tex
 1576 limitations.tex
 2604 experiments.tex
 4404 results.tex
 5259 related_work.tex
 5768 introduction.tex
 9135 method.tex
30070 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-15T23:57:27.478970+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper && latexmk -pdf main.tex 2>&1 | tail -40",
  "description": "Compile LaTeX paper with latexmk",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper && latexmk -pdf main.tex 2>&1 | tail -40",
    "description": "Compile LaTeX paper with latexmk",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T23:57:27.479102+00:00_

\T1/ptm/m/n/10.95 (+20) ply the small-est $\OML/cmm/m/it/10.95 b$ \T1/ptm/m/n/1
0.95 (+20) that achieves the qual-ity
! Undefined control sequence.
l.98 \Require
              Batch scores $\{q_i\}_{i=1}^{B}$, indicators $\{r_i\}$, qualit...

? 
! Emergency stop.
l.98 
     
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Using bibtex to make bibliography file(s).
Latexmk: Summary of warnings from last run of *latex:
  Latex failed to resolve 2 reference(s)
  Latex failed to resolve 34 citation(s)
Latexmk: ====Undefined refs and citations with line #s in .tex file:
  Citation `cheng2025contamination' on page 1 undefined on input line 2
  Citation `shumailov2024model' on page 1 undefined on input line 3
  Citation `dohmatob2025strong' on page 1 undefined on input line 3
  Citation `drayson2025detection' on page 1 undefined on input line 8
  Citation `he2025golden' on page 1 undefined on input line 10
  Citation `feng2025beyond' on page 1 undefined on input line 11
  Citation `wang2026survive' on page 1 undefined on input line 15
 And 29 more --- see log file 'main.log'
Latexmk: Errors, so I did not complete making targets
Collected error summary (may duplicate other messages):
  bibtex main: Bibtex errors: See file 'main.blg'
  pdflatex: Command for 'pdflatex' gave return code 1
      Refer to 'main.log' and/or above output for details

Latexmk: Sometimes, the -f option can be used to get latexmk
  to try to force complete processing.
  But normally, you will need to correct the file(s) that caused the
  error, and then rerun latexmk.
  In some cases, it is best to clean out generated files before rerunning
  latexmk after you've corrected the files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-15T23:57:27.479273+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "offset": "12",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "offset": "12",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T23:57:27.479395+00:00_

12	\usepackage{algorithm}
13	\usepackage{algorithmic}
14	\usepackage{booktabs}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-15T23:57:27.479509+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "old_string": "\\usepackage{algorithmic}",
  "new_string": "\\usepackage{algpseudocode}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "old_string": "\\usepackage{algorithmic}",
    "new_string": "\\usepackage{algpseudocode}"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-15T23:57:27.479636+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-15T23:57:27.479750+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "rm -f main.aux main.bbl main.blg main.log main.out main.fls main.fdb_latexmk && latexmk -pdf main.tex 2>&1 | tail -40",
  "description": "Clean build artifacts and recompile",
  "timeout": "180000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "rm -f main.aux main.bbl main.blg main.log main.out main.fls main.fdb_latexmk && latexmk -pdf main.tex 2>&1 | tail -40",
    "description": "Clean build artifacts and recompile",
    "timeout": "180000"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-15T23:57:27.479889+00:00_

LaTeX Warning: Reference `alg:bstar' on page 4 undefined on input line 83.

! Undefined control sequence.
l.98 \REQUIRE
              Batch scores $\{q_i\}_{i=1}^{B}$, indicators $\{r_i\}$, qualit...

? 
! Emergency stop.
l.98 
     
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Using bibtex to make bibliography file(s).
Latexmk: Summary of warnings from last run of *latex:
  Latex failed to resolve 9 reference(s)
  Latex failed to resolve 34 citation(s)
Latexmk: ====Undefined refs and citations with line #s in .tex file:
  Citation `cheng2025contamination' on page 1 undefined on input line 2
  Citation `shumailov2024model' on page 1 undefined on input line 3
  Citation `dohmatob2025strong' on page 1 undefined on input line 3
  Citation `drayson2025detection' on page 1 undefined on input line 8
  Citation `he2025golden' on page 1 undefined on input line 10
  Citation `feng2025beyond' on page 1 undefined on input line 11
  Citation `wang2026survive' on page 1 undefined on input line 15
 And 36 more --- see log file 'main.log'
Latexmk: Errors, so I did not complete making targets
Collected error summary (may duplicate other messages):
  pdflatex: Command for 'pdflatex' gave return code 1
      Refer to 'main.log' and/or above output for details

Latexmk: Sometimes, the -f option can be used to get latexmk
  to try to force complete processing.
  But normally, you will need to correct the file(s) that caused the
  error, and then rerun latexmk.
  In some cases, it is best to clean out generated files before rerunning
  latexmk after you've corrected the files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-15T23:57:27.480046+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n 'algorithmic\\|algpseudocode' main.tex",
  "description": "Verify algorithm package change in main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n 'algorithmic\\|algpseudocode' main.tex",
    "description": "Verify algorithm package change in main.tex"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T23:57:27.480164+00:00_

13:\usepackage{algpseudocode}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-15T23:57:27.480273+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n 'Require\\|REQUIRE\\|\\\\Call\\|\\\\If{' sections/method.tex | head -10",
  "description": "Check algorithmic command style in method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n 'Require\\|REQUIRE\\|\\\\Call\\|\\\\If{' sections/method.tex | head -10",
    "description": "Check algorithmic command style in method.tex"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-15T23:57:27.480385+00:00_

98:\REQUIRE Batch scores $\{q_i\}_{i=1}^{B}$, indicators $\{r_i\}$, quality threshold~$\tau$, ESS floor~$n_{\min}$, search bound~$b_{\max}$, tolerance~$\varepsilon$

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-15T23:57:27.480525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex",
  "offset": "94",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex",
    "offset": "94",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-15T23:57:27.480656+00:00_

94	\begin{algorithm}[t]
95	\caption{Per-batch adaptive $b^{*}$ selection}
96	\label{alg:bstar}
97	\begin{algorithmic}[1]
98	\REQUIRE Batch scores $\{q_i\}_{i=1}^{B}$, indicators $\{r_i\}$, quality threshold~$\tau$, ESS floor~$n_{\min}$, search bound~$b_{\max}$, tolerance~$\varepsilon$
99	\ENSURE Optimal exponent $b^{*}$
100	\IF{$\alpha_{\mathrm{eff}}(0) \geq \tau$}
101	  \STATE \textbf{return} $0$ \COMMENT{clean batch}
102	\ENDIF
103	\STATE $b_\tau \gets \textsc{Bisect}(\alpha_{\mathrm{eff}}(\cdot){=}\tau,\; [0, b_{\max}],\; \varepsilon)$
104	\IF{$\mathrm{ESS}(b_\tau) \geq n_{\min}$}
105	  \STATE \textbf{return} $b_\tau$ \COMMENT{$\alpha_{\mathrm{eff}}$-binding}
106	\ELSE
107	  \STATE $b_{\mathrm{ESS}} \gets \textsc{Bisect}(\mathrm{ESS}(\cdot){=}n_{\min},\; [0, b_{\max}],\; \varepsilon)$
108	  \STATE \textbf{return} $b_{\mathrm{ESS}}$ \COMMENT{ESS-binding}
109	\ENDIF
110	\end{algorithmic}
111	\end{algorithm}
112	
113	\paragraph{Implementation.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-15T23:57:27.480865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "offset": "12",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "offset": "12",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-15T23:57:27.481000+00:00_

12	\usepackage{algorithm}
13	\usepackage{algpseudocode}
14	\usepackage{booktabs}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-15T23:57:27.481125+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "old_string": "\\usepackage{algpseudocode}",
  "new_string": "\\usepackage{algorithmic}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "old_string": "\\usepackage{algpseudocode}",
    "new_string": "\\usepackage{algorithmic}"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T23:57:27.481255+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-15T23:57:27.481368+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "rm -f main.aux main.bbl main.blg main.log main.out main.fls main.fdb_latexmk && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "Clean compile with pdflatex nonstopmode",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "rm -f main.aux main.bbl main.blg main.log main.out main.fls main.fdb_latexmk && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
    "description": "Clean compile with pdflatex nonstopmode",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-15T23:57:27.481488+00:00_

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `main.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr1
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb
8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (6 pages, 250883 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-15T23:57:27.481640+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "bibtex main 2>&1 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Warning|Error|Output written\" | tail -20 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Warning|Error|Output written\" | tail -20",
  "description": "Run bibtex and two more pdflatex passes",
  "timeout": "180000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "bibtex main 2>&1 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Warning|Error|Output written\" | tail -20 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Warning|Error|Output written\" | tail -20",
    "description": "Run bibtex and two more pdflatex passes",
    "timeout": "180000"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-15T23:57:27.481767+00:00_

Exit code 2
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Illegal, another \bibstyle command---line 542 of file main.aux
 : \bibstyle
 :          {acl_natbib}
I'm skipping whatever remains of this command
Database file #1: references.bib
(There was 1 error message)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-15T23:57:27.481916+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c 'bibstyle' main.aux",
  "description": "Count bibstyle entries in aux"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c 'bibstyle' main.aux",
    "description": "Count bibstyle entries in aux"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-15T23:57:27.482034+00:00_

2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-15T23:57:27.482145+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n 'bibliographystyle\\|bibliography' main.tex",
  "description": "Check bibliography commands in main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n 'bibliographystyle\\|bibliography' main.tex",
    "description": "Check bibliography commands in main.tex"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-15T23:57:27.482257+00:00_

72:\bibliography{references}
73:\bibliographystyle{acl_natbib}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-15T23:57:27.482365+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n 'bibliographystyle' sections/*.tex 2>/dev/null; grep -rn 'bibliographystyle' acl.sty 2>/dev/null | head -5",
  "description": "Find duplicate bibliographystyle sources"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n 'bibliographystyle' sections/*.tex 2>/dev/null; grep -rn 'bibliographystyle' acl.sty 2>/dev/null | head -5",
    "description": "Find duplicate bibliographystyle sources"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-15T23:57:27.482472+00:00_

195:\bibliographystyle{acl_natbib}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-15T23:57:27.482604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "offset": "70",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "offset": "70",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-15T23:57:27.482718+00:00_

70	\input{sections/limitations}
71	
72	\bibliography{references}
73	\bibliographystyle{acl_natbib}
74	
75	\appendix
76	\input{sections/appendix}
77	
78	\end{document}
79	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-15T23:57:27.482826+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliography{references}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "new_string": "\\bibliography{references}"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-15T23:57:27.482962+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-15T23:57:27.483074+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
  "offset": "70",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/main.tex",
    "offset": "70",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-15T23:57:27.483195+00:00_

70	\input{sections/limitations}
71	
72	\bibliography{references}
73	
74	\appendix
75	\input{sections/appendix}
76	
77	\end{document}
78	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-15T23:57:27.483330+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "rm -f main.aux main.bbl main.blg main.log main.out main.fls main.fdb_latexmk && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && bibtex main 2>&1 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "Full clean compile cycle: pdflatex + bibtex + pdflatex x2",
  "timeout": "180000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "rm -f main.aux main.bbl main.blg main.log main.out main.fls main.fdb_latexmk && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && bibtex main 2>&1 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
    "description": "Full clean compile cycle: pdflatex + bibtex + pdflatex x2",
    "timeout": "180000"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-15T23:57:27.483451+00:00_

8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (6 pages, 250883 bytes).
Transcript written on main.log.
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (7 pages, 264117 bytes).
Transcript written on main.log.
8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (7 pages, 269032 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-15T23:57:27.483589+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"Warning|Error|undefined\" main.log | grep -v \"rerunfilecheck\\|rerun\\|Font\\|float\\|may have changed\" | head -20",
  "description": "Check for remaining warnings/errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"Warning|Error|undefined\" main.log | grep -v \"rerunfilecheck\\|rerun\\|Font\\|float\\|may have changed\" | head -20",
    "description": "Check for remaining warnings/errors"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-15T23:57:27.483705+00:00_

LaTeX Warning: Reference `app:proofs' on page 3 undefined on input line 54.
LaTeX Warning: Reference `fig:dual_constraint' on page 4 undefined on input lin
LaTeX Warning: Reference `app:grid' on page 5 undefined on input line 7.
LaTeX Warning: There were undefined references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-15T23:57:27.483882+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -c sections/*.tex | sort -n",
  "description": "Final file sizes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -c sections/*.tex | sort -n",
    "description": "Final file sizes"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-15T23:57:27.484037+00:00_

    0 sections/abstract.tex
    0 sections/appendix.tex
    0 sections/discussion.tex
 1324 sections/conclusion.tex
 1576 sections/limitations.tex
 2604 sections/experiments.tex
 4404 sections/results.tex
 5259 sections/related_work.tex
 5768 sections/introduction.tex
 9163 sections/method.tex
30098 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 111 · 2026-05-15T23:57:27.484201+00:00_

## 汇报清单

### 同步的文件
所有 docs/paper/sections/ 的 .tex 文件已与 artifacts 版一致（前一个 Worker 已完成内容同步和 section header 剥离）。本次修复了全部 44 个引用键格式问题：

| 文件 | 字节数 | 引用键修复数 |
|------|--------|-------------|
| introduction.tex | 5,768 | 7 |
| method.tex | 9,163 | 8 |
| experiments.tex | 2,604 | 5 |
| related_work.tex | 5,259 | 21 |
| results.tex | 4,404 | 2 |
| limitations.tex | 1,576 | 1 |
| conclusion.tex | 1,324 | 0 |

### 引用修复
1. **introduction.tex:2** — `20--60\% of crawled data~\citep{cheng2025contamination}` — 已存在（来自 artifacts 同步）
2. **related_work.tex:5** — `\citet{cheng2025contamination} survey the broader contamination landscape, confirming that synthetic content now constitutes an estimated 20--60\% of web corpora` — 已存在

所有引用键从 artifact 格式（`cheng_2025_contamination_survey`）统一为 bib 格式（`cheng2025contamination`）。bib 中已有 `cheng2025contamination` 条目（references.bib:118），无需添加。

### experiments.tex Evaluation 段落内容
第 16 行：`We report held-out perplexity (PPL) on a held-out subset of FineWeb (67.8K documents, $\sim$4M tokens) containing only human-authored text`  — "held-out FineWeb" 和 "human-authored" 均存在。

### 编译结果
**成功**。7 页，269KB PDF。  
- 修复了 `\bibliographystyle` 重复（acl.sty 已提供，main.tex 中的重复已移除）  
- 3 个 undefined ref warnings（`app:proofs`, `fig:dual_constraint`, `app:grid`）— 指向尚未创建的 appendix/figure，非致命

### 空文件
- `abstract.tex` (0 bytes)
- `appendix.tex` (0 bytes)
- `discussion.tex` (0 bytes)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_sync_paper_and_citations_20260515T234454"
}
```

</details>

---
