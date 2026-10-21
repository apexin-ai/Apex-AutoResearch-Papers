# paper writing method

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_writing_method_20260516T022801.log`
- **Structured JSON:** [`a9625b5c344822e24ef6.json`](../../sessions/a9/a9625b5c344822e24ef6.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
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
  "uuid": "8ebcb2ad-4573-4a27-9b9b-1ec775965ada",
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
  "uuid": "d896e521-9576-4f54-9c74-c3bfa4bea6fc",
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the existing experiments.tex to ensure terminology consistency, and also check if there's already a method.tex file or other paper files for context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "fb0e8f84-ef0b-4fd8-9c31-f9d6d46308f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118c7chiRTFias2bP4UDrah",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
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

<details open><summary>🔧 Tool call — Read · `toolu_019RKTEMCDepkcTRMh69eBNg`</summary>

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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "df1b69c5-875b-4ad2-be6d-3776c04c8bae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118c7chiRTFias2bP4UDrah",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
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

_source line 6 · 2026-05-16T02:28:11.083Z_

<details><summary>↩ Tool result · `toolu_019RKTEMCDepkcTRMh69eBNg`</summary>

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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "ae7ef794-3c64-45a4-a68b-58af2ba6cebd",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01KrM9v7dmyRMRnQMX8ipdoi`</summary>

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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "ded8ac56-1e83-49f2-907d-ee62e86801ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118c7chiRTFias2bP4UDrah",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
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

_source line 8 · 2026-05-16T02:28:11.345Z_

<details><summary>↩ Tool result · `toolu_01KrM9v7dmyRMRnQMX8ipdoi`</summary>

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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "856fcf55-4524-4099-913e-471199d1e8eb",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/experiments.tex"
    ],
    "durationMs": 6,
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
Now I have a clear picture of the experiments.tex terminology and style. Let me write the method.tex file, ensuring consistency with the experiments section. Key things to maintain:

1. Citation keys: kim2024_openvla, karamcheti2024, liu2023_libero, oquab2024_dinov2, radford2021_clip, zhai2023_siglip, kriegeskorte2008, alain2017, kornblith2019
2. Terminology: SigLIP+Projector, image_mean, last_preaction, cls_token, patch_mean, trained/untrained, with/without instruction


3. Style: \paragraph{} for sub-subsections, academic English, concise

Now I'll draft the method section with these constraints in mind.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "59f2f971-f903-49c6-9156-c9a7814fe684",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMsyAKGhKLAvrRgJU8teQ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5438,
      "cache_read_input_tokens": 23962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5438
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

Now I'll write the method.tex and register it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "6dd1b39a-7c31-44a0-9e0d-253572f0a31b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMsyAKGhKLAvrRgJU8teQ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5438,
      "cache_read_input_tokens": 23962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5438
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

<details open><summary>🔧 Tool call — Write · `toolu_01Ad6ZQ8KNhVyekQRY88X8nV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate where action-relevant representations originate within a vision-language-action (VLA) model by combining representational similarity analysis, functional probing, and kernel alignment across a factorial design of training and instruction conditions.\n\n\\subsection{Model and Data}\n\\label{sec:model_data}\n\n\\paragraph{Architecture.}\nWe study OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a VLA model comprising four components: (1)~a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip} that maps RGB observations to patch-level visual tokens, (2)~an MLP projector that maps vision tokens into the language model's embedding space, (3)~a Llama-2 7B language backbone (32 transformer layers) that processes the concatenated sequence of projected image tokens and tokenized language instructions, and (4)~an action head that decodes 7-dimensional continuous actions (3D translation, 3D rotation, 1D gripper) from the final hidden states.\n\n\\paragraph{Training data.}\nWe fine-tune OpenVLA on the LIBERO-10 split~\\cite{liu2023_libero}, which contains 10 tabletop manipulation tasks with 50 human demonstrations each (500 demonstrations total).\nWe evaluate generalization on LIBERO-Goal, an out-of-distribution benchmark where episodes share initial object configurations but differ in goal specifications.\n\n\\paragraph{Untrained control.}\nTo isolate the LLM's learned contribution from the vision encoder's pretrained geometry, we construct an untrained control by calling \\texttt{from\\_config()} to reinitialize all LLM parameters (6.74B weights drawn from random initialization) while preserving the frozen SigLIP encoder (0.80B pretrained weights).\nThe untrained model processes identical visual inputs through an identical vision encoder but lacks any learned language or action structure in its LLM layers.\n\n\\subsection{Representation Extraction}\n\\label{sec:rep_extraction}\n\nWe extract representations from five sources spanning the VLA processing pipeline and two external baselines:\n\n\\begin{enumerate}[label=(\\alph*),nosep,leftmargin=*]\n    \\item \\textbf{SigLIP+Projector} --- the vision encoder output after MLP projection into the LLM's input space, before any LLM processing. This captures the representation that the LLM receives as input.\n    \\item \\textbf{LLM image\\_mean} --- the mean activation across all image token positions at each of the 32 LLM layers. This captures how the LLM transforms distributed visual information through its depth.\n    \\item \\textbf{LLM last\\_preaction} --- the activation at the final token position before action decoding (the readout token) at each LLM layer. This captures the representation from which actions are directly decoded.\n    \\item \\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token} --- a vision-only baseline pretrained with self-supervised objectives and no language supervision.\n    \\item \\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean} --- a vision-language baseline pretrained on image-text pairs, serving as a generalization control for VL pretraining effects independent of the VLA pipeline.\n\\end{enumerate}\n\nSources (a)--(c) probe representations within the VLA model itself, while (d) and (e) provide external references with no VLA training signal.\n\n\\paragraph{Factorial design.}\nWe cross two factors in a $2 \\times 2$ design: \\emph{training status} (trained vs.\\ untrained LLM) and \\emph{instruction presence} (with vs.\\ without language instruction).\nThis yields four conditions per LLM representation source, enabling us to disentangle the contributions of LLM training and language grounding to action-relevant structure.\nExternal baselines (d) and (e) are evaluated once, as they are independent of both factors.\n\n\\subsection{Representational Similarity Analysis}\n\\label{sec:rsa}\n\nWe adopt Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to quantify the geometric alignment between neural representations and the action space.\n\n\\paragraph{Representational dissimilarity matrices.}\nFor a set of $n$ observations, we compute an $n \\times n$ representational dissimilarity matrix (RDM) for each representation source using Euclidean distance between representation vectors.\nWe similarly construct an action RDM from the 7-dimensional action vectors.\n\n\\paragraph{RSA correlation.}\nWe measure alignment between a representation RDM and the action RDM via Spearman rank correlation $\\rho$ between their upper-triangular elements.\nHigher $\\rho$ indicates that observations with similar representations also have similar actions, i.e., the representation geometry mirrors the action space geometry.\n\n\\paragraph{Statistical inference.}\nWe compute 95\\% confidence intervals from 10{,}000 bootstrap resamples of observation pairs for all pairwise comparisons.\nRSA is computed per task and aggregated across the 10 tasks.\n\n\\subsection{Functional Action Probes}\n\\label{sec:probes}\n\nRSA measures geometric alignment but does not assess whether action information is linearly decodable from representations.\nWe complement RSA with functional probing~\\cite{alain2017} to measure the action information accessible to a lightweight decoder.\n\n\\paragraph{Probe architecture.}\nWe train two-layer MLP probes (Linear $\\to$ ReLU $\\to$ Linear) mapping from the representation dimensionality to a 256-dimensional hidden layer and then to the 7-dimensional action space.\n\n\\paragraph{Training protocol.}\nProbes are optimized with Adam (learning rate $10^{-3}$, batch size 256) for 50 epochs with early stopping (patience 5 epochs on validation loss).\nRepresentations are frozen throughout; only probe parameters are updated.\nWe use per-task 80/20 train/validation splits and report mean $R^2$ across the 7 action dimensions as the primary metric.\n\n\\paragraph{Action-delta probes.}\nIn addition to predicting absolute actions $\\mathbf{a}_t$, we train probes to predict action deltas $\\Delta\\mathbf{a} = \\mathbf{a}_{t+1} - \\mathbf{a}_t$, which capture the dynamic component of action structure independent of the current action magnitude.\n\n\\paragraph{Statistical comparison.}\nWe use bootstrap paired comparison (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant.\n\n\\subsection{Centered Kernel Alignment}\n\\label{sec:cka}\n\nRSA captures local geometric alignment---whether pairwise distances in representation space mirror those in action space.\nTo assess global structural preservation, we additionally employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} in two variants.\n\n\\paragraph{Linear CKA.}\nLinear CKA computes the normalized Hilbert-Schmidt Independence Criterion between linear kernel matrices of two representation sets.\nIt is invariant to orthogonal transformations and isotropic scaling, making it sensitive to global structure rather than local distance preservation.\n\n\\paragraph{RDM kernel CKA.}\nWe also compute CKA using the RDMs themselves as kernel matrices, providing a bridge between the local sensitivity of RSA and the global perspective of linear CKA.\n\n\\paragraph{Dimensionality caveat.}\nWhen comparing high-dimensional representations (e.g., 4096-D LLM activations) with low-dimensional action vectors (7-D), linear CKA may be dominated by the few directions that span the action space, potentially inflating similarity estimates.\nWe report both CKA variants alongside RSA to ensure that conclusions are robust to metric choice.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "8c9d8ce9-8f62-47c0-87cd-cf7f3c25fd7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMsyAKGhKLAvrRgJU8teQ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5438,
      "cache_read_input_tokens": 23962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5438
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

_source line 12 · 2026-05-16T02:29:04.034Z_

<details><summary>↩ Tool result · `toolu_01Ad6ZQ8KNhVyekQRY88X8nV`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "4dfb9200-c8de-40d1-82e3-9efa13808c5f",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate where action-relevant representations originate within a vision-language-action (VLA) model by combining representational similarity analysis, functional probing, and kernel alignment across a factorial design of training and instruction conditions.\n\n\\subsection{Model and Data}\n\\label{sec:model_data}\n\n\\paragraph{Architecture.}\nWe study OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a VLA model comprising four components: (1)~a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip} that maps RGB observations to patch-level visual tokens, (2)~an MLP projector that maps vision tokens into the language model's embedding space, (3)~a Llama-2 7B language backbone (32 transformer layers) that processes the concatenated sequence of projected image tokens and tokenized language instructions, and (4)~an action head that decodes 7-dimensional continuous actions (3D translation, 3D rotation, 1D gripper) from the final hidden states.\n\n\\paragraph{Training data.}\nWe fine-tune OpenVLA on the LIBERO-10 split~\\cite{liu2023_libero}, which contains 10 tabletop manipulation tasks with 50 human demonstrations each (500 demonstrations total).\nWe evaluate generalization on LIBERO-Goal, an out-of-distribution benchmark where episodes share initial object configurations but differ in goal specifications.\n\n\\paragraph{Untrained control.}\nTo isolate the LLM's learned contribution from the vision encoder's pretrained geometry, we construct an untrained control by calling \\texttt{from\\_config()} to reinitialize all LLM parameters (6.74B weights drawn from random initialization) while preserving the frozen SigLIP encoder (0.80B pretrained weights).\nThe untrained model processes identical visual inputs through an identical vision encoder but lacks any learned language or action structure in its LLM layers.\n\n\\subsection{Representation Extraction}\n\\label{sec:rep_extraction}\n\nWe extract representations from five sources spanning the VLA processing pipeline and two external baselines:\n\n\\begin{enumerate}[label=(\\alph*),nosep,leftmargin=*]\n    \\item \\textbf{SigLIP+Projector} --- the vision encoder output after MLP projection into the LLM's input space, before any LLM processing. This captures the representation that the LLM receives as input.\n    \\item \\textbf{LLM image\\_mean} --- the mean activation across all image token positions at each of the 32 LLM layers. This captures how the LLM transforms distributed visual information through its depth.\n    \\item \\textbf{LLM last\\_preaction} --- the activation at the final token position before action decoding (the readout token) at each LLM layer. This captures the representation from which actions are directly decoded.\n    \\item \\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token} --- a vision-only baseline pretrained with self-supervised objectives and no language supervision.\n    \\item \\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean} --- a vision-language baseline pretrained on image-text pairs, serving as a generalization control for VL pretraining effects independent of the VLA pipeline.\n\\end{enumerate}\n\nSources (a)--(c) probe representations within the VLA model itself, while (d) and (e) provide external references with no VLA training signal.\n\n\\paragraph{Factorial design.}\nWe cross two factors in a $2 \\times 2$ design: \\emph{training status} (trained vs.\\ untrained LLM) and \\emph{instruction presence} (with vs.\\ without language instruction).\nThis yields four conditions per LLM representation source, enabling us to disentangle the contributions of LLM training and language grounding to action-relevant structure.\nExternal baselines (d) and (e) are evaluated once, as they are independent of both factors.\n\n\\subsection{Representational Similarity Analysis}\n\\label{sec:rsa}\n\nWe adopt Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to quantify the geometric alignment between neural representations and the action space.\n\n\\paragraph{Representational dissimilarity matrices.}\nFor a set of $n$ observations, we compute an $n \\times n$ representational dissimilarity matrix (RDM) for each representation source using Euclidean distance between representation vectors.\nWe similarly construct an action RDM from the 7-dimensional action vectors.\n\n\\paragraph{RSA correlation.}\nWe measure alignment between a representation RDM and the action RDM via Spearman rank correlation $\\rho$ between their upper-triangular elements.\nHigher $\\rho$ indicates that observations with similar representations also have similar actions, i.e., the representation geometry mirrors the action space geometry.\n\n\\paragraph{Statistical inference.}\nWe compute 95\\% confidence intervals from 10{,}000 bootstrap resamples of observation pairs for all pairwise comparisons.\nRSA is computed per task and aggregated across the 10 tasks.\n\n\\subsection{Functional Action Probes}\n\\label{sec:probes}\n\nRSA measures geometric alignment but does not assess whether action information is linearly decodable from representations.\nWe complement RSA with functional probing~\\cite{alain2017} to measure the action information accessible to a lightweight decoder.\n\n\\paragraph{Probe architecture.}\nWe train two-layer MLP probes (Linear $\\to$ ReLU $\\to$ Linear) mapping from the representation dimensionality to a 256-dimensional hidden layer and then to the 7-dimensional action space.\n\n\\paragraph{Training protocol.}\nProbes are optimized with Adam (learning rate $10^{-3}$, batch size 256) for 50 epochs with early stopping (patience 5 epochs on validation loss).\nRepresentations are frozen throughout; only probe parameters are updated.\nWe use per-task 80/20 train/validation splits and report mean $R^2$ across the 7 action dimensions as the primary metric.\n\n\\paragraph{Action-delta probes.}\nIn addition to predicting absolute actions $\\mathbf{a}_t$, we train probes to predict action deltas $\\Delta\\mathbf{a} = \\mathbf{a}_{t+1} - \\mathbf{a}_t$, which capture the dynamic component of action structure independent of the current action magnitude.\n\n\\paragraph{Statistical comparison.}\nWe use bootstrap paired comparison (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant.\n\n\\subsection{Centered Kernel Alignment}\n\\label{sec:cka}\n\nRSA captures local geometric alignment---whether pairwise distances in representation space mirror those in action space.\nTo assess global structural preservation, we additionally employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} in two variants.\n\n\\paragraph{Linear CKA.}\nLinear CKA computes the normalized Hilbert-Schmidt Independence Criterion between linear kernel matrices of two representation sets.\nIt is invariant to orthogonal transformations and isotropic scaling, making it sensitive to global structure rather than local distance preservation.\n\n\\paragraph{RDM kernel CKA.}\nWe also compute CKA using the RDMs themselves as kernel matrices, providing a bridge between the local sensitivity of RSA and the global perspective of linear CKA.\n\n\\paragraph{Dimensionality caveat.}\nWhen comparing high-dimensional representations (e.g., 4096-D LLM activations) with low-dimensional action vectors (7-D), linear CKA may be dominated by the few directions that span the action space, potentially inflating similarity estimates.\nWe report both CKA variants alongside RSA to ensure that conclusions are robust to metric choice.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016ou7T1pmNkjCS8P46PktgV`</summary>

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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "0a85372b-fce9-44f4-a999-24ded20ff1ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7z8Djb6mJW4rayGDVCLS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2257,
      "cache_read_input_tokens": 29400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2257
      },
      "output_tokens": 46,
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

_source line 14 · 2026-05-16T02:29:06.785Z_

<details><summary>↩ Tool result · `toolu_016ou7T1pmNkjCS8P46PktgV`</summary>

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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "7a5da55c-b3a7-40fb-9694-a33b21e3b04c",
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

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool only works for memory.md, writing_plan.yaml, paper_framing.md - not for registering artifacts. I need to find the register_artifact tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "d63d12e4-2016-457f-baaf-2677b8307a66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPEW4UPDcw9xr9ZzYAHMLL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 31657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
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

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JbFd3KTvYjqFAsAUWfkTBh`</summary>

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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "8785ede6-4fc2-4faa-81ff-66000974d8d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPEW4UPDcw9xr9ZzYAHMLL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 31657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
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

_source line 17 · 2026-05-16T02:29:09.928Z_

<details><summary>↩ Tool result · `toolu_01JbFd3KTvYjqFAsAUWfkTBh`</summary>

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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "de2640d6-4204-43c7-86b4-fc1ee88d3c43",
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

_source line 18_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019Ai6AF4xj9W5ZbyYue9U2x`</summary>

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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "704942c4-68e3-4b6f-adba-5dfe5a324d0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZfvzjL7A3bmaVjPY5Lj6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 152,
      "cache_read_input_tokens": 32020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 152
      },
      "output_tokens": 63,
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

_source line 19 · 2026-05-16T02:29:12.429Z_

<details><summary>↩ Tool result · `toolu_019Ai6AF4xj9W5ZbyYue9U2x`</summary>

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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "ec23fccd-5c51-44d9-a1f4-07df7f31e74f",
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

_source line 20_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012ucvjPGnSdA3tPM9Ku9ZZL`</summary>

```json
{
  "query": "write_paper",
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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "bf49abe9-3ce5-4d10-b969-dadbfd9a75c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ae7sNcazHU1RaTF5zKMpfb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 90,
      "cache_read_input_tokens": 32172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 90
      },
      "output_tokens": 58,
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

_source line 21 · 2026-05-16T02:29:15.024Z_

<details><summary>↩ Tool result · `toolu_012ucvjPGnSdA3tPM9Ku9ZZL`</summary>

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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "d5383b47-f814-4c15-9c07-74f5503f325d",
  "tool_use_result": {
    "matches": [],
    "query": "write_paper",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017DvtpvSUUqgD6iPiNuRjwu`</summary>

```json
{
  "query": "paper section project",
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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "d799d426-b781-4cb2-8a52-a1804b5a30d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HLpTdnb5MMczc84wDkAnp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 92,
      "cache_read_input_tokens": 32262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 92
      },
      "output_tokens": 57,
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

_source line 23 · 2026-05-16T02:29:17.543Z_

<details><summary>↩ Tool result · `toolu_017DvtpvSUUqgD6iPiNuRjwu`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "EnterWorktree"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "634f5230-9994-4336-8c4e-b18559168260",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__append_idea",
      "EnterWorktree",
      "TodoWrite"
    ],
    "query": "paper section project",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 24_

`register_artifact` 工具不可用。文件已写入指定路径。

`method.tex` 已生成：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex`

结构：
- **2.1 Model and Data** — OpenVLA-7B 架构、LIBERO-10/Goal 数据、untrained control 设计
- **2.2 Representation Extraction** — 5 个表征源 (a)-(e) + 2×2 factorial design
- **2.3 RSA** — RDM 构建、Spearman ρ、bootstrap CI
- **2.4 Functional Action Probes** — MLP 探针架构/训练、R²、action-delta probes、统计检验
- **2.5 CKA** — Linear CKA + RDM kernel CKA、维度不匹配 caveat

术语和引用格式与 `experiments.tex` 保持一致，无实验结果数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "uuid": "31be0977-6cd0-41c4-a437-fe5e02ff6c4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BE3VXHD8M6yB3Hj3BwL6f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4012,
      "cache_read_input_tokens": 32354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4012
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

### Task result

_source line 25_

`register_artifact` 工具不可用。文件已写入指定路径。

`method.tex` 已生成：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex`

结构：
- **2.1 Model and Data** — OpenVLA-7B 架构、LIBERO-10/Goal 数据、untrained control 设计
- **2.2 Representation Extraction** — 5 个表征源 (a)-(e) + 2×2 factorial design
- **2.3 RSA** — RDM 构建、Spearman ρ、bootstrap CI
- **2.4 Functional Action Probes** — MLP 探针架构/训练、R²、action-delta probes、统计检验
- **2.5 CKA** — Linear CKA + RDM kernel CKA、维度不匹配 caveat

术语和引用格式与 `experiments.tex` 保持一致，无实验结果数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 81346,
  "duration_api_ms": 84106,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "c7e3b95d-1728-447e-8400-6a2fafc7dad3",
  "total_cost_usd": 0.34706624999999997,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 24525,
    "cache_read_input_tokens": 225668,
    "output_tokens": 3151,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 24525,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 284,
        "cache_read_input_tokens": 32354,
        "cache_creation_input_tokens": 4012,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4012
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1996,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002106,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 3151,
      "cacheReadInputTokens": 225668,
      "cacheCreationInputTokens": 24525,
      "webSearchRequests": 0,
      "costUSD": 0.34496024999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6e1f55da-7ab9-4b87-8069-df65602ffc92"
}
```

</details>

---
