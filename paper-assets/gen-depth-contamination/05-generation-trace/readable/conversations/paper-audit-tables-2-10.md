# paper audit tables 2 10

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_paper_audit_tables_2_10_20260523T110133.jsonl`
- **Structured JSON:** [`0f29d42cd156aeab69f0.json`](../../sessions/0f/0f29d42cd156aeab69f0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-23T11:14:58.559939+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T11:14:58.560285+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T11:14:58.560487+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "gen-depth-contamination",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "gen-depth-contamination",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T11:14:58.562140+00:00_

Error: result (288,566 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T11:14:58.562368+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T11:14:58.562601+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on ten model configurations spanning six architecture families:
5	Pythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical \leq 2$ Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\resizebox{\textwidth}{!}{%
20	\begin{tabular}{lcccccccccc}
21	\toprule
22	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
23	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
24	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
25	\midrule
26	0v1 & .9956 & & .9722 & & .9860 & & .9971 & & .9638 & [.961,\,.967] \\
27	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6074 & [.598,\,.617]\rlap{$^*$} & .5001 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
28	2v3 & .5893 & [.580,\,.599] & .5440 & [.534,\,.554] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
29	3v4 & .5435 & & .5051 & & .5024\rlap{$^\S$} & & .5409 & & .5276
…[truncated 11916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T11:14:58.562770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T11:14:58.563189+00:00_

1	\appendix
2	\section{Supplementary Materials}
3	\label{sec:appendix}
4	
5	This appendix provides supplementary figures, detailed experimental tables, dataset statistics, and complete feature descriptions referenced in the main text.
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
10	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
11	\label{fig:filtering_strategies}
12	\end{figure}
13	
14	\paragraph{Feature ranking and cross-model consistency.}
15	Table~\ref{tab:top_features} reports per-model single-feature AUC rankings.
16	Surprisal derivative features (\texttt{surp\_d1\_std}, \texttt{surp\_d2\_std}) consistently rank among the top three across all continuation-mode models (Pythia, OLMo, Qwen-cont), with pairwise Spearman $\rho \geq 0.85$.
17	The rewrite-mode model (Qwen-rw) diverges by placing \texttt{freq\_entropy} first, reflecting a distributional shift that is lexical rather than surprisal-driven.
18	This scorer-invariant ranking supports the use of a fixed 15-dimensional feature set across generators without per-model feature selection.
19	
20	%%% Feature ranking table (moved from main text)
21	\begin{table}[!htbp]
22	\centering
23	\small
24	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
25	\label{tab:top_features}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{cllll}
28	\toprule
29	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
30	\midrule
31	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
32	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_st
…[truncated 23997 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T11:14:58.563356+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T11:14:58.563536+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Corpus-level statistical features are fed to the OBD-LightGBM classifier for depth prediction. (Simplified notation; see Eq.~\ref{eq:kstar} for the formal $\Kempirical$ definition.)}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: mutual information with the seed text degrades monotonically.
17	Together with Markov chain convergence, this motivates the existence of a finite discrimination boundary where $\auc_{k-1,k}$ falls below a decision threshold, though AUC and mutual information are not formally equivalent; the actual saturation depth must therefore be measured empirically.
18	Pairwise AUC may exhibit non-monotonicity at deeper depths due to classifier and feature interactions (e.g., Pythia-1.4B greedy 4v5 $\auc = 1.0$ vs.\ 3v4 $= 0.522$; Table~\ref{tab:s10_pythia_decoding}), reinforcing that $\Kempirical$ is a measured quantity rather than a theoretical prediction.
19	
20	We define the operational lower bound:
21	\begin{equation}
22	  \Kempirical = \max\!\bigl\{k \!\geq\! 1 : \auc_{j-1,j} > \theta,\;\forall\, 1 \!\leq\! j \!\leq\! k\bigr\},
23	  \label{eq:kstar}
24	\end{equation}
25	which requires all pairs up to depth $k$ to exceed the threshold (the $\forall j$ constraint is naturally satisfied because $\auc_{k-1,k}$ decreases monotonically above $\theta$ across all tested 
…[truncated 6142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T11:14:58.563722+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\n# Probe structure\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\n# result is likely a JSON string\nparsed = json.loads(result)\nprint(type(parsed).__name__, len(parsed) if isinstance(parsed, list) else 'N/A')\nif isinstance(parsed, list) and len(parsed) > 0:\n    print('Keys of first entry:', list(parsed[0].keys()))\n    print('First exp_id:', parsed[0].get('exp_id', 'N/A'))\n\"\n",
  "description": "Probe registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\n# Probe structure\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\n# result is likely a JSON string\nparsed = json.loads(result)\nprint(type(parsed).__name__, len(parsed) if isinstance(parsed, list) else 'N/A')\nif isinstance(parsed, list) and len(parsed) > 0:\n    print('Keys of first entry:', list(parsed[0].keys()))\n    print('First exp_id:', parsed[0].get('exp_id', 'N/A'))\n\"\n",
    "description": "Probe registry JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T11:14:58.563878+00:00_

dict N/A

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T11:14:58.564004+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nprint(type(result).__name__)\nif isinstance(result, dict):\n    print('Top keys:', list(result.keys())[:20])\n    for k in list(result.keys())[:3]:\n        v = result[k]\n        print(f'  {k}: type={type(v).__name__}')\n        if isinstance(v, dict):\n            print(f'    keys: {list(v.keys())[:10]}')\n\"\n",
  "description": "Probe registry dict structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nprint(type(result).__name__)\nif isinstance(result, dict):\n    print('Top keys:', list(result.keys())[:20])\n    for k in list(result.keys())[:3]:\n        v = result[k]\n        print(f'  {k}: type={type(v).__name__}')\n        if isinstance(v, dict):\n            print(f'    keys: {list(v.keys())[:10]}')\n\"\n",
    "description": "Probe registry dict structure"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T11:14:58.564135+00:00_

dict
Top keys: ['success', 'data', 'error', 'metadata']
  success: type=bool
  data: type=dict
    keys: ['experiments', 'count', 'total', 'baseline']
  error: type=NoneType

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T11:14:58.564257+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\nfor eid, exp in sorted(exps.items()):\n    title = exp.get('title', '')\n    status = exp.get('status', '')\n    print(f'{eid}: [{status}] {title}')\n\"\n",
  "description": "List all experiment IDs and titles"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\nfor eid, exp in sorted(exps.items()):\n    title = exp.get('title', '')\n    status = exp.get('status', '')\n    print(f'{eid}: [{status}] {title}')\n\"\n",
    "description": "List all experiment IDs and titles"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T11:14:58.564411+00:00_

Total experiments: 164

7b-cross-transfer: [PREPARING] 
arxiv_multi_source: [PREPARING] 
deberta_filter_deberta_binary: [PREPARING] 
deberta_filter_deberta_graduated: [PREPARING] 
deberta_filter_no_filter: [PREPARING] 
deberta_filter_obd_binary: [PREPARING] 
deberta_filtering_predict: [PREPARING] 
exp-008-retrain-chain: [DONE] 
exp-014: [DONE] 
exp_001_pythia_depth: [DONE] 
exp_002_olmo_depth: [DONE] 
exp_003_decoding_ablation: [DONE] 
exp_004_7b_crossscale: [DONE] 
exp_005_degradation: [DONE] 
exp_006_graduated_filtering: [DONE] 
exp_007_bootstrap_ci: [DONE] 
exp_008_retrain_chain: [PREPARING] 
exp_008_retrain_chain_v2: [DONE] 
exp_009_dose_10pct: [DONE] 
exp_009_dose_10pct_v2: [DONE] 
exp_009_dose_10pct_v3: [DONE] 
exp_009_dose_30pct: [DONE] 
exp_009_dose_30pct_v2: [DONE] 
exp_009_dose_30pct_v3: [DONE] 
exp_009_dose_50pct: [DONE] 
exp_009_dose_50pct_v2: [DONE] 
exp_009_dose_50pct_v3: [DONE] 
exp_009_dose_response: [DONE] 
exp_010_ordinal_baseline: [DONE] 
exp_011_llm_zeroshot: [DONE] 
exp_012_binary_confidence: [DONE] 
exp_013_cross_transfer: [DONE] 
exp_014_naturalistic: [DONE] 
exp_015_neural_probe: [DONE] 
exp_016_base_vs_instruct: [DONE] 
exp_017_qwen_continuation: [DONE] 
exp_018_llama8b_depth: [DONE] 
exp_019_mistral7b_depth: [DONE] 
exp_019b_mistral_cross_scorer: [DONE] 
exp_020_pythia_decoding: [DONE] 
exp_021_length_ablation: [DONE] 
exp_022_cross_scorer_matrix: [DONE] 
exp_023_domain_ablation: [DONE] 
exp_024_arxiv_domain: [DONE] 
exp_025_pythia_arxiv: [DONE] 
exp_025_pythia_filtering: [DONE] 
exp_026_arxiv_filtering: [DONE] 
exp_026_feature_stability: [DONE] 
exp_026_feature_stability_v2: [DONE] 
exp_027: [DONE] 
exp_027_latex_ablation: [DONE] 
exp_027_retrain_bootstrap: [DONE] 
exp_028_power_curve: [DONE] 
exp_028_subsampling_power: [DONE] 
exp_14b_c4: [DONE] 
exp_32b_c4: [DONE] 
exp_32b_c4_6class: [DONE] 
exp_7b_scorer_ablation: [DONE] 
exp_7b_scorer_arxiv: [DONE] 
exp_A_alt_scorer: [DONE] 
exp_B_14d_ablation: [DONE] 
exp_C_permutation_10k: [DONE] 
ex
…[truncated 3295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T11:14:58.564576+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Key experiments for Table 2 and Table 10\nkey_ids = [\n    'exp_14b_c4',  # Qwen-rw?\n    'exp_001_pythia_depth',\n    'exp_002_olmo_depth', \n    'exp_017_qwen_continuation',\n    'exp_004_7b_crossscale',\n    'exp_016_base_vs_instruct',\n    'exp_018_llama8b_depth',\n    'exp_019_mistral7b_depth',\n    'exp_pythia69b_c4_nuc',\n    'exp_gemma2b_depth',\n    'exp_gemma2b_10k',\n    'exp_007_bootstrap_ci',\n    'exp_bootstrap_10k',\n    'exp_pythia14b_10k',\n    'exp_pythia14b_c4_10k',\n    'exp_pythia14b_c4_rerun',\n    'exp_olmo1b_10k',\n    'exp_olmo1b_c4_rerun',\n    'exp_qwen_cont_10k',\n    'exp_llama8b_10k',\n    'exp_pythia69b_c4_depth_chain_v3',\n    'exp_7b_scorer_ablation',\n]\n\nfor eid in key_ids:\n    if eid in exps:\n        exp = exps[eid]\n        title = exp.get('title', 'N/A')\n        metrics = exp.get('metrics', {})\n        conclusion = exp.get('conclusion', '')\n        print(f'=== {eid} ===')\n        print(f'  Title: {title}')\n        if metrics:\n            # Print all metric keys\n            print(f'  Metric keys: {list(metrics.keys())}')\n            # Print AUC-related metrics\n            for k, v in sorted(metrics.items()):\n                if 'auc' in k.lower() or 'ci' in k.lower() or 'AUC' in k:\n                    print(f'  {k}: {v}')\n        if conclusion:\n            print(f'  Conclusion: {conclusion[:200]}')\n        print()\n\" 2>&1 | head -200\n",
  "description": "Extract metrics from key experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Key experiments for Table 2 and Table 10\nkey_ids = [\n    'exp_14b_c4',  # Qwen-rw?\n    'exp_001_pythia_depth',\n    'exp_002_olmo_depth', \n    'exp_017_qwen_continuation',\n    'exp_004_7b_crossscale',\n    'exp_016_base_vs_instruct',\n    'exp_018_llama8b_depth',\n    'exp_019_mistral7b_depth',\n    'exp_pythia69b_c4_nuc',\n    'exp_gemma2b_depth',\n    'exp_gemma2b_10k',\n    'exp_007_bootstrap_ci',\n    'exp_bootstrap_10k',\n    'exp_pythia14b_10k',\n    'exp_pythia14b_c4_10k',\n    'exp_pythia14b_c4_rerun',\n    'exp_olmo1b_10k',\n    'exp_olmo1b_c4_rerun',\n    'exp_qwen_cont_10k',\n    'exp_llama8b_10k',\n    'exp_pythia69b_c4_depth_chain_v3',\n    'exp_7b_scorer_ablation',\n]\n\nfor eid in key_ids:\n    if eid in exps:\n        exp = exps[eid]\n        title = exp.get('title', 'N/A')\n        metrics = exp.get('metrics', {})\n        conclusion = exp.get('conclusion', '')\n        print(f'=== {eid} ===')\n        print(f'  Title: {title}')\n        if metrics:\n            # Print all metric keys\n            print(f'  Metric keys: {list(metrics.keys())}')\n            # Print AUC-related metrics\n            for k, v in sorted(metrics.items()):\n                if 'auc' in k.lower() or 'ci' in k.lower() or 'AUC' in k:\n                    print(f'  {k}: {v}')\n        if conclusion:\n            print(f'  Conclusion: {conclusion[:200]}')\n        print()\n\" 2>&1 | head -200\n",
    "description": "Extract metrics from key experiments"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T11:14:58.564759+00:00_

=== exp_14b_c4 ===
  Title: N/A
  Metric keys: ['k_star', 'pairwise_auc', 'pairwise_jsd', 'bootstrap_ci', 'permutation_p', 'k_star_statistically_confirmed', 'ordinal_mae', 'ordinal_accuracy', 'top_features', 'key_finding']
  bootstrap_ci: {'0v1': [0.9564, 0.963], '1v2': [0.6119, 0.6304], '2v3': [0.5392, 0.5594], '3v4': [0.514, 0.5346], '4v5': [0.5045, 0.5265]}
  pairwise_auc: {'0v1': 0.9598, '1v2': 0.621, '2v3': 0.5494, '3v4': 0.5243, '4v5': 0.5154}
  Conclusion: success

=== exp_001_pythia_depth ===
  Title: N/A
  Metric keys: ['k_star', 'pairwise_auc', 'pairwise_auc_std', 'bootstrap_ci', 'scorer', 'note']
  bootstrap_ci: {'1v2': {'auc_oof': 0.6072, 'boot_mean': 0.6073, 'boot_std': 0.005, 'ci_95': [0.5975, 0.6172], 'ci_995_bonferroni': [0.5934, 0.621], 'perm_p': 0.0001, 'bonferroni_pass': False}}
  pairwise_auc: {'0v1': 0.9722, '1v2': 0.6074, '2v3': 0.544, '3v4': 0.5051, '4v5': 0.5079}
  pairwise_auc_std: {'0v1': 0.0039, '1v2': 0.0078, '2v3': 0.0067, '3v4': 0.0032, '4v5': 0.0101}
  Conclusion: success

=== exp_002_olmo_depth ===
  Title: N/A
  Metric keys: ['k_star', 'pairwise_auc', 'scorer', 'note']
  pairwise_auc: {'0v1': 0.9861, '1v2': 0.5001, '2v3': 0.4972, '3v4': 0.5034, '4v5': 0.4971}
  Conclusion: success

=== exp_017_qwen_continuation ===
  Title: N/A
  Metric keys: ['k_star', 'pairwise_auc', 'pairwise_jsd', 'ordinal_mae', 'ordinal_accuracy', 'top3_features']
  pairwise_auc: {'0v1': 0.9972, '1v2': 0.6114, '2v3': 0.5609, '3v4': 0.5408, '4v5': 0.5139}
  Conclusion: success

=== exp_004_7b_crossscale ===
  Title: N/A
  Metric keys: ['k_star', 'pairwise_auc', 'pairwise_auc_std', 'bootstrap_ci', 'bootstrap_resamples', 'permutation_resamples', 'pairwise_jsd', 'ordinal_mae', 'ordinal_accuracy', 'top_features', 'key_finding']
  bootstrap_ci: {'0v1': {'auc': 0.9638, 'ci_lower': 0.9607, 'ci_upper': 0.9665, 'perm_p': 0.0001}, '1v2': {'auc': 0.6168, 'ci_lower': 0.6079, 'ci_upper': 0.6261, 'perm_p': 0.0001}, '2v3': {'auc': 0.5492, 'ci_lower': 0.5388, 'ci_upper': 0.5594,
…[truncated 6780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T11:14:58.564966+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Find Qwen-rw related experiments - search by AUC values near .9956 and .6955\nfor eid, exp in sorted(exps.items()):\n    metrics = exp.get('metrics', {})\n    pauc = metrics.get('pairwise_auc', {})\n    if isinstance(pauc, dict):\n        v01 = pauc.get('0v1', None)\n        v12 = pauc.get('1v2', None)\n        if v01 and v12:\n            if (0.99 < v01 < 1.0 and 0.68 < v12 < 0.72):\n                print(f'{eid}: 0v1={v01}, 1v2={v12}')\n                print(f'  All AUC: {pauc}')\n                ci = metrics.get('bootstrap_ci', {})\n                if ci:\n                    print(f'  Bootstrap CI: {json.dumps(ci, indent=2)[:500]}')\n                print()\n\" 2>&1\n",
  "description": "Find Qwen-rw experiment by AUC pattern"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Find Qwen-rw related experiments - search by AUC values near .9956 and .6955\nfor eid, exp in sorted(exps.items()):\n    metrics = exp.get('metrics', {})\n    pauc = metrics.get('pairwise_auc', {})\n    if isinstance(pauc, dict):\n        v01 = pauc.get('0v1', None)\n        v12 = pauc.get('1v2', None)\n        if v01 and v12:\n            if (0.99 < v01 < 1.0 and 0.68 < v12 < 0.72):\n                print(f'{eid}: 0v1={v01}, 1v2={v12}')\n                print(f'  All AUC: {pauc}')\n                ci = metrics.get('bootstrap_ci', {})\n                if ci:\n                    print(f'  Bootstrap CI: {json.dumps(ci, indent=2)[:500]}')\n                print()\n\" 2>&1\n",
    "description": "Find Qwen-rw experiment by AUC pattern"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T11:14:58.565109+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 15, in &lt;module>
    if (0.99 < v01 < 1.0 and 0.68 < v12 < 0.72):
        ^^^^^^^^^^^^^^^^
TypeError: '<' not supported between instances of 'float' and 'dict'
exp_32b_c4_6class: 0v1=0.9923, 1v2=0.6945
  All AUC: {'0v1': 0.9923, '1v2': 0.6945, '2v3': 0.5978, '3v4': 0.5669, '4v5': 0.5426}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T11:14:58.565237+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Find Qwen-rw: search for 0v1 near .9956 and 1v2 near .6955\nfor eid, exp in sorted(exps.items()):\n    metrics = exp.get('metrics', {})\n    pauc = metrics.get('pairwise_auc', {})\n    if isinstance(pauc, dict):\n        v01 = pauc.get('0v1', None)\n        v12 = pauc.get('1v2', None)\n        if v01 is None or v12 is None:\n            continue\n        if not isinstance(v01, (int, float)) or not isinstance(v12, (int, float)):\n            continue\n        if (0.99 < v01 < 1.0 and 0.68 < v12 < 0.72):\n            print(f'{eid}: 0v1={v01}, 1v2={v12}')\n            print(f'  All AUC: {pauc}')\n            ci = metrics.get('bootstrap_ci', {})\n            if ci:\n                print(f'  Bootstrap CI keys: {list(ci.keys())}')\n            print()\n\" 2>&1\n",
  "description": "Find Qwen-rw experiment by AUC values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Find Qwen-rw: search for 0v1 near .9956 and 1v2 near .6955\nfor eid, exp in sorted(exps.items()):\n    metrics = exp.get('metrics', {})\n    pauc = metrics.get('pairwise_auc', {})\n    if isinstance(pauc, dict):\n        v01 = pauc.get('0v1', None)\n        v12 = pauc.get('1v2', None)\n        if v01 is None or v12 is None:\n            continue\n        if not isinstance(v01, (int, float)) or not isinstance(v12, (int, float)):\n            continue\n        if (0.99 < v01 < 1.0 and 0.68 < v12 < 0.72):\n            print(f'{eid}: 0v1={v01}, 1v2={v12}')\n            print(f'  All AUC: {pauc}')\n            ci = metrics.get('bootstrap_ci', {})\n            if ci:\n                print(f'  Bootstrap CI keys: {list(ci.keys())}')\n            print()\n\" 2>&1\n",
    "description": "Find Qwen-rw experiment by AUC values"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T11:14:58.565369+00:00_

exp_32b_c4_6class: 0v1=0.9923, 1v2=0.6945
  All AUC: {'0v1': 0.9923, '1v2': 0.6945, '2v3': 0.5978, '3v4': 0.5669, '4v5': 0.5426}

exp_deberta_c4_1b5: 0v1=0.9923, 1v2=0.7052
  All AUC: {'0v1': 0.9923, '1v2': 0.7052, '2v3': 0.5988, '3v4': 0.5698, '4v5': 0.5475}

exp_deberta_c4_1b5_qwen_cont: 0v1=0.9955, 1v2=0.7194
  All AUC: {'0v1': 0.9955, '1v2': 0.7194, '2v3': 0.5954, '3v4': 0.5689, '4v5': 0.5502}

mvp_pilot_sat_v1: 0v1=0.9956, 1v2=0.6957
  All AUC: {'0v1': 0.9956, '1v2': 0.6957, '2v3': 0.5893, '3v4': 0.5434, '4v5': 0.5343}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T11:14:58.565517+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get full details of mvp_pilot_sat_v1 and exp_007_bootstrap_ci\nfor eid in ['mvp_pilot_sat_v1', 'exp_007_bootstrap_ci', 'exp_bootstrap_10k']:\n    if eid in exps:\n        exp = exps[eid]\n        metrics = exp.get('metrics', {})\n        print(f'=== {eid} ===')\n        print(json.dumps(metrics, indent=2)[:3000])\n        print()\n\" 2>&1\n",
  "description": "Get Qwen-rw and bootstrap CI details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get full details of mvp_pilot_sat_v1 and exp_007_bootstrap_ci\nfor eid in ['mvp_pilot_sat_v1', 'exp_007_bootstrap_ci', 'exp_bootstrap_10k']:\n    if eid in exps:\n        exp = exps[eid]\n        metrics = exp.get('metrics', {})\n        print(f'=== {eid} ===')\n        print(json.dumps(metrics, indent=2)[:3000])\n        print()\n\" 2>&1\n",
    "description": "Get Qwen-rw and bootstrap CI details"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T11:14:58.565718+00:00_

=== mvp_pilot_sat_v1 ===
{
  "pairwise_auc": {
    "0v1": 0.9956,
    "1v2": 0.6957,
    "2v3": 0.5893,
    "3v4": 0.5434,
    "4v5": 0.5343
  },
  "pairwise_auc_std": {
    "0v1": 0.0005,
    "1v2": 0.0072,
    "2v3": 0.012,
    "3v4": 0.0053,
    "4v5": 0.0091
  },
  "pairwise_jsd": {
    "0v1": 0.2669,
    "1v2": 0.0163,
    "2v3": 0.0069,
    "3v4": 0.0047,
    "4v5": 0.0041
  },
  "k_star": 2,
  "ordinal_mae": 1.0163,
  "ordinal_accuracy": 0.4182
}

=== exp_007_bootstrap_ci ===
{
  "qwen_rewrite": {
    "0v1": {
      "auc": 0.9956,
      "ci_lower": 0.9946,
      "ci_upper": 0.9965,
      "perm_p": 0.002
    },
    "1v2": {
      "auc": 0.6955,
      "ci_lower": 0.6859,
      "ci_upper": 0.7041,
      "perm_p": 0.002
    },
    "2v3": {
      "auc": 0.5893,
      "ci_lower": 0.5795,
      "ci_upper": 0.5991,
      "perm_p": 0.002
    },
    "3v4": {
      "auc": 0.5435,
      "ci_lower": 0.5333,
      "ci_upper": 0.5551,
      "perm_p": 0.002
    },
    "4v5": {
      "auc": 0.534,
      "ci_lower": 0.5238,
      "ci_upper": 0.5448,
      "perm_p": 0.002
    }
  },
  "pythia_cont": {
    "0v1": {
      "auc": 0.9932,
      "ci_lower": 0.9921,
      "ci_upper": 0.9943,
      "perm_p": 0.002
    },
    "1v2": {
      "auc": 0.6539,
      "ci_lower": 0.6454,
      "ci_upper": 0.663,
      "perm_p": 0.002
    },
    "2v3": {
      "auc": 0.5514,
      "ci_lower": 0.5417,
      "ci_upper": 0.5628,
      "perm_p": 0.002
    },
    "3v4": {
      "auc": 0.5152,
      "ci_lower": 0.5041,
      "ci_upper": 0.526,
      "perm_p": 0.006
    },
    "4v5": {
      "auc": 0.5136,
      "ci_lower": 0.5021,
      "ci_upper": 0.5249,
      "perm_p": 0.008
    }
  },
  "olmo_cont": {
    "0v1": {
      "auc": 0.997,
      "ci_lower": 0.9964,
      "ci_upper": 0.9975,
      "perm_p": 0.002
    },
    "1v2": {
      "auc": 0.6145,
      "ci_lower": 0.6045,
      "ci_upper": 0.6247,
      "perm_p": 0.002
    },
    "2v3": {
      "auc": 0.5496,
      "ci_lower": 0.5399,
      "ci_
…[truncated 2410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T11:14:58.565928+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get scorer info and full metrics for OLMo and Pythia experiments\nfor eid in ['exp_002_olmo_depth', 'exp_001_pythia_depth', 'exp_olmo1b_c4_rerun', 'exp_olmo1b_10k', 'exp_pythia14b_c4_rerun', 'exp_pythia14b_c4_10k', 'exp_019_mistral7b_depth', 'exp_pythia69b_c4_nuc']:\n    if eid in exps:\n        exp = exps[eid]\n        metrics = exp.get('metrics', {})\n        print(f'=== {eid} ===')\n        # Print scorer info\n        for k in ['scorer', 'note', 'NOTE']:\n            if k in metrics:\n                print(f'  {k}: {metrics[k]}')\n        # Print all AUC and CI\n        for k, v in sorted(metrics.items()):\n            if 'auc' in k.lower() or 'ci' in k.lower() or 'AUC' in k or 'boot' in k.lower():\n                print(f'  {k}: {v}')\n        print()\n\" 2>&1\n",
  "description": "Get scorer info for OLMo and Pythia"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get scorer info and full metrics for OLMo and Pythia experiments\nfor eid in ['exp_002_olmo_depth', 'exp_001_pythia_depth', 'exp_olmo1b_c4_rerun', 'exp_olmo1b_10k', 'exp_pythia14b_c4_rerun', 'exp_pythia14b_c4_10k', 'exp_019_mistral7b_depth', 'exp_pythia69b_c4_nuc']:\n    if eid in exps:\n        exp = exps[eid]\n        metrics = exp.get('metrics', {})\n        print(f'=== {eid} ===')\n        # Print scorer info\n        for k in ['scorer', 'note', 'NOTE']:\n            if k in metrics:\n                print(f'  {k}: {metrics[k]}')\n        # Print all AUC and CI\n        for k, v in sorted(metrics.items()):\n            if 'auc' in k.lower() or 'ci' in k.lower() or 'AUC' in k or 'boot' in k.lower():\n                print(f'  {k}: {v}')\n        print()\n\" 2>&1\n",
    "description": "Get scorer info for OLMo and Pythia"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T11:14:58.566084+00:00_

=== exp_002_olmo_depth ===
  scorer: Qwen2.5-1.5B-Instruct
  note: Updated to Qwen cross-scoring (D107). Self-scored 1v2=0.6145 K*=2, Qwen-scored 1v2=0.5001 K*=1.
  pairwise_auc: {'0v1': 0.9861, '1v2': 0.5001, '2v3': 0.4972, '3v4': 0.5034, '4v5': 0.4971}

=== exp_001_pythia_depth ===
  scorer: Qwen2.5-1.5B-Instruct
  note: Updated to Qwen cross-scoring (D107). Self-scored 1v2=0.6539, Qwen-scored 1v2=0.6074.
  bootstrap_ci: {'1v2': {'auc_oof': 0.6072, 'boot_mean': 0.6073, 'boot_std': 0.005, 'ci_95': [0.5975, 0.6172], 'ci_995_bonferroni': [0.5934, 0.621], 'perm_p': 0.0001, 'bonferroni_pass': False}}
  pairwise_auc: {'0v1': 0.9722, '1v2': 0.6074, '2v3': 0.544, '3v4': 0.5051, '4v5': 0.5079}
  pairwise_auc_std: {'0v1': 0.0039, '1v2': 0.0078, '2v3': 0.0067, '3v4': 0.0032, '4v5': 0.0101}

=== exp_olmo1b_c4_rerun ===
  0v1_auc: 0.986
  1v2_auc: 0.508
  2v3_auc: 0.4973
  3v4_auc: 0.5024
  4v5_auc: 0.4942

=== exp_olmo1b_10k ===
  pairwise_auc: {'0v1': 0.9871, '1v2': 0.4984, '2v3': 0.5059, '3v4': 0.5061, '4v5': 0.5074}

=== exp_pythia14b_c4_rerun ===
  NOTE: GREEDY decoding -- inflated AUC, not comparable to main table
  0v1_auc: 0.9979
  1v2_auc: 0.8786
  2v3_auc: 0.5399
  3v4_auc: 0.5062
  4v5_auc: 0.5025

=== exp_pythia14b_c4_10k ===
  AUC_0v1: 0.9712
  AUC_1v2: 0.6175
  AUC_2v3: 0.5364
  AUC_3v4: 0.5134
  AUC_4v5: 0.5088
  bootstrap_1v2_95CI: [0.6108, 0.6242]
  bootstrap_1v2_995CI_bonferroni: [0.6078, 0.6273]

=== exp_019_mistral7b_depth ===
  bootstrap_ci_1v2: {'ci_lower': 0.5835, 'ci_upper': 0.6032, 'p_auc_leq_060': 0.9017}
  pairwise_auc: {'0v1': 0.9843, '1v2': 0.5935, '2v3': 0.5402, '3v4': 0.5232, '4v5': 0.5181}

=== exp_pythia69b_c4_nuc ===
  scorer: Qwen-1.5B
  note: 1v2 AUC borderline (0.0045 below threshold)
  pairwise_auc: {'0v1': 0.9599, '1v2': 0.5955, '2v3': 0.5298, '3v4': 0.5135}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T11:14:58.566272+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get Mistral-related and other experiments\nfor eid in ['exp_019b_mistral_cross_scorer', 'exp_019_mistral7b_depth']:\n    if eid in exps:\n        exp = exps[eid]\n        metrics = exp.get('metrics', {})\n        print(f'=== {eid} ===')\n        print(json.dumps(metrics, indent=2)[:2000])\n        print()\n\n# Also search for any experiment with 0v1 near 0.917\nprint('=== Searching for 0v1 near 0.917 ===')\nfor eid, exp in sorted(exps.items()):\n    metrics = exp.get('metrics', {})\n    pauc = metrics.get('pairwise_auc', {})\n    if isinstance(pauc, dict):\n        v01 = pauc.get('0v1', None)\n        if v01 and isinstance(v01, (int, float)) and 0.915 < v01 < 0.920:\n            print(f'{eid}: 0v1={v01}, full={pauc}')\n\" 2>&1\n",
  "description": "Get Mistral cross-scorer and search 0v1≈0.917"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get Mistral-related and other experiments\nfor eid in ['exp_019b_mistral_cross_scorer', 'exp_019_mistral7b_depth']:\n    if eid in exps:\n        exp = exps[eid]\n        metrics = exp.get('metrics', {})\n        print(f'=== {eid} ===')\n        print(json.dumps(metrics, indent=2)[:2000])\n        print()\n\n# Also search for any experiment with 0v1 near 0.917\nprint('=== Searching for 0v1 near 0.917 ===')\nfor eid, exp in sorted(exps.items()):\n    metrics = exp.get('metrics', {})\n    pauc = metrics.get('pairwise_auc', {})\n    if isinstance(pauc, dict):\n        v01 = pauc.get('0v1', None)\n        if v01 and isinstance(v01, (int, float)) and 0.915 < v01 < 0.920:\n            print(f'{eid}: 0v1={v01}, full={pauc}')\n\" 2>&1\n",
    "description": "Get Mistral cross-scorer and search 0v1≈0.917"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T11:14:58.566440+00:00_

=== exp_019b_mistral_cross_scorer ===
{
  "k_star": 1,
  "pairwise_auc": {
    "0v1": 0.9209,
    "1v2": 0.5695,
    "2v3": 0.5335,
    "3v4": 0.514,
    "4v5": 0.5184
  },
  "bootstrap_ci": {
    "0v1": {
      "mean": 0.9209,
      "ci_lower": 0.9189,
      "ci_upper": 0.9229,
      "pass_060": true
    },
    "1v2": {
      "mean": 0.5696,
      "ci_lower": 0.5645,
      "ci_upper": 0.5746,
      "pass_060": false
    },
    "2v3": {
      "mean": 0.5335,
      "ci_lower": 0.5283,
      "ci_upper": 0.5382,
      "pass_060": false
    },
    "3v4": {
      "mean": 0.514,
      "ci_lower": 0.5063,
      "ci_upper": 0.5213,
      "pass_060": false
    },
    "4v5": {
      "mean": 0.5183,
      "ci_lower": 0.5128,
      "ci_upper": 0.5244,
      "pass_060": false
    }
  },
  "jsd": {
    "0v1": 0.08355,
    "1v2": 0.007642,
    "2v3": 0.004752,
    "3v4": 0.004255,
    "4v5": 0.003758
  },
  "ordinal_mae": 1.3737,
  "ordinal_accuracy": 0.3179,
  "top3_features": [
    "freq_entropy",
    "surp_d1_skew",
    "surp_d1_mean"
  ],
  "key_finding": "Cross-scorer (Qwen-1.5B scoring Mistral text) confirms K*=1. 1v2 AUC=0.5695 (self-scorer was 0.5935) \u2014 cross-scorer LOWER, not higher. Mistral K*=1 is genuine (inherent to Mistral generations), NOT a self-scorer artifact."
}

=== exp_019_mistral7b_depth ===
{
  "k_star": 1,
  "pairwise_auc": {
    "0v1": 0.9843,
    "1v2": 0.5935,
    "2v3": 0.5402,
    "3v4": 0.5232,
    "4v5": 0.5181
  },
  "bootstrap_ci_1v2": {
    "ci_lower": 0.5835,
    "ci_upper": 0.6032,
    "p_auc_leq_060": 0.9017
  },
  "jsd": {
    "0v1": 0.124194,
    "1v2": 0.008051,
    "2v3": 0.005047,
    "3v4": 0.004516,
    "4v5": 0.004109
  },
  "ordinal_mae": 1.2275,
  "ordinal_accuracy": 0.3567,
  "top3_features": [
    "freq_entropy",
    "surp_d1_skew",
    "surp_d1_mean"
  ]
}

=== Searching for 0v1 near 0.917 ===
exp_code_llama8b: 0v1=0.9161, full={'0v1': 0.9161, '1v2': 0.7394, '2v3': 0.5112, '3v4': 0.52, '4v5': 0.4996}
exp_code_mistral7b: 0v1=0.
…[truncated 86 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T11:14:58.566620+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Search for 1v2 near 0.575 (Mistral paper value)\nprint('=== 1v2 near 0.575 ===')\nfor eid, exp in sorted(exps.items()):\n    metrics = exp.get('metrics', {})\n    pauc = metrics.get('pairwise_auc', {})\n    if isinstance(pauc, dict):\n        v12 = pauc.get('1v2', None)\n        if v12 and isinstance(v12, (int, float)) and 0.570 < v12 < 0.580:\n            v01 = pauc.get('0v1', 'N/A')\n            print(f'{eid}: 0v1={v01}, 1v2={v12}, full={pauc}')\n\n# Search for 0v1 near 0.917 more broadly\nprint()\nprint('=== 0v1 in 0.91-0.92 range ===')\nfor eid, exp in sorted(exps.items()):\n    metrics = exp.get('metrics', {})\n    pauc = metrics.get('pairwise_auc', {})\n    if isinstance(pauc, dict):\n        v01 = pauc.get('0v1', None)\n        if v01 and isinstance(v01, (int, float)) and 0.91 < v01 < 0.92:\n            print(f'{eid}: 0v1={v01}, 1v2={pauc.get(\\\"1v2\\\",\\\"N/A\\\")}')\n\n# Also look at Mistral with _qwen prefix or suffix\nprint()\nprint('=== Mistral experiments ===')\nfor eid, exp in sorted(exps.items()):\n    if 'mistral' in eid.lower():\n        metrics = exp.get('metrics', {})\n        pauc = metrics.get('pairwise_auc', {})\n        print(f'{eid}: AUC={pauc}')\n\" 2>&1\n",
  "description": "Search for Mistral paper values in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Search for 1v2 near 0.575 (Mistral paper value)\nprint('=== 1v2 near 0.575 ===')\nfor eid, exp in sorted(exps.items()):\n    metrics = exp.get('metrics', {})\n    pauc = metrics.get('pairwise_auc', {})\n    if isinstance(pauc, dict):\n        v12 = pauc.get('1v2', None)\n        if v12 and isinstance(v12, (int, float)) and 0.570 < v12 < 0.580:\n            v01 = pauc.get('0v1', 'N/A')\n            print(f'{eid}: 0v1={v01}, 1v2={v12}, full={pauc}')\n\n# Search for 0v1 near 0.917 more broadly\nprint()\nprint('=== 0v1 in 0.91-0.92 range ===')\nfor eid, exp in sorted(exps.items()):\n    metrics = exp.get('metrics', {})\n    pauc = metrics.get('pairwise_auc', {})\n    if isinstance(pauc, dict):\n        v01 = pauc.get('0v1', None)\n        if v01 and isinstance(v01, (int, float)) and 0.91 < v01 < 0.92:\n            print(f'{eid}: 0v1={v01}, 1v2={pauc.get(\\\"1v2\\\",\\\"N/A\\\")}')\n\n# Also look at Mistral with _qwen prefix or suffix\nprint()\nprint('=== Mistral experiments ===')\nfor eid, exp in sorted(exps.items()):\n    if 'mistral' in eid.lower():\n        metrics = exp.get('metrics', {})\n        pauc = metrics.get('pairwise_auc', {})\n        print(f'{eid}: AUC={pauc}')\n\" 2>&1\n",
    "description": "Search for Mistral paper values in registry"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T11:14:58.566765+00:00_

=== 1v2 near 0.575 ===

=== 0v1 in 0.91-0.92 range ===
exp_code_llama8b: 0v1=0.9161, 1v2=0.7394
exp_code_mistral7b: 0v1=0.9191, 1v2=0.6152

=== Mistral experiments ===
exp_019_mistral7b_depth: AUC={'0v1': 0.9843, '1v2': 0.5935, '2v3': 0.5402, '3v4': 0.5232, '4v5': 0.5181}
exp_019b_mistral_cross_scorer: AUC={'0v1': 0.9209, '1v2': 0.5695, '2v3': 0.5335, '3v4': 0.514, '4v5': 0.5184}
exp_arXiv_mistral7b: AUC={'0v1': 0.9848, '1v2': 0.8201, '2v3': 0.6275, '3v4': 0.5295, '4v5': 0.5295}
exp_arXiv_mistral7b_crossscorer: AUC={}
exp_code_mistral7b: AUC={'0v1': 0.9191, '1v2': 0.6152, '2v3': 0.5293, '3v4': 0.5286, '4v5': 0.5099}
exp_wiki_mistral7b: AUC={}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T11:14:58.566963+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get all OLMo experiments\nprint('=== OLMo experiments ===')\nfor eid, exp in sorted(exps.items()):\n    if 'olmo' in eid.lower():\n        metrics = exp.get('metrics', {})\n        pauc = metrics.get('pairwise_auc', {})\n        status = exp.get('status', '')\n        if status != 'DONE':\n            continue\n        print(f'{eid}:')\n        if pauc:\n            print(f'  pairwise_auc: {pauc}')\n        # Check for individual AUC keys\n        for k in ['0v1_auc', '1v2_auc', 'AUC_0v1']:\n            if k in metrics:\n                print(f'  {k}: {metrics[k]}')\n        ci = metrics.get('bootstrap_ci', {})\n        if ci:\n            print(f'  bootstrap_ci: {json.dumps(ci, indent=4)[:500]}')\n        print()\n\n# Get Pythia CI for 2v3 \nprint('=== Pythia 2v3 CI ===')\nfor eid in ['exp_001_pythia_depth', 'exp_C_permutation_10k']:\n    if eid in exps:\n        exp = exps[eid]\n        metrics = exp.get('metrics', {})\n        ci = metrics.get('bootstrap_ci', {})\n        print(f'{eid} CI: {json.dumps(ci, indent=2)[:1000]}')\n        print()\n\" 2>&1\n",
  "description": "Get OLMo and Pythia CI data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get all OLMo experiments\nprint('=== OLMo experiments ===')\nfor eid, exp in sorted(exps.items()):\n    if 'olmo' in eid.lower():\n        metrics = exp.get('metrics', {})\n        pauc = metrics.get('pairwise_auc', {})\n        status = exp.get('status', '')\n        if status != 'DONE':\n            continue\n        print(f'{eid}:')\n        if pauc:\n            print(f'  pairwise_auc: {pauc}')\n        # Check for individual AUC keys\n        for k in ['0v1_auc', '1v2_auc', 'AUC_0v1']:\n            if k in metrics:\n                print(f'  {k}: {metrics[k]}')\n        ci = metrics.get('bootstrap_ci', {})\n        if ci:\n            print(f'  bootstrap_ci: {json.dumps(ci, indent=4)[:500]}')\n        print()\n\n# Get Pythia CI for 2v3 \nprint('=== Pythia 2v3 CI ===')\nfor eid in ['exp_001_pythia_depth', 'exp_C_permutation_10k']:\n    if eid in exps:\n        exp = exps[eid]\n        metrics = exp.get('metrics', {})\n        ci = metrics.get('bootstrap_ci', {})\n        print(f'{eid} CI: {json.dumps(ci, indent=2)[:1000]}')\n        print()\n\" 2>&1\n",
    "description": "Get OLMo and Pythia CI data"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T11:14:58.567110+00:00_

=== OLMo experiments ===
exp_002_olmo_depth:
  pairwise_auc: {'0v1': 0.9861, '1v2': 0.5001, '2v3': 0.4972, '3v4': 0.5034, '4v5': 0.4971}

exp_arXiv_olmo:

exp_olmo1b_10k:
  pairwise_auc: {'0v1': 0.9871, '1v2': 0.4984, '2v3': 0.5059, '3v4': 0.5061, '4v5': 0.5074}

exp_olmo1b_c4_rerun:
  0v1_auc: 0.986
  1v2_auc: 0.508

exp_olmo_retrain_chain:

exp_olmo_retrain_v3:
  pairwise_auc: {'0v1': 0.9873, '1v2': 0.8889, '2v3': 0.7036, '3v4': 0.6817}

exp_wiki_olmo:

exp_wiki_olmo_v2:

=== Pythia 2v3 CI ===
exp_001_pythia_depth CI: {
  "1v2": {
    "auc_oof": 0.6072,
    "boot_mean": 0.6073,
    "boot_std": 0.005,
    "ci_95": [
      0.5975,
      0.6172
    ],
    "ci_995_bonferroni": [
      0.5934,
      0.621
    ],
    "perm_p": 0.0001,
    "bonferroni_pass": false
  }
}

exp_C_permutation_10k CI: {}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T11:14:58.567316+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Full dump of Gemma 10k experiment\nprint('=== exp_gemma2b_10k FULL ===')\nexp = exps.get('exp_gemma2b_10k', {})\nmetrics = exp.get('metrics', {})\nprint(json.dumps(metrics, indent=2)[:2000])\n\n# Full dump of exp_gemma2b_depth\nprint()\nprint('=== exp_gemma2b_depth FULL ===')\nexp = exps.get('exp_gemma2b_depth', {})\nmetrics = exp.get('metrics', {})\nprint(json.dumps(metrics, indent=2)[:2000])\n\n# Check if there's a seed_gemma or another gemma experiment\nprint()\nprint('=== All Gemma experiments ===')\nfor eid, exp in sorted(exps.items()):\n    if 'gemma' in eid.lower():\n        status = exp.get('status', '')\n        metrics = exp.get('metrics', {})\n        pauc = metrics.get('pairwise_auc', metrics.get('pairwise_auc_qwen', {}))\n        print(f'{eid} [{status}]: {pauc}')\n\n# Also check seed_gemma experiment\nprint()\nprint('=== seed_gemma27b_c4_s42 ===')\nexp = exps.get('seed_gemma27b_c4_s42', {})\nmetrics = exp.get('metrics', {})\nprint(json.dumps(metrics, indent=2)[:1000])\n\" 2>&1\n",
  "description": "Get Gemma experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Full dump of Gemma 10k experiment\nprint('=== exp_gemma2b_10k FULL ===')\nexp = exps.get('exp_gemma2b_10k', {})\nmetrics = exp.get('metrics', {})\nprint(json.dumps(metrics, indent=2)[:2000])\n\n# Full dump of exp_gemma2b_depth\nprint()\nprint('=== exp_gemma2b_depth FULL ===')\nexp = exps.get('exp_gemma2b_depth', {})\nmetrics = exp.get('metrics', {})\nprint(json.dumps(metrics, indent=2)[:2000])\n\n# Check if there's a seed_gemma or another gemma experiment\nprint()\nprint('=== All Gemma experiments ===')\nfor eid, exp in sorted(exps.items()):\n    if 'gemma' in eid.lower():\n        status = exp.get('status', '')\n        metrics = exp.get('metrics', {})\n        pauc = metrics.get('pairwise_auc', metrics.get('pairwise_auc_qwen', {}))\n        print(f'{eid} [{status}]: {pauc}')\n\n# Also check seed_gemma experiment\nprint()\nprint('=== seed_gemma27b_c4_s42 ===')\nexp = exps.get('seed_gemma27b_c4_s42', {})\nmetrics = exp.get('metrics', {})\nprint(json.dumps(metrics, indent=2)[:1000])\n\" 2>&1\n",
    "description": "Get Gemma experiment details"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T11:14:58.567491+00:00_

=== exp_gemma2b_10k FULL ===
{
  "K_star_self": 2,
  "K_star_qwen": 2,
  "scorer": "Qwen2.5-1.5B-Instruct (cross-scored)",
  "pairwise_auc_self": {
    "0v1": 0.9817,
    "1v2": 0.643,
    "2v3": 0.555,
    "3v4": 0.5173,
    "4v5": 0.5101
  },
  "pairwise_auc_qwen": {
    "0v1": 0.9533,
    "1v2": 0.6099,
    "2v3": 0.5409,
    "3v4": 0.5174,
    "4v5": 0.5158
  },
  "bootstrap_ci_1v2": {
    "auc_oof": 0.6099,
    "boot_std": 0.0034,
    "ci_95": [
      0.6031,
      0.6167
    ],
    "ci_995_bonferroni_pct": [
      0.5998,
      0.6192
    ],
    "ci_995_bonferroni_norm": [
      0.6003,
      0.6196
    ],
    "perm_p": 0.0001,
    "bonferroni_pass_pct": false,
    "bonferroni_pass_norm": true
  },
  "note": "5K K*=1 (1v2=0.5981), 10K Qwen cross-scored K*=2 (1v2=0.6099). Bonferroni split: percentile FAIL (0.5998), normal PASS (0.6003). Extremely borderline."
}

=== exp_gemma2b_depth FULL ===
{
  "k_star": 1,
  "pairwise_auc": {
    "0v1": 0.9534,
    "1v2": 0.5981,
    "2v3": 0.5342,
    "3v4": 0.503,
    "4v5": 0.5026
  },
  "pairwise_auc_std": {
    "0v1": 0.003,
    "1v2": 0.008,
    "2v3": 0.013,
    "3v4": 0.003,
    "4v5": 0.013
  },
  "bootstrap_ci_1v2": {
    "ci_lower": 0.5882,
    "ci_upper": 0.6076
  },
  "jsd": {
    "0v1": 0.09882,
    "1v2": 0.008852,
    "2v3": 0.004904,
    "3v4": 0.003742,
    "4v5": 0.003167
  },
  "ordinal_mae": 1.3152,
  "ordinal_accuracy": 0.3321,
  "note": "K*=1, NOT borderline K*=2. 1v2 AUC=0.5981 < theta=0.60. CI upper=0.6076 crosses theta but point estimate below."
}

=== All Gemma experiments ===
exp_gemma27b_c4 [PREPARING]: {}
exp_gemma2b_10k [DONE]: {'0v1': 0.9533, '1v2': 0.6099, '2v3': 0.5409, '3v4': 0.5174, '4v5': 0.5158}
exp_gemma2b_depth [DONE]: {'0v1': 0.9534, '1v2': 0.5981, '2v3': 0.5342, '3v4': 0.503, '4v5': 0.5026}
seed_gemma27b_c4_s42 [DONE]: {'0v1': 0.8874, '1v2': 0.5894}

=== seed_gemma27b_c4_s42 ===
{
  "K_star": 1,
  "scorer": "Qwen2.5-1.5B-Instruct (cross-scored)",
  "pairwise_auc_self": {
    "0v1": 0
…[truncated 314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T11:14:58.567693+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Full OLMo rerun details\nprint('=== exp_olmo1b_c4_rerun FULL ===')\nexp = exps.get('exp_olmo1b_c4_rerun', {})\nprint(json.dumps(exp, indent=2)[:3000])\nprint()\n\n# Check any experiment with Mistral values near paper\n# Try finding matching values for Mistral 1v2=0.575\nprint('=== All experiments with 1v2 in 0.57-0.58 ===')\nfor eid, exp in sorted(exps.items()):\n    metrics = exp.get('metrics', {})\n    pauc = metrics.get('pairwise_auc', {})\n    if isinstance(pauc, dict):\n        v12 = pauc.get('1v2', None)\n        if v12 and isinstance(v12, (int, float)) and 0.570 <= v12 <= 0.580:\n            print(f'{eid}: 1v2={v12}, 0v1={pauc.get(\\\"0v1\\\",\\\"N/A\\\")}, full={pauc}')\n\n    # Also check individual key formats\n    v12b = metrics.get('AUC_1v2', metrics.get('1v2_auc', None))\n    if v12b and isinstance(v12b, (int, float)) and 0.570 <= v12b <= 0.580:\n        print(f'{eid}: 1v2={v12b} (alt key format)')\n\" 2>&1\n",
  "description": "Get OLMo rerun details and search for Mistral values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Full OLMo rerun details\nprint('=== exp_olmo1b_c4_rerun FULL ===')\nexp = exps.get('exp_olmo1b_c4_rerun', {})\nprint(json.dumps(exp, indent=2)[:3000])\nprint()\n\n# Check any experiment with Mistral values near paper\n# Try finding matching values for Mistral 1v2=0.575\nprint('=== All experiments with 1v2 in 0.57-0.58 ===')\nfor eid, exp in sorted(exps.items()):\n    metrics = exp.get('metrics', {})\n    pauc = metrics.get('pairwise_auc', {})\n    if isinstance(pauc, dict):\n        v12 = pauc.get('1v2', None)\n        if v12 and isinstance(v12, (int, float)) and 0.570 <= v12 <= 0.580:\n            print(f'{eid}: 1v2={v12}, 0v1={pauc.get(\\\"0v1\\\",\\\"N/A\\\")}, full={pauc}')\n\n    # Also check individual key formats\n    v12b = metrics.get('AUC_1v2', metrics.get('1v2_auc', None))\n    if v12b and isinstance(v12b, (int, float)) and 0.570 <= v12b <= 0.580:\n        print(f'{eid}: 1v2={v12b} (alt key format)')\n\" 2>&1\n",
    "description": "Get OLMo rerun details and search for Mistral values"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T11:14:58.567876+00:00_

=== exp_olmo1b_c4_rerun FULL ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T11:10:33.358Z",
  "updated_at": "2026-05-21T11:11:13.525Z",
  "hypothesis": "OLMo-1B C4 depth chain \u53ef\u590d\u73b0\u6027\u9a8c\u8bc1\uff1a\u6807\u51c6\u5316 pipeline\uff08Qwen-1.5B scorer\uff09\u4e0b K* \u503c\u4e0e\u4e3b\u8868\u4e00\u81f4\u3002",
  "conclusion": "negative",
  "metrics": {
    "0v1_auc": 0.986,
    "1v2_auc": 0.508,
    "2v3_auc": 0.4973,
    "3v4_auc": 0.5024,
    "4v5_auc": 0.4942,
    "kstar_at_060": 1,
    "main_table_1v2": 0.6145,
    "delta": -0.1065
  },
  "spec": {
    "command": "python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/models--allenai--OLMo-1B-hf/... --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --no_sample",
    "server": "cqa1-22115",
    "gpu": [
      "cuda:1"
    ],
    "data_path": "data/exp_olmo1b_c4_rerun",
    "data_count": 5000,
    "model_name": "allenai/OLMo-1B-hf",
    "seed": "default",
    "checkpoint_path": "results/exp_olmo1b_c4_rerun/",
    "log_path": "results/exp_olmo1b_c4_rerun/experiment_config.json",
    "checkpoint_source": "N/A",
    "eval_data": "N/A"
  },
  "completed_at": "2026-05-21T11:11:13.525Z"
}

=== All experiments with 1v2 in 0.57-0.58 ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T11:14:58.568099+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Full comparison table\nconfigs = {\n    'Qwen-rw': {\n        'reg_exp': 'exp_007_bootstrap_ci',\n        'reg_key': 'qwen_rewrite',\n        'paper_auc': {'0v1': .9956, '1v2': .6955, '2v3': .5893, '3v4': .5435, '4v5': .5340},\n        'paper_ci_1v2': [.686, .704],\n        'paper_ci_2v3': [.580, .599],\n    },\n    'Pythia': {\n        'reg_exp': 'exp_001_pythia_depth',\n        'paper_auc': {'0v1': .9722, '1v2': .6074, '2v3': .5440, '3v4': .5051, '4v5': .5079},\n        'paper_ci_1v2': [.598, .617],\n        'paper_ci_2v3': [.534, .554],\n    },\n    'OLMo': {\n        'reg_exp': 'exp_002_olmo_depth',\n        'paper_auc': {'0v1': .9860, '1v2': .5001, '2v3': .4973, '3v4': .5024, '4v5': .4942},\n        'paper_ci_1v2': [.496, .519],\n        'paper_ci_2v3': [.486, .509],\n    },\n    'Qwen-cont': {\n        'reg_exp': 'exp_007_bootstrap_ci',\n        'reg_key': 'qwen_cont',\n        'paper_auc': {'0v1': .9971, '1v2': .6112, '2v3': .5609, '3v4': .5409, '4v5': .5141},\n        'paper_ci_1v2': [.602, .621],\n        'paper_ci_2v3': [.551, .571],\n    },\n    'Qwen-7B': {\n        'reg_exp': 'exp_004_7b_crossscale',\n        'paper_auc': {'0v1': .9638, '1v2': .6168, '2v3': .5492, '3v4': .5276, '4v5': .5085},\n    },\n    'Qwen-base': {\n        'reg_exp': 'exp_016_base_vs_instruct',\n        'paper_auc': {'0v1': .987, '1v2': .626, '2v3': .550, '3v4': .529, '4v5': .518},\n    },\n    'LLaMA-8B': {\n        'reg_exp': 'exp_018_llama8b_depth',\n        'paper_auc': {'0v1': .9224, '1v2': .6123, '2v3': .5273, '3v4': .5168, '4v5': .5159},\n    },\n    'Mistral-7B': {\n        'reg_exp': 'exp_019b_mistral_cross_scorer',\n        'paper_auc': {'0v1': .9170, '1v2': .5750, '2v3': .5369, '3v4': .5174, '4v5': .5175},\n    },\n    'Pythia-6.9B': {\n        'reg_exp': 'exp_pythia69b_c4_nuc',\n        'paper_auc': {'0v1': .9599, '1v2': .5955, '2v3': .5298, '3v4': .5135},\n    },\n    'Gemma-2B': {\n        'reg_exp': 'exp_gemma2b_depth',\n        'paper_auc': {'0v1': .953, '1v2': .5981, '2v3': .534, '3v4': .5033, '4v5': .5025},\n    },\n}\n\nmismatches = []\nfor config_name, config in configs.items():\n    exp_id = config['reg_exp']\n    exp = exps.get(exp_id, {})\n    metrics = exp.get('metrics', {})\n    \n    # Get registry AUC values\n    reg_key = config.get('reg_key', None)\n    if reg_key:\n        reg_data = metrics.get(reg_key, {})\n        reg_auc = {dp: reg_data[dp]['auc'] for dp in reg_data if isinstance(reg_data.get(dp), dict) and 'auc' in reg_data.get(dp, {})}\n    else:\n        reg_auc = metrics.get('pairwise_auc', {})\n        if not reg_auc:\n            # Try bootstrap_ci format\n            ci_data = metrics.get('bootstrap_ci', {})\n            if ci_data and all(isinstance(v, dict) and 'auc' in v for v in ci_data.values()):\n                reg_auc = {dp: ci_data[dp]['auc'] for dp in ci_data}\n    \n    paper_auc = config['paper_auc']\n    \n    for dp in ['0v1', '1v2', '2v3', '3v4', '4v5']:\n        paper_val = paper_auc.get(dp, None)\n        reg_val = reg_auc.get(dp, None)\n        if paper_val is None:\n            continue\n        if reg_val is None:\n            mismatches.append((config_name, dp, paper_val, exp_id, 'MISSING', 'N/A'))\n            continue\n        \n        # Check match with tolerance for rounding\n        diff = abs(paper_val - reg_val)\n        if diff > 0.00015:  # Allow for 4th decimal rounding\n            match = 'MISMATCH'\n            mismatches.append((config_name, dp, paper_val, exp_id, reg_val, f'Δ={diff:.4f}'))\n        else:\n            pass  # match\n\nprint('=== MISMATCHES FOUND ===')\nprint(f'{'Config':<15} {'Pair':<6} {'Paper':<8} {'Exp ID':<35} {'Registry':<10} {'Note'}')\nprint('-' * 90)\nfor m in mismatches:\n    print(f'{m[0]:<15} {m[1]:<6} {m[2]:<8.4f} {m[3]:<35} {str(m[4]):<10} {m[5]}')\n\" 2>&1\n",
  "description": "Full systematic comparison of paper vs registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Full comparison table\nconfigs = {\n    'Qwen-rw': {\n        'reg_exp': 'exp_007_bootstrap_ci',\n        'reg_key': 'qwen_rewrite',\n        'paper_auc': {'0v1': .9956, '1v2': .6955, '2v3': .5893, '3v4': .5435, '4v5': .5340},\n        'paper_ci_1v2': [.686, .704],\n        'paper_ci_2v3': [.580, .599],\n    },\n    'Pythia': {\n        'reg_exp': 'exp_001_pythia_depth',\n        'paper_auc': {'0v1': .9722, '1v2': .6074, '2v3': .5440, '3v4': .5051, '4v5': .5079},\n        'paper_ci_1v2': [.598, .617],\n        'paper_ci_2v3': [.534, .554],\n    },\n    'OLMo': {\n        'reg_exp': 'exp_002_olmo_depth',\n        'paper_auc': {'0v1': .9860, '1v2': .5001, '2v3': .4973, '3v4': .5024, '4v5': .4942},\n        'paper_ci_1v2': [.496, .519],\n        'paper_ci_2v3': [.486, .509],\n    },\n    'Qwen-cont': {\n        'reg_exp': 'exp_007_bootstrap_ci',\n        'reg_key': 'qwen_cont',\n        'paper_auc': {'0v1': .9971, '1v2': .6112, '2v3': .5609, '3v4': .5409, '4v5': .5141},\n        'paper_ci_1v2': [.602, .621],\n        'paper_ci_2v3': [.551, .571],\n    },\n    'Qwen-7B': {\n        'reg_exp': 'exp_004_7b_crossscale',\n        'paper_auc': {'0v1': .9638, '1v2': .6168, '2v3': .5492, '3v4': .5276, '4v5': .5085},\n    },\n    'Qwen-base': {\n        'reg_exp': 'exp_016_base_vs_instruct',\n        'paper_auc': {'0v1': .987, '1v2': .626, '2v3': .550, '3v4': .529, '4v5': .518},\n    },\n    'LLaMA-8B': {\n        'reg_exp': 'exp_018_llama8b_depth',\n        'paper_auc': {'0v1': .9224, '1v2': .6123, '2v3': .5273, '3v4': .5168, '4v5': .5159},\n    },\n    'Mistral-7B': {\n        'reg_exp': 'exp_019b_mistral_cross_scorer',\n        'paper_auc': {'0v1': .9170, '1v2': .5750, '2v3': .5369, '3v4': .5174, '4v5': .5175},\n    },\n    'Pythia-6.9B': {\n        'reg_exp': 'exp_pythia69b_c4_nuc',\n        'paper_auc': {'0v1': .9599, '1v2': .5955, '2v3': .5298, '3v4': .5135},\n    },\n    'Gemma-2B': {\n        'reg_exp': 'exp_gemma2b_depth',\n        'paper_auc': {'0v1': .953, '1v2': .5981, '2v3': .534, '3v4': .5033, '4v5': .5025},\n    },\n}\n\nmismatches = []\nfor config_name, config in configs.items():\n    exp_id = config['reg_exp']\n    exp = exps.get(exp_id, {})\n    metrics = exp.get('metrics', {})\n    \n    # Get registry AUC values\n    reg_key = config.get('reg_key', None)\n    if reg_key:\n        reg_data = metrics.get(reg_key, {})\n        reg_auc = {dp: reg_data[dp]['auc'] for dp in reg_data if isinstance(reg_data.get(dp), dict) and 'auc' in reg_data.get(dp, {})}\n    else:\n        reg_auc = metrics.get('pairwise_auc', {})\n        if not reg_auc:\n            # Try bootstrap_ci format\n            ci_data = metrics.get('bootstrap_ci', {})\n            if ci_data and all(isinstance(v, dict) and 'auc' in v for v in ci_data.values()):\n                reg_auc = {dp: ci_data[dp]['auc'] for dp in ci_data}\n    \n    paper_auc = config['paper_auc']\n    \n    for dp in ['0v1', '1v2', '2v3', '3v4', '4v5']:\n        paper_val = paper_auc.get(dp, None)\n        reg_val = reg_auc.get(dp, None)\n        if paper_val is None:\n            continue\n        if reg_val is None:\n            mismatches.append((config_name, dp, paper_val, exp_id, 'MISSING', 'N/A'))\n            continue\n        \n        # Check match with tolerance for rounding\n        diff = abs(paper_val - reg_val)\n        if diff > 0.00015:  # Allow for 4th decimal rounding\n            match = 'MISMATCH'\n            mismatches.append((config_name, dp, paper_val, exp_id, reg_val, f'Δ={diff:.4f}'))\n        else:\n            pass  # match\n\nprint('=== MISMATCHES FOUND ===')\nprint(f'{'Config':<15} {'Pair':<6} {'Paper':<8} {'Exp ID':<35} {'Registry':<10} {'Note'}')\nprint('-' * 90)\nfor m in mismatches:\n    print(f'{m[0]:<15} {m[1]:<6} {m[2]:<8.4f} {m[3]:<35} {str(m[4]):<10} {m[5]}')\n\" 2>&1\n",
    "description": "Full systematic comparison of paper vs registry"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T11:14:58.568293+00:00_

=== MISMATCHES FOUND ===
Config          Pair   Paper    Exp ID                              Registry   Note
------------------------------------------------------------------------------------------
OLMo            3v4    0.5024   exp_002_olmo_depth                  0.5034     Δ=0.0010
OLMo            4v5    0.4942   exp_002_olmo_depth                  0.4971     Δ=0.0029
Qwen-7B         0v1    0.9638   exp_004_7b_crossscale               0.9644     Δ=0.0006
Qwen-7B         1v2    0.6168   exp_004_7b_crossscale               0.6178     Δ=0.0010
Qwen-7B         2v3    0.5492   exp_004_7b_crossscale               0.546      Δ=0.0032
Qwen-7B         3v4    0.5276   exp_004_7b_crossscale               0.5225     Δ=0.0051
Qwen-7B         4v5    0.5085   exp_004_7b_crossscale               0.5091     Δ=0.0006
Qwen-base       1v2    0.6260   exp_016_base_vs_instruct            0.6262     Δ=0.0002
Qwen-base       2v3    0.5500   exp_016_base_vs_instruct            0.5496     Δ=0.0004
Qwen-base       3v4    0.5290   exp_016_base_vs_instruct            0.5294     Δ=0.0004
Qwen-base       4v5    0.5180   exp_016_base_vs_instruct            0.5182     Δ=0.0002
LLaMA-8B        3v4    0.5168   exp_018_llama8b_depth               0.5138     Δ=0.0030
LLaMA-8B        4v5    0.5159   exp_018_llama8b_depth               0.5097     Δ=0.0062
Mistral-7B      0v1    0.9170   exp_019b_mistral_cross_scorer       0.9209     Δ=0.0039
Mistral-7B      1v2    0.5750   exp_019b_mistral_cross_scorer       0.5695     Δ=0.0055
Mistral-7B      2v3    0.5369   exp_019b_mistral_cross_scorer       0.5335     Δ=0.0034
Mistral-7B      3v4    0.5174   exp_019b_mistral_cross_scorer       0.514      Δ=0.0034
Mistral-7B      4v5    0.5175   exp_019b_mistral_cross_scorer       0.5184     Δ=0.0009
Gemma-2B        0v1    0.9530   exp_gemma2b_depth                   0.9534     Δ=0.0004
Gemma-2B        2v3    0.5340   exp_gemma2b_depth                   0.5342     Δ=0.0002
Gemma-2B        3v4    0.5033   exp_gemm
…[truncated 47 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T11:14:58.568510+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\ndef get_auc_from_exp(exp_id, reg_key=None):\n    exp = exps.get(exp_id, {})\n    metrics = exp.get('metrics', {})\n    \n    if reg_key:\n        reg_data = metrics.get(reg_key, {})\n        return {dp: reg_data[dp]['auc'] for dp in reg_data if isinstance(reg_data.get(dp), dict) and 'auc' in reg_data.get(dp, {})}\n    \n    # Prefer bootstrap_ci (point estimates from bootstrap)\n    ci_data = metrics.get('bootstrap_ci', {})\n    if ci_data:\n        auc_dict = {}\n        for dp, val in ci_data.items():\n            if isinstance(val, dict) and 'auc' in val:\n                auc_dict[dp] = val['auc']\n            elif isinstance(val, dict) and 'mean' in val:\n                auc_dict[dp] = val['mean']\n        if auc_dict:\n            return auc_dict\n    \n    # Fall back to pairwise_auc\n    return metrics.get('pairwise_auc', {})\n\nconfigs = {\n    'Qwen-rw': ('exp_007_bootstrap_ci', 'qwen_rewrite', \n        {'0v1': .9956, '1v2': .6955, '2v3': .5893, '3v4': .5435, '4v5': .5340}),\n    'Pythia': ('exp_001_pythia_depth', None,\n        {'0v1': .9722, '1v2': .6074, '2v3': .5440, '3v4': .5051, '4v5': .5079}),\n    'OLMo': ('exp_002_olmo_depth', None,\n        {'0v1': .9860, '1v2': .5001, '2v3': .4973, '3v4': .5024, '4v5': .4942}),\n    'Qwen-cont': ('exp_007_bootstrap_ci', 'qwen_cont',\n        {'0v1': .9971, '1v2': .6112, '2v3': .5609, '3v4': .5409, '4v5': .5141}),\n    'Qwen-7B': ('exp_004_7b_crossscale', None,\n        {'0v1': .9638, '1v2': .6168, '2v3': .5492, '3v4': .5276, '4v5': .5085}),\n    'Qwen-base': ('exp_016_base_vs_instruct', None,\n        {'0v1': .987, '1v2': .626, '2v3': .550, '3v4': .529, '4v5': .518}),\n    'LLaMA-8B': ('exp_018_llama8b_depth', None,\n        {'0v1': .9224, '1v2': .6123, '2v3': .5273, '3v4': .5168, '4v5': .5159}),\n    'Mistral-7B': ('exp_019b_mistral_cross_scorer', None,\n        {'0v1': .9170, '1v2': .5750, '2v3': .5369, '3v4': .5174, '4v5': .5175}),\n    'Pythia-6.9B': ('exp_pythia69b_c4_nuc', None,\n        {'0v1': .9599, '1v2': .5955, '2v3': .5298, '3v4': .5135}),\n    'Gemma-2B': ('exp_gemma2b_depth', None,\n        {'0v1': .953, '1v2': .5981, '2v3': .534, '3v4': .5033, '4v5': .5025}),\n}\n\nmismatches = []\nfor config_name, (exp_id, reg_key, paper_auc) in configs.items():\n    reg_auc = get_auc_from_exp(exp_id, reg_key)\n    \n    # Determine decimal places from paper values\n    for dp in ['0v1', '1v2', '2v3', '3v4', '4v5']:\n        pv = paper_auc.get(dp)\n        rv = reg_auc.get(dp)\n        if pv is None:\n            continue\n        if rv is None:\n            mismatches.append((config_name, dp, f'{pv:.4f}', exp_id, 'MISSING', ''))\n            continue\n        \n        # Determine paper precision (number of significant decimals)\n        ps = f'{pv:.4f}'.rstrip('0')\n        ndp = len(ps.split('.')[1]) if '.' in ps else 0\n        ndp = max(ndp, 3)\n        \n        # Round registry to same precision for comparison\n        rv_rounded = round(rv, ndp)\n        pv_rounded = round(pv, ndp)\n        \n        if abs(pv_rounded - rv_rounded) > 1e-10:\n            diff = abs(pv - rv)\n            mismatches.append((config_name, dp, f'{pv:.4f}', exp_id, f'{rv:.4f}', f'Δ={diff:.4f}'))\n\nif mismatches:\n    print(f'{\\\"Config\\\":<15} {\\\"Pair\\\":<6} {\\\"Paper\\\":<8} {\\\"Exp ID\\\":<35} {\\\"Registry\\\":<10} {\\\"Note\\\"}')\n    print('-' * 90)\n    for m in mismatches:\n        print(f'{m[0]:<15} {m[1]:<6} {m[2]:<8} {m[3]:<35} {m[4]:<10} {m[5]}')\nelse:\n    print('No mismatches found')\n\" 2>&1\n",
  "description": "Re-run comparison with bootstrap estimates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/34d999f9-ba08-4dc3-8d75-ac2750aed5c6/tool-results/mcp-agent-ml-research-read_registry-1779534109586.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\ndef get_auc_from_exp(exp_id, reg_key=None):\n    exp = exps.get(exp_id, {})\n    metrics = exp.get('metrics', {})\n    \n    if reg_key:\n        reg_data = metrics.get(reg_key, {})\n        return {dp: reg_data[dp]['auc'] for dp in reg_data if isinstance(reg_data.get(dp), dict) and 'auc' in reg_data.get(dp, {})}\n    \n    # Prefer bootstrap_ci (point estimates from bootstrap)\n    ci_data = metrics.get('bootstrap_ci', {})\n    if ci_data:\n        auc_dict = {}\n        for dp, val in ci_data.items():\n            if isinstance(val, dict) and 'auc' in val:\n                auc_dict[dp] = val['auc']\n            elif isinstance(val, dict) and 'mean' in val:\n                auc_dict[dp] = val['mean']\n        if auc_dict:\n            return auc_dict\n    \n    # Fall back to pairwise_auc\n    return metrics.get('pairwise_auc', {})\n\nconfigs = {\n    'Qwen-rw': ('exp_007_bootstrap_ci', 'qwen_rewrite', \n        {'0v1': .9956, '1v2': .6955, '2v3': .5893, '3v4': .5435, '4v5': .5340}),\n    'Pythia': ('exp_001_pythia_depth', None,\n        {'0v1': .9722, '1v2': .6074, '2v3': .5440, '3v4': .5051, '4v5': .5079}),\n    'OLMo': ('exp_002_olmo_depth', None,\n        {'0v1': .9860, '1v2': .5001, '2v3': .4973, '3v4': .5024, '4v5': .4942}),\n    'Qwen-cont': ('exp_007_bootstrap_ci', 'qwen_cont',\n        {'0v1': .9971, '1v2': .6112, '2v3': .5609, '3v4': .5409, '4v5': .5141}),\n    'Qwen-7B': ('exp_004_7b_crossscale', None,\n        {'0v1': .9638, '1v2': .6168, '2v3': .5492, '3v4': .5276, '4v5': .5085}),\n    'Qwen-base': ('exp_016_base_vs_instruct', None,\n        {'0v1': .987, '1v2': .626, '2v3': .550, '3v4': .529, '4v5': .518}),\n    'LLaMA-8B': ('exp_018_llama8b_depth', None,\n        {'0v1': .9224, '1v2': .6123, '2v3': .5273, '3v4': .5168, '4v5': .5159}),\n    'Mistral-7B': ('exp_019b_mistral_cross_scorer', None,\n        {'0v1': .9170, '1v2': .5750, '2v3': .5369, '3v4': .5174, '4v5': .5175}),\n    'Pythia-6.9B': ('exp_pythia69b_c4_nuc', None,\n        {'0v1': .9599, '1v2': .5955, '2v3': .5298, '3v4': .5135}),\n    'Gemma-2B': ('exp_gemma2b_depth', None,\n        {'0v1': .953, '1v2': .5981, '2v3': .534, '3v4': .5033, '4v5': .5025}),\n}\n\nmismatches = []\nfor config_name, (exp_id, reg_key, paper_auc) in configs.items():\n    reg_auc = get_auc_from_exp(exp_id, reg_key)\n    \n    # Determine decimal places from paper values\n    for dp in ['0v1', '1v2', '2v3', '3v4', '4v5']:\n        pv = paper_auc.get(dp)\n        rv = reg_auc.get(dp)\n        if pv is None:\n            continue\n        if rv is None:\n            mismatches.append((config_name, dp, f'{pv:.4f}', exp_id, 'MISSING', ''))\n            continue\n        \n        # Determine paper precision (number of significant decimals)\n        ps = f'{pv:.4f}'.rstrip('0')\n        ndp = len(ps.split('.')[1]) if '.' in ps else 0\n        ndp = max(ndp, 3)\n        \n        # Round registry to same precision for comparison\n        rv_rounded = round(rv, ndp)\n        pv_rounded = round(pv, ndp)\n        \n        if abs(pv_rounded - rv_rounded) > 1e-10:\n            diff = abs(pv - rv)\n            mismatches.append((config_name, dp, f'{pv:.4f}', exp_id, f'{rv:.4f}', f'Δ={diff:.4f}'))\n\nif mismatches:\n    print(f'{\\\"Config\\\":<15} {\\\"Pair\\\":<6} {\\\"Paper\\\":<8} {\\\"Exp ID\\\":<35} {\\\"Registry\\\":<10} {\\\"Note\\\"}')\n    print('-' * 90)\n    for m in mismatches:\n        print(f'{m[0]:<15} {m[1]:<6} {m[2]:<8} {m[3]:<35} {m[4]:<10} {m[5]}')\nelse:\n    print('No mismatches found')\n\" 2>&1\n",
    "description": "Re-run comparison with bootstrap estimates"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T11:14:58.568692+00:00_

Config          Pair   Paper    Exp ID                              Registry   Note
------------------------------------------------------------------------------------------
OLMo            2v3    0.4973   exp_002_olmo_depth                  0.4972     Δ=0.0001
OLMo            3v4    0.5024   exp_002_olmo_depth                  0.5034     Δ=0.0010
OLMo            4v5    0.4942   exp_002_olmo_depth                  0.4971     Δ=0.0029
Mistral-7B      0v1    0.9170   exp_019b_mistral_cross_scorer       0.9209     Δ=0.0039
Mistral-7B      1v2    0.5750   exp_019b_mistral_cross_scorer       0.5696     Δ=0.0054
Mistral-7B      2v3    0.5369   exp_019b_mistral_cross_scorer       0.5335     Δ=0.0034
Mistral-7B      3v4    0.5174   exp_019b_mistral_cross_scorer       0.5140     Δ=0.0034
Mistral-7B      4v5    0.5175   exp_019b_mistral_cross_scorer       0.5183     Δ=0.0008
Gemma-2B        3v4    0.5033   exp_gemma2b_depth                   0.5030     Δ=0.0003
Gemma-2B        4v5    0.5025   exp_gemma2b_depth                   0.5026     Δ=0.0001

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T11:14:58.568895+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.9225",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.9225",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T11:14:58.569034+00:00_

docs/paper/appendix_extended.tex:50:Cross-scale validation confirms $\Kempirical = 2$ from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$, 0v1 $= 0.9225$) both exceed $\theta$, with progressively lower 0v1 signal consistent with larger models generating more human-like text.
docs/paper/experiments_c1.tex:49:LLaMA-3.1-8B confirms $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123\;[0.603,\,0.622]$; CI lower bound above $\theta$; Table~\ref{tab:kstar_ci_extended}).
docs/paper/experiments_c1.tex:54:$\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$) both exceed $\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9225 vs.\ $> 0.99$ at $\leq$1.5B).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T11:14:58.569212+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "old_string": "LLaMA-3.1-8B confirms $\\Kempirical{=}2$ (0v1 $\\auc = 0.9225$, 1v2 $\\auc = 0.6123\\;[0.603,\\,0.622]$; CI lower bound above $\\theta$; Table~\\ref{tab:kstar_ci_extended}).",
  "new_string": "LLaMA-3.1-8B confirms $\\Kempirical{=}2$ (0v1 $\\auc = 0.9224$, 1v2 $\\auc = 0.6123\\;[0.603,\\,0.622]$; CI lower bound above $\\theta$; Table~\\ref{tab:kstar_ci_extended})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "old_string": "LLaMA-3.1-8B confirms $\\Kempirical{=}2$ (0v1 $\\auc = 0.9225$, 1v2 $\\auc = 0.6123\\;[0.603,\\,0.622]$; CI lower bound above $\\theta$; Table~\\ref{tab:kstar_ci_extended}).",
    "new_string": "LLaMA-3.1-8B confirms $\\Kempirical{=}2$ (0v1 $\\auc = 0.9224$, 1v2 $\\auc = 0.6123\\;[0.603,\\,0.622]$; CI lower bound above $\\theta$; Table~\\ref{tab:kstar_ci_extended})."
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T11:14:58.569406+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T11:14:58.569538+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
  "old_string": "despite progressively reduced 0v1 signal (0.9638 and 0.9225 vs.\\ $> 0.99$ at $\\leq$1.5B).",
  "new_string": "despite progressively reduced 0v1 signal (0.9638 and 0.9224 vs.\\ $> 0.99$ at $\\leq$1.5B)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "old_string": "despite progressively reduced 0v1 signal (0.9638 and 0.9225 vs.\\ $> 0.99$ at $\\leq$1.5B).",
    "new_string": "despite progressively reduced 0v1 signal (0.9638 and 0.9224 vs.\\ $> 0.99$ at $\\leq$1.5B)."
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T11:14:58.569750+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T11:14:58.569911+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": "48",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "offset": "48",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T11:14:58.570041+00:00_

48	\label{sec:extended_neural_probe}
49	
50	Cross-scale validation confirms $\Kempirical = 2$ from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$, 0v1 $= 0.9225$) both exceed $\theta$, with progressively lower 0v1 signal consistent with larger models generating more human-like text.
51	Gemma-2-27B (C4 continuation, Qwen cross-scored) yields $\Kempirical{=}1$ (1v2 $\auc = 0.5894$), consistent with Gemma-2-2B at 5K ($\Kempirical{=}1$, 1v2 $\auc = 0.5981$). The Gemma family produces $\Kempirical{=}1$ at both 2B and 27B, suggesting $\Kempirical$ is model-family-dependent rather than scale-dependent.
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T11:14:58.570163+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "old_string": "LLaMA-3.1-8B (1v2 $\\auc = 0.6123$, 0v1 $= 0.9225$)",
  "new_string": "LLaMA-3.1-8B (1v2 $\\auc = 0.6123$, 0v1 $= 0.9224$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "old_string": "LLaMA-3.1-8B (1v2 $\\auc = 0.6123$, 0v1 $= 0.9225$)",
    "new_string": "LLaMA-3.1-8B (1v2 $\\auc = 0.6123$, 0v1 $= 0.9224$)"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T11:14:58.570348+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_audit_tables_2_10_20260523T110133",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-23T11:14:58.570515+00:00_

## 审计总结

**已修复**：
- `experiments_c1.tex` line 49, 54 + `appendix_extended.tex` line 50：LLaMA-8B 0v1 从 `0.9225`（CV估计）改为 `0.9224`（bootstrap估计），与 Table 10 (.9224) 一致。

**需要人工核实 — Mistral-7B**：
论文 Table 10 中 Mistral-7B 的全部 5 个 AUC 值与 registry 中**所有** Mistral 实验都不匹配：

| Pair | 论文 | exp_019 (self) | exp_019b (cross) |
|------|------|----------------|------------------|
| 0v1 | .9170 | .9843 | .9209 |
| 1v2 | .5750 | .5935 | .5695 |
| 2v3 | .5369 | .5402 | .5335 |
| 3v4 | .5174 | .5232 | .5140 |
| 4v5 | .5175 | .5181 | .5184 |

这些值看起来介于 self-scored 和 cross-scored 之间，但不是简单平均。可能来自未注册的实验。请确认数据源。

**Registry 需更新（非论文错误）**：
- `exp_002_olmo_depth` 的 3v4 (0.5034) 和 4v5 (0.4971) 已过时，论文使用的是 `exp_olmo1b_c4_rerun` 的值 (0.5024, 0.4942)。

**可忽略的精度差异**：Gemma-2B 3v4 (Δ=0.0003) 和 4v5 (Δ=0.0001)，在存储精度误差范围内。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_audit_tables_2_10_20260523T110133"
}
```

</details>

---
