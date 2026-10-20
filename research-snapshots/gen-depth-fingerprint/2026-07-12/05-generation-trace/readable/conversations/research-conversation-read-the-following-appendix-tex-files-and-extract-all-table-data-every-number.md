# Research conversation: Read the following appendix tex files and extract ALL table data (every number in every table). Be thorough. Files to re

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4ee533cda4eea682.jsonl`
- **Structured JSON:** [`9f9e4a3fa1418c8bf224.json`](../../sessions/9f/9f9e4a3fa1418c8bf224.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-23T10:22:49.207Z_

Read the following appendix tex files and extract ALL table data (every number in every table). Be thorough.

Files to read (all under /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/):
1. appendix_qlora.tex
2. appendix_instruct.tex
3. appendix_temperature_stability.tex
4. appendix_decoding_strategy.tex
5. appendix_cross_model_detail.tex
6. appendix_cross_temp.tex
7. appendix_domain.tex
8. appendix_tost.tex
9. appendix_tost_bootstrap.tex
10. appendix_ddr_causality.tex
11. appendix_ddr_validation.tex
12. appendix_9gen_scale.tex
13. appendix_generator_subsets.tex
14. appendix_prompt_type.tex
15. appendix_transfer.tex
16. appendix_iterative_comparison.tex
17. appendix_variance_decomposition.tex
18. appendix_convergence.tex
19. appendix_feature_distributions.tex
20. appendix_feature_correlation.tex
21. appendix_feature_candidates.tex
22. appendix_nll_distribution.tex
23. appendix_qualitative_examples.tex

For each file:
- Identify any table number and caption
- Extract every numerical value in tables with row/column labels
- Also extract any numerical values mentioned in the text

Report in format: [filename] Table X: caption, then list all values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "071c5763-099d-4c60-a830-e625867bc945",
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

_source line 2 · 2026-05-23T10:22:50.440Z_

I'll read all these appendix files and extract the table data. Let me start by reading them all in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "071c5763-099d-4c60-a830-e625867bc945",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1b1c33f4-5318-40f7-b6bf-d8afbae79ce9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 3 · 2026-05-23T10:22:50.640Z_

<details open><summary>🔧 Tool call — Read · `toolu_0139cUdRhZ7QgfJoNp3VWM8n`</summary>

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
  "parentUuid": "1b1c33f4-5318-40f7-b6bf-d8afbae79ce9",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a397f089-b5d2-43f9-af84-8a1e826f3ea7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 4 · 2026-05-23T10:22:50.645Z_

<details><summary>↩ Tool result · `toolu_0139cUdRhZ7QgfJoNp3VWM8n`</summary>

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
36	The QLoRA ceiling thus represents an information-asymmetric upper bound rather than a competing method: it consumes the full token sequence (0.6B parameters, GPU inference) whereas the 7-feature ensemble distills the signal into interpretable scalars that expose \emph{why} depth is detectable---a decomposition that end-to-end models cannot provide.
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a397f089-b5d2-43f9-af84-8a1e826f3ea7",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "08f8aa2d-9113-4fa8-9ea5-7e72814e18a8",
  "sourceToolAssistantUUID": "a397f089-b5d2-43f9-af84-8a1e826f3ea7",
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

_source line 5 · 2026-05-23T10:22:51.068Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WCUVfmFKp3XJAVgooD3Gnd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08f8aa2d-9113-4fa8-9ea5-7e72814e18a8",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "61cf0feb-1822-4df9-ba64-5cf9c3eeeda8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 6 · 2026-05-23T10:22:51.074Z_

<details><summary>↩ Tool result · `toolu_01WCUVfmFKp3XJAVgooD3Gnd`</summary>

```text
1	\subsection*{Instruction-Tuned Model Results}
2	
3	Table~\ref{tab:instruct} summarizes depth classification under instruction tuning for three model families.
4	All results use within-model 5-fold CV on single-generator chains; LOGO evaluation is available for two models but uses earlier generator subsets (5--6 generators), so cross-model numbers are not directly comparable across rows.
5	
6	\begin{table}[ht]
7	\centering
8	\small
9	\caption{Depth classification: base vs.\ instruction-tuned models (within-model 5-fold CV). $\rho$: Spearman correlation of entropy mean with depth. Rev.: number of features (out of 7) whose $\rho$ reverses sign under instruction tuning.}
10	\label{tab:instruct}
11	\resizebox{\linewidth}{!}{%
12	\begin{tabular}{lcc cc cc c}
13	\toprule
14	& \multicolumn{2}{c}{\textbf{3-class F1}} & \multicolumn{2}{c}{\textbf{Binary F1}} & \multicolumn{2}{c}{$\boldsymbol{\rho}$\textbf{(ent.\ mean)}} & \\
15	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
16	\textbf{Model} & Base & Instruct & Base & Instruct & Base & Instruct & \textbf{Rev.} \\
17	\midrule
18	OLMo-2-1B       & 0.754 & 0.575 & 0.845 & 0.813 & $-$0.64 & $+$0.48 & 6/7 \\
19	Qwen3-1.7B      & 0.769 & 0.732 & 0.861 & 0.875 & $-$0.60 & $+$0.48 & 6/7 \\
20	Llama-3.2-3B    & 0.742 & 0.544 & 0.849 & 0.838 & $-$0.63 & $+$0.23 & 3/7 \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	Instruction tuning degrades 3-class F1 by 3.7--19.9\,pp across all three families, while binary F1 (gen-1 vs.\ gen-2+) changes remain small ($|\Delta| \leq 3.2$\,pp).
26	The asymmetry indicates that instruction tuning primarily disrupts the gen-0/gen-1 boundary (human vs.\ first-generation), consistent with RLHF shifting the output distribution away from human-like text.
27	Entropy-mean $\rho$ reverses sign for all three models ($-0.60$--$-0.64$ base $\rightarrow$ $+0.23$--$+0.48$ instruct), and 6 of 7 features reverse for OLMo and Qwen vs.\ 3 of 7 for Llama.
28	This pattern is consistent with instruction tuning shifting the generation attractor rather than eliminating iterative dynamics (\S\ref{sec:discussion}).
29	
30	\paragraph{Retraining on instruction-tuned data.}
31	To test whether the depth signal persists under instruction tuning with reversed polarity, we retrain the XGBoost classifier on instruction-tuned feature data (Table~\ref{tab:instruct-retrain}).
32	
33	\begin{table}[ht]
34	\centering
35	\small
36	\caption{Classification recovery under instruction-tuned retraining (binary-only: gen-1 vs.\ gen-2+, gen-0 excluded from training and evaluation). Base$\rightarrow$Inst: base-trained classifier tested on instruct data. Note: Table~\ref{tab:instruct} reports higher instruct binary F1 (e.g., OLMo 0.813) because it uses 3-class training with binary evaluation, where gen-0 in training helps the classifier learn the feature space.}
37	\label{tab:instruct-retrain}
38	\begin{tabular}{lccc}
39	\toprule
40	\textbf{Model} & \textbf{Base$\rightarrow$Inst} & \textbf{Retrained} & \textbf{$\Delta$} \\
41	\midrule
42	OLMo-2-1B-Inst   & 0.321 & 0.590 & $+$0.269 \\
43	Qwen3-1.7B-Inst  & 0.500 & 0.660 & $+$0.160 \\
44	Qwen3-0.6B-Inst  & 0.532 & 0.600 & $+$0.068 \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	Retraining recovers substantial within-model performance ($+$6.8--26.9\,pp), but the retrained F1 (0.590--0.660) remains below base-model levels (0.69--0.72).
50	Three-generator instruct LOGO yields binary F1\,=\,0.487, indicating weak cross-generator transfer under instruction tuning.
51	
52	\paragraph{DDR structure under instruction tuning.}
53	$k{=}2$ clustering in $(|\rho|, d)$ space on pooled instruct features yields silhouette\,=\,0.372 (vs.\ 0.660 for base models), indicating that the clean drifting/non-drifting partition is substantially compressed.
54	The compression is model-dependent: OLMo-Instruct shows near-zero $|\rho|$ for TTR and hapax (0.006, 0.025), while Qwen instruct models retain moderate correlations ($|\rho|{=}0.48$--$0.53$).
55	Cross-condition transfer is near chance in both directions (base$\rightarrow$instruct binary F1\,=\,0.490; instruct$\rightarrow$base F1\,=\,0.454), with the asymmetry ($-$0.036) suggesting that instruct-trained features generalize even less to base distributions than the reverse.
56	These results indicate that instruction tuning compresses the feature-space structure underlying DDR rather than simply reversing feature directions (Figure~\ref{fig:instruct-ddr}).
57	
58	\begin{figure}[H]
59	\centering
60	\includegraphics[width=\columnwidth]{fig_appendix_instruct_ddr.pdf}
61	\caption{DDR partition under base vs.\ instruction-tuned models. (a)~Base models (silhouette\,=\,0.660): clear drifting/non-drifting separation. (b)~Instruction-tuned models (silhouette\,=\,0.372): all features compress toward zero, collapsing the partition; entropy max shifts from near-stationary to intermediate; formerly drifting features (hapax, TTR) lose most of their effect size. Bars show pooled $|d|$; markers show individual generators.}
62	\label{fig:instruct-ddr}
63	\end{figure}
64	
65	\paragraph{Reference model sensitivity.}
66	One hypothesis for the instruct degradation is reference-model mismatch: the base Pythia-410M reference may produce systematically biased NLL estimates on instruction-tuned outputs, masking depth-dependent variation.
67	To test this, we replace the reference with Qwen3-0.6B-Instruct and recompute all features on the two instruct generators.
68	The hypothesis is partially rejected: Qwen3-1.7B-Instruct shows mixed changes (entropy max $d$: $0.51 \to 0.08$, becoming near-stationary; entropy std $d$: $1.07 \to 1.51$, increasing), while OLMo-Instruct loses nearly all depth signal (entropy mean $d$: $1.33 \to 0.02$; tail decay $d$: $0.60 \to 0.06$).
69	The model-dependent heterogeneity rules out reference mismatch as a universal explanation for instruct DDR degradation, supporting the interpretation that alignment fundamentally reshapes the generation dynamics rather than introducing a correctable measurement artifact.
70	
71	\paragraph{End-to-end instruct classification.}
72	To test whether depth signal persists at the token level despite summary-statistic degradation, we apply the QLoRA end-to-end classifier (Appendix~\ref{app:qlora}) to instruction-tuned data using within-model 5-fold stratified CV (Table~\ref{tab:instruct-qlora}).
73	
74	\begin{table}[ht]
75	\centering
76	\small
77	\caption{End-to-end QLoRA vs.\ XGBoost on instruction-tuned data (within-model 5-fold CV, Qwen3-0.6B backbone). Base QLoRA rows shown for reference only; instruct sets ($N{\approx}4.4$--$5.0$K) are approximately twice the base sets ($N{\approx}2.3$K), so cross-condition comparison is confounded by training set size.}
78	\label{tab:instruct-qlora}
79	\resizebox{\linewidth}{!}{%
80	\begin{tabular}{lccccc}
81	\toprule
82	& \multicolumn{2}{c}{\textbf{3-class F1}} & & \\
83	\cmidrule(lr){2-3}
84	\textbf{Model} & XGB & QLoRA & $\boldsymbol{\Delta}$ & \textbf{$N$} \\
85	\midrule
86	OLMo-2-1B-Inst   & 0.575 & 0.888\,$\pm$\,0.007 & $+$31.3\,pp & 4{,}429 \\
87	Qwen3-1.7B-Inst  & 0.732 & 0.907\,$\pm$\,0.008 & $+$17.5\,pp & 4{,}963 \\
88	\midrule
89	OLMo-2-1B (base) &       & 0.859\,$\pm$\,0.004 &             & 2{,}379 \\
90	Qwen3-1.7B (base)&       & 0.904\,$\pm$\,0.009 &             & 2{,}291 \\
91	\bottomrule
92	\end{tabular}}
93	\end{table}
94	
95	The XGBoost-to-QLoRA gap on the same instruct data is substantial ($+$17.5 to $+$31.3\,pp), indicating that depth signal persists at the token level under instruction tuning but is inaccessible to the seven summary statistics; the degradation reported in Table~\ref{tab:instruct} reflects a feature-level limitation rather than signal absence.
96	Note that instruct samples are approximately twice the base count used here (Table~\ref{tab:instruct-qlora}), so the instruct-vs-base QLoRA comparison is confounded by training set size; the meaningful comparison is QLoRA-vs-XGBoost on the same instruct data.
97	All results use within-model 5-fold CV, not cross-generator LOGO, limiting generalization claims.
98	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61cf0feb-1822-4df9-ba64-5cf9c3eeeda8",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "00bfcf3a-d7d0-4ac6-a8a5-3b16e63d1c97",
  "sourceToolAssistantUUID": "61cf0feb-1822-4df9-ba64-5cf9c3eeeda8",
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

_source line 7 · 2026-05-23T10:22:51.296Z_

<details open><summary>🔧 Tool call — Read · `toolu_018JK5QjFHRptDVxVaVCYLoG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_temperature_stability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00bfcf3a-d7d0-4ac6-a8a5-3b16e63d1c97",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f5c527da-7b8f-487d-9486-0f7b09c2c00a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 8 · 2026-05-23T10:22:51.300Z_

<details><summary>↩ Tool result · `toolu_018JK5QjFHRptDVxVaVCYLoG`</summary>

```text
1	To assess whether the DDR three-way partition generalizes beyond the default temperature ($\tau{=}0.7$), we computed per-feature Cohen's $d$ (generation~1 vs.\ generation~2+) at $\tau \in \{0.5, 0.7, 0.9\}$ for all four generators in the temperature ablation (12 conditions total; Table~\ref{tab:ddr-temp-stability}).
2	
3	\begin{table}[H]
4	\centering
5	\small
6	\caption{Mean $|d|$ (gen-1 vs.\ gen-2+) across 4 generators at each temperature. Partition labels: \textbf{D}rifting ($|d|>0.5$), \textbf{I}ntermediate ($0.1{<}|d|{<}0.5$), near-\textbf{S}tationary ($|d|{<}0.1$). Boldface marks features that shift from their $\tau{=}0.7$ partition.}
7	\label{tab:ddr-temp-stability}
8	\resizebox{\linewidth}{!}{%
9	\begin{tabular}{lccc l}
10	\toprule
11	\textbf{Feature} & $\boldsymbol{\tau{=}0.5}$ & $\boldsymbol{\tau{=}0.7}$ & $\boldsymbol{\tau{=}0.9}$ & \textbf{Group} \\
12	\midrule
13	Entropy mean  & 1.39\,\textsuperscript{D} & 1.10\,\textsuperscript{D} & 0.58\,\textsuperscript{D} & Drifting \\
14	TTR           & 1.00\,\textsuperscript{D} & 0.85\,\textsuperscript{D} & \textbf{0.45}\,\textsuperscript{I} & Drifting \\
15	Hapax ratio   & 0.87\,\textsuperscript{D} & 0.75\,\textsuperscript{D} & \textbf{0.42}\,\textsuperscript{I} & Drifting \\
16	\midrule
17	Entropy std   & \textbf{0.84}\,\textsuperscript{D} & 0.52\,\textsuperscript{D} & \textbf{0.20}\,\textsuperscript{I} & Intermediate \\
18	\midrule
19	Entropy max   & 0.06\,\textsuperscript{S} & 0.09\,\textsuperscript{S} & \textbf{0.11}\,\textsuperscript{I} & Stationary \\
20	Tail decay    & 0.07\,\textsuperscript{S} & \textbf{0.12}\,\textsuperscript{I} & \textbf{0.15}\,\textsuperscript{I} & Stationary \\
21	Entropy min   & 0.04\,\textsuperscript{S} & 0.06\,\textsuperscript{S} & 0.04\,\textsuperscript{S} & Stationary \\
22	\bottomrule
23	\end{tabular}}
24	\end{table}
25	
26	The partition anchors are robust: entropy mean remains drifting in all 12 conditions, TTR in 10/12, and hapax ratio in 9/12; entropy min and entropy max stay near-stationary in 10/12 and 9/12 conditions, respectively.
27	The two boundary features are more temperature-sensitive: entropy std is drifting at $\tau{=}0.5$ for all generators but falls to intermediate at $\tau{=}0.9$ for three of four, while tail decay fluctuates between near-stationary and intermediate across generators.
28	Effect sizes compress monotonically with temperature: for the fixed drifting set (entropy mean, TTR, hapax ratio), mean $|d|$ drops from 1.09 at $\tau{=}0.5$ to 0.90 at $\tau{=}0.7$ to 0.48 at $\tau{=}0.9$, shifting individual features across partition boundaries at high temperature without altering the qualitative hierarchy: lexical diversity features drift fastest, entropy extrema remain stable across all conditions tested.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5c527da-7b8f-487d-9486-0f7b09c2c00a",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "3d07efce-8e29-4d71-99ac-a8d11fce16ee",
  "sourceToolAssistantUUID": "f5c527da-7b8f-487d-9486-0f7b09c2c00a",
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

_source line 9 · 2026-05-23T10:22:51.510Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HSa1381F2EEqAppmovtX4v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_decoding_strategy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d07efce-8e29-4d71-99ac-a8d11fce16ee",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "22f0c7be-1041-4d5a-879d-0224786e87c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 10 · 2026-05-23T10:22:51.513Z_

<details><summary>↩ Tool result · `toolu_01HSa1381F2EEqAppmovtX4v`</summary>

```text
1	% Decoding Strategy Robustness
2	To verify that DDR shape stability is not an artifact of nucleus sampling ($p{=}0.9$, $\tau{=}0.7$),
3	we repeat the generation chain experiment under two alternative decoding strategies:
4	greedy decoding ($\tau{=}0$) and top-$k$ sampling ($k{=}50$, $\tau{=}0.7$).
5	All eight generators spanning five architectural families produce ${\sim}$1{,}000 chains of depth 0--4 per strategy,
6	yielding ${\sim}$5{,}000 texts per generator--strategy combination.
7	
8	Table~\ref{tab:decoding-shape} reports Cohen's $d$ (gen-1 vs.\ gen-2+) for the three shape features across strategies;
9	Table~\ref{tab:decoding-drift} provides the corresponding values for drifting and intermediate features.
10	
11	\begin{table}[ht]
12	\centering
13	\small
14	\caption{Shape-feature Cohen's $d$ (gen-1 vs.\ gen-2+) under three decoding strategies per generator.
15	Values below 0.20 indicate negligible drift.
16	Shape features are expected to remain near-stationary across strategies if DDR is decoding-agnostic.}
17	\label{tab:decoding-shape}
18	\resizebox{\linewidth}{!}{%
19	\begin{tabular}{ll ccc ccc ccc}
20	\toprule
21	& & \multicolumn{3}{c}{entropy\_max} & \multicolumn{3}{c}{entropy\_min} & \multicolumn{3}{c}{tail\_decay} \\
22	\cmidrule(lr){3-5} \cmidrule(lr){6-8} \cmidrule(lr){9-11}
23	Family & Generator & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ \\
24	\midrule
25	Pythia  & 2.8B    & 0.25 & 0.09 & 0.26 & 0.03 & 0.08 & 0.04 & 0.07 & 0.07 & 0.12 \\
26	        & 1B      & 0.21 & 0.12 & 0.27 & 0.02 & 0.04 & 0.04 & 0.08 & 0.04 & 0.18 \\
27	OLMo    & 2-1B    & 0.06 & 0.03 & 0.01 & 0.07 & 0.03 & 0.01 & 0.22 & 0.03 & 0.22 \\
28	Qwen3   & 0.6B    & 0.01 & 0.09 & 0.02 & 0.10 & 0.02 & 0.10 & 0.08 & 0.03 & 0.13 \\
29	        & 1.7B    & 0.02 & 0.08 & 0.03 & 0.05 & 0.01 & 0.03 & 0.09 & 0.04 & 0.14 \\
30	        & 8B      & 0.04 & 0.01 & 0.05 & 0.01 & 0.06 & 0.07 & 0.15 & 0.08 & 0.17 \\
31	Llama   & 3.2-3B  & 0.01 & 0.06 & 0.08 & 0.01 & 0.07 & 0.03 & 0.19 & 0.04 & 0.20 \\
32	Mistral & 7B-v0.3 & 0.00 & 0.01 & 0.06 & 0.04 & 0.02 & 0.01 & 0.16 & 0.14 & 0.12 \\
33	\midrule
34	\multicolumn{2}{l}{\textbf{Mean}} & \textbf{0.08}$^{8/8}$ & \textbf{0.06}$^{8/8}$ & \textbf{0.10}$^{8/8}$ & \textbf{0.04}$^{8/8}$ & \textbf{0.04}$^{8/8}$ & \textbf{0.04}$^{8/8}$ & \textbf{0.13}$^{8/8}$ & \textbf{0.06}$^{8/8}$ & \textbf{0.16}$^{8/8}$ \\
35	\bottomrule
36	\end{tabular}}
37	\end{table}
38	
39	\begin{table}[ht]
40	\centering
41	\small
42	\caption{Drifting- and intermediate-feature Cohen's $d$ (gen-1 vs.\ gen-2+) under three decoding strategies per generator.
43	Drifting features are expected to maintain large $d$ regardless of strategy.}
44	\label{tab:decoding-drift}
45	\resizebox{\linewidth}{!}{%
46	\begin{tabular}{ll ccc ccc ccc ccc}
47	\toprule
48	& & \multicolumn{3}{c}{entropy\_mean} & \multicolumn{3}{c}{TTR} & \multicolumn{3}{c}{hapax\_ratio} & \multicolumn{3}{c}{entropy\_std} \\
49	\cmidrule(lr){3-5} \cmidrule(lr){6-8} \cmidrule(lr){9-11} \cmidrule(lr){12-14}
50	Family & Generator & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ & Nuc. & Gr. & Top-$k$ \\
51	\midrule
52	Pythia  & 2.8B    & 1.20 & 1.43 & 0.70 & 0.77 & 0.98 & 0.41 & 0.67 & 0.87 & 0.37 & 0.39 & 0.93 & 0.10 \\
53	        & 1B      & 1.40 & 0.98 & 0.83 & 0.80 & 0.64 & 0.41 & 0.65 & 0.53 & 0.34 & 0.53 & 0.91 & 0.13 \\
54	OLMo    & 2-1B    & 1.19 & 1.29 & 0.73 & 1.08 & 0.89 & 0.70 & 1.00 & 0.80 & 0.69 & 0.61 & 0.95 & 0.35 \\
55	Qwen3   & 0.6B    & 0.92 & 0.82 & 0.80 & 0.63 & 0.51 & 0.58 & 0.50 & 0.46 & 0.52 & 0.56 & 0.72 & 0.30 \\
56	        & 1.7B    & 1.12 & 1.03 & 0.99 & 0.93 & 0.74 & 0.85 & 0.83 & 0.68 & 0.80 & 0.52 & 0.78 & 0.32 \\
57	        & 8B      & 0.86 & 0.98 & 0.76 & 0.71 & 0.76 & 0.68 & 0.66 & 0.76 & 0.64 & 0.37 & 0.71 & 0.27 \\
58	Llama   & 3.2-3B  & 1.15 & 1.46 & 0.77 & 1.04 & 1.27 & 0.73 & 0.98 & 1.26 & 0.71 & 0.50 & 1.01 & 0.21 \\
59	Mistral & 7B-v0.3 & 0.89 & 1.31 & 0.70 & 0.82 & 1.04 & 0.64 & 0.82 & 1.03 & 0.67 & 0.23 & 0.62 & 0.15 \\
60	\midrule
61	\multicolumn{2}{l}{\textbf{Mean}} & \textbf{1.09}$^{8/8}$ & \textbf{1.16}$^{8/8}$ & \textbf{0.79}$^{8/8}$ & \textbf{0.85}$^{8/8}$ & \textbf{0.85}$^{8/8}$ & \textbf{0.63}$^{8/8}$ & \textbf{0.76}$^{8/8}$ & \textbf{0.80}$^{8/8}$ & \textbf{0.59}$^{8/8}$ & \textbf{0.46}$^{8/8}$ & \textbf{0.83}$^{8/8}$ & \textbf{0.23}$^{8/8}$ \\
62	\bottomrule
63	\end{tabular}}
64	\end{table}
65	
66	% ===== Conclusion: select ONE version below when data is available =====
67	
68	\iffalse
69	% VERSION A — shape stability confirmed across all strategies (d < 0.15)
70	Shape features (entropy\_max, entropy\_min, tail\_decay) maintain near-stationary
71	effect sizes under both greedy and top-$k$ decoding (mean $d{=}$\textbf{XX}, range \textbf{XX--XX}),
72	while drifting features exhibit consistently large effects (mean $d{=}$\textbf{XX}).
73	The DDR partition replicates across all eight generators and three decoding strategies,
74	confirming that the location/shape asymmetry is a empirical regularity of fixed-parameter
75	autoregressive sampling, independent of the specific token-selection mechanism.
76	\fi
77	
78	\iffalse
79	% VERSION B — shape stability partially degrades under greedy
80	Shape features show elevated Cohen's $d$ under greedy decoding (mean $d{=}$\textbf{XX} vs.\
81	$d{=}$\textbf{XX} under nucleus), particularly for \textbf{[feature]} in \textbf{[generators]}.
82	This suggests that sampling stochasticity partially masks shape drift:
83	without top-$p$ truncation, the deterministic mode selection in greedy decoding
84	exposes additional depth-dependent variation in the tail structure.
85	The DDR partition remains valid for nucleus and top-$k$ sampling but requires
86	qualification for greedy decoding.
87	\fi
88	
89	% VERSION C — greedy confirms DDR; top-k partially attenuates (ACTIVE)
90	Under greedy decoding ($\tau{=}0$), shape features remain near-stationary across all eight generators
91	(mean $|d|{=}$\textbf{0.05}, max \textbf{0.14}), while core drifting features maintain large effects
92	(mean $d{=}$\textbf{0.94}), confirming that DDR is a empirical regularity of autoregressive generation
93	independent of sampling truncation.
94	Top-$k$ sampling ($k{=}50$) partially attenuates the partition.
95	Shape features show boundary violations in 4/8 generators under top-$k$; however, these generators exhibit comparable or higher violations under nucleus sampling (Pythia entropy\_max: 0.21--0.25 nucleus vs.\ 0.26--0.27 top-$k$; OLMo tail\_decay: 0.22 under both), indicating model-intrinsic boundary effects rather than strategy-induced degradation.
96	Core drifting effect sizes weaken (mean $d{=}$\textbf{0.67} vs.\ \textbf{0.90} under nucleus).
97	This modulation is consistent with the mechanistic account in \S\ref{sec:discussion}:
98	top-$k$ truncation introduces a fixed-width selection window that interacts differently
99	with depth-compressed distributions than nucleus sampling's probability-mass truncation,
100	partially blurring the location/shape boundary.
101	The core DDR partition---drifting features carrying depth signal while shape features
102	provide cross-generator reference---remains intact under both greedy and nucleus sampling
103	and is attenuated but recognizable under top-$k$.
104	Notably, entropy\_std exhibits strong strategy dependence (greedy mean $d{=}$0.83; nucleus 0.46; top-$k$ 0.23), suggesting its depth sensitivity is modulated by the token-selection mechanism---deterministic greedy selection amplifies entropy variance across depths, while top-$k$'s fixed window compresses it---further supporting its classification as an intermediate rather than core feature.
105	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22f0c7be-1041-4d5a-879d-0224786e87c9",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "2247570d-f9c8-4f80-b0ee-d3aa3ee8b50f",
  "sourceToolAssistantUUID": "22f0c7be-1041-4d5a-879d-0224786e87c9",
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

_source line 11 · 2026-05-23T10:22:51.725Z_

<details open><summary>🔧 Tool call — Read · `toolu_018xgteoX3FoseCXcS7iX6yJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_cross_model_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2247570d-f9c8-4f80-b0ee-d3aa3ee8b50f",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "31a209a6-da03-4331-8078-6bb3c4977600",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 12 · 2026-05-23T10:22:51.728Z_

<details><summary>↩ Tool result · `toolu_018xgteoX3FoseCXcS7iX6yJ`</summary>

```text
1	This appendix reports per-generator breakdowns for the cross-model chain evaluation described in \S\ref{sec:results-classification}.
2	
3	\begin{table}[ht]
4	\centering
5	\footnotesize
6	\caption{Cross-model chain per-class performance (generator-level leave-one-out, $N$\,=\,2{,}964, $n_{\text{generators}}$\,=\,5: Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B). Macro F1\,=\,0.831 under class balancing; under natural class distribution, macro F1\,=\,0.789. Binary F1 (gen-1 vs.\ gen-2+)\,=\,0.830 (95\% CI [.818, .841], case-level bootstrap, $n$\,=\,2{,}000). Cross-model chains avoid the gen-0 seed sharing issue present in single-generator LOGO.}
7	\label{tab:cross-model-perclass}
8	\begin{tabular}{lcccc}
9	\toprule
10	\textbf{Class} & \textbf{Prec.} & \textbf{Rec.} & \textbf{F1} & \textbf{95\% CI} \\
11	\midrule
12	gen-0   & 0.921 & 0.948 & 0.935 & [.923, .946] \\
13	gen-1   & 0.737 & 0.803 & 0.768 & [.748, .788] \\
14	gen-2+  & 0.842 & 0.742 & 0.789 & [.768, .809] \\
15	\midrule
16	\textbf{Macro} & --- & --- & \textbf{0.831} & [.817, .844] \\
17	\bottomrule
18	\end{tabular}
19	\end{table}
20	
21	\paragraph{Variance decomposition.}
22	A two-way ANOVA (generator $\times$ depth) on cross-model chain features ($n{=}3{,}778$, depths 1--4) confirms that generator identity contributes negligible variance: partial $\eta^2_{\text{gen}} < 1\%$ for all seven features (range 0.05\%--0.90\%, mean 0.37\%), while depth accounts for 15.3\%--29.9\% of variance in drifting features.
23	The generator$\times$depth interaction is also $< 1\%$.
24	This confirms that the F1\,=\,0.830 cross-model advantage reflects depth signal rather than generator diversity accumulation: mixing generators across chain steps does not introduce a confounding generator-identity cue.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31a209a6-da03-4331-8078-6bb3c4977600",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "bf80c129-1b1b-482c-bd71-141803ed98d6",
  "sourceToolAssistantUUID": "31a209a6-da03-4331-8078-6bb3c4977600",
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

_source line 13 · 2026-05-23T10:22:51.969Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EMUX3jPJng7UNqYmjFoK4i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_cross_temp.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf80c129-1b1b-482c-bd71-141803ed98d6",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "14b5fb89-bc77-4e23-8bdf-392558765fab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 14 · 2026-05-23T10:22:51.973Z_

<details><summary>↩ Tool result · `toolu_01EMUX3jPJng7UNqYmjFoK4i`</summary>

```text
1	Figure~\ref{fig:cross-temp} shows cross-temperature transfer results for the 6-generator LOGO pipeline.
2	We evaluate four train$\rightarrow$test temperature conditions using Qwen3-1.7B data regenerated at $t{=}1.0$ (remaining five generators retain $t{=}0.7$).\footnote{The $t{=}1.0$ data uses top-$p{=}0.95$ (vs.\ $p{=}0.9$ for other configurations); this difference may contribute to the observed degradation beyond the temperature effect alone.}
3	
4	\begin{figure}[H]
5	\centering
6	\includegraphics[width=\columnwidth]{fig_appendix_cross_temp.pdf}
7	\caption{Cross-temperature transfer evaluation (6-gen LOGO). (a) Overall F1 by train$\rightarrow$test temperature condition. Matched conditions (0.7$\rightarrow$0.7, 1.0$\rightarrow$1.0) outperform cross-temperature transfer, with 0.7$\rightarrow$1.0 showing the largest degradation ($-6.6$\,pp in 3-class F1). (b) Per-generator 3-class F1 heatmap: Qwen3-1.7B shows dramatic degradation under cross-temperature conditions (0.418) while other generators remain stable. The temperature mismatch disproportionately affects the generator whose data was regenerated.}
8	\label{fig:cross-temp}
9	\end{figure}
10	
11	Key observations from the cross-temperature analysis:
12	
13	\begin{enumerate}[nosep]
14	\item \textbf{Matched-temperature robustness}: Both $t{=}0.7$ and $t{=}1.0$ matched conditions yield comparable performance (3-class F1: 0.789 vs.\ 0.726), with the gap attributable to weaker depth signal at high temperature rather than classifier degradation.
15	
16	\item \textbf{Asymmetric transfer}: Training at $t{=}1.0$ and testing at $t{=}0.7$ (F1\,=\,0.791) transfers well, but the reverse (0.7$\rightarrow$1.0, F1\,=\,0.723) degrades. This asymmetry reflects the information structure: features learned from high-variance (high-temperature) data generalize to low-variance settings, but not vice versa.
17	
18	\item \textbf{Generator-specific vulnerability}: Qwen3-1.7B, the only generator with temperature-mismatched test data, drops to F1\,=\,0.418 under cross-temperature conditions while all other generators maintain F1 $>$ 0.76. This confirms that depth features are calibrated to the specific decoding regime.
19	
20	\item \textbf{Binary transfer for the mismatched generator}: For Qwen3-1.7B (the only generator with actual temperature mismatch), binary F1 drops from 0.948 to 0.713 under 0.7$\rightarrow$1.0 transfer but recovers in the reverse direction (1.0$\rightarrow$0.7: 0.948), consistent with the asymmetric pattern in Item 2. The aggregate binary range (0.900--0.958) is inflated by five generators whose data is identical across conditions.
21	\end{enumerate}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14b5fb89-bc77-4e23-8bdf-392558765fab",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "494254d6-efb3-4ec5-9b33-1f618a3560d2",
  "sourceToolAssistantUUID": "14b5fb89-bc77-4e23-8bdf-392558765fab",
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

_source line 15 · 2026-05-23T10:22:52.358Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NQwoptVGeQFCvJ2CXjkJf6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_domain.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "494254d6-efb3-4ec5-9b33-1f618a3560d2",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ed8ec3a4-4de8-49eb-b0f2-977935fb8fb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 16 · 2026-05-23T10:22:52.361Z_

<details><summary>↩ Tool result · `toolu_01NQwoptVGeQFCvJ2CXjkJf6`</summary>

```text
1	This pilot study evaluates whether depth signal generalizes beyond Wikipedia by constructing generation chains from three additional domains: News articles, Academic abstracts, and Code documentation.
2	For each domain, we sample 200 seed texts and generate chains of depth 3 using three generators (Pythia-1B, Qwen3-1.7B, Mistral-7B).
3	The same 7-feature ensemble and LOGO protocol are applied.
4	
5	\noindent\textbf{Important caveat:} Cross-domain generation used $t{=}1.0$, top-$p{=}1.0$, which falls outside the method's reliable operating range ($t \leq 0.7$; Appendix~\ref{app:sampling-sensitivity}). Domain and temperature effects are therefore confounded in the results below; the cross-domain signal may partly reflect temperature-induced distributional divergence rather than domain generalization alone.
6	
7	\begin{table}[ht]
8	\centering
9	\small
10	\caption{Cross-domain depth classification under LOGO evaluation (binary: gen-1 vs.\ gen-2+). Three generators $\times$ 200 seeds per domain. Bootstrap 95\% CIs ($n$\,=\,1000).}
11	\label{tab:domain}
12	\begin{tabular}{lccc}
13	\toprule
14	\textbf{Domain} & \textbf{Binary F1} & \textbf{95\% CI} & \textbf{3-class F1} \\
15	\midrule
16	Code           & 0.754 & [0.737, 0.770] & 0.634 \\
17	News           & 0.746 & [0.726, 0.764] & 0.652 \\
18	Academic       & 0.739 & [0.720, 0.757] & 0.622 \\
19	\bottomrule
20	\end{tabular}
21	\end{table}
22	
23	All three non-Wikipedia domains achieve binary F1 $>$ 0.73 under leave-one-generator-out evaluation, which demonstrates that depth signal is not an artifact of Wikipedia text properties.
24	
25	\paragraph{Domain $\times$ temperature interaction.}
26	Cross-domain generation used $t{=}1.0$, top-$p{=}1.0$ (vs.\ the main experiment's $t{=}0.7$, top-$p{=}0.9$).
27	Supplementary evaluation at $t{=}0.7$ reveals a domain $\times$ temperature interaction: the main Wikipedia experiment favors lower temperature (depth signal degrades monotonically with rising temperature; Appendix~\ref{app:sampling-sensitivity}), while cross-domain evaluation favors higher temperature ($t{=}1.0$ yields +3 to +11\,pp over $t{=}0.7$; News 0.746 vs.\ 0.712, Academic 0.739 vs.\ 0.628, Code 0.754 vs.\ 0.687).
28	This asymmetry likely reflects reference-model calibration: Pythia-410M, trained predominantly on web text, detects subtle per-step drift in Wikipedia but requires larger distributional divergence (produced by higher temperature) to detect depth signal in out-of-distribution domains.
29	This finding suggests that reference model selection is a key factor for cross-domain deployment of depth profiling.
30	
31	\paragraph{3-class inversion as DDR evidence.}
32	In the cross-domain setting, 3-class F1 (0.62--0.65) falls below binary F1 (0.74--0.75), reversing the pattern observed in the main experiment (3-class 0.762 $>$ binary 0.694).
33	This inversion reflects degraded gen-0 vs.\ gen-1 separation: the Pythia-410M reference model is calibrated to Wikipedia text, so its baseline entropy estimates are less discriminative for out-of-domain human text and compresses the feature distance between gen-0 and gen-1.
34	The binary task (gen-1 vs.\ gen-2+) is unaffected because both classes are generated under identical domain and decoding conditions; recursive drift is a relative change that does not depend on absolute calibration.
35	This pattern provides additional evidence that DDR captures base-model generation dynamics rather than domain-specific text properties: depth signal remains robust even when the human-vs-machine boundary becomes less distinct.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed8ec3a4-4de8-49eb-b0f2-977935fb8fb9",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "326f8de5-3ff9-4245-a732-503b96115769",
  "sourceToolAssistantUUID": "ed8ec3a4-4de8-49eb-b0f2-977935fb8fb9",
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

_source line 17 · 2026-05-23T10:22:52.923Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HUwndjqdFCguot1GbkRrE9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "326f8de5-3ff9-4245-a732-503b96115769",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "287f9738-b930-4d35-86a1-395ee9e55a28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 18 · 2026-05-23T10:22:52.931Z_

<details><summary>↩ Tool result · `toolu_01HUwndjqdFCguot1GbkRrE9`</summary>

```text
1	\section{Per-Generator Equivalence Testing}
2	\label{app:tost}
3	
4	\begingroup\setlength{\parskip}{2pt plus 1pt}
5	
6	To confirm that the near-stationary classification is not a pooling artifact, we apply two one-sided $t$-tests (TOST) \cite{lakens_equivalence} for each feature within each generator separately (gen-1 vs.\ gen-2+, equivalence bound $|d| < 0.20$).
7	We adopt Cohen's conventional small effect size ($d{=}0.20$) \cite{cohen1988statistical} as the smallest effect of practical significance (SESOI): effects below this threshold are unlikely to be practically meaningful for depth discrimination.
8	LOFO analysis independently supports this choice: removing any near-stationary feature changes classification F1 by $\leq$1.5\,pp (Appendix~\ref{app:lofo}), linking the statistical threshold to classification irrelevance.
9	Sensitivity analysis at $\varepsilon \in \{0.15, 0.20, 0.25\}$ confirms the partition is robust to the bound choice (Appendix~\ref{app:tost-sensitivity}); bootstrap resampling ($B{=}1{,}000$) shows 100\% rejection stability for all near-stationary features (Appendix~\ref{app:tost-bootstrap}); and the partition is invariant across $\varepsilon \in [0.10, 0.75]$ (Appendix~\ref{app:epsilon-sweep}).
10	Table~\ref{tab:tost-per-gen} reports observed $|d|$; \checkmark{} marks features for which the TOST null hypothesis (non-equivalence) is rejected at $\alpha = 0.05$.
11	
12	Entropy min passes equivalence for all eight generators; entropy max passes for six of eight (exceeding $\varepsilon$ only for Pythia-1B and Pythia-2.8B, where $|d| \approx 0.21$--$0.25$); tail decay passes for four of eight.
13	All drifting and intermediate features fail equivalence uniformly, with $|d|$ ranging from 0.23 (entropy std, Mistral) to 1.40 (entropy mean, Pythia-1B).
14	The partition is robust at the individual-generator level, with entropy min as the most consistently stationary feature.
15	Figure~\ref{fig:ddr-scatter} visualizes the DDR partition in ($|\rho|$, $d$) space, showing a clear gap between the three groups.
16	
17	\endgroup
18	
19	\begin{table}[ht]
20	\centering
21	\footnotesize
22	\caption{Per-generator TOST equivalence ($\varepsilon{=}|d|{<}0.20$, gen-1 vs.\ gen-2+). Observed $|d|$; \checkmark{} = equivalent ($p_{\mathrm{TOST}} < 0.05$). Features grouped by DDR partition.}
23	\label{tab:tost-per-gen}
24	\resizebox{\columnwidth}{!}{%
25	\renewcommand{\arraystretch}{1.20}%
26	\begin{tabular}{l ccc c ccc}
27	\toprule
28	& \multicolumn{3}{c}{\textbf{Drifting}} & \textbf{Int.} & \multicolumn{3}{c}{\textbf{Near-stationary}} \\
29	\cmidrule(lr){2-4} \cmidrule(lr){5-5} \cmidrule(lr){6-8}
30	\textbf{Generator} & $\bar{H}$ & TTR & hapax & $\sigma_H$ & $H_{\max}$ & tail & $H_{\min}$ \\
31	\midrule
32	Pythia-2.8B  & 1.20 & 0.77 & 0.67 & 0.39 & 0.25          & 0.07\,\checkmark & 0.03\,\checkmark \\
33	Pythia-1B    & 1.40 & 0.80 & 0.65 & 0.53 & 0.21          & 0.08\,\checkmark & 0.02\,\checkmark \\
34	Qwen3-1.7B  & 1.12 & 0.93 & 0.83 & 0.52 & 0.02\,\checkmark & 0.09\,\checkmark & 0.05\,\checkmark \\
35	Llama-3.2-3B & 1.15 & 1.04 & 0.98 & 0.50 & 0.01\,\checkmark & 0.19          & 0.01\,\checkmark \\
36	OLMo-2-1B   & 1.19 & 1.08 & 1.00 & 0.61 & 0.06\,\checkmark & 0.22          & 0.07\,\checkmark \\
37	Qwen3-8B    & 0.86 & 0.71 & 0.66 & 0.37 & 0.04\,\checkmark & 0.15          & 0.01\,\checkmark \\
38	Qwen3-0.6B  & 0.92 & 0.63 & 0.50 & 0.56 & 0.01\,\checkmark & 0.08\,\checkmark & 0.10\,\checkmark \\
39	Mistral-7B   & 0.89 & 0.82 & 0.82 & 0.23 & 0.00\,\checkmark & 0.16          & 0.04\,\checkmark \\
40	\midrule
41	\textbf{Equiv.\ count} & 0/8 & 0/8 & 0/8 & 0/8 & 6/8 & 4/8 & 8/8 \\
42	\bottomrule
43	\end{tabular}}
44	\end{table}
45	
46	\begin{figure}[H]
47	\centering
48	\includegraphics[width=0.85\columnwidth]{fig_ddr_scatter.pdf}
49	\caption{DDR partition in pooled ($|\rho|$, Cohen's $d$) space. Drifting features (green) cluster at high $|\rho|$ and $d$; near-stationary features (orange) cluster near the origin; entropy std (purple) occupies a sole intermediate position. Dashed lines: TOST equivalence bound ($d{=}0.20$) and $|\rho|{=}0.30$. Diamond marker: entropy min (pooled $|\rho|{=}0.40$ reflects the gen-0/gen-1 boundary; gen-1 vs.\ gen-2+ $d{=}0.03$).}
50	\label{fig:ddr-scatter}
51	\end{figure}
52	
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "287f9738-b930-4d35-86a1-395ee9e55a28",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "6d7201dc-8e84-437f-856f-bc48cff29ef5",
  "sourceToolAssistantUUID": "287f9738-b930-4d35-86a1-395ee9e55a28",
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

_source line 19 · 2026-05-23T10:22:53.046Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DM78FEmCMVYeW1BVsADLrY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost_bootstrap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d7201dc-8e84-437f-856f-bc48cff29ef5",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "72099bb6-283a-4488-86ca-4628aeb21184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 20 · 2026-05-23T10:22:53.050Z_

<details><summary>↩ Tool result · `toolu_01DM78FEmCMVYeW1BVsADLrY`</summary>

```text
1	\subsection{TOST Bootstrap Stability}\label{app:tost-bootstrap}
2	
3	To verify that the equivalence conclusions in \S\ref{app:tost} are not sensitive to sample composition, we assess their stability under bootstrap resampling.
4	For each of four representative features, we run 1{,}000 bootstrap iterations (base seed\,=\,42): each iteration independently resamples with replacement from the gen-1 and gen-2+ pools, recomputes Cohen's $d$ and the TOST $p$-value (equivalence margin $|d| < 0.20$).
5	
6	\begin{table}[ht]
7	\centering
8	\footnotesize
9	\caption{Bootstrap stability of TOST equivalence ($B{=}1{,}000$, margin $|d|{<}0.20$). Rejection rate = fraction of bootstrap iterations where TOST rejects non-equivalence at $\alpha{=}0.05$.}
10	\label{tab:tost-bootstrap}
11	\resizebox{\linewidth}{!}{%
12	\begin{tabular}{l c c c}
13	\toprule
14	\textbf{Feature} & \textbf{Rejection rate} & \textbf{Median $d$} & \textbf{$d$ 95\% CI} \\
15	\midrule
16	entropy\_max  & 100\% (1000/1000) & 0.062  & [0.037, 0.088] \\
17	entropy\_min  & 100\% (1000/1000) & $-$0.016 & [$-$0.042, 0.011] \\
18	tail\_decay   & 100\% (1000/1000) & 0.088  & [0.065, 0.111] \\
19	\midrule
20	entropy\_std  & 0\% (0/1000)      & 0.458  & [0.435, 0.479] \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	All three near-stationary features achieve a 100\% rejection rate across 1{,}000 bootstrap iterations, and their effect-size 95\% CIs fall entirely within the $\pm 0.20$ equivalence margin.
26	Entropy std, included as an intermediate control, is never rejected (0\%), with its CI $[0.435, 0.479]$ lying entirely outside the margin.
27	No feature exhibits boundary-crossing: the classification of each feature is unanimous across all bootstrap samples, confirming that the equivalence conclusions are robust to resampling variability.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72099bb6-283a-4488-86ca-4628aeb21184",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "96067d1f-acc6-4ac5-a96b-79b3d955c79b",
  "sourceToolAssistantUUID": "72099bb6-283a-4488-86ca-4628aeb21184",
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

_source line 21 · 2026-05-23T10:22:53.064Z_

<details open><summary>🔧 Tool call — Read · `toolu_015eoLz7XoTX1BaeykzYQxnu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96067d1f-acc6-4ac5-a96b-79b3d955c79b",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6e9fc51e-be81-4294-babe-165522805402",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 22 · 2026-05-23T10:22:53.067Z_

<details><summary>↩ Tool result · `toolu_015eoLz7XoTX1BaeykzYQxnu`</summary>

```text
1	This appendix validates the causal predictive power of DDR features through three complementary analyses: permutation importance, Granger causality, and feature intervention.
2	
3	\paragraph{Permutation Importance.}
4	Table~\ref{tab:perm-importance} reports the mean F1 drop when each feature's values are randomly shuffled across the test set (baseline F1\,=\,0.771).
5	Drifting features dominate: their average F1 drop (0.187) is $5.5\times$ larger than the near-stationary average (0.034), confirming that location-shift features, not shape features, drive depth classification.
6	
7	\begin{table}[ht]
8	\centering
9	\small
10	\caption{Permutation importance (8-gen LOGO). Each feature is shuffled independently; the resulting F1 drop quantifies marginal importance. Drifting features average $0.187$ vs.\ near-stationary $0.034$ ($5.5\times$).}
11	\label{tab:perm-importance}
12	\resizebox{\linewidth}{!}{%
13	\begin{tabular}{llcr}
14	\toprule
15	\textbf{Feature} & \textbf{Group} & \textbf{Mean F1 Drop} & \textbf{Rank} \\
16	\midrule
17	hapax\_ratio  & Drifting      & 0.235 & 1 \\
18	entropy\_mean & Drifting      & 0.170 & 2 \\
19	ttr           & Drifting      & 0.156 & 3 \\
20	entropy\_max  & Near-stat.    & 0.070 & 4 \\
21	entropy\_std  & Intermediate  & 0.057 & 5 \\
22	entropy\_min  & Near-stat.    & 0.019 & 6 \\
23	tail\_decay   & Near-stat.    & 0.014 & 7 \\
24	\bottomrule
25	\end{tabular}}
26	\end{table}
27	
28	\paragraph{Granger Causality.}
29	Table~\ref{tab:granger} reports Fisher-combined $p$-values from panel Granger causality tests (lag\,=\,1) across 8 generators ($N$\,=\,29{,}095).
30	Six of seven features exhibit significant Granger causality ($p < 0.001$), meaning past feature values predict future depth beyond what past depth alone explains.
31	The sole exception is entropy\_min ($p$\,=\,0.375), providing additional evidence for its near-stationary classification: it carries neither large marginal importance (Table~\ref{tab:perm-importance}, rank 7) nor temporal predictive direction.
32	
33	\begin{table}[ht]
34	\centering
35	\small
36	\caption{Granger causality (Fisher combined across 8 generators, lag\,=\,1, $N$\,=\,29{,}095). $\Delta R^2$ is reported where available.}
37	\label{tab:granger}
38	\resizebox{\linewidth}{!}{%
39	\begin{tabular}{lccc}
40	\toprule
41	\textbf{Feature} & \textbf{Combined $p$} & $\boldsymbol{\Delta R^2}$ & \textbf{Significant} \\
42	\midrule
43	entropy\_std  & $< 0.001$ & 0.031 & Yes \\
44	hapax\_ratio  & $< 0.001$ & ---   & Yes \\
45	ttr           & $< 0.001$ & ---   & Yes \\
46	entropy\_mean & $< 0.001$ & ---   & Yes \\
47	entropy\_max  & $< 0.001$ & ---   & Yes \\
48	tail\_decay   & $< 0.001$ & ---   & Yes \\
49	entropy\_min  & $0.375$   & ---   & No  \\
50	\bottomrule
51	\end{tabular}}
52	\end{table}
53	
54	\paragraph{Key Findings.}
55	\begin{enumerate}[nosep,leftmargin=*]
56	\item \textbf{Drifting dominance.} The $5.5\times$ permutation-importance gap confirms that drifting features (entropy\_mean, ttr, hapax\_ratio) are the primary depth signal carriers, consistent with the DDR partition derived from convergence analysis (\S\ref{sec:results-differential}).
57	
58	\item \textbf{Entropy\_min lacks causal direction.} Beyond its small effect size (F1 drop\,=\,0.019), entropy\_min is the only feature without significant Granger causality ($p$\,=\,0.375). This strengthens the near-stationary classification: the feature is neither marginally important nor temporally predictive.
59	
60	\item \textbf{Entropy\_max asymmetry.} Entropy\_max ranks fourth in permutation importance (F1 drop\,=\,0.070) but produces the largest degradation in the counterfactual intervention ($-$2.0\,pp), indicating that it provides unique signal not redundant with other features; its causal contribution exceeds its marginal importance.
61	
62	\item \textbf{Mistral heterogeneity.} In per-generator Granger tests, Mistral-7B shows non-significant hapax\_ratio and ttr ($p > 0.4$), though Fisher combination across generators remains significant. This generator-specific attenuation partly explains Mistral's lowest LOGO F1 (0.605) and suggests that DDR depth signatures are weaker in models with heavier repetition penalties.
63	\end{enumerate}
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e9fc51e-be81-4294-babe-165522805402",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "e141ba8e-1be3-4105-80af-cf3a8afdbde6",
  "sourceToolAssistantUUID": "6e9fc51e-be81-4294-babe-165522805402",
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

_source line 23 · 2026-05-23T10:22:53.971Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RKioHyi98Rhu1q6oMwxYx9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e141ba8e-1be3-4105-80af-cf3a8afdbde6",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c5a3914f-c413-4f2f-afcb-2d4c01e1fb0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 24 · 2026-05-23T10:22:53.977Z_

<details><summary>↩ Tool result · `toolu_01RKioHyi98Rhu1q6oMwxYx9`</summary>

```text
1	\subsection*{Data-Driven Clustering}
2	
3	To assess the DDR partition structure and determine whether the drifting/non-drifting split is data-driven, we apply $k$-means clustering ($k \in \{2,3,4,5\}$) to the seven features in standardized $(|\rho|, d)$ space (Table~\ref{tab:clustering}).
4	
5	\begin{table}[ht]
6	\centering
7	\small
8	\caption{$k$-means clustering of 7 features in $(|\rho|, d)$ space.}
9	\label{tab:clustering}
10	\resizebox{\linewidth}{!}{%
11	\begin{tabular}{ccp{5.5cm}}
12	\toprule
13	$k$ & Silhouette & Clusters \\
14	\midrule
15	2 & \textbf{0.660} & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$\sigma_H$, $H_{\min}$, $H_{\max}$, tail\} \\
16	3 & 0.532 & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$\sigma_H$, $H_{\max}$, tail\} $\mid$ \{$H_{\min}$\} \\
17	4 & 0.527 & \{$\bar{H}$, TTR, hapax\} $\mid$ \{$H_{\max}$, tail\} $\mid$ \{$\sigma_H$\} $\mid$ \{$H_{\min}$\} \\
18	\bottomrule
19	\end{tabular}}
20	\end{table}
21	
22	The primary drifting/non-drifting split ($k{=}2$, silhouette\,=\,0.660) is the strongest cluster structure.
23	At $k{=}3$, entropy min forms its own cluster rather than joining the near-stationary group because its pooled $|\rho|{=}0.40$ (driven by the gen-0/gen-1 boundary) places it far from other near-stationary features in $\rho$ space.
24	The 3/1/3 DDR partition resolves this by using the gen-1 vs.\ gen-2+ Cohen's $d$ ($d{=}0.03$) to place entropy min in the near-stationary group, a domain-informed refinement that unsupervised clustering cannot recover from pooled statistics alone.
25	At $k{=}4$ (silhouette\,=\,0.571), entropy std separates from the near-stationary group, consistent with its intermediate DDR classification.
26	
27	\paragraph{Exhaustive partition enumeration.}
28	To confirm that the three-vs-four split is optimal rather than incidental, we enumerate all $\binom{7}{3}{=}35$ possible ways to assign three features to a ``drifting'' group and the remaining four to ``non-drifting,'' computing the silhouette score for each partition in standardized $(|\rho|, d)$ space.
29	The observed DDR partition (\{entropy mean, TTR, hapax ratio\}) achieves the highest silhouette (0.660), with a gap of 0.18 to the second-ranked split; 20 of 35 partitions produce negative silhouette scores.
30	
31	\paragraph{Per-generator replication.}
32	To rule out the possibility that the pooled silhouette is an artifact of mixing heterogeneous generators, we repeat the $(|\rho|, d)$ clustering independently for each of the eight generators.
33	Every generator recovers the identical \{$\bar{H}$, TTR, hapax\} vs.\ \{$\sigma_H$, $H_{\min}$, $H_{\max}$, tail\} partition, with silhouette scores ranging from 0.505 (Pythia-1B) to 0.760 (Mistral-7B-v0.3; mean\,=\,0.651).
34	No generator falls below the 0.50 moderate-structure threshold, confirming that the two-cluster structure is a per-generator property rather than a pooling artifact.
35	
36	\subsection*{TOST Equivalence Bound Sensitivity}
37	\label{app:tost-sensitivity}
38	
39	Table~\ref{tab:tost-sensitivity} shows the fraction of generators for which each feature passes the TOST equivalence test (gen-1 vs.\ gen-2+, $\alpha{=}0.05$) at three equivalence bounds $\varepsilon$.
40	
41	\begin{table}[ht]
42	\centering
43	\small
44	\caption{TOST equivalence pass rate across 8 generators at varying $\varepsilon$.}
45	\label{tab:tost-sensitivity}
46	\resizebox{\linewidth}{!}{%
47	\begin{tabular}{llccc}
48	\toprule
49	\textbf{DDR Zone} & \textbf{Feature} & $\boldsymbol{\varepsilon{=}0.15}$ & $\boldsymbol{\varepsilon{=}0.20}$ & $\boldsymbol{\varepsilon{=}0.25}$ \\
50	\midrule
51	\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 0/8 & 0/8 & 0/8 \\
52	 & TTR & 0/8 & 0/8 & 0/8 \\
53	 & hapax ratio & 0/8 & 0/8 & 0/8 \\
54	\midrule
55	Intermediate & $\sigma_H$ (ent.\ std) & 0/8 & 0/8 & 0/8 \\
56	\midrule
57	\multirow{3}{*}{Near-stat.} & $H_{\min}$ (ent.\ min) & 7/8 & 8/8 & 8/8 \\
58	 & $H_{\max}$ (ent.\ max) & 6/8 & 6/8 & 6/8 \\
59	 & tail decay & 4/8 & 4/8 & 7/8 \\
60	\bottomrule
61	\end{tabular}}
62	\end{table}
63	
64	The partition is robust to the equivalence bound: drifting features reject equivalence at all $\varepsilon$ for all generators, while entropy min passes even at the stricter bound $\varepsilon{=}0.15$ (7/8 generators).
65	Tail decay is the most $\varepsilon$-sensitive near-stationary feature, passing 4/8 at $\varepsilon{=}0.20$ but 7/8 at $\varepsilon{=}0.25$; the four non-passing generators show $|d|{=}0.15$--$0.22$, still well below the drifting threshold ($d > 0.50$).
66	Entropy max is stable across all three bounds (6/8), with the two failures (Pythia-1B $d{=}0.21$, Pythia-2.8B $d{=}0.25$) reflecting same-family reference affinity with the Pythia-410M reference model.
67	
68	\paragraph{TOST margin rationale.}
69	We adopt $\varepsilon{=}0.20$ as the primary equivalence bound, corresponding to Cohen's ``small effect'' threshold ($d{=}0.20$; \citealp{cohen1988statistical}).
70	This choice reflects a principled smallest effect size of interest (SESOI): effects below $d{=}0.20$ are conventionally negligible and unlikely to carry practical discriminative value for depth classification.
71	The bound is conservative relative to the drifting--stationary gap ($d_{\min}^{\text{drift}}{=}0.76$ vs.\ $\varepsilon{=}0.20$, a $3.8{\times}$ margin), ensuring that the equivalence test has adequate power to confirm near-stationarity without risk of misclassifying genuinely drifting features.
72	As Table~\ref{tab:tost-sensitivity} shows, conclusions are qualitatively identical at $\varepsilon{=}0.15$ and $\varepsilon{=}0.25$, confirming insensitivity to the specific bound choice.
73	LOFO analysis independently corroborates this boundary: near-stationary features contribute ${<}2$\,pp marginal importance (Appendix~\ref{app:lofo}), empirically validating $\varepsilon{=}0.20$ as a task-relevant threshold.
74	
75	\paragraph{Threshold sensitivity.}
76	To address concerns about the sensitivity of the drifting-boundary threshold,
77	we sweep $|d|$ from $0.10$ to $0.80$ in increments of $0.05$ and record the
78	resulting binary partition (drifting vs.\ stationary) along with the silhouette
79	score in standardized $(|\rho|, d)$ space.
80	Across the entire range, only \emph{three} distinct partitions emerge,
81	reflecting natural gaps between feature clusters rather than threshold artifacts.
82	The three-feature drifting set (entropy mean, TTR, hapax ratio)
83	is stable across $|d| \in [0.50,\, 0.75]$ with a silhouette of $0.660$---the
84	peak value in the sweep.
85	Including the intermediate feature entropy std ($d{=}0.49$) yields a
86	4/3 partition stable across $|d| \in [0.10,\, 0.45]$ (silhouette\,=\,0.451).
87	The partition used in our analysis corresponds to the peak-silhouette region,
88	confirming that the drifting/stationary boundary reflects a natural gap in the
89	$(|\rho|, d)$ landscape rather than an artifact of a particular
90	threshold choice.
91	
92	\paragraph{Partition stability across $\varepsilon$ thresholds.}
93	\label{app:epsilon-sweep}
94	
95	The DDR partition classifies features as non-stationary ($d \geq \varepsilon$) or stationary ($d < \varepsilon$) based on pooled Cohen's $d$ (\S\ref{sec:results-differential}).
96	Table~\ref{tab:epsilon-sweep} reports the critical $\varepsilon$ at which each feature's classification changes; the three drifting and three near-stationary features maintain their classification for all $\varepsilon \in [0.10, 0.75]$.
97	
98	\begin{table}[ht]
99	\centering
100	\small
101	\caption{Partition stability under varying $\varepsilon$. Critical threshold: the $\varepsilon$ above which a feature is reclassified as stationary. The drifting/near-stationary split is invariant for $\varepsilon \in [0.10, 0.75]$; only entropy std ($d{=}0.55$) changes at $\varepsilon > 0.55$.}
102	\label{tab:epsilon-sweep}
103	\resizebox{\linewidth}{!}{%
104	\begin{tabular}{llcc}
105	\toprule
106	\textbf{DDR Zone} & \textbf{Feature} & \textbf{Pooled $d$} & \textbf{Stationary at $\varepsilon >$} \\
107	\midrule
108	\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 1.17 & 1.17 \\
109	 & TTR & 0.88 & 0.88 \\
110	 & hapax ratio & 0.76 & 0.76 \\
111	\midrule
112	Intermediate & $\sigma_H$ (ent.\ std) & 0.55 & 0.55 \\
113	\midrule
114	\multirow{3}{*}{Near-stat.} & $H_{\max}$ (ent.\ max) & 0.08 & 0.08 \\
115	 & tail decay & 0.08 & 0.08 \\
116	 & $H_{\min}$ (ent.\ min) & 0.016 & 0.016 \\
117	\bottomrule
118	\end{tabular}}
119	\end{table}
120	
121	\noindent The 3/1/3 partition is stable across $\varepsilon \in [0.10, 0.75]$: the three drifting features remain non-stationary at all $\varepsilon < 0.76$, the three near-stationary features remain stationary at all $\varepsilon > 0.08$, and only entropy std changes classification (becoming stationary at $\varepsilon > 0.55$), confirming it as the sole threshold-sensitive feature.
122	The minimum gap between adjacent zone boundaries ($d_{\text{hapax}} - d_{\sigma_H} = 0.21$) exceeds typical effect-size estimation uncertainty, providing a margin against sampling noise.
123	
124	\subsection*{Holdout Generator Split Validation}
125	\label{app:holdout-split}
126	
127	To confirm the DDR partition is not an artifact of the specific generator pool, we split the eight generators into disjoint selection (4) and validation (4) sets, compute per-subset pooled $(|\rho|, d)$, and check whether all seven features receive the same zone assignment in both subsets.
128	We evaluate two complementary splits to avoid dependence on a single partition:
129	Split~A selects \{Pythia-2.8B, Qwen3-1.7B, OLMo, Mistral\} (validation: Pythia-1B, Qwen3-0.6B, Qwen3-8B, Llama);
130	Split~B selects \{Pythia-1B, Qwen3-0.6B, OLMo, Mistral\} (validation: Pythia-2.8B, Qwen3-1.7B, Qwen3-8B, Llama).
131	
132	\begin{table}[ht]
133	\centering
134	\small
135	\caption{Holdout split validation of the DDR partition. Selection (sel) and validation (val) $|\rho|$ and $d$ for two disjoint 4/4 generator splits. Zone assignment is identical across all four subsets for every feature.}
136	\label{tab:holdout-split}
137	\resizebox{\linewidth}{!}{%
138	\begin{tabular}{llcccccc}
139	\toprule
140	& & \multicolumn{3}{c}{\textbf{Split A}} & \multicolumn{3}{c}{\textbf{Split B}} \\
141	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
142	\textbf{Zone} & \textbf{Feature} & sel $|\rho|$ & val $|\rho|$ & $\Delta|\rho|$ & sel $|\rho|$ & val $|\rho|$ & $\Delta|\rho|$ \\
143	\midrule
144	\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 0.60 & 0.58 & 0.02 & 0.60 & 0.58 & 0.02 \\
145	 & TTR & 0.61 & 0.59 & 0.02 & 0.60 & 0.59 & 0.01 \\
146	 & hapax ratio & 0.62 & 0.60 & 0.02 & 0.62 & 0.61 & 0.01 \\
147	\midrule
148	Intermediate & $\sigma_H$ (ent.\ std) & 0.19 & 0.21 & 0.02 & 0.22 & 0.17 & 0.05 \\
149	\midrule
150	\multirow{3}{*}{Near-stat.} & $H_{\min}$ (ent.\ min) & 0.39 & 0.36 & 0.03 & 0.38 & 0.37 & 0.01 \\
151	 & $H_{\max}$ (ent.\ max) & 0.05 & 0.05 & 0.00 & 0.04 & 0.06 & 0.02 \\
152	 & tail decay & 0.10 & 0.08 & 0.02 & 0.11 & 0.07 & 0.04 \\
153	\bottomrule
154	\end{tabular}}
155	\end{table}
156	
157	Under simple joint $(|\rho|, d)$ thresholds, both splits produce a 3/2/2 partition: entropy min is classified as a second intermediate feature due to its elevated pooled $|\rho|$ (0.36--0.39).
158	However, entropy min's binary (gen-1 vs.\ gen-2+) $d$ values are uniformly below 0.06 across all four split${\times}$subset combinations, consistent with near-stationarity on the task-relevant metric; its pooled $|\rho|$ reflects change concentrated at the gen-0/gen-1 boundary rather than sustained drift.
159	Five of seven features are unambiguously classified under any reasonable criterion; entropy min's boundary status is resolved by the binary-task $d$ criterion.
160	
161	Selection and validation subsets produce identical partitions in both splits (Table~\ref{tab:holdout-split}; Figure~\ref{fig:holdout-scatter}).
162	The maximum $\Delta|\rho|$ between selection and validation is 0.05 (entropy std, Split~B), and the minimum gap between adjacent zones remains $>$0.15 in all subsets.
163	
164	\begin{figure}[H]
165	\centering
166	\includegraphics[width=\linewidth]{fig_ddr_holdout_split.pdf}
167	\caption{Holdout split validation in $(|\rho|, d)$ space. Filled markers: selection set; hollow: validation set. Zone assignments are identical across subsets; selection/validation pairs cluster tightly for all features.}
168	\label{fig:holdout-scatter}
169	\end{figure}
170	
171	\subsection*{Heteroscedasticity Sensitivity}
172	\label{app:heteroscedasticity}
173	
174	Levene tests reject equal variance between gen-1 and gen-2+ for drifting features ($p < 10^{-10}$; variance ratios 1.86--2.21).
175	To verify that the DDR partition is robust to this heteroscedasticity, we supplement pooled Cohen's $d$ with Glass's $\Delta$ (using the gen-1 standard deviation as denominator) and Cliff's $\delta$ (a non-parametric ordinal effect size; Table~\ref{tab:effect-sizes}).
176	
177	\begin{table}[ht]
178	\centering
179	\small
180	\caption{Effect size comparison (gen-1 vs.\ gen-2+, $N$\,=\,29{,}095). Glass's $\Delta$ uses the gen-1 SD as denominator; Cliff's $\delta$ thresholds follow Romano et al.\ (2006): $|\delta| < 0.147$ negligible, $< 0.33$ small, $< 0.474$ medium, otherwise large.}
181	\label{tab:effect-sizes}
182	\begin{tabular}{llrrr}
183	\toprule
184	\textbf{Zone} & \textbf{Feature} & \textbf{$|d|$} & \textbf{$|\Delta|$} & \textbf{$|\delta|$} \\
185	\midrule
186	\multirow{3}{*}{Drifting} & ent.\ mean & 1.054 & 1.410 & 0.587 \\
187	 & TTR & 0.814 & 1.116 & 0.510 \\
188	 & hapax ratio & 0.735 & 0.936 & 0.528 \\
189	\midrule
190	Intermediate & ent.\ std & 0.457 & 0.605 & 0.295 \\
191	\midrule
192	\multirow{3}{*}{Near-stat.} & tail decay & 0.087 & 0.099 & 0.072 \\
193	 & ent.\ max & 0.062 & 0.065 & 0.021 \\
194	 & ent.\ min & 0.016 & 0.015 & 0.354$^{\dagger}$ \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	\noindent Effect sizes in Table~\ref{tab:effect-sizes} are computed on the binary task (gen-1 vs.\ gen-2+); the main text (\S\ref{sec:results-differential}) reports 3-class pooled $d$ values (e.g., hapax ratio $d{=}0.76$), which are slightly larger because the gen-0/gen-1 contrast contributes additional separation.
200	Glass's $\Delta$ amplifies drifting effects (1.41 vs.\ 1.05 for entropy mean) because gen-2+ variance exceeds gen-1 variance (ratio 2.08), making the pooled Cohen's $d$ conservative.
201	Near-stationary features remain negligible under both parametric metrics ($|\Delta| \leq 0.099$).
202	The minimum drifting-to-maximum-near-stationary gap is $9.5\times$ under Glass's $\Delta$ (0.936\,/\,0.099); heteroscedasticity does not erode the partition.
203	Cliff's $\delta$ classifies all drifting features as ``large'' ($|\delta| > 0.474$) and entropy std as ``small'' ($|\delta|{=}0.295$), consistent with the parametric partition.
204	
205	\noindent $^{\dagger}$Entropy min's elevated Cliff's $\delta$ (0.354, ``medium'') reflects distributional shape asymmetry between gen-1 and gen-2+ that rank-based statistics detect but location measures do not (Cohen's $d{=}0.016$, Glass's $\Delta{=}0.015$).
206	This is consistent with its documented boundary status (\S\ref{sec:results-differential}): the gen-0/gen-1 transition produces rank-order shifts that persist into deeper generations without affecting the mean.
207	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5a3914f-c413-4f2f-afcb-2d4c01e1fb0c",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "26658176-e9e0-47e6-b6a9-a7ab8b487d04",
  "sourceToolAssistantUUID": "c5a3914f-c413-4f2f-afcb-2d4c01e1fb0c",
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

_source line 25 · 2026-05-23T10:22:54.041Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KSCD68d2BuPfbMCJnaEpi1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26658176-e9e0-47e6-b6a9-a7ab8b487d04",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLQpqFisGF54pie5iXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe478285-e754-4c88-a0d2-0e8969b097f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HPF3CYBEaxjVZxGNFpztDi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 801,
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

_source line 26 · 2026-05-23T10:22:54.045Z_

<details><summary>↩ Tool result · `toolu_01KSCD68d2BuPfbMCJnaEpi1`</summary>

```text
1	\subsection{9-Generator Scale Evaluation}\label{app:9gen-scale}
2	
3	This analysis extends the 8-generator LOGO evaluation to nine generators by adding Gemma-2-2B, a model from a previously unrepresented architecture family (Gemma).
4	All results use class-balanced LOGO; the 8-gen averages here (0.770/0.701) differ slightly from Table~\ref{tab:logo-results} (0.762/0.694), which uses an unfiltered protocol.
5	Table~\ref{tab:9gen-logo} reports per-generator LOGO performance under this expanded set.
6	
7	\begin{table}[ht]
8	\centering
9	\caption{9-generator LOGO evaluation. Each row holds out the listed generator at test time. 3-class: gen-0\,/\,gen-1\,/\,gen-2+; binary: gen-1 vs.\ gen-2+. 95\% bootstrap CIs in brackets.}
10	\label{tab:9gen-logo}
11	\small
12	\resizebox{\linewidth}{!}{%
13	\begin{tabular}{llr cc cc}
14	\toprule
15	\textbf{Generator} & \textbf{Family} & \textbf{Params} & \textbf{3-class F1} & \textbf{95\% CI} & \textbf{Binary F1} & \textbf{95\% CI} \\
16	\midrule
17	Pythia-1B       & Pythia  & 1.0B & 0.857 & [0.848, 0.866] & 0.785 & --- \\
18	Qwen3-0.6B      & Qwen    & 0.6B & 0.819 & [0.807, 0.830] & 0.743 & --- \\
19	Pythia-2.8B     & Pythia  & 2.8B & 0.812 & [0.801, 0.822] & 0.728 & --- \\
20	Qwen3-1.7B      & Qwen    & 1.7B & 0.811 & [0.800, 0.823] & 0.746 & --- \\
21	OLMo-2-1B       & OLMo    & 1.5B & 0.773 & [0.762, 0.784] & 0.692 & --- \\
22	Llama-3.2-3B    & Llama   & 3.2B & 0.759 & [0.748, 0.770] & 0.680 & --- \\
23	Qwen3-8B        & Qwen    & 8.2B & 0.696 & [0.683, 0.709] & 0.647 & [0.631, 0.664] \\
24	Gemma-2-2B      & Gemma   & 2.6B & 0.628 & [0.622, 0.634] & 0.440 & [0.432, 0.449] \\
25	Mistral-7B      & Mistral & 7.0B & 0.605 & [0.593, 0.617] & 0.534 & --- \\
26	\midrule
27	\textbf{Average (9-gen)} & & & \textbf{0.751} & & \textbf{0.666} & \\
28	\textbf{Average (8-gen)} & & & \textbf{0.770} & & \textbf{0.701} & \\
29	\bottomrule
30	\end{tabular}}
31	\end{table}
32	
33	\paragraph{Overall comparison.}
34	Adding Gemma-2-2B reduces the mean 3-class LOGO F1 from 0.770 (8-gen) to 0.751 (9-gen), a drop of $\Delta = -0.019$.
35	The per-generator F1 values for the original eight generators shift by at most $[-0.011, +0.002]$, indicating that the inclusion of Gemma data in training does not destabilize existing generalization patterns.
36	
37	\paragraph{Gemma-2-2B anomaly.}
38	Gemma-2-2B is the weakest held-out generator: 3-class F1\,=\,0.628, binary F1\,=\,0.440.
39	Per-class breakdown reveals a striking asymmetry: gen-0 F1\,=\,0.991 and gen-2+ F1\,=\,0.856, but gen-1 F1\,=\,0.036; the classifier almost entirely fails to identify first-generation Gemma continuations.
40	This is not a data-quality artifact: the Gemma-2-2B partition contains 4{,}957 instances with a balanced depth distribution ($\sim$990 per level).
41	A plausible explanation is that Gemma-2's first-generation continuations occupy a region of feature space highly similar to human-written text (gen-0), causing systematic misclassification of gen-1 as gen-0 or gen-2+.
42	This constitutes an architecture-specific generalization limitation rather than a systemic failure of the depth profiling approach.
43	Several architectural differences may explain this behavior: (a)~Gemma-2's distinct attention mechanism and SentencePiece tokenizer with a larger vocabulary may produce first-generation continuations whose feature-space signature closely resembles human text, causing systematic gen-0/gen-1 confusion; (b)~this anomaly does not affect DDR's validity for the remaining eight generators, where per-generator F1 shifts by at most 0.011 upon Gemma inclusion.
44	
45	\paragraph{Scale effect.}
46	A clear parameter-count gradient emerges across the nine generators: three of four sub-1.7B generators achieve F1\,$>$\,0.81 (OLMo-2-1B at 0.773 is the exception), mid-range models (2--3B) cluster at 0.63--0.81, and large models (7B+) fall to 0.60--0.70.
47	Qwen3-8B (8.2B parameters) achieves 3-class F1\,=\,0.696 under the 9-gen split, compared to 0.701 in the class-balanced 8-gen evaluation; this small difference reflects the changed training composition rather than a property of the Qwen3-8B generator itself.
48	
49	\paragraph{14B-parameter evidence.}
50	Preliminary evidence from a 14.7B generator (Qwen3-14B-Base) confirms that the DDR partition persists at larger scale: Cohen's $d$ for drifting features remains in the large-effect range ($d{=}0.78$--$1.12$), though Spearman $|\rho|$ attenuates by 21--35\%, with entropy mean falling just below the drifting threshold ($|\rho|{=}0.39 < 0.40$, $d{=}0.78$).
51	This scale-dependent signal compression is consistent with larger models producing more self-typical outputs that narrow inter-depth contrasts; the partition structure is preserved even as absolute effect sizes compress.
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe478285-e754-4c88-a0d2-0e8969b097f2",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "7f205387-6bf1-4e3f-9fb5-0db9efe460db",
  "sourceToolAssistantUUID": "fe478285-e754-4c88-a0d2-0e8969b097f2",
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

_source line 27 · 2026-05-23T10:22:55.509Z_

Now let me continue reading the remaining files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f205387-6bf1-4e3f-9fb5-0db9efe460db",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRBnao6x7uSrPU5pQu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0703d336-6139-4048-8386-ab900bde56d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011k8GzFMPjcTaUwx55RLyGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26293,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26293,
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

_source line 28 · 2026-05-23T10:22:56.577Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CRSErzdDo8ZWJLhnf5NaXr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_generator_subsets.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0703d336-6139-4048-8386-ab900bde56d1",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRBnao6x7uSrPU5pQu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8b665b63-0563-40ae-929e-7c9f5a492a3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011k8GzFMPjcTaUwx55RLyGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26293,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26293,
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

_source line 29 · 2026-05-23T10:22:56.583Z_

<details><summary>↩ Tool result · `toolu_01CRSErzdDo8ZWJLhnf5NaXr`</summary>

```text
1	Table~\ref{tab:gen-subsets} summarizes the generator subsets used across experiments.
2	
3	\begin{table}[ht]
4	\centering
5	\small
6	\caption{Generator subsets by experiment type.}
7	\label{tab:gen-subsets}
8	\resizebox{\linewidth}{!}{%
9	\begin{tabular}{lcl}
10	\toprule
11	\textbf{Experiment} & $\boldsymbol{N}$ & \textbf{Generators} \\
12	\midrule
13	Main LOGO (Table~\ref{tab:logo-results}) & 8 & All: Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B, Llama, Mistral \\
14	Cross-model chains (Table~\ref{tab:cross-ref}) & 5 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B \\
15	QLoRA (Table~\ref{tab:qlora}) & 6 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B \\
16	Temperature ablation (Table~\ref{tab:sampling-ablation}) & 4 & Py-2.8B, OLMo, Qw-1.7B/0.6B \\
17	Prompt-type (Appendix~\ref{app:prompt-type}) & 1 & Py-2.8B only \\
18	Cross-domain (Table~\ref{tab:domain}) & 3 & Py-1B, Qw-1.7B, Mistral \\
19	Instruct (Table~\ref{tab:instruct}) & 3 & OLMo, Qw-1.7B, Llama \\
20	Downstream (Appendix~\ref{app:downstream}) & 5 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	The 5-generator set was the initial development subset; Qwen3-8B was added for scale evaluation, and Llama-3.2-3B and Mistral-7B-v0.3 were added last for family-diversity testing.
26	Subset differences reflect chronological expansion rather than selective reporting.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b665b63-0563-40ae-929e-7c9f5a492a3d",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "5517bdcf-192e-43e6-8303-0d221d6dab76",
  "sourceToolAssistantUUID": "8b665b63-0563-40ae-929e-7c9f5a492a3d",
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

_source line 30 · 2026-05-23T10:22:56.599Z_

<details open><summary>🔧 Tool call — Read · `toolu_015RWM2fHQeNLiNn8hiyrXEE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_prompt_type.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5517bdcf-192e-43e6-8303-0d221d6dab76",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRBnao6x7uSrPU5pQu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "90e20009-fa11-4e71-a8dd-cca60e97a616",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011k8GzFMPjcTaUwx55RLyGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26293,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26293,
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

_source line 31 · 2026-05-23T10:22:56.608Z_

<details><summary>↩ Tool result · `toolu_015RWM2fHQeNLiNn8hiyrXEE`</summary>

```text
1	We evaluate depth profiling under three prompt types using Pythia-2.8B. Each uses 995 seeds $\times$ 5 depths. The exact templates are:
2	
3	\begin{tcolorbox}[colback=yellow!5!white, colframe=gray!50, title=Prompt Templates, breakable, fonttitle=\bfseries\small]
4	\textbf{Continuation:} \texttt{Continue the following text: \{text\}}\\[4pt]
5	\textbf{Elaboration:} \texttt{Elaborate on the following text: \{text\}}\\[4pt]
6	\textbf{Inspired rewriting:} \texttt{Write a new passage inspired by the following text: \{text\}}
7	\end{tcolorbox}
8	
9	\paragraph{Within-prompt-type classification.}
10	5-fold CV macro-F1: continuation 0.78, rewriting 0.74, elaboration 0.73. All three prompt types exhibit the same differential depth response pattern: drifting features (hapax ratio, TTR, entropy mean) show consistent monotonic trends, while near-stationary features (entropy max, tail decay) change by less than 5\%.
11	
12	\paragraph{Cross-prompt-type transfer (LOPTO).}
13	Leave-one-prompt-type-out evaluation yields average F1\,=\,0.753, which confirms that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\% per depth step), followed by rewriting (6.1\%) and elaboration (1.4\%), consistent with continuation chains applying less semantic constraint on the output.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90e20009-fa11-4e71-a8dd-cca60e97a616",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "4661b74b-66af-44f3-8a30-efb364a94695",
  "sourceToolAssistantUUID": "90e20009-fa11-4e71-a8dd-cca60e97a616",
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

_source line 32 · 2026-05-23T10:22:56.808Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ns8zhjf6tygS85VJLULeMA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_transfer.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4661b74b-66af-44f3-8a30-efb364a94695",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRBnao6x7uSrPU5pQu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "385dd910-4bd7-4fcb-8f74-3d6db0341c52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011k8GzFMPjcTaUwx55RLyGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26293,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26293,
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

_source line 33 · 2026-05-23T10:22:56.812Z_

<details><summary>↩ Tool result · `toolu_01Ns8zhjf6tygS85VJLULeMA`</summary>

```text
1	To isolate the depth signal from generator identity, we train a binary classifier (gen-1 vs.\ gen-2+) on each of the eight generators independently and evaluate on all others.
2	Table~\ref{tab:transfer} reports the full 8$\times$8 transfer matrix; Figure~\ref{fig:transfer-heatmap} (main text) visualizes it as a heatmap.
3	Note that these classifiers are trained with a binary objective, whereas the LOGO classifiers in Table~\ref{tab:logo-results} are trained on a 3-class task and evaluated on the binary subtask; the two setups are therefore not directly comparable.
4	
5	\begin{table}[ht]
6	\centering
7	\scriptsize
8	\setlength{\tabcolsep}{3pt}
9	\caption{Cross-generator binary F1 transfer matrix (gen-1 vs.\ gen-2+). Each row trains on one generator; each column evaluates on another. Diagonal entries (\underline{underlined}) are within-generator. All 56 off-diagonal pairs exceed chance (0.5). Classifiers use the same 7-feature XGBoost configuration as LOGO but are trained with a binary objective.}
10	\label{tab:transfer}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{l|cccccccc}
13	\toprule
14	\textbf{Train $\backslash$ Test} & \textbf{Py-2.8B} & \textbf{Py-1B} & \textbf{Qw-0.6B} & \textbf{Qw-1.7B} & \textbf{Qw-8B} & \textbf{OLMo-1B} & \textbf{Ll-3B} & \textbf{Mi-7B} \\
15	\midrule
16	Py-2.8B  & \underline{0.985} & 0.873 & 0.823 & 0.833 & 0.741 & 0.829 & 0.815 & 0.712 \\
17	Py-1B    & 0.834 & \underline{0.987} & 0.828 & 0.821 & 0.704 & 0.778 & 0.764 & 0.620 \\
18	Qw-0.6B  & 0.786 & 0.846 & \underline{0.991} & 0.851 & 0.786 & 0.795 & 0.760 & 0.680 \\
19	Qw-1.7B  & 0.794 & 0.839 & 0.859 & \underline{0.989} & 0.790 & 0.817 & 0.798 & 0.717 \\
20	Qw-8B   & 0.811 & 0.836 & 0.853 & 0.855 & \underline{0.984} & 0.848 & 0.839 & 0.790 \\
21	OLMo-1B  & 0.811 & 0.827 & 0.837 & 0.852 & 0.803 & \underline{0.988} & 0.828 & 0.763 \\
22	Ll-3B    & 0.856 & 0.860 & 0.845 & 0.851 & 0.798 & 0.851 & \underline{0.987} & 0.787 \\
23	Mi-7B    & 0.834 & 0.837 & 0.837 & 0.845 & 0.817 & 0.849 & 0.851 & \underline{0.969} \\
24	\bottomrule
25	\end{tabular}}
26	\end{table}
27	
28	All 56 off-diagonal transfer pairs yield F1 above chance, with a mean of 0.810 (95\% bootstrap CI [0.796, 0.822]; one-sample $t=46.58$, $p < 10^{-10}$).
29	Transfer is strongest within families (e.g., Py-2.8B$\to$Py-1B: 0.87) and weakest for Py-1B$\to$Mi-7B (0.62), consistent with the scale and reference-affinity effects discussed in \S\ref{sec:results-differential}.
30	These results confirm that depth signatures generalize across architectures, parameter scales, and model families, providing evidence against generator identity as a primary confound.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "385dd910-4bd7-4fcb-8f74-3d6db0341c52",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "4badfe7b-0683-4e5b-bb9a-2db845132a10",
  "sourceToolAssistantUUID": "385dd910-4bd7-4fcb-8f74-3d6db0341c52",
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

_source line 34 · 2026-05-23T10:22:57.416Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SB9mbtyEgx8G51P3Q24B1A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_iterative_comparison.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4badfe7b-0683-4e5b-bb9a-2db845132a10",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRBnao6x7uSrPU5pQu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "81d5ac41-55a8-4183-9fb2-895009abd6ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011k8GzFMPjcTaUwx55RLyGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26293,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26293,
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

_source line 35 · 2026-05-23T10:22:57.424Z_

<details><summary>↩ Tool result · `toolu_01SB9mbtyEgx8G51P3Q24B1A`</summary>

```text
1	Table~\ref{tab:iterative-comparison} compares this work with two concurrent studies on iterative LLM generation.
2	All three examine how repeated inference transforms text, but differ in chain operator, analytic lens, and downstream goal.
3	Our continuation-chain setting permits richer depth signal and enables the location/shape decomposition that defines DDR.
4	
5	\begin{table*}[!b]
6	\centering
7	\small
8	\caption{Comparison with concurrent iterative-generation studies. All three examine how repeated LLM inference transforms text, but differ in chain operator, analytic lens, and downstream goal.}
9	\label{tab:iterative-comparison}
10	\resizebox{\textwidth}{!}{%
11	\begin{tabular}{@{}l p{2.2cm} p{2.4cm} p{2.4cm} p{2.0cm} c p{3.4cm}@{}}
12	\toprule
13	\textbf{Study} & \textbf{Chain Type} & \textbf{Feature Space} & \textbf{Analysis Goal} & \textbf{Generator Scale} & \textbf{Steps} & \textbf{Core Insight} \\
14	\midrule
15	\citet{broken_telephone}
16	  & Back-translation (6 bridge langs); rephrasing (ablation)
17	  & Surface overlap (BLEU, ROUGE, METEOR, ChrF, BERTScore) + atomic factuality (FActScore)
18	  & Factuality degradation rate across iterations
19	  & 7--9B (3 open models)
20	  & 100
21	  & Factual accuracy decays progressively; rate governed by source--bridge linguistic distance \\
22	\addlinespace
23	\citet{markovian_chains}
24	  & Rephrasing + round-trip translation
25	  & String recurrence time, distinct-output count, similarity plateau (METEOR), KL contraction
26	  & Convergence \& diversity dynamics of inference-time Markov chains
27	  & 7--8B (3 open + GPT-4o-mini)
28	  & 50
29	  & Greedy decoding collapses to 1--4 recurrent outputs; sampling sustains 10--20\,+ realizations \\
30	\addlinespace
31	\textbf{Ours}
32	  & Open-ended continuation (no meaning-preserving constraint)
33	  & Token-level NLL statistics (location, scale, shape) + lexical diversity
34	  & Depth classification + DDR decomposition into generator \& depth effects
35	  & 0.6--8B (8 models)
36	  & 5
37	  & NLL location drifts monotonically with depth while shape remains invariant---enabling per-generator depth profiling \\
38	\bottomrule
39	\end{tabular}}
40	\end{table*}
41	
42	\paragraph{Finding-level connections.}
43	\citet{broken_telephone}'s factuality degradation under back-translation chains parallels DDR's location drift: both document monotonic loss of input-specific information with iteration depth, though the former measures semantic content loss while DDR captures distributional compression in the NLL feature space.
44	Their finding that degradation rate scales with source--bridge linguistic distance mirrors our observation that elaboration prompts attenuate DDR (Appendix~\ref{app:prompt-type}): tighter semantic constraints slow both factuality decay and distributional drift.
45	
46	\citet{markovian_chains}'s convergence dynamics under greedy decoding---collapse to 1--4 recurrent outputs within 50 steps---aligns with our greedy-decoding experiment where the DDR partition persists: shape features remain near-stationary (mean $|d|{=}0.05$) while location drift is maintained (mean $d{=}0.94$; Appendix~\ref{app:decoding-strategy}), confirming that DDR is an empirical regularity of autoregressive generation independent of sampling stochasticity.
47	Their KL contraction analysis complements DDR: where they quantify \emph{how fast} the output distribution contracts, DDR decomposes \emph{what} contracts (location) from what is preserved (shape).
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81d5ac41-55a8-4183-9fb2-895009abd6ed",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "01a74311-87e6-4812-af43-82e4c365160f",
  "sourceToolAssistantUUID": "81d5ac41-55a8-4183-9fb2-895009abd6ed",
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

_source line 36 · 2026-05-23T10:22:57.644Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CrjwibDyJjmUtEBhLv7jEQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_variance_decomposition.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01a74311-87e6-4812-af43-82e4c365160f",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRBnao6x7uSrPU5pQu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e383d85e-2c34-4f49-b8ef-0abb44022e2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011k8GzFMPjcTaUwx55RLyGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26293,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26293,
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

_source line 37 · 2026-05-23T10:22:57.650Z_

<details><summary>↩ Tool result · `toolu_01CrjwibDyJjmUtEBhLv7jEQ`</summary>

```text
1	\subsection{Variance Decomposition}
2	\label{app:variance-decomposition}
3	
4	To quantify the mechanistic structure underlying DDR, we decompose each feature's variance into depth, generator, interaction, and residual components via two-way ANOVA (Type~II; Table~\ref{tab:anova_decomposition}).
5	
6	\begin{table}[H]
7	\centering
8	\caption{Two-way ANOVA variance decomposition (classical $\eta^2$; proportions of total SS) for depth $\times$ generator ($N$\,=\,37{,}058). Location features show dominant depth effects ($\eta^2_{\text{depth}} {=} 0.34$--$0.37$); shape features are depth-invariant ($\eta^2_{\text{depth}} < 0.01$). All effects $p < 10^{-6}$.}
9	\label{tab:anova_decomposition}
10	\small
11	\begin{tabular}{@{}l cccc@{}}
12	\toprule
13	Feature & $\eta^2_{\text{depth}}$ & $\eta^2_{\text{gen}}$ & $\eta^2_{\text{int}}$ & $\eta^2_{\text{resid}}$ \\
14	\midrule
15	\multicolumn{5}{@{}l}{\textit{Location (drifting)}} \\
16	\quad Ent.\ Mean & \textbf{0.341} & 0.022 & 0.010 & 0.627 \\
17	\quad TTR & \textbf{0.370} & 0.024 & 0.007 & 0.599 \\
18	\quad Hapax Ratio & \textbf{0.364} & 0.017 & 0.006 & 0.612 \\
19	\addlinespace
20	\multicolumn{5}{@{}l}{\textit{Shape (near-stationary)}} \\
21	\quad Ent.\ Max & 0.007 & 0.002 & 0.003 & 0.988 \\
22	\quad Ent.\ Min & 0.002 & 0.001 & 0.001 & 0.996 \\
23	\quad Tail Decay & 0.002 & 0.023 & 0.009 & 0.967 \\
24	\addlinespace
25	\multicolumn{5}{@{}l}{\textit{Intermediate}} \\
26	\quad Ent.\ Std & 0.054 & 0.020 & 0.011 & 0.915 \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
31	The depth factor explains 34--37\% of location-feature variance but $<$1\% of shape-feature variance---a ${>}48\times$ ratio that quantifies the DDR partition as a systematic depth$\times$feature-type interaction rather than a post-hoc grouping.
32	Generator identity contributes comparably across both groups ($\eta^2_{\text{gen}} {=} 0.02$), confirming that the asymmetry is specific to depth, not generator.
33	Interaction terms are uniformly small ($\eta^2_{\text{int}} < 0.011$), indicating that the depth effect on location features operates consistently across generators.
34	
35	Exponential convergence fitting ($f(d) {=} a \cdot e^{-\lambda d} + c$) on per-generator depth trajectories corroborates this: location features converge with moderate rates ($\lambda {=} 0.40 \pm 0.26$, $R^2 {=} 0.99$), consistent with contraction toward a generator-specific fixed point under iterated autoregressive generation, while shape features show degenerate fits ($\lambda {=} 5.3 \pm 8.4$, $R^2 {=} 0.73$) reflecting their flat trajectories.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e383d85e-2c34-4f49-b8ef-0abb44022e2a",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "6128b6a5-55e5-426c-8a66-da9b0a196f90",
  "sourceToolAssistantUUID": "e383d85e-2c34-4f49-b8ef-0abb44022e2a",
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

_source line 38 · 2026-05-23T10:22:57.908Z_

<details open><summary>🔧 Tool call — Read · `toolu_013Ms4q6Sa4575AUSbYjg6pW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_convergence.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6128b6a5-55e5-426c-8a66-da9b0a196f90",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRBnao6x7uSrPU5pQu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f8476efb-39b0-4282-8916-1ad3b0803de6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011k8GzFMPjcTaUwx55RLyGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26293,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26293,
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

_source line 39 · 2026-05-23T10:22:57.912Z_

<details><summary>↩ Tool result · `toolu_013Ms4q6Sa4575AUSbYjg6pW`</summary>

```text
1	Figure~\ref{fig:convergence} (main text) visualizes per-feature convergence trajectories across generation depths 0--4, averaged over 8 generators; each feature is expressed as Cohen's $d$ relative to depth~0.
2	Drifting features (hapax ratio, TTR, entropy mean) and the intermediate feature (entropy std) diverge monotonically; lexical diversity features (TTR, hapax ratio) form a fast-convergence group ($|d| > 2$ by depth~2), while entropy mean and entropy std drift more slowly.
3	Near-stationary features (entropy max, tail decay, entropy min) remain within $|d| < 0.25$ across all depths, confirming location stability.
4	Shaded bands indicate $\pm 1$ standard deviation across generators.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8476efb-39b0-4282-8916-1ad3b0803de6",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "722f0e71-73dc-407c-b26e-93417caf9827",
  "sourceToolAssistantUUID": "f8476efb-39b0-4282-8916-1ad3b0803de6",
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

_source line 40 · 2026-05-23T10:22:58.083Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UwZ9R7kYo6gbNin5zB5sLu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "722f0e71-73dc-407c-b26e-93417caf9827",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRBnao6x7uSrPU5pQu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d02f90e2-d9fe-4d69-ba54-04a4fb3de8ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011k8GzFMPjcTaUwx55RLyGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26293,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26293,
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

_source line 41 · 2026-05-23T10:22:58.088Z_

<details><summary>↩ Tool result · `toolu_01UwZ9R7kYo6gbNin5zB5sLu`</summary>

```text
1	\subsection*{DDR Trend Lines}
2	
3	Figure~\ref{fig:ddr-trends} extends the main-text DDR trajectory plot (Figure~\ref{fig:ddr-trajectory}) by showing per-feature depth trends with individual generator traces overlaid.
4	$R^2$ values are computed from ordinary least-squares regression on depth-level means (five points per generator, one per depth 0--4), not per-sample regression; the annotated Spearman $\rho$ provides the complementary per-sample monotonicity measure.
5	
6	\begin{figure}[H]
7	\centering
8	\includegraphics[width=\columnwidth]{fig_appendix_ddr_trends.pdf}
9	\caption{Per-feature depth trends. Bold line: pooled mean ($\pm$1.96\,SE shading) across all generators, colored by DDR zone (blue: drifting, wine: intermediate, amber: near-stationary). Thin traces: individual generators. Spearman $\rho$ and linear $R^2$ are annotated per panel.}
10	\label{fig:ddr-trends}
11	\end{figure}
12	
13	\subsection*{UMAP Embedding}
14	
15	Figure~\ref{fig:umap} shows a 2D UMAP projection of the 7-feature space (7{,}500 stratified samples, StandardScaler normalization, $k$\,=\,30 neighbors, min\_dist\,=\,0.3).
16	Panel~(a) reveals a depth gradient from gen-0 through gen-4, with progressive overlap at deeper generations consistent with the convergence that motivates the gen-2+ class collapse.
17	Panel~(b) shows the 3-class view: gen-0 forms a separable cluster, while gen-1 and gen-2+ overlap substantially, explaining the classification difficulty at this boundary.
18	
19	\begin{figure}[H]
20	\centering
21	\includegraphics[width=\columnwidth, trim=0 0 356pt 0, clip]{fig_appendix_umap.pdf}\\[-2pt]
22	{\small (a) Colored by raw generation depth (0--4)}\\[6pt]
23	\includegraphics[width=\columnwidth, trim=356pt 0 0 0, clip]{fig_appendix_umap.pdf}\\[-2pt]
24	{\small (b) Colored by 3-class label}
25	\caption{UMAP 2D projection of the 7-feature space ($N$\,=\,7{,}500 stratified sample). (a) A gradient structure emerges, with deeper depths converging. (b) Gen-0 separates clearly; gen-1 and gen-2+ overlap, consistent with the high false-negative rate at the gen-1/gen-2+ boundary.}
26	\label{fig:umap}
27	\end{figure}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d02f90e2-d9fe-4d69-ba54-04a4fb3de8ee",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "8811abd6-2bce-4160-a299-ced64a032916",
  "sourceToolAssistantUUID": "d02f90e2-d9fe-4d69-ba54-04a4fb3de8ee",
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

_source line 42 · 2026-05-23T10:22:58.259Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KEiocAzbxe1etCYbaLaEsw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_correlation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8811abd6-2bce-4160-a299-ced64a032916",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRBnao6x7uSrPU5pQu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b2e078bc-9926-4cc5-8e40-e7617b09ae56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011k8GzFMPjcTaUwx55RLyGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26293,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26293,
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

_source line 43 · 2026-05-23T10:22:58.263Z_

<details><summary>↩ Tool result · `toolu_01KEiocAzbxe1etCYbaLaEsw`</summary>

```text
1	\section{Feature Correlation Matrix}
2	\label{sec:appendix-feature-correlation}
3	
4	This appendix documents inter-feature correlations and the PCA analysis referenced in \S\ref{sec:results-differential}.
5	
6	\begin{table}[t]
7	\centering
8	\caption{Pearson correlation matrix of the seven depth features ($N=27{,}529$).}
9	\label{tab:feature-corr}
10	\resizebox{\columnwidth}{!}{%
11	\begin{tabular}{lrrrrrrr}
12	\toprule
13	 & $\bar{H}$ & $\sigma_H$ & $H_{\min}$ & $H_{\max}$ & $\tau$ & TTR & Hapax \\
14	\midrule
15	$\bar{H}$ & \textemdash & 0.49 & 0.31 & 0.01 & 0.07 & \textbf{0.86} & \textbf{0.81} \\
16	$\sigma_H$ & 0.49 & \textemdash & $-$0.15 & 0.16 & 0.26 & 0.43 & 0.34 \\
17	$H_{\min}$ & 0.31 & $-$0.15 & \textemdash & $-$0.04 & 0.01 & 0.20 & 0.23 \\
18	$H_{\max}$ & 0.01 & 0.16 & $-$0.04 & \textemdash & $-$0.08 & $-$0.13 & $-$0.15 \\
19	$\tau$ & 0.07 & 0.26 & 0.01 & $-$0.08 & \textemdash & 0.13 & 0.14 \\
20	TTR & \textbf{0.86} & 0.43 & 0.20 & $-$0.13 & 0.13 & \textemdash & \textbf{0.97} \\
21	Hapax & \textbf{0.81} & 0.34 & 0.23 & $-$0.15 & 0.14 & \textbf{0.97} & \textemdash \\
22	\bottomrule
23	\end{tabular}}
24	\end{table}
25	
26	TTR and hapax ratio are near-perfectly correlated ($r=0.97$), and both correlate strongly with mean entropy ($r=0.86$ and $0.81$).
27	These three drifting features form a tightly coupled cluster: PCA on the standardized drifting-feature subset shows that a single principal component explains 92.3\% of their joint variance, with near-uniform loadings (0.56--0.59). These three features thus share a single latent dimension.
28	Full 7-feature PCA yields PC1 (44.4\% variance) loading on the drifting triplet (0.53--0.55) and PC2 (18.3\% variance) capturing entropy distributional shape (entropy std vs.\ entropy min contrast).
29	In contrast, $H_{\max}$, $\tau$ (tail decay), and $H_{\min}$ show weak pairwise correlations with all other features ($|r| < 0.27$); these features capture independent aspects of the token-probability distribution.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2e078bc-9926-4cc5-8e40-e7617b09ae56",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "d8274ee9-b21b-4f5f-a4ed-0e93753deff5",
  "sourceToolAssistantUUID": "b2e078bc-9926-4cc5-8e40-e7617b09ae56",
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

_source line 44 · 2026-05-23T10:22:58.674Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KUwcYvxXHyau7Fbr9sYfNh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8274ee9-b21b-4f5f-a4ed-0e93753deff5",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRBnao6x7uSrPU5pQu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "52125955-6079-4b63-bd96-288e20d1485b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011k8GzFMPjcTaUwx55RLyGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26293,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26293,
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

_source line 45 · 2026-05-23T10:22:58.678Z_

<details><summary>↩ Tool result · `toolu_01KUwcYvxXHyau7Fbr9sYfNh`</summary>

```text
1	To verify that the seven retained features are not an arbitrary subset, we screened six additional NLL-distributional statistics as candidate features: median, 90th percentile (p90), interquartile range (IQR), coefficient of variation (CV), skewness, and kurtosis.
2	Table~\ref{tab:candidate-features} reports their DDR coordinates, classification impact, and correlation with retained features.
3	
4	\begin{table}[ht]
5	\centering
6	\small
7	\caption{Candidate feature screening. All six candidates fall in the drifting DDR zone and correlate strongly ($|r| > 0.65$) with existing features. Adding any combination to the baseline degrades or leaves unchanged LOGO 3-class F1; LOFO $\Delta > 0$ indicates that removing the candidate \emph{improves} classification.}
8	\label{tab:candidate-features}
9	\resizebox{\linewidth}{!}{%
10	\begin{tabular}{lccccl}
11	\toprule
12	\textbf{Candidate} & $|\rho|$ & $d$ & \textbf{LOFO} $\Delta$\textbf{F1} & $|r|_{\max}$ & \textbf{Most correlated} \\
13	\midrule
14	median    & 0.685 & 0.794 & $+$0.008 & 0.960 & entropy\_mean \\
15	p90       & 0.693 & 0.960 & $+$0.000 & 0.937 & entropy\_mean \\
16	IQR       & 0.708 & 1.079 & $+$0.007 & 0.908 & entropy\_std \\
17	CV        & 0.633 & 0.980 & $-$0.000 & 0.761 & entropy\_mean \\
18	skewness  & 0.651 & 0.940 & $+$0.010 & 0.780 & entropy\_mean \\
19	kurtosis  & 0.635 & 0.769 & $-$0.003 & 0.650 & entropy\_mean \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	All six candidates occupy the drifting zone ($|\rho| > 0.63$, $d > 0.77$), overlapping with entropy mean, TTR, and hapax ratio; none introduces a new axis of depth-dependent variation.
25	Three candidates---median ($r{=}0.96$), p90 ($r{=}0.94$), and IQR ($r{=}0.91$)---are near-perfect linear proxies of existing features.
26	Adding all six to the 6-feature baseline\footnote{Tail decay requires full-vocabulary logits unavailable in the token-NLL subset used for this analysis; we report 6-feature baselines for fair comparison.} reduces 3-class LOGO F1 from 0.733 to 0.722, consistent with overfitting from redundant inputs.
27	LOFO analysis on the extended 12-feature set confirms that removing skewness ($+$0.010), median ($+$0.008), or IQR ($+$0.007) \emph{improves} classification, indicating these features inject noise rather than signal.
28	The retained seven features span three complementary DDR zones (drifting, intermediate, near-stationary) and two modalities (reference-model NLL, surface lexical diversity); additional distributional statistics provide no incremental information.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52125955-6079-4b63-bd96-288e20d1485b",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "180d21b6-426e-452a-b77c-52483703ae48",
  "sourceToolAssistantUUID": "52125955-6079-4b63-bd96-288e20d1485b",
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

_source line 46 · 2026-05-23T10:22:58.885Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RP1UtUdzD61GBC54iDGCYA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_nll_distribution.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "180d21b6-426e-452a-b77c-52483703ae48",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRBnao6x7uSrPU5pQu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eb17d387-7fc0-43b5-a459-8817a4a33724",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011k8GzFMPjcTaUwx55RLyGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26293,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26293,
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

_source line 47 · 2026-05-23T10:22:58.888Z_

<details><summary>↩ Tool result · `toolu_01RP1UtUdzD61GBC54iDGCYA`</summary>

```text
1	% section header and label in main.tex
2	
3	\begin{figure}[H]
4	\centering
5	\includegraphics[width=\columnwidth]{fig_appendix_nll_distribution.pdf}
6	\caption{Token-level NLL distribution by generation depth, aggregated across all 8 generators (Pythia-410M reference model). Dashed lines indicate median NLL per depth. The systematic leftward shift demonstrates that deeper-generation text is increasingly predictable.}
7	\label{fig:nll-dist}
8	\end{figure}
9	
10	Figure~\ref{fig:nll-dist} plots the kernel density of per-token NLL across depths~0--4 (8 generators, 25 texts/depth, ${\sim}$236k tokens, Pythia-410M reference).
11	The distributions shift leftward as depth increases: median NLL drops from 1.64~nats (gen-0) to 0.02 (gen-4), confirming that recursively generated text becomes increasingly predictable.
12	This monotonic compression provides a mechanistic explanation for the entropy-based features driving the depth classifier.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb17d387-7fc0-43b5-a459-8817a4a33724",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "7395d115-acfb-4efe-b4b6-72da71037da1",
  "sourceToolAssistantUUID": "eb17d387-7fc0-43b5-a459-8817a4a33724",
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

_source line 48 · 2026-05-23T10:22:59.142Z_

<details open><summary>🔧 Tool call — Read · `toolu_017tvpGUqSjTX5R7rHsYiqNs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qualitative_examples.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7395d115-acfb-4efe-b4b6-72da71037da1",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRBnao6x7uSrPU5pQu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b8e72f47-2622-46aa-b85f-37bad264d269",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011k8GzFMPjcTaUwx55RLyGe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 26293,
      "cache_read_input_tokens": 17476,
      "output_tokens": 865,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 26293
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 865,
          "cache_read_input_tokens": 17476,
          "cache_creation_input_tokens": 26293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 26293,
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

_source line 49 · 2026-05-23T10:22:59.145Z_

<details><summary>↩ Tool result · `toolu_017tvpGUqSjTX5R7rHsYiqNs`</summary>

```text
1	\section{Qualitative Examples}
2	\label{app:qualitative}
3	
4	Table~\ref{tab:qualitative-text} presents an example generation chain from seed 120 (Pythia-2.8B, continuation prompt), illustrating how text evolves across recursive generation steps.
5	Table~\ref{tab:qualitative-features} reports the corresponding 7-feature values. Central-tendency features ($\bar{H}$, TTR, hapax ratio) drift monotonically while shape features ($H_{\max}$, tail decay) remain near-stationary, consistent with the differential depth response pattern.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Example text chain from seed 120 (Pythia-2.8B, continuation prompt). Gen-0 is the original Wikipedia passage; gen-1 and gen-2 are successive LLM continuations. Text is truncated for space.}
10	\label{tab:qualitative-text}
11	\small
12	\begin{tabular}{p{0.90\columnwidth}}
13	\toprule
14	\textbf{Gen-0 (Wikipedia seed)} \\
15	\midrule
16	Aquarius is an equatorial constellation of the zodiac, between Capricornus and Pisces. Its name is Latin for ``water-carrier'' or ``cup-carrier''. Aquarius is one of the oldest of the recognized constellations along the zodiac (the Sun's apparent path). It was one of the 48 constellations listed by the 2nd century astronomer Ptolemy, and it remains one of the 88 modern constellations. It is found in a region often called the Sea due to its profusion of constellations with watery associations such as Cetus the whale, Pisces the fish, and Eridanus the river. [\ldots] \\
17	\midrule
18	\textbf{Gen-1} \\
19	\midrule
20	Babylonian astrology and was also depicted in ancient Egyptian art. In Greek mythology, Aquarius is the son of Poseidon and Gaia. He is also the god of the sea and the sky, the god of travelers, and the guardian of the underworld. In Roman mythology, Aquarius is the son of Saturn and the nymph Egeria, and the god of the sea. In Jewish mythology, Aquarius is the son of the God of the Air and the Goddess of the Moon. In Chinese mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. [\ldots] \\
21	\midrule
22	\textbf{Gen-2} \\
23	\midrule
24	God of the Sky and the Goddess of the Earth. In the ancient Greek mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. In the Hindu mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. In the ancient Egyptian mythology, Aquarius is the son of the God of the Sky and the Goddess of the Earth. [\ldots] \\
25	\bottomrule
26	\end{tabular}
27	\end{table}
28	
29	\begin{table}[t]
30	\centering
31	\caption{Feature values for the chain in Table~\ref{tab:qualitative-text}. Drifting features ($\bar{H}$, TTR, hapax) show monotonic degradation; shape features ($H_{\max}$, tail decay) remain stable (range $<$2\% and $<$4\% respectively).}
32	\label{tab:qualitative-features}
33	\small
34	\resizebox{\linewidth}{!}{%
35	\begin{tabular}{lrrr}
36	\toprule
37	Feature & Gen-0 & Gen-1 & Gen-2 \\
38	\midrule
39	$\bar{H}$ (entropy mean) & 2.720 & 2.206 & 0.780 \\
40	$\sigma_H$ (entropy std) & 1.772 & 1.816 & 1.517 \\
41	$H_{\min}$ (entropy min) & 0.002 & 0.005 & 0.000 \\
42	$H_{\max}$ (entropy max) & 7.000 & 7.016 & 6.926 \\
43	tail decay & $-$0.00227 & $-$0.00231 & $-$0.00223 \\
44	TTR & 0.659 & 0.272 & 0.081 \\
45	hapax ratio & 0.561 & 0.183 & 0.005 \\
46	\bottomrule
47	\end{tabular}}
48	\end{table}
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8e72f47-2622-46aa-b85f-37bad264d269",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a4ee533cda4eea682",
  "type": "user",
  "uuid": "ce8979d7-ba65-4283-b988-95f3d6d51af7",
  "sourceToolAssistantUUID": "b8e72f47-2622-46aa-b85f-37bad264d269",
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

_source line 50 · 2026-05-23T10:24:16.686Z_

Perfect! I've now read all 23 appendix files. Let me compile a comprehensive extraction of all table data from these files:

## COMPREHENSIVE TABLE DATA EXTRACTION

**appendix_qlora.tex**
- Table (caption: "QLoRA end-to-end depth classification vs. XGBoost on handcrafted features, under LOGO evaluation")
  - XGBoost (7 features): 5-class F1 = 0.501 ± 0.038, 3-class F1 = 0.789
  - QLoRA (Qwen3-0.6B): 5-class F1 = 0.583 ± 0.010, 3-class F1 = 0.905 ± 0.003, Per-class F1 (5-class) = 0.999, 0.796, 0.413, 0.259, 0.447
  - Text values: LoRA rank 16, learning rate 2×10^-4, 3 epochs; hyperparameter robustness: LoRA rank 32 seed 123 yields 5-class F1 = 0.587 ± 0.005, 3-class F1 = 0.905 ± 0.004

**appendix_instruct.tex**
- Table (caption: "Depth classification: base vs. instruction-tuned models")
  - OLMo-2-1B: 3-class F1 Base = 0.754, Instruct = 0.575; Binary F1 Base = 0.845, Instruct = 0.813; ρ(ent. mean) Base = -0.64, Instruct = +0.48; Rev. = 6/7
  - Qwen3-1.7B: 3-class F1 Base = 0.769, Instruct = 0.732; Binary F1 Base = 0.861, Instruct = 0.875; ρ Base = -0.60, Instruct = +0.48; Rev. = 6/7
  - Llama-3.2-3B: 3-class F1 Base = 0.742, Instruct = 0.544; Binary F1 Base = 0.849, Instruct = 0.838; ρ Base = -0.63, Instruct = +0.23; Rev. = 3/7
  
- Table (caption: "Classification recovery under instruction-tuned retraining")
  - OLMo-2-1B-Inst: Base→Inst = 0.321, Retrained = 0.590, Δ = +0.269
  - Qwen3-1.7B-Inst: Base→Inst = 0.500, Retrained = 0.660, Δ = +0.160
  - Qwen3-0.6B-Inst: Base→Inst = 0.532, Retrained = 0.600, Δ = +0.068
  - Text values: 3-class instruct LOGO binary F1 = 0.487; silhouette 0.372 vs 0.660 for base models; OLMo-Instruct TTR and hapax ρ = 0.006, 0.025; Qwen instruct ρ = 0.48-0.53; base→instruct binary F1 = 0.490, instruct→base = 0.454

- Table (caption: "End-to-end QLoRA vs. XGBoost on instruction-tuned data")
  - OLMo-2-1B-Inst: XGB = 0.575, QLoRA = 0.888±0.007, Δ = +31.3pp, N = 4,429
  - Qwen3-1.7B-Inst: XGB = 0.732, QLoRA = 0.907±0.008, Δ = +17.5pp, N = 4,963
  - OLMo-2-1B (base): QLoRA = 0.859±0.004, N = 2,379
  - Qwen3-1.7B (base): QLoRA = 0.904±0.009, N = 2,291

**appendix_temperature_stability.tex**
- Table (caption: "Mean |d| across 4 generators at each temperature")
  - Entropy mean: τ=0.5: 1.39^D, τ=0.7: 1.10^D, τ=0.9: 0.58^D
  - TTR: τ=0.5: 1.00^D, τ=0.7: 0.85^D, τ=0.9: 0.45^I
  - Hapax ratio: τ=0.5: 0.87^D, τ=0.7: 0.75^D, τ=0.9: 0.42^I
  - Entropy std: τ=0.5: 0.84^D, τ=0.7: 0.52^D, τ=0.9: 0.20^I
  - Entropy max: τ=0.5: 0.06^S, τ=0.7: 0.09^S, τ=0.9: 0.11^I
  - Tail decay: τ=0.5: 0.07^S, τ=0.7: 0.12^I, τ=0.9: 0.15^I
  - Entropy min: τ=0.5: 0.04^S, τ=0.7: 0.06^S, τ=0.9: 0.04^S
  - Text values: mean |d| drifting set: τ=0.5: 1.09, τ=0.7: 0.90, τ=0.9: 0.48

**appendix_decoding_strategy.tex**
- Table (caption: "Shape-feature Cohen's d under three decoding strategies")
  - Pythia-2.8B: entropy_max Nuc=0.25, Gr=0.09, Top-k=0.26; entropy_min Nuc=0.03, Gr=0.08, Top-k=0.04; tail_decay Nuc=0.07, Gr=0.07, Top-k=0.12
  - Pythia-1B: entropy_max Nuc=0.21, Gr=0.12, Top-k=0.27; entropy_min Nuc=0.02, Gr=0.04, Top-k=0.04; tail_decay Nuc=0.08, Gr=0.04, Top-k=0.18
  - OLMo-2-1B: entropy_max Nuc=0.06, Gr=0.03, Top-k=0.01; entropy_min Nuc=0.07, Gr=0.03, Top-k=0.01; tail_decay Nuc=0.22, Gr=0.03, Top-k=0.22
  - Qwen3-0.6B: entropy_max Nuc=0.01, Gr=0.09, Top-k=0.02; entropy_min Nuc=0.10, Gr=0.02, Top-k=0.10; tail_decay Nuc=0.08, Gr=0.03, Top-k=0.13
  - Qwen3-1.7B: entropy_max Nuc=0.02, Gr=0.08, Top-k=0.03; entropy_min Nuc=0.05, Gr=0.01, Top-k=0.03; tail_decay Nuc=0.09, Gr=0.04, Top-k=0.14
  - Qwen3-8B: entropy_max Nuc=0.04, Gr=0.01, Top-k=0.05; entropy_min Nuc=0.01, Gr=0.06, Top-k=0.07; tail_decay Nuc=0.15, Gr=0.08, Top-k=0.17
  - Llama-3.2-3B: entropy_max Nuc=0.01, Gr=0.06, Top-k=0.08; entropy_min Nuc=0.01, Gr=0.07, Top-k=0.03; tail_decay Nuc=0.19, Gr=0.04, Top-k=0.20
  - Mistral-7B-v0.3: entropy_max Nuc=0.00, Gr=0.01, Top-k=0.06; entropy_min Nuc=0.04, Gr=0.02, Top-k=0.01; tail_decay Nuc=0.16, Gr=0.14, Top-k=0.12
  - Mean: entropy_max Nuc=0.08^8/8, Gr=0.06^8/8, Top-k=0.10^8/8; entropy_min Nuc=0.04^8/8, Gr=0.04^8/8, Top-k=0.04^8/8; tail_decay Nuc=0.13^8/8, Gr=0.06^8/8, Top-k=0.16^8/8

- Table (caption: "Drifting- and intermediate-feature Cohen's d under three decoding strategies")
  - Pythia-2.8B: entropy_mean Nuc=1.20, Gr=1.43, Top-k=0.70; TTR Nuc=0.77, Gr=0.98, Top-k=0.41; hapax_ratio Nuc=0.67, Gr=0.87, Top-k=0.37; entropy_std Nuc=0.39, Gr=0.93, Top-k=0.10
  - Pythia-1B: entropy_mean Nuc=1.40, Gr=0.98, Top-k=0.83; TTR Nuc=0.80, Gr=0.64, Top-k=0.41; hapax_ratio Nuc=0.65, Gr=0.53, Top-k=0.34; entropy_std Nuc=0.53, Gr=0.91, Top-k=0.13
  - OLMo-2-1B: entropy_mean Nuc=1.19, Gr=1.29, Top-k=0.73; TTR Nuc=1.08, Gr=0.89, Top-k=0.70; hapax_ratio Nuc=1.00, Gr=0.80, Top-k=0.69; entropy_std Nuc=0.61, Gr=0.95, Top-k=0.35
  - Qwen3-0.6B: entropy_mean Nuc=0.92, Gr=0.82, Top-k=0.80; TTR Nuc=0.63, Gr=0.51, Top-k=0.58; hapax_ratio Nuc=0.50, Gr=0.46, Top-k=0.52; entropy_std Nuc=0.56, Gr=0.72, Top-k=0.30
  - Qwen3-1.7B: entropy_mean Nuc=1.12, Gr=1.03, Top-k=0.99; TTR Nuc=0.93, Gr=0.74, Top-k=0.85; hapax_ratio Nuc=0.83, Gr=0.68, Top-k=0.80; entropy_std Nuc=0.52, Gr=0.78, Top-k=0.32
  - Qwen3-8B: entropy_mean Nuc=0.86, Gr=0.98, Top-k=0.76; TTR Nuc=0.71, Gr=0.76, Top-k=0.68; hapax_ratio Nuc=0.66, Gr=0.76, Top-k=0.64; entropy_std Nuc=0.37, Gr=0.71, Top-k=0.27
  - Llama-3.2-3B: entropy_mean Nuc=1.15, Gr=1.46, Top-k=0.77; TTR Nuc=1.04, Gr=1.27, Top-k=0.73; hapax_ratio Nuc=0.98, Gr=1.26, Top-k=0.71; entropy_std Nuc=0.50, Gr=1.01, Top-k=0.21
  - Mistral-7B-v0.3: entropy_mean Nuc=0.89, Gr=1.31, Top-k=0.70; TTR Nuc=0.82, Gr=1.04, Top-k=0.64; hapax_ratio Nuc=0.82, Gr=1.03, Top-k=0.67; entropy_std Nuc=0.23, Gr=0.62, Top-k=0.15
  - Mean: entropy_mean Nuc=1.09^8/8, Gr=1.16^8/8, Top-k=0.79^8/8; TTR Nuc=0.85^8/8, Gr=0.85^8/8, Top-k=0.63^8/8; hapax_ratio Nuc=0.76^8/8, Gr=0.80^8/8, Top-k=0.59^8/8; entropy_std Nuc=0.46^8/8, Gr=0.83^8/8, Top-k=0.23^8/8
  - Text values: greedy decoding mean |d| = 0.05, max = 0.14, drifting mean d = 0.94; top-k core drifting mean d = 0.67

**appendix_cross_model_detail.tex**
- Table (caption: "Cross-model chain per-class performance")
  - gen-0: Precision = 0.921, Recall = 0.948, F1 = 0.935, 95% CI [.923, .946]
  - gen-1: Precision = 0.737, Recall = 0.803, F1 = 0.768, 95% CI [.748, .788]
  - gen-2+: Precision = 0.842, Recall = 0.742, F1 = 0.789, 95% CI [.768, .809]
  - Macro: F1 = 0.831, 95% CI [.817, .844]; Macro F1 balanced = 0.831; Macro F1 unbalanced = 0.789; Binary F1 = 0.830, 95% CI [.818, .841]
  - Text values: N = 2,964, n_generators = 5; partial η²_gen < 1% (range 0.05%-0.90%, mean 0.37%); depth 15.3%-29.9%; generator×depth < 1%

**appendix_cross_temp.tex**
- Text values only:
  - 3-class F1: matched t=0.7→0.7: 0.789, matched t=1.0→1.0: 0.726
  - Cross-temperature: t=1.0→0.7: 0.791, t=0.7→1.0: 0.723
  - Qwen3-1.7B under mismatch: 0.418
  - Qwen3-1.7B binary: 0.7→1.0: 0.713, 1.0→0.7: 0.948; aggregate binary range: 0.900-0.958

**appendix_domain.tex**
- Table (caption: "Cross-domain depth classification under LOGO evaluation")
  - Code: Binary F1 = 0.754, 95% CI [0.737, 0.770], 3-class F1 = 0.634
  - News: Binary F1 = 0.746, 95% CI [0.726, 0.764], 3-class F1 = 0.652
  - Academic: Binary F1 = 0.739, 95% CI [0.720, 0.757], 3-class F1 = 0.622
  - Text values: 200 seeds per domain, 3 generators; News t=0.7: 0.712 vs t=1.0: 0.746; Academic t=0.7: 0.628 vs t=1.0: 0.739; Code t=0.7: 0.687 vs t=1.0: 0.754

**appendix_tost.tex**
- Table (caption: "Per-generator TOST equivalence")
  - Pythia-2.8B: $\bar{H}$ = 1.20, TTR = 0.77, hapax = 0.67, $\sigma_H$ = 0.39, $H_{max}$ = 0.25, tail = 0.07✓, $H_{min}$ = 0.03✓
  - Pythia-1B: $\bar{H}$ = 1.40, TTR = 0.80, hapax = 0.65, $\sigma_H$ = 0.53, $H_{max}$ = 0.21, tail = 0.08✓, $H_{min}$ = 0.02✓
  - Qwen3-1.7B: $\bar{H}$ = 1.12, TTR = 0.93, hapax = 0.83, $\sigma_H$ = 0.52, $H_{max}$ = 0.02✓, tail = 0.09✓, $H_{min}$ = 0.05✓
  - Llama-3.2-3B: $\bar{H}$ = 1.15, TTR = 1.04, hapax = 0.98, $\sigma_H$ = 0.50, $H_{max}$ = 0.01✓, tail = 0.19, $H_{min}$ = 0.01✓
  - OLMo-2-1B: $\bar{H}$ = 1.19, TTR = 1.08, hapax = 1.00, $\sigma_H$ = 0.61, $H_{max}$ = 0.06✓, tail = 0.22, $H_{min}$ = 0.07✓
  - Qwen3-8B: $\bar{H}$ = 0.86, TTR = 0.71, hapax = 0.66, $\sigma_H$ = 0.37, $H_{max}$ = 0.04✓, tail = 0.15, $H_{min}$ = 0.01✓
  - Qwen3-0.6B: $\bar{H}$ = 0.92, TTR = 0.63, hapax = 0.50, $\sigma_H$ = 0.56, $H_{max}$ = 0.01✓, tail = 0.08✓, $H_{min}$ = 0.10✓
  - Mistral-7B: $\bar{H}$ = 0.89, TTR = 0.82, hapax = 0.82, $\sigma_H$ = 0.23, $H_{max}$ = 0.00✓, tail = 0.16, $H_{min}$ = 0.04✓
  - Equiv. count: $\bar{H}$ = 0/8, TTR = 0/8, hapax = 0/8, $\sigma_H$ = 0/8, $H_{max}$ = 6/8, tail = 4/8, $H_{min}$ = 8/8
  - Text values: silhouette drifting/non-drifting partition k=2: 0.660; k=3: 0.532; per-generator silhouette range 0.505-0.760, mean 0.651

**appendix_tost_bootstrap.tex**
- Table (caption: "Bootstrap stability of TOST equivalence")
  - entropy_max: Rejection rate = 100% (1000/1000), Median d = 0.062, d 95% CI [0.037, 0.088]
  - entropy_min: Rejection rate = 100% (1000/1000), Median d = -0.016, d 95% CI [-0.042, 0.011]
  - tail_decay: Rejection rate = 100% (1000/1000), Median d = 0.088, d 95% CI [0.065, 0.111]
  - entropy_std: Rejection rate = 0% (0/1000), Median d = 0.458, d 95% CI [0.435, 0.479]

**appendix_ddr_causality.tex**
- Table (caption: "Permutation importance")
  - hapax_ratio: Group = Drifting, Mean F1 Drop = 0.235, Rank = 1
  - entropy_mean: Group = Drifting, Mean F1 Drop = 0.170, Rank = 2
  - ttr: Group = Drifting, Mean F1 Drop = 0.156, Rank = 3
  - entropy_max: Group = Near-stat., Mean F1 Drop = 0.070, Rank = 4
  - entropy_std: Group = Intermediate, Mean F1 Drop = 0.057, Rank = 5
  - entropy_min: Group = Near-stat., Mean F1 Drop = 0.019, Rank = 6
  - tail_decay: Group = Near-stat., Mean F1 Drop = 0.014, Rank = 7
  - Text values: baseline F1 = 0.771; drifting average F1 drop = 0.187 vs near-stationary = 0.034 (5.5×)

- Table (caption: "Granger causality")
  - entropy_std: Combined p = < 0.001, ΔR² = 0.031, Significant = Yes
  - hapax_ratio: Combined p = < 0.001, ΔR² = ---, Significant = Yes
  - ttr: Combined p = < 0.001, ΔR² = ---, Significant = Yes
  - entropy_mean: Combined p = < 0.001, ΔR² = ---, Significant = Yes
  - entropy_max: Combined p = < 0.001, ΔR² = ---, Significant = Yes
  - tail_decay: Combined p = < 0.001, ΔR² = ---, Significant = Yes
  - entropy_min: Combined p = 0.375, ΔR² = ---, Significant = No
  - Text values: N = 29,095; 6/7 features p < 0.001; entropy_min F1 drop = 0.019

**appendix_ddr_validation.tex**
- Table (caption: "k-means clustering of 7 features")
  - k=2: silhouette = 0.660, clusters: {$\bar{H}$, TTR, hapax} | {$\sigma_H$, $H_{min}$, $H_{max}$, tail}
  - k=3: silhouette = 0.532, clusters: {$\bar{H}$, TTR, hapax} | {$\sigma_H$, $H_{max}$, tail} | {$H_{min}$}
  - k=4: silhouette = 0.527, clusters: {$\bar{H}$, TTR, hapax} | {$H_{max}$, tail} | {$\sigma_H$} | {$H_{min}$}
  - Text values: exhaustive partition enumeration best silhouette = 0.660; 20/35 partitions negative silhouette; per-generator recovery all 8 generators identical partition; silhouette range 0.505-0.760

- Table (caption: "TOST equivalence pass rate across 8 generators")
  - $\bar{H}$ (ent. mean): ε=0.15: 0/8, ε=0.20: 0/8, ε=0.25: 0/8
  - TTR: ε=0.15: 0/8, ε=0.20: 0/8, ε=0.25: 0/8
  - hapax ratio: ε=0.15: 0/8, ε=0.20: 0/8, ε=0.25: 0/8
  - $\sigma_H$ (ent. std): ε=0.15: 0/8, ε=0.20: 0/8, ε=0.25: 0/8
  - $H_{min}$ (ent. min): ε=0.15: 7/8, ε=0.20: 8/8, ε=0.25: 8/8
  - $H_{max}$ (ent. max): ε=0.15: 6/8, ε=0.20: 6/8, ε=0.25: 6/8
  - tail decay: ε=0.15: 4/8, ε=0.20: 4/8, ε=0.25: 7/8

- Table (caption: "Partition stability under varying ε")
  - $\bar{H}$ (ent. mean): Pooled d = 1.17, Stationary at ε > 1.17
  - TTR: Pooled d = 0.88, Stationary at ε > 0.88
  - hapax ratio: Pooled d = 0.76, Stationary at ε > 0.76
  - $\sigma_H$ (ent. std): Pooled d = 0.55, Stationary at ε > 0.55
  - $H_{max}$ (ent. max): Pooled d = 0.08, Stationary at ε > 0.08
  - tail decay: Pooled d = 0.08, Stationary at ε > 0.08
  - $H_{min}$ (ent. min): Pooled d = 0.016, Stationary at ε > 0.016

- Table (caption: "Holdout split validation of the DDR partition")
  - Split A selection |ρ|: $\bar{H}$ = 0.60, TTR = 0.61, hapax = 0.62, $\sigma_H$ = 0.19, $H_{min}$ = 0.39, $H_{max}$ = 0.05, tail = 0.10
  - Split A validation |ρ|: $\bar{H}$ = 0.58, TTR = 0.59, hapax = 0.60, $\sigma_H$ = 0.21, $H_{min}$ = 0.36, $H_{max}$ = 0.05, tail = 0.08
  - Split A Δ|ρ|: $\bar{H}$ = 0.02, TTR = 0.02, hapax = 0.02, $\sigma_H$ = 0.02, $H_{min}$ = 0.03, $H_{max}$ = 0.00, tail = 0.02
  - Split B selection |ρ|: $\bar{H}$ = 0.60, TTR = 0.60, hapax = 0.62, $\sigma_H$ = 0.22, $H_{min}$ = 0.38, $H_{max}$ = 0.04, tail = 0.11
  - Split B validation |ρ|: $\bar{H}$ = 0.58, TTR = 0.59, hapax = 0.61, $\sigma_H$ = 0.17, $H_{min}$ = 0.37, $H_{max}$ = 0.06, tail = 0.07
  - Split B Δ|ρ|: $\bar{H}$ = 0.02, TTR = 0.01, hapax = 0.01, $\sigma_H$ = 0.05, $H_{min}$ = 0.01, $H_{max}$ = 0.02, tail = 0.04

- Table (caption: "Effect size comparison")
  - ent. mean: |d| = 1.054, |Δ| = 1.410, |δ| = 0.587
  - TTR: |d| = 0.814, |Δ| = 1.116, |δ| = 0.510
  - hapax ratio: |d| = 0.735, |Δ| = 0.936, |δ| = 0.528
  - ent. std: |d| = 0.457, |Δ| = 0.605, |δ| = 0.295
  - tail decay: |d| = 0.087, |Δ| = 0.099, |δ| = 0.072
  - ent. max: |d| = 0.062, |Δ| = 0.065, |δ| = 0.021
  - ent. min: |d| = 0.016, |Δ| = 0.015, |δ| = 0.354†
  - Text values: variance ratios drifting 1.86-2.21, gen-2+ variance/gen-1 ratio 2.08

**appendix_9gen_scale.tex**
- Table (caption: "9-generator LOGO evaluation")
  - Pythia-1B: Family = Pythia, Params = 1.0B, 3-class F1 = 0.857, 95% CI [0.848, 0.866], Binary F1 = 0.785
  - Qwen3-0.6B: Family = Qwen, Params = 0.6B, 3-class F1 = 0.819, 95% CI [0.807, 0.830], Binary F1 = 0.743
  - Pythia-2.8B: Family = Pythia, Params = 2.8B, 3-class F1 = 0.812, 95% CI [0.801, 0.822], Binary F1 = 0.728
  - Qwen3-1.7B: Family = Qwen, Params = 1.7B, 3-class F1 = 0.811, 95% CI [0.800, 0.823], Binary F1 = 0.746
  - OLMo-2-1B: Family = OLMo, Params = 1.5B, 3-class F1 = 0.773, 95% CI [0.762, 0.784], Binary F1 = 0.692
  - Llama-3.2-3B: Family = Llama, Params = 3.2B, 3-class F1 = 0.759, 95% CI [0.748, 0.770], Binary F1 = 0.680
  - Qwen3-8B: Family = Qwen, Params = 8.2B, 3-class F1 = 0.696, 95% CI [0.683, 0.709], Binary F1 = 0.647, 95% CI [0.631, 0.664]
  - Gemma-2-2B: Family = Gemma, Params = 2.6B, 3-class F1 = 0.628, 95% CI [0.622, 0.634], Binary F1 = 0.440, 95% CI [0.432, 0.449]
  - Mistral-7B: Family = Mistral, Params = 7.0B, 3-class F1 = 0.605, 95% CI [0.593, 0.617], Binary F1 = 0.534
  - Average (9-gen): 3-class F1 = 0.751, Binary F1 = 0.666
  - Average (8-gen): 3-class F1 = 0.770, Binary F1 = 0.701
  - Text values: Gemma-2-2B gen-0 F1 = 0.991, gen-1 F1 = 0.036, gen-2+ F1 = 0.856; Gemma partition N = 4,957; Qwen3-14B-Base ρ attenuation 21-35%, entropy mean |ρ| = 0.39, d = 0.78

**appendix_generator_subsets.tex**
- Table (caption: "Generator subsets by experiment type")
  - Main LOGO: N = 8, all 8 generators
  - Cross-model chains: N = 5, Py-2.8B/1B, OLMo, Qw-1.7B/0.6B
  - QLoRA: N = 6, Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B
  - Temperature ablation: N = 4, Py-2.8B, OLMo, Qw-1.7B/0.6B
  - Prompt-type: N = 1, Py-2.8B only
  - Cross-domain: N = 3, Py-1B, Qw-1.7B, Mistral
  - Instruct: N = 3, OLMo, Qw-1.7B, Llama
  - Downstream: N = 5, Py-2.8B/1B, OLMo, Qw-1.7B/0.6B

**appendix_prompt_type.tex**
- Text values only:
  - Continuation prompt 5-fold CV macro-F1 = 0.78
  - Rewriting prompt 5-fold CV macro-F1 = 0.74
  - Elaboration prompt 5-fold CV macro-F1 = 0.73
  - Cross-prompt-type transfer (LOPTO) average F1 = 0.753
  - Feature decay rates: continuation = 16.9%/depth, rewriting = 6.1%/depth, elaboration = 1.4%/depth

**appendix_transfer.tex**
- Table (caption: "Cross-generator binary F1 transfer matrix")
  - Py-2.8B train: Py-2.8B=0.985, Py-1B=0.873, Qw-0.6B=0.823, Qw-1.7B=0.833, Qw-8B=0.741, OLMo-1B=0.829, Ll-3B=0.815, Mi-7B=0.712
  - Py-1B train: Py-2.8B=0.834, Py-1B=0.987, Qw-0.6B=0.828, Qw-1.7B=0.821, Qw-8B=0.704, OLMo-1B=0.778, Ll-3B=0.764, Mi-7B=0.620
  - Qw-0.6B train: Py-2.8B=0.786, Py-1B=0.846, Qw-0.6B=0.991, Qw-1.7B=0.851, Qw-8B=0.786, OLMo-1B=0.795, Ll-3B=0.760, Mi-7B=0.680
  - Qw-1.7B train: Py-2.8B=0.794, Py-1B=0.839, Qw-0.6B=0.859, Qw-1.7B=0.989, Qw-8B=0.790, OLMo-1B=0.817, Ll-3B=0.798, Mi-7B=0.717
  - Qw-8B train: Py-2.8B=0.811, Py-1B=0.836, Qw-0.6B=0.853, Qw-1.7B=0.855, Qw-8B=0.984, OLMo-1B=0.848, Ll-3B=0.839, Mi-7B=0.790
  - OLMo-1B train: Py-2.8B=0.811, Py-1B=0.827, Qw-0.6B=0.837, Qw-1.7B=0.852, Qw-8B=0.803, OLMo-1B=0.988, Ll-3B=0.828, Mi-7B=0.763
  - Ll-3B train: Py-2.8B=0.856, Py-1B=0.860, Qw-0.6B=0.845, Qw-1.7B=0.851, Qw-8B=0.798, OLMo-1B=0.851, Ll-3B=0.987, Mi-7B=0.787
  - Mi-7B train: Py-2.8B=0.834, Py-1B=0.837, Qw-0.6B=0.837, Qw-1.7B=0.845, Qw-8B=0.817, OLMo-1B=0.849, Ll-3B=0.851, Mi-7B=0.969
  - Text values: 56 off-diagonal pairs mean F1 = 0.810, 95% CI [0.796, 0.822], t=46.58, p<10^-10; Py-2.8B→Py-1B = 0.87; Py-1B→Mi-7B = 0.62

**appendix_iterative_comparison.tex**
- Table (caption: "Comparison with concurrent iterative-generation studies")
  - Broken Telephone: Chain Type = Back-translation (6 bridge langs); rephrasing; Feature Space = Surface overlap (BLEU, ROUGE, METEOR, ChrF, BERTScore) + atomic factuality (FActScore); Analysis Goal = Factuality degradation rate across iterations; Generator Scale = 7–9B (3 open models); Steps = 100
  - Markovian Chains: Chain Type = Rephrasing + round-trip translation; Feature Space = String recurrence time, distinct-output count, similarity plateau (METEOR), KL contraction; Analysis Goal = Convergence & diversity dynamics of inference-time Markov chains; Generator Scale = 7–8B (3 open + GPT-4o-mini); Steps = 50
  - Ours: Chain Type = Open-ended continuation (no meaning-preserving constraint); Feature Space = Token-level NLL statistics (location, scale, shape) + lexical diversity; Analysis Goal = Depth classification + DDR decomposition into generator & depth effects; Generator Scale = 0.6–8B (8 models); Steps = 5

**appendix_variance_decomposition.tex**
- Table (caption: "Two-way ANOVA variance decomposition")
  - Ent. Mean: η²_depth = 0.341, η²_gen = 0.022, η²_int = 0.010, η²_resid = 0.627
  - TTR: η²_depth = 0.370, η²_gen = 0.024, η²_int = 0.007, η²_resid = 0.599
  - Hapax Ratio: η²_depth = 0.364, η²_gen = 0.017, η²_int = 0.006, η²_resid = 0.612
  - Ent. Max: η²_depth = 0.007, η²_gen = 0.002, η²_int = 0.003, η²_resid = 0.988
  - Ent. Min: η²_depth = 0.002, η²_gen = 0.001, η²_int = 0.001, η²_resid = 0.996
  - Tail Decay: η²_depth = 0.002, η²_gen = 0.023, η²_int = 0.009, η²_resid = 0.967
  - Ent. Std: η²_depth = 0.054, η²_gen = 0.020, η²_int = 0.011, η²_resid = 0.915
  - Text values: N = 37,058; location η²_depth = 0.34-0.37, shape < 0.01, ratio > 48×; exponential convergence λ = 0.40±0.26 (location R²=0.99), λ = 5.3±8.4 (shape R²=0.73)

**appendix_convergence.tex**
- Text values only:
  - Drifting features (hapax ratio, TTR, entropy mean) and entropy std diverge monotonically
  - Lexical diversity features (TTR, hapax ratio) form fast-convergence group |d| > 2 by depth 2
  - Entropy mean and entropy std drift more slowly
  - Near-stationary features (entropy max, tail decay, entropy min) remain within |d| < 0.25 across all depths

**appendix_feature_distributions.tex**
- Text values only:
  - Median NLL: gen-0 = 1.64 nats, gen-4 = 0.02 nats
  - 8 generators, 25 texts/depth, ~236k tokens total, Pythia-410M reference

**appendix_feature_correlation.tex**
- Table (caption: "Pearson correlation matrix of the seven depth features")
  - $\bar{H}$: $\sigma_H$=0.49, $H_{min}$=0.31, $H_{max}$=0.01, $\tau$=0.07, TTR=0.86, Hapax=0.81
  - $\sigma_H$: $\bar{H}$=0.49, $H_{min}$=-0.15, $H_{max}$=0.16, $\tau$=0.26, TTR=0.43, Hapax=0.34
  - $H_{min}$: $\bar{H}$=0.31, $\sigma_H$=-0.15, $H_{max}$=-0.04, $\tau$=0.01, TTR=0.20, Hapax=0.23
  - $H_{max}$: $\bar{H}$=0.01, $\sigma_H$=0.16, $H_{min}$=-0.04, $\tau$=-0.08, TTR=-0.13, Hapax=-0.15
  - $\tau$: $\bar{H}$=0.07, $\sigma_H$=0.26, $H_{min}$=0.01, $H_{max}$=-0.08, TTR=0.13, Hapax=0.14
  - TTR: $\bar{H}$=0.86, $\sigma_H$=0.43, $H_{min}$=0.20, $H_{max}$=-0.13, $\tau$=0.13, Hapax=0.97
  - Hapax: $\bar{H}$=0.81, $\sigma_H$=0.34, $H_{min}$=0.23, $H_{max}$=-0.15, $\tau$=0.14, TTR=0.97
  - Text values: TTR-hapax r=0.97; PCA drifting subset PC1 = 92.3%, loadings 0.56-0.59; full 7-feature PCA: PC1 = 44.4% (drifting loadings 0.53-0.55), PC2 = 18.3% (entropy std vs min contrast); N = 27,529

**appendix_feature_candidates.tex**
- Table (caption: "Candidate feature screening")
  - median: |ρ| = 0.685, d = 0.794, LOFO ΔF1 = +0.008, |r|_max = 0.960, most correlated = entropy_mean
  - p90: |ρ| = 0.693, d = 0.960, LOFO ΔF1 = +0.000, |r|_max = 0.937, most correlated = entropy_mean
  - IQR: |ρ| = 0.708, d = 1.079, LOFO ΔF1 = +0.007, |r|_max = 0.908, most correlated = entropy_std
  - CV: |ρ| = 0.633, d = 0.980, LOFO ΔF1 = -0.000, |r|_max = 0.761, most correlated = entropy_mean
  - skewness: |ρ| = 0.651, d = 0.940, LOFO ΔF1 = +0.010, |r|_max = 0.780, most correlated = entropy_mean
  - kurtosis: |ρ| = 0.635, d = 0.769, LOFO ΔF1 = -0.003, |r|_max = 0.650, most correlated = entropy_mean
  - Text values: 6-feature baseline LOGO F1 = 0.733, adding all 6 candidates reduces to 0.722; removing skewness +0.010, median +0.008, IQR +0.007 improves

**appendix_nll_distribution.tex**
- Text values only:
  - Median NLL gen-0 = 1.64 nats
  - Median NLL gen-4 = 0.02 nats
  - ~236k tokens
  - 8 generators, Pythia-410M reference

**appendix_qualitative_examples.tex**
- Table (caption: "Example text chain from seed 120 (qualitative text)")
  - Text examples provided (Gen-0, Gen-1, Gen-2)

- Table (caption: "Feature values for the chain")
  - Feature | Gen-0 | Gen-1 | Gen-2
  - $\bar{H}$ (entropy mean) | 2.720 | 2.206 | 0.780
  - $\sigma_H$ (entropy std) | 1.772 | 1.816 | 1.517
  - $H_{min}$ (entropy min) | 0.002 | 0.005 | 0.000
  - $H_{max}$ (entropy max) | 7.000 | 7.016 | 6.926
  - tail decay | -0.00227 | -0.00231 | -0.00223
  - TTR | 0.659 | 0.272 | 0.081
  - hapax ratio | 0.561 | 0.183 | 0.005

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce8979d7-ba65-4283-b988-95f3d6d51af7",
  "isSidechain": true,
  "agentId": "a4ee533cda4eea682",
  "requestId": "req_011CbKLRZW3Yeh3U2FJ1Ropv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e3d899e4-3207-44fc-925a-67e19e7c87bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017S2yVvPGYpkdEej4cGewix",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 36117,
      "cache_read_input_tokens": 17476,
      "output_tokens": 11910,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 36117
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 11910,
          "cache_read_input_tokens": 17476,
          "cache_creation_input_tokens": 36117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 36117,
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
