# Research conversation: Read the full contents of /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6a8bef379c2ca3e1.jsonl`
- **Structured JSON:** [`3c008a74891c85dcea78.json`](../../sessions/3c/3c008a74891c85dcea78.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-23T19:16:50.461Z_

Read the full contents of /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex - read all of it, don't skip any parts. Report every number, percentage, mean±std value, Cohen's d, chi-squared value, and any other numerical data found in the file. Also note the section structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c546e4b2-0712-4148-a8b5-618bf4a5f24e",
  "agentId": "a6a8bef379c2ca3e1",
  "type": "user",
  "uuid": "4e63e0e2-ff20-431a-98a7-f84cde1858ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3296b1fc-f6e1-46f0-b410-51841c4ff218",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T19:16:51.739Z_

I'll read the full contents of the appendix.tex file for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e63e0e2-ff20-431a-98a7-f84cde1858ee",
  "isSidechain": true,
  "agentId": "a6a8bef379c2ca3e1",
  "requestId": "req_011CbL38iyrfYM1tUQV2xEEG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a02fd511-6b9d-4069-a5c4-2eac3e9838e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3296b1fc-f6e1-46f0-b410-51841c4ff218",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VBNyKiH7xd1fA5eVJPXSdg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 513,
      "cache_read_input_tokens": 18900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 513,
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

_source line 3 · 2026-05-23T19:16:51.935Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F8sLSR1dL7RLLMbXN56qm6`</summary>

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
  "parentUuid": "a02fd511-6b9d-4069-a5c4-2eac3e9838e3",
  "isSidechain": true,
  "agentId": "a6a8bef379c2ca3e1",
  "requestId": "req_011CbL38iyrfYM1tUQV2xEEG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7e1df8e8-a11b-4134-85db-14fdc9f0d941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3296b1fc-f6e1-46f0-b410-51841c4ff218",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VBNyKiH7xd1fA5eVJPXSdg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 513,
      "cache_read_input_tokens": 18900,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 513
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 107,
          "cache_read_input_tokens": 18900,
          "cache_creation_input_tokens": 513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 513,
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

_source line 4 · 2026-05-23T19:16:52.188Z_

<details><summary>↩ Tool result · `toolu_01F8sLSR1dL7RLLMbXN56qm6`</summary>

```text
1	\section{Training Hyperparameters}
2	\label{sec:hyperparams}
3	
4	Table~\ref{tab:hyperparams} lists the hyperparameters for all training configurations. All methods use LoRA with rank $r{=}64$ and $\alpha{=}128$ applied to all linear projections (attention and feed-forward). SFT and RSFT share the same optimizer settings; RSFT differs only in data construction (top-1 CED-selected outputs from $N{=}8$ candidates). GRPO and DPO use lower learning rates to stabilize post-SFT optimization.
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
87	Table~\ref{tab:cross_detail} supplements Table~\ref{tab:scaling} in the main text with per-scale Rel-F1 and Evi-F1 breakdowns. At 1.7B, RSFT improves Rel-F1 from 45.86 to 52.81 (+6.95, multi-seed mean) while achieving Evi-F1 82.63 and EDCR 0.6217. The 4B model shows the same pattern: Rel-F1 increases from 44.39 to 45.80 (+1.41, three-seed mean). For 8B, RSFT brings Rel-F1 from 51.87 to 56.07 (three-seed mean) with Evi-F1 of 81.26 and EDCR 0.6235, confirming tight coupling between extraction and evidence at this scale. At 14B, the SFT baseline already achieves strong Rel-F1 (56.11) and Evi-F1 (82.92).
88	
89	\begin{table}[t]
90	\centering
91	\caption{Detailed Rel-F1 and Evi-F1 across model scales on DocRED dev set. SFT and RSFT columns show multi-seed means where available (Qwen3 1.7B/4B/8B: 3-seed; 14B: single seed; LLaMA SFT Rel-F1/Evi-F1: s42 only; LLaMA RSFT: 3-seed).}
92	\label{tab:cross_detail}
93	\small
94	\resizebox{\columnwidth}{!}{%
95	\begin{tabular}{lccccc}
96	\toprule
97	\textbf{Model} & \textbf{SFT Rel-F1} & \textbf{SFT Evi-F1} & \textbf{RSFT Rel-F1} & \textbf{RSFT Evi-F1} & \textbf{RSFT EDCR} \\
98	\midrule
99	Qwen3-1.7B & 45.86 & 82.85 & 52.81 & 82.63 & 0.6217 \\
100	Qwen3-4B & 44.39 & 79.61 & 45.80 & 80.96 & 0.6487 \\
101	Qwen3-8B & 51.87 & 82.94 & 56.07 & 81.26 & 0.6235 \\
102	Qwen3-14B & 56.11 & 82.92 & -- & -- & -- \\
103	LLaMA-3.1-8B & 55.14 & 81.51 & 57.75 & 82.84 & 0.5804 \\
104	\bottomrule
105	\end{tabular}%
106	}
107	\end{table}
108	
109	\begin{figure}[t]
110	\centering
111	\includegraphics[width=\columnwidth]{fig_scaling.pdf}
112	\caption{Evidence tax across model scales. Bar heights show Ign-F1 for each training configuration. The gap between no-evidence and SFT bars reverses direction between 1.7B and 4B, revealing the scale-dependent nature of the evidence tax. RSFT consistently narrows the gap toward the no-evidence upper bound.}
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
139	\vspace{-2mm}
140	{\raggedright\footnotesize Sign test: $p = 0.0625$ (one-sided binomial, $n = 4$; underpowered). The consistent direction (4/4 SFT $>$ RSFT), non-overlapping CIs at 1.7B, and large Cohen's $d$ at 1.7B and LLaMA provide practical evidence for variance compression despite limited statistical power from $N{=}3$ seeds.\par}
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
181	\caption{Training-time evidence tax under matched@2048 fair evaluation (DocRED dev Ign-F1). Both configurations evaluated at \texttt{max\_new\_tokens}$=$2048; tax computed on format-compliant intersection. Tax $=$ no-evidence $-$ with-evidence; positive $=$ cost.}
182	\label{tab:training_tax}
183	\small
184	\begin{tabular}{lcccc}
185	\toprule
186	\textbf{Model} & \textbf{Fair w/ evi} & \textbf{Fair no-evi} & \textbf{Evi Tax} & \textbf{Subset} \\
187	\midrule
188	Qwen3-1.7B & 48.38 & 42.75 & $-$5.63 & 971 \\
189	Qwen3-4B & -- & -- & +0.25{\scriptsize$\pm$0.47}$^{(3)}$ & $\geq$982 \\
190	Qwen3-8B & 50.15 & 50.19 & +0.04 & 984 \\
191	Qwen3-14B & 55.07 & 55.10 & +0.03 & 985$^\dagger$ \\
192	\bottomrule
193	\end{tabular}
194	\vspace{-2mm}
195	{\raggedright\footnotesize 1.7B and 8B are s42; 4B reports three-seed mean $\pm$ std (per-seed range: $-$0.19 to +0.73pp); 14B evaluated at @1024 with 0\% truncation for both configurations ($^\dagger$fair subset equals full dev set). Subset: documents in format-compliant intersection out of 985.\par}
196	\end{table}
197	
198	\paragraph{Evidence training and SFT seed variance.}
199	Evidence training's effect on SFT seed variance is also scale-dependent. At 4B, with-evidence SFT models show near-identical cross-seed spread (0.02pp) compared to no-evidence models (0.50pp), yielding 25$\times$ variance compression. At 8B, the compression is more modest (0.35pp vs.\ 0.48pp, 1.4$\times$). However, at 1.7B the pattern reverses: with-evidence seed spread (0.63pp) exceeds no-evidence spread (0.20pp). This reversal likely reflects the extreme truncation rates at 1.7B (75.6\% with-evidence, 94.4\% no-evidence at \texttt{max\_new\_tokens}$=$1024): truncated outputs produce noisy extraction results whose variance depends on which triples appear before the cutoff point. The RSFT variance compression reported in \S\ref{sec:scaling} is measured relative to SFT with-evidence baselines and holds at all scales regardless of this SFT-internal pattern.
200	
201	
202	\section{Why RSFT Avoids Decoupling}
203	\label{sec:rsft_theory}
204	
205	The structural difference between selection and optimization explains why RSFT does not exhibit the decoupling observed in gradient-based methods. GRPO and DPO update model parameters through gradients that optimize a reward signal. When two sub-tasks (extraction and evidence) compete for gradient capacity, the optimizer can discover and exploit the trade-off between them, improving one at the expense of the other. RSFT operates differently: it selects complete outputs and trains on them with standard supervised loss. Because the selection is discrete (accept or reject a full response), there is no gradient pathway through which the model can learn to sacrifice extraction for evidence quality. Only outputs where both extraction and evidence are jointly strong survive the CED filter. This property is not specific to RSFT's design but is a structural consequence of discrete selection over complete outputs: any selection-based method that filters on a joint quality criterion will inherit the same coupling guarantee. The implication for practitioners is direct: when optimizing for multiple coupled generation objectives, selection-based methods preserve inter-objective balance that gradient-based methods disrupt.
206	
207	
208	\section{Full Generalization Results}
209	\label{sec:generalization_full}
210	
211	\paragraph{Cross-family transfer.}
212	LLaMA-3.1-8B confirms the scaling patterns observed with Qwen3. Its SFT baseline achieves a three-seed mean of 51.09 Ign-F1 (std 2.92pp; s42: 53.84, s43: 51.42, s44: 48.02). Under matched@2048 fair evaluation, the training-time tax is consistently negative across all three seeds (s42: $-$1.53, s43: $-$11.20, s44: $-$2.83; mean $-$5.19$\pm$5.25pp), indicating that evidence generation consistently benefits LLaMA-3.1-8B. This contrasts with Qwen3-8B's approximately neutral tax (+0.04pp), suggesting that the evidence tax may be architecture-dependent at the 8B scale; however, the high magnitude variance (driven by s43, whose no-evidence configuration has a 16.3\% format failure rate that inflates the tax estimate) precludes precise quantification. RSFT CED improves LLaMA to a three-seed mean of 56.54 Ign-F1 (std 0.64pp; s42: 57.14, s43: 56.62, s44: 55.87), a +5.45 point gain over SFT mean (51.09), with 4.6$\times$ variance compression (2.92pp $\to$ 0.64pp), consistent with the pattern at the 8B scale (Qwen3-8B: +4.14, 6.5$\times$ compression).
213	
214	\paragraph{Cross-dataset robustness.}
215	On Re-DocRED~\citep{tan2022redocred}, the SFT baseline achieves 36.59 Ign-F1 (Evi-F1 81.70, EDCR 0.6674). RSFT CED improves this to 41.45 Ign-F1 (Evi-F1 81.82, EDCR 0.6210), a +4.86pp gain that closely matches the +5.08pp improvement on DocRED (RSFT three-seed mean minus SFT s42). This consistency across datasets with different annotation protocols confirms that RSFT's benefit generalizes beyond training-set-specific artifacts. Evidence quality remains stable across datasets (Evi-F1 81.82 vs.\ 81.15 on DocRED), and the EDCR reduction ($-0.046$) mirrors the DocRED pattern, further supporting the robustness of CED-based selection.
216	
217	\paragraph{Re-DocRED test set evaluation.}
218	Table~\ref{tab:test_results} reports SFT and RSFT performance on the Re-DocRED test set. We observe a consistent performance gap between dev and test sets, with test Ign-F1 approximately 20 percentage points lower (RSFT: 1.7B 51.2$\to$29.3, 4B 44.8$\to$25.0, 8B 54.3$\to$33.5, 14B 58.9$\to$38.5, LLaMA-8B 56.5$\to$35.5; SFT 1.7B: 44.6$\to$25.8). This gap is attributable to annotation density: the test set contains 34.7 gold triples per document versus 12.3 in the dev set (a 2.82$\times$ ratio), imposing a harder recall requirement. The gap magnitude is stable across scales and architectures (range: 18.9--21.9pp), and model ranking is perfectly preserved (Spearman $\rho{=}1.0$), indicating that the absolute drop reflects the test annotation scheme rather than a model-specific deficiency. At 14B, the RSFT advantage observed on dev (+3.79pp) reverses on test ($\Delta{=}{-}0.37$pp); we note that the SFT model's 50.6\% truncation rate implies longer outputs that generate more candidate triples to match the test set's dense annotation scheme.
219	
220	\begin{table}[t]
221	\centering
222	\caption{SFT and RSFT performance on Re-DocRED test set (Ign-F1 \%). Dev Ign-F1 (RSFT) from Table~\ref{tab:scaling}. All test results use s42.}
223	\label{tab:test_results}
224	\small
225	\resizebox{\columnwidth}{!}{%
226	\begin{tabular}{lccccccc}
227	\toprule
228	\textbf{Model} & \textbf{Dev} & \textbf{SFT} & \textbf{RSFT} & \textbf{$\Delta$} & \textbf{Tr. SFT} & \textbf{Tr. RSFT} & \textbf{Evi-F1} \\
229	\midrule
230	Qwen3-1.7B & 51.19 & 25.79 & 29.33 & +3.54 & 81.8 & 73.8 & 23.20 \\
231	Qwen3-4B & 44.82$^\dagger$ & 22.32 & 25.01 & +2.69 & 64.6 & 42.8 & 18.38 \\
232	Qwen3-8B & 54.33 & 31.06 & 33.53 & +2.47 & 82.0 & 1.8 & 25.26 \\
233	Qwen3-14B & 58.86 & 38.86 & 38.49 & $-$0.37 & 50.6 & 13.4 & 26.88 \\
234	LLaMA-3.1-8B & 56.54 & 34.20 & 35.54 & +1.34 & 65.4 & 56.6 & 25.09 \\
235	\bottomrule
236	\end{tabular}%
237	}
238	\vspace{-2mm}
239	{\raggedright\footnotesize $^\dagger$4B dev Ign-F1 is three-seed mean from original checkpoint; test results use retrained checkpoint (original unavailable for reproduction; retrained v2 achieves comparable dev performance, 43.88 vs.\ 44.23). $\Delta$: RSFT $-$ SFT. Evi-F1: RSFT joint (DREEAM protocol). Tr.: truncation rate (\%). Dev is RSFT three-seed mean from Table~\ref{tab:scaling}.\par}
240	\end{table}
241	
242	\paragraph{Test-set evidence tax.}
243	Table~\ref{tab:test_tax} reports the evidence tax on the Re-DocRED test set, comparing SFT models trained with and without evidence in the output format. Test-set evaluation confirms the directional pattern observed on development data across all five model configurations: the tax is negative (beneficial) at 1.7B ($-$4.86pp) and LLaMA-8B ($-$4.94pp), and near-neutral at mid-scales ($-$0.13pp at 4B, $-$0.32pp at 14B). The 8B test tax ($-$1.71pp) shows slight variation from its near-neutral dev counterpart (+0.04pp), though both remain modest relative to the 1.7B and LLaMA benefits.
244	
245	\begin{table}[t]
246	\centering
247	\caption{Evidence tax on Re-DocRED test set (Ign-F1 \%). Tax $=$ no-evi $-$ with-evi; negative $=$ benefit. All results use s42. Dev tax from Table~\ref{tab:training_tax}.}
248	\label{tab:test_tax}
249	\small
250	\resizebox{\columnwidth}{!}{%
251	\begin{tabular}{lcccc}
252	\toprule
253	\textbf{Model} & \textbf{With-evi} & \textbf{No-evi} & \textbf{Test Tax} & \textbf{Dev Tax} \\
254	\midrule
255	Qwen3-1.7B & 25.79 & 20.93 & $-$4.86 & $-$5.63 \\
256	Qwen3-4B & 22.32 & 22.19 & $-$0.13 & +0.25 \\
257	Qwen3-8B & 31.06 & 29.35 & $-$1.71 & +0.04 \\
258	Qwen3-14B & 38.86 & 38.54 & $-$0.32 & +0.03 \\
259	LLaMA-3.1-8B & 34.20 & 29.26 & $-$4.94 & $-$5.19 \\
260	\bottomrule
261	\end{tabular}%
262	}
263	\end{table}
264	
265	\paragraph{RSFT test-set evidence tax.}
266	Table~\ref{tab:rsft_test_tax} reports the inference-time evidence tax for RSFT models on the Re-DocRED test set (same RSFT model evaluated with vs.\ without evidence output; per-seed s42 values). Figure~\ref{fig:evidence_tax} presents multi-seed means with error bars where $\geq$2 seeds are available. At 1.7B, RSFT preserves a strong evidence benefit ($-$5.43pp), comparable to the SFT tax ($-$4.86pp). At 4B, the tax is mildly positive (+1.65$\pm$0.29pp, three-seed mean; s42: +1.51pp), the Qwen3 scale with the largest positive RSFT test tax; this contrasts with the near-neutral SFT tax at 4B ($-$0.13pp). At 8B, RSFT compresses the tax magnitude relative to SFT ($-$0.91$\pm$0.74pp, three-seed mean, vs.\ SFT $-$1.71pp). At 14B, the two-seed mean tax is +0.43$\pm$0.49pp (s42: +0.77pp, s43: +0.08pp), reversing sign relative to dev ($-$4.54pp); the small test magnitude and high inter-seed variance may reflect noise or evaluation protocol differences given the 2.82$\times$ annotation density gap between dev and test. LLaMA-3.1-8B shows partial compression from SFT ($-$4.94pp $\to$ $-$1.46$\pm$0.40pp, two-seed mean).
267	
268	\begin{table}[t]
269	\centering
270	\caption{RSFT inference-time evidence tax on Re-DocRED test set (Ign-F1 \%). Tax $=$ no-evi $-$ with-evi; positive $=$ cost. All results use s42.}
271	\label{tab:rsft_test_tax}
272	\small
273	\resizebox{\columnwidth}{!}{%
274	\begin{tabular}{lccc}
275	\toprule
276	\textbf{Model} & \textbf{RSFT w/ evi} & \textbf{RSFT no-evi} & \textbf{RSFT Tax} \\
277	\midrule
278	Qwen3-1.7B & 29.33 & 23.90 & $-$5.43$^\ddagger$ \\
279	Qwen3-4B & 25.01 & 26.52 & +1.51 \\
280	Qwen3-8B & 33.53 & 33.19 & $-$0.34 \\
281	Qwen3-14B & 38.49 & 39.26 & +0.77$^\dagger$ \\
282	LLaMA-3.1-8B & 35.54 & 33.80 & $-$1.74 \\
283	\bottomrule
284	\end{tabular}%
285	}
286	\vspace{-2mm}
287	{\raggedright\footnotesize $^\ddagger$1.7B no-evi truncation rate is 94.8\% (vs.\ 73.8\% with-evi), which may amplify the tax magnitude. $^\dagger$14B shows a dev-test reversal (dev tax $= -$4.54pp); the two-seed test mean (+0.43$\pm$0.49pp) is small relative to inter-seed variance (CI crosses zero), suggesting the direction signal is noise-dominated at this magnitude. All other scales preserve dev-test direction consistency.\par}
288	\end{table}
289	
290	\paragraph{Comparison to supervised methods.}
291	Table~\ref{tab:encoder_comparison} directly compares encoder-based methods with our LLM-based approach. Encoder methods achieve substantially higher extraction performance (Rel-F1 63--65 vs.\ our 45--56), reflecting decades of architecture-specific optimization for the classification formulation. However, their evidence identification operates as binary sentence classification, producing Evi-F1 of 52--56 under a joint evaluation protocol. Our TP-only Evi-F1 exceeds 80\%, indicating that when the model correctly identifies a triple, it produces higher-quality evidence than encoder methods. The joint Evi-F1 gap (36.1 vs.\ 54.15) is driven primarily by extraction performance rather than evidence quality: false-positive and false-negative triples dilute the denominator. The substantial extraction gap (16--18pp Ign-F1) reflects the current limitation of generative LLM approaches relative to specialized encoder models. Closing this gap requires improving extraction capability of LLM-based methods, an orthogonal direction to the evidence faithfulness problem we address.
292	
293	\begin{table}[t]
294	\centering
295	\caption{Comparison with encoder-based methods on DocRED dev set. Encoder methods use RoBERTa-large; LLM methods use Qwen3. Evi-F1 for encoder methods uses joint evaluation (all triples in denominator); our joint Evi-F1 follows the same protocol for fair comparison. TP-only Evi-F1 conditions on correctly predicted triples. Rel-F1 is reported in percentage for all methods.}
296	\label{tab:encoder_comparison}
297	\small
298	\resizebox{\columnwidth}{!}{%
299	\begin{tabular}{llcccc}
300	\toprule
301	\textbf{Method} & \textbf{Type} & \textbf{Ign-F1} & \textbf{Rel-F1} & \textbf{Evi-F1 (joint)} & \textbf{Evi-F1 (TP)} \\
302	\midrule
303	ATLOP & Encoder & 61.32 & 63.18 & -- & -- \\
304	EIDER & Encoder & 62.34 & 64.27 & 52.54 & -- \\
305	SAIS & Encoder & 62.23 & 65.17 & 55.84 & -- \\
306	DREEAM & Encoder & 61.71 & 63.49 & 54.15 & -- \\
307	\midrule
308	Ours (4B RSFT) & LLM & 44.82 & 45.80 & 36.1 & 80.96 \\
309	Ours (8B RSFT) & LLM & 54.33 & 56.07 & -- & 81.26 \\
310	Ours (14B RSFT) & LLM & 58.86 & 60.09 & 48.59 & 83.92 \\
311	\bottomrule
312	\end{tabular}%
313	}
314	\end{table}
315	
316	
317	\section{Decoupling Spectrum Data}
318	\label{sec:spectrum_data}
319	
320	\begin{table}[t]
321	\centering
322	\caption{Evidence-extraction decoupling across RL paradigms (Qwen3-4B). Severity indicates the degree of extraction collapse relative to evidence improvement.}
323	\label{tab:spectrum}
324	\small
325	\resizebox{\columnwidth}{!}{%
326	\begin{tabular}{llcccc}
327	\toprule
328	\textbf{Paradigm} & \textbf{Config} & \textbf{Rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Severity} \\
329	\midrule
330	GRPO & QLoRA $G{=}4$ & 1.38 & 85.04 & 0.9876 & Catastrophic \\
331	GRPO & bf16 $G{=}8$ & 45.49 & 80.86 & 0.6318 & Mild \\
332	DPO & bf16 1ep & 33.37 & 80.90 & 0.8123 & Gradual \\
333	DPO & bf16 3ep & 31.45 & 84.84 & 0.7503 & Gradual \\
334	\midrule
335	SFT & baseline$^\ddagger$ & 44.39 & 79.61 & 0.6797 & None \\
336	RSFT & CED$^\ddagger$ & 45.80 & 80.96 & 0.6487 & None \\
337	\bottomrule
338	\end{tabular}%
339	}
340	\vspace{-2mm}
341	{\raggedright\footnotesize $^\ddagger$Three-seed mean. DPO rows evaluated at \texttt{max\_new\_tokens}$=$2048 (matched protocol); all other rows at 1024. Severity reflects training trajectory stability (propensity for extraction collapse during optimization), not the final-checkpoint EDCR value.\par}
342	\end{table}
343	
344	
345	\section{GRPO Training Dynamics}
346	\label{sec:grpo_dynamics}
347	
348	\begin{figure*}[t]
349	\centering
350	\includegraphics[width=\linewidth]{fig_grpo_dynamics.pdf}
351	\caption{Training dynamics of GRPO under different configurations. (a)~Relation F1 across checkpoints: G=4 QLoRA suffers catastrophic collapse at step~10, while G=8 bf16 remains stable. (b)~Evidence F1 stays intact for G=8 bf16, confirming the generation mechanism itself does not fail. (c)~Evidence-Decoupling Ratio (EDCR) reveals near-total decoupling in G=4 QLoRA (extraction collapses to Rel-F1 1.4), while G=8 bf16 maintains healthy ratios.}
352	\label{fig:grpo_dynamics}
353	\end{figure*}
354	
355	
356	\section{Error Analysis: SFT vs.\ RSFT}
357	\label{sec:error_analysis}
358	
359	Table~\ref{tab:error_analysis} decomposes the extraction improvements from RSFT into error categories across three scales. Three mechanisms drive the gains consistently:
360	
361	\paragraph{Truncation false negatives.} SFT models frequently hit the generation length limit, producing incomplete outputs that miss triples. RSFT training on compact, high-quality outputs reduces this truncation rate. The effect is strongest at 1.7B ($-841$ truncation FN, $-22$\%), where the SFT model's output length is least controlled.
362	
363	\paragraph{Hallucinated false positives.} CED-based filtering removes training examples with unfaithful predictions, reducing the rate of hallucinated triples at inference. LLaMA benefits most ($-593$ hallucinated FP, $-11.8$\%), suggesting cross-architecture variation in hallucination susceptibility.
364	
365	\paragraph{Duplicate predictions.} RSFT training data, selected for quality, contains fewer repetitive patterns. This propagates to inference, reducing duplicate triples by $11$--$20$\% across scales, with 1.7B showing the largest reduction ($-20.2$\%).
366	
367	\paragraph{Evidence quality unchanged.} Despite substantial extraction improvements, evidence exact-match F1 changes by less than 0.4pp at every scale. RSFT selects for joint extraction-evidence quality, but the evidence signal in CED scoring does not translate into measurable evidence improvement. This suggests that evidence grounding requires targeted optimization (e.g., evidence-specific rewards in RL) rather than data selection alone.
368	
369	\paragraph{Residual difficulty.} The proportion of ``other'' false negatives (triples missed for reasons beyond truncation or formatting) increases by 13--15\% in relative terms after RSFT. As easy errors (truncation, duplication) are eliminated, the remaining error distribution shifts toward harder cases: cross-sentence reasoning, implicit relations, and long-tail entity pairs. The relation types with the largest RSFT gains (participant, conflict, league, screenwriter, operator, contains\_administrative\_territory) involve cross-sentence reasoning or long-tail entities, consistent with RSFT's selection pressure toward diverse, high-quality outputs.
370	
371	\begin{table}[t]
372	\centering
373	\caption{Error pattern changes from SFT to RSFT across scales. $\Delta$\% shows relative change. Truncation FN, hallucinated FP, and duplicates all decrease; evidence quality and residual FN difficulty are unchanged.}
374	\label{tab:error_analysis}
375	\small
376	\resizebox{\columnwidth}{!}{%
377	\begin{tabular}{llccc}
378	\toprule
379	\textbf{Error Category} & \textbf{Direction} & \textbf{1.7B} & \textbf{4B} & \textbf{8B / LLaMA} \\
380	\midrule
381	Truncation FN & $\downarrow$ & $-$22\% & $-$16\% & $-$18\% \\
382	Hallucinated FP & $\downarrow$ & $-$8\% & $-$6\% & $-$12\% \\
383	Duplicates & $\downarrow$ & $-$20\% & $-$11\% & $-$14\% \\
384	Evidence (exact) & $\approx$ & $<$0.4pp & $<$0.4pp & $<$0.4pp \\
385	FN: other & $\uparrow$ & +13\% & +15\% & +14\% \\
386	\bottomrule
387	\end{tabular}%
388	}
389	\end{table}
390	
391	
392	\section{Per-Relation EDCR Distribution}
393	\label{sec:edcr_per_relation}
394	
395	Computing EDCR for each of the 76 relation types with $\geq$5 evaluation samples (from the RSFT CED s42 model) reveals that per-relation EDCR correlates strongly with per-relation Rel-F1 ($\rho = -0.79$, $n = 76$, $p < 0.001$), confirming its utility as a difficulty indicator. Filtering to types with $\geq$5 predictions strengthens the correlation ($\rho = -0.85$, $n = 74$, $p < 0.001$). Per-relation EDCR is statistically independent of Evi-F1 ($\rho = -0.06$, $p = 0.58$), and Evi-F1 itself shows no association with Rel-F1 ($\rho = -0.01$, $p = 0.91$). These null correlations establish that evidence quality and extraction ability are fully decoupled across relation types. Extreme cases illustrate the diagnostic power: \texttt{date\_of\_birth} has EDCR $= 0.118$ (highly faithful, with extraction and evidence tightly coupled), while \texttt{head\_of\_government} reaches $0.956$ (highly decoupled). This per-relation analysis avoids the shared-component concern present in cross-method EDCR-vs-Rel-F1 correlation, providing independent validation of EDCR's diagnostic utility. A permutation test (10,000 iterations) on the per-relation correlation yields $p < 0.0001$, confirming that the association is not an artifact of the shared TP component.
396	
397	\paragraph{Partial correlations controlling for TP.}
398	Because EDCR shares TP (true positives) in both numerator and denominator with Rel-F1, we report partial correlations controlling for Evi-Recall$_\text{TP}$. At the cross-method level ($n = 17$ seed-specific configurations), the partial Spearman $\rho = -0.8541$ ($p = 0.000025$), virtually unchanged from the raw $\rho = -0.8554$ (0.15\% reduction). Removing the GRPO QLoRA outlier yields partial $\rho = -0.8681$ ($n = 16$, $p = 0.000027$). Aggregating to $n = 7$ unique methods: raw $\rho = -0.9643$, partial $\rho = -0.9617$. These results confirm that the EDCR--Rel-F1 association is not driven by the shared TP component. Note that seed-level configurations ($n = 17$) are not fully independent; the $n = 7$ unique-method analysis provides a conservative estimate.
399	
400	\paragraph{Similar-TP, different-EDCR pairs.}
401	To further validate that EDCR captures information beyond what TP alone provides, we identify configuration pairs with similar Evi-Recall$_\text{TP}$ ($|\Delta| < 5$pp) but substantially different EDCR ($|\Delta| > 5$pp). Forty-eight such pairs exist across all configurations. The most illustrative: DPO-CED 1-epoch (Evi-Recall$_\text{TP} = 0.833$) vs.\ RSFT CED LLaMA s43 (Evi-Recall$_\text{TP} = 0.829$) differ by only 2.4pp in TP-conditioned evidence recall but 13.6pp in EDCR, reflecting the substantial extraction gap between these methods. This pattern demonstrates that EDCR captures extraction-evidence alignment that aggregate TP metrics miss.
402	
403	\begin{figure}[t]
404	\centering
405	\includegraphics[width=\linewidth]{fig_edcr_relations.pdf}
406	\caption{Per-relation EDCR distribution across all 93 relation types observed in the development set (of 96 defined in DocRED). The correlation analysis in the text uses the 76 types with $\geq$5 samples for statistical reliability. Red bars indicate EDCR $\geq$ 0.70 (severe decoupling), green bars indicate EDCR $<$ 0.30 (healthy evidence grounding). Seven types exhibit EDCR = 1.0.}
407	\label{fig:edcr_relations}
408	\end{figure}
409	
410	
411	\section{Qualitative Analysis}
412	\label{sec:qualitative}
413	
414	We present representative examples illustrating three phenomena: evidence quality differences between SFT and RSFT, GRPO format gaming under catastrophic collapse, and per-relation EDCR diagnostics.
415	
416	\paragraph{Case 1: Evidence quality.}
417	Table~\ref{tab:case_evidence} compares evidence citations from SFT and RSFT on three documents. SFT tends to cite many sentences indiscriminately, including distractors unrelated to the target triple, while RSFT selects precisely the gold evidence sentences. For \emph{America's Sweetheart}, SFT cites 6 sentences (precision 0.17) whereas RSFT cites only the single correct sentence (precision 1.00). The pattern is consistent: SFT achieves evidence precision of 0.00--0.20 across these examples, while RSFT achieves 1.00 in all three cases.
418	
419	\begin{table}[t]
420	\centering
421	\caption{Evidence citation comparison between SFT and RSFT. Precision measures the fraction of cited sentences that match gold evidence.}
422	\label{tab:case_evidence}
423	\small
424	\resizebox{\columnwidth}{!}{%
425	\begin{tabular}{llccc}
426	\toprule
427	\textbf{Document} & \textbf{Triple} & \textbf{SFT Prec.} & \textbf{RSFT Prec.} & \textbf{SFT \#Cited} \\
428	\midrule
429	Oleg Tinkov & (Oleg Tinkov, country of citizenship, Russia) & 0.00 & 1.00 & 3 \\
430	America's Sweetheart & (record label, country, United States) & 0.17 & 1.00 & 6 \\
431	Jade (Mortal Kombat) & (Jade, present in work, Mortal Kombat) & 0.20 & 1.00 & 5 \\
432	\bottomrule
433	\end{tabular}%
434	}
435	\end{table}
436	
437	\paragraph{Case 2: GRPO format gaming.}
438	Under catastrophic collapse (GRPO QLoRA $G{=}4$), the model abandons the DocRED 96-type relation ontology and generates free-text relation labels. On the document \emph{Something to Believe In}, the model produces 35 predicted triples with relations such as ``is a'', ``honor'', and ``location'', none of which belong to the target ontology. All 35 predictions are incorrect. Similarly, for \emph{J\'{o}zef Pi\l{}sudski Monument}, 28 predictions use non-standard relations with 0 correct matches. The model retains the structural format of triple-with-evidence output but fills it with fabricated relation types. The model produces well-formed evidence for these non-existent relations.
439	
440	\paragraph{Case 3: EDCR diagnostics.}
441	Per-relation EDCR identifies specific relation types where extraction and evidence are misaligned. For \texttt{date\_of\_birth} (EDCR $= 0.118$), the model's evidence consistently matches gold annotations: both extraction and evidence point to the same biographical sentence. In contrast, \texttt{notable\_work} (EDCR $= 0.941$) exhibits severe decoupling: the model cites sentence [0] (a general introduction) instead of the gold evidence sentence [3] (which contains the actual work attribution). High-EDCR relations tend to involve indirect or multi-hop reasoning where surface-level context misleads the evidence generator.
442	
443	
444	\section{Use of AI Assistants}
445	\label{app:ai-assistants}
446	
447	We used Claude (Anthropic) as an AI coding and writing assistant
448	throughout this work. Specifically:
449	\begin{itemize}
450	    \item \textbf{Code:} drafting experiment scripts, data-processing
451	    pipelines, and analysis utilities; debugging and refactoring.
452	    \item \textbf{Writing:} drafting and revising paper sections,
453	    polishing prose, and reformatting LaTeX.
454	    \item \textbf{Literature:} summarizing related papers to inform
455	    the related-work section.
456	\end{itemize}
457	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e1df8e8-a11b-4134-85db-14fdc9f0d941",
  "isSidechain": true,
  "promptId": "c546e4b2-0712-4148-a8b5-618bf4a5f24e",
  "agentId": "a6a8bef379c2ca3e1",
  "type": "user",
  "uuid": "dbda2672-f050-4c23-8b4f-359ffc33f2be",
  "sourceToolAssistantUUID": "7e1df8e8-a11b-4134-85db-14fdc9f0d941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3296b1fc-f6e1-46f0-b410-51841c4ff218",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-23T19:17:43.026Z_

## Summary of Numerical Data in appendix.tex

I've read the entire appendix.tex file. Here is a comprehensive report of all numerical data, organized by section:

### **Section 1: Training Hyperparameters (lines 1-36)**

**LoRA Configuration:**
- Rank r = 64
- Alpha α = 128

**Learning Rates:**
- SFT/RSFT: 2e-5
- GRPO: 5e-6
- DPO: 5e-7

**Batch Sizes (effective):**
- SFT/RSFT: 16
- GRPO QLoRA: 4
- GRPO bf16: 8
- DPO: 4

**Epochs:**
- SFT/RSFT: 3
- DPO: 1 and 3

**Max steps:**
- GRPO: 100

**Gradient accumulation:**
- SFT/RSFT: 4
- GRPO QLoRA: 16
- GRPO bf16: 4
- DPO: 4

**Max new tokens:**
- All: 1024

**KL coefficient:**
- GRPO: 0.01

**DPO Beta:**
- 0.1

**Group size (G):**
- GRPO QLoRA: 4
- GRPO bf16: 8

**Candidates (N):**
- RSFT: 8
- DPO: 8

**Training samples:**
- SFT/GRPO/DPO: 3,053
- RSFT: 2,718

---

### **Section 2: Full Ablation Results (lines 39-81)**

**Four-seed mean (RSFT CED k=1):**
- Ign-F1: 44.66 (std ±0.49)

**SFT s42 baseline:**
- Ign-F1: 39.74

**Improvement:**
- +4.92pp (CED RSFT vs. random)

**Three-seed mean (Table reference, seeds 42/43/44):**
- Ign-F1: 44.82

**Seed s45:**
- Ign-F1: 44.16

**Random RSFT k=1:**
- Ign-F1: 41.14
- Improvement: +1.40pp over SFT s42

**RSFT k=3:**
- Ign-F1: 43.64

**SFT no-evidence:**
- Ign-F1: 47.21

**Rel-F1 mean (CED RSFT, seeds 42/43/44/45):**
- 45.63
- Range: 45.14–46.21

**Flat-NLI RSFT mean (seeds 42, 43):**
- Rel-F1: 45.61
- Range: 45.35–45.86
- Difference from CED: 0.02pp

**Top-k selection (k=1):**
- Ign-F1: 44.66
- Rel-F1: 45.63
- Mean extraction F1 of training data: 61.57
- Mean CED of training data: 0.6683

**Top-k selection (k=3):**
- Ign-F1: 43.64
- Rel-F1: 44.54
- Mean extraction F1 of training data: 57.61
- Mean CED of training data: 0.6205
- Ratio multiplier: 2.96×

**NLI scorer capacity (v3-base vs. v3-large):**
- v3-base Ign-F1 (s42): 44.23
- v3-large Ign-F1 (s42): 45.33
- Improvement: +1.10pp
- v3-base seed noise: ±0.88pp (s42: 44.23, s44: 45.11)
- v3-base Rel-F1 (s42): 45.17
- v3-large Rel-F1 (s42): 46.36
- Improvement: +1.19pp
- v3-base Evi-F1 (s42): 81.74
- v3-large Evi-F1 (s42): 81.94
- Improvement: +0.20pp
- v3-base EDCR: 0.6569
- v3-large EDCR: 0.6530
- Change: −0.39pp
- Parameter ratio: 3.5× larger

**Per-seed results (RSFT CED k=1):**

| Seed | Ign-F1 | Rel-F1 | Evi-F1 | EDCR |
|------|--------|--------|--------|------|
| s42  | 44.23  | 45.17  | 81.74  | 0.6569 |
| s43  | 45.12  | 46.01  | 80.63  | 0.6542 |
| s44  | 45.11  | 46.21  | 80.50  | 0.6350 |
| s45  | 44.16  | 45.14  | 81.74  | 0.6550 |
| Mean | 44.66  | 45.63  | 81.15  | 0.6503 |

**SFT baseline (s42):**
- Ign-F1: 39.74
- Rel-F1: 40.49
- Evi-F1: 79.86
- EDCR: 0.6982

**RSFT random k=1:**
- Ign-F1: 41.14
- Rel-F1: 41.98
- Evi-F1: 79.64
- EDCR: 0.6971

**RSFT CED k=3:**
- Ign-F1: 43.64
- Rel-F1: 44.54
- Evi-F1: 80.88
- EDCR: 0.6635

**RSFT flat-NLI (s42):**
- Rel-F1: 45.35
- Evi-F1: 80.43
- EDCR: 0.6431

**RSFT flat-NLI (s43):**
- Rel-F1: 45.86
- Evi-F1: 81.58
- EDCR: 0.6505

**RSFT flat-NLI (mean):**
- Rel-F1: 45.61
- Evi-F1: 81.01
- EDCR: 0.6468

**RSFT CED k=1 v3-large (s42):**
- Ign-F1: 45.33
- Rel-F1: 46.36
- Evi-F1: 81.94
- EDCR: 0.6530

---

### **Section 3: Scaling Details (lines 84-107)**

**Qwen3-1.7B:**
- SFT Rel-F1: 45.86
- RSFT Rel-F1: 52.81
- Improvement: +6.95pp (multi-seed mean)
- RSFT Evi-F1: 82.63
- RSFT EDCR: 0.6217

**Qwen3-4B:**
- SFT Rel-F1: 44.39
- RSFT Rel-F1: 45.80
- Improvement: +1.41pp (three-seed mean)

**Qwen3-8B:**
- SFT Rel-F1: 51.87
- RSFT Rel-F1: 56.07 (three-seed mean)
- Evi-F1: 81.26
- EDCR: 0.6235

**Qwen3-14B:**
- SFT Rel-F1: 56.11
- SFT Evi-F1: 82.92

**LLaMA-3.1-8B:**
- SFT Rel-F1: 55.14
- SFT Evi-F1: 81.51
- RSFT Rel-F1: 57.75
- RSFT Evi-F1: 82.84
- RSFT EDCR: 0.5804

---

### **Section 4: Variance Compression Confidence Intervals (lines 117-141)**

**Qwen3-1.7B:**
- SFT std: 2.79pp
- SFT 95% CI: [1.45, 17.55]
- RSFT std: 0.09pp
- RSFT 95% CI: [0.04, 0.54]
- Compression: 32.6×
- Cohen's d: 3.31

**Qwen3-4B:**
- SFT std: 3.80pp
- SFT 95% CI: [1.98, 23.89]
- RSFT std: 0.51pp
- RSFT 95% CI: [0.27, 3.21]
- Compression: 7.5×
- Cohen's d: 0.46

**Qwen3-8B:**
- SFT std: 3.23pp
- SFT 95% CI: [1.68, 20.31]
- RSFT std: 0.50pp
- RSFT 95% CI: [0.26, 3.15]
- Compression: 6.5×
- Cohen's d: 1.79

**LLaMA-3.1-8B:**
- SFT std: 2.92pp
- SFT 95% CI: [1.52, 18.37]
- RSFT std: 0.64pp
- RSFT 95% CI: [0.33, 4.01]
- Compression: 4.6×
- Cohen's d: 2.58

**Statistical test:**
- Sign test: p = 0.0625 (one-sided binomial, n = 4; underpowered)

---

### **Section 5: Controlled Evaluation Subset (lines 144-167)**

**1.7B evidence tax (matched@2048):**
- Truncation rates at @1024: 50.9% (no-evidence, 501/985) vs. 31.9% (evidence, 314/985)
- Fair-subset documents: 971/985
- Tax: −5.63pp (s42)
- Stricter controlled subset (@1024): 442/985 documents
- Tax: −6.2pp

**Output duplication rates:**

| Scale | With evidence | No evidence | Gap |
|-------|---------------|-------------|-----|
| 1.7B  | 33.0%         | 60.5%       | 27.5pp |
| 4B    | 31.1%         | 43.2%       | 12.1pp |
| 8B    | 29.2%         | 32.9%       | 3.7pp |

**Truncation Δ (no-evidence rate - with-evidence rate):**
- 1.7B: +19pp (no-evi worse)
- 4B: +2pp (neutral)
- 8B: −9pp (evi worse)

**4B matched@2048 training-time tax:**
- +0.25±0.47pp (three-seed mean)

---

### **Section 6: Training-Time Evidence Tax (lines 170-200)**

**Qwen3-1.7B matched@2048:**
- Fair with-evidence: 48.38 Ign-F1
- Fair no-evidence: 42.75 Ign-F1
- Tax: −5.63pp
- Fair-subset: 971/985

**Qwen3-4B:**
- Tax: +0.25±0.47pp (three-seed mean)
- Per-seed range: −0.19 to +0.73pp
- Subset: ≥982/985

**Qwen3-8B:**
- Fair with-evidence: 50.15 Ign-F1
- Fair no-evidence: 50.19 Ign-F1
- Tax: +0.04pp
- Subset: 984/985

**Qwen3-14B:**
- Fair with-evidence: 55.07 Ign-F1
- Fair no-evidence: 55.10 Ign-F1
- Tax: +0.03pp
- Subset: 985/985

**4B evidence training seed variance:**
- With-evidence spread: 0.02pp
- No-evidence spread: 0.50pp
- Compression: 25×

**8B evidence training seed variance:**
- With-evidence spread: 0.35pp
- No-evidence spread: 0.48pp
- Compression: 1.4×

**1.7B evidence training seed variance (reversed pattern):**
- With-evidence spread: 0.63pp
- No-evidence spread: 0.20pp
- Truncation rates at @1024: 75.6% (with-evidence), 94.4% (no-evidence)

---

### **Section 7: Full Generalization Results (lines 208-264)**

**LLaMA-3.1-8B SFT baseline (three-seed mean):**
- Ign-F1: 51.09
- Std: 2.92pp
- s42: 53.84
- s43: 51.42
- s44: 48.02

**LLaMA-3.1-8B matched@2048 training-time tax:**
- s42: −1.53pp
- s43: −11.20pp
- s44: −2.83pp
- Mean: −5.19±5.25pp

**LLaMA-3.1-8B RSFT CED (three-seed mean):**
- Ign-F1: 56.54
- Std: 0.64pp
- s42: 57.14
- s43: 56.62
- s44: 55.87
- Gain over SFT: +5.45pp
- Variance compression: 4.6× (2.92pp → 0.64pp)

**Re-DocRED SFT baseline:**
- Ign-F1: 36.59
- Evi-F1: 81.70
- EDCR: 0.6674

**Re-DocRED RSFT CED:**
- Ign-F1: 41.45
- Evi-F1: 81.82
- EDCR: 0.6210
- Gain: +4.86pp

**Re-DocRED test set performance gap:**
- Dev vs. test Ign-F1 drops: ~20pp
- Qwen3-1.7B: 51.2 → 29.3
- Qwen3-4B: 44.8 → 25.0
- Qwen3-8B: 54.3 → 33.5
- Qwen3-14B: 58.9 → 38.5
- LLaMA-8B: 56.5 → 35.5
- SFT 1.7B: 44.6 → 25.8
- Range: 18.9–21.9pp
- Spearman ρ: 1.0 (perfect ranking preservation)

**Test set annotation density:**
- Test set: 34.7 gold triples per document
- Dev set: 12.3 gold triples per document
- Ratio: 2.82×

**Test set results:**

| Model | Dev | SFT | RSFT | Δ | Tr. SFT | Tr. RSFT | Evi-F1 |
|-------|-----|-----|------|------|---------|----------|--------|
| Qwen3-1.7B | 51.19 | 25.79 | 29.33 | +3.54 | 81.8% | 73.8% | 23.20 |
| Qwen3-4B | 44.82 | 22.32 | 25.01 | +2.69 | 64.6% | 42.8% | 18.38 |
| Qwen3-8B | 54.33 | 31.06 | 33.53 | +2.47 | 82.0% | 1.8% | 25.26 |
| Qwen3-14B | 58.86 | 38.86 | 38.49 | −0.37 | 50.6% | 13.4% | 26.88 |
| LLaMA-3.1-8B | 56.54 | 34.20 | 35.54 | +1.34 | 65.4% | 56.6% | 25.09 |

**SFT test-set evidence tax:**

| Model | With-evi | No-evi | Test Tax | Dev Tax |
|-------|----------|--------|----------|---------|
| Qwen3-1.7B | 25.79 | 20.93 | −4.86 | −5.63 |
| Qwen3-4B | 22.32 | 22.19 | −0.13 | +0.25 |
| Qwen3-8B | 31.06 | 29.35 | −1.71 | +0.04 |
| Qwen3-14B | 38.86 | 38.54 | −0.32 | +0.03 |
| LLaMA-3.1-8B | 34.20 | 29.26 | −4.94 | −5.19 |

**RSFT inference-time evidence tax on test set:**

| Model | RSFT w/ evi | RSFT no-evi | RSFT Tax |
|-------|-------------|-------------|----------|
| Qwen3-1.7B | 29.33 | 23.90 | −5.43 |
| Qwen3-4B | 25.01 | 26.52 | +1.51 |
| Qwen3-8B | 33.53 | 33.19 | −0.34 |
| Qwen3-14B | 38.49 | 39.26 | +0.77 |
| LLaMA-3.1-8B | 35.54 | 33.80 | −1.74 |

**4B test mean:**
- RSFT tax: +1.65±0.29pp (three-seed mean)

**8B test mean:**
- RSFT tax: −0.91±0.74pp (three-seed mean)

**14B test mean:**
- RSFT tax: +0.43±0.49pp (two-seed mean)
- Crosses zero

**LLaMA test mean:**
- RSFT tax: −1.46±0.40pp (two-seed mean)

**1.7B test truncation rates:**
- No-evi: 94.8%
- With-evi: 73.8%

**Encoder comparison on DocRED dev:**

| Method | Type | Ign-F1 | Rel-F1 | Evi-F1 (joint) | Evi-F1 (TP) |
|--------|------|--------|--------|----------------|------------|
| ATLOP | Encoder | 61.32 | 63.18 | -- | -- |
| EIDER | Encoder | 62.34 | 64.27 | 52.54 | -- |
| SAIS | Encoder | 62.23 | 65.17 | 55.84 | -- |
| DREEAM | Encoder | 61.71 | 63.49 | 54.15 | -- |
| Ours 4B RSFT | LLM | 44.82 | 45.80 | 36.1 | 80.96 |
| Ours 8B RSFT | LLM | 54.33 | 56.07 | -- | 81.26 |
| Ours 14B RSFT | LLM | 58.86 | 60.09 | 48.59 | 83.92 |

**Extraction gap:**
- Encoder vs. LLM: 16–18pp Ign-F1

---

### **Section 8: Decoupling Spectrum Data (lines 317-342)**

**Qwen3-4B:**

| Paradigm | Config | Rel-F1 | Evi-F1 | EDCR | Severity |
|----------|--------|--------|--------|------|----------|
| GRPO | QLoRA G=4 | 1.38 | 85.04 | 0.9876 | Catastrophic |
| GRPO | bf16 G=8 | 45.49 | 80.86 | 0.6318 | Mild |
| DPO | bf16 1ep | 33.37 | 80.90 | 0.8123 | Gradual |
| DPO | bf16 3ep | 31.45 | 84.84 | 0.7503 | Gradual |
| SFT | baseline | 44.39 | 79.61 | 0.6797 | None |
| RSFT | CED | 45.80 | 80.96 | 0.6487 | None |

---

### **Section 9: Error Analysis (lines 356-389)**

**Error pattern changes (relative change %):**

| Error Category | 1.7B | 4B | 8B/LLaMA |
|----------------|------|-----|---------|
| Truncation FN | −22% | −16% | −18% |
| Hallucinated FP | −8% | −6% | −12% |
| Duplicates | −20% | −11% | −14% |
| Evidence (exact) | <0.4pp | <0.4pp | <0.4pp |
| FN: other | +13% | +15% | +14% |

**LLaMA hallucinated reduction:**
- −593 FP
- −11.8% reduction

**1.7B truncation reduction:**
- −841 truncation FN
- −22% reduction

---

### **Section 10: Per-Relation EDCR Distribution (lines 392-408)**

**Per-relation EDCR correlation with Rel-F1:**
- ρ = −0.79 (n = 76 relation types, p < 0.001)
- ρ = −0.85 (n = 74 types with ≥5 predictions, p < 0.001)

**Per-relation EDCR vs. Evi-F1:**
- ρ = −0.06 (p = 0.58, statistically independent)

**Evi-F1 vs. Rel-F1:**
- ρ = −0.01 (p = 0.91, no association)

**Extreme relation types:**
- date_of_birth EDCR: 0.118 (highly faithful)
- head_of_government EDCR: 0.956 (highly decoupled)

**Partial correlations (controlling for TP):**
- Cross-method (n = 17): partial ρ = −0.8541 (p = 0.000025)
- Without GRPO outlier (n = 16): partial ρ = −0.8681 (p = 0.000027)
- Unique methods (n = 7): raw ρ = −0.9643, partial ρ = −0.9617

**Permutation test:**
- p < 0.0001 (10,000 iterations)

**Similar-TP, different-EDCR pairs:**
- 48 such pairs identified
- Most illustrative example difference: 13.6pp EDCR difference with only 2.4pp Evi-Recall_TP difference

**Per-relation analysis:**
- 76 relation types with ≥5 evaluation samples
- 93 relation types observed in dev set (of 96 defined)
- 7 types exhibit EDCR = 1.0

---

### **Section 11: Qualitative Analysis (lines 411-442)**

**Case 1 evidence precision comparison:**
- America's Sweetheart: SFT 0.17, RSFT 1.00 (SFT cites 6 sentences, RSFT cites 1)
- SFT evidence precision across examples: 0.00–0.20
- RSFT evidence precision across examples: 1.00

**Case 2 (GRPO catastrophic collapse):**
- Something to Believe In: 35 predicted triples, 0 correct (all non-ontology relations)
- József Piłsudski Monument: 28 predictions, 0 correct

**Case 3 per-relation diagnostics:**
- date_of_birth EDCR: 0.118
- notable_work EDCR: 0.941

---

## **Section Structure Summary**

1. Training Hyperparameters (1 table)
2. Full Ablation Results (1 table)
3. Scaling Details (2 tables + 1 figure reference)
4. Variance Compression Confidence Intervals (1 table)
5. Controlled Evaluation Subset (1 table)
6. Training-Time Evidence Tax (1 table)
7. Why RSFT Avoids Decoupling (theoretical section)
8. Full Generalization Results (4 tables + 1 figure reference)
9. Decoupling Spectrum Data (1 table + 1 figure reference)
10. GRPO Training Dynamics (1 figure reference)
11. Error Analysis: SFT vs. RSFT (1 table)
12. Per-Relation EDCR Distribution (1 table + 1 figure reference)
13. Qualitative Analysis (3 cases in text + 1 table)
14. Use of AI Assistants (text only)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbda2672-f050-4c23-8b4f-359ffc33f2be",
  "isSidechain": true,
  "agentId": "a6a8bef379c2ca3e1",
  "requestId": "req_011CbL38rJPgx1iXJEtaBHuV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "95197de1-fc53-49bf-8896-4abd6848c676",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "3296b1fc-f6e1-46f0-b410-51841c4ff218",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JFnFU6gzquGG53iv9JMZZf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 16260,
      "cache_read_input_tokens": 19413,
      "output_tokens": 6612,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16260
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 6612,
          "cache_read_input_tokens": 19413,
          "cache_creation_input_tokens": 16260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16260,
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
