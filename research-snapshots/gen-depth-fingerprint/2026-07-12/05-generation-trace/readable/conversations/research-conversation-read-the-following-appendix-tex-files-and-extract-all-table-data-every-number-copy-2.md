# Research conversation: Read the following appendix tex files and extract ALL table data (every number in every table). Be thorough. Files to re

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5eb1178a764b765b.jsonl`
- **Structured JSON:** [`74752f1425943a05101b.json`](../../sessions/74/74752f1425943a05101b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-23T10:22:43.433Z_

Read the following appendix tex files and extract ALL table data (every number in every table). Be thorough.

Files to read (all under /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/):
1. appendix_classifier.tex
2. appendix_confusion_matrix.tex
3. appendix_dataset_stats.tex
4. appendix_downstream.tex
5. appendix_finer_depth.tex
6. appendix_human_edit.tex
7. appendix_length.tex
8. appendix_lofo.tex
9. appendix_ablation.tex
10. appendix_seed_control.tex
11. appendix_error_analysis.tex

For each file:
- Identify the table number and caption
- Extract every numerical value in the table with row/column labels
- Also extract any numerical values mentioned in the text around the table

Report in format: [filename] Table X: caption, then list all values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a5eb1178a764b765b",
  "type": "user",
  "uuid": "5e9ae4c4-81f2-4e26-9481-03b03f6de4a2",
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

_source line 2 · 2026-05-23T10:22:44.519Z_

I'll read all the appendix tex files and extract the table data. Let me start by reading all of them in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e9ae4c4-81f2-4e26-9481-03b03f6de4a2",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQQ7DMfo2wbhrJLfBD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "99e1355c-318e-4af7-8528-d741f089d43b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VfQaCsEFUWXJ3dyrgmshu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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

_source line 3 · 2026-05-23T10:22:44.891Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V2hEZgvcwNMqFkiZo8wHjB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99e1355c-318e-4af7-8528-d741f089d43b",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQQ7DMfo2wbhrJLfBD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d56bc79c-5e15-4ef2-87ef-39d703907eaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VfQaCsEFUWXJ3dyrgmshu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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

_source line 4 · 2026-05-23T10:22:44.894Z_

<details><summary>↩ Tool result · `toolu_01V2hEZgvcwNMqFkiZo8wHjB`</summary>

```text
1	To verify that the depth signal resides in the features rather than the classifier,
2	we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest
3	in place of XGBoost (Table~\ref{tab:alt-classifier}).
4	All other settings (the same 7 features, 3-class labels, and class-balanced downsampling) are
5	kept identical. For Logistic Regression we apply standard scaling to the features.
6	
7	\begin{table}[ht]
8	\centering
9	\caption{LOGO macro-F1 across three classifiers. Each column shows the held-out generator F1. (6-generator LOGO; 3-class.)}
10	\label{tab:alt-classifier}
11	\small
12	\resizebox{\linewidth}{!}{%
13	\begin{tabular}{lc cccccc}
14	\toprule
15	Classifier & Avg F1 & OLMo-2 & Py-1B & Py-2.8B & Qw-0.6B & Qw-1.7B & Qw-8B \\
16	\midrule
17	XGBoost          & 0.789 & 0.764 & 0.856 & 0.804 & 0.824 & 0.806 & 0.683 \\
18	Random Forest    & 0.790 & 0.764 & 0.856 & 0.804 & 0.825 & 0.807 & 0.684 \\
19	Logistic Regr.   & 0.725 & 0.719 & 0.781 & 0.740 & 0.745 & 0.743 & 0.624 \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	Both tree-based classifiers achieve LOGO F1 $\approx 0.79$,
25	and even a linear model reaches $0.725$, well above the $0.33$ chance baseline for
26	three classes.
27	The per-generator ranking is also consistent across classifiers
28	(Pythia-1B easiest, Qwen3-8B hardest),
29	confirming that discriminative power originates in the entropy and lexical features,
30	not in classifier capacity.
31	Ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) achieve comparable F1 with overlapping CIs, which confirms that 3-class granularity provides insufficient resolution for ranking-aware losses to improve over standard multiclass classification.
32	
33	\paragraph{XGBoost hyperparameter sensitivity.}
34	To verify that performance is not an artifact of hyperparameter selection, we vary \texttt{max\_depth} $\in \{3, 4, 6, 8\}$ while keeping all other settings fixed (Table~\ref{tab:xgb-sensitivity}).
35	
36	\begin{table}[ht]
37	\centering
38	\small
39	\caption{XGBoost \texttt{max\_depth} sensitivity (8-gen LOGO). 3-class F1 varies by only 2.0\,pp; binary F1 (gen-1 vs.\ gen-2+) is effectively invariant ($\leq$0.1\,pp).}
40	\label{tab:xgb-sensitivity}
41	\begin{tabular}{lcc}
42	\toprule
43	\textbf{max\_depth} & \textbf{3-class F1} & \textbf{Binary F1} \\
44	\midrule
45	3 & 0.752 & 0.700 \\
46	4 & 0.759 & 0.699 \\
47	6 & 0.769 & 0.700 \\
48	8 & 0.772 & 0.699 \\
49	\bottomrule
50	\end{tabular}
51	\end{table}
52	
53	3-class F1 increases monotonically with tree depth but the total range is only 2.0\,pp (0.752--0.772); binary F1 is effectively invariant (0.699--0.700).
54	The default \texttt{max\_depth}\,=\,6 used throughout the paper lies within 0.3\,pp of the best 3-class setting, confirming that the reported results are not sensitive to this choice.
55	
56	\subsection*{Sampling Sensitivity Analysis}
57	\label{app:sampling-sensitivity}
58	
59	To assess robustness to decoding temperature, we regenerate continuation chains at $t \in \{0.5, 0.9\}$ with fixed nucleus $p{=}0.9$ (matching the default) for four generators spanning three model families: Pythia-2.8B, OLMo-2-1B, Qwen3-1.7B, and Qwen3-0.6B (Table~\ref{tab:sampling-ablation}).
60	
61	\begin{table}[ht]
62	\centering
63	\caption{Depth classification under varying temperature (fixed top-$p$\,=\,0.9). Binary: gen-1 vs.\ gen-2+. LOGO evaluation; 95\% bootstrap CIs.$^{\ast}$$^{\dagger}$}
64	\label{tab:sampling-ablation}
65	\small
66	\resizebox{\linewidth}{!}{%
67	\begin{tabular}{llcc c}
68	\toprule
69	Model & Temp & LOGO Binary F1 & 95\% CI & $\rho$(ent.\ mean) \\
70	\midrule
71	Pythia-2.8B$^{\dagger}$ & 0.5  & \textbf{0.814} & [.798, .828] & $-0.58$ \\
72	Pythia-2.8B$^{\dagger}$ & 0.7  & 0.740 & [.725, .755] & $-0.60$ \\
73	Pythia-2.8B$^{\dagger}$ & 0.9  & 0.480 & [.465, .498] & $-0.30$ \\
74	\midrule
75	OLMo-2-1B & 0.5  & \textbf{0.783} & [.768, .798] & $-0.72$ \\
76	OLMo-2-1B & 0.7  & 0.695 & [.679, .711] & $-0.60$ \\
77	OLMo-2-1B & 0.9  & 0.453 & [.437, .469] & $-0.26$ \\
78	\midrule
79	Qwen3-1.7B$^{\dagger}$ & 0.5  & 0.751 & --- & $-0.60$ \\
80	Qwen3-1.7B$^{\dagger}$ & 0.7  & 0.751 & --- & $-0.60$ \\
81	Qwen3-1.7B$^{\dagger}$ & 0.9  & 0.566 & --- & $-0.37$ \\
82	\midrule
83	Qwen3-0.6B & 0.5  & 0.711 & [.694, .729] & $-0.67$ \\
84	Qwen3-0.6B & 0.7  & 0.691 & [.673, .709] & $-0.60$ \\
85	Qwen3-0.6B & 0.9  & 0.598 & [.582, .615] & $-0.29$ \\
86	\bottomrule
87	\end{tabular}}
88	\end{table}
89	\vspace{2pt}
90	\noindent\begin{minipage}{\columnwidth}
91	\scriptsize $^{\ast}$OLMo temperature experiments use OLMo-2-0425-1B (April 2025 release); the original OLMo-2-1B-hf weights are no longer publicly available.\par\vspace{1pt}
92	$^{\dagger}$Pythia-2.8B and Qwen3-1.7B use 6-generator LOGO (pre-expansion); OLMo-2-1B and Qwen3-0.6B use 8-generator LOGO. Within-model comparisons are unaffected.
93	\end{minipage}
94	
95	\begin{sloppypar}
96	Temperature sensitivity is asymmetric and model-dependent. High-temperature degradation ($t{=}0.9$) is universal: all four generators lose $9.3$--$26.0$\,pp in binary F1, with entropy mean's $|\rho|$ weakening to $0.26$--$0.37$ (vs.\ $0.58$--$0.72$ at $t{=}0.5$). Low-temperature improvement ($t{=}0.5$) is model-dependent: Pythia-2.8B and OLMo-2-1B gain $+7.4$ and $+8.8$\,pp respectively, while both Qwen models show negligible change ($0$--$2.0$\,pp). This split tracks model family rather than scale: Qwen3-0.6B (smallest) and Qwen3-1.7B both plateau, while OLMo-2-1B (similar scale to Qwen3-1.7B) benefits substantially. One possible explanation is that Qwen models produce more peaked output distributions at $t{=}0.7$, leaving less room for low-temperature compression to sharpen the depth signal.
97	\end{sloppypar}
98	
99	The method operates reliably within $t \in [0.5, 0.7]$ across all tested models. Degradation onset at $t{=}0.9$ defines the practical upper bound, consistent with the hypothesis that elevated temperature injects sufficient randomness to flatten the distributional drift that DDR exploits (\S\ref{sec:discussion}).
100	
101	\subsection*{Per-Generator Performance}
102	
103	Figure~\ref{fig:per-gen} visualizes per-generator LOGO performance.
104	Pythia models (1B, 2.8B) achieve highest F1, while larger models (Mistral-7B, Qwen3-8B) show degradation.
105	The scale effect (larger models $\rightarrow$ lower F1) is consistent with higher-capacity models generating text statistically closer to human writing.
106	
107	\begin{figure}[H]
108	\centering
109	\includegraphics[width=\columnwidth, trim=0 0 347pt 0, clip]{fig_appendix_per_gen.pdf}\\[-2pt]
110	{\small (a) 8-generator binary and 3-class F1, sorted by binary F1}
111	\caption{Per-generator LOGO performance. Dashed lines: pool average.}
112	\label{fig:per-gen}
113	\end{figure}
114	
115	\begin{figure}[H]
116	\addtocounter{figure}{-1}
117	\centering
118	\includegraphics[width=\columnwidth, trim=347pt 0 0 0, clip]{fig_appendix_per_gen.pdf}\\[-2pt]
119	{\small (b) 6-generator LOGO detail heatmap}
120	\caption{(Continued) Per-generator performance heatmap across model families.}
121	\end{figure}
122	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d56bc79c-5e15-4ef2-87ef-39d703907eaa",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a5eb1178a764b765b",
  "type": "user",
  "uuid": "321aacfc-aba5-4cdc-b598-6a4ff266dc48",
  "sourceToolAssistantUUID": "d56bc79c-5e15-4ef2-87ef-39d703907eaa",
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

_source line 5 · 2026-05-23T10:22:44.940Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P2AiJ9CpT8nuxLUdB1e2aG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "321aacfc-aba5-4cdc-b598-6a4ff266dc48",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQQ7DMfo2wbhrJLfBD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a78133e2-baa9-4f18-b6bd-24a449788682",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VfQaCsEFUWXJ3dyrgmshu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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

_source line 6 · 2026-05-23T10:22:44.947Z_

<details><summary>↩ Tool result · `toolu_01P2AiJ9CpT8nuxLUdB1e2aG`</summary>

```text
1	Table~\ref{tab:confusion} reports the aggregated confusion matrix from the original six-generator subset (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B) under leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth $\geq$ 2).
2	The later-added Llama-3.2-3B and Mistral-7B-v0.3 are evaluated in the full 8-generator LOGO results (Table~\ref{tab:logo-results}).
3	
4	\begin{table}[ht]
5	\centering
6	\small
7	\caption{Aggregated 3-class confusion matrix from 6-generator LOGO evaluation ($N=27{,}529$). Each cell shows count and row-normalized percentage. Gen-0 is near-perfectly identified. Gen-1 errors are asymmetric: misclassification as gen-2+ (18.8\%) is 3$\times$ more frequent than as gen-0 (6.2\%). Gen-1 text already carries detectable recursive distortion.}
8	\label{tab:confusion}
9	\resizebox{\linewidth}{!}{%
10	\begin{tabular}{lccc}
11	\toprule
12	& \textbf{Pred gen-0} & \textbf{Pred gen-1} & \textbf{Pred gen-2+} \\
13	\midrule
14	\textbf{True gen-0} & 5{,}937 (99.4\%) & 35 (0.6\%) & 0 (0.0\%) \\
15	\textbf{True gen-1} & 368 (6.2\%) & 4{,}437 (75.0\%) & 1{,}113 (18.8\%) \\
16	\textbf{True gen-2+} & 464 (3.0\%) & 3{,}646 (23.3\%) & 11{,}529 (73.7\%) \\
17	\bottomrule
18	\end{tabular}}
19	\end{table}
20	
21	Figure~\ref{fig:confusion-heatmap} provides a heatmap visualization of the confusion matrix.
22	The row-normalized view highlights near-perfect gen-0 classification (99.4\% recall), gen-1 confusion primarily with gen-2+ (18.8\%) rather than gen-0 (6.2\%), and gen-2+ misclassification predominantly into gen-1 (23.3\%), consistent with DDR predictions.
23	
24	\begin{figure}[H]
25	\centering
26	\includegraphics[width=\columnwidth, trim=0 0 344pt 0, clip]{fig_appendix_confusion.pdf}\\[-2pt]
27	{\small (a) Raw counts}
28	\caption{3-class LOGO confusion matrix ($N$\,=\,27{,}529). Gen-0 achieves near-perfect classification; the primary confusion axis is gen-1 $\leftrightarrow$ gen-2+.}
29	\label{fig:confusion-heatmap}
30	\end{figure}
31	
32	\begin{figure}[H]
33	\addtocounter{figure}{-1}
34	\centering
35	\includegraphics[width=\columnwidth, trim=344pt 0 0 0, clip]{fig_appendix_confusion.pdf}\\[-2pt]
36	{\small (b) Row-normalized recall percentages}
37	\caption{(Continued) Row-normalized view of the confusion matrix.}
38	\end{figure}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a78133e2-baa9-4f18-b6bd-24a449788682",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a5eb1178a764b765b",
  "type": "user",
  "uuid": "9439eb7c-f996-4736-b26b-d91c0dc1cc4a",
  "sourceToolAssistantUUID": "a78133e2-baa9-4f18-b6bd-24a449788682",
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

_source line 7 · 2026-05-23T10:22:45.608Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hi74K7YapJtYXjUgN8G8Rb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_dataset_stats.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9439eb7c-f996-4736-b26b-d91c0dc1cc4a",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQQ7DMfo2wbhrJLfBD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "485967f6-af1d-4f6c-962d-fc272fc5ef8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VfQaCsEFUWXJ3dyrgmshu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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

_source line 8 · 2026-05-23T10:22:45.611Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PULDZRzM81fBhs6TD9K3gG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_downstream.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "485967f6-af1d-4f6c-962d-fc272fc5ef8f",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQQ7DMfo2wbhrJLfBD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c067207-f44c-49cc-a0cb-8edd0a618ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VfQaCsEFUWXJ3dyrgmshu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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

_source line 9 · 2026-05-23T10:22:45.619Z_

<details><summary>↩ Tool result · `toolu_01Hi74K7YapJtYXjUgN8G8Rb`</summary>

```text
1	\section{Dataset Statistics}
2	\label{app:dataset-stats}
3	
4	Table~\ref{tab:dataset-stats} reports per-generator sample counts after filtering (removing generation failures, exact duplicates, and passages shorter than 50 whitespace tokens).
5	Under the 3-class evaluation scheme, the dataset contains 7{,}963 gen-0 samples (21.5\%), 7{,}896 gen-1 (21.3\%), and 21{,}199 gen-2+ (57.2\%, combining depths 2--4).
6	The gen-2+ majority reflects the chain structure (three deeper depths per chain vs.\ one each for gen-0 and gen-1); class-balanced sampling is applied during evaluation.
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption[Per-generator sample counts]{Per-generator sample counts after filtering (8 generators, 5 families). Each generator starts from ${\sim}$1{,}000 shared Wikipedia seeds and produces chains of depth 4 (5 texts per chain). Attrition varies by generator due to differing generation failure rates.\protect\footnotemark}
12	\label{tab:dataset-stats}
13	\begin{tabular}{llcc}
14	\toprule
15	\textbf{Generator} & \textbf{Family} & \textbf{Params} & \textbf{Samples} \\
16	\midrule
17	Pythia-1B       & Pythia  & 1.0B & 4{,}555 \\
18	Pythia-2.8B     & Pythia  & 2.8B & 4{,}609 \\
19	OLMo-2-1B      & OLMo    & 1.5B & 4{,}713 \\
20	Qwen3-0.6B     & Qwen    & 0.6B & 4{,}538 \\
21	Qwen3-1.7B     & Qwen    & 1.7B & 4{,}617 \\
22	Qwen3-8B       & Qwen    & 8.2B & 4{,}497 \\
23	Llama-3.2-3B   & Llama   & 3.2B & 4{,}680 \\
24	Mistral-7B-v0.3 & Mistral & 7.0B & 4{,}849 \\
25	\midrule
26	\multicolumn{3}{l}{\textbf{Total}} & \textbf{37{,}058} \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	\footnotetext{Table~\ref{tab:baselines} evaluates on a subset of 34{,}131 samples for which all detector scores (FastDetectGPT, Binoculars, LD-Score, Avg-LogProb) are available.}
31	
32	Figure~\ref{fig:violin} shows the full distribution of each feature across five generation depths (0--4), pooled across all eight generators ($N$\,=\,37{,}058).
33	The violin plots confirm the DDR pattern: drifting features (entropy mean, TTR, hapax ratio) show progressive narrowing and location shift, while shape features (entropy max, tail decay) maintain approximately constant distributions across depths.
34	
35	\begin{figure*}[!htbp]
36	\centering
37	\includegraphics[width=\textwidth]{fig_appendix_violin.pdf}
38	\caption{Feature distributions by generation depth (violin plots, $N$\,=\,37{,}058). Drifting features (entropy mean, TTR, hapax ratio: $|\rho| > 0.60$) show clear location shifts and narrowing with increasing depth. Shape features (entropy max, tail decay: $|\rho| < 0.10$) remain approximately stationary. Quartile lines indicate median and interquartile range.}
39	\label{fig:violin}
40	\end{figure*}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "485967f6-af1d-4f6c-962d-fc272fc5ef8f",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a5eb1178a764b765b",
  "type": "user",
  "uuid": "a034747b-1be3-4942-b676-048879a0dfb4",
  "sourceToolAssistantUUID": "485967f6-af1d-4f6c-962d-fc272fc5ef8f",
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

### Tool result

_source line 10 · 2026-05-23T10:22:45.620Z_

<details><summary>↩ Tool result · `toolu_01PULDZRzM81fBhs6TD9K3gG`</summary>

```text
1	Can depth-aware data curation improve downstream language model quality?
2	We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\ref{tab:downstream}).
3	
4	\begin{table}[ht]
5	\centering
6	\small
7	\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}
8	\label{tab:downstream}
9	\begin{tabular}{lrc}
10	\toprule
11	\textbf{Variant} & \textbf{$n$} & \textbf{Test PPL} \\
12	\midrule
13	All depths            & 12{,}299 & 2.335 $\pm$ 0.000 \\
14	Size-matched (random) & 3{,}951  & 2.367 $\pm$ 0.000 \\
15	Depth 0--1 only       & 3{,}951  & 2.387 $\pm$ 0.001 \\
16	Binary-filtered       & 3{,}951  & 2.389 $\pm$ 0.000 \\
17	Depth 0 only          & 797      & 2.681 $\pm$ 0.001 \\
18	\bottomrule
19	\end{tabular}
20	\end{table}
21	
22	The results are unambiguous: data quantity dominates depth composition.
23	Training on all 12{,}299 samples yields the lowest perplexity (2.335).
24	At equal sample count ($n$\,=\,3{,}951), random subsampling (2.367) \emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).
25	Cross-seed variance is below 0.002 across all variants, which confirms the robustness of this null result.
26	
27	Restricting training to human-only text (depth 0, $n$\,=\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\times$ reduction in data volume rather than depth composition per se.
28	
29	\paragraph{Equivalence testing.}
30	We apply a two one-sided $t$-test (TOST) with a $\pm$2\% relative margin (equivalence bounds $\pm$0.047 on the ppl scale) to formally assess whether the depth-aware and random subsampling conditions produce practically indistinguishable perplexity.
31	At equal sample count ($n$\,=\,3{,}951): size-matched (random) ppl\,=\,2.367 vs.\ depth 0--1 ppl\,=\,2.387, $\Delta$\,=\,0.020.
32	TOST confirms equivalence ($p = 1.1 \times 10^{-4}$); the two curation strategies yield practically indistinguishable downstream quality within the $\pm$2\% margin.
33	Cross-seed standard deviation is below 0.001 for both variants.
34	
35	Comparing the full dataset ($n$\,=\,12{,}299, ppl\,=\,2.335) against the depth-filtered subset ($n$\,=\,3{,}951, ppl\,=\,2.387): TOST \emph{rejects} equivalence (minimum equivalence margin\,=\,0.053, exceeding the $\pm$2\% bound), which confirms that data quantity drives perplexity reduction beyond what depth-aware selection can recover.
36	
37	Knowing the generation depth of a document does not, by itself, make it more or less useful for training; at fixed sample count, depth-aware curation is statistically equivalent to uninformed random subsampling.
38	
39	\subsection*{Margin Sensitivity Analysis}
40	
41	To assess the robustness of the equivalence conclusion to margin choice, we repeat the TOST procedure across multiple equivalence margins \cite{lakens_equivalence}, following the recommendation to report sensitivity across plausible bounds rather than relying on a single threshold (Table~\ref{tab:tost-margins}).
42	
43	\begin{table}[ht]
44	\centering
45	\small
46	\caption{TOST equivalence testing across multiple margins. ``Equiv?'' indicates whether equivalence is established at $\alpha = 0.05$.}
47	\label{tab:tost-margins}
48	\resizebox{\linewidth}{!}{%
49	\begin{tabular}{llcc}
50	\toprule
51	\textbf{Comparison} & \textbf{Margin} & \textbf{Equiv?} & \textbf{TOST $p$} \\
52	\midrule
53	Full (12{,}299) vs.\ Random (3{,}951) & $\pm$1\% & No & 1.0 \\
54	                                        & $\pm$2\% & Yes & $1 \times 10^{-6}$ \\
55	                                        & $\pm$3\% & Yes & $< 10^{-10}$ \\
56	                                        & $\pm$5\% & Yes & $< 10^{-10}$ \\
57	\midrule
58	Full (12{,}299) vs.\ Depth 0--1 (3{,}951) & $\pm$1\% & No & 1.0 \\
59	                                            & $\pm$2\% & No & 1.0 \\
60	                                            & $\pm$3\% & Yes & $< 10^{-10}$ \\
61	                                            & $\pm$5\% & Yes & $< 10^{-10}$ \\
62	\bottomrule
63	\end{tabular}}
64	\end{table}
65	
66	The full dataset vs.\ random subsample comparison passes equivalence at the $\pm$2\% margin ($p = 10^{-6}$), while the full vs.\ depth 0--1 comparison requires a $\pm$3\% margin.
67	In absolute terms, perplexity differences are small: $\Delta$\,=\,0.032 (full vs.\ random, 1.4\% of baseline) and $\Delta$\,=\,0.052 (full vs.\ depth 0--1, 2.2\% of baseline).
68	
69	Cohen's $d$ values are 86.0 (full vs.\ random) and 119.7 (full vs.\ depth 0--1).
70	These appear large but are unreliable: with only $n$\,=\,3 seeds per condition, the pooled standard deviation is extremely small ($<$0.001), artificially inflating $d$.
71	The inflated effect sizes reflect low seed-level variance (confirming reproducibility) rather than practically meaningful perplexity differences.
72	The TOST framework with pre-specified relative margins provides a more appropriate assessment than Cohen's $d$ in this low-seed regime.
73	However, with only $n{=}3$ seeds per condition, the TOST results have limited generalizability: the test is valid given observed variance but the conclusion generalizes over only three random seeds. We characterize this as a preliminary observation rather than a definitive null result.
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c067207-f44c-49cc-a0cb-8edd0a618ff8",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a5eb1178a764b765b",
  "type": "user",
  "uuid": "fa857fb7-a61d-4aa8-b2bc-34f84c99e8ff",
  "sourceToolAssistantUUID": "9c067207-f44c-49cc-a0cb-8edd0a618ff8",
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

_source line 11 · 2026-05-23T10:22:45.793Z_

<details open><summary>🔧 Tool call — Read · `toolu_018yi15TcSzun3jRGBRYBq1u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_finer_depth.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa857fb7-a61d-4aa8-b2bc-34f84c99e8ff",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQQ7DMfo2wbhrJLfBD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cdc3b99c-e723-4e74-934a-cf76eee1ddd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VfQaCsEFUWXJ3dyrgmshu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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

_source line 12 · 2026-05-23T10:22:45.796Z_

<details><summary>↩ Tool result · `toolu_018yi15TcSzun3jRGBRYBq1u`</summary>

```text
1	We evaluate finer-grained 5-class depth classification (gen-0 through gen-4) using the same 7-feature ensemble and LOGO protocol described in \S\ref{sec:method}.
2	
3	\begin{table}[ht]
4	\centering
5	\small
6	\caption{5-class LOGO evaluation. Each row holds out one generator for testing, training on the remaining five.}
7	\label{tab:5class-logo}
8	\resizebox{\linewidth}{!}{%
9	\begin{tabular}{lcccc}
10	\toprule
11	\textbf{Held-out Generator} & \textbf{Macro F1} & \textbf{Weighted F1} & \textbf{Accuracy} \\
12	\midrule
13	OLMo-2-1B       & 0.484 & 0.506 & 0.524 \\
14	Pythia-1B        & 0.543 & 0.568 & 0.575 \\
15	Pythia-2.8B      & 0.523 & 0.540 & 0.560 \\
16	Qwen3-0.6B      & 0.513 & 0.521 & 0.546 \\
17	Qwen3-1.7B      & 0.510 & 0.536 & 0.548 \\
18	Qwen3-8B        & 0.434 & 0.455 & 0.493 \\
19	\midrule
20	\textbf{Average} & \textbf{0.501 $\pm$ 0.038} & \textbf{0.521} & \textbf{0.541} \\
21	\bottomrule
22	\end{tabular}}
23	\end{table}
24	
25	\begin{table}[ht]
26	\centering
27	\small
28	\caption{Per-class F1 averaged across all six LOGO folds.}
29	\label{tab:5class-perclass}
30	\resizebox{\linewidth}{!}{%
31	\begin{tabular}{lccccc}
32	\toprule
33	\textbf{Metric} & \textbf{Gen-0} & \textbf{Gen-1} & \textbf{Gen-2} & \textbf{Gen-3} & \textbf{Gen-4} \\
34	\midrule
35	Avg F1      & 0.921 & 0.634 & 0.268 & 0.259 & 0.423 \\
36	\bottomrule
37	\end{tabular}}
38	\end{table}
39	
40	\paragraph{Analysis.}
41	Moving from 3-class (gen-0 / gen-1 / gen-2+) to 5-class classification reduces LOGO macro F1 to approximately 0.50 (six-generator subset; the 3-class baseline for this subset is comparable to the 8-generator result of 0.762 in Table~\ref{tab:logo-results}).
42	The degradation is concentrated in the middle depths: gen-2 and gen-3 achieve only 0.268 and 0.259 F1, respectively.
43	The aggregated confusion matrix reveals that 36.5\% of true gen-2 samples are misclassified as gen-1, while 37.8\% of true gen-3 samples are predicted as gen-4.
44	Adjacent depths (gen-2$\leftrightarrow$gen-3, gen-3$\leftrightarrow$gen-4) account for the majority of errors, consistent with the intuition that deeper recursive generations converge in surface-level statistical signatures.
45	Gen-0 (human text) remains highly distinguishable (F1 = 0.921), and gen-1 retains moderate separability (F1 = 0.634).
46	Shape features that are near-stationary in the 3-class setting become substantially more important under 5-class evaluation: permutation importance of entropy\_std increases by 93\% and tail\_decay by 400\% relative to 3-class, yet these gains are insufficient to resolve adjacent depths.
47	These results support the 3-class grouping adopted in the main paper: collapsing gen-2+ preserves the most informative boundary (human vs.\ first-generation vs.\ deeper recursion) while avoiding the noise introduced by near-identical adjacent depths.
48	
49	\paragraph{Classifier comparison.}
50	To verify that 5-class degradation reflects feature-level limitations rather than classifier choice, we evaluate four alternatives under the same protocol: HistGradientBoosting (macro F1\,=\,0.501, 95\% bootstrap CI [0.496, 0.506]), random forest (0.476), logistic regression (0.447), and Frank-Hall ordinal reduction (0.451).
51	All classifiers perform comparably to the default XGBoost ensemble (0.501), indicating that classifier capacity is not the bottleneck.
52	The gen-2/gen-3 boundary is the primary failure mode across all methods: these two classes are effectively inseparable with the current feature set. This establishes 3-class granularity as the practical ceiling for surface and entropy features.
53	At the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\S\ref{sec:results}), which confirms that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdc3b99c-e723-4e74-934a-cf76eee1ddd9",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a5eb1178a764b765b",
  "type": "user",
  "uuid": "a37ca0ff-a096-46a4-ae1f-8bee976f9abc",
  "sourceToolAssistantUUID": "cdc3b99c-e723-4e74-934a-cf76eee1ddd9",
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

_source line 13 · 2026-05-23T10:22:46.369Z_

<details open><summary>🔧 Tool call — Read · `toolu_019XKUCYh7oEM8so5ouU6UKB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_human_edit.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a37ca0ff-a096-46a4-ae1f-8bee976f9abc",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQQ7DMfo2wbhrJLfBD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1c92f9d0-aa4f-4a7d-9676-9d13a08091d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VfQaCsEFUWXJ3dyrgmshu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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

_source line 14 · 2026-05-23T10:22:46.373Z_

<details><summary>↩ Tool result · `toolu_019XKUCYh7oEM8so5ouU6UKB`</summary>

```text
1	We assess robustness to post-generation text modification by randomly replacing words at varying rates and re-evaluating the 8-generator LOGO pipeline (Table~\ref{tab:human-edit}).
2	Random word replacement represents a worst-case perturbation: real human editing preserves semantic coherence, so practical degradation is expected to be substantially lower than these estimates.
3	
4	\begin{table}[ht]
5	\centering
6	\small
7	\caption{Robustness to random word replacement under 8-gen LOGO evaluation (binary: gen-1 vs.\ gen-2+). Bootstrap 95\% CIs on binary F1 ($n$\,=\,1000).}
8	\label{tab:human-edit}
9	\resizebox{\linewidth}{!}{%
10	\begin{tabular}{lccc}
11	\toprule
12	\textbf{Perturbation rate} & \textbf{Binary F1} & \textbf{95\% CI} & \textbf{3-class F1} \\
13	\midrule
14	0\% (baseline) & 0.695 & [0.680, 0.710] & 0.737 \\
15	5\%            & 0.650 & [0.635, 0.666] & 0.641 \\
16	10\%           & 0.614 & [0.599, 0.629] & 0.492 \\
17	20\%           & 0.591 & [0.576, 0.605] & 0.367 \\
18	\bottomrule
19	\end{tabular}}
20	\end{table}
21	
22	Binary depth discrimination (gen-1 vs.\ gen-2+) degrades sublinearly: the first 5\% replacement causes the largest drop ($-$4.6\,pp), with diminishing marginal impact thereafter ($-$3.6\,pp for 5\%$\to$10\%, $-$2.3\,pp for 10\%$\to$20\%).
23	At 10\% replacement, binary F1 remains 0.614, well above the 0.50 random baseline, which indicates that depth signal survives moderate perturbation.
24	
25	Three-class classification is more sensitive (0.737$\to$0.367 at 20\%), because distinguishing gen-0 from gen-1 relies heavily on lexical diversity features (TTR, hapax ratio) that are directly disrupted by word replacement.
26	The binary metric, which excludes gen-0, is inherently more robust since it depends primarily on reference-model entropy features distributed across many tokens.
27	
28	\paragraph{Feature subset degradation.}
29	Table~\ref{tab:feature-degrade} compares perturbation robustness of the full 7-feature ensemble against an entropy-only subset (5 reference-model features).
30	The higher unperturbed binary F1 of the entropy-only subset (0.833 vs.\ 0.695) reflects the strong discriminability of reference-model features for the coarse binary task (gen-1 vs.\ gen-2+); however, lexical features are essential for the finer-grained ordinal task (3-class F1: 0.737 vs.\ 0.688) and provide greater robustness under perturbation.
31	At 20\% replacement, the 7-feature ensemble surpasses entropy-only on binary F1 (0.591 vs.\ 0.566), despite starting from a lower baseline.
32	Random word replacement drastically alters per-token context and makes entropy features (computed over the full token sequence) extremely sensitive to noise.
33	Lexical features (TTR, hapax ratio), as document-level summary statistics, are more stable under per-word perturbation and act as stabilizers in the full ensemble.
34	The crossover confirms that degradation in the full feature set reflects genuine signal disruption rather than a lexical-feature artifact.
35	
36	\begin{table}[ht]
37	\centering
38	\small
39	\caption{Feature subset degradation under random word replacement (8-gen LOGO). Entropy-only: 5 reference-model features; 7-feature: full ensemble including lexical features.}
40	\label{tab:feature-degrade}
41	\resizebox{\linewidth}{!}{%
42	\begin{tabular}{lcccc}
43	\toprule
44	\textbf{Perturb.} & \textbf{Ent-only Bin} & \textbf{7-feat Bin} & \textbf{Ent-only 3-cl} & \textbf{7-feat 3-cl} \\
45	\midrule
46	0\%  & 0.833 & 0.695 & 0.688 & 0.737 \\
47	5\%  & 0.736 & 0.650 & 0.539 & 0.641 \\
48	10\% & 0.657 & 0.614 & 0.427 & 0.492 \\
49	20\% & 0.566 & 0.591 & 0.314 & 0.367 \\
50	\bottomrule
51	\end{tabular}}
52	\end{table}
53	
54	\paragraph{Baseline comparison.}
55	Table~\ref{tab:baseline-robustness} compares robustness across detection methods under identical perturbation conditions (8-gen LOGO, binary: gen-1 vs.\ gen-2+).
56	
57	\begin{table}[ht]
58	\centering
59	\small
60	\caption{Baseline robustness under random word replacement (8-gen LOGO, binary F1). Bold indicates highest F1 at each perturbation rate. (Baseline scores use default XGBoost settings; trends are consistent with the unified configuration in Table~\ref{tab:baselines}.)}
61	\label{tab:baseline-robustness}
62	\begin{tabular}{lcccc}
63	\toprule
64	\textbf{Method} & \textbf{0\%} & \textbf{5\%} & \textbf{10\%} & \textbf{20\%} \\
65	\midrule
66	7-feature ensemble & \textbf{0.695} & 0.650 & 0.614 & 0.591 \\
67	LD-Score           & 0.677 & \textbf{0.673} & \textbf{0.677} & \textbf{0.671} \\
68	Avg-LogProb        & 0.682 & 0.419 & 0.335 & 0.375 \\
69	FastDetectGPT      & 0.571 & 0.437 & 0.468 & 0.514 \\
70	Binoculars\textsuperscript{\dag}         & 0.500 & 0.461 & 0.446 & 0.425 \\
71	\bottomrule
72	\end{tabular}
73	
74	\vspace{2pt}
75	{\footnotesize \textsuperscript{\dag}Binoculars operates at chance level on this binary task; its degradation figures are not meaningful.}
76	\end{table}
77	
78	The 7-feature ensemble achieves the highest unperturbed binary F1 (0.695), but LD-Score surpasses it under perturbation due to near-zero degradation ($-$0.6\,pp across the full 0\%$\to$20\% range).
79	FastDetectGPT and Avg-LogProb exhibit non-monotonic degradation at higher perturbation rates, likely because severe perturbation introduces distributional artifacts that these token-level methods detect as anomalous.
80	Avg-LogProb is the most fragile overall ($-$34.7\,pp at 10\%), while FastDetectGPT drops sharply at 5\% ($-$13.4\,pp) before partially recovering.
81	LD-Score is nearly invariant to perturbation, consistent with its reliance on corpus-level distributional divergence rather than per-token likelihoods.
82	The 7-feature ensemble offers the highest starting performance among single-reference methods, with sublinear degradation ($-$10.4\,pp at 20\%).
83	
84	\paragraph{LLM-simulated sentence regeneration.}
85	To test robustness under semantically coherent editing, we use Qwen3-0.6B-Base to randomly regenerate 1--3 sentences per passage (avg 1.69 sentences, ${\sim}$50\% edit distance) and re-evaluate the 8-gen LOGO pipeline.
86	Binary F1 drops from 0.692 to 0.647 ($-$4.5\,pp, 6.5\% relative); 3-class F1 drops from 0.739 to 0.667 ($-$7.1\,pp, 9.7\% relative).
87	The binary degradation ($-$4.5\,pp) is nearly identical to that caused by 5\% random word replacement ($-$4.6\,pp), despite the LLM rephrase altering ${\sim}$50\% of characters.
88	This asymmetry arises because LLM-generated replacements preserve the underlying statistical signature of the generation process (entropy dynamics, depth-accumulated distributional drift), whereas random word substitution directly destroys local statistical signals.
89	Depth profiling thus captures deep generative structure that survives semantic-preserving edits.
90	
91	\paragraph{Seed complexity.}
92	Performance is stable across seed text complexity: stratifying seeds by vocabulary richness (TTR terciles) yields maximum F1 variation of 1.1\,pp across groups.
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c92f9d0-aa4f-4a7d-9676-9d13a08091d1",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a5eb1178a764b765b",
  "type": "user",
  "uuid": "fea413b8-cf5a-4393-8f08-5eeadc0c6af0",
  "sourceToolAssistantUUID": "1c92f9d0-aa4f-4a7d-9676-9d13a08091d1",
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

_source line 15 · 2026-05-23T10:22:46.473Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Eo6uGr1Pr4Z5FB9TQX9HEf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fea413b8-cf5a-4393-8f08-5eeadc0c6af0",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQQ7DMfo2wbhrJLfBD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d09ccb7b-2507-46a9-a8df-193b718bd666",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VfQaCsEFUWXJ3dyrgmshu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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

_source line 16 · 2026-05-23T10:22:46.477Z_

<details><summary>↩ Tool result · `toolu_01Eo6uGr1Pr4Z5FB9TQX9HEf`</summary>

```text
1	% Appendix — Length Confound Analysis
2	% Data source: 8-generator LOGO corpus (37,058 samples)
3	
4	Surface diversity features (TTR, hapax ratio) mechanically depend on text length:
5	shorter texts yield higher type-token ratios by construction.
6	If generation depth systematically shortens text, observed depth trends could be length artifacts rather than genuine distributional shifts.
7	We investigate with three complementary analyses.
8	
9	\paragraph{(a) Length--depth correlation.}
10	Spearman rank correlation between word count and generation depth is weak across all eight generators ($|\rho| < 0.14$); depth does not systematically shorten or lengthen text in our corpus.
11	
12	\paragraph{(b) Length--feature correlations.}
13	While length--depth correlation is weak, individual features show moderate length dependence:
14	tail\_decay ($|\rho| = 0.38$), hapax\_ratio ($|\rho| = 0.30$), and TTR ($|\rho| = 0.29$).
15	Reference-model features show weaker length correlations (entropy\_mean $|\rho| = 0.09$, entropy\_std $|\rho| = 0.18$).
16	This motivates the length-matched evaluation below: if length mediates some depth--feature association, controlling for length will reduce classification performance.
17	
18	\paragraph{(c) Length-matched classification.}
19	We subsample the dataset so that word-count distributions are equalized across depth classes (gen-0\,/\,gen-1\,/\,gen-2+), then retrain the binary XGBoost classifier under pooled LOGO (8-fold).
20	Length-matched binary F1\,=\,0.724, down from 0.770 on the unmatched set ($\Delta$\,=\,$-$0.046).
21	The matched subset is smaller than the full corpus; a random-subsample control at equal $N$ (below) isolates the deconfounding effect from the sample-size reduction.
22	To distinguish this from a sample-size effect, we run a random-subsample control at equal $N$ without length matching: F1\,=\,0.767, which confirms that the 0.046 drop reflects genuine length deconfounding rather than reduced data.
23	
24	\paragraph{Conclusion.}
25	Length accounts for approximately 6\% of discriminative performance ($\Delta$\,=\,0.046 out of 0.770).
26	The majority of the depth signal is length-independent: length-matched F1 (0.724) remains far above chance and significantly above all individual detection baselines (\S\ref{sec:results-baselines}).
27	Surface features (TTR, hapax\_ratio) partially co-vary with length, but their depth-discriminative contribution persists after length control, consistent with generation-induced vocabulary compression operating independently of text truncation.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d09ccb7b-2507-46a9-a8df-193b718bd666",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a5eb1178a764b765b",
  "type": "user",
  "uuid": "e09f7609-6cda-4a5f-89eb-4034bcca3e73",
  "sourceToolAssistantUUID": "d09ccb7b-2507-46a9-a8df-193b718bd666",
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

_source line 17 · 2026-05-23T10:22:46.917Z_

<details open><summary>🔧 Tool call — Read · `toolu_012zCyWaeS7Xpg96odiGtcdo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_lofo.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e09f7609-6cda-4a5f-89eb-4034bcca3e73",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQQ7DMfo2wbhrJLfBD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c452145e-fed5-48bc-b3e3-2a6063488193",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VfQaCsEFUWXJ3dyrgmshu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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

_source line 18 · 2026-05-23T10:22:46.922Z_

<details><summary>↩ Tool result · `toolu_012zCyWaeS7Xpg96odiGtcdo`</summary>

```text
1	We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.789).
2	
3	\begin{table}[ht]
4	\centering
5	\small
6	\caption{Leave-one-feature-out ablation (6-gen LOGO). Each row drops one feature and re-evaluates with the LOGO protocol. Sorted by impact magnitude.}
7	\label{tab:lofo}
8	\begin{tabular}{lcc}
9	\toprule
10	\textbf{Dropped feature} & \textbf{LOGO F1} & $\boldsymbol{\Delta}$ \textbf{vs Full} \\
11	\midrule
12	entropy\_max    & 0.774 & $-$1.50\,pp \\
13	entropy\_mean   & 0.783 & $-$0.63\,pp \\
14	ttr             & 0.784 & $-$0.55\,pp \\
15	hapax\_ratio    & 0.785 & $-$0.42\,pp \\
16	tail\_decay     & 0.786 & $-$0.33\,pp \\
17	entropy\_std    & 0.786 & $-$0.29\,pp \\
18	entropy\_min    & 0.789 & $+$0.01\,pp \\
19	\midrule
20	Full (7 features) & 0.789 & --- \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	\paragraph{Analysis.}
26	Entropy\_max causes the largest degradation when removed ($-$1.5\,pp), despite ranking only fourth in permutation importance (split frequency 0.063). This indicates that entropy\_max provides unique signal (capturing the most surprising token under the reference model) that is not redundant with other features.
27	Conversely, entropy\_min is fully redundant ($\Delta$\,=\,+0.01\,pp), consistent with its near-zero permutation importance (0.015).
28	Six of seven features contribute positively to the ensemble, which confirms that the 7-feature design is not over-specified.
29	
30	To verify that feature importance generalizes beyond the original 6-generator subset, we repeat the LOFO analysis on the full 8-generator set (37,058 samples, 10-fold stratified CV). Table~\ref{tab:lofo-8gen} confirms consistent rankings: \texttt{entropy\_max} remains the most impactful feature ($\Delta=-0.019$), followed by \texttt{entropy\_mean} ($\Delta=-0.012$). All seven features contribute positively, with no feature becoming redundant upon dataset expansion.
31	
32	\paragraph{Minimal sufficient subset.}
33	To assess feature redundancy, we evaluate all $\binom{7}{2}{=}21$ two-feature subsets under 10-fold stratified CV (8-gen, 3-class).
34	The best pair is \{entropy\_mean, entropy\_max\}, achieving F1\,=\,0.68---one drifting and one stationary feature---which captures 88\% of the full-ensemble performance (0.771) and confirms that the DDR partition's two components are individually informative.
35	Adding the remaining five features yields +9.1\,pp, indicating that the full set provides meaningful complementarity beyond the minimal core; nevertheless, the two-feature result demonstrates that the depth signal is not an artifact of feature-set size.
36	
37	\begin{table}[ht]
38	\centering
39	\small
40	\caption{Leave-one-feature-out importance on the full 8-generator set (37,058 samples). Ranking is consistent with the 6-generator subset (Table~\ref{tab:lofo}).}
41	\label{tab:lofo-8gen}
42	\begin{tabular}{lcc}
43	\toprule
44	\textbf{Configuration} & \textbf{3-class F1} & $\boldsymbol{\Delta}$ \\
45	\midrule
46	Full (7 features) & 0.771 & --- \\
47	\midrule
48	$-$ entropy\_max    & 0.752 & $-$0.019 \\
49	$-$ entropy\_mean   & 0.759 & $-$0.012 \\
50	$-$ entropy\_std    & 0.763 & $-$0.007 \\
51	$-$ ttr             & 0.764 & $-$0.007 \\
52	$-$ hapax\_ratio    & 0.765 & $-$0.005 \\
53	$-$ entropy\_min    & 0.766 & $-$0.005 \\
54	$-$ tail\_decay     & 0.767 & $-$0.004 \\
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c452145e-fed5-48bc-b3e3-2a6063488193",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a5eb1178a764b765b",
  "type": "user",
  "uuid": "4ba00ccd-d37e-4e26-8937-f7a1bafb74b9",
  "sourceToolAssistantUUID": "c452145e-fed5-48bc-b3e3-2a6063488193",
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

_source line 19 · 2026-05-23T10:22:47.111Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CVtGow8DdnQ81T4ZQf3zCx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ablation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ba00ccd-d37e-4e26-8937-f7a1bafb74b9",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQQ7DMfo2wbhrJLfBD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "892e8ec8-f678-418e-ac68-8db50982b86c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VfQaCsEFUWXJ3dyrgmshu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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

_source line 20 · 2026-05-23T10:22:47.115Z_

<details><summary>↩ Tool result · `toolu_01CVtGow8DdnQ81T4ZQf3zCx`</summary>

```text
1	This appendix presents feature ablation results supporting the complementarity analysis in \S\ref{sec:results-differential}.
2	
3	\begin{table}[t]
4	\centering
5	\footnotesize
6	\caption{Feature ablation (8-gen, 10-fold stratified CV, 3-class). Full $>$ surface (+8.5\,pp) and Full $>$ reference (+6.0\,pp) confirms complementarity.}
7	\label{tab:ablation}
8	\begingroup
9	\renewcommand{\arraystretch}{1.15}
10	\begin{tabular}{lcc}
11	\toprule
12	\textbf{Feature set} & \textbf{F1} & \textbf{Top feature (imp.)} \\
13	\midrule
14	Full (7 features)     & 0.773 & hapax\_ratio (0.35) \\
15	Surface only (2)      & 0.688 & hapax\_ratio (0.41) \\
16	Reference only (5)    & 0.713 & entropy\_mean (0.27) \\
17	\bottomrule
18	\end{tabular}
19	\endgroup
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "892e8ec8-f678-418e-ac68-8db50982b86c",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a5eb1178a764b765b",
  "type": "user",
  "uuid": "d125641e-c0cb-4a30-b029-143aa8d3ce9f",
  "sourceToolAssistantUUID": "892e8ec8-f678-418e-ac68-8db50982b86c",
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

_source line 21 · 2026-05-23T10:22:47.208Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tzq4V5BpEgphbn9oA5zAYM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_seed_control.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d125641e-c0cb-4a30-b029-143aa8d3ce9f",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQQ7DMfo2wbhrJLfBD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4b25a01a-ab1e-4bb6-9569-e9919bbd1007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VfQaCsEFUWXJ3dyrgmshu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 17476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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

_source line 22 · 2026-05-23T10:22:47.211Z_

<details><summary>↩ Tool result · `toolu_01Tzq4V5BpEgphbn9oA5zAYM`</summary>

```text
1	\section{Independent-Seed Control}
2	\label{app:seed-control}
3	
4	\begingroup\setlength{\parskip}{2pt plus 1pt}
5	
6	To test for topic-level leakage from shared seeds across generators, we construct an independent-seed evaluation where Pythia-2.8B and OLMo-2-1B use completely disjoint Wikipedia seed pools (500 seeds each, zero overlap).
7	Each generator produces depth-0 through depth-4 chains on its own seed pool; features are extracted with the same Pythia-410M reference model.
8	We then train a 7-feature XGBoost classifier on one generator's data and test on the other, in both directions.
9	
10	\begin{table}[ht]
11	\centering
12	\small
13	\caption{Independent-seed cross-generator evaluation (binary: gen-1 vs.\ gen-2+). Disjoint seed pools eliminate any possibility of topic-based leakage. The average independent-seed F1 (0.680) is within 1.4\,pp of the shared-seed LOGO baseline (0.694). The classifier thus captures generative degradation patterns rather than seed-specific topic content.}
14	\label{tab:seed-control}
15	\resizebox{\linewidth}{!}{%
16	\renewcommand{\arraystretch}{1.15}%
17	\begin{tabular}{lcc}
18	\toprule
19	\textbf{Setting} & \textbf{Binary F1} & \textbf{95\% CI} \\
20	\midrule
21	Pythia-2.8B $\rightarrow$ OLMo-2-1B & 0.695 & [0.673, 0.717] \\
22	OLMo-2-1B $\rightarrow$ Pythia-2.8B & 0.666 & [0.643, 0.689] \\
23	\midrule
24	Independent-seed average & 0.680 & --- \\
25	Shared-seed LOGO (reference) & 0.694 & [0.688, 0.700] \\
26	\bottomrule
27	\end{tabular}}
28	\end{table}
29	
30	The small gap ($-$1.4\,pp) between independent-seed and shared-seed evaluation falls within bootstrap confidence intervals, and both directions individually exceed 0.66.
31	Combined with the seed-level demeaning control (\S\ref{sec:results-classification}), these results provide converging evidence that depth classification is driven by distributional properties of recursive generation, not topic identity.
32	
33	\paragraph{Semantic similarity analysis.}
34	Embedding cosine similarity between consecutive depth steps increases monotonically: 0$\rightarrow$1 (0.622), 1$\rightarrow$2 (0.683), 2$\rightarrow$3 (0.801), 3$\rightarrow$4 (0.859).
35	Deeper generations are thus \emph{more} semantically similar to their inputs, yet the classifier still distinguishes depth classes, suggesting that the depth signal resides in distributional rather than topical properties.
36	Prompt type modulates the baseline similarity level (continuation 0.717 $<$ elaboration 0.809 $\approx$ rewriting 0.808), plausibly because semantic-preservation constraints reduce topic drift while leaving the distributional location shift intact.
37	
38	\endgroup
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b25a01a-ab1e-4bb6-9569-e9919bbd1007",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a5eb1178a764b765b",
  "type": "user",
  "uuid": "ca1f15cc-3a0d-4a11-a5a0-46011f39d46f",
  "sourceToolAssistantUUID": "4b25a01a-ab1e-4bb6-9569-e9919bbd1007",
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

_source line 23 · 2026-05-23T10:22:47.218Z_

<details open><summary>🔧 Tool call — Read · `toolu_019iSK8FbjZMBfnD9rrMLMUZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_error_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca1f15cc-3a0d-4a11-a5a0-46011f39d46f",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQQ7DMfo2wbhrJLfBD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "53778243-ff78-408e-9b7a-4114a4d0e674",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015VfQaCsEFUWXJ3dyrgmshu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 17476,
      "output_tokens": 873,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 660
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 873,
          "cache_read_input_tokens": 17476,
          "cache_creation_input_tokens": 660,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 660,
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

_source line 24 · 2026-05-23T10:22:47.221Z_

<details><summary>↩ Tool result · `toolu_019iSK8FbjZMBfnD9rrMLMUZ`</summary>

```text
1	We analyze misclassification patterns in the binary LOGO task (gen-1 vs.\ gen-2+) across 29,095 test samples (overall error rate 28.1\%).
2	
3	\paragraph{Error asymmetry.}
4	The error distribution is highly asymmetric: 86.2\% of errors are false negatives (gen-2+ predicted as gen-1), while only 13.8\% are false positives (Table~\ref{tab:error-analysis}).
5	The classifier systematically under-predicts depth, consistent with the DDR pattern: shallow gen-2+ samples that have not yet accumulated sufficient distributional drift are indistinguishable from gen-1.
6	Among generators, Mistral-7B shows the highest error rate (45.0\%), while Pythia-1B is easiest (18.2\%), suggesting that larger models produce gen-2+ text closer to the gen-1 distribution.
7	
8	\begin{table}[H]
9	\centering
10	\small
11	\caption{Binary classification error analysis (gen-1 vs.\ gen-2+) under LOGO cross-validation. FP: gen-1 misclassified as gen-2+; FN: gen-2+ misclassified as gen-1. Errors are dominated by false negatives (86.2\%).}
12	\label{tab:error-analysis}
13	\begin{tabular}{lrrrr}
14	\toprule
15	\textbf{Generator} & $N$ & \textbf{FP} & \textbf{FN} & \textbf{Err.\%} \\
16	\midrule
17	Pythia-1B & 3560 & 188 & 460 & 18.2 \\
18	Pythia-2.8B & 3614 & 129 & 737 & 24.0 \\
19	OLMo-2-1B & 3718 & 154 & 900 & 28.3 \\
20	Qwen3-0.6B & 3542 & 234 & 511 & 21.0 \\
21	Qwen3-1.7B & 3621 & 175 & 639 & 22.5 \\
22	Qwen3-8B & 3502 & 93 & 1104 & 34.2 \\
23	Llama-3.2-3B & 3685 & 82 & 1030 & 30.2 \\
24	Mistral-7B & 3853 & 75 & 1659 & 45.0 \\
25	\midrule
26	\textbf{Overall} & 29095 & 1130 & 7040 & 28.1 \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
31	\paragraph{Per-depth error rates.}
32	Error rates decrease monotonically with depth (Table~\ref{tab:error-depth}): depth-2 samples are the primary failure point (48.4\% error rate), followed by depth-3 (29.2\%) and depth-4 (20.3\%).
33	The monotonic decrease confirms that deeper generations accumulate progressively stronger depth signatures; the gen-1$\to$gen-2 transition is the hardest boundary.
34	
35	\begin{table}[H]
36	\centering
37	\small
38	\caption{Error rate by generation depth in binary classification. Depth-2 exhibits the highest misclassification rate (48.4\%), confirming the gen-1$\to$gen-2 transition as the primary confusion boundary.}
39	\label{tab:error-depth}
40	\begin{tabular}{crrrl}
41	\toprule
42	\textbf{Depth} & $N$ & \textbf{Errors} & \textbf{Rate (\%)} & \textbf{Type} \\
43	\midrule
44	1 & 7896 & 1130 & 14.3 & FP \\
45	2 & 7512 & 3637 & 48.4 & FN \\
46	3 & 7032 & 2051 & 29.2 & FN \\
47	4 & 6655 & 1352 & 20.3 & FN \\
48	\bottomrule
49	\end{tabular}
50	\end{table}
51	
52	\paragraph{Feature-level explanation.}
53	Misclassified samples occupy the overlap zone between gen-1 and gen-2+ distributions (Table~\ref{tab:error-features}): they exhibit elevated entropy ($\bar{H}$: 2.26 vs.\ 1.57, $p<10^{-300}$) and lexical diversity (TTR: 0.464 vs.\ 0.302), retaining gen-1-like characteristics.
54	In contrast, shape features show no discriminating power: entropy max ($p = \text{n.s.}$) and tail decay ($p = \text{n.s.}$), consistent with the DDR pattern (\S\ref{sec:results-differential}).
55	
56	\begin{table}[H]
57	\centering
58	\small
59	\caption{Feature comparison between correctly and incorrectly classified samples. Misclassified samples show significantly higher entropy and lexical diversity but no difference in shape features.}
60	\label{tab:error-features}
61	\begin{tabular}{lcccl}
62	\toprule
63	\textbf{Feature} & \textbf{Correct} & \textbf{Incorrect} & $\Delta$ & $p$ \\
64	\midrule
65	$\bar{H}$ & 1.5700 & 2.2618 & +0.6918 & $<10^{-300}$ $^{***}$ \\
66	$\sigma_H$ & 1.6227 & 1.7413 & +0.1186 & $<10^{-300}$ $^{***}$ \\
67	$H_{\min}$ & 0.0281 & 0.0330 & +0.0049 & 1.0e-294 $^{***}$ \\
68	$H_{\max}$ & 7.5255 & 7.5251 & -0.0004 & n.s. \\
69	$\beta_{\mathrm{tail}}$ & -0.0023 & -0.0023 & +0.0000 & n.s. \\
70	TTR & 0.3024 & 0.4635 & +0.1612 & $<10^{-300}$ $^{***}$ \\
71	Hapax & 0.1760 & 0.3131 & +0.1371 & $<10^{-300}$ $^{***}$ \\
72	\bottomrule
73	\end{tabular}
74	\end{table}
75	
76	\paragraph{3-class confusion matrix.}
77	Table~\ref{tab:confusion-3class} shows the aggregated confusion matrix: gen-0 is near-perfectly classified ($>$99\%), while gen-1 and gen-2+ exhibit substantial cross-contamination (30.2\% of gen-2+ predicted as gen-1), consistent with the binary error analysis.
78	
79	\begin{table}[H]
80	\centering
81	\small
82	\caption{Aggregated 3-class confusion matrix (\%) across 8-fold LOGO. Gen-0 is near-perfectly classified, while gen-2+ is frequently confused with gen-1.}
83	\label{tab:confusion-3class}
84	\begin{tabular}{l|ccc}
85	\toprule
86	 & \multicolumn{3}{c}{\textbf{Predicted}} \\
87	\textbf{True} & gen-0 & gen-1 & gen-2+ \\
88	\midrule
89	gen-0 & 99.2 & 0.8 & 0.1 \\
90	gen-1 & 7.3 & 78.4 & 14.3 \\
91	gen-2+ & 3.0 & 30.2 & 66.7 \\
92	\bottomrule
93	\end{tabular}
94	\end{table}
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53778243-ff78-408e-9b7a-4114a4d0e674",
  "isSidechain": true,
  "promptId": "d0f86f7c-616c-4898-b66f-e3b72f669d55",
  "agentId": "a5eb1178a764b765b",
  "type": "user",
  "uuid": "bbd1c0a9-94c8-4ea5-a06e-60cb5b7cd8ef",
  "sourceToolAssistantUUID": "53778243-ff78-408e-9b7a-4114a4d0e674",
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

_source line 25 · 2026-05-23T10:23:34.816Z_

Now I have all the file contents. Let me extract and organize all the table data systematically.

## COMPLETE TABLE DATA EXTRACTION

**appendix_classifier.tex**

Table 1: LOGO macro-F1 across three classifiers (Table~\ref{tab:alt-classifier})
- XGBoost: Avg F1 = 0.789; OLMo-2 = 0.764; Py-1B = 0.856; Py-2.8B = 0.804; Qw-0.6B = 0.824; Qw-1.7B = 0.806; Qw-8B = 0.683
- Random Forest: Avg F1 = 0.790; OLMo-2 = 0.764; Py-1B = 0.856; Py-2.8B = 0.804; Qw-0.6B = 0.825; Qw-1.7B = 0.807; Qw-8B = 0.684
- Logistic Regression: Avg F1 = 0.725; OLMo-2 = 0.719; Py-1B = 0.781; Py-2.8B = 0.740; Qw-0.6B = 0.745; Qw-1.7B = 0.743; Qw-8B = 0.624
- Baseline chance for three classes: 0.33

Table 2: XGBoost max_depth sensitivity (Table~\ref{tab:xgb-sensitivity})
- max_depth 3: 3-class F1 = 0.752; Binary F1 = 0.700
- max_depth 4: 3-class F1 = 0.759; Binary F1 = 0.699
- max_depth 6: 3-class F1 = 0.769; Binary F1 = 0.700
- max_depth 8: 3-class F1 = 0.772; Binary F1 = 0.699
- Range values: 3-class F1 range = 2.0 pp (0.752-0.772); binary F1 range = 0.699-0.700

Table 3: Depth classification under varying temperature (Table~\ref{tab:sampling-ablation})
- Pythia-2.8B, Temp 0.5: LOGO Binary F1 = 0.814, CI [.798, .828], ρ(ent. mean) = -0.58
- Pythia-2.8B, Temp 0.7: LOGO Binary F1 = 0.740, CI [.725, .755], ρ(ent. mean) = -0.60
- Pythia-2.8B, Temp 0.9: LOGO Binary F1 = 0.480, CI [.465, .498], ρ(ent. mean) = -0.30
- OLMo-2-1B, Temp 0.5: LOGO Binary F1 = 0.783, CI [.768, .798], ρ(ent. mean) = -0.72
- OLMo-2-1B, Temp 0.7: LOGO Binary F1 = 0.695, CI [.679, .711], ρ(ent. mean) = -0.60
- OLMo-2-1B, Temp 0.9: LOGO Binary F1 = 0.453, CI [.437, .469], ρ(ent. mean) = -0.26
- Qwen3-1.7B, Temp 0.5: LOGO Binary F1 = 0.751, ρ(ent. mean) = -0.60
- Qwen3-1.7B, Temp 0.7: LOGO Binary F1 = 0.751, ρ(ent. mean) = -0.60
- Qwen3-1.7B, Temp 0.9: LOGO Binary F1 = 0.566, ρ(ent. mean) = -0.37
- Qwen3-0.6B, Temp 0.5: LOGO Binary F1 = 0.711, CI [.694, .729], ρ(ent. mean) = -0.67
- Qwen3-0.6B, Temp 0.7: LOGO Binary F1 = 0.691, CI [.673, .709], ρ(ent. mean) = -0.60
- Qwen3-0.6B, Temp 0.9: LOGO Binary F1 = 0.598, CI [.582, .615], ρ(ent. mean) = -0.29
- Temperature degradation: 9.3-26.0 pp at t=0.9; entropy mean |ρ| weakening to 0.26-0.37 at t=0.9 vs. 0.58-0.72 at t=0.5
- Pythia-2.8B improvement at t=0.5: +7.4 pp; OLMo-2-1B: +8.8 pp; Qwen models: 0-2.0 pp

**appendix_confusion_matrix.tex**

Table 1: Aggregated 3-class confusion matrix from 6-generator LOGO (Table~\ref{tab:confusion}, N=27,529)
- True gen-0: Pred gen-0 = 5,937 (99.4%); Pred gen-1 = 35 (0.6%); Pred gen-2+ = 0 (0.0%)
- True gen-1: Pred gen-0 = 368 (6.2%); Pred gen-1 = 4,437 (75.0%); Pred gen-2+ = 1,113 (18.8%)
- True gen-2+: Pred gen-0 = 464 (3.0%); Pred gen-1 = 3,646 (23.3%); Pred gen-2+ = 11,529 (73.7%)
- Gen-0 recall = 99.4%; gen-1 misclassification to gen-2+ = 18.8%, to gen-0 = 6.2% (3× more frequent misclassification to gen-2+)

**appendix_dataset_stats.tex**

Table 1: Per-generator sample counts after filtering (Table~\ref{tab:dataset-stats})
- Pythia-1B (Pythia, 1.0B): 4,555 samples
- Pythia-2.8B (Pythia, 2.8B): 4,609 samples
- OLMo-2-1B (OLMo, 1.5B): 4,713 samples
- Qwen3-0.6B (Qwen, 0.6B): 4,538 samples
- Qwen3-1.7B (Qwen, 1.7B): 4,617 samples
- Qwen3-8B (Qwen, 8.2B): 4,497 samples
- Llama-3.2-3B (Llama, 3.2B): 4,680 samples
- Mistral-7B-v0.3 (Mistral, 7.0B): 4,849 samples
- Total: 37,058 samples
- 3-class split: gen-0 = 7,963 (21.5%); gen-1 = 7,896 (21.3%); gen-2+ = 21,199 (57.2%)
- Baseline evaluation subset: 34,131 samples (for which all detector scores available)
- N for feature distributions: 37,058

**appendix_downstream.tex**

Table 1: Downstream fine-tuning perplexity (Table~\ref{tab:downstream})
- All depths (12,299): Test PPL = 2.335 ± 0.000
- Size-matched (random) (3,951): Test PPL = 2.367 ± 0.000
- Depth 0-1 only (3,951): Test PPL = 2.387 ± 0.001
- Binary-filtered (3,951): Test PPL = 2.389 ± 0.000
- Depth 0 only (797): Test PPL = 2.681 ± 0.001
- PPL differences: 2.367 vs. 2.387 (Δ = 0.020); 2.335 vs. 2.387 (minimum equivalence margin = 0.053)
- Cross-seed variance: below 0.002; cross-seed standard deviation: below 0.001

Table 2: TOST equivalence testing across multiple margins (Table~\ref{tab:tost-margins})
- Full (12,299) vs. Random (3,951), ±1% margin: Equiv? = No; TOST p = 1.0
- Full (12,299) vs. Random (3,951), ±2% margin: Equiv? = Yes; TOST p = 1 × 10^-6
- Full (12,299) vs. Random (3,951), ±3% margin: Equiv? = Yes; TOST p = < 10^-10
- Full (12,299) vs. Random (3,951), ±5% margin: Equiv? = Yes; TOST p = < 10^-10
- Full (12,299) vs. Depth 0-1 (3,951), ±1% margin: Equiv? = No; TOST p = 1.0
- Full (12,299) vs. Depth 0-1 (3,951), ±2% margin: Equiv? = No; TOST p = 1.0
- Full (12,299) vs. Depth 0-1 (3,951), ±3% margin: Equiv? = Yes; TOST p = < 10^-10
- Full (12,299) vs. Depth 0-1 (3,951), ±5% margin: Equiv? = Yes; TOST p = < 10^-10
- PPL difference full vs. random: Δ = 0.032 (1.4% of baseline)
- PPL difference full vs. depth 0-1: Δ = 0.052 (2.2% of baseline)
- Cohen's d: full vs. random = 86.0; full vs. depth 0-1 = 119.7
- Pooled standard deviation: < 0.001

**appendix_finer_depth.tex**

Table 1: 5-class LOGO evaluation (Table~\ref{tab:5class-logo})
- OLMo-2-1B: Macro F1 = 0.484; Weighted F1 = 0.506; Accuracy = 0.524
- Pythia-1B: Macro F1 = 0.543; Weighted F1 = 0.568; Accuracy = 0.575
- Pythia-2.8B: Macro F1 = 0.523; Weighted F1 = 0.540; Accuracy = 0.560
- Qwen3-0.6B: Macro F1 = 0.513; Weighted F1 = 0.521; Accuracy = 0.546
- Qwen3-1.7B: Macro F1 = 0.510; Weighted F1 = 0.536; Accuracy = 0.548
- Qwen3-8B: Macro F1 = 0.434; Weighted F1 = 0.455; Accuracy = 0.493
- Average: Macro F1 = 0.501 ± 0.038; Weighted F1 = 0.521; Accuracy = 0.541

Table 2: Per-class F1 averaged across all six LOGO folds (Table~\ref{tab:5class-perclass})
- Gen-0: Avg F1 = 0.921
- Gen-1: Avg F1 = 0.634
- Gen-2: Avg F1 = 0.268
- Gen-3: Avg F1 = 0.259
- Gen-4: Avg F1 = 0.423
- Gen-2 misclassification to gen-1: 36.5%
- Gen-3 misclassification to gen-4: 37.8%
- Permutation importance changes for 5-class: entropy_std increase = 93%; tail_decay increase = 400% (relative to 3-class)
- Classifier comparisons: HistGradientBoosting = 0.501; Random Forest = 0.476; Logistic Regression = 0.447; Frank-Hall = 0.451

**appendix_human_edit.tex**

Table 1: Robustness to random word replacement (Table~\ref{tab:human-edit})
- 0% (baseline): Binary F1 = 0.695, CI [0.680, 0.710]; 3-class F1 = 0.737
- 5%: Binary F1 = 0.650, CI [0.635, 0.666]; 3-class F1 = 0.641
- 10%: Binary F1 = 0.614, CI [0.599, 0.629]; 3-class F1 = 0.492
- 20%: Binary F1 = 0.591, CI [0.576, 0.605]; 3-class F1 = 0.367
- Binary degradation: 0%-5% = -4.6 pp; 5%-10% = -3.6 pp; 10%-20% = -2.3 pp
- 3-class degradation: 0%-20% = 0.737 to 0.367

Table 2: Feature subset degradation (Table~\ref{tab:feature-degrade})
- 0%: Ent-only Binary = 0.833; 7-feat Binary = 0.695; Ent-only 3-class = 0.688; 7-feat 3-class = 0.737
- 5%: Ent-only Binary = 0.736; 7-feat Binary = 0.650; Ent-only 3-class = 0.539; 7-feat 3-class = 0.641
- 10%: Ent-only Binary = 0.657; 7-feat Binary = 0.614; Ent-only 3-class = 0.427; 7-feat 3-class = 0.492
- 20%: Ent-only Binary = 0.566; 7-feat Binary = 0.591; Ent-only 3-class = 0.314; 7-feat 3-class = 0.367

Table 3: Baseline robustness under random word replacement (Table~\ref{tab:baseline-robustness})
- 7-feature ensemble: 0% = 0.695; 5% = 0.650; 10% = 0.614; 20% = 0.591
- LD-Score: 0% = 0.677; 5% = 0.673; 10% = 0.677; 20% = 0.671
- Avg-LogProb: 0% = 0.682; 5% = 0.419; 10% = 0.335; 20% = 0.375
- FastDetectGPT: 0% = 0.571; 5% = 0.437; 10% = 0.468; 20% = 0.514
- Binoculars: 0% = 0.500; 5% = 0.461; 10% = 0.446; 20% = 0.425
- LD-Score degradation: -0.6 pp across full 0%-20% range
- Avg-LogProb degradation: -34.7 pp at 10%
- FastDetectGPT degradation: -13.4 pp at 5%
- 7-feature ensemble degradation: -10.4 pp at 20%
- LLM-simulated sentence regeneration: Binary F1 drops from 0.692 to 0.647 (-4.5 pp, 6.5% relative); 3-class F1 drops from 0.739 to 0.667 (-7.1 pp, 9.7% relative)
- Avg sentences regenerated: 1.69; edit distance: ~50%
- Seed complexity: Max F1 variation = 1.1 pp across TTR terciles

**appendix_length.tex**

Text-based values (not tables):
- Spearman rank correlation |ρ| between word count and depth: < 0.14 (all eight generators)
- Length-feature correlations: tail_decay |ρ| = 0.38; hapax_ratio |ρ| = 0.30; TTR |ρ| = 0.29; entropy_mean |ρ| = 0.09; entropy_std |ρ| = 0.18
- Length-matched classification: Binary F1 = 0.724 (matched) vs. 0.770 (unmatched); Δ = -0.046
- Random-subsample control at equal N: F1 = 0.767 (confirms 0.046 drop is length deconfounding, not sample-size effect)
- Length accounts for ~6% of discriminative performance (Δ = 0.046 out of 0.770)
- Length-matched F1 remaining: 0.724

**appendix_lofo.tex**

Table 1: Leave-one-feature-out ablation (Table~\ref{tab:lofo}, 6-gen LOGO, full F1 = 0.789)
- entropy_max dropped: LOGO F1 = 0.774; Δ = -1.50 pp
- entropy_mean dropped: LOGO F1 = 0.783; Δ = -0.63 pp
- ttr dropped: LOGO F1 = 0.784; Δ = -0.55 pp
- hapax_ratio dropped: LOGO F1 = 0.785; Δ = -0.42 pp
- tail_decay dropped: LOGO F1 = 0.786; Δ = -0.33 pp
- entropy_std dropped: LOGO F1 = 0.786; Δ = -0.29 pp
- entropy_min dropped: LOGO F1 = 0.789; Δ = +0.01 pp
- entropy_max permutation importance: 0.063
- entropy_min permutation importance: 0.015
- Best 2-feature subset: {entropy_mean, entropy_max} F1 = 0.68 (88% of full-ensemble performance of 0.771)
- Remaining 5 features contribution: +9.1 pp

Table 2: Leave-one-feature-out on full 8-generator set (Table~\ref{tab:lofo-8gen}, 37,058 samples, 10-fold CV, full F1 = 0.771)
- Full (7 features): 3-class F1 = 0.771
- - entropy_max: 3-class F1 = 0.752; Δ = -0.019
- - entropy_mean: 3-class F1 = 0.759; Δ = -0.012
- - entropy_std: 3-class F1 = 0.763; Δ = -0.007
- - ttr: 3-class F1 = 0.764; Δ = -0.007
- - hapax_ratio: 3-class F1 = 0.765; Δ = -0.005
- - entropy_min: 3-class F1 = 0.766; Δ = -0.005
- - tail_decay: 3-class F1 = 0.767; Δ = -0.004

**appendix_ablation.tex**

Table 1: Feature ablation (Table~\ref{tab:ablation}, 8-gen, 10-fold stratified CV, 3-class)
- Full (7 features): F1 = 0.773; Top feature = hapax_ratio (imp. 0.35)
- Surface only (2): F1 = 0.688; Top feature = hapax_ratio (imp. 0.41)
- Reference only (5): F1 = 0.713; Top feature = entropy_mean (imp. 0.27)
- Full > surface: +8.5 pp
- Full > reference: +6.0 pp

**appendix_seed_control.tex**

Table 1: Independent-seed cross-generator evaluation (Table~\ref{tab:seed-control}, binary: gen-1 vs. gen-2+)
- Pythia-2.8B → OLMo-2-1B: Binary F1 = 0.695; CI [0.673, 0.717]
- OLMo-2-1B → Pythia-2.8B: Binary F1 = 0.666; CI [0.643, 0.689]
- Independent-seed average: Binary F1 = 0.680
- Shared-seed LOGO (reference): Binary F1 = 0.694; CI [0.688, 0.700]
- Gap between independent-seed and shared-seed: -1.4 pp
- Semantic similarity: 0→1 (0.622); 1→2 (0.683); 2→3 (0.801); 3→4 (0.859)
- Prompt type modulates baseline similarity: continuation = 0.717; elaboration = 0.809; rewriting = 0.808

**appendix_error_analysis.tex**

Table 1: Binary classification error analysis (Table~\ref{tab:error-analysis}, LOGO cross-validation)
- Pythia-1B (N=3560): FP = 188; FN = 460; Err.% = 18.2%
- Pythia-2.8B (N=3614): FP = 129; FN = 737; Err.% = 24.0%
- OLMo-2-1B (N=3718): FP = 154; FN = 900; Err.% = 28.3%
- Qwen3-0.6B (N=3542): FP = 234; FN = 511; Err.% = 21.0%
- Qwen3-1.7B (N=3621): FP = 175; FN = 639; Err.% = 22.5%
- Qwen3-8B (N=3502): FP = 93; FN = 1104; Err.% = 34.2%
- Llama-3.2-3B (N=3685): FP = 82; FN = 1030; Err.% = 30.2%
- Mistral-7B (N=3853): FP = 75; FN = 1659; Err.% = 45.0%
- Overall (N=29,095): FP = 1,130; FN = 7,040; Err.% = 28.1%
- Error asymmetry: FN = 86.2%; FP = 13.8%
- Total test samples: 29,095

Table 2: Error rate by generation depth (Table~\ref{tab:error-depth})
- Depth 1 (N=7896): Errors = 1130; Rate = 14.3%; Type = FP
- Depth 2 (N=7512): Errors = 3637; Rate = 48.4%; Type = FN
- Depth 3 (N=7032): Errors = 2051; Rate = 29.2%; Type = FN
- Depth 4 (N=6655): Errors = 1352; Rate = 20.3%; Type = FN

Table 3: Feature comparison between correctly and incorrectly classified samples (Table~\ref{tab:error-features})
- H̄ (entropy mean): Correct = 1.5700; Incorrect = 2.2618; Δ = +0.6918; p < 10^-300
- σ_H (entropy std): Correct = 1.6227; Incorrect = 1.7413; Δ = +0.1186; p < 10^-300
- H_min (entropy min): Correct = 0.0281; Incorrect = 0.0330; Δ = +0.0049; p = 1.0e-294
- H_max (entropy max): Correct = 7.5255; Incorrect = 7.5251; Δ = -0.0004; p = n.s.
- β_tail (tail decay): Correct = -0.0023; Incorrect = -0.0023; Δ = +0.0000; p = n.s.
- TTR: Correct = 0.3024; Incorrect = 0.4635; Δ = +0.1612; p < 10^-300
- Hapax: Correct = 0.1760; Incorrect = 0.3131; Δ = +0.1371; p < 10^-300

Table 4: Aggregated 3-class confusion matrix across 8-fold LOGO (Table~\ref{tab:confusion-3class})
- True gen-0: Pred gen-0 = 99.2%; Pred gen-1 = 0.8%; Pred gen-2+ = 0.1%
- True gen-1: Pred gen-0 = 7.3%; Pred gen-1 = 78.4%; Pred gen-2+ = 14.3%
- True gen-2+: Pred gen-0 = 3.0%; Pred gen-1 = 30.2%; Pred gen-2+ = 66.7%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbd1c0a9-94c8-4ea5-a06e-60cb5b7cd8ef",
  "isSidechain": true,
  "agentId": "a5eb1178a764b765b",
  "requestId": "req_011CbKLQgaAeWZ3a2Hzr6Lx6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b76d9289-e6cd-4474-a759-3e96aac501e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "ae94a502-820e-4db6-aa03-8dcf948a01d0",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GbKYvTR9UcAeMGhFfxiSrV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 19037,
      "cache_read_input_tokens": 17476,
      "output_tokens": 6504,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 6504,
          "cache_read_input_tokens": 17476,
          "cache_creation_input_tokens": 19037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19037,
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
