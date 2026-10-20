# Research conversation: Read lines 1-250 of /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appen

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a9f9e70a81951bdd8.jsonl`
- **Structured JSON:** [`faacd19276f495e89e32.json`](../../sessions/fa/faacd19276f495e89e32.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-25T19:42:08.770Z_

Read lines 1-250 of /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex and extract EVERY numerical value that appears. For each number, report:
- The exact value as it appears in the text
- The line number
- Whether it's in a table, figure caption, or body text
- What it represents (metric name, statistic type, etc.)

Be exhaustive - include percentages, counts, p-values, correlation coefficients, ratios, standard deviations, everything. Group them by table/section for clarity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "00884a06-3250-4c87-b491-3b7baf3c5516",
  "agentId": "a9f9e70a81951bdd8",
  "type": "user",
  "uuid": "0dad51d3-a125-496e-b0c9-26d61e86c6e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T19:42:12.403Z_

I'll read the appendix file and extract all numerical values from the first 250 lines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dad51d3-a125-496e-b0c9-26d61e86c6e7",
  "isSidechain": true,
  "agentId": "a9f9e70a81951bdd8",
  "requestId": "req_011CbPrgUbYaj1HyZ8oiHe8P",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1723b418-f76e-41a3-82ed-d78723da559e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AAxMGnPvGZj7n2F3Wvnie2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 39102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 567,
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

_source line 3 · 2026-05-25T19:42:12.672Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B3hTJFgngiKLeCNxDNSqkg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1723b418-f76e-41a3-82ed-d78723da559e",
  "isSidechain": true,
  "agentId": "a9f9e70a81951bdd8",
  "requestId": "req_011CbPrgUbYaj1HyZ8oiHe8P",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d3561d08-69a7-4569-8d39-6c0d75de9ed9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AAxMGnPvGZj7n2F3Wvnie2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 39102,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 567
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 128,
          "cache_read_input_tokens": 39102,
          "cache_creation_input_tokens": 567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 567,
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

_source line 4 · 2026-05-25T19:42:12.684Z_

<details><summary>↩ Tool result · `toolu_01B3hTJFgngiKLeCNxDNSqkg`</summary>

```text
1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to all linear projections (attention and feed-forward). SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Training hyperparameters for all optimization paradigms. All experiments use Qwen3-4B with LoRA. A dash indicates non-applicable parameters. \textsuperscript{$\star$}DPO is trained for both 1 and 3 epochs to observe temporal dynamics of the evidence-extraction trade-off (\S\ref{sec:spectrum}).}
9	\label{tab:hyperparams}
10	\small
11	\begin{tabular}{l@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c@{\hspace{8pt}}c}
12	\toprule
13	\textbf{Parameter} & \textbf{SFT} & \textbf{RSFT} & \textbf{GRPO QLoRA} & \textbf{GRPO bf16} & \textbf{DPO} \\
14	\midrule
15	\multicolumn{6}{l}{\textit{Model \& Adapter}} \\
16	\quad LoRA rank $r$ / $\alpha$ & 64 / 128 & 64 / 128 & 64 / 128 & 64 / 128 & 64 / 128 \\
17	\quad Quantization & -- & -- & NF4 4-bit & bf16 & bf16 \\
18	\midrule
19	\multicolumn{6}{l}{\textit{Optimization}} \\
20	\quad Learning rate & 2e-5 & 2e-5 & 5e-6 & 5e-6 & 5e-7 \\
21	\quad Batch size (effective) & 16 & 16 & 4 & 8 & 4 \\
22	\quad Gradient accumulation & 4 & 4 & 16 & 4 & 4 \\
23	\quad Epochs / Max steps & 3 / -- & 3 / -- & -- / 100 & -- / 100 & 1, 3\textsuperscript{$\star$} / -- \\
24	\midrule
25	\multicolumn{6}{l}{\textit{RL / Selection}} \\
26	\quad Group size $G$ & -- & -- & 4 & 8 & -- \\
27	\quad KL coeff.\ / $\beta$ & -- & -- & 0.01 & 0.01 & 0.1 \\
28	\quad Candidates $N$ / Top-$k$ & -- & 8 / 1 & -- & -- & 8 / -- \\
29	\midrule
30	\multicolumn{6}{l}{\textit{Data}} \\
31	\quad Max new tokens & 1024 & 1024 & 1024 & 1024 & 1024 \\
32	\quad Training samples & 3,053 & 2,718 & 3,053 & 3,053 & 3,053 \\
33	\quad Scoring function & -- & CED & CED & CED & CED \\
34	\bottomrule
35	\end{tabular}
36	\end{table*}
37	
38	
39	\section{Full Ablation Results}
40	\label{sec:ablation_full}
41	
42	Table~\ref{tab:ablation_full} reports the complete RSFT ablation across scoring functions, top-$k$ values, and random seeds. RSFT CED $k{=}1$ achieves a four-seed mean Ign-F1 of 44.66 (standard deviation 0.53), confirming robust improvement over the SFT s42 baseline (39.74). The three-seed mean reported in Table~\ref{tab:main} (44.82, seeds 42/43/44) is slightly higher because it excludes the lowest seed (s45: 44.16). Random selection RSFT $k{=}1$ (41.14 Ign-F1), which samples from the same candidate pool without CED scoring, improves only +1.40pp over SFT s42 versus +4.92pp for CED RSFT, confirming that CED scoring precision drives the majority of the RSFT gain. Increasing $k$ to 3 slightly degrades performance (43.64 Ign-F1), consistent with the intuition that stricter selection yields higher-quality training data. The flat-NLI scoring variant produces comparable Rel-F1 (mean 45.61 vs.\ 45.63 for CED, a difference of 0.02pp). Both CED and flat-NLI improve substantially over the SFT baseline while maintaining or improving Evi-F1, confirming that the RSFT gains are driven by quality-based data selection rather than by the specific contrastive formulation.
43	
44	\paragraph{NLI scoring comparison.} Across all available seeds, CED RSFT achieves mean Rel-F1 of 45.63 (seeds 42, 43, 44, 45: range 45.14--46.21), and flat-NLI RSFT achieves mean Rel-F1 of 45.61 (seeds 42, 43: range 45.35--45.86). The 0.02pp difference suggests comparable performance: CED's contrastive design does not substantially outperform simpler NLI scoring for RSFT data selection. We adopt CED as the default because its contrastive formulation produces per-triple discrimination scores that support interpretable error analysis.
45	
46	\paragraph{Top-$k$ selection.} Best-of-8 ($k{=}1$) yields mean Ign-F1 44.66 and Rel-F1 45.63, while top-3-of-8 ($k{=}3$) produces 43.64 and 44.54. The selected training data confirms the quality gap: $k{=}1$ data has mean extraction F1 of 61.57 and mean CED of 0.6683, versus 57.61 and 0.6205 for $k{=}3$. Despite $k{=}3$ providing 2.96$\times$ more training examples, the additional lower-ranked samples introduce noise that degrades final performance.
47	
48	\paragraph{NLI scorer capacity.} CED filtering is robust to NLI model capacity: replacing the default scorer (DeBERTa-v3-base, 86M parameters) with DeBERTa-v3-large (304M) yields only +1.10pp Ign-F1 (45.33 vs.\ 44.23, s42), a difference within the v3-base seed noise of 0.88pp (s42: 44.23, s44: 45.11). Other metrics confirm the pattern: Rel-F1 improves by +1.19pp (46.36 vs.\ 45.17), Evi-F1 by +0.20pp (81.94 vs.\ 81.74), while EDCR shifts by $-$0.39pp (0.6530 vs.\ 0.6569)---the inconsistent direction across metrics rules out systematic improvement from a larger scorer. This insensitivity supports v3-base as a cost-effective default, as a 3.5$\times$ larger scorer does not materially improve CED-based data selection.
49	
50	\begin{table}[t]
51	\centering
52	\caption{Full RSFT ablation on DocRED dev set (Qwen3-4B). CED and flat-NLI denote the scoring function used for candidate selection. Best Ign-F1 among evidence-generating methods in \textbf{bold}.}
53	\label{tab:ablation_full}
54	\small
55	\resizebox{\columnwidth}{!}{%
56	\begin{tabular}{lcccc}
57	\toprule
58	\textbf{Configuration} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
59	\midrule
60	SFT baseline (s42) & 39.74 & 40.49 & 79.86 & 0.6982 \\
61	SFT no-evidence & \textbf{47.21} & 48.76 & -- & -- \\
62	\midrule
63	RSFT random $k{=}1$ & 41.14 & 41.98 & 79.64 & 0.6971 \\
64	\midrule
65	RSFT CED $k{=}1$ (s42) & 44.23 & 45.17 & 81.74 & 0.6569 \\
66	RSFT CED $k{=}1$ (s43) & 45.12 & 46.01 & 80.63 & 0.6542 \\
67	RSFT CED $k{=}1$ (s44) & 45.11 & 46.21 & 80.50 & 0.6350 \\
68	RSFT CED $k{=}1$ (s45) & 44.16 & 45.14 & 81.74 & 0.6550 \\
69	RSFT CED $k{=}1$ (mean) & 44.66 & 45.63 & 81.15 & 0.6503 \\
70	\midrule
71	RSFT CED $k{=}3$ & 43.64 & 44.54 & 80.88 & 0.6635 \\
72	\midrule
73	RSFT flat-NLI (s42) & -- & 45.35 & 80.43 & 0.6431 \\
74	RSFT flat-NLI (s43) & -- & 45.86 & 81.58 & 0.6505 \\
75	RSFT flat-NLI (mean) & -- & 45.61 & 81.01 & 0.6468 \\
76	\midrule
77	RSFT CED $k{=}1$ v3-large (s42) & 45.33 & 46.36 & 81.94 & 0.6530 \\
78	\bottomrule
79	\end{tabular}%
80	}
81	\end{table}
82	
83	
84	\section{Scaling Details}
85	\label{sec:scaling_details}
86	
87	Table~\ref{tab:cross_detail} supplements Table~\ref{tab:scaling} in the main text with per-scale Rel-F1 and Evi-F1 breakdowns. At 1.7B, RSFT improves Rel-F1 from 45.86 to 52.81 (+6.95, multi-seed mean) while achieving Evi-F1 82.63 and EDCR 0.6217. The 4B model shows the same pattern: Rel-F1 increases from 44.39 to 45.80 (+1.41, three-seed mean). For 8B, RSFT brings Rel-F1 from 51.87 to 56.07 (three-seed mean) with Evi-F1 of 81.54 and EDCR 0.6186, confirming tight coupling between extraction and evidence at this scale. At 14B, the SFT baseline achieves strong Rel-F1 (56.11) and Evi-F1 (82.92); RSFT improves Rel-F1 to 59.17 (three-seed mean) with Evi-F1 83.37 and EDCR 0.5796.
88	
89	\begin{table}[t]
90	\centering
91	\caption{Detailed Rel-F1 and Evi-F1 across model scales on DocRED dev set. SFT and RSFT columns show multi-seed means where available (Qwen3 1.7B/4B/8B/14B: 3-seed; LLaMA SFT Rel-F1/Evi-F1: s42 only; LLaMA RSFT: 3-seed).}
92	\label{tab:cross_detail}
93	\small
94	\resizebox{\columnwidth}{!}{%
95	\begin{tabular}{lccccc}
96	\toprule
97	\textbf{Model} & \textbf{SFT Rel-F1} & \textbf{SFT Evi-F1} & \textbf{RSFT Rel-F1} & \textbf{RSFT Evi-F1} & \textbf{RSFT EDCR} \\
98	\midrule
99	Qwen3-1.7B & 45.86 & 82.85 & 52.81 & 82.63 & 0.6217 \\
100	Qwen3-4B & 44.39 & 79.61 & 45.80 & 80.96 & 0.6487 \\
101	Qwen3-8B & 51.87 & 82.94 & 56.07 & 81.54 & 0.6186 \\
102	Qwen3-14B & 56.11 & 82.92 & 59.17 & 83.37 & 0.5796 \\
103	LLaMA-3.1-8B & 55.14 & 81.51 & 57.75 & 82.84 & 0.5804 \\
104	\bottomrule
105	\end{tabular}%
106	}
107	\end{table}
108	
109	\begin{figure}[t]
110	\centering
111	\includegraphics[width=\columnwidth]{fig_scaling.pdf}
112	\caption{Evidence tax and RSFT gain across model scales. Bar heights show Ign-F1 for SFT with evidence (s42), SFT without evidence (s42), and RSFT (mean). The gap between no-evidence and SFT bars reverses direction between 1.7B and 4B, revealing the scale-dependent evidence tax. RSFT consistently narrows the gap toward the no-evidence upper bound.}
113	\label{fig:scaling}
114	\end{figure}
115	
116	
117	\section{Variance Compression Confidence Intervals}
118	\label{sec:variance_ci}
119	
120	Table~\ref{tab:variance_ci} reports 95\% confidence intervals for SFT and RSFT standard deviations using the $\chi^2$ distribution ($N{=}3$ seeds per configuration). At 1.7B, the confidence intervals are fully non-overlapping (SFT lower bound 1.45pp $>$ RSFT upper bound 0.54pp), providing the strongest evidence for variance compression. At the remaining three scales, intervals overlap but point estimates are consistently in the same direction (SFT std $>$ RSFT std at all four scales; sign test $p = 0.0625$, one-sided binomial, $n = 4$, underpowered). Cohen's $d$ ranges from 0.46 (4B) to 3.31 (1.7B), with 1.7B and LLaMA-8B showing large effect sizes ($d > 2.5$).
121	
122	\begin{table}[t]
123	\centering
124	\caption{95\% confidence intervals for training variance ($\chi^2$ method, $N{=}3$ seeds). Compression is the ratio of SFT to RSFT point estimates (unrounded).}
125	\label{tab:variance_ci}
126	\small
127	\resizebox{\columnwidth}{!}{%
128	\begin{tabular}{lcccccc}
129	\toprule
130	\textbf{Scale} & \textbf{SFT std} & \textbf{SFT 95\% CI} & \textbf{RSFT std} & \textbf{RSFT 95\% CI} & \textbf{Compr.} & \textbf{Cohen's $d$} \\
131	\midrule
132	Qwen3-1.7B & 2.79 & [1.45, 17.55] & 0.09 & [0.04, 0.54] & 32.6$\times$ & 3.31 \\
133	Qwen3-4B & 3.80 & [1.98, 23.89] & 0.51 & [0.27, 3.21] & 7.5$\times$ & 0.46 \\
134	Qwen3-8B & 3.23 & [1.68, 20.31] & 0.50 & [0.26, 3.15] & 6.5$\times$ & 1.79 \\
135	LLaMA-3.1-8B & 2.92 & [1.52, 18.37] & 0.64 & [0.33, 4.01] & 4.6$\times$ & 2.58 \\
136	\bottomrule
137	\end{tabular}%
138	}
139	\vspace{1mm}
140	{\raggedright\footnotesize Sign test: $p{=}0.0625$ (one-sided binomial, $n{=}4$). Consistent direction (4/4 SFT${>}$RSFT), non-overlapping CIs at 1.7B, and large Cohen's $d$ at 1.7B/LLaMA support variance compression despite limited $N{=}3$.\par}
141	\end{table}
142	
143	
144	\section{Controlled Evaluation Subset}
145	\label{sec:fair_subset}
146	
147	The 1.7B evidence tax comparison (\S\ref{sec:scaling}) is confounded by differential truncation rates. At \texttt{max\_new\_tokens}$=$1024, the no-evidence model truncates 50.9\% of outputs (501/985 documents) versus 31.9\% (314/985) for the evidence model. To address this, we adopt a matched@2048 fair evaluation: both configurations are evaluated at \texttt{max\_new\_tokens}$=$2048, and the tax is computed on the intersection of documents where both produce format-compliant output. This yields 971/985 fair-subset documents, with a tax of $-$5.63pp (s42), confirming a genuine 1.7B evidence benefit. As additional validation, a stricter controlled subset at @1024 (excluding truncated or repetitive outputs; 442/985 documents) yields $-$6.2pp, with the stronger benefit attributable to the more aggressive filtering.
148	
149	Table~\ref{tab:mechanistic} provides a mechanistic breakdown across three scales (evaluated at @1024). Output duplication rate (fraction of documents containing $\geq$3 repeated triples or unique/total $< 0.5$) declines monotonically with scale for both training configurations, but the gap between no-evidence and with-evidence models narrows from 27.5pp at 1.7B to 3.7pp at 8B. This pattern supports the implicit regularization hypothesis: evidence generation forces smaller models to attend to supporting context, reducing degenerate repetition. At 4B, duplication is already moderate (31.1\% with evidence), so the regularization benefit diminishes; under matched@2048 evaluation, the 4B training-time tax is approximately neutral (+0.25$\pm$0.47pp, three-seed mean). The truncation asymmetry reverses across scales: at 1.7B the no-evidence model truncates 19pp more often; at 8B the evidence model truncates 9pp more often due to the longer output format.
150	
151	\begin{table}[t]
152	\centering
153	\caption{Mechanistic breakdown of output quality across scales. Duplication rate: fraction of documents with degenerate outputs. Truncation $\Delta$: no-evidence rate minus with-evidence rate (positive means no-evidence truncates more).}
154	\label{tab:mechanistic}
155	\small
156	\begin{tabular}{lccccc}
157	\toprule
158	& \multicolumn{3}{c}{\textbf{Duplication Rate}} & \multicolumn{2}{c}{\textbf{Truncation}} \\
159	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
160	\textbf{Scale} & \textbf{w/ evi} & \textbf{no-evi} & \textbf{Gap} & \textbf{$\Delta$} & \textbf{Pattern} \\
161	\midrule
162	1.7B & 33.0 & 60.5 & 27.5 & +19 & no-evi worse \\
163	4B & 31.1 & 43.2 & 12.1 & +2 & neutral \\
164	8B & 29.2 & 32.9 & 3.7 & $-$9 & evi worse \\
165	\bottomrule
166	\end{tabular}
167	\end{table}
168	
169	
170	\section{Training-Time Evidence Tax}
171	\label{sec:training_tax}
172	
173	The evidence tax can be measured in two ways. The \emph{training-time} tax compares separately trained models (SFT with evidence vs.\ SFT without evidence in the training output format). The \emph{inference-time} tax (reported in Table~\ref{tab:scaling}) evaluates the same RSFT model with and without evidence at inference time.
174	
175	Na\"ive comparisons at \texttt{max\_new\_tokens}$=$1024 are confounded by differential truncation rates (e.g., 50.9\% vs.\ 31.9\% at 1.7B). To control for this, we adopt a \emph{matched@2048 fair evaluation}: both configurations are evaluated at \texttt{max\_new\_tokens}$=$2048, and the tax is computed on the intersection of documents where both models produce format-compliant output. Table~\ref{tab:training_tax} reports the matched@2048 training-time tax across Qwen3 scales.
176	
177	The tax reveals a within-family capacity threshold: evidence generation benefits 1.7B ($-$5.63pp on 971/985 fair-subset documents) but is approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B across three seeds, +0.04pp at 8B, +0.03pp at 14B). At 1.7B, s42 is the strongest SFT seed (47.86 Ign-F1, +3.22pp above the three-seed mean of 44.64), so the benefit may be amplified relative to the population mean. LLaMA-3.1-8B SFT training-time tax is consistently negative but with high magnitude variance ($-$1.53 to $-$11.20pp, mean $-$5.19$\pm$5.25pp under matched@2048) and omitted from the table due to the s43 outlier (16.3\% no-evidence format failure inflates its tax); cross-architecture patterns are addressed in \S\ref{sec:generalization_full}.
178	
179	\begin{table}[t]
180	\centering
181	\caption{Training-time evidence tax under matched@2048 fair evaluation (DocRED dev Ign-F1). Tax $=$ no-evi $-$ with-evi; positive $=$ cost.}
182	\label{tab:training_tax}
183	\small
184	\resizebox{\columnwidth}{!}{%
185	\begin{tabular}{lcccc}
186	\toprule
187	\textbf{Model} & \textbf{Fair w/ evi} & \textbf{Fair no-evi} & \textbf{Evi Tax} & \textbf{Subset} \\
188	\midrule
189	Qwen3-1.7B & 48.38 & 42.75 & $-$5.63 & 971 \\
190	Qwen3-4B & -- & -- & +0.25{\scriptsize$\pm$0.47} & $\geq$982 \\
191	Qwen3-8B & 50.15 & 50.19 & +0.04 & 984 \\
192	Qwen3-14B & 55.07 & 55.10 & +0.03 & 985$^\dagger$ \\
193	\bottomrule
194	\end{tabular}%
195	}
196	\vspace{1mm}
197	{\raggedright\footnotesize Both evaluated at @2048 on format-compliant intersection. 1.7B/8B: s42; 4B: three-seed mean$\pm$std; $^\dagger$14B at @1024, 0\% truncation.\par}
198	\end{table}
199	
200	\paragraph{Evidence training and SFT seed variance.}
201	Evidence training's effect on SFT seed variance is also scale-dependent. At 4B, with-evidence SFT models show near-identical cross-seed spread (0.02pp) compared to no-evidence models (0.50pp), yielding 25$\times$ variance compression. At 8B, the compression is more modest (0.35pp vs.\ 0.48pp, 1.4$\times$). However, at 1.7B the pattern reverses: with-evidence seed spread (0.63pp) exceeds no-evidence spread (0.20pp). This reversal likely reflects the extreme truncation rates at 1.7B (75.6\% with-evidence, 94.4\% no-evidence at \texttt{max\_new\_tokens}$=$1024): truncated outputs produce noisy extraction results whose variance depends on which triples appear before the cutoff point. The RSFT variance compression reported in \S\ref{sec:scaling} is measured relative to SFT with-evidence baselines and holds at all scales regardless of this SFT-internal pattern.
202	
203	
204	\section{Why RSFT Avoids Decoupling}
205	\label{sec:rsft_theory}
206	
207	The structural difference between selection and optimization explains why RSFT does not exhibit the decoupling observed in gradient-based methods. GRPO and DPO update model parameters through gradients that optimize a reward signal. When two sub-tasks (extraction and evidence) compete for gradient capacity, the optimizer can discover and exploit the trade-off between them, improving one at the expense of the other. RSFT operates differently: it selects complete outputs and trains on them with standard supervised loss. Because the selection is discrete (accept or reject a full response), there is no gradient pathway through which the model can learn to sacrifice extraction for evidence quality. Only outputs where both extraction and evidence are jointly strong survive the CED filter. This property is not specific to RSFT's design but is a structural consequence of discrete selection over complete outputs: any selection-based method that filters on a joint quality criterion will inherit the same coupling guarantee. The implication for practitioners is direct: when optimizing for multiple coupled generation objectives, selection-based methods preserve inter-objective balance that gradient-based methods disrupt.
208	
209	
210	\section{Full Generalization Results}
211	\label{sec:generalization_full}
212	
213	\paragraph{Cross-family transfer.}
214	LLaMA-3.1-8B confirms the scaling patterns observed with Qwen3. Its SFT baseline achieves a three-seed mean of 51.09 Ign-F1 (std 2.92pp; s42: 53.84, s43: 51.42, s44: 48.02). Under matched@2048 fair evaluation, the training-time tax is consistently negative across all three seeds (s42: $-$1.53, s43: $-$11.20, s44: $-$2.83; mean $-$5.19$\pm$5.25pp), indicating that evidence generation consistently benefits LLaMA-3.1-8B. This contrasts with Qwen3-8B's approximately neutral tax (+0.04pp), suggesting that the evidence tax may be architecture-dependent at the 8B scale; however, the high magnitude variance (driven by s43, whose no-evidence configuration has a 16.3\% format failure rate that inflates the tax estimate) precludes precise quantification. RSFT CED improves LLaMA to a three-seed mean of 56.54 Ign-F1 (std 0.64pp; s42: 57.14, s43: 56.62, s44: 55.87), a +5.45 point gain over SFT mean (51.09), with 4.6$\times$ variance compression (2.92pp $\to$ 0.64pp), consistent with the pattern at the 8B scale (Qwen3-8B: +4.14, 6.5$\times$ compression).
215	
216	\paragraph{Cross-dataset robustness.}
217	On Re-DocRED~\citep{tan2022redocred}, the SFT baseline achieves 36.59 Ign-F1 (Evi-F1 81.70, EDCR 0.6674). RSFT CED improves this to 41.45 Ign-F1 (Evi-F1 81.82, EDCR 0.6210), a +4.86pp gain that closely matches the +5.08pp improvement on DocRED (RSFT three-seed mean minus SFT s42). This consistency across datasets with different annotation protocols confirms that RSFT's benefit generalizes beyond training-set-specific artifacts. Evidence quality remains stable across datasets (Evi-F1 81.82 vs.\ 81.15 on DocRED), and the EDCR reduction ($-0.046$) mirrors the DocRED pattern, further supporting the robustness of CED-based selection.
218	
219	\paragraph{Re-DocRED test set evaluation.}
220	Table~\ref{tab:test_results} reports SFT and RSFT performance on the Re-DocRED test set. We observe a consistent performance gap between dev and test sets, with test Ign-F1 approximately 20 percentage points lower (RSFT: 1.7B 51.2$\to$29.3, 4B 44.8$\to$25.0, 8B 54.3$\to$33.5, 14B 57.9$\to$38.5, LLaMA-8B 56.5$\to$35.5; SFT 1.7B: 44.6$\to$25.8). This gap is attributable to annotation density: the test set contains 34.7 gold triples per document versus 12.3 in the dev set (a 2.82$\times$ ratio), imposing a harder recall requirement. The gap magnitude is stable across scales and architectures (range: 18.9--21.9pp), and model ranking is perfectly preserved (Spearman $\rho{=}1.0$), indicating that the absolute drop reflects the test annotation scheme rather than a model-specific deficiency. At 14B, the RSFT advantage observed on dev (+2.78pp) reverses on test ($\Delta{=}{-}0.37$pp); we note that the SFT model's 50.6\% truncation rate implies longer outputs that generate more candidate triples to match the test set's dense annotation scheme.
221	
222	\begin{table}[t]
223	\centering
224	\caption{SFT and RSFT performance on Re-DocRED test set (Ign-F1 \%). Dev Ign-F1 (RSFT) from Table~\ref{tab:scaling}. All test results use s42.}
225	\label{tab:test_results}
226	\small
227	\resizebox{\columnwidth}{!}{%
228	\begin{tabular}{lccccccc}
229	\toprule
230	\textbf{Model} & \textbf{Dev} & \textbf{SFT} & \textbf{RSFT} & \textbf{$\Delta$} & \textbf{Tr. SFT} & \textbf{Tr. RSFT} & \textbf{Evi-F1} \\
231	\midrule
232	Qwen3-1.7B & 51.19 & 25.79 & 29.33 & +3.54 & 81.8 & 73.8 & 23.20 \\
233	Qwen3-4B & 44.82$^\dagger$ & 22.32 & 25.01 & +2.69 & 64.6 & 42.8 & 18.38 \\
234	Qwen3-8B & 54.33 & 31.06 & 33.53 & +2.47 & 82.0 & 1.8 & 25.26 \\
235	Qwen3-14B & 57.85 & 38.86 & 38.49 & $-$0.37 & 50.6 & 13.4 & 26.88 \\
236	LLaMA-3.1-8B & 56.54 & 34.20 & 35.54 & +1.34 & 65.4 & 60.0 & 24.57 \\
237	\bottomrule
238	\end{tabular}%
239	}
240	\vspace{1mm}
241	{\raggedright\footnotesize $^\dagger$4B dev is three-seed mean; test uses retrained checkpoint (comparable dev: 43.88 vs.\ 44.23). $\Delta$: RSFT$-$SFT. Evi-F1: RSFT joint (DREEAM). Tr.: truncation (\%). Dev: multi-seed mean from Table~\ref{tab:scaling}.\par}
242	\end{table}
243	
244	\paragraph{Test-set evidence tax.}
245	Table~\ref{tab:test_tax} reports the evidence tax on the Re-DocRED test set, comparing SFT models trained with and without evidence in the output format. Test-set evaluation confirms the directional pattern observed on development data across all five model configurations: the tax is negative (beneficial) at 1.7B ($-$4.86pp) and LLaMA-8B ($-$4.94pp), and near-neutral at mid-scales ($-$0.13pp at 4B, $-$0.32pp at 14B). The 8B test tax ($-$1.71pp) shows slight variation from its near-neutral dev counterpart (+0.04pp), though both remain modest relative to the 1.7B and LLaMA benefits.
246	
247	\begin{table}[t]
248	\centering
249	\caption{Evidence tax on Re-DocRED test set (Ign-F1 \%). Tax $=$ no-evi $-$ with-evi; negative $=$ benefit. All results use s42. Dev tax from Table~\ref{tab:training_tax}.}
250	\label{tab:test_tax}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3561d08-69a7-4569-8d39-6c0d75de9ed9",
  "isSidechain": true,
  "promptId": "00884a06-3250-4c87-b491-3b7baf3c5516",
  "agentId": "a9f9e70a81951bdd8",
  "type": "user",
  "uuid": "1cd7aa25-c4b8-4549-81d8-e2318fd45e72",
  "sourceToolAssistantUUID": "d3561d08-69a7-4569-8d39-6c0d75de9ed9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-25T19:43:18.510Z_

Now I'll extract all numerical values from the file systematically. Let me organize them by section:

## EXTRACTED NUMERICAL VALUES (Lines 1-250)

### SECTION 1: Training Hyperparameters (Lines 1-36)

**Table 1 (tab:hyperparams) - Model & Adapter Section:**
- Line 16: `64` (LoRA rank r across all methods)
- Line 16: `128` (LoRA alpha across all methods)

**Table 1 - Optimization Section:**
- Line 20: `2e-5` (SFT learning rate)
- Line 20: `2e-5` (RSFT learning rate)
- Line 20: `5e-6` (GRPO QLoRA learning rate)
- Line 20: `5e-6` (GRPO bf16 learning rate)
- Line 20: `5e-7` (DPO learning rate)
- Line 21: `16` (SFT batch size, effective)
- Line 21: `16` (RSFT batch size, effective)
- Line 21: `4` (GRPO QLoRA batch size)
- Line 21: `8` (GRPO bf16 batch size)
- Line 21: `4` (DPO batch size)
- Line 22: `4` (SFT gradient accumulation)
- Line 22: `4` (RSFT gradient accumulation)
- Line 22: `16` (GRPO QLoRA gradient accumulation)
- Line 22: `4` (GRPO bf16 gradient accumulation)
- Line 22: `4` (DPO gradient accumulation)
- Line 23: `3` (SFT epochs)
- Line 23: `3` (RSFT epochs)
- Line 23: `100` (GRPO QLoRA max steps)
- Line 23: `100` (GRPO bf16 max steps)
- Line 23: `1` (DPO epochs, first setting)
- Line 23: `3` (DPO epochs, second setting with asterisk)

**Table 1 - RL/Selection Section:**
- Line 26: `4` (GRPO QLoRA group size)
- Line 26: `8` (GRPO bf16 group size)
- Line 27: `0.01` (GRPO QLoRA KL coefficient)
- Line 27: `0.01` (GRPO bf16 KL coefficient)
- Line 27: `0.1` (DPO beta)
- Line 28: `8` (RSFT candidates N)
- Line 28: `1` (RSFT top-k)
- Line 28: `8` (GRPO candidates)

**Table 1 - Data Section:**
- Line 31: `1024` (Max new tokens - all methods)
- Line 32: `3,053` (SFT training samples)
- Line 32: `2,718` (RSFT training samples)
- Line 32: `3,053` (GRPO QLoRA training samples)
- Line 32: `3,053` (GRPO bf16 training samples)
- Line 32: `3,053` (DPO training samples)

**Body text (lines 4, 6, 8):**
- Line 4: `64` (LoRA rank)
- Line 4: `128` (LoRA alpha)
- Line 4: `8` (N candidates for RSFT)
- Line 8: `1` (DPO epochs for first training)
- Line 8: `3` (DPO epochs for second training)

### SECTION 2: Full Ablation Results (Lines 39-81)

**Body text (lines 42, 44, 46):**
- Line 42: `44.66` (RSFT CED k=1 four-seed mean Ign-F1)
- Line 42: `0.53` (Standard deviation of 44.66)
- Line 42: `39.74` (SFT s42 baseline Ign-F1)
- Line 42: `44.82` (RSFT three-seed mean from Table 1)
- Line 42: `42` (Seed 42)
- Line 42: `43` (Seed 43)
- Line 42: `44` (Seed 44)
- Line 42: `44.16` (RSFT s45 Ign-F1)
- Line 42: `41.14` (Random selection RSFT k=1 Ign-F1)
- Line 42: `1.40` (pp improvement for random selection)
- Line 42: `4.92` (pp improvement for CED RSFT)
- Line 42: `43.64` (RSFT CED k=3 Ign-F1)
- Line 42: `45.61` (flat-NLI Rel-F1 mean)
- Line 42: `45.63` (CED Rel-F1 mean)
- Line 42: `0.02` (pp difference between CED and flat-NLI)

**Body text continued (line 44):**
- Line 44: `45.63` (CED RSFT mean Rel-F1)
- Line 44: `42` (Seed 42)
- Line 44: `43` (Seed 43)
- Line 44: `44` (Seed 44)
- Line 44: `45` (Seed 45)
- Line 44: `45.14` (Range lower bound)
- Line 44: `46.21` (Range upper bound)
- Line 44: `45.61` (flat-NLI RSFT mean Rel-F1)
- Line 44: `42` (Seed 42)
- Line 44: `43` (Seed 43)
- Line 44: `45.35` (Range lower bound)
- Line 44: `45.86` (Range upper bound)
- Line 44: `0.02` (pp difference)

**Body text continued (line 46):**
- Line 46: `8` (Denominator for best-of-8)
- Line 46: `1` (k value)
- Line 46: `44.66` (k=1 mean Ign-F1)
- Line 46: `45.63` (k=1 Rel-F1)
- Line 46: `3` (k value for top-3)
- Line 46: `8` (Denominator for top-3)
- Line 46: `43.64` (k=3 Ign-F1)
- Line 46: `44.54` (k=3 Rel-F1)
- Line 46: `61.57` (Mean extraction F1 for k=1 data)
- Line 46: `0.6683` (Mean CED for k=1 data)
- Line 46: `57.61` (Mean extraction F1 for k=3 data)
- Line 46: `0.6205` (Mean CED for k=3 data)
- Line 46: `2.96` (Multiplication factor for more examples)

**Body text (line 48):**
- Line 48: `304` (DeBERTa-v3-large parameters - millions)
- Line 48: `86` (DeBERTa-v3-base parameters - millions)
- Line 48: `1.10` (pp improvement Ign-F1)
- Line 48: `45.33` (v3-large Ign-F1, s42)
- Line 48: `44.23` (v3-base Ign-F1)
- Line 48: `0.88` (pp v3-base seed noise)
- Line 48: `42` (Seed 42)
- Line 48: `44.23` (v3-base s42)
- Line 48: `45.11` (v3-base s44)
- Line 48: `1.19` (pp improvement Rel-F1)
- Line 48: `46.36` (v3-large Rel-F1)
- Line 48: `45.17` (v3-base Rel-F1)
- Line 48: `0.20` (pp improvement Evi-F1)
- Line 48: `81.94` (v3-large Evi-F1)
- Line 48: `81.74` (v3-base Evi-F1)
- Line 48: `0.39` (pp shift EDCR)
- Line 48: `0.6530` (v3-large EDCR)
- Line 48: `0.6569` (v3-base EDCR)
- Line 48: `3.5` (Multiplication factor - larger scorer)

**Table 2 (tab:ablation_full) - Body text and table:**
- Line 52: (Caption references evidence-generating methods)
- Line 60: `39.74` (SFT baseline s42 Ign-F1, table)
- Line 60: `40.49` (SFT baseline s42 Rel-F1, table)
- Line 60: `79.86` (SFT baseline s42 Evi-F1, table)
- Line 60: `0.6982` (SFT baseline s42 EDCR, table)
- Line 61: `47.21` (SFT no-evidence Ign-F1, table)
- Line 61: `48.76` (SFT no-evidence Rel-F1, table)
- Line 63: `41.14` (RSFT random k=1 Ign-F1, table)
- Line 63: `41.98` (RSFT random k=1 Rel-F1, table)
- Line 63: `79.64` (RSFT random k=1 Evi-F1, table)
- Line 63: `0.6971` (RSFT random k=1 EDCR, table)
- Line 65: `44.23` (RSFT CED k=1 s42 Ign-F1, table)
- Line 65: `45.17` (RSFT CED k=1 s42 Rel-F1, table)
- Line 65: `81.74` (RSFT CED k=1 s42 Evi-F1, table)
- Line 65: `0.6569` (RSFT CED k=1 s42 EDCR, table)
- Line 66: `45.12` (RSFT CED k=1 s43 Ign-F1, table)
- Line 66: `46.01` (RSFT CED k=1 s43 Rel-F1, table)
- Line 66: `80.63` (RSFT CED k=1 s43 Evi-F1, table)
- Line 66: `0.6542` (RSFT CED k=1 s43 EDCR, table)
- Line 67: `45.11` (RSFT CED k=1 s44 Ign-F1, table)
- Line 67: `46.21` (RSFT CED k=1 s44 Rel-F1, table)
- Line 67: `80.50` (RSFT CED k=1 s44 Evi-F1, table)
- Line 67: `0.6350` (RSFT CED k=1 s44 EDCR, table)
- Line 68: `44.16` (RSFT CED k=1 s45 Ign-F1, table)
- Line 68: `45.14` (RSFT CED k=1 s45 Rel-F1, table)
- Line 68: `81.74` (RSFT CED k=1 s45 Evi-F1, table)
- Line 68: `0.6550` (RSFT CED k=1 s45 EDCR, table)
- Line 69: `44.66` (RSFT CED k=1 mean Ign-F1, table)
- Line 69: `45.63` (RSFT CED k=1 mean Rel-F1, table)
- Line 69: `81.15` (RSFT CED k=1 mean Evi-F1, table)
- Line 69: `0.6503` (RSFT CED k=1 mean EDCR, table)
- Line 71: `43.64` (RSFT CED k=3 Ign-F1, table)
- Line 71: `44.54` (RSFT CED k=3 Rel-F1, table)
- Line 71: `80.88` (RSFT CED k=3 Evi-F1, table)
- Line 71: `0.6635` (RSFT CED k=3 EDCR, table)
- Line 73: `45.35` (RSFT flat-NLI s42 Rel-F1, table)
- Line 73: `80.43` (RSFT flat-NLI s42 Evi-F1, table)
- Line 73: `0.6431` (RSFT flat-NLI s42 EDCR, table)
- Line 74: `45.86` (RSFT flat-NLI s43 Rel-F1, table)
- Line 74: `81.58` (RSFT flat-NLI s43 Evi-F1, table)
- Line 74: `0.6505` (RSFT flat-NLI s43 EDCR, table)
- Line 75: `45.61` (RSFT flat-NLI mean Rel-F1, table)
- Line 75: `81.01` (RSFT flat-NLI mean Evi-F1, table)
- Line 75: `0.6468` (RSFT flat-NLI mean EDCR, table)
- Line 77: `45.33` (RSFT CED k=1 v3-large s42 Ign-F1, table)
- Line 77: `46.36` (RSFT CED k=1 v3-large s42 Rel-F1, table)
- Line 77: `81.94` (RSFT CED k=1 v3-large s42 Evi-F1, table)
- Line 77: `0.6530` (RSFT CED k=1 v3-large s42 EDCR, table)

### SECTION 3: Scaling Details (Lines 84-107)

**Body text (line 87):**
- Line 87: `1.7` (Model scale - 1.7B)
- Line 87: `52.81` (RSFT Rel-F1 at 1.7B)
- Line 87: `45.86` (SFT Rel-F1 at 1.7B)
- Line 87: `6.95` (Improvement in Rel-F1)
- Line 87: `82.63` (RSFT Evi-F1 at 1.7B)
- Line 87: `0.6217` (RSFT EDCR at 1.7B)
- Line 87: `4` (Model scale - 4B)
- Line 87: `44.39` (SFT Rel-F1 at 4B)
- Line 87: `45.80` (RSFT Rel-F1 at 4B)
- Line 87: `1.41` (Improvement in Rel-F1 at 4B, three-seed mean)
- Line 87: `8` (Model scale - 8B)
- Line 87: `51.87` (SFT Rel-F1 at 8B)
- Line 87: `56.07` (RSFT Rel-F1 at 8B, three-seed mean)
- Line 87: `81.54` (RSFT Evi-F1 at 8B)
- Line 87: `0.6186` (RSFT EDCR at 8B)
- Line 87: `14` (Model scale - 14B)
- Line 87: `56.11` (SFT Rel-F1 at 14B)
- Line 87: `59.17` (RSFT Rel-F1 at 14B, three-seed mean)
- Line 87: `82.92` (SFT Evi-F1 at 14B)
- Line 87: `83.37` (RSFT Evi-F1 at 14B)
- Line 87: `0.5796` (RSFT EDCR at 14B)

**Table 3 (tab:cross_detail):**
- Line 99: `45.86` (Qwen3-1.7B SFT Rel-F1, table)
- Line 99: `82.85` (Qwen3-1.7B SFT Evi-F1, table)
- Line 99: `52.81` (Qwen3-1.7B RSFT Rel-F1, table)
- Line 99: `82.63` (Qwen3-1.7B RSFT Evi-F1, table)
- Line 99: `0.6217` (Qwen3-1.7B RSFT EDCR, table)
- Line 100: `44.39` (Qwen3-4B SFT Rel-F1, table)
- Line 100: `79.61` (Qwen3-4B SFT Evi-F1, table)
- Line 100: `45.80` (Qwen3-4B RSFT Rel-F1, table)
- Line 100: `80.96` (Qwen3-4B RSFT Evi-F1, table)
- Line 100: `0.6487` (Qwen3-4B RSFT EDCR, table)
- Line 101: `51.87` (Qwen3-8B SFT Rel-F1, table)
- Line 101: `82.94` (Qwen3-8B SFT Evi-F1, table)
- Line 101: `56.07` (Qwen3-8B RSFT Rel-F1, table)
- Line 101: `81.54` (Qwen3-8B RSFT Evi-F1, table)
- Line 101: `0.6186` (Qwen3-8B RSFT EDCR, table)
- Line 102: `56.11` (Qwen3-14B SFT Rel-F1, table)
- Line 102: `82.92` (Qwen3-14B SFT Evi-F1, table)
- Line 102: `59.17` (Qwen3-14B RSFT Rel-F1, table)
- Line 102: `83.37` (Qwen3-14B RSFT Evi-F1, table)
- Line 102: `0.5796` (Qwen3-14B RSFT EDCR, table)
- Line 103: `55.14` (LLaMA-3.1-8B SFT Rel-F1, table)
- Line 103: `81.51` (LLaMA-3.1-8B SFT Evi-F1, table)
- Line 103: `57.75` (LLaMA-3.1-8B RSFT Rel-F1, table)
- Line 103: `82.84` (LLaMA-3.1-8B RSFT Evi-F1, table)
- Line 103: `0.5804` (LLaMA-3.1-8B RSFT EDCR, table)

**Figure 1 (fig:scaling) caption (line 112):**
- Line 112: `1.7` (Model scale comparison - 1.7B)
- Line 112: `4` (Model scale - 4B)

### SECTION 4: Variance Compression Confidence Intervals (Lines 117-141)

**Body text (line 120):**
- Line 120: `95` (Confidence interval percentage)
- Line 120: `3` (Number of seeds per configuration)
- Line 120: `1.7` (Model scale - 1.7B)
- Line 120: `1.45` (SFT lower CI bound)
- Line 120: `0.54` (RSFT upper CI bound)
- Line 120: `0.0625` (Sign test p-value)
- Line 120: `4` (Number of scales tested)
- Line 120: `2.5` (Cohen's d threshold)

**Table 4 (tab:variance_ci):**
- Line 132: `2.79` (Qwen3-1.7B SFT std, table)
- Line 132: `1.45` (Qwen3-1.7B SFT 95% CI lower, table)
- Line 132: `17.55` (Qwen3-1.7B SFT 95% CI upper, table)
- Line 132: `0.09` (Qwen3-1.7B RSFT std, table)
- Line 132: `0.04` (Qwen3-1.7B RSFT 95% CI lower, table)
- Line 132: `0.54` (Qwen3-1.7B RSFT 95% CI upper, table)
- Line 132: `32.6` (Qwen3-1.7B compression factor, table)
- Line 132: `3.31` (Qwen3-1.7B Cohen's d, table)
- Line 133: `3.80` (Qwen3-4B SFT std, table)
- Line 133: `1.98` (Qwen3-4B SFT 95% CI lower, table)
- Line 133: `23.89` (Qwen3-4B SFT 95% CI upper, table)
- Line 133: `0.51` (Qwen3-4B RSFT std, table)
- Line 133: `0.27` (Qwen3-4B RSFT 95% CI lower, table)
- Line 133: `3.21` (Qwen3-4B RSFT 95% CI upper, table)
- Line 133: `7.5` (Qwen3-4B compression factor, table)
- Line 133: `0.46` (Qwen3-4B Cohen's d, table)
- Line 134: `3.23` (Qwen3-8B SFT std, table)
- Line 134: `1.68` (Qwen3-8B SFT 95% CI lower, table)
- Line 134: `20.31` (Qwen3-8B SFT 95% CI upper, table)
- Line 134: `0.50` (Qwen3-8B RSFT std, table)
- Line 134: `0.26` (Qwen3-8B RSFT 95% CI lower, table)
- Line 134: `3.15` (Qwen3-8B RSFT 95% CI upper, table)
- Line 134: `6.5` (Qwen3-8B compression factor, table)
- Line 134: `1.79` (Qwen3-8B Cohen's d, table)
- Line 135: `2.92` (LLaMA-3.1-8B SFT std, table)
- Line 135: `1.52` (LLaMA-3.1-8B SFT 95% CI lower, table)
- Line 135: `18.37` (LLaMA-3.1-8B SFT 95% CI upper, table)
- Line 135: `0.64` (LLaMA-3.1-8B RSFT std, table)
- Line 135: `0.33` (LLaMA-3.1-8B RSFT 95% CI lower, table)
- Line 135: `4.01` (LLaMA-3.1-8B RSFT 95% CI upper, table)
- Line 135: `4.6` (LLaMA-3.1-8B compression factor, table)
- Line 135: `2.58` (LLaMA-3.1-8B Cohen's d, table)
- Line 140: `0.0625` (Sign test p-value, footnote)
- Line 140: `4` (n value for binomial test, footnote)

### SECTION 5: Controlled Evaluation Subset (Lines 144-167)

**Body text (lines 147-149):**
- Line 147: `1024` (max_new_tokens value)
- Line 147: `50.9` (Truncation percentage at 1.7B, no-evidence)
- Line 147: `501` (Numerator for truncation)
- Line 147: `985` (Denominator for truncation - total documents)
- Line 147: `31.9` (Truncation percentage at 1.7B, evidence)
- Line 147: `314` (Numerator for truncation, evidence)
- Line 147: `2048` (max_new_tokens for fair evaluation)
- Line 147: `971` (Fair-subset documents)
- Line 147: `5.63` (Evidence tax at 1.7B)
- Line 147: `1024` (max_new_tokens for stricter subset)
- Line 147: `6.2` (Evidence benefit with stricter filtering)
- Line 147: `442` (Filtered documents count)

**Body text (line 149):**
- Line 149: `27.5` (Duplication gap at 1.7B)
- Line 149: `3.7` (Duplication gap at 8B)
- Line 149: `31.1` (Duplication rate at 4B with evidence)
- Line 149: `0.25` (4B training-time tax mean)
- Line 149: `0.47` (4B training-time tax std)
- Line 149: `0.63` (With-evidence seed spread at 1.7B)
- Line 149: `0.20` (No-evidence seed spread at 1.7B)
- Line 149: `75.6` (Truncation percentage at 1.7B with-evidence)
- Line 149: `94.4` (Truncation percentage at 1.7B no-evidence)
- Line 149: `1024` (max_new_tokens reference)

**Table 5 (tab:mechanistic):**
- Line 162: `33.0` (1.7B duplication rate with evidence, table)
- Line 162: `60.5` (1.7B duplication rate no-evidence, table)
- Line 162: `27.5` (1.7B duplication gap, table)
- Line 162: `19` (1.7B truncation delta, table)
- Line 163: `31.1` (4B duplication rate with evidence, table)
- Line 163: `43.2` (4B duplication rate no-evidence, table)
- Line 163: `12.1` (4B duplication gap, table)
- Line 163: `2` (4B truncation delta, table)
- Line 164: `29.2` (8B duplication rate with evidence, table)
- Line 164: `32.9` (8B duplication rate no-evidence, table)
- Line 164: `3.7` (8B duplication gap, table)
- Line 164: `9` (8B truncation delta, table)

### SECTION 6: Training-Time Evidence Tax (Lines 170-202)

**Body text (line 177):**
- Line 177: `1024` (max_new_tokens)
- Line 177: `50.9` (Truncation at 1.7B %)
- Line 177: `31.9` (Truncation at 1.7B with-evidence %)
- Line 177: `2048` (max_new_tokens for fair evaluation)
- Line 177: `1.7` (Model scale - 1.7B)
- Line 177: `5.63` (Evidence tax at 1.7B)
- Line 177: `971` (Fair-subset documents at 1.7B)
- Line 177: `985` (Total documents)
- Line 177: `4` (Model scale - 4B)
- Line 177: `0.25` (4B tax mean)
- Line 177: `0.47` (4B tax std)
- Line 177: `8` (Model scale - 8B)
- Line 177: `0.04` (8B tax)
- Line 177: `14` (Model scale - 14B)
- Line 177: `0.03` (14B tax)
- Line 177: `1.53` (LLaMA tax minimum)
- Line 177: `11.20` (LLaMA tax maximum)
- Line 177: `5.19` (LLaMA tax mean)
- Line 177: `5.25` (LLaMA tax std)

**Body text (line 201):**
- Line 201: `4` (Model scale - 4B)
- Line 201: `0.02` (With-evidence seed spread at 4B)
- Line 201: `0.50` (No-evidence seed spread at 4B)
- Line 201: `25` (Variance compression factor at 4B)
- Line 201: `8` (Model scale - 8B)
- Line 201: `0.35` (With-evidence seed spread at 8B)
- Line 201: `0.48` (No-evidence seed spread at 8B)
- Line 201: `1.4` (Compression factor at 8B)
- Line 201: `1.7` (Model scale - 1.7B)
- Line 201: `0.63` (With-evidence seed spread at 1.7B)
- Line 201: `0.20` (No-evidence seed spread at 1.7B)
- Line 201: `75.6` (Truncation with-evidence %)
- Line 201: `94.4` (Truncation no-evidence %)
- Line 201: `1024` (max_new_tokens reference)

**Table 6 (tab:training_tax):**
- Line 189: `48.38` (Qwen3-1.7B fair with evidence, table)
- Line 189: `42.75` (Qwen3-1.7B fair no-evidence, table)
- Line 189: `5.63` (Qwen3-1.7B tax, table)
- Line 189: `971` (Qwen3-1.7B subset count, table)
- Line 190: `0.25` (Qwen3-4B tax mean, table)
- Line 190: `0.47` (Qwen3-4B tax std, table)
- Line 190: `982` (Qwen3-4B subset count, table)
- Line 191: `50.15` (Qwen3-8B fair with evidence, table)
- Line 191: `50.19` (Qwen3-8B fair no-evidence, table)
- Line 191: `0.04` (Qwen3-8B tax, table)
- Line 191: `984` (Qwen3-8B subset count, table)
- Line 192: `55.07` (Qwen3-14B fair with evidence, table)
- Line 192: `55.10` (Qwen3-14B fair no-evidence, table)
- Line 192: `0.03` (Qwen3-14B tax, table)
- Line 192: `985` (Qwen3-14B subset count, table)
- Line 197: `2048` (max_new_tokens reference)
- Line 197: `1024` (max_new_tokens reference)
- Line 197: `0` (Truncation percentage for 14B at 1024)

### SECTION 7: Full Generalization Results (Lines 210-242)

**Body text (line 214):**
- Line 214: `51.09` (LLaMA-3.1-8B three-seed mean Ign-F1)
- Line 214: `2.92` (LLaMA-3.1-8B std)
- Line 214: `53.84` (LLaMA s42 Ign-F1)
- Line 214: `51.42` (LLaMA s43 Ign-F1)
- Line 214: `48.02` (LLaMA s44 Ign-F1)
- Line 214: `2048` (max_new_tokens for fair evaluation)
- Line 214: `1.53` (LLaMA s42 training-time tax)
- Line 214: `11.20` (LLaMA s43 training-time tax)
- Line 214: `2.83` (LLaMA s44 training-time tax)
- Line 214: `5.19` (LLaMA mean tax)
- Line 214: `5.25` (LLaMA tax std)
- Line 214: `8` (Architecture scale - 8B)
- Line 214: `56.54` (LLaMA RSFT three-seed mean Ign-F1)
- Line 214: `0.64` (LLaMA RSFT std)
- Line 214: `57.14` (LLaMA s42 RSFT)
- Line 214: `56.62` (LLaMA s43 RSFT)
- Line 214: `55.87` (LLaMA s44 RSFT)
- Line 214: `5.45` (Gain over SFT mean)
- Line 214: `4.6` (Variance compression factor)
- Line 214: `2.92` (Compression numerator)
- Line 214: `0.64` (Compression denominator)
- Line 214: `4.14` (Qwen3-8B gain)
- Line 214: `6.5` (Qwen3-8B compression)

**Body text (line 217):**
- Line 217: `36.59` (Re-DocRED SFT baseline Ign-F1)
- Line 217: `81.70` (Re-DocRED SFT Evi-F1)
- Line 217: `0.6674` (Re-DocRED SFT EDCR)
- Line 217: `41.45` (Re-DocRED RSFT Ign-F1)
- Line 217: `81.82` (Re-DocRED RSFT Evi-F1)
- Line 217: `0.6210` (Re-DocRED RSFT EDCR)
- Line 217: `4.86` (Gain on Re-DocRED)
- Line 217: `5.08` (Gain on DocRED)
- Line 217: `81.15` (DocRED Evi-F1)
- Line 217: `0.046` (EDCR reduction)

**Body text (line 220):**
- Line 220: `20` (Percentage points difference between dev/test)
- Line 220: `1.7` (Model scale - 1.7B)
- Line 220: `51.2` (1.7B dev Ign-F1)
- Line 220: `29.3` (1.7B test Ign-F1)
- Line 220: `4` (Model scale - 4B)
- Line 220: `44.8` (4B dev Ign-F1)
- Line 220: `25.0` (4B test Ign-F1)
- Line 220: `8` (Model scale - 8B)
- Line 220: `54.3` (8B dev Ign-F1)
- Line 220: `33.5` (8B test Ign-F1)
- Line 220: `14` (Model scale - 14B)
- Line 220: `57.9` (14B dev Ign-F1)
- Line 220: `38.5` (14B test Ign-F1)
- Line 220: `56.5` (LLaMA dev Ign-F1)
- Line 220: `35.5` (LLaMA test Ign-F1)
- Line 220: `44.6` (SFT 1.7B dev)
- Line 220: `25.8` (SFT 1.7B test)
- Line 220: `34.7` (Gold triples per document in test set)
- Line 220: `12.3` (Gold triples per document in dev set)
- Line 220: `2.82` (Ratio of test to dev density)
- Line 220: `18.9` (Min gap range)
- Line 220: `21.9` (Max gap range)
- Line 220: `1.0` (Spearman rho value)

**Body text (line 221):**
- Line 221: `2.78` (14B RSFT advantage on dev)
- Line 221: `0.37` (14B RSFT disadvantage on test)
- Line 221: `50.6` (14B SFT truncation rate %)

**Table 7 (tab:test_results):**
- Line 232: `51.19` (Qwen3-1.7B dev, table)
- Line 232: `25.79` (Qwen3-1.7B SFT test, table)
- Line 232: `29.33` (Qwen3-1.7B RSFT test, table)
- Line 232: `3.54` (Qwen3-1.7B delta, table)
- Line 232: `81.8` (Qwen3-1.7B SFT truncation %, table)
- Line 232: `73.8` (Qwen3-1.7B RSFT truncation %, table)
- Line 232: `23.20` (Qwen3-1.7B RSFT Evi-F1, table)
- Line 233: `44.82` (Qwen3-4B dev, table)
- Line 233: `22.32` (Qwen3-4B SFT test, table)
- Line 233: `25.01` (Qwen3-4B RSFT test, table)
- Line 233: `2.69` (Qwen3-4B delta, table)
- Line 233: `64.6` (Qwen3-4B SFT truncation %, table)
- Line 233: `42.8` (Qwen3-4B RSFT truncation %, table)
- Line 233: `18.38` (Qwen3-4B RSFT Evi-F1, table)
- Line 234: `54.33` (Qwen3-8B dev, table)
- Line 234: `31.06` (Qwen3-8B SFT test, table)
- Line 234: `33.53` (Qwen3-8B RSFT test, table)
- Line 234: `2.47` (Qwen3-8B delta, table)
- Line 234: `82.0` (Qwen3-8B SFT truncation %, table)
- Line 234: `1.8` (Qwen3-8B RSFT truncation %, table)
- Line 234: `25.26` (Qwen3-8B RSFT Evi-F1, table)
- Line 235: `57.85` (Qwen3-14B dev, table)
- Line 235: `38.86` (Qwen3-14B SFT test, table)
- Line 235: `38.49` (Qwen3-14B RSFT test, table)
- Line 235: `0.37` (Qwen3-14B delta (negative), table)
- Line 235: `50.6` (Qwen3-14B SFT truncation %, table)
- Line 235: `13.4` (Qwen3-14B RSFT truncation %, table)
- Line 235: `26.88` (Qwen3-14B RSFT Evi-F1, table)
- Line 236: `56.54` (LLaMA-3.1-8B dev, table)
- Line 236: `34.20` (LLaMA-3.1-8B SFT test, table)
- Line 236: `35.54` (LLaMA-3.1-8B RSFT test, table)
- Line 236: `1.34` (LLaMA-3.1-8B delta, table)
- Line 236: `65.4` (LLaMA-3.1-8B SFT truncation %, table)
- Line 236: `60.0` (LLaMA-3.1-8B RSFT truncation %, table)
- Line 236: `24.57` (LLaMA-3.1-8B RSFT Evi-F1, table)
- Line 241: `43.88` (4B comparable dev, footnote)
- Line 241: `44.23` (4B test checkpoint dev, footnote)

### SECTION 8: Test-set Evidence Tax (Lines 244-250)

**Body text (line 245):**
- Line 245: `4.86` (1.7B test tax)
- Line 245: `4.94` (LLaMA-8B test tax)
- Line 245: `0.13` (4B test tax)
- Line 245: `0.32` (14B test tax)
- Line 245: `1.71` (8B test tax)
- Line 245: `0.04` (8B dev tax)

---

## SUMMARY BY CATEGORY

**Learning Rates:** 2e-5, 5e-6, 5e-7, 1.53, 11.20

**Batch Sizes:** 4, 8, 16

**Model Scales (B):** 1.7, 4, 8, 14

**Performance Metrics (Ign-F1/Rel-F1/Evi-F1):** 38.49 to 59.17, 40.49 to 48.76, 79.61 to 83.37

**EDCR Scores:** 0.5796 to 0.6982

**Improvement Points (pp):** 0.02, 0.03, 0.04, 0.25, 0.47, 1.40, 1.41, 2.47, 2.69, 2.78, 3.54, 4.14, 4.86, 4.92, 5.08, 5.45, 5.63, 6.95

**Standard Deviations/Variance:** 0.09 to 3.80, compression ratios of 4.6x to 32.6x

**Truncation Rates (%):** 1.8, 13.4, 31.9, 42.8, 50.6, 50.9, 60.0, 64.6, 73.8, 75.6, 81.8, 82.0, 94.4

**Cohen's d Values:** 0.46, 1.79, 2.58, 3.31

**Confidence Intervals:** Multiple ranges spanning [0.04, 23.89]

**Sample Counts:** 442, 501, 971, 982, 984, 985, 3,053, 2,718

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cd7aa25-c4b8-4549-81d8-e2318fd45e72",
  "isSidechain": true,
  "agentId": "a9f9e70a81951bdd8",
  "requestId": "req_011CbPrgmYWpyJyRgieNqadG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3a7c0095-238b-4286-8395-3f6bc84851a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "7a362cc0-08ac-4cf8-8958-672775de0ebd",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "sprightly-popping-church",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FXJHrTSaZqchBKwAKTLYLY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 10154,
      "cache_read_input_tokens": 39669,
      "output_tokens": 11136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10154
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 11136,
          "cache_read_input_tokens": 39669,
          "cache_creation_input_tokens": 10154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10154,
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
