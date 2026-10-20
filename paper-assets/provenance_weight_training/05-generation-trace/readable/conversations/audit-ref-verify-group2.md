# audit ref verify group2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 151
- **Recorded user turns:** 0
- **Tool calls:** 75
- **Original source:** `logs/chats/worker_audit_ref-verify-group2_20260526T101557.jsonl`
- **Structured JSON:** [`5b82892082eedebcce97.json`](../../sessions/5b/5b82892082eedebcce97.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

151 recorded events

### Tool call

_source line 1 · 2026-05-26T10:22:05.904787+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read bib and tex files",
  "subagent_type": "Explore",
  "prompt": "Read the following files and return their full contents:\n\n1. Find the .bib file(s) in /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/ (glob for *.bib recursively)\n2. Read all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/\n\nFor the bib file, I specifically need entries with these keys: xie2023doremi, xie2023dsir, chen2025aioli, kimura2024iw, mitchell2023detectgpt, shi2024minkprob, alemohammad2024mad, cheng2025contamination, ye2025mixing, yang2026mixing, penedo2024fineweb, yang2025qwen3, kuo2024weighting, bengio2009curriculum, radford2019language, brown2020language, longpre2024pretrainers, lee2022dedup\n\nReturn the full bib entries for these keys, and the full contents of all section tex files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Agent",
  "tool_args": {
    "description": "Read bib and tex files",
    "subagent_type": "Explore",
    "prompt": "Read the following files and return their full contents:\n\n1. Find the .bib file(s) in /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/ (glob for *.bib recursively)\n2. Read all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/\n\nFor the bib file, I specifically need entries with these keys: xie2023doremi, xie2023dsir, chen2025aioli, kimura2024iw, mitchell2023detectgpt, shi2024minkprob, alemohammad2024mad, cheng2025contamination, ye2025mixing, yang2026mixing, penedo2024fineweb, yang2025qwen3, kuo2024weighting, bengio2009curriculum, radford2019language, brown2020language, longpre2024pretrainers, lee2022dedup\n\nReturn the full bib entries for these keys, and the full contents of all section tex files."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-26T10:22:05.905184+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/**/*.bib"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-26T10:22:05.905365+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T10:22:05.905516+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-26T10:22:05.905641+00:00_

docs/paper/sections/checklist.tex
docs/paper/sections/experiments.tex
docs/paper/sections/abstract.tex
docs/paper/sections/method.tex
docs/paper/sections/limitations.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/related_work.tex
docs/paper/sections/discussion.tex
docs/paper/sections/results.tex
docs/paper/sections/appendix.tex
docs/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T10:22:05.905771+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-26T10:22:05.905991+00:00_

1	% References for Minimum Intervention Reweighting paper
2	% Note: entries to be verified via verify_references before final submission
3	
4	@inproceedings{dugan2024raid,
5	  title={{RAID}: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors},
6	  author={Dugan, Liam and Hwang, Alyssa and Trhl{\'\i}k, Filip and Langmore, Andrew and Ippolito, Daphne and Callison-Burch, Chris and Ets-Hokin, Garrison},
7	  booktitle={ACL},
8	  year={2024}
9	}
10	
11	@article{wang2024m4,
12	  title={{M4}: Multi-generator, Multi-domain, and Multi-lingual Black-Box Machine-Generated Text Detection},
13	  author={Wang, Yuxia and Manber, Jonibek and Shaar, Shaden and Arase, Yuki and Derczynski, Leon and Nakov, Preslav},
14	  journal={EACL},
15	  year={2024}
16	}
17	
18	@article{gunasekar2023textbooks,
19	  title={Textbooks Are All You Need},
20	  author={Gunasekar, Suriya and Zhang, Yi and Aneja, Jyoti and Mendes, Caio C{\'e}sar Teodoro and Del Giorno, Allie and Gopi, Sivakanth and Javaheripi, Mojan and Kauffmann, Piero and de Rosa, Gustavo and Saarikivi, Olli and Salim, Adil and Shah, Shital and Behl, Harkirat Singh and Wang, Xin and Bubeck, S{\'e}bastien and Eldan, Ronen and Kalai, Adam Tauman and Lee, Yin Tat and Li, Yuanzhi},
21	  journal={arXiv preprint arXiv:2306.11644},
22	  year={2023}
23	}
24	
25	@article{li2023textbooks2,
26	  title={Textbooks Are All You Need {II}: phi-1.5 Technical Report},
27	  author={Li, Yuanzhi and Bubeck, S{\'e}bastien and Eldan, Ronen and Del Giorno, Allie and Gunasekar, Suriya and Lee, Yin Tat},
28	  journal={arXiv preprint arXiv:2309.05463},
29	  year={2023}
30	}
31	
32	@inproceedings{katharopoulos2018not,
33	  title={Not All Samples Are Created Equal: Deep Learning with Importance Sampling},
34	  author={Katharopoulos, Angelos and Fleuret, Fran{\c{c}}ois},
35	  booktitle={International Conference on Machine Learning},
36	  pages={2525--2534},
37	  year={2018},
38	  organization={PMLR}
39	}
40	
41	@inproceedings{ren2018learning,
…[truncated 21226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:22:05.906169+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T10:22:05.906300+00:00_

1	As synthetic text pervades web corpora, detect-and-reweight methods that downweight likely-synthetic samples during training have emerged to prevent model collapse, yet when they actually help remains unclear.
2	We investigate this question through controlled continued-pretraining experiments (Qwen3-0.6B, 132M tokens, 5 seeds) and identify three effectiveness conditions.
3	First, detect-and-remove (D\&R) outperforms all reweighting methods in our setting; epoch-matched controls attribute over 95\% of the advantage to multi-epoch exposure on filtered data, identifying the mechanism behind D\&R's effectiveness.
4	Second, the detector must provide both sufficient discrimination \emph{and} good calibration; high-AUC detectors with poor calibration degrade performance below uniform training.
5	Third, minimum intervention, applying the smallest reweighting exponent that meets a quality floor, outperforms unconstrained weight maximization.
6	As an illustrative application of the minimum-intervention principle, we derive a dual-constrained adaptive exponent $\bstar$ that improves over uniform training at contamination ratios $\rho \geq 0.4$, reaching conventional significance after multiple-comparison correction, while requiring no per-model tuning.
7	These findings apply within our self-contamination setup at 0.6B scale; generalization to cross-model contamination and larger models remains to be established\footnote{Code and data are available at \url{https://anonymous.4open.science/r/provenance_weight_training-F72D/}.}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:22:05.906439+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T10:22:05.906572+00:00_

1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	\begin{figure*}[t]
6	\centering
7	\includegraphics[width=\textwidth]{fig1_overview}
8	\caption{Three effectiveness conditions for detect-and-reweight.
9	\textbf{(a)}~D\&R achieves the best raw perplexity (PPL); epoch-matched controls reveal that multi-epoch exposure on filtered data accounts for the bulk of the advantage (\S\ref{sec:results}).
10	\textbf{(b)}~Only detectors with both high AUC \emph{and} low ECE fall in the effective zone; comparable AUC with poor calibration degrades PPL below uniform.
11	\textbf{(c)}~Adaptive $\bstar{\approx}0.9$ operates near the grid-search optimum, while ESS-only $b{\approx}3.5$ falls in the degradation zone.}
12	\label{fig:overview}
13	\end{figure*}
14	
15	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
16	What mechanism drives D\&R's strong performance, and how does it compare to soft reweighting under controlled conditions?
17	What detector properties are necessary for effective reweighting?
18	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
19	
20	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 5 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters (\S\ref{sec:limitations} discusses scope).
21	To ground the analysis of exponent selectio
…[truncated 1851 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T10:22:05.906723+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T10:22:05.906880+00:00_

1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality inevitably degrades without fresh real data.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger collapse, ruling out data scaling as a remedy.
5	\citet{cheng2025contamination} confirm that synthetic content now constitutes an estimated 20--60\% of web corpora, though accumulating real data avoids divergence~\citep{kazdan2025collapse} and even minimal curation suffices~\citep{amin2025escaping}.
6	Not all synthetic data is harmful: the Phi series~\citep{gunasekar2023textbooks,li2023textbooks2} demonstrates that curated synthetic data can improve training efficiency, but this assumes intentional generation with quality control, unlike the uncontrolled web contamination we address.
7	
8	\paragraph{Detection, Filtering, and Data Reweighting.}
9	Continuous-score detectors---probability curvature~\citep{mitchell2023detectgpt}, cross-perplexity ratios~\citep{hans2024binoculars}, low-probability token statistics~\citep{shi2024minkprob}---enable document-level weighting~\citep{wu2025survey}.
10	Data composition is optimized via perplexity filtering~\citep{wenzek2020ccnet}, domain-level importance sampling~\citep{xie2023doremi,xie2023dsir,grangier2025crisp,ye2025mixing}, instance-level strategies~\citep{bengio2009curriculum,mindermann2022prioritized,sow2025dynamic,engstrom2024dsdm}, and deduplication~\citep{abbas2023semdedup}; see \citet{albalak2024survey}.
11	None targets synthetic provenance; moreover, classifier-based quality scores may capture stylistic similarity rather than intrinsic quality~\citep{naitsaada2025illusion}.
12	Most directly related, \citet{drayson2025detection} propose $w_j = (1{-
…[truncated 2560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T10:22:05.907058+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T10:22:05.907206+00:00_

1	\begin{figure}[t]
2	\centering
3	\includegraphics[width=\columnwidth]{dr_pipeline_concept}
4	\caption{Overview of the detect-and-reweight pipeline. A TF-IDF + LR detector assigns contamination scores $q(x)$; a dual-constrained optimizer selects $b$ to satisfy quality-floor and effective-sample-size constraints; the resulting weights $w(x) = (1{-}q(x))^{b}$ are applied during training.}
5	\label{fig:pipeline}
6	\end{figure}
7	
8	Figure~\ref{fig:pipeline} illustrates the pipeline. Let $\mathcal{D}$ denote a pretraining corpus with unknown synthetic contamination ratio $\rho$~\citep{cheng2025contamination}.
9	A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
10	Rather than selecting $b$ via grid search, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
11	
12	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
13	
14	\paragraph{Quality floor.}
15	The \emph{effective authenticity} $\aeff(b) = \sum_i w_i(b)(1{-}q_i) / \sum_i w_i(b)$ measures the weighted mean detector confidence that samples are real.
16	We require $\aeff(b) \geq \tau$, yielding a lower bound $b_\tau$ on the exponent, motivated by convergence theory under contamination~\citep{wang2026survive}.
17	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.79$ (Appendix~\ref{app:alpha_validation}); limitations are discussed in \S\ref{sec:discussion}.
18	
19	\paragraph{Stability ceiling.}
20	Kish's effective sample size $\mathrm{ESS}(b) = (\sum_i w_i)^2 / \sum_i w_i^2$~\citep{kish1965survey} decreases monotonically in $b$ (Appendix~\ref{app:proofs}).
21	We require $\mathrm{ESS}(b) \geq \nmin$, yielding an upper bound $\bess$.
22	
23	\paragraph{Adaptive $\bstar$.}
24	Since $\aeff$ i
…[truncated 1925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T10:22:05.907356+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T10:22:05.907491+00:00_

1	\paragraph{Training Data.}
2	We sample a 132M-token subset of FineWeb~\citep{penedo2024fineweb} as the real-data source, comparable to typical domain-adaptive continued pretraining budgets~\citep{gururangan2020dont}.
3	To simulate web-scale synthetic contamination, we generate continuations with Qwen3-0.6B~\citep{yang2025qwen3}, the same architecture used for continued pretraining, and inject them at token-level ratio $\rho = 0.4$ via uniform random mixing.\footnote{$\rho$ denotes the token-level contamination ratio. Because synthetic documents are shorter on average (304 vs.\ 560 words), the document-level synthetic fraction is 55.6\% at $\rho{=}0.4$.}
4	This self-contamination design means generator and trainee share the same distribution, providing a controlled testbed with known ground-truth labels but limiting ecological validity; cross-model transfer results (Appendix~\ref{app:cross_model}) are mixed, and we discuss implications for detection difficulty in \S\ref{sec:limitations}.
5	
6	\paragraph{Detector.}
7	We train a TF-IDF + Logistic Regression classifier on a held-out labeled split (AUC\,=\,0.94, calibrated ECE\,=\,0.048 after temperature scaling with $T{=}0.204$).
8	The resulting $q$-scores have mean 0.60, standard deviation 0.37, and median 0.71, with 46.3\% of samples in the uncertain range $[0.2, 0.8]$.
9	We use this lightweight detector rather than neural alternatives (e.g., ModernBERT at AUC\,${\geq}$\,0.98 in \citealt{drayson2025detection}) to test whether score \emph{calibration} may matter as much as raw discrimination for reweighting.
10	To evaluate detector sensitivity, we additionally test two generative baselines: a GPT-2-based perplexity scorer (AUC\,=\,0.91) and an N-gram language model perplexity scorer (AUC\,=\,0.73); results are reported in \S\ref{sec:robustness} (implementation details in Appendix~\ref{app:detector_details}).
11	
12	\paragraph{Training.}
13	Table~\ref{tab:config} summarizes the training configuration.
14	We use $B{=}4
…[truncated 2489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T10:22:05.907641+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T10:22:05.907811+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\setlength{\tabcolsep}{3pt}
5	\resizebox{\columnwidth}{!}{%
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	\textbf{Method} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean} \\
9	\midrule
10	Uniform                & 17.694 & 17.686 & 17.702 & 17.697 $\pm$ .008 \\
11	Adaptive $\bstar$ (ours) & \textbf{17.680} & \textbf{17.666} & \textbf{17.677} & \textbf{17.674} $\pm$ .006 \\
12	ESS-only               & 17.730 & 17.720 & 17.760 & 17.737 $\pm$ .021 \\
13	Random $\mathcal{U}(0,2)$ & 17.830 & 17.800 & 17.777 & 17.802 $\pm$ .027 \\
14	Permuted $q$-scores  & 17.919 & --     & --     & 17.919 \\
15	\bottomrule
16	\end{tabular}}
17	\caption{Main comparison: held-out PPL ($\downarrow$) at $\rho{=}0.4$, 1 content epoch.
18	Adaptive and Uniform: 5-seed means (seeds 42, 123, 456, 789, 234); ESS-only and Random: 3-seed means (seeds 42, 123, 456); Permuted: single seed (42).
19	Adaptive uses $\tau{=}0.7$, $\nmin{=}2$.
20	Permuted randomly shuffles $q$-scores across samples, destroying provenance signal while preserving weight non-uniformity ($\Delta{=}{+}0.225$).}
21	\label{tab:main}
22	\end{table}
23	
24	\subsection{Main Results}
25	\label{sec:main-results}
26	
27	Table~\ref{tab:main} reports held-out perplexity at $\rho = 0.4$ across five seeds.
28	Continued pretraining reduces PPL from 22.970 to the 17.3--17.8 range; method comparisons operate within a narrow residual.
29	
30	Adaptive $\bstar$ achieves 5-seed mean PPL 17.674, compared to 17.697 for uniform ($\Delta{=}{-}0.023$, directionally consistent across all seeds) and 17.620 for grid $b{=}0.3$ (3-seed mean, post-hoc oracle; gap $+$0.054; Table~\ref{tab:aux}).
31	A paired $t$-test yields $t(4){=}{-}8.21$, $p{=}0.0012$; after Bonferroni--Holm correction for nine family-wise comparisons, $p_{\mathrm{BH}}{=}0.011$, reaching conventional significance at $\alpha{=}0.05$.
32	The engineering benefit is eliminating $b$ grid search (nine full training runs~\citep{dray
…[truncated 13772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T10:22:05.908022+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T10:22:05.908164+00:00_

1	\paragraph{D\&R as the strongest strategy.}
2	D\&R outperforms all reweighting methods by $0.35$--$0.42$ PPL (Table~\ref{tab:epoch_match}), but epoch-matched controls attribute ${>}$95\% of this advantage to multi-epoch exposure on filtered data rather than superior per-token learning.
3	This benefit was invisible in \citet{drayson2025detection}, where from-scratch pretraining rarely completes one epoch; in continued pretraining, it becomes the dominant factor.
4	
5	\paragraph{When uniform beats reweighting.}
6	Table~\ref{tab:decision} summarizes three prerequisites for effective soft reweighting: (i)~sufficient detector discrimination \emph{and} calibration (AUC\,$\geq$\,0.9, ECE\,$\leq$\,0.05; \S\ref{sec:robustness}); (ii)~contamination $\rho \geq 0.4$, below which the method degrades ($+$0.046 at $\rho{=}0.2$; Appendix~\ref{app:rho02}) with a sharp transition in $[0.3, 0.4]$ (Figure~\ref{fig:delta_vs_rho}, Appendix~\ref{app:rho03}); (iii)~generator--trainee mismatch (at 1.7B the benefit diminishes to $\Delta{=}{-}0.013$ with OOD mixed).
7	When any condition is violated, uniform is the safer default.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\setlength{\tabcolsep}{3pt}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}lcll@{}}
15	\toprule
16	\textbf{Condition} & \textbf{Observed?} & \textbf{Evidence} & \textbf{$\Delta$ PPL} \\
17	\midrule
18	Detector AUC $\geq 0.9$ & Yes & N-gram (0.73) degrades & $+$0.129 \\
19	Detector ECE $\leq 0.05$ & Yes & GPT-2 (0.131) degrades & $+$0.098 \\
20	Contamination $\rho \geq 0.4$ & Yes & $\rho{=}0.2$ degrades & $+$0.046 \\
21	Generator $\neq$ trainee & Tentative & 1.7B: $\Delta{=}{-}0.013$, OOD mixed & -- \\
22	\bottomrule
23	\end{tabular}}
24	\caption{Decision summary for practitioners.
25	$\Delta$ values are relative to uniform (positive = worse).
26	When any observed condition is violated, uniform is the safer default.}
27	\label{tab:decision}
28	\end{table}
29	
30	\paragraph{Effect size and downstream impact.}
31
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:22:05.908318+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T10:22:05.908443+00:00_

1	\begin{itemize}[nosep,leftmargin=*]
2	\item \textbf{Scope.}
3	All experiments use Qwen3 (0.6B and 1.7B) under self-contamination with 132--200M tokens of continued pretraining.
4	Generalization to other architectures, full pretraining scale ($>$100B tokens), or realistic multi-source web contamination, where generator-corpus distribution mismatch may reduce detector accuracy, remains untested.
5	
6	\item \textbf{Detector coverage.}
7	Only three detectors from two families (discriminative TF-IDF+LR and generative perplexity scorers) were evaluated; fine-tuned neural classifiers (e.g., ModernBERT) and zero-shot methods (e.g., DetectGPT, Binoculars) remain untested, so the AUC/ECE thresholds reported here may shift with broader detector coverage.
8	
9	\item \textbf{Evaluation scope.}
10	Our primary metric is held-out perplexity; downstream accuracy is unchanged across conditions (Appendix~\ref{app:downstream}), so the practical benefit at 0.6B scale is limited to distributional quality rather than task performance.
11	\end{itemize}
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T10:22:05.908572+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T10:22:05.908686+00:00_

1	We identify three effectiveness conditions for detect-and-reweight: (i)~D\&R is the strongest method in our setting, with multi-epoch exposure on filtered data accounting for ${>}$95\% of its advantage over reweighting; (ii)~detector calibration alongside discrimination, as high-AUC detectors with poor calibration degrade PPL below uniform; and (iii)~minimum intervention over unconstrained maximization, supported by the ESS-only ablation and the fixed-$b$ grid curve (Figure~\ref{fig:grid_b_trend}).
2	A dual-constrained adaptive $\bstar$ implementing these principles improves over uniform training at $\rho \geq 0.4$ without per-model tuning (Table~\ref{tab:decision}), though without measurable downstream gains at 0.6B scale.
3	Whether these conditions hold at full pretraining scale ($>$100B tokens), where contamination ratios are lower but corpora are harder to curate, is the central open question; a second priority is extending the detector--calibration axis to neural classifiers whose ECE profiles differ qualitatively from the TF-IDF family tested here.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T10:22:05.908820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T10:22:05.909083+00:00_

1	\section{Proofs}
2	\label{app:proofs}
3	
4	\begin{proposition}[$\alpha_{\mathrm{eff}}$ monotonicity]
5	\label{prop:monotone}
6	$\alpha_{\mathrm{eff}}(b)$ is non-decreasing in $b$, and strictly increasing whenever the batch contains at least two samples with distinct $q$-values.
7	\end{proposition}
8	
9	\begin{proof}[Proof of Proposition~\ref{prop:monotone}]
10	Let $w_i(b) = (1 - q_i)^b$, $W(b) = \sum_{j=1}^B w_j(b)$, and $\pi_i(b) = w_i(b) / W(b)$.
11	Then
12	\begin{equation*}
13	  \alpha_{\mathrm{eff}}(b) = \sum_{i=1}^{B} \pi_i(b)\, (1 - q_i).
14	\end{equation*}
15	Taking the derivative with respect to $b$:
16	\begin{align*}
17	  \frac{d\pi_i}{db}
18	  &= \pi_i \!\left(\frac{d \ln w_i}{db} - \frac{d \ln W}{db}\right) \\
19	  &= \pi_i \!\left(\ln(1{-}q_i) - \textstyle\sum_j \pi_j \ln(1{-}q_j)\right).
20	\end{align*}
21	Substituting,
22	\begin{align*}
23	  \frac{d\alpha_{\mathrm{eff}}}{db}
24	  &= \sum_i (1{-}q_i)\, \pi_i \!\left(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\right) \\
25	  &= \mathrm{Cov}_{\pi}\!\bigl(1{-}q_i,\, \ln(1{-}q_i)\bigr).
26	\end{align*}
27	Since $(1{-}q_i)$ and $\ln(1{-}q_i)$ are both increasing functions of $(1{-}q_i)$, they are positively associated, so the covariance is non-negative.
28	\end{proof}
29	
30	\begin{proposition}[ESS monotonicity]
31	\label{prop:ess_mono}
32	$\mathrm{ESS}(b)$ is non-increasing in $b$, and strictly decreasing whenever the batch contains at least two samples with distinct $q$-values.
33	\end{proposition}
34	
35	\begin{proof}
36	Write $\mathrm{ESS}(b) = 1 / \sum_i \pi_i(b)^2$, where $\pi_i(b) = w_i(b) / W(b)$.
37	The denominator $\sum_i \pi_i^2$ is the Herfindahl index $H$.
38	Differentiating $H$ with respect to $b$:
39	\begin{equation*}
40	  \frac{dH}{db} = 2 \sum_i \pi_i^2 \bigl(\ln(1{-}q_i) - \mathbb{E}_{\pi}[\ln(1{-}q)]\bigr).
41	\end{equation*}
42	Since $\pi_i \propto (1{-}q_i)^b$, larger $\pi_i$ implies larger $\ln(1{-}q_i)$; the $\pi^2$-weighted sum assigns greater mass to terms where $\ln(1{-}q_i) > \ma
…[truncated 28103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T10:22:05.909240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T10:22:05.909402+00:00_

1	% Responsible NLP Research Checklist
2	% https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	\subsection*{A. For Every Submission}
7	
8	\begin{itemize}[nosep,leftmargin=*]
9	\item[\checkmark] \textbf{A1.} Did you describe the limitations of your work?
10	\textit{Yes, \S\ref{sec:limitations} discusses scale, contamination range, detector coverage, threshold, evaluation, and effect size limitations.}
11	
12	\item[\checkmark] \textbf{A2.} Did you discuss any potential risks of your work?
13	\textit{Yes. The method assumes a pre-trained detector is available; deploying it with a poorly calibrated detector could degrade training quality (discussed in \S\ref{sec:limitations}, Detector coverage). The method does not generate new content or enable harmful uses beyond standard language model pretraining.}
14	\end{itemize}
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\checkmark] \textbf{B1.} Did you cite the creators of artifacts you used?
20	\textit{Yes. FineWeb~\citep{penedo2024fineweb}, Qwen3~\citep{yang2025qwen3}, and all baseline methods are cited in \S\ref{sec:experiments} and \S\ref{sec:related}.}
21	
22	\item[\checkmark] \textbf{B2.} Did you discuss the license or terms for use and/or distribution of any artifacts?
23	\textit{FineWeb is released under Apache-2.0; Qwen3 under Apache-2.0. Our code and data will be released upon acceptance.}
24	
25	\item[\checkmark] \textbf{B3.} Did you discuss if your use of existing artifacts was consistent with their intended use?
26	\textit{Yes. FineWeb is intended for language model training; we use it as a pretraining corpus. Qwen3 is used for both continued pretraining and synthetic data generation, consistent with its general-purpose design.}
27	
28	\item[\checkmark] \textbf{B4.} Did you discuss the steps taken to check whether the data contains information that names or uniquely identifies individ
…[truncated 3211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T10:22:05.909592+00:00_

Perfect! I have successfully retrieved all the requested files. Let me now provide you with a comprehensive summary of the findings.

## Summary

I have successfully located and read all requested files:

### 1. Bib File Location
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib`

### 2. Bibliography Entries (All Found)

All 18 requested bibliography entries are present in the references.bib file with full citations:

- **xie2023doremi** (lines 146-151): DoReMi - Optimizing Data Mixtures Speeds Up Language Model Pretraining
- **xie2023dsir** (lines 153-158): Data Selection for Language Models via Importance Resampling
- **chen2025aioli** (lines 160-165): Aioli - A Unified Optimization Framework for Language Model Data Mixing
- **kimura2024iw** (lines 167-172): A Short Survey on Importance Weighting for Machine Learning
- **mitchell2023detectgpt** (lines 174-179): DetectGPT - Zero-Shot Machine-Generated Text Detection using Probability Curvature
- **shi2024minkprob** (lines 181-186): Detecting Pretraining Data from Large Language Models
- **alemohammad2024mad** (lines 188-193): Self-Consuming Generative Models Go MAD
- **cheng2025contamination** (lines 195-200): A Survey on Data Contamination for Large Language Models
- **ye2025mixing** (lines 202-207): Data Mixing Laws - Optimizing Data Mixtures by Predicting Language Modeling Performance
- **yang2026mixing** (lines 209-214): Data Mixing Agent - Learning to Re-weight Domains for Continual Pre-training
- **penedo2024fineweb** (lines 216-221): The FineWeb Datasets - Decanting the Web for the Finest Text Data at Scale
- **yang2025qwen3** (lines 223-228): Qwen3 Technical Report
- **kuo2024weighting** (lines 231-236): Not All LLM-Generated Data Are Equal - Rethinking Data Weighting in Text Classification
- **bengio2009curriculum** (lines 238-243): Curriculum Learning
- **radford2019language** (lines 245-250): Language Models are Unsupervised Multitas
…[truncated 1806 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T10:22:05.909745+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib",
  "offset": "145",
  "limit": "130"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib",
    "offset": "145",
    "limit": "130"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T10:22:05.909947+00:00_

145	
146	@inproceedings{xie2023doremi,
147	  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},
148	  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},
149	  booktitle={NeurIPS},
150	  year={2023}
151	}
152	
153	@inproceedings{xie2023dsir,
154	  title={Data Selection for Language Models via Importance Resampling},
155	  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
156	  booktitle={NeurIPS},
157	  year={2023}
158	}
159	
160	@inproceedings{chen2025aioli,
161	  title={Aioli: A Unified Optimization Framework for Language Model Data Mixing},
162	  author={Chen, Mayee F. and Hu, Michael Y. and Lourie, Nicholas and Cho, Kyunghyun and R{\'e}, Christopher},
163	  booktitle={ICLR},
164	  year={2025}
165	}
166	
167	@article{kimura2024iw,
168	  title={A Short Survey on Importance Weighting for Machine Learning},
169	  author={Kimura, Masanari and Hino, Hideitsu},
170	  journal={TMLR},
171	  year={2024}
172	}
173	
174	@inproceedings{mitchell2023detectgpt,
175	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
176	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
177	  booktitle={ICML},
178	  year={2023}
179	}
180	
181	@inproceedings{shi2024minkprob,
182	  title={Detecting Pretraining Data from Large Language Models},
183	  author={Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
184	  booktitle={ICLR},
185	  year={2024}
186	}
187	
188	@inproceedings{alemohammad2024mad,
189	  title={Self-Consuming Generative Models Go {MAD}},
190	  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniu
…[truncated 3319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T10:22:05.910139+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "xie2023doremi|xie2023dsir|chen2025aioli|kimura2024iw|mitchell2023detectgpt|shi2024minkprob|alemohammad2024mad|cheng2025contamination|ye2025mixing|yang2026mixing|penedo2024fineweb|yang2025qwen3|kuo2024weighting|bengio2009curriculum|radford2019language|brown2020language|longpre2024pretrainers|lee2022dedup",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections",
  "output_mode": "content",
  "-C": "1",
  "head_limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Grep",
  "tool_args": {
    "pattern": "xie2023doremi|xie2023dsir|chen2025aioli|kimura2024iw|mitchell2023detectgpt|shi2024minkprob|alemohammad2024mad|cheng2025contamination|ye2025mixing|yang2026mixing|penedo2024fineweb|yang2025qwen3|kuo2024weighting|bengio2009curriculum|radford2019language|brown2020language|longpre2024pretrainers|lee2022dedup",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections",
    "output_mode": "content",
    "-C": "1",
    "head_limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-26T10:22:05.910304+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-2-Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
docs/paper/sections/related_work.tex:3:\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality inevitably degrades without fresh real data.
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-4-More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger collapse, ruling out data scaling as a remedy.
docs/paper/sections/related_work.tex:5:\citet{cheng2025contamination} confirm that synthetic content now constitutes an estimated 20--60\% of web corpora, though accumulating real data avoids divergence~\citep{kazdan2025collapse} and even minimal curation suffices~\citep{amin2025escaping}.
docs/paper/sections/related_work.tex-6-Not all synthetic data is harmful: the Phi series~\citep{gunasekar2023textbooks,li2023textbooks2} demonstrates that curated synthetic data can improve training efficiency, but this assumes intentional generation with quality control, unlike the uncontrolled web contamination we address.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex-8-\paragraph{Detection, Filtering, and Data Reweighting.}
docs/paper/sections/related_work.tex:9:Continuous-score detectors---probability curvature~\citep{mitchell2023detectgpt}, cross-perplexity ratios~\citep{hans2024binoculars}, low-probability token statistics~\citep{shi2024minkprob}---enable document-level weighting~\citep{wu2025survey}.
docs/paper/sections/related_work.tex:10:Data composition is optimized via perplexity filtering~\citep{wenzek2020ccnet}, domain-level importance sampling~\citep{xie2
…[truncated 5393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T10:22:05.910482+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "chen2025aioli|kimura2024iw|yang2026mixing|kuo2024weighting|radford2019language|brown2020language|longpre2024pretrainers|lee2022dedup",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections",
  "output_mode": "content",
  "-C": "1",
  "head_limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Grep",
  "tool_args": {
    "pattern": "chen2025aioli|kimura2024iw|yang2026mixing|kuo2024weighting|radford2019language|brown2020language|longpre2024pretrainers|lee2022dedup",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections",
    "output_mode": "content",
    "-C": "1",
    "head_limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T10:22:05.910609+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T10:22:05.910749+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "chen2025aioli|kimura2024iw|yang2026mixing|kuo2024weighting|radford2019language|brown2020language|longpre2024pretrainers|lee2022dedup",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
  "output_mode": "content",
  "-C": "1",
  "head_limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Grep",
  "tool_args": {
    "pattern": "chen2025aioli|kimura2024iw|yang2026mixing|kuo2024weighting|radford2019language|brown2020language|longpre2024pretrainers|lee2022dedup",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper",
    "output_mode": "content",
    "-C": "1",
    "head_limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T10:22:05.910951+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib-159-
docs/paper/references.bib:160:@inproceedings{chen2025aioli,
docs/paper/references.bib-161-  title={Aioli: A Unified Optimization Framework for Language Model Data Mixing},
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib-166-
docs/paper/references.bib:167:@article{kimura2024iw,
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib-168-  title={A Short Survey on Importance Weighting for Machine Learning},
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib-208-
docs/paper/references.bib:209:@inproceedings{yang2026mixing,
docs/paper/references.bib-210-  title={Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training},
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib-230-
docs/paper/references.bib:231:@article{kuo2024weighting,
docs/paper/references.bib-232-  title={Not All {LLM}-Generated Data Are Equal: Rethinking Data Weighting in Text Classification},
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib-244-
docs/paper/references.bib:245:@article{radford2019language,
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib-246-  title={Language Models are Unsupervised Multitask Learners},
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib-251-
docs/paper/references.bib:252:@inproceedings{brown2020language,
/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/references.bib-253-  title={Language Models are Few-Shot Learners},
--
/home/ubuntu/.agent-ml-research-idea_gen_050
…[truncated 648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T10:22:05.911128+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
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

_source line 40 · 2026-05-26T10:22:05.911253+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:22:05.911402+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify entries 20-23",
  "prompt": "Verify these 4 bibliography entries by searching the web. For each, confirm: (1) paper exists, (2) exact title, (3) author names/spelling, (4) year, (5) venue, (6) arXiv ID if applicable.\n\nEntry 1: xie2023doremi\n- Bib title: \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\"\n- Bib authors: Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei\n- Bib venue: NeurIPS 2023\n\nEntry 2: xie2023dsir\n- Bib title: \"Data Selection for Language Models via Importance Resampling\"\n- Bib authors: Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\n- Bib venue: NeurIPS 2023\n\nEntry 3: chen2025aioli\n- Bib title: \"Aioli: A Unified Optimization Framework for Language Model Data Mixing\"\n- Bib authors: Chen, Mayee F. and Hu, Michael Y. and Lourie, Nicholas and Cho, Kyunghyun and Ré, Christopher\n- Bib venue: ICLR 2025\n\nEntry 4: kimura2024iw\n- Bib title: \"A Short Survey on Importance Weighting for Machine Learning\"\n- Bib authors: Kimura, Masanari and Hino, Hideitsu\n- Bib venue: TMLR 2024\n\nSearch for each on Semantic Scholar, Google Scholar, or arXiv. Report exact findings for each field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify entries 20-23",
    "prompt": "Verify these 4 bibliography entries by searching the web. For each, confirm: (1) paper exists, (2) exact title, (3) author names/spelling, (4) year, (5) venue, (6) arXiv ID if applicable.\n\nEntry 1: xie2023doremi\n- Bib title: \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\"\n- Bib authors: Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei\n- Bib venue: NeurIPS 2023\n\nEntry 2: xie2023dsir\n- Bib title: \"Data Selection for Language Models via Importance Resampling\"\n- Bib authors: Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\n- Bib venue: NeurIPS 2023\n\nEntry 3: chen2025aioli\n- Bib title: \"Aioli: A Unified Optimization Framework for Language Model Data Mixing\"\n- Bib authors: Chen, Mayee F. and Hu, Michael Y. and Lourie, Nicholas and Cho, Kyunghyun and Ré, Christopher\n- Bib venue: ICLR 2025\n\nEntry 4: kimura2024iw\n- Bib title: \"A Short Survey on Importance Weighting for Machine Learning\"\n- Bib authors: Kimura, Masanari and Hino, Hideitsu\n- Bib venue: TMLR 2024\n\nSearch for each on Semantic Scholar, Google Scholar, or arXiv. Report exact findings for each field."
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:22:05.911596+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
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

_source line 43 · 2026-05-26T10:22:05.911719+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:22:05.911834+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining Xie NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining Xie NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T10:22:05.911977+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Data Selection for Language Models via Importance Resampling DSIR Xie NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Data Selection for Language Models via Importance Resampling DSIR Xie NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T10:22:05.912101+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Aioli Unified Optimization Framework Language Model Data Mixing Chen ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Aioli Unified Optimization Framework Language Model Data Mixing Chen ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T10:22:05.912218+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Short Survey Importance Weighting Machine Learning Kimura Hino TMLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Short Survey Importance Weighting Machine Learning Kimura Hino TMLR"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-26T10:22:05.912337+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify entries 24-27",
  "prompt": "Verify these 4 bibliography entries by searching the web. For each, confirm: (1) paper exists, (2) exact title, (3) author names/spelling, (4) year, (5) venue, (6) arXiv ID if applicable.\n\nEntry 1: mitchell2023detectgpt\n- Bib title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n- Bib authors: Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea\n- Bib venue: ICML 2023\n\nEntry 2: shi2024minkprob\n- Bib title: \"Detecting Pretraining Data from Large Language Models\"\n- Bib authors: Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke\n- Bib venue: ICLR 2024\n\nEntry 3: alemohammad2024mad\n- Bib title: \"Self-Consuming Generative Models Go MAD\"\n- Bib authors: Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.\n- Bib venue: ICLR 2024\n\nEntry 4: cheng2025contamination\n- Bib title: \"A Survey on Data Contamination for Large Language Models\"\n- Bib authors: Cheng, Yuxing and Chang, Yi and Wu, Yuan\n- Bib venue: arXiv:2502.14425, 2025\n\nSearch for each on Semantic Scholar, Google Scholar, or arXiv. Report exact findings for each field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify entries 24-27",
    "prompt": "Verify these 4 bibliography entries by searching the web. For each, confirm: (1) paper exists, (2) exact title, (3) author names/spelling, (4) year, (5) venue, (6) arXiv ID if applicable.\n\nEntry 1: mitchell2023detectgpt\n- Bib title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n- Bib authors: Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea\n- Bib venue: ICML 2023\n\nEntry 2: shi2024minkprob\n- Bib title: \"Detecting Pretraining Data from Large Language Models\"\n- Bib authors: Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke\n- Bib venue: ICLR 2024\n\nEntry 3: alemohammad2024mad\n- Bib title: \"Self-Consuming Generative Models Go MAD\"\n- Bib authors: Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.\n- Bib venue: ICLR 2024\n\nEntry 4: cheng2025contamination\n- Bib title: \"A Survey on Data Contamination for Large Language Models\"\n- Bib authors: Cheng, Yuxing and Chang, Yi and Wu, Yuan\n- Bib venue: arXiv:2502.14425, 2025\n\nSearch for each on Semantic Scholar, Google Scholar, or arXiv. Report exact findings for each field."
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T10:22:05.912512+00:00_

Web search results for query: "Data Selection for Language Models via Importance Resampling DSIR Xie NeurIPS 2023"

Links: [{"title":"NeurIPS Poster Data Selection for Language Models via Importance Resampling","url":"https://neurips.cc/virtual/2023/poster/70154"},{"title":"[2302.03169] Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/abs/2302.03169"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://openreview.net/pdf?id=uPSQv0leAu"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/6b9aa8f418bde2840d5f4ab7a02f663b-Abstract-Conference.html"},{"title":"GitHub - p-lambda/dsir: DSIR large-scale data selection framework for language model training · GitHub","url":"https://github.com/p-lambda/dsir"},{"title":"[Quick Review] Data Selection for Language Models via Importance Resampling","url":"https://liner.com/review/data-selection-for-language-models-via-importance-resampling"},{"title":"Data Selection for Language Models via Importance Resampling - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230203169X/abstract"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://www.researchgate.net/publication/368333487_Data_Selection_for_Language_Models_via_Importance_Resampling"},{"title":"[PDF] Data Selection for Language Models via Importance Resampling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Data-Selection-for-Language-Models-via-Importance-Xie-Santurkar/74013b7cfa0fc524803350fca51341004565eb22"},{"title":"[2302.03169v3] Data Selection for Language Models via Importance Resampling","url":"http://arxiv.org/abs/2302.03169v3"}]

I found the paper you're looking for! Here are the key details:

## Data Selection for Language Models via Importance Resampling (DSIR)

**Authors:** Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang

**Conference:*
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T10:22:05.912675+00:00_

Web search results for query: "Short Survey Importance Weighting Machine Learning Kimura Hino TMLR"

Links: [{"title":"[2403.10175] A Short Survey on Importance Weighting for Machine Learning","url":"https://arxiv.org/abs/2403.10175"},{"title":"dblp: A Short Survey on Importance Weighting for Machine Learning.","url":"https://dblp.uni-trier.de/rec/journals/tmlr/KimuraH24.html"},{"title":"A Short Survey on Importance Weighting for Machine Learning Masanari Kimura","url":"https://openreview.net/pdf/f2362512697188a7c0fd592241ec05a6c4f78d54.pdf"},{"title":"Under review as submission to TMLR A Short Survey on Importance Weighting","url":"https://openreview.net/notes/edits/attachment?id=ckkJy32bc1&name=pdf"},{"title":"[2403.10175v2] A Short Survey on Importance Weighting for Machine Learning","url":"https://arxiv.org/abs/2403.10175v2"},{"title":"A Short Survey on Importance Weighting for Machine Learning","url":"https://arxiv.org/html/2403.10175v1"},{"title":"[PDF] A Short Survey on Importance Weighting for Machine Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Short-Survey-on-Importance-Weighting-for-Machine-Kimura-Hino/8feca4f15b7fe6bd61e8d634ff4ef869378d4485"},{"title":"about | Masanari Kimura","url":"https://nocotan.github.io/"},{"title":"Boosting Test Performance with Importance Sampling–a Subpopulation Perspective","url":"https://arxiv.org/pdf/2412.13003"}]

Based on the search results, I found the paper you're looking for:

"A Short Survey on Importance Weighting for Machine Learning" by Masanari Kimura and Hideitsu Hino defines importance weighting as "a fundamental procedure in statistics and machine learning that weights the objective function or probability distribution based on the importance of the instance in some sense."

The survey summarizes the broad applications of importance weighting in machine learning and related research. One key application is that supervised learning under distribution shift can guarantee statisticall
…[truncated 374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T10:22:05.912832+00:00_

Web search results for query: "Aioli Unified Optimization Framework Language Model Data Mixing Chen ICLR 2025"

Links: [{"title":"[2411.05735] Aioli: A Unified Optimization Framework for Language Model Data Mixing","url":"https://arxiv.org/abs/2411.05735"},{"title":"ICLR Aioli: A Unified Optimization Framework for Language Model Data Mixing","url":"https://iclr.cc/virtual/2025/34482"},{"title":"Aioli: A Unified Optimization Framework for Language Model Data Mixing | OpenReview","url":"https://openreview.net/forum?id=R8nT7EqoYF"},{"title":"Aioli: A unified optimization framework for language model data mixing","url":"https://arxiv.org/html/2411.05735v1"},{"title":"aioli: a unified optimization framework for","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/71cc3acb2578bdd1e52bf9f85bbb1af0-Paper-Conference.pdf"},{"title":"GitHub - HazyResearch/aioli: Aioli: A unified optimization framework for language model data mixing · GitHub","url":"https://github.com/HazyResearch/aioli"},{"title":"Paper page - Aioli: A Unified Optimization Framework for Language Model Data Mixing","url":"https://huggingface.co/papers/2411.05735"},{"title":"Hello, I’m Mayee! - Mayee Chen","url":"https://mayeechen.github.io/"},{"title":"Aioli: A unified optimization framework for language model data mixing","url":"https://www.researchgate.net/publication/385701131_Aioli_A_Unified_Optimization_Framework_for_Language_Model_Data_Mixing/fulltext/6731751adb208342def75a30/Aioli-A-Unified-Optimization-Framework-for-Language-Model-Data-Mixing.pdf?origin=scientificContributions"},{"title":"CDS Researchers Make Strong Showing at ICLR 2025 | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/cds-researchers-make-strong-showing-at-iclr-2025-95b0a225dc49"}]

I found relevant information about the paper you searched for. Here's what I found:

## Aioli: A Unified Optimization Framework for Language Model Data Mixing

Language model performance depends on identifying th
…[truncated 1585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:22:05.913011+00:00_

Web search results for query: "DoReMi Optimizing Data Mixtures Speeds Up Language Model Pretraining Xie NeurIPS 2023"

Links: [{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/dcba6be91359358c2355cd920da3fcbd-Paper-Conference.pdf"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | OpenReview","url":"https://openreview.net/forum?id=lXuByUeHhd"},{"title":"[2305.10429] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/abs/2305.10429"},{"title":"NeurIPS Poster DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://neurips.cc/virtual/2023/poster/70588"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Request PDF","url":"https://www.researchgate.net/publication/401463528_DoReMi_Optimizing_Data_Mixtures_Speeds_Up_Language_Model_Pretraining"},{"title":"[PDF] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DoReMi:-Optimizing-Data-Mixtures-Speeds-Up-Language-Xie-Pham/9b4f7c97c0b83a80c32bc0b93595cbcfb4ecb16d"},{"title":"Paper page - DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://huggingface.co/papers/2305.10429"},{"title":"DoReMi: optimizing data mixtures speeds up language ...","url":"https://dl.acm.org/doi/10.5555/3666122.3669181"},{"title":"GitHub - sangmichaelxie/doremi: Pytorch implementation of DoReMi, a method for optimizing the data mixture weights in language modeling datasets · GitHub","url":"https://github.com/sangmichaelxie/doremi"},{"title":"[Quick Review] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://liner.com/review/doremi-optimizing-data-mixtures-speeds-up-language-model-pretraining"}]

I found the paper you're looking for! Here are the key details:

**Title:** 
…[truncated 1111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T10:22:05.913152+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
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

_source line 54 · 2026-05-26T10:22:05.913266+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T10:22:05.913393+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature Mitchell ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature Mitchell ICML 2023"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T10:22:05.913523+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify entries 28-31",
  "prompt": "Verify these 4 bibliography entries by searching the web. For each, confirm: (1) paper exists, (2) exact title, (3) author names/spelling, (4) year, (5) venue, (6) arXiv ID if applicable.\n\nEntry 1: ye2025mixing\n- Bib title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n- Bib authors: Ye, Jiasheng and Liu, Peiju and Sun, Tianxiang and Zhou, Yunhua and Zhan, Jun and Qiu, Xipeng\n- Bib venue: ICLR 2025\n\nEntry 2: yang2026mixing\n- Bib title: \"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training\"\n- Bib authors: Yang, Kailai and Liu, Xiao and Ji, Lei and Li, Hao and Liang, Xiao and Liu, Zhiwei and Gong, Yeyun and Cheng, Peng and Yang, Mao\n- Bib venue: ACL 2026\n\nEntry 3: penedo2024fineweb\n- Bib title: \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\"\n- Bib authors: Penedo, Guilherme and Kydlíček, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and von Werra, Leandro and Wolf, Thomas\n- Bib venue: NeurIPS Datasets and Benchmarks 2024\n\nEntry 4: yang2025qwen3\n- Bib title: \"Qwen3 Technical Report\"\n- Bib authors: Yang, An and Yang, Baosong and Zhang, Beichen and others\n- Bib venue: arXiv:2505.09388, 2025\n\nSearch for each on Semantic Scholar, Google Scholar, or arXiv. Report exact findings for each field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify entries 28-31",
    "prompt": "Verify these 4 bibliography entries by searching the web. For each, confirm: (1) paper exists, (2) exact title, (3) author names/spelling, (4) year, (5) venue, (6) arXiv ID if applicable.\n\nEntry 1: ye2025mixing\n- Bib title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n- Bib authors: Ye, Jiasheng and Liu, Peiju and Sun, Tianxiang and Zhou, Yunhua and Zhan, Jun and Qiu, Xipeng\n- Bib venue: ICLR 2025\n\nEntry 2: yang2026mixing\n- Bib title: \"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training\"\n- Bib authors: Yang, Kailai and Liu, Xiao and Ji, Lei and Li, Hao and Liang, Xiao and Liu, Zhiwei and Gong, Yeyun and Cheng, Peng and Yang, Mao\n- Bib venue: ACL 2026\n\nEntry 3: penedo2024fineweb\n- Bib title: \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\"\n- Bib authors: Penedo, Guilherme and Kydlíček, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and von Werra, Leandro and Wolf, Thomas\n- Bib venue: NeurIPS Datasets and Benchmarks 2024\n\nEntry 4: yang2025qwen3\n- Bib title: \"Qwen3 Technical Report\"\n- Bib authors: Yang, An and Yang, Baosong and Zhang, Beichen and others\n- Bib venue: arXiv:2505.09388, 2025\n\nSearch for each on Semantic Scholar, Google Scholar, or arXiv. Report exact findings for each field."
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:22:05.913731+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2305.10429 DoReMi authors list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2305.10429 DoReMi authors list"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T10:22:05.913874+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2411.05735 Aioli authors Mayee Chen Michael Hu Nicholas Lourie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2411.05735 Aioli authors Mayee Chen Michael Hu Nicholas Lourie"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T10:22:05.914003+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2403.10175 Kimura Hino importance weighting TMLR accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2403.10175 Kimura Hino importance weighting TMLR accepted"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T10:22:05.914129+00:00_

Web search results for query: "arxiv 2305.10429 DoReMi authors list"

Links: [{"title":"[2305.10429] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/abs/2305.10429"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Request PDF","url":"https://www.researchgate.net/publication/370841750_DoReMi_Optimizing_Data_Mixtures_Speeds_Up_Language_Model_Pretraining"},{"title":"Paper page - DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://huggingface.co/papers/2305.10429"},{"title":"[2305.10429v4] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/abs/2305.10429v4"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/pdf/2305.10429"},{"title":"GitHub - sangmichaelxie/doremi: Pytorch implementation of DoReMi, a method for optimizing the data mixture weights in language modeling datasets · GitHub","url":"https://github.com/sangmichaelxie/doremi"},{"title":"dblp: DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining.","url":"https://dblp.org/rec/journals/corr/abs-2305-10429.html"},{"title":"Collections - Hugging Face","url":"https://huggingface.co/collections?paper=2305.10429"},{"title":"ml-papers/papers/2023/230517 DoReMi.md at main · rosinality/ml-papers","url":"https://github.com/rosinality/ml-papers/blob/main/papers/2023/230517%20DoReMi.md"}]

The authors of arxiv paper 2305.10429 (DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining) are: Sang Michael Xie, Hieu Pham, Xuanyi Dong, Nan Du, Hanxiao Liu, Yifeng Lu, Percy Liang, Quoc V. Le, Tengyu Ma, and Adams Wei Yu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T10:22:05.914279+00:00_

Web search results for query: "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature Mitchell ICML 2023"

Links: [{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://proceedings.mlr.press/v202/mitchell23a.html"},{"title":"GitHub - eric-mitchell/detect-gpt: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature · GitHub","url":"https://github.com/eric-mitchell/detect-gpt"},{"title":"(PDF) DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://www.researchgate.net/publication/367461943_DetectGPT_Zero-Shot_Machine-Generated_Text_Detection_using_Probability_Curvature"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230111305M/abstract"},{"title":"dblp: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.","url":"https://dblp.org/rec/conf/icml/Mitchell0KMF23.html"},{"title":"ICML Oral DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://icml.cc/virtual/2023/oral/25525"},{"title":"[Paper Note] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, Eric Mitchell+, ICML'23, 2023.01 · Issue #3698 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3698"}]

I've successfully found information about the DetectGPT paper. Here are the key findings:

## Overview

DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature is a paper by Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, and Chelsea Finn that was published at the 40th International Conference on Machine Learning (ICML) 2023.

## Core Methodolo
…[truncated 1097 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-26T10:22:05.914419+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shi Weijia \"Detecting Pretraining Data from Large Language Models\" ICLR 2024 Min-K% Prob"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shi Weijia \"Detecting Pretraining Data from Large Language Models\" ICLR 2024 Min-K% Prob"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-26T10:22:05.914537+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
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

_source line 64 · 2026-05-26T10:22:05.914650+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T10:22:05.914764+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ye Jiasheng \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ye Jiasheng \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\" ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-26T10:22:05.914908+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify entries 32-37",
  "prompt": "Verify these 6 bibliography entries by searching the web. For each, confirm: (1) paper exists, (2) exact title, (3) author names/spelling, (4) year, (5) venue, (6) arXiv ID if applicable.\n\nEntry 1: kuo2024weighting\n- Bib title: \"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\"\n- Bib authors: Kuo, Hsun-Yu and Tan, Pei-Yu and Peng, Chao-Wei and Chen, Yun-Nung\n- Bib venue: arXiv:2410.21526, 2024\n\nEntry 2: bengio2009curriculum\n- Bib title: \"Curriculum Learning\"\n- Bib authors: Bengio, Yoshua and Louradour, Jérôme and Collobert, Ronan and Weston, Jason\n- Bib venue: ICML 2009\n\nEntry 3: radford2019language\n- Bib title: \"Language Models are Unsupervised Multitask Learners\"\n- Bib authors: Radford, Alec and Wu, Jeffrey and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya\n- Bib venue: OpenAI Blog 2019\n\nEntry 4: brown2020language\n- Bib title: \"Language Models are Few-Shot Learners\"\n- Bib authors: Brown, Tom B. and Mann, Benjamin and Ryder, Nick and others\n- Bib venue: NeurIPS 2020\n\nEntry 5: longpre2024pretrainers\n- Bib title: \"A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity\"\n- Bib authors: Longpre, Shane and Mahari, Robert and Lee, Naana Obeng-Marnu and others\n- Bib venue: arXiv:2305.13169, 2024\n\nEntry 6: lee2022dedup\n- Bib title: \"Deduplicating Training Data Makes Language Models Better\"\n- Bib authors: Lee, Katherine and Ippolito, Daphne and Nystrom, Andrew and Zhang, Chiyuan and Eck, Douglas and Callison-Burch, Chris and Carlini, Nicholas\n- Bib venue: ACL 2022\n\nSearch for each on Semantic Scholar, Google Scholar, or arXiv. Report exact findings for each field."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify entries 32-37",
    "prompt": "Verify these 6 bibliography entries by searching the web. For each, confirm: (1) paper exists, (2) exact title, (3) author names/spelling, (4) year, (5) venue, (6) arXiv ID if applicable.\n\nEntry 1: kuo2024weighting\n- Bib title: \"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification\"\n- Bib authors: Kuo, Hsun-Yu and Tan, Pei-Yu and Peng, Chao-Wei and Chen, Yun-Nung\n- Bib venue: arXiv:2410.21526, 2024\n\nEntry 2: bengio2009curriculum\n- Bib title: \"Curriculum Learning\"\n- Bib authors: Bengio, Yoshua and Louradour, Jérôme and Collobert, Ronan and Weston, Jason\n- Bib venue: ICML 2009\n\nEntry 3: radford2019language\n- Bib title: \"Language Models are Unsupervised Multitask Learners\"\n- Bib authors: Radford, Alec and Wu, Jeffrey and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya\n- Bib venue: OpenAI Blog 2019\n\nEntry 4: brown2020language\n- Bib title: \"Language Models are Few-Shot Learners\"\n- Bib authors: Brown, Tom B. and Mann, Benjamin and Ryder, Nick and others\n- Bib venue: NeurIPS 2020\n\nEntry 5: longpre2024pretrainers\n- Bib title: \"A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity\"\n- Bib authors: Longpre, Shane and Mahari, Robert and Lee, Naana Obeng-Marnu and others\n- Bib venue: arXiv:2305.13169, 2024\n\nEntry 6: lee2022dedup\n- Bib title: \"Deduplicating Training Data Makes Language Models Better\"\n- Bib authors: Lee, Katherine and Ippolito, Daphne and Nystrom, Andrew and Zhang, Chiyuan and Eck, Douglas and Callison-Burch, Chris and Carlini, Nicholas\n- Bib venue: ACL 2022\n\nSearch for each on Semantic Scholar, Google Scholar, or arXiv. Report exact findings for each field."
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-26T10:22:05.915096+00:00_

Web search results for query: "arxiv 2411.05735 Aioli authors Mayee Chen Michael Hu Nicholas Lourie"

Links: [{"title":"[2411.05735] Aioli: A Unified Optimization Framework for Language Model Data Mixing","url":"https://arxiv.org/abs/2411.05735"},{"title":"Aioli: A unified optimization framework for language model data mixing","url":"https://arxiv.org/html/2411.05735"},{"title":"Paper page - Aioli: A Unified Optimization Framework for Language Model Data Mixing","url":"https://huggingface.co/papers/2411.05735"},{"title":"GitHub - HazyResearch/aioli: Aioli: A unified optimization framework for language model data mixing · GitHub","url":"https://github.com/HazyResearch/aioli"},{"title":"Aioli: A Unified Optimization Framework for Language ...","url":"https://arxiv.org/pdf/2411.05735"},{"title":"Hello, I’m Mayee! - Mayee Chen","url":"https://mayeechen.github.io/"},{"title":"Machine Learning Nov 2024","url":"https://arxiv.org/list/cs.LG/2024-11?skip=550&show=2000"},{"title":"dblp: Nicholas Lourie","url":"https://dblp.org/pid/218/5457.html"},{"title":"Nicholas Lourie | Semantic Scholar","url":"https://www.semanticscholar.org/author/Nicholas-Lourie/35219984"},{"title":"Mayee Chen Curriculum Vitae Education 2019 –","url":"https://mayeechen.github.io/files/MayeeChen_CV.pdf"}]

I found the paper you're looking for! Here are the details:

**Aioli: A Unified Optimization Framework for Language Model Data Mixing** is authored by Mayee F. Chen (Department of Computer Science, Stanford University), Michael Y. Hu (Center for Data Science, New York University), Nicholas Lourie (Computer Science Department, New York University), Kyunghyun Cho (Center for Data Science, New York University and Prescient Design, Genentech), and Christopher Ré (Department of Computer Science, Stanford University).

The paper addresses language model performance and how it depends on identifying the optimal mixture of data groups to train on (e.g., law, code, math). The authors find that no existing meth
…[truncated 411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-26T10:22:05.915245+00:00_

Web search results for query: "arxiv 2403.10175 Kimura Hino importance weighting TMLR accepted"

Links: [{"title":"[2403.10175] A Short Survey on Importance Weighting for Machine Learning","url":"https://arxiv.org/abs/2403.10175"},{"title":"[2403.10175v2] A Short Survey on Importance Weighting for Machine Learning","url":"https://arxiv.org/abs/2403.10175v2"},{"title":"A Short Survey on Importance Weighting for Machine Learning","url":"https://arxiv.org/html/2403.10175v1"},{"title":"[PDF] A Short Survey on Importance Weighting for Machine Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Short-Survey-on-Importance-Weighting-for-Machine-Kimura-Hino/8feca4f15b7fe6bd61e8d634ff4ef869378d4485"},{"title":"Statistics Mar 2024","url":"http://arxiv.org/list/stat/2024-03?skip=695&show=10"},{"title":"Under review as submission to TMLR A Short Survey on Importance Weighting","url":"https://openreview.net/notes/edits/attachment?id=ckkJy32bc1&name=pdf"},{"title":"dblp: A Short Survey on Importance Weighting for Machine Learning.","url":"https://dblp.uni-trier.de/rec/journals/tmlr/KimuraH24.html"},{"title":"A Short Survey on Importance Weighting for Machine Learning Masanari Kimura","url":"https://openreview.net/pdf/f2362512697188a7c0fd592241ec05a6c4f78d54.pdf"}]

Based on the search results, here's what I found about arxiv 2403.10175:

The paper is titled "A Short Survey on Importance Weighting for Machine Learning" by Masanari Kimura and Hideitsu Hino. Importance weighting is described as a fundamental procedure in statistics and machine learning that weights the objective function or probability distribution based on the importance of the instance in some sense.

Regarding the TMLR acceptance: The paper was published in Transactions on Machine Learning Research (TMLR) in 2024, confirming that it was accepted at the venue you mentioned.

The survey summarizes the broad applications of importance weighting in machine learning and related research. The pap
…[truncated 188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T10:22:05.915395+00:00_

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
  "session": "worker_audit_ref-verify-group2_20260526T101557",
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

_source line 70 · 2026-05-26T10:22:05.915512+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-26T10:22:05.915635+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2302.03169 DSIR data selection importance resampling authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2302.03169 DSIR data selection importance resampling authors"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-26T10:22:05.915760+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2410.21526 \"Not All LLM-Generated Data Are Equal\" Kuo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2410.21526 \"Not All LLM-Generated Data Are Equal\" Kuo"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-26T10:22:05.915898+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview Aioli unified optimization framework data mixing ICLR 2025 full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview Aioli unified optimization framework data mixing ICLR 2025 full author list"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-26T10:22:05.916029+00:00_

Web search results for query: "Ye Jiasheng "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance" ICLR 2025"

Links: [{"title":"[2403.16952] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/abs/2403.16952"},{"title":"ICLR Poster Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://iclr.cc/virtual/2025/poster/28624"},{"title":"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/html/2403.16952v2"},{"title":"[PDF] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Data-Mixing-Laws:-Optimizing-Data-Mixtures-by-Ye-Liu/c231dcc7f85e52c2a0e225022a4b755d472b65bb"},{"title":"[2403.16952v1] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/abs/2403.16952v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf"},{"title":"[Quick Review] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://liner.com/review/data-mixing-laws-optimizing-data-mixtures-by-predicting-language-modeling"},{"title":"GitHub - yegcjs/mixinglaws","url":"https://github.com/yegcjs/mixinglaws"}]

I found the paper! Here are the search results:

The paper "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance" was presented at ICLR 2025 as a poster by Jiasheng Ye, Peiju Liu, Tianxiang Sun, Jun Zhan, Yunhua Zhou, and Xipeng Qiu.

**Key contributions:**

The authors discover the quantitative predictability of model performance regarding mixture proportions in function forms, which they refer to as data mixing laws. Fitting such functions on sampl
…[truncated 662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-26T10:22:05.916183+00:00_

Web search results for query: "Shi Weijia "Detecting Pretraining Data from Large Language Models" ICLR 2024 Min-K% Prob"

Links: [{"title":"DETECTING PRETRAINING DATA FROM LARGE LANGUAGE MODELS - Princeton University","url":"https://collaborate.princeton.edu/en/publications/detecting-pretraining-data-from-large-language-models/"},{"title":"[2310.16789] Detecting Pretraining Data from Large Language Models","url":"https://arxiv.org/abs/2310.16789"},{"title":"Detecting Pretraining Data from Large Language Models","url":"https://swj0419.github.io/detect-pretrain.github.io/"},{"title":"Detecting Pretraining Data from Large Language Models [Quick Review]","url":"https://liner.com/review/detecting-pretraining-data-from-large-language-models"},{"title":"Detecting Pretraining Data from Large Language Models Weijia Shi1 ∗","url":"https://openreview.net/pdf?id=ZLJ6XRbdaC"},{"title":"GitHub - swj0419/detect-pretrain-code: This repository provides an original implementation of Detecting Pretraining Data from Large Language Models by *Weijia Shi, *Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu , Terra Blevins , Danqi Chen , Luke Zettlemoyer. · GitHub","url":"https://github.com/swj0419/detect-pretrain-code"},{"title":"Detecting Pretraining Data from Large Language Models","url":"https://arxiv.org/html/2310.16789v3"}]

I found comprehensive information about this research paper. Here's what I found:

## Paper Overview

Shi, W., Ajith, A., Xia, M., Huang, Y., Liu, D., Blevins, T., Chen, D., & Zettlemoyer, L. (2024) presented "Detecting Pretraining Data from Large Language Models" at the 12th International Conference on Learning Representations (ICLR 2024) in Vienna, Austria.

## The Min-K% Prob Method

The paper introduces a detection method MIN-K% PROB based on the hypothesis that an unseen example is likely to contain a few outlier words with low probabilities under the LLM, while a seen example is less likely to have words with such low probabilities.

MIN-K% PROB can b
…[truncated 761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-26T10:22:05.916329+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yang Kailai \"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training\" ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yang Kailai \"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training\" ACL 2026"
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-26T10:22:05.916456+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Alemohammad \"Self-Consuming Generative Models Go MAD\" ICLR 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Alemohammad \"Self-Consuming Generative Models Go MAD\" ICLR 2024 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-26T10:22:05.916577+00:00_

Web search results for query: "arxiv 2302.03169 DSIR data selection importance resampling authors"

Links: [{"title":"[2302.03169] Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/abs/2302.03169"},{"title":"Paper page - Data Selection for Language Models via Importance Resampling","url":"https://huggingface.co/papers/2302.03169"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/pdf/2302.03169"},{"title":"Data Selection for Language Models via Importance Resampling - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230203169X/abstract"},{"title":"[2302.03169v3] Data Selection for Language Models via Importance Resampling","url":"http://arxiv.org/abs/2302.03169v3"},{"title":"Data Selection for LMs via Importance Resampling","url":"https://www.emergentmind.com/papers/2302.03169"},{"title":"[PDF] Data Selection for Language Models via Importance Resampling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Data-Selection-for-Language-Models-via-Importance-Xie-Santurkar/a008cc894024329d832d2c9c489d57440e3fa234"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://www.researchgate.net/publication/368333487_Data_Selection_for_Language_Models_via_Importance_Resampling"},{"title":"Data Selection for Language Models via Importance Resampling | alphaXiv","url":"https://www.alphaxiv.org/abs/2302.03169v3"}]

Based on the search results, here is the information about arxiv paper 2302.03169:

**Title:** Data Selection for Language Models via Importance Resampling

**Authors:** Sang Michael Xie, Shibani Santurkar, Tengyu Ma, and Percy Liang

**Publication Date:** February 6, 2023

**Main Contribution:** The authors propose Data Selection with Importance Resampling (DSIR), an efficient and scalable framework that estimates importance weights in a reduced feature space for tractability and selects data with importance resampling according to the
…[truncated 610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-26T10:22:05.916727+00:00_

Web search results for query: "openreview Aioli unified optimization framework data mixing ICLR 2025 full author list"

Links: [{"title":"Aioli: A Unified Optimization Framework for Language Model Data Mixing | OpenReview","url":"https://openreview.net/forum?id=R8nT7EqoYF"},{"title":"aioli: a unified optimization framework for","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/71cc3acb2578bdd1e52bf9f85bbb1af0-Paper-Conference.pdf"},{"title":"[2411.05735] Aioli: A Unified Optimization Framework for Language Model Data Mixing","url":"https://arxiv.org/abs/2411.05735"},{"title":"ICLR Aioli: A Unified Optimization Framework for Language Model Data Mixing","url":"https://iclr.cc/virtual/2025/34482"},{"title":"Aioli: A unified optimization framework for language model data mixing","url":"https://arxiv.org/html/2411.05735v2"},{"title":"GitHub - HazyResearch/aioli: Aioli: A unified optimization framework for language model data mixing · GitHub","url":"https://github.com/HazyResearch/aioli"},{"title":"Paper page - Aioli: A Unified Optimization Framework for Language Model Data Mixing","url":"https://huggingface.co/papers/2411.05735"},{"title":"Meet Aioli: A Unified Optimization Framework for Language Model Data Mixing - MarkTechPost","url":"https://www.marktechpost.com/2024/11/12/meet-aioli-a-unified-optimization-framework-for-language-model-data-mixing/"},{"title":"Aioli: A Unified Optimization Framework for Language Model Data Mixing","url":"https://arxiv.org/pdf/2411.05735"}]

Based on the search results, I found the paper "Aioli: A Unified Optimization Framework for Language Model Data Mixing" with the full author list:

The authors are Mayee F. Chen, Michael Y. Hu, Nicholas Lourie, Kyunghyun Cho, and Christopher Ré, from Stanford University, New York University's Center for Data Science and Computer Science Department, and Genentech's Prescient Design.

The paper was published on March 6, 2025, and last modified on April 30, 2025 for the ICLR 2025 Workshop 
…[truncated 117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-26T10:22:05.916891+00:00_

Web search results for query: "arXiv 2410.21526 "Not All LLM-Generated Data Are Equal" Kuo"

Links: [{"title":"[2410.21526] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://arxiv.org/abs/2410.21526"},{"title":"Not All LLM-Generated Data Are Equal: Rethinking data weighting in Text Classification","url":"https://arxiv.org/html/2410.21526v1"},{"title":"[2410.21526v1] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://arxiv.org/abs/2410.21526v1"},{"title":"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification | Request PDF","url":"https://www.researchgate.net/publication/385354062_Not_All_LLM-Generated_Data_Are_Equal_Rethinking_Data_Weighting_in_Text_Classification"},{"title":"[Literature Review] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://www.themoonlight.io/en/review/not-all-llm-generated-data-are-equal-rethinking-data-weighting-in-text-classification"},{"title":"Not All LLM-Generated Data Are Equal","url":"https://www.alphaxiv.org/ko/overview/2410.21526v1"},{"title":"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification | PromptLayer","url":"https://www.promptlayer.com/research-papers/do-llms-make-training-data-irrelevant"},{"title":"What Matters in LLM-generated Data: Diversity and Its Effect on Model Fine-Tuning","url":"https://arxiv.org/html/2506.19262v2"},{"title":"Hsun-Yu Kuo - Not All LLM-Generated Data Are Equal","url":"https://www.linkedin.com/posts/hsun-yu-kuo_not-all-llm-generated-data-are-equal-rethinking-activity-7301752160239661056-aSUZ"}]

I found the paper you're looking for! Here's what I found:

**arXiv:2410.21526** is titled "Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification" by Hsun-Yu Kuo and 4 other authors (Yin-Hsiang Liao, Yu-Chieh Chao, Wei-Yun Ma, and Pu-Jen Cheng). It was submi
…[truncated 760 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-26T10:22:05.917049+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bengio Louradour Collobert Weston \"Curriculum Learning\" ICML 2009"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bengio Louradour Collobert Weston \"Curriculum Learning\" ICML 2009"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-26T10:22:05.917177+00:00_

Web search results for query: "Alemohammad "Self-Consuming Generative Models Go MAD" ICLR 2024 arXiv"

Links: [{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/pdf/2307.01850"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD - Houston Methodist Scholars","url":"https://scholars.houstonmethodist.org/en/publications/self-consuming-generative-models-go-mad/"},{"title":"(PDF) Self-Consuming Generative Models Go MAD","url":"https://www.researchgate.net/publication/372136378_Self-Consuming_Generative_Models_Go_MAD"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://richb.rice.edu/2023/07/12/self-consuming-generative-models-go-mad/"},{"title":"Self-Consuming Generative Models Go MAD | Montreal AI Ethics Institute","url":"https://montrealethics.ai/self-consuming-generative-models-go-mad/"},{"title":"ICLR Poster Self-Consuming Generative Models Go MAD","url":"https://iclr.cc/virtual/2024/poster/18592"}]

I found comprehensive information about this paper. Here are the results:

## Paper Overview

The paper "Self-Consuming Generative Models Go MAD" is authored by Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G. Baraniuk.

## Key Findings

The paper addresses how using synthetic data to train next-generation generative models create
…[truncated 730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-26T10:22:05.917339+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2502.14425 \"Survey on Data Contamination for Large Language Models\" Cheng Chang Wu 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2502.14425 \"Survey on Data Contamination for Large Language Models\" Cheng Chang Wu 2025"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-26T10:22:05.917468+00:00_

Web search results for query: "Yang Kailai "Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training" ACL 2026"

Links: [{"title":"Kailai Yang - ACL Anthology","url":"https://aclanthology.org/people/kailai-yang/"},{"title":"Yang Liu's Homepage at Tsinghua University","url":"https://nlp.csai.tsinghua.edu.cn/~ly/pub.html"},{"title":"Findings of the Association for Computational Linguistics (2026) - ACL Anthology","url":"https://aclanthology.org/events/findings-2026/"},{"title":"Machine Learning Jul 2025","url":"https://www.arxiv.org/list/cs.LG/2025-07?skip=1275&show=50"},{"title":"Accepted Main Conference Papers - ACL 2024","url":"https://2024.aclweb.org/program/main_conference_papers/"},{"title":"Selective Preference Optimization via Token-Level Reward Function Estimation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.359/"},{"title":"Towards Interpretable Mental Health Analysis with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.370/"},{"title":"Haiqin Yang - ACL Anthology","url":"https://aclanthology.org/people/haiqin-yang/"},{"title":"dblp: Haiqin Yang","url":"https://dblp.org/pid/63/3939.html"}]

I found information about the paper! "Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training" is by Kailai Yang, Xiao Liu, Lei Ji, Hao Li, Yeyun Gong, Peng Cheng, and Mao Yang, and it appears on arXiv (2507.15640) with subjects in Machine Learning (cs.LG), Artificial Intelligence (cs.AI), and Computation and Language (cs.CL).

While my search results show the paper on arXiv from July 2025, I couldn't find specific information about its ACL 2026 status in these results. You may want to check the ACL 2026 proceedings directly or the arXiv link for the most current publication status.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-26T10:22:05.917605+00:00_

Web search results for query: "Bengio Louradour Collobert Weston "Curriculum Learning" ICML 2009"

Links: [{"title":"Curriculum learning","url":"https://bibbase.org/network/publication/bengio-louradour-collobert-weston-curriculumlearning-2009"},{"title":"Curriculum learning | Proceedings of the 26th Annual International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.1145/1553374.1553380"},{"title":"[PDF] Curriculum learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Curriculum-learning-Bengio-Louradour/8de174ab5419b9d3127695405efd079808e956e8"},{"title":"Curriculum Learning - Ronan Collobert","url":"https://ronan.collobert.com/pub/2009_curriculum_icml.pdf"},{"title":"dblp: Curriculum learning.","url":"https://dblp.org/rec/conf/icml/BengioLCW09.html"},{"title":"Curriculum learning. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/11de817496c3925469b1a026ce7046342"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Bengio%2C+Y.%2C+Louradour%2C+J.%2C+Collobert%2C+R.%2C+Weston%2C+J.%3A+Curriculum+learning.+In%3A+ICML+%282009%29"},{"title":"(PDF) Curriculum learning","url":"https://www.academia.edu/58928901/Curriculum_learning"},{"title":"ICML 2009","url":"https://icml.cc/Conferences/2009/abstracts.html"},{"title":"Bengio, 2009 Curriculum Learning.pdf","url":"https://www.scribd.com/document/425393423/Bengio-2009-Curriculum-Learning-pdf"}]

I found the paper! Here are the search results for the "Curriculum Learning" paper:

**Paper Details:**
The paper is authored by Bengio, Y., Louradour, J., Collobert, R., & Weston, J. and was published in Proceedings of the 26th Annual International Conference on Machine Learning - ICML '09 in Montreal, Quebec, Canada in 2009.

**Paper Summary:**
"Curriculum learning" formalizes training strategies where humans and animals learn better when examples are organized in a meaningful order illustrating gradually more concepts and gradually more complex ones.

**Key Contribution
…[truncated 788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-26T10:22:05.917757+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Penedo Guilherme \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\" NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Penedo Guilherme \"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\" NeurIPS 2024"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-26T10:22:05.917903+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Radford Wu Child Luan Amodei Sutskever \"Language Models are Unsupervised Multitask Learners\" OpenAI 2019 GPT-2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Radford Wu Child Luan Amodei Sutskever \"Language Models are Unsupervised Multitask Learners\" OpenAI 2019 GPT-2"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-26T10:22:05.918038+00:00_

Web search results for query: "arXiv 2502.14425 "Survey on Data Contamination for Large Language Models" Cheng Chang Wu 2025"

Links: [{"title":"[2502.14425] A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/abs/2502.14425"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425"},{"title":"A Survey on Data Contamination for Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2502.14425"},{"title":"[2502.14425v1] A Survey on Data Contamination for Large Language Models","url":"http://arxiv.org/abs/2502.14425v1"},{"title":"[2502.14425v2] A Survey on Data Contamination for Large Language Models","url":"http://arxiv.org/abs/2502.14425v2"},{"title":"Pretraining Data Exposure in Large Language Models: A Survey of Membership Inference, Data Contamination, and Security Implications | Natural Language Processing and Information Systems","url":"https://dl.acm.org/doi/10.1007/978-3-031-97144-0_14"},{"title":"Pretraining Data Exposure in Large Language Models: A Survey of Membership Inference, Data Contamination, and Security Implications | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-031-97144-0_14"}]

Based on the search results, I found the paper you're looking for:

**A Survey on Data Contamination for Large Language Models** is authored by Yuxing Cheng, Yi Chang, and Yuan Wu, with the arXiv identifier 2502.14425.

**Overview:**
Recent advancements in Large Language Models (LLMs) have demonstrated significant progress in various areas, such as text generation and code synthesis. However, the reliability of performance evaluation has come under scrutiny due to data contamination—the unintended overlap between training and test datasets. This overlap has the potential to artificially inflate model performance, as LLMs are typically trained on extensive datasets scraped from publicly available sources. These datasets often inadvertently overla
…[truncated 662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-26T10:22:05.918246+00:00_

Here are the verification results for all 4 entries.

---

## Entry 1: xie2023doremi

| Field | Bib value | Verified | Status |
|-------|-----------|----------|--------|
| Paper exists | — | Yes | OK |
| Title | "DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining" | Exact match | OK |
| Authors | Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei | Exact match | OK |
| Year | 2023 | Correct | OK |
| Venue | NeurIPS 2023 | Confirmed (NeurIPS 2023 Conference paper) | OK |
| arXiv ID | — | **2305.10429** | Add if desired |

**Verdict: All fields correct.**

---

## Entry 2: xie2023dsir

| Field | Bib value | Verified | Status |
|-------|-----------|----------|--------|
| Paper exists | — | Yes | OK |
| Title | "Data Selection for Language Models via Importance Resampling" | Exact match | OK |
| Authors | Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy | Exact match | OK |
| Year | 2023 | Correct | OK |
| Venue | NeurIPS 2023 | Confirmed (NeurIPS 2023 Conference paper) | OK |
| arXiv ID | — | **2302.03169** | Add if desired |

**Verdict: All fields correct.**

---

## Entry 3: chen2025aioli

| Field | Bib value | Verified | Status |
|-------|-----------|----------|--------|
| Paper exists | — | Yes | OK |
| Title | "Aioli: A Unified Optimization Framework for Language Model Data Mixing" | Exact match | OK |
| Authors | Chen, Mayee F. and Hu, Michael Y. and Lourie, Nicholas and Cho, Kyunghyun and Ré, Christopher | Exact match (5 authors confirmed) | OK |
| Year | 2025 | Correct | OK |
| Venue | ICLR 2025 | Confirmed (ICLR 2025 Conference paper per OpenReview and proceedings) | OK |
| arXiv ID | — | **2411.05735** | Add if desired |

**Verdict: All fields correct.**

---

## Entry 4: kimura2024iw

| Field | Bib value | Verified | Status |
|-------|-----------|----------|--------|
| Paper exists | — | Yes | OK |
| Title | 
…[truncated 1434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Agent",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-26T10:22:05.918406+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2310.16789 authors list Shi Ajith Xia Huang Liu Blevins Chen Zettlemoyer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2310.16789 authors list Shi Ajith Xia Huang Liu Blevins Chen Zettlemoyer"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-26T10:22:05.918542+00:00_

Web search results for query: "Radford Wu Child Luan Amodei Sutskever "Language Models are Unsupervised Multitask Learners" OpenAI 2019 GPT-2"

Links: [{"title":"GitHub - openai/gpt-2: Code for the paper \"Language Models are Unsupervised Multitask Learners\" · GitHub","url":"https://github.com/openai/gpt-2"},{"title":"Language Models are Unsupervised Multitask Learners","url":"https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf"},{"title":"Language Models are Unsupervised Multitask Learners","url":"https://bibbase.org/network/publication/radford-wu-child-luan-amodei-sutskever-languagemodelsareunsupervisedmultitasklearners-2019"},{"title":"[PDF] Language Models are Unsupervised Multitask Learners | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-are-Unsupervised-Multitask-Learners-Radford-Wu/9405cc0d6169988371b2755e573cc28650d14dfe"},{"title":"Radford, A., Wu, J., Child, R., Luan, D., Amodei, D. and Sutskever, I. (2019) Language Models Are Unsupervised Multitask Learners. OpenAI Blog, 1, 8, 9. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3986585"},{"title":"Language models are unsupervised multitask learners | BibSonomy","url":"https://www.bibsonomy.org/bibtex/61ea7e007d6c95171a2ff3396b1af7d9"},{"title":"Language Models are Unsupervised Multitask Learners | by Samyak Kala | Medium","url":"https://medium.com/@samyakkala128/language-models-are-unsupervised-multitask-learners-e82c5b671544"},{"title":"Language Models are Unsupervised Multitask Learners (GPT-2) | Fan Pu Zeng","url":"https://fanpu.io/summaries/2023-08-10-language-models-are-unsupervised-multitask-learners/"},{"title":"Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). Language Models Are Unsupervised Multitask Learners. OpenAI Blog, 1, 9. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referen
…[truncated 1169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-26T10:22:05.918701+00:00_

Web search results for query: "Penedo Guilherme "The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale" NeurIPS 2024"

Links: [{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/370df50ccfdf8bde18f8f9c2d9151bda-Abstract-Datasets_and_Benchmarks_Track.html"},{"title":"[2406.17557] The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://arxiv.org/abs/2406.17557"},{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://papers.nips.cc/paper_files/paper/2024/hash/370df50ccfdf8bde18f8f9c2d9151bda-Abstract-Datasets_and_Benchmarks_Track.html"},{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://papers.neurips.cc/paper_files/paper/2024/file/370df50ccfdf8bde18f8f9c2d9151bda-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://www.researchgate.net/publication/397205318_The_FineWeb_Datasets_Decanting_the_Web_for_the_Finest_Text_Data_at_Scale"},{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://arxiv.org/html/2406.17557v1"},{"title":"[PDF] The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-FineWeb-Datasets:-Decanting-the-Web-for-the-at-Penedo-Kydl%C3%ADcek/b83a9e35c3aeeb37708e362473c7617d59b815b5"},{"title":"[2406.17557v2] The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://arxiv.org/abs/2406.17557v2"}]

I found the research paper you're looking for. Here's what I found:

"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale" introduces FineWeb, a 15-trillion token dataset derived from 96 Common Crawl snapshots that produces better-performing LLMs than ot
…[truncated 1039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-26T10:22:05.918869+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Brown \"Language Models are Few-Shot Learners\" NeurIPS 2020 GPT-3 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Brown \"Language Models are Few-Shot Learners\" NeurIPS 2020 GPT-3 authors"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-26T10:22:05.919004+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yang An \"Qwen3 Technical Report\" arXiv 2505.09388"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yang An \"Qwen3 Technical Report\" arXiv 2505.09388"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-26T10:22:05.919135+00:00_

Web search results for query: "arxiv 2310.16789 authors list Shi Ajith Xia Huang Liu Blevins Chen Zettlemoyer"

Links: [{"title":"[2310.16789] Detecting Pretraining Data from Large Language Models","url":"https://arxiv.org/abs/2310.16789"},{"title":"GitHub - swj0419/detect-pretrain-code: This repository provides an original implementation of Detecting Pretraining Data from Large Language Models by *Weijia Shi, *Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu , Terra Blevins , Danqi Chen , Luke Zettlemoyer. · GitHub","url":"https://github.com/swj0419/detect-pretrain-code"},{"title":"[PDF] Detecting Pretraining Data from Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a"},{"title":"[2310.16789] Detecting Pretraining Data from Large Language Models","url":"http://export.arxiv.org/abs/2310.16789"},{"title":"GitHub - jaechan-repo/muse_bench · GitHub","url":"https://github.com/jaechan-repo/muse_bench"},{"title":"detect-pretrain-code/README.md at main · swj0419/detect-pretrain-code","url":"https://github.com/swj0419/detect-pretrain-code/blob/main/README.md"},{"title":"A survey on large language model based autonomous agents | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40231-1"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?show=2000&skip=471"}]

Based on the search results, the authors of arxiv paper 2310.16789 are: Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer. 

The paper is titled "Detecting Pretraining Data from Large Language Models" and was submitted on October 25, 2023.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-26T10:22:05.919281+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2502.14425 authors \"Yuxing Cheng\" \"Yi Chang\" \"Yuan Wu\" affiliation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2502.14425 authors \"Yuxing Cheng\" \"Yi Chang\" \"Yuan Wu\" affiliation"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-26T10:22:05.919408+00:00_

Web search results for query: "Yang An "Qwen3 Technical Report" arXiv 2505.09388"

Links: [{"title":"[2505.09388] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388"},{"title":"Paper page - Qwen3 Technical Report","url":"https://huggingface.co/papers/2505.09388"},{"title":"Qwen3 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/391741196_Qwen3_Technical_Report"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"[2505.09388] Qwen3 Technical Report - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2505.09388"},{"title":"[2505.09388v1] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388v1"},{"title":"Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination","url":"https://arxiv.org/html/2507.10532v2"}]

I found the paper you're looking for. Here are the key details about the "Qwen3 Technical Report" by Yang An and colleagues:

**Paper Information:**
- arXiv:2505.09388, submitted on May 14, 2025
- Lead author: An Yang (with 59+ co-authors)

**Overview:**
Qwen3 is the latest version of the Qwen model family, comprising a series of large language models (LLMs) designed to advance performance, efficiency, and multilingual capabilities.

**Key Features:**
- The Qwen3 series includes models of both dense and Mixture-of-Expert (MoE) architectures, with parameter scales ranging from 0.6 to 235 billion.

- A key innovation is the integration of thinking mode (for complex, multi-step reasoning) and non-thinking mode (for rapid, context-driven responses) into a unified framework, eliminating the need to switch between different models like chat-optimized models and dedicated reasoning models.

- Qwen3 introduces a thinking budget mechanism, allowing users to allocate computational resources adaptively during inference, balancing latency and performance based on task complexity.

- Compared to Q
…[truncated 263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-26T10:22:05.919562+00:00_

Web search results for query: "Brown "Language Models are Few-Shot Learners" NeurIPS 2020 GPT-3 authors"

Links: [{"title":"Language Models are Few-Shot Learners","url":"https://papers.nips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html"},{"title":"[2005.14165] Language Models are Few-Shot Learners","url":"https://arxiv.org/abs/2005.14165"},{"title":"Language Models are Few-Shot Learners Tom B. Brown∗ Benjamin Mann∗ Nick Ryder∗","url":"https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf"},{"title":"(PDF) Language Models are Few-Shot Learners","url":"https://www.researchgate.net/publication/341724146_Language_Models_are_Few-Shot_Learners"},{"title":"Language Models are Few-Shot Learners Tom B. Brown∗ Benjamin Mann∗ Nick Ryder∗","url":"https://arxiv.org/pdf/2005.14165"},{"title":"Language Models are Few-shot Learners (GPT-3) - Samuel Albanie","url":"https://samuelalbanie.com/digests/2022-07-gpt-3/"},{"title":"Language models are few-shot learners | Proceedings of the 34th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/abs/10.5555/3495724.3495883"},{"title":"Language Models are Few-Shot Learners (GPT-3)","url":"https://ysu1989.github.io/courses/au20/cse5539/GPT-3.pdf"}]

Based on the search results, here's the information about the paper "Language Models are Few-Shot Learners":

## Paper Details

The paper was authored by Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei, and it was published at Advances in Neural Information Processing Systems 33 (N
…[truncated 529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-26T10:22:05.919702+00:00_

Web search results for query: "arxiv 2502.14425 authors "Yuxing Cheng" "Yi Chang" "Yuan Wu" affiliation"

Links: [{"title":"[2502.14425] A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/abs/2502.14425"},{"title":"arXiv:2502.14425v2 [cs.CL] 5 Jun 2025","url":"https://arxiv.org/pdf/2502.14425"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425.pdf"},{"title":"[2504.14425] Optimal Scheduling of Dynamic Transport","url":"https://arxiv.org/abs/2504.14425"},{"title":"Computer Science Feb 2025","url":"https://arxiv.org/list/cs/2025-02?skip=7300"},{"title":"Computation and Language Feb 2025","url":"https://www.arxiv.org/list/cs.CL/2025-02?skip=1175&show=25"},{"title":"GRB seminar log (Mar. 2023-)","url":"https://www-tap.scphys.kyoto-u.ac.jp/seminar/grbsemi2024.html"},{"title":"arXiv:2505.14425v1 [cs.CL] 20 May 2025","url":"https://arxiv.org/pdf/2505.14425"},{"title":"Artificial Intelligence Feb 2025","url":"https://arxiv.org/list/cs.AI/2025-02?skip=400&show=1000"}]

Based on the search results, here's the information about arxiv paper 2502.14425:

**Title:** A Survey on Data Contamination for Large Language Models

**Authors:** Yuxing Cheng, Yi Chang, and Yuan Wu

**Affiliations:** Yuxing Cheng is from the College of Software at Jilin University, while Yi Chang and Yuan Wu are from the School of Artificial Intelligence at Jilin University. Yi Chang also has an affiliation with the Engineering Research Center of Knowledge-Driven (the full affiliation text appears to be cut off in the search result).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-26T10:22:05.919863+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2403.16952 \"Data Mixing Laws\" authors full list Ye Jiasheng"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2403.16952 \"Data Mixing Laws\" authors full list Ye Jiasheng"
  }
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-26T10:22:05.920002+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2305.13169 Longpre Mahari \"Pretrainer's Guide to Training Data\" 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2305.13169 Longpre Mahari \"Pretrainer's Guide to Training Data\" 2024"
  }
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-26T10:22:05.920130+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DetectGPT Mitchell 2023 arXiv 2301.11305 authors \"Yoonho Lee\" \"Alexander Khazatsky\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DetectGPT Mitchell 2023 arXiv 2301.11305 authors \"Yoonho Lee\" \"Alexander Khazatsky\""
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-26T10:22:05.920251+00:00_

Web search results for query: "arxiv 2403.16952 "Data Mixing Laws" authors full list Ye Jiasheng"

Links: [{"title":"[2403.16952] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/abs/2403.16952"},{"title":"[2403.16952v1] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/abs/2403.16952v1"},{"title":"OpenMOSS Data Mixing Laws: Optimizing Data Mixtures by Predicting","url":"https://arxiv.org/pdf/2403.16952"},{"title":"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/html/2403.16952"},{"title":"GitHub - yegcjs/mixinglaws","url":"https://github.com/yegcjs/mixinglaws"},{"title":"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240316952Y/abstract"},{"title":"R&B: Domain Regrouping and Data Mixture Balancing for Efficient Foundation Model Training","url":"https://arxiv.org/html/2505.00358v1"},{"title":"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training","url":"https://arxiv.org/html/2507.15640"},{"title":"Chameleon: A Flexible Data-mixing Framework for ...","url":"https://arxiv.org/pdf/2505.24844"}]

Based on the search results, here is the full list of authors for the paper "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance" (arXiv 2403.16952):

1. Jiasheng Ye
2. Peiju Liu
3. Tianxiang Sun
4. Yunhua Zhou
5. Jun Zhan
6. Xipeng Qiu


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-26T10:22:05.920387+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2507.15640 \"Data Mixing Agent\" authors Yang Kailai full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2507.15640 \"Data Mixing Agent\" authors Yang Kailai full list"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-26T10:22:05.920513+00:00_

Web search results for query: "arXiv 2305.13169 Longpre Mahari "Pretrainer's Guide to Training Data" 2024"

Links: [{"title":"[2305.13169] A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity","url":"https://arxiv.org/abs/2305.13169"},{"title":"[PDF] A Pretrainer’s Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Pretrainer%E2%80%99s-Guide-to-Training-Data:-Measuring-of-Longpre-Yauney/1567bcac0ab09269c9d0ff33c9a406132417fab9"},{"title":"A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity | Request PDF","url":"https://www.researchgate.net/publication/370949707_A_Pretrainer's_Guide_to_Training_Data_Measuring_the_Effects_of_Data_Age_Domain_Coverage_Quality_Toxicity"},{"title":"A Pretrainer’s Guide to Training Data:","url":"https://arxiv.org/pdf/2305.13169"},{"title":"An archival perspective on pretraining data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/38645763/"},{"title":"A Pretrainer’s Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.179/"},{"title":"Robert Mahari and Shayne Longpre: “Discit ergo est: Training Data Provenance And Fair Use” - Network Law Review","url":"https://www.networklawreview.org/mahari-longpre-generative-ai/"},{"title":"A Pretrainer's Guide to Training Data","url":"https://gyauney.github.io/papers/a-pretrainers-guide_poster.pdf"}]

Based on the search results, I found information about the paper you're looking for:

The paper is titled "A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity" by Shayne Longpre and 10 other authors.

**Publication Details:**
- arXiv ID: 2305.13169, published May 22, 2023
- The paper was published in 2024 in the Proc
…[truncated 1047 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-26T10:22:05.920666+00:00_

Web search results for query: "DetectGPT Mitchell 2023 arXiv 2301.11305 authors "Yoonho Lee" "Alexander Khazatsky""

Links: [{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"title":"(PDF) DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://www.researchgate.net/publication/367461943_DetectGPT_Zero-Shot_Machine-Generated_Text_Detection_using_Probability_Curvature"},{"title":"[2301.11305v2] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305v2"},{"title":"[2301.11305v1] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305v1"},{"title":"GitHub - eric-mitchell/detect-gpt: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature · GitHub","url":"https://github.com/eric-mitchell/detect-gpt"},{"title":"[2301.11305v1] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"http://export.arxiv.org/abs/2301.11305v1"},{"title":"Google Académico","url":"https://scholar.google.com/scholar?q=Eric+Mitchell,+Yoonho+Lee,+Alexander+Khazatsky,+Christopher+D+Manning,+and+Chelsea+Finn.+2023.+DetectGPT:+Zero-Shot+Machine-Generated+Text+Detection+using+Probability+Curvature.+arXiv+preprint+arXiv:2301.11305+(2023)."},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230111305M/abstract"},{"title":"[PDF] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DetectGPT:-Zero-Shot-Machine-Generated-Text-using-Mitchell-Lee/da15ff9f152c14618e4d4987bc98b45fd0e2d0ab"},{"title":"AI-Powered Paper Summarization about the arXiv paper 2301.11305v1","url":"https://www.summari
…[truncated 1231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-26T10:22:05.920819+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lee Ippolito Nystrom Zhang Eck Callison-Burch Carlini \"Deduplicating Training Data Makes Language Models Better\" ACL 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lee Ippolito Nystrom Zhang Eck Callison-Burch Carlini \"Deduplicating Training Data Makes Language Models Better\" ACL 2022"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-26T10:22:05.920962+00:00_

Web search results for query: "arxiv 2507.15640 "Data Mixing Agent" authors Yang Kailai full list"

Links: [{"title":"[2507.15640] Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training","url":"https://arxiv.org/abs/2507.15640"},{"title":"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training","url":"https://arxiv.org/html/2507.15640"},{"title":"Machine Learning Jul 2025","url":"https://www.arxiv.org/list/cs.LG/2025-07?skip=1275&show=50"},{"title":"Artificial Intelligence Jul 2025","url":"https://www.arxiv.org/list/cs.AI/2025-07?skip=2600&show=25"},{"title":"Computation and Language Jul 2025","url":"https://arxiv.org/list/cs.CL/2025-07?skip=1350&show=2000"},{"title":"Computer Science Jul 2025","url":"https://arxiv.org/list/cs/2025-07?skip=3175&show=2000"}]

Based on the search results, the full list of authors for arxiv paper 2507.15640 "Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training" is: Kailai Yang (The University of Manchester), Xiao Liu (Microsoft Research), Lei Ji (Microsoft Research), Hao Li (Imperial College London), Xiao Liang (University of California, Los Angeles), Zhiwei Liu (The University of Manchester), Yeyun Gong (Microsoft Research), Peng Cheng (Microsoft Research), and Mao Yang (Microsoft Research).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-26T10:22:05.921101+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "semanticscholar.org \"The FineWeb Datasets\" Penedo Kydlicek authors full list 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "semanticscholar.org \"The FineWeb Datasets\" Penedo Kydlicek authors full list 2024"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-26T10:22:05.921235+00:00_

Web search results for query: "Lee Ippolito Nystrom Zhang Eck Callison-Burch Carlini "Deduplicating Training Data Makes Language Models Better" ACL 2022"

Links: [{"title":"Deduplicating Training Data Makes Language Models Better - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.577/"},{"title":"[2107.06499] Deduplicating Training Data Makes Language Models Better","url":"https://arxiv.org/abs/2107.06499"},{"title":"Deduplicating Training Data Makes Language Models Better","url":"https://www.cis.upenn.edu/~ccb/publications/deduplicating-training-data-makes-lms-better.pdf"},{"title":"[PDF] Deduplicating Training Data Makes Language Models Better | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deduplicating-Training-Data-Makes-Language-Models-Lee-Ippolito/4566c0d22ebf3c31180066ab23b6c445aeec78d5"},{"title":"[2107.06499] Deduplicating Training Data Makes Language Models Better","url":"https://ar5iv.labs.arxiv.org/html/2107.06499"},{"title":"Deduplicating Training Data Makes Language Models Better | Request PDF","url":"https://www.researchgate.net/publication/361073536_Deduplicating_Training_Data_Makes_Language_Models_Better"},{"title":"[2107.06499v2] Deduplicating Training Data Makes Language Models Better","url":"https://arxiv.org/abs/2107.06499v2"},{"title":"Deduplicating Training Data Makes Language Models Better","url":"https://research.google/pubs/pub51843/"},{"title":"Deduplicating Training Data Makes Language Models Better - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210706499L/abstract"},{"title":"[2107.06499] Deduplicating Training Data Makes Language Models Better","url":"https://arxiv-export1.library.cornell.edu/abs/2107.06499?context=cs.CL"}]

I found the paper you're looking for. Here are the key details:

**Paper Information:**
The paper "Deduplicating Training Data Makes Language Models Better" was written by Katherine Lee, Daphne Ippolito, Andrew Nystrom, Chiyuan Zhang, Douglas Eck, Chris Callison-Burch, and Nic
…[truncated 1048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-26T10:22:05.921398+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv.org 2410.21526 authors Hsun-Yu Kuo Pei-Yu Tan Chao-Wei Peng Yun-Nung Chen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv.org 2410.21526 authors Hsun-Yu Kuo Pei-Yu Tan Chao-Wei Peng Yun-Nung Chen"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-26T10:22:05.921531+00:00_

Web search results for query: "semanticscholar.org "The FineWeb Datasets" Penedo Kydlicek authors full list 2024"

Links: [{"title":"[PDF] The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-FineWeb-Datasets:-Decanting-the-Web-for-the-at-Penedo-Kydl%C3%ADcek/b83a9e35c3aeeb37708e362473c7617d59b815b5"},{"title":"The FineWeb datasets | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738886"},{"title":"dblp: The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale.","url":"https://dblp.org/rec/journals/corr/abs-2406-17557.html"},{"title":"[2406.17557] The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://arxiv.org/abs/2406.17557"},{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://arxiv.org/html/2406.17557v1"},{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/370df50ccfdf8bde18f8f9c2d9151bda-Abstract-Datasets_and_Benchmarks_Track.html"},{"title":"[2406.17557v2] The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://arxiv.org/abs/2406.17557v2"},{"title":"NeurIPS Poster The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://neurips.cc/virtual/2024/poster/97513"},{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://papers.nips.cc/paper_files/paper/2024/hash/370df50ccfdf8bde18f8f9c2d9151bda-Abstract-Datasets_and_Benchmarks_Track.html"},{"title":"[Quick Review] The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://liner.com/review/the-fineweb-datasets-decanting-the-web-for-the-finest-text"}]

Based on my search results, the full list of authors for
…[truncated 497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-26T10:22:05.921677+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2505.09388 Qwen3 full author list Yang An Yang Baosong Zhang Beichen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2505.09388 Qwen3 full author list Yang An Yang Baosong Zhang Beichen"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-26T10:22:05.921864+00:00_

Here are the verification results for all 4 entries.

---

**Entry 1: mitchell2023detectgpt** — ALL CORRECT

| Field | Bib Value | Verified Value | Status |
|-------|-----------|----------------|--------|
| Paper exists | — | Yes | OK |
| Title | "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature" | Exact match | OK |
| Authors | Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea | Exact match | OK |
| Year | 2023 | 2023 | OK |
| Venue | ICML 2023 | ICML 2023 (Proceedings of the 40th ICML) | OK |
| arXiv ID | (not in bib) | 2301.11305 | FYI |

---

**Entry 2: shi2024minkprob** — ALL CORRECT

| Field | Bib Value | Verified Value | Status |
|-------|-----------|----------------|--------|
| Paper exists | — | Yes | OK |
| Title | "Detecting Pretraining Data from Large Language Models" | Exact match | OK |
| Authors | Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke | Exact match | OK |
| Year | 2024 | 2024 | OK |
| Venue | ICLR 2024 | ICLR 2024 (12th International Conference on Learning Representations) | OK |
| arXiv ID | (not in bib) | 2310.16789 | FYI |

---

**Entry 3: alemohammad2024mad** — ALL CORRECT

| Field | Bib Value | Verified Value | Status |
|-------|-----------|----------------|--------|
| Paper exists | — | Yes | OK |
| Title | "Self-Consuming Generative Models Go MAD" | Exact match | OK |
| Authors | Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G. | Exact match | OK |
| Year | 2024 | 2024 | OK |
| Venue | ICLR 2024 | ICLR 2024 (poster presentation) | OK |
| arXiv ID | (not in bib) | 2307.01850 | FYI |

---

**Entry 4: cheng2025contamination** — ALL CORRECT

| Field | Bib Value | Verified Value | Status |
|-------|-----------|----------------|--------|
| Pap
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Agent",
  "elapsed_ms": 9
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-26T10:22:05.922030+00:00_

Web search results for query: "arxiv 2505.09388 Qwen3 full author list Yang An Yang Baosong Zhang Beichen"

Links: [{"title":"[2505.09388] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388"},{"title":"Paper page - Qwen3 Technical Report","url":"https://huggingface.co/papers/2505.09388"},{"title":"[2505.09388] Qwen3 Technical Report - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2505.09388"},{"title":"arXiv:2505.09388v1 [cs.CL] 14 May 2025","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/391741196_Qwen3_Technical_Report"},{"title":"GitHub - bytegoose/arxiv.2505.09388: Qwen3 MoE Model Simplified Implementation following the technical report","url":"https://github.com/bytegoose/arxiv.2505.09388"},{"title":"Qwen/Qwen3-VL-8B-Thinking - Demo - DeepInfra","url":"https://deepinfra.com/Qwen/Qwen3-VL-8B-Thinking"},{"title":"Qwen3 Technical Report (arXiv:2505.09388v1) - ScienceStack","url":"https://www.sciencestack.ai/paper/2505.09388v1"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"}]

Based on the search results, I found information about the Qwen3 Technical Report (arxiv 2505.09388). The full author list includes: An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong Tang, Jian Yang, Jianhong Tu, Jianwei Zhang, and 38 more authors.

The paper was published on May 14, 2025, and describes a collection of open-weight large language models (LLMs) that achieve state-of-the-art performance across a wide variety of tasks and domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-26T10:22:05.922165+00:00_

Web search results for query: "arxiv.org 2410.21526 authors Hsun-Yu Kuo Pei-Yu Tan Chao-Wei Peng Yun-Nung Chen"

Links: [{"title":"[2410.21526] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://arxiv.org/abs/2410.21526"},{"title":"Computer Vision and Pattern Recognition Jun 2025","url":"https://www.arxiv.org/list/cs.CV/2025-06?skip=800&show=2000"},{"title":"Computer Science Jan 2025","url":"https://arxiv.org/list/cs/2025-01?skip=1025&show=2000"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=1575&show=1000"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=2650&show=1000"},{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/"},{"title":"Machine Learning Jul 2025","url":"https://arxiv.org/list/cs.LG/2025-07?skip=1075&show=2000"},{"title":"Snowmass 2021 Computational Frontier CompF03 Topical Group Report:   Machine Learning","url":"https://arxiv.org/pdf/2209.07559"},{"title":"Low-Depth Optical Neural Networks","url":"https://arxiv.org/pdf/1904.02165"}]

Based on the search results, I found the paper you're looking for:

The paper titled "Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification" is authored by Hsun-Yu Kuo and 4 other authors. The paper addresses synthetic data augmentation via large language models (LLMs) for enhancing performance on downstream tasks, especially when real-world data is scarce.

The authors proposed efficient weighted-loss approaches to align synthetic data with real-world distribution by emphasizing high-quality and diversified data generated by LLMs with using merely a little real-world data.

The paper can be found at https://arxiv.org/abs/2410.21526.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-26T10:22:05.922313+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:arxiv.org/abs/2403.16952 \"Ye\" \"Liu\" \"Sun\" \"Zhou\" \"Zhan\" \"Qiu\" author order"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:arxiv.org/abs/2403.16952 \"Ye\" \"Liu\" \"Sun\" \"Zhou\" \"Zhan\" \"Qiu\" author order"
  }
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-26T10:22:05.922445+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2410.21526 full author list \"Yin-Hsiang Liao\" OR \"Pei-Yu Tan\" OR \"Chao-Wei Peng\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2410.21526 full author list \"Yin-Hsiang Liao\" OR \"Pei-Yu Tan\" OR \"Chao-Wei Peng\""
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-26T10:22:05.922567+00:00_

Web search results for query: "site:arxiv.org/abs/2403.16952 "Ye" "Liu" "Sun" "Zhou" "Zhan" "Qiu" author order"

Links: [{"title":"[2403.16952] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/abs/2403.16952"},{"title":"Computer Science Mar 2024","url":"https://arxiv.org/list/cs/2024-03?skip=7065&show=2000"},{"title":"Computer Vision and Pattern Recognition Sep 2024","url":"https://www.arxiv.org/list/cs.CV/2024-09?skip=1320&show=1000"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=2650&show=1000"},{"title":"Computer Vision and Pattern Recognition Apr 2025","url":"https://www.arxiv.org/list/cs.CV/2025-04?skip=1450&show=2000"},{"title":"Computer Vision and Pattern Recognition May 2025","url":"https://www.arxiv.org/list/cs.CV/2025-05?skip=1000&show=500"},{"title":"Computer Vision and Pattern Recognition Jun 2025","url":"https://www.arxiv.org/list/cs.CV/2025-06?skip=1950&show=1000"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1283&show=1000"}]

Based on the search results, I found the information about the paper with arXiv ID 2403.16952. The authors of "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance" are Jiasheng Ye, Peiju Liu, Tianxiang Sun, Jun Zhan, Yunhua Zhou, and Xipeng Qiu.

So the author order is:
1. Jiasheng Ye
2. Peiju Liu
3. Tianxiang Sun
4. Jun Zhan
5. Yunhua Zhou
6. Xipeng Qiu


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-26T10:22:05.922702+00:00_

Web search results for query: "arxiv 2410.21526 full author list "Yin-Hsiang Liao" OR "Pei-Yu Tan" OR "Chao-Wei Peng""

Links: [{"title":"International Conference on Learning Representations 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025"},{"title":"The Design and Technology Development of the JUNO Central Detector","url":"https://arxiv.org/pdf/2311.17314"},{"title":"Mass Testing and Characterization of 20-inch PMTs for JUNO","url":"https://arxiv.org/pdf/2205.08629"},{"title":"Search for the isospin-violating decays $\\boldsymbol{\\chi_{cJ}\\to\\Lambda\\bar{\\Sigma}^{0}+c.c.}$ and $\\boldsymbol{\\eta_{c}\\to\\Lambda\\bar{\\Sigma}^{0}+c.c.}$","url":"https://arxiv.org/pdf/2601.19493"},{"title":"Observation of $\\psi(3686)\\to \\gamma \\eta(1405)$ via $\\eta(1405)\\to f_0(980)\\pi^0$","url":"https://arxiv.org/pdf/2509.09156"},{"title":"Observation of $\\psi(3686)\\to 3\\phi$","url":"https://arxiv.org/pdf/2403.01761"},{"title":"Measurement of $e^{+}e^{-}\\rightarrow\\eta J/\\psi$ Cross Section from   $\\sqrt{s}=$ 3.808 GeV to 4.951 GeV","url":"https://arxiv.org/pdf/2310.03361"}]

Based on the search results, the paper titled "Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification" includes authors Hsun-Yu Kuo, Yin-Hsiang Liao, Yu-Chieh Chao, Wei-Yun Ma, and Pu-Jen Cheng. This appears to be from an ICLR 2025 proceedings page.

However, I should note that the search results don't explicitly show the arXiv ID 2410.21526 or the other two names you mentioned (Pei-Yu Tan and Chao-Wei Peng) in the full author list. To get the complete and accurate author list for that specific arXiv paper, you may want to visit the arXiv page directly at arxiv.org/abs/2410.21526.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-26T10:22:05.922844+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Data Mixing Agent\" ACL 2026 accepted paper Kailai Yang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Data Mixing Agent\" ACL 2026 accepted paper Kailai Yang"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-26T10:22:05.922996+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "semanticscholar.org \"Not All LLM-Generated Data Are Equal\" Kuo authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "semanticscholar.org \"Not All LLM-Generated Data Are Equal\" Kuo authors"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-26T10:22:05.923121+00:00_

Web search results for query: "semanticscholar.org "Not All LLM-Generated Data Are Equal" Kuo authors"

Links: [{"title":"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification. | Semantic Scholar","url":"https://www.semanticscholar.org/search?q=Not+All+LLM-Generated+Data+Are+Equal:+Rethinking+Data+Weighting+in+Text+Classification."},{"title":"[2410.21526] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://arxiv.org/abs/2410.21526"},{"title":"Not All LLM-Generated Data Are Equal: Rethinking data weighting in Text Classification","url":"https://arxiv.org/html/2410.21526v1"},{"title":"Hsun-Yu Kuo - Not All LLM-Generated Data Are Equal","url":"https://www.linkedin.com/posts/hsun-yu-kuo_not-all-llm-generated-data-are-equal-rethinking-activity-7301752160239661056-aSUZ"},{"title":"[2410.21526v1] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://arxiv.org/abs/2410.21526v1"},{"title":"[Literature Review] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://www.themoonlight.io/en/review/not-all-llm-generated-data-are-equal-rethinking-data-weighting-in-text-classification"},{"title":"What Matters in LLM-generated Data: Diversity and Its Effect on Model Fine-Tuning","url":"https://arxiv.org/html/2506.19262"},{"title":"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification | OpenReview","url":"https://openreview.net/forum?id=oI5tZaWkF9"},{"title":"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification | Request PDF","url":"https://www.researchgate.net/publication/385354062_Not_All_LLM-Generated_Data_Are_Equal_Rethinking_Data_Weighting_in_Text_Classification"}]

I found the paper you're looking for! Here are the key details:

**Paper:** "Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification" by Hsun-
…[truncated 826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-26T10:22:05.923274+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:openreview.net \"Not All LLM-Generated Data Are Equal\" Kuo Liao Chao"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:openreview.net \"Not All LLM-Generated Data Are Equal\" Kuo Liao Chao"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-26T10:22:05.923394+00:00_

Web search results for query: ""Data Mixing Agent" ACL 2026 accepted paper Kailai Yang"

Links: [{"title":"Machine Learning Jul 2025","url":"https://www.arxiv.org/list/cs.LG/2025-07?skip=1275&show=50"},{"title":"Mixtera: A Data Plane for Foundation Model Training","url":"https://arxiv.org/pdf/2502.19790"},{"title":"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training","url":"https://arxiv.org/pdf/2507.15640"},{"title":"DaMo: Data Mixing Optimizer in Fine-tuning Multimodal LLMs for Mobile Phone Agents","url":"https://arxiv.org/pdf/2510.19336"},{"title":"Decouple Searching from Training: Scaling Data Mixing via Model Merging for Large Language Model Pre-training","url":"https://arxiv.org/pdf/2602.00747"}]

Based on the search results, I found information about the "Data Mixing Agent" paper:

The paper "Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training" is authored by Kailai Yang, Xiao Liu, Lei Ji, Hao Li, Yeyun Gong, Peng Cheng, and Mao Yang. The paper is indexed on arXiv (2507.15640) and covers topics in Machine Learning, Artificial Intelligence, and Computation and Language.

The research demonstrates that the Data Mixing Agent outperforms strong baselines in continual pre-training on math reasoning, achieving balanced performance across source and target field benchmarks, and generalizes well across unseen source fields, target models, and domain spaces without retraining.

However, I should note that the search results show this as an arXiv preprint (dated July 2025) rather than explicitly confirming it as an accepted ACL 2026 paper. If you need confirmation of its ACL 2026 acceptance status, you may want to check the ACL 2026 conference proceedings directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-26T10:22:05.923530+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL 2026 accepted papers list \"Data Mixing Agent\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL 2026 accepted papers list \"Data Mixing Agent\""
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-26T10:22:05.923654+00:00_

Web search results for query: "site:openreview.net "Not All LLM-Generated Data Are Equal" Kuo Liao Chao"

Links: [{"title":"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification | OpenReview","url":"https://openreview.net/forum?id=oI5tZaWkF9"},{"title":"NOT ALL LLM-GENERATED DATA ARE EQUAL","url":"https://openreview.net/pdf?id=oI5tZaWkF9"},{"title":"[2410.21526] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://arxiv.org/abs/2410.21526"},{"title":"[2410.21526v1] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://arxiv.org/abs/2410.21526v1"},{"title":"Not All LLM-Generated Data Are Equal: Rethinking data weighting in Text Classification","url":"https://arxiv.org/html/2410.21526v1"},{"title":"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification | Request PDF","url":"https://www.researchgate.net/publication/385354062_Not_All_LLM-Generated_Data_Are_Equal_Rethinking_Data_Weighting_in_Text_Classification"},{"title":"Not All Thoughts are Generated Equal: Efficient LLM Reasoning via Synergizing-Oriented Multi-Turn Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=HhmuDEH80X"},{"title":"Hsun-Yu Kuo - Not All LLM-Generated Data Are Equal","url":"https://www.linkedin.com/posts/hsun-yu-kuo_not-all-llm-generated-data-are-equal-rethinking-activity-7301752160239661056-aSUZ"},{"title":"[Literature Review] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://www.themoonlight.io/en/review/not-all-llm-generated-data-are-equal-rethinking-data-weighting-in-text-classification"}]

I found the paper! Here are the search results for "Not All LLM-Generated Data Are Equal" by Kuo, Liao, and Chao:

## Paper Overview

The paper proposes weighted loss approaches for training on data generated by LLMs, addressing synthetic data augmentation via Large L
…[truncated 1084 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-26T10:22:05.923799+00:00_

Web search results for query: "ACL 2026 accepted papers list "Data Mixing Agent""

Links: [{"title":"Accepted Papers - ACL 2026","url":"https://2026.aclweb.org/program/accepted_papers/"},{"title":"Findings of the Association for Computational Linguistics (2026) - ACL Anthology","url":"https://aclanthology.org/events/findings-2026/"},{"title":"21 papers were accepted at ACL 2026 | Center for Advanced Intelligence Project","url":"https://aip.riken.jp/news/acl2026/"},{"title":"Most Influential ACL Papers (2026-03 Version) – Paper Digest","url":"https://www.paperdigest.org/2026/03/most-influential-acl-papers-2026-03-version/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"}]

I found a reference to the ACL 2026 accepted papers page, but the search results don't contain the specific details about a paper titled "Data Mixing Agent." The first result points to the Accepted Main Conference Papers of ACL 2026 at https://2026.aclweb.org/program/accepted_papers/, which should have the complete list of accepted papers.

However, the search results provided don't include the specific paper you're looking for in the snippets returned. To find the "Data Mixing Agent" paper, you would need to visit the official ACL 2026 accepted papers page directly, where you can browse or search for the paper by title.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-26T10:22:05.923966+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclanthology.org \"A Pretrainer's Guide to Training Data\" Longpre NAACL 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclanthology.org \"A Pretrainer's Guide to Training Data\" Longpre NAACL 2024 authors"
  }
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-26T10:22:05.924095+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:2026.aclweb.org \"Data Mixing Agent\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:2026.aclweb.org \"Data Mixing Agent\""
  }
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-26T10:22:05.924221+00:00_

Web search results for query: "aclanthology.org "A Pretrainer's Guide to Training Data" Longpre NAACL 2024 authors"

Links: [{"title":"A Pretrainer's Guide to Training Data","url":"https://aclanthology.org/2024.naacl-long.179.pdf"},{"title":"[2305.13169] A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity","url":"https://arxiv.org/abs/2305.13169"},{"title":"A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity | Request PDF","url":"https://www.researchgate.net/publication/370949707_A_Pretrainer's_Guide_to_Training_Data_Measuring_the_Effects_of_Data_Age_Domain_Coverage_Quality_Toxicity"},{"title":"Data, Data Everywhere: A Guide for Pretraining Dataset Construction","url":"https://arxiv.org/pdf/2407.06380"},{"title":"DataDecide: How to Predict Best Pretraining Data with Small Experiments","url":"https://arxiv.org/pdf/2504.11393"},{"title":"Register Always Matters: Analysis of LLM Pretraining Data Through the Lens of Language Variation","url":"https://arxiv.org/pdf/2504.01542"},{"title":"Data Management For Training Large Language Models: A Survey","url":"https://arxiv.org/pdf/2312.01700"}]

Based on the search results, I found the paper "A Pretrainer's Guide to Training Data" on ACL Anthology. The authors are: Shayne Longpre, Gregory Yauney, Emily Reif, Katherine Lee, Adam Roberts, Barret Zoph, Denny Zhou, Jason Wei, Kevin Robinson, David Mimno, and Daphne Ippolito.

The paper was presented at NAACL 2024 and is available at https://aclanthology.org/2024.naacl-long.179.pdf.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-26T10:22:05.924360+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Pretrainer's Guide to Training Data\" Longpre \"Robert Mahari\" OR \"Gregory Yauney\" full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Pretrainer's Guide to Training Data\" Longpre \"Robert Mahari\" OR \"Gregory Yauney\" full author list"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-26T10:22:05.924483+00:00_

Web search results for query: "site:2026.aclweb.org "Data Mixing Agent""

Links: [{"title":"Tutorials - ACL 2026","url":"https://2026.aclweb.org/program/tutorials/"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"Annual Meetings of the Association for Computational Linguistics | ACL Member Portal","url":"https://www.aclweb.org/portal/acl"},{"title":"EACL 2026 - Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-call-system-demonstrations"},{"title":"Call for Papers: ACL 2026 Workshop on Structured Understanding, Retrieval, and Generation in the LLM Era | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-acl-2026-workshop-structured-understanding-retrieval-and-generation-llm-era"},{"title":"Mixtera: A Data Plane for Foundation Model Training","url":"https://arxiv.org/pdf/2502.19790"},{"title":"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training","url":"https://arxiv.org/pdf/2507.15640"}]

I found a result for "Data Mixing Agent"! The search returned a paper titled "Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training".

The Data Mixing Agent is the first model-based, end-to-end framework that learns to reweight domains, with the agent learning generalizable heuristics through reinforcement learning on large quantities of data mixing trajectories with corresponding feedback from an evaluation environment.

The paper addresses continual pre-training on small-scale task-specific data to improve large language models in new target fields while mitigating catastrophic forgetting, by re-weighting training data mixtures from source and target fields on a domain space to achieve balanced performance. Experiments show that the Data Mixing Agent outperforms strong baselines in achieving balanced performance across source and tar
…[truncated 284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-26T10:22:05.924635+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclanthology.org 2026 \"Data Mixing Agent\" Yang Kailai"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclanthology.org 2026 \"Data Mixing Agent\" Yang Kailai"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-26T10:22:05.924764+00:00_

Web search results for query: ""A Pretrainer's Guide to Training Data" Longpre "Robert Mahari" OR "Gregory Yauney" full author list"

Links: [{"title":"A Pretrainer’s Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.179/"},{"title":"[2305.13169] A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity","url":"https://arxiv.org/abs/2305.13169"},{"title":"A Pretrainer's Guide to Training Data","url":"https://gyauney.github.io/papers/a-pretrainers-slides.pdf"},{"title":"A Pretrainer’s Guide to Training Data:","url":"https://arxiv.org/pdf/2305.13169"},{"title":"A Pretrainer's Guide to Training Data","url":"https://aclanthology.org/2024.naacl-long.179.pdf"},{"title":"dblp: A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity.","url":"https://dblp.org/rec/journals/corr/abs-2305-13169.html"},{"title":"Paper page - A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity","url":"https://huggingface.co/papers/2305.13169"},{"title":"a-pretrainers-guide/A Pretrainer's Guide To Training Data.pdf at main · shayne-longpre/a-pretrainers-guide","url":"https://github.com/shayne-longpre/a-pretrainers-guide/blob/main/A%20Pretrainer's%20Guide%20To%20Training%20Data.pdf"},{"title":"[PDF] A Pretrainer’s Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Pretrainer%E2%80%99s-Guide-to-Training-Data:-Measuring-of-Longpre-Yauney/1567bcac0ab09269c9d0ff33c9a406132417fab9"},{"title":"Gregory Yauney","url":"https://gyauney.github.io/"}]

The full author list for "A Pretrainer's Guide to Training Data" is: Shayne Longpre, Gregory Yauney, Emily Reif, Katherine Lee, Adam Roberts, Barret Zoph, Denny Zhou, Jason Wei, 
…[truncated 152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-26T10:22:05.924928+00:00_

Web search results for query: "aclanthology.org 2026 "Data Mixing Agent" Yang Kailai"

Links: [{"title":"Kailai Yang - ACL Anthology","url":"https://aclanthology.org/people/kailai-yang/"},{"title":"Findings of the Association for Computational Linguistics (2026) - ACL Anthology","url":"https://aclanthology.org/events/findings-2026/"},{"title":"Kailai Yang","url":"https://aclanthology.org/people/k/kailai-yang/"},{"title":"ACL Anthology","url":"https://aclanthology.org/"},{"title":"The AI Committee: A Multi-Agent Framework for Automated ...","url":"https://aclanthology.org/2026.eacl-demo.41.pdf"},{"title":"Navigating the Infinite Dynamic Web Space: Effective In-Context Exploration via Cognitive Multi-Agent Collaboration - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.384/"},{"title":"Aclanthology","url":"https://aclanthology.org/2026.eacl-long.2.pdf"},{"title":"A Multimodal Generalist GUI Agent with Native Reasoning ...","url":"https://aclanthology.org/2026.eacl-long.45.pdf"},{"title":"MAViS: A Multi-Agent Framework for Long-Sequence ...","url":"https://aclanthology.org/2026.eacl-long.101.pdf"},{"title":"19th Conference of the European Chapter of the Association for Computational Linguistics - ACL Anthology","url":"https://aclanthology.org/events/eacl-2026/"}]

I searched for that query on ACL Anthology, but the search results do not contain any papers specifically titled "Data Mixing Agent" by Yang Kailai from 2026. The search returned various 2026 ACL/EACL papers and information about Kailai Yang's other publications, but not the specific paper you're looking for.

It's possible that:
1. The paper title might be slightly different
2. It may not be published yet or indexed on ACL Anthology
3. The author name spelling might be different
4. It could be under a different venue

If you have additional details about the paper (such as the conference/workshop name, alternate spellings, or a different title), I'd be happy to search again.


REMINDER: You MUS
…[truncated 83 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-26T10:22:05.925089+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Data Mixing Agent\" \"Xiao Liang\" OR \"Liang Xiao\" authors arxiv 2507.15640"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Data Mixing Agent\" \"Xiao Liang\" OR \"Liang Xiao\" authors arxiv 2507.15640"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-26T10:22:05.925220+00:00_

Web search results for query: ""Data Mixing Agent" "Xiao Liang" OR "Liang Xiao" authors arxiv 2507.15640"

Links: [{"title":"[2507.15640] Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training","url":"https://arxiv.org/abs/2507.15640"},{"title":"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training","url":"https://arxiv.org/html/2507.15640"},{"title":"Artificial Intelligence Jul 2025","url":"https://www.arxiv.org/list/cs.AI/2025-07?skip=2600&show=25"},{"title":"Machine Learning Jul 2025","url":"https://www.arxiv.org/list/cs.LG/2025-07?skip=1275&show=50"},{"title":"GitHub - Westlake-AI/Awesome-Mixup: [Survey] Awesome List of Mixup Augmentation and Beyond (https://arxiv.org/abs/2409.05202) · GitHub","url":"https://github.com/Westlake-AI/Awesome-Mixup"},{"title":"MixRec: Individual and Collective Mixing Empowers Data Augmentation for Recommender Systems","url":"https://arxiv.org/html/2501.13579v3"},{"title":"[2507.01599] Data Agent: A Holistic Architecture for Orchestrating Data+AI Ecosystems","url":"https://arxiv.org/abs/2507.01599"}]

Based on the search results, I found the paper you're looking for:

**Title:** Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training

**ArXiv ID:** 2507.15640

**Authors:** Kailai Yang, Xiao Liu, Lei Ji, Hao Li, Xiao Liang, Zhiwei Liu, Yeyun Gong, Peng Cheng, Mao Yang

Yes, Xiao Liang is confirmed as one of the authors of this paper. Xiao Liang is affiliated with University of California, Los Angeles.

**Summary:** Data Mixing Agent is the first model-based, end-to-end framework that learns to re-weight domains, learning generalizable heuristics through reinforcement learning on large quantities of data mixing trajectories with corresponding feedback from an evaluation environment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-26T10:22:05.925434+00:00_

Now I have all the information. Here is my complete verification report.

---

## Verification Results

### Entry 1: kuo2024weighting

| Field | Bib Value | Actual | Status |
|-------|-----------|--------|--------|
| Exists | — | Yes | OK |
| Title | "Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification" | Same | OK |
| Authors | Kuo, Hsun-Yu and Tan, Pei-Yu and Peng, Chao-Wei and Chen, Yun-Nung | **Hsun-Yu Kuo, Yin-Hsiang Liao, Yu-Chieh Chao, Wei-Yun Ma, Pu-Jen Cheng** | **WRONG** |
| Year | 2024 | 2024 (posted Oct 28, 2024) | OK |
| Venue | arXiv:2410.21526 | arXiv:2410.21526 (also submitted to ICLR 2025) | OK |
| arXiv ID | 2410.21526 | 2410.21526 | OK |

**Issue:** The author list in the bib entry is completely wrong. The real authors are Hsun-Yu Kuo, Yin-Hsiang Liao, Yu-Chieh Chao, Wei-Yun Ma, and Pu-Jen Cheng. None of "Pei-Yu Tan", "Chao-Wei Peng", or "Yun-Nung Chen" are authors of this paper. Only Hsun-Yu Kuo is correct. This looks like a hallucinated author list.

---

### Entry 2: bengio2009curriculum

| Field | Bib Value | Actual | Status |
|-------|-----------|--------|--------|
| Exists | — | Yes | OK |
| Title | "Curriculum Learning" | Same | OK |
| Authors | Bengio, Yoshua and Louradour, Jerome and Collobert, Ronan and Weston, Jason | Same (accent: Jerome vs Jerome) | OK |
| Year | 2009 | 2009 | OK |
| Venue | ICML 2009 | ICML 2009 (26th International Conference on Machine Learning) | OK |
| arXiv ID | N/A | N/A | OK |

**Status: All correct.** The accent on "Jerome" (should be "Jerome" with accent grave: Jerome) is a minor formatting detail but the name is correct.

---

### Entry 3: radford2019language

| Field | Bib Value | Actual | Status |
|-------|-----------|--------|--------|
| Exists | — | Yes | OK |
| Title | "Language Models are Unsupervised Multitask Learners" | Same | OK |
| Authors | Radford, Alec and Wu, Jeffrey and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya | Same | OK |
| Year |
…[truncated 3700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Agent",
  "elapsed_ms": 10
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-26T10:22:05.925648+00:00_

Now I have all the information needed. Let me compile the verification results.

---

## Verification Results

### Entry 1: ye2025mixing

| Field | Bib Value | Verified Value | Status |
|-------|-----------|---------------|--------|
| Exists | — | Yes | OK |
| Title | "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance" | Same | OK |
| Authors | Ye, Jiasheng and Liu, Peiju and Sun, Tianxiang and **Zhou, Yunhua and Zhan, Jun** and Qiu, Xipeng | Ye, Jiasheng and Liu, Peiju and Sun, Tianxiang and **Zhan, Jun and Zhou, Yunhua** and Qiu, Xipeng | **ERROR: author order swapped** |
| Year | 2025 | 2025 | OK |
| Venue | ICLR 2025 | ICLR 2025 (conference paper) | OK |
| arXiv | not in bib | 2403.16952 | (info only) |

**Issue:** The bib has "Zhou, Yunhua and Zhan, Jun" (positions 4-5), but arXiv lists "Jun Zhan" before "Yunhua Zhou" (i.e., Zhan is 4th, Zhou is 5th). The author order should be: Ye, Jiasheng and Liu, Peiju and Sun, Tianxiang and **Zhan, Jun and Zhou, Yunhua** and Qiu, Xipeng.

---

### Entry 2: yang2026mixing

| Field | Bib Value | Verified Value | Status |
|-------|-----------|---------------|--------|
| Exists | — | Yes | OK |
| Title | "Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training" | Same | OK |
| Authors | Yang, Kailai and Liu, Xiao and Ji, Lei and Li, Hao and **Liang, Xiao** and Liu, Zhiwei and Gong, Yeyun and Cheng, Peng and Yang, Mao | Same | OK |
| Year | 2026 | arXiv posted July 2025; ACL 2026 acceptance not confirmed via ACL Anthology | **UNCERTAIN** |
| Venue | ACL 2026 | arXiv 2507.15640 confirmed; ACL 2026 acceptance could not be independently confirmed on ACL Anthology (proceedings may not yet be indexed) | **UNCERTAIN** |
| arXiv | not in bib | 2507.15640 | (info only) |

**Notes:** The paper exists on arXiv (2507.15640, July 2025). The ACL 2026 accepted papers page exists at `2026.aclweb.org/program/accepted_papers/` but I could not confirm this specific paper's listing via web 
…[truncated 2132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "Agent",
  "elapsed_ms": 12
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-26T10:22:05.925834+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2410.21526 \"Not All LLM-Generated Data Are Equal\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2410.21526 \"Not All LLM-Generated Data Are Equal\" authors"
  }
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-26T10:22:05.925983+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2305.13169 \"Pretrainer's Guide to Training Data\" authors Longpre"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2305.13169 \"Pretrainer's Guide to Training Data\" authors Longpre"
  }
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-26T10:22:05.926103+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2403.16952 \"Data Mixing Laws\" Ye Jiasheng author order"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2403.16952 \"Data Mixing Laws\" Ye Jiasheng author order"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-26T10:22:05.926251+00:00_

Web search results for query: "arXiv 2305.13169 "Pretrainer's Guide to Training Data" authors Longpre"

Links: [{"title":"[2305.13169] A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity","url":"https://arxiv.org/abs/2305.13169"},{"title":"A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity | Request PDF","url":"https://www.researchgate.net/publication/370949707_A_Pretrainer's_Guide_to_Training_Data_Measuring_the_Effects_of_Data_Age_Domain_Coverage_Quality_Toxicity"},{"title":"[PDF] A Pretrainer’s Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Pretrainer%E2%80%99s-Guide-to-Training-Data:-Measuring-of-Longpre-Yauney/1567bcac0ab09269c9d0ff33c9a406132417fab9"},{"title":"A Pretrainer’s Guide to Training Data:","url":"https://arxiv.org/pdf/2305.13169"},{"title":"An archival perspective on pretraining data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/38645763/"},{"title":"A Pretrainer’s Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.179/"},{"title":"A Pretrainer's Guide to Training Data","url":"https://gyauney.github.io/papers/a-pretrainers-guide_poster.pdf"},{"title":"dblp: A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity.","url":"https://dblp.org/rec/journals/corr/abs-2305-13169.html"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** A Pretrainer's Guide to Training Data: Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity

**Authors:** Shayne Longpre, Gregory Yauney, Emily Reif, Katherine Lee, Adam Roberts, Barret Zoph, Denny Zhou, Jason Wei, Kevin Robinson, David Mimno, Daphne Ippolito

**Publication Details
…[truncated 534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-26T10:22:05.926408+00:00_

Web search results for query: "arXiv 2410.21526 "Not All LLM-Generated Data Are Equal" authors"

Links: [{"title":"[2410.21526] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://arxiv.org/abs/2410.21526"},{"title":"Not All LLM-Generated Data Are Equal: Rethinking data weighting in Text Classification","url":"https://arxiv.org/html/2410.21526v1"},{"title":"Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification | Request PDF","url":"https://www.researchgate.net/publication/385354062_Not_All_LLM-Generated_Data_Are_Equal_Rethinking_Data_Weighting_in_Text_Classification"},{"title":"[2410.21526v1] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://arxiv.org/abs/2410.21526v1"},{"title":"[Literature Review] Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification","url":"https://www.themoonlight.io/en/review/not-all-llm-generated-data-are-equal-rethinking-data-weighting-in-text-classification"},{"title":"Under the Surface: Tracking the Artifactuality of LLM-Generated Data","url":"https://arxiv.org/pdf/2401.14698"},{"title":"The LLM Data Auditor: A Metric-oriented Survey on Quality and Trustworthiness in Evaluating Synthetic Data","url":"https://arxiv.org/pdf/2601.17717"},{"title":"Gen-Review: A Large-scale Dataset of AI-Generated (and Human-written) Peer Reviews","url":"https://arxiv.org/pdf/2510.21192"}]

The authors of arXiv 2410.21526 "Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification" are Hsun-Yu Kuo, Yin-Hsiang Liao, Yu-Chieh Chao, Wei-Yun Ma, and Pu-Jen Cheng.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-26T10:22:05.926561+00:00_

Web search results for query: "arXiv 2403.16952 "Data Mixing Laws" Ye Jiasheng author order"

Links: [{"title":"[2403.16952] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/abs/2403.16952"},{"title":"[2403.16952v1] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/abs/2403.16952v1"},{"title":"OpenMOSS Data Mixing Laws: Optimizing Data Mixtures by Predicting","url":"https://arxiv.org/pdf/2403.16952"},{"title":"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/html/2403.16952"},{"title":"GitHub - yegcjs/mixinglaws","url":"https://github.com/yegcjs/mixinglaws"},{"title":"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240316952Y/abstract"},{"title":"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training","url":"https://arxiv.org/html/2507.15640"},{"title":"R&B: Domain Regrouping and Data Mixture Balancing for Efficient Foundation Model Training","url":"https://arxiv.org/html/2505.00358v1"}]

Based on the search results, I can provide you with information about the authorship and author order of this paper:

The paper "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance" has authors in the following order: Ye, Jiasheng; Liu, Peiju; Sun, Tianxiang; Zhou, Yunhua; Zhan, Jun; and Qiu, Xipeng.

So Jiasheng Ye is the first author on this arXiv paper 2403.16952.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-26T10:22:05.926722+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv.org 2403.16952 Data Mixing Laws authors Ye Liu Sun",
  "allowed_domains": "['arxiv.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv.org 2403.16952 Data Mixing Laws authors Ye Liu Sun",
    "allowed_domains": "['arxiv.org']"
  }
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-26T10:22:05.926860+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Data Mixing Agent\" \"Learning to Re-weight Domains\" Yang Kailai ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Data Mixing Agent\" \"Learning to Re-weight Domains\" Yang Kailai ACL 2026"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-26T10:22:05.927002+00:00_

Web search results for query: ""Data Mixing Agent" "Learning to Re-weight Domains" Yang Kailai ACL 2026"

Links: [{"title":"[2507.15640] Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training","url":"https://arxiv.org/abs/2507.15640"},{"title":"Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training","url":"https://arxiv.org/html/2507.15640v1"},{"title":"[2604.07963v1] Rethinking Data Mixing from the Perspective of Large Language Models","url":"https://arxiv.org/abs/2604.07963v1"},{"title":"To Mix or To Merge: Toward Multi-Domain Reinforcement Learning for Large Language Models","url":"https://arxiv.org/html/2602.12566"},{"title":"[2604.07963] Rethinking Data Mixing from the Perspective of Large Language Models","url":"https://arxiv.org/abs/2604.07963"},{"title":"Rethinking Data Mixing from the Perspective of Large Language Models","url":"https://arxiv.org/html/2604.07963v1"},{"title":"Yang Liu's Homepage at Tsinghua University","url":"https://nlp.csai.tsinghua.edu.cn/~ly/pub.html"}]

Based on the search results, I found information about the paper you're looking for:

Data Mixing Agent is the first model-based, end-to-end framework that learns to re-weight domains. The paper addresses continual pre-training on small-scale task-specific data as an effective method for improving large language models in new target fields, yet it risks catastrophic forgetting of their original capabilities.

The common solution is to re-weight training data mixtures from source and target fields on a domain space to achieve balanced performance. Previous domain reweighting strategies rely on manual designation with certain heuristics based on human intuition or empirical results.

The agent learns generalizable heuristics through reinforcement learning on large quantities of data mixing trajectories with corresponding feedback from an evaluation environment.

The paper appears on arXiv (paper ID: 2507.15640) and was authored by Kailai Yang and 
…[truncated 265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-26T10:22:05.927167+00:00_

Web search results for query: "arxiv.org 2403.16952 Data Mixing Laws authors Ye Liu Sun"

Links: [{"title":"[2403.16952] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/abs/2403.16952"},{"title":"OpenMOSS Data Mixing Laws: Optimizing Data Mixtures by Predicting","url":"https://arxiv.org/pdf/2403.16952"},{"title":"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/html/2403.16952"},{"title":"[2403.16952v1] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/abs/2403.16952v1"},{"title":"Rethinking Data Mixing from the Perspective of Large Language Models","url":"https://arxiv.org/html/2604.07963v1"},{"title":"Scaling Laws for Optimal Data Mixtures","url":"https://arxiv.org/html/2507.09404v1"},{"title":"R&B: Domain Regrouping and Data Mixture Balancing for Efficient Foundation Model Training","url":"https://arxiv.org/html/2505.00358v1"},{"title":"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models","url":"https://arxiv.org/html/2508.11953"},{"title":"RegMix: Data Mixture as Regression for Language Model Pre-training","url":"https://arxiv.org/html/2407.01492v1"},{"title":"Chameleon: A Flexible Data-mixing Framework for ...","url":"https://arxiv.org/pdf/2505.24844"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance"

**Authors:** Jiasheng Ye, Peiju Liu, Tianxiang Sun, Yunhua Zhou, Jun Zhan, and Xipeng Qiu

**Paper Summary:** The paper discovers the quantitative predictability of model performance regarding mixture proportions in function forms, referred to as "data mixing laws." Fitting such functions on sample mixtures unveils model performance on unseen mixtures before actual runs, thus guiding the selection of an ideal data mixture.

**arXiv 
…[truncated 200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref-verify-group2_20260526T101557",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 151 · 2026-05-26T10:22:05.927411+00:00_

The arXiv page confirms author order for ye2025mixing as "Yunhua Zhou, Jun Zhan" — matching the bib. The agent was wrong on that one. Now I have all the data. Here's the full report:

---

## 引用验证结果（Group 2: Entry 20–37）

```
[20] xie2023doremi — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (NeurIPS 2023)
  arXiv: N/A (2305.10429 可选添加)
  引用上下文: OK — related_work.tex L10 引用 domain-level importance sampling，正确

[21] xie2023dsir — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (NeurIPS 2023)
  arXiv: N/A (2302.03169 可选添加)
  引用上下文: OK — related_work.tex L10 引用 domain-level importance sampling，正确

[22] chen2025aioli — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICLR 2025)
  arXiv: N/A (2411.05735 可选添加)
  引用上下文: 未在正文中引用（orphaned bib entry）

[23] kimura2024iw — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (TMLR 2024)
  arXiv: N/A (2403.10175 可选添加)
  引用上下文: 未在正文中引用（orphaned bib entry）

[24] mitchell2023detectgpt — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICML 2023)
  arXiv: N/A (2301.11305 可选添加)
  引用上下文: OK — related_work.tex L9 引用 probability curvature detector，正确

[25] shi2024minkprob — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICLR 2024)
  arXiv: N/A (2310.16789 可选添加)
  引用上下文: OK — related_work.tex L9 引用 low-probability token statistics，正确

[26] alemohammad2024mad — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICLR 2024)
  arXiv: N/A (2307.01850 可选添加)
  引用上下文: OK — related_work.tex L3 引用 Model Autophagy Disorder，正确

[27] cheng2025contamination — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (arXiv:2502.14425)
  arXiv: OK (2502.14425)
  引用上下文: OK — introduction.tex L1, related_work.tex L5, method.tex L8 引用 synthetic 20-60% 估计，正确

[28] ye2025mixing — ✅
  标题: OK
  作者: OK（arXiv 确认顺序为 Zhou, Yunhua → Zhan, Jun，与 bib 一致）
  年份: OK
  Venue: OK (ICLR 2025)
  arXiv: N/A (2403.16952 可选添加)
  引用上下文: OK — related_work.tex L10/L20, discussion.tex L31 引用 data mixing laws 和 PPL-to-accuracy transfer，正确

[29] yang2026mixing — ⚠️
  标题: OK
  作者: OK
  年份: OK
  Venue: ⚠️ ACL 2026 尚未召开（当前 2026-05-26），venue 无法独立确认
  arXiv: N/A (2507.15640 可选添加)
  引用上下文: 未在正文中引用（orphaned bib entry）

[30] penedo2024fineweb — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (NeurIPS Datasets and Benchmarks 2024)
  arXiv: N/A (2406.17557 可选添加)
  引用上下文: OK — experiments.tex L2 引用 FineWeb 作为 real-data source，正确

[31] yang2025qwen3 — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (arXiv:2505.09388)
  arXiv: OK (2505.09388)
  引用上下文: OK — experiments.tex L3 引用 Qwen3-0.6B 作为 generator，正确

[32] kuo2024weighting — ❌
  标题: OK
  作者: ❌ 除首作者外全部错误。Bib: "Tan, Pei-Yu; Peng, Chao-Wei; Chen, Yun-Nung"
        实际: Kuo, Hsun-Yu; Liao, Yin-Hsiang; Chao, Yu-Chieh; Ma, Wei-Yun; Cheng, Pu-Jen
  年份: OK
  Venue: OK (arXiv:2410.21526)
  arXiv: OK (2410.21526)
  引用上下文: 未在正文中引用（orphaned bib entry）

[33] bengio2009curriculum — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ICML 2009)
  arXiv: N/A
  引用上下文: OK — related_work.tex L10 引用 instance-level curriculum learning，正确

[34] radford2019language — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (OpenAI Blog 2019)
  arXiv: N/A
  引用上下文: 未在正文中引用（orphaned bib entry）

[35] brown2020language — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (NeurIPS 2020)
  arXiv: N/A (2005.14165 可选添加)
  引用上下文: 未在正文中引用（orphaned bib entry）

[36] longpre2024pretrainers — ❌
  标题: OK
  作者: ❌ 第二作者起全部错误。Bib: "Mahari, Robert; Lee, Naana Obeng-Marnu; others"
        实际: Longpre, Shane; Yauney, Gregory; Reif, Emily; Lee, Katherine; Roberts, Adam;
              Zoph, Barret; Zhou, Denny; Wei, Jason; Robinson, Kevin; Mimno, David; Ippolito, Daphne
  年份: OK
  Venue: ⚠️ 应为 NAACL 2024（已发表于 ACL Anthology 2024.naacl-long.179），非仅 arXiv preprint
  arXiv: OK (2305.13169)
  引用上下文: 未在正文中引用（orphaned bib entry）

[37] lee2022dedup — ✅
  标题: OK
  作者: OK
  年份: OK
  Venue: OK (ACL 2022)
  arXiv: N/A (2107.06499 可选添加)
  引用上下文: 未在正文中引用（orphaned bib entry）
```

---

## 汇总

| | 数量 |
|---|---|
| 总数 | 18 |
| ✅ OK | 15 |
| ❌ 有问题 | 2 |
| ⚠️ 待确认 | 1 |

### 必须修复

| # | Key | 问题 | 修复方案 |
|---|-----|------|---------|
| 32 | `kuo2024weighting` | **作者列表伪造**（仅首作者正确） | 改为: `Kuo, Hsun-Yu and Liao, Yin-Hsiang and Chao, Yu-Chieh and Ma, Wei-Yun and Cheng, Pu-Jen` |
| 36 | `longpre2024pretrainers` | **作者列表伪造**（仅首作者正确）+ venue 应升级 | 作者改为: `Longpre, Shane and Yauney, Gregory and Reif, Emily and Lee, Katherine and Roberts, Adam and Zoph, Barret and Zhou, Denny and Wei, Jason and Robinson, Kevin and Mimno, David and Ippolito, Daphne`；venue 改为 `NAACL 2024`，类型改为 `@inproceedings` |

### 待确认

| # | Key | 问题 |
|---|-----|------|
| 29 | `yang2026mixing` | ACL 2026 尚未召开，venue 无法独立验证。论文本身存在（arXiv:2507.15640）。建议确认接收通知后再标注 venue |

### 额外发现：8 条 orphaned entries

以下 entry 存在于 `references.bib` 但正文中未引用：`chen2025aioli`, `kimura2024iw`, `yang2026mixing`, `kuo2024weighting`, `radford2019language`, `brown2020language`, `longpre2024pretrainers`, `lee2022dedup`。如果最终不引用，应在提交前删除以免 LaTeX warning。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_ref-verify-group2_20260526T101557"
}
```

</details>

---
