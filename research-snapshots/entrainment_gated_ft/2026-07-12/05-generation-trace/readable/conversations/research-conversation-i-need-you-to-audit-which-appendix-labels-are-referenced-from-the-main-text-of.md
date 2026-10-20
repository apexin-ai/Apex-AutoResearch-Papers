# Research conversation: I need you to audit which appendix labels are referenced from the main text of a LaTeX paper. The appendix file is at: `

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a7ca798f294f742d3.jsonl`
- **Structured JSON:** [`516e4b2f81ff30d90b90.json`](../../sessions/51/516e4b2f81ff30d90b90.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-25T09:10:00.531Z_

I need you to audit which appendix labels are referenced from the main text of a LaTeX paper. 

The appendix file is at: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex`

The main text files (NON-appendix) are:
- `introduction.tex`
- `related_work.tex`  
- `method.tex`
- `experiments.tex`
- `conclusion.tex`
All in the same `sections/` directory. Also check `main.tex` at `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex`.

Here are ALL the appendix section labels I need you to check (grep for each in the non-appendix files):

1. `app:benchmark_details` — Confirmatory and Exploratory Analyses
2. `app:convergence_detail` — Convergence Detail
3. `app:scale_convergence` — Scale-Dependent Convergence
4. `app:sensitivity` — Sensitivity Analyses (Bootstrap CI + GDN Exclusion)
5. `app:gdn_confound` — GDN Attention Head Confound
6. `app:attention_patterns` — Attention Weight Analysis (cosine sim, entropy, last-5)
7. `app:cross_scale` — Cross-Scale Per-Example Comparisons
8. `app:per_example_counts` — Per-Example Effect Counts (Table with helped/hurt/net)
9. `app:normalized_es` — Normalized Jaccard Effect Size
10. `app:arceasy` — ARC-Easy Per-Example Analysis
11. `app:jaccard_permutation` — Jaccard Permutation Test
12. `app:transformer_entrainment` — Transformer Entrainment Comparison
13. `app:within_arch_stability` — Within-Architecture Per-Example Stability
14. `app:cross_bench_jaccard` — Cross-Benchmark Jaccard Trajectories
15. `app:continuous_jaccard` — Continuous-Threshold Jaccard Analysis
16. `app:confidence_margin` — Target-Token Confidence Margin (C1/C2 tables)
17. `app:cm_cross` — Cross-Benchmark Extension (confidence margin)
18. `app:prediction_framework` — Prediction Framework (AUC, thresholds)
19. `app:calibration` — Calibration Analysis
20. `app:boolq` — BoolQ Supplementary Analysis
21. `app:winogrande` — WinoGrande Supplementary Analysis
22. `app:scale_per_example` — 340M Per-Example Analysis
23. `app:subsample_sensitivity` — Subsample Sensitivity of α
24. `app:complementarity` — Complementarity Decomposition
25. `app:seed_calibration` — Seed-Variation Calibration
26. `app:extended_arch` — Extended Architecture Validation (Five Architectures)
27. `app:code_data` — Code and Data Availability
28. `app:ai-assistants` — Use of AI Assistants

For each label, search in the NON-appendix .tex files (introduction, related_work, method, experiments, conclusion, main.tex). Report:
- FOUND: which file(s) and line(s) reference it
- NOT FOUND: label has zero references from main text (orphan)

Be thorough. Report a simple table format:
```
Label | Status | Referenced from (file:line or "ORPHAN")
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c7608d82-8599-4782-b1a2-f177b4bb14cc",
  "agentId": "a7ca798f294f742d3",
  "type": "user",
  "uuid": "10c5f3d0-14cc-4481-b595-412ad3ed5454",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T09:10:02.464Z_

I'll audit the appendix labels by searching for references to each one in the main text files. Let me start by reading the appendix file to understand its structure, then search for each label in the non-appendix files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10c5f3d0-14cc-4481-b595-412ad3ed5454",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2UdCnskBqSvfyiEm6S",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9d01b06e-d3e8-4496-a079-22f9ae3c84ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015pm251NPWpMYsCKaigFK3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 40411,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 40411,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-25T09:10:02.685Z_

<details open><summary>🔧 Tool call — Read · `toolu_015QPE6gs5zGwHB58LUp33XM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d01b06e-d3e8-4496-a079-22f9ae3c84ed",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2UdCnskBqSvfyiEm6S",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4bd286a3-723a-45f5-a0ab-37f23981a8c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015pm251NPWpMYsCKaigFK3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 40411,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 40411,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 4 · 2026-05-25T09:10:02.946Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HgEJvEjAwnPdM1NbceDona`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bd286a3-723a-45f5-a0ab-37f23981a8c7",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2UdCnskBqSvfyiEm6S",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "add8c9fd-8b6b-451f-81fc-a3cbd3b7b8ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015pm251NPWpMYsCKaigFK3K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 40411,
      "cache_read_input_tokens": 0,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 40411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 40411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 40411,
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

_source line 5 · 2026-05-25T09:10:02.961Z_

<details><summary>↩ Tool result · `toolu_015QPE6gs5zGwHB58LUp33XM`</summary>

```text
1	% Appendix sections for the paper.
2	
3	\section{Confirmatory and Exploratory Analyses}\label{app:benchmark_details}
4	
5	The task taxonomy used in \S\ref{ssec:task_taxonomy} was defined prior to running any convergence analyses. Each benchmark was assigned to exactly one of four categories based on the primary cognitive demand of the task:
6	
7	\begin{itemize}
8	    \item \textbf{Retrieval}: tasks requiring prediction from long-range context without multi-step reasoning (LAMBADA).
9	    \item \textbf{Comprehension}: reading comprehension with explicit passage support (BoolQ).
10	    \item \textbf{Reasoning}: tasks requiring commonsense inference or multi-step reasoning (HellaSwag, ARC-Challenge, WinoGrande, PIQA).
11	    \item \textbf{Mixed}: tasks combining retrieval, comprehension, and reasoning demands (ARC-Easy, MMLU, SciQ, XStoryCloze).
12	\end{itemize}
13	
14	\paragraph{Confirmatory benchmark set.} Six benchmarks were designated as confirmatory for Bonferroni correction: LAMBADA, HellaSwag, ARC-Challenge, WinoGrande, ARC-Easy, and MMLU. These were selected as representative of retrieval, reasoning, and mixed categories before any convergence analysis was performed. The taxonomy and benchmark selection were fixed before analysis as an informal pre-analysis plan; we describe this as a confirmatory/exploratory split rather than a formal pre-registration, since no external timestamp exists. The main text applies the more conservative all-10-benchmark correction (Bonferroni-adjusted $p = .017 \times 10 = .170$). \textbf{Sensitivity:} correcting across only the six confirmatory benchmarks yields adjusted $p = .017 \times 6 = .100$, still above conventional significance.
15	
16	\paragraph{One-sided test.} If one adopts the prior that attention should reduce cross-architecture variance, the one-sided permutation $p$-value for LAMBADA is $1/120 \approx 0.0083$. Under 10-benchmark Bonferroni correction, this yields an adjusted $p = 0.083$, above the conventional threshold. We report two-sided tests throughout the main text as the more conservative choice; the one-sided result is noted here for completeness.
17	
18	\paragraph{Exploratory benchmarks.} Four additional benchmarks (BoolQ, PIQA, SciQ, XStoryCloze) were added as exploratory tests. All benchmarks share the same 10-benchmark correction (adjusted threshold $\alpha / 10 = 0.005$) and the four exploratory benchmarks are labeled as such throughout the paper. The all-10 Bonferroni correction reported in the main text is the only correction used for inference; the exploratory 6-benchmark subset correction in this appendix is provided for transparency.
19	
20	\paragraph{Supplementary benchmark.} COPA ($n = 100$) is treated as supplementary due to its small sample size. It is excluded from both correction families and reported separately with the $\dagger$ annotation in Table~\ref{tab:convergence}.
21	
22	\section{Convergence Detail}\label{app:convergence_detail}
23	
24	% Figure moved to main text (\S\ref{ssec:decoupling}).
25	
26	Beyond LAMBADA ($\rho = -1.0$), two benchmarks show moderate negative correlations that do not reach significance: ARC-Easy and MMLU (both $\rho = -0.7$, $p = .233$). Both are classified as ``Mixed'' tasks combining retrieval with reasoning demands. The sensitivity analysis (Appendix~\ref{app:sensitivity}) shows that MMLU's correlation reverses upon GDN exclusion ($\rho = +0.6$), indicating dependence on a single architecture; ARC-Easy's correlation is more stable. COPA ($n = 100$; supplementary) shows $\rho = -0.67$ with a large $\sigma$ ratio (5.57), consistent with LAMBADA's pattern but unreliable due to small sample size.
27	
28	Several benchmarks show positive or near-zero $\rho$ (BoolQ: $+0.2$; ARC-C: $+0.6$; HellaSwag: $+0.3$; WinoGrande: $+0.1$; SciQ: $+0.1$), indicating that attention does not systematically reduce cross-architecture variance on reasoning or comprehension tasks. The contrast with LAMBADA is consistent with attention's convergence benefit being specific to tasks requiring direct token-level recall \citep{arora2024zoology,arora2024based} rather than multi-step inference.
29	
30	\paragraph{Regression to the mean.} The direction of LAMBADA's aggregate convergence is consistent with regression to the mean: GDN (highest pure accuracy, 0.543) declines to 0.513 under h3-1, while HGRN2 (lowest, 0.484) rises to 0.514, yielding a $5\times$ $\sigma$ compression ($0.024 \to 0.005$). However, three observations argue against a purely statistical artifact. First, the $5\times$ reduction in cross-architecture $\sigma$ far exceeds typical regression amplitudes. Second, the direction is entirely determined by architecture identity, not random fluctuation: HGRN2 accuracy increases monotonically across all attention ratios, while GDN decreases monotonically---a pattern inconsistent with noise-driven mean reversion. Third, per-example analysis (\S\ref{ssec:per_example}) reveals architecture-specific patterns: GDN's net $-153$ examples and HGRN2's net $+153$ examples reflect distinct helped/hurt profiles with low cross-architecture Jaccard overlap, indicating that the aggregate convergence arises from structured, architecture-dependent per-example changes rather than symmetric regression.
31	
32	\section{Scale-Dependent Convergence}\label{app:scale_convergence}
33	
34	At 1.3B parameters, LAMBADA convergence is monotonic: $\sigma$ decreases at every attention level from 0\% through 25\% ($\rho = -1.0$). At 340M, convergence is partial: $\sigma$ reaches a maximum reduction of 56\% at intermediate attention ratios but rebounds at h3-1, yielding a net endpoint reduction of 36\%. The trajectory is non-monotonic, and the highest-attention model does not achieve the lowest cross-architecture variance. One possible interpretation is that at smaller scale, the capacity overhead of attention layers creates interference that offsets the retrieval benefit.
35	
36	This contrast is a preliminary observation from two data points (not a scaling law). Despite the aggregate divergence at 340M, mean pairwise Jaccard is similar at both scales ($J \approx 0.09$), extending the decoupling observation (\S\ref{ssec:decoupling}) to the scale dimension.
37	
38	\section{Sensitivity Analyses}\label{app:sensitivity}
39	
40	\subsection{Bootstrap Confidence Intervals}
41	
42	We construct 95\% bootstrap confidence intervals for the Spearman $\rho$ between attention ratio and cross-architecture $\sigma$ on LAMBADA using 10{,}000 resamples at the architecture level ($n = 3$ architectures). Of these resamples, 11.25\% are degenerate: they consist of same-architecture triplicates, which produce a constant $\sigma$ vector and therefore an undefined $\rho$ (division by zero in the rank correlation formula). These are excluded from the confidence interval computation because they carry no information about the correlation, not because they represent $\rho = 0$.
43	
44	The BCa (bias-corrected and accelerated) correction degenerates at the $\rho = -1.0$ boundary because the acceleration parameter requires finite jackknife variance, which collapses when the point estimate is at the distributional limit. We therefore report percentile confidence intervals instead. From the 88.75\% informative resamples, the 95\% percentile CI is $[-1.0,\,-0.7]$, which excludes zero.
45	
46	\subsection{GDN Exclusion Sensitivity}
47	
48	The GDN h3-1 configuration uses 16 attention heads rather than 32 (see Appendix~\ref{app:gdn_confound}). To assess the influence of this confound, we recompute all convergence correlations after excluding GDN, leaving two architectures (RetNet, HGRN2) at five attention ratios.
49	
50	Table~\ref{tab:gdn_sensitivity} reports the results for benchmarks where the correlation changes by $|\Delta\rho| \geq 0.3$. LAMBADA weakens from $\rho = -1.0$ to $\rho = -0.7$ ($p = .233$), consistent with GDN contributing to the convergence signal. MMLU reverses from $\rho = -0.7$ to $\rho = +0.6$, confirming that the moderate negative correlation on MMLU depends on GDN's inclusion and should not be interpreted as evidence of convergence.
51	
52	\begin{table}[ht]
53	\centering
54	\small
55	\caption{Effect of GDN exclusion on Spearman $\rho$ (attention ratio vs.\ cross-architecture $\sigma$) at 1.3B scale. Only benchmarks with $|\Delta\rho| \geq 0.3$ shown.}
56	\label{tab:gdn_sensitivity}
57	\begin{tabular}{lrrrr}
58	\toprule
59	Benchmark & $\rho_{\text{all}}$ & $\rho_{\text{no-GDN}}$ & $\Delta\rho$ & $p_{\text{no-GDN}}$ \\
60	\midrule
61	LAMBADA & $-1.0$ & $-0.7$ & $+0.3$ & .233 \\
62	MMLU & $-0.7$ & $+0.6$ & $+1.3$ & .350 \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\section{GDN Attention Head Confound}\label{app:gdn_confound}
68	
69	In the \citet{wang2025hybrid} model zoo, the GDN h3-1 configuration at 1.3B scale uses 16 attention heads per attention layer, while all other hybrid configurations (across GDN, RetNet, and HGRN2) use 32 attention heads. This is a design choice in the original model zoo, not an error. The reduced head count changes the per-head dimension and may affect the attention capacity of GDN h3-1 relative to other configurations.
70	
71	This confound is relevant because the convergence analysis measures cross-architecture $\sigma$ at each attention ratio. At the h3-1 ratio (25\% attention), GDN's attention layers have a different internal structure than those of RetNet and HGRN2, which could contribute to variance reduction (or inflation) for reasons unrelated to the recurrent--attention interaction under study.
72	
73	The sensitivity analysis in Appendix~\ref{app:sensitivity} shows that removing GDN weakens the LAMBADA convergence correlation from $\rho = -1.0$ to $\rho = -0.7$. This weakening is partially attributable to the reduced sample size ($n = 2$ architectures) and partially to the confound itself. We cannot separate these two effects with the available data.
74	
75	\section{Attention Weight Analysis}\label{app:attention_patterns}
76	
77	We extract attention weight matrices from the 1.3B h3-1 models of all three architectures using forward hooks on each attention layer. While \citet{ali2025hidden} show that SSM layers learn implicit attention patterns, our analysis focuses on the explicit attention layers interleaved within the hybrid architecture. For each layer, we compute the mean attention distribution across all 5{,}153 LAMBADA examples and measure cross-architecture similarity via cosine similarity.
78	
79	\subsection{Cross-Architecture Cosine Similarity}
80	
81	Table~\ref{tab:attn_cosine} reports cosine similarity between mean attention distributions at selected layers and averaged across all layers.
82	
83	\begin{table}[ht]
84	\centering
85	\caption{Cosine similarity between mean attention weight distributions of architecture pairs at selected layers (1.3B h3-1 models on LAMBADA).}
86	\label{tab:attn_cosine}
87	\resizebox{\columnwidth}{!}{%
88	\begin{tabular}{lrrr}
89	\toprule
90	Layer & GDN--RetNet & GDN--HGRN2 & HGRN2--RetNet \\
91	\midrule
92	L2 (early) & 0.995 & 0.244 & 0.196 \\
93	L20 (deep) & 0.986 & 0.942 & 0.943 \\
94	\midrule
95	Mean (all layers) & 0.905 & 0.766 & 0.698 \\
96	\bottomrule
97	\end{tabular}%
98	}
99	\end{table}
100	
101	At layer 2, GDN and RetNet produce nearly identical attention distributions (cosine 0.995), while HGRN2 diverges from both (cosine $< 0.25$). By layer 20, all three architectures converge to similar attention patterns (cosine $> 0.94$). The layer-wise trajectory suggests that early-layer attention patterns are shaped by the preceding recurrent layers (which differ across architectures), while deeper layers converge regardless of the recurrent substrate.
102	
103	\subsection{Helped vs.\ Hurt Attention Entropy}
104	
105	To test whether the attention mechanism itself differs between helped and hurt examples, we compute the Shannon entropy of the attention distribution for each example at each attention layer and compare the mean entropy of helped examples against hurt examples within each architecture.
106	
107	\begin{table}[ht]
108	\centering
109	\caption{Mean attention entropy difference (helped $-$ hurt) averaged across attention layers (1.3B h3-1 models on LAMBADA). Values near zero indicate that the attention mechanism does not discriminate between helped and hurt examples.}
110	\label{tab:attn_entropy}
111	\begin{tabular}{lr}
112	\toprule
113	Architecture & $\Delta H$ (helped $-$ hurt) \\
114	\midrule
115	GDN & $-0.0009$ \\
116	RetNet & $+0.0179$ \\
117	HGRN2 & $+0.0020$ \\
118	\bottomrule
119	\end{tabular}
120	\end{table}
121	
122	GDN and HGRN2 show negligible entropy differences ($|\Delta H| \leq 0.002$). RetNet's $\Delta H = +0.018$ is small in absolute terms but slightly larger; helped examples receive marginally more diffuse attention in RetNet. Across all three architectures, the differences are insufficient to explain the per-example divergence, consistent with per-example effects not being explained by attention weight patterns and likely originating in the recurrent layers.
123	
124	\subsection{Last-5 Attention Mass}
125	
126	We also measure the fraction of attention mass allocated to the last five tokens, which captures whether the attention mechanism concentrates differently on recent context for helped vs.\ hurt examples.
127	
128	\begin{table}[ht]
129	\centering
130	\caption{Mean attention mass on last-5 tokens for helped and hurt examples, averaged across attention layers (1.3B h3-1 models on LAMBADA).}
131	\label{tab:attn_last5}
132	\begin{tabular}{lrr}
133	\toprule
134	Architecture & Helped & Hurt \\
135	\midrule
136	GDN & 0.0834 & 0.0831 \\
137	RetNet & 0.1578 & 0.1591 \\
138	HGRN2 & 0.0453 & 0.0467 \\
139	\bottomrule
140	\end{tabular}
141	\end{table}
142	
143	No architecture shows a meaningful difference in last-5 attention mass between helped and hurt examples (Table~\ref{tab:attn_last5}). This further supports the conclusion that the per-example divergence is not driven by differential attention allocation.
144	
145	\section{Cross-Scale Per-Example Comparisons}\label{app:cross_scale}
146	
147	\subsection{Within-Scale Pairwise Jaccard}
148	
149	Table~\ref{tab:within_scale_jaccard} reports the within-scale pairwise Jaccard similarity between architectures' helped and hurt sets at both scales. Mean values are similar across scales (340M: 0.094/0.090; 1.3B: 0.100/0.093), indicating that per-example architecture specificity is consistent across the two scales examined.
150	
151	\begin{table}[ht]
152	\centering
153	\small
154	\caption{Within-scale pairwise Jaccard similarity of per-example effects (pure $\to$ h3-1) on LAMBADA. Each row compares the helped (or hurt) sets of two architectures at the same scale.}
155	\label{tab:within_scale_jaccard}
156	\begin{tabular}{llcc}
157	\toprule
158	Scale & Pair & $J_{\text{helped}}$ & $J_{\text{hurt}}$ \\
159	\midrule
160	\multirow{4}{*}{340M} & GDN--RetNet & 0.092 & 0.109 \\
161	& GDN--HGRN2 & 0.084 & 0.075 \\
162	& RetNet--HGRN2 & 0.108 & 0.085 \\
163	& \textit{Mean} & \textit{0.094} & \textit{0.090} \\
164	\midrule
165	\multirow{4}{*}{1.3B} & GDN--RetNet & 0.092 & 0.103 \\
166	& GDN--HGRN2 & 0.100 & 0.088 \\
167	& RetNet--HGRN2 & 0.108 & 0.087 \\
168	& \textit{Mean} & \textit{0.100} & \textit{0.093} \\
169	\bottomrule
170	\end{tabular}
171	\end{table}
172	
173	\subsection{Cross-Scale Pairwise Jaccard}
174	
175	For each architecture, we compare the helped and hurt sets of the pure $\to$ h3-1 transition at 340M and 1.3B scale on LAMBADA.
176	The comparison uses the same classification scheme as \S\ref{ssec:per_example}: an example is ``helped'' if it is correct only in the hybrid variant and ``hurt'' if correct only in the pure baseline.
177	All pairwise Jaccard values fall below 0.10, indicating that scale variation is associated with per-example predictive multiplicity analogous to the cross-architecture effect reported in \S\ref{ssec:per_example}.
178	
179	\begin{table}[ht]
180	\centering
181	\caption{Cross-scale pairwise Jaccard similarity of per-example effects (pure $\to$ h3-1) between 340M and 1.3B on LAMBADA. All values below 0.10.}
182	\label{tab:cross_scale_jaccard}
183	\begin{tabular}{llcc}
184	\toprule
185	Architecture & Scale Pair & $J_{\text{helped}}$ & $J_{\text{hurt}}$ \\
186	\midrule
187	GDN & 340M $\leftrightarrow$ 1.3B & 0.047 & 0.087 \\
188	RetNet & 340M $\leftrightarrow$ 1.3B & 0.059 & 0.073 \\
189	HGRN2 & 340M $\leftrightarrow$ 1.3B & 0.089 & 0.055 \\
190	\midrule
191	Mean & & 0.065 & 0.072 \\
192	\bottomrule
193	\end{tabular}
194	\end{table}
195	
196	\section{Per-Example Effect Counts}\label{app:per_example_counts}
197	
198	Table~\ref{tab:per_example} reports the full per-example effect counts for each architecture at 1.3B scale.
199	
200	\begin{table}[ht]
201	\centering
202	\caption{Per-example effects of attention (pure $\to$ h3-1) on 5{,}153 LAMBADA examples at 1.3B scale. $\bar{J}$: mean pairwise Jaccard similarity with other architectures across helped and hurt sets.}
203	\label{tab:per_example}
204	\begin{tabular}{lrrrr}
205	\toprule
206	Architecture & Helped & Hurt & Net & $\bar{J}$ \\
207	\midrule
208	GDN & 462 & 615 & $-$153 & .096 \\
209	RetNet & 426 & 495 & $-$69 & .100 \\
210	HGRN2 & 548 & 395 & $+$153 & .104 \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	\section{Normalized Jaccard Effect Size}\label{app:normalized_es}
216	
217	To assess whether low observed Jaccard reflects a floor effect imposed by unequal set sizes, we compute the theoretical upper bound $J_{\max} = \min(|A|,|B|) / \max(|A|,|B|)$ and the normalized effect size $(J_{\text{obs}} - J_{\text{null}}) / (J_{\max} - J_{\text{null}})$, which measures observed overlap as a fraction of the achievable range above chance. Table~\ref{tab:normalized_es} reports per-pair results.
218	
219	\begin{table}[ht]
220	\centering
221	\small
222	\caption{Normalized Jaccard effect size for each architecture pair (1.3B h3-1 on LAMBADA). $J_{\max}$: theoretical upper bound given set sizes. Normalized ES: fraction of achievable overlap above chance.}
223	\label{tab:normalized_es}
224	\resizebox{\columnwidth}{!}{%
225	\begin{tabular}{llcccc}
226	\toprule
227	Category & Pair & $J_{\text{obs}}$ & $J_{\max}$ & $J_{\text{null}}$ & Norm.\ ES \\
228	\midrule
229	Helped & GDN--RetNet & .092 & .922 & .045 & .054 \\
230	 & GDN--HGRN2 & .100 & .843 & .051 & .062 \\
231	 & RetNet--HGRN2 & .108 & .777 & .049 & .081 \\
232	 & \textit{Mean} & \textit{.100} & \textit{.848} & \textit{.048} & \textit{.066} \\
233	\midrule
234	Hurt & GDN--RetNet & .103 & .805 & .056 & .063 \\
235	 & GDN--HGRN2 & .088 & .642 & .049 & .066 \\
236	 & RetNet--HGRN2 & .087 & .798 & .045 & .056 \\
237	 & \textit{Mean} & \textit{.093} & \textit{.748} & \textit{.050} & \textit{.062} \\
238	\bottomrule
239	\end{tabular}%
240	}
241	\end{table}
242	
243	All normalized effect sizes fall below 0.10, confirming that observed overlap reaches only 6--7\% of the theoretical maximum. The low Jaccard values cannot be attributed to set-size constraints.
244	
245	\section{ARC-Easy Per-Example Analysis}\label{app:arceasy}
246	
247	Table~\ref{tab:arceasy_effects} reports per-example effect counts on ARC-Easy ($N = 2{,}376$) at 1.3B scale for each attention ratio. Unlike LAMBADA, ARC-Easy shows no aggregate convergence ($\rho = -0.20$, $p = .783$). HGRN2 is net positive at all ratios; GDN and RetNet are mixed.
248	
249	\begin{table}[ht]
250	\centering
251	\small
252	\caption{Per-example effects on ARC-Easy at 1.3B scale. Net = helped $-$ hurt.}
253	\label{tab:arceasy_effects}
254	\resizebox{\columnwidth}{!}{%
255	\begin{tabular}{llrrr}
256	\toprule
257	Architecture & Ratio & Helped & Hurt & Net \\
258	\midrule
259	\multirow{4}{*}{GDN} & h24-1 & 178 & 185 & $-$7 \\
260	& h12-1 & 176 & 206 & $-$30 \\
261	& h6-1 & 170 & 157 & $+$13 \\
262	& h3-1 & 171 & 180 & $-$9 \\
263	\midrule
264	\multirow{4}{*}{RetNet} & h24-1 & 158 & 168 & $-$10 \\
265	& h12-1 & 163 & 146 & $+$17 \\
266	& h6-1 & 159 & 147 & $+$12 \\
267	& h3-1 & 144 & 184 & $-$40 \\
268	\midrule
269	\multirow{4}{*}{HGRN2} & h24-1 & 160 & 119 & $+$41 \\
270	& h12-1 & 159 & 111 & $+$48 \\
271	& h6-1 & 185 & 118 & $+$67 \\
272	& h3-1 & 164 & 146 & $+$18 \\
273	\bottomrule
274	\end{tabular}%
275	}
276	\end{table}
277	
278	Table~\ref{tab:arceasy_ambiguity} reports the ambiguity $\alpha$ \citep{marx2020predictive} at each attention ratio for all four main benchmarks. Within-benchmark ranges are 0.004 (HellaSwag), 0.011 (PIQA), 0.025 (ARC-Easy), and 0.022 (LAMBADA), all below the 0.03 threshold reported in \S\ref{ssec:per_example}.
279	
280	\begin{table}[ht]
281	\centering
282	\caption{Ambiguity $\alpha$ across attention ratios (1.3B scale). 95\% CI: BCa bootstrap (10{,}000 resamples) at the pure-recurrent configuration.}
283	\label{tab:arceasy_ambiguity}
284	\resizebox{\columnwidth}{!}{%
285	\begin{tabular}{lcccccc}
286	\toprule
287	Benchmark & Pure & h24-1 & h12-1 & h6-1 & h3-1 & 95\% CI (pure) \\
288	\midrule
289	PIQA & .143 & .138 & .132 & .143 & .140 & $[.127,\,.159]$ \\
290	HellaSwag & .148 & .150 & .148 & .146 & .150 & $[.141,\,.155]$ \\
291	ARC-Easy & .205 & .226 & .223 & .201 & .210 & $[.189,\,.221]$ \\
292	LAMBADA & .307 & .300 & .316 & .294 & .296 & $[.294,\,.319]$ \\
293	\bottomrule
294	\end{tabular}%
295	}
296	\end{table}
297	
298	\section{Jaccard Permutation Test}\label{app:jaccard_permutation}
299	
300	To assess whether the observed pairwise Jaccard similarities exceed what would be expected under independence, we perform a permutation test. For each architecture pair at 1.3B h3-1, we hold the helped (or hurt) set sizes fixed and randomly assign example indices to each set (10{,}000 permutations, seed 42). Table~\ref{tab:jaccard_perm} reports the observed $J$, the null baseline $J_{\text{null}}$ (mean over permutations), and the $z$-score.
301	
302	\begin{table}[ht]
303	\centering
304	\caption{Permutation test for pairwise Jaccard similarity (1.3B h3-1 on LAMBADA, 10{,}000 permutations). All observed values significantly exceed the independence baseline.}
305	\label{tab:jaccard_perm}
306	\resizebox{\columnwidth}{!}{%
307	\begin{tabular}{llcccc}
308	\toprule
309	Category & Pair & $J_{\text{obs}}$ & $J_{\text{null}}$ & $z$ & $p$ \\
310	\midrule
311	Helped & GDN--HGRN2 & .100 & .051 & 7.11 & $<$.0001 \\
312	 & GDN--RetNet & .092 & .045 & 6.75 & $<$.0001 \\
313	 & HGRN2--RetNet & .108 & .049 & 8.61 & $<$.0001 \\
314	\midrule
315	Hurt & GDN--HGRN2 & .088 & .049 & 5.91 & $<$.0001 \\
316	 & GDN--RetNet & .103 & .056 & 6.85 & $<$.0001 \\
317	 & HGRN2--RetNet & .087 & .045 & 6.05 & $<$.0001 \\
318	\bottomrule
319	\end{tabular}%
320	}
321	\end{table}
322	
323	All six comparisons yield $z > 5.9$ ($p < .0001$). The null baseline averages $J_{\text{null}} \approx 0.049$; observed values are approximately twice this level. The overlap between architectures' per-example effect sets is therefore structured rather than a product of random set overlap given the set sizes.
324	
325	\section{Transformer Entrainment Comparison}\label{app:transformer_entrainment}
326	
327	To test whether attention layers make hybrid models' per-example behavior converge toward a pure Transformer, we compare the correct-example sets of each architecture's pure and h3-1 variants against a 1.3B Transformer baseline (accuracy 48.1\%) on LAMBADA. Table~\ref{tab:transformer_jaccard} reports the Jaccard similarity between each model's correct set and the Transformer's correct set.
328	
329	\begin{table}[ht]
330	\centering
331	\caption{Jaccard similarity between each model's correct set and the Transformer correct set on LAMBADA (1.3B scale). All three h3-1 hybrids are more similar to the Transformer than their pure counterparts.}
332	\label{tab:transformer_jaccard}
333	\small
334	\begin{tabular}{lccc}
335	\toprule
336	Architecture & $J_{\text{pure,T}}$ & $J_{\text{h3-1,T}}$ & $\Delta$ \\
337	\midrule
338	GDN & 0.645 & 0.649 & $+$0.005 \\
339	RetNet & 0.679 & 0.694 & $+$0.015 \\
340	HGRN2 & 0.672 & 0.701 & $+$0.029 \\
341	\bottomrule
342	\end{tabular}
343	\end{table}
344	
345	All three architectures show positive $\Delta$: the h3-1 correct set is more similar to the Transformer correct set than the pure correct set is. The effect is strongest for HGRN2 ($+$0.029) and weakest for GDN ($+$0.005). This ordering is consistent with HGRN2 being the only architecture with a positive net per-example effect from attention (Table~\ref{tab:per_example}). The Transformer itself achieves the lowest accuracy among all models, so the convergence is not explained by hybrid models degrading toward Transformer-level performance; rather, adding attention shifts which specific examples the hybrid gets correct toward the Transformer's pattern.
346	
347	\section{Within-Architecture Per-Example Stability}\label{app:within_arch_stability}
348	
349	Per-example effect sets exhibit a three-tier Jaccard hierarchy on LAMBADA (1.3B scale). Under independence (permutation baseline), pairwise Jaccard is $J \approx 0.05$. Cross-architecture comparisons (different architectures at the same attention ratio) yield $J \approx 0.10$, approximately $2\times$ baseline. Within-architecture comparisons (same architecture across different attention ratios) yield $J \approx 0.33$, approximately $7\times$ baseline and $3\times$ the cross-architecture level. Architecture identity therefore has approximately three times the influence of attention ratio on per-example effects.
350	
351	Table~\ref{tab:within_arch_summary} reports mean within-architecture Jaccard for each architecture. HGRN2 shows the highest helped overlap and lowest hurt overlap, consistent with its monotonically increasing helped count across ratios (479 $\to$ 548).
352	
353	\begin{table}[ht]
354	\centering
355	\caption{Mean within-architecture pairwise Jaccard similarity across attention ratios (1.3B, LAMBADA). Each mean is computed over all six ratio pairs per architecture.}
356	\label{tab:within_arch_summary}
357	\begin{tabular}{lcc}
358	\toprule
359	Architecture & $\bar{J}_{\text{helped}}$ & $\bar{J}_{\text{hurt}}$ \\
360	\midrule
361	GDN & 0.338 & 0.319 \\
362	RetNet & 0.333 & 0.321 \\
363	HGRN2 & 0.373 & 0.291 \\
364	\midrule
365	\textit{Overall mean} & \textit{0.348} & \textit{0.310} \\
366	\bottomrule
367	\end{tabular}
368	\end{table}
369	
370	Table~\ref{tab:within_arch_pairwise} reports the full pairwise Jaccard matrix. Attention ratios are denoted by their h$k$-1 labels: h24-1 (4\%), h12-1 (7.7\%), h6-1 (14.3\%), h3-1 (25\%).
371	
372	\begin{table}[ht]
373	\centering
374	\small
375	\caption{Within-architecture pairwise Jaccard similarity between helped and hurt sets at different attention ratios (1.3B, LAMBADA). Each cell compares the per-example effect sets of two attention configurations within the same architecture.}
376	\label{tab:within_arch_pairwise}
377	\resizebox{\columnwidth}{!}{%
378	\begin{tabular}{llcccccc}
379	\toprule
380	 & & \multicolumn{6}{c}{Ratio pair} \\
381	\cmidrule(lr){3-8}
382	Arch & Cat & h24--h12 & h24--h6 & h24--h3 & h12--h6 & h12--h3 & h6--h3 \\
383	\midrule
384	\multirow{2}{*}{GDN} & Helped & .345 & .335 & .311 & .344 & .341 & .352 \\
385	 & Hurt & .310 & .328 & .320 & .331 & .281 & .345 \\
386	\midrule
387	\multirow{2}{*}{RetNet} & Helped & .354 & .314 & .334 & .322 & .330 & .345 \\
388	 & Hurt & .316 & .334 & .307 & .301 & .324 & .343 \\
389	\midrule
390	\multirow{2}{*}{HGRN2} & Helped & .359 & .369 & .375 & .368 & .378 & .388 \\
391	 & Hurt & .292 & .289 & .298 & .273 & .309 & .287 \\
392	\bottomrule
393	\end{tabular}%
394	}
395	\end{table}
396	
397	Adjacent ratio pairs (e.g., h24-1 vs.\ h12-1) do not exhibit systematically higher Jaccard than non-adjacent pairs (e.g., h24-1 vs.\ h3-1). Across all architectures, the mean Jaccard for adjacent pairs is 0.353 (helped) and 0.311 (hurt), compared with 0.343 (helped) and 0.310 (hurt) for non-adjacent pairs. The negligible difference indicates that the mapping from attention ratio to per-example effects is non-smooth: doubling the attention ratio does not produce a proportionally more similar set of affected examples.
398	
399	\section{Cross-Benchmark Jaccard Trajectories}\label{app:cross_bench_jaccard}
400	
401	To test whether the Jaccard stability pattern is specific to LAMBADA or a general property, we compute mean pairwise Jaccard trajectories across all four hybrid attention ratios on all four main benchmarks. Table~\ref{tab:cross_bench_jaccard} reports the results. On every benchmark, Jaccard shows no statistically significant trend with attention ratio (all $\rho \leq 0.80$, $p \geq 0.333$), with values uniformly between 0.08 and 0.11. The stability observed at the first attention level on LAMBADA (\S\ref{ssec:decoupling}) thus appears to hold across benchmarks: once any attention is present, each architecture's per-example response remains largely consistent regardless of attention ratio.
402	
403	\begin{table}[ht]
404	\centering
405	\small
406	\caption{Mean pairwise Jaccard (mean of helped and hurt sets, 3 architecture pairs) across attention ratios and benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and $\bar{J}$. All $p \geq 0.333$.}
407	\label{tab:cross_bench_jaccard}
408	\resizebox{\columnwidth}{!}{%
409	\begin{tabular}{@{}lcccccc@{}}
410	\toprule
411	Benchmark & h24-1 & h12-1 & h6-1 & h3-1 & $\rho$ & $p$ \\
412	\midrule
413	LAMBADA & .091 & .088 & .096 & .097 & 0.80 & .333 \\
414	HellaSwag & .084 & .081 & .091 & .086 & 0.60 & .417 \\
415	PIQA & .089 & .096 & .089 & .095 & 0.00 & 1.00 \\
416	ARC-Easy & .084 & .099 & .091 & .109 & 0.80 & .333 \\
417	\bottomrule
418	\end{tabular}}
419	\end{table}
420	
421	\section{Continuous-Threshold Jaccard Analysis}\label{app:continuous_jaccard}
422	
423	The main text binarizes per-example effects at the correctness boundary. To verify that low cross-architecture Jaccard is not an artifact of this binarization, we compute Jaccard similarity using a continuous confidence threshold $\tau$: two architectures' effect sets are defined as the examples whose target-token $|\log p|$ changes by more than $\tau$ when attention is added. On LAMBADA, mean pairwise Jaccard decreases monotonically from 0.26 ($\tau = 0.00$, any change) to 0.05 ($\tau = 0.30$, large changes only). ARC-Easy and PIQA show the same monotonic decrease. The binary threshold ($\tau = 0$, correctness flip) thus represents the upper end of cross-architecture overlap; restricting to confident transitions further reduces agreement, confirming that low Jaccard is robust to the choice of binarization threshold.
424	
425	\section{Target-Token Confidence Margin}
426	\label{app:confidence_margin}
427	
428	We analyze whether pure-model confidence on the target token predicts whether attention will help or hurt on a given example.
429	We define confidence as $|\log p_{\text{pure}}(y^*)|$, where $y^*$ is the target token: lower values indicate higher probability (near-correct).
430	We initially tested raw perplexity as a predictor of helped/hurt status, but found that within-category controls (C1/C2) are necessary to isolate attention effects from the definitional confound between pure-correct and pure-wrong populations.
431	
432	Table~\ref{tab:cm_c1} compares hurt versus stayed-right samples (both pure-correct): hurt samples have significantly lower target-token probability (higher $|\log p|$), confirming that weakly-correct predictions are vulnerable to attention disruption.
433	Table~\ref{tab:cm_c2} compares helped versus stayed-wrong samples (both pure-wrong): helped samples have higher target-token probability (lower $|\log p|$), confirming that near-miss errors are rescuable.
434	This pattern is consistent across all three architectures ($|d| = 0.73$--$0.92$, all $p < 10^{-54}$) but does not alter the cross-architecture Jaccard findings---within-architecture predictability coexists with cross-architecture divergence.
435	
436	\begin{table}[ht]
437	\centering
438	\caption{Control 1: Pure-correct samples---hurt vs.\ stayed-right. Higher mean $|\log p|$ indicates lower target-token probability (less confident correct).}
439	\label{tab:cm_c1}
440	\resizebox{\columnwidth}{!}{%
441	\begin{tabular}{lrrrrr}
442	\toprule
443	Architecture & $n_{\text{hurt}}$ & $n_{\text{stay}}$ & Hurt mean & Stay mean & Cohen's $d$ \\
444	\midrule
445	GDN (h12-1) & 519 & 2281 & 1.049 & 0.576 & 0.87 \\
446	RetNet (h3-1) & 497 & 2169 & 1.293 & 0.785 & 0.83 \\
447	HGRN2 (h3-1) & 392 & 2102 & 1.481 & 0.899 & 0.92 \\
448	\bottomrule
449	\end{tabular}
450	}
451	\end{table}
452	
453	\begin{table}[ht]
454	\centering
455	\caption{Control 2: Pure-wrong samples---helped vs.\ stayed-wrong. Lower mean $|\log p|$ indicates higher target-token probability (near-miss error).}
456	\label{tab:cm_c2}
457	\resizebox{\columnwidth}{!}{%
458	\begin{tabular}{lrrrrr}
459	\toprule
460	Architecture & $n_{\text{help}}$ & $n_{\text{stay}}$ & Help mean & Stay mean & Cohen's $d$ \\
461	\midrule
462	GDN (h12-1) & 480 & 1873 & 2.459 & 4.189 & $-$0.75 \\
463	RetNet (h3-1) & 420 & 2067 & 2.478 & 4.103 & $-$0.73 \\
464	HGRN2 (h3-1) & 548 & 2111 & 2.500 & 4.112 & $-$0.77 \\
465	\bottomrule
466	\end{tabular}
467	}
468	\end{table}
469	
470	\subsection{Cross-Benchmark Extension}\label{app:cm_cross}
471	
472	The confidence margin pattern extends beyond LAMBADA to multiple-choice benchmarks, though with smaller effect sizes. Table~\ref{tab:cm_cross_c2} reports the rescue analysis (helped vs.\ stayed-wrong) on HellaSwag and ARC-Easy. All nine comparisons (three benchmarks $\times$ three architectures) are significant, confirming that attention consistently rescues near-miss errors regardless of task type. Effect sizes range from small on HellaSwag ($d = 0.13$--$0.17$) to medium on ARC-Easy ($d = 0.51$--$0.60$), compared to large on LAMBADA ($d = 0.73$--$0.77$); the attenuation on HellaSwag reflects noisier confidence proxies under length-normalized scoring. Table~\ref{tab:cm_cross_c1} reports the disruption analysis (hurt vs.\ stayed-right); two of six comparisons are significant (all on ARC-Easy) with small effect sizes ($d = 0.13$--$0.26$), indicating that the disruption signal is weaker on multiple-choice tasks and absent on HellaSwag under \texttt{acc\_norm}. The asymmetry between rescue and disruption reflects task structure: near-miss errors are an intrinsic sample property (the model almost produced the correct answer regardless of format), while borderline correctness in multiple-choice settings depends on relative option ranking rather than absolute confidence, reducing the raw log-likelihood margin's predictive power for vulnerability.
473	
474	\begin{table}[ht]
475	\centering
476	\caption{Cross-benchmark rescue analysis (Control 2): helped vs.\ stayed-wrong on HellaSwag and ARC-Easy (1.3B h3-1).}
477	\label{tab:cm_cross_c2}
478	\resizebox{\columnwidth}{!}{%
479	\begin{tabular}{llrr}
480	\toprule
481	Benchmark & Architecture & Cohen's $d$ & $p$ \\
482	\midrule
483	HellaSwag & GDN & $-$0.166 & $6.1 \times 10^{-4}$ \\
484	 & RetNet & $-$0.132 & $1.4 \times 10^{-2}$ \\
485	 & HGRN2 & $-$0.164 & $1.4 \times 10^{-3}$ \\
486	\midrule
487	ARC-Easy & GDN & $-$0.60 & $1.0 \times 10^{-13}$ \\
488	 & RetNet & $-$0.51 & $5.3 \times 10^{-10}$ \\
489	 & HGRN2 & $-$0.53 & $5.4 \times 10^{-10}$ \\
490	\bottomrule
491	\end{tabular}%
492	}
493	\end{table}
494	
495	\begin{table}[ht]
496	\centering
497	\caption{Cross-benchmark disruption analysis (Control 1): hurt vs.\ stayed-right on HellaSwag and ARC-Easy (1.3B h3-1).}
498	\label{tab:cm_cross_c1}
499	\resizebox{\columnwidth}{!}{%
500	\begin{tabular}{llrrl}
501	\toprule
502	Benchmark & Architecture & Cohen's $d$ & $p$ & Sig.? \\
503	\midrule
504	HellaSwag & GDN & 0.009 & .999 & No \\
505	 & RetNet & $-$0.035 & .453 & No \\
506	 & HGRN2 & $-$0.062 & .274 & No \\
507	\midrule
508	ARC-Easy & GDN & 0.26 & $3.2 \times 10^{-4}$ & Yes \\
509	 & RetNet & 0.22 & $2.8 \times 10^{-3}$ & Yes \\
510	 & HGRN2 & 0.13 & .145 & No \\
511	\bottomrule
512	\end{tabular}%
513	}
514	\end{table}
515	
516	\subsection{Prediction Framework}\label{app:prediction_framework}
517	
518	We formalize the confidence margin analysis as a binary prediction task: given a pure-model example and its target-token $|\log p|$, predict whether attention will change the example's correctness. Using the within-category summary statistics (Tables~\ref{tab:cm_c1},~\ref{tab:cm_c2}), we derive analytic AUC from Cohen's $d$ via $\text{AUC} = \Phi(|d|/\sqrt{2})$ and compute Gaussian-intersection thresholds (the $|\log p|$ value at which the two group densities intersect under equal priors).
519	
520	Table~\ref{tab:prediction_auc} reports within-architecture prediction performance. All AUCs exceed 0.69, indicating moderate within-architecture predictive discrimination for attention effects. Disruption prediction is consistently stronger than rescue (mean AUC 0.73 vs.\ 0.70), reflecting the larger effect sizes in Control~1.
521	
522	\begin{table}[ht]
523	\centering
524	\small
525	\caption{Within-architecture prediction of attention effects on LAMBADA (1.3B). AUC$_p$: parametric (from Cohen's $d$); AUC$_e$: empirical (non-parametric).}
526	\label{tab:prediction_auc}
527	\resizebox{\columnwidth}{!}{%
528	\begin{tabular}{@{}lcccccc@{}}
529	\toprule
530	Architecture & \multicolumn{3}{c}{Rescue} & \multicolumn{3}{c}{Disruption} \\
531	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
532	 & AUC$_p$ & AUC$_e$ & $d$ & AUC$_p$ & AUC$_e$ & $d$ \\
533	\midrule
534	GDN (h12-1) & .701 & .756 & 0.75 & .732 & .742 & 0.87 \\
535	RetNet (h3-1) & .696 & .754 & 0.73 & .722 & .735 & 0.83 \\
536	HGRN2 (h3-1) & .708 & .765 & 0.77 & .743 & .748 & 0.92 \\
537	\midrule
538	Mean & .702 & .758 & --- & .732 & .742 & --- \\
539	\bottomrule
540	\end{tabular}}
541	\end{table}
542	
543	\paragraph{Normality verification.} Shapiro-Wilk tests reject normality for all six architecture--set combinations (all $W < 0.98$, $p < 10^{-6}$), but the practical departure varies by group. Disruption-set $|\log p|$ values show mild skewness (0.53--0.77, $W \in [0.955, 0.973]$), closely approximating a normal distribution at the sample sizes involved. Rescue-set values are moderately right-skewed (skewness 1.33--1.41, $W \in [0.899, 0.920]$), following an approximately log-normal distribution. Because the skew is one-sided, parametric AUC estimates (0.70--0.74 in the main text) are conservative lower bounds; non-parametric empirical AUC from the same data yields 0.73--0.77.
544	
545	Despite similar within-architecture AUC, the optimal prediction thresholds differ across architectures for disruption but not rescue (Table~\ref{tab:threshold_gap}). Rescue thresholds cluster tightly (range 0.03 in $|\log p|$), indicating that the rescuability boundary---the confidence level below which pure-wrong examples are likely to be corrected by attention---is architecture-invariant. Disruption thresholds span a 47\% relative range (GDN: 0.70, RetNet: 1.00, HGRN2: 1.14), meaning that the same confidence level on a pure-correct example may predict vulnerability in one architecture but safety in another. This asymmetry constitutes a second dimension of multiplicity beyond per-example disagreement: all three architectures agree on which wrong answers are rescuable, but disagree on which correct answers are vulnerable to disruption.
546	
547	\begin{table}[ht]
548	\centering
549	\small
550	\caption{Gaussian-intersection prediction thresholds ($|\log p|$) across architectures. Relative spread: range/mean.}
551	\label{tab:threshold_gap}
552	\resizebox{\columnwidth}{!}{%
553	\begin{tabular}{@{}lccccr@{}}
554	\toprule
555	 & GDN & RetNet & HGRN2 & Range & Rel.\ spread \\
556	\midrule
557	Rescue & 3.32 & 3.29 & 3.31 & 0.03 & 1.0\% \\
558	Disruption & 0.70 & 1.00 & 1.14 & 0.44 & 46.7\% \\
559	\bottomrule
560	\end{tabular}}
561	\end{table}
562	
563	\section{Calibration Analysis}\label{app:calibration}
564	
565	Cross-architecture disruption threshold variation (\S\ref{ssec:per_example}) could in principle arise from calibration differences rather than genuine differences in per-example processing. We compute expected calibration error (ECE; \citealt{guo2017calibration}) for each architecture's h3-1 model on LAMBADA using 15 equal-width bins. ECE values are similar: GDN 0.222, RetNet 0.224, HGRN2 0.235. The cross-architecture ECE spread (6\%, computed as range/mean) is less than half the disruption threshold spread (47\%; Table~\ref{tab:threshold_gap}), indicating that calibration differences are insufficient to account for the observed threshold divergence. Rescue thresholds, which show only 1\% cross-architecture spread, are consistent with near-identical calibration in the low-confidence regime.
566	
567	\section{BoolQ Supplementary Analysis}
568	\label{app:boolq}
569	
570	BoolQ ($N = 3{,}270$; comprehension, binary yes/no classification) shows the highest ambiguity among the benchmarks we analyzed ($\alpha \approx 0.45$), but the Jaccard significance pattern is mixed: only 12 of 24 architecture $\times$ attention-ratio pair combinations yield $p < .01$. In particular, the RetNet--HGRN2 pair produces 0/8 significant Jaccard values, with several normalized effect sizes below zero, suggesting anti-correlated per-example effects for this pair.
571	
572	\paragraph{Binary classification baseline.} BoolQ is binary classification (two answer choices), whereas LAMBADA, HellaSwag, and ARC-Easy involve open vocabulary prediction or four-way multiple choice. Under a binary task, the null Jaccard baseline $J_{\text{null}}$ is higher because chance overlap between helped/hurt sets is larger when there are fewer ways to be wrong. This elevates the significance threshold: observed Jaccard must be substantially higher to exceed the null, which explains why 12/24 pairs fail to reach significance despite $\bar{J}_h = 0.103$ and $\bar{J}_u = 0.098$---values comparable to the four main benchmarks.
573	
574	\paragraph{Per-example summary.} Table~\ref{tab:boolq_multiplicity} reports the key metrics. The high $\alpha$ reflects that BoolQ examples are more sensitive to architectural variation in the presence of attention: approximately half of all examples change correctness status for at least one architecture. However, the mixed Jaccard significance prevents us from confidently concluding that the cross-architecture overlap structure matches the pattern observed on the four main benchmarks.
575	
576	\begin{table}[ht]
577	\centering
578	\small
579	\caption{BoolQ predictive multiplicity at 1.3B (h3-1).}
580	\label{tab:boolq_multiplicity}
581	\begin{tabular}{@{}lcccccc@{}}
582	\toprule
583	 & $N$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & Sig.\ pairs & $\rho_\alpha$ \\
584	\midrule
585	BoolQ & 3270 & .45 & .103 & .098 & 12/24 & $+0.1$ \\
586	\bottomrule
587	\end{tabular}
588	\par\vspace{1pt}
589	{\footnotesize RetNet--HGRN2: 0/8 significant; multiple normalized ES $< 0$.}
590	\end{table}
591	
592	The significant Jaccard overlap concentrates in GDN--RetNet pairs (8/8 significant), while RetNet--HGRN2 shows none (0/8). This pair-specificity does not appear on the four main benchmarks, where all architecture pairs show significant overlap; it may reflect a BoolQ-specific interaction between binary classification structure and particular recurrent architectures rather than a general property of architecture pairs.
593	
594	\paragraph{Confidence margin.} Confidence margin analysis on BoolQ shows the rescue pattern (C2) partially holds (2/3 architectures significant, $d = 0.16$--$0.36$) but the disruption pattern (C1) is absent (0/3, $|d| \leq 0.10$), consistent with compressed log-likelihood ranges in binary classification reducing the predictive power of confidence margins. This extends the gradient observed across LAMBADA, ARC-Easy, and HellaSwag: C1 effect sizes decrease from open-ended prediction ($d \approx 0.9$, LAMBADA) through ARC-Easy ($d \approx 0.1$--$0.3$) to HellaSwag ($d \approx 0$ under \texttt{acc\_norm}) and binary classification ($d \approx 0$, BoolQ). The gradient broadly tracks the coefficient of variation (CV) of the log-likelihood confidence proxy: LAMBADA ($\text{CV} = 0.75$) $>$ ARC-Easy ($0.54$) $>$ HellaSwag ($0.49$) $>$ BoolQ ($0.22$). BoolQ's high-frequency short completions (``\,yes''/``\,no'') yield elevated baseline log-likelihoods (mean $|\text{loglik}| = 3.04$ vs.\ $0.84$ for LAMBADA) with similar absolute spread (IQR $\approx 0.9$), compressing the relative variation and rendering the confidence margin unable to separate borderline-correct from robustly-correct examples.
595	
596	\paragraph{Interpretation.} The RetNet--HGRN2 anti-correlation may reflect different error modes specific to binary classification: when one architecture's recurrent state resolves a yes/no ambiguity through attention, the other architecture's resolution may be disrupted by the same attention intervention. This pattern warrants further investigation with additional binary classification benchmarks to determine whether it is BoolQ-specific or characteristic of two-choice tasks more broadly.
597	
598	\section{WinoGrande Supplementary Analysis}
599	\label{app:winogrande}
600	
601	WinoGrande ($N = 1{,}267$; reasoning, two-choice coreference resolution) shows high ambiguity ($\alpha \approx 0.41$ at h3-1) but mixed Jaccard significance: 10 of 24 architecture $\times$ attention-ratio pair combinations yield $p < .01$. Mean pairwise Jaccard ($\bar{J}_h = 0.110$, $\bar{J}_u = 0.103$) is comparable to the four main benchmarks, but the elevated null baseline from near-chance accuracy (${\sim}60\%$) reduces statistical power to detect above-chance overlap.
602	
603	\paragraph{Near-chance accuracy.} WinoGrande accuracy across hybrid configurations ranges from 59\% to 62\%, close to the two-choice chance level of 50\%. At near-chance accuracy, a large fraction of examples are borderline---small perturbations (such as adding attention) can flip predictions in either direction, inflating the helped and hurt sets and consequently $\alpha$. This structural property, shared with BoolQ (${\sim}59\%$ accuracy, $\alpha \approx 0.45$), may partially explain the elevated $\alpha$ rather than task-intrinsic multiplicity. PIQA (73\% accuracy, $\alpha = 0.14$) and HellaSwag (60\% normalized accuracy, $\alpha = 0.15$) demonstrate that near-chance accuracy is not the sole driver, but we cannot fully exclude it as a contributing factor for WinoGrande and BoolQ.
604	
605	\begin{table}[ht]
606	\centering
607	\small
608	\caption{WinoGrande predictive multiplicity at 1.3B (h3-1).}
609	\label{tab:winogrande_multiplicity}
610	\resizebox{\columnwidth}{!}{%
611	\begin{tabular}{@{}lcccccc@{}}
612	\toprule
613	 & $N$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & Sig.\ pairs & $\rho_\alpha$ \\
614	\midrule
615	WinoGrande & 1267 & .41 & .110 & .103 & 10/24 & $-0.9$ \\
616	\bottomrule
617	\end{tabular}}
618	\par\vspace{1pt}
619	{\footnotesize $\alpha$ variation across ratios: 0.054 ($> 0.03$ threshold of main benchmarks).}
620	\end{table}
621	
622	\section{340M Per-Example Analysis}\label{app:scale_per_example}
623	
624	\subsection{LAMBADA}
625	
626	At 340M, LAMBADA per-example multiplicity closely matches the 1.3B pattern: $\alpha = 0.313$ (vs.\ 0.307 at 1.3B), with mean pairwise Jaccard $\bar{J} \approx 0.089$ (vs.\ 0.095). Per-example directionality is preserved: HGRN2 shows net positive effects at h3-1 ($+238$ examples), while GDN ($-256$) and RetNet ($-106$) show net negative effects, mirroring the 1.3B profile (HGRN2 $+153$, GDN $-153$, RetNet $-69$).
627	
628	However, aggregate convergence is absent at 340M: $\rho = -0.50$ ($p = .45$), with non-monotonic $\sigma$ across attention ratios ($0.025 \to 0.012 \to 0.018 \to 0.011 \to 0.016$). This contrasts sharply with 1.3B ($\rho = -1.0$, $p = .017$, monotonic $\sigma$ decrease). The decoupling between per-example divergence and aggregate convergence thus manifests differently across scales: at 340M, per-example multiplicity is present but aggregate convergence is not, suggesting that convergence requires sufficient model capacity while multiplicity does not.
629	
630	Within-benchmark $\alpha$ variation across attention ratios is also larger at 340M (0.047, from 0.313 at pure to 0.266 at h3-1) than at 1.3B ($< 0.03$; \S\ref{ssec:per_example}), suggesting that smaller models are more sensitive to the attention ratio in terms of per-example disagreement patterns.
631	
632	\begin{table}[ht]
633	\centering
634	\small
635	\caption{340M vs.\ 1.3B LAMBADA comparison.}
636	\label{tab:scale_comparison}
637	\begin{tabular}{@{}lcc@{}}
638	\toprule
639	 & 340M & 1.3B \\
640	\midrule
641	$\alpha$ (pure) & .313 & .307 \\
642	$\bar{J}$ (h3-1) & .089 & .095 \\
643	$\rho_\sigma$ & $-0.50$ & $-1.0$ \\
644	$p$ & .45 & .017 \\
645	GDN net & $-256$ & $-153$ \\
646	HGRN2 net & $+238$ & $+153$ \\
647	\bottomrule
648	\end{tabular}
649	\end{table}
650	
651	\subsection{Cross-Benchmark Scale Comparison}
652	
653	Table~\ref{tab:340m_multi_bench} extends the scale comparison to all four main benchmarks. Two patterns emerge. First, $\alpha$ is systematically higher at 340M across all benchmarks, with the largest gap on ARC-Easy ($+$8.4pp) and the smallest on LAMBADA ($+$0.6pp). Second, pairwise Jaccard remains stable across scales ($\bar{J}_h = 0.08$--$0.10$ at both scales); three-architecture results are stable across both 340M and 1.3B scales (Jaccard $\approx$ 0.08--0.10), providing indirect support for consistency across these two scales. This suggests that the qualitative pattern of per-example multiplicity---which architectures affect which examples---is consistent across the two scales examined, even as its magnitude increases at smaller scale. Notably, the $\alpha$ inflation does not track accuracy loss: HellaSwag has the largest accuracy gap between scales yet the smallest $\Delta\alpha$ ($+$1.9pp), while ARC-Easy has a smaller accuracy gap but the largest $\Delta\alpha$ ($+$8.4pp), arguing against accuracy as the primary driver of scale-dependent multiplicity.
654	
655	\begin{table}[ht]
656	\centering
657	\small
658	\caption{340M vs.\ 1.3B per-example multiplicity across four benchmarks. $\alpha$: ambiguity at pure-recurrent configuration. Acc: mean accuracy across three architectures at pure-recurrent. $\bar{J}_{h}$/$\bar{J}_{u}$: mean pairwise Jaccard of helped/hurt sets. $\Delta\alpha$: 340M $-$ 1.3B.}
659	\label{tab:340m_multi_bench}
660	\resizebox{\columnwidth}{!}{%
661	\begin{tabular}{lcccccccr}
662	\toprule
663	 & \multicolumn{4}{c}{340M} & \multicolumn{3}{c}{1.3B} & \\
664	\cmidrule(lr){2-5} \cmidrule(lr){6-8}
665	Benchmark & Acc & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & $\Delta\alpha$ \\
666	\midrule
667	PIQA & .663 & .181 & .090 & .085 & .143 & .091 & .094 & $+$.038 \\
668	HellaSwag$^\dagger$ & .420 & .167 & .084 & .083 & .148 & .095 & .085 & $+$.019 \\
669	ARC-Easy & .594 & .289 & .098 & .103 & .205 & .092 & .099 & $+$.084 \\
670	LAMBADA & --- & .313 & .089 & .090 & .307 & .095 & .093 & $+$.006 \\
671	\bottomrule
672	\multicolumn{9}{l}{\footnotesize $^\dagger$\texttt{acc\_norm}. LAMBADA accuracy omitted (evaluated in separate run).}
673	\end{tabular}%
674	}
675	\end{table}
676	
677	Convergence is absent at 340M across all benchmarks (all $|\rho| \leq 0.4$, $p \geq .45$), in contrast to 1.3B where LAMBADA shows monotonic convergence. The absence of convergence at 340M extends beyond LAMBADA to HellaSwag ($\rho = 0.4$, $p = .52$), PIQA ($\rho = 0.3$, $p = .68$), and ARC-Easy ($\rho = -0.1$, $p = .95$).
678	
679	\section{Subsample Sensitivity of \texorpdfstring{$\alpha$}{α}}\label{app:subsample_sensitivity}
680	
681	To assess the reliability of $\alpha$ estimation at different sample sizes, we repeatedly subsample each benchmark (1{,}000 bootstrap replicates, seed 42) and compute the 95\% CI width of $\alpha$.
682	
683	\begin{table}[ht]
684	\centering
685	\small
686	\caption{$\alpha$ estimation stability: 95\% CI width by subsample size.}
687	\label{tab:subsample}
688	\resizebox{\columnwidth}{!}{%
689	\begin{tabular}{@{}lrrrrr@{}}
690	\toprule
691	Benchmark & $n = 100$ & $n = 200$ & $n = 500$ & $n = 1000$ & Full $N$ \\
692	\midrule
693	PIQA & .130 & .095 & .066 & .045 & .034 \\
694	HellaSwag & .140 & .100 & .062 & .044 & .013 \\
695	ARC-Easy & .160 & .105 & .072 & .050 & .032 \\
696	LAMBADA & .180 & .125 & .082 & .057 & .025 \\
697	\bottomrule
698	\end{tabular}}
699	\par\vspace{1pt}
700	{\footnotesize At $n = 100$, CI width (0.13--0.18) spans the entire four-benchmark $\alpha$ range (0.14--0.30), rendering $\alpha$ estimation unreliable. This justifies excluding COPA ($n = 100$) from the per-example analysis.}
701	\end{table}
702	
703	\section{Complementarity Decomposition}\label{app:complementarity}
704	
705	We decompose the three-architecture vote on each example into four categories: unanimous correct (3/3), majority correct (2/3), minority correct (1/3), and unanimous wrong (0/3). This decomposition explains the structural failure of majority vote despite substantial per-example complementarity.
706	
707	Table~\ref{tab:complementarity} reports the decomposition at h3-1 (25\% attention). Majority vote benefits only from 2/3 examples (where the correct answer holds a majority) but is actively harmed by 1/3 examples (where the correct architecture is outvoted). On LAMBADA, HellaSwag, and ARC-Easy, the MV exploitation ratio---the fraction of complementary examples where MV selects correctly---hovers near 51\%, indicating a near-even split between MV-exploitable and MV-hostile disagreements. The oracle, by contrast, exploits both categories, explaining the large oracle--MV gap ($+7$--$14$\,pp).
708	
709	\begin{table}[ht]
710	\centering
711	\small
712	\caption{Complementarity decomposition at 1.3B h3-1. Fractions of total examples in each vote category. MV expl.: fraction of complementary examples where majority vote is correct.}
713	\label{tab:complementarity}
714	\begin{tabular}{@{}lccccr@{}}
715	\toprule
716	Benchmark & 3/3 & 2/3 & 1/3 & 0/3 & MV expl. \\
717	\midrule
718	LAMBADA & .361 & .151 & .145 & .343 & 51.1\% \\
719	HellaSwag & .519 & .078 & .073 & .331 & 51.6\% \\
720	ARC-Easy & .603 & .107 & .103 & .187 & 50.9\% \\
721	BoolQ & .376 & .257 & .197 & .170 & 56.6\% \\
722	\bottomrule
723	\end{tabular}
724	\end{table}
725	
726	This near-50\% exploitation ratio is structurally invariant across attention ratios: on LAMBADA, the ratio ranges from 51.1\% to 54.4\% across all five configurations; on HellaSwag, from 50.3\% to 51.6\%. Attention changes neither the amount nor the structure of cross-architecture complementarity.
727	
728	\section{Seed-Variation Calibration}\label{app:seed_calibration}
729	
730	To contextualize the $3\times$ within- vs.\ cross-architecture Jaccard gap (\S\ref{ssec:decoupling}), we compare against within-seed variation using the Pythia 70M \citep{biderman2023pythia} PolyPythias models \citep{vanderwal2025polypythias}, which provide 9 individually trained seeds of the same architecture.
731	
732	On LAMBADA ($N = 5{,}153$), within-seed mean Jaccard is $\bar{J}_h = 0.273$ (helped) and $\bar{J}_u = 0.393$ (hurt), compared to our cross-architecture reference $J \approx 0.10$. On ARC-Easy ($N = 2{,}376$), within-seed $\bar{J}_h = 0.312$ and $\bar{J}_u = 0.354$, versus cross-architecture $J \approx 0.092$. Within-seed ambiguity is $\alpha = 0.36$ (LAMBADA) and $\alpha = 0.49$ (ARC-Easy), compared to cross-architecture $\alpha = 0.30$ and $0.21$ respectively.
733	
734	Seeds thus produce comparable or higher amounts of per-example disagreement ($\alpha$) but on more overlapping examples (higher $J$). Cross-architecture variation is associated with per-example effects on less overlapping examples (lower $J$), consistent with architecture-associated divergence yielding qualitatively different per-example patterns than seed noise. The within-seed Jaccard is 2.7--4.3$\times$ higher than cross-architecture Jaccard across both benchmarks.
735	
736	Three caveats qualify this comparison. First, scale mismatch: Pythia 70M is $5\times$ smaller than our smallest models (340M); attempts to use Pythia 410M failed repeatedly. Second, architecture family: Pythia is a standard Transformer, not a hybrid recurrent architecture, so this is a cross-family reference point rather than a matched control. Third, accuracy regime: Pythia 70M accuracy (LAMBADA 0.17--0.23, ARC-Easy ${\sim}$0.38) is far below our models (${\sim}$0.50, ${\sim}$0.72), and Jaccard is affected by base rates; the 2.7--4.3$\times$ ratio may differ at accuracy regimes closer to our main experiments. These limitations restrict the comparison to a reference point for seed-variation magnitude rather than definitive evidence for architecture-driven effects.
737	
738	\section{Extended Architecture Validation (Five Architectures)}\label{app:extended_arch}
739	
740	To test whether the low cross-architecture Jaccard pattern generalizes beyond the three primary architectures, we extend the analysis to include two additional architectures from the same model zoo: GLA (Gated Linear Attention) and DeltaNet, yielding ten pairwise comparisons. Both are available only at 340M in the model zoo; all results below use the h3-1 (25\% attention) configuration. This extension validates per-example divergence (not aggregate convergence).
741	
742	\begin{center}
743	\small
744	\captionof{table}{Pairwise Jaccard similarity across five architectures (340M, h3-1). All 40 permutation tests yield $p \leq .002$ ($z = 3.49$--$12.21$).}
745	\label{tab:extended_arch_jaccard}
746	\begin{tabular}{@{}llcc@{}}
747	\toprule
748	Benchmark & Pair & $J_h$ & $J_u$ \\
749	\midrule
750	\multirow{11}{*}{LAMBADA} & GDN--RetNet & .128 & .121 \\
751	 & GDN--HGRN2 & .123 & .083 \\
752	 & GDN--GLA & .124 & .100 \\
753	 & GDN--DeltaNet & .115 & .100 \\
754	 & RetNet--HGRN2 & .108 & .083 \\
755	 & RetNet--GLA & .123 & .107 \\
756	 & RetNet--DeltaNet & .115 & .096 \\
757	 & HGRN2--GLA & .127 & .086 \\
758	 & HGRN2--DeltaNet & .125 & .090 \\
759	 & GLA--DeltaNet & .134 & .081 \\
760	 & \textit{Mean} & \textit{.122} & \textit{.095} \\
761	\midrule
762	\multirow{11}{*}{ARC-Easy} & GDN--RetNet & .089 & .114 \\
763	 & GDN--HGRN2 & .122 & .105 \\
764	 & GDN--GLA & .114 & .106 \\
765	 & GDN--DeltaNet & .084 & .102 \\
766	 & RetNet--HGRN2 & .087 & .115 \\
767	 & RetNet--GLA & .112 & .110 \\
768	 & RetNet--DeltaNet & .138 & .123 \\
769	 & HGRN2--GLA & .098 & .087 \\
770	 & HGRN2--DeltaNet & .109 & .088 \\
771	 & GLA--DeltaNet & .129 & .098 \\
772	 & \textit{Mean} & \textit{.108} & \textit{.105} \\
773	\bottomrule
774	\end{tabular}
775	\end{center}
776	
777	% Figure moved to main text (\S\ref{ssec:robustness})
778	
779	All pairwise Jaccard values remain $\leq 0.14$, consistent with the three-architecture results at 1.3B (Table~\ref{tab:per_example}). The seven new pairs involving GLA and DeltaNet show no systematic difference from the original three pairs (Mann-Whitney $p > .3$ for both helped and hurt), indicating that the low-overlap pattern is not specific to the original architecture triple. A sixth architecture (HGRN; \citealp{qin2023hierarchically}) is also available in the zoo but excluded from the main analysis: its substantially lower baseline accuracy on LAMBADA (0.263 vs.\ 0.32--0.38 for the other five) mechanically inflates helped-set sizes and Jaccard values. All 15 six-architecture permutation tests nonetheless remain significant ($z \geq 2.9$, $p \leq .006$). The same pattern holds on HellaSwag ($N = 10{,}042$) and PIQA ($N = 1{,}838$): all 20 additional pairwise tests yield $p < .01$ with mean $J_{\text{helped}} \leq 0.10$. Full four-benchmark and six-architecture data are included in our code release.
780	
781	\section{Code and Data Availability}
782	\label{app:code_data}
783	
784	All models are from the publicly available model zoo of \citet{wang2025hybrid}. Analysis code and per-example evaluation outputs are available at \url{https://github.com/anonymous-nlp-2026-2/entrainment_gated_ft}.
785	
786	\section{Use of AI Assistants}
787	\label{app:ai-assistants}
788	
789	We used Claude (Anthropic) as an AI coding and writing assistant
790	throughout this work. Specifically:
791	\begin{itemize}
792	    \item \textbf{Code:} drafting experiment scripts, data-processing
793	    pipelines, and analysis utilities; debugging and refactoring.
794	    \item \textbf{Writing:} drafting and revising paper sections,
795	    polishing prose, and reformatting \LaTeX{}.
796	    \item \textbf{Literature:} summarizing related papers to inform
797	    the related-work section.
798	\end{itemize}
799	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bd286a3-723a-45f5-a0ab-37f23981a8c7",
  "isSidechain": true,
  "promptId": "c7608d82-8599-4782-b1a2-f177b4bb14cc",
  "agentId": "a7ca798f294f742d3",
  "type": "user",
  "uuid": "2b5885bd-0fe5-4b6b-b8ab-e33a69dc4e4b",
  "sourceToolAssistantUUID": "4bd286a3-723a-45f5-a0ab-37f23981a8c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T09:10:02.958Z_

<details><summary>↩ Tool result · `toolu_01HgEJvEjAwnPdM1NbceDona`</summary>

```text
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
15	\usepackage{xcolor}
16	\usepackage{caption}
17	\usepackage{enumitem}
18	\setlist[itemize]{itemsep=1pt, parsep=0pt, topsep=2pt}
19	
20	\setlength{\textfloatsep}{6pt plus 1pt minus 1pt}
21	\setlength{\floatsep}{6pt plus 1pt minus 1pt}
22	\setlength{\intextsep}{6pt plus 1pt minus 1pt}
23	\setlength{\abovecaptionskip}{3pt}
24	\setlength{\belowcaptionskip}{0pt}
25	\setlength{\dbltextfloatsep}{6pt plus 1pt minus 1pt}
26	\setlength{\dblfloatsep}{6pt plus 1pt minus 1pt}
27	\setlength{\abovedisplayskip}{4pt plus 1pt minus 1pt}
28	\setlength{\belowdisplayskip}{4pt plus 1pt minus 1pt}
29	\setlength{\parskip}{0pt plus 0.5pt}
30	
31	\title{Aggregate Equivalence $\neq$ Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\begin{abstract}
39	Hybrid linear recurrent architectures that appear interchangeable by aggregate benchmarks can differ on which specific examples they handle correctly. Using a controlled model zoo \citep{wang2025hybrid} (three architectures, five attention ratios, two scales), we decompose per-example effects of adding attention and find structured predictive multiplicity \citep{marx2020predictive}: pairwise overlap of helped and hurt example sets is uniformly low (Jaccard $\approx 0.10$, roughly twice the independence baseline; all $p < .01$ across five architectures). This multiplicity varies by task type or evaluation format ($\alpha = 0.14$--$0.30$) rather than attention ratio. Per-example overlap appears to stabilize at 4\% attention and remains flat across higher ratios, suggesting that minimal attention may establish which examples each architecture affects. \citet{yang2026benchmark} document analogous per-item disagreement (16--66\%) among frontier large language models (LLMs) despite comparable aggregate scores; our within-family design isolates backbone variation from training-regime differences. Confidence margins partially predict affected examples (area under the ROC curve [AUC] 0.70--0.74). Low cross-architecture overlap implies substantial complementarity, though routing-based exploitation remains task-dependent.
40	\end{abstract}
41	
42	\input{sections/introduction}
43	
44	\input{sections/related_work}
45	
46	\input{sections/method}
47	
48	\input{sections/experiments}
49	
50	\input{sections/conclusion}
51	
52	\section*{Limitations}
53	
54	\paragraph{Single training runs.} Each configuration is a single training run; consistency across all 40 architecture--benchmark combinations (all $p < .01$) and a $3\times$ within- vs.\ cross-architecture Jaccard gap (within-seed $J$ is 2.7--4.3$\times$ higher; Appendix~\ref{app:seed_calibration}) mitigate seed confounds but cannot fully resolve them.
55	
56	\paragraph{Format confound.} The confound between task type and evaluation format cannot be fully resolved: LAMBADA is the only free-form benchmark, so its higher $\alpha$ may reflect format differences rather than cognitive demands alone.
57	
58	\paragraph{Coverage.} We examine three primary architectures (plus two extended) from one model zoo, four main benchmarks, and two scale points. Generalization to Mamba, RWKV, other hybrid families, and generation tasks remains open; all four per-example benchmarks use discriminative scoring, so multiplicity under open-ended generation is untested. Results at larger scales (e.g., 7B+) may differ, particularly as attention mechanisms become more expressive with increased capacity.
59	
60	\paragraph{Pre-training only.} All evaluations use pretrained checkpoints without fine-tuning; per-example effects may not persist after task-specific adaptation. All evaluations use greedy decoding (the lm-eval-harness default); sampling strategies may alter per-example agreement patterns.
61	
62	\bibliography{references}
63	
64	\appendix
65	\input{sections/appendix}
66	
67	\end{document}
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "add8c9fd-8b6b-451f-81fc-a3cbd3b7b8ee",
  "isSidechain": true,
  "promptId": "c7608d82-8599-4782-b1a2-f177b4bb14cc",
  "agentId": "a7ca798f294f742d3",
  "type": "user",
  "uuid": "9451cd37-e8f0-4f70-816b-fe4405dbd4d4",
  "sourceToolAssistantUUID": "add8c9fd-8b6b-451f-81fc-a3cbd3b7b8ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-25T09:10:05.845Z_

Now let me search for each appendix label in the main text files. I'll search through all the non-appendix files systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9451cd37-e8f0-4f70-816b-fe4405dbd4d4",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2Uoc81y91RTtPHcqxC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e865d6b3-1596-44bb-931e-ba1ac6a9f489",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JeBAqfVHoWBXNqNRuqGkcK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23814,
      "cache_read_input_tokens": 40411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23814,
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

_source line 8 · 2026-05-25T09:10:09.060Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NvWYsXwPTi4H9Nx86tSDiW`</summary>

```json
{
  "pattern": "app:benchmark_details|app:convergence_detail|app:scale_convergence|app:sensitivity|app:gdn_confound|app:attention_patterns|app:cross_scale|app:per_example_counts|app:normalized_es|app:arceasy|app:jaccard_permutation|app:transformer_entrainment|app:within_arch_stability|app:cross_bench_jaccard|app:continuous_jaccard|app:confidence_margin|app:cm_cross|app:prediction_framework|app:calibration|app:boolq|app:winogrande|app:scale_per_example|app:subsample_sensitivity|app:complementarity|app:seed_calibration|app:extended_arch|app:code_data|app:ai-assistants",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections",
  "output_mode": "content",
  "glob": "introduction.tex|related_work.tex|method.tex|experiments.tex|conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e865d6b3-1596-44bb-931e-ba1ac6a9f489",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2Uoc81y91RTtPHcqxC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f520b05a-e004-4540-9ed4-1ee621b64238",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JeBAqfVHoWBXNqNRuqGkcK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23814,
      "cache_read_input_tokens": 40411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23814,
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

_source line 9 · 2026-05-25T09:10:09.090Z_

<details><summary>↩ Tool result · `toolu_01NvWYsXwPTi4H9Nx86tSDiW`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f520b05a-e004-4540-9ed4-1ee621b64238",
  "isSidechain": true,
  "promptId": "c7608d82-8599-4782-b1a2-f177b4bb14cc",
  "agentId": "a7ca798f294f742d3",
  "type": "user",
  "uuid": "07de4fac-4fc1-47ea-af72-3d5c8e6a1c80",
  "sourceToolAssistantUUID": "f520b05a-e004-4540-9ed4-1ee621b64238",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T09:10:09.955Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01N18gDFi6Rh8Yv4RB8FSsT7`</summary>

```json
{
  "pattern": "app:benchmark_details|app:convergence_detail|app:scale_convergence|app:sensitivity|app:gdn_confound|app:attention_patterns|app:cross_scale|app:per_example_counts|app:normalized_es|app:arceasy|app:jaccard_permutation|app:transformer_entrainment|app:within_arch_stability|app:cross_bench_jaccard|app:continuous_jaccard|app:confidence_margin|app:cm_cross|app:prediction_framework|app:calibration|app:boolq|app:winogrande|app:scale_per_example|app:subsample_sensitivity|app:complementarity|app:seed_calibration|app:extended_arch|app:code_data|app:ai-assistants",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper",
  "output_mode": "content",
  "glob": "main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07de4fac-4fc1-47ea-af72-3d5c8e6a1c80",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2Uoc81y91RTtPHcqxC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "214b9b81-5407-4696-bb72-616f75781695",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JeBAqfVHoWBXNqNRuqGkcK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23814,
      "cache_read_input_tokens": 40411,
      "output_tokens": 681,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23814
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 681,
          "cache_read_input_tokens": 40411,
          "cache_creation_input_tokens": 23814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23814,
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

_source line 11 · 2026-05-25T09:10:09.977Z_

<details><summary>↩ Tool result · `toolu_01N18gDFi6Rh8Yv4RB8FSsT7`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex:54:\paragraph{Single training runs.} Each configuration is a single training run; consistency across all 40 architecture--benchmark combinations (all $p < .01$) and a $3\times$ within- vs.\ cross-architecture Jaccard gap (within-seed $J$ is 2.7--4.3$\times$ higher; Appendix~\ref{app:seed_calibration}) mitigate seed confounds but cannot fully resolve them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "214b9b81-5407-4696-bb72-616f75781695",
  "isSidechain": true,
  "promptId": "c7608d82-8599-4782-b1a2-f177b4bb14cc",
  "agentId": "a7ca798f294f742d3",
  "type": "user",
  "uuid": "d4707205-1236-4b95-850f-78d54f402229",
  "sourceToolAssistantUUID": "214b9b81-5407-4696-bb72-616f75781695",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-25T09:10:11.803Z_

Let me read the individual non-appendix files and search more carefully:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4707205-1236-4b95-850f-78d54f402229",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2VKVDCMZCKyzTc87AV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df44e8c2-2a8a-41ed-afcd-ff12901c7116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011hKYAPx6vwk81PptBTToZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 64225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 885,
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

_source line 13 · 2026-05-25T09:10:12.071Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DMAeZybaoE44m8R7AYyxfp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df44e8c2-2a8a-41ed-afcd-ff12901c7116",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2VKVDCMZCKyzTc87AV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "825f4373-1495-446f-96f5-75b26c5ee6cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011hKYAPx6vwk81PptBTToZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 64225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 885,
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

_source line 14 · 2026-05-25T09:10:12.082Z_

<details><summary>↩ Tool result · `toolu_01DMAeZybaoE44m8R7AYyxfp`</summary>

```text
1	\section{Introduction}
2	
3	Hybrid linear recurrent architectures---including GatedDeltaNet (GDN), RetNet, HGRN2, Gated Linear Attention (GLA), and DeltaNet---achieve aggregate benchmark scores within 1--2 points of each other at matched parameter budgets, yet they can differ on up to 90\% of the individual examples they affect. This per-example divergence is invisible in aggregate metrics: architectures that score similarly reach that score by gaining and losing on different inputs, and the choice of backbone carries hidden consequences for which specific examples a deployed system handles correctly.
4	
5	\begin{figure*}[t]
6	\centering
7	\begin{minipage}[t]{0.56\textwidth}
8	\centering
9	\includegraphics[width=\textwidth]{figures/fig1_decoupling_hero.pdf}
10	\end{minipage}%
11	\hfill
12	\begin{minipage}[t]{0.42\textwidth}
13	\centering
14	\includegraphics[width=\textwidth]{figures/fig4_jaccard_saturation.pdf}
15	\end{minipage}
16	\caption{Per-example overlap appears stable from minimal attention across benchmarks. (a,\,b) LAMBADA: cross-architecture $\sigma$ shows a non-significant decreasing trend at 1.3B (solid; Bonferroni-adjusted $p = .170$) but partially rebounds at 340M (dashed), while pairwise Jaccard of helped/hurt sets appears stable from 4\% attention onward. (c) This pattern holds across all four main benchmarks: mean pairwise $\bar{J}$ remains flat across attention ratios (all $\rho \leq 0.80$, $p \geq .333$). Shaded bands are illustrative ($n = 3$).}
17	\label{fig:decoupling}
18	\end{figure*}
19	
20	This tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba}, Griffin \citep{de2024griffin}, RWKV-6 \citep{peng2024eagle}, and RecurrentGemma \citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
21	
22	Prior work on predictive multiplicity \citep{marx2020predictive} and underspecification \citep{damour2022underspecification,mccoy2020berts} documents this risk for seed variation within a single architecture, but whether it extends to architectural variation in hybrid recurrent models remains open. If architectures that score similarly in aggregate behave differently on individual inputs, the backbone choice carries hidden consequences for deployment reliability and ensemble construction.
23	
24	We present the first controlled within-family per-example analysis of how attention affects cross-architecture agreement in hybrid recurrent models. Using the model zoo of \citet{wang2025hybrid}, we compare three architectures---GatedDeltaNet (gated delta rules), RetNet (multi-scale exponential decay), and HGRN2 (gated state expansion)---at five attention ratios (0--25\%) and two scales (340M, 1.3B). We evaluate all 30 configurations on 10 benchmarks spanning retrieval, comprehension, reasoning, and mixed categories. On four benchmarks (LAMBADA, $N = 5{,}153$; HellaSwag, $N = 10{,}042$; PIQA, $N = 1{,}838$; ARC-Easy, $N = 2{,}376$) we conduct per-example decompositions, classifying each example as helped, hurt, or unchanged when attention is added, and measure cross-architecture overlap via Jaccard similarity. Figure~\ref{fig:decoupling} previews our central finding: architectures that appear equivalent by aggregate benchmarks diverge systematically at the per-example level, and this divergence is established by minimal attention.
25	
26	Our central finding is that architectural variation produces structured predictive multiplicity whose magnitude depends on task type, not attention ratio. The ambiguity $\alpha$ \citep{marx2020predictive} ranges from 0.14 (PIQA) to 0.30 (LAMBADA), varies $2\times$ across task types but only 0.03 within each benchmark across attention ratios; pairwise Jaccard remains uniformly low ($\leq 0.10$, all $p < .01$ across all ten five-architecture pairs). A supporting observation is that per-example overlap appears to stabilize at the first attention level (4\%) and remains flat at higher ratios---even on LAMBADA, where aggregate variance shows a non-significant decreasing trend ($\rho = -1.0$, Bonferroni-adjusted $p = .170$; at 1.3B only), per-example Jaccard does not change (\S\ref{ssec:decoupling}).
27	
28	Our contributions are as follows:
29	\begin{itemize}
30	    \item Architectural variation in hybrid recurrent models---controlled within a single model zoo sharing training data and hyperparameters---produces structured predictive multiplicity whose magnitude varies by task type (or evaluation format) rather than attention ratio (\S\ref{ssec:per_example}). Five-architecture validation confirms the pattern (\S\ref{ssec:robustness}; Appendix~\ref{app:extended_arch}).
31	    \item Per-example overlap appears to stabilize at the first attention level (4\%) across all four benchmarks: minimal attention may establish which examples each architecture affects, with no observed homogenization at higher ratios ($n = 5$ ratios; \S\ref{ssec:decoupling}).
32	    \item Pure-model confidence margins partially predict which examples attention will affect (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\% across architectures---a second dimension of multiplicity beyond per-example disagreement (\S\ref{ssec:per_example}; Appendix~\ref{app:prediction_framework}).
33	\end{itemize}
34	\noindent Code and data are available at \url{https://github.com/anonymous-nlp-2026-2/entrainment_gated_ft}.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "825f4373-1495-446f-96f5-75b26c5ee6cb",
  "isSidechain": true,
  "promptId": "c7608d82-8599-4782-b1a2-f177b4bb14cc",
  "agentId": "a7ca798f294f742d3",
  "type": "user",
  "uuid": "9d7fd615-108c-4028-b76b-26891075923e",
  "sourceToolAssistantUUID": "825f4373-1495-446f-96f5-75b26c5ee6cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T09:10:12.245Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QmzpHJUcvmc22TpjTvWERY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d7fd615-108c-4028-b76b-26891075923e",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2VKVDCMZCKyzTc87AV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bcbc023c-6747-481c-bef0-012521f4e422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011hKYAPx6vwk81PptBTToZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 64225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 885,
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

_source line 16 · 2026-05-25T09:10:12.255Z_

<details><summary>↩ Tool result · `toolu_01QmzpHJUcvmc22TpjTvWERY`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Hybrid Recurrent Architectures.}
4	The design space for combining attention with recurrence spans layer-level interleaving \citep[Jamba;][]{lieber2024jamba}, local attention pairing \citep[Griffin, RecurrentGemma;][]{de2024griffin,botev2024recurrentgemma}, matrix-valued recurrence \citep[RWKV-6;][]{peng2024eagle}, within-head mixing \citep[Hymba;][]{dong2024hymba}, and unbounded-context hybrid SSMs \citep[Samba;][]{ren2024samba}. H3 \citep{fu2023hungry} and Hyena \citep{poli2023hyena} establish early design points in the hybrid space with gated convolutions and subquadratic operators. Mamba-2 \citep{dao2024mamba2} establishes a duality between structured state spaces and attention; Mamba-3 \citep{lahoti2026mamba3} extends the design further, while \citet{ali2025hidden} reveal implicit attention within Mamba. Comparative evaluations confirm that hybrids outperform pure Transformers and SSMs at scale \citep{waleffe2024empirical}, and that even one attention layer enables content-based routing \citep{basu2026routing}. Recent theoretical work establishes a provable expressiveness hierarchy between hybrid and pure linear attention \citep{ye2026provable}, providing formal grounding for the architectural differences we characterize at the per-example level. \citet{wang2025hybrid} provide the controlled model zoo we use, holding training conditions constant while varying architecture and attention ratio.
5	
6	\paragraph{Linear Recurrent Models.}
7	Our three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \citep{yang2024gateddeltanet} combines gated updates with delta rules. These descend from S4 \citep{gu2022s4} and Mamba \citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, respectively, and connect to linear attention \citep{katharopoulos2020transformers} through the state-space--attention duality of Mamba-2.
8	
9	\paragraph{Underspecification and Predictive Multiplicity.}
10	\citet{damour2022underspecification} formalized underspecification---equivalent aggregate performance masking per-prediction divergence---with NLP instances including seed-dependent BERT disagreement \citep{mccoy2020berts,sellam2022multiberts}. \citet{marx2020predictive} introduced predictive multiplicity, showing that near-optimal models produce conflicting per-example predictions; extensions address probabilistic settings \citep{watson2023predictive}, Rashomon capacity \citep{hsu2022rashomon}, and reconciliation \citep{du2025reconciling,haghighat2026resolving}. These studies attribute divergence to initialization noise within a single architecture; Rashomon-set analyses \citep{fisher2019all,semenova2022existence} and weight-space interpolation \citep{wortsman2022model} operate within this scope. We show that changing the recurrent backbone---a qualitatively different source of variation---produces per-example multiplicity that varies by task type. Our routing approach relates to selective prediction \citep{geifman2017selective} and ensemble selection \citep{caruana2004ensemble}, though we select among architecturally distinct models. \citet{yang2026benchmark} demonstrate analogous per-item disagreement (16--66\%) among frontier LLMs; our within-family design isolates backbone variation from training-regime differences.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcbc023c-6747-481c-bef0-012521f4e422",
  "isSidechain": true,
  "promptId": "c7608d82-8599-4782-b1a2-f177b4bb14cc",
  "agentId": "a7ca798f294f742d3",
  "type": "user",
  "uuid": "685d0dce-ed5e-4bab-a2f0-33cce0b1e1ed",
  "sourceToolAssistantUUID": "bcbc023c-6747-481c-bef0-012521f4e422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T09:10:12.500Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MSmnS1fgvbxToE7Vxy3b1t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "685d0dce-ed5e-4bab-a2f0-33cce0b1e1ed",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2VKVDCMZCKyzTc87AV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1c99ba6b-5b49-40f2-aa5c-e7cc1c99b18e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011hKYAPx6vwk81PptBTToZM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 885,
      "cache_read_input_tokens": 64225,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 885
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 260,
          "cache_read_input_tokens": 64225,
          "cache_creation_input_tokens": 885,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 885,
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

_source line 18 · 2026-05-25T09:10:12.518Z_

<details><summary>↩ Tool result · `toolu_01MSmnS1fgvbxToE7Vxy3b1t`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	We describe the model configurations, evaluation benchmarks, and analytical framework used to measure how attention affects cross-architecture agreement at both aggregate and per-example levels.
4	
5	\begin{table}[t]
6	\centering
7	\small
8	\caption{Model zoo summary \citep{wang2025hybrid}. All configurations share training data, tokenizer, and hyperparameters; they differ only in backbone and attention ratio.}
9	\label{tab:model_zoo}
10	\begin{tabular}{@{}lll@{}}
11	\toprule
12	Architecture & Recurrence mechanism & Scales \\
13	\midrule
14	GatedDeltaNet & Gated delta rules & 340M, 1.3B \\
15	RetNet & Multi-scale exp.\ decay & 340M, 1.3B \\
16	HGRN2 & Gated state expansion & 340M, 1.3B \\
17	\midrule
18	\multicolumn{3}{@{}l@{}}{\footnotesize Attention ratios: 0\%, 4\%, 7.7\%, 14.3\%, 25\%} \\
19	\multicolumn{3}{@{}l@{}}{\footnotesize Extended (340M only): +GLA, +DeltaNet} \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	\subsection{Model Zoo}\label{ssec:model_zoo}
25	
26	We use the pretrained model zoo of \citet{wang2025hybrid} (Table~\ref{tab:model_zoo}), which provides controlled comparisons: GatedDeltaNet \citep{yang2024gateddeltanet}, RetNet \citep{sun2023retnet}, and HGRN2 \citep{qin2024hgrn2} at five attention ratios and two scales. The GDN 1.3B h3-1 configuration uses 16 attention heads vs.\ 32 for RetNet and HGRN2 (\S\ref{ssec:robustness}). We adopt the h$k$-1 notation: h3-1 = 25\% attention, h6-1 = 14.3\%, h12-1 = 7.7\%, h24-1 = 4\%. Within each scale, all models share identical training data, tokenizer, and hyperparameters, isolating architecture and attention configuration. The zoo also includes a Transformer baseline at both scales.
27	
28	\subsection{Task Taxonomy}\label{ssec:task_taxonomy}
29	
30	We evaluate on 10 benchmarks grouped into four categories defined by the primary cognitive demand of each task. This taxonomy (informal; not pre-registered) was fixed prior to analysis following standard categorizations in the evaluation literature \citep{arora2024zoology} and is treated as hypothesis-generating rather than confirmatory (see Appendix~\ref{app:benchmark_details} for the confirmatory/exploratory split), not derived post hoc from observed results. The categories test whether the effect of attention on cross-architecture variance depends on task type.
31	
32	\begin{itemize}
33	    \item \textbf{Retrieval}: LAMBADA \citep{paperno2016lambada}, which requires predicting a final word from long-range context without reasoning or world knowledge.
34	    \item \textbf{Comprehension}: Boolean Questions (BoolQ), a reading comprehension task with yes/no answers.
35	    \item \textbf{Reasoning}: HellaSwag, AI2 Reasoning Challenge (ARC-Challenge; \citealt{clark2018arc}), WinoGrande, and Physical Intuition Question Answering (PIQA). Choice of Plausible Alternatives (COPA; $n = 100$) is supplementary; its small sample renders $\alpha$ unreliable (Appendix~\ref{app:subsample_sensitivity}).
36	    \item \textbf{Mixed}: ARC-Easy, Massive Multitask Language Understanding (MMLU), SciQ, and XStoryCloze, which combine retrieval, comprehension, and reasoning demands.
37	\end{itemize}
38	
39	LAMBADA is the only free-form generation benchmark in our evaluation; all others use multiple-choice scoring. Its higher $\alpha$ (0.30 vs.\ 0.14--0.21 for multiple-choice tasks) may partly reflect the larger answer space inherent to open-ended prediction, and the multiple-choice format may mechanically constrain per-example divergence by limiting the number of distinct error patterns. We cannot fully disentangle task type from evaluation format with the present benchmarks. However, within multiple-choice tasks, format (two-way vs.\ four-way) does not predict $\alpha$ (\S\ref{ssec:per_example}), suggesting that format alone does not drive the observed variation.
40	
41	All evaluations use lm-evaluation-harness v0.4.x \citep{gao2024lmeval} with default prompts and greedy decoding; accuracy serves as the primary metric for all benchmarks. Bootstrap analyses use random seed 42 throughout.
42	
43	\begin{figure}[t]
44	\centering
45	\includegraphics[width=\columnwidth]{figures/fig_method_overview.pdf}
46	\caption{Experimental framework. For each architecture, we compare the pure-recurrent baseline against its hybrid (+attention) variant, classifying every evaluation example as helped, hurt, or unchanged. Cross-architecture overlap of these per-example effect sets is measured via pairwise Jaccard similarity ($J \approx 0.10$), revealing architecture-specific sensitivity patterns.}
47	\label{fig:method_overview}
48	\end{figure}
49	
50	\subsection{Convergence Metrics}\label{ssec:convergence_metrics}
51	
52	We quantify cross-architecture agreement as a function of attention ratio. For each benchmark and attention ratio, we compute the cross-architecture standard deviation $\sigma$ over the three architectures' accuracy scores. To measure the relationship between attention and convergence, we compute the Spearman rank correlation $\rho$ between attention ratio rank and $\sigma$ across the five attention configurations ($n = 5$). A negative $\rho$ indicates that higher attention ratios are associated with lower cross-architecture variance.
53	
54	We also report the convergence ratio $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$, defined as the standard deviation under the pure-recurrent configuration divided by that under the highest attention ratio (25\%). Values greater than 1 indicate that higher attention ratios are associated with lower cross-architecture variance.
55	
56	\subsection{Per-Example Decomposition}\label{ssec:per_example_decomposition}
57	
58	We decompose performance changes at the individual-example level on four benchmarks spanning three task categories: LAMBADA (5{,}153 examples; retrieval), HellaSwag (10{,}042; reasoning), PIQA (1{,}838; reasoning, two-choice), and ARC-Easy (2{,}376; mixed). HellaSwag uses normalized accuracy (acc\_norm) as the per-example correctness criterion. Supplementary analyses on BoolQ (3{,}270) and WinoGrande (1{,}267) appear in Appendix~\ref{app:boolq} and \ref{app:winogrande}. For each architecture, we compare the pure-recurrent baseline against its h3-1 hybrid (25\% attention), which maximizes the recurrent--hybrid contrast; \S\ref{ssec:per_example} confirms that $\alpha$ is stable across intermediate ratios (variation $< 0.03$). Each example is classified as:
59	
60	\begin{itemize}
61	    \item \textbf{Helped}: correct in the hybrid but incorrect in the pure model.
62	    \item \textbf{Hurt}: correct in the pure model but incorrect in the hybrid.
63	    \item \textbf{Unchanged}: both models agree (both correct or both incorrect).
64	\end{itemize}
65	
66	The net effect for each architecture is $|\text{helped}| - |\text{hurt}|$. A positive net effect means more examples transition to correct than to incorrect when attention is added; a negative net effect means the opposite.
67	
68	To measure cross-architecture overlap, we compute the pairwise Jaccard similarity $J = |A \cap B| / |A \cup B|$ between the helped sets of two architectures and, separately, between their hurt sets. $J = 1$ indicates identical sets; $J = 0$ indicates no overlap. On $K$-choice tasks, binarization collapses $K{-}1$ wrong answers into a single ``incorrect'' category, potentially counting architectures as agreeing (both wrong) when they select different wrong answers. This conservative bias strengthens the multiplicity claim: true divergence may exceed what binary Jaccard captures. Appendix~\ref{app:continuous_jaccard} confirms robustness under continuous Jaccard similarity.
69	
70	\subsection{Statistical Methods}\label{ssec:statistical_methods}
71	
72	All tests are two-tailed. Spearman $\rho$ uses exact permutation tests ($5! = 120$ permutations); with $n = 5$, only $|\rho| = 1.0$ achieves $p < .05$ ($p = .017$), so all Spearman-based inferences are descriptive and exploratory. Bonferroni correction spans all 10 benchmarks (adjusted threshold $\alpha / 10 = 0.005$). Bootstrap 95\% bias-corrected and accelerated (BCa) confidence intervals use 10{,}000 resamples; with $n = 3$ architectures, these are heuristic indicators of effect direction. Within-architecture comparisons use Mann-Whitney U; cross-architecture comparisons use Kruskal-Wallis. Attention weight analysis extracts per-layer cosine similarity and Shannon entropy via forward hooks (Appendix~\ref{app:attention_patterns}). The permutation null does not condition on item difficulty; if difficulty-driven correlations inflate observed Jaccard while permutation destroys this structure, the test may be anti-conservative. However, the ${\sim}2.5\times$ observed-to-null ratio (all $z > 5.9$) provides substantial margin against this bias.
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c99ba6b-5b49-40f2-aa5c-e7cc1c99b18e",
  "isSidechain": true,
  "promptId": "c7608d82-8599-4782-b1a2-f177b4bb14cc",
  "agentId": "a7ca798f294f742d3",
  "type": "user",
  "uuid": "064172ed-427b-42f8-82f8-eef7f2eeadb3",
  "sourceToolAssistantUUID": "1c99ba6b-5b49-40f2-aa5c-e7cc1c99b18e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-25T09:10:15.788Z_

Now let me read the experiments and conclusion sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "064172ed-427b-42f8-82f8-eef7f2eeadb3",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2VWRHgBCJ5yWkSgPBm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1d1fafcf-aa25-48e3-bfa8-c3c095542588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lufipk4k1gvKYK2pbhCYL7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5614,
      "cache_read_input_tokens": 65110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5614,
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

_source line 20 · 2026-05-25T09:10:20.848Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VCyFhLfo326Yg4Jigvjx5X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d1fafcf-aa25-48e3-bfa8-c3c095542588",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2VWRHgBCJ5yWkSgPBm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6ff2ceed-c4f8-4f2c-b43a-17ca32f8e23c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lufipk4k1gvKYK2pbhCYL7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5614,
      "cache_read_input_tokens": 65110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5614,
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

_source line 21 · 2026-05-25T09:10:20.858Z_

<details><summary>↩ Tool result · `toolu_01VCyFhLfo326Yg4Jigvjx5X`</summary>

```text
1	\section{Experiments}\label{sec:experiments}
2	
3	Using the model zoo of \citet{wang2025hybrid} (\S\ref{ssec:model_zoo}), we evaluate all 30 configurations on 10 benchmarks plus supplementary COPA ($n = 100$) at 1.3B scale unless noted. Results at 340M appear in scale analyses. Recall: h$k$-1 denotes one attention layer per $k{+}1$ layers; h3-1 = 25\% attention.
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\columnwidth]{figures/fig_per_example_bars.pdf}
8	\caption{Per-example effects of adding attention (pure $\to$ h3-1) on LAMBADA at 1.3B scale. Helped: correct only in the hybrid; hurt: correct only in the pure model. HGRN2 is the only architecture with a net positive effect. Despite comparable magnitudes, these sets overlap minimally across architectures ($\bar{J} \leq 0.10$, all $p < .0001$).}
9	\label{fig:per_example_bars}
10	\end{figure}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Cross-architecture variance trends across benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and cross-architecture standard deviation $\sigma$ across five configurations. $p$: exact permutation test (two-tailed, 120 permutations). $\sigma$ values reported $\times 10^{2}$ (accuracy percentage points). Ratio: $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$. \textbf{Bold}: only benchmark with $\rho = -1.0$. HellaSwag evaluated using normalized accuracy (acc\_norm), the standard metric for this benchmark.}
15	\label{tab:convergence}
16	\begin{tabular}{llrrrrr}
17	\toprule
18	Benchmark & Category & $\rho$ & $p$ & $\sigma_{\text{pure}}$ & $\sigma_{\text{h3-1}}$ & Ratio \\
19	\midrule
20	\textbf{LAMBADA$^{\ddagger}$} & \textbf{Retrieval} & $\mathbf{-1.0}$ & \textbf{.017} & \textbf{2.41} & \textbf{0.49} & \textbf{4.87} \\
21	\quad\emph{(excl.\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\
22	BoolQ & Comprehension & $0.2$ & .783 & 1.63 & 2.36 & 0.69 \\
23	ARC-C & Reasoning & $0.6$ & .350 & 0.96 & 1.32 & 0.72 \\
24	HellaSwag & Reasoning & $0.3$ & .683 & 1.17 & 1.18 & 0.99 \\
25	PIQA & Reasoning & $-0.5$ & .450 & 0.54 & 0.34 & 1.59 \\
26	WinoGrande & Reasoning & $0.1$ & .950 & 0.67 & 0.78 & 0.86 \\
27	ARC-E & Mixed & $-0.7$ & .233 & 1.00 & 0.13 & 7.70 \\
28	MMLU & Mixed & $-0.7$ & .233 & 0.92 & 0.41 & 2.27 \\
29	SciQ & Mixed & $0.1$ & .950 & 0.87 & 0.74 & 1.19 \\
30	XStoryCloze & Mixed & $-0.6$ & .350 & 0.82 & 0.55 & 1.49 \\
31	\midrule
32	COPA$^{\dagger}$ & Reasoning & $-0.67$ & .267 & 2.63 & 0.47 & 5.57 \\
33	\bottomrule
34	\multicolumn{7}{l}{\footnotesize $^{\dagger}$Supplementary ($n = 100$); excluded from multiple comparison correction.} \\
35	\multicolumn{7}{l}{\footnotesize $^{\ddagger}$GDN h3-1 uses 16 attention heads; all other configurations use 32 (\S\ref{ssec:robustness}).} \\
36	\multicolumn{7}{@{}p{\textwidth}@{}}{\footnotesize Bonferroni-adjusted $p = .170$. \textbf{Power: only $|\rho| = 1.0$ achieves $p < .05$ at $n = 5$.} Excl.\ GDN reverses MMLU $\rho$ to $+0.6$ (\S\ref{ssec:robustness}).}
37	\end{tabular}
38	\vspace{-4pt}
39	\end{table*}
40	
41	\subsection{Per-Example Divergence}\label{ssec:per_example}
42	
43	Do architectures converge by improving on the same examples? We compare each architecture's pure-recurrent baseline against its h3-1 hybrid on 5{,}153 LAMBADA examples, classifying each as helped, hurt, or unchanged. Although the decomposition is binary, it captures genuine separation in the continuous confidence space (Cohen's $d = 0.73$--$0.92$ between helped and hurt on LAMBADA; cross-benchmark details in Appendix~\ref{app:cm_cross}). Binarization discards confidence magnitude, so we supplement with continuous confidence margin analysis (Appendix~\ref{app:confidence_margin}) and verify that low Jaccard persists under continuous thresholds (Appendix~\ref{app:continuous_jaccard}).
44	
45	Each architecture displays a distinct profile of per-example changes (Figure~\ref{fig:per_example_bars}). GDN loses a net 153 examples (462 helped, 615 hurt), RetNet loses 69 (426/495), and HGRN2 gains 153 (548/395; full counts in Appendix~\ref{app:per_example_counts}). HGRN2 is the only architecture for which adding attention yields a net per-example benefit. Pairwise Jaccard similarity is low: mean $\bar{J} \leq 0.10$, indicating ${\sim}90$\% non-overlap. Overlap significantly exceeds the independence baseline ($J_{\text{null}} \approx 0.05$, all $z > 5.9$, $p < .0001$; Appendix~\ref{app:jaccard_permutation}), plausibly reflecting shared sensitivity to example difficulty. Normalizing by $J_{\max}$, observed overlap reaches only 6--7\% of the achievable range above chance (Appendix~\ref{app:normalized_es}), confirming that low Jaccard cannot be attributed to set-size constraints.
46	
47	\begin{figure}[t]
48	\centering
49	\includegraphics[width=\columnwidth]{figures/fig3_alpha_routing.pdf}
50	\caption{(a) Per-example ambiguity $\alpha$ varies $2\times$ across task types. (b) Confidence-based routing gains track $\alpha$: effective when multiplicity is high (LAMBADA) but counterproductive when low (PIQA). 1.3B, h3-1.}
51	\label{fig:alpha_routing}
52	\end{figure}
53	
54	\paragraph{Confidence margin predictor.} Pure-model confidence on the target token predicts which examples will be affected (AUC 0.70--0.74, a non-parametric measure equivalent to Mann-Whitney $U$; Appendix~\ref{app:confidence_margin}): rescue thresholds are architecture-invariant (1\% spread) but disruption thresholds vary 47\%, explaining cross-architecture Jaccard divergence (Appendix~\ref{app:prediction_framework}). Calibration differences account for less than half the threshold spread (Appendix~\ref{app:calibration}). The rescue pattern generalizes across three benchmarks ($d = 0.13$--$0.60$; Appendix~\ref{app:cm_cross}); disruption is weaker on reasoning tasks (Appendix~\ref{app:boolq}). This structured disagreement constitutes predictive multiplicity \citep{marx2020predictive} under architectural variation.
55	
56	\paragraph{Confidence-based routing.} As an illustrative case study, the rescue-threshold asymmetry suggests a routing strategy: select the architecture whose pure-model confidence best predicts successful rescue. On LAMBADA, this outperforms majority vote by $+5.3$\,pp (SD $= 0.4$\,pp, 10 cross-validated splits), extracting 36\% of the oracle gap (oracle = 65.5\%; Appendix~\ref{app:complementarity}). On ARC-Easy, gains are modest ($+1.0$\,pp, SD $= 0.5$\,pp); on HellaSwag, routing provides no benefit ($-0.02$\,pp, $p = .89$); on PIQA, it is significantly negative ($-0.6$\,pp, $p = .006$). Routing works when multiplicity is high ($\alpha = 0.30$, LAMBADA) and a clear rescue-threshold signal exists, but is counterproductive when multiplicity is low ($\alpha = 0.14$, PIQA). A natural comparison---average-logits ensemble---is left to future work as it requires simultaneous inference across all architectures.
57	
58	\paragraph{Multiplicity variation.} Extending to HellaSwag ($N = 10{,}042$) and PIQA ($N = 1{,}838$) reveals that predictive multiplicity varies systematically across tasks (Table~\ref{tab:multiplicity}). The ambiguity $\alpha$ \citep{marx2020predictive} ranges from 0.14 (PIQA) through 0.15 (HellaSwag) and 0.21 (ARC-Easy; Appendix~\ref{app:arceasy}) to 0.30 (LAMBADA). Format does not drive this ordering: HellaSwag (four-way) and PIQA (two-choice) produce nearly identical $\alpha$ despite different answer-space sizes, and $\alpha$ does not correlate with task accuracy ($\rho = -0.60$, $p = .24$). This within-multiple-choice invariance suggests that per-example multiplicity is associated with the cognitive demands of the task rather than the mechanical constraints of the evaluation format, though the confound between task type and format cannot be fully resolved with the present benchmarks (Limitations). Bootstrap 95\% CIs confirm the ordering (all non-overlapping except PIQA--HellaSwag; Table~\ref{tab:arceasy_ambiguity}). Pairwise Jaccard remains uniformly low ($\bar{J} \leq 0.10$, all $p < .01$ across four benchmarks), indicating that architectures affect different examples regardless of how many are affected. Within each benchmark, $\alpha$ is stable across attention ratios (variation $< 0.03$) but differs $2\times$ across task types (or evaluation formats), confirming that multiplicity magnitude depends on task, not attention ratio \citep[cf.][]{gorbett2026crossmodel}.
59	
60	\begin{table}[t]
61	\centering
62	\small
63	\caption{Predictive multiplicity at 1.3B. $\alpha$: ambiguity at h3-1 \citep{marx2020predictive}. $\bar{J}$: mean pairwise Jaccard of helped~(h) and hurt~(u) sets, averaged across four hybrid attention ratios and three architecture pairs. $\rho_\alpha$: Spearman $\rho$ between attention ratio and $\alpha$. Benchmarks ordered by $\alpha$.}
64	\label{tab:multiplicity}
65	\begin{tabular}{@{}lrcccc@{}}
66	\toprule
67	 & $N$ & $\alpha$ & $\bar{J}_{h}$ & $\bar{J}_{u}$ & $\rho_\alpha$ \\
68	\midrule
69	PIQA & 1838 & .14 & .091 & .094 & $0.0$ \\
70	HellaSwag & 10042 & .15 & .095 & .085 & $0.1$ \\
71	ARC-Easy & 2376 & .21 & .092 & .099 & $-0.2$ \\
72	LAMBADA & 5153 & .30 & .096 & .091 & $-0.6$ \\
73	\bottomrule
74	\end{tabular}
75	\par\vspace{-2pt}
76	{\footnotesize Within-benchmark $\alpha$ variation $< 0.03$ across ratios. BoolQ, WinoGrande: Appendix~\ref{app:boolq}, \ref{app:winogrande}.}
77	\end{table}
78	
79	\subsection{Per-Example Overlap Appears Stable from Minimal Attention}\label{ssec:decoupling}
80	
81	Does adding more attention change \emph{which} examples each architecture affects? Pairwise Jaccard appears to stabilize at the first attention level (4\%; $\bar{J} \approx 0.095$) and remains flat across all higher ratios (Figure~\ref{fig:decoupling}b), suggesting that minimal attention may suffice to establish the per-example divergence pattern, though the small number of ratios ($n = 5$) limits statistical confirmation. As background, LAMBADA's aggregate cross-architecture $\sigma$ shows a non-significant decreasing trend ($\rho = -1.0$, Bonferroni-adjusted $p = .170$; excluding GDN: $\rho = -0.7$, $p = .233$; MMLU reverses to $\rho = +0.6$ when excluding GDN; observed at 1.3B, absent at 340M; Table~\ref{tab:convergence}, Figure~\ref{fig:task_specificity}). No other benchmark shows a comparable aggregate pattern ($n = 5$; negligible power for $|\rho| < 1.0$).
82	
83	\begin{figure}[t]
84	\centering
85	\includegraphics[width=\columnwidth]{figures/fig2_task_specificity.pdf}
86	\caption{Spearman $\rho$ between attention ratio and cross-architecture $\sigma$ for each benchmark at 1.3B scale. LAMBADA ($\rho = -1.0$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic) is the only benchmark with a negative correlation whose confidence interval excludes zero. Benchmarks are grouped by task category. Bootstrap CI is heuristic given $n = 3$ architectures.}
87	\label{fig:task_specificity}
88	\end{figure}
89	
90	\begin{figure*}[t]
91	\centering
92	\includegraphics[width=\textwidth]{figures/jaccard_heatmap_5arch.pdf}
93	\caption{Pairwise Jaccard heatmap across five architectures (340M, h3-1), where helped (hurt) examples are those correct only with (without) attention. Upper triangle: $J_{\text{helped}}$; lower triangle: $J_{\text{hurt}}$. All values $\leq 0.14$, all permutation tests $p \leq .002$. HellaSwag and PIQA results in Appendix~\ref{app:extended_arch}.}
94	\label{fig:jaccard_heatmap_5arch}
95	\end{figure*}
96	
97	Each architecture's per-example response to attention is largely idiosyncratic. The observed $\bar{J}$ reaches only 6--7\% of the achievable range above chance ($J_{\max} \approx 0.78$--$0.92$), ruling out ceiling constraints (\S\ref{ssec:per_example}). Readers can verify $\rho$ directly from Table~\ref{tab:convergence}; with $n = 3$ architectures, all bootstrap CIs are heuristic indicators of direction rather than precise coverage.
98	
99	This pattern generalizes beyond LAMBADA (Figure~\ref{fig:decoupling}c): on all four main benchmarks, mean pairwise Jaccard shows no significant trend with attention ratio (all $\rho \leq 0.80$, $p \geq 0.333$), with values uniformly between 0.08 and 0.11.
100	
101	Heuristic bootstrap 95\% CIs ($n = 3$; \S\ref{ssec:statistical_methods}) show non-overlapping $\sigma$ between pure and h3-1 but completely overlapping Jaccard across all hybrid ratios (\S\ref{ssec:statistical_methods}). Figure~\ref{fig:jaccard_hierarchy} shows a three-tier Jaccard hierarchy: independence baseline (${\sim}0.05$), cross-architecture (${\sim}0.10$, $2\times$ baseline), and within-architecture (${\sim}0.33$, $3\times$ cross-architecture; Appendix~\ref{app:within_arch_stability}). Pythia 70M seed calibration yields a comparable within-seed level ($J = 0.27$--$0.39$; Appendix~\ref{app:seed_calibration}), consistent with architecture-associated divergence, though matched multi-seed experiments would be needed for definitive evidence.
102	
103	\begin{figure}[t]
104	\centering
105	\includegraphics[width=\columnwidth]{figures/fig_jaccard_hierarchy.pdf}
106	\caption{Jaccard hierarchy on LAMBADA (1.3B). Cross-architecture overlap ($\bar{J} \approx 0.09$) is $2\times$ the independence baseline but only one-third of within-architecture overlap ($\bar{J} \approx 0.33$). Pythia 70M within-seed Jaccard (different scale) falls at a comparable level. Error bars show the helped--hurt range.}
107	\label{fig:jaccard_hierarchy}
108	\end{figure}
109	
110	Two interpretations are consistent with the observed stability. \textbf{(a) Fingerprint view:} each recurrent backbone imposes a characteristic inductive bias that determines which examples attention can rescue, locking in architecture-specific sensitivity patterns. \textbf{(b) Convergence view:} even minimal attention causes all architectures to rapidly adopt Transformer-like behavior, with residual per-example divergence arising from incomplete convergence. Appendix~\ref{app:transformer_entrainment} shows that h3-1 correct sets indeed shift toward the Transformer baseline, providing partial support for interpretation (b). Disentangling these accounts requires ablation of the attention mechanism itself---for example, replacing learned attention weights with random projections---an important direction for future work. Attention weight analysis (Appendix~\ref{app:attention_patterns}) shows GDN and RetNet produce nearly identical attention distributions (cosine 0.995) yet differ in per-example effects, suggesting these originate in the recurrent layers. The four-benchmark variation (Table~\ref{tab:multiplicity}) is consistent with independence: LAMBADA ($\alpha = 0.30$) is the only benchmark showing a variance-reduction trend despite having the highest multiplicity, while PIQA ($\alpha = 0.14$) and HellaSwag ($\alpha = 0.15$) show no variance reduction with the lowest multiplicity.
111	
112	Cross-scale analysis reveals a clear dissociation: per-example Jaccard is consistent across both scales ($\bar{J} = 0.08$--$0.10$ at 340M and 1.3B), whereas the aggregate variance trend is observed only at 1.3B on LAMBADA ($\rho = -0.50$, $p = .45$ at 340M). Ambiguity $\alpha$ is systematically higher at 340M ($\Delta \leq 8$\,pp), suggesting that the \emph{pattern} of per-example multiplicity is stable across scales while its magnitude tracks model capacity (Appendix~\ref{app:scale_per_example}--\ref{app:cross_scale}).
113	\vspace{-2pt}
114	\subsection{Robustness}\label{ssec:robustness}
115	
116	Removing GDN weakens the LAMBADA variance reduction ($\rho = -0.7$, $p = .233$) and reverses MMLU's ($\rho = +0.6$), both driven by GDN's 16-head configuration (vs.\ 32 in others; Appendix~\ref{app:gdn_confound}). The RetNet--HGRN2 pair preserves the independence pattern ($\sigma \leq 0.008$, $J = 0.086$--$0.108$). The aggregate variance pattern therefore depends on GDN inclusion; the per-example stability pattern does not. Five-architecture validation at 340M (adding GLA and DeltaNet) confirms $J \leq 0.14$ across all ten pairwise comparisons and four benchmarks (all $p < .01$; Figure~\ref{fig:jaccard_heatmap_5arch}; Appendix~\ref{app:extended_arch}), extending the per-example divergence finding to architectures not used in the primary analysis. Full sensitivity analyses appear in Appendix~\ref{app:sensitivity}; Transformer baseline comparison in Appendix~\ref{app:transformer_entrainment}.
117	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ff2ceed-c4f8-4f2c-b43a-17ca32f8e23c",
  "isSidechain": true,
  "promptId": "c7608d82-8599-4782-b1a2-f177b4bb14cc",
  "agentId": "a7ca798f294f742d3",
  "type": "user",
  "uuid": "cbb659a9-2758-4591-92cd-0678397ebe7d",
  "sourceToolAssistantUUID": "6ff2ceed-c4f8-4f2c-b43a-17ca32f8e23c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T09:10:21.214Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GWziGpu6mve9fcWoXoy9vM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbb659a9-2758-4591-92cd-0678397ebe7d",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2VWRHgBCJ5yWkSgPBm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b23e3465-f9d1-4121-8cba-ddb181c663d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lufipk4k1gvKYK2pbhCYL7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5614,
      "cache_read_input_tokens": 65110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5614,
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

_source line 23 · 2026-05-25T09:10:21.237Z_

<details><summary>↩ Tool result · `toolu_01GWziGpu6mve9fcWoXoy9vM`</summary>

```text
1	\vspace{-2pt}
2	\section{Conclusion}
3	
4	We have shown that hybrid linear recurrent architectures which appear interchangeable by aggregate benchmarks diverge substantially at the per-example level. This multiplicity varies by task type ($\alpha = 0.14$--$0.30$) rather than attention ratio. Per-example overlap appears to stabilize at 4\% attention (pairwise Jaccard $\leq 0.10$); two interpretations---architecture-specific fingerprints or rapid convergence toward Transformer-like behavior---remain open (Appendix~\ref{app:transformer_entrainment}). Confidence margins partially predict which examples are affected (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\%.
5	
6	At the 340M--1.3B scales studied here, per-example audit before architecture substitution is advisable when multiplicity is substantial---aggregate equivalence does not guarantee behavioral equivalence. Low cross-architecture Jaccard creates complementarity ($+7$--$14$\,pp oracle gain), though preliminary routing experiments show exploitation remains task-dependent ($+5.3$\,pp on LAMBADA; $-0.6$\,pp on PIQA).
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b23e3465-f9d1-4121-8cba-ddb181c663d4",
  "isSidechain": true,
  "promptId": "c7608d82-8599-4782-b1a2-f177b4bb14cc",
  "agentId": "a7ca798f294f742d3",
  "type": "user",
  "uuid": "86af4e31-4e79-4515-8061-fc0220ca1463",
  "sourceToolAssistantUUID": "b23e3465-f9d1-4121-8cba-ddb181c663d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-25T09:10:23.382Z_

Perfect! Now let me search all the text I've collected for the specific appendix label references. Let me compile the findings:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86af4e31-4e79-4515-8061-fc0220ca1463",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2WAYEZZWiiKE4H4GU8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a4fdaa4d-84bf-44ef-97f1-8231505b710b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SxXGEPLYXpLkBFTAnei2XQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6124,
      "cache_read_input_tokens": 70724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6124,
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

_source line 25 · 2026-05-25T09:10:24.655Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CyUpzmoPKyWUrvahD93HUM`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper && grep -n \"ref{app:\" sections/introduction.tex sections/related_work.tex sections/method.tex sections/experiments.tex sections/conclusion.tex main.tex 2>/dev/null | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4fdaa4d-84bf-44ef-97f1-8231505b710b",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2WAYEZZWiiKE4H4GU8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0f71169-8e78-4e79-81ca-43166a1a8131",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SxXGEPLYXpLkBFTAnei2XQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6124,
      "cache_read_input_tokens": 70724,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6124
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 162,
          "cache_read_input_tokens": 70724,
          "cache_creation_input_tokens": 6124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6124,
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

_source line 26 · 2026-05-25T09:10:24.836Z_

<details><summary>↩ Tool result · `toolu_01CyUpzmoPKyWUrvahD93HUM`</summary>

```text
sections/introduction.tex:30:    \item Architectural variation in hybrid recurrent models---controlled within a single model zoo sharing training data and hyperparameters---produces structured predictive multiplicity whose magnitude varies by task type (or evaluation format) rather than attention ratio (\S\ref{ssec:per_example}). Five-architecture validation confirms the pattern (\S\ref{ssec:robustness}; Appendix~\ref{app:extended_arch}).
sections/introduction.tex:32:    \item Pure-model confidence margins partially predict which examples attention will affect (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\% across architectures---a second dimension of multiplicity beyond per-example disagreement (\S\ref{ssec:per_example}; Appendix~\ref{app:prediction_framework}).
sections/method.tex:30:We evaluate on 10 benchmarks grouped into four categories defined by the primary cognitive demand of each task. This taxonomy (informal; not pre-registered) was fixed prior to analysis following standard categorizations in the evaluation literature \citep{arora2024zoology} and is treated as hypothesis-generating rather than confirmatory (see Appendix~\ref{app:benchmark_details} for the confirmatory/exploratory split), not derived post hoc from observed results. The categories test whether the effect of attention on cross-architecture variance depends on task type.
sections/method.tex:35:    \item \textbf{Reasoning}: HellaSwag, AI2 Reasoning Challenge (ARC-Challenge; \citealt{clark2018arc}), WinoGrande, and Physical Intuition Question Answering (PIQA). Choice of Plausible Alternatives (COPA; $n = 100$) is supplementary; its small sample renders $\alpha$ unreliable (Appendix~\ref{app:subsample_sensitivity}).
sections/method.tex:58:We decompose performance changes at the individual-example level on four benchmarks spanning three task categories: LAMBADA (5{,}153 examples; retrieval), HellaSwag (10{,}042; reasoning), PIQA (1{,}838; reasoning, two-choice), and ARC-Easy (2{,}376; mixed). HellaSwag uses normalized accuracy (acc\_norm) as the per-example correctness criterion. Supplementary analyses on BoolQ (3{,}270) and WinoGrande (1{,}267) appear in Appendix~\ref{app:boolq} and \ref{app:winogrande}. For each architecture, we compare the pure-recurrent baseline against its h3-1 hybrid (25\% attention), which maximizes the recurrent--hybrid contrast; \S\ref{ssec:per_example} confirms that $\alpha$ is stable across intermediate ratios (variation $< 0.03$). Each example is classified as:
sections/method.tex:68:To measure cross-architecture overlap, we compute the pairwise Jaccard similarity $J = |A \cap B| / |A \cup B|$ between the helped sets of two architectures and, separately, between their hurt sets. $J = 1$ indicates identical sets; $J = 0$ indicates no overlap. On $K$-choice tasks, binarization collapses $K{-}1$ wrong answers into a single ``incorrect'' category, potentially counting architectures as agreeing (both wrong) when they select different wrong answers. This conservative bias strengthens the multiplicity claim: true divergence may exceed what binary Jaccard captures. Appendix~\ref{app:continuous_jaccard} confirms robustness under continuous Jaccard similarity.
sections/method.tex:72:All tests are two-tailed. Spearman $\rho$ uses exact permutation tests ($5! = 120$ permutations); with $n = 5$, only $|\rho| = 1.0$ achieves $p < .05$ ($p = .017$), so all Spearman-based inferences are descriptive and exploratory. Bonferroni correction spans all 10 benchmarks (adjusted threshold $\alpha / 10 = 0.005$). Bootstrap 95\% bias-corrected and accelerated (BCa) confidence intervals use 10{,}000 resamples; with $n = 3$ architectures, these are heuristic indicators of effect direction. Within-architecture comparisons use Mann-Whitney U; cross-architecture comparisons use Kruskal-Wallis. Attention weight analysis extracts per-layer cosine similarity and Shannon entropy via forward hooks (Appendix~\ref{app:attention_patterns}). The permutation null does not condition on item difficulty; if difficulty-driven correlations inflate observed Jaccard while permutation destroys this structure, the test may be anti-conservative. However, the ${\sim}2.5\times$ observed-to-null ratio (all $z > 5.9$) provides substantial margin against this bias.
sections/experiments.tex:43:Do architectures converge by improving on the same examples? We compare each architecture's pure-recurrent baseline against its h3-1 hybrid on 5{,}153 LAMBADA examples, classifying each as helped, hurt, or unchanged. Although the decomposition is binary, it captures genuine separation in the continuous confidence space (Cohen's $d = 0.73$--$0.92$ between helped and hurt on LAMBADA; cross-benchmark details in Appendix~\ref{app:cm_cross}). Binarization discards confidence magnitude, so we supplement with continuous confidence margin analysis (Appendix~\ref{app:confidence_margin}) and verify that low Jaccard persists under continuous thresholds (Appendix~\ref{app:continuous_jaccard}).
sections/experiments.tex:45:Each architecture displays a distinct profile of per-example changes (Figure~\ref{fig:per_example_bars}). GDN loses a net 153 examples (462 helped, 615 hurt), RetNet loses 69 (426/495), and HGRN2 gains 153 (548/395; full counts in Appendix~\ref{app:per_example_counts}). HGRN2 is the only architecture for which adding attention yields a net per-example benefit. Pairwise Jaccard similarity is low: mean $\bar{J} \leq 0.10$, indicating ${\sim}90$\% non-overlap. Overlap significantly exceeds the independence baseline ($J_{\text{null}} \approx 0.05$, all $z > 5.9$, $p < .0001$; Appendix~\ref{app:jaccard_permutation}), plausibly reflecting shared sensitivity to example difficulty. Normalizing by $J_{\max}$, observed overlap reaches only 6--7\% of the achievable range above chance (Appendix~\ref{app:normalized_es}), confirming that low Jaccard cannot be attributed to set-size constraints.
sections/experiments.tex:54:\paragraph{Confidence margin predictor.} Pure-model confidence on the target token predicts which examples will be affected (AUC 0.70--0.74, a non-parametric measure equivalent to Mann-Whitney $U$; Appendix~\ref{app:confidence_margin}): rescue thresholds are architecture-invariant (1\% spread) but disruption thresholds vary 47\%, explaining cross-architecture Jaccard divergence (Appendix~\ref{app:prediction_framework}). Calibration differences account for less than half the threshold spread (Appendix~\ref{app:calibration}). The rescue pattern generalizes across three benchmarks ($d = 0.13$--$0.60$; Appendix~\ref{app:cm_cross}); disruption is weaker on reasoning tasks (Appendix~\ref{app:boolq}). This structured disagreement constitutes predictive multiplicity \citep{marx2020predictive} under architectural variation.
sections/experiments.tex:56:\paragraph{Confidence-based routing.} As an illustrative case study, the rescue-threshold asymmetry suggests a routing strategy: select the architecture whose pure-model confidence best predicts successful rescue. On LAMBADA, this outperforms majority vote by $+5.3$\,pp (SD $= 0.4$\,pp, 10 cross-validated splits), extracting 36\% of the oracle gap (oracle = 65.5\%; Appendix~\ref{app:complementarity}). On ARC-Easy, gains are modest ($+1.0$\,pp, SD $= 0.5$\,pp); on HellaSwag, routing provides no benefit ($-0.02$\,pp, $p = .89$); on PIQA, it is significantly negative ($-0.6$\,pp, $p = .006$). Routing works when multiplicity is high ($\alpha = 0.30$, LAMBADA) and a clear rescue-threshold signal exists, but is counterproductive when multiplicity is low ($\alpha = 0.14$, PIQA). A natural comparison---average-logits ensemble---is left to future work as it requires simultaneous inference across all architectures.
sections/experiments.tex:58:\paragraph{Multiplicity variation.} Extending to HellaSwag ($N = 10{,}042$) and PIQA ($N = 1{,}838$) reveals that predictive multiplicity varies systematically across tasks (Table~\ref{tab:multiplicity}). The ambiguity $\alpha$ \citep{marx2020predictive} ranges from 0.14 (PIQA) through 0.15 (HellaSwag) and 0.21 (ARC-Easy; Appendix~\ref{app:arceasy}) to 0.30 (LAMBADA). Format does not drive this ordering: HellaSwag (four-way) and PIQA (two-choice) produce nearly identical $\alpha$ despite different answer-space sizes, and $\alpha$ does not correlate with task accuracy ($\rho = -0.60$, $p = .24$). This within-multiple-choice invariance suggests that per-example multiplicity is associated with the cognitive demands of the task rather than the mechanical constraints of the evaluation format, though the confound between task type and format cannot be fully resolved with the present benchmarks (Limitations). Bootstrap 95\% CIs confirm the ordering (all non-overlapping except PIQA--HellaSwag; Table~\ref{tab:arceasy_ambiguity}). Pairwise Jaccard remains uniformly low ($\bar{J} \leq 0.10$, all $p < .01$ across four benchmarks), indicating that architectures affect different examples regardless of how many are affected. Within each benchmark, $\alpha$ is stable across attention ratios (variation $< 0.03$) but differs $2\times$ across task types (or evaluation formats), confirming that multiplicity magnitude depends on task, not attention ratio \citep[cf.][]{gorbett2026crossmodel}.
sections/experiments.tex:76:{\footnotesize Within-benchmark $\alpha$ variation $< 0.03$ across ratios. BoolQ, WinoGrande: Appendix~\ref{app:boolq}, \ref{app:winogrande}.}
sections/experiments.tex:93:\caption{Pairwise Jaccard heatmap across five architectures (340M, h3-1), where helped (hurt) examples are those correct only with (without) attention. Upper triangle: $J_{\text{helped}}$; lower triangle: $J_{\text{hurt}}$. All values $\leq 0.14$, all permutation tests $p \leq .002$. HellaSwag and PIQA results in Appendix~\ref{app:extended_arch}.}
sections/experiments.tex:101:Heuristic bootstrap 95\% CIs ($n = 3$; \S\ref{ssec:statistical_methods}) show non-overlapping $\sigma$ between pure and h3-1 but completely overlapping Jaccard across all hybrid ratios (\S\ref{ssec:statistical_methods}). Figure~\ref{fig:jaccard_hierarchy} shows a three-tier Jaccard hierarchy: independence baseline (${\sim}0.05$), cross-architecture (${\sim}0.10$, $2\times$ baseline), and within-architecture (${\sim}0.33$, $3\times$ cross-architecture; Appendix~\ref{app:within_arch_stability}). Pythia 70M seed calibration yields a comparable within-seed level ($J = 0.27$--$0.39$; Appendix~\ref{app:seed_calibration}), consistent with architecture-associated divergence, though matched multi-seed experiments would be needed for definitive evidence.
sections/experiments.tex:110:Two interpretations are consistent with the observed stability. \textbf{(a) Fingerprint view:} each recurrent backbone imposes a characteristic inductive bias that determines which examples attention can rescue, locking in architecture-specific sensitivity patterns. \textbf{(b) Convergence view:} even minimal attention causes all architectures to rapidly adopt Transformer-like behavior, with residual per-example divergence arising from incomplete convergence. Appendix~\ref{app:transformer_entrainment} shows that h3-1 correct sets indeed shift toward the Transformer baseline, providing partial support for interpretation (b). Disentangling these accounts requires ablation of the attention mechanism itself---for example, replacing learned attention weights with random projections---an important direction for future work. Attention weight analysis (Appendix~\ref{app:attention_patterns}) shows GDN and RetNet produce nearly identical attention distributions (cosine 0.995) yet differ in per-example effects, suggesting these originate in the recurrent layers. The four-benchmark variation (Table~\ref{tab:multiplicity}) is consistent with independence: LAMBADA ($\alpha = 0.30$) is the only benchmark showing a variance-reduction trend despite having the highest multiplicity, while PIQA ($\alpha = 0.14$) and HellaSwag ($\alpha = 0.15$) show no variance reduction with the lowest multiplicity.
sections/experiments.tex:112:Cross-scale analysis reveals a clear dissociation: per-example Jaccard is consistent across both scales ($\bar{J} = 0.08$--$0.10$ at 340M and 1.3B), whereas the aggregate variance trend is observed only at 1.3B on LAMBADA ($\rho = -0.50$, $p = .45$ at 340M). Ambiguity $\alpha$ is systematically higher at 340M ($\Delta \leq 8$\,pp), suggesting that the \emph{pattern} of per-example multiplicity is stable across scales while its magnitude tracks model capacity (Appendix~\ref{app:scale_per_example}--\ref{app:cross_scale}).
sections/experiments.tex:116:Removing GDN weakens the LAMBADA variance reduction ($\rho = -0.7$, $p = .233$) and reverses MMLU's ($\rho = +0.6$), both driven by GDN's 16-head configuration (vs.\ 32 in others; Appendix~\ref{app:gdn_confound}). The RetNet--HGRN2 pair preserves the independence pattern ($\sigma \leq 0.008$, $J = 0.086$--$0.108$). The aggregate variance pattern therefore depends on GDN inclusion; the per-example stability pattern does not. Five-architecture validation at 340M (adding GLA and DeltaNet) confirms $J \leq 0.14$ across all ten pairwise comparisons and four benchmarks (all $p < .01$; Figure~\ref{fig:jaccard_heatmap_5arch}; Appendix~\ref{app:extended_arch}), extending the per-example divergence finding to architectures not used in the primary analysis. Full sensitivity analyses appear in Appendix~\ref{app:sensitivity}; Transformer baseline comparison in Appendix~\ref{app:transformer_entrainment}.
sections/conclusion.tex:4:We have shown that hybrid linear recurrent architectures which appear interchangeable by aggregate benchmarks diverge substantially at the per-example level. This multiplicity varies by task type ($\alpha = 0.14$--$0.30$) rather than attention ratio. Per-example overlap appears to stabilize at 4\% attention (pairwise Jaccard $\leq 0.10$); two interpretations---architecture-specific fingerprints or rapid convergence toward Transformer-like behavior---remain open (Appendix~\ref{app:transformer_entrainment}). Confidence margins partially predict which examples are affected (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\%.
main.tex:54:\paragraph{Single training runs.} Each configuration is a single training run; consistency across all 40 architecture--benchmark combinations (all $p < .01$) and a $3\times$ within- vs.\ cross-architecture Jaccard gap (within-seed $J$ is 2.7--4.3$\times$ higher; Appendix~\ref{app:seed_calibration}) mitigate seed confounds but cannot fully resolve them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0f71169-8e78-4e79-81ca-43166a1a8131",
  "isSidechain": true,
  "promptId": "c7608d82-8599-4782-b1a2-f177b4bb14cc",
  "agentId": "a7ca798f294f742d3",
  "type": "user",
  "uuid": "134ae4ca-dafa-408b-b139-7c84617e2d33",
  "sourceToolAssistantUUID": "a0f71169-8e78-4e79-81ca-43166a1a8131",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-25T09:10:26.576Z_

Excellent! Now let me search for any remaining appendix references that might not have been caught, and compile the complete audit:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "134ae4ca-dafa-408b-b139-7c84617e2d33",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2WR281LuPWsx2zSsfC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e9e9c080-84da-4522-baf5-31198e6d2997",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017BSpgVdP7VcC9djwruoe2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4320,
      "cache_read_input_tokens": 76848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4320,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 28 · 2026-05-25T09:10:27.756Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XJ2rD1S9qtAYBQjXHs5m2R`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper && grep -rn \"\\\\\\\\ref{app:\" sections/introduction.tex sections/related_work.tex sections/method.tex sections/experiments.tex sections/conclusion.tex main.tex 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9e9c080-84da-4522-baf5-31198e6d2997",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2WR281LuPWsx2zSsfC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "62106bba-77fe-4517-b5cc-5ea77a31c823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017BSpgVdP7VcC9djwruoe2C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4320,
      "cache_read_input_tokens": 76848,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4320
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 161,
          "cache_read_input_tokens": 76848,
          "cache_creation_input_tokens": 4320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4320,
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

_source line 29 · 2026-05-25T09:10:27.811Z_

<details><summary>↩ Tool result · `toolu_01XJ2rD1S9qtAYBQjXHs5m2R`</summary>

```text
sections/introduction.tex:30:    \item Architectural variation in hybrid recurrent models---controlled within a single model zoo sharing training data and hyperparameters---produces structured predictive multiplicity whose magnitude varies by task type (or evaluation format) rather than attention ratio (\S\ref{ssec:per_example}). Five-architecture validation confirms the pattern (\S\ref{ssec:robustness}; Appendix~\ref{app:extended_arch}).
sections/introduction.tex:32:    \item Pure-model confidence margins partially predict which examples attention will affect (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\% across architectures---a second dimension of multiplicity beyond per-example disagreement (\S\ref{ssec:per_example}; Appendix~\ref{app:prediction_framework}).
sections/method.tex:30:We evaluate on 10 benchmarks grouped into four categories defined by the primary cognitive demand of each task. This taxonomy (informal; not pre-registered) was fixed prior to analysis following standard categorizations in the evaluation literature \citep{arora2024zoology} and is treated as hypothesis-generating rather than confirmatory (see Appendix~\ref{app:benchmark_details} for the confirmatory/exploratory split), not derived post hoc from observed results. The categories test whether the effect of attention on cross-architecture variance depends on task type.
sections/method.tex:35:    \item \textbf{Reasoning}: HellaSwag, AI2 Reasoning Challenge (ARC-Challenge; \citealt{clark2018arc}), WinoGrande, and Physical Intuition Question Answering (PIQA). Choice of Plausible Alternatives (COPA; $n = 100$) is supplementary; its small sample renders $\alpha$ unreliable (Appendix~\ref{app:subsample_sensitivity}).
sections/method.tex:58:We decompose performance changes at the individual-example level on four benchmarks spanning three task categories: LAMBADA (5{,}153 examples; retrieval), HellaSwag (10{,}042; reasoning), PIQA (1{,}838; reasoning, two-choice), and ARC-Easy (2{,}376; mixed). HellaSwag uses normalized accuracy (acc\_norm) as the per-example correctness criterion. Supplementary analyses on BoolQ (3{,}270) and WinoGrande (1{,}267) appear in Appendix~\ref{app:boolq} and \ref{app:winogrande}. For each architecture, we compare the pure-recurrent baseline against its h3-1 hybrid (25\% attention), which maximizes the recurrent--hybrid contrast; \S\ref{ssec:per_example} confirms that $\alpha$ is stable across intermediate ratios (variation $< 0.03$). Each example is classified as:
sections/method.tex:68:To measure cross-architecture overlap, we compute the pairwise Jaccard similarity $J = |A \cap B| / |A \cup B|$ between the helped sets of two architectures and, separately, between their hurt sets. $J = 1$ indicates identical sets; $J = 0$ indicates no overlap. On $K$-choice tasks, binarization collapses $K{-}1$ wrong answers into a single ``incorrect'' category, potentially counting architectures as agreeing (both wrong) when they select different wrong answers. This conservative bias strengthens the multiplicity claim: true divergence may exceed what binary Jaccard captures. Appendix~\ref{app:continuous_jaccard} confirms robustness under continuous Jaccard similarity.
sections/method.tex:72:All tests are two-tailed. Spearman $\rho$ uses exact permutation tests ($5! = 120$ permutations); with $n = 5$, only $|\rho| = 1.0$ achieves $p < .05$ ($p = .017$), so all Spearman-based inferences are descriptive and exploratory. Bonferroni correction spans all 10 benchmarks (adjusted threshold $\alpha / 10 = 0.005$). Bootstrap 95\% bias-corrected and accelerated (BCa) confidence intervals use 10{,}000 resamples; with $n = 3$ architectures, these are heuristic indicators of effect direction. Within-architecture comparisons use Mann-Whitney U; cross-architecture comparisons use Kruskal-Wallis. Attention weight analysis extracts per-layer cosine similarity and Shannon entropy via forward hooks (Appendix~\ref{app:attention_patterns}). The permutation null does not condition on item difficulty; if difficulty-driven correlations inflate observed Jaccard while permutation destroys this structure, the test may be anti-conservative. However, the ${\sim}2.5\times$ observed-to-null ratio (all $z > 5.9$) provides substantial margin against this bias.
sections/experiments.tex:43:Do architectures converge by improving on the same examples? We compare each architecture's pure-recurrent baseline against its h3-1 hybrid on 5{,}153 LAMBADA examples, classifying each as helped, hurt, or unchanged. Although the decomposition is binary, it captures genuine separation in the continuous confidence space (Cohen's $d = 0.73$--$0.92$ between helped and hurt on LAMBADA; cross-benchmark details in Appendix~\ref{app:cm_cross}). Binarization discards confidence magnitude, so we supplement with continuous confidence margin analysis (Appendix~\ref{app:confidence_margin}) and verify that low Jaccard persists under continuous thresholds (Appendix~\ref{app:continuous_jaccard}).
sections/experiments.tex:45:Each architecture displays a distinct profile of per-example changes (Figure~\ref{fig:per_example_bars}). GDN loses a net 153 examples (462 helped, 615 hurt), RetNet loses 69 (426/495), and HGRN2 gains 153 (548/395; full counts in Appendix~\ref{app:per_example_counts}). HGRN2 is the only architecture for which adding attention yields a net per-example benefit. Pairwise Jaccard similarity is low: mean $\bar{J} \leq 0.10$, indicating ${\sim}90$\% non-overlap. Overlap significantly exceeds the independence baseline ($J_{\text{null}} \approx 0.05$, all $z > 5.9$, $p < .0001$; Appendix~\ref{app:jaccard_permutation}), plausibly reflecting shared sensitivity to example difficulty. Normalizing by $J_{\max}$, observed overlap reaches only 6--7\% of the achievable range above chance (Appendix~\ref{app:normalized_es}), confirming that low Jaccard cannot be attributed to set-size constraints.
sections/experiments.tex:54:\paragraph{Confidence margin predictor.} Pure-model confidence on the target token predicts which examples will be affected (AUC 0.70--0.74, a non-parametric measure equivalent to Mann-Whitney $U$; Appendix~\ref{app:confidence_margin}): rescue thresholds are architecture-invariant (1\% spread) but disruption thresholds vary 47\%, explaining cross-architecture Jaccard divergence (Appendix~\ref{app:prediction_framework}). Calibration differences account for less than half the threshold spread (Appendix~\ref{app:calibration}). The rescue pattern generalizes across three benchmarks ($d = 0.13$--$0.60$; Appendix~\ref{app:cm_cross}); disruption is weaker on reasoning tasks (Appendix~\ref{app:boolq}). This structured disagreement constitutes predictive multiplicity \citep{marx2020predictive} under architectural variation.
sections/experiments.tex:56:\paragraph{Confidence-based routing.} As an illustrative case study, the rescue-threshold asymmetry suggests a routing strategy: select the architecture whose pure-model confidence best predicts successful rescue. On LAMBADA, this outperforms majority vote by $+5.3$\,pp (SD $= 0.4$\,pp, 10 cross-validated splits), extracting 36\% of the oracle gap (oracle = 65.5\%; Appendix~\ref{app:complementarity}). On ARC-Easy, gains are modest ($+1.0$\,pp, SD $= 0.5$\,pp); on HellaSwag, routing provides no benefit ($-0.02$\,pp, $p = .89$); on PIQA, it is significantly negative ($-0.6$\,pp, $p = .006$). Routing works when multiplicity is high ($\alpha = 0.30$, LAMBADA) and a clear rescue-threshold signal exists, but is counterproductive when multiplicity is low ($\alpha = 0.14$, PIQA). A natural comparison---average-logits ensemble---is left to future work as it requires simultaneous inference across all architectures.
sections/experiments.tex:58:\paragraph{Multiplicity variation.} Extending to HellaSwag ($N = 10{,}042$) and PIQA ($N = 1{,}838$) reveals that predictive multiplicity varies systematically across tasks (Table~\ref{tab:multiplicity}). The ambiguity $\alpha$ \citep{marx2020predictive} ranges from 0.14 (PIQA) through 0.15 (HellaSwag) and 0.21 (ARC-Easy; Appendix~\ref{app:arceasy}) to 0.30 (LAMBADA). Format does not drive this ordering: HellaSwag (four-way) and PIQA (two-choice) produce nearly identical $\alpha$ despite different answer-space sizes, and $\alpha$ does not correlate with task accuracy ($\rho = -0.60$, $p = .24$). This within-multiple-choice invariance suggests that per-example multiplicity is associated with the cognitive demands of the task rather than the mechanical constraints of the evaluation format, though the confound between task type and format cannot be fully resolved with the present benchmarks (Limitations). Bootstrap 95\% CIs confirm the ordering (all non-overlapping except PIQA--HellaSwag; Table~\ref{tab:arceasy_ambiguity}). Pairwise Jaccard remains uniformly low ($\bar{J} \leq 0.10$, all $p < .01$ across four benchmarks), indicating that architectures affect different examples regardless of how many are affected. Within each benchmark, $\alpha$ is stable across attention ratios (variation $< 0.03$) but differs $2\times$ across task types (or evaluation formats), confirming that multiplicity magnitude depends on task, not attention ratio \citep[cf.][]{gorbett2026crossmodel}.
sections/experiments.tex:76:{\footnotesize Within-benchmark $\alpha$ variation $< 0.03$ across ratios. BoolQ, WinoGrande: Appendix~\ref{app:boolq}, \ref{app:winogrande}.}
sections/experiments.tex:93:\caption{Pairwise Jaccard heatmap across five architectures (340M, h3-1), where helped (hurt) examples are those correct only with (without) attention. Upper triangle: $J_{\text{helped}}$; lower triangle: $J_{\text{hurt}}$. All values $\leq 0.14$, all permutation tests $p \leq .002$. HellaSwag and PIQA results in Appendix~\ref{app:extended_arch}.}
sections/experiments.tex:101:Heuristic bootstrap 95\% CIs ($n = 3$; \S\ref{ssec:statistical_methods}) show non-overlapping $\sigma$ between pure and h3-1 but completely overlapping Jaccard across all hybrid ratios (\S\ref{ssec:statistical_methods}). Figure~\ref{fig:jaccard_hierarchy} shows a three-tier Jaccard hierarchy: independence baseline (${\sim}0.05$), cross-architecture (${\sim}0.10$, $2\times$ baseline), and within-architecture (${\sim}0.33$, $3\times$ cross-architecture; Appendix~\ref{app:within_arch_stability}). Pythia 70M seed calibration yields a comparable within-seed level ($J = 0.27$--$0.39$; Appendix~\ref{app:seed_calibration}), consistent with architecture-associated divergence, though matched multi-seed experiments would be needed for definitive evidence.
sections/experiments.tex:110:Two interpretations are consistent with the observed stability. \textbf{(a) Fingerprint view:} each recurrent backbone imposes a characteristic inductive bias that determines which examples attention can rescue, locking in architecture-specific sensitivity patterns. \textbf{(b) Convergence view:} even minimal attention causes all architectures to rapidly adopt Transformer-like behavior, with residual per-example divergence arising from incomplete convergence. Appendix~\ref{app:transformer_entrainment} shows that h3-1 correct sets indeed shift toward the Transformer baseline, providing partial support for interpretation (b). Disentangling these accounts requires ablation of the attention mechanism itself---for example, replacing learned attention weights with random projections---an important direction for future work. Attention weight analysis (Appendix~\ref{app:attention_patterns}) shows GDN and RetNet produce nearly identical attention distributions (cosine 0.995) yet differ in per-example effects, suggesting these originate in the recurrent layers. The four-benchmark variation (Table~\ref{tab:multiplicity}) is consistent with independence: LAMBADA ($\alpha = 0.30$) is the only benchmark showing a variance-reduction trend despite having the highest multiplicity, while PIQA ($\alpha = 0.14$) and HellaSwag ($\alpha = 0.15$) show no variance reduction with the lowest multiplicity.
sections/experiments.tex:112:Cross-scale analysis reveals a clear dissociation: per-example Jaccard is consistent across both scales ($\bar{J} = 0.08$--$0.10$ at 340M and 1.3B), whereas the aggregate variance trend is observed only at 1.3B on LAMBADA ($\rho = -0.50$, $p = .45$ at 340M). Ambiguity $\alpha$ is systematically higher at 340M ($\Delta \leq 8$\,pp), suggesting that the \emph{pattern} of per-example multiplicity is stable across scales while its magnitude tracks model capacity (Appendix~\ref{app:scale_per_example}--\ref{app:cross_scale}).
sections/experiments.tex:116:Removing GDN weakens the LAMBADA variance reduction ($\rho = -0.7$, $p = .233$) and reverses MMLU's ($\rho = +0.6$), both driven by GDN's 16-head configuration (vs.\ 32 in others; Appendix~\ref{app:gdn_confound}). The RetNet--HGRN2 pair preserves the independence pattern ($\sigma \leq 0.008$, $J = 0.086$--$0.108$). The aggregate variance pattern therefore depends on GDN inclusion; the per-example stability pattern does not. Five-architecture validation at 340M (adding GLA and DeltaNet) confirms $J \leq 0.14$ across all ten pairwise comparisons and four benchmarks (all $p < .01$; Figure~\ref{fig:jaccard_heatmap_5arch}; Appendix~\ref{app:extended_arch}), extending the per-example divergence finding to architectures not used in the primary analysis. Full sensitivity analyses appear in Appendix~\ref{app:sensitivity}; Transformer baseline comparison in Appendix~\ref{app:transformer_entrainment}.
sections/conclusion.tex:4:We have shown that hybrid linear recurrent architectures which appear interchangeable by aggregate benchmarks diverge substantially at the per-example level. This multiplicity varies by task type ($\alpha = 0.14$--$0.30$) rather than attention ratio. Per-example overlap appears to stabilize at 4\% attention (pairwise Jaccard $\leq 0.10$); two interpretations---architecture-specific fingerprints or rapid convergence toward Transformer-like behavior---remain open (Appendix~\ref{app:transformer_entrainment}). Confidence margins partially predict which examples are affected (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\%.
main.tex:54:\paragraph{Single training runs.} Each configuration is a single training run; consistency across all 40 architecture--benchmark combinations (all $p < .01$) and a $3\times$ within- vs.\ cross-architecture Jaccard gap (within-seed $J$ is 2.7--4.3$\times$ higher; Appendix~\ref{app:seed_calibration}) mitigate seed confounds but cannot fully resolve them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62106bba-77fe-4517-b5cc-5ea77a31c823",
  "isSidechain": true,
  "promptId": "c7608d82-8599-4782-b1a2-f177b4bb14cc",
  "agentId": "a7ca798f294f742d3",
  "type": "user",
  "uuid": "a6c66a91-07eb-4cb9-a168-d3995f9acab6",
  "sourceToolAssistantUUID": "62106bba-77fe-4517-b5cc-5ea77a31c823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-25T09:10:38.459Z_

Perfect! Now I have all the information I need to compile the audit. Let me create the comprehensive report:

## Appendix Label Reference Audit

Based on my thorough search of the main text files (introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, and main.tex), here is the complete audit:

```
Label | Status | Referenced from (file:line)
------|--------|----------------------------
app:benchmark_details | FOUND | method.tex:30
app:convergence_detail | NOT FOUND | ORPHAN
app:scale_convergence | NOT FOUND | ORPHAN
app:sensitivity | FOUND | experiments.tex:116
app:gdn_confound | FOUND | experiments.tex:116
app:attention_patterns | FOUND | method.tex:72, experiments.tex:110
app:cross_scale | FOUND | experiments.tex:112
app:per_example_counts | FOUND | experiments.tex:45
app:normalized_es | FOUND | experiments.tex:45
app:arceasy | FOUND | experiments.tex:58
app:jaccard_permutation | FOUND | experiments.tex:45
app:transformer_entrainment | FOUND | experiments.tex:110, experiments.tex:116, conclusion.tex:4
app:within_arch_stability | FOUND | experiments.tex:101
app:cross_bench_jaccard | NOT FOUND | ORPHAN
app:continuous_jaccard | FOUND | method.tex:68, experiments.tex:43
app:confidence_margin | FOUND | experiments.tex:43, experiments.tex:54
app:cm_cross | FOUND | experiments.tex:43, experiments.tex:54
app:prediction_framework | FOUND | introduction.tex:32, experiments.tex:54
app:calibration | FOUND | experiments.tex:54
app:boolq | FOUND | method.tex:58, experiments.tex:54, experiments.tex:76
app:winogrande | FOUND | method.tex:58, experiments.tex:76
app:scale_per_example | FOUND | experiments.tex:112
app:subsample_sensitivity | FOUND | method.tex:35
app:complementarity | FOUND | experiments.tex:56
app:seed_calibration | FOUND | main.tex:54, experiments.tex:101
app:extended_arch | FOUND | introduction.tex:30, experiments.tex:93, experiments.tex:116
app:code_data | NOT FOUND | ORPHAN
app:ai-assistants | NOT FOUND | ORPHAN
```

## Summary

**Total labels checked:** 28  
**Referenced from main text:** 24 (85.7%)  
**Orphan labels (zero references):** 4 (14.3%)

### Orphan Labels (not referenced in main text):
1. `app:convergence_detail` — Convergence Detail
2. `app:scale_convergence` — Scale-Dependent Convergence
3. `app:cross_bench_jaccard` — Cross-Benchmark Jaccard Trajectories
4. `app:code_data` — Code and Data Availability
5. `app:ai-assistants` — Use of AI Assistants

These five appendix sections exist in the appendix file but have no references from the non-appendix main text files. They may be referenced only within the appendix itself or may be supplementary sections that don't require cross-referencing from the main narrative.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6c66a91-07eb-4cb9-a168-d3995f9acab6",
  "isSidechain": true,
  "agentId": "a7ca798f294f742d3",
  "requestId": "req_011CbP2Wdp4hEtnTyauCQoeP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e8d0f76b-2456-4241-a5d0-d65142d2ed2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/director_63b8b789",
  "sessionId": "9aa19bf8-cb5b-42e3-9abb-cce2d701182a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "toasty-tinkering-galaxy",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0175fUVuDAAMj9VNDJ5xGBX2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 4318,
      "cache_read_input_tokens": 81168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4318,
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
