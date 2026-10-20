# Research conversation: Check these 3 LaTeX files for internal number consistency. The files are from a paper that was just updated with multi-s

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-abecba583dd61bae9.jsonl`
- **Structured JSON:** [`c3faf96bc05e5dc9072d.json`](../../sessions/c3/c3faf96bc05e5dc9072d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-19T08:16:55.268Z_

Check these 3 LaTeX files for internal number consistency. The files are from a paper that was just updated with multi-seed means. Report any mismatches between the same quantity appearing in different places.

Key numbers to verify:
- 4B SFT Ign-F1: should be 43.58±3.80 in Tables 1 and 3
- 4B RSFT Ign-F1: should be 44.82±0.51 in Tables 1 and 3
- 4B evidence tax: should be -3.63
- 4B RSFT gain: should be +1.24
- 8B SFT Ign-F1: should be 48.66±2.62 in Table 3
- 8B RSFT Ign-F1: should be 54.14±0.53 in Table 3
- 8B evidence tax: should be -2.13
- 8B RSFT gain: should be +5.48
- 1.7B RSFT surpasses 8B SFT: 51.22 vs 48.66 (8B SFT is now multi-seed mean)
- Table 2 (spectrum) SFT: Rel-F1 44.39, Evi-F1 79.61, EDCR 0.6797
- Table 2 RSFT: Rel-F1 45.80, Evi-F1 80.96, EDCR 0.6487

Also check: are there any remaining references to OLD numbers (39.74, 40.49, 7.47, 4.92, 50.51, 54.24, 0.6982, 0.6503) that should have been updated but weren't? Some old numbers are OK in context (e.g., ablation table uses SFT s42 = 39.74 explicitly).

Files to check:
1. /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex

Report each finding as: [OK] or [MISMATCH: location, expected, found]


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "0e5a603e-03fc-4e6d-b6d1-bb1e75f91437",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-19T08:16:57.116Z_

I'll systematically check these three LaTeX files for the key numbers you've specified. Let me start by reading all three files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e5a603e-03fc-4e6d-b6d1-bb1e75f91437",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbaLUBnqpYJEBtuwDGE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd07f641-8d49-479d-b4e0-e29917a8c224",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PAHwnw79AKAt8w8daRf6qe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25395,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25395,
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

_source line 3 · 2026-05-19T08:16:57.366Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fdus8WguFuWcjMidqM69NL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd07f641-8d49-479d-b4e0-e29917a8c224",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbaLUBnqpYJEBtuwDGE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "84a0f91a-9ed7-4528-9064-dbf36376d602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PAHwnw79AKAt8w8daRf6qe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25395,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25395,
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

_source line 4 · 2026-05-19T08:16:57.386Z_

<details><summary>↩ Tool result · `toolu_01Fdus8WguFuWcjMidqM69NL`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Dataset.}
8	We conduct experiments on DocRED~\citep{yao2019docred}, a large-scale document-level relation extraction benchmark containing 3,053 training and 998 development documents spanning 96 relation types. Each document requires identifying relational triples across multiple sentences and grounding each triple with supporting evidence sentences. We use Re-DocRED~\citep{tan2022redocred} for cross-dataset generalization evaluation.
9	
10	\paragraph{Models.}
11	Our primary model is Qwen3-4B. To study scale effects, we additionally train Qwen3-1.7B and Qwen3-8B under identical configurations. We include LLaMA-3.1-8B as a cross-family validation point.
12	
13	\paragraph{Training.}
14	All models use LoRA~\citep{hu2022lora} with rank $r{=}64$ and $\alpha{=}128$ over a structured output format that jointly produces relation triples and evidence sentences. For RSFT, we sample $N{=}8$ candidate outputs per document and select the top-$k{=}1$ response ranked by CED scoring (\S\ref{sec:ced}), which combines NLI-based evidence faithfulness with extraction accuracy. GRPO experiments use group sizes $G{=}4$ (QLoRA, 4-bit) and $G{=}8$ (bf16 full-precision LoRA). DPO constructs preference pairs from CED-ranked outputs.
15	
16	\paragraph{Metrics.}
17	We report five metrics. \textbf{Ign-F1} is the primary DocRED metric that ignores triples appearing in the training set, matching the official leaderboard protocol. \textbf{Rel-F1} measures relation extraction F1 on all triples. \textbf{Evi-F1 (TP-only)} measures evidence sentence F1 conditioned on correctly predicted triples, reflecting evidence quality independent of extraction errors. \textbf{Evi-F1 (joint)} includes false-positive and false-negative triples in the denominator following the DREEAM protocol~\citep{ma2023dreeam}, enabling cross-method evidence comparison. \textbf{EDCR} (Evidence-Decoupling Ratio) is our proposed diagnostic: the ratio of evidence recall on correctly-predicted triples to overall extraction recall, where values substantially exceeding the SFT baseline indicate RL-induced decoupling. All primary results use the development set; test set submission is pending.
18	
19	
20	\subsection{Main Results}
21	\label{sec:main_results}
22	
23	Table~\ref{tab:main} presents the primary comparison between SFT, no-evidence SFT, and RSFT CED on Qwen3-4B. Across three training seeds, the SFT baseline achieves 43.58 Ign-F1 (standard deviation 3.80) with joint evidence generation. Removing evidence from the output format entirely (no-evidence SFT) improves extraction to 47.21 Ign-F1, a 3.63-point gap that quantifies the \emph{evidence tax} at the 4B scale. RSFT CED achieves a three-seed mean of 44.82 Ign-F1 (+1.24 over SFT, standard deviation 0.51) while maintaining evidence quality (Evi-F1 80.96 vs.\ 79.61 for SFT). The EDCR decreases from 0.6797 to 0.6487, confirming tighter coupling between extraction and evidence capabilities. The SFT variance (3.80pp) is 7.5$\times$ that of RSFT (0.51pp), indicating that CED-based selection compresses seed sensitivity in addition to improving mean performance. Per-seed results appear in Appendix~\ref{sec:ablation_full}.
24	
25	The remaining gap to the no-evidence upper bound (2.39 points) represents the residual cost of producing structured evidence, a cost that shrinks at larger scales as we show in Section~\ref{sec:scaling}.
26	
27	\begin{table}[t]
28	\centering
29	\caption{Main results on DocRED dev set (Qwen3-4B). SFT reports three-seed mean $\pm$ std; RSFT reports three-seed mean $\pm$ std (seeds 42, 43, 44). Best Ign-F1 in \textbf{bold}; best among evidence-generating methods \underline{underlined}. Per-seed breakdown in Appendix Table~\ref{tab:ablation_full}.}
30	\label{tab:main}
31	\small
32	\resizebox{\columnwidth}{!}{%
33	\begin{tabular}{lcccc}
34	\toprule
35	\textbf{Method} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
36	\midrule
37	SFT baseline & 43.58{\scriptsize$\pm$3.80} & 44.39 & 79.61 & 0.6797 \\
38	SFT no-evidence & \textbf{47.21} & \textbf{48.76} & -- & -- \\
39	RSFT CED & \underline{44.82{\scriptsize$\pm$0.51}} & \underline{45.80} & 80.96 & 0.6487 \\
40	\bottomrule
41	\end{tabular}%
42	}
43	\end{table}
44	
45	
46	\subsection{Evidence-Extraction Decoupling Spectrum}
47	\label{sec:spectrum}
48	
49	Different RL algorithms produce qualitatively different failure modes when applied to joint evidence-and-extraction generation. We organize these outcomes along a \emph{decoupling spectrum} ranging from catastrophic collapse to mild perturbation, shown in Table~\ref{tab:spectrum} (visualized in Figure~\ref{fig:spectrum}, Appendix).
50	
51	\paragraph{GRPO QLoRA: catastrophic collapse.}
52	Under QLoRA quantization ($G{=}4$), GRPO drives Rel-F1 to 1.38 (near zero extraction) while Evi-F1 rises to 85.04 and EDCR reaches 0.9876. The model learns to produce well-formed evidence sentences but loses the ability to predict correct relation triples. This extreme decoupling co-occurs with 4-bit quantization, which constrains the effective parameter space. We hypothesize that reduced precision limits the model's ability to jointly optimize both sub-tasks, though the bf16 result below shows that GRPO with sufficient precision avoids this failure mode.
53	
54	\paragraph{GRPO bf16: mild, variable.}
55	Full-precision GRPO ($G{=}8$) avoids catastrophe. Its training trajectory shows variable Rel-F1 fluctuation (43.4 at step 30, 42.8 at step 50, 43.4 at step 70, 45.5 at step 100), stabilizing near the SFT baseline. The best checkpoint achieves Rel-F1 45.49 with Evi-F1 80.86 and EDCR 0.6318, below the SFT baseline EDCR of 0.6797. This indicates that GRPO with sufficient precision does not exhibit the decoupling pattern, and both sub-tasks can improve jointly, though the variable trajectory suggests fragile optimization dynamics that require careful checkpoint selection.
56	
57	\paragraph{DPO: gradual decay.}
58	DPO preference learning shows a progressive pattern. At 1 epoch, Rel-F1 remains at 40.34 with Evi-F1 80.88 and EDCR 0.7139. Extended training (3 epochs) degrades extraction to 34.29 while evidence improves to 84.03\footnote{DPO 3-epoch results use an earlier evaluation protocol; included for trend analysis.}, with EDCR rising to 0.7294. Unlike GRPO's sudden collapse, DPO gradually trades extraction quality for evidence quality as training progresses.
59	
60	\paragraph{RSFT: no decoupling.}
61	RSFT avoids the decoupling problem entirely. By selecting high-quality complete outputs (jointly good extraction and evidence) rather than applying gradient-based reward maximization, RSFT maintains both capabilities simultaneously (mean Rel-F1 45.80, Evi-F1 80.96, EDCR 0.6487). The key insight is that rejection sampling operates on discrete outputs rather than differentiable reward signals, so it cannot exploit the extraction-evidence trade-off that gradient methods find.
62	
63	\begin{table}[t]
64	\centering
65	\caption{Evidence-extraction decoupling across RL paradigms (Qwen3-4B). Severity indicates the degree of extraction collapse relative to evidence improvement.}
66	\label{tab:spectrum}
67	\small
68	\resizebox{\columnwidth}{!}{%
69	\begin{tabular}{llcccc}
70	\toprule
71	\textbf{Paradigm} & \textbf{Config} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Severity} \\
72	\midrule
73	GRPO & QLoRA $G{=}4$ & 1.38 & 85.04 & 0.9876 & Catastrophic \\
74	GRPO & bf16 $G{=}8$ & 45.49 & 80.86 & 0.6318 & Mild \\
75	DPO & bf16 1ep & 40.34 & 80.88 & 0.7139 & Gradual \\
76	DPO & bf16 3ep$^\dagger$ & 34.29 & 84.03 & 0.7294 & Gradual \\
77	\midrule
78	SFT & baseline$^\ddagger$ & 44.39 & 79.61 & 0.6797 & None \\
79	RSFT & CED$^\ddagger$ & 45.80 & 80.96 & 0.6487 & None \\
80	\bottomrule
81	\end{tabular}%
82	}
83	\vspace{-2mm}
84	{\raggedright\footnotesize $^\dagger$Earlier evaluation protocol. $^\ddagger$Three-seed mean.\par}
85	\end{table}
86	
87	
88	\subsection{Scale-Dependent Evidence Tax}
89	\label{sec:scaling}
90	
91	The evidence tax, defined as the Ign-F1 difference between no-evidence and joint-evidence SFT, varies across model scales. Table~\ref{tab:scaling} presents this analysis across four models (Figure~\ref{fig:scaling} in Appendix).
92	
93	At the 4B scale, the evidence tax is $-3.63$ points (three-seed mean), though SFT variance is high ($\pm$3.80pp). At 8B, the two-seed SFT mean is $-2.13$ points (Qwen3-8B) and $-0.68$ for LLaMA-3.1-8B, indicating that larger models absorb the cost of joint evidence generation more effectively. The most surprising result appears at 1.7B: instead of paying a larger tax, the smallest model \emph{benefits} from evidence generation (+8.04 points raw). However, the no-evidence model suffers a higher truncation rate (50.9\% vs.\ 31.9\% for the evidence model), partially inflating this gap. On a controlled evaluation subset that excludes truncated and repetitive outputs (442/985 documents; definition in Appendix~\ref{sec:fair_subset}), the benefit is +6.2 points. Crucially, even on this controlled subset the direction remains positive, opposite to the negative tax at 4B and 8B, confirming that the scale-dependent pattern is not an artifact of output format differences. We hypothesize that for small models, evidence generation provides implicit regularization, forcing the model to attend to supporting context rather than memorizing surface-level patterns.
94	
95	RSFT improves all scales. The gain is +3.36 for 1.7B, +1.24 for 4B, and +5.48 for 8B, confirming that CED-based selection generalizes across model capacities. RSFT also compresses variance: at 4B, SFT standard deviation is 3.80pp while RSFT achieves 0.51pp (7.5$\times$ reduction). The 8B model benefits most in absolute gain because multi-seed SFT averaging reveals higher baseline variance than previously observed with a single seed. A striking consequence is that 1.7B RSFT achieves 51.22 Ign-F1, surpassing the 8B SFT mean of 48.66 (+2.56pp). CED-based rejection sampling enables a 1.7B model to surpass a 4.7$\times$ larger model on evidence-grounded extraction, with direct implications for deployment cost.
96	
97	\begin{table}[t]
98	\centering
99	\caption{Scale-dependent evidence tax and RSFT gain. Evidence tax = SFT with evidence minus SFT no-evidence (positive means evidence helps). All results on DocRED dev set Ign-F1. Multi-seed mean $\pm$ std reported where available (4B: 3-seed, 8B: 2-seed).}
100	\label{tab:scaling}
101	\small
102	\resizebox{\columnwidth}{!}{%
103	\begin{tabular}{lccccc}
104	\toprule
105	\textbf{Model} & \textbf{SFT w/ evi} & \textbf{No-evi} & \textbf{RSFT} & \textbf{Evi Tax} & \textbf{RSFT Gain} \\
106	\midrule
107	Qwen3-1.7B & 47.86 & 39.82 & 51.22 & +8.04 & +3.36 \\
108	Qwen3-4B & 43.58{\scriptsize$\pm$3.80} & 47.21 & 44.82{\scriptsize$\pm$0.51} & $-$3.63 & +1.24 \\
109	Qwen3-8B & 48.66{\scriptsize$\pm$2.62} & 50.79 & 54.14{\scriptsize$\pm$0.53} & $-$2.13 & +5.48 \\
110	LLaMA-3.1-8B & 53.84 & 54.52 & 57.14 & $-$0.68 & +3.30 \\
111	\bottomrule
112	\end{tabular}%
113	}
114	\end{table}
115	
116	
117	\subsection{Evidence Strategy Comparison}
118	\label{sec:evidence_strategy}
119	
120	We compare joint generation against post-hoc retrieval, using Evi-F1 (joint) with the DREEAM-protocol denominator~\citep{ma2023dreeam} for fair cross-strategy comparison. Post-hoc BM25 retrieval (entity-constrained, $k{=}2$ sentences per triple) achieves higher Rel-F1 (48.76) by avoiding the evidence tax, but produces lower Evi-F1 (joint) of 34.7 with EDCR 0.766. RSFT CED (s43) reaches Evi-F1 (joint) 36.1 with EDCR 0.654, a 1.4-point evidence advantage and 0.112 EDCR reduction. CED reranking at inference time (selecting the best of $N{=}8$ outputs by CED score) achieves Rel-F1 48.64 and Evi-F1 81.88 (TP-only), approaching no-evidence extraction quality while preserving evidence. Joint training produces more faithful evidence grounded in the extraction reasoning rather than retrieved post-hoc; inference-time reranking complements this by recovering extraction accuracy.
121	
122	
123	\subsection{Generalization}
124	\label{sec:generalization}
125	
126	Cross-architecture validation on LLaMA-3.1-8B confirms the scaling patterns: the evidence tax at 8B is near zero ($-0.68$ points), and RSFT CED yields +3.30 Ign-F1 gain. The RSFT improvement transfers consistently across datasets: on Re-DocRED~\citep{tan2022redocred}, RSFT achieves 41.45 Ign-F1 (+4.86pp over SFT baseline 36.59), closely matching the +4.92pp gain on DocRED. Evidence quality remains stable (Evi-F1 81.82 vs.\ 81.70 for SFT) with improved coupling (EDCR 0.6210 vs.\ 0.6674). Our best joint Evi-F1 (36.1, DREEAM-protocol denominator) falls below supervised DREEAM (54.01\%~\citep{ma2023dreeam}), a gap driven by extraction performance rather than evidence quality (TP-only Evi-F1 exceeds 80\%). Full results appear in Appendix~\ref{sec:generalization_full}.
127	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84a0f91a-9ed7-4528-9064-dbf36376d602",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "edd505fa-57fe-484a-831f-ea8ff6921bfa",
  "sourceToolAssistantUUID": "84a0f91a-9ed7-4528-9064-dbf36376d602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T08:16:57.779Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BFnc1djauxY5pNKXYQr7oT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edd505fa-57fe-484a-831f-ea8ff6921bfa",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbaLUBnqpYJEBtuwDGE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "92dc6b87-929a-4063-96c6-4918cb00e926",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PAHwnw79AKAt8w8daRf6qe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25395,
      "cache_read_input_tokens": 0,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25395
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 262,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 25395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25395,
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

### Tool call

_source line 6 · 2026-05-19T08:16:57.789Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QyRuyXCnuThGkpfsrCmyJH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92dc6b87-929a-4063-96c6-4918cb00e926",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbaLUBnqpYJEBtuwDGE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1cca7d68-2207-4566-841b-10b5ce251c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PAHwnw79AKAt8w8daRf6qe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25395,
      "cache_read_input_tokens": 0,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25395
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 262,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 25395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25395,
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

_source line 7 · 2026-05-19T08:16:57.797Z_

<details><summary>↩ Tool result · `toolu_01BFnc1djauxY5pNKXYQr7oT`</summary>

```text
1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to attention projections. SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B as the base model with LoRA adaptation. A dash indicates that the parameter is not applicable to the given method.}
9	\label{tab:hyperparams}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	\textbf{Parameter} & \textbf{SFT} & \textbf{RSFT} & \textbf{GRPO QLoRA} & \textbf{GRPO bf16} & \textbf{DPO} \\
14	\midrule
15	Base model & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B & Qwen3-4B \\
16	LoRA rank $r$ & 64 & 64 & 64 & 64 & 64 \\
17	LoRA $\alpha$ & 128 & 128 & 128 & 128 & 128 \\
18	Learning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\
19	Batch size (effective) & 16 & 16 & 4 & 8 & 4 \\
20	Epochs & 3 & 3 & -- & -- & 1, 3\textsuperscript{$\star$} \\
21	Max steps & -- & -- & 100 & 100 & -- \\
22	Gradient accumulation & 4 & 4 & 16 & 4 & 4 \\
23	Max new tokens & 1024 & 1024 & 1024 & 1024 & 1024 \\
24	Quantization & -- & -- & NF4 4-bit & bf16 & bf16 \\
25	Group size $G$ & -- & -- & 4 & 8 & -- \\
26	KL coefficient & -- & -- & 0.01 & 0.01 & -- \\
27	$\beta$ (DPO) & -- & -- & -- & -- & 0.1 \\
28	Candidates $N$ & -- & 8 & -- & -- & 8 \\
29	Top-$k$ selection & -- & 1 & -- & -- & -- \\
30	Training samples & 3,053 & 2,718 & 3,053 & 3,053 & 3,053 \\
31	Scoring function & -- & CED & CED & CED & CED \\
32	\bottomrule
33	\end{tabular}
34	\vspace{1mm}
35	{\raggedright\footnotesize \textsuperscript{$\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction trade-off (Section~\ref{sec:spectrum}).\par}
36	\end{table*}
37	
38	
39	\section{Full Ablation Results}
40	\label{sec:ablation_full}
41	
42	Table~\ref{tab:ablation_full} reports the complete RSFT ablation across scoring functions, top-$k$ values, and random seeds. RSFT CED $k{=}1$ achieves a four-seed mean Ign-F1 of 44.66 (standard deviation 0.49), confirming robust improvement over the SFT s42 baseline (39.74). The three-seed mean reported in Table~\ref{tab:main} (44.82, seeds 42/43/44) is slightly higher because it excludes the lowest seed (s45: 44.16). Random selection RSFT $k{=}1$ (41.14 Ign-F1), which samples from the same candidate pool without CED scoring, improves only +1.40pp over SFT s42 versus +4.92pp for CED RSFT, confirming that CED scoring precision drives the majority of the RSFT gain. Increasing $k$ to 3 slightly degrades performance (43.64 Ign-F1), consistent with the intuition that stricter selection yields higher-quality training data. The flat-NLI scoring variant produces comparable Rel-F1 (mean 45.61 vs.\ 45.63 for CED, a difference of 0.02pp). Both CED and flat-NLI improve substantially over the SFT baseline while maintaining or improving Evi-F1, confirming that the RSFT gains are driven by quality-based data selection rather than by the specific contrastive formulation.
43	
44	\paragraph{NLI scoring comparison.} Across all available seeds, CED RSFT achieves mean Rel-F1 of 45.63 (seeds 42, 43, 44, 45: range 45.14--46.21), and flat-NLI RSFT achieves mean Rel-F1 of 45.61 (seeds 42, 43: range 45.35--45.86). The 0.02pp difference suggests comparable performance: CED's contrastive design does not substantially outperform simpler NLI scoring for RSFT data selection. We adopt CED as the default because its contrastive formulation produces per-triple discrimination scores that support interpretable error analysis.
45	
46	\paragraph{Top-$k$ selection.} Best-of-8 ($k{=}1$) yields mean Ign-F1 44.66 and Rel-F1 45.63, while top-3-of-8 ($k{=}3$) produces 43.64 and 44.54. The selected training data confirms the quality gap: $k{=}1$ data has mean extraction F1 of 61.57 and mean CED of 0.6683, versus 57.61 and 0.6205 for $k{=}3$. Despite $k{=}3$ providing 2.96$\times$ more training examples, the additional lower-ranked samples introduce noise that degrades final performance.
47	
48	\begin{table}[t]
49	\centering
50	\caption{Full RSFT ablation on DocRED dev set (Qwen3-4B). CED and flat-NLI denote the scoring function used for candidate selection. Best Ign-F1 among evidence-generating methods in \textbf{bold}.}
51	\label{tab:ablation_full}
52	\small
53	\resizebox{\columnwidth}{!}{%
54	\begin{tabular}{lcccc}
55	\toprule
56	\textbf{Configuration} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
57	\midrule
58	SFT baseline (s42) & 39.74 & 40.49 & 79.86 & 0.6982 \\
59	SFT no-evidence & \textbf{47.21} & 48.76 & -- & -- \\
60	\midrule
61	RSFT random $k{=}1$ & 41.14 & 41.98 & 79.64 & 0.6971 \\
62	\midrule
63	RSFT CED $k{=}1$ (s42) & 44.23 & 45.17 & 81.74 & 0.6569 \\
64	RSFT CED $k{=}1$ (s43) & 45.12 & 46.01 & 80.63 & 0.6542 \\
65	RSFT CED $k{=}1$ (s44) & 45.11 & 46.21 & 80.50 & 0.6350 \\
66	RSFT CED $k{=}1$ (s45) & 44.16 & 45.14 & 81.74 & 0.6550 \\
67	RSFT CED $k{=}1$ (mean) & 44.66 & 45.63 & 81.15 & 0.6503 \\
68	\midrule
69	RSFT CED $k{=}3$ & 43.64 & 44.54 & 80.88 & 0.6635 \\
70	\midrule
71	RSFT flat-NLI (s42) & -- & 45.35 & 80.43 & 0.6431 \\
72	RSFT flat-NLI (s43) & -- & 45.86 & 81.58 & 0.6505 \\
73	RSFT flat-NLI (mean) & -- & 45.61 & 81.01 & 0.6468 \\
74	\bottomrule
75	\end{tabular}%
76	}
77	\end{table}
78	
79	
80	\section{Scaling Details}
81	\label{sec:scaling_details}
82	
83	Table~\ref{tab:cross_detail} supplements Table~\ref{tab:scaling} in the main text with per-scale Rel-F1 and Evi-F1 breakdowns. At 1.7B, RSFT improves Rel-F1 from 49.45 to 52.90 (+3.45) while achieving Evi-F1 82.43 and EDCR 0.6224. The 4B model shows the same pattern: Rel-F1 increases from 44.39 to 45.80 (+1.41, three-seed mean). For 8B, RSFT brings Rel-F1 from 50.52 to 56.10 (two-seed mean) with Evi-F1 of 81.52 and EDCR 0.6198, confirming tight coupling between extraction and evidence at this scale.
84	
85	\begin{table}[t]
86	\centering
87	\caption{Detailed Rel-F1 and Evi-F1 across model scales on DocRED dev set. SFT and RSFT columns show multi-seed means where available (4B: 3-seed, 8B: 2-seed), single seed for 1.7B and LLaMA.}
88	\label{tab:cross_detail}
89	\small
90	\resizebox{\columnwidth}{!}{%
91	\begin{tabular}{lccccc}
92	\toprule
93	\textbf{Model} & \textbf{SFT Rel-F1} & \textbf{SFT Evi-F1} & \textbf{RSFT Rel-F1} & \textbf{RSFT Evi-F1} & \textbf{RSFT EDCR} \\
94	\midrule
95	Qwen3-1.7B & 49.45 & 83.16 & 52.90 & 82.43 & 0.6224 \\
96	Qwen3-4B & 44.39 & 79.61 & 45.80 & 80.96 & 0.6487 \\
97	Qwen3-8B & 50.52 & 82.75 & 56.10 & 81.52 & 0.6198 \\
98	LLaMA-3.1-8B & 55.14 & 81.51 & 58.39 & 82.43 & 0.5799 \\
99	\bottomrule
100	\end{tabular}%
101	}
102	\end{table}
103	
104	
105	\section{Controlled Evaluation Subset}
106	\label{sec:fair_subset}
107	
108	The 1.7B evidence tax comparison (\S\ref{sec:scaling}) is confounded by differential output quality: the no-evidence model truncates 50.9\% of outputs (501/985 documents) at the \texttt{max\_new\_tokens} limit, versus 31.9\% (314/985) for the evidence model. To control for this, we define a \emph{controlled evaluation subset} that excludes any document where either model produces a truncated or repetitive output. An output is classified as \emph{truncated} if it reaches the generation length limit. An output is classified as \emph{repetitive} if it contains $\geq$3 consecutive identical triples or if the ratio of unique triples to total triples falls below 0.5 (when total $> 5$). The resulting subset contains 442 of 985 development documents (44.9\%). On this subset, the 1.7B evidence tax is +6.2pp (vs.\ +8.04pp on the full set), indicating that approximately 23\% of the raw gap is attributable to the no-evidence model's higher truncation rate. The positive direction is preserved, confirming that the 1.7B evidence benefit is genuine and not an artifact of output format differences.
109	
110	Table~\ref{tab:mechanistic} provides a mechanistic breakdown across three scales. Output duplication rate (fraction of documents containing $\geq$3 repeated triples or unique/total $< 0.5$) declines monotonically with scale for both training configurations, but the gap between no-evidence and with-evidence models narrows from 27.5pp at 1.7B to 3.7pp at 8B. This pattern supports the implicit regularization hypothesis: evidence generation forces smaller models to attend to supporting context, reducing degenerate repetition. At 4B, duplication is already moderate (31.1\% with evidence), so the regularization benefit diminishes, while the model lacks sufficient capacity to jointly optimize extraction and evidence generation, creating the capacity valley that produces the largest evidence tax ($-3.63$pp, three-seed SFT mean). The truncation asymmetry reverses across scales: at 1.7B the no-evidence model truncates 19pp more often; at 8B the evidence model truncates 9pp more often due to the longer output format.
111	
112	\begin{table}[t]
113	\centering
114	\caption{Mechanistic breakdown of output quality across scales. Duplication rate: fraction of documents with degenerate outputs. Truncation $\Delta$: no-evidence rate minus with-evidence rate (positive means no-evidence truncates more).}
115	\label{tab:mechanistic}
116	\small
117	\begin{tabular}{lccccc}
118	\toprule
119	& \multicolumn{3}{c}{\textbf{Duplication Rate}} & \multicolumn{2}{c}{\textbf{Truncation}} \\
120	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
121	\textbf{Scale} & \textbf{w/ evi} & \textbf{no-evi} & \textbf{Gap} & \textbf{$\Delta$} & \textbf{Pattern} \\
122	\midrule
123	1.7B & 33.0 & 60.5 & 27.5 & +19 & no-evi worse \\
124	4B & 31.1 & 43.2 & 12.1 & +2 & neutral \\
125	8B & 29.2 & 32.9 & 3.7 & $-$9 & evi worse \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	
131	\section{Why RSFT Avoids Decoupling}
132	\label{sec:rsft_theory}
133	
134	The structural difference between selection and optimization explains why RSFT does not exhibit the decoupling observed in gradient-based methods. GRPO and DPO update model parameters through gradients that optimize a reward signal. When two sub-tasks (extraction and evidence) compete for gradient capacity, the optimizer can discover and exploit the trade-off between them, improving one at the expense of the other. RSFT operates differently: it selects complete outputs and trains on them with standard supervised loss. Because the selection is discrete (accept or reject a full response), there is no gradient pathway through which the model can learn to sacrifice extraction for evidence quality. Only outputs where both extraction and evidence are jointly strong survive the CED filter. This property is not specific to RSFT's design but is a structural consequence of discrete selection over complete outputs: any selection-based method that filters on a joint quality criterion will inherit the same coupling guarantee. The implication for practitioners is direct: when optimizing for multiple coupled generation objectives, selection-based methods preserve inter-objective balance that gradient-based methods disrupt.
135	
136	
137	\section{Decoupling Spectrum Visualization}
138	\label{sec:spectrum_viz}
139	
140	\begin{figure}[t]
141	\centering
142	\includegraphics[width=\columnwidth]{fig_spectrum.pdf}
143	\caption{Decoupling spectrum visualization. Each method is plotted by Rel-F1 (x-axis) and Evi-F1 (y-axis). Arrows indicate training progression for DPO (1ep$\to$3ep) and GRPO bf16 trajectory. Ideal methods occupy the upper-right quadrant; decoupled methods drift toward the upper-left.}
144	\label{fig:spectrum}
145	\end{figure}
146	
147	
148	\section{Evidence Tax Visualization}
149	\label{sec:scaling_viz}
150	
151	\begin{figure}[t]
152	\centering
153	\includegraphics[width=\columnwidth]{fig_scaling.pdf}
154	\caption{Evidence tax across model scales. Bar heights show Ign-F1 for each training configuration. The gap between no-evidence and SFT bars reverses direction between 1.7B and 4B, revealing the scale-dependent nature of the evidence tax. RSFT consistently narrows the gap toward the no-evidence upper bound.}
155	\label{fig:scaling}
156	\end{figure}
157	
158	
159	\section{Full Generalization Results}
160	\label{sec:generalization_full}
161	
162	\paragraph{Cross-family transfer.}
163	LLaMA-3.1-8B confirms the scaling patterns observed with Qwen3. Its SFT baseline achieves 53.84 Ign-F1 (Rel-F1 55.14, Evi-F1 81.51), and the no-evidence variant reaches 54.52 Ign-F1 (Rel-F1 56.24). The evidence tax of $-0.68$ points mirrors the near-zero tax seen for Qwen3-8B ($-0.28$), supporting our claim that 8B-class models absorb the cost of joint evidence generation regardless of architecture family. RSFT CED improves LLaMA to 57.14 Ign-F1 (Rel-F1 58.39, Evi-F1 82.43), a +3.30 point gain consistent with the pattern at the 8B scale (Qwen3-8B: +3.73).
164	
165	\paragraph{Cross-dataset robustness.}
166	On Re-DocRED~\citep{tan2022redocred}, the SFT baseline achieves 36.59 Ign-F1 (Evi-F1 81.70, EDCR 0.6674). RSFT CED improves this to 41.45 Ign-F1 (Evi-F1 81.82, EDCR 0.6210), a +4.86pp gain that closely matches the +4.92pp improvement on DocRED. This consistency across datasets with different annotation protocols confirms that RSFT's benefit generalizes beyond training-set-specific artifacts. Evidence quality remains stable across datasets (Evi-F1 81.82 vs.\ 81.15 on DocRED), and the EDCR reduction ($-0.046$) mirrors the DocRED pattern, further supporting the robustness of CED-based selection.
167	
168	\paragraph{Comparison to supervised methods.}
169	Table~\ref{tab:encoder_comparison} directly compares encoder-based methods with our LLM-based approach. Encoder methods achieve substantially higher extraction performance (Rel-F1 63--65 vs.\ our 45--56), reflecting decades of architecture-specific optimization for the classification formulation. However, their evidence identification operates as binary sentence classification, producing Evi-F1 of 52--56 under a joint evaluation protocol. Our TP-only Evi-F1 exceeds 80\%, indicating that when the model correctly identifies a triple, it produces higher-quality evidence than encoder methods. The joint Evi-F1 gap (36.1 vs.\ 54.15) is driven primarily by extraction performance rather than evidence quality: false-positive and false-negative triples dilute the denominator. Closing this gap requires improving extraction capability of LLM-based methods, an orthogonal direction to the evidence faithfulness problem we address.
170	
171	\begin{table}[t]
172	\centering
173	\caption{Comparison with encoder-based methods on DocRED dev set. Encoder methods use RoBERTa-large; LLM methods use Qwen3. Evi-F1 for encoder methods uses joint evaluation (all triples in denominator); our joint Evi-F1 follows the same protocol for fair comparison. TP-only Evi-F1 conditions on correctly predicted triples. Rel-F1 is reported in percentage for all methods.}
174	\label{tab:encoder_comparison}
175	\small
176	\resizebox{\columnwidth}{!}{%
177	\begin{tabular}{llcccc}
178	\toprule
179	\textbf{Method} & \textbf{Type} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1 (joint)} & \textbf{Evi-F1 (TP)} \\
180	\midrule
181	ATLOP & Encoder & 61.32 & 63.18 & -- & -- \\
182	EIDER & Encoder & 62.34 & 64.27 & 52.54 & -- \\
183	SAIS & Encoder & 62.23 & 65.17 & 55.84 & -- \\
184	DREEAM & Encoder & 61.71 & 63.49 & 54.15 & -- \\
185	\midrule
186	Ours (4B RSFT) & LLM & 44.82 & 45.80 & 36.1 & 80.96 \\
187	Ours (8B RSFT) & LLM & 54.14 & 56.10 & -- & 81.52 \\
188	\bottomrule
189	\end{tabular}%
190	}
191	\end{table}
192	
193	
194	\section{GRPO Training Dynamics}
195	\label{sec:grpo_dynamics}
196	
197	\begin{figure*}[t]
198	\centering
199	\includegraphics[width=\linewidth]{fig_grpo_dynamics.pdf}
200	\caption{Training dynamics of GRPO under different configurations. (a)~Relation F1 across checkpoints: G=4 QLoRA suffers catastrophic collapse at step~10, while G=8 bf16 remains stable. (b)~Evidence F1 stays intact for G=8 bf16, confirming the generation mechanism itself does not fail. (c)~Evidence-Decoupling Ratio (EDCR) reveals near-total decoupling in G=4 QLoRA (extraction collapses to Rel-F1 1.4), while G=8 bf16 maintains healthy ratios.}
201	\label{fig:grpo_dynamics}
202	\end{figure*}
203	
204	
205	\section{Error Analysis: SFT vs.\ RSFT}
206	\label{sec:error_analysis}
207	
208	Table~\ref{tab:error_analysis} decomposes the extraction improvements from RSFT into error categories across three scales. Three mechanisms drive the gains consistently:
209	
210	\paragraph{Truncation false negatives.} SFT models frequently hit the generation length limit, producing incomplete outputs that miss triples. RSFT training on compact, high-quality outputs reduces this truncation rate. The effect is strongest at 1.7B ($-841$ truncation FN, $-22$\%), where the SFT model's output length is least controlled.
211	
212	\paragraph{Hallucinated false positives.} CED-based filtering removes training examples with unfaithful predictions, reducing the rate of hallucinated triples at inference. LLaMA benefits most ($-593$ hallucinated FP, $-11.8$\%), suggesting cross-architecture variation in hallucination susceptibility.
213	
214	\paragraph{Duplicate predictions.} RSFT training data, selected for quality, contains fewer repetitive patterns. This propagates to inference, reducing duplicate triples by $11$--$20$\% across scales, with 1.7B showing the largest reduction ($-20.2$\%).
215	
216	\paragraph{Evidence quality unchanged.} Despite substantial extraction improvements, evidence exact-match F1 changes by less than 0.4pp at every scale. RSFT selects for joint extraction-evidence quality, but the evidence signal in CED scoring does not translate into measurable evidence improvement. This suggests that evidence grounding requires targeted optimization (e.g., evidence-specific rewards in RL) rather than data selection alone.
217	
218	\paragraph{Residual difficulty.} The proportion of ``other'' false negatives (triples missed for reasons beyond truncation or formatting) increases by 13--15\% in relative terms after RSFT. As easy errors (truncation, duplication) are eliminated, the remaining error distribution shifts toward harder cases: cross-sentence reasoning, implicit relations, and long-tail entity pairs. The relation types with the largest RSFT gains (participant, conflict, league, screenwriter, operator, contains\_administrative\_territory) involve cross-sentence reasoning or long-tail entities, consistent with RSFT's selection pressure toward diverse, high-quality outputs.
219	
220	\begin{table}[t]
221	\centering
222	\caption{Error pattern changes from SFT to RSFT across scales. $\Delta$\% shows relative change. Truncation FN, hallucinated FP, and duplicates all decrease; evidence quality and residual FN difficulty are unchanged.}
223	\label{tab:error_analysis}
224	\small
225	\resizebox{\columnwidth}{!}{%
226	\begin{tabular}{llccc}
227	\toprule
228	\textbf{Error Category} & \textbf{Direction} & \textbf{1.7B} & \textbf{4B} & \textbf{8B / LLaMA} \\
229	\midrule
230	Truncation FN & $\downarrow$ & $-$22\% & $-$16\% & $-$18\% \\
231	Hallucinated FP & $\downarrow$ & $-$8\% & $-$6\% & $-$12\% \\
232	Duplicates & $\downarrow$ & $-$20\% & $-$11\% & $-$14\% \\
233	Evidence (exact) & $\approx$ & $<$0.4pp & $<$0.4pp & $<$0.4pp \\
234	FN: other & $\uparrow$ & +13\% & +15\% & +14\% \\
235	\bottomrule
236	\end{tabular}%
237	}
238	\end{table}
239	
240	
241	\section{Per-Relation EDCR Distribution}
242	\label{sec:edcr_per_relation}
243	
244	Computing EDCR for each of the 76 relation types with $\geq$5 evaluation samples (from the RSFT CED s42 model) reveals that per-relation EDCR correlates strongly with per-relation Rel-F1 ($\rho = -0.79$, $n = 76$, $p < 0.0001$), confirming its utility as a difficulty indicator. Filtering to types with $\geq$5 predictions strengthens the correlation ($\rho = -0.85$, $n = 74$, $p < 0.0001$). Per-relation EDCR is statistically independent of Evi-F1 ($\rho = -0.06$, $p = 0.58$), and Evi-F1 itself shows no association with Rel-F1 ($\rho = -0.01$, $p = 0.91$). These null correlations establish that evidence quality and extraction ability are fully decoupled across relation types. Extreme cases illustrate the diagnostic power: \texttt{date\_of\_birth} has EDCR $= 0.118$ (highly faithful, with extraction and evidence tightly coupled), while \texttt{head\_of\_government} reaches $0.956$ (highly decoupled). This per-relation analysis avoids the shared-component concern present in cross-method EDCR-vs-Rel-F1 correlation, providing independent validation of EDCR's diagnostic utility.
245	
246	\begin{figure}[t]
247	\centering
248	\includegraphics[width=\linewidth]{fig_edcr_relations.pdf}
249	\caption{Per-relation EDCR distribution across all 93 relation types observed in the development set (of 96 defined in DocRED). The correlation analysis in the text uses the 76 types with $\geq$5 samples for statistical reliability. Red bars indicate EDCR $\geq$ 0.70 (severe decoupling), green bars indicate EDCR $<$ 0.30 (healthy evidence grounding). Seven types exhibit EDCR = 1.0.}
250	\label{fig:edcr_relations}
251	\end{figure}
252	
253	
254	\section{Qualitative Analysis}
255	\label{sec:qualitative}
256	
257	We present representative examples illustrating three phenomena: evidence quality differences between SFT and RSFT, GRPO format gaming under catastrophic collapse, and per-relation EDCR diagnostics.
258	
259	\paragraph{Case 1: Evidence quality.}
260	Table~\ref{tab:case_evidence} compares evidence citations from SFT and RSFT on three documents. SFT tends to cite many sentences indiscriminately, including distractors unrelated to the target triple, while RSFT selects precisely the gold evidence sentences. For \emph{America's Sweetheart}, SFT cites 6 sentences (precision 0.17) whereas RSFT cites only the single correct sentence (precision 1.00). The pattern is consistent: SFT achieves evidence precision of 0.00--0.20 across these examples, while RSFT achieves 1.00 in all three cases.
261	
262	\begin{table}[t]
263	\centering
264	\caption{Evidence citation comparison between SFT and RSFT. Precision measures the fraction of cited sentences that match gold evidence.}
265	\label{tab:case_evidence}
266	\small
267	\resizebox{\columnwidth}{!}{%
268	\begin{tabular}{llccc}
269	\toprule
270	\textbf{Document} & \textbf{Triple} & \textbf{SFT Prec.} & \textbf{RSFT Prec.} & \textbf{SFT \#Cited} \\
271	\midrule
272	Oleg Tinkov & (Oleg Tinkov, country of citizenship, Russia) & 0.00 & 1.00 & 3 \\
273	America's Sweetheart & (record label, country, United States) & 0.17 & 1.00 & 6 \\
274	Jade (Mortal Kombat) & (Jade, present in work, Mortal Kombat) & 0.20 & 1.00 & 5 \\
275	\bottomrule
276	\end{tabular}%
277	}
278	\end{table}
279	
280	\paragraph{Case 2: GRPO format gaming.}
281	Under catastrophic collapse (GRPO QLoRA $G{=}4$), the model abandons the DocRED 96-type relation ontology and generates free-text relation labels. On the document \emph{Something to Believe In}, the model produces 35 predicted triples with relations such as ``is a'', ``honor'', and ``location'', none of which belong to the target ontology. All 35 predictions are incorrect. Similarly, for \emph{J\'{o}zef Pi\l{}sudski Monument}, 28 predictions use non-standard relations with 0 correct matches. The model retains the structural format of triple-with-evidence output but fills it with fabricated relation types. The model produces well-formed evidence for these non-existent relations.
282	
283	\paragraph{Case 3: EDCR diagnostics.}
284	Per-relation EDCR identifies specific relation types where extraction and evidence are misaligned. For \texttt{date\_of\_birth} (EDCR $= 0.118$), the model's evidence consistently matches gold annotations: both extraction and evidence point to the same biographical sentence. In contrast, \texttt{notable\_work} (EDCR $= 0.941$) exhibits severe decoupling: the model cites sentence [0] (a general introduction) instead of the gold evidence sentence [3] (which contains the actual work attribution). High-EDCR relations tend to involve indirect or multi-hop reasoning where surface-level context misleads the evidence generator.
285	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92dc6b87-929a-4063-96c6-4918cb00e926",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "461d80eb-9507-4082-b8a4-adb7ea25ed1b",
  "sourceToolAssistantUUID": "92dc6b87-929a-4063-96c6-4918cb00e926",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T08:16:57.807Z_

<details><summary>↩ Tool result · `toolu_01QyRuyXCnuThGkpfsrCmyJH`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\paragraph{EDCR as a diagnostic.}
5	EDCR (\S\ref{sec:edcr}) operates at two complementary levels. Cross-method, Spearman $\rho = -0.89$ ($n = 7$, $p = 0.007$) across seven independent method configurations (Table~\ref{tab:spectrum}). Removing the extreme GRPO QLoRA outlier yields $\rho = -0.83$ ($n = 6$, $p = 0.042$), indicating that GRPO QLoRA is a high-leverage point. Per-relation, $\rho = -0.79$ ($n = 76$, $p < 0.0001$) across relation types provides robust validation independent of method-level sample size. EDCR shows no correlation with Evi-F1 ($\rho = -0.06$, $p = 0.58$), confirming it captures information orthogonal to evidence quality (Appendix~\ref{sec:edcr_per_relation}). RSFT avoids decoupling because discrete output selection prevents trading extraction for evidence quality (Appendix~\ref{sec:rsft_theory}). We provide qualitative examples of these phenomena in Appendix~\ref{sec:qualitative}.
6	
7	\paragraph{CED granularity.}
8	CED operates effectively at the response level for both RSFT selection and inference-time reranking, but fails at sentence-level granularity: filtering individual evidence sentences by NLI score reduces Evi-F1 by 7.7pp (Recall $-$20pp), as it disrupts co-reference chains across evidence sentences. This suggests that evidence quality is a holistic response property rather than a per-sentence attribute.
9	
10	\paragraph{Ablation.}
11	CED and flat-NLI produce comparable performance (Rel-F1 45.63 vs.\ 45.61); stricter selection ($k{=}1$) outperforms $k{=}3$ by 1.02 Ign-F1 despite 2.96$\times$ fewer examples (Appendix~\ref{sec:ablation_full}).
12	
13	\paragraph{Error pattern shifts.}
14	RSFT reduces truncation FN ($-16$ to $-22$\%), hallucinated FP ($-6$ to $-12$\%), and duplicates ($-11$ to $-20$\%) consistently across scales (Appendix~\ref{sec:error_analysis}). However, evidence quality is unchanged ($\Delta < 0.4$pp), indicating that RSFT improves \emph{what} the model extracts but not \emph{how well} it grounds extractions.
15	
16	\paragraph{Practical implications.}
17	Our findings suggest three guidelines for practitioners seeking evidence-grounded IE: (1) avoid online RL for multi-objective generation tasks where capability coupling matters; (2) prefer RSFT with strict selection ($k{=}1$) over training data quantity; (3) consider CED reranking at inference for deployment scenarios requiring both high extraction accuracy and evidence quality.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cca7d68-2207-4566-841b-10b5ce251c08",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "9441c542-a026-439f-93f7-e12a0a81bc24",
  "sourceToolAssistantUUID": "1cca7d68-2207-4566-841b-10b5ce251c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-19T08:16:59.883Z_

Now let me search for the specific numbers to verify consistency. I'll search for key numerical values across all three files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9441c542-a026-439f-93f7-e12a0a81bc24",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbaX5QgYZrzowAYUWPP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bf90bf3e-5ddf-4da1-91ac-6cc747140546",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Qa24MqTT1hP1jfs1t1fmdy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 25395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15199,
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

_source line 10 · 2026-05-19T08:17:00.954Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GMU8DgBiVHkKzKE6XGSLFY`</summary>

```json
{
  "pattern": "43\\.58|43\\.58±3\\.80|±3\\.80",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf90bf3e-5ddf-4da1-91ac-6cc747140546",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbaX5QgYZrzowAYUWPP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fd5d8afa-b004-4050-b351-38b0511d998d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Qa24MqTT1hP1jfs1t1fmdy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 25395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15199,
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

_source line 11 · 2026-05-19T08:17:00.975Z_

<details><summary>↩ Tool result · `toolu_01GMU8DgBiVHkKzKE6XGSLFY`</summary>

```text
Found 1 file
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd5d8afa-b004-4050-b351-38b0511d998d",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "6cfd5905-c7fc-41ec-98a1-21935ed8f0bb",
  "sourceToolAssistantUUID": "fd5d8afa-b004-4050-b351-38b0511d998d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T08:17:01.392Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01MNfJW4RKvwSQrKgtQeMcwM`</summary>

```json
{
  "pattern": "44\\.82|44\\.82±0\\.51|±0\\.51",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cfd5905-c7fc-41ec-98a1-21935ed8f0bb",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbaX5QgYZrzowAYUWPP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b00b8aad-2634-4403-9a58-8c1a7f847f16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Qa24MqTT1hP1jfs1t1fmdy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 25395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15199,
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

_source line 13 · 2026-05-19T08:17:01.414Z_

<details><summary>↩ Tool result · `toolu_01MNfJW4RKvwSQrKgtQeMcwM`</summary>

```text
Found 2 files
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b00b8aad-2634-4403-9a58-8c1a7f847f16",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "dee09f54-11c4-4d18-9fef-155317f198e8",
  "sourceToolAssistantUUID": "b00b8aad-2634-4403-9a58-8c1a7f847f16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T08:17:01.605Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SLVTHFx9Zej5KNam4QeJwP`</summary>

```json
{
  "pattern": "48\\.66|48\\.66±2\\.62|±2\\.62",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dee09f54-11c4-4d18-9fef-155317f198e8",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbaX5QgYZrzowAYUWPP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "85e9d4d9-3952-436d-b803-bd835286f0a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Qa24MqTT1hP1jfs1t1fmdy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 25395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15199,
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

_source line 15 · 2026-05-19T08:17:01.627Z_

<details><summary>↩ Tool result · `toolu_01SLVTHFx9Zej5KNam4QeJwP`</summary>

```text
Found 1 file
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85e9d4d9-3952-436d-b803-bd835286f0a3",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "92882ec6-6c77-4dfd-b815-43f587e4f175",
  "sourceToolAssistantUUID": "85e9d4d9-3952-436d-b803-bd835286f0a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T08:17:01.974Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013frisFnRrVaPXEsr7Twkus`</summary>

```json
{
  "pattern": "54\\.14|54\\.14±0\\.53|±0\\.53",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92882ec6-6c77-4dfd-b815-43f587e4f175",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbaX5QgYZrzowAYUWPP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "40530764-f845-4a4b-9939-06d5e0717fd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Qa24MqTT1hP1jfs1t1fmdy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 15199,
      "cache_read_input_tokens": 25395,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15199
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 438,
          "cache_read_input_tokens": 25395,
          "cache_creation_input_tokens": 15199,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15199,
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

_source line 17 · 2026-05-19T08:17:01.995Z_

<details><summary>↩ Tool result · `toolu_013frisFnRrVaPXEsr7Twkus`</summary>

```text
Found 2 files
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40530764-f845-4a4b-9939-06d5e0717fd8",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "80ee5b05-b766-4cb5-8a5f-0dcbea55e3d7",
  "sourceToolAssistantUUID": "40530764-f845-4a4b-9939-06d5e0717fd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-19T08:17:03.818Z_

Now let me search for the remaining key numbers with more context to find exact locations and verify consistency:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80ee5b05-b766-4cb5-8a5f-0dcbea55e3d7",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbappkywDTdrCbQerPf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b2957b74-0e87-42d4-abfa-7f38f2e32b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JsottFjHRHwNRfcHvBkstK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 40594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 797,
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

_source line 19 · 2026-05-19T08:17:04.474Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01H6WCL8odZm3eKpnwsnoLWs`</summary>

```json
{
  "pattern": "51\\.22|48\\.66.*51\\.22|surpass",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2957b74-0e87-42d4-abfa-7f38f2e32b17",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbappkywDTdrCbQerPf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "72ec1e50-4b56-4c64-82ba-b8c283ffec64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JsottFjHRHwNRfcHvBkstK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 40594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 797,
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

_source line 20 · 2026-05-19T08:17:04.493Z_

<details><summary>↩ Tool result · `toolu_01H6WCL8odZm3eKpnwsnoLWs`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex-12-Recent work has recast DocRE for large language models.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex-13-AutoRE \citep{autore2024} fine-tunes LLMs with QLoRA using a relation-head-facts decomposition; \citet{xu2024lmrc} frame extraction as multi-choice reading comprehension; RelPrior \citep{wang2025relprior} uses relation priors to guide LLM-based extraction; GLiDRE \citep{zhang2025glidre} presents a generalist lightweight approach; Ru-LLM \citep{wang2025rullm} incorporates logical rule constraints; and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex:14:These methods match or surpass encoder baselines but produce bare triplets without evidence.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex-15-The critical distinction lies in computational nature: in SAIS and DREEAM, evidence retrieval is classification that regularizes the encoder without increasing output length; in LLM-based DocRE, evidence requires additional output tokens per triple, imposing costs that depend on model capacity and optimization strategy.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex-16-Whether this cost is inevitable or can be mitigated is the central question of our work.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-93-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-94-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:95:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-96-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-97-\begin{table}[t]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-105-\textbf{Model} & \textbf{SFT w/ evi} & \textbf{No-evi} & \textbf{RSFT} & \textbf{Evi Tax} & \textbf{RSFT Gain} \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-106-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:107:Qwen3-1.7B & 47.86 & 39.82 & 51.22 & +8.04 & +3.36 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-108-Qwen3-4B & 43.58{\scriptsize$\pm$3.80} & 47.21 & 44.82{\scriptsize$\pm$0.51} & $-$3.63 & +1.24 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-109-Qwen3-8B & 48.66{\scriptsize$\pm$2.62} & 50.79 & 54.14{\scriptsize$\pm$0.53} & $-$2.13 & +5.48 \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex-2-\label{sec:conclusion}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex:4:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-3-Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-4-Recent LLM-based approaches have closed this gap: \citet{autore2024} fine-tune LLMs with structured decomposition for end-to-end extraction, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex:5:These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-6-Yet every one of them outputs bare relation triplets $(e_h, r, e_t)$ without any indication of \emph{which sentences} in the document support each prediction.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-7-In deployment contexts where predictions feed into clinical knowledge bases, legal due-diligence pipelines, or financial compliance systems, end users cannot verify a prediction without manually locating its textual basis across a multi-page document.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-43-    \item We identify a \textbf{scale-dependent evidence tax}: the cost of joint evidence production varies across 1.7B, 4B, and 8B parameters, challenging the assumption that evidence generation uniformly degrades extraction quality.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-44-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex:45:    \item We establish \textbf{RSFT with NLI-based scoring} as an effective solution, using CED or flat-NLI to select high-quality training data. RSFT achieves +4.92pp Ign-F1 over SFT at 4B scale (four-seed mean), and our 1.7B RSFT model (51.22 Ign-F1) surpasses 8B SFT performance (50.51), enabling deployment-efficient evidence-grounded extraction at reduced computational cost.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-46-\end{enumerate}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-12-First, RL optimization pressure correlates with evidence-extraction decoupling severity: GRPO causes catastrophic decoupling, DPO shows gradual degradation, and RSFT preserves stable joint performance.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-13-Second, the cost of evidence production varies across model scales: at 1.7B parameters evidence provides a +6.2pp Ign-F1 benefit on a controlled evaluation subset excluding truncated and repetitive outputs, at 4B it imposes a $-$7.5pp penalty, and at 8B the cost approaches zero.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex:14:Third, RSFT with NLI-based scoring is the most effective route: it achieves +4.92pp Ign-F1 over supervised fine-tuning at 4B scale (four-seed mean), and our 1.7B RSFT model (51.22 Ign-F1) surpasses 8B SFT performance (50.51).
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-15-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-16-\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72ec1e50-4b56-4c64-82ba-b8c283ffec64",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "079b0549-f610-4f08-8bfd-273336cce077",
  "sourceToolAssistantUUID": "72ec1e50-4b56-4c64-82ba-b8c283ffec64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T08:17:05.110Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011p89HFYMY2MEEegiUQkmzp`</summary>

```json
{
  "pattern": "44\\.39|79\\.61|0\\.6797",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "079b0549-f610-4f08-8bfd-273336cce077",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbappkywDTdrCbQerPf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9cf89759-7228-43c9-a4cc-f840cecddf86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JsottFjHRHwNRfcHvBkstK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 40594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 797,
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

_source line 22 · 2026-05-19T08:17:05.135Z_

<details><summary>↩ Tool result · `toolu_011p89HFYMY2MEEegiUQkmzp`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-21-\label{sec:main_results}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-22-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:23:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-24-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-25-The remaining gap to the no-evidence upper bound (2.39 points) represents the residual cost of producing structured evidence, a cost that shrinks at larger scales as we show in Section~\ref{sec:scaling}.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-35-\textbf{Method} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-36-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:37:SFT baseline & 43.58{\scriptsize$\pm$3.80} & 44.39 & 79.61 & 0.6797 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-38-SFT no-evidence & \textbf{47.21} & \textbf{48.76} & -- & -- \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-39-RSFT CED & \underline{44.82{\scriptsize$\pm$0.51}} & \underline{45.80} & 80.96 & 0.6487 \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-53-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-54-\paragraph{GRPO bf16: mild, variable.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:55:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-56-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-57-\paragraph{DPO: gradual decay.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-76-DPO & bf16 3ep$^\dagger$ & 34.29 & 84.03 & 0.7294 & Gradual \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-77-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:78:SFT & baseline$^\ddagger$ & 44.39 & 79.61 & 0.6797 & None \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-79-RSFT & CED$^\ddagger$ & 45.80 & 80.96 & 0.6487 & None \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-80-\bottomrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-81-\label{sec:scaling_details}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-82-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:83:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-84-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-85-\begin{table}[t]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-94-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-95-Qwen3-1.7B & 49.45 & 83.16 & 52.90 & 82.43 & 0.6224 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:96:Qwen3-4B & 44.39 & 79.61 & 45.80 & 80.96 & 0.6487 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-97-Qwen3-8B & 50.52 & 82.75 & 56.10 & 81.52 & 0.6198 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-98-LLaMA-3.1-8B & 55.14 & 81.51 & 58.39 & 82.43 & 0.5799 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cf89759-7228-43c9-a4cc-f840cecddf86",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "ac90fd66-783b-4688-b9bf-6dfa6498d6cb",
  "sourceToolAssistantUUID": "9cf89759-7228-43c9-a4cc-f840cecddf86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T08:17:05.550Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01EELYxNehXyrqn1QkRrjkxj`</summary>

```json
{
  "pattern": "45\\.80|80\\.96|0\\.6487",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac90fd66-783b-4688-b9bf-6dfa6498d6cb",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbappkywDTdrCbQerPf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2f91c121-0d64-4e9d-98fc-79ed121ff71c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JsottFjHRHwNRfcHvBkstK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 40594,
      "output_tokens": 433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 797
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 433,
          "cache_read_input_tokens": 40594,
          "cache_creation_input_tokens": 797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 797,
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

_source line 24 · 2026-05-19T08:17:05.566Z_

<details><summary>↩ Tool result · `toolu_01EELYxNehXyrqn1QkRrjkxj`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-21-\label{sec:main_results}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-22-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:23:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-24-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-25-The remaining gap to the no-evidence upper bound (2.39 points) represents the residual cost of producing structured evidence, a cost that shrinks at larger scales as we show in Section~\ref{sec:scaling}.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-37-SFT baseline & 43.58{\scriptsize$\pm$3.80} & 44.39 & 79.61 & 0.6797 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-38-SFT no-evidence & \textbf{47.21} & \textbf{48.76} & -- & -- \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:39:RSFT CED & \underline{44.82{\scriptsize$\pm$0.51}} & \underline{45.80} & 80.96 & 0.6487 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-40-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-41-\end{tabular}%
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-59-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-60-\paragraph{RSFT: no decoupling.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:61:RSFT avoids the decoupling problem entirely. By selecting high-quality complete outputs (jointly good extraction and evidence) rather than applying gradient-based reward maximization, RSFT maintains both capabilities simultaneously (mean Rel-F1 45.80, Evi-F1 80.96, EDCR 0.6487). The key insight is that rejection sampling operates on discrete outputs rather than differentiable reward signals, so it cannot exploit the extraction-evidence trade-off that gradient methods find.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-62-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-63-\begin{table}[t]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-77-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-78-SFT & baseline$^\ddagger$ & 44.39 & 79.61 & 0.6797 & None \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:79:RSFT & CED$^\ddagger$ & 45.80 & 80.96 & 0.6487 & None \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-80-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-81-\end{tabular}%
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-81-\label{sec:scaling_details}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-82-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:83:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-84-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-85-\begin{table}[t]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-94-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-95-Qwen3-1.7B & 49.45 & 83.16 & 52.90 & 82.43 & 0.6224 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:96:Qwen3-4B & 44.39 & 79.61 & 45.80 & 80.96 & 0.6487 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-97-Qwen3-8B & 50.52 & 82.75 & 56.10 & 81.52 & 0.6198 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-98-LLaMA-3.1-8B & 55.14 & 81.51 & 58.39 & 82.43 & 0.5799 \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-184-DREEAM & Encoder & 61.71 & 63.49 & 54.15 & -- \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-185-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:186:Ours (4B RSFT) & LLM & 44.82 & 45.80 & 36.1 & 80.96 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-187-Ours (8B RSFT) & LLM & 54.14 & 56.10 & -- & 81.52 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-188-\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f91c121-0d64-4e9d-98fc-79ed121ff71c",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "64f672d5-513f-4c2e-9104-f60dde5487c5",
  "sourceToolAssistantUUID": "2f91c121-0d64-4e9d-98fc-79ed121ff71c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-19T08:17:07.561Z_

Now let me search for some specific inconsistencies - the 50.51 vs 48.66 issue and verify other old numbers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64f672d5-513f-4c2e-9104-f60dde5487c5",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbb6Ajm2ZcyjzbNzDaY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a587411b-fa7b-4c02-bcd0-5b58e59fb4b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UiNHPoxabK2vwi1Y1XdZrc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7053,
      "cache_read_input_tokens": 41391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7053,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T08:17:08.198Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01UQ8k9zyZgrhnHxRFX6pZ1k`</summary>

```json
{
  "pattern": "50\\.51|50\\.52",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a587411b-fa7b-4c02-bcd0-5b58e59fb4b0",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbb6Ajm2ZcyjzbNzDaY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3d05791f-1b3a-46e7-8edd-bb30290df569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UiNHPoxabK2vwi1Y1XdZrc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7053,
      "cache_read_input_tokens": 41391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7053,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T08:17:08.212Z_

<details><summary>↩ Tool result · `toolu_01UQ8k9zyZgrhnHxRFX6pZ1k`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex-1-\section{Conclusion}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex-2-\label{sec:conclusion}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex:4:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-11-Three findings emerge.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-12-First, RL optimization pressure correlates with evidence-extraction decoupling severity: GRPO causes catastrophic decoupling, DPO shows gradual degradation, and RSFT preserves stable joint performance.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-13-Second, the cost of evidence production varies across model scales: at 1.7B parameters evidence provides a +6.2pp Ign-F1 benefit on a controlled evaluation subset excluding truncated and repetitive outputs, at 4B it imposes a $-$7.5pp penalty, and at 8B the cost approaches zero.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex:14:Third, RSFT with NLI-based scoring is the most effective route: it achieves +4.92pp Ign-F1 over supervised fine-tuning at 4B scale (four-seed mean), and our 1.7B RSFT model (51.22 Ign-F1) surpasses 8B SFT performance (50.51).
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-15-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-16-\end{abstract}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-80-\section{Scaling Details}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-81-\label{sec:scaling_details}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-82-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:83:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-84-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-85-\begin{table}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-86-\centering
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-94-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-95-Qwen3-1.7B & 49.45 & 83.16 & 52.90 & 82.43 & 0.6224 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-96-Qwen3-4B & 44.39 & 79.61 & 45.80 & 80.96 & 0.6487 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:97:Qwen3-8B & 50.52 & 82.75 & 56.10 & 81.52 & 0.6198 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-98-LLaMA-3.1-8B & 55.14 & 81.51 & 58.39 & 82.43 & 0.5799 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-99-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-100-\end{tabular}%
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-42-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-43-    \item We identify a \textbf{scale-dependent evidence tax}: the cost of joint evidence production varies across 1.7B, 4B, and 8B parameters, challenging the assumption that evidence generation uniformly degrades extraction quality.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-44-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex:45:    \item We establish \textbf{RSFT with NLI-based scoring} as an effective solution, using CED or flat-NLI to select high-quality training data. RSFT achieves +4.92pp Ign-F1 over SFT at 4B scale (four-seed mean), and our 1.7B RSFT model (51.22 Ign-F1) surpasses 8B SFT performance (50.51), enabling deployment-efficient evidence-grounded extraction at reduced computational cost.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-46-\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d05791f-1b3a-46e7-8edd-bb30290df569",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "aecaddb9-6ad0-47b5-b156-efe5ffc4c1d5",
  "sourceToolAssistantUUID": "3d05791f-1b3a-46e7-8edd-bb30290df569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T08:17:08.883Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01RC7KMvLWec4ZdMDHduYswt`</summary>

```json
{
  "pattern": "39\\.74|40\\.49|7\\.47|4\\.92|54\\.24|0\\.6982|0\\.6503",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aecaddb9-6ad0-47b5-b156-efe5ffc4c1d5",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbb6Ajm2ZcyjzbNzDaY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ce82997f-5a05-4f2f-9338-a9c5909249a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UiNHPoxabK2vwi1Y1XdZrc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7053,
      "cache_read_input_tokens": 41391,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7053
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 322,
          "cache_read_input_tokens": 41391,
          "cache_creation_input_tokens": 7053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7053,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T08:17:08.906Z_

<details><summary>↩ Tool result · `toolu_01RC7KMvLWec4ZdMDHduYswt`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-124-\label{sec:generalization}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-125-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:126:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex-2-\label{sec:conclusion}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex:4:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex-62-The intuition is as follows. A model that correctly identifies a few triples and provides excellent evidence for them, but misses most triples entirely, will have high $\text{Evi-Recall}_{\text{TP}}$ and low $\text{Rel-Recall}$, yielding a high EDCR. This pattern signals that evidence quality has decoupled from extraction capability: the model produces faithful evidence only within a narrow comfort zone.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex-63-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex:64:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-12-First, RL optimization pressure correlates with evidence-extraction decoupling severity: GRPO causes catastrophic decoupling, DPO shows gradual degradation, and RSFT preserves stable joint performance.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-13-Second, the cost of evidence production varies across model scales: at 1.7B parameters evidence provides a +6.2pp Ign-F1 benefit on a controlled evaluation subset excluding truncated and repetitive outputs, at 4B it imposes a $-$7.5pp penalty, and at 8B the cost approaches zero.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex:14:Third, RSFT with NLI-based scoring is the most effective route: it achieves +4.92pp Ign-F1 over supervised fine-tuning at 4B scale (four-seed mean), and our 1.7B RSFT model (51.22 Ign-F1) surpasses 8B SFT performance (50.51).
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-15-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex-16-\end{abstract}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-40-\label{sec:ablation_full}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-41-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:42:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-43-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-44-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-56-\textbf{Configuration} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-57-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:58:SFT baseline (s42) & 39.74 & 40.49 & 79.86 & 0.6982 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-59-SFT no-evidence & \textbf{47.21} & 48.76 & -- & -- \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-60-\midrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-65-RSFT CED $k{=}1$ (s44) & 45.11 & 46.21 & 80.50 & 0.6350 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-66-RSFT CED $k{=}1$ (s45) & 44.16 & 45.14 & 81.74 & 0.6550 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:67:RSFT CED $k{=}1$ (mean) & 44.66 & 45.63 & 81.15 & 0.6503 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-68-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-69-RSFT CED $k{=}3$ & 43.64 & 44.54 & 80.88 & 0.6635 \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-164-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-165-\paragraph{Cross-dataset robustness.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:166:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-167-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-168-\paragraph{Comparison to supervised methods.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-43-    \item We identify a \textbf{scale-dependent evidence tax}: the cost of joint evidence production varies across 1.7B, 4B, and 8B parameters, challenging the assumption that evidence generation uniformly degrades extraction quality.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-44-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex:45:    \item We establish \textbf{RSFT with NLI-based scoring} as an effective solution, using CED or flat-NLI to select high-quality training data. RSFT achieves +4.92pp Ign-F1 over SFT at 4B scale (four-seed mean), and our 1.7B RSFT model (51.22 Ign-F1) surpasses 8B SFT performance (50.51), enabling deployment-efficient evidence-grounded extraction at reduced computational cost.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-46-\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce82997f-5a05-4f2f-9338-a9c5909249a9",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "d3d63ec8-2c0a-42bf-a094-ba0199787145",
  "sourceToolAssistantUUID": "ce82997f-5a05-4f2f-9338-a9c5909249a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-19T08:17:11.950Z_

Perfect! I've found the key mismatch. Let me verify the exact issue in the abstract and introduction:

The abstract and introduction both say "surpasses 8B SFT performance (50.51)" but Table 3 (in appendix.tex, the cross_detail table) shows "Qwen3-8B & 50.52" for SFT Rel-F1. However, this is Rel-F1, not Ign-F1. Let me verify what metric is being compared in the main scaling table:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3d63ec8-2c0a-42bf-a094-ba0199787145",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbbLir2Utu4VeDao7AH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d84164d-4ee7-458e-b32c-6522238945aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WKfgcpYPQfjGDbtn463hPX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 11764,
      "cache_read_input_tokens": 41391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11764,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T08:17:12.923Z_

<details open><summary>🔧 Tool call — Grep · `toolu_012mhQmuff59UTQtsR7mKxWV`</summary>

```json
{
  "pattern": "evidence tax|RSFT gain.*8B.*5\\.48|-2\\.13",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections",
  "output_mode": "content",
  "context": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d84164d-4ee7-458e-b32c-6522238945aa",
  "isSidechain": true,
  "agentId": "abecba583dd61bae9",
  "requestId": "req_011CbBbbLir2Utu4VeDao7AH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d80d4209-efff-4fdf-891d-3d8f42faa67b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WKfgcpYPQfjGDbtn463hPX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 11764,
      "cache_read_input_tokens": 41391,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11764
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 276,
          "cache_read_input_tokens": 41391,
          "cache_creation_input_tokens": 11764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11764,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T08:17:12.941Z_

<details><summary>↩ Tool result · `toolu_012mhQmuff59UTQtsR7mKxWV`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-19-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-20-\subsection{Main Results}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-21-\label{sec:main_results}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-22-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:23:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-24-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-25-The remaining gap to the no-evidence upper bound (2.39 points) represents the residual cost of producing structured evidence, a cost that shrinks at larger scales as we show in Section~\ref{sec:scaling}.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-26-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-27-\begin{table}[t]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-87-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-88-\subsection{Scale-Dependent Evidence Tax}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-89-\label{sec:scaling}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-90-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:91:The evidence tax, defined as the Ign-F1 difference between no-evidence and joint-evidence SFT, varies across model scales. Table~\ref{tab:scaling} presents this analysis across four models (Figure~\ref{fig:scaling} in Appendix).
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-92-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:93:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-94-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-95-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-96-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-97-\begin{table}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-98-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:99:\caption{Scale-dependent evidence tax and RSFT gain. Evidence tax = SFT with evidence minus SFT no-evidence (positive means evidence helps). All results on DocRED dev set Ign-F1. Multi-seed mean $\pm$ std reported where available (4B: 3-seed, 8B: 2-seed).}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-100-\label{tab:scaling}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-101-\small
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-102-\resizebox{\columnwidth}{!}{%
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-103-\begin{tabular}{lccccc}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-116-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-117-\subsection{Evidence Strategy Comparison}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-118-\label{sec:evidence_strategy}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-119-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:120:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-121-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-122-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-123-\subsection{Generalization}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-124-\label{sec:generalization}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex-125-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:126:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex-11-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex-12-\subsection{Supervised Fine-Tuning Baseline}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex-13-\label{sec:sft}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex-14-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex:15:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex-16-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex-17-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex-18-\subsection{Optimization Paradigms}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex-19-\label{sec:paradigms}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-1-\section{Limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-2-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-3-All results use the DocRED development set; test set submission is pending. Exact-match F1 penalizes surface-form-different entity mentions~\citep{wan2024genres}, likely underestimating absolute extraction capability, though relative comparisons remain valid.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-4-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-6-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-7-\section{Ethics Statement}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-8-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-9-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-16-\paragraph{B. Did you discuss any potential risks of your work?}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-17-Yes. The Ethics Statement discusses data sources, absence of human subjects, and the intended use for improving verifiability in high-stakes domains.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-18-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-19-\paragraph{C. Do the abstract and introduction summarize the paper's main claims?}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex:20:Yes. The abstract states three findings (decoupling spectrum, scale-dependent evidence tax, RSFT effectiveness) with supporting numbers. The introduction provides detailed motivation, findings, and a contribution list.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-21-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-22-\paragraph{D1. Did you include the code, data, and instructions needed to reproduce the main experimental results?}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-23-We will release training and evaluation code upon publication. All experiments use publicly available datasets (DocRED, Re-DocRED) and base models (Qwen3, LLaMA-3.1) accessible through standard channels.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex-24-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-104-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-105-\section{Controlled Evaluation Subset}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-106-\label{sec:fair_subset}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-107-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:108:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-109-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:110:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-111-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-112-\begin{table}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-113-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-114-\caption{Mechanistic breakdown of output quality across scales. Duplication rate: fraction of documents with degenerate outputs. Truncation $\Delta$: no-evidence rate minus with-evidence rate (positive means no-evidence truncates more).}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-150-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-151-\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-152-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-153-\includegraphics[width=\columnwidth]{fig_scaling.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:154:\caption{Evidence tax across model scales. Bar heights show Ign-F1 for each training configuration. The gap between no-evidence and SFT bars reverses direction between 1.7B and 4B, revealing the scale-dependent nature of the evidence tax. RSFT consistently narrows the gap toward the no-evidence upper bound.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-155-\label{fig:scaling}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-156-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-157-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-158-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-159-\section{Full Generalization Results}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-160-\label{sec:generalization_full}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-161-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-162-\paragraph{Cross-family transfer.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:163:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-164-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-165-\paragraph{Cross-dataset robustness.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-166-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex-167-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-27-Our experiments across 85+ configurations, spanning four model scales (1.7B to 8B), two model families, and two datasets, reveal three principal findings.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-28-\textbf{First}, we identify a \emph{decoupling spectrum}: the strength of RL optimization pressure correlates with the severity of evidence-extraction decoupling.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-29-GRPO with Quantized Low-Rank Adaptation (QLoRA; \citealt{hu2022lora}) produces catastrophic decoupling where extraction accuracy collapses to near zero; GRPO with full-precision training shows mild decoupling; DPO exhibits gradual degradation; and RSFT maintains stable joint performance.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-30-Catastrophic extraction collapse co-occurs with QLoRA-based GRPO training, though we note that GRPO with full-precision training (bf16, $G{=}8$) achieves EDCR below the SFT baseline, indicating that the decoupling is not inherent to online RL when sufficient precision is available.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex:31:\textbf{Second}, we discover a \emph{scale-dependent evidence tax}: the cost of jointly producing evidence and relations varies across model scales.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-32-At 1.7B parameters, evidence generation provides an implicit regularization benefit of +6.2pp Ign-F1 on a controlled evaluation subset; at 4B, it imposes a $-$7.5pp penalty; at 8B, the tax approaches zero.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-33-This pattern challenges the assumption that evidence generation uniformly harms extraction.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-34-\textbf{Third}, RSFT with NLI-based scoring for training data selection emerges as the most effective optimization route.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-35-By selecting high-quality training samples through output filtering rather than applying gradient-based optimization pressure, RSFT sidesteps the multi-objective competition that destabilizes RL and preference methods.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-39-    \item We formalize \textbf{evidence-grounded document-level relation extraction} as a generation task for LLMs and conduct the first \textbf{comprehensive empirical study} spanning 85+ experiments across four model scales, two model families, two datasets (DocRED, Re-DocRED), and three optimization paradigms.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-40-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-41-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-42-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex:43:    \item We identify a \textbf{scale-dependent evidence tax}: the cost of joint evidence production varies across 1.7B, 4B, and 8B parameters, challenging the assumption that evidence generation uniformly degrades extraction quality.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-44-
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-45-    \item We establish \textbf{RSFT with NLI-based scoring} as an effective solution, using CED or flat-NLI to select high-quality training data. RSFT achieves +4.92pp Ign-F1 over SFT at 4B scale (four-seed mean), and our 1.7B RSFT model (51.22 Ign-F1) surpasses 8B SFT performance (50.51), enabling deployment-efficient evidence-grounded extraction at reduced computational cost.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex-46-\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d80d4209-efff-4fdf-891d-3d8f42faa67b",
  "isSidechain": true,
  "promptId": "d26718a4-01bf-4a67-8c10-e81493913ca8",
  "agentId": "abecba583dd61bae9",
  "type": "user",
  "uuid": "6b8756e4-fa71-41cc-b535-bef7224acca3",
  "sourceToolAssistantUUID": "d80d4209-efff-4fdf-891d-3d8f42faa67b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---
