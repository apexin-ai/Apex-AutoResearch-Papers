# Research conversation: In the paper directory at /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/, search

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9cc4d1362dafefa3.jsonl`
- **Structured JSON:** [`454036180ed0597fd5c7.json`](../../sessions/45/454036180ed0597fd5c7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-17T11:49:27.152Z_

In the paper directory at /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/, search for what baselines are cited and compared against experimentally. 

Specifically:
1. In experiments.tex, what methods appear in Table 2 (main results table) as baselines?
2. In related_work.tex, what methods are cited as most closely related (especially MaskLLM, DejaVu, CATS, PowerInfer, FastForward)?
3. In references.bib, search for: maskllm, dejavu, cats, powerinfer, fastforward, teal, wina, sparseInfer, svdcsp, d2dmoe
4. What downstream tasks are evaluated? (look for arc, winogrande, mmlu, gsm8k, hellaswag, piqa, boolq in experiments.tex and appendix.tex)

Report what baselines we compare against experimentally vs only cite, and what downstream tasks we cover vs commonly used ones we're missing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "83c10291-f9f7-46db-8cba-9066d7bf4990",
  "agentId": "a9cc4d1362dafefa3",
  "type": "user",
  "uuid": "be13c0dc-19b7-4b00-a7dd-1a71545d2983",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-17T11:49:28.839Z_

I'll help you search the paper directory for baseline methods, citations, and downstream tasks. Let me start by exploring the structure and searching the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be13c0dc-19b7-4b00-a7dd-1a71545d2983",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86AVjjzsnkX3EyPu6Qi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d5f4f3cc-cf27-456a-bd4d-f6febe3a4239",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Jwr2GfQg7aDtyZAiw9VKq7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35060,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 35060,
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

_source line 3 · 2026-05-17T11:49:28.984Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Pr8eo3FQcd2CUr8vPpt5Tb`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ -type f -name \"*.tex\" -o -name \"*.bib\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5f4f3cc-cf27-456a-bd4d-f6febe3a4239",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86AVjjzsnkX3EyPu6Qi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1a034545-2df7-48c9-95f0-8b3e7b3b68a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Jwr2GfQg7aDtyZAiw9VKq7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35060,
      "cache_read_input_tokens": 0,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 35060
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 139,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 35060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 35060,
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

_source line 4 · 2026-05-17T11:49:29.217Z_

<details><summary>↩ Tool result · `toolu_01Pr8eo3FQcd2CUr8vPpt5Tb`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a034545-2df7-48c9-95f0-8b3e7b3b68a7",
  "isSidechain": true,
  "promptId": "83c10291-f9f7-46db-8cba-9066d7bf4990",
  "agentId": "a9cc4d1362dafefa3",
  "type": "user",
  "uuid": "2dfb1e0f-311e-44c7-b597-2476a747e948",
  "sourceToolAssistantUUID": "1a034545-2df7-48c9-95f0-8b3e7b3b68a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-17T11:49:30.445Z_

Now let me search the key files for baselines and tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dfb1e0f-311e-44c7-b597-2476a747e948",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86AeRd1iPUyyrMFfMaa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8894e32d-9645-4117-8427-fe12a1785dd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0179eGZw5tK7QJVm1tJi7SKC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1395,
      "cache_read_input_tokens": 35060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1395,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-17T11:49:30.574Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SPLWQqeVF2UTr7pRGGhoQQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8894e32d-9645-4117-8427-fe12a1785dd2",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86AeRd1iPUyyrMFfMaa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c70ac07-1018-4326-a8cf-f4093a1ec54d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0179eGZw5tK7QJVm1tJi7SKC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1395,
      "cache_read_input_tokens": 35060,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1395
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 102,
          "cache_read_input_tokens": 35060,
          "cache_creation_input_tokens": 1395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1395,
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

_source line 7 · 2026-05-17T11:49:30.594Z_

<details><summary>↩ Tool result · `toolu_01SPLWQqeVF2UTr7pRGGhoQQ`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\S\ref{sec:scaling}).
28	At 30\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.98, reducing TEAL's degradation from dense (10.97 $\to$ 8.98, an 18\% improvement). % exp_id: kl_30_global_teal
29	Uniform allocation at 30\% recovers MMLU to 40.61\% (+15.3pp over KL-global's 25.27\%): global top-$k$ starves late layers (L31 retention 28.4\%) while uniform guarantees capacity in logit-forming layers (\S\ref{sec:scaling}). % exp_id: bench_kl30_uniform
30	
31	At 50\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\ 23.31, a 49\% reduction. % exp_id: bench_kl50_global, bench_teal50
32	The predictor also generalizes to held-out data (C4 validation: 52.5\% advantage over TEAL; see Appendix~\ref{app:ood}).
33	However, all methods exhibit downstream collapse on MMLU (27.89\% vs.\ 27.77\% for global vs.\ uniform, both $\approx$ random) and GSM8K ($<$2.2\%), indicating a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform
34	
35	\begin{table}[t]
36	\centering
37	\caption{Main results on LLaMA-3.1-8B. PPL$\downarrow$ on WikiText-2; accuracy$\uparrow$ on downstream tasks. \textbf{Bold}: best among compensation-free methods per sparsity level. BCE uses a different inference protocol: hard binary masks from the predictor with a learned compensation network (67.2M params) applied post-masking; no TEAL allocation. Results are single-seed except 50\% uniform (3-seed mean $\pm$ std: $11.92 \pm 0.07$; Appendix~\ref{app:stability}).}
38	\label{tab:main}
39	\resizebox{\columnwidth}{!}{
40	\begin{tabular}{llccccc}
41	\toprule
42	Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
43	\midrule
44	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
45	\midrule
46	\multirow{3}{*}{30\%}
47	& TEAL vanilla & 10.97 & \textbf{42.32} & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
48	& KL global (Ours) & 8.98 & 39.68 & \textbf{70.17} & 25.27 & \textbf{8.79} \\ % exp_id: lm_eval_kl_30pct_s42
49	& KL uniform & \textbf{8.82} & 40.78 & 68.59 & \textbf{40.61} & 7.35 \\ % exp_id: bench_kl30_uniform
50	\midrule
51	\multirow{4}{*}{50\%}
52	& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
53	& KL global (Ours) & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 27.89 & 1.29 \\ % exp_id: bench_kl50_global
54	& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \textbf{2.12} \\ % exp_id: d030_kl50_uniform
55	& BCE (2700 steps)$^\ast$ & 27.97 & 23.98 & 50.59 & 30.02 & 4.85 \\ % exp_id: eval_bce_v3_s42
56	\bottomrule
57	\end{tabular}}
58	\end{table}
59	
60	
61	\subsection{Extended Training Analysis}
62	\label{sec:isocompute}
63	
64	To test whether BCE simply requires more compute, we train it for 2700 steps (2.71$\times$ the KL step budget, approximately equal wall-clock time: $\sim$46 min BCE vs.\ $\sim$45 min KL on RTX PRO 6000).
65	The BCE predictor achieves PPL 27.97, still 2.37$\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce_isocompute_s42
66	The failure is structural, not due to architectural or compute differences: both predictors use identical architectures and TEAL allocation, yet BCE achieves +7pp oracle F1 (0.613 vs.\ 0.540) with 137\% worse PPL (27.97 vs.\ 11.79). KL's near-random precision (0.51) confirms it learns a mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42
67	Future work could further isolate coupling effects through MSE on hidden states and per-layer KL ablations.
68	
69	
70	\subsection{Ablation Studies}
71	
72	Table~\ref{tab:ablation} isolates the contribution of each design choice at 50\% sparsity.
73	
74	\begin{table}[t]
75	\centering
76	\caption{Ablation at 50\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$, unified benchmark protocol).}
77	\label{tab:ablation}
78	\small
79	\begin{tabular}{lcc}
80	\toprule
81	Configuration & PPL$\downarrow$ & $\Delta$ from Ours \\
82	\midrule
83	\multicolumn{3}{l}{\textit{KL-based variants}} \\
84	Forward KL + Gumbel (Ours) & \textbf{11.79} & --- \\ % exp_id: bench_kl50_global
85	JSD (symmetric) + Gumbel & 12.54 & +0.75 \\ % exp_id: jsd_ablation_s42
86	Reverse KL + Gumbel & 12.80 & +1.01 \\ % exp_id: reverse_kl_ablation_s42
87	Forward KL + STE & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
88	\midrule
89	\multicolumn{3}{l}{\textit{BCE-based variants}} \\
90	BCE + Compensation (hard mask) & 25.44 & +13.65 \\ % exp_id: bce_comp_staged_s42
91	BCE (no compensation) & 27.97 & +16.18 \\ % exp_id: eval_bce_v3_s42
92	BCE + Gumbel + Penalty (no KL) & 38.02 & +26.23 \\ % exp_id: bce_gumbel_lagrangian_isolation
93	\bottomrule
94	\end{tabular}
95	\end{table}
96	
97	\paragraph{Gumbel vs.\ STE.}
98	Replacing Gumbel-Sigmoid with STE~\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98), accounting for 34.5\% of the improvement over vanilla TEAL. % exp_id: ste_baseline_s42
99	
100	\paragraph{Divergence Direction.}
101	Forward KL (mode-covering) outperforms JSD (+6.4\%) and reverse KL (+8.6\%), consistent with the SNR analysis in \S\ref{sec:method:gradient}: complete teacher supervision enables better global allocation learning. % exp_id: jsd_ablation_s42, reverse_kl_ablation_s42
102	This contrasts with MiniLLM~\cite{gu2024minillm}, which finds reverse KL superior for sequence-level distillation: in generation, mode-seeking prevents low-probability token production, while in mask prediction, mode-covering (forward KL) ensures no important neuron is omitted ($q(x) \approx 0$ where $p(x) > 0$ is directly penalized).
103	
104	\paragraph{SPON Contribution.}
105	Adding SPON~\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79 (2.4\% relative); see \S\ref{sec:spon} for decomposition.\footnote{SPON analysis uses \texttt{evaluate.py}; main results use the unified benchmark.} % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42
106	
107	\paragraph{Loss Function Isolation.}
108	BCE with identical Gumbel-Sigmoid and penalty yields PPL 38.02, worse than vanilla BCE (27.97): the penalty interferes with per-neuron optimization without global coordination. % exp_id: bce_gumbel_lagrangian_isolation
109	The loss effect ($\Delta$PPL=26.23) is $6.6\times$ the relaxation effect ($\Delta$PPL=3.98).
110	
111	\paragraph{BCE + Compensation.}
112	Compensation improves BCE from 27.97 to 25.44 (9.0\%), still $2.16\times$ worse than KL. % exp_id: bce_comp_staged_s42
113	
114	\paragraph{Hyperparameter Robustness.}
115	Appendix~\ref{app:db_sensitivity} confirms robustness to predictor capacity ($d_b$, $<$3\%), temperature ($<$1.8\%), and training steps (saturated by 800). % exp_id: db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep
116	
117	
118	\subsection{Sparsity Scaling and Regime Analysis}
119	\label{sec:scaling}
120	
121	Table~\ref{tab:scaling} and Figure~\ref{fig:sparsity_sweep} show PPL as a function of sparsity for the KL predictor under global allocation and vanilla TEAL.
122	
123	\begin{figure}[t]
124	\centering
125	\includegraphics[width=\columnwidth]{fig2_sparsity_sweep.pdf}
126	\caption{Perplexity scaling with sparsity. The KL predictor's advantage grows disproportionately as more neurons are pruned.}
127	\label{fig:sparsity_sweep}
128	\end{figure}
129	
130	\begin{table}[t]
131	\centering
132	\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows disproportionately with sparsity.}
133	\label{tab:scaling}
134	\small
135	\begin{tabular}{lccc}
136	\toprule
137	Sparsity & KL (Ours) & TEAL vanilla & Relative advantage \\
138	\midrule
139	30\% & \textbf{8.98} & 10.97 & 18\% \\ % exp_id: kl_30_global_teal
140	50\% & \textbf{11.79} & 23.31 & 49\% \\ % exp_id: bench_kl50_global
141	70\% & \textbf{17.91} & 100.11 & 82\% \\ % exp_id: kl_70_global_teal
142	\bottomrule
143	\end{tabular}
144	\end{table}
145	
146	The KL advantage grows from 18\% at 30\% to 82\% at 70\%, where TEAL collapses (PPL 100.11) while the learned predictor maintains coherent allocation.
147	In absolute terms, KL/Dense degradation is $1.47\times$ at 30\%, $1.93\times$ at 50\%, and $2.93\times$ at 70\%, compared to TEAL/Dense ratios of $1.79\times$, $3.81\times$, and $16.4\times$ respectively.
148	
149	\paragraph{Three Operating Regions.}
150	Table~\ref{tab:phase} presents global vs.\ uniform allocation at three sparsity levels, revealing qualitative shifts in allocation preference. Denser sampling (e.g., 35\% sparsity) would be needed to precisely locate region boundaries.
151	
152	\begin{table}[t]
153	\centering
154	\caption{Allocation analysis: global (TEAL) vs.\ uniform per-layer allocation across sparsity levels. \textbf{Bold}: best per column within each sparsity group (compensation-free). Each row uses a predictor trained at the respective sparsity target.}
155	\label{tab:phase}
156	\resizebox{\columnwidth}{!}{
157	\begin{tabular}{llccccc}
158	\toprule
159	Sparsity & Allocation & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
160	\midrule
161	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
162	\midrule
163	\multirow{3}{*}{30\%}
164	& TEAL vanilla & 10.97 & \textbf{42.32} & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
165	& KL global & 8.98 & 39.68 & \textbf{70.17} & 25.27 & \textbf{8.79} \\ % exp_id: lm_eval_kl_30pct_s42
166	& KL uniform & \textbf{8.82} & 40.78 & 68.59 & \textbf{40.61} & 7.35 \\ % exp_id: bench_kl30_uniform
167	\midrule
168	\multirow{2}{*}{40\%}
169	& KL global & 10.12 & 40.96 & 65.35 & \textbf{38.06} & \textbf{5.00} \\ % exp_id: bench_kl40_global
170	& KL uniform & \textbf{8.36} & \textbf{41.81} & \textbf{67.17} & 30.68 & 3.94 \\ % exp_id: d030_kl40_uniform
171	\midrule
172	\multirow{3}{*}{50\%}
173	& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
174	& KL global & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 27.89 & 1.29 \\ % exp_id: bench_kl50_global
175	& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \textbf{2.12} \\ % exp_id: d030_kl50_uniform
176	\bottomrule
177	\end{tabular}}
178	\end{table}
179	
180	The allocation preference is \emph{non-monotonic}. We observe three qualitative behaviors at the sampled sparsity levels (7--8B scale):
181	
182	\noindent\textbf{Budget-surplus ($\leq$30\%).}
183	Uniform allocation recovers MMLU from 25.27\% to 40.61\% (+15.3pp), comparable to TEAL's 38.61\%, confirming degradation is attributable to allocation strategy rather than KL training. Global top-$k$ starves late layers (L31: 28.4\%, std/mean$=$1.89) which siphon disproportionate budget from logit-forming layers. Note: the adaptive controller achieves 28.5\% actual sparsity at the 30\% target (5\% deviation; Appendix~\ref{app:lagrangian}). % exp_id: bench_kl30_uniform, lm_eval_kl_30pct_s42, bench_teal30
184	
185	\noindent\textbf{Budget-constrained ($\sim$40\%).}
186	The preference reverses: global achieves MMLU 38.06\% vs.\ uniform's 30.68\% (+7.4pp). % exp_id: bench_kl40_global, d030_kl40_uniform
187	PPL remains low (8.36) but downstream accuracy degrades, confirming PPL is a poor proxy for reasoning.
188	
189	\noindent\textbf{Capacity-limited ($\geq$50\%).}
190	Global/uniform gap vanishes (MMLU 27.89\% vs.\ 27.77\%, both $\approx$ random). % exp_id: bench_kl50_global, d030_kl50_uniform
191	Late-layer starvation persists across levels (L24--31 mean retention: 50.1\% at 30\%, 34.2\% at 50\%, 22.6\% at 70\%; Figure~\ref{fig:retention}); this boundary is consistent on both 7--8B models (\S\ref{sec:cross_arch}).
192	
193	\paragraph{Gap Decomposition.}
194	Decomposing the Dense$\to$KL gap under uniform allocation (5.85 PPL): per-token hard mask evaluation (Appendix~\ref{app:db_sensitivity}, Table~\ref{tab:db_sensitivity}) yields PPL 9.22, attributing 53\% of the degradation to predictor approximation (including soft-to-hard discretization) and 47\% to per-layer budget allocation. % exp_id: db_sensitivity_sweep, bench_kl50_uniform
195	Even under global allocation, the learned predictor (11.79) remains $1.98\times$ better than TEAL's magnitude oracle (23.31), confirming that distributional training captures neuron interactions that magnitude scoring misses.
196	
197	
198	\subsection{SPON Orthogonality Analysis}
199	\label{sec:spon}
200	
201	At 50\% sparsity, the predictor's hidden-state perturbation (L2=482.65) and SPON's additive correction (L2=76.2, cosine similarity 0.196) are weakly correlated ($R^2$=0.038); SPON yields only 2.4\% PPL improvement (12.08$\to$11.79), confirming the KL predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42
202	
203	\paragraph{Cross-Architecture Validation.}
204	\label{sec:cross_arch}
205	Table~\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).
206	
207	\begin{table}[t]
208	\centering
209	\caption{Cross-architecture comparison (WikiText-2 PPL$\downarrow$). Adv = TEAL\,/\,KL ratio. LLaMA uses global top-$k$; Mistral uses uniform allocation (matched within each architecture).}
210	\label{tab:cross_arch}
211	\small
212	\begin{tabular}{l@{\hspace{4pt}}cc@{\hspace{3pt}}c@{\hspace{6pt}}|@{\hspace{6pt}}cc@{\hspace{3pt}}c}
213	\toprule
214	 & \multicolumn{3}{c}{Mistral-7B} & \multicolumn{3}{c}{LLaMA-8B} \\
215	 & KL & TEAL & Adv & KL & TEAL & Adv \\
216	\midrule
217	30\% & \textbf{6.77} & 8.38 & 1.24$\times$ & \textbf{8.98} & 10.97 & 1.22$\times$ \\ % exp_id: kl_30_mistral, teal_30_mistral
218	50\% & \textbf{8.65} & 18.31 & 2.12$\times$ & \textbf{11.79} & 23.31 & 1.98$\times$ \\ % exp_id: kl_50_mistral, teal_50_mistral
219	70\% & \textbf{13.33} & 61.72 & 4.63$\times$ & \textbf{17.91} & 100.11 & 5.59$\times$ \\ % exp_id: kl_70_mistral, teal_70_mistral
220	\bottomrule
221	\end{tabular}
222	\end{table}
223	
224	The KL advantage ratio (computed within each architecture under matched allocation) is consistent across architectures (within 8\% at $\leq$50\% sparsity), with larger variance at 70\% (4.63$\times$ vs.\ 5.59$\times$) due to differential baseline collapse.
225	Consistent ratios despite Mistral's stronger TEAL baseline (gate distribution favors magnitude pruning) provide preliminary evidence of generality across SwiGLU architectures at the 7--8B scale.
226	
227	
228	\paragraph{Inference Efficiency.}
229	The pipeline adds 6.4\% overhead to dense inference (RTX PRO 6000 Blackwell) while removing the compensation network ($-$2.7\% latency, $-$67.2M params); post-hoc SPON yields $<$3\% additional gain (\S\ref{sec:spon}), suggesting the predictor already internalizes most error-correction signal (Appendix~\ref{app:latency}).
230	
231	\paragraph{Training Stability.}
232	Three-seed evaluation (50\% uniform): PPL $11.92 \pm 0.07$ (CV$<$1\%); see Appendix~\ref{app:stability}.
233	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c70ac07-1018-4326-a8cf-f4093a1ec54d",
  "isSidechain": true,
  "promptId": "83c10291-f9f7-46db-8cba-9066d7bf4990",
  "agentId": "a9cc4d1362dafefa3",
  "type": "user",
  "uuid": "d4b05706-4d42-4685-9d64-18f94c240e02",
  "sourceToolAssistantUUID": "4c70ac07-1018-4326-a8cf-f4093a1ec54d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-17T11:49:31.812Z_

Now let me search the related_work.tex file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4b05706-4d42-4685-9d64-18f94c240e02",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86AkLKpokZVAVojx38q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8c00afa0-04e6-4e60-b426-23ab0a99b6fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H4rkZpjbF52RghkSzLX8fM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6884,
      "cache_read_input_tokens": 36455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6884,
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

_source line 9 · 2026-05-17T11:49:32.473Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AiZwpjNPz7kMzVM21KWR6d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c00afa0-04e6-4e60-b426-23ab0a99b6fa",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86AkLKpokZVAVojx38q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8adabf96-2d47-48d4-97b7-46f68a508719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H4rkZpjbF52RghkSzLX8fM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6884,
      "cache_read_input_tokens": 36455,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6884
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 103,
          "cache_read_input_tokens": 36455,
          "cache_creation_input_tokens": 6884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6884,
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

_source line 10 · 2026-05-17T11:49:32.535Z_

<details><summary>↩ Tool result · `toolu_01AiZwpjNPz7kMzVM21KWR6d`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude, achieving 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision, providing intermediate coupling within each layer but no end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
13	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
14	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
15	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint.
16	The structural mismatch we characterize (per-neuron gradient decomposition vs.\ global top-$k$) does not arise in MaskLLM's per-group categorical setting, where N:M patterns eliminate cross-group budget competition.
17	All prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
18	Our contribution is primarily empirical: we observe that a coupled KL objective propagates gradients through all downstream layers and quantify when this matters for global allocation quality.
19	
20	\paragraph{Static Bias Correction.}
21	SPON~\cite{xu2026spon} learns input-independent bias vectors via closed-form KL minimization per layer, absorbed into weights at deployment.
22	Our method is fundamentally different: a per-token contextual predictor trained end-to-end across all layers, producing input-dependent masks.
23	SPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are weakly correlated (cosine similarity 0.196, $R^2$=0.038; \S\ref{sec:experiments}).
24	
25	\paragraph{Activation Function Engineering.}
26	ReLU Strikes Back~\cite{mirzadeh2024relu} replaces SiLU with ReLU for $>$90\% natural sparsity; TurboSparse~\cite{song2024turbosparse} and ProSparse~\cite{song2025prosparse} engineer extreme sparsity through activation modifications; the Sparsing Law~\cite{luo2024sparsinglaw} formalizes how activation density increases with training compute.
27	MiniTron~\cite{muralidharan2024minitron} combines structured pruning with distillation but modifies architecture permanently.
28	All require retraining or weight modification; our method is a plug-in predictor on \emph{unmodified} SwiGLU models.
29	
30	\paragraph{Weight Pruning, Distillation, and Routing.}
31	Wanda~\cite{sun2024wanda} and SparseGPT~\cite{frantar2023sparsegpt} produce static weight masks; Switch Transformers~\cite{fedus2022switch} and Mixture-of-Depths~\cite{raposo2024mod} achieve conditional computation through learned routing.
32	KL-based distillation~\cite{kim2016sequencekd,sanh2019distilbert,gu2024minillm,agarwal2024gkd} trains compact students; SparseLoRA~\cite{khaki2025sparselora} exploits contextual sparsity for fine-tuning.
33	We apply the KL principle to train a sparsity predictor on unmodified dense models, using Gumbel-Sigmoid sampling~\cite{maddison2017concrete,louizos2018l0} for differentiable discrete mask optimization.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8adabf96-2d47-48d4-97b7-46f68a508719",
  "isSidechain": true,
  "promptId": "83c10291-f9f7-46db-8cba-9066d7bf4990",
  "agentId": "a9cc4d1362dafefa3",
  "type": "user",
  "uuid": "172d4887-1b8a-47f8-8b5a-4e1fa5d547ba",
  "sourceToolAssistantUUID": "8adabf96-2d47-48d4-97b7-46f68a508719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-17T11:49:33.932Z_

Now let me search the references.bib file for the specific methods:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "172d4887-1b8a-47f8-8b5a-4e1fa5d547ba",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86AtvFtmB68BiarQk6i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "327d8209-8007-467f-bb27-7878b38b62e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MoqzgPii1LTvRcgUyKif1i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 43339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1427,
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

_source line 12 · 2026-05-17T11:49:34.611Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W77ETCouP3q7HHRmf5XsaS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "327d8209-8007-467f-bb27-7878b38b62e0",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86AtvFtmB68BiarQk6i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c54c7437-6d53-47de-9e54-1ccd7b221768",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MoqzgPii1LTvRcgUyKif1i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 43339,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1427
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 105,
          "cache_read_input_tokens": 43339,
          "cache_creation_input_tokens": 1427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1427,
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

_source line 13 · 2026-05-17T11:49:34.633Z_

<details><summary>↩ Tool result · `toolu_01W77ETCouP3q7HHRmf5XsaS`</summary>

```text
1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Narasimha Reddy},
37	  year = {2026},
38	  journal = {arXiv preprint arXiv:2602.00397},
39	  url = {https://arxiv.org/abs/2602.00397},
40	}
41	
42	
43	% =============================================================================
44	% Direction 4: Predictor-based activation sparsity
45	% =============================================================================
46	
47	@inproceedings{liu2025teal,
48	  title = {Training-Free Activation Sparsity in Large Language Models},
49	  author = {James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben Athiwaratkun},
50	  year = {2025},
51	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
52	  url = {https://arxiv.org/abs/2408.14690},
53	}
54	
55	@inproceedings{liu2023dejavu,
56	  title = {Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time},
57	  author = {Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao Song and Anshumali Shrivastava and Ce Zhang and Yuandong Tian and Christopher Re and Beidi Chen},
58	  year = {2023},
59	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
60	  url = {https://arxiv.org/abs/2310.17157},
61	}
62	
63	@inproceedings{akhauri2024shadowllm,
64	  title = {ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models},
65	  author = {Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Alexander M Rush and Safeen Huda and Mohamed S Abdelfattah},
66	  year = {2024},
67	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
68	  url = {https://arxiv.org/abs/2406.16635},
69	}
70	
71	
72	@article{lee2024cats,
73	  title = {CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},
74	  author = {Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhoseini},
75	  year = {2024},
76	  journal = {arXiv preprint arXiv:2404.08763},
77	  url = {https://arxiv.org/abs/2404.08763},
78	}
79	
80	@inproceedings{zhang2025rsparse,
81	  title = {R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference},
82	  author = {Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang Wang and Steven Li},
83	  year = {2025},
84	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
85	  url = {https://arxiv.org/abs/2504.19449},
86	}
87	
88	@inproceedings{federici2025dip,
89	  title = {Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking},
90	  author = {Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andrii Skliar and Bence Major and Markus Nagel and Paul Whatmough},
91	  year = {2024},
92	  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},
93	  url = {https://arxiv.org/abs/2412.01380},
94	}
95	
96	@inproceedings{shin2025sparseinfer,
97	  title = {SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference},
98	  author = {Jiho Shin and Hoeseok Yang and Youngmin Yi},
99	  year = {2025},
100	  booktitle = {Proceedings of the Design, Automation \& Test in Europe Conference (DATE)},
101	  url = {https://arxiv.org/abs/2411.12692},
102	}
103	
104	@article{serbin2026svdcsp,
105	  title = {SVD Contextual Sparsity Predictors for Fast LLM Inference},
106	  author = {Georgii Serbin and Kirill Koshkin and Zhongao Sun and Anastasiya Bistrigova and C.C. Korikov},
107	  year = {2026},
108	  journal = {arXiv preprint arXiv:2603.14110},
109	  url = {https://arxiv.org/abs/2603.14110},
110	}
111	
112	% =============================================================================
113	% Activation function replacement and sparsity enhancement
114	% =============================================================================
115	
116	@inproceedings{mirzadeh2024relu,
117	  title = {ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models},
118	  author = {Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Oncel Tuzel and Golnoosh Samei and Mohammad Rastegari and Mehrdad Farajtabar},
119	  year = {2024},
120	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
121	  url = {https://arxiv.org/abs/2310.04564},
122	}
123	
124	@article{song2024turbosparse,
125	  title = {Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters},
126	  author = {Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi and Haibo Chen},
127	  year = {2024},
128	  journal = {arXiv preprint arXiv:2406.05955},
129	  url = {https://arxiv.org/abs/2406.05955},
130	}
131	
132	@inproceedings{song2025prosparse,
133	  title = {ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models},
134	  author = {Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Kuai Li and Chen Chen and Zhiyuan Liu and Guangli Li and Tao Yang and Maosong Sun},
135	  year = {2025},
136	  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},
137	  url = {https://arxiv.org/abs/2402.13516},
138	}
139	
140	@article{luo2024sparsinglaw,
141	  title = {Sparsing Law: Towards Large Language Models with Greater Activation Sparsity},
142	  author = {Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaojun Meng and Liqun Deng and Jiansheng Wei and Zhiyuan Liu and Maosong Sun},
143	  year = {2024},
144	  journal = {arXiv preprint arXiv:2411.02335},
145	  url = {https://arxiv.org/abs/2411.02335},
146	}
147	
148	
149	@inproceedings{song2024powerinfer,
150	  title = {PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU},
151	  author = {Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen},
152	  year = {2024},
153	  booktitle = {Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)},
154	  url = {https://arxiv.org/abs/2312.12456},
155	}
156	
157	
158	% =============================================================================
159	% KL distillation and knowledge distillation
160	% =============================================================================
161	
162	@inproceedings{kim2016sequencekd,
163	  title = {Sequence-Level Knowledge Distillation},
164	  author = {Yoon Kim and Alexander M. Rush},
165	  year = {2016},
166	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
167	  url = {https://arxiv.org/abs/1606.07947},
168	}
169	
170	@inproceedings{gu2024minillm,
171	  title = {MiniLLM: Knowledge Distillation of Large Language Models},
172	  author = {Yuxian Gu and Li Dong and Furu Wei and Minlie Huang},
173	  year = {2024},
174	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
175	  url = {https://openreview.net/forum?id=5h0qf7IBZZ},
176	}
177	
178	@inproceedings{agarwal2024gkd,
179	  title = {On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes},
180	  author = {Rishabh Agarwal and Nino Vieillard and Yongchao Zhou and Piotr Stanczyk and Sabela Ramos and Matthieu Geist and Olivier Bachem},
181	  year = {2024},
182	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
183	  url = {https://openreview.net/forum?id=3zKtaqxLhW},
184	}
185	
186	@inproceedings{khaki2025sparselora,
187	  title = {SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity},
188	  author = {Samir Khaki and Xiuyu Li and Junxian Guo and Ligeng Zhu and Konstantinos N. Plataniotis and Amir Yazdanbakhsh and Kurt Keutzer and Song Han and Zhijian Liu},
189	  year = {2025},
190	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
191	  url = {https://proceedings.mlr.press/v267/khaki25a.html},
192	}
193	
194	@article{raposo2024mod,
195	  title = {Mixture-of-Depths: Dynamically allocating compute in transformer-based language models},
196	  author = {David Raposo and Sam Ritter and Blake Richards and Timothy Lillicrap and Peter Conway Humphreys and Adam Santoro},
197	  year = {2024},
198	  journal = {arXiv preprint arXiv:2404.02258},
199	  url = {https://arxiv.org/abs/2404.02258},
200	}
201	
202	@article{sanh2019distilbert,
203	  title = {DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
204	  author = {Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},
205	  year = {2019},
206	  journal = {arXiv preprint arXiv:1910.01108},
207	  url = {https://arxiv.org/abs/1910.01108},
208	}
209	
210	% =============================================================================
211	% Weight pruning methods
212	% =============================================================================
213	
214	@inproceedings{sun2024wanda,
215	  title = {A Simple and Effective Pruning Approach for Large Language Models},
216	  author = {Mingjie Sun and Zhuang Liu and Anna Bair and J. Zico Kolter},
217	  year = {2024},
218	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
219	  url = {https://arxiv.org/abs/2306.11695},
220	}
221	
222	@inproceedings{frantar2023sparsegpt,
223	  title = {SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot},
224	  author = {Elias Frantar and Dan Alistarh},
225	  year = {2023},
226	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
227	  url = {https://arxiv.org/abs/2301.00774},
228	}
229	
230	% =============================================================================
231	% Conditional computation and MoE
232	% =============================================================================
233	
234	@inproceedings{szatkowski2024d2dmoe,
235	  title = {Exploiting Activation Sparsity with Dense to Dynamic-$k$ Mixture-of-Experts Conversion},
236	  author = {Filip Szatkowski and Bartosz W{\'o}jcik and Miko{\l}aj Pi{\'o}rczy{\'n}ski and Simone Scardapane},
237	  year = {2024},
238	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
239	  volume = {37},
240	  url = {https://arxiv.org/abs/2310.04361},
241	}
242	
243	@article{fedus2022switch,
244	  title = {Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity},
245	  author = {William Fedus and Barret Zoph and Noam Shazeer},
246	  year = {2022},
247	  journal = {Journal of Machine Learning Research},
248	  volume = {23},
249	  number = {120},
250	  pages = {1--40},
251	  url = {https://arxiv.org/abs/2101.03961},
252	}
253	
254	% =============================================================================
255	% Relaxation methods (Gumbel/Concrete)
256	% =============================================================================
257	
258	@inproceedings{louizos2018l0,
259	  title = {Learning Sparse Neural Networks through $L_0$ Regularization},
260	  author = {Christos Louizos and Max Welling and Diederik P. Kingma},
261	  year = {2018},
262	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
263	  url = {https://arxiv.org/abs/1712.01312},
264	}
265	
266	@inproceedings{maddison2017concrete,
267	  title = {The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables},
268	  author = {Chris J. Maddison and Andriy Mnih and Yee Whye Teh},
269	  year = {2017},
270	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
271	  url = {https://arxiv.org/abs/1611.00712},
272	}
273	
274	% =============================================================================
275	% Foundational references
276	% =============================================================================
277	
278	@article{grattafiori2024llama3,
279	  title = {The Llama 3 Herd of Models},
280	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aieleen Lakber and Aimin Chen and Ait Mokhtar Salma and Ajay Menon},
281	  year = {2024},
282	  journal = {arXiv preprint arXiv:2407.21783},
283	  url = {https://arxiv.org/abs/2407.21783},
284	}
285	
286	@article{jiang2023mistral,
287	  title = {Mistral 7B},
288	  author = {Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Florian Bressand and Gianna Lengyel and Guillaume Lample and Lucile Saulnier},
289	  year = {2023},
290	  journal = {arXiv preprint arXiv:2310.06825},
291	  url = {https://arxiv.org/abs/2310.06825},
292	}
293	
294	@inproceedings{jang2017gumbel,
295	  title = {Categorical Reparameterization with Gumbel-Softmax},
296	  author = {Eric Jang and Shixiang Gu and Ben Poole},
297	  year = {2017},
298	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
299	  url = {https://arxiv.org/abs/1611.01144},
300	}
301	
302	@article{shazeer2020glu,
303	  title = {GLU Variants Improve Transformer},
304	  author = {Noam Shazeer},
305	  year = {2020},
306	  journal = {arXiv preprint arXiv:2002.05202},
307	  url = {https://arxiv.org/abs/2002.05202},
308	}
309	
310	@inproceedings{merity2017pointer,
311	  title = {Pointer Sentinel Mixture Models},
312	  author = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},
313	  year = {2017},
314	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
315	  url = {https://arxiv.org/abs/1609.07843},
316	}
317	
318	@inproceedings{hinton2015distilling,
319	  title = {Distilling the Knowledge in a Neural Network},
320	  author = {Geoffrey Hinton and Oriol Vinyals and Jeff Dean},
321	  year = {2015},
322	  booktitle = {NeurIPS 2014 Deep Learning Workshop},
323	  url = {https://arxiv.org/abs/1503.02531},
324	}
325	
326	@article{bengio2013ste,
327	  title = {Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation},
328	  author = {Yoshua Bengio and Nicholas L\'{e}onard and Aaron Courville},
329	  year = {2013},
330	  journal = {arXiv preprint arXiv:1308.3432},
331	  url = {https://arxiv.org/abs/1308.3432},
332	}
333	
334	@inproceedings{loshchilov2019adamw,
335	  title = {Decoupled Weight Decay Regularization},
336	  author = {Ilya Loshchilov and Frank Hutter},
337	  year = {2019},
338	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
339	  url = {https://arxiv.org/abs/1711.05101},
340	}
341	
342	@article{raffel2020c4,
343	  title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
344	  author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},
345	  year = {2020},
346	  journal = {Journal of Machine Learning Research},
347	  volume = {21},
348	  number = {140},
349	  pages = {1--67},
350	  url = {https://arxiv.org/abs/1910.10683},
351	}
352	
353	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c54c7437-6d53-47de-9e54-1ccd7b221768",
  "isSidechain": true,
  "promptId": "83c10291-f9f7-46db-8cba-9066d7bf4990",
  "agentId": "a9cc4d1362dafefa3",
  "type": "user",
  "uuid": "6853de19-75f3-4e31-8fa0-68f83d6f5881",
  "sourceToolAssistantUUID": "c54c7437-6d53-47de-9e54-1ccd7b221768",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-17T11:49:35.911Z_

Now let me check the appendix for additional downstream tasks:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6853de19-75f3-4e31-8fa0-68f83d6f5881",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86B3kpiW4UVQqXKeGnT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "56d339ab-a55f-4fa3-89b5-419f2bf16981",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KzrDoDcDhzBzQtx9Ma7L4p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6157,
      "cache_read_input_tokens": 44766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6157,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 15 · 2026-05-17T11:49:37.061Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01A2KqhuMMTKjmDyTZ8mxas4`</summary>

```json
{
  "command": "grep -i -E \"(arc|winogrande|mmlu|gsm8k|hellaswag|piqa|boolq)\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56d339ab-a55f-4fa3-89b5-419f2bf16981",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86B3kpiW4UVQqXKeGnT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "814df0af-849d-4c77-bf5d-7c3af376970c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KzrDoDcDhzBzQtx9Ma7L4p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6157,
      "cache_read_input_tokens": 44766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6157,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 16 · 2026-05-17T11:49:37.132Z_

<details><summary>↩ Tool result · `toolu_01A2KqhuMMTKjmDyTZ8mxas4`</summary>

```text
Downstream metrics are similarly stable: ARC-c $33.8 \pm 1.2$\%, WinoGrande $62.9 \pm 0.1$\%, MMLU $28.0 \pm 0.6$\%, GSM8K $2.2 \pm 0.1$\%.
The low variance indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "814df0af-849d-4c77-bf5d-7c3af376970c",
  "isSidechain": true,
  "promptId": "83c10291-f9f7-46db-8cba-9066d7bf4990",
  "agentId": "a9cc4d1362dafefa3",
  "type": "user",
  "uuid": "77b8c9fb-c832-45f4-bfc2-c2248a6d539f",
  "sourceToolAssistantUUID": "814df0af-849d-4c77-bf5d-7c3af376970c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T11:49:39.106Z_

Let me search for more details about what tasks are evaluated:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77b8c9fb-c832-45f4-bfc2-c2248a6d539f",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86BEYxYqTPc5kZpAjDu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ae080e8-ea9d-4015-b540-6e6a26530905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N58CQJHJPxH1SeDGabpWi2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 50923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 258,
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

_source line 18 · 2026-05-17T11:49:39.626Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JMn2LJospw3WBbFsc19kaX`</summary>

```json
{
  "command": "grep -i \"downstream\\|task\\|benchmark\\|evaluation\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex | head -15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ae080e8-ea9d-4015-b540-6e6a26530905",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86BEYxYqTPc5kZpAjDu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "93d1ccb0-daa4-4b4a-9cca-a2b2586e5e6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N58CQJHJPxH1SeDGabpWi2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 50923,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 258
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 119,
          "cache_read_input_tokens": 50923,
          "cache_creation_input_tokens": 258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 258,
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

_source line 19 · 2026-05-17T11:49:39.742Z_

<details><summary>↩ Tool result · `toolu_01JMn2LJospw3WBbFsc19kaX`</summary>

```text
\paragraph{Evaluation.}
We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
Table~\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\S\ref{sec:scaling}).
However, all methods exhibit downstream collapse on MMLU (27.89\% vs.\ 27.77\% for global vs.\ uniform, both $\approx$ random) and GSM8K ($<$2.2\%), indicating a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform
\caption{Main results on LLaMA-3.1-8B. PPL$\downarrow$ on WikiText-2; accuracy$\uparrow$ on downstream tasks. \textbf{Bold}: best among compensation-free methods per sparsity level. BCE uses a different inference protocol: hard binary masks from the predictor with a learned compensation network (67.2M params) applied post-masking; no TEAL allocation. Results are single-seed except 50\% uniform (3-seed mean $\pm$ std: $11.92 \pm 0.07$; Appendix~\ref{app:stability}).}
\caption{Ablation at 50\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$, unified benchmark protocol).}
Adding SPON~\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79 (2.4\% relative); see \S\ref{sec:spon} for decomposition.\footnote{SPON analysis uses \texttt{evaluate.py}; main results use the unified benchmark.} % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42
PPL remains low (8.36) but downstream accuracy degrades, confirming PPL is a poor proxy for reasoning.
Decomposing the Dense$\to$KL gap under uniform allocation (5.85 PPL): per-token hard mask evaluation (Appendix~\ref{app:db_sensitivity}, Table~\ref{tab:db_sensitivity}) yields PPL 9.22, attributing 53\% of the degradation to predictor approximation (including soft-to-hard discretization) and 47\% to per-layer budget allocation. % exp_id: db_sensitivity_sweep, bench_kl50_uniform
Three-seed evaluation (50\% uniform): PPL $11.92 \pm 0.07$ (CV$<$1\%); see Appendix~\ref{app:stability}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93d1ccb0-daa4-4b4a-9cca-a2b2586e5e6c",
  "isSidechain": true,
  "promptId": "83c10291-f9f7-46db-8cba-9066d7bf4990",
  "agentId": "a9cc4d1362dafefa3",
  "type": "user",
  "uuid": "b5f18eff-9611-4933-8440-3c69ab571e8b",
  "sourceToolAssistantUUID": "93d1ccb0-daa4-4b4a-9cca-a2b2586e5e6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-17T11:49:40.692Z_

Let me also check the appendix more comprehensively:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5f18eff-9611-4933-8440-3c69ab571e8b",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86BRVXTuAHDdfYjNj3L",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "58a9d547-a368-471a-bbc3-5cafeba5ad46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0152wsRtmNrBWHN81B2cQLVA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 51181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 840,
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

_source line 21 · 2026-05-17T11:49:41.195Z_

<details open><summary>🔧 Tool call — Read · `toolu_011jr3XtCUT5KdjEToU3TgCj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58a9d547-a368-471a-bbc3-5cafeba5ad46",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86BRVXTuAHDdfYjNj3L",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "71a6195e-3006-4903-8af8-b6a297f74340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0152wsRtmNrBWHN81B2cQLVA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 51181,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 840
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 119,
          "cache_read_input_tokens": 51181,
          "cache_creation_input_tokens": 840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 840,
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

_source line 22 · 2026-05-17T11:49:41.207Z_

<details><summary>↩ Tool result · `toolu_011jr3XtCUT5KdjEToU3TgCj`</summary>

```text
1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling), confirming that KL distillation provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.
34	Our contribution is prediction quality and inference simplification (removing the compensation network), not end-to-end latency reduction.
35	
36	
37	\section{Predictor Bottleneck Sensitivity}
38	\label{app:db_sensitivity}
39	
40	Table~\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.
41	
42	\begin{table}[h]
43	\centering
44	\caption{Predictor bottleneck sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}
45	\label{tab:db_sensitivity}
46	\small
47	\begin{tabular}{lcccc}
48	\toprule
49	$d_b$ & Params & TEAL global & $\Delta$ & Per-token \\
50	\midrule
51	64 & 38.2M (0.48\%) & 12.076 & +0.9\% & 10.16 \\ % exp_id: db_sensitivity_sweep
52	128 & 75.9M (0.95\%) & 11.963 & --- & 9.218 \\ % exp_id: db_sensitivity_sweep
53	256 & 151.5M (1.89\%) & 12.105 & +1.2\% & 8.586 \\ % exp_id: db_sensitivity_sweep
54	512 & 302.5M (3.77\%) & 12.315 & +2.9\% & 7.93 \\ % exp_id: db_sensitivity_sweep
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	Under TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\to$7.93).
60	This divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.
61	The $d_b{=}128$ configuration (75.9M params, $<$1\% of base model) is therefore optimal for the TEAL inference protocol.
62	
63	\subsection{Temperature Schedule Sensitivity}
64	\label{app:tau_sensitivity}
65	
66	\begin{table}[h]
67	\centering
68	\caption{Temperature schedule sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
69	\label{tab:tau_sensitivity}
70	\small
71	\begin{tabular}{lc}
72	\toprule
73	$\tau$ Schedule & PPL$\downarrow$ \\
74	\midrule
75	Fixed $\tau{=}0.5$ & \textbf{11.861} \\ % exp_id: tau_schedule_sweep
76	Linear $1.0 \to 0.1$ (default) & 11.963 \\ % exp_id: tau_schedule_sweep
77	Fixed $\tau{=}0.1$ & 12.072 \\ % exp_id: tau_schedule_sweep
78	\bottomrule
79	\end{tabular}
80	\end{table}
81	
82	Temperature schedule has minimal impact ($<$1.8\% PPL variation).
83	The linear annealing default is a conservative choice; even removing annealing entirely (fixed $\tau{=}0.5$) yields comparable performance.
84	
85	\subsection{Training Convergence}
86	\label{app:training_convergence}
87	
88	\begin{table}[h]
89	\centering
90	\caption{Training convergence at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
91	\label{tab:training_convergence}
92	\small
93	\begin{tabular}{cc}
94	\toprule
95	Steps & PPL$\downarrow$ \\
96	\midrule
97	200 & 15.158 \\ % exp_id: training_steps_sweep
98	400 & 12.538 \\ % exp_id: training_steps_sweep
99	600 & 12.046 \\ % exp_id: training_steps_sweep
100	800 & 11.907 \\ % exp_id: training_steps_sweep
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71a6195e-3006-4903-8af8-b6a297f74340",
  "isSidechain": true,
  "promptId": "83c10291-f9f7-46db-8cba-9066d7bf4990",
  "agentId": "a9cc4d1362dafefa3",
  "type": "user",
  "uuid": "f0a827e5-dbff-4c0a-8452-bbd4875e80e4",
  "sourceToolAssistantUUID": "71a6195e-3006-4903-8af8-b6a297f74340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-17T11:49:42.457Z_

Now let me search for Table 2 in experiments.tex to see the exact baseline comparisons:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0a827e5-dbff-4c0a-8452-bbd4875e80e4",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86BXjpJTityVnV8d5aL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "28f105f2-c302-4140-8e9e-81a2f5d68667",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LfUMJXhSVX65Zm7sCMvnbb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2141,
      "cache_read_input_tokens": 52021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2141,
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

_source line 24 · 2026-05-17T11:49:43.415Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Eb2n7cJY1PXTNH1oUMCfkT`</summary>

```json
{
  "command": "grep -A 20 \"tab:main\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28f105f2-c302-4140-8e9e-81a2f5d68667",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86BXjpJTityVnV8d5aL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3af8ebf0-3738-4a2d-bd4f-3c3e8fd46c2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LfUMJXhSVX65Zm7sCMvnbb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2141,
      "cache_read_input_tokens": 52021,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2141
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 124,
          "cache_read_input_tokens": 52021,
          "cache_creation_input_tokens": 2141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2141,
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

_source line 25 · 2026-05-17T11:49:43.511Z_

<details><summary>↩ Tool result · `toolu_01Eb2n7cJY1PXTNH1oUMCfkT`</summary>

```text
Table~\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\S\ref{sec:scaling}).
At 30\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.98, reducing TEAL's degradation from dense (10.97 $\to$ 8.98, an 18\% improvement). % exp_id: kl_30_global_teal
Uniform allocation at 30\% recovers MMLU to 40.61\% (+15.3pp over KL-global's 25.27\%): global top-$k$ starves late layers (L31 retention 28.4\%) while uniform guarantees capacity in logit-forming layers (\S\ref{sec:scaling}). % exp_id: bench_kl30_uniform

At 50\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\ 23.31, a 49\% reduction. % exp_id: bench_kl50_global, bench_teal50
The predictor also generalizes to held-out data (C4 validation: 52.5\% advantage over TEAL; see Appendix~\ref{app:ood}).
However, all methods exhibit downstream collapse on MMLU (27.89\% vs.\ 27.77\% for global vs.\ uniform, both $\approx$ random) and GSM8K ($<$2.2\%), indicating a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform

\begin{table}[t]
\centering
\caption{Main results on LLaMA-3.1-8B. PPL$\downarrow$ on WikiText-2; accuracy$\uparrow$ on downstream tasks. \textbf{Bold}: best among compensation-free methods per sparsity level. BCE uses a different inference protocol: hard binary masks from the predictor with a learned compensation network (67.2M params) applied post-masking; no TEAL allocation. Results are single-seed except 50\% uniform (3-seed mean $\pm$ std: $11.92 \pm 0.07$; Appendix~\ref{app:stability}).}
\label{tab:main}
\resizebox{\columnwidth}{!}{
\begin{tabular}{llccccc}
\toprule
Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
\midrule
0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
\midrule
\multirow{3}{*}{30\%}
& TEAL vanilla & 10.97 & \textbf{42.32} & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
& KL global (Ours) & 8.98 & 39.68 & \textbf{70.17} & 25.27 & \textbf{8.79} \\ % exp_id: lm_eval_kl_30pct_s42
& KL uniform & \textbf{8.82} & 40.78 & 68.59 & \textbf{40.61} & 7.35 \\ % exp_id: bench_kl30_uniform
\midrule
\multirow{4}{*}{50\%}
& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
& KL global (Ours) & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 27.89 & 1.29 \\ % exp_id: bench_kl50_global
& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \textbf{2.12} \\ % exp_id: d030_kl50_uniform
& BCE (2700 steps)$^\ast$ & 27.97 & 23.98 & 50.59 & 30.02 & 4.85 \\ % exp_id: eval_bce_v3_s42
\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3af8ebf0-3738-4a2d-bd4f-3c3e8fd46c2b",
  "isSidechain": true,
  "promptId": "83c10291-f9f7-46db-8cba-9066d7bf4990",
  "agentId": "a9cc4d1362dafefa3",
  "type": "user",
  "uuid": "fa4c41fe-7a2f-4201-a160-3d662d5f8b82",
  "sourceToolAssistantUUID": "3af8ebf0-3738-4a2d-bd4f-3c3e8fd46c2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-17T11:49:45.034Z_

Perfect! Now let me compile a comprehensive summary of my findings. Let me double-check what methods are mentioned as citations vs experimental comparisons:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa4c41fe-7a2f-4201-a160-3d662d5f8b82",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86BhbQGvRCnMrQyeJHc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5fe5e037-2e15-4609-ba2d-760fd39ef6f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WM4HtFhLSGgX5pFJrQA9VL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 54162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1274,
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

_source line 27 · 2026-05-17T11:49:46.094Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JnkWr1t6DgLW3mhJ7TqDUN`</summary>

```json
{
  "command": "grep -i \"maskllm\\|dejavu\\|cats\\|powerinfer\\|fastforward\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fe5e037-2e15-4609-ba2d-760fd39ef6f9",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86BhbQGvRCnMrQyeJHc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de0f4d44-2000-4b84-9059-aebff1ff2101",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WM4HtFhLSGgX5pFJrQA9VL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 54162,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1274
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 141,
          "cache_read_input_tokens": 54162,
          "cache_creation_input_tokens": 1274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1274,
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

_source line 28 · 2026-05-17T11:49:46.147Z_

<details><summary>↩ Tool result · `toolu_01JnkWr1t6DgLW3mhJ7TqDUN`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de0f4d44-2000-4b84-9059-aebff1ff2101",
  "isSidechain": true,
  "promptId": "83c10291-f9f7-46db-8cba-9066d7bf4990",
  "agentId": "a9cc4d1362dafefa3",
  "type": "user",
  "uuid": "180e1238-de72-4a11-a44d-cfd0583a38a6",
  "sourceToolAssistantUUID": "de0f4d44-2000-4b84-9059-aebff1ff2101",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T11:49:47.408Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BmK5eNHyvKSgQ9cg27Tcc1`</summary>

```json
{
  "command": "grep -i \"maskllm\\|dejavu\\|cats\\|powerinfer\\|fastforward\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "180e1238-de72-4a11-a44d-cfd0583a38a6",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86BtrKJwE4GYk3QL62A",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ca717f62-a8fc-4cc2-9cec-691b48dff9b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YPCz2EdjjD5YTrWpizmkCP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 55436,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 160
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 113,
          "cache_read_input_tokens": 55436,
          "cache_creation_input_tokens": 160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 160,
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

_source line 30 · 2026-05-17T11:49:47.461Z_

<details><summary>↩ Tool result · `toolu_01BmK5eNHyvKSgQ9cg27Tcc1`</summary>

```text
CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint.
The structural mismatch we characterize (per-neuron gradient decomposition vs.\ global top-$k$) does not arise in MaskLLM's per-group categorical setting, where N:M patterns eliminate cross-group budget competition.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca717f62-a8fc-4cc2-9cec-691b48dff9b9",
  "isSidechain": true,
  "promptId": "83c10291-f9f7-46db-8cba-9066d7bf4990",
  "agentId": "a9cc4d1362dafefa3",
  "type": "user",
  "uuid": "d46c831e-469b-4420-8159-7fd0915cba5b",
  "sourceToolAssistantUUID": "ca717f62-a8fc-4cc2-9cec-691b48dff9b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-17T11:49:59.331Z_

Excellent. Now I have all the information I need. Let me compile my report.

## Summary: Baselines and Downstream Tasks in distill_sparse_swiglu Paper

### 1. **Baselines in Table 2 (Main Results)**

The paper's main experimental comparison (Table 2 / `tab:main` in experiments.tex) includes:

**Experimentally Compared Against:**
- **TEAL vanilla** (baseline at 30% and 50% sparsity) - the primary baseline
- **KL global (Ours)** - the paper's proposed method
- **KL uniform** - allocation variant of the proposed method
- **BCE (2700 steps)** - alternative training approach with compensation network (only at 50% sparsity)
- **Dense** (0% sparsity) - upper bound reference

So the paper directly compares against only **TEAL** as the main competing method, plus a **BCE** variant at one sparsity level.

### 2. **Methods Cited in Related Work (Not Experimentally Compared)**

In `related_work.tex`, the following methods are cited as related but **NOT experimentally compared**:

**Training-Free Activation Sparsity:**
- **CATS** (lee2024cats) - contextually-aware thresholding for SwiGLU
- R-Sparse - rank-aware SVD projections  
- DIP - dynamic input pruning + cache-aware masking
- SparseInfer - training-free prediction from attention outputs

**Predictor-Based Contextual Sparsity:**
- **DejaVu** (liu2023dejavu) - BCE-based learned predictor (foundational prior work)
- **FastForward** (gautam2026fastforward) - compensation network + BCE + 67.2M params overhead
- **MaskLLM** (fang2024maskllm) - learnable masks with Gumbel + KL training (but for weight sparsity, not activation)
- ShadowLLM - attention-based routing with per-layer MSE supervision
- **SVD-CSP** (serbin2026svdcsp) - SVD compression of sparsity predictors
- **PowerInfer** (song2024powerinfer) - power-law activation exploitation for GPU-CPU scheduling

**Activation Function Engineering:**
- SPON (xu2026spon) - static per-layer bias correction (analyzed in paper, not a baseline)
- ReLU Strikes Back, TurboSparse, ProSparse

**Others:**
- Weight pruning (Wanda, SparseGPT), conditional computation (Switch Transformers, Mixture-of-Depths)

### 3. **Downstream Tasks Evaluated**

The paper evaluates on **4 downstream tasks**:
- **ARC-Challenge** (25-shot)
- **WinoGrande** (5-shot)  
- **MMLU** (5-shot)
- **GSM8K** (8-shot)

**Common benchmarks NOT included:**
- HellaSwag
- PIQA
- BoolQ

### 4. **Key Findings**

| Finding | Detail |
|---------|--------|
| **Experimental vs. Cited** | Only TEAL is experimentally compared; 8+ related methods (DejaVu, CATS, MaskLLM, FastForward, PowerInfer, SVD-CSP, SparseInfer, DIP) are cited but not benchmarked |
| **Gap in Comparisons** | No experimental comparison with other learned predictor baselines like DejaVu or FastForward, which are the most directly related methods |
| **Task Coverage** | Limited to 4 reasoning/knowledge tasks; missing commonsense (HellaSwag, PIQA) and factual (BoolQ) benchmarks |
| **Models Tested** | LLaMA-3.1-8B and Mistral-7B only; no 70B models or other architectures |
| **Why Limited Comparisons** | Related work notes that competing methods use different objectives (BCE vs. KL) or target different problems (weight vs. activation sparsity; training-free vs. learned) |

### 5. **Reference Entries Present**

All requested references are present in `references.bib`:
- ✓ maskllm (fang2024maskllm)
- ✓ dejavu (liu2023dejavu) 
- ✓ cats (lee2024cats)
- ✓ powerinfer (song2024powerinfer)
- ✓ fastforward (gautam2026fastforward)
- ✓ teal (liu2025teal)
- ✓ wina (referenced in experiments.tex as variant, liu2025teal)
- ✓ sparseInfer (shin2025sparseinfer)
- ✓ svdcsp (serbin2026svdcsp)
- ✓ d2dmoe (szatkowski2024d2dmoe)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d46c831e-469b-4420-8159-7fd0915cba5b",
  "isSidechain": true,
  "agentId": "a9cc4d1362dafefa3",
  "requestId": "req_011Cb86BzUQRcdJ6KLW4PRba",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ba258f7d-1d18-467b-a386-d7af585ddd46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/director_b05a67f7",
  "sessionId": "cc7425e6-7062-479d-9699-e7d854e6065f",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "fancy-prancing-candle",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Hhg4N9JwjMxJPCfEPS3m9L",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 530,
      "cache_read_input_tokens": 55596,
      "output_tokens": 1200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 530
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1200,
          "cache_read_input_tokens": 55596,
          "cache_creation_input_tokens": 530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 530,
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
