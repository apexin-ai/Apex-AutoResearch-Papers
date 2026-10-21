# paper update experiments steering

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_paper_update-experiments-steering_20260522T155330.log`
- **Structured JSON:** [`2a2aa6547a2f6fc52b0e.json`](../../sessions/2a/2a2aa6547a2f6fc52b0e.json)

## Before a recorded user message

25 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
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
  "uuid": "96375faf-77bf-448d-ac39-ffb1aff11ac5",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod42-projects-clkc-mech-interp/memory/"
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
    "resetsAt": 1779475200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1e6cbaee-6938-487a-97fd-63fff41086de",
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb"
}
```

---

### Assistant

_source line 4_

Let me read the current experiments.tex file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "62e5ad86-d5cd-43fe-89e2-af8a1f703298",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PSBzvYt8mpCigmuJmYn1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
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

<details open><summary>🔧 Tool call — Read · `toolu_01Lyo4Qzznms8EUKML1dnT5m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "9c4b1721-4450-4a08-8adc-49ed70b6dc50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PSBzvYt8mpCigmuJmYn1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
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

_source line 6 · 2026-05-22T15:53:43.007Z_

<details><summary>↩ Tool result · `toolu_01Lyo4Qzznms8EUKML1dnT5m`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe two instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama} and Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2024qwen25}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test) and 966 samples for Qwen (773 train / 193 test), split 80/20 with stratification.
13	
14	\paragraph{Translation.}
15	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET \citep{rei2020comet} back-translation scores.
16	
17	\paragraph{Probing.}
18	For each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
19	We report balanced accuracy to account for class imbalance.
20	All confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.
21	
22	\paragraph{Non-conflict baseline.}
23	To test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \citep{conneau2018xnli}, classifying entailment versus contradiction.
24	
25	\subsection{Within-Language Conflict Detection}
26	\label{sec:within_lang}
27	
28	Table~\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.
29	Both models encode linearly detectable conflict signals in their residual streams.
30	Llama achieves 77.1\% on EN$\to$EN (peak at layer 28, 88\% depth) and 71.2\% on ZH$\to$ZH.
31	Qwen reaches 75.3\% on EN$\to$EN (peak at layer 22, 61\% depth) and 71.6\% on ZH$\to$ZH.
32	All within-language accuracies are significantly above chance (binomial $p < 0.001$).
33	Figure~\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for both models.
34	These results confirm that knowledge conflict signals are linearly separable in the residual stream across both architectures and both languages.
35	
36	\subsection{Cross-Lingual Transfer and Asymmetry}
37	\label{sec:cross_lingual}
38	
39	All four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\ref{tab:main_results}), confirming that conflict representations partially overlap across languages.
40	Both models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\to$EN) more accurately than the reverse direction (EN$\to$ZH).
41	For Llama, $\Delta_{\text{asym}} = +7.2$ percentage points (pp) with a 95\% bootstrap CI of [1.1, 13.6]; for Qwen, $\Delta_{\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7].
42	The magnitude of this asymmetry closely matches the XNLI non-conflict baseline (\S\ref{sec:xnli_baseline}), and the consistent direction across architectures suggests a shared structural property rather than a model-specific artifact (Figure~\ref{fig:asymmetry_forest}).
43	
44	%% Table 1: Main cross-lingual probe results
45	\begin{table}[t]
46	\centering
47	\caption{Cross-lingual probe balanced accuracy (\%) with bootstrap 95\% CIs ($n \geq 100$). $\Delta_{\text{asym}}$ = acc(ZH$\to$EN) $-$ acc(EN$\to$ZH), computed as the mean of paired bootstrap differences. Bold: best per-task direction.}
48	\label{tab:main_results}
49	\begin{tabular}{lcc}
50	\toprule
51	Direction & Llama-3.1-8B & Qwen3-8B \\
52	\midrule
53	\multicolumn{3}{l}{\textit{Conflict Task}} \\
54	EN $\to$ EN & \textbf{77.1} & \textbf{75.3} \\
55	ZH $\to$ ZH & 71.2 & 71.6 \\
56	EN $\to$ ZH & 64.1 & 65.0 \\
57	ZH $\to$ EN & 71.3 & 72.2 \\
58	$\Delta_{\text{asym}}$ & +7.2 [1.1, 13.6] & +7.2 [$-$0.6, 13.7] \\
59	\midrule
60	\multicolumn{3}{l}{\textit{XNLI Baseline}} \\
61	EN $\to$ EN & 94.0 & 96.6 \\
62	ZH $\to$ ZH & 87.5 & 89.5 \\
63	EN $\to$ ZH & 89.0 & 90.5 \\
64	ZH $\to$ EN & \textbf{94.9} & \textbf{97.2} \\
65	$\Delta_{\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] \\
66	\bottomrule
67	\end{tabular}
68	\end{table}
69	
70	\subsection{Non-Conflict Baseline Comparison}
71	\label{sec:xnli_baseline}
72	
73	If the ZH$\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.
74	We test this prediction using XNLI entailment-versus-contradiction probes.
75	Both models achieve high within-language accuracy on XNLI (Llama 94.0\% EN, 87.5\% ZH; Qwen 96.6\% EN, 89.5\% ZH), confirming that the probing pipeline captures semantic distinctions beyond knowledge conflicts.
76	The XNLI probes exhibit the same directional asymmetry: Llama $\Delta_{\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\Delta_{\text{asym}} = +6.7$ pp, CI [2.4, 11.7].
77	Both XNLI CIs exclude zero, and both overlap substantially with the corresponding conflict-task CIs (Figure~\ref{fig:asymmetry_forest}).
78	The close match in asymmetry magnitude between conflict probes (Llama +7.2, Qwen +7.2 pp) and XNLI probes (Llama +6.0, Qwen +6.7 pp) indicates that the ZH$\to$EN transfer advantage is not specific to knowledge conflict representations.
79	Instead, it reflects a general cross-lingual property: Chinese-trained probes transfer to English more readily than the reverse, regardless of the downstream task.
80	
81	\subsection{Confound Exclusion}
82	\label{sec:confounds}
83	
84	Two potential confounds could inflate cross-lingual probe accuracy: translation quality and lexical overlap between English and Chinese inputs.
85	
86	\paragraph{Translation quality.}
87	We stratify test samples by COMET score into terciles (high, medium, low) and compare EN$\to$ZH probe accuracy across strata.
88	If translation quality drove probe transfer, high-COMET samples would yield higher accuracy.
89	Table~\ref{tab:confound} shows no such pattern: Qwen exhibits a reversed direction ($\Delta = -5.6$ pp, Fisher $p = 0.695$), and Llama shows a negligible effect ($\Delta = +1.7$ pp, Fisher $p = 0.761$).
90	Translation quality does not confound the cross-lingual transfer results.
91	
92	\paragraph{Token overlap.}
93	Per-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\%, consistent with the minimal lexical overlap between the two languages.
94	Neither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$), where higher overlap is associated with \emph{lower} accuracy.
95	Shared tokens do not drive cross-lingual transfer.
96	
97	%% Table 2: Confound exclusion
98	\begin{table}[t]
99	\centering
100	\caption{Confound exclusion analysis. COMET tercile: $\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\to$ZH probe accuracy.}
101	\label{tab:confound}
102	\begin{tabular}{llrl}
103	\toprule
104	Confound & Model & Result & $p$ \\
105	\midrule
106	COMET tercile & Qwen & $\Delta = -5.6$ pp & 0.695 \\
107	COMET tercile & Llama & $\Delta = +1.7$ pp & 0.761 \\
108	\midrule
109	Token overlap & Qwen & n.s. & $>$0.4 \\
110	Token overlap & Llama & $r = -0.15$ & 0.012 \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	\subsection{Causal Evidence via Representation Steering}
116	\label{sec:steering}
117	
118	The probing results establish that conflict signals are detectable, but detection does not imply causal relevance.
119	We test whether the probe weight direction $\mathbf{w}_{\text{probe}}$ causally influences conflict resolution by injecting $\alpha \cdot \mathbf{w}_{\text{probe}}$ into the last-token residual stream at a target layer during inference.
120	We measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.
121	
122	\paragraph{L13 (mid-layer, 41\% depth).}
123	Steering at layer 13 produces significantly more behavioral change than random controls in both directions (Table~\ref{tab:steering}).
124	Positive steering ($\alpha = +5$) yields a flip rate of 19.9\% versus 6.6\% for the random control (Fisher $p = 0.002$), with all 4 directional flips moving from parametric to contextual answers.
125	Negative steering ($\alpha = -20$) yields 36.0\% versus 17.6\% (Fisher $p < 0.001$), with 5 of 6 directional flips moving from contextual to parametric.
126	Both results survive Bonferroni correction for multiple comparisons.
127	The bidirectionality confirms that the probe weight vector encodes a meaningful axis of conflict resolution: positive perturbations push toward contextual answers, and negative perturbations push toward parametric answers.
128	
129	\paragraph{Negative layers.}
130	Steering at L28 (the probing peak layer, 88\% depth) produces no significant effect with either last-token or all-position injection (all Fisher $p > 0.3$; Table~\ref{tab:steering}).
131	L18 (the MLP probe peak, 56\% depth) also shows no causal influence (all Fisher $p > 0.44$).
132	
133	\paragraph{$\alpha = +20$ reversal.}
134	At extreme perturbation magnitude ($\alpha = +20$), the control condition produces more flips than the steering condition ($p = 0.053$).
135	This indicates coherence collapse at large perturbation magnitudes, constraining the effective steering range.
136	
137	\paragraph{Detection $\neq$ Decision.}
138	The detectable conflict signal peaks at late layers (L28, 88\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\% depth).
139	Probing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.
140	\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation.
141	
142	%% Table 3: Steering results
143	\begin{table}[t]
144	\centering
145	\caption{Representation steering results (Llama-3.1-8B). Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\dagger}$}
146	\label{tab:steering}
147	\small
148	\begin{tabular}{lcrrrrl}
149	\toprule
150	Layer & Depth & $\alpha$ & Steer (\%) & Ctrl (\%) & Fisher $p$ & Dir. \\
151	\midrule
152	\textbf{L13} & \textbf{41\%} & $\mathbf{+5}$ & \textbf{19.9} & \textbf{6.6} & $\mathbf{0.002}$ & \textbf{4 p$\to$c} \\
153	\textbf{L13} & \textbf{41\%} & $\mathbf{-20}$ & \textbf{36.0} & \textbf{17.6} & $\mathbf{<0.001}$ & \textbf{5 c$\to$p} \\
154	L18 & 56\% & $+2$ & 3.7 & 1.5 & 0.447 & \\
155	L28 & 88\% & $-20$ & 14.7 & 16.9 & 0.740 & \\
156	L28 (all) & 88\% & $-20$ & 11.8 & 11.8 & 0.370 & \\
157	\midrule
158	\multicolumn{7}{l}{\textit{Qwen3-8B L13: \textbf{[PLACEHOLDER]}}} \\
159	\bottomrule
160	\end{tabular}
161	\begin{flushleft}
162	\footnotesize $^{\dagger}$ At $\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.
163	\end{flushleft}
164	\end{table}
165	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "7ce4b3e8-2488-4edc-b2d0-bd12d377427a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe probe two instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \\citep{grattafiori2024llama} and Qwen3-8B (36 layers, hidden dimension 4096) \\citep{yang2024qwen25}.\n\n\\paragraph{Dataset.}\nWe use ConflictQA \\citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.\nAfter verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test) and 966 samples for Qwen (773 train / 193 test), split 80/20 with stratification.\n\n\\paragraph{Translation.}\nWe translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\\to$ZH), with quality validated by COMET \\citep{rei2020comet} back-translation scores.\n\n\\paragraph{Probing.}\nFor each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.\nWe report balanced accuracy to account for class imbalance.\nAll confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\n\n\\subsection{Within-Language Conflict Detection}\n\\label{sec:within_lang}\n\nTable~\\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.\nBoth models encode linearly detectable conflict signals in their residual streams.\nLlama achieves 77.1\\% on EN$\\to$EN (peak at layer 28, 88\\% depth) and 71.2\\% on ZH$\\to$ZH.\nQwen reaches 75.3\\% on EN$\\to$EN (peak at layer 22, 61\\% depth) and 71.6\\% on ZH$\\to$ZH.\nAll within-language accuracies are significantly above chance (binomial $p < 0.001$).\nFigure~\\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for both models.\nThese results confirm that knowledge conflict signals are linearly separable in the residual stream across both architectures and both languages.\n\n\\subsection{Cross-Lingual Transfer and Asymmetry}\n\\label{sec:cross_lingual}\n\nAll four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\\ref{tab:main_results}), confirming that conflict representations partially overlap across languages.\nBoth models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\\to$EN) more accurately than the reverse direction (EN$\\to$ZH).\nFor Llama, $\\Delta_{\\text{asym}} = +7.2$ percentage points (pp) with a 95\\% bootstrap CI of [1.1, 13.6]; for Qwen, $\\Delta_{\\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7].\nThe magnitude of this asymmetry closely matches the XNLI non-conflict baseline (\\S\\ref{sec:xnli_baseline}), and the consistent direction across architectures suggests a shared structural property rather than a model-specific artifact (Figure~\\ref{fig:asymmetry_forest}).\n\n%% Table 1: Main cross-lingual probe results\n\\begin{table}[t]\n\\centering\n\\caption{Cross-lingual probe balanced accuracy (\\%) with bootstrap 95\\% CIs ($n \\geq 100$). $\\Delta_{\\text{asym}}$ = acc(ZH$\\to$EN) $-$ acc(EN$\\to$ZH), computed as the mean of paired bootstrap differences. Bold: best per-task direction.}\n\\label{tab:main_results}\n\\begin{tabular}{lcc}\n\\toprule\nDirection & Llama-3.1-8B & Qwen3-8B \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Conflict Task}} \\\\\nEN $\\to$ EN & \\textbf{77.1} & \\textbf{75.3} \\\\\nZH $\\to$ ZH & 71.2 & 71.6 \\\\\nEN $\\to$ ZH & 64.1 & 65.0 \\\\\nZH $\\to$ EN & 71.3 & 72.2 \\\\\n$\\Delta_{\\text{asym}}$ & +7.2 [1.1, 13.6] & +7.2 [$-$0.6, 13.7] \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{XNLI Baseline}} \\\\\nEN $\\to$ EN & 94.0 & 96.6 \\\\\nZH $\\to$ ZH & 87.5 & 89.5 \\\\\nEN $\\to$ ZH & 89.0 & 90.5 \\\\\nZH $\\to$ EN & \\textbf{94.9} & \\textbf{97.2} \\\\\n$\\Delta_{\\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Non-Conflict Baseline Comparison}\n\\label{sec:xnli_baseline}\n\nIf the ZH$\\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.\nWe test this prediction using XNLI entailment-versus-contradiction probes.\nBoth models achieve high within-language accuracy on XNLI (Llama 94.0\\% EN, 87.5\\% ZH; Qwen 96.6\\% EN, 89.5\\% ZH), confirming that the probing pipeline captures semantic distinctions beyond knowledge conflicts.\nThe XNLI probes exhibit the same directional asymmetry: Llama $\\Delta_{\\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\\Delta_{\\text{asym}} = +6.7$ pp, CI [2.4, 11.7].\nBoth XNLI CIs exclude zero, and both overlap substantially with the corresponding conflict-task CIs (Figure~\\ref{fig:asymmetry_forest}).\nThe close match in asymmetry magnitude between conflict probes (Llama +7.2, Qwen +7.2 pp) and XNLI probes (Llama +6.0, Qwen +6.7 pp) indicates that the ZH$\\to$EN transfer advantage is not specific to knowledge conflict representations.\nInstead, it reflects a general cross-lingual property: Chinese-trained probes transfer to English more readily than the reverse, regardless of the downstream task.\n\n\\subsection{Confound Exclusion}\n\\label{sec:confounds}\n\nTwo potential confounds could inflate cross-lingual probe accuracy: translation quality and lexical overlap between English and Chinese inputs.\n\n\\paragraph{Translation quality.}\nWe stratify test samples by COMET score into terciles (high, medium, low) and compare EN$\\to$ZH probe accuracy across strata.\nIf translation quality drove probe transfer, high-COMET samples would yield higher accuracy.\nTable~\\ref{tab:confound} shows no such pattern: Qwen exhibits a reversed direction ($\\Delta = -5.6$ pp, Fisher $p = 0.695$), and Llama shows a negligible effect ($\\Delta = +1.7$ pp, Fisher $p = 0.761$).\nTranslation quality does not confound the cross-lingual transfer results.\n\n\\paragraph{Token overlap.}\nPer-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\\%, consistent with the minimal lexical overlap between the two languages.\nNeither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$), where higher overlap is associated with \\emph{lower} accuracy.\nShared tokens do not drive cross-lingual transfer.\n\n%% Table 2: Confound exclusion\n\\begin{table}[t]\n\\centering\n\\caption{Confound exclusion analysis. COMET tercile: $\\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\\to$ZH probe accuracy.}\n\\label{tab:confound}\n\\begin{tabular}{llrl}\n\\toprule\nConfound & Model & Result & $p$ \\\\\n\\midrule\nCOMET tercile & Qwen & $\\Delta = -5.6$ pp & 0.695 \\\\\nCOMET tercile & Llama & $\\Delta = +1.7$ pp & 0.761 \\\\\n\\midrule\nToken overlap & Qwen & n.s. & $>$0.4 \\\\\nToken overlap & Llama & $r = -0.15$ & 0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Causal Evidence via Representation Steering}\n\\label{sec:steering}\n\nThe probing results establish that conflict signals are detectable, but detection does not imply causal relevance.\nWe test whether the probe weight direction $\\mathbf{w}_{\\text{probe}}$ causally influences conflict resolution by injecting $\\alpha \\cdot \\mathbf{w}_{\\text{probe}}$ into the last-token residual stream at a target layer during inference.\nWe measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.\n\n\\paragraph{L13 (mid-layer, 41\\% depth).}\nSteering at layer 13 produces significantly more behavioral change than random controls in both directions (Table~\\ref{tab:steering}).\nPositive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$), with all 4 directional flips moving from parametric to contextual answers.\nNegative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% (Fisher $p < 0.001$), with 5 of 6 directional flips moving from contextual to parametric.\nBoth results survive Bonferroni correction for multiple comparisons.\nThe bidirectionality confirms that the probe weight vector encodes a meaningful axis of conflict resolution: positive perturbations push toward contextual answers, and negative perturbations push toward parametric answers.\n\n\\paragraph{Negative layers.}\nSteering at L28 (the probing peak layer, 88\\% depth) produces no significant effect with either last-token or all-position injection (all Fisher $p > 0.3$; Table~\\ref{tab:steering}).\nL18 (the MLP probe peak, 56\\% depth) also shows no causal influence (all Fisher $p > 0.44$).\n\n\\paragraph{$\\alpha = +20$ reversal.}\nAt extreme perturbation magnitude ($\\alpha = +20$), the control condition produces more flips than the steering condition ($p = 0.053$).\nThis indicates coherence collapse at large perturbation magnitudes, constraining the effective steering range.\n\n\\paragraph{Detection $\\neq$ Decision.}\nThe detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\nProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\n\\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation.\n\n%% Table 3: Steering results\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results (Llama-3.1-8B). Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 0.370 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B L13: \\textbf{[PLACEHOLDER]}}} \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.\n\\end{flushleft}\n\\end{table}\n",
      "numLines": 165,
      "startLine": 1,
      "totalLines": 165
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
Now I have the full file. Let me identify the changes needed:

1. Replace the `\textbf{[PLACEHOLDER]}` paragraph about Qwen L13 at line 140 with actual Qwen results (L14 and L23, both negative)
2. Update the framing to emphasize "Detection ≠ Decision" as the core finding, with cross-model results showing limited transferability
3. Update Table 3 to include Qwen L14 and L23 results, remove the placeholder line
4. Adjust the table caption to include both models

Let me also add L13/all to the table since the user wants all 7 configurations.


Looking at the existing table structure, I need to understand what's currently there—it has individual alpha results for different layer/position combinations across the models. But the user wants a cleaner format with columns for Model, Layer, Depth, Position, and Best p-value. I'll need to reorganize these 7 configurations into that structure, replacing the Qwen placeholder with the actual L14 and L23 results. I'm noticing the user's requirements don't quite match what's in the current table — they want L13/all included, and the p-values they specified differ from what's shown. Let me reconsider which results to include and how to structure this properly. I'm seeing that Qwen L23 has a p-value of 1.0 with 73.2% probe accuracy. Now I need to decide how to restructure the table—I could keep the detailed Llama rows as-is and add summary rows for Qwen, or fully restructure to match the user's requested format. I think a hybrid approach works best: maintain the existing Llama detail while adding the L13/all row and the new Qwen entries, then update the caption and remove the placeholder text to create a unified table covering both models.

For the paragraph, I'll reframe the "Detection ≠ Decision" section to explain that the detection peak doesn't correspond to the causal node in Llama, and that cross-model transferability is limited based on these Qwen results. The table itself needs a Model column or grouping, and I'll need to figure out what information to include for Qwen since I have the best Fisher p-values but not the individual steering and control flip rates at the same level of detail as the Llama rows.

Looking at what I have for Qwen: L14 shows a probe accuracy of 70.2% with a best p-value of 0.6818 at α=-10 and zero directional flips, while L23 has all p-values at 1.0 and a probe accuracy of 73.2%. I don't have the exact steering and control percentages broken down the same way, so I'll report what's available and add Qwen rows with the best alpha, best p-value, and note the absence of directional flips.

The cleanest approach is to keep the existing detailed Llama table as-is, add the L13/all row, then add Qwen rows with available data and use a separator to distinguish between models.

Generating markdown table... I'm looking at the table structure and realizing the user wants a summary format with specific columns, but I also need to ensure all six steering configurations are represented in the results. Rather than restructuring the entire table, I'll keep the detailed format mostly intact, add the Qwen model rows, and update the accompanying text to clarify what's being shown.

For the Detection ≠ Decision section, I'm revising it to specify that these findings are from Llama, then noting that Qwen's steering results will confirm whether this dissociation between detection and causal influence holds across models.

For the cross-model steering analysis, the key finding is that despite Qwen having comparable probe accuracies to Llama's mid-layer, steering at those layers produces no behavioral change—suggesting that detectability doesn't guarantee causal relevance, and the computational mechanisms may differ between architectures.

Restructuring the results table... Generating markdown table... Generating markdown table... I'm doing string matching to identify the exact lines I need to replace in the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "ed9172f4-230a-4514-aa33-c30da6d3d5c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rnu1W2h7qwAG7YCGUB56bD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4141,
      "cache_read_input_tokens": 24170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4141
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

Now I'll make the edits. Two changes: (1) replace the Detection ≠ Decision paragraph + placeholder with actual results, (2) update the table to include all configurations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "609b3104-2e3f-43ec-9b21-98f4b1aeb620",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rnu1W2h7qwAG7YCGUB56bD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4141,
      "cache_read_input_tokens": 24170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4141
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

<details open><summary>🔧 Tool call — Edit · `toolu_01TLcyN7XZrhtGhgnaoumBih`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex",
  "old_string": "\t\\paragraph{Detection $\\neq$ Decision.}\n\tThe detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\n\tProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\n\t\\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation.",
  "new_string": "\t\\paragraph{Detection $\\neq$ Decision.}\n\tIn Llama, the detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\n\tProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\n\tInjecting at all token positions (L13, all) yields identical results to last-token injection, indicating that the causal signal is concentrated in the final token's residual stream.\n\n\t\\paragraph{Cross-model steering.}\n\tSteering at Qwen's mid-layer (L14, 39\\% depth; probe accuracy 70.2\\%) produces no significant behavioral change (best Fisher $p = 0.682$, $\\alpha = -10$), with zero directional flips across all steering magnitudes ($n_{\\text{test}} = 84$).\n\tL23 (64\\% depth; probe accuracy 73.2\\%) is similarly negative (all $p = 1.0$).\n\tDespite comparable probe accuracies (70--73\\%), the Qwen probe directions fail to causally shift answer routing, indicating that linear detectability does not entail causal relevance.\n\tThe mid-layer causal node identified in Llama L13 does not transfer across architectures, suggesting that the locus of conflict resolution may be model-specific even when the representational signature is shared."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "3a5b5729-c0b0-4905-8a63-6e70c6c10130",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rnu1W2h7qwAG7YCGUB56bD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4141,
      "cache_read_input_tokens": 24170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4141
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

_source line 10 · 2026-05-22T15:55:01.214Z_

<details><summary>↩ Tool result · reported error · `toolu_01TLcyN7XZrhtGhgnaoumBih`</summary>

```text
&lt;tool_use_error>String to replace not found in file.
String: 	\paragraph{Detection $\neq$ Decision.}
	The detectable conflict signal peaks at late layers (L28, 88\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\% depth).
	Probing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.
	\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "45df6001-eeb6-405e-ba2d-eb1ec2037fcb",
  "tool_use_result": "Error: String to replace not found in file.\nString: \t\\paragraph{Detection $\\neq$ Decision.}\n\tThe detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\n\tProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\n\t\\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation."
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
The tabs might not match. Let me re-read the file to check the exact indentation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "70e71d3c-7b8c-4ea9-a861-cb23fcc73bd6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4CuYTN4y6NwH33Qj2KdtY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4670,
      "cache_read_input_tokens": 28311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4670
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

Let me check the exact whitespace in the file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "43272849-1f8f-45aa-9989-29152eb598ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4CuYTN4y6NwH33Qj2KdtY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4670,
      "cache_read_input_tokens": 28311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4670
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Tie2suDS6ZE2bNm3RGJyEU`</summary>

```json
{
  "command": "cat -A /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex | sed -n '137,140p'",
  "description": "Show exact whitespace characters in lines 137-140"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "56c6b8c7-a71e-4f8e-933a-3a0ae59e1955",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4CuYTN4y6NwH33Qj2KdtY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4670,
      "cache_read_input_tokens": 28311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4670
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

_source line 14 · 2026-05-22T15:55:05.087Z_

<details><summary>↩ Tool result · `toolu_01Tie2suDS6ZE2bNm3RGJyEU`</summary>

```text
\paragraph{Detection $\neq$ Decision.}$
The detectable conflict signal peaks at late layers (L28, 88\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\% depth).$
Probing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.$
\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation.$
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "89609db7-b99e-4ffd-93a4-5bd8f51af9d7",
  "tool_use_result": {
    "stdout": "\\paragraph{Detection $\\neq$ Decision.}$\nThe detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).$\nProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.$\n\\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation.$",
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

_source line 15_

No leading tabs — just plain lines. Let me redo the edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "0c975f9a-ea6d-412d-8a44-fef991710499",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tad1xZvPCEZ9j9k5gjthem",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 316,
      "cache_read_input_tokens": 32981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 316
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

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_012XfxgN6efCrNkisg9yuQon`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex",
  "old_string": "\\paragraph{Detection $\\neq$ Decision.}\nThe detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\nProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\n\\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation.",
  "new_string": "\\paragraph{Detection $\\neq$ Decision.}\nIn Llama, the detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\nProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\nInjecting at all token positions (L13, all) yields identical results to last-token injection, indicating that the causal signal is concentrated in the final token's residual stream.\n\n\\paragraph{Cross-model steering.}\nSteering at Qwen's mid-layer (L14, 39\\% depth; probe accuracy 70.2\\%) produces no significant behavioral change (best Fisher $p = 0.682$, $\\alpha = -10$), with zero directional flips across all steering magnitudes ($n_{\\text{test}} = 84$).\nL23 (64\\% depth; probe accuracy 73.2\\%) is similarly negative (all $p = 1.0$).\nDespite comparable probe accuracies (70--73\\%), the Qwen probe directions fail to causally shift answer routing, indicating that linear detectability does not entail causal relevance.\nThe mid-layer causal node identified in Llama L13 does not transfer across architectures, suggesting that the locus of conflict resolution may be model-specific even when the representational signature is shared."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "d3f456e0-86b8-4753-834c-f1c99ba38ce7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tad1xZvPCEZ9j9k5gjthem",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 316,
      "cache_read_input_tokens": 32981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 316
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

_source line 17 · 2026-05-22T15:55:12.460Z_

<details><summary>↩ Tool result · `toolu_012XfxgN6efCrNkisg9yuQon`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "1bef22da-8041-49ae-83bd-975fe57ce55e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex",
    "oldString": "\\paragraph{Detection $\\neq$ Decision.}\nThe detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\nProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\n\\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation.",
    "newString": "\\paragraph{Detection $\\neq$ Decision.}\nIn Llama, the detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\nProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\nInjecting at all token positions (L13, all) yields identical results to last-token injection, indicating that the causal signal is concentrated in the final token's residual stream.\n\n\\paragraph{Cross-model steering.}\nSteering at Qwen's mid-layer (L14, 39\\% depth; probe accuracy 70.2\\%) produces no significant behavioral change (best Fisher $p = 0.682$, $\\alpha = -10$), with zero directional flips across all steering magnitudes ($n_{\\text{test}} = 84$).\nL23 (64\\% depth; probe accuracy 73.2\\%) is similarly negative (all $p = 1.0$).\nDespite comparable probe accuracies (70--73\\%), the Qwen probe directions fail to causally shift answer routing, indicating that linear detectability does not entail causal relevance.\nThe mid-layer causal node identified in Llama L13 does not transfer across architectures, suggesting that the locus of conflict resolution may be model-specific even when the representational signature is shared.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe probe two instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \\citep{grattafiori2024llama} and Qwen3-8B (36 layers, hidden dimension 4096) \\citep{yang2024qwen25}.\n\n\\paragraph{Dataset.}\nWe use ConflictQA \\citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.\nAfter verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test) and 966 samples for Qwen (773 train / 193 test), split 80/20 with stratification.\n\n\\paragraph{Translation.}\nWe translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\\to$ZH), with quality validated by COMET \\citep{rei2020comet} back-translation scores.\n\n\\paragraph{Probing.}\nFor each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.\nWe report balanced accuracy to account for class imbalance.\nAll confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\n\n\\subsection{Within-Language Conflict Detection}\n\\label{sec:within_lang}\n\nTable~\\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.\nBoth models encode linearly detectable conflict signals in their residual streams.\nLlama achieves 77.1\\% on EN$\\to$EN (peak at layer 28, 88\\% depth) and 71.2\\% on ZH$\\to$ZH.\nQwen reaches 75.3\\% on EN$\\to$EN (peak at layer 22, 61\\% depth) and 71.6\\% on ZH$\\to$ZH.\nAll within-language accuracies are significantly above chance (binomial $p < 0.001$).\nFigure~\\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for both models.\nThese results confirm that knowledge conflict signals are linearly separable in the residual stream across both architectures and both languages.\n\n\\subsection{Cross-Lingual Transfer and Asymmetry}\n\\label{sec:cross_lingual}\n\nAll four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\\ref{tab:main_results}), confirming that conflict representations partially overlap across languages.\nBoth models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\\to$EN) more accurately than the reverse direction (EN$\\to$ZH).\nFor Llama, $\\Delta_{\\text{asym}} = +7.2$ percentage points (pp) with a 95\\% bootstrap CI of [1.1, 13.6]; for Qwen, $\\Delta_{\\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7].\nThe magnitude of this asymmetry closely matches the XNLI non-conflict baseline (\\S\\ref{sec:xnli_baseline}), and the consistent direction across architectures suggests a shared structural property rather than a model-specific artifact (Figure~\\ref{fig:asymmetry_forest}).\n\n%% Table 1: Main cross-lingual probe results\n\\begin{table}[t]\n\\centering\n\\caption{Cross-lingual probe balanced accuracy (\\%) with bootstrap 95\\% CIs ($n \\geq 100$). $\\Delta_{\\text{asym}}$ = acc(ZH$\\to$EN) $-$ acc(EN$\\to$ZH), computed as the mean of paired bootstrap differences. Bold: best per-task direction.}\n\\label{tab:main_results}\n\\begin{tabular}{lcc}\n\\toprule\nDirection & Llama-3.1-8B & Qwen3-8B \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Conflict Task}} \\\\\nEN $\\to$ EN & \\textbf{77.1} & \\textbf{75.3} \\\\\nZH $\\to$ ZH & 71.2 & 71.6 \\\\\nEN $\\to$ ZH & 64.1 & 65.0 \\\\\nZH $\\to$ EN & 71.3 & 72.2 \\\\\n$\\Delta_{\\text{asym}}$ & +7.2 [1.1, 13.6] & +7.2 [$-$0.6, 13.7] \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{XNLI Baseline}} \\\\\nEN $\\to$ EN & 94.0 & 96.6 \\\\\nZH $\\to$ ZH & 87.5 & 89.5 \\\\\nEN $\\to$ ZH & 89.0 & 90.5 \\\\\nZH $\\to$ EN & \\textbf{94.9} & \\textbf{97.2} \\\\\n$\\Delta_{\\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Non-Conflict Baseline Comparison}\n\\label{sec:xnli_baseline}\n\nIf the ZH$\\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.\nWe test this prediction using XNLI entailment-versus-contradiction probes.\nBoth models achieve high within-language accuracy on XNLI (Llama 94.0\\% EN, 87.5\\% ZH; Qwen 96.6\\% EN, 89.5\\% ZH), confirming that the probing pipeline captures semantic distinctions beyond knowledge conflicts.\nThe XNLI probes exhibit the same directional asymmetry: Llama $\\Delta_{\\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\\Delta_{\\text{asym}} = +6.7$ pp, CI [2.4, 11.7].\nBoth XNLI CIs exclude zero, and both overlap substantially with the corresponding conflict-task CIs (Figure~\\ref{fig:asymmetry_forest}).\nThe close match in asymmetry magnitude between conflict probes (Llama +7.2, Qwen +7.2 pp) and XNLI probes (Llama +6.0, Qwen +6.7 pp) indicates that the ZH$\\to$EN transfer advantage is not specific to knowledge conflict representations.\nInstead, it reflects a general cross-lingual property: Chinese-trained probes transfer to English more readily than the reverse, regardless of the downstream task.\n\n\\subsection{Confound Exclusion}\n\\label{sec:confounds}\n\nTwo potential confounds could inflate cross-lingual probe accuracy: translation quality and lexical overlap between English and Chinese inputs.\n\n\\paragraph{Translation quality.}\nWe stratify test samples by COMET score into terciles (high, medium, low) and compare EN$\\to$ZH probe accuracy across strata.\nIf translation quality drove probe transfer, high-COMET samples would yield higher accuracy.\nTable~\\ref{tab:confound} shows no such pattern: Qwen exhibits a reversed direction ($\\Delta = -5.6$ pp, Fisher $p = 0.695$), and Llama shows a negligible effect ($\\Delta = +1.7$ pp, Fisher $p = 0.761$).\nTranslation quality does not confound the cross-lingual transfer results.\n\n\\paragraph{Token overlap.}\nPer-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\\%, consistent with the minimal lexical overlap between the two languages.\nNeither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$), where higher overlap is associated with \\emph{lower} accuracy.\nShared tokens do not drive cross-lingual transfer.\n\n%% Table 2: Confound exclusion\n\\begin{table}[t]\n\\centering\n\\caption{Confound exclusion analysis. COMET tercile: $\\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\\to$ZH probe accuracy.}\n\\label{tab:confound}\n\\begin{tabular}{llrl}\n\\toprule\nConfound & Model & Result & $p$ \\\\\n\\midrule\nCOMET tercile & Qwen & $\\Delta = -5.6$ pp & 0.695 \\\\\nCOMET tercile & Llama & $\\Delta = +1.7$ pp & 0.761 \\\\\n\\midrule\nToken overlap & Qwen & n.s. & $>$0.4 \\\\\nToken overlap & Llama & $r = -0.15$ & 0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Causal Evidence via Representation Steering}\n\\label{sec:steering}\n\nThe probing results establish that conflict signals are detectable, but detection does not imply causal relevance.\nWe test whether the probe weight direction $\\mathbf{w}_{\\text{probe}}$ causally influences conflict resolution by injecting $\\alpha \\cdot \\mathbf{w}_{\\text{probe}}$ into the last-token residual stream at a target layer during inference.\nWe measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.\n\n\\paragraph{L13 (mid-layer, 41\\% depth).}\nSteering at layer 13 produces significantly more behavioral change than random controls in both directions (Table~\\ref{tab:steering}).\nPositive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$), with all 4 directional flips moving from parametric to contextual answers.\nNegative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% (Fisher $p < 0.001$), with 5 of 6 directional flips moving from contextual to parametric.\nBoth results survive Bonferroni correction for multiple comparisons.\nThe bidirectionality confirms that the probe weight vector encodes a meaningful axis of conflict resolution: positive perturbations push toward contextual answers, and negative perturbations push toward parametric answers.\n\n\\paragraph{Negative layers.}\nSteering at L28 (the probing peak layer, 88\\% depth) produces no significant effect with either last-token or all-position injection (all Fisher $p > 0.3$; Table~\\ref{tab:steering}).\nL18 (the MLP probe peak, 56\\% depth) also shows no causal influence (all Fisher $p > 0.44$).\n\n\\paragraph{$\\alpha = +20$ reversal.}\nAt extreme perturbation magnitude ($\\alpha = +20$), the control condition produces more flips than the steering condition ($p = 0.053$).\nThis indicates coherence collapse at large perturbation magnitudes, constraining the effective steering range.\n\n\\paragraph{Detection $\\neq$ Decision.}\nThe detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\nProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\n\\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation.\n\n%% Table 3: Steering results\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results (Llama-3.1-8B). Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 0.370 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B L13: \\textbf{[PLACEHOLDER]}}} \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.\n\\end{flushleft}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 135,
        "oldLines": 10,
        "newStart": 135,
        "newLines": 16,
        "lines": [
          " This indicates coherence collapse at large perturbation magnitudes, constraining the effective steering range.",
          " ",
          " \\paragraph{Detection $\\neq$ Decision.}",
          "-The detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).",
          "+In Llama, the detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).",
          " Probing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.",
          "-\\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation.",
          "+Injecting at all token positions (L13, all) yields identical results to last-token injection, indicating that the causal signal is concentrated in the final token's residual stream.",
          " ",
          "+\\paragraph{Cross-model steering.}",
          "+Steering at Qwen's mid-layer (L14, 39\\% depth; probe accuracy 70.2\\%) produces no significant behavioral change (best Fisher $p = 0.682$, $\\alpha = -10$), with zero directional flips across all steering magnitudes ($n_{\\text{test}} = 84$).",
          "+L23 (64\\% depth; probe accuracy 73.2\\%) is similarly negative (all $p = 1.0$).",
          "+Despite comparable probe accuracies (70--73\\%), the Qwen probe directions fail to causally shift answer routing, indicating that linear detectability does not entail causal relevance.",
          "+The mid-layer causal node identified in Llama L13 does not transfer across architectures, suggesting that the locus of conflict resolution may be model-specific even when the representational signature is shared.",
          "+",
          " %% Table 3: Steering results",
          " \\begin{table}[t]",
          " \\centering"
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

_source line 18_

Now update the table to include all configurations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "0a2b8b8e-f125-4178-b395-1a758322afc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTWQBnXmMUu7bgWDAzdtpQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 33297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 691
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

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_01XdUnzUcbaM86kLegr32dUh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex",
  "old_string": "%% Table 3: Steering results\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results (Llama-3.1-8B). Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 0.370 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B L13: \\textbf{[PLACEHOLDER]}}} \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.\n\\end{flushleft}\n\\end{table}",
  "new_string": "%% Table 3: Steering results\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Llama-3.1-8B}} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL13 (all) & 41\\% & \\multicolumn{4}{c}{\\textit{identical to last-token}} & \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 0.370 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B}} \\\\\nL14 & 39\\% & $-10$ & \\multicolumn{2}{c}{0 dir.\\ flips} & 0.682 & \\\\\nL23 & 64\\% & --- & \\multicolumn{2}{c}{0 dir.\\ flips} & 1.000 & \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$ (Llama L13), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.\n\\end{flushleft}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "b594b5c7-7508-46f6-a010-f460dcf0e5be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YTWQBnXmMUu7bgWDAzdtpQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 33297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 691
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

_source line 20 · 2026-05-22T15:55:32.058Z_

<details><summary>↩ Tool result · `toolu_01XdUnzUcbaM86kLegr32dUh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "787ce28d-2a4a-4e57-876f-09a76e831dc9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex",
    "oldString": "%% Table 3: Steering results\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results (Llama-3.1-8B). Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 0.370 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B L13: \\textbf{[PLACEHOLDER]}}} \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.\n\\end{flushleft}\n\\end{table}",
    "newString": "%% Table 3: Steering results\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Llama-3.1-8B}} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL13 (all) & 41\\% & \\multicolumn{4}{c}{\\textit{identical to last-token}} & \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 0.370 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B}} \\\\\nL14 & 39\\% & $-10$ & \\multicolumn{2}{c}{0 dir.\\ flips} & 0.682 & \\\\\nL23 & 64\\% & --- & \\multicolumn{2}{c}{0 dir.\\ flips} & 1.000 & \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$ (Llama L13), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.\n\\end{flushleft}\n\\end{table}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe probe two instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \\citep{grattafiori2024llama} and Qwen3-8B (36 layers, hidden dimension 4096) \\citep{yang2024qwen25}.\n\n\\paragraph{Dataset.}\nWe use ConflictQA \\citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.\nAfter verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test) and 966 samples for Qwen (773 train / 193 test), split 80/20 with stratification.\n\n\\paragraph{Translation.}\nWe translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\\to$ZH), with quality validated by COMET \\citep{rei2020comet} back-translation scores.\n\n\\paragraph{Probing.}\nFor each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.\nWe report balanced accuracy to account for class imbalance.\nAll confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\n\n\\subsection{Within-Language Conflict Detection}\n\\label{sec:within_lang}\n\nTable~\\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.\nBoth models encode linearly detectable conflict signals in their residual streams.\nLlama achieves 77.1\\% on EN$\\to$EN (peak at layer 28, 88\\% depth) and 71.2\\% on ZH$\\to$ZH.\nQwen reaches 75.3\\% on EN$\\to$EN (peak at layer 22, 61\\% depth) and 71.6\\% on ZH$\\to$ZH.\nAll within-language accuracies are significantly above chance (binomial $p < 0.001$).\nFigure~\\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for both models.\nThese results confirm that knowledge conflict signals are linearly separable in the residual stream across both architectures and both languages.\n\n\\subsection{Cross-Lingual Transfer and Asymmetry}\n\\label{sec:cross_lingual}\n\nAll four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\\ref{tab:main_results}), confirming that conflict representations partially overlap across languages.\nBoth models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\\to$EN) more accurately than the reverse direction (EN$\\to$ZH).\nFor Llama, $\\Delta_{\\text{asym}} = +7.2$ percentage points (pp) with a 95\\% bootstrap CI of [1.1, 13.6]; for Qwen, $\\Delta_{\\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7].\nThe magnitude of this asymmetry closely matches the XNLI non-conflict baseline (\\S\\ref{sec:xnli_baseline}), and the consistent direction across architectures suggests a shared structural property rather than a model-specific artifact (Figure~\\ref{fig:asymmetry_forest}).\n\n%% Table 1: Main cross-lingual probe results\n\\begin{table}[t]\n\\centering\n\\caption{Cross-lingual probe balanced accuracy (\\%) with bootstrap 95\\% CIs ($n \\geq 100$). $\\Delta_{\\text{asym}}$ = acc(ZH$\\to$EN) $-$ acc(EN$\\to$ZH), computed as the mean of paired bootstrap differences. Bold: best per-task direction.}\n\\label{tab:main_results}\n\\begin{tabular}{lcc}\n\\toprule\nDirection & Llama-3.1-8B & Qwen3-8B \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Conflict Task}} \\\\\nEN $\\to$ EN & \\textbf{77.1} & \\textbf{75.3} \\\\\nZH $\\to$ ZH & 71.2 & 71.6 \\\\\nEN $\\to$ ZH & 64.1 & 65.0 \\\\\nZH $\\to$ EN & 71.3 & 72.2 \\\\\n$\\Delta_{\\text{asym}}$ & +7.2 [1.1, 13.6] & +7.2 [$-$0.6, 13.7] \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{XNLI Baseline}} \\\\\nEN $\\to$ EN & 94.0 & 96.6 \\\\\nZH $\\to$ ZH & 87.5 & 89.5 \\\\\nEN $\\to$ ZH & 89.0 & 90.5 \\\\\nZH $\\to$ EN & \\textbf{94.9} & \\textbf{97.2} \\\\\n$\\Delta_{\\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Non-Conflict Baseline Comparison}\n\\label{sec:xnli_baseline}\n\nIf the ZH$\\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.\nWe test this prediction using XNLI entailment-versus-contradiction probes.\nBoth models achieve high within-language accuracy on XNLI (Llama 94.0\\% EN, 87.5\\% ZH; Qwen 96.6\\% EN, 89.5\\% ZH), confirming that the probing pipeline captures semantic distinctions beyond knowledge conflicts.\nThe XNLI probes exhibit the same directional asymmetry: Llama $\\Delta_{\\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\\Delta_{\\text{asym}} = +6.7$ pp, CI [2.4, 11.7].\nBoth XNLI CIs exclude zero, and both overlap substantially with the corresponding conflict-task CIs (Figure~\\ref{fig:asymmetry_forest}).\nThe close match in asymmetry magnitude between conflict probes (Llama +7.2, Qwen +7.2 pp) and XNLI probes (Llama +6.0, Qwen +6.7 pp) indicates that the ZH$\\to$EN transfer advantage is not specific to knowledge conflict representations.\nInstead, it reflects a general cross-lingual property: Chinese-trained probes transfer to English more readily than the reverse, regardless of the downstream task.\n\n\\subsection{Confound Exclusion}\n\\label{sec:confounds}\n\nTwo potential confounds could inflate cross-lingual probe accuracy: translation quality and lexical overlap between English and Chinese inputs.\n\n\\paragraph{Translation quality.}\nWe stratify test samples by COMET score into terciles (high, medium, low) and compare EN$\\to$ZH probe accuracy across strata.\nIf translation quality drove probe transfer, high-COMET samples would yield higher accuracy.\nTable~\\ref{tab:confound} shows no such pattern: Qwen exhibits a reversed direction ($\\Delta = -5.6$ pp, Fisher $p = 0.695$), and Llama shows a negligible effect ($\\Delta = +1.7$ pp, Fisher $p = 0.761$).\nTranslation quality does not confound the cross-lingual transfer results.\n\n\\paragraph{Token overlap.}\nPer-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\\%, consistent with the minimal lexical overlap between the two languages.\nNeither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$), where higher overlap is associated with \\emph{lower} accuracy.\nShared tokens do not drive cross-lingual transfer.\n\n%% Table 2: Confound exclusion\n\\begin{table}[t]\n\\centering\n\\caption{Confound exclusion analysis. COMET tercile: $\\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\\to$ZH probe accuracy.}\n\\label{tab:confound}\n\\begin{tabular}{llrl}\n\\toprule\nConfound & Model & Result & $p$ \\\\\n\\midrule\nCOMET tercile & Qwen & $\\Delta = -5.6$ pp & 0.695 \\\\\nCOMET tercile & Llama & $\\Delta = +1.7$ pp & 0.761 \\\\\n\\midrule\nToken overlap & Qwen & n.s. & $>$0.4 \\\\\nToken overlap & Llama & $r = -0.15$ & 0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Causal Evidence via Representation Steering}\n\\label{sec:steering}\n\nThe probing results establish that conflict signals are detectable, but detection does not imply causal relevance.\nWe test whether the probe weight direction $\\mathbf{w}_{\\text{probe}}$ causally influences conflict resolution by injecting $\\alpha \\cdot \\mathbf{w}_{\\text{probe}}$ into the last-token residual stream at a target layer during inference.\nWe measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.\n\n\\paragraph{L13 (mid-layer, 41\\% depth).}\nSteering at layer 13 produces significantly more behavioral change than random controls in both directions (Table~\\ref{tab:steering}).\nPositive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$), with all 4 directional flips moving from parametric to contextual answers.\nNegative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% (Fisher $p < 0.001$), with 5 of 6 directional flips moving from contextual to parametric.\nBoth results survive Bonferroni correction for multiple comparisons.\nThe bidirectionality confirms that the probe weight vector encodes a meaningful axis of conflict resolution: positive perturbations push toward contextual answers, and negative perturbations push toward parametric answers.\n\n\\paragraph{Negative layers.}\nSteering at L28 (the probing peak layer, 88\\% depth) produces no significant effect with either last-token or all-position injection (all Fisher $p > 0.3$; Table~\\ref{tab:steering}).\nL18 (the MLP probe peak, 56\\% depth) also shows no causal influence (all Fisher $p > 0.44$).\n\n\\paragraph{$\\alpha = +20$ reversal.}\nAt extreme perturbation magnitude ($\\alpha = +20$), the control condition produces more flips than the steering condition ($p = 0.053$).\nThis indicates coherence collapse at large perturbation magnitudes, constraining the effective steering range.\n\n\\paragraph{Detection $\\neq$ Decision.}\nIn Llama, the detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\nProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\nInjecting at all token positions (L13, all) yields identical results to last-token injection, indicating that the causal signal is concentrated in the final token's residual stream.\n\n\\paragraph{Cross-model steering.}\nSteering at Qwen's mid-layer (L14, 39\\% depth; probe accuracy 70.2\\%) produces no significant behavioral change (best Fisher $p = 0.682$, $\\alpha = -10$), with zero directional flips across all steering magnitudes ($n_{\\text{test}} = 84$).\nL23 (64\\% depth; probe accuracy 73.2\\%) is similarly negative (all $p = 1.0$).\nDespite comparable probe accuracies (70--73\\%), the Qwen probe directions fail to causally shift answer routing, indicating that linear detectability does not entail causal relevance.\nThe mid-layer causal node identified in Llama L13 does not transfer across architectures, suggesting that the locus of conflict resolution may be model-specific even when the representational signature is shared.\n\n%% Table 3: Steering results\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results (Llama-3.1-8B). Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 0.370 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B L13: \\textbf{[PLACEHOLDER]}}} \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.\n\\end{flushleft}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 148,
        "oldLines": 23,
        "newStart": 148,
        "newLines": 27,
        "lines": [
          " %% Table 3: Steering results",
          " \\begin{table}[t]",
          " \\centering",
          "-\\caption{Representation steering results (Llama-3.1-8B). Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\\dagger}$}",
          "+\\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\\dagger}$}",
          " \\label{tab:steering}",
          " \\small",
          " \\begin{tabular}{lcrrrrl}",
          " \\toprule",
          " Layer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\",
          " \\midrule",
          "+\\multicolumn{7}{l}{\\textit{Llama-3.1-8B}} \\\\",
          " \\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\",
          " \\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\",
          "+L13 (all) & 41\\% & \\multicolumn{4}{c}{\\textit{identical to last-token}} & \\\\",
          " L18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\",
          " L28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\",
          " L28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 0.370 & \\\\",
          " \\midrule",
          "-\\multicolumn{7}{l}{\\textit{Qwen3-8B L13: \\textbf{[PLACEHOLDER]}}} \\\\",
          "+\\multicolumn{7}{l}{\\textit{Qwen3-8B}} \\\\",
          "+L14 & 39\\% & $-10$ & \\multicolumn{2}{c}{0 dir.\\ flips} & 0.682 & \\\\",
          "+L23 & 64\\% & --- & \\multicolumn{2}{c}{0 dir.\\ flips} & 1.000 & \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\begin{flushleft}",
          "-\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.",
          "+\\footnotesize $^{\\dagger}$ At $\\alpha = +20$ (Llama L13), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.",
          " \\end{flushleft}",
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

_source line 21_

Let me verify the final result.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "d8b21896-c912-41fa-919b-a5cc1fa32ac2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FUkYam2a3ij45NmNYrFrXE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 33988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1525
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01EpDyFMRuyDioCmkk3K9daK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex",
  "offset": 114
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "8a94db0f-9848-4722-97bc-79766eec8ec3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FUkYam2a3ij45NmNYrFrXE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 33988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1525
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

_source line 23 · 2026-05-22T15:55:35.172Z_

<details><summary>↩ Tool result · `toolu_01EpDyFMRuyDioCmkk3K9daK`</summary>

```text
114	
115	\subsection{Causal Evidence via Representation Steering}
116	\label{sec:steering}
117	
118	The probing results establish that conflict signals are detectable, but detection does not imply causal relevance.
119	We test whether the probe weight direction $\mathbf{w}_{\text{probe}}$ causally influences conflict resolution by injecting $\alpha \cdot \mathbf{w}_{\text{probe}}$ into the last-token residual stream at a target layer during inference.
120	We measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.
121	
122	\paragraph{L13 (mid-layer, 41\% depth).}
123	Steering at layer 13 produces significantly more behavioral change than random controls in both directions (Table~\ref{tab:steering}).
124	Positive steering ($\alpha = +5$) yields a flip rate of 19.9\% versus 6.6\% for the random control (Fisher $p = 0.002$), with all 4 directional flips moving from parametric to contextual answers.
125	Negative steering ($\alpha = -20$) yields 36.0\% versus 17.6\% (Fisher $p < 0.001$), with 5 of 6 directional flips moving from contextual to parametric.
126	Both results survive Bonferroni correction for multiple comparisons.
127	The bidirectionality confirms that the probe weight vector encodes a meaningful axis of conflict resolution: positive perturbations push toward contextual answers, and negative perturbations push toward parametric answers.
128	
129	\paragraph{Negative layers.}
130	Steering at L28 (the probing peak layer, 88\% depth) produces no significant effect with either last-token or all-position injection (all Fisher $p > 0.3$; Table~\ref{tab:steering}).
131	L18 (the MLP probe peak, 56\% depth) also shows no causal influence (all Fisher $p > 0.44$).
132	
133	\paragraph{$\alpha = +20$ reversal.}
134	At extreme perturbation magnitude ($\alpha = +20$), the control condition produces more flips than the steering condition ($p = 0.053$).
135	This indicates coherence collapse at large perturbation magnitudes, constraining the effective steering range.
136	
137	\paragraph{Detection $\neq$ Decision.}
138	In Llama, the detectable conflict signal peaks at late layers (L28, 88\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\% depth).
139	Probing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.
140	Injecting at all token positions (L13, all) yields identical results to last-token injection, indicating that the causal signal is concentrated in the final token's residual stream.
141	
142	\paragraph{Cross-model steering.}
143	Steering at Qwen's mid-layer (L14, 39\% depth; probe accuracy 70.2\%) produces no significant behavioral change (best Fisher $p = 0.682$, $\alpha = -10$), with zero directional flips across all steering magnitudes ($n_{\text{test}} = 84$).
144	L23 (64\% depth; probe accuracy 73.2\%) is similarly negative (all $p = 1.0$).
145	Despite comparable probe accuracies (70--73\%), the Qwen probe directions fail to causally shift answer routing, indicating that linear detectability does not entail causal relevance.
146	The mid-layer causal node identified in Llama L13 does not transfer across architectures, suggesting that the locus of conflict resolution may be model-specific even when the representational signature is shared.
147	
148	%% Table 3: Steering results
149	\begin{table}[t]
150	\centering
151	\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\dagger}$}
152	\label{tab:steering}
153	\small
154	\begin{tabular}{lcrrrrl}
155	\toprule
156	Layer & Depth & $\alpha$ & Steer (\%) & Ctrl (\%) & Fisher $p$ & Dir. \\
157	\midrule
158	\multicolumn{7}{l}{\textit{Llama-3.1-8B}} \\
159	\textbf{L13} & \textbf{41\%} & $\mathbf{+5}$ & \textbf{19.9} & \textbf{6.6} & $\mathbf{0.002}$ & \textbf{4 p$\to$c} \\
160	\textbf{L13} & \textbf{41\%} & $\mathbf{-20}$ & \textbf{36.0} & \textbf{17.6} & $\mathbf{<0.001}$ & \textbf{5 c$\to$p} \\
161	L13 (all) & 41\% & \multicolumn{4}{c}{\textit{identical to last-token}} & \\
162	L18 & 56\% & $+2$ & 3.7 & 1.5 & 0.447 & \\
163	L28 & 88\% & $-20$ & 14.7 & 16.9 & 0.740 & \\
164	L28 (all) & 88\% & $-20$ & 11.8 & 11.8 & 0.370 & \\
165	\midrule
166	\multicolumn{7}{l}{\textit{Qwen3-8B}} \\
167	L14 & 39\% & $-10$ & \multicolumn{2}{c}{0 dir.\ flips} & 0.682 & \\
168	L23 & 64\% & --- & \multicolumn{2}{c}{0 dir.\ flips} & 1.000 & \\
169	\bottomrule
170	\end{tabular}
171	\begin{flushleft}
172	\footnotesize $^{\dagger}$ At $\alpha = +20$ (Llama L13), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.
173	\end{flushleft}
174	\end{table}
175	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "812796d5-7769-4c63-a088-d9bc8086da73",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex",
      "content": "\n\\subsection{Causal Evidence via Representation Steering}\n\\label{sec:steering}\n\nThe probing results establish that conflict signals are detectable, but detection does not imply causal relevance.\nWe test whether the probe weight direction $\\mathbf{w}_{\\text{probe}}$ causally influences conflict resolution by injecting $\\alpha \\cdot \\mathbf{w}_{\\text{probe}}$ into the last-token residual stream at a target layer during inference.\nWe measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.\n\n\\paragraph{L13 (mid-layer, 41\\% depth).}\nSteering at layer 13 produces significantly more behavioral change than random controls in both directions (Table~\\ref{tab:steering}).\nPositive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$), with all 4 directional flips moving from parametric to contextual answers.\nNegative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% (Fisher $p < 0.001$), with 5 of 6 directional flips moving from contextual to parametric.\nBoth results survive Bonferroni correction for multiple comparisons.\nThe bidirectionality confirms that the probe weight vector encodes a meaningful axis of conflict resolution: positive perturbations push toward contextual answers, and negative perturbations push toward parametric answers.\n\n\\paragraph{Negative layers.}\nSteering at L28 (the probing peak layer, 88\\% depth) produces no significant effect with either last-token or all-position injection (all Fisher $p > 0.3$; Table~\\ref{tab:steering}).\nL18 (the MLP probe peak, 56\\% depth) also shows no causal influence (all Fisher $p > 0.44$).\n\n\\paragraph{$\\alpha = +20$ reversal.}\nAt extreme perturbation magnitude ($\\alpha = +20$), the control condition produces more flips than the steering condition ($p = 0.053$).\nThis indicates coherence collapse at large perturbation magnitudes, constraining the effective steering range.\n\n\\paragraph{Detection $\\neq$ Decision.}\nIn Llama, the detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\nProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\nInjecting at all token positions (L13, all) yields identical results to last-token injection, indicating that the causal signal is concentrated in the final token's residual stream.\n\n\\paragraph{Cross-model steering.}\nSteering at Qwen's mid-layer (L14, 39\\% depth; probe accuracy 70.2\\%) produces no significant behavioral change (best Fisher $p = 0.682$, $\\alpha = -10$), with zero directional flips across all steering magnitudes ($n_{\\text{test}} = 84$).\nL23 (64\\% depth; probe accuracy 73.2\\%) is similarly negative (all $p = 1.0$).\nDespite comparable probe accuracies (70--73\\%), the Qwen probe directions fail to causally shift answer routing, indicating that linear detectability does not entail causal relevance.\nThe mid-layer causal node identified in Llama L13 does not transfer across architectures, suggesting that the locus of conflict resolution may be model-specific even when the representational signature is shared.\n\n%% Table 3: Steering results\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Llama-3.1-8B}} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL13 (all) & 41\\% & \\multicolumn{4}{c}{\\textit{identical to last-token}} & \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 0.370 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B}} \\\\\nL14 & 39\\% & $-10$ & \\multicolumn{2}{c}{0 dir.\\ flips} & 0.682 & \\\\\nL23 & 64\\% & --- & \\multicolumn{2}{c}{0 dir.\\ flips} & 1.000 & \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$ (Llama L13), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.\n\\end{flushleft}\n\\end{table}\n",
      "numLines": 62,
      "startLine": 114,
      "totalLines": 175
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

完成。改动摘要：

**文本** (L137-146):
- "Detection ≠ Decision" 段改为 Llama-specific framing，补充 L13 all-position = last-token 的结论
- 新增 "Cross-model steering" 段，报告 Qwen L14 (p=0.682) 和 L23 (p=1.0) 均 negative，强调 detectability ≠ causality，用 "suggesting" hedging 跨模型结论

**Table 3** (L148-174):
- Caption 去掉 "(Llama-3.1-8B)"，改为两模型通用
- 按模型分组（Llama / Qwen），增加 L13 (all)、Qwen L14、Qwen L23 三行，共 7 个配置全覆盖
- 脚注补充 "(Llama L13)" 限定 α=+20 reversal 的适用范围

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "uuid": "34062e70-5075-4533-900e-deb6b3012bfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBdQQ8ErSAKtut42xA1KJj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1818,
      "cache_read_input_tokens": 35513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1818
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

_source line 25_

完成。改动摘要：

**文本** (L137-146):
- "Detection ≠ Decision" 段改为 Llama-specific framing，补充 L13 all-position = last-token 的结论
- 新增 "Cross-model steering" 段，报告 Qwen L14 (p=0.682) 和 L23 (p=1.0) 均 negative，强调 detectability ≠ causality，用 "suggesting" hedging 跨模型结论

**Table 3** (L148-174):
- Caption 去掉 "(Llama-3.1-8B)"，改为两模型通用
- 按模型分组（Llama / Qwen），增加 L13 (all)、Qwen L14、Qwen L23 三行，共 7 个配置全覆盖
- 脚注补充 "(Llama L13)" 限定 α=+20 reversal 的适用范围

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 127656,
  "duration_api_ms": 128293,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "bfbdbbf3-2f13-4a3b-9b3b-52910eed94eb",
  "total_cost_usd": 0.43908100000000005,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 25490,
    "cache_read_input_tokens": 200101,
    "output_tokens": 7118,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25490,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 265,
        "cache_read_input_tokens": 35513,
        "cache_creation_input_tokens": 1818,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1818
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1638,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001723,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 7118,
      "cacheReadInputTokens": 200101,
      "cacheCreationInputTokens": 25490,
      "webSearchRequests": 0,
      "costUSD": 0.437358,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c931363b-34dc-40da-8069-c7b70bd5f7f2"
}
```

</details>

---
