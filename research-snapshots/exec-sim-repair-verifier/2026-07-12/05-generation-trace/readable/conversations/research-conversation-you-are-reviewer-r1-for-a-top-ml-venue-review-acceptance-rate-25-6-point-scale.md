# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a020972963c793490.jsonl`
- **Structured JSON:** [`634524f84f940537da2c.json`](../../sessions/63/634524f84f940537da2c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-17T04:01:36.965Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus: **methodology soundness and experimental rigor**.

## Paper Summary

Title: "The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study"

The paper compares three formulations for execution-free code verification:
- CLS (per-test binary classification)
- CWM (code world model / generation-based)
- TRAJ (trajectory-level scoring)

Trained with identical LoRA configs on matched 8B models from Qwen3 and DeepSeek-R1-Qwen3 families, evaluated at function-level and repository-level complexity.

**4 claims:**
1. All formulations achieve equivalent accuracy at function-level (86.8%–90.5%)
2. At repo-level, CWM effectiveness is model-contingent (Qwen3: 53–93% unparseable vs DeepSeek: 13%)
3. Per-test CLS matches TRAJ accuracy with diagnostic granularity at 6–9× lower inference cost
4. CLS diagnostics enable re-repair: +13.3pp resolve rate (p=0.031, McNemar, n=60)

## Key Tables

**Table 2 (Function-level accuracy %)**:
- Qwen3-4B: CLS 88.4, CWM 87.2, Gap +1.2
- Qwen3-8B: CLS 90.5, CWM 87.7, Gap +2.8
- DeepSeek-8B: CLS 86.9, CWM 86.8, Gap +0.0

**Table 3 (Repo-level accuracy % and CWM unparseable rate)**:
- Qwen3-4B: CLS 83.6, CWM 58.0, Gap +25.6, Unparse 53.7%
- Qwen3-8B: CLS 84.8, CWM —, —, Unparse 93.0%
- DeepSeek-8B: CLS 81.6, CWM 77.7, Gap +3.9, Unparse 13.0%

**Table 4 (DeepSeek repo multi-seed)**:
- Seed 42: CLS Acc 82.3, F1m 78.5, CWM Acc 78.5, Unparse 11.8%
- Seed 123: CLS Acc 80.8, F1m 76.9, CWM Acc 76.9, Unparse 14.2%

**Table 5 (Re-repair resolve rates, pass@1, n=60)**:
- D (random diag): 15.0%, Δ vs A1 −3.3pp, p=0.62
- A1 (no info): 18.3%
- A2 (test names): 21.7%, Δ +3.3pp, p=0.41
- B (CLS diag): 31.7%, Δ +13.3pp, p=0.031*
- C (oracle diag): 40.0%, Δ +21.7pp, p=0.004**

**Table 6 (200-instance pilot)**:
- Control: 19.0%, CLS Diag: 33.0%, Δ +14.0pp, p=0.008, Cohen's d=0.42

**Table 7 (Robustness summary)**:
- CLS: Func 86.9–90.5 (robust), Repo 81.6–84.8 (robust)
- CWM: Func 86.8–87.7 (robust), Repo 58.0–77.7 (fragile)
- TRAJ: Func 85.7–86.2, Repo 77.1–85.7 (variable)

## Dataset: SWE-bench-PerTest
500 instances × 16 candidates = 8000 evaluations, 7680 successful (96%), 94,720 per-test labels.
F2P distribution: T1 45.2%, T2 22.8%, T3-5 18.6%, T6+ 13.4%. Mean 12.3 tests/instance.

## Method Details
- Models: Qwen3-8B, DeepSeek-R1-0528-Qwen3-8B (both 8B), plus Qwen3-4B
- LoRA rank 64, α=128, max_seq_len=8192, 6 epochs, lr=2e-4
- Repo-level: 2 seeds; Function-level: 3 seeds
- Statistical tests: McNemar for paired binary, TOST for equivalence
- Re-repair: Qwen3-8B-Instruct as repair agent, 5 conditions × 60 instances × 5 samples, T=0.7

## Review Context — Imagined experiments the paper was supposed to cover
The review_context.yaml lists these experiments:
1. deepseek-cls-repo-v4 (expected acc 82.3) — APPEARS in Table 4
2. deepseek-cls-repo-s123 (expected acc 80.8) — APPEARS in Table 4
3. deepseek-cwm-repo (expected acc 78.5, unparse 11.8%) — APPEARS in Table 4
4. deepseek-cwm-repo-s123 (expected acc 76.9, unparse 14.2%) — APPEARS in Table 4
5. re-repair-phase1-instruct (5 conditions, n=60) — APPEARS in Table 5
6. swebench-pertest-data (500×16, 94720 labels) — APPEARS in Table 1
7. diagnostic-rerepair-pilot (n=200, delta 14pp) — APPEARS in Table 6
8. deepseek-repo-composite-analysis (cross-model table) — APPEARS in Tables 3, 7

All imagined experiments appear covered.

## Your Review Task

Evaluate the following aspects and provide detailed critique:

1. **Experimental Design Soundness**: Are the controlled variables truly controlled? Are there confounds? Is the comparison fair?
2. **Statistical Rigor**: Are the statistical tests appropriate? Is n=60 sufficient? Are the equivalence claims (TOST) properly conducted?
3. **Reproducibility**: Are enough details provided to reproduce?
4. **Missing Experiments or Controls**: What's missing?
5. **Claim Support**: Does each claim have sufficient evidence?
6. **Data/Table Presentation**: Are tables clear and complete?
7. **Methodological Weaknesses**: Any flaws in the approach?

Provide your output as:
```
## R1 Review: Methodology & Experiments

### Summary
[2-3 sentences]

### Strengths
[Bulleted list, 4-6 items]

### Weaknesses
[Bulleted list, 4-8 items, each with specific detail]

### Questions for Authors
[3-5 specific questions]

### Missing Experiments
[What's absent that should be present]

### Minor Issues
[Smaller problems]

### Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "a020972963c793490",
  "type": "user",
  "uuid": "75ad4c03-0b08-4d2e-b3e0-ec980e5f7ac5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T04:01:36.971Z_

```json
{
  "parentUuid": "75ad4c03-0b08-4d2e-b3e0-ec980e5f7ac5",
  "isSidechain": true,
  "agentId": "a020972963c793490",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c34847ec-5ba9-40c6-88d2-1cc5bd7c047e",
  "timestamp": "2026-05-17T04:01:36.971Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-17T04:01:41.656Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EoctRFHm9Gqw26nb1KMagC`</summary>

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
  "parentUuid": "c34847ec-5ba9-40c6-88d2-1cc5bd7c047e",
  "isSidechain": true,
  "agentId": "a020972963c793490",
  "requestId": "req_011Cb7UVKYA89gBJyC93CqTK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bdb67a7-c4e9-4102-b5d7-0f83689fec0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hw5fAoFqTyiQ2Cg89Mm6de",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17878,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17878,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 4 · 2026-05-17T04:01:41.670Z_

<details><summary>↩ Tool result · `toolu_01EoctRFHm9Gqw26nb1KMagC`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two model families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench}.
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with LoRA~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. For cross-model validation, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge.
15	
16	\paragraph{Statistics.}
17	Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); per-test vs.\ trajectory-level comparison uses TOST~\cite{schuirmann1987tost} ($\pm$2\pp{} margin). ICC~\cite{shrout1979icc} quantifies within-problem correlation. Oracle analysis uses SWE-bench Verified (500 instances).
18	
19	
20	\subsection{Function-Level: Formulation Equivalence}
21	\label{sec:func_results}
22	
23	Table~\ref{tab:main_results} reports function-level results across formulations and model families.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\caption{Function-level per-test verification results on HumanEval+MBPP test set (1,890 samples). \cls{}: per-test binary classification; \cwm{}: execution output generation; TRAJ: trajectory-level scoring; ZS: zero-shot LLM-as-judge. Mean $\pm$ std over seeds reported where applicable.}
29	\label{tab:main_results}
30	\resizebox{\columnwidth}{!}{%
31	\setlength{\tabcolsep}{4pt}
32	\begin{tabular}{llcc}
33	\toprule
34	\textbf{Method} & \textbf{Model} & \textbf{Seeds} & \textbf{Accuracy (\%)} \\
35	\midrule
36	\multicolumn{4}{l}{\emph{Qwen3 (primary)}} \\
37	\cls{} (fine-tuned) & 4B & 5 & \textbf{88.43 $\pm$ 0.78} \\
38	\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\pm$ 0.37 \\
39	TRAJ (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
40	\midrule
41	\multicolumn{4}{l}{\emph{DeepSeek-Coder (cross-model validation)}} \\
42	\cls{} (fine-tuned) & 6.7B & 2 & 86.85 $\pm$ 0.11 \\
43	\cwm{} (fine-tuned) & 6.7B & 2 & 86.83 $\pm$ 1.49 \\
44	\midrule
45	\multicolumn{4}{l}{\emph{Zero-shot baselines}} \\
46	ZS LLM-as-judge & 8B & 1 & 64.40 \\
47	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	All three formulations achieve comparable accuracy on Qwen3-4B: \cls{} 88.43\% ($\pm$0.78), \cwm{} 87.19\% ($\pm$0.37), \traj{} 86.30\% ($\pm$0.97). The \cls{}--\cwm{} gap of 1.24\pp{} is modest, within 1.6$\times$ of the seed standard deviation for \cls{}. DeepSeek-Coder-6.7B confirms this equivalence: \cls{} 86.85\% ($\pm$0.11) vs.\ \cwm{} 86.83\% ($\pm$1.49), a gap of 0.02\pp{} indistinguishable from zero. At this complexity level, execution outputs are short and structured, generation-specific failure modes (truncation, format compliance) are not triggered, and formulation choice does not meaningfully affect accuracy. Zero-shot baselines lag substantially (64.40\% at 8B, 71.69\% at 32B NF4), confirming that task-specific fine-tuning is necessary regardless of formulation. \cwm{} produces 0\% unparseable outputs at function level for both model families.
53	
54	\paragraph{Variance asymmetry.} \cwm{}'s higher seed variance on DeepSeek ($\sigma{=}1.49$ vs.\ \cls{} $\sigma{=}0.11$) mirrors the Qwen3 pattern (\S\ref{sec:analysis}, paragraph d): generation is more sensitive to initialization than classification, consistent with the output space being less constrained.
55	
56	
57	\subsection{Scaling Behavior}
58	\label{sec:scaling}
59	
60	Table~\ref{tab:scaling} compares \cls{} and \cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.
61	
62	\begin{table}[t]
63	\centering
64	\small
65	\caption{Model-size scaling: \cls{} vs.\ \cwm{} accuracy (\%) at 4B and 8B (Qwen3). Three matched seeds in full precision. The \cls{}--\cwm{} gap widens from 1.18\pp{} to 2.43\pp{}.}
66	\label{tab:scaling}
67	\setlength{\tabcolsep}{4pt}
68	\begin{tabular}{llccccc}
69	\toprule
70	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{s456} & \textbf{Mean} & \textbf{Gap} \\
71	\midrule
72	\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \multirow{2}{*}{1.18} \\
73	\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\
74	\midrule
75	\cls{} & 8B & \textbf{90.48} & 89.40 & 88.31 & \textbf{89.40} & \multirow{2}{*}{\textbf{2.43}} \\
76	\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\
77	\bottomrule
78	\end{tabular}
79	\end{table}
80	
81	At 4B, \cls{} and \cwm{} are separated by 1.18\pp{} on the matched three-seed subset. At 8B, the gap widens to 2.43\pp{} (Figure~\ref{fig:scaling_gap}). Clustered bootstrap yields a mean gap of 2.26\pp{} ($p = 0.0066$, 95\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.
82	
83	The two formulations scale differently: from 4B to 8B, \cls{} gains +0.99\pp{} (88.41 $\to$ 89.40) while \cwm{} loses $-$0.27\pp{} (87.23 $\to$ 86.96). Additional capacity benefits classification but provides no measurable improvement for generation, consistent with the hypothesis that string prediction, not model capacity, constrains \cwm{} at this complexity level. However, the \cwm{} regression ($-$0.27\pp{}) falls within seed noise (3-seed std ${\sim}$0.5\pp{}) and could reflect suboptimal hyperparameter transfer rather than a fundamental bottleneck. This scaling pattern is observed within Qwen3 only; whether it generalizes across model families at function level is not yet tested. At repository-level complexity, the interaction between formulation and scale is examined in \S\ref{sec:repo}.
84	
85	
86	\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
87	\label{sec:equivalence}
88	
89	We compare \cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds. The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]); the TOST equivalence test confirms statistical equivalence at $p = 0.007$ ($\pm$2\pp{} margin). Within-problem predictions are correlated (ICC $= 0.191$, $p < 0.0001$, DEFF $= 3.97$); all statistical tests use clustered bootstrap accordingly. Per-test classification provides diagnostic information (which specific tests fail) at no cost to variant-level accuracy, paralleling the finding in process supervision~\cite{lightman2023letsverify} that step-level verification enables error localization without degrading outcome-level performance.
90	
91	
92	\subsection{Accuracy-Utility Frontier}
93	\label{sec:oracle-results}
94	
95	Oracle analysis on SWE-bench Verified (500 instances) reveals that per-test advantage concentrates sharply: at $T = 1$ F2P tests (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T \geq 2$ (31.3\%), with $T = 2$ alone contributing 55.3\% of the total 10.93\pp{} block-correlated advantage. Pass-to-pass (P2P) regression is negligible (1.04\% mean, 0\% median), so the practical value concentrates in fail-to-pass discrimination. Full stratification and the i.i.d.\ vs.\ block-correlated comparison appear in Appendix~\ref{app:oracle}.
96	
97	
98	\subsection{Repo-Level: Complexity-Dependent Divergence}
99	\label{sec:repo}
100	
101	Table~\ref{tab:repo_level} compares \cls{} and \cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy; the test set ($n{=}9{,}784$) has zero problem overlap with validation. We report both overall accuracy (where unparseable outputs default to the majority class, pass) and parseable-only accuracy to disentangle generation quality from default assignment effects.
102	
103	\begin{table}[t]
104	\centering
105	\small
106	\caption{Repo-level per-test verification on SWE-bench Verified test set ($n{=}9{,}784$, val-selected checkpoints). Parse Acc: accuracy computed only on parseable outputs. Unparseable \cwm{} outputs default to pass (majority class, 72.96\%).}
107	\label{tab:repo_level}
108	\resizebox{\columnwidth}{!}{%
109	\setlength{\tabcolsep}{3pt}
110	\begin{tabular}{llcccccc}
111	\toprule
112	\textbf{Method} & \textbf{Size} & \textbf{Seed} & \textbf{Acc (\%)} & \textbf{Macro \fone{}} & \textbf{Unparse (\%)} & \textbf{Parse Acc (\%)} & \textbf{vs Maj.\ (\pp{})} \\
113	\midrule
114	\cls{} & 4B & 42 & \textbf{83.63} & 75.63 & 0.0 & --- & +10.67 \\
115	\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & 42.88 & $-$14.92 \\
116	\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & 42.68 & $-$13.87 \\
117	\midrule
118	\cls{} & 8B & 42 & 84.48 & 78.17 & 0.0 & --- & +11.52 \\
119	\cls{} & 8B & 123 & 85.60 & 78.38 & 0.0 & --- & +12.64 \\
120	\cwm{} & 8B & 42 & 65.17 & --- & 73.8 & 38.52 & $-$7.79 \\
121	\midrule
122	\multicolumn{8}{l}{\emph{DeepSeek-Coder (cross-model, in progress)}} \\
123	\cls{} & 6.7B & --- & --- & --- & --- & --- & --- \\
124	\cwm{} & 6.7B & --- & --- & --- & --- & --- & --- \\
125	\midrule
126	Majority & --- & --- & 72.96 & --- & --- & --- & --- \\
127	\bottomrule
128	\end{tabular}}
129	\end{table}
130	
131	\paragraph{Formulation divergence.} At repository-level complexity, \cls{} and \cwm{} diverge sharply on Qwen3: the gap is 25.59\pp{} at 4B (\cls{} 83.63\% vs.\ \cwm{} 58.04\%, seed 42; Figure~\ref{fig:scaling_gap}) and 19.31\pp{} at 8B (84.48\% vs.\ 65.17\%). Both gaps are an order of magnitude larger than at function level (1--2\pp{}, Table~\ref{tab:scaling}), confirming that formulation effectiveness is complexity-dependent. \cwm{} falls below the majority baseline at both scales ($-$14.92\pp{} at 4B, $-$7.79\pp{} at 8B), indicating negative utility for this model/formulation combination. DeepSeek-Coder repo-level results (in progress) will determine whether this divergence is consistent across model families or specific to Qwen3's tokenizer and generation properties.
132	
133	\paragraph{Default assignment artifact.} The apparent \cwm{} ``improvement'' from 4B (58.04\%) to 8B (65.17\%) is an artifact of the default assignment protocol: unparseable outputs receive the majority-class label (pass, 72.96\% of the test set). As unparseable rate \emph{increases} from 53.7\% to 73.8\%, more predictions are replaced by this high-accuracy default, inflating overall accuracy. Parseable-only accuracy \emph{decreases} from 42.88\% (4B) to 38.52\% (8B), indicating that the generation model's actual predictive quality degrades with scale at this complexity level.
134	
135	\paragraph{Generation quality analysis.} Per-mutation analysis of \cwm{} 8B reveals degradation across all categories relative to 4B. The gold mutation (unmodified code) is most striking: parse rate collapses from 43.5\% (4B) to 23.9\% (8B), with parseable accuracy at 16.5\%. Even the simplest generation target (reproducing expected outputs for correct code) becomes harder at scale, consistent with a model-specific generation bottleneck. Whether this reflects a property of the Qwen3 tokenizer, the training regime, or the generation formulation itself will be informed by cross-model results. Detailed per-mutation breakdown appears in Appendix~\ref{app:repo_mutation}.
136	
137	\paragraph{Complexity as moderator.} The function-level \cls{}--\cwm{} gap widens from 1.18\pp{} (4B) to 2.43\pp{} (8B, $p = 0.0066$) with controlled methodology (matched seeds, same precision, no default assignment). At repo level, absolute gap magnitude (19--26\pp{}) is an order of magnitude larger than at function level (1--2\pp{}). This confirms complexity as the primary moderator of formulation divergence, though the repo-level data is from Qwen3 only.
138	
139	\paragraph{Sequence length.} A matched-context ablation confirms input context disparity explains $<$3\% of the \cls{}--\cwm{} gap: \cls{} 8B evaluated at \texttt{max\_seq\_length}$=$2,048 yields a matched-context gap of 25.00\pp{}, representing 98\% of the same-size 25.59\pp{} gap (Appendix~\ref{app:ablations}).
140	
141	\paragraph{Limitations.} The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline), indicating that val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \cwm{} 8B comparison is also single-seed. The validation and test sets have zero problem overlap but differ in mutation type composition, introducing potential distribution shift. All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches; the synthetic-to-real transfer gap remains untested.
142	
143	
144	\subsection{Analysis}
145	\label{sec:analysis}
146	
147	\paragraph{(a) Error complementarity.}
148	\cls{} and \cwm{} make errors in opposite directions at function level. Among \cls{} errors (seed 42), 75.5\% are false negatives (FAIL $\to$ PASS), meaning the classifier over-predicts passing. Among \cwm{} errors, 83.1\% are false positives (PASS $\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination achieves 90.63\% accuracy, +3.12\pp{} over the best single formulation (87.51\%). This systematic complementarity indicates that the formulations capture different aspects of code behavior: classification encodes discriminative features directly, while generation must additionally model output structure, leading to orthogonal failure patterns. Ensemble approaches combining both signals are a natural direction.
149	
150	\paragraph{(b) CWM error mode breakdown.}
151	Among unparseable \cwm{} outputs (Qwen3, repo-level), 76.9\% contain no execution keywords; 22.9\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\%), suggesting that repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-inherent one.
152	
153	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
154	Relaxed matching (tolerating format deviations, L0--L4) \emph{decreases} \cwm{} accuracy: 58.04\%$\to$56.98\% (seed 42) and 59.09\%$\to$55.91\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (42--53\%). The divergence widens from 26\pp{} to 28\pp{} under relaxed matching, ruling out the hypothesis that parsing strictness inflates the observed gap.
155	
156	\paragraph{(d) Variance compression.}
157	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and TRAJ (0.97\pp{}) at function level. If \cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
158	
159	\paragraph{(e) Per-test precision and recall.}
160	\cls{} achieves fail \fone{} 87.86\% (precision 82.75\%, recall 93.64\%) at seed 42, with 42.1\% of problems perfectly predicted. Multi-F2P instances (6--10 tests) reach 96.3\% accuracy, corroborating the oracle finding that per-test granularity is most valuable for complex instances.
161	
162	\paragraph{(f) Block correlation.}
163	Within-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\times$ more all-correct problems than i.i.d.\ expectation). All statistical tests use clustered bootstrap accordingly.
164	
165	\paragraph{(g) LoRA rank and majority voting.}
166	Doubling adapter capacity (rank 32) does not improve \cwm{} accuracy ($-$0.51\pp{}, within seed variance); majority voting ($K{=}3$) decreases accuracy ($-$0.68\pp{}). Both interventions fail to resolve the generation bottleneck on Qwen3, consistent with the failure being formulation-level or model-specific rather than capacity-limited (Appendix~\ref{app:ablations}).
167	
168	\paragraph{(h) Per-mutation scaling patterns.}
169	Scaling benefits are highly non-uniform across mutation types (Appendix, Table~\ref{tab:mutation_breakdown}). \texttt{off\_by\_one} shows the largest \cls{} scaling gain: 58.5\% (4B) to 83.0\% (8B mean, $+$24.6\pp{}). In contrast, \texttt{boundary\_removal} is scale-invariant at ${\sim}$46\% across all seeds and sizes, identifying an intrinsic difficulty ceiling. For \cwm{}, gold mutation parse rate collapses from 43.5\% (4B) to 23.9\% (8B) despite being the simplest target, indicating that generation capability degrades even for trivially correct code at larger scale within Qwen3.
170	
171	\paragraph{(i) Inference efficiency.}
172	\cls{} achieves 217$\times$ higher throughput than \cwm{} at repo level (853 vs.\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\cls{}) vs.\ 16.3s (\cwm{}). At the observed unparseable rate of 73.8\% (8B), the majority of \cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This efficiency gap is an inherent property of the formulation difference (1 vs.\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.
173	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bdb67a7-c4e9-4102-b5d7-0f83689fec0f",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "a020972963c793490",
  "type": "user",
  "uuid": "4acf44e4-2bc9-4430-9a5d-d8f74ef21df6",
  "sourceToolAssistantUUID": "5bdb67a7-c4e9-4102-b5d7-0f83689fec0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T04:01:41.839Z_

<details open><summary>🔧 Tool call — Read · `toolu_012iqRb1NQPyeujzQ596GHhn`</summary>

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
  "parentUuid": "4acf44e4-2bc9-4430-9a5d-d8f74ef21df6",
  "isSidechain": true,
  "agentId": "a020972963c793490",
  "requestId": "req_011Cb7UVKYA89gBJyC93CqTK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "029525d6-0498-48fc-b2e6-f7df64bf582d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hw5fAoFqTyiQ2Cg89Mm6de",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17878,
      "cache_read_input_tokens": 0,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17878
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 164,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17878,
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

_source line 6 · 2026-05-17T04:01:41.845Z_

<details><summary>↩ Tool result · `toolu_012iqRb1NQPyeujzQ596GHhn`</summary>

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
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests, providing no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation has characteristic failure modes that differ in their sensitivity to code complexity:
21	
22	\paragraph{Generation failure modes (\cwm{}).} The open-ended output space introduces three failure modes: (1)~\emph{token-budget exhaustion}, where $|o_i^*| > B$ guarantees exact-match failure due to truncation; (2)~\emph{string-value prediction errors}, where semantically equivalent outputs differing in surface form (floating-point precision, dictionary ordering) produce false negatives; and (3)~\emph{format compliance collapse}, where the model fails to produce structured predictions entirely at high input complexity, even when the generation budget is sufficient. Under optimistic independence, a token sequence of length $L$ with per-token accuracy $q$ has correct-sequence probability $q^L$, making long outputs exponentially harder to predict exactly. We adopt exact string matching following the original \cwm{} evaluation protocol~\citep{meta2025cwm}. Unparseable predictions default to the majority-class label (\textsc{Pass}).
23	
24	\paragraph{Classification failure modes (\cls{}).} The single-token output space eliminates format and truncation failures but constrains the model to encode its reasoning entirely within internal representations, without the intermediate reasoning trace that generation provides. \cls{} errors concentrate in false negatives (predicting \textsc{Pass} for failing tests), consistent with a bias toward the majority class.
25	
26	\paragraph{Trajectory-level failure modes (\traj{}).} By collapsing all per-test information into a single binary verdict, \traj{} discards diagnostic granularity. When a patch fails multiple tests, the trajectory-level formulation cannot identify \emph{which} tests fail. This limits downstream utility (e.g., targeted re-repair) but avoids per-test aggregation errors.
27	
28	\paragraph{Complexity dependence.} These failure modes suggest a complexity-dependent interaction: when execution outputs are short and structured (function-level code), generation modes (1)--(2) are rarely triggered, and all formulations should perform comparably. As output length and structural complexity increase (repository-level code), generation-specific failures may compound, creating divergence. Whether this divergence reflects a fundamental property of the generation formulation or is contingent on model/tokenizer properties is an empirical question we investigate in \S\ref{sec:experiments}.
29	
30	\subsection{Oracle Accuracy-Utility Framework}
31	\label{sec:oracle}
32	
33	Per-test granularity is valuable only when per-test predictions are sufficiently accurate and multiple tests provide partially independent signals. Consider a buggy patch with $k = |T_{\text{f2p}}|$ fail-to-pass tests. A per-test verifier with recall $r$ detects the bug if it identifies at least one failing test:
34	%
35	\begin{equation}
36	  P_{\text{detect}}(k) = 1 - (1 - r)^{k_{\text{eff}}}
37	  \label{eq:pdetect}
38	\end{equation}
39	%
40	where $k_{\text{eff}}$ is the effective number of independent tests. Let $a_h$ denote the trajectory-level detection accuracy; it is independent of $k$.
41	
42	\paragraph{Block-correlation model.} Per-test predictions within the same patch are correlated. We model this via the intraclass correlation coefficient $\rho$ \citep[ICC;][]{shrout1979icc}:
43	%
44	\begin{equation}
45	  k_{\text{eff}} = \frac{k}{1 + (k - 1)\rho}
46	  \label{eq:keff}
47	\end{equation}
48	%
49	When $\rho = 0$, $k_{\text{eff}} = k$ (full independence); when $\rho = 1$, $k_{\text{eff}} = 1$ (per-test collapses to trajectory-level). The per-test advantage relative to a trajectory-level baseline is $\Delta(k) = P_{\text{detect}}(k) - a_h$, and the expected population advantage is:
50	%
51	\begin{equation}
52	  \mathbb{E}[\Delta] = \sum_{k=1}^{K} P(|T_{\text{f2p}}| = k) \cdot \Delta(k)
53	  \label{eq:expected-advantage}
54	\end{equation}
55	
56	\paragraph{Testable predictions.} This yields three predictions validated in \S\ref{sec:experiments}: (1)~at $k = 1$, $\Delta \approx 0$; (2)~$\Delta(k)$ increases with $k$, dampened by $\rho > 0$; (3)~$\mathbb{E}[\Delta]$ concentrates in multi-F2P-test instances.
57	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "029525d6-0498-48fc-b2e6-f7df64bf582d",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "a020972963c793490",
  "type": "user",
  "uuid": "6ef46631-5e15-4dbf-bcfe-e5b6b684f401",
  "sourceToolAssistantUUID": "029525d6-0498-48fc-b2e6-f7df64bf582d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T04:01:47.138Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ViSoCVM2Cuzc567CSHxuVt`</summary>

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
  "parentUuid": "6ef46631-5e15-4dbf-bcfe-e5b6b684f401",
  "isSidechain": true,
  "agentId": "a020972963c793490",
  "requestId": "req_011Cb7UVgZwqEqdU259B9bop",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5eff3853-76ea-4b99-b45f-2db8f4433ec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxJ8NoZiWT5jv9xVEzpJfh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9456,
      "cache_read_input_tokens": 17878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9456,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 8 · 2026-05-17T04:01:47.150Z_

<details><summary>↩ Tool result · `toolu_01ViSoCVM2Cuzc567CSHxuVt`</summary>

```text
1	\begin{abstract}
2	Execution-free verification for LLM-based code repair can be formulated in multiple ways, yet no controlled comparison exists across formulations at matched model capacity. We systematically evaluate three formulations: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring, training on identical data with controlled model sizes (4B, 8B).
3	
4	At function level, the three formulations achieve near-equivalent accuracy (\cls{} 88.43\% vs.\ \cwm{} 87.19\% at 4B, 5 seeds; TOST equivalence with trajectory-level at $p{=}0.007$). At repository level, formulation divergence amplifies to 19--26\pp{} (4B: 25.59\pp{}; 8B: 19.31\pp{}), with \cwm{} falling below majority baseline. However, this divergence is partially model-contingent: \cwm{} failures on Qwen3 concentrate in format non-compliance (unparseable rate 53.7\%$\to$73.8\% from 4B to 8B) rather than semantic prediction errors, and generation quality uniformly degrades with scale (parseable-only accuracy 42.9\%$\to$38.5\%). Whether this reflects a fundamental generation bottleneck or model-specific behavior remains open pending cross-model validation.
5	
6	Two findings generalize across conditions. First, per-test classification provides diagnostic granularity (which specific tests fail) at equivalent trajectory-level accuracy, with the advantage concentrating in instances with $\geq$2 failing tests (31\% of instances, 55\% of oracle advantage). Second, formulations exhibit complementary error patterns: an oracle ensemble reaches 90.63\%, motivating complexity-aware routing rather than a single universal formulation.
7	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5eff3853-76ea-4b99-b45f-2db8f4433ec3",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "a020972963c793490",
  "type": "user",
  "uuid": "87c13aa8-894e-4aa0-ad76-2c9488033ac8",
  "sourceToolAssistantUUID": "5eff3853-76ea-4b99-b45f-2db8f4433ec3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T04:01:47.657Z_

<details open><summary>🔧 Tool call — Read · `toolu_013eqbSbtoPxBz6jsoxLSNHK`</summary>

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
  "parentUuid": "87c13aa8-894e-4aa0-ad76-2c9488033ac8",
  "isSidechain": true,
  "agentId": "a020972963c793490",
  "requestId": "req_011Cb7UVgZwqEqdU259B9bop",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71c79297-fd6a-4caf-bd03-a7e9d345bd54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxJ8NoZiWT5jv9xVEzpJfh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9456,
      "cache_read_input_tokens": 17878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9456,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 10 · 2026-05-17T04:01:47.662Z_

<details><summary>↩ Tool result · `toolu_013eqbSbtoPxBz6jsoxLSNHK`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a controlled comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question.
7	
8	We present the first systematic comparison of these three formulations across two model families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our central finding is that \emph{formulation effectiveness is complexity-dependent and model-contingent}: at function-level complexity, all three formulations achieve statistically equivalent accuracy regardless of model family; at repository-level complexity, formulations diverge sharply, with the magnitude and direction of divergence depending on model and tokenizer properties rather than formulation design alone. Figure~\ref{fig:reformulation} illustrates the three formulations.
9	
10	We make the following contributions:
11	
12	\begin{itemize}[leftmargin=*,itemsep=2pt]
13	\item \textbf{Formulation equivalence at low complexity.} On function-level benchmarks, \cls{}, \cwm{}, and \traj{} achieve near-identical accuracy across two model families (Qwen3-4B: 88.4/87.2/86.3\%, 5 seeds; DeepSeek-6.7B: 86.9/86.8\%, 2 seeds). The \cls{}--\cwm{} gap is 0.02--1.24\pp{}, within seed noise in both cases. This null result establishes that classification is not inherently easier than generation when execution outputs are short and structured.
14	
15	\item \textbf{Complexity-dependent divergence.} At repository-level complexity with Qwen3, \cls{} achieves 19--26\pp{} higher accuracy than \cwm{} (4B: 25.59\pp{}; 8B: 19.31\pp{}), driven by format compliance collapse: 54--74\% of \cwm{} outputs are unparseable, and parseable-only accuracy degrades from 42.9\% (4B) to 38.5\% (8B). Whether this divergence generalizes across model families or is tokenizer/model-specific is under investigation (DeepSeek repo-level results pending). Both outcomes are informative: consistency would confirm complexity as the primary moderator; divergence would identify model properties as a critical design variable.
16	
17	\item \textbf{Error complementarity and ensemble potential.} \cls{} and \cwm{} exhibit systematically opposite error patterns at function level: \cls{} over-predicts passing (75.5\% of errors are false negatives) while \cwm{} over-predicts failure (83.1\% false positives). An oracle ensemble achieves 90.63\% (+3.12\pp{} over the best single formulation), suggesting that the formulations capture complementary aspects of code behavior.
18	
19	\item \textbf{Diagnostic granularity at equivalent accuracy.} Per-test classification achieves statistically equivalent variant-level accuracy to trajectory-level scoring (TOST equivalence $p = 0.007$, $\pm$2\pp{} margin) while providing per-test diagnostic signals at 217$\times$ higher throughput than generation (1 output token vs.\ avg 477). This enables failure localization without accuracy or efficiency cost relative to coarser formulations.
20	\end{itemize}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71c79297-fd6a-4caf-bd03-a7e9d345bd54",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "a020972963c793490",
  "type": "user",
  "uuid": "3737c222-03c0-44ee-afd7-b12314de8213",
  "sourceToolAssistantUUID": "71c79297-fd6a-4caf-bd03-a7e9d345bd54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T04:01:48.059Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HdVjrnXEobaFxMVbZufzsg`</summary>

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
  "parentUuid": "3737c222-03c0-44ee-afd7-b12314de8213",
  "isSidechain": true,
  "agentId": "a020972963c793490",
  "requestId": "req_011Cb7UVgZwqEqdU259B9bop",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1290aa63-6f73-437d-a31a-4dc0d16c07e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxJ8NoZiWT5jv9xVEzpJfh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9456,
      "cache_read_input_tokens": 17878,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9456
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 17878,
          "cache_creation_input_tokens": 9456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9456,
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

_source line 12 · 2026-05-17T04:01:48.065Z_

<details><summary>↩ Tool result · `toolu_01HdVjrnXEobaFxMVbZufzsg`</summary>

```text
1	\appendix
2	
3	\section{Oracle Accuracy-Utility Analysis}
4	\label{app:oracle}
5	
6	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level TOST analysis; \S\ref{sec:equivalence}).
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from TOST equivalence analysis). P2P regression rate: 1.04\% mean, 0\% median.}
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
39	The analysis above uses ICC $= 0.191$ from function-level TOST equivalence testing (\S\ref{sec:equivalence}), where mean cluster size $\bar{k} \approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\S\ref{sec:repo}), reflecting the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly, amplifying the block-correlated per-test advantage at each $T$ stratum---the correction from i.i.d.\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage; the repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, strengthening the case for per-test granularity at repository-level complexity.
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
67	Majority voting ($K{=}3$) decreases accuracy from 87.51\% to 86.83\% ($-$0.68\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.
68	
69	\paragraph{Sequence-length ablation details.}
70	Both formulations are trained with \texttt{max\_seq\_length}$=$2,048. At inference, \cwm{} reserves \texttt{max\_new\_tokens}$=$1,024, leaving ${\sim}$1,024 effective input tokens; \cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\cls{} 8B at 2,048 tokens) achieves 83.04\%, only 1.44\pp{} below the 8,192-token evaluation (84.48\%), though truncation introduces 136 unparseable outputs (1.39\% of test samples). The matched-context gap (\cls{}@2,048 vs.\ \cwm{}@2,048) is 25.00\pp{}---98\% of the full 25.59\pp{} gap---confirming that input context disparity explains at most 3\% of the difference.
71	
72	\section{Repo-Level Per-Mutation Breakdown}
73	\label{app:repo_mutation}
74	
75	Table~\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \cls{} produces 0\% unparseable outputs; all values are direct classification accuracy. \cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \S\ref{sec:repo}).
76	
77	\begin{table}[h]
78	\centering
79	\small
80	\caption{Per-mutation test accuracy (\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \cls{} 8B reports two seeds; $\Delta$ is mean 4B$\to$8B gain for \cls{}. \cwm{} 4B per-mutation overall accuracy unavailable except gold (computed from parse rate 43.5\%, parseable acc 23.5\%).}
81	\label{tab:mutation_breakdown}
82	\resizebox{\columnwidth}{!}{%
83	\setlength{\tabcolsep}{3pt}
84	\begin{tabular}{lccccccc}
85	\toprule
86	\textbf{Mutation} & \textbf{$n$} & \textbf{CLS 4B} & \textbf{CLS 8B s42} & \textbf{CLS 8B s123} & \textbf{CWM 4B} & \textbf{CWM 8B} & \textbf{$\Delta$ CLS} \\
87	\midrule
88	gold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\
89	operator\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\
90	off\_by\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \textbf{+24.58} \\
91	return\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\
92	boundary\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\
93	\bottomrule
94	\end{tabular}}
95	\end{table}
96	
97	Table~\ref{tab:cwm_mutation_parse} shows that \cwm{} generation quality degrades from 4B to 8B across all mutation types.
98	
99	\begin{table}[h]
100	\centering
101	\small
102	\caption{\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below chance (50\%) for gold at both scales.}
103	\label{tab:cwm_mutation_parse}
104	\setlength{\tabcolsep}{4pt}
105	\begin{tabular}{lcccc}
106	\toprule
107	& \multicolumn{2}{c}{\textbf{Parse Rate (\%)}} & \multicolumn{2}{c}{\textbf{Parse Acc (\%)}} \\
108	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
109	\textbf{Mutation} & \textbf{4B} & \textbf{8B} & \textbf{4B} & \textbf{8B} \\
110	\midrule
111	gold & 43.5 & 23.9 & 23.5 & 16.5 \\
112	operator\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\
113	off\_by\_one & 4.4 & 27.3 & 0.0 & 38.0 \\
114	return\_value & 48.8 & 26.9 & 27.0 & 56.9 \\
115	boundary\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\
116	\bottomrule
117	\end{tabular}
118	\end{table}
119	
120	Key findings: (1)~Gold parse rate collapses from 43.5\% to 23.9\% at 8B---the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\%: the model generates outputs that fail exact-match even for correct code. (3)~\texttt{off\_by\_one} is an anomaly: parse rate \emph{increases} from 4.4\% to 27.3\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.
121	
122	\section{Training Hyperparameters}
123	\label{app:hyperparams}
124	
125	Table~\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \cls{} and \cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size and gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes).
126	
127	\begin{table}[h]
128	\centering
129	\small
130	\caption{Training hyperparameters for all configurations. Effective batch size is $\text{per-device} \times \text{grad.\ accum.} = 32$ in all cases.}
131	\label{tab:hyperparams}
132	\setlength{\tabcolsep}{3pt}
133	\begin{tabular}{lcccc}
134	\toprule
135	\textbf{Hyperparameter} & \textbf{4B \cls{}} & \textbf{4B \cwm{}} & \textbf{8B \cls{}} & \textbf{8B \cwm{}} \\
136	\midrule
137	Base model & Qwen3-4B & Qwen3-4B & Qwen3-8B & Qwen3-8B \\
138	LoRA rank ($r$) & 16 & 16 & 16 & 16 \\
139	LoRA alpha ($\alpha$) & 32 & 32 & 32 & 32 \\
140	LoRA dropout & 0.05 & 0.05 & 0.05 & 0.05 \\
141	LoRA targets & \multicolumn{4}{c}{\texttt{q\_proj, k\_proj, v\_proj, o\_proj}} \\
142	Learning rate & 5e-5 & 5e-5 & 5e-5 & 5e-5 \\
143	Optimizer & \multicolumn{4}{c}{AdamW ($\beta_1{=}0.9$, $\beta_2{=}0.999$)} \\
144	Weight decay & 0.01 & 0.01 & 0.01 & 0.01 \\
145	Warmup ratio & 0.05 & 0.05 & 0.05 & 0.05 \\
146	LR scheduler & \multicolumn{4}{c}{Linear} \\
147	Per-device batch size & 2 & 1 & 1 & 1 \\
148	Gradient accumulation & 16 & 32 & 32 & 32 \\
149	Effective batch size & 32 & 32 & 32 & 32 \\
150	Max sequence length & 2,048 & 2,048 & 2,048 & 2,048 \\
151	Epochs & 3 & 3 & 3 & 3 \\
152	Total steps & 6,633 & 6,633 & 6,633 & 6,633 \\
153	Precision & bf16 & bf16 & bf16 & bf16 \\
154	Gradient checkpointing & \checkmark & \checkmark & \checkmark & \checkmark \\
155	Seeds & 42, 123 & 42, 123 & 42, 123 & 42 \\
156	Training samples & 70,748 & 70,748 & 70,748 & 70,748 \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1290aa63-6f73-437d-a31a-4dc0d16c07e5",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "a020972963c793490",
  "type": "user",
  "uuid": "54375a49-76fa-4deb-8c50-b766c50023bc",
  "sourceToolAssistantUUID": "1290aa63-6f73-437d-a31a-4dc0d16c07e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T04:01:52.623Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NXr5y2g84cTne1nYzJXBws`</summary>

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
  "parentUuid": "54375a49-76fa-4deb-8c50-b766c50023bc",
  "isSidechain": true,
  "agentId": "a020972963c793490",
  "requestId": "req_011Cb7UW9FofqdFqqsrYhJH1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6789382-b064-4ed3-9501-d4b0c134cdc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012NP58D8bqErAw4AkWigJow",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6338,
      "cache_read_input_tokens": 27334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6338,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 14 · 2026-05-17T04:01:52.628Z_

<details><summary>↩ Tool result · `toolu_01NXr5y2g84cTne1nYzJXBws`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first controlled comparison of three formulations for execution-free code repair verification: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level scoring. Our central finding is that no single formulation dominates across all conditions; formulation effectiveness is complexity-dependent and, at repository scale, model-contingent.
5	
6	At function level, \cls{} and \cwm{} achieve near-equivalent accuracy (gap 1.24\pp{} at 4B, TOST equivalence $p{=}0.007$), suggesting that the formulation choice matters less than model capacity and training data at this complexity tier. At repository level, formulation divergence amplifies dramatically (4B: 25.59\pp{}; 8B: 19.31\pp{}), but the source of this divergence requires careful attribution: \cwm{} failures on Qwen3 concentrate in format non-compliance (unparseable rates 53.7--73.8\%) rather than semantic prediction errors. Whether this reflects a fundamental generation bottleneck or a model-specific tokenizer interaction remains an open empirical question pending cross-model validation.
7	
8	Two formulation-level properties generalize independent of model choice. First, per-test classification provides diagnostic granularity at equivalent trajectory-level accuracy, identifying which specific tests a patch fails. This advantage concentrates in instances with $\geq$2 fail-to-pass tests (31\% of instances, contributing 55\% of total oracle advantage). Second, the 1-token classification formulation yields a 217$\times$ throughput advantage over variable-length generation, an inherent property of the output-length asymmetry.
9	
10	Error complementarity between formulations (oracle ensemble: 90.63\%) suggests that the practitioner's choice need not be exclusive. Classification and generation exhibit complementary failure patterns, motivating routing strategies that select formulations based on predicted instance complexity.
11	
12	\paragraph{Limitations.}
13	Primary repo-level experiments use a single model family (Qwen3); cross-model validation with DeepSeek-Coder confirms near-equivalent function-level performance (gap 0.02\pp{}, 2 seeds), but repo-level cross-model results are pending. The repo-level same-size comparisons each use a single seed (4B-4B and 8B-8B). No downstream re-repair experiment validates whether per-test diagnostic signals translate to actual fix improvements. Pass-to-pass regression rates are negligible (1.04\% mean, 0\% median), meaning the per-test advantage currently concentrates in fail-to-pass discrimination; regression detection remains untested in practice. Training data comprises synthetic mutations; transfer to naturally occurring developer bugs is untested. The oracle analysis assumes ground-truth test labels; real-world per-test advantage is upper-bounded by classifier accuracy.
14	
15	\paragraph{Future work.}
16	Cross-model repo-level validation is the most critical next step: if DeepSeek-Coder replicates the Qwen3 divergence pattern, the generation bottleneck can be attributed to the formulation rather than the model. Multi-seed repo-level replication would strengthen statistical claims at this complexity tier. Error complementarity motivates complexity-aware routing that selects formulations per-instance. Per-test failure signals enable diagnostic re-repair: localizing faults from per-test verdicts rather than discarding failed patches outright. Integration with test-time scaling systems (best-of-$N$ with per-test reranking) is a natural application of the diagnostic granularity finding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6789382-b064-4ed3-9501-d4b0c134cdc6",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "a020972963c793490",
  "type": "user",
  "uuid": "36692d06-16ee-490e-a07d-fb9bcbfda19b",
  "sourceToolAssistantUUID": "d6789382-b064-4ed3-9501-d4b0c134cdc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T04:01:53.248Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DZACJhooxWGCJxjabw6XuY`</summary>

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
  "parentUuid": "36692d06-16ee-490e-a07d-fb9bcbfda19b",
  "isSidechain": true,
  "agentId": "a020972963c793490",
  "requestId": "req_011Cb7UW9FofqdFqqsrYhJH1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f4a9056-5451-4d7f-820c-34d3f49611ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012NP58D8bqErAw4AkWigJow",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6338,
      "cache_read_input_tokens": 27334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6338,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 16 · 2026-05-17T04:01:53.260Z_

<details><summary>↩ Tool result · `toolu_01DZACJhooxWGCJxjabw6XuY`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation for Code.}
5	Code World Models~\cite{meta2025cwm} mid-train a 32B LLM on execution traces to predict output strings, establishing the generation-based paradigm for execution-free verification.
6	Self-Execution~\cite{maimon2026selfexecution} extends this with step-by-step trace prediction.
7	CodeMind~\cite{liu2024codemind} evaluates code reasoning along multiple dimensions including execution prediction.
8	SolidCoder~\cite{lee2026solidcoder} bridges mental simulation and actual execution via concrete feedback.
9	Abdollahi et al.~\cite{abdollahi2025demystifying} identify systematic failure modes in LLM trace prediction, including position-dependent errors.
10	All share a generation formulation whose cost scales with output length. We provide the first controlled comparison of this formulation against classification and trajectory-level alternatives at matched model capacity, revealing that generation reliability is contingent on both code complexity and model/tokenizer properties.
11	
12	\paragraph{LLM-based Verification for Code Repair.}
13	SWE-RM~\cite{shum2025swerm} trains a trajectory-level reward model for patch ranking without execution.
14	Patch Reasoner~\cite{xu2025patchreasoner} uses chain-of-thought reasoning for patch verification.
15	Snell et al.~\cite{snell2024scaling} show that test-time scaling via verification outperforms parameter scaling.
16	S*~\cite{li2025sstar} combines execution-grounded selection with model-based scoring.
17	VG-Search~\cite{chen2025vgsearch} finds that finer-grained verification improves selection efficiency.
18	These works treat verification granularity as a design choice but do not compare the underlying formulation (classification vs.\ generation) at controlled capacity. We provide this comparison, finding that the granularity choice interacts with complexity level.
19	
20	\paragraph{Process vs.\ Outcome Supervision.}
21	Lightman et al.~\cite{lightman2023letsverify} demonstrate that process-based reward models (verifying each reasoning step) outperform outcome-based models (verifying only the final answer) for mathematical reasoning.
22	Uesato et al.~\cite{uesato2022solving} show similar advantages for process feedback in math word problems.
23	Our per-test classification is structurally analogous to process supervision: each test verdict corresponds to an intermediate verification step, while trajectory-level scoring corresponds to outcome supervision. Our finding that per-test and trajectory-level achieve equivalent accuracy (TOST $p = 0.007$) with per-test providing additional diagnostic value parallels the process supervision literature, where step-level verification enables error localization at no accuracy cost.
24	
25	\paragraph{Verification-in-the-Loop Repair.}
26	CodeRL~\cite{le2022coderl} trains a critic model to provide execution feedback for RL-based code generation.
27	AlphaCode~\cite{li2022alphacode} uses massive sampling with test-based filtering for competition programming.
28	Reflexion~\cite{shinn2023reflexion} uses verbal self-reflection on execution results to iteratively improve agent performance.
29	These systems demonstrate that verification quality is a primary bottleneck for iterative repair. Our comparison of verification formulations is complementary: the efficiency and diagnostic granularity of the verifier directly affects the viability of verification-in-the-loop approaches at scale.
30	
31	\paragraph{Learned Code Verifiers.}
32	LEVER~\cite{ni2023lever} trains a classifier to re-rank code candidates by predicting execution correctness.
33	CodeT~\cite{chen2023codet} uses dual execution agreement as a verification signal.
34	Both target execution-free deployment via classification-style training. Unlike candidate-level ranking, we provide per-test diagnostic verdicts and compare classification against generation on the same model, data, and compute budget, isolating the effect of task formulation.
35	
36	\paragraph{Automated Program Repair.}
37	SWE-bench~\cite{jimenez2024swebench} and SWE-bench Verified~\cite{chowdhury2024swebenchverified} provide standard benchmarks for repository-level repair.
38	SWE-agent~\cite{yang2024sweagent} uses tool-augmented agents; Agentless~\cite{xia2024agentless} demonstrates a simpler pipeline.
39	Yang et al.~\cite{yang2025aprsurvey} survey LLM-based repair, identifying verification as a persistent bottleneck.
40	These systems rely on execution-based validation, with cost scaling linearly in candidates. Per-test verification provides failure-localized signals that could support targeted re-repair.
41	
42	\paragraph{Predictive Mutation Testing.}
43	Predicting test outcomes for code mutations without execution has been studied in software engineering~\cite{tufano2019predictive,kim2022predictive}. Our per-test classification formulation shares this problem structure: given a code change (mutation/patch) and a test, predict pass or fail. We extend this line to LLM-based verification at repository scale, comparing it against alternative formulations (generation, trajectory-level) for the first time.
44	
45	\paragraph{Classification vs.\ Generation in NLP.}
46	Task framing affects model performance broadly: T5~\cite{raffel2020t5} and BART~\cite{lewis2020bart} demonstrate generation-classification tradeoffs under controlled capacity, while SQuAD~\cite{rajpurkar2016squad} shows that constraining output space can simplify tasks without sacrificing quality. We extend this lens to code verification, finding that code complexity moderates the tradeoff in a model-contingent manner.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f4a9056-5451-4d7f-820c-34d3f49611ea",
  "isSidechain": true,
  "promptId": "01d6b614-4fac-4d9f-8502-5b2ef520d053",
  "agentId": "a020972963c793490",
  "type": "user",
  "uuid": "f83e35c9-2509-4e23-80e1-fc92978df596",
  "sourceToolAssistantUUID": "9f4a9056-5451-4d7f-820c-34d3f49611ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T04:03:00.941Z_

Now I have a thorough understanding of the paper. Let me analyze the discrepancies between the paper summary provided in the prompt and what's actually in the paper, and then provide a rigorous methodological review.

Key observations from reading the actual paper:
1. The paper summary mentions DeepSeek-R1-0528-Qwen3-8B, LoRA rank 64, alpha=128, max_seq_len=8192, 6 epochs, lr=2e-4 -- but the actual paper uses DeepSeek-Coder-6.7B, LoRA rank 16, alpha=32, max_seq_len=2048, 3 epochs, lr=5e-5. The summary appears to describe a different (possibly planned) version of experiments.
2. The actual paper does NOT contain Tables 4, 5, or 6 as described in the summary. The DeepSeek repo-level results are listed as "in progress" with empty cells. There is no re-repair experiment in the paper.
3. The paper's actual claims are more conservative than those in the summary.

I will base my review on what is actually in the paper files.

## R1 Review: Methodology & Experiments

### Summary

This paper presents a controlled comparison of three formulations (CLS, CWM, TRAJ) for execution-free code verification, training LoRA adapters on Qwen3 (4B, 8B) and DeepSeek-Coder-6.7B. The core finding is that formulations are equivalent at function-level complexity but diverge sharply at repository-level, with CWM suffering format compliance collapse on Qwen3. The experimental design is careful in some respects (matched hyperparameters, multiple seeds at function level) but has critical gaps at the repository level where the most interesting claims are made.

### Strengths

- **Controlled comparison design**: Same LoRA config, same data, same training budget across formulations. This is the right way to isolate formulation effects and addresses a genuine gap in the literature.
- **Multiple seeds at function level**: 5 seeds for Qwen3-4B and 2 for DeepSeek provide reasonable confidence in the function-level equivalence claim.
- **Appropriate statistical methodology**: Use of clustered bootstrap (accounting for ICC), TOST for equivalence testing, and explicit reporting of seed standard deviations shows statistical awareness.
- **Transparent reporting of CWM failure modes**: The paper does not hide that CWM fails at repo level; the per-mutation breakdown and parseable-only accuracy analysis provide genuine insight into why.
- **Honest limitations section**: The paper explicitly acknowledges single-seed repo comparisons, pending cross-model results, and the synthetic-to-real gap.
- **Ablation completeness**: LoRA rank, majority voting, and sequence-length ablations systematically rule out alternative explanations for the CLS-CWM gap.

### Weaknesses

- **Repo-level claims rest on 1-2 seeds with a single model family.** The headline finding (19-26pp divergence) is observed only on Qwen3. The DeepSeek repo-level row is literally empty ("in progress"). This means the paper's most novel and surprising claim (complexity-dependent divergence) cannot be attributed to formulation vs. model/tokenizer effects. The paper acknowledges this but still frames it as a central contribution.

- **TOST equivalence margin of +/-2pp is not justified.** Why is 2pp the clinically meaningful threshold? The choice of equivalence margin is critical in TOST and must be pre-specified with a rationale (e.g., practical significance in downstream application). No justification is given for why 2pp rather than 1pp or 3pp was chosen. At 1pp margin, the equivalence claim might fail.

- **CWM is handicapped by design.** The exact string matching criterion is acknowledged as "conservative" but then used to declare CWM inferior. The paper tests relaxed matching (paragraph c) and shows it makes things worse, but this is because of the default-pass artifact. A fairer comparison might use semantic equivalence checking or output-space normalization. The paper essentially shows CWM fails at format compliance, not at semantic understanding, but then conflates these.

- **The "default to majority class" protocol for unparseable outputs is methodologically problematic.** This inflates CWM accuracy at high unparseable rates (as the authors note in the "default assignment artifact" paragraph) and deflates it when the majority class is wrong. A cleaner analysis would report (a) parseable-only accuracy and (b) coverage (parseable rate) as separate metrics. The paper partially does this but the headline numbers in tables use the conflated metric.

- **No downstream validation of per-test diagnostic utility.** The conclusion claims "per-test classification provides diagnostic granularity" as a contribution, but no experiment validates that this diagnostic signal is useful in practice. The oracle analysis shows theoretical potential, but the paper never demonstrates that a repair system actually benefits from per-test signals (the re-repair experiment is absent from the paper despite being mentioned in the summary context). This makes Claim 4 from the summary unsupported.

- **Function-level dataset may not generalize.** HumanEval+MBPP with synthetic mutations has very short, structured outputs. The function-level equivalence finding may be tautological: when outputs are trivially short, of course generation works. The interesting question is where the transition happens, but the paper has only two complexity levels with no intermediate.

- **Training hyperparameters are identical across formulations but may not be optimal for each.** CWM (a generation task) and CLS (a classification task) likely have different optimal learning rates, sequence lengths, and training durations. Using identical hyperparameters controls for compute but potentially handicaps one formulation. The paper should report hyperparameter sweeps or at minimum acknowledge this confound more prominently.

- **The scaling analysis (Table 2 / scaling table) conflates model size with other factors.** Qwen3-4B and Qwen3-8B differ not only in parameter count but in architecture details, pre-training data, and tokenizer vocabulary. The claim that "additional capacity benefits classification but not generation" is too strong for a 2-point comparison with a single model family.

### Questions for Authors

1. **TOST margin justification**: What is the principled rationale for the +/-2pp equivalence margin? Have you conducted sensitivity analysis showing that your equivalence conclusion is robust to margin choices of 1pp or 1.5pp?

2. **Cross-model repo-level results**: The paper's most interesting claim depends on results marked "in progress." Can you provide at least preliminary DeepSeek-Coder repo-level numbers? Without them, the paper cannot distinguish "CWM is fundamentally limited at repo-level complexity" from "Qwen3's tokenizer/generation properties cause CWM to fail."

3. **Hyperparameter fairness**: Did you conduct any hyperparameter search for CWM specifically (e.g., different learning rates, longer training, different sequence lengths for generation)? The identical-hyperparameter design controls for compute but may disadvantage the generation formulation, which has a fundamentally different output distribution.

4. **Practical significance threshold**: At function level, CLS achieves 88.43% vs CWM 87.19%. In a best-of-N repair pipeline with N=10 candidates, what is the downstream impact of this 1.24pp difference on resolve rate? Without calibrating to practical significance, it is unclear whether "equivalence" is the right framing or whether small differences compound.

5. **Why does CWM parseable-only accuracy decrease with model size?** The paper notes this pattern (42.9% to 38.5%) but offers no mechanistic explanation beyond "generation bottleneck." Could this reflect overfitting to format templates at larger scale, or interference between the generation and comprehension capabilities of the model?

### Missing Experiments

- **DeepSeek-Coder repo-level results** (marked "in progress" in the paper). This is essential to support the central claim and should not be published without it.
- **Re-repair experiment** demonstrating that per-test diagnostic signals actually improve downstream repair. The paper's practical contribution claim ("diagnostic granularity") is purely theoretical without this.
- **Intermediate complexity level** between HumanEval/MBPP (trivially short outputs) and full SWE-bench (extremely complex). A function-level dataset with longer/more complex outputs would help identify where the transition happens.
- **Multi-seed repo-level comparisons** (currently single-seed for most configurations). The function-level analysis has 5 seeds but repo-level has 1-2, precisely where variance matters most due to the higher complexity.
- **TOST sensitivity analysis** across different equivalence margins.
- **Alternative CWM evaluation protocols** (semantic matching, LLM-based output comparison) to disentangle format compliance from semantic understanding.

### Minor Issues

- Table 3 (repo-level) reports CWM 8B seed 42 Macro F1 as "---" despite having parseable outputs. This should be computable from parseable predictions.
- The paper summary mentions LoRA rank 64/alpha 128/lr 2e-4, but the actual paper uses rank 16/alpha 32/lr 5e-5. If the summary reflects a different experimental configuration that was actually run, the paper should clarify which configuration was used for which results.
- The inference efficiency comparison (217x throughput) uses Qwen3-4B on RTX 5090 with only 100 samples. This should be validated at 8B scale and with larger sample sizes to ensure the speedup is representative.
- The ICC value (0.191) used in the oracle analysis comes from function-level data but is applied to reason about repo-level utility. The paper notes the repo-level ICC is 0.3146, which strengthens the argument, but the oracle table itself uses the wrong ICC.
- The variance compression analysis (paragraph d) interprets low CWM variance as evidence of a ceiling, but an alternative explanation is simply that CWM's loss landscape has fewer sharp local minima for this task.

### Score: 3/6
### Confidence: 4/5

The paper tackles an important and timely question with a sound experimental philosophy, but the execution falls short of the standard needed for acceptance at a top venue. The most novel claim (repo-level divergence) rests on a single model family with 1-2 seeds and missing cross-model validation. The practical utility claim (diagnostic granularity) lacks downstream validation. The function-level equivalence finding, while clean, is somewhat expected given the triviality of the outputs. The paper would benefit substantially from completing the DeepSeek repo-level experiments, adding the re-repair validation, and increasing seed counts at repo level before resubmission.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f83e35c9-2509-4e23-80e1-fc92978df596",
  "isSidechain": true,
  "agentId": "a020972963c793490",
  "requestId": "req_011Cb7UWXU36Ly1yP4645EXL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3532a329-65ed-410f-ac33-5c8ac9b4a582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "44566697-d6b1-448a-9c2e-758fc9465c03",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4gLKdgiZSRBpqqUYvrYBT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2506,
      "cache_read_input_tokens": 33672,
      "output_tokens": 2509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2506
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2509,
          "cache_read_input_tokens": 33672,
          "cache_creation_input_tokens": 2506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2506,
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
