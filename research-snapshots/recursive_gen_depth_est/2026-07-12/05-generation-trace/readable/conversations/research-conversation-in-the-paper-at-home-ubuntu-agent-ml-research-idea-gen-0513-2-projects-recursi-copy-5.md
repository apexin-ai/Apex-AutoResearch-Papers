# Research conversation: In the paper at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/, check whet

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae8b81dc77b3d268d.jsonl`
- **Structured JSON:** [`e478bcf78d28d56d97e9.json`](../../sessions/e4/e478bcf78d28d56d97e9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-21T11:20:13.027Z_

In the paper at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/, check whether the 14B cross-reference result (44.1% accuracy, EDD=2) is properly supported in the appendix:
1. Read section_appendix.tex and find everything about "cross-reference" or "cross_reference" or "44.1" or "Pythia-1.4B" as reference model for 14B
2. Check if there's a dedicated table showing the cross-reference control results (not just self-reference)
3. Look at Table 17 and any other tables in the appendix related to 14B/Qwen2.5-14B

Report: Is there a table/section in the appendix that shows the 44.1% cross-reference result with per-strategy breakdown? Or is only self-reference (50.8%) shown?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "376d666a-6e0b-4a97-9538-83296d6e92e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T11:20:15.166Z_

I'll help you investigate whether the 14B cross-reference result is properly supported in the appendix. Let me start by exploring the paper directory and then examining the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "376d666a-6e0b-4a97-9538-83296d6e92e6",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdArW3QmQx8VvgoAHmz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "665f1508-b293-46a0-b735-dadc34447e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L9WU7bx61xqQXQz7CoqPdf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 638,
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

_source line 3 · 2026-05-21T11:20:15.393Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DdY3XaHkPgRddUmTKtWUCb`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "665f1508-b293-46a0-b735-dadc34447e54",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdArW3QmQx8VvgoAHmz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a67cee92-a600-4906-abac-ebc5da888304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L9WU7bx61xqQXQz7CoqPdf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 39102,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 638
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 136,
          "cache_read_input_tokens": 39102,
          "cache_creation_input_tokens": 638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 638,
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

_source line 4 · 2026-05-21T11:20:15.489Z_

<details><summary>↩ Tool result · `toolu_01DdY3XaHkPgRddUmTKtWUCb`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a67cee92-a600-4906-abac-ebc5da888304",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "604c4fc4-f937-4b84-9b26-b2e0d9509116",
  "sourceToolAssistantUUID": "a67cee92-a600-4906-abac-ebc5da888304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-21T11:20:17.554Z_

Now let me read the section_appendix.tex file and search for relevant content:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "604c4fc4-f937-4b84-9b26-b2e0d9509116",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdB2wqk6N5rgfxtYGLc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "24986da6-82f4-45fa-aa54-e41d3eeed2b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RoxWom8n8YN1bdVuj5nSyB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 39740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
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

_source line 6 · 2026-05-21T11:20:18.005Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KgdfZwxYmdp6yq6tfXbW5s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24986da6-82f4-45fa-aa54-e41d3eeed2b7",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdB2wqk6N5rgfxtYGLc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fad61388-2956-4bab-a216-193d8b1e7feb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RoxWom8n8YN1bdVuj5nSyB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 39740,
      "output_tokens": 111,
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
          "input_tokens": 5,
          "output_tokens": 111,
          "cache_read_input_tokens": 39740,
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

### Tool result

_source line 7 · 2026-05-21T11:20:18.457Z_

<details><summary>↩ Tool result · `toolu_01KgdfZwxYmdp6yq6tfXbW5s`</summary>

```text
1	\section{LoRA Fine-Tuning Protocol}
2	\label{app:lora_protocol}
3	
4	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
5	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
6	The HuggingFace Trainer default linear decay schedule is used with no warmup.
7	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
8	Cross-scale experiments (\S\ref{sec:gen:crossscale}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
14	\label{tab:lora_protocol}
15	\begin{tabular}{@{}ll@{}}
16	\toprule
17	Parameter & Value \\
18	\midrule
19	LoRA rank $r$ & 16 \\
20	LoRA alpha $\alpha$ & 32 \\
21	LoRA dropout & 0.05 \\
22	Bias & none \\
23	Epochs per depth & 3 \\
24	Learning rate & $2 \times 10^{-4}$ \\
25	LR schedule & linear decay (no warmup) \\
26	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
27	Max sequence length & 512 tokens \\
28	Precision & bfloat16 \\
29	Adapter init & from scratch (base model) \\
30	Seed & 42 (primary), 43 (replication) \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Additional Results}
36	\label{app:additional}
37	
38	\subsection{Top-$k$ Feature Trajectories}
39	\label{app:topk_trajectories}
40	
41	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
42	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
43	Concretely, the d0$\to$d1 drop in \texttt{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
44	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
45	
46	\subsection{Permutation Importance}
47	\label{app:permutation}
48	
49	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
50	The top-2 features are stable across measures: \texttt{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \texttt{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \texttt{p75\_ppl} displaces \texttt{var\_surprisal} to rank 3).
51	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
52	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
53	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical; the top features are therefore robust to the choice of importance measure at the aggregate level, though per-cell rankings exhibit model-dependent variation.
54	
55	\subsection{Feature Trajectories}
56	\label{app:feature_trajectories}
57	
58	\begin{figure}[h]
59	\centering
60	\includegraphics[width=\columnwidth]{figures/fig_feature_trajectory.pdf}
61	\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns) and strategy (line style). Top row: \texttt{p90\_ppl} (monotonically decreasing). Middle: \texttt{var\_surprisal} (decreasing). Bottom: \texttt{rep\_3gram} (increasing). Shaded bands: interquartile range. The $d{=}0 \to d{=}1$ gap exceeds all subsequent inter-depth gaps.}
62	\label{fig:feature_trajectory}
63	\end{figure}
64	
65	\subsection{Per-Class Recall}
66	\label{app:per_class}
67	
68	Table~\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).
69	Depth~0 recall exceeds 97\% uniformly.
70	Among generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.
71	
72	\begin{table}[h]
73	\centering
74	\small
75	\caption{Per-class recall (\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}
76	\label{tab:per_class_recall}
77	\begin{tabular}{@{}lcccc@{}}
78	\toprule
79	Cell & d0 & d1 & d2 & d3 \\
80	\midrule
81	Pythia, nuc.       & 99.3 & 81.9 & 59.2 & 74.4 \\
82	Pythia, $\tau$     & 99.2 & 79.9 & 56.0 & 72.1 \\
83	Pythia, top-$k$    & 98.7 & 71.6 & 44.2 & 60.9 \\
84	OLMo, nuc.         & 97.8 & 82.1 & 60.6 & 75.3 \\
85	OLMo, $\tau$       & 99.3 & 87.1 & 65.6 & 77.1 \\
86	OLMo, top-$k$      & 99.2 & 80.9 & 50.4 & 67.2 \\
87	GPT-2~XL, nuc.     & 98.5 & 87.4 & 72.8 & 78.5 \\
88	GPT-2~XL, $\tau$   & 99.0 & 91.1 & \textbf{73.0} & 80.5 \\
89	GPT-2~XL, top-$k$  & 98.7 & 81.3 & 54.8 & 68.4 \\
90	\bottomrule
91	\end{tabular}
92	\end{table}
93	
94	\subsection{DCOL Iteration Details}
95	\label{app:dcol_iterations}
96	
97	Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
98	DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
99	
100	\begin{table}[h]
101	\centering
102	\small
103	\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.7\%.}
104	\label{tab:dcol_iterations}
105	\resizebox{\columnwidth}{!}{%
106	\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}
107	\toprule
108	Ver. & Backbone & Config & Outcome \\
109	\midrule
110	v1 & DeBERTa & FT, m\_lr $10^{-3}$ & Embed.\ collapse (31.5\%) \\
111	v2 & DeBERTa & FT, m\_lr $10^{-4}$ & OOM \\
112	v3 & DeBERTa & FT, m\_lr $10^{-4}$ & Forgetting + OOM \\
113	v4 & DeBERTa & LoRA, m\_lr $10^{-3}$ & Embed.\ collapse \\
114	v5 & DeBERTa & LoRA, m\_lr $10^{-4}$ & NaN gradients \\
115	v6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\% ($-$13.7pp) \\
116	\bottomrule
117	\end{tabular}}
118	\end{table}
119	
120	\subsection{Zero-Shot LLM Prompt Template}
121	\label{app:zeroshot_prompt}
122	
123	Both DeepSeek V3.2 and Qwen2.5-7B-Instruct use identical prompting.
124	The system message defines recursive generation depth with per-depth descriptions (depth~0: human-written; depth~1--3: successive LLM generation cycles) and lists expected textual patterns at each depth (vocabulary richness, repetition, coherence).
125	The user message presents the passage (truncated to ${\approx}$384 words) and requests a JSON response containing an integer depth prediction (0--3), a confidence score, and a one-sentence reasoning.
126	No in-context examples are provided.
127	
128	\begin{quote}
129	\small
130	\textbf{System:} ``You are an expert at detecting AI-generated text and estimating its generation depth. `Recursive generation depth' refers to how many times a text has been through an LLM generation cycle: Depth~0: Original human-written text [\ldots] Depth~3: Text generated by an LLM given depth-2 text as input. Key patterns by depth: Depth~0 (human): Rich vocabulary [\ldots] Depth~3 (third-gen): Noticeable repetition, formulaic structure [\ldots]''
131	
132	\textbf{User:} ``Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3). TEXT: \{text\}. Respond with ONLY a JSON object: \{\texttt{"depth"}: $\langle$int 0--3$\rangle$, \texttt{"confidence"}: $\langle$float 0--1$\rangle$, \texttt{"reasoning"}: $\langle$str$\rangle$\}''
133	\end{quote}
134	
135	\subsection{Temperature Robustness}
136	\label{app:multi_tau}
137	
138	The cross-strategy results in \S\ref{sec:gen:crossstrategy} use a single temperature ($\tau{=}0.9$).
139	To test whether depth signal generalizes across temperatures, we repeat the classification pipeline at $\tau \in \{0.5, 0.7, 0.9, 1.1\}$ on Pythia-1.4B.
140	
141	\paragraph{Within-$\tau$ robustness.}
142	For $\tau \in [0.5, 0.9]$, d1-vs-d2 AUC exceeds 0.80 (peak 0.851 at $\tau{=}0.7$, comparable to nucleus $p{=}0.95$'s 0.861) and 4-class accuracy ranges from 75.4\% to 77.3\% (Table~\ref{tab:multi_tau_within}); the depth signal is therefore not an artifact of a single temperature.
143	The same top-5 features (\texttt{var\_surprisal}, \texttt{p90\_ppl}, \texttt{mean\_ppl}, \texttt{mean\_surprisal}, \texttt{p75\_ppl}) dominate across all $\tau$ values with only minor rank-order variation.
144	
145	\paragraph{Collapse at $\tau{=}1.1$: memorization as prerequisite.}
146	At $\tau{=}1.1$, 4-class accuracy drops to 57.2\% and d1v2 AUC falls to 0.528.
147	Training loss reveals the mechanism: at low temperature ($\tau{=}0.5$), fine-tuning loss decreases steeply across recursive depths ($2.27 \to 0.42 \to 0.16$), a sign of rapid memorization of the model's own output.
148	At $\tau{=}1.1$, loss remains nearly flat ($2.27 \to 1.91 \to 1.85$); high-entropy output resists memorization, so depth-dependent distributional shifts do not accumulate.
149	This establishes \emph{memorization as a prerequisite} for detectable depth signal: recursive depth is discriminable only when successive fine-tuning iterations progressively reshape the output distribution.
150	
151	\paragraph{Cross-$\tau$ non-transferability.}
152	Leave-one-$\tau$-out transfer yields mean accuracy of 46.7\% with mean d1v2 AUC of 0.319 (Table~\ref{tab:multi_tau_cross}), worse than cross-strategy transfer (59.1\%; \S\ref{sec:gen:crossstrategy}).
153	Holdout $\tau{=}0.5$ produces inverted d1v2 AUC (0.176); different temperatures therefore produce surprisal distributions with incompatible shapes.
154	This extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific; strategy-conditioned classifiers are therefore necessary.
155	
156	\paragraph{Ecological validity.}
157	On WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve $\geq$98.5\% d0 accuracy despite $+$621\% domain shift in mean perplexity, partly an easy case, as WikiText's higher perplexity places it farther from d1--d3 in feature space.
158	On noisier web-crawl data (5{,}000 C4 passages), FPR ranges from 4.7\% (OLMo) to 22.4\% (GPT-2~XL), concentrated in template/SEO content with high n-gram repetition (Table~\ref{tab:calibration}); deployment on heterogeneous web data requires model-specific calibration.
159	
160	\begin{table}[h]
161	\centering
162	\small
163	\caption{Within-$\tau$ 4-class classification (Pythia-1.4B, 5-fold CV). d$i$v$j$: pairwise AUC for depth $i$ vs.\ depth $j$.}
164	\label{tab:multi_tau_within}
165	\resizebox{\columnwidth}{!}{%
166	\begin{tabular}{@{}lcccc@{}}
167	\toprule
168	$\tau$ & 4-class acc (\%) & d1v2 AUC & d0v1 AUC & d2v3 AUC \\
169	\midrule
170	0.5 & 77.3 & 0.842 & 0.996 & 0.764 \\
171	0.7 & 75.4 & 0.851 & 0.997 & 0.720 \\
172	0.9 & 75.9 & 0.808 & 0.991 & 0.781 \\
173	1.1 & 57.2 & 0.528 & 0.988 & 0.599 \\
174	\bottomrule
175	\end{tabular}}
176	\end{table}
177	
178	\begin{table}[h]
179	\centering
180	\small
181	\caption{Cross-$\tau$ leave-one-out transfer (Pythia-1.4B). Train on three temperatures, test on the held-out one.}
182	\label{tab:multi_tau_cross}
183	\begin{tabular}{@{}lcc@{}}
184	\toprule
185	Holdout & Acc (\%) & d1v2 AUC \\
186	\midrule
187	$\tau{=}0.5$ & 52.2 & 0.176 \\
188	$\tau{=}0.7$ & 41.0 & 0.299 \\
189	$\tau{=}0.9$ & 46.4 & 0.277 \\
190	$\tau{=}1.1$ & 47.1 & 0.525 \\
191	\midrule
192	Mean & 46.7 & 0.319 \\
193	\bottomrule
194	\end{tabular}
195	\end{table}
196	
197	\subsection{Feature Overlap Analysis}
198	\label{app:feature_overlap}
199	
200	We probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.
201	PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics; \texttt{var\_surprisal} and \texttt{p90\_ppl} yield negative $R^2$ under linear probing; these features are not linearly accessible in the pretrained representation space.
202	This confirms that the 20pp accuracy gap between feature-based and end-to-end methods (\S\ref{app:e2e}) stems from complementary, not redundant, representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.
203	
204	\subsection{End-to-End Learning}
205	\label{app:e2e}
206	
207	DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end achieve 58.3\% ($\pm$4.7\%) and 59.5\% ($\pm$3.2\%) respectively, lagging the RF baseline (78.7\%) by 20.4pp and 19.2pp.
208	The 1.2pp inter-backbone gap rules out architecture bias; Table~\ref{tab:e2e_detail} shows both backbones share the same failure mode (high d0 F1, $>$0.94, but collapsed d1/d2 performance, F1 $\leq$ 0.42), while RF achieves 0.596 d2 recall, a $>$2$\times$ advantage at the hardest depth class.
209	
210	\begin{table}[h]
211	\centering
212	\small
213	\caption{Per-class performance for end-to-end PLM classifiers vs.\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}
214	\label{tab:e2e_detail}
215	\resizebox{\columnwidth}{!}{%
216	\begin{tabular}{@{}lccccc@{}}
217	\toprule
218	Method & Acc (\%) & d0 & d1 & d2 & d3 \\
219	\midrule
220	DeBERTa-v3 & 58.3\,$\pm$\,4.7 & .947 & .378 & .247 & .656 \\
221	RoBERTa-base & 59.5\,$\pm$\,3.2 & .958 & .416 & .261 & .647 \\
222	\midrule
223	RF (19 feat.) & 78.7 & --- & --- & .596$^\dagger$ & --- \\
224	\bottomrule
225	\multicolumn{6}{@{}l}{\footnotesize $^\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}
226	\end{tabular}}
227	\end{table}
228	
229	\paragraph{Feature space divergence.}
230	SHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 88.8\% of RF's total contribution.
231	Three independent importance measures (SHAP, Gini, and permutation) show strong concordance (Kendall's $W{=}0.90$, $p{<}0.005$; pairwise Spearman $\rho$: SHAP--Gini $0.93$, SHAP--permutation $0.84$; \S\ref{app:permutation}), with \texttt{p90\_ppl} appearing in the SHAP top-2 in 9/9 cells and \texttt{var\_surprisal} in 8/9.
232	Linear probing of PLM [CLS] representations yields negative $R^2$ for both \texttt{var\_surprisal} and \texttt{p90\_ppl} (\S\ref{app:feature_overlap}); pretrained representations lack the linear structure needed to recover perplexity tail statistics, a systematic representational gap rather than a backbone-specific artifact.
233	
234	DCOL \cite{cloc2025} reached 64.5\% (\S\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods; depth estimation therefore benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.
235	This comparison is bounded by backbone scale ($\leq$125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.
236	
237	\subsection{Domain Bias Analysis}
238	\label{app:domain_bias}
239	
240	To assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.
241	
242	\paragraph{Methodological note.}
243	An initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\%, seed-group prediction 20.8\%).
244	We discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.
245	The results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.
246	
247	\paragraph{Sub-A: Standard CV.}
248	Five-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\% to 82\% across the 9 atlas cells (up to 2.5$\times$ above the 33.3\% chance level); depth signal is therefore the dominant classification factor.
249	
250	\paragraph{Sub-B: LOGO evaluation.}
251	We assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.
252	LOGO mean accuracy is 72.1\% (range 59.5--81.6\%), matching standard CV (72.0\%) within noise (before fix: 64.0\%, reflecting the depth--group confound).
253	Per-cell fold standard deviations range from 0.4pp to 1.4pp; cross-group generalization is therefore as reliable as within-group classification.
254	
255	\paragraph{Sub-C: Negative control.}
256	We train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\%).
257	Depth prediction accuracy averages 72.0\%; seed-group prediction averages 10.2\%, indistinguishable from chance (before fix: 20.8\%, inflated by the depth--group confound).
258	The depth-to-seed-group accuracy ratio is 7.1$\times$; the feature representation therefore encodes depth but not seed-article identity.
259	
260	Taken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.
261	
262	\subsection{Wild-Data Calibration}
263	\label{app:calibration}
264	
265	Table~\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages, crawled 2019--2020; pre-LLM deployment).
266	
267	\begin{table}[h]
268	\centering
269	\small
270	\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+. 95\% Wilson CIs computed for C4 ($n{=}5{,}000$).}
271	\label{tab:calibration}
272	\resizebox{\columnwidth}{!}{%
273	\begin{tabular}{@{}llrccc@{}}
274	\toprule
275	Model & Source & $n$ & d0 (\%) & FPR (\%) & 95\% Wilson CI \\
276	\midrule
277	Pythia-1.4B & WikiText & 546 & 100.0 & 0.0 & --- \\
278	 & C4 & 5{,}000 & 79.8 & 20.2 & [19.1, 21.3] \\
279	\addlinespace
280	GPT-2~XL & WikiText & 546 & 99.3 & 0.7 & --- \\
281	 & C4 & 5{,}000 & 77.6 & 22.4 & [21.3, 23.6] \\
282	\addlinespace
283	OLMo-1B & WikiText & 546 & 98.5 & 1.5 & --- \\
284	 & C4 & 5{,}000 & 95.3 & 4.7 & [4.2, 5.3] \\
285	\bottomrule
286	\end{tabular}}
287	\end{table}
288	
289	On WikiText-103, all three classifiers achieve $\geq$98.5\% d0 accuracy; editorial text is therefore reliably distinguished from recursive generations across model families.
290	On C4, FPR varies sharply: OLMo (4.7\%) vs.\ Pythia (20.2\%) and GPT-2~XL (22.4\%).
291	C4 misclassifications concentrate in template and SEO content with elevated repetition features (\texttt{rep\_3gram} $+$37\%, \texttt{rep\_4gram} $+$75\% vs.\ correctly classified d0 passages), rather than in random noise.
292	The model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.
293	Among C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\%), d2 (3.7\%), d3 (9.6\%); for OLMo, d1 (2.9\%), d2 (0.5\%), d3 (1.3\%). The non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.
294	
295	\paragraph{Threshold calibration.}
296	A pooled RF classifier (trained on all three families' nucleus data) achieves ECE\,=\,0.052 on in-distribution data; Platt scaling and isotonic regression yield no improvement; probability estimates are already well calibrated.
297	The high FPR on web-crawl data is therefore a decision-threshold problem, not a probability calibration defect.
298	Applying a confidence threshold $P(\mathrm{d0}) \geq 0.15$ reduces C4 FPR from 33.4\% to 2.8\% and FineWeb FPR from 16.9\% to 0.7\%, at a cost of only $-$0.3\,pp balanced accuracy (78.0\%$\to$77.7\%).
299	The $P(\mathrm{d0})$ distribution is bimodal: 67\% of samples exceed 0.95 (high-confidence d0), while 33\% fall in the 0.15--0.30 uncertainty zone; the threshold separates these modes cleanly.
300	Wild-data FPR is thus an operational threshold choice rather than a fundamental limitation, though the optimal threshold is domain-dependent.
301	
302	\subsection{Downstream Curation PoC (Inconclusive)}
303	\label{app:curation_poc}
304	
305	To assess whether depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.
306	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.
307	Conditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\approx$25\%, moderate $\approx$50\%, soft threshold).
308	Table~\ref{tab:curation_poc} reports per-condition perplexity; Table~\ref{tab:curation_comparisons} reports pairwise contrasts.
309	
310	\begin{table}[h]
311	\centering
312	\small
313	\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $^*$\,: $p<0.05$ (paired $t$-test vs.\ unfiltered).}
314	\label{tab:curation_poc}
315	\resizebox{\columnwidth}{!}{%
316	\begin{tabular}{@{}lcccccc@{}}
317	\toprule
318	Condition & Mean PPL & Std & $n$ & $\Delta$ vs Unfilt. & $p$ & $d_z$ \\
319	\midrule
320	unfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\
321	rf\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.41    \\
322	rf\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.34    \\
323	rf\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.25  \\
324	oracle\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.34  \\
325	oracle\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$0.66  \\
326	random\_soft      & 16.062 & 0.079 &  4{,}422 & $-$0.286 & ${<}$0.001$^*$ & $-$2.77  \\
327	random\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.028$^*$ & $-$1.50  \\
328	random\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$1.89  \\
329	\bottomrule
330	\end{tabular}}
331	\end{table}
332	
333	\begin{table}[h]
334	\centering
335	\small
336	\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\,: $p<0.05$; $^{**}$\,: $p<0.01$.}
337	\label{tab:curation_comparisons}
338	\resizebox{\columnwidth}{!}{%
339	\begin{tabular}{@{}lccc@{}}
340	\toprule
341	Comparison & $\Delta$ PPL & $t$ & $p$ \\
342	\midrule
343	rf\_strict vs random\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\
344	rf\_moderate vs random\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\
345	rf\_soft vs random\_soft         & 0.328 & $-$17.98 & ${<}$0.001$^{**}$ \\
346	rf\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\
347	\bottomrule
348	\end{tabular}}
349	\end{table}
350	
351	RF-based depth filtering (19-feature F1\,=\,0.997) substantially outperforms a simple perplexity-threshold baseline (F1\,=\,0.845) for identifying low-depth passages; the multi-feature representation provides discriminative value beyond raw perplexity.
352	However, the primary comparison (RF-filtered vs.\ unfiltered, $p > 0.4$) is non-significant; the significant RF-vs-random contrasts ($p < 0.02$) involve multiple pairwise comparisons that were not corrected for multiplicity.
353	
354	\subsection{Reference Model Ablation}
355	\label{app:ref_ablation}
356	
357	\begin{table}[h]
358	\centering
359	\caption{Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0--d3) using different reference models for feature extraction.}
360	\label{tab:ref_ablation}
361	\resizebox{\columnwidth}{!}{%
362	\begin{tabular}{@{}lcc@{}}
363	\toprule
364	Reference Model & Architecture & Accuracy (\%) \\
365	\midrule
366	Pythia-1.4B (self) & GPT-NeoX & 78.6 $\pm$ 0.6 \\
367	OLMo-1B (cross) & OLMo & 74.5 $\pm$ 0.7 \\
368	GPT-2~XL (cross) & GPT-2 & 67.3 $\pm$ 0.7 \\
369	\bottomrule
370	\end{tabular}}
371	\end{table}
372	
373	\subsection{Cross-Scale Full Results}
374	\label{app:cross_scale_full}
375	
376	This section provides the full cross-scale analysis summarized in \S\ref{sec:gen:crossscale}.
377	We extend the benchmark to two 7--8B models (Qwen2.5-7B-Instruct \cite{qwen2.5}, Llama-3.1-8B-Instruct \cite{llama3}) and one 14B model (Qwen2.5-14B).
378	The 7--8B models use 4-bit NF4 QLoRA fine-tuning with nucleus sampling ($p{=}0.95$, 500 samples per depth, depths $d \in \{0, 1, \ldots, 5\}$).
379	The 14B model uses clean FP16 LoRA fine-tuning across all three decoding strategies (nucleus, temperature $\tau{=}0.9$, top-$k$ $k{=}50$; 5{,}000 samples per depth, depths $d \in \{0, 1, 2, 3\}$).
380	Feature extraction for 1--8B models uses Pythia-1.4B as reference; Qwen2.5-14B uses self-reference (the 14B model computes its own perplexity features), a choice that precludes direct comparison with the Pythia-referenced pipeline (see confounds below).
381	
382	\paragraph{Scale comparison.}
383	Table~\ref{tab:cross_scale} contrasts the 7--14B models with the three 1--1.5B models on matched evaluation (depths 0--3).
384	The 14B model is tested across all three decoding strategies; the 7--8B models use nucleus sampling only.
385	
386	\begin{table}[h]
387	\centering
388	\small
389	\caption{Cross-scale comparison: 4-class RF accuracy (\%, depths 0--3), $\mathrm{EDD}_{T{=}0.70}$, and d0-vs-d1 AUC. CI: 95\% bootstrap. Chance = 25\%. $^\dagger$Self-reference model (see text).}
390	\label{tab:cross_scale}
391	\resizebox{\columnwidth}{!}{%
392	\begin{tabular}{@{}llccc@{}}
393	\toprule
394	Model & Strategy & 4-class acc & $\mathrm{EDD}_{0.70}$ & d0v1 \\
395	\midrule
396	GPT-2~XL (1.5B) & nucleus & 84.3 & 4 & 0.999 \\
397	OLMo-1B & nucleus & 78.9 & 4 & 0.997 \\
398	Pythia-1.4B & nucleus & 78.7 & 4 & 0.998 \\
399	\midrule
400	Llama-3.1-8B & nucleus & 70.2\,[68.3, 72.4] & 4 & 0.949 \\
401	Qwen2.5-7B & nucleus & 60.1\,[58.0, 62.1] & ${>}5$ & 0.969 \\
402	\midrule
403	Qwen2.5-14B$^\dagger$ & nucleus & 54.1\,[53.4, 54.7] & 0 & 0.643 \\
404	Qwen2.5-14B$^\dagger$ & temp09 & 50.5\,[49.8, 51.2] & 0 & 0.632 \\
405	Qwen2.5-14B$^\dagger$ & top-$k$50 & 47.9\,[47.3, 48.6] & 0 & 0.561 \\
406	\cmidrule{2-5}
407	\multicolumn{2}{@{}l}{\textit{14B mean}} & \textit{50.8} & --- & --- \\
408	\bottomrule
409	\end{tabular}}
410	\end{table}
411	
412	\paragraph{(1) Depth signal persists at 7--8B scale.}
413	Both 7--8B models substantially exceed the 25\% chance baseline: Llama-3.1-8B achieves 70.2\% (95\% CI $[68.3, 72.4]$) and Qwen2.5-7B achieves 60.1\% ($[58.0, 62.1]$); recursive depth therefore remains estimable from perplexity-based features even when the generator is 5--7$\times$ larger than the reference model.
414	Depth-0 separability is preserved in both models: d0v1 AUC is 0.949 (Llama-3.1) and 0.969 (Qwen2.5).
415	
416	\paragraph{(2) EDD at 7--8B scale.}
417	At threshold $T{=}0.70$, Qwen2.5-7B maintains all consecutive-pair AUCs above 0.70 through depth~5 (Table~\ref{tab:cross_scale_auc}), yielding $\mathrm{EDD}_{T{=}0.70} > 5$, exceeding the $\mathrm{EDD}{=}4$ observed at 1--1.5B.
418	Llama-3.1-8B matches the smaller models at $\mathrm{EDD}{=}4$: its monotonic decay causes d4v5 (0.618) to drop below $T$, despite stronger signal at shallower depths.
419	Both larger generators produce weaker per-step signal than the 1--1.5B models (mean consecutive AUC: 0.786 for Llama-3.1, 0.782 for Qwen2.5, vs.\ 0.852 at 1--1.5B).
420	
421	\begin{table}[h]
422	\centering
423	\small
424	\caption{Consecutive binary AUC. Llama-3.1-8B exhibits monotonic decay; Qwen2.5-7B shows a U-shaped pattern; Qwen2.5-14B$^\dagger$ (depths 0--3 only) has all pairs below $T{=}0.70$ with strategy-specific patterns. $^\dagger$Self-reference model.}
425	\label{tab:cross_scale_auc}
426	\resizebox{\columnwidth}{!}{%
427	\begin{tabular}{@{}llccccc@{}}
428	\toprule
429	Model & Strategy & d0v1 & d1v2 & d2v3 & d3v4 & d4v5 \\
430	\midrule
431	Llama-3.1-8B & nucleus & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\
432	Qwen2.5-7B & nucleus & 0.969 & 0.729 & 0.709 & 0.732 & 0.772 \\
433	\midrule
434	Qwen2.5-14B$^\dagger$ & nucleus & 0.643 & 0.713 & \textbf{0.728} & \multicolumn{2}{c}{--} \\
435	Qwen2.5-14B$^\dagger$ & temp09 & 0.632 & \textbf{0.726} & 0.618 & \multicolumn{2}{c}{--} \\
436	Qwen2.5-14B$^\dagger$ & top-$k$50 & 0.561 & 0.687 & 0.679 & \multicolumn{2}{c}{--} \\
437	\bottomrule
438	\end{tabular}}
439	\end{table}
440	
441	\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}
442	Among instruction-tuned models, Llama-3.1-8B exhibits monotonic AUC decay consistent with the 1--1.5B pattern, while Qwen2.5-7B shows a U-shaped recovery beyond d2v3 (Table~\ref{tab:cross_scale_auc}).
443	A base-model control (Llama-3.1-8B without instruction tuning) clarifies the causal direction: the base model achieves 59.9\% four-class accuracy (95\% CI [57.8, 62.15], $\mathrm{EDD}_{0.70}{=}2$) with non-monotonic AUC decay (Table~\ref{tab:llama3_base_auc}), while the instruction-tuned variant reaches 70.2\% with strictly monotonic decay.
444	The base-model control experiment suggests instruction-tuning regularizes rather than confounds the depth signal.
445	
446	\begin{table}[h]
447	\centering
448	\small
449	\caption{Pairwise AUC: Llama-3.1-8B Base vs.\ Instruct.}
450	\label{tab:llama3_base_auc}
451	\begin{tabular}{lccccc}
452	\toprule
453	Variant & $d_{0\text{v}1}$ & $d_{1\text{v}2}$ & $d_{2\text{v}3}$ & $d_{3\text{v}4}$ & $d_{4\text{v}5}$ \\
454	\midrule
455	Base & 0.918 & 0.794 & 0.682 & 0.730 & 0.595 \\
456	Instruct & 0.965 & 0.874 & 0.771 & 0.716 & 0.618 \\
457	\bottomrule
458	\end{tabular}
459	\end{table}
460	
461	The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.
462	
463	\paragraph{(4) Signal attenuation at 14B.}
464	Qwen2.5-14B (clean FP16, self-reference) is tested across all three decoding strategies (Table~\ref{tab:cross_scale}).
465	Mean four-class accuracy is 50.8\% ($2.0{\times}$ chance), with nucleus 54.1\%, temperature 50.5\%, and top-$k$ 47.9\%.
466	$\mathrm{EDD}_{0.70}{=}0$ across all three strategies: no adjacent-depth pair reaches the 0.70 AUC threshold.
467	The d0/d1 boundary, near-perfect at 1--1.5B (AUC ${>}0.99$), attenuates to 0.56--0.64 at 14B.
468	
469	Each strategy produces a structurally distinct adjacent-pair AUC pattern (Table~\ref{tab:cross_scale_auc}):
470	nucleus is monotonically increasing (d0v1=0.643 $<$ d1v2=0.713 $<$ d2v3=0.728);
471	temperature exhibits d2v3 collapse (0.618, the weakest boundary) because temperature scaling uniformly amplifies logit differences, accelerating convergence to the attractor distribution at deeper depths;
472	top-$k$ exhibits d0v1 collapse (0.561, the weakest boundary) because vocabulary truncation constrains d0 and d1 distributions to the same top-$k$ tokens, compressing their statistical distance.
473	This three-way divergence confirms at 14B that different decoding strategies induce structurally distinct degradation trajectories (\S\ref{sec:gen:crossstrategy}).
474	
475	Feature importance shifts under top-$k$: lexical diversity metrics (TTR, hapax ratio) enter the top-5, displacing perplexity tail statistics that dominate under nucleus and temperature.
476	This result carries an important caveat: Qwen2.5-14B uses self-reference, whereas all other experiments use Pythia-1.4B.
477	Self-reference conflates the generator's distributional shift with the reference model's sensitivity; the observed attenuation may partially reflect the reference model change rather than a pure scale effect.
478	
479	\paragraph{Caveats.}
480	For Qwen2.5-7B, the CI lower bound (58.0\%) does not exclude sub-60\% accuracy; Llama-3.1-8B's lower bound (68.3\%) is more comfortably above chance but still below the 75--83\% range at 1--1.5B.
481	The divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.
482	
483	\paragraph{Confounds.}
484	\label{app:cross_scale_confounds}
485	Four confounds limit the 7--8B results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling at 7--8B (the 14B model addresses this with all three strategies); (4)~vocabulary mismatch between larger generators and the 1.4B reference model.
486	For the 14B model specifically: self-reference rather than the Pythia-1.4B reference used for all other experiments prevents direct cross-scale comparison.
487	The base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.
488	The remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution); it is therefore infeasible to attribute the observed accuracy gap (60--70\% vs.\ 78--85\% at 1--1.5B) to any single factor.
489	
490	\subsection{Cross-Boundary Generalization}
491	\label{app:cross_boundary}
492	
493	The preceding experiments assume a single model family generates all recursive depths.
494	In practice, recursive contamination may traverse model boundaries: text generated by model~A is used to train model~B, whose output trains model~C.
495	We probe whether the depth signal persists under two relaxations of the single-model assumption.
496	
497	\paragraph{Cross-model recursive chains.}
498	We construct a heterogeneous chain: human text (d0) $\to$ Pythia-1.4B generates d1 $\to$ OLMo-1B finetuned on Pythia-d1 generates d2 $\to$ GPT-2~XL finetuned on OLMo-d2 generates d3.
499	Each recursive step uses a \emph{different} model family, eliminating the possibility that depth signal arises from a single model's idiosyncratic behavior.
500	A 4-class Random Forest achieves 84.75\% accuracy (95\% CI $[81.0, 88.25]$), with per-depth F1 scores of 0.98 (d0), 0.88 (d1), 0.76 (d2), and 0.76 (d3).
501	Pairwise AUC remains high: d0-vs-d1 = 0.999 and d2-vs-d3 = 0.841.
502	These results suggest that distributional artifacts of recursive generation persist across model boundaries. This constitutes preliminary evidence for a process-level depth signal rather than individual generator artifacts.
503	
504	\paragraph{Confound discussion.}
505	The heterogeneous chain confounds architecture identity with depth (d1=Pythia, d2=OLMo, d3=GPT-2~XL).
506	However, if the classifier exploited architecture fingerprints rather than depth signal, near-perfect accuracy would be expected since architecture perfectly determines depth label.
507	The observed 84.75\% with monotonically decreasing per-depth F1 (d0=0.98, d1=0.88, d2=0.76, d3=0.76) is more consistent with a depth-signal interpretation, as architecture fingerprinting would not produce this graded pattern.
508	We address this confound directly with a reverse-chain control below.
509	
510	\paragraph{Reverse-chain control.}
511	To empirically test the architecture confound hypothesis, we constructed a reverse chain (GPT-2~XL $\to$ OLMo $\to$ Pythia) reversing the model-depth assignment.
512	The reverse chain achieves 85.75\% (95\% CI [82.0, 89.25]), statistically indistinguishable from the forward chain (84.75\%, [81.0, 88.25]).
513	If the classifier exploited architecture fingerprints rather than depth signal, reversing the chain should invert depth predictions; the equivalent accuracy under both orderings provides empirical evidence against the architecture confound.
514	
515	\paragraph{Cross-domain transfer.}
516	All prior experiments use WikiText-103 as the seed corpus.
517	To test domain dependence, we repeat the pipeline with arXiv abstracts as the seed text (Pythia-1.4B, nucleus $p{=}0.95$, 500 samples per depth, d0--d3).
518	Five-fold cross-validation yields 74.1\% $\pm$ 2.0\% accuracy, compared to ${\sim}$78\% on the WikiText seed.
519	Per-depth F1 shows the familiar pattern: d0 = 1.00, d1 = 0.78, d2 = 0.52, d3 = 0.66, with d2 remaining the most challenging class.
520	The 4pp accuracy gap relative to WikiText likely reflects the narrower stylistic range of scientific abstracts, which may reduce the distributional contrast between adjacent depths.
521	These results provide preliminary evidence that the perplexity-based features capture properties of the recursive generation process rather than domain-specific artifacts of the seed corpus.
522	
523	\subsection{Cross-Seed Replication}
524	\label{app:seed_replication}
525	
526	Table~\ref{tab:seed_replication} reports within-seed accuracy for all three model families (nucleus, depths 0--3) under two independent LoRA training seeds.
527	
528	\begin{table}[h]
529	\centering
530	\small
531	\caption{Cross-seed replication (nucleus $p{=}0.95$, d0--d3). seed=42 is the primary benchmark (matching Table~\ref{tab:main_matrix}); seed=43 is an independent replication.}
532	\label{tab:seed_replication}
533	\begin{tabular}{@{}llccc@{}}
534	\toprule
535	Model & Seed & Acc (\%) & 95\% CI & $\Delta$ (pp) \\
536	\midrule
537	Pythia-1.4B & 42 & 78.70 & [78.10, 79.24] & --- \\
538	Pythia-1.4B & 43 & 78.84 & [78.13, 79.52] & $+$0.14 \\
539	\midrule
540	OLMo-1B & 42 & 78.94 & [78.38, 79.48] & --- \\
541	OLMo-1B & 43 & 82.11 & [81.77, 82.54] & $+$3.17 \\
542	\midrule
543	GPT-2~XL & 42 & 84.28 & [83.78, 84.80] & --- \\
544	GPT-2~XL & 43 & 86.32 & [86.17, 86.49] & $+$2.04 \\
545	\bottomrule
546	\end{tabular}
547	\end{table}
548	
549	Seed=43 yields higher accuracy in all three models ($+$0.14 to $+$3.17\,pp, same direction).
550	For Pythia ($+$0.14\,pp), CIs overlap, consistent with noise; for OLMo ($+$3.17\,pp) and GPT-2~XL ($+$2.04\,pp), CIs do not overlap, so LoRA initialization has a non-trivial effect on absolute accuracy (${\sim}$1--3\,pp).
551	Top-3 features are identical across all seeds and models (\texttt{p90\_ppl}, \texttt{var\_surprisal}, \texttt{p75\_ppl}); depth ordering is preserved in every configuration.
552	
553	\paragraph{Outlier handling.}
554	Feature extraction occasionally produces extreme perplexity values (outlier passages); we apply per-feature clipping at $\pm 10^{10}$ before classification, affecting ${<}0.1$\% of samples.
555	The d3 perplexity distribution varies substantially across seeds: under seed=42, 0.56\% of d3 passages exceed $10^6$ in raw perplexity, while under seed=43 this fraction rises to 12.8\%.
556	Despite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.
557	
558	\subsection{Depth-4 Extension}
559	\label{app:depth4_ext}
560	
561	We extend all three model families (GPT-2~XL, Pythia-1.4B, OLMo-1B; nucleus $p{=}0.95$) to depth~4 and train 5-class RF classifiers (d0--d4, 5{,}000 samples per depth).
562	Five-class accuracy reaches 80.5\% (OLMo), 74.0\% (GPT-2~XL), and 71.3\% (Pythia), all substantially above the 20\% chance baseline.
563	For Pythia and GPT-2~XL, d3 recall drops from ${\sim}$80\% (4-class) to ${\sim}$49\% (5-class) due to d3/d4 confusion; d4 recall is higher (Pythia 68.1\%, GPT-2~XL 63.9\%).
564	$\mathrm{EDD}_{0.70} \geq 4$ was established by dedicated binary classifiers in the atlas (\S\ref{sec:atlas:edd}; d3v4 AUC: Pythia 0.784, OLMo 0.765, GPT-2~XL 0.750); the 5-class results provide complementary evidence that depth~4 remains discriminable in the multi-class setting.
565	
566	\paragraph{Feature monotonicity at d4.}
567	For Pythia and GPT-2~XL, the dominant depth markers (\texttt{p90\_ppl}, \texttt{var\_surprisal}) maintain monotonic decrease through d4 (Pythia \texttt{p90\_ppl}: $483.7 \to 12.5$ from d0 to d4; \texttt{var\_surprisal}: $6.50 \to 1.29$), consistent with continued tail erosion (\S\ref{sec:method:theory}).
568	Mean perplexity breaks monotonicity at d4 for GPT-2~XL (d3: $1{,}076\mathrm{K}$ $\to$ d4: $928\mathrm{K}$) while tail perplexity continues to decline.
569	OLMo exhibits a \texttt{var\_surprisal} rebound at d4 ($2.49 \to 2.83$, non-monotonic), creating a feature signature absent in GPT-2~XL and Pythia.
570	The 5-class RF exploits non-adjacent depth contrasts (particularly d0-vs-d4 and d2-vs-d4) to achieve 80.5\% accuracy, the highest among all three families, while the dedicated binary d3-vs-d4 classifier (AUC 0.765) is restricted to adjacent-depth features.
571	This discrepancy illustrates that multi-class classifiers can leverage global distributional structure unavailable to pairwise comparisons.
572	The divergence between aggregate and tail statistics suggests that aggregate distributional statistics saturate at deep recursion while tail statistics continue to shift.
573	This saturation provides a physical mechanism for the EDD ceiling: once per-step feature change falls below classifier resolution, adjacent depths become indistinguishable regardless of continued distributional drift.
574	
575	\subsection{Generation Length Ablation}
576	\label{app:length_ablation}
577	
578	Table~\ref{tab:length_ablation} reports classification accuracy as a function of passage length (Pythia-1.4B nucleus, depths 0--3).
579	
580	\begin{table}[h]
581	\centering
582	\small
583	\caption{Generation length ablation (Pythia-1.4B nucleus, 5-fold CV). Accuracy increases monotonically with passage length; the 9.47\,pp spread confirms that longer passages provide stronger statistical signal.}
584	\label{tab:length_ablation}
585	\begin{tabular}{@{}lc@{}}
586	\toprule
587	Passage length (tokens) & Acc (\%) \\
588	\midrule
589	128 & 68.35 \\
590	256 & 73.80 \\
591	512 & 77.82 \\
592	\bottomrule
593	\end{tabular}
594	\end{table}
595	
596	Depth signal is detectable from 128 tokens (2.7$\times$ chance) and saturates near 500 tokens.
597	The monotonic increase reflects the statistical nature of the features: longer passages yield more stable estimates of perplexity percentiles and surprisal variance, reducing within-class overlap at adjacent depth boundaries.
598	
599	\subsection{Mixed-Depth Corpus}
600	\label{app:mixed_depth}
601	
602	Per-passage classification is largely independent of corpus composition: evaluating on a corpus containing mixed proportions of d0--d3 passages (rather than balanced classes) yields macro-recall $\Delta{=}{-}1.62$\,pp relative to the balanced benchmark (within the 2\,pp tolerance).
603	Individual class deltas range from $-$0.45\,pp to $-$2.43\,pp (d1 shows the largest shift); the RF classifier operates on per-sample features without sensitivity to the class distribution of the evaluation corpus.
604	Macro-recall $\Delta$ = $-$1.62\,pp (within the 2\,pp threshold); individual class variations (max 2.43\,pp on d1) arise from held-out sample composition rather than classifier sensitivity to corpus distribution, as the Random Forest produces identical per-sample predictions regardless of batch context.
605	
606	\subsection{Learned Estimator Comparison}
607	\label{app:learned_estimator}
608	
609	Table~\ref{tab:learned_estimator} evaluates three learned classifiers (XGBoost, ordinal MLP with CORAL loss \cite{coral2020}, prototypical networks) under the same leave-one-model-out protocol as Table~\ref{tab:cross_model}.
610	The ordinal MLP follows the nested binary reduction framework \cite{mccullagh1980_ordinal,frank2001} with the loss function of \citet{rennie2005}.
611	All three methods operate on the same 19-dimensional feature vector; the comparison isolates the effect of the classification head.
612	
613	\begin{table}[h]
614	\centering
615	\small
616	\caption{Learned estimator cross-model transfer (leave-one-model-out, nucleus, 4-class). RF baseline from Table~\ref{tab:cross_model}. Chance = 25\%.}
617	\label{tab:learned_estimator}
618	\begin{tabular}{@{}lcccc@{}}
619	\toprule
620	Method & Pythia & OLMo & GPT-2 XL & Mean \\
621	\midrule
622	RF (baseline) & --- & --- & --- & 66.4 \\
623	XGBoost & 63.7 & 69.8 & 68.1 & 67.2 \\
624	Ordinal MLP & 62.5 & 69.7 & 67.9 & 66.7 \\
625	Prototypical & 61.6 & 70.0 & 68.4 & 66.6 \\
626	\bottomrule
627	\end{tabular}
628	\end{table}
629	
630	All three learned methods match the RF baseline within 0.8\,pp on average; the Pythia holdout is consistently the hardest (61.6--63.7\%), while OLMo and GPT-2~XL holdouts yield 67.9--70.0\%.
631	The narrow spread ($\leq$0.8\,pp across four methods) reinforces the conclusion that the 19-feature representation, not the classifier, determines the accuracy ceiling in the cross-model transfer setting.
632	
633	\subsection{Instruction-Tuned Model at 1.5B Scale}
634	\label{app:instruct_1p5b}
635	
636	To test whether instruction tuning eliminates depth signal at matched scale (1.5B, avoiding the quantization confound of \S\ref{sec:gen:crossscale}), we run the full recursive pipeline on Qwen2.5-1.5B-Instruct with self-reference feature extraction (i.e., the same model serves as both generator and reference).
637	
638	The RF classifier achieves 47.4\% four-class accuracy (95\% CI $[46.7, 48.1]$, $1.9\times$ chance); instruction tuning therefore reduces but does not eliminate depth signal.
639	The pairwise AUC profile differs from base models: d0v1 = 0.653, d1v2 = 0.620, d2v3 = 0.664, with a gap-dependent pattern (non-adjacent pairs yield higher AUC, e.g., d0v3 = 0.902) but no pair reaching the 0.75 threshold.
640	
641	The top-5 features shift substantially: \texttt{surprisal\_range}, \texttt{surprisal\_position\_corr}, \texttt{prob\_std}, \texttt{surprisal\_first\_half\_minus\_second}, and \texttt{surprisal\_std} replace the perplexity tail statistics (\texttt{p90\_ppl}, \texttt{var\_surprisal}) that dominate in base models.
642	This feature shift suggests instruction tuning compresses the perplexity distribution (reducing tail discriminability) while preserving positional and range-based surprisal patterns.
643	
644	Two caveats apply: (1) self-reference evaluation may inflate or deflate accuracy relative to cross-reference evaluation (cf.\ \S\ref{app:ref_ablation}); (2) a single instruction-tuned model does not establish the generality of the feature shift across architectures or instruction-tuning recipes.
645	
646	\subsection{Downstream Fine-Tuning Probe (Inconclusive)}
647	\label{app:downstream}
648	
649	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) on depth-stratified subsets (500 samples each) and evaluate held-out perplexity (200 samples, 50 per depth).
650	
651	\begin{table}[h]
652	\centering
653	\small
654	\caption{Downstream fine-tuning probe: held-out perplexity by training subset (Pythia-410M LoRA, seed=42). $\Delta$: signed difference vs.\ baseline (negative = better).}
655	\label{tab:downstream}
656	\begin{tabular}{@{}lcc@{}}
657	\toprule
658	Training subset & PPL & $\Delta$ vs.\ baseline \\
659	\midrule
660	Baseline (no fine-tuning) & 5.67 & --- \\
661	d0 only & 5.65 & $-$0.02 \\
662	d1 only & 5.55 & $-$0.12 \\
663	d2 only & 5.56 & $-$0.11 \\
664	Mixed (d0--d3) & 5.55 & $-$0.12 \\
665	\bottomrule
666	\end{tabular}
667	\end{table}
668	
669	The hypothesis that d0-only data yields the lowest perplexity is not supported: d1-only and mixed subsets tie for best (PPL~5.55), both marginally below d0-only (5.65).
670	The PPL spread is small (0.12, 2.1\% relative) and the sample size (500 per condition, single seed) is insufficient for statistical significance.
671	Training loss decreases monotonically with depth (d0: 2.558, d1: 1.920, d2: 1.286), consistent with recursive generation reducing information content and making text easier to model.
672	This pilot establishes that depth-filtered data is not harmful for downstream fine-tuning; whether depth-aware curation provides a meaningful advantage requires larger-scale evaluation.
673	
674	\subsection{Feature Group Ablation}
675	\label{app:feature_ablation}
676	
677	Table~\ref{tab:feature_ablation} reports cross-model transfer accuracy (leave-one-model-out, nucleus) when restricting the classifier to subsets of the 19-feature vector, grouped by signal type.
678	
679	\begin{table}[h]
680	\centering
681	\small
682	\caption{Feature group ablation (cross-model LOO, nucleus, 4-class). Chance = 25\%.}
683	\label{tab:feature_ablation}
684	\begin{tabular}{@{}lccc@{}}
685	\toprule
686	Feature group & \#Feat. & Acc (\%) & $\Delta$ vs.\ Full \\
687	\midrule
688	Full (all 19) & 19 & 66.6 & --- \\
689	Perplexity only & 9 & 66.0 & $-$0.5 \\
690	Entropy/Surprisal only & 5 & 63.2 & $-$3.4 \\
691	Repetition/Diversity only & 5 & 53.0 & $-$13.6 \\
692	\midrule
693	\texttt{p90\_ppl} only & 1 & 58.3 & $-$8.3 \\
694	\bottomrule
695	\end{tabular}
696	\end{table}
697	
698	The 9 perplexity features nearly match the full set ($\Delta{=}{-}0.5$\,pp), while repetition/diversity features alone fall 13.6\,pp below; perplexity degradation statistics therefore carry the dominant depth signal.
699	The top-2 individual features by Gini importance are \texttt{p90\_ppl} (22.4\%) and \texttt{var\_surprisal} (18.8\%), accounting for 41\% of total importance.
700	
701	\subsection{RF Seed Robustness}
702	\label{app:rf_seed}
703	
704	Table~\ref{tab:rf_seed} reports cross-model transfer accuracy across three RF random seeds.
705	
706	\begin{table}[h]
707	\centering
708	\small
709	\caption{RF seed robustness (cross-model LOO, nucleus, 4-class).}
710	\label{tab:rf_seed}
711	\begin{tabular}{@{}lc@{}}
712	\toprule
713	Seed & Acc (\%) \\
714	\midrule
715	42 & 66.4 \\
716	123 & 66.5 \\
717	456 & 66.5 \\
718	\midrule
719	Mean $\pm$ std & 66.48 $\pm$ 0.06 \\
720	\bottomrule
721	\end{tabular}
722	\end{table}
723	
724	The 0.06\,pp standard deviation across seeds confirms that RF classification is deterministic to within rounding noise at this sample size, and reported accuracy differences across experimental conditions (e.g., feature ablation, cross-model transfer) are not attributable to classifier randomness.
725	
726	\subsection{Binary Detector Baselines for Ordinal Classification}
727	\label{app:detector_baselines}
728	
729	We evaluate whether existing binary AI-text detectors and membership inference methods, when repurposed for ordinal classification, can match our 19-feature RF pipeline.
730	
731	\paragraph{Binary detectors (Pythia nucleus).}
732	Binoculars~\cite{binoculars2024} and Fast-DetectGPT~\cite{fast_detectgpt2024} scores are computed on the Pythia-1.4B nucleus ($p{=}0.95$) subset and fed to: (a)~a log-likelihood rank classifier (Log-Rank, 64.0\%), (b)~a combined RF trained on both detector scores (Combined, 74.2\%), and (c)~the standard 19-feature RF (78.7\%).
733	The 4.5\,pp gap (74.2\% vs.\ 78.7\%) confirms that perplexity distributional features capture ordinal depth structure beyond what generic detection scores provide.
734	Note that Fast-DetectGPT exhibits numerical overflow on Pythia nucleus d1 (mean perturbation score $>$28{,}000); results for this cell should be interpreted cautiously.
735	Across all 9 atlas cells, Binoculars and Fast-DetectGPT ordinal accuracy averages ${\sim}$35\% and ${\sim}$32\%, respectively.
736	
737	\paragraph{Membership inference baselines (all 9 cells).}
738	DetectGPT~\cite{mitchell2023_detectgpt} (gpt2-large scoring model, t5-large perturbation model, 5 perturbations) achieves 30.7\% mean 4-class accuracy (d1--d3 BalAcc: 24.3\%).
739	Min-K\% Prob~\cite{shi2024_minkprob} ($K{=}20$) with CORAL ordinal calibration reaches 33.2\% (d1--d3 BalAcc: 40.4\%); the best single cell is gpt2xl\_temp09 at 50.6\%.
740	Min-K\%'s advantage over DetectGPT (+2.5\,pp) is consistent with token-level log-probabilities containing more depth-relevant information than perturbation-based curvature, but both remain within 10\,pp of chance.
741	CORAL calibration improves ordinal structure (d1--d3 BalAcc 40.4\% vs.\ 33.3\% random) without closing the gap to RF (71.6\%), confirming that the bottleneck is the input signal rather than the calibration strategy.
742	Perturbation-based and membership-inference methods (28--33\%) confirm that token-level detection scores lack ordinal depth resolution.
743	Cross-perplexity (Binoculars) is a notable exception: when evaluated across all 9 atlas cells with threshold calibration, Binoculars achieves 69.8\%; with multi-feature RF calibration (11 cross-perplexity statistics), it reaches 78.1\%---matching our 19-feature pipeline within 0.3\,pp (\S\ref{sec:gen:baselines}).
744	
745	\paragraph{Augmented feature set.}
746	To test whether detection scores carry complementary ordinal signal, we add Min-K\% probability ($K{=}20$) and DetectGPT perturbation discrepancy as additional RF features.
747	The 20-feature model (19 + Min-K\%) achieves 78.90\% mean 4-class accuracy (+0.48\,pp) and 72.20\% d1--d3 balanced accuracy (+0.60\,pp).
748	Min-K\% ranks \#3 by feature importance (0.095), behind \texttt{p90\_ppl} (0.161) and \texttt{var\_surprisal} (0.126); DetectGPT ranks \#17 (0.026).
749	The marginal improvement is consistent across 8 of 9 atlas cells, indicating that Min-K\%'s token-level log-probability signal provides weak but real complementary information to the passage-level distributional features.
750	The top-2 features (\texttt{p90\_ppl} + \texttt{var\_surprisal}) retain combined importance of 28.7\%, confirming that perplexity tail statistics remain the dominant depth markers even after augmentation.
751	
752	\subsection{Binoculars Feature Ablation and Signal Decomposition}
753	\label{app:feature_ablation_bino}
754	
755	To quantify the overlap and complementarity between our 19-feature pipeline and Binoculars' cross-perplexity features, we evaluate four feature configurations across all 9 atlas cells (Table~\ref{tab:bino_ablation}).
756	
757	\begin{table}[h]
758	\centering
759	\small
760	\caption{Feature ablation: overlap and merged configurations (9-cell mean, 5-fold CV, RF 200 trees). The 6 overlap features are the perplexity statistics shared between both pipelines (mean, variance, median, p10, p90, skewness).}
761	\label{tab:bino_ablation}
762	\begin{tabular}{@{}lccc@{}}
763	\toprule
764	Configuration & \#Feat. & Acc (\%) & $\Delta$ vs.\ 19-feat \\
765	\midrule
766	6 overlap only & 6 & 75.9 & $-$2.5 \\
767	Our 19 features & 19 & 78.4 & --- \\
768	Binoculars 11 features & 11 & 78.1 & $-$0.3 \\
769	Merged (19 + 11) & 30 & \textbf{82.6} & +4.2 \\
770	\bottomrule
771	\end{tabular}
772	\end{table}
773	
774	The 6 shared perplexity features alone achieve 75.9\% (97\% of the full pipeline's accuracy), confirming that mean-level perplexity distributional displacement is the core depth signal.
775	Our 13 additional features (kurtosis, surprisal variance, lexical/n-gram statistics) contribute +2.5\,pp of shape-level information; Binoculars' 5 unique features (observer-performer agreement score, cross-entropy statistics) contribute +4.2\,pp of cross-model divergence when merged.
776	
777	Table~\ref{tab:bino_ablation_percell} reports per-cell results for all four configurations.
778	
779	\begin{table}[h]
780	\centering
781	\small
782	\caption{Per-cell feature ablation (4-class accuracy \%, 5-fold CV, RF 200 trees). $\Delta$: merged minus 19-feature accuracy.}
783	\label{tab:bino_ablation_percell}
784	\resizebox{\columnwidth}{!}{%
785	\begin{tabular}{@{}lcccc c@{}}
786	\toprule
787	Cell & 6-overlap & 19-feat & Bino-11 & Merged & $\Delta$ \\
788	\midrule
789	Pythia nucleus & 76.7 & 78.7 & --- & 83.5 & +4.8 \\
790	Pythia temp09 & 73.9 & 76.8 & --- & 81.5 & +4.7 \\
791	Pythia top-$k$50 & 65.3 & 68.9 & --- & 71.2 & +2.3 \\
792	OLMo nucleus & 76.4 & 78.9 & --- & 84.2 & +5.3 \\
793	OLMo temp09 & 81.0 & 82.3 & --- & 88.3 & +6.0 \\
794	OLMo top-$k$50 & 72.5 & 74.4 & --- & 78.4 & +4.0 \\
795	GPT-2~XL nucleus & 81.7 & 84.3 & --- & 88.8 & +4.5 \\
796	GPT-2~XL temp09 & 84.0 & 85.9 & --- & 88.5 & +2.6 \\
797	GPT-2~XL top-$k$50 & 72.1 & 75.8 & --- & 79.1 & +3.3 \\
798	\midrule
799	\textbf{9-cell mean} & \textbf{75.9} & \textbf{78.4} & \textbf{78.1} & \textbf{82.6} & \textbf{+4.2} \\
800	\bottomrule
801	\end{tabular}}
802	\end{table}
803	
804	\paragraph{Strategy-dependent complementarity.}
805	The merged improvement varies by decoding strategy: nucleus and temperature cells gain +4.7\,pp on average, while top-k cells gain +3.2\,pp.
806	Top-k sampling truncates the token distribution to the $k$ highest-probability tokens, producing text with reduced distributional diversity; this limits the information available to cross-model divergence features, which rely on disagreement between observer and performer predictions.
807	Merged improvement also varies by generator family: OLMo cells (observer-dissimilar) gain +5.1\,pp on average, compared to +3.9\,pp for Pythia (observer-similar) and +3.5\,pp for GPT-2~XL, suggesting cross-model divergence features contribute more when observer and generator architectures differ.
808	
809	\paragraph{Cross-scale Binoculars ablation (14B).}
810	We evaluate Binoculars cross-scale on two representative strategies (temperature, top-$k$); the nucleus cell was used for the main 14B pipeline and its GPU hours were allocated to generation rather than Binoculars evaluation.
811	At 14B, when only 1--1.5B reference models are available for cross-perplexity computation (Pythia-1.4B observer analyzing Qwen2.5-14B text), Binoculars features degrade substantially (Table~\ref{tab:bino_14b_ablation}).
812	Self-reference statistical features (19-feat) outperform Binoculars (11-feat) by 8--11\,pp, reversing the near-parity observed at 1--1.5B.
813	Merging all 30 features yields a consistent +3.6--3.7\,pp gain over the self-reference baseline across both tested strategies, confirming that cross-perplexity features retain complementary signal even under the 10$\times$ scale gap---though the gain is attenuated relative to +4.2\,pp at 1--1.5B.
814	
815	\begin{table}[h]
816	\centering
817	\small
818	\caption{Feature ablation at 14B (Qwen2.5-14B, self-reference$^\dagger$). Binoculars: observer=Pythia-1.4B, performer=Pythia-410M. $\Delta$: merged minus main-pipeline stat-only accuracy (Method~A alignment). Chance = 25\%.}
819	\label{tab:bino_14b_ablation}
820	\begin{tabular}{@{}lcccc@{}}
821	\toprule
822	Strategy & Bino-11 & Stat-19$^\dagger$ & Merged-30 & $\Delta$ \\
823	\midrule
824	temp09 & 42.6 & 50.5 & 54.2 & +3.7 \\
825	top-$k$50 & 37.7 & 47.9 & 51.5 & +3.6 \\
826	\bottomrule
827	\end{tabular}
828	\end{table}
829	
830	The Binoculars degradation reflects a practical deployment constraint: the 10$\times$ scale gap between observer (1.4B) and generator (14B) causes cross-perplexity features to lose sensitivity, not a fundamental limitation of the cross-model divergence channel.
831	Self-reference features are more robust across scales because they avoid the observer--generator mismatch.
832	The accuracy difference between self-reference (50.8\%) and Binoculars stat-only (40.1\% mean) may therefore partially reflect observer capacity limitations rather than feature design differences.
833	
834	\subsection{Prompted Generation Results}
835	\label{app:prompted_gen}
836	
837	Table~\ref{tab:prompted_gen} reports depth estimation performance under topic-seeded (prompted) generation using GPT-2~XL with nucleus sampling ($p{=}0.95$, depths 0--3).
838	Generation is conditioned on Wikipedia topic prompts rather than a bare BOS token, a more ecologically valid test of depth signal persistence.
839	
840	\begin{table}[h]
841	\centering
842	\small
843	\caption{Prompted generation (GPT-2~XL, nucleus $p{=}0.95$, topic-seeded). 5-fold CV accuracy and pairwise AUC. Chance = 25\%.}
844	\label{tab:prompted_gen}
845	\begin{tabular}{@{}lc@{}}
846	\toprule
847	Metric & Value \\
848	\midrule
849	4-class accuracy (\%) & 69.52 $[68.9, 70.2]$ \\
850	BOS-seeded baseline (\%) & 83.3 \\
851	$\Delta$ (prompted $-$ BOS) & $-$13.78\,pp \\
852	\midrule
853	AUC d0v1 & 0.916 \\
854	AUC d1v2 & 0.782 \\
855	AUC d2v3 & 0.744 \\
856	\midrule
857	Top-1 feature & \texttt{p90\_ppl} \\
858	Top-2 feature & \texttt{var\_surprisal} \\
859	Top-3 feature & \texttt{p75\_ppl} \\
860	\bottomrule
861	\end{tabular}
862	\end{table}
863	
864	The 13.8\,pp drop relative to BOS-seeded generation is expected: topic prompts constrain the output distribution, reducing the variance that distinguishes depths.
865	Nevertheless, accuracy remains $2.8\times$ chance and pairwise AUC decays monotonically (0.916, 0.782, 0.744); the depth signal is therefore not an artifact of unconstrained generation.
866	Top features are identical to BOS-seeded (\texttt{p90\_ppl} first); the same perplexity tail erosion mechanism operates under prompted conditions.
867	
868	\subsection{Extended Discussion}
869	\label{app:extended_discussion}
870	
871	\paragraph{Cross-strategy conditional decomposition.}
872	The two-stage pipeline (strategy identification followed by depth classification) recovers 11.5\,pp over the na\"ive pooled classifier.
873	Under correct strategy routing, four-class accuracy reaches 72.6\% vs.\ 68.0\% under misrouting ($N{=}103{,}498$ / $76{,}502$), a gap of 4.6\,pp; d0 accuracy remains near-ceiling (${\sim}99.6$\%) regardless of routing, confirming that the d0 signal is strategy-invariant.
874	Even the worst routing yields a floor of 67.6\% ($2.7\times$ chance), and the 31.5\,pp d1--d3 gap between correct and wrong routing confirms feature-space misalignment rather than uniform noise.
875	End-to-end PLMs lag RF by ${\sim}20$\,pp, suggesting that current pretrained representations do not capture the distributional tail statistics that drive depth discrimination.
876	
877	\paragraph{Depth-graduated curation (inconclusive).}
878	Initial curation experiments remain inconclusive: RF-vs-unfiltered is not significant ($p>0.4$; Appendix~\ref{app:curation_poc}).
879	
880	\paragraph{Toward a provenance toolkit.}
881	Depth estimation complements existing provenance methods along orthogonal axes.
882	Watermarking \cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
883	Source attribution \cite{uchendu2020_attribution} identifies the generating model but not the generation history.
884	Depth estimation characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
885	A layered provenance system combining these three signals (watermark presence, source model, and recursive generation depth) could support more nuanced data auditing than any single method.
886	
887	\subsection{Computational Resources and Reproducibility}
888	\label{app:compute}
889	
890	\paragraph{Hardware.}
891	All experiments were conducted on 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) GPUs locally and 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) on cloud instances.
892	Total computation is approximately 200 GPU$\cdot$hours, covering the $3 \times 3$ generation matrix (LoRA fine-tuning + sampling at each depth), feature extraction, depth extension to d5, 7--14B QLoRA experiments, and all ablations.
893	
894	\paragraph{Software.}
895	Key library versions: PyTorch 2.10.0+cu128, Transformers 5.8.1, PEFT 0.7.1, scikit-learn 1.8.0.
896	Additional dependencies: Accelerate 1.13.0, Datasets 4.8.4, XGBoost 3.2.0, NumPy 2.2.6 (Python 3.12.3, CUDA 12.8).
897	
898	\paragraph{Hyperparameters.}
899	LoRA hyperparameters ($r{=}16$, $\alpha{=}32$, dropout $0.05$, lr $2{\times}10^{-4}$, batch size 8, 3 epochs) follow \citet{hu2022lora}.
900	The Random Forest classifier uses 200 trees, Gini criterion, and no max depth, without hyperparameter search; all reported results use 5-fold stratified cross-validation.
901	
902	\paragraph{Inference cost.}
903	Feature extraction requires a single forward pass of the reference model.
904	On a single GPU this takes approximately 2 minutes for 5{,}000 passages; a CPU-only alternative requires approximately 50 minutes on server-grade hardware.
905	RF classification adds negligible overhead ($<$1\,s).
906	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fad61388-2956-4bab-a216-193d8b1e7feb",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "fed7fb0b-b4f2-4ba5-aec2-737465739a3b",
  "sourceToolAssistantUUID": "fad61388-2956-4bab-a216-193d8b1e7feb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-21T11:20:20.958Z_

Now let me search for specific mentions of "44.1", "cross-reference", "cross_reference", or "14B" in the appendix:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fed7fb0b-b4f2-4ba5-aec2-737465739a3b",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdBFbby66QowFb9Tgjt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "650784f3-5c9d-4543-acc8-346e6392cc97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MENJNSdRPFsDBmmRF3wra1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 24156,
      "cache_read_input_tokens": 41189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24156,
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

_source line 9 · 2026-05-21T11:20:22.386Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016gPvUTy8e3c2fpgYiFntAp`</summary>

```json
{
  "pattern": "(44\\.1|cross.?reference|Pythia-1\\.4B.*14B|Qwen2\\.5-14B.*cross)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "650784f3-5c9d-4543-acc8-346e6392cc97",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdBFbby66QowFb9Tgjt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c5459ae8-57f3-4b9d-a87a-998933bb8abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MENJNSdRPFsDBmmRF3wra1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 24156,
      "cache_read_input_tokens": 41189,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24156
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 203,
          "cache_read_input_tokens": 41189,
          "cache_creation_input_tokens": 24156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24156,
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

_source line 10 · 2026-05-21T11:20:22.408Z_

<details><summary>↩ Tool result · `toolu_016gPvUTy8e3c2fpgYiFntAp`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-8-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-9-\paragraph{Scale and generalization boundaries.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-10-The primary benchmark uses 1--1.5B parameter models with controlled LoRA fine-tuning.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex:11:At 14B, cross-reference accuracy drops to 44.1\% with $\mathrm{EDD}_{0.70}{=}2$ (nucleus/temperature); reference-model choice accounts for ${\sim}$7\,pp of the apparent degradation, and the remaining signal attenuation constitutes a scale-dependent boundary for the current feature set.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-12-Cross-strategy transfer drops d1--d3 accuracy to 45.9\%, and on web-crawl data (C4) false positive rates reach 22\%; these gaps narrow with confidence thresholding and strategy-aware pipelines but are not fully resolved.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-13-Additional caveats (reference model dependency, ${\leq}$11\,pp; single LoRA seed, ${\sim}$1--3\,pp uncertainty; adversarial robustness; passage length sensitivity) are detailed in the Appendix.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-14-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex-4-Depth signal concentrates in perplexity tails because recursive training shifts the bulk distribution only gradually; erosion appears first in upper quantiles \cite{dohmatob2024_tale_of_tails}.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex-5-The strategy effect (9.3\,pp) exceeding the model effect (7.2\,pp) implies auditing pipelines must account for decoding configuration.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex:6:Full-replacement chains provide the discriminability ceiling (d1--d3: 59--82\%); pilot accumulation ($-$14 to $-$15\,pp) and 14B cross-reference ($\mathrm{EDD}_{0.70}$: 0${\to}$2, ${\sim}$7\,pp reference-model artifact) confirm signal survives but attenuates with mixing and scale.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex-12-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex-13-\paragraph{Scale-dependent attenuation.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex-14-Larger models approximate the training distribution more faithfully per step ($\alpha$ closer to 1), so EDD should decrease with scale.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex:15:Qwen2.5-14B confirms this: d0-vs-d1 AUC drops to 0.643 (vs.\ ${>}0.99$ at 1--1.5B), while d1--d3 AUCs remain above 0.70 (\S\ref{sec:gen:crossscale}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex-16-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex-17-\paragraph{Strategy-dependent convergence.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex-18-The contraction rate $\alpha$ varies with decoding strategy.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-111-\subsection{Preliminary Cross-Scale Observations (14B)}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-112-\label{sec:gen:crossscale}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-113-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:114:At 14B (Qwen2.5-14B), self-reference yields 50.8\% ($2{\times}$ chance, $\mathrm{EDD}_{0.70}{=}0$); cross-reference control (Pythia-1.4B) drops accuracy to 44.1\% ($-$6.8\,pp) but raises $\mathrm{EDD}_{0.70}$ to 2 for nucleus and temperature, revealing ${\sim}$7\,pp of the apparent degradation is a reference-model artifact (Appendix~\ref{app:cross_scale_full}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-115-Cross-domain (arXiv) accuracy reaches 74.1\% at 1--1.5B; cross-domain FPR is discussed in Limitations.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-377-We extend the benchmark to two 7--8B models (Qwen2.5-7B-Instruct \cite{qwen2.5}, Llama-3.1-8B-Instruct \cite{llama3}) and one 14B model (Qwen2.5-14B).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-378-The 7--8B models use 4-bit NF4 QLoRA fine-tuning with nucleus sampling ($p{=}0.95$, 500 samples per depth, depths $d \in \{0, 1, \ldots, 5\}$).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-379-The 14B model uses clean FP16 LoRA fine-tuning across all three decoding strategies (nucleus, temperature $\tau{=}0.9$, top-$k$ $k{=}50$; 5{,}000 samples per depth, depths $d \in \{0, 1, 2, 3\}$).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:380:Feature extraction for 1--8B models uses Pythia-1.4B as reference; Qwen2.5-14B uses self-reference (the 14B model computes its own perplexity features), a choice that precludes direct comparison with the Pythia-referenced pipeline (see confounds below).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-381-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-382-\paragraph{Scale comparison.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-383-Table~\ref{tab:cross_scale} contrasts the 7--14B models with the three 1--1.5B models on matched evaluation (depths 0--3).
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-461-The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-462-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-463-\paragraph{(4) Signal attenuation at 14B.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:464:Qwen2.5-14B (clean FP16, self-reference) is tested across all three decoding strategies (Table~\ref{tab:cross_scale}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-465-Mean four-class accuracy is 50.8\% ($2.0{\times}$ chance), with nucleus 54.1\%, temperature 50.5\%, and top-$k$ 47.9\%.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-466-$\mathrm{EDD}_{0.70}{=}0$ across all three strategies: no adjacent-depth pair reaches the 0.70 AUC threshold.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-467-The d0/d1 boundary, near-perfect at 1--1.5B (AUC ${>}0.99$), attenuates to 0.56--0.64 at 14B.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-641-The top-5 features shift substantially: \texttt{surprisal\_range}, \texttt{surprisal\_position\_corr}, \texttt{prob\_std}, \texttt{surprisal\_first\_half\_minus\_second}, and \texttt{surprisal\_std} replace the perplexity tail statistics (\texttt{p90\_ppl}, \texttt{var\_surprisal}) that dominate in base models.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-642-This feature shift suggests instruction tuning compresses the perplexity distribution (reducing tail discriminability) while preserving positional and range-based surprisal patterns.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-643-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:644:Two caveats apply: (1) self-reference evaluation may inflate or deflate accuracy relative to cross-reference evaluation (cf.\ \S\ref{app:ref_ablation}); (2) a single instruction-tuned model does not establish the generality of the feature shift across architectures or instruction-tuning recipes.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-645-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-646-\subsection{Downstream Fine-Tuning Probe (Inconclusive)}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-647-\label{app:downstream}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-808-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-809-\paragraph{Cross-scale Binoculars ablation (14B).}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-810-We evaluate Binoculars cross-scale on two representative strategies (temperature, top-$k$); the nucleus cell was used for the main 14B pipeline and its GPU hours were allocated to generation rather than Binoculars evaluation.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:811:At 14B, when only 1--1.5B reference models are available for cross-perplexity computation (Pythia-1.4B observer analyzing Qwen2.5-14B text), Binoculars features degrade substantially (Table~\ref{tab:bino_14b_ablation}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-812-Self-reference statistical features (19-feat) outperform Binoculars (11-feat) by 8--11\,pp, reversing the near-parity observed at 1--1.5B.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-813-Merging all 30 features yields a consistent +3.6--3.7\,pp gain over the self-reference baseline across both tested strategies, confirming that cross-perplexity features retain complementary signal even under the 10$\times$ scale gap---though the gain is attenuated relative to +4.2\,pp at 1--1.5B.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-814-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex-2-As language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex-3-We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a 180K-passage benchmark spanning three model families, three decoding strategies, and four depths under controlled full-replacement chains at the 1--1.5B parameter scale.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex-4-A lightweight pipeline (19 statistical features dominated by perplexity tail statistics, classified by Random Forest) achieves d1--d3 balanced accuracy of 59--82\% across nine model--strategy cells, with the \emph{Effective Discriminable Depth} ($\mathrm{EDD}_{0.70}$) reaching 4 for all three families.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex-6-Perturbation-based and membership-inference baselines (29--33\%) confirm that binary detection scores lack ordinal depth resolution.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex-7-\end{abstract}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-27-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-28-    \item \textbf{Depth Degradation Atlas.} The perplexity tail feature family dominates depth discrimination across all 9 cells; $\mathrm{EDD}_{0.70}{=}4$ for all three families, validated by 5-class extension (71--80\%); feature group ablation confirms perplexity tail dominance (76.6\% alone vs.\ 78.4\% full set).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-29-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:30:    \item \textbf{Systematic characterization.} Cross-model transfer 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, preliminary 14B 44.1\% cross-reference ($\mathrm{EDD}_{0.70}{=}2$). We identify cross-strategy transfer (d1--d3: 45.9\%) as a boundary condition: decoding strategies induce qualitatively distinct degradation trajectories, with strategy affecting transfer more than model architecture.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-31-\end{itemize}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex-13-\label{sec:gen:crossscale}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex-14-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex-15-At 7--8B (QLoRA), Llama-3.1-8B \cite{llama3} achieves 70.2\% (QLoRA, instruct-tuned) ($\mathrm{EDD}_{0.70}{=}4$) and Qwen2.5-7B \cite{qwen2.5} 60.1\%.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:16:At 14B (Qwen2.5-14B), depth signal persists across all three strategies: nucleus 54.1\%, temperature \TEMPACCURACY{}\%, top-$k$ \TOPKACCURACY{}\% (chance = 25\%).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex-17-The strategy ranking %% [check: does it match 1-1.5B? If yes use next line, if no use the alternative]
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex-18-mirrors the 1--1.5B atlas ordering, confirming that strategy-dependent attenuation patterns generalize across scale.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex-19-%% Alternative if ranking differs:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5459ae8-57f3-4b9d-a87a-998933bb8abe",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "a7a3a989-5621-4fdb-8881-186060b78df1",
  "sourceToolAssistantUUID": "c5459ae8-57f3-4b9d-a87a-998933bb8abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T11:20:24.885Z_

Good! Now let me look more closely at the main table showing the 14B results (Table 17 mentioned, and the cross-reference control):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7a3a989-5621-4fdb-8881-186060b78df1",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdBYXanWkS7YNWFuiEC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c3d8a0d-afe8-4a95-ac73-884552aeaadc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WF4FDmsS1pixqLZZx9e3a9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 5787,
      "cache_read_input_tokens": 65345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5787,
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

_source line 12 · 2026-05-21T11:20:25.708Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Xwd5V3KR88gqAAsVCDLctS`</summary>

```json
{
  "pattern": "tab:cross_scale|Table.*17|tab:bino_14b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c3d8a0d-afe8-4a95-ac73-884552aeaadc",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdBYXanWkS7YNWFuiEC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "89f8fa3c-087b-4324-8635-45f37a31648a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WF4FDmsS1pixqLZZx9e3a9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 5787,
      "cache_read_input_tokens": 65345,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5787
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 193,
          "cache_read_input_tokens": 65345,
          "cache_creation_input_tokens": 5787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5787,
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

_source line 13 · 2026-05-21T11:20:25.731Z_

<details><summary>↩ Tool result · `toolu_01Xwd5V3KR88gqAAsVCDLctS`</summary>

```text
378-The 7--8B models use 4-bit NF4 QLoRA fine-tuning with nucleus sampling ($p{=}0.95$, 500 samples per depth, depths $d \in \{0, 1, \ldots, 5\}$).
379-The 14B model uses clean FP16 LoRA fine-tuning across all three decoding strategies (nucleus, temperature $\tau{=}0.9$, top-$k$ $k{=}50$; 5{,}000 samples per depth, depths $d \in \{0, 1, 2, 3\}$).
380-Feature extraction for 1--8B models uses Pythia-1.4B as reference; Qwen2.5-14B uses self-reference (the 14B model computes its own perplexity features), a choice that precludes direct comparison with the Pythia-referenced pipeline (see confounds below).
381-
382-\paragraph{Scale comparison.}
383:Table~\ref{tab:cross_scale} contrasts the 7--14B models with the three 1--1.5B models on matched evaluation (depths 0--3).
384-The 14B model is tested across all three decoding strategies; the 7--8B models use nucleus sampling only.
385-
386-\begin{table}[h]
387-\centering
388-\small
389-\caption{Cross-scale comparison: 4-class RF accuracy (\%, depths 0--3), $\mathrm{EDD}_{T{=}0.70}$, and d0-vs-d1 AUC. CI: 95\% bootstrap. Chance = 25\%. $^\dagger$Self-reference model (see text).}
390:\label{tab:cross_scale}
391-\resizebox{\columnwidth}{!}{%
392-\begin{tabular}{@{}llccc@{}}
393-\toprule
394-Model & Strategy & 4-class acc & $\mathrm{EDD}_{0.70}$ & d0v1 \\
395-\midrule
--
412-\paragraph{(1) Depth signal persists at 7--8B scale.}
413-Both 7--8B models substantially exceed the 25\% chance baseline: Llama-3.1-8B achieves 70.2\% (95\% CI $[68.3, 72.4]$) and Qwen2.5-7B achieves 60.1\% ($[58.0, 62.1]$); recursive depth therefore remains estimable from perplexity-based features even when the generator is 5--7$\times$ larger than the reference model.
414-Depth-0 separability is preserved in both models: d0v1 AUC is 0.949 (Llama-3.1) and 0.969 (Qwen2.5).
415-
416-\paragraph{(2) EDD at 7--8B scale.}
417:At threshold $T{=}0.70$, Qwen2.5-7B maintains all consecutive-pair AUCs above 0.70 through depth~5 (Table~\ref{tab:cross_scale_auc}), yielding $\mathrm{EDD}_{T{=}0.70} > 5$, exceeding the $\mathrm{EDD}{=}4$ observed at 1--1.5B.
418-Llama-3.1-8B matches the smaller models at $\mathrm{EDD}{=}4$: its monotonic decay causes d4v5 (0.618) to drop below $T$, despite stronger signal at shallower depths.
419-Both larger generators produce weaker per-step signal than the 1--1.5B models (mean consecutive AUC: 0.786 for Llama-3.1, 0.782 for Qwen2.5, vs.\ 0.852 at 1--1.5B).
420-
421-\begin{table}[h]
422-\centering
423-\small
424-\caption{Consecutive binary AUC. Llama-3.1-8B exhibits monotonic decay; Qwen2.5-7B shows a U-shaped pattern; Qwen2.5-14B$^\dagger$ (depths 0--3 only) has all pairs below $T{=}0.70$ with strategy-specific patterns. $^\dagger$Self-reference model.}
425:\label{tab:cross_scale_auc}
426-\resizebox{\columnwidth}{!}{%
427-\begin{tabular}{@{}llccccc@{}}
428-\toprule
429-Model & Strategy & d0v1 & d1v2 & d2v3 & d3v4 & d4v5 \\
430-\midrule
--
437-\bottomrule
438-\end{tabular}}
439-\end{table}
440-
441-\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}
442:Among instruction-tuned models, Llama-3.1-8B exhibits monotonic AUC decay consistent with the 1--1.5B pattern, while Qwen2.5-7B shows a U-shaped recovery beyond d2v3 (Table~\ref{tab:cross_scale_auc}).
443-A base-model control (Llama-3.1-8B without instruction tuning) clarifies the causal direction: the base model achieves 59.9\% four-class accuracy (95\% CI [57.8, 62.15], $\mathrm{EDD}_{0.70}{=}2$) with non-monotonic AUC decay (Table~\ref{tab:llama3_base_auc}), while the instruction-tuned variant reaches 70.2\% with strictly monotonic decay.
444-The base-model control experiment suggests instruction-tuning regularizes rather than confounds the depth signal.
445-
446-\begin{table}[h]
447-\centering
--
459-\end{table}
460-
461-The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.
462-
463-\paragraph{(4) Signal attenuation at 14B.}
464:Qwen2.5-14B (clean FP16, self-reference) is tested across all three decoding strategies (Table~\ref{tab:cross_scale}).
465-Mean four-class accuracy is 50.8\% ($2.0{\times}$ chance), with nucleus 54.1\%, temperature 50.5\%, and top-$k$ 47.9\%.
466-$\mathrm{EDD}_{0.70}{=}0$ across all three strategies: no adjacent-depth pair reaches the 0.70 AUC threshold.
467-The d0/d1 boundary, near-perfect at 1--1.5B (AUC ${>}0.99$), attenuates to 0.56--0.64 at 14B.
468-
469:Each strategy produces a structurally distinct adjacent-pair AUC pattern (Table~\ref{tab:cross_scale_auc}):
470-nucleus is monotonically increasing (d0v1=0.643 $<$ d1v2=0.713 $<$ d2v3=0.728);
471-temperature exhibits d2v3 collapse (0.618, the weakest boundary) because temperature scaling uniformly amplifies logit differences, accelerating convergence to the attractor distribution at deeper depths;
472-top-$k$ exhibits d0v1 collapse (0.561, the weakest boundary) because vocabulary truncation constrains d0 and d1 distributions to the same top-$k$ tokens, compressing their statistical distance.
473-This three-way divergence confirms at 14B that different decoding strategies induce structurally distinct degradation trajectories (\S\ref{sec:gen:crossstrategy}).
474-
--
806-Top-k sampling truncates the token distribution to the $k$ highest-probability tokens, producing text with reduced distributional diversity; this limits the information available to cross-model divergence features, which rely on disagreement between observer and performer predictions.
807-Merged improvement also varies by generator family: OLMo cells (observer-dissimilar) gain +5.1\,pp on average, compared to +3.9\,pp for Pythia (observer-similar) and +3.5\,pp for GPT-2~XL, suggesting cross-model divergence features contribute more when observer and generator architectures differ.
808-
809-\paragraph{Cross-scale Binoculars ablation (14B).}
810-We evaluate Binoculars cross-scale on two representative strategies (temperature, top-$k$); the nucleus cell was used for the main 14B pipeline and its GPU hours were allocated to generation rather than Binoculars evaluation.
811:At 14B, when only 1--1.5B reference models are available for cross-perplexity computation (Pythia-1.4B observer analyzing Qwen2.5-14B text), Binoculars features degrade substantially (Table~\ref{tab:bino_14b_ablation}).
812-Self-reference statistical features (19-feat) outperform Binoculars (11-feat) by 8--11\,pp, reversing the near-parity observed at 1--1.5B.
813-Merging all 30 features yields a consistent +3.6--3.7\,pp gain over the self-reference baseline across both tested strategies, confirming that cross-perplexity features retain complementary signal even under the 10$\times$ scale gap---though the gain is attenuated relative to +4.2\,pp at 1--1.5B.
814-
815-\begin{table}[h]
816-\centering
817-\small
818-\caption{Feature ablation at 14B (Qwen2.5-14B, self-reference$^\dagger$). Binoculars: observer=Pythia-1.4B, performer=Pythia-410M. $\Delta$: merged minus main-pipeline stat-only accuracy (Method~A alignment). Chance = 25\%.}
819:\label{tab:bino_14b_ablation}
820-\begin{tabular}{@{}lcccc@{}}
821-\toprule
822-Strategy & Bino-11 & Stat-19$^\dagger$ & Merged-30 & $\Delta$ \\
823-\midrule
824-temp09 & 42.6 & 50.5 & 54.2 & +3.7 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89f8fa3c-087b-4324-8635-45f37a31648a",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "4c11a981-21e2-41f0-b274-95ebb661535b",
  "sourceToolAssistantUUID": "89f8fa3c-087b-4324-8635-45f37a31648a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-21T11:20:28.345Z_

Perfect! Now I can see the key information. Let me verify what's stated about the cross-reference control by looking at the introduction section again and the generalization section more carefully:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c11a981-21e2-41f0-b274-95ebb661535b",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdBnkqrVnjL2s6P79hc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "672911eb-9dcd-4f0d-a740-b43f17aa8695",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LjXt8BdDffgserahiGLG7r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 71132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2917,
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

_source line 15 · 2026-05-21T11:20:29.212Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QhMLJKGVvSLUUpBsaNV7s4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
  "offset": 100,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "672911eb-9dcd-4f0d-a740-b43f17aa8695",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdBnkqrVnjL2s6P79hc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "10c7302d-5982-44b0-b14c-fa1142613cc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LjXt8BdDffgserahiGLG7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 71132,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 162,
          "cache_read_input_tokens": 71132,
          "cache_creation_input_tokens": 2917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2917,
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

_source line 16 · 2026-05-21T11:20:29.219Z_

<details><summary>↩ Tool result · `toolu_01QhMLJKGVvSLUUpBsaNV7s4`</summary>

```text
100	temp ($\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\
101	top-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	Cross-strategy transfer reveals a structural barrier: d1--d3 balanced accuracy drops to 45.9\% (four-class: 59.1\%), 7\,pp below cross-model transfer (Table~\ref{tab:cross_strategy}).
107	Decoding strategies induce qualitatively distinct degradation trajectories; a two-stage pipeline recovers 11.5\,pp but presupposes known strategy (Appendix~\ref{app:extended_discussion}).
108	Our depth estimation claims hold most strongly within-strategy or when the decoding configuration is known.
109	
110	%% ----------------------------------------------------------------
111	\subsection{Preliminary Cross-Scale Observations (14B)}
112	\label{sec:gen:crossscale}
113	
114	At 14B (Qwen2.5-14B), self-reference yields 50.8\% ($2{\times}$ chance, $\mathrm{EDD}_{0.70}{=}0$); cross-reference control (Pythia-1.4B) drops accuracy to 44.1\% ($-$6.8\,pp) but raises $\mathrm{EDD}_{0.70}$ to 2 for nucleus and temperature, revealing ${\sim}$7\,pp of the apparent degradation is a reference-model artifact (Appendix~\ref{app:cross_scale_full}).
115	Cross-domain (arXiv) accuracy reaches 74.1\% at 1--1.5B; cross-domain FPR is discussed in Limitations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10c7302d-5982-44b0-b14c-fa1142613cc0",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "36331eb7-64ba-4c99-9398-e4c74f0a5a17",
  "sourceToolAssistantUUID": "10c7302d-5982-44b0-b14c-fa1142613cc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-21T11:20:31.827Z_

Excellent! Now let me check if there's any dedicated table or section showing the cross-reference control breakdown with per-strategy results for the 44.1% result:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36331eb7-64ba-4c99-9398-e4c74f0a5a17",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdC3nyCcLAFVyTLfAaj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "78858d27-2fd0-45f6-acfc-5432ecf88916",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012ce53aQnFRXY5Sd4jw6ond",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 74049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 746,
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

_source line 18 · 2026-05-21T11:20:32.409Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QJUNmK63V8HEK8GnpLPTrZ`</summary>

```json
{
  "command": "grep -n \"44.1\\|cross.reference\\|Pythia.*14B\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78858d27-2fd0-45f6-acfc-5432ecf88916",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdC3nyCcLAFVyTLfAaj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "53b71dae-97eb-4bcc-acae-edfdbba6e323",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012ce53aQnFRXY5Sd4jw6ond",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 74049,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 746
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 153,
          "cache_read_input_tokens": 74049,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 746,
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

_source line 19 · 2026-05-21T11:20:32.476Z_

<details><summary>↩ Tool result · `toolu_01QJUNmK63V8HEK8GnpLPTrZ`</summary>

```text
380:Feature extraction for 1--8B models uses Pythia-1.4B as reference; Qwen2.5-14B uses self-reference (the 14B model computes its own perplexity features), a choice that precludes direct comparison with the Pythia-referenced pipeline (see confounds below).
644:Two caveats apply: (1) self-reference evaluation may inflate or deflate accuracy relative to cross-reference evaluation (cf.\ \S\ref{app:ref_ablation}); (2) a single instruction-tuned model does not establish the generality of the feature shift across architectures or instruction-tuning recipes.
811:At 14B, when only 1--1.5B reference models are available for cross-perplexity computation (Pythia-1.4B observer analyzing Qwen2.5-14B text), Binoculars features degrade substantially (Table~\ref{tab:bino_14b_ablation}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53b71dae-97eb-4bcc-acae-edfdbba6e323",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "e307340a-ef29-4bd3-80ce-0900135f92ac",
  "sourceToolAssistantUUID": "53b71dae-97eb-4bcc-acae-edfdbba6e323",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-21T11:20:34.643Z_

Let me check the confounds section more carefully to see if there's a table with cross-reference results:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e307340a-ef29-4bd3-80ce-0900135f92ac",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdCHaCEMMfgrAtqUmts",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c37400d-2313-4ec9-b720-87de197662a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KViCF1966ZwRLUoURiwuSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 391,
      "cache_read_input_tokens": 74795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 391,
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

_source line 21 · 2026-05-21T11:20:34.890Z_

<details open><summary>🔧 Tool call — Read · `toolu_0144f4NbL1LKVWKSVrvehgr9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 479,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c37400d-2313-4ec9-b720-87de197662a8",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdCHaCEMMfgrAtqUmts",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "68d447c0-d9dd-485d-a8eb-5edb15968891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KViCF1966ZwRLUoURiwuSe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 391,
      "cache_read_input_tokens": 74795,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 391
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 149,
          "cache_read_input_tokens": 74795,
          "cache_creation_input_tokens": 391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 391,
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

_source line 22 · 2026-05-21T11:20:34.902Z_

<details><summary>↩ Tool result · `toolu_0144f4NbL1LKVWKSVrvehgr9`</summary>

```text
479	\paragraph{Caveats.}
480	For Qwen2.5-7B, the CI lower bound (58.0\%) does not exclude sub-60\% accuracy; Llama-3.1-8B's lower bound (68.3\%) is more comfortably above chance but still below the 75--83\% range at 1--1.5B.
481	The divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.
482	
483	\paragraph{Confounds.}
484	\label{app:cross_scale_confounds}
485	Four confounds limit the 7--8B results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling at 7--8B (the 14B model addresses this with all three strategies); (4)~vocabulary mismatch between larger generators and the 1.4B reference model.
486	For the 14B model specifically: self-reference rather than the Pythia-1.4B reference used for all other experiments prevents direct cross-scale comparison.
487	The base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.
488	The remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution); it is therefore infeasible to attribute the observed accuracy gap (60--70\% vs.\ 78--85\% at 1--1.5B) to any single factor.
489	
490	\subsection{Cross-Boundary Generalization}
491	\label{app:cross_boundary}
492	
493	The preceding experiments assume a single model family generates all recursive depths.
494	In practice, recursive contamination may traverse model boundaries: text generated by model~A is used to train model~B, whose output trains model~C.
495	We probe whether the depth signal persists under two relaxations of the single-model assumption.
496	
497	\paragraph{Cross-model recursive chains.}
498	We construct a heterogeneous chain: human text (d0) $\to$ Pythia-1.4B generates d1 $\to$ OLMo-1B finetuned on Pythia-d1 generates d2 $\to$ GPT-2~XL finetuned on OLMo-d2 generates d3.
499	Each recursive step uses a \emph{different} model family, eliminating the possibility that depth signal arises from a single model's idiosyncratic behavior.
500	A 4-class Random Forest achieves 84.75\% accuracy (95\% CI $[81.0, 88.25]$), with per-depth F1 scores of 0.98 (d0), 0.88 (d1), 0.76 (d2), and 0.76 (d3).
501	Pairwise AUC remains high: d0-vs-d1 = 0.999 and d2-vs-d3 = 0.841.
502	These results suggest that distributional artifacts of recursive generation persist across model boundaries. This constitutes preliminary evidence for a process-level depth signal rather than individual generator artifacts.
503	
504	\paragraph{Confound discussion.}
505	The heterogeneous chain confounds architecture identity with depth (d1=Pythia, d2=OLMo, d3=GPT-2~XL).
506	However, if the classifier exploited architecture fingerprints rather than depth signal, near-perfect accuracy would be expected since architecture perfectly determines depth label.
507	The observed 84.75\% with monotonically decreasing per-depth F1 (d0=0.98, d1=0.88, d2=0.76, d3=0.76) is more consistent with a depth-signal interpretation, as architecture fingerprinting would not produce this graded pattern.
508	We address this confound directly with a reverse-chain control below.
509	
510	\paragraph{Reverse-chain control.}
511	To empirically test the architecture confound hypothesis, we constructed a reverse chain (GPT-2~XL $\to$ OLMo $\to$ Pythia) reversing the model-depth assignment.
512	The reverse chain achieves 85.75\% (95\% CI [82.0, 89.25]), statistically indistinguishable from the forward chain (84.75\%, [81.0, 88.25]).
513	If the classifier exploited architecture fingerprints rather than depth signal, reversing the chain should invert depth predictions; the equivalent accuracy under both orderings provides empirical evidence against the architecture confound.
514	
515	\paragraph{Cross-domain transfer.}
516	All prior experiments use WikiText-103 as the seed corpus.
517	To test domain dependence, we repeat the pipeline with arXiv abstracts as the seed text (Pythia-1.4B, nucleus $p{=}0.95$, 500 samples per depth, d0--d3).
518	Five-fold cross-validation yields 74.1\% $\pm$ 2.0\% accuracy, compared to ${\sim}$78\% on the WikiText seed.
519	Per-depth F1 shows the familiar pattern: d0 = 1.00, d1 = 0.78, d2 = 0.52, d3 = 0.66, with d2 remaining the most challenging class.
520	The 4pp accuracy gap relative to WikiText likely reflects the narrower stylistic range of scientific abstracts, which may reduce the distributional contrast between adjacent depths.
521	These results provide preliminary evidence that the perplexity-based features capture properties of the recursive generation process rather than domain-specific artifacts of the seed corpus.
522	
523	\subsection{Cross-Seed Replication}
524	\label{app:seed_replication}
525	
526	Table~\ref{tab:seed_replication} reports within-seed accuracy for all three model families (nucleus, depths 0--3) under two independent LoRA training seeds.
527	
528	\begin{table}[h]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68d447c0-d9dd-485d-a8eb-5edb15968891",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "6f893781-c459-43a1-a7a3-7cd06624acdd",
  "sourceToolAssistantUUID": "68d447c0-d9dd-485d-a8eb-5edb15968891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-21T11:20:37.737Z_

Now let me search more specifically for any table that shows 44.1% or the breakdown of the cross-reference result with per-strategy information:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f893781-c459-43a1-a7a3-7cd06624acdd",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdCU4j4DFkq4pByrc3y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4eaa1912-d026-4630-a72e-db1f654276f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VUeCazuuB9bR81fxndU2oY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1772,
      "cache_read_input_tokens": 75186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1772,
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

_source line 24 · 2026-05-21T11:20:39.187Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SNYmoRcC9rfFu3J1AP2MGy`</summary>

```json
{
  "command": "grep -A 15 \"tab:bino_14b_ablation\\|Pythia-1.4B.*observer\\|Qwen2.5-14B.*Pythia\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eaa1912-d026-4630-a72e-db1f654276f2",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdCU4j4DFkq4pByrc3y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "df75b741-9847-411c-b3f2-21a71171e778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VUeCazuuB9bR81fxndU2oY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1772,
      "cache_read_input_tokens": 75186,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1772
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 172,
          "cache_read_input_tokens": 75186,
          "cache_creation_input_tokens": 1772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1772,
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

_source line 25 · 2026-05-21T11:20:39.246Z_

<details><summary>↩ Tool result · `toolu_01SNYmoRcC9rfFu3J1AP2MGy`</summary>

```text
Feature extraction for 1--8B models uses Pythia-1.4B as reference; Qwen2.5-14B uses self-reference (the 14B model computes its own perplexity features), a choice that precludes direct comparison with the Pythia-referenced pipeline (see confounds below).

\paragraph{Scale comparison.}
Table~\ref{tab:cross_scale} contrasts the 7--14B models with the three 1--1.5B models on matched evaluation (depths 0--3).
The 14B model is tested across all three decoding strategies; the 7--8B models use nucleus sampling only.

\begin{table}[h]
\centering
\small
\caption{Cross-scale comparison: 4-class RF accuracy (\%, depths 0--3), $\mathrm{EDD}_{T{=}0.70}$, and d0-vs-d1 AUC. CI: 95\% bootstrap. Chance = 25\%. $^\dagger$Self-reference model (see text).}
\label{tab:cross_scale}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}llccc@{}}
\toprule
Model & Strategy & 4-class acc & $\mathrm{EDD}_{0.70}$ & d0v1 \\
\midrule
--
This result carries an important caveat: Qwen2.5-14B uses self-reference, whereas all other experiments use Pythia-1.4B.
Self-reference conflates the generator's distributional shift with the reference model's sensitivity; the observed attenuation may partially reflect the reference model change rather than a pure scale effect.

\paragraph{Caveats.}
For Qwen2.5-7B, the CI lower bound (58.0\%) does not exclude sub-60\% accuracy; Llama-3.1-8B's lower bound (68.3\%) is more comfortably above chance but still below the 75--83\% range at 1--1.5B.
The divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.

\paragraph{Confounds.}
\label{app:cross_scale_confounds}
Four confounds limit the 7--8B results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling at 7--8B (the 14B model addresses this with all three strategies); (4)~vocabulary mismatch between larger generators and the 1.4B reference model.
For the 14B model specifically: self-reference rather than the Pythia-1.4B reference used for all other experiments prevents direct cross-scale comparison.
The base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.
The remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution); it is therefore infeasible to attribute the observed accuracy gap (60--70\% vs.\ 78--85\% at 1--1.5B) to any single factor.

\subsection{Cross-Boundary Generalization}
\label{app:cross_boundary}
--
At 14B, when only 1--1.5B reference models are available for cross-perplexity computation (Pythia-1.4B observer analyzing Qwen2.5-14B text), Binoculars features degrade substantially (Table~\ref{tab:bino_14b_ablation}).
Self-reference statistical features (19-feat) outperform Binoculars (11-feat) by 8--11\,pp, reversing the near-parity observed at 1--1.5B.
Merging all 30 features yields a consistent +3.6--3.7\,pp gain over the self-reference baseline across both tested strategies, confirming that cross-perplexity features retain complementary signal even under the 10$\times$ scale gap---though the gain is attenuated relative to +4.2\,pp at 1--1.5B.

\begin{table}[h]
\centering
\small
\caption{Feature ablation at 14B (Qwen2.5-14B, self-reference$^\dagger$). Binoculars: observer=Pythia-1.4B, performer=Pythia-410M. $\Delta$: merged minus main-pipeline stat-only accuracy (Method~A alignment). Chance = 25\%.}
\label{tab:bino_14b_ablation}
\begin{tabular}{@{}lcccc@{}}
\toprule
Strategy & Bino-11 & Stat-19$^\dagger$ & Merged-30 & $\Delta$ \\
\midrule
temp09 & 42.6 & 50.5 & 54.2 & +3.7 \\
top-$k$50 & 37.7 & 47.9 & 51.5 & +3.6 \\
\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df75b741-9847-411c-b3f2-21a71171e778",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "9f8ab7b9-956e-45d1-b17e-a2ad8e13b47c",
  "sourceToolAssistantUUID": "df75b741-9847-411c-b3f2-21a71171e778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-21T11:20:41.307Z_

Let me search for a more comprehensive table that shows the cross-reference results in the appendix:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f8ab7b9-956e-45d1-b17e-a2ad8e13b47c",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdCnTGRPQmvqQA3xMdn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ad2aca20-30e6-4d4c-b474-a2be8dbc1a6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KbHBTBHK7v3QPMGXY8uZku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1551,
      "cache_read_input_tokens": 76958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1551,
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

_source line 27 · 2026-05-21T11:20:42.560Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WBvBZfLToapBaH1E2qKK8x`</summary>

```json
{
  "command": "grep -n \"Pythia-1.4B.*observer\\|cross.*reference\\|44.1\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad2aca20-30e6-4d4c-b474-a2be8dbc1a6f",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdCnTGRPQmvqQA3xMdn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "85c26ba1-4f96-4cf6-a9b8-c57601010cc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KbHBTBHK7v3QPMGXY8uZku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1551,
      "cache_read_input_tokens": 76958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1551,
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

_source line 28 · 2026-05-21T11:20:42.653Z_

<details><summary>↩ Tool result · `toolu_01WBvBZfLToapBaH1E2qKK8x`</summary>

```text
636:To test whether instruction tuning eliminates depth signal at matched scale (1.5B, avoiding the quantization confound of \S\ref{sec:gen:crossscale}), we run the full recursive pipeline on Qwen2.5-1.5B-Instruct with self-reference feature extraction (i.e., the same model serves as both generator and reference).
644:Two caveats apply: (1) self-reference evaluation may inflate or deflate accuracy relative to cross-reference evaluation (cf.\ \S\ref{app:ref_ablation}); (2) a single instruction-tuned model does not establish the generality of the feature shift across architectures or instruction-tuning recipes.
811:At 14B, when only 1--1.5B reference models are available for cross-perplexity computation (Pythia-1.4B observer analyzing Qwen2.5-14B text), Binoculars features degrade substantially (Table~\ref{tab:bino_14b_ablation}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85c26ba1-4f96-4cf6-a9b8-c57601010cc6",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "17e9c12d-ab45-4a8e-ace6-be145076b56e",
  "sourceToolAssistantUUID": "85c26ba1-4f96-4cf6-a9b8-c57601010cc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T11:20:45.004Z_

Now let me search in the entire paper directory for any table that explicitly shows 44.1% with per-strategy breakdown:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17e9c12d-ab45-4a8e-ace6-be145076b56e",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdD3QvZhthr8BnNiQ8H",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ede024f9-ca3a-462b-8e3b-9c8277971183",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y5x6woNuU9rvo1LczPVUbb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 386,
      "cache_read_input_tokens": 78509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 386,
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

_source line 30 · 2026-05-21T11:20:45.223Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UAg6pWzicCZaHzPHQjkHu4`</summary>

```json
{
  "command": "grep -r \"44.1\\|44\\.1\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ede024f9-ca3a-462b-8e3b-9c8277971183",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdD3QvZhthr8BnNiQ8H",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f28a53ad-6b27-4aa8-a1cd-f5c4be792c47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y5x6woNuU9rvo1LczPVUbb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 386,
      "cache_read_input_tokens": 78509,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 386
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 78509,
          "cache_creation_input_tokens": 386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 386,
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

_source line 31 · 2026-05-21T11:20:45.276Z_

<details><summary>↩ Tool result · `toolu_01UAg6pWzicCZaHzPHQjkHu4`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex:At 14B, cross-reference accuracy drops to 44.1\% with $\mathrm{EDD}_{0.70}{=}2$ (nucleus/temperature); reference-model choice accounts for ${\sim}$7\,pp of the apparent degradation, and the remaining signal attenuation constitutes a scale-dependent boundary for the current feature set.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:At 14B (Qwen2.5-14B), self-reference yields 50.8\% ($2{\times}$ chance, $\mathrm{EDD}_{0.70}{=}0$); cross-reference control (Pythia-1.4B) drops accuracy to 44.1\% ($-$6.8\,pp) but raises $\mathrm{EDD}_{0.70}$ to 2 for nucleus and temperature, revealing ${\sim}$7\,pp of the apparent degradation is a reference-model artifact (Appendix~\ref{app:cross_scale_full}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:    \item \textbf{Systematic characterization.} Cross-model transfer 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, preliminary 14B 44.1\% cross-reference ($\mathrm{EDD}_{0.70}{=}2$). We identify cross-strategy transfer (d1--d3: 45.9\%) as a boundary condition: decoding strategies induce qualitatively distinct degradation trajectories, with strategy affecting transfer more than model architecture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f28a53ad-6b27-4aa8-a1cd-f5c4be792c47",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "a4b94f73-762f-41ba-addb-e7c94abddbd5",
  "sourceToolAssistantUUID": "f28a53ad-6b27-4aa8-a1cd-f5c4be792c47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T11:20:49.446Z_

Now let me check if there's any actual table in the appendix showing the per-strategy breakdown for the cross-reference results (not just the Binoculars ablation, but the main cross-reference results):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4b94f73-762f-41ba-addb-e7c94abddbd5",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdDEGnZmHCrWnw1ZYrh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "33ff1c23-85de-4ea9-8f04-cfa61d400932",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011d1vdiFzSsHwRYAoiyjUWx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 78895,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 716,
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

_source line 33 · 2026-05-21T11:20:50.004Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JPBKuaDMdESfBqDBZPnxHU`</summary>

```json
{
  "command": "grep -B 5 -A 20 \"Pythia-1.4B observer analyzing Qwen2.5-14B\\|cross-reference.*nucleus.*temperature.*top\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33ff1c23-85de-4ea9-8f04-cfa61d400932",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdDEGnZmHCrWnw1ZYrh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4820b25a-43ef-45df-a8ae-57b931f60cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011d1vdiFzSsHwRYAoiyjUWx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 78895,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 716
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 181,
          "cache_read_input_tokens": 78895,
          "cache_creation_input_tokens": 716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 716,
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

_source line 34 · 2026-05-21T11:20:50.065Z_

<details><summary>↩ Tool result · `toolu_01JPBKuaDMdESfBqDBZPnxHU`</summary>

```text
Top-k sampling truncates the token distribution to the $k$ highest-probability tokens, producing text with reduced distributional diversity; this limits the information available to cross-model divergence features, which rely on disagreement between observer and performer predictions.
Merged improvement also varies by generator family: OLMo cells (observer-dissimilar) gain +5.1\,pp on average, compared to +3.9\,pp for Pythia (observer-similar) and +3.5\,pp for GPT-2~XL, suggesting cross-model divergence features contribute more when observer and generator architectures differ.

\paragraph{Cross-scale Binoculars ablation (14B).}
We evaluate Binoculars cross-scale on two representative strategies (temperature, top-$k$); the nucleus cell was used for the main 14B pipeline and its GPU hours were allocated to generation rather than Binoculars evaluation.
At 14B, when only 1--1.5B reference models are available for cross-perplexity computation (Pythia-1.4B observer analyzing Qwen2.5-14B text), Binoculars features degrade substantially (Table~\ref{tab:bino_14b_ablation}).
Self-reference statistical features (19-feat) outperform Binoculars (11-feat) by 8--11\,pp, reversing the near-parity observed at 1--1.5B.
Merging all 30 features yields a consistent +3.6--3.7\,pp gain over the self-reference baseline across both tested strategies, confirming that cross-perplexity features retain complementary signal even under the 10$\times$ scale gap---though the gain is attenuated relative to +4.2\,pp at 1--1.5B.

\begin{table}[h]
\centering
\small
\caption{Feature ablation at 14B (Qwen2.5-14B, self-reference$^\dagger$). Binoculars: observer=Pythia-1.4B, performer=Pythia-410M. $\Delta$: merged minus main-pipeline stat-only accuracy (Method~A alignment). Chance = 25\%.}
\label{tab:bino_14b_ablation}
\begin{tabular}{@{}lcccc@{}}
\toprule
Strategy & Bino-11 & Stat-19$^\dagger$ & Merged-30 & $\Delta$ \\
\midrule
temp09 & 42.6 & 50.5 & 54.2 & +3.7 \\
top-$k$50 & 37.7 & 47.9 & 51.5 & +3.6 \\
\bottomrule
\end{tabular}
\end{table}

The Binoculars degradation reflects a practical deployment constraint: the 10$\times$ scale gap between observer (1.4B) and generator (14B) causes cross-perplexity features to lose sensitivity, not a fundamental limitation of the cross-model divergence channel.
Self-reference features are more robust across scales because they avoid the observer--generator mismatch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4820b25a-43ef-45df-a8ae-57b931f60cbc",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "1aa67169-af7e-4a7f-9329-af2bae92382b",
  "sourceToolAssistantUUID": "4820b25a-43ef-45df-a8ae-57b931f60cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-21T11:20:52.143Z_

Let me search for any table that specifically shows Pythia-1.4B results on 14B data:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aa67169-af7e-4a7f-9329-af2bae92382b",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdDajqXWqomDLUXee3z",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "38874c1b-c99f-48dc-b5cc-3f6991ce25cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JJdYaYU9oNgU8R32w5eG7y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 79611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 951,
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

_source line 36 · 2026-05-21T11:20:52.657Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01K9H8JKP96M55rd8LxDHeyK`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\begin{table}\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex | tail -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38874c1b-c99f-48dc-b5cc-3f6991ce25cb",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdDajqXWqomDLUXee3z",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5a72c539-0933-45f0-8e8d-d5fdf318b56a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JJdYaYU9oNgU8R32w5eG7y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 79611,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 951
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 79611,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 951,
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

_source line 37 · 2026-05-21T11:20:52.728Z_

<details><summary>↩ Tool result · `toolu_01K9H8JKP96M55rd8LxDHeyK`</summary>

```text
160:\begin{table}[h]
178:\begin{table}[h]
210:\begin{table}[h]
267:\begin{table}[h]
310:\begin{table}[h]
333:\begin{table}[h]
357:\begin{table}[h]
386:\begin{table}[h]
421:\begin{table}[h]
446:\begin{table}[h]
528:\begin{table}[h]
580:\begin{table}[h]
613:\begin{table}[h]
651:\begin{table}[h]
679:\begin{table}[h]
706:\begin{table}[h]
757:\begin{table}[h]
779:\begin{table}[h]
815:\begin{table}[h]
840:\begin{table}[h]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a72c539-0933-45f0-8e8d-d5fdf318b56a",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "b7682ec7-af6a-4707-b4d9-996c4217d802",
  "sourceToolAssistantUUID": "5a72c539-0933-45f0-8e8d-d5fdf318b56a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-21T11:20:54.890Z_

Let me check the last few tables to see if any show cross-reference results with a dedicated table:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7682ec7-af6a-4707-b4d9-996c4217d802",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdDn9S7BkM34kH1o9i7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "22eb4979-f3fa-4ea2-ad2d-989ab99ff018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RM6wcy5cTmwNA8KNprYkdN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 80562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 341,
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

_source line 39 · 2026-05-21T11:20:55.231Z_

<details open><summary>🔧 Tool call — Read · `toolu_011nZ4FC4jbc7SiT6poey7Lw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 815,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22eb4979-f3fa-4ea2-ad2d-989ab99ff018",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdDn9S7BkM34kH1o9i7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "91f7d9fc-0081-47ec-95b9-fca88626eef9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RM6wcy5cTmwNA8KNprYkdN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 80562,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 341
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 80562,
          "cache_creation_input_tokens": 341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 341,
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

_source line 40 · 2026-05-21T11:20:55.238Z_

<details><summary>↩ Tool result · `toolu_011nZ4FC4jbc7SiT6poey7Lw`</summary>

```text
815	\begin{table}[h]
816	\centering
817	\small
818	\caption{Feature ablation at 14B (Qwen2.5-14B, self-reference$^\dagger$). Binoculars: observer=Pythia-1.4B, performer=Pythia-410M. $\Delta$: merged minus main-pipeline stat-only accuracy (Method~A alignment). Chance = 25\%.}
819	\label{tab:bino_14b_ablation}
820	\begin{tabular}{@{}lcccc@{}}
821	\toprule
822	Strategy & Bino-11 & Stat-19$^\dagger$ & Merged-30 & $\Delta$ \\
823	\midrule
824	temp09 & 42.6 & 50.5 & 54.2 & +3.7 \\
825	top-$k$50 & 37.7 & 47.9 & 51.5 & +3.6 \\
826	\bottomrule
827	\end{tabular}
828	\end{table}
829	
830	The Binoculars degradation reflects a practical deployment constraint: the 10$\times$ scale gap between observer (1.4B) and generator (14B) causes cross-perplexity features to lose sensitivity, not a fundamental limitation of the cross-model divergence channel.
831	Self-reference features are more robust across scales because they avoid the observer--generator mismatch.
832	The accuracy difference between self-reference (50.8\%) and Binoculars stat-only (40.1\% mean) may therefore partially reflect observer capacity limitations rather than feature design differences.
833	
834	\subsection{Prompted Generation Results}
835	\label{app:prompted_gen}
836	
837	Table~\ref{tab:prompted_gen} reports depth estimation performance under topic-seeded (prompted) generation using GPT-2~XL with nucleus sampling ($p{=}0.95$, depths 0--3).
838	Generation is conditioned on Wikipedia topic prompts rather than a bare BOS token, a more ecologically valid test of depth signal persistence.
839	
840	\begin{table}[h]
841	\centering
842	\small
843	\caption{Prompted generation (GPT-2~XL, nucleus $p{=}0.95$, topic-seeded). 5-fold CV accuracy and pairwise AUC. Chance = 25\%.}
844	\label{tab:prompted_gen}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91f7d9fc-0081-47ec-95b9-fca88626eef9",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "05fbe684-4eaa-40c3-9734-51a820bad377",
  "sourceToolAssistantUUID": "91f7d9fc-0081-47ec-95b9-fca88626eef9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-21T11:20:58.619Z_

Now let me look for any mention of a cross-reference table in the appendix more systematically. Let me search for the phrase "nucleus.*temperature.*top" to find if there's a table showing all three strategies for cross-reference:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05fbe684-4eaa-40c3-9734-51a820bad377",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdDy1J5BUCXFD5CYdRw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cad6ae8b-fb82-4c5a-b0b2-7867c3fa2904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011TqYjiEDAmBjAEKB6kQTdT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 80903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 787,
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

_source line 42 · 2026-05-21T11:20:59.093Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01F775LtH6DqDJ4hr93BURxW`</summary>

```json
{
  "command": "grep -n \"nucleus\\|temperature\\|top-k\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex | grep \"cross\\|44\\|Pythia.*14\\|14B.*Pythia\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cad6ae8b-fb82-4c5a-b0b2-7867c3fa2904",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdDy1J5BUCXFD5CYdRw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3243cb16-0ef5-495e-bfe5-548a4be5968c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011TqYjiEDAmBjAEKB6kQTdT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 80903,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 787
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 183,
          "cache_read_input_tokens": 80903,
          "cache_creation_input_tokens": 787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 787,
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

_source line 43 · 2026-05-21T11:20:59.164Z_

<details><summary>↩ Tool result · `toolu_01F775LtH6DqDJ4hr93BURxW`</summary>

```text
138:The cross-strategy results in \S\ref{sec:gen:crossstrategy} use a single temperature ($\tau{=}0.9$).
139:To test whether depth signal generalizes across temperatures, we repeat the classification pipeline at $\tau \in \{0.5, 0.7, 0.9, 1.1\}$ on Pythia-1.4B.
147:Training loss reveals the mechanism: at low temperature ($\tau{=}0.5$), fine-tuning loss decreases steeply across recursive depths ($2.27 \to 0.42 \to 0.16$), a sign of rapid memorization of the model's own output.
379:The 14B model uses clean FP16 LoRA fine-tuning across all three decoding strategies (nucleus, temperature $\tau{=}0.9$, top-$k$ $k{=}50$; 5{,}000 samples per depth, depths $d \in \{0, 1, 2, 3\}$).
384:The 14B model is tested across all three decoding strategies; the 7--8B models use nucleus sampling only.
616:\caption{Learned estimator cross-model transfer (leave-one-model-out, nucleus, 4-class). RF baseline from Table~\ref{tab:cross_model}. Chance = 25\%.}
677:Table~\ref{tab:feature_ablation} reports cross-model transfer accuracy (leave-one-model-out, nucleus) when restricting the classifier to subsets of the 19-feature vector, grouped by signal type.
682:\caption{Feature group ablation (cross-model LOO, nucleus, 4-class). Chance = 25\%.}
709:\caption{RF seed robustness (cross-model LOO, nucleus, 4-class).}
810:We evaluate Binoculars cross-scale on two representative strategies (temperature, top-$k$); the nucleus cell was used for the main 14B pipeline and its GPU hours were allocated to generation rather than Binoculars evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3243cb16-0ef5-495e-bfe5-548a4be5968c",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "f35dc1c9-95af-4290-a9c6-7cf9b2a3c354",
  "sourceToolAssistantUUID": "3243cb16-0ef5-495e-bfe5-548a4be5968c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-21T11:21:01.642Z_

Based on my thorough investigation, let me compile the findings. I notice that the 44.1% cross-reference result is mentioned in the main text but I should verify whether there's an actual table in the appendix with per-strategy breakdown. Let me check the text more carefully:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f35dc1c9-95af-4290-a9c6-7cf9b2a3c354",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdEFhdwrBn25Kk9Rtoz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "097d1c24-0c4a-4e4a-8960-890124dbe667",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BpddAQhV21SRQz9Z4go889",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 81690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 689,
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

_source line 45 · 2026-05-21T11:21:02.124Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TaaYyo5PABZtxD1Rq5ixH7`</summary>

```json
{
  "command": "grep -B 5 -A 10 \"44.1.*EDD\\|cross-reference.*44.1\\|44.1.*cross\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "097d1c24-0c4a-4e4a-8960-890124dbe667",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdEFhdwrBn25Kk9Rtoz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "66757569-6e3f-4228-b3b5-ec6ff004e482",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BpddAQhV21SRQz9Z4go889",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 81690,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 689
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 182,
          "cache_read_input_tokens": 81690,
          "cache_creation_input_tokens": 689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 689,
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

_source line 46 · 2026-05-21T11:21:02.179Z_

<details><summary>↩ Tool result · `toolu_01TaaYyo5PABZtxD1Rq5ixH7`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-Real-world contamination typically involves accumulation, where synthetic and human data co-exist at unknown proportions \cite{gerstgrasser2024_accumulate}.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-Pilot accumulation experiments show 14--15\,pp attenuation relative to full-replacement; our results therefore represent an upper bound on feature separability, and extending the framework to accumulation settings is a priority for future work.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-\paragraph{Scale and generalization boundaries.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-The primary benchmark uses 1--1.5B parameter models with controlled LoRA fine-tuning.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex:At 14B, cross-reference accuracy drops to 44.1\% with $\mathrm{EDD}_{0.70}{=}2$ (nucleus/temperature); reference-model choice accounts for ${\sim}$7\,pp of the apparent degradation, and the remaining signal attenuation constitutes a scale-dependent boundary for the current feature set.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-Cross-strategy transfer drops d1--d3 accuracy to 45.9\%, and on web-crawl data (C4) false positive rates reach 22\%; these gaps narrow with confidence thresholding and strategy-aware pipelines but are not fully resolved.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-Additional caveats (reference model dependency, ${\leq}$11\,pp; single LoRA seed, ${\sim}$1--3\,pp uncertainty; adversarial robustness; passage length sensitivity) are detailed in the Appendix.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-\section*{Ethics Statement}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-This work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-No human subjects were involved, no private or sensitive data were collected, and no new models were released.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-Code and data will be released upon acceptance.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-This research used AI coding assistants for experiment implementation and writing drafts.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-%% ----------------------------------------------------------------
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-\subsection{Preliminary Cross-Scale Observations (14B)}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-\label{sec:gen:crossscale}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:At 14B (Qwen2.5-14B), self-reference yields 50.8\% ($2{\times}$ chance, $\mathrm{EDD}_{0.70}{=}0$); cross-reference control (Pythia-1.4B) drops accuracy to 44.1\% ($-$6.8\,pp) but raises $\mathrm{EDD}_{0.70}$ to 2 for nucleus and temperature, revealing ${\sim}$7\,pp of the apparent degradation is a reference-model artifact (Appendix~\ref{app:cross_scale_full}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-Cross-domain (arXiv) accuracy reaches 74.1\% at 1--1.5B; cross-domain FPR is discussed in Limitations.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-\begin{itemize}[nosep,leftmargin=*]
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-    \item \textbf{Task formalization and metric.} We define recursive generation depth estimation as ordinal classification, introduce the \emph{Effective Discriminable Depth} (EDD) metric, and construct a 180K-sample benchmark ($3$ model families $\times$ $3$ decoding strategies $\times$ $4$ depths).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-    \item \textbf{Depth Degradation Atlas.} The perplexity tail feature family dominates depth discrimination across all 9 cells; $\mathrm{EDD}_{0.70}{=}4$ for all three families, validated by 5-class extension (71--80\%); feature group ablation confirms perplexity tail dominance (76.6\% alone vs.\ 78.4\% full set).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:    \item \textbf{Systematic characterization.} Cross-model transfer 66.4\% (d1--d3: 55.4\%), cross-domain arXiv 74.1\%, preliminary 14B 44.1\% cross-reference ($\mathrm{EDD}_{0.70}{=}2$). We identify cross-strategy transfer (d1--d3: 45.9\%) as a boundary condition: decoding strategies induce qualitatively distinct degradation trajectories, with strategy affecting transfer more than model architecture.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66757569-6e3f-4228-b3b5-ec6ff004e482",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "22671684-4366-4782-9505-c5044612e877",
  "sourceToolAssistantUUID": "66757569-6e3f-4228-b3b5-ec6ff004e482",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-21T11:21:04.535Z_

Perfect! Now I have all the information I need. Let me verify that the text actually says the result is shown in the appendix and what that appendix section contains:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22671684-4366-4782-9505-c5044612e877",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdEUa3FmgGFarBGwgoo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b4eb9914-e5c4-4587-816e-23d5b0a586ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TYEqC8FfXBHxyV7YxNnWgn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 2479,
      "cache_read_input_tokens": 82379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2479,
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

_source line 48 · 2026-05-21T11:21:04.958Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012Zc9dmZXsLbFt15awNCQCQ`</summary>

```json
{
  "command": "grep -n \"app:cross_scale_full\" /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4eb9914-e5c4-4587-816e-23d5b0a586ec",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdEUa3FmgGFarBGwgoo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9bb90aeb-9623-4228-a775-493a3e18c59a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TYEqC8FfXBHxyV7YxNnWgn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 2479,
      "cache_read_input_tokens": 82379,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2479
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 134,
          "cache_read_input_tokens": 82379,
          "cache_creation_input_tokens": 2479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2479,
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

_source line 49 · 2026-05-21T11:21:05.010Z_

<details><summary>↩ Tool result · `toolu_012Zc9dmZXsLbFt15awNCQCQ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:114:At 14B (Qwen2.5-14B), self-reference yields 50.8\% ($2{\times}$ chance, $\mathrm{EDD}_{0.70}{=}0$); cross-reference control (Pythia-1.4B) drops accuracy to 44.1\% ($-$6.8\,pp) but raises $\mathrm{EDD}_{0.70}$ to 2 for nucleus and temperature, revealing ${\sim}$7\,pp of the apparent degradation is a reference-model artifact (Appendix~\ref{app:cross_scale_full}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:17:The sole 8B instruction-tuned model tested (Llama-3.1-8B-Instruct) exhibits monotonically decreasing AUC, in contrast to the non-monotonic trajectory of its base-model counterpart; whether this regularization effect generalizes across architectures remains open (Appendix~\ref{app:cross_scale_full}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:374:\label{app:cross_scale_full}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bb90aeb-9623-4228-a775-493a3e18c59a",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "86a3729f-dff4-4f56-aea2-c3c6495e2aca",
  "sourceToolAssistantUUID": "9bb90aeb-9623-4228-a775-493a3e18c59a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-21T11:21:07.400Z_

Perfect! Now let me check what label that corresponds to in the appendix:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86a3729f-dff4-4f56-aea2-c3c6495e2aca",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdEgfZFBSqCX51hPUVF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6327f488-314b-41b4-8567-c1d06caf6ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HCLV6jaxbWJDvawepXzHK8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 510,
      "cache_read_input_tokens": 84858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 510,
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

_source line 51 · 2026-05-21T11:21:07.823Z_

<details open><summary>🔧 Tool call — Read · `toolu_011hvpb2W8KpyHBGvPHsm4eb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 373,
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6327f488-314b-41b4-8567-c1d06caf6ce5",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdEgfZFBSqCX51hPUVF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c96aa6f8-8764-42e3-97bc-1328fd766a26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HCLV6jaxbWJDvawepXzHK8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 510,
      "cache_read_input_tokens": 84858,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 510
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 143,
          "cache_read_input_tokens": 84858,
          "cache_creation_input_tokens": 510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 510,
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

_source line 52 · 2026-05-21T11:21:07.830Z_

<details><summary>↩ Tool result · `toolu_011hvpb2W8KpyHBGvPHsm4eb`</summary>

```text
373	\subsection{Cross-Scale Full Results}
374	\label{app:cross_scale_full}
375	
376	This section provides the full cross-scale analysis summarized in \S\ref{sec:gen:crossscale}.
377	We extend the benchmark to two 7--8B models (Qwen2.5-7B-Instruct \cite{qwen2.5}, Llama-3.1-8B-Instruct \cite{llama3}) and one 14B model (Qwen2.5-14B).
378	The 7--8B models use 4-bit NF4 QLoRA fine-tuning with nucleus sampling ($p{=}0.95$, 500 samples per depth, depths $d \in \{0, 1, \ldots, 5\}$).
379	The 14B model uses clean FP16 LoRA fine-tuning across all three decoding strategies (nucleus, temperature $\tau{=}0.9$, top-$k$ $k{=}50$; 5{,}000 samples per depth, depths $d \in \{0, 1, 2, 3\}$).
380	Feature extraction for 1--8B models uses Pythia-1.4B as reference; Qwen2.5-14B uses self-reference (the 14B model computes its own perplexity features), a choice that precludes direct comparison with the Pythia-referenced pipeline (see confounds below).
381	
382	\paragraph{Scale comparison.}
383	Table~\ref{tab:cross_scale} contrasts the 7--14B models with the three 1--1.5B models on matched evaluation (depths 0--3).
384	The 14B model is tested across all three decoding strategies; the 7--8B models use nucleus sampling only.
385	
386	\begin{table}[h]
387	\centering
388	\small
389	\caption{Cross-scale comparison: 4-class RF accuracy (\%, depths 0--3), $\mathrm{EDD}_{T{=}0.70}$, and d0-vs-d1 AUC. CI: 95\% bootstrap. Chance = 25\%. $^\dagger$Self-reference model (see text).}
390	\label{tab:cross_scale}
391	\resizebox{\columnwidth}{!}{%
392	\begin{tabular}{@{}llccc@{}}
393	\toprule
394	Model & Strategy & 4-class acc & $\mathrm{EDD}_{0.70}$ & d0v1 \\
395	\midrule
396	GPT-2~XL (1.5B) & nucleus & 84.3 & 4 & 0.999 \\
397	OLMo-1B & nucleus & 78.9 & 4 & 0.997 \\
398	Pythia-1.4B & nucleus & 78.7 & 4 & 0.998 \\
399	\midrule
400	Llama-3.1-8B & nucleus & 70.2\,[68.3, 72.4] & 4 & 0.949 \\
401	Qwen2.5-7B & nucleus & 60.1\,[58.0, 62.1] & ${>}5$ & 0.969 \\
402	\midrule
403	Qwen2.5-14B$^\dagger$ & nucleus & 54.1\,[53.4, 54.7] & 0 & 0.643 \\
404	Qwen2.5-14B$^\dagger$ & temp09 & 50.5\,[49.8, 51.2] & 0 & 0.632 \\
405	Qwen2.5-14B$^\dagger$ & top-$k$50 & 47.9\,[47.3, 48.6] & 0 & 0.561 \\
406	\cmidrule{2-5}
407	\multicolumn{2}{@{}l}{\textit{14B mean}} & \textit{50.8} & --- & --- \\
408	\bottomrule
409	\end{tabular}}
410	\end{table}
411	
412	\paragraph{(1) Depth signal persists at 7--8B scale.}
413	Both 7--8B models substantially exceed the 25\% chance baseline: Llama-3.1-8B achieves 70.2\% (95\% CI $[68.3, 72.4]$) and Qwen2.5-7B achieves 60.1\% ($[58.0, 62.1]$); recursive depth therefore remains estimable from perplexity-based features even when the generator is 5--7$\times$ larger than the reference model.
414	Depth-0 separability is preserved in both models: d0v1 AUC is 0.949 (Llama-3.1) and 0.969 (Qwen2.5).
415	
416	\paragraph{(2) EDD at 7--8B scale.}
417	At threshold $T{=}0.70$, Qwen2.5-7B maintains all consecutive-pair AUCs above 0.70 through depth~5 (Table~\ref{tab:cross_scale_auc}), yielding $\mathrm{EDD}_{T{=}0.70} > 5$, exceeding the $\mathrm{EDD}{=}4$ observed at 1--1.5B.
418	Llama-3.1-8B matches the smaller models at $\mathrm{EDD}{=}4$: its monotonic decay causes d4v5 (0.618) to drop below $T$, despite stronger signal at shallower depths.
419	Both larger generators produce weaker per-step signal than the 1--1.5B models (mean consecutive AUC: 0.786 for Llama-3.1, 0.782 for Qwen2.5, vs.\ 0.852 at 1--1.5B).
420	
421	\begin{table}[h]
422	\centering
423	\small
424	\caption{Consecutive binary AUC. Llama-3.1-8B exhibits monotonic decay; Qwen2.5-7B shows a U-shaped pattern; Qwen2.5-14B$^\dagger$ (depths 0--3 only) has all pairs below $T{=}0.70$ with strategy-specific patterns. $^\dagger$Self-reference model.}
425	\label{tab:cross_scale_auc}
426	\resizebox{\columnwidth}{!}{%
427	\begin{tabular}{@{}llccccc@{}}
428	\toprule
429	Model & Strategy & d0v1 & d1v2 & d2v3 & d3v4 & d4v5 \\
430	\midrule
431	Llama-3.1-8B & nucleus & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\
432	Qwen2.5-7B & nucleus & 0.969 & 0.729 & 0.709 & 0.732 & 0.772 \\
433	\midrule
434	Qwen2.5-14B$^\dagger$ & nucleus & 0.643 & 0.713 & \textbf{0.728} & \multicolumn{2}{c}{--} \\
435	Qwen2.5-14B$^\dagger$ & temp09 & 0.632 & \textbf{0.726} & 0.618 & \multicolumn{2}{c}{--} \\
436	Qwen2.5-14B$^\dagger$ & top-$k$50 & 0.561 & 0.687 & 0.679 & \multicolumn{2}{c}{--} \\
437	\bottomrule
438	\end{tabular}}
439	\end{table}
440	
441	\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}
442	Among instruction-tuned models, Llama-3.1-8B exhibits monotonic AUC decay consistent with the 1--1.5B pattern, while Qwen2.5-7B shows a U-shaped recovery beyond d2v3 (Table~\ref{tab:cross_scale_auc}).
443	A base-model control (Llama-3.1-8B without instruction tuning) clarifies the causal direction: the base model achieves 59.9\% four-class accuracy (95\% CI [57.8, 62.15], $\mathrm{EDD}_{0.70}{=}2$) with non-monotonic AUC decay (Table~\ref{tab:llama3_base_auc}), while the instruction-tuned variant reaches 70.2\% with strictly monotonic decay.
444	The base-model control experiment suggests instruction-tuning regularizes rather than confounds the depth signal.
445	
446	\begin{table}[h]
447	\centering
448	\small
449	\caption{Pairwise AUC: Llama-3.1-8B Base vs.\ Instruct.}
450	\label{tab:llama3_base_auc}
451	\begin{tabular}{lccccc}
452	\toprule
453	Variant & $d_{0\text{v}1}$ & $d_{1\text{v}2}$ & $d_{2\text{v}3}$ & $d_{3\text{v}4}$ & $d_{4\text{v}5}$ \\
454	\midrule
455	Base & 0.918 & 0.794 & 0.682 & 0.730 & 0.595 \\
456	Instruct & 0.965 & 0.874 & 0.771 & 0.716 & 0.618 \\
457	\bottomrule
458	\end{tabular}
459	\end{table}
460	
461	The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.
462	
463	\paragraph{(4) Signal attenuation at 14B.}
464	Qwen2.5-14B (clean FP16, self-reference) is tested across all three decoding strategies (Table~\ref{tab:cross_scale}).
465	Mean four-class accuracy is 50.8\% ($2.0{\times}$ chance), with nucleus 54.1\%, temperature 50.5\%, and top-$k$ 47.9\%.
466	$\mathrm{EDD}_{0.70}{=}0$ across all three strategies: no adjacent-depth pair reaches the 0.70 AUC threshold.
467	The d0/d1 boundary, near-perfect at 1--1.5B (AUC ${>}0.99$), attenuates to 0.56--0.64 at 14B.
468	
469	Each strategy produces a structurally distinct adjacent-pair AUC pattern (Table~\ref{tab:cross_scale_auc}):
470	nucleus is monotonically increasing (d0v1=0.643 $<$ d1v2=0.713 $<$ d2v3=0.728);
471	temperature exhibits d2v3 collapse (0.618, the weakest boundary) because temperature scaling uniformly amplifies logit differences, accelerating convergence to the attractor distribution at deeper depths;
472	top-$k$ exhibits d0v1 collapse (0.561, the weakest boundary) because vocabulary truncation constrains d0 and d1 distributions to the same top-$k$ tokens, compressing their statistical distance.
473	This three-way divergence confirms at 14B that different decoding strategies induce structurally distinct degradation trajectories (\S\ref{sec:gen:crossstrategy}).
474	
475	Feature importance shifts under top-$k$: lexical diversity metrics (TTR, hapax ratio) enter the top-5, displacing perplexity tail statistics that dominate under nucleus and temperature.
476	This result carries an important caveat: Qwen2.5-14B uses self-reference, whereas all other experiments use Pythia-1.4B.
477	Self-reference conflates the generator's distributional shift with the reference model's sensitivity; the observed attenuation may partially reflect the reference model change rather than a pure scale effect.
478	
479	\paragraph{Caveats.}
480	For Qwen2.5-7B, the CI lower bound (58.0\%) does not exclude sub-60\% accuracy; Llama-3.1-8B's lower bound (68.3\%) is more comfortably above chance but still below the 75--83\% range at 1--1.5B.
481	The divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.
482	
483	\paragraph{Confounds.}
484	\label{app:cross_scale_confounds}
485	Four confounds limit the 7--8B results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling at 7--8B (the 14B model addresses this with all three strategies); (4)~vocabulary mismatch between larger generators and the 1.4B reference model.
486	For the 14B model specifically: self-reference rather than the Pythia-1.4B reference used for all other experiments prevents direct cross-scale comparison.
487	The base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.
488	The remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution); it is therefore infeasible to attribute the observed accuracy gap (60--70\% vs.\ 78--85\% at 1--1.5B) to any single factor.
489	
490	\subsection{Cross-Boundary Generalization}
491	\label{app:cross_boundary}
492	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c96aa6f8-8764-42e3-97bc-1328fd766a26",
  "isSidechain": true,
  "promptId": "2267cdea-0a16-4d68-94b6-122eca82520d",
  "agentId": "ae8b81dc77b3d268d",
  "type": "user",
  "uuid": "9a54c91c-c2ad-4531-94d2-c5d1218d7997",
  "sourceToolAssistantUUID": "c96aa6f8-8764-42e3-97bc-1328fd766a26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-21T11:21:20.352Z_

Perfect! Now I have all the information I need to provide a comprehensive report. Let me compile my findings.

## Report: Cross-Reference Result Support in Appendix

Based on my thorough examination of the appendix, here is what I found:

**Key Finding: The 44.1% cross-reference result is NOT shown with a dedicated table in the appendix.** It is only mentioned textually in the main paper body.

### What the Paper Claims:

In **generalization.tex (Section 4.3, "Preliminary Cross-Scale Observations (14B)")**:
- "At 14B (Qwen2.5-14B), self-reference yields 50.8%... cross-reference control (Pythia-1.4B) drops accuracy to 44.1% (-6.8pp) but raises EDD_0.70 to 2 for nucleus and temperature, revealing ~7pp of the apparent degradation is a reference-model artifact (Appendix ref{app:cross_scale_full})."

The paper explicitly states the cross-reference result **refers to Appendix Section A.10 (app:cross_scale_full)** for detailed results.

### What's Actually in the Appendix:

Section A.10 ("Cross-Scale Full Results", lines 373-488) contains:
1. **Table 16 (tab:cross_scale)** - Shows ONLY self-reference results for 14B:
   - nucleus: 54.1%
   - temp09: 50.5%
   - top-k50: 47.9%
   - 14B mean: 50.8%
   - **NO per-strategy breakdown for cross-reference**

2. **Table 17 (tab:cross_scale_auc)** - Shows only pairwise AUC values (no accuracy) for 14B self-reference

3. **Table 19 (tab:bino_14b_ablation)** - Shows Binoculars cross-perplexity ablation at 14B with Pythia-1.4B observer, but only for two strategies (temp09 and top-k50, with nucleus omitted). This table shows stat-19 (self-reference) accuracy values, not the cross-reference results.

### Critical Gap:

**There is NO table in the appendix showing the per-strategy breakdown of the 44.1% cross-reference result.** The appendix only states (line 476-477):
- "Qwen2.5-14B uses self-reference, whereas all other experiments use Pythia-1.4B. Self-reference conflates the generator's distributional shift with the reference model's sensitivity..."

**The main paper mentions EDD_0.70=2 for "nucleus and temperature" for cross-reference**, but there is no table showing:
- Cross-reference nucleus accuracy
- Cross-reference temperature accuracy  
- Cross-reference top-k accuracy

### Summary:

**The 44.1% cross-reference result lacks proper tabular support in the appendix.** Only the self-reference results (50.8% mean) are shown with full per-strategy breakdown (Table 16). The paper makes a claim about the cross-reference performance (44.1% overall, EDD=2 for nucleus/temperature) but does not provide the corresponding per-strategy table or detailed results in the appendix to support this claim with the same level of detail as the self-reference baseline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a54c91c-c2ad-4531-94d2-c5d1218d7997",
  "isSidechain": true,
  "agentId": "ae8b81dc77b3d268d",
  "requestId": "req_011CbFdF2eqgtVroWeVt8EUv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d25a115b-1e64-4715-aa52-132ae5c96152",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/director_e0265221",
  "sessionId": "03062a43-5df2-4353-936e-547435cc5255",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jaunty-napping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R8BsUVnL2H8jgQuX8XaXtC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 0,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 85368,
      "output_tokens": 792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3933
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 0,
          "output_tokens": 792,
          "cache_read_input_tokens": 85368,
          "cache_creation_input_tokens": 3933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3933,
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
