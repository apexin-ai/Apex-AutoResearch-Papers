# Research conversation: You are auditing an academic paper to find which experimental data/numbers are cited. The paper tex files are in `/home/

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6a7e9e0c43b6d074.jsonl`
- **Structured JSON:** [`189e9e05a9844a67f165.json`](../../sessions/18/189e9e05a9844a67f165.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-21T07:51:45.808Z_

You are auditing an academic paper to find which experimental data/numbers are cited. The paper tex files are in `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/`.

Read ALL of these files completely:
1. `experiments.tex` — contains Table 1, Table 3, and experimental results
2. `appendix.tex` — contains appendix tables and analysis
3. `analysis.tex` — analysis section (if exists)
4. `method.tex` — may contain pilot data
5. `abstract.tex` — may cite key numbers
6. `introduction.tex` — may cite key numbers

For each file, extract:
1. ALL numeric values that appear to be experimental results (accuracy percentages, F1 scores, p-values, ICC values, etc.)
2. ALL table data — reproduce each table's content showing the metric values
3. ANY experiment IDs or run names mentioned
4. ANY references to specific seeds, checkpoints, or configurations

Write a comprehensive report to `/tmp/paper_referenced_data.md` with:
- Section-by-section breakdown of what numbers appear
- Complete reproduction of all tables with their numeric values
- List of all unique accuracy/metric values found in the paper

Be thorough — we need to match these against 132 experiments to find which ones are cited and which are missing.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "31ca5b9e-8c59-4071-ae9d-a59abbb7f73b",
  "agentId": "a6a7e9e0c43b6d074",
  "type": "user",
  "uuid": "06cb6d1f-2165-44fb-be82-52693020139b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T07:51:45.811Z_

```json
{
  "parentUuid": "06cb6d1f-2165-44fb-be82-52693020139b",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "056724a7-42c4-4217-9cdf-c6669357a828",
  "timestamp": "2026-05-21T07:51:45.811Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T07:51:48.841Z_



I'll read all the paper tex files to extract every experimental number. Let me start by reading all the files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "056724a7-42c4-4217-9cdf-c6669357a828",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMGtgZZaqXbFNjFiorP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebb24712-fac2-4836-bf4c-135767954257",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxxPQYLUwDWV8t8YMtvKYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6647,
      "cache_read_input_tokens": 8256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6647,
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

_source line 4 · 2026-05-21T07:51:49.356Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pm7hFNuy9wKoER4zAbgHL2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebb24712-fac2-4836-bf4c-135767954257",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMGtgZZaqXbFNjFiorP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6427538-848c-4f54-a853-48fa34652fc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxxPQYLUwDWV8t8YMtvKYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6647,
      "cache_read_input_tokens": 8256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6647,
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

### Tool result

_source line 5 · 2026-05-21T07:51:49.361Z_

<details><summary>↩ Tool result · `toolu_01Pm7hFNuy9wKoER4zAbgHL2`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss due to length-mismatched sequences, which defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints where available; runs with NaN validation loss use the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Full hyperparameter details appear in Appendix~\ref{app:hyperparams}.
15	
16	\paragraph{Statistics.}
17	Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples; we resample entire problems, not individual tests, to preserve within-problem correlations); per-test vs.\ trajectory-level equivalence uses Two One-Sided Tests (TOST)~\cite{schuirmann1987tost} with $\pm$2 percentage point (\pp{}) margin. Holm-Bonferroni correction~\cite{holm1979} controls family-wise error rate across the four primary comparisons (Table~\ref{tab:holm}). Intraclass correlation coefficient (ICC)~\cite{shrout1979icc} quantifies within-problem correlation. Oracle analysis uses SWE-bench Verified (500 instances).
18	
19	
20	\subsection{Function-Level Results}
21	\label{sec:func_results}
22	
23	Table~\ref{tab:main_results} reports function-level results across formulations and model families.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\caption{Function-level per-test accuracy on HumanEval+MBPP ($n{=}1{,}890$). Mean $\pm$ std over seeds. Seeds 42/123/456: bfloat16; 789/0: NF4. DeepSeek: $n{=}2$ seeds; std reported for descriptive comparison, not inferential. \traj{} evaluated on 1,032-sample subset (447 matched variants).}
29	\label{tab:main_results}
30	\resizebox{\columnwidth}{!}{%
31	\setlength{\tabcolsep}{4pt}
32	\begin{tabular}{llcc}
33	\toprule
34	\textbf{Method} & \textbf{Model} & \textbf{Seeds} & \textbf{Accuracy (\%)} \\
35	\midrule
36	\multicolumn{4}{l}{\emph{Qwen3 (primary)}} \\
37	\cls{} (fine-tuned) & 4B & 5 & \textbf{88.43 $\pm$ 0.78} \\
38	\cwm{} (fine-tuned) & 4B & 5 & \underline{87.19 $\pm$ 0.37} \\
39	\traj{} (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
40	\midrule
41	\multicolumn{4}{l}{\emph{DeepSeek-Coder (cross-model consistency check)}} \\
42	\cls{} (fine-tuned) & 6.7B & 2 & \textbf{86.85 $\pm$ 0.11} \\
43	\cwm{} (fine-tuned) & 6.7B & 2 & \underline{86.83 $\pm$ 1.49} \\
44	\traj{} (fine-tuned) & 6.7B & 2 & 84.16 $\pm$ 1.30 \\
45	\midrule
46	\multicolumn{4}{l}{\emph{Prompting baselines}} \\
47	0-shot & 8B (Qwen3) & 1 & 68.70 \\
48	0-shot & 6.7B (DeepSeek) & 1 & 63.00 \\
49	ZS LLM-as-judge & 8B (Qwen3) & 1 & 64.40 \\
50	ZS LLM-as-judge & 6.7B (DeepSeek) & 1 & 56.56 \\
51	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
52	3-shot ICL & 8B (Qwen3) & 1 & 68.78 \\
53	3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\
54	\midrule
55	Majority (pass) & --- & --- & 51.75 \\
56	\bottomrule
57	\end{tabular}}
58	\end{table}
59	
60	All three formulations achieve comparable accuracy on Qwen3-4B: \cls{} 88.43\% ($\pm$0.78), \cwm{} 87.19\% ($\pm$0.37), \traj{} 86.30\% ($\pm$0.97). DeepSeek-Coder-6.7B shows: \cls{} 86.85\%, \cwm{} 86.83\%, \traj{} 84.16\%. The \cls{}--\cwm{} gap (0.02--1.24\pp{}) is within seed noise in both families. However, the \cls{}--\traj{} gap is model-dependent: $<$1\pp{} on Qwen3 but 2.69\pp{} on DeepSeek-Coder, exceeding the $\pm$2\pp{} equivalence margin (\S\ref{sec:equivalence}). \cls{} and \cwm{} are robustly equivalent; \traj{} parity is model-contingent. Zero-shot baselines (Tables~\ref{tab:main_results} and~\ref{tab:repo_level}) establish that repo-level verification requires fine-tuning (0-shot$\to$fine-tuned gains of 35--36\pp{}) and that formulation choice matters only at repo level (\cls{} outperforms \cwm{} by 13--26\pp{}).
61	
62	
63	\subsection{Scaling Behavior}
64	\label{sec:scaling}
65	
66	Beyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\ref{tab:scaling} compares all three formulations at 4B and 8B using seeds 42 and 123 in full bfloat16 precision (excluding NF4 seeds to isolate the size effect).
67	
68	\begin{table}[t]
69	\centering
70	\small
71	\caption{Model-size scaling: accuracy (\%) at 4B and 8B (Qwen3, seeds 42/123, full bfloat16 precision). \cls{} and \traj{} scale positively; \cwm{} does not.}
72	\label{tab:scaling}
73	\setlength{\tabcolsep}{4pt}
74	\begin{tabular}{llcccc}
75	\toprule
76	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{Mean} & \textbf{$\Delta$ 4B$\to$8B} \\
77	\midrule
78	\cls{} & 4B & 87.83 & 89.52 & \textbf{88.68} & \multirow{2}{*}{+1.27} \\
79	\cls{} & 8B & \textbf{90.48} & 89.40 & \textbf{89.94} & \\
80	\midrule
81	\cwm{} & 4B & 87.51 & 87.20 & \underline{87.36} & \multirow{2}{*}{$-$0.03} \\
82	\cwm{} & 8B & 87.67 & 86.98 & 87.33 & \\
83	\midrule
84	\traj{} & 4B & 85.27 & 86.72 & 86.00 & \multirow{2}{*}{+1.70} \\
85	\traj{} & 8B & 87.60 & 87.79 & \underline{87.70} & \\
86	\bottomrule
87	\end{tabular}
88	\end{table}
89	
90	\cls{} and \traj{} both scale positively from 4B to 8B (+1.27\pp{} and +1.70\pp{} respectively), while \cwm{} remains flat ($-$0.03\pp{}). At 8B, the ranking is \cls{} (89.94) $>$ \traj{} (87.70) $>$ \cwm{} (87.33). The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B (Figure~\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \cls{}/\cwm{}) yields $p = 0.0066$ (95\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.
91	
92	\cwm{} flat scaling ($-$0.03\pp{}) may reflect suboptimal hyperparameter transfer at 8B rather than a fundamental limitation; we do not claim generation \emph{cannot} benefit from scale. At function level, outputs are short (integers, booleans) and format compliance is near-perfect; at repo level, output length grows to ${\sim}$477 tokens on average, and the same generation bottleneck manifests as format collapse (51--74\% unparseable; \S\ref{sec:repo}). \traj{} also shows no scaling benefit at repo level (72.92\% at both 4B and 8B); only \cls{} scales positively across both complexity levels.
93	
94	
95	\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
96	\label{sec:equivalence}
97	
98	We compare \cls{} (aggregated via all-pass rule) against \traj{} on 523 variant-level instances across five seeds.\footnote{Seeds 789 and 0 use NF4 quantized inference; the remaining three use bfloat16. Restricting to bfloat16 seeds only (3 seeds) yields $p{=}0.128$: consistent in direction but underpowered due to reduced seed coverage.} The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]); the TOST equivalence test confirms statistical equivalence at $p = 0.007$ ($\pm$2\pp{} margin, Holm-Bonferroni corrected). Our $\pm$2\pp{} threshold follows the SESOI framework~\cite{lakens2017}, set independently of the observed gap and grounded in deployment relevance: at function-level accuracy (85--88\%), a 2\pp{} difference corresponds to ${\sim}$38 per-test predictions across 1,890 tests (${\sim}$2--3 problems out of 114)---comparable to between-seed variation (0.37--0.97\pp{} std, Table~\ref{tab:main_results}) and checkpoint selection noise ($<$1\pp{}, \S\ref{sec:threats}). A difference within this range is indistinguishable from training noise for pipeline selection decisions. Equivalence holds at margins as tight as $\pm$1.52\pp{} (Table~\ref{tab:tost_sensitivity}), well below the pre-specified threshold. Within-problem predictions are correlated (intraclass correlation ICC $= 0.191$, $p < 0.0001$, design effect (DEFF) $= 3.97$); all statistical tests use clustered bootstrap accordingly. On DeepSeek-Coder, the observed \cls{}--\cwm{} gap of 0.02\pp{} is consistent with equivalence, but with only 2 seeds the comparison is underpowered. The DeepSeek \cls{}--\traj{} gap (2.69\pp{}) exceeds the $\pm$2\pp{} margin; \traj{} parity is model-dependent rather than universal, while the \cls{}--\cwm{} equivalence is robust across both families. Per-test classification provides diagnostic information (which specific tests fail) at no cost to variant-level accuracy. This parallels process supervision~\cite{lightman2023letsverify}: step-level verification enables error localization without accuracy loss.
99	
100	Oracle analysis on SWE-bench Verified (500 instances) shows that per-test advantage concentrates at $T \geq 2$ fail-to-pass tests (31.3\% of instances, contributing 55.3\% of the total oracle advantage; Appendix~\ref{app:oracle}).
101	
102	
103	\subsection{Repo-Level: Complexity-Dependent Divergence}
104	\label{sec:repo}
105	
106	Table~\ref{tab:repo_level} compares formulations at repository-level complexity. Variant-level comparisons rely on limited seed coverage; the per-test interaction effect is statistically confirmed (see below). Checkpoints are val-selected where validation loss is computable (\S\ref{sec:setup}); the test set has zero problem overlap with validation.
107	
108	\begin{table}[t]
109	\centering
110	\small
111	\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set. Qwen3-8B \cls{}/\traj{}: mean $\pm$ std over 3 seeds; DeepSeek \cls{}: 2 seeds\textsuperscript{$\ddagger$}; DeepSeek \traj{}: 3 seeds; Qwen3-4B: seed 42. \cwm{} multi-seed runs in progress.}
112	\label{tab:repo_level}
113	\resizebox{\columnwidth}{!}{%
114	\setlength{\tabcolsep}{4pt}
115	\begin{tabular}{lcccc}
116	\toprule
117	\textbf{Model} & \textbf{\cls{} (\%)} & \textbf{\cls{} Var.\ (\%)} & \textbf{\cwm{} (\%)} & \textbf{\traj{} Var.\ (\%)\textsuperscript{$\diamond$}} \\
118	\midrule
119	Qwen3-4B & 83.63 & 64.58 & 58.04 & 72.92 \\
120	Qwen3-8B & \textbf{84.83 $\pm$ 0.67} & 72.92 / 81.25\textsuperscript{$\dagger$} & \tbd{} & 72.91 $\pm$ 3.61 \\
121	DeepSeek-6.7B & 84.38 $\pm$ 2.50\textsuperscript{$\ddagger$} & 81.25\textsuperscript{$\dagger$} & \tbd{} & 77.08 $\pm$ 3.61 \\
122	\midrule
123	0-shot (Qwen3-8B) & 49.90 & --- & --- & --- \\
124	0-shot (DeepSeek) & 48.50 & --- & --- & --- \\
125	Majority & 72.96 & 54.17 & 72.96 & 54.17 \\
126	\bottomrule
127	\end{tabular}}
128	
129	\vspace{2pt}
130	{\footnotesize \textsuperscript{$\dagger$}Individual-seed variant accuracy; multi-seed aggregate pending. \textsuperscript{$\ddagger$}One seed excluded: truncate preprocessing$\to$NaN val loss, decision collapse (Table~\ref{tab:taxonomy}); mean over two matched seeds. \textsuperscript{$\diamond$}Var.\ columns: variant-level accuracy ($n{=}48$); \cls{} aggregated via all-pass rule; \traj{} by design. Per-test: $n{=}9{,}784$. \cwm{} unparseable: 54\% (4B); default to pass; parseable-only 38--43\%, below majority. Eval seq\_length differs across models (Appendix~\ref{app:threats}). \cwm{} uses epoch-3 checkpoint (val loss undefined); see text for checkpoint sensitivity analysis.}
131	\end{table}
132	
133	Zero-shot prompting collapses to an always-predict-unresolved baseline (variant accuracy 45.83\%, below majority 54.17\%; Appendix~\ref{app:few_shot}).
134	
135	\paragraph{Formulation divergence (single-seed).} Under our 4--8B LoRA protocol, \cls{} and \cwm{} diverge on Qwen3: the gap is 25.59\pp{} at 4B (\cls{} 83.63\% vs.\ \cwm{} 58.04\%, seed 42; Figure~\ref{fig:scaling_gap}) and 19.31\pp{} at 8B (84.48\% vs.\ 65.17\%). \cwm{} falls below majority baseline at both scales. These gaps suggest complexity-dependent formulation effectiveness, though single-seed design and multiple confounds (\S\ref{sec:threats}) preclude definitive causal attribution.
136	
137	\paragraph{Cross-model consistency.} DeepSeek-Coder shows the same direction (\cls{} $>$ \cwm{}) under single-seed constraints. DeepSeek \cls{} degradation ranges from ${\sim}$4\pp{} (s42, drop preprocessing) to ${\sim}$12\pp{} (s123, truncate preprocessing), reflecting preprocessing and checkpoint selection sensitivity (Table~\ref{tab:taxonomy}). The \cls{}--\cwm{} gap magnitude also varies across families (20\pp{} for Qwen3 vs.\ 23--28\pp{} for DeepSeek), primarily reflecting checkpoint selection: DeepSeek \cwm{}'s val-selected checkpoint (56.70\%) underperforms its epoch-3 checkpoint (61.49\%), widening the apparent gap. Under matched checkpoint selection (epoch~3 for both), the cross-model gap difference narrows to ${\sim}$2\pp{} (Qwen3: 20.47\pp{} vs.\ DeepSeek: 22.89\pp{}). The gap is formulation-driven rather than model-specific. Eval seq\_length differs between models (Appendix~\ref{app:threats}).
138	
139	\paragraph{Failure mode taxonomy.} Variant-level analysis ($n{=}48$, Appendix Table~\ref{tab:variant_level}) reveals three failure modes (Table~\ref{tab:taxonomy}): format collapse (\cwm{}, 51--74\% unparseable), decision collapse (\cls{} under truncate preprocessing, fail recall ${\sim}$14\%), and aggregation penalty (\cls{} under drop preprocessing, fail recall 38--57\%). Decision collapse is configuration-dependent, not model-inherent. \traj{} avoids aggregation penalty by predicting variant outcomes directly (72.91--77.08\%). Downsampling \cls{} training data to match \traj{}'s data volume yields 80.74\%, still 7.82\pp{} above \traj{}; this controls data volume but not label granularity (per-test vs.\ variant-level), and remains a single-seed comparison (Appendix~\ref{app:downsample}).
140	
141	\begin{table}[t]
142	\centering
143	\small
144	\caption{Repo-level failure mode taxonomy. Variant-level majority baseline: 54.17\%.}
145	\label{tab:taxonomy}
146	\setlength{\tabcolsep}{3pt}
147	\begin{tabular}{llcc}
148	\toprule
149	\textbf{Failure Mode} & \textbf{Representative} & \textbf{Fail Recall} & \textbf{Variant Acc} \\
150	\midrule
151	Format collapse & \cwm{} (all) & N/A & 48--52\% \\
152	Decision collapse & \cls{} (DeepSeek, s123) & ${\sim}$14\% & 56\% \\
153	Aggr.\ penalty & \cls{} (Qwen3-8B) & 51--57\% & 73--81\% \\
154	Aggr.\ penalty & \cls{} (DeepSeek, s42) & 38--51\% & 79--81\% \\
155	\bottomrule
156	\end{tabular}
157	\end{table}
158	
159	\paragraph{Default assignment artifact.} The apparent \cwm{} accuracy increase from 4B to 8B is an artifact of rising unparseable rate (53.7\%$\to$73.8\%), which inflates accuracy via majority-class default while parseable-only accuracy decreases (42.88\%$\to$38.52\%; Appendix~\ref{app:parseable_bias}).
160	
161	\paragraph{Complexity as moderator.} The \cls{}--\cwm{} gap widens from 1--3\pp{} (function) to 19--26\pp{} (repo) under our protocol; a matched-context ablation confirms input disparity explains $<$3\% of this gap (Appendix~\ref{app:ablations}).
162	
163	\paragraph{Formulation$\times$complexity interaction.} A mixed-effects linear probability model with problem-level random intercepts ($n{=}56{,}480$ observations, 139 problem clusters, DeepSeek-Coder) confirms the interaction: the \cwm{} effect at function level is negligible ($\hat{\beta}{=}-0.002$, $p{=}0.805$), but the formulation$\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$). \cwm{} and \cls{} are statistically indistinguishable at function level ($\Delta{=}-0.2$\pp{}) but diverge by 22\pp{} at repo level, confirming the divergence is not an artifact of aggregation. The cross-complexity analysis uses DeepSeek-Coder, the only family with both function- and repo-level \cwm{} evaluations under matched conditions. Across both model families at repo level, the \cwm{} deficit is $-$22\pp{} ($z{=}-64.4$, $p{<}0.001$); the model family effect is significant but small (+1.1\pp{} for Qwen3, $p{=}0.002$), and the formulation$\times$model interaction is likewise small (+1.6\pp{}, $p{=}0.006$). Formulation explains $>$95\% of the predictable variance; model identity modulates gap magnitude without changing direction (Appendix~\ref{app:interaction}).
164	
165	Additional repo-level limitations appear in Appendix~\ref{app:limitations}.
166	
167	
168	\subsection{Analysis}
169	\label{sec:analysis}
170	
171	\paragraph{Aggregation penalty.} Under the all-pass rule, a single false negative flips the variant verdict. The penalty ranges from 1.36\pp{} (DeepSeek s42) to 19\pp{} (Qwen3-4B), depending on fail recall and test count (Appendix Table~\ref{tab:variant_level}). Val-based checkpoint selection biases toward per-test accuracy at the expense of fail recall, which amplifies the penalty. \traj{} avoids this by predicting variant outcomes directly (72.91--77.08\%). The penalty is predictable from test count: function-level variants ($\bar{T} \approx 2.3$) incur negligible penalty, while repo-level variants ($\bar{T} \gg 10$) incur substantial penalty, both the \emph{advantage} and \emph{cost} of per-test granularity concentrate at high $T$ (Appendix~\ref{app:extended_analysis}(a)).
172	
173	\paragraph{Why does generation degrade at repo level?} Output space complexity increases nonlinearly: function-level outputs are short strings (integers, booleans); repo-level outputs are unconstrained execution traces (mean ${\sim}$477 tokens) where errors compound multiplicatively, and cause format collapse (53--74\% unparseable). Even among parseable outputs, accuracy (38--43\%) is below majority baseline, which indicates a semantic gap beyond format compliance (Appendix~\ref{app:qualitative}).
174	
175	\cls{} achieves 217$\times$ higher throughput than \cwm{} (1 output token vs.\ avg 477), consistent across both model families.
176	
177	\paragraph{Error complementarity.} At function level, \cls{} and \cwm{} exhibit partial complementarity: both are FP-dominant (over-predict failure), but at different rates (\cls{} 56.5\%, \cwm{} 70.3\%; Appendix~\ref{app:extended_analysis}(a)), so \cwm{} over-predicts failure on instances \cls{} correctly classifies. An oracle combination achieves 90.63\% (+2.80\pp{} over the best single formulation; single-seed estimate). At repo level, oracle routing across configurations reaches 95.83\% variant accuracy (+14.58\pp{} over the best single configuration, $n{=}48$), the strongest evidence that the formulation design space contains complementary solutions worth exploring. A re-repair pilot found no benefit from per-test diagnostics ($n{=}44$, $p{=}0.42$; Appendix~\ref{app:extended_analysis}(j)). Extended analysis appears in Appendix~\ref{app:extended_analysis}.
178	
179	\subsection{Threats to Validity}
180	\label{sec:threats}
181	
182	We identify five potential confounds and assess each in Appendix~\ref{app:threats}: checkpoint selection ($<$1\pp{} variation in ablation; NaN validation loss forces final-epoch default in all \cwm{} runs and DeepSeek \cls{} s123), evaluation sequence length (${\sim}$1.5\pp{}), preprocessing (${\sim}$8\pp{} cross-configuration variance), \traj{} training regime (downsample confirms formulation advantage), and \cwm{} scale/pretraining (primary limitation; all repo-level \cwm{} conclusions conditional on the ${\leq}$8B LoRA regime). The 19--26\pp{} gap exceeds any single assessed confound, but correlated confounds and limited seeds mean definitive causal attribution requires multi-seed replication. Holm-Bonferroni correction confirms the two core claims survive (adjusted $p{=}0.012$ and $p{=}0.021$; Table~\ref{tab:holm}).
183	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6427538-848c-4f54-a853-48fa34652fc1",
  "isSidechain": true,
  "promptId": "31ca5b9e-8c59-4071-ae9d-a59abbb7f73b",
  "agentId": "a6a7e9e0c43b6d074",
  "type": "user",
  "uuid": "e5a0e4c7-7587-4e4c-bb62-6ee5cc10f21a",
  "sourceToolAssistantUUID": "a6427538-848c-4f54-a853-48fa34652fc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T07:51:49.830Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LogeSEmVGVP7JBN3E2CZaa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5a0e4c7-7587-4e4c-bb62-6ee5cc10f21a",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMGtgZZaqXbFNjFiorP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "992e091d-5d69-4c2a-84ad-ee5cbc4e8181",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxxPQYLUwDWV8t8YMtvKYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6647,
      "cache_read_input_tokens": 8256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6647,
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

### Tool result

_source line 7 · 2026-05-21T07:51:50.243Z_

<details><summary>↩ Tool result · `toolu_01LogeSEmVGVP7JBN3E2CZaa`</summary>

```text
1	\appendix
2	
3	\section{Oracle Accuracy-Utility Analysis}
4	\label{app:oracle}
5	
6	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
12	\label{tab:oracle}
13	\resizebox{\columnwidth}{!}{%
14	\setlength{\tabcolsep}{3pt}
15	\begin{tabular}{lcccc}
16	\toprule
17	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
18	\midrule
19	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
20	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
21	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
22	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
23	\midrule
24	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
25	\bottomrule
26	\end{tabular}}
27	\end{table}
28	
29	\begin{figure}[h]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
32	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage).}
33	\label{fig:oracle_stratified}
34	\end{figure}
35	
36	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\pp{} vs.\ 18.49\pp{} (1.7$\times$). P2P regression is negligible (1.04\% mean, 0\% median); the practical value concentrates in F2P discrimination.
37	
38	\paragraph{Sensitivity to ICC estimate.}
39	The analysis above uses ICC $= 0.191$ from function-level analysis (\S\ref{sec:equivalence}), where mean cluster size $\bar{k} \approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\S\ref{sec:repo}), a consequence of the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly and amplify the block-correlated per-test advantage at each $T$ stratum; the correction from i.i.d.\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage. The repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, which strengthens the case for per-test granularity at repository-level complexity.
40	
41	\section{Ablation Studies}
42	\label{app:ablations}
43	
44	\paragraph{LoRA rank sensitivity.}
45	All \cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \cwm{}, we train rank-32 variants (seed 42), doubling adapter parameters.
46	
47	\begin{table}[h]
48	\centering
49	\small
50	\caption{LoRA rank ablation for \cwm{} 4B (seed 42, 3 epochs, lr $= 2{\times}10^{-4}$). Rank-16 seed variance: 0.53\pp{} (seeds 42 vs.\ 456).}
51	\label{tab:rank_ablation}
52	\setlength{\tabcolsep}{4pt}
53	\begin{tabular}{lccccc}
54	\toprule
55	\textbf{Config} & \textbf{$\alpha/r$} & \textbf{Acc (\%)} & \textbf{Fail \fone{}} & \textbf{Pass \fone{}} & \textbf{$\Delta$} \\
56	\midrule
57	$r{=}16$, $\alpha{=}32$ & 2 & \textbf{87.51} & --- & --- & --- \\
58	$r{=}32$, $\alpha{=}32$ & 1 & 87.00 & 87.1 & 86.9 & $-$0.51 \\
59	$r{=}32$, $\alpha{=}64$ & 2 & 87.04 & 87.27 & 86.79 & $-$0.47 \\
60	\bottomrule
61	\end{tabular}
62	\end{table}
63	
64	Both rank-32 variants fall within the 2-seed variance of the rank-16 baseline (0.53\pp{} between seeds 42 and 456). The $\alpha{=}64$ variant (matching the baseline $\alpha/r{=}2$ ratio) rules out the confound that the $\alpha{=}32$ result might reflect reduced effective scaling rather than rank insensitivity. This is consistent with \cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.
65	
66	\paragraph{Majority voting.}
67	Majority voting ($K{=}3$) decreases accuracy from 87.51\% to 86.83\% ($-$0.68\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\footnote{These majority-voting values were computed from an unverified checkpoint and may differ slightly from the val-best checkpoint results.}
68	
69	\paragraph{Sequence-length ablation details.}
70	Both formulations are trained with \texttt{max\_seq\_length}$=$2,048. At inference, \cwm{} reserves \texttt{max\_new\_tokens}$=$512, leaving ${\sim}$1,536 effective input tokens; \cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\cls{} 8B at 2,048 tokens) achieves 83.04\%, only 1.44\pp{} below the 8,192-token evaluation (84.48\%), though truncation introduces 136 unparseable outputs (1.39\% of test samples). The matched-context gap (\cls{}@2,048 vs.\ \cwm{}@2,048) is 25.00\pp{} (98\% of the full 25.59\pp{} gap), confirming that input context disparity explains at most 3\% of the difference.
71	
72	\paragraph{Training data size control.}
73	\label{app:downsample}
74	To control for the training set size asymmetry between \cls{} (${\sim}$70K instances) and \traj{} (386 variant-level instances, ${\sim}$8K per-test equivalents, at repo level), we downsample \cls{} training data to match \traj{} in data volume. Downsampled \cls{} (Qwen3-4B, seed 42) achieves 80.74\% repo-level per-test accuracy, only 2.89\pp{} below the full-data \cls{} (83.63\%) and still 7.82\pp{} above \traj{} (72.92\%). The \cls{} formulation advantage is not attributable to training data volume.
75	
76	\paragraph{Few-shot prompting baselines.}
77	\label{app:few_shot}
78	We evaluate 3-shot in-context learning at repo level to test whether prompting strategy closes the gap to fine-tuned models. Table~\ref{tab:few_shot} reports both per-test and variant-level accuracy.
79	
80	\begin{table}[h]
81	\centering
82	\small
83	\caption{Repo-level prompting baselines (per-test $n{=}9{,}784$; variant-level $n{=}48$). Majority baseline: 72.96\% per-test, 54.17\% variant-level.}
84	\label{tab:few_shot}
85	\setlength{\tabcolsep}{4pt}
86	\begin{tabular}{lcccc}
87	\toprule
88	\textbf{Model} & \textbf{0-shot (per-test)} & \textbf{3-shot (per-test)} & \textbf{3-shot (variant)} \\
89	\midrule
90	Qwen3-8B & 49.90\% & 71.61\% & 45.83\%\textsuperscript{$\ast$} \\
91	DeepSeek-6.7B & 48.54\% & 46.28\% & 45.83\%\textsuperscript{$\ast$} \\
92	\bottomrule
93	\end{tabular}
94	
95	\vspace{2pt}
96	{\footnotesize \textsuperscript{$\ast$}Both models achieve 45.83\% by correctly classifying all 22 unresolved variants and zero resolved variants (22/48 = 45.83\%), equivalent to an always-predict-unresolved baseline. The 100\% overlap in variant-level predictions confirms complete degradation at task-relevant granularity.}
97	\end{table}
98	
99	Both models converge to exactly 45.83\% variant-level accuracy under 3-shot prompting, below majority baseline (54.17\%). Variant-level analysis reveals this is not a coincidence: both models correctly classify all 22 unresolved variants and zero resolved variants, equivalent to an always-predict-unresolved baseline with 100\% prediction overlap. Per-test accuracy diverges sharply (Qwen3-8B 71.61\% vs.\ DeepSeek 46.28\%), but this divergence is entirely superficial: Qwen3-8B predicts pass on nearly all tests, inflating per-test accuracy on a pass-heavy dataset (72.96\% pass rate) without genuine discriminative ability. Per-test metrics can thus severely misrepresent baseline capability; variant-level evaluation is necessary to detect complete degradation. Neither 0-shot nor few-shot prompting approaches fine-tuned performance (82--84\% per-test); fine-tuning is a necessary condition for repo-level verification.
100	
101	\section{Repo-Level Per-Mutation Breakdown}
102	\label{app:repo_mutation}
103	
104	Table~\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \cls{} produces 0\% unparseable outputs; all values are direct classification accuracy. \cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \S\ref{sec:repo}).
105	
106	\begin{table}[h]
107	\centering
108	\small
109	\caption{Per-mutation test accuracy (\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \cls{} 8B reports two seeds; $\Delta$ is mean 4B$\to$8B gain for \cls{}. \cwm{} 4B per-mutation overall accuracy unavailable except gold (computed from parse rate 43.5\%, parseable acc 23.5\%).}
110	\label{tab:mutation_breakdown}
111	\resizebox{\columnwidth}{!}{%
112	\setlength{\tabcolsep}{3pt}
113	\begin{tabular}{lccccccc}
114	\toprule
115	\textbf{Mutation} & \textbf{$n$} & \textbf{CLS 4B} & \textbf{CLS 8B s42} & \textbf{CLS 8B s123} & \textbf{CWM 4B} & \textbf{CWM 8B} & \textbf{$\Delta$ CLS} \\
116	\midrule
117	gold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\
118	operator\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\
119	off\_by\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \textbf{+24.58} \\
120	return\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\
121	boundary\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\
122	\bottomrule
123	\end{tabular}}
124	\end{table}
125	
126	Table~\ref{tab:cwm_mutation_parse} shows that \cwm{} generation quality degrades from 4B to 8B across all mutation types.
127	
128	\begin{table}[h]
129	\centering
130	\small
131	\caption{\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below random binary chance (50\%) for gold at both scales.}
132	\label{tab:cwm_mutation_parse}
133	\setlength{\tabcolsep}{4pt}
134	\begin{tabular}{lcccc}
135	\toprule
136	& \multicolumn{2}{c}{\textbf{Parse Rate (\%)}} & \multicolumn{2}{c}{\textbf{Parse Acc (\%)}} \\
137	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
138	\textbf{Mutation} & \textbf{4B} & \textbf{8B} & \textbf{4B} & \textbf{8B} \\
139	\midrule
140	gold & 43.5 & 23.9 & 23.5 & 16.5 \\
141	operator\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\
142	off\_by\_one & 4.4 & 27.3 & 0.0 & 38.0 \\
143	return\_value & 48.8 & 26.9 & 27.0 & 56.9 \\
144	boundary\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\
145	\bottomrule
146	\end{tabular}
147	\end{table}
148	
149	Key findings: (1)~Gold parse rate collapses from 43.5\% to 23.9\% at 8B; the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\%: the model generates outputs that fail exact-match even for correct code. (3)~\texttt{off\_by\_one} is an anomaly: parse rate \emph{increases} from 4.4\% to 27.3\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.
150	
151	\section{Variant-Level Accuracy}
152	\label{app:variant_level}
153	
154	Table~\ref{tab:variant_level} reports variant-level accuracy ($n{=}48$) alongside per-test accuracy for all repo-level configurations. For \cls{}, the aggregation penalty (per-test $\to$ variant-level drop) ranges from 1\pp{} to 19\pp{} and is largest for models with low fail recall under the all-pass rule. \cwm{} variant-level accuracy (48--52\%) falls at or below the majority baseline, consistent with format collapse as the dominant failure mode.
155	
156	\begin{table}[h]
157	\centering
158	\small
159	\caption{Repo-level per-test vs.\ variant-level accuracy ($n{=}48$ variants). Penalty = per-test $-$ variant-level. \traj{} predicts variant outcomes directly (no aggregation). Variant-level majority baseline: 54.17\% (26/48).}
160	\label{tab:variant_level}
161	\setlength{\tabcolsep}{3pt}
162	\begin{tabular}{llcccc}
163	\toprule
164	\textbf{Model} & \textbf{Seed} & \textbf{Per-test (\%)} & \textbf{Variant (\%)} & \textbf{Penalty (\pp{})} & \textbf{Fail Recall (\%)} \\
165	\midrule
166	\multicolumn{6}{l}{\emph{\cls{}}} \\
167	Qwen3-8B & s42 & 84.48 & 72.92 & 11.56 & 56.76 \\
168	Qwen3-8B & s123 & 85.60 & 81.25 & 4.35 & 51.44 \\
169	Qwen3-4B & s42 & 83.63 & 64.58 & 19.05 & 48.72 \\
170	DeepSeek-6.7B & s42 (e1) & 82.61 & 81.25 & 1.36 & 51.02 \\
171	DeepSeek-6.7B & s42 (e3) & 82.51 & 79.17 & 3.34 & 38.47 \\
172	DeepSeek-6.7B & s123 & 74.93 & 56.25 & 18.68 & ${\sim}$13.72 \\
173	\midrule
174	\multicolumn{6}{l}{\emph{\cwm{}}} \\
175	Qwen3-8B & s42 & 65.17 & 52.08 & 13.09 & --- \\
176	DeepSeek-6.7B$^\dagger$ & s123 & --- & 47.92 & --- & --- \\
177	\midrule
178	\multicolumn{6}{l}{\emph{\traj{}}} \\
179	Qwen3-4B & s42 & --- & 72.92 & --- & --- \\
180	Qwen3-8B & s42 & --- & 70.83 & --- & --- \\
181	DeepSeek-6.7B & 3-seed & --- & 77.08 $\pm$ 3.61 & --- & --- \\
182	\midrule
183	Majority & --- & 72.96 & 54.17 & --- & --- \\
184	\bottomrule
185	\end{tabular}
186	\vspace{2pt}
187	
188	{\footnotesize $^\dagger$Preliminary; evaluated on ${\sim}$75\% of test instances (7210--7668 of 9784). DeepSeek \traj{} Table~\ref{tab:repo_level} reports 3 seeds (42/123/456) for alignment with \cls{}/\cwm{} seed coverage; three supplementary seeds (0/789/999) yield 75.0\%, 66.7\%, 79.2\% respectively (6-seed mean 75.35 $\pm$ 5.00\%), consistent in direction.}
189	\end{table}
190	
191	\section{Training Hyperparameters}
192	\label{app:hyperparams}
193	
194	Table~\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \cls{} and \cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size, gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes), and learning rate (DeepSeek-Coder uses $2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$ for Qwen3, selected via grid search over $\{5{\times}10^{-5}, 1{\times}10^{-4}, 2{\times}10^{-4}\}$ on held-out validation loss).
195	
196	\begin{table}[h]
197	\centering
198	\small
199	\caption{Training hyperparameters for \cls{}/\cwm{} configurations. Effective batch size is $\text{per-device} \times \text{grad.\ accum.} = 32$ in all cases. \traj{} models use lr $= 2{\times}10^{-4}$ due to the smaller training set (${\sim}$8K function-level instances vs.\ ${\sim}$70K for \cls{}/\cwm{}); other hyperparameters are shared.}
200	\label{tab:hyperparams}
201	\resizebox{\columnwidth}{!}{%
202	\setlength{\tabcolsep}{3pt}
203	\begin{tabular}{lcccccc}
204	\toprule
205	\textbf{Hyperparameter} & \textbf{Qwen3-4B \cls{}} & \textbf{Qwen3-4B \cwm{}} & \textbf{Qwen3-8B \cls{}} & \textbf{Qwen3-8B \cwm{}} & \textbf{DS-6.7B \cls{}} & \textbf{DS-6.7B \cwm{}} \\
206	\midrule
207	Base model & Qwen3-4B & Qwen3-4B & Qwen3-8B & Qwen3-8B & DS-Coder-6.7B & DS-Coder-6.7B \\
208	LoRA rank ($r$) & 16 & 16 & 16 & 16 & 16 & 16 \\
209	LoRA alpha ($\alpha$) & 32 & 32 & 32 & 32 & 32 & 32 \\
210	LoRA dropout & 0.05 & 0.05 & 0.05 & 0.05 & 0.05 & 0.05 \\
211	LoRA targets & \multicolumn{6}{c}{\texttt{q\_proj, k\_proj, v\_proj, o\_proj}} \\
212	Learning rate & 5e-5 & 5e-5 & 5e-5 & 5e-5 & 2e-4 & 2e-4 \\
213	Optimizer & \multicolumn{6}{c}{AdamW ($\beta_1{=}0.9$, $\beta_2{=}0.999$)} \\
214	Weight decay & 0.01 & 0.01 & 0.01 & 0.01 & 0.0 & 0.0 \\
215	Warmup ratio & 0.05 & 0.05 & 0.05 & 0.05 & 0.1 & 0.1 \\
216	LR scheduler & \multicolumn{6}{c}{Linear} \\
217	Per-device batch size & 2 & 1 & 1 & 1 & 2 & 1 \\
218	Gradient accumulation & 16 & 32 & 32 & 32 & 16 & 32 \\
219	Effective batch size & 32 & 32 & 32 & 32 & 32 & 32 \\
220	Max sequence length & 2,048 & 2,048 & 2,048 & 2,048 & 2,048 & 2,048 \\
221	Epochs & 3 & 3 & 3 & 3 & 3 & 3 \\
222	Precision & bf16 & bf16 & bf16 & bf16 & bf16 & bf16 \\
223	Gradient checkpointing & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
224	Seeds (function) & \multicolumn{6}{c}{\{42, 123, 456, 789, 0\}\textsuperscript{$b$}} \\
225	Seeds (repo) & \multicolumn{6}{c}{\{42, 123, 456\}\textsuperscript{$c$}} \\
226	Training samples & 70,748 & 70,748 & 70,748 & 70,748 & 67,343$^a$ & 70,748 \\
227	\bottomrule
228	\end{tabular}}
229	
230	\vspace{2pt}
231	{\footnotesize $^a$DeepSeek \cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \S\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\ref{tab:repo_level} caption for per-model counts.}
232	\end{table}
233	
234	\paragraph{Data processing.} DeepSeek CWM seeds use \texttt{train\_unified.py}, which drops samples exceeding \texttt{max\_seq\_length} (3{,}405 of 70{,}748 samples, 4.8\%). Qwen CWM seeds use \texttt{train\_repo\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\sim}$12{,}627 vs.\ ${\sim}$13{,}266 for DeepSeek, ${\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.
235	
236	\paragraph{Prompt templates.} Prompt templates for all formulations (\cls{}, \cwm{}, \traj{}) are provided in the code repository. \cls{} uses a binary classification template (``Does this test pass or fail?''); \cwm{} uses an execution simulation template (``What is the output of this test?''); \traj{} uses a variant-level verdict template (``Is this patch resolved or unresolved?'').
237	
238	\paragraph{Mutation operators.} We use five mutation types: (1)~\emph{gold}: unmodified code (all tests pass); (2)~\emph{operator\_swap}: replaces comparison or arithmetic operators (e.g., \texttt{<} $\to$ \texttt{<=}); (3)~\emph{off\_by\_one}: shifts loop bounds or array indices by $\pm$1; (4)~\emph{return\_value}: modifies return statements (e.g., negating a boolean, changing a constant); (5)~\emph{boundary\_removal}: removes conditional guards or boundary checks. Mutation operators were applied using AST-level transformation; variants that did not alter any test outcome were discarded.
239	
240	\paragraph{Compute budget.}
241	All experiments were conducted on NVIDIA RTX 5090 GPUs. Training time is approximately 1.5 hours per run for 4B models and 2 hours for 8B models. Total compute budget: ${\sim}$370 GPU-hours across 223 completed runs (135 successful, 88 failed/killed; ${\sim}$46 unique configurations including seeds, formulations, model sizes, and ablations).
242	
243	\section{Val-Test Mutation Type Distribution}
244	\label{app:mutation_distribution}
245	
246	Table~\ref{tab:mutation_distribution} reports the mutation type composition of the repo-level validation and test sets. The most notable shift is \texttt{operator\_swap}, which nearly doubles from val (19.1\%) to test (34.3\%), while \texttt{off\_by\_one} shrinks from 10.0\% to 1.9\%.
247	
248	\begin{table}[h]
249	\centering
250	\small
251	\caption{Repo-level mutation type distribution: validation vs.\ test set, with per-type \cls{} accuracy at two model sizes (seed 42). Shift = test\% $-$ val\%.}
252	\label{tab:mutation_distribution}
253	\setlength{\tabcolsep}{3pt}
254	\begin{tabular}{lccccc}
255	\toprule
256	\textbf{Mutation Type} & \textbf{Val (\%)} & \textbf{Test (\%)} & \textbf{Shift} & \textbf{\cls{} 4B} & \textbf{\cls{} 8B} \\
257	\midrule
258	gold & 45.2 & 47.4 & +2.2 & 98.3 & 96.2 \\
259	operator\_swap & 19.1 & 34.3 & +15.2 & 78.9 & 81.4 \\
260	boundary\_removal & 15.0 & 10.7 & $-$4.3 & 46.9 & 46.9 \\
261	return\_value & 10.7 & 5.7 & $-$5.0 & 68.0 & 75.4 \\
262	off\_by\_one & 10.0 & 1.9 & $-$8.1 & 58.5 & 86.9 \\
263	\bottomrule
264	\end{tabular}
265	\end{table}
266	
267	The \texttt{operator\_swap} shift is the primary source of val-test distribution mismatch. Since \cls{} achieves moderate accuracy on this type (78.9--81.4\%), the over-representation in the test set does not systematically bias overall accuracy estimates in either direction. Two boundary observations are notable: (1)~\texttt{boundary\_removal} represents a scale-invariant difficulty ceiling at ${\sim}$47\% across both model sizes: this mutation type resists capacity scaling; (2)~\texttt{off\_by\_one} shows the largest scaling gain (+28.4\pp{}, 58.5\%$\to$86.9\%) but its small test share (1.9\%) limits its contribution to overall accuracy differences across scales.
268	
269	\section{Qualitative Error Analysis}
270	\label{app:qualitative}
271	
272	To complement the quantitative divergence reported in \S\ref{sec:repo}, we examine representative errors from each formulation at repository level.
273	
274	\paragraph{\cwm{} failure modes.}
275	Two patterns account for the majority of unparseable \cwm{} outputs on Qwen3. (1)~\emph{Task misunderstanding}: the model generates a complete simulated test runner log (test names, timing, summary lines) rather than a pass/fail verdict. For instance, on \texttt{django\_\_django-14315}, the model outputs a fabricated 1,248-token Django test execution trace with hallucinated test names that do not exist in the target file. The model confuses ``predict test outcome'' with ``simulate test execution environment.'' (2)~\emph{Autoregressive degeneration}: the model enters a repetitive loop (e.g., repeating \texttt{from \_pytest.config import \_parse\_pytest\_args} until truncation at 4,542 tokens). Both patterns produce zero usable signal and default to the majority-class label. This explains why unparseable predictions carry higher accuracy than parseable ones (\S\ref{sec:repo}).
276	
277	\paragraph{\cls{} failure modes.}
278	\cls{} errors concentrate in two categories requiring multi-step reasoning. False positives arise from \emph{cross-concern value propagation}: a boundary removal mutation in \texttt{pytest} converts a guarded attribute access (\texttt{if xfailed and not xfailed.run}) to \texttt{if True:}, causing a NoneType error on tests exercising unrelated skip marks. The model fails to trace the None path through the pytest hook lifecycle. False negatives arise from \emph{mathematical equivalence}: on \texttt{HumanEval/130} (Tribonacci variant), the model predicts failure for correct code because verifying the self-referential recurrence requires algebraic substitution rather than syntactic inspection. This single problem accounts for 17\% of all function-level false negatives.
279	
280	\paragraph{Complementarity.}
281	These failure patterns operate at different levels: \cwm{} fails at the format level (producing no usable signal), while \cls{} fails at the reasoning level (producing a confident but incorrect binary verdict). Both formulations are FP-dominant (over-predict failure), but \cwm{}'s higher FP rate (70.3\% vs.\ 56.5\%) means it over-predicts failure on instances \cls{} correctly classifies, producing partial complementarity (oracle combination: 90.63\%; \S\ref{app:extended_analysis}, paragraph a).
282	
283	\section{Extended Analysis}
284	\label{app:extended_analysis}
285	
286	\paragraph{(a) Error complementarity.}
287	\cls{} and \cwm{} are both FP-dominant at function level but at different rates, producing partial complementarity. Among \cls{} errors (seed 42), 56.5\% are false positives (PASS $\to$ FAIL); among \cwm{} errors, 70.3\% are false positives. Both formulations over-predict failure, but \cwm{}'s stronger FP bias means it incorrectly rejects passing tests that \cls{} correctly accepts. An oracle combination achieves 90.63\% accuracy (1713/1890 correct, 177 both-wrong; +2.80\pp{} over the best single formulation, \cls{} 87.83\%; single-seed estimate, seed 42). The complementarity arises from different \emph{degrees} of fail-bias rather than opposite error directions: \cwm{}'s generation bottleneck produces aggressive failure predictions, while \cls{}'s single-token output is more calibrated. Ensemble approaches exploiting this degree difference are a natural direction.
288	
289	\paragraph{(b) CWM error mode breakdown.}
290	Among unparseable \cwm{} outputs (Qwen3, repo-level), 76.9\% contain no execution keywords; 22.9\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\%); repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-level one.
291	
292	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
293	Relaxed matching (tolerating format deviations, L0--L4) \emph{decreases} \cwm{} accuracy: 58.04\%$\to$56.98\% (seed 42) and 59.09\%$\to$55.91\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (42--53\%). The divergence widens from 26\pp{} to 28\pp{} under relaxed matching. This rules out the hypothesis that parsing strictness inflates the observed gap. Constrained decoding~\cite{willard2023outlines} could enforce format compliance but would not address the semantic accuracy deficit among parseable outputs.
294	
295	\paragraph{(d) Variance compression.}
296	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and \traj{} (0.97\pp{}) at function level. If \cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
297	
298	\paragraph{(e) Per-test precision and recall.}
299	\cls{} achieves fail \fone{} 87.59\% (precision 86.20\%, recall 89.04\%) at seed 42.% derived from overlap analysis (error_overlap_matched_seed.json); FP=130, FN=100, TP=848, TN=812
300	Multi-F2P instances (6--10 tests) reach 96.3\% accuracy, consistent with the oracle finding that per-test granularity is most valuable for complex instances.
301	
302	\paragraph{(f) Block correlation.}
303	Within-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\times$ more all-correct problems than i.i.d.\ expectation). All statistical tests use clustered bootstrap accordingly.
304	
305	\paragraph{(g) Failed interventions.}
306	We systematically tested four interventions targeting different hypothesized causes of \cwm{} repo-level degradation; all failed:
307	
308	\begin{itemize}[leftmargin=*,itemsep=1pt,topsep=2pt]
309	\item \textbf{Capacity (rank 32):} Doubling adapter parameters does not improve accuracy ($-$0.51\pp{}, within seed variance; Appendix~\ref{app:ablations}).
310	\item \textbf{Majority voting ($K{=}3$):} Accuracy \emph{decreases} by 0.68\pp{} (87.51\%$\to$86.83\%); 93.3\% of samples are unanimous across passes, and net flips are negative ($-$13), indicating errors are systematic bias rather than stochastic noise.
311	\item \textbf{Relaxed matching (L0--L4):} Tolerating format deviations \emph{decreases} accuracy from 58.04\% to 56.98\% (seed 42; Appendix~\ref{app:extended_analysis}(c)), because unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (38--43\%).
312	\item \textbf{Model scaling (4B$\to$8B):} Parseable-only accuracy decreases (42.88\%$\to$38.52\%) while unparseable rate increases (53.7\%$\to$73.8\%); the apparent accuracy gain is entirely a default-assignment artifact (\S\ref{sec:repo}).
313	\end{itemize}
314	
315	\noindent Each intervention targets a distinct alternative explanation (insufficient capacity, random noise, parsing strictness, model scale); the uniform failure across all four confirms the bottleneck is formulation-level---output space complexity at repo level exceeds what ${\leq}$8B generation models can handle, independent of these surface-level factors.
316	
317	\paragraph{(h) Per-mutation scaling patterns.}
318	Scaling benefits are highly non-uniform across mutation types (Table~\ref{tab:mutation_breakdown}). \texttt{off\_by\_one} shows the largest \cls{} scaling gain: 58.5\% (4B) to 86.9\% (8B, $+$28.4\pp{}). In contrast, \texttt{boundary\_removal} is scale-invariant at ${\sim}$47\% across both sizes, which marks an intrinsic difficulty ceiling. For \cwm{}, gold mutation parse rate collapses from 43.5\% (4B) to 23.9\% (8B) despite being the simplest target: generation capability degrades even for trivially correct code at larger scale within Qwen3. The val-test mutation type distribution differs notably (\texttt{operator\_swap} shifts from 19.1\% to 34.3\%; Table~\ref{tab:mutation_distribution}), but this shift does not systematically bias overall accuracy because \cls{} performance on \texttt{operator\_swap} (78.9--81.4\%) is close to the overall mean.
319	
320	\paragraph{(i) Inference efficiency.}
321	\cls{} achieves 217$\times$ higher throughput than \cwm{} at repo level (853 vs.\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\cls{}) vs.\ 16.3s (\cwm{}). At the observed unparseable rate of 73.8\% (8B), the majority of \cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This \cls{}--\cwm{} efficiency gap is an inherent property of the formulation difference (1 vs.\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.
322	
323	The \cls{}--\traj{} efficiency comparison is more nuanced, because \cls{} makes one call per test while \traj{} makes one call per instance. Per-call, \cls{} is 20--138$\times$ faster (depending on input length: 47ms for short contexts vs.\ 2,632ms for \traj{}). However, the per-instance effective speedup depends on test count $|T|$: at function level ($|T| \approx 2.3$), \cls{} is ${\sim}$24$\times$ faster (108ms vs.\ 2,632ms per instance); at repo level ($|T| \approx 12.3$, ${\sim}$70ms/call with longer inputs), \cls{} is ${\sim}$3$\times$ faster (861ms vs.\ 2,631ms). A crossover exists at $|T| \approx 50$ tests, beyond which \traj{}'s single-call amortization dominates. This boundary condition is informative for deployment: \cls{} is strongly preferred for function-level and moderate repo-level test suites, while extremely large test suites ($>$50 tests per instance) favor trajectory-level efficiency despite its coarser diagnostic signal.
324	
325	\paragraph{(j) Re-repair pilot.}
326	We tested whether per-test diagnostic feedback improves downstream repair. A Qwen3-8B repair agent received either per-test diagnostic signals (which specific tests failed and why) or binary accept/reject feedback, evaluated on 44 SWE-bench Verified instances. The diagnostic condition achieved accuracy no higher than the binary baseline ($A_1 = 52.3\%$, $p = 0.42$, effect size $\approx 0$). Per-test diagnostic information does not automatically translate to repair improvements at this scale. The negative result may reflect insufficient agent capability to exploit fine-grained feedback, insufficient sample size (at $n = 44$, statistical power is ${\sim}$0.3 for a medium effect size), or a genuine limitation of the diagnostic-to-repair translation.
327	
328	\section{TOST Margin Sensitivity}
329	\label{app:tost_sensitivity}
330	
331	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence $p$-value as a function of the equivalence margin, computed on the 5-seed variant-level \cls{}--\traj{} comparison (gap $= -$0.45\pp{}, 523 variants, 114 clusters, clustered bootstrap).
332	
333	\begin{table}[h]
334	\centering
335	\small
336	\caption{TOST margin sensitivity for \cls{}--\traj{} variant-level equivalence (5 seeds, 523 variants, 114 clusters). The smallest margin achieving equivalence at $\alpha = 0.05$ is $\pm$1.52\pp{}.}
337	\label{tab:tost_sensitivity}
338	\setlength{\tabcolsep}{4pt}
339	\begin{tabular}{ccc}
340	\toprule
341	\textbf{Margin ($\pm$\pp{})} & \textbf{$p$-value} & \textbf{Equivalent ($\alpha{=}0.05$)?} \\
342	\midrule
343	1.0 & $\gg$0.05 & No \\
344	1.5 & 0.054 & No (borderline) \\
345	\textbf{1.52} & ${\sim}$\textbf{0.05} & \textbf{Smallest margin} \\
346	1.71 & 0.027 & Yes \\
347	2.0 & 0.0087 & Yes \\
348	3.0 & $4.6{\times}10^{-5}$ & Yes \\
349	5.0 & $\ll$0.001 & Yes \\
350	\bottomrule
351	\end{tabular}
352	\end{table}
353	
354	The minimum equivalence margin is $\pm$1.52\pp{}, 0.48\pp{} below our pre-specified $\pm$2\pp{} threshold. The $\pm$2\pp{} threshold was set based on deployment relevance rather than observed data: at function-level accuracy (85--88\%), a 2\pp{} per-test difference corresponds to ${\sim}$38 additional errors across 1,890 tests (${\sim}$2--3 problems out of 114), comparable in magnitude to between-seed standard deviation (0.37--0.97\pp{}) and checkpoint selection noise ($<$1\pp{}). Differences within this range do not reliably distinguish formulations from training noise in pipeline selection decisions.
355	
356	
357	\section{Variant-Level Effect Sizes}
358	\label{app:power}
359	
360	Table~\ref{tab:variant_power} reports variant-level bootstrap confidence intervals for the repo-level formulation comparisons ($n{=}48$ variants). Following Hoenig and Heisey~\cite{hoenig2001}, we report minimum detectable effect (MDE) rather than post-hoc observed power.
361	
362	\begin{table}[h]
363	\centering
364	\small
365	\caption{Variant-level bootstrap analysis ($n{=}48$). \cls{}--\cwm{} uses paired bootstrap (same variants, same seed); \cls{}--\traj{} uses unpaired bootstrap (per-variant \traj{} predictions not archived for pairing). MDE at $n{=}48$: ${\sim}$25\pp{}.}
366	\label{tab:variant_power}
367	\setlength{\tabcolsep}{3pt}
368	\begin{tabular}{llccc}
369	\toprule
370	\textbf{Comparison} & \textbf{Config} & \textbf{$\Delta$ (\pp{})} & \textbf{95\% CI} & \textbf{$p$} \\
371	\midrule
372	\multicolumn{5}{l}{\emph{\cls{} vs.\ \cwm{} (paired)}} \\
373	& Qwen3-8B & +29.17 & [10.42, 47.92] & 0.003 \\
374	& DeepSeek-6.7B & +35.42 & [18.75, 50.05] & ${<}$0.001 \\
375	\midrule
376	\multicolumn{5}{l}{\emph{\cls{} vs.\ \traj{} (unpaired)}} \\
377	& Qwen3-4B & $-$4.17 & wide & 0.740 \\
378	& Qwen3-8B & +8.33 & wide & 0.385 \\
379	& DeepSeek-6.7B & 0.00 & wide & 1.000 \\
380	\bottomrule
381	\end{tabular}
382	\end{table}
383	
384	At $n{=}48$, the MDE is ${\sim}$25\pp{}. The \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \cls{}--\traj{} gaps ($<$10\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\S\ref{sec:equivalence}).
385	
386	The \cls{}--\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \traj{} per-variant predictions were not archived in a format that permits pairing. The \cls{}--\cwm{} paired comparison uses \cls{} s123 vs.\ \cwm{} s42 (different seeds), but the CI lower bound of 10.42\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\pp{}).
387	
388	
389	\section{Multiple Comparison Correction}
390	\label{app:holm}
391	
392	Table~\ref{tab:holm} applies Holm-Bonferroni correction~\cite{holm1979} to the four primary statistical comparisons across this study ($k{=}4$, family-wise $\alpha{=}0.05$).
393	
394	\begin{table}[h]
395	\centering
396	\small
397	\caption{Holm-Bonferroni correction for primary comparisons ($k{=}4$). Comparisons ranked by raw $p$-value; each tested against $\alpha / (k - \text{rank} + 1)$.}
398	\label{tab:holm}
399	\setlength{\tabcolsep}{3pt}
400	\begin{tabular}{clcccc}
401	\toprule
402	\textbf{Rank} & \textbf{Comparison} & \textbf{Raw $p$} & \textbf{Factor} & \textbf{Adj $p$} & \textbf{Sig.?} \\
403	\midrule
404	1 & Repo: \cls{} vs \cwm{} & 0.003 & $\times$4 & 0.012 & \checkmark \\
405	2 & Func: \cls{} vs \traj{} (TOST $\pm$2\pp{}) & 0.0071 & $\times$3 & 0.021 & \checkmark \\
406	3 & Repo: \cwm{} vs \traj{} & 0.039 & $\times$2 & 0.078 & --- \\
407	4 & Repo: \cls{} vs \traj{} & 0.385 & $\times$1 & 0.385 & --- \\
408	\bottomrule
409	\end{tabular}
410	\end{table}
411	
412	The two core claims survive correction: the repo-level \cls{}--\cwm{} gap (adjusted $p{=}0.012$) and function-level \cls{}--\traj{} equivalence (adjusted $p{=}0.021$). The repo-level \cwm{}--\traj{} comparison does not survive correction (adjusted $p{=}0.078$); we interpret this difference as directionally consistent but not confirmatory.
413	
414	\section{Mixed-Effects Regression}
415	\label{app:interaction}
416	
417	We fit mixed-effects linear probability models (LPM) to test the formulation$\times$complexity interaction formally. We choose LPM because coefficients are directly interpretable as probability differences (percentage points), consistent with the reporting units in the main text; at these sample sizes ($n{\approx}56$K cross-complexity, repo-level pooled cross-model) and base rate range (0.6--0.9), LPM and logistic regression yield identical significance conclusions~\cite{angrist2009mostly}.
418	
419	\paragraph{Cross-complexity model (DeepSeek-Coder).} \texttt{correct $\sim$ formulation $\times$ complexity + (1|problem\_id)}, $n{=}56{,}480$ observations (\cls{} + \cwm{} $\times$ function + repo), 139 problem clusters. The \cwm{} main effect at function level is non-significant ($\hat{\beta}{=}-0.002$, $z{=}-0.25$, $p{=}0.805$); the \cwm{}$\times$repo interaction is highly significant ($\hat{\beta}{=}-0.219$, $z{=}-23.7$, $p{<}0.001$). \cwm{} and \cls{} are statistically indistinguishable at function level ($\Delta{=}-0.2$\pp{}, $p{=}0.805$) but diverge by 22\pp{} at repo level, confirming the complexity-dependent divergence is not an artifact of aggregation.
420	
421	\paragraph{Repo-level cross-model model.} \texttt{correct $\sim$ formulation $\times$ model + (1|problem\_id)}, both model families, repo level only. \cwm{} deficit: $\hat{\beta}{=}-0.22$ ($-$22\pp{}, $z{=}-64.4$, $p{<}0.001$). Model effect: +1.1\pp{} for Qwen3 ($z{=}3.1$, $p{=}0.002$). Formulation$\times$model interaction: +1.6\pp{} less \cwm{} degradation on Qwen3 ($z{=}2.8$, $p{=}0.006$). Formulation explains $>$95\% of the predictable variance; model identity modulates gap magnitude without changing direction. The 25-cluster random intercept structure limits effective degrees of freedom for the random effects; inferences on fixed effects (formulation, complexity) are robust as they pool across the full observation count.
422	
423	\section{CWM Parseable Bias Analysis}
424	\label{app:parseable_bias}
425	
426	The default-to-pass assignment for unparseable \cwm{} outputs is not random with respect to instance difficulty. Unparseable instances have significantly higher pass rates than parseable ones (74.6\% vs.\ 68.3\%, $\chi^2$ $p = 5.9 \times 10^{-10}$), and \cls{} models achieve higher accuracy on unparseable instances (86.4\% vs.\ 79.1\%, $p = 3.3 \times 10^{-18}$). This indicates that \cwm{}'s parsing failures concentrate on simpler, pass-heavy instances where the majority-class default happens to be correct more often. Cross-model Jaccard overlap of unparseable instance sets is 0.46, confirming this pattern is instance-driven (specific inputs consistently cause parsing failure across models) rather than stochastic. The net effect is that \cwm{}'s reported accuracy is inflated by default-correct assignments on easy instances, while its effective discriminative accuracy on harder instances is substantially lower than the aggregate figure suggests.
427	
428	
429	\section{Threats to Validity (Full Analysis)}
430	\label{app:threats}
431	
432	We identify five potential confounds and assess their impact on our conclusions.
433	
434	\paragraph{Checkpoint selection.} Val-based selection is unavailable for runs with NaN validation loss (all \cwm{} repo-level runs, DeepSeek \cls{} s123), which default to the final epoch checkpoint. A checkpoint ablation on Qwen3-8B \cls{} s42 quantifies this confound: epoch~1 (ckpt-2200) achieves 85.34\%, val-selected (ckpt-3600) 84.48\%, and final epoch (ckpt-6633) 85.29\%---a $<$1\pp{} range. The val-selected checkpoint is the lowest, indicating no upward bias from checkpoint selection. The Qwen3-8B \traj{} comparison (epoch 2: 72.92\% vs.\ epoch 3: 70.83\%) shows a slightly larger ${\sim}$2\pp{} shift. No \cwm{} overtraining is observed: epoch 2 and 3 final checkpoints achieve comparable running accuracy (${\sim}$65\%, $<$2\pp{} difference) at matched settings.
435	
436	\paragraph{Evaluation sequence length.} \cwm{} accuracy varies by ${\sim}$9\pp{} across evaluation sequence lengths for the same checkpoint (seq2048: ${\sim}$65\% vs.\ seq4096: ${\sim}$56\%), driven by unparseable-rate differences that propagate through majority-class default assignment. \cls{} is invariant to this parameter. Cross-model \cwm{} comparisons use different eval lengths (Qwen3: 8192, DeepSeek: 4096) and are not directly comparable in absolute terms. A matched-sequence evaluation shows ${\sim}$1.5\pp{} difference for \cls{} (Appendix~\ref{app:ablations}), insufficient to explain the 19--26\pp{} gap. Furthermore, increasing Qwen3-8B \cwm{} evaluation from seq4096 to seq8192 \emph{raises} the unparseable rate (63.7\%$\to$74\%) while changing accuracy by only 0.81\pp{} (64.36\%$\to$65.17\%); giving the model more generation budget worsens format compliance rather than improving it, confirming that format collapse is a structural bottleneck rather than a truncation artifact. Practitioners must standardize evaluation sequence length for generation-based formulations.
437	
438	\paragraph{Preprocessing.} DeepSeek \cls{} accuracy ranges from 82.61\% (s42, drop preprocessing) to 74.93\% (s123, truncate preprocessing), a 7.68\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \cls{} $>$ \cwm{} holds under both strategies (Table~\ref{tab:taxonomy}).
439	
440	\paragraph{\traj{} training regime.} \traj{} uses a different training configuration: smaller training set (${\sim}$400 repo-level variants vs.\ ${\sim}$70K per-test instances), higher learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level labels. This asymmetry is inherent to the formulation (trajectory-level labels are only available at variant granularity), but precludes training-data-controlled comparison at repo level. The downsample ablation confirms the \cls{} formulation advantage persists at matched data volume (80.74\% vs.\ 72.92\%; Appendix~\ref{app:downsample}), though it controls for training volume but not label granularity (per-test vs.\ variant-level). Crucially, \traj{} achieves statistical equivalence with \cls{} at function level (${\leq}$1.3\pp{}, \S\ref{sec:func_results}), demonstrating the formulation itself is viable; the repo-level gap is more consistent with data scarcity (${\sim}$400 variants vs.\ ${\sim}$70K per-test instances) than with a formulation-level limitation.
441	
442	\paragraph{\cwm{} scale and pretraining.} Our \cwm{} baseline uses 4--8B LoRA fine-tuning without execution trace pretraining. The original Code World Model~\cite{meta2025cwm} uses 32B parameters with mid-training on execution traces, a fundamentally different training regime. At larger scale or with execution-trace pretraining, the generation bottleneck observed here may diminish: larger models produce more coherent long-form outputs, and execution trace exposure may improve output format compliance. This is the primary limitation: all repo-level \cwm{} conclusions are conditional on the ${\leq}$8B LoRA regime.
443	
444	Despite these confounds, the repo-level \cls{}--\cwm{} gap (19--26\pp{}) exceeds any single assessed confound. Even under worst-case compounding (${\sim}$11.5\pp{}), the gap retains ${\geq}$7.5\pp{} margin; confounds predominantly disadvantage \cwm{}. However, correlated confounds and limited seed coverage mean definitive causal attribution requires multi-seed replication. At $n{=}48$, the minimum detectable effect (MDE) is ${\sim}$25\pp{}~\cite{hoenig2001}; the \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, while the \cls{}--\traj{} gap ($<$10\pp{}) falls below it, consistent with our TOST equivalence finding. Holm-Bonferroni correction across the four primary comparisons ($k{=}4$) confirms both the \cls{}--\cwm{} gap (adjusted $p{=}0.012$) and function-level equivalence (adjusted $p{=}0.021$) survive; the repo-level \cwm{}--\traj{} comparison is directionally consistent but does not survive correction (adjusted $p{=}0.078$; Table~\ref{tab:holm}). The consistent direction across both model families and all tested configurations supports a formulation-level explanation, though definitive causal attribution requires future experiments addressing each confound individually.
445	
446	
447	\section{Extended Limitations}
448	\label{app:limitations}
449	
450	The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline); val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \cwm{} 8B comparison is also single-seed. The validation and test sets have zero problem overlap but differ in mutation type composition (Table~\ref{tab:mutation_distribution}): \texttt{operator\_swap} shifts from 19.1\% (val) to 34.3\% (test), the largest single-type distribution mismatch (+15.2\pp{}). All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches. While mutation testing literature establishes that mutants are reasonable proxies for real faults in test effectiveness studies~\cite{andrews2005mutation,just2014mutants}, these findings concern mutation \emph{adequacy} (whether tests that kill mutants also detect real faults), not whether verifiers trained on mutants transfer to real patches. However, the coupling effect underlying these results supports \emph{relative ranking} validity: a domain shift from synthetic mutations to real bugs may affect absolute accuracy levels, but our core finding---that formulation choice matters at repo level but not function level---concerns relative performance ordering, which is expected to be preserved under distributional shifts that affect all formulations equally. The synthetic-to-real transfer gap for absolute accuracy remains untested. The \traj{} training configuration differs from \cls{}/\cwm{}: smaller training set (${\sim}$400 vs.\ ${\sim}$70K instances), different learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level evaluation ($n{=}48$ vs.\ per-test $n{=}9{,}784$). The function-level TOST equivalence ($p = 0.007$, $\pm$2\pp{}) is computed on 523 matched variant-level instances across 5 seeds; 2 of 5 seeds use NF4 quantization. Restricting to three bfloat16 seeds yields a comparable mean gap ($-$0.45\pp{}) but wider confidence interval (df${=}$2); the TOST $p$-value increases from 0.007 to 0.128, which reflects reduced statistical power rather than a shift in the point estimate. The NF4 seeds contribute precision (narrowing the CI) without shifting the mean, consistent with precision being comparable across both quantization levels at function level. Repo-level \cls{}--\traj{} comparison is preliminary due to configuration and granularity differences.
451	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "992e091d-5d69-4c2a-84ad-ee5cbc4e8181",
  "isSidechain": true,
  "promptId": "31ca5b9e-8c59-4071-ae9d-a59abbb7f73b",
  "agentId": "a6a7e9e0c43b6d074",
  "type": "user",
  "uuid": "5aac1d1d-5a84-4247-bf78-b11eae9a7ffb",
  "sourceToolAssistantUUID": "992e091d-5d69-4c2a-84ad-ee5cbc4e8181",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T07:51:50.295Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SfFTCWGUABMfJJ5L5nkuQo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5aac1d1d-5a84-4247-bf78-b11eae9a7ffb",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMGtgZZaqXbFNjFiorP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f932280-56b5-4238-a375-627e5954acde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxxPQYLUwDWV8t8YMtvKYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6647,
      "cache_read_input_tokens": 8256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6647,
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

### Tool result

_source line 9 · 2026-05-21T07:51:50.299Z_

<details><summary>↩ Tool result · `toolu_01SfFTCWGUABMfJJ5L5nkuQo`</summary>

```text
1	\begin{abstract}
2	LLM-based program repair increasingly relies on generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares these formulations under matched conditions.
3	
4	We present the first systematic comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is model-dependent. At repository level, a robust interaction ($z{=}-23.7$) confirms this equivalence collapses: the \cls{}--\cwm{} gap widens to 19--26\pp{} in single-seed variant-level evaluation, driven by format collapse in generation-based simulation. Gap magnitude depends on multiple confounds.
5	
6	Error complementarity and a failure mode taxonomy motivate complexity-aware formulation routing over uniform selection.
7	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f932280-56b5-4238-a375-627e5954acde",
  "isSidechain": true,
  "promptId": "31ca5b9e-8c59-4071-ae9d-a59abbb7f73b",
  "agentId": "a6a7e9e0c43b6d074",
  "type": "user",
  "uuid": "ea3a2125-c577-4b8d-93f2-2740f4b08fc0",
  "sourceToolAssistantUUID": "5f932280-56b5-4238-a375-627e5954acde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T07:51:50.826Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RAe2xx87nMQi7V66JqFaGF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea3a2125-c577-4b8d-93f2-2740f4b08fc0",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMGtgZZaqXbFNjFiorP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be77618a-8597-426d-bce5-5c685c85dfb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxxPQYLUwDWV8t8YMtvKYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6647,
      "cache_read_input_tokens": 8256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6647,
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

### Tool result

_source line 11 · 2026-05-21T07:51:50.830Z_

<details><summary>↩ Tool result · `toolu_01RAe2xx87nMQi7V66JqFaGF`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	These three formulations represent discrete points in the verification design space, each imposing different output complexity, diagnostic granularity, and inference cost. We present the first systematic empirical comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our contribution is primarily methodological: a matched experimental framework that isolates formulation effects from confounding variables. The analysis also produces actionable outputs: a failure mode taxonomy that characterizes when and why each formulation fails (\S\ref{sec:repo}), error complementarity findings with practical ensemble implications (\S\ref{sec:analysis}), and formulation selection recommendations conditioned on code complexity (\S\ref{sec:conclusion}). The results reveal a three-layer structure. Fine-tuning is necessary (0-shot$\to$fine-tuned gains of 35--36\pp{} at repo level). After fine-tuning, \emph{formulation choice is governed by code complexity}: at function level, all formulations achieve comparable accuracy---consistent with the theoretical analysis in \S\ref{sec:failure-modes}, which predicts that short outputs minimize generation-specific failures. At repository level under our ${\leq}$8B LoRA protocol, this equivalence collapses; variant-level analysis reveals three distinct failure modes consistent across model families, though gap magnitude depends on multiple confounds (\S\ref{sec:threats}). Figure~\ref{fig:reformulation} illustrates the three formulations.
9	
10	We make the following contributions:
11	
12	\begin{itemize}[leftmargin=*,itemsep=2pt]
13	\item \textbf{Formulation near-equivalence at low complexity.} At function level, \cls{} and \cwm{} achieve statistical equivalence across two representative code LLM families; \traj{} reaches parity on Qwen3 but exceeds the equivalence margin on DeepSeek-Coder. Per-test classification matches trajectory-level accuracy while identifying which tests fail (\S\ref{sec:func_results}, \S\ref{sec:equivalence}).
14	
15	\item \textbf{Complexity-dependent divergence.} A robust interaction ($z{=}-23.7$, $n{=}56{,}480$) confirms that formulations equivalent at function level (${\leq}$1.3\pp{}) diverge by 19--26\pp{} at repository level under ${\leq}$8B LoRA fine-tuning, driven by format collapse---four targeted interventions all fail to close the gap (Appendix~\ref{app:extended_analysis}(g)). Variant-level analysis reveals three failure modes consistent across model families, though gap magnitude depends on single-seed evaluation and multiple confounds (\S\ref{sec:repo}, \S\ref{sec:threats}).
16	
17	\item \textbf{Error complementarity.} \cls{} and \cwm{} exhibit partially complementary error patterns at function level (oracle: 90.63\%; single-seed); at repo level, oracle routing reaches 95.83\% variant accuracy (+14.58\pp{}; single-seed), the strongest practical argument for exploring the formulation design space (\S\ref{sec:analysis}).
18	\end{itemize}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be77618a-8597-426d-bce5-5c685c85dfb1",
  "isSidechain": true,
  "promptId": "31ca5b9e-8c59-4071-ae9d-a59abbb7f73b",
  "agentId": "a6a7e9e0c43b6d074",
  "type": "user",
  "uuid": "9a00fb23-2eb6-4b21-903b-8883d4d4fe07",
  "sourceToolAssistantUUID": "be77618a-8597-426d-bce5-5c685c85dfb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T07:51:51.301Z_

<details open><summary>🔧 Tool call — Read · `toolu_017SQKmgjUw34eApQCvuwmPj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a00fb23-2eb6-4b21-903b-8883d4d4fe07",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMGtgZZaqXbFNjFiorP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea8c4307-aa03-4257-981f-3479d7d59483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxxPQYLUwDWV8t8YMtvKYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6647,
      "cache_read_input_tokens": 8256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6647,
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

### Tool result

_source line 13 · 2026-05-21T07:51:51.305Z_

<details><summary>↩ Tool result · `toolu_017SQKmgjUw34eApQCvuwmPj`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation has characteristic failure modes that differ in their sensitivity to code complexity:
21	
22	\paragraph{Generation failure modes (\cwm{}).} The open-ended output space introduces three failure modes: (1)~\emph{token-budget exhaustion}, where $|o_i^*| > B$ guarantees exact-match failure due to truncation; (2)~\emph{string-value prediction errors}, where semantically equivalent outputs differing in surface form (floating-point precision, dictionary ordering) produce false negatives; and (3)~\emph{format compliance collapse}, where the model fails to produce structured predictions entirely at high input complexity, even when the generation budget is sufficient. Under optimistic independence, a token sequence of length $L$ with per-token accuracy $q$ has correct-sequence probability $q^L$; long outputs are therefore exponentially harder to predict exactly. We adopt exact string matching following the original \cwm{} evaluation protocol~\citep{meta2025cwm}. Unparseable predictions default to the majority-class label (\textsc{Pass}).
23	
24	\paragraph{Classification failure modes (\cls{}).} The single-token output space eliminates format and truncation failures but constrains the model to encode its reasoning entirely within internal representations, without the intermediate reasoning trace that generation provides. \cls{} errors manifest as false positives or false negatives without format failures; at function level, a mild FP bias (56.5\%) emerges, with the error direction depending on class distribution and fine-tuning dynamics.
25	
26	\paragraph{Trajectory-level failure modes (\traj{}).} By collapsing all per-test information into a single binary verdict, \traj{} discards diagnostic granularity. When a patch fails multiple tests, the trajectory-level formulation cannot identify \emph{which} tests fail. This limits downstream utility (e.g., targeted re-repair) but avoids per-test aggregation errors.
27	
28	\paragraph{Complexity dependence.} These failure modes suggest a complexity-dependent interaction: when execution outputs are short and structured (function-level code), generation modes (1)--(2) are rarely triggered, and all formulations should perform comparably. As output length and structural complexity increase (repository-level code), generation-specific failures may compound, creating divergence. Whether this divergence reflects a fundamental property of the generation formulation or is contingent on model/tokenizer properties is an empirical question we investigate in \S\ref{sec:experiments}.
29	
30	\subsection{Oracle Accuracy-Utility Framework}
31	\label{sec:oracle}
32	
33	For a buggy patch with $k = |T_{\text{f2p}}|$ fail-to-pass tests, a per-test verifier with recall $r$ detects the bug if it identifies at least one failing test: $P_{\text{detect}}(k) = 1 - (1 - r)^{k_{\text{eff}}}$, where $k_{\text{eff}} = k / (1 + (k-1)\rho)$ accounts for within-patch correlation via ICC $\rho$~\citep{shrout1979icc}. The per-test advantage over a trajectory-level baseline ($a_h$) is $\Delta(k) = P_{\text{detect}}(k) - a_h$, with population expectation $\mathbb{E}[\Delta] = \sum_{k} P(|T_{\text{f2p}}| = k) \cdot \Delta(k)$. This predicts that per-test advantage concentrates in multi-F2P-test instances and vanishes at $k{=}1$, validated in \S\ref{sec:experiments} and Appendix~\ref{app:oracle}.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea8c4307-aa03-4257-981f-3479d7d59483",
  "isSidechain": true,
  "promptId": "31ca5b9e-8c59-4071-ae9d-a59abbb7f73b",
  "agentId": "a6a7e9e0c43b6d074",
  "type": "user",
  "uuid": "368006ab-0c28-41f3-8813-9ec858cda711",
  "sourceToolAssistantUUID": "ea8c4307-aa03-4257-981f-3479d7d59483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T07:51:51.888Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NxTDFWD4K1ufhVgwRWxBQr`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "368006ab-0c28-41f3-8813-9ec858cda711",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMGtgZZaqXbFNjFiorP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae82b99d-4f39-4594-80af-21729d7df3f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxxPQYLUwDWV8t8YMtvKYd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6647,
      "cache_read_input_tokens": 8256,
      "output_tokens": 496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6647
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 496,
          "cache_read_input_tokens": 8256,
          "cache_creation_input_tokens": 6647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6647,
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

_source line 15 · 2026-05-21T07:51:51.904Z_

<details><summary>↩ Tool result · `toolu_01NxTDFWD4K1ufhVgwRWxBQr`</summary>

```text
docs/paper/main.tex
docs/paper/appendix.tex
docs/paper/checklist.tex
docs/paper/abstract.tex
docs/paper/method.tex
docs/paper/conclusion.tex
docs/paper/introduction.tex
docs/paper/experiments.tex
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae82b99d-4f39-4594-80af-21729d7df3f3",
  "isSidechain": true,
  "promptId": "31ca5b9e-8c59-4071-ae9d-a59abbb7f73b",
  "agentId": "a6a7e9e0c43b6d074",
  "type": "user",
  "uuid": "7a540ee7-b862-4e14-8baa-8d7d6de33299",
  "sourceToolAssistantUUID": "ae82b99d-4f39-4594-80af-21729d7df3f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-21T07:51:54.953Z_

Now let me read the remaining tex files that might contain numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a540ee7-b862-4e14-8baa-8d7d6de33299",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMHLzM6WHbB2Xgm74bZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c86403f-208a-4305-bda0-678db7bed9c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6Lkw7bqnAYh37ejwe9woQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29268,
      "cache_read_input_tokens": 14903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29268,
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

_source line 17 · 2026-05-21T07:51:56.429Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BQGU2bq1MY3WXhXxbWMBd3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c86403f-208a-4305-bda0-678db7bed9c1",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMHLzM6WHbB2Xgm74bZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "910ab4a8-2dea-49b5-8bd4-e41f75bc87b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6Lkw7bqnAYh37ejwe9woQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29268,
      "cache_read_input_tokens": 14903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29268,
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

_source line 18 · 2026-05-21T07:51:56.434Z_

<details><summary>↩ Tool result · `toolu_01BQGU2bq1MY3WXhXxbWMBd3`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} reaches parity on Qwen3 but not DeepSeek-Coder (2.69\pp{}). Per-test classification achieves 217$\times$ throughput (token ratio) while providing unconfirmed diagnostic signal. Complementary errors (oracle: 90.63\%/95.83\%; single-seed) motivate complexity-aware routing. At repository level under ${\leq}$8B LoRA fine-tuning, a robust interaction ($z{=}-23.7$) confirms divergence (19--26\pp{}, single-seed variant-level), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}). \cls{} is recommended for throughput; behavior at larger scale remains open~\cite{meta2025cwm}.
5	
6	\section*{Limitations}
7	
8	Most repo-level comparisons use a single seed; the gap magnitude (19--26\pp{}) exceeds any single assessed confound (\S\ref{sec:threats}), but correlated confounds and limited seeds mean definitive causal attribution requires multi-seed replication. The two-seed DeepSeek comparison is exploratory; seed-level power is insufficient for independent confirmation of the Qwen3 finding. Our \cwm{} baseline uses ${\leq}$8B LoRA fine-tuning, not the original 32B CWM with execution trace mid-training~\cite{meta2025cwm}; at larger scale, the generation bottleneck may diminish. However, matched comparison at controlled capacity isolates the formulation effect from scale confounds---complementary to work scaling execution simulators. Training data comprises synthetic mutations~\cite{andrews2005mutation,just2014mutants}; the synthetic-to-real transfer gap for absolute accuracy remains untested, though the coupling effect supports relative ranking validity: our core finding---that formulation choice matters at repo level but not function level---concerns relative ordering, expected to be preserved under distributional shifts that affect all formulations equally (Appendix~\ref{app:limitations}). \traj{} training uses variant-level labels (386 instances vs.\ ${\sim}$70K for \cls{}/\cwm{}), which limits direct comparison. A re-repair pilot ($n{=}44$, $p{=}0.42$; Appendix~\ref{app:extended_analysis}(j)) found no benefit from per-test diagnostics. The mixed-effects regressions use 25--139 problem-level clusters (cross-model and cross-complexity respectively); fixed-effect estimates pool across $>$56K observations, but the random-effects structure has limited resolution for the 25-cluster model. Model coverage is limited to 6--8B code-specialized LLMs; generalization to larger or general-purpose models is untested. Extended discussion: Appendix~\ref{app:limitations}. All code, data, and model checkpoints will be released upon acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "910ab4a8-2dea-49b5-8bd4-e41f75bc87b9",
  "isSidechain": true,
  "promptId": "31ca5b9e-8c59-4071-ae9d-a59abbb7f73b",
  "agentId": "a6a7e9e0c43b6d074",
  "type": "user",
  "uuid": "f83f3fb6-c6d3-4f1c-b732-944739e4fc91",
  "sourceToolAssistantUUID": "910ab4a8-2dea-49b5-8bd4-e41f75bc87b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T07:51:56.842Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MoUC1dk5LBY1bMjr6uRNcn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f83f3fb6-c6d3-4f1c-b732-944739e4fc91",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMHLzM6WHbB2Xgm74bZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6987956a-7ada-42b5-a637-7986236731a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6Lkw7bqnAYh37ejwe9woQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29268,
      "cache_read_input_tokens": 14903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29268,
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

_source line 20 · 2026-05-21T07:51:56.846Z_

<details><summary>↩ Tool result · `toolu_01MoUC1dk5LBY1bMjr6uRNcn`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. Verification formulations span trajectory-level reward~\cite{shum2025swerm,zhu2026codescaler}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. Our \cls{} provides per-test (process) supervision while \traj{} provides outcome-level; the PRM literature compares supervision granularity given a fixed output format, while we additionally vary the output format (\cwm{} generation vs.\ \cls{} classification).
9	
10	\paragraph{Repair, Mutation Testing, and Task Framing.}
11	CodeRL~\cite{le2022coderl}, AlphaCode~\cite{li2022alphacode,alphacode2023team}, and Reflexion~\cite{shinn2023reflexion} use execution feedback for repair. SWE-bench~\cite{jimenez2024swebench,chowdhury2024swebenchverified} provides benchmarks; SWE-agent~\cite{yang2024sweagent} and Agentless~\cite{xia2024agentless} demonstrate pipelines where verification is a bottleneck~\cite{yang2025aprsurvey}. Predictive mutation testing~\cite{tufano2019predictive,kim2022predictive,wang2024llmmutation,jain2023contextual} shares our per-test structure. LoRA~\cite{hu2022lora} and QLoRA~\cite{dettmers2024qlora} enable parameter-efficient fine-tuning. Task framing---how a problem is cast as a model's input--output mapping---systematically affects performance: \citet{raffel2020t5} showed that classification, generation, and span-extraction formulations yield different accuracy--efficiency tradeoffs across NLP tasks. We apply this paradigm to code verification, holding architecture and training data constant while varying only the formulation; our finding that complexity moderates the classification--generation tradeoff extends their analysis to a new domain.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6987956a-7ada-42b5-a637-7986236731a3",
  "isSidechain": true,
  "promptId": "31ca5b9e-8c59-4071-ae9d-a59abbb7f73b",
  "agentId": "a6a7e9e0c43b6d074",
  "type": "user",
  "uuid": "3080494f-cd59-44d6-a42a-774273871b00",
  "sourceToolAssistantUUID": "6987956a-7ada-42b5-a637-7986236731a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T07:51:57.316Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KCLgCtmJ5TWphfa9N6YqyN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3080494f-cd59-44d6-a42a-774273871b00",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMHLzM6WHbB2Xgm74bZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad14168a-eed7-4b41-a3fd-b1adef0c4e6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6Lkw7bqnAYh37ejwe9woQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29268,
      "cache_read_input_tokens": 14903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29268,
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

_source line 22 · 2026-05-21T07:51:57.337Z_

<details><summary>↩ Tool result · `toolu_01KCLgCtmJ5TWphfa9N6YqyN`</summary>

```text
1	% ARR Responsible NLP Research Checklist
2	% Reference: https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	This paper follows the ARR Responsible NLP Research checklist.
7	
8	\subsection*{A. For Every Submission}
9	
10	\paragraph{A1. Did you describe the limitations of your work?}
11	Yes. Section~\ref{sec:conclusion} (Limitations paragraph) discusses: single-seed repo-level comparisons, synthetic-to-real transfer gap, lack of downstream re-repair validation, and val-test mutation distribution mismatch. Section~\ref{sec:repo} (Limitations paragraph) discusses val-best checkpoint selection variance and single-seed constraints.
12	
13	\paragraph{A2. Did you discuss any potential risks of your work?}
14	This work compares formulations for execution-free code verification on public benchmarks. The primary application is improving automated program repair pipelines. We identify no significant risks: the methods predict test outcomes rather than generating executable code, the datasets are derived from open-source repositories, and no personally identifiable information is involved. Misuse potential is limited because the verifiers require task-specific fine-tuning on labeled data and do not generalize to arbitrary code generation.
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\paragraph{B1. Did you cite the creators of artifacts you used?}
19	Yes. All datasets (HumanEval~\cite{chen2021humaneval}, MBPP~\cite{austin2021mbpp}, SWE-bench Verified~\cite{chowdhury2024swebenchverified}), models (Qwen3~\cite{qwen2025qwen3}, DeepSeek-Coder~\cite{guo2024deepseekcoder}), and methods (LoRA~\cite{hu2022lora}, QLoRA~\cite{dettmers2024qlora}) are cited in Sections~\ref{sec:setup} and~\ref{sec:formulations}.
20	
21	\paragraph{B2. Did you discuss the license or terms for use and/or distribution of any artifacts?}
22	HumanEval is released under MIT license; MBPP under CC-BY-4.0; SWE-bench Verified under MIT license. Qwen3 models are released under Apache 2.0; DeepSeek-Coder under the DeepSeek License. All uses are consistent with their respective licenses. We do not release new artifacts in this submission.
23	
24	\paragraph{B3. Did you discuss if your use of existing artifact(s) was consistent with their intended use?}
25	Yes. All benchmarks are used for their intended purpose of evaluating code understanding and generation capabilities. SWE-bench Verified is used for repository-level evaluation as designed by its creators.
26	
27	\paragraph{B4. Did you discuss the steps taken to check whether the data contains any information that names or uniquely identifies individual people or offensive content?}
28	Not applicable. Our datasets consist of code snippets and test cases from open-source repositories. The mutation-based data construction process operates on source code only and does not involve personal data or natural language content that could contain offensive material.
29	
30	\paragraph{B5. Did you provide documentation of the artifacts?}
31	Yes. Section~\ref{sec:setup} documents dataset statistics (sizes, splits, label distributions, majority baselines). The mutation-based data construction process is described in Section~\ref{sec:setup}. Appendix~\ref{app:hyperparams} provides full hyperparameter details.
32	
33	\paragraph{B6. Did you report relevant statistics like the number of examples, details of train/test/dev splits, etc.?}
34	Yes. Section~\ref{sec:setup}: function-level 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48); repo-level ${\sim}$70K training, val $n{=}9{,}335$, test $n{=}9{,}784$ (majority baseline 72.96\%).
35	
36	\subsection*{C. Did You Run Computational Experiments?}
37	
38	\paragraph{C1. Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}
39	Yes. Models: Qwen3-4B (${\sim}$4B parameters, LoRA rank 16 $\approx$ 4M trainable), Qwen3-8B (${\sim}$8B), DeepSeek-Coder-6.7B (${\sim}$6.7B). Infrastructure: 4$\times$ NVIDIA RTX 5090 GPUs. Total compute: ${\sim}$370 GPU-hours across 223 completed runs (${\sim}$46 configurations including seeds, formulations, model sizes, and ablations). Appendix~\ref{app:hyperparams} provides per-run details.
40	
41	\paragraph{C2. Did you discuss the experimental setup, including hyperparameter search and best-found hyperparameter values?}
42	Yes. Section~\ref{sec:setup} reports the training configuration (LoRA rank 16, 3 epochs, 5 seeds with mixed precision). Appendix~\ref{app:hyperparams} provides full hyperparameter values. We use a fixed configuration rather than extensive hyperparameter search; repo-level models use validation accuracy for checkpoint selection.
43	
44	\paragraph{C3. Did you report descriptive statistics about your results with, e.g., error bars or confidence intervals?}
45	Yes. All multi-seed results report mean $\pm$ standard deviation. Confidence intervals use clustered bootstrap (114 problem clusters, 10K resamples; Section~\ref{sec:setup}). Equivalence testing uses TOST ($p = 0.007$, $\pm$2\pp{} margin; Section~\ref{sec:equivalence}). ICC quantifies within-problem correlation with design effect reported.
46	
47	\paragraph{C4. If you used existing packages, did you report the implementation and version numbers?}
48	Yes. Implementation uses HuggingFace Transformers (${\geq}$4.44), PEFT (${\geq}$0.12), PyTorch (${\geq}$2.0), bitsandbytes (${\geq}$0.43, for NF4 quantization), and Python 3.10. LoRA~\cite{hu2022lora} and QLoRA~\cite{dettmers2024qlora} configurations are detailed in Appendix~\ref{app:hyperparams}. Exact version pinning is provided in the code repository.
49	
50	\subsection*{D. Did You Use Human Annotators?}
51	
52	Not applicable. This work uses no human annotators or participants. All labels are derived from automated test execution.
53	
54	\subsection*{E. AI Assistants}
55	
56	\paragraph{E1. Did you use AI assistants (e.g., ChatGPT, Copilot) in any part of the paper writing or coding process?}
57	Yes. AI coding assistants were used during development of training and evaluation scripts. AI writing assistants were used for drafting and editing portions of the manuscript. All scientific claims, experimental design, and analysis were conducted and verified by the authors.
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad14168a-eed7-4b41-a3fd-b1adef0c4e6d",
  "isSidechain": true,
  "promptId": "31ca5b9e-8c59-4071-ae9d-a59abbb7f73b",
  "agentId": "a6a7e9e0c43b6d074",
  "type": "user",
  "uuid": "086491f9-f9d6-4238-8361-9f484eb5b0bc",
  "sourceToolAssistantUUID": "ad14168a-eed7-4b41-a3fd-b1adef0c4e6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T07:51:57.843Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EvZxAcBowbNGBTq8WbvEta`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "086491f9-f9d6-4238-8361-9f484eb5b0bc",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMHLzM6WHbB2Xgm74bZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4a6c88b-1775-4e88-b0c7-048ef198bb50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6Lkw7bqnAYh37ejwe9woQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29268,
      "cache_read_input_tokens": 14903,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29268
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 14903,
          "cache_creation_input_tokens": 29268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29268,
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

_source line 24 · 2026-05-21T07:51:57.849Z_

<details><summary>↩ Tool result · `toolu_01EvZxAcBowbNGBTq8WbvEta`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Math
7	\usepackage{amsmath}
8	\usepackage{amssymb}
9	
10	% Tables
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{tabularx}
14	
15	% Graphics
16	\usepackage{graphicx}
17	\graphicspath{{../../artifacts/}}
18	
19	% Lists
20	\usepackage{enumitem}
21	
22	% Custom commands
23	\newcommand{\cls}{\textsc{Cls}}
24	\newcommand{\cwm}{\textsc{Cwm}}
25	\newcommand{\traj}{\textsc{Traj}}
26	\newcommand{\fone}{F\textsubscript{1}}
27	\newcommand{\pp}{\,\text{pp}}
28	\newcommand{\tbd}{\textsc{tbd}}
29	
30	\title{The Formulation Design Space for Execution-Free Code Verification:\\A Systematic Empirical Study}
31	\author{Anonymous}
32	
33	\begin{document}
34	\maketitle
35	
36	\input{abstract}
37	
38	\input{introduction}
39	
40	\begin{figure*}[t]
41	\centering
42	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
43	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
44	\label{fig:reformulation}
45	\end{figure*}
46	
47	\input{method}
48	
49	\input{experiments}
50	
51	\begin{figure}[t]
52	\centering
53	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
54	\caption{Gap amplification from function to repo level. At function level, the \cls{}--\cwm{} gap is 1--3\pp{}; at repo level, it widens to 19--26\pp{} with \cwm{} falling below majority baseline.}
55	\label{fig:scaling_gap}
56	\end{figure}
57	
58	
59	\input{related_work}
60	
61	\input{conclusion}
62	
63	\bibliography{references}
64	
65	\input{checklist}
66	
67	\input{appendix}
68	
69	\end{document}
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4a6c88b-1775-4e88-b0c7-048ef198bb50",
  "isSidechain": true,
  "promptId": "31ca5b9e-8c59-4071-ae9d-a59abbb7f73b",
  "agentId": "a6a7e9e0c43b6d074",
  "type": "user",
  "uuid": "6c682df8-1a63-41b7-806d-23fbc9bace0c",
  "sourceToolAssistantUUID": "a4a6c88b-1775-4e88-b0c7-048ef198bb50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-21T07:52:00.588Z_

Now I have all the data. Let me compile the comprehensive report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c682df8-1a63-41b7-806d-23fbc9bace0c",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMHnPZuXxH1PrQ4QWef",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2cf574b8-d4bb-4ce2-8d1e-e52c7592cfa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WvpitXXopwGQhEbrdEvpKi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4741,
      "cache_read_input_tokens": 44171,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4741,
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

_source line 26 · 2026-05-21T07:55:52.504Z_

<details open><summary>🔧 Tool call — Write · `toolu_01XDyB4dvucZyJfoR8MkFjAt`</summary>

```json
{
  "file_path": "/tmp/paper_referenced_data.md",
  "content": "# Paper Referenced Data: Complete Numeric Audit\n\n## 1. abstract.tex\n\n### Key Numbers\n- z = -23.7 (formulation x complexity interaction)\n- CLS--CWM gap: 19--26pp (repo-level, single-seed variant-level)\n- TOST: 5 seeds\n- Two model families: Qwen3, DeepSeek-Coder\n- <=8B LoRA fine-tuning\n\n---\n\n## 2. introduction.tex\n\n### Key Numbers\n- z = -23.7, n = 56,480 (interaction test)\n- Formulation gap at function level: <=1.3pp\n- Formulation gap at repo level: 19--26pp\n- Oracle function-level: 90.63% (single-seed)\n- Oracle repo-level variant: 95.83% (+14.58pp, single-seed)\n- 0-shot -> fine-tuned gains: 35--36pp at repo level\n- DeepSeek-Coder CLS--TRAJ gap: 2.69pp\n- CLS throughput: 217x over CWM (token ratio)\n- Four targeted interventions all fail (Appendix (g))\n\n---\n\n## 3. method.tex\n\n### Key Numbers\n- No specific experimental results (theoretical framework only)\n- ICC rho referenced conceptually\n- FP bias: 56.5% (CLS, function-level, cited in failure mode discussion)\n\n---\n\n## 4. experiments.tex\n\n### Table 1 (tab:main_results) — Function-Level Per-Test Accuracy on HumanEval+MBPP (n=1,890)\n\n| Method | Model | Seeds | Accuracy (%) |\n|--------|-------|-------|-------------|\n| **Qwen3 (primary)** | | | |\n| CLS (fine-tuned) | 4B | 5 | **88.43 +/- 0.78** |\n| CWM (fine-tuned) | 4B | 5 | 87.19 +/- 0.37 |\n| TRAJ (fine-tuned) | 4B | 5 | 86.30 +/- 0.97 |\n| **DeepSeek-Coder (cross-model)** | | | |\n| CLS (fine-tuned) | 6.7B | 2 | **86.85 +/- 0.11** |\n| CWM (fine-tuned) | 6.7B | 2 | 86.83 +/- 1.49 |\n| TRAJ (fine-tuned) | 6.7B | 2 | 84.16 +/- 1.30 |\n| **Prompting baselines** | | | |\n| 0-shot | 8B (Qwen3) | 1 | 68.70 |\n| 0-shot | 6.7B (DeepSeek) | 1 | 63.00 |\n| ZS LLM-as-judge | 8B (Qwen3) | 1 | 64.40 |\n| ZS LLM-as-judge | 6.7B (DeepSeek) | 1 | 56.56 |\n| ZS LLM-as-judge | 32B (NF4) | 1 | 71.69 |\n| 3-shot ICL | 8B (Qwen3) | 1 | 68.78 |\n| 3-shot ICL | 6.7B (DeepSeek) | 1 | 59.95 |\n| Majority (pass) | --- | --- | 51.75 |\n\n### In-Text Function-Level Numbers\n- CLS--CWM gap: 0.02--1.24pp (within seed noise)\n- CLS--TRAJ gap on Qwen3: <1pp\n- CLS--TRAJ gap on DeepSeek-Coder: 2.69pp\n- 0-shot -> fine-tuned gains: 35--36pp\n\n### Table 2 (tab:scaling) — Model-Size Scaling (Qwen3, seeds 42/123, bf16)\n\n| Method | Size | s42 | s123 | Mean | Delta 4B->8B |\n|--------|------|-----|------|------|-------------|\n| CLS | 4B | 87.83 | 89.52 | **88.68** | +1.27 |\n| CLS | 8B | **90.48** | 89.40 | **89.94** | |\n| CWM | 4B | 87.51 | 87.20 | 87.36 | -0.03 |\n| CWM | 8B | 87.67 | 86.98 | 87.33 | |\n| TRAJ | 4B | 85.27 | 86.72 | 86.00 | +1.70 |\n| TRAJ | 8B | 87.60 | 87.79 | 87.70 | |\n\n### In-Text Scaling Numbers\n- CLS: +1.27pp (4B->8B)\n- TRAJ: +1.70pp (4B->8B)\n- CWM: -0.03pp (flat)\n- At 8B: CLS (89.94) > TRAJ (87.70) > CWM (87.33)\n- CLS--CWM gap at 4B: 1.32pp\n- CLS--CWM gap at 8B: 2.62pp\n- Clustered bootstrap p = 0.0066, 95% CI [1.80, 2.71] (3-seed superset: 42, 123, 456)\n- CWM avg output tokens: ~477 tokens\n- CWM unparseable: 51--74%\n- TRAJ: 72.92% at both 4B and 8B (repo-level)\n\n### Equivalence Section (sec:equivalence)\n- 523 variant-level instances, 5 seeds\n- Pooled gap: -0.45pp (95% CI [-1.71, +0.84])\n- TOST equivalence: p = 0.007 (+/-2pp margin, Holm-Bonferroni corrected)\n- ICC = 0.191, p < 0.0001, DEFF = 3.97\n- Between-seed std: 0.37--0.97pp\n- Checkpoint selection noise: <1pp\n- Equivalence holds at margins as tight as +/-1.52pp\n- DeepSeek CLS--CWM gap: 0.02pp\n- DeepSeek CLS--TRAJ gap: 2.69pp\n- bfloat16 only (3 seeds): p = 0.128\n- Oracle on SWE-bench Verified: 500 instances\n- Per-test advantage at T>=2: 31.3% of instances, 55.3% of total oracle advantage\n\n### Table 3 (tab:repo_level) — Repo-Level Cross-Formulation Comparison\n\n| Model | CLS (%) | CLS Var (%) | CWM (%) | TRAJ Var (%) |\n|-------|---------|-------------|---------|-------------|\n| Qwen3-4B | 83.63 | 64.58 | 58.04 | 72.92 |\n| Qwen3-8B | **84.83 +/- 0.67** | 72.92 / 81.25 | TBD | 72.91 +/- 3.61 |\n| DeepSeek-6.7B | 84.38 +/- 2.50 | 81.25 | TBD | 77.08 +/- 3.61 |\n| 0-shot (Qwen3-8B) | 49.90 | --- | --- | --- |\n| 0-shot (DeepSeek) | 48.50 | --- | --- | --- |\n| Majority | 72.96 | 54.17 | 72.96 | 54.17 |\n\n### Repo-Level In-Text Numbers\n- Zero-shot: always-predict-unresolved baseline 45.83%, below majority 54.17%\n- CLS vs CWM divergence at 4B: 25.59pp (CLS 83.63% vs CWM 58.04%, seed 42)\n- CLS vs CWM divergence at 8B: 19.31pp (84.48% vs 65.17%)\n- DeepSeek CLS degradation: ~4pp (s42, drop) to ~12pp (s123, truncate)\n- DeepSeek CWM val-selected: 56.70%\n- DeepSeek CWM epoch-3: 61.49%\n- Matched checkpoint gap difference: Qwen3 20.47pp vs DeepSeek 22.89pp (~2pp difference)\n- CWM unparseable rate: 53.7% (4B) -> 73.8% (8B)\n- Parseable-only accuracy: 42.88% (4B) -> 38.52% (8B)\n- CWM unparseable: 54% (4B in table note)\n- CWM parseable-only: 38--43% (below majority)\n- Downsampled CLS: 80.74% (still 7.82pp above TRAJ)\n\n### Table 4 (tab:taxonomy) — Repo-Level Failure Mode Taxonomy\n\n| Failure Mode | Representative | Fail Recall | Variant Acc |\n|-------------|---------------|-------------|-------------|\n| Format collapse | CWM (all) | N/A | 48--52% |\n| Decision collapse | CLS (DeepSeek, s123) | ~14% | 56% |\n| Aggr. penalty | CLS (Qwen3-8B) | 51--57% | 73--81% |\n| Aggr. penalty | CLS (DeepSeek, s42) | 38--51% | 79--81% |\n\n### Mixed-Effects Model Numbers\n- n = 56,480 observations, 139 problem clusters, DeepSeek-Coder\n- CWM effect at function level: beta = -0.002, p = 0.805\n- Formulation x complexity interaction: z = -23.7, p < 0.001\n- CWM and CLS at function level: Delta = -0.2pp\n- Divergence at repo level: 22pp\n- Cross-model CWM deficit: -22pp, z = -64.4, p < 0.001\n- Model effect: +1.1pp for Qwen3, p = 0.002\n- Formulation x model interaction: +1.6pp, p = 0.006\n- Formulation explains >95% of predictable variance\n\n### Analysis Section Numbers\n- Aggregation penalty range: 1.36pp (DeepSeek s42) to 19pp (Qwen3-4B)\n- TRAJ: 72.91--77.08% variant accuracy\n- Function-level avg T: ~2.3\n- CWM avg output: ~477 tokens\n- CWM unparseable: 53--74%\n- CWM parseable accuracy: 38--43%\n- CLS FP rate: 56.5%\n- CWM FP rate: 70.3%\n- Oracle combination (func): 90.63% (+2.80pp over best single, CLS 87.83%; seed 42)\n  - 1713/1890 correct, 177 both-wrong\n- Oracle routing (repo-level variant): 95.83% (+14.58pp, n=48)\n- Re-repair pilot: n=44, p=0.42, A1=52.3%, effect size ~0\n- CLS throughput: 217x over CWM (1 token vs avg 477 tokens)\n\n### Threats Numbers\n- Checkpoint selection: <1pp variation\n- Eval seq length: ~1.5pp\n- Preprocessing: ~8pp cross-config variance\n- Gap: 19--26pp exceeds any single confound\n- Holm-Bonferroni adjusted p = 0.012 (repo CLS vs CWM)\n- Holm-Bonferroni adjusted p = 0.021 (func CLS-TRAJ TOST)\n\n---\n\n## 5. appendix.tex\n\n### Table: Oracle Accuracy-Utility (tab:oracle) — SWE-bench Verified (500 instances)\n\n| T | Inst.% | i.i.d. (pp) | Block (pp) | Contrib.% |\n|---|--------|-------------|-----------|-----------|\n| 1 | 68.7 | -0.04 | -0.09 | ~0 |\n| 2 | 19.1 | 18.49 | 31.69 | 55.3 |\n| 3--5 | 7.1 | 25.00 | 40.74 | ~26 |\n| >=6 | 5.1 | 30.00 | 40.06 | ~19 |\n| **All** | 100.0 | --- | **10.93** | 100.0 |\n\n- P2P regression rate: 1.04% mean, 0% median\n- ICC = 0.191 (function-level)\n- Block amplification at T=2: 31.69pp vs 18.49pp (1.7x)\n- Overall block-correlated advantage: 10.93pp\n- Repo-level ICC: 0.3146, DEFF = 114.4\n- Function-level mean cluster size: k ~ 16.5\n\n### Table: LoRA Rank Ablation (tab:rank_ablation) — CWM 4B, seed 42\n\n| Config | alpha/r | Acc (%) | Fail F1 | Pass F1 | Delta |\n|--------|---------|---------|---------|---------|-------|\n| r=16, alpha=32 | 2 | **87.51** | --- | --- | --- |\n| r=32, alpha=32 | 1 | 87.00 | 87.1 | 86.9 | -0.51 |\n| r=32, alpha=64 | 2 | 87.04 | 87.27 | 86.79 | -0.47 |\n\n- Rank-16 seed variance: 0.53pp (seeds 42 vs 456)\n- Majority voting K=3: 87.51% -> 86.83% (-0.68pp)\n- 93.3% of samples unanimous; net flips negative (-13)\n\n### Sequence-Length Ablation\n- CLS 8B at 2,048 tokens: 83.04% (1.44pp below 8,192-token: 84.48%)\n- Truncation: 136 unparseable outputs (1.39% of test samples)\n- Matched-context gap (CLS@2048 vs CWM@2048): 25.00pp (98% of full 25.59pp gap)\n- Input context disparity explains at most 3%\n\n### Training Data Size Control (app:downsample)\n- Downsampled CLS (Qwen3-4B, seed 42): 80.74% repo-level per-test\n- Full-data CLS: 83.63% (difference 2.89pp)\n- TRAJ: 72.92% (7.82pp below downsampled CLS)\n\n### Table: Few-Shot Prompting (tab:few_shot) — Repo-Level\n\n| Model | 0-shot (per-test) | 3-shot (per-test) | 3-shot (variant) |\n|-------|-------------------|-------------------|-------------------|\n| Qwen3-8B | 49.90% | 71.61% | 45.83% |\n| DeepSeek-6.7B | 48.54% | 46.28% | 45.83% |\n\n- Both: 45.83% variant-level = always-predict-unresolved baseline (22/48)\n- Majority baseline: 72.96% per-test, 54.17% variant-level\n\n### Table: Per-Mutation Breakdown (tab:mutation_breakdown) — Repo-Level (n=9,784)\n\n| Mutation | n | CLS 4B | CLS 8B s42 | CLS 8B s123 | CWM 4B | CWM 8B | Delta CLS |\n|----------|---|--------|------------|-------------|--------|--------|-----------|\n| gold | 4,633 | 98.25 | 96.24 | 99.60 | 66.72 | 80.06 | -0.33 |\n| operator_swap | 3,357 | 78.91 | 81.38 | 82.60 | --- | 54.57 | +3.08 |\n| off_by_one | 183 | 58.47 | 86.89 | 79.20 | --- | 63.39 | **+24.58** |\n| return_value | 562 | 67.97 | 75.44 | 66.40 | --- | 49.11 | +2.95 |\n| boundary_removal | 1,049 | 46.90 | 46.90 | 44.90 | --- | 42.23 | -1.00 |\n\n### Table: CWM Parse Rates (tab:cwm_mutation_parse) — seed 42\n\n| Mutation | Parse Rate 4B (%) | Parse Rate 8B (%) | Parse Acc 4B (%) | Parse Acc 8B (%) |\n|----------|-------------------|-------------------|------------------|------------------|\n| gold | 43.5 | 23.9 | 23.5 | 16.5 |\n| operator_swap | 56.9 | 21.2 | 63.1 | 58.8 |\n| off_by_one | 4.4 | 27.3 | 0.0 | 38.0 |\n| return_value | 48.8 | 26.9 | 27.0 | 56.9 |\n| boundary_removal | 30.6 | 51.8 | 59.2 | 51.8 |\n\n- Off_by_one: n=8 parseable at 4B (extremely low base)\n\n### Table: Variant-Level Accuracy (tab:variant_level) — n=48 variants\n\n| Model | Seed | Per-test (%) | Variant (%) | Penalty (pp) | Fail Recall (%) |\n|-------|------|-------------|-------------|-------------|----------------|\n| **CLS** | | | | | |\n| Qwen3-8B | s42 | 84.48 | 72.92 | 11.56 | 56.76 |\n| Qwen3-8B | s123 | 85.60 | 81.25 | 4.35 | 51.44 |\n| Qwen3-4B | s42 | 83.63 | 64.58 | 19.05 | 48.72 |\n| DeepSeek-6.7B | s42 (e1) | 82.61 | 81.25 | 1.36 | 51.02 |\n| DeepSeek-6.7B | s42 (e3) | 82.51 | 79.17 | 3.34 | 38.47 |\n| DeepSeek-6.7B | s123 | 74.93 | 56.25 | 18.68 | ~13.72 |\n| **CWM** | | | | | |\n| Qwen3-8B | s42 | 65.17 | 52.08 | 13.09 | --- |\n| DeepSeek-6.7B | s123 | --- | 47.92 | --- | --- |\n| **TRAJ** | | | | | |\n| Qwen3-4B | s42 | --- | 72.92 | --- | --- |\n| Qwen3-8B | s42 | --- | 70.83 | --- | --- |\n| DeepSeek-6.7B | 3-seed | --- | 77.08 +/- 3.61 | --- | --- |\n| Majority | --- | 72.96 | 54.17 | --- | --- |\n\n- DeepSeek TRAJ supplementary seeds (0/789/999): 75.0%, 66.7%, 79.2%; 6-seed mean 75.35 +/- 5.00%\n\n### Val-Test Mutation Distribution (tab:mutation_distribution)\n\n| Mutation Type | Val (%) | Test (%) | Shift | CLS 4B | CLS 8B |\n|--------------|---------|----------|-------|--------|--------|\n| gold | 45.2 | 47.4 | +2.2 | 98.3 | 96.2 |\n| operator_swap | 19.1 | 34.3 | +15.2 | 78.9 | 81.4 |\n| boundary_removal | 15.0 | 10.7 | -4.3 | 46.9 | 46.9 |\n| return_value | 10.7 | 5.7 | -5.0 | 68.0 | 75.4 |\n| off_by_one | 10.0 | 1.9 | -8.1 | 58.5 | 86.9 |\n\n- Off_by_one scaling gain: +28.4pp (58.5% -> 86.9%)\n- Boundary_removal: scale-invariant ~47%\n\n### TOST Margin Sensitivity (tab:tost_sensitivity) — 5 seeds, 523 variants, 114 clusters\n\n| Margin (+/-pp) | p-value | Equivalent (alpha=0.05)? |\n|---------------|---------|--------------------------|\n| 1.0 | >>0.05 | No |\n| 1.5 | 0.054 | No (borderline) |\n| **1.52** | **~0.05** | **Smallest margin** |\n| 1.71 | 0.027 | Yes |\n| 2.0 | 0.0087 | Yes |\n| 3.0 | 4.6e-5 | Yes |\n| 5.0 | <<0.001 | Yes |\n\n### Variant-Level Effect Sizes (tab:variant_power) — n=48\n\n| Comparison | Config | Delta (pp) | 95% CI | p |\n|-----------|--------|-----------|--------|---|\n| **CLS vs CWM (paired)** | | | | |\n| | Qwen3-8B | +29.17 | [10.42, 47.92] | 0.003 |\n| | DeepSeek-6.7B | +35.42 | [18.75, 50.05] | <0.001 |\n| **CLS vs TRAJ (unpaired)** | | | | |\n| | Qwen3-4B | -4.17 | wide | 0.740 |\n| | Qwen3-8B | +8.33 | wide | 0.385 |\n| | DeepSeek-6.7B | 0.00 | wide | 1.000 |\n\n- MDE at n=48: ~25pp\n\n### Holm-Bonferroni Correction (tab:holm) — k=4\n\n| Rank | Comparison | Raw p | Factor | Adj p | Sig? |\n|------|-----------|-------|--------|-------|------|\n| 1 | Repo: CLS vs CWM | 0.003 | x4 | 0.012 | Yes |\n| 2 | Func: CLS vs TRAJ (TOST +/-2pp) | 0.0071 | x3 | 0.021 | Yes |\n| 3 | Repo: CWM vs TRAJ | 0.039 | x2 | 0.078 | No |\n| 4 | Repo: CLS vs TRAJ | 0.385 | x1 | 0.385 | No |\n\n### Mixed-Effects Regression (app:interaction)\n- Cross-complexity: n=56,480, 139 clusters, DeepSeek-Coder\n  - CWM main effect: beta=-0.002, z=-0.25, p=0.805\n  - CWM x repo interaction: beta=-0.219, z=-23.7, p<0.001\n  - Function-level delta: -0.2pp (p=0.805); repo-level: 22pp divergence\n- Repo-level cross-model:\n  - CWM deficit: beta=-0.22, -22pp, z=-64.4, p<0.001\n  - Model effect: +1.1pp Qwen3, z=3.1, p=0.002\n  - Formulation x model: +1.6pp, z=2.8, p=0.006\n  - 25-cluster random intercept structure\n\n### CWM Parseable Bias (app:parseable_bias)\n- Unparseable pass rate: 74.6% vs parseable: 68.3%, chi-sq p=5.9e-10\n- CLS accuracy on unparseable instances: 86.4% vs 79.1%, p=3.3e-18\n- Cross-model Jaccard overlap: 0.46\n\n### Threats (app:threats) — Full Analysis\n- Checkpoint ablation Qwen3-8B CLS s42:\n  - epoch 1 (ckpt-2200): 85.34%\n  - val-selected (ckpt-3600): 84.48%\n  - final epoch (ckpt-6633): 85.29%\n  - Range: <1pp\n- Qwen3-8B TRAJ: epoch 2: 72.92% vs epoch 3: 70.83% (~2pp shift)\n- CWM overtraining: epoch 2 and 3 ~65%, <2pp difference\n- CWM seq-length variation: ~9pp (seq2048: ~65% vs seq4096: ~56%)\n- CLS invariant to seq length\n- Qwen3-8B CWM seq4096 vs seq8192: unparseable 63.7% -> 74%; accuracy 64.36% -> 65.17% (0.81pp)\n- CLS matched-sequence: ~1.5pp difference\n- DeepSeek CLS: 82.61% (s42, drop) to 74.93% (s123, truncate), 7.68pp spread\n- Training samples: drop=67,343 vs truncate=70,748\n- Worst-case confound compounding: ~11.5pp, gap retains >=7.5pp margin\n\n### Extended Analysis Numbers\n- (a) CLS errors (s42): 56.5% FP (PASS->FAIL); CWM: 70.3% FP\n  - Oracle: 90.63% (1713/1890 correct, 177 both-wrong; +2.80pp over CLS 87.83%)\n- (b) Unparseable CWM outputs: 76.9% no execution keywords; 22.9% ambiguous\n- (c) Relaxed matching: 58.04% -> 56.98% (s42); 59.09% -> 55.91% (s123)\n  - Divergence widens 26pp -> 28pp\n- (d) CWM std: 0.37pp; CLS std: 0.78pp; TRAJ std: 0.97pp\n- (e) CLS fail F1: 87.59% (precision 86.20%, recall 89.04%) at seed 42\n  - FP=130, FN=100, TP=848, TN=812\n  - Multi-F2P (6-10 tests): 96.3% accuracy\n- (f) ICC=0.191, DEFF=3.97, 2.81x more all-correct problems than i.i.d.\n- (g) Failed interventions:\n  - Capacity (rank 32): -0.51pp\n  - Majority voting K=3: -0.68pp (87.51% -> 86.83%), 93.3% unanimous, -13 net flips\n  - Relaxed matching: 58.04% -> 56.98% (s42)\n  - Model scaling 4B->8B: parseable acc 42.88% -> 38.52%; unparseable 53.7% -> 73.8%\n- (h) Off_by_one scaling: 58.5% -> 86.9% (+28.4pp); boundary_removal: ~47% (scale-invariant)\n  - Gold parse rate: 43.5% (4B) -> 23.9% (8B); gold parseable acc: 16.5--23.5%\n- (i) Inference throughput:\n  - CLS: 853 inferences/min; CWM: 3.9 inferences/min (217x)\n  - Median latency: CLS 48ms vs CWM 16.3s\n  - Qwen3-4B, RTX 5090, 100 samples, avg ~1,040 input tokens\n  - CWM: avg 477 output tokens\n  - CWM unparseable: 73.8% (8B)\n  - CLS per-call: 47ms (short) to 2,632ms (TRAJ)\n  - Per-instance function-level (T~2.3): CLS ~24x faster (108ms vs 2,632ms)\n  - Per-instance repo-level (T~12.3, ~70ms/call): CLS ~3x faster (861ms vs 2,631ms)\n  - Crossover at T~50 tests\n- (j) Re-repair pilot: n=44, A1=52.3%, p=0.42, effect size ~0\n\n### Extended Limitations (app:limitations)\n- CLS 4B seed 123 (val-best ckpt-800): 75.33% (+2.4pp above majority baseline)\n- TOST p-value increases from 0.007 to 0.128 (3 bfloat16 seeds only)\n- TRAJ training set: ~400 variants vs ~70K per-test instances\n\n### Hyperparameters (tab:hyperparams)\n- LoRA rank: 16 (all configs)\n- LoRA alpha: 32 (all configs)\n- LoRA dropout: 0.05 (all configs)\n- LoRA targets: q_proj, k_proj, v_proj, o_proj\n- Learning rate: 5e-5 (Qwen3), 2e-4 (DeepSeek)\n- Optimizer: AdamW (beta1=0.9, beta2=0.999)\n- Weight decay: 0.01 (Qwen3), 0.0 (DeepSeek)\n- Warmup ratio: 0.05 (Qwen3), 0.1 (DeepSeek)\n- Scheduler: Linear\n- Per-device batch: 1 or 2\n- Grad accum: 16 or 32\n- Effective batch: 32 (all)\n- Max seq length: 2,048\n- Epochs: 3\n- Precision: bf16\n- Seeds (function): {42, 123, 456, 789, 0}\n- Seeds (repo): {42, 123, 456}\n- Training samples: 70,748 (CWM all), 67,343 (DeepSeek CLS s42 drop)\n- TRAJ lr: 2e-4\n- Total compute: ~370 GPU-hours, 223 completed runs, ~46 unique configs\n- Training time: ~1.5h (4B), ~2h (8B)\n- GPU: NVIDIA RTX 5090\n\n---\n\n## 6. conclusion.tex\n\n### Key Numbers (summary of previously cited)\n- TOST p = 0.007, 5 seeds\n- DeepSeek CLS--TRAJ: 2.69pp\n- CLS throughput: 217x (token ratio)\n- Oracle: 90.63% / 95.83% (single-seed)\n- z = -23.7 interaction\n- Gap: 19--26pp (single-seed variant-level)\n- Re-repair: n=44, p=0.42\n- Mixed-effects: 25--139 clusters, >56K observations\n- Holm-Bonferroni: adjusted p=0.012 and p=0.021\n\n---\n\n## 7. checklist.tex\n\n### Numbers\n- Function-level: 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail ~52:48)\n- Repo-level: ~70K training, val n=9,335, test n=9,784 (majority baseline 72.96%)\n- Models: Qwen3-4B (~4B params, LoRA ~4M trainable), Qwen3-8B (~8B), DeepSeek-Coder-6.7B (~6.7B)\n- Infrastructure: 4x NVIDIA RTX 5090\n- Compute: ~370 GPU-hours, 223 runs, ~46 configs\n- LoRA rank 16, 3 epochs, 5 seeds\n- TOST p=0.007, +/-2pp\n- ICC with DEFF\n- Clustered bootstrap: 114 problem clusters, 10K resamples\n- HuggingFace Transformers >=4.44, PEFT >=0.12, PyTorch >=2.0, bitsandbytes >=0.43, Python 3.10\n\n---\n\n## 8. related_work.tex\n\n### Numbers\n- None (pure literature discussion, no experimental numbers)\n\n---\n\n## MASTER LIST: All Unique Accuracy/Metric Values Referenced\n\n### Function-Level Accuracies (per-test, n=1,890)\n- 88.43% — CLS Qwen3-4B (5-seed mean)\n- 87.19% — CWM Qwen3-4B (5-seed mean)\n- 86.30% — TRAJ Qwen3-4B (5-seed mean)\n- 86.85% — CLS DeepSeek-6.7B (2-seed mean)\n- 86.83% — CWM DeepSeek-6.7B (2-seed mean)\n- 84.16% — TRAJ DeepSeek-6.7B (2-seed mean)\n- 68.70% — 0-shot Qwen3-8B\n- 63.00% — 0-shot DeepSeek-6.7B\n- 64.40% — ZS LLM-as-judge Qwen3-8B\n- 56.56% — ZS LLM-as-judge DeepSeek-6.7B\n- 71.69% — ZS LLM-as-judge 32B NF4\n- 68.78% — 3-shot ICL Qwen3-8B\n- 59.95% — 3-shot ICL DeepSeek-6.7B\n- 51.75% — Majority baseline\n\n### Per-Seed Function-Level Accuracies (from scaling table, bf16 only)\n- 87.83% — CLS Qwen3-4B s42\n- 89.52% — CLS Qwen3-4B s123\n- 90.48% — CLS Qwen3-8B s42\n- 89.40% — CLS Qwen3-8B s123\n- 87.51% — CWM Qwen3-4B s42\n- 87.20% — CWM Qwen3-4B s123\n- 87.67% — CWM Qwen3-8B s42\n- 86.98% — CWM Qwen3-8B s123\n- 85.27% — TRAJ Qwen3-4B s42\n- 86.72% — TRAJ Qwen3-4B s123\n- 87.60% — TRAJ Qwen3-8B s42\n- 87.79% — TRAJ Qwen3-8B s123\n\n### Scaling Means (2-seed, bf16)\n- 88.68% — CLS Qwen3-4B mean\n- 89.94% — CLS Qwen3-8B mean\n- 87.36% — CWM Qwen3-4B mean\n- 87.33% — CWM Qwen3-8B mean\n- 86.00% — TRAJ Qwen3-4B mean\n- 87.70% — TRAJ Qwen3-8B mean\n\n### Repo-Level Per-Test Accuracies (n=9,784)\n- 83.63% — CLS Qwen3-4B s42\n- 84.48% — CLS Qwen3-8B s42\n- 85.60% — CLS Qwen3-8B s123\n- 84.83% — CLS Qwen3-8B (3-seed mean, +/-0.67)\n- 82.61% — CLS DeepSeek-6.7B s42 (e1)\n- 82.51% — CLS DeepSeek-6.7B s42 (e3)\n- 74.93% — CLS DeepSeek-6.7B s123\n- 84.38% — CLS DeepSeek-6.7B (2-seed mean, +/-2.50)\n- 58.04% — CWM Qwen3-4B s42\n- 65.17% — CWM Qwen3-8B s42\n- 56.70% — CWM DeepSeek-6.7B (val-selected)\n- 61.49% — CWM DeepSeek-6.7B (epoch-3)\n- 49.90% — 0-shot Qwen3-8B\n- 48.50% — 0-shot DeepSeek\n- 48.54% — 0-shot DeepSeek (few_shot table version)\n- 72.96% — Majority baseline\n- 71.61% — 3-shot ICL Qwen3-8B (per-test)\n- 46.28% — 3-shot ICL DeepSeek (per-test)\n- 80.74% — Downsampled CLS Qwen3-4B s42\n- 75.33% — CLS Qwen3-4B s123 (val-best ckpt-800)\n- 83.04% — CLS Qwen3-8B at 2,048 seq length\n- 64.36% — CWM Qwen3-8B seq4096\n- 85.34% — CLS Qwen3-8B s42 (ckpt-2200, epoch 1)\n- 85.29% — CLS Qwen3-8B s42 (ckpt-6633, final epoch)\n\n### Repo-Level Variant Accuracies (n=48)\n- 64.58% — CLS Qwen3-4B s42\n- 72.92% — CLS Qwen3-8B s42\n- 81.25% — CLS Qwen3-8B s123\n- 81.25% — CLS DeepSeek-6.7B s42 (e1)\n- 79.17% — CLS DeepSeek-6.7B s42 (e3)\n- 56.25% — CLS DeepSeek-6.7B s123\n- 52.08% — CWM Qwen3-8B s42\n- 47.92% — CWM DeepSeek-6.7B s123\n- 72.92% — TRAJ Qwen3-4B s42\n- 70.83% — TRAJ Qwen3-8B s42\n- 72.91% — TRAJ Qwen3-8B (3-seed mean, +/-3.61)\n- 77.08% — TRAJ DeepSeek-6.7B (3-seed mean, +/-3.61)\n- 75.0% — TRAJ DeepSeek-6.7B s0 (supplementary)\n- 66.7% — TRAJ DeepSeek-6.7B s789 (supplementary)\n- 79.2% — TRAJ DeepSeek-6.7B s999 (supplementary)\n- 75.35% — TRAJ DeepSeek-6.7B 6-seed mean (+/-5.00)\n- 54.17% — Majority baseline\n- 45.83% — Always-predict-unresolved baseline\n- 95.83% — Oracle routing (single-seed)\n- 72.92% — TRAJ epoch 2 (Qwen3-8B)\n- 70.83% — TRAJ epoch 3 (Qwen3-8B)\n\n### Oracle/Combination Accuracies\n- 90.63% — Oracle combination (func-level, seed 42)\n- 95.83% — Oracle routing (repo-level variant, n=48)\n\n### Ablation Accuracies\n- 87.51% — CWM r=16 (baseline, seed 42)\n- 87.00% — CWM r=32, alpha=32\n- 87.04% — CWM r=32, alpha=64\n- 86.83% — CWM majority voting K=3\n\n### Per-Mutation Repo-Level Accuracies (CLS)\n- 98.25% — gold, CLS 4B\n- 96.24% — gold, CLS 8B s42\n- 99.60% — gold, CLS 8B s123\n- 78.91% — operator_swap, CLS 4B\n- 81.38% — operator_swap, CLS 8B s42\n- 82.60% — operator_swap, CLS 8B s123\n- 58.47% — off_by_one, CLS 4B\n- 86.89% — off_by_one, CLS 8B s42\n- 79.20% — off_by_one, CLS 8B s123\n- 67.97% — return_value, CLS 4B\n- 75.44% — return_value, CLS 8B s42\n- 66.40% — return_value, CLS 8B s123\n- 46.90% — boundary_removal, CLS 4B\n- 46.90% — boundary_removal, CLS 8B s42\n- 44.90% — boundary_removal, CLS 8B s123\n\n### Per-Mutation Repo-Level Accuracies (CWM)\n- 66.72% — gold, CWM 4B\n- 80.06% — gold, CWM 8B\n- 54.57% — operator_swap, CWM 8B\n- 63.39% — off_by_one, CWM 8B\n- 49.11% — return_value, CWM 8B\n- 42.23% — boundary_removal, CWM 8B\n\n### CWM Parse Rates\n- 43.5% / 23.9% — gold (4B/8B)\n- 56.9% / 21.2% — operator_swap (4B/8B)\n- 4.4% / 27.3% — off_by_one (4B/8B)\n- 48.8% / 26.9% — return_value (4B/8B)\n- 30.6% / 51.8% — boundary_removal (4B/8B)\n\n### CWM Parseable-Only Accuracies\n- 23.5% / 16.5% — gold (4B/8B)\n- 63.1% / 58.8% — operator_swap (4B/8B)\n- 0.0% / 38.0% — off_by_one (4B/8B)\n- 27.0% / 56.9% — return_value (4B/8B)\n- 59.2% / 51.8% — boundary_removal (4B/8B)\n- 42.88% — overall parseable CWM 4B\n- 38.52% — overall parseable CWM 8B\n\n### Statistical Test Values\n- TOST: p=0.007 (CLS--TRAJ equivalence, +/-2pp, Holm corrected)\n- TOST smallest margin: +/-1.52pp\n- Gap: -0.45pp (95% CI [-1.71, +0.84])\n- ICC: 0.191 (function-level), DEFF=3.97\n- ICC: 0.3146 (repo-level), DEFF=114.4\n- z=-23.7 (formulation x complexity interaction, p<0.001)\n- z=-64.4 (cross-model CWM deficit, p<0.001)\n- z=-0.25 (CWM function-level effect, p=0.805)\n- z=3.1 (model effect, p=0.002)\n- z=2.8 (formulation x model, p=0.006)\n- p=0.0066 (CLS-CWM scaling gap, 95% CI [1.80, 2.71])\n- Holm-Bonferroni adjusted: p=0.012 (repo CLS-CWM), p=0.021 (func TOST), p=0.078 (repo CWM-TRAJ), p=0.385 (repo CLS-TRAJ)\n- Variant-level bootstrap: p=0.003 (Qwen3-8B CLS-CWM), p<0.001 (DeepSeek CLS-CWM)\n- Re-repair: p=0.42, n=44, A1=52.3%\n- Parseable bias chi-sq: p=5.9e-10, p=3.3e-18\n- Jaccard overlap: 0.46\n- Relaxed matching: 58.04%->56.98% (s42), 59.09%->55.91% (s123)\n\n### Precision/Recall/F1\n- CLS fail F1: 87.59% (precision 86.20%, recall 89.04%) at seed 42\n- CWM rank=32 alpha=32: fail F1 87.1, pass F1 86.9\n- CWM rank=32 alpha=64: fail F1 87.27, pass F1 86.79\n- CLS FP rate: 56.5%, CWM FP rate: 70.3%\n- FP=130, FN=100, TP=848, TN=812 (CLS seed 42 func-level)\n\n### Fail Recall Values (Repo-Level)\n- 56.76% — CLS Qwen3-8B s42\n- 51.44% — CLS Qwen3-8B s123\n- 48.72% — CLS Qwen3-4B s42\n- 51.02% — CLS DeepSeek s42 (e1)\n- 38.47% — CLS DeepSeek s42 (e3)\n- ~13.72% — CLS DeepSeek s123\n- ~14% — Decision collapse (taxonomy)\n\n### Inference Throughput\n- CLS: 853 inferences/min, 48ms median latency\n- CWM: 3.9 inferences/min, 16.3s median latency\n- 217x throughput ratio\n- CWM avg output: 477 tokens\n- CWM unparseable: 53.7% (4B), 73.8% (8B), 63.7% (8B seq4096)\n\n### Dataset Sizes\n- Function-level: 19,076 total (train 15,290, val 1,896, test 1,890)\n- pass:fail ratio: ~52:48\n- Repo-level: ~70K training, val 9,335, test 9,784\n- Repo-level pass rate: 72.96%\n- Repo variants: n=48 (26 resolved, 22 unresolved)\n- Oracle: 500 SWE-bench Verified instances\n- TRAJ training: ~400 variants (~8K per-test equivalents)\n- DeepSeek CLS drop: 67,343 of 70,748 samples (3,405 dropped, 4.8%)\n- n=56,480 (mixed-effects cross-complexity)\n- 139 problem clusters (cross-complexity)\n- 25 problem clusters (cross-model repo)\n- 114 problem clusters (function-level bootstrap)\n- 523 variant-level instances (TOST)\n- 10K bootstrap resamples\n- Per-mutation test counts: gold 4,633; operator_swap 3,357; off_by_one 183; return_value 562; boundary_removal 1,049\n\n### Seeds Referenced\n- Function-level: {42, 123, 456, 789, 0}\n- Repo-level: {42, 123, 456}\n- TRAJ DeepSeek supplementary: {0, 789, 999}\n- NF4 seeds: 789, 0\n- bf16 seeds: 42, 123, 456\n\n### Checkpoints Referenced\n- ckpt-2200 (epoch 1, Qwen3-8B CLS s42): 85.34%\n- ckpt-3600 (val-selected, Qwen3-8B CLS s42): 84.48%\n- ckpt-6633 (final epoch, Qwen3-8B CLS s42): 85.29%\n- ckpt-800 (val-best, Qwen3-4B CLS s123): 75.33%\n- Training steps: ~12,627 vs ~13,266 (DeepSeek), ~6,633 (Qwen)\n\n### Experiment IDs / Run References\n- Total: 223 completed runs (135 successful, 88 failed/killed)\n- ~46 unique configurations\n- DeepSeek CWM: evaluated on ~75% of test instances (7210-7668 of 9784) — preliminary\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cf574b8-d4bb-4ce2-8d1e-e52c7592cfa7",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMHnPZuXxH1PrQ4QWef",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fed19ca-f191-48dc-b9d2-3b1607636b25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WvpitXXopwGQhEbrdEvpKi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4741,
      "cache_read_input_tokens": 44171,
      "output_tokens": 12754,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4741
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12754,
          "cache_read_input_tokens": 44171,
          "cache_creation_input_tokens": 4741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4741,
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

_source line 27 · 2026-05-21T07:55:52.517Z_

<details><summary>↩ Tool result · `toolu_01XDyB4dvucZyJfoR8MkFjAt`</summary>

```text
File created successfully at: /tmp/paper_referenced_data.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fed19ca-f191-48dc-b9d2-3b1607636b25",
  "isSidechain": true,
  "promptId": "f6b3cdb2-5a83-49f4-8d96-c2a7c5744d22",
  "agentId": "a6a7e9e0c43b6d074",
  "type": "user",
  "uuid": "713c4607-bbe7-43d9-992d-28ffd6871810",
  "sourceToolAssistantUUID": "1fed19ca-f191-48dc-b9d2-3b1607636b25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-21T07:56:03.961Z_

The comprehensive report has been written to `/tmp/paper_referenced_data.md`. Here is a summary of what was extracted:

**Files read:** All 9 `.tex` files in the paper directory (`main.tex`, `abstract.tex`, `introduction.tex`, `method.tex`, `experiments.tex`, `appendix.tex`, `conclusion.tex`, `related_work.tex`, `checklist.tex`).

**Key findings:**

- **12 tables** were fully reproduced: Table 1 (main_results), Table 2 (scaling), Table 3 (repo_level), Table 4 (taxonomy), plus appendix tables for oracle stratification, LoRA rank ablation, few-shot baselines, per-mutation breakdown, CWM parse rates, variant-level accuracy, mutation distribution, TOST sensitivity, variant-level effect sizes, and Holm-Bonferroni correction.

- **~150+ unique numeric values** were extracted, spanning function-level per-test accuracies, repo-level per-test and variant-level accuracies, per-seed breakdowns, per-mutation breakdowns, CWM parse rates and parseable-only accuracies, inference throughput metrics, all p-values and confidence intervals, ICC/DEFF values, and fail recall values.

- **Seeds referenced:** Function-level {42, 123, 456, 789, 0}; repo-level {42, 123, 456}; supplementary TRAJ DeepSeek {0, 789, 999}.

- **Checkpoints referenced:** ckpt-2200, ckpt-3600, ckpt-6633 (Qwen3-8B CLS s42), ckpt-800 (Qwen3-4B CLS s123).

- **Run metadata:** 223 completed runs total (135 successful, 88 failed/killed), ~46 unique configurations, ~370 GPU-hours on RTX 5090.

The report is organized section-by-section with complete table reproductions, followed by a master list of all unique accuracy/metric values grouped by category (function-level, repo-level per-test, repo-level variant, oracle, ablation, per-mutation, statistical tests, etc.).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "713c4607-bbe7-43d9-992d-28ffd6871810",
  "isSidechain": true,
  "agentId": "a6a7e9e0c43b6d074",
  "requestId": "req_011CbFMb5g7G5M2X8vvJ3VRs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89f284a1-c69a-4598-b370-a496c5f6b0d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "214e1416-6a36-4ad4-8f28-4356406d36e3",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QeL943r9WFnAkpBvjgqhyz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12781,
      "cache_read_input_tokens": 48912,
      "output_tokens": 521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12781
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 521,
          "cache_read_input_tokens": 48912,
          "cache_creation_input_tokens": 12781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12781,
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
