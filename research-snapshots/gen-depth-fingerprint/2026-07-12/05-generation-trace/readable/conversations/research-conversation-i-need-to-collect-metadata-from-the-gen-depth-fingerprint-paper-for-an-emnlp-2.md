# Research conversation: I need to collect metadata from the gen-depth-fingerprint paper for an EMNLP 2026 OpenReview submission form. Read the f

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a4a6587a077516985.jsonl`
- **Structured JSON:** [`e8758a0d2dd8a23a8c1e.json`](../../sessions/e8/e8758a0d2dd8a23a8c1e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-26T03:40:32.519Z_

I need to collect metadata from the gen-depth-fingerprint paper for an EMNLP 2026 OpenReview submission form. Read the following files and extract the requested information:

1. `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex` — extract the \title{} content
2. `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex` — extract the full abstract text (plain English, no LaTeX commands)
3. `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex` — confirm it exists and note the section label
4. `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex` — confirm content
5. `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ai_assistants.tex` — confirm content and section label
6. `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex` — check what models/datasets are used, hyperparameters mentioned
7. `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex` — check for descriptive statistics, error bars, etc.

Also check if there's a `conclusion.tex` and `discussion.tex` in the same directory.

Report ALL the extracted text verbatim (especially title and abstract). Search breadth: medium

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9f0868a9-f721-4721-9bb7-3b609471c65b",
  "agentId": "a4a6587a077516985",
  "type": "user",
  "uuid": "87922154-2dc8-436a-aec9-aeb83528f5cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-26T03:40:35.138Z_

I'll help you extract metadata from the gen-depth-fingerprint paper. Let me read all the requested files systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87922154-2dc8-436a-aec9-aeb83528f5cc",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAMi2awQ96vmcKW26k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b77b7cc8-41bb-4475-ad37-b284dfae841d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011go97HoACPHFMmYutWZFuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39976,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39976,
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

_source line 3 · 2026-05-26T03:40:35.392Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XbC4s85bqaDobwA6Lqw546`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b77b7cc8-41bb-4475-ad37-b284dfae841d",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAMi2awQ96vmcKW26k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "53ab5309-e13f-4037-a44d-f70c7321ea22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011go97HoACPHFMmYutWZFuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39976,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39976,
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

_source line 4 · 2026-05-26T03:40:35.404Z_

<details><summary>↩ Tool result · `toolu_01XbC4s85bqaDobwA6Lqw546`</summary>

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
17	\usepackage{stfloats}
18	\usepackage{alphalph}
19	\usepackage{tcolorbox}
20	\tcbuselibrary{breakable}
21	
22	\graphicspath{{../chart/}}
23	
24	\title{Depth Profiling: Classifying Recursive Generation Depth\\in Base-Model LLM Text}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{results}
37	
38	\input{discussion}
39	\input{conclusion}
40	\input{limitations}
41	\input{ethics}
42	\bibliography{references}
43	
44	\appendix
45	\renewcommand{\thesection}{\alphalph{\value{section}}}
46	
47	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
48	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
49	
50	\input{appendix_dataset_stats}
51	
52	\section{Length Confound Analysis}
53	\label{app:length}
54	\input{appendix_length}
55	
56	\section{Prompt Type Generalization}
57	\label{app:prompt-type}
58	\input{appendix_prompt_type}
59	\FloatBarrier
60	
61	\section{Finer-Grained Depth Classification}
62	\label{app:finer-depth}
63	\input{appendix_finer_depth}
64	\FloatBarrier
65	
66	\section{End-to-End Depth Classification (QLoRA)}
67	\label{app:qlora}
68	\input{appendix_qlora}
69	\FloatBarrier
70	
71	\section{Leave-One-Feature-Out Analysis}
72	\label{app:lofo}
73	\input{appendix_lofo}
74	\FloatBarrier
75	
76	\subsection{Candidate Feature Screening}
77	\label{app:feature-candidate}
78	\input{appendix_feature_candidates}
79	\FloatBarrier
80	
81	\section{Confusion Matrix}
82	\label{app:confusion}
83	\input{appendix_confusion_matrix}
84	\FloatBarrier
85	
86	\section{Classifier Sensitivity}
87	\label{app:classifier}
88	\input{appendix_classifier}
89	\FloatBarrier
90	
91	\section{Robustness to Text Perturbation}
92	\label{app:human-edit}
93	\input{appendix_human_edit}
94	\FloatBarrier
95	
96	\section{Cross-Domain Generalization}
97	\label{app:domain}
98	\input{appendix_domain}
99	\FloatBarrier
100	
101	\section{Instruction-Tuned Model Analysis}
102	\label{app:instruct}
103	\input{appendix_instruct}
104	
105	\section{Error Analysis of Binary Classification}
106	\label{app:error-analysis}
107	\input{appendix_error_analysis}
108	\FloatBarrier
109	
110	
111	\section{Downstream Utility}
112	\label{app:downstream}
113	\input{appendix_downstream}
114	\FloatBarrier
115	
116	\section{Cross-Model Chain Per-Class Detail}
117	\label{app:cross-model-detail}
118	\input{appendix_cross_model_detail}
119	\FloatBarrier
120	
121	\section{Feature Distribution Analysis}
122	\label{app:feature-distributions}
123	\input{appendix_feature_distributions}
124	
125	\section{Cross-Temperature Transfer}
126	\label{app:cross-temp}
127	\input{appendix_cross_temp}
128	
129	\section{Feature Ablation}
130	\label{app:ablation-table}
131	\input{appendix_ablation}
132	
133	\input{appendix_feature_correlation}
134	
135	\section{Cross-Family Reference Models}
136	\label{app:cross-ref}
137	\input{table4}
138	
139	\input{appendix_seed_control}
140	
141	\input{appendix_tost}
142	
143	\input{appendix_tost_bootstrap}
144	
145	\section{DDR Partition Validation}
146	\label{app:ddr-validation}
147	\input{appendix_ddr_validation}
148	
149	\section{Generator Subset Summary}
150	\label{app:gen-subsets-section}
151	\input{appendix_generator_subsets}
152	
153	\input{appendix_qualitative_examples}
154	
155	\section{Cross-Generator Transfer Analysis}
156	\label{app:transfer}
157	\input{appendix_transfer}
158	
159	\vspace{-2mm}
160	\section{Supplementary DDR Characterization}
161	\label{app:ddr-supplement}
162	\vspace{-2mm}
163	
164	\subsection{Partition Stability Across Temperatures}
165	\label{app:ddr-temp-stability}
166	\input{appendix_temperature_stability}
167	
168	\subsection{Per-Family DDR Consistency}
169	\label{app:family-ddr}
170	\input{per_family_ddr_table}
171	\FloatBarrier
172	
173	\subsection{Per-Feature Convergence Dynamics}
174	\label{app:convergence}
175	\input{appendix_convergence}
176	
177	\subsection{DDR Causality Analysis}
178	\label{app:ddr-causality}
179	\input{appendix_ddr_causality}
180	
181	\input{appendix_variance_decomposition}
182	
183	\subsection{Decoding Strategy Robustness}
184	\label{app:decoding-strategy}
185	\input{appendix_decoding_strategy}
186	\FloatBarrier
187	
188	\input{appendix_9gen_scale}
189	
190	\subsection{Comparison with Concurrent Iterative-Generation Studies}
191	\label{app:iterative-comparison}
192	\input{appendix_iterative_comparison}
193	
194	\subsection{Token-Level NLL Distribution}
195	\label{app:nll-distribution}
196	\input{appendix_nll_distribution}
197	\FloatBarrier
198	
199	\section{Use of AI Assistants}
200	\label{app:ai-assistants}
201	\input{appendix_ai_assistants}
202	
203	\end{document}
204	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53ab5309-e13f-4037-a44d-f70c7321ea22",
  "isSidechain": true,
  "promptId": "9f0868a9-f721-4721-9bb7-3b609471c65b",
  "agentId": "a4a6587a077516985",
  "type": "user",
  "uuid": "74691820-5054-4276-93c9-9c65d6482c38",
  "sourceToolAssistantUUID": "53ab5309-e13f-4037-a44d-f70c7321ea22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T03:40:35.588Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XwHb1REVKP3Mxz71fLyHoL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74691820-5054-4276-93c9-9c65d6482c38",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAMi2awQ96vmcKW26k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7ff1e3ee-3ae4-470d-922b-d826e12129b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011go97HoACPHFMmYutWZFuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39976,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39976,
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

_source line 6 · 2026-05-26T03:40:35.600Z_

<details><summary>↩ Tool result · `toolu_01XwHb1REVKP3Mxz71fLyHoL`</summary>

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
  "parentUuid": "7ff1e3ee-3ae4-470d-922b-d826e12129b1",
  "isSidechain": true,
  "promptId": "9f0868a9-f721-4721-9bb7-3b609471c65b",
  "agentId": "a4a6587a077516985",
  "type": "user",
  "uuid": "77aa5fbf-8861-4dad-b127-e16517f0d256",
  "sourceToolAssistantUUID": "7ff1e3ee-3ae4-470d-922b-d826e12129b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T03:40:35.780Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NVgzmU2to7dftRjXdgEvUo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77aa5fbf-8861-4dad-b127-e16517f0d256",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAMi2awQ96vmcKW26k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "14452ec0-4ef8-4189-bdab-814a10056455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011go97HoACPHFMmYutWZFuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39976,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39976,
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

_source line 8 · 2026-05-26T03:40:35.786Z_

<details><summary>↩ Tool result · `toolu_01NVgzmU2to7dftRjXdgEvUo`</summary>

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
  "parentUuid": "14452ec0-4ef8-4189-bdab-814a10056455",
  "isSidechain": true,
  "promptId": "9f0868a9-f721-4721-9bb7-3b609471c65b",
  "agentId": "a4a6587a077516985",
  "type": "user",
  "uuid": "035ff43e-76d8-4468-9d7d-6877a8545dfb",
  "sourceToolAssistantUUID": "14452ec0-4ef8-4189-bdab-814a10056455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T03:40:35.990Z_

<details open><summary>🔧 Tool call — Read · `toolu_015fQQzzKtpbzbaGbMjY8Bws`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "035ff43e-76d8-4468-9d7d-6877a8545dfb",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAMi2awQ96vmcKW26k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e8e0451c-0124-4f53-b792-8ed373fbfa06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011go97HoACPHFMmYutWZFuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39976,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39976,
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

_source line 10 · 2026-05-26T03:40:35.995Z_

<details><summary>↩ Tool result · `toolu_015fQQzzKtpbzbaGbMjY8Bws`</summary>

```text
1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	All code, data, and trained models will be released upon publication.
10	
11	\paragraph{Licenses.}
12	All generator models are publicly available under permissive licenses (Apache 2.0 for Pythia, OLMo, and Mistral; Qwen License for Qwen3; Llama Community License for Llama 3.2).
13	Wikipedia seed passages are distributed under CC BY-SA 3.0.
14	
15	\paragraph{Compute budget.}
16	All experiments were conducted on 4$\times$ NVIDIA RTX 5090 GPUs (32\,GB each), totaling approximately 62 GPU-hours.
17	
18	\paragraph{Software.}
19	Experiments used Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, and SciPy 1.17.1.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8e0451c-0124-4f53-b792-8ed373fbfa06",
  "isSidechain": true,
  "promptId": "9f0868a9-f721-4721-9bb7-3b609471c65b",
  "agentId": "a4a6587a077516985",
  "type": "user",
  "uuid": "379ca9ce-5029-4f04-b678-01e61cbbf17e",
  "sourceToolAssistantUUID": "e8e0451c-0124-4f53-b792-8ed373fbfa06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T03:40:36.630Z_

<details open><summary>🔧 Tool call — Read · `toolu_018CJV9Dn5EWivhjycX2vwnD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_ai_assistants.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "379ca9ce-5029-4f04-b678-01e61cbbf17e",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAMi2awQ96vmcKW26k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "65d4e1be-6f48-43a8-bb23-42ac589c312f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011go97HoACPHFMmYutWZFuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39976,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39976,
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

_source line 12 · 2026-05-26T03:40:36.636Z_

<details open><summary>🔧 Tool call — Read · `toolu_015QbCQor2kfJDYsk35gEoJw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65d4e1be-6f48-43a8-bb23-42ac589c312f",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAMi2awQ96vmcKW26k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "97aa971a-86d0-4151-b246-fc9468817a88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011go97HoACPHFMmYutWZFuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39976,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39976,
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

_source line 13 · 2026-05-26T03:40:36.645Z_

<details><summary>↩ Tool result · `toolu_018CJV9Dn5EWivhjycX2vwnD`</summary>

```text
1	This paper was produced with the assistance of AI writing tools for drafting and editing.
2	All scientific claims, experimental designs, and analyses were conducted by the authors.
3	The authors take full responsibility for the content of this work.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65d4e1be-6f48-43a8-bb23-42ac589c312f",
  "isSidechain": true,
  "promptId": "9f0868a9-f721-4721-9bb7-3b609471c65b",
  "agentId": "a4a6587a077516985",
  "type": "user",
  "uuid": "24b705da-80f3-4a77-9713-1ac706f50eb7",
  "sourceToolAssistantUUID": "65d4e1be-6f48-43a8-bb23-42ac589c312f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T03:40:36.647Z_

<details><summary>↩ Tool result · `toolu_015QbCQor2kfJDYsk35gEoJw`</summary>

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
  "parentUuid": "97aa971a-86d0-4151-b246-fc9468817a88",
  "isSidechain": true,
  "promptId": "9f0868a9-f721-4721-9bb7-3b609471c65b",
  "agentId": "a4a6587a077516985",
  "type": "user",
  "uuid": "170778fd-be15-4d58-8ef6-2f132c899cb2",
  "sourceToolAssistantUUID": "97aa971a-86d0-4151-b246-fc9468817a88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T03:40:36.709Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NjuhjJYq2jMoJBUS4oGFLm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "170778fd-be15-4d58-8ef6-2f132c899cb2",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAMi2awQ96vmcKW26k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2531c882-3985-4ef6-b14f-177036007f8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011go97HoACPHFMmYutWZFuP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39976,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39976,
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

_source line 16 · 2026-05-26T03:40:36.715Z_

<details><summary>↩ Tool result · `toolu_01NjuhjJYq2jMoJBUS4oGFLm`</summary>

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
  "parentUuid": "2531c882-3985-4ef6-b14f-177036007f8f",
  "isSidechain": true,
  "promptId": "9f0868a9-f721-4721-9bb7-3b609471c65b",
  "agentId": "a4a6587a077516985",
  "type": "user",
  "uuid": "5f85b26d-e8f2-408c-b097-7a586cfe09b9",
  "sourceToolAssistantUUID": "2531c882-3985-4ef6-b14f-177036007f8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-26T03:40:39.027Z_

Now let me check for the conclusion and discussion files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f85b26d-e8f2-408c-b097-7a586cfe09b9",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAfWr6peexdJqRLLsg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9bb00bee-4758-46b6-ba83-6b349dccf602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UYJwd4ofvhe6bZTmB9eEPT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12856,
      "cache_read_input_tokens": 39976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12856,
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

_source line 18 · 2026-05-26T03:40:39.898Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LhQcLH2e4s7YTyVmUoChAM`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ | grep -E \"(conclusion|discussion)\\.tex\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bb00bee-4758-46b6-ba83-6b349dccf602",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAfWr6peexdJqRLLsg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c6a8123-6688-475c-b894-9c851d7a3884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UYJwd4ofvhe6bZTmB9eEPT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12856,
      "cache_read_input_tokens": 39976,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12856
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 113,
          "cache_read_input_tokens": 39976,
          "cache_creation_input_tokens": 12856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12856,
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

_source line 19 · 2026-05-26T03:40:40.070Z_

<details><summary>↩ Tool result · `toolu_01LhQcLH2e4s7YTyVmUoChAM`</summary>

```text
-rw-r--r--  1 ubuntu ubuntu     571 May 25 15:41 conclusion.tex
-rw-r--r--  1 ubuntu ubuntu    2804 May 25 15:41 discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c6a8123-6688-475c-b894-9c851d7a3884",
  "isSidechain": true,
  "promptId": "9f0868a9-f721-4721-9bb7-3b609471c65b",
  "agentId": "a4a6587a077516985",
  "type": "user",
  "uuid": "95aae874-956a-4176-9d49-4e87da99604b",
  "sourceToolAssistantUUID": "4c6a8123-6688-475c-b894-9c851d7a3884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-26T03:40:42.103Z_

Let me read those files and also verify other files exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95aae874-956a-4176-9d49-4e87da99604b",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAujrgAPkuLwjPiUZE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01c57cf3-cd64-46e7-8a18-20348d7e5cdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FHhY6gx1t41KKWfT7H3gug",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 52832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 286,
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

_source line 21 · 2026-05-26T03:40:42.321Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Kiup2mfcAUS16g2GkWSKuQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01c57cf3-cd64-46e7-8a18-20348d7e5cdd",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAujrgAPkuLwjPiUZE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9809adfe-0a41-4adb-b5bc-76237bb62e6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FHhY6gx1t41KKWfT7H3gug",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 52832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 286,
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

_source line 22 · 2026-05-26T03:40:42.329Z_

<details><summary>↩ Tool result · `toolu_01Kiup2mfcAUS16g2GkWSKuQ`</summary>

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
  "parentUuid": "9809adfe-0a41-4adb-b5bc-76237bb62e6a",
  "isSidechain": true,
  "promptId": "9f0868a9-f721-4721-9bb7-3b609471c65b",
  "agentId": "a4a6587a077516985",
  "type": "user",
  "uuid": "45b29f79-ece5-4edf-8113-4133d345a250",
  "sourceToolAssistantUUID": "9809adfe-0a41-4adb-b5bc-76237bb62e6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T03:40:42.475Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L28Ni3GW7BYwvUkxSf19Km`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45b29f79-ece5-4edf-8113-4133d345a250",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVAujrgAPkuLwjPiUZE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c98d26a2-0753-471a-a210-1c8be587994e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FHhY6gx1t41KKWfT7H3gug",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 52832,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 286
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 176,
          "cache_read_input_tokens": 52832,
          "cache_creation_input_tokens": 286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 286,
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

_source line 24 · 2026-05-26T03:40:42.486Z_

<details><summary>↩ Tool result · `toolu_01L28Ni3GW7BYwvUkxSf19Km`</summary>

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
  "parentUuid": "c98d26a2-0753-471a-a210-1c8be587994e",
  "isSidechain": true,
  "promptId": "9f0868a9-f721-4721-9bb7-3b609471c65b",
  "agentId": "a4a6587a077516985",
  "type": "user",
  "uuid": "67110316-c302-472d-bd12-1800beaad529",
  "sourceToolAssistantUUID": "c98d26a2-0753-471a-a210-1c8be587994e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-26T03:41:10.921Z_

Perfect! Now I have all the information requested. Let me compile the metadata extraction report.

## EMNLP 2026 OpenReview Submission Metadata Extraction

### 1. **Paper Title**
```
Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text
```

### 2. **Abstract (Plain Text, No LaTeX)**
As large language model (LLM) outputs re-enter training corpora and seed further generation, understanding how recursive generation reshapes text distributions is critical for data provenance and corpus curation. Existing detectors answer only the binary human-or-machine question, ignoring generation depth; we introduce depth profiling to address this gap.

We decompose distributional drift under recursive generation into location and shape components. Across eight base-model generators from five families, negative log-likelihood (NLL) location features drift monotonically with depth (effect size d=0.74–1.05) while three shape features remain near-stationary (d < 0.10), with entropy std intermediate (d=0.46). We term this ≥8× effect-size gap the differential depth response (DDR).

Prior work documents what converges; the central finding here is what is approximately preserved: shape stability complements location drift for ordinal depth grading without per-generator calibration. A lightweight ensemble achieves leak-free binary F1=0.694 (gen-1 vs. gen-2+) and 3-class F1=0.762 under 8-generator leave-one-generator-out evaluation; cross-model chains (5 generators) reach binary F1=0.830 (gen-0 seeds shared across generators; Section 2.2).

Instruction tuning compresses DDR and bounds current applicability to base models. Code and data are available at https://anonymous.4open.science/r/gen-depth-fingerprint-3FB3/.

### 3. **Limitations Section**
**File Status**: EXISTS
**Section Label**: `\label{sec:limitations}`

All eight generators are base (pretrained) models with ≤8.2B parameters; instruction-tuned variants show substantially degraded depth signal. The evaluation assumes English Wikipedia seeds, a fixed decoding regime (t=0.7, nucleus p=0.9), and an English-centric reference model (Pythia-410M). Depth resolution is bounded at three classes; finer-grained 5-class classification yields F1≈0.50. DDR signal strength is temperature-dependent; at τ=0.9, classification performance degrades substantially.

### 4. **Ethics Statement**
**File Status**: EXISTS
**Section Label**: `\label{sec:ethics}`

**Content Summary**:
- All texts analyzed are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data involved
- Method estimates generation depth, not author identity
- Privacy implications minimal
- Acknowledges potential misuse (suppressing machine-generated text)
- Encourages deployment in data governance pipelines for provenance transparency
- All code, data, and trained models will be released upon publication
- **Licenses**: Apache 2.0 (Pythia, OLMo, Mistral); Qwen License (Qwen3); Llama Community License (Llama 3.2); CC BY-SA 3.0 (Wikipedia)
- **Compute Budget**: 4× NVIDIA RTX 5090 GPUs (32GB each), ~62 GPU-hours total
- **Software**: Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, SciPy 1.17.1

### 5. **AI Assistants Appendix**
**File Status**: EXISTS
**Section Label**: `\label{app:ai-assistants}`

**Content**: "This paper was produced with the assistance of AI writing tools for drafting and editing. All scientific claims, experimental designs, and analyses were conducted by the authors. The authors take full responsibility for the content of this work."

### 6. **Method Section - Key Details**

**Models/Generators Used** (8 total, spanning 5 families):
- Pythia: 2.8B, 1B
- OLMo: OLMo-2-1B
- Qwen: Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base
- Llama: Llama-3.2-3B
- Mistral: Mistral-7B-v0.3

**Reference Model**: Pythia-410M (for NLL feature extraction)

**Dataset**: Approximately 1,000 seed passages from English Wikipedia

**Decoding Hyperparameters**:
- Temperature: τ=0.7
- Nucleus sampling: p=0.9
- Maximum length: 256 new tokens
- Final dataset: 37,058 texts across all depths

**Features Extracted** (7 total):
1. entropy_mean (NLL-based)
2. entropy_std (NLL-based)
3. entropy_max (NLL-based)
4. entropy_min (NLL-based)
5. tail_decay (NLL-based, slope ranks 100–1K)
6. ttr (surface feature, type-token ratio)
7. hapax_ratio (surface feature, proportion of hapax legomena)

**Classifier**: XGBoost (n_estimators=200, max_depth=6, learning_rate=0.1)

**Evaluation Protocol**:
- Leave-One-Generator-Out (LOGO) cross-validation
- Leave-One-Family-Out (LOFO) for family-level effects
- Primary metric: macro-averaged F1 over three depth classes
- Depth classes: gen-0 (human), gen-1 (first-gen LLM), gen-2+ (≥2 recursive generations)

### 7. **Results Section - Descriptive Statistics & Error Analysis**

**Primary Results**:
- 3-class LOGO F1: 0.762 (95% CI [0.758, 0.766], N=37,058)
- Leak-free binary F1 (gen-1 vs. gen-2+): 0.694 (CI [0.688, 0.700])
- Cross-model generalization (5-gen LOGO): binary F1=0.830 (CI [.818, .841])
- Per-generator binary F1 range: 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B)
- LOFO (family-level): 0.686

**Differential Depth Response (DDR) Quantification**:
- Drifting features effect size: Cohen's d=0.74–1.05
- Near-stationary features effect size: d<0.10
- Intermediate (entropy_std): d=0.46
- Spearman correlations: drifting |ρ|>0.60 vs. stationary |ρ|≤0.16

**Error Analysis**:
- Gen-1/gen-2+ boundary is primary failure point
- Depth-2 error rate: 48.4% (highest)
- Monotonic decrease at deeper generations: ≤20.3% at depth-4
- Error rates ≤29.2% at gen-3+

**Baseline Comparison**:
- 4-detector + surface ensemble: binary F1=0.708 (22.8 ms/text)
- 7-feature ensemble (ours): binary F1=0.705 (9.7 ms/text, 2.4× faster)
- Individual detectors: Avg-LogProb (0.673), FastDetectGPT (0.569), LD-Score (0.675), Binoculars (0.539)

**Confound Controls**:
- Length-matched subsampling: F1=0.724
- Independent-seed evaluation: F1=0.680
- Cross-temperature (τ=0.9): -9.3 to -26.0 pp binary F1 degradation

**Additional Findings**:
- End-to-end QLoRA: 3-class F1=0.905 (within-model 5-fold CV, +10.0 pp over interpretable features)
- QLoRA on instruction-tuned data: F1=0.89–0.91 (within-model)
- Cross-domain generalization: F1=0.74–0.75
- Cross-temperature transfer: DDR partition preserved across all tested temperatures
- Robustness to 10% random word replacement: -8 pp binary F1

### 8. **Discussion & Conclusion**

**Discussion File**: EXISTS (`\label{sec:discussion}`)
- Relates DDR to monotonic NLL compression under recursive generation
- Discusses relationship to model collapse (shape changes under retraining but not inference)
- Addresses temperature sensitivity limitations
- Explains error structure: gen-1→gen-2+ boundary difficulty due to diversity overlap
- Identifies use case: corpus contamination detection and synthetic data pipeline auditing
- Notes: depth-aware filtering does NOT improve perplexity, so DDR identifies provenance rather than fluency

**Conclusion File**: EXISTS (`\label{sec:conclusion}`)
- Recursive generation produces decomposable depth response
- Location features drift monotonically; shape features approximately preserved
- Cross-generator classification achievable (F1=0.694–0.762; 5-generator cross-model F1=0.830)
- Applicable to base models under moderate sampling temperatures (τ≤0.7)
- Instruction tuning compresses DDR; QLoRA recovery shows tractable extension

---

**Summary**: All requested files exist and contain the expected content. The paper is thoroughly documented with strong empirical results, comprehensive ablation studies, and transparent discussion of limitations. Ready for EMNLP 2026 submission.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67110316-c302-472d-bd12-1800beaad529",
  "isSidechain": true,
  "agentId": "a4a6587a077516985",
  "requestId": "req_011CbQVB64idrD5FjqmVi1Y8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aae64c56-9ce6-45d4-a9ed-1e61edd7234d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/director_98a1947f",
  "sessionId": "2753d30b-37d4-4038-8aa4-591d041c5cad",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PdPTs8Ca4rqiVEupgb2Rqc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1243,
      "cache_read_input_tokens": 53118,
      "output_tokens": 2410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1243
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2410,
          "cache_read_input_tokens": 53118,
          "cache_creation_input_tokens": 1243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1243,
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
