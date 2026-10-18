# paper atlas edd r1n1

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_atlas-edd-r1n1_20260515T155041.log`
- **Structured JSON:** [`699675563e056489d181.json`](../../sessions/69/699675563e056489d181.json)

## Before a recorded user message

27 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
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
  "uuid": "6be507dd-515e-4bb6-8e19-9fc9aff8979e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est/memory/"
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
    "resetsAt": 1778877600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4b4b2c30-57cb-473d-9ea0-61d40d2d034f",
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912"
}
```

---

### Assistant

_source line 4_

Let me start by reading the current atlas.tex file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "42261bbd-f8cf-4cee-98b9-16d1c8d35932",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe4RQafsB8ZGqPUX747esu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12248,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12248
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

<details open><summary>🔧 Tool call — Read · `toolu_014jcydfwXzzRsdyBXsdCCbK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "0a704c53-23ca-4134-b1b2-8ebc2006f94b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe4RQafsB8ZGqPUX747esu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12248,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12248
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

_source line 6 · 2026-05-15T15:50:50.808Z_

<details><summary>↩ Tool result · `toolu_014jcydfwXzzRsdyBXsdCCbK`</summary>

```text
1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\times$ 3 decoding strategies $\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.
5	For each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \S\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.
6	
7	\subsection{In-Distribution Performance}
8	\label{sec:atlas:indist}
9	
10	Table~\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.
11	All 9 cells exceed chance (25\%) by a wide margin, with accuracy ranging from 69.6\% to 85.4\%.
12	Both model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.
13	Top-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{In-distribution 4-class depth estimation accuracy (\%) across 3 model families $\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\%.}
19	\label{tab:main_matrix}
20	\begin{tabular}{lccc}
21	\toprule
22	Model & Nucleus & Temp & Top-$k$ \\
23	 & $p{=}0.95$ & $\tau{=}0.9$ & $k{=}50$ \\
24	\midrule
25	Pythia-1.4B & 78.2 & 76.3 & 69.6 \\
26	OLMo-1B & 78.8 & 82.0 & 74.2 \\
27	GPT-2 XL & 83.3 & \textbf{85.4} & 76.6 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	Because the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accuracy excluding d0.
33	Performance drops moderately---GPT-2~XL with temperature sampling still reaches 82.0\%, and even the weakest setting (Pythia nucleus) retains 70.8\%---confirming that the classifier captures inter-generation differences beyond the human--machine boundary.
34	
35	\subsection{Feature Universality}
36	\label{sec:atlas:features}
37	
38	To identify which statistical fingerprints carry depth signal, we train a dedicated binary RF per cell (d$_i$ vs.\ rest) and extract feature importances (Gini impurity; permutation importance yields consistent rankings, Appendix~\ref{app:permutation}).
39	Figure~\ref{fig:atlas_heatmap} visualizes the top-7 feature importances across all 9 cells.
40	
41	Two features dominate.
42	The 90th-percentile perplexity (\textsc{p90\_ppl}) ranks in the top 2 in all 9 cells, while surprisal variance (\textsc{var\_surprisal}) does so in 7 of 9.
43	In the two exceptions---GPT-2~XL with temperature and top-$k$ sampling---the 75th-percentile perplexity (\textsc{p75\_ppl}) replaces surprisal variance in the top 2, though surprisal variance remains among the top 4 features.
44	To quantify cross-model agreement, we compute the Spearman rank correlation of the full 19-feature importance vectors across all $\binom{9}{2}=36$ cell pairs and obtain a mean $\rho = 0.868$ (range: 0.619--0.954).
45	
46	\begin{figure}[t]
47	\centering
48	\includegraphics[width=\columnwidth]{../../figures/paper/fig_atlas_heatmap.pdf}
49	\caption{Feature importance heatmap across 9 cells (3 models $\times$ 3 strategies). Top-7 features by mean importance. \textsc{p90\_ppl} appears in the top 2 for all cells; \textsc{var\_surprisal} for 7 of 9.}
50	\label{fig:atlas_heatmap}
51	\end{figure}
52	
53	These results align with theoretical predictions: recursive finetuning erodes the tail of the token-probability distribution \cite{shumailov2024_nature,dohmatob2024_tale_of_tails}, and high-percentile perplexity directly measures tail behavior.
54	The universality of these markers across architectures and decoding strategies suggests they reflect a structural property of the recursive generation process rather than model-specific artifacts.
55	
56	\subsection{Effective Discriminable Depth}
57	\label{sec:atlas:edd}
58	
59	Aggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \emph{Effective Discriminable Depth} (EDD).
60	For each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\mathrm{AUC}(d, d{+}1)$ (Eq.~\ref{eq:edd}).
61	We set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \in \{0.65, 0.70, 0.75, 0.80\}$ below.
62	
63	Within the 4-class atlas (d0--d3), 7 of 9 cells achieve $\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \S\ref{sec:atlas:indist}.
64	
65	We extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair.
66	Figure~\ref{fig:auc_decay} shows the pairwise AUC decay curve.
67	The d0\,vs.\,d1 boundary is near-perfect (AUC\,=\,0.998), reflecting the well-known human--machine gap.
68	Subsequent boundaries degrade monotonically: d1\,vs.\,d2 achieves 0.925 [95\% CI: 0.914,\,0.935], d2\,vs.\,d3 reaches 0.823 [0.805,\,0.840], and d3\,vs.\,d4 yields 0.784 [0.765,\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.
69	At d4\,vs.\,d5, AUC drops to 0.683 [0.661,\,0.705], falling below the threshold and fixing $\mathrm{EDD}_{0.75}=4$.
70	
71	\paragraph{Cross-model EDD.}
72	We extend the same d0--d5 pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).
73	The d3\,vs.\,d4 AUC consistently clusters near the 0.75 threshold: Pythia 0.784 ($p{=}0.001$), OLMo 0.765 ($p{=}0.091$, marginal), GPT-2~XL 0.750 ($p{=}0.505$, n.s.)---only Pythia achieves conventional significance, yet all three exhibit the same directional pattern.
74	At d4\,vs.\,d5, AUC uniformly drops below 0.70 (Pythia 0.683, OLMo 0.684, GPT-2~XL 0.681), fixing $\mathrm{EDD}_{0.75}{=}4$ for all three models.
75	This cross-model EDD is stable across threshold choices: all three yield $\mathrm{EDD}{=}5$ at $T{=}0.65$, $\mathrm{EDD}{=}4$ at $T \in \{0.70, 0.75\}$, and $\mathrm{EDD}{=}3$ at $T{=}0.80$, matching the single-model pattern in Table~\ref{tab:edd_sensitivity}.
76	
77	\begin{figure}[t]
78	\centering
79	\includegraphics[width=\columnwidth]{../../figures/paper/fig_auc_decay.pdf}
80	\caption{Binary pairwise AUC between adjacent depths (Pythia-1.4B, nucleus $p{=}0.95$, d0--d5). Shaded bands: 95\% bootstrap CI. Dashed line: $T{=}0.75$. $\mathrm{EDD}_{0.75}=4$: depth pairs up to d3\,vs.\,d4 remain discriminable.}
81	\label{fig:auc_decay}
82	\end{figure}
83	
84	Table~\ref{tab:edd_sensitivity} shows the sensitivity of EDD to the choice of threshold.
85	At $T{=}0.65$, all pairs through d4\,vs.\,d5 pass, giving $\mathrm{EDD}=5$.
86	At $T{=}0.80$, only d1\,vs.\,d2 and d2\,vs.\,d3 pass, yielding $\mathrm{EDD}=3$.
87	The d0\,vs.\,d1 pair passes at every threshold ($\text{AUC}\geq0.99$).
88	
89	\begin{table}[t]
90	\centering
91	\small
92	\caption{EDD sensitivity to threshold $T$ (Pythia-1.4B, nucleus $p{=}0.95$). \checkmark: pairwise AUC $\geq T$; ---: below $T$. d0\,vs.\,d1 always passes (AUC$\geq$0.99) and is omitted.}
93	\label{tab:edd_sensitivity}
94	\begin{tabular}{cccccr}
95	\toprule
96	$T$ & d1/d2 & d2/d3 & d3/d4 & d4/d5 & EDD \\
97	\midrule
98	0.65 & \checkmark & \checkmark & \checkmark & \checkmark & 5 \\
99	0.70 & \checkmark & \checkmark & \checkmark & --- & 4 \\
100	0.75 & \checkmark & \checkmark & \checkmark & --- & 4 \\
101	0.80 & \checkmark & \checkmark & --- & --- & 3 \\
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	\paragraph{Granularity ablation.}
107	Decision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\% (binary) to 78.3\% (4-class) to 62.9\% (6-class), and the d2\,vs.\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\% relative decline attributable to boundary dilution, not signal loss.
108	
109	\subsection{Strategy-Dependent Trajectories}
110	\label{sec:atlas:trajectories}
111	
112	The atlas reveals that decoding strategy does not merely scale the overall signal strength---it reshapes the degradation trajectory.
113	Figure~\ref{fig:feature_trajectory} plots normalized feature means across depths for three key features.
114	
115	\begin{figure}[t]
116	\centering
117	\includegraphics[width=\columnwidth]{../../figures/paper/fig_feature_trajectory.pdf}
118	\caption{Normalized feature trajectories across generation depths for 3 models $\times$ 2 strategies (nucleus $p{=}0.95$, temperature $\tau{=}0.9$). All features decrease monotonically with depth, but inter-depth spacing is highly non-uniform. Top-$k$ results are provided in Appendix~\ref{app:topk_trajectories}.}
119	\label{fig:feature_trajectory}
120	\end{figure}
121	
122	\paragraph{Non-uniform inter-depth spacing.}
123	For Pythia nucleus, \textsc{p90\_ppl} drops from 483.7 (d0) to 61.4 (d1)---an 87\% reduction---but only from 29.7 (d2) to 18.2 (d3), a 39\% reduction.
124	This geometric compression of the feature space explains why adjacent-pair AUC decays monotonically (Figure~\ref{fig:auc_decay}): each successive generation step yields diminishing statistical displacement.
125	
126	\paragraph{Temperature-induced acceleration.}
127	Temperature sampling ($\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \citet{marchi2024_heat_death}.
128	Concretely, feature values at depth $N$ under temperature sampling approximate those at depth $N{+}1$ under nucleus or top-$k$.
129	This shift yields higher in-distribution accuracy (Table~\ref{tab:main_matrix}) because each depth occupies a more distinct region of feature space, but it also means the d1/d2 boundary under temperature is closer to the d2/d3 boundary under nucleus---a mismatch that creates reversal risk in cross-strategy transfer (\S\ref{sec:generalization}).
130	
131	\paragraph{Three-tier strategy taxonomy.}
132	The trajectory data suggests a functional classification.
133	Nucleus sampling ($p{=}0.95$) serves as a stable baseline with moderate signal strength.
134	Temperature sampling ($\tau{=}0.9$) enhances the signal via accelerated convergence, yielding higher within-strategy accuracy but strategy-specific depth boundaries.
135	Top-$k$ sampling ($k{=}50$) attenuates the signal---accuracy drops 6--9 points relative to nucleus---because hard truncation at a fixed vocabulary size preserves more of the original distribution's shape across depths, compressing inter-depth distances.
136	Notably, top-$k$ preserves the \emph{direction} of all feature trends despite the magnitude reduction, which has implications for ordinal classifiers that rely on monotonicity (\S\ref{sec:generalization}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "04287a04-a0f6-4b12-8d16-44ed80b37646",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
      "content": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\\times$ 3 decoding strategies $\\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.\nFor each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \\S\\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.\n\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:indist}\n\nTable~\\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.\nAll 9 cells exceed chance (25\\%) by a wide margin, with accuracy ranging from 69.6\\% to 85.4\\%.\nBoth model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.\nTop-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{In-distribution 4-class depth estimation accuracy (\\%) across 3 model families $\\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\\%.}\n\\label{tab:main_matrix}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Nucleus & Temp & Top-$k$ \\\\\n & $p{=}0.95$ & $\\tau{=}0.9$ & $k{=}50$ \\\\\n\\midrule\nPythia-1.4B & 78.2 & 76.3 & 69.6 \\\\\nOLMo-1B & 78.8 & 82.0 & 74.2 \\\\\nGPT-2 XL & 83.3 & \\textbf{85.4} & 76.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBecause the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accuracy excluding d0.\nPerformance drops moderately---GPT-2~XL with temperature sampling still reaches 82.0\\%, and even the weakest setting (Pythia nucleus) retains 70.8\\%---confirming that the classifier captures inter-generation differences beyond the human--machine boundary.\n\n\\subsection{Feature Universality}\n\\label{sec:atlas:features}\n\nTo identify which statistical fingerprints carry depth signal, we train a dedicated binary RF per cell (d$_i$ vs.\\ rest) and extract feature importances (Gini impurity; permutation importance yields consistent rankings, Appendix~\\ref{app:permutation}).\nFigure~\\ref{fig:atlas_heatmap} visualizes the top-7 feature importances across all 9 cells.\n\nTwo features dominate.\nThe 90th-percentile perplexity (\\textsc{p90\\_ppl}) ranks in the top 2 in all 9 cells, while surprisal variance (\\textsc{var\\_surprisal}) does so in 7 of 9.\nIn the two exceptions---GPT-2~XL with temperature and top-$k$ sampling---the 75th-percentile perplexity (\\textsc{p75\\_ppl}) replaces surprisal variance in the top 2, though surprisal variance remains among the top 4 features.\nTo quantify cross-model agreement, we compute the Spearman rank correlation of the full 19-feature importance vectors across all $\\binom{9}{2}=36$ cell pairs and obtain a mean $\\rho = 0.868$ (range: 0.619--0.954).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_atlas_heatmap.pdf}\n\\caption{Feature importance heatmap across 9 cells (3 models $\\times$ 3 strategies). Top-7 features by mean importance. \\textsc{p90\\_ppl} appears in the top 2 for all cells; \\textsc{var\\_surprisal} for 7 of 9.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\nThese results align with theoretical predictions: recursive finetuning erodes the tail of the token-probability distribution \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails}, and high-percentile perplexity directly measures tail behavior.\nThe universality of these markers across architectures and decoding strategies suggests they reflect a structural property of the recursive generation process rather than model-specific artifacts.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFor each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ (Eq.~\\ref{eq:edd}).\nWe set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ below.\n\nWithin the 4-class atlas (d0--d3), 7 of 9 cells achieve $\\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \\S\\ref{sec:atlas:indist}.\n\nWe extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair.\nFigure~\\ref{fig:auc_decay} shows the pairwise AUC decay curve.\nThe d0\\,vs.\\,d1 boundary is near-perfect (AUC\\,=\\,0.998), reflecting the well-known human--machine gap.\nSubsequent boundaries degrade monotonically: d1\\,vs.\\,d2 achieves 0.925 [95\\% CI: 0.914,\\,0.935], d2\\,vs.\\,d3 reaches 0.823 [0.805,\\,0.840], and d3\\,vs.\\,d4 yields 0.784 [0.765,\\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.\nAt d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling below the threshold and fixing $\\mathrm{EDD}_{0.75}=4$.\n\n\\paragraph{Cross-model EDD.}\nWe extend the same d0--d5 pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).\nThe d3\\,vs.\\,d4 AUC consistently clusters near the 0.75 threshold: Pythia 0.784 ($p{=}0.001$), OLMo 0.765 ($p{=}0.091$, marginal), GPT-2~XL 0.750 ($p{=}0.505$, n.s.)---only Pythia achieves conventional significance, yet all three exhibit the same directional pattern.\nAt d4\\,vs.\\,d5, AUC uniformly drops below 0.70 (Pythia 0.683, OLMo 0.684, GPT-2~XL 0.681), fixing $\\mathrm{EDD}_{0.75}{=}4$ for all three models.\nThis cross-model EDD is stable across threshold choices: all three yield $\\mathrm{EDD}{=}5$ at $T{=}0.65$, $\\mathrm{EDD}{=}4$ at $T \\in \\{0.70, 0.75\\}$, and $\\mathrm{EDD}{=}3$ at $T{=}0.80$, matching the single-model pattern in Table~\\ref{tab:edd_sensitivity}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_auc_decay.pdf}\n\\caption{Binary pairwise AUC between adjacent depths (Pythia-1.4B, nucleus $p{=}0.95$, d0--d5). Shaded bands: 95\\% bootstrap CI. Dashed line: $T{=}0.75$. $\\mathrm{EDD}_{0.75}=4$: depth pairs up to d3\\,vs.\\,d4 remain discriminable.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:edd_sensitivity} shows the sensitivity of EDD to the choice of threshold.\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$.\nAt $T{=}0.80$, only d1\\,vs.\\,d2 and d2\\,vs.\\,d3 pass, yielding $\\mathrm{EDD}=3$.\nThe d0\\,vs.\\,d1 pair passes at every threshold ($\\text{AUC}\\geq0.99$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EDD sensitivity to threshold $T$ (Pythia-1.4B, nucleus $p{=}0.95$). \\checkmark: pairwise AUC $\\geq T$; ---: below $T$. d0\\,vs.\\,d1 always passes (AUC$\\geq$0.99) and is omitted.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccccr}\n\\toprule\n$T$ & d1/d2 & d2/d3 & d3/d4 & d4/d5 & EDD \\\\\n\\midrule\n0.65 & \\checkmark & \\checkmark & \\checkmark & \\checkmark & 5 \\\\\n0.70 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.75 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.80 & \\checkmark & \\checkmark & --- & --- & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Granularity ablation.}\nDecision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class), and the d2\\,vs.\\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\\% relative decline attributable to boundary dilution, not signal loss.\n\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:trajectories}\n\nThe atlas reveals that decoding strategy does not merely scale the overall signal strength---it reshapes the degradation trajectory.\nFigure~\\ref{fig:feature_trajectory} plots normalized feature means across depths for three key features.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_feature_trajectory.pdf}\n\\caption{Normalized feature trajectories across generation depths for 3 models $\\times$ 2 strategies (nucleus $p{=}0.95$, temperature $\\tau{=}0.9$). All features decrease monotonically with depth, but inter-depth spacing is highly non-uniform. Top-$k$ results are provided in Appendix~\\ref{app:topk_trajectories}.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n\\paragraph{Non-uniform inter-depth spacing.}\nFor Pythia nucleus, \\textsc{p90\\_ppl} drops from 483.7 (d0) to 61.4 (d1)---an 87\\% reduction---but only from 29.7 (d2) to 18.2 (d3), a 39\\% reduction.\nThis geometric compression of the feature space explains why adjacent-pair AUC decays monotonically (Figure~\\ref{fig:auc_decay}): each successive generation step yields diminishing statistical displacement.\n\n\\paragraph{Temperature-induced acceleration.}\nTemperature sampling ($\\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \\citet{marchi2024_heat_death}.\nConcretely, feature values at depth $N$ under temperature sampling approximate those at depth $N{+}1$ under nucleus or top-$k$.\nThis shift yields higher in-distribution accuracy (Table~\\ref{tab:main_matrix}) because each depth occupies a more distinct region of feature space, but it also means the d1/d2 boundary under temperature is closer to the d2/d3 boundary under nucleus---a mismatch that creates reversal risk in cross-strategy transfer (\\S\\ref{sec:generalization}).\n\n\\paragraph{Three-tier strategy taxonomy.}\nThe trajectory data suggests a functional classification.\nNucleus sampling ($p{=}0.95$) serves as a stable baseline with moderate signal strength.\nTemperature sampling ($\\tau{=}0.9$) enhances the signal via accelerated convergence, yielding higher within-strategy accuracy but strategy-specific depth boundaries.\nTop-$k$ sampling ($k{=}50$) attenuates the signal---accuracy drops 6--9 points relative to nucleus---because hard truncation at a fixed vocabulary size preserves more of the original distribution's shape across depths, compressing inter-depth distances.\nNotably, top-$k$ preserves the \\emph{direction} of all feature trends despite the magnitude reduction, which has implications for ordinal classifiers that rely on monotonicity (\\S\\ref{sec:generalization}).",
      "numLines": 136,
      "startLine": 1,
      "totalLines": 136
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the current content and what needs to change:

1. **R1-N1: EDD formal math definition** - Need to add a formal equation for EDD_T. Currently line 60 references `Eq.~\ref{eq:edd}` but the equation isn't defined in this file. I need to add a formal equation block.

2. **D024/D027: EDD narrative from hard threshold to continuous decay** - Looking at the current text:
   - Line 69: "fixing $\mathrm{EDD}_{0.75}=4$" — this is a hard threshold statement
   - Line 74: "fixing $\mathrm{EDD}_{0.75}{=}4$ for all three models" — another hard threshold
   - Need to change the narrative to emphasize continuous decay, stratified statistical strength, directional consistency
   - Need to include bootstrap CI + p-values more prominently
   - The current text at line 73-74 already has some p-values but then says "fixing EDD=4 for all three"

3. **EDD Sensitivity Table** - Already exists (Table 2, lines 89-104) but only for Pythia. Need to extend to all three models.

4. **Decision boundary dilution** - Already mentioned at line 107 but briefly. Need to expand explanation.

Let me plan the revisions: I need to add the formal EDD equation definition, reframe the threshold language to emphasize continuous decay rather than fixed cutoffs, expand the sensitivity analysis across all models, and elaborate on the decision boundary dilution concept. the math and LaTeX formatting. I'm pulling together the binary pairwise AUC values across all three models—Pythia, GPT-2 XL, and OLMo—along with the statistical significance tests for the depth comparisons, particularly where the AUC drops off between d3v4 and d4v5.

Now I'm working through the EDD sensitivity analysis by testing each model's AUC thresholds across different T values to see how many depth comparisons pass at each threshold level. Wait, d2v3=0.823 ≥ 0.80 ✓, d3v4=0.784 < 0.80 ✗ → EDD=3

For GPT-2 XL: d1v2=0.966, d2v3=0.919, d3v4=0.750, d4v5=0.681
- T=0.65: all pass → EDD=5
- T=0.70: d4v5=0.681 < 0.70, rest pass (d3v4=0.750 ≥ 0.70) → EDD=4
- T=0.75: d3v4=0.750 ≥ 0.75 ✓, d4v5=0.681 < 0.75 → EDD=4
- T=0.80: d3v4=0.750 < 0.80 → EDD=3

For OLMo: d1v2=0.968, d2v3=0.843, d3v4=0.765, d4v5=0.684
- T=0.65: all pass → EDD=5
- T=0.70: d4v5=0.684 < 0.70, rest pass (d3v4=0.765 ≥ 0.70) → EDD=4
- T=0.75: d3v4=0.765 ≥ 0.75 ✓, d4v5=0.684 < 0.75 → EDD=4
- T=0.80: d3v4=0.765 < 0.80 → EDD=3

Across all three models, the pattern holds: EDD=5 at T=0.65, EDD=4 at T=0.70 and T=0.75, then EDD=3 at T=0.80.

The d0v1 pair consistently achieves AUC≥0.99 across all models, so it passes at every threshold. Now I need to draft the edits for the formal EDD definition—I should add it to the existing EDD section in §4.3, clarifying the mathematical formulation. I'm specifying the threshold value and justifying why we need dedicated binary classifiers rather than extracting results from a multi-class model, since the latter introduces decision boundary dilution that would underestimate discriminability. Extending the same pipeline to OLMo-1B and GPT-2 XL, I'm seeing that the d3 vs d4 AUC clusters consistently around 0.75 across all three models, though only Pythia reaches conventional significance while the others show the same directional trend. At d4 vs d5, the AUC drops uniformly below 0.70 across all models, establishing the EDD boundary. The AUC decay curves show a consistent monotonic pattern across all three models, with discriminability steadily eroding from d1–d2 (0.925–0.968) through d2–d3 (0.823–0.919) to d3–d4 clustering around 0.75, then collapsing below 0.70 at d4–d5 where no model maintains conventional statistical power. Bootstrap tests reveal that while all models show the same directional trend at the d3/d4 boundary, the statistical significance varies—Pythia achieves p=0.001, indicating a genuinely reliable separation point there. I need to expand the sensitivity analysis table to cover all three models across the different threshold values, not just Pythia. I should also soften the language around the hard threshold in the single-model section to be more consistent with avoiding deterministic claims. Let me plan out these edits carefully—adding the cross-model AUC table and making sure the sensitivity analysis captures the full range of thresholds for each model. I'm defining the EDD metric formally as the maximum depth where adjacent pairs maintain discriminability above a threshold, with each pair evaluated using a binary classifier's AUC score. The threshold defaults to 0.75—halfway between random guessing and perfect separation—and I'll test sensitivity across multiple threshold values.

The key insight is that these pairwise AUCs must come from dedicated binary classifiers rather than extracting them from a multi-class model, since the latter introduces decision boundary dilution that artificially inflates scores. For each adjacent depth pair, I'm training a separate random forest with 500 trees using 5-fold stratified cross-validation to compute the AUC, then applying the threshold to find where discrimination breaks down. I'm working through the edits systematically—I need to expand the granularity ablation section to better explain how decision boundary dilution affects performance across different class configurations, showing the accuracy and AUC degradation more clearly. I also realize the sensitivity table needs to cover all three models, not just Pythia, so I'll need to derive the EDD values for each model across the different T thresholds from the pairwise AUC data in the registry.

Computing EDD values for each model... I'm noticing all three models show the same EDD values across every threshold, which keeps the results straightforward. Now I need to figure out how to organize the edits—I should add a cross-model AUC table showing the full decay curves alongside what's already there. Let me map out where everything fits in section 4.3: the intro with EDD definition, the 4-class atlas results, the Pythia extension, the cross-model EDD paragraph, and the AUC decay figure.

For the new structure, I'm planning to add a formal equation to the intro, keep the atlas and Pythia results but soften the Pythia ending, rewrite the cross-model paragraph and insert that AUC table, expand the EDD sensitivity table to cover all three models, and add a decision boundary dilution paragraph with proper labeling. Let me start working through the specific edits sequentially.

For the first edit, I'm replacing the intro section with a version that includes the formal EDD equation and clarifies the binary pairwise requirement. The new text introduces the equation and explains how we compute AUC for each adjacent depth pair using a dedicated random forest, then sets the threshold at 0.75 as the default while noting sensitivity across other threshold values. the key insight is that I need to use dedicated binary classifiers for each adjacent depth pair rather than extracting discriminability from the multi-class model, since the latter suffers from decision boundary dilution. For each pair, I'm training a random forest with 500 trees using 5-fold stratified cross-validation to compute the AUC, and this approach reveals that discriminability drops below the 0.75 threshold between depths 4 and 5, establishing the effective depth as 4.

When I extend this same pipeline to OLMo-1B and GPT-2 XL, the pattern holds across models—the depth 3 vs. 4 boundary consistently hovers near the 0.75 threshold, though only Pythia reaches conventional statistical significance while the other models show marginal or non-significant results.

At the depth 4 vs. 5 comparison, all three models show a sharp drop below 0.70, converging on an EDD of 4 at the 0.75 threshold. What's striking is how stable this EDD estimate remains across different threshold choices: whether I set the threshold at 0.65, 0.70, 0.75, or 0.80, the models consistently yield the same sequence of EDD values, mirroring the single-model behavior. The statistical significance of this boundary differs markedly across models—Pythia shows a reliable separation ($p=0.001$), OLMo is marginal ($p=0.091$), and GPT-2~XL shows no significant difference ($p=0.505$)—which suggests I should treat EDD as a continuous decay profile rather than a discrete threshold, with the 0.75 AUC line marking a meaningful but not universal inflection point.

Generating markdown table... Generating markdown table... I'm realizing the task only provides AUC values for GPT-2 XL and OLMo, without confidence intervals like I have for Pythia. I should stick to what's actually given and either show just the point estimates for all models or note where CIs are unavailable.

Generating markdown table... Generating sensitivity table... Generating markdown table...

The granularity ablation reveals how decision boundary dilution degrades performance—accuracy plummets from 99.5% in the binary setting down to 78.3% with four classes and further to 62.9% with six classes, while the AUC between adjacent difficulty levels drops noticeably from 0.804 to 0.689 when moving from four-class to six-class discrimination. The accuracy metrics show a similar pattern—dropping from 99.5% in binary classification down to 78.3% with four classes and 62.9% with six—but since the underlying signal between adjacent depths remains constant, this degradation stems purely from boundary dilution rather than any loss of discriminative information. Binary pairwise classifiers sidestep this issue entirely, letting me measure the true pairwise separability that EDD is meant to capture.

Now I'm checking the cross-model AUC table and realizing I need to reference the specific experiment IDs from the task context for the Pythia, GPT-2 XL, and OLMo results, along with the granularity ablation run. The CI values are only available for Pythia, so I'll keep the table with point estimates as is and proceed with applying all the edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "e18fc31f-52be-47e2-981e-a9b10437f186",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mEhhX5bP16ktY7zR2pPzK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 24089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4089
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

_source line 8_

Now I'll apply the four required modifications. Let me make the edits sequentially.

**Edit 1: Add formal EDD equation (R1-N1)**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "1a1e196d-5046-45f9-a090-a2c7ce86d2a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mEhhX5bP16ktY7zR2pPzK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 24089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4089
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01AUQJgQuK6bDtSCS77Bf7E9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
  "old_string": "Aggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFor each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ (Eq.~\\ref{eq:edd}).\nWe set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ below.",
  "new_string": "Aggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFormally, given binary pairwise AUC scores for consecutive depth pairs:\n\\begin{equation}\n\\mathrm{EDD}_T \\;=\\; \\max\\bigl\\{d^* : \\mathrm{AUC}(d^*,\\, d^*{+}1) \\geq T\\bigr\\}\n\\label{eq:edd}\n\\end{equation}\nwhere $\\mathrm{AUC}(d, d{+}1)$ is the area under the ROC curve of a dedicated binary classifier distinguishing depth~$d$ from depth~$d{+}1$, and $T$ is the minimum AUC at which an adjacent pair is considered discriminable.\nWe adopt $T{=}0.75$ as default---the midpoint between chance (0.5) and perfect discrimination (1.0)---and report sensitivity across $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ in Table~\\ref{tab:edd_sensitivity}.\nCrucially, $\\mathrm{AUC}(d, d{+}1)$ must be estimated from a dedicated binary classifier rather than derived from a multi-class pipeline, as the latter suffers from decision boundary dilution (\\S\\ref{sec:atlas:edd:dilution}).\n\nFor each adjacent pair we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ per Eq.~\\ref{eq:edd}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "f932ff39-78d5-49ab-bd6f-e3e1bd421d84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mEhhX5bP16ktY7zR2pPzK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 24089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4089
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

_source line 10 · 2026-05-15T15:53:14.361Z_

<details><summary>↩ Tool result · `toolu_01AUQJgQuK6bDtSCS77Bf7E9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "8623d39a-27a0-427e-ab35-22af0e1fd3af",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
    "oldString": "Aggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFor each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ (Eq.~\\ref{eq:edd}).\nWe set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ below.",
    "newString": "Aggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFormally, given binary pairwise AUC scores for consecutive depth pairs:\n\\begin{equation}\n\\mathrm{EDD}_T \\;=\\; \\max\\bigl\\{d^* : \\mathrm{AUC}(d^*,\\, d^*{+}1) \\geq T\\bigr\\}\n\\label{eq:edd}\n\\end{equation}\nwhere $\\mathrm{AUC}(d, d{+}1)$ is the area under the ROC curve of a dedicated binary classifier distinguishing depth~$d$ from depth~$d{+}1$, and $T$ is the minimum AUC at which an adjacent pair is considered discriminable.\nWe adopt $T{=}0.75$ as default---the midpoint between chance (0.5) and perfect discrimination (1.0)---and report sensitivity across $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ in Table~\\ref{tab:edd_sensitivity}.\nCrucially, $\\mathrm{AUC}(d, d{+}1)$ must be estimated from a dedicated binary classifier rather than derived from a multi-class pipeline, as the latter suffers from decision boundary dilution (\\S\\ref{sec:atlas:edd:dilution}).\n\nFor each adjacent pair we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ per Eq.~\\ref{eq:edd}.",
    "originalFile": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\\times$ 3 decoding strategies $\\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.\nFor each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \\S\\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.\n\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:indist}\n\nTable~\\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.\nAll 9 cells exceed chance (25\\%) by a wide margin, with accuracy ranging from 69.6\\% to 85.4\\%.\nBoth model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.\nTop-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{In-distribution 4-class depth estimation accuracy (\\%) across 3 model families $\\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\\%.}\n\\label{tab:main_matrix}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Nucleus & Temp & Top-$k$ \\\\\n & $p{=}0.95$ & $\\tau{=}0.9$ & $k{=}50$ \\\\\n\\midrule\nPythia-1.4B & 78.2 & 76.3 & 69.6 \\\\\nOLMo-1B & 78.8 & 82.0 & 74.2 \\\\\nGPT-2 XL & 83.3 & \\textbf{85.4} & 76.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBecause the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accuracy excluding d0.\nPerformance drops moderately---GPT-2~XL with temperature sampling still reaches 82.0\\%, and even the weakest setting (Pythia nucleus) retains 70.8\\%---confirming that the classifier captures inter-generation differences beyond the human--machine boundary.\n\n\\subsection{Feature Universality}\n\\label{sec:atlas:features}\n\nTo identify which statistical fingerprints carry depth signal, we train a dedicated binary RF per cell (d$_i$ vs.\\ rest) and extract feature importances (Gini impurity; permutation importance yields consistent rankings, Appendix~\\ref{app:permutation}).\nFigure~\\ref{fig:atlas_heatmap} visualizes the top-7 feature importances across all 9 cells.\n\nTwo features dominate.\nThe 90th-percentile perplexity (\\textsc{p90\\_ppl}) ranks in the top 2 in all 9 cells, while surprisal variance (\\textsc{var\\_surprisal}) does so in 7 of 9.\nIn the two exceptions---GPT-2~XL with temperature and top-$k$ sampling---the 75th-percentile perplexity (\\textsc{p75\\_ppl}) replaces surprisal variance in the top 2, though surprisal variance remains among the top 4 features.\nTo quantify cross-model agreement, we compute the Spearman rank correlation of the full 19-feature importance vectors across all $\\binom{9}{2}=36$ cell pairs and obtain a mean $\\rho = 0.868$ (range: 0.619--0.954).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_atlas_heatmap.pdf}\n\\caption{Feature importance heatmap across 9 cells (3 models $\\times$ 3 strategies). Top-7 features by mean importance. \\textsc{p90\\_ppl} appears in the top 2 for all cells; \\textsc{var\\_surprisal} for 7 of 9.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\nThese results align with theoretical predictions: recursive finetuning erodes the tail of the token-probability distribution \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails}, and high-percentile perplexity directly measures tail behavior.\nThe universality of these markers across architectures and decoding strategies suggests they reflect a structural property of the recursive generation process rather than model-specific artifacts.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFor each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ (Eq.~\\ref{eq:edd}).\nWe set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ below.\n\nWithin the 4-class atlas (d0--d3), 7 of 9 cells achieve $\\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \\S\\ref{sec:atlas:indist}.\n\nWe extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair.\nFigure~\\ref{fig:auc_decay} shows the pairwise AUC decay curve.\nThe d0\\,vs.\\,d1 boundary is near-perfect (AUC\\,=\\,0.998), reflecting the well-known human--machine gap.\nSubsequent boundaries degrade monotonically: d1\\,vs.\\,d2 achieves 0.925 [95\\% CI: 0.914,\\,0.935], d2\\,vs.\\,d3 reaches 0.823 [0.805,\\,0.840], and d3\\,vs.\\,d4 yields 0.784 [0.765,\\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.\nAt d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling below the threshold and fixing $\\mathrm{EDD}_{0.75}=4$.\n\n\\paragraph{Cross-model EDD.}\nWe extend the same d0--d5 pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).\nThe d3\\,vs.\\,d4 AUC consistently clusters near the 0.75 threshold: Pythia 0.784 ($p{=}0.001$), OLMo 0.765 ($p{=}0.091$, marginal), GPT-2~XL 0.750 ($p{=}0.505$, n.s.)---only Pythia achieves conventional significance, yet all three exhibit the same directional pattern.\nAt d4\\,vs.\\,d5, AUC uniformly drops below 0.70 (Pythia 0.683, OLMo 0.684, GPT-2~XL 0.681), fixing $\\mathrm{EDD}_{0.75}{=}4$ for all three models.\nThis cross-model EDD is stable across threshold choices: all three yield $\\mathrm{EDD}{=}5$ at $T{=}0.65$, $\\mathrm{EDD}{=}4$ at $T \\in \\{0.70, 0.75\\}$, and $\\mathrm{EDD}{=}3$ at $T{=}0.80$, matching the single-model pattern in Table~\\ref{tab:edd_sensitivity}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_auc_decay.pdf}\n\\caption{Binary pairwise AUC between adjacent depths (Pythia-1.4B, nucleus $p{=}0.95$, d0--d5). Shaded bands: 95\\% bootstrap CI. Dashed line: $T{=}0.75$. $\\mathrm{EDD}_{0.75}=4$: depth pairs up to d3\\,vs.\\,d4 remain discriminable.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:edd_sensitivity} shows the sensitivity of EDD to the choice of threshold.\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$.\nAt $T{=}0.80$, only d1\\,vs.\\,d2 and d2\\,vs.\\,d3 pass, yielding $\\mathrm{EDD}=3$.\nThe d0\\,vs.\\,d1 pair passes at every threshold ($\\text{AUC}\\geq0.99$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EDD sensitivity to threshold $T$ (Pythia-1.4B, nucleus $p{=}0.95$). \\checkmark: pairwise AUC $\\geq T$; ---: below $T$. d0\\,vs.\\,d1 always passes (AUC$\\geq$0.99) and is omitted.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccccr}\n\\toprule\n$T$ & d1/d2 & d2/d3 & d3/d4 & d4/d5 & EDD \\\\\n\\midrule\n0.65 & \\checkmark & \\checkmark & \\checkmark & \\checkmark & 5 \\\\\n0.70 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.75 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.80 & \\checkmark & \\checkmark & --- & --- & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Granularity ablation.}\nDecision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class), and the d2\\,vs.\\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\\% relative decline attributable to boundary dilution, not signal loss.\n\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:trajectories}\n\nThe atlas reveals that decoding strategy does not merely scale the overall signal strength---it reshapes the degradation trajectory.\nFigure~\\ref{fig:feature_trajectory} plots normalized feature means across depths for three key features.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_feature_trajectory.pdf}\n\\caption{Normalized feature trajectories across generation depths for 3 models $\\times$ 2 strategies (nucleus $p{=}0.95$, temperature $\\tau{=}0.9$). All features decrease monotonically with depth, but inter-depth spacing is highly non-uniform. Top-$k$ results are provided in Appendix~\\ref{app:topk_trajectories}.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n\\paragraph{Non-uniform inter-depth spacing.}\nFor Pythia nucleus, \\textsc{p90\\_ppl} drops from 483.7 (d0) to 61.4 (d1)---an 87\\% reduction---but only from 29.7 (d2) to 18.2 (d3), a 39\\% reduction.\nThis geometric compression of the feature space explains why adjacent-pair AUC decays monotonically (Figure~\\ref{fig:auc_decay}): each successive generation step yields diminishing statistical displacement.\n\n\\paragraph{Temperature-induced acceleration.}\nTemperature sampling ($\\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \\citet{marchi2024_heat_death}.\nConcretely, feature values at depth $N$ under temperature sampling approximate those at depth $N{+}1$ under nucleus or top-$k$.\nThis shift yields higher in-distribution accuracy (Table~\\ref{tab:main_matrix}) because each depth occupies a more distinct region of feature space, but it also means the d1/d2 boundary under temperature is closer to the d2/d3 boundary under nucleus---a mismatch that creates reversal risk in cross-strategy transfer (\\S\\ref{sec:generalization}).\n\n\\paragraph{Three-tier strategy taxonomy.}\nThe trajectory data suggests a functional classification.\nNucleus sampling ($p{=}0.95$) serves as a stable baseline with moderate signal strength.\nTemperature sampling ($\\tau{=}0.9$) enhances the signal via accelerated convergence, yielding higher within-strategy accuracy but strategy-specific depth boundaries.\nTop-$k$ sampling ($k{=}50$) attenuates the signal---accuracy drops 6--9 points relative to nucleus---because hard truncation at a fixed vocabulary size preserves more of the original distribution's shape across depths, compressing inter-depth distances.\nNotably, top-$k$ preserves the \\emph{direction} of all feature trends despite the magnitude reduction, which has implications for ordinal classifiers that rely on monotonicity (\\S\\ref{sec:generalization}).",
    "structuredPatch": [
      {
        "oldStart": 57,
        "oldLines": 9,
        "newStart": 57,
        "newLines": 17,
        "lines": [
          " \\label{sec:atlas:edd}",
          " ",
          " Aggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \\emph{Effective Discriminable Depth} (EDD).",
          "-For each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ (Eq.~\\ref{eq:edd}).",
          "-We set $T{=}0.75$ as the default threshold---the midpoint between chance AUC (0.5) and perfect discrimination (1.0)---and report sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ below.",
          "+Formally, given binary pairwise AUC scores for consecutive depth pairs:",
          "+\\begin{equation}",
          "+\\mathrm{EDD}_T \\;=\\; \\max\\bigl\\{d^* : \\mathrm{AUC}(d^*,\\, d^*{+}1) \\geq T\\bigr\\}",
          "+\\label{eq:edd}",
          "+\\end{equation}",
          "+where $\\mathrm{AUC}(d, d{+}1)$ is the area under the ROC curve of a dedicated binary classifier distinguishing depth~$d$ from depth~$d{+}1$, and $T$ is the minimum AUC at which an adjacent pair is considered discriminable.",
          "+We adopt $T{=}0.75$ as default---the midpoint between chance (0.5) and perfect discrimination (1.0)---and report sensitivity across $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ in Table~\\ref{tab:edd_sensitivity}.",
          "+Crucially, $\\mathrm{AUC}(d, d{+}1)$ must be estimated from a dedicated binary classifier rather than derived from a multi-class pipeline, as the latter suffers from decision boundary dilution (\\S\\ref{sec:atlas:edd:dilution}).",
          " ",
          "+For each adjacent pair we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ per Eq.~\\ref{eq:edd}.",
          "+",
          " Within the 4-class atlas (d0--d3), 7 of 9 cells achieve $\\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \\S\\ref{sec:atlas:indist}.",
          " ",
          " We extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair."
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

_source line 11_

**Edit 2: Soften Pythia single-model conclusion**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "2d8a46b4-c276-4556-b969-9216a4709911",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHUBa64rRP32EygKT6ZZmg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10990,
      "cache_read_input_tokens": 28178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10990
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

_source line 12_

<details open><summary>🔧 Tool call — Edit · `toolu_01272bXmeUJFTsqQXyeB4QNC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
  "old_string": "At d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling below the threshold and fixing $\\mathrm{EDD}_{0.75}=4$.",
  "new_string": "At d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling decisively below $T{=}0.75$ and placing $\\mathrm{EDD}_{0.75}$ at~4 for this configuration."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "167b52e9-a250-4f38-a2cf-776e429b96e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHUBa64rRP32EygKT6ZZmg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10990,
      "cache_read_input_tokens": 28178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10990
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

_source line 13 · 2026-05-15T15:53:20.202Z_

<details><summary>↩ Tool result · `toolu_01272bXmeUJFTsqQXyeB4QNC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "6e898db0-ca06-47ab-8f23-ccd6cfd737fc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
    "oldString": "At d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling below the threshold and fixing $\\mathrm{EDD}_{0.75}=4$.",
    "newString": "At d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling decisively below $T{=}0.75$ and placing $\\mathrm{EDD}_{0.75}$ at~4 for this configuration.",
    "originalFile": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\\times$ 3 decoding strategies $\\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.\nFor each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \\S\\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.\n\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:indist}\n\nTable~\\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.\nAll 9 cells exceed chance (25\\%) by a wide margin, with accuracy ranging from 69.6\\% to 85.4\\%.\nBoth model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.\nTop-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{In-distribution 4-class depth estimation accuracy (\\%) across 3 model families $\\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\\%.}\n\\label{tab:main_matrix}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Nucleus & Temp & Top-$k$ \\\\\n & $p{=}0.95$ & $\\tau{=}0.9$ & $k{=}50$ \\\\\n\\midrule\nPythia-1.4B & 78.2 & 76.3 & 69.6 \\\\\nOLMo-1B & 78.8 & 82.0 & 74.2 \\\\\nGPT-2 XL & 83.3 & \\textbf{85.4} & 76.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBecause the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accuracy excluding d0.\nPerformance drops moderately---GPT-2~XL with temperature sampling still reaches 82.0\\%, and even the weakest setting (Pythia nucleus) retains 70.8\\%---confirming that the classifier captures inter-generation differences beyond the human--machine boundary.\n\n\\subsection{Feature Universality}\n\\label{sec:atlas:features}\n\nTo identify which statistical fingerprints carry depth signal, we train a dedicated binary RF per cell (d$_i$ vs.\\ rest) and extract feature importances (Gini impurity; permutation importance yields consistent rankings, Appendix~\\ref{app:permutation}).\nFigure~\\ref{fig:atlas_heatmap} visualizes the top-7 feature importances across all 9 cells.\n\nTwo features dominate.\nThe 90th-percentile perplexity (\\textsc{p90\\_ppl}) ranks in the top 2 in all 9 cells, while surprisal variance (\\textsc{var\\_surprisal}) does so in 7 of 9.\nIn the two exceptions---GPT-2~XL with temperature and top-$k$ sampling---the 75th-percentile perplexity (\\textsc{p75\\_ppl}) replaces surprisal variance in the top 2, though surprisal variance remains among the top 4 features.\nTo quantify cross-model agreement, we compute the Spearman rank correlation of the full 19-feature importance vectors across all $\\binom{9}{2}=36$ cell pairs and obtain a mean $\\rho = 0.868$ (range: 0.619--0.954).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_atlas_heatmap.pdf}\n\\caption{Feature importance heatmap across 9 cells (3 models $\\times$ 3 strategies). Top-7 features by mean importance. \\textsc{p90\\_ppl} appears in the top 2 for all cells; \\textsc{var\\_surprisal} for 7 of 9.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\nThese results align with theoretical predictions: recursive finetuning erodes the tail of the token-probability distribution \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails}, and high-percentile perplexity directly measures tail behavior.\nThe universality of these markers across architectures and decoding strategies suggests they reflect a structural property of the recursive generation process rather than model-specific artifacts.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFormally, given binary pairwise AUC scores for consecutive depth pairs:\n\\begin{equation}\n\\mathrm{EDD}_T \\;=\\; \\max\\bigl\\{d^* : \\mathrm{AUC}(d^*,\\, d^*{+}1) \\geq T\\bigr\\}\n\\label{eq:edd}\n\\end{equation}\nwhere $\\mathrm{AUC}(d, d{+}1)$ is the area under the ROC curve of a dedicated binary classifier distinguishing depth~$d$ from depth~$d{+}1$, and $T$ is the minimum AUC at which an adjacent pair is considered discriminable.\nWe adopt $T{=}0.75$ as default---the midpoint between chance (0.5) and perfect discrimination (1.0)---and report sensitivity across $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ in Table~\\ref{tab:edd_sensitivity}.\nCrucially, $\\mathrm{AUC}(d, d{+}1)$ must be estimated from a dedicated binary classifier rather than derived from a multi-class pipeline, as the latter suffers from decision boundary dilution (\\S\\ref{sec:atlas:edd:dilution}).\n\nFor each adjacent pair we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ per Eq.~\\ref{eq:edd}.\n\nWithin the 4-class atlas (d0--d3), 7 of 9 cells achieve $\\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \\S\\ref{sec:atlas:indist}.\n\nWe extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair.\nFigure~\\ref{fig:auc_decay} shows the pairwise AUC decay curve.\nThe d0\\,vs.\\,d1 boundary is near-perfect (AUC\\,=\\,0.998), reflecting the well-known human--machine gap.\nSubsequent boundaries degrade monotonically: d1\\,vs.\\,d2 achieves 0.925 [95\\% CI: 0.914,\\,0.935], d2\\,vs.\\,d3 reaches 0.823 [0.805,\\,0.840], and d3\\,vs.\\,d4 yields 0.784 [0.765,\\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.\nAt d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling below the threshold and fixing $\\mathrm{EDD}_{0.75}=4$.\n\n\\paragraph{Cross-model EDD.}\nWe extend the same d0--d5 pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).\nThe d3\\,vs.\\,d4 AUC consistently clusters near the 0.75 threshold: Pythia 0.784 ($p{=}0.001$), OLMo 0.765 ($p{=}0.091$, marginal), GPT-2~XL 0.750 ($p{=}0.505$, n.s.)---only Pythia achieves conventional significance, yet all three exhibit the same directional pattern.\nAt d4\\,vs.\\,d5, AUC uniformly drops below 0.70 (Pythia 0.683, OLMo 0.684, GPT-2~XL 0.681), fixing $\\mathrm{EDD}_{0.75}{=}4$ for all three models.\nThis cross-model EDD is stable across threshold choices: all three yield $\\mathrm{EDD}{=}5$ at $T{=}0.65$, $\\mathrm{EDD}{=}4$ at $T \\in \\{0.70, 0.75\\}$, and $\\mathrm{EDD}{=}3$ at $T{=}0.80$, matching the single-model pattern in Table~\\ref{tab:edd_sensitivity}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_auc_decay.pdf}\n\\caption{Binary pairwise AUC between adjacent depths (Pythia-1.4B, nucleus $p{=}0.95$, d0--d5). Shaded bands: 95\\% bootstrap CI. Dashed line: $T{=}0.75$. $\\mathrm{EDD}_{0.75}=4$: depth pairs up to d3\\,vs.\\,d4 remain discriminable.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:edd_sensitivity} shows the sensitivity of EDD to the choice of threshold.\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$.\nAt $T{=}0.80$, only d1\\,vs.\\,d2 and d2\\,vs.\\,d3 pass, yielding $\\mathrm{EDD}=3$.\nThe d0\\,vs.\\,d1 pair passes at every threshold ($\\text{AUC}\\geq0.99$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EDD sensitivity to threshold $T$ (Pythia-1.4B, nucleus $p{=}0.95$). \\checkmark: pairwise AUC $\\geq T$; ---: below $T$. d0\\,vs.\\,d1 always passes (AUC$\\geq$0.99) and is omitted.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccccr}\n\\toprule\n$T$ & d1/d2 & d2/d3 & d3/d4 & d4/d5 & EDD \\\\\n\\midrule\n0.65 & \\checkmark & \\checkmark & \\checkmark & \\checkmark & 5 \\\\\n0.70 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.75 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.80 & \\checkmark & \\checkmark & --- & --- & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Granularity ablation.}\nDecision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class), and the d2\\,vs.\\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\\% relative decline attributable to boundary dilution, not signal loss.\n\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:trajectories}\n\nThe atlas reveals that decoding strategy does not merely scale the overall signal strength---it reshapes the degradation trajectory.\nFigure~\\ref{fig:feature_trajectory} plots normalized feature means across depths for three key features.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_feature_trajectory.pdf}\n\\caption{Normalized feature trajectories across generation depths for 3 models $\\times$ 2 strategies (nucleus $p{=}0.95$, temperature $\\tau{=}0.9$). All features decrease monotonically with depth, but inter-depth spacing is highly non-uniform. Top-$k$ results are provided in Appendix~\\ref{app:topk_trajectories}.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n\\paragraph{Non-uniform inter-depth spacing.}\nFor Pythia nucleus, \\textsc{p90\\_ppl} drops from 483.7 (d0) to 61.4 (d1)---an 87\\% reduction---but only from 29.7 (d2) to 18.2 (d3), a 39\\% reduction.\nThis geometric compression of the feature space explains why adjacent-pair AUC decays monotonically (Figure~\\ref{fig:auc_decay}): each successive generation step yields diminishing statistical displacement.\n\n\\paragraph{Temperature-induced acceleration.}\nTemperature sampling ($\\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \\citet{marchi2024_heat_death}.\nConcretely, feature values at depth $N$ under temperature sampling approximate those at depth $N{+}1$ under nucleus or top-$k$.\nThis shift yields higher in-distribution accuracy (Table~\\ref{tab:main_matrix}) because each depth occupies a more distinct region of feature space, but it also means the d1/d2 boundary under temperature is closer to the d2/d3 boundary under nucleus---a mismatch that creates reversal risk in cross-strategy transfer (\\S\\ref{sec:generalization}).\n\n\\paragraph{Three-tier strategy taxonomy.}\nThe trajectory data suggests a functional classification.\nNucleus sampling ($p{=}0.95$) serves as a stable baseline with moderate signal strength.\nTemperature sampling ($\\tau{=}0.9$) enhances the signal via accelerated convergence, yielding higher within-strategy accuracy but strategy-specific depth boundaries.\nTop-$k$ sampling ($k{=}50$) attenuates the signal---accuracy drops 6--9 points relative to nucleus---because hard truncation at a fixed vocabulary size preserves more of the original distribution's shape across depths, compressing inter-depth distances.\nNotably, top-$k$ preserves the \\emph{direction} of all feature trends despite the magnitude reduction, which has implications for ordinal classifiers that rely on monotonicity (\\S\\ref{sec:generalization}).",
    "structuredPatch": [
      {
        "oldStart": 74,
        "oldLines": 7,
        "newStart": 74,
        "newLines": 7,
        "lines": [
          " Figure~\\ref{fig:auc_decay} shows the pairwise AUC decay curve.",
          " The d0\\,vs.\\,d1 boundary is near-perfect (AUC\\,=\\,0.998), reflecting the well-known human--machine gap.",
          " Subsequent boundaries degrade monotonically: d1\\,vs.\\,d2 achieves 0.925 [95\\% CI: 0.914,\\,0.935], d2\\,vs.\\,d3 reaches 0.823 [0.805,\\,0.840], and d3\\,vs.\\,d4 yields 0.784 [0.765,\\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.",
          "-At d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling below the threshold and fixing $\\mathrm{EDD}_{0.75}=4$.",
          "+At d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling decisively below $T{=}0.75$ and placing $\\mathrm{EDD}_{0.75}$ at~4 for this configuration.",
          " ",
          " \\paragraph{Cross-model EDD.}",
          " We extend the same d0--d5 pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$)."
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

_source line 14_

**Edit 3: Rewrite cross-model paragraph with continuous decay narrative + AUC table**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "e64f2f78-33f2-40e3-bbd9-a42263172f04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Joy8181RwBhm5nzaja5mew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 39168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 340
      },
      "output_tokens": 7,
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_011aH9zn8nNfDMu2WfFB15KD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
  "old_string": "\\paragraph{Cross-model EDD.}\nWe extend the same d0--d5 pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).\nThe d3\\,vs.\\,d4 AUC consistently clusters near the 0.75 threshold: Pythia 0.784 ($p{=}0.001$), OLMo 0.765 ($p{=}0.091$, marginal), GPT-2~XL 0.750 ($p{=}0.505$, n.s.)---only Pythia achieves conventional significance, yet all three exhibit the same directional pattern.\nAt d4\\,vs.\\,d5, AUC uniformly drops below 0.70 (Pythia 0.683, OLMo 0.684, GPT-2~XL 0.681), fixing $\\mathrm{EDD}_{0.75}{=}4$ for all three models.\nThis cross-model EDD is stable across threshold choices: all three yield $\\mathrm{EDD}{=}5$ at $T{=}0.65$, $\\mathrm{EDD}{=}4$ at $T \\in \\{0.70, 0.75\\}$, and $\\mathrm{EDD}{=}3$ at $T{=}0.80$, matching the single-model pattern in Table~\\ref{tab:edd_sensitivity}.",
  "new_string": "\\paragraph{Cross-model AUC decay.}\nWe extend the d0--d5 binary pairwise pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).\nTable~\\ref{tab:cross_model_auc} reports the full decay curves.\nAll three models exhibit monotonic AUC decline with a characteristic inflection: d1\\,vs.\\,d2 AUC ranges from 0.925 to 0.968, d2\\,vs.\\,d3 from 0.823 to 0.919, and d3\\,vs.\\,d4 clusters tightly near 0.75 (range 0.750--0.784).\nAt d4\\,vs.\\,d5, AUC uniformly falls below 0.70 (range 0.681--0.684), with no model sustaining discriminability at conventional thresholds.\n\nThe statistical strength of the d3\\,vs.\\,d4 boundary varies across models despite directional agreement.\nBootstrap permutation tests comparing $\\mathrm{AUC}(d3,d4)$ and $\\mathrm{AUC}(d4,d5)$ yield $p{=}0.001$ for Pythia (the d3/d4 margin is reliably above d4/d5), $p{=}0.091$ for OLMo (marginal), and $p{=}0.505$ for GPT-2~XL (not statistically significant).\nThis stratification reflects the tightness of the AUC gap: all three models place d3\\,vs.\\,d4 above and d4\\,vs.\\,d5 below the $T{=}0.75$ line, but only Pythia's margin is large enough for conventional significance.\nWe therefore interpret EDD as a continuous decay profile rather than a single integer, noting that $\\mathrm{EDD}_{0.75}$ coincides at~4 across all three models while the underlying confidence varies substantially.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Binary pairwise AUC for adjacent depths across three models (nucleus $p{=}0.95$, d0--d5). d0\\,vs.\\,d1 omitted (AUC$\\geq$0.99 for all). $p$: bootstrap permutation test of $\\mathrm{AUC}(d3,d4) > \\mathrm{AUC}(d4,d5)$. Experiment IDs: \\texttt{depth\\_extension\\_binary\\_pairwise\\_002}, \\texttt{depth\\_extension\\_gpt2xl\\_d4d5\\_001}, \\texttt{depth\\_extension\\_olmo\\_d4d5\\_002}.}\n\\label{tab:cross_model_auc}\n\\begin{tabular}{lccccl}\n\\toprule\nModel & d1/d2 & d2/d3 & d3/d4 & d4/d5 & $p$ \\\\\n\\midrule\nPythia-1.4B & .925 & .823 & .784 & .683 & .001 \\\\\nGPT-2 XL & .966 & .919 & .750 & .681 & .505 \\\\\nOLMo-1B & .968 & .843 & .765 & .684 & .091 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "e20c2a42-097e-4ff8-b977-59001ccbfcce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Joy8181RwBhm5nzaja5mew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 39168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 340
      },
      "output_tokens": 7,
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

_source line 16 · 2026-05-15T15:53:41.187Z_

<details><summary>↩ Tool result · `toolu_011aH9zn8nNfDMu2WfFB15KD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "ea33d945-562a-4c45-bbbb-29ec7854506c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
    "oldString": "\\paragraph{Cross-model EDD.}\nWe extend the same d0--d5 pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).\nThe d3\\,vs.\\,d4 AUC consistently clusters near the 0.75 threshold: Pythia 0.784 ($p{=}0.001$), OLMo 0.765 ($p{=}0.091$, marginal), GPT-2~XL 0.750 ($p{=}0.505$, n.s.)---only Pythia achieves conventional significance, yet all three exhibit the same directional pattern.\nAt d4\\,vs.\\,d5, AUC uniformly drops below 0.70 (Pythia 0.683, OLMo 0.684, GPT-2~XL 0.681), fixing $\\mathrm{EDD}_{0.75}{=}4$ for all three models.\nThis cross-model EDD is stable across threshold choices: all three yield $\\mathrm{EDD}{=}5$ at $T{=}0.65$, $\\mathrm{EDD}{=}4$ at $T \\in \\{0.70, 0.75\\}$, and $\\mathrm{EDD}{=}3$ at $T{=}0.80$, matching the single-model pattern in Table~\\ref{tab:edd_sensitivity}.",
    "newString": "\\paragraph{Cross-model AUC decay.}\nWe extend the d0--d5 binary pairwise pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).\nTable~\\ref{tab:cross_model_auc} reports the full decay curves.\nAll three models exhibit monotonic AUC decline with a characteristic inflection: d1\\,vs.\\,d2 AUC ranges from 0.925 to 0.968, d2\\,vs.\\,d3 from 0.823 to 0.919, and d3\\,vs.\\,d4 clusters tightly near 0.75 (range 0.750--0.784).\nAt d4\\,vs.\\,d5, AUC uniformly falls below 0.70 (range 0.681--0.684), with no model sustaining discriminability at conventional thresholds.\n\nThe statistical strength of the d3\\,vs.\\,d4 boundary varies across models despite directional agreement.\nBootstrap permutation tests comparing $\\mathrm{AUC}(d3,d4)$ and $\\mathrm{AUC}(d4,d5)$ yield $p{=}0.001$ for Pythia (the d3/d4 margin is reliably above d4/d5), $p{=}0.091$ for OLMo (marginal), and $p{=}0.505$ for GPT-2~XL (not statistically significant).\nThis stratification reflects the tightness of the AUC gap: all three models place d3\\,vs.\\,d4 above and d4\\,vs.\\,d5 below the $T{=}0.75$ line, but only Pythia's margin is large enough for conventional significance.\nWe therefore interpret EDD as a continuous decay profile rather than a single integer, noting that $\\mathrm{EDD}_{0.75}$ coincides at~4 across all three models while the underlying confidence varies substantially.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Binary pairwise AUC for adjacent depths across three models (nucleus $p{=}0.95$, d0--d5). d0\\,vs.\\,d1 omitted (AUC$\\geq$0.99 for all). $p$: bootstrap permutation test of $\\mathrm{AUC}(d3,d4) > \\mathrm{AUC}(d4,d5)$. Experiment IDs: \\texttt{depth\\_extension\\_binary\\_pairwise\\_002}, \\texttt{depth\\_extension\\_gpt2xl\\_d4d5\\_001}, \\texttt{depth\\_extension\\_olmo\\_d4d5\\_002}.}\n\\label{tab:cross_model_auc}\n\\begin{tabular}{lccccl}\n\\toprule\nModel & d1/d2 & d2/d3 & d3/d4 & d4/d5 & $p$ \\\\\n\\midrule\nPythia-1.4B & .925 & .823 & .784 & .683 & .001 \\\\\nGPT-2 XL & .966 & .919 & .750 & .681 & .505 \\\\\nOLMo-1B & .968 & .843 & .765 & .684 & .091 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
    "originalFile": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\\times$ 3 decoding strategies $\\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.\nFor each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \\S\\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.\n\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:indist}\n\nTable~\\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.\nAll 9 cells exceed chance (25\\%) by a wide margin, with accuracy ranging from 69.6\\% to 85.4\\%.\nBoth model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.\nTop-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{In-distribution 4-class depth estimation accuracy (\\%) across 3 model families $\\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\\%.}\n\\label{tab:main_matrix}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Nucleus & Temp & Top-$k$ \\\\\n & $p{=}0.95$ & $\\tau{=}0.9$ & $k{=}50$ \\\\\n\\midrule\nPythia-1.4B & 78.2 & 76.3 & 69.6 \\\\\nOLMo-1B & 78.8 & 82.0 & 74.2 \\\\\nGPT-2 XL & 83.3 & \\textbf{85.4} & 76.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBecause the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accuracy excluding d0.\nPerformance drops moderately---GPT-2~XL with temperature sampling still reaches 82.0\\%, and even the weakest setting (Pythia nucleus) retains 70.8\\%---confirming that the classifier captures inter-generation differences beyond the human--machine boundary.\n\n\\subsection{Feature Universality}\n\\label{sec:atlas:features}\n\nTo identify which statistical fingerprints carry depth signal, we train a dedicated binary RF per cell (d$_i$ vs.\\ rest) and extract feature importances (Gini impurity; permutation importance yields consistent rankings, Appendix~\\ref{app:permutation}).\nFigure~\\ref{fig:atlas_heatmap} visualizes the top-7 feature importances across all 9 cells.\n\nTwo features dominate.\nThe 90th-percentile perplexity (\\textsc{p90\\_ppl}) ranks in the top 2 in all 9 cells, while surprisal variance (\\textsc{var\\_surprisal}) does so in 7 of 9.\nIn the two exceptions---GPT-2~XL with temperature and top-$k$ sampling---the 75th-percentile perplexity (\\textsc{p75\\_ppl}) replaces surprisal variance in the top 2, though surprisal variance remains among the top 4 features.\nTo quantify cross-model agreement, we compute the Spearman rank correlation of the full 19-feature importance vectors across all $\\binom{9}{2}=36$ cell pairs and obtain a mean $\\rho = 0.868$ (range: 0.619--0.954).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_atlas_heatmap.pdf}\n\\caption{Feature importance heatmap across 9 cells (3 models $\\times$ 3 strategies). Top-7 features by mean importance. \\textsc{p90\\_ppl} appears in the top 2 for all cells; \\textsc{var\\_surprisal} for 7 of 9.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\nThese results align with theoretical predictions: recursive finetuning erodes the tail of the token-probability distribution \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails}, and high-percentile perplexity directly measures tail behavior.\nThe universality of these markers across architectures and decoding strategies suggests they reflect a structural property of the recursive generation process rather than model-specific artifacts.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFormally, given binary pairwise AUC scores for consecutive depth pairs:\n\\begin{equation}\n\\mathrm{EDD}_T \\;=\\; \\max\\bigl\\{d^* : \\mathrm{AUC}(d^*,\\, d^*{+}1) \\geq T\\bigr\\}\n\\label{eq:edd}\n\\end{equation}\nwhere $\\mathrm{AUC}(d, d{+}1)$ is the area under the ROC curve of a dedicated binary classifier distinguishing depth~$d$ from depth~$d{+}1$, and $T$ is the minimum AUC at which an adjacent pair is considered discriminable.\nWe adopt $T{=}0.75$ as default---the midpoint between chance (0.5) and perfect discrimination (1.0)---and report sensitivity across $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ in Table~\\ref{tab:edd_sensitivity}.\nCrucially, $\\mathrm{AUC}(d, d{+}1)$ must be estimated from a dedicated binary classifier rather than derived from a multi-class pipeline, as the latter suffers from decision boundary dilution (\\S\\ref{sec:atlas:edd:dilution}).\n\nFor each adjacent pair we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ per Eq.~\\ref{eq:edd}.\n\nWithin the 4-class atlas (d0--d3), 7 of 9 cells achieve $\\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \\S\\ref{sec:atlas:indist}.\n\nWe extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair.\nFigure~\\ref{fig:auc_decay} shows the pairwise AUC decay curve.\nThe d0\\,vs.\\,d1 boundary is near-perfect (AUC\\,=\\,0.998), reflecting the well-known human--machine gap.\nSubsequent boundaries degrade monotonically: d1\\,vs.\\,d2 achieves 0.925 [95\\% CI: 0.914,\\,0.935], d2\\,vs.\\,d3 reaches 0.823 [0.805,\\,0.840], and d3\\,vs.\\,d4 yields 0.784 [0.765,\\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.\nAt d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling decisively below $T{=}0.75$ and placing $\\mathrm{EDD}_{0.75}$ at~4 for this configuration.\n\n\\paragraph{Cross-model EDD.}\nWe extend the same d0--d5 pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).\nThe d3\\,vs.\\,d4 AUC consistently clusters near the 0.75 threshold: Pythia 0.784 ($p{=}0.001$), OLMo 0.765 ($p{=}0.091$, marginal), GPT-2~XL 0.750 ($p{=}0.505$, n.s.)---only Pythia achieves conventional significance, yet all three exhibit the same directional pattern.\nAt d4\\,vs.\\,d5, AUC uniformly drops below 0.70 (Pythia 0.683, OLMo 0.684, GPT-2~XL 0.681), fixing $\\mathrm{EDD}_{0.75}{=}4$ for all three models.\nThis cross-model EDD is stable across threshold choices: all three yield $\\mathrm{EDD}{=}5$ at $T{=}0.65$, $\\mathrm{EDD}{=}4$ at $T \\in \\{0.70, 0.75\\}$, and $\\mathrm{EDD}{=}3$ at $T{=}0.80$, matching the single-model pattern in Table~\\ref{tab:edd_sensitivity}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_auc_decay.pdf}\n\\caption{Binary pairwise AUC between adjacent depths (Pythia-1.4B, nucleus $p{=}0.95$, d0--d5). Shaded bands: 95\\% bootstrap CI. Dashed line: $T{=}0.75$. $\\mathrm{EDD}_{0.75}=4$: depth pairs up to d3\\,vs.\\,d4 remain discriminable.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:edd_sensitivity} shows the sensitivity of EDD to the choice of threshold.\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$.\nAt $T{=}0.80$, only d1\\,vs.\\,d2 and d2\\,vs.\\,d3 pass, yielding $\\mathrm{EDD}=3$.\nThe d0\\,vs.\\,d1 pair passes at every threshold ($\\text{AUC}\\geq0.99$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EDD sensitivity to threshold $T$ (Pythia-1.4B, nucleus $p{=}0.95$). \\checkmark: pairwise AUC $\\geq T$; ---: below $T$. d0\\,vs.\\,d1 always passes (AUC$\\geq$0.99) and is omitted.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccccr}\n\\toprule\n$T$ & d1/d2 & d2/d3 & d3/d4 & d4/d5 & EDD \\\\\n\\midrule\n0.65 & \\checkmark & \\checkmark & \\checkmark & \\checkmark & 5 \\\\\n0.70 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.75 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.80 & \\checkmark & \\checkmark & --- & --- & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Granularity ablation.}\nDecision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class), and the d2\\,vs.\\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\\% relative decline attributable to boundary dilution, not signal loss.\n\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:trajectories}\n\nThe atlas reveals that decoding strategy does not merely scale the overall signal strength---it reshapes the degradation trajectory.\nFigure~\\ref{fig:feature_trajectory} plots normalized feature means across depths for three key features.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_feature_trajectory.pdf}\n\\caption{Normalized feature trajectories across generation depths for 3 models $\\times$ 2 strategies (nucleus $p{=}0.95$, temperature $\\tau{=}0.9$). All features decrease monotonically with depth, but inter-depth spacing is highly non-uniform. Top-$k$ results are provided in Appendix~\\ref{app:topk_trajectories}.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n\\paragraph{Non-uniform inter-depth spacing.}\nFor Pythia nucleus, \\textsc{p90\\_ppl} drops from 483.7 (d0) to 61.4 (d1)---an 87\\% reduction---but only from 29.7 (d2) to 18.2 (d3), a 39\\% reduction.\nThis geometric compression of the feature space explains why adjacent-pair AUC decays monotonically (Figure~\\ref{fig:auc_decay}): each successive generation step yields diminishing statistical displacement.\n\n\\paragraph{Temperature-induced acceleration.}\nTemperature sampling ($\\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \\citet{marchi2024_heat_death}.\nConcretely, feature values at depth $N$ under temperature sampling approximate those at depth $N{+}1$ under nucleus or top-$k$.\nThis shift yields higher in-distribution accuracy (Table~\\ref{tab:main_matrix}) because each depth occupies a more distinct region of feature space, but it also means the d1/d2 boundary under temperature is closer to the d2/d3 boundary under nucleus---a mismatch that creates reversal risk in cross-strategy transfer (\\S\\ref{sec:generalization}).\n\n\\paragraph{Three-tier strategy taxonomy.}\nThe trajectory data suggests a functional classification.\nNucleus sampling ($p{=}0.95$) serves as a stable baseline with moderate signal strength.\nTemperature sampling ($\\tau{=}0.9$) enhances the signal via accelerated convergence, yielding higher within-strategy accuracy but strategy-specific depth boundaries.\nTop-$k$ sampling ($k{=}50$) attenuates the signal---accuracy drops 6--9 points relative to nucleus---because hard truncation at a fixed vocabulary size preserves more of the original distribution's shape across depths, compressing inter-depth distances.\nNotably, top-$k$ preserves the \\emph{direction} of all feature trends despite the magnitude reduction, which has implications for ordinal classifiers that rely on monotonicity (\\S\\ref{sec:generalization}).",
    "structuredPatch": [
      {
        "oldStart": 76,
        "oldLines": 12,
        "newStart": 76,
        "newLines": 33,
        "lines": [
          " Subsequent boundaries degrade monotonically: d1\\,vs.\\,d2 achieves 0.925 [95\\% CI: 0.914,\\,0.935], d2\\,vs.\\,d3 reaches 0.823 [0.805,\\,0.840], and d3\\,vs.\\,d4 yields 0.784 [0.765,\\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.",
          " At d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling decisively below $T{=}0.75$ and placing $\\mathrm{EDD}_{0.75}$ at~4 for this configuration.",
          " ",
          "-\\paragraph{Cross-model EDD.}",
          "-We extend the same d0--d5 pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).",
          "-The d3\\,vs.\\,d4 AUC consistently clusters near the 0.75 threshold: Pythia 0.784 ($p{=}0.001$), OLMo 0.765 ($p{=}0.091$, marginal), GPT-2~XL 0.750 ($p{=}0.505$, n.s.)---only Pythia achieves conventional significance, yet all three exhibit the same directional pattern.",
          "-At d4\\,vs.\\,d5, AUC uniformly drops below 0.70 (Pythia 0.683, OLMo 0.684, GPT-2~XL 0.681), fixing $\\mathrm{EDD}_{0.75}{=}4$ for all three models.",
          "-This cross-model EDD is stable across threshold choices: all three yield $\\mathrm{EDD}{=}5$ at $T{=}0.65$, $\\mathrm{EDD}{=}4$ at $T \\in \\{0.70, 0.75\\}$, and $\\mathrm{EDD}{=}3$ at $T{=}0.80$, matching the single-model pattern in Table~\\ref{tab:edd_sensitivity}.",
          "+\\paragraph{Cross-model AUC decay.}",
          "+We extend the d0--d5 binary pairwise pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).",
          "+Table~\\ref{tab:cross_model_auc} reports the full decay curves.",
          "+All three models exhibit monotonic AUC decline with a characteristic inflection: d1\\,vs.\\,d2 AUC ranges from 0.925 to 0.968, d2\\,vs.\\,d3 from 0.823 to 0.919, and d3\\,vs.\\,d4 clusters tightly near 0.75 (range 0.750--0.784).",
          "+At d4\\,vs.\\,d5, AUC uniformly falls below 0.70 (range 0.681--0.684), with no model sustaining discriminability at conventional thresholds.",
          " ",
          "+The statistical strength of the d3\\,vs.\\,d4 boundary varies across models despite directional agreement.",
          "+Bootstrap permutation tests comparing $\\mathrm{AUC}(d3,d4)$ and $\\mathrm{AUC}(d4,d5)$ yield $p{=}0.001$ for Pythia (the d3/d4 margin is reliably above d4/d5), $p{=}0.091$ for OLMo (marginal), and $p{=}0.505$ for GPT-2~XL (not statistically significant).",
          "+This stratification reflects the tightness of the AUC gap: all three models place d3\\,vs.\\,d4 above and d4\\,vs.\\,d5 below the $T{=}0.75$ line, but only Pythia's margin is large enough for conventional significance.",
          "+We therefore interpret EDD as a continuous decay profile rather than a single integer, noting that $\\mathrm{EDD}_{0.75}$ coincides at~4 across all three models while the underlying confidence varies substantially.",
          "+",
          "+\\begin{table}[t]",
          "+\\centering",
          "+\\small",
          "+\\caption{Binary pairwise AUC for adjacent depths across three models (nucleus $p{=}0.95$, d0--d5). d0\\,vs.\\,d1 omitted (AUC$\\geq$0.99 for all). $p$: bootstrap permutation test of $\\mathrm{AUC}(d3,d4) > \\mathrm{AUC}(d4,d5)$. Experiment IDs: \\texttt{depth\\_extension\\_binary\\_pairwise\\_002}, \\texttt{depth\\_extension\\_gpt2xl\\_d4d5\\_001}, \\texttt{depth\\_extension\\_olmo\\_d4d5\\_002}.}",
          "+\\label{tab:cross_model_auc}",
          "+\\begin{tabular}{lccccl}",
          "+\\toprule",
          "+Model & d1/d2 & d2/d3 & d3/d4 & d4/d5 & $p$ \\\\",
          "+\\midrule",
          "+Pythia-1.4B & .925 & .823 & .784 & .683 & .001 \\\\",
          "+GPT-2 XL & .966 & .919 & .750 & .681 & .505 \\\\",
          "+OLMo-1B & .968 & .843 & .765 & .684 & .091 \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          "+",
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{../../figures/paper/fig_auc_decay.pdf}"
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

**Edit 4: Expand EDD sensitivity table to three models**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "0012718e-7b4d-43ba-8365-dc3cca753d92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRJ9dYBaPi4cAS8e4VLJaX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 39508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1426
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

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01NnbCvQk2xKags4ptKesTzt`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
  "old_string": "Table~\\ref{tab:edd_sensitivity} shows the sensitivity of EDD to the choice of threshold.\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$.\nAt $T{=}0.80$, only d1\\,vs.\\,d2 and d2\\,vs.\\,d3 pass, yielding $\\mathrm{EDD}=3$.\nThe d0\\,vs.\\,d1 pair passes at every threshold ($\\text{AUC}\\geq0.99$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EDD sensitivity to threshold $T$ (Pythia-1.4B, nucleus $p{=}0.95$). \\checkmark: pairwise AUC $\\geq T$; ---: below $T$. d0\\,vs.\\,d1 always passes (AUC$\\geq$0.99) and is omitted.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccccr}\n\\toprule\n$T$ & d1/d2 & d2/d3 & d3/d4 & d4/d5 & EDD \\\\\n\\midrule\n0.65 & \\checkmark & \\checkmark & \\checkmark & \\checkmark & 5 \\\\\n0.70 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.75 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.80 & \\checkmark & \\checkmark & --- & --- & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
  "new_string": "Table~\\ref{tab:edd_sensitivity} shows $\\mathrm{EDD}_T$ across all three models and four threshold choices.\nAll three models yield identical EDD at every $T$, reflecting the tight clustering of d3\\,vs.\\,d4 AUC near 0.75 and d4\\,vs.\\,d5 AUC near 0.68 (Table~\\ref{tab:cross_model_auc}).\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$; at $T{=}0.80$, the d3\\,vs.\\,d4 boundary falls below threshold for all models, yielding $\\mathrm{EDD}=3$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\mathrm{EDD}_T$ across three models (nucleus $p{=}0.95$) and four thresholds. All three models yield identical EDD at every $T$ despite differing pairwise AUC values (Table~\\ref{tab:cross_model_auc}). Experiment ID: \\texttt{granularity\\_ablation\\_rf\\_001}.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccc}\n\\toprule\n$T$ & Pythia-1.4B & GPT-2 XL & OLMo-1B \\\\\n\\midrule\n0.65 & 5 & 5 & 5 \\\\\n0.70 & 4 & 4 & 4 \\\\\n0.75 & 4 & 4 & 4 \\\\\n0.80 & 3 & 3 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "4b8e6b45-a0d0-4c20-97b7-248ad4b819d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRJ9dYBaPi4cAS8e4VLJaX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 39508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1426
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

_source line 19 · 2026-05-15T15:53:51.870Z_

<details><summary>↩ Tool result · `toolu_01NnbCvQk2xKags4ptKesTzt`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "70bcbe97-71f4-4895-8966-4c5de503d557",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
    "oldString": "Table~\\ref{tab:edd_sensitivity} shows the sensitivity of EDD to the choice of threshold.\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$.\nAt $T{=}0.80$, only d1\\,vs.\\,d2 and d2\\,vs.\\,d3 pass, yielding $\\mathrm{EDD}=3$.\nThe d0\\,vs.\\,d1 pair passes at every threshold ($\\text{AUC}\\geq0.99$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EDD sensitivity to threshold $T$ (Pythia-1.4B, nucleus $p{=}0.95$). \\checkmark: pairwise AUC $\\geq T$; ---: below $T$. d0\\,vs.\\,d1 always passes (AUC$\\geq$0.99) and is omitted.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccccr}\n\\toprule\n$T$ & d1/d2 & d2/d3 & d3/d4 & d4/d5 & EDD \\\\\n\\midrule\n0.65 & \\checkmark & \\checkmark & \\checkmark & \\checkmark & 5 \\\\\n0.70 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.75 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.80 & \\checkmark & \\checkmark & --- & --- & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
    "newString": "Table~\\ref{tab:edd_sensitivity} shows $\\mathrm{EDD}_T$ across all three models and four threshold choices.\nAll three models yield identical EDD at every $T$, reflecting the tight clustering of d3\\,vs.\\,d4 AUC near 0.75 and d4\\,vs.\\,d5 AUC near 0.68 (Table~\\ref{tab:cross_model_auc}).\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$; at $T{=}0.80$, the d3\\,vs.\\,d4 boundary falls below threshold for all models, yielding $\\mathrm{EDD}=3$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\mathrm{EDD}_T$ across three models (nucleus $p{=}0.95$) and four thresholds. All three models yield identical EDD at every $T$ despite differing pairwise AUC values (Table~\\ref{tab:cross_model_auc}). Experiment ID: \\texttt{granularity\\_ablation\\_rf\\_001}.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccc}\n\\toprule\n$T$ & Pythia-1.4B & GPT-2 XL & OLMo-1B \\\\\n\\midrule\n0.65 & 5 & 5 & 5 \\\\\n0.70 & 4 & 4 & 4 \\\\\n0.75 & 4 & 4 & 4 \\\\\n0.80 & 3 & 3 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
    "originalFile": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\\times$ 3 decoding strategies $\\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.\nFor each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \\S\\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.\n\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:indist}\n\nTable~\\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.\nAll 9 cells exceed chance (25\\%) by a wide margin, with accuracy ranging from 69.6\\% to 85.4\\%.\nBoth model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.\nTop-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{In-distribution 4-class depth estimation accuracy (\\%) across 3 model families $\\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\\%.}\n\\label{tab:main_matrix}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Nucleus & Temp & Top-$k$ \\\\\n & $p{=}0.95$ & $\\tau{=}0.9$ & $k{=}50$ \\\\\n\\midrule\nPythia-1.4B & 78.2 & 76.3 & 69.6 \\\\\nOLMo-1B & 78.8 & 82.0 & 74.2 \\\\\nGPT-2 XL & 83.3 & \\textbf{85.4} & 76.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBecause the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accuracy excluding d0.\nPerformance drops moderately---GPT-2~XL with temperature sampling still reaches 82.0\\%, and even the weakest setting (Pythia nucleus) retains 70.8\\%---confirming that the classifier captures inter-generation differences beyond the human--machine boundary.\n\n\\subsection{Feature Universality}\n\\label{sec:atlas:features}\n\nTo identify which statistical fingerprints carry depth signal, we train a dedicated binary RF per cell (d$_i$ vs.\\ rest) and extract feature importances (Gini impurity; permutation importance yields consistent rankings, Appendix~\\ref{app:permutation}).\nFigure~\\ref{fig:atlas_heatmap} visualizes the top-7 feature importances across all 9 cells.\n\nTwo features dominate.\nThe 90th-percentile perplexity (\\textsc{p90\\_ppl}) ranks in the top 2 in all 9 cells, while surprisal variance (\\textsc{var\\_surprisal}) does so in 7 of 9.\nIn the two exceptions---GPT-2~XL with temperature and top-$k$ sampling---the 75th-percentile perplexity (\\textsc{p75\\_ppl}) replaces surprisal variance in the top 2, though surprisal variance remains among the top 4 features.\nTo quantify cross-model agreement, we compute the Spearman rank correlation of the full 19-feature importance vectors across all $\\binom{9}{2}=36$ cell pairs and obtain a mean $\\rho = 0.868$ (range: 0.619--0.954).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_atlas_heatmap.pdf}\n\\caption{Feature importance heatmap across 9 cells (3 models $\\times$ 3 strategies). Top-7 features by mean importance. \\textsc{p90\\_ppl} appears in the top 2 for all cells; \\textsc{var\\_surprisal} for 7 of 9.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\nThese results align with theoretical predictions: recursive finetuning erodes the tail of the token-probability distribution \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails}, and high-percentile perplexity directly measures tail behavior.\nThe universality of these markers across architectures and decoding strategies suggests they reflect a structural property of the recursive generation process rather than model-specific artifacts.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFormally, given binary pairwise AUC scores for consecutive depth pairs:\n\\begin{equation}\n\\mathrm{EDD}_T \\;=\\; \\max\\bigl\\{d^* : \\mathrm{AUC}(d^*,\\, d^*{+}1) \\geq T\\bigr\\}\n\\label{eq:edd}\n\\end{equation}\nwhere $\\mathrm{AUC}(d, d{+}1)$ is the area under the ROC curve of a dedicated binary classifier distinguishing depth~$d$ from depth~$d{+}1$, and $T$ is the minimum AUC at which an adjacent pair is considered discriminable.\nWe adopt $T{=}0.75$ as default---the midpoint between chance (0.5) and perfect discrimination (1.0)---and report sensitivity across $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ in Table~\\ref{tab:edd_sensitivity}.\nCrucially, $\\mathrm{AUC}(d, d{+}1)$ must be estimated from a dedicated binary classifier rather than derived from a multi-class pipeline, as the latter suffers from decision boundary dilution (\\S\\ref{sec:atlas:edd:dilution}).\n\nFor each adjacent pair we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ per Eq.~\\ref{eq:edd}.\n\nWithin the 4-class atlas (d0--d3), 7 of 9 cells achieve $\\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \\S\\ref{sec:atlas:indist}.\n\nWe extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair.\nFigure~\\ref{fig:auc_decay} shows the pairwise AUC decay curve.\nThe d0\\,vs.\\,d1 boundary is near-perfect (AUC\\,=\\,0.998), reflecting the well-known human--machine gap.\nSubsequent boundaries degrade monotonically: d1\\,vs.\\,d2 achieves 0.925 [95\\% CI: 0.914,\\,0.935], d2\\,vs.\\,d3 reaches 0.823 [0.805,\\,0.840], and d3\\,vs.\\,d4 yields 0.784 [0.765,\\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.\nAt d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling decisively below $T{=}0.75$ and placing $\\mathrm{EDD}_{0.75}$ at~4 for this configuration.\n\n\\paragraph{Cross-model AUC decay.}\nWe extend the d0--d5 binary pairwise pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).\nTable~\\ref{tab:cross_model_auc} reports the full decay curves.\nAll three models exhibit monotonic AUC decline with a characteristic inflection: d1\\,vs.\\,d2 AUC ranges from 0.925 to 0.968, d2\\,vs.\\,d3 from 0.823 to 0.919, and d3\\,vs.\\,d4 clusters tightly near 0.75 (range 0.750--0.784).\nAt d4\\,vs.\\,d5, AUC uniformly falls below 0.70 (range 0.681--0.684), with no model sustaining discriminability at conventional thresholds.\n\nThe statistical strength of the d3\\,vs.\\,d4 boundary varies across models despite directional agreement.\nBootstrap permutation tests comparing $\\mathrm{AUC}(d3,d4)$ and $\\mathrm{AUC}(d4,d5)$ yield $p{=}0.001$ for Pythia (the d3/d4 margin is reliably above d4/d5), $p{=}0.091$ for OLMo (marginal), and $p{=}0.505$ for GPT-2~XL (not statistically significant).\nThis stratification reflects the tightness of the AUC gap: all three models place d3\\,vs.\\,d4 above and d4\\,vs.\\,d5 below the $T{=}0.75$ line, but only Pythia's margin is large enough for conventional significance.\nWe therefore interpret EDD as a continuous decay profile rather than a single integer, noting that $\\mathrm{EDD}_{0.75}$ coincides at~4 across all three models while the underlying confidence varies substantially.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Binary pairwise AUC for adjacent depths across three models (nucleus $p{=}0.95$, d0--d5). d0\\,vs.\\,d1 omitted (AUC$\\geq$0.99 for all). $p$: bootstrap permutation test of $\\mathrm{AUC}(d3,d4) > \\mathrm{AUC}(d4,d5)$. Experiment IDs: \\texttt{depth\\_extension\\_binary\\_pairwise\\_002}, \\texttt{depth\\_extension\\_gpt2xl\\_d4d5\\_001}, \\texttt{depth\\_extension\\_olmo\\_d4d5\\_002}.}\n\\label{tab:cross_model_auc}\n\\begin{tabular}{lccccl}\n\\toprule\nModel & d1/d2 & d2/d3 & d3/d4 & d4/d5 & $p$ \\\\\n\\midrule\nPythia-1.4B & .925 & .823 & .784 & .683 & .001 \\\\\nGPT-2 XL & .966 & .919 & .750 & .681 & .505 \\\\\nOLMo-1B & .968 & .843 & .765 & .684 & .091 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_auc_decay.pdf}\n\\caption{Binary pairwise AUC between adjacent depths (Pythia-1.4B, nucleus $p{=}0.95$, d0--d5). Shaded bands: 95\\% bootstrap CI. Dashed line: $T{=}0.75$. $\\mathrm{EDD}_{0.75}=4$: depth pairs up to d3\\,vs.\\,d4 remain discriminable.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:edd_sensitivity} shows the sensitivity of EDD to the choice of threshold.\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$.\nAt $T{=}0.80$, only d1\\,vs.\\,d2 and d2\\,vs.\\,d3 pass, yielding $\\mathrm{EDD}=3$.\nThe d0\\,vs.\\,d1 pair passes at every threshold ($\\text{AUC}\\geq0.99$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{EDD sensitivity to threshold $T$ (Pythia-1.4B, nucleus $p{=}0.95$). \\checkmark: pairwise AUC $\\geq T$; ---: below $T$. d0\\,vs.\\,d1 always passes (AUC$\\geq$0.99) and is omitted.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccccr}\n\\toprule\n$T$ & d1/d2 & d2/d3 & d3/d4 & d4/d5 & EDD \\\\\n\\midrule\n0.65 & \\checkmark & \\checkmark & \\checkmark & \\checkmark & 5 \\\\\n0.70 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.75 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\\n0.80 & \\checkmark & \\checkmark & --- & --- & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Granularity ablation.}\nDecision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class), and the d2\\,vs.\\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\\% relative decline attributable to boundary dilution, not signal loss.\n\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:trajectories}\n\nThe atlas reveals that decoding strategy does not merely scale the overall signal strength---it reshapes the degradation trajectory.\nFigure~\\ref{fig:feature_trajectory} plots normalized feature means across depths for three key features.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_feature_trajectory.pdf}\n\\caption{Normalized feature trajectories across generation depths for 3 models $\\times$ 2 strategies (nucleus $p{=}0.95$, temperature $\\tau{=}0.9$). All features decrease monotonically with depth, but inter-depth spacing is highly non-uniform. Top-$k$ results are provided in Appendix~\\ref{app:topk_trajectories}.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n\\paragraph{Non-uniform inter-depth spacing.}\nFor Pythia nucleus, \\textsc{p90\\_ppl} drops from 483.7 (d0) to 61.4 (d1)---an 87\\% reduction---but only from 29.7 (d2) to 18.2 (d3), a 39\\% reduction.\nThis geometric compression of the feature space explains why adjacent-pair AUC decays monotonically (Figure~\\ref{fig:auc_decay}): each successive generation step yields diminishing statistical displacement.\n\n\\paragraph{Temperature-induced acceleration.}\nTemperature sampling ($\\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \\citet{marchi2024_heat_death}.\nConcretely, feature values at depth $N$ under temperature sampling approximate those at depth $N{+}1$ under nucleus or top-$k$.\nThis shift yields higher in-distribution accuracy (Table~\\ref{tab:main_matrix}) because each depth occupies a more distinct region of feature space, but it also means the d1/d2 boundary under temperature is closer to the d2/d3 boundary under nucleus---a mismatch that creates reversal risk in cross-strategy transfer (\\S\\ref{sec:generalization}).\n\n\\paragraph{Three-tier strategy taxonomy.}\nThe trajectory data suggests a functional classification.\nNucleus sampling ($p{=}0.95$) serves as a stable baseline with moderate signal strength.\nTemperature sampling ($\\tau{=}0.9$) enhances the signal via accelerated convergence, yielding higher within-strategy accuracy but strategy-specific depth boundaries.\nTop-$k$ sampling ($k{=}50$) attenuates the signal---accuracy drops 6--9 points relative to nucleus---because hard truncation at a fixed vocabulary size preserves more of the original distribution's shape across depths, compressing inter-depth distances.\nNotably, top-$k$ preserves the \\emph{direction} of all feature trends despite the magnitude reduction, which has implications for ordinal classifiers that rely on monotonicity (\\S\\ref{sec:generalization}).",
    "structuredPatch": [
      {
        "oldStart": 110,
        "oldLines": 24,
        "newStart": 110,
        "newLines": 23,
        "lines": [
          " \\label{fig:auc_decay}",
          " \\end{figure}",
          " ",
          "-Table~\\ref{tab:edd_sensitivity} shows the sensitivity of EDD to the choice of threshold.",
          "-At $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$.",
          "-At $T{=}0.80$, only d1\\,vs.\\,d2 and d2\\,vs.\\,d3 pass, yielding $\\mathrm{EDD}=3$.",
          "-The d0\\,vs.\\,d1 pair passes at every threshold ($\\text{AUC}\\geq0.99$).",
          "+Table~\\ref{tab:edd_sensitivity} shows $\\mathrm{EDD}_T$ across all three models and four threshold choices.",
          "+All three models yield identical EDD at every $T$, reflecting the tight clustering of d3\\,vs.\\,d4 AUC near 0.75 and d4\\,vs.\\,d5 AUC near 0.68 (Table~\\ref{tab:cross_model_auc}).",
          "+At $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$; at $T{=}0.80$, the d3\\,vs.\\,d4 boundary falls below threshold for all models, yielding $\\mathrm{EDD}=3$.",
          " ",
          " \\begin{table}[t]",
          " \\centering",
          " \\small",
          "-\\caption{EDD sensitivity to threshold $T$ (Pythia-1.4B, nucleus $p{=}0.95$). \\checkmark: pairwise AUC $\\geq T$; ---: below $T$. d0\\,vs.\\,d1 always passes (AUC$\\geq$0.99) and is omitted.}",
          "+\\caption{$\\mathrm{EDD}_T$ across three models (nucleus $p{=}0.95$) and four thresholds. All three models yield identical EDD at every $T$ despite differing pairwise AUC values (Table~\\ref{tab:cross_model_auc}). Experiment ID: \\texttt{granularity\\_ablation\\_rf\\_001}.}",
          " \\label{tab:edd_sensitivity}",
          "-\\begin{tabular}{cccccr}",
          "+\\begin{tabular}{cccc}",
          " \\toprule",
          "-$T$ & d1/d2 & d2/d3 & d3/d4 & d4/d5 & EDD \\\\",
          "+$T$ & Pythia-1.4B & GPT-2 XL & OLMo-1B \\\\",
          " \\midrule",
          "-0.65 & \\checkmark & \\checkmark & \\checkmark & \\checkmark & 5 \\\\",
          "-0.70 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\",
          "-0.75 & \\checkmark & \\checkmark & \\checkmark & --- & 4 \\\\",
          "-0.80 & \\checkmark & \\checkmark & --- & --- & 3 \\\\",
          "+0.65 & 5 & 5 & 5 \\\\",
          "+0.70 & 4 & 4 & 4 \\\\",
          "+0.75 & 4 & 4 & 4 \\\\",
          "+0.80 & 3 & 3 & 3 \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}"
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

_source line 20_

**Edit 5: Expand decision boundary dilution paragraph**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "2f4bbe1e-4abb-43c1-8e1f-a4d29ff381da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJLZBoyfHwFpuXnQ9nLnXn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1212,
      "cache_read_input_tokens": 40934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1212
      },
      "output_tokens": 7,
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01UQ8g4cXYN2T9Xpir677zVn`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
  "old_string": "\\paragraph{Granularity ablation.}\nDecision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class), and the d2\\,vs.\\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\\% relative decline attributable to boundary dilution, not signal loss.",
  "new_string": "\\paragraph{Decision boundary dilution.}\n\\label{sec:atlas:edd:dilution}\nEDD's binary-pair design is motivated by \\emph{decision boundary dilution}: when a multi-class classifier must simultaneously separate $K$ depths, its decision boundaries are shared across all $\\binom{K}{2}$ class pairs, diluting the capacity allocated to any single adjacent pair.\nConcretely, in the Pythia nucleus setting (experiment \\texttt{granularity\\_ablation\\_rf\\_001}), the d2\\,vs.\\,d3 pairwise AUC degrades from 0.804 in a 4-class pipeline to 0.689 in a 6-class pipeline---a 14.3\\% relative decline---despite identical underlying data.\nMean classification accuracy likewise drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class).\nBecause the pairwise signal between depths $d$ and $d{+}1$ does not change when unrelated depths are added, this degradation is entirely attributable to boundary dilution, not signal loss.\nBinary pairwise classifiers eliminate this confound, isolating the true adjacent-pair discriminability that EDD is designed to measure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "151eb8e7-c5a2-4bb5-9b4b-ef854061fc1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJLZBoyfHwFpuXnQ9nLnXn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1212,
      "cache_read_input_tokens": 40934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1212
      },
      "output_tokens": 7,
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

_source line 22 · 2026-05-15T15:54:03.116Z_

<details><summary>↩ Tool result · `toolu_01UQ8g4cXYN2T9Xpir677zVn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "70a20f2d-befd-4d3d-84e5-48f6fa216c4c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
    "oldString": "\\paragraph{Granularity ablation.}\nDecision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class), and the d2\\,vs.\\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\\% relative decline attributable to boundary dilution, not signal loss.",
    "newString": "\\paragraph{Decision boundary dilution.}\n\\label{sec:atlas:edd:dilution}\nEDD's binary-pair design is motivated by \\emph{decision boundary dilution}: when a multi-class classifier must simultaneously separate $K$ depths, its decision boundaries are shared across all $\\binom{K}{2}$ class pairs, diluting the capacity allocated to any single adjacent pair.\nConcretely, in the Pythia nucleus setting (experiment \\texttt{granularity\\_ablation\\_rf\\_001}), the d2\\,vs.\\,d3 pairwise AUC degrades from 0.804 in a 4-class pipeline to 0.689 in a 6-class pipeline---a 14.3\\% relative decline---despite identical underlying data.\nMean classification accuracy likewise drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class).\nBecause the pairwise signal between depths $d$ and $d{+}1$ does not change when unrelated depths are added, this degradation is entirely attributable to boundary dilution, not signal loss.\nBinary pairwise classifiers eliminate this confound, isolating the true adjacent-pair discriminability that EDD is designed to measure.",
    "originalFile": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\\times$ 3 decoding strategies $\\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.\nFor each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \\S\\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.\n\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:indist}\n\nTable~\\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.\nAll 9 cells exceed chance (25\\%) by a wide margin, with accuracy ranging from 69.6\\% to 85.4\\%.\nBoth model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.\nTop-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{In-distribution 4-class depth estimation accuracy (\\%) across 3 model families $\\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\\%.}\n\\label{tab:main_matrix}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Nucleus & Temp & Top-$k$ \\\\\n & $p{=}0.95$ & $\\tau{=}0.9$ & $k{=}50$ \\\\\n\\midrule\nPythia-1.4B & 78.2 & 76.3 & 69.6 \\\\\nOLMo-1B & 78.8 & 82.0 & 74.2 \\\\\nGPT-2 XL & 83.3 & \\textbf{85.4} & 76.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBecause the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accuracy excluding d0.\nPerformance drops moderately---GPT-2~XL with temperature sampling still reaches 82.0\\%, and even the weakest setting (Pythia nucleus) retains 70.8\\%---confirming that the classifier captures inter-generation differences beyond the human--machine boundary.\n\n\\subsection{Feature Universality}\n\\label{sec:atlas:features}\n\nTo identify which statistical fingerprints carry depth signal, we train a dedicated binary RF per cell (d$_i$ vs.\\ rest) and extract feature importances (Gini impurity; permutation importance yields consistent rankings, Appendix~\\ref{app:permutation}).\nFigure~\\ref{fig:atlas_heatmap} visualizes the top-7 feature importances across all 9 cells.\n\nTwo features dominate.\nThe 90th-percentile perplexity (\\textsc{p90\\_ppl}) ranks in the top 2 in all 9 cells, while surprisal variance (\\textsc{var\\_surprisal}) does so in 7 of 9.\nIn the two exceptions---GPT-2~XL with temperature and top-$k$ sampling---the 75th-percentile perplexity (\\textsc{p75\\_ppl}) replaces surprisal variance in the top 2, though surprisal variance remains among the top 4 features.\nTo quantify cross-model agreement, we compute the Spearman rank correlation of the full 19-feature importance vectors across all $\\binom{9}{2}=36$ cell pairs and obtain a mean $\\rho = 0.868$ (range: 0.619--0.954).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_atlas_heatmap.pdf}\n\\caption{Feature importance heatmap across 9 cells (3 models $\\times$ 3 strategies). Top-7 features by mean importance. \\textsc{p90\\_ppl} appears in the top 2 for all cells; \\textsc{var\\_surprisal} for 7 of 9.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\nThese results align with theoretical predictions: recursive finetuning erodes the tail of the token-probability distribution \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails}, and high-percentile perplexity directly measures tail behavior.\nThe universality of these markers across architectures and decoding strategies suggests they reflect a structural property of the recursive generation process rather than model-specific artifacts.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFormally, given binary pairwise AUC scores for consecutive depth pairs:\n\\begin{equation}\n\\mathrm{EDD}_T \\;=\\; \\max\\bigl\\{d^* : \\mathrm{AUC}(d^*,\\, d^*{+}1) \\geq T\\bigr\\}\n\\label{eq:edd}\n\\end{equation}\nwhere $\\mathrm{AUC}(d, d{+}1)$ is the area under the ROC curve of a dedicated binary classifier distinguishing depth~$d$ from depth~$d{+}1$, and $T$ is the minimum AUC at which an adjacent pair is considered discriminable.\nWe adopt $T{=}0.75$ as default---the midpoint between chance (0.5) and perfect discrimination (1.0)---and report sensitivity across $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ in Table~\\ref{tab:edd_sensitivity}.\nCrucially, $\\mathrm{AUC}(d, d{+}1)$ must be estimated from a dedicated binary classifier rather than derived from a multi-class pipeline, as the latter suffers from decision boundary dilution (\\S\\ref{sec:atlas:edd:dilution}).\n\nFor each adjacent pair we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ per Eq.~\\ref{eq:edd}.\n\nWithin the 4-class atlas (d0--d3), 7 of 9 cells achieve $\\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \\S\\ref{sec:atlas:indist}.\n\nWe extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair.\nFigure~\\ref{fig:auc_decay} shows the pairwise AUC decay curve.\nThe d0\\,vs.\\,d1 boundary is near-perfect (AUC\\,=\\,0.998), reflecting the well-known human--machine gap.\nSubsequent boundaries degrade monotonically: d1\\,vs.\\,d2 achieves 0.925 [95\\% CI: 0.914,\\,0.935], d2\\,vs.\\,d3 reaches 0.823 [0.805,\\,0.840], and d3\\,vs.\\,d4 yields 0.784 [0.765,\\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.\nAt d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling decisively below $T{=}0.75$ and placing $\\mathrm{EDD}_{0.75}$ at~4 for this configuration.\n\n\\paragraph{Cross-model AUC decay.}\nWe extend the d0--d5 binary pairwise pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).\nTable~\\ref{tab:cross_model_auc} reports the full decay curves.\nAll three models exhibit monotonic AUC decline with a characteristic inflection: d1\\,vs.\\,d2 AUC ranges from 0.925 to 0.968, d2\\,vs.\\,d3 from 0.823 to 0.919, and d3\\,vs.\\,d4 clusters tightly near 0.75 (range 0.750--0.784).\nAt d4\\,vs.\\,d5, AUC uniformly falls below 0.70 (range 0.681--0.684), with no model sustaining discriminability at conventional thresholds.\n\nThe statistical strength of the d3\\,vs.\\,d4 boundary varies across models despite directional agreement.\nBootstrap permutation tests comparing $\\mathrm{AUC}(d3,d4)$ and $\\mathrm{AUC}(d4,d5)$ yield $p{=}0.001$ for Pythia (the d3/d4 margin is reliably above d4/d5), $p{=}0.091$ for OLMo (marginal), and $p{=}0.505$ for GPT-2~XL (not statistically significant).\nThis stratification reflects the tightness of the AUC gap: all three models place d3\\,vs.\\,d4 above and d4\\,vs.\\,d5 below the $T{=}0.75$ line, but only Pythia's margin is large enough for conventional significance.\nWe therefore interpret EDD as a continuous decay profile rather than a single integer, noting that $\\mathrm{EDD}_{0.75}$ coincides at~4 across all three models while the underlying confidence varies substantially.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Binary pairwise AUC for adjacent depths across three models (nucleus $p{=}0.95$, d0--d5). d0\\,vs.\\,d1 omitted (AUC$\\geq$0.99 for all). $p$: bootstrap permutation test of $\\mathrm{AUC}(d3,d4) > \\mathrm{AUC}(d4,d5)$. Experiment IDs: \\texttt{depth\\_extension\\_binary\\_pairwise\\_002}, \\texttt{depth\\_extension\\_gpt2xl\\_d4d5\\_001}, \\texttt{depth\\_extension\\_olmo\\_d4d5\\_002}.}\n\\label{tab:cross_model_auc}\n\\begin{tabular}{lccccl}\n\\toprule\nModel & d1/d2 & d2/d3 & d3/d4 & d4/d5 & $p$ \\\\\n\\midrule\nPythia-1.4B & .925 & .823 & .784 & .683 & .001 \\\\\nGPT-2 XL & .966 & .919 & .750 & .681 & .505 \\\\\nOLMo-1B & .968 & .843 & .765 & .684 & .091 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_auc_decay.pdf}\n\\caption{Binary pairwise AUC between adjacent depths (Pythia-1.4B, nucleus $p{=}0.95$, d0--d5). Shaded bands: 95\\% bootstrap CI. Dashed line: $T{=}0.75$. $\\mathrm{EDD}_{0.75}=4$: depth pairs up to d3\\,vs.\\,d4 remain discriminable.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:edd_sensitivity} shows $\\mathrm{EDD}_T$ across all three models and four threshold choices.\nAll three models yield identical EDD at every $T$, reflecting the tight clustering of d3\\,vs.\\,d4 AUC near 0.75 and d4\\,vs.\\,d5 AUC near 0.68 (Table~\\ref{tab:cross_model_auc}).\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$; at $T{=}0.80$, the d3\\,vs.\\,d4 boundary falls below threshold for all models, yielding $\\mathrm{EDD}=3$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\mathrm{EDD}_T$ across three models (nucleus $p{=}0.95$) and four thresholds. All three models yield identical EDD at every $T$ despite differing pairwise AUC values (Table~\\ref{tab:cross_model_auc}). Experiment ID: \\texttt{granularity\\_ablation\\_rf\\_001}.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccc}\n\\toprule\n$T$ & Pythia-1.4B & GPT-2 XL & OLMo-1B \\\\\n\\midrule\n0.65 & 5 & 5 & 5 \\\\\n0.70 & 4 & 4 & 4 \\\\\n0.75 & 4 & 4 & 4 \\\\\n0.80 & 3 & 3 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Granularity ablation.}\nDecision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class), and the d2\\,vs.\\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\\% relative decline attributable to boundary dilution, not signal loss.\n\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:trajectories}\n\nThe atlas reveals that decoding strategy does not merely scale the overall signal strength---it reshapes the degradation trajectory.\nFigure~\\ref{fig:feature_trajectory} plots normalized feature means across depths for three key features.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_feature_trajectory.pdf}\n\\caption{Normalized feature trajectories across generation depths for 3 models $\\times$ 2 strategies (nucleus $p{=}0.95$, temperature $\\tau{=}0.9$). All features decrease monotonically with depth, but inter-depth spacing is highly non-uniform. Top-$k$ results are provided in Appendix~\\ref{app:topk_trajectories}.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n\\paragraph{Non-uniform inter-depth spacing.}\nFor Pythia nucleus, \\textsc{p90\\_ppl} drops from 483.7 (d0) to 61.4 (d1)---an 87\\% reduction---but only from 29.7 (d2) to 18.2 (d3), a 39\\% reduction.\nThis geometric compression of the feature space explains why adjacent-pair AUC decays monotonically (Figure~\\ref{fig:auc_decay}): each successive generation step yields diminishing statistical displacement.\n\n\\paragraph{Temperature-induced acceleration.}\nTemperature sampling ($\\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \\citet{marchi2024_heat_death}.\nConcretely, feature values at depth $N$ under temperature sampling approximate those at depth $N{+}1$ under nucleus or top-$k$.\nThis shift yields higher in-distribution accuracy (Table~\\ref{tab:main_matrix}) because each depth occupies a more distinct region of feature space, but it also means the d1/d2 boundary under temperature is closer to the d2/d3 boundary under nucleus---a mismatch that creates reversal risk in cross-strategy transfer (\\S\\ref{sec:generalization}).\n\n\\paragraph{Three-tier strategy taxonomy.}\nThe trajectory data suggests a functional classification.\nNucleus sampling ($p{=}0.95$) serves as a stable baseline with moderate signal strength.\nTemperature sampling ($\\tau{=}0.9$) enhances the signal via accelerated convergence, yielding higher within-strategy accuracy but strategy-specific depth boundaries.\nTop-$k$ sampling ($k{=}50$) attenuates the signal---accuracy drops 6--9 points relative to nucleus---because hard truncation at a fixed vocabulary size preserves more of the original distribution's shape across depths, compressing inter-depth distances.\nNotably, top-$k$ preserves the \\emph{direction} of all feature trends despite the magnitude reduction, which has implications for ordinal classifiers that rely on monotonicity (\\S\\ref{sec:generalization}).",
    "structuredPatch": [
      {
        "oldStart": 131,
        "oldLines": 8,
        "newStart": 131,
        "newLines": 13,
        "lines": [
          " \\end{tabular}",
          " \\end{table}",
          " ",
          "-\\paragraph{Granularity ablation.}",
          "-Decision boundary dilution motivates EDD's binary-pair design: mean accuracy drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class), and the d2\\,vs.\\,d3 AUC falls from 0.804 to 0.689 between the 4-class and 6-class settings for Pythia nucleus---a 14\\% relative decline attributable to boundary dilution, not signal loss.",
          "+\\paragraph{Decision boundary dilution.}",
          "+\\label{sec:atlas:edd:dilution}",
          "+EDD's binary-pair design is motivated by \\emph{decision boundary dilution}: when a multi-class classifier must simultaneously separate $K$ depths, its decision boundaries are shared across all $\\binom{K}{2}$ class pairs, diluting the capacity allocated to any single adjacent pair.",
          "+Concretely, in the Pythia nucleus setting (experiment \\texttt{granularity\\_ablation\\_rf\\_001}), the d2\\,vs.\\,d3 pairwise AUC degrades from 0.804 in a 4-class pipeline to 0.689 in a 6-class pipeline---a 14.3\\% relative decline---despite identical underlying data.",
          "+Mean classification accuracy likewise drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class).",
          "+Because the pairwise signal between depths $d$ and $d{+}1$ does not change when unrelated depths are added, this degradation is entirely attributable to boundary dilution, not signal loss.",
          "+Binary pairwise classifiers eliminate this confound, isolating the true adjacent-pair discriminability that EDD is designed to measure.",
          " ",
          " \\subsection{Strategy-Dependent Trajectories}",
          " \\label{sec:atlas:trajectories}"
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

Now verifying the final file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "a4fb5c43-c261-4397-9cef-a162b3c0b1ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XusbdcqzR29ER2B9pi8q5y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 42146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 633
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

<details open><summary>🔧 Tool call — Read · `toolu_01C8MvjY3Hqr8e7xYHKZ7iN3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "645900d6-51d7-40a8-a3ac-0f8701557101",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XusbdcqzR29ER2B9pi8q5y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 633,
      "cache_read_input_tokens": 42146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 633
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

_source line 25 · 2026-05-15T15:54:06.252Z_

<details><summary>↩ Tool result · `toolu_01C8MvjY3Hqr8e7xYHKZ7iN3`</summary>

```text
1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\times$ 3 decoding strategies $\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.
5	For each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \S\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.
6	
7	\subsection{In-Distribution Performance}
8	\label{sec:atlas:indist}
9	
10	Table~\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.
11	All 9 cells exceed chance (25\%) by a wide margin, with accuracy ranging from 69.6\% to 85.4\%.
12	Both model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.
13	Top-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{In-distribution 4-class depth estimation accuracy (\%) across 3 model families $\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\%.}
19	\label{tab:main_matrix}
20	\begin{tabular}{lccc}
21	\toprule
22	Model & Nucleus & Temp & Top-$k$ \\
23	 & $p{=}0.95$ & $\tau{=}0.9$ & $k{=}50$ \\
24	\midrule
25	Pythia-1.4B & 78.2 & 76.3 & 69.6 \\
26	OLMo-1B & 78.8 & 82.0 & 74.2 \\
27	GPT-2 XL & 83.3 & \textbf{85.4} & 76.6 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	Because the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accuracy excluding d0.
33	Performance drops moderately---GPT-2~XL with temperature sampling still reaches 82.0\%, and even the weakest setting (Pythia nucleus) retains 70.8\%---confirming that the classifier captures inter-generation differences beyond the human--machine boundary.
34	
35	\subsection{Feature Universality}
36	\label{sec:atlas:features}
37	
38	To identify which statistical fingerprints carry depth signal, we train a dedicated binary RF per cell (d$_i$ vs.\ rest) and extract feature importances (Gini impurity; permutation importance yields consistent rankings, Appendix~\ref{app:permutation}).
39	Figure~\ref{fig:atlas_heatmap} visualizes the top-7 feature importances across all 9 cells.
40	
41	Two features dominate.
42	The 90th-percentile perplexity (\textsc{p90\_ppl}) ranks in the top 2 in all 9 cells, while surprisal variance (\textsc{var\_surprisal}) does so in 7 of 9.
43	In the two exceptions---GPT-2~XL with temperature and top-$k$ sampling---the 75th-percentile perplexity (\textsc{p75\_ppl}) replaces surprisal variance in the top 2, though surprisal variance remains among the top 4 features.
44	To quantify cross-model agreement, we compute the Spearman rank correlation of the full 19-feature importance vectors across all $\binom{9}{2}=36$ cell pairs and obtain a mean $\rho = 0.868$ (range: 0.619--0.954).
45	
46	\begin{figure}[t]
47	\centering
48	\includegraphics[width=\columnwidth]{../../figures/paper/fig_atlas_heatmap.pdf}
49	\caption{Feature importance heatmap across 9 cells (3 models $\times$ 3 strategies). Top-7 features by mean importance. \textsc{p90\_ppl} appears in the top 2 for all cells; \textsc{var\_surprisal} for 7 of 9.}
50	\label{fig:atlas_heatmap}
51	\end{figure}
52	
53	These results align with theoretical predictions: recursive finetuning erodes the tail of the token-probability distribution \cite{shumailov2024_nature,dohmatob2024_tale_of_tails}, and high-percentile perplexity directly measures tail behavior.
54	The universality of these markers across architectures and decoding strategies suggests they reflect a structural property of the recursive generation process rather than model-specific artifacts.
55	
56	\subsection{Effective Discriminable Depth}
57	\label{sec:atlas:edd}
58	
59	Aggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \emph{Effective Discriminable Depth} (EDD).
60	Formally, given binary pairwise AUC scores for consecutive depth pairs:
61	\begin{equation}
62	\mathrm{EDD}_T \;=\; \max\bigl\{d^* : \mathrm{AUC}(d^*,\, d^*{+}1) \geq T\bigr\}
63	\label{eq:edd}
64	\end{equation}
65	where $\mathrm{AUC}(d, d{+}1)$ is the area under the ROC curve of a dedicated binary classifier distinguishing depth~$d$ from depth~$d{+}1$, and $T$ is the minimum AUC at which an adjacent pair is considered discriminable.
66	We adopt $T{=}0.75$ as default---the midpoint between chance (0.5) and perfect discrimination (1.0)---and report sensitivity across $T \in \{0.65, 0.70, 0.75, 0.80\}$ in Table~\ref{tab:edd_sensitivity}.
67	Crucially, $\mathrm{AUC}(d, d{+}1)$ must be estimated from a dedicated binary classifier rather than derived from a multi-class pipeline, as the latter suffers from decision boundary dilution (\S\ref{sec:atlas:edd:dilution}).
68	
69	For each adjacent pair we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\mathrm{AUC}(d, d{+}1)$ per Eq.~\ref{eq:edd}.
70	
71	Within the 4-class atlas (d0--d3), 7 of 9 cells achieve $\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \S\ref{sec:atlas:indist}.
72	
73	We extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair.
74	Figure~\ref{fig:auc_decay} shows the pairwise AUC decay curve.
75	The d0\,vs.\,d1 boundary is near-perfect (AUC\,=\,0.998), reflecting the well-known human--machine gap.
76	Subsequent boundaries degrade monotonically: d1\,vs.\,d2 achieves 0.925 [95\% CI: 0.914,\,0.935], d2\,vs.\,d3 reaches 0.823 [0.805,\,0.840], and d3\,vs.\,d4 yields 0.784 [0.765,\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.
77	At d4\,vs.\,d5, AUC drops to 0.683 [0.661,\,0.705], falling decisively below $T{=}0.75$ and placing $\mathrm{EDD}_{0.75}$ at~4 for this configuration.
78	
79	\paragraph{Cross-model AUC decay.}
80	We extend the d0--d5 binary pairwise pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).
81	Table~\ref{tab:cross_model_auc} reports the full decay curves.
82	All three models exhibit monotonic AUC decline with a characteristic inflection: d1\,vs.\,d2 AUC ranges from 0.925 to 0.968, d2\,vs.\,d3 from 0.823 to 0.919, and d3\,vs.\,d4 clusters tightly near 0.75 (range 0.750--0.784).
83	At d4\,vs.\,d5, AUC uniformly falls below 0.70 (range 0.681--0.684), with no model sustaining discriminability at conventional thresholds.
84	
85	The statistical strength of the d3\,vs.\,d4 boundary varies across models despite directional agreement.
86	Bootstrap permutation tests comparing $\mathrm{AUC}(d3,d4)$ and $\mathrm{AUC}(d4,d5)$ yield $p{=}0.001$ for Pythia (the d3/d4 margin is reliably above d4/d5), $p{=}0.091$ for OLMo (marginal), and $p{=}0.505$ for GPT-2~XL (not statistically significant).
87	This stratification reflects the tightness of the AUC gap: all three models place d3\,vs.\,d4 above and d4\,vs.\,d5 below the $T{=}0.75$ line, but only Pythia's margin is large enough for conventional significance.
88	We therefore interpret EDD as a continuous decay profile rather than a single integer, noting that $\mathrm{EDD}_{0.75}$ coincides at~4 across all three models while the underlying confidence varies substantially.
89	
90	\begin{table}[t]
91	\centering
92	\small
93	\caption{Binary pairwise AUC for adjacent depths across three models (nucleus $p{=}0.95$, d0--d5). d0\,vs.\,d1 omitted (AUC$\geq$0.99 for all). $p$: bootstrap permutation test of $\mathrm{AUC}(d3,d4) > \mathrm{AUC}(d4,d5)$. Experiment IDs: \texttt{depth\_extension\_binary\_pairwise\_002}, \texttt{depth\_extension\_gpt2xl\_d4d5\_001}, \texttt{depth\_extension\_olmo\_d4d5\_002}.}
94	\label{tab:cross_model_auc}
95	\begin{tabular}{lccccl}
96	\toprule
97	Model & d1/d2 & d2/d3 & d3/d4 & d4/d5 & $p$ \\
98	\midrule
99	Pythia-1.4B & .925 & .823 & .784 & .683 & .001 \\
100	GPT-2 XL & .966 & .919 & .750 & .681 & .505 \\
101	OLMo-1B & .968 & .843 & .765 & .684 & .091 \\
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	\begin{figure}[t]
107	\centering
108	\includegraphics[width=\columnwidth]{../../figures/paper/fig_auc_decay.pdf}
109	\caption{Binary pairwise AUC between adjacent depths (Pythia-1.4B, nucleus $p{=}0.95$, d0--d5). Shaded bands: 95\% bootstrap CI. Dashed line: $T{=}0.75$. $\mathrm{EDD}_{0.75}=4$: depth pairs up to d3\,vs.\,d4 remain discriminable.}
110	\label{fig:auc_decay}
111	\end{figure}
112	
113	Table~\ref{tab:edd_sensitivity} shows $\mathrm{EDD}_T$ across all three models and four threshold choices.
114	All three models yield identical EDD at every $T$, reflecting the tight clustering of d3\,vs.\,d4 AUC near 0.75 and d4\,vs.\,d5 AUC near 0.68 (Table~\ref{tab:cross_model_auc}).
115	At $T{=}0.65$, all pairs through d4\,vs.\,d5 pass, giving $\mathrm{EDD}=5$; at $T{=}0.80$, the d3\,vs.\,d4 boundary falls below threshold for all models, yielding $\mathrm{EDD}=3$.
116	
117	\begin{table}[t]
118	\centering
119	\small
120	\caption{$\mathrm{EDD}_T$ across three models (nucleus $p{=}0.95$) and four thresholds. All three models yield identical EDD at every $T$ despite differing pairwise AUC values (Table~\ref{tab:cross_model_auc}). Experiment ID: \texttt{granularity\_ablation\_rf\_001}.}
121	\label{tab:edd_sensitivity}
122	\begin{tabular}{cccc}
123	\toprule
124	$T$ & Pythia-1.4B & GPT-2 XL & OLMo-1B \\
125	\midrule
126	0.65 & 5 & 5 & 5 \\
127	0.70 & 4 & 4 & 4 \\
128	0.75 & 4 & 4 & 4 \\
129	0.80 & 3 & 3 & 3 \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	\paragraph{Decision boundary dilution.}
135	\label{sec:atlas:edd:dilution}
136	EDD's binary-pair design is motivated by \emph{decision boundary dilution}: when a multi-class classifier must simultaneously separate $K$ depths, its decision boundaries are shared across all $\binom{K}{2}$ class pairs, diluting the capacity allocated to any single adjacent pair.
137	Concretely, in the Pythia nucleus setting (experiment \texttt{granularity\_ablation\_rf\_001}), the d2\,vs.\,d3 pairwise AUC degrades from 0.804 in a 4-class pipeline to 0.689 in a 6-class pipeline---a 14.3\% relative decline---despite identical underlying data.
138	Mean classification accuracy likewise drops from 99.5\% (binary) to 78.3\% (4-class) to 62.9\% (6-class).
139	Because the pairwise signal between depths $d$ and $d{+}1$ does not change when unrelated depths are added, this degradation is entirely attributable to boundary dilution, not signal loss.
140	Binary pairwise classifiers eliminate this confound, isolating the true adjacent-pair discriminability that EDD is designed to measure.
141	
142	\subsection{Strategy-Dependent Trajectories}
143	\label{sec:atlas:trajectories}
144	
145	The atlas reveals that decoding strategy does not merely scale the overall signal strength---it reshapes the degradation trajectory.
146	Figure~\ref{fig:feature_trajectory} plots normalized feature means across depths for three key features.
147	
148	\begin{figure}[t]
149	\centering
150	\includegraphics[width=\columnwidth]{../../figures/paper/fig_feature_trajectory.pdf}
151	\caption{Normalized feature trajectories across generation depths for 3 models $\times$ 2 strategies (nucleus $p{=}0.95$, temperature $\tau{=}0.9$). All features decrease monotonically with depth, but inter-depth spacing is highly non-uniform. Top-$k$ results are provided in Appendix~\ref{app:topk_trajectories}.}
152	\label{fig:feature_trajectory}
153	\end{figure}
154	
155	\paragraph{Non-uniform inter-depth spacing.}
156	For Pythia nucleus, \textsc{p90\_ppl} drops from 483.7 (d0) to 61.4 (d1)---an 87\% reduction---but only from 29.7 (d2) to 18.2 (d3), a 39\% reduction.
157	This geometric compression of the feature space explains why adjacent-pair AUC decays monotonically (Figure~\ref{fig:auc_decay}): each successive generation step yields diminishing statistical displacement.
158	
159	\paragraph{Temperature-induced acceleration.}
160	Temperature sampling ($\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \citet{marchi2024_heat_death}.
161	Concretely, feature values at depth $N$ under temperature sampling approximate those at depth $N{+}1$ under nucleus or top-$k$.
162	This shift yields higher in-distribution accuracy (Table~\ref{tab:main_matrix}) because each depth occupies a more distinct region of feature space, but it also means the d1/d2 boundary under temperature is closer to the d2/d3 boundary under nucleus---a mismatch that creates reversal risk in cross-strategy transfer (\S\ref{sec:generalization}).
163	
164	\paragraph{Three-tier strategy taxonomy.}
165	The trajectory data suggests a functional classification.
166	Nucleus sampling ($p{=}0.95$) serves as a stable baseline with moderate signal strength.
167	Temperature sampling ($\tau{=}0.9$) enhances the signal via accelerated convergence, yielding higher within-strategy accuracy but strategy-specific depth boundaries.
168	Top-$k$ sampling ($k{=}50$) attenuates the signal---accuracy drops 6--9 points relative to nucleus---because hard truncation at a fixed vocabulary size preserves more of the original distribution's shape across depths, compressing inter-depth distances.
169	Notably, top-$k$ preserves the \emph{direction} of all feature trends despite the magnitude reduction, which has implications for ordinal classifiers that rely on monotonicity (\S\ref{sec:generalization}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "0731b619-b49e-4887-a409-bd8b644c8cde",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
      "content": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe systematically characterize how recursive generation reshapes the statistical profile of text across a grid of 3 model families $\\times$ 3 decoding strategies $\\times$ 4 generation depths (d0--d3), yielding 9 experimental configurations each spanning 4 depths.\nFor each cell we train a Random Forest (RF) classifier on the 19 statistical features defined in \\S\\ref{sec:method} and examine (i)~in-distribution depth classification accuracy, (ii)~which features carry depth signal, (iii)~how far into the recursion chain depth remains discriminable, and (iv)~how decoding strategy modulates the degradation trajectory.\n\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:indist}\n\nTable~\\ref{tab:main_matrix} reports 4-class depth estimation accuracy under 5-fold cross-validation.\nAll 9 cells exceed chance (25\\%) by a wide margin, with accuracy ranging from 69.6\\% to 85.4\\%.\nBoth model family and decoding strategy influence accuracy, with model ordering GPT-2~XL $>$ OLMo $>$ Pythia holding across all strategies.\nTop-$k$ ($k{=}50$) trails by 6--9 percentage points, while temperature and nucleus sampling alternate for the lead depending on model family.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{In-distribution 4-class depth estimation accuracy (\\%) across 3 model families $\\times$ 3 decoding strategies. RF classifier with 19 statistical features, 5-fold CV (std 0.2--0.9pp across all cells). Chance = 25\\%.}\n\\label{tab:main_matrix}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Nucleus & Temp & Top-$k$ \\\\\n & $p{=}0.95$ & $\\tau{=}0.9$ & $k{=}50$ \\\\\n\\midrule\nPythia-1.4B & 78.2 & 76.3 & 69.6 \\\\\nOLMo-1B & 78.8 & 82.0 & 74.2 \\\\\nGPT-2 XL & 83.3 & \\textbf{85.4} & 76.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBecause the human-written seed text (d0) is often trivially separable from any machine-generated depth, we also evaluate 3-class accuracy excluding d0.\nPerformance drops moderately---GPT-2~XL with temperature sampling still reaches 82.0\\%, and even the weakest setting (Pythia nucleus) retains 70.8\\%---confirming that the classifier captures inter-generation differences beyond the human--machine boundary.\n\n\\subsection{Feature Universality}\n\\label{sec:atlas:features}\n\nTo identify which statistical fingerprints carry depth signal, we train a dedicated binary RF per cell (d$_i$ vs.\\ rest) and extract feature importances (Gini impurity; permutation importance yields consistent rankings, Appendix~\\ref{app:permutation}).\nFigure~\\ref{fig:atlas_heatmap} visualizes the top-7 feature importances across all 9 cells.\n\nTwo features dominate.\nThe 90th-percentile perplexity (\\textsc{p90\\_ppl}) ranks in the top 2 in all 9 cells, while surprisal variance (\\textsc{var\\_surprisal}) does so in 7 of 9.\nIn the two exceptions---GPT-2~XL with temperature and top-$k$ sampling---the 75th-percentile perplexity (\\textsc{p75\\_ppl}) replaces surprisal variance in the top 2, though surprisal variance remains among the top 4 features.\nTo quantify cross-model agreement, we compute the Spearman rank correlation of the full 19-feature importance vectors across all $\\binom{9}{2}=36$ cell pairs and obtain a mean $\\rho = 0.868$ (range: 0.619--0.954).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_atlas_heatmap.pdf}\n\\caption{Feature importance heatmap across 9 cells (3 models $\\times$ 3 strategies). Top-7 features by mean importance. \\textsc{p90\\_ppl} appears in the top 2 for all cells; \\textsc{var\\_surprisal} for 7 of 9.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\nThese results align with theoretical predictions: recursive finetuning erodes the tail of the token-probability distribution \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails}, and high-percentile perplexity directly measures tail behavior.\nThe universality of these markers across architectures and decoding strategies suggests they reflect a structural property of the recursive generation process rather than model-specific artifacts.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:atlas:edd}\n\nAggregate accuracy masks that adjacent depths become harder to distinguish as depth increases; we quantify this via the \\emph{Effective Discriminable Depth} (EDD).\nFormally, given binary pairwise AUC scores for consecutive depth pairs:\n\\begin{equation}\n\\mathrm{EDD}_T \\;=\\; \\max\\bigl\\{d^* : \\mathrm{AUC}(d^*,\\, d^*{+}1) \\geq T\\bigr\\}\n\\label{eq:edd}\n\\end{equation}\nwhere $\\mathrm{AUC}(d, d{+}1)$ is the area under the ROC curve of a dedicated binary classifier distinguishing depth~$d$ from depth~$d{+}1$, and $T$ is the minimum AUC at which an adjacent pair is considered discriminable.\nWe adopt $T{=}0.75$ as default---the midpoint between chance (0.5) and perfect discrimination (1.0)---and report sensitivity across $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ in Table~\\ref{tab:edd_sensitivity}.\nCrucially, $\\mathrm{AUC}(d, d{+}1)$ must be estimated from a dedicated binary classifier rather than derived from a multi-class pipeline, as the latter suffers from decision boundary dilution (\\S\\ref{sec:atlas:edd:dilution}).\n\nFor each adjacent pair we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute $\\mathrm{AUC}(d, d{+}1)$ per Eq.~\\ref{eq:edd}.\n\nWithin the 4-class atlas (d0--d3), 7 of 9 cells achieve $\\mathrm{EDD}_{0.75}=3$; the two exceptions are Pythia and OLMo with top-$k$ sampling ($\\mathrm{EDD}_{0.75}=2$), consistent with top-$k$'s signal-attenuating effect noted in \\S\\ref{sec:atlas:indist}.\n\nWe extend the Pythia-1.4B nucleus pipeline to 6 depths (d0--d5) and train a 500-tree binary RF for each adjacent pair.\nFigure~\\ref{fig:auc_decay} shows the pairwise AUC decay curve.\nThe d0\\,vs.\\,d1 boundary is near-perfect (AUC\\,=\\,0.998), reflecting the well-known human--machine gap.\nSubsequent boundaries degrade monotonically: d1\\,vs.\\,d2 achieves 0.925 [95\\% CI: 0.914,\\,0.935], d2\\,vs.\\,d3 reaches 0.823 [0.805,\\,0.840], and d3\\,vs.\\,d4 yields 0.784 [0.765,\\,0.802]---with the confidence interval lower bound still exceeding $T{=}0.75$.\nAt d4\\,vs.\\,d5, AUC drops to 0.683 [0.661,\\,0.705], falling decisively below $T{=}0.75$ and placing $\\mathrm{EDD}_{0.75}$ at~4 for this configuration.\n\n\\paragraph{Cross-model AUC decay.}\nWe extend the d0--d5 binary pairwise pipeline to OLMo-1B and GPT-2~XL (both nucleus $p{=}0.95$).\nTable~\\ref{tab:cross_model_auc} reports the full decay curves.\nAll three models exhibit monotonic AUC decline with a characteristic inflection: d1\\,vs.\\,d2 AUC ranges from 0.925 to 0.968, d2\\,vs.\\,d3 from 0.823 to 0.919, and d3\\,vs.\\,d4 clusters tightly near 0.75 (range 0.750--0.784).\nAt d4\\,vs.\\,d5, AUC uniformly falls below 0.70 (range 0.681--0.684), with no model sustaining discriminability at conventional thresholds.\n\nThe statistical strength of the d3\\,vs.\\,d4 boundary varies across models despite directional agreement.\nBootstrap permutation tests comparing $\\mathrm{AUC}(d3,d4)$ and $\\mathrm{AUC}(d4,d5)$ yield $p{=}0.001$ for Pythia (the d3/d4 margin is reliably above d4/d5), $p{=}0.091$ for OLMo (marginal), and $p{=}0.505$ for GPT-2~XL (not statistically significant).\nThis stratification reflects the tightness of the AUC gap: all three models place d3\\,vs.\\,d4 above and d4\\,vs.\\,d5 below the $T{=}0.75$ line, but only Pythia's margin is large enough for conventional significance.\nWe therefore interpret EDD as a continuous decay profile rather than a single integer, noting that $\\mathrm{EDD}_{0.75}$ coincides at~4 across all three models while the underlying confidence varies substantially.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Binary pairwise AUC for adjacent depths across three models (nucleus $p{=}0.95$, d0--d5). d0\\,vs.\\,d1 omitted (AUC$\\geq$0.99 for all). $p$: bootstrap permutation test of $\\mathrm{AUC}(d3,d4) > \\mathrm{AUC}(d4,d5)$. Experiment IDs: \\texttt{depth\\_extension\\_binary\\_pairwise\\_002}, \\texttt{depth\\_extension\\_gpt2xl\\_d4d5\\_001}, \\texttt{depth\\_extension\\_olmo\\_d4d5\\_002}.}\n\\label{tab:cross_model_auc}\n\\begin{tabular}{lccccl}\n\\toprule\nModel & d1/d2 & d2/d3 & d3/d4 & d4/d5 & $p$ \\\\\n\\midrule\nPythia-1.4B & .925 & .823 & .784 & .683 & .001 \\\\\nGPT-2 XL & .966 & .919 & .750 & .681 & .505 \\\\\nOLMo-1B & .968 & .843 & .765 & .684 & .091 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_auc_decay.pdf}\n\\caption{Binary pairwise AUC between adjacent depths (Pythia-1.4B, nucleus $p{=}0.95$, d0--d5). Shaded bands: 95\\% bootstrap CI. Dashed line: $T{=}0.75$. $\\mathrm{EDD}_{0.75}=4$: depth pairs up to d3\\,vs.\\,d4 remain discriminable.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:edd_sensitivity} shows $\\mathrm{EDD}_T$ across all three models and four threshold choices.\nAll three models yield identical EDD at every $T$, reflecting the tight clustering of d3\\,vs.\\,d4 AUC near 0.75 and d4\\,vs.\\,d5 AUC near 0.68 (Table~\\ref{tab:cross_model_auc}).\nAt $T{=}0.65$, all pairs through d4\\,vs.\\,d5 pass, giving $\\mathrm{EDD}=5$; at $T{=}0.80$, the d3\\,vs.\\,d4 boundary falls below threshold for all models, yielding $\\mathrm{EDD}=3$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\mathrm{EDD}_T$ across three models (nucleus $p{=}0.95$) and four thresholds. All three models yield identical EDD at every $T$ despite differing pairwise AUC values (Table~\\ref{tab:cross_model_auc}). Experiment ID: \\texttt{granularity\\_ablation\\_rf\\_001}.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{cccc}\n\\toprule\n$T$ & Pythia-1.4B & GPT-2 XL & OLMo-1B \\\\\n\\midrule\n0.65 & 5 & 5 & 5 \\\\\n0.70 & 4 & 4 & 4 \\\\\n0.75 & 4 & 4 & 4 \\\\\n0.80 & 3 & 3 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Decision boundary dilution.}\n\\label{sec:atlas:edd:dilution}\nEDD's binary-pair design is motivated by \\emph{decision boundary dilution}: when a multi-class classifier must simultaneously separate $K$ depths, its decision boundaries are shared across all $\\binom{K}{2}$ class pairs, diluting the capacity allocated to any single adjacent pair.\nConcretely, in the Pythia nucleus setting (experiment \\texttt{granularity\\_ablation\\_rf\\_001}), the d2\\,vs.\\,d3 pairwise AUC degrades from 0.804 in a 4-class pipeline to 0.689 in a 6-class pipeline---a 14.3\\% relative decline---despite identical underlying data.\nMean classification accuracy likewise drops from 99.5\\% (binary) to 78.3\\% (4-class) to 62.9\\% (6-class).\nBecause the pairwise signal between depths $d$ and $d{+}1$ does not change when unrelated depths are added, this degradation is entirely attributable to boundary dilution, not signal loss.\nBinary pairwise classifiers eliminate this confound, isolating the true adjacent-pair discriminability that EDD is designed to measure.\n\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:trajectories}\n\nThe atlas reveals that decoding strategy does not merely scale the overall signal strength---it reshapes the degradation trajectory.\nFigure~\\ref{fig:feature_trajectory} plots normalized feature means across depths for three key features.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_feature_trajectory.pdf}\n\\caption{Normalized feature trajectories across generation depths for 3 models $\\times$ 2 strategies (nucleus $p{=}0.95$, temperature $\\tau{=}0.9$). All features decrease monotonically with depth, but inter-depth spacing is highly non-uniform. Top-$k$ results are provided in Appendix~\\ref{app:topk_trajectories}.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n\\paragraph{Non-uniform inter-depth spacing.}\nFor Pythia nucleus, \\textsc{p90\\_ppl} drops from 483.7 (d0) to 61.4 (d1)---an 87\\% reduction---but only from 29.7 (d2) to 18.2 (d3), a 39\\% reduction.\nThis geometric compression of the feature space explains why adjacent-pair AUC decays monotonically (Figure~\\ref{fig:auc_decay}): each successive generation step yields diminishing statistical displacement.\n\n\\paragraph{Temperature-induced acceleration.}\nTemperature sampling ($\\tau{=}0.9$) applies uniform logit scaling rather than the hard truncation of nucleus or top-$k$, which accelerates convergence toward the low-entropy attractor described by \\citet{marchi2024_heat_death}.\nConcretely, feature values at depth $N$ under temperature sampling approximate those at depth $N{+}1$ under nucleus or top-$k$.\nThis shift yields higher in-distribution accuracy (Table~\\ref{tab:main_matrix}) because each depth occupies a more distinct region of feature space, but it also means the d1/d2 boundary under temperature is closer to the d2/d3 boundary under nucleus---a mismatch that creates reversal risk in cross-strategy transfer (\\S\\ref{sec:generalization}).\n\n\\paragraph{Three-tier strategy taxonomy.}\nThe trajectory data suggests a functional classification.\nNucleus sampling ($p{=}0.95$) serves as a stable baseline with moderate signal strength.\nTemperature sampling ($\\tau{=}0.9$) enhances the signal via accelerated convergence, yielding higher within-strategy accuracy but strategy-specific depth boundaries.\nTop-$k$ sampling ($k{=}50$) attenuates the signal---accuracy drops 6--9 points relative to nucleus---because hard truncation at a fixed vocabulary size preserves more of the original distribution's shape across depths, compressing inter-depth distances.\nNotably, top-$k$ preserves the \\emph{direction} of all feature trends despite the magnitude reduction, which has implications for ordinal classifiers that rely on monotonicity (\\S\\ref{sec:generalization}).",
      "numLines": 169,
      "startLine": 1,
      "totalLines": 169
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

全部 4 项修改已完成：

1. **R1-N1 EDD 正式定义** (L60-67) — 添加了 Eq.1 公式 `EDD_T = max{d*: AUC(d*, d*+1) ≥ T}`，说明 T 含义，并前向引用 decision boundary dilution。

2. **D024/D027 连续衰减叙事** (L79-88) — 跨模型段落重写为 "Cross-model AUC decay"，报告三模型完整 AUC 衰减曲线 + bootstrap p-values（Pythia 0.001/OLMo 0.091/GPT-2 XL 0.505），强调方向一致性 + 统计强度分层，不做硬阈值判定。新增 Table `cross_model_auc` (L90-104)。

3. **EDD Sensitivity Table** (L117-132) — 扩展为三模型 × 四档 T 的 EDD 值表格，注明 experiment ID。

4. **Decision boundary dilution** (L134-140) — 从原来一句扩展为完整段落，解释多分类 softmax 边界稀释机制，引用 4-class→6-class d2v3 AUC 从 0.804 降至 0.689 (-14.3%) 的具体数据，添加 `\label{sec:atlas:edd:dilution}` 供前文交叉引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "uuid": "1433bd8f-4beb-4270-baa0-86e4813c5116",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014QaNNpmeuHNwvQqtbmLwS5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5078,
      "cache_read_input_tokens": 42779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5078
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

_source line 27_

全部 4 项修改已完成：

1. **R1-N1 EDD 正式定义** (L60-67) — 添加了 Eq.1 公式 `EDD_T = max{d*: AUC(d*, d*+1) ≥ T}`，说明 T 含义，并前向引用 decision boundary dilution。

2. **D024/D027 连续衰减叙事** (L79-88) — 跨模型段落重写为 "Cross-model AUC decay"，报告三模型完整 AUC 衰减曲线 + bootstrap p-values（Pythia 0.001/OLMo 0.091/GPT-2 XL 0.505），强调方向一致性 + 统计强度分层，不做硬阈值判定。新增 Table `cross_model_auc` (L90-104)。

3. **EDD Sensitivity Table** (L117-132) — 扩展为三模型 × 四档 T 的 EDD 值表格，注明 experiment ID。

4. **Decision boundary dilution** (L134-140) — 从原来一句扩展为完整段落，解释多分类 softmax 边界稀释机制，引用 4-class→6-class d2v3 AUC 从 0.804 降至 0.689 (-14.3%) 的具体数据，添加 `\label{sec:atlas:edd:dilution}` 供前文交叉引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 209803,
  "duration_api_ms": 210878,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "bf9a9230-f4a8-4013-bef4-d9e4a899c912",
  "total_cost_usd": 0.7317855,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 36016,
    "cache_read_input_tokens": 268643,
    "output_tokens": 14806,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36016,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 416,
        "cache_read_input_tokens": 42779,
        "cache_creation_input_tokens": 5078,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5078
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2074,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0021639999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 14806,
      "cacheReadInputTokens": 268643,
      "cacheCreationInputTokens": 36016,
      "webSearchRequests": 0,
      "costUSD": 0.7296215,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "716fb0ea-b86e-4934-a727-fca4f4c7b478"
}
```

</details>

---
