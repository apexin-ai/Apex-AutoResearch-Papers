# Research conversation: In /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/, read the following files 

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac60bb2420338e251.jsonl`
- **Structured JSON:** [`0e8c9d4f4bc3200f9178.json`](../../sessions/0e/0e8c9d4f4bc3200f9178.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-25T19:40:59.756Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/, read the following files completely and extract EVERY number that appears (F1 scores, percentages, effect sizes, sample counts, model parameters, GPU hours, etc.):

1. abstract.tex
2. introduction.tex
3. method.tex
4. results.tex
5. discussion.tex
6. conclusion.tex
7. limitations.tex

For each number found, note:
- The exact value
- Which file and approximate line
- What it represents (e.g., "binary F1", "Cohen's d", "sample size")
- Whether it also appears in other sections (cross-references)

Be exhaustive - don't skip any numbers. Include model parameter counts, dataset sizes, confidence intervals, everything.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9d60d394-a874-4281-aae5-d0919e91a07f",
  "agentId": "ac60bb2420338e251",
  "type": "user",
  "uuid": "58faa1cc-a363-467a-a8e8-c0a571de55aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T19:41:01.892Z_

I'll read all seven files completely and extract every number with its context and cross-references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58faa1cc-a363-467a-a8e8-c0a571de55aa",
  "isSidechain": true,
  "agentId": "ac60bb2420338e251",
  "requestId": "req_011CbPrbPWp8Au6usDsuvybZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "15fc4dd7-62c8-4fc4-832d-6676ba46bf1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013TrSEkJjdMPDTiGr6Nwo3U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 615,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T19:41:02.102Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EkJtJBWFFVHXfkhZYpp5PR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15fc4dd7-62c8-4fc4-832d-6676ba46bf1e",
  "isSidechain": true,
  "agentId": "ac60bb2420338e251",
  "requestId": "req_011CbPrbPWp8Au6usDsuvybZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4e8440f3-2e8e-482a-8bea-23e133ac2607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013TrSEkJjdMPDTiGr6Nwo3U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 615,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T19:41:02.111Z_

<details><summary>↩ Tool result · `toolu_01EkJtJBWFFVHXfkhZYpp5PR`</summary>

```text
1	% Abstract — Depth Profiling of Recursive LLM Generation Chains
2	\begin{abstract}
3	As large language model (LLM) outputs re-enter training corpora and seed further generation, understanding how recursive generation reshapes text distributions is critical for data provenance and corpus curation. Existing detectors answer only the binary human-or-machine question, ignoring \emph{generation depth}; we introduce \emph{depth profiling} to address this gap.
4	We decompose distributional drift under recursive generation into location and shape components. Across eight base-model generators from five families, negative log-likelihood (NLL) location features drift monotonically with depth (effect size $d{=}0.74$--$1.05$) while three shape features remain near-stationary ($d < 0.10$), with entropy std intermediate ($d{=}0.46$). We term this ${\geq}8{\times}$ effect-size gap the \emph{differential depth response} (DDR).
5	Prior work documents \emph{what converges}; the central finding here is \emph{what is approximately preserved}: shape stability complements location drift for ordinal depth grading without per-generator calibration. A lightweight ensemble achieves leak-free binary F1\,=\,0.694 (gen-1 vs.\ gen-2+) and 3-class F1\,=\,0.762 under 8-generator leave-one-generator-out evaluation; cross-model chains (5 generators) reach binary F1\,=\,0.830 (gen-0 seeds shared across generators; \S\ref{sec:generation}).
6	Instruction tuning compresses DDR and bounds current applicability to base models\footnote{Code and data are available at \url{https://anonymous.4open.science/r/gen-depth-fingerprint-3FB3/}.}.
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e8440f3-2e8e-482a-8bea-23e133ac2607",
  "isSidechain": true,
  "promptId": "9d60d394-a874-4281-aae5-d0919e91a07f",
  "agentId": "ac60bb2420338e251",
  "type": "user",
  "uuid": "3ba9409b-d6df-4156-9fb8-7b8be1da9d1b",
  "sourceToolAssistantUUID": "4e8440f3-2e8e-482a-8bea-23e133ac2607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T19:41:02.349Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A2TD4UeEg2fryevtS87wJv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ba9409b-d6df-4156-9fb8-7b8be1da9d1b",
  "isSidechain": true,
  "agentId": "ac60bb2420338e251",
  "requestId": "req_011CbPrbPWp8Au6usDsuvybZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "670b24f4-8380-4012-97e6-553a303d62a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013TrSEkJjdMPDTiGr6Nwo3U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 615,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T19:41:02.355Z_

<details><summary>↩ Tool result · `toolu_01A2TD4UeEg2fryevtS87wJv`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1 An estimated 7--17\% of recent scientific publications already contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}. As these outputs re-enter training corpora \cite{dolma,fineweb} and seed further generation, text accumulates at varying \emph{generation depths}; each successive cycle reshapes distributional properties in ways that matter for data provenance, corpus auditing, and contamination monitoring in base-model pretraining corpora \cite{ccnet,dsir} as well as model collapse analysis \cite{curse_of_recursion,strong_model_collapse}. Understanding \emph{how} recursive generation alters text distributions, and which properties change versus which are preserved, is therefore a prerequisite for principled corpus curation, yet current methods address only binary human-or-machine detection \cite{detectgpt,fast_detectgpt,binoculars,ld_score}.
5	Base models provide the cleanest substrate to isolate depth effects from alignment-induced changes.
6	We find that recursive generation produces a decomposable depth profile: distributional \emph{location} drifts with depth while \emph{shape} remains stable across generators, an asymmetry sufficient for cross-generator depth prediction.
7	
8	\looseness=-1 Distributional compression under recursive generation is well-documented \cite{curious_decline,broken_telephone,markovian_chains}, yet existing analyses characterize \emph{that} and \emph{why} convergence occurs without decomposing what drifts from what is preserved.
9	We introduce \emph{depth profiling} (coarse ordinal classification into gen-0\,/\,gen-1\,/\,gen-2+), and decompose this compression into structurally distinct components: across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy\footnote{Throughout, ``entropy'' denotes per-token NLL under the reference model (Pythia-410M), not information-theoretic entropy; see \S\ref{sec:features}.}, lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) remains ${\geq}8{\times}$ more stable (effect size $d{=}0.74$--$1.05$ vs.\ $d < 0.10$ for three near-stationary features; entropy std is intermediate at $d{=}0.46$; boundary features show additional nuance; convergent effect-size measures confirm this partition).
10	We term this location/shape asymmetry the \emph{differential depth response} (DDR; Figure~\ref{fig:ddr-trajectory}), an empirical regularity of base-model autoregressive generation that is mechanistically distinct from model collapse \cite{curse_of_recursion}. Model collapse erodes tail coverage via weight updates; DDR instead analyzes fixed-parameter inference chains.
11	The stationary shape component complements location drift for depth prediction without per-generator calibration.
12	
13	\begin{figure*}[t!]
14	\centering
15	\includegraphics[width=\textwidth]{fig_ddr_trajectory.pdf}
16	\caption{Feature trajectories across generation depth ($y$-axis: $z$-scored feature values). \textbf{Top row (drifting)}: entropy mean and hapax ratio decline monotonically across all eight generators ($|\rho| > 0.59$). \textbf{Bottom row (stationary)}: entropy max and tail decay remain flat ($|\rho| < 0.07$). Colored lines: individual generators; diamonds: cross-generator mean (red for drifting, blue for stationary). This dichotomy defines the DDR.}
17	\label{fig:ddr-trajectory}
18	\end{figure*}
19	We focus on base (pretrained) models; instruction tuning degrades depth signal (Appendix~\ref{app:instruct}).
20	Figure~\ref{fig:framework} summarizes the pipeline: recursive generation chains (\S\ref{sec:generation}), feature extraction with DDR partitioning (\S\ref{sec:features}), and leave-one-generator-out evaluation (\S\ref{sec:evaluation}).
21	
22	\looseness=-1 As a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\,=\,0.694 (macro-averaged LOGO; pooled: 0.705), matching multi-detector ensembles (0.708) at ${\sim}2.4\times$ lower cost; an end-to-end QLoRA \cite{qlora} (Quantized Low-Rank Adaptation) classifier reaches 3-class F1\,=\,0.905 (within-model 5-fold CV; Appendix~\ref{app:qlora}), and the depth signal thus extends well beyond handcrafted features.
23	
24	Our contributions:
25	\begin{enumerate}[nosep,leftmargin=*]
26	    \item \textbf{Empirical decomposition (DDR).} Across eight generators from five families, we decompose inference-chain drift into two primary response zones (drifting, $d{=}0.74$--$1.05$; near-stationary, $d < 0.10$) plus one intermediate feature ($d{=}0.46$). Where prior work documents \emph{what converges} \cite{curious_decline,markovian_chains}, DDR identifies \emph{what is approximately preserved}, an empirical regularity with analytical utility for depth classification without per-generator calibration. DDR is a descriptive empirical finding; the classification value lies in this decomposition rather than the classifier itself.
27	    \item \textbf{Task formulation and evaluation suite.} We define generation depth classification as an ordinal prediction task and construct a controlled dataset of 37K texts from eight generators across five families (0.6B--8B; exploratory evidence extends to 14B, Appendix~\ref{app:9gen-scale}), with leave-one-generator-out cross-validation as the primary evaluation protocol.
28	    \item \textbf{Scope characterization.} Systematic evaluation across temperature, prompt type, instruction tuning, model scale, domain transfer, and perturbation robustness maps the operational envelope of depth profiling.
29	\end{enumerate}
30	
31	\begin{figure*}[t]
32	\centering
33	\includegraphics[width=\textwidth]{fig2_framework.pdf}
34	\caption{Depth profiling pipeline. (a)~Human seeds are iteratively fed through generator $G$ to produce chains of increasing depth. (b)~Seven features extracted from NLL distributions group into three DDR zones: drifting (red), intermediate (purple), near-stationary (blue). (c)~LOGO evaluation holds out one generator for testing.}
35	\label{fig:framework}
36	\end{figure*}
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "670b24f4-8380-4012-97e6-553a303d62a8",
  "isSidechain": true,
  "promptId": "9d60d394-a874-4281-aae5-d0919e91a07f",
  "agentId": "ac60bb2420338e251",
  "type": "user",
  "uuid": "25b1bbce-dda1-4e9c-add5-84efd32d4dc1",
  "sourceToolAssistantUUID": "670b24f4-8380-4012-97e6-553a303d62a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T19:41:02.529Z_

<details open><summary>🔧 Tool call — Read · `toolu_013qtwh2ggmUEJrueduZNahR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25b1bbce-dda1-4e9c-add5-84efd32d4dc1",
  "isSidechain": true,
  "agentId": "ac60bb2420338e251",
  "requestId": "req_011CbPrbPWp8Au6usDsuvybZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "59c974b0-989f-44c1-a7dd-e1728aae40b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013TrSEkJjdMPDTiGr6Nwo3U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 615,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T19:41:02.539Z_

<details><summary>↩ Tool result · `toolu_013qtwh2ggmUEJrueduZNahR`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{table}[t!]
5	\centering
6	\footnotesize
7	\caption{Seven distributional features. ``Entropy'' features are per-token NLL under Pythia-410M (\S\ref{sec:features}); surface features require no reference model. DDR analysis (\S\ref{sec:results-differential}) reveals entropy mean, TTR, and hapax ratio drift with depth while entropy max, min, and tail decay remain near-stationary; entropy std is intermediate.}
8	\label{tab:features}
9	\setlength{\tabcolsep}{4pt}
10	\begin{tabular}{@{}llp{3.0cm}@{}}
11	\toprule
12	\textbf{Feature} & \textbf{Source} & \textbf{Measures} \\
13	\midrule
14	\texttt{entropy\_mean} \textit{\scriptsize(NLL)} & Ref.\ NLL & Central tendency of token surprise \\
15	\texttt{entropy\_std} \textit{\scriptsize(NLL)}  & Ref.\ NLL & Spread of token surprise \\
16	\texttt{entropy\_max} \textit{\scriptsize(NLL)}  & Ref.\ NLL & Maximum token surprise \\
17	\texttt{entropy\_min} \textit{\scriptsize(NLL)}  & Ref.\ NLL & Minimum token surprise \\
18	\texttt{tail\_decay}   & Ref.\ NLL & Log-prob decay slope (ranks 100--1K) \\
19	\midrule
20	\texttt{ttr}           & Surface & Type-token ratio \\
21	\texttt{hapax\_ratio}  & Surface & Proportion of hapax legomena \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\subsection{Task Formulation}
27	\label{sec:task}
28	
29	Given a text $x$, we predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$: human-written ($d{=}0$), first-generation LLM output ($d{=}1$), or text produced by two or more recursive LLM generations ($d{=}2{+}$).
30	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$ (human corpus), $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic autoregressive generation.
31	Depths beyond 2 are merged into $2{+}$ because feature convergence compresses inter-class margins at deeper levels (\S\ref{sec:results-differential}).
32	
33	\subsection{Generation Chain Construction}
34	\label{sec:generation}
35	
36	\looseness=-1 We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
37	\looseness=-1 These span a 13$\times$ parameter range (0.6B--8B) across five architectures; Qwen's overrepresentation (3/8) is a limitation mitigated by LOFO (F1\,=\,0.686; \S\ref{sec:results-classification}).
38	
39	\looseness=-1 For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
40	The same seed pool serves as gen-0 for all generators, controlling for input content; in LOGO evaluation this creates a potential train--test overlap for gen-0, addressed by our binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
41	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
42	We generate up to depth~4 to empirically confirm convergence: 5-class LOGO yields macro F1\,$\approx$\,0.50, with depths 2--4 near-indistinguishable (gen-2/gen-3 per-class F1\,$<$\,0.27; Appendix~\ref{app:finer-depth}). This motivates the gen-2+ class collapse.
43	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
44	After filtering chain breaks and passages too short for feature extraction, 37{,}058 texts remain across all depths (Appendix~\ref{app:dataset-stats}); depths 2--4 are collapsed into $2{+}$.
45	
46	\subsection{Feature Extraction}
47	\label{sec:features}
48	
49	\paragraph{Terminology.} Throughout this paper, we refer to per-token cross-entropy loss under a fixed reference model as ``entropy'' for conciseness; these are reference-model NLL values, not true information-theoretic entropy of the generating distribution.
50	
51	We use interpretable distributional statistics so that the DDR partition remains transparent; end-to-end neural features improve classification ($+$10.0\,pp; Appendix~\ref{app:qlora}) but obscure the decomposition (LOFO confirms both feature groups contribute independently; Appendix~\ref{app:lofo}).
52	
53	\looseness=-1 We extract seven distributional features per text (Table~\ref{tab:features}), covering the NLL distribution's location, spread, extremes, and tail structure, plus two reference-free surface diversity measures; six additional NLL statistics were rejected for redundancy ($|r| > 0.65$, $\Delta$F1\,$\leq$\,$-0.011$; Appendix~\ref{app:feature-candidate}).
54	
55	\paragraph{Reference-model features.}
56	\looseness=-1 A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
57	Cross-family reference validation (Appendix~\ref{app:cross-ref}) shows F1 spread of only 0.013 across Pythia, OLMo, and Qwen references, so DDR is reference-model agnostic; however, all tested references are causal LMs.
58	From the resulting NLL sequence, we extract five statistics: mean, standard deviation, maximum, and minimum of the token-level NLL, plus tail\_decay (the slope of the vocabulary-level averaged log-probability distribution in ranks 100--1000), which captures the power-law regime where depth-induced compression is most detectable.
59	
60	\paragraph{Surface features.}
61	Two features capture lexical diversity without requiring a reference model: type-token ratio (TTR) and the proportion of words appearing exactly once (hapax\_ratio).
62	
63	\paragraph{Feature complementarity.}
64	These features exhibit a \emph{differential depth response} (DDR), separating into drifting and non-drifting groups (\S\ref{sec:results-differential}; pairwise correlations in Appendix~\ref{sec:appendix-feature-correlation}).
65	TTR and hapax ratio are strongly correlated ($r = 0.97$); both are retained for marginal LOFO gains.
66	
67	\subsection{Evaluation Protocol}
68	\label{sec:evaluation}
69	
70	\paragraph{Cross-validation.}
71	\looseness=-1 We evaluate generalization via \textbf{Leave-One-Generator-Out (LOGO)} cross-validation: each fold holds out one generator entirely, so the classifier must generalize to a generator absent from training. This constitutes the strictest per-model protocol for assessing deployment against previously unseen generators.
72	LOGO does not isolate family-level effects; \textbf{Leave-One-Family-Out (LOFO)} addresses this by holding out entire model families (binary F1\,=\,0.686; \S\ref{sec:results-classification}).
73	Generator subsets vary across experiments (Appendix~\ref{app:gen-subsets-section}).
74	
75	\paragraph{Classifier.}
76	\looseness=-1 We use XGBoost \cite{xgboost} throughout ($n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, learning rate $0.1$; fixed without tuning), with identical hyperparameters across all methods in Table~\ref{tab:baselines}.
77	Alternative classifiers (CORAL \cite{coral_ordinal}, CORN \cite{corn_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance (Appendix~\ref{app:classifier}); hyperparameter sensitivity (max\_depth sweep) shows F1 variation $\leq$2.0\,pp, so discriminative power resides in the features, not the classifier.
78	
79	\paragraph{Metrics and statistical testing.}
80	The primary metric is \textbf{macro-averaged F1} over the three depth classes, with 95\% bootstrap confidence intervals (CIs; $n{=}1{,}000$).
81	All $p$-values are two-sided with Bonferroni correction within each family of simultaneous tests.
82	
83	\paragraph{Baselines.}
84	We compare the 7-feature ensemble against four single-score detection methods repurposed as depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
85	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation to ensure a controlled comparison.
86	
87	\paragraph{Length confound control.}
88	Since TTR and hapax\_ratio are mechanically length-dependent, we verify depth signal is not a length artifact via length-matched subsampling that equalizes length distributions across depth classes (\S\ref{sec:results-classification}; Appendix~\ref{app:length}).
89	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59c974b0-989f-44c1-a7dd-e1728aae40b5",
  "isSidechain": true,
  "promptId": "9d60d394-a874-4281-aae5-d0919e91a07f",
  "agentId": "ac60bb2420338e251",
  "type": "user",
  "uuid": "72e3a2dc-9603-4985-aa2b-c1167f124494",
  "sourceToolAssistantUUID": "59c974b0-989f-44c1-a7dd-e1728aae40b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T19:41:02.744Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RhtWXeSY9hyEUvWqu2A6FV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72e3a2dc-9603-4985-aa2b-c1167f124494",
  "isSidechain": true,
  "agentId": "ac60bb2420338e251",
  "requestId": "req_011CbPrbPWp8Au6usDsuvybZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1b461f34-472a-4660-95e6-8f7a88bc5f26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013TrSEkJjdMPDTiGr6Nwo3U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 615,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T19:41:02.749Z_

<details><summary>↩ Tool result · `toolu_01RhtWXeSY9hyEUvWqu2A6FV`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{fig_transfer_heatmap.pdf}
7	\caption{Cross-generator $8{\times}8$ transfer matrix (binary F1, gen-1 vs.\ gen-2+). Mean cross-generator F1\,=\,0.810 [95\% CI: 0.796, 0.822]; uniformly high off-diagonal values confirm depth signal transfers across five families without calibration.}
8	\label{fig:transfer-heatmap}
9	\end{figure}
10	
11	\subsection{Depth Classification Performance}
12	\label{sec:results-classification}
13	
14	\looseness=-1 The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}); cross-generator F1 spread of 9.1\,pp captures generator selection uncertainty.
15	This 3-class metric is inflated by shared gen-0 seeds (per-class gen-0 F1\,$\approx$\,0.94; \S\ref{sec:generation}); we therefore report \textbf{leak-free binary F1} (gen-1 vs.\ gen-2+)\,=\,0.694 (CI [0.688, 0.700]) throughout, excluding gen-0 entirely.
16	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B; std.\ dev.\ 0.028), with the primary difficulty at the gen-1\,/\,gen-2+ boundary (Appendix~\ref{app:confusion}).
17	
18	\paragraph{Cross-model generalization.}
19	\looseness=-1 Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]; Appendix~\ref{app:cross-model-detail}) under 5-generator LOGO.\footnote{Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B; generator-level LOGO with bootstrap CIs ($n$\,=\,1{,}000).}
20	Single-generator transfer confirms the signal is not a mixed-chain artifact (mean transfer F1\,=\,0.810, Figure~\ref{fig:transfer-heatmap}; full $8{\times}8$ matrix: Appendix~\ref{app:transfer}; LOFO\,=\,0.686); analysis of variance (ANOVA) confirms generator identity contributes ${<}1$\% of feature variance ($\eta^2_{\text{gen}} \leq 0.009$; Appendix~\ref{app:cross-model-detail}).
21	A scale effect emerges: smaller models achieve higher F1 (Pythia-2.8B: 0.724 vs.\ Mistral-7B: 0.633), partly due to same-family affinity with the Pythia-410M reference (spread $\leq$0.013; \S\ref{sec:results-differential}).
22	An end-to-end QLoRA classifier reaches 3-class F1\,=\,0.905 (within-model 5-fold CV; $+$10.0\,pp; Appendix~\ref{app:qlora}), evidence that additional depth signal resides in token-level representations. On instruct data, QLoRA recovers to 0.89--0.91 (within-model; Appendix~\ref{app:instruct}); the decomposition, not the classifier, is DDR's primary contribution.
23	
24	\paragraph{Confound controls.}
25	\looseness=-1 Length-matched subsampling yields binary F1\,=\,0.724 (vs.\ 0.770; Appendix~\ref{app:length}); independent-seed evaluation with disjoint pools (F1\,=\,0.680; Appendix~\ref{app:seed-control}), so the classifier captures generative degradation rather than seed-specific content.
26	
27	\paragraph{Error analysis.}
28	\looseness=-1 The gen-1\,/\,gen-2+ boundary is the primary failure point: depth-2 samples (the shallowest within the 2+ class) exhibit the highest error rate (48.4\%), decreasing monotonically to 20.3\% at depth-4 (Appendix~\ref{app:error-analysis}) due to insufficient accumulated drift beyond the large gen-0$\to$gen-1 distributional shift.
29	Error rates decrease monotonically at deeper generations ($\leq$29.2\% at gen-3+); DDR signal thus strengthens with chain length, and the DDR decomposition is the primary analytical contribution.
30	
31	\begin{table}[t]
32	\centering
33	\footnotesize
34	\caption{8-generator LOGO macro-F1 (bootstrap 95\% CIs, $n$\,=\,1{,}000). Binary F1 excludes gen-0. $^{\dagger}$3-class F1 has upward bias from shared gen-0 seeds; independent-seed controls confirm the signal (F1\,=\,0.680; Appendix~\ref{app:seed-control}).}
35	\label{tab:logo-results}
36	\resizebox{\columnwidth}{!}{%
37	\begin{tabular}{@{}llcccc@{}}
38	\toprule
39	\textbf{Model} & \textbf{Family} & \textbf{Params} & \textbf{Bin F1} & \textbf{95\% CI} & \textbf{3-class F1}$^{\dagger}$ \\
40	\midrule
41	Pythia-2.8B     & Pythia  & 2.8B & \textbf{0.724} & [.707, .742] & 0.798 \\
42	Pythia-1B       & Pythia  & 1.0B & 0.718 & [.700, .735] & \textbf{0.806} \\
43	Qwen3-1.7B     & Qwen    & 1.7B & 0.709 & [.693, .726] & 0.772 \\
44	Llama-3.2-3B   & Llama   & 3.2B & 0.697 & [.680, .713] & 0.775 \\
45	OLMo-2-1B      & OLMo    & 1.5B & 0.695 & [.679, .711] & 0.781 \\
46	Qwen3-8B       & Qwen    & 8.2B & 0.692 & [.674, .708] & 0.714 \\
47	Qwen3-0.6B     & Qwen    & 0.6B & 0.691 & [.673, .709] & 0.780 \\
48	Mistral-7B     & Mistral & 7.0B & 0.633 & [.617, .648] & 0.682 \\
49	\midrule
50	\multicolumn{3}{l}{\textbf{Average (8-gen LOGO)}} & \textbf{0.694} & [.688, .700] & \textbf{0.762} \\
51	\multicolumn{3}{l}{\textbf{LOFO (family-level)}} & 0.686 & --- & --- \\
52	\bottomrule
53	\end{tabular}}
54	\end{table}
55	
56	\subsection{Differential Depth Response}
57	\label{sec:results-differential}
58	
59	\paragraph{Formal definition.}
60	\looseness=-1 For feature $f$ measured across depths $d \in \{0,1,2{+}\}$, we define its \emph{depth sensitivity} as $\text{DDR}(f) = |\rho(\text{depth}, f)|$, where $\rho$ is Spearman correlation over all per-text measurements.
61	A feature is classified as \emph{drifting} if Cohen's $d > 0.50$ between adjacent depths, or \emph{stationary} if $d < 0.15$; the two-cluster structure is robust across $\varepsilon \in [0.10, 0.75]$ ($k$-means silhouette\,=\,0.660, $p{=}0.030$; exhaustive split enumeration ranks this partition first; independent replication in all eight generators; Appendix~\ref{app:ddr-validation}).
62	\looseness=-1 Recursive inputs grow increasingly self-typical~\citep{markovian_chains}; this predicts location drift with shape invariance (confirmed across nucleus, greedy, and top-$k$ strategies; Appendix~\ref{app:decoding-strategy}).
63	
64	\looseness=-1 Figure~\ref{fig:ddr-trajectory} reveals the dichotomy: central-tendency features (entropy mean, TTR, hapax ratio) decline monotonically with depth, while shape features (entropy max, tail decay, entropy min) remain flat (per-feature distributions: Appendix~\ref{app:feature-distributions}; qualitative chain example: Appendix~\ref{app:qualitative}).
65	The partition is binary ($k{=}2$; silhouette\,=\,0.660), with entropy std as the sole \emph{intermediate} member ($d{=}0.46$, $|\rho|{=}0.16$), distinct from three near-stationary features ($d < 0.10$; Appendix~\ref{app:ddr-validation}).
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
70	\caption{Differential depth response (DDR). Drifting features (red; $|\rho| > 0.60$, effect size $d{=}0.74$--$1.05$) shift monotonically with generation depth; near-stationary features (blue; $d \leq 0.10$) are approximately preserved; entropy std (purple; $d{=}0.46$) is intermediate. Diamonds: cross-generator means; dots: per-generator values.}
71	\label{fig:feature-drift}
72	\end{figure}
73	
74	\looseness=-1 Pooled Spearman correlations corroborate the split: drifting features show $|\rho| > 0.60$ (hapax ratio $-0.64$, TTR $-0.62$, entropy mean $-0.60$) vs.\ $|\rho| \leq 0.16$ for entropy max and tail decay; entropy min reaches $|\rho|{=}0.40$ due to its gen-0/gen-1 boundary sensitivity (discussed below). This persistent magnitude gap defines the DDR partition (Figure~\ref{fig:feature-drift}).
75	
76	\begin{figure}[t]
77	\centering
78	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.pdf}
79	\caption{LOGO binary F1 vs.\ inference cost (8-gen pooled). The 7-feature ensemble (one 410M model) matches multi-detector ensembles (1.4B total) at ${\sim}2.4\times$ lower cost. RTX 5090 timings.}
80	\label{fig:baseline-ci}
81	\end{figure}
82	
83	\paragraph{Quantification.}
84	\looseness=-1 Cohen's $d$ shows a ${\geq}8{\times}$ gap between drifting ($d{=}0.74$--$1.05$) and near-stationary ($d < 0.10$); KS, Glass's $\Delta$, Cliff's $\delta$ corroborate (Appendix~\ref{app:ddr-validation}).
85	Entropy min and tail decay are \emph{boundary features}: entropy min is near-stationary for gen-1/gen-2+ ($d{=}0.016$) but sensitive at gen-0/gen-1; tail decay passes two one-sided tests (TOST) equivalence (Appendix~\ref{app:tost}) for only 4/8 generators (per-generator $|d|{=}0.07$--$0.22$).
86	\paragraph{Validation.}
87	\looseness=-1 Each hold-out generator independently recovers the identical partition (silhouette 0.505--0.760); TOST confirms near-stationarity for entropy min (8/8) and entropy max (6/8); permutation testing confirms the split as non-random ($p{=}0.030$). Per-feature convergence dynamics (Figure~\ref{fig:convergence}), per-family DDR consistency (Appendix~\ref{app:family-ddr}), and causal feature analysis (Appendix~\ref{app:ddr-causality}) appear in Appendices~\ref{app:ddr-validation}--\ref{app:convergence}.
88	
89	\paragraph{Feature complementarity.}
90	\looseness=-1 The full 7-feature set (F1\,=\,0.773, 10-fold stratified cross-validation) outperforms surface-only (0.688) and reference-only (0.713; McNemar $p \approx 0$; Appendix~\ref{app:ablation-table}).
91	Group ablation (10-fold stratified CV) confirms complementarity: 3-class F1 gains $+$5.3\,pp when non-drifting features are added (drifting-only 0.716, all-7 0.769), while binary detection is already saturated by location drift alone (drifting-only 0.697 vs.\ all-7 0.700); shape stability thus contributes to depth \emph{grading}, not detection.
92	TTR and hapax ratio ($r = 0.97$) are retained for marginal LOFO gains (Appendix~\ref{app:lofo}).
93	
94	\paragraph{Cross-family reference models.}
95	\looseness=-1 Alternative references (OLMo-2-1B, Qwen3-0.6B) yield F1 spread of only 0.013 (Appendix~\ref{app:cross-ref}); same-family proximity may inflate Pythia F1 by up to 1.2\,pp, but the DDR partition is preserved.
96	
97	\paragraph{Temperature and prompt-type sensitivity.}
98	\looseness=-1 All four tested generators degrade at $t{=}0.9$ ($-$9.3 to $-$26.0\,pp binary F1; Appendix~\ref{app:sampling-sensitivity}); continuation chains show the strongest drift (F1\,=\,0.781; Appendix~\ref{app:prompt-type}).
99	The DDR partition hierarchy is preserved across temperatures (Appendix~\ref{app:ddr-temp-stability}), including cross-temperature transfer (Appendix~\ref{app:cross-temp}); random word replacement at 10\% degrades binary F1 by only 8\,pp (Appendix~\ref{app:human-edit}).
100	
101	
102	\subsection{Comparison with Detection Baselines}
103	\label{sec:results-baselines}
104	
105	\begin{table}[t]
106	\centering
107	\footnotesize
108	\caption{Depth classification (8-gen LOGO, pooled). Binary F1 excludes gen-0. 7-feature: one 410M model; 4-det ensembles: two models, 1.4B. QLoRA (\S\ref{sec:results-classification}) uses full token sequences (within-model 5-fold CV, not LOGO), serving as an information-asymmetric ceiling.}
109	\label{tab:baselines}
110	\resizebox{\columnwidth}{!}{%
111	\begin{tabular}{lcccc}
112	\toprule
113	\textbf{Method} & \textbf{Feat.} & \textbf{3-class F1} & \textbf{Bin F1} & \textbf{ms/text} \\
114	\midrule
115	4-det.\ + surface     & 6 & \textbf{0.795} & \textbf{0.708} & 22.8 \\
116	4-detector ens.\      & 4 & 0.785 & 0.700 & 22.8 \\
117	7-feature (ours)      & 7 & 0.774 & 0.705 & \textbf{9.7} \\
118	\midrule
119	Avg-LogProb           & 1 & 0.707 & 0.673 & --- \\
120	FastDetectGPT         & 1 & 0.660 & 0.569 & --- \\
121	LD-Score              & 1 & 0.630 & 0.675 & --- \\
122	Binoculars            & 1 & 0.411 & 0.539 & --- \\
123	\bottomrule
124	\end{tabular}}
125	\end{table}
126	
127	\looseness=-1 We next ask whether existing detection methods, designed for binary real-vs-synthetic classification, incidentally capture depth structure, repurposing four detection scores as ordinal depth predictors under identical XGBoost and LOGO conditions (Table~\ref{tab:baselines}).
128	The strongest baseline is a 4-detector + surface feature ensemble (binary F1\,=\,0.708), which pools four detection scores with TTR and hapax ratio; among individual detectors, Avg-LogProb provides the most meaningful single-feature comparison.
129	
130	\looseness=-1 The 7-feature ensemble matches the 4-detector+surface ensemble on binary F1 (0.705 vs.\ 0.708; Figure~\ref{fig:baseline-ci}) at ${\sim}2.4\times$ lower cost, though the latter leads by 2.1\,pp on 3-class F1 (0.795 vs.\ 0.774); both surpass individual detectors by 3.0--16.6\,pp.
131	The DDR decomposition explains why depth discrimination is achievable: location features carry the signal and shape features enable cross-generator transfer (\S\ref{sec:discussion}), all with a single 410M reference model; ordinal-specific methods (CORAL, Frank-Hall) yield comparable F1 (Appendix~\ref{app:classifier}).
132	Among individual detectors, LD-Score and Avg-LogProb best capture depth structure (binary F1\,=\,0.675 and 0.673); FastDetectGPT captures 3-class ordering (F1\,=\,0.660) but struggles with binary depth separation (F1\,=\,0.569); Binoculars is least informative (binary F1\,=\,0.539).
133	Concurrent iterative-generation studies use different chain operators and cannot be directly included as depth baselines (Appendix~\ref{app:iterative-comparison}).
134	
135	\begin{figure*}[t]
136	\centering
137	\includegraphics[width=\textwidth]{fig_convergence_dynamics.pdf}
138	\caption{Feature convergence dynamics. (a)~Drifting features (red) and intermediate entropy std (purple): $|d| > 0.46$ by gen-2+. (b)~Near-stationary features (blue): $|d| < 0.25$ at all depths. Shape stability persists across chain lengths.}
139	\label{fig:convergence}
140	\end{figure*}
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b461f34-472a-4660-95e6-8f7a88bc5f26",
  "isSidechain": true,
  "promptId": "9d60d394-a874-4281-aae5-d0919e91a07f",
  "agentId": "ac60bb2420338e251",
  "type": "user",
  "uuid": "9007eea5-b0ee-420e-8c64-db203b706e8d",
  "sourceToolAssistantUUID": "1b461f34-472a-4660-95e6-8f7a88bc5f26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T19:41:02.934Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VfibcyX67x7u3SVu18L2iV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9007eea5-b0ee-420e-8c64-db203b706e8d",
  "isSidechain": true,
  "agentId": "ac60bb2420338e251",
  "requestId": "req_011CbPrbPWp8Au6usDsuvybZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "573c2091-3693-4494-9382-4a6d6e19afc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013TrSEkJjdMPDTiGr6Nwo3U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 615,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T19:41:02.940Z_

<details><summary>↩ Tool result · `toolu_01VfibcyX67x7u3SVu18L2iV`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\looseness=-1 DDR reflects monotonic NLL compression under recursive generation (Appendix~\ref{app:nll-distribution}).
5	Shape stability is not trivially predictable from architecture: entropy\_max is bounded by $\log|V|{\approx}10.8$ nats but observed values fall far below this ceiling; tail\_decay lacks an obvious bound yet remains near-stationary ($|d|{=}0.10$--$0.22$); entropy\_std drifts ($d{=}0.46$) despite shared NLL derivation.
6	ANOVA confirms depth explains ${>}48{\times}$ more variance in location than shape features (Appendix~\ref{app:variance-decomposition}).
7	
8	\paragraph{Relationship to model collapse.}
9	\looseness=-1 Model collapse erodes tail coverage via weight updates, and shape features \emph{do} change under retraining \cite{curse_of_recursion,strong_model_collapse}. DDR, by contrast, characterizes fixed-parameter inference where shape remains stable.
10	Shape stability is thus specific to the fixed-parameter regime, not an a priori consequence of architecture; DDR complements concurrent iterative-generation studies (Appendix~\ref{app:iterative-comparison}).
11	
12	\paragraph{Temperature sensitivity.}
13	\looseness=-1 Higher sampling temperature ($\tau > 0.7$) flattens token probability distributions, narrowing NLL variance and diluting the location shift that drifting features capture (\S\ref{sec:results-differential}).
14	The DDR partition hierarchy is preserved across all tested temperatures (Appendix~\ref{app:ddr-temp-stability}), but signal strength is temperature-dependent, bounding current applicability to moderate sampling.
15	
16	\paragraph{Error structure and scope.}
17	\looseness=-1 The gen-1$\to$gen-2+ boundary is the primary failure point (error rate 48.4\%; Appendix~\ref{app:error-analysis}): gen-1 texts retain sufficient diversity to overlap with gen-0; deeper generations show monotonically decreasing error ($\leq$29.2\%), so DDR-based classifiers are most reliable for heavily recycled content.
18	The DDR partition is robust across decoding strategies, temperatures, and reference models (Appendices~\ref{app:decoding-strategy}--\ref{app:cross-ref}).
19	Instruction tuning compresses DDR (Appendix~\ref{app:instruct}), but QLoRA recovery to F1\,=\,0.89--0.91 (within-model) shows the signal persists.
20	Cross-domain (F1\,=\,0.74--0.75; Appendix~\ref{app:domain}) and 9-generator (Appendix~\ref{app:9gen-scale}) evaluations confirm generalization.
21	DDR enables corpus contamination detection and synthetic data pipeline auditing; depth-aware filtering does not improve perplexity (Appendix~\ref{app:downstream}), so DDR identifies \emph{provenance} rather than \emph{fluency degradation}. Finer-grained 5-class classification yields F1\,$\approx$\,0.50 (Appendix~\ref{app:finer-depth}), a resolution limit of three depth classes.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "573c2091-3693-4494-9382-4a6d6e19afc6",
  "isSidechain": true,
  "promptId": "9d60d394-a874-4281-aae5-d0919e91a07f",
  "agentId": "ac60bb2420338e251",
  "type": "user",
  "uuid": "4e7e9af3-7145-4753-ba5d-ca9382bcdca6",
  "sourceToolAssistantUUID": "573c2091-3693-4494-9382-4a6d6e19afc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T19:41:03.371Z_

<details open><summary>🔧 Tool call — Read · `toolu_017zU8ZdzXdUj9cHXgMt6Bcd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e7e9af3-7145-4753-ba5d-ca9382bcdca6",
  "isSidechain": true,
  "agentId": "ac60bb2420338e251",
  "requestId": "req_011CbPrbPWp8Au6usDsuvybZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f5dfb016-1ebe-4744-99dd-68256e850c99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013TrSEkJjdMPDTiGr6Nwo3U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 39102,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 534,
          "cache_read_input_tokens": 39102,
          "cache_creation_input_tokens": 615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 615,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T19:41:03.377Z_

<details><summary>↩ Tool result · `toolu_017zU8ZdzXdUj9cHXgMt6Bcd`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-1 Recursive generation produces a decomposable depth response: location features drift monotonically while shape features remain approximately preserved. This asymmetry supports cross-generator depth classification (F1\,=\,0.694--0.762; 5-generator cross-model F1\,=\,0.830) under moderate sampling temperatures ($\tau \leq 0.7$).
5	Instruction tuning compresses DDR, bounding current applicability to base models; QLoRA recovery (F1\,=\,0.89--0.91, within-model) points to tractable extension to instruct settings.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5dfb016-1ebe-4744-99dd-68256e850c99",
  "isSidechain": true,
  "promptId": "9d60d394-a874-4281-aae5-d0919e91a07f",
  "agentId": "ac60bb2420338e251",
  "type": "user",
  "uuid": "89edce92-ccb2-4df3-8232-bc654fcf349f",
  "sourceToolAssistantUUID": "f5dfb016-1ebe-4744-99dd-68256e850c99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T19:41:03.436Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WmJe8PYB8zyYqiTfs2kudP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89edce92-ccb2-4df3-8232-bc654fcf349f",
  "isSidechain": true,
  "agentId": "ac60bb2420338e251",
  "requestId": "req_011CbPrbPWp8Au6usDsuvybZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "572cb721-e218-4ad8-a405-b3006f05d015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013TrSEkJjdMPDTiGr6Nwo3U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 39102,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 534,
          "cache_read_input_tokens": 39102,
          "cache_creation_input_tokens": 615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 615,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T19:41:03.445Z_

<details><summary>↩ Tool result · `toolu_01WmJe8PYB8zyYqiTfs2kudP`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\looseness=-1 All eight generators are base (pretrained) models with $\leq$8.2B parameters; instruction-tuned variants show substantially degraded depth signal (within-model 3-class F1 drops 3.7--19.9\,pp; Appendix~\ref{app:instruct}), though QLoRA partially recovers (F1\,=\,0.89--0.91, within-model); this pattern is consistent with signal compression rather than elimination.
5	The evaluation assumes English Wikipedia seeds, a fixed decoding regime ($t{=}0.7$, nucleus $p{=}0.9$), and an English-centric reference model (Pythia-410M); cross-temperature transfer is tested (Appendix~\ref{app:cross-temp}) but cross-lingual generalization remains untested.
6	Depth resolution is bounded at three classes (gen-0\,/\,gen-1\,/\,gen-2+); finer-grained 5-class classification yields F1\,$\approx$\,0.50 with deeper depths mutually indistinguishable (Appendix~\ref{app:finer-depth}).
7	DDR signal strength is temperature-dependent; at $\tau{=}0.9$, classification performance degrades substantially ($-$9.3 to $-$26.0\,pp binary F1), and cross-temperature transfer at production scales remains untested.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "572cb721-e218-4ad8-a405-b3006f05d015",
  "isSidechain": true,
  "promptId": "9d60d394-a874-4281-aae5-d0919e91a07f",
  "agentId": "ac60bb2420338e251",
  "type": "user",
  "uuid": "49408501-e642-4141-9c67-6f0376ea1224",
  "sourceToolAssistantUUID": "572cb721-e218-4ad8-a405-b3006f05d015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-25T19:41:57.403Z_

Now I'll systematically extract all numbers from the files I've read:

## Complete Number Extraction from Paper Files

### **ABSTRACT.tex**

| Number | Value | Context | File Location | Cross-References |
|--------|-------|---------|----------------|------------------|
| 1 | 8 | Eight base-model generators | Line 4 | intro, method, results |
| 2 | 5 | Five model families | Line 4 | intro, method |
| 3 | 0.74 | Cohen's d (effect size, lower bound for drifting features) | Line 4 | intro, results |
| 4 | 1.05 | Cohen's d (effect size, upper bound for drifting features) | Line 4 | intro, results |
| 5 | 0.10 | Cohen's d (effect size threshold, near-stationary features) | Line 4 | intro, results |
| 6 | 8 | Approximate effect-size gap multiplier (8× or ≥8×) | Line 4 | intro, method, results, discussion |
| 7 | 0.46 | Cohen's d (entropy std intermediate value) | Line 4 | intro, results, discussion |
| 8 | 0.694 | Leak-free binary F1 (gen-1 vs. gen-2+) | Line 5 | intro, results, conclusion |
| 9 | 0.762 | 3-class F1 (LOGO evaluation) | Line 5 | results |
| 10 | 8 | Eight generators in ensemble evaluation | Line 5 | method, results |
| 11 | 5 | Five generators in cross-model chains | Line 5 | results |
| 12 | 0.830 | Binary F1 for cross-model chains (gen-0 seeds) | Line 5 | results |

### **INTRODUCTION.tex**

| Number | Value | Context | File Location | Cross-References |
|--------|-------|---------|----------------|------------------|
| 1 | 7 | Lower bound percentage for LLM-modified publications | Line 4 | — |
| 2 | 17 | Upper bound percentage for LLM-modified publications | Line 4 | — |
| 3 | 8 | Eight base-model generators | Line 9 | abstract, method, results |
| 4 | 5 | Five architectural families | Line 9 | abstract, method |
| 5 | 0.6 | Model size lower bound (0.6B) | Line 9 | method |
| 6 | 8 | Model size upper bound (8B) | Line 9 | method |
| 7 | 0.74 | Cohen's d (drifting, lower bound) | Line 9 | abstract, results |
| 8 | 1.05 | Cohen's d (drifting, upper bound) | Line 9 | abstract, results |
| 9 | 0.10 | Cohen's d (near-stationary threshold) | Line 9 | abstract, results |
| 10 | 0.46 | Cohen's d (entropy std intermediate) | Line 9 | abstract, results, discussion |
| 11 | 8 | Effect-size gap multiplier (≥8×) | Line 9 | abstract, method, results, discussion |
| 12 | 0.59 | Correlation threshold (|ρ| > 0.59) | Line 16 | results |
| 13 | 0.07 | Correlation threshold (|ρ| < 0.07) | Line 16 | results |
| 14 | 0.694 | Binary F1 (macro-averaged LOGO) | Line 22 | abstract, results |
| 15 | 0.705 | Binary F1 (pooled) | Line 22 | results |
| 16 | 0.708 | Multi-detector ensemble F1 | Line 22 | results |
| 17 | 2.4 | Cost factor multiplier (2.4×) | Line 22 | results |
| 18 | 0.905 | QLoRA 3-class F1 (within-model 5-fold CV) | Line 22 | results |
| 19 | 10.0 | QLoRA improvement (pp) | Line 22 | method, results |
| 20 | 37 | Dataset size (37K texts) | Line 27 | method, results |
| 21 | 0.6 | Model size lower bound (0.6B) | Line 27 | method |
| 22 | 8 | Model size upper bound (8B) | Line 27 | method |
| 23 | 14 | Exploratory model scale upper bound (14B) | Line 27 | — |
| 24 | 0.74 | Cohen's d (drifting, lower) | Line 26 | abstract, results |
| 25 | 1.05 | Cohen's d (drifting, upper) | Line 26 | abstract, results |
| 26 | 0.10 | Cohen's d (near-stationary) | Line 26 | abstract, results |
| 27 | 0.686 | LOFO binary F1 | Line 37 | method, results |

### **METHOD.tex**

| Number | Value | Context | File Location | Cross-References |
|--------|-------|---------|----------------|------------------|
| 1 | 7 | Seven distributional features | Line 7, Table 1 caption | results, discussion |
| 2 | 2.8 | Pythia model size (2.8B) | Line 36 | results (Table 1) |
| 3 | 1 | Pythia model size (1B) | Line 36 | results (Table 1) |
| 4 | 1 | OLMo model size (1B) | Line 36 | — |
| 5 | 1.7 | Qwen model size (1.7B) | Line 36 | results (Table 1) |
| 6 | 0.6 | Qwen model size (0.6B) | Line 36 | results (Table 1) |
| 7 | 8 | Qwen model size (8B) | Line 36 | results (Table 1) |
| 8 | 3 | Llama model size (3B) | Line 36 | results (Table 1) |
| 9 | 7 | Mistral model size (7B) | Line 36 | results (Table 1) |
| 10 | 13 | Parameter range multiplier (13×) | Line 37 | — |
| 11 | 0.6 | Lower bound (0.6B) | Line 37 | — |
| 12 | 8 | Upper bound (8B) | Line 37 | — |
| 13 | 3 | Qwen generator count (3/8) | Line 37 | — |
| 14 | 0.686 | LOFO F1 | Line 37 | results |
| 15 | 1 | Number of seed passages (approximately 1,000) | Line 39 | — |
| 16 | 1000 | Seed passages per generator | Line 39 | — |
| 17 | 4 | Generation chain depth (gen-0 through gen-4) | Line 41 | — |
| 18 | 0.7 | Temperature (τ) | Line 43 | results, discussion, limitations |
| 19 | 0.9 | Nucleus sampling parameter (p) | Line 43 | — |
| 20 | 256 | Maximum length (new tokens) | Line 43 | — |
| 21 | 37 | Dataset size (37K texts) | Line 44 | abstract, results |
| 22 | 37058 | Exact dataset size | Line 44 | results |
| 23 | 0.50 | 5-class LOGO macro F1 | Line 42 | limitations |
| 24 | 0.27 | Per-class F1 for depths 2–4 (gen-2/gen-3) | Line 42 | — |
| 25 | 2 | Minimum depth class boundary | Line 42 | — |
| 26 | 4 | Maximum depth class boundary | Line 42 | — |
| 27 | 410 | Reference model size (Pythia-410M) | Line 56 | abstract, results, discussion |
| 28 | 0.013 | F1 spread across different reference models | Line 57 | results |
| 29 | 0.65 | Redundancy correlation threshold (|r| > 0.65) | Line 53 | — |
| 30 | 0.011 | Delta F1 threshold (ΔF1 ≤ -0.011) | Line 53 | — |
| 31 | 100 | Tail decay rank lower bound | Line 58 | — |
| 32 | 1000 | Tail decay rank upper bound | Line 58 | — |
| 33 | 0.97 | Correlation between TTR and hapax ratio (r) | Line 65 | results |
| 34 | 200 | XGBoost estimators (n_estimators) | Line 76 | — |
| 35 | 6 | XGBoost max depth | Line 76 | — |
| 36 | 0.1 | XGBoost learning rate | Line 76 | — |
| 37 | 2.0 | Hyperparameter sensitivity F1 variation (pp) | Line 77 | — |
| 38 | 95 | Bootstrap confidence interval percentage | Line 80 | results |
| 39 | 1000 | Bootstrap resamples (n) | Line 80 | results |

### **RESULTS.tex**

| Number | Value | Context | File Location | Cross-References |
|--------|-------|---------|----------------|------------------|
| 1 | 8 | 8×8 transfer matrix (binary F1) | Line 7 caption | — |
| 2 | 0.810 | Mean cross-generator F1 | Line 7 caption | — |
| 3 | 0.796 | 95% CI lower bound (cross-generator F1) | Line 7 caption | — |
| 4 | 0.822 | 95% CI upper bound (cross-generator F1) | Line 7 caption | — |
| 5 | 3 | 3-class LOGO | Line 14 | abstract, method |
| 6 | 0.762 | 3-class LOGO F1 | Line 14 | abstract, conclusion |
| 7 | 37 | Dataset size (37K texts) | Line 14 | method |
| 8 | 37058 | Exact dataset size (N) | Line 14 | method |
| 9 | 8 | Eight generators from five families | Line 14 | — |
| 10 | 5 | Five model families | Line 14 | — |
| 11 | 0.758 | 95% CI lower (3-class LOGO F1) | Line 14 | — |
| 12 | 0.766 | 95% CI upper (3-class LOGO F1) | Line 14 | — |
| 13 | 9.1 | Cross-generator F1 spread (pp) | Line 14 | — |
| 14 | 0.694 | Leak-free binary F1 (gen-1 vs. gen-2+) | Line 15 | abstract, intro, conclusion |
| 15 | 0.688 | 95% CI lower (binary F1) | Line 15 | — |
| 16 | 0.700 | 95% CI upper (binary F1) | Line 15 | — |
| 17 | 0.94 | Per-class gen-0 F1 | Line 15 | — |
| 18 | 0.633 | Mistral-7B binary F1 (minimum) | Line 16 | — |
| 19 | 0.724 | Pythia-2.8B binary F1 (maximum) | Line 16 | — |
| 20 | 0.028 | Standard deviation of per-generator F1 | Line 16 | — |
| 21 | 0.830 | Cross-model chains binary F1 | Line 19 | abstract |
| 22 | 0.818 | 95% CI lower (cross-model F1) | Line 19 | — |
| 23 | 0.841 | 95% CI upper (cross-model F1) | Line 19 | — |
| 24 | 5 | Number of generators in LOGO (cross-model) | Line 19 | — |
| 25 | 1000 | Bootstrap resamples (n) | Line 19 | — |
| 26 | 0.810 | Mean transfer F1 | Line 20 | — |
| 27 | 0.009 | ANOVA generator identity contribution (η²_gen) | Line 20 | — |
| 28 | 0.724 | Pythia-2.8B F1 | Line 21 | Table 1 |
| 29 | 0.633 | Mistral-7B F1 | Line 21 | Table 1 |
| 30 | 0.013 | Reference model spread | Line 21 | method |
| 31 | 0.905 | QLoRA 3-class F1 (within-model 5-fold CV) | Line 22 | intro, conclusion |
| 32 | 10.0 | QLoRA improvement (pp) | Line 22 | intro, method |
| 33 | 0.89 | QLoRA instruct F1 (lower bound) | Line 22 | conclusion, limitations |
| 34 | 0.91 | QLoRA instruct F1 (upper bound) | Line 22 | conclusion, limitations |
| 35 | 0.724 | Length-matched binary F1 | Line 25 | — |
| 36 | 0.770 | Standard binary F1 | Line 25 | — |
| 37 | 0.680 | Independent-seed evaluation F1 | Line 25 | — |
| 38 | 48.4 | Error rate at depth-2 (%) | Line 28 | discussion, limitations |
| 39 | 20.3 | Error rate at depth-4 (%) | Line 28 | — |
| 40 | 29.2 | Error rate at deeper generations (≤) | Line 29 | discussion |
| 41 | 2.8 | Pythia-2.8B model size (Table 1) | Line 41 | — |
| 42 | 1.0 | Pythia-1B model size (Table 1) | Line 42 | — |
| 43 | 1.7 | Qwen3-1.7B model size (Table 1) | Line 43 | — |
| 44 | 3.2 | Llama-3.2-3B model size (Table 1) | Line 44 | — |
| 45 | 1.5 | OLMo-2-1B actual size (Table 1) | Line 45 | — |
| 46 | 8.2 | Qwen3-8B actual size (Table 1) | Line 46 | limitations |
| 47 | 0.6 | Qwen3-0.6B model size (Table 1) | Line 47 | — |
| 48 | 7.0 | Mistral-7B model size (Table 1) | Line 48 | — |
| 49 | 0.707 | Pythia-2.8B 95% CI lower (Table 1) | Line 41 | — |
| 50 | 0.742 | Pythia-2.8B 95% CI upper (Table 1) | Line 41 | — |
| 51 | 0.798 | Pythia-2.8B 3-class F1 (Table 1) | Line 41 | — |
| 52 | 0.700 | Pythia-1B 95% CI lower (Table 1) | Line 42 | — |
| 53 | 0.735 | Pythia-1B 95% CI upper (Table 1) | Line 42 | — |
| 54 | 0.806 | Pythia-1B 3-class F1 (Table 1) | Line 42 | — |
| 55 | 0.693 | Qwen3-1.7B 95% CI lower (Table 1) | Line 43 | — |
| 56 | 0.726 | Qwen3-1.7B 95% CI upper (Table 1) | Line 43 | — |
| 57 | 0.772 | Qwen3-1.7B 3-class F1 (Table 1) | Line 43 | — |
| 58 | 0.680 | Llama-3.2-3B 95% CI lower (Table 1) | Line 44 | — |
| 59 | 0.713 | Llama-3.2-3B 95% CI upper (Table 1) | Line 44 | — |
| 60 | 0.775 | Llama-3.2-3B 3-class F1 (Table 1) | Line 44 | — |
| 61 | 0.679 | OLMo-2-1B 95% CI lower (Table 1) | Line 45 | — |
| 62 | 0.711 | OLMo-2-1B 95% CI upper (Table 1) | Line 45 | — |
| 63 | 0.781 | OLMo-2-1B 3-class F1 (Table 1) | Line 45 | — |
| 64 | 0.674 | Qwen3-8B 95% CI lower (Table 1) | Line 46 | — |
| 65 | 0.708 | Qwen3-8B 95% CI upper (Table 1) | Line 46 | — |
| 66 | 0.714 | Qwen3-8B 3-class F1 (Table 1) | Line 46 | — |
| 67 | 0.673 | Qwen3-0.6B 95% CI lower (Table 1) | Line 47 | — |
| 68 | 0.709 | Qwen3-0.6B 95% CI upper (Table 1) | Line 47 | — |
| 69 | 0.780 | Qwen3-0.6B 3-class F1 (Table 1) | Line 47 | — |
| 70 | 0.617 | Mistral-7B 95% CI lower (Table 1) | Line 48 | — |
| 71 | 0.648 | Mistral-7B 95% CI upper (Table 1) | Line 48 | — |
| 72 | 0.682 | Mistral-7B 3-class F1 (Table 1) | Line 48 | — |
| 73 | 0.686 | LOFO (family-level) binary F1 (Table 1) | Line 51 | intro, method |
| 74 | 0.50 | Cohen's d threshold (drifting) | Line 61 | — |
| 75 | 0.15 | Cohen's d threshold (stationary) | Line 61 | — |
| 76 | 0.10 | Cohen's d epsilon range lower (ε) | Line 61 | — |
| 77 | 0.75 | Cohen's d epsilon range upper (ε) | Line 61 | — |
| 78 | 0.660 | K-means silhouette (DDR validation) | Line 61 | — |
| 79 | 0.030 | P-value for silhouette | Line 61 | — |
| 80 | 0.60 | Correlation threshold (|ρ|) | Line 64 | — |
| 81 | 0.46 | Cohen's d (entropy std, intermediate) | Line 65 | abstract, intro, discussion |
| 82 | 0.16 | Spearman correlation (entropy std) | Line 65 | — |
| 83 | 0.10 | Cohen's d (near-stationary, upper) | Line 65 | — |
| 84 | 0.660 | Silhouette score (DDR partition) | Line 65 | — |
| 85 | 0.60 | Spearman correlation threshold (drifting) | Line 74 | — |
| 86 | 0.64 | Hapax ratio Spearman correlation | Line 74 | — |
| 87 | 0.62 | TTR Spearman correlation | Line 74 | — |
| 88 | 0.60 | Entropy mean Spearman correlation | Line 74 | — |
| 89 | 0.16 | Spearman correlation (entropy max, tail decay) | Line 74 | — |
| 90 | 0.40 | Entropy min Spearman correlation | Line 74 | — |
| 91 | 8 | Effect-size gap multiplier (≥8×) | Line 84 | abstract, intro, method |
| 92 | 0.74 | Cohen's d (drifting, lower) | Line 84 | — |
| 93 | 1.05 | Cohen's d (drifting, upper) | Line 84 | — |
| 94 | 0.10 | Cohen's d (near-stationary, upper) | Line 84 | — |
| 95 | 0.016 | Cohen's d (entropy min, gen-1/gen-2+) | Line 85 | — |
| 96 | 0.07 | Per-generator |d| lower bound (boundary) | Line 85 | — |
| 97 | 0.22 | Per-generator |d| upper bound (boundary) | Line 85 | — |
| 98 | 4 | Generator count (TOST equivalence) | Line 85 | — |
| 99 | 0.505 | Hold-out generator silhouette lower | Line 87 | — |
| 100 | 0.760 | Hold-out generator silhouette upper | Line 87 | — |
| 101 | 0.030 | P-value (permutation test) | Line 87 | — |
| 102 | 0.773 | Full 7-feature F1 (10-fold CV) | Line 90 | — |
| 103 | 0.688 | Surface-only F1 | Line 90 | — |
| 104 | 0.713 | Reference-only F1 | Line 90 | — |
| 105 | 0.716 | Drifting-only 3-class F1 | Line 91 | — |
| 106 | 5.3 | 3-class F1 gain (pp) | Line 91 | — |
| 107 | 0.769 | All-7 3-class F1 (group ablation) | Line 91 | — |
| 108 | 0.697 | Drifting-only binary F1 | Line 91 | — |
| 109 | 0.700 | All-7 binary F1 (group ablation) | Line 91 | — |
| 110 | 0.97 | TTR-hapax correlation | Line 92 | method |
| 111 | 0.013 | Alternative reference F1 spread | Line 95 | method |
| 112 | 1.2 | Pythia F1 inflation (pp) | Line 95 | — |
| 113 | 0.9 | Temperature (t) maximum | Line 98 | — |
| 114 | 9.3 | Binary F1 degradation at t=0.9 (lower bound, pp) | Line 98 | limitations |
| 115 | 26.0 | Binary F1 degradation at t=0.9 (upper bound, pp) | Line 98 | limitations |
| 116 | 0.781 | Continuation chains F1 | Line 98 | — |
| 117 | 0.708 | 4-detector + surface F1 (binary) | Line 115 | — |
| 118 | 0.700 | 4-detector ensemble binary F1 | Line 116 | — |
| 119 | 0.705 | 7-feature ensemble binary F1 (pooled) | Line 117 | abstract, intro |
| 120 | 9.7 | 7-feature inference time (ms/text) | Line 117 | — |
| 121 | 0.673 | Avg-LogProb binary F1 | Line 119 | — |
| 122 | 0.569 | FastDetectGPT binary F1 | Line 120 | — |
| 123 | 0.675 | LD-Score binary F1 | Line 121 | — |
| 124 | 0.539 | Binoculars binary F1 | Line 122 | — |
| 125 | 0.795 | 4-det + surface 3-class F1 | Line 115 | — |
| 126 | 0.785 | 4-detector ens. 3-class F1 | Line 116 | — |
| 127 | 0.774 | 7-feature 3-class F1 (pooled) | Line 117 | — |
| 128 | 22.8 | 4-det ensemble inference time (ms/text) | Line 116 | — |
| 129 | 0.707 | Avg-LogProb 3-class F1 | Line 119 | — |
| 130 | 0.660 | FastDetectGPT 3-class F1 | Line 120 | — |
| 131 | 0.630 | LD-Score 3-class F1 | Line 121 | — |
| 132 | 0.411 | Binoculars 3-class F1 | Line 122 | — |
| 133 | 2.1 | 4-detector+surface advantage over 7-feature (pp) | Line 130 | — |
| 134 | 2.4 | Cost multiplier (lower) | Line 130 | abstract, intro |
| 135 | 3.0 | Individual detector advantage (lower bound, pp) | Line 130 | — |
| 136 | 16.6 | Individual detector advantage (upper bound, pp) | Line 130 | — |
| 137 | 1.4 | 4-detector ensemble size (B) | Line 130 | results |
| 138 | 48 | Variance explained by depth in location (>) | Line 6, discussion | — |

### **DISCUSSION.tex**

| Number | Value | Context | File Location | Cross-References |
|--------|-------|---------|----------------|------------------|
| 1 | 10.8 | log|V| (entropy max bound, nats) | Line 5 | — |
| 2 | 0.10 | tail_decay Cohen's d lower (–d) | Line 5 | results |
| 3 | 0.22 | tail_decay Cohen's d upper (–d) | Line 5 | results |
| 4 | 0.46 | entropy_std Cohen's d | Line 5 | abstract, intro, results |
| 5 | 48 | Variance ratio (depth vs. shape features) | Line 6 | — |
| 6 | 0.7 | Temperature (τ) reference | Line 13 | method, limitations |
| 7 | 48.4 | Gen-1/gen-2+ error rate (%) | Line 17 | results, limitations |
| 8 | 29.2 | Error rate at depth ≥3 (%) | Line 17 | results |
| 9 | 0.74 | Domain transfer F1 lower bound | Line 20 | — |
| 10 | 0.75 | Domain transfer F1 upper bound | Line 20 | — |
| 11 | 0.50 | 5-class F1 approximation | Line 21 | method, limitations |
| 12 | 0.89 | QLoRA instruct F1 lower | Line 19 | conclusion, limitations |
| 13 | 0.91 | QLoRA instruct F1 upper | Line 19 | conclusion, limitations |

### **CONCLUSION.tex**

| Number | Value | Context | File Location | Cross-References |
|--------|-------|---------|----------------|------------------|
| 1 | 0.694 | Binary F1 (location drift) | Line 4 | abstract, intro, results |
| 2 | 0.762 | 3-class F1 (location drift) | Line 4 | abstract, results |
| 3 | 5 | Five generators (cross-model F1) | Line 4 | results |
| 4 | 0.830 | Cross-model F1 | Line 4 | abstract, results |
| 5 | 0.7 | Temperature (τ) | Line 4 | method, results, discussion, limitations |
| 6 | 0.89 | QLoRA recovery F1 (lower) | Line 5 | results, limitations |
| 7 | 0.91 | QLoRA recovery F1 (upper) | Line 5 | results, limitations |

### **LIMITATIONS.tex**

| Number | Value | Context | File Location | Cross-References |
|--------|-------|---------|----------------|------------------|
| 1 | 8 | Eight base generators | Line 4 | abstract, intro, method, results |
| 2 | 8.2 | Maximum model size (8.2B) | Line 4 | results |
| 3 | 3.7 | 3-class F1 drop (lower bound, pp) | Line 4 | — |
| 4 | 19.9 | 3-class F1 drop (upper bound, pp) | Line 4 | — |
| 5 | 0.89 | QLoRA F1 (lower) | Line 4 | results, conclusion |
| 6 | 0.91 | QLoRA F1 (upper) | Line 4 | results, conclusion |
| 7 | 0.7 | Temperature (τ) | Line 5 | method, results, discussion |
| 8 | 0.9 | Nucleus sampling (p) | Line 5 | method |
| 9 | 0.50 | 5-class F1 approximation | Line 6 | method, discussion |
| 10 | 0.9 | Temperature (t) maximum | Line 7 | results |
| 11 | 9.3 | Binary F1 degradation lower (pp) | Line 7 | results |
| 12 | 26.0 | Binary F1 degradation upper (pp) | Line 7 | results |

## Summary of Cross-References

**Most frequently cited numbers across sections:**
- **0.694** (binary F1): abstract, intro, results, conclusion
- **0.762** (3-class F1): abstract, results, conclusion
- **0.74–1.05** (Cohen's d drifting): abstract, intro, results
- **0.46** (entropy std Cohen's d): abstract, intro, results, discussion
- **0.830** (cross-model F1): abstract, results, conclusion
- **8 generators / 5 families**: abstract, intro, method, results, limitations
- **0.7 temperature**: method, results, discussion, limitations
- **0.89–0.91 QLoRA**: results, conclusion, limitations
- **48.4% / 29.2% error rates**: results, discussion, limitations
- **8× effect-size gap**: abstract, intro, method, results, discussion
- **37K texts / 37,058 exact**: abstract, method, results

All numbers have been extracted with line-level precision and cross-reference mapping across all seven files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49408501-e642-4141-9c67-6f0376ea1224",
  "isSidechain": true,
  "agentId": "ac60bb2420338e251",
  "requestId": "req_011CbPrbfQXwKdM9sidWmk1U",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4beef273-be11-4116-962c-30e8ee807d3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "ef0deb25-58cd-4916-8c8f-13a3573781d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "glittery-wishing-coral",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019DqzJJXfAA1DZdUjE8Wv2w",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12942,
      "cache_read_input_tokens": 39717,
      "output_tokens": 8278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12942
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 8278,
          "cache_read_input_tokens": 39717,
          "cache_creation_input_tokens": 12942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12942,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
