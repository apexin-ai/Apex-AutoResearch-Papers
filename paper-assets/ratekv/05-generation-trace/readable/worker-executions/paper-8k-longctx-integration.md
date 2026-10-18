# paper 8k longctx integration

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_paper_8k_longctx_integration_20260516T031348.log`
- **Structured JSON:** [`af15093818e46fcfb102.json`](../../sessions/af/af15093818e46fcfb102.json)

## Before a recorded user message

30 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
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
  "uuid": "2257e905-4ff6-40f5-b03f-6c14b3823355",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/memory/"
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
    "resetsAt": 1778904600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7289ea62-056c-42bf-b727-ae6f992aa77a",
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd"
}
```

---

### Assistant

_source line 4_

Let me read the current state of experiments.tex to find §4.3 and understand the context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "6a8aad75-9a78-4873-a19e-ec485604794c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpcS4ySvejfBqFbvrDCbZx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12695,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12695
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — Read · `toolu_0158U7HvNoaCfr1sKEpVodpQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "9f3cc003-e18c-4040-a1c8-3cd3775bc20c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpcS4ySvejfBqFbvrDCbZx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12695,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12695
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-16T03:14:02.367Z_

<details><summary>↩ Tool result · `toolu_0158U7HvNoaCfr1sKEpVodpQ`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate eight models spanning six architecture families and diverse attention configurations:
9	\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\times$ 4 KV heads = 112),
10	\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\times$ 8 = 384),
11	\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\times$ 4 = 192),
12	\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\times$ 8 = 256),
13	\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\times$ 8 = 256, sliding window attention),
14	\textbf{Gemma-2-9B} (GQA 2:1, 42 $\times$ 8 = 336, \texttt{head\_dim}=256, attention logit softcapping),
15	\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\times$ 10 = 400),
16	and \textbf{Pythia-1.4B} (MHA 1:1, 24 $\times$ 16 = 384).
17	This selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.
18	
19	\paragraph{Evaluation.}
20	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
21	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
22	
23	\paragraph{Profiling.}
24	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
25	All results use high-resolution profiling (64 sequences $\times$ 2048 tokens from WikiText-2 train); Appendix~\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\times$ 512 tok).
26	
27	\paragraph{Compression and constraint.}
28	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
29	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).
30	
31	\paragraph{Baselines.}
32	We compare against:
33	(1)~uniform 4-bit quantization;
34	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
35	(3)~unconstrained MCKP allocation;
36	(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
37	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
38	
39	\subsection{Main Results}
40	\label{sec:main_results}
41	
42	\begin{table}[t]
43	\centering
44	\small
45	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\times$ bf16), severe on Pythia ($1.9\times$), moderate on Gemma-2 ($1.5\times$), mild on remaining incl.\ Qwen-14B (${\sim}1.1\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \textbf{bold}. $^*$BOS-corrected.}
46	\label{tab:main_results}
47	\begin{tabular}{lccccc}
48	\toprule
49	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
50	\cmidrule(lr){4-5}
51	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
52	\midrule
53	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{10.91} \\
54	Qwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\
55	Yi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\
56	Llama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \textbf{8.45} \\
57	Mistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\
58	Gemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\
59	Phi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\
60	Pythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	On Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\% reduction over uniform 4-bit (15.45).
66	Without the constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.
67	Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 with 90.2\% three-way allocation agreement, confirming profiling stability.
68	
69	On Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47, $\Delta < 0.02$ PPL).
70	Hires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.
71	
72	On Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.
73	On Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.
74	
75	On Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\ uniform 6.17 ($+$0.4\%).
76	Despite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\times$ bf16) from 31.5\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.
77	
78	On Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\times$ bf16). %exp_id=phi3_medium_constrained_mckp
79	
80	Unconstrained failure severity tracks heterogeneity shape: \emph{catastrophic} on Qwen-7B ($3.3\times$ bf16, 60\% heads at 2-bit), \emph{severe} on Pythia ($1.9\times$), \emph{moderate} on Gemma-2 ($1.47\times$), and \emph{mild} on remaining models (${\sim}1.07$--$1.12\times$) including Qwen-14B ($1.12\times$, 20\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\ flat).
81	See Appendix~\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\ref{sec:budget_sweep} (budget sweep) for additional detail.
82	
83	MCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\%; Table~\ref{tab:heuristic} in Appendix~\ref{sec:heuristic_appendix}).
84	
85	\paragraph{Comparison with KIVI.}
86	KIVI~\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.
87	At 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.
88	Within the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).
89	The two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.
90	However, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.
91	Per-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.
92	
93	\subsection{Cross-Architecture Compounding}
94	\label{sec:compounding_cross}
95	
96	\begin{figure}[t]
97	\centering
98	\includegraphics[width=\columnwidth]{figures/fig_compounding_curves.pdf}
99	\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\times$). All three stay near-baseline for $k{\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\approx}96$ due to its 112 KV heads (maximum ${\sim}96$ eligible for 2-bit assignment).}
100	\label{fig:compounding_cross}
101	\end{figure}
102	
103	Figure~\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.
104	At small $k$ (${\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\leq}2.5\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.
105	
106	Beyond $k{=}8$, divergence is stark.
107	Llama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.
108	Qwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\times$) and $98.75$ at $k{=}256$ ($10.1\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.
109	Mistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.
110	
111	These curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\times$ baseline) is ${\sim}32$ for Qwen, ${\sim}64$ for Llama, and ${\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.
112	
113	\subsection{Downstream Evaluation}
114	\label{sec:downstream}
115	
116	\begin{table}[t]
117	\centering
118	\small
119	\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\times$ compression. Qwen values are mean over 3 calibration seeds ($\pm$1$\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}
120	\label{tab:downstream}
121	\begin{tabular}{lccccc}
122	\toprule
123	Model & ARC-C & HS & PIQA & WG & Avg \\
124	\midrule
125	Qwen2.5-7B        & $+$0.0{\scriptsize$\pm$0.4} & $+$4.1{\scriptsize$\pm$0.2} & $+$2.0{\scriptsize$\pm$0.2} & $+$1.6{\scriptsize$\pm$1.2} & $+$1.9 \\
126	Yi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\
127	Llama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\
128	Mistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\
129	Gemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	On Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\pm$1$\sigma$ in Table~\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).
135	The four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.
136	ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.
137	Cross-dataset (Appendix~\ref{sec:cross_dataset}, ${>}96\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\ref{sec:long_context}, Qwen uniform $11.15\times$ bf16 at 8K vs.\ MCKP $1.23\times$) analyses confirm allocation robustness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "e42fe0d3-72ee-4aa7-84f8-9ecba4d1b082",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate eight models spanning six architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\n\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPhi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite the highest concentration tested (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nOn Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\\times$ bf16). %exp_id=phi3_medium_constrained_mckp\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nWithin the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\nHowever, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.\nPer-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.\n\n\\subsection{Cross-Architecture Compounding}\n\\label{sec:compounding_cross}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_compounding_curves.pdf}\n\\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\\times$). All three stay near-baseline for $k{\\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\\approx}96$ due to its 112 KV heads (maximum ${\\sim}96$ eligible for 2-bit assignment).}\n\\label{fig:compounding_cross}\n\\end{figure}\n\nFigure~\\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.\nAt small $k$ (${\\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\\leq}2.5\\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.\n\nBeyond $k{=}8$, divergence is stark.\nLlama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.\nQwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\\times$) and $98.75$ at $k{=}256$ ($10.1\\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.\nMistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.\n\nThese curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\\times$ baseline) is ${\\sim}32$ for Qwen, ${\\sim}64$ for Llama, and ${\\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen values are mean over 3 calibration seeds ($\\pm$1$\\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$0.0{\\scriptsize$\\pm$0.4} & $+$4.1{\\scriptsize$\\pm$0.2} & $+$2.0{\\scriptsize$\\pm$0.2} & $+$1.6{\\scriptsize$\\pm$1.2} & $+$1.9 \\\\\nYi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\\\\nLlama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\\\\nMistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\\\\nGemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
      "numLines": 137,
      "startLine": 1,
      "totalLines": 137
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_017EVpSwQY5vg6UvES2sFiQp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "offset": 137
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "8023c806-57f2-40eb-98ff-6dcebc38e1df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K52Bp9m8HoCaJswQUXkFzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4909,
      "cache_read_input_tokens": 24536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4909
      },
      "output_tokens": 38,
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

_source line 8 · 2026-05-16T03:14:08.238Z_

<details><summary>↩ Tool result · `toolu_017EVpSwQY5vg6UvES2sFiQp`</summary>

```text
137	Cross-dataset (Appendix~\ref{sec:cross_dataset}, ${>}96\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\ref{sec:long_context}, Qwen uniform $11.15\times$ bf16 at 8K vs.\ MCKP $1.23\times$) analyses confirm allocation robustness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "068d9a8e-15f9-4f0a-8ed8-1bbb86107528",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
      "content": "Cross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
      "numLines": 1,
      "startLine": 137,
      "totalLines": 137
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
The file ends at line 137. There's no separate §4.3 section for long-context evaluation in the main experiments.tex. The long-context reference is currently just a parenthetical mention in the last line (137) that points to Appendix~\ref{sec:long_context}.

Let me check if there's a separate appendix file or if the long-context section is elsewhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "f6e24c70-3aae-42cc-a99d-bbf03956b28e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUT3vKZWHi7QESQTpJ7Ea9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 210,
      "cache_read_input_tokens": 29445,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 210
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

_source line 10_

The long-context data is currently only a parenthetical reference on line 137, pointing to an appendix. Let me find where §4.3 / the long-context appendix lives.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "eee17bd5-eb66-419a-b487-18d080a58732",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUT3vKZWHi7QESQTpJ7Ea9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 210,
      "cache_read_input_tokens": 29445,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 210
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

_source line 11_

<details open><summary>🔧 Tool call — Grep · `toolu_015RLrYPhFdLcB5oNYRtX7cZ`</summary>

```json
{
  "pattern": "long.context|sec:long_context",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
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
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "ac936f86-0b0d-4a76-8e9f-32ba8c442075",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUT3vKZWHi7QESQTpJ7Ea9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 210,
      "cache_read_input_tokens": 29445,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 210
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

_source line 12 · 2026-05-16T03:14:14.544Z_

<details><summary>↩ Tool result · `toolu_015RLrYPhFdLcB5oNYRtX7cZ`</summary>

```text
docs/paper/experiments.tex:137:Cross-dataset (Appendix~\ref{sec:cross_dataset}, ${>}96\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\ref{sec:long_context}, Qwen uniform $11.15\times$ bf16 at 8K vs.\ MCKP $1.23\times$) analyses confirm allocation robustness.
docs/paper/main.bbl:94:  long-context inference in {LLMs}}.
docs/paper/main.bbl:168:  long context inference}.
docs/paper/main.bbl:231:  mixed-precision {KV} cache quantization for long-context reasoning}.
docs/paper/appendix.tex:183:\label{sec:long_context}
docs/paper/appendix.tex:189:\label{tab:long_context}
docs/paper/appendix.tex:205:Table~\ref{tab:long_context} extends the evaluation to 8K context length using 2K-calibrated profiles.
docs/paper/main.aux:1389:\newlabel{sec:long_context}{{L}{14}{Long-Context Generalization}{appendix.L}{}}
docs/paper/main.aux:1391:\newlabel{tab:long_context}{{8}{14}{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times $ 2048 tok). Yi-1.5 excluded (max position 4096)}{table.caption.40}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "2046c5f5-e0e2-4845-87da-435ebcb0b7c7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments.tex:137:Cross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.\ndocs/paper/main.bbl:94:  long-context inference in {LLMs}}.\ndocs/paper/main.bbl:168:  long context inference}.\ndocs/paper/main.bbl:231:  mixed-precision {KV} cache quantization for long-context reasoning}.\ndocs/paper/appendix.tex:183:\\label{sec:long_context}\ndocs/paper/appendix.tex:189:\\label{tab:long_context}\ndocs/paper/appendix.tex:205:Table~\\ref{tab:long_context} extends the evaluation to 8K context length using 2K-calibrated profiles.\ndocs/paper/main.aux:1389:\\newlabel{sec:long_context}{{L}{14}{Long-Context Generalization}{appendix.L}{}}\ndocs/paper/main.aux:1391:\\newlabel{tab:long_context}{{8}{14}{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\\times $ 2048 tok). Yi-1.5 excluded (max position 4096)}{table.caption.40}{}}",
    "numLines": 9
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01FcUcWn76eWF5Kmj9pWhYn9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
  "offset": 178,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "804538b8-b9ce-4da4-b4fa-6eedda4bf149",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CR8dvPSum3VxUaxQHCLeJs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 29655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 667
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

_source line 14 · 2026-05-16T03:14:17.491Z_

<details><summary>↩ Tool result · `toolu_01FcUcWn76eWF5Kmj9pWhYn9`</summary>

```text
178	Production inference engines such as vLLM and TensorRT-LLM employ fused attention kernels that batch dequantization with the matrix multiply, amortizing the per-head dispatch cost that dominates the gap between uniform and MCKP in our simulation.
179	The 8.5\% overhead reported here should therefore be treated as an upper bound on the mixed-precision penalty; real-world deployment with fused kernels would likely narrow or eliminate this gap.
180	As noted in the Limitations section, we report no real-kernel latency benchmarks: the numbers above quantify simulation overhead, not production inference speedup.
181	
182	\section{Long-Context Generalization}
183	\label{sec:long_context}
184	
185	\begin{table}[ht]
186	\centering
187	\small
188	\caption{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times$ 2048 tok). Yi-1.5 excluded (max position 4096).}
189	\label{tab:long_context}
190	\begin{tabular}{llcc}
191	\toprule
192	Model & Method & 2K PPL & 8K PPL \\
193	\midrule
194	 & BF16 baseline & 9.81 & 6.97 \\
195	Qwen2.5-7B & MCKP ($k{=}8$) & 10.89 & 8.59 \\
196	 & Uniform 4-bit & 15.45 & 77.75 \\
197	\midrule
198	 & BF16 baseline & 8.09 & 5.60 \\
199	Llama-3.1-8B & MCKP ($k{=}2$) & 8.50 & 6.05 \\
200	 & Uniform 4-bit & 8.47 & 6.04 \\
201	\bottomrule
202	\end{tabular}
203	\end{table}
204	
205	Table~\ref{tab:long_context} extends the evaluation to 8K context length using 2K-calibrated profiles.
206	On Qwen (spread), uniform 4-bit degrades from $1.57\times$ bf16 at 2K to $11.15\times$ at 8K---quantization errors accumulate catastrophically over longer sequences.
207	Constrained MCKP remains robust ($1.11\times$ at 2K, $1.23\times$ at 8K), recovering 97.7\% of the quantization loss at 8K vs.\ 80.8\% at 2K.
208	On Llama (spike), both methods remain indistinguishable at 8K (6.05 vs.\ 6.04), consistent with the 2K result.
209	The diagnostic (concentration $+$ $t_1/t_5$) thus generalizes across context lengths, and the spread-pattern MCKP advantage amplifies with longer sequences.
210	Profiles calibrated at 2K transfer effectively to 8K without re-profiling, providing positive evidence of calibration generalization.
211	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "0b694959-19ab-4dab-b3b0-e75a6ad72c26",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
      "content": "Production inference engines such as vLLM and TensorRT-LLM employ fused attention kernels that batch dequantization with the matrix multiply, amortizing the per-head dispatch cost that dominates the gap between uniform and MCKP in our simulation.\nThe 8.5\\% overhead reported here should therefore be treated as an upper bound on the mixed-precision penalty; real-world deployment with fused kernels would likely narrow or eliminate this gap.\nAs noted in the Limitations section, we report no real-kernel latency benchmarks: the numbers above quantify simulation overhead, not production inference speedup.\n\n\\section{Long-Context Generalization}\n\\label{sec:long_context}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\\times$ 2048 tok). Yi-1.5 excluded (max position 4096).}\n\\label{tab:long_context}\n\\begin{tabular}{llcc}\n\\toprule\nModel & Method & 2K PPL & 8K PPL \\\\\n\\midrule\n & BF16 baseline & 9.81 & 6.97 \\\\\nQwen2.5-7B & MCKP ($k{=}8$) & 10.89 & 8.59 \\\\\n & Uniform 4-bit & 15.45 & 77.75 \\\\\n\\midrule\n & BF16 baseline & 8.09 & 5.60 \\\\\nLlama-3.1-8B & MCKP ($k{=}2$) & 8.50 & 6.05 \\\\\n & Uniform 4-bit & 8.47 & 6.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:long_context} extends the evaluation to 8K context length using 2K-calibrated profiles.\nOn Qwen (spread), uniform 4-bit degrades from $1.57\\times$ bf16 at 2K to $11.15\\times$ at 8K---quantization errors accumulate catastrophically over longer sequences.\nConstrained MCKP remains robust ($1.11\\times$ at 2K, $1.23\\times$ at 8K), recovering 97.7\\% of the quantization loss at 8K vs.\\ 80.8\\% at 2K.\nOn Llama (spike), both methods remain indistinguishable at 8K (6.05 vs.\\ 6.04), consistent with the 2K result.\nThe diagnostic (concentration $+$ $t_1/t_5$) thus generalizes across context lengths, and the spread-pattern MCKP advantage amplifies with longer sequences.\nProfiles calibrated at 2K transfer effectively to 8K without re-profiling, providing positive evidence of calibration generalization.\n",
      "numLines": 34,
      "startLine": 178,
      "totalLines": 211
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
The appendix already has Llama 8K data in the table and discussion (lines 198-200, 208). The data matches what the user provided:

- BF16: 5.60 (user says 5.5958)
- MCKP (k=2): 6.05 (user says 6.0537)  
- Uniform 4-bit: 6.04 (user says 6.0364)

So the appendix already has both Qwen and Llama 8K data with discussion. The task is about §4.3 in the main experiments section. But looking at the experiments.tex, there is no §4.3 dedicated to long-context - it's only a parenthetical on line 137.


Let me recount the subsections to clarify what §4.3 actually covers: it's "Cross-Architecture Compounding" starting at line 93, not long-context evaluation. The long-context content the user is referring to doesn't appear to have its own dedicated section in the main text.

Looking at where the long-context reference actually appears, it's in a parenthetical at the end of §4.4 (Downstream Evaluation) on line 137, which only mentions Qwen. But the appendix already contains a full table with both Qwen and Llama data for this evaluation. The user likely wants me to integrate the Llama 8K results into the main text where the long-context evaluation is discussed.

I should expand that parenthetical to include the Llama contrast, showing that the long-context amplification effect is specific to Qwen while Llama shows negligible differences between methods at 8K tokens.

Now I'm verifying the numerical calculations to support this claim—checking the degradation ratios at both 2K and 8K context lengths to quantify how the gap between Spread and non-Spread models scales with context. Looking at the 8K results, Qwen shows a dramatic degradation with uniform quantization at 77.75 PPL versus 8.59 constrained, a ~9× ratio, while Llama remains stable. So the gap widens significantly as context length increases — at 2K it's around 1.4× for Qwen, but jumps to 9× at 8K, suggesting the user might be referring to a different metric or I'm misinterpreting which comparison they meant. I think I've found it—the user is likely referring to the ratio between uniform and constrained quantization performance for Qwen specifically, which widens dramatically from about 1.4× at 2K tokens to 9× at 8K tokens, while Llama's ratio stays essentially flat around 1.0× across both contexts. This explains the ~4× to ~9× progression they mentioned, though the exact numbers suggest it's more like 1.4× to 9×.

Looking at the actual text in line 137, I need to replace that parenthetical about long-context with clearer language that captures how the gap between uniform and constrained quantization amplifies with context length, particularly for Qwen.

Let me revise the long-context portion to show both Qwen and Llama, making it clear that this amplification is specific to Spread's approach rather than a general phenomenon.

I'm restructuring this to emphasize how the uniform-vs-constrained gap widens dramatically on Qwen as context length increases, whereas Llama shows minimal degradation in either case, highlighting that Spread's advantage is architecture-dependent rather than universal. I'm checking the actual numbers from the data—at 2K context, the ratio between uniform and constrained allocation is around 1.4×, but at 8K it jumps to about 9×, so the user's "~4× at 2K" might be referring to a different metric or I need to clarify which comparison we're measuring. I need to revise that section to make the narrative clearer. I'll expand line 137 into a fuller paragraph that walks through the Qwen results with actual numbers, contrasts them against Llama's stability, and ties it back to the Spread-specific degradation pattern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "fc2c7c46-abcc-48a6-b16a-76c055a2e102",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnH2FuTcqsKF3KhP44ivNN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 933,
      "cache_read_input_tokens": 30322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 933
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

_source line 16_

The appendix (line 182-210) already has a full long-context section with both Qwen and Llama data in the table. The main text on line 137 only has a parenthetical mentioning Qwen. I need to expand that to include the Llama contrast.

Let me verify the numbers from the appendix table match the user's data:
- Llama BF16 8K: 5.60, Uniform: 6.04 (6.04/5.60 = 1.079×), MCKP: 6.05 (6.05/5.60 = 1.080×) -- matches.
- Qwen uniform/MCKP ratio at 2K: 15.45/10.91 = 1.42×, at 8K: 77.75/8.59 = 9.05×.

Now I'll expand line 137 to integrate Llama as a Spread-specific contrast.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "5c847460-51c6-46f5-a2a4-d6bb3c7276a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnH2FuTcqsKF3KhP44ivNN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 933,
      "cache_read_input_tokens": 30322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 933
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

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_01Fs4rpJYvKQLsCMLiVMDtru`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "old_string": "Cross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
  "new_string": "Cross-dataset evaluation (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) confirms calibration robustness.\nLong-context evaluation (Appendix~\\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\\times$ bf16 at 2K to $11.15\\times$ at 8K, while constrained MCKP remains stable ($1.11\\times$ to $1.23\\times$).\nIn contrast, Llama-3.1-8B (spike, $t_1/t_5{=}0.85$) shows negligible difference between uniform ($1.08\\times$ bf16) and constrained MCKP ($1.08\\times$) at 8K, consistent with its 2K behavior.\nThe uniform-to-constrained PPL ratio on Qwen thus widens from $1.4\\times$ at 2K to $9.1\\times$ at 8K, while Llama remains flat---long-context stress amplifies the spread-specific benefit of per-head allocation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "c19649dd-0416-4cd7-b3b1-d1e8a3d27be4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnH2FuTcqsKF3KhP44ivNN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 933,
      "cache_read_input_tokens": 30322,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 933
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

_source line 18 · 2026-05-16T03:15:23.592Z_

<details><summary>↩ Tool result · reported error · `toolu_01Fs4rpJYvKQLsCMLiVMDtru`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "164c3b5d-0d9c-4bc3-981e-ec8780258873",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01TLPt6BhtrcAovxPbZFaVeb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "offset": 130,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "ed54ee0b-c459-4e1c-8693-26532dc538d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPbg5drJevFzE1wax3vzQ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4036,
      "cache_read_input_tokens": 31255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4036
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

_source line 20 · 2026-05-16T03:15:26.593Z_

<details><summary>↩ Tool result · `toolu_01TLPt6BhtrcAovxPbZFaVeb`</summary>

```text
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	On Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\pm$1$\sigma$ in Table~\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).
135	The four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.
136	ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.
137	Cross-dataset (Appendix~\ref{sec:cross_dataset}, ${>}96\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\ref{sec:long_context}, Qwen uniform $11.15\times$ bf16 at 8K vs.\ MCKP $1.23\times$) analyses confirm allocation robustness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "c492712f-61f9-4ec8-b4b2-d0a021fab2e9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
      "content": "\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
      "numLines": 8,
      "startLine": 130,
      "totalLines": 137
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01MmGqkuvnkSkV49prvjby58`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "old_string": "Cross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
  "new_string": "Cross-dataset evaluation (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) confirms calibration robustness.\nLong-context evaluation (Appendix~\\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\\times$ bf16 at 2K to $11.15\\times$ at 8K, while constrained MCKP remains stable ($1.11\\times$ to $1.23\\times$).\nIn contrast, Llama-3.1-8B (spike, $t_1/t_5{=}0.85$) shows negligible difference between uniform ($1.08\\times$ bf16) and constrained MCKP ($1.08\\times$) at 8K, consistent with its 2K behavior.\nThe uniform-to-constrained PPL ratio on Qwen thus widens from $1.4\\times$ at 2K to $9.1\\times$ at 8K, while Llama remains flat---long-context stress amplifies the spread-specific benefit of per-head allocation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "d538c649-c71a-4a28-b312-2b6bb2dbc430",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PqmrzbnVkGvhFFs3yJXnUb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 486,
      "cache_read_input_tokens": 35291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 486
      },
      "output_tokens": 67,
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

_source line 22 · 2026-05-16T03:15:32.575Z_

<details><summary>↩ Tool result · `toolu_01MmGqkuvnkSkV49prvjby58`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "76bc1793-b074-418f-b921-f86a8df69cfd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "oldString": "Cross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
    "newString": "Cross-dataset evaluation (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) confirms calibration robustness.\nLong-context evaluation (Appendix~\\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\\times$ bf16 at 2K to $11.15\\times$ at 8K, while constrained MCKP remains stable ($1.11\\times$ to $1.23\\times$).\nIn contrast, Llama-3.1-8B (spike, $t_1/t_5{=}0.85$) shows negligible difference between uniform ($1.08\\times$ bf16) and constrained MCKP ($1.08\\times$) at 8K, consistent with its 2K behavior.\nThe uniform-to-constrained PPL ratio on Qwen thus widens from $1.4\\times$ at 2K to $9.1\\times$ at 8K, while Llama remains flat---long-context stress amplifies the spread-specific benefit of per-head allocation.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate eight models spanning seven architecture families and diverse attention configurations:\n\\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\\times$ 4 KV heads = 112),\n\\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\\times$ 8 = 384),\n\\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\\times$ 4 = 192),\n\\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\\times$ 8 = 256),\n\\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\\times$ 8 = 256, sliding window attention),\n\\textbf{Gemma-2-9B} (GQA 2:1, 42 $\\times$ 8 = 336, \\texttt{head\\_dim}=256, attention logit softcapping),\n\\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\\times$ 10 = 400),\nand \\textbf{Pythia-1.4B} (MHA 1:1, 24 $\\times$ 16 = 384).\nThis selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nAll results use high-resolution profiling (64 sequences $\\times$ 2048 tokens from WikiText-2 train); Appendix~\\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\\times$ 512 tok).\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen-7B and Qwen-14B, $k{=}2$ for Yi-1.5 and Llama, $k{=}2$ for Mistral, $k{=}8$ for Gemma-2, Phi-3-medium, and Pythia).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained failure: catastrophic on Qwen-7B ($3.3\\times$ bf16), severe on Pythia ($1.9\\times$), moderate on Gemma-2 ($1.5\\times$), mild on remaining incl.\\ Qwen-14B (${\\sim}1.1\\times$). Greedy and MCKP columns are both unconstrained; identical allocations on 6/8 models (equivalence verified experimentally on Qwen-7B and Qwen-14B; Qwen-14B and Pythia Greedy values inferred via this equivalence). Best constrained result per model in \\textbf{bold}. $^*$BOS-corrected.}\n\\label{tab:main_results}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n\\cmidrule(lr){4-5}\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{10.91} \\\\\nQwen2.5-14B     & 6.87  & 7.20  & 7.69  & 7.69  & 7.22 \\\\\nYi-1.5-9B       & 7.02  & 7.22  & 7.56  & 7.56  & 7.22 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & 8.63  & 8.63  & \\textbf{8.45} \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & 7.57  & 7.60  & 7.13 \\\\\nGemma-2-9B$^*$  & 6.03  & 6.17  & 8.85  & 8.85  & 6.20 \\\\\nPhi-3-medium-14B & 5.64 & 5.80  & 6.07  & 6.07  & 5.81 \\\\\nPythia-1.4B     & 16.49 & 24.29 & 31.54 & 31.54 & 24.45 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen2.5-7B, constrained MCKP achieves 10.91 PPL, a 29.4\\% reduction over uniform 4-bit (15.45).\nWithout the constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure from excessive 2-bit assignments compounding across layers.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the result is essentially indistinguishable from uniform (8.45 vs.\\ 8.47, $\\Delta < 0.02$ PPL).\nHires profiling reveals concentration $0.57$ (comparable to Qwen's $0.61$) but a spike pattern ($t_1/t_5{=}0.85$) dominated by a single head (L2H5), leaving no cross-bitwidth gradient to exploit.\n\nOn Yi-1.5-9B, constrained MCKP ($k{=}2$) matches uniform (7.22); despite high concentration (0.71), sensitivity is dominated by a single outlier (L4H3, $t_1/t_5{=}0.90$), a spike pattern with no cross-bitwidth gradient.\nOn Mistral-7B-v0.3, constrained MCKP ($k{=}2$) matches uniform (7.13 vs.\\ 7.13); near-zero sensitivity differences and sliding-window attention leave no room for reallocation gains.\n\nOn Gemma-2-9B$^*$ (GQA 2:1), constrained MCKP ($k{=}8$) achieves 6.20 PPL vs.\\ uniform 6.17 ($+$0.4\\%).\nDespite flat sensitivity (concentration 0.23), unconstrained MCKP degrades to 8.85 ($1.47\\times$ bf16) from 31.5\\% 2-bit over-allocation; the constraint reduces this to 8 heads, confirming universal over-allocation prevention.\n\nOn Phi-3-medium-14B (GQA 4:1), constrained MCKP ($k{=}8$) achieves 5.81 PPL vs.\\ uniform 5.80, consistent with its flat sensitivity profile (concentration 0.17); unconstrained MCKP degrades mildly to 6.07 ($1.08\\times$ bf16). %exp_id=phi3_medium_constrained_mckp\n\nUnconstrained failure severity tracks heterogeneity shape: \\emph{catastrophic} on Qwen-7B ($3.3\\times$ bf16, 60\\% heads at 2-bit), \\emph{severe} on Pythia ($1.9\\times$), \\emph{moderate} on Gemma-2 ($1.47\\times$), and \\emph{mild} on remaining models (${\\sim}1.07$--$1.12\\times$) including Qwen-14B ($1.12\\times$, 20\\% 2-bit)---the within-family contrast directly reflects shape (spread vs.\\ flat).\nSee Appendix~\\ref{sec:allocation_appendix} (allocation visualization) and Appendix~\\ref{sec:budget_sweep} (budget sweep) for additional detail.\n\nMCKP consistently outperforms random L0-constrained allocation and naive positional baselines across all three tested models (median gap 5--16\\%; Table~\\ref{tab:heuristic} in Appendix~\\ref{sec:heuristic_appendix}).\n\n\\paragraph{Comparison with KIVI.}\nKIVI~\\cite{liu2024kivi} uses asymmetric per-channel quantization with per-token scaling, applied uniformly across all heads.\nAt 4-bit ($r{=}0$), KIVI achieves near-lossless PPL (9.91 on Qwen, 8.14 on Llama vs.\\ 9.81/8.09 bf16), while our symmetric scheme yields 15.45 and 8.47---a gap from the quantization method, not allocation.\nWithin the symmetric scheme, constrained MCKP reduces Qwen from 15.45 to 10.91 ($-$4.54 PPL) by reallocating bits across heads; on Llama (spike), the gain is negligible ($-$0.02).\nThe two approaches are orthogonal and composable: KIVI selects the per-channel scheme, our method selects the per-head bit-width.\nHowever, composability does not imply additive benefit: on Qwen, KIVI+MCKP achieves 9.90 PPL---identical to KIVI alone (9.90; MCKP alone: 10.89), as the per-channel method subsumes the head-level reallocation signal.\nPer-head allocation provides independent value in symmetric-only deployment environments---common in hardware accelerators that lack per-channel asymmetric support---where it is the sole degree of freedom for exploiting sensitivity heterogeneity.\n\n\\subsection{Cross-Architecture Compounding}\n\\label{sec:compounding_cross}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_compounding_curves.pdf}\n\\caption{Compounding effect across architectures. As the number of 2-bit heads ($k$) increases, PPL degradation follows architecture-dependent trajectories: Llama (spike, $c{=}0.57$) explodes to $1519\\times$ at $k{=}256$ due to a single extreme-sensitivity head compounding through the residual stream; Qwen (spread, $c{=}0.61$) degrades $10\\times$; Mistral (flat, $c{=}0.24$) remains most resilient ($6.4\\times$). All three stay near-baseline for $k{\\leq}8$, validating the cardinality constraint regime. Qwen saturates at $k{\\approx}96$ due to its 112 KV heads (maximum ${\\sim}96$ eligible for 2-bit assignment).}\n\\label{fig:compounding_cross}\n\\end{figure}\n\nFigure~\\ref{fig:compounding_cross} shows the compounding sweep across three architectures representing the three sensitivity patterns.\nAt small $k$ (${\\leq}8$), all models tolerate 2-bit assignments with minimal PPL increase (${\\leq}2.5\\%$ over baseline), confirming that the cardinality constraint ($k{=}2$--$8$) operates in the near-additive regime regardless of architecture.\n\nBeyond $k{=}8$, divergence is stark.\nLlama (spike pattern) remains stable through $k{=}32$ (PPL $9.05$, $1.12\\times$ baseline) but explodes at $k{=}128$ ($40.21$) and $k{=}256$ ($1519$, $188\\times$ baseline)---the single extreme-sensitivity head (L2H5) amplifies compounding once enough surrounding heads are also degraded.\nQwen (spread pattern) rises earlier, reaching $23.22$ at $k{=}64$ ($2.4\\times$) and $98.75$ at $k{=}256$ ($10.1\\times$), as its cluster of Layer-0 sensitive heads compound non-additively at moderate $k$.\nMistral (flat pattern) is the most resilient: PPL stays below $8$ through $k{=}64$ and reaches only $45.28$ at $k{=}256$ ($6.4\\times$), consistent with its near-uniform sensitivity distribution offering no single failure mode.\n\nThese curves directly motivate architecture-specific $k$ selection: the compounding onset ($k$ at which PPL exceeds $1.5\\times$ baseline) is ${\\sim}32$ for Qwen, ${\\sim}64$ for Llama, and ${\\sim}128$ for Mistral, with the optimal constrained $k$ lying well below each onset.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\\times$ compression. Qwen values are mean over 3 calibration seeds ($\\pm$1$\\sigma$). Qwen shows gains on HS/PIQA/WG; the remaining models show near-neutral change, tracking PPL results.}\n\\label{tab:downstream}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & ARC-C & HS & PIQA & WG & Avg \\\\\n\\midrule\nQwen2.5-7B        & $+$0.0{\\scriptsize$\\pm$0.4} & $+$4.1{\\scriptsize$\\pm$0.2} & $+$2.0{\\scriptsize$\\pm$0.2} & $+$1.6{\\scriptsize$\\pm$1.2} & $+$1.9 \\\\\nYi-1.5-9B        & $-$2.1 & $-$0.4 & $+$0.0 & $+$0.3 & $-$0.5 \\\\\nLlama-3.1-8B     & $-$0.8 & $+$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\\\\nMistral-7B       & $+$0.0 & $+$0.0 & $-$0.1 & $-$0.1 & $+$0.0 \\\\\nGemma-2-9B       & $-$0.1 & $+$0.0 & $+$0.4 & $+$0.6 & $+$0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
    "structuredPatch": [
      {
        "oldStart": 134,
        "oldLines": 4,
        "newStart": 134,
        "newLines": 7,
        "lines": [
          " On Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).",
          " The four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.",
          " ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.",
          "-Cross-dataset (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) and long-context (Appendix~\\ref{sec:long_context}, Qwen uniform $11.15\\times$ bf16 at 8K vs.\\ MCKP $1.23\\times$) analyses confirm allocation robustness.",
          "\\ No newline at end of file",
          "+Cross-dataset evaluation (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) confirms calibration robustness.",
          "+Long-context evaluation (Appendix~\\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\\times$ bf16 at 2K to $11.15\\times$ at 8K, while constrained MCKP remains stable ($1.11\\times$ to $1.23\\times$).",
          "+In contrast, Llama-3.1-8B (spike, $t_1/t_5{=}0.85$) shows negligible difference between uniform ($1.08\\times$ bf16) and constrained MCKP ($1.08\\times$) at 8K, consistent with its 2K behavior.",
          "+The uniform-to-constrained PPL ratio on Qwen thus widens from $1.4\\times$ at 2K to $9.1\\times$ at 8K, while Llama remains flat---long-context stress amplifies the spread-specific benefit of per-head allocation.",
          "\\ No newline at end of file"
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

### Assistant

_source line 23_

Now let me verify the final result reads well in context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "613004e7-97a5-4a86-bf29-5dac10326a2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSzGDXoGmghRyLvVYUjNQP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 35777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 676
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

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_019CvicGQk7b6MioScfXWWUD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "offset": 134,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "69e8e4b2-d986-425b-acb8-40376e1a2df6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSzGDXoGmghRyLvVYUjNQP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 35777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 676
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

_source line 25 · 2026-05-16T03:15:37.752Z_

<details><summary>↩ Tool result · `toolu_019CvicGQk7b6MioScfXWWUD`</summary>

```text
134	On Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\pm$1$\sigma$ in Table~\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).
135	The four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.
136	ARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.
137	Cross-dataset evaluation (Appendix~\ref{sec:cross_dataset}, ${>}96\%$ bit-assignment agreement across WikiText-2/C4) confirms calibration robustness.
138	Long-context evaluation (Appendix~\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\times$ bf16 at 2K to $11.15\times$ at 8K, while constrained MCKP remains stable ($1.11\times$ to $1.23\times$).
139	In contrast, Llama-3.1-8B (spike, $t_1/t_5{=}0.85$) shows negligible difference between uniform ($1.08\times$ bf16) and constrained MCKP ($1.08\times$) at 8K, consistent with its 2K behavior.
140	The uniform-to-constrained PPL ratio on Qwen thus widens from $1.4\times$ at 2K to $9.1\times$ at 8K, while Llama remains flat---long-context stress amplifies the spread-specific benefit of per-head allocation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "89d94d58-d93b-4d67-947e-4e3517bb4123",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
      "content": "On Qwen, constrained MCKP improves average 0-shot accuracy by 1.9 pts over uniform (mean over 3 seeds, $\\pm$1$\\sigma$ in Table~\\ref{tab:downstream}), with the largest gains on HellaSwag ($+$4.1) and PIQA ($+$2.0).\nThe four non-spread models show near-neutral average change (Yi $-$0.5, Llama $-$0.1, Mistral $+$0.0, Gemma-2 $+$0.2 pts); Mistral is effectively unchanged across all tasks, consistent with its flat sensitivity profile.\nARC-Challenge shows the largest per-task sensitivity across all models (Yi $-$2.1, Llama $-$0.8, Gemma-2 $-$0.1 pts), consistent with multi-step reasoning where KV cache errors accumulate across longer inference chains.\nCross-dataset evaluation (Appendix~\\ref{sec:cross_dataset}, ${>}96\\%$ bit-assignment agreement across WikiText-2/C4) confirms calibration robustness.\nLong-context evaluation (Appendix~\\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\\times$ bf16 at 2K to $11.15\\times$ at 8K, while constrained MCKP remains stable ($1.11\\times$ to $1.23\\times$).\nIn contrast, Llama-3.1-8B (spike, $t_1/t_5{=}0.85$) shows negligible difference between uniform ($1.08\\times$ bf16) and constrained MCKP ($1.08\\times$) at 8K, consistent with its 2K behavior.\nThe uniform-to-constrained PPL ratio on Qwen thus widens from $1.4\\times$ at 2K to $9.1\\times$ at 8K, while Llama remains flat---long-context stress amplifies the spread-specific benefit of per-head allocation.",
      "numLines": 7,
      "startLine": 134,
      "totalLines": 140
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

Now let me verify the other files the user said not to touch remain unchanged, and check for consistency with the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "d7de7baf-a57e-46b6-8344-9251a8ea5f9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESLW2e4X3tt9wvapyEh3Nx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 36453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 671
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

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_01VZytw41vGtigDRxP3q8v8E`</summary>

```json
{
  "pattern": "11\\.15",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
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
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "550eaad4-a42e-45b0-8eaf-9877a37c9059",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESLW2e4X3tt9wvapyEh3Nx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 36453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 671
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

_source line 28 · 2026-05-16T03:15:43.046Z_

<details><summary>↩ Tool result · `toolu_01VZytw41vGtigDRxP3q8v8E`</summary>

```text
docs/paper/experiments.tex:138:Long-context evaluation (Appendix~\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\times$ bf16 at 2K to $11.15\times$ at 8K, while constrained MCKP remains stable ($1.11\times$ to $1.23\times$).
docs/paper/appendix.tex:206:On Qwen (spread), uniform 4-bit degrades from $1.57\times$ bf16 at 2K to $11.15\times$ at 8K---quantization errors accumulate catastrophically over longer sequences.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "3beb466c-d00f-4ff3-b91c-aa0c5ad62873",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments.tex:138:Long-context evaluation (Appendix~\\ref{sec:long_context}) reveals that the spread-pattern advantage amplifies with sequence length: on Qwen (spread), uniform 4-bit degrades from $1.57\\times$ bf16 at 2K to $11.15\\times$ at 8K, while constrained MCKP remains stable ($1.11\\times$ to $1.23\\times$).\ndocs/paper/appendix.tex:206:On Qwen (spread), uniform 4-bit degrades from $1.57\\times$ bf16 at 2K to $11.15\\times$ at 8K---quantization errors accumulate catastrophically over longer sequences.",
    "numLines": 2
  }
}
```

</details>

---

### Assistant

_source line 29_

Numbers are consistent between the main text and appendix. The edit:

- Split the original single-sentence parenthetical into four sentences
- Preserved the cross-dataset reference (line 137)
- Expanded the long-context portion with Qwen data (line 138)
- Added Llama-3.1-8B spike contrast with $t_1/t_5=0.85$ and $1.08\times$ numbers (line 139)
- Closed with the key quantitative contrast: uniform-to-constrained ratio widens from $1.4\times$ to $9.1\times$ on Qwen while Llama stays flat (line 140)

No changes to abstract.tex, introduction.tex, or the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "uuid": "e85ca505-779a-4f4c-a8b3-16635929b240",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtN8BDJGG2Em2Z9dKmQ4j1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 37124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 328
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

_source line 30_

Numbers are consistent between the main text and appendix. The edit:

- Split the original single-sentence parenthetical into four sentences
- Preserved the cross-dataset reference (line 137)
- Expanded the long-context portion with Qwen data (line 138)
- Added Llama-3.1-8B spike contrast with $t_1/t_5=0.85$ and $1.08\times$ numbers (line 139)
- Closed with the key quantitative contrast: uniform-to-constrained ratio widens from $1.4\times$ to $9.1\times$ on Qwen while Llama stays flat (line 140)

No changes to abstract.tex, introduction.tex, or the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 109680,
  "duration_api_ms": 111026,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "bfdc5772-b51c-4613-ba22-fcb99fa880cd",
  "total_cost_usd": 0.45399925,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 25611,
    "cache_read_input_tokens": 301699,
    "output_tokens": 5661,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25611,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 175,
        "cache_read_input_tokens": 37124,
        "cache_creation_input_tokens": 328,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 328
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1376,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0014960000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 5661,
      "cacheReadInputTokens": 301699,
      "cacheCreationInputTokens": 25611,
      "webSearchRequests": 0,
      "costUSD": 0.45250325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "80d8de29-fc57-42c3-afe0-bb9f92bb8596"
}
```

</details>

---
