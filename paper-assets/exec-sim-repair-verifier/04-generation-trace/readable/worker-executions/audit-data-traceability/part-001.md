# audit data traceability — Part 1 of 2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Worker execution logs

[Transcript overview](../audit-data-traceability.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/e6/e6712637b0bce6633a8f.json)

## Before a recorded user message

## Before a recorded user message

114 recorded events


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
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "06672482-3e57-4b6e-9b22-ef984d962723",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/memory/"
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
    "resetsAt": 1779581400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e4ccd11d-c91c-4e78-94aa-222ffe998a28",
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
This is a comprehensive data audit task for a paper submission. I need to systematically check all numbers in the paper against their source data. Let me start by reading the tex files and registry data in parallel.

Let me plan the approach:
1. Read all .tex files to extract numbers
2. Read registry to get experiment data
3. Read relevant artifacts for statistical results
4. Cross-reference everything

I'll start by reading the key files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "b6a5967b-4879-4060-bf2a-9b7f2461a274",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Km93WjotU3nDqKb6QngQ7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14571,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14571
      },
      "output_tokens": 19,
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


### Assistant

_source line 5_

Starting the full data audit. I'll read the tex files and registry in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "7af8cd22-7288-40c7-a993-41e41360e18f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Km93WjotU3nDqKb6QngQ7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14571,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14571
      },
      "output_tokens": 19,
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01L2KEDyxhBLBYXKDnDNay7X`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "934d397d-ca93-42ef-a6cf-1558ed5d92f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Km93WjotU3nDqKb6QngQ7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14571,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14571
      },
      "output_tokens": 19,
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

_source line 7 · 2026-05-23T19:16:45.367Z_

<details><summary>↩ Tool result · `toolu_01L2KEDyxhBLBYXKDnDNay7X`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "76307611-cc9b-4f5c-aca9-ecc0f2fb3752",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Ni76QPFss5azzejnmcK3uF`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "29f52515-ab4f-48e5-9df5-ec3697983bf4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVTBykmq9zNh5u5794g9f1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 26412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 576
      },
      "output_tokens": 52,
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

_source line 9 · 2026-05-23T19:16:47.748Z_

<details><summary>↩ Tool result · `toolu_01Ni76QPFss5azzejnmcK3uF`</summary>

```text
1	\begin{abstract}
2	LLM-based repair generates candidate patches, selecting the best via a verifier. Three execution-free alternatives to expensive execution-based verification have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level scoring (\traj{}). No prior work compares \cls{} and \cwm{} under matched conditions; the \traj{} comparison is inherently confounded.
3	
4	We present the first systematic comparison across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} equivalence is inconclusive after multiple comparison correction at current power (${\sim}$0.3), but the gap narrows from 3.11\pp{} (4B) to 1.07\pp{} (14B). At repository level, this equivalence diverges sharply (DeepSeek-Coder): the \cls{}--\cwm{} gap widens to 18--26\pp{} across 2--3 seeds under our ${\leq}$8B LoRA protocol, accompanied by format collapse. Preliminary 14B results (3 seeds, single family) suggest the gap may narrow at larger scale.
5	
6	Error complementarity and a failure mode taxonomy motivate complexity-aware routing, though simple heuristics capture $<$0.4\pp{} of oracle advantage.
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "80e4c09f-271e-4e93-a076-dfb8ac7019a9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nLLM-based repair generates candidate patches, selecting the best via a verifier. Three execution-free alternatives to expensive execution-based verification have emerged: per-test binary classification (\\cls{}), execution output generation (\\cwm{}), and trajectory-level scoring (\\traj{}). No prior work compares \\cls{} and \\cwm{} under matched conditions; the \\traj{} comparison is inherently confounded.\n\nWe present the first systematic comparison across two code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\\leq}$8B LoRA fine-tuning. At function level, \\cls{} and \\cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \\traj{} equivalence is inconclusive after multiple comparison correction at current power (${\\sim}$0.3), but the gap narrows from 3.11\\pp{} (4B) to 1.07\\pp{} (14B). At repository level, this equivalence diverges sharply (DeepSeek-Coder): the \\cls{}--\\cwm{} gap widens to 18--26\\pp{} across 2--3 seeds under our ${\\leq}$8B LoRA protocol, accompanied by format collapse. Preliminary 14B results (3 seeds, single family) suggest the gap may narrow at larger scale.\n\nError complementarity and a failure mode taxonomy motivate complexity-aware routing, though simple heuristics capture $<$0.4\\pp{} of oracle advantage.\n\\end{abstract}\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01VUzNLvrERBHtGQXswCqB7S`</summary>

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
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "d934de1f-96ae-4787-b4ce-1e3a940f4c7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVTBykmq9zNh5u5794g9f1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 26412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 576
      },
      "output_tokens": 52,
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

_source line 11 · 2026-05-23T19:16:48.713Z_

<details><summary>↩ Tool result · `toolu_01VUzNLvrERBHtGQXswCqB7S`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench}; runs with NaN validation loss (due to truncated targets exceeding 2,048-token limits) default to the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Qwen3 \cwm{} runs show early overfitting (best at ${\sim}$6\% of training); checkpoint details in Appendix~\ref{app:hyperparams}.
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model~\cite{meta2025cwm}. \traj{} uses variant-level rather than per-test labels (8,052 vs.\ 15,290 training instances, but covering $2.24\times$ more unique code variants); the comparison is confounded by both label granularity and data composition (\S\ref{sec:repo}). Repo-level models use val-selected checkpoints where available; runs with NaN validation loss use the final epoch checkpoint (Appendix~\ref{app:hyperparams}). Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Full hyperparameter details appear in Appendix~\ref{app:hyperparams}.
15	
16	\paragraph{Statistics.}
17	TOST equivalence testing is our primary inferential framework for function-level claims; clustered bootstrap provides confidence intervals, Bayesian ROPE serves as a robustness check, and mixed-effects regression tests the formulation$\times$complexity interaction. Confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples; we resample entire problems, not individual tests, to preserve within-problem correlations). Equivalence uses Two One-Sided Tests (TOST)~\cite{schuirmann1987tost} with $\pm$2 percentage point (\pp{}) margin; for function-level TOST, we use seed-level paired analysis (df${=}$4 for 5-seed comparisons, df${=}$2 for 3-seed), treating each training seed as the unit of replication. This is more conservative than problem-level clustered bootstrap, which pools within-seed observations and may understate between-seed uncertainty. Holm-Bonferroni correction~\cite{holm1979} controls family-wise error rate across the five primary comparisons (Table~\ref{tab:holm}). Intraclass correlation coefficient (ICC)~\cite{shrout1979icc} quantifies within-problem correlation. Variant-level effect sizes and statistical power analysis are reported in Appendix~\ref{app:power}. Oracle analysis uses SWE-bench Verified (500 instances).
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
28	\caption{Function-level per-test accuracy on HumanEval+MBPP ($n{=}1{,}890$). Mean $\pm$ std over 5 seeds (Qwen3) or 2 seeds (DeepSeek). Seeds 42/123/456: bfloat16; 789/0: NF4. DeepSeek: $n{=}2$ seeds; std reported for descriptive comparison, not inferential. \traj{}\textsuperscript{$\star$} evaluated on 1,032-sample subset (447 matched variants). All prompting baselines use NF4 4-bit quantization. \textsuperscript{$\star$}Training configuration differs (\S\ref{sec:repo}).}
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
39	\traj{}\textsuperscript{$\star$} (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
40	\midrule
41	\multicolumn{4}{l}{\emph{DeepSeek-Coder (cross-model consistency check)}} \\
42	\cls{} (fine-tuned) & 6.7B & 2 & \textbf{86.85 $\pm$ 0.11} \\
43	\cwm{} (fine-tuned) & 6.7B & 2 & \underline{86.83 $\pm$ 1.49} \\
44	\traj{}\textsuperscript{$\star$} (fine-tuned) & 6.7B & 2 & 84.16 $\pm$ 1.30 \\
45	\midrule
46	\multicolumn{4}{l}{\emph{Prompting baselines}} \\
47	0-shot & 8B (Qwen3) & 1 & 60.53 \\
48	0-shot & 14B (Qwen3) & 1 & 66.24 \\
49	0-shot & 6.7B (DeepSeek) & 1 & 63.00 \\
50	ZS LLM-as-judge & 8B (Qwen3) & 1 & 64.40 \\
51	ZS LLM-as-judge & 6.7B (DeepSeek) & 1 & 56.56 \\
52	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
53	3-shot ICL & 8B (Qwen3) & 1 & 60.42 \\
54	3-shot ICL & 14B (Qwen3) & 1 & 73.12 \\
55	3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\
56	\midrule
57	Majority (pass) & --- & --- & 51.75 \\
58	\bottomrule
59	\end{tabular}}
60	\end{table}
61	
62	All three formulations achieve comparable accuracy on Qwen3-4B: \cls{} 88.43\% ($\pm$0.78), \cwm{} 87.19\% ($\pm$0.37), \traj{} 86.30\% ($\pm$0.97). DeepSeek-Coder-6.7B shows: \cls{} 86.85\%, \cwm{} 86.83\%, \traj{} 84.16\%. The \cls{}--\cwm{} gap (0.02--1.24\pp{}) is within seed noise in both families. However, the \cls{}--\traj{} gap is model-dependent: $<$1\pp{} on Qwen3 but 2.69\pp{} on DeepSeek-Coder, exceeding the $\pm$2\pp{} equivalence margin (\S\ref{sec:equivalence}). \cls{} and \cwm{} are robustly equivalent; \traj{} parity is model-contingent. Zero-shot baselines (Tables~\ref{tab:main_results} and~\ref{tab:repo_level}) establish that repo-level verification requires fine-tuning (0-shot$\to$fine-tuned gains of 35--36\pp{}) and that formulation choice matters only at repo level (\cls{} outperforms \cwm{} by 18--26\pp{}).
63	
64	
65	\subsection{Scaling Behavior}
66	\label{sec:scaling}
67	
68	Beyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\ref{tab:scaling} compares all three formulations at 4B, 8B, and 14B. The 4B and 8B rows use seeds 42 and 123; the 14B row uses seeds 42, 123, and 456. All rows use bfloat16 inference.
69	
70	\begin{table}[t]
71	\centering
72	\small
73	\caption{Model-size scaling: accuracy (\%) at 4B, 8B, and 14B (Qwen3). Seeds 42/123 (4B/8B), seeds 42/123/456 (14B). All bfloat16 inference. $\Delta$: change from previous size. \cwm{} and \traj{}\textsuperscript{$\star$} use $n{=}2$ seeds (4B/8B) and $n{=}3$ seeds (14B). \traj{}\textsuperscript{$\star$} evaluated on 1{,}032-sample subset; \cls{}/\cwm{} use the full 1{,}890-sample set. \textsuperscript{$\star$}Training configuration differs (\S\ref{sec:repo}).}
74	\label{tab:scaling}
75	\setlength{\tabcolsep}{3.5pt}
76	\begin{tabular}{llccccc}
77	\toprule
78	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{s456} & \textbf{Mean} & \textbf{$\Delta$} \\
79	\midrule
80	\multirow{3}{*}{\cls{}} & 4B & 87.83 & 89.52 & --- & \textbf{88.68} & --- \\
81	 & 8B & \textbf{90.48} & 89.40 & --- & \textbf{89.94} & +1.27 \\
82	 & 14B & 89.21 & \textbf{90.79} & 89.79 & \textbf{89.93 $\pm$ 0.80} & $-$0.01 \\
83	\midrule
84	\multirow{3}{*}{\cwm{}} & 4B & 87.51 & 87.20 & --- & \underline{87.36} & --- \\
85	 & 8B & 87.67 & 86.98 & --- & 87.33 & $-$0.03 \\
86	 & 14B & 89.26 & 88.99 & 90.26 & \underline{89.50 $\pm$ 0.67} & +2.17 \\
87	\midrule
88	\multirow{3}{*}{\traj{}} & 4B & 85.66 & 85.47 & --- & 85.57 & --- \\
89	 & 8B & 87.60 & 87.79 & --- & \underline{87.70} & +2.13 \\
90	 & 14B & 89.73 & 88.57 & 88.28 & 88.86 $\pm$ 0.77 & +1.16 \\
91	\bottomrule
92	\end{tabular}
93	\end{table}
94	
95	\begin{figure}[!t]
96	\centering
97	\includegraphics[width=\columnwidth]{figures/paper/figure2_v3.pdf}
98	\caption{Function-level accuracy scaling (4B--14B). CLS and CWM accuracy with shaded gap region; $y$-axis does not start at zero. The \cls{}--\cwm{} gap shows a non-monotonic pattern: 1.32\pp{} at 4B, widening to 2.62\pp{} at 8B, then narrowing to 0.43\pp{} at 14B (3 seeds).}
99	\label{fig:scaling_gap}
100	\end{figure}
101	
102	\cls{} and \traj{} both scale positively from 4B to 8B (+1.27\pp{} and +2.13\pp{} respectively), while \cwm{} remains flat ($-$0.03\pp{}). At 8B, the ranking is \cls{} (89.94) $>$ \traj{} (87.70) $>$ \cwm{} (87.33). The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B (Figure~\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \cls{}/\cwm{}) yields $p = 0.0066$ (95\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.
103	
104	At 14B (3 seeds), all three formulations converge in point estimates: \cls{} 89.93$\pm$0.80\%, \cwm{} 89.50$\pm$0.67\%, \traj{} 88.86$\pm$0.77\%. The maximum pairwise gap (\cls{}--\traj{}) narrows from 3.11\pp{} at 4B to 1.07\pp{} at 14B, within the $\pm$2\pp{} equivalence margin. Seed-level TOST (df${=}$2) is inconclusive for equivalence in both pairs ($p{=}0.076$ for \cls{}--\cwm{}, $p{=}0.187$ for \cls{}--\traj{}), reflecting the low power inherent in 3-seed comparisons; Bayesian ROPE provides moderate support ($P(\text{ROPE}){=}0.887$ and $0.780$ respectively; Appendix~\ref{app:bayesian_rope}). \cwm{}'s delayed scaling onset---flat from 4B to 8B, then +2.17\pp{} at 14B---and \traj{}'s decelerating convergence (+2.13\pp{} at 8B, +1.16\pp{} at 14B) are both consistent with capacity-dependent convergence at function level.
105	
106	\paragraph{Baseline scaling.} Prompting baselines remain well below fine-tuning: the best result (14B 3-shot, 73.12\%) is 16.82\pp{} below fine-tuned \cls{} at 8B. Only \cls{} scales positively across both complexity levels; \traj{} shows no repo-level scaling benefit (72.92\% at both 4B and 8B).
107	
108	
109	\subsection{Function-Level Equivalence}
110	\label{sec:equivalence}
111	
112	We test pairwise equivalence on 523 variant-level instances across five seeds.\footnote{Seeds 789/0 use NF4 inference; the remaining three use bfloat16. Restricting to bfloat16 only: \cls{}--\cwm{} remains significant ($p{<}0.05$); \cls{}--\traj{} yields $p{=}0.128$.} Our $\pm$2\pp{} SESOI threshold~\cite{lakens2017,wellek2010} is motivated by domain considerations but was not pre-registered: at 85--88\% accuracy, 2\pp{} corresponds to ${\sim}$2--3 problems out of 114, below practitioner-relevant differences, and is consistent with between-seed variation (0.37--0.97\pp{} std). Within-problem predictions are correlated (ICC $= 0.191$, DEFF $= 3.97$~\cite{moulton1990}); confidence intervals use clustered bootstrap (\S\ref{sec:setup}). Sensitivity analysis shows \cls{}--\cwm{} equivalence is robust across $\pm$1.5--3\pp{} margins (minimum $\pm$1.52\pp{}); \cls{}--\traj{} equivalence is margin-sensitive ($\pm$1.5\pp{}: $p{=}0.068$; Table~\ref{tab:tost_sensitivity}).
113	
114	\paragraph{\cls{}--\cwm{} equivalence.} The pooled gap is 1.24\pp{} (88.43\%--87.19\%); TOST confirms equivalence at $p = 0.007$ ($\pm$2\pp{} margin), surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.028$; Table~\ref{tab:holm}). Equivalence holds at margins as tight as $\pm$1.52\pp{} (Table~\ref{tab:tost_sensitivity}). On DeepSeek-Coder, the \cls{}--\cwm{} gap of 0.02\pp{} is consistent with equivalence but underpowered (2 seeds).
115	
116	\paragraph{\cls{}--\traj{} equivalence.} The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]); TOST yields $p = 0.025$ ($\pm$2\pp{}), nominally significant but not surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.075$; Table~\ref{tab:holm}). The DeepSeek \cls{}--\traj{} gap (2.69\pp{}) exceeds the $\pm$2\pp{} margin; \traj{} parity is model-dependent. Per-test classification provides diagnostic information (which tests fail) at no cost to variant-level accuracy, paralleling process supervision~\cite{lightman2023letsverify}.
117	
118	\paragraph{Statistical power.} With $n_{\text{eff}} \approx 86$ after clustering, TOST power is ${\sim}$0.3~\cite{cohen1988}---a 70\% probability of failing to confirm equivalence even if the true difference is moderate. The \cls{}--\cwm{} equivalence ($p{=}0.007$) is robust to this limitation; the \cls{}--\traj{} inconclusive result ($p{=}0.025$, adjusted $p{=}0.075$) may reflect insufficient power rather than a genuine difference (a minimum $n_{\text{eff}} \approx 350$ would be needed for ${\geq}$0.8 power at $\pm$2\pp{}). A Bayesian ROPE analysis corroborates: $P(\text{ROPE}){=}0.975$ for \cls{}--\cwm{} and $P(\text{ROPE}){=}0.970$ at variant level for \cls{}--\traj{} (Appendix~\ref{app:bayesian_rope}). At per-test level, \cls{}--\traj{} $P(\text{ROPE}){=}0.542$ (inconclusive), reflecting aggregation effects. 14B scaling data corroborates: the \cls{}--\traj{} gap narrows to 1.07\pp{} (\S\ref{sec:scaling}).
119	
120	
121	\subsection{Repo-Level: Complexity-Dependent Divergence}
122	\label{sec:repo}
123	
124	Table~\ref{tab:repo_level} compares formulations at repository-level complexity. The following results are established under ${\leq}$8B LoRA; preliminary 14B evidence (\S\ref{sec:scaling}) suggests these gaps may narrow at larger scales. Variant-level comparisons ($n{=}48$) are exploratory due to limited seed coverage; the per-test interaction effect is statistically confirmed (see below). Checkpoints are val-selected where validation loss is computable (\S\ref{sec:setup}); the test set has zero problem overlap with validation.
125	
126	\begin{table}[t]
127	\centering
128	\small
129	\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set. Qwen3-8B \cls{}/\traj{}: mean $\pm$ std over 3 seeds; DeepSeek \cls{}: 2 seeds\textsuperscript{$\ddagger$}; DeepSeek \traj{}: 3 seeds; Qwen3-4B: seed 42. \cwm{}: 3 seeds (42/123/456).}
130	\label{tab:repo_level}
131	\resizebox{\columnwidth}{!}{%
132	\setlength{\tabcolsep}{4pt}
133	\begin{tabular}{lcccc}
134	\toprule
135	\textbf{Model} & \textbf{\cls{} (\%)} & \textbf{\cls{} Var.\ (\%)} & \textbf{\cwm{} (\%)} & \textbf{\traj{} Var.\ (\%)\textsuperscript{$\diamond$}} \\
136	\midrule
137	Qwen3-4B & 83.63 & 64.58 & 58.04 & 72.92 \\
138	Qwen3-8B & \textbf{84.83 $\pm$ 0.67} & 72.92 / 81.25\textsuperscript{$\dagger$} & 66.48 $\pm$ 1.15 & 72.91 $\pm$ 3.61 \\
139	DeepSeek-6.7B & 84.38 $\pm$ 2.50\textsuperscript{$\ddagger$} & 81.25\textsuperscript{$\dagger$} & 58.30 $\pm$ 2.82 & 77.08 $\pm$ 3.61 \\
140	\midrule
141	0-shot (Qwen3-8B) & 49.90 & --- & --- & --- \\
142	0-shot (DeepSeek) & 48.54 & --- & --- & --- \\
143	Majority & 72.96 & 54.17 & 72.96 & 54.17 \\
144	\bottomrule
145	\end{tabular}}
146	
147	\vspace{2pt}
148	{\footnotesize \textsuperscript{$\dagger$}Individual-seed variant accuracy. \textsuperscript{$\ddagger$}One seed excluded: truncate preprocessing$\to$NaN val loss, decision collapse (Table~\ref{tab:taxonomy}); mean over two matched seeds. \textsuperscript{$\diamond$}Var.\ columns: variant-level accuracy ($n{=}48$); \cls{} aggregated via all-pass rule; \traj{} by design. Per-test: $n{=}9{,}784$. \cwm{} unparseable: 54\% (4B); default to pass; parseable-only 38--43\%, below majority. Eval seq\_length differs across models (Appendix~\ref{app:threats}). \cwm{} uses final-epoch checkpoint (step 6633) for s123/s456; s42 uses an earlier checkpoint (step 400) from a prior training configuration. Val loss is undefined for DeepSeek \cwm{} runs (Qwen3 \cwm{} has valid val loss; see \S\ref{sec:setup}). Checkpoint sensitivity analysis in Appendix~\ref{app:cwm_convergence}.}
149	\end{table}
150	
151	Few-shot prompting (3-shot ICL) collapses to an always-predict-unresolved baseline (variant accuracy 45.83\%, below majority 54.17\%; Appendix~\ref{app:few_shot}), establishing that execution-free verification requires task-specific fine-tuning regardless of formulation. The fine-tuning requirement (35--36\pp{} gains, Table~\ref{tab:repo_level}) is the first layer of our three-layer structure.
152	
153	\paragraph{Formulation divergence.} Under our 4--8B LoRA protocol, \cls{} and \cwm{} diverge: the gap is 25.59\pp{} at 4B and 18.35\pp{} at 8B (Table~\ref{tab:repo_level}), with \cwm{} falling below majority baseline at both scales. Limited seed coverage and multiple confounds (\S\ref{sec:threats}) limit causal attribution.
154	
155	\paragraph{Cross-model consistency.} DeepSeek-Coder shows the same direction (\cls{} $>$ \cwm{}) across all seeds; gap variation across families (20\pp{} Qwen3 vs.\ 23--28\pp{} DeepSeek) narrows to ${\sim}$2\pp{} under matched checkpoints (Appendix~\ref{app:threats}). All six \cwm{} repo-level seeds exhibit format collapse ($>$50\% unparseable), ruling out seed-specific artifacts.
156	
157	\paragraph{Failure mode taxonomy.} Variant-level analysis ($n{=}48$) identifies three failure modes (Table~\ref{tab:taxonomy}): format collapse (\cwm{}, 51--74\% unparseable), decision collapse (\cls{} under truncate preprocessing, fail recall ${\sim}$14\%), and aggregation penalty (\cls{} under drop preprocessing, fail recall 38--57\%). Decision collapse is configuration-dependent, not model-inherent. \traj{} avoids aggregation penalty by predicting variant outcomes directly (72.91--77.08\%). Downsampling \cls{} to match \traj{}'s data volume still yields 80.74\% (+7.82\pp{} above \traj{}; Appendix~\ref{app:downsample}). The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity (per-test vs.\ variant-level), a formulation-inherent confound that cannot be experimentally resolved.
158	
159	\begin{table}[t]
160	\centering
161	\small
162	\caption{Repo-level failure mode taxonomy. Variant-level majority baseline: 54.17\%.}
163	\label{tab:taxonomy}
164	\setlength{\tabcolsep}{3pt}
165	\resizebox{\columnwidth}{!}{%
166	\begin{tabular}{llcc}
167	\toprule
168	\textbf{Failure Mode} & \textbf{Representative} & \textbf{Fail Recall} & \textbf{Variant Acc} \\
169	\midrule
170	Format collapse & \cwm{} (all) & N/A & 48--52\% \\
171	Decision collapse & \cls{} (DeepSeek, s123) & ${\sim}$14\% & 56\% \\
172	Aggr.\ penalty & \cls{} (Qwen3-8B) & 51--57\% & 73--81\% \\
173	Aggr.\ penalty & \cls{} (DeepSeek, s42) & 38--51\% & 79--81\% \\
174	\bottomrule
175	\end{tabular}}
176	\end{table}
177	
178	\paragraph{Default assignment artifact.} The apparent \cwm{} accuracy increase from 4B to 8B is an artifact of rising unparseable rate (53.7\%$\to$73.8\%), inflating accuracy via majority-class default while parseable-only accuracy decreases (42.88\%$\to$38.52\%); cross-seed evidence confirms the pattern (Appendix~\ref{app:parseable_bias}).
179	
180	\paragraph{Complexity as moderator.} The \cls{}--\cwm{} gap widens from 1--3\pp{} (function) to 18--26\pp{} (repo) under our protocol; a matched-context ablation confirms input disparity explains $<$3\% of this gap (Appendix~\ref{app:ablations}). While the directional advantage of lower-complexity output formulations may be anticipated from \S\ref{sec:failure-modes}, the magnitude of this gap, the function-level equivalence, and the specific failure mechanisms (Table~\ref{tab:taxonomy}) were not predictable a priori.
181	
182	\paragraph{Formulation$\times$complexity interaction.} A mixed-effects LPM ($n{=}56{,}480$, 139 clusters, DeepSeek-Coder) confirms: \cwm{} effect at function level is negligible ($\hat{\beta}{=}-0.002$, $p{=}0.805$), but the formulation$\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$). A cross-model LPM confirms formulation dominates ($\hat{\beta}{=}-0.22$ vs.\ model $\hat{\beta}{=}+0.011$); model identity significance is estimator-dependent (LPM $p{=}0.002$; GEE $p{=}0.449$), consistent with limited clusters ($k{=}25 < 40$; Appendix~\ref{app:interaction}).
183	
184	\subsection{Analysis}
185	\label{sec:analysis}
186	
187	\paragraph{Aggregation penalty.} The aggregation penalty ranges from 1.36\pp{} to 19\pp{}, negligible at function level ($\bar{T} \approx 2.3$) but substantial at repo level ($\bar{T} \gg 10$; Appendix~\ref{app:extended_analysis}(a)).
188	
189	\paragraph{Why does generation degrade at repo level?} Output complexity increases nonlinearly: function-level outputs average ${\sim}$5--15 tokens; repo-level outputs average ${\sim}$477 tokens, leading to format collapse under our ${\leq}$8B LoRA protocol (53--74\% unparseable). Even parseable outputs achieve only 38--43\%, below majority; forced parsing suggests the bottleneck is semantic, not syntactic (Appendix~\ref{app:extended_analysis}(c)). Four targeted interventions all fail to close this gap: doubling LoRA rank to~32 does not improve format compliance; majority voting ($k{=}5$) is ineffective because collapsed outputs are near-identical across samples; relaxed matching still leaves ${>}$50\% unparseable; and scaling from 4B to 8B worsens the unparseable rate from 53.7\% to 73.8\% (Appendix~\ref{app:extended_analysis}(g)). Checkpoint selection does not explain the gap: matched epoch-3 comparisons yield 20--23\pp{} gaps, and \cls{} varies $<$1\pp{} across epochs (Appendix~\ref{app:cwm_convergence}). \cls{} achieves 217$\times$ higher throughput than \cwm{} (1 vs.\ avg 477 output tokens; Appendix~\ref{app:extended_analysis}(i)).
190	
191	\paragraph{Error complementarity.} \cls{} and \cwm{} exhibit partially complementary errors. An oracle combination achieves 90.63\% (+2.80\pp{}; 95\% CI [89.3\%, 91.9\%]; single-seed) at function level and 95.83\% (+14.58\pp{}; $n{=}48$) at repo level. Simple routing heuristics capture $<$0.4\pp{} of the oracle gap; the complementarity is instance-specific, suggesting a learned router is needed (Appendix~\ref{app:oracle}).
192	
193	\subsection{Threats to Validity}
194	\label{sec:threats}
195	
196	We identify five potential confounds (Appendix~\ref{app:threats}): checkpoint selection ($<$1\pp{}), evaluation sequence length (${\sim}$1.5\pp{}), preprocessing (${\sim}$8\pp{}), \traj{} training regime, and \cwm{} scale/pretraining (primary limitation). Preprocessing and checkpoint interact, accounting for up to 7.68\pp{} variation within one model (Appendix~\ref{app:threats}). The 18--26\pp{} gap exceeds any single confound, but correlated confounds and limited seeds preclude definitive causal attribution. Holm-Bonferroni ($k{=}5$) confirms the two core claims (adjusted $p{=}0.015$ and $p{=}0.028$; Table~\ref{tab:holm}).
197	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "ea25e1f2-a294-4f99-82fb-211383880449",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe systematically compare \\cls{}, \\cwm{}, and \\traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\n\\emph{Function-level}: mutated variants from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).\n\\emph{Repo-level}: per-test instances from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants. ${\\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\\%). Val-based checkpoint selection follows standard practice~\\cite{jimenez2024swebench}; runs with NaN validation loss (due to truncated targets exceeding 2,048-token limits) default to the final epoch checkpoint (Appendix~\\ref{app:hyperparams}). Qwen3 \\cwm{} runs show early overfitting (best at ${\\sim}$6\\% of training); checkpoint details in Appendix~\\ref{app:hyperparams}.\n\n\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \\S\\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \\cls{} and \\cwm{}). Our \\cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model~\\cite{meta2025cwm}. \\traj{} uses variant-level rather than per-test labels (8,052 vs.\\ 15,290 training instances, but covering $2.24\\times$ more unique code variants); the comparison is confounded by both label granularity and data composition (\\S\\ref{sec:repo}). Repo-level models use val-selected checkpoints where available; runs with NaN validation loss use the final epoch checkpoint (Appendix~\\ref{app:hyperparams}). Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Full hyperparameter details appear in Appendix~\\ref{app:hyperparams}.\n\n\\paragraph{Statistics.}\nTOST equivalence testing is our primary inferential framework for function-level claims; clustered bootstrap provides confidence intervals, Bayesian ROPE serves as a robustness check, and mixed-effects regression tests the formulation$\\times$complexity interaction. Confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples; we resample entire problems, not individual tests, to preserve within-problem correlations). Equivalence uses Two One-Sided Tests (TOST)~\\cite{schuirmann1987tost} with $\\pm$2 percentage point (\\pp{}) margin; for function-level TOST, we use seed-level paired analysis (df${=}$4 for 5-seed comparisons, df${=}$2 for 3-seed), treating each training seed as the unit of replication. This is more conservative than problem-level clustered bootstrap, which pools within-seed observations and may understate between-seed uncertainty. Holm-Bonferroni correction~\\cite{holm1979} controls family-wise error rate across the five primary comparisons (Table~\\ref{tab:holm}). Intraclass correlation coefficient (ICC)~\\cite{shrout1979icc} quantifies within-problem correlation. Variant-level effect sizes and statistical power analysis are reported in Appendix~\\ref{app:power}. Oracle analysis uses SWE-bench Verified (500 instances).\n\n\n\\subsection{Function-Level Results}\n\\label{sec:func_results}\n\nTable~\\ref{tab:main_results} reports function-level results across formulations and model families.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Function-level per-test accuracy on HumanEval+MBPP ($n{=}1{,}890$). Mean $\\pm$ std over 5 seeds (Qwen3) or 2 seeds (DeepSeek). Seeds 42/123/456: bfloat16; 789/0: NF4. DeepSeek: $n{=}2$ seeds; std reported for descriptive comparison, not inferential. \\traj{}\\textsuperscript{$\\star$} evaluated on 1,032-sample subset (447 matched variants). All prompting baselines use NF4 4-bit quantization. \\textsuperscript{$\\star$}Training configuration differs (\\S\\ref{sec:repo}).}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Seeds} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Qwen3 (primary)}} \\\\\n\\cls{} (fine-tuned) & 4B & 5 & \\textbf{88.43 $\\pm$ 0.78} \\\\\n\\cwm{} (fine-tuned) & 4B & 5 & \\underline{87.19 $\\pm$ 0.37} \\\\\n\\traj{}\\textsuperscript{$\\star$} (fine-tuned) & 4B & 5 & 86.30 $\\pm$ 0.97 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{DeepSeek-Coder (cross-model consistency check)}} \\\\\n\\cls{} (fine-tuned) & 6.7B & 2 & \\textbf{86.85 $\\pm$ 0.11} \\\\\n\\cwm{} (fine-tuned) & 6.7B & 2 & \\underline{86.83 $\\pm$ 1.49} \\\\\n\\traj{}\\textsuperscript{$\\star$} (fine-tuned) & 6.7B & 2 & 84.16 $\\pm$ 1.30 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Prompting baselines}} \\\\\n0-shot & 8B (Qwen3) & 1 & 60.53 \\\\\n0-shot & 14B (Qwen3) & 1 & 66.24 \\\\\n0-shot & 6.7B (DeepSeek) & 1 & 63.00 \\\\\nZS LLM-as-judge & 8B (Qwen3) & 1 & 64.40 \\\\\nZS LLM-as-judge & 6.7B (DeepSeek) & 1 & 56.56 \\\\\nZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\\\\n3-shot ICL & 8B (Qwen3) & 1 & 60.42 \\\\\n3-shot ICL & 14B (Qwen3) & 1 & 73.12 \\\\\n3-shot ICL & 6.7B (DeepSeek) & 1 & 59.95 \\\\\n\\midrule\nMajority (pass) & --- & --- & 51.75 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll three formulations achieve comparable accuracy on Qwen3-4B: \\cls{} 88.43\\% ($\\pm$0.78), \\cwm{} 87.19\\% ($\\pm$0.37), \\traj{} 86.30\\% ($\\pm$0.97). DeepSeek-Coder-6.7B shows: \\cls{} 86.85\\%, \\cwm{} 86.83\\%, \\traj{} 84.16\\%. The \\cls{}--\\cwm{} gap (0.02--1.24\\pp{}) is within seed noise in both families. However, the \\cls{}--\\traj{} gap is model-dependent: $<$1\\pp{} on Qwen3 but 2.69\\pp{} on DeepSeek-Coder, exceeding the $\\pm$2\\pp{} equivalence margin (\\S\\ref{sec:equivalence}). \\cls{} and \\cwm{} are robustly equivalent; \\traj{} parity is model-contingent. Zero-shot baselines (Tables~\\ref{tab:main_results} and~\\ref{tab:repo_level}) establish that repo-level verification requires fine-tuning (0-shot$\\to$fine-tuned gains of 35--36\\pp{}) and that formulation choice matters only at repo level (\\cls{} outperforms \\cwm{} by 18--26\\pp{}).\n\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nBeyond overall accuracy, we examine whether formulation ranking is stable across model sizes. Table~\\ref{tab:scaling} compares all three formulations at 4B, 8B, and 14B. The 4B and 8B rows use seeds 42 and 123; the 14B row uses seeds 42, 123, and 456. All rows use bfloat16 inference.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: accuracy (\\%) at 4B, 8B, and 14B (Qwen3). Seeds 42/123 (4B/8B), seeds 42/123/456 (14B). All bfloat16 inference. $\\Delta$: change from previous size. \\cwm{} and \\traj{}\\textsuperscript{$\\star$} use $n{=}2$ seeds (4B/8B) and $n{=}3$ seeds (14B). \\traj{}\\textsuperscript{$\\star$} evaluated on 1{,}032-sample subset; \\cls{}/\\cwm{} use the full 1{,}890-sample set. \\textsuperscript{$\\star$}Training configuration differs (\\S\\ref{sec:repo}).}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Mean} & \\textbf{$\\Delta$} \\\\\n\\midrule\n\\multirow{3}{*}{\\cls{}} & 4B & 87.83 & 89.52 & --- & \\textbf{88.68} & --- \\\\\n & 8B & \\textbf{90.48} & 89.40 & --- & \\textbf{89.94} & +1.27 \\\\\n & 14B & 89.21 & \\textbf{90.79} & 89.79 & \\textbf{89.93 $\\pm$ 0.80} & $-$0.01 \\\\\n\\midrule\n\\multirow{3}{*}{\\cwm{}} & 4B & 87.51 & 87.20 & --- & \\underline{87.36} & --- \\\\\n & 8B & 87.67 & 86.98 & --- & 87.33 & $-$0.03 \\\\\n & 14B & 89.26 & 88.99 & 90.26 & \\underline{89.50 $\\pm$ 0.67} & +2.17 \\\\\n\\midrule\n\\multirow{3}{*}{\\traj{}} & 4B & 85.66 & 85.47 & --- & 85.57 & --- \\\\\n & 8B & 87.60 & 87.79 & --- & \\underline{87.70} & +2.13 \\\\\n & 14B & 89.73 & 88.57 & 88.28 & 88.86 $\\pm$ 0.77 & +1.16 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[!t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/figure2_v3.pdf}\n\\caption{Function-level accuracy scaling (4B--14B). CLS and CWM accuracy with shaded gap region; $y$-axis does not start at zero. The \\cls{}--\\cwm{} gap shows a non-monotonic pattern: 1.32\\pp{} at 4B, widening to 2.62\\pp{} at 8B, then narrowing to 0.43\\pp{} at 14B (3 seeds).}\n\\label{fig:scaling_gap}\n\\end{figure}\n\n\\cls{} and \\traj{} both scale positively from 4B to 8B (+1.27\\pp{} and +2.13\\pp{} respectively), while \\cwm{} remains flat ($-$0.03\\pp{}). At 8B, the ranking is \\cls{} (89.94) $>$ \\traj{} (87.70) $>$ \\cwm{} (87.33). The \\cls{}--\\cwm{} gap widens from 1.32\\pp{} at 4B to 2.62\\pp{} at 8B (Figure~\\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \\cls{}/\\cwm{}) yields $p = 0.0066$ (95\\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.\n\nAt 14B (3 seeds), all three formulations converge in point estimates: \\cls{} 89.93$\\pm$0.80\\%, \\cwm{} 89.50$\\pm$0.67\\%, \\traj{} 88.86$\\pm$0.77\\%. The maximum pairwise gap (\\cls{}--\\traj{}) narrows from 3.11\\pp{} at 4B to 1.07\\pp{} at 14B, within the $\\pm$2\\pp{} equivalence margin. Seed-level TOST (df${=}$2) is inconclusive for equivalence in both pairs ($p{=}0.076$ for \\cls{}--\\cwm{}, $p{=}0.187$ for \\cls{}--\\traj{}), reflecting the low power inherent in 3-seed comparisons; Bayesian ROPE provides moderate support ($P(\\text{ROPE}){=}0.887$ and $0.780$ respectively; Appendix~\\ref{app:bayesian_rope}). \\cwm{}'s delayed scaling onset---flat from 4B to 8B, then +2.17\\pp{} at 14B---and \\traj{}'s decelerating convergence (+2.13\\pp{} at 8B, +1.16\\pp{} at 14B) are both consistent with capacity-dependent convergence at function level.\n\n\\paragraph{Baseline scaling.} Prompting baselines remain well below fine-tuning: the best result (14B 3-shot, 73.12\\%) is 16.82\\pp{} below fine-tuned \\cls{} at 8B. Only \\cls{} scales positively across both complexity levels; \\traj{} shows no repo-level scaling benefit (72.92\\% at both 4B and 8B).\n\n\n\\subsection{Function-Level Equivalence}\n\\label{sec:equivalence}\n\nWe test pairwise equivalence on 523 variant-level instances across five seeds.\\footnote{Seeds 789/0 use NF4 inference; the remaining three use bfloat16. Restricting to bfloat16 only: \\cls{}--\\cwm{} remains significant ($p{<}0.05$); \\cls{}--\\traj{} yields $p{=}0.128$.} Our $\\pm$2\\pp{} SESOI threshold~\\cite{lakens2017,wellek2010} is motivated by domain considerations but was not pre-registered: at 85--88\\% accuracy, 2\\pp{} corresponds to ${\\sim}$2--3 problems out of 114, below practitioner-relevant differences, and is consistent with between-seed variation (0.37--0.97\\pp{} std). Within-problem predictions are correlated (ICC $= 0.191$, DEFF $= 3.97$~\\cite{moulton1990}); confidence intervals use clustered bootstrap (\\S\\ref{sec:setup}). Sensitivity analysis shows \\cls{}--\\cwm{} equivalence is robust across $\\pm$1.5--3\\pp{} margins (minimum $\\pm$1.52\\pp{}); \\cls{}--\\traj{} equivalence is margin-sensitive ($\\pm$1.5\\pp{}: $p{=}0.068$; Table~\\ref{tab:tost_sensitivity}).\n\n\\paragraph{\\cls{}--\\cwm{} equivalence.} The pooled gap is 1.24\\pp{} (88.43\\%--87.19\\%); TOST confirms equivalence at $p = 0.007$ ($\\pm$2\\pp{} margin), surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.028$; Table~\\ref{tab:holm}). Equivalence holds at margins as tight as $\\pm$1.52\\pp{} (Table~\\ref{tab:tost_sensitivity}). On DeepSeek-Coder, the \\cls{}--\\cwm{} gap of 0.02\\pp{} is consistent with equivalence but underpowered (2 seeds).\n\n\\paragraph{\\cls{}--\\traj{} equivalence.} The pooled gap is $-$0.45\\pp{} (95\\% CI [$-$1.71, +0.84]); TOST yields $p = 0.025$ ($\\pm$2\\pp{}), nominally significant but not surviving Holm-Bonferroni correction ($k{=}5$, adjusted $p{=}0.075$; Table~\\ref{tab:holm}). The DeepSeek \\cls{}--\\traj{} gap (2.69\\pp{}) exceeds the $\\pm$2\\pp{} margin; \\traj{} parity is model-dependent. Per-test classification provides diagnostic information (which tests fail) at no cost to variant-level accuracy, paralleling process supervision~\\cite{lightman2023letsverify}.\n\n\\paragraph{Statistical power.} With $n_{\\text{eff}} \\approx 86$ after clustering, TOST power is ${\\sim}$0.3~\\cite{cohen1988}---a 70\\% probability of failing to confirm equivalence even if the true difference is moderate. The \\cls{}--\\cwm{} equivalence ($p{=}0.007$) is robust to this limitation; the \\cls{}--\\traj{} inconclusive result ($p{=}0.025$, adjusted $p{=}0.075$) may reflect insufficient power rather than a genuine difference (a minimum $n_{\\text{eff}} \\approx 350$ would be needed for ${\\geq}$0.8 power at $\\pm$2\\pp{}). A Bayesian ROPE analysis corroborates: $P(\\text{ROPE}){=}0.975$ for \\cls{}--\\cwm{} and $P(\\text{ROPE}){=}0.970$ at variant level for \\cls{}--\\traj{} (Appendix~\\ref{app:bayesian_rope}). At per-test level, \\cls{}--\\traj{} $P(\\text{ROPE}){=}0.542$ (inconclusive), reflecting aggregation effects. 14B scaling data corroborates: the \\cls{}--\\traj{} gap narrows to 1.07\\pp{} (\\S\\ref{sec:scaling}).\n\n\n\\subsection{Repo-Level: Complexity-Dependent Divergence}\n\\label{sec:repo}\n\nTable~\\ref{tab:repo_level} compares formulations at repository-level complexity. The following results are established under ${\\leq}$8B LoRA; preliminary 14B evidence (\\S\\ref{sec:scaling}) suggests these gaps may narrow at larger scales. Variant-level comparisons ($n{=}48$) are exploratory due to limited seed coverage; the per-test interaction effect is statistically confirmed (see below). Checkpoints are val-selected where validation loss is computable (\\S\\ref{sec:setup}); the test set has zero problem overlap with validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set. Qwen3-8B \\cls{}/\\traj{}: mean $\\pm$ std over 3 seeds; DeepSeek \\cls{}: 2 seeds\\textsuperscript{$\\ddagger$}; DeepSeek \\traj{}: 3 seeds; Qwen3-4B: seed 42. \\cwm{}: 3 seeds (42/123/456).}\n\\label{tab:repo_level}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{\\cls{} (\\%)} & \\textbf{\\cls{} Var.\\ (\\%)} & \\textbf{\\cwm{} (\\%)} & \\textbf{\\traj{} Var.\\ (\\%)\\textsuperscript{$\\diamond$}} \\\\\n\\midrule\nQwen3-4B & 83.63 & 64.58 & 58.04 & 72.92 \\\\\nQwen3-8B & \\textbf{84.83 $\\pm$ 0.67} & 72.92 / 81.25\\textsuperscript{$\\dagger$} & 66.48 $\\pm$ 1.15 & 72.91 $\\pm$ 3.61 \\\\\nDeepSeek-6.7B & 84.38 $\\pm$ 2.50\\textsuperscript{$\\ddagger$} & 81.25\\textsuperscript{$\\dagger$} & 58.30 $\\pm$ 2.82 & 77.08 $\\pm$ 3.61 \\\\\n\\midrule\n0-shot (Qwen3-8B) & 49.90 & --- & --- & --- \\\\\n0-shot (DeepSeek) & 48.54 & --- & --- & --- \\\\\nMajority & 72.96 & 54.17 & 72.96 & 54.17 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{$\\dagger$}Individual-seed variant accuracy. \\textsuperscript{$\\ddagger$}One seed excluded: truncate preprocessing$\\to$NaN val loss, decision collapse (Table~\\ref{tab:taxonomy}); mean over two matched seeds. \\textsuperscript{$\\diamond$}Var.\\ columns: variant-level accuracy ($n{=}48$); \\cls{} aggregated via all-pass rule; \\traj{} by design. Per-test: $n{=}9{,}784$. \\cwm{} unparseable: 54\\% (4B); default to pass; parseable-only 38--43\\%, below majority. Eval seq\\_length differs across models (Appendix~\\ref{app:threats}). \\cwm{} uses final-epoch checkpoint (step 6633) for s123/s456; s42 uses an earlier checkpoint (step 400) from a prior training configuration. Val loss is undefined for DeepSeek \\cwm{} runs (Qwen3 \\cwm{} has valid val loss; see \\S\\ref{sec:setup}). Checkpoint sensitivity analysis in Appendix~\\ref{app:cwm_convergence}.}\n\\end{table}\n\nFew-shot prompting (3-shot ICL) collapses to an always-predict-unresolved baseline (variant accuracy 45.83\\%, below majority 54.17\\%; Appendix~\\ref{app:few_shot}), establishing that execution-free verification requires task-specific fine-tuning regardless of formulation. The fine-tuning requirement (35--36\\pp{} gains, Table~\\ref{tab:repo_level}) is the first layer of our three-layer structure.\n\n\\paragraph{Formulation divergence.} Under our 4--8B LoRA protocol, \\cls{} and \\cwm{} diverge: the gap is 25.59\\pp{} at 4B and 18.35\\pp{} at 8B (Table~\\ref{tab:repo_level}), with \\cwm{} falling below majority baseline at both scales. Limited seed coverage and multiple confounds (\\S\\ref{sec:threats}) limit causal attribution.\n\n\\paragraph{Cross-model consistency.} DeepSeek-Coder shows the same direction (\\cls{} $>$ \\cwm{}) across all seeds; gap variation across families (20\\pp{} Qwen3 vs.\\ 23--28\\pp{} DeepSeek) narrows to ${\\sim}$2\\pp{} under matched checkpoints (Appendix~\\ref{app:threats}). All six \\cwm{} repo-level seeds exhibit format collapse ($>$50\\% unparseable), ruling out seed-specific artifacts.\n\n\\paragraph{Failure mode taxonomy.} Variant-level analysis ($n{=}48$) identifies three failure modes (Table~\\ref{tab:taxonomy}): format collapse (\\cwm{}, 51--74\\% unparseable), decision collapse (\\cls{} under truncate preprocessing, fail recall ${\\sim}$14\\%), and aggregation penalty (\\cls{} under drop preprocessing, fail recall 38--57\\%). Decision collapse is configuration-dependent, not model-inherent. \\traj{} avoids aggregation penalty by predicting variant outcomes directly (72.91--77.08\\%). Downsampling \\cls{} to match \\traj{}'s data volume still yields 80.74\\% (+7.82\\pp{} above \\traj{}; Appendix~\\ref{app:downsample}). The CLS--TRAJ repo-level comparison remains exploratory: downsample ablation controls data volume but not label granularity (per-test vs.\\ variant-level), a formulation-inherent confound that cannot be experimentally resolved.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level failure mode taxonomy. Variant-level majority baseline: 54.17\\%.}\n\\label{tab:taxonomy}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Failure Mode} & \\textbf{Representative} & \\textbf{Fail Recall} & \\textbf{Variant Acc} \\\\\n\\midrule\nFormat collapse & \\cwm{} (all) & N/A & 48--52\\% \\\\\nDecision collapse & \\cls{} (DeepSeek, s123) & ${\\sim}$14\\% & 56\\% \\\\\nAggr.\\ penalty & \\cls{} (Qwen3-8B) & 51--57\\% & 73--81\\% \\\\\nAggr.\\ penalty & \\cls{} (DeepSeek, s42) & 38--51\\% & 79--81\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Default assignment artifact.} The apparent \\cwm{} accuracy increase from 4B to 8B is an artifact of rising unparseable rate (53.7\\%$\\to$73.8\\%), inflating accuracy via majority-class default while parseable-only accuracy decreases (42.88\\%$\\to$38.52\\%); cross-seed evidence confirms the pattern (Appendix~\\ref{app:parseable_bias}).\n\n\\paragraph{Complexity as moderator.} The \\cls{}--\\cwm{} gap widens from 1--3\\pp{} (function) to 18--26\\pp{} (repo) under our protocol; a matched-context ablation confirms input disparity explains $<$3\\% of this gap (Appendix~\\ref{app:ablations}). While the directional advantage of lower-complexity output formulations may be anticipated from \\S\\ref{sec:failure-modes}, the magnitude of this gap, the function-level equivalence, and the specific failure mechanisms (Table~\\ref{tab:taxonomy}) were not predictable a priori.\n\n\\paragraph{Formulation$\\times$complexity interaction.} A mixed-effects LPM ($n{=}56{,}480$, 139 clusters, DeepSeek-Coder) confirms: \\cwm{} effect at function level is negligible ($\\hat{\\beta}{=}-0.002$, $p{=}0.805$), but the formulation$\\times$complexity interaction is highly significant ($z{=}-23.7$, $p{<}0.001$). A cross-model LPM confirms formulation dominates ($\\hat{\\beta}{=}-0.22$ vs.\\ model $\\hat{\\beta}{=}+0.011$); model identity significance is estimator-dependent (LPM $p{=}0.002$; GEE $p{=}0.449$), consistent with limited clusters ($k{=}25 < 40$; Appendix~\\ref{app:interaction}).\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{Aggregation penalty.} The aggregation penalty ranges from 1.36\\pp{} to 19\\pp{}, negligible at function level ($\\bar{T} \\approx 2.3$) but substantial at repo level ($\\bar{T} \\gg 10$; Appendix~\\ref{app:extended_analysis}(a)).\n\n\\paragraph{Why does generation degrade at repo level?} Output complexity increases nonlinearly: function-level outputs average ${\\sim}$5--15 tokens; repo-level outputs average ${\\sim}$477 tokens, leading to format collapse under our ${\\leq}$8B LoRA protocol (53--74\\% unparseable). Even parseable outputs achieve only 38--43\\%, below majority; forced parsing suggests the bottleneck is semantic, not syntactic (Appendix~\\ref{app:extended_analysis}(c)). Four targeted interventions all fail to close this gap: doubling LoRA rank to~32 does not improve format compliance; majority voting ($k{=}5$) is ineffective because collapsed outputs are near-identical across samples; relaxed matching still leaves ${>}$50\\% unparseable; and scaling from 4B to 8B worsens the unparseable rate from 53.7\\% to 73.8\\% (Appendix~\\ref{app:extended_analysis}(g)). Checkpoint selection does not explain the gap: matched epoch-3 comparisons yield 20--23\\pp{} gaps, and \\cls{} varies $<$1\\pp{} across epochs (Appendix~\\ref{app:cwm_convergence}). \\cls{} achieves 217$\\times$ higher throughput than \\cwm{} (1 vs.\\ avg 477 output tokens; Appendix~\\ref{app:extended_analysis}(i)).\n\n\\paragraph{Error complementarity.} \\cls{} and \\cwm{} exhibit partially complementary errors. An oracle combination achieves 90.63\\% (+2.80\\pp{}; 95\\% CI [89.3\\%, 91.9\\%]; single-seed) at function level and 95.83\\% (+14.58\\pp{}; $n{=}48$) at repo level. Simple routing heuristics capture $<$0.4\\pp{} of the oracle gap; the complementarity is instance-specific, suggesting a learned router is needed (Appendix~\\ref{app:oracle}).\n\n\\subsection{Threats to Validity}\n\\label{sec:threats}\n\nWe identify five potential confounds (Appendix~\\ref{app:threats}): checkpoint selection ($<$1\\pp{}), evaluation sequence length (${\\sim}$1.5\\pp{}), preprocessing (${\\sim}$8\\pp{}), \\traj{} training regime, and \\cwm{} scale/pretraining (primary limitation). Preprocessing and checkpoint interact, accounting for up to 7.68\\pp{} variation within one model (Appendix~\\ref{app:threats}). The 18--26\\pp{} gap exceeds any single confound, but correlated confounds and limited seeds preclude definitive causal attribution. Holm-Bonferroni ($k{=}5$) confirms the two core claims (adjusted $p{=}0.015$ and $p{=}0.028$; Table~\\ref{tab:holm}).\n",
      "numLines": 197,
      "startLine": 1,
      "totalLines": 197
    }
  }
}
```

</details>

---


### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01UxwVKXfWTn4vNgmBdVsXjg`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "a9c148ba-67f0-4fa1-b03a-20b079ee5f6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVTBykmq9zNh5u5794g9f1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 26412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 576
      },
      "output_tokens": 52,
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

_source line 13 · 2026-05-23T19:16:49.189Z_

<details><summary>↩ Tool result · `toolu_01UxwVKXfWTn4vNgmBdVsXjg`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. This connects to a broader pattern in NLP: task formulation---classification vs.\ generation vs.\ span extraction---systematically affects performance~\cite{raffel2020t5}, but the conditions under which each wins remain task-dependent and empirically unresolved. Recent evidence that generation-based verification outperforms classification in mathematical reasoning~\cite{hosseini2025genrm} raises a further question: does this advantage transfer to code verification, where outputs are longer and format-constrained? A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We present the first systematic empirical comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our contribution is primarily methodological: a matched experimental framework that controls for major confounding variables. The analysis also produces actionable outputs: a failure mode taxonomy that characterizes when and why each formulation fails (\S\ref{sec:repo}), error complementarity findings with practical ensemble implications (\S\ref{sec:analysis}), and formulation selection recommendations conditioned on code complexity (\S\ref{sec:conclusion}). The results suggest a three-layer structure. Fine-tuning is necessary (0-shot$\to$fine-tuned gains of 35--36 percentage points (pp) at repo level). After fine-tuning under our ${\leq}$8B LoRA protocol, \emph{formulation choice is moderated by code complexity, operating through output format}: function-level outputs average ${\sim}$5--15 tokens (minimizing generation-specific failures per \S\ref{sec:failure-modes}), while repo-level outputs average ${\sim}$477 tokens (triggering format collapse): at function level, all formulations achieve comparable accuracy---consistent with the theoretical analysis in \S\ref{sec:failure-modes}, which predicts that short outputs minimize generation-specific failures. At repository level under our ${\leq}$8B LoRA protocol, this equivalence diverges; variant-level analysis identifies three distinct failure modes consistent across model families, though gap magnitude depends on multiple confounds (\S\ref{sec:threats}). Figure~\ref{fig:reformulation} illustrates the three formulations.
9	
10	We make the following contributions:
11	
12	\begin{itemize}[leftmargin=*,itemsep=2pt]
13	\item \textbf{Complexity-moderated formulation choice.} We establish a three-layer structure: (1)~fine-tuning is necessary (35--36\pp{} gains); (2)~at function level, formulations are near-equivalent---\cls{} and \cwm{} achieve statistical equivalence (TOST $p{=}0.007$, Holm-corrected) across both families, while \traj{} equivalence is inconclusive after Holm correction, but the gap narrows from 3.11\pp{} at 4B to 1.07\pp{} at 14B (\S\ref{sec:scaling}); (3)~at repository level under ${\leq}$8B LoRA, this equivalence diverges ($z{=}-23.7$, DeepSeek-Coder), with \cwm{} falling 18--26\pp{} below \cls{}, accompanied by format collapse---four interventions all fail to close the gap. The TOST framework demonstrates strict equivalence rather than mere non-significance. Error analysis reveals partially complementary patterns (oracle: 90.63\% function, 95.83\% repo), though simple heuristics capture $<$0.4\pp{}, framing ensemble routing as an open challenge (\S\ref{sec:equivalence}, \S\ref{sec:repo}, \S\ref{sec:analysis}).
14	
15	\item \textbf{Failure mode taxonomy.} Variant-level analysis identifies three distinct failure modes at repository level---format collapse (\cwm{}), decision collapse (\cls{} under truncate preprocessing), and aggregation penalty (\cls{} under all-pass rule)---providing actionable diagnostic criteria for practitioners selecting a verification formulation (\S\ref{sec:repo}, Table~\ref{tab:taxonomy}).
16	\end{itemize}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "9257028b-9154-4ec9-9fc6-d20ae0342427",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\\cite{snell2024scaling}. Full execution verification is reliable but expensive (\\$1--3 per candidate at repository scale\\footnote{Based on per-instance costs reported by \\citet{yang2024sweagent} and \\citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \\textbf{generation-based simulation}~\\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \\textbf{trajectory-level scoring}~\\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \\textbf{per-test classification}~\\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.\n\nDespite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. This connects to a broader pattern in NLP: task formulation---classification vs.\\ generation vs.\\ span extraction---systematically affects performance~\\cite{raffel2020t5}, but the conditions under which each wins remain task-dependent and empirically unresolved. Recent evidence that generation-based verification outperforms classification in mathematical reasoning~\\cite{hosseini2025genrm} raises a further question: does this advantage transfer to code verification, where outputs are longer and format-constrained? A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?\n\nWe present the first systematic empirical comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our contribution is primarily methodological: a matched experimental framework that controls for major confounding variables. The analysis also produces actionable outputs: a failure mode taxonomy that characterizes when and why each formulation fails (\\S\\ref{sec:repo}), error complementarity findings with practical ensemble implications (\\S\\ref{sec:analysis}), and formulation selection recommendations conditioned on code complexity (\\S\\ref{sec:conclusion}). The results suggest a three-layer structure. Fine-tuning is necessary (0-shot$\\to$fine-tuned gains of 35--36 percentage points (pp) at repo level). After fine-tuning under our ${\\leq}$8B LoRA protocol, \\emph{formulation choice is moderated by code complexity, operating through output format}: function-level outputs average ${\\sim}$5--15 tokens (minimizing generation-specific failures per \\S\\ref{sec:failure-modes}), while repo-level outputs average ${\\sim}$477 tokens (triggering format collapse): at function level, all formulations achieve comparable accuracy---consistent with the theoretical analysis in \\S\\ref{sec:failure-modes}, which predicts that short outputs minimize generation-specific failures. At repository level under our ${\\leq}$8B LoRA protocol, this equivalence diverges; variant-level analysis identifies three distinct failure modes consistent across model families, though gap magnitude depends on multiple confounds (\\S\\ref{sec:threats}). Figure~\\ref{fig:reformulation} illustrates the three formulations.\n\nWe make the following contributions:\n\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Complexity-moderated formulation choice.} We establish a three-layer structure: (1)~fine-tuning is necessary (35--36\\pp{} gains); (2)~at function level, formulations are near-equivalent---\\cls{} and \\cwm{} achieve statistical equivalence (TOST $p{=}0.007$, Holm-corrected) across both families, while \\traj{} equivalence is inconclusive after Holm correction, but the gap narrows from 3.11\\pp{} at 4B to 1.07\\pp{} at 14B (\\S\\ref{sec:scaling}); (3)~at repository level under ${\\leq}$8B LoRA, this equivalence diverges ($z{=}-23.7$, DeepSeek-Coder), with \\cwm{} falling 18--26\\pp{} below \\cls{}, accompanied by format collapse---four interventions all fail to close the gap. The TOST framework demonstrates strict equivalence rather than mere non-significance. Error analysis reveals partially complementary patterns (oracle: 90.63\\% function, 95.83\\% repo), though simple heuristics capture $<$0.4\\pp{}, framing ensemble routing as an open challenge (\\S\\ref{sec:equivalence}, \\S\\ref{sec:repo}, \\S\\ref{sec:analysis}).\n\n\\item \\textbf{Failure mode taxonomy.} Variant-level analysis identifies three distinct failure modes at repository level---format collapse (\\cwm{}), decision collapse (\\cls{} under truncate preprocessing), and aggregation penalty (\\cls{} under all-pass rule)---providing actionable diagnostic criteria for practitioners selecting a verification formulation (\\S\\ref{sec:repo}, Table~\\ref{tab:taxonomy}).\n\\end{itemize}\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  }
}
```

</details>

---


### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01UhFgvsLo2rmD57riTZDW2y`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "b257df8c-6c50-438b-9f95-2ed0604cf57b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVTBykmq9zNh5u5794g9f1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 26412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 576
      },
      "output_tokens": 52,
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

_source line 15 · 2026-05-23T19:16:49.779Z_

<details><summary>↩ Tool result · `toolu_01UhFgvsLo2rmD57riTZDW2y`</summary>

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
13	\paragraph{\cwm{} (output generation).}\footnote{We use ``code world model'' following \citet{meta2025cwm} to denote execution output prediction, distinct from world models in model-based reinforcement learning.} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Expected Failure Modes}
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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "a944e71b-870c-41f2-bfa1-67e571e53c65",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nLet $p$ denote a candidate patch and $T = \\{t_1, \\ldots, t_n\\}$ its test suite, where each $t_i$ has label $y_i \\in \\{\\text{\\textsc{Pass}}, \\text{\\textsc{Fail}}\\}$ from execution. Tests decompose into \\emph{fail-to-pass} ($T_{\\text{f2p}}$) and \\emph{pass-to-pass} ($T_{\\text{p2p}}$) subsets; a patch is correct iff $\\forall\\, t_i{:}\\ y_i = \\text{\\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.\n\n\\subsection{Verification Formulations}\n\\label{sec:formulations}\n\nLet $c_p$ denote the code context (unified diff) of patch $p$.\n\n\\paragraph{\\cls{} (per-test classification).} $f(c_p, t_i) \\rightarrow \\hat{y}_i \\in \\{\\text{\\textsc{Pass}}, \\text{\\textsc{Fail}}\\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\\hat{y}_p = \\bigwedge_{i} [\\hat{y}_i = \\text{\\textsc{Pass}}]$. Output cost: one token per test.\n\n\\paragraph{\\cwm{} (output generation).}\\footnote{We use ``code world model'' following \\citet{meta2025cwm} to denote execution output prediction, distinct from world models in model-based reinforcement learning.} $g(c_p, t_i) \\rightarrow \\hat{o}_i \\in \\Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\\hat{y}_i = \\text{\\textsc{Pass}}$ iff $\\hat{o}_i = o_i^*$.\\footnote{Exact string matching is conservative, consistent with \\citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\\sum_i |\\hat{o}_i|$ tokens.\n\n\\paragraph{\\traj{} (trajectory-level).} $h(c_p, T) \\rightarrow \\hat{y}_p \\in \\{\\text{\\textsc{Resolved}}, \\text{\\textsc{Unresolved}}\\}$ predicts a single patch verdict from all tests and provides no per-test signal. \\traj{} serves as a granularity control: \\cls{}--\\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.\n\n\\subsection{Expected Failure Modes}\n\\label{sec:failure-modes}\n\nEach formulation has characteristic failure modes that differ in their sensitivity to code complexity:\n\n\\paragraph{Generation failure modes (\\cwm{}).} The open-ended output space introduces three failure modes: (1)~\\emph{token-budget exhaustion}, where $|o_i^*| > B$ guarantees exact-match failure due to truncation; (2)~\\emph{string-value prediction errors}, where semantically equivalent outputs differing in surface form (floating-point precision, dictionary ordering) produce false negatives; and (3)~\\emph{format compliance collapse}, where the model fails to produce structured predictions entirely at high input complexity, even when the generation budget is sufficient. Under optimistic independence, a token sequence of length $L$ with per-token accuracy $q$ has correct-sequence probability $q^L$; long outputs are therefore exponentially harder to predict exactly. We adopt exact string matching following the original \\cwm{} evaluation protocol~\\citep{meta2025cwm}. Unparseable predictions default to the majority-class label (\\textsc{Pass}).\n\n\\paragraph{Classification failure modes (\\cls{}).} The single-token output space eliminates format and truncation failures but constrains the model to encode its reasoning entirely within internal representations, without the intermediate reasoning trace that generation provides. \\cls{} errors manifest as false positives or false negatives without format failures; at function level, a mild FP bias (56.5\\%) emerges, with the error direction depending on class distribution and fine-tuning dynamics.\n\n\\paragraph{Trajectory-level failure modes (\\traj{}).} By collapsing all per-test information into a single binary verdict, \\traj{} discards diagnostic granularity. When a patch fails multiple tests, the trajectory-level formulation cannot identify \\emph{which} tests fail. This limits downstream utility (e.g., targeted re-repair) but avoids per-test aggregation errors.\n\n\\paragraph{Complexity dependence.} These failure modes suggest a complexity-dependent interaction: when execution outputs are short and structured (function-level code), generation modes (1)--(2) are rarely triggered, and all formulations should perform comparably. As output length and structural complexity increase (repository-level code), generation-specific failures may compound, creating divergence. Whether this divergence reflects a fundamental property of the generation formulation or is contingent on model/tokenizer properties is an empirical question we investigate in \\S\\ref{sec:experiments}.\n\n\\subsection{Oracle Accuracy-Utility Framework}\n\\label{sec:oracle}\n\nFor a buggy patch with $k = |T_{\\text{f2p}}|$ fail-to-pass tests, a per-test verifier with recall $r$ detects the bug if it identifies at least one failing test: $P_{\\text{detect}}(k) = 1 - (1 - r)^{k_{\\text{eff}}}$, where $k_{\\text{eff}} = k / (1 + (k-1)\\rho)$ accounts for within-patch correlation via ICC $\\rho$~\\citep{shrout1979icc}. The per-test advantage over a trajectory-level baseline ($a_h$) is $\\Delta(k) = P_{\\text{detect}}(k) - a_h$, with population expectation $\\mathbb{E}[\\Delta] = \\sum_{k} P(|T_{\\text{f2p}}| = k) \\cdot \\Delta(k)$. This predicts that per-test advantage concentrates in multi-F2P-test instances and vanishes at $k{=}1$, validated in \\S\\ref{sec:experiments} and Appendix~\\ref{app:oracle}.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_012Mz24cUQjtN2evxzLibDzX`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "d05d3627-892f-4d7f-a822-2b85ff9b4eca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVTBykmq9zNh5u5794g9f1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 26412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 576
      },
      "output_tokens": 52,
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

_source line 17 · 2026-05-23T19:16:50.129Z_

<details><summary>↩ Tool result · `toolu_012Mz24cUQjtN2evxzLibDzX`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}) under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} equivalence is inconclusive after correction, but the gap narrows to 1.07\pp{} at 14B. At repository level under ${\leq}$8B LoRA, divergence reaches 18--26\pp{} ($z{=}-23.7$), consistent across families (\S\ref{sec:threats}). Preliminary 14B results (3 seeds, single family) narrow all gaps to within 1.07\pp{}; whether the repo-level divergence is formulation-inherent or capacity-contingent remains open. This contrasts with mathematical reasoning, where generative verification outperforms discriminative~\cite{hosseini2025genrm}; we hypothesize this reflects output structure---code verification requires exact-match outputs (${\sim}$477 tokens/test for \cwm{} vs.\ 1 for \cls{}), and $>$50\% of repo-level \cwm{} outputs are unparseable, in which generation becomes a format fidelity challenge absent in math. If confirmed at larger scale with cross-family replication, the 14B convergence trend would partially reconcile our findings with GenRM's generation advantage, suggesting a capacity-dependent account that bridges both domains.
5	
6	Three directions follow: (1)~complexity-aware routing; (2)~scaling to 32B+ with more seeds~\cite{meta2025cwm}; (3)~per-test diagnostics for downstream repair.
7	
8	\section*{Limitations}
9	
10	Primary findings use ${\leq}$8B LoRA fine-tuning with multi-seed replication; 14B results use a single model family (Qwen3) with 3 seeds; cross-family replication and evaluation at 32B+ are needed. The repo-level gap may diminish at 32B+ scale or with execution-trace pretraining~\cite{meta2025cwm}. All evaluation uses Python-only benchmarks; other languages may exhibit different format compliance rates. Training data uses synthetic mutation operators~\cite{andrews2005mutation,just2014mutants}; the synthetic-to-real transfer gap remains untested (Appendix~\ref{app:limitations}). Format-specific interventions (constrained decoding, output-format pretraining) may mitigate \cwm{}'s format collapse but were not evaluated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "b134577a-2105-4fe0-96db-af4030d55f6a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented the first systematic comparison of three execution-free verification formulations (\\cls{}, \\cwm{}, \\traj{}) under ${\\leq}$8B LoRA fine-tuning. At function level, \\cls{} and \\cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \\traj{} equivalence is inconclusive after correction, but the gap narrows to 1.07\\pp{} at 14B. At repository level under ${\\leq}$8B LoRA, divergence reaches 18--26\\pp{} ($z{=}-23.7$), consistent across families (\\S\\ref{sec:threats}). Preliminary 14B results (3 seeds, single family) narrow all gaps to within 1.07\\pp{}; whether the repo-level divergence is formulation-inherent or capacity-contingent remains open. This contrasts with mathematical reasoning, where generative verification outperforms discriminative~\\cite{hosseini2025genrm}; we hypothesize this reflects output structure---code verification requires exact-match outputs (${\\sim}$477 tokens/test for \\cwm{} vs.\\ 1 for \\cls{}), and $>$50\\% of repo-level \\cwm{} outputs are unparseable, in which generation becomes a format fidelity challenge absent in math. If confirmed at larger scale with cross-family replication, the 14B convergence trend would partially reconcile our findings with GenRM's generation advantage, suggesting a capacity-dependent account that bridges both domains.\n\nThree directions follow: (1)~complexity-aware routing; (2)~scaling to 32B+ with more seeds~\\cite{meta2025cwm}; (3)~per-test diagnostics for downstream repair.\n\n\\section*{Limitations}\n\nPrimary findings use ${\\leq}$8B LoRA fine-tuning with multi-seed replication; 14B results use a single model family (Qwen3) with 3 seeds; cross-family replication and evaluation at 32B+ are needed. The repo-level gap may diminish at 32B+ scale or with execution-trace pretraining~\\cite{meta2025cwm}. All evaluation uses Python-only benchmarks; other languages may exhibit different format compliance rates. Training data uses synthetic mutation operators~\\cite{andrews2005mutation,just2014mutants}; the synthetic-to-real transfer gap remains untested (Appendix~\\ref{app:limitations}). Format-specific interventions (constrained decoding, output-format pretraining) may mitigate \\cwm{}'s format collapse but were not evaluated.",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---


### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01MguefzTzTgrXwrpt3qCJnR`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "a8f2b2ef-c24e-4ce4-aa87-112e66ebea63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVTBykmq9zNh5u5794g9f1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 26412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 576
      },
      "output_tokens": 52,
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

_source line 19 · 2026-05-23T19:16:50.869Z_

<details><summary>↩ Tool result · `toolu_01MguefzTzTgrXwrpt3qCJnR`</summary>

```text
1	\appendix
2	
3	\noindent\textbf{Appendix overview.} A: Oracle resolve advantage. B: Ablation studies. C-F: Extended analysis (error complementarity, parseable accuracy, forced parsing, qualitative errors, failed interventions, mutation scaling, inference efficiency, re-repair, chain-of-thought). G: TOST sensitivity (G.1: Bayesian ROPE). H: Effect sizes. I: Holm-Bonferroni. J: Mixed-effects regression. K: Parseable bias. L: CWM convergence. M: Few-shot. N: Threats. O: Downsample. P: Use of AI assistants.
4	
5	\section{Oracle Accuracy-Utility Analysis}
6	\label{app:oracle}
7	
8	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
14	\label{tab:oracle}
15	\resizebox{\columnwidth}{!}{%
16	\setlength{\tabcolsep}{3pt}
17	\begin{tabular}{lcccc}
18	\toprule
19	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
20	\midrule
21	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
22	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
23	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
24	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
25	\midrule
26	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
31	\begin{figure}[h]
32	\centering
33	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
34	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage). Note: $y$-axis does not start at zero.}
35	\label{fig:oracle_stratified}
36	\end{figure}
37	
38	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\pp{} vs.\ 18.49\pp{} (1.7$\times$). P2P regression is negligible (1.04\% mean, 0\% median); the practical value concentrates in F2P discrimination.
39	
40	\paragraph{Sensitivity to ICC estimate.}
41	The analysis above uses ICC $= 0.191$ from function-level analysis (\S\ref{sec:equivalence}), where mean cluster size $\bar{k} \approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\S\ref{sec:repo}), yielding an effective sample size of $n_{\text{eff}} \approx 9{,}784 / 114.4 \approx 86$ independent observations~\cite{moulton1990}---still sufficient for regression but limiting precision of variance component estimates. This is a consequence of the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly and amplify the block-correlated per-test advantage at each $T$ stratum; the correction from i.i.d.\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage. The repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, which strengthens the case for per-test granularity at repository-level complexity.
42	
43	\section{Ablation Studies}
44	\label{app:ablations}
45	
46	\paragraph{LoRA rank sensitivity.}
47	All \cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \cwm{}, we train rank-32 variants (seed 42), doubling adapter parameters.
48	
49	\begin{table}[h]
50	\centering
51	\small
52	\caption{LoRA rank ablation for \cwm{} 4B (seed 42, 3 epochs, lr $= 2{\times}10^{-4}$). Rank-16 seed variance: 0.53\pp{} (seeds 42 vs.\ 456).}
53	\label{tab:rank_ablation}
54	\setlength{\tabcolsep}{4pt}
55	\begin{tabular}{lccccc}
56	\toprule
57	\textbf{Config} & \textbf{$\alpha/r$} & \textbf{Acc (\%)} & \textbf{Fail \fone{}} & \textbf{Pass \fone{}} & \textbf{$\Delta$} \\
58	\midrule
59	$r{=}16$, $\alpha{=}32$ & 2 & \textbf{87.51} & --- & --- & --- \\
60	$r{=}32$, $\alpha{=}32$ & 1 & 87.00 & 87.1 & 86.9 & $-$0.51 \\
61	$r{=}32$, $\alpha{=}64$ & 2 & 87.04 & 87.27 & 86.79 & $-$0.47 \\
62	\bottomrule
63	\end{tabular}
64	\end{table}
65	
66	Both rank-32 variants fall within the 2-seed variance of the rank-16 baseline (0.53\pp{} between seeds 42 and 456; Table~\ref{tab:rank_ablation}). The $\alpha{=}64$ variant (matching the baseline $\alpha/r{=}2$ ratio) rules out the confound that the $\alpha{=}32$ result might reflect reduced effective scaling rather than rank insensitivity. This is consistent with \cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.
67	
68	\paragraph{Majority voting.}
69	Majority voting ($K{=}3$) decreases accuracy from 87.51\% to 86.83\% ($-$0.68\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.
70	
71	\paragraph{Sequence-length ablation details.}
72	Both formulations are trained with \texttt{max\_seq\_length}$=$2,048. At inference, \cwm{} reserves \texttt{max\_new\_tokens}$=$512, leaving ${\sim}$1,536 effective input tokens; \cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\cls{} 8B at 2,048 tokens) achieves 83.04\%, only 1.44\pp{} below the 8,192-token evaluation (84.48\%), though truncation introduces 136 unparseable outputs (1.39\% of test samples). The matched-context gap (\cls{}@2,048 vs.\ \cwm{}@2,048) is 25.00\pp{} (98\% of the full 25.59\pp{} gap), confirming that input context disparity explains at most 3\% of the difference.
73	
74	\paragraph{Training data size control.}
75	\label{app:downsample}
76	To control for the training set size asymmetry between \cls{} (${\sim}$70K instances) and \traj{} (386 variant-level instances, ${\sim}$8K per-test equivalents, at repo level), we downsample \cls{} training data to match \traj{} in data volume. Downsampled \cls{} (Qwen3-4B, seed 42) achieves 80.74\% repo-level per-test accuracy, only 2.89\pp{} below the full-data \cls{} (83.63\%) and still 7.82\pp{} above \traj{} (72.92\%). The \cls{} formulation advantage is not attributable to training data volume.
77	
78	\paragraph{Few-shot prompting baselines.}
79	\label{app:few_shot}
80	We evaluate 3-shot in-context learning at repo level to test whether prompting strategy closes the gap to fine-tuned models. Table~\ref{tab:few_shot} reports both per-test and variant-level accuracy.
81	
82	\begin{table}[h]
83	\centering
84	\small
85	\caption{Repo-level prompting baselines (per-test $n{=}9{,}784$; variant-level $n{=}48$). Majority baseline: 72.96\% per-test, 54.17\% variant-level.}
86	\label{tab:few_shot}
87	\setlength{\tabcolsep}{4pt}
88	\resizebox{\columnwidth}{!}{%
89	\begin{tabular}{lcccc}
90	\toprule
91	\textbf{Model} & \textbf{0-shot (per-test)} & \textbf{3-shot (per-test)} & \textbf{3-shot (variant)} \\
92	\midrule
93	Qwen3-8B & 49.90\% & 71.61\% & 45.83\%\textsuperscript{$\ast$} \\
94	DeepSeek-6.7B & 48.54\% & 46.28\% & 45.83\%\textsuperscript{$\ast$} \\
95	\bottomrule
96	\end{tabular}}
97	
98	\vspace{2pt}
99	{\footnotesize \textsuperscript{$\ast$}Both models achieve 45.83\% by correctly classifying all 22 unresolved variants and zero resolved variants (22/48 = 45.83\%), equivalent to an always-predict-unresolved baseline. The 100\% overlap in variant-level predictions confirms complete degradation at task-relevant granularity.}
100	\end{table}
101	
102	Both models converge to exactly 45.83\% variant-level accuracy under 3-shot prompting, below majority baseline (54.17\%). Variant-level analysis reveals this is not a coincidence: both models correctly classify all 22 unresolved variants and zero resolved variants, equivalent to an always-predict-unresolved baseline with 100\% prediction overlap. Per-test accuracy diverges sharply (Qwen3-8B 71.61\% vs.\ DeepSeek 46.28\%), but this divergence is entirely superficial: Qwen3-8B predicts pass on nearly all tests, inflating per-test accuracy on a pass-heavy dataset (72.96\% pass rate) without genuine discriminative ability. Per-test metrics can thus severely misrepresent baseline capability; variant-level evaluation is necessary to detect complete degradation. Neither 0-shot nor few-shot prompting approaches fine-tuned performance (82--84\% per-test); fine-tuning is a necessary condition for repo-level verification.
103	
104	\section{Repo-Level Per-Mutation Breakdown}
105	\label{app:repo_mutation}
106	
107	Table~\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \cls{} produces 0\% unparseable outputs; all values are direct classification accuracy. \cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \S\ref{sec:repo}).
108	
109	\begin{table}[h]
110	\centering
111	\small
112	\caption{Per-mutation test accuracy (\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \cls{} 8B reports two seeds; $\Delta$ is mean 4B$\to$8B gain for \cls{}. \cwm{} 4B per-mutation overall accuracy omitted for non-gold mutations due to low parse rates (4.4--56.9\%, Table~\ref{tab:cwm_mutation_parse}); gold overall accuracy derived from parse rate 43.5\% and parseable accuracy 23.5\%.}
113	\label{tab:mutation_breakdown}
114	\resizebox{\columnwidth}{!}{%
115	\setlength{\tabcolsep}{3pt}
116	\begin{tabular}{lccccccc}
117	\toprule
118	\textbf{Mutation} & \textbf{$n$} & \textbf{CLS 4B} & \textbf{CLS 8B s42} & \textbf{CLS 8B s123} & \textbf{CWM 4B} & \textbf{CWM 8B} & \textbf{$\Delta$ CLS} \\
119	\midrule
120	gold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\
121	operator\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\
122	off\_by\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \textbf{+24.58} \\
123	return\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\
124	boundary\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\
125	\bottomrule
126	\end{tabular}}
127	\end{table}
128	
129	Table~\ref{tab:cwm_mutation_parse} shows that \cwm{} generation quality degrades from 4B to 8B across all mutation types.
130	
131	\begin{table}[h]
132	\centering
133	\small
134	\caption{\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below random binary chance (50\%) for gold at both scales.}
135	\label{tab:cwm_mutation_parse}
136	\setlength{\tabcolsep}{4pt}
137	\begin{tabular}{lcccc}
138	\toprule
139	& \multicolumn{2}{c}{\textbf{Parse Rate (\%)}} & \multicolumn{2}{c}{\textbf{Parse Acc (\%)}} \\
140	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
141	\textbf{Mutation} & \textbf{4B} & \textbf{8B} & \textbf{4B} & \textbf{8B} \\
142	\midrule
143	gold & 43.5 & 23.9 & 23.5 & 16.5 \\
144	operator\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\
145	off\_by\_one & 4.4 & 27.3 & 0.0 & 38.0 \\
146	return\_value & 48.8 & 26.9 & 27.0 & 56.9 \\
147	boundary\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\
148	\bottomrule
149	\end{tabular}
150	\end{table}
151	
152	Key findings: (1)~Gold parse rate collapses from 43.5\% to 23.9\% at 8B; the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\%: the model generates outputs that fail exact-match even for correct code. (3)~\texttt{off\_by\_one} is an anomaly: parse rate \emph{increases} from 4.4\% to 27.3\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.
153	
154	\section{Variant-Level Accuracy}
155	\label{app:variant_level}
156	
157	Table~\ref{tab:variant_level} reports variant-level accuracy ($n{=}48$) alongside per-test accuracy for all repo-level configurations. For \cls{}, the aggregation penalty (per-test $\to$ variant-level drop) ranges from 1\pp{} to 19\pp{} and is largest for models with low fail recall under the all-pass rule. \cwm{} variant-level accuracy (48--52\%) falls at or below the majority baseline, consistent with format collapse as the dominant failure mode.
158	
159	\begin{table}[h]
160	\centering
161	\small
162	\caption{Repo-level per-test vs.\ variant-level accuracy ($n{=}48$ variants). Penalty = per-test $-$ variant-level. \traj{} predicts variant outcomes directly (no aggregation). Variant-level majority baseline: 54.17\% (26/48).}
163	\label{tab:variant_level}
164	\setlength{\tabcolsep}{3pt}
165	\resizebox{\columnwidth}{!}{%
166	\begin{tabular}{llcccc}
167	\toprule
168	\textbf{Model} & \textbf{Seed} & \textbf{Per-test (\%)} & \textbf{Variant (\%)} & \textbf{Penalty (\pp{})} & \textbf{Fail Recall (\%)} \\
169	\midrule
170	\multicolumn{6}{l}{\emph{\cls{}}} \\
171	Qwen3-8B & s42 & 84.48 & 72.92 & 11.56 & 56.76 \\
172	Qwen3-8B & s123 & 85.60 & 81.25 & 4.35 & 51.44 \\
173	Qwen3-4B & s42 & 83.63 & 64.58 & 19.05 & 48.72 \\
174	DeepSeek-6.7B & s42 (e1) & 82.61 & 81.25 & 1.36 & 51.02 \\
175	DeepSeek-6.7B & s42 (e3) & 82.51 & 79.17 & 3.34 & 38.47 \\
176	DeepSeek-6.7B & s123 & 74.93 & 56.25 & 18.68 & ${\sim}$13.72 \\
177	\midrule
178	\multicolumn{6}{l}{\emph{\cwm{}}} \\
179	Qwen3-8B & s42 & 65.17 & 52.08 & 13.09 & --- \\
180	DeepSeek-6.7B$^\dagger$ & s123 & --- & 47.92 & --- & --- \\
181	\midrule
182	\multicolumn{6}{l}{\emph{\traj{}}} \\
183	Qwen3-4B & s42 & --- & 72.92 & --- & --- \\
184	Qwen3-8B & s42 & --- & 70.83 & --- & --- \\
185	DeepSeek-6.7B & 3-seed & --- & 77.08 $\pm$ 3.61 & --- & --- \\
186	\midrule
187	Majority & --- & 72.96 & 54.17 & --- & --- \\
188	\bottomrule
189	\end{tabular}}
190	\vspace{2pt}
191	
192	{\footnotesize $^\dagger$Evaluated on ${\sim}$75\% of test instances (7210--7668 of 9784). DeepSeek \traj{} Table~\ref{tab:repo_level} reports 3 seeds (42/123/456) for alignment with \cls{}/\cwm{} seed coverage; three supplementary seeds (0/789/999) yield 75.0\%, 66.7\%, 79.2\% respectively (6-seed mean 75.35 $\pm$ 5.00\%), consistent in direction.}
193	\end{table}
194	
195	\section{Training Hyperparameters}
196	\label{app:hyperparams}
197	
198	Table~\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \cls{} and \cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size, gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes), and learning rate (DeepSeek-Coder uses $2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$ for Qwen3, selected via grid search over $\{5{\times}10^{-5}, 1{\times}10^{-4}, 2{\times}10^{-4}\}$ on held-out validation loss).
199	
200	\begin{table}[h]
201	\centering
202	\small
203	\caption{Training hyperparameters for \cls{}/\cwm{} configurations. \traj{} models use lr $= 2{\times}10^{-4}$ due to the smaller training set (${\sim}$8K function-level instances vs.\ ${\sim}$70K for \cls{}/\cwm{}); other hyperparameters are shared.}
204	\label{tab:hyperparams}
205	\resizebox{\columnwidth}{!}{%
206	\begin{tabular}{ll}
207	\toprule
208	\multicolumn{2}{l}{\textbf{Shared across all configurations}} \\
209	\midrule
210	LoRA rank / alpha / dropout & 16 / 32 / 0.05 \\
211	LoRA targets & \texttt{q/k/v/o\_proj} \\
212	Optimizer & AdamW ($\beta_1{=}0.9$, $\beta_2{=}0.999$) \\
213	LR scheduler & Linear \\
214	Effective batch size & 32 \\
215	Max sequence length & 2,048 \\
216	Epochs & 3 \\
217	Precision & bf16 \\
218	Gradient checkpointing & \checkmark \\
219	Seeds (function) & \{42, 123, 456, 789, 0\}\textsuperscript{$b$} \\
220	Seeds (repo) & \{42, 123, 456\}\textsuperscript{$c$} \\
221	\bottomrule
222	\end{tabular}}
223	
224	\vspace{6pt}
225	
226	\resizebox{\columnwidth}{!}{%
227	\begin{tabular}{lccc}
228	\toprule
229	\multicolumn{4}{l}{\textbf{Model-family--specific parameters}} \\
230	\midrule
231	& \textbf{Qwen3-4B} & \textbf{Qwen3-8B} & \textbf{DS-6.7B} \\
232	\midrule
233	Learning rate & 5e-5 & 5e-5 & 2e-4 \\
234	Weight decay & 0.01 & 0.01 & 0.0 \\
235	Warmup ratio & 0.05 & 0.05 & 0.1 \\
236	Batch / grad.\ accum.\ (\cls{}) & 2 / 16 & 1 / 32 & 2 / 16 \\
237	Batch / grad.\ accum.\ (\cwm{}) & 1 / 32 & 1 / 32 & 1 / 32 \\
238	Training samples & 70,748 & 70,748 & 67,343--70,748\textsuperscript{$a$} \\
239	\bottomrule
240	\end{tabular}}
241	
242	\vspace{2pt}
243	{\footnotesize $^a$DeepSeek \cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \S\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\ref{tab:repo_level} caption for per-model counts.}
244	\end{table}
245	
246	\paragraph{Data processing.} DeepSeek CWM seeds use \texttt{train\_unified.py}, which drops samples exceeding \texttt{max\_seq\_length} (3{,}405 of 70{,}748 samples, 4.8\%). Qwen CWM seeds use \texttt{train\_repo\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\sim}$12{,}627 vs.\ ${\sim}$13{,}266 for DeepSeek, ${\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.
247	
248	\paragraph{Prompt templates.} Prompt templates for all formulations (\cls{}, \cwm{}, \traj{}) are provided in the code repository. \cls{} uses a binary classification template (``Does this test pass or fail?''); \cwm{} uses an execution simulation template (``What is the output of this test?''); \traj{} uses a variant-level verdict template (``Is this patch resolved or unresolved?'').
249	
250	\paragraph{Mutation operators.} We use five mutation types: (1)~\emph{gold}: unmodified code (all tests pass); (2)~\emph{operator\_swap}: replaces comparison or arithmetic operators (e.g., \texttt{<} $\to$ \texttt{<=}); (3)~\emph{off\_by\_one}: shifts loop bounds or array indices by $\pm$1; (4)~\emph{return\_value}: modifies return statements (e.g., negating a boolean, changing a constant); (5)~\emph{boundary\_removal}: removes conditional guards or boundary checks. Mutation operators were applied using AST-level transformation; variants that did not alter any test outcome were discarded.
251	
252	\paragraph{Compute budget.}
253	All experiments were conducted on NVIDIA RTX 5090 GPUs. Training time is approximately 1.5 hours per run for 4B models and 2 hours for 8B models. Total compute budget: ${\sim}$370 GPU-hours across 223 completed runs (135 successful, 88 failed/killed; ${\sim}$46 unique configurations including seeds, formulations, model sizes, and ablations).
254	
255	\section{Prompt Templates}
256	\label{app:prompts}
257	
258	We show representative prompt examples for each formulation. All examples use the same input instance for comparability.
259	
260	\paragraph{CLS (per-test classification).}
261	{\footnotesize\begin{verbatim}
262	System: You are a code verifier.
263	Given a code patch and a test name,
264	predict whether the test will pass
265	or fail when run against the
266	patched code.
267	
268	User:
269	## Patch (git diff)
270	&lt;patch content> [... truncated]
271	## Test
272	test_boundary_check
273	Will this test pass or fail?
274	
275	Target: pass
276	\end{verbatim}}
277	
278	\paragraph{CWM (execution simulation).}
279	{\footnotesize\begin{verbatim}
280	System: You are a code execution
281	simulator. Given a code snippet and
282	a test case, predict the execution
283	result.
284	
285	User:
286	## Code
287	&lt;code content> [... truncated]
288	## Test
289	test_boundary_check
290	What is the execution result?
291	
292	Target: PASS: test completed
293	successfully
294	\end{verbatim}}
295	
296	\paragraph{TRAJ (trajectory scoring).}
297	{\footnotesize\begin{verbatim}
298	System: You are a code repair
299	verifier. Given the code patch and
300	test summary, predict whether all
301	tests pass (resolved) or any test
302	fails (unresolved).
303	
304	User:
305	[Code]
306	&lt;patch content> [... truncated]
307	[Test Summary]
308	&lt;all test names and descriptions>
309	
310	Target: resolved
311	\end{verbatim}}
312	
313	\cls{} and \cwm{} share the same input format (one code--test pair per instance); \cls{} produces a single token (\texttt{pass}/\texttt{fail}), while \cwm{} generates a variable-length execution trace. \traj{} receives all tests concatenated and produces a single token (\texttt{resolved}/\texttt{unresolved}).
314	
315	
316	\section{Val-Test Mutation Type Distribution}
317	\label{app:mutation_distribution}
318	
319	Table~\ref{tab:mutation_distribution} reports the mutation type composition of the repo-level validation and test sets. The most notable shift is \texttt{operator\_swap}, which nearly doubles from val (19.1\%) to test (34.3\%), while \texttt{off\_by\_one} shrinks from 10.0\% to 1.9\%.
320	
321	\begin{table}[h]
322	\centering
323	\small
324	\caption{Repo-level mutation type distribution: validation vs.\ test set, with per-type \cls{} accuracy at two model sizes (seed 42). Shift = test\% $-$ val\%.}
325	\label{tab:mutation_distribution}
326	\setlength{\tabcolsep}{3pt}
327	\resizebox{\columnwidth}{!}{%
328	\begin{tabular}{lccccc}
329	\toprule
330	\textbf{Mutation Type} & \textbf{Val (\%)} & \textbf{Test (\%)} & \textbf{Shift} & \textbf{\cls{} 4B} & \textbf{\cls{} 8B} \\
331	\midrule
332	gold & 45.2 & 47.4 & +2.2 & 98.3 & 96.2 \\
333	operator\_swap & 19.1 & 34.3 & +15.2 & 78.9 & 81.4 \\
334	boundary\_removal & 15.0 & 10.7 & $-$4.3 & 46.9 & 46.9 \\
335	return\_value & 10.7 & 5.7 & $-$5.0 & 68.0 & 75.4 \\
336	off\_by\_one & 10.0 & 1.9 & $-$8.1 & 58.5 & 86.9 \\
337	\bottomrule
338	\end{tabular}}
339	\end{table}
340	
341	The \texttt{operator\_swap} shift is the primary source of val-test distribution mismatch. Since \cls{} achieves moderate accuracy on this type (78.9--81.4\%), the over-representation in the test set does not systematically bias overall accuracy estimates in either direction. Two boundary observations are notable: (1)~\texttt{boundary\_removal} represents a scale-invariant difficulty ceiling at ${\sim}$47\% across both model sizes: this mutation type resists capacity scaling; (2)~\texttt{off\_by\_one} shows the largest scaling gain (+28.4\pp{}, 58.5\%$\to$86.9\%) but its small test share (1.9\%) limits its contribution to overall accuracy differences across scales.
342	
343	\section{Qualitative Error Analysis}
344	\label{app:qualitative}
345	
346	To complement the quantitative divergence reported in \S\ref{sec:repo}, we examine representative errors from each formulation at repository level.
347	
348	\paragraph{\cwm{} failure modes.}
349	Two patterns account for the majority of unparseable \cwm{} outputs on Qwen3. (1)~\emph{Task misunderstanding}: the model generates a complete simulated test runner log (test names, timing, summary lines) rather than a pass/fail verdict. For instance, on \texttt{django\_\_django-14315}, the model outputs a fabricated 1,248-token Django test execution trace with hallucinated test names that do not exist in the target file. The model confuses ``predict test outcome'' with ``simulate test execution environment.'' (2)~\emph{Autoregressive degeneration}: the model enters a repetitive loop (e.g., repeating \texttt{from \_pytest.config import \_parse\_pytest\_args} until truncation at 4,542 tokens). Both patterns produce zero usable signal and default to the majority-class label. This explains why unparseable predictions carry higher accuracy than parseable ones (\S\ref{sec:repo}).
350	
351	\paragraph{\cls{} failure modes.}
352	\cls{} errors concentrate in two categories requiring multi-step reasoning. False positives arise from \emph{cross-concern value propagation}: a boundary removal mutation in \texttt{pytest} converts a guarded attribute access (\texttt{if xfailed and not xfailed.run}) to \texttt{if True:}, causing a NoneType error on tests exercising unrelated skip marks. The model fails to trace the None path through the pytest hook lifecycle. False negatives arise from \emph{mathematical equivalence}: on \texttt{HumanEval/130} (Tribonacci variant), the model predicts failure for correct code because verifying the self-referential recurrence requires algebraic substitution rather than syntactic inspection. This single problem accounts for 17\% of all function-level false negatives.
353	
354	\paragraph{Complementarity.}
355	These failure patterns operate at different levels: \cwm{} fails at the format level (producing no usable signal), while \cls{} fails at the reasoning level (producing a confident but incorrect binary verdict). Both formulations are FP-dominant (over-predict failure), but \cwm{}'s higher FP rate (70.3\% vs.\ 56.5\%) means it over-predicts failure on instances \cls{} correctly classifies, producing partial complementarity (oracle combination: 90.63\%; \S\ref{app:extended_analysis}, paragraph a).
356	
357	\section{Extended Analysis}
358	\label{app:extended_analysis}
359	
360	\paragraph{Function-level CWM metric robustness.}
361	At function level, \cwm{} outputs are short status strings (mean ${\sim}$5--15 tokens). The unparseable rate is only 1.39\%, and default-to-pass bias is $<$1\pp{}---well below the SESOI threshold. Exact string matching is appropriate for these short, structured outputs; semantic-but-format-different matches are rare given the constrained output space.
362	
363	\paragraph{(a) Error complementarity.}
364	\cls{} and \cwm{} are both FP-dominant at function level but at different rates, producing partial complementarity. Among \cls{} errors (seed 42), 56.5\% are false positives (PASS $\to$ FAIL); among \cwm{} errors, 70.3\% are false positives. Both formulations over-predict failure, but \cwm{}'s stronger FP bias means it incorrectly rejects passing tests that \cls{} correctly accepts. An oracle combination achieves 90.63\% accuracy (1713/1890 correct, 177 both-wrong; +2.80\pp{} over the best single formulation, \cls{} 87.83\%; single-seed estimate, seed 42). The complementarity arises from different \emph{degrees} of fail-bias rather than opposite error directions: \cwm{}'s generation bottleneck produces aggressive failure predictions, while \cls{}'s single-token output is more calibrated. Ensemble approaches exploiting this degree difference are a natural direction.
365	
366	\paragraph{(b) CWM error mode breakdown.}
367	Among unparseable \cwm{} outputs (Qwen3, repo-level), 76.9\% contain no execution keywords; 22.9\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\%); repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-level one.
368	
369	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
370	Relaxed matching (tolerating format deviations, L0--L4) \emph{decreases} \cwm{} accuracy: 58.04\%$\to$56.98\% (seed 42) and 59.09\%$\to$55.91\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\%), which outperforms the model's own parseable predictions (38--43\%). The divergence widens from 26\pp{} to 27\pp{} under relaxed matching. This rules out the hypothesis that parsing strictness inflates the observed gap. Constrained decoding~\cite{willard2023outlines} could enforce format compliance but would not address the semantic accuracy deficit among parseable outputs. An accidental training artifact provides further evidence: a \cwm{} model inadvertently trained on function-level (\cls{}-format) data achieved 86.05\% accuracy with 0\% unparseable outputs at repo level---recovering \cls{}-level performance. This confirms that the repo-level \cwm{} degradation stems entirely from trace generation complexity, not from the underlying verification task.
371	
372	\paragraph{(d) Variance compression.}
373	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and \traj{} (0.97\pp{}) at function level. If \cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
374	
375	\paragraph{(e) Per-test precision and recall.}
376	\cls{} achieves fail \fone{} 87.59\% (precision 86.20\%, recall 89.04\%) at seed 42.% derived from overlap analysis (error_overlap_matched_seed.json); FP=130, FN=100, TP=848, TN=812
377	Multi-F2P instances (6--10 tests) reach 96.3\% accuracy, consistent with the oracle finding that per-test granularity is most valuable for complex instances.
378	
379	\paragraph{(f) Block correlation.}
380	Within-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\times$ more all-correct problems than i.i.d.\ expectation). All statistical tests use clustered bootstrap accordingly.
381	
382	\paragraph{(g) Failed interventions.}
383	We systematically tested four interventions targeting different hypothesized causes of \cwm{} repo-level degradation; all failed:
384	
385	\begin{itemize}[leftmargin=*,itemsep=1pt,topsep=2pt]
386	\item \textbf{Capacity (rank 32, $\alpha{=}64$):} $-$0.47\pp{}, within seed variance (\S\ref{app:ablations}).
387	\item \textbf{Majority voting ($K{=}3$):} $-$0.68\pp{}; 93.3\% unanimous, net flips negative (\S\ref{app:ablations}).
388	\item \textbf{Relaxed matching (L0--L4):} $-$1.06\pp{}; default-pass outperforms parseable predictions (paragraph~(c) above).
389	\item \textbf{Model scaling (4B$\to$8B):} parseable accuracy decreases (42.88\%$\to$38.52\%) while unparseable rate rises (53.7\%$\to$73.8\%); gain is a default-assignment artifact (\S\ref{sec:repo}).
390	\end{itemize}
391	
392	\noindent Each intervention targets a distinct alternative explanation (insufficient capacity, random noise, parsing strictness, model scale); the uniform failure across all four confirms the bottleneck is formulation-level---output space complexity at repo level exceeds what ${\leq}$8B generation models can handle, independent of these surface-level factors.
393	
394	\paragraph{(h) Per-mutation scaling patterns.}
395	Scaling benefits are highly non-uniform across mutation types (Table~\ref{tab:mutation_breakdown}). \texttt{off\_by\_one} shows the largest \cls{} scaling gain: 58.5\% (4B) to 86.9\% (8B, $+$28.4\pp{}). In contrast, \texttt{boundary\_removal} is scale-invariant at ${\sim}$47\% across both sizes, which marks an intrinsic difficulty ceiling. For \cwm{}, gold mutation parse rate collapses from 43.5\% (4B) to 23.9\% (8B) despite being the simplest target: generation capability degrades even for trivially correct code at larger scale within Qwen3. The val-test mutation type distribution differs notably (\texttt{operator\_swap} shifts from 19.1\% to 34.3\%; Table~\ref{tab:mutation_distribution}), but this shift does not systematically bias overall accuracy because \cls{} performance on \texttt{operator\_swap} (78.9--81.4\%) is close to the overall mean.
396	
397	\paragraph{(i) Inference efficiency.}
398	\cls{} achieves 217$\times$ higher throughput than \cwm{} at repo level (853 vs.\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\cls{}) vs.\ 16.3s (\cwm{}). At the observed unparseable rate of 73.8\% (8B), the majority of \cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This \cls{}--\cwm{} efficiency gap is an inherent property of the formulation difference (1 vs.\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.
399	
400	The \cls{}--\traj{} efficiency comparison is more nuanced, because \cls{} makes one call per test while \traj{} makes one call per instance. Per-call, \cls{} is 20--138$\times$ faster (depending on input length: 47ms for short contexts vs.\ 2,632ms for \traj{}). However, the per-instance effective speedup depends on test count $|T|$: at function level ($|T| \approx 2.3$), \cls{} is ${\sim}$24$\times$ faster (108ms vs.\ 2,632ms per instance); at repo level ($|T| \approx 12.3$, ${\sim}$70ms/call with longer inputs), \cls{} is ${\sim}$3$\times$ faster (861ms vs.\ 2,631ms). A crossover exists at $|T| \approx 50$ tests, beyond which \traj{}'s single-call amortization dominates. This boundary condition is informative for deployment: \cls{} is strongly preferred for function-level and moderate repo-level test suites, while extremely large test suites ($>$50 tests per instance) favor trajectory-level efficiency despite its coarser diagnostic signal.
401	
402	\paragraph{(j) Re-repair pilot.}
403	We tested whether per-test diagnostic feedback improves downstream repair. A Qwen3-8B repair agent received either per-test diagnostic signals (which specific tests failed and why) or binary accept/reject feedback, evaluated on 44 SWE-bench Verified instances. The diagnostic condition achieved accuracy no higher than the binary baseline ($A_1 = 52.3\%$, $p = 0.42$, effect size $\approx 0$). Per-test diagnostic information does not automatically translate to repair improvements at this scale. The negative result may reflect insufficient agent capability to exploit fine-grained feedback, insufficient sample size (at $n = 44$, statistical power is ${\sim}$0.3 for a medium effect size), or a genuine limitation of the diagnostic-to-repair translation.
404	
405	\paragraph{(k) Relationship to chain-of-thought verification.}
406	\cwm{} is structurally a chain-of-thought verifier: the model generates an execution trace token by token and derives its PASS/FAIL verdict from the final trace state. If intermediate reasoning improved verification, \cwm{} should outperform the reasoning-free \cls{} baseline. At function level, no such advantage materialises: \cwm{} and \cls{} are statistically equivalent (TOST $p{=}0.007$, $\pm$2\pp{} margin; \S\ref{sec:equivalence}), indicating that the additional trace generation provides no accuracy benefit over direct binary classification. At repo level, the chain-of-thought mechanism actively \emph{hurts}: trace generation triggers format collapse (53--74\% unparseable), and even parseable traces yield accuracy below the majority baseline (38--43\% vs.\ 72.96\%; paragraph~(c)). Four targeted interventions fail to rescue the generation pathway (paragraph~(g)). Within the ${\leq}$8B LoRA regime, chain-of-thought--style verification does not outperform direct classification for execution prediction. Whether execution-trace pretraining at larger scale~\cite{meta2025cwm} changes this conclusion remains the primary open question (\S\ref{sec:threats}).
407	
408	\section{TOST Margin Sensitivity}
409	\label{app:tost_sensitivity}
410	
411	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence $p$-value as a function of the equivalence margin, computed on the 5-seed variant-level \cls{}--\cwm{} comparison (gap $= 1.24$\pp{}, 523 variants, 114 clusters, clustered bootstrap).
412	
413	\begin{table}[h]
414	\centering
415	\small
416	\caption{TOST margin sensitivity for \cls{}--\cwm{} variant-level equivalence (5 seeds, 523 variants, 114 clusters). The smallest margin achieving equivalence at $\alpha = 0.05$ is $\pm$1.52\pp{}.}
417	\label{tab:tost_sensitivity}
418	\setlength{\tabcolsep}{4pt}
419	\begin{tabular}{ccc}
420	\toprule
421	\textbf{Margin ($\pm$\pp{})} & \textbf{$p$-value} & \textbf{Equivalent ($\alpha{=}0.05$)?} \\
422	\midrule
423	1.0 & $\gg$0.05 & No \\
424	1.5 & 0.054 & No (borderline) \\
425	\textbf{1.52} & ${\sim}$\textbf{0.05} & \textbf{Smallest margin} \\
426	1.71 & 0.027 & Yes \\
427	2.0 & 0.007 & Yes \\
428	3.0 & $4.6{\times}10^{-5}$ & Yes \\
429	5.0 & $\ll$0.001 & Yes \\
430	\bottomrule
431	\end{tabular}
432	\end{table}
433	
434	The minimum equivalence margin is $\pm$1.52\pp{}, 0.48\pp{} below our pre-specified $\pm$2\pp{} threshold. The $\pm$2\pp{} threshold was set based on deployment relevance rather than observed data: at function-level accuracy (85--88\%), a 2\pp{} per-test difference corresponds to ${\sim}$38 additional errors across 1,890 tests (${\sim}$2--3 problems out of 114), comparable in magnitude to between-seed standard deviation (0.37--0.97\pp{}) and checkpoint selection noise ($<$1\pp{}). Differences within this range do not reliably distinguish formulations from training noise in pipeline selection decisions. For \cls{}--\traj{}, the TOST at $\pm$2\pp{} yields $p{=}0.025$, nominally significant but not surviving Holm-Bonferroni correction at $k{=}5$ (adjusted $p{=}0.075$; Table~\ref{tab:holm}). The one-sided decomposition reveals the binding constraint: $p_{\text{upper}}{=}0.005$ ($\Delta < {+}2$\pp{} is well-confirmed) while $p_{\text{lower}}{=}0.025$ ($\Delta > {-}2$\pp{}) limits the overall TOST, consistent with \cls{} having mildly higher accuracy.
435	
436	\paragraph{Robustness: seed-level vs.\ clustered bootstrap TOST.}
437	The primary TOST $p$-values use seed-level paired analysis (df${=}$4), treating each training seed as the unit of replication (\S\ref{sec:setup}). Under problem-level clustered bootstrap (resampling 114 problem clusters, 10K iterations), the \cls{}--\traj{} raw TOST $p$ decreases to ${\sim}$0.007 (Holm-adjusted $p{\approx}0.021$), which would confirm equivalence. We report the more conservative seed-level result ($p{=}0.025$, adjusted $p{=}0.075$) as primary, since training seeds are the true unit of replication; problem-level bootstrap pools within-seed observations and may understate between-seed uncertainty. For \cls{}--\cwm{}, both methods confirm equivalence ($p \leq 0.010$), so the choice does not affect conclusions.
438	
439	\subsection{Bayesian ROPE Analysis}
440	\label{app:bayesian_rope}
441	To complement the frequentist TOST, we conduct a Bayesian equivalence analysis using a paired $t$-test with Jeffreys prior~\cite{kruschke2013bayesian,kruschke2018rejecting}. The marginal posterior for the mean accuracy difference follows a $t$-distribution with $n{-}1$ degrees of freedom. For \cls{}--\cwm{}, the posterior probability within the $\pm$2\pp{} ROPE is $P(\text{ROPE}) = 0.975$, and the 95\% highest density interval (HDI $= [{+}0.10, {+}2.00]$\,pp) falls entirely inside the ROPE, confirming equivalence under both continuous and HDI-based decision criteria. For \cls{}--\traj{} at per-test level, $P(\text{ROPE}) = 0.542$ (inconclusive; 95\% HDI $= [{+}0.35, {+}3.52]$\,pp extends beyond the ROPE), consistent with the TOST inconclusive result after Holm correction ($p_{\text{adj}} = 0.075$). At variant level, \cls{}--\traj{} equivalence is supported by the Bayesian criterion ($P(\text{ROPE}) = 0.970$, HDI $= [{-}2.00, {+}1.03]$\,pp), but the frequentist TOST remains inconclusive after Holm-Bonferroni correction ($p_{\text{adj}} = 0.075$; Table~\ref{tab:holm}). This discrepancy reflects differing treatments of multiplicity: Bayesian ROPE evaluates each comparison independently, while Holm correction penalizes across all $k{=}5$ primary tests. For \cls{}--\cwm{}, both frameworks agree (TOST $p_{\text{adj}}{=}0.028$, $P(\text{ROPE}){=}0.975$); for \cls{}--\traj{} per-test, both are inconclusive. We conservatively follow the Holm-corrected TOST in the main text and report \cls{}--\traj{} equivalence as inconclusive.
442	
443	\paragraph{14B scaling evidence.} At 14B (3 seeds), the \cls{}--\cwm{} gap narrows to 0.43\pp{} and the \cls{}--\traj{} gap to 1.07\pp{}, both within the $\pm$2\pp{} margin. Seed-level TOST (df${=}$2) is inconclusive for equivalence in both pairs ($p{=}0.076$ for \cls{}--\cwm{}, $p{=}0.187$ for \cls{}--\traj{}), reflecting the severe power limitation of 3-seed comparisons (power ${\sim}$0.08 at $\pm$2\pp{} margin with df${=}$2). Bayesian ROPE provides moderate support: $P(\text{ROPE}){=}0.887$ for \cls{}--\cwm{} and $P(\text{ROPE}){=}0.780$ for \cls{}--\traj{}. Under problem-level clustered bootstrap, both comparisons reach significance ($p{=}0.0006$ and $p{=}0.043$ respectively), but this analysis treats within-seed observations as exchangeable, potentially understating between-seed uncertainty. The monotonic gap reduction (3.11\pp{} at 4B $\to$ 2.24\pp{} at 8B $\to$ 1.07\pp{} at 14B) favors a capacity-dependent convergence interpretation, though formal confirmation at seed level requires more training seeds.
444	
445	
446	\section{Variant-Level Effect Sizes}
447	\label{app:power}
448	
449	Table~\ref{tab:variant_power} reports variant-level bootstrap confidence intervals for the repo-level formulation comparisons ($n{=}48$ variants). Following Hoenig and Heisey~\cite{hoenig2001}, we report minimum detectable effect (MDE) rather than post-hoc observed power.
450	
451	\begin{table}[h]
452	\centering
453	\small
454	\caption{Variant-level bootstrap analysis ($n{=}48$). \cls{}--\cwm{} uses paired bootstrap (same variants, same seed); \cls{}--\traj{} uses unpaired bootstrap (per-variant \traj{} predictions not archived for pairing). MDE at $n{=}48$: ${\sim}$25\pp{}.}
455	\label{tab:variant_power}
456	\setlength{\tabcolsep}{3pt}
457	\resizebox{\columnwidth}{!}{%
458	\begin{tabular}{llccc}
459	\toprule
460	\textbf{Comparison} & \textbf{Config} & \textbf{$\Delta$ (\pp{})} & \textbf{95\% CI} & \textbf{$p$} \\
461	\midrule
462	\multicolumn{5}{l}{\emph{\cls{} vs.\ \cwm{} (paired)}} \\
463	& Qwen3-8B & +29.17 & [10.42, 47.92] & 0.003 \\
464	& DeepSeek-6.7B & +35.42 & [18.75, 50.05] & ${<}$0.001 \\
465	\midrule
466	\multicolumn{5}{l}{\emph{\cls{} vs.\ \traj{} (unpaired)}} \\
467	& Qwen3-4B & $-$4.17 & wide & 0.740 \\
468	& Qwen3-8B & +8.33 & wide & 0.385 \\
469	& DeepSeek-6.7B & 0.00 & wide & 1.000 \\
470	\bottomrule
471	\end{tabular}}
472	\end{table}
473	
474	At $n{=}48$, the MDE is ${\sim}$25\pp{}. The \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \cls{}--\traj{} gaps ($<$10\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\S\ref{sec:equivalence}).
475	
476	The \cls{}--\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \traj{} per-variant predictions were not archived in a format that permits pairing. The \cls{}--\cwm{} paired comparison uses \cls{} s123 vs.\ \cwm{} s42 (different seeds), but the CI lower bound of 10.42\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\pp{}).
477	
478	
479	\section{Multiple Comparison Correction}
480	\label{app:holm}
481	
482	Table~\ref{tab:holm} applies Holm-Bonferroni correction~\cite{holm1979} to the five primary statistical comparisons across this study ($k{=}5$, family-wise $\alpha{=}0.05$).
483	
484	\begin{table}[h]
485	\centering
486	\small
487	\caption{Holm-Bonferroni correction for primary comparisons ($k{=}5$). Comparisons ranked by raw $p$-value; each tested against $\alpha / (k - \text{rank} + 1)$.}
488	\label{tab:holm}
489	\setlength{\tabcolsep}{3pt}
490	\resizebox{\columnwidth}{!}{%
491	\begin{tabular}{clcccc}
492	\toprule
493	\textbf{Rank} & \textbf{Comparison} & \textbf{Raw $p$} & \textbf{Factor} & \textbf{Adj $p$} & \textbf{Sig.?} \\
494	\midrule
495	1 & Repo: \cls{} vs \cwm{} & 0.003 & $\times$5 & 0.015 & \checkmark \\
496	2 & Func: \cls{} vs \cwm{} (TOST $\pm$2\pp{}) & 0.007 & $\times$4 & 0.028 & \checkmark \\
497	3 & Func: \cls{} vs \traj{} (TOST $\pm$2\pp{}) & 0.025 & $\times$3 & 0.075 & --- \\
498	4 & Repo: \cwm{} vs \traj{} & 0.039 & $\times$2 & 0.078 & --- \\
499	5 & Repo: \cls{} vs \traj{} & 0.385 & $\times$1 & 0.385 & --- \\
500	\bottomrule
501	\end{tabular}}
502	\end{table}
503	
504	The two core claims survive correction: the repo-level \cls{}--\cwm{} divergence (adjusted $p{=}0.015$) and function-level \cls{}--\cwm{} equivalence (adjusted $p{=}0.028$). The function-level \cls{}--\traj{} equivalence does not survive correction (adjusted $p{=}0.075$). Under problem-level clustered bootstrap, the raw TOST $p$ decreases to ${\sim}$0.007 (adjusted $p{\approx}0.021$), which would confirm equivalence; we report the more conservative seed-level result ($p{=}0.025$) as primary, since training seeds are the true unit of replication.
505	
506	\section{Mixed-Effects Regression}
507	\label{app:interaction}
508	
509	We fit mixed-effects linear probability models (LPM) with heteroskedasticity-robust standard errors (HC1) to test the formulation$\times$complexity interaction formally~\cite{moulton1990}. We choose LPM because coefficients are directly interpretable as probability differences (percentage points), consistent with the reporting units in the main text; at these sample sizes ($n{\approx}56$K cross-complexity, repo-level pooled cross-model) and base rate range (0.6--0.9), LPM and logistic regression yield concordant conclusions for all primary effects~\cite{angrist2009mostly} (confirmed below).
510	
511	\paragraph{Cross-complexity model (DeepSeek-Coder).} \texttt{correct $\sim$ formulation $\times$ complexity + (1|problem\_id)}, $n{=}56{,}480$ observations (\cls{} + \cwm{} $\times$ function + repo), 139 problem clusters. The \cwm{} main effect at function level is non-significant ($\hat{\beta}{=}-0.002$, $z{=}-0.25$, $p{=}0.805$); the \cwm{}$\times$repo interaction is highly significant ($\hat{\beta}{=}-0.219$, $z{=}-23.7$, $p{<}0.001$). \cwm{} and \cls{} are statistically indistinguishable at function level ($\Delta{=}-0.2$\pp{}, $p{=}0.805$) but diverge by 22\pp{} at repo level, confirming the complexity-dependent divergence is not an artifact of aggregation.
512	
513	\paragraph{Repo-level cross-model model.} \texttt{correct $\sim$ formulation $\times$ model + (1|problem\_id)}, both model families, repo level only. \cwm{} deficit: $\hat{\beta}{=}-0.22$ ($-$22\pp{}, $z{=}-64.4$, $p{<}0.001$). Model effect: +1.1\pp{} for Qwen3 ($z{=}3.1$, $p{=}0.002$ in LPM; not significant under GEE, $p{=}0.449$). Formulation$\times$model interaction: +1.6\pp{} less \cwm{} degradation on Qwen3 ($z{=}2.8$, $p{=}0.006$ in LPM; not significant under GEE, $p{=}0.860$). Formulation dominates the predictable variance; model identity is directionally positive but specification-dependent. The 25-cluster random intercept structure limits effective degrees of freedom for the random effects; inferences on fixed effects (formulation, complexity) are robust as they pool across the full observation count.
514	
515	\paragraph{Logistic regression robustness check.} To verify that LPM conclusions are not artifacts of the linear link function, we fit GEE logistic regression (binomial family, exchangeable working correlation, robust sandwich standard errors) to the same data. For the cross-complexity model, the \cwm{} main effect at function level has OR$=$0.98 (95\% CI [0.86, 1.12], $p{=}0.771$) and the \cwm{}$\times$repo interaction has OR$=$0.31 ([0.15, 0.65], $p{=}0.002$). Average marginal effects are $-$0.2\pp{} (function) and $-$21.6\pp{} (repo), matching LPM coefficients within 0.3\pp{}. For the cross-model model, the \cwm{} deficit has OR$=$0.30 ([0.15, 0.63], $p{=}0.001$, AME$=$\,$-$21.1\pp{}). Direction, magnitude, and significance of all primary effects are concordant between LPM and logistic regression; minor discrepancies in secondary effects (model identity, formulation$\times$model interaction: $p{=}0.449$ and $p{=}0.860$ under GEE vs.\ $p{=}0.002$ and $p{=}0.006$ under LPM) reflect the GEE's more conservative cluster-robust inference with $k{=}25$ clusters. The discrepancy in secondary effects reflects cluster count: the cross-complexity model ($k{=}139$) yields reliable sandwich SEs, while the cross-model model ($k{=}25$) falls below the $k{\geq}40$ threshold recommended for stable cluster-robust inference~\cite{cameron2008bootstrap}.
516	
517	\section{CWM Parseable Bias Analysis}
518	\label{app:parseable_bias}
519	
520	The default-to-pass assignment for unparseable \cwm{} outputs is not random with respect to instance difficulty. Unparseable instances have significantly higher pass rates than parseable ones (74.6\% vs.\ 68.3\%, $\chi^2$ $p = 5.9 \times 10^{-10}$), and \cls{} models achieve higher accuracy on unparseable instances (86.4\% vs.\ 79.1\%, $p = 3.3 \times 10^{-18}$). This indicates that \cwm{}'s parsing failures concentrate on simpler, pass-heavy instances where the majority-class default happens to be correct more often. Cross-model Jaccard overlap of unparseable instance sets is 0.46, confirming this pattern is instance-driven (specific inputs consistently cause parsing failure across models) rather than stochastic. The net effect is that \cwm{}'s reported accuracy is inflated by default-correct assignments on easy instances, while its effective discriminative accuracy on harder instances is substantially lower than the aggregate figure suggests.
521	
522	
523	\section{Threats to Validity (Full Analysis)}
524	\label{app:threats}
525	
526	We identify five potential confounds and assess their impact on our conclusions.
527	
528	\paragraph{Checkpoint selection.} Val-based selection is unavailable for runs with NaN validation loss (DeepSeek \cwm{} repo-level runs, DeepSeek \cls{} s123), which default to the final epoch checkpoint. A checkpoint ablation on Qwen3-8B \cls{} s42 quantifies this confound: epoch~1 (ckpt-2200) achieves 85.34\%, val-selected (ckpt-3600) 84.48\%, and final epoch (ckpt-6633) 85.29\%---a $<$1\pp{} range. The val-selected checkpoint is the lowest, indicating no upward bias from checkpoint selection. The Qwen3-8B \traj{} comparison (epoch 2: 72.92\% vs.\ epoch 3: 70.83\%) shows a slightly larger ${\sim}$2\pp{} shift. For \cwm{}, the convergence analysis (Appendix~\ref{app:cwm_convergence}) shows eval loss at the final epoch is 1.8$\times$ its minimum; however, early-stopped checkpoints retain high unparseable rates, leaving the qualitative ranking unchanged.
529	
530	\paragraph{\cwm{} convergence analysis.}
531	\label{app:cwm_convergence}
532	Qwen3-8B \cwm{} repo-level eval loss reaches its minimum within ${\sim}$5\% of training (step 300--400 of 6{,}633) and increases monotonically thereafter, with no plateau or recovery (Table~\ref{tab:cwm_convergence}). This pattern is consistent across all three seeds, confirming systematic overfitting to trace generation rather than stochastic variation. The final-epoch eval loss is ${\sim}$1.8$\times$ the optimal value. By contrast, function-level \cwm{} achieves \cls{}-equivalent accuracy (TOST $p{=}0.007$) with the same training recipe, indicating that the overfit is specific to repo-level output complexity. Cross-model validation: a DeepSeek-Coder early-stopped checkpoint (s123, epoch~1) achieves 75.45\% versus 57.31\% at epoch~3 (s123; +18.14\pp{}), but retains 66.4\% unparseable rate, confirming that format collapse emerges early and is not a late-training artifact. No epoch-level checkpoint is available for Qwen3 CWM (only step-level checkpoints at steps 300/400 and late steps ${\geq}$5800; continuous epoch checkpointing was not enabled for this training run). The convergence analysis (Table~\ref{tab:cwm_convergence}) shows eval loss minimum at step 300--400 across all three Qwen3 seeds, consistent with DeepSeek-Coder's epoch-1 improvement, providing cross-model evidence that the overtraining pattern generalizes. An early checkpoint (step 400, ${\sim}$6.5\% of training, s42) yields 65.17\% repo-level accuracy with 63.7\% unparseable rate---comparable to or below final-epoch performance (66.93--67.33\% accuracy, 60.4--63.9\% unparseable; s123/s456 at step 6633). This rules out late-training format degradation: collapse is present from early training, and the optimal eval-loss checkpoint does not recover repo-level accuracy.
533	
534	\begin{table}[h]
535	\centering
536	\small
537	\caption{\cwm{} repo-level eval loss across training (Qwen3-8B, 3 seeds). Minimum is reached at step 300--400 (${\sim}$5\% of training); subsequent training monotonically increases loss.}
538	\label{tab:cwm_convergence}
539	\begin{tabular}{lccc}
540	\toprule
541	Step & s42 & s123 & s456 \\
542	\midrule
543	300 & 0.291 & \textbf{0.288} & \textbf{0.277} \\
544	400 & \textbf{0.286} & 0.306 & 0.283 \\
545	1000 & 0.333 & 0.336 & 0.351 \\
546	3000 & 0.445 & 0.453 & 0.435 \\
547	6600 & 0.521 & 0.517 & 0.507 \\
548	\bottomrule
549	\end{tabular}
550	\end{table}
551	
552	\paragraph{Evaluation sequence length.} \cwm{} accuracy varies by ${\sim}$9\pp{} across evaluation sequence lengths for the same checkpoint (seq2048: ${\sim}$65\% vs.\ seq4096: ${\sim}$56\%), driven by unparseable-rate differences that propagate through majority-class default assignment. \cls{} is invariant to this parameter. Cross-model \cwm{} comparisons use different eval lengths (Qwen3: 8192, DeepSeek: 4096) and are not directly comparable in absolute terms. A matched-sequence evaluation shows ${\sim}$1.5\pp{} difference for \cls{} (Appendix~\ref{app:ablations}), insufficient to explain the 18--26\pp{} gap. Furthermore, increasing Qwen3-8B \cwm{} evaluation from seq4096 to seq8192 \emph{raises} the unparseable rate (63.7\%$\to$73.8\%) while changing accuracy by only 0.81\pp{} (64.36\%$\to$65.17\%); giving the model more generation budget worsens format compliance rather than improving it, confirming that format collapse is a structural bottleneck rather than a truncation artifact. Practitioners must standardize evaluation sequence length for generation-based formulations.
553	
554	\paragraph{Preprocessing.} DeepSeek \cls{} accuracy ranges from 82.61\% (s42, drop preprocessing) to 74.93\% (s123, truncate preprocessing), a 7.68\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \cls{} $>$ \cwm{} holds under both strategies (Table~\ref{tab:taxonomy}).
555	
556	\paragraph{\traj{} training regime.} \traj{} uses a different training configuration: smaller training set (${\sim}$400 repo-level variants vs.\ ${\sim}$70K per-test instances), higher learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level labels. This asymmetry is inherent to the formulation (trajectory-level labels are only available at variant granularity), but precludes training-data-controlled comparison at repo level. The downsample ablation confirms the \cls{} formulation advantage persists at matched data volume (80.74\% vs.\ 72.92\%; Appendix~\ref{app:downsample}), though it controls for training volume but not label granularity (per-test vs.\ variant-level). Crucially, \traj{} achieves statistical equivalence with \cls{} at function level (${\leq}$1.3\pp{}, \S\ref{sec:func_results}), demonstrating the formulation itself is viable; the repo-level gap attribution remains uncertain: data volume (${\sim}$400 variants vs.\ ${\sim}$70K per-test instances) and label granularity (variant-level vs.\ per-test) are both plausible confounds that cannot be separately controlled.
557	
558	\paragraph{\cwm{} scale and pretraining.} Our \cwm{} baseline uses 4--8B LoRA fine-tuning without execution trace pretraining. The original Code World Model~\cite{meta2025cwm} uses 32B parameters with mid-training on execution traces, a fundamentally different training regime. At larger scale or with execution-trace pretraining, the generation bottleneck observed here may diminish: larger models produce more coherent long-form outputs, and execution trace exposure may improve output format compliance. This is the primary limitation: all repo-level \cwm{} conclusions are conditional on the ${\leq}$8B LoRA regime.
559	
560	Despite these confounds, the repo-level \cls{}--\cwm{} gap (18--26\pp{}) exceeds any single assessed confound. Even under worst-case compounding (${\sim}$11.5\pp{}), the gap retains ${\geq}$7.5\pp{} margin; confounds predominantly disadvantage \cwm{}. However, correlated confounds and limited seed coverage mean definitive causal attribution requires multi-seed replication. At $n{=}48$, the minimum detectable effect (MDE) is ${\sim}$25\pp{}~\cite{hoenig2001}; the \cls{}--\cwm{} gap (29--35\pp{}) exceeds this threshold, while the \cls{}--\traj{} gap ($<$10\pp{}) falls below it, consistent with our TOST equivalence finding. Holm-Bonferroni correction across the five primary comparisons ($k{=}5$; Table~\ref{tab:holm}) confirms the \cls{}--\cwm{} gap (adjusted $p{=}0.015$) and function-level \cls{}--\cwm{} equivalence (adjusted $p{=}0.028$); function-level \cls{}--\traj{} equivalence does not survive correction (adjusted $p{=}0.075$), nor does the repo-level \cwm{}--\traj{} comparison (adjusted $p{=}0.078$). The consistent direction across both model families and all tested configurations supports a formulation-level explanation, though definitive causal attribution requires future experiments addressing each confound individually.
561	
562	
563	\paragraph{Extended validity discussion.}
564	\label{app:limitations}
565	The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline); val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \cwm{} 8B comparison uses 3 seeds per model. The validation and test sets have zero problem overlap but differ in mutation type composition (Table~\ref{tab:mutation_distribution}): \texttt{operator\_swap} shifts from 19.1\% (val) to 34.3\% (test), the largest single-type distribution mismatch (+15.2\pp{}). All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches. While mutation testing literature establishes that mutants are reasonable proxies for real faults in test effectiveness studies~\cite{andrews2005mutation,just2014mutants}, these findings concern mutation \emph{adequacy} (whether tests that kill mutants also detect real faults), not whether verifiers trained on mutants transfer to real patches. However, the coupling effect underlying these results supports \emph{relative ranking} validity: a domain shift from synthetic mutations to real bugs may affect absolute accuracy levels, but our core finding---that formulation choice matters at repo level but not function level---concerns relative performance ordering, which is expected to be preserved under distributional shifts that affect all formulations equally. The synthetic-to-real transfer gap for absolute accuracy remains untested. The \traj{} training configuration differs from \cls{}/\cwm{}: smaller training set (${\sim}$400 vs.\ ${\sim}$70K instances), different learning rate ($2{\times}10^{-4}$ vs.\ $5{\times}10^{-5}$), and variant-level evaluation ($n{=}48$ vs.\ per-test $n{=}9{,}784$). The function-level \cls{}--\traj{} TOST equivalence ($p = 0.025$, seed-level paired, $\pm$2\pp{}) is computed on 523 matched variant-level instances across 5 seeds; 2 of 5 seeds use NF4 quantization. Restricting to three bfloat16 seeds yields a comparable mean gap ($-$0.45\pp{}) but wider confidence interval (df${=}$2); the TOST $p$-value increases to 0.128, which reflects reduced statistical power rather than a shift in the point estimate. The NF4 seeds contribute precision (narrowing the CI) without shifting the mean, consistent with precision being comparable across both quantization levels at function level. Repo-level \cls{}--\traj{} comparison should be interpreted with caution due to configuration and granularity differences.
566	
567	\section{Use of AI Assistants}
568	\label{app:ai-assistants}
569	
570	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
571	\begin{itemize}
572	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
573	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
574	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
575	\end{itemize}
576	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "74f794bc-fe63-4013-928c-f57d8f6c70a7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\noindent\\textbf{Appendix overview.} A: Oracle resolve advantage. B: Ablation studies. C-F: Extended analysis (error complementarity, parseable accuracy, forced parsing, qualitative errors, failed interventions, mutation scaling, inference efficiency, re-repair, chain-of-thought). G: TOST sensitivity (G.1: Bayesian ROPE). H: Effect sizes. I: Holm-Bonferroni. J: Mixed-effects regression. K: Parseable bias. L: CWM convergence. M: Few-shot. N: Threats. O: Downsample. P: Use of AI assistants.\n\n\\section{Oracle Accuracy-Utility Analysis}\n\\label{app:oracle}\n\nWe stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\\ trajectory-level oracle resolve rates under i.i.d.\\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \\S\\ref{sec:equivalence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \\S\\ref{sec:equivalence}). P2P regression rate: 1.04\\% mean, 0\\% median.}\n\\label{tab:oracle}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$T$} & \\textbf{Inst.\\%} & \\textbf{i.i.d.\\ (\\pp{})} & \\textbf{Block (\\pp{})} & \\textbf{Contrib.\\%} \\\\\n\\midrule\n$1$ & 68.7 & $-$0.04 & $-$0.09 & $\\approx$0 \\\\\n$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\\\\n$3$--$5$ & 7.1 & 25.00 & 40.74 & $\\approx$26 \\\\\n$\\geq 6$ & 5.1 & 30.00 & 40.06 & $\\approx$19 \\\\\n\\midrule\n\\textbf{All} & 100.0 & --- & \\textbf{10.93} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}\n\\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\\%) and concentrates at $T{=}2$ (19.1\\%, contributing 55.3\\% of total advantage). Note: $y$-axis does not start at zero.}\n\\label{fig:oracle_stratified}\n\\end{figure}\n\nTable~\\ref{tab:oracle} and Figure~\\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\\%), where block-correlated advantage reaches 31.69\\pp{} (55.3\\% of total). The overall block-correlated advantage is 10.93\\pp{}, driven by the $T \\geq 2$ minority. Block correlation amplifies relative to i.i.d.: at $T = 2$, 31.69\\pp{} vs.\\ 18.49\\pp{} (1.7$\\times$). P2P regression is negligible (1.04\\% mean, 0\\% median); the practical value concentrates in F2P discrimination.\n\n\\paragraph{Sensitivity to ICC estimate.}\nThe analysis above uses ICC $= 0.191$ from function-level analysis (\\S\\ref{sec:equivalence}), where mean cluster size $\\bar{k} \\approx 16.5$ yields DEFF $= 3.97$. At repository level, within-problem correlation is substantially stronger: ICC $= 0.3146$ with DEFF $= 114.4$ (\\S\\ref{sec:repo}), yielding an effective sample size of $n_{\\text{eff}} \\approx 9{,}784 / 114.4 \\approx 86$ independent observations~\\cite{moulton1990}---still sufficient for regression but limiting precision of variance component estimates. This is a consequence of the larger and more heterogeneous test suites in SWE-bench Verified problems. Under higher ICC, within-problem errors cluster more tightly and amplify the block-correlated per-test advantage at each $T$ stratum; the correction from i.i.d.\\ to block-correlated grows monotonically with ICC. The function-level ICC $= 0.191$ used in Table~\\ref{tab:oracle} thus provides a conservative lower bound on the per-test advantage. The repo-level correlation structure would yield an even larger gap between per-test and trajectory-level oracle resolve rates, which strengthens the case for per-test granularity at repository-level complexity.\n\n\\section{Ablation Studies}\n\\label{app:ablations}\n\n\\paragraph{LoRA rank sensitivity.}\nAll \\cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \\cwm{}, we train rank-32 variants (seed 42), doubling adapter parameters.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LoRA rank ablation for \\cwm{} 4B (seed 42, 3 epochs, lr $= 2{\\times}10^{-4}$). Rank-16 seed variance: 0.53\\pp{} (seeds 42 vs.\\ 456).}\n\\label{tab:rank_ablation}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Config} & \\textbf{$\\alpha/r$} & \\textbf{Acc (\\%)} & \\textbf{Fail \\fone{}} & \\textbf{Pass \\fone{}} & \\textbf{$\\Delta$} \\\\\n\\midrule\n$r{=}16$, $\\alpha{=}32$ & 2 & \\textbf{87.51} & --- & --- & --- \\\\\n$r{=}32$, $\\alpha{=}32$ & 1 & 87.00 & 87.1 & 86.9 & $-$0.51 \\\\\n$r{=}32$, $\\alpha{=}64$ & 2 & 87.04 & 87.27 & 86.79 & $-$0.47 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth rank-32 variants fall within the 2-seed variance of the rank-16 baseline (0.53\\pp{} between seeds 42 and 456; Table~\\ref{tab:rank_ablation}). The $\\alpha{=}64$ variant (matching the baseline $\\alpha/r{=}2$ ratio) rules out the confound that the $\\alpha{=}32$ result might reflect reduced effective scaling rather than rank insensitivity. This is consistent with \\cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.\n\n\\paragraph{Majority voting.}\nMajority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\n\n\\paragraph{Sequence-length ablation details.}\nBoth formulations are trained with \\texttt{max\\_seq\\_length}$=$2,048. At inference, \\cwm{} reserves \\texttt{max\\_new\\_tokens}$=$512, leaving ${\\sim}$1,536 effective input tokens; \\cls{} allocates nearly all context to input (5,120--8,192 tokens). A matched-context ablation (\\cls{} 8B at 2,048 tokens) achieves 83.04\\%, only 1.44\\pp{} below the 8,192-token evaluation (84.48\\%), though truncation introduces 136 unparseable outputs (1.39\\% of test samples). The matched-context gap (\\cls{}@2,048 vs.\\ \\cwm{}@2,048) is 25.00\\pp{} (98\\% of the full 25.59\\pp{} gap), confirming that input context disparity explains at most 3\\% of the difference.\n\n\\paragraph{Training data size control.}\n\\label{app:downsample}\nTo control for the training set size asymmetry between \\cls{} (${\\sim}$70K instances) and \\traj{} (386 variant-level instances, ${\\sim}$8K per-test equivalents, at repo level), we downsample \\cls{} training data to match \\traj{} in data volume. Downsampled \\cls{} (Qwen3-4B, seed 42) achieves 80.74\\% repo-level per-test accuracy, only 2.89\\pp{} below the full-data \\cls{} (83.63\\%) and still 7.82\\pp{} above \\traj{} (72.92\\%). The \\cls{} formulation advantage is not attributable to training data volume.\n\n\\paragraph{Few-shot prompting baselines.}\n\\label{app:few_shot}\nWe evaluate 3-shot in-context learning at repo level to test whether prompting strategy closes the gap to fine-tuned models. Table~\\ref{tab:few_shot} reports both per-test and variant-level accuracy.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level prompting baselines (per-test $n{=}9{,}784$; variant-level $n{=}48$). Majority baseline: 72.96\\% per-test, 54.17\\% variant-level.}\n\\label{tab:few_shot}\n\\setlength{\\tabcolsep}{4pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{0-shot (per-test)} & \\textbf{3-shot (per-test)} & \\textbf{3-shot (variant)} \\\\\n\\midrule\nQwen3-8B & 49.90\\% & 71.61\\% & 45.83\\%\\textsuperscript{$\\ast$} \\\\\nDeepSeek-6.7B & 48.54\\% & 46.28\\% & 45.83\\%\\textsuperscript{$\\ast$} \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{$\\ast$}Both models achieve 45.83\\% by correctly classifying all 22 unresolved variants and zero resolved variants (22/48 = 45.83\\%), equivalent to an always-predict-unresolved baseline. The 100\\% overlap in variant-level predictions confirms complete degradation at task-relevant granularity.}\n\\end{table}\n\nBoth models converge to exactly 45.83\\% variant-level accuracy under 3-shot prompting, below majority baseline (54.17\\%). Variant-level analysis reveals this is not a coincidence: both models correctly classify all 22 unresolved variants and zero resolved variants, equivalent to an always-predict-unresolved baseline with 100\\% prediction overlap. Per-test accuracy diverges sharply (Qwen3-8B 71.61\\% vs.\\ DeepSeek 46.28\\%), but this divergence is entirely superficial: Qwen3-8B predicts pass on nearly all tests, inflating per-test accuracy on a pass-heavy dataset (72.96\\% pass rate) without genuine discriminative ability. Per-test metrics can thus severely misrepresent baseline capability; variant-level evaluation is necessary to detect complete degradation. Neither 0-shot nor few-shot prompting approaches fine-tuned performance (82--84\\% per-test); fine-tuning is a necessary condition for repo-level verification.\n\n\\section{Repo-Level Per-Mutation Breakdown}\n\\label{app:repo_mutation}\n\nTable~\\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \\cls{} produces 0\\% unparseable outputs; all values are direct classification accuracy. \\cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \\S\\ref{sec:repo}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-mutation test accuracy (\\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \\cls{} 8B reports two seeds; $\\Delta$ is mean 4B$\\to$8B gain for \\cls{}. \\cwm{} 4B per-mutation overall accuracy omitted for non-gold mutations due to low parse rates (4.4--56.9\\%, Table~\\ref{tab:cwm_mutation_parse}); gold overall accuracy derived from parse rate 43.5\\% and parseable accuracy 23.5\\%.}\n\\label{tab:mutation_breakdown}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Mutation} & \\textbf{$n$} & \\textbf{CLS 4B} & \\textbf{CLS 8B s42} & \\textbf{CLS 8B s123} & \\textbf{CWM 4B} & \\textbf{CWM 8B} & \\textbf{$\\Delta$ CLS} \\\\\n\\midrule\ngold & 4,633 & 98.25 & 96.24 & 99.60 & 66.72 & 80.06 & $-$0.33 \\\\\noperator\\_swap & 3,357 & 78.91 & 81.38 & 82.60 & --- & 54.57 & +3.08 \\\\\noff\\_by\\_one & 183 & 58.47 & 86.89 & 79.20 & --- & 63.39 & \\textbf{+24.58} \\\\\nreturn\\_value & 562 & 67.97 & 75.44 & 66.40 & --- & 49.11 & +2.95 \\\\\nboundary\\_removal & 1,049 & 46.90 & 46.90 & 44.90 & --- & 42.23 & $-$1.00 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:cwm_mutation_parse} shows that \\cwm{} generation quality degrades from 4B to 8B across all mutation types.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\cwm{} parse rates and parseable-only accuracy per mutation type (seed 42). Parse rate decreases uniformly from 4B to 8B; parseable-only accuracy is below random binary chance (50\\%) for gold at both scales.}\n\\label{tab:cwm_mutation_parse}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Parse Rate (\\%)}} & \\multicolumn{2}{c}{\\textbf{Parse Acc (\\%)}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Mutation} & \\textbf{4B} & \\textbf{8B} & \\textbf{4B} & \\textbf{8B} \\\\\n\\midrule\ngold & 43.5 & 23.9 & 23.5 & 16.5 \\\\\noperator\\_swap & 56.9 & 21.2 & 63.1 & 58.8 \\\\\noff\\_by\\_one & 4.4 & 27.3 & 0.0 & 38.0 \\\\\nreturn\\_value & 48.8 & 26.9 & 27.0 & 56.9 \\\\\nboundary\\_removal & 30.6 & 51.8 & 59.2 & 51.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKey findings: (1)~Gold parse rate collapses from 43.5\\% to 23.9\\% at 8B; the simplest generation target (unmodified code, where all tests pass) degrades most, consistent with a fundamental generation bottleneck rather than task difficulty. (2)~Among parseable outputs, gold accuracy is 16.5--23.5\\%: the model generates outputs that fail exact-match even for correct code. (3)~\\texttt{off\\_by\\_one} is an anomaly: parse rate \\emph{increases} from 4.4\\% to 27.3\\%, but this is from an extremely low base ($n{=}8$ parseable at 4B), making both directions unreliable for this category.\n\n\\section{Variant-Level Accuracy}\n\\label{app:variant_level}\n\nTable~\\ref{tab:variant_level} reports variant-level accuracy ($n{=}48$) alongside per-test accuracy for all repo-level configurations. For \\cls{}, the aggregation penalty (per-test $\\to$ variant-level drop) ranges from 1\\pp{} to 19\\pp{} and is largest for models with low fail recall under the all-pass rule. \\cwm{} variant-level accuracy (48--52\\%) falls at or below the majority baseline, consistent with format collapse as the dominant failure mode.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level per-test vs.\\ variant-level accuracy ($n{=}48$ variants). Penalty = per-test $-$ variant-level. \\traj{} predicts variant outcomes directly (no aggregation). Variant-level majority baseline: 54.17\\% (26/48).}\n\\label{tab:variant_level}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Seed} & \\textbf{Per-test (\\%)} & \\textbf{Variant (\\%)} & \\textbf{Penalty (\\pp{})} & \\textbf{Fail Recall (\\%)} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\cls{}}} \\\\\nQwen3-8B & s42 & 84.48 & 72.92 & 11.56 & 56.76 \\\\\nQwen3-8B & s123 & 85.60 & 81.25 & 4.35 & 51.44 \\\\\nQwen3-4B & s42 & 83.63 & 64.58 & 19.05 & 48.72 \\\\\nDeepSeek-6.7B & s42 (e1) & 82.61 & 81.25 & 1.36 & 51.02 \\\\\nDeepSeek-6.7B & s42 (e3) & 82.51 & 79.17 & 3.34 & 38.47 \\\\\nDeepSeek-6.7B & s123 & 74.93 & 56.25 & 18.68 & ${\\sim}$13.72 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\cwm{}}} \\\\\nQwen3-8B & s42 & 65.17 & 52.08 & 13.09 & --- \\\\\nDeepSeek-6.7B$^\\dagger$ & s123 & --- & 47.92 & --- & --- \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{\\traj{}}} \\\\\nQwen3-4B & s42 & --- & 72.92 & --- & --- \\\\\nQwen3-8B & s42 & --- & 70.83 & --- & --- \\\\\nDeepSeek-6.7B & 3-seed & --- & 77.08 $\\pm$ 3.61 & --- & --- \\\\\n\\midrule\nMajority & --- & 72.96 & 54.17 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n\n{\\footnotesize $^\\dagger$Evaluated on ${\\sim}$75\\% of test instances (7210--7668 of 9784). DeepSeek \\traj{} Table~\\ref{tab:repo_level} reports 3 seeds (42/123/456) for alignment with \\cls{}/\\cwm{} seed coverage; three supplementary seeds (0/789/999) yield 75.0\\%, 66.7\\%, 79.2\\% respectively (6-seed mean 75.35 $\\pm$ 5.00\\%), consistent in direction.}\n\\end{table}\n\n\\section{Training Hyperparameters}\n\\label{app:hyperparams}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters used for fine-tuning. Both \\cls{} and \\cwm{} share the same LoRA configuration, optimizer, and training schedule; the only differences are per-device batch size, gradient accumulation steps (adjusted to maintain identical effective batch size of 32 across model sizes), and learning rate (DeepSeek-Coder uses $2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$ for Qwen3, selected via grid search over $\\{5{\\times}10^{-5}, 1{\\times}10^{-4}, 2{\\times}10^{-4}\\}$ on held-out validation loss).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Training hyperparameters for \\cls{}/\\cwm{} configurations. \\traj{} models use lr $= 2{\\times}10^{-4}$ due to the smaller training set (${\\sim}$8K function-level instances vs.\\ ${\\sim}$70K for \\cls{}/\\cwm{}); other hyperparameters are shared.}\n\\label{tab:hyperparams}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll}\n\\toprule\n\\multicolumn{2}{l}{\\textbf{Shared across all configurations}} \\\\\n\\midrule\nLoRA rank / alpha / dropout & 16 / 32 / 0.05 \\\\\nLoRA targets & \\texttt{q/k/v/o\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1{=}0.9$, $\\beta_2{=}0.999$) \\\\\nLR scheduler & Linear \\\\\nEffective batch size & 32 \\\\\nMax sequence length & 2,048 \\\\\nEpochs & 3 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & \\checkmark \\\\\nSeeds (function) & \\{42, 123, 456, 789, 0\\}\\textsuperscript{$b$} \\\\\nSeeds (repo) & \\{42, 123, 456\\}\\textsuperscript{$c$} \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{6pt}\n\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\multicolumn{4}{l}{\\textbf{Model-family--specific parameters}} \\\\\n\\midrule\n& \\textbf{Qwen3-4B} & \\textbf{Qwen3-8B} & \\textbf{DS-6.7B} \\\\\n\\midrule\nLearning rate & 5e-5 & 5e-5 & 2e-4 \\\\\nWeight decay & 0.01 & 0.01 & 0.0 \\\\\nWarmup ratio & 0.05 & 0.05 & 0.1 \\\\\nBatch / grad.\\ accum.\\ (\\cls{}) & 2 / 16 & 1 / 32 & 2 / 16 \\\\\nBatch / grad.\\ accum.\\ (\\cwm{}) & 1 / 32 & 1 / 32 & 1 / 32 \\\\\nTraining samples & 70,748 & 70,748 & 67,343--70,748\\textsuperscript{$a$} \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\footnotesize $^a$DeepSeek \\cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \\S\\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Table~\\ref{tab:repo_level} caption for per-model counts.}\n\\end{table}\n\n\\paragraph{Data processing.} DeepSeek CWM seeds use \\texttt{train\\_unified.py}, which drops samples exceeding \\texttt{max\\_seq\\_length} (3{,}405 of 70{,}748 samples, 4.8\\%). Qwen CWM seeds use \\texttt{train\\_repo\\_cwm.py}, which truncates and retains all samples. This difference affects total training steps (${\\sim}$12{,}627 vs.\\ ${\\sim}$13{,}266 for DeepSeek, ${\\sim}$6{,}633 for Qwen) but not the training data distribution, as dropped samples are uniformly distributed across labels.\n\n\\paragraph{Prompt templates.} Prompt templates for all formulations (\\cls{}, \\cwm{}, \\traj{}) are provided in the code repository. \\cls{} uses a binary classification template (``Does this test pass or fail?''); \\cwm{} uses an execution simulation template (``What is the output of this test?''); \\traj{} uses a variant-level verdict template (``Is this patch resolved or unresolved?'').\n\n\\paragraph{Mutation operators.} We use five mutation types: (1)~\\emph{gold}: unmodified code (all tests pass); (2)~\\emph{operator\\_swap}: replaces comparison or arithmetic operators (e.g., \\texttt{<} $\\to$ \\texttt{<=}); (3)~\\emph{off\\_by\\_one}: shifts loop bounds or array indices by $\\pm$1; (4)~\\emph{return\\_value}: modifies return statements (e.g., negating a boolean, changing a constant); (5)~\\emph{boundary\\_removal}: removes conditional guards or boundary checks. Mutation operators were applied using AST-level transformation; variants that did not alter any test outcome were discarded.\n\n\\paragraph{Compute budget.}\nAll experiments were conducted on NVIDIA RTX 5090 GPUs. Training time is approximately 1.5 hours per run for 4B models and 2 hours for 8B models. Total compute budget: ${\\sim}$370 GPU-hours across 223 completed runs (135 successful, 88 failed/killed; ${\\sim}$46 unique configurations including seeds, formulations, model sizes, and ablations).\n\n\\section{Prompt Templates}\n\\label{app:prompts}\n\nWe show representative prompt examples for each formulation. All examples use the same input instance for comparability.\n\n\\paragraph{CLS (per-test classification).}\n{\\footnotesize\\begin{verbatim}\nSystem: You are a code verifier.\nGiven a code patch and a test name,\npredict whether the test will pass\nor fail when run against the\npatched code.\n\nUser:\n## Patch (git diff)\n&lt;patch content> [... truncated]\n## Test\ntest_boundary_check\nWill this test pass or fail?\n\nTarget: pass\n\\end{verbatim}}\n\n\\paragraph{CWM (execution simulation).}\n{\\footnotesize\\begin{verbatim}\nSystem: You are a code execution\nsimulator. Given a code snippet and\na test case, predict the execution\nresult.\n\nUser:\n## Code\n&lt;code content> [... truncated]\n## Test\ntest_boundary_check\nWhat is the execution result?\n\nTarget: PASS: test completed\nsuccessfully\n\\end{verbatim}}\n\n\\paragraph{TRAJ (trajectory scoring).}\n{\\footnotesize\\begin{verbatim}\nSystem: You are a code repair\nverifier. Given the code patch and\ntest summary, predict whether all\ntests pass (resolved) or any test\nfails (unresolved).\n\nUser:\n[Code]\n&lt;patch content> [... truncated]\n[Test Summary]\n&lt;all test names and descriptions>\n\nTarget: resolved\n\\end{verbatim}}\n\n\\cls{} and \\cwm{} share the same input format (one code--test pair per instance); \\cls{} produces a single token (\\texttt{pass}/\\texttt{fail}), while \\cwm{} generates a variable-length execution trace. \\traj{} receives all tests concatenated and produces a single token (\\texttt{resolved}/\\texttt{unresolved}).\n\n\n\\section{Val-Test Mutation Type Distribution}\n\\label{app:mutation_distribution}\n\nTable~\\ref{tab:mutation_distribution} reports the mutation type composition of the repo-level validation and test sets. The most notable shift is \\texttt{operator\\_swap}, which nearly doubles from val (19.1\\%) to test (34.3\\%), while \\texttt{off\\_by\\_one} shrinks from 10.0\\% to 1.9\\%.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Repo-level mutation type distribution: validation vs.\\ test set, with per-type \\cls{} accuracy at two model sizes (seed 42). Shift = test\\% $-$ val\\%.}\n\\label{tab:mutation_distribution}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mutation Type} & \\textbf{Val (\\%)} & \\textbf{Test (\\%)} & \\textbf{Shift} & \\textbf{\\cls{} 4B} & \\textbf{\\cls{} 8B} \\\\\n\\midrule\ngold & 45.2 & 47.4 & +2.2 & 98.3 & 96.2 \\\\\noperator\\_swap & 19.1 & 34.3 & +15.2 & 78.9 & 81.4 \\\\\nboundary\\_removal & 15.0 & 10.7 & $-$4.3 & 46.9 & 46.9 \\\\\nreturn\\_value & 10.7 & 5.7 & $-$5.0 & 68.0 & 75.4 \\\\\noff\\_by\\_one & 10.0 & 1.9 & $-$8.1 & 58.5 & 86.9 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe \\texttt{operator\\_swap} shift is the primary source of val-test distribution mismatch. Since \\cls{} achieves moderate accuracy on this type (78.9--81.4\\%), the over-representation in the test set does not systematically bias overall accuracy estimates in either direction. Two boundary observations are notable: (1)~\\texttt{boundary\\_removal} represents a scale-invariant difficulty ceiling at ${\\sim}$47\\% across both model sizes: this mutation type resists capacity scaling; (2)~\\texttt{off\\_by\\_one} shows the largest scaling gain (+28.4\\pp{}, 58.5\\%$\\to$86.9\\%) but its small test share (1.9\\%) limits its contribution to overall accuracy differences across scales.\n\n\\section{Qualitative Error Analysis}\n\\label{app:qualitative}\n\nTo complement the quantitative divergence reported in \\S\\ref{sec:repo}, we examine representative errors from each formulation at repository level.\n\n\\paragraph{\\cwm{} failure modes.}\nTwo patterns account for the majority of unparseable \\cwm{} outputs on Qwen3. (1)~\\emph{Task misunderstanding}: the model generates a complete simulated test runner log (test names, timing, summary lines) rather than a pass/fail verdict. For instance, on \\texttt{django\\_\\_django-14315}, the model outputs a fabricated 1,248-token Django test execution trace with hallucinated test names that do not exist in the target file. The model confuses ``predict test outcome'' with ``simulate test execution environment.'' (2)~\\emph{Autoregressive degeneration}: the model enters a repetitive loop (e.g., repeating \\texttt{from \\_pytest.config import \\_parse\\_pytest\\_args} until truncation at 4,542 tokens). Both patterns produce zero usable signal and default to the majority-class label. This explains why unparseable predictions carry higher accuracy than parseable ones (\\S\\ref{sec:repo}).\n\n\\paragraph{\\cls{} failure modes.}\n\\cls{} errors concentrate in two categories requiring multi-step reasoning. False positives arise from \\emph{cross-concern value propagation}: a boundary removal mutation in \\texttt{pytest} converts a guarded attribute access (\\texttt{if xfailed and not xfailed.run}) to \\texttt{if True:}, causing a NoneType error on tests exercising unrelated skip marks. The model fails to trace the None path through the pytest hook lifecycle. False negatives arise from \\emph{mathematical equivalence}: on \\texttt{HumanEval/130} (Tribonacci variant), the model predicts failure for correct code because verifying the self-referential recurrence requires algebraic substitution rather than syntactic inspection. This single problem accounts for 17\\% of all function-level false negatives.\n\n\\paragraph{Complementarity.}\nThese failure patterns operate at different levels: \\cwm{} fails at the format level (producing no usable signal), while \\cls{} fails at the reasoning level (producing a confident but incorrect binary verdict). Both formulations are FP-dominant (over-predict failure), but \\cwm{}'s higher FP rate (70.3\\% vs.\\ 56.5\\%) means it over-predicts failure on instances \\cls{} correctly classifies, producing partial complementarity (oracle combination: 90.63\\%; \\S\\ref{app:extended_analysis}, paragraph a).\n\n\\section{Extended Analysis}\n\\label{app:extended_analysis}\n\n\\paragraph{Function-level CWM metric robustness.}\nAt function level, \\cwm{} outputs are short status strings (mean ${\\sim}$5--15 tokens). The unparseable rate is only 1.39\\%, and default-to-pass bias is $<$1\\pp{}---well below the SESOI threshold. Exact string matching is appropriate for these short, structured outputs; semantic-but-format-different matches are rare given the constrained output space.\n\n\\paragraph{(a) Error complementarity.}\n\\cls{} and \\cwm{} are both FP-dominant at function level but at different rates, producing partial complementarity. Among \\cls{} errors (seed 42), 56.5\\% are false positives (PASS $\\to$ FAIL); among \\cwm{} errors, 70.3\\% are false positives. Both formulations over-predict failure, but \\cwm{}'s stronger FP bias means it incorrectly rejects passing tests that \\cls{} correctly accepts. An oracle combination achieves 90.63\\% accuracy (1713/1890 correct, 177 both-wrong; +2.80\\pp{} over the best single formulation, \\cls{} 87.83\\%; single-seed estimate, seed 42). The complementarity arises from different \\emph{degrees} of fail-bias rather than opposite error directions: \\cwm{}'s generation bottleneck produces aggressive failure predictions, while \\cls{}'s single-token output is more calibrated. Ensemble approaches exploiting this degree difference are a natural direction.\n\n\\paragraph{(b) CWM error mode breakdown.}\nAmong unparseable \\cwm{} outputs (Qwen3, repo-level), 76.9\\% contain no execution keywords; 22.9\\% contain ambiguous co-occurring pass/fail keywords. Format compliance varies sharply across repositories (scikit-learn: near-zero unparseable; sphinx: 100\\%); repository-specific code patterns interact with the model's generation capabilities in complex ways. This per-repository variation is consistent with a model/tokenizer-specific failure rather than a formulation-level one.\n\n\\paragraph{(c) Relaxed matching does not rescue \\cwm{}.}\nRelaxed matching (tolerating format deviations, L0--L4) \\emph{decreases} \\cwm{} accuracy: 58.04\\%$\\to$56.98\\% (seed 42) and 59.09\\%$\\to$55.91\\% (seed 123). Unparseable predictions default to the majority class (pass, 72.96\\%), which outperforms the model's own parseable predictions (38--43\\%). The divergence widens from 26\\pp{} to 27\\pp{} under relaxed matching. This rules out the hypothesis that parsing strictness inflates the observed gap. Constrained decoding~\\cite{willard2023outlines} could enforce format compliance but would not address the semantic accuracy deficit among parseable outputs. An accidental training artifact provides further evidence: a \\cwm{} model inadvertently trained on function-level (\\cls{}-format) data achieved 86.05\\% accuracy with 0\\% unparseable outputs at repo level---recovering \\cls{}-level performance. This confirms that the repo-level \\cwm{} degradation stems entirely from trace generation complexity, not from the underlying verification task.\n\n\\paragraph{(d) Variance compression.}\n\\cwm{}'s 5-seed standard deviation (0.37\\pp{}) is lower than \\cls{} (0.78\\pp{}) and \\traj{} (0.97\\pp{}) at function level. If \\cwm{} performance is capped by output-format constraints at a given complexity level, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.\n\n\\paragraph{(e) Per-test precision and recall.}\n\\cls{} achieves fail \\fone{} 87.59\\% (precision 86.20\\%, recall 89.04\\%) at seed 42.% derived from overlap analysis (error_overlap_matched_seed.json); FP=130, FN=100, TP=848, TN=812\nMulti-F2P instances (6--10 tests) reach 96.3\\% accuracy, consistent with the oracle finding that per-test granularity is most valuable for complex instances.\n\n\\paragraph{(f) Block correlation.}\nWithin-problem errors are correlated (ICC $= 0.191$, DEFF $= 3.97$, 2.81$\\times$ more all-correct problems than i.i.d.\\ expectation). All statistical tests use clustered bootstrap accordingly.\n\n\\paragraph{(g) Failed interventions.}\nWe systematically tested four interventions targeting different hypothesized causes of \\cwm{} repo-level degradation; all failed:\n\n\\begin{itemize}[leftmargin=*,itemsep=1pt,topsep=2pt]\n\\item \\textbf{Capacity (rank 32, $\\alpha{=}64$):} $-$0.47\\pp{}, within seed variance (\\S\\ref{app:ablations}).\n\\item \\textbf{Majority voting ($K{=}3$):} $-$0.68\\pp{}; 93.3\\% unanimous, net flips negative (\\S\\ref{app:ablations}).\n\\item \\textbf{Relaxed matching (L0--L4):} $-$1.06\\pp{}; default-pass outperforms parseable predictions (paragraph~(c) above).\n\\item \\textbf{Model scaling (4B$\\to$8B):} parseable accuracy decreases (42.88\\%$\\to$38.52\\%) while unparseable rate rises (53.7\\%$\\to$73.8\\%); gain is a default-assignment artifact (\\S\\ref{sec:repo}).\n\\end{itemize}\n\n\\noindent Each intervention targets a distinct alternative explanation (insufficient capacity, random noise, parsing strictness, model scale); the uniform failure across all four confirms the bottleneck is formulation-level---output space complexity at repo level exceeds what ${\\leq}$8B generation models can handle, independent of these surface-level factors.\n\n\\paragraph{(h) Per-mutation scaling patterns.}\nScaling benefits are highly non-uniform across mutation types (Table~\\ref{tab:mutation_breakdown}). \\texttt{off\\_by\\_one} shows the largest \\cls{} scaling gain: 58.5\\% (4B) to 86.9\\% (8B, $+$28.4\\pp{}). In contrast, \\texttt{boundary\\_removal} is scale-invariant at ${\\sim}$47\\% across both sizes, which marks an intrinsic difficulty ceiling. For \\cwm{}, gold mutation parse rate collapses from 43.5\\% (4B) to 23.9\\% (8B) despite being the simplest target: generation capability degrades even for trivially correct code at larger scale within Qwen3. The val-test mutation type distribution differs notably (\\texttt{operator\\_swap} shifts from 19.1\\% to 34.3\\%; Table~\\ref{tab:mutation_distribution}), but this shift does not systematically bias overall accuracy because \\cls{} performance on \\texttt{operator\\_swap} (78.9--81.4\\%) is close to the overall mean.\n\n\\paragraph{(i) Inference efficiency.}\n\\cls{} achieves 217$\\times$ higher throughput than \\cwm{} at repo level (853 vs.\\ 3.9 inferences/min; Qwen3-4B, RTX 5090, 100 samples, avg ${\\sim}$1,040 input tokens). The speedup derives directly from the formulation: classification requires a single output token, whereas \\cwm{} generates an average of 477 tokens per inference. Median latency is 48ms (\\cls{}) vs.\\ 16.3s (\\cwm{}). At the observed unparseable rate of 73.8\\% (8B), the majority of \\cwm{}'s generation budget produces tokens that cannot yield a valid verdict. This \\cls{}--\\cwm{} efficiency gap is an inherent property of the formulation difference (1 vs.\\ $O(L)$ output tokens) and should generalize across models, unlike the accuracy divergence which may be model-contingent.\n\nThe \\cls{}--\\traj{} efficiency comparison is more nuanced, because \\cls{} makes one call per test while \\traj{} makes one call per instance. Per-call, \\cls{} is 20--138$\\times$ faster (depending on input length: 47ms for short contexts vs.\\ 2,632ms for \\traj{}). However, the per-instance effective speedup depends on test count $|T|$: at function level ($|T| \\approx 2.3$), \\cls{} is ${\\sim}$24$\\times$ faster (108ms vs.\\ 2,632ms per instance); at repo level ($|T| \\approx 12.3$, ${\\sim}$70ms/call with longer inputs), \\cls{} is ${\\sim}$3$\\times$ faster (861ms vs.\\ 2,631ms). A crossover exists at $|T| \\approx 50$ tests, beyond which \\traj{}'s single-call amortization dominates. This boundary condition is informative for deployment: \\cls{} is strongly preferred for function-level and moderate repo-level test suites, while extremely large test suites ($>$50 tests per instance) favor trajectory-level efficiency despite its coarser diagnostic signal.\n\n\\paragraph{(j) Re-repair pilot.}\nWe tested whether per-test diagnostic feedback improves downstream repair. A Qwen3-8B repair agent received either per-test diagnostic signals (which specific tests failed and why) or binary accept/reject feedback, evaluated on 44 SWE-bench Verified instances. The diagnostic condition achieved accuracy no higher than the binary baseline ($A_1 = 52.3\\%$, $p = 0.42$, effect size $\\approx 0$). Per-test diagnostic information does not automatically translate to repair improvements at this scale. The negative result may reflect insufficient agent capability to exploit fine-grained feedback, insufficient sample size (at $n = 44$, statistical power is ${\\sim}$0.3 for a medium effect size), or a genuine limitation of the diagnostic-to-repair translation.\n\n\\paragraph{(k) Relationship to chain-of-thought verification.}\n\\cwm{} is structurally a chain-of-thought verifier: the model generates an execution trace token by token and derives its PASS/FAIL verdict from the final trace state. If intermediate reasoning improved verification, \\cwm{} should outperform the reasoning-free \\cls{} baseline. At function level, no such advantage materialises: \\cwm{} and \\cls{} are statistically equivalent (TOST $p{=}0.007$, $\\pm$2\\pp{} margin; \\S\\ref{sec:equivalence}), indicating that the additional trace generation provides no accuracy benefit over direct binary classification. At repo level, the chain-of-thought mechanism actively \\emph{hurts}: trace generation triggers format collapse (53--74\\% unparseable), and even parseable traces yield accuracy below the majority baseline (38--43\\% vs.\\ 72.96\\%; paragraph~(c)). Four targeted interventions fail to rescue the generation pathway (paragraph~(g)). Within the ${\\leq}$8B LoRA regime, chain-of-thought--style verification does not outperform direct classification for execution prediction. Whether execution-trace pretraining at larger scale~\\cite{meta2025cwm} changes this conclusion remains the primary open question (\\S\\ref{sec:threats}).\n\n\\section{TOST Margin Sensitivity}\n\\label{app:tost_sensitivity}\n\nTable~\\ref{tab:tost_sensitivity} reports the TOST equivalence $p$-value as a function of the equivalence margin, computed on the 5-seed variant-level \\cls{}--\\cwm{} comparison (gap $= 1.24$\\pp{}, 523 variants, 114 clusters, clustered bootstrap).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST margin sensitivity for \\cls{}--\\cwm{} variant-level equivalence (5 seeds, 523 variants, 114 clusters). The smallest margin achieving equivalence at $\\alpha = 0.05$ is $\\pm$1.52\\pp{}.}\n\\label{tab:tost_sensitivity}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{ccc}\n\\toprule\n\\textbf{Margin ($\\pm$\\pp{})} & \\textbf{$p$-value} & \\textbf{Equivalent ($\\alpha{=}0.05$)?} \\\\\n\\midrule\n1.0 & $\\gg$0.05 & No \\\\\n1.5 & 0.054 & No (borderline) \\\\\n\\textbf{1.52} & ${\\sim}$\\textbf{0.05} & \\textbf{Smallest margin} \\\\\n1.71 & 0.027 & Yes \\\\\n2.0 & 0.007 & Yes \\\\\n3.0 & $4.6{\\times}10^{-5}$ & Yes \\\\\n5.0 & $\\ll$0.001 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe minimum equivalence margin is $\\pm$1.52\\pp{}, 0.48\\pp{} below our pre-specified $\\pm$2\\pp{} threshold. The $\\pm$2\\pp{} threshold was set based on deployment relevance rather than observed data: at function-level accuracy (85--88\\%), a 2\\pp{} per-test difference corresponds to ${\\sim}$38 additional errors across 1,890 tests (${\\sim}$2--3 problems out of 114), comparable in magnitude to between-seed standard deviation (0.37--0.97\\pp{}) and checkpoint selection noise ($<$1\\pp{}). Differences within this range do not reliably distinguish formulations from training noise in pipeline selection decisions. For \\cls{}--\\traj{}, the TOST at $\\pm$2\\pp{} yields $p{=}0.025$, nominally significant but not surviving Holm-Bonferroni correction at $k{=}5$ (adjusted $p{=}0.075$; Table~\\ref{tab:holm}). The one-sided decomposition reveals the binding constraint: $p_{\\text{upper}}{=}0.005$ ($\\Delta < {+}2$\\pp{} is well-confirmed) while $p_{\\text{lower}}{=}0.025$ ($\\Delta > {-}2$\\pp{}) limits the overall TOST, consistent with \\cls{} having mildly higher accuracy.\n\n\\paragraph{Robustness: seed-level vs.\\ clustered bootstrap TOST.}\nThe primary TOST $p$-values use seed-level paired analysis (df${=}$4), treating each training seed as the unit of replication (\\S\\ref{sec:setup}). Under problem-level clustered bootstrap (resampling 114 problem clusters, 10K iterations), the \\cls{}--\\traj{} raw TOST $p$ decreases to ${\\sim}$0.007 (Holm-adjusted $p{\\approx}0.021$), which would confirm equivalence. We report the more conservative seed-level result ($p{=}0.025$, adjusted $p{=}0.075$) as primary, since training seeds are the true unit of replication; problem-level bootstrap pools within-seed observations and may understate between-seed uncertainty. For \\cls{}--\\cwm{}, both methods confirm equivalence ($p \\leq 0.010$), so the choice does not affect conclusions.\n\n\\subsection{Bayesian ROPE Analysis}\n\\label{app:bayesian_rope}\nTo complement the frequentist TOST, we conduct a Bayesian equivalence analysis using a paired $t$-test with Jeffreys prior~\\cite{kruschke2013bayesian,kruschke2018rejecting}. The marginal posterior for the mean accuracy difference follows a $t$-distribution with $n{-}1$ degrees of freedom. For \\cls{}--\\cwm{}, the posterior probability within the $\\pm$2\\pp{} ROPE is $P(\\text{ROPE}) = 0.975$, and the 95\\% highest density interval (HDI $= [{+}0.10, {+}2.00]$\\,pp) falls entirely inside the ROPE, confirming equivalence under both continuous and HDI-based decision criteria. For \\cls{}--\\traj{} at per-test level, $P(\\text{ROPE}) = 0.542$ (inconclusive; 95\\% HDI $= [{+}0.35, {+}3.52]$\\,pp extends beyond the ROPE), consistent with the TOST inconclusive result after Holm correction ($p_{\\text{adj}} = 0.075$). At variant level, \\cls{}--\\traj{} equivalence is supported by the Bayesian criterion ($P(\\text{ROPE}) = 0.970$, HDI $= [{-}2.00, {+}1.03]$\\,pp), but the frequentist TOST remains inconclusive after Holm-Bonferroni correction ($p_{\\text{adj}} = 0.075$; Table~\\ref{tab:holm}). This discrepancy reflects differing treatments of multiplicity: Bayesian ROPE evaluates each comparison independently, while Holm correction penalizes across all $k{=}5$ primary tests. For \\cls{}--\\cwm{}, both frameworks agree (TOST $p_{\\text{adj}}{=}0.028$, $P(\\text{ROPE}){=}0.975$); for \\cls{}--\\traj{} per-test, both are inconclusive. We conservatively follow the Holm-corrected TOST in the main text and report \\cls{}--\\traj{} equivalence as inconclusive.\n\n\\paragraph{14B scaling evidence.} At 14B (3 seeds), the \\cls{}--\\cwm{} gap narrows to 0.43\\pp{} and the \\cls{}--\\traj{} gap to 1.07\\pp{}, both within the $\\pm$2\\pp{} margin. Seed-level TOST (df${=}$2) is inconclusive for equivalence in both pairs ($p{=}0.076$ for \\cls{}--\\cwm{}, $p{=}0.187$ for \\cls{}--\\traj{}), reflecting the severe power limitation of 3-seed comparisons (power ${\\sim}$0.08 at $\\pm$2\\pp{} margin with df${=}$2). Bayesian ROPE provides moderate support: $P(\\text{ROPE}){=}0.887$ for \\cls{}--\\cwm{} and $P(\\text{ROPE}){=}0.780$ for \\cls{}--\\traj{}. Under problem-level clustered bootstrap, both comparisons reach significance ($p{=}0.0006$ and $p{=}0.043$ respectively), but this analysis treats within-seed observations as exchangeable, potentially understating between-seed uncertainty. The monotonic gap reduction (3.11\\pp{} at 4B $\\to$ 2.24\\pp{} at 8B $\\to$ 1.07\\pp{} at 14B) favors a capacity-dependent convergence interpretation, though formal confirmation at seed level requires more training seeds.\n\n\n\\section{Variant-Level Effect Sizes}\n\\label{app:power}\n\nTable~\\ref{tab:variant_power} reports variant-level bootstrap confidence intervals for the repo-level formulation comparisons ($n{=}48$ variants). Following Hoenig and Heisey~\\cite{hoenig2001}, we report minimum detectable effect (MDE) rather than post-hoc observed power.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Variant-level bootstrap analysis ($n{=}48$). \\cls{}--\\cwm{} uses paired bootstrap (same variants, same seed); \\cls{}--\\traj{} uses unpaired bootstrap (per-variant \\traj{} predictions not archived for pairing). MDE at $n{=}48$: ${\\sim}$25\\pp{}.}\n\\label{tab:variant_power}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Config} & \\textbf{$\\Delta$ (\\pp{})} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{\\cls{} vs.\\ \\cwm{} (paired)}} \\\\\n& Qwen3-8B & +29.17 & [10.42, 47.92] & 0.003 \\\\\n& DeepSeek-6.7B & +35.42 & [18.75, 50.05] & ${<}$0.001 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{\\cls{} vs.\\ \\traj{} (unpaired)}} \\\\\n& Qwen3-4B & $-$4.17 & wide & 0.740 \\\\\n& Qwen3-8B & +8.33 & wide & 0.385 \\\\\n& DeepSeek-6.7B & 0.00 & wide & 1.000 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt $n{=}48$, the MDE is ${\\sim}$25\\pp{}. The \\cls{}--\\cwm{} gap (29--35\\pp{}) exceeds this threshold, confirming that $n{=}48$ is sufficient to detect the observed divergence. The \\cls{}--\\traj{} gaps ($<$10\\pp{}) fall well below the MDE: any true difference is too small to detect at this sample size, consistent with the function-level TOST equivalence (\\S\\ref{sec:equivalence}).\n\nThe \\cls{}--\\traj{} unpaired bootstrap produces wider confidence intervals than paired analysis would; \\traj{} per-variant predictions were not archived in a format that permits pairing. The \\cls{}--\\cwm{} paired comparison uses \\cls{} s123 vs.\\ \\cwm{} s42 (different seeds), but the CI lower bound of 10.42\\pp{} far exceeds the seed noise observed in function-level experiments ($<$2\\pp{}).\n\n\n\\section{Multiple Comparison Correction}\n\\label{app:holm}\n\nTable~\\ref{tab:holm} applies Holm-Bonferroni correction~\\cite{holm1979} to the five primary statistical comparisons across this study ($k{=}5$, family-wise $\\alpha{=}0.05$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Holm-Bonferroni correction for primary comparisons ($k{=}5$). Comparisons ranked by raw $p$-value; each tested against $\\alpha / (k - \\text{rank} + 1)$.}\n\\label{tab:holm}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{clcccc}\n\\toprule\n\\textbf{Rank} & \\textbf{Comparison} & \\textbf{Raw $p$} & \\textbf{Factor} & \\textbf{Adj $p$} & \\textbf{Sig.?} \\\\\n\\midrule\n1 & Repo: \\cls{} vs \\cwm{} & 0.003 & $\\times$5 & 0.015 & \\checkmark \\\\\n2 & Func: \\cls{} vs \\cwm{} (TOST $\\pm$2\\pp{}) & 0.007 & $\\times$4 & 0.028 & \\checkmark \\\\\n3 & Func: \\cls{} vs \\traj{} (TOST $\\pm$2\\pp{}) & 0.025 & $\\times$3 & 0.075 & --- \\\\\n4 & Repo: \\cwm{} vs \\traj{} & 0.039 & $\\times$2 & 0.078 & --- \\\\\n5 & Repo: \\cls{} vs \\traj{} & 0.385 & $\\times$1 & 0.385 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe two core claims survive correction: the repo-level \\cls{}--\\cwm{} divergence (adjusted $p{=}0.015$) and function-level \\cls{}--\\cwm{} equivalence (adjusted $p{=}0.028$). The function-level \\cls{}--\\traj{} equivalence does not survive correction (adjusted $p{=}0.075$). Under problem-level clustered bootstrap, the raw TOST $p$ decreases to ${\\sim}$0.007 (adjusted $p{\\approx}0.021$), which would confirm equivalence; we report the more conservative seed-level result ($p{=}0.025$) as primary, since training seeds are the true unit of replication.\n\n\\section{Mixed-Effects Regression}\n\\label{app:interaction}\n\nWe fit mixed-effects linear probability models (LPM) with heteroskedasticity-robust standard errors (HC1) to test the formulation$\\times$complexity interaction formally~\\cite{moulton1990}. We choose LPM because coefficients are directly interpretable as probability differences (percentage points), consistent with the reporting units in the main text; at these sample sizes ($n{\\approx}56$K cross-complexity, repo-level pooled cross-model) and base rate range (0.6--0.9), LPM and logistic regression yield concordant conclusions for all primary effects~\\cite{angrist2009mostly} (confirmed below).\n\n\\paragraph{Cross-complexity model (DeepSeek-Coder).} \\texttt{correct $\\sim$ formulation $\\times$ complexity + (1|problem\\_id)}, $n{=}56{,}480$ observations (\\cls{} + \\cwm{} $\\times$ function + repo), 139 problem clusters. The \\cwm{} main effect at function level is non-significant ($\\hat{\\beta}{=}-0.002$, $z{=}-0.25$, $p{=}0.805$); the \\cwm{}$\\times$repo interaction is highly significant ($\\hat{\\beta}{=}-0.219$, $z{=}-23.7$, $p{<}0.001$). \\cwm{} and \\cls{} are statistically indistinguishable at function level ($\\Delta{=}-0.2$\\pp{}, $p{=}0.805$) but diverge by 22\\pp{} at repo level, confirming the complexity-dependent divergence is not an artifact of aggregation.\n\n\\paragraph{Repo-level cross-model model.} \\texttt{correct $\\sim$ formulation $\\times$ model + (1|problem\\_id)}, both model families, repo level only. \\cwm{} deficit: $\\hat{\\beta}{=}-0.22$ ($-$22\\pp{}, $z{=}-64.4$, $p{<}0.001$). Model effect: +1.1\\pp{} for Qwen3 ($z{=}3.1$, $p{=}0.002$ in LPM; not significant under GEE, $p{=}0.449$). Formulation$\\times$model interaction: +1.6\\pp{} less \\cwm{} degradation on Qwen3 ($z{=}2.8$, $p{=}0.006$ in LPM; not significant under GEE, $p{=}0.860$). Formulation dominates the predictable variance; model identity is directionally positive but specification-dependent. The 25-cluster random intercept structure limits effective degrees of freedom for the random effects; inferences on fixed effects (formulation, complexity) are robust as they pool across the full observation count.\n\n\\paragraph{Logistic regression robustness check.} To verify that LPM conclusions are not artifacts of the linear link function, we fit GEE logistic regression (binomial family, exchangeable working correlation, robust sandwich standard errors) to the same data. For the cross-complexity model, the \\cwm{} main effect at function level has OR$=$0.98 (95\\% CI [0.86, 1.12], $p{=}0.771$) and the \\cwm{}$\\times$repo interaction has OR$=$0.31 ([0.15, 0.65], $p{=}0.002$). Average marginal effects are $-$0.2\\pp{} (function) and $-$21.6\\pp{} (repo), matching LPM coefficients within 0.3\\pp{}. For the cross-model model, the \\cwm{} deficit has OR$=$0.30 ([0.15, 0.63], $p{=}0.001$, AME$=$\\,$-$21.1\\pp{}). Direction, magnitude, and significance of all primary effects are concordant between LPM and logistic regression; minor discrepancies in secondary effects (model identity, formulation$\\times$model interaction: $p{=}0.449$ and $p{=}0.860$ under GEE vs.\\ $p{=}0.002$ and $p{=}0.006$ under LPM) reflect the GEE's more conservative cluster-robust inference with $k{=}25$ clusters. The discrepancy in secondary effects reflects cluster count: the cross-complexity model ($k{=}139$) yields reliable sandwich SEs, while the cross-model model ($k{=}25$) falls below the $k{\\geq}40$ threshold recommended for stable cluster-robust inference~\\cite{cameron2008bootstrap}.\n\n\\section{CWM Parseable Bias Analysis}\n\\label{app:parseable_bias}\n\nThe default-to-pass assignment for unparseable \\cwm{} outputs is not random with respect to instance difficulty. Unparseable instances have significantly higher pass rates than parseable ones (74.6\\% vs.\\ 68.3\\%, $\\chi^2$ $p = 5.9 \\times 10^{-10}$), and \\cls{} models achieve higher accuracy on unparseable instances (86.4\\% vs.\\ 79.1\\%, $p = 3.3 \\times 10^{-18}$). This indicates that \\cwm{}'s parsing failures concentrate on simpler, pass-heavy instances where the majority-class default happens to be correct more often. Cross-model Jaccard overlap of unparseable instance sets is 0.46, confirming this pattern is instance-driven (specific inputs consistently cause parsing failure across models) rather than stochastic. The net effect is that \\cwm{}'s reported accuracy is inflated by default-correct assignments on easy instances, while its effective discriminative accuracy on harder instances is substantially lower than the aggregate figure suggests.\n\n\n\\section{Threats to Validity (Full Analysis)}\n\\label{app:threats}\n\nWe identify five potential confounds and assess their impact on our conclusions.\n\n\\paragraph{Checkpoint selection.} Val-based selection is unavailable for runs with NaN validation loss (DeepSeek \\cwm{} repo-level runs, DeepSeek \\cls{} s123), which default to the final epoch checkpoint. A checkpoint ablation on Qwen3-8B \\cls{} s42 quantifies this confound: epoch~1 (ckpt-2200) achieves 85.34\\%, val-selected (ckpt-3600) 84.48\\%, and final epoch (ckpt-6633) 85.29\\%---a $<$1\\pp{} range. The val-selected checkpoint is the lowest, indicating no upward bias from checkpoint selection. The Qwen3-8B \\traj{} comparison (epoch 2: 72.92\\% vs.\\ epoch 3: 70.83\\%) shows a slightly larger ${\\sim}$2\\pp{} shift. For \\cwm{}, the convergence analysis (Appendix~\\ref{app:cwm_convergence}) shows eval loss at the final epoch is 1.8$\\times$ its minimum; however, early-stopped checkpoints retain high unparseable rates, leaving the qualitative ranking unchanged.\n\n\\paragraph{\\cwm{} convergence analysis.}\n\\label{app:cwm_convergence}\nQwen3-8B \\cwm{} repo-level eval loss reaches its minimum within ${\\sim}$5\\% of training (step 300--400 of 6{,}633) and increases monotonically thereafter, with no plateau or recovery (Table~\\ref{tab:cwm_convergence}). This pattern is consistent across all three seeds, confirming systematic overfitting to trace generation rather than stochastic variation. The final-epoch eval loss is ${\\sim}$1.8$\\times$ the optimal value. By contrast, function-level \\cwm{} achieves \\cls{}-equivalent accuracy (TOST $p{=}0.007$) with the same training recipe, indicating that the overfit is specific to repo-level output complexity. Cross-model validation: a DeepSeek-Coder early-stopped checkpoint (s123, epoch~1) achieves 75.45\\% versus 57.31\\% at epoch~3 (s123; +18.14\\pp{}), but retains 66.4\\% unparseable rate, confirming that format collapse emerges early and is not a late-training artifact. No epoch-level checkpoint is available for Qwen3 CWM (only step-level checkpoints at steps 300/400 and late steps ${\\geq}$5800; continuous epoch checkpointing was not enabled for this training run). The convergence analysis (Table~\\ref{tab:cwm_convergence}) shows eval loss minimum at step 300--400 across all three Qwen3 seeds, consistent with DeepSeek-Coder's epoch-1 improvement, providing cross-model evidence that the overtraining pattern generalizes. An early checkpoint (step 400, ${\\sim}$6.5\\% of training, s42) yields 65.17\\% repo-level accuracy with 63.7\\% unparseable rate---comparable to or below final-epoch performance (66.93--67.33\\% accuracy, 60.4--63.9\\% unparseable; s123/s456 at step 6633). This rules out late-training format degradation: collapse is present from early training, and the optimal eval-loss checkpoint does not recover repo-level accuracy.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{\\cwm{} repo-level eval loss across training (Qwen3-8B, 3 seeds). Minimum is reached at step 300--400 (${\\sim}$5\\% of training); subsequent training monotonically increases loss.}\n\\label{tab:cwm_convergence}\n\\begin{tabular}{lccc}\n\\toprule\nStep & s42 & s123 & s456 \\\\\n\\midrule\n300 & 0.291 & \\textbf{0.288} & \\textbf{0.277} \\\\\n400 & \\textbf{0.286} & 0.306 & 0.283 \\\\\n1000 & 0.333 & 0.336 & 0.351 \\\\\n3000 & 0.445 & 0.453 & 0.435 \\\\\n6600 & 0.521 & 0.517 & 0.507 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation sequence length.} \\cwm{} accuracy varies by ${\\sim}$9\\pp{} across evaluation sequence lengths for the same checkpoint (seq2048: ${\\sim}$65\\% vs.\\ seq4096: ${\\sim}$56\\%), driven by unparseable-rate differences that propagate through majority-class default assignment. \\cls{} is invariant to this parameter. Cross-model \\cwm{} comparisons use different eval lengths (Qwen3: 8192, DeepSeek: 4096) and are not directly comparable in absolute terms. A matched-sequence evaluation shows ${\\sim}$1.5\\pp{} difference for \\cls{} (Appendix~\\ref{app:ablations}), insufficient to explain the 18--26\\pp{} gap. Furthermore, increasing Qwen3-8B \\cwm{} evaluation from seq4096 to seq8192 \\emph{raises} the unparseable rate (63.7\\%$\\to$73.8\\%) while changing accuracy by only 0.81\\pp{} (64.36\\%$\\to$65.17\\%); giving the model more generation budget worsens format compliance rather than improving it, confirming that format collapse is a structural bottleneck rather than a truncation artifact. Practitioners must standardize evaluation sequence length for generation-based formulations.\n\n\\paragraph{Preprocessing.} DeepSeek \\cls{} accuracy ranges from 82.61\\% (s42, drop preprocessing) to 74.93\\% (s123, truncate preprocessing), a 7.68\\pp{} spread that conflates preprocessing strategy, checkpoint selection method, and seed. The two strategies produce different effective training sets (67,343 vs.\\ 70,748 samples) and different checkpoint selection regimes. The qualitative ranking \\cls{} $>$ \\cwm{} holds under both strategies (Table~\\ref{tab:taxonomy}).\n\n\\paragraph{\\traj{} training regime.} \\traj{} uses a different training configuration: smaller training set (${\\sim}$400 repo-level variants vs.\\ ${\\sim}$70K per-test instances), higher learning rate ($2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$), and variant-level labels. This asymmetry is inherent to the formulation (trajectory-level labels are only available at variant granularity), but precludes training-data-controlled comparison at repo level. The downsample ablation confirms the \\cls{} formulation advantage persists at matched data volume (80.74\\% vs.\\ 72.92\\%; Appendix~\\ref{app:downsample}), though it controls for training volume but not label granularity (per-test vs.\\ variant-level). Crucially, \\traj{} achieves statistical equivalence with \\cls{} at function level (${\\leq}$1.3\\pp{}, \\S\\ref{sec:func_results}), demonstrating the formulation itself is viable; the repo-level gap attribution remains uncertain: data volume (${\\sim}$400 variants vs.\\ ${\\sim}$70K per-test instances) and label granularity (variant-level vs.\\ per-test) are both plausible confounds that cannot be separately controlled.\n\n\\paragraph{\\cwm{} scale and pretraining.} Our \\cwm{} baseline uses 4--8B LoRA fine-tuning without execution trace pretraining. The original Code World Model~\\cite{meta2025cwm} uses 32B parameters with mid-training on execution traces, a fundamentally different training regime. At larger scale or with execution-trace pretraining, the generation bottleneck observed here may diminish: larger models produce more coherent long-form outputs, and execution trace exposure may improve output format compliance. This is the primary limitation: all repo-level \\cwm{} conclusions are conditional on the ${\\leq}$8B LoRA regime.\n\nDespite these confounds, the repo-level \\cls{}--\\cwm{} gap (18--26\\pp{}) exceeds any single assessed confound. Even under worst-case compounding (${\\sim}$11.5\\pp{}), the gap retains ${\\geq}$7.5\\pp{} margin; confounds predominantly disadvantage \\cwm{}. However, correlated confounds and limited seed coverage mean definitive causal attribution requires multi-seed replication. At $n{=}48$, the minimum detectable effect (MDE) is ${\\sim}$25\\pp{}~\\cite{hoenig2001}; the \\cls{}--\\cwm{} gap (29--35\\pp{}) exceeds this threshold, while the \\cls{}--\\traj{} gap ($<$10\\pp{}) falls below it, consistent with our TOST equivalence finding. Holm-Bonferroni correction across the five primary comparisons ($k{=}5$; Table~\\ref{tab:holm}) confirms the \\cls{}--\\cwm{} gap (adjusted $p{=}0.015$) and function-level \\cls{}--\\cwm{} equivalence (adjusted $p{=}0.028$); function-level \\cls{}--\\traj{} equivalence does not survive correction (adjusted $p{=}0.075$), nor does the repo-level \\cwm{}--\\traj{} comparison (adjusted $p{=}0.078$). The consistent direction across both model families and all tested configurations supports a formulation-level explanation, though definitive causal attribution requires future experiments addressing each confound individually.\n\n\n\\paragraph{Extended validity discussion.}\n\\label{app:limitations}\nThe same-size 4B comparison uses a single seed; \\cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\\% test accuracy (+2.4\\pp{} above majority baseline); val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The \\cwm{} 8B comparison uses 3 seeds per model. The validation and test sets have zero problem overlap but differ in mutation type composition (Table~\\ref{tab:mutation_distribution}): \\texttt{operator\\_swap} shifts from 19.1\\% (val) to 34.3\\% (test), the largest single-type distribution mismatch (+15.2\\pp{}). All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences. Our training data is synthetically constructed from mutation operators rather than real developer patches. While mutation testing literature establishes that mutants are reasonable proxies for real faults in test effectiveness studies~\\cite{andrews2005mutation,just2014mutants}, these findings concern mutation \\emph{adequacy} (whether tests that kill mutants also detect real faults), not whether verifiers trained on mutants transfer to real patches. However, the coupling effect underlying these results supports \\emph{relative ranking} validity: a domain shift from synthetic mutations to real bugs may affect absolute accuracy levels, but our core finding---that formulation choice matters at repo level but not function level---concerns relative performance ordering, which is expected to be preserved under distributional shifts that affect all formulations equally. The synthetic-to-real transfer gap for absolute accuracy remains untested. The \\traj{} training configuration differs from \\cls{}/\\cwm{}: smaller training set (${\\sim}$400 vs.\\ ${\\sim}$70K instances), different learning rate ($2{\\times}10^{-4}$ vs.\\ $5{\\times}10^{-5}$), and variant-level evaluation ($n{=}48$ vs.\\ per-test $n{=}9{,}784$). The function-level \\cls{}--\\traj{} TOST equivalence ($p = 0.025$, seed-level paired, $\\pm$2\\pp{}) is computed on 523 matched variant-level instances across 5 seeds; 2 of 5 seeds use NF4 quantization. Restricting to three bfloat16 seeds yields a comparable mean gap ($-$0.45\\pp{}) but wider confidence interval (df${=}$2); the TOST $p$-value increases to 0.128, which reflects reduced statistical power rather than a shift in the point estimate. The NF4 seeds contribute precision (narrowing the CI) without shifting the mean, consistent with precision being comparable across both quantization levels at function level. Repo-level \\cls{}--\\traj{} comparison should be interpreted with caution due to configuration and granularity differences.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform the related-work section.\n\\end{itemize}\n",
      "numLines": 576,
      "startLine": 1,
      "totalLines": 576
    }
  }
}
```

</details>

---


### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_013259xMsSQXBSSKbMrUM94f`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "07de5244-b2c4-4786-8027-95184b55f15b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVTBykmq9zNh5u5794g9f1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 26412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 576
      },
      "output_tokens": 52,
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

_source line 21 · 2026-05-23T19:16:51.550Z_

<details><summary>↩ Tool result · `toolu_013259xMsSQXBSSKbMrUM94f`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. CodeScaler~\cite{zhu2026codescaler} trains execution-free reward models for both RL and test-time scaling. Verification formulations span trajectory-level reward~\cite{shum2025swerm}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. DreamPRM~\cite{dreamprm2025code} treats functions as process steps with label correction; CodePRM~\cite{li2025codeprm} leverages execution feedback for step-level rewards. These approaches optimize reward quality within a fixed formulation; we compare across output formulations at matched capacity. GenRM~\cite{hosseini2025genrm} and GenPRM~\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formulation (\cwm{}) does not outperform the discriminative one (\cls{}), suggesting that the generation advantage may be domain-specific. CodeRM~\cite{ma2025coderm} demonstrates that test-level reward granularity improves code generation quality, corroborating our finding that per-test classification provides diagnostic value. In reward modeling terminology, per-test supervision (\cls{}) is analogous to process-level reward (PRM, with tests as reasoning steps), while per-patch verdict (\traj{}) corresponds to outcome-level reward (ORM); \cwm{} serves as a generative verifier~\cite{hosseini2025genrm}. We additionally vary the output format (\cwm{} generation vs.\ \cls{} classification).
9	
10	\paragraph{Repair, Mutation Testing, and Task Framing.}
11	CodeRL~\cite{le2022coderl}, AlphaCode~\cite{li2022alphacode,alphacode2023team}, and Reflexion~\cite{shinn2023reflexion} use execution feedback for repair. SWE-bench~\cite{jimenez2024swebench,chowdhury2024swebenchverified} provides benchmarks; SWE-agent~\cite{yang2024sweagent} and Agentless~\cite{xia2024agentless} demonstrate pipelines where verification is a bottleneck~\cite{yang2025aprsurvey}. Predictive mutation testing~\cite{tufano2019predictive,kim2022predictive,wang2024llmmutation,jain2023contextual} shares our per-test structure. \citet{raffel2020t5} showed that task framing affects performance across NLP tasks; we extend this to code verification, finding that complexity moderates the classification--generation tradeoff.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "1c149f73-3be2-4b55-9aac-a54e97de0c5f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Execution Simulation and Verification.}\nExecution trace generation improves code reasoning~\\cite{nye2021scratchpad}, with extensions to output prediction~\\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\\cite{abdollahi2025demystifying}, and error detection~\\cite{li2024redo}. CRUXEval~\\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. CodeScaler~\\cite{zhu2026codescaler} trains execution-free reward models for both RL and test-time scaling. Verification formulations span trajectory-level reward~\\cite{shum2025swerm}, process-level feedback~\\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\\cite{ni2023lever,chen2023codet}, learned metrics~\\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\\cite{wang2026verpo,tang2026execverify}. Aletheia~\\cite{venkatkrishna2026aletheia} compares training recipes; we compare \\emph{formulations}. Test-time scaling~\\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.\n\n\\paragraph{Process vs.\\ Outcome Supervision.}\nPRMs outperform ORMs for math reasoning~\\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\\cite{ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. DreamPRM~\\cite{dreamprm2025code} treats functions as process steps with label correction; CodePRM~\\cite{li2025codeprm} leverages execution feedback for step-level rewards. These approaches optimize reward quality within a fixed formulation; we compare across output formulations at matched capacity. GenRM~\\cite{hosseini2025genrm} and GenPRM~\\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formulation (\\cwm{}) does not outperform the discriminative one (\\cls{}), suggesting that the generation advantage may be domain-specific. CodeRM~\\cite{ma2025coderm} demonstrates that test-level reward granularity improves code generation quality, corroborating our finding that per-test classification provides diagnostic value. In reward modeling terminology, per-test supervision (\\cls{}) is analogous to process-level reward (PRM, with tests as reasoning steps), while per-patch verdict (\\traj{}) corresponds to outcome-level reward (ORM); \\cwm{} serves as a generative verifier~\\cite{hosseini2025genrm}. We additionally vary the output format (\\cwm{} generation vs.\\ \\cls{} classification).\n\n\\paragraph{Repair, Mutation Testing, and Task Framing.}\nCodeRL~\\cite{le2022coderl}, AlphaCode~\\cite{li2022alphacode,alphacode2023team}, and Reflexion~\\cite{shinn2023reflexion} use execution feedback for repair. SWE-bench~\\cite{jimenez2024swebench,chowdhury2024swebenchverified} provides benchmarks; SWE-agent~\\cite{yang2024sweagent} and Agentless~\\cite{xia2024agentless} demonstrate pipelines where verification is a bottleneck~\\cite{yang2025aprsurvey}. Predictive mutation testing~\\cite{tufano2019predictive,kim2022predictive,wang2024llmmutation,jain2023contextual} shares our per-test structure. \\citet{raffel2020t5} showed that task framing affects performance across NLP tasks; we extend this to code verification, finding that complexity moderates the classification--generation tradeoff.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---


### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AKQz8PbmCHVhGZzGLgYyAa`</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "filters": {
    "conclusion": "success"
  },
  "limit": 0,
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "b67514ae-a3a1-4ded-9fe4-e71592d78108",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVTBykmq9zNh5u5794g9f1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 26412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 576
      },
      "output_tokens": 52,
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

_source line 23 · 2026-05-23T19:16:54.070Z_

<details><summary>↩ Tool result · `toolu_01AKQz8PbmCHVhGZzGLgYyAa`</summary>

```text
Error: result (259,127 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/mcp-agent-ml-research-read_registry-1779563814054.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/mcp-agent-ml-research-read_registry-1779563814054.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "ff9352e2-705a-46cc-96f0-2048d60da49f",
  "tool_use_result": {
    "content": "Error: result (259,127 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/mcp-agent-ml-research-read_registry-1779563814054.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/mcp-agent-ml-research-read_registry-1779563814054.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"deepseek-cwm-repo-s456-train-v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-20T08:04:20.919Z\", \"updated_at\": \"2026-05-23T16:14:08.119Z\", \"hypothesis\": \"DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。\", \"parent\": \"deepseek-cwm-repo-s456-train\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"completed_at\": \"2026-05-20T09:22:41.733Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python train_unified.py --data_dir data/ --task cwm --train_file swebench_full/swebench_train.jsonl --seed 456 --output_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo_s456_v2/\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"data_path\": \"data/swebench_full/swebench_train.jsonl\", \"data_count\": 70748, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 456, \"pid\": 949112, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training, not eval)\"}, \"metrics\": {\"train_loss\": 0.02127, \"eval_loss\": 5.2837, \"total_steps\": 12627, \"training_time_hours\": 27.55}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s456_v2/checkpoint-12627\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-cwm-repo-s456-train-v2.log\"}, \"traj14b-func-s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:04:54.197Z\", \"updated_at\": \"2026-05-23T11:12:04.889Z\", \"hypothesis\": \"TRAJ 14B (seed 456) 补完 Table 2 的 14B TRAJ 行。与 CLS/CWM 14B 对比验证三公式在 14B 的 scaling 趋势。4B→8B TRAJ scaling +2.13pp，14B 应保持或扩大趋势。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python3 train_traj_verifier.py --data_dir data/ --model_name /dev/shm/Qwen3-14B --output_dir /root/autodl-tmp/checkpoints/traj14b-func-s456/ --seed 456 --lr 2e-4 --epochs 3 --lora_rank 16 --lora_alpha 32 --batch_size 1 --grad_accumulation 32 --run_name traj14b-func-s456 --no_wandb\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/traj_train.jsonl\", \"data_count\": 8052, \"model_name\": \"Qwen3-14B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/traj14b-func-s456/best\", \"log_path\": \"/tmp/traj14b_s456.log\", \"pid\": 265996, \"batch_size\": 1, \"grad_accumulation\": 32, \"effective_batch_size\": 32}, \"conclusion\": \"success\", \"metrics\": {\"best_eval_loss\": 0.0971, \"best_checkpoint\": \"best\", \"epochs\": 3, \"accuracy\": 88.28, \"dtype\": \"bf16\", \"n_test\": 1032}, \"completed_at\": \"2026-05-23T10:50:21.483Z\"}, \"traj14b-func-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:04:52.673Z\", \"updated_at\": \"2026-05-23T11:12:03.596Z\", \"hypothesis\": \"TRAJ 14B (seed 123) 补完 Table 2 的 14B TRAJ 行。与 CLS/CWM 14B 对比验证三公式在 14B 的 scaling 趋势。4B→8B TRAJ scaling +2.13pp，14B 应保持或扩大趋势。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python3 train_traj_verifier.py --data_dir data/ --model_name /dev/shm/Qwen3-14B --output_dir /root/autodl-tmp/checkpoints/traj14b-func-s123/ --seed 123 --lr 2e-4 --epochs 3 --lora_rank 16 --lora_alpha 32 --batch_size 1 --grad_accumulation 32 --run_name traj14b-func-s123 --no_wandb\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/traj_train.jsonl\", \"data_count\": 8052, \"model_name\": \"Qwen3-14B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/traj14b-func-s123/best\", \"log_path\": \"/tmp/traj14b_s123.log\", \"pid\": 265560, \"batch_size\": 1, \"grad_accumulation\": 32, \"effective_batch_size\": 32}, \"metrics\": {\"best_eval_loss\": 0.0836, \"best_checkpoint\": \"checkpoint-252\", \"epochs\": 3, \"accuracy\": 88.57, \"dtype\": \"bf16\", \"n_test\": 1032}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T10:50:33.782Z\"}, \"traj14b-func-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:04:50.993Z\", \"updated_at\": \"2026-05-23T11:12:01.847Z\", \"hypothesis\": \"TRAJ 14B (seed 42) 补完 Table 2 的 14B TRAJ 行。与 CLS/CWM 14B 对比验证三公式在 14B 的 scaling 趋势。4B→8B TRAJ scaling +2.13pp，14B 应保持或扩大趋势。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python3 train_traj_verifier.py --data_dir data/ --model_name /dev/shm/Qwen3-14B --output_dir /root/autodl-tmp/checkpoints/traj14b-func-s42/ --seed 42 --lr 2e-4 --epochs 3 --lora_rank 16 --lora_alpha 32 --batch_size 1 --grad_accumulation 32 --run_name traj14b-func-s42 --no_wandb\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/traj_train.jsonl\", \"data_count\": 8052, \"model_name\": \"Qwen3-14B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/traj14b-func-s42/best\", \"log_path\": \"/tmp/traj14b_s42.log\", \"pid\": 265154, \"batch_size\": 1, \"grad_accumulation\": 32, \"effective_batch_size\": 32}, \"conclusion\": \"success\", \"metrics\": {\"best_eval_loss\": 0.0958, \"best_checkpoint\": \"best\", \"epochs\": 3, \"accuracy\": 89.73, \"dtype\": \"bf16\", \"n_test\": 1032}, \"completed_at\": \"2026-05-23T10:50:16.737Z\"}, \"cwm14b-func-s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:44:11.674Z\", \"updated_at\": \"2026-05-23T08:01:04.687Z\", \"spec\": {\"command\": \"python3 train_unified.py --task cwm --seed 456\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"241623\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm14b-func-s456.log\", \"submitted_at\": \"2026-05-23T04:44:11.046Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/cwm_train.jsonl\", \"data_count\": 0, \"model_name\": \"Qwen3-14B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/cwm14b-func-s456/best\", \"eval_predictions\": \"/root/autodl-tmp/eval_results/cwm14b_func_s456/eval_cwm_results_predictions.json\", \"wall_clock_seconds\": 11813.6, \"gpu_hours\": 3.28}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 90.26, \"unparseable\": 0, \"best_checkpoint\": \"best\", \"dtype\": \"bf16\", \"n_test\": 1890}, \"hypothesis\": \"Qwen3-14B CWM (seed 456) should remain equivalent to CLS within ±2pp SESOI at function level, consistent with 4B/8B equivalence. Multi-seed replication (3 seeds) enables clustered bootstrap TOST to confirm capacity-dependent convergence.\", \"completed_at\": \"2026-05-23T08:01:04.687Z\"}, \"cwm14b-func-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:44:09.178Z\", \"updated_at\": \"2026-05-23T08:01:01.936Z\", \"spec\": {\"command\": \"python3 train_unified.py --task cwm --seed 123\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"241378\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm14b-func-s123.log\", \"submitted_at\": \"2026-05-23T04:44:08.472Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/cwm_train.jsonl\", \"data_count\": 0, \"model_name\": \"Qwen3-14B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/cwm14b-func-s123/best\", \"eval_predictions\": \"/root/autodl-tmp/eval_results/cwm14b_func_s123/eval_cwm_results_predictions.json\", \"wall_clock_seconds\": 11813.5, \"gpu_hours\": 3.28}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 88.99, \"unparseable\": 0, \"best_checkpoint\": \"best\", \"dtype\": \"bf16\", \"n_test\": 1890}, \"hypothesis\": \"Qwen3-14B CWM (seed 123) should remain equivalent to CLS within ±2pp SESOI at function level, consistent with 4B/8B equivalence. Multi-seed replication (3 seeds) enables clustered bootstrap TOST to confirm capacity-dependent convergence.\", \"completed_at\": \"2026-05-23T08:01:01.936Z\"}, \"cls14b-func-s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:44:06.214Z\", \"updated_at\": \"2026-05-23T07:48:21.582Z\", \"spec\": {\"command\": \"python3 train_unified.py --task cls --seed 456\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"241135\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls14b-func-s456.log\", \"submitted_at\": \"2026-05-23T04:44:05.582Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train.jsonl\", \"data_count\": 0, \"model_name\": \"Qwen3-14B\", \"seed\": 456, \"wall_clock_seconds\": 11056.0, \"gpu_hours\": 3.07}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/cls14b-func-s456/checkpoint-478\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls14b-func-s456.log\", \"metrics\": {\"accuracy\": 89.79, \"f1_fail\": 89.45, \"f1_pass\": 90.11, \"precision_fail\": 89.2, \"recall_fail\": 89.69, \"precision_pass\": 90.34, \"recall_pass\": 89.88, \"unparseable\": 0, \"best_checkpoint\": \"checkpoint-478\", \"dtype\": \"bf16\", \"best_train_loss\": 0.0659}, \"hypothesis\": \"Qwen3-14B LoRA CLS bf16 eval (seed 456) should exceed NF4 accuracy (89.47%) from s42-v2, confirming that quantization was a confound in the 8B→14B regression. Multi-seed replication to verify s42 result is not a seed artifact.\", \"completed_at\": \"2026-05-23T07:48:21.582Z\"}, \"cls14b-func-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:44:03.567Z\", \"updated_at\": \"2026-05-23T07:48:19.344Z\", \"spec\": {\"command\": \"python3 train_unified.py --task cls --seed 123\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"241053\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls14b-func-s123.log\", \"submitted_at\": \"2026-05-23T04:44:02.810Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train.jsonl\", \"data_count\": 0, \"model_name\": \"Qwen3-14B\", \"seed\": 123, \"wall_clock_seconds\": 11056.5, \"gpu_hours\": 3.07}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/cls14b-func-s123/checkpoint-956\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls14b-func-s123.log\", \"metrics\": {\"accuracy\": 90.79, \"f1_fail\": 90.58, \"f1_pass\": 90.99, \"precision_fail\": 89.42, \"recall_fail\": 91.78, \"precision_pass\": 92.14, \"recall_pass\": 89.88, \"unparseable\": 0, \"best_checkpoint\": \"checkpoint-956\", \"dtype\": \"bf16\", \"best_train_loss\": 0.063}, \"hypothesis\": \"Qwen3-14B LoRA CLS bf16 eval (seed 123) should exceed NF4 accuracy (89.47%) from s42-v2, confirming that quantization was a confound in the 8B→14B regression. Multi-seed replication to verify s42 result is not a seed artifact.\", \"completed_at\": \"2026-05-23T07:48:19.344Z\"}, \"cls14b-func-s42-v2-bf16-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T02:30:53.514Z\", \"updated_at\": \"2026-05-23T02:46:45.777Z\", \"hypothesis\": \"CLS 14B bf16 eval should yield higher accuracy than NF4 eval (89.47%), eliminating quantization confound. If bf16 accuracy > 89.47%, the CLS 8B→14B regression is an NF4 artifact; if bf16 ≈ 89.47%, the regression is real.\", \"conclusion\": \"success\", \"spec\": null}, \"cls14b-func-s42-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:36:01.821Z\", \"updated_at\": \"2026-05-23T02:26:34.263Z\", \"hypothesis\": \"Qwen3-14B QLoRA CLS on function-level data (15K train.jsonl) should exceed 8B baseline (90.48%) by ≥1pp, confirming CLS scaling trend 4B→8B→14B. v2 fixes data bug: v1 used 70K repo-level swebench_full instead of 15K function-level train.jsonl.\", \"parent\": \"cls14b-func-s42\", \"spec\": {\"command\": \"python3 train_unified.py --task cls --train_file train.jsonl --val_file val.jsonl --model Qwen3-14B --epochs 3 --quantize_4bit\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen3-14B\", \"seed\": 42, \"pid\": \"215642\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/exec-sim-repair-verifier/cls14b-func-s42-v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_cls14b_func_s42_v2/checkpoint-956\", \"checkpoint_source\": \"pretrained Qwen3-14B (fresh LoRA)\", \"eval_data\": \"data/test.jsonl (1890 samples)\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 89.47, \"f1_fail\": 89.02, \"f1_pass\": 89.88, \"unparseable\": 0, \"checkpoint\": \"checkpoint-956\", \"delta_vs_8b\": -0.47, \"cls_cwm_gap_14b\": 0.21}, \"completed_at\": \"2026-05-23T02:26:34.263Z\"}, \"cwm14b-func-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:23:21.299Z\", \"updated_at\": \"2026-05-23T00:47:46.413Z\", \"hypothesis\": \"Qwen3-14B QLoRA CWM at function level should remain equivalent to CLS (within ±2pp SESOI), consistent with 4B/8B equivalence pattern. If CWM remains flat while CLS scales, the CLS-CWM gap at 14B widens further, strengthening the scaling divergence narrative for §5.3.\", \"spec\": {\"command\": \"train_unified.py --task cwm --model Qwen3-14B --epochs 3 --quantize_4bit\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/cwm_train.jsonl\", \"data_count\": 15280, \"model_name\": \"Qwen3-14B\", \"seed\": 42, \"gpu\": \"cuda:2\", \"pid\": \"211042\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm14b-func-s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_cwm14b_func_s42/checkpoint-956\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 89.3, \"f1_fail\": 88.3, \"f1_pass\": 90.1, \"exact_match_rate\": 86.6, \"unparseable\": 0, \"checkpoint\": \"checkpoint-956\", \"delta_vs_8b\": 1.97}, \"completed_at\": \"2026-05-23T00:47:46.413Z\"}, \"8b-baseline-rerun\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:36:27.917Z\", \"updated_at\": \"2026-05-22T22:02:47.948Z\", \"hypothesis\": \"Qwen3-8B 0-shot/3-shot baseline rerun with unified NF4 quantization and identical prompt to 14B baseline, ensuring fair comparison. Expected: 0-shot ~52%, 3-shot ~60%.\", \"spec\": {\"command\": \"python3 eval_14b_baseline.py --model_path /root/autodl-tmp/models/Qwen/Qwen3-8B --num_shots 0 then --num_shots 3\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"gpu\": [\"cuda:1\"], \"checkpoint_path\": \"N/A (0-shot/3-shot eval, no fine-tuning)\", \"log_path\": \"/root/autodl-tmp/results_8b_0shot_rerun.json + results_8b_3shot_nf4_rerun.json\"}, \"conclusion\": \"success\", \"metrics\": {\"0shot_accuracy\": 60.53, \"0shot_f1_macro\": 55.73, \"3shot_accuracy\": 60.42, \"3shot_f1_macro\": 56.09, \"0shot_unparseable\": 5, \"3shot_unparseable\": 1}, \"completed_at\": \"2026-05-22T22:02:47.948Z\"}, \"14b-baseline-0shot-3shot-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:42:42.654Z\", \"updated_at\": \"2026-05-22T20:32:47.881Z\", \"hypothesis\": \"Qwen3-14B 0-shot and 3-shot baselines on function-level CLS should be comparable to or below 8B baselines (0-shot ~52%, 3-shot ~60%), establishing that scale alone without fine-tuning does not close the gap to fine-tuned models.\", \"parent\": \"14b-baseline-0shot-3shot\", \"spec\": {\"pid\": \"202994\", \"server\": \"seetacloud-westd-4x5090\", \"command\": \"bash /tmp/run_14b_eval.sh\", \"model_name\": \"Qwen3-14B\", \"gpu\": \"cuda:1\", \"data_path\": \"swebench_full/swebench_test_func.jsonl\", \"data_count\": 0, \"seed\": 0, \"checkpoint_source\": \"Qwen/Qwen3-14B (base model, no fine-tuning)\", \"eval_data\": \"swebench_full/swebench_test_func.jsonl\"}, \"conclusion\": \"success\", \"metrics\": {\"0shot\": {\"accuracy\": 66.24, \"gap_vs_majority\": 14.5, \"f1_fail\": 72.99, \"f1_pass\": 55.01, \"f1_macro\": 64, \"unparseable\": 0, \"n\": 1890}, \"3shot\": {\"accuracy\": 73.12, \"gap_vs_majority\": 21.38, \"f1_fail\": 75.79, \"f1_pass\": 69.8, \"f1_macro\": 72.79, \"unparseable\": 0, \"n\": 1890}}, \"checkpoint_path\": \"N/A (eval-only, no checkpoint)\", \"log_path\": \"/tmp/14b_eval.log\", \"completed_at\": \"2026-05-22T20:27:04.106Z\"}, \"deepseek-cwm-repo-s123-eval-1epoch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:16:05.664Z\", \"updated_at\": \"2026-05-22T14:51:28.766Z\", \"hypothesis\": \"Eval DeepSeek CWM repo-level s123 1-epoch checkpoint (checkpoint-4209)。验证 appendix cwm_convergence 中引用的 early-stopping 数据 (75.45% acc / 66.4% unparseable) 是否在干净 eval 下可复现。\", \"parent\": \"deepseek-cwm-repo-s123-train-v2\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 75.45, \"f1_macro\": 65.08, \"f1_fail\": 46.05, \"f1_pass\": 84.11, \"unparseable_rate\": 66.4, \"unparseable_count\": 6500, \"n_instances\": 9784, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 2.49, \"truncated\": 0}, \"spec\": {\"command\": \"bash eval_deepseek_cwm_s123_1epoch.sh (CVD=1, batch=4, checkpoint-4209)\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 123, \"pid\": 111113, \"gpu\": \"GPU 1 (RTX 5090 32GB)\", \"checkpoint_source\": \"deepseek-cwm-repo-s123-train-v2 checkpoint-4209 (epoch 1)\", \"eval_data\": \"repo-level CWM test set (9784 per-test samples)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123_v2/checkpoint-4209\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/eval_deepseek_cwm_s123_1epoch.log\"}, \"log_path\": \"/home/sonny/exec-sim-repair-verifier/eval_deepseek_cwm_s123_1epoch.log\", \"completed_at\": \"2026-05-22T14:51:28.766Z\"}, \"qwen3-8b-cwm-repo-s456-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T22:07:40.156Z\", \"updated_at\": \"2026-05-22T12:30:37.182Z\", \"hypothesis\": \"Eval Qwen3-8B CWM repo-level s456 checkpoint-6633。与 s42/s123 对比验证 CWM repo-level 跨 seed 一致性，组成 3-seed coverage 用于论文 Table 3。\", \"parent\": \"qwen3-8b-cwm-repo-s456-train-v4\", \"spec\": {\"command\": \"bash eval_qwen_cwm_s456.sh (CVD=3, batch=4, checkpoint-6633)\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"swebench_full/swebench_test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 456, \"pid\": 96722, \"gpu\": \"GPU 3 (RTX 5090 32GB)\", \"checkpoint_source\": \"qwen3-8b-cwm-repo-s456-train-v4 checkpoint-6633\", \"eval_data\": \"repo-level CWM test set (1890 samples)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cwm_8b_s456/checkpoint-6633\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/eval_qwen_cwm_s456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T12:30:35.024Z\", \"metrics\": {\"accuracy\": 66.93, \"f1_macro\": 51.97, \"f1_fail\": 25.16, \"f1_pass\": 78.77, \"unparseable_rate\": 60.39, \"unparseable_count\": 5909, \"n_instances\": 9784, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -6.03, \"precision_fail\": 32.42, \"recall_fail\": 20.56, \"checkpoint_step\": 6633}}, \"deepseek-cwm-repo-s123-e3-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T01:07:53.274Z\", \"updated_at\": \"2026-05-22T11:49:21.356Z\", \"hypothesis\": \"Eval DeepSeek CWM repo-level s123 epoch 3 final checkpoint (checkpoint-12627)。与 s42 (61.49%) 和 s456 (~56%) 对比，验证 CWM repo-level 跨 seed 一致性。\", \"parent\": \"deepseek-cwm-repo-s123\", \"spec\": {\"command\": \"eval_deepseek_cwm_s123_v2.sh (CVD=2, batch=4, checkpoint-12627)\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 123, \"pid\": 100824, \"gpu\": \"GPU 2 (RTX 5090 32GB)\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123_v2/checkpoint-12627\", \"eval_data\": \"repo-level CWM test set (9784 per-test samples)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123/checkpoint-12627\", \"log_path\": \"/root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_v2_eval/final_eval.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:49:14.792Z\", \"metrics\": {\"accuracy\": 57.31, \"f1_macro\": 51.79, \"f1_fail\": 35.49, \"f1_pass\": 68.1, \"precision_fail\": 30.01, \"precision_pass\": 74.86, \"recall_fail\": 43.42, \"recall_pass\": 62.45, \"unparseable_count\": 5028, \"unparseable_rate\": 51.39, \"n_instances\": 9784, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -15.65}}, \"qwen3-8b-cwm-repo-s123-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T02:10:32.994Z\", \"updated_at\": \"2026-05-22T11:21:32.743Z\", \"hypothesis\": \"Qwen3-8B CWM model trained on repo-level data with seed 123 will achieve accuracy above majority baseline on the test set, demonstrating that the counterfactual reasoning signal transfers across seeds\", \"parent\": \"qwen3-8b-cwm-repo-s123-train-v4\", \"spec\": {\"command\": \"bash run_qwen_cwm_s123_eval.sh\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 123, \"pid\": 94100, \"gpu\": \"GPU 0 (RTX 5090 32GB)\", \"checkpoint_source\": \"qwen3-8b-cwm-repo-s123-train-v4 checkpoint-6633\", \"eval_data\": \"repo-level CWM test set (9784 per-test samples)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cwm_8b_s123/checkpoint-6633\", \"log_path\": \"/root/autodl-tmp/eval_results/qwen3_8b_cwm_repo_s123_eval/eval_repo_cwm.json\", \"output_dir\": \"/root/autodl-tmp/eval_results/qwen3_8b_cwm_repo_s123_eval\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 67.33, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -5.62, \"f1_fail\": 32.94, \"f1_pass\": 78.41, \"f1_macro\": 55.67, \"precision_fail\": 37.03, \"precision_pass\": 75.72, \"recall_fail\": 29.67, \"recall_pass\": 81.3, \"unparseable_count\": 6257, \"unparseable_rate\": 63.95, \"n_instances\": 9784, \"checkpoint_step\": 6633}, \"completed_at\": \"2026-05-22T11:20:18.566Z\"}, \"deepseek-cwm-repo-s456-e3-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:13:08.749Z\", \"updated_at\": \"2026-05-22T02:20:45.706Z\", \"hypothesis\": \"Eval DeepSeek CWM repo-level s456 epoch 3 final checkpoint (checkpoint-12627)。与 s42 epoch 3 (61.49% @seq4096) 对比，验证 CWM repo-level 跨 seed 一致性。组成 3-seed coverage (42/123/456) 用于论文 Table 3。\", \"parent\": \"deepseek-cwm-repo-s456-train-v2\", \"spec\": {\"command\": \"bash eval_deepseek_cwm_s456_v2.sh (fixed sort, checkpoint-12627)\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 456, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s456_v2/checkpoint-12627\", \"eval_data\": \"swebench test set (9784 samples)\", \"data_path\": \"data/swebench_full/\", \"data_count\": 9784, \"log_path\": \"/home/sonny/exec-sim-repair-verifier/eval_deepseek_cwm_s456.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s456_v2/checkpoint-12627\"}, \"extra\": {\"note\": \"status restored to RUNNING: auto-resolver falsely marked as failed (process dead 5×) but PID 63490 confirmed alive at 524/9784 (57.6% acc). Cron still monitoring.\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 56.11, \"unparseable_rate\": 56.97, \"parseable_only_accuracy\": 32.45, \"f1_macro\": 50.6, \"samples\": 9784}, \"completed_at\": \"2026-05-22T02:20:45.706Z\"}, \"deepseek-cwm-repo-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:29:52.481Z\", \"updated_at\": \"2026-05-22T01:07:45.373Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 python3 train_unified.py --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/ --train_file swebench_full/swebench_train.jsonl --val_file swebench_full/swebench_val.jsonl --task cwm --lora_rank 16 --lora_alpha 32 --max_seq_length 2048 --epochs 3 --batch_size 2 --grad_accumulation 8 --lr 2e-4 --seed 123 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123/ --run_name deepseek-cwm-repo-s123\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"542901\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/logs/\", \"submitted_at\": \"2026-05-16T17:30:20Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/swebench_full/swebench_train.jsonl\", \"data_count\": 70748, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123/checkpoint-12627\", \"wall_clock_seconds\": 81656.1, \"gpu_hours\": 22.68}, \"hypothesis\": \"DeepSeek CWM repo-level seed 123 replication — multi-seed evidence to address Dream review concern about single-seed repo results\", \"reproduce\": {\"finished_at\": \"2026-05-17T16:11:18.726Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T16:11:16.146Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T16:11:32.178598+00:00\"}]}, \"notes\": \"失败原因: 进程在 step 9489/13266 (71%, epoch 3 中途) 静默死亡, 无 Traceback/Error | 诊断中: worker_diagnose_deepseek-cwm-repo-s123 正在查系统日志和 checkpoint 可用性 | 已有成果: 至少有 epoch 1-2 checkpoints, eval worker 正在评估\", \"metrics\": {\"accuracy\": 61.9, \"majority_baseline\": 72.96, \"gap_vs_majority\": -11.06, \"f1_macro\": 51.5, \"f1_pass\": 73.96, \"f1_fail\": 29.04, \"recall_pass\": 74.15, \"recall_fail\": 28.84, \"unparseable_rate\": 65.53, \"total\": 9784, \"correct\": 6056, \"truncated\": 0, \"checkpoint\": \"checkpoint-8844 (epoch 2)\", \"seq_length\": 4096, \"source_file\": \"/root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_test/eval_deepseek_cwm_repo_s123.json\"}}, \"qwen3-8b-cwm-repo-s456-train-v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:47:24.823Z\", \"updated_at\": \"2026-05-21T22:06:35.049Z\", \"hypothesis\": \"Qwen3-8B CWM repo-level s456 训练恢复 (v4): 从 v3 的 checkpoint-6100 恢复（v3 被 SIGTERM 在 step 6200 杀死），跑完剩余 ~533 步。与 s42 config 一致 (train_repo_cwm.py, bs=1, ga=32, lr=5e-5, seq2048, epochs=3, lora_r=16)。\", \"parent\": \"\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python train_repo_cwm.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_s456/ --seed 456 --resume_from_checkpoint checkpoint-6100 --max_seq_length 2048 --batch_size 1 --grad_accumulation 32 --lr 5e-5 --epochs 3 --lora_rank 16 --no_wandb\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"83238\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_train.jsonl\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 456, \"log_path\": \"~/runs/exec-sim-repair-verifier/qwen_cwm_s456_resume2.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cwm_8b_s456/checkpoint-6633\", \"log_path\": \"~/runs/exec-sim-repair-verifier/qwen_cwm_s456_resume2.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T22:06:35.049Z\"}, \"qwen3-8b-cwm-repo-s123-train-v4\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-20T01:30:02.379Z\", \"updated_at\": \"2026-05-21T21:56:51.630Z\", \"hypothesis\": \"Qwen3-8B CWM repo-level s123 训练 (v4, OOM 修复后重启): multi-seed replication (2nd seed)。与 s42 config 一致 (train_repo_cwm.py, bs=1, ga=32, lr=5e-5, seq2048, epochs=3, lora_r=16)。预期 CWM repo-level 仍显著低于 CLS (84.83%)。\", \"parent\": \"qwen3-8b-cwm-repo-s123-train-v3\", \"reproduce\": {\"finished_at\": \"2026-05-21T21:35:38.746Z\"}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-20T21:28:57.233Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T21:29:03.263512+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T21:35:43.111452+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"nohup python train_repo_cwm.py --model_name Qwen/Qwen3-8B --seed 123 --output_dir runs/exec-sim-repair-verifier/qwen3-8b-cwm-repo-s123 --batch_size 1 --gradient_accumulation_steps 32 --learning_rate 5e-5 --max_seq_length 2048 --num_epochs 3 --lora_r 16 --lora_alpha 32 --no_wandb --resume_from_checkpoint checkpoint-3000\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"repo-level CWM data (swebench_full/swebench_train.jsonl)\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 123, \"pid\": 4271, \"monitor_pid\": 4871, \"gpu\": \"GPU 0 (RTX 5090 32GB)\", \"resumed_from\": \"checkpoint-3000\", \"remaining_steps\": 3633, \"log_path\": \"/home/sonny/exec-sim-repair-verifier/outputs_qwen3_8b_cwm_repo_s123/\", \"checkpoint_source\": \"checkpoint-3000 (from v3 run killed by SIGTERM)\", \"eval_data\": \"N/A (training, not eval)\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/outputs_qwen3_8b_cwm_repo_s123/checkpoint-6633\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.00873, \"eval_loss\": 0.5166, \"steps_completed\": 6633, \"epochs\": 3, \"training_time_seconds\": 85699}}, \"deepseek-cwm-repo-s42-seq4096-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T12:38:52.444Z\", \"updated_at\": \"2026-05-20T01:20:00.829Z\", \"conclusion\": \"success\", \"hypothesis\": \"DeepSeek CWM s42 eval @seq4096 for cross-model comparison. Previous eval may have used different seq_length. This provides matched seq4096 evaluation for Table 3.\", \"parent\": \"deepseek-cwm-repo\", \"spec\": {\"command\": \"cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-13266 --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --split test --device cuda:0 --max_seq_length 4096 --max_new_tokens 512 --batch_size 4 --output_dir /root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_seq4096/\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"833667\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-cwm-repo-s42-seq4096-eval.log\", \"submitted_at\": \"2026-05-19T12:39:46.560Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_source\": \"deepseek-cwm-repo/checkpoint-13266\", \"eval_data\": \"swebench_test.jsonl\"}, \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:2\", \"reproduce\": {\"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-19T14:07:52.935Z\"}, \"notes\": \"完成后必须检查截断率：max_new_tokens=512（Qwen3用1024），如果截断率>5%需要用max_new_tokens=1024重跑。检查方法：统计输出token数达到512上限的样本比例。\", \"metrics\": {\"accuracy\": 61.49, \"unparseable_rate\": 62.5, \"unparseable_count\": 6115, \"n_instances\": 9784, \"f1_macro\": 43.73, \"truncated\": 0, \"truncated_rate\": 0, \"max_generation_tokens\": 284, \"max_new_tokens_limit\": 512, \"seq_length\": 4096}}, \"deepseek-cls-repo-s456-eval-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T23:19:23.395Z\", \"updated_at\": \"2026-05-20T00:38:25.348Z\", \"hypothesis\": \"DeepSeek CLS repo-level s456 eval: epoch 1 checkpoint-2163 test accuracy。与 s42(82.61%) 对比提供 multi-seed evidence。参考 s42 ablation 显示 epoch 1 可能优于 final epoch。\", \"parent\": \"deepseek-cls-repo-s456-train-v3\", \"spec\": {\"command\": \"cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo_s456_v2/checkpoint-2163 --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --split test --max_seq_length 8192 --batch_size 1 --device cuda:0 --output eval_summary.json\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"876065\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-cls-repo-s456-eval-v2.log\", \"submitted_at\": \"2026-05-19T23:20:03.597Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints_deepseek_cls_repo_s456_v2/checkpoint-2163\", \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 456, \"eval_data\": \"swebench_test\", \"data_count\": 9784, \"data_path\": \"data/swebench_full/swebench_test.jsonl\"}, \"metrics\": {\"accuracy\": 86.15, \"f1_macro\": 80.43, \"f1_fail\": 69.84, \"f1_pass\": 91.01, \"precision_fail\": 84.95, \"recall_fail\": 59.3, \"checkpoint\": \"checkpoint-2163\", \"seq_length\": 8192}, \"conclusion\": \"success\"}, \"cls8b-repo-s456-eval-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T23:19:25.850Z\", \"updated_at\": \"2026-05-20T00:38:24.288Z\", \"hypothesis\": \"Qwen3-8B CLS repo-level s456 eval: 用 val-best checkpoint 评估 test set accuracy。与 s42(84.48%)/s123(85.6%) 组成 3-seed coverage，回应 N1 审稿意见。\", \"parent\": \"cls8b-repo-s456-train-v2\", \"spec\": {\"command\": \"cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s456_v2/checkpoint-2200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --max_seq_length 8192 --batch_size 1 --device cuda:0 --output eval_summary.json\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"876205\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-repo-s456-eval-v2.log\", \"submitted_at\": \"2026-05-19T23:20:06.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints_repo_cls_8b_s456_v2/checkpoint-2200\", \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 456, \"eval_data\": \"swebench_test\", \"data_count\": 9784, \"data_path\": \"data/swebench_full/swebench_test.jsonl\"}, \"metrics\": {\"accuracy\": 84.4, \"f1_macro\": 76.19, \"f1_fail\": 62.21, \"f1_pass\": 90.17, \"precision_fail\": 90.23, \"recall_fail\": 47.47, \"checkpoint\": \"checkpoint-2200\", \"seq_length\": 8192}, \"conclusion\": \"success\"}, \"qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:11:09.889Z\", \"updated_at\": \"2026-05-19T19:52:52.545Z\", \"spec\": {\"command\": \"cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --max_seq_length 4096 --max_new_tokens 1024 --batch_size 8 --output_dir /root/autodl-tmp/eval_results/qwen3_8b_cwm_repo_s42_ckpt400_seq4096/\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"778328\", \"log_path\": \"~/runs/exec-sim-repair-verifier/qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval.log\", \"submitted_at\": \"2026-05-19T00:11:09.199Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B\", \"data_path\": \"SWE-bench Verified test set\", \"data_count\": 9784, \"seed\": 42, \"checkpoint_source\": \"checkpoints_repo_cwm_8b_conda/checkpoint-400\", \"eval_data\": \"SWE-bench Verified test (n=9784)\", \"wall_clock_seconds\": 70550.6, \"gpu_hours\": 19.6}, \"hypothesis\": \"Qwen3-8B CWM repo-level eval @seq4096 for D146 cross-model comparison fix. Previous Qwen3 CWM evals used seq8192 while DeepSeek CWM used seq4096, creating confound. This eval provides matched seq_length comparison point.\", \"parent\": \"cwm8b-ckpt400-test-eval\", \"reproduce\": {\"finished_at\": \"2026-05-19T19:45:39.797Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T19:45:45.091313+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 64.36, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -8.6, \"f1_macro\": 54.42, \"f1_pass\": 75.71, \"f1_fail\": 33.14, \"precision_pass\": 75.3, \"precision_fail\": 33.63, \"recall_pass\": 76.11, \"recall_fail\": 32.65, \"unparseable\": 6236, \"unparseable_rate\": 63.74, \"truncated\": 0, \"truncated_rate\": 0, \"total\": 9784, \"class_pass\": 7138, \"class_fail\": 2646, \"confusion\": {\"TP\": 5433, \"FP\": 1782, \"TN\": 864, \"FN\": 1705}, \"gen_length_mean\": 149.8, \"gen_length_median\": 125, \"gen_length_p95\": 313, \"seq_length\": 4096, \"max_new_tokens\": 1024, \"checkpoint\": \"checkpoint-400\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-400\", \"log_path\": \"~/runs/exec-sim-repair-verifier/qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval.log\", \"completed_at\": \"2026-05-19T19:46:59.823Z\"}, \"cls8b-s42-ckpt-ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T12:03:31.233Z\", \"updated_at\": \"2026-05-19T13:18:58.272Z\", \"hypothesis\": \"Checkpoint selection bias quantification (N2): comparing epoch 1 (ckpt-2200) / val-selected (ckpt-3600, 84.48%) / final epoch (ckpt-6633) for Qwen3-8B CLS repo-level s42\", \"spec\": {\"command\": \"bash -c \\\"bash /home/sonny/exec-sim-repair-verifier/run_cls_ablation_chain.sh > /root/autodl-tmp/logs/cls8b_ablation_chain.log 2>&1\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"830917\", \"log_path\": \"/root/autodl-tmp/logs/cls8b_ablation_chain.log\", \"submitted_at\": \"2026-05-19T12:18:34.779Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (eval-only ablation, checkpoints at /home/sonny/exec-sim-repair-verifier/checkpoints/cls-repo-8b-s42-*/)\", \"wall_clock_seconds\": 3568.1, \"gpu_hours\": 0.99}, \"metrics\": {\"ckpt-2200\": {\"accuracy\": 85.34, \"f1_macro\": 79.04, \"f1_fail\": 67.56, \"f1_pass\": 90.53}, \"ckpt-3600\": {\"accuracy\": 84.48, \"f1_macro\": 78.17, \"f1_fail\": 66.43, \"f1_pass\": 89.91}, \"ckpt-6633\": {\"accuracy\": 85.29, \"f1_macro\": 78.44, \"f1_fail\": 66.28, \"f1_pass\": 90.6}}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:09:55.556Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:18:02.927Z\", \"notes\": \"N2 回应: Checkpoint selection bias < 1pp. ckpt-2200 (epoch 1) = 85.34%, ckpt-3600 (val-selected, 当前使用) = 84.48%, ckpt-6633 (final) = 85.29%. Val-selected 比 epoch 1 差 0.86pp, 但不改变 CLS 领先 CWM 19-26pp 的结论。\"}, \"qwen3-8b-traj-repo-s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:57:13.413Z\", \"updated_at\": \"2026-05-19T11:57:43.364Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python train_traj_verifier.py --data_dir data/swebench_full/ --model_name Qwen3-8B --output_dir checkpoints_qwen3_8b_traj_repo_s456/ --seed 456 --max_seq_length 4096 --batch_size 1 --grad_accumulation 8 --lr 2e-4 --epochs 3 --lora_rank 16 --lora_alpha 32\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/swebench_full/\", \"data_count\": 48, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_qwen3_8b_traj_repo_s456/checkpoint-98\", \"log_path\": \"/root/autodl-tmp/logs/traj_s456_train.log\"}, \"hypothesis\": \"Qwen3-8B TRAJ repo-level s456: multi-seed replication for N1. s42=72.92%; s123=77.08%; DeepSeek TRAJ s123=77.1%\", \"parent\": \"qwen3-8b-traj-repo-s42-v2\", \"metrics\": {\"variant_accuracy\": 70.83, \"variant_correct\": 34, \"variant_total\": 48, \"f1_macro\": 70.63, \"overall_accuracy\": 70.83, \"precision_unresolved\": 63.33, \"recall_unresolved\": 86.36, \"f1_unresolved\": 73.08, \"precision_resolved\": 83.33, \"recall_resolved\": 57.69, \"f1_resolved\": 68.18, \"train_loss\": 0.5664, \"eval_loss_all_nan\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:57:43.364Z\"}, \"qwen3-8b-traj-repo-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:51:14.265Z\", \"updated_at\": \"2026-05-19T11:51:52.084Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python train_traj_verifier.py --data_dir data/swebench_full/ --model_name Qwen3-8B --output_dir checkpoints_qwen3_8b_traj_repo_s123/ --seed 123 --max_seq_length 4096 --batch_size 1 --grad_accumulation 8 --lr 2e-4 --epochs 3 --lora_rank 16 --lora_alpha 32\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/swebench_full/\", \"data_count\": 48, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_qwen3_8b_traj_repo_s123/checkpoint-98\", \"log_path\": \"/root/autodl-tmp/logs/traj_s123_train.log\"}, \"hypothesis\": \"Qwen3-8B TRAJ repo-level s123: multi-seed replication for N1. s42=72.92%; DeepSeek TRAJ s123=77.1%\", \"parent\": \"qwen3-8b-traj-repo-s42-v2\", \"metrics\": {\"variant_accuracy\": 77.08, \"variant_correct\": 37, \"variant_total\": 48, \"f1_macro\": 76.59, \"overall_accuracy\": 77.08, \"precision_unresolved\": 78.95, \"recall_unresolved\": 68.18, \"f1_unresolved\": 73.17, \"precision_resolved\": 75.86, \"recall_resolved\": 84.62, \"f1_resolved\": 80, \"train_loss\": 0.5706, \"eval_loss_all_nan\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:51:52.084Z\"}, \"exp-downsample-cls-func-v3-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:32:19.527Z\", \"updated_at\": \"2026-05-19T07:10:09.357Z\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && /root/miniconda3/bin/python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_cls_downsample_qwen3_4b/best --model_name /root/autodl-tmp/models/Qwen/Qwen3-4B --output artifacts/eval_cls_downsample_v3/eval_repo_cls.json --pred_output artifacts/eval_cls_downsample_v3/eval_repo_cls_predictions.jsonl --device cuda:0 --split test\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"808206\", \"log_path\": \"~/runs/exec-sim-repair-verifier/exp-downsample-cls-func-v3-eval.log\", \"submitted_at\": \"2026-05-19T06:57:29.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 574.1, \"gpu_hours\": 0.16}, \"hypothesis\": \"Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量\", \"conclusion\": \"success\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-19T07:06:58.661Z\"}, \"completed_at\": \"2026-05-19T07:07:03.399Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T07:07:09.351958+00:00\"}]}, \"metrics\": {\"accuracy\": 80.74, \"f1_macro\": 75.89, \"fail_f1\": 65.1, \"pass_f1\": 86.7, \"unparseable\": 132, \"total\": 9784, \"source\": \"extracted from log (file write failed)\"}}, \"exp-downsample-cls-func-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:05:36.371Z\", \"updated_at\": \"2026-05-19T06:57:21.152Z\", \"spec\": {\"command\": \"cd /home/sonny/exec-sim-repair-verifier && WANDB_MODE=offline HF_HUB_OFFLINE=1 /root/miniconda3/bin/python train_unified.py --model_name_or_path /root/autodl-tmp/models/Qwen/Qwen3-4B --data_dir data/ --task cls --train_file train_downsampled.jsonl --val_file val.jsonl --output_dir /root/autodl-tmp/checkpoints_cls_downsample_qwen3_4b/ --run_name cls-downsample-qwen3-4b-lora --epochs 3 --batch_size 2 --grad_accumulation 16 --lr 2e-4 --lora_rank 16 --lora_alpha 32 --max_seq_length 2048 --seed 42 --wandb_project exec-sim-repair-verifier\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"796724\", \"log_path\": \"~/runs/exec-sim-repair-verifier/exp-downsample-cls-func-v3.log\", \"submitted_at\": \"2026-05-19T04:05:35.621Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_downsampled.jsonl\", \"data_count\": 8051, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 10305.5, \"gpu_hours\": 2.86}, \"hypothesis\": \"CLS function-level 的 accuracy 优势不仅仅来自更多训练数据（CLS 15K vs TRAJ 8K）。将 CLS 训练数据 downsample 至与 TRAJ 相同规模（~8K），CLS 仍应优于 TRAJ，证明 formulation 本身的优势\", \"parent\": \"exp-downsample-cls-func-v2\", \"notes\": \"v2 failed (EXIT_CODE=1) at trainer.train() — wandb tried online mode, no API key configured: `UsageError: No API key configured. Use wandb login to log in.` (line `_find_or_prompt_for_key`). v3 fix: submit_training_job framework auto-injected `WANDB_MODE=offline` + `CUDA_VISIBLE_DEVICES=1` + `HF_HUB_OFFLINE=1`. Confirmed via /proc/796729/environ. v3 running on GPU 1 (cuda:1), tmux session exp-downsample-cls-func-v3, started 2026-05-19 12:05:35, step ~36/756 @ ~3.35s/iter, ETA ~42 min total. Data: train_downsampled.jsonl 8051 rows (8041 after masking filter), val.jsonl 1896 rows.\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.2869, \"eval_loss_epoch1\": 0.1061, \"eval_loss_epoch2\": 0.0907, \"eval_loss_epoch3\": 0.1156, \"best_epoch\": 2, \"training_time_min\": 44.4}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_cls_downsample_qwen3_4b/best\", \"completed_at\": \"2026-05-19T06:57:21.152Z\"}, \"exp-e-qwen3-3shot-baseline\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:20:13.381Z\", \"updated_at\": \"2026-05-19T05:31:22.482Z\", \"hypothesis\": \"Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立\", \"spec\": {\"command\": \"cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_3shot_baseline.py --model_name_or_path /root/autodl-tmp/models/Qwen/Qwen3-8B --data_dir data/swebench_full --split test --max_seq_length 4096 --device cuda:0 --output_dir artifacts/eval_3shot_qwen3_8b\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"799259\", \"model_name\": \"Qwen3-8B\", \"data_path\": \"data/swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"seed\": 42, \"checkpoint_source\": \"base model (no fine-tuning)\", \"eval_data\": \"swebench_test.jsonl (9784 per-test, 48 variants)\"}, \"conclusion\": \"success\", \"metrics\": {\"per_test_accuracy\": 71.61, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -1.35, \"f1_fail\": 61.42, \"f1_pass\": 77.54, \"f1_macro\": 69.48, \"variant_accuracy\": 45.83, \"variant_correct\": 22, \"variant_total\": 48, \"n_instances\": 9784, \"unparseable\": 0, \"truncated\": 0, \"elapsed_min\": 24.6}, \"log_path\": \"~/runs/exec-sim-repair-verifier/exp-e-qwen3-3shot-baseline.log\"}, \"repo-level-3shot-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:08:27.137Z\", \"updated_at\": \"2026-05-19T04:36:55.833Z\", \"hypothesis\": \"3-shot few-shot 在 repo-level 能否作为 baseline，预期因 context 长度限制表现差于 fine-tuned models\", \"conclusion\": \"success\", \"failure_reason\": \"CORRECTED: initial run had context overflow, final run @seq4096 succeeded. Previous failure_reason was stale metadata.\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_3shot_baseline.py --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full --device cuda:0 --max_seq_length 4096 --output_dir artifacts/eval_3shot_deepseek\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"788567\", \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-3shot-baseline.log\", \"submitted_at\": \"2026-05-19T02:53:00.493Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_source\": \"base model (no fine-tuning)\", \"eval_data\": \"swebench_test.jsonl (9784 per-test, 48 variants)\", \"wall_clock_seconds\": 3414.8, \"gpu_hours\": 0.95}, \"completed_at\": \"2026-05-19T03:49:55.284Z\", \"metrics\": {\"per_test_accuracy\": 46.28, \"variant_accuracy\": 45.83, \"variant_correct\": 22, \"variant_total\": 48, \"majority_baseline\": 73, \"truncated\": 0, \"unparseable\": 0, \"total\": 9784, \"runtime_min\": 33.8}}, \"exp-d-constrained-decoding\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:20:10.868Z\", \"updated_at\": \"2026-05-19T03:52:22.449Z\", \"hypothesis\": \"CWM 的低 accuracy 主要由 unparseable outputs 导致（51-72%），constrained decoding 或 forced-parse 可将 parseable rate 提升至接近 100%，但 parseable-only accuracy 仍低（~38-42%），证明 CWM 问题不仅是格式问题\", \"metrics\": {\"forced_parse\": {\"qwen3_8b\": {\"n\": 9784, \"original_unparseable_rate\": 73.8, \"rescue_rate\": 90.6, \"original_parseable_acc\": 38.5, \"forced_parseable_acc\": 49.4, \"delta_pp\": 10.8}, \"qwen3_4b\": {\"n\": 500, \"original_unparseable_rate\": 75.2, \"rescue_rate\": 77.9, \"original_parseable_acc\": 42.7, \"forced_parseable_acc\": 55.9, \"delta_pp\": 13.2}, \"deepseek\": {\"n\": 9784, \"original_unparseable_rate\": 51, \"rescue_rate\": 20.3, \"original_parseable_acc\": 38.7, \"forced_parseable_acc\": 51.8, \"delta_pp\": 13.1}}, \"best_strategy\": \"test_ok_fail (67-71% acc)\", \"constrained_decoding\": \"code ready, blocker: swebench_full test data not on server\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python cwm_forced_parse.py (CPU analysis)\", \"server\": \"local\", \"data_path\": \"CWM eval predictions\", \"data_count\": 9784, \"model_name\": \"N/A (post-hoc parsing)\", \"seed\": \"N/A\"}, \"checkpoint_path\": \"N/A (CPU analysis)\", \"log_path\": \"worker_code_exp-d-constrained-decoding-prep_20260519T030047\", \"completed_at\": \"2026-05-19T03:52:22.449Z\"}, \"exp-b-complexity-bin\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:20:07.634Z\", \"updated_at\": \"2026-05-19T03:46:26.036Z\", \"hypothesis\": \"不同 formulation 的 accuracy 优劣与 variant 复杂度（test count）相关：TRAJ 在低 test-count variants 更优，CLS 在高 test-count variants 更优\", \"spec\": {\"command\": \"python complexity_bin_analysis.py\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"eval_results/ (CLS + CWM predictions)\", \"data_count\": 9784, \"model_name\": \"N/A (post-processing)\", \"seed\": 42, \"checkpoint_path\": \"artifacts/complexity_bin_analysis.json\", \"log_path\": \"artifacts/complexity_bin_analysis.json\"}, \"conclusion\": \"success\", \"metrics\": {\"bins\": {\"23-70\": {\"n_variants\": 12, \"n_tests\": 538, \"cls_qwen3_8b_s123\": 83.3, \"cls_ds_v5\": 91.7, \"cwm_qwen3_8b\": 66.7}, \"71-150\": {\"n_variants\": 14, \"n_tests\": 1282, \"cls_qwen3_8b_s123\": 64.3, \"cls_ds_v5\": 71.4, \"cwm_qwen3_8b\": 42.9}, \"151-250\": {\"n_variants\": 15, \"n_tests\": 2999, \"cls_qwen3_8b_s123\": 93.3, \"cls_ds_v5\": 80, \"cwm_qwen3_8b\": 53.3}, \"251+\": {\"n_variants\": 7, \"n_tests\": 4965, \"cls_ds_v5\": 85.7, \"cls_qwen3_8b_s123\": 85.7, \"cwm_qwen3_8b\": 42.9}}, \"overall_cls_qwen3_8b\": 81.2, \"overall_cls_ds_v5\": 81.2, \"overall_cwm_qwen3_8b\": 52.1, \"cls_cwm_gap_simple\": 16.7, \"cls_cwm_gap_complex\": 42.9, \"traj_per_bin\": \"unavailable — per-variant predictions not saved\"}, \"completed_at\": \"2026-05-19T03:46:26.036Z\"}, \"exp-a-routing\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:20:05.183Z\", \"updated_at\": \"2026-05-19T03:44:43.981Z\", \"hypothesis\": \"Complexity-aware routing（按 test count/confidence/learned features 选 formulation）在 repo-level 可以超越任何单一 formulation 的 accuracy，证明 formulation 具有互补性\", \"metrics\": {\"oracle_routing_7cls\": 100, \"oracle_best_pair\": 95.83, \"test_count_heuristic\": 85.42, \"agreement_confidence\": 83.33, \"majority_vote\": \"75-79%\", \"best_single_cls\": 81.25, \"test_count_heuristic_delta\": \"+4.17pp\", \"oracle_delta\": \"+18.75pp\", \"traj_per_variant\": \"unavailable\", \"cwm_repo_level\": \"45-52%\", \"n_variants\": 48}, \"conclusion\": \"success\", \"spec\": {\"command\": \"CPU analysis — worker_analysis_exp-a-routing_20260519T030014\", \"server\": \"local\", \"data_path\": \"artifacts/per-variant predictions\", \"data_count\": 48, \"model_name\": \"N/A (analysis)\", \"seed\": \"N/A\"}, \"checkpoint_path\": \"N/A (CPU analysis)\", \"log_path\": \"worker_analysis_exp-a-routing_20260519T030014\", \"completed_at\": \"2026-05-19T03:44:43.981Z\"}, \"qwen3-8b-traj-repo-s42-ckpt98-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:28:45.370Z\", \"updated_at\": \"2026-05-19T00:08:03.186Z\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_traj_verifier.py --data_dir data/swebench_full/ --checkpoint_dir /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/checkpoint-98/ --model_name /root/autodl-tmp/models/Qwen/Qwen3-8B --max_seq_length 4096 --output /root/autodl-tmp/eval_results/qwen3_8b_traj_repo_s42_ckpt98_eval.json 2>&1 | tee ~/runs/exec-sim-repair-verifier/qwen3-8b-traj-repo-s42-ckpt98-eval.log\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"775278\", \"log_path\": \"~/runs/exec-sim-repair-verifier/qwen3-8b-traj-repo-s42-ckpt98-eval.log\", \"submitted_at\": \"2026-05-18T23:28:44.784Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Qwen3-8B TRAJ repo-level eval checkpoint-98 (epoch 2). Qwen3-4B TRAJ epoch 2 > epoch 3, testing if same pattern holds for 8B. Table 4 canonical number.\", \"metrics\": {\"variant_accuracy\": 72.92, \"variant_correct\": 35, \"variant_total\": 48, \"f1_macro\": 72.9, \"fail_recall\": 77.3, \"pass_recall\": 69.2, \"unparseable\": 0, \"note\": \"epoch 2 checkpoint, better class balance than epoch 3\"}, \"conclusion\": \"success\", \"parent\": \"qwen3-8b-traj-repo-s42-v2\"}, \"qwen3-8b-traj-repo-s42-best-eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:02:09.930Z\", \"updated_at\": \"2026-05-19T00:07:52.073Z\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_traj_verifier.py --data_dir data/swebench_full/ --checkpoint_dir /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/best/ --model_name /root/autodl-tmp/models/Qwen/Qwen3-8B --max_seq_length 4096 --output /root/autodl-tmp/eval_results/qwen3_8b_traj_repo_s42_best_eval.json 2>&1 | tee ~/runs/exec-sim-repair-verifier/qwen3-8b-traj-repo-s42-best-eval.log\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"773052\", \"log_path\": \"~/runs/exec-sim-repair-verifier/qwen3-8b-traj-repo-s42-best-eval.log\", \"submitted_at\": \"2026-05-18T23:02:09.373Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Qwen3-8B TRAJ repo-level eval on test set (best/ checkpoint = epoch 3, eval_loss=NaN forced). Table 4 canonical number. Compare with Qwen3-4B TRAJ (72.92%) and DeepSeek TRAJ (81.25%). Expected ~78-85% variant-level.\", \"parent\": \"qwen3-8b-traj-repo-s42-v2\", \"metrics\": {\"variant_accuracy\": 70.83, \"variant_correct\": 34, \"variant_total\": 48, \"f1_macro\": 70, \"fail_recall\": 95.5, \"pass_recall\": 50, \"unparseable\": 0, \"note\": \"epoch 3 checkpoint, biased toward predicting unresolved\"}, \"conclusion\": \"success\"}, \"qwen3-8b-traj-repo-s42-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:49:06.304Z\", \"updated_at\": \"2026-05-18T23:02:25.726Z\", \"hypothesis\": \"Qwen3-8B TRAJ repo-level training retry with seq4096 (v1 OOM at seq8192). Table 4 completion. DeepSeek TRAJ s42=81.25%; Qwen3-4B TRAJ=72.92%. Qwen3-8B expected ~78-85% variant-level. Lower seq_length may truncate some long repo-level diffs but DeepSeek non-8k variant showed comparable results.\", \"parent\": \"qwen3-8b-traj-repo-s42\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T22:49:43.183Z\", \"command\": \"bash -c \\\"mkdir -p /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo && cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 /root/miniconda3/bin/python train_traj_verifier.py --data_dir data/swebench_full/ --model_name /root/autodl-tmp/models/Qwen/Qwen3-8B --output_dir /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/ --run_name qwen3-8b-traj-repo --seed 42 --max_seq_length 4096 --batch_size 1 --grad_accumulation 8 --lr 2e-4 --epochs 3 --lora_rank 16 --lora_alpha 32 --no_wandb\\\"\", \"finished_at\": \"2026-05-18T22:56:16.289Z\", \"training_hours\": 0.11}, \"spec\": {\"command\": \"bash -c \\\"mkdir -p /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo && cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 /root/miniconda3/bin/python train_traj_verifier.py --data_dir data/swebench_full/ --model_name /root/autodl-tmp/models/Qwen/Qwen3-8B --output_dir /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/ --run_name qwen3-8b-traj-repo --seed 42 --max_seq_length 4096 --batch_size 1 --grad_accumulation 8 --lr 2e-4 --epochs 3 --lora_rank 16 --lora_alpha 32 --no_wandb\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"771183\", \"log_path\": \"~/runs/exec-sim-repair-verifier/qwen3-8b-traj-repo-s42-v2.log\", \"submitted_at\": \"2026-05-18T22:49:46.114Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/\", \"data_path\": \"data/swebench_full/\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"pid\": \"771183\", \"log_path\": \"~/runs/exec-sim-repair-verifier/qwen3-8b-traj-repo-s42-v2.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T22:56:21.854472+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:00:20.346Z\", \"metrics\": {\"eval_loss\": \"NaN_all_epochs\", \"total_steps\": 147, \"epochs\": 3, \"seq_length\": 4096, \"best_checkpoint\": \"epoch_3_default_due_to_nan_eval_loss\", \"gradient_checkpointing\": true}}, \"deepseek-cls-repo-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:26:56.947Z\", \"updated_at\": \"2026-05-18T22:53:36.387Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 python3 train_unified.py --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/ --task cls --output_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo_s123/ --run_name deepseek-cls-repo-s123 --epochs 3 --seed 123 --no_wandb\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"542509\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-cls-repo-s123.log\", \"submitted_at\": \"2026-05-16T17:27:50.211Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/swebench_full/swebench_train.jsonl\", \"data_count\": 70748, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cls_repo_s123/best/\", \"wall_clock_seconds\": 192346.2, \"gpu_hours\": 53.43}, \"hypothesis\": \"DeepSeek CLS repo-level seed 123 replication for multi-seed evidence (same config as s42)\", \"reproduce\": {\"finished_at\": \"2026-05-17T15:08:43.365Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T15:08:48.655545+00:00\"}]}, \"metrics\": {\"per_test_accuracy_seq8192\": 74.93, \"per_test_accuracy_seq2048\": 82.62, \"majority_baseline\": 72.96, \"gap_vs_majority_seq8192\": 1.97, \"f1_macro_seq8192\": 53.94, \"f1_fail_seq8192\": 22.84, \"f1_pass_seq8192\": 85.03, \"precision_fail_seq8192\": 68.11, \"recall_fail_seq8192\": 13.72, \"recall_pass_seq8192\": 97.62, \"variant_accuracy_seq8192\": 28, \"variant_correct_seq8192\": 7, \"variant_total_seq8192\": 25, \"variant_accuracy_seq2048\": 36, \"variant_correct_seq2048\": 9, \"variant_total_seq2048\": 25, \"unparseable_seq8192\": 0, \"unparseable_seq2048\": 2796, \"train_loss_avg\": 0.0393, \"eval_loss\": \"NaN_all_epochs\", \"total_steps\": 6633, \"epochs\": 3, \"train_time\": \"21h30m\", \"best_checkpoint\": \"epoch_3_default_due_to_nan_eval_loss\", \"note\": \"seq2048 metrics inflated by 28.6% unparseable defaulting to pass; seq8192 is reliable measure\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:53:36.387Z\"}, \"deepseek-cls-repo-v5-ckpt6315-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:58:30.134Z\", \"updated_at\": \"2026-05-18T22:49:27.392Z\", \"spec\": {\"command\": \"bash -c \\\"mkdir -p /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt6315_test_seq8192 && cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/checkpoint-6315 --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full --split test --max_seq_length 8192 --batch_size 1 --device cuda:0 --output /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt6315_test_seq8192/eval_summary.json --pred_output /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt6315_test_seq8192/predictions.jsonl\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"763689\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-cls-repo-v5-ckpt6315-eval.log\", \"submitted_at\": \"2026-05-18T21:21:48.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1892.9, \"gpu_hours\": 0.53}, \"hypothesis\": \"CLS v5 epoch 3 final checkpoint (ckpt-6315) eval at seq8192: D140 checkpoint selection confound 对比数据。eval_loss epoch 3=0.1587 vs epoch 1=0.0886 (+79%)，预期 repo-level accuracy 低于 ckpt-2105。\", \"parent\": \"deepseek-cls-repo-v5-ckpt2105-eval\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T21:21:44.467Z\", \"command\": \"bash -c \\\"mkdir -p /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt6315_test_seq8192 && cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/checkpoint-6315 --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full --split test --max_seq_length 8192 --batch_size 1 --device cuda:0 --output /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt6315_test_seq8192/eval_summary.json --pred_output /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt6315_test_seq8192/predictions.jsonl\\\"\", \"finished_at\": \"2026-05-18T21:52:04.878Z\", \"training_hours\": 0.51}, \"pid\": \"763689\", \"log_path\": \"/root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt6315_test_seq8192/eval_summary.json\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:52:10.294218+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 82.51, \"fail_recall\": 38.47, \"pass_recall\": 98.84, \"unparseable\": 0, \"n_instances\": 9784, \"confusion\": {\"TN\": 1018, \"FP\": 1628, \"FN\": 83, \"TP\": 7055}, \"variant_accuracy\": 79.17, \"variant_correct\": 38, \"variant_total\": 48, \"variant_fail_recall\": 59.09}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/checkpoint-6315\", \"completed_at\": \"2026-05-18T21:53:21.231Z\"}, \"qwen3-4b-traj-repo-s42-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:28:24.376Z\", \"updated_at\": \"2026-05-18T22:34:32.172Z\", \"hypothesis\": \"Qwen3-4B TRAJ repo-level eval on test set (best checkpoint, epoch 2). Table 4 canonical number. DeepSeek TRAJ s42=81.25%; Qwen3 CLS repo=83.63%. 预期 variant-level ~75-85%.\", \"parent\": \"qwen3-4b-traj-repo-s42\", \"spec\": {\"command\": \"python eval_traj_verifier.py --model_path /root/autodl-tmp/checkpoints_qwen3_4b_traj_repo/best --test_file swebench_test.jsonl --output /root/autodl-tmp/eval_results/qwen3_4b_traj_repo_s42_best/eval_test_s42.json --seed 42\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"swebench_test.jsonl\", \"data_count\": 48, \"model_name\": \"Qwen3-4B-TRAJ-repo-s42-best\", \"seed\": 42, \"checkpoint_source\": \"qwen3-4b-traj-repo-s42\", \"eval_data\": \"swebench_test.jsonl (48 variants)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_qwen3_4b_traj_repo/best\", \"log_path\": \"/root/autodl-tmp/eval_results/qwen3_4b_traj_repo_s42_best/eval_test_s42.json\"}, \"conclusion\": \"success\", \"metrics\": {\"variant_accuracy\": 72.92, \"variant_correct\": 35, \"variant_total\": 48, \"f1_macro\": 72.62, \"resolved_precision\": 74.1, \"resolved_recall\": 76.9, \"resolved_f1\": 75.5, \"unresolved_precision\": 71.4, \"unresolved_recall\": 68.2, \"unresolved_f1\": 69.8, \"vs_majority_baseline_pp\": 18.8}, \"completed_at\": \"2026-05-18T22:34:32.172Z\"}, \"qwen3-4b-traj-repo-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:10:00.484Z\", \"updated_at\": \"2026-05-18T22:28:42.684Z\", \"hypothesis\": \"Qwen3-4B TRAJ repo-level training for Table 4 completion. DeepSeek TRAJ achieves 75.35% ± 5.00 (6 seeds); Qwen3-4B TRAJ expected to be comparable or higher given Qwen3 在 CLS repo-level 的强表现 (83.63%).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python train_traj_verifier.py --data_dir data/swebench_full/ --model_name /root/autodl-tmp/models/Qwen/Qwen3-4B --output_dir /root/autodl-tmp/checkpoints_qwen3_4b_traj_repo/ --run_name qwen3-4b-traj-repo --seed 42 --max_seq_length 8192 --batch_size 1 --grad_accumulation 8 --lr 2e-4 --epochs 3 --lora_rank 16 --lora_alpha 32 --no_wandb\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/swebench_full/traj_train.jsonl\", \"data_count\": 386, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"gpu_ids\": [\"cuda:0\"], \"pid\": 767245, \"max_seq_length\": 8192, \"batch_size\": 1, \"grad_accumulation\": 8, \"lr\": \"2e-4\", \"epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"total_steps\": 147, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_qwen3_4b_traj_repo/\", \"log_path\": \"/root/autodl-tmp/checkpoints_qwen3_4b_traj_repo/train.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_loss_epoch1\": 0.2123, \"eval_loss_epoch2\": 0.1503, \"eval_loss_epoch3\": 0.2249, \"best_epoch\": 2, \"total_steps\": 147}, \"completed_at\": \"2026-05-18T22:28:42.684Z\"}, \"deepseek-cls-repo-v5-ckpt2105-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:57:13.898Z\", \"updated_at\": \"2026-05-18T21:34:56.469Z\", \"spec\": {\"command\": \"bash -c \\\"mkdir -p /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192 && cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/checkpoint-2105 --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full --split test --max_seq_length 8192 --batch_size 1 --device cuda:0 --output /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192/eval_summary.json --pred_output /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192/predictions.jsonl\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"761181\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-cls-repo-v5-ckpt2105-eval.log\", \"submitted_at\": \"2026-05-18T20:44:28.404Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3028.1, \"gpu_hours\": 0.84}, \"hypothesis\": \"CLS v5 epoch 1 (ckpt-2105, eval_loss=0.0886 最低) 在 repo-level test set 上应优于 epoch 3，验证 early stopping 选择并为 Table 4 提供 s42 canonical 数字\", \"parent\": \"deepseek-cls-repo-v5\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T20:44:26.314Z\", \"command\": \"bash -c \\\"mkdir -p /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192 && cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 /root/miniconda3/bin/python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/checkpoint-2105 --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full --split test --max_seq_length 8192 --batch_size 1 --device cuda:0 --output /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192/eval_summary.json --pred_output /root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192/predictions.jsonl\\\"\", \"finished_at\": \"2026-05-18T21:14:03.068Z\", \"training_hours\": 0.49}, \"pid\": \"761181\", \"log_path\": \"/root/autodl-tmp/eval_results/deepseek_cls_repo_v5_ckpt2105_test_seq8192/eval_summary.json\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:14:08.424039+00:00\"}]}, \"metrics\": {\"accuracy\": 82.61, \"variant_accuracy\": 81.25, \"variant_correct\": 39, \"variant_total\": 48, \"fail_recall\": 51.02, \"pass_recall\": 94.33, \"f1_macro\": 75.07, \"fail_f1\": 61.35, \"pass_f1\": 88.78, \"fail_precision\": 76.92, \"pass_precision\": 83.86, \"unparseable\": 0, \"n_instances\": 9784, \"confusion\": {\"TP\": 6733, \"FP\": 1296, \"TN\": 1350, \"FN\": 405}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/checkpoint-2105\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T21:34:56.469Z\"}, \"deepseek-cls-repo-v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:47:56.629Z\", \"updated_at\": \"2026-05-18T20:42:57.953Z\", \"hypothesis\": \"DeepSeek CLS repo-level s42 完整 3 epoch 训练，预期与 s123 (~74%) 相近，提供 R1-N1 要求的多 seed 证据\", \"reproduce\": {\"finished_at\": \"2026-05-18T20:35:45.428Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:35:47.523864+00:00\"}]}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python train_unified.py --formulation cls --data_dir data/swebench_full --model_name deepseek-ai/deepseek-coder-6.7b-instruct --output_dir /root/autodl-tmp/checkpoints_deepseek_cls_repo_v5 --seed 42 --max_seq_length 8192 --epochs 3\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/swebench_full/\", \"data_count\": 2211, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"gpu\": [\"cuda:0\"], \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cls_repo_v5\", \"log_path\": \"~/runs/deepseek-cls-repo-v5.log\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss_final\": 0.0399, \"eval_loss_epoch1\": 0.0886, \"eval_loss_epoch2\": 0.1587, \"eval_loss_epoch3\": 0.1975, \"total_steps\": 6315, \"train_time_seconds\": 63312, \"best_checkpoint\": \"checkpoint-2105 (epoch 1)\", \"lora_params\": \"16.8M\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/\", \"log_path\": \"/root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/train.log\", \"completed_at\": \"2026-05-18T20:42:57.953Z\"}, \"deepseek-0shot-func-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:30:55.534Z\", \"updated_at\": \"2026-05-18T00:10:08.086Z\", \"hypothesis\": \"DeepSeek 0-shot instruction 在 func-level 的基准表现，完成 2×2 model×level 0-shot 矩阵\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6302, \"pass_f1\": 0.7196, \"fail_f1\": 0.4569, \"unparseable_rate\": 0.0106, \"unparseable_count\": 20, \"total_samples\": 1890, \"runtime_seconds\": 113, \"confusion\": {\"TP\": 897, \"FP\": 618, \"TN\": 294, \"FN\": 81}}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/0shot_func_level_deepseek.log\", \"completed_at\": \"2026-05-18T00:10:08.086Z\"}, \"qwen3-0shot-func-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:30:53.841Z\", \"updated_at\": \"2026-05-18T00:10:06.393Z\", \"hypothesis\": \"Qwen3-8B 0-shot instruction 在 func-level 的基准表现，预期优于 repo-level 0-shot (49.9%) 因为 func-level 上下文更短更清晰\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6873, \"pass_f1\": 0.655, \"fail_f1\": 0.7141, \"unparseable_rate\": 0.0032, \"unparseable_count\": 6, \"total_samples\": 1890, \"runtime_seconds\": 96, \"confusion\": {\"TP\": 561, \"FP\": 174, \"TN\": 738, \"FN\": 417}}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/0shot_func_level_qwen.log\", \"completed_at\": \"2026-05-18T00:10:06.394Z\"}, \"deepseek-0shot-repo-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:30:52.005Z\", \"updated_at\": \"2026-05-18T00:10:04.699Z\", \"hypothesis\": \"DeepSeek 0-shot instruction 在 repo-level 的基准表现，跨模型验证 0-shot 在 repo-level 普遍接近随机\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.4854, \"pass_f1\": 0.647, \"fail_f1\": 0.0509, \"unparseable_rate\": 0.087, \"unparseable_count\": 851, \"total_samples\": 9784, \"runtime_seconds\": 1545, \"confusion\": {\"TP\": 4614, \"FP\": 2511, \"TN\": 135, \"FN\": 2524}}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/0shot_repo_level_deepseek.log\", \"completed_at\": \"2026-05-18T00:10:04.699Z\"}, \"repo-level-0shot-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:08:25.505Z\", \"updated_at\": \"2026-05-17T23:29:33.741Z\", \"hypothesis\": \"0-shot instruction 在 repo-level 的基准表现，预期远低于 fine-tuned CLS/CWM\", \"spec\": {\"command\": \"python3 run_0shot_repo_level.py\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3929211\", \"data_path\": \"data/swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"log_path\": \"/home/sonny/exec-sim-repair-verifier/0shot_repo_level.log\", \"tmux_session\": \"0shot-repo-baseline\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.499, \"pass_f1\": 0.4895, \"fail_f1\": 0.5081, \"unparseable_rate\": 0, \"unparseable_count\": 0, \"total_samples\": 9784, \"runtime_seconds\": 1018.2, \"confusion\": {\"TP\": 2350, \"FP\": 114, \"TN\": 2532, \"FN\": 4788}}, \"checkpoint_path\": \"N/A (inference-only baseline, no checkpoint)\", \"completed_at\": \"2026-05-17T23:29:33.741Z\"}, \"deepseek-cwm-repo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T08:05:07.323Z\", \"updated_at\": \"2026-05-17T15:41:06.948Z\", \"spec\": {\"command\": \"python3 train_unified.py --task cwm --model_name deepseek-ai/deepseek-coder-6.7b-instruct --seed 42\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/swebench_full/swebench_train.jsonl\", \"data_count\": 70748, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"gpu\": [\"cuda:1\"], \"pid\": \"479953\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cwm_repo/best/\", \"log_path\": \"/root/autodl-tmp/checkpoints_deepseek_cwm_repo/trainer_state.json\"}, \"hypothesis\": \"DeepSeek CWM repo-level 训练验证 CWM 在第二模型家族上的 repo-level 表现，预期 CWM 因生成式格式在长上下文 repo 代码上产生高 unparseable rate（类似 Qwen CWM repo 53-74%）\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.021, \"eval_loss\": \"NaN\", \"total_steps\": 13266, \"epochs\": 3, \"wall_clock_seconds\": 112680, \"gpu_hours\": 31.3, \"note\": \"eval_loss=NaN is known DeepSeek issue, does not affect training quality\"}, \"completed_at\": \"2026-05-17T15:41:06.948Z\"}, \"qwen3-8b-traj-func-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:19:44.990Z\", \"updated_at\": \"2026-05-17T15:17:35.756Z\", \"hypothesis\": \"Qwen3-8B TRAJ func-level seed 123 复制实验，验证 s42 结果的稳定性。预期与 s42 差距 &lt;1.5pp，与 4B TRAJ (86.30±0.97%) 的 scaling pattern 一致\", \"parent\": \"qwen3-8b-traj-func-s42\", \"spec\": {\"command\": \"python3 train_traj_verifier.py --model_name Qwen/Qwen3-8B --seed 123 --batch_size 2 --grad_accumulation 16 --epochs 3 --lr 2e-4 --lora_rank 16 --lora_alpha 32 --max_seq_length 2048\", \"server\": \"home-1x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/traj_train.jsonl\", \"data_count\": 8052, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"training-from-scratch\", \"eval_data\": \"data/traj_test.jsonl\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj_8b_seed123/best\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj_8b_seed123/trainer_state.json\"}, \"conclusion\": \"success\", \"metrics\": {\"test_accuracy\": 87.79, \"best_eval_loss\": 0.0782, \"pass_f1\": 86.74, \"fail_f1\": 88.69, \"unparseable\": 0, \"per_test_consistency\": 76.07, \"total_steps\": 756, \"test_set_size\": 1032, \"eval_script\": \"eval_traj_verifier_8b.py\"}, \"completed_at\": \"2026-05-17T15:17:35.756Z\"}, \"qwen3-8b-traj-func-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:19:43.240Z\", \"updated_at\": \"2026-05-17T14:29:53.572Z\", \"hypothesis\": \"Qwen3-8B TRAJ func-level 将展示 TRAJ 在更大模型上的 scaling 行为，预期与 4B TRAJ (86.30%) 相比有小幅提升（类似 CLS/CWM 的 4B→8B +1-2pp pattern），填补 Table 2 scaling 分析的 TRAJ 8B 缺口\", \"spec\": {\"command\": \"python3 train_traj_verifier.py --model_name Qwen/Qwen3-8B --seed 42 --batch_size 2 --grad_accumulation 16 --epochs 3 --lr 2e-4 --lora_rank 16 --lora_alpha 32 --max_seq_length 2048\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3819402\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj_8b_seed42/trainer_state.json\", \"submitted_at\": \"2026-05-17T13:20:05.999Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/traj_train.jsonl\", \"data_count\": 8052, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj_8b_seed42/best\", \"wall_clock_seconds\": 3443.2, \"gpu_hours\": 0.96}, \"reproduce\": {\"finished_at\": \"2026-05-17T14:10:45.579Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:10:47.921325+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"test_accuracy\": 87.6, \"eval_loss\": 0.0975, \"train_loss\": 0.0312, \"unparseable\": 0, \"pass_f1\": 85.96, \"fail_f1\": 88.89, \"per_test_consistency\": 78.78, \"total_steps\": 756, \"test_set_size\": 1032, \"eval_script\": \"eval_traj_verifier_8b.py\", \"note\": \"87.98% from eval_traj_verifier.py (model.cuda) also valid; 4/1032 samples differ due to bf16 placement\"}, \"completed_at\": \"2026-05-17T14:17:29.217Z\"}, \"deepseek-cls-func-s123\": {\"status\": \"DONE\", \"parent\": \"deepseek-cls-func\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:11:40.451Z\", \"updated_at\": \"2026-05-17T02:55:51.817Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 train_unified.py --task cls --granularity func --seed 123 --model deepseek-coder-6.7b-instruct\", \"server\": \"westd-48478\", \"data_path\": \"data/swebench_full/\", \"data_count\": 15293, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cls_func_seed123/best/\", \"log_path\": \"/root/autodl-tmp/checkpoints_deepseek_cls_func_seed123/checkpoint-2868/trainer_state.json\"}, \"completed_at\": \"2026-05-16T11:12:17.916Z\", \"metrics\": {\"best_eval_loss\": 0.06753, \"train_time_seconds\": 5391, \"test_accuracy\": 86.77, \"test_f1_macro\": 86.77, \"test_precision_fail\": 84.99, \"test_precision_pass\": 88.56, \"test_recall_fail\": 88.16, \"test_recall_pass\": 85.48, \"test_unparseable_rate\": 0, \"test_n\": 1890}, \"hypothesis\": \"验证 DeepSeek CLS func-level 结论在 seed=123 下的稳定性，确认 CLS accuracy 不是单 seed 偶然\"}, \"deepseek-cwm-func-s123\": {\"status\": \"DONE\", \"parent\": \"deepseek-cwm-func\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:31:21.577Z\", \"updated_at\": \"2026-05-17T02:55:50.883Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 python3 train_unified.py --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/ --task cwm --output_dir /root/autodl-tmp/checkpoints_deepseek_cwm_func_seed123/ --run_name deepseek-cwm-func-seed123 --seed 123 --epochs 3 --no_wandb\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"471780\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-cwm-func-s123.log\", \"submitted_at\": \"2026-05-16T06:32:05.964Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cwm_func_seed123/best/\", \"wall_clock_seconds\": 5599.6, \"gpu_hours\": 1.56}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:00:28.244Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:00:33.559062+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_eval_loss\": 0.0408, \"train_time_seconds\": 5244, \"test_accuracy\": 87.88, \"test_f1_macro\": 87.88, \"test_precision_fail\": 83.78, \"test_precision_pass\": 92.61, \"test_recall_fail\": 92.87, \"test_recall_pass\": 83.23, \"test_unparseable_rate\": 0, \"test_n\": 1890}, \"completed_at\": \"2026-05-16T08:05:25.551Z\", \"hypothesis\": \"验证 DeepSeek CWM func-level 结论在 seed=123 下的稳定性，确认 CWM≈CLS 不是单 seed 偶然\"}, \"deepseek-cls-func\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:27:32.723Z\", \"updated_at\": \"2026-05-17T02:55:48.576Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 python3 train_unified.py --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/ --task cls --train_file train.jsonl --val_file val.jsonl --output_dir /root/autodl-tmp/checkpoints_deepseek_cls_func/ --run_name deepseek-cls-func-level --epochs 3 --no_wandb\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"470484\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-cls-func.log\", \"submitted_at\": \"2026-05-16T06:27:32.326Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cls_func/best/\", \"wall_clock_seconds\": 5870.7, \"gpu_hours\": 1.63}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:00:19.246Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:00:23.213374+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_eval_loss\": 0.0701, \"train_time_seconds\": 5444, \"test_accuracy\": 86.93, \"test_f1_macro\": 86.92, \"test_precision_fail\": 86.42, \"test_precision_pass\": 87.41, \"test_recall_fail\": 86.51, \"test_recall_pass\": 87.32, \"test_n\": 1890}, \"completed_at\": \"2026-05-16T08:05:23.016Z\", \"hypothesis\": \"DeepSeek CLS func-level 验证 CLS 分类任务在 DeepSeek-coder-6.7B 上的表现，预期与 Qwen func-level CLS 水平相当（86-89%），建立第二模型家族 baseline\"}, \"deepseek-cwm-func\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:27:30.350Z\", \"updated_at\": \"2026-05-17T02:55:46.579Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 python3 train_unified.py --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/ --task cwm --output_dir /root/autodl-tmp/checkpoints_deepseek_cwm_func/ --run_name deepseek-cwm-func-level --epochs 3 --no_wandb\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"470341\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-cwm-func.log\", \"submitted_at\": \"2026-05-16T06:27:29.952Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_cwm_func/best/\", \"wall_clock_seconds\": 5626.0, \"gpu_hours\": 1.56}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:56:41.785Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:56:45.618056+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"best_eval_loss\": 0.04292, \"train_time_seconds\": 5215, \"test_accuracy\": 85.77, \"test_f1_macro\": 85.73, \"test_precision_fail\": 80.07, \"test_precision_pass\": 93.18, \"test_recall_fail\": 93.86, \"test_recall_pass\": 78.22, \"test_unparseable_rate\": 0, \"test_n\": 1890}, \"completed_at\": \"2026-05-16T08:01:15.997Z\", \"hypothesis\": \"DeepSeek CWM func-level 验证 CWM 任务在第二模型家族上的表现，预期 CWM≈CLS（与 Qwen func-level gap &lt;2pp 一致），确认跨模型 CLS≈CWM 规律\"}, \"deepseek-traj-repo-8k-s999\": {\"status\": \"DONE\", \"hypothesis\": \"DeepSeek TRAJ repo-level@8k seed=999，multi-seed 稳定性验证\", \"parent\": \"deepseek-traj-repo-8k\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:01:18.947Z\", \"updated_at\": \"2026-05-16T16:51:39.701Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 python3 train_traj_verifier.py --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full --data_prefix traj --lora_rank 16 --lora_alpha 32 --max_seq_length 8192 --epochs 3 --batch_size 1 --grad_accumulation 8 --lr 2e-4 --seed 999 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s999/ --run_name deepseek-traj-repo-8k-s999\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/swebench_full/traj_train.jsonl\", \"data_count\": 386, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 999, \"gpu\": [\"cuda:3\"], \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s999/best/\", \"log_path\": \"/root/runs/exec-sim-repair-verifier/deepseek-traj-repo-8k-s999.log\"}, \"metrics\": {\"test_accuracy\": 79.2, \"unparseable\": 0, \"best_eval_loss\": 0.1565, \"resolved_f1\": 82.1, \"unresolved_f1\": 75, \"f1_macro\": 78.57, \"train_loss\": 0.2184}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T16:51:39.702Z\"}, \"deepseek-traj-repo-8k-s456\": {\"status\": \"DONE\", \"hypothesis\": \"DeepSeek TRAJ repo-level@8k seed=456，multi-seed 稳定性验证\", \"parent\": \"deepseek-traj-repo-8k\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:01:17.202Z\", \"updated_at\": \"2026-05-16T16:38:51.114Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 python3 train_traj_verifier.py --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full --data_prefix traj --lora_rank 16 --lora_alpha 32 --max_seq_length 8192 --epochs 3 --batch_size 1 --grad_accumulation 8 --lr 2e-4 --seed 456 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s456/ --run_name deepseek-traj-repo-8k-s456\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/swebench_full/traj_train.jsonl\", \"data_count\": 386, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 456, \"gpu\": [\"cuda:3\"], \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s456/best/\", \"log_path\": \"/root/runs/exec-sim-repair-verifier/deepseek-traj-repo-8k-s456.log\"}, \"metrics\": {\"test_accuracy\": 75, \"unparseable\": 0, \"best_eval_loss\": 0.1547, \"resolved_f1\": 75, \"unresolved_f1\": 75, \"f1_macro\": 75, \"train_loss\": 0.2176}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T16:38:51.114Z\"}, \"deepseek-traj-repo-8k-s0\": {\"status\": \"DONE\", \"hypothesis\": \"DeepSeek TRAJ repo-level@8k seed=0，multi-seed 稳定性验证\", \"parent\": \"deepseek-traj-repo-8k\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:01:13.961Z\", \"updated_at\": \"2026-05-16T16:38:45.542Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 python3 train_traj_verifier.py --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full --data_prefix traj --lora_rank 16 --lora_alpha 32 --max_seq_length 8192 --epochs 3 --batch_size 1 --grad_accumulation 8 --lr 2e-4 --seed 0 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s0/ --run_name deepseek-traj-repo-8k-s0\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/swebench_full/traj_train.jsonl\", \"data_count\": 386, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 0, \"gpu\": [\"cuda:2\"], \"pid\": \"530525\", \"log_path\": \"/tmp/train_traj_8k_s0.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s0/best\"}, \"conclusion\": \"success\", \"metrics\": {\"test_accuracy\": 75, \"f1_macro\": 72.68, \"majority_baseline\": 54.2, \"gap_vs_majority_pp\": 20.8, \"unresolved_f1\": 64.7, \"resolved_f1\": 80.6, \"unresolved_precision\": 91.7, \"unresolved_recall\": 50, \"resolved_precision\": 69.4, \"resolved_recall\": 96.2, \"per_test_consistency\": 75, \"unparseable_rate\": 0, \"test_n\": 48, \"train_loss_final\": 0.2125, \"eval_loss_best\": 0.1013}, \"completed_at\": \"2026-05-16T16:38:02.088Z\"}, \"deepseek-traj-repo-8k-s789\": {\"status\": \"DONE\", \"hypothesis\": \"DeepSeek TRAJ repo-level@8k seed=789，multi-seed 稳定性验证\", \"parent\": \"deepseek-traj-repo-8k\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:01:15.534Z\", \"updated_at\": \"2026-05-16T16:38:14.182Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 python3 train_traj_verifier.py --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full --data_prefix traj --lora_rank 16 --lora_alpha 32 --max_seq_length 8192 --epochs 3 --batch_size 1 --grad_accumulation 8 --lr 2e-4 --seed 789 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s789/ --run_name deepseek-traj-repo-8k-s789\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/swebench_full/traj_train.jsonl\", \"data_count\": 386, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 789, \"gpu\": [\"cuda:2\"], \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s789/best\", \"log_path\": \"/tmp/train_traj_8k_s789.log\"}, \"conclusion\": \"success\", \"metrics\": {\"test_accuracy\": 66.67, \"resolved_f1\": 75, \"unresolved_f1\": 50, \"best_eval_loss\": 0.1295, \"unparseable\": 0}, \"completed_at\": \"2026-05-16T16:38:14.182Z\"}, \"deepseek-traj-repo-8k-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:24:57.265Z\", \"updated_at\": \"2026-05-16T15:37:42.424Z\", \"hypothesis\": \"TRAJ repo 8k seed 123 replication\", \"spec\": {\"command\": \"python3 train_traj_verifier.py --model_name deepseek-coder-6.7b-instruct --max_seq_length 8192 --epochs 3 --batch_size 1 --grad_accumulation 8 --lr 2e-4 --seed 123\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"525539\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-traj-repo-8k-s123.log\", \"submitted_at\": \"2026-05-16T15:26:36.984Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/swebench_full/traj_train.jsonl\", \"data_count\": 386, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 123, \"wall_clock_seconds\": 665.4, \"gpu_hours\": 0.18}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s123/best\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-traj-repo-8k-s123.log\", \"conclusion\": \"success\", \"metrics\": {\"test_accuracy\": 75, \"unparseable\": 0, \"best_eval_loss\": 0.1182, \"best_epoch\": 2, \"train_truncated_pct\": 2.1, \"gpu_mem_mib\": 21399, \"resolved_f1\": 76.92, \"unresolved_f1\": 72.73}, \"completed_at\": \"2026-05-16T15:37:42.424Z\"}, \"deepseek-traj-repo-8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:24:55.739Z\", \"updated_at\": \"2026-05-16T15:37:40.913Z\", \"hypothesis\": \"TRAJ repo at seq_length=8192 (fair comparison with CLS/CWM repo) reduces unparseable rate and improves accuracy vs 2048 truncated version\", \"spec\": {\"command\": \"python3 train_traj_verifier.py --model_name deepseek-coder-6.7b-instruct --max_seq_length 8192 --epochs 3 --batch_size 1 --grad_accumulation 8 --lr 2e-4 --seed 42\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"525459\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-traj-repo-8k.log\", \"submitted_at\": \"2026-05-16T15:26:34.475Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/swebench_full/traj_train.jsonl\", \"data_count\": 386, \"model_name\": \"deepseek-ai/deepseek-coder-6.7b-instruct\", \"seed\": 42, \"wall_clock_seconds\": 666.4, \"gpu_hours\": 0.19}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k/best\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-traj-repo-8k.log\", \"conclusion\": \"success\", \"metrics\": {\"test_accuracy\": 81.25, \"unparseable\": 0, \"best_eval_loss\": 0.1216, \"best_epoch\": 2, \"train_truncated_pct\": 2.1, \"gpu_mem_mib\": 22475, \"resolved_f1\": 84.21, \"unresolved_f1\": 76.92}, \"completed_at\": \"2026-05-16T15:37:40.913Z\"}, \"deepseek-traj-repo-s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:42:03.670Z\", \"updated_at\": \"2026-05-16T15:23:35.933Z\", \"hypothesis\": \"Repo-level TRAJ verifier seed 123 replication for statistical significance\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 python3 train_traj_verifier.py --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full --data_prefix traj --lora_rank 16 --lora_alpha 32 --max_seq_length 2048 --epochs 3 --batch_size 2 --grad_accumulation 4 --lr 2e-4 --seed 123 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_traj_repo_s123/ --run_name deepseek-traj-repo-s123\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"520761\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-traj-repo-s123.log\", \"submitted_at\": \"2026-05-16T14:44:28.931Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/swebench_full/traj_train.jsonl\", \"data_count\": 386, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_traj_repo_s123/best\", \"wall_clock_seconds\": 2347.0, \"gpu_hours\": 0.65}, \"metrics\": {\"test_accuracy\": 0.771, \"best_eval_loss\": 0.1147, \"best_step\": 98, \"train_loss\": 0.12, \"unparseable_rate\": 0.167, \"resolved_recall\": 0.962, \"unresolved_recall\": 0.545, \"total_test\": 48}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T15:23:35.933Z\"}, \"deepseek-traj-repo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:42:01.929Z\", \"updated_at\": \"2026-05-16T15:23:34.502Z\", \"hypothesis\": \"Repo-level TRAJ (trajectory) verifier performs worse than per-test CLS/CWM, consistent with func-level finding that CLS≥CWM≥TRAJ\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && HF_HUB_OFFLINE=1 python3 train_traj_verifier.py --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/swebench_full --data_prefix traj --lora_rank 16 --lora_alpha 32 --max_seq_length 2048 --epochs 3 --batch_size 2 --grad_accumulation 4 --lr 2e-4 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_traj_repo/ --run_name deepseek-traj-repo-s42\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"520683\", \"log_path\": \"~/runs/exec-sim-repair-verifier/deepseek-traj-repo.log\", \"submitted_at\": \"2026-05-16T14:44:26.286Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/swebench_full/traj_train.jsonl\", \"data_count\": 386, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_traj_repo/best\", \"wall_clock_seconds\": 2348.2, \"gpu_hours\": 0.65}, \"metrics\": {\"test_accuracy\": 0.771, \"best_eval_loss\": 0.111, \"best_step\": 98, \"train_loss\": 0.12, \"unparseable_rate\": 0.167, \"resolved_recall\": 0.962, \"unresolved_recall\": 0.545, \"total_test\": 48}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T15:23:34.502Z\"}, \"deepseek-traj-func-v2-s123\": {\"status\": \"DONE\", \"parent\": \"deepseek-traj-func-v2\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:47:04.812Z\", \"updated_at\": \"2026-05-16T14:35:44.136Z\", \"hypothesis\": \"DeepSeek TRAJ func-level seed=123 复现，验证 DeepSeek TRAJ 结果的 multi-seed 稳定性\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T13:47:10.604094+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 python3 train_traj_verifier.py --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/ --train_file traj_train.jsonl --val_file traj_val.jsonl --lora_rank 16 --lora_alpha 32 --max_seq_length 2048 --epochs 3 --batch_size 2 --grad_accumulation 4 --lr 2e-4 --seed 123 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_traj_v2_s123/ --run_name deepseek-traj-v2-s123\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/traj_train.jsonl\", \"data_count\": 8052, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 123, \"gpu\": [\"cuda:3\"], \"pid\": \"513115\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_traj_v2_s123/best\", \"log_path\": \"/tmp/deepseek_traj_v2_s123.log\"}, \"metrics\": {\"best_eval_loss\": 0.077, \"best_step\": 504, \"test_accuracy\": 0.8508, \"majority_baseline\": 0.5359, \"train_loss\": 0.0842, \"train_runtime_seconds\": 3021, \"per_test_consistency\": 0.782}, \"completed_at\": \"2026-05-16T14:35:44.136Z\"}, \"deepseek-traj-func-v2\": {\"status\": \"DONE\", \"parent\": \"deepseek-traj-func\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:46:37.918Z\", \"updated_at\": \"2026-05-16T14:23:22.554Z\", \"hypothesis\": \"DeepSeek TRAJ func-level v2（修复 v1 问题），验证 TRAJ 在 DeepSeek 上的可靠表现\", \"failure_reason\": \"NOT_FAILED: training completed successfully (3 epochs, 756 steps, train_loss=0.0857, eval_loss=0.0891). Best checkpoint saved at /root/autodl-tmp/checkpoints_deepseek_traj_v2/best. Process exited normally after completion.\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T13:46:41.254478+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 python3 train_traj_verifier.py --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --data_dir data/ --train_file traj_train.jsonl --val_file traj_val.jsonl --lora_rank 16 --lora_alpha 32 --max_seq_length 2048 --epochs 3 --batch_size 2 --grad_accumulation 4 --lr 2e-4 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_traj_v2/ --run_name deepseek-traj-v2-s42\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/traj_train.jsonl\", \"data_count\": 8052, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 42, \"gpu\": [\"cuda:2\"], \"pid\": \"511676\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_traj_v2/best\", \"log_path\": \"/tmp/deepseek_traj_v2.log\"}, \"completed_at\": \"2026-05-16T14:20:39.090Z\", \"metrics\": {\"best_eval_loss\": 0.0796, \"best_step\": 504, \"test_accuracy\": 0.8324, \"majority_baseline\": 0.5359, \"train_loss\": 0.0857, \"train_runtime_seconds\": 3069.6}}, \"deepseek-traj-func\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:09:15.058Z\", \"updated_at\": \"2026-05-16T12:58:15.907Z\", \"hypothesis\": \"DeepSeek TRAJ func-level 验证 trajectory verifier 在第二模型家族上的表现，预期与 Qwen TRAJ 类似（~86%）\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 python3 train_unified.py --model_name_or_path /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --task cls --granularity func --train_file traj_train_cls.jsonl --val_file traj_val_cls.jsonl --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_deepseek_traj_func/\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/swebench_full/traj_train_cls.jsonl\", \"data_count\": 8052, \"model_name\": \"deepseek-coder-6.7b-instruct\", \"seed\": 42}, \"metrics\": {\"eval_loss_epoch1\": 0.0943, \"eval_loss_epoch2\": 0.0793, \"eval_loss_epoch3\": 0.0884, \"best_eval_loss\": 0.0793, \"best_step\": 1008, \"best_epoch\": 2, \"train_loss\": 0.1131, \"train_runtime_sec\": 2910.6}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_deepseek_traj_func/best\", \"log_path\": \"/tmp/deepseek_traj_func.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T12:58:15.907Z\"}, \"cwm8b-ckpt400-test-eval-shard2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:27:27.393Z\", \"updated_at\": \"2026-05-16T05:31:43.839Z\", \"hypothesis\": \"CWM 8B ckpt-400 test eval shard 2/4，分片并行评估加速\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 8 --max_new_tokens 1024 --start_idx 7680 --output_dir /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard2/\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/swebench_full/swebench_test.jsonl\", \"data_count\": 2104, \"model_name\": \"Qwen3-8B + CWM LoRA ckpt-400\", \"seed\": null, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-400\", \"eval_data\": \"swebench_test (idx 7680-9784)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard2/\", \"log_path\": \"/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard2/eval_repo_cwm.json\", \"completed_at\": \"2026-05-16T05:31:43.839Z\"}, \"cwm8b-ckpt400-test-eval-shard4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:52:45.544Z\", \"updated_at\": \"2026-05-16T04:34:48.371Z\", \"hypothesis\": \"CWM 8B ckpt-400 test eval shard 4/4，分片并行评估加速\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 python3 eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 8 --max_new_tokens 1024 --start_idx 9100 --output_dir /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard4/\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard4/\", \"data_count\": 684, \"model_name\": \"Qwen3-8B + CWM ckpt-400\", \"seed\": 42, \"checkpoint_source\": \"cwm8b-ckpt400-test-eval-v3\", \"eval_data\": \"test split idx 9100-9783 (684 samples)\", \"kill_reason\": \"Never submitted via submit_training_job (no PID, no tmux, no cron). Range 9100-9783 fully covered by shard2 (7680-9784). Orphan registry entry.\", \"log_path\": \"N/A\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T04:34:07.005Z\"}, \"cwm4b-s42-mutation-breakdown\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:33:17.769Z\", \"updated_at\": \"2026-05-16T02:33:36.196Z\", \"hypothesis\": \"CWM 4B s42 per-mutation-type breakdown，与 CLS 对比验证 CWM 在哪些 mutation 类型上劣势更大\", \"spec\": {\"command\": \"mutation_breakdown.py on existing CWM 4B predictions\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"CWM 4B test predictions\", \"data_count\": 9784, \"model_name\": \"Qwen3-4B + CWM LoRA\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis of existing predictions)\", \"log_path\": \"artifacts/cwm4b_mutation_breakdown.json\"}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 58.04, \"parseable_rate\": 46.3, \"parseable_only_accuracy\": 42.9, \"gold_parse_rate\": 43.5, \"gold_parseable_acc\": 23.5, \"operator_swap_parse_rate\": 56.9, \"operator_swap_parseable_acc\": 63.1, \"off_by_one_parse_rate\": 4.4, \"off_by_one_parseable_acc\": 0, \"return_value_parse_rate\": 48.8, \"return_value_parseable_acc\": 27, \"boundary_removal_parse_rate\": 30.6, \"boundary_removal_parseable_acc\": 59.2, \"n_instances\": 9784}, \"completed_at\": \"2026-05-16T02:33:36.196Z\"}, \"cls4b-ckpt4600-test-mutation-pr\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:30:55.662Z\", \"updated_at\": \"2026-05-16T02:31:18.691Z\", \"hypothesis\": \"4B CLS ckpt-4600 test mutation-type precision/recall breakdown，论文 Table 数据\", \"spec\": {\"command\": \"eval_repo_cls.py + per-mutation P/R breakdown on home server\", \"server\": \"home-1x5090\", \"data_path\": \"data/swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"checkpoints_repo_cls_v5/checkpoint-4600\", \"eval_data\": \"swebench_test\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/checkpoint-4600/\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/results/cls4b_ckpt4600_test_mutation_breakdown.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 83.63, \"gold_acc\": 98.25, \"operator_swap_acc\": 78.91, \"return_value_acc\": 67.97, \"off_by_one_acc\": 58.47, \"boundary_removal_acc\": 46.9, \"n_instances\": 9784, \"note\": \"off_by_one recall_fail=0 (all predicted pass); boundary_removal identical to 8B\"}, \"completed_at\": \"2026-05-16T02:31:18.691Z\"}, \"cls8b-seed123-ckpt3000-mutation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:21:39.827Z\", \"updated_at\": \"2026-05-16T02:25:49.152Z\", \"hypothesis\": \"CLS 8B seed123 ckpt-3000 test mutation breakdown — 跨 seed 验证 boundary_removal failure mode\", \"spec\": {\"command\": \"eval_repo_cls.py + mutation_breakdown.py\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"data/swebench_full/swebench_test.jsonl\", \"data_count\": 0, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000/\", \"eval_data\": \"swebench_test\", \"pid\": 447483, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000/\", \"log_path\": \"/root/autodl-tmp/eval_results/cls8b_seed123_ckpt3000_mutation/\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 85.6, \"boundary_removal\": 44.9, \"operator_swap\": 82.6, \"return_value\": 66.4, \"off_by_one\": 79.2, \"gold\": 99.6, \"n_samples\": 9784}, \"completed_at\": \"2026-05-16T02:25:49.152Z\"}, \"cls8b-s42-resume-ckpt3600-test-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:18:39.982Z\", \"updated_at\": \"2026-05-16T02:25:47.677Z\", \"hypothesis\": \"ckpt-3600 test 评估修正版（v1 数据问题），获取准确 test 指标\", \"spec\": {\"command\": \"eval_repo_cls.py --checkpoint_dir checkpoint-3600 --split test --batch_size 1 --max_seq_length 8192\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": 446868, \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-resume-ckpt3600-test-v2.log\", \"submitted_at\": \"2026-05-16T01:19:03.561Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-3600/\", \"eval_data\": \"test split n=9784\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-3600/\", \"wall_clock_seconds\": 4004.1, \"gpu_hours\": 1.11}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 84.48, \"f1_macro\": 78.17, \"fail_recall\": 56.8, \"pass_recall\": 94.8, \"n_samples\": 9784, \"note\": \"reproduces v1 exactly\"}, \"completed_at\": \"2026-05-16T02:25:47.677Z\"}, \"cls8b-s42-resume-ckpt3600-mutation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:34:55.660Z\", \"updated_at\": \"2026-05-16T01:15:08.404Z\", \"hypothesis\": \"8B CLS resume ckpt-3600 per-mutation-type breakdown，验证跨 checkpoint 的 mutation 难度排序稳定性\", \"failure_reason\": \"CLEARED: was false positive from cron. Experiment still in PREPARING, awaiting GPU allocation.\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:35:02.463599+00:00\"}]}, \"spec\": {\"command\": \"python3 mutation_breakdown.py (post-processing from existing predictions)\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-3600/\", \"eval_data\": \"test\", \"parent\": \"cls8b-s42-resume-ckpt3600-test\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-3600/\", \"log_path\": \"/root/autodl-tmp/eval_results/cls8b_s42_resume_test_ckpt3600_mutation/\"}, \"metrics\": {\"overall_accuracy\": 84.4849, \"overall_correct\": 8266, \"overall_total\": 9784, \"gold_accuracy\": 96.2443, \"gold_correct\": 4459, \"gold_total\": 4633, \"mutation_operator_swap_accuracy\": 81.3822, \"mutation_operator_swap_correct\": 2732, \"mutation_operator_swap_total\": 3357, \"mutation_off_by_one_accuracy\": 86.8852, \"mutation_off_by_one_correct\": 159, \"mutation_off_by_one_total\": 183, \"mutation_return_value_accuracy\": 75.4448, \"mutation_return_value_correct\": 424, \"mutation_return_value_total\": 562, \"mutation_boundary_removal_accuracy\": 46.9018, \"mutation_boundary_removal_correct\": 492, \"mutation_boundary_removal_total\": 1049}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-3600/\", \"log_path\": \"/root/autodl-tmp/eval_results/cls8b_s42_resume_test_ckpt3600_mutation/\", \"completed_at\": \"2026-05-16T01:13:58.493Z\"}, \"cls8b-s42-resume-ckpt3600-test\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:34:43.691Z\", \"updated_at\": \"2026-05-16T01:08:43.143Z\", \"hypothesis\": \"8B CLS s42 resume ckpt-3600 test 评估，验证是否为新 test-best\", \"failure_reason\": \"FALSE POSITIVE: cron误判——实验仍在PREPARING从未提交，无进程是正常状态。需重新提交。\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:34:47.164915+00:00\"}]}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-3600/\", \"log_path\": \"eval results in memory.md\", \"metrics\": {\"accuracy\": 84.48, \"f1_macro\": 78.17, \"unparseable\": 0, \"n_samples\": 9784}}, \"completed_at\": \"2026-05-16T01:08:43.143Z\"}, \"cls8b-s42-ckpt3600-seq2048-ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:48:09.625Z\", \"updated_at\": \"2026-05-16T00:38:31.977Z\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-3600/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 1 --max_seq_length 2048 --max_new_tokens 8 --output_dir /root/autodl-tmp/eval_results/cls8b_s42_resume_ckpt3600_test_seq2048/\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"ckpt-3600 (val-best from resume sweep)\", \"eval_data\": \"test split n=9784\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-3600/\", \"log_path\": \"/tmp/eval_cls8b_ckpt3600_seq2048.log\", \"output_dir\": \"/root/autodl-tmp/eval_results/cls8b_s42_resume_ckpt3600_test_seq2048/\", \"max_seq_length\": 2048, \"batch_size\": 1, \"purpose\": \"Appendix B seq-length ablation\"}, \"hypothesis\": \"CLS 8B ckpt-3600 @seq2048 ablation: 测试新 val-best 在短 context 下表现，与 ckpt-1000 @2048 (82.83%) 对比\", \"reproduce\": {\"finished_at\": \"2026-05-16T00:24:10.728Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T00:24:13.557Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:24:17.644744+00:00\"}]}, \"metrics\": {\"accuracy\": 83.04, \"f1_macro\": 76.8, \"unparseable\": 136, \"n_samples\": 9784, \"seq_length\": 2048}}, \"cls8b-s42-resume-val-sweep-seq8192-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:43:36.203Z\", \"updated_at\": \"2026-05-15T22:33:50.928Z\", \"spec\": {\"command\": \"bash /root/autodl-tmp/scripts/cls8b_s42_resume_val_sweep.sh\", \"server\": \"seetacloud-westd-4x5090\", \"pid\": 398981, \"gpu\": [\"cuda:0\"], \"data_path\": \"data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-resume-val-sweep-seq8192-v2.log\", \"batch_size\": 1, \"max_seq_length\": 8192}, \"hypothesis\": \"s42 resume val sweep (seq8192 bs=1): 21 checkpoints (1800-5800), 与 baseline 一致的 seq_length\", \"notes\": \"Early terminated after ckpt-3800 (unique range 1800-3800 fully evaluated on cuda:0). ckpt-4000-5800 already covered by cuda:1 sweep (PID 405526). 11 unique checkpoints from this sweep: 1800-3800. Results dir also contains 4000-5400 which were evaluated before kill.\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/eval_results/cls_8b_s42_resume_val/\", \"completed_at\": \"2026-05-15T22:32:47.767Z\"}, \"repo-level-cls-8b-s42-resume\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:48:30.781Z\", \"updated_at\": \"2026-05-15T18:51:06.920Z\", \"hypothesis\": \"8B CLS s42 resume 训练（从 ckpt-600 继续），获取更多 checkpoint 用于 val/test sweep\", \"spec\": {\"command\": \"python train_repo_verifier.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --batch_size 1 --grad_accumulation 32 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/ --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-600 --save_total_limit 35 --dataloader_num_workers 0 --epochs 3\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"295789\", \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-8b-s42-resume.log\", \"submitted_at\": \"2026-05-14T21:48:30.485Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"resume_checkpoint\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-600\", \"save_steps\": 200, \"num_workers\": 0, \"lora_r\": 16, \"lora_alpha\": 32, \"hypothesis\": \"8B CLS s42 full training (ckpt-600 -> 6633), every 200 steps save checkpoint, for CLS vs CWM apple-to-apple comparison + val sweep\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/\", \"wall_clock_seconds\": 75197.4, \"gpu_hours\": 20.89}, \"notes\": \"best/ 目录验证: 包含旧 run (checkpoints_repo_cls_8b_conda) 的 step-200 权重 (eval_loss=0.0796), 由 Trainer load_best_model_at_end 在训练结束时自动保存。不是 ckpt-1000 也不是 ckpt-6633。主表使用 val-selected ckpt-1000, 不受影响。\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:37:51.216Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:37:55.023198+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 6633, \"epochs\": 3, \"train_time_sec\": 74425, \"final_train_loss\": 0.4284, \"final_eval_loss\": 0.4768, \"best_eval_loss_resume\": 0.2516, \"best_eval_loss_resume_step\": 4200, \"best_eval_loss_overall\": 0.0796, \"best_eval_loss_overall_step\": 200, \"checkpoints_saved\": 32, \"overfitting\": true, \"note\": \"Severe overfitting after epoch 2. Resume-best=ckpt-4200. Val sweep running on cuda:0.\"}, \"completed_at\": \"2026-05-15T18:41:47.899Z\"}, \"cwm-rank32-alpha64-ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:15:21.249Z\", \"updated_at\": \"2026-05-15T16:03:03.126Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir checkpoints_cwm_rank32_alpha64/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 --lora_rank 32 --lora_alpha 64\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"pid\": 379609, \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-rank32-alpha64-ablation.log\", \"submitted_at\": \"2026-05-15T14:15:20.783Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"lora_rank\": 32, \"lora_alpha\": 64, \"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 2, \"grad_accumulation\": 16, \"total_steps\": 1434, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_rank32_alpha64/\", \"description\": \"CWM rank=32 alpha=64 ablation. Fixes alpha/rank ratio confound from v2 (ratio=2, matching baseline).\", \"wall_clock_seconds\": 5508.5, \"gpu_hours\": 1.53}, \"hypothesis\": \"LoRA rank ablation 修正：CWM 4B rank=32, alpha=64 (alpha/rank=2，匹配 baseline ratio)。Reviewer 指出 cwm-rank32-ablation-v2 的 alpha=32 导致 effective scaling factor 减半（ratio=1 vs baseline ratio=2），构成混淆变量。本实验修正 alpha 使 ratio 一致，验证 rank=32 在公平 scaling 下是否仍与 rank=16 无差异。\", \"reproduce\": {\"finished_at\": \"2026-05-15T15:40:31.748Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:40:34.962371+00:00\"}]}, \"metrics\": {\"accuracy\": 87.04, \"pass_f1\": 86.79, \"fail_f1\": 87.27, \"f1_macro\": 87.03, \"pass_precision\": 91.8, \"pass_recall\": 82.3, \"fail_precision\": 82.9, \"fail_recall\": 92.1, \"exact_match_rate\": 84.55, \"train_loss\": 0.2069, \"eval_loss\": 0.0606, \"n_instances\": 1890, \"vs_rank16_baseline\": -0.47, \"rank16_baseline_accuracy\": 87.51}, \"conclusion\": \"success\", \"notes\": \"rank=32 alpha=64 (ratio=2) accuracy=87.0%，与 rank=32 alpha=32 (ratio=1) 完全一致，均低于 baseline rank=16 (87.51%)。结论：alpha/rank ratio 不是混淆变量，rank=16 已足够，增加 rank 轻微损害泛化。epoch2 eval_loss 最低(0.0555) → epoch3 回升(0.0606)，轻微过拟合与过参数化一致。\", \"completed_at\": \"2026-05-15T15:47:09.278Z\"}, \"cls8b-seed123-ckpt6200-test-eval-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:09:10.387Z\", \"updated_at\": \"2026-05-15T14:04:08.427Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 1 --max_seq_length 8192 --max_new_tokens 8 --output_dir /root/autodl-tmp/eval_results/cls8b_seed123_ckpt6200_test/ --output eval_summary.json --pred_output eval_predictions.jsonl\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"377611\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6200-test-eval-v2.log\", \"submitted_at\": \"2026-05-15T14:03:12.423Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6200\", \"eval_data\": \"test@full(n=9784)\"}, \"hypothesis\": \"seed123 test curve 补点: ckpt-6200 test@full(n=9784)。修复 v1 的 --max_samples 8192 bug（只评了 8192/9784），改为全量评估。\", \"reproduce\": {\"finished_at\": \"2026-05-15T10:30:50.246Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:30:53.672771+00:00\"}]}, \"metrics\": {\"accuracy\": 84.7, \"f1_fail\": 63.71, \"f1_pass\": 90.31, \"f1_macro\": 77.01, \"precision_fail\": 88.84, \"precision_pass\": 83.96, \"recall_fail\": 49.66, \"recall_pass\": 97.69, \"n_instances\": 9784, \"n_cls_unparseable\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6200/eval_test_full/\", \"completed_at\": \"2026-05-15T10:32:49.699Z\"}, \"cwm-rank32-ablation-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:50:32.964Z\", \"updated_at\": \"2026-05-15T14:03:09.909Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir checkpoints_cwm_rank32/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 --lora_rank 32\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"log_path\": \"/root/runs/exec-sim-repair-verifier/cwm-rank32-ablation.log\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_rank32/\", \"gpu\": \"cuda:0\", \"pid\": 368823, \"lora_rank\": 32, \"lora_alpha\": 32, \"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 2, \"grad_accumulation\": 16, \"total_steps\": 1434, \"description\": \"CWM rank=32 ablation (vs baseline rank=16). Function-level data. Alpha kept at 32.\", \"estimated_duration\": \"~1.5h total\"}, \"hypothesis\": \"LoRA rank ablation: CWM 4B rank=32 vs baseline rank=16. 回应审稿人质疑 rank=16 是否系统性低估 CWM 能力。其余配置完全一致（lr=2e-4, epochs=3, seed=42, alpha=32, data=function-level）。PID 368823 在 GPU 0 上正常训练，step 324/1434 (22%)。注意：训练命令未串联 eval，完成后需单独触发 eval。\", \"conclusion\": \"success\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_rank32/best\", \"log_path\": \"/root/runs/exec-sim-repair-verifier/cwm-rank32-ablation.log\", \"notes\": \"诊断结论: 训练成功完成 (EXIT_CODE=0)\\n最后 step: 1434/1434 (100%)\\n训练时间: 5003.67s (~83min)\\ntrain_loss=0.2536, eval_loss=0.0688\\nCheckpoints: best/, checkpoint-1434/, checkpoint-478/\\n评估结果: accuracy=87.0% (+35.2pp), F1(fail)=87.1%, F1(pass)=86.9%, exact_match=83.4%\\nMVP-B: PASS (per-class F1>65%, gap>=10pp)\\n**Director 确认结论**: rank=32 (87.0%) vs rank=16 baseline (87.19%) 无显著差异。CWM capacity 非瓶颈，LoRA rank=16 未系统性低估 CWM 能力。\", \"metrics\": {\"accuracy\": 87, \"exact_match_rate\": 83.4, \"fail_f1\": 87.1, \"pass_f1\": 86.9, \"train_loss_final\": 0.0152, \"train_loss_avg\": 0.2536, \"eval_loss\": 0.0688, \"train_runtime_sec\": 5003, \"test_set_size\": 1890, \"vs_rank16_baseline\": -0.51, \"rank16_baseline_accuracy\": 87.51}, \"completed_at\": \"2026-05-15T13:57:05.960Z\"}, \"cls8b-seed123-ckpt200-test-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:29:27.906Z\", \"updated_at\": \"2026-05-15T12:11:58.203Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 1 --max_seq_length 8192 --max_new_tokens 8 --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-200/eval_test_full --output eval_summary.json --pred_output eval_predictions.jsonl\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"363037\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt200-test-eval.log\", \"submitted_at\": \"2026-05-15T11:29:27.560Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-200\", \"eval_data\": \"test@full(n=9784)\", \"wall_clock_seconds\": 2550.6, \"gpu_hours\": 0.71}, \"hypothesis\": \"seed123 test curve 最后补点: ckpt-200 test@full(n=9784)。完成后 seed123 test curve 6/6 全齐。\", \"reproduce\": {\"finished_at\": \"2026-05-15T11:52:02.852Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:52:06.230063+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 72.55, \"f1_macro\": 70.18, \"pass_f1\": 78.58, \"fail_f1\": 61.78, \"pass_precision\": 91.21, \"pass_recall\": 69.02, \"fail_precision\": 49.54, \"fail_recall\": 82.05, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 72.96, \"unparseable\": 0, \"confusion_matrix\": {\"tn\": 2171, \"fp\": 475, \"fn\": 2211, \"tp\": 4927}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-200\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt200-test-eval.log\", \"completed_at\": \"2026-05-15T12:11:58.203Z\"}, \"cls8b-s42-ckpt1000-test-seq2048-ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:42:13.701Z\", \"updated_at\": \"2026-05-15T11:29:21.594Z\", \"hypothesis\": \"Seq_length confound ablation: CLS 8B val-best (ckpt-1000) eval@max_seq_length=2048（与 CWM 训练配置对齐）。对比 CLS@8192=83.52%。如 CLS@2048 仍大幅超越 CWM，排除 seq_length confound。Reviewer critical 直接回应。\", \"notes\": \"高优先级 Reviewer critical。等 cuda:0 或 cuda:3 空闲后立即提交。ckpt-1000 在 /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000。命令: eval_repo_cls.py --max_seq_length 2048 --max_new_tokens 8 --split test --batch_size 1。\", \"spec\": {\"command\": \"eval_repo_cls.py --max_seq_length 2048 --max_new_tokens 8 --split test\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"360735\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1000-test-seq2048-ablation.log\", \"submitted_at\": \"2026-05-15T10:59:58.351Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000\", \"eval_data\": \"test@2048(n=9784)\", \"wall_clock_seconds\": 1763.2, \"gpu_hours\": 0.49}, \"reproduce\": {\"finished_at\": \"2026-05-15T11:26:38.401Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:26:43.647776+00:00\"}]}, \"metrics\": {\"accuracy\": 82.83, \"f1_macro\": 76.88, \"fail_precision\": 72.2, \"fail_recall\": 59.3, \"fail_f1\": 65.2, \"pass_precision\": 85.9, \"pass_recall\": 91.5, \"pass_f1\": 88.6, \"unparseable\": 136}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000\", \"completed_at\": \"2026-05-15T11:29:21.594Z\"}, \"cls8b-seed123-ckpt6633-test-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:00:01.048Z\", \"updated_at\": \"2026-05-15T11:28:43.331Z\", \"spec\": {\"command\": \"eval_repo_cls.py --checkpoint_dir ckpt-6633 --max_seq_length 8192 --split test\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"360877\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6633-test-eval.log\", \"submitted_at\": \"2026-05-15T11:00:00.305Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6633\", \"eval_data\": \"test@full(n=9784)\", \"wall_clock_seconds\": 1723.0, \"gpu_hours\": 0.48}, \"hypothesis\": \"seed123 test curve 补点: ckpt-6633 (final) test@full(n=9784)。Supplementary val+test 双线图。\", \"reproduce\": {\"finished_at\": \"2026-05-15T11:26:49.701Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:26:54.350756+00:00\"}]}, \"metrics\": {\"accuracy\": 84.89, \"f1_macro\": 77.56, \"f1_fail\": 64.7, \"f1_pass\": 90.4, \"precision_fail\": 87.8, \"recall_fail\": 51.2, \"precision_pass\": 84.3, \"recall_pass\": 97.4, \"majority_baseline\": 73, \"gap_vs_majority_pp\": 11.9, \"total_samples\": 9784, \"unparseable_count\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6633/eval_test_full/\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6633-test-eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T11:28:43.331Z\"}, \"cls8b-seed123-ckpt6600-test-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:35:08.915Z\", \"updated_at\": \"2026-05-15T10:58:57.529Z\", \"spec\": {\"command\": \"python3 eval_repo_cls.py ... ckpt-6600 test\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"358109\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6600-test-eval.log\", \"submitted_at\": \"2026-05-15T10:35:08.559Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6600\", \"eval_data\": \"test@full(n=9784)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6600\", \"wall_clock_seconds\": 1429.0, \"gpu_hours\": 0.4}, \"hypothesis\": \"seed123 test curve 补点: ckpt-6600 test@full(n=9784)。Supplementary val+test 双线图。\", \"reproduce\": {\"finished_at\": \"2026-05-15T10:56:49.721Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:56:55.215417+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 84.9, \"f1_macro\": 77.58, \"pass_f1\": 90.4, \"fail_f1\": 64.8, \"pass_precision\": 84.3, \"pass_recall\": 97.4, \"fail_precision\": 87.8, \"fail_recall\": 51.3, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 73, \"unparseable\": 0, \"confusion_matrix\": {\"fail_as_fail\": 1357, \"fail_as_pass\": 1289, \"pass_as_fail\": 188, \"pass_as_pass\": 6950}}, \"completed_at\": \"2026-05-15T10:58:57.529Z\"}, \"cls8b-s42-ckpt200-test8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:35:10.602Z\", \"updated_at\": \"2026-05-15T10:58:56.283Z\", \"spec\": {\"command\": \"python3 eval_repo_cls.py ... s42 ckpt-200 test\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"358249\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt200-test8192-eval.log\", \"submitted_at\": \"2026-05-15T10:35:10.288Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200\", \"eval_data\": \"test@full(n=9784)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200\", \"wall_clock_seconds\": 1426.0, \"gpu_hours\": 0.4}, \"hypothesis\": \"s42 test curve 补点: ckpt-200 test@full(n=9784)。补齐与 val curve 对齐的最后一个缺失点。\", \"reproduce\": {\"finished_at\": \"2026-05-15T10:56:21.866Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:56:25.466058+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 70.07, \"f1_macro\": 68.18, \"pass_f1\": 75.9, \"fail_f1\": 60.4, \"pass_precision\": 91.8, \"pass_recall\": 64.7, \"fail_precision\": 47, \"fail_recall\": 84.5, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 73, \"unparseable\": 0, \"confusion_matrix\": {\"fail_as_fail\": 2235, \"fail_as_pass\": 411, \"pass_as_fail\": 2517, \"pass_as_pass\": 4621}}, \"completed_at\": \"2026-05-15T10:58:56.283Z\"}, \"cls4b-v5-ckpt600-test5120-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:15:48.518Z\", \"updated_at\": \"2026-05-15T10:46:49.940Z\", \"spec\": {\"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/checkpoint-600\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt600-test5120-eval.log\"}, \"hypothesis\": \"4B s42 test sweep 补点: ckpt-600 test@5120。与 val curve 对齐，supplementary val+test 双线图。\", \"notes\": \"4B test curve 补点 1/3。完成后依次提交 ckpt-4000 和 ckpt-4200。\", \"reproduce\": {\"finished_at\": \"2026-05-15T10:43:54.705Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:43:58.308051+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 77.74, \"f1_macro\": 74.74, \"f1_fail\": 66.03, \"f1_pass\": 83.44, \"precision_fail\": 56.21, \"recall_fail\": 80.01, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 4.78, \"unparseable_count\": 0, \"total_samples\": 9784}, \"completed_at\": \"2026-05-15T10:46:49.940Z\"}, \"cls8b-seed123-ckpt6400-test-eval-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:09:12.759Z\", \"updated_at\": \"2026-05-15T10:33:02.486Z\", \"spec\": {\"data_path\": \"test split\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6400\", \"eval_data\": \"test@full(n=9784)\", \"parent\": \"repo-level-cls-8b-seed123-conda-v3\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 1 --max_seq_length 8192 --max_new_tokens 8 --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6400/eval_test_full --output eval_summary.json --pred_output eval_predictions.jsonl\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"355710\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6400-test-eval-v2.log\"}, \"hypothesis\": \"seed123 ckpt-6400 test eval（完整 n=9784，无 --max_samples），补充 test curve 数据点\", \"reproduce\": {\"finished_at\": \"2026-05-15T10:30:59.776Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:31:05.812128+00:00\"}]}, \"metrics\": {\"accuracy\": 85.08, \"f1_fail\": 65.32, \"f1_pass\": 90.49, \"f1_macro\": 77.91, \"precision_fail\": 87.92, \"precision_pass\": 84.54, \"recall_fail\": 51.97, \"recall_pass\": 97.35, \"n_instances\": 9784, \"n_cls_unparseable\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6400/eval_test_full/\", \"completed_at\": \"2026-05-15T10:32:51.435Z\"}, \"repo-level-cls-8b-seed123-conda-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:43:51.115Z\", \"updated_at\": \"2026-05-15T09:39:13.861Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_verifier.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --batch_size 1 --grad_accumulation 32 --seed 123 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/ --dataloader_num_workers 0 --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-3000\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"266444\", \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-8b-seed123-conda-v3.log\", \"submitted_at\": \"2026-05-14T17:43:50.914Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 37338, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"wall_clock_seconds\": 45617.8, \"gpu_hours\": 12.67, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6633/\", \"best_model_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/best/\", \"final_train_loss\": 0.162, \"final_eval_loss\": 0.464, \"train_runtime_seconds\": 45210}, \"hypothesis\": \"8B CLS seed123 训练重启（第三次提交，修正 resume 路径指向 checkpoint-3000）。与 v1/v2 同配置，num_workers=0。验证 8B CLS multi-seed robustness。\", \"parent\": \"\", \"notes\": \"2026-05-15: 训练完成 6633/6633。EXIT_CODE=129 是 SIGHUP 误报，非失败。磁盘 checkpoint: 200, 6200, 6400, 6600, 6633, best（中段被 save_total_limit 清理）。Val-best=ckpt-3000 (88.69%, from backup), test=85.60%。\", \"reproduce\": {\"finished_at\": \"2026-05-15T06:24:06.400Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:24:08.733Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:24:11.437335+00:00\"}]}}, \"cls8b-seed123-ckpt6633-val8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:42:16.467Z\", \"updated_at\": \"2026-05-15T08:57:04.203Z\", \"hypothesis\": \"seed123 val sweep: ckpt-6633 (最后一个 checkpoint) val@8192。确定 seed123 val-best。\", \"parent\": \"repo-level-cls-8b-seed123-conda-v3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6633 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split val --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_seed123_ckpt6633_val8192\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"346231\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6633\", \"eval_data\": \"val@8192\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/results/cls8b_seed123_ckpt6633_val8192\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6633-val8192-eval.log\", \"completed_at\": \"2026-05-15T08:55:48.265Z\", \"metrics\": {\"accuracy\": 87.1, \"f1_macro\": 78.79, \"f1_fail\": 65.52, \"f1_pass\": 92.07, \"precision_fail\": 92.26, \"recall_fail\": 50.8, \"precision_pass\": 86.31, \"recall_pass\": 98.64, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.23, \"unparseable_count\": 9, \"total_samples\": 9335}}, \"cls8b-seed123-ckpt3000-test8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:32:32.981Z\", \"updated_at\": \"2026-05-15T08:14:23.380Z\", \"hypothesis\": \"seed123 val-best (ckpt-3000, val=88.69%) 的 test@8192。决定 seed123 multi-seed headline number。\", \"parent\": \"repo-level-cls-8b-seed123-conda-v3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split test --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_seed123_ckpt3000_test8192\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt3000-test8192-eval.log\", \"submitted_at\": \"2026-05-15T15:33:50Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000\", \"eval_data\": \"test@8192\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T07:55:14.458Z\", \"notes\": \"v1 进程 PID 345441 实际一直在跑（从未被 kill）。之前误标 DONE/failed 是因为 Reviewer 报告\\\"无 PID 无日志\\\"但实际进程已启动。v2 因与 v1 同 GPU 导致 OOM。保留 v1 收集结果。教训：标 FAILED 前必须 ps -p PID 确认进程已退出。\", \"metrics\": {\"accuracy\": 85.6, \"f1_macro\": 78.38, \"f1_fail\": 65.89, \"f1_pass\": 90.87, \"precision_fail\": 91.65, \"recall_fail\": 51.44, \"precision_pass\": 84.52, \"recall_pass\": 98.26, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.64, \"unparseable_count\": 0, \"total_samples\": 9784}, \"checkpoint_path\": \"/root/autodl-tmp/results/cls8b_seed123_ckpt3000_test8192\"}, \"cls4b-v5-ckpt4400-test5120-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:29:48.065Z\", \"updated_at\": \"2026-05-15T07:59:20.222Z\", \"hypothesis\": \"4B test sweep 补点: ckpt-4400 test@5120。Supplementary val+test 双线图数据。\", \"parent\": \"cls4b-v5-train\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4400 --model_name Qwen/Qwen3-4B --split test --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/repo_cls_v5_ckpt4400_test5120\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3244661\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt4400-test5120-eval.log\", \"submitted_at\": \"2026-05-15T07:30:01.279Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"wall_clock_seconds\": 1752.2, \"gpu_hours\": 0.49}, \"conclusion\": \"success\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/results/repo_cls_v5_ckpt4400_test5120\", \"completed_at\": \"2026-05-15T07:59:13.441Z\", \"metrics\": {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_fail\": 59.45, \"f1_pass\": 89.44, \"precision_fail\": 85.98, \"recall_fail\": 45.43, \"precision_pass\": 82.78, \"recall_pass\": 97.25, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.28, \"unparseable_count\": 0, \"total_samples\": 9784}}, \"cls8b-seed123-ckpt6400-val8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:25:25.076Z\", \"updated_at\": \"2026-05-15T07:58:50.500Z\", \"hypothesis\": \"seed123 val sweep: ckpt-6400 val@8192\", \"parent\": \"repo-level-cls-8b-seed123-conda-v3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split val --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_seed123_ckpt6400_val8192\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"343011\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6400-val8192-eval.log\", \"submitted_at\": \"2026-05-15T07:26:03.290Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1959.6, \"gpu_hours\": 0.54}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/results/cls8b_seed123_ckpt6400_val8192\", \"completed_at\": \"2026-05-15T07:58:42.916Z\", \"metrics\": {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_fail\": 67.04, \"f1_pass\": 92.27, \"precision_fail\": 91.81, \"recall_fail\": 52.8, \"precision_pass\": 86.78, \"recall_pass\": 98.5, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.6, \"unparseable_count\": 9, \"total_samples\": 9335}}, \"cls8b-seed123-ckpt6200-val8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:29:36.909Z\", \"updated_at\": \"2026-05-15T07:58:33.467Z\", \"hypothesis\": \"seed123 val sweep: ckpt-6200 val@8192（与 cuda:3 ckpt-6400 并行加速）\", \"parent\": \"repo-level-cls-8b-seed123-conda-v3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split val --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_seed123_ckpt6200_val8192\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"343605\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6200-val8192-eval.log\", \"submitted_at\": \"2026-05-15T07:29:46.229Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1727.2, \"gpu_hours\": 0.48}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_fail\": 66.16, \"f1_pass\": 92.35, \"precision_fail\": 95.63, \"recall_fail\": 50.58, \"precision_pass\": 86.33, \"recall_pass\": 99.27, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.64, \"unparseable_count\": 9, \"total_samples\": 9335}, \"checkpoint_path\": \"/root/autodl-tmp/results/cls8b_seed123_ckpt6200_val8192\", \"completed_at\": \"2026-05-15T07:58:33.467Z\"}, \"cls4b-v5-val-sweep-ckpt4600\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:50:50.548Z\", \"updated_at\": \"2026-05-15T07:41:04.726Z\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4600 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/repo_cls_v5_ckpt4600_val5120\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3221945\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-val-sweep-ckpt4600.log\", \"submitted_at\": \"2026-05-15T04:42:23.647Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"wall_clock_seconds\": 10715.3, \"gpu_hours\": 2.98}, \"hypothesis\": \"4B v5 val sweep 最后一个数据点: ckpt-4600 val@5120。确认 val-best 是否在 ckpt-4400(89.96%) 之后继续改善。\", \"parent\": \"cls4b-v5-train\", \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints_repo_cls_v5/checkpoint-4600\", \"completed_at\": \"2026-05-15T07:40:58.936Z\", \"metrics\": {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_fail\": 76.37, \"f1_pass\": 93.71, \"precision_fail\": 89.65, \"recall_fail\": 66.52, \"precision_pass\": 90.16, \"recall_pass\": 97.56, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 14.19, \"unparseable_count\": 0, \"total_samples\": 9335, \"n_truncated\": 234}}, \"cls8b-seed123-ckpt6600-val8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:49:01.026Z\", \"updated_at\": \"2026-05-15T07:25:59.750Z\", \"hypothesis\": \"seed123 val sweep: ckpt-6600 val@8192。确定 seed123 val-best。\", \"parent\": \"repo-level-cls-8b-seed123-conda-v3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6600 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split val --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_seed123_ckpt6600_val8192\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"340511\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6600-val8192-eval.log\", \"submitted_at\": \"2026-05-15T06:49:09.694Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2204.3, \"gpu_hours\": 0.61}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6600\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123-ckpt6600-val8192-eval.log\", \"completed_at\": \"2026-05-15T07:25:54.003Z\", \"metrics\": {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_fail\": 65.9, \"f1_pass\": 92.14, \"precision_fail\": 92.6, \"recall_fail\": 51.15, \"precision_pass\": 86.4, \"recall_pass\": 98.7, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.36, \"unparseable_count\": 9, \"total_samples\": 9335}}, \"cls8b-s42-ckpt1600-test8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:10:45.814Z\", \"updated_at\": \"2026-05-15T07:25:47.928Z\", \"hypothesis\": \"8B s42 test sweep 最后数据点: ckpt-1600 test@8192。完成 7-point test curve。\", \"parent\": \"repo-level-cls-8b-s42-resume\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --max_seq_length 8192 --batch_size 1 --split test --max_new_tokens 8 --output_dir /root/autodl-tmp/results/cls8b_s42_ckpt1600_test8192\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"339064\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1600-test8192-eval.log\", \"submitted_at\": \"2026-05-15T06:30:12.425Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"test split\", \"data_count\": null, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600\", \"eval_data\": \"test@8192\", \"wall_clock_seconds\": 3328.2, \"gpu_hours\": 0.92}, \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1600-test8192-eval.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T07:25:40.622Z\", \"metrics\": {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_fail\": 67.65, \"f1_pass\": 90.22, \"precision_fail\": 81.06, \"recall_fail\": 58.05, \"precision_pass\": 85.93, \"recall_pass\": 94.97, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.03, \"unparseable_count\": 0, \"total_samples\": 9784}}, \"cls4b-v5-ckpt4600-test-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:49:35.927Z\", \"updated_at\": \"2026-05-15T07:25:44.429Z\", \"hypothesis\": \"4B v5 val-best (ckpt-4600, val=90.07%) 的 test eval。D088 要求 val-best 必须有对应 test 数字。\", \"parent\": \"cls4b-v5-train\", \"spec\": {\"command\": \"python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4600 --model_name Qwen/Qwen3-4B --split test --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/repo_cls_v5_ckpt4600_test\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3238979\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt4600-test-eval.log\", \"submitted_at\": \"2026-05-15T06:49:49.224Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"test split\", \"data_count\": null, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": null, \"checkpoint_source\": \"checkpoints_repo_cls_v5/checkpoint-4600\", \"eval_data\": \"test\", \"wall_clock_seconds\": 2155.2, \"gpu_hours\": 0.6}, \"conclusion\": \"success\", \"log_path\": \"/home/sonny/runs/exec-sim-repair-verifier/cls4b-v5-ckpt4600-test-eval.log\", \"checkpoint_path\": \"checkpoints_repo_cls_v5/checkpoint-4600\", \"metrics\": {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_fail\": 61.67, \"f1_pass\": 89.59, \"precision_fail\": 84.03, \"recall_fail\": 48.72, \"precision_pass\": 83.55, \"recall_pass\": 96.57, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.67, \"unparseable_count\": 0, \"total_samples\": 9784}, \"completed_at\": \"2026-05-15T07:25:44.429Z\"}, \"cls8b-s42-ckpt1400-test8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:10:44.689Z\", \"updated_at\": \"2026-05-15T06:09:21.509Z\", \"hypothesis\": \"D089: s42 ckpt-1400 test@8192。Val+test 双线 sweep，用于论文 supplementary。\", \"parent\": \"repo-level-cls-8b-conda\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --device cuda:0 --max_seq_length 8192 --batch_size 1 --split test --output_dir /root/autodl-tmp/eval_results/cls8b_s42_ckpt1400_test8192 --max_new_tokens 8\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"335070\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1400-test8192-eval.log\", \"submitted_at\": \"2026-05-15T05:32:38.596Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:24:53.684Z\", \"notes\": \"2026-05-15: 首次运行 PID 332736 在 80.8% (7900/9784) 处被误杀，running_acc=85.2%。重新提交中。\", \"metrics\": {\"accuracy\": 85.47, \"f1_macro\": 78.9, \"f1_fail\": 67.13, \"f1_pass\": 90.67, \"precision_fail\": 86.43, \"recall_fail\": 54.88, \"precision_pass\": 85.27, \"recall_pass\": 96.81, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.51, \"unparseable_count\": 0, \"total_samples\": 9784}, \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1400-test8192-eval.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1400\"}, \"cls8b-s42-ckpt1200-test8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:10:43.492Z\", \"updated_at\": \"2026-05-15T05:09:08.608Z\", \"hypothesis\": \"补充 test curve 第五个数据点: 8B CLS s42 ckpt-1200 test@8192。与 ckpt-800 一起构成完整 5-point test curve 用于 supplementary\", \"parent\": \"repo-level-cls-8b-conda\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --max_seq_length 8192 --batch_size 1 --device cuda:0 --output_dir /root/autodl-tmp/results/cls8b_s42_ckpt1200_test8192/\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200\", \"eval_data\": \"test@8192\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_fail\": 65.49, \"f1_pass\": 89.45, \"precision_fail\": 77.52, \"recall_fail\": 56.69, \"precision_pass\": 85.4, \"recall_pass\": 93.91, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.89, \"unparseable_count\": 0, \"total_samples\": 9784}, \"log_path\": \"/tmp/eval_cls8b_ckpt1200_test8192.log\", \"checkpoint_path\": \"/root/autodl-tmp/results/cls8b_s42_ckpt1200_test8192/\", \"completed_at\": \"2026-05-15T05:09:08.608Z\"}, \"cls8b-s42-ckpt800-test8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:21:53.215Z\", \"updated_at\": \"2026-05-15T04:46:22.291Z\", \"hypothesis\": \"补充 test curve 第四个数据点: 8B CLS s42 ckpt-800 test@8192。已有 400(84.79%)/600(79.05%)/1000(83.52%)，补 800 使 curve 更完整\", \"parent\": \"repo-level-cls-8b-conda\", \"spec\": {\"command\": \"python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-800 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split test --max_seq_length 8192 --batch_size 1 --device cuda:0 --output_dir /root/autodl-tmp/eval_results/cls8b_s42_ckpt800_test8192\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-800\", \"eval_data\": \"swebench_test\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl\", \"data_count\": 9784, \"log_path\": \"/tmp/eval_cls8b_ckpt800_test8192.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-800\", \"parent\": \"repo-level-cls-8b-s42-resume\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_fail\": 69.17, \"f1_pass\": 88.77, \"precision_fail\": 70.07, \"recall_fail\": 68.29, \"precision_pass\": 88.36, \"recall_pass\": 89.18, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.58, \"unparseable_count\": 0, \"total_samples\": 9784}, \"completed_at\": \"2026-05-15T04:46:19.522Z\"}, \"cls4b-v5-val-sweep-ckpt4200\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:50:52.861Z\", \"updated_at\": \"2026-05-15T04:41:23.963Z\", \"hypothesis\": \"4B v5 ckpt-4200 val@5120 评估，checkpoint selection sweep 数据点\", \"spec\": {\"command\": \"cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4200 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/repo_cls_v5_ckpt4200_val5120\", \"server\": \"home-1x5090\", \"data_path\": \"data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"checkpoints_repo_cls_v5/checkpoint-4200\", \"eval_data\": \"val@5120\", \"parent\": \"cls4b-v5-train\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_fail\": 73, \"f1_pass\": 93.1, \"precision_fail\": 90.3, \"recall_fail\": 61.3, \"precision_pass\": 88.8, \"recall_pass\": 97.9}, \"log_path\": \"/home/sonny/runs/exec-sim-repair-verifier/cls4b-v5-val-sweep-ckpt4200.log\", \"checkpoint_path\": \"results/repo_cls_v5_ckpt4200_val5120/\", \"completed_at\": \"2026-05-15T04:40:23.852Z\"}, \"cls8b-s42-ckpt1600-val8192-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:47:46.239Z\", \"updated_at\": \"2026-05-15T04:17:07.114Z\", \"hypothesis\": \"8B CLS s42 ckpt-1600 val@8192 评估（v2 修复版），sweep 数据点\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_seq_length 8192 --batch_size 1 --device cuda:0 --output_dir results/repo_cls_8b_s42_ckpt1600_val8192\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:0\", \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"parent\": \"cls8b-s42\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600\", \"eval_data\": \"val\", \"data_path\": \"val split\", \"data_count\": 8192, \"notes\": \"v2 resubmit: v1 failed due to network unreachable (no network_turbo). Fixed by using local model path + OFFLINE flags + network_turbo.\", \"log_path\": \"/tmp/eval_cls8b_ckpt1600_val8192_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1600\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:17:00.749Z\", \"metrics\": {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_fail\": 66.12, \"f1_pass\": 91.76, \"precision_fail\": 86.28, \"precision_pass\": 86.83, \"recall_fail\": 53.6, \"recall_pass\": 97.29, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 10.87, \"unparseable\": 9, \"total\": 9335}}, \"cls8b-s42-ckpt1400-val8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:44:39.102Z\", \"updated_at\": \"2026-05-15T03:38:16.497Z\", \"hypothesis\": \"D088 val pipeline: s42 ckpt-1400 val@8192 (resume 训练产出)。完整 sweep curve 数据点。\", \"parent\": \"repo-level-cls-8b-conda\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1400\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1400-val8192-eval.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T03:35:20.058Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T03:35:22.925701+00:00\"}]}, \"metrics\": {\"accuracy\": 85.97, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 10.09, \"f1_macro\": 77.15, \"f1_fail\": 62.95, \"f1_pass\": 91.34, \"precision_fail\": 86.68, \"precision_pass\": 85.85, \"recall_fail\": 49.42, \"recall_pass\": 97.59, \"n_instances\": 9335, \"n_unparseable\": 9, \"confusion_matrix\": {\"tn\": 1113, \"fp\": 1139, \"fn\": 171, \"tp\": 6912}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T03:38:16.497Z\"}, \"cls4b-v5-val-sweep-ckpt4400-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:08:08.786Z\", \"updated_at\": \"2026-05-15T03:23:04.176Z\", \"hypothesis\": \"v1/v2 因 RTX 5090 间歇性 CUDA hang 卡死（详见 4b_eval_hang_analysis.md）。v3 未修改 watchdog，验证是否为低概率事件。SIGKILL + resume 修复待实施。\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4400 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --batch_size 16 --device cuda:0 --output_dir results/repo_cls_v5_ckpt4400_val5120_v3\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3204975\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-val-sweep-ckpt4400-v3.log\", \"submitted_at\": \"2026-05-15T02:08:34.304Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"checkpoint_source\": \"checkpoints_repo_cls_v5/checkpoint-4400\", \"eval_data\": \"val@5120\", \"data_path\": \"data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 4469.9, \"gpu_hours\": 1.24}, \"reproduce\": {\"finished_at\": \"2026-05-15T03:19:29.874Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T03:19:32.726372+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_fail\": 76.25, \"f1_pass\": 93.64, \"precision_fail\": 88.84, \"precision_pass\": 90.21, \"recall_fail\": 66.79, \"recall_pass\": 97.33, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 14.09, \"n_instances\": 9335, \"n_truncated\": 234, \"n_unparseable\": 0}, \"checkpoint_path\": \"results/repo_cls_v5_ckpt4400_val5120_v3\", \"completed_at\": \"2026-05-15T03:23:04.176Z\"}, \"cls8b-s42-ckpt1200-val8192-eval\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T01:44:38.194Z\", \"updated_at\": \"2026-05-15T02:40:31.850Z\", \"hypothesis\": \"D088 val pipeline: s42 ckpt-1200 val@8192 (resume 训练产出)。完整 sweep curve 数据点。\", \"parent\": \"repo-level-cls-8b-conda\", \"reproduce\": {\"finished_at\": \"2026-05-15T02:09:34.488Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"completed_at\": \"2026-05-15T02:09:38.693Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T02:09:41.436348+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"v1 (PID 315418) OOM，Worker 清理后重提交为 v2 (PID 316307, tmux: ckpt1200-val8192-v2)。18238 MiB VRAM。\"}}, \"notes\": \"失败原因: GPU 调度冲突——重复实验 cls8b-s42-ckpt1200-val8192 (PID 315834) 在 02:06:09 被提交到同一 cuda:0，导致 OOM 连锁反应。本实验 (PID 315418) 正常运行至 640/9335 (running_acc=87.5%) 时被 SIGTERM 杀死。| 已有成果: running_acc=87.5% @640/9335，确认 ckpt-1200 质量正常 | 建议: 在 westd cuda:0 重新提交（现已空闲）\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --max_seq_length 8192 --batch_size 1 --device cuda:0\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"316940\", \"log_path\": \"/tmp/eval_ckpt1200.log\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200\", \"eval_data\": \"val@8192\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200\"}, \"cls8b-s42-ckpt1200-val8192-v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:32:59.322Z\", \"updated_at\": \"2026-05-15T02:40:09.068Z\", \"hypothesis\": \"D089 val sweep: ckpt-1200 val@8192。PID 316940 实际在跑（v1 OOM, v2 GPU冲突, 此条目追踪实际运行进程）。\", \"parent\": \"repo-level-cls-8b-conda\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --max_seq_length 8192 --batch_size 1 --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"316940\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1200-val8192-v2.log\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200\", \"eval_data\": \"val@8192\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"success\", \"log_path\": \"/tmp/eval_ckpt1200.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1200\", \"completed_at\": \"2026-05-15T02:39:58.194Z\", \"metrics\": {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_fail\": 70.2, \"f1_pass\": 92.3, \"precision_fail\": 85, \"recall_fail\": 59.8, \"precision_pass\": 88.3, \"recall_pass\": 96.7, \"majority_baseline\": 75.9, \"gap_vs_majority\": 11.9, \"unparseable\": 9}, \"notes\": \"评估完成 10:39 UTC。PID 316940 在 cuda:0 跑了 ~30 分钟。实际日志: /tmp/eval_ckpt1200.log (非 v2.log)。v2.log 是一个较晚启动的短命进程（10:07-10:10, 仅到 740/9335 就停了）。Accuracy=87.76%, F1_macro=81.25%, 超过 majority baseline 11.9pp。\"}, \"cls8b-s42-ckpt1000-test8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:40:01.711Z\", \"updated_at\": \"2026-05-15T02:09:18.381Z\", \"hypothesis\": \"ckpt-1000 成为新 val-best (88.23% > 85%), 跑 test@8192 获取最终论文数字\", \"parent\": \"repo-level-cls-8b-conda\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split test --max_new_tokens 512 --max_seq_length 8192 --batch_size 1 --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"312975\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1000-test8192-eval.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full\", \"data_count\": 9784, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000\", \"eval_data\": \"swebench test split\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000\"}, \"notes\": \"2026-05-15 09:46 UTC: eval 运行中，PID 312981 on cuda:0 (17.4GB VRAM)。进度 2700/9784 (27.6%), running_acc=82.7%。速度 ~0.13s/sample，预计 ~15min 后完成（~10:01 UTC）。命令确认含 --max_new_tokens 512 --max_seq_length 8192。\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 83.52, \"f1_macro\": 77.5, \"f1_fail\": 65.85, \"f1_pass\": 89.14, \"precision_fail\": 74.93, \"recall_fail\": 58.73, \"precision_pass\": 85.84, \"recall_pass\": 92.72, \"majority_baseline\": 72.96, \"gap_vs_majority\": 10.56, \"unparseable_count\": 0, \"unparseable_rate\": 0, \"total_samples\": 9784, \"tp\": 6618, \"fp\": 1092, \"fn\": 520, \"tn\": 1554}, \"completed_at\": \"2026-05-15T02:05:02.421Z\"}, \"cls8b-s42-ckpt1000-val8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:03:36.750Z\", \"updated_at\": \"2026-05-15T01:39:37.277Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --max_seq_length 8192 --batch_size 1 --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"310114\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1000-val8192-eval.log\", \"submitted_at\": \"2026-05-15T01:03:36.501Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full\", \"data_count\": 9335, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000\", \"eval_data\": \"swebench val split\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-1000\", \"wall_clock_seconds\": 2045.2, \"gpu_hours\": 0.57}, \"hypothesis\": \"D088 val pipeline: s42 ckpt-1000 val@8192 (resume 训练产出)。如 > 85.00% 需补跑 test@8192\", \"parent\": \"repo-level-cls-8b-conda\", \"reproduce\": {\"finished_at\": \"2026-05-15T01:33:47.289Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T01:33:49.926975+00:00\"}]}, \"metrics\": {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_fail\": 73, \"f1_pass\": 92.5, \"precision_fail\": 81.8, \"recall_fail\": 65.8, \"precision_pass\": 89.8, \"recall_pass\": 95.3, \"unparseable\": 9, \"total_instances\": 9335}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:37:41.694Z\"}, \"cls8b-s42-ckpt800-val8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:40:21.590Z\", \"updated_at\": \"2026-05-15T01:07:58.963Z\", \"spec\": {\"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt800-val8192-eval.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-800\"}, \"hypothesis\": \"D088 val pipeline: s42 ckpt-800 val@8192 (resume 训练产出)。如 > 85.00% (当前 val-best) 需补跑 test@8192\", \"parent\": \"repo-level-cls-8b-conda\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 84.5, \"f1_macro\": 79.2}, \"completed_at\": \"2026-05-15T01:07:58.963Z\"}, \"cls4b-v5-ckpt4000-val5120-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:43:18.289Z\", \"updated_at\": \"2026-05-15T01:03:10.774Z\", \"spec\": {\"command\": \"python3 eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-4000 --model_name Qwen/Qwen3-4B --split val --max_new_tokens 512 --max_seq_length 5120 --batch_size 16 --device cuda:0\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3186818\", \"account\": \"sonny\", \"data_path\": \"val split\", \"data_count\": 9335, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"checkpoints_repo_cls_v5/checkpoint-4000\", \"eval_data\": \"val@5120 9335 samples\", \"checkpoint_path\": \"checkpoints_repo_cls_v5/checkpoint-4000\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt4000-val5120-eval.log\"}, \"hypothesis\": \"4B v5 ckpt-4000 val@5120 eval (supplementary data, D088)\", \"parent\": \"repo-level-cls-v5\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_fail\": 74.85, \"f1_pass\": 93.64, \"precision_fail\": 92.95, \"recall_fail\": 62.66, \"precision_pass\": 89.24, \"recall_pass\": 98.49, \"unparseable\": 0, \"truncated\": 234, \"total\": 9335}, \"completed_at\": \"2026-05-15T00:50:30.859Z\"}, \"cls4b-v5-ckpt600-val5120-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:39:23.063Z\", \"updated_at\": \"2026-05-14T23:47:43.530Z\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_v5/checkpoint-600 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --device cuda:0\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3179262\", \"account\": \"sonny\", \"data_path\": \"val split\", \"data_count\": 9335, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"checkpoints_repo_cls_v5/checkpoint-600\", \"eval_data\": \"val@5120 9335 samples\", \"checkpoint_path\": \"checkpoints_repo_cls_v5/checkpoint-600\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls4b-v5-ckpt600-val5120-eval.log\"}, \"hypothesis\": \"Evaluate repo-level classification v5 checkpoint-600 on val split with max_seq_length=5120\", \"metrics\": {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_fail\": 72.03, \"f1_pass\": 87.6, \"precision_fail\": 59.3, \"recall_fail\": 91.7, \"unparseable\": 0, \"total\": 9335}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:47:04.584Z\"}, \"repo-level-cls-8b-conda\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:07:02.272Z\", \"updated_at\": \"2026-05-14T22:38:53.233Z\", \"hypothesis\": \"Qwen3-8B CLS repo-level conda 环境重训（transformers 4.57.6），消除跨环境混杂，验证 8B CLS repo 表现\", \"spec\": {\"hypothesis\": \"CLS 8B conda 重训 (transformers 4.57.6)，与 CLS v5 (4B) 同环境对比，验证 repo-level scaling effect。之前 8B 在 transformers 5.8.0 训练结果无效 (71.37%)。\", \"server\": \"westd-48478\", \"gpu\": \"cuda:3\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=3 python3 train_repo_verifier.py --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --device cuda:0 --batch_size 1 --grad_accumulation 32 --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/ --run_name repo-cls-qwen3-8b-conda\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_steps\": 200, \"eval_steps\": 200, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 1, \"grad_accumulation\": 32, \"max_seq_length\": 2048, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/\", \"log_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/train.log\", \"env\": \"conda base, transformers 4.57.6\", \"pid\": 185438, \"account\": \"root\", \"total_steps\": 6633, \"speed\": \"~8.3s/step\", \"estimated_hours\": 15.3, \"gpu_mem_used\": \"25751/32607 MiB\", \"tmux_session\": \"cls8b-conda\"}, \"notes\": \"Checkpoint sweep 完成 (ckpt 200/400/600)。最优 ckpt-400: accuracy=84.52% (+11.56pp vs baseline), f1_macro=80.89。ckpt-600 过拟合退化至 78.51%。8B (84.52%) vs 4B best (80.73% seed123 ckpt-600) = +3.79pp scaling gain，与函数级趋势一致（8B CLS-4B CLS gap ~2pp）。Repo-level 8B scaling 比函数级更明显。\", \"reproduce\": {\"finished_at\": \"2026-05-14T01:06:38.490Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T01:06:39.345Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T01:06:40.925438+00:00\"}]}, \"metrics\": {\"val_8192\": {\"ckpt_200\": {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_fail\": 51.6, \"f1_pass\": 70.7, \"unparseable\": 9}, \"ckpt_400\": {\"accuracy\": 80.96}, \"ckpt_600\": {\"accuracy\": 85}, \"best_acc\": \"ckpt_600\"}, \"val_5120\": {\"ckpt_400\": {\"accuracy\": 80.47, \"f1_macro\": 75.84}}, \"test_2048\": {\"ckpt_400\": {\"accuracy\": 84.52, \"f1_macro\": 80.89}, \"ckpt_600\": {\"accuracy\": 78.51}}, \"test_8192\": {\"ckpt_400\": {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_fail\": 72.93, \"f1_pass\": 89.43, \"unparseable\": 0, \"total\": 9784}, \"ckpt_600\": {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_fail\": 65.24, \"f1_pass\": 85, \"unparseable\": 0, \"total\": 9784}}}}, \"cls8b-s42-ckpt200-val8192-eval-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:06:17.105Z\", \"updated_at\": \"2026-05-14T22:38:47.098Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --max_seq_length 8192 --batch_size 1 --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"297542\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt200-val8192-eval-v2.log\", \"submitted_at\": \"2026-05-14T22:06:16.784Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200\", \"eval_data\": \"val set 9335 samples\", \"data_count\": 9335, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"data_path\": \"val set\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-200\", \"wall_clock_seconds\": 1950.3, \"gpu_hours\": 0.54}, \"hypothesis\": \"D063 val sweep: 8B CLS s42 ckpt-200 val@8192，补全 val sweep 数据（之前 PID 死了标记 failed）\", \"parent\": \"repo-level-cls-8b-conda\", \"reproduce\": {\"finished_at\": \"2026-05-14T22:36:26.677Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:36:29.208613+00:00\"}]}, \"metrics\": {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_fail\": 51.6, \"f1_pass\": 70.7, \"unparseable\": 9, \"total\": 9335}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T22:38:47.099Z\"}, \"cls4b-seed123-ckpt800-val5120-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:23:23.578Z\", \"updated_at\": \"2026-05-14T22:29:34.755Z\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_seed123_home/checkpoint-800 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --device cuda:0\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"3172988\", \"account\": \"sonny\", \"data_path\": \"data/swebench_full/swebench_val.jsonl\", \"data_count\": 9335, \"model_name\": \"Qwen3-4B\", \"seed\": 123, \"checkpoint_source\": \"checkpoints_repo_cls_seed123_home/checkpoint-800\", \"eval_data\": \"val split 9335 samples\", \"checkpoint_path\": \"checkpoints_repo_cls_seed123_home/checkpoint-800\", \"log_path\": \"~/runs/cls4b-seed123-ckpt800-val5120-eval.log\"}, \"hypothesis\": \"D063 val@5120: 4B CLS seed123 ckpt-800 在 val set 上评估\", \"parent\": \"repo-level-cls-seed123-home\", \"notes\": \"诊断结果：PID 3172988 于 14:13 PDT 启动，dtype=bf16（正确），batch_size=16（默认），速率 ~7500 样本/小时，预计 ~15:28 PDT 完成。VRAM 31.7/32.6GB 偏高但未影响性能。无需修复。\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 87.92, \"f1_macro\": 81.95, \"f1_pass\": 92.33, \"f1_fail\": 71.57, \"unparseable\": 0, \"truncated\": 234, \"total\": 9335}, \"completed_at\": \"2026-05-14T22:29:34.755Z\"}, \"repo-level-cls-seed123-home\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T21:30:50.413Z\", \"updated_at\": \"2026-05-14T22:27:09.307Z\", \"spec\": {\"command\": \"python3 train_repo_verifier.py --seed 123 --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_seed123_home/ --no_wandb\", \"server\": \"home-1x5090\", \"gpu\": \"cuda:0\", \"pid\": 2998850, \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-seed123-home.log\", \"submitted_at\": \"2026-05-13T21:30:50.261Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 123, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_steps\": 200, \"eval_steps\": 200, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 2, \"grad_accumulation\": 16, \"max_seq_length\": 2048, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_seed123_home/\", \"wall_clock_seconds\": 13620.5, \"gpu_hours\": 3.78}, \"hypothesis\": \"D053: CLS seed123 在 home 重跑（与 v5 同环境：transformers 4.57.6 + 相同数据）。验证 repo-level CLS multi-seed robustness，与 CWM seed123 配对。原 westd 训练因环境差异 (transformers 5.8.0) 无效。\", \"notes\": \"Val@5120 sweep 完成 (ckpt-400/600/800)。⚠️ 重大发现：val@5120 best=ckpt-800 (87.92% acc, F1m 81.95)，但 test@2048 best=ckpt-600 (80.73%)。ckpt-800 在 test 上退化至 74.27%，val 上却是最佳。与 val@2048 趋势一致（later ckpts val 更好）。Val-test distribution shift 显著——选 checkpoint 不能只看 val。Sweep script 继续跑 v5 (seed42) checkpoints。\", \"reproduce\": {\"finished_at\": \"2026-05-14T01:17:48.834Z\"}, \"failure_reason\": \"D056 early stop — 训练正常但 best checkpoint 已在 step 200，Director 指令提前终止训练并启动 eval\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T01:17:50.747Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T01:17:52.342754+00:00\"}]}, \"metrics\": {\"val_2048\": {\"n\": 9335, \"unparseable\": 1883, \"ckpt_200\": {\"accuracy\": 62.51, \"f1_macro\": 55.54, \"f1_pass\": 73.14, \"f1_fail\": 37.94}, \"ckpt_400\": {\"accuracy\": 80.72, \"f1_macro\": 67.03, \"f1_pass\": 88.27, \"f1_fail\": 45.78}, \"ckpt_600\": {\"accuracy\": 76.78, \"f1_macro\": 66.81, \"f1_pass\": 85, \"f1_fail\": 48.63}, \"ckpt_800\": {\"accuracy\": 81.81, \"f1_macro\": 69.14, \"f1_pass\": 88.91, \"f1_fail\": 49.37}, \"ckpt_1000\": {\"accuracy\": 82.3, \"f1_macro\": 67.63, \"f1_pass\": 89.42, \"f1_fail\": 45.84}, \"best_f1\": \"ckpt_800\", \"best_acc\": \"ckpt_1000\"}, \"val_4096\": {\"n\": 9335, \"unparseable\": 1406, \"ckpt_400\": {\"accuracy\": 82.57, \"f1_macro\": 71.24, \"f1_pass\": 89.29, \"f1_fail\": 53.18}, \"ckpt_600\": {\"accuracy\": 79.18, \"f1_macro\": 70.73, \"f1_pass\": 86.45, \"f1_fail\": 55}, \"ckpt_800\": {\"accuracy\": 83.7, \"f1_macro\": 73.31, \"f1_pass\": 90, \"f1_fail\": 56.7}, \"best_f1\": \"ckpt_800\", \"best_acc\": \"ckpt_800\"}, \"val_5120\": {\"n\": 9335, \"unparseable\": 0, \"truncated\": 234, \"ckpt_400\": {\"accuracy\": 86.01, \"f1_macro\": 79.66, \"f1_pass\": 91.02, \"f1_fail\": 68.3}, \"ckpt_600\": {\"accuracy\": 81.89, \"f1_macro\": 77.01, \"f1_pass\": 87.6, \"f1_fail\": 66.43}, \"ckpt_800\": {\"accuracy\": 87.92, \"f1_macro\": 81.95, \"f1_pass\": 92.33, \"f1_fail\": 71.57}, \"best_f1\": \"ckpt_800\", \"best_acc\": \"ckpt_800\"}}}, \"cls8b-s42-ckpt600-test8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:40:33.560Z\", \"updated_at\": \"2026-05-14T22:05:28.408Z\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-600 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split test --max_seq_length 8192 --batch_size 1 --device cuda:0\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"294732\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt600-test8192-eval.log\", \"submitted_at\": \"2026-05-14T21:40:33.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-600\", \"eval_data\": \"test set 9784 samples\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"data_path\": \"test set\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-600\"}, \"hypothesis\": \"CRITICAL D063: 8B CLS s42 ckpt-600 test@8192，消除 max_seq_length 混杂变量，与 ckpt-400 test@8192 比较\", \"parent\": \"repo-level-cls-8b-conda\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_fail\": 65.24, \"f1_pass\": 85, \"precision_fail\": 59.16, \"precision_pass\": 88.95, \"recall_fail\": 72.71, \"recall_pass\": 81.4, \"unparseable\": 0, \"total\": 9784, \"majority_baseline\": 73, \"gap_vs_majority_pp\": 6.09}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-600\", \"completed_at\": \"2026-05-14T22:05:27.478Z\"}, \"cls8b-seed123-ckpt3000-val8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:11:09.823Z\", \"updated_at\": \"2026-05-14T21:41:38.471Z\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split val --max_new_tokens 512 --max_seq_length 8192 --device cuda:0\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"291117\", \"log_path\": \"/root/runs/cls8b-seed123-ckpt3000-val8192-eval.log\", \"submitted_at\": \"2026-05-14T21:11:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"val split\", \"data_count\": 9335, \"model_name\": \"Qwen3-8B + CLS LoRA seed123\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000\", \"eval_data\": \"val split 9335 samples\", \"max_seq_length\": 8192, \"wall_clock_seconds\": 1838.5, \"gpu_hours\": 0.51}, \"hypothesis\": \"D063 val@8192 checkpoint selection: 8B CLS seed123 ckpt-3000 在 val set (9335 samples) 上评估。修复缺失 max_seq_length 问题。\", \"parent\": \"repo-level-cls-8b-seed123-conda\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000\", \"log_path\": \"/root/runs/cls8b-seed123-ckpt3000-val8192-eval.log\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_fail\": 70.5, \"f1_pass\": 93, \"precision_fail\": 95.2, \"precision_pass\": 87.6, \"recall_fail\": 55.9, \"recall_pass\": 99.1, \"majority_baseline\": 75.9, \"gap_vs_majority_pp\": 12.8, \"unparseable\": 9, \"total\": 9335}, \"completed_at\": \"2026-05-14T21:41:38.471Z\"}, \"cls8b-s42-ckpt400-test8192-eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:18:24.242Z\", \"updated_at\": \"2026-05-14T21:40:54.735Z\", \"hypothesis\": \"8B CLS s42 ckpt-400 test@8192 评估，消除 max_seq_length 混杂变量\", \"spec\": {\"command\": \"python eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-400 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --split test --max_seq_length 8192 --max_new_tokens 512 --batch_size 1 --device cuda:0\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"291891\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt400-test8192-eval.log\", \"submitted_at\": \"2026-05-14T21:18:23.942Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier\", \"data_count\": 9784, \"model_name\": \"Qwen3-8B + CLS LoRA s42\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-400\", \"eval_data\": \"test split\", \"hypothesis\": \"CRITICAL D063: 8B CLS s42 ckpt-400 test@8192, eliminate max_seq_length confound\", \"max_seq_length\": 8192, \"parent\": \"repo-level-cls-8b-conda\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-400\", \"result_accuracy\": 84.79, \"result_f1_macro\": 81.18, \"result_f1_fail\": 72.93, \"result_f1_pass\": 89.43, \"wall_clock_seconds\": 1325.2, \"gpu_hours\": 0.37}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T21:40:29.170Z\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-400\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt400-test8192-eval.log\", \"metrics\": {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_fail\": 72.93, \"f1_pass\": 89.43, \"precision_fail\": 70.32, \"precision_pass\": 90.74, \"recall_fail\": 75.74, \"recall_pass\": 88.15, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 11.84, \"unparseable\": 0, \"total\": 9784}}, \"repo-level-cls-v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T07:42:07.962Z\", \"updated_at\": \"2026-05-14T14:52:33.985Z\", \"hypothesis\": \"D046 超参修正：lr 5e-5（原 2e-4）, weight_decay 0.01, warmup_ratio 0.05。修复 v4 warmup 阶段 checkpoint + LR 过高问题。验证 repo-level CLS verifier 在正确超参下的性能。\", \"spec\": {\"command\": \"python3 train_repo_verifier.py --output_dir checkpoints_repo_cls_v5/ --seed 42 --run_name repo-cls-qwen3-4b-lora-v5\", \"server\": \"home-1x5090\", \"gpu\": \"cuda:0\", \"pid\": 2947259, \"log_path\": \"~/runs/exec-sim-repair-verifier/repo-level-cls-v5.log\", \"submitted_at\": \"2026-05-13T07:42:26.431Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_steps\": 200, \"eval_steps\": 200, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 2, \"grad_accumulation\": 16, \"max_seq_length\": 2048, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/\", \"wall_clock_seconds\": 49682.4, \"gpu_hours\": 13.8}, \"notes\": \"Eval on checkpoint-600 (best eval_loss=0.0642) done on westd cuda:2. Accuracy 76.92% (+3.97pp vs majority baseline 72.96%, +10.81pp vs v4 66.11%). Fail F1 65.01 (+28.71pp vs v4 36.3). 训练仍在继续（step ~2000/6633）但 best checkpoint 不太可能改善。\", \"metrics\": {\"checkpoint_sweep\": {\"ckpt_600\": {\"accuracy\": 76.74, \"f1_macro\": 73.74, \"fail_f1\": 64.88, \"pass_f1\": 82.61}, \"ckpt_4000\": {\"accuracy\": 81.51, \"f1_macro\": 72.56, \"fail_f1\": 56.9, \"pass_f1\": 88.23}, \"ckpt_4200\": {\"accuracy\": 80.64, \"f1_macro\": 72.1, \"fail_f1\": 56.66, \"pass_f1\": 87.54}, \"ckpt_4400\": {\"accuracy\": 82.11, \"f1_macro\": 73.94, \"fail_f1\": 59.34, \"fail_precision\": 77.02, \"fail_recall\": 48.26}, \"ckpt_4600\": {\"accuracy\": 82.35, \"f1_macro\": 74.74, \"fail_f1\": 60.87, \"pass_f1\": 88.6, \"fail_precision\": 76, \"fail_recall\": 50.76}}, \"best_checkpoint_accuracy\": \"checkpoint-4600\", \"best_checkpoint_f1\": \"checkpoint-4600\", \"eval_samples\": 9784, \"accuracy\": 82.35, \"f1_macro\": 74.74, \"unparseable\": 132, \"unparseable_pct\": 1.3, \"majority_baseline\": 72.96, \"gap_vs_baseline\": 9.39, \"eval_server\": \"home-1x5090\", \"eval_env\": \"transformers 4.57.6\", \"note\": \"Test set sweep complete. ckpt-4600 best on both accuracy (82.35%) and f1_macro (74.74%).\", \"val_2048\": {\"ckpt_600\": {\"accuracy\": 77.25, \"f1_macro\": 70.81, \"fail_f1\": 57.11, \"pass_f1\": 84.52}, \"ckpt_4000\": {\"accuracy\": 83.32, \"f1_macro\": 70.26, \"fail_f1\": 50.56, \"pass_f1\": 89.97}, \"ckpt_4200\": {\"accuracy\": 82.82, \"f1_macro\": 69.54, \"fail_f1\": 49.43, \"pass_f1\": 89.65}, \"ckpt_4400\": {\"accuracy\": 83.49, \"f1_macro\": 71.63, \"fail_f1\": 53.29, \"pass_f1\": 89.97}, \"ckpt_4600\": {\"accuracy\": 83.63, \"f1_macro\": 71.72, \"fail_f1\": 53.36, \"pass_f1\": 90.07}, \"eval_samples\": 9335, \"unparseable\": 1883, \"unparseable_pct\": 20.2, \"val_best_f1\": \"ckpt-4600\", \"val_best_acc\": \"ckpt-4600\", \"note\": \"val-test 一致: 都是 ckpt-4600\"}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T21:30:28.798Z\"}, \"repo-level-cls-v5-conda\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:55:01.260Z\", \"updated_at\": \"2026-05-14T05:24:22.630Z\", \"hypothesis\": \"CLS v5 conda 环境重训（同 CWM v12 环境），消除 transformers 版本差异，建立公平 CLS-CWM 对比基线\", \"spec\": {\"hypothesis\": \"CLS seed42 conda 重训 (westd, transformers 4.57.6)，与 CWM v12 同服务器+同环境 apple-to-apple 对比。消除 CLS v5 (home) vs CWM v12 (westd) 的跨服务器差异。\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python3 train_repo_verifier.py --seed 42 --no_wandb --output_dir /root/autodl-tmp/checkpoints_repo_cls_v5_conda/\", \"server\": \"westd-48478\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"learning_rate\": 5e-05, \"weight_decay\": 0.01, \"warmup_ratio\": 0.05, \"save_steps\": 200, \"eval_steps\": 200, \"save_total_limit\": 5, \"num_train_epochs\": 3, \"lora_rank\": 16, \"lora_alpha\": 32, \"batch_size\": 2, \"grad_accumulation\": 16, \"max_seq_length\": 2048, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cls_v5_conda/\", \"log_path\": \"/root/autodl-tmp/checkpoints_repo_cls_v5_conda/train.log\", \"env\": \"conda base, transformers 4.57.6\", \"tmux_session\": \"cls-v5-conda\", \"gpu\": \"cuda:2\"}, \"notes\": \"Checkpoint sweep 完成 (ckpt 200/400/600)。ckpt-200=52.96% (极差), ckpt-400=78.43% (accuracy 最高, pass-biased), ckpt-600=76.37% (f1_macro 最高=71.17, 更均衡)。与 home CLS v5 ckpt-600 (76.92%) 仅差 0.55pp，确认 home vs westd conda 环境差异可忽略。checkpoint 选择才是主因。D056 early stop 导致只看了 ckpt-200 险些误判。\", \"conclusion\": \"success\", \"metrics\": {\"checkpoint_sweep\": {\"ckpt_200\": {\"accuracy\": 52.96, \"f1_macro\": 52.89, \"fail_f1\": 51.02, \"pass_f1\": 54.76}, \"ckpt_400\": {\"accuracy\": 78.43, \"f1_macro\": 68.41, \"fail_f1\": 50.61, \"pass_f1\": 86.21, \"fail_precision\": 66.48, \"fail_recall\": 40.85, \"pass_precision\": 80.82, \"pass_recall\": 92.36}, \"ckpt_600\": {\"accuracy\": 76.37, \"f1_macro\": 71.17, \"fail_f1\": 58.93, \"pass_f1\": 83.41, \"fail_precision\": 55.6, \"fail_recall\": 62.7, \"pass_precision\": 85.49, \"pass_recall\": 81.44}}, \"best_checkpoint_accuracy\": \"checkpoint-400\", \"best_checkpoint_f1\": \"checkpoint-600\", \"eval_samples\": 9784, \"accuracy\": 78.43, \"f1_macro\": 71.17, \"unparseable\": 132, \"unparseable_pct\": 1.35, \"majority_baseline\": 72.96, \"eval_server\": \"westd-48478\", \"eval_env\": \"conda, transformers 4.57.6\"}, \"completed_at\": \"2026-05-14T05:21:01.269Z\"}, \"repo-level-cwm-v10\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T23:28:57.911Z\", \"updated_at\": \"2026-05-13T08:20:00.891Z\", \"hypothesis\": \"CWM v10: 诊断 v9 EXIT_CODE=2 语法错误后修复重提交。seetacloud cuda:2。验证 repo-level complexity-dependent CWM 训练（C1 claim 必备对照组）。\", \"spec\": {\"command\": \"python3 train_repo_cwm.py --output_dir /root/autodl-tmp/checkpoints_repo_cwm_v9/ --resume_from_checkpoint /root/autodl-tmp/checkpoints_repo_cwm_v9/checkpoint-200 --no_wandb --save_steps 100 --eval_steps 100\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:2\", \"pid\": 105205, \"data_path\": \"/root/autodl-tmp/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/cwm_v9_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints_repo_cwm_v9/\", \"resume_from\": \"checkpoint-200\", \"eval_steps\": 100, \"save_steps\": 100}, \"notes\": \"D045 early stop. Eval on checkpoint-400: accuracy=69.91% (below majority 72.96%), but 93% unparseable due to max_new_tokens=64 (D047). Eval results invalid — CWM repo-level outputs exceed 64 tokens. F1_macro=46.71%, F1_fail=11.54%. Predictions: /root/autodl-tmp/results/repo_cwm_v10_eval/eval_repo_cwm_predictions.jsonl (9784 lines).\", \"reproduce\": {\"finished_at\": \"2026-05-13T06:25:35.849Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T06:25:37.043Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T06:25:38.583232+00:00\"}]}, \"metrics\": {\"accuracy\": 0.6991, \"f1_macro\": 0.4671, \"f1_pass\": 0.8187, \"f1_fail\": 0.1154, \"precision_pass\": 0.7304, \"recall_pass\": 0.9314, \"precision_fail\": 0.2815, \"recall_fail\": 0.0726, \"majority_baseline\": 0.7296, \"n_unparseable\": 9102, \"n_unparseable_pct\": 0.93, \"n_truncated\": 478, \"n_truncated_pct\": 0.0489, \"truncated_accuracy\": 0.2176, \"best_checkpoint\": \"checkpoint-400\", \"early_stop\": \"D045\", \"eval_invalid\": \"max_new_tokens=64 caused 93% unparseable (D047)\"}}, \"repo-level-cls-v4\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-12T17:17:08.066Z\", \"updated_at\": \"2026-05-13T07:01:27.247Z\", \"hypothesis\": \"CLS v4: 基于 v3 代码（DataCollator 已修复），home-1x5090 重提交。磁盘已修复（89%→64%）。save_steps=200, eval_steps=200。验证 repo-level complexity-dependent CLS advantage (C1 claim)。\", \"notes\": \"D045 early stop at step 2600/6633. Best checkpoint = step-200 (eval_loss=0.0701). Eval on checkpoint-200: accuracy=66.11% (below majority 72.96%), F1_macro=56.61%, F1_pass=76.9%, F1_fail=36.3%, 132 unparseable. Predictions: /home/sonny/exec-sim-repair-verifier/results/repo_cls_v4_eval/eval_repo_cls_predictions.jsonl\", \"completed_at\": \"2026-05-12T19:00:01.551Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\", \"notes\": \"已被 repo-level-cls-home 替代（同实验，转至 home-1x5090 执行）。seetacloud 并行限制导致无法在该服务器提交。\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T06:32:57.144063+00:00\"}]}, \"spec\": {\"command\": \"nohup python3 train_repo_verifier.py --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/ --no_wandb\", \"server\": \"home-1x5090\", \"gpu\": \"cuda:0\", \"pid\": 2885139, \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/swebench_full/\", \"data_count\": 70748, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"save_strategy\": \"steps\", \"save_steps\": 200, \"eval_strategy\": \"steps\", \"eval_steps\": 200, \"save_total_limit\": 3, \"load_best_model_at_end\": true, \"log_path\": \"/tmp/repo-level-cls-v3_stdout.log\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T06:32:54.657Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6611, \"f1_macro\": 0.5661, \"f1_pass\": 0.769, \"f1_fail\": 0.363, \"precision_pass\": 0.765, \"recall_pass\": 0.774, \"precision_fail\": 0.369, \"recall_fail\": 0.357, \"majority_baseline\": 0.7296, \"n_unparseable\": 132, \"best_checkpoint\": \"checkpoint-200\", \"early_stop\": \"D045\"}}, \"cwm8b-seed123\": {\"status\": \"DONE\", \"parent\": \"model-size-scaling-cwm8b\", \"retry_count\": 0, \"created_at\": \"2026-05-12T09:23:40.894Z\", \"updated_at\": \"2026-05-12T19:04:22.633Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output_dir checkpoints_cwm8b_seed123/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 123 --no_wandb && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm8b_seed123/best --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output eval_cwm8b_seed123.json\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"22516\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm8b-seed123.log\", \"submitted_at\": \"2026-05-12T09:23:51.749Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm8b_seed123/best/\", \"wall_clock_seconds\": 5947.9, \"gpu_hours\": 1.65}, \"hypothesis\": \"验证 8B CWM 87.67% accuracy 在不同 seed 下稳定，确认 cls vs cwm 2.81pp gap 的可复现性\", \"reproduce\": {\"finished_at\": \"2026-05-12T10:59:44.440Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T10:59:46.008298+00:00\"}]}, \"metrics\": {\"overall_accuracy\": 86.98, \"pass_f1\": 86.83, \"fail_f1\": 87.13, \"pass_precision\": 91.12, \"pass_recall\": 82.92, \"fail_precision\": 83.3, \"fail_recall\": 91.34, \"exact_match_rate\": 84.13, \"unparseable\": 0, \"test_set_size\": 1890}, \"conclusion\": \"success\", \"notes\": \"8B CWM seed123: accuracy=86.98%, pass_f1=86.83%, fail_f1=87.13%, exact_match=84.13%。与 seed42 (87.67%) 相比下降 0.69pp。8B cls-cwm gap: seed42=2.81pp, seed123=3.50pp (90.48-86.98)。Classification 优势在两个 seed 下均稳定。\", \"completed_at\": \"2026-05-12T11:02:59.646Z\"}, \"cls8b-seed123\": {\"status\": \"DONE\", \"parent\": \"model-size-scaling-cls8b\", \"retry_count\": 1, \"created_at\": \"2026-05-12T09:23:37.452Z\", \"updated_at\": \"2026-05-12T19:04:21.268Z\", \"hypothesis\": \"验证 8B classification 90.48% accuracy 在不同 seed 下稳定，确认 cls vs cwm 2.81pp gap 的可复现性\", \"reproduce\": {\"finished_at\": \"2026-05-12T11:04:29.187Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 596.00 MiB. GPU 0 has a total capacity of 31.36 GiB of which 297.69 MiB is free. Process 21715 has 13.57 GiB memory in use. Including non-PyTorch memory, this process has 17.49 GiB memory in use. Of the allocated\", \"completed_at\": \"2026-05-12T09:26:17.270Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-12T09:26:18.332729+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T11:04:31.005638+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"notes\": \"8B cls seed123 完成。accuracy=89.4% (vs seed42=90.48%, 差距 1.08pp 在正常波动范围内)。8B cls-cwm gap: seed42=2.81pp (90.48-87.67), seed123=2.42pp (89.4-86.98)。两个 seed 均显示 classification 在 8B 上显著优于 CWM，gap ~2.4-2.8pp 稳定。对比 4B gap ~0.9pp，8B 放大了 cls 的优势，支撑 Pillar 1 (complexity hypothesis)。OOM 后使用 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True 重试成功。\", \"spec\": {\"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b_seed123/best/\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed123.log\"}, \"metrics\": {\"overall_accuracy\": 89.4, \"pass_f1\": 89.5, \"fail_f1\": 89.2, \"pass_precision\": 91.2, \"pass_recall\": 87.9, \"fail_precision\": 87.5, \"fail_recall\": 90.9, \"train_loss\": 0.3087, \"eval_loss\": 0.0848, \"train_runtime_sec\": 5666, \"unparseable\": 0}, \"conclusion\": \"success\"}, \"cls8b-eval-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T17:21:33.209Z\", \"updated_at\": \"2026-05-12T19:04:18.835Z\", \"hypothesis\": \"生成 8B CLS seed123 的 per-instance prediction JSON，用于 matched-seed error overlap 分析和论文数据支撑\", \"spec\": {\"command\": \"python eval_verifier.py --data_dir data --checkpoint_dir checkpoints_cls8b_seed123/best --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output eval_results/cls8b_seed123_results.json --save_predictions\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 123, \"checkpoint_source\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b_seed123/best/\", \"eval_data\": \"test.jsonl\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b_seed123/best/\", \"log_path\": \"/tmp/eval_cls8b_seed123.log\", \"parent\": \"cls8b-seed123\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T17:26:38.679Z\", \"output_path\": \"/home/sonny/exec-sim-repair-verifier/eval_results/cls8b_seed123_predictions.json\", \"metrics\": {\"overall_accuracy\": 89.37, \"pass_f1\": 89.54, \"fail_f1\": 89.19, \"pass_precision\": 91.2, \"pass_recall\": 87.93, \"fail_precision\": 87.54, \"fail_recall\": 90.9, \"unparseable\": 0, \"test_set_size\": 1890}}, \"cls8b-eval-seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T17:21:32.288Z\", \"updated_at\": \"2026-05-12T19:04:17.529Z\", \"hypothesis\": \"生成 8B CLS seed42 的 per-instance prediction JSON，用于 matched-seed error overlap 分析和论文数据支撑\", \"spec\": {\"command\": \"python eval_verifier.py --data_dir data --checkpoint_dir checkpoints_cls8b/best/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output eval_results/cls8b_seed42.json --save_predictions\", \"server\": \"seetacloud-westd-4x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b/best/\", \"eval_data\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"parent\": \"cls8b-seed42\"}, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b/best/\", \"log_path\": \"/tmp/eval_cls8b_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T17:25:15.288Z\", \"metrics\": {\"overall_accuracy\": 90.48, \"pass_f1\": 90.86, \"fail_f1\": 90.06, \"pass_precision\": 90.22, \"pass_recall\": 91.51, \"fail_precision\": 90.76, \"fail_recall\": 89.36, \"unparseable\": 0, \"test_set_size\": 1890}}, \"matched-seed-8b-predictions\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T17:21:33.762Z\", \"updated_at\": \"2026-05-12T17:46:21.454Z\", \"hypothesis\": \"在 home 服务器生成 matched-seed per-instance predictions（8B CWM eval JSONs 或 4B 补充分析），为 error overlap / oracle 分析提供数据\", \"notes\": \"Worker 完成。4B CWM per-instance predictions 已生成: seed0 (87.57%), seed42 (已有), seed456 (86.98%). 可用 matched CLS-CWM pairs: seed0/seed42/seed456 (3对). 缺失: CWM seed123/789 (checkpoints only on seetacloud), 8B preds (checkpoints分散+GPU占用). 3 pairs 足够做 error overlap 分析。\", \"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"n/a (eval-only task)\", \"log_path\": \"n/a (worker task)\"}, \"completed_at\": \"2026-05-12T17:46:21.454Z\"}, \"cwm-seed789\": {\"status\": \"DONE\", \"parent\": \"cwm-baseline\", \"retry_count\": 0, \"created_at\": \"2026-05-12T12:31:34.311Z\", \"updated_at\": \"2026-05-12T16:13:15.185Z\", \"hypothesis\": \"补充 4B CWM seed=789，凑齐 CWM 5-seed 对比（42, 123, 456, 789, 0），与 5-seed CLS 做 paired 统计检验\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B --output_dir checkpoints_cwm_seed789/ --seed 789 --no_wandb && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm_seed789/best --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B --output eval_cwm_seed789.json\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": 42227, \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-seed789.log\", \"submitted_at\": \"2026-05-12T12:34:07.017Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 789, \"metrics\": {\"overall_accuracy\": 86.67, \"pass_f1\": 86.74, \"fail_f1\": 86.6, \"exact_match_rate\": 83.97, \"baseline_gap_pp\": 34.92, \"test_set_size\": 1890, \"unparseable_predictions\": 0}, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_seed789/best/\", \"wall_clock_seconds\": 5158.3, \"gpu_hours\": 1.43}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T14:00:05.341Z\", \"metrics\": {\"overall_accuracy\": 86.67, \"pass_f1\": 86.74, \"fail_f1\": 86.6, \"exact_match_rate\": 83.97, \"baseline_gap_pp\": 34.92, \"test_set_size\": 1890, \"unparseable_predictions\": 0, \"per_class\": {\"fail\": {\"precision\": 84.09, \"recall\": 89.25, \"f1\": 86.6}, \"pass\": {\"precision\": 89.37, \"recall\": 84.25, \"f1\": 86.74}}}}, \"cls8b-seed456\": {\"status\": \"DONE\", \"parent\": \"model-size-scaling-cls8b\", \"retry_count\": 0, \"created_at\": \"2026-05-12T13:55:11.074Z\", \"updated_at\": \"2026-05-12T15:28:45.391Z\", \"hypothesis\": \"8B CLS 第 3 个 seed，与 cwm8b-seed456 配对。完成后有 3 matched 8B pairs (seed42/123/456)，增强 scaling gap 证据\", \"spec\": {\"command\": \"bash -c \\\"export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model_name /home/sonny/projects/verifier-tts-struct-ie/models/Qwen3-8B --output_dir checkpoints_cls8b_seed456/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 456 --no_wandb && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_cls8b_seed456/best --model_name /home/sonny/projects/verifier-tts-struct-ie/models/Qwen3-8B --output eval_cls8b_seed456.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": 2810143, \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed456.log\", \"submitted_at\": \"2026-05-12T13:57:23.981Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 456, \"wall_clock_seconds\": 5481.4, \"gpu_hours\": 1.52}, \"reproduce\": {\"finished_at\": \"2026-05-12T15:25:37.799Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T15:25:39.132859+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 88.31, \"pass_f1\": 88.2, \"fail_f1\": 88.41, \"pass_precision\": 92.29, \"pass_recall\": 84.46, \"fail_precision\": 84.72, \"fail_recall\": 92.43, \"train_loss\": 0.3105, \"eval_loss\": 0.0928, \"unparseable\": 0, \"test_set_size\": 1890}, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b_seed456/best\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls8b-seed456.log\", \"completed_at\": \"2026-05-12T15:28:45.391Z\"}, \"cwm8b-seed456\": {\"status\": \"DONE\", \"parent\": \"model-size-scaling-cwm8b\", \"retry_count\": 0, \"created_at\": \"2026-05-12T13:18:05.040Z\", \"updated_at\": \"2026-05-12T15:00:31.635Z\", \"hypothesis\": \"8B CWM 第 3 个 seed，补强 scaling gap 证据。当前 8B cls-cwm gap 基于 2 seeds (seed42=2.81pp, seed123=2.42pp, mean=2.60pp)，3 seeds 更稳健\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output_dir checkpoints_cwm8b_seed456/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 456 --no_wandb && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm8b_seed456/best --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output eval_cwm8b_seed456.json\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": 47236, \"log_path\": \"/root/runs/exec-sim-repair-verifier/cwm8b-seed456.log\", \"submitted_at\": \"2026-05-12T13:19:20.937Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 456, \"hyperparams\": {\"batch_size\": 2, \"grad_accumulation\": 16, \"lr\": \"2e-4\", \"epochs\": 3, \"PYTORCH_CUDA_ALLOC_CONF\": \"expandable_segments:True\", \"trainable_params\": \"15.3M/8.2B (0.19%)\"}, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm8b_seed456/best/\", \"eval_output_path\": \"/home/sonny/exec-sim-repair-verifier/eval_cwm8b_seed456.json\", \"wall_clock_seconds\": 6070.7, \"gpu_hours\": 1.69}, \"reproduce\": {\"finished_at\": \"2026-05-12T14:57:01.804Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T14:57:03.276321+00:00\"}]}, \"metrics\": {\"overall_accuracy\": 86.24, \"pass_f1\": 85.96, \"fail_f1\": 86.51, \"pass_precision\": 91.08, \"pass_recall\": 81.39, \"fail_precision\": 82.09, \"fail_recall\": 91.45, \"exact_match_rate\": 82.8, \"train_loss\": 0.2279, \"eval_loss\": 0.0583, \"unparseable\": 0, \"test_set_size\": 1890, \"majority_baseline_accuracy\": 51.75, \"accuracy_vs_baseline_gap_pp\": 34.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T15:00:31.635Z\"}, \"5-paired-clustered-bootstrap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T13:10:42.139Z\", \"updated_at\": \"2026-05-12T14:33:52.551Z\", \"hypothesis\": \"5-seed paired variant-level clustered bootstrap CI + TOST 等价检验，验证 CLS 和 TRAJ 在 variant 级别是否等价（扩展之前 3-paired 分析）\", \"conclusion\": \"success\", \"metrics\": {\"pooled_gap_pp\": -0.45, \"pooled_ci_lower\": -1.71, \"pooled_ci_upper\": 0.84, \"pooled_p_value\": 0.499, \"tost_p_value\": 0.0071, \"tost_margin_pp\": 2, \"seed_level_paired_t_p\": 0.425, \"seed_level_mean_gap\": -0.48, \"n_variants_pooled\": 523, \"n_clusters\": 114, \"per_seed_gaps\": {\"seed42\": -0.97, \"seed123\": 1.45, \"seed456\": -1.84, \"seed789\": -0.78, \"seed0\": -0.29}}, \"notes\": \"5-paired 扩展了之前 3-paired 分析。核心发现：CLS 和 TRAJ 在 variant 级别统计等价（TOST p=0.0071, margin ±2pp），无显著差异（gap=-0.45pp, p=0.499）。确认 D018：per-test CLS 聚合到 variant 级别后与 TRAJ 表现一致。注意：seed 789/0 使用 4-bit 量化推理（低于 bf16 ~2-3pp），但 paired 比较内部一致。结果保存在 home:/home/sonny/exec-sim-repair-verifier/clustered_bootstrap_5paired.json。\", \"checkpoint_path\": \"N/A (statistical analysis)\", \"spec\": {\"checkpoint_path\": \"N/A (analysis task)\", \"log_path\": \"home:/home/sonny/exec-sim-repair-verifier/clustered_bootstrap_5paired.json\"}, \"completed_at\": \"2026-05-12T14:33:41.311Z\", \"log_path\": \"home:/home/sonny/exec-sim-repair-verifier/clustered_bootstrap_5paired.json\"}, \"cwm-seed0\": {\"status\": \"DONE\", \"parent\": \"cwm-baseline\", \"retry_count\": 0, \"created_at\": \"2026-05-12T12:49:43.806Z\", \"updated_at\": \"2026-05-12T13:53:51.849Z\", \"hypothesis\": \"补充 4B CWM seed=0，凑齐 CWM 5-seed (42, 123, 456, 789, 0)，与 5-seed CLS 做完整 paired 统计分析\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /home/sonny/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c --output_dir checkpoints_cwm_seed0/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 0 && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm_seed0/best/ --model_name /home/sonny/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c --output eval_cwm_seed0.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2764835\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-seed0.log\", \"submitted_at\": \"2026-05-12T12:50:46.224Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 0, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_seed0/best/\", \"wall_clock_seconds\": 3785.6, \"gpu_hours\": 1.05}, \"reproduce\": {\"finished_at\": \"2026-05-12T13:52:02.918Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T13:52:04.195613+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 87.57, \"fail_f1\": 87.93, \"fail_precision\": 82.71, \"fail_recall\": 93.86, \"pass_f1\": 87.18, \"pass_precision\": 93.45, \"pass_recall\": 81.7, \"exact_match_rate\": 84.29, \"eval_loss\": 0.0665, \"train_loss\": 0.2554, \"train_runtime_sec\": 3586}, \"completed_at\": \"2026-05-12T13:53:51.849Z\"}, \"per-test-precision-recall\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T05:51:25.659Z\", \"updated_at\": \"2026-05-12T13:38:59.726Z\", \"spec\": {\"command\": \"python3 eval_precision_recall.py --data_dir data/ --checkpoint_dir checkpoints/best --model_name Qwen/Qwen3-4B --output eval_precision_recall_results.json\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2414143\", \"log_path\": \"~/runs/exec-sim-repair-verifier/per-test-precision-recall.log\", \"submitted_at\": \"2026-05-12T05:51:25.631Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"/home/sonny/exec-sim-repair-verifier/checkpoints/best/\", \"eval_data\": \"data/test.jsonl\", \"checkpoint_path\": \"n/a (eval only)\", \"wall_clock_seconds\": 1093.5, \"gpu_hours\": 0.3}, \"hypothesis\": \"Per-test 级别 precision/recall 诊断分析 — 按 mutation type 和 problem 粒度评估分类器的诊断质量\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T06:09:39.167Z\", \"metrics\": {\"accuracy\": 87.51, \"fail_precision\": 82.75, \"fail_recall\": 93.64, \"fail_f1\": 87.86, \"pass_precision\": 93.24, \"pass_recall\": 81.8, \"pass_f1\": 87.15, \"FP_count\": 58, \"FN_count\": 178, \"best_mutation\": \"return_value (97.26%)\", \"worst_mutation\": \"off_by_one (82.56%)\", \"bucket_6_10_acc\": 96.3, \"bucket_11plus_acc\": 87.12}, \"notes\": \"扩展诊断分析完成 (eval_pertest_diagnostic.py)。新增发现：114 个 problems 中 48 个 (42.1%) 完美预测；median problem fail-F1=94.12%；return_value 最易 (F1=98.6%), off_by_one 最难 (F1=80.8%)；worst problems: MBPP/397 (40%), HumanEval/130 (46%)。脚本和结果保存在 home:/home/sonny/exec-sim-repair-verifier/eval_pertest_diag.json。\"}, \"cwm-seed123\": {\"status\": \"DONE\", \"parent\": \"cwm-baseline\", \"retry_count\": 0, \"created_at\": \"2026-05-12T11:24:58.500Z\", \"updated_at\": \"2026-05-12T13:15:21.097Z\", \"hypothesis\": \"补充 4B CWM seed=123，与 cwm-baseline (seed=42, 87.51%) 对比确认 4B cls-cwm gap ~0.9pp 的稳定性，同时为 \\\"scaling widens gap\\\" 叙事提供更强 evidence\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B --seed 123 --no_wandb --device cuda:0 && python3 eval_cwm_baseline.py --checkpoint_dir checkpoints_cwm_seed123/best --device cuda:0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": \"cuda:2\", \"pid\": 39006, \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-seed123.log\", \"submitted_at\": \"2026-05-12T11:49:35.477Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 123, \"metrics\": {\"overall_accuracy\": 87.2, \"pass_f1\": 86.95, \"fail_f1\": 87.44, \"exact_match_rate\": 84.44, \"majority_baseline_accuracy\": 51.75, \"accuracy_vs_baseline_gap_pp\": 35.45, \"test_set_size\": 1890, \"unparseable_predictions\": 0}, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_seed123/best\", \"wall_clock_seconds\": 5095.9, \"gpu_hours\": 1.42}, \"reproduce\": {\"finished_at\": \"2026-05-12T13:14:08.136Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T13:14:09.405600+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 87.2, \"pass_f1\": 86.95, \"fail_f1\": 87.44, \"exact_match_rate\": 84.44, \"majority_baseline_accuracy\": 51.75, \"accuracy_vs_baseline_gap_pp\": 35.45, \"test_set_size\": 1890, \"unparseable_predictions\": 0}, \"completed_at\": \"2026-05-12T13:14:31.380Z\"}, \"cwm-seed456\": {\"status\": \"DONE\", \"parent\": \"cwm-baseline\", \"retry_count\": 0, \"created_at\": \"2026-05-12T11:46:14.491Z\", \"updated_at\": \"2026-05-12T12:51:35.823Z\", \"hypothesis\": \"补充 4B CWM seed=456，与 cwm-baseline (seed=42, 87.51%) 对比确认 4B cls-cwm gap ~0.9pp 的稳定性，支撑 scaling widens gap 叙事\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /home/sonny/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c --output_dir checkpoints_cwm_seed456/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 456 && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm_seed456/best/ --model_name /home/sonny/.cache/huggingface/hub/models--Qwen--Qwen3-4B/snapshots/1cfa9a7208912126459214e8b04321603b3df60c --output eval_cwm_seed456.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2759009\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-seed456.log\", \"submitted_at\": \"2026-05-12T12:49:16Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 456, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_seed456/best/\", \"wall_clock_seconds\": 38.4, \"gpu_hours\": 0.01}, \"reproduce\": {\"finished_at\": \"2026-05-12T12:48:36.344Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T12:48:37.698557+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 86.98, \"pass_f1\": 86.66, \"fail_f1\": 87.29, \"pass_precision\": 92.26, \"pass_recall\": 81.7, \"fail_precision\": 82.52, \"fail_recall\": 92.65, \"exact_match_rate\": 84.02, \"train_loss\": 0.2525, \"eval_loss_best\": 0.0551, \"eval_loss_final\": 0.0635, \"train_runtime_sec\": 3440, \"unparseable\": 0}, \"completed_at\": \"2026-05-12T12:49:54.438Z\", \"notes\": \"CWM 4B seed=456 训练和评估正常完成。accuracy=86.98%，与 cwm-baseline (seed=42, 87.51%) 相差 -0.53pp，与 cwm8b-seed123 (seed=123, 86.98%) 完全一致。4B CWM 两个非默认 seed 均为 86.98%，略低于 seed=42 的 87.51%，说明 seed=42 可能略偏高，4B CWM 的真实水平约 87.0-87.5%。exact_match_rate=84.02% 与 baseline 完全一致。pass_f1=86.66% vs baseline 87.31% (-0.65pp)，fail_f1=87.29% vs baseline 87.71% (-0.42pp)，差异很小。4B cls-cwm gap 分析：cls-baseline accuracy=88.36%，CWM 均值约 87.16%，gap ~1.2pp，在不同 seed 下稳定存在，支撑 scaling widens gap 叙事。\"}, \"cls-seed0\": {\"status\": \"DONE\", \"parent\": \"multi-seed-core\", \"retry_count\": 0, \"created_at\": \"2026-05-12T10:22:27.264Z\", \"updated_at\": \"2026-05-12T12:31:31.781Z\", \"hypothesis\": \"补充 cls seed=0 用于 5-paired comparison (cls vs traj 各 5 seeds)，确认 per-test classification accuracy 的稳定性\", \"spec\": {\"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls_seed0/best/\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cls-seed0.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-12T12:29:09.860Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T12:29:11.272583+00:00\"}]}, \"metrics\": {\"accuracy\": 87.94, \"pass_f1\": 87.79, \"fail_f1\": 88.08, \"pass_precision\": 92.13, \"pass_recall\": 83.84, \"fail_precision\": 84.2, \"fail_recall\": 92.32, \"train_loss\": 0.2347, \"eval_loss\": 0.0963, \"train_runtime_sec\": 4976.75, \"unparseable\": 0}, \"conclusion\": \"success\", \"notes\": \"5-seed cls comparison complete. Seeds: seed0=87.94, seed42=87.83, seed123=89.52, seed456=87.88, seed789=89.00. Cls 5-seed mean=88.43±0.78 (sample std). Traj 5-seed mean=86.30±0.97. Cls outperforms traj by +2.13pp with lower variance (0.78 vs 0.97). All 5 cls seeds pass MVP-B criteria (per-class F1>65%, accuracy gap>=10pp). Classification approach shows consistent advantage over trajectory-level approach across all seeds.\", \"completed_at\": \"2026-05-12T12:31:22.221Z\"}, \"cls-seed789\": {\"status\": \"DONE\", \"parent\": \"multi-seed-core\", \"retry_count\": 0, \"created_at\": \"2026-05-12T10:22:01.380Z\", \"updated_at\": \"2026-05-12T11:26:34.278Z\", \"hypothesis\": \"补充 cls seed=789 用于 5-paired comparison (cls vs traj 各 5 seeds)，确认 per-test classification accuracy 的稳定性\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_seed789/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 789 --no_wandb && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_seed789/best --model_name Qwen/Qwen3-4B --output eval_seed789.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2748645\", \"log_path\": \"/home/sonny/runs/exec-sim-repair-verifier/cls-seed789.log\", \"submitted_at\": \"2026-05-12T10:22:13.530Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 789, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_seed789/best/\", \"wall_clock_seconds\": 3849.0, \"gpu_hours\": 1.07}, \"reproduce\": {\"finished_at\": \"2026-05-12T11:24:03.000Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T11:24:04.214486+00:00\"}]}, \"metrics\": {\"accuracy\": 89, \"pass_f1\": 88.9, \"fail_f1\": 89.1, \"pass_precision\": 93.3, \"pass_recall\": 84.9, \"fail_precision\": 85.2, \"fail_recall\": 93.4}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T11:26:22.575Z\", \"notes\": \"cls seed789 完成。accuracy=89.0%, pass_f1=88.9%, fail_f1=89.1%。5-seed cls 汇总: seed42=87.83, seed123=89.52, seed456=87.88, seed789=89.0, seed0=pending。4 seeds mean=88.56±0.78。与 traj 5-seed mean 86.30±0.97 比，cls 仍领先 ~2.3pp。\"}, \"traj-level-finetuned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T04:01:30.468Z\", \"updated_at\": \"2026-05-12T10:25:09.350Z\", \"hypothesis\": \"Trajectory-level verifier (聚合 per-test → resolved/unresolved) 的 accuracy 低于 per-test classification 聚合后的准确率，验证 per-test granularity 的信息优势\", \"parent\": \"multi-seed-core\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_traj_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_traj/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 42 --no_wandb && python3 eval_traj_verifier.py --data_dir data/ --checkpoint_dir checkpoints_traj/best --model_name Qwen/Qwen3-4B --output eval_traj_results.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2364326\", \"log_path\": \"~/runs/exec-sim-repair-verifier/traj-level-finetuned.log\", \"submitted_at\": \"2026-05-12T04:51:11.439Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/traj_train.jsonl\", \"data_count\": 8052, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"checkpoint_source\": \"n/a (training from scratch)\", \"eval_data\": \"data/traj_test.jsonl\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj/best/\", \"wall_clock_seconds\": 3366.1, \"gpu_hours\": 0.94}, \"notes\": \"Trajectory-level 85.66% vs per-test classification 88.41%。⚠️ 此比较是不同粒度（1890 tests vs 1032 variants），clustered bootstrap 在 variant 级别对齐后 gap=-0.37pp, p=0.646，两者无显著差异。Per-test 的真正优势在 diagnostic granularity（知道哪个测试失败），不在 raw accuracy。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T05:47:17.506Z\", \"metrics\": {\"accuracy\": 85.66, \"unresolved_f1\": 87.5, \"resolved_f1\": 83.18, \"per_test_consistency\": 79.94}}, \"traj-level-seed456\": {\"status\": \"DONE\", \"parent\": \"traj-level-finetuned\", \"retry_count\": 0, \"created_at\": \"2026-05-12T07:00:59.345Z\", \"updated_at\": \"2026-05-12T10:25:07.158Z\", \"spec\": {\"log_path\": \"~/runs/exec-sim-repair-verifier/traj-level-seed456.log\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj_seed456/best\", \"wall_clock_seconds\": 2001.8, \"gpu_hours\": 0.56}, \"reproduce\": {\"finished_at\": \"2026-05-12T08:21:55.462Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T08:21:56.909045+00:00\"}]}, \"metrics\": {\"overall_accuracy\": 87.4, \"unresolved_f1\": 88.7, \"resolved_f1\": 85.8, \"unresolved_precision\": 85.7, \"unresolved_recall\": 91.9, \"resolved_precision\": 89.7, \"resolved_recall\": 82.3, \"consistency_rate\": 78.8}, \"conclusion\": \"success\", \"hypothesis\": \"验证 traj-level-finetuned 的 2.75pp gap（vs per-test classification）在不同 seed 下稳定存在，确认统计显著性\", \"notes\": \"Traj-level seed 456: accuracy=87.4%, unresolved_f1=88.7%, resolved_f1=85.8%, consistency=78.8%。\\n\\n⚠️ 注意：per-test accuracy vs traj accuracy 的直接比较是不同粒度对比（1890 tests vs 1032 variants），clustered bootstrap 在 variant 级别对齐后无显著差异 (gap=-0.37pp, p=0.646)。Per-test 的优势在 diagnostic granularity 而非 raw accuracy。\", \"completed_at\": \"2026-05-12T08:25:05.975Z\"}, \"traj-level-seed789\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T08:23:44.159Z\", \"updated_at\": \"2026-05-12T10:25:04.794Z\", \"spec\": {\"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj_seed789/best/\", \"log_path\": \"~/runs/exec-sim-repair-verifier/traj-level-seed789.log\"}, \"hypothesis\": \"补充第 4 seed (789) 验证 traj-level ~3pp gap 的统计显著性，5 seeds 降低 p 值至 <0.05\", \"parent\": \"traj-level-finetuned\", \"reproduce\": {\"finished_at\": \"2026-05-12T09:04:01.723Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T09:04:03.029128+00:00\"}]}, \"metrics\": {\"overall_accuracy\": 87.31, \"unresolved_f1\": 88.27, \"resolved_f1\": 86.17, \"unresolved_precision\": 87.41, \"unresolved_recall\": 89.15, \"resolved_precision\": 87.18, \"resolved_recall\": 85.18, \"consistency_rate\": 76.74, \"eval_loss\": 0.1115, \"train_loss\": 0.2255, \"train_runtime_sec\": 2055.9}, \"conclusion\": \"success\", \"notes\": \"seed789: accuracy=87.31, unresolved_f1=88.27, resolved_f1=86.17, consistency=76.74, train_loss=0.2255, eval_loss=0.1115, wall_time=34.3min。\\n\\n5-seed traj-level 汇总: mean accuracy=86.30±0.97, unresolved_f1=87.76±0.68, resolved_f1=84.42±1.45。\\n\\n⚠️ 注意：per-test accuracy (88.41%) vs traj accuracy (86.30%) 的直接比较是不同粒度对比（1890 tests vs 1032 variants），clustered bootstrap 在 variant 级别对齐后 gap=-0.37pp, p=0.646，无显著差异。Per-test 的真正优势在 diagnostic granularity 而非 raw accuracy。\", \"completed_at\": \"2026-05-12T09:06:35.540Z\"}, \"traj-level-seed0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T08:23:47.402Z\", \"updated_at\": \"2026-05-12T10:23:10.812Z\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_traj_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_traj_seed0/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 0 --no_wandb && python3 eval_traj_verifier.py --data_dir data/ --checkpoint_dir checkpoints_traj_seed0/best --model_name Qwen/Qwen3-4B --output eval_traj_seed0.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2611195\", \"log_path\": \"~/runs/exec-sim-repair-verifier/traj-level-seed0.log\", \"submitted_at\": \"2026-05-12T09:07:53.148Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj_seed0/best/\", \"wall_clock_seconds\": 4444.1, \"gpu_hours\": 1.23}, \"hypothesis\": \"补充第 5 seed (0) 验证 traj-level ~3pp gap 的统计显著性，5 seeds 降低 p 值至 <0.05\", \"parent\": \"traj-level-finetuned\", \"reproduce\": {\"finished_at\": \"2026-05-12T10:17:50.011Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T10:17:51.159128+00:00\"}]}, \"notes\": \"clustered bootstrap CI 分析（跨 3 seeds）发现：将 cls 预测聚合到 variant 级别后，cls vs traj gap 消失。Pooled gap = -0.37pp, 95% CI [-1.89, +1.07], p=0.646。原先 per-test accuracy (88.41%) vs traj accuracy (86.46%) 的 2.23pp gap 是苹果橘子比较——前者评估 1890 个测试，后者评估 1032 个变体。方法论重要发现：per-test 的优势不在 variant-level accuracy，而在 diagnostic granularity（知道哪个测试失败）。\", \"metrics\": {\"overall_accuracy\": 85.66, \"unresolved_f1\": 87.37, \"resolved_f1\": 83.41, \"unresolved_precision\": 82.71, \"unresolved_recall\": 92.59, \"resolved_precision\": 90.07, \"resolved_recall\": 77.66, \"consistency_rate\": 79.55, \"train_loss\": 0.225, \"eval_loss_epoch1\": 0.0949, \"eval_loss_epoch2\": 0.0885, \"eval_loss_epoch3\": 0.1011, \"train_runtime_sec\": 4071.3}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T10:21:57.297Z\"}, \"block-corr-empirical\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T08:20:56.388Z\", \"updated_at\": \"2026-05-12T09:27:14.694Z\", \"spec\": {\"plan_id\": \"block-corr-empirical\", \"command\": \"python3 block_correlation_analysis.py --data_dir data --checkpoint_dir checkpoints/best --model_name Qwen/Qwen3-4B --output block_corr_results.json --batch_size 4 --n_permutations 2000\", \"server\": \"home-1x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen/Qwen3-4B + LoRA (seed 42)\", \"seed\": 42, \"checkpoint_source\": \"/home/sonny/exec-sim-repair-verifier/checkpoints/best/\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints/best/\", \"log_path\": \"/tmp/block_corr.log\"}, \"hypothesis\": \"训练好的 per-test 分类器的预测误差在同一 problem_id 内是 block-correlated 而非 i.i.d.，验证 oracle 模拟的 block-correlation 假设\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T08:36:39.118Z\", \"metrics\": {\"icc\": 0.1909, \"icc_p_value\": 0, \"design_effect\": 3.9676, \"overall_error_rate\": 0.1249, \"all_correct_observed\": 46, \"all_correct_expected_iid\": 16.35, \"all_correct_ratio\": 2.81, \"error_std_observed\": 0.1531, \"error_std_expected_iid\": 0.0811, \"error_std_ratio\": 1.89, \"n_samples\": 1890, \"n_problems\": 114, \"inference_precision\": \"bfloat16\", \"version\": \"v2_corrected\"}, \"notes\": \"v2 修正版：用 bfloat16 推理替代 v1 的 4-bit 量化。accuracy 偏差已消除 (87.51% = 主评估)。ICC 从 0.233 降至 0.191（4-bit 量化误差本身也是 block-correlated 的），但结论不变：block-correlation 显著存在 (p<0.0001)，DEFF=3.97。\"}, \"model-size-scaling-cwm8b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T05:08:45.037Z\", \"updated_at\": \"2026-05-12T09:23:59.200Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output_dir checkpoints_cwm8b/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 42 --no_wandb && python3 eval_cwm_baseline.py --data_dir data/ --checkpoint_dir checkpoints_cwm8b/best --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output eval_cwm8b_results.json\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"11522\", \"log_path\": \"/root/runs/exec-sim-repair-verifier/model-size-scaling-cwm8b.log\", \"submitted_at\": \"2026-05-12T07:45:44.177Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cwm8b/best/\", \"wall_clock_seconds\": 5867.9, \"gpu_hours\": 1.63}, \"hypothesis\": \"Qwen3-8B CWM generation baseline 在函数级的 F1 与同尺寸 classification 的差距，相比 4B 尺度（差距 0.2pp）是否扩大或缩小\", \"reproduce\": {\"finished_at\": \"2026-05-12T09:21:05.535Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T09:21:07.119998+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 87.67, \"pass_f1\": 87.57, \"fail_f1\": 87.77, \"pass_precision\": 91.53, \"pass_recall\": 83.95, \"fail_precision\": 84.19, \"fail_recall\": 91.67, \"exact_match_rate\": 84.39, \"train_loss\": 0.229, \"eval_loss_epoch1\": 0.0554, \"eval_loss_epoch2\": 0.0512, \"eval_loss_epoch3\": 0.0564, \"train_runtime_sec\": 5570, \"unparseable\": 0}, \"completed_at\": \"2026-05-12T09:23:32.111Z\", \"notes\": \"8B CWM 相比 4B 几乎无提升: accuracy 87.67 vs 87.51 (+0.16pp), pass_f1 87.57 vs 87.31 (+0.26pp), fail_f1 87.77 vs 87.71 (+0.06pp), exact_match 84.39 vs 84.02 (+0.37pp)。CWM对模型容量增加不敏感，瓶颈可能在于生成精确错误信息的任务复杂度本身，而非模型能力不足。训练3 epoch完成，train_loss=0.229（低于cls的0.3125），eval_loss在epoch2最低(0.0512)。关键对比：8B cls-cwm gap (accuracy 2.81pp, pass_f1 3.29pp, fail_f1 2.29pp) 远大于4B的gap (accuracy 0.90pp, pass_f1 1.10pp, fail_f1 0.69pp)。Gap扩大约3倍，强烈支持complexity hypothesis——classification的scaling效率显著优于CWM generation。\"}, \"model-size-scaling-cls8b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T05:08:43.293Z\", \"updated_at\": \"2026-05-12T09:23:53.485Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output_dir checkpoints_cls8b/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 42 --no_wandb && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_cls8b/best --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --output eval_cls8b_results.json\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"11443\", \"log_path\": \"/root/runs/exec-sim-repair-verifier/model-size-scaling-cls8b.log\", \"submitted_at\": \"2026-05-12T07:45:42.174Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_cls8b/best/\", \"wall_clock_seconds\": 5868.8, \"gpu_hours\": 1.63}, \"hypothesis\": \"Qwen3-8B classification 在函数级 per-test 任务上的 F1 高于 4B (87.5%)，且与 8B CWM 的差距大于 4B 尺度的差距（0.2pp），验证 classification 优势随模型增大扩大\", \"reproduce\": {\"finished_at\": \"2026-05-12T09:21:04.045Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T09:21:05.418335+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 90.48, \"pass_f1\": 90.86, \"fail_f1\": 90.06, \"pass_precision\": 90.22, \"pass_recall\": 91.51, \"fail_precision\": 90.76, \"fail_recall\": 89.36, \"train_loss\": 0.3125, \"eval_loss_epoch1\": 0.0723, \"eval_loss_epoch2\": 0.0741, \"eval_loss_epoch3\": 0.0783, \"train_runtime_sec\": 5614, \"unparseable\": 0}, \"completed_at\": \"2026-05-12T09:23:30.976Z\", \"notes\": \"8B classification 显著优于 4B baseline: accuracy 90.48 vs 88.41 (+2.07pp), pass_f1 90.86 vs 88.41 (+2.45pp), fail_f1 90.06 vs 88.40 (+1.66pp)。训练3 epoch完成，train_loss=0.3125，eval_loss在epoch1最低(0.0723)后略升(epoch3=0.0783)，有轻微过拟合但不影响最终效果。Scaling 明确有效。与同尺寸8B CWM对比：cls-cwm accuracy gap从4B的0.90pp扩大到8B的2.81pp (+1.91pp)，pass_f1 gap从1.10pp扩大到3.29pp (+2.19pp)，fail_f1 gap从0.69pp扩大到2.29pp (+1.60pp)。Classification在模型增大时获益远超CWM generation，支持complexity hypothesis。\"}, \"llm-judge-32b-zeroshot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T05:08:47.931Z\", \"updated_at\": \"2026-05-12T08:21:22.141Z\", \"spec\": {\"command\": \"python eval_llm_judge.py --model /root/autodl-tmp/models/Qwen/Qwen3-32B --quantize-4bit --test-file data/test.jsonl --output eval_llm_judge_32b.json\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"13452\", \"log_path\": \"~/runs/exec-sim-repair-verifier/llm-judge-32b-zeroshot.log\", \"submitted_at\": \"2026-05-12T08:09:27.519Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen3-32B-4bit\", \"seed\": 0, \"checkpoint_path\": \"n/a (eval only, zero-shot)\", \"wall_clock_seconds\": 471, \"gpu_hours\": 0.13}, \"hypothesis\": \"Qwen3-32B 4-bit 量化 zero-shot 是否可达 fine-tuned 4B 水平——若是则 fine-tuning 价值存疑，若否则确认小模型 fine-tuning 的 Pareto 优势\", \"reproduce\": {\"finished_at\": \"2026-05-12T08:19:22.507Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T08:19:23.592438+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 71.69, \"majority_baseline\": 51.75, \"accuracy_vs_baseline_gap\": 19.95, \"fail_precision\": 64.4, \"fail_recall\": 92.43, \"fail_f1\": 75.91, \"pass_precision\": 88.12, \"pass_recall\": 52.35, \"pass_f1\": 65.68, \"unparseable_predictions\": 0, \"trajectory_accuracy\": 99.12, \"trajectory_total_problems\": 114, \"trajectory_correct\": 113, \"trajectory_true_resolved\": 1, \"trajectory_pred_resolved\": 0}, \"completed_at\": \"2026-05-12T08:20:44.265Z\", \"notes\": \"Qwen3-32B 4-bit zero-shot accuracy=71.69%, 远低于 fine-tuned 4B 的 88.41%（差距 16.7pp），确认小模型 fine-tuning 的 Pareto 优势。\\n\\n## Scaling 趋势 (zero-shot)\\n- 8B → 32B: accuracy 64.4% → 71.69% (+7.3pp)\\n- 模型规模增大 4x 仅带来约 7pp 提升，外推到更大模型也难以弥补 16.7pp 差距\\n- pass_recall 从 35.1%(8B) 提升到 52.35%(32B)，但仍远低于 fine-tuned 4B 的均衡水平\\n\\n## Zero-shot 的系统性偏差\\n- 所有 zero-shot 模型都严重偏向预测 FAIL（fail_recall>92%, pass_recall<53%）\\n- Fine-tuned 4B 实现了均衡的 precision/recall（~88%/88%），这是 zero-shot prompting 无法达到的\\n\\n## Trajectory-level\\n- 32B zero-shot trajectory accuracy=99.12%（113/114），与 8B 和 fine-tuned 类似\\n- Trajectory-level 区分度不足以区分方法优劣，sample-level metrics 才是关键\\n\\n## 结论\\n8x 参数量的 zero-shot 推理无法替代小模型 fine-tuning。Fine-tuned 4B 在 accuracy、F1 和 class balance 上全面碾压 32B zero-shot，且推理成本低 8x+。\\n\\nWall clock: 471s (含模型加载 73s), 1 GPU, 0.13 GPU-hours。\"}, \"llm-judge-8b-zeroshot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T05:08:46.511Z\", \"updated_at\": \"2026-05-12T08:14:26.582Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 llm_judge_zeroshot.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B --data_dir data/ --output eval_llm_judge_8b.json --gpu 0\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"13295\", \"log_path\": \"~/runs/exec-sim-repair-verifier/llm-judge-8b-zeroshot.log\", \"submitted_at\": \"2026-05-12T08:09:25.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/test.jsonl\", \"data_count\": 1890, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 0, \"checkpoint_path\": \"n/a (eval only, zero-shot)\", \"wall_clock_seconds\": 300.9, \"gpu_hours\": 0.08}, \"hypothesis\": \"Qwen3-8B zero-shot LLM-as-judge 在 per-test 和 trajectory-level 判别上均低于 fine-tuned 4B 模型，确认 fine-tuning 的必要性\", \"reproduce\": {\"finished_at\": \"2026-05-12T08:12:32.985Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T08:12:34.081464+00:00\"}]}, \"metrics\": {\"overall_accuracy\": 64.4, \"fail_precision\": 57.9, \"fail_recall\": 95.8, \"fail_f1\": 72.2, \"pass_precision\": 90, \"pass_recall\": 35.1, \"pass_f1\": 50.5, \"majority_baseline\": 51.7, \"accuracy_vs_baseline_gap\": 12.6, \"traj_accuracy\": 99.1, \"traj_problems\": 114, \"traj_true_resolved\": 1, \"traj_pred_resolved\": 0, \"confusion\": {\"TP_fail\": 874, \"FN_fail\": 38, \"FP_fail\": 635, \"TN_fail\": 343}}, \"conclusion\": \"success\", \"notes\": \"Qwen3-8B zero-shot LLM-as-judge 远低于 fine-tuned 4B：accuracy 64.4% vs 88.41% (-24pp), fail_f1 72.2% vs 88.4% (-16.2pp), pass_f1 50.5% vs 88.4% (-37.9pp)。模型严重偏向预测 FAIL（1509/1890 预测为 FAIL），fail recall 95.8% 但 precision 仅 57.9%，pass recall 仅 35.1%。Trajectory-level 99.1% accuracy 无意义（114 problems 中仅 1 个 resolved，模型全部预测 unresolved）。结论：fine-tuning 必要性强验证，即使更大的 zero-shot 模型（8B）也无法匹敌更小的 fine-tuned 模型（4B），差距达 24pp。\", \"completed_at\": \"2026-05-12T08:14:26.582Z\"}, \"traj-level-seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T06:09:51.802Z\", \"updated_at\": \"2026-05-12T08:05:28.994Z\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_traj_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_traj_seed123/ --batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 123 --no_wandb && python3 eval_traj_verifier.py --data_dir data/ --checkpoint_dir checkpoints_traj_seed123/best --model_name Qwen/Qwen3-4B --output eval_traj_seed123.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2427622\", \"log_path\": \"~/runs/exec-sim-repair-verifier/traj-level-seed123.log\", \"submitted_at\": \"2026-05-12T06:10:21.885Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/traj_train.jsonl\", \"data_count\": 8052, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 123, \"checkpoint_source\": \"n/a (training from scratch)\", \"eval_data\": \"data/traj_test.jsonl\", \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_traj_seed123/best\", \"wall_clock_seconds\": 6907.1, \"gpu_hours\": 1.92}, \"hypothesis\": \"验证 traj-level-finetuned 的 2.75pp gap（vs per-test classification）在不同 seed 下稳定存在，确认统计显著性\", \"parent\": \"traj-level-finetuned\", \"reproduce\": {\"finished_at\": \"2026-05-12T07:50:37.896Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-12T07:50:38.908178+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 85.47, \"unresolved_f1\": 87, \"resolved_f1\": 83.52, \"unresolved_precision\": 83.53, \"unresolved_recall\": 90.78, \"resolved_precision\": 88.17, \"resolved_recall\": 79.33, \"consistency_rate\": 78.59}, \"completed_at\": \"2026-05-12T08:05:28.994Z\"}, \"oracle-f2p-stratified\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T06:06:58.065Z\", \"updated_at\": \"2026-05-12T06:07:22.217Z\", \"spec\": {\"command\": \"python3 oracle_f2p_stratified.py --output oracle_f2p_stratified_results.json\", \"server\": \"home-1x5090\", \"data_path\": \"n/a (simulation using SWE-bench F2P distribution)\", \"data_count\": 0, \"model_name\": \"n/a (oracle simulation)\", \"seed\": 42, \"checkpoint_path\": \"n/a\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/oracle_f2p_stratified_results.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T06:07:14.982Z\", \"hypothesis\": \"Per-test verifier 的优势集中在 F2P test count ≥2 的实例上，T=1 时退化为 trajectory-level（无信息增益）\", \"metrics\": {\"T1_pct\": 68.7, \"T1_block_adv\": -0.09, \"T2_pct\": 19.1, \"T2_block_adv\": 31.69, \"T3_5_pct\": 7.1, \"T3_5_block_adv\": 40.74, \"T6plus_pct\": 5.1, \"T6plus_block_adv\": 40.06, \"overall_block_adv\": 10.93, \"T2_contribution_pct\": 55.3}}, \"mvp-b-train\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-11T19:24:04.462Z\", \"updated_at\": \"2026-05-12T04:44:41.807Z\", \"hypothesis\": \"Qwen3-4B LoRA 在函数级 (code, test) → pass/fail 上可达 per-class F1 >65%, accuracy > majority+10pp\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints/best/ --output eval_results.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2102798\", \"log_path\": \"~/runs/exec-sim-repair-verifier/mvp-b-train.log\", \"submitted_at\": \"2026-05-11T20:06:48.617Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"wall_clock_seconds\": 4384.0, \"gpu_hours\": 1.22}, \"notes\": \"OOM at step 15 (2nd attempt). Root cause: cross_entropy logits fp32 = 9.4GB + model 26GB > 32GB VRAM. Fix: bs 8→2, grad_accum 4→16, effective bs unchanged at 32. Retry count: 2.\", \"conclusion\": \"success\", \"metrics\": {\"overall_accuracy\": 0.875, \"pass_f1\": 0.871, \"fail_f1\": 0.879, \"pass_precision\": 0.9324, \"pass_recall\": 0.818, \"fail_precision\": 0.8275, \"fail_recall\": 0.9364, \"majority_baseline\": 0.52, \"accuracy_vs_majority_gap\": 0.355}, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints/best/\", \"completed_at\": \"2026-05-11T21:19:52.606Z\"}, \"multi-seed-core\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-11T22:31:56.650Z\", \"updated_at\": \"2026-05-12T04:44:24.731Z\", \"hypothesis\": \"Classification verifier 在 3 seeds 下稳定达到 ~87% accuracy/F1，CWM ≈ classification 的 null result robust\", \"spec\": {\"command\": \"bash -c \\\"cd /home/sonny/exec-sim-repair-verifier && python3 train_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_seed42/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_seed42/best/ --output eval_seed42.json && python3 train_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_seed123/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 123 && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_seed123/best/ --output eval_seed123.json && python3 train_verifier.py --data_dir data/ --model_name Qwen/Qwen3-4B --output_dir checkpoints_seed456/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 456 && python3 eval_verifier.py --data_dir data/ --checkpoint_dir checkpoints_seed456/best/ --output eval_seed456.json\\\"\", \"server\": \"home-1x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"2135757\", \"log_path\": \"~/runs/exec-sim-repair-verifier/multi-seed-core.log\", \"submitted_at\": \"2026-05-11T23:56:06.403Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"sonny\", \"wall_clock_seconds\": 17298.3, \"gpu_hours\": 4.81}, \"metrics\": {\"seed42\": {\"accuracy\": 87.83, \"pass_f1\": 88.06, \"fail_f1\": 87.59, \"pass_precision\": 89.45, \"pass_recall\": 86.71, \"fail_precision\": 86.2, \"fail_recall\": 89.04}, \"seed123\": {\"accuracy\": 89.52, \"pass_f1\": 89.64, \"fail_f1\": 89.4, \"pass_precision\": 91.76, \"pass_recall\": 87.63, \"fail_precision\": 87.34, \"fail_recall\": 91.56}, \"seed456\": {\"accuracy\": 87.88, \"pass_f1\": 87.53, \"fail_f1\": 88.21, \"pass_precision\": 93.6, \"pass_recall\": 82.21, \"fail_precision\": 83.12, \"fail_recall\": 93.97}, \"mean\": {\"accuracy\": 88.41, \"pass_f1\": 88.41, \"fail_f1\": 88.4}, \"std\": {\"accuracy\": 0.96, \"pass_f1\": 1.1, \"fail_f1\": 0.92}}, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/checkpoints_seed{42,123,456}/best/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T04:44:24.731Z\"}, \"mvp-a-oracle-sim\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-11T18:02:03.506Z\", \"updated_at\": \"2026-05-11T20:05:44.123Z\", \"hypothesis\": \"Per-test verifier 在 70-85% 精度下 resolve rate 比 trajectory-level 高 ≥5%（绝对值）\", \"spec\": {\"command\": \"python3 mvp_a_oracle_sim.py\", \"server\": \"home-1x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/\", \"data_count\": 10000, \"model_name\": \"oracle-sim\", \"seed\": 42, \"checkpoint_path\": \"/home/sonny/exec-sim-repair-verifier/mvp_a_results.json\", \"log_path\": \"/home/sonny/exec-sim-repair-verifier/mvp_a_results.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-11T18:39:41.540Z\", \"metrics\": {\"original_T12\": {\"iid_adv_70_85\": 0.1849, \"block_adv_70_85\": 0.3618}, \"sensitivity_T3\": {\"iid_adv_70_85\": 0.0761, \"block_adv_70_85\": 0.3839}, \"sensitivity_T7\": {\"iid_adv_70_85\": 0.1351, \"block_adv_70_85\": 0.3833}, \"sensitivity_T11\": {\"iid_adv_70_85\": 0.1863, \"block_adv_70_85\": 0.3639}, \"real_f2p_T1\": {\"iid_adv_70_85\": 0.0198, \"block_adv_70_85\": 0.1088, \"pct_T1\": 0.687, \"T_median\": 1, \"T_mean\": 2.3}, \"swebench_f2p_stats\": {\"median\": 1, \"mean\": 3, \"P75\": 2, \"P90\": 3}, \"total_reg5pct\": {\"iid_adv_70_85\": -0.01, \"block_adv_70_85\": -0.005, \"pass\": false}, \"total_reg10pct\": {\"iid_adv_70_85\": 0.132, \"block_adv_70_85\": 0.083, \"pass\": true}, \"total_reg20pct\": {\"iid_adv_70_85\": 0.357, \"block_adv_70_85\": 0.278, \"pass\": true}}, \"notes\": \"Total (F2P+P2P) simulation completed (2026-05-11). Real SWE-bench dist: F2P median=1, P2P median=50.5, Total median=52. Results by P2P regression rate: (1) reg=5%: per-test advantage NEGATIVE for both i.i.d.(-1.0%) and block(-0.5%) — BOTH FAIL. (2) reg=10%: clear advantage, PASS. (3) reg=20%: dominant, PASS. CRITICAL UPDATE: Real P2P regression rate measured at ~1% (mean), 0% (median) from CoderForge data (106 wrong patches). 77% of wrong patches break zero P2P tests. Real scenario is WORSE than reg=5% simulation. Per-test advantage on Total tests is NEGATIVE in practice. Remaining value: F2P-only discrimination (block-corr advantage=10.9%), but F2P median=1 limits this to 31% of instances with F2P≥2.\"}, \"mvp-b-data-prep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-11T18:02:03.573Z\", \"updated_at\": \"2026-05-11T19:00:11.658Z\", \"hypothesis\": \"HumanEval/MBPP 可构建足够的 (code, test) → pass/fail 训练数据用于函数级 pilot\", \"spec\": {\"command\": \"python3 -u build_data.py --output-dir data --seed 42\", \"server\": \"home-1x5090\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/\", \"data_count\": 19076, \"model_name\": \"n/a\", \"seed\": 42}, \"checkpoint_path\": \"n/a\", \"log_path\": \"/tmp/build_data.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-11T19:00:03.494Z\", \"notes\": \"Total: 19,076 samples (HumanEval 5,575 + MBPP 13,501). Class balance: pass 52.0% / fail 48.0%. Majority baseline: 52.0%. Splits: train=15,290 val=1,896 test=1,890. 5 mutation types: operator_swap (66.1% fail), return_value (87.5%), boundary_removal (72.3%), variable_swap (51.6%), off_by_one (42.5%). All labels verified by actual test execution (5s timeout).\"}}, \"count\": 152, \"total\": 152, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6971}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
The registry output is too large. Let me read it in chunks and also start reading key artifact files. Let me plan my approach:

1. I need to read the registry data to check experiment numbers
2. I need to read specific artifacts for statistical results
3. I need to cross-reference everything

Let me start by reading the registry data and key artifacts in parallel. The registry is saved to a file, let me read it in chunks. Also let me start reading the key artifacts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "c31efe46-4eb8-4828-b637-c2fa393a962e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9uhWYiwMzv988V3eoithR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36576,
      "cache_read_input_tokens": 26988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 36576
      },
      "output_tokens": 8,
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


### Assistant

_source line 25_

Registry data is large. Let me read it in chunks and the key artifact files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "33c20752-0acc-4e1f-b087-8c97f9c109b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9uhWYiwMzv988V3eoithR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36576,
      "cache_read_input_tokens": 26988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 36576
      },
      "output_tokens": 8,
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

_source line 26_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0158JUDwJknhY8ZYNNuQNCeb`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "d48f5829-bc92-4eec-9a29-2a5f37b91d1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9uhWYiwMzv988V3eoithR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36576,
      "cache_read_input_tokens": 26988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 36576
      },
      "output_tokens": 8,
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

_source line 27 · 2026-05-23T19:17:00.249Z_

<details><summary>↩ Tool result · `toolu_0158JUDwJknhY8ZYNNuQNCeb`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "74e95585-891b-43a9-a3ee-2447708e4fd2",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_015B7N2dNCw1kPXWbymnDkw4`</summary>

```json
{
  "todos": [
    {
      "content": "Audit Abstract numbers",
      "status": "in_progress",
      "activeForm": "Auditing Abstract numbers"
    },
    {
      "content": "Audit Table 1 (function-level)",
      "status": "pending",
      "activeForm": "Auditing Table 1 function-level numbers"
    },
    {
      "content": "Audit Table 2 (repo-level)",
      "status": "pending",
      "activeForm": "Auditing Table 2 repo-level numbers"
    },
    {
      "content": "Audit Table 3 (failure mode taxonomy)",
      "status": "pending",
      "activeForm": "Auditing Table 3 failure mode taxonomy"
    },
    {
      "content": "Audit Scaling Table (14B results)",
      "status": "pending",
      "activeForm": "Auditing Scaling Table 14B results"
    },
    {
      "content": "Audit TOST and statistical numbers",
      "status": "pending",
      "activeForm": "Auditing TOST and statistical numbers"
    },
    {
      "content": "Audit inline text numbers",
      "status": "pending",
      "activeForm": "Auditing inline text numbers"
    },
    {
      "content": "Audit special check items (M1 data, oracle, etc.)",
      "status": "pending",
      "activeForm": "Auditing special check items"
    },
    {
      "content": "Audit Figures data sources",
      "status": "pending",
      "activeForm": "Auditing Figures data sources"
    },
    {
      "content": "Write audit results to artifacts/data_audit_results.md",
      "status": "pending",
      "activeForm": "Writing audit results"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "f6fcc002-27d4-4e5d-baaf-522e4d3ba9a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xjo8WGUMLPefBaem7HGif6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 63564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2604
      },
      "output_tokens": 42,
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

_source line 29 · 2026-05-23T19:17:17.501Z_

<details><summary>↩ Tool result · `toolu_015B7N2dNCw1kPXWbymnDkw4`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "e6cc7f29-415a-46f6-a988-ac49dd09f2c9",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Audit Abstract numbers",
        "status": "in_progress",
        "activeForm": "Auditing Abstract numbers"
      },
      {
        "content": "Audit Table 1 (function-level)",
        "status": "pending",
        "activeForm": "Auditing Table 1 function-level numbers"
      },
      {
        "content": "Audit Table 2 (repo-level)",
        "status": "pending",
        "activeForm": "Auditing Table 2 repo-level numbers"
      },
      {
        "content": "Audit Table 3 (failure mode taxonomy)",
        "status": "pending",
        "activeForm": "Auditing Table 3 failure mode taxonomy"
      },
      {
        "content": "Audit Scaling Table (14B results)",
        "status": "pending",
        "activeForm": "Auditing Scaling Table 14B results"
      },
      {
        "content": "Audit TOST and statistical numbers",
        "status": "pending",
        "activeForm": "Auditing TOST and statistical numbers"
      },
      {
        "content": "Audit inline text numbers",
        "status": "pending",
        "activeForm": "Auditing inline text numbers"
      },
      {
        "content": "Audit special check items (M1 data, oracle, etc.)",
        "status": "pending",
        "activeForm": "Auditing special check items"
      },
      {
        "content": "Audit Figures data sources",
        "status": "pending",
        "activeForm": "Auditing Figures data sources"
      },
      {
        "content": "Write audit results to artifacts/data_audit_results.md",
        "status": "pending",
        "activeForm": "Writing audit results"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 30_

Let me read the registry data and key artifacts in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "09faeb83-43a9-4fd3-b772-d3d9740d1539",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ro7ymyKJZKhwGyphMYZfM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 66168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 447
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

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01SAav8kscgzTg4edxtQBKDA`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/mcp-agent-ml-research-read_registry-1779563814054.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n# Print experiment IDs, metrics, and key fields\nfor exp in result:\n    eid = exp.get('experiment_id', 'N/A')\n    status = exp.get('status', 'N/A')\n    conclusion = exp.get('conclusion', 'N/A')\n    metrics = exp.get('metrics', {})\n    notes = exp.get('notes', '')[:100] if exp.get('notes') else ''\n    print(f'{eid} | {status} | {conclusion} | {json.dumps(metrics)} | {notes}')\n\" 2>&1 | head -200",
  "description": "Extract experiment IDs and metrics from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "978e98c4-5ec3-4f39-8f55-896e844d7803",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ro7ymyKJZKhwGyphMYZfM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 66168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 447
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

_source line 32 · 2026-05-23T19:17:31.424Z_

<details><summary>↩ Tool result · `toolu_01SAav8kscgzTg4edxtQBKDA`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    eid = exp.get('experiment_id', 'N/A')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "cfcd060e-35a6-4f19-9a9c-e2ff6fd200d7",
  "tool_use_result": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 7, in &lt;module>\n    eid = exp.get('experiment_id', 'N/A')\n          ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Glob · `toolu_012marYFZDmEKPFEzSAj9r56`</summary>

```json
{
  "pattern": "artifacts/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "16ac6d03-d1c7-42b2-8197-8c3ca03c3a42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ro7ymyKJZKhwGyphMYZfM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 66168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 447
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

_source line 34 · 2026-05-23T19:17:31.525Z_

<details><summary>↩ Tool result · `toolu_012marYFZDmEKPFEzSAj9r56`</summary>

```text
artifacts/mvp-a-oracle-sim/data/mvp_a_results_summary.txt
artifacts/mvp-a-oracle-sim/chart/mvp_a_curves_ref.txt
artifacts/mvp-a-oracle-sim/data/mvp_a_results_ref.txt
artifacts/mvp-b-data-prep/data/mvp-b-training-data-manifest.txt
artifacts/mvp-b-data-prep/data/mvp_b_data_ref.txt
artifacts/mvp-a-oracle-sim/data/mvp_a_sensitivity_pointer.txt
artifacts/mvp-a-oracle-sim/data/mvp_a_real_f2p_pointer.txt
artifacts/_project/data/swebench_test_dist_pointer.txt
artifacts/mvp-a-oracle-sim/chart/mvp_a_sensitivity_ref.txt
artifacts/mvp-a-oracle-sim/data/mvp_a_total_results.json
artifacts/mvp-a-oracle-sim/chart/mvp_a_total_curves.pdf
artifacts/mvp-a-oracle-sim/chart/mvp_a_total_curves_ref.txt
artifacts/p2p-regression-rate/report/p2p_regression_analysis.md
artifacts/dream_reports/dream_20260511T214810/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260511T214810/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260511T214810/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260511T214810/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260511T214810/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260511T214810/best/experiment_data.json
artifacts/dream_reports/dream_20260511T214810/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260511T214810/median/experiment_data.json
artifacts/dream_reports/dream_20260511T214810/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260511T214810/worst/experiment_data.json
artifacts/dream_reports/dream_20260511T214810/best/review_report.md
artifacts/dream_reports/dream_20260511T214810/median/review_report.md
artifacts/dream_reports/dream_20260511T214810/worst/review_report.md
artifacts/dream_reports/dream_20260511T214810/meta.yaml
artifacts/dream_reports/dream_20260511T223609/meta.yaml
artifacts/dream_reports/dream_20260511T225536/logs/orchestrator.log
artifacts/dream_reports/dream_20260511T225536/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260511T225536/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260511T225536/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260511T230709/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260511T230709/logs/orchestrator.log
artifacts/dream_reports/dream_20260511T230709/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260511T230709/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260511T231719/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260511T231719/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260511T231719/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260511T231719/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260511T231719/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260511T231719/best/experiment_data.json
artifacts/dream_reports/dream_20260511T231719/best/paper.tex
artifacts/dream_reports/dream_20260511T231719/best/references.bib
artifacts/dream_reports/dream_20260511T231719/best/paper.bbl
artifacts/dream_reports/dream_20260511T231719/best/paper.blg
artifacts/dream_reports/dream_20260511T231719/best/paper.aux
artifacts/dream_reports/dream_20260511T231719/best/paper.out
artifacts/dream_reports/dream_20260511T231719/best/paper.pdf
artifacts/dream_reports/dream_20260511T231719/best/paper.log
artifacts/dream_reports/dream_20260511T231719/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260511T231719/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260511T231719/median/experiment_data.json
artifacts/dream_reports/dream_20260511T231719/median/paper.tex
artifacts/dream_reports/dream_20260511T231719/median/paper.aux
artifacts/dream_reports/dream_20260511T231719/median/paper.out
artifacts/dream_reports/dream_20260511T231719/median/paper.pdf
artifacts/dream_reports/dream_20260511T231719/median/paper.log
artifacts/dream_reports/dream_20260511T231719/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260511T231719/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260511T231719/worst/experiment_data.json
artifacts/dream_reports/dream_20260511T231719/worst/paper.tex
artifacts/dream_reports/dream_20260511T231719/worst/paper.aux
artifacts/dream_reports/dream_20260511T231719/worst/paper.out
artifacts/dream_reports/dream_20260511T231719/worst/paper.pdf
artifacts/dream_reports/dream_20260511T231719/worst/paper.log
artifacts/dream_reports/dream_20260511T231719/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260511T231719/logs/orchestrator.log
artifacts/dream_reports/dream_20260511T231719/best/review_report.md
artifacts/dream_reports/dream_20260511T231719/logs/review_best.log
artifacts/dream_reports/dream_20260511T231719/median/review_report.md
artifacts/dream_reports/dream_20260511T231719/logs/review_median.log
artifacts/dream_reports/dream_20260511T231719/worst/review_report.md
artifacts/dream_reports/dream_20260511T231719/logs/review_worst.log
artifacts/dream_reports/dream_20260511T231719/meta.yaml
artifacts/_project/report/swebench_pipeline_design.md
artifacts/swebench_pipeline_design.md
artifacts/_project/data/inference_cost_results_summary.txt
artifacts/oracle-f2p-stratified/data/oracle_f2p_stratified_results.json
artifacts/block_correlation_analysis.py
artifacts/block-corr-empirical/data/block_corr_results_pointer.txt
artifacts/block-corr-empirical/data/eval_block_correlation_v2.json
artifacts/cwm8b_seed123_analysis.txt
artifacts/repo_level_failure_diagnosis.md
artifacts/_project/intermediate/analysis_5paired_bootstrap.py
artifacts/analysis_5paired_bootstrap.py
artifacts/_project/intermediate/extract_predictions_generic.py
artifacts/extract_predictions_generic.py
artifacts/_project/report/analysis_cls_vs_cwm_4b_5paired.json
artifacts/_project/report/error_overlap_analysis.md
artifacts/_project/data/error_overlap_analysis.txt
artifacts/_project/data/cls_seed42_predictions_ref.txt
artifacts/_project/data/cwm_seed42_predictions_ref.txt
artifacts/_project/data/cls_cwm_error_overlap.md
artifacts/_project/data/8b_scaling_bootstrap_results.json
artifacts/_project/report/repo_8b_training_plan.md
artifacts/repo_8b_training_plan.md
artifacts/_project/data/4b_8b_cls_cwm_paired_bootstrap_corrected.json
artifacts/4b_8b_cls_cwm_paired_bootstrap_corrected.json
artifacts/_project/chart/fig1_reformulation_927a9d.pdf
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "8584f44a-8094-4331-a09e-c4975dc51f11",
  "tool_use_result": {
    "filenames": [
      "artifacts/mvp-a-oracle-sim/data/mvp_a_results_summary.txt",
      "artifacts/mvp-a-oracle-sim/chart/mvp_a_curves_ref.txt",
      "artifacts/mvp-a-oracle-sim/data/mvp_a_results_ref.txt",
      "artifacts/mvp-b-data-prep/data/mvp-b-training-data-manifest.txt",
      "artifacts/mvp-b-data-prep/data/mvp_b_data_ref.txt",
      "artifacts/mvp-a-oracle-sim/data/mvp_a_sensitivity_pointer.txt",
      "artifacts/mvp-a-oracle-sim/data/mvp_a_real_f2p_pointer.txt",
      "artifacts/_project/data/swebench_test_dist_pointer.txt",
      "artifacts/mvp-a-oracle-sim/chart/mvp_a_sensitivity_ref.txt",
      "artifacts/mvp-a-oracle-sim/data/mvp_a_total_results.json",
      "artifacts/mvp-a-oracle-sim/chart/mvp_a_total_curves.pdf",
      "artifacts/mvp-a-oracle-sim/chart/mvp_a_total_curves_ref.txt",
      "artifacts/p2p-regression-rate/report/p2p_regression_analysis.md",
      "artifacts/dream_reports/dream_20260511T214810/logs/phase1_attempt0.log",
      "artifacts/dream_reports/dream_20260511T214810/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260511T214810/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260511T214810/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260511T214810/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260511T214810/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260511T214810/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260511T214810/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260511T214810/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260511T214810/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260511T214810/best/review_report.md",
      "artifacts/dream_reports/dream_20260511T214810/median/review_report.md",
      "artifacts/dream_reports/dream_20260511T214810/worst/review_report.md",
      "artifacts/dream_reports/dream_20260511T214810/meta.yaml",
      "artifacts/dream_reports/dream_20260511T223609/meta.yaml",
      "artifacts/dream_reports/dream_20260511T225536/logs/orchestrator.log",
      "artifacts/dream_reports/dream_20260511T225536/logs/phase1_attempt0.log",
      "artifacts/dream_reports/dream_20260511T225536/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260511T225536/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260511T230709/logs/phase1_attempt0.log",
      "artifacts/dream_reports/dream_20260511T230709/logs/orchestrator.log",
      "artifacts/dream_reports/dream_20260511T230709/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260511T230709/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260511T231719/logs/phase1_attempt0.log",
      "artifacts/dream_reports/dream_20260511T231719/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260511T231719/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260511T231719/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260511T231719/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260511T231719/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260511T231719/best/paper.tex",
      "artifacts/dream_reports/dream_20260511T231719/best/references.bib",
      "artifacts/dream_reports/dream_20260511T231719/best/paper.bbl",
      "artifacts/dream_reports/dream_20260511T231719/best/paper.blg",
      "artifacts/dream_reports/dream_20260511T231719/best/paper.aux",
      "artifacts/dream_reports/dream_20260511T231719/best/paper.out",
      "artifacts/dream_reports/dream_20260511T231719/best/paper.pdf",
      "artifacts/dream_reports/dream_20260511T231719/best/paper.log",
      "artifacts/dream_reports/dream_20260511T231719/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260511T231719/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260511T231719/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260511T231719/median/paper.tex",
      "artifacts/dream_reports/dream_20260511T231719/median/paper.aux",
      "artifacts/dream_reports/dream_20260511T231719/median/paper.out",
      "artifacts/dream_reports/dream_20260511T231719/median/paper.pdf",
      "artifacts/dream_reports/dream_20260511T231719/median/paper.log",
      "artifacts/dream_reports/dream_20260511T231719/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260511T231719/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260511T231719/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260511T231719/worst/paper.tex",
      "artifacts/dream_reports/dream_20260511T231719/worst/paper.aux",
      "artifacts/dream_reports/dream_20260511T231719/worst/paper.out",
      "artifacts/dream_reports/dream_20260511T231719/worst/paper.pdf",
      "artifacts/dream_reports/dream_20260511T231719/worst/paper.log",
      "artifacts/dream_reports/dream_20260511T231719/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260511T231719/logs/orchestrator.log",
      "artifacts/dream_reports/dream_20260511T231719/best/review_report.md",
      "artifacts/dream_reports/dream_20260511T231719/logs/review_best.log",
      "artifacts/dream_reports/dream_20260511T231719/median/review_report.md",
      "artifacts/dream_reports/dream_20260511T231719/logs/review_median.log",
      "artifacts/dream_reports/dream_20260511T231719/worst/review_report.md",
      "artifacts/dream_reports/dream_20260511T231719/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260511T231719/meta.yaml",
      "artifacts/_project/report/swebench_pipeline_design.md",
      "artifacts/swebench_pipeline_design.md",
      "artifacts/_project/data/inference_cost_results_summary.txt",
      "artifacts/oracle-f2p-stratified/data/oracle_f2p_stratified_results.json",
      "artifacts/block_correlation_analysis.py",
      "artifacts/block-corr-empirical/data/block_corr_results_pointer.txt",
      "artifacts/block-corr-empirical/data/eval_block_correlation_v2.json",
      "artifacts/cwm8b_seed123_analysis.txt",
      "artifacts/repo_level_failure_diagnosis.md",
      "artifacts/_project/intermediate/analysis_5paired_bootstrap.py",
      "artifacts/analysis_5paired_bootstrap.py",
      "artifacts/_project/intermediate/extract_predictions_generic.py",
      "artifacts/extract_predictions_generic.py",
      "artifacts/_project/report/analysis_cls_vs_cwm_4b_5paired.json",
      "artifacts/_project/report/error_overlap_analysis.md",
      "artifacts/_project/data/error_overlap_analysis.txt",
      "artifacts/_project/data/cls_seed42_predictions_ref.txt",
      "artifacts/_project/data/cwm_seed42_predictions_ref.txt",
      "artifacts/_project/data/cls_cwm_error_overlap.md",
      "artifacts/_project/data/8b_scaling_bootstrap_results.json",
      "artifacts/_project/report/repo_8b_training_plan.md",
      "artifacts/repo_8b_training_plan.md",
      "artifacts/_project/data/4b_8b_cls_cwm_paired_bootstrap_corrected.json",
      "artifacts/4b_8b_cls_cwm_paired_bootstrap_corrected.json",
      "artifacts/_project/chart/fig1_reformulation_927a9d.pdf"
    ],
    "durationMs": 44,
    "numFiles": 100,
    "truncated": true
  }
}
```

</details>

---


### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01VW3T4CbVghvFykCR1e7K3x`</summary>

```json
{
  "command": "head -c 5000 /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/mcp-agent-ml-research-read_registry-1779563814054.txt | python3 -c \"\nimport json, sys\nraw = sys.stdin.read()\ndata = json.loads(raw)\nresult = data['result']\n# result is a string, parse it\nparsed = json.loads(result)\nif isinstance(parsed, list):\n    print(f'Total experiments: {len(parsed)}')\n    print(f'Type of first: {type(parsed[0])}')\n    if isinstance(parsed[0], dict):\n        print(f'Keys: {list(parsed[0].keys())}')\n        print(json.dumps(parsed[0], indent=2)[:2000])\nelif isinstance(parsed, dict):\n    print(f'Keys: {list(parsed.keys())}')\n\" 2>&1",
  "description": "Examine registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "c18391c9-a5d2-4413-9329-c228155da0ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeUhoMizAgTgLZN3A8MoWc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2755,
      "cache_read_input_tokens": 66615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2755
      },
      "output_tokens": 40,
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

_source line 36 · 2026-05-23T19:17:40.756Z_

<details><summary>↩ Tool result · reported error · `toolu_01VW3T4CbVghvFykCR1e7K3x`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 4, in &lt;module>
    data = json.loads(raw)
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 361, in raw_decode
    obj, end = self.scan_once(s, idx)
               ~~~~~~~~~~~~~~^^^^^^^^
json.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 11 (char 10)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "1020df5b-f058-49f5-afe0-428417edc912",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 4, in &lt;module>\n    data = json.loads(raw)\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 361, in raw_decode\n    obj, end = self.scan_once(s, idx)\n               ~~~~~~~~~~~~~~^^^^^^^^\njson.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 11 (char 10)"
}
```

</details>

---


### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Glob · `toolu_01QpoRgYqHXuhuxSgrWiSLnA`</summary>

```json
{
  "pattern": "artifacts/*holm*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "953cd70e-30a4-42b8-bf7b-7de09a4df972",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeUhoMizAgTgLZN3A8MoWc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2755,
      "cache_read_input_tokens": 66615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2755
      },
      "output_tokens": 40,
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

_source line 38 · 2026-05-23T19:17:41.529Z_

<details><summary>↩ Tool result · reported error · `toolu_01QpoRgYqHXuhuxSgrWiSLnA`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(head -c 5000 /home/ubuntu/.claude-accoun…) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "26ed40e0-8570-4331-84e4-b9eadb6db928",
  "tool_use_result": "Cancelled: parallel tool call Bash(head -c 5000 /home/ubuntu/.claude-accoun…) errored"
}
```

</details>

---


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Glob · `toolu_01JKd7GpVwKrsDyJbfer3pfJ`</summary>

```json
{
  "pattern": "artifacts/*bayesian*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "1147a653-72e7-4068-8f01-ffac6c1c7aac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeUhoMizAgTgLZN3A8MoWc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2755,
      "cache_read_input_tokens": 66615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2755
      },
      "output_tokens": 40,
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

_source line 40 · 2026-05-23T19:17:42.051Z_

<details><summary>↩ Tool result · reported error · `toolu_01JKd7GpVwKrsDyJbfer3pfJ`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(head -c 5000 /home/ubuntu/.claude-accoun…) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "f9476cf4-412d-4be0-bafa-3140033a975b",
  "tool_use_result": "Cancelled: parallel tool call Bash(head -c 5000 /home/ubuntu/.claude-accoun…) errored"
}
```

</details>

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Glob · `toolu_013dvfDsmv3sskopXorbCZug`</summary>

```json
{
  "pattern": "artifacts/*oracle*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "ae9f8a31-5a2a-47e7-9c65-41381fb1b4bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeUhoMizAgTgLZN3A8MoWc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2755,
      "cache_read_input_tokens": 66615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2755
      },
      "output_tokens": 40,
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

_source line 42 · 2026-05-23T19:17:42.963Z_

<details><summary>↩ Tool result · reported error · `toolu_013dvfDsmv3sskopXorbCZug`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(head -c 5000 /home/ubuntu/.claude-accoun…) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "3dd39dea-4381-4acc-b42f-6f6aaf617552",
  "tool_use_result": "Cancelled: parallel tool call Bash(head -c 5000 /home/ubuntu/.claude-accoun…) errored"
}
```

</details>

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Glob · `toolu_01BQKLKaCXdcdVrhpXESoCvH`</summary>

```json
{
  "pattern": "artifacts/*14b*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "13aedf7a-bb99-44e2-b25a-0c95ce51658c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeUhoMizAgTgLZN3A8MoWc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2755,
      "cache_read_input_tokens": 66615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2755
      },
      "output_tokens": 40,
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

_source line 44 · 2026-05-23T19:17:43.456Z_

<details><summary>↩ Tool result · reported error · `toolu_01BQKLKaCXdcdVrhpXESoCvH`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(head -c 5000 /home/ubuntu/.claude-accoun…) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "701c7026-12e8-4fa5-914e-fcaf04684ee9",
  "tool_use_result": "Cancelled: parallel tool call Bash(head -c 5000 /home/ubuntu/.claude-accoun…) errored"
}
```

</details>

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Glob · `toolu_01WYfnC78n2yyeWQzp6ig3gg`</summary>

```json
{
  "pattern": "artifacts/*routing*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "dafc3939-9a63-4d7b-a0fe-84aeb9e711b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeUhoMizAgTgLZN3A8MoWc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2755,
      "cache_read_input_tokens": 66615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2755
      },
      "output_tokens": 40,
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

_source line 46 · 2026-05-23T19:17:44.022Z_

<details><summary>↩ Tool result · reported error · `toolu_01WYfnC78n2yyeWQzp6ig3gg`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(head -c 5000 /home/ubuntu/.claude-accoun…) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "ca184ab1-5b9e-4559-80ed-c7fd6ed0990a",
  "tool_use_result": "Cancelled: parallel tool call Bash(head -c 5000 /home/ubuntu/.claude-accoun…) errored"
}
```

</details>

---


### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_0179i8J1d4uxvtNoZAAJHS3o`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/mcp-agent-ml-research-read_registry-1779563814054.txt', 'r') as f:\n    data = json.load(f)\nresult = data['result']\nparsed = json.loads(result)\nprint(f'Total experiments: {len(parsed)}')\nif len(parsed) > 0:\n    print(f'Keys: {list(parsed[0].keys())}')\n    for exp in parsed[:3]:\n        print(json.dumps(exp, indent=2)[:1500])\n        print('---')\n\" 2>&1",
  "description": "Parse registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "a321c65f-f209-445b-9e46-f7e169fc0e05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mfz7K5fCNC5x3DuBFY9TWF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1356,
      "cache_read_input_tokens": 69370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1356
      },
      "output_tokens": 49,
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

_source line 48 · 2026-05-23T19:17:52.266Z_

<details><summary>↩ Tool result · reported error · `toolu_0179i8J1d4uxvtNoZAAJHS3o`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    print(f'Keys: {list(parsed[0].keys())}')
                        ~~~~~~^^^
KeyError: 0
Total experiments: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "1599f5ac-0028-4796-baed-b5c48f05e4cd",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 9, in &lt;module>\n    print(f'Keys: {list(parsed[0].keys())}')\n                        ~~~~~~^^^\nKeyError: 0\nTotal experiments: 4"
}
```

</details>

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_014YfNWmcyK7sN1wFVCFXDT8`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/mcp-agent-ml-research-read_registry-1779563814054.txt', 'r') as f:\n    data = json.load(f)\nresult = data['result']\nparsed = json.loads(result)\nprint(f'Type: {type(parsed)}')\nif isinstance(parsed, dict):\n    print(f'Top-level keys: {list(parsed.keys())}')\n    for key in parsed:\n        val = parsed[key]\n        if isinstance(val, dict):\n            print(f'\\n=== {key} ===')\n            print(json.dumps(val, indent=2)[:800])\n        elif isinstance(val, list):\n            print(f'\\n=== {key} === (list, len={len(val)})')\n            for item in val[:2]:\n                print(json.dumps(item, indent=2)[:500])\n        else:\n            print(f'{key}: {str(val)[:200]}')\n\" 2>&1",
  "description": "Inspect registry data top-level structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "ad871e2a-6b4d-4ed0-9d70-7df97d8a88e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUTExeRwxHaSVYXKZkxjjn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 70726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 650
      },
      "output_tokens": 73,
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

_source line 50 · 2026-05-23T19:17:57.842Z_

<details><summary>↩ Tool result · `toolu_014YfNWmcyK7sN1wFVCFXDT8`</summary>

```text
Type: &lt;class 'dict'>
Top-level keys: ['success', 'data', 'error', 'metadata']
success: True

=== data ===
{
  "experiments": {
    "deepseek-cwm-repo-s456-train-v2": {
      "status": "DONE",
      "retry_count": 1,
      "created_at": "2026-05-20T08:04:20.919Z",
      "updated_at": "2026-05-23T16:14:08.119Z",
      "hypothesis": "DeepSeek CWM repo-level s456-v2\uff1a\u7b2c 3 seed\uff0c\u4e0e s42/s123-v2 \u5bf9\u9f50\uff08train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 \u884c\uff09\u3002\u7ec4\u6210\u5b8c\u6574 3-seed coverage (42/123/456)\u3002\u4f7f\u7528 epoch 3 final checkpoint \u8bc4\u4f30\u3002",
      "parent": "deepseek-cwm-repo-s456-train",
      "failure_reason": "startup recovery: RUNNING with no cron and no server/pid info",
      "completed_at": "2026-05-20T09:22:41.733Z",
      "extra": {
        "previous_failure": {
          "conclusion": "failed"
   
error: None

=== metadata ===
{
  "elapsed_seconds": 0.6971
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "ba8c61a2-fd99-4857-99d4-dc666991ad44",
  "tool_use_result": {
    "stdout": "Type: &lt;class 'dict'>\nTop-level keys: ['success', 'data', 'error', 'metadata']\nsuccess: True\n\n=== data ===\n{\n  \"experiments\": {\n    \"deepseek-cwm-repo-s456-train-v2\": {\n      \"status\": \"DONE\",\n      \"retry_count\": 1,\n      \"created_at\": \"2026-05-20T08:04:20.919Z\",\n      \"updated_at\": \"2026-05-23T16:14:08.119Z\",\n      \"hypothesis\": \"DeepSeek CWM repo-level s456-v2\\uff1a\\u7b2c 3 seed\\uff0c\\u4e0e s42/s123-v2 \\u5bf9\\u9f50\\uff08train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 \\u884c\\uff09\\u3002\\u7ec4\\u6210\\u5b8c\\u6574 3-seed coverage (42/123/456)\\u3002\\u4f7f\\u7528 epoch 3 final checkpoint \\u8bc4\\u4f30\\u3002\",\n      \"parent\": \"deepseek-cwm-repo-s456-train\",\n      \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\",\n      \"completed_at\": \"2026-05-20T09:22:41.733Z\",\n      \"extra\": {\n        \"previous_failure\": {\n          \"conclusion\": \"failed\"\n   \nerror: None\n\n=== metadata ===\n{\n  \"elapsed_seconds\": 0.6971\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Bash · `toolu_013GHjmQsAgaoFsm8k7ba5HF`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/mcp-agent-ml-research-read_registry-1779563814054.txt', 'r') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\nprint(f'Total experiments: {len(experiments)}')\nfor eid, exp in experiments.items():\n    conclusion = exp.get('conclusion', 'N/A')\n    metrics = exp.get('metrics', {})\n    if metrics:\n        print(f'{eid} | {conclusion} | {json.dumps(metrics)[:300]}')\n\" 2>&1",
  "description": "Extract experiment metrics from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "040c7667-9497-40d5-b7d0-8623f06a5a2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVScUa7mgWjSdS8uTa1Z5M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 837,
      "cache_read_input_tokens": 71376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 837
      },
      "output_tokens": 72,
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

_source line 52 · 2026-05-23T19:18:03.291Z_

<details><summary>↩ Tool result · `toolu_013GHjmQsAgaoFsm8k7ba5HF`</summary>

```text
&lt;persisted-output>
Output too large (37.6KB). Full output saved to: /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/b5t546udu.txt

Preview (first 2KB):
Total experiments: 152
deepseek-cwm-repo-s456-train-v2 | success | {"train_loss": 0.02127, "eval_loss": 5.2837, "total_steps": 12627, "training_time_hours": 27.55}
traj14b-func-s456 | success | {"best_eval_loss": 0.0971, "best_checkpoint": "best", "epochs": 3, "accuracy": 88.28, "dtype": "bf16", "n_test": 1032}
traj14b-func-s123 | success | {"best_eval_loss": 0.0836, "best_checkpoint": "checkpoint-252", "epochs": 3, "accuracy": 88.57, "dtype": "bf16", "n_test": 1032}
traj14b-func-s42 | success | {"best_eval_loss": 0.0958, "best_checkpoint": "best", "epochs": 3, "accuracy": 89.73, "dtype": "bf16", "n_test": 1032}
cwm14b-func-s456 | success | {"accuracy": 90.26, "unparseable": 0, "best_checkpoint": "best", "dtype": "bf16", "n_test": 1890}
cwm14b-func-s123 | success | {"accuracy": 88.99, "unparseable": 0, "best_checkpoint": "best", "dtype": "bf16", "n_test": 1890}
cls14b-func-s456 | success | {"accuracy": 89.79, "f1_fail": 89.45, "f1_pass": 90.11, "precision_fail": 89.2, "recall_fail": 89.69, "precision_pass": 90.34, "recall_pass": 89.88, "unparseable": 0, "best_checkpoint": "checkpoint-478", "dtype": "bf16", "best_train_loss": 0.0659}
cls14b-func-s123 | success | {"accuracy": 90.79, "f1_fail": 90.58, "f1_pass": 90.99, "precision_fail": 89.42, "recall_fail": 91.78, "precision_pass": 92.14, "recall_pass": 89.88, "unparseable": 0, "best_checkpoint": "checkpoint-956", "dtype": "bf16", "best_train_loss": 0.063}
cls14b-func-s42-v2 | success | {"accuracy": 89.47, "f1_fail": 89.02, "f1_pass": 89.88, "unparseable": 0, "checkpoint": "checkpoint-956", "delta_vs_8b": -0.47, "cls_cwm_gap_14b": 0.21}
cwm14b-func-s42 | success | {"accuracy": 89.3, "f1_fail": 88.3, "f1_pass": 90.1, "exact_match_rate": 86.6, "unparseable": 0, "checkpoint": "checkpoint-956", "delta_vs_8b": 1.97}
8b-baseline-rerun | success | {"0shot_accuracy": 60.53, "0shot_f1_macro": 55.73, "3shot_accuracy": 60.42, "3shot_f1_macro": 56.09, "0shot_unparseable": 5, "3shot_unparseable": 1}
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "cf93308b-7788-4822-b1b0-8bd3f45373e4",
  "tool_use_result": {
    "stdout": "Total experiments: 152\ndeepseek-cwm-repo-s456-train-v2 | success | {\"train_loss\": 0.02127, \"eval_loss\": 5.2837, \"total_steps\": 12627, \"training_time_hours\": 27.55}\ntraj14b-func-s456 | success | {\"best_eval_loss\": 0.0971, \"best_checkpoint\": \"best\", \"epochs\": 3, \"accuracy\": 88.28, \"dtype\": \"bf16\", \"n_test\": 1032}\ntraj14b-func-s123 | success | {\"best_eval_loss\": 0.0836, \"best_checkpoint\": \"checkpoint-252\", \"epochs\": 3, \"accuracy\": 88.57, \"dtype\": \"bf16\", \"n_test\": 1032}\ntraj14b-func-s42 | success | {\"best_eval_loss\": 0.0958, \"best_checkpoint\": \"best\", \"epochs\": 3, \"accuracy\": 89.73, \"dtype\": \"bf16\", \"n_test\": 1032}\ncwm14b-func-s456 | success | {\"accuracy\": 90.26, \"unparseable\": 0, \"best_checkpoint\": \"best\", \"dtype\": \"bf16\", \"n_test\": 1890}\ncwm14b-func-s123 | success | {\"accuracy\": 88.99, \"unparseable\": 0, \"best_checkpoint\": \"best\", \"dtype\": \"bf16\", \"n_test\": 1890}\ncls14b-func-s456 | success | {\"accuracy\": 89.79, \"f1_fail\": 89.45, \"f1_pass\": 90.11, \"precision_fail\": 89.2, \"recall_fail\": 89.69, \"precision_pass\": 90.34, \"recall_pass\": 89.88, \"unparseable\": 0, \"best_checkpoint\": \"checkpoint-478\", \"dtype\": \"bf16\", \"best_train_loss\": 0.0659}\ncls14b-func-s123 | success | {\"accuracy\": 90.79, \"f1_fail\": 90.58, \"f1_pass\": 90.99, \"precision_fail\": 89.42, \"recall_fail\": 91.78, \"precision_pass\": 92.14, \"recall_pass\": 89.88, \"unparseable\": 0, \"best_checkpoint\": \"checkpoint-956\", \"dtype\": \"bf16\", \"best_train_loss\": 0.063}\ncls14b-func-s42-v2 | success | {\"accuracy\": 89.47, \"f1_fail\": 89.02, \"f1_pass\": 89.88, \"unparseable\": 0, \"checkpoint\": \"checkpoint-956\", \"delta_vs_8b\": -0.47, \"cls_cwm_gap_14b\": 0.21}\ncwm14b-func-s42 | success | {\"accuracy\": 89.3, \"f1_fail\": 88.3, \"f1_pass\": 90.1, \"exact_match_rate\": 86.6, \"unparseable\": 0, \"checkpoint\": \"checkpoint-956\", \"delta_vs_8b\": 1.97}\n8b-baseline-rerun | success | {\"0shot_accuracy\": 60.53, \"0shot_f1_macro\": 55.73, \"3shot_accuracy\": 60.42, \"3shot_f1_macro\": 56.09, \"0shot_unparseable\": 5, \"3shot_unparseable\": 1}\n14b-baseline-0shot-3shot-v2 | success | {\"0shot\": {\"accuracy\": 66.24, \"gap_vs_majority\": 14.5, \"f1_fail\": 72.99, \"f1_pass\": 55.01, \"f1_macro\": 64, \"unparseable\": 0, \"n\": 1890}, \"3shot\": {\"accuracy\": 73.12, \"gap_vs_majority\": 21.38, \"f1_fail\": 75.79, \"f1_pass\": 69.8, \"f1_macro\": 72.79, \"unparseable\": 0, \"n\": 1890}}\ndeepseek-cwm-repo-s123-eval-1epoch | success | {\"accuracy\": 75.45, \"f1_macro\": 65.08, \"f1_fail\": 46.05, \"f1_pass\": 84.11, \"unparseable_rate\": 66.4, \"unparseable_count\": 6500, \"n_instances\": 9784, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 2.49, \"truncated\": 0}\nqwen3-8b-cwm-repo-s456-eval | success | {\"accuracy\": 66.93, \"f1_macro\": 51.97, \"f1_fail\": 25.16, \"f1_pass\": 78.77, \"unparseable_rate\": 60.39, \"unparseable_count\": 5909, \"n_instances\": 9784, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -6.03, \"precision_fail\": 32.42, \"recall_fail\": 20.56, \"checkpoint_step\": 6633}\ndeepseek-cwm-repo-s123-e3-eval | success | {\"accuracy\": 57.31, \"f1_macro\": 51.79, \"f1_fail\": 35.49, \"f1_pass\": 68.1, \"precision_fail\": 30.01, \"precision_pass\": 74.86, \"recall_fail\": 43.42, \"recall_pass\": 62.45, \"unparseable_count\": 5028, \"unparseable_rate\": 51.39, \"n_instances\": 9784, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -15.65}\nqwen3-8b-cwm-repo-s123-eval | success | {\"accuracy\": 67.33, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -5.62, \"f1_fail\": 32.94, \"f1_pass\": 78.41, \"f1_macro\": 55.67, \"precision_fail\": 37.03, \"precision_pass\": 75.72, \"recall_fail\": 29.67, \"recall_pass\": 81.3, \"unparseable_count\": 6257, \"unparseable_rate\": 63.95, \"n_instances\": 9784, \ndeepseek-cwm-repo-s456-e3-eval | success | {\"accuracy\": 56.11, \"unparseable_rate\": 56.97, \"parseable_only_accuracy\": 32.45, \"f1_macro\": 50.6, \"samples\": 9784}\ndeepseek-cwm-repo-s123 | success | {\"accuracy\": 61.9, \"majority_baseline\": 72.96, \"gap_vs_majority\": -11.06, \"f1_macro\": 51.5, \"f1_pass\": 73.96, \"f1_fail\": 29.04, \"recall_pass\": 74.15, \"recall_fail\": 28.84, \"unparseable_rate\": 65.53, \"total\": 9784, \"correct\": 6056, \"truncated\": 0, \"checkpoint\": \"checkpoint-8844 (epoch 2)\", \"seq_lengt\nqwen3-8b-cwm-repo-s123-train-v4 | success | {\"train_loss\": 0.00873, \"eval_loss\": 0.5166, \"steps_completed\": 6633, \"epochs\": 3, \"training_time_seconds\": 85699}\ndeepseek-cwm-repo-s42-seq4096-eval | success | {\"accuracy\": 61.49, \"unparseable_rate\": 62.5, \"unparseable_count\": 6115, \"n_instances\": 9784, \"f1_macro\": 43.73, \"truncated\": 0, \"truncated_rate\": 0, \"max_generation_tokens\": 284, \"max_new_tokens_limit\": 512, \"seq_length\": 4096}\ndeepseek-cls-repo-s456-eval-v2 | success | {\"accuracy\": 86.15, \"f1_macro\": 80.43, \"f1_fail\": 69.84, \"f1_pass\": 91.01, \"precision_fail\": 84.95, \"recall_fail\": 59.3, \"checkpoint\": \"checkpoint-2163\", \"seq_length\": 8192}\ncls8b-repo-s456-eval-v2 | success | {\"accuracy\": 84.4, \"f1_macro\": 76.19, \"f1_fail\": 62.21, \"f1_pass\": 90.17, \"precision_fail\": 90.23, \"recall_fail\": 47.47, \"checkpoint\": \"checkpoint-2200\", \"seq_length\": 8192}\nqwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval | success | {\"accuracy\": 64.36, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -8.6, \"f1_macro\": 54.42, \"f1_pass\": 75.71, \"f1_fail\": 33.14, \"precision_pass\": 75.3, \"precision_fail\": 33.63, \"recall_pass\": 76.11, \"recall_fail\": 32.65, \"unparseable\": 6236, \"unparseable_rate\": 63.74, \"truncated\": 0, \"truncated_r\ncls8b-s42-ckpt-ablation | success | {\"ckpt-2200\": {\"accuracy\": 85.34, \"f1_macro\": 79.04, \"f1_fail\": 67.56, \"f1_pass\": 90.53}, \"ckpt-3600\": {\"accuracy\": 84.48, \"f1_macro\": 78.17, \"f1_fail\": 66.43, \"f1_pass\": 89.91}, \"ckpt-6633\": {\"accuracy\": 85.29, \"f1_macro\": 78.44, \"f1_fail\": 66.28, \"f1_pass\": 90.6}}\nqwen3-8b-traj-repo-s456 | success | {\"variant_accuracy\": 70.83, \"variant_correct\": 34, \"variant_total\": 48, \"f1_macro\": 70.63, \"overall_accuracy\": 70.83, \"precision_unresolved\": 63.33, \"recall_unresolved\": 86.36, \"f1_unresolved\": 73.08, \"precision_resolved\": 83.33, \"recall_resolved\": 57.69, \"f1_resolved\": 68.18, \"train_loss\": 0.5664, \nqwen3-8b-traj-repo-s123 | success | {\"variant_accuracy\": 77.08, \"variant_correct\": 37, \"variant_total\": 48, \"f1_macro\": 76.59, \"overall_accuracy\": 77.08, \"precision_unresolved\": 78.95, \"recall_unresolved\": 68.18, \"f1_unresolved\": 73.17, \"precision_resolved\": 75.86, \"recall_resolved\": 84.62, \"f1_resolved\": 80, \"train_loss\": 0.5706, \"ev\nexp-downsample-cls-func-v3-eval | success | {\"accuracy\": 80.74, \"f1_macro\": 75.89, \"fail_f1\": 65.1, \"pass_f1\": 86.7, \"unparseable\": 132, \"total\": 9784, \"source\": \"extracted from log (file write failed)\"}\nexp-downsample-cls-func-v3 | success | {\"train_loss\": 0.2869, \"eval_loss_epoch1\": 0.1061, \"eval_loss_epoch2\": 0.0907, \"eval_loss_epoch3\": 0.1156, \"best_epoch\": 2, \"training_time_min\": 44.4}\nexp-e-qwen3-3shot-baseline | success | {\"per_test_accuracy\": 71.61, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -1.35, \"f1_fail\": 61.42, \"f1_pass\": 77.54, \"f1_macro\": 69.48, \"variant_accuracy\": 45.83, \"variant_correct\": 22, \"variant_total\": 48, \"n_instances\": 9784, \"unparseable\": 0, \"truncated\": 0, \"elapsed_min\": 24.6}\nrepo-level-3shot-baseline | success | {\"per_test_accuracy\": 46.28, \"variant_accuracy\": 45.83, \"variant_correct\": 22, \"variant_total\": 48, \"majority_baseline\": 73, \"truncated\": 0, \"unparseable\": 0, \"total\": 9784, \"runtime_min\": 33.8}\nexp-d-constrained-decoding | success | {\"forced_parse\": {\"qwen3_8b\": {\"n\": 9784, \"original_unparseable_rate\": 73.8, \"rescue_rate\": 90.6, \"original_parseable_acc\": 38.5, \"forced_parseable_acc\": 49.4, \"delta_pp\": 10.8}, \"qwen3_4b\": {\"n\": 500, \"original_unparseable_rate\": 75.2, \"rescue_rate\": 77.9, \"original_parseable_acc\": 42.7, \"forced_pa\nexp-b-complexity-bin | success | {\"bins\": {\"23-70\": {\"n_variants\": 12, \"n_tests\": 538, \"cls_qwen3_8b_s123\": 83.3, \"cls_ds_v5\": 91.7, \"cwm_qwen3_8b\": 66.7}, \"71-150\": {\"n_variants\": 14, \"n_tests\": 1282, \"cls_qwen3_8b_s123\": 64.3, \"cls_ds_v5\": 71.4, \"cwm_qwen3_8b\": 42.9}, \"151-250\": {\"n_variants\": 15, \"n_tests\": 2999, \"cls_qwen3_8b_s\nexp-a-routing | success | {\"oracle_routing_7cls\": 100, \"oracle_best_pair\": 95.83, \"test_count_heuristic\": 85.42, \"agreement_confidence\": 83.33, \"majority_vote\": \"75-79%\", \"best_single_cls\": 81.25, \"test_count_heuristic_delta\": \"+4.17pp\", \"oracle_delta\": \"+18.75pp\", \"traj_per_variant\": \"unavailable\", \"cwm_repo_level\": \"45-52%\nqwen3-8b-traj-repo-s42-ckpt98-eval | success | {\"variant_accuracy\": 72.92, \"variant_correct\": 35, \"variant_total\": 48, \"f1_macro\": 72.9, \"fail_recall\": 77.3, \"pass_recall\": 69.2, \"unparseable\": 0, \"note\": \"epoch 2 checkpoint, better class balance than epoch 3\"}\nqwen3-8b-traj-repo-s42-best-eval | success | {\"variant_accuracy\": 70.83, \"variant_correct\": 34, \"variant_total\": 48, \"f1_macro\": 70, \"fail_recall\": 95.5, \"pass_recall\": 50, \"unparseable\": 0, \"note\": \"epoch 3 checkpoint, biased toward predicting unresolved\"}\nqwen3-8b-traj-repo-s42-v2 | success | {\"eval_loss\": \"NaN_all_epochs\", \"total_steps\": 147, \"epochs\": 3, \"seq_length\": 4096, \"best_checkpoint\": \"epoch_3_default_due_to_nan_eval_loss\", \"gradient_checkpointing\": true}\ndeepseek-cls-repo-s123 | success | {\"per_test_accuracy_seq8192\": 74.93, \"per_test_accuracy_seq2048\": 82.62, \"majority_baseline\": 72.96, \"gap_vs_majority_seq8192\": 1.97, \"f1_macro_seq8192\": 53.94, \"f1_fail_seq8192\": 22.84, \"f1_pass_seq8192\": 85.03, \"precision_fail_seq8192\": 68.11, \"recall_fail_seq8192\": 13.72, \"recall_pass_seq8192\": 9\ndeepseek-cls-repo-v5-ckpt6315-eval | success | {\"accuracy\": 82.51, \"fail_recall\": 38.47, \"pass_recall\": 98.84, \"unparseable\": 0, \"n_instances\": 9784, \"confusion\": {\"TN\": 1018, \"FP\": 1628, \"FN\": 83, \"TP\": 7055}, \"variant_accuracy\": 79.17, \"variant_correct\": 38, \"variant_total\": 48, \"variant_fail_recall\": 59.09}\nqwen3-4b-traj-repo-s42-eval | success | {\"variant_accuracy\": 72.92, \"variant_correct\": 35, \"variant_total\": 48, \"f1_macro\": 72.62, \"resolved_precision\": 74.1, \"resolved_recall\": 76.9, \"resolved_f1\": 75.5, \"unresolved_precision\": 71.4, \"unresolved_recall\": 68.2, \"unresolved_f1\": 69.8, \"vs_majority_baseline_pp\": 18.8}\nqwen3-4b-traj-repo-s42 | success | {\"eval_loss_epoch1\": 0.2123, \"eval_loss_epoch2\": 0.1503, \"eval_loss_epoch3\": 0.2249, \"best_epoch\": 2, \"total_steps\": 147}\ndeepseek-cls-repo-v5-ckpt2105-eval | success | {\"accuracy\": 82.61, \"variant_accuracy\": 81.25, \"variant_correct\": 39, \"variant_total\": 48, \"fail_recall\": 51.02, \"pass_recall\": 94.33, \"f1_macro\": 75.07, \"fail_f1\": 61.35, \"pass_f1\": 88.78, \"fail_precision\": 76.92, \"pass_precision\": 83.86, \"unparseable\": 0, \"n_instances\": 9784, \"confusion\": {\"TP\": 6\ndeepseek-cls-repo-v5 | success | {\"train_loss_final\": 0.0399, \"eval_loss_epoch1\": 0.0886, \"eval_loss_epoch2\": 0.1587, \"eval_loss_epoch3\": 0.1975, \"total_steps\": 6315, \"train_time_seconds\": 63312, \"best_checkpoint\": \"checkpoint-2105 (epoch 1)\", \"lora_params\": \"16.8M\"}\ndeepseek-0shot-func-baseline | success | {\"accuracy\": 0.6302, \"pass_f1\": 0.7196, \"fail_f1\": 0.4569, \"unparseable_rate\": 0.0106, \"unparseable_count\": 20, \"total_samples\": 1890, \"runtime_seconds\": 113, \"confusion\": {\"TP\": 897, \"FP\": 618, \"TN\": 294, \"FN\": 81}}\nqwen3-0shot-func-baseline | success | {\"accuracy\": 0.6873, \"pass_f1\": 0.655, \"fail_f1\": 0.7141, \"unparseable_rate\": 0.0032, \"unparseable_count\": 6, \"total_samples\": 1890, \"runtime_seconds\": 96, \"confusion\": {\"TP\": 561, \"FP\": 174, \"TN\": 738, \"FN\": 417}}\ndeepseek-0shot-repo-baseline | success | {\"accuracy\": 0.4854, \"pass_f1\": 0.647, \"fail_f1\": 0.0509, \"unparseable_rate\": 0.087, \"unparseable_count\": 851, \"total_samples\": 9784, \"runtime_seconds\": 1545, \"confusion\": {\"TP\": 4614, \"FP\": 2511, \"TN\": 135, \"FN\": 2524}}\nrepo-level-0shot-baseline | success | {\"accuracy\": 0.499, \"pass_f1\": 0.4895, \"fail_f1\": 0.5081, \"unparseable_rate\": 0, \"unparseable_count\": 0, \"total_samples\": 9784, \"runtime_seconds\": 1018.2, \"confusion\": {\"TP\": 2350, \"FP\": 114, \"TN\": 2532, \"FN\": 4788}}\ndeepseek-cwm-repo | success | {\"train_loss\": 0.021, \"eval_loss\": \"NaN\", \"total_steps\": 13266, \"epochs\": 3, \"wall_clock_seconds\": 112680, \"gpu_hours\": 31.3, \"note\": \"eval_loss=NaN is known DeepSeek issue, does not affect training quality\"}\nqwen3-8b-traj-func-s123 | success | {\"test_accuracy\": 87.79, \"best_eval_loss\": 0.0782, \"pass_f1\": 86.74, \"fail_f1\": 88.69, \"unparseable\": 0, \"per_test_consistency\": 76.07, \"total_steps\": 756, \"test_set_size\": 1032, \"eval_script\": \"eval_traj_verifier_8b.py\"}\nqwen3-8b-traj-func-s42 | success | {\"test_accuracy\": 87.6, \"eval_loss\": 0.0975, \"train_loss\": 0.0312, \"unparseable\": 0, \"pass_f1\": 85.96, \"fail_f1\": 88.89, \"per_test_consistency\": 78.78, \"total_steps\": 756, \"test_set_size\": 1032, \"eval_script\": \"eval_traj_verifier_8b.py\", \"note\": \"87.98% from eval_traj_verifier.py (model.cuda) also v\ndeepseek-cls-func-s123 | success | {\"best_eval_loss\": 0.06753, \"train_time_seconds\": 5391, \"test_accuracy\": 86.77, \"test_f1_macro\": 86.77, \"test_precision_fail\": 84.99, \"test_precision_pass\": 88.56, \"test_recall_fail\": 88.16, \"test_recall_pass\": 85.48, \"test_unparseable_rate\": 0, \"test_n\": 1890}\ndeepseek-cwm-func-s123 | success | {\"best_eval_loss\": 0.0408, \"train_time_seconds\": 5244, \"test_accuracy\": 87.88, \"test_f1_macro\": 87.88, \"test_precision_fail\": 83.78, \"test_precision_pass\": 92.61, \"test_recall_fail\": 92.87, \"test_recall_pass\": 83.23, \"test_unparseable_rate\": 0, \"test_n\": 1890}\ndeepseek-cls-func | success | {\"best_eval_loss\": 0.0701, \"train_time_seconds\": 5444, \"test_accuracy\": 86.93, \"test_f1_macro\": 86.92, \"test_precision_fail\": 86.42, \"test_precision_pass\": 87.41, \"test_recall_fail\": 86.51, \"test_recall_pass\": 87.32, \"test_n\": 1890}\ndeepseek-cwm-func | success | {\"best_eval_loss\": 0.04292, \"train_time_seconds\": 5215, \"test_accuracy\": 85.77, \"test_f1_macro\": 85.73, \"test_precision_fail\": 80.07, \"test_precision_pass\": 93.18, \"test_recall_fail\": 93.86, \"test_recall_pass\": 78.22, \"test_unparseable_rate\": 0, \"test_n\": 1890}\ndeepseek-traj-repo-8k-s999 | success | {\"test_accuracy\": 79.2, \"unparseable\": 0, \"best_eval_loss\": 0.1565, \"resolved_f1\": 82.1, \"unresolved_f1\": 75, \"f1_macro\": 78.57, \"train_loss\": 0.2184}\ndeepseek-traj-repo-8k-s456 | success | {\"test_accuracy\": 75, \"unparseable\": 0, \"best_eval_loss\": 0.1547, \"resolved_f1\": 75, \"unresolved_f1\": 75, \"f1_macro\": 75, \"train_loss\": 0.2176}\ndeepseek-traj-repo-8k-s0 | success | {\"test_accuracy\": 75, \"f1_macro\": 72.68, \"majority_baseline\": 54.2, \"gap_vs_majority_pp\": 20.8, \"unresolved_f1\": 64.7, \"resolved_f1\": 80.6, \"unresolved_precision\": 91.7, \"unresolved_recall\": 50, \"resolved_precision\": 69.4, \"resolved_recall\": 96.2, \"per_test_consistency\": 75, \"unparseable_rate\": 0, \"\ndeepseek-traj-repo-8k-s789 | success | {\"test_accuracy\": 66.67, \"resolved_f1\": 75, \"unresolved_f1\": 50, \"best_eval_loss\": 0.1295, \"unparseable\": 0}\ndeepseek-traj-repo-8k-s123 | success | {\"test_accuracy\": 75, \"unparseable\": 0, \"best_eval_loss\": 0.1182, \"best_epoch\": 2, \"train_truncated_pct\": 2.1, \"gpu_mem_mib\": 21399, \"resolved_f1\": 76.92, \"unresolved_f1\": 72.73}\ndeepseek-traj-repo-8k | success | {\"test_accuracy\": 81.25, \"unparseable\": 0, \"best_eval_loss\": 0.1216, \"best_epoch\": 2, \"train_truncated_pct\": 2.1, \"gpu_mem_mib\": 22475, \"resolved_f1\": 84.21, \"unresolved_f1\": 76.92}\ndeepseek-traj-repo-s123 | success | {\"test_accuracy\": 0.771, \"best_eval_loss\": 0.1147, \"best_step\": 98, \"train_loss\": 0.12, \"unparseable_rate\": 0.167, \"resolved_recall\": 0.962, \"unresolved_recall\": 0.545, \"total_test\": 48}\ndeepseek-traj-repo | success | {\"test_accuracy\": 0.771, \"best_eval_loss\": 0.111, \"best_step\": 98, \"train_loss\": 0.12, \"unparseable_rate\": 0.167, \"resolved_recall\": 0.962, \"unresolved_recall\": 0.545, \"total_test\": 48}\ndeepseek-traj-func-v2-s123 | success | {\"best_eval_loss\": 0.077, \"best_step\": 504, \"test_accuracy\": 0.8508, \"majority_baseline\": 0.5359, \"train_loss\": 0.0842, \"train_runtime_seconds\": 3021, \"per_test_consistency\": 0.782}\ndeepseek-traj-func-v2 | success | {\"best_eval_loss\": 0.0796, \"best_step\": 504, \"test_accuracy\": 0.8324, \"majority_baseline\": 0.5359, \"train_loss\": 0.0857, \"train_runtime_seconds\": 3069.6}\ndeepseek-traj-func | success | {\"eval_loss_epoch1\": 0.0943, \"eval_loss_epoch2\": 0.0793, \"eval_loss_epoch3\": 0.0884, \"best_eval_loss\": 0.0793, \"best_step\": 1008, \"best_epoch\": 2, \"train_loss\": 0.1131, \"train_runtime_sec\": 2910.6}\ncwm4b-s42-mutation-breakdown | success | {\"overall_accuracy\": 58.04, \"parseable_rate\": 46.3, \"parseable_only_accuracy\": 42.9, \"gold_parse_rate\": 43.5, \"gold_parseable_acc\": 23.5, \"operator_swap_parse_rate\": 56.9, \"operator_swap_parseable_acc\": 63.1, \"off_by_one_parse_rate\": 4.4, \"off_by_one_parseable_acc\": 0, \"return_value_parse_rate\": 48.\ncls4b-ckpt4600-test-mutation-pr | success | {\"accuracy\": 83.63, \"gold_acc\": 98.25, \"operator_swap_acc\": 78.91, \"return_value_acc\": 67.97, \"off_by_one_acc\": 58.47, \"boundary_removal_acc\": 46.9, \"n_instances\": 9784, \"note\": \"off_by_one recall_fail=0 (all predicted pass); boundary_removal identical to 8B\"}\ncls8b-seed123-ckpt3000-mutation | success | {\"accuracy\": 85.6, \"boundary_removal\": 44.9, \"operator_swap\": 82.6, \"return_value\": 66.4, \"off_by_one\": 79.2, \"gold\": 99.6, \"n_samples\": 9784}\ncls8b-s42-resume-ckpt3600-test-v2 | success | {\"accuracy\": 84.48, \"f1_macro\": 78.17, \"fail_recall\": 56.8, \"pass_recall\": 94.8, \"n_samples\": 9784, \"note\": \"reproduces v1 exactly\"}\ncls8b-s42-resume-ckpt3600-mutation | success | {\"overall_accuracy\": 84.4849, \"overall_correct\": 8266, \"overall_total\": 9784, \"gold_accuracy\": 96.2443, \"gold_correct\": 4459, \"gold_total\": 4633, \"mutation_operator_swap_accuracy\": 81.3822, \"mutation_operator_swap_correct\": 2732, \"mutation_operator_swap_total\": 3357, \"mutation_off_by_one_accuracy\": \ncls8b-s42-ckpt3600-seq2048-ablation | success | {\"accuracy\": 83.04, \"f1_macro\": 76.8, \"unparseable\": 136, \"n_samples\": 9784, \"seq_length\": 2048}\nrepo-level-cls-8b-s42-resume | success | {\"total_steps\": 6633, \"epochs\": 3, \"train_time_sec\": 74425, \"final_train_loss\": 0.4284, \"final_eval_loss\": 0.4768, \"best_eval_loss_resume\": 0.2516, \"best_eval_loss_resume_step\": 4200, \"best_eval_loss_overall\": 0.0796, \"best_eval_loss_overall_step\": 200, \"checkpoints_saved\": 32, \"overfitting\": true, \ncwm-rank32-alpha64-ablation | success | {\"accuracy\": 87.04, \"pass_f1\": 86.79, \"fail_f1\": 87.27, \"f1_macro\": 87.03, \"pass_precision\": 91.8, \"pass_recall\": 82.3, \"fail_precision\": 82.9, \"fail_recall\": 92.1, \"exact_match_rate\": 84.55, \"train_loss\": 0.2069, \"eval_loss\": 0.0606, \"n_instances\": 1890, \"vs_rank16_baseline\": -0.47, \"rank16_baselin\ncls8b-seed123-ckpt6200-test-eval-v2 | success | {\"accuracy\": 84.7, \"f1_fail\": 63.71, \"f1_pass\": 90.31, \"f1_macro\": 77.01, \"precision_fail\": 88.84, \"precision_pass\": 83.96, \"recall_fail\": 49.66, \"recall_pass\": 97.69, \"n_instances\": 9784, \"n_cls_unparseable\": 0}\ncwm-rank32-ablation-v2 | success | {\"accuracy\": 87, \"exact_match_rate\": 83.4, \"fail_f1\": 87.1, \"pass_f1\": 86.9, \"train_loss_final\": 0.0152, \"train_loss_avg\": 0.2536, \"eval_loss\": 0.0688, \"train_runtime_sec\": 5003, \"test_set_size\": 1890, \"vs_rank16_baseline\": -0.51, \"rank16_baseline_accuracy\": 87.51}\ncls8b-seed123-ckpt200-test-eval | success | {\"accuracy\": 72.55, \"f1_macro\": 70.18, \"pass_f1\": 78.58, \"fail_f1\": 61.78, \"pass_precision\": 91.21, \"pass_recall\": 69.02, \"fail_precision\": 49.54, \"fail_recall\": 82.05, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 72.96, \"unparseable\": 0, \"confusion_matrix\": {\"tn\": 2171, \"\ncls8b-s42-ckpt1000-test-seq2048-ablation | success | {\"accuracy\": 82.83, \"f1_macro\": 76.88, \"fail_precision\": 72.2, \"fail_recall\": 59.3, \"fail_f1\": 65.2, \"pass_precision\": 85.9, \"pass_recall\": 91.5, \"pass_f1\": 88.6, \"unparseable\": 136}\ncls8b-seed123-ckpt6633-test-eval | success | {\"accuracy\": 84.89, \"f1_macro\": 77.56, \"f1_fail\": 64.7, \"f1_pass\": 90.4, \"precision_fail\": 87.8, \"recall_fail\": 51.2, \"precision_pass\": 84.3, \"recall_pass\": 97.4, \"majority_baseline\": 73, \"gap_vs_majority_pp\": 11.9, \"total_samples\": 9784, \"unparseable_count\": 0}\ncls8b-seed123-ckpt6600-test-eval | success | {\"accuracy\": 84.9, \"f1_macro\": 77.58, \"pass_f1\": 90.4, \"fail_f1\": 64.8, \"pass_precision\": 84.3, \"pass_recall\": 97.4, \"fail_precision\": 87.8, \"fail_recall\": 51.3, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 73, \"unparseable\": 0, \"confusion_matrix\": {\"fail_as_fail\": 1357, \"\ncls8b-s42-ckpt200-test8192-eval | success | {\"accuracy\": 70.07, \"f1_macro\": 68.18, \"pass_f1\": 75.9, \"fail_f1\": 60.4, \"pass_precision\": 91.8, \"pass_recall\": 64.7, \"fail_precision\": 47, \"fail_recall\": 84.5, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 73, \"unparseable\": 0, \"confusion_matrix\": {\"fail_as_fail\": 2235, \"f\ncls4b-v5-ckpt600-test5120-eval | success | {\"accuracy\": 77.74, \"f1_macro\": 74.74, \"f1_fail\": 66.03, \"f1_pass\": 83.44, \"precision_fail\": 56.21, \"recall_fail\": 80.01, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 4.78, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-seed123-ckpt6400-test-eval-v2 | success | {\"accuracy\": 85.08, \"f1_fail\": 65.32, \"f1_pass\": 90.49, \"f1_macro\": 77.91, \"precision_fail\": 87.92, \"precision_pass\": 84.54, \"recall_fail\": 51.97, \"recall_pass\": 97.35, \"n_instances\": 9784, \"n_cls_unparseable\": 0}\ncls8b-seed123-ckpt6633-val8192-eval | success | {\"accuracy\": 87.1, \"f1_macro\": 78.79, \"f1_fail\": 65.52, \"f1_pass\": 92.07, \"precision_fail\": 92.26, \"recall_fail\": 50.8, \"precision_pass\": 86.31, \"recall_pass\": 98.64, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.23, \"unparseable_count\": 9, \"total_samples\": 9335}\ncls8b-seed123-ckpt3000-test8192-eval | success | {\"accuracy\": 85.6, \"f1_macro\": 78.38, \"f1_fail\": 65.89, \"f1_pass\": 90.87, \"precision_fail\": 91.65, \"recall_fail\": 51.44, \"precision_pass\": 84.52, \"recall_pass\": 98.26, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.64, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls4b-v5-ckpt4400-test5120-eval | success | {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_fail\": 59.45, \"f1_pass\": 89.44, \"precision_fail\": 85.98, \"recall_fail\": 45.43, \"precision_pass\": 82.78, \"recall_pass\": 97.25, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.28, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-seed123-ckpt6400-val8192-eval | success | {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_fail\": 67.04, \"f1_pass\": 92.27, \"precision_fail\": 91.81, \"recall_fail\": 52.8, \"precision_pass\": 86.78, \"recall_pass\": 98.5, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.6, \"unparseable_count\": 9, \"total_samples\": 9335}\ncls8b-seed123-ckpt6200-val8192-eval | success | {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_fail\": 66.16, \"f1_pass\": 92.35, \"precision_fail\": 95.63, \"recall_fail\": 50.58, \"precision_pass\": 86.33, \"recall_pass\": 99.27, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.64, \"unparseable_count\": 9, \"total_samples\": 9335}\ncls4b-v5-val-sweep-ckpt4600 | success | {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_fail\": 76.37, \"f1_pass\": 93.71, \"precision_fail\": 89.65, \"recall_fail\": 66.52, \"precision_pass\": 90.16, \"recall_pass\": 97.56, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 14.19, \"unparseable_count\": 0, \"total_samples\": 9335, \"n_truncated\": 234}\ncls8b-seed123-ckpt6600-val8192-eval | success | {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_fail\": 65.9, \"f1_pass\": 92.14, \"precision_fail\": 92.6, \"recall_fail\": 51.15, \"precision_pass\": 86.4, \"recall_pass\": 98.7, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.36, \"unparseable_count\": 9, \"total_samples\": 9335}\ncls8b-s42-ckpt1600-test8192-eval | success | {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_fail\": 67.65, \"f1_pass\": 90.22, \"precision_fail\": 81.06, \"recall_fail\": 58.05, \"precision_pass\": 85.93, \"recall_pass\": 94.97, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.03, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls4b-v5-ckpt4600-test-eval | success | {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_fail\": 61.67, \"f1_pass\": 89.59, \"precision_fail\": 84.03, \"recall_fail\": 48.72, \"precision_pass\": 83.55, \"recall_pass\": 96.57, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.67, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-s42-ckpt1400-test8192-eval | success | {\"accuracy\": 85.47, \"f1_macro\": 78.9, \"f1_fail\": 67.13, \"f1_pass\": 90.67, \"precision_fail\": 86.43, \"recall_fail\": 54.88, \"precision_pass\": 85.27, \"recall_pass\": 96.81, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.51, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-s42-ckpt1200-test8192-eval | success | {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_fail\": 65.49, \"f1_pass\": 89.45, \"precision_fail\": 77.52, \"recall_fail\": 56.69, \"precision_pass\": 85.4, \"recall_pass\": 93.91, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.89, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-s42-ckpt800-test8192-eval | success | {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_fail\": 69.17, \"f1_pass\": 88.77, \"precision_fail\": 70.07, \"recall_fail\": 68.29, \"precision_pass\": 88.36, \"recall_pass\": 89.18, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.58, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls4b-v5-val-sweep-ckpt4200 | success | {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_fail\": 73, \"f1_pass\": 93.1, \"precision_fail\": 90.3, \"recall_fail\": 61.3, \"precision_pass\": 88.8, \"recall_pass\": 97.9}\ncls8b-s42-ckpt1600-val8192-v2 | success | {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_fail\": 66.12, \"f1_pass\": 91.76, \"precision_fail\": 86.28, \"precision_pass\": 86.83, \"recall_fail\": 53.6, \"recall_pass\": 97.29, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 10.87, \"unparseable\": 9, \"total\": 9335}\ncls8b-s42-ckpt1400-val8192-eval | success | {\"accuracy\": 85.97, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 10.09, \"f1_macro\": 77.15, \"f1_fail\": 62.95, \"f1_pass\": 91.34, \"precision_fail\": 86.68, \"precision_pass\": 85.85, \"recall_fail\": 49.42, \"recall_pass\": 97.59, \"n_instances\": 9335, \"n_unparseable\": 9, \"confusion_matrix\": {\"tn\": 1113, \ncls4b-v5-val-sweep-ckpt4400-v3 | success | {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_fail\": 76.25, \"f1_pass\": 93.64, \"precision_fail\": 88.84, \"precision_pass\": 90.21, \"recall_fail\": 66.79, \"recall_pass\": 97.33, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 14.09, \"n_instances\": 9335, \"n_truncated\": 234, \"n_unparseable\": 0}\ncls8b-s42-ckpt1200-val8192-v3 | success | {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_fail\": 70.2, \"f1_pass\": 92.3, \"precision_fail\": 85, \"recall_fail\": 59.8, \"precision_pass\": 88.3, \"recall_pass\": 96.7, \"majority_baseline\": 75.9, \"gap_vs_majority\": 11.9, \"unparseable\": 9}\ncls8b-s42-ckpt1000-test8192-eval | success | {\"accuracy\": 83.52, \"f1_macro\": 77.5, \"f1_fail\": 65.85, \"f1_pass\": 89.14, \"precision_fail\": 74.93, \"recall_fail\": 58.73, \"precision_pass\": 85.84, \"recall_pass\": 92.72, \"majority_baseline\": 72.96, \"gap_vs_majority\": 10.56, \"unparseable_count\": 0, \"unparseable_rate\": 0, \"total_samples\": 9784, \"tp\": 66\ncls8b-s42-ckpt1000-val8192-eval | success | {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_fail\": 73, \"f1_pass\": 92.5, \"precision_fail\": 81.8, \"recall_fail\": 65.8, \"precision_pass\": 89.8, \"recall_pass\": 95.3, \"unparseable\": 9, \"total_instances\": 9335}\ncls8b-s42-ckpt800-val8192-eval | success | {\"accuracy\": 84.5, \"f1_macro\": 79.2}\ncls4b-v5-ckpt4000-val5120-eval | success | {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_fail\": 74.85, \"f1_pass\": 93.64, \"precision_fail\": 92.95, \"recall_fail\": 62.66, \"precision_pass\": 89.24, \"recall_pass\": 98.49, \"unparseable\": 0, \"truncated\": 234, \"total\": 9335}\ncls4b-v5-ckpt600-val5120-eval | success | {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_fail\": 72.03, \"f1_pass\": 87.6, \"precision_fail\": 59.3, \"recall_fail\": 91.7, \"unparseable\": 0, \"total\": 9335}\nrepo-level-cls-8b-conda | success | {\"val_8192\": {\"ckpt_200\": {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_fail\": 51.6, \"f1_pass\": 70.7, \"unparseable\": 9}, \"ckpt_400\": {\"accuracy\": 80.96}, \"ckpt_600\": {\"accuracy\": 85}, \"best_acc\": \"ckpt_600\"}, \"val_5120\": {\"ckpt_400\": {\"accuracy\": 80.47, \"f1_macro\": 75.84}}, \"test_2048\": {\"ckpt_400\": {\"\ncls8b-s42-ckpt200-val8192-eval-v2 | success | {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_fail\": 51.6, \"f1_pass\": 70.7, \"unparseable\": 9, \"total\": 9335}\ncls4b-seed123-ckpt800-val5120-eval | success | {\"accuracy\": 87.92, \"f1_macro\": 81.95, \"f1_pass\": 92.33, \"f1_fail\": 71.57, \"unparseable\": 0, \"truncated\": 234, \"total\": 9335}\nrepo-level-cls-seed123-home | success | {\"val_2048\": {\"n\": 9335, \"unparseable\": 1883, \"ckpt_200\": {\"accuracy\": 62.51, \"f1_macro\": 55.54, \"f1_pass\": 73.14, \"f1_fail\": 37.94}, \"ckpt_400\": {\"accuracy\": 80.72, \"f1_macro\": 67.03, \"f1_pass\": 88.27, \"f1_fail\": 45.78}, \"ckpt_600\": {\"accuracy\": 76.78, \"f1_macro\": 66.81, \"f1_pass\": 85, \"f1_fail\": 4\ncls8b-s42-ckpt600-test8192-eval | success | {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_fail\": 65.24, \"f1_pass\": 85, \"precision_fail\": 59.16, \"precision_pass\": 88.95, \"recall_fail\": 72.71, \"recall_pass\": 81.4, \"unparseable\": 0, \"total\": 9784, \"majority_baseline\": 73, \"gap_vs_majority_pp\": 6.09}\ncls8b-seed123-ckpt3000-val8192-eval | success | {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_fail\": 70.5, \"f1_pass\": 93, \"precision_fail\": 95.2, \"precision_pass\": 87.6, \"recall_fail\": 55.9, \"recall_pass\": 99.1, \"majority_baseline\": 75.9, \"gap_vs_majority_pp\": 12.8, \"unparseable\": 9, \"total\": 9335}\ncls8b-s42-ckpt400-test8192-eval | success | {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_fail\": 72.93, \"f1_pass\": 89.43, \"precision_fail\": 70.32, \"precision_pass\": 90.74, \"recall_fail\": 75.74, \"recall_pass\": 88.15, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 11.84, \"unparseable\": 0, \"total\": 9784}\nrepo-level-cls-v5 | success | {\"checkpoint_sweep\": {\"ckpt_600\": {\"accuracy\": 76.74, \"f1_macro\": 73.74, \"fail_f1\": 64.88, \"pass_f1\": 82.61}, \"ckpt_4000\": {\"accuracy\": 81.51, \"f1_macro\": 72.56, \"fail_f1\": 56.9, \"pass_f1\": 88.23}, \"ckpt_4200\": {\"accuracy\": 80.64, \"f1_macro\": 72.1, \"fail_f1\": 56.66, \"pass_f1\": 87.54}, \"ckpt_4400\": {\nrepo-level-cls-v5-conda | success | {\"checkpoint_sweep\": {\"ckpt_200\": {\"accuracy\": 52.96, \"f1_macro\": 52.89, \"fail_f1\": 51.02, \"pass_f1\": 54.76}, \"ckpt_400\": {\"accuracy\": 78.43, \"f1_macro\": 68.41, \"fail_f1\": 50.61, \"pass_f1\": 86.21, \"fail_precision\": 66.48, \"fail_recall\": 40.85, \"pass_precision\": 80.82, \"pass_recall\": 92.36}, \"ckpt_60\nrepo-level-cwm-v10 | success | {\"accuracy\": 0.6991, \"f1_macro\": 0.4671, \"f1_pass\": 0.8187, \"f1_fail\": 0.1154,",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/b5t546udu.txt",
    "persistedOutputSize": 38474
  }
}
```

</details>

---


### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01ML5XS8D2hzYjRvVAhKyBPE`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/b5t546udu.txt",
  "description": "Read full registry metrics output",
  "timeout": 10000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "4f5f1241-5c52-40ba-9134-345ccc76a131",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EWmfoSJeC9A2y5gS6M77T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 72213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1308
      },
      "output_tokens": 62,
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

_source line 54 · 2026-05-23T19:18:06.800Z_

<details><summary>↩ Tool result · `toolu_01ML5XS8D2hzYjRvVAhKyBPE`</summary>

```text
&lt;persisted-output>
Output too large (37.6KB). Full output saved to: /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/bofsph3hk.txt

Preview (first 2KB):
Total experiments: 152
deepseek-cwm-repo-s456-train-v2 | success | {"train_loss": 0.02127, "eval_loss": 5.2837, "total_steps": 12627, "training_time_hours": 27.55}
traj14b-func-s456 | success | {"best_eval_loss": 0.0971, "best_checkpoint": "best", "epochs": 3, "accuracy": 88.28, "dtype": "bf16", "n_test": 1032}
traj14b-func-s123 | success | {"best_eval_loss": 0.0836, "best_checkpoint": "checkpoint-252", "epochs": 3, "accuracy": 88.57, "dtype": "bf16", "n_test": 1032}
traj14b-func-s42 | success | {"best_eval_loss": 0.0958, "best_checkpoint": "best", "epochs": 3, "accuracy": 89.73, "dtype": "bf16", "n_test": 1032}
cwm14b-func-s456 | success | {"accuracy": 90.26, "unparseable": 0, "best_checkpoint": "best", "dtype": "bf16", "n_test": 1890}
cwm14b-func-s123 | success | {"accuracy": 88.99, "unparseable": 0, "best_checkpoint": "best", "dtype": "bf16", "n_test": 1890}
cls14b-func-s456 | success | {"accuracy": 89.79, "f1_fail": 89.45, "f1_pass": 90.11, "precision_fail": 89.2, "recall_fail": 89.69, "precision_pass": 90.34, "recall_pass": 89.88, "unparseable": 0, "best_checkpoint": "checkpoint-478", "dtype": "bf16", "best_train_loss": 0.0659}
cls14b-func-s123 | success | {"accuracy": 90.79, "f1_fail": 90.58, "f1_pass": 90.99, "precision_fail": 89.42, "recall_fail": 91.78, "precision_pass": 92.14, "recall_pass": 89.88, "unparseable": 0, "best_checkpoint": "checkpoint-956", "dtype": "bf16", "best_train_loss": 0.063}
cls14b-func-s42-v2 | success | {"accuracy": 89.47, "f1_fail": 89.02, "f1_pass": 89.88, "unparseable": 0, "checkpoint": "checkpoint-956", "delta_vs_8b": -0.47, "cls_cwm_gap_14b": 0.21}
cwm14b-func-s42 | success | {"accuracy": 89.3, "f1_fail": 88.3, "f1_pass": 90.1, "exact_match_rate": 86.6, "unparseable": 0, "checkpoint": "checkpoint-956", "delta_vs_8b": 1.97}
8b-baseline-rerun | success | {"0shot_accuracy": 60.53, "0shot_f1_macro": 55.73, "3shot_accuracy": 60.42, "3shot_f1_macro": 56.09, "0shot_unparseable": 5, "3shot_unparseable": 1}
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "1971054e-d75a-40a5-8c4d-3a6a7865604b",
  "tool_use_result": {
    "stdout": "Total experiments: 152\ndeepseek-cwm-repo-s456-train-v2 | success | {\"train_loss\": 0.02127, \"eval_loss\": 5.2837, \"total_steps\": 12627, \"training_time_hours\": 27.55}\ntraj14b-func-s456 | success | {\"best_eval_loss\": 0.0971, \"best_checkpoint\": \"best\", \"epochs\": 3, \"accuracy\": 88.28, \"dtype\": \"bf16\", \"n_test\": 1032}\ntraj14b-func-s123 | success | {\"best_eval_loss\": 0.0836, \"best_checkpoint\": \"checkpoint-252\", \"epochs\": 3, \"accuracy\": 88.57, \"dtype\": \"bf16\", \"n_test\": 1032}\ntraj14b-func-s42 | success | {\"best_eval_loss\": 0.0958, \"best_checkpoint\": \"best\", \"epochs\": 3, \"accuracy\": 89.73, \"dtype\": \"bf16\", \"n_test\": 1032}\ncwm14b-func-s456 | success | {\"accuracy\": 90.26, \"unparseable\": 0, \"best_checkpoint\": \"best\", \"dtype\": \"bf16\", \"n_test\": 1890}\ncwm14b-func-s123 | success | {\"accuracy\": 88.99, \"unparseable\": 0, \"best_checkpoint\": \"best\", \"dtype\": \"bf16\", \"n_test\": 1890}\ncls14b-func-s456 | success | {\"accuracy\": 89.79, \"f1_fail\": 89.45, \"f1_pass\": 90.11, \"precision_fail\": 89.2, \"recall_fail\": 89.69, \"precision_pass\": 90.34, \"recall_pass\": 89.88, \"unparseable\": 0, \"best_checkpoint\": \"checkpoint-478\", \"dtype\": \"bf16\", \"best_train_loss\": 0.0659}\ncls14b-func-s123 | success | {\"accuracy\": 90.79, \"f1_fail\": 90.58, \"f1_pass\": 90.99, \"precision_fail\": 89.42, \"recall_fail\": 91.78, \"precision_pass\": 92.14, \"recall_pass\": 89.88, \"unparseable\": 0, \"best_checkpoint\": \"checkpoint-956\", \"dtype\": \"bf16\", \"best_train_loss\": 0.063}\ncls14b-func-s42-v2 | success | {\"accuracy\": 89.47, \"f1_fail\": 89.02, \"f1_pass\": 89.88, \"unparseable\": 0, \"checkpoint\": \"checkpoint-956\", \"delta_vs_8b\": -0.47, \"cls_cwm_gap_14b\": 0.21}\ncwm14b-func-s42 | success | {\"accuracy\": 89.3, \"f1_fail\": 88.3, \"f1_pass\": 90.1, \"exact_match_rate\": 86.6, \"unparseable\": 0, \"checkpoint\": \"checkpoint-956\", \"delta_vs_8b\": 1.97}\n8b-baseline-rerun | success | {\"0shot_accuracy\": 60.53, \"0shot_f1_macro\": 55.73, \"3shot_accuracy\": 60.42, \"3shot_f1_macro\": 56.09, \"0shot_unparseable\": 5, \"3shot_unparseable\": 1}\n14b-baseline-0shot-3shot-v2 | success | {\"0shot\": {\"accuracy\": 66.24, \"gap_vs_majority\": 14.5, \"f1_fail\": 72.99, \"f1_pass\": 55.01, \"f1_macro\": 64, \"unparseable\": 0, \"n\": 1890}, \"3shot\": {\"accuracy\": 73.12, \"gap_vs_majority\": 21.38, \"f1_fail\": 75.79, \"f1_pass\": 69.8, \"f1_macro\": 72.79, \"unparseable\": 0, \"n\": 1890}}\ndeepseek-cwm-repo-s123-eval-1epoch | success | {\"accuracy\": 75.45, \"f1_macro\": 65.08, \"f1_fail\": 46.05, \"f1_pass\": 84.11, \"unparseable_rate\": 66.4, \"unparseable_count\": 6500, \"n_instances\": 9784, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 2.49, \"truncated\": 0}\nqwen3-8b-cwm-repo-s456-eval | success | {\"accuracy\": 66.93, \"f1_macro\": 51.97, \"f1_fail\": 25.16, \"f1_pass\": 78.77, \"unparseable_rate\": 60.39, \"unparseable_count\": 5909, \"n_instances\": 9784, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -6.03, \"precision_fail\": 32.42, \"recall_fail\": 20.56, \"checkpoint_step\": 6633}\ndeepseek-cwm-repo-s123-e3-eval | success | {\"accuracy\": 57.31, \"f1_macro\": 51.79, \"f1_fail\": 35.49, \"f1_pass\": 68.1, \"precision_fail\": 30.01, \"precision_pass\": 74.86, \"recall_fail\": 43.42, \"recall_pass\": 62.45, \"unparseable_count\": 5028, \"unparseable_rate\": 51.39, \"n_instances\": 9784, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -15.65}\nqwen3-8b-cwm-repo-s123-eval | success | {\"accuracy\": 67.33, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -5.62, \"f1_fail\": 32.94, \"f1_pass\": 78.41, \"f1_macro\": 55.67, \"precision_fail\": 37.03, \"precision_pass\": 75.72, \"recall_fail\": 29.67, \"recall_pass\": 81.3, \"unparseable_count\": 6257, \"unparseable_rate\": 63.95, \"n_instances\": 9784, \ndeepseek-cwm-repo-s456-e3-eval | success | {\"accuracy\": 56.11, \"unparseable_rate\": 56.97, \"parseable_only_accuracy\": 32.45, \"f1_macro\": 50.6, \"samples\": 9784}\ndeepseek-cwm-repo-s123 | success | {\"accuracy\": 61.9, \"majority_baseline\": 72.96, \"gap_vs_majority\": -11.06, \"f1_macro\": 51.5, \"f1_pass\": 73.96, \"f1_fail\": 29.04, \"recall_pass\": 74.15, \"recall_fail\": 28.84, \"unparseable_rate\": 65.53, \"total\": 9784, \"correct\": 6056, \"truncated\": 0, \"checkpoint\": \"checkpoint-8844 (epoch 2)\", \"seq_lengt\nqwen3-8b-cwm-repo-s123-train-v4 | success | {\"train_loss\": 0.00873, \"eval_loss\": 0.5166, \"steps_completed\": 6633, \"epochs\": 3, \"training_time_seconds\": 85699}\ndeepseek-cwm-repo-s42-seq4096-eval | success | {\"accuracy\": 61.49, \"unparseable_rate\": 62.5, \"unparseable_count\": 6115, \"n_instances\": 9784, \"f1_macro\": 43.73, \"truncated\": 0, \"truncated_rate\": 0, \"max_generation_tokens\": 284, \"max_new_tokens_limit\": 512, \"seq_length\": 4096}\ndeepseek-cls-repo-s456-eval-v2 | success | {\"accuracy\": 86.15, \"f1_macro\": 80.43, \"f1_fail\": 69.84, \"f1_pass\": 91.01, \"precision_fail\": 84.95, \"recall_fail\": 59.3, \"checkpoint\": \"checkpoint-2163\", \"seq_length\": 8192}\ncls8b-repo-s456-eval-v2 | success | {\"accuracy\": 84.4, \"f1_macro\": 76.19, \"f1_fail\": 62.21, \"f1_pass\": 90.17, \"precision_fail\": 90.23, \"recall_fail\": 47.47, \"checkpoint\": \"checkpoint-2200\", \"seq_length\": 8192}\nqwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval | success | {\"accuracy\": 64.36, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -8.6, \"f1_macro\": 54.42, \"f1_pass\": 75.71, \"f1_fail\": 33.14, \"precision_pass\": 75.3, \"precision_fail\": 33.63, \"recall_pass\": 76.11, \"recall_fail\": 32.65, \"unparseable\": 6236, \"unparseable_rate\": 63.74, \"truncated\": 0, \"truncated_r\ncls8b-s42-ckpt-ablation | success | {\"ckpt-2200\": {\"accuracy\": 85.34, \"f1_macro\": 79.04, \"f1_fail\": 67.56, \"f1_pass\": 90.53}, \"ckpt-3600\": {\"accuracy\": 84.48, \"f1_macro\": 78.17, \"f1_fail\": 66.43, \"f1_pass\": 89.91}, \"ckpt-6633\": {\"accuracy\": 85.29, \"f1_macro\": 78.44, \"f1_fail\": 66.28, \"f1_pass\": 90.6}}\nqwen3-8b-traj-repo-s456 | success | {\"variant_accuracy\": 70.83, \"variant_correct\": 34, \"variant_total\": 48, \"f1_macro\": 70.63, \"overall_accuracy\": 70.83, \"precision_unresolved\": 63.33, \"recall_unresolved\": 86.36, \"f1_unresolved\": 73.08, \"precision_resolved\": 83.33, \"recall_resolved\": 57.69, \"f1_resolved\": 68.18, \"train_loss\": 0.5664, \nqwen3-8b-traj-repo-s123 | success | {\"variant_accuracy\": 77.08, \"variant_correct\": 37, \"variant_total\": 48, \"f1_macro\": 76.59, \"overall_accuracy\": 77.08, \"precision_unresolved\": 78.95, \"recall_unresolved\": 68.18, \"f1_unresolved\": 73.17, \"precision_resolved\": 75.86, \"recall_resolved\": 84.62, \"f1_resolved\": 80, \"train_loss\": 0.5706, \"ev\nexp-downsample-cls-func-v3-eval | success | {\"accuracy\": 80.74, \"f1_macro\": 75.89, \"fail_f1\": 65.1, \"pass_f1\": 86.7, \"unparseable\": 132, \"total\": 9784, \"source\": \"extracted from log (file write failed)\"}\nexp-downsample-cls-func-v3 | success | {\"train_loss\": 0.2869, \"eval_loss_epoch1\": 0.1061, \"eval_loss_epoch2\": 0.0907, \"eval_loss_epoch3\": 0.1156, \"best_epoch\": 2, \"training_time_min\": 44.4}\nexp-e-qwen3-3shot-baseline | success | {\"per_test_accuracy\": 71.61, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -1.35, \"f1_fail\": 61.42, \"f1_pass\": 77.54, \"f1_macro\": 69.48, \"variant_accuracy\": 45.83, \"variant_correct\": 22, \"variant_total\": 48, \"n_instances\": 9784, \"unparseable\": 0, \"truncated\": 0, \"elapsed_min\": 24.6}\nrepo-level-3shot-baseline | success | {\"per_test_accuracy\": 46.28, \"variant_accuracy\": 45.83, \"variant_correct\": 22, \"variant_total\": 48, \"majority_baseline\": 73, \"truncated\": 0, \"unparseable\": 0, \"total\": 9784, \"runtime_min\": 33.8}\nexp-d-constrained-decoding | success | {\"forced_parse\": {\"qwen3_8b\": {\"n\": 9784, \"original_unparseable_rate\": 73.8, \"rescue_rate\": 90.6, \"original_parseable_acc\": 38.5, \"forced_parseable_acc\": 49.4, \"delta_pp\": 10.8}, \"qwen3_4b\": {\"n\": 500, \"original_unparseable_rate\": 75.2, \"rescue_rate\": 77.9, \"original_parseable_acc\": 42.7, \"forced_pa\nexp-b-complexity-bin | success | {\"bins\": {\"23-70\": {\"n_variants\": 12, \"n_tests\": 538, \"cls_qwen3_8b_s123\": 83.3, \"cls_ds_v5\": 91.7, \"cwm_qwen3_8b\": 66.7}, \"71-150\": {\"n_variants\": 14, \"n_tests\": 1282, \"cls_qwen3_8b_s123\": 64.3, \"cls_ds_v5\": 71.4, \"cwm_qwen3_8b\": 42.9}, \"151-250\": {\"n_variants\": 15, \"n_tests\": 2999, \"cls_qwen3_8b_s\nexp-a-routing | success | {\"oracle_routing_7cls\": 100, \"oracle_best_pair\": 95.83, \"test_count_heuristic\": 85.42, \"agreement_confidence\": 83.33, \"majority_vote\": \"75-79%\", \"best_single_cls\": 81.25, \"test_count_heuristic_delta\": \"+4.17pp\", \"oracle_delta\": \"+18.75pp\", \"traj_per_variant\": \"unavailable\", \"cwm_repo_level\": \"45-52%\nqwen3-8b-traj-repo-s42-ckpt98-eval | success | {\"variant_accuracy\": 72.92, \"variant_correct\": 35, \"variant_total\": 48, \"f1_macro\": 72.9, \"fail_recall\": 77.3, \"pass_recall\": 69.2, \"unparseable\": 0, \"note\": \"epoch 2 checkpoint, better class balance than epoch 3\"}\nqwen3-8b-traj-repo-s42-best-eval | success | {\"variant_accuracy\": 70.83, \"variant_correct\": 34, \"variant_total\": 48, \"f1_macro\": 70, \"fail_recall\": 95.5, \"pass_recall\": 50, \"unparseable\": 0, \"note\": \"epoch 3 checkpoint, biased toward predicting unresolved\"}\nqwen3-8b-traj-repo-s42-v2 | success | {\"eval_loss\": \"NaN_all_epochs\", \"total_steps\": 147, \"epochs\": 3, \"seq_length\": 4096, \"best_checkpoint\": \"epoch_3_default_due_to_nan_eval_loss\", \"gradient_checkpointing\": true}\ndeepseek-cls-repo-s123 | success | {\"per_test_accuracy_seq8192\": 74.93, \"per_test_accuracy_seq2048\": 82.62, \"majority_baseline\": 72.96, \"gap_vs_majority_seq8192\": 1.97, \"f1_macro_seq8192\": 53.94, \"f1_fail_seq8192\": 22.84, \"f1_pass_seq8192\": 85.03, \"precision_fail_seq8192\": 68.11, \"recall_fail_seq8192\": 13.72, \"recall_pass_seq8192\": 9\ndeepseek-cls-repo-v5-ckpt6315-eval | success | {\"accuracy\": 82.51, \"fail_recall\": 38.47, \"pass_recall\": 98.84, \"unparseable\": 0, \"n_instances\": 9784, \"confusion\": {\"TN\": 1018, \"FP\": 1628, \"FN\": 83, \"TP\": 7055}, \"variant_accuracy\": 79.17, \"variant_correct\": 38, \"variant_total\": 48, \"variant_fail_recall\": 59.09}\nqwen3-4b-traj-repo-s42-eval | success | {\"variant_accuracy\": 72.92, \"variant_correct\": 35, \"variant_total\": 48, \"f1_macro\": 72.62, \"resolved_precision\": 74.1, \"resolved_recall\": 76.9, \"resolved_f1\": 75.5, \"unresolved_precision\": 71.4, \"unresolved_recall\": 68.2, \"unresolved_f1\": 69.8, \"vs_majority_baseline_pp\": 18.8}\nqwen3-4b-traj-repo-s42 | success | {\"eval_loss_epoch1\": 0.2123, \"eval_loss_epoch2\": 0.1503, \"eval_loss_epoch3\": 0.2249, \"best_epoch\": 2, \"total_steps\": 147}\ndeepseek-cls-repo-v5-ckpt2105-eval | success | {\"accuracy\": 82.61, \"variant_accuracy\": 81.25, \"variant_correct\": 39, \"variant_total\": 48, \"fail_recall\": 51.02, \"pass_recall\": 94.33, \"f1_macro\": 75.07, \"fail_f1\": 61.35, \"pass_f1\": 88.78, \"fail_precision\": 76.92, \"pass_precision\": 83.86, \"unparseable\": 0, \"n_instances\": 9784, \"confusion\": {\"TP\": 6\ndeepseek-cls-repo-v5 | success | {\"train_loss_final\": 0.0399, \"eval_loss_epoch1\": 0.0886, \"eval_loss_epoch2\": 0.1587, \"eval_loss_epoch3\": 0.1975, \"total_steps\": 6315, \"train_time_seconds\": 63312, \"best_checkpoint\": \"checkpoint-2105 (epoch 1)\", \"lora_params\": \"16.8M\"}\ndeepseek-0shot-func-baseline | success | {\"accuracy\": 0.6302, \"pass_f1\": 0.7196, \"fail_f1\": 0.4569, \"unparseable_rate\": 0.0106, \"unparseable_count\": 20, \"total_samples\": 1890, \"runtime_seconds\": 113, \"confusion\": {\"TP\": 897, \"FP\": 618, \"TN\": 294, \"FN\": 81}}\nqwen3-0shot-func-baseline | success | {\"accuracy\": 0.6873, \"pass_f1\": 0.655, \"fail_f1\": 0.7141, \"unparseable_rate\": 0.0032, \"unparseable_count\": 6, \"total_samples\": 1890, \"runtime_seconds\": 96, \"confusion\": {\"TP\": 561, \"FP\": 174, \"TN\": 738, \"FN\": 417}}\ndeepseek-0shot-repo-baseline | success | {\"accuracy\": 0.4854, \"pass_f1\": 0.647, \"fail_f1\": 0.0509, \"unparseable_rate\": 0.087, \"unparseable_count\": 851, \"total_samples\": 9784, \"runtime_seconds\": 1545, \"confusion\": {\"TP\": 4614, \"FP\": 2511, \"TN\": 135, \"FN\": 2524}}\nrepo-level-0shot-baseline | success | {\"accuracy\": 0.499, \"pass_f1\": 0.4895, \"fail_f1\": 0.5081, \"unparseable_rate\": 0, \"unparseable_count\": 0, \"total_samples\": 9784, \"runtime_seconds\": 1018.2, \"confusion\": {\"TP\": 2350, \"FP\": 114, \"TN\": 2532, \"FN\": 4788}}\ndeepseek-cwm-repo | success | {\"train_loss\": 0.021, \"eval_loss\": \"NaN\", \"total_steps\": 13266, \"epochs\": 3, \"wall_clock_seconds\": 112680, \"gpu_hours\": 31.3, \"note\": \"eval_loss=NaN is known DeepSeek issue, does not affect training quality\"}\nqwen3-8b-traj-func-s123 | success | {\"test_accuracy\": 87.79, \"best_eval_loss\": 0.0782, \"pass_f1\": 86.74, \"fail_f1\": 88.69, \"unparseable\": 0, \"per_test_consistency\": 76.07, \"total_steps\": 756, \"test_set_size\": 1032, \"eval_script\": \"eval_traj_verifier_8b.py\"}\nqwen3-8b-traj-func-s42 | success | {\"test_accuracy\": 87.6, \"eval_loss\": 0.0975, \"train_loss\": 0.0312, \"unparseable\": 0, \"pass_f1\": 85.96, \"fail_f1\": 88.89, \"per_test_consistency\": 78.78, \"total_steps\": 756, \"test_set_size\": 1032, \"eval_script\": \"eval_traj_verifier_8b.py\", \"note\": \"87.98% from eval_traj_verifier.py (model.cuda) also v\ndeepseek-cls-func-s123 | success | {\"best_eval_loss\": 0.06753, \"train_time_seconds\": 5391, \"test_accuracy\": 86.77, \"test_f1_macro\": 86.77, \"test_precision_fail\": 84.99, \"test_precision_pass\": 88.56, \"test_recall_fail\": 88.16, \"test_recall_pass\": 85.48, \"test_unparseable_rate\": 0, \"test_n\": 1890}\ndeepseek-cwm-func-s123 | success | {\"best_eval_loss\": 0.0408, \"train_time_seconds\": 5244, \"test_accuracy\": 87.88, \"test_f1_macro\": 87.88, \"test_precision_fail\": 83.78, \"test_precision_pass\": 92.61, \"test_recall_fail\": 92.87, \"test_recall_pass\": 83.23, \"test_unparseable_rate\": 0, \"test_n\": 1890}\ndeepseek-cls-func | success | {\"best_eval_loss\": 0.0701, \"train_time_seconds\": 5444, \"test_accuracy\": 86.93, \"test_f1_macro\": 86.92, \"test_precision_fail\": 86.42, \"test_precision_pass\": 87.41, \"test_recall_fail\": 86.51, \"test_recall_pass\": 87.32, \"test_n\": 1890}\ndeepseek-cwm-func | success | {\"best_eval_loss\": 0.04292, \"train_time_seconds\": 5215, \"test_accuracy\": 85.77, \"test_f1_macro\": 85.73, \"test_precision_fail\": 80.07, \"test_precision_pass\": 93.18, \"test_recall_fail\": 93.86, \"test_recall_pass\": 78.22, \"test_unparseable_rate\": 0, \"test_n\": 1890}\ndeepseek-traj-repo-8k-s999 | success | {\"test_accuracy\": 79.2, \"unparseable\": 0, \"best_eval_loss\": 0.1565, \"resolved_f1\": 82.1, \"unresolved_f1\": 75, \"f1_macro\": 78.57, \"train_loss\": 0.2184}\ndeepseek-traj-repo-8k-s456 | success | {\"test_accuracy\": 75, \"unparseable\": 0, \"best_eval_loss\": 0.1547, \"resolved_f1\": 75, \"unresolved_f1\": 75, \"f1_macro\": 75, \"train_loss\": 0.2176}\ndeepseek-traj-repo-8k-s0 | success | {\"test_accuracy\": 75, \"f1_macro\": 72.68, \"majority_baseline\": 54.2, \"gap_vs_majority_pp\": 20.8, \"unresolved_f1\": 64.7, \"resolved_f1\": 80.6, \"unresolved_precision\": 91.7, \"unresolved_recall\": 50, \"resolved_precision\": 69.4, \"resolved_recall\": 96.2, \"per_test_consistency\": 75, \"unparseable_rate\": 0, \"\ndeepseek-traj-repo-8k-s789 | success | {\"test_accuracy\": 66.67, \"resolved_f1\": 75, \"unresolved_f1\": 50, \"best_eval_loss\": 0.1295, \"unparseable\": 0}\ndeepseek-traj-repo-8k-s123 | success | {\"test_accuracy\": 75, \"unparseable\": 0, \"best_eval_loss\": 0.1182, \"best_epoch\": 2, \"train_truncated_pct\": 2.1, \"gpu_mem_mib\": 21399, \"resolved_f1\": 76.92, \"unresolved_f1\": 72.73}\ndeepseek-traj-repo-8k | success | {\"test_accuracy\": 81.25, \"unparseable\": 0, \"best_eval_loss\": 0.1216, \"best_epoch\": 2, \"train_truncated_pct\": 2.1, \"gpu_mem_mib\": 22475, \"resolved_f1\": 84.21, \"unresolved_f1\": 76.92}\ndeepseek-traj-repo-s123 | success | {\"test_accuracy\": 0.771, \"best_eval_loss\": 0.1147, \"best_step\": 98, \"train_loss\": 0.12, \"unparseable_rate\": 0.167, \"resolved_recall\": 0.962, \"unresolved_recall\": 0.545, \"total_test\": 48}\ndeepseek-traj-repo | success | {\"test_accuracy\": 0.771, \"best_eval_loss\": 0.111, \"best_step\": 98, \"train_loss\": 0.12, \"unparseable_rate\": 0.167, \"resolved_recall\": 0.962, \"unresolved_recall\": 0.545, \"total_test\": 48}\ndeepseek-traj-func-v2-s123 | success | {\"best_eval_loss\": 0.077, \"best_step\": 504, \"test_accuracy\": 0.8508, \"majority_baseline\": 0.5359, \"train_loss\": 0.0842, \"train_runtime_seconds\": 3021, \"per_test_consistency\": 0.782}\ndeepseek-traj-func-v2 | success | {\"best_eval_loss\": 0.0796, \"best_step\": 504, \"test_accuracy\": 0.8324, \"majority_baseline\": 0.5359, \"train_loss\": 0.0857, \"train_runtime_seconds\": 3069.6}\ndeepseek-traj-func | success | {\"eval_loss_epoch1\": 0.0943, \"eval_loss_epoch2\": 0.0793, \"eval_loss_epoch3\": 0.0884, \"best_eval_loss\": 0.0793, \"best_step\": 1008, \"best_epoch\": 2, \"train_loss\": 0.1131, \"train_runtime_sec\": 2910.6}\ncwm4b-s42-mutation-breakdown | success | {\"overall_accuracy\": 58.04, \"parseable_rate\": 46.3, \"parseable_only_accuracy\": 42.9, \"gold_parse_rate\": 43.5, \"gold_parseable_acc\": 23.5, \"operator_swap_parse_rate\": 56.9, \"operator_swap_parseable_acc\": 63.1, \"off_by_one_parse_rate\": 4.4, \"off_by_one_parseable_acc\": 0, \"return_value_parse_rate\": 48.\ncls4b-ckpt4600-test-mutation-pr | success | {\"accuracy\": 83.63, \"gold_acc\": 98.25, \"operator_swap_acc\": 78.91, \"return_value_acc\": 67.97, \"off_by_one_acc\": 58.47, \"boundary_removal_acc\": 46.9, \"n_instances\": 9784, \"note\": \"off_by_one recall_fail=0 (all predicted pass); boundary_removal identical to 8B\"}\ncls8b-seed123-ckpt3000-mutation | success | {\"accuracy\": 85.6, \"boundary_removal\": 44.9, \"operator_swap\": 82.6, \"return_value\": 66.4, \"off_by_one\": 79.2, \"gold\": 99.6, \"n_samples\": 9784}\ncls8b-s42-resume-ckpt3600-test-v2 | success | {\"accuracy\": 84.48, \"f1_macro\": 78.17, \"fail_recall\": 56.8, \"pass_recall\": 94.8, \"n_samples\": 9784, \"note\": \"reproduces v1 exactly\"}\ncls8b-s42-resume-ckpt3600-mutation | success | {\"overall_accuracy\": 84.4849, \"overall_correct\": 8266, \"overall_total\": 9784, \"gold_accuracy\": 96.2443, \"gold_correct\": 4459, \"gold_total\": 4633, \"mutation_operator_swap_accuracy\": 81.3822, \"mutation_operator_swap_correct\": 2732, \"mutation_operator_swap_total\": 3357, \"mutation_off_by_one_accuracy\": \ncls8b-s42-ckpt3600-seq2048-ablation | success | {\"accuracy\": 83.04, \"f1_macro\": 76.8, \"unparseable\": 136, \"n_samples\": 9784, \"seq_length\": 2048}\nrepo-level-cls-8b-s42-resume | success | {\"total_steps\": 6633, \"epochs\": 3, \"train_time_sec\": 74425, \"final_train_loss\": 0.4284, \"final_eval_loss\": 0.4768, \"best_eval_loss_resume\": 0.2516, \"best_eval_loss_resume_step\": 4200, \"best_eval_loss_overall\": 0.0796, \"best_eval_loss_overall_step\": 200, \"checkpoints_saved\": 32, \"overfitting\": true, \ncwm-rank32-alpha64-ablation | success | {\"accuracy\": 87.04, \"pass_f1\": 86.79, \"fail_f1\": 87.27, \"f1_macro\": 87.03, \"pass_precision\": 91.8, \"pass_recall\": 82.3, \"fail_precision\": 82.9, \"fail_recall\": 92.1, \"exact_match_rate\": 84.55, \"train_loss\": 0.2069, \"eval_loss\": 0.0606, \"n_instances\": 1890, \"vs_rank16_baseline\": -0.47, \"rank16_baselin\ncls8b-seed123-ckpt6200-test-eval-v2 | success | {\"accuracy\": 84.7, \"f1_fail\": 63.71, \"f1_pass\": 90.31, \"f1_macro\": 77.01, \"precision_fail\": 88.84, \"precision_pass\": 83.96, \"recall_fail\": 49.66, \"recall_pass\": 97.69, \"n_instances\": 9784, \"n_cls_unparseable\": 0}\ncwm-rank32-ablation-v2 | success | {\"accuracy\": 87, \"exact_match_rate\": 83.4, \"fail_f1\": 87.1, \"pass_f1\": 86.9, \"train_loss_final\": 0.0152, \"train_loss_avg\": 0.2536, \"eval_loss\": 0.0688, \"train_runtime_sec\": 5003, \"test_set_size\": 1890, \"vs_rank16_baseline\": -0.51, \"rank16_baseline_accuracy\": 87.51}\ncls8b-seed123-ckpt200-test-eval | success | {\"accuracy\": 72.55, \"f1_macro\": 70.18, \"pass_f1\": 78.58, \"fail_f1\": 61.78, \"pass_precision\": 91.21, \"pass_recall\": 69.02, \"fail_precision\": 49.54, \"fail_recall\": 82.05, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 72.96, \"unparseable\": 0, \"confusion_matrix\": {\"tn\": 2171, \"\ncls8b-s42-ckpt1000-test-seq2048-ablation | success | {\"accuracy\": 82.83, \"f1_macro\": 76.88, \"fail_precision\": 72.2, \"fail_recall\": 59.3, \"fail_f1\": 65.2, \"pass_precision\": 85.9, \"pass_recall\": 91.5, \"pass_f1\": 88.6, \"unparseable\": 136}\ncls8b-seed123-ckpt6633-test-eval | success | {\"accuracy\": 84.89, \"f1_macro\": 77.56, \"f1_fail\": 64.7, \"f1_pass\": 90.4, \"precision_fail\": 87.8, \"recall_fail\": 51.2, \"precision_pass\": 84.3, \"recall_pass\": 97.4, \"majority_baseline\": 73, \"gap_vs_majority_pp\": 11.9, \"total_samples\": 9784, \"unparseable_count\": 0}\ncls8b-seed123-ckpt6600-test-eval | success | {\"accuracy\": 84.9, \"f1_macro\": 77.58, \"pass_f1\": 90.4, \"fail_f1\": 64.8, \"pass_precision\": 84.3, \"pass_recall\": 97.4, \"fail_precision\": 87.8, \"fail_recall\": 51.3, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 73, \"unparseable\": 0, \"confusion_matrix\": {\"fail_as_fail\": 1357, \"\ncls8b-s42-ckpt200-test8192-eval | success | {\"accuracy\": 70.07, \"f1_macro\": 68.18, \"pass_f1\": 75.9, \"fail_f1\": 60.4, \"pass_precision\": 91.8, \"pass_recall\": 64.7, \"fail_precision\": 47, \"fail_recall\": 84.5, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 73, \"unparseable\": 0, \"confusion_matrix\": {\"fail_as_fail\": 2235, \"f\ncls4b-v5-ckpt600-test5120-eval | success | {\"accuracy\": 77.74, \"f1_macro\": 74.74, \"f1_fail\": 66.03, \"f1_pass\": 83.44, \"precision_fail\": 56.21, \"recall_fail\": 80.01, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 4.78, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-seed123-ckpt6400-test-eval-v2 | success | {\"accuracy\": 85.08, \"f1_fail\": 65.32, \"f1_pass\": 90.49, \"f1_macro\": 77.91, \"precision_fail\": 87.92, \"precision_pass\": 84.54, \"recall_fail\": 51.97, \"recall_pass\": 97.35, \"n_instances\": 9784, \"n_cls_unparseable\": 0}\ncls8b-seed123-ckpt6633-val8192-eval | success | {\"accuracy\": 87.1, \"f1_macro\": 78.79, \"f1_fail\": 65.52, \"f1_pass\": 92.07, \"precision_fail\": 92.26, \"recall_fail\": 50.8, \"precision_pass\": 86.31, \"recall_pass\": 98.64, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.23, \"unparseable_count\": 9, \"total_samples\": 9335}\ncls8b-seed123-ckpt3000-test8192-eval | success | {\"accuracy\": 85.6, \"f1_macro\": 78.38, \"f1_fail\": 65.89, \"f1_pass\": 90.87, \"precision_fail\": 91.65, \"recall_fail\": 51.44, \"precision_pass\": 84.52, \"recall_pass\": 98.26, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.64, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls4b-v5-ckpt4400-test5120-eval | success | {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_fail\": 59.45, \"f1_pass\": 89.44, \"precision_fail\": 85.98, \"recall_fail\": 45.43, \"precision_pass\": 82.78, \"recall_pass\": 97.25, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.28, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-seed123-ckpt6400-val8192-eval | success | {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_fail\": 67.04, \"f1_pass\": 92.27, \"precision_fail\": 91.81, \"recall_fail\": 52.8, \"precision_pass\": 86.78, \"recall_pass\": 98.5, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.6, \"unparseable_count\": 9, \"total_samples\": 9335}\ncls8b-seed123-ckpt6200-val8192-eval | success | {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_fail\": 66.16, \"f1_pass\": 92.35, \"precision_fail\": 95.63, \"recall_fail\": 50.58, \"precision_pass\": 86.33, \"recall_pass\": 99.27, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.64, \"unparseable_count\": 9, \"total_samples\": 9335}\ncls4b-v5-val-sweep-ckpt4600 | success | {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_fail\": 76.37, \"f1_pass\": 93.71, \"precision_fail\": 89.65, \"recall_fail\": 66.52, \"precision_pass\": 90.16, \"recall_pass\": 97.56, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 14.19, \"unparseable_count\": 0, \"total_samples\": 9335, \"n_truncated\": 234}\ncls8b-seed123-ckpt6600-val8192-eval | success | {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_fail\": 65.9, \"f1_pass\": 92.14, \"precision_fail\": 92.6, \"recall_fail\": 51.15, \"precision_pass\": 86.4, \"recall_pass\": 98.7, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.36, \"unparseable_count\": 9, \"total_samples\": 9335}\ncls8b-s42-ckpt1600-test8192-eval | success | {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_fail\": 67.65, \"f1_pass\": 90.22, \"precision_fail\": 81.06, \"recall_fail\": 58.05, \"precision_pass\": 85.93, \"recall_pass\": 94.97, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.03, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls4b-v5-ckpt4600-test-eval | success | {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_fail\": 61.67, \"f1_pass\": 89.59, \"precision_fail\": 84.03, \"recall_fail\": 48.72, \"precision_pass\": 83.55, \"recall_pass\": 96.57, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.67, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-s42-ckpt1400-test8192-eval | success | {\"accuracy\": 85.47, \"f1_macro\": 78.9, \"f1_fail\": 67.13, \"f1_pass\": 90.67, \"precision_fail\": 86.43, \"recall_fail\": 54.88, \"precision_pass\": 85.27, \"recall_pass\": 96.81, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.51, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-s42-ckpt1200-test8192-eval | success | {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_fail\": 65.49, \"f1_pass\": 89.45, \"precision_fail\": 77.52, \"recall_fail\": 56.69, \"precision_pass\": 85.4, \"recall_pass\": 93.91, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.89, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-s42-ckpt800-test8192-eval | success | {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_fail\": 69.17, \"f1_pass\": 88.77, \"precision_fail\": 70.07, \"recall_fail\": 68.29, \"precision_pass\": 88.36, \"recall_pass\": 89.18, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.58, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls4b-v5-val-sweep-ckpt4200 | success | {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_fail\": 73, \"f1_pass\": 93.1, \"precision_fail\": 90.3, \"recall_fail\": 61.3, \"precision_pass\": 88.8, \"recall_pass\": 97.9}\ncls8b-s42-ckpt1600-val8192-v2 | success | {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_fail\": 66.12, \"f1_pass\": 91.76, \"precision_fail\": 86.28, \"precision_pass\": 86.83, \"recall_fail\": 53.6, \"recall_pass\": 97.29, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 10.87, \"unparseable\": 9, \"total\": 9335}\ncls8b-s42-ckpt1400-val8192-eval | success | {\"accuracy\": 85.97, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 10.09, \"f1_macro\": 77.15, \"f1_fail\": 62.95, \"f1_pass\": 91.34, \"precision_fail\": 86.68, \"precision_pass\": 85.85, \"recall_fail\": 49.42, \"recall_pass\": 97.59, \"n_instances\": 9335, \"n_unparseable\": 9, \"confusion_matrix\": {\"tn\": 1113, \ncls4b-v5-val-sweep-ckpt4400-v3 | success | {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_fail\": 76.25, \"f1_pass\": 93.64, \"precision_fail\": 88.84, \"precision_pass\": 90.21, \"recall_fail\": 66.79, \"recall_pass\": 97.33, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 14.09, \"n_instances\": 9335, \"n_truncated\": 234, \"n_unparseable\": 0}\ncls8b-s42-ckpt1200-val8192-v3 | success | {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_fail\": 70.2, \"f1_pass\": 92.3, \"precision_fail\": 85, \"recall_fail\": 59.8, \"precision_pass\": 88.3, \"recall_pass\": 96.7, \"majority_baseline\": 75.9, \"gap_vs_majority\": 11.9, \"unparseable\": 9}\ncls8b-s42-ckpt1000-test8192-eval | success | {\"accuracy\": 83.52, \"f1_macro\": 77.5, \"f1_fail\": 65.85, \"f1_pass\": 89.14, \"precision_fail\": 74.93, \"recall_fail\": 58.73, \"precision_pass\": 85.84, \"recall_pass\": 92.72, \"majority_baseline\": 72.96, \"gap_vs_majority\": 10.56, \"unparseable_count\": 0, \"unparseable_rate\": 0, \"total_samples\": 9784, \"tp\": 66\ncls8b-s42-ckpt1000-val8192-eval | success | {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_fail\": 73, \"f1_pass\": 92.5, \"precision_fail\": 81.8, \"recall_fail\": 65.8, \"precision_pass\": 89.8, \"recall_pass\": 95.3, \"unparseable\": 9, \"total_instances\": 9335}\ncls8b-s42-ckpt800-val8192-eval | success | {\"accuracy\": 84.5, \"f1_macro\": 79.2}\ncls4b-v5-ckpt4000-val5120-eval | success | {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_fail\": 74.85, \"f1_pass\": 93.64, \"precision_fail\": 92.95, \"recall_fail\": 62.66, \"precision_pass\": 89.24, \"recall_pass\": 98.49, \"unparseable\": 0, \"truncated\": 234, \"total\": 9335}\ncls4b-v5-ckpt600-val5120-eval | success | {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_fail\": 72.03, \"f1_pass\": 87.6, \"precision_fail\": 59.3, \"recall_fail\": 91.7, \"unparseable\": 0, \"total\": 9335}\nrepo-level-cls-8b-conda | success | {\"val_8192\": {\"ckpt_200\": {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_fail\": 51.6, \"f1_pass\": 70.7, \"unparseable\": 9}, \"ckpt_400\": {\"accuracy\": 80.96}, \"ckpt_600\": {\"accuracy\": 85}, \"best_acc\": \"ckpt_600\"}, \"val_5120\": {\"ckpt_400\": {\"accuracy\": 80.47, \"f1_macro\": 75.84}}, \"test_2048\": {\"ckpt_400\": {\"\ncls8b-s42-ckpt200-val8192-eval-v2 | success | {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_fail\": 51.6, \"f1_pass\": 70.7, \"unparseable\": 9, \"total\": 9335}\ncls4b-seed123-ckpt800-val5120-eval | success | {\"accuracy\": 87.92, \"f1_macro\": 81.95, \"f1_pass\": 92.33, \"f1_fail\": 71.57, \"unparseable\": 0, \"truncated\": 234, \"total\": 9335}\nrepo-level-cls-seed123-home | success | {\"val_2048\": {\"n\": 9335, \"unparseable\": 1883, \"ckpt_200\": {\"accuracy\": 62.51, \"f1_macro\": 55.54, \"f1_pass\": 73.14, \"f1_fail\": 37.94}, \"ckpt_400\": {\"accuracy\": 80.72, \"f1_macro\": 67.03, \"f1_pass\": 88.27, \"f1_fail\": 45.78}, \"ckpt_600\": {\"accuracy\": 76.78, \"f1_macro\": 66.81, \"f1_pass\": 85, \"f1_fail\": 4\ncls8b-s42-ckpt600-test8192-eval | success | {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_fail\": 65.24, \"f1_pass\": 85, \"precision_fail\": 59.16, \"precision_pass\": 88.95, \"recall_fail\": 72.71, \"recall_pass\": 81.4, \"unparseable\": 0, \"total\": 9784, \"majority_baseline\": 73, \"gap_vs_majority_pp\": 6.09}\ncls8b-seed123-ckpt3000-val8192-eval | success | {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_fail\": 70.5, \"f1_pass\": 93, \"precision_fail\": 95.2, \"precision_pass\": 87.6, \"recall_fail\": 55.9, \"recall_pass\": 99.1, \"majority_baseline\": 75.9, \"gap_vs_majority_pp\": 12.8, \"unparseable\": 9, \"total\": 9335}\ncls8b-s42-ckpt400-test8192-eval | success | {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_fail\": 72.93, \"f1_pass\": 89.43, \"precision_fail\": 70.32, \"precision_pass\": 90.74, \"recall_fail\": 75.74, \"recall_pass\": 88.15, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 11.84, \"unparseable\": 0, \"total\": 9784}\nrepo-level-cls-v5 | success | {\"checkpoint_sweep\": {\"ckpt_600\": {\"accuracy\": 76.74, \"f1_macro\": 73.74, \"fail_f1\": 64.88, \"pass_f1\": 82.61}, \"ckpt_4000\": {\"accuracy\": 81.51, \"f1_macro\": 72.56, \"fail_f1\": 56.9, \"pass_f1\": 88.23}, \"ckpt_4200\": {\"accuracy\": 80.64, \"f1_macro\": 72.1, \"fail_f1\": 56.66, \"pass_f1\": 87.54}, \"ckpt_4400\": {\nrepo-level-cls-v5-conda | success | {\"checkpoint_sweep\": {\"ckpt_200\": {\"accuracy\": 52.96, \"f1_macro\": 52.89, \"fail_f1\": 51.02, \"pass_f1\": 54.76}, \"ckpt_400\": {\"accuracy\": 78.43, \"f1_macro\": 68.41, \"fail_f1\": 50.61, \"pass_f1\": 86.21, \"fail_precision\": 66.48, \"fail_recall\": 40.85, \"pass_precision\": 80.82, \"pass_recall\": 92.36}, \"ckpt_60\nrepo-level-cwm-v10 | success | {\"accuracy\": 0.6991, \"f1_macro\": 0.4671, \"f1_pass\": 0.8187, \"f1_fail\": 0.1154,",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/bofsph3hk.txt",
    "persistedOutputSize": 38474
  }
}
```

</details>

---


### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01KgdiV8QsM4xZCVbnPz9Rqt`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/bofsph3hk.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "1e7a43b6-c50c-457f-998f-552ecaed0747",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A14R7Pn5WppW6nvMLbNeeT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 73521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1176
      },
      "output_tokens": 66,
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

_source line 56 · 2026-05-23T19:18:09.772Z_

<details><summary>↩ Tool result · `toolu_01KgdiV8QsM4xZCVbnPz9Rqt`</summary>

```text
1	Total experiments: 152
2	deepseek-cwm-repo-s456-train-v2 | success | {"train_loss": 0.02127, "eval_loss": 5.2837, "total_steps": 12627, "training_time_hours": 27.55}
3	traj14b-func-s456 | success | {"best_eval_loss": 0.0971, "best_checkpoint": "best", "epochs": 3, "accuracy": 88.28, "dtype": "bf16", "n_test": 1032}
4	traj14b-func-s123 | success | {"best_eval_loss": 0.0836, "best_checkpoint": "checkpoint-252", "epochs": 3, "accuracy": 88.57, "dtype": "bf16", "n_test": 1032}
5	traj14b-func-s42 | success | {"best_eval_loss": 0.0958, "best_checkpoint": "best", "epochs": 3, "accuracy": 89.73, "dtype": "bf16", "n_test": 1032}
6	cwm14b-func-s456 | success | {"accuracy": 90.26, "unparseable": 0, "best_checkpoint": "best", "dtype": "bf16", "n_test": 1890}
7	cwm14b-func-s123 | success | {"accuracy": 88.99, "unparseable": 0, "best_checkpoint": "best", "dtype": "bf16", "n_test": 1890}
8	cls14b-func-s456 | success | {"accuracy": 89.79, "f1_fail": 89.45, "f1_pass": 90.11, "precision_fail": 89.2, "recall_fail": 89.69, "precision_pass": 90.34, "recall_pass": 89.88, "unparseable": 0, "best_checkpoint": "checkpoint-478", "dtype": "bf16", "best_train_loss": 0.0659}
9	cls14b-func-s123 | success | {"accuracy": 90.79, "f1_fail": 90.58, "f1_pass": 90.99, "precision_fail": 89.42, "recall_fail": 91.78, "precision_pass": 92.14, "recall_pass": 89.88, "unparseable": 0, "best_checkpoint": "checkpoint-956", "dtype": "bf16", "best_train_loss": 0.063}
10	cls14b-func-s42-v2 | success | {"accuracy": 89.47, "f1_fail": 89.02, "f1_pass": 89.88, "unparseable": 0, "checkpoint": "checkpoint-956", "delta_vs_8b": -0.47, "cls_cwm_gap_14b": 0.21}
11	cwm14b-func-s42 | success | {"accuracy": 89.3, "f1_fail": 88.3, "f1_pass": 90.1, "exact_match_rate": 86.6, "unparseable": 0, "checkpoint": "checkpoint-956", "delta_vs_8b": 1.97}
12	8b-baseline-rerun | success | {"0shot_accuracy": 60.53, "0shot_f1_macro": 55.73, "3shot_accuracy": 60.42, "3shot_f1_macro": 56.09, "0shot_unparseable": 5, "3shot_unparseable": 1}
13	14b-baseline-0shot-3shot-v2 | success | {"0shot": {"accuracy": 66.24, "gap_vs_majority": 14.5, "f1_fail": 72.99, "f1_pass": 55.01, "f1_macro": 64, "unparseable": 0, "n": 1890}, "3shot": {"accuracy": 73.12, "gap_vs_majority": 21.38, "f1_fail": 75.79, "f1_pass": 69.8, "f1_macro": 72.79, "unparseable": 0, "n": 1890}}
14	deepseek-cwm-repo-s123-eval-1epoch | success | {"accuracy": 75.45, "f1_macro": 65.08, "f1_fail": 46.05, "f1_pass": 84.11, "unparseable_rate": 66.4, "unparseable_count": 6500, "n_instances": 9784, "majority_baseline": 72.96, "gap_vs_majority_pp": 2.49, "truncated": 0}
15	qwen3-8b-cwm-repo-s456-eval | success | {"accuracy": 66.93, "f1_macro": 51.97, "f1_fail": 25.16, "f1_pass": 78.77, "unparseable_rate": 60.39, "unparseable_count": 5909, "n_instances": 9784, "majority_baseline": 72.96, "gap_vs_majority_pp": -6.03, "precision_fail": 32.42, "recall_fail": 20.56, "checkpoint_step": 6633}
16	deepseek-cwm-repo-s123-e3-eval | success | {"accuracy": 57.31, "f1_macro": 51.79, "f1_fail": 35.49, "f1_pass": 68.1, "precision_fail": 30.01, "precision_pass": 74.86, "recall_fail": 43.42, "recall_pass": 62.45, "unparseable_count": 5028, "unparseable_rate": 51.39, "n_instances": 9784, "majority_baseline": 72.96, "gap_vs_majority_pp": -15.65}
17	qwen3-8b-cwm-repo-s123-eval | success | {"accuracy": 67.33, "majority_baseline": 72.96, "gap_vs_majority_pp": -5.62, "f1_fail": 32.94, "f1_pass": 78.41, "f1_macro": 55.67, "precision_fail": 37.03, "precision_pass": 75.72, "recall_fail": 29.67, "recall_pass": 81.3, "unparseable_count": 6257, "unparseable_rate": 63.95, "n_instances": 9784, 
18	deepseek-cwm-repo-s456-e3-eval | success | {"accuracy": 56.11, "unparseable_rate": 56.97, "parseable_only_accuracy": 32.45, "f1_macro": 50.6, "samples": 9784}
19	deepseek-cwm-repo-s123 | success | {"accuracy": 61.9, "majority_baseline": 72.96, "gap_vs_majority": -11.06, "f1_macro": 51.5, "f1_pass": 73.96, "f1_fail": 29.04, "recall_pass": 74.15, "recall_fail": 28.84, "unparseable_rate": 65.53, "total": 9784, "correct": 6056, "truncated": 0, "checkpoint": "checkpoint-8844 (epoch 2)", "seq_lengt
20	qwen3-8b-cwm-repo-s123-train-v4 | success | {"train_loss": 0.00873, "eval_loss": 0.5166, "steps_completed": 6633, "epochs": 3, "training_time_seconds": 85699}
21	deepseek-cwm-repo-s42-seq4096-eval | success | {"accuracy": 61.49, "unparseable_rate": 62.5, "unparseable_count": 6115, "n_instances": 9784, "f1_macro": 43.73, "truncated": 0, "truncated_rate": 0, "max_generation_tokens": 284, "max_new_tokens_limit": 512, "seq_length": 4096}
22	deepseek-cls-repo-s456-eval-v2 | success | {"accuracy": 86.15, "f1_macro": 80.43, "f1_fail": 69.84, "f1_pass": 91.01, "precision_fail": 84.95, "recall_fail": 59.3, "checkpoint": "checkpoint-2163", "seq_length": 8192}
23	cls8b-repo-s456-eval-v2 | success | {"accuracy": 84.4, "f1_macro": 76.19, "f1_fail": 62.21, "f1_pass": 90.17, "precision_fail": 90.23, "recall_fail": 47.47, "checkpoint": "checkpoint-2200", "seq_length": 8192}
24	qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval | success | {"accuracy": 64.36, "majority_baseline": 72.96, "gap_vs_majority_pp": -8.6, "f1_macro": 54.42, "f1_pass": 75.71, "f1_fail": 33.14, "precision_pass": 75.3, "precision_fail": 33.63, "recall_pass": 76.11, "recall_fail": 32.65, "unparseable": 6236, "unparseable_rate": 63.74, "truncated": 0, "truncated_r
25	cls8b-s42-ckpt-ablation | success | {"ckpt-2200": {"accuracy": 85.34, "f1_macro": 79.04, "f1_fail": 67.56, "f1_pass": 90.53}, "ckpt-3600": {"accuracy": 84.48, "f1_macro": 78.17, "f1_fail": 66.43, "f1_pass": 89.91}, "ckpt-6633": {"accuracy": 85.29, "f1_macro": 78.44, "f1_fail": 66.28, "f1_pass": 90.6}}
26	qwen3-8b-traj-repo-s456 | success | {"variant_accuracy": 70.83, "variant_correct": 34, "variant_total": 48, "f1_macro": 70.63, "overall_accuracy": 70.83, "precision_unresolved": 63.33, "recall_unresolved": 86.36, "f1_unresolved": 73.08, "precision_resolved": 83.33, "recall_resolved": 57.69, "f1_resolved": 68.18, "train_loss": 0.5664, 
27	qwen3-8b-traj-repo-s123 | success | {"variant_accuracy": 77.08, "variant_correct": 37, "variant_total": 48, "f1_macro": 76.59, "overall_accuracy": 77.08, "precision_unresolved": 78.95, "recall_unresolved": 68.18, "f1_unresolved": 73.17, "precision_resolved": 75.86, "recall_resolved": 84.62, "f1_resolved": 80, "train_loss": 0.5706, "ev
28	exp-downsample-cls-func-v3-eval | success | {"accuracy": 80.74, "f1_macro": 75.89, "fail_f1": 65.1, "pass_f1": 86.7, "unparseable": 132, "total": 9784, "source": "extracted from log (file write failed)"}
29	exp-downsample-cls-func-v3 | success | {"train_loss": 0.2869, "eval_loss_epoch1": 0.1061, "eval_loss_epoch2": 0.0907, "eval_loss_epoch3": 0.1156, "best_epoch": 2, "training_time_min": 44.4}
30	exp-e-qwen3-3shot-baseline | success | {"per_test_accuracy": 71.61, "majority_baseline": 72.96, "gap_vs_majority_pp": -1.35, "f1_fail": 61.42, "f1_pass": 77.54, "f1_macro": 69.48, "variant_accuracy": 45.83, "variant_correct": 22, "variant_total": 48, "n_instances": 9784, "unparseable": 0, "truncated": 0, "elapsed_min": 24.6}
31	repo-level-3shot-baseline | success | {"per_test_accuracy": 46.28, "variant_accuracy": 45.83, "variant_correct": 22, "variant_total": 48, "majority_baseline": 73, "truncated": 0, "unparseable": 0, "total": 9784, "runtime_min": 33.8}
32	exp-d-constrained-decoding | success | {"forced_parse": {"qwen3_8b": {"n": 9784, "original_unparseable_rate": 73.8, "rescue_rate": 90.6, "original_parseable_acc": 38.5, "forced_parseable_acc": 49.4, "delta_pp": 10.8}, "qwen3_4b": {"n": 500, "original_unparseable_rate": 75.2, "rescue_rate": 77.9, "original_parseable_acc": 42.7, "forced_pa
33	exp-b-complexity-bin | success | {"bins": {"23-70": {"n_variants": 12, "n_tests": 538, "cls_qwen3_8b_s123": 83.3, "cls_ds_v5": 91.7, "cwm_qwen3_8b": 66.7}, "71-150": {"n_variants": 14, "n_tests": 1282, "cls_qwen3_8b_s123": 64.3, "cls_ds_v5": 71.4, "cwm_qwen3_8b": 42.9}, "151-250": {"n_variants": 15, "n_tests": 2999, "cls_qwen3_8b_s
34	exp-a-routing | success | {"oracle_routing_7cls": 100, "oracle_best_pair": 95.83, "test_count_heuristic": 85.42, "agreement_confidence": 83.33, "majority_vote": "75-79%", "best_single_cls": 81.25, "test_count_heuristic_delta": "+4.17pp", "oracle_delta": "+18.75pp", "traj_per_variant": "unavailable", "cwm_repo_level": "45-52%
35	qwen3-8b-traj-repo-s42-ckpt98-eval | success | {"variant_accuracy": 72.92, "variant_correct": 35, "variant_total": 48, "f1_macro": 72.9, "fail_recall": 77.3, "pass_recall": 69.2, "unparseable": 0, "note": "epoch 2 checkpoint, better class balance than epoch 3"}
36	qwen3-8b-traj-repo-s42-best-eval | success | {"variant_accuracy": 70.83, "variant_correct": 34, "variant_total": 48, "f1_macro": 70, "fail_recall": 95.5, "pass_recall": 50, "unparseable": 0, "note": "epoch 3 checkpoint, biased toward predicting unresolved"}
37	qwen3-8b-traj-repo-s42-v2 | success | {"eval_loss": "NaN_all_epochs", "total_steps": 147, "epochs": 3, "seq_length": 4096, "best_checkpoint": "epoch_3_default_due_to_nan_eval_loss", "gradient_checkpointing": true}
38	deepseek-cls-repo-s123 | success | {"per_test_accuracy_seq8192": 74.93, "per_test_accuracy_seq2048": 82.62, "majority_baseline": 72.96, "gap_vs_majority_seq8192": 1.97, "f1_macro_seq8192": 53.94, "f1_fail_seq8192": 22.84, "f1_pass_seq8192": 85.03, "precision_fail_seq8192": 68.11, "recall_fail_seq8192": 13.72, "recall_pass_seq8192": 9
39	deepseek-cls-repo-v5-ckpt6315-eval | success | {"accuracy": 82.51, "fail_recall": 38.47, "pass_recall": 98.84, "unparseable": 0, "n_instances": 9784, "confusion": {"TN": 1018, "FP": 1628, "FN": 83, "TP": 7055}, "variant_accuracy": 79.17, "variant_correct": 38, "variant_total": 48, "variant_fail_recall": 59.09}
40	qwen3-4b-traj-repo-s42-eval | success | {"variant_accuracy": 72.92, "variant_correct": 35, "variant_total": 48, "f1_macro": 72.62, "resolved_precision": 74.1, "resolved_recall": 76.9, "resolved_f1": 75.5, "unresolved_precision": 71.4, "unresolved_recall": 68.2, "unresolved_f1": 69.8, "vs_majority_baseline_pp": 18.8}
41	qwen3-4b-traj-repo-s42 | success | {"eval_loss_epoch1": 0.2123, "eval_loss_epoch2": 0.1503, "eval_loss_epoch3": 0.2249, "best_epoch": 2, "total_steps": 147}
42	deepseek-cls-repo-v5-ckpt2105-eval | success | {"accuracy": 82.61, "variant_accuracy": 81.25, "variant_correct": 39, "variant_total": 48, "fail_recall": 51.02, "pass_recall": 94.33, "f1_macro": 75.07, "fail_f1": 61.35, "pass_f1": 88.78, "fail_precision": 76.92, "pass_precision": 83.86, "unparseable": 0, "n_instances": 9784, "confusion": {"TP": 6
43	deepseek-cls-repo-v5 | success | {"train_loss_final": 0.0399, "eval_loss_epoch1": 0.0886, "eval_loss_epoch2": 0.1587, "eval_loss_epoch3": 0.1975, "total_steps": 6315, "train_time_seconds": 63312, "best_checkpoint": "checkpoint-2105 (epoch 1)", "lora_params": "16.8M"}
44	deepseek-0shot-func-baseline | success | {"accuracy": 0.6302, "pass_f1": 0.7196, "fail_f1": 0.4569, "unparseable_rate": 0.0106, "unparseable_count": 20, "total_samples": 1890, "runtime_seconds": 113, "confusion": {"TP": 897, "FP": 618, "TN": 294, "FN": 81}}
45	qwen3-0shot-func-baseline | success | {"accuracy": 0.6873, "pass_f1": 0.655, "fail_f1": 0.7141, "unparseable_rate": 0.0032, "unparseable_count": 6, "total_samples": 1890, "runtime_seconds": 96, "confusion": {"TP": 561, "FP": 174, "TN": 738, "FN": 417}}
46	deepseek-0shot-repo-baseline | success | {"accuracy": 0.4854, "pass_f1": 0.647, "fail_f1": 0.0509, "unparseable_rate": 0.087, "unparseable_count": 851, "total_samples": 9784, "runtime_seconds": 1545, "confusion": {"TP": 4614, "FP": 2511, "TN": 135, "FN": 2524}}
47	repo-level-0shot-baseline | success | {"accuracy": 0.499, "pass_f1": 0.4895, "fail_f1": 0.5081, "unparseable_rate": 0, "unparseable_count": 0, "total_samples": 9784, "runtime_seconds": 1018.2, "confusion": {"TP": 2350, "FP": 114, "TN": 2532, "FN": 4788}}
48	deepseek-cwm-repo | success | {"train_loss": 0.021, "eval_loss": "NaN", "total_steps": 13266, "epochs": 3, "wall_clock_seconds": 112680, "gpu_hours": 31.3, "note": "eval_loss=NaN is known DeepSeek issue, does not affect training quality"}
49	qwen3-8b-traj-func-s123 | success | {"test_accuracy": 87.79, "best_eval_loss": 0.0782, "pass_f1": 86.74, "fail_f1": 88.69, "unparseable": 0, "per_test_consistency": 76.07, "total_steps": 756, "test_set_size": 1032, "eval_script": "eval_traj_verifier_8b.py"}
50	qwen3-8b-traj-func-s42 | success | {"test_accuracy": 87.6, "eval_loss": 0.0975, "train_loss": 0.0312, "unparseable": 0, "pass_f1": 85.96, "fail_f1": 88.89, "per_test_consistency": 78.78, "total_steps": 756, "test_set_size": 1032, "eval_script": "eval_traj_verifier_8b.py", "note": "87.98% from eval_traj_verifier.py (model.cuda) also v
51	deepseek-cls-func-s123 | success | {"best_eval_loss": 0.06753, "train_time_seconds": 5391, "test_accuracy": 86.77, "test_f1_macro": 86.77, "test_precision_fail": 84.99, "test_precision_pass": 88.56, "test_recall_fail": 88.16, "test_recall_pass": 85.48, "test_unparseable_rate": 0, "test_n": 1890}
52	deepseek-cwm-func-s123 | success | {"best_eval_loss": 0.0408, "train_time_seconds": 5244, "test_accuracy": 87.88, "test_f1_macro": 87.88, "test_precision_fail": 83.78, "test_precision_pass": 92.61, "test_recall_fail": 92.87, "test_recall_pass": 83.23, "test_unparseable_rate": 0, "test_n": 1890}
53	deepseek-cls-func | success | {"best_eval_loss": 0.0701, "train_time_seconds": 5444, "test_accuracy": 86.93, "test_f1_macro": 86.92, "test_precision_fail": 86.42, "test_precision_pass": 87.41, "test_recall_fail": 86.51, "test_recall_pass": 87.32, "test_n": 1890}
54	deepseek-cwm-func | success | {"best_eval_loss": 0.04292, "train_time_seconds": 5215, "test_accuracy": 85.77, "test_f1_macro": 85.73, "test_precision_fail": 80.07, "test_precision_pass": 93.18, "test_recall_fail": 93.86, "test_recall_pass": 78.22, "test_unparseable_rate": 0, "test_n": 1890}
55	deepseek-traj-repo-8k-s999 | success | {"test_accuracy": 79.2, "unparseable": 0, "best_eval_loss": 0.1565, "resolved_f1": 82.1, "unresolved_f1": 75, "f1_macro": 78.57, "train_loss": 0.2184}
56	deepseek-traj-repo-8k-s456 | success | {"test_accuracy": 75, "unparseable": 0, "best_eval_loss": 0.1547, "resolved_f1": 75, "unresolved_f1": 75, "f1_macro": 75, "train_loss": 0.2176}
57	deepseek-traj-repo-8k-s0 | success | {"test_accuracy": 75, "f1_macro": 72.68, "majority_baseline": 54.2, "gap_vs_majority_pp": 20.8, "unresolved_f1": 64.7, "resolved_f1": 80.6, "unresolved_precision": 91.7, "unresolved_recall": 50, "resolved_precision": 69.4, "resolved_recall": 96.2, "per_test_consistency": 75, "unparseable_rate": 0, "
58	deepseek-traj-repo-8k-s789 | success | {"test_accuracy": 66.67, "resolved_f1": 75, "unresolved_f1": 50, "best_eval_loss": 0.1295, "unparseable": 0}
59	deepseek-traj-repo-8k-s123 | success | {"test_accuracy": 75, "unparseable": 0, "best_eval_loss": 0.1182, "best_epoch": 2, "train_truncated_pct": 2.1, "gpu_mem_mib": 21399, "resolved_f1": 76.92, "unresolved_f1": 72.73}
60	deepseek-traj-repo-8k | success | {"test_accuracy": 81.25, "unparseable": 0, "best_eval_loss": 0.1216, "best_epoch": 2, "train_truncated_pct": 2.1, "gpu_mem_mib": 22475, "resolved_f1": 84.21, "unresolved_f1": 76.92}
61	deepseek-traj-repo-s123 | success | {"test_accuracy": 0.771, "best_eval_loss": 0.1147, "best_step": 98, "train_loss": 0.12, "unparseable_rate": 0.167, "resolved_recall": 0.962, "unresolved_recall": 0.545, "total_test": 48}
62	deepseek-traj-repo | success | {"test_accuracy": 0.771, "best_eval_loss": 0.111, "best_step": 98, "train_loss": 0.12, "unparseable_rate": 0.167, "resolved_recall": 0.962, "unresolved_recall": 0.545, "total_test": 48}
63	deepseek-traj-func-v2-s123 | success | {"best_eval_loss": 0.077, "best_step": 504, "test_accuracy": 0.8508, "majority_baseline": 0.5359, "train_loss": 0.0842, "train_runtime_seconds": 3021, "per_test_consistency": 0.782}
64	deepseek-traj-func-v2 | success | {"best_eval_loss": 0.0796, "best_step": 504, "test_accuracy": 0.8324, "majority_baseline": 0.5359, "train_loss": 0.0857, "train_runtime_seconds": 3069.6}
65	deepseek-traj-func | success | {"eval_loss_epoch1": 0.0943, "eval_loss_epoch2": 0.0793, "eval_loss_epoch3": 0.0884, "best_eval_loss": 0.0793, "best_step": 1008, "best_epoch": 2, "train_loss": 0.1131, "train_runtime_sec": 2910.6}
66	cwm4b-s42-mutation-breakdown | success | {"overall_accuracy": 58.04, "parseable_rate": 46.3, "parseable_only_accuracy": 42.9, "gold_parse_rate": 43.5, "gold_parseable_acc": 23.5, "operator_swap_parse_rate": 56.9, "operator_swap_parseable_acc": 63.1, "off_by_one_parse_rate": 4.4, "off_by_one_parseable_acc": 0, "return_value_parse_rate": 48.
67	cls4b-ckpt4600-test-mutation-pr | success | {"accuracy": 83.63, "gold_acc": 98.25, "operator_swap_acc": 78.91, "return_value_acc": 67.97, "off_by_one_acc": 58.47, "boundary_removal_acc": 46.9, "n_instances": 9784, "note": "off_by_one recall_fail=0 (all predicted pass); boundary_removal identical to 8B"}
68	cls8b-seed123-ckpt3000-mutation | success | {"accuracy": 85.6, "boundary_removal": 44.9, "operator_swap": 82.6, "return_value": 66.4, "off_by_one": 79.2, "gold": 99.6, "n_samples": 9784}
69	cls8b-s42-resume-ckpt3600-test-v2 | success | {"accuracy": 84.48, "f1_macro": 78.17, "fail_recall": 56.8, "pass_recall": 94.8, "n_samples": 9784, "note": "reproduces v1 exactly"}
70	cls8b-s42-resume-ckpt3600-mutation | success | {"overall_accuracy": 84.4849, "overall_correct": 8266, "overall_total": 9784, "gold_accuracy": 96.2443, "gold_correct": 4459, "gold_total": 4633, "mutation_operator_swap_accuracy": 81.3822, "mutation_operator_swap_correct": 2732, "mutation_operator_swap_total": 3357, "mutation_off_by_one_accuracy": 
71	cls8b-s42-ckpt3600-seq2048-ablation | success | {"accuracy": 83.04, "f1_macro": 76.8, "unparseable": 136, "n_samples": 9784, "seq_length": 2048}
72	repo-level-cls-8b-s42-resume | success | {"total_steps": 6633, "epochs": 3, "train_time_sec": 74425, "final_train_loss": 0.4284, "final_eval_loss": 0.4768, "best_eval_loss_resume": 0.2516, "best_eval_loss_resume_step": 4200, "best_eval_loss_overall": 0.0796, "best_eval_loss_overall_step": 200, "checkpoints_saved": 32, "overfitting": true, 
73	cwm-rank32-alpha64-ablation | success | {"accuracy": 87.04, "pass_f1": 86.79, "fail_f1": 87.27, "f1_macro": 87.03, "pass_precision": 91.8, "pass_recall": 82.3, "fail_precision": 82.9, "fail_recall": 92.1, "exact_match_rate": 84.55, "train_loss": 0.2069, "eval_loss": 0.0606, "n_instances": 1890, "vs_rank16_baseline": -0.47, "rank16_baselin
74	cls8b-seed123-ckpt6200-test-eval-v2 | success | {"accuracy": 84.7, "f1_fail": 63.71, "f1_pass": 90.31, "f1_macro": 77.01, "precision_fail": 88.84, "precision_pass": 83.96, "recall_fail": 49.66, "recall_pass": 97.69, "n_instances": 9784, "n_cls_unparseable": 0}
75	cwm-rank32-ablation-v2 | success | {"accuracy": 87, "exact_match_rate": 83.4, "fail_f1": 87.1, "pass_f1": 86.9, "train_loss_final": 0.0152, "train_loss_avg": 0.2536, "eval_loss": 0.0688, "train_runtime_sec": 5003, "test_set_size": 1890, "vs_rank16_baseline": -0.51, "rank16_baseline_accuracy": 87.51}
76	cls8b-seed123-ckpt200-test-eval | success | {"accuracy": 72.55, "f1_macro": 70.18, "pass_f1": 78.58, "fail_f1": 61.78, "pass_precision": 91.21, "pass_recall": 69.02, "fail_precision": 49.54, "fail_recall": 82.05, "n_samples": 9784, "n_pass": 7138, "n_fail": 2646, "majority_baseline": 72.96, "unparseable": 0, "confusion_matrix": {"tn": 2171, "
77	cls8b-s42-ckpt1000-test-seq2048-ablation | success | {"accuracy": 82.83, "f1_macro": 76.88, "fail_precision": 72.2, "fail_recall": 59.3, "fail_f1": 65.2, "pass_precision": 85.9, "pass_recall": 91.5, "pass_f1": 88.6, "unparseable": 136}
78	cls8b-seed123-ckpt6633-test-eval | success | {"accuracy": 84.89, "f1_macro": 77.56, "f1_fail": 64.7, "f1_pass": 90.4, "precision_fail": 87.8, "recall_fail": 51.2, "precision_pass": 84.3, "recall_pass": 97.4, "majority_baseline": 73, "gap_vs_majority_pp": 11.9, "total_samples": 9784, "unparseable_count": 0}
79	cls8b-seed123-ckpt6600-test-eval | success | {"accuracy": 84.9, "f1_macro": 77.58, "pass_f1": 90.4, "fail_f1": 64.8, "pass_precision": 84.3, "pass_recall": 97.4, "fail_precision": 87.8, "fail_recall": 51.3, "n_samples": 9784, "n_pass": 7138, "n_fail": 2646, "majority_baseline": 73, "unparseable": 0, "confusion_matrix": {"fail_as_fail": 1357, "
80	cls8b-s42-ckpt200-test8192-eval | success | {"accuracy": 70.07, "f1_macro": 68.18, "pass_f1": 75.9, "fail_f1": 60.4, "pass_precision": 91.8, "pass_recall": 64.7, "fail_precision": 47, "fail_recall": 84.5, "n_samples": 9784, "n_pass": 7138, "n_fail": 2646, "majority_baseline": 73, "unparseable": 0, "confusion_matrix": {"fail_as_fail": 2235, "f
81	cls4b-v5-ckpt600-test5120-eval | success | {"accuracy": 77.74, "f1_macro": 74.74, "f1_fail": 66.03, "f1_pass": 83.44, "precision_fail": 56.21, "recall_fail": 80.01, "majority_baseline": 72.96, "gap_vs_majority_pp": 4.78, "unparseable_count": 0, "total_samples": 9784}
82	cls8b-seed123-ckpt6400-test-eval-v2 | success | {"accuracy": 85.08, "f1_fail": 65.32, "f1_pass": 90.49, "f1_macro": 77.91, "precision_fail": 87.92, "precision_pass": 84.54, "recall_fail": 51.97, "recall_pass": 97.35, "n_instances": 9784, "n_cls_unparseable": 0}
83	cls8b-seed123-ckpt6633-val8192-eval | success | {"accuracy": 87.1, "f1_macro": 78.79, "f1_fail": 65.52, "f1_pass": 92.07, "precision_fail": 92.26, "recall_fail": 50.8, "precision_pass": 86.31, "recall_pass": 98.64, "majority_baseline": 75.88, "gap_vs_majority_pp": 11.23, "unparseable_count": 9, "total_samples": 9335}
84	cls8b-seed123-ckpt3000-test8192-eval | success | {"accuracy": 85.6, "f1_macro": 78.38, "f1_fail": 65.89, "f1_pass": 90.87, "precision_fail": 91.65, "recall_fail": 51.44, "precision_pass": 84.52, "recall_pass": 98.26, "majority_baseline": 72.96, "gap_vs_majority_pp": 12.64, "unparseable_count": 0, "total_samples": 9784}
85	cls4b-v5-ckpt4400-test5120-eval | success | {"accuracy": 83.24, "f1_macro": 74.44, "f1_fail": 59.45, "f1_pass": 89.44, "precision_fail": 85.98, "recall_fail": 45.43, "precision_pass": 82.78, "recall_pass": 97.25, "majority_baseline": 72.96, "gap_vs_majority_pp": 10.28, "unparseable_count": 0, "total_samples": 9784}
86	cls8b-seed123-ckpt6400-val8192-eval | success | {"accuracy": 87.48, "f1_macro": 79.66, "f1_fail": 67.04, "f1_pass": 92.27, "precision_fail": 91.81, "recall_fail": 52.8, "precision_pass": 86.78, "recall_pass": 98.5, "majority_baseline": 75.88, "gap_vs_majority_pp": 11.6, "unparseable_count": 9, "total_samples": 9335}
87	cls8b-seed123-ckpt6200-val8192-eval | success | {"accuracy": 87.52, "f1_macro": 79.26, "f1_fail": 66.16, "f1_pass": 92.35, "precision_fail": 95.63, "recall_fail": 50.58, "precision_pass": 86.33, "recall_pass": 99.27, "majority_baseline": 75.88, "gap_vs_majority_pp": 11.64, "unparseable_count": 9, "total_samples": 9335}
88	cls4b-v5-val-sweep-ckpt4600 | success | {"accuracy": 90.07, "f1_macro": 85.04, "f1_fail": 76.37, "f1_pass": 93.71, "precision_fail": 89.65, "recall_fail": 66.52, "precision_pass": 90.16, "recall_pass": 97.56, "majority_baseline": 75.88, "gap_vs_majority_pp": 14.19, "unparseable_count": 0, "total_samples": 9335, "n_truncated": 234}
89	cls8b-seed123-ckpt6600-val8192-eval | success | {"accuracy": 87.23, "f1_macro": 79.02, "f1_fail": 65.9, "f1_pass": 92.14, "precision_fail": 92.6, "recall_fail": 51.15, "precision_pass": 86.4, "recall_pass": 98.7, "majority_baseline": 75.88, "gap_vs_majority_pp": 11.36, "unparseable_count": 9, "total_samples": 9335}
90	cls8b-s42-ckpt1600-test8192-eval | success | {"accuracy": 84.99, "f1_macro": 78.94, "f1_fail": 67.65, "f1_pass": 90.22, "precision_fail": 81.06, "recall_fail": 58.05, "precision_pass": 85.93, "recall_pass": 94.97, "majority_baseline": 72.96, "gap_vs_majority_pp": 12.03, "unparseable_count": 0, "total_samples": 9784}
91	cls4b-v5-ckpt4600-test-eval | success | {"accuracy": 83.63, "f1_macro": 75.63, "f1_fail": 61.67, "f1_pass": 89.59, "precision_fail": 84.03, "recall_fail": 48.72, "precision_pass": 83.55, "recall_pass": 96.57, "majority_baseline": 72.96, "gap_vs_majority_pp": 10.67, "unparseable_count": 0, "total_samples": 9784}
92	cls8b-s42-ckpt1400-test8192-eval | success | {"accuracy": 85.47, "f1_macro": 78.9, "f1_fail": 67.13, "f1_pass": 90.67, "precision_fail": 86.43, "recall_fail": 54.88, "precision_pass": 85.27, "recall_pass": 96.81, "majority_baseline": 72.96, "gap_vs_majority_pp": 12.51, "unparseable_count": 0, "total_samples": 9784}
93	cls8b-s42-ckpt1200-test8192-eval | success | {"accuracy": 83.84, "f1_macro": 77.47, "f1_fail": 65.49, "f1_pass": 89.45, "precision_fail": 77.52, "recall_fail": 56.69, "precision_pass": 85.4, "recall_pass": 93.91, "majority_baseline": 72.96, "gap_vs_majority_pp": 10.89, "unparseable_count": 0, "total_samples": 9784}
94	cls8b-s42-ckpt800-test8192-eval | success | {"accuracy": 83.53, "f1_macro": 78.97, "f1_fail": 69.17, "f1_pass": 88.77, "precision_fail": 70.07, "recall_fail": 68.29, "precision_pass": 88.36, "recall_pass": 89.18, "majority_baseline": 72.96, "gap_vs_majority_pp": 10.58, "unparseable_count": 0, "total_samples": 9784}
95	cls4b-v5-val-sweep-ckpt4200 | success | {"accuracy": 89.06, "f1_macro": 83.07, "f1_fail": 73, "f1_pass": 93.1, "precision_fail": 90.3, "recall_fail": 61.3, "precision_pass": 88.8, "recall_pass": 97.9}
96	cls8b-s42-ckpt1600-val8192-v2 | success | {"accuracy": 86.75, "f1_macro": 78.94, "f1_fail": 66.12, "f1_pass": 91.76, "precision_fail": 86.28, "precision_pass": 86.83, "recall_fail": 53.6, "recall_pass": 97.29, "majority_baseline": 75.88, "gap_vs_majority_pp": 10.87, "unparseable": 9, "total": 9335}
97	cls8b-s42-ckpt1400-val8192-eval | success | {"accuracy": 85.97, "majority_baseline": 75.88, "gap_vs_majority_pp": 10.09, "f1_macro": 77.15, "f1_fail": 62.95, "f1_pass": 91.34, "precision_fail": 86.68, "precision_pass": 85.85, "recall_fail": 49.42, "recall_pass": 97.59, "n_instances": 9335, "n_unparseable": 9, "confusion_matrix": {"tn": 1113, 
98	cls4b-v5-val-sweep-ckpt4400-v3 | success | {"accuracy": 89.96, "f1_macro": 84.94, "f1_fail": 76.25, "f1_pass": 93.64, "precision_fail": 88.84, "precision_pass": 90.21, "recall_fail": 66.79, "recall_pass": 97.33, "majority_baseline": 75.88, "gap_vs_majority_pp": 14.09, "n_instances": 9335, "n_truncated": 234, "n_unparseable": 0}
99	cls8b-s42-ckpt1200-val8192-v3 | success | {"accuracy": 87.76, "f1_macro": 81.25, "f1_fail": 70.2, "f1_pass": 92.3, "precision_fail": 85, "recall_fail": 59.8, "precision_pass": 88.3, "recall_pass": 96.7, "majority_baseline": 75.9, "gap_vs_majority": 11.9, "unparseable": 9}
100	cls8b-s42-ckpt1000-test8192-eval | success | {"accuracy": 83.52, "f1_macro": 77.5, "f1_fail": 65.85, "f1_pass": 89.14, "precision_fail": 74.93, "recall_fail": 58.73, "precision_pass": 85.84, "recall_pass": 92.72, "majority_baseline": 72.96, "gap_vs_majority": 10.56, "unparseable_count": 0, "unparseable_rate": 0, "total_samples": 9784, "tp": 66
101	cls8b-s42-ckpt1000-val8192-eval | success | {"accuracy": 88.23, "f1_macro": 82.72, "f1_fail": 73, "f1_pass": 92.5, "precision_fail": 81.8, "recall_fail": 65.8, "precision_pass": 89.8, "recall_pass": 95.3, "unparseable": 9, "total_instances": 9335}
102	cls8b-s42-ckpt800-val8192-eval | success | {"accuracy": 84.5, "f1_macro": 79.2}
103	cls4b-v5-ckpt4000-val5120-eval | success | {"accuracy": 89.84, "f1_macro": 84.25, "f1_fail": 74.85, "f1_pass": 93.64, "precision_fail": 92.95, "recall_fail": 62.66, "precision_pass": 89.24, "recall_pass": 98.49, "unparseable": 0, "truncated": 234, "total": 9335}
104	cls4b-v5-ckpt600-val5120-eval | success | {"accuracy": 82.82, "f1_macro": 79.81, "f1_fail": 72.03, "f1_pass": 87.6, "precision_fail": 59.3, "recall_fail": 91.7, "unparseable": 0, "total": 9335}
105	repo-level-cls-8b-conda | success | {"val_8192": {"ckpt_200": {"accuracy": 63.52, "f1_macro": 61.17, "f1_fail": 51.6, "f1_pass": 70.7, "unparseable": 9}, "ckpt_400": {"accuracy": 80.96}, "ckpt_600": {"accuracy": 85}, "best_acc": "ckpt_600"}, "val_5120": {"ckpt_400": {"accuracy": 80.47, "f1_macro": 75.84}}, "test_2048": {"ckpt_400": {"
106	cls8b-s42-ckpt200-val8192-eval-v2 | success | {"accuracy": 63.52, "f1_macro": 61.17, "f1_fail": 51.6, "f1_pass": 70.7, "unparseable": 9, "total": 9335}
107	cls4b-seed123-ckpt800-val5120-eval | success | {"accuracy": 87.92, "f1_macro": 81.95, "f1_pass": 92.33, "f1_fail": 71.57, "unparseable": 0, "truncated": 234, "total": 9335}
108	repo-level-cls-seed123-home | success | {"val_2048": {"n": 9335, "unparseable": 1883, "ckpt_200": {"accuracy": 62.51, "f1_macro": 55.54, "f1_pass": 73.14, "f1_fail": 37.94}, "ckpt_400": {"accuracy": 80.72, "f1_macro": 67.03, "f1_pass": 88.27, "f1_fail": 45.78}, "ckpt_600": {"accuracy": 76.78, "f1_macro": 66.81, "f1_pass": 85, "f1_fail": 4
109	cls8b-s42-ckpt600-test8192-eval | success | {"accuracy": 79.05, "f1_macro": 75.12, "f1_fail": 65.24, "f1_pass": 85, "precision_fail": 59.16, "precision_pass": 88.95, "recall_fail": 72.71, "recall_pass": 81.4, "unparseable": 0, "total": 9784, "majority_baseline": 73, "gap_vs_majority_pp": 6.09}
110	cls8b-seed123-ckpt3000-val8192-eval | success | {"accuracy": 88.69, "f1_macro": 81.73, "f1_fail": 70.5, "f1_pass": 93, "precision_fail": 95.2, "precision_pass": 87.6, "recall_fail": 55.9, "recall_pass": 99.1, "majority_baseline": 75.9, "gap_vs_majority_pp": 12.8, "unparseable": 9, "total": 9335}
111	cls8b-s42-ckpt400-test8192-eval | success | {"accuracy": 84.79, "f1_macro": 81.18, "f1_fail": 72.93, "f1_pass": 89.43, "precision_fail": 70.32, "precision_pass": 90.74, "recall_fail": 75.74, "recall_pass": 88.15, "majority_baseline": 72.96, "gap_vs_majority_pp": 11.84, "unparseable": 0, "total": 9784}
112	repo-level-cls-v5 | success | {"checkpoint_sweep": {"ckpt_600": {"accuracy": 76.74, "f1_macro": 73.74, "fail_f1": 64.88, "pass_f1": 82.61}, "ckpt_4000": {"accuracy": 81.51, "f1_macro": 72.56, "fail_f1": 56.9, "pass_f1": 88.23}, "ckpt_4200": {"accuracy": 80.64, "f1_macro": 72.1, "fail_f1": 56.66, "pass_f1": 87.54}, "ckpt_4400": {
113	repo-level-cls-v5-conda | success | {"checkpoint_sweep": {"ckpt_200": {"accuracy": 52.96, "f1_macro": 52.89, "fail_f1": 51.02, "pass_f1": 54.76}, "ckpt_400": {"accuracy": 78.43, "f1_macro": 68.41, "fail_f1": 50.61, "pass_f1": 86.21, "fail_precision": 66.48, "fail_recall": 40.85, "pass_precision": 80.82, "pass_recall": 92.36}, "ckpt_60
114	repo-level-cwm-v10 | success | {"accuracy": 0.6991, "f1_macro": 0.4671, "f1_pass": 0.8187, "f1_fail": 0.1154, "precision_pass": 0.7304, "recall_pass": 0.9314, "precision_fail": 0.2815, "recall_fail": 0.0726, "majority_baseline": 0.7296, "n_unparseable": 9102, "n_unparseable_pct": 0.93, "n_truncated": 478, "n_truncated_pct": 0.048
115	repo-level-cls-v4 | success | {"accuracy": 0.6611, "f1_macro": 0.5661, "f1_pass": 0.769, "f1_fail": 0.363, "precision_pass": 0.765, "recall_pass": 0.774, "precision_fail": 0.369, "recall_fail": 0.357, "majority_baseline": 0.7296, "n_unparseable": 132, "best_checkpoint": "checkpoint-200", "early_stop": "D045"}
116	cwm8b-seed123 | success | {"overall_accuracy": 86.98, "pass_f1": 86.83, "fail_f1": 87.13, "pass_precision": 91.12, "pass_recall": 82.92, "fail_precision": 83.3, "fail_recall": 91.34, "exact_match_rate": 84.13, "unparseable": 0, "test_set_size": 1890}
117	cls8b-seed123 | success | {"overall_accuracy": 89.4, "pass_f1": 89.5, "fail_f1": 89.2, "pass_precision": 91.2, "pass_recall": 87.9, "fail_precision": 87.5, "fail_recall": 90.9, "train_loss": 0.3087, "eval_loss": 0.0848, "train_runtime_sec": 5666, "unparseable": 0}
118	cls8b-eval-seed123 | success | {"overall_accuracy": 89.37, "pass_f1": 89.54, "fail_f1": 89.19, "pass_precision": 91.2, "pass_recall": 87.93, "fail_precision": 87.54, "fail_recall": 90.9, "unparseable": 0, "test_set_size": 1890}
119	cls8b-eval-seed42 | success | {"overall_accuracy": 90.48, "pass_f1": 90.86, "fail_f1": 90.06, "pass_precision": 90.22, "pass_recall": 91.51, "fail_precision": 90.76, "fail_recall": 89.36, "unparseable": 0, "test_set_size": 1890}
120	cwm-seed789 | success | {"overall_accuracy": 86.67, "pass_f1": 86.74, "fail_f1": 86.6, "exact_match_rate": 83.97, "baseline_gap_pp": 34.92, "test_set_size": 1890, "unparseable_predictions": 0, "per_class": {"fail": {"precision": 84.09, "recall": 89.25, "f1": 86.6}, "pass": {"precision": 89.37, "recall": 84.25, "f1": 86.74}
121	cls8b-seed456 | success | {"overall_accuracy": 88.31, "pass_f1": 88.2, "fail_f1": 88.41, "pass_precision": 92.29, "pass_recall": 84.46, "fail_precision": 84.72, "fail_recall": 92.43, "train_loss": 0.3105, "eval_loss": 0.0928, "unparseable": 0, "test_set_size": 1890}
122	cwm8b-seed456 | success | {"overall_accuracy": 86.24, "pass_f1": 85.96, "fail_f1": 86.51, "pass_precision": 91.08, "pass_recall": 81.39, "fail_precision": 82.09, "fail_recall": 91.45, "exact_match_rate": 82.8, "train_loss": 0.2279, "eval_loss": 0.0583, "unparseable": 0, "test_set_size": 1890, "majority_baseline_accuracy": 51
123	5-paired-clustered-bootstrap | success | {"pooled_gap_pp": -0.45, "pooled_ci_lower": -1.71, "pooled_ci_upper": 0.84, "pooled_p_value": 0.499, "tost_p_value": 0.0071, "tost_margin_pp": 2, "seed_level_paired_t_p": 0.425, "seed_level_mean_gap": -0.48, "n_variants_pooled": 523, "n_clusters": 114, "per_seed_gaps": {"seed42": -0.97, "seed123": 1
124	cwm-seed0 | success | {"overall_accuracy": 87.57, "fail_f1": 87.93, "fail_precision": 82.71, "fail_recall": 93.86, "pass_f1": 87.18, "pass_precision": 93.45, "pass_recall": 81.7, "exact_match_rate": 84.29, "eval_loss": 0.0665, "train_loss": 0.2554, "train_runtime_sec": 3586}
125	per-test-precision-recall | success | {"accuracy": 87.51, "fail_precision": 82.75, "fail_recall": 93.64, "fail_f1": 87.86, "pass_precision": 93.24, "pass_recall": 81.8, "pass_f1": 87.15, "FP_count": 58, "FN_count": 178, "best_mutation": "return_value (97.26%)", "worst_mutation": "off_by_one (82.56%)", "bucket_6_10_acc": 96.3, "bucket_11
126	cwm-seed123 | success | {"overall_accuracy": 87.2, "pass_f1": 86.95, "fail_f1": 87.44, "exact_match_rate": 84.44, "majority_baseline_accuracy": 51.75, "accuracy_vs_baseline_gap_pp": 35.45, "test_set_size": 1890, "unparseable_predictions": 0}
127	cwm-seed456 | success | {"accuracy": 86.98, "pass_f1": 86.66, "fail_f1": 87.29, "pass_precision": 92.26, "pass_recall": 81.7, "fail_precision": 82.52, "fail_recall": 92.65, "exact_match_rate": 84.02, "train_loss": 0.2525, "eval_loss_best": 0.0551, "eval_loss_final": 0.0635, "train_runtime_sec": 3440, "unparseable": 0}
128	cls-seed0 | success | {"accuracy": 87.94, "pass_f1": 87.79, "fail_f1": 88.08, "pass_precision": 92.13, "pass_recall": 83.84, "fail_precision": 84.2, "fail_recall": 92.32, "train_loss": 0.2347, "eval_loss": 0.0963, "train_runtime_sec": 4976.75, "unparseable": 0}
129	cls-seed789 | success | {"accuracy": 89, "pass_f1": 88.9, "fail_f1": 89.1, "pass_precision": 93.3, "pass_recall": 84.9, "fail_precision": 85.2, "fail_recall": 93.4}
130	traj-level-finetuned | success | {"accuracy": 85.66, "unresolved_f1": 87.5, "resolved_f1": 83.18, "per_test_consistency": 79.94}
131	traj-level-seed456 | success | {"overall_accuracy": 87.4, "unresolved_f1": 88.7, "resolved_f1": 85.8, "unresolved_precision": 85.7, "unresolved_recall": 91.9, "resolved_precision": 89.7, "resolved_recall": 82.3, "consistency_rate": 78.8}
132	traj-level-seed789 | success | {"overall_accuracy": 87.31, "unresolved_f1": 88.27, "resolved_f1": 86.17, "unresolved_precision": 87.41, "unresolved_recall": 89.15, "resolved_precision": 87.18, "resolved_recall": 85.18, "consistency_rate": 76.74, "eval_loss": 0.1115, "train_loss": 0.2255, "train_runtime_sec": 2055.9}
133	traj-level-seed0 | success | {"overall_accuracy": 85.66, "unresolved_f1": 87.37, "resolved_f1": 83.41, "unresolved_precision": 82.71, "unresolved_recall": 92.59, "resolved_precision": 90.07, "resolved_recall": 77.66, "consistency_rate": 79.55, "train_loss": 0.225, "eval_loss_epoch1": 0.0949, "eval_loss_epoch2": 0.0885, "eval_lo
134	block-corr-empirical | success | {"icc": 0.1909, "icc_p_value": 0, "design_effect": 3.9676, "overall_error_rate": 0.1249, "all_correct_observed": 46, "all_correct_expected_iid": 16.35, "all_correct_ratio": 2.81, "error_std_observed": 0.1531, "error_std_expected_iid": 0.0811, "error_std_ratio": 1.89, "n_samples": 1890, "n_problems":
135	model-size-scaling-cwm8b | success | {"accuracy": 87.67, "pass_f1": 87.57, "fail_f1": 87.77, "pass_precision": 91.53, "pass_recall": 83.95, "fail_precision": 84.19, "fail_recall": 91.67, "exact_match_rate": 84.39, "train_loss": 0.229, "eval_loss_epoch1": 0.0554, "eval_loss_epoch2": 0.0512, "eval_loss_epoch3": 0.0564, "train_runtime_sec
136	model-size-scaling-cls8b | success | {"accuracy": 90.48, "pass_f1": 90.86, "fail_f1": 90.06, "pass_precision": 90.22, "pass_recall": 91.51, "fail_precision": 90.76, "fail_recall": 89.36, "train_loss": 0.3125, "eval_loss_epoch1": 0.0723, "eval_loss_epoch2": 0.0741, "eval_loss_epoch3": 0.0783, "train_runtime_sec": 5614, "unparseable": 0}
137	llm-judge-32b-zeroshot | success | {"overall_accuracy": 71.69, "majority_baseline": 51.75, "accuracy_vs_baseline_gap": 19.95, "fail_precision": 64.4, "fail_recall": 92.43, "fail_f1": 75.91, "pass_precision": 88.12, "pass_recall": 52.35, "pass_f1": 65.68, "unparseable_predictions": 0, "trajectory_accuracy": 99.12, "trajectory_total_pr
138	llm-judge-8b-zeroshot | success | {"overall_accuracy": 64.4, "fail_precision": 57.9, "fail_recall": 95.8, "fail_f1": 72.2, "pass_precision": 90, "pass_recall": 35.1, "pass_f1": 50.5, "majority_baseline": 51.7, "accuracy_vs_baseline_gap": 12.6, "traj_accuracy": 99.1, "traj_problems": 114, "traj_true_resolved": 1, "traj_pred_resolved"
139	traj-level-seed123 | success | {"overall_accuracy": 85.47, "unresolved_f1": 87, "resolved_f1": 83.52, "unresolved_precision": 83.53, "unresolved_recall": 90.78, "resolved_precision": 88.17, "resolved_recall": 79.33, "consistency_rate": 78.59}
140	oracle-f2p-stratified | success | {"T1_pct": 68.7, "T1_block_adv": -0.09, "T2_pct": 19.1, "T2_block_adv": 31.69, "T3_5_pct": 7.1, "T3_5_block_adv": 40.74, "T6plus_pct": 5.1, "T6plus_block_adv": 40.06, "overall_block_adv": 10.93, "T2_contribution_pct": 55.3}
141	mvp-b-train | success | {"overall_accuracy": 0.875, "pass_f1": 0.871, "fail_f1": 0.879, "pass_precision": 0.9324, "pass_recall": 0.818, "fail_precision": 0.8275, "fail_recall": 0.9364, "majority_baseline": 0.52, "accuracy_vs_majority_gap": 0.355}
142	multi-seed-core | success | {"seed42": {"accuracy": 87.83, "pass_f1": 88.06, "fail_f1": 87.59, "pass_precision": 89.45, "pass_recall": 86.71, "fail_precision": 86.2, "fail_recall": 89.04}, "seed123": {"accuracy": 89.52, "pass_f1": 89.64, "fail_f1": 89.4, "pass_precision": 91.76, "pass_recall": 87.63, "fail_precision": 87.34, "
143	mvp-a-oracle-sim | success | {"original_T12": {"iid_adv_70_85": 0.1849, "block_adv_70_85": 0.3618}, "sensitivity_T3": {"iid_adv_70_85": 0.0761, "block_adv_70_85": 0.3839}, "sensitivity_T7": {"iid_adv_70_85": 0.1351, "block_adv_70_85": 0.3833}, "sensitivity_T11": {"iid_adv_70_85": 0.1863, "block_adv_70_85": 0.3639}, "real_f2p_T1
144	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "5627d554-2584-4e32-8a22-0c060a6fdc2e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/72deb850-edfb-4093-94b6-8107ea44f4ef/tool-results/bofsph3hk.txt",
      "content": "Total experiments: 152\ndeepseek-cwm-repo-s456-train-v2 | success | {\"train_loss\": 0.02127, \"eval_loss\": 5.2837, \"total_steps\": 12627, \"training_time_hours\": 27.55}\ntraj14b-func-s456 | success | {\"best_eval_loss\": 0.0971, \"best_checkpoint\": \"best\", \"epochs\": 3, \"accuracy\": 88.28, \"dtype\": \"bf16\", \"n_test\": 1032}\ntraj14b-func-s123 | success | {\"best_eval_loss\": 0.0836, \"best_checkpoint\": \"checkpoint-252\", \"epochs\": 3, \"accuracy\": 88.57, \"dtype\": \"bf16\", \"n_test\": 1032}\ntraj14b-func-s42 | success | {\"best_eval_loss\": 0.0958, \"best_checkpoint\": \"best\", \"epochs\": 3, \"accuracy\": 89.73, \"dtype\": \"bf16\", \"n_test\": 1032}\ncwm14b-func-s456 | success | {\"accuracy\": 90.26, \"unparseable\": 0, \"best_checkpoint\": \"best\", \"dtype\": \"bf16\", \"n_test\": 1890}\ncwm14b-func-s123 | success | {\"accuracy\": 88.99, \"unparseable\": 0, \"best_checkpoint\": \"best\", \"dtype\": \"bf16\", \"n_test\": 1890}\ncls14b-func-s456 | success | {\"accuracy\": 89.79, \"f1_fail\": 89.45, \"f1_pass\": 90.11, \"precision_fail\": 89.2, \"recall_fail\": 89.69, \"precision_pass\": 90.34, \"recall_pass\": 89.88, \"unparseable\": 0, \"best_checkpoint\": \"checkpoint-478\", \"dtype\": \"bf16\", \"best_train_loss\": 0.0659}\ncls14b-func-s123 | success | {\"accuracy\": 90.79, \"f1_fail\": 90.58, \"f1_pass\": 90.99, \"precision_fail\": 89.42, \"recall_fail\": 91.78, \"precision_pass\": 92.14, \"recall_pass\": 89.88, \"unparseable\": 0, \"best_checkpoint\": \"checkpoint-956\", \"dtype\": \"bf16\", \"best_train_loss\": 0.063}\ncls14b-func-s42-v2 | success | {\"accuracy\": 89.47, \"f1_fail\": 89.02, \"f1_pass\": 89.88, \"unparseable\": 0, \"checkpoint\": \"checkpoint-956\", \"delta_vs_8b\": -0.47, \"cls_cwm_gap_14b\": 0.21}\ncwm14b-func-s42 | success | {\"accuracy\": 89.3, \"f1_fail\": 88.3, \"f1_pass\": 90.1, \"exact_match_rate\": 86.6, \"unparseable\": 0, \"checkpoint\": \"checkpoint-956\", \"delta_vs_8b\": 1.97}\n8b-baseline-rerun | success | {\"0shot_accuracy\": 60.53, \"0shot_f1_macro\": 55.73, \"3shot_accuracy\": 60.42, \"3shot_f1_macro\": 56.09, \"0shot_unparseable\": 5, \"3shot_unparseable\": 1}\n14b-baseline-0shot-3shot-v2 | success | {\"0shot\": {\"accuracy\": 66.24, \"gap_vs_majority\": 14.5, \"f1_fail\": 72.99, \"f1_pass\": 55.01, \"f1_macro\": 64, \"unparseable\": 0, \"n\": 1890}, \"3shot\": {\"accuracy\": 73.12, \"gap_vs_majority\": 21.38, \"f1_fail\": 75.79, \"f1_pass\": 69.8, \"f1_macro\": 72.79, \"unparseable\": 0, \"n\": 1890}}\ndeepseek-cwm-repo-s123-eval-1epoch | success | {\"accuracy\": 75.45, \"f1_macro\": 65.08, \"f1_fail\": 46.05, \"f1_pass\": 84.11, \"unparseable_rate\": 66.4, \"unparseable_count\": 6500, \"n_instances\": 9784, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 2.49, \"truncated\": 0}\nqwen3-8b-cwm-repo-s456-eval | success | {\"accuracy\": 66.93, \"f1_macro\": 51.97, \"f1_fail\": 25.16, \"f1_pass\": 78.77, \"unparseable_rate\": 60.39, \"unparseable_count\": 5909, \"n_instances\": 9784, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -6.03, \"precision_fail\": 32.42, \"recall_fail\": 20.56, \"checkpoint_step\": 6633}\ndeepseek-cwm-repo-s123-e3-eval | success | {\"accuracy\": 57.31, \"f1_macro\": 51.79, \"f1_fail\": 35.49, \"f1_pass\": 68.1, \"precision_fail\": 30.01, \"precision_pass\": 74.86, \"recall_fail\": 43.42, \"recall_pass\": 62.45, \"unparseable_count\": 5028, \"unparseable_rate\": 51.39, \"n_instances\": 9784, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -15.65}\nqwen3-8b-cwm-repo-s123-eval | success | {\"accuracy\": 67.33, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -5.62, \"f1_fail\": 32.94, \"f1_pass\": 78.41, \"f1_macro\": 55.67, \"precision_fail\": 37.03, \"precision_pass\": 75.72, \"recall_fail\": 29.67, \"recall_pass\": 81.3, \"unparseable_count\": 6257, \"unparseable_rate\": 63.95, \"n_instances\": 9784, \ndeepseek-cwm-repo-s456-e3-eval | success | {\"accuracy\": 56.11, \"unparseable_rate\": 56.97, \"parseable_only_accuracy\": 32.45, \"f1_macro\": 50.6, \"samples\": 9784}\ndeepseek-cwm-repo-s123 | success | {\"accuracy\": 61.9, \"majority_baseline\": 72.96, \"gap_vs_majority\": -11.06, \"f1_macro\": 51.5, \"f1_pass\": 73.96, \"f1_fail\": 29.04, \"recall_pass\": 74.15, \"recall_fail\": 28.84, \"unparseable_rate\": 65.53, \"total\": 9784, \"correct\": 6056, \"truncated\": 0, \"checkpoint\": \"checkpoint-8844 (epoch 2)\", \"seq_lengt\nqwen3-8b-cwm-repo-s123-train-v4 | success | {\"train_loss\": 0.00873, \"eval_loss\": 0.5166, \"steps_completed\": 6633, \"epochs\": 3, \"training_time_seconds\": 85699}\ndeepseek-cwm-repo-s42-seq4096-eval | success | {\"accuracy\": 61.49, \"unparseable_rate\": 62.5, \"unparseable_count\": 6115, \"n_instances\": 9784, \"f1_macro\": 43.73, \"truncated\": 0, \"truncated_rate\": 0, \"max_generation_tokens\": 284, \"max_new_tokens_limit\": 512, \"seq_length\": 4096}\ndeepseek-cls-repo-s456-eval-v2 | success | {\"accuracy\": 86.15, \"f1_macro\": 80.43, \"f1_fail\": 69.84, \"f1_pass\": 91.01, \"precision_fail\": 84.95, \"recall_fail\": 59.3, \"checkpoint\": \"checkpoint-2163\", \"seq_length\": 8192}\ncls8b-repo-s456-eval-v2 | success | {\"accuracy\": 84.4, \"f1_macro\": 76.19, \"f1_fail\": 62.21, \"f1_pass\": 90.17, \"precision_fail\": 90.23, \"recall_fail\": 47.47, \"checkpoint\": \"checkpoint-2200\", \"seq_length\": 8192}\nqwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval | success | {\"accuracy\": 64.36, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -8.6, \"f1_macro\": 54.42, \"f1_pass\": 75.71, \"f1_fail\": 33.14, \"precision_pass\": 75.3, \"precision_fail\": 33.63, \"recall_pass\": 76.11, \"recall_fail\": 32.65, \"unparseable\": 6236, \"unparseable_rate\": 63.74, \"truncated\": 0, \"truncated_r\ncls8b-s42-ckpt-ablation | success | {\"ckpt-2200\": {\"accuracy\": 85.34, \"f1_macro\": 79.04, \"f1_fail\": 67.56, \"f1_pass\": 90.53}, \"ckpt-3600\": {\"accuracy\": 84.48, \"f1_macro\": 78.17, \"f1_fail\": 66.43, \"f1_pass\": 89.91}, \"ckpt-6633\": {\"accuracy\": 85.29, \"f1_macro\": 78.44, \"f1_fail\": 66.28, \"f1_pass\": 90.6}}\nqwen3-8b-traj-repo-s456 | success | {\"variant_accuracy\": 70.83, \"variant_correct\": 34, \"variant_total\": 48, \"f1_macro\": 70.63, \"overall_accuracy\": 70.83, \"precision_unresolved\": 63.33, \"recall_unresolved\": 86.36, \"f1_unresolved\": 73.08, \"precision_resolved\": 83.33, \"recall_resolved\": 57.69, \"f1_resolved\": 68.18, \"train_loss\": 0.5664, \nqwen3-8b-traj-repo-s123 | success | {\"variant_accuracy\": 77.08, \"variant_correct\": 37, \"variant_total\": 48, \"f1_macro\": 76.59, \"overall_accuracy\": 77.08, \"precision_unresolved\": 78.95, \"recall_unresolved\": 68.18, \"f1_unresolved\": 73.17, \"precision_resolved\": 75.86, \"recall_resolved\": 84.62, \"f1_resolved\": 80, \"train_loss\": 0.5706, \"ev\nexp-downsample-cls-func-v3-eval | success | {\"accuracy\": 80.74, \"f1_macro\": 75.89, \"fail_f1\": 65.1, \"pass_f1\": 86.7, \"unparseable\": 132, \"total\": 9784, \"source\": \"extracted from log (file write failed)\"}\nexp-downsample-cls-func-v3 | success | {\"train_loss\": 0.2869, \"eval_loss_epoch1\": 0.1061, \"eval_loss_epoch2\": 0.0907, \"eval_loss_epoch3\": 0.1156, \"best_epoch\": 2, \"training_time_min\": 44.4}\nexp-e-qwen3-3shot-baseline | success | {\"per_test_accuracy\": 71.61, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": -1.35, \"f1_fail\": 61.42, \"f1_pass\": 77.54, \"f1_macro\": 69.48, \"variant_accuracy\": 45.83, \"variant_correct\": 22, \"variant_total\": 48, \"n_instances\": 9784, \"unparseable\": 0, \"truncated\": 0, \"elapsed_min\": 24.6}\nrepo-level-3shot-baseline | success | {\"per_test_accuracy\": 46.28, \"variant_accuracy\": 45.83, \"variant_correct\": 22, \"variant_total\": 48, \"majority_baseline\": 73, \"truncated\": 0, \"unparseable\": 0, \"total\": 9784, \"runtime_min\": 33.8}\nexp-d-constrained-decoding | success | {\"forced_parse\": {\"qwen3_8b\": {\"n\": 9784, \"original_unparseable_rate\": 73.8, \"rescue_rate\": 90.6, \"original_parseable_acc\": 38.5, \"forced_parseable_acc\": 49.4, \"delta_pp\": 10.8}, \"qwen3_4b\": {\"n\": 500, \"original_unparseable_rate\": 75.2, \"rescue_rate\": 77.9, \"original_parseable_acc\": 42.7, \"forced_pa\nexp-b-complexity-bin | success | {\"bins\": {\"23-70\": {\"n_variants\": 12, \"n_tests\": 538, \"cls_qwen3_8b_s123\": 83.3, \"cls_ds_v5\": 91.7, \"cwm_qwen3_8b\": 66.7}, \"71-150\": {\"n_variants\": 14, \"n_tests\": 1282, \"cls_qwen3_8b_s123\": 64.3, \"cls_ds_v5\": 71.4, \"cwm_qwen3_8b\": 42.9}, \"151-250\": {\"n_variants\": 15, \"n_tests\": 2999, \"cls_qwen3_8b_s\nexp-a-routing | success | {\"oracle_routing_7cls\": 100, \"oracle_best_pair\": 95.83, \"test_count_heuristic\": 85.42, \"agreement_confidence\": 83.33, \"majority_vote\": \"75-79%\", \"best_single_cls\": 81.25, \"test_count_heuristic_delta\": \"+4.17pp\", \"oracle_delta\": \"+18.75pp\", \"traj_per_variant\": \"unavailable\", \"cwm_repo_level\": \"45-52%\nqwen3-8b-traj-repo-s42-ckpt98-eval | success | {\"variant_accuracy\": 72.92, \"variant_correct\": 35, \"variant_total\": 48, \"f1_macro\": 72.9, \"fail_recall\": 77.3, \"pass_recall\": 69.2, \"unparseable\": 0, \"note\": \"epoch 2 checkpoint, better class balance than epoch 3\"}\nqwen3-8b-traj-repo-s42-best-eval | success | {\"variant_accuracy\": 70.83, \"variant_correct\": 34, \"variant_total\": 48, \"f1_macro\": 70, \"fail_recall\": 95.5, \"pass_recall\": 50, \"unparseable\": 0, \"note\": \"epoch 3 checkpoint, biased toward predicting unresolved\"}\nqwen3-8b-traj-repo-s42-v2 | success | {\"eval_loss\": \"NaN_all_epochs\", \"total_steps\": 147, \"epochs\": 3, \"seq_length\": 4096, \"best_checkpoint\": \"epoch_3_default_due_to_nan_eval_loss\", \"gradient_checkpointing\": true}\ndeepseek-cls-repo-s123 | success | {\"per_test_accuracy_seq8192\": 74.93, \"per_test_accuracy_seq2048\": 82.62, \"majority_baseline\": 72.96, \"gap_vs_majority_seq8192\": 1.97, \"f1_macro_seq8192\": 53.94, \"f1_fail_seq8192\": 22.84, \"f1_pass_seq8192\": 85.03, \"precision_fail_seq8192\": 68.11, \"recall_fail_seq8192\": 13.72, \"recall_pass_seq8192\": 9\ndeepseek-cls-repo-v5-ckpt6315-eval | success | {\"accuracy\": 82.51, \"fail_recall\": 38.47, \"pass_recall\": 98.84, \"unparseable\": 0, \"n_instances\": 9784, \"confusion\": {\"TN\": 1018, \"FP\": 1628, \"FN\": 83, \"TP\": 7055}, \"variant_accuracy\": 79.17, \"variant_correct\": 38, \"variant_total\": 48, \"variant_fail_recall\": 59.09}\nqwen3-4b-traj-repo-s42-eval | success | {\"variant_accuracy\": 72.92, \"variant_correct\": 35, \"variant_total\": 48, \"f1_macro\": 72.62, \"resolved_precision\": 74.1, \"resolved_recall\": 76.9, \"resolved_f1\": 75.5, \"unresolved_precision\": 71.4, \"unresolved_recall\": 68.2, \"unresolved_f1\": 69.8, \"vs_majority_baseline_pp\": 18.8}\nqwen3-4b-traj-repo-s42 | success | {\"eval_loss_epoch1\": 0.2123, \"eval_loss_epoch2\": 0.1503, \"eval_loss_epoch3\": 0.2249, \"best_epoch\": 2, \"total_steps\": 147}\ndeepseek-cls-repo-v5-ckpt2105-eval | success | {\"accuracy\": 82.61, \"variant_accuracy\": 81.25, \"variant_correct\": 39, \"variant_total\": 48, \"fail_recall\": 51.02, \"pass_recall\": 94.33, \"f1_macro\": 75.07, \"fail_f1\": 61.35, \"pass_f1\": 88.78, \"fail_precision\": 76.92, \"pass_precision\": 83.86, \"unparseable\": 0, \"n_instances\": 9784, \"confusion\": {\"TP\": 6\ndeepseek-cls-repo-v5 | success | {\"train_loss_final\": 0.0399, \"eval_loss_epoch1\": 0.0886, \"eval_loss_epoch2\": 0.1587, \"eval_loss_epoch3\": 0.1975, \"total_steps\": 6315, \"train_time_seconds\": 63312, \"best_checkpoint\": \"checkpoint-2105 (epoch 1)\", \"lora_params\": \"16.8M\"}\ndeepseek-0shot-func-baseline | success | {\"accuracy\": 0.6302, \"pass_f1\": 0.7196, \"fail_f1\": 0.4569, \"unparseable_rate\": 0.0106, \"unparseable_count\": 20, \"total_samples\": 1890, \"runtime_seconds\": 113, \"confusion\": {\"TP\": 897, \"FP\": 618, \"TN\": 294, \"FN\": 81}}\nqwen3-0shot-func-baseline | success | {\"accuracy\": 0.6873, \"pass_f1\": 0.655, \"fail_f1\": 0.7141, \"unparseable_rate\": 0.0032, \"unparseable_count\": 6, \"total_samples\": 1890, \"runtime_seconds\": 96, \"confusion\": {\"TP\": 561, \"FP\": 174, \"TN\": 738, \"FN\": 417}}\ndeepseek-0shot-repo-baseline | success | {\"accuracy\": 0.4854, \"pass_f1\": 0.647, \"fail_f1\": 0.0509, \"unparseable_rate\": 0.087, \"unparseable_count\": 851, \"total_samples\": 9784, \"runtime_seconds\": 1545, \"confusion\": {\"TP\": 4614, \"FP\": 2511, \"TN\": 135, \"FN\": 2524}}\nrepo-level-0shot-baseline | success | {\"accuracy\": 0.499, \"pass_f1\": 0.4895, \"fail_f1\": 0.5081, \"unparseable_rate\": 0, \"unparseable_count\": 0, \"total_samples\": 9784, \"runtime_seconds\": 1018.2, \"confusion\": {\"TP\": 2350, \"FP\": 114, \"TN\": 2532, \"FN\": 4788}}\ndeepseek-cwm-repo | success | {\"train_loss\": 0.021, \"eval_loss\": \"NaN\", \"total_steps\": 13266, \"epochs\": 3, \"wall_clock_seconds\": 112680, \"gpu_hours\": 31.3, \"note\": \"eval_loss=NaN is known DeepSeek issue, does not affect training quality\"}\nqwen3-8b-traj-func-s123 | success | {\"test_accuracy\": 87.79, \"best_eval_loss\": 0.0782, \"pass_f1\": 86.74, \"fail_f1\": 88.69, \"unparseable\": 0, \"per_test_consistency\": 76.07, \"total_steps\": 756, \"test_set_size\": 1032, \"eval_script\": \"eval_traj_verifier_8b.py\"}\nqwen3-8b-traj-func-s42 | success | {\"test_accuracy\": 87.6, \"eval_loss\": 0.0975, \"train_loss\": 0.0312, \"unparseable\": 0, \"pass_f1\": 85.96, \"fail_f1\": 88.89, \"per_test_consistency\": 78.78, \"total_steps\": 756, \"test_set_size\": 1032, \"eval_script\": \"eval_traj_verifier_8b.py\", \"note\": \"87.98% from eval_traj_verifier.py (model.cuda) also v\ndeepseek-cls-func-s123 | success | {\"best_eval_loss\": 0.06753, \"train_time_seconds\": 5391, \"test_accuracy\": 86.77, \"test_f1_macro\": 86.77, \"test_precision_fail\": 84.99, \"test_precision_pass\": 88.56, \"test_recall_fail\": 88.16, \"test_recall_pass\": 85.48, \"test_unparseable_rate\": 0, \"test_n\": 1890}\ndeepseek-cwm-func-s123 | success | {\"best_eval_loss\": 0.0408, \"train_time_seconds\": 5244, \"test_accuracy\": 87.88, \"test_f1_macro\": 87.88, \"test_precision_fail\": 83.78, \"test_precision_pass\": 92.61, \"test_recall_fail\": 92.87, \"test_recall_pass\": 83.23, \"test_unparseable_rate\": 0, \"test_n\": 1890}\ndeepseek-cls-func | success | {\"best_eval_loss\": 0.0701, \"train_time_seconds\": 5444, \"test_accuracy\": 86.93, \"test_f1_macro\": 86.92, \"test_precision_fail\": 86.42, \"test_precision_pass\": 87.41, \"test_recall_fail\": 86.51, \"test_recall_pass\": 87.32, \"test_n\": 1890}\ndeepseek-cwm-func | success | {\"best_eval_loss\": 0.04292, \"train_time_seconds\": 5215, \"test_accuracy\": 85.77, \"test_f1_macro\": 85.73, \"test_precision_fail\": 80.07, \"test_precision_pass\": 93.18, \"test_recall_fail\": 93.86, \"test_recall_pass\": 78.22, \"test_unparseable_rate\": 0, \"test_n\": 1890}\ndeepseek-traj-repo-8k-s999 | success | {\"test_accuracy\": 79.2, \"unparseable\": 0, \"best_eval_loss\": 0.1565, \"resolved_f1\": 82.1, \"unresolved_f1\": 75, \"f1_macro\": 78.57, \"train_loss\": 0.2184}\ndeepseek-traj-repo-8k-s456 | success | {\"test_accuracy\": 75, \"unparseable\": 0, \"best_eval_loss\": 0.1547, \"resolved_f1\": 75, \"unresolved_f1\": 75, \"f1_macro\": 75, \"train_loss\": 0.2176}\ndeepseek-traj-repo-8k-s0 | success | {\"test_accuracy\": 75, \"f1_macro\": 72.68, \"majority_baseline\": 54.2, \"gap_vs_majority_pp\": 20.8, \"unresolved_f1\": 64.7, \"resolved_f1\": 80.6, \"unresolved_precision\": 91.7, \"unresolved_recall\": 50, \"resolved_precision\": 69.4, \"resolved_recall\": 96.2, \"per_test_consistency\": 75, \"unparseable_rate\": 0, \"\ndeepseek-traj-repo-8k-s789 | success | {\"test_accuracy\": 66.67, \"resolved_f1\": 75, \"unresolved_f1\": 50, \"best_eval_loss\": 0.1295, \"unparseable\": 0}\ndeepseek-traj-repo-8k-s123 | success | {\"test_accuracy\": 75, \"unparseable\": 0, \"best_eval_loss\": 0.1182, \"best_epoch\": 2, \"train_truncated_pct\": 2.1, \"gpu_mem_mib\": 21399, \"resolved_f1\": 76.92, \"unresolved_f1\": 72.73}\ndeepseek-traj-repo-8k | success | {\"test_accuracy\": 81.25, \"unparseable\": 0, \"best_eval_loss\": 0.1216, \"best_epoch\": 2, \"train_truncated_pct\": 2.1, \"gpu_mem_mib\": 22475, \"resolved_f1\": 84.21, \"unresolved_f1\": 76.92}\ndeepseek-traj-repo-s123 | success | {\"test_accuracy\": 0.771, \"best_eval_loss\": 0.1147, \"best_step\": 98, \"train_loss\": 0.12, \"unparseable_rate\": 0.167, \"resolved_recall\": 0.962, \"unresolved_recall\": 0.545, \"total_test\": 48}\ndeepseek-traj-repo | success | {\"test_accuracy\": 0.771, \"best_eval_loss\": 0.111, \"best_step\": 98, \"train_loss\": 0.12, \"unparseable_rate\": 0.167, \"resolved_recall\": 0.962, \"unresolved_recall\": 0.545, \"total_test\": 48}\ndeepseek-traj-func-v2-s123 | success | {\"best_eval_loss\": 0.077, \"best_step\": 504, \"test_accuracy\": 0.8508, \"majority_baseline\": 0.5359, \"train_loss\": 0.0842, \"train_runtime_seconds\": 3021, \"per_test_consistency\": 0.782}\ndeepseek-traj-func-v2 | success | {\"best_eval_loss\": 0.0796, \"best_step\": 504, \"test_accuracy\": 0.8324, \"majority_baseline\": 0.5359, \"train_loss\": 0.0857, \"train_runtime_seconds\": 3069.6}\ndeepseek-traj-func | success | {\"eval_loss_epoch1\": 0.0943, \"eval_loss_epoch2\": 0.0793, \"eval_loss_epoch3\": 0.0884, \"best_eval_loss\": 0.0793, \"best_step\": 1008, \"best_epoch\": 2, \"train_loss\": 0.1131, \"train_runtime_sec\": 2910.6}\ncwm4b-s42-mutation-breakdown | success | {\"overall_accuracy\": 58.04, \"parseable_rate\": 46.3, \"parseable_only_accuracy\": 42.9, \"gold_parse_rate\": 43.5, \"gold_parseable_acc\": 23.5, \"operator_swap_parse_rate\": 56.9, \"operator_swap_parseable_acc\": 63.1, \"off_by_one_parse_rate\": 4.4, \"off_by_one_parseable_acc\": 0, \"return_value_parse_rate\": 48.\ncls4b-ckpt4600-test-mutation-pr | success | {\"accuracy\": 83.63, \"gold_acc\": 98.25, \"operator_swap_acc\": 78.91, \"return_value_acc\": 67.97, \"off_by_one_acc\": 58.47, \"boundary_removal_acc\": 46.9, \"n_instances\": 9784, \"note\": \"off_by_one recall_fail=0 (all predicted pass); boundary_removal identical to 8B\"}\ncls8b-seed123-ckpt3000-mutation | success | {\"accuracy\": 85.6, \"boundary_removal\": 44.9, \"operator_swap\": 82.6, \"return_value\": 66.4, \"off_by_one\": 79.2, \"gold\": 99.6, \"n_samples\": 9784}\ncls8b-s42-resume-ckpt3600-test-v2 | success | {\"accuracy\": 84.48, \"f1_macro\": 78.17, \"fail_recall\": 56.8, \"pass_recall\": 94.8, \"n_samples\": 9784, \"note\": \"reproduces v1 exactly\"}\ncls8b-s42-resume-ckpt3600-mutation | success | {\"overall_accuracy\": 84.4849, \"overall_correct\": 8266, \"overall_total\": 9784, \"gold_accuracy\": 96.2443, \"gold_correct\": 4459, \"gold_total\": 4633, \"mutation_operator_swap_accuracy\": 81.3822, \"mutation_operator_swap_correct\": 2732, \"mutation_operator_swap_total\": 3357, \"mutation_off_by_one_accuracy\": \ncls8b-s42-ckpt3600-seq2048-ablation | success | {\"accuracy\": 83.04, \"f1_macro\": 76.8, \"unparseable\": 136, \"n_samples\": 9784, \"seq_length\": 2048}\nrepo-level-cls-8b-s42-resume | success | {\"total_steps\": 6633, \"epochs\": 3, \"train_time_sec\": 74425, \"final_train_loss\": 0.4284, \"final_eval_loss\": 0.4768, \"best_eval_loss_resume\": 0.2516, \"best_eval_loss_resume_step\": 4200, \"best_eval_loss_overall\": 0.0796, \"best_eval_loss_overall_step\": 200, \"checkpoints_saved\": 32, \"overfitting\": true, \ncwm-rank32-alpha64-ablation | success | {\"accuracy\": 87.04, \"pass_f1\": 86.79, \"fail_f1\": 87.27, \"f1_macro\": 87.03, \"pass_precision\": 91.8, \"pass_recall\": 82.3, \"fail_precision\": 82.9, \"fail_recall\": 92.1, \"exact_match_rate\": 84.55, \"train_loss\": 0.2069, \"eval_loss\": 0.0606, \"n_instances\": 1890, \"vs_rank16_baseline\": -0.47, \"rank16_baselin\ncls8b-seed123-ckpt6200-test-eval-v2 | success | {\"accuracy\": 84.7, \"f1_fail\": 63.71, \"f1_pass\": 90.31, \"f1_macro\": 77.01, \"precision_fail\": 88.84, \"precision_pass\": 83.96, \"recall_fail\": 49.66, \"recall_pass\": 97.69, \"n_instances\": 9784, \"n_cls_unparseable\": 0}\ncwm-rank32-ablation-v2 | success | {\"accuracy\": 87, \"exact_match_rate\": 83.4, \"fail_f1\": 87.1, \"pass_f1\": 86.9, \"train_loss_final\": 0.0152, \"train_loss_avg\": 0.2536, \"eval_loss\": 0.0688, \"train_runtime_sec\": 5003, \"test_set_size\": 1890, \"vs_rank16_baseline\": -0.51, \"rank16_baseline_accuracy\": 87.51}\ncls8b-seed123-ckpt200-test-eval | success | {\"accuracy\": 72.55, \"f1_macro\": 70.18, \"pass_f1\": 78.58, \"fail_f1\": 61.78, \"pass_precision\": 91.21, \"pass_recall\": 69.02, \"fail_precision\": 49.54, \"fail_recall\": 82.05, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 72.96, \"unparseable\": 0, \"confusion_matrix\": {\"tn\": 2171, \"\ncls8b-s42-ckpt1000-test-seq2048-ablation | success | {\"accuracy\": 82.83, \"f1_macro\": 76.88, \"fail_precision\": 72.2, \"fail_recall\": 59.3, \"fail_f1\": 65.2, \"pass_precision\": 85.9, \"pass_recall\": 91.5, \"pass_f1\": 88.6, \"unparseable\": 136}\ncls8b-seed123-ckpt6633-test-eval | success | {\"accuracy\": 84.89, \"f1_macro\": 77.56, \"f1_fail\": 64.7, \"f1_pass\": 90.4, \"precision_fail\": 87.8, \"recall_fail\": 51.2, \"precision_pass\": 84.3, \"recall_pass\": 97.4, \"majority_baseline\": 73, \"gap_vs_majority_pp\": 11.9, \"total_samples\": 9784, \"unparseable_count\": 0}\ncls8b-seed123-ckpt6600-test-eval | success | {\"accuracy\": 84.9, \"f1_macro\": 77.58, \"pass_f1\": 90.4, \"fail_f1\": 64.8, \"pass_precision\": 84.3, \"pass_recall\": 97.4, \"fail_precision\": 87.8, \"fail_recall\": 51.3, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 73, \"unparseable\": 0, \"confusion_matrix\": {\"fail_as_fail\": 1357, \"\ncls8b-s42-ckpt200-test8192-eval | success | {\"accuracy\": 70.07, \"f1_macro\": 68.18, \"pass_f1\": 75.9, \"fail_f1\": 60.4, \"pass_precision\": 91.8, \"pass_recall\": 64.7, \"fail_precision\": 47, \"fail_recall\": 84.5, \"n_samples\": 9784, \"n_pass\": 7138, \"n_fail\": 2646, \"majority_baseline\": 73, \"unparseable\": 0, \"confusion_matrix\": {\"fail_as_fail\": 2235, \"f\ncls4b-v5-ckpt600-test5120-eval | success | {\"accuracy\": 77.74, \"f1_macro\": 74.74, \"f1_fail\": 66.03, \"f1_pass\": 83.44, \"precision_fail\": 56.21, \"recall_fail\": 80.01, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 4.78, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-seed123-ckpt6400-test-eval-v2 | success | {\"accuracy\": 85.08, \"f1_fail\": 65.32, \"f1_pass\": 90.49, \"f1_macro\": 77.91, \"precision_fail\": 87.92, \"precision_pass\": 84.54, \"recall_fail\": 51.97, \"recall_pass\": 97.35, \"n_instances\": 9784, \"n_cls_unparseable\": 0}\ncls8b-seed123-ckpt6633-val8192-eval | success | {\"accuracy\": 87.1, \"f1_macro\": 78.79, \"f1_fail\": 65.52, \"f1_pass\": 92.07, \"precision_fail\": 92.26, \"recall_fail\": 50.8, \"precision_pass\": 86.31, \"recall_pass\": 98.64, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.23, \"unparseable_count\": 9, \"total_samples\": 9335}\ncls8b-seed123-ckpt3000-test8192-eval | success | {\"accuracy\": 85.6, \"f1_macro\": 78.38, \"f1_fail\": 65.89, \"f1_pass\": 90.87, \"precision_fail\": 91.65, \"recall_fail\": 51.44, \"precision_pass\": 84.52, \"recall_pass\": 98.26, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.64, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls4b-v5-ckpt4400-test5120-eval | success | {\"accuracy\": 83.24, \"f1_macro\": 74.44, \"f1_fail\": 59.45, \"f1_pass\": 89.44, \"precision_fail\": 85.98, \"recall_fail\": 45.43, \"precision_pass\": 82.78, \"recall_pass\": 97.25, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.28, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-seed123-ckpt6400-val8192-eval | success | {\"accuracy\": 87.48, \"f1_macro\": 79.66, \"f1_fail\": 67.04, \"f1_pass\": 92.27, \"precision_fail\": 91.81, \"recall_fail\": 52.8, \"precision_pass\": 86.78, \"recall_pass\": 98.5, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.6, \"unparseable_count\": 9, \"total_samples\": 9335}\ncls8b-seed123-ckpt6200-val8192-eval | success | {\"accuracy\": 87.52, \"f1_macro\": 79.26, \"f1_fail\": 66.16, \"f1_pass\": 92.35, \"precision_fail\": 95.63, \"recall_fail\": 50.58, \"precision_pass\": 86.33, \"recall_pass\": 99.27, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.64, \"unparseable_count\": 9, \"total_samples\": 9335}\ncls4b-v5-val-sweep-ckpt4600 | success | {\"accuracy\": 90.07, \"f1_macro\": 85.04, \"f1_fail\": 76.37, \"f1_pass\": 93.71, \"precision_fail\": 89.65, \"recall_fail\": 66.52, \"precision_pass\": 90.16, \"recall_pass\": 97.56, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 14.19, \"unparseable_count\": 0, \"total_samples\": 9335, \"n_truncated\": 234}\ncls8b-seed123-ckpt6600-val8192-eval | success | {\"accuracy\": 87.23, \"f1_macro\": 79.02, \"f1_fail\": 65.9, \"f1_pass\": 92.14, \"precision_fail\": 92.6, \"recall_fail\": 51.15, \"precision_pass\": 86.4, \"recall_pass\": 98.7, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 11.36, \"unparseable_count\": 9, \"total_samples\": 9335}\ncls8b-s42-ckpt1600-test8192-eval | success | {\"accuracy\": 84.99, \"f1_macro\": 78.94, \"f1_fail\": 67.65, \"f1_pass\": 90.22, \"precision_fail\": 81.06, \"recall_fail\": 58.05, \"precision_pass\": 85.93, \"recall_pass\": 94.97, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.03, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls4b-v5-ckpt4600-test-eval | success | {\"accuracy\": 83.63, \"f1_macro\": 75.63, \"f1_fail\": 61.67, \"f1_pass\": 89.59, \"precision_fail\": 84.03, \"recall_fail\": 48.72, \"precision_pass\": 83.55, \"recall_pass\": 96.57, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.67, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-s42-ckpt1400-test8192-eval | success | {\"accuracy\": 85.47, \"f1_macro\": 78.9, \"f1_fail\": 67.13, \"f1_pass\": 90.67, \"precision_fail\": 86.43, \"recall_fail\": 54.88, \"precision_pass\": 85.27, \"recall_pass\": 96.81, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 12.51, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-s42-ckpt1200-test8192-eval | success | {\"accuracy\": 83.84, \"f1_macro\": 77.47, \"f1_fail\": 65.49, \"f1_pass\": 89.45, \"precision_fail\": 77.52, \"recall_fail\": 56.69, \"precision_pass\": 85.4, \"recall_pass\": 93.91, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.89, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls8b-s42-ckpt800-test8192-eval | success | {\"accuracy\": 83.53, \"f1_macro\": 78.97, \"f1_fail\": 69.17, \"f1_pass\": 88.77, \"precision_fail\": 70.07, \"recall_fail\": 68.29, \"precision_pass\": 88.36, \"recall_pass\": 89.18, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 10.58, \"unparseable_count\": 0, \"total_samples\": 9784}\ncls4b-v5-val-sweep-ckpt4200 | success | {\"accuracy\": 89.06, \"f1_macro\": 83.07, \"f1_fail\": 73, \"f1_pass\": 93.1, \"precision_fail\": 90.3, \"recall_fail\": 61.3, \"precision_pass\": 88.8, \"recall_pass\": 97.9}\ncls8b-s42-ckpt1600-val8192-v2 | success | {\"accuracy\": 86.75, \"f1_macro\": 78.94, \"f1_fail\": 66.12, \"f1_pass\": 91.76, \"precision_fail\": 86.28, \"precision_pass\": 86.83, \"recall_fail\": 53.6, \"recall_pass\": 97.29, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 10.87, \"unparseable\": 9, \"total\": 9335}\ncls8b-s42-ckpt1400-val8192-eval | success | {\"accuracy\": 85.97, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 10.09, \"f1_macro\": 77.15, \"f1_fail\": 62.95, \"f1_pass\": 91.34, \"precision_fail\": 86.68, \"precision_pass\": 85.85, \"recall_fail\": 49.42, \"recall_pass\": 97.59, \"n_instances\": 9335, \"n_unparseable\": 9, \"confusion_matrix\": {\"tn\": 1113, \ncls4b-v5-val-sweep-ckpt4400-v3 | success | {\"accuracy\": 89.96, \"f1_macro\": 84.94, \"f1_fail\": 76.25, \"f1_pass\": 93.64, \"precision_fail\": 88.84, \"precision_pass\": 90.21, \"recall_fail\": 66.79, \"recall_pass\": 97.33, \"majority_baseline\": 75.88, \"gap_vs_majority_pp\": 14.09, \"n_instances\": 9335, \"n_truncated\": 234, \"n_unparseable\": 0}\ncls8b-s42-ckpt1200-val8192-v3 | success | {\"accuracy\": 87.76, \"f1_macro\": 81.25, \"f1_fail\": 70.2, \"f1_pass\": 92.3, \"precision_fail\": 85, \"recall_fail\": 59.8, \"precision_pass\": 88.3, \"recall_pass\": 96.7, \"majority_baseline\": 75.9, \"gap_vs_majority\": 11.9, \"unparseable\": 9}\ncls8b-s42-ckpt1000-test8192-eval | success | {\"accuracy\": 83.52, \"f1_macro\": 77.5, \"f1_fail\": 65.85, \"f1_pass\": 89.14, \"precision_fail\": 74.93, \"recall_fail\": 58.73, \"precision_pass\": 85.84, \"recall_pass\": 92.72, \"majority_baseline\": 72.96, \"gap_vs_majority\": 10.56, \"unparseable_count\": 0, \"unparseable_rate\": 0, \"total_samples\": 9784, \"tp\": 66\ncls8b-s42-ckpt1000-val8192-eval | success | {\"accuracy\": 88.23, \"f1_macro\": 82.72, \"f1_fail\": 73, \"f1_pass\": 92.5, \"precision_fail\": 81.8, \"recall_fail\": 65.8, \"precision_pass\": 89.8, \"recall_pass\": 95.3, \"unparseable\": 9, \"total_instances\": 9335}\ncls8b-s42-ckpt800-val8192-eval | success | {\"accuracy\": 84.5, \"f1_macro\": 79.2}\ncls4b-v5-ckpt4000-val5120-eval | success | {\"accuracy\": 89.84, \"f1_macro\": 84.25, \"f1_fail\": 74.85, \"f1_pass\": 93.64, \"precision_fail\": 92.95, \"recall_fail\": 62.66, \"precision_pass\": 89.24, \"recall_pass\": 98.49, \"unparseable\": 0, \"truncated\": 234, \"total\": 9335}\ncls4b-v5-ckpt600-val5120-eval | success | {\"accuracy\": 82.82, \"f1_macro\": 79.81, \"f1_fail\": 72.03, \"f1_pass\": 87.6, \"precision_fail\": 59.3, \"recall_fail\": 91.7, \"unparseable\": 0, \"total\": 9335}\nrepo-level-cls-8b-conda | success | {\"val_8192\": {\"ckpt_200\": {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_fail\": 51.6, \"f1_pass\": 70.7, \"unparseable\": 9}, \"ckpt_400\": {\"accuracy\": 80.96}, \"ckpt_600\": {\"accuracy\": 85}, \"best_acc\": \"ckpt_600\"}, \"val_5120\": {\"ckpt_400\": {\"accuracy\": 80.47, \"f1_macro\": 75.84}}, \"test_2048\": {\"ckpt_400\": {\"\ncls8b-s42-ckpt200-val8192-eval-v2 | success | {\"accuracy\": 63.52, \"f1_macro\": 61.17, \"f1_fail\": 51.6, \"f1_pass\": 70.7, \"unparseable\": 9, \"total\": 9335}\ncls4b-seed123-ckpt800-val5120-eval | success | {\"accuracy\": 87.92, \"f1_macro\": 81.95, \"f1_pass\": 92.33, \"f1_fail\": 71.57, \"unparseable\": 0, \"truncated\": 234, \"total\": 9335}\nrepo-level-cls-seed123-home | success | {\"val_2048\": {\"n\": 9335, \"unparseable\": 1883, \"ckpt_200\": {\"accuracy\": 62.51, \"f1_macro\": 55.54, \"f1_pass\": 73.14, \"f1_fail\": 37.94}, \"ckpt_400\": {\"accuracy\": 80.72, \"f1_macro\": 67.03, \"f1_pass\": 88.27, \"f1_fail\": 45.78}, \"ckpt_600\": {\"accuracy\": 76.78, \"f1_macro\": 66.81, \"f1_pass\": 85, \"f1_fail\": 4\ncls8b-s42-ckpt600-test8192-eval | success | {\"accuracy\": 79.05, \"f1_macro\": 75.12, \"f1_fail\": 65.24, \"f1_pass\": 85, \"precision_fail\": 59.16, \"precision_pass\": 88.95, \"recall_fail\": 72.71, \"recall_pass\": 81.4, \"unparseable\": 0, \"total\": 9784, \"majority_baseline\": 73, \"gap_vs_majority_pp\": 6.09}\ncls8b-seed123-ckpt3000-val8192-eval | success | {\"accuracy\": 88.69, \"f1_macro\": 81.73, \"f1_fail\": 70.5, \"f1_pass\": 93, \"precision_fail\": 95.2, \"precision_pass\": 87.6, \"recall_fail\": 55.9, \"recall_pass\": 99.1, \"majority_baseline\": 75.9, \"gap_vs_majority_pp\": 12.8, \"unparseable\": 9, \"total\": 9335}\ncls8b-s42-ckpt400-test8192-eval | success | {\"accuracy\": 84.79, \"f1_macro\": 81.18, \"f1_fail\": 72.93, \"f1_pass\": 89.43, \"precision_fail\": 70.32, \"precision_pass\": 90.74, \"recall_fail\": 75.74, \"recall_pass\": 88.15, \"majority_baseline\": 72.96, \"gap_vs_majority_pp\": 11.84, \"unparseable\": 0, \"total\": 9784}\nrepo-level-cls-v5 | success | {\"checkpoint_sweep\": {\"ckpt_600\": {\"accuracy\": 76.74, \"f1_macro\": 73.74, \"fail_f1\": 64.88, \"pass_f1\": 82.61}, \"ckpt_4000\": {\"accuracy\": 81.51, \"f1_macro\": 72.56, \"fail_f1\": 56.9, \"pass_f1\": 88.23}, \"ckpt_4200\": {\"accuracy\": 80.64, \"f1_macro\": 72.1, \"fail_f1\": 56.66, \"pass_f1\": 87.54}, \"ckpt_4400\": {\nrepo-level-cls-v5-conda | success | {\"checkpoint_sweep\": {\"ckpt_200\": {\"accuracy\": 52.96, \"f1_macro\": 52.89, \"fail_f1\": 51.02, \"pass_f1\": 54.76}, \"ckpt_400\": {\"accuracy\": 78.43, \"f1_macro\": 68.41, \"fail_f1\": 50.61, \"pass_f1\": 86.21, \"fail_precision\": 66.48, \"fail_recall\": 40.85, \"pass_precision\": 80.82, \"pass_recall\": 92.36}, \"ckpt_60\nrepo-level-cwm-v10 | success | {\"accuracy\": 0.6991, \"f1_macro\": 0.4671, \"f1_pass\": 0.8187, \"f1_fail\": 0.1154, \"precision_pass\": 0.7304, \"recall_pass\": 0.9314, \"precision_fail\": 0.2815, \"recall_fail\": 0.0726, \"majority_baseline\": 0.7296, \"n_unparseable\": 9102, \"n_unparseable_pct\": 0.93, \"n_truncated\": 478, \"n_truncated_pct\": 0.048\nrepo-level-cls-v4 | success | {\"accuracy\": 0.6611, \"f1_macro\": 0.5661, \"f1_pass\": 0.769, \"f1_fail\": 0.363, \"precision_pass\": 0.765, \"recall_pass\": 0.774, \"precision_fail\": 0.369, \"recall_fail\": 0.357, \"majority_baseline\": 0.7296, \"n_unparseable\": 132, \"best_checkpoint\": \"checkpoint-200\", \"early_stop\": \"D045\"}\ncwm8b-seed123 | success | {\"overall_accuracy\": 86.98, \"pass_f1\": 86.83, \"fail_f1\": 87.13, \"pass_precision\": 91.12, \"pass_recall\": 82.92, \"fail_precision\": 83.3, \"fail_recall\": 91.34, \"exact_match_rate\": 84.13, \"unparseable\": 0, \"test_set_size\": 1890}\ncls8b-seed123 | success | {\"overall_accuracy\": 89.4, \"pass_f1\": 89.5, \"fail_f1\": 89.2, \"pass_precision\": 91.2, \"pass_recall\": 87.9, \"fail_precision\": 87.5, \"fail_recall\": 90.9, \"train_loss\": 0.3087, \"eval_loss\": 0.0848, \"train_runtime_sec\": 5666, \"unparseable\": 0}\ncls8b-eval-seed123 | success | {\"overall_accuracy\": 89.37, \"pass_f1\": 89.54, \"fail_f1\": 89.19, \"pass_precision\": 91.2, \"pass_recall\": 87.93, \"fail_precision\": 87.54, \"fail_recall\": 90.9, \"unparseable\": 0, \"test_set_size\": 1890}\ncls8b-eval-seed42 | success | {\"overall_accuracy\": 90.48, \"pass_f1\": 90.86, \"fail_f1\": 90.06, \"pass_precision\": 90.22, \"pass_recall\": 91.51, \"fail_precision\": 90.76, \"fail_recall\": 89.36, \"unparseable\": 0, \"test_set_size\": 1890}\ncwm-seed789 | success | {\"overall_accuracy\": 86.67, \"pass_f1\": 86.74, \"fail_f1\": 86.6, \"exact_match_rate\": 83.97, \"baseline_gap_pp\": 34.92, \"test_set_size\": 1890, \"unparseable_predictions\": 0, \"per_class\": {\"fail\": {\"precision\": 84.09, \"recall\": 89.25, \"f1\": 86.6}, \"pass\": {\"precision\": 89.37, \"recall\": 84.25, \"f1\": 86.74}\ncls8b-seed456 | success | {\"overall_accuracy\": 88.31, \"pass_f1\": 88.2, \"fail_f1\": 88.41, \"pass_precision\": 92.29, \"pass_recall\": 84.46, \"fail_precision\": 84.72, \"fail_recall\": 92.43, \"train_loss\": 0.3105, \"eval_loss\": 0.0928, \"unparseable\": 0, \"test_set_size\": 1890}\ncwm8b-seed456 | success | {\"overall_accuracy\": 86.24, \"pass_f1\": 85.96, \"fail_f1\": 86.51, \"pass_precision\": 91.08, \"pass_recall\": 81.39, \"fail_precision\": 82.09, \"fail_recall\": 91.45, \"exact_match_rate\": 82.8, \"train_loss\": 0.2279, \"eval_loss\": 0.0583, \"unparseable\": 0, \"test_set_size\": 1890, \"majority_baseline_accuracy\": 51\n5-paired-clustered-bootstrap | success | {\"pooled_gap_pp\": -0.45, \"pooled_ci_lower\": -1.71, \"pooled_ci_upper\": 0.84, \"pooled_p_value\": 0.499, \"tost_p_value\": 0.0071, \"tost_margin_pp\": 2, \"seed_level_paired_t_p\": 0.425, \"seed_level_mean_gap\": -0.48, \"n_variants_pooled\": 523, \"n_clusters\": 114, \"per_seed_gaps\": {\"seed42\": -0.97, \"seed123\": 1\ncwm-seed0 | success | {\"overall_accuracy\": 87.57, \"fail_f1\": 87.93, \"fail_precision\": 82.71, \"fail_recall\": 93.86, \"pass_f1\": 87.18, \"pass_precision\": 93.45, \"pass_recall\": 81.7, \"exact_match_rate\": 84.29, \"eval_loss\": 0.0665, \"train_loss\": 0.2554, \"train_runtime_sec\": 3586}\nper-test-precision-recall | success | {\"accuracy\": 87.51, \"fail_precision\": 82.75, \"fail_recall\": 93.64, \"fail_f1\": 87.86, \"pass_precision\": 93.24, \"pass_recall\": 81.8, \"pass_f1\": 87.15, \"FP_count\": 58, \"FN_count\": 178, \"best_mutation\": \"return_value (97.26%)\", \"worst_mutation\": \"off_by_one (82.56%)\", \"bucket_6_10_acc\": 96.3, \"bucket_11\ncwm-seed123 | success | {\"overall_accuracy\": 87.2, \"pass_f1\": 86.95, \"fail_f1\": 87.44, \"exact_match_rate\": 84.44, \"majority_baseline_accuracy\": 51.75, \"accuracy_vs_baseline_gap_pp\": 35.45, \"test_set_size\": 1890, \"unparseable_predictions\": 0}\ncwm-seed456 | success | {\"accuracy\": 86.98, \"pass_f1\": 86.66, \"fail_f1\": 87.29, \"pass_precision\": 92.26, \"pass_recall\": 81.7, \"fail_precision\": 82.52, \"fail_recall\": 92.65, \"exact_match_rate\": 84.02, \"train_loss\": 0.2525, \"eval_loss_best\": 0.0551, \"eval_loss_final\": 0.0635, \"train_runtime_sec\": 3440, \"unparseable\": 0}\ncls-seed0 | success | {\"accuracy\": 87.94, \"pass_f1\": 87.79, \"fail_f1\": 88.08, \"pass_precision\": 92.13, \"pass_recall\": 83.84, \"fail_precision\": 84.2, \"fail_recall\": 92.32, \"train_loss\": 0.2347, \"eval_loss\": 0.0963, \"train_runtime_sec\": 4976.75, \"unparseable\": 0}\ncls-seed789 | success | {\"accuracy\": 89, \"pass_f1\": 88.9, \"fail_f1\": 89.1, \"pass_precision\": 93.3, \"pass_recall\": 84.9, \"fail_precision\": 85.2, \"fail_recall\": 93.4}\ntraj-level-finetuned | success | {\"accuracy\": 85.66, \"unresolved_f1\": 87.5, \"resolved_f1\": 83.18, \"per_test_consistency\": 79.94}\ntraj-level-seed456 | success | {\"overall_accuracy\": 87.4, \"unresolved_f1\": 88.7, \"resolved_f1\": 85.8, \"unresolved_precision\": 85.7, \"unresolved_recall\": 91.9, \"resolved_precision\": 89.7, \"resolved_recall\": 82.3, \"consistency_rate\": 78.8}\ntraj-level-seed789 | success | {\"overall_accuracy\": 87.31, \"unresolved_f1\": 88.27, \"resolved_f1\": 86.17, \"unresolved_precision\": 87.41, \"unresolved_recall\": 89.15, \"resolved_precision\": 87.18, \"resolved_recall\": 85.18, \"consistency_rate\": 76.74, \"eval_loss\": 0.1115, \"train_loss\": 0.2255, \"train_runtime_sec\": 2055.9}\ntraj-level-seed0 | success | {\"overall_accuracy\": 85.66, \"unresolved_f1\": 87.37, \"resolved_f1\": 83.41, \"unresolved_precision\": 82.71, \"unresolved_recall\": 92.59, \"resolved_precision\": 90.07, \"resolved_recall\": 77.66, \"consistency_rate\": 79.55, \"train_loss\": 0.225, \"eval_loss_epoch1\": 0.0949, \"eval_loss_epoch2\": 0.0885, \"eval_lo\nblock-corr-empirical | success | {\"icc\": 0.1909, \"icc_p_value\": 0, \"design_effect\": 3.9676, \"overall_error_rate\": 0.1249, \"all_correct_observed\": 46, \"all_correct_expected_iid\": 16.35, \"all_correct_ratio\": 2.81, \"error_std_observed\": 0.1531, \"error_std_expected_iid\": 0.0811, \"error_std_ratio\": 1.89, \"n_samples\": 1890, \"n_problems\":\nmodel-size-scaling-cwm8b | success | {\"accuracy\": 87.67, \"pass_f1\": 87.57, \"fail_f1\": 87.77, \"pass_precision\": 91.53, \"pass_recall\": 83.95, \"fail_precision\": 84.19, \"fail_recall\": 91.67, \"exact_match_rate\": 84.39, \"train_loss\": 0.229, \"eval_loss_epoch1\": 0.0554, \"eval_loss_epoch2\": 0.0512, \"eval_loss_epoch3\": 0.0564, \"train_runtime_sec\nmodel-size-scaling-cls8b | success | {\"accuracy\": 90.48, \"pass_f1\": 90.86, \"fail_f1\": 90.06, \"pass_precision\": 90.22, \"pass_recall\": 91.51, \"fail_precision\": 90.76, \"fail_recall\": 89.36, \"train_loss\": 0.3125, \"eval_loss_epoch1\": 0.0723, \"eval_loss_epoch2\": 0.0741, \"eval_loss_epoch3\": 0.0783, \"train_runtime_sec\": 5614, \"unparseable\": 0}\nllm-judge-32b-zeroshot | success | {\"overall_accuracy\": 71.69, \"majority_baseline\": 51.75, \"accuracy_vs_baseline_gap\": 19.95, \"fail_precision\": 64.4, \"fail_recall\": 92.43, \"fail_f1\": 75.91, \"pass_precision\": 88.12, \"pass_recall\": 52.35, \"pass_f1\": 65.68, \"unparseable_predictions\": 0, \"trajectory_accuracy\": 99.12, \"trajectory_total_pr\nllm-judge-8b-zeroshot | success | {\"overall_accuracy\": 64.4, \"fail_precision\": 57.9, \"fail_recall\": 95.8, \"fail_f1\": 72.2, \"pass_precision\": 90, \"pass_recall\": 35.1, \"pass_f1\": 50.5, \"majority_baseline\": 51.7, \"accuracy_vs_baseline_gap\": 12.6, \"traj_accuracy\": 99.1, \"traj_problems\": 114, \"traj_true_resolved\": 1, \"traj_pred_resolved\"\ntraj-level-seed123 | success | {\"overall_accuracy\": 85.47, \"unresolved_f1\": 87, \"resolved_f1\": 83.52, \"unresolved_precision\": 83.53, \"unresolved_recall\": 90.78, \"resolved_precision\": 88.17, \"resolved_recall\": 79.33, \"consistency_rate\": 78.59}\noracle-f2p-stratified | success | {\"T1_pct\": 68.7, \"T1_block_adv\": -0.09, \"T2_pct\": 19.1, \"T2_block_adv\": 31.69, \"T3_5_pct\": 7.1, \"T3_5_block_adv\": 40.74, \"T6plus_pct\": 5.1, \"T6plus_block_adv\": 40.06, \"overall_block_adv\": 10.93, \"T2_contribution_pct\": 55.3}\nmvp-b-train | success | {\"overall_accuracy\": 0.875, \"pass_f1\": 0.871, \"fail_f1\": 0.879, \"pass_precision\": 0.9324, \"pass_recall\": 0.818, \"fail_precision\": 0.8275, \"fail_recall\": 0.9364, \"majority_baseline\": 0.52, \"accuracy_vs_majority_gap\": 0.355}\nmulti-seed-core | success | {\"seed42\": {\"accuracy\": 87.83, \"pass_f1\": 88.06, \"fail_f1\": 87.59, \"pass_precision\": 89.45, \"pass_recall\": 86.71, \"fail_precision\": 86.2, \"fail_recall\": 89.04}, \"seed123\": {\"accuracy\": 89.52, \"pass_f1\": 89.64, \"fail_f1\": 89.4, \"pass_precision\": 91.76, \"pass_recall\": 87.63, \"fail_precision\": 87.34, \"\nmvp-a-oracle-sim | success | {\"original_T12\": {\"iid_adv_70_85\": 0.1849, \"block_adv_70_85\": 0.3618}, \"sensitivity_T3\": {\"iid_adv_70_85\": 0.0761, \"block_adv_70_85\": 0.3839}, \"sensitivity_T7\": {\"iid_adv_70_85\": 0.1351, \"block_adv_70_85\": 0.3833}, \"sensitivity_T11\": {\"iid_adv_70_85\": 0.1863, \"block_adv_70_85\": 0.3639}, \"real_f2p_T1\n",
      "numLines": 144,
      "startLine": 1,
      "totalLines": 144
    }
  }
}
```

</details>

---


### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full registry data. Let me extract all the key numbers I need. Let me now systematically go through each audit item.

Let me first organize what I've found from the registry:

**14B function-level results:**
- cls14b-func-s42-v2: accuracy 89.47 (but wait, there's a cls14b-func-s42-v2 with 89.47... hmm, the paper says 89.21 for s42)
- cls14b-func-s123: accuracy 90.79 ✓


- cls14b-func-s456: accuracy 89.79 ✓
- cwm14b-func-s42: accuracy 89.3 (but paper says 89.26 for s42?)
- cwm14b-func-s123: accuracy 88.99 ✓
- cwm14b-func-s456: accuracy 90.26 ✓
- traj14b-func-s42: accuracy 89.73 ✓
- traj14b-func-s123: accuracy 88.57 ✓
- traj14b-func-s456: accuracy 88.28 ✓

I'm noticing some discrepancies between the registry values and what the paper reports, particularly for the s42 seed variants.  The cls14b-func-s42-v2 shows 89.47 in the registry while the paper lists 89.21, and cwm14b-func-s42 is 89.3 versus the paper's 89.26. The v2 suffix suggests this might be a re-run, so I need to check if there's an original cls14b-func-s42 entry I'm missing or if the versioning indicates different experimental conditions.

Now looking at the 4B function-level results across multiple seeds. For CLS 4B, I see multi-seed-core entries with seed42 at 87.83 and seed123 at 89.52. For CWM 4B, there's a spread across different seeds ranging from about 86.67 to 87.57, with seed42 showing 87.51 and seed0 at 87.57. Now I'm looking at the trajectory-level results across all five seeds to calculate the 4B baseline mean and standard deviation, comparing them against the CLS variants. I'm working through the naming convention to identify which entries correspond to CWM 4B—it looks like the baseline 4B model uses the cwm-seed prefix, while the 8B variant has cwm8b-seed, so I need to pull together the five seed results for the 4B version. Let me verify this calculation: adding those five accuracy values gives 435.93, which divides to 87.186—matching the paper's reported 87.19. For the standard deviation, I'm computing the squared deviations from the mean, which sum to 0.5614, giving a variance of 0.14 when divided by 4.

Now I'm moving to the CLS 4B results. I can see seed42=87.83, seed123=89.52, seed789=89.00, and seed0=87.94 in the data, but I'm having trouble locating the fifth seed value (seed456) that would complete the set. The paper reports CLS 4B = 88.43 ± 0.78, so with these four values I'm getting a mean of around 88.57, which is close but I need to find that missing fifth seed to verify the exact average and standard deviation. I'm noticing there are duplicate entries in the registry for the 8B CLS model with seed 123 — one shows 89.40 and another shows 89.37 — but the paper uses 89.40, which matches the primary entry. Now I need to locate the specific artifact files to extract the statistics I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "77d7dc0f-3bc6-4341-8d86-4040a4df1d68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSjhArcDPCkeEsEaycey3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18030,
      "cache_read_input_tokens": 74697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18030
      },
      "output_tokens": 8,
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


### Assistant

_source line 58_

Good, I have the registry data. Now let me find the statistical artifacts and verify the 14B CLS s42 discrepancy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "67268ca5-9fb4-4bf7-a62a-cd5a076c1875",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSjhArcDPCkeEsEaycey3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18030,
      "cache_read_input_tokens": 74697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18030
      },
      "output_tokens": 8,
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

_source line 59_

<details open><summary>🔧 Tool call — Glob · `toolu_018h1rt1NokZyLE5AfJmdVnG`</summary>

```json
{
  "pattern": "artifacts/*holm*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "dede73a2-1c6d-4171-9f4e-c69b771ab673",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSjhArcDPCkeEsEaycey3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18030,
      "cache_read_input_tokens": 74697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18030
      },
      "output_tokens": 8,
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

_source line 60 · 2026-05-23T19:19:04.801Z_

<details><summary>↩ Tool result · `toolu_018h1rt1NokZyLE5AfJmdVnG`</summary>

```text
artifacts/holm_bonferroni.py
artifacts/holm_bonferroni_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "c2b9c24e-c146-4a48-b2d3-069a4d11f49a",
  "tool_use_result": {
    "filenames": [
      "artifacts/holm_bonferroni.py",
      "artifacts/holm_bonferroni_results.json"
    ],
    "durationMs": 41,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Glob · `toolu_01ULgzxVwxZsDjkviSMssUyS`</summary>

```json
{
  "pattern": "artifacts/*bayesian*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "ce817e76-5ee8-4be0-aafc-d3849aa1fb39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSjhArcDPCkeEsEaycey3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18030,
      "cache_read_input_tokens": 74697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18030
      },
      "output_tokens": 8,
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

_source line 62 · 2026-05-23T19:19:05.303Z_

<details><summary>↩ Tool result · `toolu_01ULgzxVwxZsDjkviSMssUyS`</summary>

```text
artifacts/bayesian_rope_report.md
artifacts/compute_bayesian_rope.py
artifacts/bayesian_rope_results_reproduced.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "30f702f6-7886-4760-994b-6b46cfeffb9a",
  "tool_use_result": {
    "filenames": [
      "artifacts/bayesian_rope_report.md",
      "artifacts/compute_bayesian_rope.py",
      "artifacts/bayesian_rope_results_reproduced.json"
    ],
    "durationMs": 39,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Glob · `toolu_01Nkxea4WiLWJuL2cQvQ4XsQ`</summary>

```json
{
  "pattern": "artifacts/*14b*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "03196350-8b42-4563-a8b4-e11f734fe8d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSjhArcDPCkeEsEaycey3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18030,
      "cache_read_input_tokens": 74697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18030
      },
      "output_tokens": 8,
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

_source line 64 · 2026-05-23T19:19:09.525Z_

<details><summary>↩ Tool result · `toolu_01Nkxea4WiLWJuL2cQvQ4XsQ`</summary>

```text
artifacts/14b_upgrade_checklist.txt
artifacts/eval_14b_multiseed.sh
artifacts/update_14b_table.py
artifacts/compute_14b_seed_level_stats.py
artifacts/14b_seed_level_stats.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "37ce704b-6ca6-4865-93aa-d6dc38fd738d",
  "tool_use_result": {
    "filenames": [
      "artifacts/14b_upgrade_checklist.txt",
      "artifacts/eval_14b_multiseed.sh",
      "artifacts/update_14b_table.py",
      "artifacts/compute_14b_seed_level_stats.py",
      "artifacts/14b_seed_level_stats.json"
    ],
    "durationMs": 42,
    "numFiles": 5,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Glob · `toolu_01UBfEvqMnwgh1QfCty4P2nE`</summary>

```json
{
  "pattern": "artifacts/*routing*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "53da039d-293f-450b-b3fc-3c502892d1ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSjhArcDPCkeEsEaycey3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18030,
      "cache_read_input_tokens": 74697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18030
      },
      "output_tokens": 8,
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

_source line 66 · 2026-05-23T19:19:09.734Z_

<details><summary>↩ Tool result · `toolu_01UBfEvqMnwgh1QfCty4P2nE`</summary>

```text
artifacts/routing_analysis_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "b5fb5f2c-4232-4374-9c89-897cf1b96fcc",
  "tool_use_result": {
    "filenames": [
      "artifacts/routing_analysis_report.md"
    ],
    "durationMs": 49,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Glob · `toolu_01B286wMNSjL79H2zdgDhSA3`</summary>

```json
{
  "pattern": "artifacts/*oracle*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "8dab853c-b1d7-4c0c-86d9-dbf465ea0df4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSjhArcDPCkeEsEaycey3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18030,
      "cache_read_input_tokens": 74697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18030
      },
      "output_tokens": 8,
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

_source line 68_

<details open><summary>🔧 Tool call — Glob · `toolu_01GqpqvkqJNYoWze62y7VvmM`</summary>

```json
{
  "pattern": "*oracle*3seed*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "58f5114e-17f6-4d40-b5c6-19031705c370",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSjhArcDPCkeEsEaycey3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18030,
      "cache_read_input_tokens": 74697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18030
      },
      "output_tokens": 8,
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

_source line 69 · 2026-05-23T19:19:09.849Z_

<details><summary>↩ Tool result · `toolu_01B286wMNSjL79H2zdgDhSA3`</summary>

```text
artifacts/oracle_icc_sensitivity.json
artifacts/oracle_icc_sensitivity.pdf
artifacts/oracle_icc_sensitivity.png
artifacts/oracle_frontier_dual_icc.md
artifacts/fig3_oracle_stratified.py
artifacts/fig3_oracle_stratified.pdf
artifacts/fig3_oracle_stratified.png
artifacts/compute_oracle_3seed.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "b456c949-2159-4655-a172-e5b97d12b5ca",
  "tool_use_result": {
    "filenames": [
      "artifacts/oracle_icc_sensitivity.json",
      "artifacts/oracle_icc_sensitivity.pdf",
      "artifacts/oracle_icc_sensitivity.png",
      "artifacts/oracle_frontier_dual_icc.md",
      "artifacts/fig3_oracle_stratified.py",
      "artifacts/fig3_oracle_stratified.pdf",
      "artifacts/fig3_oracle_stratified.png",
      "artifacts/compute_oracle_3seed.py"
    ],
    "durationMs": 76,
    "numFiles": 8,
    "truncated": false
  }
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-23T19:19:09.883Z_

<details><summary>↩ Tool result · `toolu_01GqpqvkqJNYoWze62y7VvmM`</summary>

```text
artifacts/compute_oracle_3seed.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "564ab520-744a-410a-b3c5-adce9416966b",
  "tool_use_result": {
    "filenames": [
      "artifacts/compute_oracle_3seed.py"
    ],
    "durationMs": 55,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Read · `toolu_017kQW6RQwGmh7TEacYkUgbh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/holm_bonferroni_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "7e03ae80-7a83-40cd-8053-72c1d1be615d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELbkVamxKPob8FgizuBXi9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 92727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3867
      },
      "output_tokens": 69,
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

_source line 72 · 2026-05-23T19:19:12.797Z_

<details><summary>↩ Tool result · `toolu_017kQW6RQwGmh7TEacYkUgbh`</summary>

```text
1	{
2	  "method": "Holm-Bonferroni",
3	  "k": 5,
4	  "alpha": 0.05,
5	  "results": [
6	    {
7	      "rank": 1,
8	      "comparison": "Repo: CLS vs CWM (Qwen3-8B)",
9	      "level": "repo",
10	      "raw_p": 0.003,
11	      "multiplier": 5,
12	      "adj_p": 0.015,
13	      "significant": true,
14	      "note": "paired bootstrap, diff=+29.17pp"
15	    },
16	    {
17	      "rank": 2,
18	      "comparison": "Func: CLS vs CWM (TOST \u00b12pp)",
19	      "level": "function",
20	      "raw_p": 0.007,
21	      "multiplier": 4,
22	      "adj_p": 0.028,
23	      "significant": true,
24	      "note": "seed-level paired t-test, 5 seeds (same as clustered bootstrap)"
25	    },
26	    {
27	      "rank": 3,
28	      "comparison": "Func: CLS vs TRAJ (TOST \u00b12pp)",
29	      "level": "function",
30	      "raw_p": 0.025,
31	      "multiplier": 3,
32	      "adj_p": 0.075,
33	      "significant": false,
34	      "note": "seed-level paired t-test, 5 seeds, df=4"
35	    },
36	    {
37	      "rank": 4,
38	      "comparison": "Repo: CWM vs TRAJ (Qwen3-8B)",
39	      "level": "repo",
40	      "raw_p": 0.039,
41	      "multiplier": 2,
42	      "adj_p": 0.078,
43	      "significant": false,
44	      "note": "unpaired bootstrap, diff=-20.83pp"
45	    },
46	    {
47	      "rank": 5,
48	      "comparison": "Repo: CLS vs TRAJ (Qwen3-8B)",
49	      "level": "repo",
50	      "raw_p": 0.385,
51	      "multiplier": 1,
52	      "adj_p": 0.385,
53	      "significant": false,
54	      "note": "unpaired bootstrap, diff=+8.33pp"
55	    }
56	  ]
57	}
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "a3be99e9-fefb-4cff-9d89-ce83a056fb04",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/holm_bonferroni_results.json",
      "content": "{\n  \"method\": \"Holm-Bonferroni\",\n  \"k\": 5,\n  \"alpha\": 0.05,\n  \"results\": [\n    {\n      \"rank\": 1,\n      \"comparison\": \"Repo: CLS vs CWM (Qwen3-8B)\",\n      \"level\": \"repo\",\n      \"raw_p\": 0.003,\n      \"multiplier\": 5,\n      \"adj_p\": 0.015,\n      \"significant\": true,\n      \"note\": \"paired bootstrap, diff=+29.17pp\"\n    },\n    {\n      \"rank\": 2,\n      \"comparison\": \"Func: CLS vs CWM (TOST \\u00b12pp)\",\n      \"level\": \"function\",\n      \"raw_p\": 0.007,\n      \"multiplier\": 4,\n      \"adj_p\": 0.028,\n      \"significant\": true,\n      \"note\": \"seed-level paired t-test, 5 seeds (same as clustered bootstrap)\"\n    },\n    {\n      \"rank\": 3,\n      \"comparison\": \"Func: CLS vs TRAJ (TOST \\u00b12pp)\",\n      \"level\": \"function\",\n      \"raw_p\": 0.025,\n      \"multiplier\": 3,\n      \"adj_p\": 0.075,\n      \"significant\": false,\n      \"note\": \"seed-level paired t-test, 5 seeds, df=4\"\n    },\n    {\n      \"rank\": 4,\n      \"comparison\": \"Repo: CWM vs TRAJ (Qwen3-8B)\",\n      \"level\": \"repo\",\n      \"raw_p\": 0.039,\n      \"multiplier\": 2,\n      \"adj_p\": 0.078,\n      \"significant\": false,\n      \"note\": \"unpaired bootstrap, diff=-20.83pp\"\n    },\n    {\n      \"rank\": 5,\n      \"comparison\": \"Repo: CLS vs TRAJ (Qwen3-8B)\",\n      \"level\": \"repo\",\n      \"raw_p\": 0.385,\n      \"multiplier\": 1,\n      \"adj_p\": 0.385,\n      \"significant\": false,\n      \"note\": \"unpaired bootstrap, diff=+8.33pp\"\n    }\n  ]\n}\n",
      "numLines": 58,
      "startLine": 1,
      "totalLines": 58
    }
  }
}
```

</details>

---


### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Read · `toolu_01KoSh1UCdFprmkqhuTA3Wpj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/bayesian_rope_results_reproduced.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "a4f39b9e-d3df-475b-bd95-2f31e6e7fb4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELbkVamxKPob8FgizuBXi9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 92727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3867
      },
      "output_tokens": 69,
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

_source line 74 · 2026-05-23T19:19:13.108Z_

<details><summary>↩ Tool result · `toolu_01KoSh1UCdFprmkqhuTA3Wpj`</summary>

```text
1	{
2	  "method": "Bayesian ROPE (Kruschke 2013)",
3	  "prior": "Jeffreys (non-informative)",
4	  "posterior": "t(n-1, x_bar, s/sqrt(n))",
5	  "rope_margin_pp": 2.0,
6	  "results": [
7	    {
8	      "n": 5,
9	      "mean_diff_pp": 1.048,
10	      "sd_pp": 0.765,
11	      "se_pp": 0.342,
12	      "df": 4,
13	      "rope": [
14	        -2.0,
15	        2.0
16	      ],
17	      "p_rope": 0.975,
18	      "p_above_rope": 0.025,
19	      "p_below_rope": 0.0,
20	      "hdi_95_lo": 0.1,
21	      "hdi_95_hi": 2.0,
22	      "hdi_inside_rope": true,
23	      "decision_continuous": "Equivalence supported",
24	      "decision_hdi": "Accept equivalence (95% HDI inside ROPE)",
25	      "comparison": "CLS-CWM per-test (8B, 5 seeds)",
26	      "source": "bayesian_rope_report.md, from per-seed per-test accuracy diffs"
27	    },
28	    {
29	      "n": 5,
30	      "mean_diff_pp": 1.934,
31	      "sd_pp": 1.279,
32	      "se_pp": 0.572,
33	      "df": 4,
34	      "rope": [
35	        -2.0,
36	        2.0
37	      ],
38	      "p_rope": 0.542,
39	      "p_above_rope": 0.457,
40	      "p_below_rope": 0.001,
41	      "hdi_95_lo": 0.35,
42	      "hdi_95_hi": 3.52,
43	      "hdi_inside_rope": false,
44	      "decision_continuous": "Inconclusive",
45	      "decision_hdi": "Undecided (95% HDI overlaps ROPE boundary)",
46	      "comparison": "CLS-TRAJ per-test (8B, 5 seeds)",
47	      "source": "bayesian_rope_report.md, from per-seed per-test accuracy diffs"
48	    },
49	    {
50	      "n": 5,
51	      "mean_diff_pp": -0.486,
52	      "sd_pp": 1.219,
53	      "se_pp": 0.545,
54	      "df": 4,
55	      "rope": [
56	        -2.0,
57	        2.0
58	      ],
59	      "p_rope": 0.97,
60	      "p_above_rope": 0.005,
61	      "p_below_rope": 0.025,
62	      "hdi_95_lo": -2.0,
63	      "hdi_95_hi": 1.03,
64	      "hdi_inside_rope": true,
65	      "decision_continuous": "Equivalence supported",
66	      "decision_hdi": "Accept equivalence (95% HDI inside ROPE)",
67	      "comparison": "CLS-TRAJ variant (8B, 5 seeds)",
68	      "source": "tost_margin_sweep_cls_traj.json, variant-level paired diffs"
69	    },
70	    {
71	      "n": 3,
72	      "mean_diff_pp": 1.07,
73	      "sd_pp": 1.422,
74	      "se_pp": 0.821,
75	      "df": 2,
76	      "rope": [
77	        -2.0,
78	        2.0
79	      ],
80	      "p_rope": 0.78,
81	      "p_above_rope": 0.187,
82	      "p_below_rope": 0.032,
83	      "hdi_95_lo": -2.46,
84	      "hdi_95_hi": 4.6,
85	      "hdi_inside_rope": false,
86	      "decision_continuous": "Inconclusive",
87	      "decision_hdi": "Undecided (95% HDI overlaps ROPE boundary)",
88	      "comparison": "CLS-TRAJ (14B, 3 seeds)",
89	      "source": "registry: CLS_14B=[89.21, 90.79, 89.79], TRAJ_14B=[89.73, 88.57, 88.28], diffs=[-0.52, 2.22, 1.51]"
90	    }
91	  ]
92	}
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "50eb7150-efa0-4a95-b826-c086579b9721",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/bayesian_rope_results_reproduced.json",
      "content": "{\n  \"method\": \"Bayesian ROPE (Kruschke 2013)\",\n  \"prior\": \"Jeffreys (non-informative)\",\n  \"posterior\": \"t(n-1, x_bar, s/sqrt(n))\",\n  \"rope_margin_pp\": 2.0,\n  \"results\": [\n    {\n      \"n\": 5,\n      \"mean_diff_pp\": 1.048,\n      \"sd_pp\": 0.765,\n      \"se_pp\": 0.342,\n      \"df\": 4,\n      \"rope\": [\n        -2.0,\n        2.0\n      ],\n      \"p_rope\": 0.975,\n      \"p_above_rope\": 0.025,\n      \"p_below_rope\": 0.0,\n      \"hdi_95_lo\": 0.1,\n      \"hdi_95_hi\": 2.0,\n      \"hdi_inside_rope\": true,\n      \"decision_continuous\": \"Equivalence supported\",\n      \"decision_hdi\": \"Accept equivalence (95% HDI inside ROPE)\",\n      \"comparison\": \"CLS-CWM per-test (8B, 5 seeds)\",\n      \"source\": \"bayesian_rope_report.md, from per-seed per-test accuracy diffs\"\n    },\n    {\n      \"n\": 5,\n      \"mean_diff_pp\": 1.934,\n      \"sd_pp\": 1.279,\n      \"se_pp\": 0.572,\n      \"df\": 4,\n      \"rope\": [\n        -2.0,\n        2.0\n      ],\n      \"p_rope\": 0.542,\n      \"p_above_rope\": 0.457,\n      \"p_below_rope\": 0.001,\n      \"hdi_95_lo\": 0.35,\n      \"hdi_95_hi\": 3.52,\n      \"hdi_inside_rope\": false,\n      \"decision_continuous\": \"Inconclusive\",\n      \"decision_hdi\": \"Undecided (95% HDI overlaps ROPE boundary)\",\n      \"comparison\": \"CLS-TRAJ per-test (8B, 5 seeds)\",\n      \"source\": \"bayesian_rope_report.md, from per-seed per-test accuracy diffs\"\n    },\n    {\n      \"n\": 5,\n      \"mean_diff_pp\": -0.486,\n      \"sd_pp\": 1.219,\n      \"se_pp\": 0.545,\n      \"df\": 4,\n      \"rope\": [\n        -2.0,\n        2.0\n      ],\n      \"p_rope\": 0.97,\n      \"p_above_rope\": 0.005,\n      \"p_below_rope\": 0.025,\n      \"hdi_95_lo\": -2.0,\n      \"hdi_95_hi\": 1.03,\n      \"hdi_inside_rope\": true,\n      \"decision_continuous\": \"Equivalence supported\",\n      \"decision_hdi\": \"Accept equivalence (95% HDI inside ROPE)\",\n      \"comparison\": \"CLS-TRAJ variant (8B, 5 seeds)\",\n      \"source\": \"tost_margin_sweep_cls_traj.json, variant-level paired diffs\"\n    },\n    {\n      \"n\": 3,\n      \"mean_diff_pp\": 1.07,\n      \"sd_pp\": 1.422,\n      \"se_pp\": 0.821,\n      \"df\": 2,\n      \"rope\": [\n        -2.0,\n        2.0\n      ],\n      \"p_rope\": 0.78,\n      \"p_above_rope\": 0.187,\n      \"p_below_rope\": 0.032,\n      \"hdi_95_lo\": -2.46,\n      \"hdi_95_hi\": 4.6,\n      \"hdi_inside_rope\": false,\n      \"decision_continuous\": \"Inconclusive\",\n      \"decision_hdi\": \"Undecided (95% HDI overlaps ROPE boundary)\",\n      \"comparison\": \"CLS-TRAJ (14B, 3 seeds)\",\n      \"source\": \"registry: CLS_14B=[89.21, 90.79, 89.79], TRAJ_14B=[89.73, 88.57, 88.28], diffs=[-0.52, 2.22, 1.51]\"\n    }\n  ]\n}\n",
      "numLines": 93,
      "startLine": 1,
      "totalLines": 93
    }
  }
}
```

</details>

---


### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Read · `toolu_018iXc1eQV6Jez46mnCg7ohq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/14b_seed_level_stats.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "38ad25a7-7555-42e3-98ea-1df07ba76338",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELbkVamxKPob8FgizuBXi9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 92727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3867
      },
      "output_tokens": 69,
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

_source line 76 · 2026-05-23T19:19:13.577Z_

<details><summary>↩ Tool result · `toolu_018iXc1eQV6Jez46mnCg7ohq`</summary>

```text
1	{
2	  "title": "14B Seed-Level Statistical Analysis (D169 compliant)",
3	  "method": "Seed-level paired t-test (training seeds = replication unit)",
4	  "n_seeds": 3,
5	  "df": 2,
6	  "rope_margin_pp": 2.0,
7	  "data": {
8	    "CLS_14B": {
9	      "s42": 89.21,
10	      "s123": 90.79,
11	      "s456": 89.79
12	    },
13	    "CWM_14B": {
14	      "s42": 89.26,
15	      "s123": 88.99,
16	      "s456": 90.26
17	    },
18	    "TRAJ_14B": {
19	      "s42": 89.73,
20	      "s123": 88.57,
21	      "s456": 88.28
22	    },
23	    "note": "All bf16-consistent. CLS s42=89.21 from bf16 eval (NF4=89.47). CWM s42=89.26 from bf16 eval (NF4=89.30)."
24	  },
25	  "results": {
26	    "CLS-CWM": {
27	      "tost": {
28	        "method": "seed-level paired TOST (D169)",
29	        "n_seeds": 3,
30	        "df": 2,
31	        "mean_diff_pp": 0.4267,
32	        "sd_pp": 1.2077,
33	        "se_pp": 0.6973,
34	        "margin_pp": 2.0,
35	        "t_lower": 3.4801,
36	        "t_upper": -2.2564,
37	        "p_lower": 0.036785,
38	        "p_upper": 0.076338,
39	        "tost_p": 0.076338,
40	        "equivalent_at_alpha05": false,
41	        "ci90_pp": [
42	          -1.609,
43	          2.463
44	        ],
45	        "ci90_inside_rope": false,
46	        "ci95_pp": [
47	          -2.574,
48	          3.427
49	        ],
50	        "diffs": [
51	          -0.05,
52	          1.8,
53	          -0.47
54	        ]
55	      },
56	      "bayesian_rope": {
57	        "method": "Bayesian ROPE (Kruschke 2013, Jeffreys prior)",
58	        "n": 3,
59	        "df": 2,
60	        "mean_diff_pp": 0.4267,
61	        "sd_pp": 1.2077,
62	        "se_pp": 0.6973,
63	        "rope": [
64	          -2.0,
65	          2.0
66	        ],
67	        "p_rope": 0.8869,
68	        "p_above_rope": 0.0763,
69	        "p_below_rope": 0.0368,
70	        "hdi_95_lo": -2.57,
71	        "hdi_95_hi": 3.43,
72	        "hdi_inside_rope": false,
73	        "decision_continuous": "Inconclusive",
74	        "decision_hdi": "Undecided (95% HDI overlaps ROPE boundary)"
75	      }
76	    },
77	    "CLS-TRAJ": {
78	      "tost": {
79	        "method": "seed-level paired TOST (D169)",
80	        "n_seeds": 3,
81	        "df": 2,
82	        "mean_diff_pp": 1.07,
83	        "sd_pp": 1.422,
84	        "se_pp": 0.821,
85	        "margin_pp": 2.0,
86	        "t_lower": 3.7394,
87	        "t_upper": -1.1328,
88	        "p_lower": 0.032329,
89	        "p_upper": 0.187417,
90	        "tost_p": 0.187417,
91	        "equivalent_at_alpha05": false,
92	        "ci90_pp": [
93	          -1.327,
94	          3.467
95	        ],
96	        "ci90_inside_rope": false,
97	        "ci95_pp": [
98	          -2.462,
99	          4.602
100	        ],
101	        "diffs": [
102	          -0.52,
103	          2.22,
104	          1.51
105	        ]
106	      },
107	      "bayesian_rope": {
108	        "method": "Bayesian ROPE (Kruschke 2013, Jeffreys prior)",
109	        "n": 3,
110	        "df": 2,
111	        "mean_diff_pp": 1.07,
112	        "sd_pp": 1.422,
113	        "se_pp": 0.821,
114	        "rope": [
115	          -2.0,
116	          2.0
117	        ],
118	        "p_rope": 0.7803,
119	        "p_above_rope": 0.1874,
120	        "p_below_rope": 0.0323,
121	        "hdi_95_lo": -2.46,
122	        "hdi_95_hi": 4.6,
123	        "hdi_inside_rope": false,
124	        "decision_continuous": "Inconclusive",
125	        "decision_hdi": "Undecided (95% HDI overlaps ROPE boundary)"
126	      }
127	    }
128	  },
129	  "paper_comparison": {
130	    "CLS-TRAJ": {
131	      "seed_level_tost_p": 0.187417,
132	      "paper_tost_p": 0.043,
133	      "match": false,
134	      "seed_level_p_rope": 0.7803,
135	      "paper_p_rope": 0.956,
136	      "match_rope": false,
137	      "diagnosis": "Paper values (p=0.043, P(ROPE)=0.956) are from per-test clustered bootstrap, NOT seed-level. D169 requires seed-level values."
138	    }
139	  }
140	}
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "147d1f85-9ca0-49b1-8144-0c472f5ae787",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/14b_seed_level_stats.json",
      "content": "{\n  \"title\": \"14B Seed-Level Statistical Analysis (D169 compliant)\",\n  \"method\": \"Seed-level paired t-test (training seeds = replication unit)\",\n  \"n_seeds\": 3,\n  \"df\": 2,\n  \"rope_margin_pp\": 2.0,\n  \"data\": {\n    \"CLS_14B\": {\n      \"s42\": 89.21,\n      \"s123\": 90.79,\n      \"s456\": 89.79\n    },\n    \"CWM_14B\": {\n      \"s42\": 89.26,\n      \"s123\": 88.99,\n      \"s456\": 90.26\n    },\n    \"TRAJ_14B\": {\n      \"s42\": 89.73,\n      \"s123\": 88.57,\n      \"s456\": 88.28\n    },\n    \"note\": \"All bf16-consistent. CLS s42=89.21 from bf16 eval (NF4=89.47). CWM s42=89.26 from bf16 eval (NF4=89.30).\"\n  },\n  \"results\": {\n    \"CLS-CWM\": {\n      \"tost\": {\n        \"method\": \"seed-level paired TOST (D169)\",\n        \"n_seeds\": 3,\n        \"df\": 2,\n        \"mean_diff_pp\": 0.4267,\n        \"sd_pp\": 1.2077,\n        \"se_pp\": 0.6973,\n        \"margin_pp\": 2.0,\n        \"t_lower\": 3.4801,\n        \"t_upper\": -2.2564,\n        \"p_lower\": 0.036785,\n        \"p_upper\": 0.076338,\n        \"tost_p\": 0.076338,\n        \"equivalent_at_alpha05\": false,\n        \"ci90_pp\": [\n          -1.609,\n          2.463\n        ],\n        \"ci90_inside_rope\": false,\n        \"ci95_pp\": [\n          -2.574,\n          3.427\n        ],\n        \"diffs\": [\n          -0.05,\n          1.8,\n          -0.47\n        ]\n      },\n      \"bayesian_rope\": {\n        \"method\": \"Bayesian ROPE (Kruschke 2013, Jeffreys prior)\",\n        \"n\": 3,\n        \"df\": 2,\n        \"mean_diff_pp\": 0.4267,\n        \"sd_pp\": 1.2077,\n        \"se_pp\": 0.6973,\n        \"rope\": [\n          -2.0,\n          2.0\n        ],\n        \"p_rope\": 0.8869,\n        \"p_above_rope\": 0.0763,\n        \"p_below_rope\": 0.0368,\n        \"hdi_95_lo\": -2.57,\n        \"hdi_95_hi\": 3.43,\n        \"hdi_inside_rope\": false,\n        \"decision_continuous\": \"Inconclusive\",\n        \"decision_hdi\": \"Undecided (95% HDI overlaps ROPE boundary)\"\n      }\n    },\n    \"CLS-TRAJ\": {\n      \"tost\": {\n        \"method\": \"seed-level paired TOST (D169)\",\n        \"n_seeds\": 3,\n        \"df\": 2,\n        \"mean_diff_pp\": 1.07,\n        \"sd_pp\": 1.422,\n        \"se_pp\": 0.821,\n        \"margin_pp\": 2.0,\n        \"t_lower\": 3.7394,\n        \"t_upper\": -1.1328,\n        \"p_lower\": 0.032329,\n        \"p_upper\": 0.187417,\n        \"tost_p\": 0.187417,\n        \"equivalent_at_alpha05\": false,\n        \"ci90_pp\": [\n          -1.327,\n          3.467\n        ],\n        \"ci90_inside_rope\": false,\n        \"ci95_pp\": [\n          -2.462,\n          4.602\n        ],\n        \"diffs\": [\n          -0.52,\n          2.22,\n          1.51\n        ]\n      },\n      \"bayesian_rope\": {\n        \"method\": \"Bayesian ROPE (Kruschke 2013, Jeffreys prior)\",\n        \"n\": 3,\n        \"df\": 2,\n        \"mean_diff_pp\": 1.07,\n        \"sd_pp\": 1.422,\n        \"se_pp\": 0.821,\n        \"rope\": [\n          -2.0,\n          2.0\n        ],\n        \"p_rope\": 0.7803,\n        \"p_above_rope\": 0.1874,\n        \"p_below_rope\": 0.0323,\n        \"hdi_95_lo\": -2.46,\n        \"hdi_95_hi\": 4.6,\n        \"hdi_inside_rope\": false,\n        \"decision_continuous\": \"Inconclusive\",\n        \"decision_hdi\": \"Undecided (95% HDI overlaps ROPE boundary)\"\n      }\n    }\n  },\n  \"paper_comparison\": {\n    \"CLS-TRAJ\": {\n      \"seed_level_tost_p\": 0.187417,\n      \"paper_tost_p\": 0.043,\n      \"match\": false,\n      \"seed_level_p_rope\": 0.7803,\n      \"paper_p_rope\": 0.956,\n      \"match_rope\": false,\n      \"diagnosis\": \"Paper values (p=0.043, P(ROPE)=0.956) are from per-test clustered bootstrap, NOT seed-level. D169 requires seed-level values.\"\n    }\n  }\n}\n",
      "numLines": 141,
      "startLine": 1,
      "totalLines": 141
    }
  }
}
```

</details>

---


### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Read · `toolu_01HaA1NuQi72FQaakeoC2aCz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/routing_analysis_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "faf2099b-4947-46ca-84b4-e17cd4d87bd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELbkVamxKPob8FgizuBXi9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 92727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3867
      },
      "output_tokens": 69,
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

_source line 78 · 2026-05-23T19:19:14.516Z_

<details><summary>↩ Tool result · `toolu_01HaA1NuQi72FQaakeoC2aCz`</summary>

```text
1	# Routing Heuristic Analysis: CLS vs CWM Formulation Routing
2	
3	**Date**: 2026-05-22
4	**Type**: Post-hoc analysis (no model training)
5	**Data**: 1,890 function-level per-test predictions, 7 prediction files (3 CLS, 4 CWM), 12 CLS-CWM pairs analyzed
6	
7	---
8	
9	## Data Inventory
10	
11	| Model | Seed | File | Acc (%) | n |
12	|-------|------|------|---------|---|
13	| CLS 4B | 0 | predictions_cls_seed0.jsonl | 87.78 | 1890 |
14	| CLS 8B | 42 | cls8b_seed42_predictions.json | 90.48 | 1890 |
15	| CLS 8B | 123 | cls8b_seed123_predictions.json | 89.37 | 1890 |
16	| CWM 4B | 42 | eval_results_bf16_predictions.json | 87.51 | 1890 |
17	| CWM 4B | 123 | predictions_cwm_seed123.jsonl | 87.30 | 1890 |
18	| CWM 4B | 789 | predictions_cwm_seed789.jsonl | 86.67 | 1890 |
19	| CWM 4B | 123v2 | eval_cwm_seed123_with_preds_predictions.json | 87.20 | 1890 |
20	
21	**Missing data**: No CWM 8B per-instance predictions. No TRAJ per-test predictions (TRAJ operates at variant level). No confidence/logit scores for any model. Repo-level CWM predictions not available (CWM ~58% accuracy at repo-level makes routing moot).
22	
23	---
24	
25	## Oracle Complementarity (Reference)
26	
27	| Pair Type | Best Single (%) | Oracle (%) | Gap (pp) | Error Complementarity (%) |
28	|-----------|----------------|------------|----------|--------------------------|
29	| 4B CLS vs 4B CWM | 87.78 | 89.84–90.16 | +2.0–2.4 | 31–34% |
30	| 8B CLS vs 4B CWM | 89.37–90.48 | 93.07–94.44 | +3.7–4.0 | 53–59% |
31	
32	Error complementarity is higher for 8B-vs-4B pairs because the 8B CLS makes different errors than 4B CWM, creating more room for oracle ensemble.
33	
34	---
35	
36	## Heuristic 1: Complexity-Based Routing (Test Count T)
37	
38	**Design**: T=1 → use CWM; T≥2 → use CLS (motivated by SWE-bench F2P distribution where 68.7% of instances have T=1).
39	
40	**Result: Inapplicable to function-level dataset.**
41	
42	All 114 problems have T≥6 tests (mean ≈16.6 tests/problem), so every instance falls in the T≥6 bin. The routing degenerates to always-CLS:
43	
44	| Pair | Routed Acc (%) | Best Single (%) | Gain (pp) |
45	|------|---------------|-----------------|-----------|
46	| All 12 pairs | = Best Single | 87.78–90.48 | **+0.00** |
47	
48	**Bootstrap 95% CI**: [0.00, 0.00] for all 8B pairs; [-0.74, 0.00] for 4B pairs (slightly negative when CWM is picked for nonexistent T=1 bin).
49	
50	**Interpretation**: This heuristic is designed for heterogeneous test-count distributions (SWE-bench: T=1 to T≥50). The function-level benchmark has uniform high-T problems, so there is no routing signal. The heuristic remains theoretically valid for deployment on SWE-bench-like tasks but cannot be empirically validated with function-level data alone.
51	
52	---
53	
54	## Heuristic 2: Level-Based Routing
55	
56	**Design**: Function-level → use CWM (equivalent accuracy, richer diagnostic output); Repo-level → use CLS (dramatically higher accuracy + throughput).
57	
58	| Level | CLS Acc (%) | CWM Acc (%) | Gap (pp) | Recommendation |
59	|-------|------------|------------|----------|----------------|
60	| Function (4B mean) | 88.43 | 87.19 | +1.24 | Either (TOST equivalent) |
61	| Function (8B mean) | 89.39 | 86.96 | +2.43 | CLS |
62	| Repo (8B mean) | 84.56 | 58.57 | +25.99 | CLS |
63	
64	**Result**: Trivially correct for repo-level (CWM is unusable). At function-level, the CLS-CWM gap is 1.24pp (4B) to 2.43pp (8B) — small but potentially meaningful with 8B.
65	
66	**This heuristic captures 0pp of oracle complementarity** — it's a static assignment, not instance-level routing. Its value is practitioner guidance (which formulation to deploy), not accuracy improvement.
67	
68	---
69	
70	## Heuristic 3: Mutation-Type Routing
71	
72	**Design**: For each mutation type, route to whichever formulation has higher accuracy on that type (oracle on mutation type, not on individual instances).
73	
74	### Per-Mutation Accuracy (representative pair: CLS 4B s0 vs CWM 4B s42)
75	
76	| Mutation Type | n | CLS (%) | CWM (%) | Winner | Gap (pp) |
77	|--------------|---|---------|---------|--------|----------|
78	| return_value | 402 | 97.51 | 97.26 | CLS | 0.25 |
79	| variable_swap | 85 | 94.12 | 92.94 | CLS | 1.18 |
80	| boundary_removal | 36 | 91.67 | 91.67 | tie | 0.00 |
81	| original | 398 | 86.43 | 84.17 | CLS | 2.26 |
82	| operator_swap | 298 | 86.24 | 87.92 | CWM | 1.68 |
83	| off_by_one | 671 | 82.41 | 82.56 | CWM | 0.15 |
84	
85	### Routing Accuracy Across All Pairs
86	
87	| Pair | Best Single (%) | Routed (%) | Gain (pp) | Oracle (%) | Oracle Gap (pp) |
88	|------|----------------|------------|-----------|------------|----------------|
89	| CLS 4B s0 vs CWM 4B s42 | 87.78 | 88.10 | **+0.32** | 90.16 | 2.06 |
90	| CLS 4B s0 vs CWM 4B s123 | 87.78 | 88.15 | **+0.37** | 89.84 | 1.69 |
91	| CLS 4B s0 vs CWM 4B s789 | 87.78 | 88.04 | **+0.26** | 89.79 | 1.75 |
92	| CLS 4B s0 vs CWM 4B s123v2 | 87.78 | 88.04 | **+0.26** | 89.84 | 1.80 |
93	| CLS 8B s42 vs CWM 4B s42 | 90.48 | 90.58 | +0.10 | 94.44 | 3.86 |
94	| CLS 8B s42 vs CWM 4B s123 | 90.48 | 90.48 | +0.00 | 94.39 | 3.92 |
95	| CLS 8B s42 vs CWM 4B s789 | 90.48 | 90.48 | +0.00 | 94.23 | 3.76 |
96	| CLS 8B s42 vs CWM 4B s123v2 | 90.48 | 90.48 | +0.00 | 94.34 | 3.86 |
97	| CLS 8B s123 vs CWM 4B s42 | 89.37 | 89.68 | +0.31 | 93.33 | 3.65 |
98	| CLS 8B s123 vs CWM 4B s123 | 89.37 | 89.58 | +0.21 | 93.17 | 3.59 |
99	| CLS 8B s123 vs CWM 4B s789 | 89.37 | 89.37 | +0.00 | 93.07 | 3.70 |
100	| CLS 8B s123 vs CWM 4B s123v2 | 89.37 | 89.52 | +0.15 | 93.23 | 3.70 |
101	
102	**Mean routing gain**: +0.16pp (range: 0.00 to +0.37pp)
103	**Mean oracle gap remaining**: 2.88pp
104	
105	### Bootstrap 95% CI (Routing Gain over Best Single)
106	
107	| Pair | Mean (pp) | 95% CI | % Positive |
108	|------|-----------|--------|------------|
109	| CLS 4B s0 vs CWM 4B s42 | +0.22 | [-0.48, +0.79] | 73.9% |
110	| CLS 4B s0 vs CWM 4B s123 | +0.33 | [-0.32, +0.90] | 82.8% |
111	| CLS 4B s0 vs CWM 4B s789 | +0.26 | [-0.16, +0.69] | 86.3% |
112	| CLS 8B s42 vs CWM 4B s42 | +0.10 | [-0.48, +0.69] | 60.6% |
113	| CLS 8B s123 vs CWM 4B s42 | +0.14 | [-0.48, +0.79] | 64.1% |
114	
115	**No pair achieves statistical significance** (all CIs include 0).
116	
117	### Why Mutation-Type Routing Fails for 8B CLS
118	
119	When CLS is 8B (90.48%), it dominates CWM (4B, 87.51%) on **every** mutation type. There is no mutation type where CWM beats 8B CLS, so routing reverts to always-CLS (gain = 0.00pp). The mutation-type routing only helps when formulations are close in overall accuracy (4B vs 4B: +0.26–0.37pp).
120	
121	---
122	
123	## Heuristic 3b: Confidence-Based Routing
124	
125	**Status: Not possible.** No logit or confidence scores were saved during inference. The prediction files contain only hard labels (pass/fail). To enable this heuristic, future inference runs would need to output token-level logits or calibrated confidence scores.
126	
127	---
128	
129	## Key Conclusions
130	
131	1. **Oracle complementarity is real but not capturable by simple heuristics.** The oracle CLS∪CWM ensemble gains 2.0–4.0pp over best single formulation, but error complementarity (31–59%) is distributed across diverse, instance-specific patterns — not systematic features like test count or mutation type.
132	
133	2. **Complexity-based routing (H1) is inapplicable** to the function-level benchmark (uniform T≥6). It remains valid in principle for SWE-bench-like distributions where T varies from 1 to 50+.
134	
135	3. **Level-based routing (H2) is trivially correct** for repo-level (CWM unusable at 58.57%). At function-level, it reduces to a deployment choice, not an accuracy-improving strategy.
136	
137	4. **Mutation-type routing (H3) captures ≤0.37pp** of the 2–4pp oracle gap. The gain is not statistically significant (all bootstrap CIs include 0). When the stronger model (8B CLS) dominates across all mutation types, the gain drops to 0.
138	
139	5. **Implication for paper**: The oracle gap represents genuinely complementary error patterns between formulations — errors that are diverse and instance-specific rather than predictable from observable features. A learned routing model (e.g., trained on validation-set error patterns) might capture more of this gap, but this would add model complexity inconsistent with the paper's focus on formulation comparison. The oracle results should be reported as an **upper bound** on ensemble potential, with explicit acknowledgment that simple heuristics do not close the gap.
140	
141	---
142	
143	## Data for Paper
144	
145	If reporting these results, the key numbers are:
146	
147	> Simple routing heuristics (test-count threshold, task-level assignment, mutation-type oracle) capture at most 0.4 pp of the 2–4 pp oracle gap between CLS and CWM, and this gain is not statistically significant (bootstrap 95% CI includes zero for all 12 formulation pairs tested). The complementarity between formulations is driven by instance-specific error patterns rather than systematic features observable before inference.
148	
149	---
150	
151	## Files
152	
153	- **Analysis script**: `routing_analysis.py` (on server at `/home/sonny/exec-sim-repair-verifier/routing_analysis.py`)
154	- **Raw results JSON**: `routing_analysis_results.json` (on server)
155	- **This report**: `artifacts/routing_analysis_report.md`
156	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "a2fb8b38-6686-4c80-b11d-0aa5db6e9da2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/routing_analysis_report.md",
      "content": "# Routing Heuristic Analysis: CLS vs CWM Formulation Routing\n\n**Date**: 2026-05-22\n**Type**: Post-hoc analysis (no model training)\n**Data**: 1,890 function-level per-test predictions, 7 prediction files (3 CLS, 4 CWM), 12 CLS-CWM pairs analyzed\n\n---\n\n## Data Inventory\n\n| Model | Seed | File | Acc (%) | n |\n|-------|------|------|---------|---|\n| CLS 4B | 0 | predictions_cls_seed0.jsonl | 87.78 | 1890 |\n| CLS 8B | 42 | cls8b_seed42_predictions.json | 90.48 | 1890 |\n| CLS 8B | 123 | cls8b_seed123_predictions.json | 89.37 | 1890 |\n| CWM 4B | 42 | eval_results_bf16_predictions.json | 87.51 | 1890 |\n| CWM 4B | 123 | predictions_cwm_seed123.jsonl | 87.30 | 1890 |\n| CWM 4B | 789 | predictions_cwm_seed789.jsonl | 86.67 | 1890 |\n| CWM 4B | 123v2 | eval_cwm_seed123_with_preds_predictions.json | 87.20 | 1890 |\n\n**Missing data**: No CWM 8B per-instance predictions. No TRAJ per-test predictions (TRAJ operates at variant level). No confidence/logit scores for any model. Repo-level CWM predictions not available (CWM ~58% accuracy at repo-level makes routing moot).\n\n---\n\n## Oracle Complementarity (Reference)\n\n| Pair Type | Best Single (%) | Oracle (%) | Gap (pp) | Error Complementarity (%) |\n|-----------|----------------|------------|----------|--------------------------|\n| 4B CLS vs 4B CWM | 87.78 | 89.84–90.16 | +2.0–2.4 | 31–34% |\n| 8B CLS vs 4B CWM | 89.37–90.48 | 93.07–94.44 | +3.7–4.0 | 53–59% |\n\nError complementarity is higher for 8B-vs-4B pairs because the 8B CLS makes different errors than 4B CWM, creating more room for oracle ensemble.\n\n---\n\n## Heuristic 1: Complexity-Based Routing (Test Count T)\n\n**Design**: T=1 → use CWM; T≥2 → use CLS (motivated by SWE-bench F2P distribution where 68.7% of instances have T=1).\n\n**Result: Inapplicable to function-level dataset.**\n\nAll 114 problems have T≥6 tests (mean ≈16.6 tests/problem), so every instance falls in the T≥6 bin. The routing degenerates to always-CLS:\n\n| Pair | Routed Acc (%) | Best Single (%) | Gain (pp) |\n|------|---------------|-----------------|-----------|\n| All 12 pairs | = Best Single | 87.78–90.48 | **+0.00** |\n\n**Bootstrap 95% CI**: [0.00, 0.00] for all 8B pairs; [-0.74, 0.00] for 4B pairs (slightly negative when CWM is picked for nonexistent T=1 bin).\n\n**Interpretation**: This heuristic is designed for heterogeneous test-count distributions (SWE-bench: T=1 to T≥50). The function-level benchmark has uniform high-T problems, so there is no routing signal. The heuristic remains theoretically valid for deployment on SWE-bench-like tasks but cannot be empirically validated with function-level data alone.\n\n---\n\n## Heuristic 2: Level-Based Routing\n\n**Design**: Function-level → use CWM (equivalent accuracy, richer diagnostic output); Repo-level → use CLS (dramatically higher accuracy + throughput).\n\n| Level | CLS Acc (%) | CWM Acc (%) | Gap (pp) | Recommendation |\n|-------|------------|------------|----------|----------------|\n| Function (4B mean) | 88.43 | 87.19 | +1.24 | Either (TOST equivalent) |\n| Function (8B mean) | 89.39 | 86.96 | +2.43 | CLS |\n| Repo (8B mean) | 84.56 | 58.57 | +25.99 | CLS |\n\n**Result**: Trivially correct for repo-level (CWM is unusable). At function-level, the CLS-CWM gap is 1.24pp (4B) to 2.43pp (8B) — small but potentially meaningful with 8B.\n\n**This heuristic captures 0pp of oracle complementarity** — it's a static assignment, not instance-level routing. Its value is practitioner guidance (which formulation to deploy), not accuracy improvement.\n\n---\n\n## Heuristic 3: Mutation-Type Routing\n\n**Design**: For each mutation type, route to whichever formulation has higher accuracy on that type (oracle on mutation type, not on individual instances).\n\n### Per-Mutation Accuracy (representative pair: CLS 4B s0 vs CWM 4B s42)\n\n| Mutation Type | n | CLS (%) | CWM (%) | Winner | Gap (pp) |\n|--------------|---|---------|---------|--------|----------|\n| return_value | 402 | 97.51 | 97.26 | CLS | 0.25 |\n| variable_swap | 85 | 94.12 | 92.94 | CLS | 1.18 |\n| boundary_removal | 36 | 91.67 | 91.67 | tie | 0.00 |\n| original | 398 | 86.43 | 84.17 | CLS | 2.26 |\n| operator_swap | 298 | 86.24 | 87.92 | CWM | 1.68 |\n| off_by_one | 671 | 82.41 | 82.56 | CWM | 0.15 |\n\n### Routing Accuracy Across All Pairs\n\n| Pair | Best Single (%) | Routed (%) | Gain (pp) | Oracle (%) | Oracle Gap (pp) |\n|------|----------------|------------|-----------|------------|----------------|\n| CLS 4B s0 vs CWM 4B s42 | 87.78 | 88.10 | **+0.32** | 90.16 | 2.06 |\n| CLS 4B s0 vs CWM 4B s123 | 87.78 | 88.15 | **+0.37** | 89.84 | 1.69 |\n| CLS 4B s0 vs CWM 4B s789 | 87.78 | 88.04 | **+0.26** | 89.79 | 1.75 |\n| CLS 4B s0 vs CWM 4B s123v2 | 87.78 | 88.04 | **+0.26** | 89.84 | 1.80 |\n| CLS 8B s42 vs CWM 4B s42 | 90.48 | 90.58 | +0.10 | 94.44 | 3.86 |\n| CLS 8B s42 vs CWM 4B s123 | 90.48 | 90.48 | +0.00 | 94.39 | 3.92 |\n| CLS 8B s42 vs CWM 4B s789 | 90.48 | 90.48 | +0.00 | 94.23 | 3.76 |\n| CLS 8B s42 vs CWM 4B s123v2 | 90.48 | 90.48 | +0.00 | 94.34 | 3.86 |\n| CLS 8B s123 vs CWM 4B s42 | 89.37 | 89.68 | +0.31 | 93.33 | 3.65 |\n| CLS 8B s123 vs CWM 4B s123 | 89.37 | 89.58 | +0.21 | 93.17 | 3.59 |\n| CLS 8B s123 vs CWM 4B s789 | 89.37 | 89.37 | +0.00 | 93.07 | 3.70 |\n| CLS 8B s123 vs CWM 4B s123v2 | 89.37 | 89.52 | +0.15 | 93.23 | 3.70 |\n\n**Mean routing gain**: +0.16pp (range: 0.00 to +0.37pp)\n**Mean oracle gap remaining**: 2.88pp\n\n### Bootstrap 95% CI (Routing Gain over Best Single)\n\n| Pair | Mean (pp) | 95% CI | % Positive |\n|------|-----------|--------|------------|\n| CLS 4B s0 vs CWM 4B s42 | +0.22 | [-0.48, +0.79] | 73.9% |\n| CLS 4B s0 vs CWM 4B s123 | +0.33 | [-0.32, +0.90] | 82.8% |\n| CLS 4B s0 vs CWM 4B s789 | +0.26 | [-0.16, +0.69] | 86.3% |\n| CLS 8B s42 vs CWM 4B s42 | +0.10 | [-0.48, +0.69] | 60.6% |\n| CLS 8B s123 vs CWM 4B s42 | +0.14 | [-0.48, +0.79] | 64.1% |\n\n**No pair achieves statistical significance** (all CIs include 0).\n\n### Why Mutation-Type Routing Fails for 8B CLS\n\nWhen CLS is 8B (90.48%), it dominates CWM (4B, 87.51%) on **every** mutation type. There is no mutation type where CWM beats 8B CLS, so routing reverts to always-CLS (gain = 0.00pp). The mutation-type routing only helps when formulations are close in overall accuracy (4B vs 4B: +0.26–0.37pp).\n\n---\n\n## Heuristic 3b: Confidence-Based Routing\n\n**Status: Not possible.** No logit or confidence scores were saved during inference. The prediction files contain only hard labels (pass/fail). To enable this heuristic, future inference runs would need to output token-level logits or calibrated confidence scores.\n\n---\n\n## Key Conclusions\n\n1. **Oracle complementarity is real but not capturable by simple heuristics.** The oracle CLS∪CWM ensemble gains 2.0–4.0pp over best single formulation, but error complementarity (31–59%) is distributed across diverse, instance-specific patterns — not systematic features like test count or mutation type.\n\n2. **Complexity-based routing (H1) is inapplicable** to the function-level benchmark (uniform T≥6). It remains valid in principle for SWE-bench-like distributions where T varies from 1 to 50+.\n\n3. **Level-based routing (H2) is trivially correct** for repo-level (CWM unusable at 58.57%). At function-level, it reduces to a deployment choice, not an accuracy-improving strategy.\n\n4. **Mutation-type routing (H3) captures ≤0.37pp** of the 2–4pp oracle gap. The gain is not statistically significant (all bootstrap CIs include 0). When the stronger model (8B CLS) dominates across all mutation types, the gain drops to 0.\n\n5. **Implication for paper**: The oracle gap represents genuinely complementary error patterns between formulations — errors that are diverse and instance-specific rather than predictable from observable features. A learned routing model (e.g., trained on validation-set error patterns) might capture more of this gap, but this would add model complexity inconsistent with the paper's focus on formulation comparison. The oracle results should be reported as an **upper bound** on ensemble potential, with explicit acknowledgment that simple heuristics do not close the gap.\n\n---\n\n## Data for Paper\n\nIf reporting these results, the key numbers are:\n\n> Simple routing heuristics (test-count threshold, task-level assignment, mutation-type oracle) capture at most 0.4 pp of the 2–4 pp oracle gap between CLS and CWM, and this gain is not statistically significant (bootstrap 95% CI includes zero for all 12 formulation pairs tested). The complementarity between formulations is driven by instance-specific error patterns rather than systematic features observable before inference.\n\n---\n\n## Files\n\n- **Analysis script**: `routing_analysis.py` (on server at `/home/sonny/exec-sim-repair-verifier/routing_analysis.py`)\n- **Raw results JSON**: `routing_analysis_results.json` (on server)\n- **This report**: `artifacts/routing_analysis_report.md`\n",
      "numLines": 156,
      "startLine": 1,
      "totalLines": 156
    }
  }
}
```

</details>

---


### Tool call

_source line 79_

<details open><summary>🔧 Tool call — Read · `toolu_01RVQFLxsN1vKiHi7dvgQNeo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/compute_oracle_3seed.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "de547395-08d6-439e-8878-12d67bd5af2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELbkVamxKPob8FgizuBXi9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 92727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3867
      },
      "output_tokens": 69,
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

_source line 80 · 2026-05-23T19:19:14.677Z_

<details><summary>↩ Tool result · `toolu_01RVQFLxsN1vKiHi7dvgQNeo`</summary>

```text
1	#!/usr/bin/env python3
2	"""Compute cross-seed oracle accuracy (CLS ∪ CWM) at repo level.
3	
4	Target: 94.27 ± 2.59% (3 seeds: 42, 123, 456)
5	
6	Oracle = for each problem, if either CLS or CWM (from any seed) predicts
7	correctly, count as correct. Computed per-seed (each seed gets its own oracle),
8	then mean ± std across seeds.
9	
10	Requires prediction JSONL files on the evaluation server. This script documents
11	the computation logic; to run, provide paths to the prediction files.
12	
13	Usage:
14	  python3 compute_oracle_3seed.py \\
15	    --cls-preds cls_s42.jsonl cls_s123.jsonl cls_s456.jsonl \\
16	    --cwm-preds cwm_s42.jsonl cwm_s123.jsonl cwm_s456.jsonl
17	
18	Without prediction files, the script shows the documented per-seed results.
19	"""
20	
21	import argparse
22	import json
23	import math
24	import sys
25	from collections import defaultdict
26	
27	
28	# --- Documented results from worker analysis (2026-05-22) ---
29	# Source: worker_analysis_multi-seed-oracle_20260522T124959_result.json
30	DOCUMENTED_RESULTS = {
31	    "s42": {
32	        "cls_acc": 85.34,
33	        "cwm_acc": 65.17,
34	        "oracle_acc": 91.28,
35	        "note": "Same training seed for both CLS and CWM → higher error correlation",
36	    },
37	    "s123": {
38	        "cls_acc": 85.34,
39	        "cwm_acc": 67.33,
40	        "oracle_acc": 95.86,
41	        "note": "CWM uses different seed → lower error correlation with CLS",
42	    },
43	    "s456": {
44	        "cls_acc": 85.34,
45	        "cwm_acc": 66.93,
46	        "oracle_acc": 95.68,
47	        "note": "CWM uses different seed → lower error correlation with CLS",
48	    },
49	}
50	
51	
52	def load_predictions(path):
53	    """Load prediction file (JSON list or JSONL)."""
54	    with open(path) as f:
55	        raw = json.load(f)
56	    if isinstance(raw, dict) and "predictions" in raw:
57	        records = raw["predictions"]
58	    elif isinstance(raw, list):
59	        records = raw
60	    else:
61	        with open(path) as f:
62	            records = [json.loads(line) for line in f if line.strip()]
63	    out = {}
64	    for r in records:
65	        idx = r.get("index", r.get("idx"))
66	        label = int(r.get("label", r.get("true_label")))
67	        pred = int(r.get("pred", r.get("prediction", r.get("predicted_label"))))
68	        pid = r["problem_id"]
69	        out[idx] = {"label": label, "pred": pred, "problem_id": pid, "correct": pred == label}
70	    return out
71	
72	
73	def compute_oracle(cls_preds, cwm_preds):
74	    """Compute oracle (CLS ∪ CWM) accuracy at problem level."""
75	    common = sorted(set(cls_preds) & set(cwm_preds))
76	    if not common:
77	        raise ValueError("No common indices between CLS and CWM predictions")
78	
79	    # Group by problem
80	    problems = defaultdict(lambda: {"cls_correct": [], "cwm_correct": [], "labels": []})
81	    for idx in common:
82	        c, w = cls_preds[idx], cwm_preds[idx]
83	        assert c["label"] == w["label"], f"Label mismatch at {idx}"
84	        pid = c["problem_id"]
85	        problems[pid]["cls_correct"].append(c["correct"])
86	        problems[pid]["cwm_correct"].append(w["correct"])
87	
88	    n_problems = len(problems)
89	    cls_correct_problems = 0
90	    cwm_correct_problems = 0
91	    oracle_correct_problems = 0
92	
93	    for pid, data in problems.items():
94	        cls_all_correct = all(data["cls_correct"])
95	        cwm_all_correct = all(data["cwm_correct"])
96	        cls_correct_problems += cls_all_correct
97	        cwm_correct_problems += cwm_all_correct
98	        oracle_correct_problems += (cls_all_correct or cwm_all_correct)
99	
100	    return {
101	        "n_tests": len(common),
102	        "n_problems": n_problems,
103	        "cls_acc": round(cls_correct_problems / n_problems * 100, 2),
104	        "cwm_acc": round(cwm_correct_problems / n_problems * 100, 2),
105	        "oracle_acc": round(oracle_correct_problems / n_problems * 100, 2),
106	        "oracle_gain_over_cls": round(
107	            (oracle_correct_problems - cls_correct_problems) / n_problems * 100, 2
108	        ),
109	    }
110	
111	
112	def main():
113	    ap = argparse.ArgumentParser(description=__doc__,
114	                                 formatter_class=argparse.RawDescriptionHelpFormatter)
115	    ap.add_argument("--cls-preds", nargs="+", help="CLS prediction files (one per seed)")
116	    ap.add_argument("--cwm-preds", nargs="+", help="CWM prediction files (one per seed)")
117	    args = ap.parse_args()
118	
119	    if args.cls_preds and args.cwm_preds:
120	        if len(args.cls_preds) != len(args.cwm_preds):
121	            ap.error("Must provide same number of CLS and CWM prediction files")
122	
123	        print("Computing oracle from prediction files...")
124	        print("=" * 60)
125	
126	        oracle_accs = []
127	        for i, (cls_path, cwm_path) in enumerate(zip(args.cls_preds, args.cwm_preds)):
128	            print(f"\nSeed {i+1}: {cls_path} vs {cwm_path}")
129	            cls_preds = load_predictions(cls_path)
130	            cwm_preds = load_predictions(cwm_path)
131	            result = compute_oracle(cls_preds, cwm_preds)
132	            oracle_accs.append(result["oracle_acc"])
133	            print(f"  CLS: {result['cls_acc']}%  CWM: {result['cwm_acc']}%")
134	            print(f"  Oracle: {result['oracle_acc']}%  (+{result['oracle_gain_over_cls']}pp)")
135	
136	        mean_oracle = sum(oracle_accs) / len(oracle_accs)
137	        if len(oracle_accs) > 1:
138	            std_oracle = math.sqrt(
139	                sum((x - mean_oracle) ** 2 for x in oracle_accs) / (len(oracle_accs) - 1)
140	            )
141	        else:
142	            std_oracle = 0.0
143	
144	        print(f"\n{'='*60}")
145	        print(f"Cross-seed oracle: {mean_oracle:.2f} ± {std_oracle:.2f}%")
146	        print(f"Per-seed: {oracle_accs}")
147	    else:
148	        # Show documented results
149	        print("Cross-seed Oracle (CLS ∪ CWM) — Repo Level")
150	        print("Source: worker_analysis_multi-seed-oracle_20260522T124959_result.json")
151	        print("=" * 60)
152	
153	        oracle_accs = []
154	        for seed, data in DOCUMENTED_RESULTS.items():
155	            print(f"\n{seed}:")
156	            print(f"  CLS: {data['cls_acc']}%  CWM: {data['cwm_acc']}%")
157	            print(f"  Oracle: {data['oracle_acc']}%")
158	            print(f"  ({data['note']})")
159	            oracle_accs.append(data["oracle_acc"])
160	
161	        mean_oracle = sum(oracle_accs) / len(oracle_accs)
162	        std_oracle = math.sqrt(
163	            sum((x - mean_oracle) ** 2 for x in oracle_accs) / (len(oracle_accs) - 1)
164	        )
165	
166	        print(f"\n{'='*60}")
167	        print(f"Cross-seed oracle: {mean_oracle:.2f} ± {std_oracle:.2f}%")
168	        print(f"Per-seed: {oracle_accs}")
169	
170	        target_mean, target_std = 94.27, 2.59
171	        mean_match = abs(mean_oracle - target_mean) < 0.05
172	        std_match = abs(std_oracle - target_std) < 0.05
173	        print(f"\nTarget: {target_mean} ± {target_std}%")
174	        print(f"Mean: {'MATCH' if mean_match else 'MISMATCH'}")
175	        print(f"Std:  {'MATCH' if std_match else 'MISMATCH'}")
176	
177	        if not args.cls_preds:
178	            print("\nTo compute from raw predictions, run:")
179	            print("  python3 compute_oracle_3seed.py \\")
180	            print("    --cls-preds cls_s42.jsonl cls_s123.jsonl cls_s456.jsonl \\")
181	            print("    --cwm-preds cwm_s42.jsonl cwm_s123.jsonl cwm_s456.jsonl")
182	
183	
184	if __name__ == "__main__":
185	    main()
186	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "5534e220-886e-45fa-a324-835b51a7fc19",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/compute_oracle_3seed.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Compute cross-seed oracle accuracy (CLS ∪ CWM) at repo level.\n\nTarget: 94.27 ± 2.59% (3 seeds: 42, 123, 456)\n\nOracle = for each problem, if either CLS or CWM (from any seed) predicts\ncorrectly, count as correct. Computed per-seed (each seed gets its own oracle),\nthen mean ± std across seeds.\n\nRequires prediction JSONL files on the evaluation server. This script documents\nthe computation logic; to run, provide paths to the prediction files.\n\nUsage:\n  python3 compute_oracle_3seed.py \\\\\n    --cls-preds cls_s42.jsonl cls_s123.jsonl cls_s456.jsonl \\\\\n    --cwm-preds cwm_s42.jsonl cwm_s123.jsonl cwm_s456.jsonl\n\nWithout prediction files, the script shows the documented per-seed results.\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport sys\nfrom collections import defaultdict\n\n\n# --- Documented results from worker analysis (2026-05-22) ---\n# Source: worker_analysis_multi-seed-oracle_20260522T124959_result.json\nDOCUMENTED_RESULTS = {\n    \"s42\": {\n        \"cls_acc\": 85.34,\n        \"cwm_acc\": 65.17,\n        \"oracle_acc\": 91.28,\n        \"note\": \"Same training seed for both CLS and CWM → higher error correlation\",\n    },\n    \"s123\": {\n        \"cls_acc\": 85.34,\n        \"cwm_acc\": 67.33,\n        \"oracle_acc\": 95.86,\n        \"note\": \"CWM uses different seed → lower error correlation with CLS\",\n    },\n    \"s456\": {\n        \"cls_acc\": 85.34,\n        \"cwm_acc\": 66.93,\n        \"oracle_acc\": 95.68,\n        \"note\": \"CWM uses different seed → lower error correlation with CLS\",\n    },\n}\n\n\ndef load_predictions(path):\n    \"\"\"Load prediction file (JSON list or JSONL).\"\"\"\n    with open(path) as f:\n        raw = json.load(f)\n    if isinstance(raw, dict) and \"predictions\" in raw:\n        records = raw[\"predictions\"]\n    elif isinstance(raw, list):\n        records = raw\n    else:\n        with open(path) as f:\n            records = [json.loads(line) for line in f if line.strip()]\n    out = {}\n    for r in records:\n        idx = r.get(\"index\", r.get(\"idx\"))\n        label = int(r.get(\"label\", r.get(\"true_label\")))\n        pred = int(r.get(\"pred\", r.get(\"prediction\", r.get(\"predicted_label\"))))\n        pid = r[\"problem_id\"]\n        out[idx] = {\"label\": label, \"pred\": pred, \"problem_id\": pid, \"correct\": pred == label}\n    return out\n\n\ndef compute_oracle(cls_preds, cwm_preds):\n    \"\"\"Compute oracle (CLS ∪ CWM) accuracy at problem level.\"\"\"\n    common = sorted(set(cls_preds) & set(cwm_preds))\n    if not common:\n        raise ValueError(\"No common indices between CLS and CWM predictions\")\n\n    # Group by problem\n    problems = defaultdict(lambda: {\"cls_correct\": [], \"cwm_correct\": [], \"labels\": []})\n    for idx in common:\n        c, w = cls_preds[idx], cwm_preds[idx]\n        assert c[\"label\"] == w[\"label\"], f\"Label mismatch at {idx}\"\n        pid = c[\"problem_id\"]\n        problems[pid][\"cls_correct\"].append(c[\"correct\"])\n        problems[pid][\"cwm_correct\"].append(w[\"correct\"])\n\n    n_problems = len(problems)\n    cls_correct_problems = 0\n    cwm_correct_problems = 0\n    oracle_correct_problems = 0\n\n    for pid, data in problems.items():\n        cls_all_correct = all(data[\"cls_correct\"])\n        cwm_all_correct = all(data[\"cwm_correct\"])\n        cls_correct_problems += cls_all_correct\n        cwm_correct_problems += cwm_all_correct\n        oracle_correct_problems += (cls_all_correct or cwm_all_correct)\n\n    return {\n        \"n_tests\": len(common),\n        \"n_problems\": n_problems,\n        \"cls_acc\": round(cls_correct_problems / n_problems * 100, 2),\n        \"cwm_acc\": round(cwm_correct_problems / n_problems * 100, 2),\n        \"oracle_acc\": round(oracle_correct_problems / n_problems * 100, 2),\n        \"oracle_gain_over_cls\": round(\n            (oracle_correct_problems - cls_correct_problems) / n_problems * 100, 2\n        ),\n    }\n\n\ndef main():\n    ap = argparse.ArgumentParser(description=__doc__,\n                                 formatter_class=argparse.RawDescriptionHelpFormatter)\n    ap.add_argument(\"--cls-preds\", nargs=\"+\", help=\"CLS prediction files (one per seed)\")\n    ap.add_argument(\"--cwm-preds\", nargs=\"+\", help=\"CWM prediction files (one per seed)\")\n    args = ap.parse_args()\n\n    if args.cls_preds and args.cwm_preds:\n        if len(args.cls_preds) != len(args.cwm_preds):\n            ap.error(\"Must provide same number of CLS and CWM prediction files\")\n\n        print(\"Computing oracle from prediction files...\")\n        print(\"=\" * 60)\n\n        oracle_accs = []\n        for i, (cls_path, cwm_path) in enumerate(zip(args.cls_preds, args.cwm_preds)):\n            print(f\"\\nSeed {i+1}: {cls_path} vs {cwm_path}\")\n            cls_preds = load_predictions(cls_path)\n            cwm_preds = load_predictions(cwm_path)\n            result = compute_oracle(cls_preds, cwm_preds)\n            oracle_accs.append(result[\"oracle_acc\"])\n            print(f\"  CLS: {result['cls_acc']}%  CWM: {result['cwm_acc']}%\")\n            print(f\"  Oracle: {result['oracle_acc']}%  (+{result['oracle_gain_over_cls']}pp)\")\n\n        mean_oracle = sum(oracle_accs) / len(oracle_accs)\n        if len(oracle_accs) > 1:\n            std_oracle = math.sqrt(\n                sum((x - mean_oracle) ** 2 for x in oracle_accs) / (len(oracle_accs) - 1)\n            )\n        else:\n            std_oracle = 0.0\n\n        print(f\"\\n{'='*60}\")\n        print(f\"Cross-seed oracle: {mean_oracle:.2f} ± {std_oracle:.2f}%\")\n        print(f\"Per-seed: {oracle_accs}\")\n    else:\n        # Show documented results\n        print(\"Cross-seed Oracle (CLS ∪ CWM) — Repo Level\")\n        print(\"Source: worker_analysis_multi-seed-oracle_20260522T124959_result.json\")\n        print(\"=\" * 60)\n\n        oracle_accs = []\n        for seed, data in DOCUMENTED_RESULTS.items():\n            print(f\"\\n{seed}:\")\n            print(f\"  CLS: {data['cls_acc']}%  CWM: {data['cwm_acc']}%\")\n            print(f\"  Oracle: {data['oracle_acc']}%\")\n            print(f\"  ({data['note']})\")\n            oracle_accs.append(data[\"oracle_acc\"])\n\n        mean_oracle = sum(oracle_accs) / len(oracle_accs)\n        std_oracle = math.sqrt(\n            sum((x - mean_oracle) ** 2 for x in oracle_accs) / (len(oracle_accs) - 1)\n        )\n\n        print(f\"\\n{'='*60}\")\n        print(f\"Cross-seed oracle: {mean_oracle:.2f} ± {std_oracle:.2f}%\")\n        print(f\"Per-seed: {oracle_accs}\")\n\n        target_mean, target_std = 94.27, 2.59\n        mean_match = abs(mean_oracle - target_mean) < 0.05\n        std_match = abs(std_oracle - target_std) < 0.05\n        print(f\"\\nTarget: {target_mean} ± {target_std}%\")\n        print(f\"Mean: {'MATCH' if mean_match else 'MISMATCH'}\")\n        print(f\"Std:  {'MATCH' if std_match else 'MISMATCH'}\")\n\n        if not args.cls_preds:\n            print(\"\\nTo compute from raw predictions, run:\")\n            print(\"  python3 compute_oracle_3seed.py \\\\\")\n            print(\"    --cls-preds cls_s42.jsonl cls_s123.jsonl cls_s456.jsonl \\\\\")\n            print(\"    --cwm-preds cwm_s42.jsonl cwm_s123.jsonl cwm_s456.jsonl\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 186,
      "startLine": 1,
      "totalLines": 186
    }
  }
}
```

</details>

---


### Assistant

_source line 81_

<details><summary>Logged reasoning block</summary>

```text
Now let me analyze what I have. I need to also find the function-level oracle values (90.63%) and repo-level oracle (95.83%). The compute_oracle_3seed.py is for repo-level cross-seed oracle (94.27±2.59%), but the paper mentions 95.83% for repo oracle. Let me check...

Actually, the paper says:
- Function-level oracle: 90.63% (+2.80pp) - single seed
- Repo-level oracle: 95.83% (+14.58pp) - n=48 variant-level


The 95.83% repo-level oracle is a variant-level measurement at n=48, while compute_oracle_3seed.py gives the per-test oracle across seeds. Looking at the seed-level stats, CLS_14B with seed 42 shows 89.21 in bf16 evaluation (or 89.47 in NF4), and the registry confirms the bf16 value of 89.21 is what's used in the scaling table.

Similarly, CWM_14B seed 42 shows 89.26 in bf16 versus 89.30 in NF4, matching what the registry entry shows. Now I'm systematically auditing the function-level results, starting with the CLS 4B seeds across the five variants. I have seed 42, 123, 789, and 0 from various sources, but I'm still looking for the CLS 4B seed 456 value to complete the set. I'm checking the full multi-seed-core entry to see if there are additional seeds beyond 42 and 123. Looking at the CLS 4B candidates I can identify from the registry—seeds 42, 123, 789, and 0—I'm still missing seed 456 to match the paper's five-seed average of 88.43. I notice the 8B model has a cls8b-seed456 entry with 88.31 accuracy, but I haven't found the corresponding 4B version yet. I'm looking for the missing 5th seed value for CLS 4B (seed 456) to calculate the proper mean, and I'm noticing the per-test-precision-recall experiment shows an accuracy of 87.51 with detailed metrics on precision, recall, and mutation testing results that might be relevant to the CWM model. Now I'm calculating the mean and standard deviation for the 14B models across their three seeds. For CLS 14B, the three accuracy values average to 89.93 with a standard deviation of 0.80. For CWM 14B, I'm working through the same calculation with its seed values. Finishing the mean calculation for TRAJ 14B and computing its standard deviation, then calculating the gap between CLS and TRAJ scores to verify the 1.07 percentage point difference for the 14B model.

Now I'm noticing a discrepancy in the abstract claim—the 3.11pp gap comes from the 2-seed scaling table comparison, not from Table 1's 5-seed results which show a smaller 2.13pp gap. And the 18–26pp range is pulled from Table 2.

For the oracle variant accuracy, the 14.58pp improvement is the difference between the repo-level oracle at 95.83% and the best CLS variant at 81.25%. The routing heuristic shows gains under 0.4pp, with a mean of +0.16pp and max of +0.37pp.

Now I'm verifying the statistical significance through Holm-Bonferroni correction. The repo-level CLS vs CWM comparison shows raw p=0.003 and adjusted p=0.015, while the function-level TOST comparisons yield adjusted p-values of 0.028 and 0.075 respectively. These results match exactly with Table I in the paper.

Moving to the Bayesian ROPE analysis, the probability of practical equivalence is 0.975 for CLS-CWM at the per-test level, 0.542 for CLS-TRAJ per-test (which the paper notes as inconclusive), and 0.970 at the variant level for CLS-TRAJ. All of these align with what's reported in the paper text.

Now checking the 14B seed-level statistics...

the TOST p-values match at 0.076 for CLS-CWM and 0.187 for CLS-TRAJ, and the ROPE probabilities are also confirmed at 0.887 and 0.780 respectively.

Moving to Table 2 verification at the repository level, I'm checking the registry data for the Qwen3-4B models across different evaluation checkpoints...

For Qwen3-8B CLS, I'm finding multiple seed results but the paper reports a mean with standard deviation over 3 seeds, so I need to locate all three seed runs to match the reported 84.83 ± 0.67. Finishing the standard deviation calculation for the first model, then moving on to verify the Qwen3-8B CWM results across different checkpoint and sequence length configurations. Finishing the standard deviation calculation for CWM 8B, which comes out to about 1.15. Now looking at the TRAJ variant across the same three seeds, where the scores range from 70.83 to 77.08, giving a mean of 73.61.

But wait—the paper reports 72.91 ± 3.61 for this configuration, which doesn't match my calculation. Let me verify whether the paper might be using different seeds or checkpoint versions than what I'm seeing in the registry. Looking at the table more carefully, I see the CLS Var column lists individual seed results (72.92 / 81.25†) rather than an average, while the TRAJ Var column shows 72.91 ± 3.61 as a mean and standard deviation—but I'm puzzled because those individual values don't seem to average to 72.91. I'm verifying the standard deviation calculation for DeepSeek TRAJ matches the paper's reported 3.61, which it does. For Qwen3-8B TRAJ, the paper reports 72.91 ± 3.61, but my data shows a mean of 73.61 with different values, so I'm checking whether different random seeds were used in the original experiments. I'm verifying the standard deviation calculation matches, which confirms the results use the epoch 3 checkpoint for s42 at 70.83. Now I'm noticing the checkpoint descriptions mention different trade-offs—epoch 2 has better class balance while epoch 3is biased toward predicting unresolved—and the table context indicates these are means and standard deviations computed across 3 seeds. So the paper's checkpoint selection is actually consistent—for s42 with NaN validation loss, it uses the final epoch 3 checkpoint (70.83), and combined with s123=77.08 and s456=70.83, that gives the reported mean of 72.91 ± 3.61 for Qwen3-8B TRAJ.

Now I need to figure out which checkpoint the CLS variant used for s42 to get that 72.92 accuracy.

For DeepSeek, I'm verifying the mean and standard deviation across the two seed runs: the first seed gives 82.61 and the second gives 86.15, which averages to 84.38, and I'm calculating the standard deviation to confirm it matches the reported 2.50.

I notice the footnote mentions one seed was excluded due to preprocessing issues causing NaN values, so only the s42 and s456 runs are being used. Now looking at DeepSeek CWM, I have three seed results to work with: 61.49, 57.31, and 56.

11. Computing the mean gives me 58.30, which matches the paper's reported value. For the standard deviation, I'm calculating the variance across these three seeds and getting approximately 2.82, which confirms the reported uncertainty.

Now I'm noticing that the evaluation sequences differ between models—DeepSeek uses seq4096 while Qwen3 uses seq8192, as noted in the appendix. Looking at the baseline numbers, the 0-shot repo-level accuracy for Qwen3 is 49.90% and for DeepSeek is 48.54%, both matching the reported values. The majority baseline sits at 72.96%. Moving into the function-level results from Table 1, I'm verifying the CLS and CWM metrics for the 4B models.

Checking the CWM 4B numbers more carefully—the paper reports 87.19 ± 0.37, and when I compute the mean from the individual runs (87.51, 87.20, 86.98, 86.67), I get 87.186 which rounds to 87.19, and the standard deviation of 0.375 rounds to 0.37, so everything checks out.

Now I need to track down all five seed runs for CLS 4B from the registry.  I've found four of them, but s456 is missing, so I'll work backwards from the mean of 88.43 to calculate what that value should be. Once I have all five, I can verify the standard deviation of 0.78 checks out with the deviations and squared differences.

The math confirms that if s456 equals 87.86, the variance and standard deviation align perfectly with what's reported. However, I can't locate s456 directly in the registry output—it might be buried in the truncated multi-seed-core data. Let me search for the full experiment details to see if I can find it there, and then I'll move on to checking the 8B model seeds.

For the 8B results, I'm noticing some inconsistencies between different experiment entries. The cls8b-seed123 experiment shows 89.40 overall accuracy, but cls8b-eval-seed123 reports 89.37—a small discrepancy that suggests these are separate evaluation runs of the same model. The paper's Table 1 appears to use the 89.40 value for the 8B seed123 result, so I need to verify what the table actually lists for individual seeds versus the scaling summary.

Looking at the table structure more carefully, Table 1 focuses on function-level results with Qwen3 at 4B and DeepSeek-Coder at 6.7B, while the 8B fine-tuned results only appear in the scaling table. The prompting baselines in Table 1 include 8B and 14B models, but those are zero-shot, not fine-tuned versions.

Now I'm calculating the mean and standard deviation for DeepSeek's function-level performance across the different metrics—CLS shows 86.85 with a standard deviation around 0.11, and CWM is averaging around 86.83 from the two runs. Now I'm verifying the TRAJ 6.7B results by calculating the mean and standard deviation from the two model variants, which checks out to 84.16 ± 1.30. I'm also cross-referencing the prompting baselines from Table 1, confirming the 0-shot accuracy scores for the 8B and 14B Qwen3 models.

For the DeepSeek 6.7B baseline, I'm noticing a small discrepancy between the reported 63.00% in the paper and the registry value of 0.6302, which calculates to 63.02%—likely due to rounding from the actual count of 1191 correct samples out of 1890 total. I'm testing different numerator values to see which produces the 63.00% figure—1191 gives 63.02%, which is close but off by 0.02 percentage points, and I'm wondering if there's a precision or rounding difference in how the paper computed this metric.

Now I'm cross-referencing the table entries with my results: the 8B baseline 0-shot matches at 60.53%, and the LLM-as-judge 8B zero-shot is 64.40%, but I'm not finding a corresponding DeepSeek LLM-as-judge entry in my data. I'm cross-referencing the baseline results across different model sizes and configurations—the 8B Qwen3 function-level accuracy should be 60.53, not 68.73, which suggests the qwen3-0shot-func-baseline entry is actually for the 4B model. With 152 total experiments in the registry, I need to systematically work through them to find the remaining entries like the 6.7B DeepSeek 3-shot result and verify the majority voting baseline at 51.75%.

Now moving to the scaling table verification, I'm checking the 4B results across different methods—CLS, CWM, and TRAJ—against their multi-seed averages, and I'm noticing the registry entries for s42 and s123 seeds need to be cross-referenced with the specific experiment configurations to ensure I'm matching the right results. I'm verifying the CWM results by cross-referencing the scaling table with the registry entries. CWM 4B s42 matches at 87.51, CWM 4B s123 at 87.20, and CWM 8B s42 at 87.67, so the metrics are consistent across both sources.

Now checking the CLS 8B results—s42 is 90.48 and s123 is 89.40 in the scaling table, though I notice there's a slight discrepancy where cls8b-eval-seed123 shows 89.37 instead of 89.40, but these appear to be separate experimental runs and the paper uses the 89.40 value.

For TRAJ 4B, I'm seeing s42 at 85.66 and s123 at 85.47, both matching their respective experiment registries. TRAJ 8B shows s42 at 87.60 and s123 at 87.79, also confirmed. Now I'm computing the scaling deltas—CLS 4B to 8B should be 89.94 minus 88.68, which gives 1.26, but the paper reports 1.27, so there's a small rounding difference to account for.

I'm verifying the other model transitions: CWM 4B to 8B shows essentially no change at -0.03, TRAJ 4B to 8B jumps by 2.13, and CLS 8B to 14B is nearly flat at -0.01. CWM 8B to 14B is coming up next.

For CWM 8B to 14B, the mean of the 4B and 8B values is 87.33, and subtracting that from the 14B value of 89.50 gives a gain of 2.17. TRAJ shows a more modest improvement of 1.16 going from 8B to 14B.

Now I'm checking the zero-shot gains mentioned in the paper—looking at how much improvement comes from the instruction-tuning approaches compared to the base zero-shot model, which sits at 49.90 for the 8B variant. The gains check out—34.93 rounds to 35 and 35.84 rounds to 36, so the "35-36pp" range is accurate. The 18.35pp and 25.59pp improvements at 8B and 4B respectively both match the reported numbers. The >50% unparseable rate holds up too, with 4B at 53.7% and 8B at 73.8%. Now I need to track down where that 477-token average for CWM output length comes from in the repo-level data.

For the z-score of -23.7, that's from the mixed-effects regression on the formulation×complexity interaction, which I'd need to verify in the actual regression script. The routing gap claim of <0.4pp is solid—the maximum gain is 0.37pp. On the dataset sizes, CLS has 15,290 training instances according to Table 1, TRAJ has 8,052, and the 2.24× multiplier for unique code variants checks out from the task description.

Now I'm puzzling through the phrasing about variant coverage—TRAJ has fewer total instances than CLS but somehow covers 2.24× more unique code variants, which seems counterintuitive at first. Let me reconsider what this ratio actually means in context. So TRAJ's 8,052 instances actually represent 2.24× more unique code variants than CLS's 15,290 instances because CLS repeats the same variants across multiple tests, whereas TRAJ uses variant-level labels. This explains why TRAJ has fewer total training instances but greater diversity in the actual code patterns being learned. Looking at the variant-level calculation more carefully: with 15,290 per-test instances and roughly 1.9 tests per variant on average, that gives around 8,047 unique variants in the training set, which aligns with the 8,052 figure. Now checking the oracle numbers from the appendix—the function-level oracle achieves 90.63% accuracy (1713 out of 1890 correct), which is 2.80 percentage points above the best single model at 87.83%.

But I'm noticing a discrepancy: the routing analysis report shows different oracle numbers using CLS at seed 0 (87.78%) versus the appendix which uses seed 42 (87.83%), so the oracle combinations they're comparing aren't quite the same. CLS.

Hmm, actually the paper's 90.63% is:
"oracle combination achieves 90.63% accuracy (1713/1890 correct, 177 both-wrong; +2.80pp over the best single formulation, CLS 87.83%; single-seed estimate, seed 42)"

So it's CLS s42 (87.83) oracle with CWM s42 (87.51), giving 90.63%. That's +2.80pp over 87.83. ✓

Repo oracle: 95.83% variant accuracy (+14.58pp)
Variant accuracy maximum in Table 2 for CLS is 81.25 (Qwen3-8B s123 or DeepSeek s42).
95.83 - 81.25 = 14.58 ✓

The 95.83% comes from the routing analysis experiment where the repo-level variant oracle for the best CLS-CWM pair achieves that score. That's 46 out of 48 variants correct, representing the variant-level oracle rather than per-test performance. For Figure 2, I'm checking the CLS-CWM performance gaps across model sizes: 1.32pp at 4B, 2.62pp at 8B, and 0.43pp at 14B based on the 3-seed average. I'm verifying the gap measurements across model sizes and checking the bootstrap statistics mentioned in section 4.3. The 4B and 8B gaps match the paper's reported values, and now I need to locate the bootstrap results to confirm the p-value and confidence interval for the 8B comparison.

Looking at the downsampling results in Appendix O, the accuracy of 80.74% checks out against the paper. For the format collapse metrics, I'm tracing the unparseable rate increase from 53.7% at 4B to 73.8% at 8B by cross-referencing the registry entries for both model checkpoints. So the 73.8% unparseable rate for the 8B model appears when evaluating at seq8192 length, not seq4096 where it's around 63.7%. The paper's comparison of 53.7% to 73.8% is tracking how performance degrades as you scale from 4B to 8B and extend the sequence length.

Now I'm double-checking the deepseek baseline accuracy—if it's 63.02% across 1890 samples with 20 unparseable entries, that should give roughly 1191 correct predictions, which aligns with the reported figure.

Looking at the CWM 8B mean next: averaging the two values gives 87.325, which rounds to 87.33% as shown in the paper's scaling table.

The text mentions CWM remains flat at −0.03pp, and checking: 87.33 − 87.36 = −0.03, which checks out. CLS 8B mean calculates to 89.94, matching the table exactly. TRAJ 8B mean is 87.695, which rounds to 87.70 as reported.

Now I need to verify the CLS 4B seed456 value—the scaling table only includes seed42 and seed123 for 4B models, but Table 1 uses five seeds for CLS 4B.

Checking the five seeds: I have seed42 at 87.83, seed123 at 89.52, seed789 at 89.00, and seed0 at 87.94. The missing seed456 would need to be around 87.86 to produce the reported mean of 88.43 ± 0.78, which seems plausible even though I can't locate it directly in the registry excerpt—it may be in the multi-seed-core experiment data that wasn't fully shown.

Moving to the 8B CLS seeds: seed42 gives 90.48 and seed123 gives 89.40, and I'm checking the remaining three seeds to verify the full set.

I'm realizing the confusion here—Table 1 reports 4B results for Qwen3, not 8B, while the 8B CLS numbers only appear in the scaling table with just seed42 and seed123 available.

Looking at the discrepancy between the two seed123 evaluations, cls8b-seed123 shows 89.40 while cls8b-eval-seed123 shows 89.37—likely the same model tested under slightly different conditions, with the 0.03 difference accounting for just a handful of samples out of nearly 1900. Looking at the rounding more carefully—both models might actually have the same underlying accuracy of 89.37% (1689 out of 1890 correct), but they're being reported at different decimal precisions, with the scaling table rounding to 89.40.

If I recalculate using 89.37 instead, the 8B CLS mean drops from 89.94 to 89.93, which shifts the CLS-CWM gap to 2.60 and the 8B→14B delta to 0.00—both within 0.02 percentage points of the reported values. The discrepancy is small enough that I'll note it but not dig deeper into this.

Now I'm ready to compile the audit report. Let me quickly verify the figure 2 plot script and the scaling bootstrap results, then check the p-value and confidence interval for the 8B CLS-CWM gap clustering bootstrap. I also want to confirm the abstract mentions "TOST, 5 seeds" and that both CLS and CWM use 5 seeds at the function level.

Looking at the abstract claim about statistical equivalence across both model families—the TOST with 5 seeds applies to Qwen3, while DeepSeek only has 2 seeds, so the "across both families" phrasing is slightly stronger than what the data fully supports. The Qwen3 TOST p=0.028 (Holm-corrected) is the main evidence, with DeepSeek showing a consistent but underpowered 0.02pp CLS-CWM gap.

Now I need to check the DeepSeek LLM-as-judge score and the 3-shot in-context learning result at the function level to see how those compare.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72deb850-edfb-4093-94b6-8107ea44f4ef",
  "uuid": "117d0f24-750e-4564-9669-1e63ad477e49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Y8HJeL36YQGc9NRwwffFv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10776,
      "cache_read_input_tokens": 96594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10776
      },
      "output_tokens": 9,
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
