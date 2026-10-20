# paper math n250 revision

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_paper_math-n250-revision_20260515T090715.log`
- **Structured JSON:** [`f27804fa7c090b4ec8da.json`](../../sessions/f2/f27804fa7c090b4ec8da.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
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
  "uuid": "ebcbb6d3-6d4b-4ccd-94e0-d54a7618ba30",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/memory/"
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
    "resetsAt": 1778844600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a91b238e-41b1-4fee-9cee-b534b32b3667",
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the two files that need to be modified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "uuid": "1506d065-8832-4fb0-927a-bed957550d12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R41hmUfU4Ad9UMHn5XjUiH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11631,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11631
      },
      "output_tokens": 36,
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

<details open><summary>🔧 Tool call — Read · `toolu_01Pvon6y8hUfLT8kKbSKfDBY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "uuid": "11896bf8-37a5-436c-b1ee-9a4687a1d7b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R41hmUfU4Ad9UMHn5XjUiH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11631,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11631
      },
      "output_tokens": 36,
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

_source line 6 · 2026-05-15T09:07:36.131Z_

<details><summary>↩ Tool result · `toolu_01Pvon6y8hUfLT8kKbSKfDBY`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	
14	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
15	
16	\author{Anonymous}
17	
18	\begin{document}
19	\maketitle
20	
21	\input{abstract}
22	\input{introduction}
23	\input{method}
24	\input{experiments}
25	\input{related_work}
26	\input{conclusion}
27	
28	\section*{Limitations}
29	
30	Our analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. On the 135 episodes (55.1\%) where neither strategy leads to catastrophic failure, deterministic computation retains a small advantage ($\Delta_{\text{nd}} = +2.84$), indicating non-zero routing signal beyond death avoidance. Our analysis covers 11 of 30 ScienceWorld task types; the remaining 19 (63\%) were excluded during prescreening because both strategies timed out on all seed variations within the 30-step budget, providing no counterfactual signal. These tasks likely require longer-horizon planning; increasing the step budget could surface additional routing signal whose composition may differ from the death-dominated pattern observed here. Stronger models (e.g., 70B-scale or reasoning-specialized) likely exhibit lower internal-strategy death rates, which would reduce DAF. Our finding may reflect a capability-dependent failure mode: at higher capability levels, death avoidance may no longer dominate routing signal.
31	
32	\paragraph{Cross-environment evidence.}
33	A 300-problem MATH Level~4--5 evaluation (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, provides evidence beyond ScienceWorld. Internal reasoning achieved 81.7\% accuracy (95\% CI [77.3, 86.0]) versus 76.7\% for code interpreter (95\% CI [72.0, 81.3]). Although the individual CIs overlap, the paired difference of $+5.0$~percentage points (95\% CI [$+0.7$, $+9.3$]) excludes zero, constituting a statistically significant signal reversal favoring internal reasoning. Label distribution reflects weak routing signal: 88.7\% of problems show no modality preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage in ScienceWorld. An exploratory ALFWorld study \cite{alfworld-2021} (135 games, 6 task types) shows a related but mechanistically distinct pattern: 25.9\% of episodes are deterministic-preferred versus 1.5\% internal-preferred, with deterministic success rate (27.4\%) far exceeding internal (3.0\%). However, the underlying mechanism differs from ScienceWorld. In ScienceWorld, the internal strategy has baseline competence (57.1\% survival rate) but suffers hallucination-induced catastrophic failures; in ALFWorld, the 3\% internal success rate reflects a fundamental capability gap---without admissible action filtering, the agent rarely completes tasks at all. The deterministic advantage in ALFWorld thus stems from action space pruning rather than death avoidance per se. These results are suggestive but do not directly confirm that the DAF pattern generalizes; environments with intermediate failure modes remain to be studied.
34	
35	\paragraph{Step-level mislabeling.} Episode-level labels may assign suboptimal routing decisions to individual steps; in particular, steps preceding a death event are labeled det-preferred even if the death was not foreseeable from those steps' observations. Training on pure-strategy trajectories but deploying on mixed policy also introduces a distribution shift \citep{dagger-2011}.
36	
37	\paragraph{Scope.}
38	Extending the counterfactual methodology to environments with graded failure costs, embodied agents, or multi-turn dialogue systems would clarify how broadly death avoidance accounts for apparent routing signal. Step-level labeling with denser rewards and the logit--generation gap in the implicit router are natural next steps. We audit labeling quality in Appendix~\ref{app:labeling}.
39	
40	\section*{Ethics Statement}
41	
42	This work uses ScienceWorld \cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All language models are accessed via standard APIs or publicly released weights. We report computational costs: approximately 40 GPU-hours on two RTX 5090 GPUs for data collection, router training, and evaluation.
43	
44	\bibliography{references}
45	
46	\appendix
47	
48	\section{Labeling Quality Audit}
49	\label{app:labeling}
50	
51	A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine modality differences. We audit all 245 labels. Of the 150 \texttt{no\_preference} labels (61.2\%), 115 (46.9\%) are both-alive ties and 35 (14.3\%) are both-dead---all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields balanced accuracy of 57.3\%, within 1$\sigma$ of the full-label retrain (57.6 $\pm$ 0.5\%), confirming that score-comparison labels contribute negligible additional signal. The 97.4\% step-level tie rate (\S\ref{sec:collection}) further motivates episode-level over step-level labeling.
52	
53	\section{Per-Task Decomposition}
54	\label{app:per-task}
55	We select 11 of ScienceWorld's 30 task types via prescreening: task types where both strategies complete at least one episode within the 30-step budget are retained; types where both strategies time out on all seed variations are excluded.\footnote{Prescreening ensures that the counterfactual comparison is meaningful---task types where neither strategy makes progress provide no routing signal.}
56	
57	\begin{table}[h]
58	\centering
59	\scriptsize
60	\setlength{\tabcolsep}{2.5pt}
61	\begin{tabular}{@{}lrrccc@{}}
62	\toprule
63	Task & $n$ & $\Delta_\text{full}$ & D\%\textsubscript{int} & D\%\textsubscript{det} & D / I / N \\
64	\midrule
65	id-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\
66	lifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\
67	lifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\
68	inclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\
69	freeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\
70	meas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\
71	id-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\
72	find-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\
73	grow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\
74	chem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\
75	\midrule
76	find-non-living$^\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\
77	\midrule
78	\textbf{All (11 tasks)} & \textbf{245} & $\mathbf{+29.60}$ & \textbf{42.9} & \textbf{16.3} & \textbf{86 / 9 / 150} \\
79	\bottomrule
80	\end{tabular}
81	\caption{Per-task decomposition of the death avoidance effect. D\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\Delta_{\text{full}}$ descending. $\dagger$\,Only task with zero deaths under both strategies.}
82	\label{tab:per-task}
83	\end{table}
84	
85	\section{Correlation Robustness}
86	\label{app:correlation}
87	
88	The Pearson $r = 0.9698$ reported in \S\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\rho = 0.986$ ($p = 2.4 \times 10^{-8}$), confirming that the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\% CI $[0.952, 0.995]$.
89	
90	\begin{table}[h]
91	\centering
92	\small
93	\begin{tabular}{@{}lr@{}}
94	\toprule
95	Task removed & $r_{\text{LOO}}$ \\
96	\midrule
97	id-life-stages-1       & 0.963 \\
98	lifespan-long          & 0.969 \\
99	lifespan-l-then-s      & 0.976 \\
100	inclined-plane         & 0.969 \\
101	freeze                 & 0.971 \\
102	meas-melt-point        & 0.972 \\
103	id-life-stages-2       & 0.972 \\
104	find-animal            & 0.970 \\
105	grow-fruit             & 0.973 \\
106	chem-mix               & 0.969 \\
107	find-non-living        & 0.980 \\
108	\bottomrule
109	\end{tabular}
110	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
111	\label{tab:loo}
112	\end{table}
113	
114	\section{Router Training Details}
115	\label{app:router-details}
116	
117	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
118	
119	Gradient accumulation is critical for the implicit router: with gradient accumulation of 1, the model fails to achieve meaningful routing discrimination (internal recall 26.7\%); with gradient accumulation of 8, the model becomes non-degenerate (internal recall above 50\% across all seeds). All main-text results use gradient accumulation 8.
120	
121	Cross-seed balanced accuracy is stable (57--59\%), but internal recall varies from 51.5\% to 81.8\%, reflecting the structurally thin learnable signal: when ${\sim}90\%$ of routing value is death avoidance, the non-death signal is inherently noisy. Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
122	
123	\begin{table}[h]
124	\centering
125	\small
126	\begin{tabular}{@{}lcc@{}}
127	\toprule
128	Hyperparameter & Classification Head & Implicit Router \\
129	\midrule
130	Base model & Qwen3-1.7B & Qwen3-1.7B \\
131	Architecture & Linear + LoRA & SFT + LoRA \\
132	LoRA $r$ / $\alpha$ & 16 / 32 & 16 / 32 \\
133	Learning rate & 2e-5 & 2e-4 \\
134	Optimizer & AdamW & AdamW \\
135	Epochs & 3 & 3 \\
136	Batch size (per device) & 4 & 4 \\
137	Gradient accumulation & 8 & 8 \\
138	Warmup ratio & 0.1 & 0.1 \\
139	Weight decay & 0.01 & 0.01 \\
140	Max sequence length & 512 & 512 \\
141	Seeds & \{42\} & \{42, 123, 456, 789\} \\
142	\bottomrule
143	\end{tabular}
144	\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\pm$std.}
145	\label{tab:hyperparams}
146	\end{table}
147	
148	\section{Penalty Sensitivity Analysis}
149	\label{app:penalty}
150	
151	\begin{table}[h]
152	\centering
153	\small
154	\begin{tabular}{@{}rrrr@{}}
155	\toprule
156	$P$ & $\Delta_{\text{full}}(P)$ & $\Delta_{\text{nd}}$ & DAF($P$) \\
157	\midrule
158	10 & 5.72 & 3.07 & 46.4\% \\
159	25 & 9.70 & 3.07 & 68.4\% \\
160	50 & 16.33 & 3.07 & 81.2\% \\
161	100 & 29.60 & 3.07 & 89.6\%\textsuperscript{*} \\
162	200 & 56.13 & 3.07 & 94.5\% \\
163	\bottomrule
164	\end{tabular}
165	\caption{Sensitivity of $\Delta_{\text{full}}$ and DAF to death penalty magnitude $P$. $\Delta_{\text{full}}(P) = \delta \cdot P + \Delta_{\text{nd}}$, where $\delta = 0.2653$ is the death-rate differential. $\Delta_{\text{nd}} = 3.07$ here includes both-died episodes in the non-death pool, yielding DAF=89.6\% at $P{=}100$ versus 90.41\% in the main text (\S\ref{sec:death-decomp}), which uses strict neither-died filtering ($\Delta_{\text{nd}} = 2.84$). \textsuperscript{*}Default setting.}
166	\label{tab:penalty-sensitivity}
167	\end{table}
168	
169	\end{document}
170	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "uuid": "d5b6eb3d-d35d-46b3-b890-0a58406437d6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\n\\title{Death Avoidance as the Dominant Routing Signal:\\\\A Counterfactual Analysis on ScienceWorld}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\\input{introduction}\n\\input{method}\n\\input{experiments}\n\\input{related_work}\n\\input{conclusion}\n\n\\section*{Limitations}\n\nOur analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. On the 135 episodes (55.1\\%) where neither strategy leads to catastrophic failure, deterministic computation retains a small advantage ($\\Delta_{\\text{nd}} = +2.84$), indicating non-zero routing signal beyond death avoidance. Our analysis covers 11 of 30 ScienceWorld task types; the remaining 19 (63\\%) were excluded during prescreening because both strategies timed out on all seed variations within the 30-step budget, providing no counterfactual signal. These tasks likely require longer-horizon planning; increasing the step budget could surface additional routing signal whose composition may differ from the death-dominated pattern observed here. Stronger models (e.g., 70B-scale or reasoning-specialized) likely exhibit lower internal-strategy death rates, which would reduce DAF. Our finding may reflect a capability-dependent failure mode: at higher capability levels, death avoidance may no longer dominate routing signal.\n\n\\paragraph{Cross-environment evidence.}\nA 300-problem MATH Level~4--5 evaluation (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, provides evidence beyond ScienceWorld. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]). Although the individual CIs overlap, the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, constituting a statistically significant signal reversal favoring internal reasoning. Label distribution reflects weak routing signal: 88.7\\% of problems show no modality preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage in ScienceWorld. An exploratory ALFWorld study \\cite{alfworld-2021} (135 games, 6 task types) shows a related but mechanistically distinct pattern: 25.9\\% of episodes are deterministic-preferred versus 1.5\\% internal-preferred, with deterministic success rate (27.4\\%) far exceeding internal (3.0\\%). However, the underlying mechanism differs from ScienceWorld. In ScienceWorld, the internal strategy has baseline competence (57.1\\% survival rate) but suffers hallucination-induced catastrophic failures; in ALFWorld, the 3\\% internal success rate reflects a fundamental capability gap---without admissible action filtering, the agent rarely completes tasks at all. The deterministic advantage in ALFWorld thus stems from action space pruning rather than death avoidance per se. These results are suggestive but do not directly confirm that the DAF pattern generalizes; environments with intermediate failure modes remain to be studied.\n\n\\paragraph{Step-level mislabeling.} Episode-level labels may assign suboptimal routing decisions to individual steps; in particular, steps preceding a death event are labeled det-preferred even if the death was not foreseeable from those steps' observations. Training on pure-strategy trajectories but deploying on mixed policy also introduces a distribution shift \\citep{dagger-2011}.\n\n\\paragraph{Scope.}\nExtending the counterfactual methodology to environments with graded failure costs, embodied agents, or multi-turn dialogue systems would clarify how broadly death avoidance accounts for apparent routing signal. Step-level labeling with denser rewards and the logit--generation gap in the implicit router are natural next steps. We audit labeling quality in Appendix~\\ref{app:labeling}.\n\n\\section*{Ethics Statement}\n\nThis work uses ScienceWorld \\cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All language models are accessed via standard APIs or publicly released weights. We report computational costs: approximately 40 GPU-hours on two RTX 5090 GPUs for data collection, router training, and evaluation.\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Labeling Quality Audit}\n\\label{app:labeling}\n\nA potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine modality differences. We audit all 245 labels. Of the 150 \\texttt{no\\_preference} labels (61.2\\%), 115 (46.9\\%) are both-alive ties and 35 (14.3\\%) are both-dead---all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields balanced accuracy of 57.3\\%, within 1$\\sigma$ of the full-label retrain (57.6 $\\pm$ 0.5\\%), confirming that score-comparison labels contribute negligible additional signal. The 97.4\\% step-level tie rate (\\S\\ref{sec:collection}) further motivates episode-level over step-level labeling.\n\n\\section{Per-Task Decomposition}\n\\label{app:per-task}\nWe select 11 of ScienceWorld's 30 task types via prescreening: task types where both strategies complete at least one episode within the 30-step budget are retained; types where both strategies time out on all seed variations are excluded.\\footnote{Prescreening ensures that the counterfactual comparison is meaningful---task types where neither strategy makes progress provide no routing signal.}\n\n\\begin{table}[h]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{2.5pt}\n\\begin{tabular}{@{}lrrccc@{}}\n\\toprule\nTask & $n$ & $\\Delta_\\text{full}$ & D\\%\\textsubscript{int} & D\\%\\textsubscript{det} & D / I / N \\\\\n\\midrule\nid-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\\\\nlifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\\\\nlifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\\\\ninclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\\\\nfreeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\\\\nmeas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\\\\nid-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\\\\nfind-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\\\\ngrow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\\\\nchem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\\\\n\\midrule\nfind-non-living$^\\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\\\\n\\midrule\n\\textbf{All (11 tasks)} & \\textbf{245} & $\\mathbf{+29.60}$ & \\textbf{42.9} & \\textbf{16.3} & \\textbf{86 / 9 / 150} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-task decomposition of the death avoidance effect. D\\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\\Delta_{\\text{full}}$ descending. $\\dagger$\\,Only task with zero deaths under both strategies.}\n\\label{tab:per-task}\n\\end{table}\n\n\\section{Correlation Robustness}\n\\label{app:correlation}\n\nThe Pearson $r = 0.9698$ reported in \\S\\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\\rho = 0.986$ ($p = 2.4 \\times 10^{-8}$), confirming that the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\\% CI $[0.952, 0.995]$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nTask removed & $r_{\\text{LOO}}$ \\\\\n\\midrule\nid-life-stages-1       & 0.963 \\\\\nlifespan-long          & 0.969 \\\\\nlifespan-l-then-s      & 0.976 \\\\\ninclined-plane         & 0.969 \\\\\nfreeze                 & 0.971 \\\\\nmeas-melt-point        & 0.972 \\\\\nid-life-stages-2       & 0.972 \\\\\nfind-animal            & 0.970 \\\\\ngrow-fruit             & 0.973 \\\\\nchem-mix               & 0.969 \\\\\nfind-non-living        & 0.980 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\\ $\\Delta_{\\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}\n\\label{tab:loo}\n\\end{table}\n\n\\section{Router Training Details}\n\\label{app:router-details}\n\nWe use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.\n\nGradient accumulation is critical for the implicit router: with gradient accumulation of 1, the model fails to achieve meaningful routing discrimination (internal recall 26.7\\%); with gradient accumulation of 8, the model becomes non-degenerate (internal recall above 50\\% across all seeds). All main-text results use gradient accumulation 8.\n\nCross-seed balanced accuracy is stable (57--59\\%), but internal recall varies from 51.5\\% to 81.8\\%, reflecting the structurally thin learnable signal: when ${\\sim}90\\%$ of routing value is death avoidance, the non-death signal is inherently noisy. Deployed end-to-end, the trained router allocates 97.0\\% of episodes to deterministic computation with 17.6\\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nHyperparameter & Classification Head & Implicit Router \\\\\n\\midrule\nBase model & Qwen3-1.7B & Qwen3-1.7B \\\\\nArchitecture & Linear + LoRA & SFT + LoRA \\\\\nLoRA $r$ / $\\alpha$ & 16 / 32 & 16 / 32 \\\\\nLearning rate & 2e-5 & 2e-4 \\\\\nOptimizer & AdamW & AdamW \\\\\nEpochs & 3 & 3 \\\\\nBatch size (per device) & 4 & 4 \\\\\nGradient accumulation & 8 & 8 \\\\\nWarmup ratio & 0.1 & 0.1 \\\\\nWeight decay & 0.01 & 0.01 \\\\\nMax sequence length & 512 & 512 \\\\\nSeeds & \\{42\\} & \\{42, 123, 456, 789\\} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\\pm$std.}\n\\label{tab:hyperparams}\n\\end{table}\n\n\\section{Penalty Sensitivity Analysis}\n\\label{app:penalty}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}rrrr@{}}\n\\toprule\n$P$ & $\\Delta_{\\text{full}}(P)$ & $\\Delta_{\\text{nd}}$ & DAF($P$) \\\\\n\\midrule\n10 & 5.72 & 3.07 & 46.4\\% \\\\\n25 & 9.70 & 3.07 & 68.4\\% \\\\\n50 & 16.33 & 3.07 & 81.2\\% \\\\\n100 & 29.60 & 3.07 & 89.6\\%\\textsuperscript{*} \\\\\n200 & 56.13 & 3.07 & 94.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity of $\\Delta_{\\text{full}}$ and DAF to death penalty magnitude $P$. $\\Delta_{\\text{full}}(P) = \\delta \\cdot P + \\Delta_{\\text{nd}}$, where $\\delta = 0.2653$ is the death-rate differential. $\\Delta_{\\text{nd}} = 3.07$ here includes both-died episodes in the non-death pool, yielding DAF=89.6\\% at $P{=}100$ versus 90.41\\% in the main text (\\S\\ref{sec:death-decomp}), which uses strict neither-died filtering ($\\Delta_{\\text{nd}} = 2.84$). \\textsuperscript{*}Default setting.}\n\\label{tab:penalty-sensitivity}\n\\end{table}\n\n\\end{document}\n",
      "numLines": 170,
      "startLine": 1,
      "totalLines": 170
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_011BvxRD29E6qMCRMEqFyKCC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "uuid": "315f86c6-ef3e-430f-a1c3-c30e1c5903dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R41hmUfU4Ad9UMHn5XjUiH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11631,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11631
      },
      "output_tokens": 36,
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

_source line 8 · 2026-05-15T09:07:36.462Z_

<details><summary>↩ Tool result · `toolu_011BvxRD29E6qMCRMEqFyKCC`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Cross-environment evidence.}
5	The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A 300-problem evaluation on MATH Level~4--5 (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, suggests not---and in fact reverses. Internal reasoning achieved 81.7\% accuracy (95\% CI [77.3, 86.0]) versus 76.7\% for code interpreter (95\% CI [72.0, 81.3]); the paired difference of $+5.0$~percentage points (95\% CI [$+0.7$, $+9.3$]) excludes zero, a statistically significant reversal favoring internal reasoning. The contingency table (215 both-correct, 40 both-wrong, 30 only-internal-correct, 15 only-code-correct) shows that the majority of problems are modality-insensitive, with 88.7\% labeled no-preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld.
6	
7	\paragraph{Scope and future directions.}
8	Our analysis is grounded in a single interactive environment with a specific failure mode (the $-100$ death penalty). Extending the counterfactual methodology to environments with graded failure costs, embodied agents with continuous action spaces, or multi-turn dialogue systems would clarify how broadly death avoidance---or analogous catastrophic-failure avoidance---accounts for apparent routing signal. Step-level counterfactual labeling, rather than episode-level, is a complementary direction that could reveal finer-grained routing structure masked by our current aggregation.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "uuid": "6ea798cc-e236-464d-a0de-7b9b24f57cbd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Cross-environment evidence.}\nThe death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A 300-problem evaluation on MATH Level~4--5 (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, suggests not---and in fact reverses. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]); the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, a statistically significant reversal favoring internal reasoning. The contingency table (215 both-correct, 40 both-wrong, 30 only-internal-correct, 15 only-code-correct) shows that the majority of problems are modality-insensitive, with 88.7\\% labeled no-preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld.\n\n\\paragraph{Scope and future directions.}\nOur analysis is grounded in a single interactive environment with a specific failure mode (the $-100$ death penalty). Extending the counterfactual methodology to environments with graded failure costs, embodied agents with continuous action spaces, or multi-turn dialogue systems would clarify how broadly death avoidance---or analogous catastrophic-failure avoidance---accounts for apparent routing signal. Step-level counterfactual labeling, rather than episode-level, is a complementary direction that could reveal finer-grained routing structure masked by our current aggregation.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
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
Now I have both files. Let me make the edits.

For `main.tex` (line 32-33), the cross-environment evidence paragraph needs to be updated:
- N=250 instead of 300
- Updated numbers: 82.0% vs 77.6%, CI changes
- +4.4 pp, CI [−0.4, +9.2]
- Remove "statistically significant"
- Add footnote about excluding 50 pilot problems
- Update label counts for N=250

For `discussion.tex` (line 4-5), similar changes.


Since the accuracy numbers shifted when we removed the 50 pilot problems, the label distribution changed too, but I don't have the exact breakdown of which labels were in that subset. I'll either use proportional estimates based on the original distribution or note that these are counts from the 250 clean problems without specifying the exact label breakdown. I need to remove the contingency table numbers since I can't precisely reconstruct them from the N=250 dataset, and now I'm revising the main.tex paragraph to use the correct statistics: 82.0% for internal reasoning versus 77.6% for code, with the +4.4 percentage point difference and 88% no-preference rate that the task specifies. Looking at the MATH evaluation results, internal reasoning pulls ahead by 4.4 percentage points, but the confidence interval crosses zero so it's not a statistically significant win. The weak routing signal across both datasets suggests that without the death-risk penalty present in ScienceWorld, the deterministic approach loses its edge. Looking at the MATH Level 4-5 results, internal reasoning again outperforms code interpretation with an 82.0% versus 77.6% accuracy, though the 4.4 percentage point advantage doesn't quite reach statistical significance. The majority of problems show no preference between modalities, suggesting that without the death-avoidance pressure present in ScienceWorld, the routing signal fundamentally shifts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "uuid": "c2263deb-6981-49fb-9354-82af64958c8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6kGRRmVJANnLioMVRef23",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4981,
      "cache_read_input_tokens": 23472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4981
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

修改两个文件中的 Cross-environment evidence 段落。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "uuid": "ca673e28-4668-433c-bbca-5e334a579947",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6kGRRmVJANnLioMVRef23",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4981,
      "cache_read_input_tokens": 23472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4981
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

<details open><summary>🔧 Tool call — Edit · `toolu_01PGmbHNdFZDr6NSoT4qG4yZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "old_string": "\\paragraph{Cross-environment evidence.}\nA 300-problem MATH Level~4--5 evaluation (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, provides evidence beyond ScienceWorld. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]). Although the individual CIs overlap, the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, constituting a statistically significant signal reversal favoring internal reasoning. Label distribution reflects weak routing signal: 88.7\\% of problems show no modality preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage in ScienceWorld.",
  "new_string": "\\paragraph{Cross-environment evidence.}\nA MATH Level~4--5 evaluation (250 clean problems)\\footnote{We exclude 50 pilot problems affected by a sandbox execution bug that produced empty outputs for 32\\% of code-interpreter runs.}, using code interpreter as the deterministic modality, provides evidence beyond ScienceWorld. Internal reasoning achieved 82.0\\% accuracy (95\\% CI [77.2, 86.8]) versus 77.6\\% for code interpreter (95\\% CI [72.4, 82.4])---a directional reversal of $+4.4$~percentage points favoring internal reasoning, though not statistically significant at the 95\\% level (paired difference 95\\% CI [$-0.4$, $+9.2$] includes zero). Label distribution reflects weak routing signal: over 88\\% of the 250 problems show no modality preference. In the absence of death risk, the deterministic strategy's advantage vanishes---consistent with death avoidance as the primary driver of the routing signal observed in ScienceWorld."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "uuid": "78a0e2b0-6cfd-43cd-9fee-463f426ed47f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6kGRRmVJANnLioMVRef23",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4981,
      "cache_read_input_tokens": 23472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4981
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

_source line 12 · 2026-05-15T09:08:12.928Z_

<details><summary>↩ Tool result · `toolu_01PGmbHNdFZDr6NSoT4qG4yZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "uuid": "8de63673-0275-473a-971b-c6bb0c3554ed",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "oldString": "\\paragraph{Cross-environment evidence.}\nA 300-problem MATH Level~4--5 evaluation (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, provides evidence beyond ScienceWorld. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]). Although the individual CIs overlap, the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, constituting a statistically significant signal reversal favoring internal reasoning. Label distribution reflects weak routing signal: 88.7\\% of problems show no modality preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage in ScienceWorld.",
    "newString": "\\paragraph{Cross-environment evidence.}\nA MATH Level~4--5 evaluation (250 clean problems)\\footnote{We exclude 50 pilot problems affected by a sandbox execution bug that produced empty outputs for 32\\% of code-interpreter runs.}, using code interpreter as the deterministic modality, provides evidence beyond ScienceWorld. Internal reasoning achieved 82.0\\% accuracy (95\\% CI [77.2, 86.8]) versus 77.6\\% for code interpreter (95\\% CI [72.4, 82.4])---a directional reversal of $+4.4$~percentage points favoring internal reasoning, though not statistically significant at the 95\\% level (paired difference 95\\% CI [$-0.4$, $+9.2$] includes zero). Label distribution reflects weak routing signal: over 88\\% of the 250 problems show no modality preference. In the absence of death risk, the deterministic strategy's advantage vanishes---consistent with death avoidance as the primary driver of the routing signal observed in ScienceWorld.",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\n\\title{Death Avoidance as the Dominant Routing Signal:\\\\A Counterfactual Analysis on ScienceWorld}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\\input{introduction}\n\\input{method}\n\\input{experiments}\n\\input{related_work}\n\\input{conclusion}\n\n\\section*{Limitations}\n\nOur analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. On the 135 episodes (55.1\\%) where neither strategy leads to catastrophic failure, deterministic computation retains a small advantage ($\\Delta_{\\text{nd}} = +2.84$), indicating non-zero routing signal beyond death avoidance. Our analysis covers 11 of 30 ScienceWorld task types; the remaining 19 (63\\%) were excluded during prescreening because both strategies timed out on all seed variations within the 30-step budget, providing no counterfactual signal. These tasks likely require longer-horizon planning; increasing the step budget could surface additional routing signal whose composition may differ from the death-dominated pattern observed here. Stronger models (e.g., 70B-scale or reasoning-specialized) likely exhibit lower internal-strategy death rates, which would reduce DAF. Our finding may reflect a capability-dependent failure mode: at higher capability levels, death avoidance may no longer dominate routing signal.\n\n\\paragraph{Cross-environment evidence.}\nA 300-problem MATH Level~4--5 evaluation (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, provides evidence beyond ScienceWorld. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]). Although the individual CIs overlap, the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, constituting a statistically significant signal reversal favoring internal reasoning. Label distribution reflects weak routing signal: 88.7\\% of problems show no modality preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage in ScienceWorld. An exploratory ALFWorld study \\cite{alfworld-2021} (135 games, 6 task types) shows a related but mechanistically distinct pattern: 25.9\\% of episodes are deterministic-preferred versus 1.5\\% internal-preferred, with deterministic success rate (27.4\\%) far exceeding internal (3.0\\%). However, the underlying mechanism differs from ScienceWorld. In ScienceWorld, the internal strategy has baseline competence (57.1\\% survival rate) but suffers hallucination-induced catastrophic failures; in ALFWorld, the 3\\% internal success rate reflects a fundamental capability gap---without admissible action filtering, the agent rarely completes tasks at all. The deterministic advantage in ALFWorld thus stems from action space pruning rather than death avoidance per se. These results are suggestive but do not directly confirm that the DAF pattern generalizes; environments with intermediate failure modes remain to be studied.\n\n\\paragraph{Step-level mislabeling.} Episode-level labels may assign suboptimal routing decisions to individual steps; in particular, steps preceding a death event are labeled det-preferred even if the death was not foreseeable from those steps' observations. Training on pure-strategy trajectories but deploying on mixed policy also introduces a distribution shift \\citep{dagger-2011}.\n\n\\paragraph{Scope.}\nExtending the counterfactual methodology to environments with graded failure costs, embodied agents, or multi-turn dialogue systems would clarify how broadly death avoidance accounts for apparent routing signal. Step-level labeling with denser rewards and the logit--generation gap in the implicit router are natural next steps. We audit labeling quality in Appendix~\\ref{app:labeling}.\n\n\\section*{Ethics Statement}\n\nThis work uses ScienceWorld \\cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All language models are accessed via standard APIs or publicly released weights. We report computational costs: approximately 40 GPU-hours on two RTX 5090 GPUs for data collection, router training, and evaluation.\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Labeling Quality Audit}\n\\label{app:labeling}\n\nA potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine modality differences. We audit all 245 labels. Of the 150 \\texttt{no\\_preference} labels (61.2\\%), 115 (46.9\\%) are both-alive ties and 35 (14.3\\%) are both-dead---all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields balanced accuracy of 57.3\\%, within 1$\\sigma$ of the full-label retrain (57.6 $\\pm$ 0.5\\%), confirming that score-comparison labels contribute negligible additional signal. The 97.4\\% step-level tie rate (\\S\\ref{sec:collection}) further motivates episode-level over step-level labeling.\n\n\\section{Per-Task Decomposition}\n\\label{app:per-task}\nWe select 11 of ScienceWorld's 30 task types via prescreening: task types where both strategies complete at least one episode within the 30-step budget are retained; types where both strategies time out on all seed variations are excluded.\\footnote{Prescreening ensures that the counterfactual comparison is meaningful---task types where neither strategy makes progress provide no routing signal.}\n\n\\begin{table}[h]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{2.5pt}\n\\begin{tabular}{@{}lrrccc@{}}\n\\toprule\nTask & $n$ & $\\Delta_\\text{full}$ & D\\%\\textsubscript{int} & D\\%\\textsubscript{det} & D / I / N \\\\\n\\midrule\nid-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\\\\nlifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\\\\nlifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\\\\ninclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\\\\nfreeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\\\\nmeas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\\\\nid-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\\\\nfind-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\\\\ngrow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\\\\nchem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\\\\n\\midrule\nfind-non-living$^\\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\\\\n\\midrule\n\\textbf{All (11 tasks)} & \\textbf{245} & $\\mathbf{+29.60}$ & \\textbf{42.9} & \\textbf{16.3} & \\textbf{86 / 9 / 150} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-task decomposition of the death avoidance effect. D\\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\\Delta_{\\text{full}}$ descending. $\\dagger$\\,Only task with zero deaths under both strategies.}\n\\label{tab:per-task}\n\\end{table}\n\n\\section{Correlation Robustness}\n\\label{app:correlation}\n\nThe Pearson $r = 0.9698$ reported in \\S\\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\\rho = 0.986$ ($p = 2.4 \\times 10^{-8}$), confirming that the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\\% CI $[0.952, 0.995]$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nTask removed & $r_{\\text{LOO}}$ \\\\\n\\midrule\nid-life-stages-1       & 0.963 \\\\\nlifespan-long          & 0.969 \\\\\nlifespan-l-then-s      & 0.976 \\\\\ninclined-plane         & 0.969 \\\\\nfreeze                 & 0.971 \\\\\nmeas-melt-point        & 0.972 \\\\\nid-life-stages-2       & 0.972 \\\\\nfind-animal            & 0.970 \\\\\ngrow-fruit             & 0.973 \\\\\nchem-mix               & 0.969 \\\\\nfind-non-living        & 0.980 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\\ $\\Delta_{\\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}\n\\label{tab:loo}\n\\end{table}\n\n\\section{Router Training Details}\n\\label{app:router-details}\n\nWe use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.\n\nGradient accumulation is critical for the implicit router: with gradient accumulation of 1, the model fails to achieve meaningful routing discrimination (internal recall 26.7\\%); with gradient accumulation of 8, the model becomes non-degenerate (internal recall above 50\\% across all seeds). All main-text results use gradient accumulation 8.\n\nCross-seed balanced accuracy is stable (57--59\\%), but internal recall varies from 51.5\\% to 81.8\\%, reflecting the structurally thin learnable signal: when ${\\sim}90\\%$ of routing value is death avoidance, the non-death signal is inherently noisy. Deployed end-to-end, the trained router allocates 97.0\\% of episodes to deterministic computation with 17.6\\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nHyperparameter & Classification Head & Implicit Router \\\\\n\\midrule\nBase model & Qwen3-1.7B & Qwen3-1.7B \\\\\nArchitecture & Linear + LoRA & SFT + LoRA \\\\\nLoRA $r$ / $\\alpha$ & 16 / 32 & 16 / 32 \\\\\nLearning rate & 2e-5 & 2e-4 \\\\\nOptimizer & AdamW & AdamW \\\\\nEpochs & 3 & 3 \\\\\nBatch size (per device) & 4 & 4 \\\\\nGradient accumulation & 8 & 8 \\\\\nWarmup ratio & 0.1 & 0.1 \\\\\nWeight decay & 0.01 & 0.01 \\\\\nMax sequence length & 512 & 512 \\\\\nSeeds & \\{42\\} & \\{42, 123, 456, 789\\} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\\pm$std.}\n\\label{tab:hyperparams}\n\\end{table}\n\n\\section{Penalty Sensitivity Analysis}\n\\label{app:penalty}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}rrrr@{}}\n\\toprule\n$P$ & $\\Delta_{\\text{full}}(P)$ & $\\Delta_{\\text{nd}}$ & DAF($P$) \\\\\n\\midrule\n10 & 5.72 & 3.07 & 46.4\\% \\\\\n25 & 9.70 & 3.07 & 68.4\\% \\\\\n50 & 16.33 & 3.07 & 81.2\\% \\\\\n100 & 29.60 & 3.07 & 89.6\\%\\textsuperscript{*} \\\\\n200 & 56.13 & 3.07 & 94.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity of $\\Delta_{\\text{full}}$ and DAF to death penalty magnitude $P$. $\\Delta_{\\text{full}}(P) = \\delta \\cdot P + \\Delta_{\\text{nd}}$, where $\\delta = 0.2653$ is the death-rate differential. $\\Delta_{\\text{nd}} = 3.07$ here includes both-died episodes in the non-death pool, yielding DAF=89.6\\% at $P{=}100$ versus 90.41\\% in the main text (\\S\\ref{sec:death-decomp}), which uses strict neither-died filtering ($\\Delta_{\\text{nd}} = 2.84$). \\textsuperscript{*}Default setting.}\n\\label{tab:penalty-sensitivity}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 7,
        "newStart": 30,
        "newLines": 7,
        "lines": [
          " Our analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. On the 135 episodes (55.1\\%) where neither strategy leads to catastrophic failure, deterministic computation retains a small advantage ($\\Delta_{\\text{nd}} = +2.84$), indicating non-zero routing signal beyond death avoidance. Our analysis covers 11 of 30 ScienceWorld task types; the remaining 19 (63\\%) were excluded during prescreening because both strategies timed out on all seed variations within the 30-step budget, providing no counterfactual signal. These tasks likely require longer-horizon planning; increasing the step budget could surface additional routing signal whose composition may differ from the death-dominated pattern observed here. Stronger models (e.g., 70B-scale or reasoning-specialized) likely exhibit lower internal-strategy death rates, which would reduce DAF. Our finding may reflect a capability-dependent failure mode: at higher capability levels, death avoidance may no longer dominate routing signal.",
          " ",
          " \\paragraph{Cross-environment evidence.}",
          "-A 300-problem MATH Level~4--5 evaluation (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, provides evidence beyond ScienceWorld. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]). Although the individual CIs overlap, the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, constituting a statistically significant signal reversal favoring internal reasoning. Label distribution reflects weak routing signal: 88.7\\% of problems show no modality preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage in ScienceWorld. An exploratory ALFWorld study \\cite{alfworld-2021} (135 games, 6 task types) shows a related but mechanistically distinct pattern: 25.9\\% of episodes are deterministic-preferred versus 1.5\\% internal-preferred, with deterministic success rate (27.4\\%) far exceeding internal (3.0\\%). However, the underlying mechanism differs from ScienceWorld. In ScienceWorld, the internal strategy has baseline competence (57.1\\% survival rate) but suffers hallucination-induced catastrophic failures; in ALFWorld, the 3\\% internal success rate reflects a fundamental capability gap---without admissible action filtering, the agent rarely completes tasks at all. The deterministic advantage in ALFWorld thus stems from action space pruning rather than death avoidance per se. These results are suggestive but do not directly confirm that the DAF pattern generalizes; environments with intermediate failure modes remain to be studied.",
          "+A MATH Level~4--5 evaluation (250 clean problems)\\footnote{We exclude 50 pilot problems affected by a sandbox execution bug that produced empty outputs for 32\\% of code-interpreter runs.}, using code interpreter as the deterministic modality, provides evidence beyond ScienceWorld. Internal reasoning achieved 82.0\\% accuracy (95\\% CI [77.2, 86.8]) versus 77.6\\% for code interpreter (95\\% CI [72.4, 82.4])---a directional reversal of $+4.4$~percentage points favoring internal reasoning, though not statistically significant at the 95\\% level (paired difference 95\\% CI [$-0.4$, $+9.2$] includes zero). Label distribution reflects weak routing signal: over 88\\% of the 250 problems show no modality preference. In the absence of death risk, the deterministic strategy's advantage vanishes---consistent with death avoidance as the primary driver of the routing signal observed in ScienceWorld. An exploratory ALFWorld study \\cite{alfworld-2021} (135 games, 6 task types) shows a related but mechanistically distinct pattern: 25.9\\% of episodes are deterministic-preferred versus 1.5\\% internal-preferred, with deterministic success rate (27.4\\%) far exceeding internal (3.0\\%). However, the underlying mechanism differs from ScienceWorld. In ScienceWorld, the internal strategy has baseline competence (57.1\\% survival rate) but suffers hallucination-induced catastrophic failures; in ALFWorld, the 3\\% internal success rate reflects a fundamental capability gap---without admissible action filtering, the agent rarely completes tasks at all. The deterministic advantage in ALFWorld thus stems from action space pruning rather than death avoidance per se. These results are suggestive but do not directly confirm that the DAF pattern generalizes; environments with intermediate failure modes remain to be studied.",
          " ",
          " \\paragraph{Step-level mislabeling.} Episode-level labels may assign suboptimal routing decisions to individual steps; in particular, steps preceding a death event are labeled det-preferred even if the death was not foreseeable from those steps' observations. Training on pure-strategy trajectories but deploying on mixed policy also introduces a distribution shift \\citep{dagger-2011}.",
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01KveY1xWKqzD8Wju77hcetT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex",
  "old_string": "\\paragraph{Cross-environment evidence.}\nThe death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A 300-problem evaluation on MATH Level~4--5 (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, suggests not---and in fact reverses. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]); the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, a statistically significant reversal favoring internal reasoning. The contingency table (215 both-correct, 40 both-wrong, 30 only-internal-correct, 15 only-code-correct) shows that the majority of problems are modality-insensitive, with 88.7\\% labeled no-preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld.",
  "new_string": "\\paragraph{Cross-environment evidence.}\nThe death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? An evaluation on MATH Level~4--5 (250 clean problems; we exclude 50 pilot problems affected by a sandbox execution bug that produced empty outputs for 32\\% of code-interpreter runs), using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 82.0\\% accuracy (95\\% CI [77.2, 86.8]) versus 77.6\\% for code interpreter (95\\% CI [72.4, 82.4]); the paired difference of $+4.4$~percentage points (95\\% CI [$-0.4$, $+9.2$]) shows a directional reversal favoring internal reasoning, though not statistically significant at the 95\\% level. Over 88\\% of the 250 problems are labeled no-preference, indicating that most problems are modality-insensitive. In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "uuid": "666b757f-b3ef-4ca6-906b-27ffdc7ea475",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6kGRRmVJANnLioMVRef23",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4981,
      "cache_read_input_tokens": 23472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4981
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

_source line 14 · 2026-05-15T09:08:17.596Z_

<details><summary>↩ Tool result · `toolu_01KveY1xWKqzD8Wju77hcetT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "uuid": "394cc6ab-426f-43a7-b65d-d9bce02f0e81",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex",
    "oldString": "\\paragraph{Cross-environment evidence.}\nThe death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A 300-problem evaluation on MATH Level~4--5 (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, suggests not---and in fact reverses. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]); the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, a statistically significant reversal favoring internal reasoning. The contingency table (215 both-correct, 40 both-wrong, 30 only-internal-correct, 15 only-code-correct) shows that the majority of problems are modality-insensitive, with 88.7\\% labeled no-preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld.",
    "newString": "\\paragraph{Cross-environment evidence.}\nThe death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? An evaluation on MATH Level~4--5 (250 clean problems; we exclude 50 pilot problems affected by a sandbox execution bug that produced empty outputs for 32\\% of code-interpreter runs), using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 82.0\\% accuracy (95\\% CI [77.2, 86.8]) versus 77.6\\% for code interpreter (95\\% CI [72.4, 82.4]); the paired difference of $+4.4$~percentage points (95\\% CI [$-0.4$, $+9.2$]) shows a directional reversal favoring internal reasoning, though not statistically significant at the 95\\% level. Over 88\\% of the 250 problems are labeled no-preference, indicating that most problems are modality-insensitive. In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Cross-environment evidence.}\nThe death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A 300-problem evaluation on MATH Level~4--5 (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, suggests not---and in fact reverses. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]); the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, a statistically significant reversal favoring internal reasoning. The contingency table (215 both-correct, 40 both-wrong, 30 only-internal-correct, 15 only-code-correct) shows that the majority of problems are modality-insensitive, with 88.7\\% labeled no-preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld.\n\n\\paragraph{Scope and future directions.}\nOur analysis is grounded in a single interactive environment with a specific failure mode (the $-100$ death penalty). Extending the counterfactual methodology to environments with graded failure costs, embodied agents with continuous action spaces, or multi-turn dialogue systems would clarify how broadly death avoidance---or analogous catastrophic-failure avoidance---accounts for apparent routing signal. Step-level counterfactual labeling, rather than episode-level, is a complementary direction that could reveal finer-grained routing structure masked by our current aggregation.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " \\label{sec:discussion}",
          " ",
          " \\paragraph{Cross-environment evidence.}",
          "-The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A 300-problem evaluation on MATH Level~4--5 (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, suggests not---and in fact reverses. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]); the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, a statistically significant reversal favoring internal reasoning. The contingency table (215 both-correct, 40 both-wrong, 30 only-internal-correct, 15 only-code-correct) shows that the majority of problems are modality-insensitive, with 88.7\\% labeled no-preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld.",
          "+The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? An evaluation on MATH Level~4--5 (250 clean problems; we exclude 50 pilot problems affected by a sandbox execution bug that produced empty outputs for 32\\% of code-interpreter runs), using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 82.0\\% accuracy (95\\% CI [77.2, 86.8]) versus 77.6\\% for code interpreter (95\\% CI [72.4, 82.4]); the paired difference of $+4.4$~percentage points (95\\% CI [$-0.4$, $+9.2$]) shows a directional reversal favoring internal reasoning, though not statistically significant at the 95\\% level. Over 88\\% of the 250 problems are labeled no-preference, indicating that most problems are modality-insensitive. In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld.",
          " ",
          " \\paragraph{Scope and future directions.}",
          " Our analysis is grounded in a single interactive environment with a specific failure mode (the $-100$ death penalty). Extending the counterfactual methodology to environments with graded failure costs, embodied agents with continuous action spaces, or multi-turn dialogue systems would clarify how broadly death avoidance---or analogous catastrophic-failure avoidance---accounts for apparent routing signal. Step-level counterfactual labeling, rather than episode-level, is a complementary direction that could reveal finer-grained routing structure masked by our current aggregation."
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

_source line 15_

两个文件已更新。变更摘要：

**main.tex** (Limitations → Cross-environment evidence):
- N=300 → N=250 clean problems，加脚注说明排除 50 pilot 题及原因
- 数字更新：81.7/76.7 → 82.0/77.6，CI 对应更新，差异 +5.0 → +4.4
- "statistically significant signal reversal" → "directional reversal … though not statistically significant at the 95% level"
- 删除具体 label 计数（9/25/266），改为 "over 88% of the 250 problems"
- "routing signal reverses" → "deterministic strategy's advantage vanishes"

**discussion.tex** (Discussion → Cross-environment evidence):
- 同样的数字和措辞更新
- 删除 contingency table 具体数字（215/40/30/15）
- "suggests not---and in fact reverses" → "suggests not"（去掉过强措辞）
- "routing signal reverses" → "routing signal vanishes or reverses"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "uuid": "96b348d8-ae0e-4e72-a733-05ea69dcd059",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSCzqdvvgvVM1xbF8uxpJV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3185,
      "cache_read_input_tokens": 28453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3185
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

_source line 16_

两个文件已更新。变更摘要：

**main.tex** (Limitations → Cross-environment evidence):
- N=300 → N=250 clean problems，加脚注说明排除 50 pilot 题及原因
- 数字更新：81.7/76.7 → 82.0/77.6，CI 对应更新，差异 +5.0 → +4.4
- "statistically significant signal reversal" → "directional reversal … though not statistically significant at the 95% level"
- 删除具体 label 计数（9/25/266），改为 "over 88% of the 250 problems"
- "routing signal reverses" → "deterministic strategy's advantage vanishes"

**discussion.tex** (Discussion → Cross-environment evidence):
- 同样的数字和措辞更新
- 删除 contingency table 具体数字（215/40/30/15）
- "suggests not---and in fact reverses" → "suggests not"（去掉过强措辞）
- "routing signal reverses" → "routing signal vanishes or reverses"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 58917,
  "duration_api_ms": 59947,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "f30fc496-1bf9-4902-be17-7267eb05a90f",
  "total_cost_usd": 0.24422925,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 19797,
    "cache_read_input_tokens": 63766,
    "output_tokens": 3480,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 19797,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 286,
        "cache_read_input_tokens": 28453,
        "cache_creation_input_tokens": 3185,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3185
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1495,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00159,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 3480,
      "cacheReadInputTokens": 63766,
      "cacheCreationInputTokens": 19797,
      "webSearchRequests": 0,
      "costUSD": 0.24263925000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "56db720f-e0d0-411c-b785-09a822c53209"
}
```

</details>

---
