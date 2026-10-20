# Research conversation: You are Reviewer 1 (R1) for a top ML venue peer review. Your focus is **methods and experiments**. Review the paper belo

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-abe263163347f9054.jsonl`
- **Structured JSON:** [`34d90f3acfad066ba805.json`](../../sessions/34/34d90f3acfad066ba805.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-16T08:18:28.571Z_

You are Reviewer 1 (R1) for a top ML venue peer review. Your focus is **methods and experiments**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary
Title: "Classification Beats Generation: Complexity-Dependent Reformulation Advantage for Per-Test Code Repair Verification"

The paper reformulates execution simulation for code repair verification from open-ended generation (Code World Models / CWM) to binary classification (pass/fail per test). Key claims:
1. Function-level equivalence: CLS ≈ CWM on simple code (Qwen3-4B gap: 1.0pp, DeepSeek-6.7B: 0.6pp, both non-significant)
2. Repo-level divergence: CLS achieves 85.5% accuracy (3-seed, σ=0.61) while CWM collapses to 52% due to ≥85% unparseable predictions
3. Cross-architecture validation with DeepSeek-Coder-6.7B confirms formulation-driven pattern
4. Error complementarity: oracle ensemble 91.2% on parseable subset
5. Downstream re-repair: +6.0pp resolve rate (McNemar p=0.022), concentrated in multi-failure instances (+11.5pp)

## Key Tables/Results from the paper:

**Table 1: Function-level CLS vs CWM**
| Architecture | Size | CLS Acc | CWM Acc | Gap |
|---|---|---|---|---|
| Qwen3 | 4B | 88.41% | 87.4% | +1.0 |
| Qwen3 | 8B | 89.75% | 87.3% | +2.43 |
| DeepSeek-Coder | 6.7B | 86.3% | 85.7% | +0.6 |

**Table 2: DeepSeek multi-seed CWM** — Seed 42: 85.7%, Seed 123: 86.1%, Mean gap 0.4pp, 95% CI [-0.9, 1.7], p=0.68

**Table 3: Repo-level CLS 8B multi-seed**
| Seed | Ckpt | Accuracy | Fail F1 | Pass F1 |
|---|---|---|---|---|
| 42 | ckpt-400 | 84.79% | 72.93% | 89.43% |
| 123 | ckpt-500 | 85.8% | 76.2% | 90.1% |
| 456 | ckpt-450 | 85.9% | 76.8% | 90.5% |
| Mean±Std | — | 85.5±0.61 | 75.3±2.1 | 90.0±0.5 |

**Table 4: Function→Repo drop across architectures** — Consistent ~4-5pp drop for CLS

**Table 5: Repo-level CWM failure modes** — 85% unparseable total (38% token exhaustion, 28% format failure, 19% string mismatch), 10% parseable correct, 5% parseable wrong. Overall CWM accuracy 52% (below majority baseline 72.96%).

**Table 6: Complexity-dependent advantage summary** — Func(4B): +1.0pp, Func(8B): +2.43pp, Repo(8B): >30pp

**Table 7: Error complementarity (parseable subset, n=1468)** — Both correct 48.8%, CLS only 34.5%, CWM only 8.2%, Both wrong 8.5%, Oracle 91.2%

**Table 8: Oracle across levels** — Func(4B): 90.63%, Repo(8B parseable): 91.2%

**Table 9: Re-repair results (n=200)** — Baseline 27%, Without diag 29.5% (+2.5pp), With diag 33% (+6.0pp), Diagnostic-specific lift +3.5pp (p=0.022)

**Table 10: Stratified by F2P** — T=1: Diag +2.0pp, T≥2: Diag +11.5pp

**Table 11: SWE-bench-PerTest stats** — 489 instances, 16 candidates/instance, 9784 test samples, 72.96% pass class balance

**Dataset**: SWE-bench-PerTest built from SWE-bench Verified, 489/500 instances, Docker re-execution.

**Training**: LoRA rank 64, alpha 128, matched hyperparameters across CLS and CWM. Qwen3-8B/4B primary, DeepSeek-Coder-6.7B cross-validation.

**Method**: CLS outputs single binary token (pass/fail). CWM generates execution output, then parses to extract pass/fail.

**Limitations stated**: (1) Re-repair n=200 small, (2) same LoRA config for CLS and CWM, (3) only 4-8B models tested.

## Review Context (experiment design plan)
The experiment plan includes these imagined experiments:
1. SWE-bench-PerTest Dataset Construction — covered in paper
2. Repo-Level CLS Multi-Seed Validation (8B) — covered (Table 3)
3. Repo-Level CWM Unparseable Rate Confirmation — covered (Table 5), but paper doesn't show the CWM version evolution table (v10-v12 iterations)
4. DeepSeek Function-Level Classification — covered (Table 1)
5. DeepSeek Function-Level CWM + Multi-Seed — partially covered (Table 2 shows multi-seed, but only 2 seeds for DeepSeek CWM)
6. DeepSeek Repo-Level Classification — covered (Table 4, 81.5%)
7. Repo-Level Error Complementarity & Oracle Ensemble — covered (Tables 7-8)
8. Diagnostic Re-repair Experiment — covered (Tables 9-10)

## Your Review Task (R1: Methods + Experiments)

Evaluate:
1. **Experimental methodology**: Are experiments well-designed? Controls adequate? Confounds addressed?
2. **Statistical rigor**: Are significance tests appropriate? Sample sizes sufficient? Multi-seed validation adequate?
3. **Reproducibility**: Are details sufficient to reproduce? Missing details?
4. **Result interpretation**: Are claims supported by evidence? Over-claimed or under-claimed?
5. **Fairness of comparison**: Is the CLS vs CWM comparison fair? Same compute, same data, same hyperparameters?
6. **Missing experiments**: What important ablations or baselines are missing?

Produce a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted)
- Questions for authors
- Minor issues
- Overall score (1-6) with confidence (1-5)
- Recommendation: Accept / Weak Accept / Weak Reject / Reject

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d5e605e9-006a-4a90-83e2-16d1eb41e85d",
  "agentId": "abe263163347f9054",
  "type": "user",
  "uuid": "ed12c209-d38a-42c7-b08d-cdcda6efd593",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T08:18:28.577Z_

```json
{
  "parentUuid": "ed12c209-d38a-42c7-b08d-cdcda6efd593",
  "isSidechain": true,
  "agentId": "abe263163347f9054",
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
  "uuid": "45222435-ab0e-47d4-9b6f-dee8431baac5",
  "timestamp": "2026-05-16T08:18:28.577Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-16T08:18:32.794Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HKTNP33A9AZgPtJyuVLuCS`</summary>

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
  "parentUuid": "45222435-ab0e-47d4-9b6f-dee8431baac5",
  "isSidechain": true,
  "agentId": "abe263163347f9054",
  "requestId": "req_011Cb5vGTdEawRiuA1soN9mZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed98abd7-cd4e-4aa4-a97b-d1a44c029037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kc2KnSvLLfo4KiCzHtKbT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16556,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16556,
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

_source line 4 · 2026-05-16T08:18:32.807Z_

<details><summary>↩ Tool result · `toolu_01HKTNP33A9AZgPtJyuVLuCS`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate \cls{}, \cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench}.
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with LoRA~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. Our \cwm{} baseline is a LoRA fine-tuned variant for controlled comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge.
15	
16	\paragraph{Statistics.}
17	Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); per-test vs.\ trajectory-level comparison uses TOST~\cite{schuirmann1987tost} ($\pm$2\pp{} margin). ICC~\cite{shrout1979icc} quantifies within-problem correlation. Oracle analysis uses SWE-bench Verified (500 instances).
18	
19	
20	\subsection{Function-Level Results}
21	\label{sec:func_results}
22	
23	Table~\ref{tab:main_results} reports function-level results across formulations.
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
36	\cls{} (fine-tuned) & 4B & 5 & \textbf{88.43 $\pm$ 0.78} \\
37	\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\pm$ 0.37 \\
38	TRAJ (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
39	\midrule
40	ZS LLM-as-judge & 8B & 1 & 64.40 \\
41	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
42	\bottomrule
43	\end{tabular}}
44	\end{table}
45	
46	Fine-tuned \cls{} achieves 88.43\% ($\pm$0.78), compared to 87.19\% ($\pm$0.37) for \cwm{} and 86.30\% ($\pm$0.97) for TRAJ. The \cls{}--\cwm{} gap is 1.24\pp{}, modest at this complexity level where generation is not yet bottlenecked by token budget or string complexity. Zero-shot baselines lag substantially (64.40\% at 8B, 71.69\% at 32B NF4), confirming that task-specific fine-tuning is necessary for reliable verification.
47	
48	
49	\subsection{Scaling Behavior}
50	\label{sec:scaling}
51	
52	Table~\ref{tab:scaling} compares \cls{} and \cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.
53	
54	\begin{table}[t]
55	\centering
56	\small
57	\caption{Model-size scaling: \cls{} vs.\ \cwm{} accuracy (\%) at 4B and 8B. Three matched seeds in full precision. The \cls{}--\cwm{} gap widens from 1.18\pp{} to 2.43\pp{}.}
58	\label{tab:scaling}
59	\setlength{\tabcolsep}{4pt}
60	\begin{tabular}{llccccc}
61	\toprule
62	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{s456} & \textbf{Mean} & \textbf{Gap} \\
63	\midrule
64	\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \multirow{2}{*}{1.18} \\
65	\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\
66	\midrule
67	\cls{} & 8B & \textbf{90.48} & 89.40 & 88.31 & \textbf{89.40} & \multirow{2}{*}{\textbf{2.43}} \\
68	\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\
69	\bottomrule
70	\end{tabular}
71	\end{table}
72	
73	At 4B, \cls{} and \cwm{} are separated by 1.18\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\pp{} (Figure~\ref{fig:scaling_gap}). Clustered bootstrap analysis yields a mean gap of 2.26\pp{} ($p = 0.0066$, 95\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.
74	
75	The asymmetry in scaling efficiency is striking: from 4B to 8B, \cls{} gains +0.99\pp{} (88.41 $\to$ 89.40) while \cwm{} loses $-$0.27\pp{} (87.23 $\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \cwm{} accuracy. However, the \cwm{} regression ($-$0.27\pp{}) falls within seed noise (3-seed std ${\sim}$0.5\pp{}) and could reflect suboptimal hyperparameter transfer rather than a fundamental bottleneck. Whether this divergence amplifies at repository-level complexity is examined in \S\ref{sec:repo}.
76	
77	
78	\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
79	\label{sec:equivalence}
80	
81	We compare \cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds. The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]); the TOST equivalence test confirms statistical equivalence at $p = 0.007$ ($\pm$2\pp{} margin). Within-problem predictions are correlated (ICC $= 0.191$, $p < 0.0001$, DEFF $= 3.97$); all statistical tests use clustered bootstrap accordingly. Per-test classification thus provides diagnostic information---which specific tests fail---at no cost to variant-level accuracy.
82	
83	
84	\subsection{Accuracy-Utility Frontier}
85	\label{sec:oracle-results}
86	
87	Oracle analysis on SWE-bench Verified (500 instances) reveals that per-test advantage concentrates sharply: at $T = 1$ F2P tests (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T \geq 2$ (31.3\%), with $T = 2$ alone contributing 55.3\% of the total 10.93\pp{} block-correlated advantage. Pass-to-pass (P2P) regression is negligible (1.04\% mean, 0\% median), so the practical value concentrates in fail-to-pass discrimination. Full stratification and the i.i.d.\ vs.\ block-correlated comparison appear in Appendix~\ref{app:oracle}.
88	
89	
90	\subsection{Repo-Level Results}
91	\label{sec:repo}
92	
93	Table~\ref{tab:repo_level} compares \cls{} and \cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy; the test set ($n{=}9{,}784$) has zero problem overlap with validation. We report both overall accuracy (where unparseable outputs default to the majority class, pass) and parseable-only accuracy to disentangle generation quality from default assignment effects.
94	
95	\begin{table}[t]
96	\centering
97	\small
98	\caption{Repo-level per-test verification on SWE-bench Verified test set ($n{=}9{,}784$, val-selected checkpoints). Parse Acc: accuracy computed only on parseable outputs. Unparseable \cwm{} outputs default to pass (majority class, 72.96\%).}
99	\label{tab:repo_level}
100	\resizebox{\columnwidth}{!}{%
101	\setlength{\tabcolsep}{3pt}
102	\begin{tabular}{llcccccc}
103	\toprule
104	\textbf{Method} & \textbf{Size} & \textbf{Seed} & \textbf{Acc (\%)} & \textbf{Macro \fone{}} & \textbf{Unparse (\%)} & \textbf{Parse Acc (\%)} & \textbf{vs Maj.\ (\pp{})} \\
105	\midrule
106	\cls{} & 4B & 42 & \textbf{83.63} & 75.63 & 0.0 & --- & +10.67 \\
107	\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & 42.88 & $-$14.92 \\
108	\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & 42.68 & $-$13.87 \\
109	\midrule
110	\cls{} & 8B & 42 & 84.48 & 78.17 & 0.0 & --- & +11.52 \\
111	\cls{} & 8B & 123 & 85.60 & 78.38 & 0.0 & --- & +12.64 \\
112	\cwm{} & 8B & 42 & 65.17 & --- & 73.8 & 38.52 & $-$7.79 \\
113	\midrule
114	Majority & --- & --- & 72.96 & --- & --- & --- & --- \\
115	\bottomrule
116	\end{tabular}}
117	\end{table}
118	
119	\paragraph{Same-size gap magnitude.} The \cls{}--\cwm{} gap at 4B is 25.59\pp{} (\cls{} 83.63\% vs.\ \cwm{} 58.04\%, seed 42; Figure~\ref{fig:scaling_gap}); at 8B it is 19.31\pp{} (84.48\% vs.\ 65.17\%). Both gaps far exceed the function-level gap (1--2\pp{}, Table~\ref{tab:scaling}), confirming that the classification advantage is complexity-dependent. \cwm{} falls below the majority baseline at both scales ($-$14.92\pp{} at 4B, $-$7.79\pp{} at 8B), indicating negative utility.
120	
121	\paragraph{Overall accuracy is misleading.} The apparent \cwm{} ``improvement'' from 4B (58.04\%) to 8B (65.17\%) is an artifact of the default assignment protocol: unparseable outputs receive the majority-class label (pass, 72.96\% of the test set). As unparseable rate \emph{increases} from 53.7\% to 73.8\%, more predictions are replaced by this high-accuracy default, inflating overall accuracy. The parseable-only accuracy---which isolates actual generation quality---\emph{decreases} from 42.88\% (4B) to 38.52\% (8B), confirming that CWM generation degrades with scale at repository-level complexity.
122	
123	\paragraph{Generation quality degrades uniformly.} Per-mutation analysis of \cwm{} 8B reveals degradation across all categories relative to 4B. The gold mutation (unmodified code) is most striking: parse rate collapses from 43.5\% (4B) to 23.9\% (8B), with parseable accuracy at 16.5\%---far below the trivially-correct ``pass'' prediction. This indicates that even the simplest generation target (reproducing expected outputs for correct code) becomes harder at scale, consistent with a fundamental generation bottleneck rather than insufficient capacity. Detailed per-mutation breakdown appears in Appendix~\ref{app:repo_mutation}.
124	
125	\paragraph{Scaling evidence.} The correct scaling signal comes from function-level results (\S\ref{sec:scaling}), where the \cls{}--\cwm{} gap widens from 1.18\pp{} (4B) to 2.43\pp{} (8B, $p = 0.0066$) with controlled methodology (matched seeds, same precision, no default assignment). At repo-level, the primary claim is that absolute gap magnitude (19--26\pp{}) is an order of magnitude larger than at function level (1--2\pp{}), demonstrating complexity-dependent advantage.
126	
127	\paragraph{Sequence length.} A matched-context ablation confirms input context disparity explains $<$3\% of the \cls{}--\cwm{} gap: \cls{} 8B evaluated at \texttt{max\_seq\_length}$=$2,048 yields a matched-context gap of 25.00\pp{}, representing 98\% of the same-size 25.59\pp{} gap (Appendix~\ref{app:ablations}).
128	
129	\paragraph{Limitations.} The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline), indicating that val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \cwm{} 8B comparison is also single-seed. The validation and test sets have zero problem overlap but differ in mutation type composition, introducing potential distribution shift. All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches; the synthetic-to-real transfer gap remains untested.
130	
131	
132	\subsection{Analysis}
133	\label{sec:analysis}
134	
135	\paragraph{(a) Error complementarity.}
136	\cls{} and \cwm{} make errors in opposite directions at function level. Among \cls{} errors (seed 42), 75.5\% are false negatives (FAIL $\to$ PASS), meaning the classifier tends to over-predict passing. Among \cwm{} errors, 83.1\% are false positives (PASS $\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\% accuracy, a 3.12\pp{} improvement over \cls{} alone (87.51\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains.
137	
138	\paragraph{(b) CWM error mode breakdown.}
139	Among unparseable \cwm{} outputs, 76.9\% contain no execution keywords; 22.9\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\%), suggesting domain-specific code contexts prevent structured generation.
140	
141	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
142	Relaxed matching (tolerating format deviations, L0--L4) \emph{decreases} \cwm{} accuracy: 58.04\%$\to$56.98\% (seed 42) and 59.09\%$\to$55.91\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (42--53\%). The \cls{}--\cwm{} gap widens from 26\pp{} to 28\pp{}, ruling out the hypothesis that parsing strictness inflates the observed gap.
143	
144	\paragraph{(d) Variance compression.}
145	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and TRAJ (0.97\pp{}) at function level. This is consistent with the bottleneck hypothesis: if \cwm{} performance is capped by output-format constraints, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
146	
147	\paragraph{(e) Per-test precision and recall.}
148	\cls{} achieves fail \fone{} 87.86\% (precision 82.75\%, recall 93.64\%) at seed 42, with 42.1\% of problems perfectly predicted. Multi-F2P instances (6--10 tests) reach 96.3\% accuracy, corroborating the oracle finding.
149	
150	\paragraph{(f) Block correlation.}
151	Within-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\times$ more all-correct problems than i.i.d.\ expectation). All tests use clustered bootstrap accordingly.
152	
153	\paragraph{(g) LoRA rank and majority voting.}
154	Doubling adapter capacity (rank 32) does not improve \cwm{} accuracy ($-$0.51\pp{}, within seed variance); majority voting ($K{=}3$) decreases accuracy ($-$0.68\pp{}). Both confirm the bottleneck is formulation-level, not capacity-level (Appendix~\ref{app:ablations}).
155	
156	\paragraph{(h) Per-mutation scaling patterns.}
157	Scaling benefits are highly non-uniform across mutation types (Appendix, Table~\ref{tab:mutation_breakdown}). \texttt{off\_by\_one} is the largest \cls{} scaling beneficiary: accuracy jumps from 58.5\% (4B) to 83.0\% (8B mean, $+$24.6\pp{}). In contrast, \texttt{boundary\_removal} is scale-invariant at ${\sim}$46\% across all seeds and sizes, identifying a difficulty ceiling independent of capacity. For \cwm{}, gold mutation parse rate collapses from 43.5\% (4B) to 23.9\% (8B) despite being the simplest target---all tests pass by construction---indicating that generation capability degrades even for trivially correct code at larger scale.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed98abd7-cd4e-4aa4-a97b-d1a44c029037",
  "isSidechain": true,
  "promptId": "d5e605e9-006a-4a90-83e2-16d1eb41e85d",
  "agentId": "abe263163347f9054",
  "type": "user",
  "uuid": "ed32dc90-336d-4b2a-b106-08600c136dd5",
  "sourceToolAssistantUUID": "ed98abd7-cd4e-4aa4-a97b-d1a44c029037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T08:18:32.977Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ER8y33pAzSz6MzHic73tAh`</summary>

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
  "parentUuid": "ed32dc90-336d-4b2a-b106-08600c136dd5",
  "isSidechain": true,
  "agentId": "abe263163347f9054",
  "requestId": "req_011Cb5vGTdEawRiuA1soN9mZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "953dece5-45ce-4ba7-8e73-583d6a174edc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kc2KnSvLLfo4KiCzHtKbT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16556,
      "cache_read_input_tokens": 0,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16556
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16556,
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

_source line 6 · 2026-05-16T08:18:32.982Z_

<details><summary>↩ Tool result · `toolu_01ER8y33pAzSz6MzHic73tAh`</summary>

```text
1	% Method section — EMNLP 2026 ARR submission
2	% Classification Succeeds Where Generation Stalls:
3	% Reformulating Execution Simulation for Code Repair Verification
4	
5	\section{Method}
6	\label{sec:method}
7	
8	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
9	
10	\subsection{Verification Formulations}
11	\label{sec:formulations}
12	
13	Let $c_p$ denote the code context (unified diff) of patch $p$.
14	
15	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Cost: one token per test.
16	
17	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Cost: $\sum_i |\hat{o}_i|$ tokens.
18	
19	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests, providing no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences reflect per-test decomposition value.
20	
21	\subsection{\cwm{} Failure Modes}
22	\label{sec:failure-modes}
23	
24	The generation formulation introduces three systematic failure modes absent in classification: (1)~\emph{token-budget exhaustion}---when $|o_i^*| > B$, truncation guarantees exact-match failure; (2)~\emph{string-value prediction errors}---semantically equivalent outputs differing in surface form (floating-point precision, dictionary ordering) produce false negatives; even under optimistic independence assumptions, a sequence of $L$ tokens each with accuracy $q$ yields correct-sequence probability $q^L$, making long outputs exponentially harder; (3)~\emph{format compliance collapse}---at repository-level complexity, the model fails to produce structured predictions entirely, even when the generation budget is sufficient. We hypothesize that the increased input complexity and multi-file context at repository level overwhelm the model's ability to maintain format adherence across the generation; per-repository unparseable rates support this (\S\ref{sec:analysis}). We adopt exact string matching following the original \cwm{} evaluation protocol \citep{meta2025cwm}. This is conservative but does not disadvantage \cwm{}: the dominant failure at repository scale is format non-compliance, where outputs are structurally unparseable regardless of matching strategy. Unparseable \cwm{} predictions---those that cannot be parsed into a structured verdict---default to the majority-class label (\textsc{Pass}), equivalent to the majority baseline prediction. This favors \cwm{} by assigning the statistically most likely label rather than penalizing format failures.
25	
26	\cls{} bypasses all three by construction: its single-token output cannot be truncated, requires no string matching, and is always parseable. Classification reduces the output space from $\Sigma^*$ to $\{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$---strictly lower output complexity, though the underlying reasoning need not be simpler. We hypothesize a \emph{complexity-dependent advantage}: both formulations perform comparably on simple code, but \cls{} gains as output complexity triggers \cwm{} failure modes.
27	
28	\subsection{Oracle Accuracy-Utility Framework}
29	\label{sec:oracle}
30	
31	Per-test granularity is valuable only when per-test predictions are sufficiently accurate and multiple tests provide partially independent signals. Consider a buggy patch with $k = |T_{\text{f2p}}|$ fail-to-pass tests. A per-test verifier with recall $r$ detects the bug if it identifies at least one failing test:
32	%
33	\begin{equation}
34	  P_{\text{detect}}(k) = 1 - (1 - r)^{k_{\text{eff}}}
35	  \label{eq:pdetect}
36	\end{equation}
37	%
38	where $k_{\text{eff}}$ is the effective number of independent tests. Let $a_h$ denote the trajectory-level detection accuracy; it is independent of $k$.
39	
40	\paragraph{Block-correlation model.} Per-test predictions within the same patch are correlated. We model this via the intraclass correlation coefficient $\rho$ \citep[ICC;][]{shrout1979icc}:
41	%
42	\begin{equation}
43	  k_{\text{eff}} = \frac{k}{1 + (k - 1)\rho}
44	  \label{eq:keff}
45	\end{equation}
46	%
47	When $\rho = 0$, $k_{\text{eff}} = k$ (full independence); when $\rho = 1$, $k_{\text{eff}} = 1$ (per-test collapses to trajectory-level). The per-test advantage relative to a trajectory-level baseline is $\Delta(k) = P_{\text{detect}}(k) - a_h$, and the expected population advantage is:
48	%
49	\begin{equation}
50	  \mathbb{E}[\Delta] = \sum_{k=1}^{K} P(|T_{\text{f2p}}| = k) \cdot \Delta(k)
51	  \label{eq:expected-advantage}
52	\end{equation}
53	
54	\paragraph{Testable predictions.} This yields three predictions validated in \S\ref{sec:experiments}: (1)~at $k = 1$, $\Delta \approx 0$; (2)~$\Delta(k)$ increases with $k$, dampened by $\rho > 0$; (3)~$\mathbb{E}[\Delta]$ concentrates in multi-F2P-test instances.
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "953dece5-45ce-4ba7-8e73-583d6a174edc",
  "isSidechain": true,
  "promptId": "d5e605e9-006a-4a90-83e2-16d1eb41e85d",
  "agentId": "abe263163347f9054",
  "type": "user",
  "uuid": "ad371104-3aec-40a4-9997-a21b9a0a5206",
  "sourceToolAssistantUUID": "953dece5-45ce-4ba7-8e73-583d6a174edc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T08:18:37.118Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MFnC1ZoRGHT9YLAxAxrU22`</summary>

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
  "parentUuid": "ad371104-3aec-40a4-9997-a21b9a0a5206",
  "isSidechain": true,
  "agentId": "abe263163347f9054",
  "requestId": "req_011Cb5vGneUUUG9zouEf3Z7a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99c60f1e-3c21-4173-ac3c-dac7d8f2fc1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XD8dvcCkZAGZyhgzFzzoF1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8387,
      "cache_read_input_tokens": 16556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8387,
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

_source line 8 · 2026-05-16T08:18:37.124Z_

<details><summary>↩ Tool result · `toolu_01MFnC1ZoRGHT9YLAxAxrU22`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair has advanced rapidly on real-world software tasks. Agent-based systems such as SWE-agent~\cite{yang2024sweagent} and pipeline approaches like Agentless~\cite{xia2024agentless} resolve substantial fractions of SWE-bench~\cite{jimenez2024swebench} issues through candidate patch generation and validation. The prevailing strategy for improving resolve rates is test-time compute scaling~\cite{snell2024scaling}: generating $K$ candidate patches and selecting the best via a verifier. This verification step is critical---without it, the additional compute invested in diverse patch generation yields diminishing returns, because correct patches are diluted among incorrect ones. Full execution verification---running the repository's test suite against each candidate---is reliable but expensive, costing \$1--3 and several minutes per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}, making it prohibitive for large $K$. The resulting demand for fast, execution-free verification has driven work on learned verifiers~\cite{ni2023lever,shum2025swerm} and execution simulators~\cite{meta2025cwm,maimon2026selfexecution}, but the choice of \emph{how} to formulate the verification task---what the model predicts and in what format---has received surprisingly little systematic study.
5	
6	Two dominant paradigms have emerged. \textbf{Generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test, deriving verdicts by exact match. This suffers three failure modes at scale: (1)~\emph{token-budget exhaustion} truncates long outputs; (2)~\emph{string-value errors} reject semantically correct outputs differing in surface form; (3)~\emph{format compliance collapse} renders the majority of predictions unparseable at repository-level complexity, with parseable accuracy dropping below chance (38--43\% across model sizes).
7	
8	\textbf{Trajectory-level scoring}~\cite{shum2025swerm} predicts patch-level correctness directly, bypassing generation. This is robust---no outputs to truncate or parse---but discards per-test diagnostic signals needed for targeted re-repair~\cite{yang2024sweagent,xia2024agentless}. The apparent trade-off: generation preserves per-test granularity at the cost of reliability, while trajectory-level scoring provides reliability at the cost of granularity.
9	
10	We argue this trade-off is an artifact of the formulation. Per-test binary classification---predicting a single \textsc{Pass}/\textsc{Fail} token---eliminates all three failure modes by construction: a single-token output cannot be truncated, needs no string matching, and is always parseable, while preserving the per-test diagnostics that trajectory-level scoring discards. Prior learned verifiers (LEVER~\cite{ni2023lever}, CodeT~\cite{chen2023codet}) leverage execution signals but target candidate-level ranking rather than per-test diagnostic classification. No prior work compares classification and generation formulations at controlled model sizes across complexity levels.
11	
12	Crucially, the advantage is complexity-dependent. At function level, both formulations achieve near-equivalent accuracy (\mbox{1.24\pp{}} gap, 5 seeds, 4B). The gap emerges only when \cwm{} failure modes dominate: at repository level, it widens to \mbox{25.59\pp{}}. We formalize this via an oracle accuracy-utility framework (\S\ref{sec:oracle}) that predicts when per-test granularity provides value given test distribution and prediction correlation.
13	
14	We validate these predictions through controlled experiments comparing the three formulations on function-level benchmarks (HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp}) and repository-level tasks (SWE-bench Verified~\cite{chowdhury2024swebenchverified}), using Qwen3~\cite{qwen2025qwen3} models at 4B and 8B parameters with matched training data and compute. Figure~\ref{fig:reformulation} illustrates the three formulations. We make the following contributions:
15	
16	\begin{itemize}[leftmargin=*,itemsep=2pt]
17	\item \textbf{Complexity-dependent reformulation advantage.} The \cls{}--\cwm{} gap grows with complexity: near-null at function level (\mbox{1.18\pp{}}, 4B), widening to 2.26\pp{} at 8B (bootstrap mean, $p = 0.0066$; both 3 seeds), and 19--26\pp{} at repository level (8B-8B: 19.31\pp{}; 4B-4B: 25.59\pp{}, seed~42)---an order of magnitude larger than function-level. \cwm{} generation quality uniformly degrades with scale: parseable-only accuracy decreases from 42.9\% (4B) to 38.5\% (8B) while unparseable rate increases from 53.7\% to 73.8\%. Function-level scaling provides converging evidence: \cls{} gains \mbox{+0.99\pp{}} (4B$\to$8B) while \cwm{} loses \mbox{$-$0.27\pp{}}, consistent with a generation bottleneck rather than a capacity limitation.
18	
19	\item \textbf{Diagnostic granularity at equivalent accuracy.} Per-test classification achieves statistically equivalent variant-level accuracy to trajectory-level scoring (TOST equivalence test $p = 0.007$, $\pm$2\pp{} margin) while providing per-test diagnostic signals---which specific tests fail---at no accuracy cost. This enables downstream applications such as targeted re-repair that trajectory-level verifiers cannot support.
20	
21	\item \textbf{Accuracy-utility frontier characterization.} Oracle analysis on SWE-bench Verified~\cite{chowdhury2024swebenchverified} shows that the per-test advantage concentrates in instances with $T \geq 2$ FAIL\_TO\_PASS tests (31\% of instances, contributing 55\% of total advantage), while instances with $T = 1$ (69\%) gain nothing from per-test granularity. This provides a practical decision framework for when per-test verification is worth deploying.
22	\end{itemize}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99c60f1e-3c21-4173-ac3c-dac7d8f2fc1a",
  "isSidechain": true,
  "promptId": "d5e605e9-006a-4a90-83e2-16d1eb41e85d",
  "agentId": "abe263163347f9054",
  "type": "user",
  "uuid": "f995a408-5a91-4935-b5e7-654269ed1abc",
  "sourceToolAssistantUUID": "99c60f1e-3c21-4173-ac3c-dac7d8f2fc1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T08:18:37.425Z_

<details open><summary>🔧 Tool call — Read · `toolu_0191C6zzeEejWySxUcfzUHSd`</summary>

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
  "parentUuid": "f995a408-5a91-4935-b5e7-654269ed1abc",
  "isSidechain": true,
  "agentId": "abe263163347f9054",
  "requestId": "req_011Cb5vGneUUUG9zouEf3Z7a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "718d0bee-0e7b-42b1-bfa4-e6b3a6b6d3b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XD8dvcCkZAGZyhgzFzzoF1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8387,
      "cache_read_input_tokens": 16556,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8387
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 16556,
          "cache_creation_input_tokens": 8387,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8387,
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

_source line 10 · 2026-05-16T08:18:37.431Z_

<details><summary>↩ Tool result · `toolu_0191C6zzeEejWySxUcfzUHSd`</summary>

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
  "parentUuid": "718d0bee-0e7b-42b1-bfa4-e6b3a6b6d3b6",
  "isSidechain": true,
  "promptId": "d5e605e9-006a-4a90-83e2-16d1eb41e85d",
  "agentId": "abe263163347f9054",
  "type": "user",
  "uuid": "30928fa6-dcab-42cb-9a43-990bf212474c",
  "sourceToolAssistantUUID": "718d0bee-0e7b-42b1-bfa4-e6b3a6b6d3b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T08:18:41.662Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CNagrJYoEpkbXMaYZyDHTa`</summary>

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
  "parentUuid": "30928fa6-dcab-42cb-9a43-990bf212474c",
  "isSidechain": true,
  "agentId": "abe263163347f9054",
  "requestId": "req_011Cb5vH7UodjFpSEecTVoN2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0119170c-e86f-4de6-9252-f90201e4b381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uikczmz9ZVbeTLLMWwphFS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6268,
      "cache_read_input_tokens": 24943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6268,
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

_source line 12 · 2026-05-16T08:18:41.667Z_

<details><summary>↩ Tool result · `toolu_01CNagrJYoEpkbXMaYZyDHTa`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation for Code.}
5	Code World Models~\cite{meta2025cwm} mid-train a 32B LLM on execution traces to predict output strings, establishing the generation-based paradigm for execution-free code verification.
6	Self-Execution~\cite{maimon2026selfexecution} extends this with step-by-step trace prediction, demonstrating that simulation-based self-verification can improve code generation without external execution.
7	CodeMind~\cite{liu2024codemind} evaluates code reasoning along multiple dimensions including independent and dependent execution reasoning.
8	SolidCoder~\cite{lee2026solidcoder} bridges mental simulation and actual execution via concrete execution feedback.
9	Abdollahi et al.~\cite{abdollahi2025demystifying} identify systematic failure modes in LLM trace prediction, including position-dependent and cascading errors.
10	All share a generation formulation whose cost scales with output length and whose reliability degrades when outputs are complex---at repository-level complexity, we observe format compliance collapse (53--67\% unparseable outputs; \S\ref{sec:experiments}). We reformulate as per-test classification and show the advantage is complexity-dependent: negligible at function level but critical at repository scale.
11	
12	\paragraph{LLM-based Verification for Code Repair.}
13	SWE-RM~\cite{shum2025swerm} trains a 30B MoE reward model for trajectory-level execution-free patch ranking, achieving strong results on SWE-bench without test execution.
14	Patch Reasoner~\cite{xu2025patchreasoner} uses chain-of-thought reasoning for patch verification.
15	Snell et al.~\cite{snell2024scaling} show that test-time compute scaling via verification can outperform parameter scaling, establishing verification quality as a key lever for code generation improvement.
16	S*~\cite{li2025sstar} combines execution-grounded selection with model-based scoring for efficient test-time scaling.
17	VG-Search~\cite{chen2025vgsearch} studies how verification granularity affects compute-efficient scaling, finding that finer-grained verification can improve selection efficiency.
18	These works treat verification granularity as a design choice but do not compare the underlying \emph{formulation}---classification vs.\ generation---at controlled capacity. We formally compare per-test and trajectory-level granularity, showing statistical equivalence (TOST $p = 0.007$) with additional per-test diagnostic signals.
19	
20	\paragraph{Learned Code Verifiers.}
21	LEVER~\cite{ni2023lever} trains a classifier to re-rank code candidates by predicting execution correctness, learning verification from execution feedback.
22	CodeT~\cite{chen2023codet} generates auxiliary test cases and uses dual execution agreement---consensus between generated code and generated tests---as a verification signal.
23	Both methods leverage execution signals during training but target execution-free deployment, a goal shared by our classification formulation. Unlike LEVER's candidate-level ranking and CodeT's agreement-based filtering, we provide \emph{per-test} diagnostic verdicts that identify which specific tests fail, and systematically compare classification against generation on the same model, data, and compute budget, isolating the effect of task formulation.
24	
25	\paragraph{Automated Program Repair.}
26	SWE-bench~\cite{jimenez2024swebench} and SWE-bench Verified~\cite{chowdhury2024swebenchverified} provide standard benchmarks for repository-level repair, driving rapid progress in LLM-based program repair.
27	SWE-agent~\cite{yang2024sweagent} uses tool-augmented agents while Agentless~\cite{xia2024agentless} demonstrates a simpler localize--repair--validate pipeline that achieves competitive results.
28	Yang et al.~\cite{yang2025aprsurvey} survey the broader landscape of LLM-based program repair, identifying verification as a persistent bottleneck across approaches.
29	These systems rely on execution-based validation as the final filter, with verification cost scaling linearly in the number of candidates. Per-test classification provides failure-localized signals that could inform targeted re-repair---re-generating only the code responsible for a specific failing test---a capability absent from trajectory-level verifiers.
30	
31	\paragraph{Classification vs.\ Generation in NLP.}
32	Task framing affects model performance across NLP: T5~\cite{raffel2020t5} and BART~\cite{lewis2020bart} show generation--classification tradeoffs under controlled capacity, while SQuAD~\cite{rajpurkar2016squad} demonstrates that constraining output space (span extraction vs.\ generation) can simplify tasks without sacrificing quality. We extend this lens to code verification, identifying code complexity as the key moderator of the classification--generation tradeoff.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0119170c-e86f-4de6-9252-f90201e4b381",
  "isSidechain": true,
  "promptId": "d5e605e9-006a-4a90-83e2-16d1eb41e85d",
  "agentId": "abe263163347f9054",
  "type": "user",
  "uuid": "8ed4f726-7c4c-4380-adad-025d061739cf",
  "sourceToolAssistantUUID": "0119170c-e86f-4de6-9252-f90201e4b381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T08:18:42.223Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ALwmfPz7yq3cPCxJaBRdFK`</summary>

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
  "parentUuid": "8ed4f726-7c4c-4380-adad-025d061739cf",
  "isSidechain": true,
  "agentId": "abe263163347f9054",
  "requestId": "req_011Cb5vH7UodjFpSEecTVoN2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a0a9754-538d-4474-873f-e4afa38890a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uikczmz9ZVbeTLLMWwphFS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6268,
      "cache_read_input_tokens": 24943,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6268
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 24943,
          "cache_creation_input_tokens": 6268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6268,
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

_source line 14 · 2026-05-16T08:18:42.227Z_

<details><summary>↩ Tool result · `toolu_01ALwmfPz7yq3cPCxJaBRdFK`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We reformulated execution simulation for code repair verification from open-ended output generation to per-test binary classification. Our central finding is that the advantage of this reformulation is complexity-dependent: on function-level code with short, structurally simple outputs, classification and generation achieve near-equivalent accuracy; at repository scale, classification dominates by a wide margin. The generation formulation suffers a compounding failure on complex code---format non-compliance discards the majority of predictions, and the surviving parseable outputs are themselves unreliable, falling below chance-level accuracy (50\%). Classification is immune to this failure mode by construction, as binary verdicts require no structured output parsing. Moreover, at function level, scaling model capacity does not resolve the generation bottleneck: \cwm{} accuracy decreases by 0.27\pp{} from 4B to 8B, consistent with a formulation-level bottleneck at this complexity tier. Independently, per-test classification provides fine-grained diagnostic signals---identifying which specific tests a patch fails---at equivalent trajectory-level accuracy, with the advantage concentrating in instances that contain multiple fail-to-pass tests.
5	
6	For test-time scaling pipelines evaluating patches against multi-test suites, classification avoids the compounding failure that degrades generation on complex code. Per-test verdicts unlock targeted re-repair guided by failure localization rather than binary accept/reject decisions.
7	
8	\paragraph{Limitations.}
9	All experiments use a single model family (Qwen3); scaling behavior may differ across architectures or pre-training regimes. The repo-level same-size comparisons each use a single seed (4B-4B and 8B-8B); the second seed's repo-level comparison is cross-size (8B \cls{} vs.\ 4B \cwm{}), not an apple-to-apple same-size match. No downstream re-repair experiment validates whether per-test diagnostic signals translate to actual fix improvements. Pass-to-pass regression rates are negligible (1.04\% mean, 0\% median), meaning the per-test advantage currently concentrates in fail-to-pass discrimination; regression detection---a potential benefit of per-test granularity---remains untested in practice. Training data comprises synthetic mutations; transfer to naturally occurring developer bugs is untested. A matched-context ablation (\cls{} evaluated at \texttt{max\_seq\_length}$=$2,048) confirms that $>$95\% of the \cls{}--\cwm{} gap stems from formulation differences, not input context disparity. The oracle analysis assumes ground-truth test labels; real-world per-test advantage is upper-bounded by classifier accuracy.
10	
11	\paragraph{Future work.}
12	\cls{}--\cwm{} error complementarity (oracle: 90.63\%) motivates ensemble verification that routes instances by predicted output complexity---using generation when outputs are simple and classification when they are complex. Per-test failure signals enable diagnostic re-repair: localizing faults from per-test verdicts rather than discarding failed patches outright. Multi-model validation across architectures, multi-seed repo-level replication, and integration with test-time scaling systems (best-of-$N$ with per-test reranking) are natural next steps.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a0a9754-538d-4474-873f-e4afa38890a5",
  "isSidechain": true,
  "promptId": "d5e605e9-006a-4a90-83e2-16d1eb41e85d",
  "agentId": "abe263163347f9054",
  "type": "user",
  "uuid": "7f7cd424-579a-402d-b74a-0703c1bf9a80",
  "sourceToolAssistantUUID": "2a0a9754-538d-4474-873f-e4afa38890a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-16T08:19:43.486Z_

Now I have a comprehensive understanding of the paper. Let me produce the review.

---

## Review: "Classification Beats Generation: Complexity-Dependent Reformulation Advantage for Per-Test Code Repair Verification"

### Summary

This paper reformulates execution simulation for code repair verification from generation (predicting execution output strings) to binary classification (pass/fail per test). The central claim is that the advantage is complexity-dependent: negligible at function-level (~1.2pp gap) but dominant at repository-level (19-26pp gap), driven by CWM's format compliance collapse at scale. The paper also introduces a trajectory-level comparator and an oracle accuracy-utility framework.

---

### Strengths

- **Well-motivated research question.** The observation that task formulation---not model capacity---is the binding constraint for execution simulation is genuinely useful. The complexity-dependent framing gives the contribution a clear boundary condition rather than overclaiming universal superiority.

- **Controlled experimental design at function level.** Matched LoRA configurations, same training data, same effective batch size, and multi-seed evaluation (5 seeds for main results, 3 matched bf16 seeds for scaling) enable clean causal attribution at function level. The hyperparameter table (Appendix) is complete and reproducible.

- **Appropriate statistical methodology.** Clustered bootstrap accounting for within-problem correlation (ICC=0.191, DEFF=3.97), TOST equivalence testing for CLS-TRAJ comparison, and bootstrap CIs for the scaling gap are all methodologically sound and well-reported.

- **Ablations address obvious confounds.** LoRA rank ablation, majority voting ablation, and the sequence-length matched-context experiment (showing <3% of gap is context-related) strengthen the formulation-level bottleneck interpretation.

- **Transparency about limitations.** The paper explicitly flags single-seed repo-level comparisons, the misleading CWM overall accuracy (inflated by default-pass), and the synthetic-to-real transfer gap.

- **The TRAJ baseline adds value.** Showing CLS achieves per-test granularity at no accuracy cost relative to trajectory-level scoring (TOST p=0.007) is a clean result that establishes the formulation is not trading off accuracy for diagnostics.

---

### Weaknesses

- **Repo-level evidence is severely underpowered.** The headline claim---25pp gap at repo level---rests on single-seed comparisons for both the 4B-4B and 8B-8B same-size matches. The paper's own function-level results show checkpoint/seed variance can be substantial (CLS 4B seed 123 at repo-level achieves only 75.33% vs. 83.63% at seed 42---an 8pp swing). Without multi-seed repo-level replication for both CLS and CWM at the same model size, the precise magnitude of the gap is not established with any statistical confidence. The gap clearly exists and is large, but the exact claim of "19-26pp" carries no error bar.

- **CWM training is arguably suboptimal, making the comparison partially unfair.** The paper uses LoRA rank 16 for CWM, which is quite small for a generation task requiring multi-token structured output. The rank-32 ablation is only at function level, where CWM was already performing well. At repo level---where CWM catastrophically fails---no capacity ablation is reported. More critically, the paper uses max_seq_length=2048 for training CWM on repository-level code, leaving only ~1024 tokens for generation. If repo-level outputs are routinely longer than 1024 tokens, the "format compliance collapse" may be partly a training/inference configuration issue rather than a fundamental formulation limitation. The paper notes 38% of failures are "token exhaustion" but does not ablate with longer generation budgets.

- **No DeepSeek-Coder results at repo level for CWM.** The paper summary mentions DeepSeek cross-architecture validation, but the actual paper text only shows Qwen3 at repo level. The "cross-architecture" evidence is limited to function level, where gaps are small and the central claim is that formulations are equivalent at that complexity. This weakens the generalizability claim.

- **The CWM baseline is not representative of the state-of-the-art.** The authors acknowledge their CWM is a LoRA fine-tuned 4B/8B model, not a reproduction of Meta's 32B Code World Model. This is a fair controlled comparison, but it means the paper cannot claim that classification "beats generation" in general---it beats generation at the same small model scale with the same adapter budget. The title oversells relative to the evidence.

- **No downstream re-repair experiment despite claiming diagnostic utility.** The conclusion states "No downstream re-repair experiment validates whether per-test diagnostic signals translate to actual fix improvements." Yet the user-provided summary mentions a re-repair result (Table 9: +6.0pp). This discrepancy is confusing---either the experiment was done (and should be in the paper body) or it was not (and the paper summary is inaccurate). Reading the actual paper text, I find no re-repair results in the paper body, only in the user prompt summary. If these results exist but are excluded from the paper, they should be included; if they don't exist, the paper correctly acknowledges this as a limitation.

- **Oracle analysis uses function-level ICC for repo-level predictions.** The oracle framework applies ICC=0.191 (from function-level data) to reason about SWE-bench Verified (repo-level). The paper acknowledges repo-level ICC is much higher (0.3146), but uses the lower estimate for the headline numbers. This creates an inconsistency: the block-correlated advantages in Table A1 are computed under the wrong correlation structure for the actual deployment scenario.

- **Synthetic training data limits external validity.** All training uses mutation-based synthetic data (operator_swap, off_by_one, return_value, boundary_removal, gold). Real developer bugs have different distributions. The paper acknowledges this but provides no evidence of transfer to natural bugs.

---

### Questions for Authors

1. Can you provide multi-seed repo-level results for CWM at 8B (you have seeds 42/123 for CLS 8B---do matched CWM 8B runs exist)?

2. What is the average expected output length for repo-level CWM test samples? If most ground-truth outputs exceed 1024 tokens, the "format compliance collapse" is partially an engineering constraint (insufficient generation budget) rather than a formulation bottleneck.

3. The paper states CWM 8B unparseable rate is 73.8% but Table 5 in the summary says 85%. Which is correct? (The paper text Table 3 shows 73.8% for 8B seed 42.)

4. Why does CWM 8B have worse parseable accuracy (38.5%) than CWM 4B (42.9%)? If this is a genuine finding rather than an artifact of single-seed noise, it would strengthen the bottleneck argument---but it's currently single-seed evidence.

5. Would a CWM variant with explicit format prompting or constrained decoding (forcing structured output) substantially reduce the unparseable rate? This would help isolate whether the issue is generation difficulty or format adherence.

6. The re-repair experiment mentioned in the review context (Tables 9-10)---is this in the paper or planned? Its presence would substantially strengthen the contribution.

---

### Minor Issues

- The paper text uses LoRA rank 16, alpha 32, but the user summary states "rank 64, alpha 128." This discrepancy suggests the paper has been revised---ensure consistency between abstract claims and appendix hyperparameters.
- Table 3 (repo-level) in the paper shows CLS 8B seeds 42/123 but only CWM 8B seed 42. The asymmetry is acknowledged but weakens the comparison.
- The variance compression observation (CWM std 0.37 < CLS std 0.78) is interesting but could also reflect that CWM is undertrained/underfitting at function level rather than a "bottleneck ceiling."
- Figure references (fig:scaling_gap, fig:reformulation) are mentioned but figures are not included in the review materials.

---

### Overall Assessment

The paper identifies a real and practically important phenomenon: generation-based execution simulation catastrophically fails at repository-level complexity while classification remains robust. The function-level experiments are well-controlled and statistically sound. However, the headline repo-level results---where the contribution is most impactful---are underpowered (single-seed), the CWM baseline may be disadvantaged by insufficient generation budget, and the paper lacks downstream validation of the diagnostic utility that motivates per-test classification. The contribution is incremental but clear: showing that formulation matters more than capacity at this scale.

**Overall Score: 4 (Weak Accept)**

**Confidence: 4/5** (I am confident in identifying the statistical and experimental limitations, though I acknowledge the practical importance of the finding)

**Recommendation: Weak Accept**

The core insight is sound and useful for the community. The function-level evidence is rigorous. The repo-level evidence, while understandably expensive to replicate, needs at minimum 2-3 seeds per condition to be taken at face value in a top venue. If the authors can provide multi-seed repo-level results and address the generation budget confound (even briefly), this would move to a clear Accept. As submitted, the paper's central claim is well-supported qualitatively but quantitatively under-specified at the complexity level where it matters most.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f7cd424-579a-402d-b74a-0703c1bf9a80",
  "isSidechain": true,
  "agentId": "abe263163347f9054",
  "requestId": "req_011Cb5vHUKS4CjKjqMoUdnSp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3914c9d6-26d8-4160-9372-6e35f93f9713",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "bb1cd3bd-4c39-4492-be2f-2de9468a472a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157G7QQYtdyjgtGKDyv6b5Q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2190,
      "cache_read_input_tokens": 31211,
      "output_tokens": 2241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2190
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2241,
          "cache_read_input_tokens": 31211,
          "cache_creation_input_tokens": 2190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2190,
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
