# audit paper consistency

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_audit_paper-consistency_20260516T022243.jsonl`
- **Structured JSON:** [`78f73521e5efab3feb74.json`](../../sessions/78/78f73521e5efab3feb74.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-16T02:28:12.369057+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T02:28:12.369454+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T02:28:12.369741+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T02:28:12.369999+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T02:28:12.370224+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T02:28:12.370536+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T02:28:12.370784+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T02:28:12.371047+00:00_

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
…[truncated 9093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T02:28:12.371274+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T02:28:12.371465+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T02:28:12.371686+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T02:28:12.371929+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All six generators are base (pretrained) models.
5	Web text is predominantly produced by instruction-tuned and RLHF-aligned models, whose generation distributions differ from base model continuations.
6	Preliminary instruct experiments show substantial depth-signal degradation: OLMo-2-1B-Instruct drops to 3-class LOGO F1\,=\,0.338 (vs.\ 0.764 for base OLMo-2-1B) and Qwen3-0.6B with chat template to F1\,=\,0.667 (vs.\ 0.816 base).
7	Length-controlled analysis reveals that the effect of instruct tuning on surface features is model-dependent: Qwen models retain weakly positive TTR and hapax partial correlations with depth, while OLMo-Instruct exhibits negative correlations similar to base models.
8	By contrast, entropy-based depth signals consistently reverse sign across all three instruct models (partial $\rho$ ranging from +0.103 to +0.364), suggesting a genuine behavioral change that persists after controlling for output length.
9	Disentangling architecture-dependent surface effects from the robust entropy reversal in instruct-tuned generation is a critical direction for future work.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale, but cross-scale classifier transfer incurs a moderate gap (held-out F1\,=\,0.683 vs.\ 0.76--0.86 for $\leq$2.8B generators).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	We evaluate three prompt types (continuation, elaboration, rewriting; Appendix~\ref{app:prompt-type}) but all share the same Pythia-2.8B generator.
16	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms the depth signal generalizes, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\times$ cross-prompt interactions remain untested.
17	
18	Our primary evaluation uses single-generator chains; cross-model chains (\S\ref{sec:results-classificat
…[truncated 1642 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T02:28:12.372176+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T02:28:12.372476+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T02:28:12.372748+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T02:28:12.373034+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T02:28:12.373303+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T02:28:12.373551+00:00_

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
…[truncated 1422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T02:28:12.373809+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T02:28:12.374007+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T02:28:12.374209+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table4.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T02:28:12.374417+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T02:28:12.374645+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/_project/paper/appendix_*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/_project/paper/appendix_*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T02:28:12.374874+00:00_

artifacts/_project/paper/appendix_length.tex
artifacts/_project/paper/appendix_prompt_type.tex
artifacts/_project/paper/appendix_confusion_matrix.tex
artifacts/_project/paper/appendix_lofo.tex
artifacts/_project/paper/appendix_human_edit.tex
artifacts/_project/paper/appendix_classifier.tex
artifacts/_project/paper/appendix_finer_depth.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T02:28:12.375079+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T02:28:12.375313+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T02:28:12.375548+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T02:28:12.375814+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T02:28:12.376059+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_prompt_type.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T02:28:12.376275+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T02:28:12.376504+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T02:28:12.376765+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T02:28:12.377016+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T02:28:12.377251+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T02:28:12.377480+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T02:28:12.377734+00:00_

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
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T02:28:12.378189+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T02:28:12.378424+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T02:28:12.378736+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper-number-audit-20260516",
  "type": "report",
  "description": "论文全文数字一致性审计报告：逐文件检查所有定量声明与实验数据的一致性",
  "project": "gen-depth-fingerprint",
  "tags": "['paper', 'audit', 'consistency']",
  "content_filename": "paper_number_audit_20260516.md",
  "content": "# 论文全文数字一致性审计报告\n\n**审计日期**: 2026-05-16\n**审计范围**: abstract.tex, introduction.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, method.tex, related_work.tex, table4.tex, ethics.tex, appendix_finer_depth.tex, appendix_classifier.tex, appendix_human_edit.tex, appendix_prompt_type.tex, appendix_length.tex, appendix_lofo.tex, appendix_confusion_matrix.tex\n\n---\n\n## 审计结果\n\n### CRITICAL（必须修复）\n\n无。\n\n### WARNING（建议修复）\n\n- **[results.tex:30]** \"best single-model ceiling (Pythia-1B, 0.862)\" — 主 LOGO 表 (Table 1) 中 Pythia-1B held-out F1 = **0.856**，0.862 不在 ground truth 中。该数字可能来自 cross-model chain 的 5-fold stratified CV 对照实验，但论文未说明来源，且 0.862 恰好落在 LOGO CI 上界 [0.843, 0.863] 附近，有误用 CI 端点作点估计的嫌疑。**建议**：确认 0.862 的来源，若为 5-fold CV 则标注 \"(5-fold CV)\"；若为笔误则改为 0.856。\n\n- **[discussion.tex:67, limitations.tex:6]** Instruct 实验中 base Qwen3-0.6B 对比值写作 F1=0.816，但主 LOGO 表 (Table 1) 中同一模型 held-out F1 = **0.824**。差异原因是 instruct 实验可能使用了不同 reference model（Qwen3-0.6B 自身作 ref 时整体 LOGO F1=0.816，见 Table cross-ref），但论文未解释此差异。读者对比 Table 1 (0.824) 与此处 (0.816) 会产生疑惑。**建议**：在 instruct 讨论段落中加一句说明，或统一引用同一评估设置下的数字。\n\n- **[discussion.tex:69, limitations.tex:8]** Entropy 特征在 instruct 模型上 \"reverse sign\" 的措辞。项目叙事规范要求使用 \"depth signal degradation\" / \"method boundary\" 叙事而非 \"方向反转\"。当前文本标题已采用 \"degrades depth signal\" 叙事（合规），但正文中多次使用 \"reverse sign\"、\"reversal\" 等词汇。**建议**：将 \"reverse sign\" 改为 \"shift to positive\"，\"reversal\" 改为 \"sign change\" 或 \"weakening/degradation of the negative correlation\"，避免暗示系统性方向反转。\n\n### INFO（信息备注）\n\n- **[appendix_human_edit.tex:22-27]** 表格内舍入不一致：Random 20% 行显示 Binary F1 从 0.724→0.717（差 0.7pp），但 Δ 列写 −0.8pp（从未舍入值 0.7241→0.7165=0.76pp 四舍五入而来）。LLM rephrase 行类似：0.724→0.662=6.2pp，但 Δ 列写 −6.3pp。这是 \"从原始值计算 Δ\" vs \"从显示值计算 Δ\" 的经典舍入问题。不影响正确性，但严谨读者可能注意到。\n\n- **[discussion.tex:9, limitations.tex:27]** \"degrades at extreme temperatures (t=1.0, −6pp)\" — 实际 3-class 降幅为 6.2pp (0.788→0.726)，binary 为 6.6pp (0.799→0.733)。\"~6pp\" 是合理的近似值。\n\n- **[appendix_classifier.tex:44-47]** Sampling ablation 的 default config 3-class F1=0.788，而主结果报告 0.789。差异 (0.001) 来自数据重新生成，属预期行为。\n\n- **[appendix_human_edit.tex:22]** Human edit baseline binary F1=0.724（从 0.7241 舍入），而主结果 primary binary F1=0.723。两者来自不同实验流程，差异合理，但读者可能疑惑为何同一 baseline 在不同表中有微小差异。\n\n- **[results.tex:30]** Cross-model chain 比较中 single-model ceiling 使用 5-fold stratified CV（0.862），而 Table 1 使用 LOGO（0.856），两种评估协议不同。建议在文中明确标注评估协议以避免混淆。\n\n---\n\n## 逐文件核查清单\n\n### abstract.tex ✅\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| Binary F1 | 0.723 | 0.723 | ✓ |\n| 95% CI | [0.717, 0.729] | [0.717, 0.729] | ✓ |\n| Per-gen std | 0.051 | 0.051 | ✓ |\n| 6 generators, 3 families, 0.6B-8.2B | — | — | ✓ |\n\n### introduction.tex ✅\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| Binary F1 (×3处) | 0.723 | 0.723 | ✓ |\n| 95% CI (×3处) | [0.717, 0.729] | [0.717, 0.729] | ✓ |\n| Per-gen std (×2处) | 0.051 | 0.051 | ✓ |\n| PPL random vs depth | 2.367 vs 2.387 | 2.367 vs 2.387 | ✓ |\n| Per-gen F1 range (baselines) | 0.42–0.81 | 与 per-gen 详细数据一致 | ✓ |\n\n### results.tex ✅ (1 WARNING)\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| 3-class LOGO F1 | 0.789 | 0.789 | ✓ |\n| Binary F1 | 0.723 | 0.723 | ✓ |\n| Per-gen F1 (6个) | 0.856/0.804/0.764/0.824/0.806/0.683 | 全部匹配 | ✓ |\n| Per-class F1 | 0.94/0.64/0.80 | 0.94/0.64/0.80 | ✓ |\n| LOFO F1 (3个) | 0.772/0.762/0.754, Δ=-2.6pp | 全部匹配 | ✓ |\n| Cross-model chains | 3c=0.809, bin=0.764 | 0.809/0.764 | ✓ |\n| Ordinal: CORAL/FH/XGB | 0.771/0.793/0.789; bin 0.721/0.728; conc 0.821/0.810/0.825 | 全部匹配 | ✓ |\n| Spearman (5个) | -0.558/-0.542/-0.475/0.076/0.089 | 全部匹配 | ✓ |\n| Ablation: full/surface/ref | 0.789/0.729/0.745 | 全部匹配 | ✓ |\n| Top importance: hapax | 0.269 | 0.269 | ✓ |\n| Cross-ref (3个) | 0.803/0.807/0.816, spread=0.013 | 全部匹配 | ✓ |\n| Baselines (7行×3列) | 全部数字 | 全部匹配 | ✓ |\n| Baseline Δ计算 (4个) | +1.1/+2.2/+10.7/+19.9pp | 算术正确 | ✓ |\n| Downstream PPL (5行) | 2.335/2.367/2.387/2.389/2.681 | 全部匹配 | ✓ |\n| ⚠ Single-model ceiling | 0.862 | 真值 LOGO=0.856 | WARNING |\n\n### discussion.tex ✅ (2 WARNING)\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| Sampling robustness | ≤0.3pp, -6pp | 0.3pp, ~6.2pp | ✓ (近似) |\n| 5-class drop | 0.789→0.501, Δ=0.288 | 0.501 | ✓ |\n| 5-class per-class (gen2/3/4) | 0.268/0.259/0.423 | 全部匹配 | ✓ |\n| Alt classifiers | RF 0.476, LR 0.447, FH 0.451 | 全部匹配 | ✓ |\n| Human edit 20% | -6.0pp 3c, ≤0.8pp bin | -5.97pp/-0.76pp | ✓ |\n| LLM rephrase | -3.4pp 3c, -6.3pp bin | -3.4pp/-6.26pp | ✓ |\n| Multi-det ensemble | 0.805 vs 0.789; 0.723 vs 0.724 | 全部匹配 | ✓ |\n| Cross-ref spread | 0.013, range 0.803-0.816 | 匹配 | ✓ |\n| Pythia-1B cross-family | 0.845-0.848 | 0.845-0.848 | ✓ |\n| Instruct OLMo | 0.338 vs 0.764 | 匹配 | ✓ |\n| Instruct Qwen3-0.6B | 0.667 vs 0.816 | 匹配 | ⚠ 见WARNING |\n| Entropy partial ρ | +0.103/+0.161/+0.364 | 全部匹配 | ✓ |\n\n### conclusion.tex ✅\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| Binary F1 + CI + std | 0.723/[0.717,0.729]/0.051 | 全部匹配 | ✓ |\n| Cross-model | 3c=0.809, bin=0.764 | 匹配 | ✓ |\n\n### limitations.tex ✅ (同 discussion WARNING)\n所有数字与 discussion 一致，instruct 对比值同上 WARNING。\n\n### method.tex ✅\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| Cross-ref spread | 0.013 | 0.013 | ✓ |\n| Seed stability | mean=0.789, std=0.0009 | mean 匹配 | ✓ |\n| Ordinal range | 0.771-0.793 vs 0.789 | 匹配 | ✓ |\n\n### related_work.tex ✅\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| Baseline binary range | 0.52-0.71 | 0.524-0.712 | ✓ |\n\n### appendix_finer_depth.tex ✅\n5-class avg 0.501±0.038、per-class 0.921/0.634/0.268/0.259/0.423、alt classifiers 全部匹配。\n\n### appendix_human_edit.tex ✅ (INFO: 舍入)\nBaseline/delta 全部匹配 ground truth 原始值；delta 列有轻微舍入不一致（见 INFO）。\n\n### appendix_classifier.tex + sampling ✅\nXGBoost/RF/LR 全部匹配；sampling ablation 3×3 全部匹配。\n\n### 其他附录 (prompt_type, length, lofo, confusion_matrix, ethics) ✅\n无 ground truth 冲突，内部一致。\n\n---\n\n## 总结\n\n**通过（有条件）**。\n\n- **0 个 CRITICAL 问题**\n- **3 个 WARNING**：(1) Pythia-1B 0.862 来源不明；(2) Instruct Qwen3-0.6B base 对比值 0.816 vs LOGO 表 0.824 未解释；(3) instruct \"reverse sign\" 措辞与叙事规范的兼容性\n- **5 个 INFO**：均为轻微舍入近似，不影响结论\n\n所有主要指标（binary F1=0.723、3-class F1=0.789、CI、std、baseline 全表、downstream PPL、ablation、cross-ref、LOFO、5-class、human edit delta）均与 ground truth 完全一致或在合理舍入范围内。无 7-gen vs 6-gen 混用、无不支持的 \"significantly\" 声明。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper-number-audit-20260516",
    "type": "report",
    "description": "论文全文数字一致性审计报告：逐文件检查所有定量声明与实验数据的一致性",
    "project": "gen-depth-fingerprint",
    "tags": "['paper', 'audit', 'consistency']",
    "content_filename": "paper_number_audit_20260516.md",
    "content": "# 论文全文数字一致性审计报告\n\n**审计日期**: 2026-05-16\n**审计范围**: abstract.tex, introduction.tex, results.tex, discussion.tex, conclusion.tex, limitations.tex, method.tex, related_work.tex, table4.tex, ethics.tex, appendix_finer_depth.tex, appendix_classifier.tex, appendix_human_edit.tex, appendix_prompt_type.tex, appendix_length.tex, appendix_lofo.tex, appendix_confusion_matrix.tex\n\n---\n\n## 审计结果\n\n### CRITICAL（必须修复）\n\n无。\n\n### WARNING（建议修复）\n\n- **[results.tex:30]** \"best single-model ceiling (Pythia-1B, 0.862)\" — 主 LOGO 表 (Table 1) 中 Pythia-1B held-out F1 = **0.856**，0.862 不在 ground truth 中。该数字可能来自 cross-model chain 的 5-fold stratified CV 对照实验，但论文未说明来源，且 0.862 恰好落在 LOGO CI 上界 [0.843, 0.863] 附近，有误用 CI 端点作点估计的嫌疑。**建议**：确认 0.862 的来源，若为 5-fold CV 则标注 \"(5-fold CV)\"；若为笔误则改为 0.856。\n\n- **[discussion.tex:67, limitations.tex:6]** Instruct 实验中 base Qwen3-0.6B 对比值写作 F1=0.816，但主 LOGO 表 (Table 1) 中同一模型 held-out F1 = **0.824**。差异原因是 instruct 实验可能使用了不同 reference model（Qwen3-0.6B 自身作 ref 时整体 LOGO F1=0.816，见 Table cross-ref），但论文未解释此差异。读者对比 Table 1 (0.824) 与此处 (0.816) 会产生疑惑。**建议**：在 instruct 讨论段落中加一句说明，或统一引用同一评估设置下的数字。\n\n- **[discussion.tex:69, limitations.tex:8]** Entropy 特征在 instruct 模型上 \"reverse sign\" 的措辞。项目叙事规范要求使用 \"depth signal degradation\" / \"method boundary\" 叙事而非 \"方向反转\"。当前文本标题已采用 \"degrades depth signal\" 叙事（合规），但正文中多次使用 \"reverse sign\"、\"reversal\" 等词汇。**建议**：将 \"reverse sign\" 改为 \"shift to positive\"，\"reversal\" 改为 \"sign change\" 或 \"weakening/degradation of the negative correlation\"，避免暗示系统性方向反转。\n\n### INFO（信息备注）\n\n- **[appendix_human_edit.tex:22-27]** 表格内舍入不一致：Random 20% 行显示 Binary F1 从 0.724→0.717（差 0.7pp），但 Δ 列写 −0.8pp（从未舍入值 0.7241→0.7165=0.76pp 四舍五入而来）。LLM rephrase 行类似：0.724→0.662=6.2pp，但 Δ 列写 −6.3pp。这是 \"从原始值计算 Δ\" vs \"从显示值计算 Δ\" 的经典舍入问题。不影响正确性，但严谨读者可能注意到。\n\n- **[discussion.tex:9, limitations.tex:27]** \"degrades at extreme temperatures (t=1.0, −6pp)\" — 实际 3-class 降幅为 6.2pp (0.788→0.726)，binary 为 6.6pp (0.799→0.733)。\"~6pp\" 是合理的近似值。\n\n- **[appendix_classifier.tex:44-47]** Sampling ablation 的 default config 3-class F1=0.788，而主结果报告 0.789。差异 (0.001) 来自数据重新生成，属预期行为。\n\n- **[appendix_human_edit.tex:22]** Human edit baseline binary F1=0.724（从 0.7241 舍入），而主结果 primary binary F1=0.723。两者来自不同实验流程，差异合理，但读者可能疑惑为何同一 baseline 在不同表中有微小差异。\n\n- **[results.tex:30]** Cross-model chain 比较中 single-model ceiling 使用 5-fold stratified CV（0.862），而 Table 1 使用 LOGO（0.856），两种评估协议不同。建议在文中明确标注评估协议以避免混淆。\n\n---\n\n## 逐文件核查清单\n\n### abstract.tex ✅\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| Binary F1 | 0.723 | 0.723 | ✓ |\n| 95% CI | [0.717, 0.729] | [0.717, 0.729] | ✓ |\n| Per-gen std | 0.051 | 0.051 | ✓ |\n| 6 generators, 3 families, 0.6B-8.2B | — | — | ✓ |\n\n### introduction.tex ✅\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| Binary F1 (×3处) | 0.723 | 0.723 | ✓ |\n| 95% CI (×3处) | [0.717, 0.729] | [0.717, 0.729] | ✓ |\n| Per-gen std (×2处) | 0.051 | 0.051 | ✓ |\n| PPL random vs depth | 2.367 vs 2.387 | 2.367 vs 2.387 | ✓ |\n| Per-gen F1 range (baselines) | 0.42–0.81 | 与 per-gen 详细数据一致 | ✓ |\n\n### results.tex ✅ (1 WARNING)\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| 3-class LOGO F1 | 0.789 | 0.789 | ✓ |\n| Binary F1 | 0.723 | 0.723 | ✓ |\n| Per-gen F1 (6个) | 0.856/0.804/0.764/0.824/0.806/0.683 | 全部匹配 | ✓ |\n| Per-class F1 | 0.94/0.64/0.80 | 0.94/0.64/0.80 | ✓ |\n| LOFO F1 (3个) | 0.772/0.762/0.754, Δ=-2.6pp | 全部匹配 | ✓ |\n| Cross-model chains | 3c=0.809, bin=0.764 | 0.809/0.764 | ✓ |\n| Ordinal: CORAL/FH/XGB | 0.771/0.793/0.789; bin 0.721/0.728; conc 0.821/0.810/0.825 | 全部匹配 | ✓ |\n| Spearman (5个) | -0.558/-0.542/-0.475/0.076/0.089 | 全部匹配 | ✓ |\n| Ablation: full/surface/ref | 0.789/0.729/0.745 | 全部匹配 | ✓ |\n| Top importance: hapax | 0.269 | 0.269 | ✓ |\n| Cross-ref (3个) | 0.803/0.807/0.816, spread=0.013 | 全部匹配 | ✓ |\n| Baselines (7行×3列) | 全部数字 | 全部匹配 | ✓ |\n| Baseline Δ计算 (4个) | +1.1/+2.2/+10.7/+19.9pp | 算术正确 | ✓ |\n| Downstream PPL (5行) | 2.335/2.367/2.387/2.389/2.681 | 全部匹配 | ✓ |\n| ⚠ Single-model ceiling | 0.862 | 真值 LOGO=0.856 | WARNING |\n\n### discussion.tex ✅ (2 WARNING)\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| Sampling robustness | ≤0.3pp, -6pp | 0.3pp, ~6.2pp | ✓ (近似) |\n| 5-class drop | 0.789→0.501, Δ=0.288 | 0.501 | ✓ |\n| 5-class per-class (gen2/3/4) | 0.268/0.259/0.423 | 全部匹配 | ✓ |\n| Alt classifiers | RF 0.476, LR 0.447, FH 0.451 | 全部匹配 | ✓ |\n| Human edit 20% | -6.0pp 3c, ≤0.8pp bin | -5.97pp/-0.76pp | ✓ |\n| LLM rephrase | -3.4pp 3c, -6.3pp bin | -3.4pp/-6.26pp | ✓ |\n| Multi-det ensemble | 0.805 vs 0.789; 0.723 vs 0.724 | 全部匹配 | ✓ |\n| Cross-ref spread | 0.013, range 0.803-0.816 | 匹配 | ✓ |\n| Pythia-1B cross-family | 0.845-0.848 | 0.845-0.848 | ✓ |\n| Instruct OLMo | 0.338 vs 0.764 | 匹配 | ✓ |\n| Instruct Qwen3-0.6B | 0.667 vs 0.816 | 匹配 | ⚠ 见WARNING |\n| Entropy partial ρ | +0.103/+0.161/+0.364 | 全部匹配 | ✓ |\n\n### conclusion.tex ✅\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| Binary F1 + CI + std | 0.723/[0.717,0.729]/0.051 | 全部匹配 | ✓ |\n| Cross-model | 3c=0.809, bin=0.764 | 匹配 | ✓ |\n\n### limitations.tex ✅ (同 discussion WARNING)\n所有数字与 discussion 一致，instruct 对比值同上 WARNING。\n\n### method.tex ✅\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| Cross-ref spread | 0.013 | 0.013 | ✓ |\n| Seed stability | mean=0.789, std=0.0009 | mean 匹配 | ✓ |\n| Ordinal range | 0.771-0.793 vs 0.789 | 匹配 | ✓ |\n\n### related_work.tex ✅\n| 声明 | 论文值 | 真值 | 状态 |\n|------|--------|------|------|\n| Baseline binary range | 0.52-0.71 | 0.524-0.712 | ✓ |\n\n### appendix_finer_depth.tex ✅\n5-class avg 0.501±0.038、per-class 0.921/0.634/0.268/0.259/0.423、alt classifiers 全部匹配。\n\n### appendix_human_edit.tex ✅ (INFO: 舍入)\nBaseline/delta 全部匹配 ground truth 原始值；delta 列有轻微舍入不一致（见 INFO）。\n\n### appendix_classifier.tex + sampling ✅\nXGBoost/RF/LR 全部匹配；sampling ablation 3×3 全部匹配。\n\n### 其他附录 (prompt_type, length, lofo, confusion_matrix, ethics) ✅\n无 ground truth 冲突，内部一致。\n\n---\n\n## 总结\n\n**通过（有条件）**。\n\n- **0 个 CRITICAL 问题**\n- **3 个 WARNING**：(1) Pythia-1B 0.862 来源不明；(2) Instruct Qwen3-0.6B base 对比值 0.816 vs LOGO 表 0.824 未解释；(3) instruct \"reverse sign\" 措辞与叙事规范的兼容性\n- **5 个 INFO**：均为轻微舍入近似，不影响结论\n\n所有主要指标（binary F1=0.723、3-class F1=0.789、CI、std、baseline 全表、downstream PPL、ablation、cross-ref、LOFO、5-class、human edit delta）均与 ground truth 完全一致或在合理舍入范围内。无 7-gen vs 6-gen 混用、无不支持的 \"significantly\" 声明。\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T02:28:12.379123+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_c94dd3\", \"name\": \"paper-number-audit-20260516\", \"type\": \"report\", \"description\": \"论文全文数字一致性审计报告：逐文件检查所有定量声明与实验数据的一致性\", \"path\": \"projects/gen-depth-fingerprint/artifacts/_project/report/paper_number_audit_20260516.md\", \"url\": null, \"project\": \"gen-depth-fingerprint\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T02:28:01.242921+00:00\", \"tags\": [\"paper\", \"audit\", \"consistency\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper-consistency_20260516T022243",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-16T02:28:12.379410+00:00_

## 审计结果

**通过（有条件）** — 0 CRITICAL / 3 WARNING / 5 INFO

### WARNING（建议修复）

1. **results.tex:30** — `"best single-model ceiling (Pythia-1B, 0.862)"` 与 LOGO 表中 Pythia-1B=**0.856** 不符。0.862 来源不明（疑为 5-fold CV 或 CI 上界误用），需确认或修正。

2. **discussion.tex:67 + limitations.tex:6** — Instruct 对比中 base Qwen3-0.6B=**0.816**，但 LOGO 表中同一模型=**0.824**。差异源于不同 reference model 设置（cross-ref Qwen3-0.6B=0.816），但论文未解释，读者会困惑。

3. **discussion.tex:69 + limitations.tex:8** — "reverse sign" 措辞与叙事规范（应用 "degradation" 而非 "方向反转"）存在张力。建议改为 "shift to positive" 或 "sign change"。

### INFO

- appendix_human_edit 表 delta 列有轻微舍入不一致（从原始值 vs 显示值计算 delta 的经典问题）
- Sampling ablation default 3-class=0.788 vs 主结果 0.789（数据重生成所致）
- "~6pp" 近似值（实际 6.2-6.6pp）

其余所有主要数字（binary F1、CI、std、baseline 全表、downstream PPL、ablation、cross-ref、LOFO、5-class、human edit）均与 ground truth 完全一致。报告已注册为 `art_20260516_c94dd3`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_paper-consistency_20260516T022243"
}
```

</details>

---
