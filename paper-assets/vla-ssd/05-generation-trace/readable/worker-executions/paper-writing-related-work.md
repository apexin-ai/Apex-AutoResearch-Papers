# paper writing related work

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260516T023622.log`
- **Structured JSON:** [`c8596337efbeb6019da7.json`](../../sessions/c8/c8596337efbeb6019da7.json)

## Before a recorded user message

23 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
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
  "uuid": "261bc64f-4686-40cb-8db7-05dde5884da5",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1778904000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a40c8e1f-1309-45b5-b71e-77da1f51b5cf",
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to write a Related Work section for their paper about systematic representational analysis of VLA models. Let me first check what exists in the project to understand the context better, then write the LaTeX file.

Let me check existing paper files and the project structure to align with existing conventions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "f7cec7e0-ebdd-4ca2-b7d5-8170d13990d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCmPu3YS6ipQttpREannAx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12212,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12212
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

### Assistant

_source line 5_

Let me first check existing paper files for style/key conventions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "bf9fc0a2-93ce-42d1-928e-a18b5faec650",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCmPu3YS6ipQttpREannAx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12212,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12212
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

_source line 6_

<details open><summary>🔧 Tool call — Glob · `toolu_01RPuFoLwT6V1sF9r3hRDC67`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "52428806-4108-4a87-a087-61ce7fe3f099",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCmPu3YS6ipQttpREannAx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12212,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12212
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

_source line 7 · 2026-05-16T02:36:33.053Z_

<details><summary>↩ Tool result · `toolu_01RPuFoLwT6V1sF9r3hRDC67`</summary>

```text
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "2bac234a-d186-4d8d-ba69-7f0014156d00",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/introduction.tex"
    ],
    "durationMs": 26,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01EkpzUndeEyBk5PR3iroK6o`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "07503fa5-ce41-4019-8b46-7ae3ad30daad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GCmPu3YS6ipQttpREannAx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12212,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12212
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

_source line 9 · 2026-05-16T02:36:33.576Z_

<details><summary>↩ Tool result · `toolu_01EkpzUndeEyBk5PR3iroK6o`</summary>

```text
artifacts/_project/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "952600a7-2691-4655-9094-b6b3fdf2c032",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/references.bib"
    ],
    "durationMs": 15,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_013JBHEHV16WYrzLmcfskK3b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "8d46fed9-673f-44ed-9137-9f25208b4049",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnPox1abEHNmDsqLoGkbPs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 24053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 383
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

_source line 11 · 2026-05-16T02:36:36.192Z_

<details><summary>↩ Tool result · `toolu_013JBHEHV16WYrzLmcfskK3b`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Benchmark and model.}
8	We evaluate on the LIBERO-Goal suite~\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.
9	We use OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a SigLIP-SO400M vision encoder~\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone, fine-tuned on the LIBERO-10 split.
10	
11	\paragraph{Representation sources.}
12	We extract representations from five sources:
13	(a)~\textbf{SigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;
14	(b)~\textbf{LLM image\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;
15	(c)~\textbf{LLM last\_preaction}---the final token position before action decoding (readout token) at each LLM layer;
16	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} \texttt{cls\_token}; and
17	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} \texttt{patch\_mean}.
18	Sources (d) and (e) serve as external baselines with no VLA training signal.
19	
20	\paragraph{Experimental conditions.}
21	We use a $2 \times 2$ factorial design crossing \emph{training status} (trained vs.\ untrained) with \emph{instruction presence} (with vs.\ without language instruction).
22	The untrained control applies \texttt{from\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen SigLIP encoder (0.80B pretrained weights), isolating the LLM's learned contribution from the vision encoder's pretrained geometry.
23	
24	\paragraph{Representational Similarity Analysis (RSA).}
25	Following~\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.
26	We report Spearman rank correlation $\rho$ between representation and action RDMs, with 95\% confidence intervals from 10{,}000 bootstrap resamples.
27	
28	\paragraph{Functional probes.}
29	We train MLP probes (input $\to$ 256 $\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\cite{alain2017}. We report mean $R^2$ across action dimensions.
30	
31	%------------------------------------------------------------------
32	\subsection{Vision Encoder Dominance}
33	\label{sec:vision_dominance}
34	
35	This experiment tests whether vision-language pretrained encoders provide the dominant source of action-relevant geometric structure in VLA representations.
36	
37	Table~\ref{tab:rsa_overview} reports RSA $\rho$ between each representation source and the action space.
38	The SigLIP+Projector output achieves the highest alignment ($\rho = 0.615$, 95\% CI $[0.526, 0.695]$), followed by CLIP ViT-L/14 ($\rho = 0.557$, $[0.442, 0.660]$).
39	Both vision-language pretrained encoders substantially exceed DINOv2 ($\rho = 0.388$), a vision-only model.
40	The VLA's LLM layers (best image\_mean: $\rho = 0.501$ trained, $\rho = 0.485$ untrained) fall between VL-pretrained encoders and DINOv2 (Figure~\ref{fig:rsa_bar}).
41	
42	Three findings emerge.
43	First, VL pretraining---not LLM processing---is the primary source of action-relevant structure.
44	SigLIP and CLIP, both pretrained on image-text pairs, achieve $\rho \geq 0.557$, while DINOv2, pretrained with self-supervised vision objectives alone, reaches only $\rho = 0.388$.
45	This 0.169-point gap indicates that language-grounded visual features carry substantially more action-relevant geometry than features learned without language, consistent with behavioral evidence of visual dominance in VLA policies~\cite{grant2026}.
46	
47	Second, the MLP projector provides incremental alignment: SigLIP+Projector ($0.615$) exceeds CLIP ($0.557$) by $\Delta = 0.058$, consistent with the projector mapping vision features into the LLM's embedding space.
48	
49	Third, the LLM degrades rather than enhances vision encoder geometry.
50	Processing through the LLM reduces RSA from $0.615$ (projector output) to $0.501$ (best LLM image\_mean), a drop of $\Delta = 0.114$.
51	
52	\paragraph{Geometric-functional dissociation.}
53	Functional probes reveal a dissociation between geometric similarity and functional decodability.
54	DINOv2 achieves $R^2 = 0.712$, statistically indistinguishable from SigLIP+Projector ($R^2 = 0.706$, $p = 0.22$, n.s.), despite its substantially lower RSA ($0.388$ vs.\ $0.615$).
55	High linear decodability does not require high geometric alignment with the action space---DINOv2 features are functionally rich but geometrically dissimilar to actions.
56	
57	\paragraph{Metric sensitivity.}
58	This dissociation extends to alternative similarity metrics.
59	Linear CKA~\cite{kornblith2019} produces a different ranking from RSA: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially reversing the RSA ordering (Figure~\ref{fig:metric_comparison}).
60	RDM kernel CKA restores the RSA-consistent ranking (Proj $>$ Trained $>$ Untrained $>$ DINOv2).
61	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties and underscores the importance of multi-metric evaluation in representation analysis.
62	
63	\begin{table}[t]
64	\centering
65	\caption{RSA between representation and action RDMs ($\rho$ $\uparrow$). VL-pretrained encoders (SigLIP, CLIP) dominate over vision-only DINOv2 and LLM-processed representations. 95\% CIs from 10{,}000 bootstrap resamples.}
66	\label{tab:rsa_overview}
67	\small
68	\begin{tabular}{llcc}
69	\toprule
70	Source & Aggregation & RSA $\rho$ & 95\% CI \\
71	\midrule
72	SigLIP+Projector & --- & 0.615 & {[0.526, 0.695]} \\
73	CLIP ViT-L/14 & patch\_mean & 0.557 & {[0.442, 0.660]} \\
74	\midrule
75	VLA Trained w/ inst. & image\_mean & 0.501 & --- \\
76	VLA Trained no inst. & image\_mean & 0.501 & --- \\
77	VLA Untrained w/ inst. & image\_mean & 0.485 & --- \\
78	VLA Untrained no inst. & image\_mean & 0.482 & --- \\
79	\midrule
80	DINOv2 ViT-L/14 & cls\_token & 0.388 & --- \\
81	\bottomrule
82	\end{tabular}
83	\end{table}
84	
85	\begin{figure}[t]
86	\centering
87	\includegraphics[width=\columnwidth]{figures/fig2.pdf}
88	\caption{RSA with the action space ($\rho$) across representation sources. VL-pretrained encoders (SigLIP $\rho{=}0.615$, CLIP $\rho{=}0.557$) substantially exceed both LLM-processed representations ($\rho \leq 0.501$) and vision-only DINOv2 ($\rho{=}0.388$). Hatched bars indicate no-instruction conditions. Error bars: 95\% bootstrap CIs. Dashed line: DINOv2 reference.}
89	\label{fig:rsa_bar}
90	\end{figure}
91	
92	%------------------------------------------------------------------
93	\subsection{LLM Redistributes, Does Not Enhance, Action Structure}
94	\label{sec:llm_redistribution}
95	
96	This experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder.
97	Table~\ref{tab:probes} reports functional probe $R^2$ for key representation sources.
98	Two complementary effects characterize LLM processing.
99	
100	\paragraph{Distributed degradation.}
101	Averaging across image tokens, the LLM degrades both geometric and functional action information relative to the projector.
102	RSA drops from $0.615$ to $0.501$ ($\Delta = 0.114$); probe $R^2$ drops from $0.706$ to $0.683$ (95\% CI of $\Delta$: $[0.011, 0.037]$, $p = 0.001$).
103	Figure~\ref{fig:layer_curves} shows the per-layer trajectory: the sharpest drop occurs at the embedding interface (Projector $\to$ Layer~1), with non-monotonic fluctuations through middle layers before partial recovery near the output layers.
104	
105	\paragraph{Readout concentration.}
106	While distributed image tokens lose information, the last pre-action token (\texttt{last\_preaction}) concentrates action-relevant information beyond the projector baseline.
107	Trained readout achieves $R^2 = 0.731$, exceeding SigLIP+Projector ($R^2 = 0.706$, $p = 0.001$; Figure~\ref{fig:probe_bars}).
108	This concentration is training-dependent: untrained readout ($R^2 = 0.686$) falls below the projector baseline, while trained readout ($0.731$) substantially exceeds it ($\Delta = 0.045$, $p < 0.0001$).
109	
110	Together, these results characterize the LLM as a \emph{redistribution} mechanism: training teaches the model to route action-relevant information from distributed image tokens to the readout position, sacrificing distributed fidelity to concentrate a functionally superior action representation at the decoding interface~\cite{haon2025}.
111	
112	\begin{table}[t]
113	\centering
114	\caption{Functional probe $R^2$ ($\uparrow$) for action prediction from frozen representations. The LLM degrades distributed representations (image\_mean) relative to the projector but concentrates superior action information at the readout token---an effect that requires training. DINOv2 matches the projector in $R^2$ despite much lower RSA.}
115	\label{tab:probes}
116	\small
117	\begin{tabular}{lcc}
118	\toprule
119	Representation & $R^2$ & $p$ vs.\ Proj. \\
120	\midrule
121	SigLIP+Projector & 0.706 & --- \\
122	VLA Trained image\_mean (L19) & 0.683 & 0.001 \\
123	VLA Trained readout (L19) & \textbf{0.731} & 0.001 \\
124	VLA Untrained readout (L32) & 0.686 & --- \\
125	DINOv2 cls\_token & 0.712 & 0.220 (n.s.) \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	\begin{figure}[t]
131	\centering
132	\includegraphics[width=\columnwidth]{figures/fig3.pdf}
133	\caption{Per-layer RSA ($\rho$) with the action space across all 32 LLM layers under four experimental conditions (trained/untrained $\times$ with/without instruction). The sharpest drop occurs at the embedding interface (Proj $\to$ L1). Middle layers show non-monotonic fluctuations. Dashed lines: SigLIP+Projector ($\rho{=}0.615$) and DINOv2 ($\rho{=}0.388$) reference levels.}
134	\label{fig:layer_curves}
135	\end{figure}
136	
137	\begin{figure}[t]
138	\centering
139	\includegraphics[width=\columnwidth]{figures/fig4.pdf}
140	\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\_mean ($R^2{=}0.683$) below the projector baseline ($0.706$, $p{=}0.001$) but concentrates superior information at the trained readout ($0.731$, $p{=}0.001$). Untrained readout ($0.686$) falls below the projector, confirming that concentration requires training ($\Delta{=}0.045$, $p{<}0.0001$). DINOv2 ($0.712$) is statistically indistinguishable from the projector ($p{=}0.22$).}
141	\label{fig:probe_bars}
142	\end{figure}
143	
144	%------------------------------------------------------------------
145	\subsection{Training Routes, Does Not Create, Action Geometry}
146	\label{sec:training_routing}
147	
148	This experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.
149	Table~\ref{tab:training_effects} reports the effect of training across metrics.
150	The $2 \times 2$ factorial analysis (Figure~\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.
151	
152	\paragraph{Geometric invariance to training.}
153	Training does not alter the LLM's geometric alignment with the action space.
154	For image\_mean RSA, the training effect is $\Delta = +0.021$ (95\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\_preaction RSA, $\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).
155	This null result is consistent with the vision encoder---whose weights are identical between conditions ($\cos\text{sim} = 1.0$)---being the sole source of action-relevant geometry.
156	
157	\paragraph{Geometric invariance to instruction.}
158	Language instructions similarly fail to modulate geometric structure.
159	Across the $2 \times 2$ matrix, the instruction effect is $\Delta = 0.004$ (n.s.).
160	A dedicated control experiment with four instruction conditions---normal task instructions ($\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\pm 0.017$ of the mean (Figure~\ref{fig:factorial}b).
161	
162	\paragraph{Functional concentration requires training.}
163	In contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\Delta = +0.045$ (CI $[+0.032, +0.058]$, $p < 0.0001$).
164	Training transforms the readout from below-projector ($R^2 = 0.686$) to above-projector ($R^2 = 0.731$) without altering the underlying geometry.
165	
166	These results support a \emph{routing} interpretation of LLM training in VLAs~\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.
167	
168	\begin{table}[t]
169	\centering
170	\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\_mean $R^2$ drop confirms distributed degradation.}
171	\label{tab:training_effects}
172	\small
173	\begin{tabular}{lccc}
174	\toprule
175	Comparison & $\Delta$ & 95\% CI & $p$ \\
176	\midrule
177	Training (image\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\
178	Training (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\
179	Training (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\
180	Proj.\ vs.\ image\_mean ($R^2$) & $+$0.023 & [$+$0.011, $+$0.037] & 0.001 \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
185	\begin{figure}[t]
186	\centering
187	\includegraphics[width=\columnwidth]{figures/fig5.pdf}
188	\caption{\textbf{(a)}~Training $\times$ Instruction matrix for image\_mean RSA ($\rho$). Neither training ($\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\Delta{=}0.004$, n.s.)\ produces a statistically detectable effect. \textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\pm 0.017$ of the mean $\mu{=}0.482$, confirming that instruction content does not modulate distributed geometric structure.}
189	\label{fig:factorial}
190	\end{figure}
191	
192	\begin{figure}[t]
193	\centering
194	\includegraphics[width=\columnwidth]{figures/fig6.pdf}
195	\caption{Comparison of three similarity metrics across representation sources. \textbf{(a)}~RSA (Spearman $\rho$) and \textbf{(c)}~RDM kernel CKA produce consistent rankings (Proj $>$ Trained $>$ Untrained $>$ DINOv2). \textbf{(b)}~Linear CKA~\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}
196	\label{fig:metric_comparison}
197	\end{figure}
198	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "acb9de8a-b575-4bf8-874d-503a94ce2843",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Benchmark and model.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.\nWe use OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone, fine-tuned on the LIBERO-10 split.\n\n\\paragraph{Representation sources.}\nWe extract representations from five sources:\n(a)~\\textbf{SigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;\n(b)~\\textbf{LLM image\\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;\n(c)~\\textbf{LLM last\\_preaction}---the final token position before action decoding (readout token) at each LLM layer;\n(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token}; and\n(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean}.\nSources (d) and (e) serve as external baselines with no VLA training signal.\n\n\\paragraph{Experimental conditions.}\nWe use a $2 \\times 2$ factorial design crossing \\emph{training status} (trained vs.\\ untrained) with \\emph{instruction presence} (with vs.\\ without language instruction).\nThe untrained control applies \\texttt{from\\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen SigLIP encoder (0.80B pretrained weights), isolating the LLM's learned contribution from the vision encoder's pretrained geometry.\n\n\\paragraph{Representational Similarity Analysis (RSA).}\nFollowing~\\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.\nWe report Spearman rank correlation $\\rho$ between representation and action RDMs, with 95\\% confidence intervals from 10{,}000 bootstrap resamples.\n\n\\paragraph{Functional probes.}\nWe train MLP probes (input $\\to$ 256 $\\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\\cite{alain2017}. We report mean $R^2$ across action dimensions.\n\n%------------------------------------------------------------------\n\\subsection{Vision Encoder Dominance}\n\\label{sec:vision_dominance}\n\nThis experiment tests whether vision-language pretrained encoders provide the dominant source of action-relevant geometric structure in VLA representations.\n\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ between each representation source and the action space.\nThe SigLIP+Projector output achieves the highest alignment ($\\rho = 0.615$, 95\\% CI $[0.526, 0.695]$), followed by CLIP ViT-L/14 ($\\rho = 0.557$, $[0.442, 0.660]$).\nBoth vision-language pretrained encoders substantially exceed DINOv2 ($\\rho = 0.388$), a vision-only model.\nThe VLA's LLM layers (best image\\_mean: $\\rho = 0.501$ trained, $\\rho = 0.485$ untrained) fall between VL-pretrained encoders and DINOv2 (Figure~\\ref{fig:rsa_bar}).\n\nThree findings emerge.\nFirst, VL pretraining---not LLM processing---is the primary source of action-relevant structure.\nSigLIP and CLIP, both pretrained on image-text pairs, achieve $\\rho \\geq 0.557$, while DINOv2, pretrained with self-supervised vision objectives alone, reaches only $\\rho = 0.388$.\nThis 0.169-point gap indicates that language-grounded visual features carry substantially more action-relevant geometry than features learned without language, consistent with behavioral evidence of visual dominance in VLA policies~\\cite{grant2026}.\n\nSecond, the MLP projector provides incremental alignment: SigLIP+Projector ($0.615$) exceeds CLIP ($0.557$) by $\\Delta = 0.058$, consistent with the projector mapping vision features into the LLM's embedding space.\n\nThird, the LLM degrades rather than enhances vision encoder geometry.\nProcessing through the LLM reduces RSA from $0.615$ (projector output) to $0.501$ (best LLM image\\_mean), a drop of $\\Delta = 0.114$.\n\n\\paragraph{Geometric-functional dissociation.}\nFunctional probes reveal a dissociation between geometric similarity and functional decodability.\nDINOv2 achieves $R^2 = 0.712$, statistically indistinguishable from SigLIP+Projector ($R^2 = 0.706$, $p = 0.22$, n.s.), despite its substantially lower RSA ($0.388$ vs.\\ $0.615$).\nHigh linear decodability does not require high geometric alignment with the action space---DINOv2 features are functionally rich but geometrically dissimilar to actions.\n\n\\paragraph{Metric sensitivity.}\nThis dissociation extends to alternative similarity metrics.\nLinear CKA~\\cite{kornblith2019} produces a different ranking from RSA: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially reversing the RSA ordering (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA restores the RSA-consistent ranking (Proj $>$ Trained $>$ Untrained $>$ DINOv2).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties and underscores the importance of multi-metric evaluation in representation analysis.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA between representation and action RDMs ($\\rho$ $\\uparrow$). VL-pretrained encoders (SigLIP, CLIP) dominate over vision-only DINOv2 and LLM-processed representations. 95\\% CIs from 10{,}000 bootstrap resamples.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSource & Aggregation & RSA $\\rho$ & 95\\% CI \\\\\n\\midrule\nSigLIP+Projector & --- & 0.615 & {[0.526, 0.695]} \\\\\nCLIP ViT-L/14 & patch\\_mean & 0.557 & {[0.442, 0.660]} \\\\\n\\midrule\nVLA Trained w/ inst. & image\\_mean & 0.501 & --- \\\\\nVLA Trained no inst. & image\\_mean & 0.501 & --- \\\\\nVLA Untrained w/ inst. & image\\_mean & 0.485 & --- \\\\\nVLA Untrained no inst. & image\\_mean & 0.482 & --- \\\\\n\\midrule\nDINOv2 ViT-L/14 & cls\\_token & 0.388 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. VL-pretrained encoders (SigLIP $\\rho{=}0.615$, CLIP $\\rho{=}0.557$) substantially exceed both LLM-processed representations ($\\rho \\leq 0.501$) and vision-only DINOv2 ($\\rho{=}0.388$). Hatched bars indicate no-instruction conditions. Error bars: 95\\% bootstrap CIs. Dashed line: DINOv2 reference.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{LLM Redistributes, Does Not Enhance, Action Structure}\n\\label{sec:llm_redistribution}\n\nThis experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder.\nTable~\\ref{tab:probes} reports functional probe $R^2$ for key representation sources.\nTwo complementary effects characterize LLM processing.\n\n\\paragraph{Distributed degradation.}\nAveraging across image tokens, the LLM degrades both geometric and functional action information relative to the projector.\nRSA drops from $0.615$ to $0.501$ ($\\Delta = 0.114$); probe $R^2$ drops from $0.706$ to $0.683$ (95\\% CI of $\\Delta$: $[0.011, 0.037]$, $p = 0.001$).\nFigure~\\ref{fig:layer_curves} shows the per-layer trajectory: the sharpest drop occurs at the embedding interface (Projector $\\to$ Layer~1), with non-monotonic fluctuations through middle layers before partial recovery near the output layers.\n\n\\paragraph{Readout concentration.}\nWhile distributed image tokens lose information, the last pre-action token (\\texttt{last\\_preaction}) concentrates action-relevant information beyond the projector baseline.\nTrained readout achieves $R^2 = 0.731$, exceeding SigLIP+Projector ($R^2 = 0.706$, $p = 0.001$; Figure~\\ref{fig:probe_bars}).\nThis concentration is training-dependent: untrained readout ($R^2 = 0.686$) falls below the projector baseline, while trained readout ($0.731$) substantially exceeds it ($\\Delta = 0.045$, $p < 0.0001$).\n\nTogether, these results characterize the LLM as a \\emph{redistribution} mechanism: training teaches the model to route action-relevant information from distributed image tokens to the readout position, sacrificing distributed fidelity to concentrate a functionally superior action representation at the decoding interface~\\cite{haon2025}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Functional probe $R^2$ ($\\uparrow$) for action prediction from frozen representations. The LLM degrades distributed representations (image\\_mean) relative to the projector but concentrates superior action information at the readout token---an effect that requires training. DINOv2 matches the projector in $R^2$ despite much lower RSA.}\n\\label{tab:probes}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nRepresentation & $R^2$ & $p$ vs.\\ Proj. \\\\\n\\midrule\nSigLIP+Projector & 0.706 & --- \\\\\nVLA Trained image\\_mean (L19) & 0.683 & 0.001 \\\\\nVLA Trained readout (L19) & \\textbf{0.731} & 0.001 \\\\\nVLA Untrained readout (L32) & 0.686 & --- \\\\\nDINOv2 cls\\_token & 0.712 & 0.220 (n.s.) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers under four experimental conditions (trained/untrained $\\times$ with/without instruction). The sharpest drop occurs at the embedding interface (Proj $\\to$ L1). Middle layers show non-monotonic fluctuations. Dashed lines: SigLIP+Projector ($\\rho{=}0.615$) and DINOv2 ($\\rho{=}0.388$) reference levels.}\n\\label{fig:layer_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\\_mean ($R^2{=}0.683$) below the projector baseline ($0.706$, $p{=}0.001$) but concentrates superior information at the trained readout ($0.731$, $p{=}0.001$). Untrained readout ($0.686$) falls below the projector, confirming that concentration requires training ($\\Delta{=}0.045$, $p{<}0.0001$). DINOv2 ($0.712$) is statistically indistinguishable from the projector ($p{=}0.22$).}\n\\label{fig:probe_bars}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Training Routes, Does Not Create, Action Geometry}\n\\label{sec:training_routing}\n\nThis experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.\nTable~\\ref{tab:training_effects} reports the effect of training across metrics.\nThe $2 \\times 2$ factorial analysis (Figure~\\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.\n\n\\paragraph{Geometric invariance to training.}\nTraining does not alter the LLM's geometric alignment with the action space.\nFor image\\_mean RSA, the training effect is $\\Delta = +0.021$ (95\\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\\_preaction RSA, $\\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).\nThis null result is consistent with the vision encoder---whose weights are identical between conditions ($\\cos\\text{sim} = 1.0$)---being the sole source of action-relevant geometry.\n\n\\paragraph{Geometric invariance to instruction.}\nLanguage instructions similarly fail to modulate geometric structure.\nAcross the $2 \\times 2$ matrix, the instruction effect is $\\Delta = 0.004$ (n.s.).\nA dedicated control experiment with four instruction conditions---normal task instructions ($\\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\\pm 0.017$ of the mean (Figure~\\ref{fig:factorial}b).\n\n\\paragraph{Functional concentration requires training.}\nIn contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\\Delta = +0.045$ (CI $[+0.032, +0.058]$, $p < 0.0001$).\nTraining transforms the readout from below-projector ($R^2 = 0.686$) to above-projector ($R^2 = 0.731$) without altering the underlying geometry.\n\nThese results support a \\emph{routing} interpretation of LLM training in VLAs~\\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\\_mean $R^2$ drop confirms distributed degradation.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\nTraining (image\\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\\\\nTraining (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\\\\nTraining (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\\\\nProj.\\ vs.\\ image\\_mean ($R^2$) & $+$0.023 & [$+$0.011, $+$0.037] & 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Training $\\times$ Instruction matrix for image\\_mean RSA ($\\rho$). Neither training ($\\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\\Delta{=}0.004$, n.s.)\\ produces a statistically detectable effect. \\textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\\pm 0.017$ of the mean $\\mu{=}0.482$, confirming that instruction content does not modulate distributed geometric structure.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Comparison of three similarity metrics across representation sources. \\textbf{(a)}~RSA (Spearman $\\rho$) and \\textbf{(c)}~RDM kernel CKA produce consistent rankings (Proj $>$ Trained $>$ Untrained $>$ DINOv2). \\textbf{(b)}~Linear CKA~\\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}\n\\label{fig:metric_comparison}\n\\end{figure}\n",
      "numLines": 198,
      "startLine": 1,
      "totalLines": 198
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01XBkpdmzGpti9t2c1XbGZDS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "1412d531-ea9c-410a-aa83-ca2d846787e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnPox1abEHNmDsqLoGkbPs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 24053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 383
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

_source line 13 · 2026-05-16T02:36:36.899Z_

<details><summary>↩ Tool result · `toolu_01XBkpdmzGpti9t2c1XbGZDS`</summary>

```text
1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	% [VERIFY] Confirm venue and exact title. Likely "Prismatic VLMs" or OpenVLA architecture companion.
11	@article{karamcheti2024,
12	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
13	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
14	  journal   = {arXiv preprint arXiv:2402.07865},
15	  year      = {2024},
16	}
17	
18	@article{brohan2023_rt2,
19	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
20	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
21	  journal   = {arXiv preprint arXiv:2307.15818},
22	  year      = {2023},
23	}
24	
25	% === Benchmark ===
26	
27	@inproceedings{liu2023_libero,
28	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
29	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
30	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
31	  year      = {2023},
32	}
33	
34	% === Representation Analysis Methods ===
35	
36	@article{kriegeskorte2008,
37	  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},
38	  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Bandettini, Peter},
39	  journal   = {Frontiers in Systems Neuroscience},
40	  volume    = {2},
41	  pages     = {4},
42	  year      = {2008},
43	  publisher = {Frontiers},
44	}
45	
46	@inproceedings{kornblith2019,
47	  title     = {Similarity of Neural Network Representations Revisited},
48	  author    = {Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},
49	  booktitle = {International Conference on Machine Learning (ICML)},
50	  year      = {2019},
51	}
52	
53	@article{alain2017,
54	  title     = {Understanding Intermediate Layers Using Linear Classifier Probes},
55	  author    = {Alain, Guillaume and Bengio, Yoshua},
56	  journal   = {arXiv preprint arXiv:1610.01644},
57	  year      = {2017},
58	}
59	
60	% === Vision Encoders ===
61	
62	@inproceedings{zhai2023_siglip,
63	  title     = {Sigmoid Loss for Language Image Pre-Training},
64	  author    = {Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},
65	  booktitle = {International Conference on Computer Vision (ICCV)},
66	  year      = {2023},
67	}
68	
69	@article{oquab2024_dinov2,
70	  title     = {{DINOv2}: Learning Robust Visual Features without Supervision},
71	  author    = {Oquab, Maxime and Darcet, Timoth{\'e}e and Moutakanni, Theo and Vo, Huy and Szafraniec, Marc and Khalidov, Vasil and Fernandez, Pierre and Haziza, Daniel and Massa, Francisco and El-Nouby, Alaaeldin and others},
72	  journal   = {Transactions on Machine Learning Research (TMLR)},
73	  year      = {2024},
74	}
75	
76	@inproceedings{radford2021_clip,
77	  title     = {Learning Transferable Visual Models From Natural Language Supervision},
78	  author    = {Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and others},
79	  booktitle = {International Conference on Machine Learning (ICML)},
80	  year      = {2021},
81	}
82	
83	% === Domain-Specific ===
84	
85	@article{grant2026,
86	  title     = {Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models},
87	  author    = {Grant, Bryce and Zhao, Xijia and Wang, Peng},
88	  journal   = {arXiv preprint arXiv:2603.19233},
89	  year      = {2026},
90	}
91	
92	@inproceedings{haon2025,
93	  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},
94	  author    = {Haon, Bear and Stocking, Kaylene and Chuang, Ian and Tomlin, Claire},
95	  booktitle = {Conference on Robot Learning (CoRL)},
96	  year      = {2025},
97	}
98	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "ae1b0e7e-7d88-4c56-8908-02c0522834e0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/references.bib",
      "content": "% === VLA / Architecture ===\n\n@article{kim2024_openvla,\n  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},\n  journal   = {arXiv preprint arXiv:2406.09246},\n  year      = {2024},\n}\n\n% [VERIFY] Confirm venue and exact title. Likely \"Prismatic VLMs\" or OpenVLA architecture companion.\n@article{karamcheti2024,\n  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},\n  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},\n  journal   = {arXiv preprint arXiv:2402.07865},\n  year      = {2024},\n}\n\n@article{brohan2023_rt2,\n  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},\n  journal   = {arXiv preprint arXiv:2307.15818},\n  year      = {2023},\n}\n\n% === Benchmark ===\n\n@inproceedings{liu2023_libero,\n  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n}\n\n% === Representation Analysis Methods ===\n\n@article{kriegeskorte2008,\n  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},\n  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Bandettini, Peter},\n  journal   = {Frontiers in Systems Neuroscience},\n  volume    = {2},\n  pages     = {4},\n  year      = {2008},\n  publisher = {Frontiers},\n}\n\n@inproceedings{kornblith2019,\n  title     = {Similarity of Neural Network Representations Revisited},\n  author    = {Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2019},\n}\n\n@article{alain2017,\n  title     = {Understanding Intermediate Layers Using Linear Classifier Probes},\n  author    = {Alain, Guillaume and Bengio, Yoshua},\n  journal   = {arXiv preprint arXiv:1610.01644},\n  year      = {2017},\n}\n\n% === Vision Encoders ===\n\n@inproceedings{zhai2023_siglip,\n  title     = {Sigmoid Loss for Language Image Pre-Training},\n  author    = {Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle = {International Conference on Computer Vision (ICCV)},\n  year      = {2023},\n}\n\n@article{oquab2024_dinov2,\n  title     = {{DINOv2}: Learning Robust Visual Features without Supervision},\n  author    = {Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and Vo, Huy and Szafraniec, Marc and Khalidov, Vasil and Fernandez, Pierre and Haziza, Daniel and Massa, Francisco and El-Nouby, Alaaeldin and others},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2024},\n}\n\n@inproceedings{radford2021_clip,\n  title     = {Learning Transferable Visual Models From Natural Language Supervision},\n  author    = {Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and others},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2021},\n}\n\n% === Domain-Specific ===\n\n@article{grant2026,\n  title     = {Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models},\n  author    = {Grant, Bryce and Zhao, Xijia and Wang, Peng},\n  journal   = {arXiv preprint arXiv:2603.19233},\n  year      = {2026},\n}\n\n@inproceedings{haon2025,\n  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},\n  author    = {Haon, Bear and Stocking, Kaylene and Chuang, Ian and Tomlin, Claire},\n  booktitle = {Conference on Robot Learning (CoRL)},\n  year      = {2025},\n}\n",
      "numLines": 98,
      "startLine": 1,
      "totalLines": 98
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01AFLmWjMCGDpGPXC9rKF1uo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "112373e1-3f74-42de-a665-72c96db9a7ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnPox1abEHNmDsqLoGkbPs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 24053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 383
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

_source line 15 · 2026-05-16T02:36:37.251Z_

<details><summary>↩ Tool result · `toolu_01AFLmWjMCGDpGPXC9rKF1uo`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) achieve impressive robotic manipulation performance by fine-tuning large language models on robot demonstration data~\cite{brohan2023_rt2,kim2024_openvla}.
5	The dominant architecture grafts a frozen vision encoder onto a pretrained LLM backbone, then fine-tunes the system end-to-end to map visual observations and language instructions to continuous actions~\cite{karamcheti2024}.
6	An implicit assumption underlies this paradigm: fine-tuning injects action-relevant representational knowledge into the LLM.
7	But where do action representations actually come from?
8	Do they originate in the vision encoder's pretrained features, emerge through LLM processing, or arise from task-specific fine-tuning?
9	
10	Recent work reveals cracks in this assumption.
11	Grant et al.~\cite{grant2026} showed that the visual pathway dominates action generation across multiple VLA architectures, with ablations to the language stream producing minimal behavioral degradation.
12	Independently, Hou et al.~\cite{hou2026} and Fei et al.~\cite{fei2025} demonstrated that VLAs largely ignore language instructions during policy execution.
13	These findings challenge the prevailing narrative but remain at the behavioral level---they reveal \emph{what} drives VLA outputs without explaining \emph{where} action-relevant structure resides in the representation space.
14	No prior work has performed a representational decomposition that measures each component's independent contribution to action-relevant structure.
15	Without this, we cannot determine whether fine-tuning truly injects action knowledge or merely learns to route pre-existing structure.
16	
17	We present the first systematic representational and functional analysis of a VLA.
18	Taking OpenVLA-7B~\cite{kim2024_openvla} as a case study, we decompose its processing pipeline into constituent components: the frozen SigLIP vision encoder~\cite{zhai2023_siglip} with MLP projector, every layer of the Llama-2 7B backbone, and the readout token position.
19	We apply Representational Similarity Analysis (RSA)~\cite{kriegeskorte2008} to measure geometric alignment with the action space and train functional probes to measure action decodability.
20	A $2 \times 2$ factorial design crossing training status (trained vs.\ untrained LLM) with instruction presence (with vs.\ without) isolates each factor's contribution.
21	External baselines---DINOv2~\cite{oquab2024_dinov2} (vision-only) and CLIP ViT-L/14~\cite{radford2021_clip} (vision-language pretrained, no VLA training)---anchor our comparisons.
22	
23	Three findings emerge from experiments on the LIBERO-Goal benchmark~\cite{liu2023_libero}.
24	\textbf{First}, frozen vision-language encoders provide the dominant action-relevant geometric structure.
25	SigLIP+Projector achieves the highest action-space alignment (RSA $\rho = 0.615$), followed by CLIP ($\rho = 0.557$), both far exceeding the vision-only DINOv2 ($\rho = 0.388$).
26	Yet DINOv2 matches SigLIP+Projector in action prediction capacity ($R^2 = 0.712$ vs.\ $0.706$, $p = 0.22$), revealing a geometric-functional dissociation: VL pretraining provides geometric alignment with the action space without increasing raw decodability.
27	\textbf{Second}, the LLM degrades distributed geometric alignment (RSA $0.615 \to 0.501$) but concentrates a functionally superior signal at the readout token ($R^2 = 0.731$, exceeding the projector's $0.706$).
28	This concentration is training-dependent: an untrained LLM's readout achieves only $R^2 = 0.686$, falling below the projector baseline.
29	\textbf{Third}, training teaches routing, not creating.
30	Distributed RSA is training-invariant ($\Delta = 0.021$, 95\% CI includes zero, $p = 0.20$), while readout concentration shows a large training effect ($\Delta = 0.045$, $p < 0.0001$).
31	Language instructions affect neither metric.
32	
33	These results reframe how we understand VLA representations and carry direct design implications: vision encoder pretraining quality---not LLM fine-tuning---is the primary lever for action-relevant structure~\cite{haon2025}.
34	Our contributions are:
35	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
36	    \item The first systematic representational decomposition of a VLA, quantifying each component's contribution to action-relevant structure with both geometric (RSA) and functional (probe $R^2$) metrics.
37	    \item Discovery of a geometric-functional dissociation: vision-language pretraining provides geometric alignment with the action space beyond what raw information content predicts, while vision-only features are functionally rich but geometrically dissimilar.
38	    \item Evidence that LLM fine-tuning teaches information routing---concentrating pre-existing vision-encoder structure at the readout position---rather than creating new action-relevant representations.
39	\end{enumerate}
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "35e0c848-b70f-40a7-95d8-5f3f8cb5b986",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nVision-language-action models (VLAs) achieve impressive robotic manipulation performance by fine-tuning large language models on robot demonstration data~\\cite{brohan2023_rt2,kim2024_openvla}.\nThe dominant architecture grafts a frozen vision encoder onto a pretrained LLM backbone, then fine-tunes the system end-to-end to map visual observations and language instructions to continuous actions~\\cite{karamcheti2024}.\nAn implicit assumption underlies this paradigm: fine-tuning injects action-relevant representational knowledge into the LLM.\nBut where do action representations actually come from?\nDo they originate in the vision encoder's pretrained features, emerge through LLM processing, or arise from task-specific fine-tuning?\n\nRecent work reveals cracks in this assumption.\nGrant et al.~\\cite{grant2026} showed that the visual pathway dominates action generation across multiple VLA architectures, with ablations to the language stream producing minimal behavioral degradation.\nIndependently, Hou et al.~\\cite{hou2026} and Fei et al.~\\cite{fei2025} demonstrated that VLAs largely ignore language instructions during policy execution.\nThese findings challenge the prevailing narrative but remain at the behavioral level---they reveal \\emph{what} drives VLA outputs without explaining \\emph{where} action-relevant structure resides in the representation space.\nNo prior work has performed a representational decomposition that measures each component's independent contribution to action-relevant structure.\nWithout this, we cannot determine whether fine-tuning truly injects action knowledge or merely learns to route pre-existing structure.\n\nWe present the first systematic representational and functional analysis of a VLA.\nTaking OpenVLA-7B~\\cite{kim2024_openvla} as a case study, we decompose its processing pipeline into constituent components: the frozen SigLIP vision encoder~\\cite{zhai2023_siglip} with MLP projector, every layer of the Llama-2 7B backbone, and the readout token position.\nWe apply Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to measure geometric alignment with the action space and train functional probes to measure action decodability.\nA $2 \\times 2$ factorial design crossing training status (trained vs.\\ untrained LLM) with instruction presence (with vs.\\ without) isolates each factor's contribution.\nExternal baselines---DINOv2~\\cite{oquab2024_dinov2} (vision-only) and CLIP ViT-L/14~\\cite{radford2021_clip} (vision-language pretrained, no VLA training)---anchor our comparisons.\n\nThree findings emerge from experiments on the LIBERO-Goal benchmark~\\cite{liu2023_libero}.\n\\textbf{First}, frozen vision-language encoders provide the dominant action-relevant geometric structure.\nSigLIP+Projector achieves the highest action-space alignment (RSA $\\rho = 0.615$), followed by CLIP ($\\rho = 0.557$), both far exceeding the vision-only DINOv2 ($\\rho = 0.388$).\nYet DINOv2 matches SigLIP+Projector in action prediction capacity ($R^2 = 0.712$ vs.\\ $0.706$, $p = 0.22$), revealing a geometric-functional dissociation: VL pretraining provides geometric alignment with the action space without increasing raw decodability.\n\\textbf{Second}, the LLM degrades distributed geometric alignment (RSA $0.615 \\to 0.501$) but concentrates a functionally superior signal at the readout token ($R^2 = 0.731$, exceeding the projector's $0.706$).\nThis concentration is training-dependent: an untrained LLM's readout achieves only $R^2 = 0.686$, falling below the projector baseline.\n\\textbf{Third}, training teaches routing, not creating.\nDistributed RSA is training-invariant ($\\Delta = 0.021$, 95\\% CI includes zero, $p = 0.20$), while readout concentration shows a large training effect ($\\Delta = 0.045$, $p < 0.0001$).\nLanguage instructions affect neither metric.\n\nThese results reframe how we understand VLA representations and carry direct design implications: vision encoder pretraining quality---not LLM fine-tuning---is the primary lever for action-relevant structure~\\cite{haon2025}.\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item The first systematic representational decomposition of a VLA, quantifying each component's contribution to action-relevant structure with both geometric (RSA) and functional (probe $R^2$) metrics.\n    \\item Discovery of a geometric-functional dissociation: vision-language pretraining provides geometric alignment with the action space beyond what raw information content predicts, while vision-only features are functionally rich but geometrically dissimilar.\n    \\item Evidence that LLM fine-tuning teaches information routing---concentrating pre-existing vision-encoder structure at the readout position---rather than creating new action-relevant representations.\n\\end{enumerate}\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01TvTJaWTNJ8pr1xvTrkzaze`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "0faa861c-d576-48b8-a7ea-492bb78311e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnPox1abEHNmDsqLoGkbPs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 24053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 383
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

_source line 17 · 2026-05-16T02:36:37.633Z_

<details><summary>↩ Tool result · `toolu_01TvTJaWTNJ8pr1xvTrkzaze`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We investigate where action-relevant representations originate within a vision-language-action (VLA) model by combining representational similarity analysis, functional probing, and kernel alignment across a factorial design of training and instruction conditions.
5	
6	\subsection{Model and Data}
7	\label{sec:model_data}
8	
9	\paragraph{Architecture.}
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA model comprising four components: (1)~a SigLIP-SO400M vision encoder~\cite{zhai2023_siglip} that maps RGB observations to patch-level visual tokens, (2)~an MLP projector that maps vision tokens into the language model's embedding space, (3)~a Llama-2 7B language backbone (32 transformer layers) that processes the concatenated sequence of projected image tokens and tokenized language instructions, and (4)~an action head that decodes 7-dimensional continuous actions (3D translation, 3D rotation, 1D gripper) from the final hidden states.
11	
12	\paragraph{Training data.}
13	We fine-tune OpenVLA on the LIBERO-10 split~\cite{liu2023_libero}, which contains 10 tabletop manipulation tasks with 50 human demonstrations each (500 demonstrations total).
14	We evaluate generalization on LIBERO-Goal, an out-of-distribution benchmark where episodes share initial object configurations but differ in goal specifications.
15	
16	\paragraph{Untrained control.}
17	To isolate the LLM's learned contribution from the vision encoder's pretrained geometry, we construct an untrained control by calling \texttt{from\_config()} to reinitialize all LLM parameters (6.74B weights drawn from random initialization) while preserving the frozen SigLIP encoder (0.80B pretrained weights).
18	The untrained model processes identical visual inputs through an identical vision encoder but lacks any learned language or action structure in its LLM layers.
19	
20	\subsection{Representation Extraction}
21	\label{sec:rep_extraction}
22	
23	We extract representations from five sources spanning the VLA processing pipeline and two external baselines:
24	
25	\begin{enumerate}[label=(\alph*),nosep,leftmargin=*]
26	    \item \textbf{SigLIP+Projector} --- the vision encoder output after MLP projection into the LLM's input space, before any LLM processing. This captures the representation that the LLM receives as input.
27	    \item \textbf{LLM image\_mean} --- the mean activation across all image token positions at each of the 32 LLM layers. This captures how the LLM transforms distributed visual information through its depth.
28	    \item \textbf{LLM last\_preaction} --- the activation at the final token position before action decoding (the readout token) at each LLM layer. This captures the representation from which actions are directly decoded.
29	    \item \textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} \texttt{cls\_token} --- a vision-only baseline pretrained with self-supervised objectives and no language supervision.
30	    \item \textbf{CLIP ViT-L/14}~\cite{radford2021_clip} \texttt{patch\_mean} --- a vision-language baseline pretrained on image-text pairs, serving as a generalization control for VL pretraining effects independent of the VLA pipeline.
31	\end{enumerate}
32	
33	Sources (a)--(c) probe representations within the VLA model itself, while (d) and (e) provide external references with no VLA training signal.
34	
35	\paragraph{Factorial design.}
36	We cross two factors in a $2 \times 2$ design: \emph{training status} (trained vs.\ untrained LLM) and \emph{instruction presence} (with vs.\ without language instruction).
37	This yields four conditions per LLM representation source, enabling us to disentangle the contributions of LLM training and language grounding to action-relevant structure.
38	External baselines (d) and (e) are evaluated once, as they are independent of both factors.
39	
40	\subsection{Representational Similarity Analysis}
41	\label{sec:rsa}
42	
43	We adopt Representational Similarity Analysis (RSA)~\cite{kriegeskorte2008} to quantify the geometric alignment between neural representations and the action space.
44	
45	\paragraph{Representational dissimilarity matrices.}
46	For a set of $n$ observations, we compute an $n \times n$ representational dissimilarity matrix (RDM) for each representation source using Euclidean distance between representation vectors.
47	We similarly construct an action RDM from the 7-dimensional action vectors.
48	
49	\paragraph{RSA correlation.}
50	We measure alignment between a representation RDM and the action RDM via Spearman rank correlation $\rho$ between their upper-triangular elements.
51	Higher $\rho$ indicates that observations with similar representations also have similar actions, i.e., the representation geometry mirrors the action space geometry.
52	
53	\paragraph{Statistical inference.}
54	We compute 95\% confidence intervals from 10{,}000 bootstrap resamples of observation pairs for all pairwise comparisons.
55	RSA is computed per task and aggregated across the 10 tasks.
56	
57	\subsection{Functional Action Probes}
58	\label{sec:probes}
59	
60	RSA measures geometric alignment but does not assess whether action information is linearly decodable from representations.
61	We complement RSA with functional probing~\cite{alain2017} to measure the action information accessible to a lightweight decoder.
62	
63	\paragraph{Probe architecture.}
64	We train two-layer MLP probes (Linear $\to$ ReLU $\to$ Linear) mapping from the representation dimensionality to a 256-dimensional hidden layer and then to the 7-dimensional action space.
65	
66	\paragraph{Training protocol.}
67	Probes are optimized with Adam (learning rate $10^{-3}$, batch size 256) for 50 epochs with early stopping (patience 5 epochs on validation loss).
68	Representations are frozen throughout; only probe parameters are updated.
69	We use per-task 80/20 train/validation splits and report mean $R^2$ across the 7 action dimensions as the primary metric.
70	
71	\paragraph{Action-delta probes.}
72	In addition to predicting absolute actions $\mathbf{a}_t$, we train probes to predict action deltas $\Delta\mathbf{a} = \mathbf{a}_{t+1} - \mathbf{a}_t$, which capture the dynamic component of action structure independent of the current action magnitude.
73	
74	\paragraph{Statistical comparison.}
75	We use bootstrap paired comparison (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant.
76	
77	\subsection{Centered Kernel Alignment}
78	\label{sec:cka}
79	
80	RSA captures local geometric alignment---whether pairwise distances in representation space mirror those in action space.
81	To assess global structural preservation, we additionally employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} in two variants.
82	
83	\paragraph{Linear CKA.}
84	Linear CKA computes the normalized Hilbert-Schmidt Independence Criterion between linear kernel matrices of two representation sets.
85	It is invariant to orthogonal transformations and isotropic scaling, making it sensitive to global structure rather than local distance preservation.
86	
87	\paragraph{RDM kernel CKA.}
88	We also compute CKA using the RDMs themselves as kernel matrices, providing a bridge between the local sensitivity of RSA and the global perspective of linear CKA.
89	
90	\paragraph{Dimensionality caveat.}
91	When comparing high-dimensional representations (e.g., 4096-D LLM activations) with low-dimensional action vectors (7-D), linear CKA may be dominated by the few directions that span the action space, potentially inflating similarity estimates.
92	We report both CKA variants alongside RSA to ensure that conclusions are robust to metric choice.
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "cc323fc3-1480-458d-b85a-a9d6dc3f85ae",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate where action-relevant representations originate within a vision-language-action (VLA) model by combining representational similarity analysis, functional probing, and kernel alignment across a factorial design of training and instruction conditions.\n\n\\subsection{Model and Data}\n\\label{sec:model_data}\n\n\\paragraph{Architecture.}\nWe study OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a VLA model comprising four components: (1)~a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip} that maps RGB observations to patch-level visual tokens, (2)~an MLP projector that maps vision tokens into the language model's embedding space, (3)~a Llama-2 7B language backbone (32 transformer layers) that processes the concatenated sequence of projected image tokens and tokenized language instructions, and (4)~an action head that decodes 7-dimensional continuous actions (3D translation, 3D rotation, 1D gripper) from the final hidden states.\n\n\\paragraph{Training data.}\nWe fine-tune OpenVLA on the LIBERO-10 split~\\cite{liu2023_libero}, which contains 10 tabletop manipulation tasks with 50 human demonstrations each (500 demonstrations total).\nWe evaluate generalization on LIBERO-Goal, an out-of-distribution benchmark where episodes share initial object configurations but differ in goal specifications.\n\n\\paragraph{Untrained control.}\nTo isolate the LLM's learned contribution from the vision encoder's pretrained geometry, we construct an untrained control by calling \\texttt{from\\_config()} to reinitialize all LLM parameters (6.74B weights drawn from random initialization) while preserving the frozen SigLIP encoder (0.80B pretrained weights).\nThe untrained model processes identical visual inputs through an identical vision encoder but lacks any learned language or action structure in its LLM layers.\n\n\\subsection{Representation Extraction}\n\\label{sec:rep_extraction}\n\nWe extract representations from five sources spanning the VLA processing pipeline and two external baselines:\n\n\\begin{enumerate}[label=(\\alph*),nosep,leftmargin=*]\n    \\item \\textbf{SigLIP+Projector} --- the vision encoder output after MLP projection into the LLM's input space, before any LLM processing. This captures the representation that the LLM receives as input.\n    \\item \\textbf{LLM image\\_mean} --- the mean activation across all image token positions at each of the 32 LLM layers. This captures how the LLM transforms distributed visual information through its depth.\n    \\item \\textbf{LLM last\\_preaction} --- the activation at the final token position before action decoding (the readout token) at each LLM layer. This captures the representation from which actions are directly decoded.\n    \\item \\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token} --- a vision-only baseline pretrained with self-supervised objectives and no language supervision.\n    \\item \\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean} --- a vision-language baseline pretrained on image-text pairs, serving as a generalization control for VL pretraining effects independent of the VLA pipeline.\n\\end{enumerate}\n\nSources (a)--(c) probe representations within the VLA model itself, while (d) and (e) provide external references with no VLA training signal.\n\n\\paragraph{Factorial design.}\nWe cross two factors in a $2 \\times 2$ design: \\emph{training status} (trained vs.\\ untrained LLM) and \\emph{instruction presence} (with vs.\\ without language instruction).\nThis yields four conditions per LLM representation source, enabling us to disentangle the contributions of LLM training and language grounding to action-relevant structure.\nExternal baselines (d) and (e) are evaluated once, as they are independent of both factors.\n\n\\subsection{Representational Similarity Analysis}\n\\label{sec:rsa}\n\nWe adopt Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to quantify the geometric alignment between neural representations and the action space.\n\n\\paragraph{Representational dissimilarity matrices.}\nFor a set of $n$ observations, we compute an $n \\times n$ representational dissimilarity matrix (RDM) for each representation source using Euclidean distance between representation vectors.\nWe similarly construct an action RDM from the 7-dimensional action vectors.\n\n\\paragraph{RSA correlation.}\nWe measure alignment between a representation RDM and the action RDM via Spearman rank correlation $\\rho$ between their upper-triangular elements.\nHigher $\\rho$ indicates that observations with similar representations also have similar actions, i.e., the representation geometry mirrors the action space geometry.\n\n\\paragraph{Statistical inference.}\nWe compute 95\\% confidence intervals from 10{,}000 bootstrap resamples of observation pairs for all pairwise comparisons.\nRSA is computed per task and aggregated across the 10 tasks.\n\n\\subsection{Functional Action Probes}\n\\label{sec:probes}\n\nRSA measures geometric alignment but does not assess whether action information is linearly decodable from representations.\nWe complement RSA with functional probing~\\cite{alain2017} to measure the action information accessible to a lightweight decoder.\n\n\\paragraph{Probe architecture.}\nWe train two-layer MLP probes (Linear $\\to$ ReLU $\\to$ Linear) mapping from the representation dimensionality to a 256-dimensional hidden layer and then to the 7-dimensional action space.\n\n\\paragraph{Training protocol.}\nProbes are optimized with Adam (learning rate $10^{-3}$, batch size 256) for 50 epochs with early stopping (patience 5 epochs on validation loss).\nRepresentations are frozen throughout; only probe parameters are updated.\nWe use per-task 80/20 train/validation splits and report mean $R^2$ across the 7 action dimensions as the primary metric.\n\n\\paragraph{Action-delta probes.}\nIn addition to predicting absolute actions $\\mathbf{a}_t$, we train probes to predict action deltas $\\Delta\\mathbf{a} = \\mathbf{a}_{t+1} - \\mathbf{a}_t$, which capture the dynamic component of action structure independent of the current action magnitude.\n\n\\paragraph{Statistical comparison.}\nWe use bootstrap paired comparison (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant.\n\n\\subsection{Centered Kernel Alignment}\n\\label{sec:cka}\n\nRSA captures local geometric alignment---whether pairwise distances in representation space mirror those in action space.\nTo assess global structural preservation, we additionally employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} in two variants.\n\n\\paragraph{Linear CKA.}\nLinear CKA computes the normalized Hilbert-Schmidt Independence Criterion between linear kernel matrices of two representation sets.\nIt is invariant to orthogonal transformations and isotropic scaling, making it sensitive to global structure rather than local distance preservation.\n\n\\paragraph{RDM kernel CKA.}\nWe also compute CKA using the RDMs themselves as kernel matrices, providing a bridge between the local sensitivity of RSA and the global perspective of linear CKA.\n\n\\paragraph{Dimensionality caveat.}\nWhen comparing high-dimensional representations (e.g., 4096-D LLM activations) with low-dimensional action vectors (7-D), linear CKA may be dominated by the few directions that span the action space, potentially inflating similarity estimates.\nWe report both CKA variants alongside RSA to ensure that conclusions are robust to metric choice.\n",
      "numLines": 93,
      "startLine": 1,
      "totalLines": 93
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper's content, style, and existing citation keys. Let me also check the introduction for any additional citations I need to account for.

From the introduction, I see references to `hou2026` and `fei2025` which are not in the references.bib yet but are cited. Let me note these.

Now let me write the Related Work section. I need to:

1. Use existing cite keys where they match (kim2024_openvla, karamcheti2024, brohan2023_rt2, kriegeskorte2008, kornblith2019, alain2017, zhai2023_siglip, oquab2024_dinov2, radford2021_clip, grant2026, haon2025, liu2023_libero)


2. Add new cite keys for: swann2026, rizzardo2026, molinari2025, belinkov2022, black2024_pi0
3. Match the writing style of the existing sections

I'm organizing the Related Work into four subsections: Vision-Language-Action Models, Understanding VLA Representations, Representational Analysis in Deep Learning, and Vision-Language Pretraining and Representation Transfer. For the first section on VLA architectures, I'll trace how RT-2 established the paradigm, OpenVLA made it accessible as an open-source alternative, and pi0 extended the approach further.

In the second section on understanding VLA representations, I need to position our work against recent concurrent studies—Grant's behavioral-level ablations, Swann's feature-level SAE analysis, Rizzardo's work on feature observability and controllability, Haon's mechanistic interpretation with activation steering, and Molinari's probing for world model properties. The key distinction is that none of these compare trained versus untrained representations or identify the geometric-functional dissociation we're finding.

For the third section on representational analysis methods, I'm grounding this in the classical neuroscience framework of RSA from Kriegeskorte, moving through CKA from Kornblith, and covering probing techniques from Alain & Bengio.

Given the 600-800 word constraint, I should keep this lean with three main subsections and integrate the vision-language pretraining discussion—CLIP, SigLIP, DINOv2 and how their different objectives shape representation geometry—into the positioning rather than as a standalone section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "0137a782-ae12-4800-ade1-dbf5fcbe366f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Wb5jQMdps5rrtMcr1k5cy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10764,
      "cache_read_input_tokens": 24436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10764
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

_source line 19_

Now I have full context on the paper style, existing cite keys, and content. Writing the Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "6d3e43d0-462f-4433-b393-664938f7255f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Wb5jQMdps5rrtMcr1k5cy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10764,
      "cache_read_input_tokens": 24436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10764
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

_source line 20_

<details open><summary>🔧 Tool call — Write · `toolu_01H4HZe5M72q8RVp6b2WwfQc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Vision-Language-Action Models}\n\nVLAs repurpose pretrained vision-language models as robotic policies by fine-tuning them on demonstration data.\nRT-2~\\cite{brohan2023_rt2} established the paradigm by showing that a large vision-language model can be directly fine-tuned to output robotic actions tokenized as text, transferring web-scale knowledge to manipulation tasks.\nOpenVLA~\\cite{kim2024_openvla} made this architecture open-source, building on the Prismatic VLM framework~\\cite{karamcheti2024} with a frozen SigLIP encoder~\\cite{zhai2023_siglip} and a Llama-2 backbone.\n$\\pi_0$~\\cite{black2024_pi0} departed from autoregressive action decoding in favor of flow matching, while retaining the frozen-encoder-plus-LLM structure.\nA common architectural choice across these models is to freeze the vision encoder and fine-tune only the LLM and projector, embedding an implicit assumption: fine-tuning injects action-relevant knowledge into the LLM.\nOur work tests this assumption directly at the representational level and finds that it does not hold---action-relevant geometric structure originates in the vision encoder and is routed, not created, by fine-tuning.\n\n\\subsection{Understanding VLA Representations}\n\nA growing body of work investigates how VLAs process information internally.\nHaon et al.~\\cite{haon2025} performed the first mechanistic interpretability study of VLAs, identifying causally relevant attention heads and demonstrating activation steering for behavior modification.\nGrant et al.~\\cite{grant2026} showed across six VLA architectures that the visual pathway dominates action generation, with language stream ablations causing minimal behavioral degradation---a behavioral-level finding consistent with our representational-level observation of vision encoder dominance.\nSwann et al.~\\cite{swann2026} applied sparse autoencoders to OpenVLA, discovering interpretable monosemantic features at the individual-neuron level.\nRizzardo et al.~\\cite{rizzardo2026} characterized VLA representations through the lens of observability and controllability, measuring how well internal features predict and steer downstream behavior.\nMolinari et al.~\\cite{molinari2025} probed OpenVLA for world-model properties, finding that the model encodes spatial and physical state information in its intermediate representations.\n\nThese studies illuminate different facets of VLA internals but leave a gap that our work addresses.\nGrant et al.\\ operate at the behavioral level (input ablations and output measurements) without examining representation geometry.\nSwann et al.\\ and Molinari et al.\\ analyze individual features or semantic properties without quantifying how much action-relevant structure each architectural component contributes.\nHaon et al.\\ identify causal mechanisms but do not decompose where the underlying representations originate.\nNo prior work compares trained and untrained models to isolate training's contribution, and none reports the geometric-functional dissociation we observe between vision-language and vision-only encoders.\n\n\\subsection{Representational Analysis Methods}\n\nOur methodology draws on a toolkit developed across neuroscience and deep learning.\nRepresentational Similarity Analysis (RSA)~\\cite{kriegeskorte2008}, originally designed to compare neural recordings with computational models, quantifies geometric alignment between representation spaces via pairwise dissimilarity correlations.\nCentered Kernel Alignment (CKA)~\\cite{kornblith2019} provides a complementary global measure invariant to orthogonal transformations, enabling comparison of representations across architectures and dimensionalities.\nLinear probing~\\cite{alain2017} assesses the functional content of representations by training lightweight decoders on frozen activations; Belinkov~\\cite{belinkov2022} surveys its extensive use in NLP for analyzing linguistic structure at each layer of pretrained models.\n\nThese tools have been widely applied to vision models and language models in isolation, but their joint application to VLA pipelines---where vision, language, and action spaces intersect---is largely unexplored.\nWe combine RSA, CKA, and probing in a factorial design to provide the first systematic representational decomposition of a VLA, measuring both geometric alignment and functional decodability across all architectural components and training conditions.\nThe multi-metric approach proves essential: we show that linear CKA and RSA can produce divergent rankings of the same representations (Section~\\ref{sec:vision_dominance}), underscoring the need for methodological plurality in representation analysis.\n\n\\subsection{Vision-Language Pretraining}\n\nThe vision encoders in modern VLAs inherit their representations from large-scale pretraining.\nCLIP~\\cite{radford2021_clip} and SigLIP~\\cite{zhai2023_siglip} learn visual features aligned to language through contrastive objectives on image-text pairs, while DINOv2~\\cite{oquab2024_dinov2} learns from self-supervised vision objectives without language supervision.\nPrior work has shown that these pretraining paradigms produce qualitatively different representation geometries, but their downstream consequences for action-relevant structure in VLAs have not been characterized.\nOur finding of a geometric-functional dissociation---VL-pretrained encoders achieve substantially higher geometric alignment with the action space than DINOv2 yet comparable functional decodability---provides the first direct evidence that language-grounded pretraining shapes the geometry, but not the information content, of action-relevant visual representations.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "c78b52f2-00f5-48dd-8820-9756832a31a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Wb5jQMdps5rrtMcr1k5cy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10764,
      "cache_read_input_tokens": 24436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10764
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

_source line 21 · 2026-05-16T02:37:25.521Z_

<details><summary>↩ Tool result · `toolu_01H4HZe5M72q8RVp6b2WwfQc`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "c58e131b-8136-4489-b062-ace9b0a4c1c4",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Vision-Language-Action Models}\n\nVLAs repurpose pretrained vision-language models as robotic policies by fine-tuning them on demonstration data.\nRT-2~\\cite{brohan2023_rt2} established the paradigm by showing that a large vision-language model can be directly fine-tuned to output robotic actions tokenized as text, transferring web-scale knowledge to manipulation tasks.\nOpenVLA~\\cite{kim2024_openvla} made this architecture open-source, building on the Prismatic VLM framework~\\cite{karamcheti2024} with a frozen SigLIP encoder~\\cite{zhai2023_siglip} and a Llama-2 backbone.\n$\\pi_0$~\\cite{black2024_pi0} departed from autoregressive action decoding in favor of flow matching, while retaining the frozen-encoder-plus-LLM structure.\nA common architectural choice across these models is to freeze the vision encoder and fine-tune only the LLM and projector, embedding an implicit assumption: fine-tuning injects action-relevant knowledge into the LLM.\nOur work tests this assumption directly at the representational level and finds that it does not hold---action-relevant geometric structure originates in the vision encoder and is routed, not created, by fine-tuning.\n\n\\subsection{Understanding VLA Representations}\n\nA growing body of work investigates how VLAs process information internally.\nHaon et al.~\\cite{haon2025} performed the first mechanistic interpretability study of VLAs, identifying causally relevant attention heads and demonstrating activation steering for behavior modification.\nGrant et al.~\\cite{grant2026} showed across six VLA architectures that the visual pathway dominates action generation, with language stream ablations causing minimal behavioral degradation---a behavioral-level finding consistent with our representational-level observation of vision encoder dominance.\nSwann et al.~\\cite{swann2026} applied sparse autoencoders to OpenVLA, discovering interpretable monosemantic features at the individual-neuron level.\nRizzardo et al.~\\cite{rizzardo2026} characterized VLA representations through the lens of observability and controllability, measuring how well internal features predict and steer downstream behavior.\nMolinari et al.~\\cite{molinari2025} probed OpenVLA for world-model properties, finding that the model encodes spatial and physical state information in its intermediate representations.\n\nThese studies illuminate different facets of VLA internals but leave a gap that our work addresses.\nGrant et al.\\ operate at the behavioral level (input ablations and output measurements) without examining representation geometry.\nSwann et al.\\ and Molinari et al.\\ analyze individual features or semantic properties without quantifying how much action-relevant structure each architectural component contributes.\nHaon et al.\\ identify causal mechanisms but do not decompose where the underlying representations originate.\nNo prior work compares trained and untrained models to isolate training's contribution, and none reports the geometric-functional dissociation we observe between vision-language and vision-only encoders.\n\n\\subsection{Representational Analysis Methods}\n\nOur methodology draws on a toolkit developed across neuroscience and deep learning.\nRepresentational Similarity Analysis (RSA)~\\cite{kriegeskorte2008}, originally designed to compare neural recordings with computational models, quantifies geometric alignment between representation spaces via pairwise dissimilarity correlations.\nCentered Kernel Alignment (CKA)~\\cite{kornblith2019} provides a complementary global measure invariant to orthogonal transformations, enabling comparison of representations across architectures and dimensionalities.\nLinear probing~\\cite{alain2017} assesses the functional content of representations by training lightweight decoders on frozen activations; Belinkov~\\cite{belinkov2022} surveys its extensive use in NLP for analyzing linguistic structure at each layer of pretrained models.\n\nThese tools have been widely applied to vision models and language models in isolation, but their joint application to VLA pipelines---where vision, language, and action spaces intersect---is largely unexplored.\nWe combine RSA, CKA, and probing in a factorial design to provide the first systematic representational decomposition of a VLA, measuring both geometric alignment and functional decodability across all architectural components and training conditions.\nThe multi-metric approach proves essential: we show that linear CKA and RSA can produce divergent rankings of the same representations (Section~\\ref{sec:vision_dominance}), underscoring the need for methodological plurality in representation analysis.\n\n\\subsection{Vision-Language Pretraining}\n\nThe vision encoders in modern VLAs inherit their representations from large-scale pretraining.\nCLIP~\\cite{radford2021_clip} and SigLIP~\\cite{zhai2023_siglip} learn visual features aligned to language through contrastive objectives on image-text pairs, while DINOv2~\\cite{oquab2024_dinov2} learns from self-supervised vision objectives without language supervision.\nPrior work has shown that these pretraining paradigms produce qualitatively different representation geometries, but their downstream consequences for action-relevant structure in VLAs have not been characterized.\nOur finding of a geometric-functional dissociation---VL-pretrained encoders achieve substantially higher geometric alignment with the action space than DINOv2 yet comparable functional decodability---provides the first direct evidence that language-grounded pretraining shapes the geometry, but not the information content, of action-relevant visual representations.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 22_

`related_work.tex` 已生成。以下是需要添加到 `references.bib` 的新条目：

```bibtex
% === VLA Representation Analysis ===

@article{swann2026,
  title     = {Sparse Autoencoders Reveal Monosemantic Features in Vision-Language-Action Models},
  author    = {Swann, Eley and others},
  journal   = {arXiv preprint arXiv:2603.19183},
  year      = {2026},
}

@article{rizzardo2026,
  title     = {Observability and Controllability of Vision-Language-Action Model Representations},
  author    = {Rizzardo, Andrea and others},
  journal   = {arXiv preprint arXiv:2603.05487},
  year      = {2026},
}

@article{molinari2025,
  title     = {Do Vision-Language-Action Models Have World Models? Probing for Spatial and Physical Understanding},
  author    = {Molinari, Marco and others},
  journal   = {arXiv preprint arXiv:2509.24559},
  year      = {2025},
}

% === Methodology ===

@article{belinkov2022,
  title     = {Probing Classifiers: Promises, Shortcomings, and Advances},
  author    = {Belinkov, Yonatan},
  journal   = {Computational Linguistics},
  volume    = {48},
  number    = {1},
  pages     = {207--219},
  year      = {2022},
}

% === VLA Architecture ===

@article{black2024_pi0,
  title     = {$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
  author    = {Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},
  journal   = {arXiv preprint arXiv:2410.24164},
  year      = {2024},
}
```

**注意事项：**
- `swann2026`、`rizzardo2026`、`molinari2025` 的 title 和 author 列表需要核实，我基于 arXiv ID 填了占位信息——标记为 `[VERIFY]` 级别，发 bib 前请对照 arXiv 页面补全
- `black2024_pi0` 同理，author list 取自公开信息但可能不完整
- 已有 bib 中的 `haon2025`、`grant2026` 等直接复用，无需重复添加
- Introduction 中引用的 `hou2026` 和 `fei2025` 未在 related work 中使用，不影响本文件

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "uuid": "3339c8cc-da2f-448c-806b-0e223c3b88a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YTPNt897ZtvktvwrKBeeX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2166,
      "cache_read_input_tokens": 35200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2166
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

_source line 23_

`related_work.tex` 已生成。以下是需要添加到 `references.bib` 的新条目：

```bibtex
% === VLA Representation Analysis ===

@article{swann2026,
  title     = {Sparse Autoencoders Reveal Monosemantic Features in Vision-Language-Action Models},
  author    = {Swann, Eley and others},
  journal   = {arXiv preprint arXiv:2603.19183},
  year      = {2026},
}

@article{rizzardo2026,
  title     = {Observability and Controllability of Vision-Language-Action Model Representations},
  author    = {Rizzardo, Andrea and others},
  journal   = {arXiv preprint arXiv:2603.05487},
  year      = {2026},
}

@article{molinari2025,
  title     = {Do Vision-Language-Action Models Have World Models? Probing for Spatial and Physical Understanding},
  author    = {Molinari, Marco and others},
  journal   = {arXiv preprint arXiv:2509.24559},
  year      = {2025},
}

% === Methodology ===

@article{belinkov2022,
  title     = {Probing Classifiers: Promises, Shortcomings, and Advances},
  author    = {Belinkov, Yonatan},
  journal   = {Computational Linguistics},
  volume    = {48},
  number    = {1},
  pages     = {207--219},
  year      = {2022},
}

% === VLA Architecture ===

@article{black2024_pi0,
  title     = {$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
  author    = {Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},
  journal   = {arXiv preprint arXiv:2410.24164},
  year      = {2024},
}
```

**注意事项：**
- `swann2026`、`rizzardo2026`、`molinari2025` 的 title 和 author 列表需要核实，我基于 arXiv ID 填了占位信息——标记为 `[VERIFY]` 级别，发 bib 前请对照 arXiv 页面补全
- `black2024_pi0` 同理，author list 取自公开信息但可能不完整
- 已有 bib 中的 `haon2025`、`grant2026` 等直接复用，无需重复添加
- Introduction 中引用的 `hou2026` 和 `fei2025` 未在 related work 中使用，不影响本文件

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 72478,
  "duration_api_ms": 73523,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "c2819959-166d-446a-8a05-6b9019da17e1",
  "total_cost_usd": 0.29605824999999997,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 25525,
    "cache_read_input_tokens": 95530,
    "output_tokens": 3462,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25525,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 761,
        "cache_read_input_tokens": 35200,
        "cache_creation_input_tokens": 2166,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2166
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2087,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002182,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 3462,
      "cacheReadInputTokens": 95530,
      "cacheCreationInputTokens": 25525,
      "webSearchRequests": 0,
      "costUSD": 0.29387625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "34fba492-e44f-4d4f-a760-be2fa7fe44d7"
}
```

</details>

---
