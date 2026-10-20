# Research conversation: I need to read multiple files from the paper source directory. The base path is `/home/ubuntu/.agent-ml-research-idea_ge

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ad94135ba66be0aed.jsonl`
- **Structured JSON:** [`d96cbbe4f5358bb273fb.json`](../../sessions/d9/d96cbbe4f5358bb273fb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-21T08:39:52.548Z_

I need to read multiple files from the paper source directory. The base path is `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/`. 

Please read the following files in full:
1. results.tex
2. method.tex
3. appendix_qlora.tex
4. related_work.tex
5. references.bib
6. introduction.tex
7. main.tex

Also glob for any fig1-related Python files in `artifacts/_project/chart/` under `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`.

And grep across all .tex files in `docs/paper/` for:
- "recursive generation depth"
- "DDR"
- "6-gen"
- "aaronson"
- "ordinal"
- "$+$11.6" or "+11.6"
- "QLoRA" or "qlora"

Report all findings with file paths, line numbers, and surrounding context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "c6d96a66-cc69-44e6-a695-ac834f62fd95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T08:39:54.216Z_

I'll read all those files and perform the grep searches for you. Let me start with multiple parallel operations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6d96a66-cc69-44e6-a695-ac834f62fd95",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwgkQ91ZpYGxzpYsRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d361973e-170e-4271-83bc-934972e34d91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 3 · 2026-05-21T08:39:54.450Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CrgYpQRinaYfeifx4XqYoF`</summary>

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
  "parentUuid": "d361973e-170e-4271-83bc-934972e34d91",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwgkQ91ZpYGxzpYsRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e65cbbd4-ba9c-4a16-b1c3-53ca62af377b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 4 · 2026-05-21T08:39:54.464Z_

<details><summary>↩ Tool result · `toolu_01CrgYpQRinaYfeifx4XqYoF`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}), with cross-generator F1 spread of 9.1\,pp capturing generator selection uncertainty.
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94), inflating the 3-class metric.
9	We therefore adopt \textbf{leak-free binary F1} (gen-1 vs.\ gen-2+)\,=\,0.694 (CI [0.688, 0.700]) as the primary metric throughout: it excludes gen-0 entirely and is unaffected by seed sharing.
10	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B; SD\,=\,0.028), with the primary difficulty concentrated at the gen-1\,/\,gen-2+ boundary (Appendix~\ref{app:confusion}).
11	Note that CIs above reflect bootstrap sampling variability; the cross-generator range (9.1\,pp) captures the distinct and larger uncertainty of generator selection.
12	
13	\paragraph{Cross-model generalization.}
14	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]) under 5-generator LOGO.\footnote{5-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B); generator-level LOGO with bootstrap CIs ($n$\,=\,2{,}000). Not directly comparable to 8-generator LOGO due to differing subsets.}
15	Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\,=\,0.810; LOFO yields 0.686.
16	A scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}); cross-domain signal persists with variation (Appendix~\ref{app:domain}).
17	An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 under 6-generator LOGO ($+$11.6\,pp vs.\ the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution.
18	
19	\paragraph{Length confound control.}
20	Length-matched subsampling yields binary F1\,=\,0.724 (vs.\ 0.770 unmatched); a random-subsample control confirms the drop reflects deconfounding, not sample-size reduction (Appendix~\ref{app:length}).
21	
22	\paragraph{Seed-sharing control.}
23	Seed-level demeaning (F1\,=\,0.701) and an independent-seed experiment with disjoint seed pools (F1\,=\,0.680; Appendix~\ref{app:seed-control}) both confirm the classifier captures generative degradation, not seed-specific content.
24	
25	\begin{table}[t]
26	\centering
27	\footnotesize
28	\resizebox{\columnwidth}{!}{%
29	\begin{tabular}{llcccc}
30	\toprule
31	\textbf{Model} & \textbf{Family} & \textbf{Params} & \textbf{Bin F1} & \textbf{95\% CI} & \textbf{3-cl F1}$^{\dagger}$ \\
32	\midrule
33	Pythia-2.8B     & Pythia  & 2.8B & \textbf{0.724} & [.707, .742] & 0.798 \\
34	Pythia-1B       & Pythia  & 1.0B & 0.718 & [.700, .735] & \textbf{0.806} \\
35	Qwen3-1.7B     & Qwen    & 1.7B & 0.709 & [.693, .726] & 0.772 \\
36	Llama-3.2-3B   & Llama   & 3.2B & 0.697 & [.680, .713] & 0.775 \\
37	OLMo-2-1B      & OLMo    & 1.5B & 0.695 & [.679, .711] & 0.781 \\
38	Qwen3-8B       & Qwen    & 8.2B & 0.692 & [.674, .708] & 0.714 \\
39	Qwen3-0.6B     & Qwen    & 0.6B & 0.691 & [.673, .709] & 0.780 \\
40	Mistral-7B     & Mistral & 7.0B & 0.633 & [.617, .648] & 0.682 \\
41	\midrule
42	\multicolumn{3}{l}{\textbf{Average (8-gen LOGO)}} & \textbf{0.694} & [.688, .700] & \textbf{0.762} \\
43	\multicolumn{3}{l}{\textbf{LOFO (family-level)}} & 0.686 & --- & --- \\
44	\bottomrule
45	\end{tabular}}
46	\caption{8-generator LOGO macro-F1 for the 7-feature ensemble (bootstrap 95\% CIs, $n$\,=\,1000). Binary F1 (gen-1 vs.\ gen-2+) is the primary metric; it excludes gen-0 entirely and is unaffected by seed sharing. Cross-generator binary F1: SD\,=\,0.028, IQR\,=\,[0.692, 0.714]. $^{\dagger}$3-class F1 carries upward bias because gen-0 seeds are shared across generators (\S\ref{sec:generation}); independent-seed controls confirm the depth signal (F1\,=\,0.680; Appendix~\ref{app:seed-control}).}
47	\label{tab:logo-results}
48	\end{table}
49	
50	\subsection{Differential Depth Response}
51	\label{sec:results-differential}
52	
53	\begin{figure*}[t]
54	\centering
55	\includegraphics[width=\textwidth]{fig_ddr_trajectory.pdf}
56	\caption{Feature trajectories across generation depth. \textbf{Top row (drifting)}: entropy mean and hapax ratio decline monotonically across all eight generators ($|\rho| > 0.59$). \textbf{Bottom row (stationary)}: entropy max and tail decay remain flat ($|\rho| < 0.07$). Colored lines: individual generators; diamonds: cross-generator mean (blue for drifting, amber for stationary). This dichotomy defines the differential depth response (DDR).}
57	\label{fig:ddr-trajectory}
58	\end{figure*}
59	
60	Not all distributional properties respond equally to recursive generation.
61	Figure~\ref{fig:ddr-trajectory} reveals a striking dichotomy that holds across all eight generators: central-tendency features (entropy mean, TTR, hapax ratio) decline monotonically with depth, while shape features (entropy max, tail decay, entropy min) remain flat.
62	We term this asymmetry the \emph{differential depth response} (DDR).
63	The primary partition is binary: $k{=}2$ clustering in standardized $(|\rho|, d)$ space yields silhouette\,=\,0.660 (Appendix~\ref{app:ddr-validation}), cleanly separating three \emph{drifting} features ($|\rho| > 0.60$, $d{=}0.76$--$1.17$) from four \emph{non-drifting} ones ($d \leq 0.55$); higher $k$ degrades cluster quality ($k{=}3$: silhouette\,=\,0.532).
64	A domain-informed refinement resolves entropy std as a sole \emph{intermediate} member ($d{=}0.55$, $|\rho|{=}0.16$), distinct from the three near-stationary features ($d < 0.10$; CV shift $<$3\% vs.\ $>$15\% for drifting features).
65	Convergence across parametric and non-parametric effect-size measures confirms this partition, establishing that the location/shape asymmetry reflects distributional structure rather than feature-selection artifact (\S\ref{sec:results-differential}, Quantification).
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
70	\caption{Differential depth response (DDR). Diamonds: cross-generator means; dots: per-generator values. Drifting features (blue; $|\rho| > 0.60$, $d{=}0.76$--$1.17$) show strong monotonic depth sensitivity; non-drifting features remain stable. Entropy std (wine; $d{=}0.55$) is an intermediate member; non-drifting features (amber; $d < 0.10$) show negligible drift. Entropy min ($|\rho|{=}0.40$ pooled; gen-0/gen-1 sensitive) and tail decay (TOST 4/8) are boundary features within this group.}
71	\label{fig:feature-drift}
72	\end{figure}
73	
74	Pooled class-balanced Spearman correlations with depth confirm the binary split (Figure~\ref{fig:feature-drift}):
75	drifting features show substantial monotonic trends (hapax ratio $\rho = -0.64$, TTR $\rho = -0.63$, entropy mean $\rho = -0.60$),
76	while non-drifting features remain near-zero (tail decay $|\rho| = 0.04$; per-depth distributions in Appendix~\ref{app:feature-distributions}).
77	The six-fold magnitude gap between drifting ($|\rho| > 0.60$) and non-drifting features ($|\rho| \leq 0.16$) defines the DDR partition.
78	Within the non-drifting group, entropy std ($|\rho| = 0.16$, $d{=}0.55$) shows a substantial level shift despite low monotonicity, distinguishing it from the three near-stationary features ($d < 0.10$); this refinement is stable across $d$ thresholds in $[0.56, 0.75]$ (Appendix~\ref{app:ddr-validation}).
79	
80	\paragraph{Quantification.}
81	Convergence across parametric and non-parametric effect-size measures confirm the split.
82	Cohen's $d$ \cite{cohen1988statistical} shows a ${\geq}7\times$ gap between drifting ($d{=}0.76$--$1.17$) and near-stationary features ($d \leq 0.08$); KS statistics, Glass's $\Delta$, Cliff's $\delta$, and CV shift all corroborate (Appendix~\ref{app:ddr-validation}).
83	Four features fall cleanly into drifting or non-drifting groups.
84	Entropy min and tail decay are \emph{boundary features}: entropy min is near-stationary for gen-1 vs.\ gen-2+ ($d{=}0.016$) but sensitive at gen-0/gen-1 ($|\rho|{=}0.40$); tail decay is \emph{weakly stationary}, passing TOST for only 4/8 generators ($|d|{=}0.10$--$0.22$).
85	Entropy std ($d{=}0.55$, $|\rho|{=}0.16$) is the sole intermediate member.
86	\paragraph{Validation.}
87	The drifting/non-drifting boundary is validated by convergent evidence: $k{=}2$ clustering in standardized $(|\rho|, d)$ space yields a clean separation (silhouette\,=\,0.660), invariant across threshold choices $\varepsilon \in [0.10, 0.75]$; crucially, per-generator split analysis recovers the identical partition in all eight hold-out generators independently (per-generator silhouette range 0.505--0.760; Appendix~\ref{app:ddr-validation}).
88	Per-generator TOST equivalence testing ($\varepsilon{=}|d|{<}0.20$, following Cohen's~\citeyearpar{cohen1988statistical} conventional threshold; gen-1 vs.\ gen-2+) confirms near-stationarity for entropy min (8/8 pass) and entropy max (6/8); tail decay passes for only 4/8, with $|d|{=}0.10$--$0.22$ spanning the boundary.
89	A permutation test ($n{=}10{,}000$) confirms the three-vs-four split is non-random ($p{=}0.030$; fixed-label silhouette\,=\,0.660 vs.\ null mean\,=\,0.46); exhaustive enumeration of all $\binom{7}{3}{=}35$ possible splits ranks this partition first (Appendix~\ref{app:ddr-validation}).
90	Reclassifying either boundary feature as intermediate preserves the core drifting/non-drifting split and leaves classification unchanged.
91	
92	\paragraph{Feature complementarity.}
93	The full 7-feature set (F1\,=\,0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar $p \approx 0$; Appendix~\ref{app:ablation-table}).
94	PCA confirms the three drifting features share a single latent dimension (92.3\% variance; Appendix~\ref{sec:appendix-feature-correlation}); replacing them with PC1 costs only 1.1\,pp, confirming that DDR's contribution is identifying \emph{which} distributional properties drift, not classification per se.
95	TTR and hapax ratio ($r = 0.97$) are both retained for marginal LOFO gains despite feature masking \cite{strobl_conditional_2008} (Appendix~\ref{app:lofo}).
96	
97	\paragraph{Cross-family reference models.}
98	Alternative references (OLMo-2-1B, Qwen3-0.6B) achieve comparable LOGO F1 (spread 0.013; Appendix~\ref{app:cross-ref}), bounding the same-family affinity effect; depth features are robust to reference model choice, though residual same-family proximity may inflate Pythia-family F1 by up to 1.3\,pp.
99	
100	\paragraph{Temperature and prompt-type sensitivity.}
101	All four tested generators degrade at $t{=}0.9$ ($-9.3$ to $-26.0$\,pp binary F1); low-temperature improvement is family-dependent ($+7$--$9$\,pp for Pythia/OLMo at $t{=}0.5$, negligible for Qwen; Appendix~\ref{app:sampling-sensitivity}).
102	Continuation chains show the strongest drift (F1\,=\,0.781), with cross-prompt-type transfer confirming shared signal (LOPTO F1\,=\,0.753; Appendix~\ref{app:prompt-type}); the DDR partition hierarchy is preserved across temperatures despite absolute effect-size compression (Appendix~\ref{app:ddr-temp-stability}).
103	
104	
105	\subsection{Comparison with Detection Baselines}
106	\label{sec:results-baselines}
107	
108	Existing detection methods target binary real-vs-synthetic classification; we test whether their continuous scores incidentally encode recursive depth by repurposing four detection scores as ordinal depth predictors under identical XGBoost and LOGO conditions (Table~\ref{tab:baselines}).
109	
110	\begin{table}[t]
111	\centering
112	\footnotesize
113	\begin{tabular}{lcccc}
114	\toprule
115	\textbf{Method} & \textbf{Feat.} & \textbf{3-cl F1} & \textbf{Bin F1} & \textbf{ms/text} \\
116	\midrule
117	4-det.\ + surface     & 6 & \textbf{0.795} & \textbf{0.708} & 22.8 \\
118	4-detector ens.\      & 4 & 0.785 & 0.700 & 22.8 \\
119	7-feature (ours)      & 7 & 0.774 & 0.705 & \textbf{9.7} \\
120	\midrule
121	Avg-LogProb           & 1 & 0.707 & 0.673 & --- \\
122	FastDetectGPT         & 1 & 0.660 & 0.569 & --- \\
123	LD-Score              & 1 & 0.630 & 0.675 & --- \\
124	Binoculars            & 1 & 0.411 & 0.539 & --- \\
125	\bottomrule
126	\end{tabular}
127	\caption{Depth classification (8-gen LOGO, pooled evaluation; slightly higher than per-generator macro average in Table~\ref{tab:logo-results}). Identical XGBoost configuration. 7-feature: one 410M model (905\,MB); 4-det ensembles: two models, 1.4B params (2{,}868\,MB). Individual detection scores (N/A) share the reference-model forward pass; per-method timing is not separately profiled.}
128	\label{tab:baselines}
129	\end{table}
130	
131	\begin{figure}[t]
132	\centering
133	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.pdf}
134	\caption{LOGO binary F1 vs.\ inference cost in ms/text (8-gen pooled). The 7-feature ensemble (one 410M reference model) matches multi-detector ensembles (two models, 1.4B total) at 2.4$\times$ lower cost; individual detectors vary widely when repurposed for depth. Inference costs measured on a single NVIDIA RTX 5090.}
135	\label{fig:baseline-ci}
136	\end{figure}
137	
138	The 7-feature ensemble surpasses all individual baselines in 3-class F1 ($\Delta$\,=\,6.7--36.3\,pp; Figure~\ref{fig:baseline-ci}) and the pure 4-detector ensemble in binary F1 (0.705 vs.\ 0.700).
139	Adding DDR's surface features to the four detectors yields the highest binary F1 (0.708), marginally above the 7-feature set at 2.4$\times$ the inference cost.
140	This result underscores that DDR's primary contribution is not classification performance---where multi-detector ensembles match or marginally exceed it---but the decomposition of depth signal into location-sensitive and shape-stable components, a structural distinction absent from both binary detection methods and model collapse analyses (\S\ref{sec:discussion}).
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e65cbbd4-ba9c-4a16-b1c3-53ca62af377b",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "4a42263c-535c-4fe4-a73f-226e2116e634",
  "sourceToolAssistantUUID": "e65cbbd4-ba9c-4a16-b1c3-53ca62af377b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T08:39:54.643Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XHh4kfqcFqWWgRQcnrwMdZ`</summary>

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
  "parentUuid": "4a42263c-535c-4fe4-a73f-226e2116e634",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwgkQ91ZpYGxzpYsRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3ffaef17-4e21-422c-b9a4-b09c362ef517",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 6 · 2026-05-21T08:39:54.648Z_

<details><summary>↩ Tool result · `toolu_01XHh4kfqcFqWWgRQcnrwMdZ`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, we predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$: human-written ($d{=}0$), first-generation LLM output ($d{=}1$), or text produced by two or more recursive LLM generations ($d{=}2{+}$).
8	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$ (human corpus), $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic autoregressive generation.
9	Depths beyond 2 are merged into $2{+}$ because feature convergence compresses inter-class margins at deeper levels (\S\ref{sec:results-differential}).
10	
11	\subsection{Generation Chain Construction}
12	\label{sec:generation}
13	
14	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
15	This selection spans parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
16	
17	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
18	The same pool of seed passages serves as gen-0 for all generators.
19	We use shared seeds across generators so that cross-generator comparisons control for input content and isolate the effect of the generation model from source text variation.
20	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
21	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
22	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
23	We generate up to depth~4 to empirically confirm convergence: 5-class analysis shows adjacent depths 2--4 become indistinguishable (F1\,$\approx$\,0.27; Appendix~\ref{app:finer-depth}), motivating the gen-2+ class collapse.
24	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
25	After filtering chain breaks and passages too short for feature extraction, 37{,}058 texts remain across all depths (Appendix~\ref{app:dataset-stats}); depths 2--4 are collapsed into $2{+}$.
26	
27	\subsection{Feature Extraction}
28	\label{sec:features}
29	
30	The seven features operationalize two complementary views of distributional drift: reference-model features capture how the token-level NLL distribution shifts relative to a fixed model (location and shape statistics), while surface features capture how lexical diversity contracts under recursive generation (type-token statistics).
31	This dual-view design enables the location/shape decomposition that constitutes our primary finding.
32	We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition.
33	Cross-group ablation (\S\ref{sec:results-differential}) and leave-one-feature-out analysis (Appendix~\ref{app:lofo}) confirm that both feature groups contribute independently.
34	
35	We extract seven distributional features per text (Table~\ref{tab:features}), selected to provide principled coverage of the NLL distribution---location (mean), spread (std), extremes (max, min), and tail structure (decay)---complemented by two reference-free surface diversity measures.
36	We evaluated six additional NLL statistics (median, 90th percentile, IQR, CV, skewness, kurtosis) as candidate features; all exhibit $|r| > 0.65$ with existing features and yield no classification gain when added ($\Delta$F1\,$\leq$\,$-0.011$; Appendix~\ref{app:feature-candidate}).
37	
38	\begin{table}[t]
39	\centering
40	\footnotesize
41	\begin{tabular}{llp{3.8cm}}
42	\toprule
43	\textbf{Feature} & \textbf{Source} & \textbf{Measures} \\
44	\midrule
45	entropy\_mean & Ref.\ NLL & Central tendency of token surprise \\
46	entropy\_std  & Ref.\ NLL & Spread of token surprise \\
47	entropy\_max  & Ref.\ NLL & Maximum token surprise \\
48	entropy\_min  & Ref.\ NLL & Minimum token surprise \\
49	tail\_decay   & Ref.\ NLL & Log-prob decay slope (ranks 100--1K) \\
50	\midrule
51	TTR           & Surface & Type-token ratio \\
52	hapax\_ratio  & Surface & Proportion of hapax legomena \\
53	\bottomrule
54	\end{tabular}
55	\caption{Seven distributional features. Reference features use Pythia-410M per-token NLL; surface features require no reference model. DDR analysis (\S\ref{sec:results-differential}) reveals that the first three drift with depth while the last four remain stable.}
56	\label{tab:features}
57	\end{table}
58	
59	\paragraph{Reference-model features.}
60	A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
61	We use ``entropy'' as shorthand for token-level NLL throughout, following convention in prior detection work; these are point-wise NLL values, not Shannon entropy of the full distribution.
62	Although Pythia-410M shares the GPT-NeoX architecture with two of the eight generators, cross-family reference model experiments (\S\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by $\leq$0.013 across Pythia, OLMo, and Qwen references).
63	From the resulting NLL sequence, we extract five statistics: mean, standard deviation, maximum, and minimum of the token-level NLL, plus tail\_decay---the slope of the vocabulary-level averaged log-probability distribution in the mid-rank region (ranks 100--1000), capturing how steeply probability mass decays beyond high-frequency tokens.
64	
65	\paragraph{Surface features.}
66	Two features capture lexical diversity without requiring a reference model: type-token ratio (TTR) and the proportion of words appearing exactly once (hapax\_ratio).
67	
68	\paragraph{Feature complementarity.}
69	These features exhibit a \emph{differential depth response} (DDR), separating into drifting and non-drifting groups (\S\ref{sec:results-differential}; pairwise correlations in Appendix~\ref{sec:appendix-feature-correlation}).
70	TTR and hapax ratio are strongly correlated ($r = 0.97$); both are retained for marginal LOFO gains.
71	
72	\subsection{Evaluation Protocol}
73	\label{sec:evaluation}
74	
75	\paragraph{Cross-validation.}
76	To evaluate generalization, we use \textbf{Leave-One-Generator-Out (LOGO)} cross-validation over all eight generators.
77	LOGO holds out individual generators but does not isolate family effects; \textbf{Leave-One-Family-Out (LOFO)} addresses this by holding out entire model families (binary F1\,=\,0.686; \S\ref{sec:results-classification}).
78	Generator subsets vary across experiments (Appendix~\ref{app:gen-subsets-section}).
79	
80	\paragraph{Classifier.}
81	We use XGBoost \cite{xgboost} throughout ($n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, learning rate $0.1$), with identical hyperparameters across all methods in Table~\ref{tab:baselines}.
82	Alternative classifiers (CORAL \cite{coral_ordinal}, CORN \cite{corn_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance (Appendix~\ref{app:classifier}); discriminative power resides in the features, not the classifier.
83	
84	\paragraph{Metrics and statistical testing.}
85	The primary metric is \textbf{macro-averaged F1} over the three depth classes, with 95\% bootstrap CIs ($n{=}1{,}000$).
86	All $p$-values are two-sided with Bonferroni correction within each family of simultaneous tests.
87	
88	\paragraph{Baselines.}
89	We compare the 7-feature ensemble against four single-score detection methods repurposed as depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
90	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation to ensure a controlled comparison.
91	
92	\paragraph{Length confound control.}
93	Since TTR and hapax\_ratio are mechanically length-dependent, we verify depth signal is not a length artifact via length-matched subsampling that equalizes length distributions across depth classes (\S\ref{sec:results-classification}; Appendix~\ref{app:length}).
94	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ffaef17-4e21-422c-b9a4-b09c362ef517",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "68d6fda5-100c-4a3d-8338-91e6c39843e7",
  "sourceToolAssistantUUID": "3ffaef17-4e21-422c-b9a4-b09c362ef517",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T08:39:55.084Z_

<details open><summary>🔧 Tool call — Read · `toolu_019i3mY14Gvq87YdGhkEisjr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68d6fda5-100c-4a3d-8338-91e6c39843e7",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwgkQ91ZpYGxzpYsRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "80e2d4c4-9510-4726-abf6-fd724f486dce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 8 · 2026-05-21T08:39:55.089Z_

<details><summary>↩ Tool result · `toolu_019i3mY14Gvq87YdGhkEisjr`</summary>

```text
1	To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
2	
3	\paragraph{Setup.}
4	We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).\footnote{Evaluated on the original 6-generator subset; XGBoost 3-class F1\,=\,0.789. We expect 8-generator training to further improve given additional diversity; the comparison direction is preserved.}
5	For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
6	All results use the same LOGO protocol as the main experiments.
7	
8	\begin{table}[ht]
9	\centering
10	\small
11	\caption{QLoRA end-to-end depth classification vs.\ XGBoost on handcrafted features, under LOGO evaluation.}
12	\label{tab:qlora}
13	\resizebox{\linewidth}{!}{%
14	\begin{tabular}{lccc}
15	\toprule
16	\textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
17	\midrule
18	XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
19	QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	\paragraph{Results.}
25	QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).
26	On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
27	The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
28	
29	\paragraph{Hyperparameter robustness.}
30	A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), which confirms stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).
31	
32	\paragraph{Implications.}
33	The substantial 3-class improvement demonstrates that raw token embeddings contain depth signal beyond what summary statistics capture; the seven handcrafted features are a strong but lossy compression of the full distributional information.
34	End-to-end fine-tuning exploits token-level patterns (e.g., positional regularities, n-gram repetitions) that aggregate features cannot represent.
35	This confirms that the depth signal documented in our main analysis is real and exploitable beyond engineered features, while the handcrafted approach retains practical advantages: interpretability, computational efficiency (no GPU inference), and the ability to reveal the differential depth response pattern that motivates the task formulation.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80e2d4c4-9510-4726-abf6-fd724f486dce",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "1c57a41d-ed13-4d1c-8365-e53f225195db",
  "sourceToolAssistantUUID": "80e2d4c4-9510-4726-abf6-fd724f486dce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T08:39:55.292Z_

<details open><summary>🔧 Tool call — Read · `toolu_019rfvz1HcKSy2LxpbW3DoMz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c57a41d-ed13-4d1c-8365-e53f225195db",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwgkQ91ZpYGxzpYsRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "58d69c23-e260-4822-9ac7-b8ce8c098bb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 10 · 2026-05-21T08:39:55.297Z_

<details><summary>↩ Tool result · `toolu_019rfvz1HcKSy2LxpbW3DoMz`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	The detection literature spans statistical tests \cite{gltr,grover,release_strategies}, zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, surprisal diversity \cite{diveye}, geometric invariants \cite{intrinsic_dim_detection}, and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
8	RAID \cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation.
9	Several recent efforts move beyond the binary boundary---collaboration roles \cite{beyond_binary}, joint detection-attribution \cite{two_birds}, creator-editor modes \cite{beyond_final_actor}, multi-generator attribution \cite{semeval2024_task8}---but all taxonomize by \emph{source} or \emph{production mode}, not recursive generation \emph{depth}; repurposing their scores as depth predictors reveals high cross-generator variance (binary F1\,=\,0.52--0.71; Table~\ref{tab:baselines}) \cite{paraphrase_evades,detection_possibilities}.
10	Our contribution is orthogonal: ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task, and the finding that combining drifting and stationary features yields consistent cross-generator performance where individual detection scores show high variance \cite{uchendu_attribution,munir_looking_glass}.
11	
12	\subsection{Model Collapse and Iterative Generation}
13	\label{sec:related-collapse}
14	
15	Self-consuming generative models progressively lose distributional coverage \cite{self_consuming_mad,curse_of_recursion,briesch_self_consuming,seddik_synthetic_data}, though data mixing mitigates collapse \cite{model_collapse_avoidable,strong_model_collapse}.
16	These studies address \emph{training-loop} degradation where parameter updates erode tail coverage; indeed, \citet{schaeffer_collapse_position} identify eight distinct definitions of ``collapse,'' most tied to retraining dynamics.
17	We study \emph{inference chains} where parameters are fixed and only the input distribution evolves.
18	Two concurrent works are most directly relevant: \citet{broken_telephone} analyze paraphrasing and translation chains, documenting progressive information loss, while \citet{markovian_chains} demonstrate attractor dynamics that bound distinguishable depth to approximately three classes; \citet{attractor_cycles} provide complementary evidence that LLM outputs converge to cyclic attractor states under repeated generation.
19	We study \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal, and offer a complementary decomposition: where these works characterize \emph{that} and \emph{why} convergence occurs, DDR isolates \emph{what} converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.
20	The independent convergence of all three approaches on ${\sim}$3 distinguishable depth classes---via Markovian dynamics \cite{markovian_chains}, information-theoretic loss \cite{broken_telephone}, and distributional feature compression (this work)---points to a shared resolution ceiling in recursive text generation (Table~\ref{tab:iterative-comparison} in Appendix~\ref{app:iterative-comparison} provides a structured comparison).
21	
22	\subsection{Vocabulary Diversity and Stylometry}
23	\label{sec:related-diversity}
24	
25	Declining lexical diversity in LLM text is documented in both training \cite{curious_decline} and deployment settings \cite{writing_diversity}; MAUVE \cite{mauve} provides a divergence-based metric for quantifying this distributional gap.
26	Our surface features (TTR, hapax ratio) are classical stylometric measures \cite{stamatatos_survey,koppel_authorship}; we repurpose them from generator identity \cite{uchendu_attribution} to the depth dimension, where their monotonic decline under top-$p$ sampling \cite{nucleus_sampling} constitutes a drifting component of DDR.
27	
28	\subsection{Data Quality and Provenance}
29	\label{sec:related-provenance}
30	
31	Scalable data curation relies on quality signals \cite{dsir,qurating,ccnet}; generation depth offers a complementary provenance axis.
32	Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns but degrades across multi-step chains \cite{chainwash}, motivating passive approaches.
33	Our NLL-based analysis connects to \citet{min_k_percent} (probability-tail membership inference) but extends from binary membership to full distributional decomposition for ordinal depth.
34	\citet{koike_mia_detection} formalize this connection from the opposite direction, showing that detection scores implicitly perform membership inference, underscoring the shared statistical basis of detection and provenance.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58d69c23-e260-4822-9ac7-b8ce8c098bb6",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "09c97bae-6437-441e-bd96-ed25b1fa7c18",
  "sourceToolAssistantUUID": "58d69c23-e260-4822-9ac7-b8ce8c098bb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T08:39:55.505Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TrR8ND26veZrS6PkFaRLkE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09c97bae-6437-441e-bd96-ed25b1fa7c18",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwgkQ91ZpYGxzpYsRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2d00ea9c-f471-428a-bc66-c1e9e4bcab69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 12 · 2026-05-21T08:39:55.717Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QVh46urg3UDr1bkb264nV8`</summary>

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
  "parentUuid": "2d00ea9c-f471-428a-bc66-c1e9e4bcab69",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwgkQ91ZpYGxzpYsRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6dd9ca73-7ba9-4b49-8079-af2fc2ce3338",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 13 · 2026-05-21T08:39:55.781Z_

<details><summary>↩ Tool result · `toolu_01TrR8ND26veZrS6PkFaRLkE`</summary>

```text
1	% ===== Data Provenance / Contamination =====
2	
3	% ===== Statistics =====
4	
5	@book{cohen1988statistical,
6	  title = {{Statistical Power Analysis for the Behavioral Sciences}},
7	  author = {Cohen, Jacob},
8	  edition = {2nd},
9	  publisher = {Lawrence Erlbaum Associates},
10	  year = {1988},
11	}
12	
13	% ===== Detection =====
14	
15	@inproceedings{detectgpt,
16	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
17	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
18	  booktitle = {Proceedings of the International Conference on Machine Learning},
19	  year = {2023},
20	}
21	
22	@inproceedings{gltr,
23	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
24	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
25	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
26	  year = {2019},
27	}
28	
29	@inproceedings{dna_gpt,
30	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
31	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
32	  booktitle = {Proceedings of the International Conference on Learning Representations},
33	  year = {2024},
34	}
35	
36	@inproceedings{binoculars,
37	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
38	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
39	  booktitle = {Proceedings of the International Conference on Machine Learning},
40	  year = {2024},
41	}
42	
43	@inproceedings{fast_detectgpt,
44	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
45	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
46	  booktitle = {Proceedings of the International Conference on Learning Representations},
47	  year = {2024},
48	}
49	
50	@article{ld_score,
51	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
52	  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},
53	  journal = {arXiv preprint arXiv:2605.01647},
54	  year = {2026},
55	}
56	
57	@inproceedings{diveye,
58	  title = {{Diversity Boosts AI-Generated Text Detection}},
59	  author = {Basani, Advik Raj and Chen, Pin-Yu},
60	  booktitle = {Proceedings of the International Conference on Learning Representations},
61	  year = {2026},
62	  eprint = {2509.18880},
63	  archiveprefix = {arXiv},
64	}
65	
66	@article{feat_aug_transformer,
67	  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},
68	  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\"o}rn},
69	  journal = {arXiv preprint arXiv:2605.03969},
70	  year = {2026},
71	}
72	
73	@article{reliable_detection,
74	  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},
75	  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
76	  journal = {Transactions on Machine Learning Research},
77	  year = {2025},
78	  url = {https://openreview.net/forum?id=OOgsAZdFOt},
79	}
80	
81	@inproceedings{paraphrase_evades,
82	  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},
83	  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
84	  booktitle = {Advances in Neural Information Processing Systems},
85	  year = {2023},
86	}
87	
88	@inproceedings{detection_possibilities,
89	  title = {{Position: On the Possibilities of AI-Generated Text Detection}},
90	  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},
91	  booktitle = {Proceedings of the International Conference on Machine Learning},
92	  year = {2024},
93	}
94	
95	@inproceedings{intrinsic_dim_detection,
96	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
97	  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
98	  booktitle = {Advances in Neural Information Processing Systems},
99	  year = {2023},
100	}
101	
102	@inproceedings{grover,
103	  title = {{Defending Against Neural Fake News}},
104	  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
105	  booktitle = {Advances in Neural Information Processing Systems},
106	  year = {2019},
107	}
108	
109	@article{release_strategies,
110	  title = {{Release Strategies and the Social Impacts of Language Models}},
111	  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
112	  journal = {arXiv preprint arXiv:1908.09203},
113	  year = {2019},
114	}
115	
116	@inproceedings{beyond_binary,
117	  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
118	  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
119	  booktitle = {Proceedings of the ACM Web Conference},
120	  year = {2025},
121	}
122	
123	@inproceedings{semeval2024_task8,
124	  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
125	  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
126	  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
127	  year = {2024},
128	}
129	
130	% ===== Model Collapse =====
131	
132	@inproceedings{self_consuming_mad,
133	  title = {{Self-Consuming Generative Models Go MAD}},
134	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
135	  booktitle = {Proceedings of the International Conference on Learning Representations},
136	  year = {2024},
137	}
138	
139	@article{curse_of_recursion,
140	  title = {{AI models collapse when trained on recursively generated data}},
141	  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
142	  journal = {Nature},
143	  volume = {631},
144	  pages = {755--759},
145	  year = {2024},
146	}
147	
148	@inproceedings{strong_model_collapse,
149	  title = {{Strong Model Collapse}},
150	  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
151	  booktitle = {Proceedings of the International Conference on Learning Representations},
152	  year = {2025},
153	}
154	
155	@inproceedings{model_collapse_avoidable,
156	  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
157	  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
158	  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},
159	  year = {2024},
160	}
161	
162	@inproceedings{schaeffer_collapse_position,
163	  title = {{Position: Model Collapse Does Not Mean What You Think}},
164	  author = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
165	  booktitle = {Proceedings of the International Conference on Machine Learning},
166	  year = {2025},
167	  eprint = {2503.03150},
168	  archiveprefix = {arXiv},
169	}
170	
171	@inproceedings{drayson_detection_prevents_collapse,
172	  title = {{Machine-Generated Text Detection Prevents Language Model Collapse}},
173	  author = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
174	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
175	  year = {2025},
176	  eprint = {2502.15654},
177	  archiveprefix = {arXiv},
178	}
179	
180	@article{seddik_synthetic_data,
181	  title = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},
182	  author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},
183	  journal = {arXiv preprint arXiv:2404.05090},
184	  year = {2024},
185	}
186	
187	% ===== Fine-tuning =====
188	
189	@inproceedings{qlora,
190	  title = {{QLoRA: Efficient Finetuning of Quantized LLMs}},
191	  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
192	  booktitle = {Advances in Neural Information Processing Systems},
193	  year = {2023},
194	}
195	
196	% ===== Data Quality =====
197	
198	% ===== (orphan entries removed: fineweb, dolma) =====
199	
200	@inproceedings{dsir,
201	  title = {{Data Selection for Language Models via Importance Resampling}},
202	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
203	  booktitle = {Advances in Neural Information Processing Systems},
204	  year = {2023},
205	}
206	
207	@inproceedings{qurating,
208	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
209	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
210	  booktitle = {Proceedings of the International Conference on Machine Learning},
211	  year = {2024},
212	}
213	
214	@inproceedings{ccnet,
215	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
216	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
217	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
218	  year = {2020},
219	}
220	
221	% ===== Watermarking =====
222	
223	@inproceedings{watermark_llm,
224	  title = {{A Watermark for Large Language Models}},
225	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
226	  booktitle = {Proceedings of the International Conference on Machine Learning},
227	  year = {2023},
228	}
229	
230	@article{synthid_text,
231	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
232	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
233	  journal = {Nature},
234	  volume = {634},
235	  pages = {818--823},
236	  year = {2024},
237	}
238	
239	@misc{aaronson_watermark,
240	  title = {{Watermarking GPT Outputs}},
241	  author = {Aaronson, Scott and Kirchner, Jan Hendrik},
242	  year = {2022},
243	  note = {Blog post},
244	  url = {https://scottaaronson.blog/?p=6823},
245	}
246	
247	@article{chainwash,
248	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
249	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
250	  journal = {arXiv preprint arXiv:2605.05503},
251	  year = {2026},
252	}
253	
254	% ===== Vocabulary Diversity =====
255	
256	@inproceedings{curious_decline,
257	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
258	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
259	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
260	  year = {2024},
261	}
262	
263	@inproceedings{writing_diversity,
264	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
265	  author = {Padmakumar, Vishakh and He, He},
266	  booktitle = {Proceedings of the International Conference on Learning Representations},
267	  year = {2024},
268	}
269	
270	@inproceedings{nucleus_sampling,
271	  title = {{The Curious Case of Neural Text Degeneration}},
272	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
273	  booktitle = {Proceedings of the International Conference on Learning Representations},
274	  year = {2020},
275	}
276	
277	% ===== Stylometry =====
278	
279	@article{stamatatos_survey,
280	  title = {{A Survey of Modern Authorship Attribution Methods}},
281	  author = {Stamatatos, Efstathios},
282	  journal = {Journal of the American Society for Information Science and Technology},
283	  volume = {60},
284	  number = {3},
285	  pages = {538--556},
286	  year = {2009},
287	}
288	
289	@article{koppel_authorship,
290	  title = {{Computational Methods in Authorship Attribution}},
291	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
292	  journal = {Journal of the American Society for Information Science and Technology},
293	  volume = {60},
294	  number = {1},
295	  pages = {9--26},
296	  year = {2009},
297	}
298	
299	@inproceedings{uchendu_attribution,
300	  title = {{Authorship Attribution for Neural Text Generation}},
301	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
302	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
303	  year = {2020},
304	}
305	
306	@inproceedings{munir_looking_glass,
307	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
308	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
309	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
310	  year = {2021},
311	}
312	
313	@article{briesch_self_consuming,
314	  title = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},
315	  author = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},
316	  journal = {arXiv preprint arXiv:2311.16822},
317	  year = {2023},
318	}
319	
320	% ===== Iterative Generation =====
321	
322	@inproceedings{broken_telephone,
323	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
324	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
325	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
326	  year = {2025},
327	}
328	
329	@article{markovian_chains,
330	  title = {{Markovian Generation Chains in Large Language Models}},
331	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
332	  journal = {arXiv preprint arXiv:2603.11228},
333	  year = {2026},
334	}
335	
336	@inproceedings{attractor_cycles,
337	  title = {{Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing}},
338	  author = {Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue},
339	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
340	  year = {2025},
341	  eprint = {2502.15208},
342	  archiveprefix = {arXiv},
343	}
344	
345	% ===== Membership Inference =====
346	
347	@inproceedings{min_k_percent,
348	  title = {{Detecting Pretraining Data from Large Language Models}},
349	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
350	  booktitle = {Proceedings of the International Conference on Learning Representations},
351	  year = {2024},
352	}
353	
354	@article{koike_mia_detection,
355	  title = {{Machine Text Detectors are Membership Inference Attacks}},
356	  author = {Koike, Ryuto and Dugan, Liam and Kaneko, Masahiro and Callison-Burch, Chris and Okazaki, Naoaki},
357	  journal = {arXiv preprint arXiv:2510.19492},
358	  year = {2025},
359	}
360	
361	% ===== Survey =====
362	
363	@article{wu_survey_2025,
364	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
365	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
366	  journal = {Computational Linguistics},
367	  publisher = {MIT Press},
368	  year = {2025},
369	}
370	
371	@inproceedings{jawahar_survey,
372	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
373	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
374	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
375	  year = {2020},
376	}
377	
378	% ===== Models =====
379	
380	@inproceedings{pythia,
381	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
382	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
383	  booktitle = {Proceedings of the International Conference on Machine Learning},
384	  year = {2023},
385	}
386	
387	@inproceedings{olmo,
388	  title = {{OLMo: Accelerating the Science of Language Models}},
389	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
390	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
391	  year = {2024},
392	}
393	
394	@article{qwen3,
395	  title = {{Qwen3 Technical Report}},
396	  author = {{Qwen Team}},
397	  journal = {arXiv preprint arXiv:2505.09388},
398	  year = {2025},
399	}
400	
401	@inproceedings{ghostbuster,
402	  title = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},
403	  author = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},
404	  booktitle = {Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},
405	  year = {2024},
406	}
407	
408	@article{two_birds,
409	  title = {{Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text}},
410	  author = {Rao, Zixin and Mohamed, Youssef and Liu, Shang and Liu, Zeyan},
411	  journal = {arXiv preprint arXiv:2508.14190},
412	  year = {2025},
413	}
414	
415	@inproceedings{beyond_final_actor,
416	  title = {{Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection}},
417	  author = {Li, Yang and Sheng, Qiang and Wang, Zhengjia and Yang, Yehan and Wang, Danding and Cao, Juan},
418	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
419	  year = {2026},
420	}
421	
422	% ===== Machine Learning =====
423	
424	@article{gutierrez_ordinal_survey,
425	  title = {{Ordinal Regression Methods: Survey and Experimental Study}},
426	  author = {Guti{\'e}rrez, Pedro Antonio and P{\'e}rez-Ortiz, Mar{\'i}a and S{\'a}nchez-Monedero, Javier and Fern{\'a}ndez-Navarro, Francisco and Herv{\'a}s-Mart{\'i}nez, C{\'e}sar},
427	  journal = {IEEE Transactions on Knowledge and Data Engineering},
428	  volume = {28},
429	  number = {1},
430	  pages = {127--146},
431	  year = {2016},
432	}
433	
434	@article{coral_ordinal,
435	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
436	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
437	  journal = {Pattern Recognition Letters},
438	  volume = {140},
439	  pages = {325--331},
440	  year = {2020},
441	}
442	
443	@inproceedings{frank_hall_ordinal,
444	  title = {{A Simple Approach to Ordinal Classification}},
445	  author = {Frank, Eibe and Hall, Mark},
446	  booktitle = {Proceedings of the European Conference on Machine Learning},
447	  year = {2001},
448	}
449	
450	@article{corn_ordinal,
451	  title = {{Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities}},
452	  author = {Shi, Xintong and Cao, Wenzhi and Raschka, Sebastian},
453	  journal = {Pattern Analysis and Applications},
454	  volume = {26},
455	  pages = {941--955},
456	  year = {2023},
457	}
458	
459	@inproceedings{kasa_ordinality_nlp,
460	  title = {{Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques}},
461	  author = {Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and Roychowdhury, Sumegh and Priyatam, Pattisapu and Bhanushali, Anish and Murthy, Prasanna Srinivasa},
462	  booktitle = {Findings of the Association for Computational Linguistics: ACL},
463	  year = {2024},
464	}
465	
466	@inproceedings{xgboost,
467	  title = {{XGBoost: A Scalable Tree Boosting System}},
468	  author = {Chen, Tianqi and Guestrin, Carlos},
469	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
470	  year = {2016},
471	}
472	
473	@article{lakens_equivalence,
474	  title = {{Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses}},
475	  author = {Lakens, Dani{\"e}l},
476	  journal = {Social Psychological and Personality Science},
477	  volume = {8},
478	  number = {4},
479	  pages = {355--362},
480	  year = {2017},
481	}
482	
483	% ===== Generator Model References =====
484	
485	@article{llama3,
486	  title = {{The Llama 3 Herd of Models}},
487	  author = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others},
488	  journal = {arXiv preprint arXiv:2407.21783},
489	  year = {2024},
490	}
491	
492	@article{mistral7b,
493	  title = {{Mistral 7B}},
494	  author = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others},
495	  journal = {arXiv preprint arXiv:2310.06825},
496	  year = {2023},
497	}
498	
499	@article{strobl_conditional_2008,
500	  title = {Conditional Variable Importance for Random Forests},
501	  author = {Strobl, Carolin and Boulesteix, Anne-Laure and Kneib, Thomas and Augustin, Thomas and Zeileis, Achim},
502	  journal = {BMC Bioinformatics},
503	  volume = {9},
504	  pages = {307},
505	  year = {2008},
506	}
507	
508	% --- Entries from Paper Agent (docs/paper) ---
509	
510	@inproceedings{dolma,
511	  title = {{Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research}},
512	  author = {Soldaini, Luca and Kinney, Rodney and Bhagia, Akshita and Schwenk, Dustin and Atkinson, David and Authur, Russell and Bogin, Ben and Chandu, Khyathi and Dumas, Jennifer and Elazar, Yanai and Hofmann, Valentin and Jha, Ananya Harsh and Kumar, Sachin and Lucy, Li and Lyu, Xinxi and Lambert, Nathan and Magnusson, Ian and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Ravichander, Abhilasha and Richardson, Kyle and Shen, Zejiang and Strubell, Emma and Subramani, Nishant and Tafjord, Oyvind and Walsh, Evan Pete and Zettlemoyer, Luke and Smith, Noah A. and Hajishirzi, Hannaneh and Beltagy, Iz and Groeneveld, Dirk and Dodge, Jesse and Lo, Kyle},
513	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
514	  year = {2024},
515	}
516	
517	
518	@inproceedings{fineweb,
519	  title = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},
520	  author = {Penedo, Guilherme and Kydl{\'\i}{\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},
521	  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},
522	  year = {2024},
523	}
524	
525	
526	@inproceedings{mapping_llm_science,
527	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
528	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
529	  booktitle = {Proceedings of the Conference on Language Modeling},
530	  year = {2024},
531	}
532	
533	
534	@inproceedings{monitoring_ai_review,
535	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
536	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
537	  booktitle = {Proceedings of the International Conference on Machine Learning},
538	  year = {2024},
539	}
540	
541	% ===== Stylometry =====
542	
543	
544	
545	@inproceedings{raid,
546	  title = {{RAID}: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors},
547	  author = {Dugan, Liam and Hwang, Alyssa and Trhl{\'\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},
548	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
549	  year = {2024},
550	  address = {Bangkok, Thailand},
551	  publisher = {Association for Computational Linguistics},
552	  pages = {12463--12492},
553	}
554	
555	% ===== Distribution Quality =====
556	
557	@inproceedings{mauve,
558	  title = {{MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers}},
559	  author = {Pillutla, Krishna and Swayamdipta, Swabha and Zellers, Rowan and Thickstun, John and Welleck, Sean and Choi, Yejin and Harchaoui, Zaid},
560	  booktitle = {Advances in Neural Information Processing Systems},
561	  year = {2021},
562	}
563	
564	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d00ea9c-f471-428a-bc66-c1e9e4bcab69",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "d6db34b3-feba-4cb9-a831-608b449bf17a",
  "sourceToolAssistantUUID": "2d00ea9c-f471-428a-bc66-c1e9e4bcab69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T08:39:55.723Z_

<details><summary>↩ Tool result · `toolu_01QVh46urg3UDr1bkb264nV8`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	AI text detection asks a single binary question---\emph{human or machine?}---and recent methods answer it with increasing reliability \cite{detectgpt,fast_detectgpt,binoculars,ld_score}.
5	Yet this framing elides a richer structure emerging on the open web: as LLM outputs re-enter training corpora \cite{dolma,fineweb} and seed further generation, text accumulates at varying \emph{recursive depths}---an estimated 7--17\% of recent scientific publications already contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}---and each generation cycle pushes distributional properties further from both the human source and the first-generation predecessor.
6	While most deployed LLM outputs use instruction-tuned models, base-model generation pipelines remain prevalent in synthetic data production, pre-training corpus construction, and recursive data augmentation; we accordingly scope this study to base (pretrained) models.
7	Knowing \emph{how many times} text has been recursively generated matters for data provenance \cite{ccnet,dsir} and model collapse analysis \cite{curse_of_recursion,strong_model_collapse}, yet no current method moves beyond the binary boundary.
8	
9	Distributional compression under recursive generation is well-documented \cite{curious_decline,broken_telephone,markovian_chains}.
10	We introduce \emph{depth fingerprinting}---classifying text by ordinal generation depth (gen-0\,/\,gen-1\,/\,gen-2+)---and decompose this compression into structurally distinct components: across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy, lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) remains an order of magnitude more stable ($d{=}0.76$--$1.17$ vs.\ $d < 0.10$; convergence across parametric and non-parametric effect-size measures confirms this partition).
11	We term this location/shape asymmetry the \emph{differential depth response} (DDR)---a structural property of fixed-parameter autoregressive sampling that is mechanistically distinct from the tail-coverage erosion in model collapse \cite{curse_of_recursion} and analytically informative independent of both the specific mechanism and classification accuracy.
12	Where concurrent work characterizes \emph{that} and \emph{why} convergence occurs \cite{broken_telephone,markovian_chains}, DDR isolates \emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.
13	
14	As a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at $2.4\times$ lower cost; an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features.
15	
16	Our contributions:
17	\begin{enumerate}[nosep,leftmargin=*]
18	    \item \textbf{Empirical decomposition (DDR).} Clustering-based validation ($k{=}2$, silhouette\,=\,0.660) confirms that inference-chain drift separates into a drifting location component ($d{=}0.76$--$1.17$) and a stable shape component ($d < 0.10$). Where prior work documents \emph{what converges}---diversity loss \cite{curious_decline}, attractor dynamics \cite{markovian_chains}---DDR identifies \emph{what is preserved}: shape invariance provides the cross-generator reference needed for depth detection without per-generator calibration.
19	    \item \textbf{Task formulation and evaluation suite.} We define generation depth classification as an ordinal prediction task and construct a controlled dataset of 37K texts from eight generators across five families (0.6B--8B), with leave-one-generator-out cross-validation as the primary evaluation protocol.
20	\end{enumerate}
21	A proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dd9ca73-7ba9-4b49-8079-af2fc2ce3338",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "693333a2-0fae-486c-aa21-89a3f612561b",
  "sourceToolAssistantUUID": "6dd9ca73-7ba9-4b49-8079-af2fc2ce3338",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T08:39:55.927Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WyF41sgEzGEcwi9L4tKr91`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "693333a2-0fae-486c-aa21-89a3f612561b",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwgkQ91ZpYGxzpYsRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "37548ae6-ed9a-43cf-a4e2-980a5c6cf5f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 16 · 2026-05-21T08:39:55.933Z_

<details><summary>↩ Tool result · `toolu_01WyF41sgEzGEcwi9L4tKr91`</summary>

```text
1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{placeins}
15	\usepackage{multirow}
16	\usepackage{float}
17	
18	\graphicspath{{../chart/}}
19	
20	\title{Depth Fingerprinting: Classifying Recursive Generation Depth\\in Base-Model LLM Text}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{abstract}
28	
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{results}
33	
34	\input{discussion}
35	\input{conclusion}
36	\input{limitations}
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	
43	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
44	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
45	
46	\input{appendix_dataset_stats}
47	
48	\section{Length Confound Analysis}
49	\label{app:length}
50	\input{appendix_length}
51	
52	\section{Prompt Type Generalization}
53	\label{app:prompt-type}
54	\input{appendix_prompt_type}
55	
56	\section{Finer-Grained Depth Classification}
57	\label{app:finer-depth}
58	\input{appendix_finer_depth}
59	
60	\section{End-to-End Depth Classification (QLoRA)}
61	\label{app:qlora}
62	\input{appendix_qlora}
63	
64	\section{Leave-One-Feature-Out Analysis}
65	\label{app:lofo}
66	\input{appendix_lofo}
67	
68	\subsection{Candidate Feature Screening}
69	\label{app:feature-candidate}
70	\input{appendix_feature_candidates}
71	
72	\section{Confusion Matrix}
73	\label{app:confusion}
74	\input{appendix_confusion_matrix}
75	
76	\section{Classifier Sensitivity}
77	\label{app:classifier}
78	\input{appendix_classifier}
79	\FloatBarrier
80	
81	\section{Robustness to Text Perturbation}
82	\label{app:human-edit}
83	\input{appendix_human_edit}
84	
85	\section{Cross-Domain Generalization}
86	\label{app:domain}
87	\input{appendix_domain}
88	
89	\section{Instruction-Tuned Model Analysis}
90	\label{app:instruct}
91	\input{appendix_instruct}
92	
93	\section{Error Analysis of Binary Classification}
94	\label{app:error-analysis}
95	\input{appendix_error_analysis}
96	
97	\section{Downstream Utility}
98	\label{app:downstream}
99	\input{appendix_downstream}
100	
101	\section{Cross-Model Chain Per-Class Detail}
102	\label{app:cross-model-detail}
103	\input{appendix_cross_model_detail}
104	
105	\section{Feature Distribution Analysis}
106	\label{app:feature-distributions}
107	\input{appendix_feature_distributions}
108	
109	\section{Cross-Temperature Transfer}
110	\label{app:cross-temp}
111	\input{appendix_cross_temp}
112	\FloatBarrier
113	
114	\section{Feature Ablation}
115	\label{app:ablation-table}
116	\input{appendix_ablation}
117	
118	\input{appendix_feature_correlation}
119	
120	\section{Cross-Family Reference Models}
121	\label{app:cross-ref}
122	\input{table4}
123	
124	\input{appendix_seed_control}
125	
126	\input{appendix_tost}
127	\FloatBarrier
128	
129	\input{appendix_tost_bootstrap}
130	
131	\section{DDR Partition Validation}
132	\label{app:ddr-validation}
133	\input{appendix_ddr_validation}
134	\FloatBarrier
135	
136	\section{Generator Subset Summary}
137	\label{app:gen-subsets-section}
138	\input{appendix_generator_subsets}
139	
140	\input{appendix_qualitative_examples}
141	
142	\section{Cross-Generator Transfer Analysis}
143	\label{app:transfer}
144	\input{appendix_transfer}
145	\FloatBarrier
146	
147	\section{Supplementary DDR Characterization}
148	\label{app:ddr-supplement}
149	
150	\subsection{Partition Stability Across Temperatures}
151	\label{app:ddr-temp-stability}
152	\input{appendix_temperature_stability}
153	
154	\subsection{Per-Feature Convergence Dynamics}
155	\label{app:convergence}
156	\input{appendix_convergence}
157	\FloatBarrier
158	
159	\subsection{DDR Causality Analysis}
160	\label{app:ddr-causality}
161	\input{appendix_ddr_causality}
162	
163	\subsection{Decoding Strategy Robustness}
164	\label{app:decoding-strategy}
165	\input{appendix_decoding_strategy}
166	
167	\input{appendix_9gen_scale}
168	
169	\subsection{Comparison with Concurrent Iterative-Generation Studies}
170	\label{app:iterative-comparison}
171	\input{appendix_iterative_comparison}
172	
173	\subsection{Token-Level NLL Distribution}
174	\label{app:nll-distribution}
175	\input{appendix_nll_distribution}
176	
177	\end{document}
178	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37548ae6-ed9a-43cf-a4e2-980a5c6cf5f9",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "1d9e7b86-2cf3-43ae-8b5f-44ced95c538c",
  "sourceToolAssistantUUID": "37548ae6-ed9a-43cf-a4e2-980a5c6cf5f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T08:39:56.133Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DrTVezSoUSbuNbGYdPQZcU`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d9e7b86-2cf3-43ae-8b5f-44ced95c538c",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwgkQ91ZpYGxzpYsRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6e29f4c3-5d73-43cc-8f21-8f8619dffe70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "output_tokens": 618,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17198
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 618,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17198,
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

_source line 18 · 2026-05-21T08:39:56.144Z_

<details><summary>↩ Tool result · `toolu_01DrTVezSoUSbuNbGYdPQZcU`</summary>

```text
artifacts/_project/chart/fig1_ddr_v2.py
artifacts/_project/chart/fig1_combined_v1.py
artifacts/_project/chart/fig1_ddr_v3.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e29f4c3-5d73-43cc-8f21-8f8619dffe70",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "8b7d1a97-8249-4ee5-87da-2084bae0abfb",
  "sourceToolAssistantUUID": "6e29f4c3-5d73-43cc-8f21-8f8619dffe70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T08:39:58.588Z_

Now let me perform the grep searches across all .tex files in the docs/paper directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b7d1a97-8249-4ee5-87da-2084bae0abfb",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwxHYArqbg5ECsVat3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3c68c25f-b662-4edb-8665-5f19b619a494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 20 · 2026-05-21T08:39:59.668Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JK9SNTTUbJgjyiDR6P2BGf`</summary>

```json
{
  "pattern": "recursive generation depth",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c68c25f-b662-4edb-8665-5f19b619a494",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwxHYArqbg5ECsVat3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ca941af8-d57d-45b7-bd7c-51392b9d1e8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 21 · 2026-05-21T08:39:59.690Z_

<details><summary>↩ Tool result · `toolu_01JK9SNTTUbJgjyiDR6P2BGf`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca941af8-d57d-45b7-bd7c-51392b9d1e8d",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "5b19b15e-1712-4334-8557-9082caa1b670",
  "sourceToolAssistantUUID": "ca941af8-d57d-45b7-bd7c-51392b9d1e8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T08:40:00.096Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Mmunk34dV2Y9Trdd2hnZ5b`</summary>

```json
{
  "pattern": "DDR",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b19b15e-1712-4334-8557-9082caa1b670",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwxHYArqbg5ECsVat3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9be32c4c-e1d4-4df8-bab7-0582bfbf0f0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 23 · 2026-05-21T08:40:00.112Z_

<details><summary>↩ Tool result · `toolu_01Mmunk34dV2Y9Trdd2hnZ5b`</summary>

```text
&lt;persisted-output>
Output too large (40.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/f0729576-0a0b-4639-9730-0c3f60cce994/tool-results/toolu_01Mmunk34dV2Y9Trdd2hnZ5b.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-17-We study \emph{inference chains} where parameters are fixed and only the input distribution evolves.
docs/paper/related_work.tex-18-Two concurrent works are most directly relevant: \citet{broken_telephone} analyze paraphrasing and translation chains, documenting progressive information loss, while \citet{markovian_chains} demonstrate attractor dynamics that bound distinguishable depth to approximately three classes; \citet{attractor_cycles} provide complementary evidence that LLM outputs converge to cyclic attractor states under repeated generation.
docs/paper/related_work.tex:19:We study \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal, and offer a complementary decomposition: where these works characterize \emph{that} and \emph{why} convergence occurs, DDR isolates \emph{what} converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.
docs/paper/related_work.tex-20-The independent convergence of all three approaches on ${\sim}$3 distinguishable depth classes---via Markovian dynamics \cite{markovian_chains}, information-theoretic loss \cite{broken_telephone}, and distributional feature compression (this work)---points to a shared resolution ceiling in recursive text generation (Table~\ref{tab:iterative-comparison} in Appendix~\ref{app:iterative-comparison} provides a structured comparison).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-21-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-24-
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9be32c4c-e1d4-4df8-bab7-0582bfbf0f0d",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "861face8-084f-4d58-af55-81a427715c1a",
  "sourceToolAssistantUUID": "9be32c4c-e1d4-4df8-bab7-0582bfbf0f0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T08:40:00.721Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Bc1vMZTZ6qHDP9d82UtMw7`</summary>

```json
{
  "pattern": "6-gen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "861face8-084f-4d58-af55-81a427715c1a",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwxHYArqbg5ECsVat3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4e6d0f6b-ac04-4c90-978e-69d1f2fcb29b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 25 · 2026-05-21T08:40:00.736Z_

<details><summary>↩ Tool result · `toolu_01Bc1vMZTZ6qHDP9d82UtMw7`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-2-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-3-\paragraph{Setup.}
docs/paper/appendix_qlora.tex:4:We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).\footnote{Evaluated on the original 6-generator subset; XGBoost 3-class F1\,=\,0.789. We expect 8-generator training to further improve given additional diversity; the comparison direction is preserved.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-5-For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-6-All results use the same LOGO protocol as the main experiments.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-23-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-24-\paragraph{Results.}
docs/paper/appendix_qlora.tex:25:QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-26-On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
docs/paper/appendix_qlora.tex-27-The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
--
docs/paper/appendix_cross_temp.tex:1:Figure~\ref{fig:cross-temp} shows cross-temperature transfer results for the 6-generator LOGO pipeline.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_cross_temp.tex-2-We evaluate four train$\rightarrow$test temperature conditions using Qwen3-1.7B data regenerated at $t{=}1.0$ (remaining five generators retain $t{=}0.7$).\footnote{The $t{=}1.0$ data uses top-$p{=}0.95$ (vs.\ $p{=}0.9$ for other configurations); this difference may contribute to the observed degradation beyond the temperature effect alone.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_cross_temp.tex-3-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_cross_temp.tex-5-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_cross_temp.tex-6-\includegraphics[width=\columnwidth]{fig_appendix_cross_temp.pdf}
docs/paper/appendix_cross_temp.tex:7:[Omitted long matching line]
docs/paper/appendix_cross_temp.tex-8-\label{fig:cross-temp}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_cross_temp.tex-9-\end{figure}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-15-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-16-\end{tabular}}
docs/paper/appendix_confusion_matrix.tex:17:\caption{Aggregated 3-class confusion matrix from 6-generator LOGO evaluation ($N=27{,}529$). Each cell shows count and row-normalized percentage. Gen-0 is near-perfectly identified. Gen-1 errors are asymmetric: misclassification as gen-2+ (18.8\%) is 3$\times$ more frequent than as gen-0 (6.2\%). Gen-1 text already carries detectable recursive distortion.}
docs/paper/appendix_confusion_matrix.tex-18-\label{tab:confusion}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-19-\end{table}
--
docs/paper/appendix_lofo.tex:1:We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.789).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_lofo.tex-2-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_lofo.tex-3-\begin{table}[ht]
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_lofo.tex-19-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_lofo.tex-20-\end{tabular}
docs/paper/appendix_lofo.tex:21:\caption{Leave-one-feature-out ablation (6-gen LOGO). Each row drops one feature and re-evaluates with the LOGO protocol. Sorted by impact magnitude.}
docs/paper/appendix_lofo.tex-22-\label{tab:lofo}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_lofo.tex-23-\end{table}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex-4-[Omitted long context line]
docs/paper/abstract.tex-5-Where prior work on iterative generation documents \emph{what converges}, the novel observation here is \emph{what is preserved}: shape invariance under the same process that compresses location provides the stable reference needed for depth estimation without per-generator calibration.
docs/paper/abstract.tex:6:As a proof of concept, a lightweight 7-feature ensemble exploiting DDR achieves leak-free binary F1\,=\,0.694 (gen-1 vs.\ gen-2+, effective resolution: three depth classes) under leave-one-generator-out evaluation, surpassing individual baselines and matching multi-detector ensembles at $2.4\times$ lower cost; an end-to-end classifier recovers substantially more (F1\,=\,0.905, 6-gen LOGO), establishing the analytical framework---not the specific features---as the primary contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex-7-The signal attenuates under instruction tuning; current applicability is restricted to base models.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex-8-\end{abstract}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-1-To verify that the depth signal resides in the features rather than the classifier,
docs/paper/appendix_classifier.tex:2:we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest
docs/paper/appendix_classifier.tex-3-in place of XGBoost (Table~\ref{tab:alt-classifier}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-4-All other settings (the same 7 features, 3-class labels, and class-balanced downsampling) are
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-7-\begin{table}[ht]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-8-\centering
docs/paper/appendix_classifier.tex:9:\caption{LOGO macro-F1 across three classifiers. Each column shows the held-out generator F1. (6-generator LOGO; 3-class.)}
docs/paper/appendix_classifier.tex-10-\label{tab:alt-classifier}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-11-\small
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-67-\noindent\begin{minipage}{\columnwidth}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-68-\scriptsize $^{\ast}$OLMo temperature experiments use OLMo-2-0425-1B (April 2025 release); the original OLMo-2-1B-hf weights are no longer publicly available.\par\vspace{1pt}
docs/paper/appendix_classifier.tex:69:$^{\dagger}$Pythia-2.8B and Qwen3-1.7B use 6-generator LOGO (pre-expansion); OLMo-2-1B and Qwen3-0.6B use 8-generator LOGO. Within-model comparisons are unaffected.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-70-\end{minipage}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-71-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-85-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-86-\includegraphics[width=\columnwidth]{fig_appendix_per_gen.pdf}
docs/paper/appendix_classifier.tex:87:\caption{Per-generator LOGO performance. (a) 8-generator binary and 3-class F1, sorted by binary F1. Dashed lines: pool average. (b) 6-generator LOGO detail heatmap showing the performance spread across model families.}
docs/paper/appendix_classifier.tex-88-\label{fig:per-gen}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-89-\end{figure}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-12-Where concurrent work characterizes \emph{that} and \emph{why} convergence occurs \cite{broken_telephone,markovian_chains}, DDR isolates \emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-13-
docs/paper/introduction.tex:14:As a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at $2.4\times$ lower cost; an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-15-
docs/paper/introduction.tex-16-Our contributions:
--
docs/paper/results.tex-15-Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\,=\,0.810; LOFO yields 0.686.
docs/paper/results.tex-16-A scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}); cross-domain signal persists with variation (Appendix~\ref{app:domain}).
docs/paper/results.tex:17:An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 under 6-generator LOGO ($+$11.6\,pp vs.\ the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-18-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-19-\paragraph{Length confound control.}
--
docs/paper/method.tex-30-The seven features operationalize two complementary views of distributional drift: reference-model features capture how the token-level NLL distribution shifts relative to a fixed model (location and shape statistics), while surface features capture how lexical diversity contracts under recursive generation (type-token statistics).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-31-This dual-view design enables the location/shape decomposition that constitutes our primary finding.
docs/paper/method.tex:32:We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition.
docs/paper/method.tex-33-Cross-group ablation (\S\ref{sec:results-differential}) and leave-one-feature-out analysis (Appendix~\ref{app:lofo}) confirm that both feature groups contribute independently.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-34-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-16-Prior work documents \emph{what converges}---diversity loss \cite{curious_decline}, attractor dynamics \cite{markovian_chains}---but not what is \emph{preserved}; this complementary observation enables depth detection without per-generator calibration.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-17-The decomposition itself---identifying which distributional properties carry cross-generator depth signal---constitutes the analytical contribution, independent of whether shape stability originates from sampling truncation or deeper autoregressive properties.
docs/paper/discussion.tex:18:Three depth classes represent the practical resolution ceiling (5-class F1\,$\approx$\,0.50; Appendix~\ref{app:finer-depth}); QLoRA recovers more signal (F1\,=\,0.905, 6-gen LOGO; Appendix~\ref{app:qlora}), reflecting token-order patterns that aggregate statistics miss.
docs/paper/discussion.tex-19-Instruction-tuned models substantially compress DDR structure (silhouette 0.660$\to$0.372; entropy-mean $\rho$ reverses sign; 3-class F1 degrades 3.7--19.9\,pp), with model-dependent heterogeneity ruling out a uniform mechanism (Appendix~\ref{app:instruct}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-20-Yet QLoRA recovers to 0.89--0.91 on instruct data, confirming that depth signal persists at the token-sequence level beyond DDR's summary-statistic decomposition.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e6d0f6b-ac04-4c90-978e-69d1f2fcb29b",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "8bc0933f-43df-4672-8728-ba05a568334d",
  "sourceToolAssistantUUID": "4e6d0f6b-ac04-4c90-978e-69d1f2fcb29b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T08:40:01.152Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01ECmSCSogQipdREXvbnKjMy`</summary>

```json
{
  "pattern": "aaronson",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bc0933f-43df-4672-8728-ba05a568334d",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwxHYArqbg5ECsVat3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bac7bb08-6a93-4471-bf83-e023f6458778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 27 · 2026-05-21T08:40:01.168Z_

<details><summary>↩ Tool result · `toolu_01ECmSCSogQipdREXvbnKjMy`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-30-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-31-Scalable data curation relies on quality signals \cite{dsir,qurating,ccnet}; generation depth offers a complementary provenance axis.
docs/paper/related_work.tex:32:Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns but degrades across multi-step chains \cite{chainwash}, motivating passive approaches.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-33-Our NLL-based analysis connects to \citet{min_k_percent} (probability-tail membership inference) but extends from binary membership to full distributional decomposition for ordinal depth.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-34-\citet{koike_mia_detection} formalize this connection from the opposite direction, showing that detection scores implicitly perform membership inference, underscoring the shared statistical basis of detection and provenance.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-237-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-238-
docs/paper/references.bib:239:@misc{aaronson_watermark,
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-240-  title = {{Watermarking GPT Outputs}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-241-  author = {Aaronson, Scott and Kirchner, Jan Hendrik},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-242-  year = {2022},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-243-  note = {Blog post},
docs/paper/references.bib:244:  url = {https://scottaaronson.blog/?p=6823},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-245-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-246-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bac7bb08-6a93-4471-bf83-e023f6458778",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "e441a6e3-c482-4d95-a4ec-98659fd35eeb",
  "sourceToolAssistantUUID": "bac7bb08-6a93-4471-bf83-e023f6458778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T08:40:01.782Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015HzzAcW3WCRYcE1qCzwaaa`</summary>

```json
{
  "pattern": "ordinal",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e441a6e3-c482-4d95-a4ec-98659fd35eeb",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwxHYArqbg5ECsVat3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "57fd5280-277e-4ba8-92ab-b046b462fdd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 29 · 2026-05-21T08:40:01.795Z_

<details><summary>↩ Tool result · `toolu_015HzzAcW3WCRYcE1qCzwaaa`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-6-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-7-The detection literature spans statistical tests \cite{gltr,grover,release_strategies}, zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, surprisal diversity \cite{diveye}, geometric invariants \cite{intrinsic_dim_detection}, and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
docs/paper/related_work.tex:8:RAID \cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-9-[Omitted long context line]
docs/paper/related_work.tex:10:Our contribution is orthogonal: ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task, and the finding that combining drifting and stationary features yields consistent cross-generator performance where individual detection scores show high variance \cite{uchendu_attribution,munir_looking_glass}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-11-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-12-\subsection{Model Collapse and Iterative Generation}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-17-We study \emph{inference chains} where parameters are fixed and only the input distribution evolves.
docs/paper/related_work.tex-18-Two concurrent works are most directly relevant: \citet{broken_telephone} analyze paraphrasing and translation chains, documenting progressive information loss, while \citet{markovian_chains} demonstrate attractor dynamics that bound distinguishable depth to approximately three classes; \citet{attractor_cycles} provide complementary evidence that LLM outputs converge to cyclic attractor states under repeated generation.
docs/paper/related_work.tex:19:We study \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal, and offer a complementary decomposition: where these works characterize \emph{that} and \emph{why} convergence occurs, DDR isolates \emph{what} converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.
docs/paper/related_work.tex-20-The independent convergence of all three approaches on ${\sim}$3 distinguishable depth classes---via Markovian dynamics \cite{markovian_chains}, information-theoretic loss \cite{broken_telephone}, and distributional feature compression (this work)---points to a shared resolution ceiling in recursive text generation (Table~\ref{tab:iterative-comparison} in Appendix~\ref{app:iterative-comparison} provides a structured comparison).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-21-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-31-Scalable data curation relies on quality signals \cite{dsir,qurating,ccnet}; generation depth offers a complementary provenance axis.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-32-Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns but degrades across multi-step chains \cite{chainwash}, motivating passive approaches.
docs/paper/related_work.tex:33:Our NLL-based analysis connects to \citet{min_k_percent} (probability-tail membership inference) but extends from binary membership to full distributional decomposition for ordinal depth.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-34-\citet{koike_mia_detection} formalize this connection from the opposite direction, showing that detection scores implicitly perform membership inference, underscoring the shared statistical basis of detection and provenance.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-166-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-167-Levene tests reject equal variance between gen-1 and gen-2+ for drifting features ($p < 10^{-10}$; variance ratios 1.86--2.21).
docs/paper/appendix_ddr_validation.tex:168:To verify that the DDR partition is robust to this heteroscedasticity, we supplement pooled Cohen's $d$ with Glass's $\Delta$ (using the gen-1 standard deviation as denominator) and Cliff's $\delta$ (a non-parametric ordinal effect size; Table~\ref{tab:effect-sizes}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-169-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-170-\begin{table}[ht]
--
docs/paper/appendix_confusion_matrix.tex:1:Table~\ref{tab:confusion} reports the aggregated confusion matrix from the original six-generator subset (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B) under leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth $\geq$ 2).
docs/paper/appendix_confusion_matrix.tex-2-The later-added Llama-3.2-3B and Mistral-7B-v0.3 are evaluated in the full 8-generator LOGO results (Table~\ref{tab:logo-results}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-3-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_human_edit.tex-28-\paragraph{Feature subset degradation.}
docs/paper/appendix_human_edit.tex-29-Table~\ref{tab:feature-degrade} compares perturbation robustness of the full 7-feature ensemble against an entropy-only subset (5 reference-model features).
docs/paper/appendix_human_edit.tex:30:The higher unperturbed binary F1 of the entropy-only subset (0.833 vs.\ 0.695) reflects the strong discriminability of reference-model features for the coarse binary task (gen-1 vs.\ gen-2+); however, lexical features are essential for the finer-grained ordinal task (3-class F1: 0.737 vs.\ 0.688) and provide greater robustness under perturbation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_human_edit.tex-31-At 20\% replacement, the 7-feature ensemble surpasses entropy-only on binary F1 (0.591 vs.\ 0.569), despite starting from a lower baseline.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_human_edit.tex-32-Random word replacement drastically alters per-token context and makes entropy features (computed over the full token sequence) extremely sensitive to noise.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-80-\paragraph{Classifier.}
docs/paper/method.tex-81-We use XGBoost \cite{xgboost} throughout ($n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, learning rate $0.1$), with identical hyperparameters across all methods in Table~\ref{tab:baselines}.
docs/paper/method.tex:82:Alternative classifiers (CORAL \cite{coral_ordinal}, CORN \cite{corn_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance (Appendix~\ref{app:classifier}); discriminative power resides in the features, not the classifier.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-83-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-84-\paragraph{Metrics and statistical testing.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-29-confirming that discriminative power originates in the entropy and lexical features,
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-30-not in classifier capacity.
docs/paper/appendix_classifier.tex:31:Ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) achieve comparable F1 with overlapping CIs, which confirms that 3-class granularity provides insufficient resolution for ranking-aware losses to improve over standard multiclass classification.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-32-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-33-\subsection*{Sampling Sensitivity Analysis}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-8-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-9-Distributional compression under recursive generation is well-documented \cite{curious_decline,broken_telephone,markovian_chains}.
docs/paper/introduction.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-11-We term this location/shape asymmetry the \emph{differential depth response} (DDR)---a structural property of fixed-parameter autoregressive sampling that is mechanistically distinct from the tail-coverage erosion in model collapse \cite{curse_of_recursion} and analytically informative independent of both the specific mechanism and classification accuracy.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-12-Where concurrent work characterizes \emph{that} and \emph{why} convergence occurs \cite{broken_telephone,markovian_chains}, DDR isolates \emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-17-\begin{enumerate}[nosep,leftmargin=*]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-18-[Omitted long context line]
docs/paper/introduction.tex:19:    \item \textbf{Task formulation and evaluation suite.} We define generation depth classification as an ordinal prediction task and construct a controlled dataset of 37K texts from eight generators across five families (0.6B--8B), with leave-one-generator-out cross-validation as the primary evaluation protocol.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-20-\end{enumerate}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-21-A proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-422-% ===== Machine Learning =====
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-423-
docs/paper/references.bib:424:@article{gutierrez_ordinal_survey,
docs/paper/references.bib-425-  title = {{Ordinal Regression Methods: Survey and Experimental Study}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-426-  author = {Guti{\'e}rrez, Pedro Antonio and P{\'e}rez-Ortiz, Mar{\'i}a and S{\'a}nchez-Monedero, Javier and Fern{\'a}ndez-Navarro, Francisco and Herv{\'a}s-Mart{\'i}nez, C{\'e}sar},
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-432-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-433-
docs/paper/references.bib:434:@article{coral_ordinal,
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-435-  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-436-  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-441-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-442-
docs/paper/references.bib:443:@inproceedings{frank_hall_ordinal,
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-444-  title = {{A Simple Approach to Ordinal Classification}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-445-  author = {Frank, Eibe and Hall, Mark},
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-448-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-449-
docs/paper/references.bib:450:@article{corn_ordinal,
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-451-  title = {{Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-452-  author = {Shi, Xintong and Cao, Wenzhi and Raschka, Sebastian},
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-457-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-458-
docs/paper/references.bib:459:@inproceedings{kasa_ordinality_nlp,
docs/paper/references.bib-460-  title = {{Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-461-  author = {Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and Roychowdhury, Sumegh and Priyatam, Pattisapu and Bhanushali, Anish and Murthy, Prasanna Srinivasa},
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_finer_depth.tex-48-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_finer_depth.tex-49-\paragraph{Classifier comparison.}
docs/paper/appendix_finer_depth.tex:50:To verify that 5-class degradation reflects feature-level limitations rather than classifier choice, we evaluate four alternatives under the same protocol: HistGradientBoosting (macro F1\,=\,0.501, 95\% bootstrap CI [0.496, 0.506]), random forest (0.476), logistic regression (0.447), and Frank-Hall ordinal reduction (0.451).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_finer_depth.tex-51-All classifiers perform comparably to the default XGBoost ensemble (0.501), indicating that classifier capacity is not the bottleneck.
docs/paper/appendix_finer_depth.tex-52-The gen-2/gen-3 boundary is the primary failure mode across all methods: these two classes are effectively inseparable with the current feature set. This establishes 3-class granularity as the practical ceiling for surface and entropy features.
docs/paper/appendix_finer_depth.tex:53:At the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\S\ref{sec:results}), which confirms that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.
--
docs/paper/results.tex-106-\label{sec:results-baselines}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-107-
docs/paper/results.tex:108:Existing detection methods target binary real-vs-synthetic classification; we test whether their continuous scores incidentally encode recursive depth by repurposing four detection scores as ordinal depth predictors under identical XGBoost and LOGO conditions (Table~\ref{tab:baselines}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-109-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-110-\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57fd5280-277e-4ba8-92ab-b046b462fdd1",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "61451ae7-c3c9-470d-80ac-d4a39ccedc04",
  "sourceToolAssistantUUID": "57fd5280-277e-4ba8-92ab-b046b462fdd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T08:40:02.411Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011MR4BJaBFrCiAd3pDQJtYh`</summary>

```json
{
  "pattern": "\\$\\+\\$11\\.6|\\+11\\.6",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61451ae7-c3c9-470d-80ac-d4a39ccedc04",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwxHYArqbg5ECsVat3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "726467d1-fdf5-400e-aa60-22a9bca0a1c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 31 · 2026-05-21T08:40:02.424Z_

<details><summary>↩ Tool result · `toolu_011MR4BJaBFrCiAd3pDQJtYh`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-23-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-24-\paragraph{Results.}
docs/paper/appendix_qlora.tex:25:QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-26-On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
docs/paper/appendix_qlora.tex-27-The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
--
docs/paper/method.tex-30-The seven features operationalize two complementary views of distributional drift: reference-model features capture how the token-level NLL distribution shifts relative to a fixed model (location and shape statistics), while surface features capture how lexical diversity contracts under recursive generation (type-token statistics).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-31-This dual-view design enables the location/shape decomposition that constitutes our primary finding.
docs/paper/method.tex:32:We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition.
docs/paper/method.tex-33-Cross-group ablation (\S\ref{sec:results-differential}) and leave-one-feature-out analysis (Appendix~\ref{app:lofo}) confirm that both feature groups contribute independently.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-34-
--
docs/paper/results.tex-15-Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\,=\,0.810; LOFO yields 0.686.
docs/paper/results.tex-16-A scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}); cross-domain signal persists with variation (Appendix~\ref{app:domain}).
docs/paper/results.tex:17:An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 under 6-generator LOGO ($+$11.6\,pp vs.\ the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-18-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-19-\paragraph{Length confound control.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "726467d1-fdf5-400e-aa60-22a9bca0a1c7",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "67a94ecd-ee8b-4a5b-8522-87e1c469ca3a",
  "sourceToolAssistantUUID": "726467d1-fdf5-400e-aa60-22a9bca0a1c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T08:40:02.937Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01HyoVyRjLbTj3d4f4vFtTuw`</summary>

```json
{
  "pattern": "QLoRA|qlora",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67a94ecd-ee8b-4a5b-8522-87e1c469ca3a",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQwxHYArqbg5ECsVat3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "234ced8e-b7e2-4891-af19-00736dc8bed1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "output_tokens": 1017,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25128
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1017,
          "cache_read_input_tokens": 17198,
          "cache_creation_input_tokens": 25128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25128,
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

_source line 33 · 2026-05-21T08:40:02.957Z_

<details><summary>↩ Tool result · `toolu_01HyoVyRjLbTj3d4f4vFtTuw`</summary>

```text
docs/paper/appendix_qlora.tex:1:To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-2-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-3-\paragraph{Setup.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-9-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-10-\small
docs/paper/appendix_qlora.tex:11:\caption{QLoRA end-to-end depth classification vs.\ XGBoost on handcrafted features, under LOGO evaluation.}
docs/paper/appendix_qlora.tex:12:\label{tab:qlora}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-13-\resizebox{\linewidth}{!}{%
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-14-\begin{tabular}{lccc}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-17-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-18-XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
docs/paper/appendix_qlora.tex:19:QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-20-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-21-\end{tabular}}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-23-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-24-\paragraph{Results.}
docs/paper/appendix_qlora.tex:25:QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).
docs/paper/appendix_qlora.tex:26:On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
docs/paper/appendix_qlora.tex-27-The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-28-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-58-\input{appendix_finer_depth}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-59-
docs/paper/main.tex:60:\section{End-to-End Depth Classification (QLoRA)}
docs/paper/main.tex:61:\label{app:qlora}
docs/paper/main.tex:62:\input{appendix_qlora}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-63-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-64-\section{Leave-One-Feature-Out Analysis}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex-4-Recursive generation in base models imprints a systematic distributional signature---central-tendency features drift with depth while shape features remain stable---a dichotomy we term differential depth response (DDR), validated across eight generators from five families.
docs/paper/conclusion.tex-5-This enables cross-generator depth classification (leak-free binary F1\,=\,0.694; end-to-end: 0.905) and provides an analytical lens complementary to model collapse: inference-chain drift compresses location while preserving shape, whereas retraining erodes both.
docs/paper/conclusion.tex:6:Current boundaries are instruction tuning---where alignment compresses DDR structure while token-level signal persists (QLoRA 0.89--0.91)---and frontier scale, where preliminary evidence suggests attenuated but persistent effects.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-16-Prior work documents \emph{what converges}---diversity loss \cite{curious_decline}, attractor dynamics \cite{markovian_chains}---but not what is \emph{preserved}; this complementary observation enables depth detection without per-generator calibration.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-17-The decomposition itself---identifying which distributional properties carry cross-generator depth signal---constitutes the analytical contribution, independent of whether shape stability originates from sampling truncation or deeper autoregressive properties.
docs/paper/discussion.tex:18:Three depth classes represent the practical resolution ceiling (5-class F1\,$\approx$\,0.50; Appendix~\ref{app:finer-depth}); QLoRA recovers more signal (F1\,=\,0.905, 6-gen LOGO; Appendix~\ref{app:qlora}), reflecting token-order patterns that aggregate statistics miss.
docs/paper/discussion.tex-19-Instruction-tuned models substantially compress DDR structure (silhouette 0.660$\to$0.372; entropy-mean $\rho$ reverses sign; 3-class F1 degrades 3.7--19.9\,pp), with model-dependent heterogeneity ruling out a uniform mechanism (Appendix~\ref{app:instruct}).
docs/paper/discussion.tex:20:Yet QLoRA recovers to 0.89--0.91 on instruct data, confirming that depth signal persists at the token-sequence level beyond DDR's summary-statistic decomposition.
docs/paper/discussion.tex-21-Cross-domain evaluation (News, Academic, Code; $t{=}1.0$) yields binary F1\,=\,0.74--0.75 but degraded 3-class F1 (0.62--0.65; Appendix~\ref{app:domain}), with temperature and domain effects confounded.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-22-Our generation chains use open-ended continuation prompts; real-world recursive pipelines---instruction-following chains, multi-turn dialogues, mixed-model editing---may attenuate, restructure, or introduce confounds not present in controlled chains.
--
docs/paper/method.tex-30-The seven features operationalize two complementary views of distributional drift: reference-model features capture how the token-level NLL distribution shifts relative to a fixed model (location and shape statistics), while surface features capture how lexical diversity contracts under recursive generation (type-token statistics).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-31-This dual-view design enables the location/shape decomposition that constitutes our primary finding.
docs/paper/method.tex:32:We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition.
docs/paper/method.tex-33-Cross-group ablation (\S\ref{sec:results-differential}) and leave-one-feature-out analysis (Appendix~\ref{app:lofo}) confirm that both feature groups contribute independently.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-34-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-70-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-71-\paragraph{End-to-end instruct classification.}
docs/paper/appendix_instruct.tex:72:To test whether depth signal persists at the token level despite summary-statistic degradation, we apply the QLoRA end-to-end classifier (Appendix~\ref{app:qlora}) to instruction-tuned data using within-model 5-fold stratified CV (Table~\ref{tab:instruct-qlora}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-73-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-74-\begin{table}[ht]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-75-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-76-\small
docs/paper/appendix_instruct.tex:77:\caption{End-to-end QLoRA vs.\ XGBoost on instruction-tuned data (within-model 5-fold CV, Qwen3-0.6B backbone). Base QLoRA rows shown for reference only; instruct sets ($N{\approx}4.4$--$5.0$K) are approximately twice the base sets ($N{\approx}2.3$K), so cross-condition comparison is confounded by training set size.}
docs/paper/appendix_instruct.tex:78:\label{tab:instruct-qlora}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-79-\resizebox{\linewidth}{!}{%
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-80-\begin{tabular}{lccccc}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-82-& \multicolumn{2}{c}{\textbf{3-class F1}} & & \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-83-\cmidrule(lr){2-3}
docs/paper/appendix_instruct.tex:84:\textbf{Model} & XGB & QLoRA & $\boldsymbol{\Delta}$ & \textbf{$N$} \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-85-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-86-OLMo-2-1B-Inst   & 0.575 & 0.888\,$\pm$\,0.007 & $+$31.3\,pp & 4{,}429 \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-93-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-94-
docs/paper/appendix_instruct.tex:95:The XGBoost-to-QLoRA gap on the same instruct data is substantial ($+$17.5 to $+$31.3\,pp), indicating that depth signal persists at the token level under instruction tuning but is inaccessible to the seven summary statistics; the degradation reported in Table~\ref{tab:instruct} reflects a feature-level limitation rather than signal absence.
docs/paper/appendix_instruct.tex:96:Note that instruct samples are approximately twice the base count used here (Table~\ref{tab:instruct-qlora}), so the instruct-vs-base QLoRA comparison is confounded by training set size; the meaningful comparison is QLoRA-vs-XGBoost on the same instruct data.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-97-All results use within-model 5-fold CV, not cross-generator LOGO, limiting generalization claims.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-12-Where concurrent work characterizes \emph{that} and \emph{why} convergence occurs \cite{broken_telephone,markovian_chains}, DDR isolates \emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-13-
docs/paper/introduction.tex:14:As a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at $2.4\times$ lower cost; an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-15-
docs/paper/introduction.tex-16-Our contributions:
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-187-% ===== Fine-tuning =====
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-188-
docs/paper/references.bib:189:@inproceedings{qlora,
docs/paper/references.bib:190:  title = {{QLoRA: Efficient Finetuning of Quantized LLMs}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-191-  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-192-  booktitle = {Advances in Neural Information Processing Systems},
--
docs/paper/appendix_generator_subsets.tex-13-Main LOGO (Table~\ref{tab:logo-results}) & 8 & All: Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B, Llama, Mistral \\
docs/paper/appendix_generator_subsets.tex-14-Cross-model chains (Table~\ref{tab:cross-ref}) & 5 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B \\
docs/paper/appendix_generator_subsets.tex:15:QLoRA (Table~\ref{tab:qlora}) & 6 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B \\
docs/paper/appendix_generator_subsets.tex-16-Temperature ablation (Table~\ref{tab:sampling-ablation}) & 4 & Py-2.8B, OLMo, Qw-1.7B/0.6B \\
docs/paper/appendix_generator_subsets.tex-17-Prompt-type (Appendix~\ref{app:prompt-type}) & 1 & Py-2.8B only \\
--
docs/paper/results.tex-15-Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\,=\,0.810; LOFO yields 0.686.
docs/paper/results.tex-16-A scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}); cross-domain signal persists with variation (Appendix~\ref{app:domain}).
docs/paper/results.tex:17:An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 under 6-generator LOGO ($+$11.6\,pp vs.\ the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-18-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-19-\paragraph{Length confound control.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "234ced8e-b7e2-4891-af19-00736dc8bed1",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "49980e33-bed7-4899-967e-719c7775e408",
  "sourceToolAssistantUUID": "234ced8e-b7e2-4891-af19-00736dc8bed1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-21T08:40:05.187Z_

Perfect. Now let me read the full DDR grep output that was saved to a file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49980e33-bed7-4899-967e-719c7775e408",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQxTFa3m8BEBk5hQQk3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "241cdb16-c895-46ed-87c0-df131065fdec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014j1yHFq47yoGUwyAA91LQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 19324,
      "cache_read_input_tokens": 42326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19324,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 35 · 2026-05-21T08:40:06.758Z_

<details open><summary>🔧 Tool call — Read · `toolu_015LqTsV6fCZjqq8Nu1iNiLe`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/f0729576-0a0b-4639-9730-0c3f60cce994/tool-results/toolu_01Mmunk34dV2Y9Trdd2hnZ5b.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "241cdb16-c895-46ed-87c0-df131065fdec",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQxTFa3m8BEBk5hQQk3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bf96f909-2482-4f23-b623-cb1ac4b25302",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014j1yHFq47yoGUwyAA91LQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 19324,
      "cache_read_input_tokens": 42326,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19324
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 166,
          "cache_read_input_tokens": 42326,
          "cache_creation_input_tokens": 19324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19324,
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

_source line 36 · 2026-05-21T08:40:07.208Z_

<details><summary>↩ Tool result · `toolu_015LqTsV6fCZjqq8Nu1iNiLe`</summary>

```text
1	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-17-We study \emph{inference chains} where parameters are fixed and only the input distribution evolves.
2	docs/paper/related_work.tex-18-Two concurrent works are most directly relevant: \citet{broken_telephone} analyze paraphrasing and translation chains, documenting progressive information loss, while \citet{markovian_chains} demonstrate attractor dynamics that bound distinguishable depth to approximately three classes; \citet{attractor_cycles} provide complementary evidence that LLM outputs converge to cyclic attractor states under repeated generation.
3	docs/paper/related_work.tex:19:We study \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal, and offer a complementary decomposition: where these works characterize \emph{that} and \emph{why} convergence occurs, DDR isolates \emph{what} converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.
4	docs/paper/related_work.tex-20-The independent convergence of all three approaches on ${\sim}$3 distinguishable depth classes---via Markovian dynamics \cite{markovian_chains}, information-theoretic loss \cite{broken_telephone}, and distributional feature compression (this work)---points to a shared resolution ceiling in recursive text generation (Table~\ref{tab:iterative-comparison} in Appendix~\ref{app:iterative-comparison} provides a structured comparison).
5	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-21-
6	--
7	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-24-
8	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-25-Declining lexical diversity in LLM text is documented in both training \cite{curious_decline} and deployment settings \cite{writing_diversity}; MAUVE \cite{mauve} provides a divergence-based metric for quantifying this distributional gap.
9	docs/paper/related_work.tex:26:Our surface features (TTR, hapax ratio) are classical stylometric measures \cite{stamatatos_survey,koppel_authorship}; we repurpose them from generator identity \cite{uchendu_attribution} to the depth dimension, where their monotonic decline under top-$p$ sampling \cite{nucleus_sampling} constitutes a drifting component of DDR.
10	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-27-
11	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-28-\subsection{Data Quality and Provenance}
12	--
13	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_dataset_stats.tex-31-
14	docs/paper/appendix_dataset_stats.tex-32-Figure~\ref{fig:violin} shows the full distribution of each feature across five generation depths (0--4), pooled across all eight generators ($N$\,=\,37{,}058).
15	docs/paper/appendix_dataset_stats.tex:33:The violin plots confirm the DDR pattern: drifting features (entropy mean, TTR, hapax ratio) show progressive narrowing and location shift, while shape features (entropy max, tail decay) maintain approximately constant distributions across depths.
16	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_dataset_stats.tex-34-
17	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_dataset_stats.tex-35-\begin{figure*}[!htbp]
18	--
19	docs/paper/appendix_feature_distributions.tex:1:\subsection*{DDR Trend Lines}
20	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex-2-
21	docs/paper/appendix_feature_distributions.tex-3-Figure~\ref{fig:ddr-trends} shows the per-feature depth trend (mean across all samples at each depth) with individual generator traces overlaid.
22	docs/paper/appendix_feature_distributions.tex:4:The consistent downward trajectories for drifting features across all generators confirm that DDR is a universal property of recursive generation.
23	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex-5-Shape features exhibit flat trajectories regardless of generator, with near-zero $R^2$ for the linear fit.
24	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex-6-
25	--
26	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex-8-\centering
27	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex-9-\includegraphics[width=\textwidth]{fig_appendix_ddr_trends.pdf}
28	docs/paper/appendix_feature_distributions.tex:10:\caption{Per-feature depth trends. Bold line: pooled mean ($\pm$1.96\,SE shading) across all generators, colored by DDR zone (blue: drifting, wine: intermediate, amber: near-stationary). Thin traces: individual generators. Spearman $\rho$ and linear $R^2$ are annotated per panel.}
29	docs/paper/appendix_feature_distributions.tex-11-\label{fig:ddr-trends}
30	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex-12-\vspace{-0.5em}
31	--
32	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-1-\subsection*{Data-Driven Clustering}
33	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-2-
34	docs/paper/appendix_ddr_validation.tex:3:To assess the DDR partition structure and determine whether the drifting/non-drifting split is data-driven, we apply $k$-means clustering ($k \in \{2,3,4,5\}$) to the seven features in standardized $(|\rho|, d)$ space (Table~\ref{tab:clustering}).
35	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-4-
36	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-5-\begin{table}[ht]
37	--
38	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-22-The primary drifting/non-drifting split ($k{=}2$, silhouette\,=\,0.660) is the strongest cluster structure.
39	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-23-At $k{=}3$, entropy min forms its own cluster rather than joining the near-stationary group because its pooled $|\rho|{=}0.40$ (driven by the gen-0/gen-1 boundary) places it far from other near-stationary features in $\rho$ space.
40	docs/paper/appendix_ddr_validation.tex:24:The 3/1/3 DDR partition resolves this by using the gen-1 vs.\ gen-2+ Cohen's $d$ ($d{=}0.03$) to place entropy min in the near-stationary group, a domain-informed refinement that unsupervised clustering cannot recover from pooled statistics alone.
41	docs/paper/appendix_ddr_validation.tex:25:At $k{=}4$ (silhouette\,=\,0.571), entropy std separates from the near-stationary group, consistent with its intermediate DDR classification.
42	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-26-
43	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-27-\paragraph{Exhaustive partition enumeration.}
44	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-28-To confirm that the three-vs-four split is optimal rather than incidental, we enumerate all $\binom{7}{3}{=}35$ possible ways to assign three features to a ``drifting'' group and the remaining four to ``non-drifting,'' computing the silhouette score for each partition in standardized $(|\rho|, d)$ space.
45	docs/paper/appendix_ddr_validation.tex:29:The observed DDR partition (\{entropy mean, TTR, hapax ratio\}) achieves the highest silhouette (0.660), with a gap of 0.18 to the second-ranked split; 20 of 35 partitions produce negative silhouette scores.
46	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-30-
47	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-31-\paragraph{Per-generator replication.}
48	--
49	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-47-\begin{tabular}{llccc}
50	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-48-\toprule
51	docs/paper/appendix_ddr_validation.tex:49:\textbf{DDR Zone} & \textbf{Feature} & $\boldsymbol{\varepsilon{=}0.15}$ & $\boldsymbol{\varepsilon{=}0.20}$ & $\boldsymbol{\varepsilon{=}0.25}$ \\
52	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-50-\midrule
53	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-51-\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 0/8 & 0/8 & 0/8 \\
54	--
55	docs/paper/appendix_ddr_validation.tex-86-\label{app:epsilon-sweep}
56	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-87-
57	docs/paper/appendix_ddr_validation.tex:88:The DDR partition classifies features as non-stationary ($d \geq \varepsilon$) or stationary ($d < \varepsilon$) based on pooled Cohen's $d$ (\S\ref{sec:results-differential}).
58	docs/paper/appendix_ddr_validation.tex-89-Table~\ref{tab:epsilon-sweep} reports the critical $\varepsilon$ at which each feature's classification changes; the three drifting and three near-stationary features maintain their classification for all $\varepsilon \in [0.10, 0.75]$.
59	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-90-
60	--
61	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-97-\begin{tabular}{llcc}
62	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-98-\toprule
63	docs/paper/appendix_ddr_validation.tex:99:\textbf{DDR Zone} & \textbf{Feature} & \textbf{Pooled $d$} & \textbf{Stationary at $\varepsilon >$} \\
64	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-100-\midrule
65	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-101-\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 1.17 & 1.17 \\
66	--
67	docs/paper/appendix_ddr_validation.tex-118-\label{app:holdout-split}
68	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-119-
69	docs/paper/appendix_ddr_validation.tex:120:To confirm the DDR partition is not an artifact of the specific generator pool, we split the eight generators into disjoint selection (4) and validation (4) sets, compute per-subset pooled $(|\rho|, d)$, and check whether all seven features receive the same zone assignment in both subsets.
70	docs/paper/appendix_ddr_validation.tex-121-We evaluate two complementary splits to avoid dependence on a single partition:
71	docs/paper/appendix_ddr_validation.tex-122-Split~A selects \{Pythia-2.8B, Qwen3-1.7B, OLMo, Mistral\} (validation: Pythia-1B, Qwen3-0.6B, Qwen3-8B, Llama);
72	--
73	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-126-\centering
74	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-127-\small
75	docs/paper/appendix_ddr_validation.tex:128:\caption{Holdout split validation of the DDR partition. Selection (sel) and validation (val) $|\rho|$ and $d$ for two disjoint 4/4 generator splits. Zone assignment is identical across all four subsets for every feature.}
76	docs/paper/appendix_ddr_validation.tex-129-\label{tab:holdout-split}
77	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-130-\resizebox{\linewidth}{!}{%
78	--
79	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-166-
80	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-167-Levene tests reject equal variance between gen-1 and gen-2+ for drifting features ($p < 10^{-10}$; variance ratios 1.86--2.21).
81	docs/paper/appendix_ddr_validation.tex:168:To verify that the DDR partition is robust to this heteroscedasticity, we supplement pooled Cohen's $d$ with Glass's $\Delta$ (using the gen-1 standard deviation as denominator) and Cliff's $\delta$ (a non-parametric ordinal effect size; Table~\ref{tab:effect-sizes}).
82	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-169-
83	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-170-\begin{table}[ht]
84	--
85	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-129-\input{appendix_tost_bootstrap}
86	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-130-
87	docs/paper/main.tex:131:\section{DDR Partition Validation}
88	docs/paper/main.tex-132-\label{app:ddr-validation}
89	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-133-\input{appendix_ddr_validation}
90	--
91	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-145-\FloatBarrier
92	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-146-
93	docs/paper/main.tex:147:\section{Supplementary DDR Characterization}
94	docs/paper/main.tex-148-\label{app:ddr-supplement}
95	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-149-
96	--
97	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-157-\FloatBarrier
98	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-158-
99	docs/paper/main.tex:159:\subsection{DDR Causality Analysis}
100	docs/paper/main.tex-160-\label{app:ddr-causality}
101	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-161-\input{appendix_ddr_causality}
102	--
103	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-20-
104	docs/paper/appendix_confusion_matrix.tex-21-Figure~\ref{fig:confusion-heatmap} provides a heatmap visualization of the confusion matrix.
105	docs/paper/appendix_confusion_matrix.tex:22:The row-normalized view highlights near-perfect gen-0 classification (99.4\% recall), gen-1 confusion primarily with gen-2+ (18.8\%) rather than gen-0 (6.2\%), and gen-2+ misclassification predominantly into gen-1 (23.3\%), consistent with DDR predictions.
106	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-23-
107	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-24-\begin{figure}[H]
108	--
109	docs/paper/appendix_feature_candidates.tex-1-To verify that the seven retained features are not an arbitrary subset, we screened six additional NLL-distributional statistics as candidate features: median, 90th percentile (p90), interquartile range (IQR), coefficient of variation (CV), skewness, and kurtosis.
110	docs/paper/appendix_feature_candidates.tex:2:Table~\ref{tab:candidate-features} reports their DDR coordinates, classification impact, and correlation with retained features.
111	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-3-
112	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-4-\begin{table}[ht]
113	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-5-\centering
114	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-6-\small
115	docs/paper/appendix_feature_candidates.tex:7:\caption{Candidate feature screening. All six candidates fall in the drifting DDR zone and correlate strongly ($|r| > 0.65$) with existing features. Adding any combination to the baseline degrades or leaves unchanged LOGO 3-class F1; LOFO $\Delta > 0$ indicates that removing the candidate \emph{improves} classification.}
116	docs/paper/appendix_feature_candidates.tex-8-\label{tab:candidate-features}
117	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-9-\resizebox{\linewidth}{!}{%
118	--
119	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-26-Adding all six to the 6-feature baseline\footnote{Tail decay requires full-vocabulary logits unavailable in the token-NLL subset used for this analysis; we report 6-feature baselines for fair comparison.} reduces 3-class LOGO F1 from 0.733 to 0.722, consistent with overfitting from redundant inputs.
120	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-27-LOFO analysis on the extended 12-feature set confirms that removing skewness ($+$0.010), median ($+$0.008), or IQR ($+$0.007) \emph{improves} classification, indicating these features inject noise rather than signal.
121	docs/paper/appendix_feature_candidates.tex:28:The retained seven features span three complementary DDR zones (drifting, intermediate, near-stationary) and two modalities (reference-model NLL, surface lexical diversity); additional distributional statistics provide no incremental information.
122	--
123	docs/paper/conclusion.tex-2-\label{sec:conclusion}
124	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex-3-
125	docs/paper/conclusion.tex:4:Recursive generation in base models imprints a systematic distributional signature---central-tendency features drift with depth while shape features remain stable---a dichotomy we term differential depth response (DDR), validated across eight generators from five families.
126	docs/paper/conclusion.tex-5-This enables cross-generator depth classification (leak-free binary F1\,=\,0.694; end-to-end: 0.905) and provides an analytical lens complementary to model collapse: inference-chain drift compresses location while preserving shape, whereas retraining erodes both.
127	docs/paper/conclusion.tex:6:Current boundaries are instruction tuning---where alignment compresses DDR structure while token-level signal persists (QLoRA 0.89--0.91)---and frontier scale, where preliminary evidence suggests attenuated but persistent effects.
128	--
129	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-41-A plausible explanation is that Gemma-2's first-generation continuations occupy a region of feature space highly similar to human-written text (gen-0), causing systematic misclassification of gen-1 as gen-0 or gen-2+.
130	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-42-This constitutes an architecture-specific generalization limitation rather than a systemic failure of the depth fingerprinting approach.
131	docs/paper/appendix_9gen_scale.tex:43:Several architectural differences may explain this behavior: (a)~Gemma-2's distinct attention mechanism and SentencePiece tokenizer with a larger vocabulary may produce first-generation continuations whose feature-space signature closely resembles human text, causing systematic gen-0/gen-1 confusion; (b)~this anomaly does not affect DDR's validity for the remaining eight generators, where per-generator F1 shifts by at most 0.011 upon Gemma inclusion.
132	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-44-
133	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-45-\paragraph{Scale effect.}
134	--
135	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-48-
136	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-49-\paragraph{14B-parameter evidence.}
137	docs/paper/appendix_9gen_scale.tex:50:Preliminary evidence from a 14.7B generator (Qwen3-14B-Base) confirms that the DDR partition persists at larger scale: Cohen's $d$ for drifting features remains in the large-effect range ($d{=}0.78$--$1.12$), though Spearman $|\rho|$ attenuates by 21--35\%, with entropy mean falling just below the drifting threshold ($|\rho|{=}0.39 < 0.40$, $d{=}0.78$).
138	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-51-This scale-dependent signal compression is consistent with larger models producing more self-typical outputs that narrow inter-depth contrasts; the partition structure is preserved even as absolute effect sizes compress.
139	--
140	docs/paper/discussion.tex-13-Depth-aware filtering can serve as a prophylactic against model collapse \cite{drayson_detection_prevents_collapse}, though depth-stratified curation does not yet improve downstream training (TOST equivalence at $\varepsilon{=}{\pm}2\%$; Appendix~\ref{app:downstream}); the primary value lies in provenance, not training improvement.
141	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-14-
142	docs/paper/discussion.tex:15:DDR is mechanistically distinct from model collapse \cite{curse_of_recursion,strong_model_collapse}: retraining erodes tail coverage by updating weights, whereas inference-chain drift at fixed parameters shifts only location, leaving shape stable.
143	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-16-Prior work documents \emph{what converges}---diversity loss \cite{curious_decline}, attractor dynamics \cite{markovian_chains}---but not what is \emph{preserved}; this complementary observation enables depth detection without per-generator calibration.
144	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-17-The decomposition itself---identifying which distributional properties carry cross-generator depth signal---constitutes the analytical contribution, independent of whether shape stability originates from sampling truncation or deeper autoregressive properties.
145	docs/paper/discussion.tex-18-Three depth classes represent the practical resolution ceiling (5-class F1\,$\approx$\,0.50; Appendix~\ref{app:finer-depth}); QLoRA recovers more signal (F1\,=\,0.905, 6-gen LOGO; Appendix~\ref{app:qlora}), reflecting token-order patterns that aggregate statistics miss.
146	docs/paper/discussion.tex:19:Instruction-tuned models substantially compress DDR structure (silhouette 0.660$\to$0.372; entropy-mean $\rho$ reverses sign; 3-class F1 degrades 3.7--19.9\,pp), with model-dependent heterogeneity ruling out a uniform mechanism (Appendix~\ref{app:instruct}).
147	docs/paper/discussion.tex:20:Yet QLoRA recovers to 0.89--0.91 on instruct data, confirming that depth signal persists at the token-sequence level beyond DDR's summary-statistic decomposition.
148	docs/paper/discussion.tex-21-Cross-domain evaluation (News, Academic, Code; $t{=}1.0$) yields binary F1\,=\,0.74--0.75 but degraded 3-class F1 (0.62--0.65; Appendix~\ref{app:domain}), with temperature and domain effects confounded.
149	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-22-Our generation chains use open-ended continuation prompts; real-world recursive pipelines---instruction-following chains, multi-turn dialogues, mixed-model editing---may attenuate, restructure, or introduce confounds not present in controlled chains.
150	--
151	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_iterative_comparison.tex-28-  & Open-ended continuation (no meaning-preserving constraint)
152	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_iterative_comparison.tex-29-  & Token-level NLL statistics (location, scale, shape) + lexical diversity
153	docs/paper/appendix_iterative_comparison.tex:30:  & Depth classification + DDR decomposition into generator \& depth effects
154	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_iterative_comparison.tex-31-  & 0.6--8B (8 models)
155	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_iterative_comparison.tex-32-  & 5
156	--
157	docs/paper/appendix_iterative_comparison.tex-38-Table~\ref{tab:iterative-comparison} compares this work with two concurrent studies on iterative LLM generation.
158	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_iterative_comparison.tex-39-All three examine how repeated inference transforms text, but differ in the chain operator (meaning-preserving vs.\ open-ended), the analytic lens (factuality decay, convergence dynamics, vs.\ distributional decomposition), and the downstream goal.
159	docs/paper/appendix_iterative_comparison.tex:40:Our continuation-chain setting, which imposes no semantic-preservation constraint, permits richer depth signal and enables the location/shape decomposition that defines DDR.
160	--
161	docs/paper/appendix_ddr_causality.tex:1:This appendix validates the causal predictive power of DDR features through three complementary analyses: permutation importance, Granger causality, and feature intervention.
162	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-2-
163	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-3-\paragraph{Permutation Importance.}
164	--
165	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-54-\paragraph{Key Findings.}
166	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-55-\begin{enumerate}[nosep,leftmargin=*]
167	docs/paper/appendix_ddr_causality.tex:56:\item \textbf{Drifting dominance.} The $5.5\times$ permutation-importance gap confirms that drifting features (entropy\_mean, ttr, hapax\_ratio) are the primary depth signal carriers, consistent with the DDR partition derived from convergence analysis (\S\ref{sec:results-differential}).
168	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-57-
169	docs/paper/appendix_ddr_causality.tex-58-\item \textbf{Entropy\_min lacks causal direction.} Beyond its small effect size (F1 drop\,=\,0.019), entropy\_min is the only feature without significant Granger causality ($p$\,=\,0.375). This strengthens the near-stationary classification: the feature is neither marginally important nor temporally predictive.
170	--
171	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-60-\item \textbf{Entropy\_max asymmetry.} Entropy\_max ranks fourth in permutation importance (F1 drop\,=\,0.070) but produces the largest degradation in the counterfactual intervention ($-$2.0\,pp), indicating that it provides unique signal not redundant with other features; its causal contribution exceeds its marginal importance.
172	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-61-
173	docs/paper/appendix_ddr_causality.tex:62:\item \textbf{Mistral heterogeneity.} In per-generator Granger tests, Mistral-7B shows non-significant hapax\_ratio and ttr ($p > 0.4$), though Fisher combination across generators remains significant. This generator-specific attenuation partly explains Mistral's lowest LOGO F1 (0.605) and suggests that DDR fingerprints are weaker in models with heavier repetition penalties.
174	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-63-\end{enumerate}
175	--
176	docs/paper/method.tex-30-The seven features operationalize two complementary views of distributional drift: reference-model features capture how the token-level NLL distribution shifts relative to a fixed model (location and shape statistics), while surface features capture how lexical diversity contracts under recursive generation (type-token statistics).
177	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-31-This dual-view design enables the location/shape decomposition that constitutes our primary finding.
178	docs/paper/method.tex:32:We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition.
179	docs/paper/method.tex-33-Cross-group ablation (\S\ref{sec:results-differential}) and leave-one-feature-out analysis (Appendix~\ref{app:lofo}) confirm that both feature groups contribute independently.
180	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-34-
181	--
182	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-53-\bottomrule
183	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-54-\end{tabular}
184	docs/paper/method.tex:55:\caption{Seven distributional features. Reference features use Pythia-410M per-token NLL; surface features require no reference model. DDR analysis (\S\ref{sec:results-differential}) reveals that the first three drift with depth while the last four remain stable.}
185	docs/paper/method.tex-56-\label{tab:features}
186	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-57-\end{table}
187	--
188	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-67-
189	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-68-\paragraph{Feature complementarity.}
190	docs/paper/method.tex:69:These features exhibit a \emph{differential depth response} (DDR), separating into drifting and non-drifting groups (\S\ref{sec:results-differential}; pairwise correlations in Appendix~\ref{sec:appendix-feature-correlation}).
191	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-70-TTR and hapax ratio are strongly correlated ($r = 0.97$); both are retained for marginal LOFO gains.
192	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-71-
193	--
194	docs/paper/appendix_convergence.tex:1:This appendix visualizes per-feature convergence trajectories across generation depth, complementing the DDR analysis in \S\ref{sec:results-differential}.
195	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_convergence.tex-2-
196	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_convergence.tex-3-\begin{figure}[H]
197	--
198	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-50-Three-generator instruct LOGO yields binary F1\,=\,0.487, indicating weak cross-generator transfer under instruction tuning.
199	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-51-
200	docs/paper/appendix_instruct.tex:52:\paragraph{DDR structure under instruction tuning.}
201	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-53-$k{=}2$ clustering in $(|\rho|, d)$ space on pooled instruct features yields silhouette\,=\,0.372 (vs.\ 0.660 for base models), indicating that the clean drifting/non-drifting partition is substantially compressed.
202	docs/paper/appendix_instruct.tex-54-The compression is model-dependent: OLMo-Instruct shows near-zero $|\rho|$ for TTR and hapax (0.006, 0.025), while Qwen instruct models retain moderate correlations ($|\rho|{=}0.48$--$0.53$).
203	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-55-Cross-condition transfer is near chance in both directions (base$\rightarrow$instruct binary F1\,=\,0.490; instruct$\rightarrow$base F1\,=\,0.454), with the asymmetry ($-$0.036) suggesting that instruct-trained features generalize even less to base distributions than the reverse.
204	docs/paper/appendix_instruct.tex:56:These results indicate that instruction tuning compresses the feature-space structure underlying DDR rather than simply reversing feature directions (Figure~\ref{fig:instruct-ddr}).
205	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-57-
206	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-58-\begin{figure}[ht]
207	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-59-\centering
208	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-60-\includegraphics[width=\linewidth]{fig_appendix_instruct_ddr.pdf}
209	docs/paper/appendix_instruct.tex:61:\caption{DDR partition under base (left) vs.\ instruction-tuned (right) models. Bars show pooled $|d|$; markers show individual generators. Base models exhibit a clean drifting/non-drifting separation (silhouette\,=\,0.660); instruction tuning compresses all features toward zero, collapsing the partition (silhouette\,=\,0.372). Entropy max shifts from near-stationary to intermediate under instruct, while formerly drifting features (hapax, TTR) lose most of their effect size.}
210	docs/paper/appendix_instruct.tex-62-\label{fig:instruct-ddr}
211	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-63-\end{figure}
212	--
213	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-67-To test this, we replace the reference with Qwen3-0.6B-Instruct and recompute all features on the two instruct generators.
214	docs/paper/appendix_instruct.tex-68-The hypothesis is partially rejected: Qwen3-1.7B-Instruct shows mixed changes (entropy max $d$: $0.51 \to 0.08$, becoming near-stationary; entropy std $d$: $1.07 \to 1.51$, increasing), while OLMo-Instruct loses nearly all depth signal (entropy mean $d$: $1.33 \to 0.02$; tail decay $d$: $0.60 \to 0.06$).
215	docs/paper/appendix_instruct.tex:69:The model-dependent heterogeneity rules out reference mismatch as a universal explanation for instruct DDR degradation, supporting the interpretation that alignment fundamentally reshapes the generation dynamics rather than introducing a correctable measurement artifact.
216	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-70-
217	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-71-\paragraph{End-to-end instruct classification.}
218	--
219	docs/paper/appendix_temperature_stability.tex:1:To assess whether the DDR three-way partition generalizes beyond the default temperature ($\tau{=}0.7$), we computed per-feature Cohen's $d$ (generation~1 vs.\ generation~2+) at $\tau \in \{0.5, 0.7, 0.9\}$ for all four generators in the temperature ablation (12 conditions total; Table~\ref{tab:ddr-temp-stability}).
220	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_temperature_stability.tex-2-
221	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_temperature_stability.tex-3-\begin{table}[ht]
222	--
223	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_error_analysis.tex-3-\paragraph{Error asymmetry.}
224	docs/paper/appendix_error_analysis.tex-4-Errors are heavily asymmetric: 86.2\% are false negatives (gen-2+ predicted as gen-1) and only 13.8\% are false positives (gen-1 predicted as gen-2+).
225	docs/paper/appendix_error_analysis.tex:5:The classifier systematically under-predicts depth, consistent with the DDR pattern: shallow gen-2+ samples that have not yet accumulated sufficient distributional drift are indistinguishable from gen-1.
226	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_error_analysis.tex-6-
227	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_error_analysis.tex-7-\paragraph{Per-depth error rates.}
228	--
229	docs/paper/appendix_error_analysis.tex-39-In contrast, shape features show no discriminating power: entropy\_max ($p = 0.584$) and tail\_decay ($p = 0.653$).
230	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_error_analysis.tex-40-Misclassified gen-2+ samples have systematically higher TTR (0.464 vs.\ 0.302 for correct) and entropy\_mean (2.26 vs.\ 1.57); these samples retain gen-1-like lexical diversity and have not undergone the distributional convergence characteristic of deeper generations.
231	docs/paper/appendix_error_analysis.tex:41:This is consistent with the DDR pattern (\S\ref{sec:results-differential}): errors concentrate where depth-accumulated drift is insufficient, and shape features (which are near-stationary by design) provide no additional discriminative signal for error correction.
232	--
233	docs/paper/appendix_tost.tex-5-We adopt Cohen's conventional small effect size ($d{=}0.20$) \cite{cohen1988statistical} as the smallest effect of practical significance (SESOI): effects below this threshold are unlikely to be practically meaningful for depth discrimination.
234	docs/paper/appendix_tost.tex-6-LOFO analysis independently supports this choice: removing any near-stationary feature changes classification F1 by $\leq$1.5\,pp (Appendix~\ref{app:lofo}), linking the statistical threshold to classification irrelevance.
235	docs/paper/appendix_tost.tex:7:Sensitivity analysis at $\varepsilon \in \{0.15, 0.20, 0.25\}$ confirms the partition is robust to the bound choice (see DDR Validation appendix).
236	docs/paper/appendix_tost.tex-8-Table~\ref{tab:tost-per-gen} reports observed $|d|$; \checkmark{} marks features for which the TOST null hypothesis (non-equivalence) is rejected at $\alpha = 0.05$.
237	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-9-
238	--
239	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-11-All drifting and intermediate features fail equivalence uniformly, with $|d|$ ranging from 0.23 (entropy std, Mistral) to 1.40 (entropy mean, Pythia-1B).
240	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-12-The partition is robust at the individual-generator level, with entropy min as the most consistently stationary feature.
241	docs/paper/appendix_tost.tex:13:Figure~\ref{fig:ddr-scatter} visualizes the DDR partition in ($|\rho|$, $d$) space, showing a clear gap between the three groups.
242	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-14-
243	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-15-\begin{table}[ht]
244	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-16-\centering
245	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-17-\footnotesize
246	docs/paper/appendix_tost.tex:18:\caption{Per-generator TOST equivalence ($\varepsilon{=}|d|{<}0.20$, gen-1 vs.\ gen-2+). Observed $|d|$; \checkmark{} = equivalent ($p_{\mathrm{TOST}} < 0.05$). Features grouped by DDR partition.}
247	docs/paper/appendix_tost.tex-19-\label{tab:tost-per-gen}
248	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-20-\resizebox{\columnwidth}{!}{%
249	--
250	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-42-\centering
251	
252	[Showing results with pagination = limit: 250]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf96f909-2482-4f23-b623-cb1ac4b25302",
  "isSidechain": true,
  "promptId": "8f4fd886-c938-4a2d-a294-164c965c4cd1",
  "agentId": "ad94135ba66be0aed",
  "type": "user",
  "uuid": "e46947a8-3755-4227-a777-913083ea422a",
  "sourceToolAssistantUUID": "bf96f909-2482-4f23-b623-cb1ac4b25302",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-21T08:40:32.544Z_

Perfect! Now I have all the information. Let me compile the comprehensive findings report.

## COMPREHENSIVE FINDINGS REPORT

### FILES READ (Full Content)

I have successfully read all 7 requested files in full:

1. **results.tex** - 141 lines: Contains results section with depth classification performance metrics, differential depth response analysis, and baseline comparisons
2. **method.tex** - 94 lines: Documents task formulation, generation chain construction, feature extraction methodology, and evaluation protocol
3. **appendix_qlora.tex** - 36 lines: Details QLoRA end-to-end depth classification experiments with setup, results, and hyperparameter robustness analysis
4. **related_work.tex** - 35 lines: Covers related work in AI-generated text detection, model collapse, vocabulary diversity, stylometry, and data provenance
5. **references.bib** - 563 lines: Complete bibliography with 80+ citations covering detection methods, model collapse, fine-tuning, watermarking, and model papers
6. **introduction.tex** - 22 lines: Introduces depth fingerprinting concept, DDR principle, and key contributions
7. **main.tex** - 178 lines: Master document with structure, document class configuration, and appendix organization

### FIG1-RELATED PYTHON FILES FOUND

Located in `artifacts/_project/chart/`:
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_ddr_v2.py`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_combined_v1.py`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_ddr_v3.py`

### GREP SEARCH FINDINGS

#### 1. "recursive generation depth" - **NO MATCHES FOUND**

#### 2. "DDR" - **Extensive Matches (40+ occurrences)**

Key findings across the paper:

- **Results.tex Line 17**: "An end-to-end QLoRA classifier achieves 3-class F1=0.905 under 6-generator LOGO (+11.6pp vs. the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution."

- **Method.tex Line 32**: "We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification (+11.6pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition."

- **Introduction.tex Line 10**: Document defines DDR as "location/shape asymmetry" that is "a structural property of fixed-parameter autoregressive sampling"

- **Related Work.tex Line 19**: "DDR isolates what converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration."

- **Discussion.tex Line 15-20**: Multiple references to DDR's mechanistic distinctness from model collapse and its structure under instruction tuning (silhouette compression 0.660→0.372)

- **Appendix references**: DDR Partition Validation (app:ddr-validation), DDR Causality Analysis (app:ddr-causality), Supplementary DDR Characterization (app:ddr-supplement), DDR Trends in feature distributions, Temperature stability of DDR partition

#### 3. "6-gen" - **Multiple Matches**

- **Appendix_qlora.tex Line 4**: "Evaluated on the original 6-generator subset; XGBoost 3-class F1=0.789"
- **Appendix_qlora.tex Line 25**: "QLoRA achieves 3-class LOGO F1=0.905 (±0.003) under 6-generator LOGO"
- **Appendix_cross_temp.tex Line 1**: "Figure~\ref{fig:cross-temp} shows cross-temperature transfer results for the 6-generator LOGO pipeline"
- **Appendix_lofo.tex Line 1**: "Leave-one-feature-out ablation (6-gen LOGO)"
- **Appendix_confusion_matrix.tex Line 17**: "Aggregated 3-class confusion matrix from 6-generator LOGO evaluation (N=27,529)"
- **Appendix_classifier.tex Line 2**: "we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest"

#### 4. "aaronson" - **2 Matches**

- **Related_work.tex Line 32**: "Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns but degrades across multi-step chains \cite{chainwash}, motivating passive approaches."

- **References.bib Line 239-244**: 
```bibtex
@misc{aaronson_watermark,
  title = {{Watermarking GPT Outputs}},
  author = {Aaronson, Scott and Kirchner, Jan Hendrik},
  year = {2022},
  note = {Blog post},
  url = {https://scottaaronson.blog/?p=6823},
}
```

#### 5. "ordinal" - **8 Matches**

- **Related_work.tex Line 8**: "RAID \cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation."

- **Related_work.tex Line 10**: "Our contribution is orthogonal: ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task"

- **Related_work.tex Line 19**: "DDR isolates what converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration."

- **Related_work.tex Line 33**: "Our NLL-based analysis connects to \citet{min_k_percent} (probability-tail membership inference) but extends from binary membership to full distributional decomposition for ordinal depth."

- **Method.tex Line 82**: "Alternative classifiers (CORAL \cite{coral_ordinal}, CORN \cite{corn_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance"

- **Introduction.tex Line 19**: "We define generation depth classification as an ordinal prediction task"

- **References.bib**: Multiple ordinal-related entries (gutierrez_ordinal_survey, coral_ordinal, frank_hall_ordinal, corn_ordinal, kasa_ordinality_nlp)

#### 6. "$+$11.6" or "+11.6" - **3 Matches**

- **Results.tex Line 17**: "An end-to-end QLoRA classifier achieves 3-class F1=0.905 under 6-generator LOGO ($+$11.6\,pp vs. the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora})"

- **Method.tex Line 32**: "end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora})"

- **Appendix_qlora.tex Line 25**: "QLoRA achieves 3-class LOGO F1=0.905 (±0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789)."

#### 7. "QLoRA" or "qlora" - **23 Matches**

Primary occurrences:
- **Appendix_qlora.tex**: Entire section dedicated to QLoRA experiments (36 lines)
- **Results.tex Line 17**: Main results mention of QLoRA performance
- **Method.tex Line 32**: Reference to QLoRA improving classification by +11.6pp
- **Introduction.tex Line 14**: "an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\ref{app:qlora})"
- **Discussion.tex Line 18**: "QLoRA recovers more signal (F1=0.905, 6-gen LOGO; Appendix~\ref{app:qlora})"
- **Discussion.tex Line 20**: "Yet QLoRA recovers to 0.89--0.91 on instruct data"
- **Conclusion.tex Line 6**: "Current boundaries are instruction tuning---where alignment compresses DDR structure while token-level signal persists (QLoRA 0.89--0.91)"
- **References.bib Line 189-193**: QLoRA citation (Dettmers et al., NeurIPS 2023)
- **Appendix_instruct.tex**: Multiple references to QLoRA performance on instruction-tuned models

### SUMMARY STATISTICS

- **Total files read**: 7 papers/documents (418 total lines)
- **Total grep patterns searched**: 7 queries
- **Patterns with matches**: 6/7 (all except "recursive generation depth")
- **Total DDR mentions**: 40+ occurrences across multiple files
- **QLoRA mentions**: 23 occurrences
- **6-gen references**: 12+ mentions
- **Ordinal classification references**: 8 matches
- **"Aaronson watermark" references**: 2 matches (cited work)
- **+11.6pp improvement references**: 3 critical mentions

The paper extensively documents differential depth response (DDR) as the core contribution, with QLoRA as an important validation experiment showing that end-to-end neural classifiers can recover deeper signal (0.905 F1) beyond the handcrafted features (0.789-0.694 F1 range).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e46947a8-3755-4227-a777-913083ea422a",
  "isSidechain": true,
  "agentId": "ad94135ba66be0aed",
  "requestId": "req_011CbFQxmqX1vTPy3VdJKVcE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "27092b31-fae2-4aa7-be81-d7c5235af4f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MfrK7P9pJu8Hwb8JZ1BKx3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 13946,
      "cache_read_input_tokens": 61650,
      "output_tokens": 2498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13946
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2498,
          "cache_read_input_tokens": 61650,
          "cache_creation_input_tokens": 13946,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13946,
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
