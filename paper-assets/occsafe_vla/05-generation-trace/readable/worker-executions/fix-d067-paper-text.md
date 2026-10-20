# fix d067 paper text

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_fix_d067-paper-text_20260527T042938.log`
- **Structured JSON:** [`ac00639902e0db63d6c0.json`](../../sessions/ac/ac00639902e0db63d6c0.json)

## Before a recorded user message

37 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
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
  "uuid": "12de369f-7654-45ea-9c35-3d3633bdc9e7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant files to understand the current state before making any changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "3b60d981-c518-496a-9acb-416459735d41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GD4JGvZiqA3k2DNJeGXMxS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12028
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

### Assistant

_source line 4_

先读取 results.tex 和 appendix.tex 的当前内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "4ed9c39c-f2cc-4f59-8b4a-9dfdbe8eeb2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GD4JGvZiqA3k2DNJeGXMxS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12028
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

### Runtime record

_source line 5_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779865200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "dc1092d7-4a67-42ca-aae9-54383ffb8d03",
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc"
}
```

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_011teqiyNWvFEbRr3xzySLzF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "1842b6ac-1212-4208-bf9d-5f2ae5a02653",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GD4JGvZiqA3k2DNJeGXMxS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12028
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

_source line 7 · 2026-05-27T04:29:58.068Z_

<details><summary>↩ Tool result · `toolu_011teqiyNWvFEbRr3xzySLzF`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Main Results}
6	
7	Table~\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\times$ 10 tasks per seed). $\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\star$) uses v1 code but is included above the midrule as a factorial control; its $\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.
8	
9	\textbf{Interaction pattern between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) show a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type; whether normalization modulates the magnitude requires additional LN seeds to confirm (Section~\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\Delta{=}-2.0$\,pp vs.\ Vanilla, $-$4.2\,pp vs.\ Detach OCC within the BN factorial row) and the most unstable ($\sigma{=}0.064$, more than $2.5{\times}$ that of other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\Delta{=}-0.5$\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767, $\Delta{=}+2.2$\,pp) and Detach+LN (0.765, $\Delta{=}+2.0$\,pp) both match or slightly exceed the Vanilla baseline (0.745). These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).
10	
11	\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\sigma{=}0.064$, more than $2.5{\times}$ that of other cells): individual seeds range from 0.776 (near Vanilla) to 0.654 ($\Delta{=}-9.1$\,pp), indicating a volatile optimization landscape under the BN + gradient flow combination.
12	
13	
14	\begin{table}[t]
15	\centering
16	\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\pm$ SD across seeds; 95\% CIs via bootstrap. $^\dagger$1 seed; $^\ddagger$2 seeds; $^\star$v1 code. Factorial conditions (above midrule) use v2 code unless marked $^\star$; supplementary conditions (below midrule) use v1 code.}
17	\label{tab:main_results}
18	\small
19	\setlength{\tabcolsep}{4pt}
20	\begin{tabular}{lccccc}
21	\toprule
22	Condition & Seeds & TSR & CAR & $95\%$ CI & $\Delta$CAR \\
23	\midrule
24	Vanilla       & 3 & 0.878 $\pm$ 0.032 & \textbf{0.745} $\pm$ 0.024 & --- & ---    \\
25	Detach OCC (BN)    & 4 & 0.908 $\pm$ 0.026 & 0.767 $\pm$ 0.024 & [0.744, 0.794] & $+$2.2 \\
26	Detach+LN$^\star$     & 3 & 0.901 $\pm$ 0.016 & 0.765 $\pm$ 0.023 & [0.748, 0.792] & --- \\
27	\addlinespace[3pt]
28	Random OCC (BN)$^\star$    & 3 & 0.869 $\pm$ 0.029 & 0.789 $\pm$ 0.031 & [0.754, 0.814] & --- \\
29	Full OCC+LN$^\dagger$   & 1 & 0.842 & 0.740 & --- & $-$0.5 \\
30	Full OCC (BN) & 3 & 0.854 $\pm$ 0.052 & 0.725 $\pm$ 0.064 & [0.654, 0.776] & $-$2.0 \\
31	\midrule
32	Depth             & 4 & 0.889 $\pm$ 0.042 & 0.780 $\pm$ 0.039 & [0.747, 0.812] & 0.0 \\
33	Cutoff@15K$^\ddagger$   & 2 & 0.883 $\pm$ 0.041 & 0.782 $\pm$ 0.031 & --- & $+$0.2 \\
34	Cutoff@25K$^\ddagger$   & 2 & 0.887 $\pm$ 0.061 & 0.724 $\pm$ 0.051 & --- & $-$5.6 \\
35	Cutoff@35K        & 3 & 0.933 $\pm$ 0.032 & 0.779 $\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\
36	Cutoff@45K$^\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\
37	Reverse Cutoff$^\ddagger$ & 2 & 0.839 $\pm$ 0.072 & 0.718 $\pm$ 0.025 & --- & $-$6.2 \\
38	\bottomrule
39	\end{tabular}
40	\end{table}
41	
42	\subsection{Normalization--Gradient Flow Interaction}
43	\label{sec:mechanism}
44	
45	The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\times}2$ factorial (Table~\ref{tab:factorial}, Figure~\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\,pp (Full OCC 0.725 vs.\ Detach OCC 0.767; Hedges' $g{=}-0.781$, bootstrap 95\% CI $[-0.108, 0.014]$, crossing zero and thus not individually significant at $\alpha{=}0.05$ given the small sample). The LN cells show the same directional pattern ($-$2.5\,pp), yielding a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type, with the BN cell showing a larger deficit ($-$4.2\,pp vs.\ $-$2.5\,pp under LN) in current data, though Full OCC+LN has $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\star$). We report effect sizes and confidence intervals for transparency; the small-$n$ factorial design prioritizes breadth across a 12-condition space over statistical power for individual pairwise tests. The consistent gradient flow effect---both BN and LN rows show lower CAR under gradient flow ON than OFF---provides the primary evidence for the ordinal interaction pattern.
46	
47	\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON without crossing (Figure~\ref{fig:factorial}), confirming an ordinal pattern. The BN cell shows a larger deficit ($-$4.2\,pp vs.\ $-$2.5\,pp under LN) in current data, though Full OCC+LN has only $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\star$); whether normalization type modulates the gradient flow effect requires additional seeds to confirm.
48	
49	\begin{table}[t]
50	\centering
51	\caption{$2{\times}2$ factorial: normalization type $\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data ($n{=}1$ for LN cells).}
52	\label{tab:factorial}
53	\begin{tabular}{lccc}
54	\toprule
55	 & Gradient ON & Gradient OFF & $\Delta$(ON$-$OFF) \\
56	\midrule
57	BatchNorm    & Full OCC (0.725) & Detach OCC (\textbf{0.767}) & $-$4.2 \\
58	LayerNorm    & Full OCC+LN (0.740) & Detach+LN (0.765) & $-$2.5 \\
59	\midrule
60	$\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	\begin{figure}[t]
66	\centering
67	\includegraphics[width=0.65\textwidth]{figures/factorial_2x2.pdf}
68	\caption{$2{\times}2$ factorial interaction: normalization type (BN/LN) $\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\,pp) and LN ($-$2.5\,pp), consistent with an ordinal interaction pattern. The BN cell shows a larger deficit; LN cells have $n{=}1$. Error bars: cross-seed SD.}
69	\label{fig:factorial}
70	\end{figure}
71	
72	\subsection{Gradient Dynamics}
73	
74	Gradient analysis (Figure~\ref{fig:gradient_analysis}, Appendix) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).
75	
76	\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC, with conflict rates of ${\sim}$50\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions, ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content does not affect outcomes.
77	
78	\textbf{Mechanism remains open.} The observed interaction pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. CKA analysis~\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\geq$ 0.95 for both DINOv2 and SigLIP), localizing the safety degradation to optimization dynamics rather than representational corruption.
79	
80	Additional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\ref{app:additional}.
81	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "8a62d92c-b347-4cc1-9fa4-eaa6f42c9bdb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.\n\n\\textbf{Interaction pattern between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) show a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type; whether normalization modulates the magnitude requires additional LN seeds to confirm (Section~\\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\\Delta{=}-2.0$\\,pp vs.\\ Vanilla, $-$4.2\\,pp vs.\\ Detach OCC within the BN factorial row) and the most unstable ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\\Delta{=}-0.5$\\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) and Detach+LN (0.765, $\\Delta{=}+2.0$\\,pp) both match or slightly exceed the Vanilla baseline (0.745). These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).\n\n\\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells): individual seeds range from 0.776 (near Vanilla) to 0.654 ($\\Delta{=}-9.1$\\,pp), indicating a volatile optimization landscape under the BN + gradient flow combination.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds; $^\\star$v1 code. Factorial conditions (above midrule) use v2 code unless marked $^\\star$; supplementary conditions (below midrule) use v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nVanilla       & 3 & 0.878 $\\pm$ 0.032 & \\textbf{0.745} $\\pm$ 0.024 & --- & ---    \\\\\nDetach OCC (BN)    & 4 & 0.908 $\\pm$ 0.026 & 0.767 $\\pm$ 0.024 & [0.744, 0.794] & $+$2.2 \\\\\nDetach+LN$^\\star$     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & --- \\\\\n\\addlinespace[3pt]\nRandom OCC (BN)$^\\star$    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & --- \\\\\nFull OCC+LN$^\\dagger$   & 1 & 0.842 & 0.740 & --- & $-$0.5 \\\\\nFull OCC (BN) & 3 & 0.854 $\\pm$ 0.052 & 0.725 $\\pm$ 0.064 & [0.654, 0.776] & $-$2.0 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\\nCutoff@15K$^\\ddagger$   & 2 & 0.883 $\\pm$ 0.041 & 0.782 $\\pm$ 0.031 & --- & $+$0.2 \\\\\nCutoff@25K$^\\ddagger$   & 2 & 0.887 $\\pm$ 0.061 & 0.724 $\\pm$ 0.051 & --- & $-$5.6 \\\\\nCutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\\nCutoff@45K$^\\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\\\\nReverse Cutoff$^\\ddagger$ & 2 & 0.839 $\\pm$ 0.072 & 0.718 $\\pm$ 0.025 & --- & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Normalization--Gradient Flow Interaction}\n\\label{sec:mechanism}\n\nThe four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach OCC 0.767; Hedges' $g{=}-0.781$, bootstrap 95\\% CI $[-0.108, 0.014]$, crossing zero and thus not individually significant at $\\alpha{=}0.05$ given the small sample). The LN cells show the same directional pattern ($-$2.5\\,pp), yielding a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type, with the BN cell showing a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$). We report effect sizes and confidence intervals for transparency; the small-$n$ factorial design prioritizes breadth across a 12-condition space over statistical power for individual pairwise tests. The consistent gradient flow effect---both BN and LN rows show lower CAR under gradient flow ON than OFF---provides the primary evidence for the ordinal interaction pattern.\n\n\\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON without crossing (Figure~\\ref{fig:factorial}), confirming an ordinal pattern. The BN cell shows a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has only $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$); whether normalization type modulates the gradient flow effect requires additional seeds to confirm.\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data ($n{=}1$ for LN cells).}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (\\textbf{0.767}) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.740) & Detach+LN (0.765) & $-$2.5 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\\,pp) and LN ($-$2.5\\,pp), consistent with an ordinal interaction pattern. The BN cell shows a larger deficit; LN cells have $n{=}1$. Error bars: cross-seed SD.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:gradient_analysis}, Appendix) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC, with conflict rates of ${\\sim}$50\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions, ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content does not affect outcomes.\n\n\\textbf{Mechanism remains open.} The observed interaction pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. CKA analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP), localizing the safety degradation to optimization dynamics rather than representational corruption.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
      "numLines": 81,
      "startLine": 1,
      "totalLines": 81
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_012E5cUs4RG4ZELt63mwohaG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "72eea9ab-58cd-4421-a8d1-2026a5f27554",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GD4JGvZiqA3k2DNJeGXMxS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12028
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

_source line 9 · 2026-05-27T04:29:58.514Z_

<details><summary>↩ Tool result · `toolu_012E5cUs4RG4ZELt63mwohaG`</summary>

```text
1	
2	\section{Extended Per-Task Results}
3	\label{app:per_task}
4	
5	Table~\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.
6	
7	\begin{table}[h]
8	\centering
9	\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}
10	\label{tab:per_task}
11	\begin{tabular}{clccccccc}
12	\toprule
13	 & & \multicolumn{7}{c}{Mean CAR by Condition} \\
14	\cmidrule(lr){3-9}
15	Task & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\
16	\midrule
17	T0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\
18	T1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\
19	T2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\
20	T3 & Hard  & 0.38 & 0.37 & 0.31 & \textbf{0.11} & 0.44 & 0.50 & 0.55 \\
21	T4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\
22	T5 & Hard  & 0.07 & 0.17 & 0.23 & \textbf{0.05} & 0.12 & 0.08 & 0.04 \\
23	T6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\
24	T7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\
25	T8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\
26	T9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\
27	\midrule
28	\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.
34	
35	\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.
36	
37	\section{Training Details}
38	\label{app:training}
39	
40	\begin{table}[h]
41	\centering
42	\caption{Training hyperparameters.}
43	\begin{tabular}{ll}
44	\toprule
45	Parameter & Value \\
46	\midrule
47	Base model & OpenVLA-7B~\cite{kim2024openvla} \\
48	Fine-tuning recipe & OFT~\cite{kim2025oft} \\
49	Vision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\
50	Patch token dim. & 2176 (concatenated) \\
51	LoRA rank / $\alpha$ & 32 / 16 \\
52	Batch size & 8 \\
53	Learning rate & $5 \times 10^{-4}$ (constant) \\
54	Training steps & 50{,}000 \\
55	Aux.\ loss weight $\lambda_0$ & 0.01 \\
56	Aux.\ loss decay & $\exp(-t / 50{,}000)$ \\
57	BEV grid resolution & $64 \times 64$ \\
58	Focal loss $\alpha$ / $\gamma$ & 0.25 / 2.0 \\
59	Depth loss & Smooth-L1 \\
60	Aux.\ head parameters & 1.2M \\
61	Hardware & NVIDIA RTX PRO 6000 (98\,GB) \\
62	Wall time per run & $\sim$12.9 hours \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \texttt{body\_xpos} exceeds $10^{-3}$. Bootstrap 95\% CIs are computed via 10{,}000 resamples (percentile method).
68	
69	\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed paired $t$-tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency. Under the v1 codebase, Detach OCC shows negligible difference from Vanilla ($d \approx -0.04$, $p = 0.91$); under v2 (Table~\ref{tab:main_results}), the effect reverses in sign ($\Delta{=}+2.2$\,pp, $p = 0.28$) but remains statistically indistinguishable from Vanilla, confirming that gradient-detached auxiliary supervision does not harm collision avoidance regardless of codebase version. Under v1, all gradient-flow conditions also show $p > 0.35$.
70	
71	\textbf{CKA analysis.} Centered Kernel Alignment~\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.
72	
73	\textbf{Cutoff implementation.} As described in Section~\ref{sec:ablation}, setting $\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).
74	
75	\section{Extended Analysis}
76	
77	\begin{figure}[h]
78	\centering
79	\includegraphics[width=\textwidth]{figures/gradient_analysis_combined.pdf}
80	\caption{Gradient dynamics during VLA fine-tuning (preliminary analysis using v1 codebase checkpoint; seed 42, 200 batches at 50K checkpoint). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach shows substantially reduced norms. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, confirming orthogonality). (d)~Gradient norm ratio (Detach / Vanilla) per layer. V2 validation is ongoing; directional conclusions should be interpreted with caution.}
81	\label{fig:gradient_analysis}
82	\end{figure}
83	
84	The Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \texttt{stop\_gradient}. Results (3 seeds) are reported in Table~\ref{tab:main_results} and analyzed in Section~\ref{sec:why_gradient}. Detach+LN (CAR 0.765) approaches the Vanilla baseline, consistent with the interaction pattern: removing gradient flow mitigates safety degradation regardless of normalization choice. The interaction pattern (Section~\ref{sec:mechanism}) indicates that gradient flow is associated with lower safety under both BN and LN, with BN amplifying the deficit.
85	
86	\textbf{Per-layer gradient analysis.} Figure~\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints; preliminary v2 analysis suggests the Detach gradient reduction may not reproduce at the same magnitude, and validation with the current codebase is pending. The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 50\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 44.1\%, Random OCC 43.9\%) fall below the 50\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.
87	
88	\begin{figure}[h]
89	\centering
90	\includegraphics[width=\textwidth]{figures/per_layer_combined.pdf}
91	\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches; v2 validation pending). \textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers. \textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\sim$50\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, which confirms architectural rather than label-dependent structure. Directional analysis (c--d) is confirmed in v2; amplitude analysis (a--b) is pending v2 validation.}
92	\label{fig:per_layer_combined}
93	\end{figure}
94	
95	\label{app:temporal}
96	\textbf{Dose-response: gradient flow duration vs.\ CAR (v1 data).} Figure~\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.
97	
98	\begin{figure}[h]
99	\centering
100	\includegraphics[width=0.75\textwidth]{figures/dose_response.pdf}
101	\caption{Dose-response: CAR vs.\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\leq$2 seeds (counts annotated as $n$). Diamond ($\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\pm\,$1\,SE. The ``+0.2\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}
102	\label{fig:dose_response}
103	\end{figure}
104	
105	\section{Additional Observations}
106	\label{app:additional}
107	
108	\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\ref{app:per_task}). Detach shows the lowest CAR on these hard tasks in v1 data (T3: 0.11, T5: 0.05). This v1 pattern does not replicate under the controlled v2 factorial design (Table~\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.
109	
110	\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.
111	
112	\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\Delta = -$0.1\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\ref{app:temporal}.
113	
114	\section{Codebase Sensitivity (v1 vs.\ v2)}
115	\label{app:codebase}
116	
117	The five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.
118	
119	\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\ref{tab:per_task}); under v2, the same condition yields 0.725 $\pm$ 0.064 (Table~\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\,pp, while Vanilla remains stable across codebases ($<$1.5\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.
120	
121	\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\sim$4\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\sim$44\% (v1) to $\sim$50\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.
122	
123	\textbf{Interaction pattern shift.} Under v1, the normalization $\times$ gradient flow interaction appeared as a crossover pattern ($p{=}0.025$); under v2, the pattern is ordinal (both lines slope downward without crossing). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.
124	
125	\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.
126	
127	\section{Statistical Power Analysis}
128	\label{app:stat_power}
129	
130	The $2{\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. For the BN row, the observed effect size is large (Hedges' $g{=}-0.781$), but with $n{=}3$ vs.\ $n{=}4$ seeds per cell, post-hoc power is approximately 0.3--0.4~\cite{cohen1988statistical}, meaning there is a 60--70\% probability of failing to detect a true effect of this magnitude at $\alpha{=}0.05$. We report this limitation transparently.
131	
132	However, the study's evidential strength does not rest on any single pairwise comparison. The consistent gradient flow effect---both BN and LN rows show lower CAR under gradient flow ON than OFF---provides the primary evidence for the ordinal interaction pattern, complemented by the large observed effect size (Hedges' $g{=}-0.781$) in the fully powered BN row. Seed expansion ($n{=}5$ per factorial cell) is underway to increase per-cell power.
133	
134	\section{Limitations}
135	\label{app:limitations}
136	
137	Our study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation (SafeLIBERO Level~I, 10 tasks); real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The interaction pattern is based on $n{=}1$--$4$ seeds per cell; larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations.
138	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "d0ea8594-1ff2-41de-95be-ed982d19e052",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
      "content": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (98\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed paired $t$-tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency. Under the v1 codebase, Detach OCC shows negligible difference from Vanilla ($d \\approx -0.04$, $p = 0.91$); under v2 (Table~\\ref{tab:main_results}), the effect reverses in sign ($\\Delta{=}+2.2$\\,pp, $p = 0.28$) but remains statistically indistinguishable from Vanilla, confirming that gradient-detached auxiliary supervision does not harm collision avoidance regardless of codebase version. Under v1, all gradient-flow conditions also show $p > 0.35$.\n\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (preliminary analysis using v1 codebase checkpoint; seed 42, 200 batches at 50K checkpoint). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach shows substantially reduced norms. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, confirming orthogonality). (d)~Gradient norm ratio (Detach / Vanilla) per layer. V2 validation is ongoing; directional conclusions should be interpreted with caution.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Results (3 seeds) are reported in Table~\\ref{tab:main_results} and analyzed in Section~\\ref{sec:why_gradient}. Detach+LN (CAR 0.765) approaches the Vanilla baseline, consistent with the interaction pattern: removing gradient flow mitigates safety degradation regardless of normalization choice. The interaction pattern (Section~\\ref{sec:mechanism}) indicates that gradient flow is associated with lower safety under both BN and LN, with BN amplifying the deficit.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints; preliminary v2 analysis suggests the Detach gradient reduction may not reproduce at the same magnitude, and validation with the current codebase is pending. The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 50\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 44.1\\%, Random OCC 43.9\\%) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches; v2 validation pending). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers. \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$50\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, which confirms architectural rather than label-dependent structure. Directional analysis (c--d) is confirmed in v2; amplitude analysis (a--b) is pending v2 validation.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Detach shows the lowest CAR on these hard tasks in v1 data (T3: 0.11, T5: 0.05). This v1 pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$50\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Interaction pattern shift.} Under v1, the normalization $\\times$ gradient flow interaction appeared as a crossover pattern ($p{=}0.025$); under v2, the pattern is ordinal (both lines slope downward without crossing). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. For the BN row, the observed effect size is large (Hedges' $g{=}-0.781$), but with $n{=}3$ vs.\\ $n{=}4$ seeds per cell, post-hoc power is approximately 0.3--0.4~\\cite{cohen1988statistical}, meaning there is a 60--70\\% probability of failing to detect a true effect of this magnitude at $\\alpha{=}0.05$. We report this limitation transparently.\n\nHowever, the study's evidential strength does not rest on any single pairwise comparison. The consistent gradient flow effect---both BN and LN rows show lower CAR under gradient flow ON than OFF---provides the primary evidence for the ordinal interaction pattern, complemented by the large observed effect size (Hedges' $g{=}-0.781$) in the fully powered BN row. Seed expansion ($n{=}5$ per factorial cell) is underway to increase per-cell power.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation (SafeLIBERO Level~I, 10 tasks); real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The interaction pattern is based on $n{=}1$--$4$ seeds per cell; larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations.\n",
      "numLines": 138,
      "startLine": 1,
      "totalLines": 138
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

````text
Now let me analyze the current state and what needs to be changed:

### 1. Table 1 (results.tex): Detach+LN row
Current (line 26):
```
Detach+LN$^\star$     & 3 & 0.901 $\pm$ 0.016 & 0.765 $\pm$ 0.023 & [0.748, 0.792] & --- \\
```
- Already has `$^\star$` mark ✓
- ΔCAR is already `---` ✓
- This item is already done!


- The caption already includes the footnote explaining that `$^\star$` denotes v1 code, and the Detach+LN row is properly marked with this symbol to indicate it uses v1 code while other factorial conditions use v2 code.

Now I need to check the body text where Detach+LN is referenced to make sure those citations are consistent with the table footnote. I see the issue now—the delta value for Detach+LN in line 9 is marked as a cross-codebase comparison when it should only reflect within-version changes. Lines 45 and 47 are already properly annotated with the version markers, so the main fix needed is clarifying that Detach+LN's +2.0pp delta is comparing v1 cells only, not mixing v1 and v2 data. Looking at the next section, I need to mark Detach+LN with a star in Table 2 since it's v1 data. The figure caption also needs attention—it's currently cut off mid-sentence, so I should complete it based on what comes next about the factorial interaction showing downward slopes for both normalization and gradient flow conditions. I'm looking at the statistical results comparing v1 and v2 codebases for the Detach OCC condition. The v1 results show negligible differences from Vanilla with a small effect size and high p-value, while v2 shows a reversal in the effect direction but still remains statistically insignificant. This entire paragraph documenting v1 statistics needs to be removed since it contradicts the main v2 findings and isn't part of the final narrative. I need to figure out exactly what the task is asking me to delete. The instruction says to remove the entire paragraph containing v1 statistics, but I'm uncertain whether that means just the v1-specific sentences or the whole Statistical tests section since it mixes both v1 and v2 information. Let me parse this more carefully — the v1 stats are the two sentences about Detach OCC showing negligible difference and the gradient-flow conditions, so maybe I should remove only those specific sentences rather than the entire paragraph. the whole paragraph. Actually, the paragraph starts with \textbf{Statistical tests.} and this is a whole paragraph. Looking at the context, I need to delete the entire section that describes the statistical methodology and v1/v2 comparisons, even though it contains important details about how the tests were conducted. The instruction is clear—remove the whole thing.

Wait, let me reconsider. The task asks me to delete paragraphs reporting v1 statistics that contradict the main v2 results, but the methodology section is foundational. I should preserve the explanation of how the statistical tests work and only remove the specific v1 results that conflict with the main findings. That way I keep the methodological transparency while eliminating the contradictory data.

Now I'm mapping out all the edits needed: updating Table 1 to mark v1 results with a footnote and use dashes for pending v2 data, removing the conflicting v1 statistics from the body text, adding the same footnote to Table 2, and adjusting figure captions to reflect these changes.

Let me start making these revisions. First, I'll expand the table caption to clarify that v1 code was used but v2 multi-seed results are still pending. Then I'll remove Detach+LN's performance delta from the main text since it's marked as incomplete, and add the footnote marker to Table 2 as well. Now I need to remove the v1 codebase statistics from the Statistical tests section in the appendix, specifically deleting everything from "Under the v1 codebase..." through the end of that paragraph.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "31fa92ff-2a01-4dea-9aa8-fd58e015f2f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcqdzXrfV2Don86xQaUJg2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8831,
      "cache_read_input_tokens": 23869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8831
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

_source line 11_

Table 1 的 Detach+LN 行已经有 `$^\star$` 和 `---`，不需要改。开始其他修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "026b0090-76e4-41dc-8960-3730d5121902",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcqdzXrfV2Don86xQaUJg2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8831,
      "cache_read_input_tokens": 23869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8831
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

_source line 12_

<details open><summary>🔧 Tool call — Edit · `toolu_017v6fDPUfRs7NZdWdXKZ8u8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "$^\\star$v1 code.",
  "new_string": "$^\\star$Trained with v1 code; v2 multi-seed results pending."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "9c9291eb-1b98-4a88-85de-8bf18aa07777",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcqdzXrfV2Don86xQaUJg2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8831,
      "cache_read_input_tokens": 23869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8831
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

_source line 13 · 2026-05-27T04:31:02.624Z_

<details><summary>↩ Tool result · `toolu_017v6fDPUfRs7NZdWdXKZ8u8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "5a817c9b-b7fb-4764-8408-c75bab7ab7a9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "$^\\star$v1 code.",
    "newString": "$^\\star$Trained with v1 code; v2 multi-seed results pending.",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.\n\n\\textbf{Interaction pattern between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) show a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type; whether normalization modulates the magnitude requires additional LN seeds to confirm (Section~\\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\\Delta{=}-2.0$\\,pp vs.\\ Vanilla, $-$4.2\\,pp vs.\\ Detach OCC within the BN factorial row) and the most unstable ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\\Delta{=}-0.5$\\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) and Detach+LN (0.765, $\\Delta{=}+2.0$\\,pp) both match or slightly exceed the Vanilla baseline (0.745). These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).\n\n\\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells): individual seeds range from 0.776 (near Vanilla) to 0.654 ($\\Delta{=}-9.1$\\,pp), indicating a volatile optimization landscape under the BN + gradient flow combination.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds; $^\\star$v1 code. Factorial conditions (above midrule) use v2 code unless marked $^\\star$; supplementary conditions (below midrule) use v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nVanilla       & 3 & 0.878 $\\pm$ 0.032 & \\textbf{0.745} $\\pm$ 0.024 & --- & ---    \\\\\nDetach OCC (BN)    & 4 & 0.908 $\\pm$ 0.026 & 0.767 $\\pm$ 0.024 & [0.744, 0.794] & $+$2.2 \\\\\nDetach+LN$^\\star$     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & --- \\\\\n\\addlinespace[3pt]\nRandom OCC (BN)$^\\star$    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & --- \\\\\nFull OCC+LN$^\\dagger$   & 1 & 0.842 & 0.740 & --- & $-$0.5 \\\\\nFull OCC (BN) & 3 & 0.854 $\\pm$ 0.052 & 0.725 $\\pm$ 0.064 & [0.654, 0.776] & $-$2.0 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\\nCutoff@15K$^\\ddagger$   & 2 & 0.883 $\\pm$ 0.041 & 0.782 $\\pm$ 0.031 & --- & $+$0.2 \\\\\nCutoff@25K$^\\ddagger$   & 2 & 0.887 $\\pm$ 0.061 & 0.724 $\\pm$ 0.051 & --- & $-$5.6 \\\\\nCutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\\nCutoff@45K$^\\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\\\\nReverse Cutoff$^\\ddagger$ & 2 & 0.839 $\\pm$ 0.072 & 0.718 $\\pm$ 0.025 & --- & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Normalization--Gradient Flow Interaction}\n\\label{sec:mechanism}\n\nThe four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach OCC 0.767; Hedges' $g{=}-0.781$, bootstrap 95\\% CI $[-0.108, 0.014]$, crossing zero and thus not individually significant at $\\alpha{=}0.05$ given the small sample). The LN cells show the same directional pattern ($-$2.5\\,pp), yielding a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type, with the BN cell showing a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$). We report effect sizes and confidence intervals for transparency; the small-$n$ factorial design prioritizes breadth across a 12-condition space over statistical power for individual pairwise tests. The consistent gradient flow effect---both BN and LN rows show lower CAR under gradient flow ON than OFF---provides the primary evidence for the ordinal interaction pattern.\n\n\\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON without crossing (Figure~\\ref{fig:factorial}), confirming an ordinal pattern. The BN cell shows a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has only $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$); whether normalization type modulates the gradient flow effect requires additional seeds to confirm.\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data ($n{=}1$ for LN cells).}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (\\textbf{0.767}) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.740) & Detach+LN (0.765) & $-$2.5 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\\,pp) and LN ($-$2.5\\,pp), consistent with an ordinal interaction pattern. The BN cell shows a larger deficit; LN cells have $n{=}1$. Error bars: cross-seed SD.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:gradient_analysis}, Appendix) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC, with conflict rates of ${\\sim}$50\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions, ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content does not affect outcomes.\n\n\\textbf{Mechanism remains open.} The observed interaction pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. CKA analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP), localizing the safety degradation to optimization dynamics rather than representational corruption.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 7,
        "newStart": 13,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{table}[t]",
          " \\centering",
          "-\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds; $^\\star$v1 code. Factorial conditions (above midrule) use v2 code unless marked $^\\star$; supplementary conditions (below midrule) use v1 code.}",
          "+\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds; $^\\star$Trained with v1 code; v2 multi-seed results pending. Factorial conditions (above midrule) use v2 code unless marked $^\\star$; supplementary conditions (below midrule) use v1 code.}",
          " \\label{tab:main_results}",
          " \\small",
          " \\setlength{\\tabcolsep}{4pt}"
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

_source line 14_

<details open><summary>🔧 Tool call — Edit · `toolu_01ThNMLXhMEdYzfE5e8QsXMv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) and Detach+LN (0.765, $\\Delta{=}+2.0$\\,pp) both match or slightly exceed the Vanilla baseline (0.745).",
  "new_string": "Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) matches or slightly exceeds the Vanilla baseline (0.745); Detach+LN$^\\star$ (0.765) shows a comparable level under v1 code."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "6a42f739-090b-4c5e-8442-b2b0794710db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HXSfYrLYEipsLYsnyv8jQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3860,
      "cache_read_input_tokens": 32700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3860
      },
      "output_tokens": 64,
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

_source line 15 · 2026-05-27T04:31:07.668Z_

<details><summary>↩ Tool result · `toolu_01ThNMLXhMEdYzfE5e8QsXMv`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "a9a1dddf-1483-4f85-81ed-3cca51f10ec2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) and Detach+LN (0.765, $\\Delta{=}+2.0$\\,pp) both match or slightly exceed the Vanilla baseline (0.745).",
    "newString": "Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) matches or slightly exceeds the Vanilla baseline (0.745); Detach+LN$^\\star$ (0.765) shows a comparable level under v1 code.",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.\n\n\\textbf{Interaction pattern between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) show a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type; whether normalization modulates the magnitude requires additional LN seeds to confirm (Section~\\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\\Delta{=}-2.0$\\,pp vs.\\ Vanilla, $-$4.2\\,pp vs.\\ Detach OCC within the BN factorial row) and the most unstable ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\\Delta{=}-0.5$\\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) and Detach+LN (0.765, $\\Delta{=}+2.0$\\,pp) both match or slightly exceed the Vanilla baseline (0.745). These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).\n\n\\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells): individual seeds range from 0.776 (near Vanilla) to 0.654 ($\\Delta{=}-9.1$\\,pp), indicating a volatile optimization landscape under the BN + gradient flow combination.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds; $^\\star$Trained with v1 code; v2 multi-seed results pending. Factorial conditions (above midrule) use v2 code unless marked $^\\star$; supplementary conditions (below midrule) use v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nVanilla       & 3 & 0.878 $\\pm$ 0.032 & \\textbf{0.745} $\\pm$ 0.024 & --- & ---    \\\\\nDetach OCC (BN)    & 4 & 0.908 $\\pm$ 0.026 & 0.767 $\\pm$ 0.024 & [0.744, 0.794] & $+$2.2 \\\\\nDetach+LN$^\\star$     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & --- \\\\\n\\addlinespace[3pt]\nRandom OCC (BN)$^\\star$    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & --- \\\\\nFull OCC+LN$^\\dagger$   & 1 & 0.842 & 0.740 & --- & $-$0.5 \\\\\nFull OCC (BN) & 3 & 0.854 $\\pm$ 0.052 & 0.725 $\\pm$ 0.064 & [0.654, 0.776] & $-$2.0 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\\nCutoff@15K$^\\ddagger$   & 2 & 0.883 $\\pm$ 0.041 & 0.782 $\\pm$ 0.031 & --- & $+$0.2 \\\\\nCutoff@25K$^\\ddagger$   & 2 & 0.887 $\\pm$ 0.061 & 0.724 $\\pm$ 0.051 & --- & $-$5.6 \\\\\nCutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\\nCutoff@45K$^\\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\\\\nReverse Cutoff$^\\ddagger$ & 2 & 0.839 $\\pm$ 0.072 & 0.718 $\\pm$ 0.025 & --- & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Normalization--Gradient Flow Interaction}\n\\label{sec:mechanism}\n\nThe four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach OCC 0.767; Hedges' $g{=}-0.781$, bootstrap 95\\% CI $[-0.108, 0.014]$, crossing zero and thus not individually significant at $\\alpha{=}0.05$ given the small sample). The LN cells show the same directional pattern ($-$2.5\\,pp), yielding a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type, with the BN cell showing a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$). We report effect sizes and confidence intervals for transparency; the small-$n$ factorial design prioritizes breadth across a 12-condition space over statistical power for individual pairwise tests. The consistent gradient flow effect---both BN and LN rows show lower CAR under gradient flow ON than OFF---provides the primary evidence for the ordinal interaction pattern.\n\n\\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON without crossing (Figure~\\ref{fig:factorial}), confirming an ordinal pattern. The BN cell shows a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has only $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$); whether normalization type modulates the gradient flow effect requires additional seeds to confirm.\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data ($n{=}1$ for LN cells).}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (\\textbf{0.767}) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.740) & Detach+LN (0.765) & $-$2.5 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\\,pp) and LN ($-$2.5\\,pp), consistent with an ordinal interaction pattern. The BN cell shows a larger deficit; LN cells have $n{=}1$. Error bars: cross-seed SD.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:gradient_analysis}, Appendix) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC, with conflict rates of ${\\sim}$50\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions, ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content does not affect outcomes.\n\n\\textbf{Mechanism remains open.} The observed interaction pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. CKA analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP), localizing the safety degradation to optimization dynamics rather than representational corruption.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 7,
        "newStart": 6,
        "newLines": 7,
        "lines": [
          " ",
          " Table~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.",
          " ",
          "-\\textbf{Interaction pattern between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) show a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type; whether normalization modulates the magnitude requires additional LN seeds to confirm (Section~\\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\\Delta{=}-2.0$\\,pp vs.\\ Vanilla, $-$4.2\\,pp vs.\\ Detach OCC within the BN factorial row) and the most unstable ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\\Delta{=}-0.5$\\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) and Detach+LN (0.765, $\\Delta{=}+2.0$\\,pp) both match or slightly exceed the Vanilla baseline (0.745). These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).",
          "+\\textbf{Interaction pattern between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) show a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type; whether normalization modulates the magnitude requires additional LN seeds to confirm (Section~\\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\\Delta{=}-2.0$\\,pp vs.\\ Vanilla, $-$4.2\\,pp vs.\\ Detach OCC within the BN factorial row) and the most unstable ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\\Delta{=}-0.5$\\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) matches or slightly exceeds the Vanilla baseline (0.745); Detach+LN$^\\star$ (0.765) shows a comparable level under v1 code. These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).",
          " ",
          " \\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells): individual seeds range from 0.776 (near Vanilla) to 0.654 ($\\Delta{=}-9.1$\\,pp), indicating a volatile optimization landscape under the BN + gradient flow combination.",
          " "
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

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_01NfYqenKj7oz96S9ie7WR2o`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "LayerNorm    & Full OCC+LN (0.740) & Detach+LN (0.765) & $-$2.5 \\\\",
  "new_string": "LayerNorm    & Full OCC+LN (0.740) & Detach+LN$^\\star$ (0.765) & $-$2.5 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "031820ed-ddaa-4379-8dc2-a83847edd7e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ww7GoXZ661sYuGDdEdeZcu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 322,
      "cache_read_input_tokens": 36560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 322
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

_source line 17 · 2026-05-27T04:31:14.020Z_

<details><summary>↩ Tool result · `toolu_01NfYqenKj7oz96S9ie7WR2o`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "0c69d6c0-28bc-4ecf-a75f-347549d1ab03",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "LayerNorm    & Full OCC+LN (0.740) & Detach+LN (0.765) & $-$2.5 \\\\",
    "newString": "LayerNorm    & Full OCC+LN (0.740) & Detach+LN$^\\star$ (0.765) & $-$2.5 \\\\",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.\n\n\\textbf{Interaction pattern between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) show a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type; whether normalization modulates the magnitude requires additional LN seeds to confirm (Section~\\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\\Delta{=}-2.0$\\,pp vs.\\ Vanilla, $-$4.2\\,pp vs.\\ Detach OCC within the BN factorial row) and the most unstable ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\\Delta{=}-0.5$\\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) matches or slightly exceeds the Vanilla baseline (0.745); Detach+LN$^\\star$ (0.765) shows a comparable level under v1 code. These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).\n\n\\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells): individual seeds range from 0.776 (near Vanilla) to 0.654 ($\\Delta{=}-9.1$\\,pp), indicating a volatile optimization landscape under the BN + gradient flow combination.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds; $^\\star$Trained with v1 code; v2 multi-seed results pending. Factorial conditions (above midrule) use v2 code unless marked $^\\star$; supplementary conditions (below midrule) use v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nVanilla       & 3 & 0.878 $\\pm$ 0.032 & \\textbf{0.745} $\\pm$ 0.024 & --- & ---    \\\\\nDetach OCC (BN)    & 4 & 0.908 $\\pm$ 0.026 & 0.767 $\\pm$ 0.024 & [0.744, 0.794] & $+$2.2 \\\\\nDetach+LN$^\\star$     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & --- \\\\\n\\addlinespace[3pt]\nRandom OCC (BN)$^\\star$    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & --- \\\\\nFull OCC+LN$^\\dagger$   & 1 & 0.842 & 0.740 & --- & $-$0.5 \\\\\nFull OCC (BN) & 3 & 0.854 $\\pm$ 0.052 & 0.725 $\\pm$ 0.064 & [0.654, 0.776] & $-$2.0 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\\nCutoff@15K$^\\ddagger$   & 2 & 0.883 $\\pm$ 0.041 & 0.782 $\\pm$ 0.031 & --- & $+$0.2 \\\\\nCutoff@25K$^\\ddagger$   & 2 & 0.887 $\\pm$ 0.061 & 0.724 $\\pm$ 0.051 & --- & $-$5.6 \\\\\nCutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\\nCutoff@45K$^\\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\\\\nReverse Cutoff$^\\ddagger$ & 2 & 0.839 $\\pm$ 0.072 & 0.718 $\\pm$ 0.025 & --- & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Normalization--Gradient Flow Interaction}\n\\label{sec:mechanism}\n\nThe four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach OCC 0.767; Hedges' $g{=}-0.781$, bootstrap 95\\% CI $[-0.108, 0.014]$, crossing zero and thus not individually significant at $\\alpha{=}0.05$ given the small sample). The LN cells show the same directional pattern ($-$2.5\\,pp), yielding a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type, with the BN cell showing a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$). We report effect sizes and confidence intervals for transparency; the small-$n$ factorial design prioritizes breadth across a 12-condition space over statistical power for individual pairwise tests. The consistent gradient flow effect---both BN and LN rows show lower CAR under gradient flow ON than OFF---provides the primary evidence for the ordinal interaction pattern.\n\n\\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON without crossing (Figure~\\ref{fig:factorial}), confirming an ordinal pattern. The BN cell shows a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has only $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$); whether normalization type modulates the gradient flow effect requires additional seeds to confirm.\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data ($n{=}1$ for LN cells).}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (\\textbf{0.767}) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.740) & Detach+LN (0.765) & $-$2.5 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\\,pp) and LN ($-$2.5\\,pp), consistent with an ordinal interaction pattern. The BN cell shows a larger deficit; LN cells have $n{=}1$. Error bars: cross-seed SD.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:gradient_analysis}, Appendix) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC, with conflict rates of ${\\sim}$50\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions, ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content does not affect outcomes.\n\n\\textbf{Mechanism remains open.} The observed interaction pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. CKA analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP), localizing the safety degradation to optimization dynamics rather than representational corruption.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
    "structuredPatch": [
      {
        "oldStart": 55,
        "oldLines": 7,
        "newStart": 55,
        "newLines": 7,
        "lines": [
          "  & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\",
          " \\midrule",
          " BatchNorm    & Full OCC (0.725) & Detach OCC (\\textbf{0.767}) & $-$4.2 \\\\",
          "-LayerNorm    & Full OCC+LN (0.740) & Detach+LN (0.765) & $-$2.5 \\\\",
          "+LayerNorm    & Full OCC+LN (0.740) & Detach+LN$^\\star$ (0.765) & $-$2.5 \\\\",
          " \\midrule",
          " $\\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\\\",
          " \\bottomrule"
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

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01DkP4jhbwBTTCTvXYAogTAx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "LN cells have $n{=}1$. Error bars: cross-seed SD.}",
  "new_string": "Full OCC+LN has $n{=}1$ (v2); Detach+LN has $n{=}3$ (v1, marked $^\\star$). Error bars: cross-seed SD.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "6afcdd0c-92eb-4a47-8313-60eb7aba22c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JgYVWdveAtpwUkeSicAk5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 275,
      "cache_read_input_tokens": 36882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 275
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

_source line 19 · 2026-05-27T04:31:17.582Z_

<details><summary>↩ Tool result · `toolu_01DkP4jhbwBTTCTvXYAogTAx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "b2ab4ce9-f390-40bd-9b35-d2efbd4f3238",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "LN cells have $n{=}1$. Error bars: cross-seed SD.}",
    "newString": "Full OCC+LN has $n{=}1$ (v2); Detach+LN has $n{=}3$ (v1, marked $^\\star$). Error bars: cross-seed SD.}",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.\n\n\\textbf{Interaction pattern between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) show a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type; whether normalization modulates the magnitude requires additional LN seeds to confirm (Section~\\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\\Delta{=}-2.0$\\,pp vs.\\ Vanilla, $-$4.2\\,pp vs.\\ Detach OCC within the BN factorial row) and the most unstable ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\\Delta{=}-0.5$\\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) matches or slightly exceeds the Vanilla baseline (0.745); Detach+LN$^\\star$ (0.765) shows a comparable level under v1 code. These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).\n\n\\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells): individual seeds range from 0.776 (near Vanilla) to 0.654 ($\\Delta{=}-9.1$\\,pp), indicating a volatile optimization landscape under the BN + gradient flow combination.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds; $^\\star$Trained with v1 code; v2 multi-seed results pending. Factorial conditions (above midrule) use v2 code unless marked $^\\star$; supplementary conditions (below midrule) use v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nVanilla       & 3 & 0.878 $\\pm$ 0.032 & \\textbf{0.745} $\\pm$ 0.024 & --- & ---    \\\\\nDetach OCC (BN)    & 4 & 0.908 $\\pm$ 0.026 & 0.767 $\\pm$ 0.024 & [0.744, 0.794] & $+$2.2 \\\\\nDetach+LN$^\\star$     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & --- \\\\\n\\addlinespace[3pt]\nRandom OCC (BN)$^\\star$    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & --- \\\\\nFull OCC+LN$^\\dagger$   & 1 & 0.842 & 0.740 & --- & $-$0.5 \\\\\nFull OCC (BN) & 3 & 0.854 $\\pm$ 0.052 & 0.725 $\\pm$ 0.064 & [0.654, 0.776] & $-$2.0 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\\nCutoff@15K$^\\ddagger$   & 2 & 0.883 $\\pm$ 0.041 & 0.782 $\\pm$ 0.031 & --- & $+$0.2 \\\\\nCutoff@25K$^\\ddagger$   & 2 & 0.887 $\\pm$ 0.061 & 0.724 $\\pm$ 0.051 & --- & $-$5.6 \\\\\nCutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\\nCutoff@45K$^\\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\\\\nReverse Cutoff$^\\ddagger$ & 2 & 0.839 $\\pm$ 0.072 & 0.718 $\\pm$ 0.025 & --- & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Normalization--Gradient Flow Interaction}\n\\label{sec:mechanism}\n\nThe four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach OCC 0.767; Hedges' $g{=}-0.781$, bootstrap 95\\% CI $[-0.108, 0.014]$, crossing zero and thus not individually significant at $\\alpha{=}0.05$ given the small sample). The LN cells show the same directional pattern ($-$2.5\\,pp), yielding a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type, with the BN cell showing a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$). We report effect sizes and confidence intervals for transparency; the small-$n$ factorial design prioritizes breadth across a 12-condition space over statistical power for individual pairwise tests. The consistent gradient flow effect---both BN and LN rows show lower CAR under gradient flow ON than OFF---provides the primary evidence for the ordinal interaction pattern.\n\n\\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON without crossing (Figure~\\ref{fig:factorial}), confirming an ordinal pattern. The BN cell shows a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has only $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$); whether normalization type modulates the gradient flow effect requires additional seeds to confirm.\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data ($n{=}1$ for LN cells).}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (\\textbf{0.767}) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.740) & Detach+LN$^\\star$ (0.765) & $-$2.5 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\\,pp) and LN ($-$2.5\\,pp), consistent with an ordinal interaction pattern. The BN cell shows a larger deficit; LN cells have $n{=}1$. Error bars: cross-seed SD.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:gradient_analysis}, Appendix) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC, with conflict rates of ${\\sim}$50\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions, ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content does not affect outcomes.\n\n\\textbf{Mechanism remains open.} The observed interaction pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. CKA analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP), localizing the safety degradation to optimization dynamics rather than representational corruption.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
    "structuredPatch": [
      {
        "oldStart": 65,
        "oldLines": 7,
        "newStart": 65,
        "newLines": 7,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}",
          "-\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\\,pp) and LN ($-$2.5\\,pp), consistent with an ordinal interaction pattern. The BN cell shows a larger deficit; LN cells have $n{=}1$. Error bars: cross-seed SD.}",
          "+\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\\,pp) and LN ($-$2.5\\,pp), consistent with an ordinal interaction pattern. The BN cell shows a larger deficit; Full OCC+LN has $n{=}1$ (v2); Detach+LN has $n{=}3$ (v1, marked $^\\star$). Error bars: cross-seed SD.}",
          " \\label{fig:factorial}",
          " \\end{figure}",
          " "
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

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01KzqP3xjkV6dsn99Q8HgduX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": " Under the v1 codebase, Detach OCC shows negligible difference from Vanilla ($d \\approx -0.04$, $p = 0.91$); under v2 (Table~\\ref{tab:main_results}), the effect reverses in sign ($\\Delta{=}+2.2$\\,pp, $p = 0.28$) but remains statistically indistinguishable from Vanilla, confirming that gradient-detached auxiliary supervision does not harm collision avoidance regardless of codebase version. Under v1, all gradient-flow conditions also show $p > 0.35$.",
  "new_string": ""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "d03eaf94-6efc-4740-a5e2-f764bd38019b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KabxK8cNfScF3XxYAsu35",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 263,
      "cache_read_input_tokens": 37157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 263
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

_source line 21 · 2026-05-27T04:31:21.893Z_

<details><summary>↩ Tool result · `toolu_01KzqP3xjkV6dsn99Q8HgduX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "12082bde-421b-4f3a-b449-392cbbcfae02",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": " Under the v1 codebase, Detach OCC shows negligible difference from Vanilla ($d \\approx -0.04$, $p = 0.91$); under v2 (Table~\\ref{tab:main_results}), the effect reverses in sign ($\\Delta{=}+2.2$\\,pp, $p = 0.28$) but remains statistically indistinguishable from Vanilla, confirming that gradient-detached auxiliary supervision does not harm collision avoidance regardless of codebase version. Under v1, all gradient-flow conditions also show $p > 0.35$.",
    "newString": "",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (98\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed paired $t$-tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency. Under the v1 codebase, Detach OCC shows negligible difference from Vanilla ($d \\approx -0.04$, $p = 0.91$); under v2 (Table~\\ref{tab:main_results}), the effect reverses in sign ($\\Delta{=}+2.2$\\,pp, $p = 0.28$) but remains statistically indistinguishable from Vanilla, confirming that gradient-detached auxiliary supervision does not harm collision avoidance regardless of codebase version. Under v1, all gradient-flow conditions also show $p > 0.35$.\n\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (preliminary analysis using v1 codebase checkpoint; seed 42, 200 batches at 50K checkpoint). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach shows substantially reduced norms. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, confirming orthogonality). (d)~Gradient norm ratio (Detach / Vanilla) per layer. V2 validation is ongoing; directional conclusions should be interpreted with caution.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Results (3 seeds) are reported in Table~\\ref{tab:main_results} and analyzed in Section~\\ref{sec:why_gradient}. Detach+LN (CAR 0.765) approaches the Vanilla baseline, consistent with the interaction pattern: removing gradient flow mitigates safety degradation regardless of normalization choice. The interaction pattern (Section~\\ref{sec:mechanism}) indicates that gradient flow is associated with lower safety under both BN and LN, with BN amplifying the deficit.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints; preliminary v2 analysis suggests the Detach gradient reduction may not reproduce at the same magnitude, and validation with the current codebase is pending. The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 50\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 44.1\\%, Random OCC 43.9\\%) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches; v2 validation pending). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers. \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$50\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, which confirms architectural rather than label-dependent structure. Directional analysis (c--d) is confirmed in v2; amplitude analysis (a--b) is pending v2 validation.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Detach shows the lowest CAR on these hard tasks in v1 data (T3: 0.11, T5: 0.05). This v1 pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$50\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Interaction pattern shift.} Under v1, the normalization $\\times$ gradient flow interaction appeared as a crossover pattern ($p{=}0.025$); under v2, the pattern is ordinal (both lines slope downward without crossing). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. For the BN row, the observed effect size is large (Hedges' $g{=}-0.781$), but with $n{=}3$ vs.\\ $n{=}4$ seeds per cell, post-hoc power is approximately 0.3--0.4~\\cite{cohen1988statistical}, meaning there is a 60--70\\% probability of failing to detect a true effect of this magnitude at $\\alpha{=}0.05$. We report this limitation transparently.\n\nHowever, the study's evidential strength does not rest on any single pairwise comparison. The consistent gradient flow effect---both BN and LN rows show lower CAR under gradient flow ON than OFF---provides the primary evidence for the ordinal interaction pattern, complemented by the large observed effect size (Hedges' $g{=}-0.781$) in the fully powered BN row. Seed expansion ($n{=}5$ per factorial cell) is underway to increase per-cell power.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation (SafeLIBERO Level~I, 10 tasks); real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The interaction pattern is based on $n{=}1$--$4$ seeds per cell; larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations.\n",
    "structuredPatch": [
      {
        "oldStart": 66,
        "oldLines": 8,
        "newStart": 66,
        "newLines": 7,
        "lines": [
          " ",
          " \\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).",
          " ",
          "-\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed paired $t$-tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency. Under the v1 codebase, Detach OCC shows negligible difference from Vanilla ($d \\approx -0.04$, $p = 0.91$); under v2 (Table~\\ref{tab:main_results}), the effect reverses in sign ($\\Delta{=}+2.2$\\,pp, $p = 0.28$) but remains statistically indistinguishable from Vanilla, confirming that gradient-detached auxiliary supervision does not harm collision avoidance regardless of codebase version. Under v1, all gradient-flow conditions also show $p > 0.35$.",
          "-",
          "+\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed paired $t$-tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.",
          " \\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.",
          " ",
          " \\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details)."
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

_source line 22_

Now let me also check the Table 2 caption (line 51) for the n description, since task 5 mentions n counts should be accurate there too.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "8a77bac4-8ebc-473d-8b66-afe154cc851c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Em3TbpnQJ5AMV29oFBN8Ku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 337,
      "cache_read_input_tokens": 37420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 337
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

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_013oJnWhvDHEEXouC6H6PQD4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "offset": 49,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "bb2ea3c4-85d0-4bf2-91ca-100da69ac13f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Em3TbpnQJ5AMV29oFBN8Ku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 337,
      "cache_read_input_tokens": 37420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 337
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

_source line 24 · 2026-05-27T04:31:25.897Z_

<details><summary>↩ Tool result · `toolu_013oJnWhvDHEEXouC6H6PQD4`</summary>

```text
49	\begin{table}[t]
50	\centering
51	\caption{$2{\times}2$ factorial: normalization type $\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data ($n{=}1$ for LN cells).}
52	\label{tab:factorial}
53	\begin{tabular}{lccc}
54	\toprule
55	 & Gradient ON & Gradient OFF & $\Delta$(ON$-$OFF) \\
56	\midrule
57	BatchNorm    & Full OCC (0.725) & Detach OCC (\textbf{0.767}) & $-$4.2 \\
58	LayerNorm    & Full OCC+LN (0.740) & Detach+LN$^\star$ (0.765) & $-$2.5 \\
59	\midrule
60	$\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "ae313a34-c9d5-4c2b-8c99-c0b35a4ec226",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data ($n{=}1$ for LN cells).}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (\\textbf{0.767}) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.740) & Detach+LN$^\\star$ (0.765) & $-$2.5 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
      "numLines": 15,
      "startLine": 49,
      "totalLines": 81
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

Table 2 caption also has inaccurate n description. Fixing it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "2fd5e644-18fe-4102-8456-659d18314bda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FS5oVMSYBEfd1aB7n4kFUe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 37757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
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

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_01PX5MqPjBSwrxipC51EypXP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "The BN cell shows a larger deficit in current data ($n{=}1$ for LN cells).}",
  "new_string": "The BN cell shows a larger deficit in current data (Full OCC+LN: $n{=}1$, v2; Detach+LN: $n{=}3$, v1$^\\star$).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "ac113a90-077d-454b-9424-18fee2f089b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FS5oVMSYBEfd1aB7n4kFUe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 37757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
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

_source line 27 · 2026-05-27T04:31:30.149Z_

<details><summary>↩ Tool result · `toolu_01PX5MqPjBSwrxipC51EypXP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "e7c14b50-9abe-46f7-b134-a10265da8fd7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "The BN cell shows a larger deficit in current data ($n{=}1$ for LN cells).}",
    "newString": "The BN cell shows a larger deficit in current data (Full OCC+LN: $n{=}1$, v2; Detach+LN: $n{=}3$, v1$^\\star$).}",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.\n\n\\textbf{Interaction pattern between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) show a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type; whether normalization modulates the magnitude requires additional LN seeds to confirm (Section~\\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\\Delta{=}-2.0$\\,pp vs.\\ Vanilla, $-$4.2\\,pp vs.\\ Detach OCC within the BN factorial row) and the most unstable ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\\Delta{=}-0.5$\\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) matches or slightly exceeds the Vanilla baseline (0.745); Detach+LN$^\\star$ (0.765) shows a comparable level under v1 code. These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).\n\n\\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells): individual seeds range from 0.776 (near Vanilla) to 0.654 ($\\Delta{=}-9.1$\\,pp), indicating a volatile optimization landscape under the BN + gradient flow combination.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds; $^\\star$Trained with v1 code; v2 multi-seed results pending. Factorial conditions (above midrule) use v2 code unless marked $^\\star$; supplementary conditions (below midrule) use v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nVanilla       & 3 & 0.878 $\\pm$ 0.032 & \\textbf{0.745} $\\pm$ 0.024 & --- & ---    \\\\\nDetach OCC (BN)    & 4 & 0.908 $\\pm$ 0.026 & 0.767 $\\pm$ 0.024 & [0.744, 0.794] & $+$2.2 \\\\\nDetach+LN$^\\star$     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & --- \\\\\n\\addlinespace[3pt]\nRandom OCC (BN)$^\\star$    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & --- \\\\\nFull OCC+LN$^\\dagger$   & 1 & 0.842 & 0.740 & --- & $-$0.5 \\\\\nFull OCC (BN) & 3 & 0.854 $\\pm$ 0.052 & 0.725 $\\pm$ 0.064 & [0.654, 0.776] & $-$2.0 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\\nCutoff@15K$^\\ddagger$   & 2 & 0.883 $\\pm$ 0.041 & 0.782 $\\pm$ 0.031 & --- & $+$0.2 \\\\\nCutoff@25K$^\\ddagger$   & 2 & 0.887 $\\pm$ 0.061 & 0.724 $\\pm$ 0.051 & --- & $-$5.6 \\\\\nCutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\\nCutoff@45K$^\\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\\\\nReverse Cutoff$^\\ddagger$ & 2 & 0.839 $\\pm$ 0.072 & 0.718 $\\pm$ 0.025 & --- & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Normalization--Gradient Flow Interaction}\n\\label{sec:mechanism}\n\nThe four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach OCC 0.767; Hedges' $g{=}-0.781$, bootstrap 95\\% CI $[-0.108, 0.014]$, crossing zero and thus not individually significant at $\\alpha{=}0.05$ given the small sample). The LN cells show the same directional pattern ($-$2.5\\,pp), yielding a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type, with the BN cell showing a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$). We report effect sizes and confidence intervals for transparency; the small-$n$ factorial design prioritizes breadth across a 12-condition space over statistical power for individual pairwise tests. The consistent gradient flow effect---both BN and LN rows show lower CAR under gradient flow ON than OFF---provides the primary evidence for the ordinal interaction pattern.\n\n\\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON without crossing (Figure~\\ref{fig:factorial}), confirming an ordinal pattern. The BN cell shows a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has only $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$); whether normalization type modulates the gradient flow effect requires additional seeds to confirm.\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data ($n{=}1$ for LN cells).}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (\\textbf{0.767}) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.740) & Detach+LN$^\\star$ (0.765) & $-$2.5 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\\,pp) and LN ($-$2.5\\,pp), consistent with an ordinal interaction pattern. The BN cell shows a larger deficit; Full OCC+LN has $n{=}1$ (v2); Detach+LN has $n{=}3$ (v1, marked $^\\star$). Error bars: cross-seed SD.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:gradient_analysis}, Appendix) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC, with conflict rates of ${\\sim}$50\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions, ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content does not affect outcomes.\n\n\\textbf{Mechanism remains open.} The observed interaction pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. CKA analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP), localizing the safety degradation to optimization dynamics rather than representational corruption.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
    "structuredPatch": [
      {
        "oldStart": 48,
        "oldLines": 7,
        "newStart": 48,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{table}[t]",
          " \\centering",
          "-\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data ($n{=}1$ for LN cells).}",
          "+\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data (Full OCC+LN: $n{=}1$, v2; Detach+LN: $n{=}3$, v1$^\\star$).}",
          " \\label{tab:factorial}",
          " \\begin{tabular}{lccc}",
          " \\toprule"
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

_source line 28_

Now compile to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "65836ee1-cf27-46b9-90d3-98604a426fdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019oxnQBix3UEBVowpZ39YkR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 38337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
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

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_012zU6uUzY1naR7gTo4Swwya`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/ && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^!\" | head -20",
  "description": "Compile LaTeX and check for errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "e1645d67-9ad2-4f3b-b816-aedcc2155838",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019oxnQBix3UEBVowpZ39YkR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 38337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
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

_source line 30 · 2026-05-27T04:31:35.088Z_

<details><summary>↩ Tool result · `toolu_012zU6uUzY1naR7gTo4Swwya`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "c55d1abd-fb90-4e3d-ad71-580071c3725b",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 31_

编译无报错。最终验证修改后的文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "790823dd-f460-4845-9ce3-6feab18cb62c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gi4jJB8s8aMSBUtxuJkQMt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 162,
      "cache_read_input_tokens": 38624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 162
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

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_0195h7YLZqVVsD35q4ijss5r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "offset": 1,
  "limit": 70
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "99959edb-d599-4108-b6ec-a507c46d4b06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gi4jJB8s8aMSBUtxuJkQMt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 162,
      "cache_read_input_tokens": 38624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 162
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

_source line 33 · 2026-05-27T04:31:38.316Z_

<details><summary>↩ Tool result · `toolu_0195h7YLZqVVsD35q4ijss5r`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Main Results}
6	
7	Table~\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\times$ 10 tasks per seed). $\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\star$) uses v1 code but is included above the midrule as a factorial control; its $\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.
8	
9	\textbf{Interaction pattern between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) show a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type; whether normalization modulates the magnitude requires additional LN seeds to confirm (Section~\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\Delta{=}-2.0$\,pp vs.\ Vanilla, $-$4.2\,pp vs.\ Detach OCC within the BN factorial row) and the most unstable ($\sigma{=}0.064$, more than $2.5{\times}$ that of other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\Delta{=}-0.5$\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767, $\Delta{=}+2.2$\,pp) matches or slightly exceeds the Vanilla baseline (0.745); Detach+LN$^\star$ (0.765) shows a comparable level under v1 code. These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).
10	
11	\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\sigma{=}0.064$, more than $2.5{\times}$ that of other cells): individual seeds range from 0.776 (near Vanilla) to 0.654 ($\Delta{=}-9.1$\,pp), indicating a volatile optimization landscape under the BN + gradient flow combination.
12	
13	
14	\begin{table}[t]
15	\centering
16	\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\pm$ SD across seeds; 95\% CIs via bootstrap. $^\dagger$1 seed; $^\ddagger$2 seeds; $^\star$Trained with v1 code; v2 multi-seed results pending. Factorial conditions (above midrule) use v2 code unless marked $^\star$; supplementary conditions (below midrule) use v1 code.}
17	\label{tab:main_results}
18	\small
19	\setlength{\tabcolsep}{4pt}
20	\begin{tabular}{lccccc}
21	\toprule
22	Condition & Seeds & TSR & CAR & $95\%$ CI & $\Delta$CAR \\
23	\midrule
24	Vanilla       & 3 & 0.878 $\pm$ 0.032 & \textbf{0.745} $\pm$ 0.024 & --- & ---    \\
25	Detach OCC (BN)    & 4 & 0.908 $\pm$ 0.026 & 0.767 $\pm$ 0.024 & [0.744, 0.794] & $+$2.2 \\
26	Detach+LN$^\star$     & 3 & 0.901 $\pm$ 0.016 & 0.765 $\pm$ 0.023 & [0.748, 0.792] & --- \\
27	\addlinespace[3pt]
28	Random OCC (BN)$^\star$    & 3 & 0.869 $\pm$ 0.029 & 0.789 $\pm$ 0.031 & [0.754, 0.814] & --- \\
29	Full OCC+LN$^\dagger$   & 1 & 0.842 & 0.740 & --- & $-$0.5 \\
30	Full OCC (BN) & 3 & 0.854 $\pm$ 0.052 & 0.725 $\pm$ 0.064 & [0.654, 0.776] & $-$2.0 \\
31	\midrule
32	Depth             & 4 & 0.889 $\pm$ 0.042 & 0.780 $\pm$ 0.039 & [0.747, 0.812] & 0.0 \\
33	Cutoff@15K$^\ddagger$   & 2 & 0.883 $\pm$ 0.041 & 0.782 $\pm$ 0.031 & --- & $+$0.2 \\
34	Cutoff@25K$^\ddagger$   & 2 & 0.887 $\pm$ 0.061 & 0.724 $\pm$ 0.051 & --- & $-$5.6 \\
35	Cutoff@35K        & 3 & 0.933 $\pm$ 0.032 & 0.779 $\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\
36	Cutoff@45K$^\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\
37	Reverse Cutoff$^\ddagger$ & 2 & 0.839 $\pm$ 0.072 & 0.718 $\pm$ 0.025 & --- & $-$6.2 \\
38	\bottomrule
39	\end{tabular}
40	\end{table}
41	
42	\subsection{Normalization--Gradient Flow Interaction}
43	\label{sec:mechanism}
44	
45	The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\times}2$ factorial (Table~\ref{tab:factorial}, Figure~\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\,pp (Full OCC 0.725 vs.\ Detach OCC 0.767; Hedges' $g{=}-0.781$, bootstrap 95\% CI $[-0.108, 0.014]$, crossing zero and thus not individually significant at $\alpha{=}0.05$ given the small sample). The LN cells show the same directional pattern ($-$2.5\,pp), yielding a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type, with the BN cell showing a larger deficit ($-$4.2\,pp vs.\ $-$2.5\,pp under LN) in current data, though Full OCC+LN has $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\star$). We report effect sizes and confidence intervals for transparency; the small-$n$ factorial design prioritizes breadth across a 12-condition space over statistical power for individual pairwise tests. The consistent gradient flow effect---both BN and LN rows show lower CAR under gradient flow ON than OFF---provides the primary evidence for the ordinal interaction pattern.
46	
47	\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON without crossing (Figure~\ref{fig:factorial}), confirming an ordinal pattern. The BN cell shows a larger deficit ($-$4.2\,pp vs.\ $-$2.5\,pp under LN) in current data, though Full OCC+LN has only $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\star$); whether normalization type modulates the gradient flow effect requires additional seeds to confirm.
48	
49	\begin{table}[t]
50	\centering
51	\caption{$2{\times}2$ factorial: normalization type $\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data (Full OCC+LN: $n{=}1$, v2; Detach+LN: $n{=}3$, v1$^\star$).}
52	\label{tab:factorial}
53	\begin{tabular}{lccc}
54	\toprule
55	 & Gradient ON & Gradient OFF & $\Delta$(ON$-$OFF) \\
56	\midrule
57	BatchNorm    & Full OCC (0.725) & Detach OCC (\textbf{0.767}) & $-$4.2 \\
58	LayerNorm    & Full OCC+LN (0.740) & Detach+LN$^\star$ (0.765) & $-$2.5 \\
59	\midrule
60	$\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	\begin{figure}[t]
66	\centering
67	\includegraphics[width=0.65\textwidth]{figures/factorial_2x2.pdf}
68	\caption{$2{\times}2$ factorial interaction: normalization type (BN/LN) $\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\,pp) and LN ($-$2.5\,pp), consistent with an ordinal interaction pattern. The BN cell shows a larger deficit; Full OCC+LN has $n{=}1$ (v2); Detach+LN has $n{=}3$ (v1, marked $^\star$). Error bars: cross-seed SD.}
69	\label{fig:factorial}
70	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "56168452-6442-43c9-b145-f50db0e1cbb3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.\n\n\\textbf{Interaction pattern between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) show a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type; whether normalization modulates the magnitude requires additional LN seeds to confirm (Section~\\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\\Delta{=}-2.0$\\,pp vs.\\ Vanilla, $-$4.2\\,pp vs.\\ Detach OCC within the BN factorial row) and the most unstable ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\\Delta{=}-0.5$\\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767, $\\Delta{=}+2.2$\\,pp) matches or slightly exceeds the Vanilla baseline (0.745); Detach+LN$^\\star$ (0.765) shows a comparable level under v1 code. These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).\n\n\\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\\sigma{=}0.064$, more than $2.5{\\times}$ that of other cells): individual seeds range from 0.776 (near Vanilla) to 0.654 ($\\Delta{=}-9.1$\\,pp), indicating a volatile optimization landscape under the BN + gradient flow combination.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds; $^\\star$Trained with v1 code; v2 multi-seed results pending. Factorial conditions (above midrule) use v2 code unless marked $^\\star$; supplementary conditions (below midrule) use v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nVanilla       & 3 & 0.878 $\\pm$ 0.032 & \\textbf{0.745} $\\pm$ 0.024 & --- & ---    \\\\\nDetach OCC (BN)    & 4 & 0.908 $\\pm$ 0.026 & 0.767 $\\pm$ 0.024 & [0.744, 0.794] & $+$2.2 \\\\\nDetach+LN$^\\star$     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & --- \\\\\n\\addlinespace[3pt]\nRandom OCC (BN)$^\\star$    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & --- \\\\\nFull OCC+LN$^\\dagger$   & 1 & 0.842 & 0.740 & --- & $-$0.5 \\\\\nFull OCC (BN) & 3 & 0.854 $\\pm$ 0.052 & 0.725 $\\pm$ 0.064 & [0.654, 0.776] & $-$2.0 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\\nCutoff@15K$^\\ddagger$   & 2 & 0.883 $\\pm$ 0.041 & 0.782 $\\pm$ 0.031 & --- & $+$0.2 \\\\\nCutoff@25K$^\\ddagger$   & 2 & 0.887 $\\pm$ 0.061 & 0.724 $\\pm$ 0.051 & --- & $-$5.6 \\\\\nCutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\\nCutoff@45K$^\\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\\\\nReverse Cutoff$^\\ddagger$ & 2 & 0.839 $\\pm$ 0.072 & 0.718 $\\pm$ 0.025 & --- & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Normalization--Gradient Flow Interaction}\n\\label{sec:mechanism}\n\nThe four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach OCC 0.767; Hedges' $g{=}-0.781$, bootstrap 95\\% CI $[-0.108, 0.014]$, crossing zero and thus not individually significant at $\\alpha{=}0.05$ given the small sample). The LN cells show the same directional pattern ($-$2.5\\,pp), yielding a pattern consistent with an ordinal interaction: gradient flow is associated with lower safety regardless of normalization type, with the BN cell showing a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$). We report effect sizes and confidence intervals for transparency; the small-$n$ factorial design prioritizes breadth across a 12-condition space over statistical power for individual pairwise tests. The consistent gradient flow effect---both BN and LN rows show lower CAR under gradient flow ON than OFF---provides the primary evidence for the ordinal interaction pattern.\n\n\\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON without crossing (Figure~\\ref{fig:factorial}), confirming an ordinal pattern. The BN cell shows a larger deficit ($-$4.2\\,pp vs.\\ $-$2.5\\,pp under LN) in current data, though Full OCC+LN has only $n{=}1$ (v2) and Detach+LN has $n{=}3$ (v1, marked $^\\star$); whether normalization type modulates the gradient flow effect requires additional seeds to confirm.\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (consistent with an ordinal interaction pattern): gradient flow is associated with lower CAR. The BN cell shows a larger deficit in current data (Full OCC+LN: $n{=}1$, v2; Detach+LN: $n{=}3$, v1$^\\star$).}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (\\textbf{0.767}) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.740) & Detach+LN$^\\star$ (0.765) & $-$2.5 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\\,pp) and LN ($-$2.5\\,pp), consistent with an ordinal interaction pattern. The BN cell shows a larger deficit; Full OCC+LN has $n{=}1$ (v2); Detach+LN has $n{=}3$ (v1, marked $^\\star$). Error bars: cross-seed SD.}\n\\label{fig:factorial}\n\\end{figure}",
      "numLines": 70,
      "startLine": 1,
      "totalLines": 81
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01Bsm55RKUApubHDYcpbUtBU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "offset": 67,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "bda87d8e-fc7f-4d81-90a8-af6975b426cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gi4jJB8s8aMSBUtxuJkQMt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 162,
      "cache_read_input_tokens": 38624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 162
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

_source line 35 · 2026-05-27T04:31:39.123Z_

<details><summary>↩ Tool result · `toolu_01Bsm55RKUApubHDYcpbUtBU`</summary>

```text
67	\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \texttt{body\_xpos} exceeds $10^{-3}$. Bootstrap 95\% CIs are computed via 10{,}000 resamples (percentile method).
68	
69	\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed paired $t$-tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.
70	\textbf{CKA analysis.} Centered Kernel Alignment~\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.
71	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "56e6963f-1013-40cd-940c-b8a18be0b9be",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
      "content": "\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed paired $t$-tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n",
      "numLines": 5,
      "startLine": 67,
      "totalLines": 137
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

全部修改完成，编译无错误。汇总：

| 项目 | 修改内容 |
|------|---------|
| **Table 1 Detach+LN 行** | 已有 `$^\star$` 和 `---`，无需改 |
| **Table 1 caption** | `$^\star$v1 code` → `$^\star$Trained with v1 code; v2 multi-seed results pending` |
| **正文 ΔCAR 描述** | 删除 Detach+LN 的 `$\Delta{=}+2.0$\,pp`，改为 `Detach+LN$^\star$ (0.765) shows a comparable level under v1 code` |
| **Table 2** | `Detach+LN (0.765)` → `Detach+LN$^\star$ (0.765)` |
| **Table 2 caption** | `$n{=}1$ for LN cells` → `Full OCC+LN: $n{=}1$, v2; Detach+LN: $n{=}3$, v1$^\star$` |
| **Figure 2 caption** | `LN cells have $n{=}1$` → `Full OCC+LN has $n{=}1$ (v2); Detach+LN has $n{=}3$ (v1, marked $^\star$)` |
| **appendix.tex Statistical tests** | 删除 v1 统计数据（`d ≈ -0.04, p = 0.91` 及相关句子） |
| **编译** | pdflatex 无报错 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "uuid": "27139d93-4eda-4b41-8a94-66f374d0fa33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7REucDReMkas2BgoYSDuy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3390,
      "cache_read_input_tokens": 38786,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3390
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

_source line 37_

全部修改完成，编译无错误。汇总：

| 项目 | 修改内容 |
|------|---------|
| **Table 1 Detach+LN 行** | 已有 `$^\star$` 和 `---`，无需改 |
| **Table 1 caption** | `$^\star$v1 code` → `$^\star$Trained with v1 code; v2 multi-seed results pending` |
| **正文 ΔCAR 描述** | 删除 Detach+LN 的 `$\Delta{=}+2.0$\,pp`，改为 `Detach+LN$^\star$ (0.765) shows a comparable level under v1 code` |
| **Table 2** | `Detach+LN (0.765)` → `Detach+LN$^\star$ (0.765)` |
| **Table 2 caption** | `$n{=}1$ for LN cells` → `Full OCC+LN: $n{=}1$, v2; Detach+LN: $n{=}3$, v1$^\star$` |
| **Figure 2 caption** | `LN cells have $n{=}1$` → `Full OCC+LN has $n{=}1$ (v2); Detach+LN has $n{=}3$ (v1, marked $^\star$)` |
| **appendix.tex Statistical tests** | 删除 v1 统计数据（`d ≈ -0.04, p = 0.91` 及相关句子） |
| **编译** | pdflatex 无报错 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 114767,
  "duration_api_ms": 116869,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "4f91e1b7-0518-4953-99a2-9c7e161d17cc",
  "total_cost_usd": 0.53124625,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 30335,
    "cache_read_input_tokens": 369933,
    "output_tokens": 6188,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30335,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 438,
        "cache_read_input_tokens": 38786,
        "cache_creation_input_tokens": 3390,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3390
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1821,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001926,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 6188,
      "cacheReadInputTokens": 369933,
      "cacheCreationInputTokens": 30335,
      "webSearchRequests": 0,
      "costUSD": 0.52932025,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "10d85163-48cf-4cf6-9a10-743c12aa02fd"
}
```

</details>

---
