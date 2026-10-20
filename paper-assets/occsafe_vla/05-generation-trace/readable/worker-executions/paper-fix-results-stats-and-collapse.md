# paper fix results stats and collapse

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_paper_fix_results-stats-and-collapse_20260526T151131.log`
- **Structured JSON:** [`2ec4b9c51cdb5f4768d3.json`](../../sessions/2e/2ec4b9c51cdb5f4768d3.json)

## Before a recorded user message

18 recorded events

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
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
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
  "uuid": "b715b191-0842-4987-874b-87d8cd8c0986",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/memory/"
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
    "resetsAt": 1779809400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "55c7603d-b36a-4be1-9f71-f95b9a0f5c00",
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the file and running the Python code to get the new statistics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "uuid": "6fea4eb2-b4cf-47b6-b742-2480da4c6ad7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wfeg5aHkxWkF2EdpPKiLQi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12027,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12027
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — Read · `toolu_01NyUNpgrnDFXzfctSqvEVeF`</summary>

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
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "uuid": "bd4a365e-83b2-424a-92bf-67df435dc859",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wfeg5aHkxWkF2EdpPKiLQi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12027,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12027
      },
      "output_tokens": 24,
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

_source line 6 · 2026-05-26T15:11:45.136Z_

<details><summary>↩ Tool result · `toolu_01NyUNpgrnDFXzfctSqvEVeF`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Main Results}
6	\label{sec:main_results}
7	
8	Table~\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\times$ 10 tasks per seed). Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.
9	
10	\textbf{Ordinal interaction between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) reveal an ordinal interaction: gradient flow is detrimental to safety regardless of normalization, and BatchNorm amplifies the damage (Section~\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\Delta{=}-4.3$\,pp vs.\ Vanilla) and the most unstable ($\sigma{=}0.064$, $3{\times}$ other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\Delta{=}-2.8$\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767) and Detach+LN (0.765) both approach the Vanilla baseline (0.768). These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).
11	
12	\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell: one seed achieves CAR 0.776 (near Vanilla), while another collapses to 0.654 ($\Delta{=}-11.4$\,pp). This seed-dependent instability, unique to the BN + gradient flow combination, suggests a volatile optimization landscape where BatchNorm statistics amplify the effect of initialization under dual-objective training.
13	
14	
15	
16	\begin{table}[t]
17	\centering
18	\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\pm$ SD across seeds; 95\% CIs via bootstrap. $^\dagger$1 seed; $^\ddagger$2 seeds. Factorial cell CAR values use v2 code; $\Delta$CAR computed against v2 Vanilla. Cutoff conditions retain the auxiliary head forward pass post-cutoff (Detach mode).}
19	\label{tab:main_results}
20	\small
21	\setlength{\tabcolsep}{4pt}
22	\begin{tabular}{lccccc}
23	\toprule
24	Condition & Seeds & TSR & CAR & $95\%$ CI & $\Delta$CAR \\
25	\midrule
26	Vanilla$^\dagger$       & 1 & --- & \textbf{0.768} & --- & ---    \\
27	Detach OCC (BN)    & 4 & --- & 0.767 $\pm$ 0.024 & [0.744, 0.794] & $-$0.1 \\
28	Detach+LN     & 3 & 0.901 $\pm$ 0.016 & 0.765 $\pm$ 0.023 & [0.748, 0.792] & $-$0.3 \\
29	Random OCC (BN)    & 3 & 0.869 $\pm$ 0.029 & 0.789 $\pm$ 0.031 & [0.754, 0.814] & --- \\
30	Full OCC+LN$^\dagger$   & 1 & --- & 0.740 & --- & $-$2.8 \\
31	Full OCC (BN) & 3 & --- & 0.725 $\pm$ 0.064 & [0.654, 0.776] & $-$4.3 \\
32	\midrule
33	Depth             & 4 & 0.889 $\pm$ 0.042 & 0.780 $\pm$ 0.039 & [0.747, 0.812] & 0.0 \\
34	Cutoff@15K$^\ddagger$   & 2 & 0.883 $\pm$ 0.041 & 0.782 $\pm$ 0.031 & --- & $+$0.2 \\
35	Cutoff@25K$^\ddagger$   & 2 & 0.887 $\pm$ 0.061 & 0.724 $\pm$ 0.051 & --- & $-$5.6 \\
36	Cutoff@35K        & 3 & 0.933 $\pm$ 0.032 & 0.779 $\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\
37	Cutoff@45K$^\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\
38	Reverse Cutoff$^\ddagger$ & 2 & 0.839 $\pm$ 0.072 & 0.718 $\pm$ 0.025 & --- & $-$6.2 \\
39	\bottomrule
40	\end{tabular}
41	\end{table}
42	
43	\subsection{Normalization--Gradient Flow Interaction}
44	\label{sec:mechanism}
45	
46	The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\times}2$ factorial (Table~\ref{tab:factorial}, Figure~\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\,pp (Full OCC 0.725 vs.\ Detach OCC 0.767; Hedges' $g{=}-1.023$, $p{=}0.422$, bootstrap 95\% CI $[-0.001, 0.116]$). The LN cells show the same directional pattern ($-$2.5\,pp), yielding an ordinal interaction: gradient flow is detrimental regardless of normalization, and BatchNorm amplifies the damage.
47	
48	\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON; the lines do not cross (Figure~\ref{fig:factorial}). With BN, gradient flow degrades CAR by $-$4.2\,pp (Full OCC 0.725 vs.\ Detach 0.767). With LN, gradient flow degrades CAR by $-$2.5\,pp (Full OCC+LN 0.740 vs.\ Detach+LN 0.765). The larger BN deficit suggests that BatchNorm statistics amplify the detrimental effect of auxiliary gradient flow on safety behavior.
49	
50	\textbf{Full OCC (BN) is the worst and most unstable configuration.} Full OCC with BatchNorm and gradient flow (CAR 0.725) falls 4.3\,pp below Vanilla, with cross-seed standard deviation of 0.064---nearly three times that of the other factorial cells ($\sigma \leq 0.024$). Individual seeds range from 0.654 to 0.776, indicating that the BN + gradient flow combination creates a volatile optimization landscape.
51	
52	\begin{table}[t]
53	\centering
54	\caption{$2{\times}2$ factorial: normalization type $\times$ gradient flow. Both lines slope downward (ordinal interaction): gradient flow is detrimental, and BatchNorm amplifies the damage.}
55	\label{tab:factorial}
56	\begin{tabular}{lccc}
57	\toprule
58	 & Gradient ON & Gradient OFF & $\Delta$(ON$-$OFF) \\
59	\midrule
60	BatchNorm    & Full OCC (0.725) & Detach OCC (\textbf{0.767}) & $-$4.2 \\
61	LayerNorm    & Full OCC+LN (0.740) & Detach+LN (0.765) & $-$2.5 \\
62	\midrule
63	$\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\
64	\bottomrule
65	\end{tabular}
66	\end{table}
67	
68	\begin{figure}[t]
69	\centering
70	\includegraphics[width=0.65\textwidth]{figures/factorial_2x2.pdf}
71	\caption{$2{\times}2$ factorial interaction: normalization type (BN/LN) $\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\,pp) and LN ($-$2.5\,pp), an ordinal interaction. BatchNorm amplifies the damage. Error bars: cross-seed SD.}
72	\label{fig:factorial}
73	\end{figure}
74	
75	\subsection{Gradient Dynamics}
76	\label{sec:gradient_dynamics}
77	
78	\begin{figure}[t]
79	\centering
80	\includegraphics[width=\textwidth]{figures/gradient_analysis_combined.pdf}
81	\caption{Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Random OCC, Detach OCC). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1--13\% of Vanilla. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d)~Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.}
82	\label{fig:gradient_analysis}
83	\end{figure}
84	
85	Figure~\ref{fig:gradient_analysis} examines gradient dynamics across conditions. All gradient norms are computed with respect to the L1 action loss (action tokens only), not the full language modeling objective.
86	
87	\textbf{Gradient orthogonality.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\ref{fig:gradient_analysis}c), with conflict rates of ${\sim}$50\%. This confirms that action and auxiliary gradients are orthogonal: direct gradient conflict is not the mechanism through which auxiliary heads affect safety. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (0.87--1.14$\times$ Vanilla norms), which rules out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content does not affect outcomes.
88	
89	\textbf{Mechanism remains open.} The ordinal interaction---gradient flow is detrimental, BatchNorm amplifies---cannot be explained by gradient conflict (orthogonality rules it out) or by gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape, but the precise mechanism requires further investigation.
90	
91	\textbf{Representational structure is preserved across all conditions.} CKA between fine-tuned and pretrained encoder features shows that all conditions, including the worst-performing Full OCC (BN), maintain high similarity to the pretrained representations (CKA $\geq$ 0.95 for both DINOv2 and SigLIP encoders). The safety degradation under gradient flow therefore does not stem from representational corruption: the encoders retain their pretrained structure, yet the policy behaves less safely. This dissociation between representational fidelity and behavioral safety reinforces the conclusion that the detrimental effect operates through optimization dynamics rather than representation distortion.
92	
93	Additional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\ref{app:additional}.
94	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "uuid": "29b18a34-a2e7-4eac-b240-60da8c1149fc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.\n\n\\textbf{Ordinal interaction between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) reveal an ordinal interaction: gradient flow is detrimental to safety regardless of normalization, and BatchNorm amplifies the damage (Section~\\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\\Delta{=}-4.3$\\,pp vs.\\ Vanilla) and the most unstable ($\\sigma{=}0.064$, $3{\\times}$ other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\\Delta{=}-2.8$\\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767) and Detach+LN (0.765) both approach the Vanilla baseline (0.768). These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).\n\n\\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell: one seed achieves CAR 0.776 (near Vanilla), while another collapses to 0.654 ($\\Delta{=}-11.4$\\,pp). This seed-dependent instability, unique to the BN + gradient flow combination, suggests a volatile optimization landscape where BatchNorm statistics amplify the effect of initialization under dual-objective training.\n\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds. Factorial cell CAR values use v2 code; $\\Delta$CAR computed against v2 Vanilla. Cutoff conditions retain the auxiliary head forward pass post-cutoff (Detach mode).}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nVanilla$^\\dagger$       & 1 & --- & \\textbf{0.768} & --- & ---    \\\\\nDetach OCC (BN)    & 4 & --- & 0.767 $\\pm$ 0.024 & [0.744, 0.794] & $-$0.1 \\\\\nDetach+LN     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & $-$0.3 \\\\\nRandom OCC (BN)    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & --- \\\\\nFull OCC+LN$^\\dagger$   & 1 & --- & 0.740 & --- & $-$2.8 \\\\\nFull OCC (BN) & 3 & --- & 0.725 $\\pm$ 0.064 & [0.654, 0.776] & $-$4.3 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\\nCutoff@15K$^\\ddagger$   & 2 & 0.883 $\\pm$ 0.041 & 0.782 $\\pm$ 0.031 & --- & $+$0.2 \\\\\nCutoff@25K$^\\ddagger$   & 2 & 0.887 $\\pm$ 0.061 & 0.724 $\\pm$ 0.051 & --- & $-$5.6 \\\\\nCutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\\nCutoff@45K$^\\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\\\\nReverse Cutoff$^\\ddagger$ & 2 & 0.839 $\\pm$ 0.072 & 0.718 $\\pm$ 0.025 & --- & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Normalization--Gradient Flow Interaction}\n\\label{sec:mechanism}\n\nThe four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach OCC 0.767; Hedges' $g{=}-1.023$, $p{=}0.422$, bootstrap 95\\% CI $[-0.001, 0.116]$). The LN cells show the same directional pattern ($-$2.5\\,pp), yielding an ordinal interaction: gradient flow is detrimental regardless of normalization, and BatchNorm amplifies the damage.\n\n\\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON; the lines do not cross (Figure~\\ref{fig:factorial}). With BN, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach 0.767). With LN, gradient flow degrades CAR by $-$2.5\\,pp (Full OCC+LN 0.740 vs.\\ Detach+LN 0.765). The larger BN deficit suggests that BatchNorm statistics amplify the detrimental effect of auxiliary gradient flow on safety behavior.\n\n\\textbf{Full OCC (BN) is the worst and most unstable configuration.} Full OCC with BatchNorm and gradient flow (CAR 0.725) falls 4.3\\,pp below Vanilla, with cross-seed standard deviation of 0.064---nearly three times that of the other factorial cells ($\\sigma \\leq 0.024$). Individual seeds range from 0.654 to 0.776, indicating that the BN + gradient flow combination creates a volatile optimization landscape.\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (ordinal interaction): gradient flow is detrimental, and BatchNorm amplifies the damage.}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (\\textbf{0.767}) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.740) & Detach+LN (0.765) & $-$2.5 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\\,pp) and LN ($-$2.5\\,pp), an ordinal interaction. BatchNorm amplifies the damage. Error bars: cross-seed SD.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Gradient Dynamics}\n\\label{sec:gradient_dynamics}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Random OCC, Detach OCC). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1--13\\% of Vanilla. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d)~Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nFigure~\\ref{fig:gradient_analysis} examines gradient dynamics across conditions. All gradient norms are computed with respect to the L1 action loss (action tokens only), not the full language modeling objective.\n\n\\textbf{Gradient orthogonality.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\\ref{fig:gradient_analysis}c), with conflict rates of ${\\sim}$50\\%. This confirms that action and auxiliary gradients are orthogonal: direct gradient conflict is not the mechanism through which auxiliary heads affect safety. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (0.87--1.14$\\times$ Vanilla norms), which rules out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content does not affect outcomes.\n\n\\textbf{Mechanism remains open.} The ordinal interaction---gradient flow is detrimental, BatchNorm amplifies---cannot be explained by gradient conflict (orthogonality rules it out) or by gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape, but the precise mechanism requires further investigation.\n\n\\textbf{Representational structure is preserved across all conditions.} CKA between fine-tuned and pretrained encoder features shows that all conditions, including the worst-performing Full OCC (BN), maintain high similarity to the pretrained representations (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP encoders). The safety degradation under gradient flow therefore does not stem from representational corruption: the encoders retain their pretrained structure, yet the policy behaves less safely. This dissociation between representational fidelity and behavioral safety reinforces the conclusion that the detrimental effect operates through optimization dynamics rather than representation distortion.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
      "numLines": 94,
      "startLine": 1,
      "totalLines": 94
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Bash · `toolu_01G3bw29E69EuMa2CAQJhmKa`</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\nfrom scipy import stats\n\ncell1 = np.array([0.746, 0.654, 0.776])\ncell3 = np.array([0.774, 0.736, 0.762, 0.794])\n\n# Hedges' g\nn1, n2 = len(cell1), len(cell3)\ns_pooled = np.sqrt(((n1-1)*cell1.std(ddof=1)**2 + (n2-1)*cell3.std(ddof=1)**2) / (n1+n2-2))\nd = (cell1.mean() - cell3.mean()) / s_pooled\nJ = 1 - 3/(4*(n1+n2-2)-1)\ng = d * J\n\n# Welch t-test\nt_stat, p_val = stats.ttest_ind(cell1, cell3, equal_var=False)\n\n# Bootstrap CI\nrng = np.random.default_rng(42)\ndiffs = []\nfor _ in range(10000):\n    b1 = rng.choice(cell1, size=n1, replace=True)\n    b3 = rng.choice(cell3, size=n2, replace=True)\n    diffs.append(b1.mean() - b3.mean())\nci_lo, ci_hi = np.percentile(diffs, [2.5, 97.5])\n\nprint(f'Hedges g = {g:.3f}')\nprint(f'Welch p = {p_val:.3f}')\nprint(f'Bootstrap 95% CI = [{ci_lo:.3f}, {ci_hi:.3f}]')\nprint(f'Mean diff = {cell1.mean() - cell3.mean():.3f}')\n\"\n",
  "description": "Calculate updated statistics for results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "uuid": "ab999012-3641-424f-a03c-45fc12f7e6c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wfeg5aHkxWkF2EdpPKiLQi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12027,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12027
      },
      "output_tokens": 24,
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

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bhqe4r2rk",
  "tool_use_id": "toolu_01G3bw29E69EuMa2CAQJhmKa",
  "description": "Calculate updated statistics for results.tex",
  "task_type": "local_bash",
  "uuid": "44e76318-6c96-4aaa-a804-5736c98eff33",
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6"
}
```

---

### System

_source line 9_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bhqe4r2rk",
  "tool_use_id": "toolu_01G3bw29E69EuMa2CAQJhmKa",
  "status": "completed",
  "output_file": "",
  "summary": "Calculate updated statistics for results.tex",
  "uuid": "6f84da0d-49f1-4b56-b189-f5177ea1f8ea",
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6"
}
```

---

### Tool result

_source line 10 · 2026-05-26T15:11:52.469Z_

<details><summary>↩ Tool result · `toolu_01G3bw29E69EuMa2CAQJhmKa`</summary>

```text
Hedges g = -0.781
Welch p = 0.381
Bootstrap 95% CI = [-0.108, 0.014]
Mean diff = -0.041
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "uuid": "876d02f4-16df-4e8c-9e3f-5d9110f650c4",
  "tool_use_result": {
    "stdout": "Hedges g = -0.781\nWelch p = 0.381\nBootstrap 95% CI = [-0.108, 0.014]\nMean diff = -0.041",
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

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I have the new statistics:
- Hedges' g = -0.781
- Welch p = 0.381
- Bootstrap 95% CI = [-0.108, 0.014]

And I need to find and fix:
1. The old statistics in §4.2 (line 46): `g{=}-1.023$, $p{=}0.422$, bootstrap 95\% CI $[-0.001, 0.116]`
2. The "Gradient collapse ratio" text in the Fig 3 caption (line 81): `(d)~Gradient collapse ratio`


3. Making both replacements now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "uuid": "8a855d5e-388d-46f5-be56-a82804099d83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSEgZuDe12p4dxPhW52P2G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3902,
      "cache_read_input_tokens": 23868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3902
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

_source line 12_

New statistics: Hedges' g = -0.781, p = 0.381, bootstrap 95% CI [-0.108, 0.014]. Applying both fixes now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "uuid": "9ec7e5f4-10de-43bf-a480-01222fc15837",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSEgZuDe12p4dxPhW52P2G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3902,
      "cache_read_input_tokens": 23868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3902
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01N3z7kD6r8D7cz7h9VymVES`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "Hedges' $g{=}-1.023$, $p{=}0.422$, bootstrap 95\\% CI $[-0.001, 0.116]$",
  "new_string": "Hedges' $g{=}-0.781$, $p{=}0.381$, bootstrap 95\\% CI $[-0.108, 0.014]$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "uuid": "90667df1-0c58-4fb0-9e32-b43693097117",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSEgZuDe12p4dxPhW52P2G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3902,
      "cache_read_input_tokens": 23868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3902
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

_source line 14 · 2026-05-26T15:12:01.643Z_

<details><summary>↩ Tool result · `toolu_01N3z7kD6r8D7cz7h9VymVES`</summary>

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
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "uuid": "31b830d9-28a1-4e99-a275-2c0728afbfbf",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "Hedges' $g{=}-1.023$, $p{=}0.422$, bootstrap 95\\% CI $[-0.001, 0.116]$",
    "newString": "Hedges' $g{=}-0.781$, $p{=}0.381$, bootstrap 95\\% CI $[-0.108, 0.014]$",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.\n\n\\textbf{Ordinal interaction between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) reveal an ordinal interaction: gradient flow is detrimental to safety regardless of normalization, and BatchNorm amplifies the damage (Section~\\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\\Delta{=}-4.3$\\,pp vs.\\ Vanilla) and the most unstable ($\\sigma{=}0.064$, $3{\\times}$ other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\\Delta{=}-2.8$\\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767) and Detach+LN (0.765) both approach the Vanilla baseline (0.768). These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).\n\n\\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell: one seed achieves CAR 0.776 (near Vanilla), while another collapses to 0.654 ($\\Delta{=}-11.4$\\,pp). This seed-dependent instability, unique to the BN + gradient flow combination, suggests a volatile optimization landscape where BatchNorm statistics amplify the effect of initialization under dual-objective training.\n\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds. Factorial cell CAR values use v2 code; $\\Delta$CAR computed against v2 Vanilla. Cutoff conditions retain the auxiliary head forward pass post-cutoff (Detach mode).}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nVanilla$^\\dagger$       & 1 & --- & \\textbf{0.768} & --- & ---    \\\\\nDetach OCC (BN)    & 4 & --- & 0.767 $\\pm$ 0.024 & [0.744, 0.794] & $-$0.1 \\\\\nDetach+LN     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & $-$0.3 \\\\\nRandom OCC (BN)    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & --- \\\\\nFull OCC+LN$^\\dagger$   & 1 & --- & 0.740 & --- & $-$2.8 \\\\\nFull OCC (BN) & 3 & --- & 0.725 $\\pm$ 0.064 & [0.654, 0.776] & $-$4.3 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\\nCutoff@15K$^\\ddagger$   & 2 & 0.883 $\\pm$ 0.041 & 0.782 $\\pm$ 0.031 & --- & $+$0.2 \\\\\nCutoff@25K$^\\ddagger$   & 2 & 0.887 $\\pm$ 0.061 & 0.724 $\\pm$ 0.051 & --- & $-$5.6 \\\\\nCutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\\nCutoff@45K$^\\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\\\\nReverse Cutoff$^\\ddagger$ & 2 & 0.839 $\\pm$ 0.072 & 0.718 $\\pm$ 0.025 & --- & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Normalization--Gradient Flow Interaction}\n\\label{sec:mechanism}\n\nThe four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach OCC 0.767; Hedges' $g{=}-1.023$, $p{=}0.422$, bootstrap 95\\% CI $[-0.001, 0.116]$). The LN cells show the same directional pattern ($-$2.5\\,pp), yielding an ordinal interaction: gradient flow is detrimental regardless of normalization, and BatchNorm amplifies the damage.\n\n\\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON; the lines do not cross (Figure~\\ref{fig:factorial}). With BN, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach 0.767). With LN, gradient flow degrades CAR by $-$2.5\\,pp (Full OCC+LN 0.740 vs.\\ Detach+LN 0.765). The larger BN deficit suggests that BatchNorm statistics amplify the detrimental effect of auxiliary gradient flow on safety behavior.\n\n\\textbf{Full OCC (BN) is the worst and most unstable configuration.} Full OCC with BatchNorm and gradient flow (CAR 0.725) falls 4.3\\,pp below Vanilla, with cross-seed standard deviation of 0.064---nearly three times that of the other factorial cells ($\\sigma \\leq 0.024$). Individual seeds range from 0.654 to 0.776, indicating that the BN + gradient flow combination creates a volatile optimization landscape.\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (ordinal interaction): gradient flow is detrimental, and BatchNorm amplifies the damage.}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (\\textbf{0.767}) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.740) & Detach+LN (0.765) & $-$2.5 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\\,pp) and LN ($-$2.5\\,pp), an ordinal interaction. BatchNorm amplifies the damage. Error bars: cross-seed SD.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Gradient Dynamics}\n\\label{sec:gradient_dynamics}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Random OCC, Detach OCC). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1--13\\% of Vanilla. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d)~Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nFigure~\\ref{fig:gradient_analysis} examines gradient dynamics across conditions. All gradient norms are computed with respect to the L1 action loss (action tokens only), not the full language modeling objective.\n\n\\textbf{Gradient orthogonality.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\\ref{fig:gradient_analysis}c), with conflict rates of ${\\sim}$50\\%. This confirms that action and auxiliary gradients are orthogonal: direct gradient conflict is not the mechanism through which auxiliary heads affect safety. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (0.87--1.14$\\times$ Vanilla norms), which rules out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content does not affect outcomes.\n\n\\textbf{Mechanism remains open.} The ordinal interaction---gradient flow is detrimental, BatchNorm amplifies---cannot be explained by gradient conflict (orthogonality rules it out) or by gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape, but the precise mechanism requires further investigation.\n\n\\textbf{Representational structure is preserved across all conditions.} CKA between fine-tuned and pretrained encoder features shows that all conditions, including the worst-performing Full OCC (BN), maintain high similarity to the pretrained representations (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP encoders). The safety degradation under gradient flow therefore does not stem from representational corruption: the encoders retain their pretrained structure, yet the policy behaves less safely. This dissociation between representational fidelity and behavioral safety reinforces the conclusion that the detrimental effect operates through optimization dynamics rather than representation distortion.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
    "structuredPatch": [
      {
        "oldStart": 43,
        "oldLines": 7,
        "newStart": 43,
        "newLines": 7,
        "lines": [
          " \\subsection{Normalization--Gradient Flow Interaction}",
          " \\label{sec:mechanism}",
          " ",
          "-The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach OCC 0.767; Hedges' $g{=}-1.023$, $p{=}0.422$, bootstrap 95\\% CI $[-0.001, 0.116]$). The LN cells show the same directional pattern ($-$2.5\\,pp), yielding an ordinal interaction: gradient flow is detrimental regardless of normalization, and BatchNorm amplifies the damage.",
          "+The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach OCC 0.767; Hedges' $g{=}-0.781$, $p{=}0.381$, bootstrap 95\\% CI $[-0.108, 0.014]$). The LN cells show the same directional pattern ($-$2.5\\,pp), yielding an ordinal interaction: gradient flow is detrimental regardless of normalization, and BatchNorm amplifies the damage.",
          " ",
          " \\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON; the lines do not cross (Figure~\\ref{fig:factorial}). With BN, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach 0.767). With LN, gradient flow degrades CAR by $-$2.5\\,pp (Full OCC+LN 0.740 vs.\\ Detach+LN 0.765). The larger BN deficit suggests that BatchNorm statistics amplify the detrimental effect of auxiliary gradient flow on safety behavior.",
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_01QwXwFgKodoEHvugZ788qVX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "Gradient collapse ratio",
  "new_string": "Gradient norm ratio"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "uuid": "9a271381-b66c-46f1-a5e6-a0b3619c0a6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSEgZuDe12p4dxPhW52P2G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3902,
      "cache_read_input_tokens": 23868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3902
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

_source line 16 · 2026-05-26T15:12:02.266Z_

<details><summary>↩ Tool result · `toolu_01QwXwFgKodoEHvugZ788qVX`</summary>

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
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "uuid": "10e31b76-d2f8-4526-ab83-dda0b79c7c6f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "Gradient collapse ratio",
    "newString": "Gradient norm ratio",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.\n\n\\textbf{Ordinal interaction between gradient flow and normalization.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) reveal an ordinal interaction: gradient flow is detrimental to safety regardless of normalization, and BatchNorm amplifies the damage (Section~\\ref{sec:mechanism}). Full OCC with BN (gradient flow ON, BatchNorm) is the worst-performing factorial cell (CAR 0.725, $\\Delta{=}-4.3$\\,pp vs.\\ Vanilla) and the most unstable ($\\sigma{=}0.064$, $3{\\times}$ other cells). Full OCC+LN (gradient flow ON, LayerNorm) also degrades CAR below Vanilla (0.740, $\\Delta{=}-2.8$\\,pp). Detaching gradient flow recovers safety: Detach OCC (0.767) and Detach+LN (0.765) both approach the Vanilla baseline (0.768). These results are consistent with the hypothesis that spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$).\n\n\\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell: one seed achieves CAR 0.776 (near Vanilla), while another collapses to 0.654 ($\\Delta{=}-11.4$\\,pp). This seed-dependent instability, unique to the BN + gradient flow combination, suggests a volatile optimization landscape where BatchNorm statistics amplify the effect of initialization under dual-objective training.\n\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds. Factorial cell CAR values use v2 code; $\\Delta$CAR computed against v2 Vanilla. Cutoff conditions retain the auxiliary head forward pass post-cutoff (Detach mode).}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nVanilla$^\\dagger$       & 1 & --- & \\textbf{0.768} & --- & ---    \\\\\nDetach OCC (BN)    & 4 & --- & 0.767 $\\pm$ 0.024 & [0.744, 0.794] & $-$0.1 \\\\\nDetach+LN     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & $-$0.3 \\\\\nRandom OCC (BN)    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & --- \\\\\nFull OCC+LN$^\\dagger$   & 1 & --- & 0.740 & --- & $-$2.8 \\\\\nFull OCC (BN) & 3 & --- & 0.725 $\\pm$ 0.064 & [0.654, 0.776] & $-$4.3 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\\nCutoff@15K$^\\ddagger$   & 2 & 0.883 $\\pm$ 0.041 & 0.782 $\\pm$ 0.031 & --- & $+$0.2 \\\\\nCutoff@25K$^\\ddagger$   & 2 & 0.887 $\\pm$ 0.061 & 0.724 $\\pm$ 0.051 & --- & $-$5.6 \\\\\nCutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\\nCutoff@45K$^\\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\\\\nReverse Cutoff$^\\ddagger$ & 2 & 0.839 $\\pm$ 0.072 & 0.718 $\\pm$ 0.025 & --- & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Normalization--Gradient Flow Interaction}\n\\label{sec:mechanism}\n\nThe four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). Within the fully v2 BN cells, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach OCC 0.767; Hedges' $g{=}-0.781$, $p{=}0.381$, bootstrap 95\\% CI $[-0.108, 0.014]$). The LN cells show the same directional pattern ($-$2.5\\,pp), yielding an ordinal interaction: gradient flow is detrimental regardless of normalization, and BatchNorm amplifies the damage.\n\n\\textbf{Ordinal, not additive.} Both BN and LN lines slope downward from Gradient OFF to Gradient ON; the lines do not cross (Figure~\\ref{fig:factorial}). With BN, gradient flow degrades CAR by $-$4.2\\,pp (Full OCC 0.725 vs.\\ Detach 0.767). With LN, gradient flow degrades CAR by $-$2.5\\,pp (Full OCC+LN 0.740 vs.\\ Detach+LN 0.765). The larger BN deficit suggests that BatchNorm statistics amplify the detrimental effect of auxiliary gradient flow on safety behavior.\n\n\\textbf{Full OCC (BN) is the worst and most unstable configuration.} Full OCC with BatchNorm and gradient flow (CAR 0.725) falls 4.3\\,pp below Vanilla, with cross-seed standard deviation of 0.064---nearly three times that of the other factorial cells ($\\sigma \\leq 0.024$). Individual seeds range from 0.654 to 0.776, indicating that the BN + gradient flow combination creates a volatile optimization landscape.\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. Both lines slope downward (ordinal interaction): gradient flow is detrimental, and BatchNorm amplifies the damage.}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (\\textbf{0.767}) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.740) & Detach+LN (0.765) & $-$2.5 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$1.5 & $+$0.2 & interaction: 1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Both lines slope downward: gradient flow degrades CAR under BN ($-$4.2\\,pp) and LN ($-$2.5\\,pp), an ordinal interaction. BatchNorm amplifies the damage. Error bars: cross-seed SD.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Gradient Dynamics}\n\\label{sec:gradient_dynamics}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Random OCC, Detach OCC). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1--13\\% of Vanilla. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d)~Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nFigure~\\ref{fig:gradient_analysis} examines gradient dynamics across conditions. All gradient norms are computed with respect to the L1 action loss (action tokens only), not the full language modeling objective.\n\n\\textbf{Gradient orthogonality.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\\ref{fig:gradient_analysis}c), with conflict rates of ${\\sim}$50\\%. This confirms that action and auxiliary gradients are orthogonal: direct gradient conflict is not the mechanism through which auxiliary heads affect safety. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (0.87--1.14$\\times$ Vanilla norms), which rules out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content does not affect outcomes.\n\n\\textbf{Mechanism remains open.} The ordinal interaction---gradient flow is detrimental, BatchNorm amplifies---cannot be explained by gradient conflict (orthogonality rules it out) or by gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape, but the precise mechanism requires further investigation.\n\n\\textbf{Representational structure is preserved across all conditions.} CKA between fine-tuned and pretrained encoder features shows that all conditions, including the worst-performing Full OCC (BN), maintain high similarity to the pretrained representations (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP encoders). The safety degradation under gradient flow therefore does not stem from representational corruption: the encoders retain their pretrained structure, yet the policy behaves less safely. This dissociation between representational fidelity and behavioral safety reinforces the conclusion that the detrimental effect operates through optimization dynamics rather than representation distortion.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
    "structuredPatch": [
      {
        "oldStart": 78,
        "oldLines": 7,
        "newStart": 78,
        "newLines": 7,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\textwidth]{figures/gradient_analysis_combined.pdf}",
          "-\\caption{Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Random OCC, Detach OCC). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1--13\\% of Vanilla. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d)~Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.}",
          "+\\caption{Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Random OCC, Detach OCC). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1--13\\% of Vanilla. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d)~Gradient norm ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.}",
          " \\label{fig:gradient_analysis}",
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

### Assistant

_source line 17_

两处修改完成：

1. **§4.2 统计量**（第46行）：`g=-1.023, p=0.422, CI [-0.001, 0.116]` → `g=-0.781, p=0.381, CI [-0.108, 0.014]`
2. **Fig 3 caption**（第81行）：`Gradient collapse ratio` → `Gradient norm ratio`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "uuid": "bd3f6afc-7ac9-41e2-b31c-f2a41a70d428",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSRMAjRMTCehKMNtVADSA5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 27770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 705
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

_source line 18_

两处修改完成：

1. **§4.2 统计量**（第46行）：`g=-1.023, p=0.422, CI [-0.001, 0.116]` → `g=-0.781, p=0.381, CI [-0.108, 0.014]`
2. **Fig 3 caption**（第81行）：`Gradient collapse ratio` → `Gradient norm ratio`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 23315,
  "duration_api_ms": 20843,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "3c378fea-6039-4c53-8406-be100db1b9d6",
  "total_cost_usd": 0.16927799999999998,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 16634,
    "cache_read_input_tokens": 63479,
    "output_tokens": 1266,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 16634,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 109,
        "cache_read_input_tokens": 27770,
        "cache_creation_input_tokens": 705,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 705
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1821,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001901,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 1266,
      "cacheReadInputTokens": 63479,
      "cacheCreationInputTokens": 16634,
      "webSearchRequests": 0,
      "costUSD": 0.16737699999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d019a1ca-165c-4957-a17b-6a83a13557ed"
}
```

</details>

---
