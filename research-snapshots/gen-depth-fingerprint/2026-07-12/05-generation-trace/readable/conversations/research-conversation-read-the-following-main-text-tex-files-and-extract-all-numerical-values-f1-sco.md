# Research conversation: Read the following main text tex files and extract ALL numerical values (F1 scores, accuracy, Cohen's d, p-values, perce

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a21bf54d5265f3fa3.jsonl`
- **Structured JSON:** [`866eaf44974eea40f900.json`](../../sessions/86/866eaf44974eea40f900.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-23T10:22:39.115Z_

Read the following main text tex files and extract ALL numerical values (F1 scores, accuracy, Cohen's d, p-values, percentages, counts, etc.) with their context. Be thorough - capture every number that appears.

Files to read (all under /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/):
1. abstract.tex
2. introduction.tex
3. results.tex
4. conclusion.tex
5. limitations.tex
6. discussion.tex
7. table1.tex
8. table2.tex
9. table4.tex
10. per_family_ddr_table.tex

For each file, list every number/metric found with its context (what it refers to). Pay special attention to:
- F1 scores
- Cohen's d values
- p-values
- Accuracy values
- DDR values
- Any percentages
- Sample counts

Report everything in a structured format: [file:line] metric_name = value

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a21bf54d5265f3fa3",
  "type": "user",
  "uuid": "b2cf465c-e934-4eca-b893-a1629115c1c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T10:22:40.169Z_

I'll read all the specified tex files and extract all numerical values with their context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2cf465c-e934-4eca-b893-a1629115c1c7",
  "isSidechain": true,
  "agentId": "a21bf54d5265f3fa3",
  "requestId": "req_011CbKLQ5hS9qCiPq9KxfVez",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "507f7a38-65db-455a-a7a6-d96130e4f692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YY31tWihQGgZMf1N6wVfYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18137,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18137,
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

_source line 3 · 2026-05-23T10:22:40.600Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A8BEFTAWvZ4oqdgbb6DAMU`</summary>

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
  "parentUuid": "507f7a38-65db-455a-a7a6-d96130e4f692",
  "isSidechain": true,
  "agentId": "a21bf54d5265f3fa3",
  "requestId": "req_011CbKLQ5hS9qCiPq9KxfVez",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fdca7416-adb7-445e-b682-0fb7ce4d8891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YY31tWihQGgZMf1N6wVfYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18137,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18137,
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

_source line 4 · 2026-05-23T10:22:40.607Z_

<details><summary>↩ Tool result · `toolu_01A8BEFTAWvZ4oqdgbb6DAMU`</summary>

```text
1	% Abstract — Depth Profiling of Recursive LLM Generation Chains
2	\begin{abstract}
3	As LLM outputs re-enter training corpora and seed further generation, understanding how recursive generation reshapes text distributions becomes important for data provenance and corpus curation---yet existing detectors answer only the binary human-or-machine question, ignoring \emph{generation depth}: we introduce \emph{depth profiling} to address this gap.
4	We decompose distributional drift under recursive generation into location and shape components, revealing an asymmetry we term \emph{differential depth response} (DDR): across eight base-model generators from five families, NLL location features drift monotonically with depth (effect size $d{=}0.76$--$1.17$) while three shape features remain near-stationary ($d < 0.10$), with entropy std intermediate ($d{=}0.55$).
5	Prior work documents \emph{what converges}; the central finding here is \emph{what is approximately preserved}: shape stability complements location drift for ordinal depth grading without per-generator calibration, achieving leak-free binary F1\,=\,0.694 (gen-1 vs.\ gen-2+) and 3-class F1\,=\,0.762 (gen-0 seeds shared across generators; \S\ref{sec:generation}) under leave-one-generator-out evaluation; an end-to-end classifier reaches 3-class F1\,=\,0.905 (6-gen LOGO; Appendix~\ref{app:qlora}).
6	Instruction tuning compresses DDR, bounding current applicability to base models.
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdca7416-adb7-445e-b682-0fb7ce4d8891",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a21bf54d5265f3fa3",
  "type": "user",
  "uuid": "b1187b52-5eb2-4100-9395-c4ed5a7f3226",
  "sourceToolAssistantUUID": "fdca7416-adb7-445e-b682-0fb7ce4d8891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T10:22:40.811Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QorxPF54nF73awnuiqxNVU`</summary>

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
  "parentUuid": "b1187b52-5eb2-4100-9395-c4ed5a7f3226",
  "isSidechain": true,
  "agentId": "a21bf54d5265f3fa3",
  "requestId": "req_011CbKLQ5hS9qCiPq9KxfVez",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ea39ee8-b8ec-46ef-b8c8-2b1211da27fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YY31tWihQGgZMf1N6wVfYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18137,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18137,
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

_source line 6 · 2026-05-23T10:22:40.816Z_

<details><summary>↩ Tool result · `toolu_01QorxPF54nF73awnuiqxNVU`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	An estimated 7--17\% of recent scientific publications already contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}. As these outputs re-enter training corpora \cite{dolma,fineweb} and seed further generation, text accumulates at varying \emph{generation depths}; each successive cycle reshapes distributional properties in ways that matter for data provenance, corpus auditing, and contamination monitoring in base-model pretraining corpora \cite{ccnet,dsir} as well as model collapse analysis \cite{curse_of_recursion,strong_model_collapse}. Understanding \emph{how} recursive generation alters text distributions---and which properties change versus which are preserved---is therefore a prerequisite for principled corpus curation, yet current methods address only binary human-or-machine detection \cite{detectgpt,fast_detectgpt,binoculars,ld_score}.
5	Base models provide the cleanest substrate to isolate depth effects from alignment-induced changes.
6	We find that recursive generation produces a decomposable depth profile: distributional \emph{location} drifts with depth while \emph{shape} remains stable across generators, an asymmetry sufficient for cross-generator depth prediction.
7	
8	Distributional compression under recursive generation is well-documented \cite{curious_decline,broken_telephone,markovian_chains}, yet existing analyses characterize \emph{that} and \emph{why} convergence occurs without decomposing what drifts from what is preserved.
9	We introduce \emph{depth profiling} (coarse ordinal classification into gen-0\,/\,gen-1\,/\,gen-2+), and decompose this compression into structurally distinct components: across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy (reference-model NLL), lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) remains an order of magnitude more stable (effect size $d{=}0.76$--$1.17$ vs.\ $d < 0.10$ for three near-stationary features; entropy std is intermediate ($d{=}0.55$); boundary features show additional nuance; convergent effect-size measures confirm this partition).
10	We term this location/shape asymmetry the \emph{differential depth response} (DDR; Figure~\ref{fig:ddr-trajectory}), an empirical regularity of base-model autoregressive generation that is mechanistically distinct from model collapse \cite{curse_of_recursion}, which erodes tail coverage via weight updates; DDR instead analyzes fixed-parameter inference chains.
11	The stationary shape component complements location drift for depth prediction without per-generator calibration.
12	
13	\begin{figure*}[t!]
14	\centering
15	\includegraphics[width=\textwidth]{fig_ddr_trajectory.pdf}
16	\caption{Feature trajectories across generation depth ($y$-axis: $z$-scored feature values). \textbf{Top row (drifting)}: entropy mean and hapax ratio decline monotonically across all eight generators ($|\rho| > 0.59$). \textbf{Bottom row (stationary)}: entropy max and tail decay remain flat ($|\rho| < 0.07$). Colored lines: individual generators; diamonds: cross-generator mean (blue for drifting, amber for stationary). This dichotomy defines the DDR.}
17	\label{fig:ddr-trajectory}
18	\end{figure*}
19	We focus on base (pretrained) models; instruction tuning degrades depth signal (Appendix~\ref{app:instruct}).
20	
21	As a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at ${\sim}2.4\times$ lower cost; an end-to-end QLoRA classifier reaches 3-class F1\,=\,0.905 (6-gen LOGO; Appendix~\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features.
22	
23	Our contributions:
24	\begin{enumerate}[nosep,leftmargin=*]
25	    \item \textbf{Empirical decomposition (DDR).} Across eight generators from five families, we decompose inference-chain drift into two primary response zones---drifting ($d{=}0.76$--$1.17$) vs.\ near-stationary ($d < 0.10$)---plus one intermediate feature ($d{=}0.55$). Where prior work documents \emph{what converges} \cite{curious_decline,markovian_chains}, DDR identifies \emph{what is approximately preserved}, an empirical regularity with analytical utility for depth classification without per-generator calibration. DDR is a descriptive empirical finding; the classification value lies in this decomposition rather than the classifier itself.
26	    \item \textbf{Task formulation and evaluation suite.} We define generation depth classification as an ordinal prediction task and construct a controlled dataset of 37K texts from eight generators across five families (0.6B--8B; exploratory evidence extends to 14B, Appendix~\ref{app:9gen-scale}), with leave-one-generator-out cross-validation as the primary evaluation protocol.
27	    \item \textbf{Scope characterization.} Systematic evaluation across temperature, prompt type, instruction tuning, model scale, domain transfer, and perturbation robustness maps the operational envelope of depth profiling.
28	\end{enumerate}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ea39ee8-b8ec-46ef-b8c8-2b1211da27fd",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a21bf54d5265f3fa3",
  "type": "user",
  "uuid": "e5461c22-0854-464c-bf3e-6edacd54ed52",
  "sourceToolAssistantUUID": "1ea39ee8-b8ec-46ef-b8c8-2b1211da27fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T10:22:41.027Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VN7gNScSJANRGyaEpTETnx`</summary>

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
  "parentUuid": "e5461c22-0854-464c-bf3e-6edacd54ed52",
  "isSidechain": true,
  "agentId": "a21bf54d5265f3fa3",
  "requestId": "req_011CbKLQ5hS9qCiPq9KxfVez",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff2ace4d-1dad-45da-948a-f31d437c9aef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YY31tWihQGgZMf1N6wVfYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18137,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18137,
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

_source line 8 · 2026-05-23T10:22:41.030Z_

<details><summary>↩ Tool result · `toolu_01VN7gNScSJANRGyaEpTETnx`</summary>

```text
1	\vspace{-1mm}
2	\section{Results}
3	\label{sec:results}
4	\vspace{-1mm}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{fig_transfer_heatmap.pdf}
9	\caption{Cross-generator depth classification: $8{\times}8$ transfer matrix (binary F1, gen-1 vs.\ gen-2+). Each cell shows F1 when training on one generator (row) and testing on another (column). Mean cross-generator F1\,=\,0.810 [95\% CI: 0.796, 0.822]; uniformly high off-diagonal values demonstrate that depth signal transfers robustly across five architectural families without per-generator calibration.}
10	\label{fig:transfer-heatmap}
11	\end{figure}
12	
13	\subsection{Depth Classification Performance}
14	\label{sec:results-classification}
15	
16	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}), with cross-generator F1 spread of 9.1\,pp capturing generator selection uncertainty.
17	This 3-class metric is inflated by shared gen-0 seeds across generators (per-class gen-0 F1\,$\approx$\,0.94; \S\ref{sec:generation}); we therefore report \textbf{leak-free binary F1} (gen-1 vs.\ gen-2+, our primary conservative metric)\,=\,0.694 (CI [0.688, 0.700]; generator-level mean${\pm}$SE: $0.694{\pm}0.010$) throughout, excluding gen-0 entirely.
18	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B; SD\,=\,0.028), with the primary difficulty at the gen-1\,/\,gen-2+ boundary (Appendix~\ref{app:confusion}).
19	
20	\paragraph{Cross-model generalization.}
21	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]; Appendix~\ref{app:cross-model-detail}) under 5-generator LOGO.\footnote{Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B; generator-level LOGO with bootstrap CIs ($n$\,=\,1{,}000). Not directly comparable to 8-generator LOGO due to differing subsets.}
22	Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact (mean transfer F1\,=\,0.810, Figure~\ref{fig:transfer-heatmap}; LOFO\,=\,0.686); the cross-model advantage is only 2\,pp; ANOVA variance decomposition confirms generator identity contributes ${<}1$\% of feature variance ($\eta^2_{\text{gen}} \leq 0.009$; Appendix~\ref{app:cross-model-detail}).
23	A scale effect emerges: smaller models achieve higher F1 (Pythia-2.8B: 0.724 vs.\ Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (spread $\leq$0.013; \S\ref{sec:results-differential}).
24	An end-to-end QLoRA classifier reaches 3-class F1\,=\,0.905 ($+$11.6\,pp; Appendix~\ref{app:qlora}), confirming additional depth signal in token-level representations; on instruct data, QLoRA recovers to 0.89--0.91 (Appendix~\ref{app:instruct}), establishing the decomposition as DDR's primary contribution.
25	
26	\paragraph{Confound controls.}
27	Length-matched subsampling yields binary F1\,=\,0.724 (vs.\ 0.770; Appendix~\ref{app:length}); independent-seed evaluation with disjoint pools (F1\,=\,0.680; Appendix~\ref{app:seed-control}) confirms the classifier captures generative degradation, not seed-specific content.
28	
29	\begin{table}[t]
30	\centering
31	\footnotesize
32	\caption{8-generator LOGO macro-F1 for the 7-feature ensemble (bootstrap 95\% CIs, $n$\,=\,1000). Binary F1 (gen-1 vs.\ gen-2+) is the primary metric; it excludes gen-0 entirely and is unaffected by seed sharing. Cross-generator binary F1: SD\,=\,0.028, IQR\,=\,[0.692, 0.714]. $^{\dagger}$3-class F1 carries upward bias because gen-0 seeds are shared across generators (\S\ref{sec:generation}); independent-seed controls confirm the depth signal (F1\,=\,0.680; Appendix~\ref{app:seed-control}). CIs: text-level bootstrap ($n$\,=\,1{,}000) within each fold.}
33	\label{tab:logo-results}
34	\resizebox{\columnwidth}{!}{%
35	\begin{tabular}{@{}llcccc@{}}
36	\toprule
37	\textbf{Model} & \textbf{Family} & \textbf{Params} & \textbf{Bin F1} & \textbf{95\% CI} & \textbf{3-class F1}$^{\dagger}$ \\
38	\midrule
39	Pythia-2.8B     & Pythia  & 2.8B & \textbf{0.724} & [.707, .742] & 0.798 \\
40	Pythia-1B       & Pythia  & 1.0B & 0.718 & [.700, .735] & \textbf{0.806} \\
41	Qwen3-1.7B     & Qwen    & 1.7B & 0.709 & [.693, .726] & 0.772 \\
42	Llama-3.2-3B   & Llama   & 3.2B & 0.697 & [.680, .713] & 0.775 \\
43	OLMo-2-1B      & OLMo    & 1.5B & 0.695 & [.679, .711] & 0.781 \\
44	Qwen3-8B       & Qwen    & 8.2B & 0.692 & [.674, .708] & 0.714 \\
45	Qwen3-0.6B     & Qwen    & 0.6B & 0.691 & [.673, .709] & 0.780 \\
46	Mistral-7B     & Mistral & 7.0B & 0.633 & [.617, .648] & 0.682 \\
47	\midrule
48	\multicolumn{3}{l}{\textbf{Average (8-gen LOGO)}} & \textbf{0.694} & [.688, .700] & \textbf{0.762} \\
49	\multicolumn{3}{l}{\textbf{LOFO (family-level)}} & 0.686 & --- & --- \\
50	\bottomrule
51	\end{tabular}}
52	\end{table}
53	
54	\vspace{-1mm}
55	\subsection{Differential Depth Response}
56	\label{sec:results-differential}
57	
58	\begin{figure}[!t]
59	\centering
60	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.pdf}
61	\caption{LOGO binary F1 vs.\ inference cost in ms/text (8-gen pooled). The 7-feature ensemble (one 410M reference model) matches multi-detector ensembles (two models, 1.4B total) at ${\sim}2.4\times$ lower cost; individual detectors vary widely when repurposed for depth. Inference costs measured on a single NVIDIA RTX 5090.}
62	\label{fig:baseline-ci}
63	\end{figure}
64	
65	\paragraph{Formal definition.}
66	For feature $f$ measured across depths $d \in \{0,1,2{+}\}$, we define its \emph{depth sensitivity} as $\text{DDR}(f) = |\rho(\text{depth}, f)|$, where $\rho$ is Spearman correlation over all per-text measurements.
67	A feature is classified as \emph{drifting} if Cohen's $d > 0.50$ between adjacent depths, or \emph{stationary} if $d < 0.15$; these thresholds are reference anchors, not definitive boundaries---the two-cluster structure is robust across $\varepsilon \in [0.10, 0.75]$, supported by unsupervised $k$-means (silhouette\,=\,0.660, $p{=}0.030$), exhaustive enumeration of all 35 splits (this partition ranks first), and independent replication in all eight generators (Appendix~\ref{app:ddr-validation}); crucially, each generator's data is fully independent, making per-generator split analysis an 8-fold independent validation of the partition rather than same-data circularity.
68	Recursive inputs grow increasingly self-typical~\citep{markovian_chains}, predicting location drift with shape invariance (confirmed across nucleus, greedy, and top-$k$ strategies; Appendix~\ref{app:decoding-strategy}).
69	
70	Figure~\ref{fig:ddr-trajectory} reveals the dichotomy: central-tendency features (entropy mean, TTR, hapax ratio) decline monotonically with depth, while shape features (entropy max, tail decay, entropy min) remain flat.
71	The partition is binary ($k{=}2$; silhouette\,=\,0.660), with entropy std as a sole \emph{intermediate} member ($d{=}0.55$, $|\rho|{=}0.16$), distinct from three near-stationary features ($d < 0.10$; Appendix~\ref{app:ddr-validation}).
72	
73	\begin{figure}[t]
74	\centering
75	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
76	\caption{Differential depth response (DDR). Drifting features (blue; $|\rho| > 0.60$, effect size $d{=}0.76$--$1.17$) shift monotonically with generation depth; near-stationary features (amber; $d \leq 0.10$) are approximately preserved; entropy std (wine; $d{=}0.55$) is intermediate. Diamonds: cross-generator means; dots: per-generator values.}
77	\label{fig:feature-drift}
78	\end{figure}
79	
80	Pooled Spearman correlations corroborate the split: drifting features show $|\rho| > 0.60$ (hapax ratio $-0.64$, TTR $-0.63$, entropy mean $-0.60$) vs.\ $|\rho| \leq 0.16$ for entropy max and tail decay; entropy min reaches $|\rho|{=}0.40$ due to its gen-0/gen-1 boundary sensitivity (discussed below)---a persistent magnitude gap defining the DDR partition (Figure~\ref{fig:feature-drift}).
81	
82	\paragraph{Quantification.}
83	Cohen's $d$ \cite{cohen1988statistical} shows a ${\geq}7{\times}$ gap between drifting ($d{=}0.76$--$1.17$) and near-stationary ($d \leq 0.08$); KS, Glass's $\Delta$, Cliff's $\delta$ all corroborate (Appendix~\ref{app:ddr-validation}).
84	Entropy min and tail decay are \emph{boundary features}: entropy min is near-stationary for gen-1/gen-2+ ($d{=}0.016$) but sensitive at gen-0/gen-1; tail decay passes TOST for only 4/8 generators ($|d|{=}0.10$--$0.22$).
85	\paragraph{Validation.}
86	Each hold-out generator independently recovers the identical partition (silhouette 0.505--0.760; Appendix~\ref{app:ddr-validation}); TOST confirms near-stationarity for entropy min (8/8) and entropy max (6/8); permutation testing confirms the split as non-random ($p{=}0.030$); $\Delta|\rho| \leq 0.05$ across splits; disjoint generator-pool splits, heteroscedasticity robustness, per-feature convergence dynamics (Figure~\ref{fig:convergence}), and per-family DDR consistency (Appendix~\ref{app:family-ddr}) appear in Appendices~\ref{app:holdout-split}--\ref{app:convergence}.
87	
88	\begin{figure}[t]
89	\centering
90	\includegraphics[width=\columnwidth]{fig_convergence_dynamics.pdf}
91	\caption{Feature convergence dynamics across generation depth. Drifting features (blue) show monotonically increasing effect size ($|d| > 1$ by gen-2+); near-stationary features (amber) remain within $|d| < 0.25$ at all depths, confirming shape stability is not an artifact of insufficient chain length.}
92	\label{fig:convergence}
93	\end{figure}
94	
95	\paragraph{Feature complementarity.}
96	The full 7-feature set (F1\,=\,0.773, 10-fold stratified CV, complementing the LOGO protocol in Table~\ref{tab:logo-results}) outperforms surface-only (0.688) and reference-only (0.713; McNemar $p \approx 0$; Appendix~\ref{app:ablation-table}).
97	The collinear drifting triplet captures ${\sim}$1 effective dimension (PCA PC1\,=\,92.3\%; Appendix~\ref{sec:appendix-feature-correlation}); group ablation confirms complementarity for depth profiling: 3-class F1 gains $+$5.3\,pp when non-drifting features are added (drifting-only 0.716, all-7 0.769), while binary detection is already saturated by location drift alone (drifting-only binary F1\,=\,0.697 vs.\ all-7\,=\,0.700; Appendix~\ref{app:ablation-table})---shape stability contributes to depth \emph{grading}, not detection.
98	TTR and hapax ratio ($r = 0.97$) are retained for marginal LOFO gains \cite{strobl_conditional_2008} (Appendix~\ref{app:lofo}).
99	
100	\paragraph{Cross-family reference models.}
101	Alternative references (OLMo-2-1B, Qwen3-0.6B) yield F1 spread of only 0.013 (Appendix~\ref{app:cross-ref}); same-family proximity may inflate Pythia F1 by up to 1.3\,pp, but the DDR partition is preserved.
102	
103	\paragraph{Temperature and prompt-type sensitivity.}
104	All four tested generators degrade at $t{=}0.9$ ($-$9.3 to $-$26.0\,pp binary F1; Appendix~\ref{app:sampling-sensitivity}); continuation chains show the strongest drift (F1\,=\,0.781; Appendix~\ref{app:prompt-type}).
105	The DDR partition hierarchy is preserved across temperatures (Appendix~\ref{app:ddr-temp-stability}).
106	
107	
108	\vspace{-1mm}
109	\subsection{Comparison with Detection Baselines}
110	\label{sec:results-baselines}
111	
112	We next ask whether existing detection methods---designed for binary real-vs-synthetic classification---incidentally capture depth structure, repurposing four detection scores as ordinal depth predictors under identical XGBoost and LOGO conditions (Table~\ref{tab:baselines}).
113	The strongest baseline is a 4-detector + surface feature ensemble (binary F1\,=\,0.708), which pools four detection scores with TTR and hapax ratio; among individual detectors, Avg-LogProb provides the most meaningful single-feature comparison.
114	
115	\begin{table}[t]
116	\centering
117	\footnotesize
118	\caption{Depth classification (8-gen LOGO, pooled evaluation; pooled F1 is slightly higher than per-generator macro F1 in Table~\ref{tab:logo-results} because larger test folds from high-performing generators contribute proportionally more). Identical XGBoost configuration. 7-feature: one 410M model (905\,MB); 4-det ensembles: two models, 1.4B params (2{,}868\,MB). Individual detection scores (N/A) share the reference-model forward pass; per-method timing is not separately profiled. XGBoost uses 7 handcrafted scalar features (one 410M reference); QLoRA (\S\ref{sec:results-classification}) uses the full token sequence---an information-asymmetric ceiling, not a fair comparison.}
119	\label{tab:baselines}
120	\resizebox{\columnwidth}{!}{%
121	\begin{tabular}{lcccc}
122	\toprule
123	\textbf{Method} & \textbf{Feat.} & \textbf{3-class F1} & \textbf{Bin F1} & \textbf{ms/text} \\
124	\midrule
125	4-det.\ + surface     & 6 & \textbf{0.795} & \textbf{0.708} & 22.8 \\
126	4-detector ens.\      & 4 & 0.785 & 0.700 & 22.8 \\
127	7-feature (ours)      & 7 & 0.774 & 0.705 & \textbf{9.7} \\
128	\midrule
129	Avg-LogProb           & 1 & 0.707 & 0.673 & --- \\
130	FastDetectGPT         & 1 & 0.660 & 0.569 & --- \\
131	LD-Score              & 1 & 0.630 & 0.675 & --- \\
132	Binoculars            & 1 & 0.411 & 0.539 & --- \\
133	\bottomrule
134	\end{tabular}}
135	\end{table}
136	
137	The 7-feature ensemble matches the 4-detector+surface ensemble on binary F1 (0.705 vs.\ 0.708; Figure~\ref{fig:baseline-ci}) at ${\sim}2.4\times$ lower cost, though the latter leads by 2.1\,pp on 3-class F1 (0.795 vs.\ 0.774); both surpass individual detectors by 3.0--16.6\,pp.
138	DDR's contribution is the decomposition into location-sensitive and shape-stable components (\S\ref{sec:discussion}), achieving comparable depth discrimination with a single 410M reference model; ordinal-specific methods (CORAL, Frank-Hall) yield comparable F1 (Appendix~\ref{app:classifier}).
139	Concurrent iterative-generation studies use different chain operators (back-translation, rephrasing) and target different phenomena (factuality, convergence dynamics), precluding direct inclusion as depth classification baselines (Appendix~\ref{app:iterative-comparison}).
140	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff2ace4d-1dad-45da-948a-f31d437c9aef",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a21bf54d5265f3fa3",
  "type": "user",
  "uuid": "ea6e445e-9fd0-426f-b899-c129896f3e97",
  "sourceToolAssistantUUID": "ff2ace4d-1dad-45da-948a-f31d437c9aef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T10:22:41.238Z_

<details open><summary>🔧 Tool call — Read · `toolu_014jxm5JUJdZ5HiZyaq6hmBG`</summary>

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
  "parentUuid": "ea6e445e-9fd0-426f-b899-c129896f3e97",
  "isSidechain": true,
  "agentId": "a21bf54d5265f3fa3",
  "requestId": "req_011CbKLQ5hS9qCiPq9KxfVez",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2ad8e332-0f12-40b4-9615-70328a13244d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YY31tWihQGgZMf1N6wVfYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18137,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18137,
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

_source line 10 · 2026-05-23T10:22:41.246Z_

<details><summary>↩ Tool result · `toolu_014jxm5JUJdZ5HiZyaq6hmBG`</summary>

```text
1	\vspace{-2mm}
2	\section{Conclusion}
3	\label{sec:conclusion}
4	\vspace{-2mm}
5	
6	\looseness=-1 Recursive generation produces a decomposable depth response---location features drift while shape is approximately preserved---enabling cross-generator depth classification (F1\,=\,0.694--0.762) within the base-model scope; QLoRA recovery on instruct data (F1\,=\,0.89--0.91) suggests tractable adaptation.
7	Batch contamination estimation reaches ${\pm}3$--$4$\% at $n{=}1{,}000$ (Appendix~\ref{app:error-analysis}), positioning depth profiling as a practical audit dimension.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ad8e332-0f12-40b4-9615-70328a13244d",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a21bf54d5265f3fa3",
  "type": "user",
  "uuid": "fa2387b2-3e64-4c92-af26-fc9f0dd83d11",
  "sourceToolAssistantUUID": "2ad8e332-0f12-40b4-9615-70328a13244d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T10:22:41.449Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CP2DfR1rVgii9UYYcvCNQa`</summary>

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
  "parentUuid": "fa2387b2-3e64-4c92-af26-fc9f0dd83d11",
  "isSidechain": true,
  "agentId": "a21bf54d5265f3fa3",
  "requestId": "req_011CbKLQ5hS9qCiPq9KxfVez",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "14054806-c4c9-4a68-a9e3-15426f898de0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YY31tWihQGgZMf1N6wVfYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18137,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18137,
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

_source line 12 · 2026-05-23T10:22:41.452Z_

<details><summary>↩ Tool result · `toolu_01CP2DfR1rVgii9UYYcvCNQa`</summary>

```text
1	\vspace{-1mm}
2	\section*{Limitations}
3	\label{sec:limitations}
4	\vspace{-1mm}
5	
6	\looseness=-1 All eight generators are base (pretrained) models with $\leq$8.2B parameters; instruction-tuned variants show substantially degraded depth signal (LOGO binary F1\,=\,0.487; Appendix~\ref{app:instruct}), though QLoRA partially recovers (F1\,=\,0.89--0.91), suggesting the signal is compressed rather than eliminated.
7	The evaluation assumes English Wikipedia seeds, a fixed decoding regime ($t{=}0.7$, nucleus $p{=}0.9$), and an English-centric reference model (Pythia-410M); cross-temperature and cross-lingual transfer remain untested.
8	Depth resolution is bounded at three classes (gen-0\,/\,gen-1\,/\,gen-2+); finer-grained 5-class classification yields F1\,$\approx$\,0.50 with deeper depths mutually indistinguishable (Appendix~\ref{app:finer-depth}).
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14054806-c4c9-4a68-a9e3-15426f898de0",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a21bf54d5265f3fa3",
  "type": "user",
  "uuid": "434d7362-1b6f-4d45-a0d6-fe6729a25bd1",
  "sourceToolAssistantUUID": "14054806-c4c9-4a68-a9e3-15426f898de0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T10:22:41.669Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NbvXgzhRZsKkMs3YZi8Lna`</summary>

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
  "parentUuid": "434d7362-1b6f-4d45-a0d6-fe6729a25bd1",
  "isSidechain": true,
  "agentId": "a21bf54d5265f3fa3",
  "requestId": "req_011CbKLQ5hS9qCiPq9KxfVez",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "237d0998-5063-43fa-b5c4-98e2788b097d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YY31tWihQGgZMf1N6wVfYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18137,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18137,
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

_source line 14 · 2026-05-23T10:22:41.673Z_

<details><summary>↩ Tool result · `toolu_01NbvXgzhRZsKkMs3YZi8Lna`</summary>

```text
1	\vspace{-3mm}
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\looseness=-1 We hypothesize that DDR reflects an empirical regularity of base-model autoregressive generation: recursive inputs compress the token-level NLL distribution monotonically (Appendix~\ref{app:nll-distribution}), producing location drift independent of the token-selection mechanism. Shape features (extreme ranges, tail decay) are bounded by architectural constraints (vocabulary size, softmax temperature) rather than input statistics, explaining their stability under recursive compression. Controlled ablations---greedy decoding, temperature modulation, and semantic-constraint attenuation---support this (Appendices~\ref{app:decoding-strategy}--\ref{app:prompt-type}); ANOVA quantifies the asymmetry: $\eta^2_{\text{depth}}{=}0.34$--$0.37$ for location vs.\ ${<}0.01$ for shape (${>}48{\times}$; Appendix~\ref{app:variance-decomposition}; Granger causality tests support the predictive direction, Appendix~\ref{app:ddr-causality}). DDR is mechanistically distinct from model collapse \cite{curse_of_recursion,strong_model_collapse}---retraining erodes tail via weight updates, whereas inference-chain drift shifts only location---and complements concurrent iterative-generation studies (Appendix~\ref{app:iterative-comparison}). Preliminary batch-level estimates suggest depth constitutes a new analytical dimension for corpus auditing, with contamination estimation reaching ${\pm}3$--$4$\% at $n{=}1{,}000$ (Appendix~\ref{app:error-analysis}); instruction tuning compresses DDR (QLoRA: F1\,=\,0.89--0.91; Appendix~\ref{app:instruct}), while cross-domain signal persists (F1\,=\,0.74--0.75; Appendix~\ref{app:domain}).
6	\vspace{-2mm}
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "237d0998-5063-43fa-b5c4-98e2788b097d",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a21bf54d5265f3fa3",
  "type": "user",
  "uuid": "ba6bdfa6-1495-4676-83f9-218dfce5a00c",
  "sourceToolAssistantUUID": "237d0998-5063-43fa-b5c4-98e2788b097d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T10:22:41.889Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RGSqLo48EpSyQSHk8uhRec`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/table1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba6bdfa6-1495-4676-83f9-218dfce5a00c",
  "isSidechain": true,
  "agentId": "a21bf54d5265f3fa3",
  "requestId": "req_011CbKLQ5hS9qCiPq9KxfVez",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "60b79efd-4e55-4166-8427-a57e34d03dcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YY31tWihQGgZMf1N6wVfYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18137,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18137,
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

_source line 16 · 2026-05-23T10:22:41.901Z_

<details><summary>↩ Tool result · `toolu_01RGSqLo48EpSyQSHk8uhRec`</summary>

```text
1	%% NOTE: this standalone file is NOT \input'd by main.tex; the inline table in results.tex is authoritative.
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{Leave-one-generator-out (LOGO) depth classification results (3-class).
6	Each row holds out one generator for testing and trains on the remaining seven.}
7	\label{tab:logo-results}
8	\begin{tabular}{llccc}
9	\toprule
10	\textbf{Held-out Generator} & \textbf{Family} & \textbf{Params} & \textbf{Macro-F1} & \textbf{95\% CI} \\
11	\midrule
12	Pythia-2.8B   & Pythia  & 2.8B & ---   & --- \\
13	Pythia-1B     & Pythia  & 1.0B & 0.806 & --- \\
14	Qwen3-1.7B   & Qwen    & 1.7B & ---   & --- \\
15	Llama-3.2-3B & Llama   & 3.2B & ---   & --- \\
16	OLMo-2-1B    & OLMo    & 1.0B & ---   & --- \\
17	Qwen3-8B     & Qwen    & 8.0B & ---   & --- \\
18	Qwen3-0.6B   & Qwen    & 0.6B & ---   & --- \\
19	Mistral-7B   & Mistral & 7.0B & 0.681 & --- \\
20	\midrule
21	\textbf{Average (8-gen)} & & & \textbf{0.762} & [0.758, 0.766] \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60b79efd-4e55-4166-8427-a57e34d03dcd",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a21bf54d5265f3fa3",
  "type": "user",
  "uuid": "14917353-36a4-4633-8fc2-6557ee9f747f",
  "sourceToolAssistantUUID": "60b79efd-4e55-4166-8427-a57e34d03dcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T10:22:42.086Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RWMAckYRnQgbUYQwMMCtRR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/table2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14917353-36a4-4633-8fc2-6557ee9f747f",
  "isSidechain": true,
  "agentId": "a21bf54d5265f3fa3",
  "requestId": "req_011CbKLQ5hS9qCiPq9KxfVez",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "752d1f19-1430-4c71-a5a1-cdded48406af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YY31tWihQGgZMf1N6wVfYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18137,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18137,
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

_source line 18 · 2026-05-23T10:22:42.091Z_

<details><summary>↩ Tool result · `toolu_01RWMAckYRnQgbUYQwMMCtRR`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Feature group ablation and complementarity (8-gen 10-fold CV).
5	Both subsets significantly underperform the full set (+8.5\,pp, +5.9\,pp).
6	Permutation importance: \texttt{hapax\_ratio} (0.269) $>$ \texttt{entropy\_mean} (0.164) $>$ \texttt{ttr} (0.159).}
7	\label{tab:feature-ablation}
8	\begin{tabular}{lp{3.2cm}ccc}
9	\toprule
10	\textbf{Feature Set} & \textbf{Features} & \textbf{LOGO F1} & \textbf{95\% CI} & \textbf{McNemar $p$} \\
11	\midrule
12	Full (7 features) & all & 0.773 & --- & --- \\
13	Surface only (2)  & TTR, hapax\_ratio & 0.688 & --- & $<$ 0.001 \\
14	Reference only (5) & entropy\_mean/std/min/max, tail\_decay & 0.713 & --- & $<$ 0.001 \\
15	\bottomrule
16	\end{tabular}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "752d1f19-1430-4c71-a5a1-cdded48406af",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a21bf54d5265f3fa3",
  "type": "user",
  "uuid": "641f6682-4d9c-4457-bfc0-e9dcdd69a21e",
  "sourceToolAssistantUUID": "752d1f19-1430-4c71-a5a1-cdded48406af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T10:22:42.498Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UnUEcH5c6z3x6fR2SpnHXu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/table4.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "641f6682-4d9c-4457-bfc0-e9dcdd69a21e",
  "isSidechain": true,
  "agentId": "a21bf54d5265f3fa3",
  "requestId": "req_011CbKLQ5hS9qCiPq9KxfVez",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d0842f50-2f5e-4d43-8541-86a7b22b126f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YY31tWihQGgZMf1N6wVfYt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18137,
      "cache_read_input_tokens": 0,
      "output_tokens": 755,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18137
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 755,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18137,
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

_source line 20 · 2026-05-23T10:22:42.502Z_

<details><summary>↩ Tool result · `toolu_01UnUEcH5c6z3x6fR2SpnHXu`</summary>

```text
1	To isolate reference-model bias, we replace Pythia-410M with two alternative references from different families and evaluate on a 5-generator subset excluding all Pythia generators.
2	Table~\ref{tab:cross-ref} shows that performance spread across references is only 0.013 F1, confirming the DDR partition is reference-model agnostic.
3	
4	\begin{table}[t]
5	\centering
6	\footnotesize
7	\renewcommand{\arraystretch}{1.3}
8	\caption{Cross-family reference model validation (5-gen LOGO subset). Drift direction is consistent (negative) across all three references; magnitude varies with capacity. Spread in LOGO F1 is 0.013.}
9	\label{tab:cross-ref}
10	\resizebox{\linewidth}{!}{%
11	\begin{tabular}{llccc}
12	\toprule
13	\textbf{Reference} & \textbf{Family} & \textbf{Params} & \textbf{LOGO F1} & \textbf{Ent.\ Drift} \\
14	\midrule
15	Pythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\
16	OLMo-2-1B  & OLMo   & 1.5B & 0.807 & [$-$0.61, $-$0.91] \\
17	Qwen3-0.6B & Qwen   & 0.6B & 0.816 & [$-$0.96, $-$1.35] \\
18	\bottomrule
19	\end{tabular}}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0842f50-2f5e-4d43-8541-86a7b22b126f",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a21bf54d5265f3fa3",
  "type": "user",
  "uuid": "f63d9305-7bd9-4ebd-ae3c-ecf60cdaa44f",
  "sourceToolAssistantUUID": "d0842f50-2f5e-4d43-8541-86a7b22b126f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T10:22:42.557Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L4GvozSftbF4ZMMu3TLYLJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/per_family_ddr_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f63d9305-7bd9-4ebd-ae3c-ecf60cdaa44f",
  "isSidechain": true,
  "agentId": "a21bf54d5265f3fa3",
  "requestId": "req_011CbKLQ5hS9qCiPq9KxfVez",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8ab47914-8185-4156-956b-ffba7c79b11f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YY31tWihQGgZMf1N6wVfYt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18137,
      "cache_read_input_tokens": 0,
      "output_tokens": 755,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18137
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 755,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18137,
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

_source line 22 · 2026-05-23T10:22:42.561Z_

<details><summary>↩ Tool result · `toolu_01L4GvozSftbF4ZMMu3TLYLJ`</summary>

```text
1	\begin{table}[H]
2	\centering
3	\caption{Intra-family consistency of DDR patterns. Each cell shows the mean Spearman $|\rho|$(depth, feature) across generators within a family ($\pm$ SD for multi-generator families). Drifting features exhibit consistently high $|\rho|$ while near-stationary features remain low across all families. $H_{\mathrm{min}}$ is a \emph{boundary feature}: its elevated $|\rho| \approx 0.40$ reflects a large gen-0$\to$gen-1 transition, whereas its Cohen's $d \approx 0$ for gen-1\,/\,gen-2+ confirms near-stationarity within the binary classification scope (\S\ref{sec:results-differential}).}
4	\label{tab:family_ddr_consistency}
5	\small
6	\setlength{\tabcolsep}{3.5pt}
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{l c ccc c ccc}
9	\toprule
10	 & & \multicolumn{3}{c}{\textsc{Drifting}} & \textsc{Int.} & \multicolumn{3}{c}{\textsc{Near-Stationary}} \\
11	\cmidrule(lr){3-5} \cmidrule(lr){6-6} \cmidrule(lr){7-9}
12	Family & $n$ & $H_{\mathrm{mean}}$ & TTR & Hapax & $H_{\mathrm{std}}$ & $H_{\mathrm{max}}$ & $H_{\mathrm{min}}$ & $\beta_{\mathrm{tail}}$ \\
13	\midrule
14	Pythia & 2 & 0.69\tiny{$\pm$0.03} & 0.65\tiny{$\pm$0.02} & 0.66\tiny{$\pm$0.01} & 0.20\tiny{$\pm$0.06} & 0.02\tiny{$\pm$0.02} & 0.49\tiny{$\pm$0.02} & 0.08\tiny{$\pm$0.02} \\
15	OLMo & 1 & 0.64 & 0.70 & 0.71 & 0.30 & 0.07 & 0.39 & 0.14 \\
16	Qwen & 3 & 0.55\tiny{$\pm$0.07} & 0.60\tiny{$\pm$0.06} & 0.62\tiny{$\pm$0.06} & 0.16\tiny{$\pm$0.08} & 0.09\tiny{$\pm$0.00} & 0.36\tiny{$\pm$0.05} & 0.08\tiny{$\pm$0.01} \\
17	Llama & 1 & 0.63 & 0.69 & 0.70 & 0.16 & 0.09 & 0.40 & 0.06 \\
18	Mistral & 1 & 0.54 & 0.60 & 0.61 & 0.06 & 0.09 & 0.40 & 0.03 \\
19	\midrule
20	All 8 gen. & 8 & 0.60\tiny{$\pm$0.08} & 0.63\tiny{$\pm$0.05} & 0.65\tiny{$\pm$0.05} & 0.18\tiny{$\pm$0.08} & 0.07\tiny{$\pm$0.03} & 0.40\tiny{$\pm$0.06} & 0.08\tiny{$\pm$0.03} \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ab47914-8185-4156-956b-ffba7c79b11f",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a21bf54d5265f3fa3",
  "type": "user",
  "uuid": "0c9142a5-8739-4a0d-812f-cab98751c16d",
  "sourceToolAssistantUUID": "8ab47914-8185-4156-956b-ffba7c79b11f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-23T10:23:17.977Z_

Now let me compile all the numerical values extracted from these files in a structured format:

## Extracted Numerical Values from Paper Files

### **abstract.tex**
- [Line 4] Cohen's d (drifting features) = 0.76–1.17
- [Line 4] Cohen's d (near-stationary features) = < 0.10
- [Line 4] Cohen's d (entropy std) = 0.55
- [Line 5] Binary F1 (leak-free, gen-1 vs. gen-2+) = 0.694
- [Line 5] 3-class F1 (gen-0 seeds) = 0.762
- [Line 5] 3-class F1 (6-gen LOGO, QLoRA) = 0.905

### **introduction.tex**
- [Line 4] LLM-modified content in publications (estimate) = 7–17%
- [Line 9] Cohen's d (drifting features) = 0.76–1.17
- [Line 9] Cohen's d (near-stationary features) = < 0.10
- [Line 9] Cohen's d (entropy std) = 0.55
- [Line 9] Spearman correlation (drifting features) = |ρ| > 0.59
- [Line 9] Spearman correlation (stationary features) = |ρ| < 0.07
- [Line 9] Model scale range = 0.6B–8B parameters
- [Line 16] Spearman correlation (drifting, entropy mean) = ρ > 0.59
- [Line 16] Spearman correlation (stationary, entropy max) = |ρ| < 0.07
- [Line 21] Binary F1 (7-feature ensemble, LOGO) = 0.694
- [Line 21] 3-class F1 (end-to-end QLoRA, 6-gen LOGO) = 0.905
- [Line 25] Cohen's d (drifting) = 0.76–1.17
- [Line 25] Cohen's d (near-stationary) = < 0.10
- [Line 25] Cohen's d (entropy std) = 0.55
- [Line 26] Dataset size = 37K texts
- [Line 26] Model scale = 0.6B–8B
- [Line 26] Exploratory evidence extends to = 14B

### **results.tex**
- [Line 9] Mean cross-generator F1 = 0.810
- [Line 9] 95% CI (mean cross-generator F1) = [0.796, 0.822]
- [Line 16] 3-class LOGO F1 = 0.762
- [Line 16] 95% CI (3-class LOGO F1) = [0.758, 0.766]
- [Line 16] Sample size (N) = 37,058
- [Line 16] Cross-generator F1 spread = 9.1 pp
- [Line 17] 3-class gen-0 F1 = ≈ 0.94
- [Line 17] Binary F1 (leak-free, gen-1 vs. gen-2+) = 0.694
- [Line 17] 95% CI (binary F1) = [0.688, 0.700]
- [Line 17] Generator-level mean ± SE = 0.694 ± 0.010
- [Line 18] Binary F1 range (per-generator) = 0.633–0.724
- [Line 18] Binary F1 (Mistral-7B, lowest) = 0.633
- [Line 18] Binary F1 (Pythia-2.8B, highest) = 0.724
- [Line 18] SD (cross-generator) = 0.028
- [Line 21] Binary F1 (cross-model chains, 5-gen LOGO) = 0.830
- [Line 21] 95% CI (cross-model binary F1) = [0.818, 0.841]
- [Line 21] Bootstrap CI (n) = 1,000
- [Line 22] Mean transfer F1 = 0.810
- [Line 22] LOFO = 0.686
- [Line 22] Cross-model advantage = 2 pp
- [Line 22] ANOVA variance (generator identity) = η²ₘ ≤ 0.009
- [Line 23] Binary F1 (Pythia-2.8B) = 0.724
- [Line 23] Binary F1 (Mistral-7B) = 0.633
- [Line 23] Same-family affinity inflation = ≤ 0.013
- [Line 24] End-to-end QLoRA 3-class F1 = 0.905
- [Line 24] 3-class F1 gain = +11.6 pp
- [Line 24] QLoRA instruct data F1 = 0.89–0.91
- [Line 27] Length-matched binary F1 = 0.724 (vs. 0.770 baseline)
- [Line 27] Independent-seed evaluation F1 = 0.680
- [Line 39] Pythia-2.8B Binary F1 = 0.724
- [Line 39] Pythia-2.8B 95% CI = [.707, .742]
- [Line 39] Pythia-2.8B 3-class F1 = 0.798
- [Line 40] Pythia-1B Binary F1 = 0.718
- [Line 40] Pythia-1B 95% CI = [.700, .735]
- [Line 40] Pythia-1B 3-class F1 = 0.806
- [Line 41] Qwen3-1.7B Binary F1 = 0.709
- [Line 41] Qwen3-1.7B 95% CI = [.693, .726]
- [Line 41] Qwen3-1.7B 3-class F1 = 0.772
- [Line 42] Llama-3.2-3B Binary F1 = 0.697
- [Line 42] Llama-3.2-3B 95% CI = [.680, .713]
- [Line 42] Llama-3.2-3B 3-class F1 = 0.775
- [Line 43] OLMo-2-1B Binary F1 = 0.695
- [Line 43] OLMo-2-1B 95% CI = [.679, .711]
- [Line 43] OLMo-2-1B 3-class F1 = 0.781
- [Line 44] Qwen3-8B Binary F1 = 0.692
- [Line 44] Qwen3-8B 95% CI = [.674, .708]
- [Line 44] Qwen3-8B 3-class F1 = 0.714
- [Line 45] Qwen3-0.6B Binary F1 = 0.691
- [Line 45] Qwen3-0.6B 95% CI = [.673, .709]
- [Line 45] Qwen3-0.6B 3-class F1 = 0.780
- [Line 46] Mistral-7B Binary F1 = 0.633
- [Line 46] Mistral-7B 95% CI = [.617, .648]
- [Line 46] Mistral-7B 3-class F1 = 0.682
- [Line 48] Average 8-gen LOGO Binary F1 = 0.694
- [Line 48] Average 8-gen LOGO 95% CI = [.688, .700]
- [Line 48] Average 8-gen LOGO 3-class F1 = 0.762
- [Line 49] LOFO (family-level) = 0.686
- [Line 61] Inference cost (7-feature ensemble) = ~2.4× lower cost
- [Line 67] Cohen's d threshold (drifting) = > 0.50
- [Line 67] Cohen's d threshold (stationary) = < 0.15
- [Line 67] Silhouette score = 0.660
- [Line 67] p-value (permutation test) = 0.030
- [Line 71] Silhouette score (binary partition) = 0.660
- [Line 71] Cohen's d (entropy std) = 0.55
- [Line 71] Spearman |ρ| (entropy std) = 0.16
- [Line 76] Drifting effect size = d = 0.76–1.17
- [Line 76] Near-stationary effect size = d ≤ 0.10
- [Line 76] Entropy std effect size = d = 0.55
- [Line 80] Hapax ratio correlation = -0.64
- [Line 80] TTR correlation = -0.63
- [Line 80] Entropy mean correlation = -0.60
- [Line 80] Entropy max correlation = |ρ| ≤ 0.16
- [Line 80] Tail decay correlation = |ρ| ≤ 0.16
- [Line 80] Entropy min correlation = |ρ| = 0.40
- [Line 83] Cohen's d (drifting) = 0.76–1.17
- [Line 83] Cohen's d gap (drifting vs. near-stationary) = ≥ 7×
- [Line 83] Cohen's d (near-stationary) = ≤ 0.08
- [Line 84] Cohen's d (entropy min gen-1/gen-2+) = 0.016
- [Line 84] Cohen's d (entropy min at gen-0/gen-1) = sensitive
- [Line 84] Cohen's d (tail decay) = 0.10–0.22
- [Line 84] Generators passing TOST (tail decay) = 4/8
- [Line 86] Silhouette range (hold-out validation) = 0.505–0.760
- [Line 86] Delta |ρ| across splits = ≤ 0.05
- [Line 86] p-value (permutation test) = 0.030
- [Line 96] Full 7-feature set F1 (10-fold CV) = 0.773
- [Line 96] Surface-only F1 = 0.688
- [Line 96] Reference-only F1 = 0.713
- [Line 96] McNemar p-value ≈ 0
- [Line 97] PCA PC1 (drifting triplet) = 92.3%
- [Line 97] 3-class F1 gain (non-drifting features) = +5.3 pp
- [Line 97] Drifting-only 3-class F1 = 0.716
- [Line 97] All-7 3-class F1 = 0.769
- [Line 97] Drifting-only binary F1 = 0.697
- [Line 97] All-7 binary F1 = 0.700
- [Line 98] TTR and hapax ratio correlation = 0.97
- [Line 101] F1 spread (cross-ref alternatives) = 0.013
- [Line 101] Same-family inflation (Pythia F1) = up to 1.3 pp
- [Line 104] Temperature t=0.9 degradation = -9.3 to -26.0 pp
- [Line 104] Continuation chains F1 = 0.781
- [Line 113] 4-detector + surface ensemble binary F1 = 0.708
- [Line 125] 4-det. + surface 3-class F1 = 0.795
- [Line 125] 4-det. + surface binary F1 = 0.708
- [Line 125] 4-det. + surface ms/text = 22.8
- [Line 126] 4-detector ens. 3-class F1 = 0.785
- [Line 126] 4-detector ens. binary F1 = 0.700
- [Line 126] 4-detector ens. ms/text = 22.8
- [Line 127] 7-feature (ours) 3-class F1 = 0.774
- [Line 127] 7-feature (ours) binary F1 = 0.705
- [Line 127] 7-feature (ours) ms/text = 9.7
- [Line 129] Avg-LogProb 3-class F1 = 0.707
- [Line 129] Avg-LogProb binary F1 = 0.673
- [Line 130] FastDetectGPT 3-class F1 = 0.660
- [Line 130] FastDetectGPT binary F1 = 0.569
- [Line 131] LD-Score 3-class F1 = 0.630
- [Line 131] LD-Score binary F1 = 0.675
- [Line 132] Binoculars 3-class F1 = 0.411
- [Line 132] Binoculars binary F1 = 0.539
- [Line 137] 7-feature binary F1 vs. 4-det+surface = 0.705 vs. 0.708
- [Line 137] 3-class F1 difference = 2.1 pp
- [Line 137] Individual detector improvement = 3.0–16.6 pp
- [Line 138] Single reference model params = 410M

### **conclusion.tex**
- [Line 6] Binary F1 range = 0.694–0.762
- [Line 6] QLoRA instruct recovery = 0.89–0.91
- [Line 7] Batch contamination estimation = ± 3–4% at n=1,000

### **limitations.tex**
- [Line 6] Maximum parameter size = 8.2B
- [Line 6] Instruction-tuned LOGO binary F1 = 0.487
- [Line 6] QLoRA recovery = 0.89–0.91
- [Line 8] 5-class classification F1 ≈ 0.50

### **discussion.tex**
- [Line 5] ANOVA variance (depth, location) = η²ₐ = 0.34–0.37
- [Line 5] ANOVA variance (depth, shape) = < 0.01
- [Line 5] Variance ratio = > 48×
- [Line 5] Contamination estimation at n=1,000 = ± 3–4%
- [Line 5] QLoRA instruct F1 = 0.89–0.91
- [Line 5] Cross-domain F1 = 0.74–0.75

### **table1.tex**
- [Line 13] Pythia-1B 3-class Macro-F1 = 0.806
- [Line 21] Average 8-gen 3-class F1 = 0.762
- [Line 21] 95% CI = [0.758, 0.766]

### **table2.tex**
- [Line 5] Full 7 features 10-fold CV F1 = 0.773
- [Line 5] Surface only F1 = 0.688
- [Line 5] Reference only F1 = 0.713
- [Line 5] Full set improvement over surface = +8.5 pp
- [Line 5] Full set improvement over reference = +5.9 pp
- [Line 6] Permutation importance (hapax_ratio) = 0.269
- [Line 6] Permutation importance (entropy_mean) = 0.164
- [Line 6] Permutation importance (ttr) = 0.159
- [Line 12] Full 7 features F1 = 0.773
- [Line 13] Surface only (TTR, hapax_ratio) F1 = 0.688
- [Line 13] McNemar p < 0.001
- [Line 14] Reference only F1 = 0.713
- [Line 14] McNemar p < 0.001

### **table4.tex**
- [Line 15] Pythia-410M LOGO F1 = 0.803
- [Line 15] Pythia-410M Entropy Drift = [-1.19, -1.40]
- [Line 16] OLMo-2-1B LOGO F1 = 0.807
- [Line 16] OLMo-2-1B Entropy Drift = [-0.61, -0.91]
- [Line 17] Qwen3-0.6B LOGO F1 = 0.816
- [Line 17] Qwen3-0.6B Entropy Drift = [-0.96, -1.35]
- [Line 2] Cross-ref F1 spread = 0.013

### **per_family_ddr_table.tex**
- [Line 14] Pythia (n=2) H_mean = 0.69 ± 0.03
- [Line 14] Pythia TTR = 0.65 ± 0.02
- [Line 14] Pythia Hapax = 0.66 ± 0.01
- [Line 14] Pythia H_std = 0.20 ± 0.06
- [Line 14] Pythia H_max = 0.02 ± 0.02
- [Line 14] Pythia H_min = 0.49 ± 0.02
- [Line 14] Pythia β_tail = 0.08 ± 0.02
- [Line 15] OLMo (n=1) H_mean = 0.64
- [Line 15] OLMo TTR = 0.70
- [Line 15] OLMo Hapax = 0.71
- [Line 15] OLMo H_std = 0.30
- [Line 15] OLMo H_max = 0.07
- [Line 15] OLMo H_min = 0.39
- [Line 15] OLMo β_tail = 0.14
- [Line 16] Qwen (n=3) H_mean = 0.55 ± 0.07
- [Line 16] Qwen TTR = 0.60 ± 0.06
- [Line 16] Qwen Hapax = 0.62 ± 0.06
- [Line 16] Qwen H_std = 0.16 ± 0.08
- [Line 16] Qwen H_max = 0.09 ± 0.00
- [Line 16] Qwen H_min = 0.36 ± 0.05
- [Line 16] Qwen β_tail = 0.08 ± 0.01
- [Line 17] Llama (n=1) H_mean = 0.63
- [Line 17] Llama TTR = 0.69
- [Line 17] Llama Hapax = 0.70
- [Line 17] Llama H_std = 0.16
- [Line 17] Llama H_max = 0.09
- [Line 17] Llama H_min = 0.40
- [Line 17] Llama β_tail = 0.06
- [Line 18] Mistral (n=1) H_mean = 0.54
- [Line 18] Mistral TTR = 0.60
- [Line 18] Mistral Hapax = 0.61
- [Line 18] Mistral H_std = 0.06
- [Line 18] Mistral H_max = 0.09
- [Line 18] Mistral H_min = 0.40
- [Line 18] Mistral β_tail = 0.03
- [Line 20] All 8 gen. H_mean = 0.60 ± 0.08
- [Line 20] All 8 gen. TTR = 0.63 ± 0.05
- [Line 20] All 8 gen. Hapax = 0.65 ± 0.05
- [Line 20] All 8 gen. H_std = 0.18 ± 0.08
- [Line 20] All 8 gen. H_max = 0.07 ± 0.03
- [Line 20] All 8 gen. H_min = 0.40 ± 0.06
- [Line 20] All 8 gen. β_tail = 0.08 ± 0.03

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c9142a5-8739-4a0d-812f-cab98751c16d",
  "isSidechain": true,
  "agentId": "a21bf54d5265f3fa3",
  "requestId": "req_011CbKLQLatQxWKhGCBHDcyr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8ca24c70-4f8d-45f8-a26b-d34dd203b314",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WmB4UC953NGDbcLM5zagi3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12276,
      "cache_read_input_tokens": 18137,
      "output_tokens": 5295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12276
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 5295,
          "cache_read_input_tokens": 18137,
          "cache_creation_input_tokens": 12276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12276,
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
