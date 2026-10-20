# paper writing introduction

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260516T022839.log`
- **Structured JSON:** [`a86885cd2e69f9e3b7d9.json`](../../sessions/a8/a86885cd2e69f9e3b7d9.json)

## Before a recorded user message

11 recorded events

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
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
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
  "uuid": "7349ab17-1413-487e-96da-296c8cd40b2a",
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
  "uuid": "d87ef977-51b1-4707-b5a9-a3a42964a498",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the existing experiments.tex and any other relevant paper files to understand the context and style, then write the introduction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "28ea8e87-3eac-4cb1-8286-4ce66b5d3ca8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DiQmfeQHojkctxpo4TR8dC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12599,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12599
      },
      "output_tokens": 30,
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

<details open><summary>🔧 Tool call — Read · `toolu_01EcFbgJNWPKQzVt6LNDchEe`</summary>

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
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "5412d8a9-eece-47a9-99bd-0ea1fa0614aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DiQmfeQHojkctxpo4TR8dC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12599,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12599
      },
      "output_tokens": 30,
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

_source line 6 · 2026-05-16T02:28:49.848Z_

<details><summary>↩ Tool result · `toolu_01EcFbgJNWPKQzVt6LNDchEe`</summary>

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
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "51341285-8c9c-4f49-b363-8efbc523cf4b",
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

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01CNo6iP7TwRqrYaXjMDmmdL`</summary>

```json
{
  "pattern": "*.tex",
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
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "df6e0068-cadd-4079-a34b-a9a372747b0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DiQmfeQHojkctxpo4TR8dC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12599,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12599
      },
      "output_tokens": 30,
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

_source line 8 · 2026-05-16T02:28:50.559Z_

<details><summary>↩ Tool result · `toolu_01CNo6iP7TwRqrYaXjMDmmdL`</summary>

```text
artifacts/_project/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "d9207f80-4862-41d5-b48c-b50fa503c5ac",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/experiments.tex"
    ],
    "durationMs": 30,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Let me also check for any existing paper_framing.md or other context files that might have additional numbers or framing guidance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "db53f844-75cd-4dd0-a110-d350e902b2b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TN9H4mFuuGfGzRM6zCntjF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5432,
      "cache_read_input_tokens": 24440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5432
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

_source line 10_

<details open><summary>🔧 Tool call — Agent · `toolu_01GU9V4Q4WDF22n3FYFv26oh`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find paper framing files",
  "prompt": "Search for paper_framing.md or any framing/story document in the vla-ssd project. Check paths like /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ and subdirectories. Also look for references.bib. Report file paths found and key content snippets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "c904fd05-5fc6-46cb-a51c-eca9884a2e29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TN9H4mFuuGfGzRM6zCntjF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5432,
      "cache_read_input_tokens": 24440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5432
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

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ad6f96e6818eb4afa",
  "tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "description": "Find paper framing files",
  "task_type": "local_agent",
  "prompt": "Search for paper_framing.md or any framing/story document in the vla-ssd project. Check paths like /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ and subdirectories. Also look for references.bib. Report file paths found and key content snippets.",
  "uuid": "b239509a-46ff-46ab-9722-b65610538982",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

## Round 1

53 recorded events

### User

_source line 12 · 2026-05-16T02:28:57.219Z_

Search for paper_framing.md or any framing/story document in the vla-ssd project. Check paths like /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ and subdirectories. Also look for references.bib. Report file paths found and key content snippets.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "ab632283-3fd1-4561-b99a-008eb61d98c8"
}
```

</details>

---

### System

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6f96e6818eb4afa",
  "tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "description": "Finding **/paper_framing.md",
  "usage": {
    "total_tokens": 17851,
    "tool_uses": 1,
    "duration_ms": 1485
  },
  "last_tool_name": "Glob",
  "uuid": "c251982e-32e3-4af3-ad21-e2dc75205e1e",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_01NDAn27pjAXCBEg3uA5UvEj`</summary>

```json
{
  "pattern": "**/paper_framing.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "ced99502-568e-4671-81d0-4233d59f15c0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TB43Ktbt3Xt8oPLRXvffkS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17832,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17832,
        "ephemeral_1h_input_tokens": 0
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

_source line 15 · 2026-05-16T02:28:58.754Z_

<details><summary>↩ Tool result · `toolu_01NDAn27pjAXCBEg3uA5UvEj`</summary>

```text
artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md
artifacts/dream_reports/dream_20260515T222933/median/paper_framing.md
artifacts/dream_reports/dream_20260515T222933/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T011810/best/paper_framing.md
artifacts/dream_reports/dream_20260516T011810/median/paper_framing.md
artifacts/dream_reports/dream_20260516T011810/worst/paper_framing.md
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "ccf584ff-cdf9-45f6-af51-bcdc03abbc01"
}
```

</details>

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6f96e6818eb4afa",
  "tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "description": "Finding **/references.bib",
  "usage": {
    "total_tokens": 17859,
    "tool_uses": 2,
    "duration_ms": 1908
  },
  "last_tool_name": "Glob",
  "uuid": "434b7e1b-2f6d-456b-a4d8-56f65286adbf",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_01DjniqWQc2RxkQDDYYfKzQE`</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "6b2fcdca-ca31-49d2-abf4-0d22efff260f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TB43Ktbt3Xt8oPLRXvffkS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17832,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17832,
        "ephemeral_1h_input_tokens": 0
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

_source line 18 · 2026-05-16T02:28:59.144Z_

<details><summary>↩ Tool result · `toolu_01DjniqWQc2RxkQDDYYfKzQE`</summary>

```text
docs/paper/references.bib
artifacts/_project/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "afa511f0-c1a2-4601-8a91-6db17800059f"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6f96e6818eb4afa",
  "tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "description": "Finding **/*framing*",
  "usage": {
    "total_tokens": 17867,
    "tool_uses": 3,
    "duration_ms": 2121
  },
  "last_tool_name": "Glob",
  "uuid": "44020be1-c6c0-4f48-84a3-5044e4bc3fa3",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01GkPsaic7B85wCqfmH8JDMY`</summary>

```json
{
  "pattern": "**/*framing*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "ac315003-83ed-4c4d-aba2-0d3ee1043cec",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TB43Ktbt3Xt8oPLRXvffkS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17832,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17832,
        "ephemeral_1h_input_tokens": 0
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

_source line 21 · 2026-05-16T02:28:59.355Z_

<details><summary>↩ Tool result · `toolu_01GkPsaic7B85wCqfmH8JDMY`</summary>

```text
artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md
artifacts/dream_reports/dream_20260515T222933/median/paper_framing.md
artifacts/dream_reports/dream_20260515T222933/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T011810/best/paper_framing.md
artifacts/dream_reports/dream_20260516T011810/median/paper_framing.md
artifacts/dream_reports/dream_20260516T011810/worst/paper_framing.md
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "7d259e99-f274-4c9b-86b9-196fe34e4239"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6f96e6818eb4afa",
  "tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "description": "Finding **/*story*",
  "usage": {
    "total_tokens": 17875,
    "tool_uses": 4,
    "duration_ms": 2359
  },
  "last_tool_name": "Glob",
  "uuid": "2dd57133-e66f-4c83-a71c-5587a630a62b",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Glob · `toolu_01BtMKrSdGKxa24AdTGGMWkT`</summary>

```json
{
  "pattern": "**/*story*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "e181c011-e850-43b8-b889-588c5cad8749",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TB43Ktbt3Xt8oPLRXvffkS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17832,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17832,
        "ephemeral_1h_input_tokens": 0
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

_source line 24 · 2026-05-16T02:28:59.591Z_

<details><summary>↩ Tool result · `toolu_01BtMKrSdGKxa24AdTGGMWkT`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "3dc832b7-4dfe-42b0-bddf-1709652e3d39"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6f96e6818eb4afa",
  "tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 17883,
    "tool_uses": 5,
    "duration_ms": 2654
  },
  "last_tool_name": "Bash",
  "uuid": "eabfed22-6f1d-42ee-8584-deab5fc89352",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_014uReu6fJruDB4crXgNiUV9`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd -type f -name \"*.md\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "ae463764-d8cb-4dc7-a643-aa2053fa1a6c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TB43Ktbt3Xt8oPLRXvffkS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17832,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17832,
        "ephemeral_1h_input_tokens": 0
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

_source line 27 · 2026-05-16T02:29:00.059Z_

<details><summary>↩ Tool result · `toolu_014uReu6fJruDB4crXgNiUV9`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/agent.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/director/loop_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3_1778877858.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_4_1778887654.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_2_1778866326.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3_1778878478.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_2_1778865132.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_2_1778867412.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_4_1778895396.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3_1778878475.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3_1778889604.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3_1778875986.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_2_1778863795.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_4_1778886984.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_3_1778879069.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/task_context/history/agent/loop_4_1778889532.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "24835460-3181-4123-800c-f05f75995a4e"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6f96e6818eb4afa",
  "tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "description": "Reading paper_framing.md",
  "usage": {
    "total_tokens": 20524,
    "tool_uses": 6,
    "duration_ms": 4470
  },
  "last_tool_name": "Read",
  "uuid": "a50f24fc-3946-45fa-b664-4a1db22700c7",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_019bapSXDvQjxkDJWWZpJYWh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "a082f7c3-ade6-482c-8855-11652ddf8be7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HTzRstxAs968G2E2rLs2eQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2629,
      "cache_read_input_tokens": 17832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2629,
        "ephemeral_1h_input_tokens": 0
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

_source line 30 · 2026-05-16T02:29:01.708Z_

<details><summary>↩ Tool result · `toolu_019bapSXDvQjxkDJWWZpJYWh`</summary>

```text
1	# Paper Framing — vla-ssd
2	
3	## Target Venue
4	- Primary: CoRL 2026
5	- Deadline: Abstract May 26, Paper May 29
6	- Format: 8 pages + references
7	
8	## Core Claims (3 条)
9	
10	1. **Vision Encoder Dominance + Geometric-Functional Dissociation**: VLA 中 action-relevant 表征结构由 frozen vision encoder 决定。RSA geometric alignment: SigLIP (0.615) > CLIP (0.557) >> DINO (0.388)——VL pretrained encoders 显著优于 vision-only。但 functional capacity (R²) 方向相反: DINO (0.634) ≈ Projector (0.630) > CLIP (0.587)。**Geometric alignment 和 predictive capacity 是可分离的独立维度**。VL pretraining 提供 geometric alignment（表征结构匹配 action 空间），不增加甚至略降低 functional capacity。
11	2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM 降解 distributed image token 的 **geometric alignment**（RSA: 0.615→0.501）和 functional capacity（R²: 0.630→0.599, p<0.001），但 global structure 保留（CKA 单调上升）。**训练后** LLM 学会将 action 信号 concentrate 到 readout token（trained R²=0.671 > projector 0.630, p=0.002），但 **untrained LLM 做不到**（untrained readout best=0.686 < projector）。Readout concentration 是 learned behavior，不是架构固有属性。
12	3. **Training: Routing Without Creating**: VLA fine-tuning 不改变 distributed representation structure（image_mean RSA: trained 0.501 ≈ untrained 0.485, bootstrap CI includes 0, p=0.20），但提升 readout concentration（trained last_preaction 0.731 >> untrained 0.686，Δ=0.045, bootstrap CI=[0.032, 0.058], p<0.0001）。Instruction input 对两者均无影响。综合解读：**Training 的贡献是学习信息路由（routing），而非注入新的 action knowledge（creating）**。
13	
14	## Paper 主数值基准（image_mean 聚合，公平对比）
15	
16	| Model / Condition | RSA (image_mean) | Notes |
17	|---|---|---|
18	| **SigLIP+Projector** | **0.615** | Smoking gun, LLM input |
19	| VLA trained with-inst | 0.501 | Peak L23 |
20	| VLA untrained with-inst | 0.485 | Peak L23 |
21	| VLA trained no-inst | 0.501 | Peak L23, identical to with-inst |
22	| VLA untrained no-inst | 0.482 | Peak L29 |
23	| **CLIP ViT-L/14** | **0.557** | VL-pretrained control, CI=[0.442, 0.660] |
24	| DINO-V2 | 0.388 | Vision-only baseline |
25	
26	last_preaction 数值（trained 0.488, untrained 0.485）放 supplementary 作为 robustness check。
27	
28	## Functional Probe 数值基准
29	
30	### Raw Action Prediction R² (统一超参: 50ep/patience5/lr1e-3/hidden256/seed42)
31	
32	| Model | mean_R² | Notes |
33	|---|---|---|
34	| **VLA Trained last_preaction L19** | **0.671** | readout concentration, > projector (p=0.002) |
35	| DINO-V2 cls | 0.634 | ≈ projector (p=0.557, n.s.) |
36	| **SigLIP+Projector** | **0.630** | ≈ DINO |
37	| VLA Trained image_mean L19 | 0.599 | < projector (p<0.001) |
38	| CLIP ViT-L/14 cls | 0.587 | < projector (p<0.001), < DINO (p<0.001) |
39	
40	**Ordering**: last_preaction (0.671) > DINO (0.634) ≈ Projector (0.630) > image_mean (0.599) > CLIP (0.587)
41	
42	**重要发现 — Geometric-Functional Dissociation（比预期更极端）**:
43	- RSA 排序: SigLIP (0.615) > CLIP (0.557) >> DINO (0.388) — VL pretraining 提高几何对齐
44	- R² 排序: DINO (0.634) ≈ Projector (0.630) > CLIP (0.587) — VL pretraining **降低**预测能力
45	- **RSA 和 R² 方向相反**：CLIP 高几何低预测，DINO 低几何高预测
46	- 结论：geometric alignment（表征结构匹配 action 空间）与 predictive capacity（probe 可解码性）是**可分离的独立维度**。VL pretraining 选择性提供 geometric alignment，但不增加甚至略降低 functional capacity。
47	- Redistribution 不变：last_preaction > all others 确认 LLM routing 有效
48	
49	注：所有 probe 统一预测 a_{t+1}（已验证，无 target 差异问题）。论文主表（5-model 对比）用 unified_action_probe 数字。Untrained/trained 对比 + delta probes 用 p0_probe_v2（同一 target，内部一致）。两组 R² 绝对值不同是超参/数据处理差异，不影响组内排序和结论。
50	
51	### Action-Delta Prediction R²
52	
53	| Model | mean_R² | Notes |
54	|---|---|---|
55	| VLA Trained image_mean L14 | 0.122 | |
56	| SigLIP+Projector | 0.118 | ≈ LLM, CI includes 0 (p=0.04) |
57	| Untrained image_mean L0 | 0.117 | ≈ projector ≈ LLM |
58	| DINO (LIBERO-Goal) | 0.100 | action_delta probe from v2 |
59	| DINO (MVP-2 LIBERO-10) | 0.061 | 2× lower than projector/LLM |
60	
61	**Delta 维度结论**：三者几乎相同（~0.12），远 > DINO (0.06-0.10)。支持 vision encoder dominance（所有 action-delta info 追溯到 SigLIP）。Delta last_preaction 缺失（待补）。
62	
63	### 聚合口径依赖性（论文必须如实讨论）
64	
65	| Comparison | image_mean | last_preaction |
66	|---|---|---|
67	| Raw action: Proj vs LLM | Proj wins (+0.023, CI=[0.011, 0.037], p=0.001) | LLM wins (+0.025, p=0.001) |
68	| Delta: Proj vs LLM | ≈ tie (−0.003, CI includes 0) | TBD |
69	
70	主文用 image_mean（公平聚合），last_preaction 放 supplementary。但必须讨论聚合口径对结论的影响。
71	
72	## Story Spine
73	
74	- **Problem**: VLAs 通过 fine-tuning LLM on robot data 实现 impressive performance，但 action-relevant 表征从何而来？业界隐性假设 fine-tuning 注入 new representational knowledge，但无系统性验证。
75	- **Existing approaches & gaps**: Grant et al. 2026 从 behavioral level 发现 visual pathway dominates，但未做 representational decomposition。无人测量过 VLA 各组件（vision encoder / projector / LLM）对 action-relevant 表征结构的独立贡献。
76	- **Our framing**: 首次对 VLA 进行系统性 representational + functional analysis——组件级分解 + per-layer probing + action prediction probes，定量揭示 action-relevant 结构的来源和 LLM 对其的变换。发现 vision encoder 是 action information 的通用源头（DINO ≈ SigLIP in R²，但 VL pretraining 赋予 geometric alignment）。LLM 降解分布式 image token 表征但通过**训练依赖的** attention 机制将信号聚合到 readout token——training 教会 routing 而非 creating new knowledge。
77	- **Headline result**: "The frozen vision encoder provides action-relevant representations (RSA ρ=0.615, action probe R²=0.706) that the LLM degrades at the image-token level (R²→0.683) but reconcentrates into a readout token (R²=0.731). This reconcentration is training-dependent (untrained readout R²=0.686 < projector 0.706), while distributed representation structure remains training-invariant (image_mean RSA: trained 0.501 ≈ untrained 0.485, p=0.20). Language instructions affect neither."
78	- **✅ All core evidence complete.** P1 remaining: plan_012 CLIP-ViT control, plan_010 LIBERO-Spatial (P2).
79	
80	## Anticipated Reviewer Concerns & Responses
81	
82	### C1: 单一 VLA 架构（OpenVLA）泛化性
83	- **应对**: Scope 明确限定为 "OpenVLA-class architecture"。OpenVLA 是最广泛使用的开源 VLA 之一，findings 对该架构族直接适用。Discussion 中讨论扩展到其他架构的预期。
84	- **实验**: 无需额外实验，Limitations 明确标注。
85	
86	### C2: SigLIP vs DINOv2 pretraining confound
87	- **问题**: SigLIP 是 image-text contrastive pretrained，DINOv2 是 self-supervised。RSA gap 可能来自 language-aware pretraining 而非纯 vision encoder 质量。
88	- **应对**: 这个 confound 实际上 **强化** 我们的 story——如果 gap 来自 SigLIP 的 vision-language pretraining，说明 pretraining 阶段的 language grounding 远比 task-specific fine-tuning 重要。Discussion 正面讨论此 confound 并将其转化为 insight。新发现加强此论点：DINO 与 Projector 在 action R² 上无差异（0.712 vs 0.706, p=0.22），但 RSA 几何差异显著（0.388 vs 0.615）。说明 VL pretraining 的贡献在于 geometric alignment 而非 information content。
89	- **实验**: ✅ plan_012 CLIP-ViT control Done。CLIP RSA=0.557, 远高于 DINO (0.388), 接近 SigLIP+projector (0.615)。确认 VL pretraining 是关键因素，非 SigLIP 独有。CLIP action probe R² 待补。
90	
91	### C3: LLM 对 action structure 的作用机制
92	- **问题**: LLM 到底做了什么？为什么 image token RSA 降低？
93	- **应对**: Functional probe 揭示机制——LLM 降解分布式 image token 表征（R² 0.706→0.683, bootstrap CI=[0.011, 0.037]）但通过 self-attention 将 action 信号 concentrate 到 readout token（R² 0.731）。这是 next-token prediction architecture 的自然行为：信息从 context tokens 流向 prediction position。Per-layer curve 的非单调模式（中间层部分恢复）与此一致。
94	- **实验**: ✅ plan_011 functional probe (Done) + plan_003 per-layer curve (Done)。
95	
96	### C4: Grant 2026 checkpoint 差异
97	- **问题**: Grant 用 OFT fine-tuned，我们用 standard fine-tuning checkpoint。
98	- **应对**: 我们用 standard fine-tuning 是更强的测试——如果完全不同的 LLM 权重（random init vs pretrained+finetuned，cos_sim≈0.2）都不改变表征，OFT 更不会。Related Work 明确区分。
99	
100	### C5: Practical implications / 功能验证
101	- **问题**: RSA alignment ≠ task performance。Practical implications?
102	- **应对**: ✅ plan_011 functional probe 完成——projector R²=0.706 vs LLM image_mean 0.683（gap=0.023, bootstrap CI=[0.011, 0.037], p=0.001）。LLM readout token R²=0.731 > projector（p=0.001）。Delta probe: projector < LLM 但不显著（CI 含 0）。三个建议：(1) Vision encoder pretraining 是 action info 关键；(2) Image-level tasks 用 projector output；(3) LLM 的价值在于 readout concentration。
103	- **实验**: ✅ plan_011 Done（含 bootstrap CI + DINO 三方对比）。
104	
105	### C6: 聚合方式伪影（已解决）
106	- **问题**: SigLIP 用 mean pooling，VLA 用 last token，比较不公平。
107	- **应对**: ✅ 已用 image_mean 聚合验证。VLA image_mean RSA=0.501，仍远低于 SigLIP 0.615（gap=0.114）。两种聚合方式结果一致（last_preaction 0.488 vs image_mean 0.501）。主文使用 image_mean 保证公平，last_preaction 放 supplementary。
108	
109	## Key Evidence Inventory
110	
111	| Evidence | Claim | Status |
112	|----------|-------|--------|
113	| SigLIP+Projector RSA=0.615 | C1, C2 | ✅ Done |
114	| Full VLA RSA ≈ 0.501 (image_mean, 4 conditions) | C2, C3 | ✅ Done |
115	| DINO RSA=0.388 | C1 | ✅ Done |
116	| 6 probing methods × 2 benchmarks: trained ≈ untrained | C3 | ✅ Done |
117	| Instruction ablation Δ=0.004 | C3 | ✅ Done |
118	| 2×2 matrix Bootstrap CI includes 0 | C3 | ✅ Done |
119	| Output head analysis: SigLIP+projector frozen | C1, C2 | ✅ Done |
120	| Per-layer RSA degradation curve | C2 | ✅ Done — non-monotonic, Proj→L1 primary drop |
121	| VLA image_mean RSA (aggregation robustness) | C2 | ✅ Done — 0.501 vs SigLIP 0.615, gap=0.114 |
122	| Bootstrap CI on training effect (image_mean) | C3 | ✅ Done — CI includes 0, invariance holds |
123	| Functional action probe: Proj 0.706 vs LLM img_mean 0.683 vs readout 0.731 | C1, C2 | ✅ Done — bootstrap CI=[0.011, 0.037], p=0.001 |
124	| DINO action probe on LIBERO-Goal | C1 | ✅ Done — R²=0.712, DINO ≈ Proj (p=0.22) |
125	| Action-delta probe: Proj 0.118 < LLM 0.122, CI includes 0 | C2 | ✅ Done — BELOW but not significant |
126	| No-inst image_mean RSA: trained 0.501 = with-inst, untrained 0.482 | C3 | ✅ Done |
127	| Untrained last_preaction: L32 R²=0.686 < projector 0.706 | C2, C3 | ✅ Done — redistribution is training-dependent (D034) |
128	| Untrained vs trained last_preaction bootstrap CI | C2, C3 | ✅ Done — Δ=0.045, CI=[0.032, 0.058], p<0.0001 |
129	| Random instruction control: normal 0.489, random 0.484, shuffled 0.483, empty 0.472 — all within ±0.017 | C3 | ✅ Done — instruction content invariant (plan_008) |
130	| CLIP-ViT RSA=0.557 >> DINO 0.388; CLIP R²=0.805 ≈ DINO 0.814 (p=0.10 n.s.) — geometric-functional dissociation confirmed across VL encoders | C1, C2 | ✅ Done — plan_012 complete |
131	| CKA verification: ordering reversal — CKA untrained > trained > proj > DINO | C1, C2, C7 | ✅ Done — RSA-CKA dissociation (plan_009) |
132	| LIBERO-Spatial cross-benchmark | C1, C2, C3 | 📋 P2 planned (plan_010) |
133	
134	### C7: RSA vs CKA metric dependency — 排序反转（plan_009 已完成）
135	- **问题**: CKA 不仅缩小 gap，还**反转排序**。RSA: projector > trained > untrained > DINO。CKA: untrained > trained > projector > DINO。
136	- **数据**:
137	  - CKA vs actions: untrained L23 (0.089) > trained L23 (0.083) > projector (0.081) > DINO (0.066)
138	  - CKA per-layer trained image_mean: L0=0.081 **单调上升** to L32=0.098（与 RSA 的非单调模式不同）
139	  - CKA last_preaction: L32=0.127（最高，支持 redistribution — readout concentration）
140	  - CKA_RDM: last_preaction (0.290) > projector (0.257) ≈ trained (0.260) > DINO (0.241)（部分一致）
141	- **应对**: 论文正面讨论作为 finding。关键区分：
142	  - RSA 捕捉 **local geometric alignment**（representation 距离结构是否匹配 action 距离结构）→ LLM 降解
143	  - CKA 捕捉 **global structure preservation**（整体变换后结构是否保留）→ LLM 保留或改善
144	  - **Claim 2 必须明确限定为 "geometric (RSA) degradation"**，不能泛化为 "representation quality degradation"
145	  - CKA last_preaction 最高 (0.127) 与 redistribution narrative 一致
146	- **实验**: ✅ plan_009 Done。
147	
148	## Literature Positioning
149	
150	- **Grant et al. 2026**: Behavioral level "visual pathway dominates" → 我们 representational level 确认 + 定量组件分解
151	- **Fang 2025**: "Fine-tuning erodes VLM reasoning" → 我们发现 LLM step 本身（不只是 fine-tuning）就降低 visual structure
152	- **Hou 2026 (LangGap) / Fei 2025 (LIBERO-Plus)**: "VLAs ignore language instructions" → 我们从 representation level 解释 why：instruction text 对表征结构无实质影响
153	- **Haon et al. (CoRL 2025)**: Mechanistic interpretability + activation steering on OpenVLA — same venue, same model. Must discuss: their sparse semantic directions vs our geometric analysis are complementary views
154	- **Lu et al. 2025**: Linear probing on OpenVLA hidden layers >90% accuracy — methodologically closest, must differentiate (component decomposition vs layer probing)
155	- **Rizzardo et al. 2026**: Feature observability/controllability in VLAs
156	- **Swann et al. 2026**: SAE-based OpenVLA interpretability
157	- **Molinari et al. 2025**: Emergent world representations in OpenVLA
158	- **Karamcheti et al. 2024 (Prismatic)**: OpenVLA's architectural foundation, must cite
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "e8ec40f8-61d7-407e-934c-b22ee70f15b6"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6f96e6818eb4afa",
  "tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "description": "Reading docs/paper/references.bib",
  "usage": {
    "total_tokens": 20528,
    "tool_uses": 7,
    "duration_ms": 4675
  },
  "last_tool_name": "Read",
  "uuid": "da3c8c7c-5e96-4cc7-98a9-5b76677efcf8",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01Hc5KTEPUBcB8w2Zk16ao7V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "3e991bfd-b2c9-4600-bf35-401d8d3e1e10",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HTzRstxAs968G2E2rLs2eQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2629,
      "cache_read_input_tokens": 17832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2629,
        "ephemeral_1h_input_tokens": 0
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

_source line 33 · 2026-05-16T02:29:01.903Z_

<details><summary>↩ Tool result · `toolu_01Hc5KTEPUBcB8w2Zk16ao7V`</summary>

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
85	% [VERIFY] Cannot confirm full bibliographic details. Cited for behavioral visual dominance in VLA policies.
86	@article{grant2026,
87	  title     = {[VERIFY] Behavioral Visual Dominance in Vision-Language-Action Policies},
88	  author    = {Grant, [VERIFY]},
89	  journal   = {[VERIFY]},
90	  year      = {2026},
91	}
92	
93	% [VERIFY] Cannot confirm full bibliographic details. Cited for VLA interpretability.
94	@article{haon2025,
95	  title     = {[VERIFY] Interpretability of Vision-Language-Action Models},
96	  author    = {Haon, [VERIFY]},
97	  journal   = {[VERIFY]},
98	  year      = {2025},
99	}
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "a3798ada-d1c0-4ee5-8f01-35ae42042f9f"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6f96e6818eb4afa",
  "tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "description": "Reading artifacts/_project/paper/references.bib",
  "usage": {
    "total_tokens": 20532,
    "tool_uses": 8,
    "duration_ms": 5053
  },
  "last_tool_name": "Read",
  "uuid": "a226b57a-d4e2-4e39-959f-c50eaad4a7ae",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01UL7EyfjRvSbvahcUyuPJve`</summary>

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
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "3505bb4b-1e25-4e97-8be8-ea852d5940c1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HTzRstxAs968G2E2rLs2eQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2629,
      "cache_read_input_tokens": 17832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2629,
        "ephemeral_1h_input_tokens": 0
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

_source line 36 · 2026-05-16T02:29:02.297Z_

<details><summary>↩ Tool result · `toolu_01UL7EyfjRvSbvahcUyuPJve`</summary>

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
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "3c06b31d-bca7-432b-980c-403336b00d4c"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6f96e6818eb4afa",
  "tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "description": "Reading artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md",
  "usage": {
    "total_tokens": 30281,
    "tool_uses": 9,
    "duration_ms": 7569
  },
  "last_tool_name": "Read",
  "uuid": "eb6f9ef0-f810-49b2-bcab-13b62d0b3856",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01F5LrQ4XwekrRwqLZ7dQAWH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "d59c0868-1fb4-41a9-a6af-2963f9398335",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CqdFsVnicAWjsg7ctmmdbu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9745,
      "cache_read_input_tokens": 20461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9745,
        "ephemeral_1h_input_tokens": 0
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

_source line 39 · 2026-05-16T02:29:04.800Z_

<details><summary>↩ Tool result · `toolu_01F5LrQ4XwekrRwqLZ7dQAWH`</summary>

```text
1	# Paper Framing — vla-ssd
2	
3	## Target Venue
4	- Primary: CoRL 2026
5	- Deadline: Abstract May 26, Paper May 29
6	- Format: 8 pages + references
7	
8	## Core Claims (3 条)
9	
10	1. **Vision Encoder Dominance**: VLA 中 action-relevant 表征结构由 frozen vision encoder（SigLIP）决定。SigLIP+projector 的 RSA 与 action structure 的相关性（ρ=0.615）远高于完整 VLA（ρ≈0.488）和 standalone vision model（DINOv2 ρ=0.388）。
11	2. **LLM Degrades Action Alignment**: LLM processing 降低而非增强 action-relevant 几何结构（0.615→0.488）。这一 degradation 在 trained/untrained、with/without instruction 四种条件下一致发生。
12	3. **Training and Instruction Invariance**: VLA task-specific fine-tuning（Δ<0.01）和 instruction input（Δ<0.005）均不显著改变 LLM hidden state 中的 action-relevant 表征结构。2×2 matrix（training × instruction）四格收敛于 0.48-0.49。
13	
14	## Story Spine
15	
16	- **Problem**: VLAs 通过 fine-tuning LLM on robot data 实现 impressive performance，但 action-relevant 表征从何而来？业界隐性假设 fine-tuning 注入 new representational knowledge，但无系统性验证。
17	- **Existing approaches & gaps**: Grant et al. 2026 从 behavioral level 发现 visual pathway dominates，但未做 representational decomposition。无人测量过 VLA 各组件（vision encoder / projector / LLM）对 action-relevant 表征结构的独立贡献。
18	- **Our framing**: 首次对 VLA 进行系统性 representational analysis——7 种 probing 方法 × 2 benchmarks × 组件级分解，定量揭示 action-relevant 结构的来源。发现 LLM 不仅不贡献，反而 degrades vision encoder 提供的 action alignment。
19	- **Headline result**: "SigLIP+projector representations achieve RSA ρ=0.615 with action structure, while the full VLA only achieves ρ≈0.488 regardless of training or instruction — the LLM degrades rather than enhances action-relevant representations."
20	
21	## Anticipated Reviewer Concerns & Responses
22	
23	### C1: 单一 VLA 架构（OpenVLA）泛化性
24	- **应对**: Scope 明确限定为 "OpenVLA-class architecture"。OpenVLA 是最广泛使用的开源 VLA 之一，findings 对该架构族直接适用。Discussion 中讨论扩展到其他架构的预期。
25	- **实验**: 无需额外实验，Limitations 明确标注。
26	
27	### C2: SigLIP vs DINOv2 pretraining confound
28	- **问题**: SigLIP 是 image-text contrastive pretrained，DINOv2 是 self-supervised。RSA gap 可能来自 language-aware pretraining 而非纯 vision encoder 质量。
29	- **应对**: 这个 confound 实际上 **强化** 我们的 story——如果 gap 来自 SigLIP 的 vision-language pretraining，说明 pretraining 阶段的 language grounding 远比 task-specific fine-tuning 重要。Discussion 正面讨论此 confound 并将其转化为 insight。
30	- **实验**: P2 可补 CLIP vs DINOv2 对比，但非 blocking。
31	
32	### C3: LLM degradation 机制不清
33	- **问题**: 为什么 LLM 降低 action alignment？
34	- **应对**: LLM 对 representation 做 next-token prediction 优化的变换，这与保持 action-relevant geometric structure 目标不同。Projector bottleneck（D026 发现 SigLIP+projector frozen）约束了信息通路。Discussion 讨论 information bottleneck 解释。
35	- **实验**: Per-layer RSA degradation curve 作为 P1 supplementary evidence。
36	
37	### C4: Grant 2026 checkpoint 差异
38	- **问题**: Grant 用 OFT fine-tuned，我们用 standard fine-tuning checkpoint。
39	- **应对**: 我们用 standard fine-tuning 是更强的测试——如果完全不同的 LLM 权重（random init vs pretrained+finetuned，cos_sim≈0.2）都不改变表征，OFT 更不会。Related Work 明确区分。
40	
41	### C5: Practical implications 不够
42	- **问题**: 发现了问题，然后呢？
43	- **应对**: 三个可操作建议：(1) 投资 vision encoder pretraining 质量比 LLM fine-tuning 更重要；(2) representation-based downstream tasks 应直接使用 projector output 而非 LLM hidden states；(3) VLA 架构设计应关注减少 LLM 对 visual structure 的 degradation。
44	
45	## Key Evidence Inventory
46	
47	| Evidence | Claim | Status |
48	|----------|-------|--------|
49	| SigLIP+Projector RSA=0.615 | C1, C2 | ✅ Done |
50	| Full VLA RSA ≈ 0.488 (4 conditions) | C2, C3 | ✅ Done |
51	| DINO RSA=0.388 | C1 | ✅ Done |
52	| 6 probing methods × 2 benchmarks: trained ≈ untrained | C3 | ✅ Done |
53	| Instruction ablation Δ=0.004 | C3 | ✅ Done |
54	| 2×2 matrix Bootstrap CI includes 0 | C3 | ✅ Done |
55	| Output head analysis: SigLIP+projector frozen | C1, C2 | ✅ Done |
56	| Per-layer RSA degradation curve | C2 | 🔄 P1 supplementary |
57	| Random instruction control | C3 | 📋 P1 planned |
58	
59	## Literature Positioning
60	
61	- **Grant et al. 2026**: Behavioral level "visual pathway dominates" → 我们 representational level 确认 + 定量组件分解
62	- **Fang 2025**: "Fine-tuning erodes VLM reasoning" → 我们发现 LLM step 本身（不只是 fine-tuning）就降低 visual structure
63	- **Hou 2026 (LangGap) / Fei 2025 (LIBERO-Plus)**: "VLAs ignore language instructions" → 我们从 representation level 解释 why：instruction text 对表征结构无实质影响
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "71ecb888-cefc-423e-b80e-9fd9abaee834"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6f96e6818eb4afa",
  "tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "description": "Running ls -lah /home/ubuntu/.agent-ml-research-idea_gen_…",
  "usage": {
    "total_tokens": 30283,
    "tool_uses": 10,
    "duration_ms": 7728
  },
  "last_tool_name": "Bash",
  "uuid": "f65fe750-ed7b-4f8e-b1f1-9701934c0975",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01QjSo5LABx7obPfah9N4wA6`</summary>

```json
{
  "command": "ls -lah /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "d7200a26-3cf1-4d36-81bf-1140148d68c0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CqdFsVnicAWjsg7ctmmdbu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9745,
      "cache_read_input_tokens": 20461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9745,
        "ephemeral_1h_input_tokens": 0
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

_source line 42 · 2026-05-16T02:29:05.029Z_

<details><summary>↩ Tool result · `toolu_01QjSo5LABx7obPfah9N4wA6`</summary>

```text
total 328K
drwxr-xr-x  9 ubuntu ubuntu 4.0K May 16 02:21 .
drwxrwxr-x  5 ubuntu ubuntu 4.0K May 15 04:32 ..
drwxr-xr-x  3 ubuntu ubuntu 4.0K May 15 04:32 .claude
-rw-------  1 ubuntu ubuntu    0 May 15 17:07 .registry_veak6jl2.tmp
-rw-r--r--  1 ubuntu ubuntu  13K May 16 02:28 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu    0 May 15 04:34 ROADMAP.lock
-rw-------  1 ubuntu ubuntu 4.1K May 16 02:14 ROADMAP.md
drwxr-xr-x 10 ubuntu ubuntu 4.0K May 16 02:09 artifacts
drwxr-xr-x  2 ubuntu ubuntu  32K May 16 02:17 checkpoints
-rw-r--r--  1 ubuntu ubuntu    0 May 15 19:40 constraints.lock
-rw-------  1 ubuntu ubuntu  440 May 15 19:40 constraints.yaml
-rw-r--r--  1 ubuntu ubuntu    0 May 15 11:03 decisions.lock
-rw-------  1 ubuntu ubuntu  43K May 16 02:14 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu 4.0K May 15 05:23 docs
-rwxr-xr-x  1 ubuntu ubuntu    0 May 15 05:23 dream_registry.lock
-rw-------  1 ubuntu ubuntu 1.9K May 16 01:59 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu 1.9K May 16 01:59 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu 5.3K May 16 01:41 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu  29K May 16 02:15 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu 4.0K May 15 04:56 logs
-rw-r--r--  1 ubuntu ubuntu 6.2K May 16 02:14 memory.md
-rw-r--r--  1 ubuntu ubuntu  15K May 16 02:21 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu    0 May 15 04:55 registry.lock
-rw-------  1 ubuntu ubuntu  83K May 16 02:20 registry.yaml
-rw-r--r--  1 ubuntu ubuntu 1.9K May 16 02:17 report.md
drwxr-xr-x  2 ubuntu ubuntu 4.0K May 15 19:16 scripts
-rwxr-xr-x  1 ubuntu ubuntu    0 May 15 04:33 study_status.lock
drwxr-xr-x  3 ubuntu ubuntu 4.0K May 16 02:28 task_context
-rw-r--r--  1 ubuntu ubuntu  27K May 16 02:09 writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "885e6137-fbb5-4387-aad4-2501a72e91fd"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ad6f96e6818eb4afa",
  "tool_use_id": "toolu_01GU9V4Q4WDF22n3FYFv26oh",
  "status": "completed",
  "output_file": "",
  "summary": "Find paper framing files",
  "usage": {
    "total_tokens": 33374,
    "tool_uses": 10,
    "duration_ms": 23720
  },
  "uuid": "bff04b69-ab5a-4e29-84af-9384c7fd3ff3",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a"
}
```

---

### Tool result

_source line 44 · 2026-05-16T02:29:20.942Z_

<details><summary>↩ Tool result · `toolu_01GU9V4Q4WDF22n3FYFv26oh`</summary>

```text
Perfect. I've found all the framing and bibliography files. Let me provide you with a comprehensive report.

## Summary of Findings

I found three key document types in the vla-ssd project:

### Paper Framing Documents Located

**Main file:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md`

**Dream report variants (historical iterations):**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/worst/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/best/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/median/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/worst/paper_framing.md`

### Bibliography Files Located

**Main BibTeX file:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib`

**Archived version:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/references.bib`

---

### Key Content Snippets

**Main Paper Framing:**
The primary framing document is comprehensive and highly detailed. The core contribution is a **three-claim architecture**:

1. **Vision Encoder Dominance + Geometric-Functional Dissociation**: VLA action-relevant representations are determined by frozen vision encoder (SigLIP). Representational Similarity Analysis shows: SigLIP (RSA ρ=0.615) > CLIP (0.557) >> DINO (0.388). But action prediction capacity (R²) shows opposite ordering: DINO (0.634) ≈ Projector (0.630) > CLIP (0.587). This reveals that geometric alignment and predictive capacity are separable, independent dimensions.

2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM reduces geometric alignment (RSA: 0.615→0.501) and functional capacity (R²: 0.630→0.599), but preserves global structure (CKA monotonically increases). **After training**, the LLM learns to concentrate action signals into the readout token (trained R²=0.671 > projector 0.630, p=0.002), but untrained LLM cannot. This concentration is learned behavior, not architectural property.

3. **Training: Routing Without Creating**: VLA fine-tuning doesn't change distributed representation structure (image_mean RSA: trained 0.501 ≈ untrained 0.485, p=0.20), but improves readout concentration (trained last_preaction 0.731 >> untrained 0.686, Δ=0.045, p<0.0001). Training's contribution is learning information routing, not injecting new action knowledge.

**Target Venue:** CoRL 2026 (Abstract deadline May 26, Paper deadline May 29, 8 pages + references)

**Main numerical benchmarks (image_mean aggregation):**
- SigLIP+Projector RSA: 0.615
- Full VLA (4 conditions): RSA ≈ 0.501
- CLIP ViT-L/14: 0.557
- DINO-V2: 0.388

**Anticipated challenges addressed:**
- C1: Single VLA architecture generalizability (scoped to OpenVLA-class)
- C2: SigLIP vs DINOv2 pretraining confound (addressed via CLIP control, plan_012)
- C3: LLM's mechanism of action degradation (functional probes show routing vs creating)
- C4: Grant 2026 checkpoint differences (standard fine-tuning is stronger test)
- C5: Practical implications (vision encoder pretraining > LLM fine-tuning)
- C6: Aggregation method artifacts (validated with image_mean aggregation)
- C7: RSA vs CKA metric dependency (ranking reversal documented as finding)

**Bibliography:**
The references file contains ~17 citations covering:
- VLA/Architecture: OpenVLA (Kim 2024), Prismatic VLMs (Karamcheti 2024), RT-2 (Brohan 2023)
- Benchmarks: LIBERO (Liu 2023)
- Analysis methods: RSA (Kriegeskorte 2008), CKA/similarity (Kornblith 2019), Linear probing (Alain 2017)
- Vision encoders: SigLIP (Zhai 2023), DINOv2 (Oquab 2024), CLIP (Radford 2021)
- Domain-specific: Grant 2026 (visual dominance), Haon 2025 (mechanistic interpretability)

**Evolution:** The dream reports show evolution from earlier "degradation" framing to the current "routing vs creating" mechanistic story with detailed functional probes and training-dependent analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "8532e8c5-4fe7-4461-b1d8-0ddc934caea3",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search for paper_framing.md or any framing/story document in the vla-ssd project. Check paths like /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ and subdirectories. Also look for references.bib. Report file paths found and key content snippets.",
    "agentId": "ad6f96e6818eb4afa",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. I've found all the framing and bibliography files. Let me provide you with a comprehensive report.\n\n## Summary of Findings\n\nI found three key document types in the vla-ssd project:\n\n### Paper Framing Documents Located\n\n**Main file:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md`\n\n**Dream report variants (historical iterations):**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/median/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260515T222933/worst/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/best/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/median/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/dream_20260516T011810/worst/paper_framing.md`\n\n### Bibliography Files Located\n\n**Main BibTeX file:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib`\n\n**Archived version:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/references.bib`\n\n---\n\n### Key Content Snippets\n\n**Main Paper Framing:**\nThe primary framing document is comprehensive and highly detailed. The core contribution is a **three-claim architecture**:\n\n1. **Vision Encoder Dominance + Geometric-Functional Dissociation**: VLA action-relevant representations are determined by frozen vision encoder (SigLIP). Representational Similarity Analysis shows: SigLIP (RSA ρ=0.615) > CLIP (0.557) >> DINO (0.388). But action prediction capacity (R²) shows opposite ordering: DINO (0.634) ≈ Projector (0.630) > CLIP (0.587). This reveals that geometric alignment and predictive capacity are separable, independent dimensions.\n\n2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM reduces geometric alignment (RSA: 0.615→0.501) and functional capacity (R²: 0.630→0.599), but preserves global structure (CKA monotonically increases). **After training**, the LLM learns to concentrate action signals into the readout token (trained R²=0.671 > projector 0.630, p=0.002), but untrained LLM cannot. This concentration is learned behavior, not architectural property.\n\n3. **Training: Routing Without Creating**: VLA fine-tuning doesn't change distributed representation structure (image_mean RSA: trained 0.501 ≈ untrained 0.485, p=0.20), but improves readout concentration (trained last_preaction 0.731 >> untrained 0.686, Δ=0.045, p<0.0001). Training's contribution is learning information routing, not injecting new action knowledge.\n\n**Target Venue:** CoRL 2026 (Abstract deadline May 26, Paper deadline May 29, 8 pages + references)\n\n**Main numerical benchmarks (image_mean aggregation):**\n- SigLIP+Projector RSA: 0.615\n- Full VLA (4 conditions): RSA ≈ 0.501\n- CLIP ViT-L/14: 0.557\n- DINO-V2: 0.388\n\n**Anticipated challenges addressed:**\n- C1: Single VLA architecture generalizability (scoped to OpenVLA-class)\n- C2: SigLIP vs DINOv2 pretraining confound (addressed via CLIP control, plan_012)\n- C3: LLM's mechanism of action degradation (functional probes show routing vs creating)\n- C4: Grant 2026 checkpoint differences (standard fine-tuning is stronger test)\n- C5: Practical implications (vision encoder pretraining > LLM fine-tuning)\n- C6: Aggregation method artifacts (validated with image_mean aggregation)\n- C7: RSA vs CKA metric dependency (ranking reversal documented as finding)\n\n**Bibliography:**\nThe references file contains ~17 citations covering:\n- VLA/Architecture: OpenVLA (Kim 2024), Prismatic VLMs (Karamcheti 2024), RT-2 (Brohan 2023)\n- Benchmarks: LIBERO (Liu 2023)\n- Analysis methods: RSA (Kriegeskorte 2008), CKA/similarity (Kornblith 2019), Linear probing (Alain 2017)\n- Vision encoders: SigLIP (Zhai 2023), DINOv2 (Oquab 2024), CLIP (Radford 2021)\n- Domain-specific: Grant 2026 (visual dominance), Haon 2025 (mechanistic interpretability)\n\n**Evolution:** The dream reports show evolution from earlier \"degradation\" framing to the current \"routing vs creating\" mechanistic story with detailed functional probes and training-dependent analysis."
      }
    ],
    "totalDurationMs": 23722,
    "totalTokens": 34755,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3090,
      "cache_read_input_tokens": 30206,
      "output_tokens": 1452,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3090
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1452,
          "cache_read_input_tokens": 30206,
          "cache_creation_input_tokens": 3090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3090,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 4,
      "bashCount": 2,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01FyyaEdSrSnWme7y37AyjHD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "0841e917-41ec-4548-b266-59e39f66259f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mq8V1Aqi2uMtZmDYUREaGv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1672,
      "cache_read_input_tokens": 29872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1672
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

_source line 46 · 2026-05-16T02:29:24.087Z_

<details><summary>↩ Tool result · `toolu_01FyyaEdSrSnWme7y37AyjHD`</summary>

```text
1	# Paper Framing — vla-ssd
2	
3	## Target Venue
4	- Primary: CoRL 2026
5	- Deadline: Abstract May 26, Paper May 29
6	- Format: 8 pages + references
7	
8	## Core Claims (3 条)
9	
10	1. **Vision Encoder Dominance + Geometric-Functional Dissociation**: VLA 中 action-relevant 表征结构由 frozen vision encoder 决定。RSA geometric alignment: SigLIP (0.615) > CLIP (0.557) >> DINO (0.388)——VL pretrained encoders 显著优于 vision-only。但 functional capacity (R²) 方向相反: DINO (0.634) ≈ Projector (0.630) > CLIP (0.587)。**Geometric alignment 和 predictive capacity 是可分离的独立维度**。VL pretraining 提供 geometric alignment（表征结构匹配 action 空间），不增加甚至略降低 functional capacity。
11	2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM 降解 distributed image token 的 **geometric alignment**（RSA: 0.615→0.501）和 functional capacity（R²: 0.630→0.599, p<0.001），但 global structure 保留（CKA 单调上升）。**训练后** LLM 学会将 action 信号 concentrate 到 readout token（trained R²=0.671 > projector 0.630, p=0.002），但 **untrained LLM 做不到**（untrained readout best=0.686 < projector）。Readout concentration 是 learned behavior，不是架构固有属性。
12	3. **Training: Routing Without Creating**: VLA fine-tuning 不改变 distributed representation structure（image_mean RSA: trained 0.501 ≈ untrained 0.485, bootstrap CI includes 0, p=0.20），但提升 readout concentration（trained last_preaction 0.731 >> untrained 0.686，Δ=0.045, bootstrap CI=[0.032, 0.058], p<0.0001）。Instruction input 对两者均无影响。综合解读：**Training 的贡献是学习信息路由（routing），而非注入新的 action knowledge（creating）**。
13	
14	## Paper 主数值基准（image_mean 聚合，公平对比）
15	
16	| Model / Condition | RSA (image_mean) | Notes |
17	|---|---|---|
18	| **SigLIP+Projector** | **0.615** | Smoking gun, LLM input |
19	| VLA trained with-inst | 0.501 | Peak L23 |
20	| VLA untrained with-inst | 0.485 | Peak L23 |
21	| VLA trained no-inst | 0.501 | Peak L23, identical to with-inst |
22	| VLA untrained no-inst | 0.482 | Peak L29 |
23	| **CLIP ViT-L/14** | **0.557** | VL-pretrained control, CI=[0.442, 0.660] |
24	| DINO-V2 | 0.388 | Vision-only baseline |
25	
26	last_preaction 数值（trained 0.488, untrained 0.485）放 supplementary 作为 robustness check。
27	
28	## Functional Probe 数值基准
29	
30	### Raw Action Prediction R² (统一超参: 50ep/patience5/lr1e-3/hidden256/seed42)
31	
32	| Model | mean_R² | Notes |
33	|---|---|---|
34	| **VLA Trained last_preaction L19** | **0.671** | readout concentration, > projector (p=0.002) |
35	| DINO-V2 cls | 0.634 | ≈ projector (p=0.557, n.s.) |
36	| **SigLIP+Projector** | **0.630** | ≈ DINO |
37	| VLA Trained image_mean L19 | 0.599 | < projector (p<0.001) |
38	| CLIP ViT-L/14 cls | 0.587 | < projector (p<0.001), < DINO (p<0.001) |
39	
40	**Ordering**: last_preaction (0.671) > DINO (0.634) ≈ Projector (0.630) > image_mean (0.599) > CLIP (0.587)
41	
42	**重要发现 — Geometric-Functional Dissociation（比预期更极端）**:
43	- RSA 排序: SigLIP (0.615) > CLIP (0.557) >> DINO (0.388) — VL pretraining 提高几何对齐
44	- R² 排序: DINO (0.634) ≈ Projector (0.630) > CLIP (0.587) — VL pretraining **降低**预测能力
45	- **RSA 和 R² 方向相反**：CLIP 高几何低预测，DINO 低几何高预测
46	- 结论：geometric alignment（表征结构匹配 action 空间）与 predictive capacity（probe 可解码性）是**可分离的独立维度**。VL pretraining 选择性提供 geometric alignment，但不增加甚至略降低 functional capacity。
47	- Redistribution 不变：last_preaction > all others 确认 LLM routing 有效
48	
49	注：所有 probe 统一预测 a_{t+1}（已验证，无 target 差异问题）。论文主表（5-model 对比）用 unified_action_probe 数字。Untrained/trained 对比 + delta probes 用 p0_probe_v2（同一 target，内部一致）。两组 R² 绝对值不同是超参/数据处理差异，不影响组内排序和结论。
50	
51	### Action-Delta Prediction R²
52	
53	| Model | mean_R² | Notes |
54	|---|---|---|
55	| VLA Trained image_mean L14 | 0.122 | |
56	| SigLIP+Projector | 0.118 | ≈ LLM, CI includes 0 (p=0.04) |
57	| Untrained image_mean L0 | 0.117 | ≈ projector ≈ LLM |
58	| DINO (LIBERO-Goal) | 0.100 | action_delta probe from v2 |
59	| DINO (MVP-2 LIBERO-10) | 0.061 | 2× lower than projector/LLM |
60	
61	**Delta 维度结论**：三者几乎相同（~0.12），远 > DINO (0.06-0.10)。支持 vision encoder dominance（所有 action-delta info 追溯到 SigLIP）。Delta last_preaction 缺失（待补）。
62	
63	### 聚合口径依赖性（论文必须如实讨论）
64	
65	| Comparison | image_mean | last_preaction |
66	|---|---|---|
67	| Raw action: Proj vs LLM | Proj wins (+0.023, CI=[0.011, 0.037], p=0.001) | LLM wins (+0.025, p=0.001) |
68	| Delta: Proj vs LLM | ≈ tie (−0.003, CI includes 0) | TBD |
69	
70	主文用 image_mean（公平聚合），last_preaction 放 supplementary。但必须讨论聚合口径对结论的影响。
71	
72	## Story Spine
73	
74	- **Problem**: VLAs 通过 fine-tuning LLM on robot data 实现 impressive performance，但 action-relevant 表征从何而来？业界隐性假设 fine-tuning 注入 new representational knowledge，但无系统性验证。
75	- **Existing approaches & gaps**: Grant et al. 2026 从 behavioral level 发现 visual pathway dominates，但未做 representational decomposition。无人测量过 VLA 各组件（vision encoder / projector / LLM）对 action-relevant 表征结构的独立贡献。
76	- **Our framing**: 首次对 VLA 进行系统性 representational + functional analysis——组件级分解 + per-layer probing + action prediction probes，定量揭示 action-relevant 结构的来源和 LLM 对其的变换。发现 vision encoder 是 action information 的通用源头（DINO ≈ SigLIP in R²，但 VL pretraining 赋予 geometric alignment）。LLM 降解分布式 image token 表征但通过**训练依赖的** attention 机制将信号聚合到 readout token——training 教会 routing 而非 creating new knowledge。
77	- **Headline result**: "The frozen vision encoder provides action-relevant representations (RSA ρ=0.615, action probe R²=0.706) that the LLM degrades at the image-token level (R²→0.683) but reconcentrates into a readout token (R²=0.731). This reconcentration is training-dependent (untrained readout R²=0.686 < projector 0.706), while distributed representation structure remains training-invariant (image_mean RSA: trained 0.501 ≈ untrained 0.485, p=0.20). Language instructions affect neither."
78	- **✅ All core evidence complete.** P1 remaining: plan_012 CLIP-ViT control, plan_010 LIBERO-Spatial (P2).
79	
80	## Anticipated Reviewer Concerns & Responses
81	
82	### C1: 单一 VLA 架构（OpenVLA）泛化性
83	- **应对**: Scope 明确限定为 "OpenVLA-class architecture"。OpenVLA 是最广泛使用的开源 VLA 之一，findings 对该架构族直接适用。Discussion 中讨论扩展到其他架构的预期。
84	- **实验**: 无需额外实验，Limitations 明确标注。
85	
86	### C2: SigLIP vs DINOv2 pretraining confound
87	- **问题**: SigLIP 是 image-text contrastive pretrained，DINOv2 是 self-supervised。RSA gap 可能来自 language-aware pretraining 而非纯 vision encoder 质量。
88	- **应对**: 这个 confound 实际上 **强化** 我们的 story——如果 gap 来自 SigLIP 的 vision-language pretraining，说明 pretraining 阶段的 language grounding 远比 task-specific fine-tuning 重要。Discussion 正面讨论此 confound 并将其转化为 insight。新发现加强此论点：DINO 与 Projector 在 action R² 上无差异（0.712 vs 0.706, p=0.22），但 RSA 几何差异显著（0.388 vs 0.615）。说明 VL pretraining 的贡献在于 geometric alignment 而非 information content。
89	- **实验**: ✅ plan_012 CLIP-ViT control Done。CLIP RSA=0.557, 远高于 DINO (0.388), 接近 SigLIP+projector (0.615)。确认 VL pretraining 是关键因素，非 SigLIP 独有。CLIP action probe R² 待补。
90	
91	### C3: LLM 对 action structure 的作用机制
92	- **问题**: LLM 到底做了什么？为什么 image token RSA 降低？
93	- **应对**: Functional probe 揭示机制——LLM 降解分布式 image token 表征（R² 0.706→0.683, bootstrap CI=[0.011, 0.037]）但通过 self-attention 将 action 信号 concentrate 到 readout token（R² 0.731）。这是 next-token prediction architecture 的自然行为：信息从 context tokens 流向 prediction position。Per-layer curve 的非单调模式（中间层部分恢复）与此一致。
94	- **实验**: ✅ plan_011 functional probe (Done) + plan_003 per-layer curve (Done)。
95	
96	### C4: Grant 2026 checkpoint 差异
97	- **问题**: Grant 用 OFT fine-tuned，我们用 standard fine-tuning checkpoint。
98	- **应对**: 我们用 standard fine-tuning 是更强的测试——如果完全不同的 LLM 权重（random init vs pretrained+finetuned，cos_sim≈0.2）都不改变表征，OFT 更不会。Related Work 明确区分。
99	
100	### C5: Practical implications / 功能验证
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "54e46029-5ce8-4a50-9c28-3bdf93dde879",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md",
      "content": "# Paper Framing — vla-ssd\n\n## Target Venue\n- Primary: CoRL 2026\n- Deadline: Abstract May 26, Paper May 29\n- Format: 8 pages + references\n\n## Core Claims (3 条)\n\n1. **Vision Encoder Dominance + Geometric-Functional Dissociation**: VLA 中 action-relevant 表征结构由 frozen vision encoder 决定。RSA geometric alignment: SigLIP (0.615) > CLIP (0.557) >> DINO (0.388)——VL pretrained encoders 显著优于 vision-only。但 functional capacity (R²) 方向相反: DINO (0.634) ≈ Projector (0.630) > CLIP (0.587)。**Geometric alignment 和 predictive capacity 是可分离的独立维度**。VL pretraining 提供 geometric alignment（表征结构匹配 action 空间），不增加甚至略降低 functional capacity。\n2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM 降解 distributed image token 的 **geometric alignment**（RSA: 0.615→0.501）和 functional capacity（R²: 0.630→0.599, p<0.001），但 global structure 保留（CKA 单调上升）。**训练后** LLM 学会将 action 信号 concentrate 到 readout token（trained R²=0.671 > projector 0.630, p=0.002），但 **untrained LLM 做不到**（untrained readout best=0.686 < projector）。Readout concentration 是 learned behavior，不是架构固有属性。\n3. **Training: Routing Without Creating**: VLA fine-tuning 不改变 distributed representation structure（image_mean RSA: trained 0.501 ≈ untrained 0.485, bootstrap CI includes 0, p=0.20），但提升 readout concentration（trained last_preaction 0.731 >> untrained 0.686，Δ=0.045, bootstrap CI=[0.032, 0.058], p<0.0001）。Instruction input 对两者均无影响。综合解读：**Training 的贡献是学习信息路由（routing），而非注入新的 action knowledge（creating）**。\n\n## Paper 主数值基准（image_mean 聚合，公平对比）\n\n| Model / Condition | RSA (image_mean) | Notes |\n|---|---|---|\n| **SigLIP+Projector** | **0.615** | Smoking gun, LLM input |\n| VLA trained with-inst | 0.501 | Peak L23 |\n| VLA untrained with-inst | 0.485 | Peak L23 |\n| VLA trained no-inst | 0.501 | Peak L23, identical to with-inst |\n| VLA untrained no-inst | 0.482 | Peak L29 |\n| **CLIP ViT-L/14** | **0.557** | VL-pretrained control, CI=[0.442, 0.660] |\n| DINO-V2 | 0.388 | Vision-only baseline |\n\nlast_preaction 数值（trained 0.488, untrained 0.485）放 supplementary 作为 robustness check。\n\n## Functional Probe 数值基准\n\n### Raw Action Prediction R² (统一超参: 50ep/patience5/lr1e-3/hidden256/seed42)\n\n| Model | mean_R² | Notes |\n|---|---|---|\n| **VLA Trained last_preaction L19** | **0.671** | readout concentration, > projector (p=0.002) |\n| DINO-V2 cls | 0.634 | ≈ projector (p=0.557, n.s.) |\n| **SigLIP+Projector** | **0.630** | ≈ DINO |\n| VLA Trained image_mean L19 | 0.599 | < projector (p<0.001) |\n| CLIP ViT-L/14 cls | 0.587 | < projector (p<0.001), < DINO (p<0.001) |\n\n**Ordering**: last_preaction (0.671) > DINO (0.634) ≈ Projector (0.630) > image_mean (0.599) > CLIP (0.587)\n\n**重要发现 — Geometric-Functional Dissociation（比预期更极端）**:\n- RSA 排序: SigLIP (0.615) > CLIP (0.557) >> DINO (0.388) — VL pretraining 提高几何对齐\n- R² 排序: DINO (0.634) ≈ Projector (0.630) > CLIP (0.587) — VL pretraining **降低**预测能力\n- **RSA 和 R² 方向相反**：CLIP 高几何低预测，DINO 低几何高预测\n- 结论：geometric alignment（表征结构匹配 action 空间）与 predictive capacity（probe 可解码性）是**可分离的独立维度**。VL pretraining 选择性提供 geometric alignment，但不增加甚至略降低 functional capacity。\n- Redistribution 不变：last_preaction > all others 确认 LLM routing 有效\n\n注：所有 probe 统一预测 a_{t+1}（已验证，无 target 差异问题）。论文主表（5-model 对比）用 unified_action_probe 数字。Untrained/trained 对比 + delta probes 用 p0_probe_v2（同一 target，内部一致）。两组 R² 绝对值不同是超参/数据处理差异，不影响组内排序和结论。\n\n### Action-Delta Prediction R²\n\n| Model | mean_R² | Notes |\n|---|---|---|\n| VLA Trained image_mean L14 | 0.122 | |\n| SigLIP+Projector | 0.118 | ≈ LLM, CI includes 0 (p=0.04) |\n| Untrained image_mean L0 | 0.117 | ≈ projector ≈ LLM |\n| DINO (LIBERO-Goal) | 0.100 | action_delta probe from v2 |\n| DINO (MVP-2 LIBERO-10) | 0.061 | 2× lower than projector/LLM |\n\n**Delta 维度结论**：三者几乎相同（~0.12），远 > DINO (0.06-0.10)。支持 vision encoder dominance（所有 action-delta info 追溯到 SigLIP）。Delta last_preaction 缺失（待补）。\n\n### 聚合口径依赖性（论文必须如实讨论）\n\n| Comparison | image_mean | last_preaction |\n|---|---|---|\n| Raw action: Proj vs LLM | Proj wins (+0.023, CI=[0.011, 0.037], p=0.001) | LLM wins (+0.025, p=0.001) |\n| Delta: Proj vs LLM | ≈ tie (−0.003, CI includes 0) | TBD |\n\n主文用 image_mean（公平聚合），last_preaction 放 supplementary。但必须讨论聚合口径对结论的影响。\n\n## Story Spine\n\n- **Problem**: VLAs 通过 fine-tuning LLM on robot data 实现 impressive performance，但 action-relevant 表征从何而来？业界隐性假设 fine-tuning 注入 new representational knowledge，但无系统性验证。\n- **Existing approaches & gaps**: Grant et al. 2026 从 behavioral level 发现 visual pathway dominates，但未做 representational decomposition。无人测量过 VLA 各组件（vision encoder / projector / LLM）对 action-relevant 表征结构的独立贡献。\n- **Our framing**: 首次对 VLA 进行系统性 representational + functional analysis——组件级分解 + per-layer probing + action prediction probes，定量揭示 action-relevant 结构的来源和 LLM 对其的变换。发现 vision encoder 是 action information 的通用源头（DINO ≈ SigLIP in R²，但 VL pretraining 赋予 geometric alignment）。LLM 降解分布式 image token 表征但通过**训练依赖的** attention 机制将信号聚合到 readout token——training 教会 routing 而非 creating new knowledge。\n- **Headline result**: \"The frozen vision encoder provides action-relevant representations (RSA ρ=0.615, action probe R²=0.706) that the LLM degrades at the image-token level (R²→0.683) but reconcentrates into a readout token (R²=0.731). This reconcentration is training-dependent (untrained readout R²=0.686 < projector 0.706), while distributed representation structure remains training-invariant (image_mean RSA: trained 0.501 ≈ untrained 0.485, p=0.20). Language instructions affect neither.\"\n- **✅ All core evidence complete.** P1 remaining: plan_012 CLIP-ViT control, plan_010 LIBERO-Spatial (P2).\n\n## Anticipated Reviewer Concerns & Responses\n\n### C1: 单一 VLA 架构（OpenVLA）泛化性\n- **应对**: Scope 明确限定为 \"OpenVLA-class architecture\"。OpenVLA 是最广泛使用的开源 VLA 之一，findings 对该架构族直接适用。Discussion 中讨论扩展到其他架构的预期。\n- **实验**: 无需额外实验，Limitations 明确标注。\n\n### C2: SigLIP vs DINOv2 pretraining confound\n- **问题**: SigLIP 是 image-text contrastive pretrained，DINOv2 是 self-supervised。RSA gap 可能来自 language-aware pretraining 而非纯 vision encoder 质量。\n- **应对**: 这个 confound 实际上 **强化** 我们的 story——如果 gap 来自 SigLIP 的 vision-language pretraining，说明 pretraining 阶段的 language grounding 远比 task-specific fine-tuning 重要。Discussion 正面讨论此 confound 并将其转化为 insight。新发现加强此论点：DINO 与 Projector 在 action R² 上无差异（0.712 vs 0.706, p=0.22），但 RSA 几何差异显著（0.388 vs 0.615）。说明 VL pretraining 的贡献在于 geometric alignment 而非 information content。\n- **实验**: ✅ plan_012 CLIP-ViT control Done。CLIP RSA=0.557, 远高于 DINO (0.388), 接近 SigLIP+projector (0.615)。确认 VL pretraining 是关键因素，非 SigLIP 独有。CLIP action probe R² 待补。\n\n### C3: LLM 对 action structure 的作用机制\n- **问题**: LLM 到底做了什么？为什么 image token RSA 降低？\n- **应对**: Functional probe 揭示机制——LLM 降解分布式 image token 表征（R² 0.706→0.683, bootstrap CI=[0.011, 0.037]）但通过 self-attention 将 action 信号 concentrate 到 readout token（R² 0.731）。这是 next-token prediction architecture 的自然行为：信息从 context tokens 流向 prediction position。Per-layer curve 的非单调模式（中间层部分恢复）与此一致。\n- **实验**: ✅ plan_011 functional probe (Done) + plan_003 per-layer curve (Done)。\n\n### C4: Grant 2026 checkpoint 差异\n- **问题**: Grant 用 OFT fine-tuned，我们用 standard fine-tuning checkpoint。\n- **应对**: 我们用 standard fine-tuning 是更强的测试——如果完全不同的 LLM 权重（random init vs pretrained+finetuned，cos_sim≈0.2）都不改变表征，OFT 更不会。Related Work 明确区分。\n\n### C5: Practical implications / 功能验证",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 159
    }
  }
}
```

</details>

---

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough context. Let me also check the p0_probe_v2 numbers mentioned in the task — the task says to use those for headline numbers: projector R²=0.706, image_mean R²=0.683, readout R²=0.731, untrained readout R²=0.686. These match the experiments.tex table. The paper_framing.md mentions two sets of numbers (unified_action_probe vs p0_probe_v2), and the task instructs me to use p0_probe_v2 numbers, which are the ones in experiments.tex.


Now I'll start drafting the introduction section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "d6489c1a-0f0e-4b02-8713-630a77e3a9db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CbxPmuCVV9kWYCs8kfumx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3688,
      "cache_read_input_tokens": 31544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3688
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

_source line 48_

Now writing the introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "6b5ba7b8-6790-4614-b5ed-83363696377d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CbxPmuCVV9kWYCs8kfumx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3688,
      "cache_read_input_tokens": 31544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3688
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

_source line 49_

<details open><summary>🔧 Tool call — Write · `toolu_01Nm35aVAfPf72RcDBkdBRxa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nVision-language-action models (VLAs) achieve impressive robotic manipulation performance by fine-tuning large language models on robot demonstration data~\\cite{brohan2023_rt2,kim2024_openvla}.\nThe dominant architecture grafts a frozen vision encoder onto a pretrained LLM backbone, then fine-tunes the system end-to-end to map visual observations and language instructions to continuous actions~\\cite{karamcheti2024}.\nAn implicit assumption underlies this paradigm: fine-tuning injects action-relevant representational knowledge into the LLM.\nBut where do action representations actually come from?\nDo they originate in the vision encoder's pretrained features, emerge through LLM processing, or arise from task-specific fine-tuning?\n\nRecent work reveals cracks in this assumption.\nGrant et al.~\\cite{grant2026} showed that the visual pathway dominates action generation across multiple VLA architectures, with ablations to the language stream producing minimal behavioral degradation.\nIndependently, Hou et al.~\\cite{hou2026} and Fei et al.~\\cite{fei2025} demonstrated that VLAs largely ignore language instructions during policy execution.\nThese findings challenge the prevailing narrative but remain at the behavioral level---they reveal \\emph{what} drives VLA outputs without explaining \\emph{where} action-relevant structure resides in the representation space.\nNo prior work has performed a representational decomposition that measures each component's independent contribution to action-relevant structure.\nWithout this, we cannot determine whether fine-tuning truly injects action knowledge or merely learns to route pre-existing structure.\n\nWe present the first systematic representational and functional analysis of a VLA.\nTaking OpenVLA-7B~\\cite{kim2024_openvla} as a case study, we decompose its processing pipeline into constituent components: the frozen SigLIP vision encoder~\\cite{zhai2023_siglip} with MLP projector, every layer of the Llama-2 7B backbone, and the readout token position.\nWe apply Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to measure geometric alignment with the action space and train functional probes to measure action decodability.\nA $2 \\times 2$ factorial design crossing training status (trained vs.\\ untrained LLM) with instruction presence (with vs.\\ without) isolates each factor's contribution.\nExternal baselines---DINOv2~\\cite{oquab2024_dinov2} (vision-only) and CLIP ViT-L/14~\\cite{radford2021_clip} (vision-language pretrained, no VLA training)---anchor our comparisons.\n\nThree findings emerge from experiments on the LIBERO-Goal benchmark~\\cite{liu2023_libero}.\n\\textbf{First}, frozen vision-language encoders provide the dominant action-relevant geometric structure.\nSigLIP+Projector achieves the highest action-space alignment (RSA $\\rho = 0.615$), followed by CLIP ($\\rho = 0.557$), both far exceeding the vision-only DINOv2 ($\\rho = 0.388$).\nYet DINOv2 matches SigLIP+Projector in action prediction capacity ($R^2 = 0.712$ vs.\\ $0.706$, $p = 0.22$), revealing a geometric-functional dissociation: VL pretraining provides geometric alignment with the action space without increasing raw decodability.\n\\textbf{Second}, the LLM degrades distributed geometric alignment (RSA $0.615 \\to 0.501$) but concentrates a functionally superior signal at the readout token ($R^2 = 0.731$, exceeding the projector's $0.706$).\nThis concentration is training-dependent: an untrained LLM's readout achieves only $R^2 = 0.686$, falling below the projector baseline.\n\\textbf{Third}, training teaches routing, not creating.\nDistributed RSA is training-invariant ($\\Delta = 0.021$, 95\\% CI includes zero, $p = 0.20$), while readout concentration shows a large training effect ($\\Delta = 0.045$, $p < 0.0001$).\nLanguage instructions affect neither metric.\n\nThese results reframe how we understand VLA representations and carry direct design implications: vision encoder pretraining quality---not LLM fine-tuning---is the primary lever for action-relevant structure~\\cite{haon2025}.\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item The first systematic representational decomposition of a VLA, quantifying each component's contribution to action-relevant structure with both geometric (RSA) and functional (probe $R^2$) metrics.\n    \\item Discovery of a geometric-functional dissociation: vision-language pretraining provides geometric alignment with the action space beyond what raw information content predicts, while vision-only features are functionally rich but geometrically dissimilar.\n    \\item Evidence that LLM fine-tuning teaches information routing---concentrating pre-existing vision-encoder structure at the readout position---rather than creating new action-relevant representations.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "b7d4651f-34ab-4da8-8282-a2531e0a1cd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CbxPmuCVV9kWYCs8kfumx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3688,
      "cache_read_input_tokens": 31544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3688
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

_source line 50 · 2026-05-16T02:29:58.798Z_

<details><summary>↩ Tool result · `toolu_01Nm35aVAfPf72RcDBkdBRxa`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "309ac412-2137-4766-ad96-9bded87d828b",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nVision-language-action models (VLAs) achieve impressive robotic manipulation performance by fine-tuning large language models on robot demonstration data~\\cite{brohan2023_rt2,kim2024_openvla}.\nThe dominant architecture grafts a frozen vision encoder onto a pretrained LLM backbone, then fine-tunes the system end-to-end to map visual observations and language instructions to continuous actions~\\cite{karamcheti2024}.\nAn implicit assumption underlies this paradigm: fine-tuning injects action-relevant representational knowledge into the LLM.\nBut where do action representations actually come from?\nDo they originate in the vision encoder's pretrained features, emerge through LLM processing, or arise from task-specific fine-tuning?\n\nRecent work reveals cracks in this assumption.\nGrant et al.~\\cite{grant2026} showed that the visual pathway dominates action generation across multiple VLA architectures, with ablations to the language stream producing minimal behavioral degradation.\nIndependently, Hou et al.~\\cite{hou2026} and Fei et al.~\\cite{fei2025} demonstrated that VLAs largely ignore language instructions during policy execution.\nThese findings challenge the prevailing narrative but remain at the behavioral level---they reveal \\emph{what} drives VLA outputs without explaining \\emph{where} action-relevant structure resides in the representation space.\nNo prior work has performed a representational decomposition that measures each component's independent contribution to action-relevant structure.\nWithout this, we cannot determine whether fine-tuning truly injects action knowledge or merely learns to route pre-existing structure.\n\nWe present the first systematic representational and functional analysis of a VLA.\nTaking OpenVLA-7B~\\cite{kim2024_openvla} as a case study, we decompose its processing pipeline into constituent components: the frozen SigLIP vision encoder~\\cite{zhai2023_siglip} with MLP projector, every layer of the Llama-2 7B backbone, and the readout token position.\nWe apply Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to measure geometric alignment with the action space and train functional probes to measure action decodability.\nA $2 \\times 2$ factorial design crossing training status (trained vs.\\ untrained LLM) with instruction presence (with vs.\\ without) isolates each factor's contribution.\nExternal baselines---DINOv2~\\cite{oquab2024_dinov2} (vision-only) and CLIP ViT-L/14~\\cite{radford2021_clip} (vision-language pretrained, no VLA training)---anchor our comparisons.\n\nThree findings emerge from experiments on the LIBERO-Goal benchmark~\\cite{liu2023_libero}.\n\\textbf{First}, frozen vision-language encoders provide the dominant action-relevant geometric structure.\nSigLIP+Projector achieves the highest action-space alignment (RSA $\\rho = 0.615$), followed by CLIP ($\\rho = 0.557$), both far exceeding the vision-only DINOv2 ($\\rho = 0.388$).\nYet DINOv2 matches SigLIP+Projector in action prediction capacity ($R^2 = 0.712$ vs.\\ $0.706$, $p = 0.22$), revealing a geometric-functional dissociation: VL pretraining provides geometric alignment with the action space without increasing raw decodability.\n\\textbf{Second}, the LLM degrades distributed geometric alignment (RSA $0.615 \\to 0.501$) but concentrates a functionally superior signal at the readout token ($R^2 = 0.731$, exceeding the projector's $0.706$).\nThis concentration is training-dependent: an untrained LLM's readout achieves only $R^2 = 0.686$, falling below the projector baseline.\n\\textbf{Third}, training teaches routing, not creating.\nDistributed RSA is training-invariant ($\\Delta = 0.021$, 95\\% CI includes zero, $p = 0.20$), while readout concentration shows a large training effect ($\\Delta = 0.045$, $p < 0.0001$).\nLanguage instructions affect neither metric.\n\nThese results reframe how we understand VLA representations and carry direct design implications: vision encoder pretraining quality---not LLM fine-tuning---is the primary lever for action-relevant structure~\\cite{haon2025}.\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item The first systematic representational decomposition of a VLA, quantifying each component's contribution to action-relevant structure with both geometric (RSA) and functional (probe $R^2$) metrics.\n    \\item Discovery of a geometric-functional dissociation: vision-language pretraining provides geometric alignment with the action space beyond what raw information content predicts, while vision-only features are functionally rich but geometrically dissimilar.\n    \\item Evidence that LLM fine-tuning teaches information routing---concentrating pre-existing vision-encoder structure at the readout position---rather than creating new action-relevant representations.\n\\end{enumerate}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01P66JvKByFHBVFepYfDGiNY`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "5f58f789-a223-4cfb-9420-02ab004d3443",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWa8QDpNFoxpMFeq3n3Lgg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 35232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1583
      },
      "output_tokens": 44,
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

_source line 52 · 2026-05-16T02:30:02.158Z_

<details><summary>↩ Tool result · `toolu_01P66JvKByFHBVFepYfDGiNY`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "b44fbe77-3a2a-4cda-8c57-1b65e588be3a",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool only allows writing to memory.md, writing_plan.yaml, paper_framing.md. It won't work for registering artifacts. Let me search for the register_artifact tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "7c8ab802-5511-4499-aa13-b42f33ba3b0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Zzo5ptJsU4m7PSW1Cnc83",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 36815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
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

_source line 54_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RHM1HEt4DXcSRLjnHumni7`</summary>

```json
{
  "query": "register_artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "5cb4c76e-cb46-4e36-b300-9e2c61d6c055",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Zzo5ptJsU4m7PSW1Cnc83",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 36815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
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

_source line 55 · 2026-05-16T02:30:06.157Z_

<details><summary>↩ Tool result · `toolu_01RHM1HEt4DXcSRLjnHumni7`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "bb0e1a7e-f8e9-4bb3-9ad3-ea43f8c131fd",
  "tool_use_result": {
    "matches": [],
    "query": "register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DF1vxg3PeK9SyEXg4FUTUX`</summary>

```json
{
  "query": "artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "269c7a23-d05d-46ee-89ee-11f5b5afbf99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiLgtwxz2RH7ZKSm8SZQfK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 156,
      "cache_read_input_tokens": 37178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 156
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

_source line 57 · 2026-05-16T02:30:09.301Z_

<details><summary>↩ Tool result · `toolu_01DF1vxg3PeK9SyEXg4FUTUX`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "542b34fc-ea19-4d8f-9373-b6d98d448a9c",
  "tool_use_result": {
    "matches": [],
    "query": "artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019gJiWV3FKShiLYQq5Nwvkg`</summary>

```json
{
  "query": "mcp agent-ml-research",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "0db16dc9-41ca-4e4e-914c-1c00319891c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017wqDCrRvqvaX92DWy5HUjZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 37334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 90
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

_source line 59 · 2026-05-16T02:30:12.116Z_

<details><summary>↩ Tool result · `toolu_019gJiWV3FKShiLYQq5Nwvkg`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "ListMcpResourcesTool"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "ReadMcpResourceTool"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
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
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "4c820c78-f05b-4a9b-8762-319cad0cdaed",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "ListMcpResourcesTool",
      "ReadMcpResourceTool",
      "WebFetch"
    ],
    "query": "mcp agent-ml-research",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 60_

`register_artifact` not available as an MCP tool. File already written. Let me verify the output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "796d55e4-fc49-4a3b-b97c-b17a4e34dd98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTqZPGKbYd1duLbvMDwwmD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 37424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1790
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

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_018Dv4dUHpoz5nZ7UiZ7zPAc`</summary>

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
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "6546fbb9-663f-4d92-a9fc-e343b36999c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTqZPGKbYd1duLbvMDwwmD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 37424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1790
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

_source line 62 · 2026-05-16T02:30:15.275Z_

<details><summary>↩ Tool result · `toolu_018Dv4dUHpoz5nZ7UiZ7zPAc`</summary>

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
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "5dbff09f-02c5-49b1-8721-088cd154fe15",
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

### Assistant

_source line 63_

`introduction.tex` 已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex`。

5 段结构：Problem → Gap → Approach → Findings (with headline numbers) → Implications + 3 contributions（enumerate）。约 ~650 词，符合 1-1.5 页目标。所有引用 key 均按指定使用，包括 `hou2026` 和 `fei2025`。数值用 p0_probe_v2 口径（R² 0.706/0.683/0.731/0.686，RSA 0.615/0.557/0.388）。

`register_artifact` 工具不在当前可用 MCP 工具列表中，无法注册。如需注册请手动操作或确认工具名称。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "uuid": "1f7b5634-a0d0-46a7-8455-ad9fddd7966f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GFFNiUPKETjgKhG61ywdN4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1471,
      "cache_read_input_tokens": 39214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1471
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

_source line 64_

`introduction.tex` 已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/introduction.tex`。

5 段结构：Problem → Gap → Approach → Findings (with headline numbers) → Implications + 3 contributions（enumerate）。约 ~650 词，符合 1-1.5 页目标。所有引用 key 均按指定使用，包括 `hou2026` 和 `fei2025`。数值用 p0_probe_v2 口径（R² 0.706/0.683/0.731/0.686，RSA 0.615/0.557/0.388）。

`register_artifact` 工具不在当前可用 MCP 工具列表中，无法注册。如需注册请手动操作或确认工具名称。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 97856,
  "duration_api_ms": 99004,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "967a45e7-b14e-4dce-8ee2-80af86a0922a",
  "total_cost_usd": 0.47331989999999996,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 28844,
    "cache_read_input_tokens": 320894,
    "output_tokens": 2785,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 28844,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 235,
        "cache_read_input_tokens": 39214,
        "cache_creation_input_tokens": 1471,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1471
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2498,
      "outputTokens": 2385,
      "cacheReadInputTokens": 68499,
      "cacheCreationInputTokens": 33296,
      "webSearchRequests": 0,
      "costUSD": 0.0628929,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 2785,
      "cacheReadInputTokens": 320894,
      "cacheCreationInputTokens": 28844,
      "webSearchRequests": 0,
      "costUSD": 0.41042700000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e9946522-93d8-41cc-9f87-f07b87b8a317"
}
```

</details>

---
