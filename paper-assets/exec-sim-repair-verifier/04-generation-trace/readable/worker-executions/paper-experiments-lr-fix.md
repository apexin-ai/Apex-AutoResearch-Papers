# paper experiments lr fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_paper_experiments-lr-fix_20260515T145959.log`
- **Structured JSON:** [`db7b8d8afae237421e1d.json`](../../sessions/db/db7b8d8afae237421e1d.json)

## Before a recorded user message

15 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "64d32ce8-6503-468a-bbdd-d0cd5f23d18a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778873400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "cec344f8-aa7f-46d0-b47e-2fdc331fb3aa",
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the file to find the lr description in §4.1 Setup.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "uuid": "a676f813-4678-4914-8ba0-1b5fbbbe89cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hhSp3FTo1Z3JFzuFiXrA7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11648,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11648
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01HbQ97STZ9TVMQTxFG7WHVy`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "uuid": "bdb9a86e-a29d-4d13-acef-847f5c42b2f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hhSp3FTo1Z3JFzuFiXrA7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11648,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11648
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T15:00:16.088Z_

<details><summary>↩ Tool result · `toolu_01HbQ97STZ9TVMQTxFG7WHVy`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate \cls{}, \cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Function-level dataset.}
10	We construct a function-level benchmark from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} by generating mutated variants (five mutation types: \texttt{wrong\_operator}, \texttt{off\_by\_one}, \texttt{boundary\_error}, \texttt{return\_value}, \texttt{type\_error}), with labels verified by execution (5s timeout). The dataset contains 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	
12	\paragraph{Repo-level dataset.}
13	We construct a repo-level benchmark from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants, extracting per-test instances from repository-scale patches. The dataset contains approximately 70K training samples, with validation ($n{=}9{,}335$) and test ($n{=}9{,}784$) splits having zero problem overlap. The majority baseline (always predict pass) is 72.96\%. Mutation type composition differs between validation and test due to the non-overlapping problem split; this is a consequence of the design (no data leakage), and val-based checkpoint selection is standard practice~\cite{jimenez2024swebench}.
14	
15	\paragraph{Models and training.}
16	We fine-tune Qwen3-4B and Qwen3-8B~\cite{yang2024qwen25} with LoRA~\cite{hu2022lora} (rank 16, lr $2{\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Our \cwm{} baseline is a LoRA fine-tuned variant trained for controlled comparison, not a reproduction of the full-scale 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).
17	
18	\paragraph{Oracle analysis and statistics.}
19	We use SWE-bench Verified~\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\S\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\ trajectory-level comparison uses TOST~\cite{schuirmann1987tost} with $\pm$2\pp{} margin. Within-problem correlation is quantified via the intraclass correlation coefficient~\cite{shrout1979icc}.
20	
21	
22	\subsection{Function-Level Results}
23	\label{sec:func_results}
24	
25	Table~\ref{tab:main_results} reports function-level results across formulations.
26	
27	\begin{table}[t]
28	\centering
29	\small
30	\caption{Function-level per-test verification results on HumanEval+MBPP test set (1,890 samples). \cls{}: per-test binary classification; \cwm{}: execution output generation; TRAJ: trajectory-level scoring; ZS: zero-shot LLM-as-judge. Mean $\pm$ std over seeds reported where applicable.}
31	\label{tab:main_results}
32	\resizebox{\columnwidth}{!}{%
33	\setlength{\tabcolsep}{4pt}
34	\begin{tabular}{llcc}
35	\toprule
36	\textbf{Method} & \textbf{Model} & \textbf{Seeds} & \textbf{Accuracy (\%)} \\
37	\midrule
38	\cls{} (fine-tuned) & 4B & 5 & \textbf{88.43 $\pm$ 0.78} \\
39	\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\pm$ 0.37 \\
40	TRAJ (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
41	\midrule
42	ZS LLM-as-judge & 8B & 1 & 64.40 \\
43	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
44	\bottomrule
45	\end{tabular}}
46	\end{table}
47	
48	Fine-tuned \cls{} achieves a mean accuracy of 88.43\% ($\pm$0.78 across seeds 87.83, 89.52, 87.88, 89.00, 87.94), compared to 87.19\% ($\pm$0.37; seeds: 87.51, 87.20, 86.98, 86.67, 87.57) for \cwm{} and 86.30\% ($\pm$0.97; seeds: 85.66, 85.47, 87.40, 87.31, 85.66) for TRAJ. The \cls{}--\cwm{} gap is 1.24\pp{}, which is modest at this complexity level---both formulations operate on short, single-function code with simple return values, where generation is not yet bottlenecked by token budget or string complexity.
49	
50	Zero-shot baselines lag by a wide margin: Qwen3-8B achieves 64.40\% and Qwen3-32B (NF4) achieves 71.69\%, both far below fine-tuned 4B models. The 8B zero-shot model exhibits a strong FAIL bias (fail recall 95.8\%, pass recall 35.1\%), indicating that zero-shot prompting cannot achieve the balanced precision/recall that fine-tuning produces. Even with 8$\times$ more parameters, the 32B zero-shot model trails the fine-tuned 4B \cls{} by 16.74\pp{}, confirming that task-specific fine-tuning, rather than model scale alone, is necessary for reliable per-test verification.
51	
52	
53	\subsection{Scaling Behavior}
54	\label{sec:scaling}
55	
56	Table~\ref{tab:scaling} compares \cls{} and \cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.
57	
58	\begin{table}[t]
59	\centering
60	\small
61	\caption{Model-size scaling: \cls{} vs.\ \cwm{} accuracy (\%) at 4B and 8B. Three matched seeds in full precision. The \cls{}--\cwm{} gap widens from 1.18\pp{} to 2.43\pp{}.}
62	\label{tab:scaling}
63	\setlength{\tabcolsep}{4pt}
64	\begin{tabular}{llccccc}
65	\toprule
66	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{s456} & \textbf{Mean} & \textbf{Gap} \\
67	\midrule
68	\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \multirow{2}{*}{1.18} \\
69	\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\
70	\midrule
71	\cls{} & 8B & \textbf{90.48} & 89.40 & 88.31 & \textbf{89.40} & \multirow{2}{*}{\textbf{2.43}} \\
72	\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\
73	\bottomrule
74	\end{tabular}
75	\end{table}
76	
77	At 4B, \cls{} and \cwm{} are separated by 1.18\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\pp{}. Clustered bootstrap analysis yields a mean gap of 2.26\pp{} ($p = 0.0066$, 95\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.
78	
79	The asymmetry in scaling efficiency is striking: from 4B to 8B, \cls{} gains +0.99\pp{} (88.41 $\to$ 89.40) while \cwm{} loses $-$0.27\pp{} (87.23 $\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \cwm{} accuracy. However, the \cwm{} regression ($-$0.27\pp{}) falls within seed noise (3-seed std ${\sim}$0.5\pp{}) and could reflect suboptimal hyperparameter transfer (LoRA rank and learning rate were not re-tuned for 8B) rather than a fundamental bottleneck; disentangling these factors requires larger-scale experiments. We also acknowledge the limited model-level statistical power of three seeds: while the clustered bootstrap provides instance-level confidence (1,890 samples $\times$ 10K resamples), three model instances cannot fully separate seed variance from systematic scaling effects. Figure~\ref{fig:scaling_gap} visualizes the diverging trajectories. Whether this divergence amplifies at repository-level complexity is examined in \S\ref{sec:repo}.
80	
81	
82	\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
83	\label{sec:equivalence}
84	
85	A natural concern is whether per-test predictions, when aggregated to the variant level, match the accuracy of a model trained directly at that granularity. We address this by comparing \cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds.
86	
87	The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]), with per-seed gaps ranging from $-$1.84 to +1.45\pp{} (seed 42: $-$0.97; seed 123: +1.45; seed 456: $-$1.84; seed 789: $-$0.78; seed 0: $-$0.29). The TOST equivalence test rejects the null hypothesis of non-equivalence at $p = 0.007$ with a $\pm$2\pp{} margin, confirming that per-test classification and trajectory-level scoring achieve statistically equivalent variant-level accuracy.
88	
89	Critically, however, predictions within the same problem are not independent. The intraclass correlation coefficient is ICC $= 0.191$ ($p < 0.0001$), yielding a design effect DEFF $= 3.97$. This means that naive i.i.d.\ confidence intervals would be approximately $2\times$ too narrow. All statistical tests in this paper use clustered bootstrap to account for this within-problem correlation.
90	
91	The practical implication is clear: per-test classification provides per-test diagnostic information---which specific tests fail and why---at no cost to variant-level accuracy. A trajectory-level model gives only a binary patch verdict, discarding the per-test signal that downstream repair systems could exploit for targeted re-repair.
92	
93	
94	\subsection{Accuracy-Utility Frontier}
95	\label{sec:oracle-results}
96	
97	Where does per-test granularity actually help? We formalize this via an oracle analysis on SWE-bench Verified, stratifying instances by the number of F2P tests $T$ and comparing per-test vs.\ trajectory-level oracle resolve rates under both i.i.d.\ and block-correlated error models (using the empirical ICC $= 0.191$).
98	
99	\begin{table}[t]
100	\centering
101	\small
102	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses empirical ICC $= 0.191$. P2P regression rate: 1.04\% mean, 0\% median.}
103	\label{tab:oracle}
104	\resizebox{\columnwidth}{!}{%
105	\setlength{\tabcolsep}{3pt}
106	\begin{tabular}{lcccc}
107	\toprule
108	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
109	\midrule
110	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
111	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
112	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
113	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
114	\midrule
115	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
116	\bottomrule
117	\end{tabular}}
118	\end{table}
119	
120	Table~\ref{tab:oracle} reveals a sharp concentration of per-test advantage. When $T = 1$---the dominant case at 68.7\% of SWE-bench instances---per-test and trajectory-level are informationally equivalent (block advantage $-$0.09\pp{}), because a single F2P test provides no more signal than a binary patch verdict. The advantage materializes at $T = 2$ (19.1\% of instances), where block-correlated advantage reaches 31.69\pp{}, contributing 55.3\% of the total advantage. Instances with $T \geq 3$ exhibit block advantages exceeding 40\pp{} but constitute only 12.2\% of instances. The overall block-correlated advantage is 10.93\pp{}, driven almost entirely by the $T \geq 2$ minority. Figure~\ref{fig:oracle_stratified} visualizes this distribution.
121	
122	Block correlation amplifies the advantage relative to the i.i.d.\ model: at $T = 2$, the block advantage (31.69\pp{}) is 1.7$\times$ the i.i.d.\ advantage (18.49\pp{}). This occurs because correlated errors make the per-test classifier more likely to get all tests correct or all wrong for a given problem, increasing the information value of each additional test.
123	
124	\paragraph{P2P regression signal.}
125	The P2P regression rate in SWE-bench Verified is low: 1.04\% mean and 0\% median---77\% of incorrect patches break zero P2P tests. This means per-test granularity on the P2P dimension currently provides minimal signal. The practical value of per-test verification concentrates in F2P discrimination, particularly for instances with multiple F2P tests.
126	
127	
128	\subsection{Repo-Level Results}
129	\label{sec:repo}
130	
131	Table~\ref{tab:repo_level} compares \cls{} and \cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy (D088 protocol); the test set ($n{=}9{,}784$) has zero problem overlap with validation.
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\caption{Repo-level per-test verification on SWE-bench Verified test set ($n{=}9{,}784$, val-selected checkpoints). Same-size 4B comparison is primary; \cls{} 8B included for scaling context; \cwm{} 8B in progress.}
137	\label{tab:repo_level}
138	\resizebox{\columnwidth}{!}{%
139	\setlength{\tabcolsep}{3pt}
140	\begin{tabular}{llccccc}
141	\toprule
142	\textbf{Method} & \textbf{Size} & \textbf{Seed} & \textbf{Acc (\%)} & \textbf{Macro \fone{}} & \textbf{Unparse (\%)} & \textbf{vs Maj.\ (\pp{})} \\
143	\midrule
144	\cls{} & 4B & 42 & \textbf{83.63} & 75.63 & 0.0 & +10.67 \\
145	\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & $-$14.92 \\
146	\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & $-$13.87 \\
147	\midrule
148	\cls{} & 8B & 42 & 83.52 & 77.50 & 0.0 & +10.56 \\
149	\cls{} & 8B & 123 & 85.60 & 78.38 & 0.0 & +12.64 \\
150	\cwm{} & 8B & --- & --- & --- & --- & --- \\
151	\midrule
152	Majority & --- & --- & 72.96 & --- & --- & --- \\
153	\bottomrule
154	\end{tabular}}
155	\end{table}
156	
157	The same-size 4B comparison reveals a 25.59\pp{} gap: \cls{} achieves 83.63\% accuracy (macro \fone{} 75.63) versus \cwm{} at 58.04\% (macro \fone{} 51.67) on seed 42. \cwm{} falls 14.92\pp{} below the majority baseline (72.96\%), indicating negative utility---a system that always predicts pass outperforms \cwm{}. A second \cwm{} seed (123) yields 59.09\% with a higher unparseable rate (67.2\% vs.\ 53.7\%), confirming the failure is not seed-specific.
158	
159	The primary driver is output format compliance collapse. \cwm{} produces unparseable outputs for 53.7\% (seed 42) and 67.2\% (seed 123) of test instances, while \cls{} produces zero unparseable outputs across all configurations. The generation budget (1,024 tokens) is sufficient for the outputs required---this is not a token-budget limitation but a failure of the model to produce structured execution predictions when faced with repository-level code complexity. Among parseable \cwm{} outputs, accuracy is 42--43\%---below both the majority baseline (72.96\%) and chance level (50\%)---indicating that even well-formed \cwm{} predictions are anti-informative at this complexity level. \cls{}, producing a single binary token per test, is immune to format compliance failures by construction. Figure~\ref{fig:scaling_gap} visualizes the gap amplification from function level (1.24\pp{}) to repo level (25.59\pp{}).
160	
161	For scaling context, we include \cls{} 8B results (cross-size comparison, not directly comparable to the same-size gap above). \cls{} 8B achieves 83.52\% (seed 42) and 85.60\% (seed 123), yielding cross-size gaps of 25.48\pp{} and 26.51\pp{} against \cwm{} 4B at the corresponding seeds. Within \cls{}, the 4B$\to$8B transition at repo level shows 83.63\% $\to$ 83.52\% (seed 42), a difference within noise, suggesting that classification may be approaching a capacity ceiling at repo-level complexity or that checkpoint selection variance dominates at this scale. \cwm{} 8B training is in progress; if \cwm{} 8B performs similarly to 4B, this would confirm a generation bottleneck rather than a capacity limitation.
162	
163	\paragraph{Sequence length and formulation cost.} Both \cls{} and \cwm{} are trained with identical \texttt{max\_seq\_length}$=$2,048, so training-time input context is fully controlled. The asymmetry arises at inference: \cwm{} reserves \texttt{max\_new\_tokens}$=$1,024 for output generation, leaving an effective input window of ${\sim}$1,024 tokens; \cls{} produces a single token and can allocate nearly all context to input (\texttt{max\_seq\_length}$=$5,120 at 4B, 8,192 at 8B during evaluation). This eval-time difference primarily reflects structural properties of each formulation: generation \emph{must} reserve context for output tokens, while classification need not. A matched-context ablation confirms this: \cls{} 8B evaluated at \texttt{max\_seq\_length}$=$2,048 achieves 82.83\%, a reduction of only 0.69\pp{} from the 8,192-token evaluation (83.52\%). The matched-context gap (\cls{}@2,048 vs.\ \cwm{}@2,048) is 24.79\pp{}, accounting for 97\% of the full 25.59\pp{} gap---input context disparity explains at most 3\% of the observed difference. Moreover, input context cannot explain the qualitative failures. Format compliance collapse---53.7--67.2\% of \cwm{} outputs are unparseable despite sufficient generation budget---reflects the model's inability to produce structured predictions, not input truncation. Among parseable outputs where the model does produce well-formed predictions, accuracy is 42--43\%, below chance level (50\%): if input truncation were the sole issue, parseable outputs should at minimum exceed chance.
164	
165	\paragraph{Limitations.} The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline), indicating that val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The validation and test sets have zero problem overlap but differ in mutation type composition, introducing potential distribution shift. All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences.
166	
167	
168	\subsection{Analysis}
169	\label{sec:analysis}
170	
171	\paragraph{(a) Error complementarity.}
172	\cls{} and \cwm{} make errors in opposite directions at function level. Among \cls{} errors (seed 42), 75.5\% are false negatives (FAIL $\to$ PASS), meaning the classifier tends to over-predict passing. Among \cwm{} errors, 83.1\% are false positives (PASS $\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\% accuracy, a 3.12\pp{} improvement over \cls{} alone (87.51\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains.
173	
174	\paragraph{(b) CWM error mode breakdown.}
175	At repo level, \cwm{} output format compliance collapses. Of 9,784 test instances, 5,255 (53.7\%, seed 42) and 6,574 (67.2\%, seed 123) produce unparseable outputs. Among unparseable outputs, 76.9\% contain no execution keywords whatsoever, while 22.9\% contain ambiguous co-occurring keywords for both pass and fail. Among parseable outputs, \cwm{} achieves only 42.88\% accuracy (seed 42)---below the 50\% random baseline, indicating that even when the model produces well-formed outputs, its predictions are anti-informative. Format compliance varies across repositories: scikit-learn instances yield near-zero unparseable rates, while sphinx instances are 100\% unparseable. This per-repo variation suggests that certain code contexts---likely those with complex execution traces or domain-specific output patterns---prevent the model from generating structured responses.
176	
177	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
178	A natural concern is that strict parsing penalizes \cwm{} unfairly---perhaps many unparseable outputs contain correct predictions in a non-standard format. We test this with relaxed matching that tolerates format deviations across five levels (L0--L4). Counter-intuitively, relaxed matching \emph{decreases} \cwm{} accuracy: from 58.04\% to 56.98\% (seed 42, L4) and from 59.09\% to 55.91\% (seed 123, L4). The mechanism is straightforward: unparseable predictions default to the majority class (pass, 72.96\% base rate), which is more accurate than the model's own parseable predictions (42--53\% accuracy). Recovering these predictions from the majority-class fallback into the model's actual outputs \emph{hurts} performance. The \cls{}--\cwm{} gap widens from 26\pp{} (L0) to 28\pp{} (L4), ruling out the hypothesis that parsing strictness inflates the observed gap. This confirms that \cwm{}'s failure at repository-level complexity is not an artifact of format compliance evaluation but reflects the generation formulation itself.
179	
180	\paragraph{(d) Variance compression.}
181	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and TRAJ (0.97\pp{}) at function level. This is consistent with the bottleneck hypothesis: if \cwm{} performance is capped by output-format constraints, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
182	
183	\paragraph{(e) Per-test precision and recall.}
184	At the per-test level (seed 42), \cls{} achieves fail \fone{} 87.86\% (precision 82.75\%, recall 93.64\%) and pass \fone{} 87.15\%. Of 114 problems, 48 (42.1\%) are perfectly predicted. Performance varies by mutation type: \texttt{return\_value} is easiest (97.3\%) while \texttt{off\_by\_one} is hardest (82.6\%). Multi-F2P instances with 6--10 tests reach 96.3\% accuracy, corroborating the oracle finding that per-test granularity is most valuable with multiple F2P tests.
185	
186	\paragraph{(f) Majority voting.}
187	Majority voting ($K{=}3$) decreases accuracy from 87.51\% to 86.83\% ($-$0.68\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.
188	
189	\paragraph{(g) Block correlation.}
190	Prediction errors within the same problem are correlated: ICC $= 0.191$ ($p < 0.0001$), DEFF $= 3.97$, with 2.81$\times$ more all-correct problems than expected under i.i.d.\ errors. All statistical tests use clustered bootstrap to account for this, and the block-correlated oracle model (\S\ref{sec:oracle-results}) is the more relevant estimate for deployment.
191	
192	\paragraph{(h) LoRA rank sensitivity.}
193	All \cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \cwm{}, we train a rank-32 variant (seed 42), doubling the number of adapter parameters. The rank-32 model achieves 87.0\% accuracy (fail \fone{} 87.1\%, pass \fone{} 86.9\%), compared with 87.51\% for rank-16 under the same seed---a difference of $-$0.51\pp{}, within the 2-seed variance of the rank-16 configuration (0.53\pp{} between seeds 42 and 456). This is consistent with \cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "uuid": "69a4d11e-40fd-4540-8b21-e689c95601ad",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate \\cls{}, \\cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Function-level dataset.}\nWe construct a function-level benchmark from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} by generating mutated variants (five mutation types: \\texttt{wrong\\_operator}, \\texttt{off\\_by\\_one}, \\texttt{boundary\\_error}, \\texttt{return\\_value}, \\texttt{type\\_error}), with labels verified by execution (5s timeout). The dataset contains 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).\n\n\\paragraph{Repo-level dataset.}\nWe construct a repo-level benchmark from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants, extracting per-test instances from repository-scale patches. The dataset contains approximately 70K training samples, with validation ($n{=}9{,}335$) and test ($n{=}9{,}784$) splits having zero problem overlap. The majority baseline (always predict pass) is 72.96\\%. Mutation type composition differs between validation and test due to the non-overlapping problem split; this is a consequence of the design (no data leakage), and val-based checkpoint selection is standard practice~\\cite{jimenez2024swebench}.\n\n\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Our \\cwm{} baseline is a LoRA fine-tuned variant trained for controlled comparison, not a reproduction of the full-scale 32B Code World Model~\\cite{meta2025cwm}. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).\n\n\\paragraph{Oracle analysis and statistics.}\nWe use SWE-bench Verified~\\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\\S\\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\\ trajectory-level comparison uses TOST~\\cite{schuirmann1987tost} with $\\pm$2\\pp{} margin. Within-problem correlation is quantified via the intraclass correlation coefficient~\\cite{shrout1979icc}.\n\n\n\\subsection{Function-Level Results}\n\\label{sec:func_results}\n\nTable~\\ref{tab:main_results} reports function-level results across formulations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Function-level per-test verification results on HumanEval+MBPP test set (1,890 samples). \\cls{}: per-test binary classification; \\cwm{}: execution output generation; TRAJ: trajectory-level scoring; ZS: zero-shot LLM-as-judge. Mean $\\pm$ std over seeds reported where applicable.}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Seeds} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n\\cls{} (fine-tuned) & 4B & 5 & \\textbf{88.43 $\\pm$ 0.78} \\\\\n\\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\\pm$ 0.37 \\\\\nTRAJ (fine-tuned) & 4B & 5 & 86.30 $\\pm$ 0.97 \\\\\n\\midrule\nZS LLM-as-judge & 8B & 1 & 64.40 \\\\\nZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFine-tuned \\cls{} achieves a mean accuracy of 88.43\\% ($\\pm$0.78 across seeds 87.83, 89.52, 87.88, 89.00, 87.94), compared to 87.19\\% ($\\pm$0.37; seeds: 87.51, 87.20, 86.98, 86.67, 87.57) for \\cwm{} and 86.30\\% ($\\pm$0.97; seeds: 85.66, 85.47, 87.40, 87.31, 85.66) for TRAJ. The \\cls{}--\\cwm{} gap is 1.24\\pp{}, which is modest at this complexity level---both formulations operate on short, single-function code with simple return values, where generation is not yet bottlenecked by token budget or string complexity.\n\nZero-shot baselines lag by a wide margin: Qwen3-8B achieves 64.40\\% and Qwen3-32B (NF4) achieves 71.69\\%, both far below fine-tuned 4B models. The 8B zero-shot model exhibits a strong FAIL bias (fail recall 95.8\\%, pass recall 35.1\\%), indicating that zero-shot prompting cannot achieve the balanced precision/recall that fine-tuning produces. Even with 8$\\times$ more parameters, the 32B zero-shot model trails the fine-tuned 4B \\cls{} by 16.74\\pp{}, confirming that task-specific fine-tuning, rather than model scale alone, is necessary for reliable per-test verification.\n\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} compares \\cls{} and \\cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: \\cls{} vs.\\ \\cwm{} accuracy (\\%) at 4B and 8B. Three matched seeds in full precision. The \\cls{}--\\cwm{} gap widens from 1.18\\pp{} to 2.43\\pp{}.}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Mean} & \\textbf{Gap} \\\\\n\\midrule\n\\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \\multirow{2}{*}{1.18} \\\\\n\\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\\\\n\\midrule\n\\cls{} & 8B & \\textbf{90.48} & 89.40 & 88.31 & \\textbf{89.40} & \\multirow{2}{*}{\\textbf{2.43}} \\\\\n\\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 4B, \\cls{} and \\cwm{} are separated by 1.18\\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\\pp{}. Clustered bootstrap analysis yields a mean gap of 2.26\\pp{} ($p = 0.0066$, 95\\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.\n\nThe asymmetry in scaling efficiency is striking: from 4B to 8B, \\cls{} gains +0.99\\pp{} (88.41 $\\to$ 89.40) while \\cwm{} loses $-$0.27\\pp{} (87.23 $\\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \\cwm{} accuracy. However, the \\cwm{} regression ($-$0.27\\pp{}) falls within seed noise (3-seed std ${\\sim}$0.5\\pp{}) and could reflect suboptimal hyperparameter transfer (LoRA rank and learning rate were not re-tuned for 8B) rather than a fundamental bottleneck; disentangling these factors requires larger-scale experiments. We also acknowledge the limited model-level statistical power of three seeds: while the clustered bootstrap provides instance-level confidence (1,890 samples $\\times$ 10K resamples), three model instances cannot fully separate seed variance from systematic scaling effects. Figure~\\ref{fig:scaling_gap} visualizes the diverging trajectories. Whether this divergence amplifies at repository-level complexity is examined in \\S\\ref{sec:repo}.\n\n\n\\subsection{Per-Test vs.\\ Trajectory-Level Equivalence}\n\\label{sec:equivalence}\n\nA natural concern is whether per-test predictions, when aggregated to the variant level, match the accuracy of a model trained directly at that granularity. We address this by comparing \\cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds.\n\nThe pooled gap is $-$0.45\\pp{} (95\\% CI [$-$1.71, +0.84]), with per-seed gaps ranging from $-$1.84 to +1.45\\pp{} (seed 42: $-$0.97; seed 123: +1.45; seed 456: $-$1.84; seed 789: $-$0.78; seed 0: $-$0.29). The TOST equivalence test rejects the null hypothesis of non-equivalence at $p = 0.007$ with a $\\pm$2\\pp{} margin, confirming that per-test classification and trajectory-level scoring achieve statistically equivalent variant-level accuracy.\n\nCritically, however, predictions within the same problem are not independent. The intraclass correlation coefficient is ICC $= 0.191$ ($p < 0.0001$), yielding a design effect DEFF $= 3.97$. This means that naive i.i.d.\\ confidence intervals would be approximately $2\\times$ too narrow. All statistical tests in this paper use clustered bootstrap to account for this within-problem correlation.\n\nThe practical implication is clear: per-test classification provides per-test diagnostic information---which specific tests fail and why---at no cost to variant-level accuracy. A trajectory-level model gives only a binary patch verdict, discarding the per-test signal that downstream repair systems could exploit for targeted re-repair.\n\n\n\\subsection{Accuracy-Utility Frontier}\n\\label{sec:oracle-results}\n\nWhere does per-test granularity actually help? We formalize this via an oracle analysis on SWE-bench Verified, stratifying instances by the number of F2P tests $T$ and comparing per-test vs.\\ trajectory-level oracle resolve rates under both i.i.d.\\ and block-correlated error models (using the empirical ICC $= 0.191$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses empirical ICC $= 0.191$. P2P regression rate: 1.04\\% mean, 0\\% median.}\n\\label{tab:oracle}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$T$} & \\textbf{Inst.\\%} & \\textbf{i.i.d.\\ (\\pp{})} & \\textbf{Block (\\pp{})} & \\textbf{Contrib.\\%} \\\\\n\\midrule\n$1$ & 68.7 & $-$0.04 & $-$0.09 & $\\approx$0 \\\\\n$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\\\\n$3$--$5$ & 7.1 & 25.00 & 40.74 & $\\approx$26 \\\\\n$\\geq 6$ & 5.1 & 30.00 & 40.06 & $\\approx$19 \\\\\n\\midrule\n\\textbf{All} & 100.0 & --- & \\textbf{10.93} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:oracle} reveals a sharp concentration of per-test advantage. When $T = 1$---the dominant case at 68.7\\% of SWE-bench instances---per-test and trajectory-level are informationally equivalent (block advantage $-$0.09\\pp{}), because a single F2P test provides no more signal than a binary patch verdict. The advantage materializes at $T = 2$ (19.1\\% of instances), where block-correlated advantage reaches 31.69\\pp{}, contributing 55.3\\% of the total advantage. Instances with $T \\geq 3$ exhibit block advantages exceeding 40\\pp{} but constitute only 12.2\\% of instances. The overall block-correlated advantage is 10.93\\pp{}, driven almost entirely by the $T \\geq 2$ minority. Figure~\\ref{fig:oracle_stratified} visualizes this distribution.\n\nBlock correlation amplifies the advantage relative to the i.i.d.\\ model: at $T = 2$, the block advantage (31.69\\pp{}) is 1.7$\\times$ the i.i.d.\\ advantage (18.49\\pp{}). This occurs because correlated errors make the per-test classifier more likely to get all tests correct or all wrong for a given problem, increasing the information value of each additional test.\n\n\\paragraph{P2P regression signal.}\nThe P2P regression rate in SWE-bench Verified is low: 1.04\\% mean and 0\\% median---77\\% of incorrect patches break zero P2P tests. This means per-test granularity on the P2P dimension currently provides minimal signal. The practical value of per-test verification concentrates in F2P discrimination, particularly for instances with multiple F2P tests.\n\n\n\\subsection{Repo-Level Results}\n\\label{sec:repo}\n\nTable~\\ref{tab:repo_level} compares \\cls{} and \\cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy (D088 protocol); the test set ($n{=}9{,}784$) has zero problem overlap with validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level per-test verification on SWE-bench Verified test set ($n{=}9{,}784$, val-selected checkpoints). Same-size 4B comparison is primary; \\cls{} 8B included for scaling context; \\cwm{} 8B in progress.}\n\\label{tab:repo_level}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{Seed} & \\textbf{Acc (\\%)} & \\textbf{Macro \\fone{}} & \\textbf{Unparse (\\%)} & \\textbf{vs Maj.\\ (\\pp{})} \\\\\n\\midrule\n\\cls{} & 4B & 42 & \\textbf{83.63} & 75.63 & 0.0 & +10.67 \\\\\n\\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & $-$14.92 \\\\\n\\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & $-$13.87 \\\\\n\\midrule\n\\cls{} & 8B & 42 & 83.52 & 77.50 & 0.0 & +10.56 \\\\\n\\cls{} & 8B & 123 & 85.60 & 78.38 & 0.0 & +12.64 \\\\\n\\cwm{} & 8B & --- & --- & --- & --- & --- \\\\\n\\midrule\nMajority & --- & --- & 72.96 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe same-size 4B comparison reveals a 25.59\\pp{} gap: \\cls{} achieves 83.63\\% accuracy (macro \\fone{} 75.63) versus \\cwm{} at 58.04\\% (macro \\fone{} 51.67) on seed 42. \\cwm{} falls 14.92\\pp{} below the majority baseline (72.96\\%), indicating negative utility---a system that always predicts pass outperforms \\cwm{}. A second \\cwm{} seed (123) yields 59.09\\% with a higher unparseable rate (67.2\\% vs.\\ 53.7\\%), confirming the failure is not seed-specific.\n\nThe primary driver is output format compliance collapse. \\cwm{} produces unparseable outputs for 53.7\\% (seed 42) and 67.2\\% (seed 123) of test instances, while \\cls{} produces zero unparseable outputs across all configurations. The generation budget (1,024 tokens) is sufficient for the outputs required---this is not a token-budget limitation but a failure of the model to produce structured execution predictions when faced with repository-level code complexity. Among parseable \\cwm{} outputs, accuracy is 42--43\\%---below both the majority baseline (72.96\\%) and chance level (50\\%)---indicating that even well-formed \\cwm{} predictions are anti-informative at this complexity level. \\cls{}, producing a single binary token per test, is immune to format compliance failures by construction. Figure~\\ref{fig:scaling_gap} visualizes the gap amplification from function level (1.24\\pp{}) to repo level (25.59\\pp{}).\n\nFor scaling context, we include \\cls{} 8B results (cross-size comparison, not directly comparable to the same-size gap above). \\cls{} 8B achieves 83.52\\% (seed 42) and 85.60\\% (seed 123), yielding cross-size gaps of 25.48\\pp{} and 26.51\\pp{} against \\cwm{} 4B at the corresponding seeds. Within \\cls{}, the 4B$\\to$8B transition at repo level shows 83.63\\% $\\to$ 83.52\\% (seed 42), a difference within noise, suggesting that classification may be approaching a capacity ceiling at repo-level complexity or that checkpoint selection variance dominates at this scale. \\cwm{} 8B training is in progress; if \\cwm{} 8B performs similarly to 4B, this would confirm a generation bottleneck rather than a capacity limitation.\n\n\\paragraph{Sequence length and formulation cost.} Both \\cls{} and \\cwm{} are trained with identical \\texttt{max\\_seq\\_length}$=$2,048, so training-time input context is fully controlled. The asymmetry arises at inference: \\cwm{} reserves \\texttt{max\\_new\\_tokens}$=$1,024 for output generation, leaving an effective input window of ${\\sim}$1,024 tokens; \\cls{} produces a single token and can allocate nearly all context to input (\\texttt{max\\_seq\\_length}$=$5,120 at 4B, 8,192 at 8B during evaluation). This eval-time difference primarily reflects structural properties of each formulation: generation \\emph{must} reserve context for output tokens, while classification need not. A matched-context ablation confirms this: \\cls{} 8B evaluated at \\texttt{max\\_seq\\_length}$=$2,048 achieves 82.83\\%, a reduction of only 0.69\\pp{} from the 8,192-token evaluation (83.52\\%). The matched-context gap (\\cls{}@2,048 vs.\\ \\cwm{}@2,048) is 24.79\\pp{}, accounting for 97\\% of the full 25.59\\pp{} gap---input context disparity explains at most 3\\% of the observed difference. Moreover, input context cannot explain the qualitative failures. Format compliance collapse---53.7--67.2\\% of \\cwm{} outputs are unparseable despite sufficient generation budget---reflects the model's inability to produce structured predictions, not input truncation. Among parseable outputs where the model does produce well-formed predictions, accuracy is 42--43\\%, below chance level (50\\%): if input truncation were the sole issue, parseable outputs should at minimum exceed chance.\n\n\\paragraph{Limitations.} The same-size 4B comparison uses a single seed; \\cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\\% test accuracy (+2.4\\pp{} above majority baseline), indicating that val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The validation and test sets have zero problem overlap but differ in mutation type composition, introducing potential distribution shift. All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences.\n\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{(a) Error complementarity.}\n\\cls{} and \\cwm{} make errors in opposite directions at function level. Among \\cls{} errors (seed 42), 75.5\\% are false negatives (FAIL $\\to$ PASS), meaning the classifier tends to over-predict passing. Among \\cwm{} errors, 83.1\\% are false positives (PASS $\\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\\% accuracy, a 3.12\\pp{} improvement over \\cls{} alone (87.51\\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains.\n\n\\paragraph{(b) CWM error mode breakdown.}\nAt repo level, \\cwm{} output format compliance collapses. Of 9,784 test instances, 5,255 (53.7\\%, seed 42) and 6,574 (67.2\\%, seed 123) produce unparseable outputs. Among unparseable outputs, 76.9\\% contain no execution keywords whatsoever, while 22.9\\% contain ambiguous co-occurring keywords for both pass and fail. Among parseable outputs, \\cwm{} achieves only 42.88\\% accuracy (seed 42)---below the 50\\% random baseline, indicating that even when the model produces well-formed outputs, its predictions are anti-informative. Format compliance varies across repositories: scikit-learn instances yield near-zero unparseable rates, while sphinx instances are 100\\% unparseable. This per-repo variation suggests that certain code contexts---likely those with complex execution traces or domain-specific output patterns---prevent the model from generating structured responses.\n\n\\paragraph{(c) Relaxed matching does not rescue \\cwm{}.}\nA natural concern is that strict parsing penalizes \\cwm{} unfairly---perhaps many unparseable outputs contain correct predictions in a non-standard format. We test this with relaxed matching that tolerates format deviations across five levels (L0--L4). Counter-intuitively, relaxed matching \\emph{decreases} \\cwm{} accuracy: from 58.04\\% to 56.98\\% (seed 42, L4) and from 59.09\\% to 55.91\\% (seed 123, L4). The mechanism is straightforward: unparseable predictions default to the majority class (pass, 72.96\\% base rate), which is more accurate than the model's own parseable predictions (42--53\\% accuracy). Recovering these predictions from the majority-class fallback into the model's actual outputs \\emph{hurts} performance. The \\cls{}--\\cwm{} gap widens from 26\\pp{} (L0) to 28\\pp{} (L4), ruling out the hypothesis that parsing strictness inflates the observed gap. This confirms that \\cwm{}'s failure at repository-level complexity is not an artifact of format compliance evaluation but reflects the generation formulation itself.\n\n\\paragraph{(d) Variance compression.}\n\\cwm{}'s 5-seed standard deviation (0.37\\pp{}) is lower than \\cls{} (0.78\\pp{}) and TRAJ (0.97\\pp{}) at function level. This is consistent with the bottleneck hypothesis: if \\cwm{} performance is capped by output-format constraints, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.\n\n\\paragraph{(e) Per-test precision and recall.}\nAt the per-test level (seed 42), \\cls{} achieves fail \\fone{} 87.86\\% (precision 82.75\\%, recall 93.64\\%) and pass \\fone{} 87.15\\%. Of 114 problems, 48 (42.1\\%) are perfectly predicted. Performance varies by mutation type: \\texttt{return\\_value} is easiest (97.3\\%) while \\texttt{off\\_by\\_one} is hardest (82.6\\%). Multi-F2P instances with 6--10 tests reach 96.3\\% accuracy, corroborating the oracle finding that per-test granularity is most valuable with multiple F2P tests.\n\n\\paragraph{(f) Majority voting.}\nMajority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\n\n\\paragraph{(g) Block correlation.}\nPrediction errors within the same problem are correlated: ICC $= 0.191$ ($p < 0.0001$), DEFF $= 3.97$, with 2.81$\\times$ more all-correct problems than expected under i.i.d.\\ errors. All statistical tests use clustered bootstrap to account for this, and the block-correlated oracle model (\\S\\ref{sec:oracle-results}) is the more relevant estimate for deployment.\n\n\\paragraph{(h) LoRA rank sensitivity.}\nAll \\cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \\cwm{}, we train a rank-32 variant (seed 42), doubling the number of adapter parameters. The rank-32 model achieves 87.0\\% accuracy (fail \\fone{} 87.1\\%, pass \\fone{} 86.9\\%), compared with 87.51\\% for rank-16 under the same seed---a difference of $-$0.51\\pp{}, within the 2-seed variance of the rank-16 configuration (0.53\\pp{} between seeds 42 and 456). This is consistent with \\cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.",
      "numLines": 193,
      "startLine": 1,
      "totalLines": 193
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Grep · `toolu_013V6SKccXdASNGyEYu6wNkX`</summary>

```json
{
  "pattern": "2\\{\\\\times\\}10\\^\\{-5\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "uuid": "5f62722b-4328-48f9-bce4-e59ca7fa0d5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015aVxSS5HeVMSc7xY1sc7HQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7668,
      "cache_read_input_tokens": 23095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7668
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T15:00:21.007Z_

<details><summary>↩ Tool result · `toolu_013V6SKccXdASNGyEYu6wNkX`</summary>

```text
16:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "uuid": "21f7371c-1985-4e8b-b2e8-8d3bd3d35dbc",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "16:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 9_

第16行有唯一一处 `$2{\times}10^{-5}$`，在 "Models and training" 段落中。需要将其改为区分两个级别的 lr。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "uuid": "7d942216-1152-4674-a380-2418396b2d6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQEqMJvpczqUfXN4cuNGph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 30763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Edit · `toolu_01AuYAG9HKtZHQ4AXgq4Y8aJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "old_string": "LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-5}$, 3 epochs)",
  "new_string": "LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-4}$ function-level / $5{\\times}10^{-5}$ repo-level, 3 epochs)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "uuid": "ed62e45d-7ec3-4753-9c98-aa3ab1198765",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQEqMJvpczqUfXN4cuNGph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 30763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T15:00:27.296Z_

<details><summary>↩ Tool result · `toolu_01AuYAG9HKtZHQ4AXgq4Y8aJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "uuid": "557deb4c-a926-4a1b-a961-09ede393e5f3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "oldString": "LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-5}$, 3 epochs)",
    "newString": "LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-4}$ function-level / $5{\\times}10^{-5}$ repo-level, 3 epochs)",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate \\cls{}, \\cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Function-level dataset.}\nWe construct a function-level benchmark from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} by generating mutated variants (five mutation types: \\texttt{wrong\\_operator}, \\texttt{off\\_by\\_one}, \\texttt{boundary\\_error}, \\texttt{return\\_value}, \\texttt{type\\_error}), with labels verified by execution (5s timeout). The dataset contains 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).\n\n\\paragraph{Repo-level dataset.}\nWe construct a repo-level benchmark from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants, extracting per-test instances from repository-scale patches. The dataset contains approximately 70K training samples, with validation ($n{=}9{,}335$) and test ($n{=}9{,}784$) splits having zero problem overlap. The majority baseline (always predict pass) is 72.96\\%. Mutation type composition differs between validation and test due to the non-overlapping problem split; this is a consequence of the design (no data leakage), and val-based checkpoint selection is standard practice~\\cite{jimenez2024swebench}.\n\n\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Our \\cwm{} baseline is a LoRA fine-tuned variant trained for controlled comparison, not a reproduction of the full-scale 32B Code World Model~\\cite{meta2025cwm}. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).\n\n\\paragraph{Oracle analysis and statistics.}\nWe use SWE-bench Verified~\\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\\S\\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\\ trajectory-level comparison uses TOST~\\cite{schuirmann1987tost} with $\\pm$2\\pp{} margin. Within-problem correlation is quantified via the intraclass correlation coefficient~\\cite{shrout1979icc}.\n\n\n\\subsection{Function-Level Results}\n\\label{sec:func_results}\n\nTable~\\ref{tab:main_results} reports function-level results across formulations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Function-level per-test verification results on HumanEval+MBPP test set (1,890 samples). \\cls{}: per-test binary classification; \\cwm{}: execution output generation; TRAJ: trajectory-level scoring; ZS: zero-shot LLM-as-judge. Mean $\\pm$ std over seeds reported where applicable.}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Seeds} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n\\cls{} (fine-tuned) & 4B & 5 & \\textbf{88.43 $\\pm$ 0.78} \\\\\n\\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\\pm$ 0.37 \\\\\nTRAJ (fine-tuned) & 4B & 5 & 86.30 $\\pm$ 0.97 \\\\\n\\midrule\nZS LLM-as-judge & 8B & 1 & 64.40 \\\\\nZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFine-tuned \\cls{} achieves a mean accuracy of 88.43\\% ($\\pm$0.78 across seeds 87.83, 89.52, 87.88, 89.00, 87.94), compared to 87.19\\% ($\\pm$0.37; seeds: 87.51, 87.20, 86.98, 86.67, 87.57) for \\cwm{} and 86.30\\% ($\\pm$0.97; seeds: 85.66, 85.47, 87.40, 87.31, 85.66) for TRAJ. The \\cls{}--\\cwm{} gap is 1.24\\pp{}, which is modest at this complexity level---both formulations operate on short, single-function code with simple return values, where generation is not yet bottlenecked by token budget or string complexity.\n\nZero-shot baselines lag by a wide margin: Qwen3-8B achieves 64.40\\% and Qwen3-32B (NF4) achieves 71.69\\%, both far below fine-tuned 4B models. The 8B zero-shot model exhibits a strong FAIL bias (fail recall 95.8\\%, pass recall 35.1\\%), indicating that zero-shot prompting cannot achieve the balanced precision/recall that fine-tuning produces. Even with 8$\\times$ more parameters, the 32B zero-shot model trails the fine-tuned 4B \\cls{} by 16.74\\pp{}, confirming that task-specific fine-tuning, rather than model scale alone, is necessary for reliable per-test verification.\n\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} compares \\cls{} and \\cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: \\cls{} vs.\\ \\cwm{} accuracy (\\%) at 4B and 8B. Three matched seeds in full precision. The \\cls{}--\\cwm{} gap widens from 1.18\\pp{} to 2.43\\pp{}.}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Mean} & \\textbf{Gap} \\\\\n\\midrule\n\\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \\multirow{2}{*}{1.18} \\\\\n\\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\\\\n\\midrule\n\\cls{} & 8B & \\textbf{90.48} & 89.40 & 88.31 & \\textbf{89.40} & \\multirow{2}{*}{\\textbf{2.43}} \\\\\n\\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 4B, \\cls{} and \\cwm{} are separated by 1.18\\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\\pp{}. Clustered bootstrap analysis yields a mean gap of 2.26\\pp{} ($p = 0.0066$, 95\\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.\n\nThe asymmetry in scaling efficiency is striking: from 4B to 8B, \\cls{} gains +0.99\\pp{} (88.41 $\\to$ 89.40) while \\cwm{} loses $-$0.27\\pp{} (87.23 $\\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \\cwm{} accuracy. However, the \\cwm{} regression ($-$0.27\\pp{}) falls within seed noise (3-seed std ${\\sim}$0.5\\pp{}) and could reflect suboptimal hyperparameter transfer (LoRA rank and learning rate were not re-tuned for 8B) rather than a fundamental bottleneck; disentangling these factors requires larger-scale experiments. We also acknowledge the limited model-level statistical power of three seeds: while the clustered bootstrap provides instance-level confidence (1,890 samples $\\times$ 10K resamples), three model instances cannot fully separate seed variance from systematic scaling effects. Figure~\\ref{fig:scaling_gap} visualizes the diverging trajectories. Whether this divergence amplifies at repository-level complexity is examined in \\S\\ref{sec:repo}.\n\n\n\\subsection{Per-Test vs.\\ Trajectory-Level Equivalence}\n\\label{sec:equivalence}\n\nA natural concern is whether per-test predictions, when aggregated to the variant level, match the accuracy of a model trained directly at that granularity. We address this by comparing \\cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds.\n\nThe pooled gap is $-$0.45\\pp{} (95\\% CI [$-$1.71, +0.84]), with per-seed gaps ranging from $-$1.84 to +1.45\\pp{} (seed 42: $-$0.97; seed 123: +1.45; seed 456: $-$1.84; seed 789: $-$0.78; seed 0: $-$0.29). The TOST equivalence test rejects the null hypothesis of non-equivalence at $p = 0.007$ with a $\\pm$2\\pp{} margin, confirming that per-test classification and trajectory-level scoring achieve statistically equivalent variant-level accuracy.\n\nCritically, however, predictions within the same problem are not independent. The intraclass correlation coefficient is ICC $= 0.191$ ($p < 0.0001$), yielding a design effect DEFF $= 3.97$. This means that naive i.i.d.\\ confidence intervals would be approximately $2\\times$ too narrow. All statistical tests in this paper use clustered bootstrap to account for this within-problem correlation.\n\nThe practical implication is clear: per-test classification provides per-test diagnostic information---which specific tests fail and why---at no cost to variant-level accuracy. A trajectory-level model gives only a binary patch verdict, discarding the per-test signal that downstream repair systems could exploit for targeted re-repair.\n\n\n\\subsection{Accuracy-Utility Frontier}\n\\label{sec:oracle-results}\n\nWhere does per-test granularity actually help? We formalize this via an oracle analysis on SWE-bench Verified, stratifying instances by the number of F2P tests $T$ and comparing per-test vs.\\ trajectory-level oracle resolve rates under both i.i.d.\\ and block-correlated error models (using the empirical ICC $= 0.191$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses empirical ICC $= 0.191$. P2P regression rate: 1.04\\% mean, 0\\% median.}\n\\label{tab:oracle}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$T$} & \\textbf{Inst.\\%} & \\textbf{i.i.d.\\ (\\pp{})} & \\textbf{Block (\\pp{})} & \\textbf{Contrib.\\%} \\\\\n\\midrule\n$1$ & 68.7 & $-$0.04 & $-$0.09 & $\\approx$0 \\\\\n$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\\\\n$3$--$5$ & 7.1 & 25.00 & 40.74 & $\\approx$26 \\\\\n$\\geq 6$ & 5.1 & 30.00 & 40.06 & $\\approx$19 \\\\\n\\midrule\n\\textbf{All} & 100.0 & --- & \\textbf{10.93} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:oracle} reveals a sharp concentration of per-test advantage. When $T = 1$---the dominant case at 68.7\\% of SWE-bench instances---per-test and trajectory-level are informationally equivalent (block advantage $-$0.09\\pp{}), because a single F2P test provides no more signal than a binary patch verdict. The advantage materializes at $T = 2$ (19.1\\% of instances), where block-correlated advantage reaches 31.69\\pp{}, contributing 55.3\\% of the total advantage. Instances with $T \\geq 3$ exhibit block advantages exceeding 40\\pp{} but constitute only 12.2\\% of instances. The overall block-correlated advantage is 10.93\\pp{}, driven almost entirely by the $T \\geq 2$ minority. Figure~\\ref{fig:oracle_stratified} visualizes this distribution.\n\nBlock correlation amplifies the advantage relative to the i.i.d.\\ model: at $T = 2$, the block advantage (31.69\\pp{}) is 1.7$\\times$ the i.i.d.\\ advantage (18.49\\pp{}). This occurs because correlated errors make the per-test classifier more likely to get all tests correct or all wrong for a given problem, increasing the information value of each additional test.\n\n\\paragraph{P2P regression signal.}\nThe P2P regression rate in SWE-bench Verified is low: 1.04\\% mean and 0\\% median---77\\% of incorrect patches break zero P2P tests. This means per-test granularity on the P2P dimension currently provides minimal signal. The practical value of per-test verification concentrates in F2P discrimination, particularly for instances with multiple F2P tests.\n\n\n\\subsection{Repo-Level Results}\n\\label{sec:repo}\n\nTable~\\ref{tab:repo_level} compares \\cls{} and \\cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy (D088 protocol); the test set ($n{=}9{,}784$) has zero problem overlap with validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level per-test verification on SWE-bench Verified test set ($n{=}9{,}784$, val-selected checkpoints). Same-size 4B comparison is primary; \\cls{} 8B included for scaling context; \\cwm{} 8B in progress.}\n\\label{tab:repo_level}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{Seed} & \\textbf{Acc (\\%)} & \\textbf{Macro \\fone{}} & \\textbf{Unparse (\\%)} & \\textbf{vs Maj.\\ (\\pp{})} \\\\\n\\midrule\n\\cls{} & 4B & 42 & \\textbf{83.63} & 75.63 & 0.0 & +10.67 \\\\\n\\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & $-$14.92 \\\\\n\\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & $-$13.87 \\\\\n\\midrule\n\\cls{} & 8B & 42 & 83.52 & 77.50 & 0.0 & +10.56 \\\\\n\\cls{} & 8B & 123 & 85.60 & 78.38 & 0.0 & +12.64 \\\\\n\\cwm{} & 8B & --- & --- & --- & --- & --- \\\\\n\\midrule\nMajority & --- & --- & 72.96 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe same-size 4B comparison reveals a 25.59\\pp{} gap: \\cls{} achieves 83.63\\% accuracy (macro \\fone{} 75.63) versus \\cwm{} at 58.04\\% (macro \\fone{} 51.67) on seed 42. \\cwm{} falls 14.92\\pp{} below the majority baseline (72.96\\%), indicating negative utility---a system that always predicts pass outperforms \\cwm{}. A second \\cwm{} seed (123) yields 59.09\\% with a higher unparseable rate (67.2\\% vs.\\ 53.7\\%), confirming the failure is not seed-specific.\n\nThe primary driver is output format compliance collapse. \\cwm{} produces unparseable outputs for 53.7\\% (seed 42) and 67.2\\% (seed 123) of test instances, while \\cls{} produces zero unparseable outputs across all configurations. The generation budget (1,024 tokens) is sufficient for the outputs required---this is not a token-budget limitation but a failure of the model to produce structured execution predictions when faced with repository-level code complexity. Among parseable \\cwm{} outputs, accuracy is 42--43\\%---below both the majority baseline (72.96\\%) and chance level (50\\%)---indicating that even well-formed \\cwm{} predictions are anti-informative at this complexity level. \\cls{}, producing a single binary token per test, is immune to format compliance failures by construction. Figure~\\ref{fig:scaling_gap} visualizes the gap amplification from function level (1.24\\pp{}) to repo level (25.59\\pp{}).\n\nFor scaling context, we include \\cls{} 8B results (cross-size comparison, not directly comparable to the same-size gap above). \\cls{} 8B achieves 83.52\\% (seed 42) and 85.60\\% (seed 123), yielding cross-size gaps of 25.48\\pp{} and 26.51\\pp{} against \\cwm{} 4B at the corresponding seeds. Within \\cls{}, the 4B$\\to$8B transition at repo level shows 83.63\\% $\\to$ 83.52\\% (seed 42), a difference within noise, suggesting that classification may be approaching a capacity ceiling at repo-level complexity or that checkpoint selection variance dominates at this scale. \\cwm{} 8B training is in progress; if \\cwm{} 8B performs similarly to 4B, this would confirm a generation bottleneck rather than a capacity limitation.\n\n\\paragraph{Sequence length and formulation cost.} Both \\cls{} and \\cwm{} are trained with identical \\texttt{max\\_seq\\_length}$=$2,048, so training-time input context is fully controlled. The asymmetry arises at inference: \\cwm{} reserves \\texttt{max\\_new\\_tokens}$=$1,024 for output generation, leaving an effective input window of ${\\sim}$1,024 tokens; \\cls{} produces a single token and can allocate nearly all context to input (\\texttt{max\\_seq\\_length}$=$5,120 at 4B, 8,192 at 8B during evaluation). This eval-time difference primarily reflects structural properties of each formulation: generation \\emph{must} reserve context for output tokens, while classification need not. A matched-context ablation confirms this: \\cls{} 8B evaluated at \\texttt{max\\_seq\\_length}$=$2,048 achieves 82.83\\%, a reduction of only 0.69\\pp{} from the 8,192-token evaluation (83.52\\%). The matched-context gap (\\cls{}@2,048 vs.\\ \\cwm{}@2,048) is 24.79\\pp{}, accounting for 97\\% of the full 25.59\\pp{} gap---input context disparity explains at most 3\\% of the observed difference. Moreover, input context cannot explain the qualitative failures. Format compliance collapse---53.7--67.2\\% of \\cwm{} outputs are unparseable despite sufficient generation budget---reflects the model's inability to produce structured predictions, not input truncation. Among parseable outputs where the model does produce well-formed predictions, accuracy is 42--43\\%, below chance level (50\\%): if input truncation were the sole issue, parseable outputs should at minimum exceed chance.\n\n\\paragraph{Limitations.} The same-size 4B comparison uses a single seed; \\cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\\% test accuracy (+2.4\\pp{} above majority baseline), indicating that val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The validation and test sets have zero problem overlap but differ in mutation type composition, introducing potential distribution shift. All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences.\n\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{(a) Error complementarity.}\n\\cls{} and \\cwm{} make errors in opposite directions at function level. Among \\cls{} errors (seed 42), 75.5\\% are false negatives (FAIL $\\to$ PASS), meaning the classifier tends to over-predict passing. Among \\cwm{} errors, 83.1\\% are false positives (PASS $\\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\\% accuracy, a 3.12\\pp{} improvement over \\cls{} alone (87.51\\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains.\n\n\\paragraph{(b) CWM error mode breakdown.}\nAt repo level, \\cwm{} output format compliance collapses. Of 9,784 test instances, 5,255 (53.7\\%, seed 42) and 6,574 (67.2\\%, seed 123) produce unparseable outputs. Among unparseable outputs, 76.9\\% contain no execution keywords whatsoever, while 22.9\\% contain ambiguous co-occurring keywords for both pass and fail. Among parseable outputs, \\cwm{} achieves only 42.88\\% accuracy (seed 42)---below the 50\\% random baseline, indicating that even when the model produces well-formed outputs, its predictions are anti-informative. Format compliance varies across repositories: scikit-learn instances yield near-zero unparseable rates, while sphinx instances are 100\\% unparseable. This per-repo variation suggests that certain code contexts---likely those with complex execution traces or domain-specific output patterns---prevent the model from generating structured responses.\n\n\\paragraph{(c) Relaxed matching does not rescue \\cwm{}.}\nA natural concern is that strict parsing penalizes \\cwm{} unfairly---perhaps many unparseable outputs contain correct predictions in a non-standard format. We test this with relaxed matching that tolerates format deviations across five levels (L0--L4). Counter-intuitively, relaxed matching \\emph{decreases} \\cwm{} accuracy: from 58.04\\% to 56.98\\% (seed 42, L4) and from 59.09\\% to 55.91\\% (seed 123, L4). The mechanism is straightforward: unparseable predictions default to the majority class (pass, 72.96\\% base rate), which is more accurate than the model's own parseable predictions (42--53\\% accuracy). Recovering these predictions from the majority-class fallback into the model's actual outputs \\emph{hurts} performance. The \\cls{}--\\cwm{} gap widens from 26\\pp{} (L0) to 28\\pp{} (L4), ruling out the hypothesis that parsing strictness inflates the observed gap. This confirms that \\cwm{}'s failure at repository-level complexity is not an artifact of format compliance evaluation but reflects the generation formulation itself.\n\n\\paragraph{(d) Variance compression.}\n\\cwm{}'s 5-seed standard deviation (0.37\\pp{}) is lower than \\cls{} (0.78\\pp{}) and TRAJ (0.97\\pp{}) at function level. This is consistent with the bottleneck hypothesis: if \\cwm{} performance is capped by output-format constraints, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.\n\n\\paragraph{(e) Per-test precision and recall.}\nAt the per-test level (seed 42), \\cls{} achieves fail \\fone{} 87.86\\% (precision 82.75\\%, recall 93.64\\%) and pass \\fone{} 87.15\\%. Of 114 problems, 48 (42.1\\%) are perfectly predicted. Performance varies by mutation type: \\texttt{return\\_value} is easiest (97.3\\%) while \\texttt{off\\_by\\_one} is hardest (82.6\\%). Multi-F2P instances with 6--10 tests reach 96.3\\% accuracy, corroborating the oracle finding that per-test granularity is most valuable with multiple F2P tests.\n\n\\paragraph{(f) Majority voting.}\nMajority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\n\n\\paragraph{(g) Block correlation.}\nPrediction errors within the same problem are correlated: ICC $= 0.191$ ($p < 0.0001$), DEFF $= 3.97$, with 2.81$\\times$ more all-correct problems than expected under i.i.d.\\ errors. All statistical tests use clustered bootstrap to account for this, and the block-correlated oracle model (\\S\\ref{sec:oracle-results}) is the more relevant estimate for deployment.\n\n\\paragraph{(h) LoRA rank sensitivity.}\nAll \\cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \\cwm{}, we train a rank-32 variant (seed 42), doubling the number of adapter parameters. The rank-32 model achieves 87.0\\% accuracy (fail \\fone{} 87.1\\%, pass \\fone{} 86.9\\%), compared with 87.51\\% for rank-16 under the same seed---a difference of $-$0.51\\pp{}, within the 2-seed variance of the rank-16 configuration (0.53\\pp{} between seeds 42 and 456). This is consistent with \\cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 7,
        "newStart": 13,
        "newLines": 7,
        "lines": [
          " We construct a repo-level benchmark from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants, extracting per-test instances from repository-scale patches. The dataset contains approximately 70K training samples, with validation ($n{=}9{,}335$) and test ($n{=}9{,}784$) splits having zero problem overlap. The majority baseline (always predict pass) is 72.96\\%. Mutation type composition differs between validation and test due to the non-overlapping problem split; this is a consequence of the design (no data leakage), and val-based checkpoint selection is standard practice~\\cite{jimenez2024swebench}.",
          " ",
          " \\paragraph{Models and training.}",
          "-We fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Our \\cwm{} baseline is a LoRA fine-tuned variant trained for controlled comparison, not a reproduction of the full-scale 32B Code World Model~\\cite{meta2025cwm}. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).",
          "+We fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-4}$ function-level / $5{\\times}10^{-5}$ repo-level, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Our \\cwm{} baseline is a LoRA fine-tuned variant trained for controlled comparison, not a reproduction of the full-scale 32B Code World Model~\\cite{meta2025cwm}. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).",
          " ",
          " \\paragraph{Oracle analysis and statistics.}",
          " We use SWE-bench Verified~\\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\\S\\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\\ trajectory-level comparison uses TOST~\\cite{schuirmann1987tost} with $\\pm$2\\pp{} margin. Within-problem correlation is quantified via the intraclass correlation coefficient~\\cite{shrout1979icc}."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01F1pbXoGABbNpheZBYwTNDX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "offset": 15,
  "limit": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "uuid": "9f21cc32-37af-4745-88ae-b2c628f02919",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNAA2dDfkk7t6ttt32viSS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 346,
      "cache_read_input_tokens": 30922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 346
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T15:00:30.402Z_

<details><summary>↩ Tool result · `toolu_01F1pbXoGABbNpheZBYwTNDX`</summary>

```text
15	\paragraph{Models and training.}
16	We fine-tune Qwen3-4B and Qwen3-8B~\cite{yang2024qwen25} with LoRA~\cite{hu2022lora} (rank 16, lr $2{\times}10^{-4}$ function-level / $5{\times}10^{-5}$ repo-level, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Our \cwm{} baseline is a LoRA fine-tuned variant trained for controlled comparison, not a reproduction of the full-scale 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "uuid": "a360cda6-2e5a-45f2-aee4-917e7b39ee73",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
      "content": "\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-4}$ function-level / $5{\\times}10^{-5}$ repo-level, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Our \\cwm{} baseline is a LoRA fine-tuned variant trained for controlled comparison, not a reproduction of the full-scale 32B Code World Model~\\cite{meta2025cwm}. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).",
      "numLines": 2,
      "startLine": 15,
      "totalLines": 193
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

改动正确。文件中无其他 `$2{\times}10^{-5}$` 出现，修复完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "uuid": "b7c86979-27ac-4a3a-92e1-c0413e5800e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016omRm2sv1GGo5zpBPtKD7A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 419,
      "cache_read_input_tokens": 31268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 419
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 15_

改动正确。文件中无其他 `$2{\times}10^{-5}$` 出现，修复完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 21357,
  "duration_api_ms": 22979,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "ea813b9e-fde7-446c-bd59-44687d32ac16",
  "total_cost_usd": 0.20882650000000003,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 20240,
    "cache_read_input_tokens": 127495,
    "output_tokens": 695,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 20240,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 38,
        "cache_read_input_tokens": 31268,
        "cache_creation_input_tokens": 419,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 419
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1094,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001174,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 695,
      "cacheReadInputTokens": 127495,
      "cacheCreationInputTokens": 20240,
      "webSearchRequests": 0,
      "costUSD": 0.20765250000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8ea43fac-30c2-4f01-90c3-2883349cfc68"
}
```

</details>

---
