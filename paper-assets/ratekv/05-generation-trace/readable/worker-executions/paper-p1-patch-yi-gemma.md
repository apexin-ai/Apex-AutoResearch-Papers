# paper p1 patch yi gemma

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_paper_p1-patch-yi-gemma_20260514T185845.log`
- **Structured JSON:** [`28b6a726b703140eecfc.json`](../../sessions/28/28b6a726b703140eecfc.json)

## Before a recorded user message

16 recorded events

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
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
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
  "uuid": "238b155b-0f2f-436b-ad0b-5660099dfd88",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1778796000,
    "rateLimitType": "seven_day",
    "utilization": 0.88,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "1ed77afd-2759-49e7-8da6-58170adac66c",
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316"
}
```

---

### Assistant

_source line 4_

I'll start by reading all the relevant .tex files to understand the current structure and format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "598e04c5-a01d-4213-bd98-d6c63911c8af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9uKRM6A7utL6q9SfSaktk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13631
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — Read · `toolu_01TUedYK9QNhRFaF2Yf8TxH6`</summary>

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
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "1ad23de3-d7d2-42ee-9b38-04bee7f8b698",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9uKRM6A7utL6q9SfSaktk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13631
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-14T18:58:54.589Z_

<details><summary>↩ Tool result · `toolu_01TUedYK9QNhRFaF2Yf8TxH6`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate on three architectures spanning different grouped-query attention (GQA) configurations:
9	\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\times$ 4 KV heads = 112 KV heads),
10	\textbf{Llama-3.1-8B} (4:1, 32 $\times$ 8 = 256 KV heads),
11	and \textbf{Mistral-7B-v0.3} (4:1, 32 $\times$ 8 = 256 KV heads, sliding window attention).
12	This selection covers the two dominant KV head counts (112 vs.\ 256) and both standard and sliding-window attention.
13	
14	\paragraph{Evaluation.}
15	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
16	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
17	
18	\paragraph{Profiling.}
19	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
20	We use two profiling resolutions: \emph{standard} (16 sequences $\times$ 512 tokens) and \emph{high-resolution} (64 sequences $\times$ 2048 tokens), both from WikiText-2 train.
21	Unless marked with $\dagger$, all results use standard-resolution profiling; Appendix~\ref{sec:profiling_resolution} analyzes the effect of resolution.
22	
23	\paragraph{Compression and constraint.}
24	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
25	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).
26	
27	\paragraph{Baselines.}
28	We compare against:
29	(1)~uniform 4-bit quantization;
30	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
31	(3)~unconstrained MCKP allocation;
32	(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
33	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
34	
35	\subsection{Main Results}
36	\label{sec:main_results}
37	
38	\begin{table}[t]
39	\centering
40	\small
41	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained allocation fails catastrophically on $\{2,4,8,16\}$; our cardinality constraint restores performance. Best constrained result per model in \textbf{bold}. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok); standard profiling does not improve over uniform on these architectures. $^\ddagger$Best $k$ from ablation ($k{=}4$). The $\pm$0.06 on Qwen reports std over 3 calibration seeds (hires profiling); bit distributions are identical across seeds.}
42	\label{tab:main_results}
43	\begin{tabular}{lcccccc}
44	\toprule
45	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
46	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
47	\midrule
48	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{11.23}$\pm$0.06 \\
49	Llama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \textbf{8.45}$^\dagger$ \\
50	Mistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\dagger\ddagger}$ \\
51	\bottomrule
52	\end{tabular}
53	\end{table}
54	
55	Table~\ref{tab:main_results} summarizes the main results.
56	On Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\% reduction over uniform 4-bit (15.45).
57	Higher-resolution profiling (64 seq $\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in Appendix~\ref{sec:profiling_resolution}.
58	Without the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.
59	The constraint eliminates this failure mode entirely.
60	Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 (std is 1.3\% of the uniform gap), with 90.2\% three-way allocation agreement, confirming profiling stability.
61	
62	On Llama-3.1-8B, the improvement is marginal: 8.45 vs.\ 8.47 (0.2\%).
63	The profiler finds low sensitivity heterogeneity across Llama's 256 KV heads, leaving little room for non-uniform allocation to improve over uniform.
64	
65	On Mistral-7B-v0.3, constrained MCKP (7.16, $k{=}4$) is slightly worse than uniform (7.13, $+$0.4\%).
66	This is a genuine negative result: the profiler reports near-zero sensitivity differences across heads, meaning the optimization has no reliable signal to exploit.
67	Mistral's sliding-window attention may contribute to this uniformity by limiting head-level variation in effective context length.
68	
69	Unconstrained results for Llama and Mistral are omitted (---) as those experiments were conducted only on Qwen, where the failure mode is most pronounced.
70	Figure~\ref{fig:allocation} visualizes the bit-width allocation on Qwen, showing how constrained MCKP protects Layer-0 heads at 8-bit while selectively assigning only the 8 least-sensitive heads to 2-bit.
71	
72	\begin{figure}[t]
73	\centering
74	\includegraphics[width=\columnwidth]{figures/fig3_allocation_comparison.pdf}
75	\caption{Bit-width allocation on Qwen2.5-7B at 4$\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}
76	\label{fig:allocation}
77	\end{figure}
78	
79	\subsection{Budget Sweep}
80	\label{sec:budget_sweep}
81	
82	\begin{table}[t]
83	\centering
84	\small
85	\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\geq$4$\times$). Standard-resolution profiling; hires results in Appendix~\ref{sec:profiling_resolution}.}
86	\label{tab:budget_sweep}
87	\begin{tabular}{cccc}
88	\toprule
89	Compression & Uniform PPL & Constr.\ MCKP PPL & $\Delta$ PPL \\
90	\midrule
91	2$\times$ & 10.10 & 10.66 & $-$0.56 \\
92	4$\times$ & 15.45 & 11.23 & $+$4.22 \\
93	8$\times$ & 14{,}759 & 907 & $+$13{,}852 \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	Table~\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.
99	
100	At 2$\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\ 9.81 bf16, $+$0.29).
101	Per-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.
102	
103	At 4$\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\% improvement.
104	Hires profiling further reduces this to 10.91 (Appendix~\ref{sec:profiling_resolution}).
105	
106	At 8$\times$, both methods degrade catastrophically---the budget is too aggressive for any allocation to preserve model quality.
107	However, constrained MCKP (907) is an order of magnitude better than uniform (14{,}759) because the constraint still protects Layer-0 heads at 8-bit, preventing total representational collapse.
108	Neither result is practically usable, but the gap demonstrates the protection mechanism at work.
109	
110	\subsection{Heuristic Baselines}
111	\label{sec:heuristic}
112	
113	\begin{table}[t]
114	\centering
115	\small
116	\caption{Constrained MCKP vs.\ heuristic baselines at 4$\times$ compression. L0-random reports median and mean$\pm$std over 5 seeds. All methods use per-model optimal $k$ ($k{=}8$ for Qwen, $k{=}2$ for Llama, $k{=}4$ for Mistral). Llama and Mistral use hires profiling, consistent with Table~\ref{tab:main_results}.}
117	\label{tab:heuristic}
118	\begin{tabular}{lcccc}
119	\toprule
120	Model & MCKP & \multicolumn{2}{c}{L0-random} & Naive \\
121	 & & Median & Mean$\pm$Std & Positional \\
122	\midrule
123	Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\pm$0.47 & 12.23 \\
124	Llama-3.1-8B    & 8.45  & 8.62  & 8.62$\pm$0.07  & 8.58 \\
125	Mistral-7B-v0.3 & 7.16  & 7.20  & 7.24$\pm$0.07  & 7.21 \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	Table~\ref{tab:heuristic} compares profiling-guided MCKP against heuristic baselines that use the same Layer-0 protection but assign 2-bit heads without profiling.
131	
132	On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.
133	
134	On Llama ($k{=}2$), the gap between methods is small: MCKP achieves 8.45 vs.\ L0-random 8.62 and naive positional 8.58.
135	With only 2 heads assigned to 2-bit, the choice of which heads to compress has limited impact, and all methods cluster within 0.17 PPL.
136	MCKP still achieves the best result, but the practical advantage of profiling-guided selection is marginal at this constraint level.
137	
138	On Mistral ($k{=}4$), all non-uniform strategies are worse than uniform 4-bit (7.13): MCKP 7.16, naive 7.21, L0-random median 7.20 (mean 7.24$\pm$0.07).
139	MCKP outperforms both heuristics, but the best non-uniform result (7.16) still exceeds uniform by 0.03 PPL, reinforcing that non-uniform allocation is counterproductive when heterogeneity is low.
140	Note that the heuristic baselines use a slightly higher budget (0.256 vs.\ 0.248 for MCKP, a 3\% difference) because integer $k$ does not divide evenly into the target; despite this advantage, they still underperform MCKP, making the comparison conservative.
141	
142	\subsection{Downstream Evaluation}
143	\label{sec:downstream}
144	
145	\begin{table}[t]
146	\centering
147	\small
148	\caption{0-shot accuracy on Qwen2.5-7B at 4$\times$ compression. Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization.}
149	\label{tab:downstream}
150	\begin{tabular}{lcccc}
151	\toprule
152	Task & Baseline & Uniform & MCKP & $\Delta$ vs \\
153	 & (bf16) & (4-bit) & (Ours) & Uniform \\
154	\midrule
155	ARC-C      & ---   & 0.482 & 0.514 & $+$3.2 pts \\
156	HellaSwag  & ---   & 0.728 & 0.768 & $+$4.0 pts \\
157	PIQA       & ---   & 0.766 & 0.779 & $+$1.3 pts \\
158	WinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\
159	\midrule
160	Average    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\
161	\bottomrule
162	\end{tabular}
163	\end{table}
164	
165	Table~\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.
166	Constrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\ 0.660), with gains on all four benchmarks.
167	The largest gain appears on HellaSwag ($+$4.0 pts), where language modeling quality is most directly reflected.
168	
169	Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization, indicating that per-head bit allocation addresses much of the degradation, though a gap to bf16 remains.
170	
171	\subsection{Cross-Dataset Stability}
172	\label{sec:cross_dataset}
173	
174	To verify that the profiled allocation is not overfit to the calibration corpus, we profile on C4 and evaluate on WikiText-2, and vice versa, at $4\times$ compression.
175	On Qwen2.5-7B, C4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\ 15.45 uniform, a 27\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).
176	In the reverse direction, WikiText-2-calibrated MCKP achieves 20.56 PPL on the C4 held-out split (vs.\ 35.42 uniform, a 42\% reduction; C4 bf16 baseline on this split is 15.32).
177	All three models show ${>}96\%$ bit-assignment agreement across calibration sources: Qwen 96.4\% (108/112 heads), Llama 97.7\% (250/256), and Mistral 96.5\% (247/256).
178	Qwen's agreement is the most informative, as all 112 heads have variable assignments; on Llama, 253 of 256 heads are forced to 4-bit by the $k{=}2$ constraint, inflating agreement.
179	The cross-dataset results reinforce the heterogeneity-driven narrative: on Qwen, the MCKP benefit is preserved across calibration sources; on Llama and Mistral, the lack of benefit is equally stable---Llama's C4-calibrated MCKP is 0.18 PPL worse than uniform, and Mistral shows similar degradation ($-$0.03 to $-$0.05 PPL).
180	Whether non-uniform allocation helps is determined by the model's intrinsic head sensitivity heterogeneity, not the calibration data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "fefafcfa-3577-444d-9d17-f477c29a59ba",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate on three architectures spanning different grouped-query attention (GQA) configurations:\n\\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\\times$ 4 KV heads = 112 KV heads),\n\\textbf{Llama-3.1-8B} (4:1, 32 $\\times$ 8 = 256 KV heads),\nand \\textbf{Mistral-7B-v0.3} (4:1, 32 $\\times$ 8 = 256 KV heads, sliding window attention).\nThis selection covers the two dominant KV head counts (112 vs.\\ 256) and both standard and sliding-window attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nWe use two profiling resolutions: \\emph{standard} (16 sequences $\\times$ 512 tokens) and \\emph{high-resolution} (64 sequences $\\times$ 2048 tokens), both from WikiText-2 train.\nUnless marked with $\\dagger$, all results use standard-resolution profiling; Appendix~\\ref{sec:profiling_resolution} analyzes the effect of resolution.\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained allocation fails catastrophically on $\\{2,4,8,16\\}$; our cardinality constraint restores performance. Best constrained result per model in \\textbf{bold}. $^\\dagger$Hires profiling (64 seq $\\times$ 2048 tok); standard profiling does not improve over uniform on these architectures. $^\\ddagger$Best $k$ from ablation ($k{=}4$). The $\\pm$0.06 on Qwen reports std over 3 calibration seeds (hires profiling); bit distributions are identical across seeds.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{11.23}$\\pm$0.06 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \\textbf{8.45}$^\\dagger$ \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\\dagger\\ddagger}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:main_results} summarizes the main results.\nOn Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\\% reduction over uniform 4-bit (15.45).\nHigher-resolution profiling (64 seq $\\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in Appendix~\\ref{sec:profiling_resolution}.\nWithout the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.\nThe constraint eliminates this failure mode entirely.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 (std is 1.3\\% of the uniform gap), with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the improvement is marginal: 8.45 vs.\\ 8.47 (0.2\\%).\nThe profiler finds low sensitivity heterogeneity across Llama's 256 KV heads, leaving little room for non-uniform allocation to improve over uniform.\n\nOn Mistral-7B-v0.3, constrained MCKP (7.16, $k{=}4$) is slightly worse than uniform (7.13, $+$0.4\\%).\nThis is a genuine negative result: the profiler reports near-zero sensitivity differences across heads, meaning the optimization has no reliable signal to exploit.\nMistral's sliding-window attention may contribute to this uniformity by limiting head-level variation in effective context length.\n\nUnconstrained results for Llama and Mistral are omitted (---) as those experiments were conducted only on Qwen, where the failure mode is most pronounced.\nFigure~\\ref{fig:allocation} visualizes the bit-width allocation on Qwen, showing how constrained MCKP protects Layer-0 heads at 8-bit while selectively assigning only the 8 least-sensitive heads to 2-bit.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_allocation_comparison.pdf}\n\\caption{Bit-width allocation on Qwen2.5-7B at 4$\\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}\n\\label{fig:allocation}\n\\end{figure}\n\n\\subsection{Budget Sweep}\n\\label{sec:budget_sweep}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\\geq$4$\\times$). Standard-resolution profiling; hires results in Appendix~\\ref{sec:profiling_resolution}.}\n\\label{tab:budget_sweep}\n\\begin{tabular}{cccc}\n\\toprule\nCompression & Uniform PPL & Constr.\\ MCKP PPL & $\\Delta$ PPL \\\\\n\\midrule\n2$\\times$ & 10.10 & 10.66 & $-$0.56 \\\\\n4$\\times$ & 15.45 & 11.23 & $+$4.22 \\\\\n8$\\times$ & 14{,}759 & 907 & $+$13{,}852 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.\n\nAt 2$\\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\\ 9.81 bf16, $+$0.29).\nPer-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.\n\nAt 4$\\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\\% improvement.\nHires profiling further reduces this to 10.91 (Appendix~\\ref{sec:profiling_resolution}).\n\nAt 8$\\times$, both methods degrade catastrophically---the budget is too aggressive for any allocation to preserve model quality.\nHowever, constrained MCKP (907) is an order of magnitude better than uniform (14{,}759) because the constraint still protects Layer-0 heads at 8-bit, preventing total representational collapse.\nNeither result is practically usable, but the gap demonstrates the protection mechanism at work.\n\n\\subsection{Heuristic Baselines}\n\\label{sec:heuristic}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Constrained MCKP vs.\\ heuristic baselines at 4$\\times$ compression. L0-random reports median and mean$\\pm$std over 5 seeds. All methods use per-model optimal $k$ ($k{=}8$ for Qwen, $k{=}2$ for Llama, $k{=}4$ for Mistral). Llama and Mistral use hires profiling, consistent with Table~\\ref{tab:main_results}.}\n\\label{tab:heuristic}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & MCKP & \\multicolumn{2}{c}{L0-random} & Naive \\\\\n & & Median & Mean$\\pm$Std & Positional \\\\\n\\midrule\nQwen2.5-7B      & 11.23 & 11.52 & 11.69$\\pm$0.47 & 12.23 \\\\\nLlama-3.1-8B    & 8.45  & 8.62  & 8.62$\\pm$0.07  & 8.58 \\\\\nMistral-7B-v0.3 & 7.16  & 7.20  & 7.24$\\pm$0.07  & 7.21 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:heuristic} compares profiling-guided MCKP against heuristic baselines that use the same Layer-0 protection but assign 2-bit heads without profiling.\n\nOn Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.\n\nOn Llama ($k{=}2$), the gap between methods is small: MCKP achieves 8.45 vs.\\ L0-random 8.62 and naive positional 8.58.\nWith only 2 heads assigned to 2-bit, the choice of which heads to compress has limited impact, and all methods cluster within 0.17 PPL.\nMCKP still achieves the best result, but the practical advantage of profiling-guided selection is marginal at this constraint level.\n\nOn Mistral ($k{=}4$), all non-uniform strategies are worse than uniform 4-bit (7.13): MCKP 7.16, naive 7.21, L0-random median 7.20 (mean 7.24$\\pm$0.07).\nMCKP outperforms both heuristics, but the best non-uniform result (7.16) still exceeds uniform by 0.03 PPL, reinforcing that non-uniform allocation is counterproductive when heterogeneity is low.\nNote that the heuristic baselines use a slightly higher budget (0.256 vs.\\ 0.248 for MCKP, a 3\\% difference) because integer $k$ does not divide evenly into the target; despite this advantage, they still underperform MCKP, making the comparison conservative.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy on Qwen2.5-7B at 4$\\times$ compression. Constrained MCKP recovers approximately 73\\% of the accuracy lost by uniform 4-bit quantization.}\n\\label{tab:downstream}\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Baseline & Uniform & MCKP & $\\Delta$ vs \\\\\n & (bf16) & (4-bit) & (Ours) & Uniform \\\\\n\\midrule\nARC-C      & ---   & 0.482 & 0.514 & $+$3.2 pts \\\\\nHellaSwag  & ---   & 0.728 & 0.768 & $+$4.0 pts \\\\\nPIQA       & ---   & 0.766 & 0.779 & $+$1.3 pts \\\\\nWinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\\\\n\\midrule\nAverage    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.\nConstrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\\ 0.660), with gains on all four benchmarks.\nThe largest gain appears on HellaSwag ($+$4.0 pts), where language modeling quality is most directly reflected.\n\nConstrained MCKP recovers approximately 73\\% of the accuracy lost by uniform 4-bit quantization, indicating that per-head bit allocation addresses much of the degradation, though a gap to bf16 remains.\n\n\\subsection{Cross-Dataset Stability}\n\\label{sec:cross_dataset}\n\nTo verify that the profiled allocation is not overfit to the calibration corpus, we profile on C4 and evaluate on WikiText-2, and vice versa, at $4\\times$ compression.\nOn Qwen2.5-7B, C4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\\ 15.45 uniform, a 27\\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).\nIn the reverse direction, WikiText-2-calibrated MCKP achieves 20.56 PPL on the C4 held-out split (vs.\\ 35.42 uniform, a 42\\% reduction; C4 bf16 baseline on this split is 15.32).\nAll three models show ${>}96\\%$ bit-assignment agreement across calibration sources: Qwen 96.4\\% (108/112 heads), Llama 97.7\\% (250/256), and Mistral 96.5\\% (247/256).\nQwen's agreement is the most informative, as all 112 heads have variable assignments; on Llama, 253 of 256 heads are forced to 4-bit by the $k{=}2$ constraint, inflating agreement.\nThe cross-dataset results reinforce the heterogeneity-driven narrative: on Qwen, the MCKP benefit is preserved across calibration sources; on Llama and Mistral, the lack of benefit is equally stable---Llama's C4-calibrated MCKP is 0.18 PPL worse than uniform, and Mistral shows similar degradation ($-$0.03 to $-$0.05 PPL).\nWhether non-uniform allocation helps is determined by the model's intrinsic head sensitivity heterogeneity, not the calibration data.",
      "numLines": 180,
      "startLine": 1,
      "totalLines": 180
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_011qEx7D5sHU6VVnTWGgNfvs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "882b83ca-36ec-41ef-8ce2-e0a1c057a9a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9uKRM6A7utL6q9SfSaktk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13631
      },
      "output_tokens": 4,
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

_source line 8 · 2026-05-14T18:58:55.503Z_

<details><summary>↩ Tool result · `toolu_011qEx7D5sHU6VVnTWGgNfvs`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across three architectures at $4\times$ compression.
12	Qwen2.5-7B exhibits the highest heterogeneity (top-5\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.
13	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\% improvement over uniform 4-bit.
14	Llama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\ $+$0.38).
15	Mistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.
16	Here, constrained MCKP is slightly \emph{worse} than uniform ($+$0.13 vs.\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\times$ compression. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok).}
22	\label{tab:heterogeneity}
23	\begin{tabular}{lccccc}
24	\toprule
25	Model & GQA & Top-5\% & $\Delta$ PPL & $\Delta$ PPL & Recommendation \\
26	 & Ratio & Conc. & (Uniform) & (Ours) & \\
27	\midrule
28	Qwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\
29	Llama-3.1-8B$^\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\
30	Mistral-7B-v0.3$^\dagger$ & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\begin{figure*}[t]
36	\centering
37	\includegraphics[width=\textwidth]{figures/fig1_head_delta_heatmap.pdf}
38	\caption{Per-head 2-bit quantization sensitivity across three models. Qwen2.5-7B (left) shows high concentration in Layer-0 heads; Llama-3.1-8B (center) shows moderate spread; Mistral-7B-v0.3 (right) shows near-zero sensitivity across all heads. Color intensity indicates PPL increase when the head is quantized to 2-bit.}
39	\label{fig:heatmap}
40	\end{figure*}
41	
42	Figure~\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.
43	The contrast is stark: Qwen's Layer-0 heads show high distortion (dark cells) while mid-to-deep layers are near-zero; Mistral shows uniformly low distortion across all layers and heads.
44	
45	\subsection{Diagnostic Framework}
46	\label{sec:diagnostic}
47	
48	The heterogeneity characterization yields a preliminary guideline, based on three architectures, for deciding when non-uniform allocation is worthwhile:
49	
50	\begin{enumerate}[nosep]
51	\item Run per-head profiling as described in \S\ref{sec:profiling}.
52	\item Compute the top-5\% concentration from the resulting distortion table.
53	\item Select allocation strategy:
54	  \begin{itemize}[nosep]
55	  \item Concentration ${>}\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\% PPL improvement).
56	  \item Concentration $0.30$--$0.50$: marginal benefit; depends on target compression ratio (Llama case; 0.2\% at $4\times$).
57	  \item Near-zero absolute distortion for most heads: use uniform directly (Mistral case; non-uniform is counterproductive).
58	  \end{itemize}
59	\end{enumerate}
60	
61	The diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver.
62	This avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.
63	The thresholds above are derived from three architectures and should be validated on a broader set of models before being treated as general rules.
64	Additional analyses---the effect of aggressive compression ratios, profiling resolution and multi-seed stability, per-layer optimality validation, and KV separation ablation---are provided in Appendices~\ref{sec:aggressive}--\ref{sec:kv_separation}.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "925b0918-57c4-40ff-a62a-ece3de73226f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Heterogeneity Characterization}\n\\label{sec:heterogeneity}\n\nThe benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.\nWe quantify this with a \\emph{top-5\\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\\% of heads.\nHigh concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.\n\nTable~\\ref{tab:heterogeneity} summarizes the results across three architectures at $4\\times$ compression.\nQwen2.5-7B exhibits the highest heterogeneity (top-5\\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\\% improvement over uniform 4-bit.\nLlama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\\ $+$0.38).\nMistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.\nHere, constrained MCKP is slightly \\emph{worse} than uniform ($+$0.13 vs.\\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\\times$ compression. $^\\dagger$Hires profiling (64 seq $\\times$ 2048 tok).}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & GQA & Top-5\\% & $\\Delta$ PPL & $\\Delta$ PPL & Recommendation \\\\\n & Ratio & Conc. & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\\\\nLlama-3.1-8B$^\\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\\\\nMistral-7B-v0.3$^\\dagger$ & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_head_delta_heatmap.pdf}\n\\caption{Per-head 2-bit quantization sensitivity across three models. Qwen2.5-7B (left) shows high concentration in Layer-0 heads; Llama-3.1-8B (center) shows moderate spread; Mistral-7B-v0.3 (right) shows near-zero sensitivity across all heads. Color intensity indicates PPL increase when the head is quantized to 2-bit.}\n\\label{fig:heatmap}\n\\end{figure*}\n\nFigure~\\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.\nThe contrast is stark: Qwen's Layer-0 heads show high distortion (dark cells) while mid-to-deep layers are near-zero; Mistral shows uniformly low distortion across all layers and heads.\n\n\\subsection{Diagnostic Framework}\n\\label{sec:diagnostic}\n\nThe heterogeneity characterization yields a preliminary guideline, based on three architectures, for deciding when non-uniform allocation is worthwhile:\n\n\\begin{enumerate}[nosep]\n\\item Run per-head profiling as described in \\S\\ref{sec:profiling}.\n\\item Compute the top-5\\% concentration from the resulting distortion table.\n\\item Select allocation strategy:\n  \\begin{itemize}[nosep]\n  \\item Concentration ${>}\\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\\% PPL improvement).\n  \\item Concentration $0.30$--$0.50$: marginal benefit; depends on target compression ratio (Llama case; 0.2\\% at $4\\times$).\n  \\item Near-zero absolute distortion for most heads: use uniform directly (Mistral case; non-uniform is counterproductive).\n  \\end{itemize}\n\\end{enumerate}\n\nThe diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver.\nThis avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.\nThe thresholds above are derived from three architectures and should be validated on a broader set of models before being treated as general rules.\nAdditional analyses---the effect of aggressive compression ratios, profiling resolution and multi-seed stability, per-layer optimality validation, and KV separation ablation---are provided in Appendices~\\ref{sec:aggressive}--\\ref{sec:kv_separation}.\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_014f24gmrSv3fcauJwmpvGNc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "b354ff3f-1930-4277-b3f6-0069b8e8a812",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9uKRM6A7utL6q9SfSaktk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13631
      },
      "output_tokens": 4,
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

_source line 10 · 2026-05-14T18:58:56.005Z_

<details><summary>↩ Tool result · `toolu_014f24gmrSv3fcauJwmpvGNc`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Per-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.
5	Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
6	RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
7	
8	In practice, hardware-efficient inference requires bit-widths drawn from $\{2, 4, 8, 16\}$---the formats natively supported by modern accelerators.
9	On this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.
10	One might expect that exact MCKP solvers would fill this gap.
11	They do not.
12	On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
13	The optimization does not merely underperform; it fails catastrophically.
14	
15	The root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.
17	The additive model predicts $\sim$11 PPL for these allocations; the actual PPL is $3$--$4\times$ higher.
18	At 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves close to its additive prediction---but 2-bit distortions are orders of magnitude larger.
19	When most heads are quantized to 2-bit simultaneously, cumulative truncation errors exceed the network's capacity to compensate, and perplexity degrades super-linearly.
20	
21	This observation points to a minimal intervention: cap the number of 2-bit assignments.
22	We add a single cardinality constraint $\sum_h \mathbb{1}[b_h{=}2] \leq k$ to the standard MCKP formulation (\S\ref{sec:method}).
23	On Qwen2.5-7B, setting $k{=}8$ (7\% of heads) yields 11.23 PPL---a 27.3\% reduction over uniform 4-bit.
24	The constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.
25	This is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.
26	
27	A surprising consequence is that, under the cardinality constraint, the choice of solver becomes irrelevant.
28	Constrained greedy and constrained MCKP produce identical allocations---not approximately, but exactly: all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3 (the single difference is a zero-distortion tie with no PPL impact).
29	The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal (\S\ref{sec:solver_equiv}), enabling practitioners to use the simpler $O(H \log H)$ greedy algorithm without sacrificing solution quality.
30	A per-layer brute-force oracle confirms near-optimality: the maximum gap across 28 layers is 0.02 PPL, 0.4\% of the total improvement (\S\ref{sec:solver_equiv}).
31	
32	However, non-uniform allocation does not help universally.
33	On Llama-3.1-8B, constrained MCKP achieves 8.45 PPL vs.\ uniform 8.47---a marginal 0.2\% improvement.
34	On Mistral-7B-v0.3, it is slightly \emph{worse}: 7.16 vs.\ 7.13.
35	The difference across architectures traces to head sensitivity heterogeneity: Qwen's KV heads vary widely in 2-bit distortion, with Layer-0 heads contributing a disproportionate share, while Mistral's heads are nearly uniform in sensitivity.
36	When there is no heterogeneity to exploit, non-uniform allocation adds noise without benefit.
37	
38	This motivates a diagnostic question that prior work does not address: \emph{when} should a practitioner use per-head mixed-precision quantization?
39	We propose a heterogeneity diagnostic based on the top-5\% concentration of per-head distortion (\S\ref{sec:heterogeneity}).
40	On our three architectures, the concentration metric---combined with the absolute magnitude of per-head distortion---separates the beneficial case (Qwen, concentration 0.59--0.66, 27.3\% PPL improvement) from cases where non-uniform allocation provides marginal (Llama) or no benefit (Mistral), across the three tested architectures.
41	The diagnostic reuses profiling data already required by the solver and adds no computational overhead.
42	
43	Our contributions are:
44	\begin{enumerate}[nosep]
45	\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
46	
47	\item We demonstrate that the cardinality constraint makes solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent per-head allocations across three architectures, enabling use of a simple greedy algorithm (\S\ref{sec:solver_equiv}).
48	
49	\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes (\S\ref{sec:heterogeneity}).
50	\end{enumerate}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "dd5470c1-4d79-4723-bca6-a05f5dc4b083",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nPer-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.\nRecent work on KV cache quantization explores both uniform schemes~\\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\\cite{zhang2023h2o,li2024snapkv}.\nRateQuant~\\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\\{2,3,4,5,6\\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).\n\nIn practice, hardware-efficient inference requires bit-widths drawn from $\\{2, 4, 8, 16\\}$---the formats natively supported by modern accelerators.\nOn this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.\nOne might expect that exact MCKP solvers would fill this gap.\nThey do not.\nOn Qwen2.5-7B at $4\\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \\emph{far worse} than uniform 4-bit (15.45).\nThe optimization does not merely underperform; it fails catastrophically.\n\nThe root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.\nBoth solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.\nThe additive model predicts $\\sim$11 PPL for these allocations; the actual PPL is $3$--$4\\times$ higher.\nAt 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves close to its additive prediction---but 2-bit distortions are orders of magnitude larger.\nWhen most heads are quantized to 2-bit simultaneously, cumulative truncation errors exceed the network's capacity to compensate, and perplexity degrades super-linearly.\n\nThis observation points to a minimal intervention: cap the number of 2-bit assignments.\nWe add a single cardinality constraint $\\sum_h \\mathbb{1}[b_h{=}2] \\leq k$ to the standard MCKP formulation (\\S\\ref{sec:method}).\nOn Qwen2.5-7B, setting $k{=}8$ (7\\% of heads) yields 11.23 PPL---a 27.3\\% reduction over uniform 4-bit.\nThe constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.\nThis is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.\n\nA surprising consequence is that, under the cardinality constraint, the choice of solver becomes irrelevant.\nConstrained greedy and constrained MCKP produce identical allocations---not approximately, but exactly: all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3 (the single difference is a zero-distortion tie with no PPL impact).\nThe constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal (\\S\\ref{sec:solver_equiv}), enabling practitioners to use the simpler $O(H \\log H)$ greedy algorithm without sacrificing solution quality.\nA per-layer brute-force oracle confirms near-optimality: the maximum gap across 28 layers is 0.02 PPL, 0.4\\% of the total improvement (\\S\\ref{sec:solver_equiv}).\n\nHowever, non-uniform allocation does not help universally.\nOn Llama-3.1-8B, constrained MCKP achieves 8.45 PPL vs.\\ uniform 8.47---a marginal 0.2\\% improvement.\nOn Mistral-7B-v0.3, it is slightly \\emph{worse}: 7.16 vs.\\ 7.13.\nThe difference across architectures traces to head sensitivity heterogeneity: Qwen's KV heads vary widely in 2-bit distortion, with Layer-0 heads contributing a disproportionate share, while Mistral's heads are nearly uniform in sensitivity.\nWhen there is no heterogeneity to exploit, non-uniform allocation adds noise without benefit.\n\nThis motivates a diagnostic question that prior work does not address: \\emph{when} should a practitioner use per-head mixed-precision quantization?\nWe propose a heterogeneity diagnostic based on the top-5\\% concentration of per-head distortion (\\S\\ref{sec:heterogeneity}).\nOn our three architectures, the concentration metric---combined with the absolute magnitude of per-head distortion---separates the beneficial case (Qwen, concentration 0.59--0.66, 27.3\\% PPL improvement) from cases where non-uniform allocation provides marginal (Llama) or no benefit (Mistral), across the three tested architectures.\nThe diagnostic reuses profiling data already required by the solver and adds no computational overhead.\n\nOur contributions are:\n\\begin{enumerate}[nosep]\n\\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\\times$ compression (\\S\\ref{sec:compounding}, \\S\\ref{sec:experiments}).\n\n\\item We demonstrate that the cardinality constraint makes solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent per-head allocations across three architectures, enabling use of a simple greedy algorithm (\\S\\ref{sec:solver_equiv}).\n\n\\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes (\\S\\ref{sec:heterogeneity}).\n\\end{enumerate}\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01QyvpuGvwh8vf73DStW77a8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "b624ab6b-604c-4a67-9882-e7b7aeaebefb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9uKRM6A7utL6q9SfSaktk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13631
      },
      "output_tokens": 4,
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

_source line 12 · 2026-05-14T18:58:56.460Z_

<details><summary>↩ Tool result · `toolu_01QyvpuGvwh8vf73DStW77a8`</summary>

```text
1	Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\{2, 4, 8, 16\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).
2	We trace this failure to \emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.
3	We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
4	On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
5	The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
6	However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\ 7.13).
7	We propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that can indicate, before any allocation, whether a given architecture will benefit from non-uniform quantization.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "08e5a671-2dad-4cda-9b06-bde5226a3914",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex",
      "content": "Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\\{2, 4, 8, 16\\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).\nWe trace this failure to \\emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.\nWe show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.\nOn Qwen2.5-7B at $4\\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\\% reduction over uniform 4-bit.\nThe constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\\Delta{=}0.0000$), enabling use of a simple $O(H \\log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).\nHowever, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\\ 7.13).\nWe propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that can indicate, before any allocation, whether a given architecture will benefit from non-uniform quantization.\n",
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_019ep6rSt5xiWH8RDi9N5Rhm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "e5553a41-3f51-44fd-b251-3bff1482d56f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9uKRM6A7utL6q9SfSaktk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13631
      },
      "output_tokens": 4,
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

_source line 14 · 2026-05-14T18:58:56.954Z_

<details><summary>↩ Tool result · `toolu_019ep6rSt5xiWH8RDi9N5Rhm`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.
4	A single constraint---limiting simultaneously active 2-bit heads to $k \leq 8$ (7\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\% improvement at $4\times$ compression.
5	Under the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\Delta = 0.0000$), so a simple $O(H \log H)$ greedy algorithm suffices.
6	The benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) is slightly counterproductive (7.16 vs.\ 7.13 PPL).
7	This diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \emph{before deployment} whether non-uniform quantization is worthwhile for a given model.
8	
9	\paragraph{Limitations.}
10	Our study has several limitations that temper the generality of the findings.
11	First, we evaluate only three 7B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.
12	Second, profiling relies on a single sensitivity metric (perplexity-based per-head distortion); alternative measures such as gradient-based or activation-norm diagnostics remain unexplored and could yield different allocation decisions.
13	Third, we report perplexity and downstream accuracy but no real-kernel latency benchmarks, leaving the practical inference speedup from mixed-precision allocation unquantified.
14	Fourth, we have not verified whether these findings transfer to larger scales (70B+), where head counts and attention patterns differ substantially.
15	Finally, although we validate on four downstream tasks, profiling and primary evaluation use a single dataset (WikiText-2).
16	
17	\paragraph{Future Work.}
18	Extending evaluation to 70B+ models would test whether the heterogeneity--benefit relationship holds at scale.
19	Integration with production inference engines (vLLM, TensorRT-LLM) would enable real-kernel latency measurement, and investigating per-side K/V cardinality constraints (Appendix~\ref{sec:kv_separation}) or dynamic per-request allocation could further improve the framework.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "03dddd6f-26bf-461a-bab0-8eb37df93983",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \\{2, 4, 8, 16\\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.\nA single constraint---limiting simultaneously active 2-bit heads to $k \\leq 8$ (7\\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\\% improvement at $4\\times$ compression.\nUnder the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\\Delta = 0.0000$), so a simple $O(H \\log H)$ greedy algorithm suffices.\nThe benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) is slightly counterproductive (7.16 vs.\\ 7.13 PPL).\nThis diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \\emph{before deployment} whether non-uniform quantization is worthwhile for a given model.\n\n\\paragraph{Limitations.}\nOur study has several limitations that temper the generality of the findings.\nFirst, we evaluate only three 7B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.\nSecond, profiling relies on a single sensitivity metric (perplexity-based per-head distortion); alternative measures such as gradient-based or activation-norm diagnostics remain unexplored and could yield different allocation decisions.\nThird, we report perplexity and downstream accuracy but no real-kernel latency benchmarks, leaving the practical inference speedup from mixed-precision allocation unquantified.\nFourth, we have not verified whether these findings transfer to larger scales (70B+), where head counts and attention patterns differ substantially.\nFinally, although we validate on four downstream tasks, profiling and primary evaluation use a single dataset (WikiText-2).\n\n\\paragraph{Future Work.}\nExtending evaluation to 70B+ models would test whether the heterogeneity--benefit relationship holds at scale.\nIntegration with production inference engines (vLLM, TensorRT-LLM) would enable real-kernel latency measurement, and investigating per-side K/V cardinality constraints (Appendix~\\ref{sec:kv_separation}) or dynamic per-request allocation could further improve the framework.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01835FKhMy487eb9jS7ANeYS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "f7681c94-9324-4009-b34d-9f05ea42c742",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9uKRM6A7utL6q9SfSaktk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13631,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13631
      },
      "output_tokens": 4,
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

_source line 16 · 2026-05-14T18:58:57.137Z_

<details><summary>↩ Tool result · `toolu_01835FKhMy487eb9jS7ANeYS`</summary>

```text
1	\appendix
2	
3	\section{Aggressive Compression}
4	\label{sec:aggressive}
5	
6	At $4\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.
7	At more aggressive ratios, the picture changes: at $5.3\times$ (average 3 bits), constrained MCKP achieves $45\times$ lower PPL than uniform on Llama (57.60 vs.\ 2643.77) and $44\times$ on Mistral (11.91 vs.\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.
8	At $8\times$, the budget is too constrained for any allocation to preserve quality (both methods degrade catastrophically).
9	The intermediate regime ($5.3\times$) provides the largest relative benefit.
10	
11	\section{Profiling Resolution and Stability}
12	\label{sec:profiling_resolution}
13	
14	We compare standard-resolution profiling (16 sequences $\times$ 512 tokens) against high-resolution profiling (64 sequences $\times$ 2048 tokens) on Qwen2.5-7B at $4\times$ compression.
15	
16	High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
17	Relative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\% reduction.
18	The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\times$ more).
19	
20	The additional signal changes 8 of 112 head assignments.
21	High-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.
22	
23	\paragraph{Multi-seed stability.}
24	The profiled allocation is stable across calibration subsets.
25	Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\%.
26	The bit distribution is identical across all seeds ($\{$2-bit: 8, 4-bit: 100, 8-bit: 4$\}$), and 101 of 112 heads (90.2\%) receive the same assignment in all three runs.
27	This stability confirms that the per-head sensitivity ranking is robust to calibration sampling noise.
28	
29	\paragraph{Per-layer optimality.}
30	To validate the additive distortion assumption underlying the MCKP formulation, we compare constrained MCKP against a per-layer brute-force oracle that exhaustively enumerates all $4^4 = 256$ bit-width combinations within each 4-head group on Qwen2.5-7B (hires profiling).
31	Of the 8 layers admitting multiple feasible allocations, MCKP matches the oracle exactly in 5; the remaining 3 show gaps of 0.018 (Layer~1), 0.014 (Layer~11), and 0.005 (Layer~4) PPL.
32	All three gaps involve repositioning a 2-bit assignment among heads with near-identical sensitivity within the same layer bit budget.
33	The negligible total gap ($<0.04$ PPL) confirms that the per-head additive distortion model closely approximates the true layer-level interaction.
34	
35	\section{KV Separation Ablation}
36	\label{sec:kv_separation}
37	
38	We test whether treating K and V caches as independent items in the MCKP solver---allowing different bit-widths for K and V within the same head---improves over joint allocation where K and V share a bit-width.
39	
40	Joint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).
41	The degradation stems from K-side over-compression: the separated solver doubles the maximum number of 2-bit K items to 16 (vs.\ 8 in the joint formulation), since K and V are counted independently against the cardinality constraint.
42	Meanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.
43	
44	Of the 112 heads, 21 show K$\neq$V asymmetry in the separated allocation, all with K receiving a lower bit-width than V.
45	This systematic asymmetry suggests that K caches are inherently more compressible than V caches, consistent with the observation that key vectors primarily encode positional information while value vectors carry content.
46	
47	Joint allocation is sufficient under the current constraint formulation.
48	Separated K/V allocation with per-side cardinality constraints---limiting 2-bit assignments independently for K and V---is a direction for future work.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "630f5873-abde-4a07-a332-d74e0f858316",
  "uuid": "e402cd67-f00d-4913-a84d-57273eb0394a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{Aggressive Compression}\n\\label{sec:aggressive}\n\nAt $4\\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.\nAt more aggressive ratios, the picture changes: at $5.3\\times$ (average 3 bits), constrained MCKP achieves $45\\times$ lower PPL than uniform on Llama (57.60 vs.\\ 2643.77) and $44\\times$ on Mistral (11.91 vs.\\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.\nAt $8\\times$, the budget is too constrained for any allocation to preserve quality (both methods degrade catastrophically).\nThe intermediate regime ($5.3\\times$) provides the largest relative benefit.\n\n\\section{Profiling Resolution and Stability}\n\\label{sec:profiling_resolution}\n\nWe compare standard-resolution profiling (16 sequences $\\times$ 512 tokens) against high-resolution profiling (64 sequences $\\times$ 2048 tokens) on Qwen2.5-7B at $4\\times$ compression.\n\nHigh-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).\nRelative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\\% reduction.\nThe improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\\times$ more).\n\nThe additional signal changes 8 of 112 head assignments.\nHigh-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.\n\n\\paragraph{Multi-seed stability.}\nThe profiled allocation is stable across calibration subsets.\nUnder hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \\pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\\%.\nThe bit distribution is identical across all seeds ($\\{$2-bit: 8, 4-bit: 100, 8-bit: 4$\\}$), and 101 of 112 heads (90.2\\%) receive the same assignment in all three runs.\nThis stability confirms that the per-head sensitivity ranking is robust to calibration sampling noise.\n\n\\paragraph{Per-layer optimality.}\nTo validate the additive distortion assumption underlying the MCKP formulation, we compare constrained MCKP against a per-layer brute-force oracle that exhaustively enumerates all $4^4 = 256$ bit-width combinations within each 4-head group on Qwen2.5-7B (hires profiling).\nOf the 8 layers admitting multiple feasible allocations, MCKP matches the oracle exactly in 5; the remaining 3 show gaps of 0.018 (Layer~1), 0.014 (Layer~11), and 0.005 (Layer~4) PPL.\nAll three gaps involve repositioning a 2-bit assignment among heads with near-identical sensitivity within the same layer bit budget.\nThe negligible total gap ($<0.04$ PPL) confirms that the per-head additive distortion model closely approximates the true layer-level interaction.\n\n\\section{KV Separation Ablation}\n\\label{sec:kv_separation}\n\nWe test whether treating K and V caches as independent items in the MCKP solver---allowing different bit-widths for K and V within the same head---improves over joint allocation where K and V share a bit-width.\n\nJoint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).\nThe degradation stems from K-side over-compression: the separated solver doubles the maximum number of 2-bit K items to 16 (vs.\\ 8 in the joint formulation), since K and V are counted independently against the cardinality constraint.\nMeanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.\n\nOf the 112 heads, 21 show K$\\neq$V asymmetry in the separated allocation, all with K receiving a lower bit-width than V.\nThis systematic asymmetry suggests that K caches are inherently more compressible than V caches, consistent with the observation that key vectors primarily encode positional information while value vectors carry content.\n\nJoint allocation is sufficient under the current constraint formulation.\nSeparated K/V allocation with per-side cardinality constraints---limiting 2-bit assignments independently for K and V---is a direction for future work.\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  }
}
```

</details>

---
