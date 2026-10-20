# paper long paper math update

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_paper_long-paper-math-update_20260515T090022.log`
- **Structured JSON:** [`3f045c48245bfca1680f.json`](../../sessions/3f/3f045c48245bfca1680f.json)

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
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
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
  "uuid": "a55b03c7-3077-4ce5-9bf5-4f9e80b82498",
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
  "uuid": "48521d60-68ff-4aed-ba9a-8cd0acba9843",
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76"
}
```

---

### Assistant

_source line 4_

Let me read the two files that need updating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "uuid": "7b41144b-9fe1-4834-94ea-e6bfc6039171",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012cPYC6rS46rNwNAHFcWQMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11622,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11622
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

<details open><summary>🔧 Tool call — Read · `toolu_01VgsA2C6qt1W26XF86YwQMA`</summary>

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
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "uuid": "fe313673-e861-4a42-89a8-a24033e79912",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012cPYC6rS46rNwNAHFcWQMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11622,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11622
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

_source line 6 · 2026-05-15T09:00:34.892Z_

<details><summary>↩ Tool result · `toolu_01VgsA2C6qt1W26XF86YwQMA`</summary>

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
33	A preliminary 50-problem MATH Level~4--5 pilot, using code interpreter as the deterministic modality, provides initial evidence beyond ScienceWorld. Internal reasoning achieved 80\% accuracy (95\% CI [66, 90]) versus 72\% for code interpreter (95\% CI [58, 84]); overlapping CIs confirm this is a preliminary signal, with 88\% of problems showing no modality preference (1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver. An exploratory ALFWorld study \cite{alfworld-2021} (135 games, 6 task types) shows a related but mechanistically distinct pattern: 25.9\% of episodes are deterministic-preferred versus 1.5\% internal-preferred, with deterministic success rate (27.4\%) far exceeding internal (3.0\%). However, the underlying mechanism differs from ScienceWorld. In ScienceWorld, the internal strategy has baseline competence (57.1\% survival rate) but suffers hallucination-induced catastrophic failures; in ALFWorld, the 3\% internal success rate reflects a fundamental capability gap---without admissible action filtering, the agent rarely completes tasks at all. The deterministic advantage in ALFWorld thus stems from action space pruning rather than death avoidance per se. These results are suggestive but do not directly confirm that the DAF pattern generalizes; environments with intermediate failure modes remain to be studied.
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
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "uuid": "a38545b6-c017-4919-8998-e7883b6598c4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\n\\title{Death Avoidance as the Dominant Routing Signal:\\\\A Counterfactual Analysis on ScienceWorld}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\\input{introduction}\n\\input{method}\n\\input{experiments}\n\\input{related_work}\n\\input{conclusion}\n\n\\section*{Limitations}\n\nOur analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. On the 135 episodes (55.1\\%) where neither strategy leads to catastrophic failure, deterministic computation retains a small advantage ($\\Delta_{\\text{nd}} = +2.84$), indicating non-zero routing signal beyond death avoidance. Our analysis covers 11 of 30 ScienceWorld task types; the remaining 19 (63\\%) were excluded during prescreening because both strategies timed out on all seed variations within the 30-step budget, providing no counterfactual signal. These tasks likely require longer-horizon planning; increasing the step budget could surface additional routing signal whose composition may differ from the death-dominated pattern observed here. Stronger models (e.g., 70B-scale or reasoning-specialized) likely exhibit lower internal-strategy death rates, which would reduce DAF. Our finding may reflect a capability-dependent failure mode: at higher capability levels, death avoidance may no longer dominate routing signal.\n\n\\paragraph{Cross-environment evidence.}\nA preliminary 50-problem MATH Level~4--5 pilot, using code interpreter as the deterministic modality, provides initial evidence beyond ScienceWorld. Internal reasoning achieved 80\\% accuracy (95\\% CI [66, 90]) versus 72\\% for code interpreter (95\\% CI [58, 84]); overlapping CIs confirm this is a preliminary signal, with 88\\% of problems showing no modality preference (1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver. An exploratory ALFWorld study \\cite{alfworld-2021} (135 games, 6 task types) shows a related but mechanistically distinct pattern: 25.9\\% of episodes are deterministic-preferred versus 1.5\\% internal-preferred, with deterministic success rate (27.4\\%) far exceeding internal (3.0\\%). However, the underlying mechanism differs from ScienceWorld. In ScienceWorld, the internal strategy has baseline competence (57.1\\% survival rate) but suffers hallucination-induced catastrophic failures; in ALFWorld, the 3\\% internal success rate reflects a fundamental capability gap---without admissible action filtering, the agent rarely completes tasks at all. The deterministic advantage in ALFWorld thus stems from action space pruning rather than death avoidance per se. These results are suggestive but do not directly confirm that the DAF pattern generalizes; environments with intermediate failure modes remain to be studied.\n\n\\paragraph{Step-level mislabeling.} Episode-level labels may assign suboptimal routing decisions to individual steps; in particular, steps preceding a death event are labeled det-preferred even if the death was not foreseeable from those steps' observations. Training on pure-strategy trajectories but deploying on mixed policy also introduces a distribution shift \\citep{dagger-2011}.\n\n\\paragraph{Scope.}\nExtending the counterfactual methodology to environments with graded failure costs, embodied agents, or multi-turn dialogue systems would clarify how broadly death avoidance accounts for apparent routing signal. Step-level labeling with denser rewards and the logit--generation gap in the implicit router are natural next steps. We audit labeling quality in Appendix~\\ref{app:labeling}.\n\n\\section*{Ethics Statement}\n\nThis work uses ScienceWorld \\cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All language models are accessed via standard APIs or publicly released weights. We report computational costs: approximately 40 GPU-hours on two RTX 5090 GPUs for data collection, router training, and evaluation.\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Labeling Quality Audit}\n\\label{app:labeling}\n\nA potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine modality differences. We audit all 245 labels. Of the 150 \\texttt{no\\_preference} labels (61.2\\%), 115 (46.9\\%) are both-alive ties and 35 (14.3\\%) are both-dead---all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields balanced accuracy of 57.3\\%, within 1$\\sigma$ of the full-label retrain (57.6 $\\pm$ 0.5\\%), confirming that score-comparison labels contribute negligible additional signal. The 97.4\\% step-level tie rate (\\S\\ref{sec:collection}) further motivates episode-level over step-level labeling.\n\n\\section{Per-Task Decomposition}\n\\label{app:per-task}\nWe select 11 of ScienceWorld's 30 task types via prescreening: task types where both strategies complete at least one episode within the 30-step budget are retained; types where both strategies time out on all seed variations are excluded.\\footnote{Prescreening ensures that the counterfactual comparison is meaningful---task types where neither strategy makes progress provide no routing signal.}\n\n\\begin{table}[h]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{2.5pt}\n\\begin{tabular}{@{}lrrccc@{}}\n\\toprule\nTask & $n$ & $\\Delta_\\text{full}$ & D\\%\\textsubscript{int} & D\\%\\textsubscript{det} & D / I / N \\\\\n\\midrule\nid-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\\\\nlifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\\\\nlifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\\\\ninclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\\\\nfreeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\\\\nmeas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\\\\nid-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\\\\nfind-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\\\\ngrow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\\\\nchem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\\\\n\\midrule\nfind-non-living$^\\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\\\\n\\midrule\n\\textbf{All (11 tasks)} & \\textbf{245} & $\\mathbf{+29.60}$ & \\textbf{42.9} & \\textbf{16.3} & \\textbf{86 / 9 / 150} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-task decomposition of the death avoidance effect. D\\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\\Delta_{\\text{full}}$ descending. $\\dagger$\\,Only task with zero deaths under both strategies.}\n\\label{tab:per-task}\n\\end{table}\n\n\\section{Correlation Robustness}\n\\label{app:correlation}\n\nThe Pearson $r = 0.9698$ reported in \\S\\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\\rho = 0.986$ ($p = 2.4 \\times 10^{-8}$), confirming that the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\\% CI $[0.952, 0.995]$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nTask removed & $r_{\\text{LOO}}$ \\\\\n\\midrule\nid-life-stages-1       & 0.963 \\\\\nlifespan-long          & 0.969 \\\\\nlifespan-l-then-s      & 0.976 \\\\\ninclined-plane         & 0.969 \\\\\nfreeze                 & 0.971 \\\\\nmeas-melt-point        & 0.972 \\\\\nid-life-stages-2       & 0.972 \\\\\nfind-animal            & 0.970 \\\\\ngrow-fruit             & 0.973 \\\\\nchem-mix               & 0.969 \\\\\nfind-non-living        & 0.980 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\\ $\\Delta_{\\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}\n\\label{tab:loo}\n\\end{table}\n\n\\section{Router Training Details}\n\\label{app:router-details}\n\nWe use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.\n\nGradient accumulation is critical for the implicit router: with gradient accumulation of 1, the model fails to achieve meaningful routing discrimination (internal recall 26.7\\%); with gradient accumulation of 8, the model becomes non-degenerate (internal recall above 50\\% across all seeds). All main-text results use gradient accumulation 8.\n\nCross-seed balanced accuracy is stable (57--59\\%), but internal recall varies from 51.5\\% to 81.8\\%, reflecting the structurally thin learnable signal: when ${\\sim}90\\%$ of routing value is death avoidance, the non-death signal is inherently noisy. Deployed end-to-end, the trained router allocates 97.0\\% of episodes to deterministic computation with 17.6\\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nHyperparameter & Classification Head & Implicit Router \\\\\n\\midrule\nBase model & Qwen3-1.7B & Qwen3-1.7B \\\\\nArchitecture & Linear + LoRA & SFT + LoRA \\\\\nLoRA $r$ / $\\alpha$ & 16 / 32 & 16 / 32 \\\\\nLearning rate & 2e-5 & 2e-4 \\\\\nOptimizer & AdamW & AdamW \\\\\nEpochs & 3 & 3 \\\\\nBatch size (per device) & 4 & 4 \\\\\nGradient accumulation & 8 & 8 \\\\\nWarmup ratio & 0.1 & 0.1 \\\\\nWeight decay & 0.01 & 0.01 \\\\\nMax sequence length & 512 & 512 \\\\\nSeeds & \\{42\\} & \\{42, 123, 456, 789\\} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\\pm$std.}\n\\label{tab:hyperparams}\n\\end{table}\n\n\\section{Penalty Sensitivity Analysis}\n\\label{app:penalty}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}rrrr@{}}\n\\toprule\n$P$ & $\\Delta_{\\text{full}}(P)$ & $\\Delta_{\\text{nd}}$ & DAF($P$) \\\\\n\\midrule\n10 & 5.72 & 3.07 & 46.4\\% \\\\\n25 & 9.70 & 3.07 & 68.4\\% \\\\\n50 & 16.33 & 3.07 & 81.2\\% \\\\\n100 & 29.60 & 3.07 & 89.6\\%\\textsuperscript{*} \\\\\n200 & 56.13 & 3.07 & 94.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity of $\\Delta_{\\text{full}}$ and DAF to death penalty magnitude $P$. $\\Delta_{\\text{full}}(P) = \\delta \\cdot P + \\Delta_{\\text{nd}}$, where $\\delta = 0.2653$ is the death-rate differential. $\\Delta_{\\text{nd}} = 3.07$ here includes both-died episodes in the non-death pool, yielding DAF=89.6\\% at $P{=}100$ versus 90.41\\% in the main text (\\S\\ref{sec:death-decomp}), which uses strict neither-died filtering ($\\Delta_{\\text{nd}} = 2.84$). \\textsuperscript{*}Default setting.}\n\\label{tab:penalty-sensitivity}\n\\end{table}\n\n\\end{document}\n",
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

<details open><summary>🔧 Tool call — Read · `toolu_01ReD7jd1tQk26AJY7s6NJ8e`</summary>

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
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "uuid": "751cdbd9-2fc5-457b-a029-5af37abf3516",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012cPYC6rS46rNwNAHFcWQMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11622,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11622
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

_source line 8 · 2026-05-15T09:00:35.419Z_

<details><summary>↩ Tool result · `toolu_01ReD7jd1tQk26AJY7s6NJ8e`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Cross-environment evidence.}
5	The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A preliminary 50-problem pilot on MATH Level~4--5, using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 80\% accuracy versus 72\% for code interpreter, with 88\% of problems showing no modality preference (label distribution: 1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld. The pilot study used a code sandbox with a known bug (bare expressions returned empty output), which may slightly underestimate code-interpreter accuracy; a post-fix replication on a different 55-question subset shows the same qualitative trend. A larger-scale replication with improved code execution is in progress.
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
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "uuid": "210da565-c0c2-4f3a-9968-7791d851e5d5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Cross-environment evidence.}\nThe death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A preliminary 50-problem pilot on MATH Level~4--5, using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 80\\% accuracy versus 72\\% for code interpreter, with 88\\% of problems showing no modality preference (label distribution: 1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld. The pilot study used a code sandbox with a known bug (bare expressions returned empty output), which may slightly underestimate code-interpreter accuracy; a post-fix replication on a different 55-question subset shows the same qualitative trend. A larger-scale replication with improved code execution is in progress.\n\n\\paragraph{Scope and future directions.}\nOur analysis is grounded in a single interactive environment with a specific failure mode (the $-100$ death penalty). Extending the counterfactual methodology to environments with graded failure costs, embodied agents with continuous action spaces, or multi-turn dialogue systems would clarify how broadly death avoidance---or analogous catastrophic-failure avoidance---accounts for apparent routing signal. Step-level counterfactual labeling, rather than episode-level, is a complementary direction that could reveal finer-grained routing structure masked by our current aggregation.\n",
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

````text
Now I have both files. Let me update them.

**main.tex** (lines 32-33): The "Cross-environment evidence" paragraph in the Limitations section needs updating.

**discussion.tex** (lines 4-5): The "Cross-environment evidence" paragraph needs updating.

Let me craft the updates.

For main.tex line 32-33, the current text is:
```
A preliminary 50-problem MATH Level~4--5 pilot, using code interpreter as the deterministic modality, provides initial evidence beyond ScienceWorld. 

Internal reasoning achieved 80\% accuracy (95\% CI [66, 90]) versus 72\% for code interpreter (95\% CI [58, 84]); overlapping CIs confirm this is a preliminary signal, with 88\% of problems showing no modality preference (1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver.
```

I'm now looking at the expanded dataset with 300 MATH problems across Levels 4 and 5, where internal reasoning achieved 81.7% accuracy compared to code interpreter's performance, with updated confidence intervals reflecting the larger sample size.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "uuid": "ed4ad5ac-195c-41da-98fc-2a360e685771",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gpiQ4cHANDzjRTGUg9gFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4799,
      "cache_read_input_tokens": 23463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4799
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

Now I'll update both paragraphs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "uuid": "b7815060-8ee9-4432-92a9-b38ab37baa5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gpiQ4cHANDzjRTGUg9gFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4799,
      "cache_read_input_tokens": 23463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4799
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

<details open><summary>🔧 Tool call — Edit · `toolu_01X6DGHDsBrk3kncuMf4Zwwf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "old_string": "A preliminary 50-problem MATH Level~4--5 pilot, using code interpreter as the deterministic modality, provides initial evidence beyond ScienceWorld. Internal reasoning achieved 80\\% accuracy (95\\% CI [66, 90]) versus 72\\% for code interpreter (95\\% CI [58, 84]); overlapping CIs confirm this is a preliminary signal, with 88\\% of problems showing no modality preference (1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver.",
  "new_string": "A 300-problem MATH Level~4--5 evaluation (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, provides evidence beyond ScienceWorld. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]). Although the individual CIs overlap, the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, constituting a statistically significant signal reversal favoring internal reasoning. Label distribution reflects weak routing signal: 88.7\\% of problems show no modality preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage in ScienceWorld."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "uuid": "ac95affc-5352-4d99-ae2a-76bc70dcf802",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gpiQ4cHANDzjRTGUg9gFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4799,
      "cache_read_input_tokens": 23463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4799
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

_source line 12 · 2026-05-15T09:00:51.841Z_

<details><summary>↩ Tool result · `toolu_01X6DGHDsBrk3kncuMf4Zwwf`</summary>

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
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "uuid": "c1fb2885-cb84-426e-a649-7896ea053e8d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "oldString": "A preliminary 50-problem MATH Level~4--5 pilot, using code interpreter as the deterministic modality, provides initial evidence beyond ScienceWorld. Internal reasoning achieved 80\\% accuracy (95\\% CI [66, 90]) versus 72\\% for code interpreter (95\\% CI [58, 84]); overlapping CIs confirm this is a preliminary signal, with 88\\% of problems showing no modality preference (1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver.",
    "newString": "A 300-problem MATH Level~4--5 evaluation (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, provides evidence beyond ScienceWorld. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]). Although the individual CIs overlap, the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, constituting a statistically significant signal reversal favoring internal reasoning. Label distribution reflects weak routing signal: 88.7\\% of problems show no modality preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage in ScienceWorld.",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\n\\title{Death Avoidance as the Dominant Routing Signal:\\\\A Counterfactual Analysis on ScienceWorld}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\\input{introduction}\n\\input{method}\n\\input{experiments}\n\\input{related_work}\n\\input{conclusion}\n\n\\section*{Limitations}\n\nOur analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. On the 135 episodes (55.1\\%) where neither strategy leads to catastrophic failure, deterministic computation retains a small advantage ($\\Delta_{\\text{nd}} = +2.84$), indicating non-zero routing signal beyond death avoidance. Our analysis covers 11 of 30 ScienceWorld task types; the remaining 19 (63\\%) were excluded during prescreening because both strategies timed out on all seed variations within the 30-step budget, providing no counterfactual signal. These tasks likely require longer-horizon planning; increasing the step budget could surface additional routing signal whose composition may differ from the death-dominated pattern observed here. Stronger models (e.g., 70B-scale or reasoning-specialized) likely exhibit lower internal-strategy death rates, which would reduce DAF. Our finding may reflect a capability-dependent failure mode: at higher capability levels, death avoidance may no longer dominate routing signal.\n\n\\paragraph{Cross-environment evidence.}\nA preliminary 50-problem MATH Level~4--5 pilot, using code interpreter as the deterministic modality, provides initial evidence beyond ScienceWorld. Internal reasoning achieved 80\\% accuracy (95\\% CI [66, 90]) versus 72\\% for code interpreter (95\\% CI [58, 84]); overlapping CIs confirm this is a preliminary signal, with 88\\% of problems showing no modality preference (1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver. An exploratory ALFWorld study \\cite{alfworld-2021} (135 games, 6 task types) shows a related but mechanistically distinct pattern: 25.9\\% of episodes are deterministic-preferred versus 1.5\\% internal-preferred, with deterministic success rate (27.4\\%) far exceeding internal (3.0\\%). However, the underlying mechanism differs from ScienceWorld. In ScienceWorld, the internal strategy has baseline competence (57.1\\% survival rate) but suffers hallucination-induced catastrophic failures; in ALFWorld, the 3\\% internal success rate reflects a fundamental capability gap---without admissible action filtering, the agent rarely completes tasks at all. The deterministic advantage in ALFWorld thus stems from action space pruning rather than death avoidance per se. These results are suggestive but do not directly confirm that the DAF pattern generalizes; environments with intermediate failure modes remain to be studied.\n\n\\paragraph{Step-level mislabeling.} Episode-level labels may assign suboptimal routing decisions to individual steps; in particular, steps preceding a death event are labeled det-preferred even if the death was not foreseeable from those steps' observations. Training on pure-strategy trajectories but deploying on mixed policy also introduces a distribution shift \\citep{dagger-2011}.\n\n\\paragraph{Scope.}\nExtending the counterfactual methodology to environments with graded failure costs, embodied agents, or multi-turn dialogue systems would clarify how broadly death avoidance accounts for apparent routing signal. Step-level labeling with denser rewards and the logit--generation gap in the implicit router are natural next steps. We audit labeling quality in Appendix~\\ref{app:labeling}.\n\n\\section*{Ethics Statement}\n\nThis work uses ScienceWorld \\cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All language models are accessed via standard APIs or publicly released weights. We report computational costs: approximately 40 GPU-hours on two RTX 5090 GPUs for data collection, router training, and evaluation.\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Labeling Quality Audit}\n\\label{app:labeling}\n\nA potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine modality differences. We audit all 245 labels. Of the 150 \\texttt{no\\_preference} labels (61.2\\%), 115 (46.9\\%) are both-alive ties and 35 (14.3\\%) are both-dead---all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields balanced accuracy of 57.3\\%, within 1$\\sigma$ of the full-label retrain (57.6 $\\pm$ 0.5\\%), confirming that score-comparison labels contribute negligible additional signal. The 97.4\\% step-level tie rate (\\S\\ref{sec:collection}) further motivates episode-level over step-level labeling.\n\n\\section{Per-Task Decomposition}\n\\label{app:per-task}\nWe select 11 of ScienceWorld's 30 task types via prescreening: task types where both strategies complete at least one episode within the 30-step budget are retained; types where both strategies time out on all seed variations are excluded.\\footnote{Prescreening ensures that the counterfactual comparison is meaningful---task types where neither strategy makes progress provide no routing signal.}\n\n\\begin{table}[h]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{2.5pt}\n\\begin{tabular}{@{}lrrccc@{}}\n\\toprule\nTask & $n$ & $\\Delta_\\text{full}$ & D\\%\\textsubscript{int} & D\\%\\textsubscript{det} & D / I / N \\\\\n\\midrule\nid-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\\\\nlifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\\\\nlifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\\\\ninclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\\\\nfreeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\\\\nmeas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\\\\nid-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\\\\nfind-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\\\\ngrow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\\\\nchem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\\\\n\\midrule\nfind-non-living$^\\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\\\\n\\midrule\n\\textbf{All (11 tasks)} & \\textbf{245} & $\\mathbf{+29.60}$ & \\textbf{42.9} & \\textbf{16.3} & \\textbf{86 / 9 / 150} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-task decomposition of the death avoidance effect. D\\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\\Delta_{\\text{full}}$ descending. $\\dagger$\\,Only task with zero deaths under both strategies.}\n\\label{tab:per-task}\n\\end{table}\n\n\\section{Correlation Robustness}\n\\label{app:correlation}\n\nThe Pearson $r = 0.9698$ reported in \\S\\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\\rho = 0.986$ ($p = 2.4 \\times 10^{-8}$), confirming that the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\\% CI $[0.952, 0.995]$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nTask removed & $r_{\\text{LOO}}$ \\\\\n\\midrule\nid-life-stages-1       & 0.963 \\\\\nlifespan-long          & 0.969 \\\\\nlifespan-l-then-s      & 0.976 \\\\\ninclined-plane         & 0.969 \\\\\nfreeze                 & 0.971 \\\\\nmeas-melt-point        & 0.972 \\\\\nid-life-stages-2       & 0.972 \\\\\nfind-animal            & 0.970 \\\\\ngrow-fruit             & 0.973 \\\\\nchem-mix               & 0.969 \\\\\nfind-non-living        & 0.980 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\\ $\\Delta_{\\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}\n\\label{tab:loo}\n\\end{table}\n\n\\section{Router Training Details}\n\\label{app:router-details}\n\nWe use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.\n\nGradient accumulation is critical for the implicit router: with gradient accumulation of 1, the model fails to achieve meaningful routing discrimination (internal recall 26.7\\%); with gradient accumulation of 8, the model becomes non-degenerate (internal recall above 50\\% across all seeds). All main-text results use gradient accumulation 8.\n\nCross-seed balanced accuracy is stable (57--59\\%), but internal recall varies from 51.5\\% to 81.8\\%, reflecting the structurally thin learnable signal: when ${\\sim}90\\%$ of routing value is death avoidance, the non-death signal is inherently noisy. Deployed end-to-end, the trained router allocates 97.0\\% of episodes to deterministic computation with 17.6\\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nHyperparameter & Classification Head & Implicit Router \\\\\n\\midrule\nBase model & Qwen3-1.7B & Qwen3-1.7B \\\\\nArchitecture & Linear + LoRA & SFT + LoRA \\\\\nLoRA $r$ / $\\alpha$ & 16 / 32 & 16 / 32 \\\\\nLearning rate & 2e-5 & 2e-4 \\\\\nOptimizer & AdamW & AdamW \\\\\nEpochs & 3 & 3 \\\\\nBatch size (per device) & 4 & 4 \\\\\nGradient accumulation & 8 & 8 \\\\\nWarmup ratio & 0.1 & 0.1 \\\\\nWeight decay & 0.01 & 0.01 \\\\\nMax sequence length & 512 & 512 \\\\\nSeeds & \\{42\\} & \\{42, 123, 456, 789\\} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\\pm$std.}\n\\label{tab:hyperparams}\n\\end{table}\n\n\\section{Penalty Sensitivity Analysis}\n\\label{app:penalty}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}rrrr@{}}\n\\toprule\n$P$ & $\\Delta_{\\text{full}}(P)$ & $\\Delta_{\\text{nd}}$ & DAF($P$) \\\\\n\\midrule\n10 & 5.72 & 3.07 & 46.4\\% \\\\\n25 & 9.70 & 3.07 & 68.4\\% \\\\\n50 & 16.33 & 3.07 & 81.2\\% \\\\\n100 & 29.60 & 3.07 & 89.6\\%\\textsuperscript{*} \\\\\n200 & 56.13 & 3.07 & 94.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Sensitivity of $\\Delta_{\\text{full}}$ and DAF to death penalty magnitude $P$. $\\Delta_{\\text{full}}(P) = \\delta \\cdot P + \\Delta_{\\text{nd}}$, where $\\delta = 0.2653$ is the death-rate differential. $\\Delta_{\\text{nd}} = 3.07$ here includes both-died episodes in the non-death pool, yielding DAF=89.6\\% at $P{=}100$ versus 90.41\\% in the main text (\\S\\ref{sec:death-decomp}), which uses strict neither-died filtering ($\\Delta_{\\text{nd}} = 2.84$). \\textsuperscript{*}Default setting.}\n\\label{tab:penalty-sensitivity}\n\\end{table}\n\n\\end{document}\n",
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
          "-A preliminary 50-problem MATH Level~4--5 pilot, using code interpreter as the deterministic modality, provides initial evidence beyond ScienceWorld. Internal reasoning achieved 80\\% accuracy (95\\% CI [66, 90]) versus 72\\% for code interpreter (95\\% CI [58, 84]); overlapping CIs confirm this is a preliminary signal, with 88\\% of problems showing no modality preference (1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver. An exploratory ALFWorld study \\cite{alfworld-2021} (135 games, 6 task types) shows a related but mechanistically distinct pattern: 25.9\\% of episodes are deterministic-preferred versus 1.5\\% internal-preferred, with deterministic success rate (27.4\\%) far exceeding internal (3.0\\%). However, the underlying mechanism differs from ScienceWorld. In ScienceWorld, the internal strategy has baseline competence (57.1\\% survival rate) but suffers hallucination-induced catastrophic failures; in ALFWorld, the 3\\% internal success rate reflects a fundamental capability gap---without admissible action filtering, the agent rarely completes tasks at all. The deterministic advantage in ALFWorld thus stems from action space pruning rather than death avoidance per se. These results are suggestive but do not directly confirm that the DAF pattern generalizes; environments with intermediate failure modes remain to be studied.",
          "+A 300-problem MATH Level~4--5 evaluation (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, provides evidence beyond ScienceWorld. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]). Although the individual CIs overlap, the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, constituting a statistically significant signal reversal favoring internal reasoning. Label distribution reflects weak routing signal: 88.7\\% of problems show no modality preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage in ScienceWorld. An exploratory ALFWorld study \\cite{alfworld-2021} (135 games, 6 task types) shows a related but mechanistically distinct pattern: 25.9\\% of episodes are deterministic-preferred versus 1.5\\% internal-preferred, with deterministic success rate (27.4\\%) far exceeding internal (3.0\\%). However, the underlying mechanism differs from ScienceWorld. In ScienceWorld, the internal strategy has baseline competence (57.1\\% survival rate) but suffers hallucination-induced catastrophic failures; in ALFWorld, the 3\\% internal success rate reflects a fundamental capability gap---without admissible action filtering, the agent rarely completes tasks at all. The deterministic advantage in ALFWorld thus stems from action space pruning rather than death avoidance per se. These results are suggestive but do not directly confirm that the DAF pattern generalizes; environments with intermediate failure modes remain to be studied.",
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

<details open><summary>🔧 Tool call — Edit · `toolu_01PkpkLjeRvAY3QcA9bLpYBB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex",
  "old_string": "The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A preliminary 50-problem pilot on MATH Level~4--5, using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 80\\% accuracy versus 72\\% for code interpreter, with 88\\% of problems showing no modality preference (label distribution: 1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld. The pilot study used a code sandbox with a known bug (bare expressions returned empty output), which may slightly underestimate code-interpreter accuracy; a post-fix replication on a different 55-question subset shows the same qualitative trend. A larger-scale replication with improved code execution is in progress.",
  "new_string": "The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A 300-problem evaluation on MATH Level~4--5 (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, suggests not---and in fact reverses. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]); the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, a statistically significant reversal favoring internal reasoning. The contingency table (215 both-correct, 40 both-wrong, 30 only-internal-correct, 15 only-code-correct) shows that the majority of problems are modality-insensitive, with 88.7\\% labeled no-preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "uuid": "324f2d4c-fa1e-4ba4-89dd-d5e34763ab95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gpiQ4cHANDzjRTGUg9gFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4799,
      "cache_read_input_tokens": 23463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4799
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

_source line 14 · 2026-05-15T09:00:57.933Z_

<details><summary>↩ Tool result · `toolu_01PkpkLjeRvAY3QcA9bLpYBB`</summary>

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
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "uuid": "549b8cdd-2ee0-47d2-9f58-d59f17c8d191",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex",
    "oldString": "The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A preliminary 50-problem pilot on MATH Level~4--5, using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 80\\% accuracy versus 72\\% for code interpreter, with 88\\% of problems showing no modality preference (label distribution: 1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld. The pilot study used a code sandbox with a known bug (bare expressions returned empty output), which may slightly underestimate code-interpreter accuracy; a post-fix replication on a different 55-question subset shows the same qualitative trend. A larger-scale replication with improved code execution is in progress.",
    "newString": "The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A 300-problem evaluation on MATH Level~4--5 (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, suggests not---and in fact reverses. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]); the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, a statistically significant reversal favoring internal reasoning. The contingency table (215 both-correct, 40 both-wrong, 30 only-internal-correct, 15 only-code-correct) shows that the majority of problems are modality-insensitive, with 88.7\\% labeled no-preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Cross-environment evidence.}\nThe death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A preliminary 50-problem pilot on MATH Level~4--5, using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 80\\% accuracy versus 72\\% for code interpreter, with 88\\% of problems showing no modality preference (label distribution: 1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld. The pilot study used a code sandbox with a known bug (bare expressions returned empty output), which may slightly underestimate code-interpreter accuracy; a post-fix replication on a different 55-question subset shows the same qualitative trend. A larger-scale replication with improved code execution is in progress.\n\n\\paragraph{Scope and future directions.}\nOur analysis is grounded in a single interactive environment with a specific failure mode (the $-100$ death penalty). Extending the counterfactual methodology to environments with graded failure costs, embodied agents with continuous action spaces, or multi-turn dialogue systems would clarify how broadly death avoidance---or analogous catastrophic-failure avoidance---accounts for apparent routing signal. Step-level counterfactual labeling, rather than episode-level, is a complementary direction that could reveal finer-grained routing structure masked by our current aggregation.\n",
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
          "-The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A preliminary 50-problem pilot on MATH Level~4--5, using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 80\\% accuracy versus 72\\% for code interpreter, with 88\\% of problems showing no modality preference (label distribution: 1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld. The pilot study used a code sandbox with a known bug (bare expressions returned empty output), which may slightly underestimate code-interpreter accuracy; a post-fix replication on a different 55-question subset shows the same qualitative trend. A larger-scale replication with improved code execution is in progress.",
          "+The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A 300-problem evaluation on MATH Level~4--5 (152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, suggests not---and in fact reverses. Internal reasoning achieved 81.7\\% accuracy (95\\% CI [77.3, 86.0]) versus 76.7\\% for code interpreter (95\\% CI [72.0, 81.3]); the paired difference of $+5.0$~percentage points (95\\% CI [$+0.7$, $+9.3$]) excludes zero, a statistically significant reversal favoring internal reasoning. The contingency table (215 both-correct, 40 both-wrong, 30 only-internal-correct, 15 only-code-correct) shows that the majority of problems are modality-insensitive, with 88.7\\% labeled no-preference (9 deterministic-preferred, 25 internal-preferred, 266 no-preference). In the absence of death risk, the routing signal reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld.",
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

两处已更新：

- **main.tex** Limitations 段落：50题pilot → 300题evaluation，accuracy/CI/label分布全部更新，措辞从 "preliminary signal" 改为 "statistically significant signal reversal"，保留了个体CI重叠的说明。
- **discussion.tex** Cross-environment evidence 段落：同步更新为300题数据，加入contingency table (215/40/30/15)，删除 known bug caveat 和 "in progress" 说法，措辞升级为显著反转。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "uuid": "ff2fc44c-25a0-42ef-a82f-eb489875807c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrWwp7MQGUWXNS5rzXkg5G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1768,
      "cache_read_input_tokens": 28262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1768
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

两处已更新：

- **main.tex** Limitations 段落：50题pilot → 300题evaluation，accuracy/CI/label分布全部更新，措辞从 "preliminary signal" 改为 "statistically significant signal reversal"，保留了个体CI重叠的说明。
- **discussion.tex** Cross-environment evidence 段落：同步更新为300题数据，加入contingency table (215/40/30/15)，删除 known bug caveat 和 "in progress" 说法，措辞升级为显著反转。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 32157,
  "duration_api_ms": 33414,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "5f7820c7-8a37-4a76-9be8-4ab5d0243a76",
  "total_cost_usd": 0.19469525000000001,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 18189,
    "cache_read_input_tokens": 63566,
    "output_tokens": 1905,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 18189,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 147,
        "cache_read_input_tokens": 28262,
        "cache_creation_input_tokens": 1768,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1768
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1486,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001581,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 1905,
      "cacheReadInputTokens": 63566,
      "cacheCreationInputTokens": 18189,
      "webSearchRequests": 0,
      "costUSD": 0.19311425000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "660bd23c-5323-480d-90ec-1bd9bb31b77b"
}
```

</details>

---
