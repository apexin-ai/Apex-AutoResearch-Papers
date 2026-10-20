# Research conversation: I need to review the full content of an academic paper to decide where to expand it. The paper is at /home/ubuntu/.agent

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad9c11a1a52b2a80e.jsonl`
- **Structured JSON:** [`4f5f15c136b10c831d64.json`](../../sessions/4f/4f5f15c136b10c831d64.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-25T16:07:24.479Z_

I need to review the full content of an academic paper to decide where to expand it. The paper is at /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/

Please read and summarize the content of these files (full content, not excerpts):
1. conclusion.tex - the conclusion section
2. experiments.tex - the experiments section  
3. method.tex - the method section
4. introduction.tex - the introduction
5. abstract.tex - the abstract
6. appendix_proofs.tex - just the SECTION HEADINGS and any important tables/figures (not full proofs). I need to know what's in the appendix that could potentially be moved to the main text.

For each file, give me the full text content. For appendix_proofs.tex, just list the section/subsection headings and any \begin{table} or \begin{figure} environments with their captions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2270b57b-d325-458d-b789-f645f11c5c65",
  "agentId": "ad9c11a1a52b2a80e",
  "type": "user",
  "uuid": "57b5a6c1-be27-446c-9ac8-05989b55f0c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T16:07:26.273Z_

I'll read all these files for you. Let me start by reading them in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57b5a6c1-be27-446c-9ac8-05989b55f0c3",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaJin73Y8xTQWk4RXDk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "94a6037a-8980-47be-bc5a-75cecd25fa36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NP3RnwSrkW81PARdKXreqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37386,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37386,
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

_source line 3 · 2026-05-25T16:07:26.692Z_

<details open><summary>🔧 Tool call — Read · `toolu_013nNFhjKVYVyfWcWUfKBLVD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94a6037a-8980-47be-bc5a-75cecd25fa36",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaJin73Y8xTQWk4RXDk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8562332c-51a4-411f-9f53-0195a1b0d051",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NP3RnwSrkW81PARdKXreqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37386,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37386,
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

_source line 4 · 2026-05-25T16:07:26.721Z_

<details><summary>↩ Tool result · `toolu_013nNFhjKVYVyfWcWUfKBLVD`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We characterized how multi-class annotation errors interact with causal DAG topology: at $K{\geq}3$, exposure and IV can reverse treatment effect signs while five topologies preserve them. ASVs provide a topology-dependent vulnerability ranking; matrix-based corrections are provably ineffective for four topologies (FWL invariance). Practitioners should identify the topology first: for exposure, PPI++ reduces bias from ${\sim}61\%$ to ${<}1\%$ (Table~\ref{tab:e2e-real-cm}); for IV, topology-agnostic correction can amplify bias ($-$139\% in our demo; Table~\ref{tab:e2e-demo}). High $F_1$ does not guarantee low causal bias; topology assessment must precede downstream inference.
5	
6	Differential misclassification and proving Conjecture~\ref{conj:monotone} for general $K$ remain open.
7	
8	\section*{Limitations}
9	
10	Our closed-form results assume linear SEMs with proportional effects ($f{=}\lambda g$); sign preservation empirically holds at 97.3\% under non-proportional effects (Appendix~\ref{sec:proportional_real_matrices}), but recommendations do not directly extend to nonlinear models (matching, doubly-robust). The framework assumes a known DAG with non-differential misclassification (Appendix~\ref{sec:nondiff_stress},~\ref{sec:realistic_epsilon}); DAG misspecification under measurement error may compound bias. ASV computation requires gold labels for $C^{-1}$; error propagation under small gold-label budgets ($<$500) and general $K{\geq}3$ envelope monotonicity (Conjecture~\ref{conj:monotone}) remain open.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8562332c-51a4-411f-9f53-0195a1b0d051",
  "isSidechain": true,
  "promptId": "2270b57b-d325-458d-b789-f645f11c5c65",
  "agentId": "ad9c11a1a52b2a80e",
  "type": "user",
  "uuid": "ef9d7e1c-cacf-4527-88ec-fba4ccca73c2",
  "sourceToolAssistantUUID": "8562332c-51a4-411f-9f53-0195a1b0d051",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T16:07:26.814Z_

<details open><summary>🔧 Tool call — Read · `toolu_018iDS2AUAbfu68m1gEpRNMr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef9d7e1c-cacf-4527-88ec-fba4ccca73c2",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaJin73Y8xTQWk4RXDk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0cc5d13-f04e-4746-b999-f79c00f53165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NP3RnwSrkW81PARdKXreqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37386,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37386,
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

_source line 6 · 2026-05-25T16:07:26.820Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NtwVWkEXG3RLGTbdPkrpd1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0cc5d13-f04e-4746-b999-f79c00f53165",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaJin73Y8xTQWk4RXDk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c361b2ec-3475-4925-b71c-9ed9d9eabdb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NP3RnwSrkW81PARdKXreqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37386,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37386,
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

_source line 7 · 2026-05-25T16:07:26.831Z_

<details><summary>↩ Tool result · `toolu_018iDS2AUAbfu68m1gEpRNMr`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{table}[t]
5	\centering
6	\caption{Bias under $K{=}3$ non-differential misclassification (100{,}000 Dirichlet$(1,1,1)$ matrices). Violation: $|\text{bias}| > 0$; Sign Flip: any coefficient reverses sign; Amplif.: $|\hat{\tau}| > |\tau|$. $\tau_{\text{sf}}{=}0$?: sign-flip guarantee holds unconditionally (Yes), conditionally (Cond.; Proposition~\ref{prop:signflip}), or not (No). Collider 100\% amplification reflects Berkson bias; misclassification is protective.}
7	\label{tab:taxonomy}
8	\small
9	\resizebox{\columnwidth}{!}{\begin{tabular}{lcccc}
10	\toprule
11	\textbf{Topology} & \textbf{Violation} & \textbf{Sign Flip} & \textbf{Amplif.} & $\tau_{\text{sf}}{=}0$? \\
12	\midrule
13	Confounding & 100\% & 0\% & 100\% & Cond. \\
14	Exposure & 85\% & 83.4\% & 14.1\% & No \\
15	Mediation & 100\% & 0\% & 100\% & Cond. \\
16	Front-door & 100\% & 0\% & 100\% & Cond. \\
17	Collider & 100\% & 0\% & 100\% & Cond. \\
18	M-bias & 53.2\% & 0\% & 10.4\% & Yes \\
19	IV & 100\% & 52.6\% & 100\% & No \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	We validate through Monte Carlo simulation ($K{=}3$), cross-$K$ robustness checks ($K{=}5,7$), and empirical validation with real LLM confusion matrices from three natural language processing (NLP) tasks ($K{=}2,3,10$).
25	
26	\subsection{Setup}
27	\label{sec:setup}
28	
29	For each topology, we sample 100{,}000 confusion matrices from a Dirichlet$(1,1,1)$ prior, compute analytical probability limits, and validate against Monte Carlo simulation ($N{=}10{,}000$). ASV experiments use $C(\delta) = (1{-}\delta)I + \delta C_0$.
30	
31	\subsection{Bias Taxonomy}
32	\label{sec:taxonomy_results}
33	
34	\begin{figure}[t]
35	\centering
36	\includegraphics[width=\columnwidth]{fig7_dirichlet_overlay.pdf}
37	\caption{Empirical LLM confusion matrices (markers) overlaid on theoretical violation-rate curves from $K{=}3$ Dirichlet analysis. Left: exposure; right: IV. Real-world accuracy places all models in the low-risk region for IV sign reversal but not for exposure.}
38	\label{fig:dirichlet_overlay}
39	\end{figure}
40	
41	\paragraph{Theory-MC agreement.}
42	Analytical probability limits match Monte Carlo estimates with mean absolute percentage error (MAPE) of 1.6\%, averaged across 161 scenarios (23 LLM configurations $\times$ 7 topologies; per-topology range: 0.3\%--3.7\%), validating the closed-form derivations and justifying probability limits as practical bias diagnostics.
43	
44	\paragraph{Exposure DAG: sign reversal under multi-class misclassification.}
45	Under realistic accuracy (diagonal $\geq 0.7$), the violation rate is 13.7\% with 2.1\% sign reversal; at diagonal $\geq 0.9$, violation persists at 11.9\% (Appendix~\ref{sec:iv_dirichlet_subspace}). Under the full Dirichlet prior, 85\% of matrices violate the binary ``toward-null'' guarantee and 83.4\% cause sign reversal; $\min_k C_{kk} < 0.55$ predicts sign reversal with 91\% accuracy (Appendix~\ref{sec:sign_determinants}). The $K{=}2$ control confirms classical attenuation~\cite{brenner1993}. This establishes the multi-class failure as structurally distinct.
46	
47	\paragraph{Structural guarantee for non-exposure topologies.}
48	Five topologies exhibit zero sign-flip rate (Table~\ref{tab:taxonomy}): confounding, mediation, and front-door show 100\% amplification~\cite{brenner1993, dosemeci1990} but never reverse the sign; collider is protective ($|B(C)|$ non-increasing; Conjecture~\ref{conj:monotone}); M-bias shows weakest sensitivity (53.2\% violation). All patterns persist at $K{=}5,7$ (Appendix~\ref{sec:cross_k_robustness}).
49	
50	\paragraph{IV: Wald estimator instability.}
51	The IV topology is the sole non-exposure exception: 52.6\% of random matrices cause sign reversal, stable across $K{=}3,5,7$. Diagonal dominance ($C_{kk} > 0.5$) eliminates sign reversal but preserves amplification (Appendix~\ref{sec:iv_dirichlet_subspace}); however, all 23 empirical LLM configurations show zero IV sign reversal.
52	
53	Figure~\ref{fig:dirichlet_overlay} overlays all 23 empirical LLM configurations onto the theoretical violation-rate curves; real-world accuracy ($\min_k C_{kk} \geq 0.6$) places all models in the low-risk region for IV but leaves exposure vulnerable.
54	
55	\subsection{ASV Framework Validation}
56	\label{sec:asv_results}
57	
58	\begin{table}[t]
59	\centering
60	\small
61	\caption{ASV summary across topologies ($K{=}3$, $\tau{=}0.5$). ---: not applicable.}
62	\label{tab:asv_summary}
63	\begin{tabular}{lccc}
64	\toprule
65	\textbf{Topology} & \textbf{Mag ASV} & \textbf{Power} & \textbf{Sign-flip} \\
66	\midrule
67	IV          & 0.10--0.61 & 0\%   & 1.1--6.7 \\
68	Front-door  & 0.06--0.39 & 100\% & --- \\
69	Confounding & 0.08--0.49 & 100\% & --- \\
70	Mediation   & 0.08--0.45 & 0\%   & --- \\
71	Collider    & 0.34--2.03 & 0\%   & --- \\
72	M-bias      & $\infty$   & 98\%  & --- \\
73	Exposure    & ---        & ---   & 83.4\% \\
74	\bottomrule
75	\end{tabular}
76	\end{table}
77	
78	\paragraph{ASV results.}
79	The ASV envelope is $\varepsilon$-approximately monotonic ($\varepsilon < 0.02$; Conjecture~\ref{conj:monotone}); IV is maximally fragile, M-bias is immune ($\text{ASV} = \infty$; Figure~\ref{fig:asv_ranking}). Sign-flip ASV: 83.4\% of exposure matrices yield $\delta^*_{\text{sf}} < 1$; IV ranges 1.1--6.7 (Table~\ref{tab:asv_summary}). Significance ASV exhibits a phase transition at $N^* \approx 6{,}000$--$10{,}000$; bootstrap CIs (Appendix~\ref{sec:bootstrap_asv},~\ref{sec:c_robustness}) confirm stable topology ranking, with the safe/fragile partition recovering from $n_{\text{gold}} \geq 100$ (82\% stability; Appendix~\ref{sec:asv_diagnostics},~\ref{sec:asv_case_study}).
80	
81	\subsection{Empirical Validation}
82	\label{sec:empirical}
83	
84	We validate using real LLM confusion matrices from HumAID~\cite{alam2021humaid} ($K{=}10$), VAST ($K{=}3$), and CivilComments ($K{=}2$): four LLMs, 23 configurations, 161 bias scenarios. HumAID ($K{=}10$) matches predictions: IV (12.4--42.1\%) and exposure (9.0--17.4\%) dominate; remaining topologies $<$15\%. $F_1$ does not exhibit significant rank correlation with bias ($\rho = -0.10$, $p = 0.45$; Figure~\ref{fig:f1_vs_bias}), but per-topology patterns diverge ($\rho \leq -0.53$ for five topologies vs.\ $0.87$ for M-bias; Appendix~\ref{sec:within_topo_f1}). Of exposure coefficients, 14/23 (61\%) exhibit sign reversal, all secondary; zero across 138 non-exposure scenarios.
85	
86	\begin{figure}[t]
87	\centering
88	\includegraphics[width=\columnwidth]{fig5_f1_vs_bias.pdf}
89	\caption{Topology determines downstream causal bias, not $F_1$. HumAID $K{=}10$ (56 points): within $F_1$ range 0.614--0.690, bias varies $10{\times}$ (IV 42.1\% vs.\ collider $<$5.6\%).}
90	\label{fig:f1_vs_bias}
91	\end{figure}
92	
93	\subsection{Correction Guidance}
94	\label{sec:correction}
95	
96	We evaluate five correction methods (naive plug-in, maximum likelihood adjustment (MLA), design-based supervised learning (DSL)~\cite{egami_hinck_stewart_wei2023}, Monte Carlo simulation extrapolation (MC-SIMEX)~\cite{kuchenhoff2006simex}, PPI++~\cite{angelopoulos2023}) across all topologies (210 configurations; Table~\ref{tab:correction}, Appendix~\ref{app:supplementary}).
97	
98	\paragraph{FWL invariance.}
99	Under linear regression, FWL invariance renders matrix-based methods (naive plug-in, MLA) provably ineffective for covariate topologies (0\% bias reduction; Appendix~\ref{app:fwl_proof}): the treatment coefficient depends only on the projection orthogonal to the covariate space, so relabeling $A^* \to A$ leaves the coefficient unchanged. Under logistic regression this invariance breaks, but the method ranking persists ($|\Delta| < 0.02$; Appendix~\ref{sec:fwl_nonlinear}).
100	
101	\begin{figure}[t]
102	\centering
103	\includegraphics[width=\columnwidth]{fig4_binarization.pdf}
104	\caption{Binarization collapse $\Delta$: additional bias from collapsing $K{=}3$ to binary. Topology determines severity ($>$150$\times$ range); exposure and IV exhibit sign flips.}
105	\label{fig:binarization}
106	\end{figure}
107	
108	\paragraph{Method ranking and decision procedure.}
109	PPI++ achieves the highest root mean squared error (RMSE) reduction (47.0\% at $K{=}3$) but requires gold labels (Appendix~\ref{sec:ppi_gold_ratio}) and harms M-bias ($-$88\%); MC-SIMEX is gold-free and $K$-robust (27--70\%), though it harms front-door ($-$62.4\%); rankings are stable across $K$ ($\rho \geq 0.80$; Appendix~\ref{sec:correction_k_sensitivity}). Algorithm~\ref{alg:correction} (Appendix) routes through risk assessment, method selection, and FWL screening. End-to-end demos (Appendix~\ref{sec:e2e_demo},~\ref{sec:real_cm_demo},~\ref{app:case_study}) validate: PPI++ reduces exposure bias from 42.9\% to 0.2\%, while topology-agnostic IV correction amplifies bias ($-$139\%). Collapsing $K{=}3$ to binary is not a safe fallback: the additional bias $\Delta$ varies $>$150$\times$ by topology (Figure~\ref{fig:binarization}; Appendix~\ref{app:binarization}).
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0cc5d13-f04e-4746-b999-f79c00f53165",
  "isSidechain": true,
  "promptId": "2270b57b-d325-458d-b789-f645f11c5c65",
  "agentId": "ad9c11a1a52b2a80e",
  "type": "user",
  "uuid": "e178238c-ce1f-4c73-8ad5-ed40ea03ebdb",
  "sourceToolAssistantUUID": "a0cc5d13-f04e-4746-b999-f79c00f53165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T16:07:26.829Z_

<details><summary>↩ Tool result · `toolu_01NtwVWkEXG3RLGTbdPkrpd1`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Setup and Notation}
5	\label{sec:notation}
6	
7	Let $A$ denote a true $K$-class categorical variable (e.g., sentiment with $K{=}3$ levels) and $A^*$ its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a $K{\times}K$ confusion matrix $C$ with entries $C_{jk} = P(A^*{=}j \mid A{=}k)$, where each column sums to one (column-stochastic: each column gives the distribution of predicted labels for a given true label). Following \citet{hernan_cole2009}, we represent this measurement process using \emph{starred-node} DAGs: the true variable $A$ is latent, and the observed $A^*$ is connected to $A$ via a dashed measurement edge.
8	
9	\paragraph{Notation conventions.}
10	Our analysis characterizes probability limits ($N \to \infty$) under the FWL theorem~\cite{frisch1933partial}, which explains why matrix-based corrections fail for covariate topologies (Section~\ref{sec:correction}). Notation is collected in Table~\ref{tab:notation} (Appendix~\ref{app:notation_table}).
11	
12	\begin{definition}[Non-differential misclassification]
13	\label{def:nondiff}
14	Misclassification of $A$ is non-differential with respect to outcome $Y$ and covariates $\mathbf{Z}$ if $P(A^*{=}j \mid A{=}k, Y, \mathbf{Z}) = P(A^*{=}j \mid A{=}k) = C_{jk}$ for all $j,k$.
15	\end{definition}
16	
17	In batch annotation pipelines, the LLM processes each text independently without access to $Y$, making non-differentiality an architectural invariant~\cite{ziems2024can}; Y-stratified permutation tests confirm this (1/12 rejection at $\alpha{=}0.05$; Appendix~\ref{sec:nondiff_verify},~\ref{sec:y_stratified_test}). Non-differentiality may be violated when $Y$ correlates with text content, in which case our Y-stratified test provides empirical verification. Under stress testing, sign reversal occurs in 14/16 $K{\geq}3$ exposure configurations at $\eta{=}0.01$ structured departure (Appendix~\ref{sec:nondiff_stress}).
18	
19	Throughout, $\tau$ denotes the causal estimand of interest, whose definition varies by topology: the confounder's coefficient, the treatment effect, the indirect effect, or the Wald ratio (Appendix~\ref{app:confounding}ff.).
20	
21	We study seven canonical DAG topologies (Figure~\ref{fig:dag_taxonomy})~\cite{pearl2009, hernan2020causal}, deriving probability limits under linear structural equation models (SEMs)~\cite{carroll2006}; logistic regression robustness is verified in Appendix~\ref{sec:logistic_dgp} and~\ref{sec:fwl_nonlinear}.
22	
23	\begin{figure*}[t]
24	\centering
25	\includegraphics[width=\textwidth]{fig2_bias_distribution.pdf}
26	\caption{Bias distributions under 100{,}000 random $K{=}3$ confusion matrices (uniform Dirichlet; realistic-accuracy results in Section~\ref{sec:taxonomy_results}). Red = sign reversal. Exposure: 83.4\% sign reversal; IV: 52.6\%.}
27	\label{fig:bias_distribution}
28	\end{figure*}
29	
30	\subsection{Multi-Class Bias Expressions}
31	\label{sec:bias_expressions}
32	
33	For each topology, we derive the $\operatorname{plim}$\footnote{The probability limit (plim) is the value to which an estimator converges as sample size $N \to \infty$; it characterizes systematic bias separately from sampling variability.} of the naive estimator that substitutes $A^*$ for $A$. Let $\tau$ denote the target causal parameter, whose precise definition is topology-specific (e.g., the coefficient on $X$ for confounding, the category-specific $\beta_j$ for exposure, or the direct effect $\tau_{\text{direct}}$ for mediation), and $\hat{\tau}(A^*)$ the estimator using misclassified annotations.
34	
35	\paragraph{Confounding ($A$ = confounder).}
36	When $A$ confounds the $X{\to}Y$ relationship, the ordinary least squares (OLS) estimator controlling for $A^*$ has probability limit
37	\begin{equation}
38	\label{eq:confounding}
39	\operatorname{plim}\;\hat{\tau}(A^*) = \bigl(\mathbb{E}[Z^{\prime}Z]\bigr)^{-1}\mathbb{E}[Z^{\prime}X]\,\boldsymbol{\beta},
40	\end{equation}
41	where $Z = [X, \text{dummies}(A^*)]$, $\boldsymbol{\beta}$ contains the true coefficients, and the target parameter $\tau$ is the coefficient on $X$. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of $\hat{\tau}$ is preserved: $\tau_{\text{sign\_flip}} = 0$ structurally.\footnote{Consistent with \citet{brenner1993}: misclassification degrades confounding control, producing amplification ($|\hat{\tau}| > |\tau|$, universal in this topology) but never sign reversal ($\operatorname{sign}(\hat{\tau}) \neq \operatorname{sign}(\tau)$).}
42	
43	\paragraph{Exposure ($A$ = treatment variable).}
44	When $A$ is the exposure of interest, the biased coefficient for category $j$ becomes a weighted combination of true coefficients:
45	\begin{equation}
46	\label{eq:exposure}
47	\operatorname{plim}\;\hat{\beta}_j(A^*) = \sum_{k=1}^{K} w_{jk}\,\beta_k,
48	\end{equation}
49	where $w_{jk}$ depends on the confusion matrix $C$ and the population marginal $\pi_k = P(A{=}k)$. Unlike binary misclassification~\cite{brenner1993}, $K{\geq}3$ permits $w_{jk}$ to assign negative weight to categories with opposite-sign coefficients, producing \emph{sign reversal} (83.4\% under uniform Dirichlet prior); this is structurally impossible at $K{=}2$.
50	
51	\begin{figure*}[t]
52	\centering
53	\includegraphics[width=\textwidth]{fig3_asv_ranking.pdf}
54	\caption{ASV vulnerability ranking across topologies. Three ASV types (magnitude, significance, sign-flip) reveal a topology-dependent spectrum from IV (maximally fragile) to M-bias (immune, ASV $= \infty$).}
55	\label{fig:asv_ranking}
56	\end{figure*}
57	
58	\paragraph{Primary coefficient preservation.}
59	Across 23 empirical LLM configurations, the primary coefficient (the category with the largest true effect $|\beta_k|$) never reverses sign, while 61\% reverse a secondary (non-dominant) coefficient, confirmed under 100{,}000 Dirichlet matrices with diagonal ${\geq}\,0.7$ across six beta-ratio conditions (1.0 to 50.0) with 0\% primary sign-flip (Appendix~\ref{app:exposure}).
60	
61	\paragraph{Mediation ($A$ = mediator).}
62	When $A$ mediates the $X{\to}Y$ relationship~\cite{vanderweele2015explanation}, the direct effect estimator controlling for $A^*$ has probability limit
63	\begin{equation}
64	\label{eq:mediation}
65	\operatorname{plim}\;\hat{\tau}_{\text{direct}}(A^*) = \tau_{\text{direct}} + \bigl(1 - \lambda(C)\bigr)\,\tau_{\text{indirect}},
66	\end{equation}
67	where $\lambda(C) \in [0,1]$ under proportional effects (Appendix~\ref{app:mediation}, Proposition~\ref{prop:lambda_bound}), with $\lambda(I) = 1$ under perfect classification. Misclassification ($\lambda < 1$) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in $|\hat{\tau}_{\text{direct}}|$ but preserving the sign ($\tau_{\text{sign\_flip}} = 0$).
68	
69	\paragraph{Collider, M-bias, and front-door.}
70	Three topologies exhibit protective or immune behavior. \textbf{Collider:} conditioning on $A^*$ instead of $A$ attenuates Berkson bias by weakening the spurious path, so annotation error is protective ($\tau_{\text{sign\_flip}} = 0$). \textbf{M-bias:} in the M-shaped DAG~\cite{greenland2003}, misclassifying $A$ attenuates the non-causal path, making this topology immune ($\text{ASV} = \infty$). \textbf{Front-door:} the front-door estimator~\cite{bellemare_bloem2024} requires two stages ($X \to A$ and $A \to Y$), each attenuated by $C$; the compound effect produces moderate bias with $\tau_{\text{sign\_flip}} = 0$ (Appendix~\ref{app:frontdoor}).
71	
72	\paragraph{Instrumental variable ($A$ = instrument).}
73	The Wald estimator~\cite{angrist_imbens1995} $\hat{\tau}_{\text{IV}} = \hat{\text{cov}}(A^*, Y) / \hat{\text{cov}}(A^*, X)$ has $C$ in the denominator. Misclassification can drive first-stage coefficients toward zero or reverse their sign; under random Dirichlet matrices, 52.6\% produce sign reversal; IV is the most fragile topology (Appendix~\ref{sec:iv_dirichlet_subspace}).
74	
75	\paragraph{Structural sign-flip guarantee.}
76	\begin{proposition}[Sign preservation: analytic results]
77	\label{prop:signflip}
78	Under non-differential misclassification with $C_{kk} > 0$ for all $k$:
79	\emph{(a)}~Confounding preserves sign when $\operatorname{sign}(\tau) = \operatorname{sign}(\tau {+} B_{\mathrm{OV}})$, where $B_{\mathrm{OV}} {=} \operatorname{Cov}(g(A),f(A))/\operatorname{Var}(T)$ is the omitted-variable bias (Cauchy--Schwarz; Appendix~\ref{app:confounding}).
80	\emph{(b)}~Collider preserves sign when $|\tau| > \sqrt{\operatorname{Var}(g)\operatorname{Var}(h)}/\mathbb{E}[\operatorname{Var}(T{\mid}A)]$ (Berkson attenuation; Appendix~\ref{app:collider}); empirically verified across 100{,}000 matrices with zero violations.
81	\emph{(c)}~Exposure can produce sign reversal for $K {\geq} 3$, even with $C_{kk} {>} 0.5$ (counterexample in Appendix~\ref{app:exposure}).
82	\end{proposition}
83	
84	Sign preservation for non-exposure topologies holds under topology-specific conditions (Table~\ref{tab:sign_conditions}, Appendix~\ref{app:conditions}), verified across 100{,}000 random matrices with zero violations; analytic proofs for general $K$ remain open.
85	
86	\subsection{Annotation Sensitivity Values}
87	\label{sec:asv}
88	
89	We adapt the sensitivity analysis paradigm (E-values~\cite{vanderweele_ding2017}, partial-$R^2$ bounds~\cite{cinelli2020making}, coefficient stability~\cite{oster2019}) to $K{\times}K$ annotation error and define Annotation Sensitivity Values (ASVs): we prove $\varepsilon$-approximate monotonicity along $C(\delta)$ (Theorem~\ref{thm:monotone}), which reduces $K^2$ dimensions to a scalar; define three ASV diagnostics for topology-dependent failure modes; and combine ASVs with FWL invariance to route corrections.
90	
91	\paragraph{Parameterization.}
92	We set $C(\delta) = (1{-}\delta)I + \delta C_0$, where $C_0$ is a reference confusion matrix and $\delta \in [0,1]$ controls severity ($\delta{=}0$: perfect; $\delta{=}1$: matches $C_0$). This linear path is one of many in the column-stochastic polytope from $I$ to $C_0$; ASV thresholds are path-dependent, but our bootstrap procedure (Section~\ref{sec:asv_results}) captures estimation uncertainty along the empirical path. We recommend bootstrapping $C_0$ and reporting ASV confidence intervals (Appendix~\ref{sec:bootstrap_asv}).
93	\paragraph{Three ASV types.}
94	We define three complementary measures: (1)~\textbf{Magnitude ASV} $\delta^*_{\text{mag}} = \min\{\delta : |\operatorname{plim}\;\hat{\tau}(C(\delta)) - \tau| > \epsilon\}$, analogous to E-values; (2)~\textbf{Significance ASV} $\delta^*_{\text{sig}} = \min\{\delta : |\operatorname{plim}\;\hat{\tau}(C(\delta))| < z_{\alpha/2} \cdot SE(N)\}$, relevant for attenuating topologies; (3)~\textbf{Sign-flip ASV} $\delta^*_{\text{sf}} = \min\{\delta : \operatorname{sign}(\hat{\tau}) \neq \operatorname{sign}(\tau)\}$, for exposure and IV only. The significance ASV depends on $N$ through $SE(N)$, exhibiting a sharp phase transition at a critical $N^*$ below which all rejections are blocked.
95	
96	\begin{theorem}[Envelope monotonicity, $K{=}2$]
97	\label{thm:monotone}
98	For $K{=}2$ confounding and mediation topologies with proportional effects ($f = \lambda g$ for some scalar $\lambda$) under $C(\delta) = (1{-}\delta)I + \delta C_0$ with $(C_0)_{jj} \geq \tfrac{1}{2}$, $|B(C(\delta))|$ is monotonically non-decreasing in $\delta \in [0,1]$.
99	\end{theorem}
100	
101	The proof (Appendix~\ref{app:monotonicity_proof},~\ref{par:med_monotone}) exploits perspective function convexity. All 23 empirical configurations preserve sign; 97.3\% do so under non-proportional effects (Appendix~\ref{sec:proportional_effects}).
102	
103	\begin{theorem}[$K{=}3$ symmetric monotonicity]
104	\label{thm:k3_symmetric}
105	For $K{=}3$ with symmetric confusion matrix $C_{jk} = c$ for $j \neq k$ and $C_{kk} = 1{-}2c$, $c \in (0, 1/3)$, and proportional effects ($f{=}\lambda g$), envelope monotonicity holds exactly: $|B(C(\delta))|$ is strictly monotone in $\delta$ for confounding, mediation, and collider topologies whenever $\mathrm{Var}(g) > 0$.
106	\end{theorem}
107	
108	Theorem~\ref{thm:k3_symmetric} anchors exact monotonicity at $K{=}3$; for general asymmetric matrices ($d_{\mathrm{rel}}{=}0.33$; Remark~\ref{rem:symmetry}), Conjecture~\ref{conj:monotone} provides $\varepsilon < 0.017$ coverage. The proof exploits the reduction $s = c\delta$ (Appendix~\ref{app:k3_symmetric_proof}).
109	
110	\paragraph{From proofs to numerical evidence.}
111	Exact monotonicity (Theorems~\ref{thm:monotone}--\ref{thm:k3_symmetric}) does not extend to general $K{\geq}3$ column-stochastic structures; we state a conjecture supported by numerical evidence:
112	
113	\begin{conjecture}[$\varepsilon$-approximate envelope monotonicity]
114	\label{conj:monotone}
115	For general $K{\geq}3$ non-IV topologies under $C(\delta) = (1{-}\delta)I + \delta C_0$, $|B(C(\delta))|$ is $\varepsilon$-approximately monotonic with $\varepsilon < 0.02$ for $|\beta| \leq 1$, scaling with effect magnitude (Table~\ref{tab:conjecture_verify},~\ref{tab:dgp_sensitivity}; Appendix~\ref{sec:conjecture_verify}). The safe/fragile partition (five sign-preserving topologies versus exposure and IV) is robust across all tested parameterizations.
116	\end{conjecture}
117	
118	Numerical support spans 100{,}000 Dirichlet matrices and 545{,}945 adversarial curves (Appendix~\ref{app:adversarial_monotonicity}).
119	
120	\begin{remark}[ASV and E-values as complementary tools]
121	\label{rem:evalue}
122	ASV and E-values~\cite{vanderweele_ding2017} address orthogonal sources (annotation error vs.\ unmeasured confounding; Appendix~\ref{sec:sensitivity_comparison}) and are most valuable jointly.
123	\end{remark}
124	
125	Under alternating-sign effects ($\boldsymbol{\beta}{=}[0,\,1.0,\,-0.5]$), magnitude ASV ranges from 0.09 (exposure) to $\infty$ (M-bias), a $4{\times}$ difference determined by topology (Table~\ref{tab:asv_stability}). Sign-flip ASV $< 1$ flags sign-reversal-prone pairs; magnitude ASV $< \delta_{\text{observed}}$ indicates bias exceeds tolerance (Algorithm~\ref{alg:correction}); the safe/fragile partition is stable across parameterizations ($\varepsilon < 0.02$; Appendix~\ref{sec:asv_stability}).
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c361b2ec-3475-4925-b71c-9ed9d9eabdb0",
  "isSidechain": true,
  "promptId": "2270b57b-d325-458d-b789-f645f11c5c65",
  "agentId": "ad9c11a1a52b2a80e",
  "type": "user",
  "uuid": "1f683349-4c4b-4820-8ce9-38714fc8ccb1",
  "sourceToolAssistantUUID": "c361b2ec-3475-4925-b71c-9ed9d9eabdb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T16:07:27.505Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UXh4nBSTcUA2aRx9B8SSd8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f683349-4c4b-4820-8ce9-38714fc8ccb1",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaJin73Y8xTQWk4RXDk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ebafe07-fb57-4a21-a8f3-783092f506bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NP3RnwSrkW81PARdKXreqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37386,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37386,
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

_source line 10 · 2026-05-25T16:07:27.513Z_

<details><summary>↩ Tool result · `toolu_01UXh4nBSTcUA2aRx9B8SSd8`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Large language models (LLMs) are rapidly replacing human annotators in computational social science~\cite{gilardi2023chatgpt, ziems2024can, egami_hinck_stewart_wei2023, baumann2025}. Most tasks are inherently multi-class (stance detection: 3--4 categories, sentiment: 5, disaster response: 10+), and annotation errors propagate into downstream causal estimates in ways that depend on both error structure and causal design. \citet{baumann2025} show that 31\% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, with 60\% error correlation across models~\cite{kim_garg2025}. Standard metrics do not capture this risk: within $F_1$ 0.61--0.69, causal bias varies by an order of magnitude across topologies.
5	
6	The transition at $K{\geq}3$ is not gradual but structural. For $K{=}2$, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs, an algebraic property of the $2{\times}2$ matrix dimension~\cite{brenner1993}. This guarantee vanishes at $K{\geq}3$: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients; sign reversal can occur even under high accuracy~\cite{veirod_laake2001}. Under a uniform Dirichlet prior, 83.4\% of $K{=}3$ exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal $\geq 0.7$), 2.1\% still do. The primary treatment coefficient is never reversed under the tested $\beta$ configurations where a single category dominates ($\beta_1 \gg \beta_2$), an empirical regularity we discuss in Section~\ref{sec:method}.
7	
8	$F_1$ does not exhibit significant rank correlation with causal bias ($\rho = -0.10$, $p = 0.45$ across 56 HumAID scenarios; bias varies $>$10${\times}$ (from $<$6\% to 42.1\%) within $F_1$ 0.614--0.690). Prior work noted polytomous sign reversal~\cite{dosemeci1990, veirod_laake2001} and confounder amplification~\cite{brenner1993}, but covered at most one topology~\cite{lee_wood_doughty2024}. We present the first systematic analysis jointly addressing multi-class ($K{\geq}3$) misclassification across seven directed acyclic graph (DAG) topologies, with analytical predictions matching Monte Carlo within 1.6\% MAPE across 161 scenarios.
9	
10	We address these gaps with three contributions:
11	
12	\begin{enumerate}
13	\item \textbf{Multi-class bias taxonomy.} We derive bias expressions for seven canonical DAG topologies\footnote{These span the four structural roles of the annotated variable: treatment (exposure), outcome-side covariate (confounding, mediation, M-bias, front-door), selection variable (collider), and instrumental variable (IV).} (Figure~\ref{fig:dag_taxonomy}) under $K$-class non-differential misclassification and establish a sign-preservation/reversal dichotomy: five topologies preserve the treatment effect sign under topology-specific regularity conditions (Proposition~\ref{prop:signflip}), while exposure and IV can reverse it.
14	
15	\item \textbf{Annotation Sensitivity Values.} We define three ASV diagnostics (magnitude, significance, and sign-flip) with proved envelope monotonicity (Theorems~\ref{thm:monotone},~\ref{thm:k3_symmetric}) and $\varepsilon$-approximate monotonicity for general $K{\geq}3$ (Conjecture~\ref{conj:monotone}). This reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune).
16	
17	\item \textbf{Topology-aware correction routing.} Frisch--Waugh--Lovell (FWL) invariance renders matrix-based corrections provably ineffective for four topologies (confounding, mediation, collider, M-bias). We evaluate five correction methods and provide a topology-aware decision procedure (Algorithm~\ref{alg:correction}, Appendix), validated with real LLM confusion matrices.
18	\end{enumerate}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ebafe07-fb57-4a21-a8f3-783092f506bb",
  "isSidechain": true,
  "promptId": "2270b57b-d325-458d-b789-f645f11c5c65",
  "agentId": "ad9c11a1a52b2a80e",
  "type": "user",
  "uuid": "81d5e775-ddb0-440e-9c24-34173ea52b9f",
  "sourceToolAssistantUUID": "1ebafe07-fb57-4a21-a8f3-783092f506bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T16:07:27.567Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BwFNk1qx8NZq1ZLS67yG4T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81d5e775-ddb0-440e-9c24-34173ea52b9f",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaJin73Y8xTQWk4RXDk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4a7e3b3e-3d27-46af-8b75-41738c3ea3bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NP3RnwSrkW81PARdKXreqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37386,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37386,
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

_source line 12 · 2026-05-25T16:07:27.574Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KcyzeUqxEo8pTWvodSCLvC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a7e3b3e-3d27-46af-8b75-41738c3ea3bd",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaJin73Y8xTQWk4RXDk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "415a60b4-5844-488d-a697-fb2e060a9150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NP3RnwSrkW81PARdKXreqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37386,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37386,
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

_source line 13 · 2026-05-25T16:07:27.586Z_

<details><summary>↩ Tool result · `toolu_01BwFNk1qx8NZq1ZLS67yG4T`</summary>

```text
1	\begin{abstract}
2	When large language model (LLM)-generated annotations feed into causal inference, annotation quality alone is insufficient to assess causal validity; the causal directed acyclic graph (DAG) topology determines whether errors attenuate, amplify, or reverse the treatment effect estimate. We derive bias expressions for seven canonical topologies under $K$-class non-differential misclassification in linear structural equation models and show that $K {\geq} 3$ introduces a structural possibility of sign reversal absent in the binary case. Under proportional effects, five topologies preserve the treatment effect sign under regularity conditions; exposure and instrumental variable (IV) can reverse it. Under empirical LLM confusion matrices, sign reversal is confined to exposure topology. We introduce Annotation Sensitivity Values (ASVs), with proved ($K{=}2$, $K{=}3$ symmetric) and extensively validated (general $K{\geq}3$) monotonicity that yields a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch--Waugh--Lovell invariance. A case study with 10 real LLM confusion matrices confirms: topology-aware correction reduces exposure bias from ${\sim}$61\% to ${<}$1\%, while topology-blind corrections are provably futile under linear regression for four topologies\footnote{Code and data are available at \url{https://anonymous.4open.science/r/causal_annot_error_attrib-C146/}.}.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a7e3b3e-3d27-46af-8b75-41738c3ea3bd",
  "isSidechain": true,
  "promptId": "2270b57b-d325-458d-b789-f645f11c5c65",
  "agentId": "ad9c11a1a52b2a80e",
  "type": "user",
  "uuid": "cde804ee-b456-4638-930c-d4020313d927",
  "sourceToolAssistantUUID": "4a7e3b3e-3d27-46af-8b75-41738c3ea3bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T16:07:27.882Z_

<details><summary>↩ Tool result · reported error · `toolu_01KcyzeUqxEo8pTWvodSCLvC`</summary>

```text
File content (46247 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "415a60b4-5844-488d-a697-fb2e060a9150",
  "isSidechain": true,
  "promptId": "2270b57b-d325-458d-b789-f645f11c5c65",
  "agentId": "ad9c11a1a52b2a80e",
  "type": "user",
  "uuid": "6d581c13-1ee7-48a6-9c66-66c493ba7a0c",
  "toolUseResult": "Error: File content (46247 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "415a60b4-5844-488d-a697-fb2e060a9150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-25T16:07:29.785Z_

The appendix_proofs.tex file is too large to read in one go. Let me read it in sections to extract the structure you need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d581c13-1ee7-48a6-9c66-66c493ba7a0c",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaJyVdVA9SzsqTi7nRr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bbe51af3-0de5-4942-aad5-806ed4603dad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01458L2tyBtNaGQxuCbj9baP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11814,
      "cache_read_input_tokens": 37386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11814,
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

_source line 16 · 2026-05-25T16:07:30.283Z_

<details open><summary>🔧 Tool call — Read · `toolu_018w77inhU9vPhVaQAuRg8P8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "limit": 1000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbe51af3-0de5-4942-aad5-806ed4603dad",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaJyVdVA9SzsqTi7nRr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe3885a3-71a4-443d-96a1-a81e7dbf3745",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01458L2tyBtNaGQxuCbj9baP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11814,
      "cache_read_input_tokens": 37386,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11814
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 142,
          "cache_read_input_tokens": 37386,
          "cache_creation_input_tokens": 11814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11814,
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

_source line 17 · 2026-05-25T16:07:30.556Z_

<details><summary>↩ Tool result · reported error · `toolu_018w77inhU9vPhVaQAuRg8P8`</summary>

```text
File content (29274 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe3885a3-71a4-443d-96a1-a81e7dbf3745",
  "isSidechain": true,
  "promptId": "2270b57b-d325-458d-b789-f645f11c5c65",
  "agentId": "ad9c11a1a52b2a80e",
  "type": "user",
  "uuid": "ede1b860-6e55-484f-b17e-190e05c455cb",
  "toolUseResult": "Error: File content (29274 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "fe3885a3-71a4-443d-96a1-a81e7dbf3745",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-25T16:07:31.952Z_

Let me search for just the section headings in the appendix file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ede1b860-6e55-484f-b17e-190e05c455cb",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaKAhKuFVw7vEHhkntS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "edf21307-1f68-443b-96c8-e4f2ca4a4799",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018ZPmNY1V23JPsEDTXPASij",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 49200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 203,
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

_source line 19 · 2026-05-25T16:07:32.516Z_

<details open><summary>🔧 Tool call — Grep · `toolu_018S8BqcFBXhhMJm4rriiLjU`</summary>

```json
{
  "pattern": "^\\\\(section|subsection|subsubsection|begin\\{(table|figure)\\})",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edf21307-1f68-443b-96c8-e4f2ca4a4799",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaKAhKuFVw7vEHhkntS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b8d872e5-8898-40ce-8a01-e9df984a0e7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018ZPmNY1V23JPsEDTXPASij",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 49200,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 203
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 164,
          "cache_read_input_tokens": 49200,
          "cache_creation_input_tokens": 203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 203,
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

_source line 20 · 2026-05-25T16:07:32.545Z_

<details><summary>↩ Tool result · `toolu_018S8BqcFBXhhMJm4rriiLjU`</summary>

```text
1:\section{Proofs of Proposition~\ref{prop:signflip} and Theorem~\ref{thm:monotone}}
8:\subsection{Notation and Key Identities}
20:\subsection{Frisch--Waugh--Lovell Decomposition}
70:\subsection{Confounding Topology ($A$ = Confounder)}
242:\subsection{Proof of Theorem~\ref{thm:monotone} (Confounding Monotonicity)}
330:\subsection{Mediation Topology ($A$ = Mediator)}
516:\subsection{Proof of Theorem~\ref{thm:k3_symmetric} ($K{=}3$ Symmetric Monotonicity)}
526:\subsection{Collider Topology ($A$ = Collider)}
625:\subsection{Front-door Topology ($A$ = Mediator under Confounding)}
694:\subsection{Exposure Topology: Sign Reversal Counterexample}
761:\subsection{Summary of Conditions}
768:\begin{table}[H]
805:\subsection{Adversarial Monotonicity Verification}
812:\begin{table}[H]
833:\section{Supplementary Tables, Figures, and Algorithm}
836:\subsection{Binarization Collapse}
846:\begin{table}[H]
877:\begin{table}[H]
934:\subsection{Proof of FWL Invariance}
945:\begin{table}[H]
969:\subsection{Applied Illustration: ClinicalBERT Case Study}
980:\subsection{IV Wald Estimator: Diagonal-Dominance Subspaces}
992:\begin{table}[H]
1011:\subsection{Non-Differential Misclassification Verification}
1022:\subsection{Non-Differential Assumption Stress Test}
1029:\begin{table}[H]
1059:\subsection{Robustness to Nonlinear DGP}
1083:\subsection{Bootstrap Uncertainty of ASV}
1110:\subsection{Cross-$K$ Robustness}
1115:\subsection{ASV Diagnostic Results}
1122:\subsection{ASV Stability Across DGP Parameters}
1133:\subsection{Extended Conjecture Verification}
1140:\begin{table}[H]
1166:\begin{table}[H]
1189:\subsection{Proportional Effects Breakdown}
1196:\begin{table}[H]
1218:\subsection{FWL Invariance Under Nonlinear Models}
1225:\begin{table}[H]
1249:\subsection{PPI++ Gold Label Ratio Sensitivity}
1256:\begin{table}[H]
1275:\subsection{Realistic Differential Misclassification Thresholds}
1282:\begin{table}[H]
1299:\subsection{Proportional Effects with Empirical Confusion Matrices}
1306:\begin{table}[H]
1325:\subsection{Case Study: ASV Diagnosis of Political Ad Tone Classification}
1344:\subsection{End-to-End Demonstration}
1351:\subsection{Semi-Real Case Study with Production LLM Confusion Matrices}
1358:\subsection{Correction Method Sensitivity to $K$}
1371:\begin{table}[H]
1391:\subsection{Comparison with Related Sensitivity Frameworks}
1394:\begin{table}[H]
1413:\subsection{Per-Topology $F_1$--Bias Correlation}
1420:\begin{table}[H]
1442:\subsection{Confusion Matrix Estimation Robustness}
1449:\begin{table}[H]
1468:\subsection{Sign Reversal Determinants}
1475:\begin{table}[H]
1493:\subsection{Y-Stratified Non-Differential Verification}
1500:\begin{table}[H]
1518:\section{Notation}
1521:\begin{table}[H]
1544:\section{Use of AI Assistants}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8d872e5-8898-40ce-8a01-e9df984a0e7f",
  "isSidechain": true,
  "promptId": "2270b57b-d325-458d-b789-f645f11c5c65",
  "agentId": "ad9c11a1a52b2a80e",
  "type": "user",
  "uuid": "206d7917-32d5-4f00-8717-56dac22b287e",
  "sourceToolAssistantUUID": "b8d872e5-8898-40ce-8a01-e9df984a0e7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-25T16:07:34.260Z_

Perfect! Now let me get the table captions from the appendix to see what supplementary material is there.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "206d7917-32d5-4f00-8717-56dac22b287e",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaKKKjgNixXmT8g5gLG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "86baf828-eea8-4319-9b95-0d6e6e2d2111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F7ssZ9adgnSk52jEswpVV3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1165,
      "cache_read_input_tokens": 49403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1165,
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

_source line 22 · 2026-05-25T16:07:35.015Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DjmoFFsehCoAvqj3brwKX4`</summary>

```json
{
  "command": "grep -A 2 \"\\\\\\\\caption{\" /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/appendix_proofs.tex | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86baf828-eea8-4319-9b95-0d6e6e2d2111",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaKKKjgNixXmT8g5gLG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cd489c76-3b84-49bb-b7fe-0c7f9649af80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F7ssZ9adgnSk52jEswpVV3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1165,
      "cache_read_input_tokens": 49403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1165,
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

_source line 23 · 2026-05-25T16:07:35.211Z_

<details><summary>↩ Tool result · `toolu_01DjmoFFsehCoAvqj3brwKX4`</summary>

```text
\caption{Sufficient conditions for sign preservation under non-differential misclassification.}
\label{tab:sign_conditions}
\end{table}
--
\caption{Adversarial monotonicity test across $K{=}3,5,7$ and seven topologies.}
\label{tab:adversarial_monotonicity}
\resizebox{\columnwidth}{!}{\begin{tabular}{lcc}
--
\caption{ASV type applicability and sensitivity across DAG topologies.}
\label{tab:asv_grid}
\small
--
\caption{ASV magnitude ranges across topologies for HumAID ($K{=}10$). Left: magnitude ASV ($\delta^*$) range across 8 LLM configurations; lower values indicate greater fragility. ``Safe'' topologies never exceed the 10\% bias threshold. Right: percentage of configurations flagged as ASV-unsafe.}
\label{fig:asv_heatmap}
\end{figure*}
--
\caption{RMSE reduction (\%) by correction method and DAG topology.}
\label{tab:correction}
\resizebox{\columnwidth}{!}{\begin{tabular}{lccccc}
--
\caption{Correction method selection for LLM-annotated causal inference.}
\label{alg:correction}
\footnotesize
--
\caption{FWL invariance under OLS vs.\ breakdown under logistic regression.}
\label{tab:fwl_logistic}
\resizebox{\columnwidth}{!}{\begin{tabular}{lcccc}
--
\caption{IV Wald estimator bias by minimum-diagonal subspace.}
\label{tab:iv_dirichlet_subspace}
\small
--
\caption{Effect of differential misclassification on bias violation rates.}
\label{tab:nondiff_stress}
\resizebox{\columnwidth}{!}{\begin{tabular}{cccc}
--
\caption{Bootstrap distribution of magnitude ASV $\delta^*$ ($B{=}1{,}000$) for HumAID DeepSeek zero-shot ($K{=}10$). Dashed line: point estimate; shaded: 95\% CI.}
\label{fig:bootstrap_asv}
\end{figure*}
--
\caption{Envelope monotonicity violations per 10{,}000 random $C_0$ matrices.}
\label{tab:conjecture_verify}
\resizebox{\columnwidth}{!}{\begin{tabular}{lccccc}
--
\caption{DGP parameter sensitivity of envelope monotonicity violations.}
\label{tab:conjecture_tau_sens}
\resizebox{\columnwidth}{!}{\begin{tabular}{lccccc}
--
\caption{$\lambda(C)$ out-of-bounds rate and mediation sign failure rate.}
\label{tab:proportional_effects}
\resizebox{\columnwidth}{!}{\begin{tabular}{lcc}
--
\caption{Mean logistic bias reduction (\%) from matrix-based correction.}
\label{tab:fwl_nonlinear}
\resizebox{\columnwidth}{!}{\begin{tabular}{lccc}
--
\caption{PPI++ RMSE reduction (\%) vs.\ gold label fraction.}
\label{tab:ppi_gold_ratio}
\resizebox{\columnwidth}{!}{\begin{tabular}{lccccc}
--
\caption{Safe differential misclassification thresholds $\varepsilon^*_{\text{safe}}$ by dataset/$K$.}
\label{tab:realistic_epsilon}
\resizebox{\columnwidth}{!}{\begin{tabular}{lccccc}
--
\caption{Proportional effects validation with 23 real LLM confusion matrices.}
\label{tab:proportional_empirical}
\resizebox{\columnwidth}{!}{\begin{tabular}{lcccc}
--
\caption{Top correction method and RMSE reduction (\%) by topology across $K$.}
\label{tab:correction_k}
\resizebox{\columnwidth}{!}{\begin{tabular}{lccc}
--
\caption{Comparison of sensitivity frameworks.}
\label{tab:sensitivity_comparison}
\resizebox{\columnwidth}{!}{\begin{tabular}{lccc}
--
\caption{Within-topology Spearman $\rho(F_1, |\text{bias}|)$ across LLM configurations.}
\label{tab:within_topo_f1}
\begin{tabular}{lccc}
--
\caption{$\hat{C}$ estimation robustness: partition stability and ASV ranking correlation.}
\label{tab:c_robustness}
\begin{tabular}{lccc}
--
\caption{Sign reversal rates by $K$ and best single-feature decision rule.}
\label{tab:sign_determinants}
\begin{tabular}{lcc}
--
\caption{Y-stratified non-differential test.}
\label{tab:y_stratified}
\resizebox{\columnwidth}{!}{\begin{tabular}{lccc}
--
\caption{Key notation used throughout the paper.}
\label{tab:notation}
\resizebox{\columnwidth}{!}{\begin{tabular}{cl}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd489c76-3b84-49bb-b7fe-0c7f9649af80",
  "isSidechain": true,
  "promptId": "2270b57b-d325-458d-b789-f645f11c5c65",
  "agentId": "ad9c11a1a52b2a80e",
  "type": "user",
  "uuid": "e903e18c-fd65-4676-81fa-9eafa57a4de4",
  "sourceToolAssistantUUID": "cd489c76-3b84-49bb-b7fe-0c7f9649af80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-25T16:09:01.328Z_

Excellent! Now I have all the information I need. Let me compile the comprehensive summary for you.

---

## Paper Content Summary

### 1. ABSTRACT (Full Text)

When large language model (LLM)-generated annotations feed into causal inference, annotation quality alone is insufficient to assess causal validity; the causal directed acyclic graph (DAG) topology determines whether errors attenuate, amplify, or reverse the treatment effect estimate. We derive bias expressions for seven canonical topologies under K-class non-differential misclassification in linear structural equation models and show that K ≥ 3 introduces a structural possibility of sign reversal absent in the binary case. Under proportional effects, five topologies preserve the treatment effect sign under regularity conditions; exposure and instrumental variable (IV) can reverse it. Under empirical LLM confusion matrices, sign reversal is confined to exposure topology. We introduce Annotation Sensitivity Values (ASVs), with proved (K=2, K=3 symmetric) and extensively validated (general K≥3) monotonicity that yields a vulnerability ranking from IV (maximally fragile) to M-bias (immune), and show that matrix-based corrections are provably ineffective under linear regression for four topologies due to Frisch–Waugh–Lovell invariance. A case study with 10 real LLM confusion matrices confirms: topology-aware correction reduces exposure bias from ~61% to <1%, while topology-blind corrections are provably futile under linear regression for four topologies.

---

### 2. INTRODUCTION (Full Text)

Large language models (LLMs) are rapidly replacing human annotators in computational social science. Most tasks are inherently multi-class (stance detection: 3–4 categories, sentiment: 5, disaster response: 10+), and annotation errors propagate into downstream causal estimates in ways that depend on both error structure and causal design. 31% of hypotheses yield incorrect conclusions with state-of-the-art LLMs, with 60% error correlation across models. Standard metrics do not capture this risk: within F1 0.61–0.69, causal bias varies by an order of magnitude across topologies.

The transition at K≥3 is not gradual but structural. For K=2, the stochastic constraint forces any confusion matrix with positive diagonal to preserve coefficient signs, an algebraic property of the 2×2 matrix dimension. This guarantee vanishes at K≥3: the higher-dimensional confusion matrix admits negative effective weights on categories with opposite-sign coefficients; sign reversal can occur even under high accuracy. Under a uniform Dirichlet prior, 83.4% of K=3 exposure confusion matrices produce sign reversal of at least one secondary coefficient; under realistic accuracy (diagonal ≥ 0.7), 2.1% still do. The primary treatment coefficient is never reversed under the tested β configurations where a single category dominates (β₁ >> β₂), an empirical regularity discussed in Section 3.

F1 does not exhibit significant rank correlation with causal bias (ρ = -0.10, p = 0.45 across 56 HumAID scenarios; bias varies >10× (from <6% to 42.1%) within F1 0.614–0.690). Prior work noted polytomous sign reversal and confounder amplification, but covered at most one topology. This paper presents the first systematic analysis jointly addressing multi-class (K≥3) misclassification across seven directed acyclic graph (DAG) topologies, with analytical predictions matching Monte Carlo within 1.6% MAPE across 161 scenarios.

**Three contributions:**

1. **Multi-class bias taxonomy.** Derive bias expressions for seven canonical DAG topologies under K-class non-differential misclassification and establish a sign-preservation/reversal dichotomy: five topologies preserve the treatment effect sign under topology-specific regularity conditions (Proposition 1), while exposure and IV can reverse it.

2. **Annotation Sensitivity Values.** Define three ASV diagnostics (magnitude, significance, and sign-flip) with proved envelope monotonicity (Theorems 1–2) and ε-approximate monotonicity for general K≥3 (Conjecture 1). This reveals a vulnerability spectrum from IV (maximally fragile) to M-bias (immune).

3. **Topology-aware correction routing.** Frisch–Waugh–Lovell (FWL) invariance renders matrix-based corrections provably ineffective for four topologies (confounding, mediation, collider, M-bias). Evaluate five correction methods and provide a topology-aware decision procedure (Algorithm, Appendix), validated with real LLM confusion matrices.

---

### 3. METHOD (Full Text)

**Setup and Notation**

Let A denote a true K-class categorical variable (e.g., sentiment with K=3 levels) and A* its observed, potentially misclassified version produced by an LLM annotator. The misclassification process is characterized by a K×K confusion matrix C with entries C_jk = P(A*=j | A=k), where each column sums to one (column-stochastic: each column gives the distribution of predicted labels for a given true label). Following prior work, represent this measurement process using starred-node DAGs: the true variable A is latent, and the observed A* is connected to A via a dashed measurement edge.

**Notation conventions.** Analysis characterizes probability limits (N → ∞) under the FWL theorem, which explains why matrix-based corrections fail for covariate topologies. Notation is collected in Table (Appendix).

**Non-differential misclassification [Definition]:** Misclassification of A is non-differential with respect to outcome Y and covariates Z if P(A*=j | A=k, Y, Z) = P(A*=j | A=k) = C_jk for all j,k.

In batch annotation pipelines, the LLM processes each text independently without access to Y, making non-differentiality an architectural invariant; Y-stratified permutation tests confirm this (1/12 rejection at α=0.05). Non-differentiality may be violated when Y correlates with text content, in which case Y-stratified tests provide empirical verification. Under stress testing, sign reversal occurs in 14/16 K≥3 exposure configurations at η=0.01 structured departure.

Throughout, τ denotes the causal estimand of interest, whose definition varies by topology: the confounder's coefficient, the treatment effect, the indirect effect, or the Wald ratio (Appendix).

Study seven canonical DAG topologies (Figure), deriving probability limits under linear structural equation models (SEMs); logistic regression robustness is verified in Appendix.

**Multi-Class Bias Expressions**

For each topology, derive the plim (probability limit) of the naive estimator that substitutes A* for A. Let τ denote the target causal parameter, whose precise definition is topology-specific (e.g., the coefficient on X for confounding, the category-specific β_j for exposure, or the direct effect τ_direct for mediation), and τ̂(A*) the estimator using misclassified annotations.

**Confounding (A = confounder).** When A confounds the X→Y relationship, the OLS estimator controlling for A* has probability limit plim τ̂(A*) = (E[Z'Z])^{-1}E[Z'X]β, where Z = [X, dummies(A*)], β contains the true coefficients, and the target parameter τ is the coefficient on X. Misclassification produces residual confounding that monotonically approaches the omitted variable bias, but the sign of τ̂ is preserved: τ_sign_flip = 0 structurally. (Consistent with prior work: misclassification degrades confounding control, producing amplification (|τ̂| > |τ|, universal in this topology) but never sign reversal.)

**Exposure (A = treatment variable).** When A is the exposure of interest, the biased coefficient for category j becomes a weighted combination of true coefficients: plim β̂_j(A*) = Σ_k w_jk β_k, where w_jk depends on the confusion matrix C and the population marginal π_k = P(A=k). Unlike binary misclassification, K≥3 permits w_jk to assign negative weight to categories with opposite-sign coefficients, producing sign reversal (83.4% under uniform Dirichlet prior); this is structurally impossible at K=2.

**Primary coefficient preservation.** Across 23 empirical LLM configurations, the primary coefficient (the category with the largest true effect |β_k|) never reverses sign, while 61% reverse a secondary (non-dominant) coefficient, confirmed under 100,000 Dirichlet matrices with diagonal ≥ 0.7 across six beta-ratio conditions (1.0 to 50.0) with 0% primary sign-flip.

**Mediation (A = mediator).** When A mediates the X→Y relationship, the direct effect estimator controlling for A* has probability limit plim τ̂_direct(A*) = τ_direct + (1 - λ(C)) τ_indirect, where λ(C) ∈ [0,1] under proportional effects, with λ(I) = 1 under perfect classification. Misclassification (λ < 1) causes the residual indirect effect to be absorbed into the direct path estimate, producing upward bias in |τ̂_direct| but preserving the sign (τ_sign_flip = 0).

**Collider, M-bias, and front-door.** Three topologies exhibit protective or immune behavior. **Collider:** conditioning on A* instead of A attenuates Berkson bias by weakening the spurious path, so annotation error is protective (τ_sign_flip = 0). **M-bias:** in the M-shaped DAG, misclassifying A attenuates the non-causal path, making this topology immune (ASV = ∞). **Front-door:** the front-door estimator requires two stages (X → A and A → Y), each attenuated by C; the compound effect produces moderate bias with τ_sign_flip = 0.

**Instrumental variable (A = instrument).** The Wald estimator τ̂_IV = ĉov(A*, Y) / ĉov(A*, X) has C in the denominator. Misclassification can drive first-stage coefficients toward zero or reverse their sign; under random Dirichlet matrices, 52.6% produce sign reversal; IV is the most fragile topology.

**Structural sign-flip guarantee [Proposition 1]:** Under non-differential misclassification with C_kk > 0 for all k:
- **(a)** Confounding preserves sign when sign(τ) = sign(τ + B_OV), where B_OV = Cov(g(A),f(A))/Var(T) is the omitted-variable bias (Cauchy–Schwarz; Appendix).
- **(b)** Collider preserves sign when |τ| > √(Var(g)Var(h))/E[Var(T|A)] (Berkson attenuation; Appendix); empirically verified across 100,000 matrices with zero violations.
- **(c)** Exposure can produce sign reversal for K ≥ 3, even with C_kk > 0.5 (counterexample in Appendix).

Sign preservation for non-exposure topologies holds under topology-specific conditions, verified across 100,000 random matrices with zero violations; analytic proofs for general K remain open.

**Annotation Sensitivity Values**

Adapt the sensitivity analysis paradigm (E-values, partial-R² bounds, coefficient stability) to K×K annotation error and define Annotation Sensitivity Values (ASVs): prove ε-approximate monotonicity along C(δ) (Theorem), which reduces K² dimensions to a scalar; define three ASV diagnostics for topology-dependent failure modes; and combine ASVs with FWL invariance to route corrections.

**Parameterization.** Set C(δ) = (1−δ)I + δC₀, where C₀ is a reference confusion matrix and δ ∈ [0,1] controls severity (δ=0: perfect; δ=1: matches C₀). This linear path is one of many in the column-stochastic polytope from I to C₀; ASV thresholds are path-dependent, but bootstrap procedure (Section 4) captures estimation uncertainty along the empirical path. Recommend bootstrapping C₀ and reporting ASV confidence intervals.

**Three ASV types.** Define three complementary measures:
1. **Magnitude ASV** δ*_mag = min{δ : |plim τ̂(C(δ)) − τ| > ε}, analogous to E-values;
2. **Significance ASV** δ*_sig = min{δ : |plim τ̂(C(δ))| < z_{α/2} · SE(N)}, relevant for attenuating topologies;
3. **Sign-flip ASV** δ*_sf = min{δ : sign(τ̂) ≠ sign(τ)}, for exposure and IV only.

The significance ASV depends on N through SE(N), exhibiting a sharp phase transition at a critical N* below which all rejections are blocked.

**[Theorem 1 - Envelope monotonicity, K=2]** For K=2 confounding and mediation topologies with proportional effects (f = λg for some scalar λ) under C(δ) = (1−δ)I + δC₀ with (C₀)_jj ≥ 1/2, |B(C(δ))| is monotonically non-decreasing in δ ∈ [0,1].

The proof exploits perspective function convexity. All 23 empirical configurations preserve sign; 97.3% do so under non-proportional effects.

**[Theorem 2 - K=3 symmetric monotonicity]** For K=3 with symmetric confusion matrix C_jk = c for j ≠ k and C_kk = 1−2c, c ∈ (0, 1/3), and proportional effects (f=λg), envelope monotonicity holds exactly: |B(C(δ))| is strictly monotone in δ for confounding, mediation, and collider topologies whenever Var(g) > 0.

Theorem 2 anchors exact monotonicity at K=3; for general asymmetric matrices, Conjecture provides ε < 0.017 coverage. The proof exploits the reduction s = cδ.

**From proofs to numerical evidence.** Exact monotonicity does not extend to general K≥3 column-stochastic structures; state a conjecture supported by numerical evidence:

**[Conjecture 1 - ε-approximate envelope monotonicity]** For general K≥3 non-IV topologies under C(δ) = (1−δ)I + δC₀, |B(C(δ))| is ε-approximately monotonic with ε < 0.02 for |β| ≤ 1, scaling with effect magnitude (Tables; Appendix). The safe/fragile partition (five sign-preserving topologies versus exposure and IV) is robust across all tested parameterizations.

Numerical support spans 100,000 Dirichlet matrices and 545,945 adversarial curves.

**[Remark - ASV and E-values as complementary tools]** ASV and E-values address orthogonal sources (annotation error vs. unmeasured confounding; Appendix) and are most valuable jointly.

Under alternating-sign effects (β=[0, 1.0, −0.5]), magnitude ASV ranges from 0.09 (exposure) to ∞ (M-bias), a 4× difference determined by topology. Sign-flip ASV < 1 flags sign-reversal-prone pairs; magnitude ASV < δ_observed indicates bias exceeds tolerance (Algorithm); the safe/fragile partition is stable across parameterizations (ε < 0.02).

---

### 4. EXPERIMENTS (Full Text)

Validate through Monte Carlo simulation (K=3), cross-K robustness checks (K=5,7), and empirical validation with real LLM confusion matrices from three natural language processing (NLP) tasks (K=2,3,10).

**Setup.** For each topology, sample 100,000 confusion matrices from a Dirichlet(1,1,1) prior, compute analytical probability limits, and validate against Monte Carlo simulation (N=10,000). ASV experiments use C(δ) = (1−δ)I + δC₀.

**Bias Taxonomy**

Shows Table with taxonomy results: **Confounding:** 100% violation, 0% sign flip, 100% amplification, conditional sign-flip guarantee. **Exposure:** 85% violation, 83.4% sign flip, 14.1% amplification, no guarantee. **Mediation:** 100% violation, 0% sign flip, 100% amplification, conditional guarantee. **Front-door:** 100% violation, 0% sign flip, 100% amplification, conditional guarantee. **Collider:** 100% violation, 0% sign flip, 100% amplification, conditional guarantee. **M-bias:** 53.2% violation, 0% sign flip, 10.4% amplification, yes (guaranteed). **IV:** 100% violation, 52.6% sign flip, 100% amplification, no guarantee.

**Theory-MC agreement.** Analytical probability limits match Monte Carlo estimates with mean absolute percentage error (MAPE) of 1.6%, averaged across 161 scenarios (23 LLM configurations × 7 topologies; per-topology range: 0.3%–3.7%), validating the closed-form derivations and justifying probability limits as practical bias diagnostics.

**Exposure DAG: sign reversal under multi-class misclassification.** Under realistic accuracy (diagonal ≥ 0.7), the violation rate is 13.7% with 2.1% sign reversal; at diagonal ≥ 0.9, violation persists at 11.9%. Under the full Dirichlet prior, 85% of matrices violate the binary "toward-null" guarantee and 83.4% cause sign reversal; min_k C_kk < 0.55 predicts sign reversal with 91% accuracy. The K=2 control confirms classical attenuation. This establishes the multi-class failure as structurally distinct.

**Structural guarantee for non-exposure topologies.** Five topologies exhibit zero sign-flip rate: confounding, mediation, and front-door show 100% amplification but never reverse the sign; collider is protective (|B(C)| non-increasing; Conjecture); M-bias shows weakest sensitivity (53.2% violation). All patterns persist at K=5,7.

**IV: Wald estimator instability.** The IV topology is the sole non-exposure exception: 52.6% of random matrices cause sign reversal, stable across K=3,5,7. Diagonal dominance (C_kk > 0.5) eliminates sign reversal but preserves amplification; however, all 23 empirical LLM configurations show zero IV sign reversal.

Figure overlays all 23 empirical LLM configurations onto the theoretical violation-rate curves; real-world accuracy (min_k C_kk ≥ 0.6) places all models in the low-risk region for IV but leaves exposure vulnerable.

**ASV Framework Validation**

Table shows ASV summary across topologies (K=3, τ=0.5): **IV:** magnitude ASV 0.10–0.61, power 0%, sign-flip 1.1–6.7. **Front-door:** magnitude ASV 0.06–0.39, power 100%, sign-flip N/A. **Confounding:** magnitude ASV 0.08–0.49, power 100%, sign-flip N/A. **Mediation:** magnitude ASV 0.08–0.45, power 0%, sign-flip N/A. **Collider:** magnitude ASV 0.34–2.03, power 0%, sign-flip N/A. **M-bias:** magnitude ASV ∞, power 98%, sign-flip N/A. **Exposure:** magnitude ASV N/A, power N/A, sign-flip 83.4%.

**ASV results.** The ASV envelope is ε-approximately monotonic (ε < 0.02; Conjecture); IV is maximally fragile, M-bias is immune (ASV = ∞; Figure). Sign-flip ASV: 83.4% of exposure matrices yield δ*_sf < 1; IV ranges 1.1–6.7. Significance ASV exhibits a phase transition at N* ≈ 6,000–10,000; bootstrap CIs confirm stable topology ranking, with the safe/fragile partition recovering from n_gold ≥ 100 (82% stability).

**Empirical Validation**

Validate using real LLM confusion matrices from HumAID (K=10), VAST (K=3), and CivilComments (K=2): four LLMs, 23 configurations, 161 bias scenarios. HumAID (K=10) matches predictions: IV (12.4–42.1%) and exposure (9.0–17.4%) dominate; remaining topologies <15%. F1 does not exhibit significant rank correlation with bias (ρ = -0.10, p = 0.45; Figure), but per-topology patterns diverge (ρ ≤ -0.53 for five topologies vs. 0.87 for M-bias). Of exposure coefficients, 14/23 (61%) exhibit sign reversal, all secondary; zero across 138 non-exposure scenarios.

**Figure:** Topology determines downstream causal bias, not F1. HumAID K=10 (56 points): within F1 range 0.614–0.690, bias varies 10× (IV 42.1% vs. collider <5.6%).

**Correction Guidance**

Evaluate five correction methods (naive plug-in, maximum likelihood adjustment (MLA), design-based supervised learning (DSL), Monte Carlo simulation extrapolation (MC-SIMEX), PPI++) across all topologies (210 configurations; Table, Appendix).

**FWL invariance.** Under linear regression, FWL invariance renders matrix-based methods (naive plug-in, MLA) provably ineffective for covariate topologies (0% bias reduction): the treatment coefficient depends only on the projection orthogonal to the covariate space, so relabeling A* → A leaves the coefficient unchanged. Under logistic regression this invariance breaks, but the method ranking persists (|Δ| < 0.02).

**Figure:** Binarization collapse Δ: additional bias from collapsing K=3 to binary. Topology determines severity (>150× range); exposure and IV exhibit sign flips.

**Method ranking and decision procedure.** PPI++ achieves the highest root mean squared error (RMSE) reduction (47.0% at K=3) but requires gold labels and harms M-bias (−88%); MC-SIMEX is gold-free and K-robust (27–70%), though it harms front-door (−62.4%); rankings are stable across K (ρ ≥ 0.80). Algorithm (Appendix) routes through risk assessment, method selection, and FWL screening. End-to-end demos validate: PPI++ reduces exposure bias from 42.9% to 0.2%, while topology-agnostic IV correction amplifies bias (−139%). Collapsing K=3 to binary is not a safe fallback: the additional bias Δ varies >150× by topology (Figure).

---

### 5. CONCLUSION (Full Text)

We characterized how multi-class annotation errors interact with causal DAG topology: at K≥3, exposure and IV can reverse treatment effect signs while five topologies preserve them. ASVs provide a topology-dependent vulnerability ranking; matrix-based corrections are provably ineffective for four topologies (FWL invariance). Practitioners should identify the topology first: for exposure, PPI++ reduces bias from ~61% to <1% (Table); for IV, topology-agnostic correction can amplify bias (−139% in our demo; Table). High F1 does not guarantee low causal bias; topology assessment must precede downstream inference.

Differential misclassification and proving Conjecture for general K remain open.

**Limitations**

Closed-form results assume linear SEMs with proportional effects (f=λg); sign preservation empirically holds at 97.3% under non-proportional effects, but recommendations do not directly extend to nonlinear models (matching, doubly-robust). The framework assumes a known DAG with non-differential misclassification; DAG misspecification under measurement error may compound bias. ASV computation requires gold labels for C⁻¹; error propagation under small gold-label budgets (<500) and general K≥3 envelope monotonicity (Conjecture) remain open.

---

### 6. APPENDIX STRUCTURE

The appendix contains the following major sections and tables:

**Main Proof Sections:**
- Proofs of Proposition (sign-flip) and Theorem (monotonicity)
  - Notation and Key Identities
  - Frisch–Waugh–Lovell Decomposition
  - Confounding Topology (A = Confounder)
  - Proof of Theorem (Confounding Monotonicity)
  - Mediation Topology (A = Mediator)
  - Proof of Theorem (K=3 Symmetric Monotonicity)
  - Collider Topology (A = Collider)
  - Front-door Topology (A = Mediator under Confounding)
  - Exposure Topology: Sign Reversal Counterexample
  - Summary of Conditions (Table: Sufficient conditions for sign preservation)
  - Adversarial Monotonicity Verification (Table: verification across K=3,5,7)

**Supplementary Tables, Figures, and Algorithm:**
- Binarization Collapse (analysis of K=3 to binary collapse bias)
- Proof of FWL Invariance
- Applied Illustration: ClinicalBERT Case Study
- IV Wald Estimator: Diagonal-Dominance Subspaces
- Non-Differential Misclassification Verification
- Non-Differential Assumption Stress Test (Table: stress test results)
- Robustness to Nonlinear DGP (logistic regression)
- Bootstrap Uncertainty of ASV (Figure: bootstrap ASV distribution)
- Cross-K Robustness (K=5,7 validation)
- ASV Diagnostic Results
- ASV Stability Across DGP Parameters (Table: parameter sensitivity)
- Extended Conjecture Verification (Table: monotonicity violations)
  - Proportional Effects Breakdown (Table: λ(C) validation)
- FWL Invariance Under Nonlinear Models (Table: logistic regression results)
- PPI++ Gold Label Ratio Sensitivity (Table: gold label fraction sensitivity)
- Realistic Differential Misclassification Thresholds (Table: safe thresholds by dataset)
- Proportional Effects with Empirical Confusion Matrices (Table: validation with 23 LLM matrices)
- Case Study: ASV Diagnosis of Political Ad Tone Classification
- End-to-End Demonstration
- Semi-Real Case Study with Production LLM Confusion Matrices
- Correction Method Sensitivity to K (Table: top method and RMSE by topology)
- Comparison with Related Sensitivity Frameworks (Table: comparison with E-values, etc.)
- Per-Topology F1–Bias Correlation (Table: Spearman ρ analysis)
- Confusion Matrix Estimation Robustness (Table: partition stability)
- Sign Reversal Determinants (Table: decision rule analysis)
- Y-Stratified Non-Differential Verification (Table: Y-stratified test results)

**Final Sections:**
- Notation (Table: key notation throughout the paper)
- Use of AI Assistants

---

## Key Opportunities for Expansion

Based on this review, here are potential areas where the main text could be expanded:

1. **Mediation section:** Currently brief; could expand the probability limit derivation (Eq. 64–67) with more intuition about λ(C) and Berkson attenuation under mediation.

2. **Front-door topology:** Only 3 paragraphs currently; the two-stage mechanism deserves more detailed treatment given it's less standard.

3. **Correction methods section (4.3):** Currently describes results but doesn't show the actual Algorithm in main text. Moving Algorithm and FWL proof to main text would strengthen the decision procedure narrative.

4. **IV section:** Currently compressed to one paragraph. The Wald denominator sensitivity and why IV is "most fragile" deserves expanded treatment with more intuition about sign reversal at K≥3.

5. **Primary coefficient preservation:** This empirical regularity (β₁ >> β₂ prevents sign flip) appears in Method but isn't deeply explored. Could expand with implications for practitioners.

6. **Case studies:** Appendix contains a ClinicalBERT case study and political ad tone classification case study that could potentially be moved to main text to illustrate practical impact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e903e18c-fd65-4676-81fa-9eafa57a4de4",
  "isSidechain": true,
  "agentId": "ad9c11a1a52b2a80e",
  "requestId": "req_011CbPaKWddnWpwHDxznizGV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5c160621-45f0-42f1-837f-2222b97020a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/director_d3562b73",
  "sessionId": "80009587-b410-4ace-a00d-57e3723528f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "peppy-whistling-swan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014N9ui5F3LE1DXp7Q9N5Y6Q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 50568,
      "output_tokens": 7078,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1449
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 7078,
          "cache_read_input_tokens": 50568,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1449,
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
