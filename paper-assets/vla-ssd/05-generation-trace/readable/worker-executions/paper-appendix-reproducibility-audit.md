# paper appendix reproducibility audit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 92
- **Recorded user turns:** 1
- **Tool calls:** 32
- **Original source:** `logs/workers/worker_paper_appendix_reproducibility_audit_20260519T150435.log`
- **Structured JSON:** [`852b45d89dd639bfa786.json`](../../sessions/85/852b45d89dd639bfa786.json)

## Before a recorded user message

12 recorded events

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
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
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
  "uuid": "198cb585-4ae2-4f9f-8f41-91067342a175",
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
    "resetsAt": 1779216000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4af797b3-9937-4c99-b75b-bdb5f81077c4",
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088"
}
```

---

### Assistant

_source line 4_

I'll start by reading the appendix.tex and checking the registry for experiment details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "6cb87a7a-4e77-4f2a-b50f-6c8a806b48b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqMcq35mY7rQgdC73es6iT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11972,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11972
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

<details open><summary>🔧 Tool call — Read · `toolu_0141NLj3FwtwcPV3G82bc3M1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "1dcdfeb6-348c-4316-8c4a-1f9dbb1cddac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqMcq35mY7rQgdC73es6iT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11972,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11972
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

_source line 6 · 2026-05-19T15:04:48.565Z_

<details><summary>↩ Tool result · `toolu_0141NLj3FwtwcPV3G82bc3M1`</summary>

```text
1	\paragraph{Use of Generative AI.}
2	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
3	
4	\appendix
5	
6	\section{Supplementary Material}
7	\label{sec:appendix}
8	
9	\subsection{CKA Analysis Method}
10	\label{sec:cka_appendix}
11	
12	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
13	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
14	
15	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
16	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
17	
18	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
19	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
20	
21	\subsection{Metric Sensitivity: RSA versus CKA}
22	\label{sec:metric_sensitivity_appendix}
23	
24	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
25	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
26	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
27	
28	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), with no inverted-U pattern.
29	RSA captures rank-order geometric alignment; CKA captures global linear structure.
30	The dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).
31	
32	\begin{figure}[t]
33	\centering
34	\includegraphics[width=\columnwidth]{figures/fig6.pdf}
35	\caption{Three similarity metrics across representation sources. \textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}
36	\label{fig:metric_comparison}
37	\end{figure}
38	
39	\subsection{Branch-Split Detailed Analysis}
40	\label{sec:branch_split_appendix}
41	
42	To disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.
43	The two branches yield near-identical RSA: DINOv2 branch $\rho = 0.619$, SigLIP branch $\rho = 0.621$.
44	Fusion produces a representation ($\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.
45	The MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\rho = 0.615$, a drop of $\Delta = 0.019$ from the fused 2{,}176-D input.
46	
47	\subsection{RSA Across Representation Sources}
48	\label{sec:rsa_bar_appendix}
49	
50	Figure~\ref{fig:rsa_bar} shows RSA with the action space across all representation sources; the ordering matches Table~\ref{tab:rsa_overview}.
51	
52	\begin{figure}[h]
53	\centering
54	\includegraphics[width=\columnwidth]{figures/fig2.pdf}
55	\caption{RSA with the action space ($\rho$) across representation sources. Self-supervised DINOv2 \texttt{cls\_token} ($\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\% bootstrap CIs.}
56	\label{fig:rsa_bar}
57	\end{figure}
58	
59	\subsection{Per-Layer RSA Profiles}
60	\label{sec:rsa_perlayer_appendix}
61	
62	Figure~\ref{fig:rsa_perlayer_curve} extends Figure~\ref{fig:layer_curves} (main text) by adding readout and untrained profiles.
63	
64	\begin{figure}[h]
65	\centering
66	\includegraphics[width=\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}
67	\caption{Per-layer RSA ($\rho$) for trained and untrained models at image\_mean and readout (last\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\_mean diverge: readout $\rho$ declines gradually ($0.628 \to 0.584$) while image\_mean $\rho$ drops sharply ($0.628 \to 0.422$), consistent with task-specific conditioning at the readout position.}
68	\label{fig:rsa_perlayer_curve}
69	\end{figure}
70	
71	\subsection{Per-Layer Action Decoding Across Training Stages}
72	\label{sec:action_r2_threecond}
73	
74	Figure~\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\pm$ std).
75	All three conditions share L0 representations ($R^2 = 0.645 \pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.
76	The trained model peaks at L9 ($R^2 = 0.643 \pm 0.014$), consistent with progressive specialization for action-relevant feature integration.
77	Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), consistent with stable but unspecialized processing.
78	The untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability indicates that randomly initialized Transformer layers produce destructive interference on action-relevant structure.
79	The three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.
80	The qualitative pattern is consistent across all 3 seeds.
81	
82	\begin{figure}[h]
83	\centering
84	\includegraphics[width=\columnwidth]{figures/fig_action_r2_threecond.pdf}
85	\caption{Per-layer action probe $R^2$ (image\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\pm$ std).}
86	\label{fig:action_r2_threecond}
87	\end{figure}
88	
89	\subsection{Random-Subset Ablation Details}
90	\label{sec:random_subset_ablation}
91	
92	To evaluate whether the ablation effect in \S\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).
93	Dominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \pm 0.013$ (Figure~\ref{fig:random_subset_ablation}).
94	The dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); heads with higher instruction-attention fraction carry more organized routing signals, consistent with graded rather than binary specialization.
95	
96	\begin{figure}[h]
97	\centering
98	\includegraphics[width=0.75\columnwidth]{figures/fig_random_subset_ablation.pdf}
99	\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with graded routing specialization across L1 heads.}
100	\label{fig:random_subset_ablation}
101	\end{figure}
102	
103	\subsection{Action Trajectory Analysis Details}
104	\label{sec:action_trajectory}
105	
106	Table~\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.
107	Both conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).
108	The gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.
109	
110	Per-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).
111	Token-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.
112	
113	\paragraph{Trajectory-level aggregation.}
114	Aggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\sim}4\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).
115	Instruction-head ablation ($N = 50$: 5 tasks $\times$ 10 demos) yields trajectory $d = 2.943$ (95\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).
116	All 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.
117	Counterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).
118	Fine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\sim} 1{,}500$) provide higher resolution for ordering claims.
119	
120	\paragraph{Ground-truth action error.}
121	Ablation redirects model outputs ($d = 0.65$) but does not systematically increase error relative to expert demonstrations: original MSE $= 0.498$; top-24 instruction-head ablation MSE $= 0.497$ ($\Delta = -0.001$, Wilcoxon $p = 0.52$, n.s.); bottom-24 non-instruction heads MSE $= 0.506$ ($\Delta = +0.008$).
122	Changes concentrate on the gripper dimension; translation and rotation dimensions are negligibly affected.
123	Per-task breakdown shows all $|\Delta\text{MSE}| < 3\%$ of baseline with all $p > 0.27$; the near-zero aggregate $\Delta$ reflects uniformly small per-task effects rather than cancellation across tasks.
124	This is consistent with the information-computation dissociation: routing heads control instruction-specific direction selection rather than action precision.
125	
126	Table~\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).
127	Individual control heads produce ${\sim}1.9\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.
128	The 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\ $0.41$), consistent with collective coordination rather than individual strength.
129	
130	\begin{table}[h]
131	\centering
132	\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}
133	\label{tab:perhead_bootstrap}
134	\small
135	\begin{tabular}{lccc}
136	\toprule
137	Group & $N$ heads & Collective $d$ & Per-head $d$ [95\% CI] \\
138	\midrule
139	Instruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\
140	Control & 8 & 0.41 & 0.051 [0.048, 0.055] \\
141	\midrule
142	Difference & --- & --- & 0.024, $p = 0.0018$ \\
143	\bottomrule
144	\end{tabular}
145	\end{table}
146	
147	Instruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.
148	
149	Table~\ref{tab:dose_response} and Figure~\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.
150	Trajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\Delta d / \Delta 4 \approx 0.026$), a plateau at 16--20 heads ($\Delta d = 0.001$), and slow increase at 20--32.
151	
152	\begin{figure}[h]
153	\centering
154	\includegraphics[width=0.75\columnwidth]{figures/fig_dose_response.pdf}
155	\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}
156	\label{fig:dose_response}
157	\end{figure}
158	
159	\begin{table}[h]
160	\centering
161	\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\ original action sequence; 95\% bootstrap CIs ($10{,}000$ resamples).}
162	\label{tab:dose_response}
163	\small
164	\begin{tabular}{rcc}
165	\toprule
166	Heads ablated & Cohen's $d$ & 95\% CI \\
167	\midrule
168	4 & 0.482 & [0.449, 0.511] \\
169	8 & 0.508 & [0.479, 0.541] \\
170	12 & 0.560 & [0.529, 0.593] \\
171	16 & 0.592 & [0.559, 0.625] \\
172	20 & 0.593 & [0.559, 0.627] \\
173	24 & 0.611 & [0.578, 0.645] \\
174	28 & 0.619 & [0.587, 0.654] \\
175	32 & 0.639 & [0.603, 0.671] \\
176	\bottomrule
177	\end{tabular}
178	\end{table}
179	
180	\begin{table}[h]
181	\centering
182	\caption{Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$, token divergence (\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}
183	\label{tab:counterfactual}
184	\small
185	\begin{tabular}{lccc}
186	\toprule
187	Condition & Jaccard & Cohen's $d$ & Token div.\ (\%) \\
188	\midrule
189	Empty (no instruction) & 0.000 & 0.968 & 90.7 \\
190	Wrong (different task) & 0.174 & 0.844 & 89.5 \\
191	Paraphrased & 0.533 & 0.697 & 82.6 \\
192	Shuffled (random order) & 1.000 & 0.625 & 85.7 \\
193	\midrule
194	L1 ablation (24 heads) & --- & 0.650 & 72.3 \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	\begin{table}[h]
200	\centering
201	\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}
202	\label{tab:action_shift_perdim}
203	\small
204	\begin{tabular}{lccccccc}
205	\toprule
206	Condition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\
207	\midrule
208	Instruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\
209	Control (8) & 0.000 & 0.001 & 0.002 & 0.008 & 0.014 & 0.018 & 0.141 \\
210	\bottomrule
211	\end{tabular}
212	\end{table}
213	
214	\subsection{Pretrained LLM Representation Quality Under Visual Input}
215	\label{sec:ood_diagnostics}
216	
217	A potential concern with the three-condition comparison (\S\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.
218	We evaluate three diagnostics to assess representation quality.
219	Activation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.
220	Per-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\approx 0.28$ at L25, consistent with gradual differentiation rather than catastrophic out-of-distribution behavior.
221	Top-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.
222	These diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining (Figure~\ref{fig:ood_diagnostics}). These results support the validity of the three-condition comparison.
223	
224	\begin{figure}[h]
225	\centering
226	\includegraphics[width=\columnwidth]{figures/fig_ood_diagnostics.pdf}
227	\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics indicate structured, non-degenerate representations.}
228	\label{fig:ood_diagnostics}
229	\end{figure}
230	
231	\subsection{Probe Architecture Sensitivity}
232	\label{sec:linear_probe}
233	
234	To rule out that our findings depend on MLP probe capacity ($N/\text{params} \approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \to 7$, $N/\text{params} \approx 2.2$).
235	The inverted-U pattern reproduces: trained image\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).
236	The trained--untrained gap is larger under the linear probe (L14: $\Delta = +0.324$) than the MLP probe (L8: $\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.
237	Untrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.
238	For last\_preaction tokens, the linear probe also corroborates the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\Delta = 0.103$ ($p < 0.001$).
239	These results indicate that our qualitative findings reflect representational structure rather than probe capacity artifacts (Figure~\ref{fig:linear_vs_mlp}).
240	
241	\begin{figure}[h]
242	\centering
243	\includegraphics[width=\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}
244	\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}
245	\label{fig:linear_vs_mlp}
246	\end{figure}
247	
248	\subsection{Functional Probe Comparison}
249	\label{sec:probe_bars_appendix}
250	
251	Figure~\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.
252	
253	\begin{figure}[h]
254	\centering
255	\includegraphics[width=\columnwidth]{figures/fig4.pdf}
256	\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\_mean ($0.655$, L8) exceed the projector baseline ($0.630$); the inverted-U extends to functional capacity.}
257	\label{fig:probe_bars}
258	\end{figure}
259	
260	\subsection{Training Effect and Instruction Invariance}
261	\label{sec:instruction_invariance_appendix}
262	
263	Figure~\ref{fig:factorial} shows trained vs.\ untrained RSA profiles and instruction invariance.
264	Instruction invariance holds across all conditions: maximum $|\Delta| < 0.006$, so action geometry is visually grounded and not modulated by language instructions.
265	
266	\begin{figure}[h]
267	\centering
268	\includegraphics[width=\columnwidth]{figures/fig5.pdf}
269	\caption{\textbf{(a)}~Trained vs.\ untrained image\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\Delta{=}+0.017$, $3\%$). \textbf{(b)}~Instruction invariance: all conditions within $|\Delta|{<}0.006$; action geometry is visually grounded.}
270	\label{fig:factorial}
271	\end{figure}
272	
273	\subsection{Additional RSA Values}
274	\label{sec:additional_rsa}
275	
276	DINOv2 \texttt{patch\_mean} achieves RSA $\rho = 0.631$, between the \texttt{cls\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).
277	VLA untrained readout peaks at L1 ($\rho = 0.626$).
278	
279	\subsection{Cross-Benchmark Validation: LIBERO-Spatial}
280	\label{sec:cross_benchmark_appendix}
281	
282	To assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks requiring spatial reasoning).
283	Figure~\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.
284	
285	The inverted-U profile replicates on LIBERO-Spatial: trained image\_mean RSA peaks at L14 ($\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.
286	Training produces a significant geometric gain (best-vs-best $\Delta = +0.023$, 95\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\Delta = +0.017$, CI includes zero).
287	
288	Two notable differences emerge.
289	First, the absolute RSA values are higher on Spatial ($0.691$ vs.\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.
290	Second, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\Delta_\text{layer}| = 1$).
291	This suggests that peak convergence is benchmark-specific rather than a general consequence of training.
292	
293	\begin{figure}[t]
294	\centering
295	\includegraphics[width=\columnwidth]{figures/fig7.pdf}
296	\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}
297	\label{fig:cross_benchmark}
298	\end{figure}
299	
300	\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}
301	\label{sec:spatial_cross_instruction}
302	
303	Table~\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.
304	The core pattern from LIBERO-Goal replicates: image\_mean remains at chance (${\sim}10\%$) across all layers and conditions, while the trained readout token saturates to $100\%$ by L4.
305	The untrained readout decays more steeply than on LIBERO-Goal ($75.4\%$ at L31 vs.\ $82\%$), consistent with greater task difficulty.
306	
307	\begin{table}[h]
308	\centering
309	\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\%$ from L4; image\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\ Table~\ref{tab:dense_routing_main}).}
310	\label{tab:spatial_cross_instruction}
311	\small
312	\begin{tabular}{llccccc}
313	\toprule
314	Token & Condition & L1 & L4 & L8 & L16 & L31 \\
315	\midrule
316	last\_preaction & Trained & 98.9\% & 100.0\% & 100.0\% & 100.0\% & 100.0\% \\
317	last\_preaction & Untrained & 99.5\% & 98.3\% & 85.7\% & 68.3\% & 75.4\% \\
318	image\_mean & Trained & 10.2\% & 10.0\% & 9.9\% & 10.0\% & 10.1\% \\
319	image\_mean & Untrained & 10.1\% & 10.0\% & 10.0\% & 10.0\% & 10.2\% \\
320	\bottomrule
321	\end{tabular}
322	\end{table}
323	
324	\subsection{Robustness Analyses}
325	\label{sec:robustness_appendix}
326	
327	\subsubsection{Distance Metric Invariance}
328	\label{sec:metric_invariance}
329	
330	The inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\ref{tab:metric_invariance}).
331	
332	\begin{table}[h]
333	\centering
334	\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}
335	\label{tab:metric_invariance}
336	\small
337	\begin{tabular}{lccc}
338	\toprule
339	Condition & Eucl.\ Peak & Cos.\ Peak & Profile $r$ \\
340	\midrule
341	Trained image\_mean & L12 & L12 & 0.990 \\
342	Trained last\_preaction & L12 & L13 & 0.990 \\
343	Untrained image\_mean & L0 & L0 & 0.995 \\
344	Untrained last\_preaction & L1 & L1 & 0.992 \\
345	\bottomrule
346	\end{tabular}
347	\end{table}
348	
349	\subsubsection{Per-DOF Decomposition}
350	\label{sec:perdof}
351	
352	RSA decomposition by action dimension indicates the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\rho = 0.193$), rotation (peak L12, $\rho = 0.175$), and gripper (peak L13, $\rho = 0.106$) all exhibit non-monotonic profiles.
353	Per-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.
354	
355	\subsubsection{Permutation Test}
356	\label{sec:permutation}
357	
358	Permutation testing (1{,}000 shuffles) indicates all observed RSA values are highly significant: observed $\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).
359	
360	\subsubsection{Probe Seed Sensitivity}
361	\label{sec:seed_sensitivity}
362	
363	Action probe $R^2$ is highly stable across random seeds.
364	Over 5 seeds (trained image\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\%$ ($0.655 \pm 0.002$; Table~\ref{tab:seed_sensitivity}).
365	Peak layer concentrates in the L8--L10 region ($4/5$ seeds); the inverted-U shape is not a seed artifact.
366	Seed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.
367	
368	\begin{table}[h]
369	\centering
370	\caption{Probe $R^2$ peak across 5 random seeds (trained image\_mean).}
371	\label{tab:seed_sensitivity}
372	\small
373	\begin{tabular}{lcc}
374	\toprule
375	Seed & Peak Layer & Peak $R^2$ \\
376	\midrule
377	0 & L9 & 0.654 \\
378	1 & L16 & 0.656 \\
379	2 & L9 & 0.653 \\
380	3 & L10 & 0.655 \\
381	42 & L9 & 0.655 \\
382	\midrule
383	Mean$\pm$std & $10.6\pm2.7$ & $0.655\pm0.002$ \\
384	\bottomrule
385	\end{tabular}
386	\end{table}
387	
388	\subsubsection{Demonstration Subsample Sensitivity}
389	\label{sec:demo_sensitivity}
390	
391	To verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\ref{tab:demo_sensitivity}).
392	The RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions (high stability).
393	The probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$; $R^2$ is more sensitive to training set size than RSA.
394	Both metrics show reduced absolute values (RSA $-3.6\%$, $R^2$ $-7.6\%$) as expected from halved data, but the non-monotonic profile shape is preserved.
395	
396	\begin{table}[h]
397	\centering
398	\caption{Inverted-U stability under demonstration subsampling (trained image\_mean).}
399	\label{tab:demo_sensitivity}
400	\small
401	\begin{tabular}{lccc}
402	\toprule
403	Metric & 50 demos & 25 demos & $\Delta$ \\
404	\midrule
405	RSA peak layer & L12 & L12 & 0 \\
406	RSA peak $\rho$ & 0.628 & 0.606 & $-3.6\%$ \\
407	$R^2$ peak layer & L9 & L11 & $+2$ \\
408	$R^2$ peak value & 0.659 & 0.609 & $-7.6\%$ \\
409	RSA profile $r$ & --- & 0.970 & --- \\
410	$R^2$ profile $r$ & --- & 0.819 & --- \\
411	\bottomrule
412	\end{tabular}
413	\end{table}
414	
415	\subsection{Detailed Training Effects}
416	\label{sec:training_effects_appendix}
417	
418	Table~\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.
419	
420	\begin{table}[h]
421	\centering
422	\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\Delta{=}+0.017$, $3\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}
423	\label{tab:training_effects}
424	\small
425	\begin{tabular}{lccc}
426	\toprule
427	Comparison & $\Delta$ & 95\% CI & $p$ \\
428	\midrule
429	\multicolumn{4}{l}{\emph{RSA ($\rho$)}} \\
430	Best-vs-best image\_mean & $+$0.017 & incl.\ 0 & n.s. \\
431	\quad (trained L12 vs.\ untrained L0) & & & \\
432	Same-layer L12 image\_mean & $+$0.079 & excl.\ 0 & $<$0.0001 \\
433	\quad (trained vs.\ untrained) & & & \\
434	Instruction effect (max $|\Delta|$) & 0.006 & --- & n.s. \\
435	\midrule
436	\multicolumn{4}{l}{\emph{Probe $R^2$}} \\
437	Best-vs-best image\_mean & $+$0.015 & excl.\ 0 & 0.006 \\
438	\quad (trained L8 vs.\ untrained L0) & & & \\
439	Best-vs-best readout & $+$0.069 & excl.\ 0 & $<$0.0001 \\
440	\quad (trained L13 vs.\ untrained L32) & & & \\
441	\bottomrule
442	\end{tabular}
443	\end{table}
444	
445	\subsection{Training Effect Size Summary}
446	\label{sec:training_effect_summary}
447	
448	Table~\ref{tab:training_effect_summary} consolidates training effects across all metrics.
449	Training effects on image\_mean metrics are modest (RSA $\Delta = +0.017$, $R^2$ $\Delta = +0.015$), but effects on last\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\Delta = +0.069$).
450	This asymmetry indicates that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.
451	
452	\begin{table}[h]
453	\centering
454	\caption{Training effect sizes across metrics. Image\_mean effects are modest; last\_preaction effects are large. Training targets readout-token information integration.}
455	\label{tab:training_effect_summary}
456	\small
457	\begin{tabular}{lccc}
458	\toprule
459	Metric & Trained & Untrained & $\Delta$ \\
460	\midrule
461	RSA peak (image\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\
462	$R^2$ peak (image\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\
463	$R^2$ peak (last\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\
464	Instruction routing L31 & 100\% & 82\% & $+$18pp \\
465	Instruction attention L1 & 58\% & 12\% & $+$46pp \\
466	Progress classification & 86.3\% (L20) & 85.3\% (L4) & $+$1pp \\
467	\bottomrule
468	\end{tabular}
469	\end{table}
470	
471	\subsection{Instruction Routing Probes}
472	\label{sec:routing_appendix}
473	
474	\subsubsection{Cross-Instruction Classification: Dense Layer Profile}
475	\label{sec:dense_routing}
476	
477	Table~\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.
478	The step-function onset between L0 ($10\%$, chance) and L1 (${\geq}99.6\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\sim}12\%$) suffices for linear classification at L1.
479	Both pretrained and VLA-trained models sustain $100\%$ through L31; only random initialization shows progressive decay ($82\%$ at L31). Deep-layer stability thus derives from structured pretrained weights rather than task-specific fine-tuning.
480	
481	\begin{table}[h]
482	\centering
483	\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8. Values reflect dense routing evaluation; main-text Table~\ref{tab:dense_routing_main} reports sparse single-split results, yielding minor differences (e.g., L8: $98.2\%$ vs.\ $98.6\%$).}
484	\label{tab:dense_routing}
485	\small
486	\begin{tabular}{lccc}
487	\toprule
488	Layer & Trained & Untrained & Image\_mean (trained) \\
489	\midrule
490	L0 & 10.0\% & 10.0\% & 10.0\% \\
491	L1 & 100.0\% & 100.0\% & 10.0\% \\
492	L2 & 100.0\% & 99.6\% & 10.0\% \\
493	L3 & 100.0\% & 99.6\% & 10.0\% \\
494	L4 & 100.0\% & 99.1\% & 10.0\% \\
495	L5 & 100.0\% & 98.2\% & 10.0\% \\
496	L6 & 100.0\% & 97.3\% & 10.0\% \\
497	L7 & 100.0\% & 96.4\% & 10.0\% \\
498	L8 & 100.0\% & 98.6\% & 10.0\% \\
499	\bottomrule
500	\end{tabular}
501	\end{table}
502	
503	\subsubsection{Cross-Instruction LOOCV Validation}
504	\label{sec:loocv}
505	
506	Leave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) validates that the cross-instruction probe result is not driven by memorization.
507	Trained last\_preaction achieves $100\% \pm 0.00$ across all 10 folds at layers L1--L31 (perfect generalization).
508	
509	\subsubsection{QA Probe: Progress and Subtask Classification}
510	\label{sec:qa_probe}
511	
512	To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\ref{tab:qa_probe}).
513	
514	\begin{table}[h]
515	\centering
516	\caption{QA probe accuracy (progress + subtask classification, best layer).}
517	\label{tab:qa_probe}
518	\small
519	\begin{tabular}{lcc}
520	\toprule
521	Source & Best Layer & Accuracy \\
522	\midrule
523	Trained last\_preaction & L20 & 86.3\% \\
524	Untrained last\_preaction & L20 & 85.3\% \\
525	DINOv2 cls\_token & --- & 82.7\% \\
526	\bottomrule
527	\end{tabular}
528	\end{table}
529	
530	\subsubsection{Cross-Instruction Probe Profiles}
531	\label{sec:probe_profiles}
532	
533	\begin{figure}[h]
534	\centering
535	\includegraphics[width=\columnwidth]{figures/fig_probe_conditions.pdf}
536	\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\%$ at L1, saturating to $100\%$. Llama-2 base starts at $80.2\%$, reaching $100\%$ by L5. Untrained starts at $100\%$ but decays to $82\%$ by L31.}
537	\label{fig:probe_conditions_appendix}
538	\end{figure}
539	
540	\subsubsection{Four-Condition Cross-Instruction Probe Profile}
541	\label{app:finetuned_probe}
542	
543	Table~\ref{tab:finetuned_probe} extends the three-condition probe comparison (Table~\ref{tab:dense_routing_main}) with the LIBERO-finetuned checkpoint.
544	
545	\begin{table}[h]
546	\centering
547	\caption{Cross-instruction 10-way classification accuracy across four training conditions. Task-specific fine-tuning (LIBERO) preserves instruction decodability at all layers despite eliminating L31 exit-layer attention engagement (18$\to$0 instruction-dominant heads).}
548	\label{tab:finetuned_probe}
549	\small
550	\begin{tabular}{lcccc}
551	\toprule
552	Layer & Untrained & Llama-2 base & OpenVLA-7B & LIBERO-finetuned \\
553	\midrule
554	L0 & 10.0\% & 10.0\% & 10.0\% & 10.0\% \\
555	L1 & 100.0\% & 80.2\% & 99.6\% & 99.7\% \\
556	L8 & 98.6\% & 99.9\% & 100.0\% & 100.0\% \\
557	L31 & 82.0\% & 100.0\% & 100.0\% & 100.0\% \\
558	\bottomrule
559	\end{tabular}
560	\end{table}
561	
562	\subsubsection{L1 Attention Pattern Analysis}
563	\label{sec:attention_pattern}
564	
565	Figure~\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.
566	The three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.
567	
568	\begin{figure}[h]
569	\centering
570	\includegraphics[width=\columnwidth]{figures/fig_l1_stacked_bar.pdf}
571	\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\%$ text attention). Llama-2 base: 9/32 heads ($36.5\%$). Untrained: 0/32 heads ($11.7\%$). See Table~\ref{tab:routing_gradient} for quantitative comparison.}
572	\label{fig:attention_appendix}
573	\end{figure}
574	
575	\subsubsection{Multi-Layer Attention Patterns}
576	\label{sec:multilayer_attention}
577	
578	Table~\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\ref{fig:attention_profile}, main text).
579	The full profile (Figure~\ref{fig:multilayer_attention}) reveals three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).
580	
581	\begin{figure}[h]
582	\centering
583	\includegraphics[width=\columnwidth]{figures/fig_multi_layer_attn.pdf}
584	\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}
585	\label{fig:multilayer_attention}
586	\end{figure}
587	
588	\begin{table}[h]
589	\centering
590	\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\ref{tab:routing_gradient}) due to threshold boundary effects.}
591	\label{tab:multilayer_attention}
592	\small
593	\begin{tabular}{lcccccc}
594	\toprule
595	 & \multicolumn{2}{c}{VLA Trained} & \multicolumn{2}{c}{Llama-2 base} & \multicolumn{2}{c}{Untrained} \\
596	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
597	Layer & Heads & Text\% & Heads & Text\% & Heads & Text\% \\
598	\midrule
599	L1 & \textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\
600	L8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\
601	L16 & 10/32 & 48.4 & \textbf{25/32} & 60.2 & 0/32 & 9.2 \\
602	L31 & \textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\
603	\bottomrule
604	\end{tabular}
605	\end{table}
606	
607	\subsubsection{Threshold Sensitivity Analysis}
608	\label{sec:threshold_sensitivity}
609	
610	The main text defines instruction-dominant heads as those allocating $>50\%$ attention to instruction tokens.
611	Table~\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\% to 70\%; the 50\% threshold is not a boundary-sensitive choice.
612	
613	\begin{table}[h]
614	\centering
615	\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}
616	\label{tab:threshold_sensitivity}
617	\small
618	\begin{tabular}{lccc}
619	\toprule
620	Threshold & VLA Trained & Llama-2 base & Untrained \\
621	\midrule
622	30\% & 32 & 13 & 0 \\
623	40\% & 31 & 10 & 0 \\
624	50\% & 24 & 9 & 0 \\
625	60\% & 9 & 4 & 0 \\
626	70\% & 5 & 3 & 0 \\
627	\bottomrule
628	\end{tabular}
629	\end{table}
630	
631	\subsection{L1 Attention Decomposition by Head Group}
632	\label{sec:attention_decomp}
633	
634	Table~\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.
635	
636	\begin{table}[h]
637	\centering
638	\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}
639	\label{tab:attention_decomp}
640	\small
641	\begin{tabular}{lcccc}
642	\toprule
643	Head Group & $N$ & Instruction & Vision & BOS/Other \\
644	\midrule
645	Instruction-dominant & 24 & 62.4\% & 18.8\% & 18.8\% \\
646	Control & 8 & 44.9\% & 27.1\% & 28.0\% \\
647	\midrule
648	$\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\
649	\bottomrule
650	\end{tabular}
651	\end{table}
652	
653	Head-level instruction attention entropy reaches $99.5\%$ of the uniform maximum; routing is broadly distributed rather than concentrated in a few heads.
654	
655	\paragraph{Per-token attention normalization.}
656	The $57.7\%$ aggregate text attention in instruction-dominant heads partly reflects token-count imbalance (22 instruction vs.\ 256 image tokens).
657	Per-token normalization reveals a $38.2\times$ ratio: each instruction token receives $38.2\times$ the attention of each image token in trained instruction-dominant heads, compared to only $1.5\times$ in untrained heads (a $25.5\times$ increase from training).
658	Instruction-dominant heads also show lower attention entropy ($0.465$) than non-dominant heads ($0.569$), indicating more concentrated attention distributions.
659	
660	\subsection{Per-Dimension Action MAE Under Head Ablation}
661	\label{sec:per_dim_mae}
662	
663	Table~\ref{tab:per_dim_mae} extends Table~\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.
664	
665	\begin{table}[h]
666	\centering
667	\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\times$); instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\times$) falls between the two groups.}
668	\label{tab:per_dim_mae}
669	\small
670	\begin{tabular}{lccc}
671	\toprule
672	Dimension & Instr.\ 24h MAE & Control 8h MAE & Ratio \\
673	\midrule
674	$dx$ & 0.00189 & 0.00037 & 5.09$\times$ \\
675	$dy$ & 0.00531 & 0.00125 & 4.26$\times$ \\
676	$dz$ & 0.00762 & 0.00243 & 3.14$\times$ \\
677	$roll$ & 0.02059 & 0.00785 & 2.62$\times$ \\
678	$pitch$ & 0.03071 & 0.01387 & 2.21$\times$ \\
679	$yaw$ & 0.03388 & 0.01783 & 1.90$\times$ \\
680	$gripper$ & 0.29072 & 0.14072 & 2.07$\times$ \\
681	\bottomrule
682	\end{tabular}
683	\end{table}
684	
685	\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}
686	\label{sec:per_task_r2}
687	
688	Table~\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).
689	
690	\begin{table}[h]
691	\centering
692	\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\Delta > 0$): instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\Delta R^2 = +0.107$; the 50-demo setting (\S\ref{sec:learned_routing}) yields a consistent $+0.059$.}
693	\label{tab:per_task_r2}
694	\small
695	\begin{tabular}{lccc}
696	\toprule
697	Task & Baseline $R^2$ & Ablated $R^2$ & $\Delta R^2$ \\
698	\midrule
699	open middle drawer & 0.197 & 0.221 & $+$0.024 \\
700	open top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\
701	push plate to stove & 0.190 & 0.197 & $+$0.007 \\
702	put bowl on plate & 0.375 & 0.474 & $+$0.099 \\
703	put bowl on stove & 0.235 & 0.395 & $+$0.160 \\
704	put bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\
705	put cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\
706	put wine on rack & 0.189 & 0.424 & $+$0.235 \\
707	put wine on cabinet & 0.279 & 0.353 & $+$0.074 \\
708	turn on stove & 0.385 & 0.421 & $+$0.036 \\
709	\midrule
710	Mean $\pm$ std & $0.256 \pm 0.070$ & $0.363 \pm 0.088$ & $+$0.107 \\
711	\bottomrule
712	\end{tabular}
713	\end{table}
714	
715	\subsection{Task Complexity and Routing Dependence}
716	\label{sec:task_complexity}
717	
718	We classify tasks as \emph{instruction-discriminative} when multiple tasks share the same manipulated object(s), requiring instruction content to disambiguate the target action (e.g., ``put bowl on plate'' vs.\ ``put bowl on stove''); remaining tasks involve unique object-action pairings recoverable from visual context alone.
719	Table~\ref{tab:task_complexity} reports per-task $|\Delta R^2|$ under both groupings.
720	
721	\begin{table}[h]
722	\centering
723	\caption{Task-level L1 ablation effects ($|\Delta R^2|$) grouped by instruction dependence. \emph{Primary} (conservative): cream cheese in bowl classified as visual-sufficient ($2.5\times$, $p = 0.033$). \emph{Sensitivity} (shared-object criterion): cream cheese reclassified as instruction-discriminative ($6.5\times$, $p = 0.008$).}
724	\label{tab:task_complexity}
725	\small
726	\begin{tabular}{lcc}
727	\toprule
728	Task & $|\Delta R^2|$ & Group \\
729	\midrule
730	put wine on rack & 0.235 & Instr-disc \\
731	put bowl on cabinet & 0.201 & Instr-disc \\
732	put bowl on stove & 0.160 & Instr-disc \\
733	put bowl on plate & 0.099 & Instr-disc \\
734	open top drawer + bowl & 0.075 & Instr-disc \\
735	put wine on cabinet & 0.074 & Instr-disc \\
736	\midrule
737	put cream cheese in bowl$^\dagger$ & 0.159 & Vis-suff \\
738	turn on stove & 0.036 & Vis-suff \\
739	open middle drawer & 0.024 & Vis-suff \\
740	push plate to stove & 0.007 & Vis-suff \\
741	\midrule
742	\multicolumn{3}{l}{\textbf{Primary}: Instr-disc mean $0.141$; Vis-suff mean $0.057$} \\
743	\multicolumn{3}{l}{Mann-Whitney $U = 21.0$, $p = 0.033$, ratio $= 2.49\times$} \\
744	\multicolumn{3}{l}{\textbf{Sensitivity}$^\dagger$: cream cheese as Instr-disc: $p = 0.008$, $6.5\times$} \\
745	\bottomrule
746	\end{tabular}
747	\end{table}
748	
749	\paragraph{Leave-one-out sensitivity.}
750	All leave-one-out $p$-values remain $\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.
751	Reclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).
752	
753	\subsection{Specificity Control: Matched-Size Head Ablation}
754	\label{sec:specificity_control}
755	
756	To test whether ablation effects are specific to instruction-dominant heads, we ablate four matched-size subsets of 24 heads at L1: instruction-dominant (highest instruction attention fraction), image-dominant (highest image attention fraction), random (5 seeds), and bottom-24 (lowest instruction attention fraction; overlaps 16/24 heads with the instruction-dominant group).
757	
758	\begin{table}[h]
759	\centering
760	\caption{Matched-size ablation controls: trajectory disruption ($d$) from ablating 24-head subsets at L1, ranked by instruction attention fraction. Instruction-dominant heads produce the largest effect, but the modest gap ($8\%$ over random) indicates distributed, attention-graded routing rather than a dedicated subset.}
761	\label{tab:specificity_control}
762	\small
763	\begin{tabular}{lcc}
764	\toprule
765	Condition (24 heads) & Cohen's $d$ & 95\% CI \\
766	\midrule
767	Instruction-dominant & 0.650 & (reference) \\
768	Random (5 seeds) & $0.601 \pm 0.021$ & $[0.568, 0.622]$ \\
769	Image-dominant & 0.580 & $[0.547, 0.613]$ \\
770	Bottom-24 & 0.565 & --- \\
771	\bottomrule
772	\end{tabular}
773	\end{table}
774	
775	All conditions yield comparable ground-truth MSE ($0.487$--$0.504$ vs.\ baseline $0.497$), consistent with direction-selective rather than precision-degrading effects.
776	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "a9b88492-07ef-4464-956e-4500782ef336",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
      "content": "\\paragraph{Use of Generative AI.}\nGenerative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.\n\n\\appendix\n\n\\section{Supplementary Material}\n\\label{sec:appendix}\n\n\\subsection{CKA Analysis Method}\n\\label{sec:cka_appendix}\n\nWe employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA as a complementary perspective.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.\n\n\\subsection{Metric Sensitivity: RSA versus CKA}\n\\label{sec:metric_sensitivity_appendix}\n\nLinear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.\n\nAt the per-layer level, linear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), with no inverted-U pattern.\nRSA captures rank-order geometric alignment; CKA captures global linear structure.\nThe dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}\n\\label{fig:metric_comparison}\n\\end{figure}\n\n\\subsection{Branch-Split Detailed Analysis}\n\\label{sec:branch_split_appendix}\n\nTo disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.\nThe two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.\nFusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.\nThe MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.\n\n\\subsection{RSA Across Representation Sources}\n\\label{sec:rsa_bar_appendix}\n\nFigure~\\ref{fig:rsa_bar} shows RSA with the action space across all representation sources; the ordering matches Table~\\ref{tab:rsa_overview}.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n\\subsection{Per-Layer RSA Profiles}\n\\label{sec:rsa_perlayer_appendix}\n\nFigure~\\ref{fig:rsa_perlayer_curve} extends Figure~\\ref{fig:layer_curves} (main text) by adding readout and untrained profiles.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}\n\\caption{Per-layer RSA ($\\rho$) for trained and untrained models at image\\_mean and readout (last\\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\\_mean diverge: readout $\\rho$ declines gradually ($0.628 \\to 0.584$) while image\\_mean $\\rho$ drops sharply ($0.628 \\to 0.422$), consistent with task-specific conditioning at the readout position.}\n\\label{fig:rsa_perlayer_curve}\n\\end{figure}\n\n\\subsection{Per-Layer Action Decoding Across Training Stages}\n\\label{sec:action_r2_threecond}\n\nFigure~\\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\\pm$ std).\nAll three conditions share L0 representations ($R^2 = 0.645 \\pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.\nThe trained model peaks at L9 ($R^2 = 0.643 \\pm 0.014$), consistent with progressive specialization for action-relevant feature integration.\nLlama-2 base shows a steady decline (L0: $0.645 \\to$ L32: $0.551$, std $0.003$--$0.035$), consistent with stable but unspecialized processing.\nThe untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability indicates that randomly initialized Transformer layers produce destructive interference on action-relevant structure.\nThe three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.\nThe qualitative pattern is consistent across all 3 seeds.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_action_r2_threecond.pdf}\n\\caption{Per-layer action probe $R^2$ (image\\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \\pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\\pm$ std).}\n\\label{fig:action_r2_threecond}\n\\end{figure}\n\n\\subsection{Random-Subset Ablation Details}\n\\label{sec:random_subset_ablation}\n\nTo evaluate whether the ablation effect in \\S\\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).\nDominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \\pm 0.013$ (Figure~\\ref{fig:random_subset_ablation}).\nThe dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); heads with higher instruction-attention fraction carry more organized routing signals, consistent with graded rather than binary specialization.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_random_subset_ablation.pdf}\n\\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \\pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with graded routing specialization across L1 heads.}\n\\label{fig:random_subset_ablation}\n\\end{figure}\n\n\\subsection{Action Trajectory Analysis Details}\n\\label{sec:action_trajectory}\n\nTable~\\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.\nBoth conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).\nThe gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.\n\nPer-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).\nToken-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.\n\n\\paragraph{Trajectory-level aggregation.}\nAggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\\sim}4\\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).\nInstruction-head ablation ($N = 50$: 5 tasks $\\times$ 10 demos) yields trajectory $d = 2.943$ (95\\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).\nAll 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.\nCounterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).\nFine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\\sim} 1{,}500$) provide higher resolution for ordering claims.\n\n\\paragraph{Ground-truth action error.}\nAblation redirects model outputs ($d = 0.65$) but does not systematically increase error relative to expert demonstrations: original MSE $= 0.498$; top-24 instruction-head ablation MSE $= 0.497$ ($\\Delta = -0.001$, Wilcoxon $p = 0.52$, n.s.); bottom-24 non-instruction heads MSE $= 0.506$ ($\\Delta = +0.008$).\nChanges concentrate on the gripper dimension; translation and rotation dimensions are negligibly affected.\nPer-task breakdown shows all $|\\Delta\\text{MSE}| < 3\\%$ of baseline with all $p > 0.27$; the near-zero aggregate $\\Delta$ reflects uniformly small per-task effects rather than cancellation across tasks.\nThis is consistent with the information-computation dissociation: routing heads control instruction-specific direction selection rather than action precision.\n\nTable~\\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).\nIndividual control heads produce ${\\sim}1.9\\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.\nThe 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\\ $0.41$), consistent with collective coordination rather than individual strength.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}\n\\label{tab:perhead_bootstrap}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nGroup & $N$ heads & Collective $d$ & Per-head $d$ [95\\% CI] \\\\\n\\midrule\nInstruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\\\\nControl & 8 & 0.41 & 0.051 [0.048, 0.055] \\\\\n\\midrule\nDifference & --- & --- & 0.024, $p = 0.0018$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInstruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.\n\nTable~\\ref{tab:dose_response} and Figure~\\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.\nTrajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\\Delta d / \\Delta 4 \\approx 0.026$), a plateau at 16--20 heads ($\\Delta d = 0.001$), and slow increase at 20--32.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\\ original action sequence; 95\\% bootstrap CIs ($10{,}000$ resamples).}\n\\label{tab:dose_response}\n\\small\n\\begin{tabular}{rcc}\n\\toprule\nHeads ablated & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\n4 & 0.482 & [0.449, 0.511] \\\\\n8 & 0.508 & [0.479, 0.541] \\\\\n12 & 0.560 & [0.529, 0.593] \\\\\n16 & 0.592 & [0.559, 0.625] \\\\\n20 & 0.593 & [0.559, 0.627] \\\\\n24 & 0.611 & [0.578, 0.645] \\\\\n28 & 0.619 & [0.587, 0.654] \\\\\n32 & 0.639 & [0.603, 0.671] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$, token divergence (\\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \\text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}\n\\label{tab:counterfactual}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Jaccard & Cohen's $d$ & Token div.\\ (\\%) \\\\\n\\midrule\nEmpty (no instruction) & 0.000 & 0.968 & 90.7 \\\\\nWrong (different task) & 0.174 & 0.844 & 89.5 \\\\\nParaphrased & 0.533 & 0.697 & 82.6 \\\\\nShuffled (random order) & 1.000 & 0.625 & 85.7 \\\\\n\\midrule\nL1 ablation (24 heads) & --- & 0.650 & 72.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}\n\\label{tab:action_shift_perdim}\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\nCondition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\\\\n\\midrule\nInstruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\\\\nControl (8) & 0.000 & 0.001 & 0.002 & 0.008 & 0.014 & 0.018 & 0.141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pretrained LLM Representation Quality Under Visual Input}\n\\label{sec:ood_diagnostics}\n\nA potential concern with the three-condition comparison (\\S\\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.\nWe evaluate three diagnostics to assess representation quality.\nActivation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \\to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.\nPer-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\\approx 0.28$ at L25, consistent with gradual differentiation rather than catastrophic out-of-distribution behavior.\nTop-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.\nThese diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining (Figure~\\ref{fig:ood_diagnostics}). These results support the validity of the three-condition comparison.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ood_diagnostics.pdf}\n\\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics indicate structured, non-degenerate representations.}\n\\label{fig:ood_diagnostics}\n\\end{figure}\n\n\\subsection{Probe Architecture Sensitivity}\n\\label{sec:linear_probe}\n\nTo rule out that our findings depend on MLP probe capacity ($N/\\text{params} \\approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \\to 7$, $N/\\text{params} \\approx 2.2$).\nThe inverted-U pattern reproduces: trained image\\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).\nThe trained--untrained gap is larger under the linear probe (L14: $\\Delta = +0.324$) than the MLP probe (L8: $\\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.\nUntrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.\nFor last\\_preaction tokens, the linear probe also corroborates the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\\Delta = 0.103$ ($p < 0.001$).\nThese results indicate that our qualitative findings reflect representational structure rather than probe capacity artifacts (Figure~\\ref{fig:linear_vs_mlp}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}\n\\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}\n\\label{fig:linear_vs_mlp}\n\\end{figure}\n\n\\subsection{Functional Probe Comparison}\n\\label{sec:probe_bars_appendix}\n\nFigure~\\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\\_mean ($0.655$, L8) exceed the projector baseline ($0.630$); the inverted-U extends to functional capacity.}\n\\label{fig:probe_bars}\n\\end{figure}\n\n\\subsection{Training Effect and Instruction Invariance}\n\\label{sec:instruction_invariance_appendix}\n\nFigure~\\ref{fig:factorial} shows trained vs.\\ untrained RSA profiles and instruction invariance.\nInstruction invariance holds across all conditions: maximum $|\\Delta| < 0.006$, so action geometry is visually grounded and not modulated by language instructions.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\\Delta{=}+0.017$, $3\\%$). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$; action geometry is visually grounded.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Additional RSA Values}\n\\label{sec:additional_rsa}\n\nDINOv2 \\texttt{patch\\_mean} achieves RSA $\\rho = 0.631$, between the \\texttt{cls\\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).\nVLA untrained readout peaks at L1 ($\\rho = 0.626$).\n\n\\subsection{Cross-Benchmark Validation: LIBERO-Spatial}\n\\label{sec:cross_benchmark_appendix}\n\nTo assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks requiring spatial reasoning).\nFigure~\\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.\n\nThe inverted-U profile replicates on LIBERO-Spatial: trained image\\_mean RSA peaks at L14 ($\\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.\nTraining produces a significant geometric gain (best-vs-best $\\Delta = +0.023$, 95\\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\\Delta = +0.017$, CI includes zero).\n\nTwo notable differences emerge.\nFirst, the absolute RSA values are higher on Spatial ($0.691$ vs.\\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.\nSecond, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\\Delta_\\text{layer}| = 1$).\nThis suggests that peak convergence is benchmark-specific rather than a general consequence of training.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig7.pdf}\n\\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}\n\\label{fig:cross_benchmark}\n\\end{figure}\n\n\\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}\n\\label{sec:spatial_cross_instruction}\n\nTable~\\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.\nThe core pattern from LIBERO-Goal replicates: image\\_mean remains at chance (${\\sim}10\\%$) across all layers and conditions, while the trained readout token saturates to $100\\%$ by L4.\nThe untrained readout decays more steeply than on LIBERO-Goal ($75.4\\%$ at L31 vs.\\ $82\\%$), consistent with greater task difficulty.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\\%$ from L4; image\\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\\ Table~\\ref{tab:dense_routing_main}).}\n\\label{tab:spatial_cross_instruction}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nToken & Condition & L1 & L4 & L8 & L16 & L31 \\\\\n\\midrule\nlast\\_preaction & Trained & 98.9\\% & 100.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\nlast\\_preaction & Untrained & 99.5\\% & 98.3\\% & 85.7\\% & 68.3\\% & 75.4\\% \\\\\nimage\\_mean & Trained & 10.2\\% & 10.0\\% & 9.9\\% & 10.0\\% & 10.1\\% \\\\\nimage\\_mean & Untrained & 10.1\\% & 10.0\\% & 10.0\\% & 10.0\\% & 10.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness Analyses}\n\\label{sec:robustness_appendix}\n\n\\subsubsection{Distance Metric Invariance}\n\\label{sec:metric_invariance}\n\nThe inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\\ref{tab:metric_invariance}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}\n\\label{tab:metric_invariance}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Eucl.\\ Peak & Cos.\\ Peak & Profile $r$ \\\\\n\\midrule\nTrained image\\_mean & L12 & L12 & 0.990 \\\\\nTrained last\\_preaction & L12 & L13 & 0.990 \\\\\nUntrained image\\_mean & L0 & L0 & 0.995 \\\\\nUntrained last\\_preaction & L1 & L1 & 0.992 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Per-DOF Decomposition}\n\\label{sec:perdof}\n\nRSA decomposition by action dimension indicates the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\\rho = 0.193$), rotation (peak L12, $\\rho = 0.175$), and gripper (peak L13, $\\rho = 0.106$) all exhibit non-monotonic profiles.\nPer-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.\n\n\\subsubsection{Permutation Test}\n\\label{sec:permutation}\n\nPermutation testing (1{,}000 shuffles) indicates all observed RSA values are highly significant: observed $\\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).\n\n\\subsubsection{Probe Seed Sensitivity}\n\\label{sec:seed_sensitivity}\n\nAction probe $R^2$ is highly stable across random seeds.\nOver 5 seeds (trained image\\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\\%$ ($0.655 \\pm 0.002$; Table~\\ref{tab:seed_sensitivity}).\nPeak layer concentrates in the L8--L10 region ($4/5$ seeds); the inverted-U shape is not a seed artifact.\nSeed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe $R^2$ peak across 5 random seeds (trained image\\_mean).}\n\\label{tab:seed_sensitivity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSeed & Peak Layer & Peak $R^2$ \\\\\n\\midrule\n0 & L9 & 0.654 \\\\\n1 & L16 & 0.656 \\\\\n2 & L9 & 0.653 \\\\\n3 & L10 & 0.655 \\\\\n42 & L9 & 0.655 \\\\\n\\midrule\nMean$\\pm$std & $10.6\\pm2.7$ & $0.655\\pm0.002$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Demonstration Subsample Sensitivity}\n\\label{sec:demo_sensitivity}\n\nTo verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\\ref{tab:demo_sensitivity}).\nThe RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions (high stability).\nThe probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$; $R^2$ is more sensitive to training set size than RSA.\nBoth metrics show reduced absolute values (RSA $-3.6\\%$, $R^2$ $-7.6\\%$) as expected from halved data, but the non-monotonic profile shape is preserved.\n\n\\begin{table}[h]\n\\centering\n\\caption{Inverted-U stability under demonstration subsampling (trained image\\_mean).}\n\\label{tab:demo_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 50 demos & 25 demos & $\\Delta$ \\\\\n\\midrule\nRSA peak layer & L12 & L12 & 0 \\\\\nRSA peak $\\rho$ & 0.628 & 0.606 & $-3.6\\%$ \\\\\n$R^2$ peak layer & L9 & L11 & $+2$ \\\\\n$R^2$ peak value & 0.659 & 0.609 & $-7.6\\%$ \\\\\nRSA profile $r$ & --- & 0.970 & --- \\\\\n$R^2$ profile $r$ & --- & 0.819 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detailed Training Effects}\n\\label{sec:training_effects_appendix}\n\nTable~\\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\\Delta{=}+0.017$, $3\\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{RSA ($\\rho$)}} \\\\\nBest-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\\n\\quad (trained L12 vs.\\ untrained L0) & & & \\\\\nSame-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained vs.\\ untrained) & & & \\\\\nInstruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Probe $R^2$}} \\\\\nBest-vs-best image\\_mean & $+$0.015 & excl.\\ 0 & 0.006 \\\\\n\\quad (trained L8 vs.\\ untrained L0) & & & \\\\\nBest-vs-best readout & $+$0.069 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained L13 vs.\\ untrained L32) & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Training Effect Size Summary}\n\\label{sec:training_effect_summary}\n\nTable~\\ref{tab:training_effect_summary} consolidates training effects across all metrics.\nTraining effects on image\\_mean metrics are modest (RSA $\\Delta = +0.017$, $R^2$ $\\Delta = +0.015$), but effects on last\\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\\Delta = +0.069$).\nThis asymmetry indicates that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effect sizes across metrics. Image\\_mean effects are modest; last\\_preaction effects are large. Training targets readout-token information integration.}\n\\label{tab:training_effect_summary}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Trained & Untrained & $\\Delta$ \\\\\n\\midrule\nRSA peak (image\\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\\\\n$R^2$ peak (image\\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\\\\n$R^2$ peak (last\\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\\\\nInstruction routing L31 & 100\\% & 82\\% & $+$18pp \\\\\nInstruction attention L1 & 58\\% & 12\\% & $+$46pp \\\\\nProgress classification & 86.3\\% (L20) & 85.3\\% (L4) & $+$1pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Instruction Routing Probes}\n\\label{sec:routing_appendix}\n\n\\subsubsection{Cross-Instruction Classification: Dense Layer Profile}\n\\label{sec:dense_routing}\n\nTable~\\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.\nThe step-function onset between L0 ($10\\%$, chance) and L1 (${\\geq}99.6\\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\\sim}12\\%$) suffices for linear classification at L1.\nBoth pretrained and VLA-trained models sustain $100\\%$ through L31; only random initialization shows progressive decay ($82\\%$ at L31). Deep-layer stability thus derives from structured pretrained weights rather than task-specific fine-tuning.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8. Values reflect dense routing evaluation; main-text Table~\\ref{tab:dense_routing_main} reports sparse single-split results, yielding minor differences (e.g., L8: $98.2\\%$ vs.\\ $98.6\\%$).}\n\\label{tab:dense_routing}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained & Untrained & Image\\_mean (trained) \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL2 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL3 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL5 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL6 & 100.0\\% & 97.3\\% & 10.0\\% \\\\\nL7 & 100.0\\% & 96.4\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.6\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction LOOCV Validation}\n\\label{sec:loocv}\n\nLeave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) validates that the cross-instruction probe result is not driven by memorization.\nTrained last\\_preaction achieves $100\\% \\pm 0.00$ across all 10 folds at layers L1--L31 (perfect generalization).\n\n\\subsubsection{QA Probe: Progress and Subtask Classification}\n\\label{sec:qa_probe}\n\nTo test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\\ref{tab:qa_probe}).\n\n\\begin{table}[h]\n\\centering\n\\caption{QA probe accuracy (progress + subtask classification, best layer).}\n\\label{tab:qa_probe}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSource & Best Layer & Accuracy \\\\\n\\midrule\nTrained last\\_preaction & L20 & 86.3\\% \\\\\nUntrained last\\_preaction & L20 & 85.3\\% \\\\\nDINOv2 cls\\_token & --- & 82.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction Probe Profiles}\n\\label{sec:probe_profiles}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_probe_conditions.pdf}\n\\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\\%$ at L1, saturating to $100\\%$. Llama-2 base starts at $80.2\\%$, reaching $100\\%$ by L5. Untrained starts at $100\\%$ but decays to $82\\%$ by L31.}\n\\label{fig:probe_conditions_appendix}\n\\end{figure}\n\n\\subsubsection{Four-Condition Cross-Instruction Probe Profile}\n\\label{app:finetuned_probe}\n\nTable~\\ref{tab:finetuned_probe} extends the three-condition probe comparison (Table~\\ref{tab:dense_routing_main}) with the LIBERO-finetuned checkpoint.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy across four training conditions. Task-specific fine-tuning (LIBERO) preserves instruction decodability at all layers despite eliminating L31 exit-layer attention engagement (18$\\to$0 instruction-dominant heads).}\n\\label{tab:finetuned_probe}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & Untrained & Llama-2 base & OpenVLA-7B & LIBERO-finetuned \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 80.2\\% & 99.6\\% & 99.7\\% \\\\\nL8 & 98.6\\% & 99.9\\% & 100.0\\% & 100.0\\% \\\\\nL31 & 82.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{L1 Attention Pattern Analysis}\n\\label{sec:attention_pattern}\n\nFigure~\\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.\nThe three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_l1_stacked_bar.pdf}\n\\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\\%$ text attention). Llama-2 base: 9/32 heads ($36.5\\%$). Untrained: 0/32 heads ($11.7\\%$). See Table~\\ref{tab:routing_gradient} for quantitative comparison.}\n\\label{fig:attention_appendix}\n\\end{figure}\n\n\\subsubsection{Multi-Layer Attention Patterns}\n\\label{sec:multilayer_attention}\n\nTable~\\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\\ref{fig:attention_profile}, main text).\nThe full profile (Figure~\\ref{fig:multilayer_attention}) reveals three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_multi_layer_attn.pdf}\n\\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}\n\\label{fig:multilayer_attention}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\\ref{tab:routing_gradient}) due to threshold boundary effects.}\n\\label{tab:multilayer_attention}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{VLA Trained} & \\multicolumn{2}{c}{Llama-2 base} & \\multicolumn{2}{c}{Untrained} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\nLayer & Heads & Text\\% & Heads & Text\\% & Heads & Text\\% \\\\\n\\midrule\nL1 & \\textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\\\\nL8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\\\\nL16 & 10/32 & 48.4 & \\textbf{25/32} & 60.2 & 0/32 & 9.2 \\\\\nL31 & \\textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Threshold Sensitivity Analysis}\n\\label{sec:threshold_sensitivity}\n\nThe main text defines instruction-dominant heads as those allocating $>50\\%$ attention to instruction tokens.\nTable~\\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\\% to 70\\%; the 50\\% threshold is not a boundary-sensitive choice.\n\n\\begin{table}[h]\n\\centering\n\\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}\n\\label{tab:threshold_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nThreshold & VLA Trained & Llama-2 base & Untrained \\\\\n\\midrule\n30\\% & 32 & 13 & 0 \\\\\n40\\% & 31 & 10 & 0 \\\\\n50\\% & 24 & 9 & 0 \\\\\n60\\% & 9 & 4 & 0 \\\\\n70\\% & 5 & 3 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{L1 Attention Decomposition by Head Group}\n\\label{sec:attention_decomp}\n\nTable~\\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.\n\n\\begin{table}[h]\n\\centering\n\\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}\n\\label{tab:attention_decomp}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nHead Group & $N$ & Instruction & Vision & BOS/Other \\\\\n\\midrule\nInstruction-dominant & 24 & 62.4\\% & 18.8\\% & 18.8\\% \\\\\nControl & 8 & 44.9\\% & 27.1\\% & 28.0\\% \\\\\n\\midrule\n$\\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHead-level instruction attention entropy reaches $99.5\\%$ of the uniform maximum; routing is broadly distributed rather than concentrated in a few heads.\n\n\\paragraph{Per-token attention normalization.}\nThe $57.7\\%$ aggregate text attention in instruction-dominant heads partly reflects token-count imbalance (22 instruction vs.\\ 256 image tokens).\nPer-token normalization reveals a $38.2\\times$ ratio: each instruction token receives $38.2\\times$ the attention of each image token in trained instruction-dominant heads, compared to only $1.5\\times$ in untrained heads (a $25.5\\times$ increase from training).\nInstruction-dominant heads also show lower attention entropy ($0.465$) than non-dominant heads ($0.569$), indicating more concentrated attention distributions.\n\n\\subsection{Per-Dimension Action MAE Under Head Ablation}\n\\label{sec:per_dim_mae}\n\nTable~\\ref{tab:per_dim_mae} extends Table~\\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\\times$); instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\\times$) falls between the two groups.}\n\\label{tab:per_dim_mae}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDimension & Instr.\\ 24h MAE & Control 8h MAE & Ratio \\\\\n\\midrule\n$dx$ & 0.00189 & 0.00037 & 5.09$\\times$ \\\\\n$dy$ & 0.00531 & 0.00125 & 4.26$\\times$ \\\\\n$dz$ & 0.00762 & 0.00243 & 3.14$\\times$ \\\\\n$roll$ & 0.02059 & 0.00785 & 2.62$\\times$ \\\\\n$pitch$ & 0.03071 & 0.01387 & 2.21$\\times$ \\\\\n$yaw$ & 0.03388 & 0.01783 & 1.90$\\times$ \\\\\n$gripper$ & 0.29072 & 0.14072 & 2.07$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}\n\\label{sec:per_task_r2}\n\nTable~\\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\\Delta > 0$): instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\\Delta R^2 = +0.107$; the 50-demo setting (\\S\\ref{sec:learned_routing}) yields a consistent $+0.059$.}\n\\label{tab:per_task_r2}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTask & Baseline $R^2$ & Ablated $R^2$ & $\\Delta R^2$ \\\\\n\\midrule\nopen middle drawer & 0.197 & 0.221 & $+$0.024 \\\\\nopen top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\\\\npush plate to stove & 0.190 & 0.197 & $+$0.007 \\\\\nput bowl on plate & 0.375 & 0.474 & $+$0.099 \\\\\nput bowl on stove & 0.235 & 0.395 & $+$0.160 \\\\\nput bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\\\\nput cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\\\\nput wine on rack & 0.189 & 0.424 & $+$0.235 \\\\\nput wine on cabinet & 0.279 & 0.353 & $+$0.074 \\\\\nturn on stove & 0.385 & 0.421 & $+$0.036 \\\\\n\\midrule\nMean $\\pm$ std & $0.256 \\pm 0.070$ & $0.363 \\pm 0.088$ & $+$0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Task Complexity and Routing Dependence}\n\\label{sec:task_complexity}\n\nWe classify tasks as \\emph{instruction-discriminative} when multiple tasks share the same manipulated object(s), requiring instruction content to disambiguate the target action (e.g., ``put bowl on plate'' vs.\\ ``put bowl on stove''); remaining tasks involve unique object-action pairings recoverable from visual context alone.\nTable~\\ref{tab:task_complexity} reports per-task $|\\Delta R^2|$ under both groupings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Task-level L1 ablation effects ($|\\Delta R^2|$) grouped by instruction dependence. \\emph{Primary} (conservative): cream cheese in bowl classified as visual-sufficient ($2.5\\times$, $p = 0.033$). \\emph{Sensitivity} (shared-object criterion): cream cheese reclassified as instruction-discriminative ($6.5\\times$, $p = 0.008$).}\n\\label{tab:task_complexity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nTask & $|\\Delta R^2|$ & Group \\\\\n\\midrule\nput wine on rack & 0.235 & Instr-disc \\\\\nput bowl on cabinet & 0.201 & Instr-disc \\\\\nput bowl on stove & 0.160 & Instr-disc \\\\\nput bowl on plate & 0.099 & Instr-disc \\\\\nopen top drawer + bowl & 0.075 & Instr-disc \\\\\nput wine on cabinet & 0.074 & Instr-disc \\\\\n\\midrule\nput cream cheese in bowl$^\\dagger$ & 0.159 & Vis-suff \\\\\nturn on stove & 0.036 & Vis-suff \\\\\nopen middle drawer & 0.024 & Vis-suff \\\\\npush plate to stove & 0.007 & Vis-suff \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Primary}: Instr-disc mean $0.141$; Vis-suff mean $0.057$} \\\\\n\\multicolumn{3}{l}{Mann-Whitney $U = 21.0$, $p = 0.033$, ratio $= 2.49\\times$} \\\\\n\\multicolumn{3}{l}{\\textbf{Sensitivity}$^\\dagger$: cream cheese as Instr-disc: $p = 0.008$, $6.5\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Leave-one-out sensitivity.}\nAll leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.\nReclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).\n\n\\subsection{Specificity Control: Matched-Size Head Ablation}\n\\label{sec:specificity_control}\n\nTo test whether ablation effects are specific to instruction-dominant heads, we ablate four matched-size subsets of 24 heads at L1: instruction-dominant (highest instruction attention fraction), image-dominant (highest image attention fraction), random (5 seeds), and bottom-24 (lowest instruction attention fraction; overlaps 16/24 heads with the instruction-dominant group).\n\n\\begin{table}[h]\n\\centering\n\\caption{Matched-size ablation controls: trajectory disruption ($d$) from ablating 24-head subsets at L1, ranked by instruction attention fraction. Instruction-dominant heads produce the largest effect, but the modest gap ($8\\%$ over random) indicates distributed, attention-graded routing rather than a dedicated subset.}\n\\label{tab:specificity_control}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition (24 heads) & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\nInstruction-dominant & 0.650 & (reference) \\\\\nRandom (5 seeds) & $0.601 \\pm 0.021$ & $[0.568, 0.622]$ \\\\\nImage-dominant & 0.580 & $[0.547, 0.613]$ \\\\\nBottom-24 & 0.565 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll conditions yield comparable ground-truth MSE ($0.487$--$0.504$ vs.\\ baseline $0.497$), consistent with direction-selective rather than precision-degrading effects.\n",
      "numLines": 776,
      "startLine": 1,
      "totalLines": 776
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Fd7Rhepvkw3bGN78kyYPfA`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "ed1de6b3-b787-4aac-8dd1-e95053c00c90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqMcq35mY7rQgdC73es6iT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11972,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11972
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

_source line 8 · 2026-05-19T15:04:48.741Z_

<details><summary>↩ Tool result · `toolu_01Fd7Rhepvkw3bGN78kyYPfA`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "b86ac84e-1c3b-4fd2-aec8-0f1e65f78a3a",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the appendix.tex content I just read. I need to identify all subsections and check each one against the 5 reproducibility criteria. Let me also read the experiments.tex and method.tex to know what's already described there, and check the registry for experiment specs.

Let me first list all subsections I found in the appendix:

1. **CKA Analysis Method** (§sec:cka_appendix) - lines 9-19
2. **Metric Sensitivity: RSA versus CKA** (§sec:metric_sensitivity_appendix) - lines 21-37
3. **Branch-Split Detailed Analysis** (§sec:branch_split_appendix) - lines 39-46


4. **RSA Across Representation Sources** (§sec:rsa_bar_appendix) - lines 47-57
5. **Per-Layer RSA Profiles** (§sec:rsa_perlayer_appendix) - lines 59-69
6. **Per-Layer Action Decoding Across Training Stages** (§sec:action_r2_threecond) - lines 71-87
7. **Random-Subset Ablation Details** (§sec:random_subset_ablation) - lines 89-101
8. **Action Trajectory Analysis Details** (§sec:action_trajectory) - continuing through the rest of the appendix with sections on pretrained LLM representation quality under visual inputs, probe architecture sensitivity, functional probe comparisons, training effects and instruction invariance, additional RSA values, cross-benchmark validation on LIBERO-Spatial, and robustness analyses covering lines 103-413.

Now I'm moving into the detailed training effects and their summary, followed by a comprehensive analysis of instruction routing probes that spans multiple subanalyses including cross-instruction classification, LOOCV validation, QA probe performance, attention pattern analysis across layers, and probe profiles across different conditions.

Continuing with the attention decomposition work, I'm examining how individual attention heads contribute to the model's behavior under ablation, then looking at per-dimension action prediction errors and task-specific R² distributions when removing head groups. I'm also investigating how task complexity relates to routing dependence, and finally running a specificity control experiment using matched-size head ablations to ensure the effects aren't just artifacts of removing different numbers of parameters.

Now I'm checking the documentation against key criteria like model version and checkpoint source, dataset specifications, and hyperparameters.

Looking through the experiments and method sections to see what setup details are already documented there, since most of these analyses share the same OpenVLA-7B and LIBERO-Goal configuration that could be referenced rather than repeated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "aa73acb4-1ee0-4996-8558-199c6dd62d38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcU1fzx4XwsSpeqN3HDsV5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18371,
      "cache_read_input_tokens": 23813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18371
      },
      "output_tokens": 25,
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

Now let me read the main text sections and registry to know what's already covered.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "e546ed23-1176-4bce-bb9b-709287dab13d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcU1fzx4XwsSpeqN3HDsV5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18371,
      "cache_read_input_tokens": 23813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18371
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — Agent · `toolu_01RfECVzK9DgYeJA3Mhw8imG`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Read experiments.tex and method.tex",
  "prompt": "Read the following files fully and summarize what experimental setup details are already described (model version/checkpoint, dataset, hyperparameters, metric definitions, hardware):\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex\n\nFor each file, list:\n- Which model(s) are mentioned and their exact names/sources\n- Dataset details (name, split, sample counts)\n- Any hyperparameters mentioned (learning rate, batch size, epochs, optimizer, seed, etc.)\n- Metric definitions (RSA, CKA, probe R², Cohen's d, etc.)\n- Hardware mentioned\n- Section labels (\\label{}) so I know what can be cross-referenced\n\nReport the full details found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "0fd38077-418e-49d3-9357-41412d0bf3c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcU1fzx4XwsSpeqN3HDsV5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18371,
      "cache_read_input_tokens": 23813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18371
      },
      "output_tokens": 25,
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

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a9facc9f4edacaa35",
  "tool_use_id": "toolu_01RfECVzK9DgYeJA3Mhw8imG",
  "description": "Read experiments.tex and method.tex",
  "task_type": "local_agent",
  "prompt": "Read the following files fully and summarize what experimental setup details are already described (model version/checkpoint, dataset, hyperparameters, metric definitions, hardware):\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex\n\nFor each file, list:\n- Which model(s) are mentioned and their exact names/sources\n- Dataset details (name, split, sample counts)\n- Any hyperparameters mentioned (learning rate, batch size, epochs, optimizer, seed, etc.)\n- Metric definitions (RSA, CKA, probe R², Cohen's d, etc.)\n- Hardware mentioned\n- Section labels (\\label{}) so I know what can be cross-referenced\n\nReport the full details found.",
  "uuid": "f2ba3795-4f62-4858-b8bc-66d0bdfe8401",
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088"
}
```

---

## Round 1

80 recorded events

### User

_source line 13 · 2026-05-19T15:05:17.937Z_

Read the following files fully and summarize what experimental setup details are already described (model version/checkpoint, dataset, hyperparameters, metric definitions, hardware):

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex

For each file, list:
- Which model(s) are mentioned and their exact names/sources
- Dataset details (name, split, sample counts)
- Any hyperparameters mentioned (learning rate, batch size, epochs, optimizer, seed, etc.)
- Metric definitions (RSA, CKA, probe R², Cohen's d, etc.)
- Hardware mentioned
- Section labels (\label{}) so I know what can be cross-referenced

Report the full details found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RfECVzK9DgYeJA3Mhw8imG",
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "15f309c9-038d-4a93-b458-8f2a73dd3897"
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_014MzygpaEptxwiAfBsxw6aw`</summary>

```json
{
  "project": "vla-ssd",
  "limit": 0,
  "fields": [
    "id",
    "title",
    "status",
    "spec"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "aa8961ac-fcc6-49d0-b62b-7785f8081080",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcU1fzx4XwsSpeqN3HDsV5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18371,
      "cache_read_input_tokens": 23813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18371
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — Glob · `toolu_01B6h8h8hAs4MnXVjLvLLeUC`</summary>

```json
{
  "pattern": "*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "70c16201-42fa-40e9-8878-bda1aa3f4f0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcU1fzx4XwsSpeqN3HDsV5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18371,
      "cache_read_input_tokens": 23813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18371
      },
      "output_tokens": 25,
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

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9facc9f4edacaa35",
  "tool_use_id": "toolu_01RfECVzK9DgYeJA3Mhw8imG",
  "description": "Reading docs/paper/experiments.tex",
  "usage": {
    "total_tokens": 19405,
    "tool_uses": 1,
    "duration_ms": 2049
  },
  "last_tool_name": "Read",
  "uuid": "be2beae2-6b32-47c7-8348-3da5875b907e",
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_019f9ZoS1P3bZxXzm4RJad8q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RfECVzK9DgYeJA3Mhw8imG",
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "8741423f-e057-409e-a014-58d74c567fb7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F52bUcrX9BUoBkMGS7rmxc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19396,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19396,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9facc9f4edacaa35",
  "tool_use_id": "toolu_01RfECVzK9DgYeJA3Mhw8imG",
  "description": "Reading docs/paper/method.tex",
  "usage": {
    "total_tokens": 19408,
    "tool_uses": 2,
    "duration_ms": 2058
  },
  "last_tool_name": "Read",
  "uuid": "628b9ebf-6080-4a24-9da9-b87d86da3cd6",
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01XZ6VEfWbUXJcHyud6z474n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RfECVzK9DgYeJA3Mhw8imG",
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "253ea62b-0ea0-4e91-bb0b-4cc1831243c5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F52bUcrX9BUoBkMGS7rmxc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19396,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19396,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 20 · 2026-05-19T15:05:20.008Z_

<details><summary>↩ Tool result · `toolu_019f9ZoS1P3bZxXzm4RJad8q`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); RSA uses task-level blocking ($N_\text{eff} = 10$) and probes use demo-level train/test splits.
13	All patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
14	
15	%------------------------------------------------------------------
16	\subsection{Framework Validation: Token-Level Specialization}
17	\label{sec:token_specialization}
18	
19	As a sanity check on the experimental framework, we train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
20	
21	\paragraph{Image tokens are instruction-blind (expected).}
22	As predicted by the causal mask and frozen encoder, image\_mean instruction classification remains at chance ($10\%$) across all 32 layers in all conditions (Table~\ref{tab:dense_routing_main}).
23	Both linear and MLP probes corroborate this, as does standalone DINOv2 ($10\%$; Appendix~\ref{sec:instruction_invariance_appendix}).
24	
25	\paragraph{Readout token as multimodal hub.}
26	Trained readout achieves $100\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\ref{sec:loocv}); untrained achieves $100\%$ at L1 but decays to $82\%$ by L31.
27	The readout is thus the primary locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\%$ vs.\ $82.7\%$; Appendix~\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
28	
29	\begin{table}[t]
30	\centering
31	\caption{Cross-instruction 10-way classification at selected layers (full profile in Appendix~\ref{sec:dense_routing}). Image\_mean remains at chance ($10\%$) in all conditions; trained readout reaches $100\%$ at L1 and holds; untrained readout decays from L1 to L31.}
32	\label{tab:dense_routing_main}
33	\small
34	\begin{tabular}{lccc}
35	\toprule
36	Layer & Trained readout & Untrained readout & Image\_mean \\
37	\midrule
38	L0 & 10.0\% & 10.0\% & 10.0\% \\
39	L1 & 100.0\% & 100.0\% & 10.0\% \\
40	L4 & 100.0\% & 99.1\% & 10.0\% \\
41	L8 & 100.0\% & 98.2\% & 10.0\% \\
42	L16 & 100.0\% & 92.3\% & 10.0\% \\
43	L31 & 100.0\% & 82.0\% & 10.0\% \\
44	\bottomrule
45	\end{tabular}
46	\end{table}
47	
48	%------------------------------------------------------------------
49	\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}
50	\label{sec:learned_routing}
51	
52	\paragraph{Three-level routing gradient at L1.}
53	We compare L1 readout attention across three conditions (Table~\ref{tab:routing_gradient}; Figure~\ref{fig:attention_profile}): untrained networks allocate 0/32 instruction-dominant heads ($11.7\%$ text); Llama-2 base 9/32 ($36.5\%$); VLA fine-tuning 24/32 ($57.7\%$), a redistribution beyond inherited priors.
54	Per-token normalization ($38.2\times$ text-to-image ratio; Appendix~\ref{sec:attention_decomp}) corroborates this redistribution.
55	
56	\paragraph{Redistribution of routing across depth.}
57	The 32-layer profile (Figure~\ref{fig:attention_profile}) shows qualitatively distinct patterns.
58	Llama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).
59	VLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30).
60	Head counts reflect single-sample extraction; threshold sensitivity (30\%--70\%) analysis confirms ordering robustness across classification boundaries (Appendix~\ref{sec:threshold_sensitivity}).
61	
62	\paragraph{Task-specific sharpening.}
63	A fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\ 6--11), an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute.
64	Probe accuracy is preserved (L1: $99.7\%$; Appendix~\ref{app:finetuned_probe}).
65	
66	\paragraph{Probe robustness corroborates the pattern.}
67	Cross-instruction probes corroborate the three-condition gradient (Appendix Figure~\ref{fig:probe_conditions_appendix}).
68	Training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\_mean changes minimally ($\Delta \leq 1.7\%$; Appendix~\ref{sec:training_effect_summary},~\ref{sec:action_r2_threecond}).
69	
70	\paragraph{Open-loop functional sensitivity.}
71	We ablate attention to instruction tokens at the readout position.
72	Ablating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\footnote{$R^2$ values differ from Table~\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.
73	We compare against 10 random subsets of 24 heads (Appendix~\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \pm 0.013$ ($z = -2.73$, $p = 0.003$).
74	Dominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.
75	In the original extraction pipeline (\S\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\Delta \approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\ref{tab:per_task_r2}).
76	
77	\paragraph{Action trajectory validation.}
78	Ablating 24 instruction-dominant heads alters $72.3\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\%$), concentrated on the gripper dimension (shift $0.291$ vs.\ $< 0.034$; Tables~\ref{tab:attention_decomp},~\ref{tab:per_dim_mae}; Appendix~\ref{sec:action_trajectory}).
79	
80	\paragraph{Dose-response gradient.}
81	Ablating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \to 0.639$; Figure~\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\ref{sec:action_trajectory}).
82	
83	\paragraph{Counterfactual instruction analysis.}
84	Replacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\ref{tab:counterfactual}).
85	Token novelty ($1 - \text{Jaccard}$) predicts the ordering ($\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.
86	L1 ablation ($d = 0.65$) falls within this range (Appendix~\ref{sec:action_trajectory}).
87	
88	\begin{table}[t]
89	\centering
90	\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\% vs.\ 100.0\% in Table~\ref{tab:dense_routing_main}): task-level vs.\ LOOCV splits.}
91	\label{tab:routing_gradient}
92	\small
93	\begin{tabular}{lccccc}
94	\toprule
95	Condition & Heads & Text attn & L1 acc & L31 acc & Mode \\
96	\midrule
97	VLA Trained & 24/32 & 57.7\% & 99.6\% & 100.0\% & immed.+stable \\
98	Llama-2 base & 9/32 & 36.5\% & 80.2\% & 100.0\% & gradual+stable \\
99	Untrained & 0/32 & 11.7\% & 100.0\% & 82.0\% & incid.+forget \\
100	\bottomrule
101	\end{tabular}
102	\end{table}
103	
104	\begin{figure}[t]
105	\centering
106	\includegraphics[width=0.75\columnwidth]{figures/fig_32layer_attention.pdf}
107	\caption{Instruction-dominant heads ($>50\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\ref{fig:probe_conditions_appendix}.}
108	\label{fig:attention_profile}
109	\end{figure}
110	
111	%------------------------------------------------------------------
112	\subsection{Non-Monotonic Refinement of Vision Encoder Output}
113	\label{sec:nonmonotonic}
114	
115	\paragraph{Vision encoder provides geometric foundation.}
116	Table~\ref{tab:rsa_overview} reports RSA $\rho$ and probe $R^2$ between representations and actions.
117	DINOv2 \texttt{cls\_token} achieves the highest RSA ($\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\ref{sec:cka_appendix}).
118	
119	\paragraph{Middle-layer peak (metric-dependent).}
120	Under RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\_mean $\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).
121	The readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\Delta = 0.048$ (Table~\ref{tab:rsa_overview}).
122	Under linear CKA, this pattern disappears (monotonic increase; Appendix~\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.
123	
124	\paragraph{Training primarily enhances readout decodability.}
125	Best-vs-best RSA gain is non-significant on LIBERO-Goal ($\Delta\rho = 0.017$, $3\%$, $N{=}10$ tasks; Appendix Table~\ref{tab:training_effects}), though LIBERO-Spatial yields a significant geometric gain ($\Delta = +0.023$, $p < 0.001$; Appendix~\ref{sec:cross_benchmark_appendix}).
126	The $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.
127	Functional improvements are larger: readout $R^2$ $\Delta = +0.069$ ($p < 0.0001$, 95\% CI $[0.047, 0.090]$), image\_mean $\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.
128	
129	\begin{table}[t]
130	\centering
131	\caption{RSA $\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\ref{sec:cka_appendix}). VLA rows: peak values. \textbf{Bold}: best; \underline{underline}: second.}
132	\label{tab:rsa_overview}
133	\small
134	\begin{tabular}{lcccc}
135	\toprule
136	Source & RSA $\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\
137	\midrule
138	DINOv2 cls\_token & \textbf{0.692} & 0.634 & --- & --- \\
139	VLA Trained readout & \underline{0.643} & \textbf{0.678} & L12 & L13 \\
140	Fused DinoSigLIP & 0.634 & --- & --- & --- \\
141	VLA Trained image\_mean & 0.628 & \underline{0.655} & L12 & L8--L10$^\dagger$ \\
142	DinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\
143	VLA Untrained image\_mean & 0.612 & 0.640 & L0 & L0 \\
144	VLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\
145	CLIP ViT-L/14$^\ddagger$ & 0.557 & 0.587 & --- & --- \\
146	\bottomrule
147	\multicolumn{5}{l}{\footnotesize $^\dagger$$R^2$ peak region across 5 seeds ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).} \\
148	\multicolumn{5}{l}{\footnotesize $^\ddagger$RSA uses \texttt{patch\_mean}; $R^2$ uses \texttt{cls\_token} (each encoder's best aggregation).}
149	\end{tabular}
150	\end{table}
151	
152	\begin{figure}[t]
153	\centering
154	\includegraphics[width=0.92\columnwidth]{figures/fig3.pdf}
155	\caption{Per-layer RSA ($\rho$). Trained image\_mean follows an inverted-U (L0 $0.612 \to$ L12 $0.628 \to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}
156	\label{fig:layer_curves}
157	\end{figure}
158	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RfECVzK9DgYeJA3Mhw8imG",
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "f9e255c4-1f32-449a-b82e-66808e68031d"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T15:05:20.012Z_

<details><summary>↩ Tool result · `toolu_01XZ6VEfWbUXJcHyud6z474n`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (970K episodes spanning multiple robot platforms and task types) and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each), which was not part of the pretraining mixture.
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}); a fourth condition (task-specific fine-tuning on LIBERO) is compared in \S\ref{sec:learned_routing}.
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context and is thus the natural site for multimodal integration before action prediction);
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
24	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} (\texttt{patch\_mean}), a VL-pretrained baseline;
25	(f)~\textbf{Branch-split}, the DINOv2 (1{,}024-D) and SigLIP (1{,}152-D) branches before fusion.
26	Throughout, L0 denotes the embedding layer output, L1--L31 the 32 transformer layers, and L32 the output after the final layer norm.
27	We cross two factors: \emph{training status} (trained vs.\ untrained) and \emph{instruction presence} (with vs.\ without task description) in a $2\times 2$ factorial design.
28	
29	%------------------------------------------------------------------
30	\subsection{Cross-Instruction Probes}
31	\label{sec:cross_instruction_probes}
32	
33	To test whether different token types encode instruction identity, we construct a cross-instruction dataset: each visual frame is paired with all 10 task instructions, producing 10 representation vectors per frame per layer.
34	A linear classifier (10-way) is trained to identify which instruction was present, separately for image\_mean and readout token positions.
35	We validate with leave-one-out cross-validation (LOOCV) over 10 folds, each holding out one task's instructions, to verify that results reflect generalizable instruction encoding rather than memorization.
36	
37	%------------------------------------------------------------------
38	\subsection{Attention Pattern Analysis}
39	\label{sec:attention_analysis}
40	
41	We analyze attention distributions at the readout token position across all 32 layers, categorizing each head as instruction-dominant ($>50\%$ attention to instruction tokens) or image-dominant, with detailed per-head decomposition at L1.
42	This complements the cross-instruction probe by revealing the \emph{mechanism} through which instruction information reaches the readout token.
43	
44	%------------------------------------------------------------------
45	\subsection{Representational Similarity Analysis}
46	\label{sec:rsa}
47	
48	We adopt RSA~\cite{kriegeskorte2008} to quantify geometric alignment between representations and the action space.
49	For each task, we compute pairwise $N \times N$ representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, using within-task observation pairs from 50 demonstrations.
50	Alignment is measured via Spearman $\rho$ between the upper-triangular entries of the representation and action RDMs; higher $\rho$ indicates that representationally similar observations require similar actions.
51	We report mean $\rho$ across 10 tasks with 95\% confidence intervals from 10{,}000 bootstrap resamples; resampling is performed at the task level ($N=10$), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure~\cite{nili2014toolbox}.
52	
53	%------------------------------------------------------------------
54	\subsection{Functional Action Probes}
55	\label{sec:probes}
56	
57	RSA measures geometric alignment but not decodability.
58	We complement it with MLP probes~\cite{alain2017}: two-layer networks ($d_\text{in} \to 256 \to 7$) trained to predict 7-D action vectors from frozen representations (Adam, lr${}=10^{-3}$, batch 256, 50 epochs, early stopping patience 5), with demo-level train/test splits (demos 0--39 vs.\ 40--49).
59	We report per-task macro-averaged $R^2$ across 10 tasks with bootstrap paired comparisons (10{,}000 resamples).
60	
61	\paragraph{Why RSA over CKA.}
62	RSA captures relative distance structure via scale-invariant Spearman rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\ 7-D).
63	CKA~\cite{kornblith2019} measures global subspace overlap, which can remain high even when geometric structure differs.
64	We report both in Appendix~\ref{sec:cka_appendix}; the divergence between metrics (\S\ref{sec:nonmonotonic}) indicates neither alone fully characterizes representational structure.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RfECVzK9DgYeJA3Mhw8imG",
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "668d2949-b1b0-48fa-8b0e-07915ee2cd8e"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a9facc9f4edacaa35",
  "tool_use_id": "toolu_01RfECVzK9DgYeJA3Mhw8imG",
  "status": "completed",
  "output_file": "",
  "summary": "Read experiments.tex and method.tex",
  "usage": {
    "total_tokens": 26978,
    "tool_uses": 2,
    "duration_ms": 19079
  },
  "uuid": "3bdc6904-c51b-4985-8939-ea459b73d0a5",
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088"
}
```

---

### Tool result

_source line 23 · 2026-05-19T15:05:37.021Z_

<details><summary>↩ Tool result · `toolu_01RfECVzK9DgYeJA3Mhw8imG`</summary>

```text
## Summary of Experimental Setup Details

### File 1: experiments.tex

**Section Labels:**
- `sec:experiments`
- `sec:setup`
- `sec:token_specialization`
- `sec:learned_routing`
- `sec:nonmonotonic`

**Model Details:**
- **OpenVLA-7B**: Base checkpoint pretrained on Open X-Embodiment (970K episodes, multiple robot platforms/task types). Specific checkpoint mentioned: released checkpoint for VLA-trained condition.
- Three LLM conditions compared:
  1. VLA-trained (released checkpoint)
  2. Pretrained Llama-2 base (no VLA fine-tuning)
  3. Untrained (6.74B parameters reinitialized)
- Vision backbone: DinoSigLIP (frozen): DINOv2 ViT-L/14 + SigLIP-SO400M
- Projector: 2,176-D to 4,096-D MLP
- Llama-2 7B (6.74B parameters) with 32 transformer layers
- Comparison models: DINOv2 ViT-L/14, CLIP ViT-L/14

**Dataset:**
- **LIBERO-Goal**: 10 tasks, 50 demonstrations each
- Total observations: N = 63,228 (after excluding terminal frames without next-action labels; 63,728 total raw)
- Additional: LIBERO-Spatial (mentioned in cross-benchmark validation, Appendix reference)
- Splits: Demo-level train/test splits (demos 0-39 vs. 40-49)

**Hyperparameters:**
- **MLP probes**: Input → 256 → 7 (2 layers)
  - Optimizer: Adam
  - Learning rate: lr = 10^-3
  - Epochs: 50
  - Early stopping: enabled
- **Cross-instruction classification**: 10-way classification, LOOCV validation

**Metric Definitions:**
- **RSA (Representational Similarity Analysis)**: Spearman ρ between cosine-distance representation RDMs and Euclidean-distance action RDMs
  - Bootstrap confidence intervals: 10,000 CIs
  - Task-level blocking (N_eff = 10)
  - Pairwise comparison of 50 demonstrations per task
- **Probe R²**: Mean R² from MLP probes predicting 7-D actions
- **Cross-instruction classification accuracy**: 10-way classification (% correct)
- **Action trajectory changes**: Cohen's d (effect size)
- **CKA (Canonical Correlation Analysis)**: Linear CKA mentioned as alternative metric (Appendix reference)
- **Attention analysis**: Head counts, text attention percentage

**Hardware:**
- Not explicitly mentioned

**Representation Sources Extracted:**
1. DinoSigLIP+Projector (4,096-D)
2. LLM image_mean (32 layers)
3. LLM readout (32 layers)
4. DINOv2 cls_token and patch_mean
5. CLIP patch_mean
6. Branch-split (DINOv2 1,024-D / SigLIP 1,152-D before fusion)

---

### File 2: method.tex

**Section Labels:**
- `sec:method`
- `sec:model_data`
- `sec:repr_extraction`
- `sec:cross_instruction_probes`
- `sec:attention_analysis`
- `sec:rsa`
- `sec:probes`

**Model Details:**
- **OpenVLA-7B**: 
  - Frozen DinoSigLIP vision backbone: DINOv2 ViT-L/14 + SigLIP-SO400M
  - MLP projector: 2,176-D → 4,096-D
  - Llama-2 7B (6.74B parameters) with 32 transformer layers
  - Autoregressive decoding of 7-D actions
  - Base checkpoint: pretrained on Open X-Embodiment (970K episodes)
- Three LLM conditions:
  1. VLA-trained (released checkpoint)
  2. Llama-2 base (pretrained backbone, no VLA fine-tuning)
  3. Untrained (6.74B parameters reinitialized via `from_config()`)
  - Fourth condition: task-specific fine-tuning on LIBERO (mentioned in Section 3.2)

**Dataset:**
- **LIBERO-Goal**: 10 tasks, 50 demonstrations each
- Not part of pretraining mixture
- Demo-level train/test splits: demos 0-39 (train) vs. 40-49 (test)

**Hyperparameters:**
- **MLP Probes**: Two-layer networks (d_in → 256 → 7)
  - Optimizer: Adam
  - Learning rate: lr = 10^-3
  - Batch size: 256
  - Epochs: 50
  - Early stopping patience: 5

**Metric Definitions:**
- **RSA**: Spearman ρ between upper-triangular entries of RDMs
  - Representation RDMs: cosine distances
  - Action RDMs: Euclidean distances for 7-D action vectors
  - Within-task observation pairs from 50 demonstrations
  - Task-level blocking (N_eff = 10)
  - Bootstrap resamples: 10,000 at task level
  - Mean ρ reported across 10 tasks with 95% CIs
- **Probe R²**: Per-task macro-averaged R² across 10 tasks
  - Predicts 7-D action vectors
  - Demo-level train/test splits
  - Bootstrap paired comparisons: 10,000 resamples
- **CKA**: Canonical Correlation Analysis (mentioned as comparison metric; reported in Appendix)
  - Note: RSA chosen over CKA as primary metric for scale-invariant rank correlation

**Hardware:**
- Not explicitly mentioned

**Layer Structure:**
- L0: embedding layer output
- L1-L31: 32 transformer layers
- L32: output after final layer norm

**Other Details:**
- Cross two factors: training status (trained vs. untrained) × instruction presence (with vs. without task description) = 2×2 factorial design
- 10 task instructions per evaluation set
- Action dimensionality: 7-D vectors
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "4e3927e4-c437-4d91-a7a9-af3cec8be584",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the following files fully and summarize what experimental setup details are already described (model version/checkpoint, dataset, hyperparameters, metric definitions, hardware):\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex\n\nFor each file, list:\n- Which model(s) are mentioned and their exact names/sources\n- Dataset details (name, split, sample counts)\n- Any hyperparameters mentioned (learning rate, batch size, epochs, optimizer, seed, etc.)\n- Metric definitions (RSA, CKA, probe R², Cohen's d, etc.)\n- Hardware mentioned\n- Section labels (\\label{}) so I know what can be cross-referenced\n\nReport the full details found.",
    "agentId": "a9facc9f4edacaa35",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Experimental Setup Details\n\n### File 1: experiments.tex\n\n**Section Labels:**\n- `sec:experiments`\n- `sec:setup`\n- `sec:token_specialization`\n- `sec:learned_routing`\n- `sec:nonmonotonic`\n\n**Model Details:**\n- **OpenVLA-7B**: Base checkpoint pretrained on Open X-Embodiment (970K episodes, multiple robot platforms/task types). Specific checkpoint mentioned: released checkpoint for VLA-trained condition.\n- Three LLM conditions compared:\n  1. VLA-trained (released checkpoint)\n  2. Pretrained Llama-2 base (no VLA fine-tuning)\n  3. Untrained (6.74B parameters reinitialized)\n- Vision backbone: DinoSigLIP (frozen): DINOv2 ViT-L/14 + SigLIP-SO400M\n- Projector: 2,176-D to 4,096-D MLP\n- Llama-2 7B (6.74B parameters) with 32 transformer layers\n- Comparison models: DINOv2 ViT-L/14, CLIP ViT-L/14\n\n**Dataset:**\n- **LIBERO-Goal**: 10 tasks, 50 demonstrations each\n- Total observations: N = 63,228 (after excluding terminal frames without next-action labels; 63,728 total raw)\n- Additional: LIBERO-Spatial (mentioned in cross-benchmark validation, Appendix reference)\n- Splits: Demo-level train/test splits (demos 0-39 vs. 40-49)\n\n**Hyperparameters:**\n- **MLP probes**: Input → 256 → 7 (2 layers)\n  - Optimizer: Adam\n  - Learning rate: lr = 10^-3\n  - Epochs: 50\n  - Early stopping: enabled\n- **Cross-instruction classification**: 10-way classification, LOOCV validation\n\n**Metric Definitions:**\n- **RSA (Representational Similarity Analysis)**: Spearman ρ between cosine-distance representation RDMs and Euclidean-distance action RDMs\n  - Bootstrap confidence intervals: 10,000 CIs\n  - Task-level blocking (N_eff = 10)\n  - Pairwise comparison of 50 demonstrations per task\n- **Probe R²**: Mean R² from MLP probes predicting 7-D actions\n- **Cross-instruction classification accuracy**: 10-way classification (% correct)\n- **Action trajectory changes**: Cohen's d (effect size)\n- **CKA (Canonical Correlation Analysis)**: Linear CKA mentioned as alternative metric (Appendix reference)\n- **Attention analysis**: Head counts, text attention percentage\n\n**Hardware:**\n- Not explicitly mentioned\n\n**Representation Sources Extracted:**\n1. DinoSigLIP+Projector (4,096-D)\n2. LLM image_mean (32 layers)\n3. LLM readout (32 layers)\n4. DINOv2 cls_token and patch_mean\n5. CLIP patch_mean\n6. Branch-split (DINOv2 1,024-D / SigLIP 1,152-D before fusion)\n\n---\n\n### File 2: method.tex\n\n**Section Labels:**\n- `sec:method`\n- `sec:model_data`\n- `sec:repr_extraction`\n- `sec:cross_instruction_probes`\n- `sec:attention_analysis`\n- `sec:rsa`\n- `sec:probes`\n\n**Model Details:**\n- **OpenVLA-7B**: \n  - Frozen DinoSigLIP vision backbone: DINOv2 ViT-L/14 + SigLIP-SO400M\n  - MLP projector: 2,176-D → 4,096-D\n  - Llama-2 7B (6.74B parameters) with 32 transformer layers\n  - Autoregressive decoding of 7-D actions\n  - Base checkpoint: pretrained on Open X-Embodiment (970K episodes)\n- Three LLM conditions:\n  1. VLA-trained (released checkpoint)\n  2. Llama-2 base (pretrained backbone, no VLA fine-tuning)\n  3. Untrained (6.74B parameters reinitialized via `from_config()`)\n  - Fourth condition: task-specific fine-tuning on LIBERO (mentioned in Section 3.2)\n\n**Dataset:**\n- **LIBERO-Goal**: 10 tasks, 50 demonstrations each\n- Not part of pretraining mixture\n- Demo-level train/test splits: demos 0-39 (train) vs. 40-49 (test)\n\n**Hyperparameters:**\n- **MLP Probes**: Two-layer networks (d_in → 256 → 7)\n  - Optimizer: Adam\n  - Learning rate: lr = 10^-3\n  - Batch size: 256\n  - Epochs: 50\n  - Early stopping patience: 5\n\n**Metric Definitions:**\n- **RSA**: Spearman ρ between upper-triangular entries of RDMs\n  - Representation RDMs: cosine distances\n  - Action RDMs: Euclidean distances for 7-D action vectors\n  - Within-task observation pairs from 50 demonstrations\n  - Task-level blocking (N_eff = 10)\n  - Bootstrap resamples: 10,000 at task level\n  - Mean ρ reported across 10 tasks with 95% CIs\n- **Probe R²**: Per-task macro-averaged R² across 10 tasks\n  - Predicts 7-D action vectors\n  - Demo-level train/test splits\n  - Bootstrap paired comparisons: 10,000 resamples\n- **CKA**: Canonical Correlation Analysis (mentioned as comparison metric; reported in Appendix)\n  - Note: RSA chosen over CKA as primary metric for scale-invariant rank correlation\n\n**Hardware:**\n- Not explicitly mentioned\n\n**Layer Structure:**\n- L0: embedding layer output\n- L1-L31: 32 transformer layers\n- L32: output after final layer norm\n\n**Other Details:**\n- Cross two factors: training status (trained vs. untrained) × instruction presence (with vs. without task description) = 2×2 factorial design\n- 10 task instructions per evaluation set\n- Action dimensionality: 7-D vectors"
      }
    ],
    "totalDurationMs": 19082,
    "totalTokens": 28537,
    "totalToolUseCount": 2,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7565,
      "cache_read_input_tokens": 19396,
      "output_tokens": 1569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7565
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1569,
          "cache_read_input_tokens": 19396,
          "cache_creation_input_tokens": 7565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7565,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 0,
      "bashCount": 0,
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

### Tool result

_source line 24 · 2026-05-19T15:05:37.654Z_

<details><summary>↩ Tool result · `toolu_014MzygpaEptxwiAfBsxw6aw`</summary>

```text
Error: result (62,339 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "c3017cc0-2f18-4d2e-925a-a1eafacc32ec",
  "tool_use_result": {
    "content": "Error: result (62,339 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"finetuned_probe_profile\": {\"status\": \"DONE\", \"spec\": {\"command\": \"/root/miniconda3/envs/libero/bin/python scripts/libero_finetuned_probe_profile.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal/\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal/\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/finetuned_probe_profile.log\", \"eval_data\": \"LIBERO-Goal 10 tasks x 50 demos, 10-way cross-instruction LOOCV\"}}, \"libero_finetuned_probe\": {\"status\": \"PREPARING\"}, \"libero_finetuned_attention\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/libero_finetuned_attention_profile.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": 10, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": null, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/libero_finetuned_attention_profile.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/libero_finetuned_attention.log\", \"eval_data\": \"libero_goal_10tasks_frame0\"}}, \"behavioral_smoketest_diag\": {\"status\": \"PREPARING\"}, \"behavioral_smoketest\": {\"status\": \"DONE\", \"spec\": {\"command\": \"NUMBA_DISABLE_JIT=1 CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python behavioral_smoketest.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/LIBERO\", \"data_count\": \"1 task x 3 ep\", \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"LIBERO-Goal task_id=0, 3 episodes\"}}, \"matched_ablation_controls\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=0 python /root/vla-ssd/scripts/matched_ablation_controls.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": \"3 tasks x 10 demos x 50 steps = 1500 samples, 7 passes each = 10500 total\", \"model_name\": \"openvla-7b\", \"seed\": \"42,123,456,789,1024 (random-24); deterministic (image-dominant-24)\", \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"LIBERO libero_goal 3 tasks, 10 demos each, 50 timesteps\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/matched_ablation_controls.log\", \"checkpoint_path\": \"N/A (inference-only)\"}}, \"task_routing_loo_sensitivity\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 loo_sensitivity.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/task_complexity_routing.json\", \"data_count\": 10, \"model_name\": \"N/A\", \"seed\": 42, \"checkpoint_source\": \"task_complexity_routing\", \"eval_data\": \"task_complexity_routing.json\"}}, \"attention_normalization_entropy\": {\"status\": \"DONE\"}, \"trajectory_level_cohens_d\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/trajectory_level_cohens_d.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": \"14 conditions, 30-50 demos each\", \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"libero_goal 5 tasks\"}}, \"groundtruth_action_error\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python -u scripts/groundtruth_action_error.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": 4500, \"model_name\": \"openvla-7b\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\"}}, \"counterfactual_token_overlap\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/token_overlap_analysis.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/counterfactual_combined.json\", \"data_count\": 3, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"counterfactual_instruction\", \"eval_data\": \"counterfactual_combined.json\"}}, \"task_complexity_routing\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python task_complexity_analysis.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/per_task_r2_distribution.json\", \"data_count\": 10, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"per_task_r2_distribution.json\", \"eval_data\": \"LIBERO-Goal 10 tasks\"}}, \"llama2_base_control\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python create_llama2_base_openvla.py + cross_instruction_extract_dense.py --condition llama2base + l1_attention_visualization.py --condition llama2base\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction/\", \"data_count\": 500, \"model_name\": \"openvla-7b-llama2base (Llama-2-7B base weights injected into OpenVLA)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-llama2base/\", \"eval_data\": \"LIBERO cross-instruction 10 tasks × 50 demos (same as cross_inst_extract_trained)\"}}, \"specificity_control_action\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl python -u scripts/specificity_control_action.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": 1500, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"libero_goal 3 tasks x 10 demos x 50 timesteps\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/specificity_control_action.log\"}}, \"counterfactual_instruction\": {\"status\": \"DONE\", \"spec\": {\"command\": \"MUJOCO_GL=egl python -u scripts/counterfactual_instruction.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": 6000, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/counterfactual_instruction.log\"}}, \"attention_decomposition\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 attention_decomposition_and_r2.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/attention/\", \"data_count\": \"5 trained samples + 32-head untrained data\", \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"existing attention data\", \"eval_data\": \"L1 attention summaries\"}}, \"action_metrics_extended\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python3 (CPU-only, from existing JSONs)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/\", \"data_count\": 5000, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"N/A (analysis only)\", \"eval_data\": \"action_trajectory_analysis.json + action_trajectory_control.json\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/action_metrics_extended.json\"}}, \"cross_layer_L13_ablation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=1 python -u scripts/action_trajectory_L13_ablation.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": \"5 tasks x 10 demos x 50 timesteps = 2500 samples\", \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/action_trajectory_L13_ablation.log\"}}, \"cross_layer_L8_ablation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_L8_ablation.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": 2500, \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/action_trajectory_L8_ablation.log\"}}, \"dose_response_curve\": {\"status\": \"DONE\", \"spec\": {\"command\": \"dose_response_curve.py --conditions 4,8,12,16 (cuda:0) + --conditions 20,24,28,32 (cuda:1)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": \"5 tasks x 10 demos x 50 timesteps x 8 conditions = 20000 passes\", \"model_name\": \"openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\"}}, \"permutation_test_I2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/permutation_test_I2.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json\", \"data_count\": \"5 tasks x 2 conditions + 7 dims x 2 conditions\", \"model_name\": \"n/a (statistical test)\", \"seed\": 42, \"checkpoint_path\": \"n/a\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/permutation_test_I2.json\", \"checkpoint_source\": \"n/a\", \"eval_data\": \"action_trajectory_extended_analysis.json\"}}, \"action_trajectory_cpu_analysis\": {\"status\": \"PREPARING\"}, \"action_trajectory_control\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_control.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_control.log\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"47936\", \"log_path\": \"~/runs/vla-ssd/action_trajectory_control.log\", \"submitted_at\": \"2026-05-18T11:53:06.410Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"behavioral_pilot_v2\": {\"status\": \"PREPARING\"}, \"action_trajectory_analysis\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python scripts/action_trajectory_analysis.py\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"5 tasks x 10 demos x 50 timesteps = 2500 forward passes x 2 conditions\", \"model_name\": \"OpenVLA-7b (openvla-7b base pretrained)\", \"seed\": \"42\", \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"LIBERO-Goal demo observations (open-loop, no execution)\", \"checkpoint_path\": \"N/A (inference only)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.log\"}}, \"behavioral_pilot_w4\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && MUJOCO_GL=egl HDF5_USE_FILE_LOCKING=FALSE PYTHONUNBUFFERED=1 python /root/vla-ssd/scripts/behavioral_pilot.py\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"24738\", \"log_path\": \"~/runs/vla-ssd/behavioral_pilot_w4.log\", \"submitted_at\": \"2026-05-18T10:23:14.928Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"3 tasks x 10 episodes x 2 conditions = 60 episodes\", \"model_name\": \"OpenVLA-7b (openvla-7b)\", \"seed\": \"42\", \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\", \"eval_data\": \"LIBERO-Goal benchmark (3 selected tasks, 300 max steps per episode)\", \"wall_clock_seconds\": 508.3, \"gpu_hours\": 0.14}}, \"behavioral_pilot\": {\"status\": \"PREPARING\"}, \"threecond_multiseed_r2_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && CUDA_VISIBLE_DEVICES=0 python scripts/threecond_multiseed_probe_v2.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.log\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,llama2base}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 3 conditions\", \"model_name\": \"ActionMLPProbe(4096->256->7)\", \"seed\": \"42,123,456\", \"split\": \"sequential_80_20_no_shuffle\", \"r2_space\": \"original_denormalized\", \"checkpoint_source\": \"pre-extracted features from openvla-7b / openvla-7b-untrained / openvla-7b-llama2base\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/ (10 tasks, 50 demos, sequential split demo_0-39 train / demo_40-49 val)\", \"checkpoint_path\": \"N/A (probe experiment)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.log\"}}, \"threecond_multiseed_r2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && CUDA_VISIBLE_DEVICES=0 python scripts/threecond_multiseed_probe.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,llama2base}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 3 conditions\", \"model_name\": \"ActionMLPProbe(4096->256->7)\", \"seed\": \"42,123,456\", \"checkpoint_source\": \"pre-extracted features from openvla-7b / openvla-7b-untrained / openvla-7b-llama2base\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/ (10 tasks, 50 demos each, 80/20 split)\", \"checkpoint_path\": \"N/A (probe experiment)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/threecond_multiseed.log\"}}, \"random_subset_ablation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/random_subset_ablation.py --n_demos 50 --n_random 10 --output /root/autodl-tmp/vla-ssd/results/random_subset_ablation.json\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"ActionMLPProbe(4096->256->7) with L1 head ablation\", \"seed\": \"10 random seeds for subset selection\", \"checkpoint_source\": \"pre-extracted features from openvla-7b (trained)\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/ (10 tasks, 50 demos, sequential split)\", \"checkpoint_path\": \"N/A (probe experiment, no checkpoint saved)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/random_subset_ablation.json\"}}, \"linear_probe_last_preaction\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && CUDA_VISIBLE_DEVICES=1 python scripts/linear_probe_last_preaction.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 2 conditions x 33 layers\", \"model_name\": \"Linear(4096,7)\", \"seed\": 42, \"checkpoint_source\": \"fulllayer_action_probe features (pre-extracted)\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"checkpoint_path\": \"N/A (probe experiment)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/logs/linear_probe_last_preaction.log\"}}, \"fulllayer_action_probe\": {\"status\": \"PREPARING\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/vla-ssd/scripts/fulllayer_action_probe.py\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"700649\", \"log_path\": \"~/runs/vla-ssd/fulllayer_action_probe.log\", \"submitted_at\": \"2026-05-16T03:50:36.686Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"l1_head_ablation_control8\": {\"status\": \"PREPARING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_control8.py --demos_per_task 50 --readout_layers 1 8 13 --output /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos_control8.json\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"905194\", \"log_path\": \"~/runs/vla-ssd/l1_head_ablation_control8.log\", \"submitted_at\": \"2026-05-17T18:29:35.353Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"l1_head_ablation_50demos\": {\"status\": \"PREPARING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"905824\", \"log_path\": \"~/runs/vla-ssd/l1_head_ablation_50demos.log\", \"submitted_at\": \"2026-05-17T18:36:35.597Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"llama2base_action_probe\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && CUDA_VISIBLE_DEVICES=1 python scripts/llama2base_action_probe.py\\\"\", \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"pid\": \"913312\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/llama2base_action_probe/three_condition_comparison.json\", \"submitted_at\": \"2026-05-17T20:55:56.743Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero_goal/\", \"data_count\": \"50 demos/task x 10 tasks\", \"model_name\": \"meta-llama/Llama-2-7b-hf (via OpenVLA architecture)\", \"seed\": 42, \"checkpoint_path\": \"N/A (probe experiment, no checkpoint)\", \"wall_clock_seconds\": 3995.4, \"gpu_hours\": 1.11}}, \"ablation_50demos_main\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py --demos_per_task 50 --readout_layers 1 8 13\", \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero_goal/\", \"data_count\": \"50 demos/task x 10 tasks x 3 conditions\", \"model_name\": \"openvla-7b (trained)\", \"seed\": 42, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json\"}}, \"ablation_p2_demo_sensitivity\": {\"status\": \"DONE\", \"spec\": {\"command\": \"subsample 25 from 50 demos, reuse existing extracted features\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"720669\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/demo_sensitivity_25/results.json\", \"submitted_at\": \"2026-05-16T10:17:17.128Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/demo_sensitivity_25/\", \"data_count\": \"25 demos/task x 10 tasks\", \"model_name\": \"openvla-7b (trained)\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis-only)\", \"wall_clock_seconds\": 121729.4, \"gpu_hours\": 33.81}}, \"ablation_50demos_control8\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_control8.py --demos_per_task 50 --readout_layers 1 8 13\", \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero_goal/\", \"data_count\": \"50 demos/task x 10 tasks x 1 condition\", \"model_name\": \"openvla-7b (trained)\", \"seed\": 42, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos_control8.json\"}}, \"l1_head_ablation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe.py --readout_layers 1 8 13 --demos_per_task 5 2>&1 | tee /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_log.txt\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"896931\", \"log_path\": \"~/runs/vla-ssd/l1_head_ablation.log\", \"submitted_at\": \"2026-05-17T14:49:06.028Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4379.9, \"gpu_hours\": 1.22}}, \"cross_inst_spatial_trained\": {\"status\": \"DONE\"}, \"plan010_rsa_spatial\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/rsa_libero_spatial.py > /root/autodl-tmp/vla-ssd/logs/rsa_spatial.log 2>&1\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"708431\", \"log_path\": \"~/runs/vla-ssd/plan010_rsa_spatial.log\", \"submitted_at\": \"2026-05-16T06:25:55.106Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 92663.1, \"gpu_hours\": 25.74}}, \"plan010_action_probe_spatial\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/action_probe_libero_spatial.py > /root/autodl-tmp/vla-ssd/logs/action_probe_spatial.log 2>&1\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"708576\", \"log_path\": \"~/runs/vla-ssd/plan010_action_probe_spatial.log\", \"submitted_at\": \"2026-05-16T06:25:57.400Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 92659.9, \"gpu_hours\": 51.48}}, \"rsa_cosine_ablation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/ablations/rsa_cosine_action_metric.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": 500, \"model_name\": \"openvla-7b (features already extracted)\", \"seed\": 42}}, \"rsa_permutation_test\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/ablations/rsa_permutation_null.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": 500, \"model_name\": \"openvla-7b (features already extracted)\", \"seed\": 42}}, \"ablation_p1_seed_robustness\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/ablations/probe_seed_robustness.py --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"718019\", \"log_path\": \"~/runs/vla-ssd/ablation_p1_seed_robustness.log\", \"submitted_at\": \"2026-05-16T09:19:20.361Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": 500, \"model_name\": \"openvla-7b (features, probe only)\", \"seed\": \"multi: [0,1,2,3,42]\", \"wall_clock_seconds\": 3828.3, \"gpu_hours\": 1.06}}, \"ablation_p2_demo_sensitivity_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/ablations/demo_sensitivity.py --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"722187\", \"log_path\": \"~/runs/vla-ssd/ablation_p2_demo_sensitivity_v2.log\", \"submitted_at\": \"2026-05-16T10:34:16.487Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": 500, \"model_name\": \"openvla-7b (features, RSA+probe)\", \"seed\": 42, \"wall_clock_seconds\": 41519.1, \"gpu_hours\": 11.53}}, \"p0_functional_action_delta_probe\": {\"status\": \"DONE\"}, \"p0_functional_probe_v2\": {\"status\": \"DONE\"}, \"d027_trained_no_inst_rsa\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/extract_features.py --task_instruction '' + python /root/vla-ssd/rsa_analysis.py (trained no-inst)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal_no_inst/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim (trained, no instruction)\", \"model_name\": \"openvla/openvla-7b (trained, empty instruction)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_trained_no_inst.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/\"}}, \"d021_output_head_analysis\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python output_head_analysis.py (load trained + untrained state_dicts, compute per-layer Frobenius norm ratio)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/ + openvla-7b-untrained/\", \"data_count\": \"2 models x ~7B params each\", \"model_name\": \"openvla/openvla-7b vs openvla-7b-untrained weight comparison\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/output_head_analysis.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/\", \"note\": \"Worker: worker_ssh_output-head-analysis_20260515T200957. CPU-only analysis. PASS: output head norm ratio > 3x LLM layer mean.\"}}, \"d021_instruction_ablation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/extract_features_no_instruction.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal_no_inst/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50 && python rsa_analysis.py (no-inst features)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal_no_inst/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim (no instruction)\", \"model_name\": \"openvla/openvla-7b-untrained (empty instruction ablation)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_no_instruction.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/\", \"note\": \"Worker: worker_ssh_instruction-ablation_20260515T200929. Gate: PASS = Δ(with-no)>0.10 + CI excludes 0 + no-inst ≤ DINO+0.05. FAIL = no-inst ≥ with-inst−0.05.\"}}, \"lg_pca1024_linear_pertimestep\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python pca_linear_probe_pertimestep.py --trained_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --untrained_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --dino_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --pca_dim 1024 --output /root/autodl-tmp/vla-ssd/results/pca1024_linear_pertimestep.json\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,dinov2}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos, best layer features, 10 timestep bins\", \"model_name\": \"LogisticRegression (PCA-1024), per-timestep evaluation\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/pca1024_linear_pertimestep.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/pca1024_linear_pertimestep.json\"}}, \"lg_rsa_analysis\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python rsa_analysis.py (full run on LIBERO-Goal features)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,dinov2}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers (VLA) / 1 layer (DINO)\", \"model_name\": \"RSA: Spearman(repr_RDM, action_RDM) per layer + CKA\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/\"}}, \"lg_gc_trained_frame0\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_frame0/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_frames 1\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim (frame 0 only)\", \"model_name\": \"GoalClassificationProbe MLP (4096→256→10), trained VLA features frame-0 only\", \"seed\": 42, \"checkpoint_source\": \"lg_extract_trained\", \"note\": \"Frame-0 layer curve: L0=10%, L1=39%, L2=58%, L3+=100%. Shows 3+ layers needed for instruction integration at max visual ambiguity. Worker: worker_ssh_initial-frame-gc\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_libero_goal_frame0/goal_classification/\", \"log_path\": \"~/runs/vla-ssd/lg_gc_trained_frame0.log\"}}, \"lg_gc_dino\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"635723\", \"log_path\": \"~/runs/vla-ssd/lg_gc_dino.log\", \"submitted_at\": \"2026-05-15T17:54:11.228Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 1 layer x 1024 dim\", \"model_name\": \"GoalClassificationProbe MLP (1024->256->10), DINO-V2 features\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/goal_classification/\", \"wall_clock_seconds\": 386.6, \"gpu_hours\": 0.11}}, \"lg_gc_untrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained_libero_goal/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim\", \"model_name\": \"GoalClassificationProbe MLP (4096→256→10), untrained VLA features\", \"seed\": 42, \"checkpoint_source\": \"lg_extract_untrained\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ + /root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_libero_goal/goal_classification/\", \"log_path\": \"~/runs/vla-ssd/lg_gc_untrained.log\"}}, \"lg_gc_trained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir .../trained_libero_goal/ --output_dir .../results/trained_libero_goal/ --probe_type goal_classification --data_dir .../libero_goal/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers\", \"model_name\": \"GoalClassificationProbe MLP (4096→256→10), trained VLA features\", \"seed\": 42, \"checkpoint_source\": \"lg_extract_trained\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/ + /root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_libero_goal/goal_classification/\", \"log_path\": \"~/runs/vla-ssd/lg_gc_trained.log\"}}, \"cross_inst_extract_untrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/instruction_conditional_extract.py --condition untrained --gpu 1\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/\", \"data_count\": \"10 tasks × 50 frames × 10 instructions\", \"model_name\": \"openvla-7b (untrained)\", \"seed\": 42, \"output_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction/untrained_cross_inst.h5\"}}, \"cross_inst_extract_trained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/instruction_conditional_extract.py --condition trained --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/\", \"data_count\": \"10 tasks × 50 frames × 10 instructions\", \"model_name\": \"openvla-7b (trained)\", \"seed\": 42, \"output_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction/trained_cross_inst.h5\"}}, \"openvla-untrained-extract\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir features/untrained/ --gpu 0 --max_demos 50 (retry: reextracted LIVING_ROOM_SCENE6 + STUDY_SCENE1)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps\", \"model_name\": \"openvla/openvla-7b-untrained (LLM 6.74B random from_config, Vision 0.80B preserved)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"log_path\": \"~/runs/vla-ssd/openvla-untrained-extract.log\"}}, \"openvla-trained-extract\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/extract_features.py --model_path openvla-7b --output_dir features/trained/ --gpu 0 --max_demos 50\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"27091\", \"log_path\": \"~/runs/vla-ssd/openvla-trained-extract.log\", \"submitted_at\": \"2026-05-15T10:01:11.065Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps\", \"model_name\": \"openvla/openvla-7b\", \"seed\": 42, \"notes\": \"transformers 版本差异: 模型期望 4.40.1, 实际 4.57.6。trained/untrained 使用同一版本，对比有效。复现时需注意版本匹配。\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"wall_clock_seconds\": 11497.6, \"gpu_hours\": 3.19}}, \"lg_extract_untrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b-untrained (LLM random, SigLIP preserved)\", \"seed\": 42, \"pid\": \"627335\", \"log_path\": \"~/runs/vla-ssd/lg_extract_untrained.log\", \"restarted_at\": \"2026-05-15T17:00:00Z\", \"retry_count\": 1, \"note\": \"--gpu 0 + CUDA_VISIBLE_DEVICES=1 maps to physical cuda:1\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/\"}}, \"lg_extract_trained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b (LIBERO-10 fine-tuned)\", \"seed\": 42, \"pid\": \"627256\", \"log_path\": \"~/runs/vla-ssd/lg_extract_trained.log\", \"restarted_at\": \"2026-05-15T17:00:00Z\", \"retry_count\": 1, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"wall_clock_seconds\": 3204, \"gpu_hours\": 0.89}}, \"dinov2_baseline\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type temporal_distance --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps = 138,090 frames\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/dinov2-large, 304.4M params)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/dinov2-large/\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/\", \"feature_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2/ (503MB, 10 .pt files)\", \"probe_config\": \"MLP (1 hidden layer) trained with Adam + early stopping, task-level 80/20 split, distance-stratified sampling (10 bins x 50 pairs/bin/traj)\", \"feature_dim\": 1024, \"feature_key\": \"cls_token\", \"extraction_time\": \"795.8s, 174 fps, batch_size=32\"}}, \"plan_012_clip_vit_control\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/extract_features_clip.py + python scripts/rsa_clip.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos = 63728 frames\", \"model_name\": \"CLIP ViT-L/14 (openai)\", \"seed\": 42, \"checkpoint_path\": \"/root/vla-ssd/checkpoints/clip-vit-large-patch14/\", \"log_path\": \"/tmp/clip_extract.log\"}}, \"qa_probe_classification\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/qa_probe_classification.py --condition all\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"744973\", \"log_path\": \"~/runs/vla-ssd/qa_probe_classification.log\", \"submitted_at\": \"2026-05-16T22:02:46.068Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/\", \"data_count\": \"10 tasks × 50 demos, 4-class progress + binary subtask\", \"model_name\": \"openvla-7b (trained + untrained)\", \"seed\": 42, \"wall_clock_seconds\": 14729.6, \"gpu_hours\": 4.09}}, \"rsa_per_dof_ablation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/ablations/rsa_per_dof.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": 500, \"model_name\": \"openvla-7b (features already extracted)\", \"seed\": 42}}, \"plan_010_extract_trained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/extract_features.py --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_spatial/ --mode trained --gpu 0 --batch_size 4 --max_demos 50\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"705603\", \"log_path\": \"~/runs/vla-ssd/plan_010_extract_trained.log\", \"submitted_at\": \"2026-05-16T05:18:41.078Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial/\", \"data_count\": 500, \"model_name\": \"openvla-7b (LIBERO-Goal fine-tuned)\", \"seed\": 42, \"wall_clock_seconds\": 11701.5, \"gpu_hours\": 3.25}}, \"plan_010_extract_untrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/extract_features.py --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_spatial/ --mode trained --gpu 0 --batch_size 4 --max_demos 50\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"705681\", \"log_path\": \"~/runs/vla-ssd/plan_010_extract_untrained.log\", \"submitted_at\": \"2026-05-16T05:18:42.203Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial/\", \"data_count\": 500, \"model_name\": \"openvla-7b-untrained (random LLM + preserved SigLIP)\", \"seed\": 42, \"wall_clock_seconds\": 11704.6, \"gpu_hours\": 3.25}}, \"plan_010_libero_spatial\": {\"status\": \"DONE\", \"spec\": {\"command\": \"extract_features.py × 2 (trained cuda:0 + untrained cuda:1)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial/\", \"data_count\": \"10 tasks × 50 demos = 500 demos\", \"model_name\": \"OpenVLA-7B trained (LIBERO-Goal fine-tuned) + untrained (random LLM)\", \"seed\": \"N/A (feature extraction)\", \"checkpoint_path\": \"features → trained_libero_spatial/ + untrained_libero_spatial/\", \"log_path\": \"~/runs/vla-ssd/plan_010_extract_trained.log + plan_010_extract_untrained.log\", \"sub_experiments\": [\"plan_010_extract_trained (cuda:0, PID 705603)\", \"plan_010_extract_untrained (cuda:1, PID 705681)\"]}}, \"plan_013_branch_split\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python rsa_branch_split.py + extract_fused_backbone.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/fused_backbone_libero_goal/\", \"data_count\": \"50 demos/task × 10 tasks, 2176d patch_mean\", \"model_name\": \"Prismatic DinoSigLIP fused backbone (DINOv2 1024d + SigLIP 1152d)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_branch_split.json\", \"log_path\": \"/root/vla-ssd/scripts/rsa_branch_split.py\"}}, \"d041_method_b_rsa\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python rsa_unified_vla.py + rsa_definitive_recalc.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/ + untrained + baselines\", \"data_count\": \"50 demos/task × 10 tasks\", \"model_name\": \"OpenVLA-7B trained/untrained + DINO/CLIP/SigLIP baselines\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/unified_rsa_results.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_definitive.json\"}}, \"plan_011_fulllayer_r2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/fulllayer_action_probe.py\", \"server\": \"westd-19183\", \"gpu\": \"cuda:0,cuda:1\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4 conditions\", \"model_name\": \"MLP action probe (4096-256-7)\", \"seed\": 42, \"checkpoint_path\": \"N/A (probe experiment)\", \"log_path\": \"/root/runs/vla-ssd/fulllayer_action_probe.log\"}}, \"unified_action_probe\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/unified_action_probe.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{clip,dino,trained,siglip}/\", \"data_count\": 63728, \"model_name\": \"MLP(input→256→7)\", \"seed\": 42, \"checkpoint_path\": \"N/A (probe, no checkpoint saved)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json\"}}, \"lg_instruction_ablation\": {\"status\": \"DONE\"}, \"lg_output_head_analysis\": {\"status\": \"DONE\"}, \"plan_008_random_inst_control\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/extract_features_rand_inst.py --instruction_mode random --seed 0 --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b\", \"seed\": 0}}, \"untrained_last_preaction_probe\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/action_probe.py --features untrained --feature_key last_preaction\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b-untrained\", \"seed\": 42, \"checkpoint_path\": \"N/A (probe analysis)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/functional_validation/\"}}, \"plan_009_cka_verification\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/cka_analysis.py (CPU-only, multiple conditions)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained,siglip_only,dino}_libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b\", \"seed\": 0, \"checkpoint_path\": \"N/A (CPU analysis)\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/cka_verification/\"}}, \"p0_functional_action_probe\": {\"status\": \"DONE\"}, \"p0_bootstrap_ci_training_effect\": {\"status\": \"DONE\"}, \"p0_image_mean_rsa_verify\": {\"status\": \"DONE\"}, \"plan_003_perlayer_degradation\": {\"status\": \"DONE\"}, \"d027_siglip_only_rsa\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python /root/vla-ssd/scripts/extract_siglip_features.py + python /root/vla-ssd/rsa_siglip_only.py\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/siglip_only_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 1 layer (projector output, 4096 dim)\", \"model_name\": \"openvla/openvla-7b SigLIP+projector only (no LLM forward)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/rsa_siglip_only.json\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/\"}}, \"lg_shuffled_token_control\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_shuffled/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --shuffle_tokens\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4096 dim (token-shuffled)\", \"model_name\": \"GoalClassificationProbe MLP (4096→256→10), trained VLA features with shuffled tokens\", \"seed\": 42, \"checkpoint_source\": \"lg_extract_trained\", \"note\": \"Control: uses bare task name prompt (NOT formatted prompt). Results not directly comparable to main pipeline. Worker: worker_ssh_shuffled-tokens-control\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_libero_goal_shuffled/goal_classification/\", \"log_path\": \"~/runs/vla-ssd/lg_shuffled_token_control.log\"}}, \"lg_dino_extract\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/extract_dinov2.py --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --model_path /root/autodl-tmp/vla-ssd/checkpoints/dinov2-large --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/dinov2-large)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/\", \"log_path\": \"~/runs/vla-ssd/lg_dino_extract.log\"}}, \"mvp2_action_probe\": {\"status\": \"DONE\", \"spec\": {\"command\": \"N/A - parent experiment, superseded by LIBERO-Goal pivot (D015)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\"}}, \"lg_extract_untrained_r2\": {\"status\": \"DONE\", \"spec\": {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from untrained OpenVLA. Fixed local_files_only=True. Continues from 2/10 tasks (skip existing).\", \"parent\": \"lg_extract_untrained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos (8 remaining after skip)\", \"model_name\": \"openvla/openvla-7b-untrained (LLM random, SigLIP preserved)\", \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"note\": \"Retry of lg_extract_untrained after local_files_only fix. Script uses --gpu 0 but CUDA_VISIBLE_DEVICES=1 maps to physical cuda:1.\", \"pid\": \"627335\", \"log_path\": \"~/runs/vla-ssd/lg_extract_untrained.log\"}}, \"lg_extract_trained_r2\": {\"status\": \"DONE\", \"spec\": {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from LIBERO-10 fine-tuned OpenVLA-7B. Fixed local_files_only=True. Continues from 3/10 tasks (skip existing).\", \"parent\": \"lg_extract_trained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos (8 remaining after skip)\", \"model_name\": \"openvla/openvla-7b (LIBERO-10 fine-tuned)\", \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"note\": \"Retry of lg_extract_trained after local_files_only fix. Script skips completed .h5 files.\", \"pid\": \"627256\", \"log_path\": \"~/runs/vla-ssd/lg_extract_trained.log\"}}, \"lg_extract_untrained_r1\": {\"status\": \"DONE\", \"spec\": {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from untrained OpenVLA (random LLM + preserved SigLIP). Baseline for instruction probing.\", \"parent\": \"lg_extract_untrained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b-untrained (LLM random, SigLIP preserved)\", \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"note\": \"retry of lg_extract_untrained after network failure, script uses --gpu 0 but CUDA_VISIBLE_DEVICES=1 maps to physical cuda:1\"}}, \"lg_extract_trained_r1\": {\"status\": \"DONE\", \"spec\": {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from LIBERO-10 fine-tuned OpenVLA-7B. OOD test. Fix: local_files_only=True, skip logic resumes from completed tasks.\", \"parent\": \"lg_extract_trained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b (LIBERO-10 fine-tuned)\", \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"note\": \"retry of lg_extract_trained after network failure\"}}, \"mvp2_delta_dino\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type action_delta --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2/\", \"data_count\": \"10 tasks x 50 demos, 1 layer x 1024 dim\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/dinov2-large)\", \"seed\": 42, \"checkpoint_source\": \"dinov2_baseline\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/dinov2/ + actions from libero_10\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/action_delta/\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/action_delta/\"}}, \"mvp2_delta_untrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --probe_type action_delta --features_dir .../features/untrained/ --output_dir .../results/untrained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"617923\", \"log_path\": \"~/runs/vla-ssd/mvp2_delta_untrained.log\", \"submitted_at\": \"2026-05-15T14:43:14.724Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim\", \"model_name\": \"MLP action-delta probe (4096->256->7)\", \"seed\": 42, \"checkpoint_source\": \"openvla-untrained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/untrained/ + actions from libero_10\", \"wall_clock_seconds\": 2409.9, \"gpu_hours\": 0.67}}, \"mvp2_delta_trained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --probe_type action_delta --features_dir .../features/trained/ --output_dir .../results/trained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"617841\", \"log_path\": \"~/runs/vla-ssd/mvp2_delta_trained.log\", \"submitted_at\": \"2026-05-15T14:43:13.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim\", \"model_name\": \"MLP action-delta probe (4096->256->7)\", \"seed\": 42, \"checkpoint_source\": \"openvla-trained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/trained/ + actions from libero_10\", \"wall_clock_seconds\": 2410.9, \"gpu_hours\": 0.67}}, \"mvp2_action_dino\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type action_prediction --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2/\", \"data_count\": \"10 tasks x 50 demos, 1 layer x 1024 dim\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/dinov2-large)\", \"seed\": 42, \"checkpoint_source\": \"dinov2_baseline\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/dinov2/ (10 tasks H5) + actions from libero_10\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/action_prediction/\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/dinov2/action_prediction/\"}}, \"mvp2_action_untrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --probe_type action_prediction --features_dir .../features/untrained/ --output_dir .../results/untrained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"613477\", \"log_path\": \"~/runs/vla-ssd/mvp2_action_untrained.log\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/ + /root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim features + 7-dim actions\", \"model_name\": \"MLP action probe (4096->256->7), untrained openvla features\", \"seed\": 42, \"checkpoint_source\": \"openvla-untrained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/untrained/ (10 tasks x 50 demos H5) + actions from /root/autodl-tmp/vla-ssd/data/libero/libero_10/\"}}, \"mvp2_action_trained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --probe_type action_prediction --features_dir .../features/trained/ --output_dir .../results/trained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"613335\", \"log_path\": \"~/runs/vla-ssd/mvp2_action_trained.log\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/ + /root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim features + 7-dim actions\", \"model_name\": \"MLP action probe (4096->256->7), trained on openvla-7b features\", \"seed\": 42, \"checkpoint_source\": \"openvla-trained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/trained/ (10 tasks x 50 demos H5) + actions from /root/autodl-tmp/vla-ssd/data/libero/libero_10/\"}}, \"mvp_controlb_untrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --shuffle-labels --untrained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"608886\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\", \"submitted_at\": \"2026-05-15T13:49:54.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/\", \"data_count\": 0, \"model_name\": \"openvla-untrained\", \"seed\": 42, \"wall_clock_seconds\": 1377.0, \"gpu_hours\": 0.38, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/untrained_label_perm/\"}}, \"mvp_controlb_trained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python scripts/train_probes.py --shuffle-labels --trained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"608744\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\", \"submitted_at\": \"2026-05-15T13:49:53.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/\", \"data_count\": 0, \"model_name\": \"openvla-trained\", \"seed\": 42, \"wall_clock_seconds\": 1377.9, \"gpu_hours\": 0.38, \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/results/trained_label_perm/\"}}, \"mvp_001\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"model_name\": \"openvla/openvla-7b\", \"model_version\": \"HuggingFace main\", \"seed\": 42, \"gpu\": \"2xRTX PRO 6000\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/\", \"log_path\": \"~/runs/vla-ssd/openvla-trained-extract.log\", \"feature_path\": \"/root/vla-ssd/features/ (symlink to data disk)\", \"controls\": [\"Control A: timestep fraction oracle\", \"Control B: cross-trajectory shuffle\", \"Control C: untrained model baseline\", \"Control D: DINO-V2 ViT-L/14\"], \"pass_criteria\": \"best_layer rho>0.3 AND delta_rho(trained-untrained)>0.1 AND (VLA>=DINO-V2 OR subtask_AUC>0.7)\", \"command\": \"python scripts/extract_features.py (trained cuda:0 + untrained cuda:1)\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps = ~125K frames\", \"phase\": \"Phase 2 feature extraction\", \"tmux_sessions\": [\"openvla-trained-extract\", \"openvla-untrained-extract\"]}}, \"mvp_probe_untrained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained/ --probe_type temporal_distance --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"606129\", \"log_path\": \"~/runs/vla-ssd/mvp_probe_untrained.log\", \"submitted_at\": \"2026-05-15T13:24:31.801Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim\", \"model_name\": \"MLP probe (1 hidden layer, Adam + early stopping)\", \"seed\": 42, \"checkpoint_source\": \"openvla-untrained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/untrained/ (10 tasks x 50 demos H5)\", \"wall_clock_seconds\": 1638.6, \"gpu_hours\": 0.46}}, \"mvp_probe_trained\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained/ --probe_type temporal_distance --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"606050\", \"log_path\": \"~/runs/vla-ssd/mvp_probe_trained.log\", \"submitted_at\": \"2026-05-15T13:24:30.997Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": \"10 tasks x 50 demos, 33 layers x 4096 dim\", \"model_name\": \"MLP probe (1 hidden layer, Adam + early stopping)\", \"seed\": 42, \"checkpoint_source\": \"openvla-trained-extract\", \"eval_data\": \"/root/autodl-tmp/vla-ssd/features/trained/ (10 tasks x 50 demos H5)\", \"wall_clock_seconds\": 1634.3, \"gpu_hours\": 0.45}}}, \"count\": 102, \"total\": 102, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3176}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T15:05:37.675Z_

<details><summary>↩ Tool result · `toolu_01B6h8h8hAs4MnXVjLvLLeUC`</summary>

```text
artifacts/dream_reports/dream_20260515T222933/best/experiment_data.json
artifacts/dream_reports/dream_20260515T222933/median/experiment_data.json
artifacts/dream_reports/dream_20260515T222933/worst/experiment_data.json
artifacts/_project/data/bootstrap_training_effect.json
artifacts/_project/data/action_delta_probe_projector.json
artifacts/_project/data/dino_action_probe.json
artifacts/_project/data/untrained_last_preaction_probe.json
artifacts/untrained_last_preaction_probe.json
artifacts/dream_reports/dream_20260516T011810/best/experiment_data.json
artifacts/dream_reports/dream_20260516T011810/median/experiment_data.json
artifacts/dream_reports/dream_20260516T011810/worst/experiment_data.json
artifacts/_project/report/rsa_method_audit.json
artifacts/_project/data/branch_split_rsa_results.json
artifacts/action_metrics_extended/data/action_metrics_extended.json
artifacts/attention_decomposition/data/attention_decomposition.json
artifacts/attention_decomposition/data/per_task_r2_distribution.json
artifacts/task_routing_loo_sensitivity/data/task_routing_loo_sensitivity.json
artifacts/libero_finetuned_probe_profile.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "d39e793f-8ae2-4ea4-b3b5-6a81236f623d",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260515T222933/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T222933/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T222933/worst/experiment_data.json",
      "artifacts/_project/data/bootstrap_training_effect.json",
      "artifacts/_project/data/action_delta_probe_projector.json",
      "artifacts/_project/data/dino_action_probe.json",
      "artifacts/_project/data/untrained_last_preaction_probe.json",
      "artifacts/untrained_last_preaction_probe.json",
      "artifacts/dream_reports/dream_20260516T011810/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T011810/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T011810/worst/experiment_data.json",
      "artifacts/_project/report/rsa_method_audit.json",
      "artifacts/_project/data/branch_split_rsa_results.json",
      "artifacts/action_metrics_extended/data/action_metrics_extended.json",
      "artifacts/attention_decomposition/data/attention_decomposition.json",
      "artifacts/attention_decomposition/data/per_task_r2_distribution.json",
      "artifacts/task_routing_loo_sensitivity/data/task_routing_loo_sensitivity.json",
      "artifacts/libero_finetuned_probe_profile.json"
    ],
    "durationMs": 14,
    "numFiles": 18,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have a clear picture of what's in the main text. Let me assess what's missing from the appendix.

Key findings from main text coverage:
- **Model**: OpenVLA-7B, checkpoint from Open X-Embodiment. But exact HuggingFace path not mentioned.
- **Dataset**: LIBERO-Goal, 10 tasks × 50 demos, N=63,228 observations
- **Hyperparameters**: MLP probes (256 hidden, Adam, lr=1e-3, batch 256, epochs 50, early stopping patience 5)


- **Metrics**: RSA (Spearman ρ, cosine rep distances, Euclidean action distances, 10,000 bootstrap), Probe R² (per-task macro-averaged)
- **Hardware**: NOT mentioned anywhere

Now checking the appendix sections. The CKA analysis method describes the linear CKA approach and metric definition, but it's missing the specific model, dataset, and computational details like which kernel implementation was used.

The metric sensitivity section comparing RSA versus CKA presents results but relies on implicit references to the main text setup—it could be clearer about which models and datasets are being compared.

Moving into the branch-split detailed analysis... Looking at the per-layer action decoding results, I can see they specify the dataset size and mention averaging across seeds, but the model checkpoints and hardware details are still missing. The random-subset ablation section starts to describe the methodology but gets cut off mid-sentence about the number of subsets used.

Moving through the action trajectory analysis, I'm noting that while the metrics are well-defined with Cohen's d, KL divergence, and statistical tests, the dataset composition varies across experiments and the bootstrap resampling approach needs clarification. The pretrained LLM section begins to reference a model but appears incomplete. Looking at the reproducibility checklist for the remaining experiments, most are missing model and dataset specifications. The functional probe comparison and training effect sections just reference figures with R² and RSA metrics defined. The cross-benchmark validation on LIBERO-Spatial is starting to be documented but appears incomplete. Looking at the robustness checks for demonstration subsample sensitivity and the training effects section, those are straightforward metric definitions. Moving into the instruction routing probes, I'm seeing several validation approaches—dense layer classification, leave-one-out cross-validation, and a QA probe that's missing some architectural details about the classifier itself. The probe profiles are just visualizations, and there's a four-condition probe with clear metrics, though the attention pattern analysis seems to be cut off.

Continuing through the attention decomposition and per-dimension error metrics, those are well-defined. The per-task R² analysis includes partial hyperparameter documentation, and the task complexity section uses Mann-Whitney U testing with leave-one-out validation. I'm now looking at the specificity control section to see what that entails.

The real problem I'm seeing is that the appendix subsections don't connect back to the main text setup. Most of these are just presenting results without explicitly stating the experimental conditions, which means readers have to flip back to sections 3.1 and 3.2 to understand what's actually being measured. The most useful fix would be adding a shared setup statement at the start of the appendix that covers the default configuration—OpenVLA-7B on LIBERO-Goal with 10 tasks and 50 demonstrations totaling 63,228 observations—and then noting any deviations in individual subsections. A few specific gaps stand out: the cross-benchmark section needs to specify the sample count for LIBERO-Spatial, while the per-layer action decoding section is already clear on this front.

Looking more carefully at what each subsection actually requires, I realize the distinction matters. For pure analysis work like RSA or attention profiling, I don't need training hyperparameters, but I do need the extraction and computation details spelled out. For probe experiments, the critical pieces are the probe architecture itself (like PCA256 + LogReg), the training procedure (LOOCV folds), and which token type serves as input. The QA probe section is missing those architecture specifics, and the probe architecture sensitivity subsection could be clearer about the linear probe setup. The cross-instruction classification needs to explicitly state the PCA256 + LogReg combination.

The most glaring omissions across the entire appendix are the lack of a shared setup paragraph that references the main text, no mention of the model checkpoint source from HuggingFace, no hardware specifications anywhere, and the cross-benchmark section leaving out the LIBERO-Spatial sample count.

I should start by adding a brief shared setup section at the top that points readers to relevant parts of the main text, then systematically fill in the specific gaps for each subsection. Before I do that, let me verify what I can find about the hardware and model path—the model is OpenVLA-7B, so the HuggingFace identifier is probably `openvla/openvla-7b`, and given this is analysis rather than training, it's likely running on a single GPU.

Now I need to check the registry for hardware specifications and also look up the LIBERO-Spatial sample count to complete the missing details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "52e472ff-be37-4888-b30c-07f7a5a37498",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjWBRYbfmoCDiFM92e4HDu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3931,
      "cache_read_input_tokens": 42184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3931
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

_source line 27_

Let me check the registry for hardware details and LIBERO-Spatial sample counts, and also look for a shared setup reference in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "1621d5e4-3090-4408-8a8e-5ecf3a0952c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjWBRYbfmoCDiFM92e4HDu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3931,
      "cache_read_input_tokens": 42184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3931
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01RTjQ3jBhtCQg4VeaBrPKLg`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nentries = json.loads(data['result'])\nfor e in entries:\n    spec = e.get('spec', {})\n    if spec:\n        hw = spec.get('hardware', spec.get('gpu', ''))\n        ds = spec.get('dataset', spec.get('data', ''))\n        model = spec.get('model', '')\n        if hw or 'spatial' in str(ds).lower() or 'spatial' in e.get('title','').lower():\n            print(f\\\"ID: {e['id']}, Title: {e['title']}\\\")\n            print(f\\\"  Hardware: {hw}\\\")\n            print(f\\\"  Dataset: {ds}\\\")\n            print(f\\\"  Model: {model}\\\")\n            print(f\\\"  Full spec keys: {list(spec.keys())}\\\")\n            print()\n\" 2>/dev/null | head -80",
  "description": "Extract hardware and spatial dataset info from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "e6d6baf1-d615-4b8f-b534-1952a3e14f44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjWBRYbfmoCDiFM92e4HDu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3931,
      "cache_read_input_tokens": 42184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3931
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

_source line 29 · 2026-05-19T15:06:32.883Z_

<details><summary>↩ Tool result · `toolu_01RTjQ3jBhtCQg4VeaBrPKLg`</summary>

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
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "981c07aa-144c-49a4-8be7-92dd29408857",
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

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Grep · `toolu_01HGVMdACRrzDHQiKHFp43XT`</summary>

```json
{
  "pattern": "hardware|GPU|gpu|A100|V100|H100|RTX",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "3c213401-4a67-4b11-82d2-41d81129aaba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjWBRYbfmoCDiFM92e4HDu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3931,
      "cache_read_input_tokens": 42184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3931
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

_source line 31 · 2026-05-19T15:06:33.938Z_

<details><summary>↩ Tool result · `toolu_01HGVMdACRrzDHQiKHFp43XT`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "52c14df1-4632-4d5b-b89f-a2e30f8124db",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Grep · `toolu_01UUY5WKJjHBse5jRXHJVb74`</summary>

```json
{
  "pattern": "sec:setup|sec:model_data|sec:repr_extraction",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "7696ecd9-7668-4ed1-9045-1a4af01971aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjWBRYbfmoCDiFM92e4HDu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3931,
      "cache_read_input_tokens": 42184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3931
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

_source line 33 · 2026-05-19T15:06:34.726Z_

<details><summary>↩ Tool result · `toolu_01UUY5WKJjHBse5jRXHJVb74`</summary>

```text
5:\label{sec:setup}
8:Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9:Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
75:In the original extraction pipeline (\S\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\Delta \approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\ref{tab:per_task_r2}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "d38db2ab-1345-45b5-8fcc-c78f548c6dc9",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "5:\\label{sec:setup}\n8:Representations are extracted from six sources spanning the VLA pipeline (\\S\\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\\_mean and readout tokens at each of 32 layers, DINOv2~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}), CLIP~\\cite{radford2021_clip} (\\texttt{patch\\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).\n9:Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\\S\\ref{sec:model_data}).\n75:In the original extraction pipeline (\\S\\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\\Delta \\approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\\ref{tab:per_task_r2}).",
    "numLines": 4
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
No hardware info in any .tex file. Let me check the registry more carefully for hardware/GPU info, and also check for LIBERO-Spatial sample counts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "bf200271-901a-4524-a94e-036288995b2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cehdPsnhGpnfYZmeVk77i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 46115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01KjDYg6wbhrpiqPjsyGLemJ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nentries = json.loads(data['result'])\n# Find any spec with hardware/gpu info\nfor e in entries:\n    spec = e.get('spec', {})\n    spec_str = json.dumps(spec).lower()\n    if 'gpu' in spec_str or 'hardware' in spec_str or 'a100' in spec_str or 'cuda' in spec_str:\n        print(f\\\"ID: {e['id']}, Title: {e['title']}\\\")\n        print(f\\\"  Spec: {json.dumps(spec, indent=2)[:500]}\\\")\n        print()\n# Also find spatial experiments\nfor e in entries:\n    if 'spatial' in e.get('title','').lower() or 'spatial' in json.dumps(e.get('spec',{})).lower():\n        print(f\\\"SPATIAL - ID: {e['id']}, Title: {e['title']}\\\")\n        spec = e.get('spec', {})\n        print(f\\\"  Spec: {json.dumps(spec, indent=2)[:500]}\\\")\n        print()\n\" 2>/dev/null",
  "description": "Search registry for hardware and spatial experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "d26e149a-a2e5-4802-9f9d-9a3b47be5e6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cehdPsnhGpnfYZmeVk77i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 46115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 36 · 2026-05-19T15:06:42.063Z_

<details><summary>↩ Tool result · reported error · `toolu_01KjDYg6wbhrpiqPjsyGLemJ`</summary>

```text
Exit code 1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "53cccdf3-8899-4ca2-8b04-ce85f7e4944e",
  "tool_use_result": "Error: Exit code 1"
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_014MigKhuCPyKmzguw2ryvK3`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nentries = json.loads(data['result'])\n# Get first entry spec to see structure\nfor e in entries[:3]:\n    print(f\\\"ID: {e['id']}, Title: {e['title']}\\\")\n    print(f\\\"  Spec keys: {list(e.get('spec', {}).keys())}\\\")\n    print(f\\\"  Spec: {json.dumps(e.get('spec',{}), indent=2)[:600]}\\\")\n    print()\n\" 2>/dev/null",
  "description": "Check registry spec structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "0e42f2c7-7221-43b3-990a-1d824c8c5783",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cehdPsnhGpnfYZmeVk77i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4090,
      "cache_read_input_tokens": 46115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4090
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

_source line 38 · 2026-05-19T15:06:44.240Z_

<details><summary>↩ Tool result · reported error · `toolu_014MigKhuCPyKmzguw2ryvK3`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-1/proje…) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "11042dd3-58ac-4ae0-8889-9d5be1fb53fb",
  "tool_use_result": "Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-1/proje…) errored"
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01HiyHsqynLC4LsbNtWUJtJy`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt') as f:\n    data = json.load(f)\nentries = json.loads(data['result'])\nfor e in entries[:3]:\n    print(f'ID: {e[\\\"id\\\"]}, Title: {e[\\\"title\\\"]}')\n    print(f'  Spec keys: {list(e.get(\\\"spec\\\", {}).keys())}')\n    print(f'  Spec: {json.dumps(e.get(\\\"spec\\\",{}))[:600]}')\n    print()\n# Search for gpu/hardware/spatial\nfor e in entries:\n    spec_str = json.dumps(e.get('spec',{})).lower()\n    if 'gpu' in spec_str or 'hardware' in spec_str or 'a100' in spec_str or 'spatial' in spec_str or 'spatial' in e.get('title','').lower():\n        print(f'MATCH: {e[\\\"id\\\"]}, Title: {e[\\\"title\\\"]}')\n        print(f'  Spec: {json.dumps(e.get(\\\"spec\\\",{}))[:600]}')\n        print()\n\"",
  "description": "Parse registry for hardware and spatial info"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "9dd272cd-edd0-4888-91d4-df8ec7d45a10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YaH3CQY84DQv1DnpbmuMmQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 50205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 903
      },
      "output_tokens": 70,
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

_source line 40 · 2026-05-19T15:06:51.049Z_

<details><summary>↩ Tool result · reported error · `toolu_01HiyHsqynLC4LsbNtWUJtJy`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    for e in entries[:3]:
             ~~~~~~~^^^^
KeyError: slice(None, 3, None)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "7bf75f04-342c-4adc-bfd2-5df90a91c476",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 6, in &lt;module>\n    for e in entries[:3]:\n             ~~~~~~~^^^^\nKeyError: slice(None, 3, None)"
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_016QwqYreb5eksnKg8FkMYkm`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt') as f:\n    data = json.load(f)\nentries = json.loads(data['result'])\nprint(type(entries), type(entries) == dict)\nif isinstance(entries, dict):\n    print(list(entries.keys())[:5])\n    for k,v in list(entries.items())[:2]:\n        print(f'Key: {k}')\n        print(f'  Type: {type(v)}')\n        if isinstance(v, dict):\n            print(f'  Keys: {list(v.keys())}')\n            spec = v.get('spec', {})\n            print(f'  Spec: {json.dumps(spec)[:400]}')\n        print()\n\"",
  "description": "Understand registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "cca1d4d9-e7f0-495d-bcce-d9728f6b9ee0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TcRLsimV1ByeHcDyzU79n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 51108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 522
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T15:06:56.345Z_

<details><summary>↩ Tool result · `toolu_016QwqYreb5eksnKg8FkMYkm`</summary>

```text
&lt;class 'dict'> True
['success', 'data', 'error', 'metadata']
Key: success
  Type: &lt;class 'bool'>

Key: data
  Type: &lt;class 'dict'>
  Keys: ['experiments', 'count', 'total', 'baseline']
  Spec: {}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "791801ef-4ac1-40de-8c58-c9dad82e1235",
  "tool_use_result": {
    "stdout": "&lt;class 'dict'> True\n['success', 'data', 'error', 'metadata']\nKey: success\n  Type: &lt;class 'bool'>\n\nKey: data\n  Type: &lt;class 'dict'>\n  Keys: ['experiments', 'count', 'total', 'baseline']\n  Spec: {}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01TxdEP4QqTHNbc3hZhf3e9m`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\n# Print all titles and look for spatial / hardware\nfor e in exps:\n    title = e.get('title','')\n    spec = e.get('spec',{})\n    spec_str = json.dumps(spec).lower()\n    if 'spatial' in title.lower() or 'spatial' in spec_str:\n        print(f'SPATIAL: {e[\\\"id\\\"]} - {title}')\n        print(f'  Spec: {json.dumps(spec)[:600]}')\n        print()\n    if 'gpu' in spec_str or 'hardware' in spec_str or 'a100' in spec_str:\n        print(f'HARDWARE: {e[\\\"id\\\"]} - {title}')\n        print(f'  Spec: {json.dumps(spec)[:400]}')\n        print()\n# Also print one representative spec\nfor e in exps[:1]:\n    print(f'Example: {e[\\\"id\\\"]} - {e[\\\"title\\\"]}')\n    print(json.dumps(e.get('spec',{}), indent=2)[:800])\n\"",
  "description": "Search registry experiments for spatial/hardware"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "cfb809e6-8659-46a1-bf02-55ea3f317cf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AoMvdMoc1Vpt4pMAktnXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 51108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 953
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T15:07:03.968Z_

<details><summary>↩ Tool result · reported error · `toolu_01TxdEP4QqTHNbc3hZhf3e9m`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 10, in &lt;module>
    title = e.get('title','')
            ^^^^^
AttributeError: 'str' object has no attribute 'get'
Total experiments: 102
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "5e90bc27-4bff-472f-b85e-ed4878c06350",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 10, in &lt;module>\n    title = e.get('title','')\n            ^^^^^\nAttributeError: 'str' object has no attribute 'get'\nTotal experiments: 102"
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01Lo85dgD5e9z31kxDE7fA8R`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\n# Check structure\nfor k in list(exps.keys())[:3] if isinstance(exps, dict) else []:\n    v = exps[k]\n    print(f'{k}: {type(v)}')\n    if isinstance(v, dict):\n        print(f'  keys: {list(v.keys())[:10]}')\n    break\nif isinstance(exps, list):\n    print(f'first elem type: {type(exps[0])}')\n    if isinstance(exps[0], str):\n        print(f'first: {exps[0][:200]}')\n\"",
  "description": "Debug registry structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "e02afcdc-7cd8-41ab-84ed-297342b6f8bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3nSW9Vk5faN9oA7hZsbdY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 578,
      "cache_read_input_tokens": 52061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 578
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

_source line 46 · 2026-05-19T15:07:09.768Z_

<details><summary>↩ Tool result · `toolu_01Lo85dgD5e9z31kxDE7fA8R`</summary>

```text
finetuned_probe_profile: &lt;class 'dict'>
  keys: ['status', 'spec']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "70bd7580-c18d-4ba7-9d06-9d4976a3ef63",
  "tool_use_result": {
    "stdout": "finetuned_probe_profile: &lt;class 'dict'>\n  keys: ['status', 'spec']",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_014xnJyHzwdyVUu7JfMuTnMR`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\n# It's a dict with experiment IDs as keys\nfor eid, edata in exps.items():\n    spec = edata.get('spec', {})\n    spec_str = json.dumps(spec).lower()\n    title = edata.get('title', eid)\n    if 'spatial' in eid.lower() or 'spatial' in spec_str:\n        print(f'SPATIAL: {eid}')\n        print(f'  Spec: {json.dumps(spec, indent=2)[:600]}')\n        print()\n    if 'gpu' in spec_str or 'hardware' in spec_str or 'a100' in spec_str:\n        print(f'HARDWARE: {eid}')\n        print(f'  Spec: {json.dumps(spec)[:400]}')\n        print()\n\n# Print one representative spec\nfor eid, edata in list(exps.items())[:1]:\n    print(f'Example: {eid}')\n    print(json.dumps(edata, indent=2)[:800])\nPYEOF",
  "description": "Parse registry for spatial/hardware experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "dce1f76d-4476-41b7-a5dc-038b236f991f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MQSjfw6Bu1enyEnW9puZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 390,
      "cache_read_input_tokens": 52639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 390
      },
      "output_tokens": 53,
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

_source line 48 · 2026-05-19T15:07:16.462Z_

<details><summary>↩ Tool result · `toolu_014xnJyHzwdyVUu7JfMuTnMR`</summary>

```text
HARDWARE: action_trajectory_control
  Spec: {"command": "bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_control.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_control.log\"", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "47936", "log_path": "~/runs/vla-ssd/action_trajectory_control.log", "submitted_at": "2026-05-18T11

HARDWARE: behavioral_pilot_w4
  Spec: {"command": "bash -c \"source /root/miniconda3/bin/activate base && MUJOCO_GL=egl HDF5_USE_FILE_LOCKING=FALSE PYTHONUNBUFFERED=1 python /root/vla-ssd/scripts/behavioral_pilot.py\"", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "24738", "log_path": "~/runs/vla-ssd/behavioral_pilot_w4.log", "submitted_at": "2026-05-18T10:23:14.928Z", "submitted_via": "submit_training_job", "backend": "tmux", "

HARDWARE: fulllayer_action_probe
  Spec: {"command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/vla-ssd/scripts/fulllayer_action_probe.py\"", "server": "westd-19183", "gpu": ["cuda:0", "cuda:1"], "pid": "700649", "log_path": "~/runs/vla-ssd/fulllayer_action_probe.log", "submitted_at": "2026-05-16T03:50:36.686Z", "submitted_via": "submit_training_job", "backend": "tmux", "account": "ro

HARDWARE: l1_head_ablation_control8
  Spec: {"command": "CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_control8.py --demos_per_task 50 --readout_layers 1 8 13 --output /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos_control8.json", "server": "westd-19183", "gpu": ["cuda:1"], "pid": "905194", "log_path": "~/runs/vla-ssd/l1_head_ablation_control8.log", "submitted_a

HARDWARE: l1_head_ablation_50demos
  Spec: {"command": "CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "905824", "log_path": "~/runs/vla-ssd/l1_head_ablation_50demos.log", "submitted_at": "2026-05-17T18:36:35.597Z", "submitted_via": "submit_training_job", "backend": "tmux", "account": "root"}

HARDWARE: llama2base_action_probe
  Spec: {"command": "bash -c \"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && CUDA_VISIBLE_DEVICES=1 python scripts/llama2base_action_probe.py\"", "server": "westd-19183", "gpu": "cuda:1", "pid": "913312", "log_path": "/root/autodl-tmp/vla-ssd/results/llama2base_action_probe/three_condition_comparison.json", "submitted_at": "2026-05-17T20:55:56.743Z", "submitted_via": "submit_training_jo

HARDWARE: ablation_50demos_main
  Spec: {"command": "CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py --demos_per_task 50 --readout_layers 1 8 13", "server": "westd-19183", "gpu": "cuda:0", "data_path": "/root/autodl-tmp/vla-ssd/data/libero_goal/", "data_count": "50 demos/task x 10 tasks x 3 conditions", "model_name": "openvla-7b (trained)", "seed": 42, "checkpoint_path": "

HARDWARE: ablation_p2_demo_sensitivity
  Spec: {"command": "subsample 25 from 50 demos, reuse existing extracted features", "server": "westd-19183", "gpu": ["cuda:1"], "pid": "720669", "log_path": "/root/autodl-tmp/vla-ssd/results/demo_sensitivity_25/results.json", "submitted_at": "2026-05-16T10:17:17.128Z", "submitted_via": "submit_training_job", "backend": "tmux", "account": "root", "data_path": "/root/autodl-tmp/vla-ssd/results/demo_sensiti

HARDWARE: ablation_50demos_control8
  Spec: {"command": "CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_control8.py --demos_per_task 50 --readout_layers 1 8 13", "server": "westd-19183", "gpu": "cuda:1", "data_path": "/root/autodl-tmp/vla-ssd/data/libero_goal/", "data_count": "50 demos/task x 10 tasks x 1 condition", "model_name": "openvla-7b (trained)", "seed": 42, "checkpoint_path": "

HARDWARE: l1_head_ablation
  Spec: {"command": "CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe.py --readout_layers 1 8 13 --demos_per_task 5 2>&1 | tee /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_log.txt", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "896931", "log_path": "~/runs/vla-ssd/l1_head_ablation.log", "submitted_at": "2026-05-17T14:49:06.028Z",

SPATIAL: cross_inst_spatial_trained
  Spec: {}

SPATIAL: plan010_rsa_spatial
  Spec: {
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/rsa_libero_spatial.py > /root/autodl-tmp/vla-ssd/logs/rsa_spatial.log 2>&1\"",
  "server": "westd-19183",
  "gpu": [
    "cuda:0"
  ],
  "pid": "708431",
  "log_path": "~/runs/vla-ssd/plan010_rsa_spatial.log",
  "submitted_at": "2026-05-16T06:25:55.106Z",
  "submitted_via": "submit_training_job",
  "backend": "tmux",
  "account": "root",
  "wall_clock_seconds": 92663.1,
  "gpu_hours": 25.74
}

HARDWARE: plan010_rsa_spatial
  Spec: {"command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/rsa_libero_spatial.py > /root/autodl-tmp/vla-ssd/logs/rsa_spatial.log 2>&1\"", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "708431", "log_path": "~/runs/vla-ssd/plan010_rsa_spatial.log", "submitted_at": "2026-05-16T06:25:55.106Z", "submitted_via": "submit_traini

SPATIAL: plan010_action_probe_spatial
  Spec: {
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/action_probe_libero_spatial.py > /root/autodl-tmp/vla-ssd/logs/action_probe_spatial.log 2>&1\"",
  "server": "westd-19183",
  "gpu": [
    "cuda:0",
    "cuda:1"
  ],
  "pid": "708576",
  "log_path": "~/runs/vla-ssd/plan010_action_probe_spatial.log",
  "submitted_at": "2026-05-16T06:25:57.400Z",
  "submitted_via": "submit_training_job",
  "backend": "tmux",
  "account": "root",
  "wall_clock_seconds": 92659.9,
  "gpu_hours": 51.48
}

HARDWARE: plan010_action_probe_spatial
  Spec: {"command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/action_probe_libero_spatial.py > /root/autodl-tmp/vla-ssd/logs/action_probe_spatial.log 2>&1\"", "server": "westd-19183", "gpu": ["cuda:0", "cuda:1"], "pid": "708576", "log_path": "~/runs/vla-ssd/plan010_action_probe_spatial.log", "submitted_at": "2026-05-16T06:25:57.4

HARDWARE: ablation_p1_seed_robustness
  Spec: {"command": "python /root/vla-ssd/scripts/ablations/probe_seed_robustness.py --gpu 0", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "718019", "log_path": "~/runs/vla-ssd/ablation_p1_seed_robustness.log", "submitted_at": "2026-05-16T09:19:20.361Z", "submitted_via": "submit_training_job", "backend": "tmux", "account": "root", "data_path": "/root/autodl-tmp/vla-ssd/features/trained/", "data_cou

HARDWARE: ablation_p2_demo_sensitivity_v2
  Spec: {"command": "python scripts/ablations/demo_sensitivity.py --gpu 0", "server": "westd-19183", "gpu": ["cuda:1"], "pid": "722187", "log_path": "~/runs/vla-ssd/ablation_p2_demo_sensitivity_v2.log", "submitted_at": "2026-05-16T10:34:16.487Z", "submitted_via": "submit_training_job", "backend": "tmux", "account": "root", "data_path": "/root/autodl-tmp/vla-ssd/features/trained/", "data_count": 500, "mode

HARDWARE: d021_instruction_ablation
  Spec: {"command": "python scripts/extract_features_no_instruction.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal_no_inst/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50 && python rsa_analysis.py (no-inst features)", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/features/untrained_libero_goal

HARDWARE: lg_gc_trained_frame0
  Spec: {"command": "python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_frame0/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_frames 1", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/features/trained_libero_goal/

HARDWARE: lg_gc_dino
  Spec: {"command": "python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "635723", "log_path": "~/runs/vla-ssd/lg_gc_dino.log", "submitted_

HARDWARE: lg_gc_untrained
  Spec: {"command": "python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained_libero_goal/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/", "data_count":

HARDWARE: lg_gc_trained
  Spec: {"command": "python scripts/train_probes.py --features_dir .../trained_libero_goal/ --output_dir .../results/trained_libero_goal/ --probe_type goal_classification --data_dir .../libero_goal/ --gpu 0", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/features/trained_libero_goal/", "data_count": "10 tasks x 50 demos x 33 layers", "model_name": "GoalClassificationProbe MLP (4096\u2192

HARDWARE: cross_inst_extract_untrained
  Spec: {"command": "source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/instruction_conditional_extract.py --condition untrained --gpu 1", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/features/", "data_count": "10 tasks \u00d7 50 frames \u00d7 10 instructions", "model_name": "openvla-7b (untrained)", "seed": 42, "output_path": "/root/autodl-tmp/vla-ssd/results/cross_in

HARDWARE: cross_inst_extract_trained
  Spec: {"command": "source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/instruction_conditional_extract.py --condition trained --gpu 0", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/features/", "data_count": "10 tasks \u00d7 50 frames \u00d7 10 instructions", "model_name": "openvla-7b (trained)", "seed": 42, "output_path": "/root/autodl-tmp/vla-ssd/results/cross_instru

HARDWARE: openvla-untrained-extract
  Spec: {"command": "python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir features/untrained/ --gpu 0 --max_demos 50 (retry: reextracted LIVING_ROOM_SCENE6 + STUDY_SCENE1)", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_10/", "data_count": "10 tasks x 50 demos x ~250 timesteps", "model_name": "openvla/openvla-7b-untrained (LLM 6.74B random 

HARDWARE: openvla-trained-extract
  Spec: {"command": "python scripts/extract_features.py --model_path openvla-7b --output_dir features/trained/ --gpu 0 --max_demos 50", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "27091", "log_path": "~/runs/vla-ssd/openvla-trained-extract.log", "submitted_at": "2026-05-15T10:01:11.065Z", "submitted_via": "submit_training_job", "backend": "tmux", "account": "root", "data_path": "/root/autodl-tmp/v

HARDWARE: lg_extract_untrained
  Spec: {"command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\"", "server": "westd-19183", "data_path": "/root/autodl-tmp/v

HARDWARE: lg_extract_trained
  Spec: {"command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\"", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/data/

HARDWARE: dinov2_baseline
  Spec: {"command": "python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type temporal_distance --gpu 0", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_10/", "data_count": "10 tasks x 50 demos x ~250 timesteps = 138,090 frames", "model_name": "DINO-V2 ViT-L/14 (facebook/di

HARDWARE: qa_probe_classification
  Spec: {"command": "source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/qa_probe_classification.py --condition all", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "744973", "log_path": "~/runs/vla-ssd/qa_probe_classification.log", "submitted_at": "2026-05-16T22:02:46.068Z", "submitted_via": "submit_training_job", "backend": "tmux", "account": "root", "data_path": "/root/autodl-tmp/v

SPATIAL: plan_010_extract_trained
  Spec: {
  "command": "python scripts/extract_features.py --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_spatial/ --mode trained --gpu 0 --batch_size 4 --max_demos 50",
  "server": "westd-19183",
  "gpu": [
    "cuda:0"
  ],
  "pid": "705603",
  "log_path": "~/runs/vla-ssd/plan_010_extract_trained.log",
  "submitted_at": "2026-05-16T05:18:41.078Z",
  "submitted_via": "submit_training_job",
  "backend": "tmux",
  "account": "root",
  "data_path": "/root/autodl-tmp

HARDWARE: plan_010_extract_trained
  Spec: {"command": "python scripts/extract_features.py --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_spatial/ --mode trained --gpu 0 --batch_size 4 --max_demos 50", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "705603", "log_path": "~/runs/vla-ssd/plan_010_ext

SPATIAL: plan_010_extract_untrained
  Spec: {
  "command": "python scripts/extract_features.py --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_spatial/ --mode trained --gpu 0 --batch_size 4 --max_demos 50",
  "server": "westd-19183",
  "gpu": [
    "cuda:1"
  ],
  "pid": "705681",
  "log_path": "~/runs/vla-ssd/plan_010_extract_untrained.log",
  "submitted_at": "2026-05-16T05:18:42.203Z",
  "submitted_via": "submit_training_job",
  "backend": "tmux",
  "account": "root",
  "data_path": "/r

HARDWARE: plan_010_extract_untrained
  Spec: {"command": "python scripts/extract_features.py --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_spatial/ --mode trained --gpu 0 --batch_size 4 --max_demos 50", "server": "westd-19183", "gpu": ["cuda:1"], "pid": "705681", "log_path": "~/runs/vla-ssd/

SPATIAL: plan_010_libero_spatial
  Spec: {
  "command": "extract_features.py \u00d7 2 (trained cuda:0 + untrained cuda:1)",
  "server": "westd-19183",
  "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_spatial/",
  "data_count": "10 tasks \u00d7 50 demos = 500 demos",
  "model_name": "OpenVLA-7B trained (LIBERO-Goal fine-tuned) + untrained (random LLM)",
  "seed": "N/A (feature extraction)",
  "checkpoint_path": "features \u2192 trained_libero_spatial/ + untrained_libero_spatial/",
  "log_path": "~/runs/vla-ssd/plan_010_extract_trained.log + plan_010_extract_untrained.log",
  "sub_experiments": [
    "plan_010_extract_traine

HARDWARE: plan_011_fulllayer_r2
  Spec: {"command": "python /root/vla-ssd/scripts/fulllayer_action_probe.py", "server": "westd-19183", "gpu": "cuda:0,cuda:1", "data_path": "/root/autodl-tmp/vla-ssd/features/{trained,untrained}_libero_goal/", "data_count": "10 tasks x 50 demos x 33 layers x 4 conditions", "model_name": "MLP action probe (4096-256-7)", "seed": 42, "checkpoint_path": "N/A (probe experiment)", "log_path": "/root/runs/vla-ss

HARDWARE: plan_008_random_inst_control
  Spec: {"command": "python scripts/extract_features_rand_inst.py --instruction_mode random --seed 0 --gpu 0", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal", "data_count": 500, "model_name": "openvla-7b", "seed": 0}

HARDWARE: lg_shuffled_token_control
  Spec: {"command": "python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_shuffled/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --shuffle_tokens", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/features/trained_libero_g

HARDWARE: lg_dino_extract
  Spec: {"command": "python scripts/extract_dinov2.py --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --model_path /root/autodl-tmp/vla-ssd/checkpoints/dinov2-large --gpu 0", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/", "data_count": "10 tasks x 50 demos", "model_name": "DINO-V2 Vi

HARDWARE: lg_extract_untrained_r2
  Spec: {"hypothesis": "Retry: Extract LIBERO-Goal features from untrained OpenVLA. Fixed local_files_only=True. Continues from 2/10 tasks (skip existing).", "parent": "lg_extract_untrained", "server": "westd-19183", "gpu": ["cuda:1"], "account": "root", "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/", "data_count": "10 tasks x 50 demos (8 remaining after skip)", "model_name": "openvla/op

HARDWARE: lg_extract_trained_r2
  Spec: {"hypothesis": "Retry: Extract LIBERO-Goal features from LIBERO-10 fine-tuned OpenVLA-7B. Fixed local_files_only=True. Continues from 3/10 tasks (skip existing).", "parent": "lg_extract_trained", "server": "westd-19183", "gpu": ["cuda:0"], "account": "root", "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/", "data_count": "10 tasks x 50 demos (8 remaining after skip)", "model_name":

HARDWARE: lg_extract_untrained_r1
  Spec: {"hypothesis": "Retry: Extract LIBERO-Goal features from untrained OpenVLA (random LLM + preserved SigLIP). Baseline for instruction probing.", "parent": "lg_extract_untrained", "server": "westd-19183", "gpu": ["cuda:1"], "account": "root", "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/", "data_count": "10 tasks x 50 demos", "model_name": "openvla/openvla-7b-untrained (LLM random,

HARDWARE: lg_extract_trained_r1
  Spec: {"hypothesis": "Retry: Extract LIBERO-Goal features from LIBERO-10 fine-tuned OpenVLA-7B. OOD test. Fix: local_files_only=True, skip logic resumes from completed tasks.", "parent": "lg_extract_trained", "server": "westd-19183", "gpu": ["cuda:0"], "account": "root", "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/", "data_count": "10 tasks x 50 demos", "model_name": "openvla/openvla-

HARDWARE: mvp2_delta_dino
  Spec: {"command": "python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type action_delta --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ --gpu 0", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/features/dinov2/", "data_count": "10 tasks x 50 demos, 1 layer x 1024 dim", "model_nam

HARDWARE: mvp2_delta_untrained
  Spec: {"command": "python scripts/train_probes.py --probe_type action_delta --features_dir .../features/untrained/ --output_dir .../results/untrained/ --data_dir .../data/libero/libero_10/ --gpu 0", "server": "westd-19183", "gpu": ["cuda:1"], "pid": "617923", "log_path": "~/runs/vla-ssd/mvp2_delta_untrained.log", "submitted_at": "2026-05-15T14:43:14.724Z", "submitted_via": "submit_training_job", "backen

HARDWARE: mvp2_delta_trained
  Spec: {"command": "python scripts/train_probes.py --probe_type action_delta --features_dir .../features/trained/ --output_dir .../results/trained/ --data_dir .../data/libero/libero_10/ --gpu 0", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "617841", "log_path": "~/runs/vla-ssd/mvp2_delta_trained.log", "submitted_at": "2026-05-15T14:43:13.318Z", "submitted_via": "submit_training_job", "backend": "t

HARDWARE: mvp2_action_dino
  Spec: {"command": "python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type action_prediction --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ --gpu 0", "server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/features/dinov2/", "data_count": "10 tasks x 50 demos, 1 layer x 1024 dim", "mode

HARDWARE: mvp2_action_untrained
  Spec: {"command": "python scripts/train_probes.py --probe_type action_prediction --features_dir .../features/untrained/ --output_dir .../results/untrained/ --data_dir .../data/libero/libero_10/ --gpu 0", "server": "westd-19183", "gpu": ["cuda:1"], "pid": "613477", "log_path": "~/runs/vla-ssd/mvp2_action_untrained.log", "data_path": "/root/autodl-tmp/vla-ssd/features/untrained/ + /root/autodl-tmp/vla-ssd

HARDWARE: mvp2_action_trained
  Spec: {"command": "python scripts/train_probes.py --probe_type action_prediction --features_dir .../features/trained/ --output_dir .../results/trained/ --data_dir .../data/libero/libero_10/ --gpu 0", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "613335", "log_path": "~/runs/vla-ssd/mvp2_action_trained.log", "data_path": "/root/autodl-tmp/vla-ssd/features/trained/ + /root/autodl-tmp/vla-ssd/data/li

HARDWARE: mvp_controlb_untrained
  Spec: {"command": "python scripts/train_probes.py --shuffle-labels --untrained", "server": "westd-19183", "gpu": ["cuda:1"], "pid": "608886", "log_path": "~/runs/vla-ssd/mvp_controlb_untrained.log", "submitted_at": "2026-05-15T13:49:54.473Z", "submitted_via": "submit_training_job", "backend": "tmux", "account": "root", "data_path": "/root/autodl-tmp/vla-ssd/", "data_count": 0, "model_name": "openvla-unt

HARDWARE: mvp_controlb_trained
  Spec: {"command": "python scripts/train_probes.py --shuffle-labels --trained", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "608744", "log_path": "~/runs/vla-ssd/mvp_controlb_trained.log", "submitted_at": "2026-05-15T13:49:53.172Z", "submitted_via": "submit_training_job", "backend": "tmux", "account": "root", "data_path": "/root/autodl-tmp/vla-ssd/", "data_count": 0, "model_name": "openvla-trained

HARDWARE: mvp_001
  Spec: {"server": "westd-19183", "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_10/", "model_name": "openvla/openvla-7b", "model_version": "HuggingFace main", "seed": 42, "gpu": "2xRTX PRO 6000", "checkpoint_path": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/", "log_path": "~/runs/vla-ssd/openvla-trained-extract.log", "feature_path": "/root/vla-ssd/features/ (symlink to data disk)", "cont

HARDWARE: mvp_probe_untrained
  Spec: {"command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained/ --probe_type temporal_distance --gpu 0\"", "server": "westd-19183", "gpu": ["cuda:1"], "pid": "606129", "log_path": "~/runs/vla-ssd/mvp_

HARDWARE: mvp_probe_trained
  Spec: {"command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained/ --probe_type temporal_distance --gpu 0\"", "server": "westd-19183", "gpu": ["cuda:0"], "pid": "606050", "log_path": "~/runs/vla-ssd/mvp_prob

Example: finetuned_probe_profile
{
  "status": "DONE",
  "spec": {
    "command": "/root/miniconda3/envs/libero/bin/python scripts/libero_finetuned_probe_profile.py",
    "server": "westd-19183",
    "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/",
    "data_count": 500,
    "model_name": "openvla-7b-finetuned-libero-goal",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal/",
    "checkpoint_path": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal/",
    "log_path": "/root/autodl-tmp/vla-ssd/results/finetuned_probe_profile.log",
    "eval_data": "LIBERO-Goal 10 tasks x 50 demos, 10-way cross-instruction LOOCV"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "127beb59-eb2c-4ff1-b45c-2ec3e9d2d1b0",
  "tool_use_result": {
    "stdout": "HARDWARE: action_trajectory_control\n  Spec: {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl CUDA_VISIBLE_DEVICES=0 python -u scripts/action_trajectory_control.py 2>&1 | tee /root/autodl-tmp/vla-ssd/results/action_trajectory_control.log\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"47936\", \"log_path\": \"~/runs/vla-ssd/action_trajectory_control.log\", \"submitted_at\": \"2026-05-18T11\n\nHARDWARE: behavioral_pilot_w4\n  Spec: {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && MUJOCO_GL=egl HDF5_USE_FILE_LOCKING=FALSE PYTHONUNBUFFERED=1 python /root/vla-ssd/scripts/behavioral_pilot.py\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"24738\", \"log_path\": \"~/runs/vla-ssd/behavioral_pilot_w4.log\", \"submitted_at\": \"2026-05-18T10:23:14.928Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"\n\nHARDWARE: fulllayer_action_probe\n  Spec: {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/vla-ssd/scripts/fulllayer_action_probe.py\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"700649\", \"log_path\": \"~/runs/vla-ssd/fulllayer_action_probe.log\", \"submitted_at\": \"2026-05-16T03:50:36.686Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"ro\n\nHARDWARE: l1_head_ablation_control8\n  Spec: {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_control8.py --demos_per_task 50 --readout_layers 1 8 13 --output /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos_control8.json\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"905194\", \"log_path\": \"~/runs/vla-ssd/l1_head_ablation_control8.log\", \"submitted_a\n\nHARDWARE: l1_head_ablation_50demos\n  Spec: {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"905824\", \"log_path\": \"~/runs/vla-ssd/l1_head_ablation_50demos.log\", \"submitted_at\": \"2026-05-17T18:36:35.597Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}\n\nHARDWARE: llama2base_action_probe\n  Spec: {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/vla-ssd && CUDA_VISIBLE_DEVICES=1 python scripts/llama2base_action_probe.py\\\"\", \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"pid\": \"913312\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/llama2base_action_probe/three_condition_comparison.json\", \"submitted_at\": \"2026-05-17T20:55:56.743Z\", \"submitted_via\": \"submit_training_jo\n\nHARDWARE: ablation_50demos_main\n  Spec: {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py --demos_per_task 50 --readout_layers 1 8 13\", \"server\": \"westd-19183\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero_goal/\", \"data_count\": \"50 demos/task x 10 tasks x 3 conditions\", \"model_name\": \"openvla-7b (trained)\", \"seed\": 42, \"checkpoint_path\": \"\n\nHARDWARE: ablation_p2_demo_sensitivity\n  Spec: {\"command\": \"subsample 25 from 50 demos, reuse existing extracted features\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"720669\", \"log_path\": \"/root/autodl-tmp/vla-ssd/results/demo_sensitivity_25/results.json\", \"submitted_at\": \"2026-05-16T10:17:17.128Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/results/demo_sensiti\n\nHARDWARE: ablation_50demos_control8\n  Spec: {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_control8.py --demos_per_task 50 --readout_layers 1 8 13\", \"server\": \"westd-19183\", \"gpu\": \"cuda:1\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero_goal/\", \"data_count\": \"50 demos/task x 10 tasks x 1 condition\", \"model_name\": \"openvla-7b (trained)\", \"seed\": 42, \"checkpoint_path\": \"\n\nHARDWARE: l1_head_ablation\n  Spec: {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe.py --readout_layers 1 8 13 --demos_per_task 5 2>&1 | tee /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_log.txt\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"896931\", \"log_path\": \"~/runs/vla-ssd/l1_head_ablation.log\", \"submitted_at\": \"2026-05-17T14:49:06.028Z\",\n\nSPATIAL: cross_inst_spatial_trained\n  Spec: {}\n\nSPATIAL: plan010_rsa_spatial\n  Spec: {\n  \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/rsa_libero_spatial.py > /root/autodl-tmp/vla-ssd/logs/rsa_spatial.log 2>&1\\\"\",\n  \"server\": \"westd-19183\",\n  \"gpu\": [\n    \"cuda:0\"\n  ],\n  \"pid\": \"708431\",\n  \"log_path\": \"~/runs/vla-ssd/plan010_rsa_spatial.log\",\n  \"submitted_at\": \"2026-05-16T06:25:55.106Z\",\n  \"submitted_via\": \"submit_training_job\",\n  \"backend\": \"tmux\",\n  \"account\": \"root\",\n  \"wall_clock_seconds\": 92663.1,\n  \"gpu_hours\": 25.74\n}\n\nHARDWARE: plan010_rsa_spatial\n  Spec: {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/rsa_libero_spatial.py > /root/autodl-tmp/vla-ssd/logs/rsa_spatial.log 2>&1\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"708431\", \"log_path\": \"~/runs/vla-ssd/plan010_rsa_spatial.log\", \"submitted_at\": \"2026-05-16T06:25:55.106Z\", \"submitted_via\": \"submit_traini\n\nSPATIAL: plan010_action_probe_spatial\n  Spec: {\n  \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/action_probe_libero_spatial.py > /root/autodl-tmp/vla-ssd/logs/action_probe_spatial.log 2>&1\\\"\",\n  \"server\": \"westd-19183\",\n  \"gpu\": [\n    \"cuda:0\",\n    \"cuda:1\"\n  ],\n  \"pid\": \"708576\",\n  \"log_path\": \"~/runs/vla-ssd/plan010_action_probe_spatial.log\",\n  \"submitted_at\": \"2026-05-16T06:25:57.400Z\",\n  \"submitted_via\": \"submit_training_job\",\n  \"backend\": \"tmux\",\n  \"account\": \"root\",\n  \"wall_clock_seconds\": 92659.9,\n  \"gpu_hours\": 51.48\n}\n\nHARDWARE: plan010_action_probe_spatial\n  Spec: {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/action_probe_libero_spatial.py > /root/autodl-tmp/vla-ssd/logs/action_probe_spatial.log 2>&1\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\", \"cuda:1\"], \"pid\": \"708576\", \"log_path\": \"~/runs/vla-ssd/plan010_action_probe_spatial.log\", \"submitted_at\": \"2026-05-16T06:25:57.4\n\nHARDWARE: ablation_p1_seed_robustness\n  Spec: {\"command\": \"python /root/vla-ssd/scripts/ablations/probe_seed_robustness.py --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"718019\", \"log_path\": \"~/runs/vla-ssd/ablation_p1_seed_robustness.log\", \"submitted_at\": \"2026-05-16T09:19:20.361Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_cou\n\nHARDWARE: ablation_p2_demo_sensitivity_v2\n  Spec: {\"command\": \"python scripts/ablations/demo_sensitivity.py --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"722187\", \"log_path\": \"~/runs/vla-ssd/ablation_p2_demo_sensitivity_v2.log\", \"submitted_at\": \"2026-05-16T10:34:16.487Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/\", \"data_count\": 500, \"mode\n\nHARDWARE: d021_instruction_ablation\n  Spec: {\"command\": \"python scripts/extract_features_no_instruction.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal_no_inst/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50 && python rsa_analysis.py (no-inst features)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal\n\nHARDWARE: lg_gc_trained_frame0\n  Spec: {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_frame0/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_frames 1\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\n\nHARDWARE: lg_gc_dino\n  Spec: {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"635723\", \"log_path\": \"~/runs/vla-ssd/lg_gc_dino.log\", \"submitted_\n\nHARDWARE: lg_gc_untrained\n  Spec: {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained_libero_goal/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/\", \"data_count\":\n\nHARDWARE: lg_gc_trained\n  Spec: {\"command\": \"python scripts/train_probes.py --features_dir .../trained_libero_goal/ --output_dir .../results/trained_libero_goal/ --probe_type goal_classification --data_dir .../libero_goal/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers\", \"model_name\": \"GoalClassificationProbe MLP (4096\\u2192\n\nHARDWARE: cross_inst_extract_untrained\n  Spec: {\"command\": \"source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/instruction_conditional_extract.py --condition untrained --gpu 1\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/\", \"data_count\": \"10 tasks \\u00d7 50 frames \\u00d7 10 instructions\", \"model_name\": \"openvla-7b (untrained)\", \"seed\": 42, \"output_path\": \"/root/autodl-tmp/vla-ssd/results/cross_in\n\nHARDWARE: cross_inst_extract_trained\n  Spec: {\"command\": \"source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/instruction_conditional_extract.py --condition trained --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/\", \"data_count\": \"10 tasks \\u00d7 50 frames \\u00d7 10 instructions\", \"model_name\": \"openvla-7b (trained)\", \"seed\": 42, \"output_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instru\n\nHARDWARE: openvla-untrained-extract\n  Spec: {\"command\": \"python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir features/untrained/ --gpu 0 --max_demos 50 (retry: reextracted LIVING_ROOM_SCENE6 + STUDY_SCENE1)\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps\", \"model_name\": \"openvla/openvla-7b-untrained (LLM 6.74B random \n\nHARDWARE: openvla-trained-extract\n  Spec: {\"command\": \"python scripts/extract_features.py --model_path openvla-7b --output_dir features/trained/ --gpu 0 --max_demos 50\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"27091\", \"log_path\": \"~/runs/vla-ssd/openvla-trained-extract.log\", \"submitted_at\": \"2026-05-15T10:01:11.065Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/v\n\nHARDWARE: lg_extract_untrained\n  Spec: {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b-untrained --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/v\n\nHARDWARE: lg_extract_trained\n  Spec: {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/extract_features.py --model_path openvla-7b --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --max_demos 50\\\"\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/\n\nHARDWARE: dinov2_baseline\n  Spec: {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type temporal_distance --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"data_count\": \"10 tasks x 50 demos x ~250 timesteps = 138,090 frames\", \"model_name\": \"DINO-V2 ViT-L/14 (facebook/di\n\nHARDWARE: qa_probe_classification\n  Spec: {\"command\": \"source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/qa_probe_classification.py --condition all\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"744973\", \"log_path\": \"~/runs/vla-ssd/qa_probe_classification.log\", \"submitted_at\": \"2026-05-16T22:02:46.068Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/v\n\nSPATIAL: plan_010_extract_trained\n  Spec: {\n  \"command\": \"python scripts/extract_features.py --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_spatial/ --mode trained --gpu 0 --batch_size 4 --max_demos 50\",\n  \"server\": \"westd-19183\",\n  \"gpu\": [\n    \"cuda:0\"\n  ],\n  \"pid\": \"705603\",\n  \"log_path\": \"~/runs/vla-ssd/plan_010_extract_trained.log\",\n  \"submitted_at\": \"2026-05-16T05:18:41.078Z\",\n  \"submitted_via\": \"submit_training_job\",\n  \"backend\": \"tmux\",\n  \"account\": \"root\",\n  \"data_path\": \"/root/autodl-tmp\n\nHARDWARE: plan_010_extract_trained\n  Spec: {\"command\": \"python scripts/extract_features.py --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_spatial/ --mode trained --gpu 0 --batch_size 4 --max_demos 50\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"705603\", \"log_path\": \"~/runs/vla-ssd/plan_010_ext\n\nSPATIAL: plan_010_extract_untrained\n  Spec: {\n  \"command\": \"python scripts/extract_features.py --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_spatial/ --mode trained --gpu 0 --batch_size 4 --max_demos 50\",\n  \"server\": \"westd-19183\",\n  \"gpu\": [\n    \"cuda:1\"\n  ],\n  \"pid\": \"705681\",\n  \"log_path\": \"~/runs/vla-ssd/plan_010_extract_untrained.log\",\n  \"submitted_at\": \"2026-05-16T05:18:42.203Z\",\n  \"submitted_via\": \"submit_training_job\",\n  \"backend\": \"tmux\",\n  \"account\": \"root\",\n  \"data_path\": \"/r\n\nHARDWARE: plan_010_extract_untrained\n  Spec: {\"command\": \"python scripts/extract_features.py --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_spatial/ --mode trained --gpu 0 --batch_size 4 --max_demos 50\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"705681\", \"log_path\": \"~/runs/vla-ssd/\n\nSPATIAL: plan_010_libero_spatial\n  Spec: {\n  \"command\": \"extract_features.py \\u00d7 2 (trained cuda:0 + untrained cuda:1)\",\n  \"server\": \"westd-19183\",\n  \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_spatial/\",\n  \"data_count\": \"10 tasks \\u00d7 50 demos = 500 demos\",\n  \"model_name\": \"OpenVLA-7B trained (LIBERO-Goal fine-tuned) + untrained (random LLM)\",\n  \"seed\": \"N/A (feature extraction)\",\n  \"checkpoint_path\": \"features \\u2192 trained_libero_spatial/ + untrained_libero_spatial/\",\n  \"log_path\": \"~/runs/vla-ssd/plan_010_extract_trained.log + plan_010_extract_untrained.log\",\n  \"sub_experiments\": [\n    \"plan_010_extract_traine\n\nHARDWARE: plan_011_fulllayer_r2\n  Spec: {\"command\": \"python /root/vla-ssd/scripts/fulllayer_action_probe.py\", \"server\": \"westd-19183\", \"gpu\": \"cuda:0,cuda:1\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained}_libero_goal/\", \"data_count\": \"10 tasks x 50 demos x 33 layers x 4 conditions\", \"model_name\": \"MLP action probe (4096-256-7)\", \"seed\": 42, \"checkpoint_path\": \"N/A (probe experiment)\", \"log_path\": \"/root/runs/vla-ss\n\nHARDWARE: plan_008_random_inst_control\n  Spec: {\"command\": \"python scripts/extract_features_rand_inst.py --instruction_mode random --seed 0 --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b\", \"seed\": 0}\n\nHARDWARE: lg_shuffled_token_control\n  Spec: {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_libero_goal_shuffled/ --probe_type goal_classification --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --gpu 0 --shuffle_tokens\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained_libero_g\n\nHARDWARE: lg_dino_extract\n  Spec: {\"command\": \"python scripts/extract_dinov2.py --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ --output_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ --model_path /root/autodl-tmp/vla-ssd/checkpoints/dinov2-large --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"DINO-V2 Vi\n\nHARDWARE: lg_extract_untrained_r2\n  Spec: {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from untrained OpenVLA. Fixed local_files_only=True. Continues from 2/10 tasks (skip existing).\", \"parent\": \"lg_extract_untrained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos (8 remaining after skip)\", \"model_name\": \"openvla/op\n\nHARDWARE: lg_extract_trained_r2\n  Spec: {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from LIBERO-10 fine-tuned OpenVLA-7B. Fixed local_files_only=True. Continues from 3/10 tasks (skip existing).\", \"parent\": \"lg_extract_trained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos (8 remaining after skip)\", \"model_name\":\n\nHARDWARE: lg_extract_untrained_r1\n  Spec: {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from untrained OpenVLA (random LLM + preserved SigLIP). Baseline for instruction probing.\", \"parent\": \"lg_extract_untrained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-7b-untrained (LLM random,\n\nHARDWARE: lg_extract_trained_r1\n  Spec: {\"hypothesis\": \"Retry: Extract LIBERO-Goal features from LIBERO-10 fine-tuned OpenVLA-7B. OOD test. Fix: local_files_only=True, skip logic resumes from completed tasks.\", \"parent\": \"lg_extract_trained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 50 demos\", \"model_name\": \"openvla/openvla-\n\nHARDWARE: mvp2_delta_dino\n  Spec: {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type action_delta --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2/\", \"data_count\": \"10 tasks x 50 demos, 1 layer x 1024 dim\", \"model_nam\n\nHARDWARE: mvp2_delta_untrained\n  Spec: {\"command\": \"python scripts/train_probes.py --probe_type action_delta --features_dir .../features/untrained/ --output_dir .../results/untrained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"617923\", \"log_path\": \"~/runs/vla-ssd/mvp2_delta_untrained.log\", \"submitted_at\": \"2026-05-15T14:43:14.724Z\", \"submitted_via\": \"submit_training_job\", \"backen\n\nHARDWARE: mvp2_delta_trained\n  Spec: {\"command\": \"python scripts/train_probes.py --probe_type action_delta --features_dir .../features/trained/ --output_dir .../results/trained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"617841\", \"log_path\": \"~/runs/vla-ssd/mvp2_delta_trained.log\", \"submitted_at\": \"2026-05-15T14:43:13.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"t\n\nHARDWARE: mvp2_action_dino\n  Spec: {\"command\": \"python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ --probe_type action_prediction --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/dinov2/\", \"data_count\": \"10 tasks x 50 demos, 1 layer x 1024 dim\", \"mode\n\nHARDWARE: mvp2_action_untrained\n  Spec: {\"command\": \"python scripts/train_probes.py --probe_type action_prediction --features_dir .../features/untrained/ --output_dir .../results/untrained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"613477\", \"log_path\": \"~/runs/vla-ssd/mvp2_action_untrained.log\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/untrained/ + /root/autodl-tmp/vla-ssd\n\nHARDWARE: mvp2_action_trained\n  Spec: {\"command\": \"python scripts/train_probes.py --probe_type action_prediction --features_dir .../features/trained/ --output_dir .../results/trained/ --data_dir .../data/libero/libero_10/ --gpu 0\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"613335\", \"log_path\": \"~/runs/vla-ssd/mvp2_action_trained.log\", \"data_path\": \"/root/autodl-tmp/vla-ssd/features/trained/ + /root/autodl-tmp/vla-ssd/data/li\n\nHARDWARE: mvp_controlb_untrained\n  Spec: {\"command\": \"python scripts/train_probes.py --shuffle-labels --untrained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"608886\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_untrained.log\", \"submitted_at\": \"2026-05-15T13:49:54.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/\", \"data_count\": 0, \"model_name\": \"openvla-unt\n\nHARDWARE: mvp_controlb_trained\n  Spec: {\"command\": \"python scripts/train_probes.py --shuffle-labels --trained\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"608744\", \"log_path\": \"~/runs/vla-ssd/mvp_controlb_trained.log\", \"submitted_at\": \"2026-05-15T13:49:53.172Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/\", \"data_count\": 0, \"model_name\": \"openvla-trained\n\nHARDWARE: mvp_001\n  Spec: {\"server\": \"westd-19183\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_10/\", \"model_name\": \"openvla/openvla-7b\", \"model_version\": \"HuggingFace main\", \"seed\": 42, \"gpu\": \"2xRTX PRO 6000\", \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/\", \"log_path\": \"~/runs/vla-ssd/openvla-trained-extract.log\", \"feature_path\": \"/root/vla-ssd/features/ (symlink to data disk)\", \"cont\n\nHARDWARE: mvp_probe_untrained\n  Spec: {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained/ --probe_type temporal_distance --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"606129\", \"log_path\": \"~/runs/vla-ssd/mvp_\n\nHARDWARE: mvp_probe_trained\n  Spec: {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/vla-ssd && python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained/ --probe_type temporal_distance --gpu 0\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:0\"], \"pid\": \"606050\", \"log_path\": \"~/runs/vla-ssd/mvp_prob\n\nExample: finetuned_probe_profile\n{\n  \"status\": \"DONE\",\n  \"spec\": {\n    \"command\": \"/root/miniconda3/envs/libero/bin/python scripts/libero_finetuned_probe_profile.py\",\n    \"server\": \"westd-19183\",\n    \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\",\n    \"data_count\": 500,\n    \"model_name\": \"openvla-7b-finetuned-libero-goal\",\n    \"seed\": 42,\n    \"checkpoint_source\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal/\",\n    \"checkpoint_path\": \"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal/\",\n    \"log_path\": \"/root/autodl-tmp/vla-ssd/results/finetuned_probe_profile.log\",\n    \"eval_data\": \"LIBERO-Goal 10 tasks x 50 demos, 10-way cross-instruction LOOCV\"\n  }\n}",
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

_source line 49_

<details><summary>Logged reasoning block</summary>

```text
Now I have key hardware info: `"gpu": "2xRTX PRO 6000"` from the mvp_001 entry. Also the model is from HuggingFace `openvla/openvla-7b`. The LIBERO-Spatial data has `"data_count": "10 tasks × 50 demos = 500 demos"`.

Now let me also check the QA probe experiment for its architecture details.

Let me also check the `ablation_50demos_main` spec for more details about the main ablation experiment setup.

OK, I now have enough info. Let me now do the audit systematically.


I've gathered the full model lineup: the base OpenVLA-7B, an untrained variant with random LLM weights but preserved vision, the Llama-2 backbone without VLA fine-tuning, and the LIBERO-finetuned version. The dataset consists of 500 demonstrations across 10 tasks.

For the probing setup, I'm using an MLP probe with a 4096-to-256-to-7 architecture, trained with Adam at learning rate 1e-3 for up to 50 epochs with early stopping. The cross-instruction probe runs 10-way classification with leave-one-out cross-validation, and I still need to confirm the specifics for the QA probe.

Now I'm planning how to restructure the appendix—I'll add a shared setup section at the top covering the models, datasets, and hardware, then make targeted fixes to each subsection based on what's missing.

Looking at the subsections, I can group them by what they need: the analysis sections like CKA and RSA mostly just need dataset and model references, while the probe experiments require full training details.

For the probe work, I'm tracking which experiments have enough information and which are missing key details—most need either the probe architecture specified or references to the training methodology. The ablation experiments at the end also need model and dataset references to be complete.

The most efficient approach is to write a shared setup section upfront that covers the model details, experimental conditions, and dataset specs, then each subsection just needs targeted additions rather than repeating everything. I should draft that shared paragraph to include the OpenVLA-7B model reference, the three conditions, and the LIBERO-Goal dataset with task and demo counts, keeping it concise and then identify what each subsection still needs on top of that. Looking at the checklist for reproducibility requirements, I need to verify that each experimental section includes the model version, dataset details with exact sample counts, relevant hyperparameters, precise metric definitions, and hardware specs. I'm checking the QA probe architecture next since that's missing from the current documentation, and I should cross-reference the cross-instruction classification methods back to the main methodology section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "34a95399-074d-4022-9d7e-7510e9dc21f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019UhnrWtEA71tu1jgM8biL6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10393,
      "cache_read_input_tokens": 53029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10393
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

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01GzWtheRGueqMcSo25GHMro`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/c7f8ee1c-2669-4287-a396-fbc9a7afe088/tool-results/mcp-agent-ml-research-read_registry-1779203137649.txt') as f:\n    data = json.load(f)\nparsed = json.loads(data['result'])\nexps = parsed['data']['experiments']\n# Get QA probe details\nfor eid in ['qa_probe_classification']:\n    if eid in exps:\n        print(f'{eid}:')\n        print(json.dumps(exps[eid], indent=2))\n        print()\n# Also get ablation_50demos_main\nfor eid in ['ablation_50demos_main', 'plan_011_fulllayer_r2']:\n    if eid in exps:\n        print(f'{eid}:')\n        print(json.dumps(exps[eid].get('spec',{}), indent=2)[:800])\n        print()\nPYEOF",
  "description": "Get QA probe and key experiment details from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "680298c8-0fb6-4d1b-a280-f23da95d1e29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019UhnrWtEA71tu1jgM8biL6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10393,
      "cache_read_input_tokens": 53029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10393
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

_source line 51 · 2026-05-19T15:08:05.681Z_

<details><summary>↩ Tool result · `toolu_01GzWtheRGueqMcSo25GHMro`</summary>

```text
qa_probe_classification:
{
  "status": "DONE",
  "spec": {
    "command": "source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/qa_probe_classification.py --condition all",
    "server": "westd-19183",
    "gpu": [
      "cuda:0"
    ],
    "pid": "744973",
    "log_path": "~/runs/vla-ssd/qa_probe_classification.log",
    "submitted_at": "2026-05-16T22:02:46.068Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/vla-ssd/features/",
    "data_count": "10 tasks \u00d7 50 demos, 4-class progress + binary subtask",
    "model_name": "openvla-7b (trained + untrained)",
    "seed": 42,
    "wall_clock_seconds": 14729.6,
    "gpu_hours": 4.09
  }
}

ablation_50demos_main:
{
  "command": "CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py --demos_per_task 50 --readout_layers 1 8 13",
  "server": "westd-19183",
  "gpu": "cuda:0",
  "data_path": "/root/autodl-tmp/vla-ssd/data/libero_goal/",
  "data_count": "50 demos/task x 10 tasks x 3 conditions",
  "model_name": "openvla-7b (trained)",
  "seed": 42,
  "checkpoint_path": "N/A (inference-only)",
  "log_path": "/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json"
}

plan_011_fulllayer_r2:
{
  "command": "python /root/vla-ssd/scripts/fulllayer_action_probe.py",
  "server": "westd-19183",
  "gpu": "cuda:0,cuda:1",
  "data_path": "/root/autodl-tmp/vla-ssd/features/{trained,untrained}_libero_goal/",
  "data_count": "10 tasks x 50 demos x 33 layers x 4 conditions",
  "model_name": "MLP action probe (4096-256-7)",
  "seed": 42,
  "checkpoint_path": "N/A (probe experiment)",
  "log_path": "/root/runs/vla-ssd/fulllayer_action_probe.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "e9cc6867-46fc-4940-9403-8eb04e8e63ac",
  "tool_use_result": {
    "stdout": "qa_probe_classification:\n{\n  \"status\": \"DONE\",\n  \"spec\": {\n    \"command\": \"source /root/miniconda3/bin/activate && python /root/vla-ssd/scripts/qa_probe_classification.py --condition all\",\n    \"server\": \"westd-19183\",\n    \"gpu\": [\n      \"cuda:0\"\n    ],\n    \"pid\": \"744973\",\n    \"log_path\": \"~/runs/vla-ssd/qa_probe_classification.log\",\n    \"submitted_at\": \"2026-05-16T22:02:46.068Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"data_path\": \"/root/autodl-tmp/vla-ssd/features/\",\n    \"data_count\": \"10 tasks \\u00d7 50 demos, 4-class progress + binary subtask\",\n    \"model_name\": \"openvla-7b (trained + untrained)\",\n    \"seed\": 42,\n    \"wall_clock_seconds\": 14729.6,\n    \"gpu_hours\": 4.09\n  }\n}\n\nablation_50demos_main:\n{\n  \"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/l1_ablation_action_probe_50demos.py --demos_per_task 50 --readout_layers 1 8 13\",\n  \"server\": \"westd-19183\",\n  \"gpu\": \"cuda:0\",\n  \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero_goal/\",\n  \"data_count\": \"50 demos/task x 10 tasks x 3 conditions\",\n  \"model_name\": \"openvla-7b (trained)\",\n  \"seed\": 42,\n  \"checkpoint_path\": \"N/A (inference-only)\",\n  \"log_path\": \"/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json\"\n}\n\nplan_011_fulllayer_r2:\n{\n  \"command\": \"python /root/vla-ssd/scripts/fulllayer_action_probe.py\",\n  \"server\": \"westd-19183\",\n  \"gpu\": \"cuda:0,cuda:1\",\n  \"data_path\": \"/root/autodl-tmp/vla-ssd/features/{trained,untrained}_libero_goal/\",\n  \"data_count\": \"10 tasks x 50 demos x 33 layers x 4 conditions\",\n  \"model_name\": \"MLP action probe (4096-256-7)\",\n  \"seed\": 42,\n  \"checkpoint_path\": \"N/A (probe experiment)\",\n  \"log_path\": \"/root/runs/vla-ssd/fulllayer_action_probe.log\"\n}",
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

_source line 52_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the QA probe script to find the probe architecture details, and the cross-instruction probe details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "5271a5ea-04f7-441d-a3e5-04e822115768",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dsbCJmNbCrPkHiNaQifDr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2876,
      "cache_read_input_tokens": 63422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2876
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

_source line 53_

Let me check the QA probe and cross-instruction probe scripts for architecture details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "237eafe2-4362-4219-8975-9adc141395b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dsbCJmNbCrPkHiNaQifDr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2876,
      "cache_read_input_tokens": 63422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2876
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

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y6oXbfnfaERoouVhUDmvmY`</summary>

```json
{
  "command": "ssh connect.westd.seetacloud.com \"head -80 /root/vla-ssd/scripts/qa_probe_classification.py 2>/dev/null || echo 'FILE_NOT_FOUND'\" 2>/dev/null | head -80",
  "description": "Check QA probe script for architecture details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "35c91ae9-5313-4b8c-8902-a68cdb31ba0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dsbCJmNbCrPkHiNaQifDr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2876,
      "cache_read_input_tokens": 63422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2876
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

_source line 55 · 2026-05-19T15:08:11.552Z_

<details><summary>↩ Tool result · `toolu_01Y6oXbfnfaERoouVhUDmvmY`</summary>

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
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "115c8ae1-8d6e-4918-a721-482935a06f57",
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

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Grep · `toolu_019SHXtR6DQr1fcqvZwPfESq`</summary>

```json
{
  "pattern": "cross.instruction|classification|LOOCV|LogReg|logistic|PCA|probe.*arch",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "output_mode": "content",
  "-C": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "a2048526-d200-4be5-8314-dc402e247fa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dsbCJmNbCrPkHiNaQifDr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2876,
      "cache_read_input_tokens": 63422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2876
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

_source line 57 · 2026-05-19T15:08:12.093Z_

<details><summary>↩ Tool result · `toolu_019SHXtR6DQr1fcqvZwPfESq`</summary>

```text
2-\label{sec:method}
3-
4:We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5-
6-%------------------------------------------------------------------
--
29-%------------------------------------------------------------------
30-\subsection{Cross-Instruction Probes}
31:\label{sec:cross_instruction_probes}
32-
33:To test whether different token types encode instruction identity, we construct a cross-instruction dataset: each visual frame is paired with all 10 task instructions, producing 10 representation vectors per frame per layer.
34-A linear classifier (10-way) is trained to identify which instruction was present, separately for image\_mean and readout token positions.
35:We validate with leave-one-out cross-validation (LOOCV) over 10 folds, each holding out one task's instructions, to verify that results reflect generalizable instruction encoding rather than memorization.
36-
37-%------------------------------------------------------------------
--
40-
41-We analyze attention distributions at the readout token position across all 32 layers, categorizing each head as instruction-dominant ($>50\%$ attention to instruction tokens) or image-dominant, with detailed per-head decomposition at L1.
42:This complements the cross-instruction probe by revealing the \emph{mechanism} through which instruction information reaches the readout token.
43-
44-%------------------------------------------------------------------
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "3fda8f21-1d05-45aa-86f1-0e7f7949d8ca",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "2-\\label{sec:method}\n3-\n4:We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.\n5-\n6-%------------------------------------------------------------------\n--\n29-%------------------------------------------------------------------\n30-\\subsection{Cross-Instruction Probes}\n31:\\label{sec:cross_instruction_probes}\n32-\n33:To test whether different token types encode instruction identity, we construct a cross-instruction dataset: each visual frame is paired with all 10 task instructions, producing 10 representation vectors per frame per layer.\n34-A linear classifier (10-way) is trained to identify which instruction was present, separately for image\\_mean and readout token positions.\n35:We validate with leave-one-out cross-validation (LOOCV) over 10 folds, each holding out one task's instructions, to verify that results reflect generalizable instruction encoding rather than memorization.\n36-\n37-%------------------------------------------------------------------\n--\n40-\n41-We analyze attention distributions at the readout token position across all 32 layers, categorizing each head as instruction-dominant ($>50\\%$ attention to instruction tokens) or image-dominant, with detailed per-head decomposition at L1.\n42:This complements the cross-instruction probe by revealing the \\emph{mechanism} through which instruction information reaches the readout token.\n43-\n44-%------------------------------------------------------------------",
    "numLines": 21
  }
}
```

</details>

---

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Good. So from method.tex §3.3, the cross-instruction probe is described as:
- "A linear classifier (10-way) is trained to identify which instruction was present"
- "leave-one-out cross-validation (LOOCV) over 10 folds, each holding out one task's instructions"

For the QA probe, the method.tex doesn't describe it in detail. Let me check more about it in the paper.

Let me also check what the method.tex says about probes in §3.5 (functional probes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "e2afd65d-8a43-42f6-8213-11bc00b5678d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VP2wDBWjx5gLeyvfB4DcQh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 66298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 842
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

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_012QcnGEDR8E2s7avDGUe78m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "offset": 44,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "ff643ea4-8760-42bb-ae02-48a300251f3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VP2wDBWjx5gLeyvfB4DcQh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 66298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 842
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

_source line 60 · 2026-05-19T15:08:17.318Z_

<details><summary>↩ Tool result · `toolu_012QcnGEDR8E2s7avDGUe78m`</summary>

```text
44	%------------------------------------------------------------------
45	\subsection{Representational Similarity Analysis}
46	\label{sec:rsa}
47	
48	We adopt RSA~\cite{kriegeskorte2008} to quantify geometric alignment between representations and the action space.
49	For each task, we compute pairwise $N \times N$ representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, using within-task observation pairs from 50 demonstrations.
50	Alignment is measured via Spearman $\rho$ between the upper-triangular entries of the representation and action RDMs; higher $\rho$ indicates that representationally similar observations require similar actions.
51	We report mean $\rho$ across 10 tasks with 95\% confidence intervals from 10{,}000 bootstrap resamples; resampling is performed at the task level ($N=10$), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure~\cite{nili2014toolbox}.
52	
53	%------------------------------------------------------------------
54	\subsection{Functional Action Probes}
55	\label{sec:probes}
56	
57	RSA measures geometric alignment but not decodability.
58	We complement it with MLP probes~\cite{alain2017}: two-layer networks ($d_\text{in} \to 256 \to 7$) trained to predict 7-D action vectors from frozen representations (Adam, lr${}=10^{-3}$, batch 256, 50 epochs, early stopping patience 5), with demo-level train/test splits (demos 0--39 vs.\ 40--49).
59	We report per-task macro-averaged $R^2$ across 10 tasks with bootstrap paired comparisons (10{,}000 resamples).
60	
61	\paragraph{Why RSA over CKA.}
62	RSA captures relative distance structure via scale-invariant Spearman rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\ 7-D).
63	CKA~\cite{kornblith2019} measures global subspace overlap, which can remain high even when geometric structure differs.
64	We report both in Appendix~\ref{sec:cka_appendix}; the divergence between metrics (\S\ref{sec:nonmonotonic}) indicates neither alone fully characterizes representational structure.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "e1fcada4-3999-4e37-9dc5-51c1b2b2047a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
      "content": "%------------------------------------------------------------------\n\\subsection{Representational Similarity Analysis}\n\\label{sec:rsa}\n\nWe adopt RSA~\\cite{kriegeskorte2008} to quantify geometric alignment between representations and the action space.\nFor each task, we compute pairwise $N \\times N$ representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, using within-task observation pairs from 50 demonstrations.\nAlignment is measured via Spearman $\\rho$ between the upper-triangular entries of the representation and action RDMs; higher $\\rho$ indicates that representationally similar observations require similar actions.\nWe report mean $\\rho$ across 10 tasks with 95\\% confidence intervals from 10{,}000 bootstrap resamples; resampling is performed at the task level ($N=10$), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure~\\cite{nili2014toolbox}.\n\n%------------------------------------------------------------------\n\\subsection{Functional Action Probes}\n\\label{sec:probes}\n\nRSA measures geometric alignment but not decodability.\nWe complement it with MLP probes~\\cite{alain2017}: two-layer networks ($d_\\text{in} \\to 256 \\to 7$) trained to predict 7-D action vectors from frozen representations (Adam, lr${}=10^{-3}$, batch 256, 50 epochs, early stopping patience 5), with demo-level train/test splits (demos 0--39 vs.\\ 40--49).\nWe report per-task macro-averaged $R^2$ across 10 tasks with bootstrap paired comparisons (10{,}000 resamples).\n\n\\paragraph{Why RSA over CKA.}\nRSA captures relative distance structure via scale-invariant Spearman rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\\ 7-D).\nCKA~\\cite{kornblith2019} measures global subspace overlap, which can remain high even when geometric structure differs.\nWe report both in Appendix~\\ref{sec:cka_appendix}; the divergence between metrics (\\S\\ref{sec:nonmonotonic}) indicates neither alone fully characterizes representational structure.\n",
      "numLines": 22,
      "startLine": 44,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have a complete picture. Let me plan the edits:

## Summary of what's already in the main text (referenceable):

- **§3.1 (sec:setup)**: Model conditions (OpenVLA-7B, three LLM conditions), dataset (LIBERO-Goal, 10 tasks × 50 demos)
- **§3.2 (sec:model_data)**: Three conditions details, representation extraction (6 sources)  


- **§3.3 (sec:cross_instruction_probes)**: Cross-instruction probe setup with a 10-way linear classifier trained via leave-one-out cross-validation across 10 folds
- **§3.4 (sec:attention_analysis)**: Attention head categorization using a 50% threshold to identify task-relevant heads
- **§3.5 (sec:rsa)**: RSA analysis computing Spearman correlations between representational dissimilarity matrices derived from cosine and Euclidean distances, with 10,000 bootstrap samples for significance testing
- **§3.6 (sec:probes)**: MLP probe architecture with hidden dimension 256, trained using Adam optimizer at learning rate 1e-3, batch size 256 for 50 epochs with early stopping when validation performance plateaus after 5 epochs without improvement

Now I'm identifying critical missing details that need to be added to the appendix. The hardware setup (2× NVIDIA RTX PRO 6000 Ada), the specific HuggingFace checkpoint identifier, and the exact sample count for LIBERO-Spatial aren't documented anywhere in the paper. I should add a shared reproducibility statement early in the supplementary material that establishes these baseline conditions and references back to the main methodology sections. I'm reviewing the experimental setup details across different sections. The QA probe needs its own method description since it only appears in the appendix, not in the main methods section. For the per-layer action decoding and probe architecture sensitivity analyses, the existing captions and references already capture the necessary experimental parameters and probe specifications, so those sections are adequately documented.

Looking at the CKA analysis, the current description covers both linear and RDM kernel variants and explains how the dimension mismatch is handled, which provides sufficient methodological detail. The main gaps I need to address are adding a shared setup paragraph that consolidates common experimental details across subsections, clarifying the LIBERO-Spatial sample count, and providing the QA probe architecture description.

For the Llama-2 base checkpoint, I should note that it refers to the 7B backbone from OpenVLA rather than treating it as a separate model, though the three-condition comparison is already well-defined in the main text. Let me also verify the observation counts across the different experimental conditions.

Actually, I don't need the exact number for LIBERO-Spatial—saying "10 tasks × 50 demonstrations" captures what's needed. Now I'm checking the QA probe section to see how it's described in the appendix, particularly what the probe measures and how the results are presented.

Looking at the section, I notice there's a gap between what the text claims—classifying task progress as early/mid/late—and what the registry indicates, which is 4-class progress plus binary subtask classification. The appendix doesn't specify the probe architecture, how the progress labels are actually defined, or the training procedure, so I can't fully reconcile this discrepancy without checking the implementation details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "0fadd649-cd28-4dd3-a211-aa3715ea178a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsnMoGXLDErhqCq5qjLJkt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 67140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 878
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

_source line 62_

<details open><summary>🔧 Tool call — Glob · `toolu_014LisC65zvDrVhZSWpNza2Z`</summary>

```json
{
  "pattern": "**/qa_probe*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "0e35ff3a-d1e9-49cd-9973-e31d006ec740",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsnMoGXLDErhqCq5qjLJkt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 67140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 878
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

_source line 63 · 2026-05-19T15:08:59.755Z_

<details><summary>↩ Tool result · `toolu_014LisC65zvDrVhZSWpNza2Z`</summary>

```text
artifacts/qa_probe_classification.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "1381f27c-bbed-4974-a861-d333b157cc94",
  "tool_use_result": {
    "filenames": [
      "artifacts/qa_probe_classification.py"
    ],
    "durationMs": 14,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Grep · `toolu_01UUmuVwxCBF7bbZCz8hrMc3`</summary>

```json
{
  "pattern": "class|LogReg|logistic|MLP|Linear|hidden|progress|early|mid|late|subtask|n_class",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/qa_probe_classification.py",
  "output_mode": "content",
  "-C": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "0c726ffd-7fe1-4cd0-96e2-9d895d76b4f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMx9A4gSothpLwh8s7Uz9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2002,
      "cache_read_input_tokens": 68018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2002
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

_source line 65 · 2026-05-19T15:09:03.512Z_

<details><summary>↩ Tool result · `toolu_01UUmuVwxCBF7bbZCz8hrMc3`</summary>

```text
1-"""
2:QA Probe Classification: Progress (4-class) and Subtask (binary) probes
3-on VLA layer features, DINOv2 cls_token, and projector output.
--
15-RESULT_DIR = "/root/autodl-tmp/vla-ssd/results/qa_probe"
16:RESULT_PATH = os.path.join(RESULT_DIR, "classification_results.json")
17-
--
25-TASKS = [
26:    "open_the_middle_drawer_of_the_cabinet",
27-    "open_the_top_drawer_and_put_the_bowl_inside",
28:    "push_the_plate_to_the_front_of_the_stove",
29:    "put_the_bowl_on_the_plate",
30-    "put_the_bowl_on_the_stove",
--
66-
67:def make_progress_labels(features_per_demo):
68:    """4-class progress labels: each trajectory split into 4 equal segments."""
69-    labels_per_demo = []
--
78-
79:def make_subtask_labels(features_per_demo):
80:    """Binary subtask labels: first half=0, second half=1."""
81-    labels_per_demo = []
--
83-        T = len(feat)
84:        mid = T // 2
85-        labels = np.zeros(T, dtype=int)
86:        labels[mid:] = 1
87-        labels_per_demo.append(labels)
--
165-        "tasks": {
166:            "progress_4class": {},
167:            "subtask_binary": {},
168-        },
--
178-    for label_task, label_fn in [
179:        ("progress_4class", make_progress_labels),
180:        ("subtask_binary", make_subtask_labels),
181-    ]:
--
231-    # Summary
232:    for label_task in ["progress_4class", "subtask_binary"]:
233:        prefix = "progress" if "progress" in label_task else "subtask"
234-        task_data = results["tasks"][label_task]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "b48355be-8775-4ed7-803f-b061bb195907",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1-\"\"\"\n2:QA Probe Classification: Progress (4-class) and Subtask (binary) probes\n3-on VLA layer features, DINOv2 cls_token, and projector output.\n--\n15-RESULT_DIR = \"/root/autodl-tmp/vla-ssd/results/qa_probe\"\n16:RESULT_PATH = os.path.join(RESULT_DIR, \"classification_results.json\")\n17-\n--\n25-TASKS = [\n26:    \"open_the_middle_drawer_of_the_cabinet\",\n27-    \"open_the_top_drawer_and_put_the_bowl_inside\",\n28:    \"push_the_plate_to_the_front_of_the_stove\",\n29:    \"put_the_bowl_on_the_plate\",\n30-    \"put_the_bowl_on_the_stove\",\n--\n66-\n67:def make_progress_labels(features_per_demo):\n68:    \"\"\"4-class progress labels: each trajectory split into 4 equal segments.\"\"\"\n69-    labels_per_demo = []\n--\n78-\n79:def make_subtask_labels(features_per_demo):\n80:    \"\"\"Binary subtask labels: first half=0, second half=1.\"\"\"\n81-    labels_per_demo = []\n--\n83-        T = len(feat)\n84:        mid = T // 2\n85-        labels = np.zeros(T, dtype=int)\n86:        labels[mid:] = 1\n87-        labels_per_demo.append(labels)\n--\n165-        \"tasks\": {\n166:            \"progress_4class\": {},\n167:            \"subtask_binary\": {},\n168-        },\n--\n178-    for label_task, label_fn in [\n179:        (\"progress_4class\", make_progress_labels),\n180:        (\"subtask_binary\", make_subtask_labels),\n181-    ]:\n--\n231-    # Summary\n232:    for label_task in [\"progress_4class\", \"subtask_binary\"]:\n233:        prefix = \"progress\" if \"progress\" in label_task else \"subtask\"\n234-        task_data = results[\"tasks\"][label_task]",
    "numLines": 45
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Grep · `toolu_01C7FPKaBX8BTzuDD285fooi`</summary>

```json
{
  "pattern": "LogisticRegression|sklearn|classifier|clf|probe.*=|PCA|n_components",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/qa_probe_classification.py",
  "output_mode": "content",
  "-C": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "36416a65-8e47-4881-9ec6-b8a318edac29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013WVx2ZGXTv8gdW955JPfWe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 733,
      "cache_read_input_tokens": 70020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 733
      },
      "output_tokens": 40,
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

_source line 67 · 2026-05-19T15:09:07.334Z_

<details><summary>↩ Tool result · `toolu_01C7FPKaBX8BTzuDD285fooi`</summary>

```text
9-import h5py
10:from sklearn.linear_model import LogisticRegression
11:from sklearn.metrics import accuracy_score, f1_score
12:from sklearn.model_selection import train_test_split
13-
--
91-def run_probe(features_per_demo, labels_per_demo):
92:    """Train LogisticRegression probe with random 80/20 split across all demos.
93-    Returns (accuracy, macro_f1).
--
101-
102:    clf = LogisticRegression(max_iter=1000, C=1.0, random_state=SEED)
103:    clf.fit(X_train, y_train)
104:    y_pred = clf.predict(X_test)
105-
--
163-    results = {
164:        "method": "Classification probe (LogisticRegression)",
165-        "tasks": {
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "68c5e35b-6fe1-476b-9e02-ea3aadc43820",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "9-import h5py\n10:from sklearn.linear_model import LogisticRegression\n11:from sklearn.metrics import accuracy_score, f1_score\n12:from sklearn.model_selection import train_test_split\n13-\n--\n91-def run_probe(features_per_demo, labels_per_demo):\n92:    \"\"\"Train LogisticRegression probe with random 80/20 split across all demos.\n93-    Returns (accuracy, macro_f1).\n--\n101-\n102:    clf = LogisticRegression(max_iter=1000, C=1.0, random_state=SEED)\n103:    clf.fit(X_train, y_train)\n104:    y_pred = clf.predict(X_test)\n105-\n--\n163-    results = {\n164:        \"method\": \"Classification probe (LogisticRegression)\",\n165-        \"tasks\": {",
    "numLines": 19
  }
}
```

</details>

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
Now I have the QA probe details:
- **Classifier**: LogisticRegression (sklearn, max_iter=1000, C=1.0)
- **Progress labeling**: 4-class (trajectory split into 4 equal temporal segments)
- **Subtask labeling**: Binary (first half=0, second half=1)
- **Split**: Random 80/20 across all demos
- **Seed**: 42

But wait, the appendix says "early/mid/late" (3-class) but the actual implementation is 4-class. 

Looking at the accuracy values, the 86.3% for trained last_preaction at L20 appears to be a combined metric across both tasks rather than a single classification task, which aligns with the table header mentioning "progress + subtask classification." The discrepancy between the documented 3-class progress scheme and the actual 4-class implementation in the code is still puzzling though. There's a potential discrepancy between the appendix describing "early/mid/late" progress classes and the actual 4-class implementation, but that might just be a simplification rather than a reproducibility issue. The real gaps I need to address are the missing details about the QA probe classifier: it uses LogisticRegression, divides trajectories into 4 equal temporal segments, and applies an 80/20 random split. Let me now put together all the edits, starting with a shared setup paragraph that covers the model checkpoint and dataset details. I'm specifying the model and dataset for the main experiments—OpenVLA-7B evaluated on LIBERO-Goal with its 10 tasks and 50 demonstrations per task. The setup details are cross-referenced to earlier sections, and I'm noting the hardware and random seed used throughout. For the cross-benchmark validation, I should also mention the LIBERO-Spatial evaluation with its 10 out-of-distribution spatial reasoning tasks. I need to clarify the progress classification scheme—the text describes it as "early/mid/late" but the actual implementation uses 4 equal temporal segments, and the 86.3% accuracy in the table was computed with the 4-class version, so the description is misleading and should be corrected to reflect the actual 4-class setup.

Now I'm going through the edits systematically. The linear probe section adequately references the main probe setup by mentioning the architecture and parameter count, with the MLP probe details already covered in §3.6. For the cross-instruction LOOCV validation, I'm checking whether the description of holding out one task's instructions across 10 folds is clear enough to validate that memorization isn't driving the results.

Looking at the counterfactual instruction analysis table, the metrics are well-defined—Cohen's d, token divergence, and Jaccard overlap—but the actual generation procedures for the counterfactual conditions (how the "wrong" instruction was selected, how "paraphrased" was created, how "shuffled" was performed) aren't fully spelled out in the table or its caption. I need to identify whether these procedures are described elsewhere in the paper or if they need clarification here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "aae5b3f3-f4f5-421e-a892-4584a1eb0116",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVNoNmASdFA3a7o6fgJTVG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 70753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 395
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

_source line 69_

<details open><summary>🔧 Tool call — Grep · `toolu_01P3ACJCkoPBeQDDeCEN4kHv`</summary>

```json
{
  "pattern": "counterfactual|paraphras|shuffled|wrong.*instruction|empty.*instruction",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-C": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "c74c64b0-79ba-4873-b5bc-2f2d69884cb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVNoNmASdFA3a7o6fgJTVG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 70753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 395
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

_source line 70 · 2026-05-19T15:09:50.864Z_

<details><summary>↩ Tool result · `toolu_01P3ACJCkoPBeQDDeCEN4kHv`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex-82-
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex-83-\paragraph{Counterfactual instruction analysis.}
docs/paper/experiments.tex:84:Replacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\ref{tab:counterfactual}).
docs/paper/experiments.tex:85:Token novelty ($1 - \text{Jaccard}$) predicts the ordering ($\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.
docs/paper/experiments.tex-86-L1 ablation ($d = 0.65$) falls within this range (Appendix~\ref{sec:action_trajectory}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex-87-
--
docs/paper/discussion.tex-5-VLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
docs/paper/discussion.tex-6-This explains Grant et al.'s~\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
docs/paper/discussion.tex:7:Seven analyses support distributed L1 routing: \emph{interventional} (dose-response, $d = 0.48 \to 0.64$; counterfactual, $d = 0.63$--$0.97$), \emph{supporting} (attention gradient $0 \to 9 \to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\times$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex-8-
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex-9-\paragraph{Mechanistic interpretation.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex-3-Three findings emerge.
docs/paper/abstract.tex-4-First, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).
docs/paper/abstract.tex:5:Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\times$ stronger for instruction-discriminative tasks ($p = 0.033$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex-6-Second, vision encoder representations show a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training effects concentrated at the readout token ($R^2$ $+0.069$, attention $+46$pp) rather than visual geometry.
docs/paper/abstract.tex-7-Token-level analysis reveals strict functional specialization: image tokens remain instruction-blind across all 32 layers while the readout token serves as the primary multimodal integration site.
--
docs/paper/appendix.tex-115-Instruction-head ablation ($N = 50$: 5 tasks $\times$ 10 demos) yields trajectory $d = 2.943$ (95\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-116-All 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.
docs/paper/appendix.tex:117:Counterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-118-Fine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\sim} 1{,}500$) provide higher resolution for ordering claims.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-119-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-181-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-182-\caption{Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$, token divergence (\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}
docs/paper/appendix.tex:183:\label{tab:counterfactual}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-184-\small
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-185-\begin{tabular}{lccc}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex-16-Three findings emerge from our analysis of OpenVLA-7B on LIBERO.
docs/paper/introduction.tex-17-\emph{First}, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads).
docs/paper/introduction.tex:18:Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\times$ stronger for instruction-discriminative tasks ($p = 0.033$).
docs/paper/introduction.tex-19-\emph{Second}, under RSA and action-probe decodability, vision encoder representations show a middle-layer peak ($R^2$ at L8--L14, RSA at L12), but this pattern is metric-dependent (CKA diverges; Appendix~\ref{sec:cka_appendix}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex-20-Training yields substantial functional improvement at the readout ($R^2$ $\Delta = +0.069$, $p < 0.0001$) with limited geometric gain ($\Delta\rho = 0.017$ on LIBERO-Goal; significant on LIBERO-Spatial, $p < 0.001$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "e08479d8-1667-492f-a91c-53357a9d7aea",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex-82-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex-83-\\paragraph{Counterfactual instruction analysis.}\ndocs/paper/experiments.tex:84:Replacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\\ref{tab:counterfactual}).\ndocs/paper/experiments.tex:85:Token novelty ($1 - \\text{Jaccard}$) predicts the ordering ($\\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.\ndocs/paper/experiments.tex-86-L1 ablation ($d = 0.65$) falls within this range (Appendix~\\ref{sec:action_trajectory}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex-87-\n--\ndocs/paper/discussion.tex-5-VLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\ndocs/paper/discussion.tex-6-This explains Grant et al.'s~\\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\ndocs/paper/discussion.tex:7:Seven analyses support distributed L1 routing: \\emph{interventional} (dose-response, $d = 0.48 \\to 0.64$; counterfactual, $d = 0.63$--$0.97$), \\emph{supporting} (attention gradient $0 \\to 9 \\to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\\times$).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex-8-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex-9-\\paragraph{Mechanistic interpretation.}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex-3-Three findings emerge.\ndocs/paper/abstract.tex-4-First, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).\ndocs/paper/abstract.tex:5:Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex-6-Second, vision encoder representations show a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training effects concentrated at the readout token ($R^2$ $+0.069$, attention $+46$pp) rather than visual geometry.\ndocs/paper/abstract.tex-7-Token-level analysis reveals strict functional specialization: image tokens remain instruction-blind across all 32 layers while the readout token serves as the primary multimodal integration site.\n--\ndocs/paper/appendix.tex-115-Instruction-head ablation ($N = 50$: 5 tasks $\\times$ 10 demos) yields trajectory $d = 2.943$ (95\\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-116-All 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.\ndocs/paper/appendix.tex:117:Counterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-118-Fine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\\sim} 1{,}500$) provide higher resolution for ordering claims.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-119-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-181-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-182-\\caption{Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$, token divergence (\\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \\text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}\ndocs/paper/appendix.tex:183:\\label{tab:counterfactual}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-184-\\small\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex-185-\\begin{tabular}{lccc}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex-16-Three findings emerge from our analysis of OpenVLA-7B on LIBERO.\ndocs/paper/introduction.tex-17-\\emph{First}, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads).\ndocs/paper/introduction.tex:18:Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).\ndocs/paper/introduction.tex-19-\\emph{Second}, under RSA and action-probe decodability, vision encoder representations show a middle-layer peak ($R^2$ at L8--L14, RSA at L12), but this pattern is metric-dependent (CKA diverges; Appendix~\\ref{sec:cka_appendix}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex-20-Training yields substantial functional improvement at the readout ($R^2$ $\\Delta = +0.069$, $p < 0.0001$) with limited geometric gain ($\\Delta\\rho = 0.017$ on LIBERO-Goal; significant on LIBERO-Spatial, $p < 0.001$).",
    "numLines": 36
  }
}
```

</details>

---

### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
The counterfactual instruction analysis is described in the main text (experiments.tex line 83-86) but the perturbation definitions are not explicit. The main text says "four perturbation types" — empty, wrong task, paraphrased, shuffled — but doesn't detail how each was generated (e.g., how the paraphrase was produced, which wrong instructions were used). This is a gap, but it's in the main text, not the appendix. The appendix just presents additional details (per-dimension analysis, etc.).


Now I'm ready to make the edits: I'll add a shared setup paragraph, include the LIBERO-Spatial sample count, revise the QA probe section with architecture details, and potentially add a note about the counterfactual generation procedure to the Action Trajectory section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "c2a24daf-0d25-42d2-ad9d-d1d116861a4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XepYqs5gnCNtq5QLJF7FC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4602,
      "cache_read_input_tokens": 71148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4602
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

_source line 72_

Now I have a complete picture. Let me make the edits. The main gaps are:

1. No shared setup paragraph (hardware, checkpoint source, seed)
2. LIBERO-Spatial missing explicit sample count
3. QA Probe missing classifier architecture and labeling details

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "2d1273fe-207c-4297-8a4f-2dab6ed6f55b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XepYqs5gnCNtq5QLJF7FC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4602,
      "cache_read_input_tokens": 71148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4602
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

_source line 73_

<details open><summary>🔧 Tool call — Edit · `toolu_01Nur2gemLXN7Z2G4PB9KsLQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "old_string": "\\section{Supplementary Material}\n\\label{sec:appendix}\n\n\\subsection{CKA Analysis Method}",
  "new_string": "\\section{Supplementary Material}\n\\label{sec:appendix}\n\nUnless noted otherwise, all analyses use OpenVLA-7B (\\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).\nModel conditions, representation extraction, metric definitions, and probe architectures follow \\S\\ref{sec:setup}--\\S\\ref{sec:probes}.\nCross-benchmark experiments (\\S\\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\\times$ 50 demonstrations).\nAll experiments ran on 2$\\times$ NVIDIA RTX PRO 6000 Ada GPUs (48\\,GB each); random seed is 42 unless stated otherwise.\n\n\\subsection{CKA Analysis Method}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "297c8b7a-007a-4825-b0e0-34f11ae05181",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XepYqs5gnCNtq5QLJF7FC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4602,
      "cache_read_input_tokens": 71148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4602
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

_source line 74 · 2026-05-19T15:10:02.340Z_

<details><summary>↩ Tool result · `toolu_01Nur2gemLXN7Z2G4PB9KsLQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "6586a85d-0d20-4418-9643-07f43d20f195",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "oldString": "\\section{Supplementary Material}\n\\label{sec:appendix}\n\n\\subsection{CKA Analysis Method}",
    "newString": "\\section{Supplementary Material}\n\\label{sec:appendix}\n\nUnless noted otherwise, all analyses use OpenVLA-7B (\\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).\nModel conditions, representation extraction, metric definitions, and probe architectures follow \\S\\ref{sec:setup}--\\S\\ref{sec:probes}.\nCross-benchmark experiments (\\S\\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\\times$ 50 demonstrations).\nAll experiments ran on 2$\\times$ NVIDIA RTX PRO 6000 Ada GPUs (48\\,GB each); random seed is 42 unless stated otherwise.\n\n\\subsection{CKA Analysis Method}",
    "originalFile": "\\paragraph{Use of Generative AI.}\nGenerative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.\n\n\\appendix\n\n\\section{Supplementary Material}\n\\label{sec:appendix}\n\n\\subsection{CKA Analysis Method}\n\\label{sec:cka_appendix}\n\nWe employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA as a complementary perspective.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.\n\n\\subsection{Metric Sensitivity: RSA versus CKA}\n\\label{sec:metric_sensitivity_appendix}\n\nLinear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.\n\nAt the per-layer level, linear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), with no inverted-U pattern.\nRSA captures rank-order geometric alignment; CKA captures global linear structure.\nThe dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}\n\\label{fig:metric_comparison}\n\\end{figure}\n\n\\subsection{Branch-Split Detailed Analysis}\n\\label{sec:branch_split_appendix}\n\nTo disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.\nThe two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.\nFusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.\nThe MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.\n\n\\subsection{RSA Across Representation Sources}\n\\label{sec:rsa_bar_appendix}\n\nFigure~\\ref{fig:rsa_bar} shows RSA with the action space across all representation sources; the ordering matches Table~\\ref{tab:rsa_overview}.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n\\subsection{Per-Layer RSA Profiles}\n\\label{sec:rsa_perlayer_appendix}\n\nFigure~\\ref{fig:rsa_perlayer_curve} extends Figure~\\ref{fig:layer_curves} (main text) by adding readout and untrained profiles.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}\n\\caption{Per-layer RSA ($\\rho$) for trained and untrained models at image\\_mean and readout (last\\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\\_mean diverge: readout $\\rho$ declines gradually ($0.628 \\to 0.584$) while image\\_mean $\\rho$ drops sharply ($0.628 \\to 0.422$), consistent with task-specific conditioning at the readout position.}\n\\label{fig:rsa_perlayer_curve}\n\\end{figure}\n\n\\subsection{Per-Layer Action Decoding Across Training Stages}\n\\label{sec:action_r2_threecond}\n\nFigure~\\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\\pm$ std).\nAll three conditions share L0 representations ($R^2 = 0.645 \\pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.\nThe trained model peaks at L9 ($R^2 = 0.643 \\pm 0.014$), consistent with progressive specialization for action-relevant feature integration.\nLlama-2 base shows a steady decline (L0: $0.645 \\to$ L32: $0.551$, std $0.003$--$0.035$), consistent with stable but unspecialized processing.\nThe untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability indicates that randomly initialized Transformer layers produce destructive interference on action-relevant structure.\nThe three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.\nThe qualitative pattern is consistent across all 3 seeds.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_action_r2_threecond.pdf}\n\\caption{Per-layer action probe $R^2$ (image\\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \\pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\\pm$ std).}\n\\label{fig:action_r2_threecond}\n\\end{figure}\n\n\\subsection{Random-Subset Ablation Details}\n\\label{sec:random_subset_ablation}\n\nTo evaluate whether the ablation effect in \\S\\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).\nDominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \\pm 0.013$ (Figure~\\ref{fig:random_subset_ablation}).\nThe dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); heads with higher instruction-attention fraction carry more organized routing signals, consistent with graded rather than binary specialization.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_random_subset_ablation.pdf}\n\\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \\pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with graded routing specialization across L1 heads.}\n\\label{fig:random_subset_ablation}\n\\end{figure}\n\n\\subsection{Action Trajectory Analysis Details}\n\\label{sec:action_trajectory}\n\nTable~\\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.\nBoth conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).\nThe gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.\n\nPer-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).\nToken-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.\n\n\\paragraph{Trajectory-level aggregation.}\nAggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\\sim}4\\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).\nInstruction-head ablation ($N = 50$: 5 tasks $\\times$ 10 demos) yields trajectory $d = 2.943$ (95\\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).\nAll 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.\nCounterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).\nFine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\\sim} 1{,}500$) provide higher resolution for ordering claims.\n\n\\paragraph{Ground-truth action error.}\nAblation redirects model outputs ($d = 0.65$) but does not systematically increase error relative to expert demonstrations: original MSE $= 0.498$; top-24 instruction-head ablation MSE $= 0.497$ ($\\Delta = -0.001$, Wilcoxon $p = 0.52$, n.s.); bottom-24 non-instruction heads MSE $= 0.506$ ($\\Delta = +0.008$).\nChanges concentrate on the gripper dimension; translation and rotation dimensions are negligibly affected.\nPer-task breakdown shows all $|\\Delta\\text{MSE}| < 3\\%$ of baseline with all $p > 0.27$; the near-zero aggregate $\\Delta$ reflects uniformly small per-task effects rather than cancellation across tasks.\nThis is consistent with the information-computation dissociation: routing heads control instruction-specific direction selection rather than action precision.\n\nTable~\\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).\nIndividual control heads produce ${\\sim}1.9\\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.\nThe 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\\ $0.41$), consistent with collective coordination rather than individual strength.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}\n\\label{tab:perhead_bootstrap}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nGroup & $N$ heads & Collective $d$ & Per-head $d$ [95\\% CI] \\\\\n\\midrule\nInstruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\\\\nControl & 8 & 0.41 & 0.051 [0.048, 0.055] \\\\\n\\midrule\nDifference & --- & --- & 0.024, $p = 0.0018$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInstruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.\n\nTable~\\ref{tab:dose_response} and Figure~\\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.\nTrajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\\Delta d / \\Delta 4 \\approx 0.026$), a plateau at 16--20 heads ($\\Delta d = 0.001$), and slow increase at 20--32.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\\ original action sequence; 95\\% bootstrap CIs ($10{,}000$ resamples).}\n\\label{tab:dose_response}\n\\small\n\\begin{tabular}{rcc}\n\\toprule\nHeads ablated & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\n4 & 0.482 & [0.449, 0.511] \\\\\n8 & 0.508 & [0.479, 0.541] \\\\\n12 & 0.560 & [0.529, 0.593] \\\\\n16 & 0.592 & [0.559, 0.625] \\\\\n20 & 0.593 & [0.559, 0.627] \\\\\n24 & 0.611 & [0.578, 0.645] \\\\\n28 & 0.619 & [0.587, 0.654] \\\\\n32 & 0.639 & [0.603, 0.671] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$, token divergence (\\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \\text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}\n\\label{tab:counterfactual}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Jaccard & Cohen's $d$ & Token div.\\ (\\%) \\\\\n\\midrule\nEmpty (no instruction) & 0.000 & 0.968 & 90.7 \\\\\nWrong (different task) & 0.174 & 0.844 & 89.5 \\\\\nParaphrased & 0.533 & 0.697 & 82.6 \\\\\nShuffled (random order) & 1.000 & 0.625 & 85.7 \\\\\n\\midrule\nL1 ablation (24 heads) & --- & 0.650 & 72.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}\n\\label{tab:action_shift_perdim}\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\nCondition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\\\\n\\midrule\nInstruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\\\\nControl (8) & 0.000 & 0.001 & 0.002 & 0.008 & 0.014 & 0.018 & 0.141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pretrained LLM Representation Quality Under Visual Input}\n\\label{sec:ood_diagnostics}\n\nA potential concern with the three-condition comparison (\\S\\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.\nWe evaluate three diagnostics to assess representation quality.\nActivation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \\to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.\nPer-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\\approx 0.28$ at L25, consistent with gradual differentiation rather than catastrophic out-of-distribution behavior.\nTop-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.\nThese diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining (Figure~\\ref{fig:ood_diagnostics}). These results support the validity of the three-condition comparison.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ood_diagnostics.pdf}\n\\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics indicate structured, non-degenerate representations.}\n\\label{fig:ood_diagnostics}\n\\end{figure}\n\n\\subsection{Probe Architecture Sensitivity}\n\\label{sec:linear_probe}\n\nTo rule out that our findings depend on MLP probe capacity ($N/\\text{params} \\approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \\to 7$, $N/\\text{params} \\approx 2.2$).\nThe inverted-U pattern reproduces: trained image\\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).\nThe trained--untrained gap is larger under the linear probe (L14: $\\Delta = +0.324$) than the MLP probe (L8: $\\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.\nUntrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.\nFor last\\_preaction tokens, the linear probe also corroborates the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\\Delta = 0.103$ ($p < 0.001$).\nThese results indicate that our qualitative findings reflect representational structure rather than probe capacity artifacts (Figure~\\ref{fig:linear_vs_mlp}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}\n\\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}\n\\label{fig:linear_vs_mlp}\n\\end{figure}\n\n\\subsection{Functional Probe Comparison}\n\\label{sec:probe_bars_appendix}\n\nFigure~\\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\\_mean ($0.655$, L8) exceed the projector baseline ($0.630$); the inverted-U extends to functional capacity.}\n\\label{fig:probe_bars}\n\\end{figure}\n\n\\subsection{Training Effect and Instruction Invariance}\n\\label{sec:instruction_invariance_appendix}\n\nFigure~\\ref{fig:factorial} shows trained vs.\\ untrained RSA profiles and instruction invariance.\nInstruction invariance holds across all conditions: maximum $|\\Delta| < 0.006$, so action geometry is visually grounded and not modulated by language instructions.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\\Delta{=}+0.017$, $3\\%$). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$; action geometry is visually grounded.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Additional RSA Values}\n\\label{sec:additional_rsa}\n\nDINOv2 \\texttt{patch\\_mean} achieves RSA $\\rho = 0.631$, between the \\texttt{cls\\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).\nVLA untrained readout peaks at L1 ($\\rho = 0.626$).\n\n\\subsection{Cross-Benchmark Validation: LIBERO-Spatial}\n\\label{sec:cross_benchmark_appendix}\n\nTo assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks requiring spatial reasoning).\nFigure~\\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.\n\nThe inverted-U profile replicates on LIBERO-Spatial: trained image\\_mean RSA peaks at L14 ($\\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.\nTraining produces a significant geometric gain (best-vs-best $\\Delta = +0.023$, 95\\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\\Delta = +0.017$, CI includes zero).\n\nTwo notable differences emerge.\nFirst, the absolute RSA values are higher on Spatial ($0.691$ vs.\\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.\nSecond, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\\Delta_\\text{layer}| = 1$).\nThis suggests that peak convergence is benchmark-specific rather than a general consequence of training.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig7.pdf}\n\\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}\n\\label{fig:cross_benchmark}\n\\end{figure}\n\n\\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}\n\\label{sec:spatial_cross_instruction}\n\nTable~\\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.\nThe core pattern from LIBERO-Goal replicates: image\\_mean remains at chance (${\\sim}10\\%$) across all layers and conditions, while the trained readout token saturates to $100\\%$ by L4.\nThe untrained readout decays more steeply than on LIBERO-Goal ($75.4\\%$ at L31 vs.\\ $82\\%$), consistent with greater task difficulty.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\\%$ from L4; image\\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\\ Table~\\ref{tab:dense_routing_main}).}\n\\label{tab:spatial_cross_instruction}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nToken & Condition & L1 & L4 & L8 & L16 & L31 \\\\\n\\midrule\nlast\\_preaction & Trained & 98.9\\% & 100.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\nlast\\_preaction & Untrained & 99.5\\% & 98.3\\% & 85.7\\% & 68.3\\% & 75.4\\% \\\\\nimage\\_mean & Trained & 10.2\\% & 10.0\\% & 9.9\\% & 10.0\\% & 10.1\\% \\\\\nimage\\_mean & Untrained & 10.1\\% & 10.0\\% & 10.0\\% & 10.0\\% & 10.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness Analyses}\n\\label{sec:robustness_appendix}\n\n\\subsubsection{Distance Metric Invariance}\n\\label{sec:metric_invariance}\n\nThe inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\\ref{tab:metric_invariance}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}\n\\label{tab:metric_invariance}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Eucl.\\ Peak & Cos.\\ Peak & Profile $r$ \\\\\n\\midrule\nTrained image\\_mean & L12 & L12 & 0.990 \\\\\nTrained last\\_preaction & L12 & L13 & 0.990 \\\\\nUntrained image\\_mean & L0 & L0 & 0.995 \\\\\nUntrained last\\_preaction & L1 & L1 & 0.992 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Per-DOF Decomposition}\n\\label{sec:perdof}\n\nRSA decomposition by action dimension indicates the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\\rho = 0.193$), rotation (peak L12, $\\rho = 0.175$), and gripper (peak L13, $\\rho = 0.106$) all exhibit non-monotonic profiles.\nPer-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.\n\n\\subsubsection{Permutation Test}\n\\label{sec:permutation}\n\nPermutation testing (1{,}000 shuffles) indicates all observed RSA values are highly significant: observed $\\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).\n\n\\subsubsection{Probe Seed Sensitivity}\n\\label{sec:seed_sensitivity}\n\nAction probe $R^2$ is highly stable across random seeds.\nOver 5 seeds (trained image\\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\\%$ ($0.655 \\pm 0.002$; Table~\\ref{tab:seed_sensitivity}).\nPeak layer concentrates in the L8--L10 region ($4/5$ seeds); the inverted-U shape is not a seed artifact.\nSeed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe $R^2$ peak across 5 random seeds (trained image\\_mean).}\n\\label{tab:seed_sensitivity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSeed & Peak Layer & Peak $R^2$ \\\\\n\\midrule\n0 & L9 & 0.654 \\\\\n1 & L16 & 0.656 \\\\\n2 & L9 & 0.653 \\\\\n3 & L10 & 0.655 \\\\\n42 & L9 & 0.655 \\\\\n\\midrule\nMean$\\pm$std & $10.6\\pm2.7$ & $0.655\\pm0.002$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Demonstration Subsample Sensitivity}\n\\label{sec:demo_sensitivity}\n\nTo verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\\ref{tab:demo_sensitivity}).\nThe RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions (high stability).\nThe probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$; $R^2$ is more sensitive to training set size than RSA.\nBoth metrics show reduced absolute values (RSA $-3.6\\%$, $R^2$ $-7.6\\%$) as expected from halved data, but the non-monotonic profile shape is preserved.\n\n\\begin{table}[h]\n\\centering\n\\caption{Inverted-U stability under demonstration subsampling (trained image\\_mean).}\n\\label{tab:demo_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 50 demos & 25 demos & $\\Delta$ \\\\\n\\midrule\nRSA peak layer & L12 & L12 & 0 \\\\\nRSA peak $\\rho$ & 0.628 & 0.606 & $-3.6\\%$ \\\\\n$R^2$ peak layer & L9 & L11 & $+2$ \\\\\n$R^2$ peak value & 0.659 & 0.609 & $-7.6\\%$ \\\\\nRSA profile $r$ & --- & 0.970 & --- \\\\\n$R^2$ profile $r$ & --- & 0.819 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detailed Training Effects}\n\\label{sec:training_effects_appendix}\n\nTable~\\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\\Delta{=}+0.017$, $3\\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{RSA ($\\rho$)}} \\\\\nBest-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\\n\\quad (trained L12 vs.\\ untrained L0) & & & \\\\\nSame-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained vs.\\ untrained) & & & \\\\\nInstruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Probe $R^2$}} \\\\\nBest-vs-best image\\_mean & $+$0.015 & excl.\\ 0 & 0.006 \\\\\n\\quad (trained L8 vs.\\ untrained L0) & & & \\\\\nBest-vs-best readout & $+$0.069 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained L13 vs.\\ untrained L32) & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Training Effect Size Summary}\n\\label{sec:training_effect_summary}\n\nTable~\\ref{tab:training_effect_summary} consolidates training effects across all metrics.\nTraining effects on image\\_mean metrics are modest (RSA $\\Delta = +0.017$, $R^2$ $\\Delta = +0.015$), but effects on last\\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\\Delta = +0.069$).\nThis asymmetry indicates that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effect sizes across metrics. Image\\_mean effects are modest; last\\_preaction effects are large. Training targets readout-token information integration.}\n\\label{tab:training_effect_summary}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Trained & Untrained & $\\Delta$ \\\\\n\\midrule\nRSA peak (image\\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\\\\n$R^2$ peak (image\\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\\\\n$R^2$ peak (last\\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\\\\nInstruction routing L31 & 100\\% & 82\\% & $+$18pp \\\\\nInstruction attention L1 & 58\\% & 12\\% & $+$46pp \\\\\nProgress classification & 86.3\\% (L20) & 85.3\\% (L4) & $+$1pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Instruction Routing Probes}\n\\label{sec:routing_appendix}\n\n\\subsubsection{Cross-Instruction Classification: Dense Layer Profile}\n\\label{sec:dense_routing}\n\nTable~\\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.\nThe step-function onset between L0 ($10\\%$, chance) and L1 (${\\geq}99.6\\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\\sim}12\\%$) suffices for linear classification at L1.\nBoth pretrained and VLA-trained models sustain $100\\%$ through L31; only random initialization shows progressive decay ($82\\%$ at L31). Deep-layer stability thus derives from structured pretrained weights rather than task-specific fine-tuning.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8. Values reflect dense routing evaluation; main-text Table~\\ref{tab:dense_routing_main} reports sparse single-split results, yielding minor differences (e.g., L8: $98.2\\%$ vs.\\ $98.6\\%$).}\n\\label{tab:dense_routing}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained & Untrained & Image\\_mean (trained) \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL2 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL3 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL5 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL6 & 100.0\\% & 97.3\\% & 10.0\\% \\\\\nL7 & 100.0\\% & 96.4\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.6\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction LOOCV Validation}\n\\label{sec:loocv}\n\nLeave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) validates that the cross-instruction probe result is not driven by memorization.\nTrained last\\_preaction achieves $100\\% \\pm 0.00$ across all 10 folds at layers L1--L31 (perfect generalization).\n\n\\subsubsection{QA Probe: Progress and Subtask Classification}\n\\label{sec:qa_probe}\n\nTo test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\\ref{tab:qa_probe}).\n\n\\begin{table}[h]\n\\centering\n\\caption{QA probe accuracy (progress + subtask classification, best layer).}\n\\label{tab:qa_probe}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSource & Best Layer & Accuracy \\\\\n\\midrule\nTrained last\\_preaction & L20 & 86.3\\% \\\\\nUntrained last\\_preaction & L20 & 85.3\\% \\\\\nDINOv2 cls\\_token & --- & 82.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction Probe Profiles}\n\\label{sec:probe_profiles}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_probe_conditions.pdf}\n\\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\\%$ at L1, saturating to $100\\%$. Llama-2 base starts at $80.2\\%$, reaching $100\\%$ by L5. Untrained starts at $100\\%$ but decays to $82\\%$ by L31.}\n\\label{fig:probe_conditions_appendix}\n\\end{figure}\n\n\\subsubsection{Four-Condition Cross-Instruction Probe Profile}\n\\label{app:finetuned_probe}\n\nTable~\\ref{tab:finetuned_probe} extends the three-condition probe comparison (Table~\\ref{tab:dense_routing_main}) with the LIBERO-finetuned checkpoint.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy across four training conditions. Task-specific fine-tuning (LIBERO) preserves instruction decodability at all layers despite eliminating L31 exit-layer attention engagement (18$\\to$0 instruction-dominant heads).}\n\\label{tab:finetuned_probe}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & Untrained & Llama-2 base & OpenVLA-7B & LIBERO-finetuned \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 80.2\\% & 99.6\\% & 99.7\\% \\\\\nL8 & 98.6\\% & 99.9\\% & 100.0\\% & 100.0\\% \\\\\nL31 & 82.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{L1 Attention Pattern Analysis}\n\\label{sec:attention_pattern}\n\nFigure~\\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.\nThe three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_l1_stacked_bar.pdf}\n\\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\\%$ text attention). Llama-2 base: 9/32 heads ($36.5\\%$). Untrained: 0/32 heads ($11.7\\%$). See Table~\\ref{tab:routing_gradient} for quantitative comparison.}\n\\label{fig:attention_appendix}\n\\end{figure}\n\n\\subsubsection{Multi-Layer Attention Patterns}\n\\label{sec:multilayer_attention}\n\nTable~\\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\\ref{fig:attention_profile}, main text).\nThe full profile (Figure~\\ref{fig:multilayer_attention}) reveals three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_multi_layer_attn.pdf}\n\\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}\n\\label{fig:multilayer_attention}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\\ref{tab:routing_gradient}) due to threshold boundary effects.}\n\\label{tab:multilayer_attention}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{VLA Trained} & \\multicolumn{2}{c}{Llama-2 base} & \\multicolumn{2}{c}{Untrained} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\nLayer & Heads & Text\\% & Heads & Text\\% & Heads & Text\\% \\\\\n\\midrule\nL1 & \\textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\\\\nL8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\\\\nL16 & 10/32 & 48.4 & \\textbf{25/32} & 60.2 & 0/32 & 9.2 \\\\\nL31 & \\textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Threshold Sensitivity Analysis}\n\\label{sec:threshold_sensitivity}\n\nThe main text defines instruction-dominant heads as those allocating $>50\\%$ attention to instruction tokens.\nTable~\\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\\% to 70\\%; the 50\\% threshold is not a boundary-sensitive choice.\n\n\\begin{table}[h]\n\\centering\n\\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}\n\\label{tab:threshold_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nThreshold & VLA Trained & Llama-2 base & Untrained \\\\\n\\midrule\n30\\% & 32 & 13 & 0 \\\\\n40\\% & 31 & 10 & 0 \\\\\n50\\% & 24 & 9 & 0 \\\\\n60\\% & 9 & 4 & 0 \\\\\n70\\% & 5 & 3 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{L1 Attention Decomposition by Head Group}\n\\label{sec:attention_decomp}\n\nTable~\\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.\n\n\\begin{table}[h]\n\\centering\n\\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}\n\\label{tab:attention_decomp}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nHead Group & $N$ & Instruction & Vision & BOS/Other \\\\\n\\midrule\nInstruction-dominant & 24 & 62.4\\% & 18.8\\% & 18.8\\% \\\\\nControl & 8 & 44.9\\% & 27.1\\% & 28.0\\% \\\\\n\\midrule\n$\\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHead-level instruction attention entropy reaches $99.5\\%$ of the uniform maximum; routing is broadly distributed rather than concentrated in a few heads.\n\n\\paragraph{Per-token attention normalization.}\nThe $57.7\\%$ aggregate text attention in instruction-dominant heads partly reflects token-count imbalance (22 instruction vs.\\ 256 image tokens).\nPer-token normalization reveals a $38.2\\times$ ratio: each instruction token receives $38.2\\times$ the attention of each image token in trained instruction-dominant heads, compared to only $1.5\\times$ in untrained heads (a $25.5\\times$ increase from training).\nInstruction-dominant heads also show lower attention entropy ($0.465$) than non-dominant heads ($0.569$), indicating more concentrated attention distributions.\n\n\\subsection{Per-Dimension Action MAE Under Head Ablation}\n\\label{sec:per_dim_mae}\n\nTable~\\ref{tab:per_dim_mae} extends Table~\\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\\times$); instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\\times$) falls between the two groups.}\n\\label{tab:per_dim_mae}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDimension & Instr.\\ 24h MAE & Control 8h MAE & Ratio \\\\\n\\midrule\n$dx$ & 0.00189 & 0.00037 & 5.09$\\times$ \\\\\n$dy$ & 0.00531 & 0.00125 & 4.26$\\times$ \\\\\n$dz$ & 0.00762 & 0.00243 & 3.14$\\times$ \\\\\n$roll$ & 0.02059 & 0.00785 & 2.62$\\times$ \\\\\n$pitch$ & 0.03071 & 0.01387 & 2.21$\\times$ \\\\\n$yaw$ & 0.03388 & 0.01783 & 1.90$\\times$ \\\\\n$gripper$ & 0.29072 & 0.14072 & 2.07$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}\n\\label{sec:per_task_r2}\n\nTable~\\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\\Delta > 0$): instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\\Delta R^2 = +0.107$; the 50-demo setting (\\S\\ref{sec:learned_routing}) yields a consistent $+0.059$.}\n\\label{tab:per_task_r2}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTask & Baseline $R^2$ & Ablated $R^2$ & $\\Delta R^2$ \\\\\n\\midrule\nopen middle drawer & 0.197 & 0.221 & $+$0.024 \\\\\nopen top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\\\\npush plate to stove & 0.190 & 0.197 & $+$0.007 \\\\\nput bowl on plate & 0.375 & 0.474 & $+$0.099 \\\\\nput bowl on stove & 0.235 & 0.395 & $+$0.160 \\\\\nput bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\\\\nput cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\\\\nput wine on rack & 0.189 & 0.424 & $+$0.235 \\\\\nput wine on cabinet & 0.279 & 0.353 & $+$0.074 \\\\\nturn on stove & 0.385 & 0.421 & $+$0.036 \\\\\n\\midrule\nMean $\\pm$ std & $0.256 \\pm 0.070$ & $0.363 \\pm 0.088$ & $+$0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Task Complexity and Routing Dependence}\n\\label{sec:task_complexity}\n\nWe classify tasks as \\emph{instruction-discriminative} when multiple tasks share the same manipulated object(s), requiring instruction content to disambiguate the target action (e.g., ``put bowl on plate'' vs.\\ ``put bowl on stove''); remaining tasks involve unique object-action pairings recoverable from visual context alone.\nTable~\\ref{tab:task_complexity} reports per-task $|\\Delta R^2|$ under both groupings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Task-level L1 ablation effects ($|\\Delta R^2|$) grouped by instruction dependence. \\emph{Primary} (conservative): cream cheese in bowl classified as visual-sufficient ($2.5\\times$, $p = 0.033$). \\emph{Sensitivity} (shared-object criterion): cream cheese reclassified as instruction-discriminative ($6.5\\times$, $p = 0.008$).}\n\\label{tab:task_complexity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nTask & $|\\Delta R^2|$ & Group \\\\\n\\midrule\nput wine on rack & 0.235 & Instr-disc \\\\\nput bowl on cabinet & 0.201 & Instr-disc \\\\\nput bowl on stove & 0.160 & Instr-disc \\\\\nput bowl on plate & 0.099 & Instr-disc \\\\\nopen top drawer + bowl & 0.075 & Instr-disc \\\\\nput wine on cabinet & 0.074 & Instr-disc \\\\\n\\midrule\nput cream cheese in bowl$^\\dagger$ & 0.159 & Vis-suff \\\\\nturn on stove & 0.036 & Vis-suff \\\\\nopen middle drawer & 0.024 & Vis-suff \\\\\npush plate to stove & 0.007 & Vis-suff \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Primary}: Instr-disc mean $0.141$; Vis-suff mean $0.057$} \\\\\n\\multicolumn{3}{l}{Mann-Whitney $U = 21.0$, $p = 0.033$, ratio $= 2.49\\times$} \\\\\n\\multicolumn{3}{l}{\\textbf{Sensitivity}$^\\dagger$: cream cheese as Instr-disc: $p = 0.008$, $6.5\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Leave-one-out sensitivity.}\nAll leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.\nReclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).\n\n\\subsection{Specificity Control: Matched-Size Head Ablation}\n\\label{sec:specificity_control}\n\nTo test whether ablation effects are specific to instruction-dominant heads, we ablate four matched-size subsets of 24 heads at L1: instruction-dominant (highest instruction attention fraction), image-dominant (highest image attention fraction), random (5 seeds), and bottom-24 (lowest instruction attention fraction; overlaps 16/24 heads with the instruction-dominant group).\n\n\\begin{table}[h]\n\\centering\n\\caption{Matched-size ablation controls: trajectory disruption ($d$) from ablating 24-head subsets at L1, ranked by instruction attention fraction. Instruction-dominant heads produce the largest effect, but the modest gap ($8\\%$ over random) indicates distributed, attention-graded routing rather than a dedicated subset.}\n\\label{tab:specificity_control}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition (24 heads) & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\nInstruction-dominant & 0.650 & (reference) \\\\\nRandom (5 seeds) & $0.601 \\pm 0.021$ & $[0.568, 0.622]$ \\\\\nImage-dominant & 0.580 & $[0.547, 0.613]$ \\\\\nBottom-24 & 0.565 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll conditions yield comparable ground-truth MSE ($0.487$--$0.504$ vs.\\ baseline $0.497$), consistent with direction-selective rather than precision-degrading effects.\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 6,
        "newStart": 6,
        "newLines": 11,
        "lines": [
          " \\section{Supplementary Material}",
          " \\label{sec:appendix}",
          " ",
          "+Unless noted otherwise, all analyses use OpenVLA-7B (\\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).",
          "+Model conditions, representation extraction, metric definitions, and probe architectures follow \\S\\ref{sec:setup}--\\S\\ref{sec:probes}.",
          "+Cross-benchmark experiments (\\S\\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\\times$ 50 demonstrations).",
          "+All experiments ran on 2$\\times$ NVIDIA RTX PRO 6000 Ada GPUs (48\\,GB each); random seed is 42 unless stated otherwise.",
          "+",
          " \\subsection{CKA Analysis Method}",
          " \\label{sec:cka_appendix}",
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

_source line 75_

<details open><summary>🔧 Tool call — Edit · `toolu_01M8BVLyxDfvnwUHBZzTaL2z`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "old_string": "we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks requiring spatial reasoning).",
  "new_string": "we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks $\\times$ 50 demonstrations each, requiring spatial reasoning)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "5393b0d6-0dea-450a-9d7c-33428a964ad4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167fTmmDYcEB8eBom9y2nJp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 75750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 719
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

_source line 76 · 2026-05-19T15:10:06.932Z_

<details><summary>↩ Tool result · `toolu_01M8BVLyxDfvnwUHBZzTaL2z`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "7b01d35c-308f-4411-a9f8-21909f095a0a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "oldString": "we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks requiring spatial reasoning).",
    "newString": "we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks $\\times$ 50 demonstrations each, requiring spatial reasoning).",
    "originalFile": "\\paragraph{Use of Generative AI.}\nGenerative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.\n\n\\appendix\n\n\\section{Supplementary Material}\n\\label{sec:appendix}\n\nUnless noted otherwise, all analyses use OpenVLA-7B (\\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).\nModel conditions, representation extraction, metric definitions, and probe architectures follow \\S\\ref{sec:setup}--\\S\\ref{sec:probes}.\nCross-benchmark experiments (\\S\\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\\times$ 50 demonstrations).\nAll experiments ran on 2$\\times$ NVIDIA RTX PRO 6000 Ada GPUs (48\\,GB each); random seed is 42 unless stated otherwise.\n\n\\subsection{CKA Analysis Method}\n\\label{sec:cka_appendix}\n\nWe employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA as a complementary perspective.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.\n\n\\subsection{Metric Sensitivity: RSA versus CKA}\n\\label{sec:metric_sensitivity_appendix}\n\nLinear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.\n\nAt the per-layer level, linear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), with no inverted-U pattern.\nRSA captures rank-order geometric alignment; CKA captures global linear structure.\nThe dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}\n\\label{fig:metric_comparison}\n\\end{figure}\n\n\\subsection{Branch-Split Detailed Analysis}\n\\label{sec:branch_split_appendix}\n\nTo disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.\nThe two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.\nFusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.\nThe MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.\n\n\\subsection{RSA Across Representation Sources}\n\\label{sec:rsa_bar_appendix}\n\nFigure~\\ref{fig:rsa_bar} shows RSA with the action space across all representation sources; the ordering matches Table~\\ref{tab:rsa_overview}.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n\\subsection{Per-Layer RSA Profiles}\n\\label{sec:rsa_perlayer_appendix}\n\nFigure~\\ref{fig:rsa_perlayer_curve} extends Figure~\\ref{fig:layer_curves} (main text) by adding readout and untrained profiles.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}\n\\caption{Per-layer RSA ($\\rho$) for trained and untrained models at image\\_mean and readout (last\\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\\_mean diverge: readout $\\rho$ declines gradually ($0.628 \\to 0.584$) while image\\_mean $\\rho$ drops sharply ($0.628 \\to 0.422$), consistent with task-specific conditioning at the readout position.}\n\\label{fig:rsa_perlayer_curve}\n\\end{figure}\n\n\\subsection{Per-Layer Action Decoding Across Training Stages}\n\\label{sec:action_r2_threecond}\n\nFigure~\\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\\pm$ std).\nAll three conditions share L0 representations ($R^2 = 0.645 \\pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.\nThe trained model peaks at L9 ($R^2 = 0.643 \\pm 0.014$), consistent with progressive specialization for action-relevant feature integration.\nLlama-2 base shows a steady decline (L0: $0.645 \\to$ L32: $0.551$, std $0.003$--$0.035$), consistent with stable but unspecialized processing.\nThe untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability indicates that randomly initialized Transformer layers produce destructive interference on action-relevant structure.\nThe three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.\nThe qualitative pattern is consistent across all 3 seeds.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_action_r2_threecond.pdf}\n\\caption{Per-layer action probe $R^2$ (image\\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \\pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\\pm$ std).}\n\\label{fig:action_r2_threecond}\n\\end{figure}\n\n\\subsection{Random-Subset Ablation Details}\n\\label{sec:random_subset_ablation}\n\nTo evaluate whether the ablation effect in \\S\\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).\nDominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \\pm 0.013$ (Figure~\\ref{fig:random_subset_ablation}).\nThe dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); heads with higher instruction-attention fraction carry more organized routing signals, consistent with graded rather than binary specialization.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_random_subset_ablation.pdf}\n\\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \\pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with graded routing specialization across L1 heads.}\n\\label{fig:random_subset_ablation}\n\\end{figure}\n\n\\subsection{Action Trajectory Analysis Details}\n\\label{sec:action_trajectory}\n\nTable~\\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.\nBoth conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).\nThe gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.\n\nPer-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).\nToken-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.\n\n\\paragraph{Trajectory-level aggregation.}\nAggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\\sim}4\\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).\nInstruction-head ablation ($N = 50$: 5 tasks $\\times$ 10 demos) yields trajectory $d = 2.943$ (95\\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).\nAll 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.\nCounterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).\nFine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\\sim} 1{,}500$) provide higher resolution for ordering claims.\n\n\\paragraph{Ground-truth action error.}\nAblation redirects model outputs ($d = 0.65$) but does not systematically increase error relative to expert demonstrations: original MSE $= 0.498$; top-24 instruction-head ablation MSE $= 0.497$ ($\\Delta = -0.001$, Wilcoxon $p = 0.52$, n.s.); bottom-24 non-instruction heads MSE $= 0.506$ ($\\Delta = +0.008$).\nChanges concentrate on the gripper dimension; translation and rotation dimensions are negligibly affected.\nPer-task breakdown shows all $|\\Delta\\text{MSE}| < 3\\%$ of baseline with all $p > 0.27$; the near-zero aggregate $\\Delta$ reflects uniformly small per-task effects rather than cancellation across tasks.\nThis is consistent with the information-computation dissociation: routing heads control instruction-specific direction selection rather than action precision.\n\nTable~\\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).\nIndividual control heads produce ${\\sim}1.9\\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.\nThe 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\\ $0.41$), consistent with collective coordination rather than individual strength.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}\n\\label{tab:perhead_bootstrap}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nGroup & $N$ heads & Collective $d$ & Per-head $d$ [95\\% CI] \\\\\n\\midrule\nInstruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\\\\nControl & 8 & 0.41 & 0.051 [0.048, 0.055] \\\\\n\\midrule\nDifference & --- & --- & 0.024, $p = 0.0018$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInstruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.\n\nTable~\\ref{tab:dose_response} and Figure~\\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.\nTrajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\\Delta d / \\Delta 4 \\approx 0.026$), a plateau at 16--20 heads ($\\Delta d = 0.001$), and slow increase at 20--32.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\\ original action sequence; 95\\% bootstrap CIs ($10{,}000$ resamples).}\n\\label{tab:dose_response}\n\\small\n\\begin{tabular}{rcc}\n\\toprule\nHeads ablated & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\n4 & 0.482 & [0.449, 0.511] \\\\\n8 & 0.508 & [0.479, 0.541] \\\\\n12 & 0.560 & [0.529, 0.593] \\\\\n16 & 0.592 & [0.559, 0.625] \\\\\n20 & 0.593 & [0.559, 0.627] \\\\\n24 & 0.611 & [0.578, 0.645] \\\\\n28 & 0.619 & [0.587, 0.654] \\\\\n32 & 0.639 & [0.603, 0.671] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$, token divergence (\\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \\text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}\n\\label{tab:counterfactual}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Jaccard & Cohen's $d$ & Token div.\\ (\\%) \\\\\n\\midrule\nEmpty (no instruction) & 0.000 & 0.968 & 90.7 \\\\\nWrong (different task) & 0.174 & 0.844 & 89.5 \\\\\nParaphrased & 0.533 & 0.697 & 82.6 \\\\\nShuffled (random order) & 1.000 & 0.625 & 85.7 \\\\\n\\midrule\nL1 ablation (24 heads) & --- & 0.650 & 72.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}\n\\label{tab:action_shift_perdim}\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\nCondition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\\\\n\\midrule\nInstruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\\\\nControl (8) & 0.000 & 0.001 & 0.002 & 0.008 & 0.014 & 0.018 & 0.141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pretrained LLM Representation Quality Under Visual Input}\n\\label{sec:ood_diagnostics}\n\nA potential concern with the three-condition comparison (\\S\\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.\nWe evaluate three diagnostics to assess representation quality.\nActivation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \\to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.\nPer-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\\approx 0.28$ at L25, consistent with gradual differentiation rather than catastrophic out-of-distribution behavior.\nTop-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.\nThese diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining (Figure~\\ref{fig:ood_diagnostics}). These results support the validity of the three-condition comparison.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ood_diagnostics.pdf}\n\\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics indicate structured, non-degenerate representations.}\n\\label{fig:ood_diagnostics}\n\\end{figure}\n\n\\subsection{Probe Architecture Sensitivity}\n\\label{sec:linear_probe}\n\nTo rule out that our findings depend on MLP probe capacity ($N/\\text{params} \\approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \\to 7$, $N/\\text{params} \\approx 2.2$).\nThe inverted-U pattern reproduces: trained image\\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).\nThe trained--untrained gap is larger under the linear probe (L14: $\\Delta = +0.324$) than the MLP probe (L8: $\\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.\nUntrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.\nFor last\\_preaction tokens, the linear probe also corroborates the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\\Delta = 0.103$ ($p < 0.001$).\nThese results indicate that our qualitative findings reflect representational structure rather than probe capacity artifacts (Figure~\\ref{fig:linear_vs_mlp}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}\n\\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}\n\\label{fig:linear_vs_mlp}\n\\end{figure}\n\n\\subsection{Functional Probe Comparison}\n\\label{sec:probe_bars_appendix}\n\nFigure~\\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\\_mean ($0.655$, L8) exceed the projector baseline ($0.630$); the inverted-U extends to functional capacity.}\n\\label{fig:probe_bars}\n\\end{figure}\n\n\\subsection{Training Effect and Instruction Invariance}\n\\label{sec:instruction_invariance_appendix}\n\nFigure~\\ref{fig:factorial} shows trained vs.\\ untrained RSA profiles and instruction invariance.\nInstruction invariance holds across all conditions: maximum $|\\Delta| < 0.006$, so action geometry is visually grounded and not modulated by language instructions.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\\Delta{=}+0.017$, $3\\%$). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$; action geometry is visually grounded.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Additional RSA Values}\n\\label{sec:additional_rsa}\n\nDINOv2 \\texttt{patch\\_mean} achieves RSA $\\rho = 0.631$, between the \\texttt{cls\\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).\nVLA untrained readout peaks at L1 ($\\rho = 0.626$).\n\n\\subsection{Cross-Benchmark Validation: LIBERO-Spatial}\n\\label{sec:cross_benchmark_appendix}\n\nTo assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks requiring spatial reasoning).\nFigure~\\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.\n\nThe inverted-U profile replicates on LIBERO-Spatial: trained image\\_mean RSA peaks at L14 ($\\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.\nTraining produces a significant geometric gain (best-vs-best $\\Delta = +0.023$, 95\\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\\Delta = +0.017$, CI includes zero).\n\nTwo notable differences emerge.\nFirst, the absolute RSA values are higher on Spatial ($0.691$ vs.\\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.\nSecond, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\\Delta_\\text{layer}| = 1$).\nThis suggests that peak convergence is benchmark-specific rather than a general consequence of training.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig7.pdf}\n\\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}\n\\label{fig:cross_benchmark}\n\\end{figure}\n\n\\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}\n\\label{sec:spatial_cross_instruction}\n\nTable~\\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.\nThe core pattern from LIBERO-Goal replicates: image\\_mean remains at chance (${\\sim}10\\%$) across all layers and conditions, while the trained readout token saturates to $100\\%$ by L4.\nThe untrained readout decays more steeply than on LIBERO-Goal ($75.4\\%$ at L31 vs.\\ $82\\%$), consistent with greater task difficulty.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\\%$ from L4; image\\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\\ Table~\\ref{tab:dense_routing_main}).}\n\\label{tab:spatial_cross_instruction}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nToken & Condition & L1 & L4 & L8 & L16 & L31 \\\\\n\\midrule\nlast\\_preaction & Trained & 98.9\\% & 100.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\nlast\\_preaction & Untrained & 99.5\\% & 98.3\\% & 85.7\\% & 68.3\\% & 75.4\\% \\\\\nimage\\_mean & Trained & 10.2\\% & 10.0\\% & 9.9\\% & 10.0\\% & 10.1\\% \\\\\nimage\\_mean & Untrained & 10.1\\% & 10.0\\% & 10.0\\% & 10.0\\% & 10.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness Analyses}\n\\label{sec:robustness_appendix}\n\n\\subsubsection{Distance Metric Invariance}\n\\label{sec:metric_invariance}\n\nThe inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\\ref{tab:metric_invariance}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}\n\\label{tab:metric_invariance}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Eucl.\\ Peak & Cos.\\ Peak & Profile $r$ \\\\\n\\midrule\nTrained image\\_mean & L12 & L12 & 0.990 \\\\\nTrained last\\_preaction & L12 & L13 & 0.990 \\\\\nUntrained image\\_mean & L0 & L0 & 0.995 \\\\\nUntrained last\\_preaction & L1 & L1 & 0.992 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Per-DOF Decomposition}\n\\label{sec:perdof}\n\nRSA decomposition by action dimension indicates the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\\rho = 0.193$), rotation (peak L12, $\\rho = 0.175$), and gripper (peak L13, $\\rho = 0.106$) all exhibit non-monotonic profiles.\nPer-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.\n\n\\subsubsection{Permutation Test}\n\\label{sec:permutation}\n\nPermutation testing (1{,}000 shuffles) indicates all observed RSA values are highly significant: observed $\\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).\n\n\\subsubsection{Probe Seed Sensitivity}\n\\label{sec:seed_sensitivity}\n\nAction probe $R^2$ is highly stable across random seeds.\nOver 5 seeds (trained image\\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\\%$ ($0.655 \\pm 0.002$; Table~\\ref{tab:seed_sensitivity}).\nPeak layer concentrates in the L8--L10 region ($4/5$ seeds); the inverted-U shape is not a seed artifact.\nSeed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe $R^2$ peak across 5 random seeds (trained image\\_mean).}\n\\label{tab:seed_sensitivity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSeed & Peak Layer & Peak $R^2$ \\\\\n\\midrule\n0 & L9 & 0.654 \\\\\n1 & L16 & 0.656 \\\\\n2 & L9 & 0.653 \\\\\n3 & L10 & 0.655 \\\\\n42 & L9 & 0.655 \\\\\n\\midrule\nMean$\\pm$std & $10.6\\pm2.7$ & $0.655\\pm0.002$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Demonstration Subsample Sensitivity}\n\\label{sec:demo_sensitivity}\n\nTo verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\\ref{tab:demo_sensitivity}).\nThe RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions (high stability).\nThe probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$; $R^2$ is more sensitive to training set size than RSA.\nBoth metrics show reduced absolute values (RSA $-3.6\\%$, $R^2$ $-7.6\\%$) as expected from halved data, but the non-monotonic profile shape is preserved.\n\n\\begin{table}[h]\n\\centering\n\\caption{Inverted-U stability under demonstration subsampling (trained image\\_mean).}\n\\label{tab:demo_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 50 demos & 25 demos & $\\Delta$ \\\\\n\\midrule\nRSA peak layer & L12 & L12 & 0 \\\\\nRSA peak $\\rho$ & 0.628 & 0.606 & $-3.6\\%$ \\\\\n$R^2$ peak layer & L9 & L11 & $+2$ \\\\\n$R^2$ peak value & 0.659 & 0.609 & $-7.6\\%$ \\\\\nRSA profile $r$ & --- & 0.970 & --- \\\\\n$R^2$ profile $r$ & --- & 0.819 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detailed Training Effects}\n\\label{sec:training_effects_appendix}\n\nTable~\\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\\Delta{=}+0.017$, $3\\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{RSA ($\\rho$)}} \\\\\nBest-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\\n\\quad (trained L12 vs.\\ untrained L0) & & & \\\\\nSame-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained vs.\\ untrained) & & & \\\\\nInstruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Probe $R^2$}} \\\\\nBest-vs-best image\\_mean & $+$0.015 & excl.\\ 0 & 0.006 \\\\\n\\quad (trained L8 vs.\\ untrained L0) & & & \\\\\nBest-vs-best readout & $+$0.069 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained L13 vs.\\ untrained L32) & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Training Effect Size Summary}\n\\label{sec:training_effect_summary}\n\nTable~\\ref{tab:training_effect_summary} consolidates training effects across all metrics.\nTraining effects on image\\_mean metrics are modest (RSA $\\Delta = +0.017$, $R^2$ $\\Delta = +0.015$), but effects on last\\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\\Delta = +0.069$).\nThis asymmetry indicates that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effect sizes across metrics. Image\\_mean effects are modest; last\\_preaction effects are large. Training targets readout-token information integration.}\n\\label{tab:training_effect_summary}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Trained & Untrained & $\\Delta$ \\\\\n\\midrule\nRSA peak (image\\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\\\\n$R^2$ peak (image\\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\\\\n$R^2$ peak (last\\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\\\\nInstruction routing L31 & 100\\% & 82\\% & $+$18pp \\\\\nInstruction attention L1 & 58\\% & 12\\% & $+$46pp \\\\\nProgress classification & 86.3\\% (L20) & 85.3\\% (L4) & $+$1pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Instruction Routing Probes}\n\\label{sec:routing_appendix}\n\n\\subsubsection{Cross-Instruction Classification: Dense Layer Profile}\n\\label{sec:dense_routing}\n\nTable~\\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.\nThe step-function onset between L0 ($10\\%$, chance) and L1 (${\\geq}99.6\\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\\sim}12\\%$) suffices for linear classification at L1.\nBoth pretrained and VLA-trained models sustain $100\\%$ through L31; only random initialization shows progressive decay ($82\\%$ at L31). Deep-layer stability thus derives from structured pretrained weights rather than task-specific fine-tuning.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8. Values reflect dense routing evaluation; main-text Table~\\ref{tab:dense_routing_main} reports sparse single-split results, yielding minor differences (e.g., L8: $98.2\\%$ vs.\\ $98.6\\%$).}\n\\label{tab:dense_routing}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained & Untrained & Image\\_mean (trained) \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL2 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL3 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL5 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL6 & 100.0\\% & 97.3\\% & 10.0\\% \\\\\nL7 & 100.0\\% & 96.4\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.6\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction LOOCV Validation}\n\\label{sec:loocv}\n\nLeave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) validates that the cross-instruction probe result is not driven by memorization.\nTrained last\\_preaction achieves $100\\% \\pm 0.00$ across all 10 folds at layers L1--L31 (perfect generalization).\n\n\\subsubsection{QA Probe: Progress and Subtask Classification}\n\\label{sec:qa_probe}\n\nTo test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\\ref{tab:qa_probe}).\n\n\\begin{table}[h]\n\\centering\n\\caption{QA probe accuracy (progress + subtask classification, best layer).}\n\\label{tab:qa_probe}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSource & Best Layer & Accuracy \\\\\n\\midrule\nTrained last\\_preaction & L20 & 86.3\\% \\\\\nUntrained last\\_preaction & L20 & 85.3\\% \\\\\nDINOv2 cls\\_token & --- & 82.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction Probe Profiles}\n\\label{sec:probe_profiles}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_probe_conditions.pdf}\n\\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\\%$ at L1, saturating to $100\\%$. Llama-2 base starts at $80.2\\%$, reaching $100\\%$ by L5. Untrained starts at $100\\%$ but decays to $82\\%$ by L31.}\n\\label{fig:probe_conditions_appendix}\n\\end{figure}\n\n\\subsubsection{Four-Condition Cross-Instruction Probe Profile}\n\\label{app:finetuned_probe}\n\nTable~\\ref{tab:finetuned_probe} extends the three-condition probe comparison (Table~\\ref{tab:dense_routing_main}) with the LIBERO-finetuned checkpoint.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy across four training conditions. Task-specific fine-tuning (LIBERO) preserves instruction decodability at all layers despite eliminating L31 exit-layer attention engagement (18$\\to$0 instruction-dominant heads).}\n\\label{tab:finetuned_probe}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & Untrained & Llama-2 base & OpenVLA-7B & LIBERO-finetuned \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 80.2\\% & 99.6\\% & 99.7\\% \\\\\nL8 & 98.6\\% & 99.9\\% & 100.0\\% & 100.0\\% \\\\\nL31 & 82.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{L1 Attention Pattern Analysis}\n\\label{sec:attention_pattern}\n\nFigure~\\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.\nThe three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_l1_stacked_bar.pdf}\n\\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\\%$ text attention). Llama-2 base: 9/32 heads ($36.5\\%$). Untrained: 0/32 heads ($11.7\\%$). See Table~\\ref{tab:routing_gradient} for quantitative comparison.}\n\\label{fig:attention_appendix}\n\\end{figure}\n\n\\subsubsection{Multi-Layer Attention Patterns}\n\\label{sec:multilayer_attention}\n\nTable~\\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\\ref{fig:attention_profile}, main text).\nThe full profile (Figure~\\ref{fig:multilayer_attention}) reveals three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_multi_layer_attn.pdf}\n\\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}\n\\label{fig:multilayer_attention}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\\ref{tab:routing_gradient}) due to threshold boundary effects.}\n\\label{tab:multilayer_attention}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{VLA Trained} & \\multicolumn{2}{c}{Llama-2 base} & \\multicolumn{2}{c}{Untrained} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\nLayer & Heads & Text\\% & Heads & Text\\% & Heads & Text\\% \\\\\n\\midrule\nL1 & \\textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\\\\nL8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\\\\nL16 & 10/32 & 48.4 & \\textbf{25/32} & 60.2 & 0/32 & 9.2 \\\\\nL31 & \\textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Threshold Sensitivity Analysis}\n\\label{sec:threshold_sensitivity}\n\nThe main text defines instruction-dominant heads as those allocating $>50\\%$ attention to instruction tokens.\nTable~\\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\\% to 70\\%; the 50\\% threshold is not a boundary-sensitive choice.\n\n\\begin{table}[h]\n\\centering\n\\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}\n\\label{tab:threshold_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nThreshold & VLA Trained & Llama-2 base & Untrained \\\\\n\\midrule\n30\\% & 32 & 13 & 0 \\\\\n40\\% & 31 & 10 & 0 \\\\\n50\\% & 24 & 9 & 0 \\\\\n60\\% & 9 & 4 & 0 \\\\\n70\\% & 5 & 3 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{L1 Attention Decomposition by Head Group}\n\\label{sec:attention_decomp}\n\nTable~\\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.\n\n\\begin{table}[h]\n\\centering\n\\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}\n\\label{tab:attention_decomp}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nHead Group & $N$ & Instruction & Vision & BOS/Other \\\\\n\\midrule\nInstruction-dominant & 24 & 62.4\\% & 18.8\\% & 18.8\\% \\\\\nControl & 8 & 44.9\\% & 27.1\\% & 28.0\\% \\\\\n\\midrule\n$\\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHead-level instruction attention entropy reaches $99.5\\%$ of the uniform maximum; routing is broadly distributed rather than concentrated in a few heads.\n\n\\paragraph{Per-token attention normalization.}\nThe $57.7\\%$ aggregate text attention in instruction-dominant heads partly reflects token-count imbalance (22 instruction vs.\\ 256 image tokens).\nPer-token normalization reveals a $38.2\\times$ ratio: each instruction token receives $38.2\\times$ the attention of each image token in trained instruction-dominant heads, compared to only $1.5\\times$ in untrained heads (a $25.5\\times$ increase from training).\nInstruction-dominant heads also show lower attention entropy ($0.465$) than non-dominant heads ($0.569$), indicating more concentrated attention distributions.\n\n\\subsection{Per-Dimension Action MAE Under Head Ablation}\n\\label{sec:per_dim_mae}\n\nTable~\\ref{tab:per_dim_mae} extends Table~\\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\\times$); instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\\times$) falls between the two groups.}\n\\label{tab:per_dim_mae}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDimension & Instr.\\ 24h MAE & Control 8h MAE & Ratio \\\\\n\\midrule\n$dx$ & 0.00189 & 0.00037 & 5.09$\\times$ \\\\\n$dy$ & 0.00531 & 0.00125 & 4.26$\\times$ \\\\\n$dz$ & 0.00762 & 0.00243 & 3.14$\\times$ \\\\\n$roll$ & 0.02059 & 0.00785 & 2.62$\\times$ \\\\\n$pitch$ & 0.03071 & 0.01387 & 2.21$\\times$ \\\\\n$yaw$ & 0.03388 & 0.01783 & 1.90$\\times$ \\\\\n$gripper$ & 0.29072 & 0.14072 & 2.07$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}\n\\label{sec:per_task_r2}\n\nTable~\\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\\Delta > 0$): instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\\Delta R^2 = +0.107$; the 50-demo setting (\\S\\ref{sec:learned_routing}) yields a consistent $+0.059$.}\n\\label{tab:per_task_r2}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTask & Baseline $R^2$ & Ablated $R^2$ & $\\Delta R^2$ \\\\\n\\midrule\nopen middle drawer & 0.197 & 0.221 & $+$0.024 \\\\\nopen top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\\\\npush plate to stove & 0.190 & 0.197 & $+$0.007 \\\\\nput bowl on plate & 0.375 & 0.474 & $+$0.099 \\\\\nput bowl on stove & 0.235 & 0.395 & $+$0.160 \\\\\nput bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\\\\nput cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\\\\nput wine on rack & 0.189 & 0.424 & $+$0.235 \\\\\nput wine on cabinet & 0.279 & 0.353 & $+$0.074 \\\\\nturn on stove & 0.385 & 0.421 & $+$0.036 \\\\\n\\midrule\nMean $\\pm$ std & $0.256 \\pm 0.070$ & $0.363 \\pm 0.088$ & $+$0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Task Complexity and Routing Dependence}\n\\label{sec:task_complexity}\n\nWe classify tasks as \\emph{instruction-discriminative} when multiple tasks share the same manipulated object(s), requiring instruction content to disambiguate the target action (e.g., ``put bowl on plate'' vs.\\ ``put bowl on stove''); remaining tasks involve unique object-action pairings recoverable from visual context alone.\nTable~\\ref{tab:task_complexity} reports per-task $|\\Delta R^2|$ under both groupings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Task-level L1 ablation effects ($|\\Delta R^2|$) grouped by instruction dependence. \\emph{Primary} (conservative): cream cheese in bowl classified as visual-sufficient ($2.5\\times$, $p = 0.033$). \\emph{Sensitivity} (shared-object criterion): cream cheese reclassified as instruction-discriminative ($6.5\\times$, $p = 0.008$).}\n\\label{tab:task_complexity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nTask & $|\\Delta R^2|$ & Group \\\\\n\\midrule\nput wine on rack & 0.235 & Instr-disc \\\\\nput bowl on cabinet & 0.201 & Instr-disc \\\\\nput bowl on stove & 0.160 & Instr-disc \\\\\nput bowl on plate & 0.099 & Instr-disc \\\\\nopen top drawer + bowl & 0.075 & Instr-disc \\\\\nput wine on cabinet & 0.074 & Instr-disc \\\\\n\\midrule\nput cream cheese in bowl$^\\dagger$ & 0.159 & Vis-suff \\\\\nturn on stove & 0.036 & Vis-suff \\\\\nopen middle drawer & 0.024 & Vis-suff \\\\\npush plate to stove & 0.007 & Vis-suff \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Primary}: Instr-disc mean $0.141$; Vis-suff mean $0.057$} \\\\\n\\multicolumn{3}{l}{Mann-Whitney $U = 21.0$, $p = 0.033$, ratio $= 2.49\\times$} \\\\\n\\multicolumn{3}{l}{\\textbf{Sensitivity}$^\\dagger$: cream cheese as Instr-disc: $p = 0.008$, $6.5\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Leave-one-out sensitivity.}\nAll leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.\nReclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).\n\n\\subsection{Specificity Control: Matched-Size Head Ablation}\n\\label{sec:specificity_control}\n\nTo test whether ablation effects are specific to instruction-dominant heads, we ablate four matched-size subsets of 24 heads at L1: instruction-dominant (highest instruction attention fraction), image-dominant (highest image attention fraction), random (5 seeds), and bottom-24 (lowest instruction attention fraction; overlaps 16/24 heads with the instruction-dominant group).\n\n\\begin{table}[h]\n\\centering\n\\caption{Matched-size ablation controls: trajectory disruption ($d$) from ablating 24-head subsets at L1, ranked by instruction attention fraction. Instruction-dominant heads produce the largest effect, but the modest gap ($8\\%$ over random) indicates distributed, attention-graded routing rather than a dedicated subset.}\n\\label{tab:specificity_control}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition (24 heads) & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\nInstruction-dominant & 0.650 & (reference) \\\\\nRandom (5 seeds) & $0.601 \\pm 0.021$ & $[0.568, 0.622]$ \\\\\nImage-dominant & 0.580 & $[0.547, 0.613]$ \\\\\nBottom-24 & 0.565 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll conditions yield comparable ground-truth MSE ($0.487$--$0.504$ vs.\\ baseline $0.497$), consistent with direction-selective rather than precision-degrading effects.\n",
    "structuredPatch": [
      {
        "oldStart": 284,
        "oldLines": 7,
        "newStart": 284,
        "newLines": 7,
        "lines": [
          " \\subsection{Cross-Benchmark Validation: LIBERO-Spatial}",
          " \\label{sec:cross_benchmark_appendix}",
          " ",
          "-To assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks requiring spatial reasoning).",
          "+To assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks $\\times$ 50 demonstrations each, requiring spatial reasoning).",
          " Figure~\\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.",
          " ",
          " The inverted-U profile replicates on LIBERO-Spatial: trained image\\_mean RSA peaks at L14 ($\\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing."
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

_source line 77_

Now fix the QA Probe section with classifier architecture and labeling details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "cfcb2aa3-0337-4e0a-a2f9-2c333e819166",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BCEGCR15ifMMN3zWtUHzQi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 76469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 78_

<details open><summary>🔧 Tool call — Edit · `toolu_011BcUtrhTD4BuvNkYDq6aA6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "old_string": "To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\\ref{tab:qa_probe}).",
  "new_string": "To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train logistic regression probes (scikit-learn, $C = 1.0$, max\\_iter $= 1{,}000$) to classify task progress (4-class: each trajectory split into 4 equal temporal segments) and active subtask (binary: first vs.\\ second half) from frozen representations, with an 80/20 random train/test split (Table~\\ref{tab:qa_probe})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "12165d68-1262-435c-8ca5-16ffe1910231",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BCEGCR15ifMMN3zWtUHzQi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 76469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 79 · 2026-05-19T15:10:14.710Z_

<details><summary>↩ Tool result · `toolu_011BcUtrhTD4BuvNkYDq6aA6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "73d11aa9-86ae-4671-89f7-760c90bec904",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "oldString": "To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\\ref{tab:qa_probe}).",
    "newString": "To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train logistic regression probes (scikit-learn, $C = 1.0$, max\\_iter $= 1{,}000$) to classify task progress (4-class: each trajectory split into 4 equal temporal segments) and active subtask (binary: first vs.\\ second half) from frozen representations, with an 80/20 random train/test split (Table~\\ref{tab:qa_probe}).",
    "originalFile": "\\paragraph{Use of Generative AI.}\nGenerative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.\n\n\\appendix\n\n\\section{Supplementary Material}\n\\label{sec:appendix}\n\nUnless noted otherwise, all analyses use OpenVLA-7B (\\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).\nModel conditions, representation extraction, metric definitions, and probe architectures follow \\S\\ref{sec:setup}--\\S\\ref{sec:probes}.\nCross-benchmark experiments (\\S\\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\\times$ 50 demonstrations).\nAll experiments ran on 2$\\times$ NVIDIA RTX PRO 6000 Ada GPUs (48\\,GB each); random seed is 42 unless stated otherwise.\n\n\\subsection{CKA Analysis Method}\n\\label{sec:cka_appendix}\n\nWe employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA as a complementary perspective.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.\n\n\\subsection{Metric Sensitivity: RSA versus CKA}\n\\label{sec:metric_sensitivity_appendix}\n\nLinear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.\n\nAt the per-layer level, linear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), with no inverted-U pattern.\nRSA captures rank-order geometric alignment; CKA captures global linear structure.\nThe dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}\n\\label{fig:metric_comparison}\n\\end{figure}\n\n\\subsection{Branch-Split Detailed Analysis}\n\\label{sec:branch_split_appendix}\n\nTo disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.\nThe two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.\nFusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.\nThe MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.\n\n\\subsection{RSA Across Representation Sources}\n\\label{sec:rsa_bar_appendix}\n\nFigure~\\ref{fig:rsa_bar} shows RSA with the action space across all representation sources; the ordering matches Table~\\ref{tab:rsa_overview}.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n\\subsection{Per-Layer RSA Profiles}\n\\label{sec:rsa_perlayer_appendix}\n\nFigure~\\ref{fig:rsa_perlayer_curve} extends Figure~\\ref{fig:layer_curves} (main text) by adding readout and untrained profiles.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}\n\\caption{Per-layer RSA ($\\rho$) for trained and untrained models at image\\_mean and readout (last\\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\\_mean diverge: readout $\\rho$ declines gradually ($0.628 \\to 0.584$) while image\\_mean $\\rho$ drops sharply ($0.628 \\to 0.422$), consistent with task-specific conditioning at the readout position.}\n\\label{fig:rsa_perlayer_curve}\n\\end{figure}\n\n\\subsection{Per-Layer Action Decoding Across Training Stages}\n\\label{sec:action_r2_threecond}\n\nFigure~\\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\\pm$ std).\nAll three conditions share L0 representations ($R^2 = 0.645 \\pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.\nThe trained model peaks at L9 ($R^2 = 0.643 \\pm 0.014$), consistent with progressive specialization for action-relevant feature integration.\nLlama-2 base shows a steady decline (L0: $0.645 \\to$ L32: $0.551$, std $0.003$--$0.035$), consistent with stable but unspecialized processing.\nThe untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability indicates that randomly initialized Transformer layers produce destructive interference on action-relevant structure.\nThe three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.\nThe qualitative pattern is consistent across all 3 seeds.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_action_r2_threecond.pdf}\n\\caption{Per-layer action probe $R^2$ (image\\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \\pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\\pm$ std).}\n\\label{fig:action_r2_threecond}\n\\end{figure}\n\n\\subsection{Random-Subset Ablation Details}\n\\label{sec:random_subset_ablation}\n\nTo evaluate whether the ablation effect in \\S\\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).\nDominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \\pm 0.013$ (Figure~\\ref{fig:random_subset_ablation}).\nThe dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); heads with higher instruction-attention fraction carry more organized routing signals, consistent with graded rather than binary specialization.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_random_subset_ablation.pdf}\n\\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \\pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with graded routing specialization across L1 heads.}\n\\label{fig:random_subset_ablation}\n\\end{figure}\n\n\\subsection{Action Trajectory Analysis Details}\n\\label{sec:action_trajectory}\n\nTable~\\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.\nBoth conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).\nThe gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.\n\nPer-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).\nToken-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.\n\n\\paragraph{Trajectory-level aggregation.}\nAggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\\sim}4\\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).\nInstruction-head ablation ($N = 50$: 5 tasks $\\times$ 10 demos) yields trajectory $d = 2.943$ (95\\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).\nAll 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.\nCounterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).\nFine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\\sim} 1{,}500$) provide higher resolution for ordering claims.\n\n\\paragraph{Ground-truth action error.}\nAblation redirects model outputs ($d = 0.65$) but does not systematically increase error relative to expert demonstrations: original MSE $= 0.498$; top-24 instruction-head ablation MSE $= 0.497$ ($\\Delta = -0.001$, Wilcoxon $p = 0.52$, n.s.); bottom-24 non-instruction heads MSE $= 0.506$ ($\\Delta = +0.008$).\nChanges concentrate on the gripper dimension; translation and rotation dimensions are negligibly affected.\nPer-task breakdown shows all $|\\Delta\\text{MSE}| < 3\\%$ of baseline with all $p > 0.27$; the near-zero aggregate $\\Delta$ reflects uniformly small per-task effects rather than cancellation across tasks.\nThis is consistent with the information-computation dissociation: routing heads control instruction-specific direction selection rather than action precision.\n\nTable~\\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).\nIndividual control heads produce ${\\sim}1.9\\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.\nThe 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\\ $0.41$), consistent with collective coordination rather than individual strength.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}\n\\label{tab:perhead_bootstrap}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nGroup & $N$ heads & Collective $d$ & Per-head $d$ [95\\% CI] \\\\\n\\midrule\nInstruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\\\\nControl & 8 & 0.41 & 0.051 [0.048, 0.055] \\\\\n\\midrule\nDifference & --- & --- & 0.024, $p = 0.0018$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInstruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.\n\nTable~\\ref{tab:dose_response} and Figure~\\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.\nTrajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\\Delta d / \\Delta 4 \\approx 0.026$), a plateau at 16--20 heads ($\\Delta d = 0.001$), and slow increase at 20--32.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\\ original action sequence; 95\\% bootstrap CIs ($10{,}000$ resamples).}\n\\label{tab:dose_response}\n\\small\n\\begin{tabular}{rcc}\n\\toprule\nHeads ablated & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\n4 & 0.482 & [0.449, 0.511] \\\\\n8 & 0.508 & [0.479, 0.541] \\\\\n12 & 0.560 & [0.529, 0.593] \\\\\n16 & 0.592 & [0.559, 0.625] \\\\\n20 & 0.593 & [0.559, 0.627] \\\\\n24 & 0.611 & [0.578, 0.645] \\\\\n28 & 0.619 & [0.587, 0.654] \\\\\n32 & 0.639 & [0.603, 0.671] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$, token divergence (\\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \\text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}\n\\label{tab:counterfactual}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Jaccard & Cohen's $d$ & Token div.\\ (\\%) \\\\\n\\midrule\nEmpty (no instruction) & 0.000 & 0.968 & 90.7 \\\\\nWrong (different task) & 0.174 & 0.844 & 89.5 \\\\\nParaphrased & 0.533 & 0.697 & 82.6 \\\\\nShuffled (random order) & 1.000 & 0.625 & 85.7 \\\\\n\\midrule\nL1 ablation (24 heads) & --- & 0.650 & 72.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}\n\\label{tab:action_shift_perdim}\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\nCondition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\\\\n\\midrule\nInstruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\\\\nControl (8) & 0.000 & 0.001 & 0.002 & 0.008 & 0.014 & 0.018 & 0.141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pretrained LLM Representation Quality Under Visual Input}\n\\label{sec:ood_diagnostics}\n\nA potential concern with the three-condition comparison (\\S\\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.\nWe evaluate three diagnostics to assess representation quality.\nActivation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \\to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.\nPer-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\\approx 0.28$ at L25, consistent with gradual differentiation rather than catastrophic out-of-distribution behavior.\nTop-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.\nThese diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining (Figure~\\ref{fig:ood_diagnostics}). These results support the validity of the three-condition comparison.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ood_diagnostics.pdf}\n\\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics indicate structured, non-degenerate representations.}\n\\label{fig:ood_diagnostics}\n\\end{figure}\n\n\\subsection{Probe Architecture Sensitivity}\n\\label{sec:linear_probe}\n\nTo rule out that our findings depend on MLP probe capacity ($N/\\text{params} \\approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \\to 7$, $N/\\text{params} \\approx 2.2$).\nThe inverted-U pattern reproduces: trained image\\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).\nThe trained--untrained gap is larger under the linear probe (L14: $\\Delta = +0.324$) than the MLP probe (L8: $\\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.\nUntrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.\nFor last\\_preaction tokens, the linear probe also corroborates the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\\Delta = 0.103$ ($p < 0.001$).\nThese results indicate that our qualitative findings reflect representational structure rather than probe capacity artifacts (Figure~\\ref{fig:linear_vs_mlp}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}\n\\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}\n\\label{fig:linear_vs_mlp}\n\\end{figure}\n\n\\subsection{Functional Probe Comparison}\n\\label{sec:probe_bars_appendix}\n\nFigure~\\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\\_mean ($0.655$, L8) exceed the projector baseline ($0.630$); the inverted-U extends to functional capacity.}\n\\label{fig:probe_bars}\n\\end{figure}\n\n\\subsection{Training Effect and Instruction Invariance}\n\\label{sec:instruction_invariance_appendix}\n\nFigure~\\ref{fig:factorial} shows trained vs.\\ untrained RSA profiles and instruction invariance.\nInstruction invariance holds across all conditions: maximum $|\\Delta| < 0.006$, so action geometry is visually grounded and not modulated by language instructions.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\\Delta{=}+0.017$, $3\\%$). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$; action geometry is visually grounded.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Additional RSA Values}\n\\label{sec:additional_rsa}\n\nDINOv2 \\texttt{patch\\_mean} achieves RSA $\\rho = 0.631$, between the \\texttt{cls\\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).\nVLA untrained readout peaks at L1 ($\\rho = 0.626$).\n\n\\subsection{Cross-Benchmark Validation: LIBERO-Spatial}\n\\label{sec:cross_benchmark_appendix}\n\nTo assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks $\\times$ 50 demonstrations each, requiring spatial reasoning).\nFigure~\\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.\n\nThe inverted-U profile replicates on LIBERO-Spatial: trained image\\_mean RSA peaks at L14 ($\\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.\nTraining produces a significant geometric gain (best-vs-best $\\Delta = +0.023$, 95\\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\\Delta = +0.017$, CI includes zero).\n\nTwo notable differences emerge.\nFirst, the absolute RSA values are higher on Spatial ($0.691$ vs.\\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.\nSecond, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\\Delta_\\text{layer}| = 1$).\nThis suggests that peak convergence is benchmark-specific rather than a general consequence of training.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig7.pdf}\n\\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}\n\\label{fig:cross_benchmark}\n\\end{figure}\n\n\\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}\n\\label{sec:spatial_cross_instruction}\n\nTable~\\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.\nThe core pattern from LIBERO-Goal replicates: image\\_mean remains at chance (${\\sim}10\\%$) across all layers and conditions, while the trained readout token saturates to $100\\%$ by L4.\nThe untrained readout decays more steeply than on LIBERO-Goal ($75.4\\%$ at L31 vs.\\ $82\\%$), consistent with greater task difficulty.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\\%$ from L4; image\\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\\ Table~\\ref{tab:dense_routing_main}).}\n\\label{tab:spatial_cross_instruction}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nToken & Condition & L1 & L4 & L8 & L16 & L31 \\\\\n\\midrule\nlast\\_preaction & Trained & 98.9\\% & 100.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\nlast\\_preaction & Untrained & 99.5\\% & 98.3\\% & 85.7\\% & 68.3\\% & 75.4\\% \\\\\nimage\\_mean & Trained & 10.2\\% & 10.0\\% & 9.9\\% & 10.0\\% & 10.1\\% \\\\\nimage\\_mean & Untrained & 10.1\\% & 10.0\\% & 10.0\\% & 10.0\\% & 10.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness Analyses}\n\\label{sec:robustness_appendix}\n\n\\subsubsection{Distance Metric Invariance}\n\\label{sec:metric_invariance}\n\nThe inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\\ref{tab:metric_invariance}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}\n\\label{tab:metric_invariance}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Eucl.\\ Peak & Cos.\\ Peak & Profile $r$ \\\\\n\\midrule\nTrained image\\_mean & L12 & L12 & 0.990 \\\\\nTrained last\\_preaction & L12 & L13 & 0.990 \\\\\nUntrained image\\_mean & L0 & L0 & 0.995 \\\\\nUntrained last\\_preaction & L1 & L1 & 0.992 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Per-DOF Decomposition}\n\\label{sec:perdof}\n\nRSA decomposition by action dimension indicates the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\\rho = 0.193$), rotation (peak L12, $\\rho = 0.175$), and gripper (peak L13, $\\rho = 0.106$) all exhibit non-monotonic profiles.\nPer-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.\n\n\\subsubsection{Permutation Test}\n\\label{sec:permutation}\n\nPermutation testing (1{,}000 shuffles) indicates all observed RSA values are highly significant: observed $\\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).\n\n\\subsubsection{Probe Seed Sensitivity}\n\\label{sec:seed_sensitivity}\n\nAction probe $R^2$ is highly stable across random seeds.\nOver 5 seeds (trained image\\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\\%$ ($0.655 \\pm 0.002$; Table~\\ref{tab:seed_sensitivity}).\nPeak layer concentrates in the L8--L10 region ($4/5$ seeds); the inverted-U shape is not a seed artifact.\nSeed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe $R^2$ peak across 5 random seeds (trained image\\_mean).}\n\\label{tab:seed_sensitivity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSeed & Peak Layer & Peak $R^2$ \\\\\n\\midrule\n0 & L9 & 0.654 \\\\\n1 & L16 & 0.656 \\\\\n2 & L9 & 0.653 \\\\\n3 & L10 & 0.655 \\\\\n42 & L9 & 0.655 \\\\\n\\midrule\nMean$\\pm$std & $10.6\\pm2.7$ & $0.655\\pm0.002$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Demonstration Subsample Sensitivity}\n\\label{sec:demo_sensitivity}\n\nTo verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\\ref{tab:demo_sensitivity}).\nThe RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions (high stability).\nThe probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$; $R^2$ is more sensitive to training set size than RSA.\nBoth metrics show reduced absolute values (RSA $-3.6\\%$, $R^2$ $-7.6\\%$) as expected from halved data, but the non-monotonic profile shape is preserved.\n\n\\begin{table}[h]\n\\centering\n\\caption{Inverted-U stability under demonstration subsampling (trained image\\_mean).}\n\\label{tab:demo_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 50 demos & 25 demos & $\\Delta$ \\\\\n\\midrule\nRSA peak layer & L12 & L12 & 0 \\\\\nRSA peak $\\rho$ & 0.628 & 0.606 & $-3.6\\%$ \\\\\n$R^2$ peak layer & L9 & L11 & $+2$ \\\\\n$R^2$ peak value & 0.659 & 0.609 & $-7.6\\%$ \\\\\nRSA profile $r$ & --- & 0.970 & --- \\\\\n$R^2$ profile $r$ & --- & 0.819 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detailed Training Effects}\n\\label{sec:training_effects_appendix}\n\nTable~\\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\\Delta{=}+0.017$, $3\\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{RSA ($\\rho$)}} \\\\\nBest-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\\n\\quad (trained L12 vs.\\ untrained L0) & & & \\\\\nSame-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained vs.\\ untrained) & & & \\\\\nInstruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Probe $R^2$}} \\\\\nBest-vs-best image\\_mean & $+$0.015 & excl.\\ 0 & 0.006 \\\\\n\\quad (trained L8 vs.\\ untrained L0) & & & \\\\\nBest-vs-best readout & $+$0.069 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained L13 vs.\\ untrained L32) & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Training Effect Size Summary}\n\\label{sec:training_effect_summary}\n\nTable~\\ref{tab:training_effect_summary} consolidates training effects across all metrics.\nTraining effects on image\\_mean metrics are modest (RSA $\\Delta = +0.017$, $R^2$ $\\Delta = +0.015$), but effects on last\\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\\Delta = +0.069$).\nThis asymmetry indicates that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effect sizes across metrics. Image\\_mean effects are modest; last\\_preaction effects are large. Training targets readout-token information integration.}\n\\label{tab:training_effect_summary}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Trained & Untrained & $\\Delta$ \\\\\n\\midrule\nRSA peak (image\\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\\\\n$R^2$ peak (image\\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\\\\n$R^2$ peak (last\\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\\\\nInstruction routing L31 & 100\\% & 82\\% & $+$18pp \\\\\nInstruction attention L1 & 58\\% & 12\\% & $+$46pp \\\\\nProgress classification & 86.3\\% (L20) & 85.3\\% (L4) & $+$1pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Instruction Routing Probes}\n\\label{sec:routing_appendix}\n\n\\subsubsection{Cross-Instruction Classification: Dense Layer Profile}\n\\label{sec:dense_routing}\n\nTable~\\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.\nThe step-function onset between L0 ($10\\%$, chance) and L1 (${\\geq}99.6\\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\\sim}12\\%$) suffices for linear classification at L1.\nBoth pretrained and VLA-trained models sustain $100\\%$ through L31; only random initialization shows progressive decay ($82\\%$ at L31). Deep-layer stability thus derives from structured pretrained weights rather than task-specific fine-tuning.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8. Values reflect dense routing evaluation; main-text Table~\\ref{tab:dense_routing_main} reports sparse single-split results, yielding minor differences (e.g., L8: $98.2\\%$ vs.\\ $98.6\\%$).}\n\\label{tab:dense_routing}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained & Untrained & Image\\_mean (trained) \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL2 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL3 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL5 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL6 & 100.0\\% & 97.3\\% & 10.0\\% \\\\\nL7 & 100.0\\% & 96.4\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.6\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction LOOCV Validation}\n\\label{sec:loocv}\n\nLeave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) validates that the cross-instruction probe result is not driven by memorization.\nTrained last\\_preaction achieves $100\\% \\pm 0.00$ across all 10 folds at layers L1--L31 (perfect generalization).\n\n\\subsubsection{QA Probe: Progress and Subtask Classification}\n\\label{sec:qa_probe}\n\nTo test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\\ref{tab:qa_probe}).\n\n\\begin{table}[h]\n\\centering\n\\caption{QA probe accuracy (progress + subtask classification, best layer).}\n\\label{tab:qa_probe}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSource & Best Layer & Accuracy \\\\\n\\midrule\nTrained last\\_preaction & L20 & 86.3\\% \\\\\nUntrained last\\_preaction & L20 & 85.3\\% \\\\\nDINOv2 cls\\_token & --- & 82.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction Probe Profiles}\n\\label{sec:probe_profiles}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_probe_conditions.pdf}\n\\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\\%$ at L1, saturating to $100\\%$. Llama-2 base starts at $80.2\\%$, reaching $100\\%$ by L5. Untrained starts at $100\\%$ but decays to $82\\%$ by L31.}\n\\label{fig:probe_conditions_appendix}\n\\end{figure}\n\n\\subsubsection{Four-Condition Cross-Instruction Probe Profile}\n\\label{app:finetuned_probe}\n\nTable~\\ref{tab:finetuned_probe} extends the three-condition probe comparison (Table~\\ref{tab:dense_routing_main}) with the LIBERO-finetuned checkpoint.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy across four training conditions. Task-specific fine-tuning (LIBERO) preserves instruction decodability at all layers despite eliminating L31 exit-layer attention engagement (18$\\to$0 instruction-dominant heads).}\n\\label{tab:finetuned_probe}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & Untrained & Llama-2 base & OpenVLA-7B & LIBERO-finetuned \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 80.2\\% & 99.6\\% & 99.7\\% \\\\\nL8 & 98.6\\% & 99.9\\% & 100.0\\% & 100.0\\% \\\\\nL31 & 82.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{L1 Attention Pattern Analysis}\n\\label{sec:attention_pattern}\n\nFigure~\\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.\nThe three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_l1_stacked_bar.pdf}\n\\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\\%$ text attention). Llama-2 base: 9/32 heads ($36.5\\%$). Untrained: 0/32 heads ($11.7\\%$). See Table~\\ref{tab:routing_gradient} for quantitative comparison.}\n\\label{fig:attention_appendix}\n\\end{figure}\n\n\\subsubsection{Multi-Layer Attention Patterns}\n\\label{sec:multilayer_attention}\n\nTable~\\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\\ref{fig:attention_profile}, main text).\nThe full profile (Figure~\\ref{fig:multilayer_attention}) reveals three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_multi_layer_attn.pdf}\n\\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}\n\\label{fig:multilayer_attention}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\\ref{tab:routing_gradient}) due to threshold boundary effects.}\n\\label{tab:multilayer_attention}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{VLA Trained} & \\multicolumn{2}{c}{Llama-2 base} & \\multicolumn{2}{c}{Untrained} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\nLayer & Heads & Text\\% & Heads & Text\\% & Heads & Text\\% \\\\\n\\midrule\nL1 & \\textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\\\\nL8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\\\\nL16 & 10/32 & 48.4 & \\textbf{25/32} & 60.2 & 0/32 & 9.2 \\\\\nL31 & \\textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Threshold Sensitivity Analysis}\n\\label{sec:threshold_sensitivity}\n\nThe main text defines instruction-dominant heads as those allocating $>50\\%$ attention to instruction tokens.\nTable~\\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\\% to 70\\%; the 50\\% threshold is not a boundary-sensitive choice.\n\n\\begin{table}[h]\n\\centering\n\\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}\n\\label{tab:threshold_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nThreshold & VLA Trained & Llama-2 base & Untrained \\\\\n\\midrule\n30\\% & 32 & 13 & 0 \\\\\n40\\% & 31 & 10 & 0 \\\\\n50\\% & 24 & 9 & 0 \\\\\n60\\% & 9 & 4 & 0 \\\\\n70\\% & 5 & 3 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{L1 Attention Decomposition by Head Group}\n\\label{sec:attention_decomp}\n\nTable~\\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.\n\n\\begin{table}[h]\n\\centering\n\\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}\n\\label{tab:attention_decomp}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nHead Group & $N$ & Instruction & Vision & BOS/Other \\\\\n\\midrule\nInstruction-dominant & 24 & 62.4\\% & 18.8\\% & 18.8\\% \\\\\nControl & 8 & 44.9\\% & 27.1\\% & 28.0\\% \\\\\n\\midrule\n$\\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHead-level instruction attention entropy reaches $99.5\\%$ of the uniform maximum; routing is broadly distributed rather than concentrated in a few heads.\n\n\\paragraph{Per-token attention normalization.}\nThe $57.7\\%$ aggregate text attention in instruction-dominant heads partly reflects token-count imbalance (22 instruction vs.\\ 256 image tokens).\nPer-token normalization reveals a $38.2\\times$ ratio: each instruction token receives $38.2\\times$ the attention of each image token in trained instruction-dominant heads, compared to only $1.5\\times$ in untrained heads (a $25.5\\times$ increase from training).\nInstruction-dominant heads also show lower attention entropy ($0.465$) than non-dominant heads ($0.569$), indicating more concentrated attention distributions.\n\n\\subsection{Per-Dimension Action MAE Under Head Ablation}\n\\label{sec:per_dim_mae}\n\nTable~\\ref{tab:per_dim_mae} extends Table~\\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\\times$); instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\\times$) falls between the two groups.}\n\\label{tab:per_dim_mae}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDimension & Instr.\\ 24h MAE & Control 8h MAE & Ratio \\\\\n\\midrule\n$dx$ & 0.00189 & 0.00037 & 5.09$\\times$ \\\\\n$dy$ & 0.00531 & 0.00125 & 4.26$\\times$ \\\\\n$dz$ & 0.00762 & 0.00243 & 3.14$\\times$ \\\\\n$roll$ & 0.02059 & 0.00785 & 2.62$\\times$ \\\\\n$pitch$ & 0.03071 & 0.01387 & 2.21$\\times$ \\\\\n$yaw$ & 0.03388 & 0.01783 & 1.90$\\times$ \\\\\n$gripper$ & 0.29072 & 0.14072 & 2.07$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}\n\\label{sec:per_task_r2}\n\nTable~\\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\\Delta > 0$): instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\\Delta R^2 = +0.107$; the 50-demo setting (\\S\\ref{sec:learned_routing}) yields a consistent $+0.059$.}\n\\label{tab:per_task_r2}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTask & Baseline $R^2$ & Ablated $R^2$ & $\\Delta R^2$ \\\\\n\\midrule\nopen middle drawer & 0.197 & 0.221 & $+$0.024 \\\\\nopen top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\\\\npush plate to stove & 0.190 & 0.197 & $+$0.007 \\\\\nput bowl on plate & 0.375 & 0.474 & $+$0.099 \\\\\nput bowl on stove & 0.235 & 0.395 & $+$0.160 \\\\\nput bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\\\\nput cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\\\\nput wine on rack & 0.189 & 0.424 & $+$0.235 \\\\\nput wine on cabinet & 0.279 & 0.353 & $+$0.074 \\\\\nturn on stove & 0.385 & 0.421 & $+$0.036 \\\\\n\\midrule\nMean $\\pm$ std & $0.256 \\pm 0.070$ & $0.363 \\pm 0.088$ & $+$0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Task Complexity and Routing Dependence}\n\\label{sec:task_complexity}\n\nWe classify tasks as \\emph{instruction-discriminative} when multiple tasks share the same manipulated object(s), requiring instruction content to disambiguate the target action (e.g., ``put bowl on plate'' vs.\\ ``put bowl on stove''); remaining tasks involve unique object-action pairings recoverable from visual context alone.\nTable~\\ref{tab:task_complexity} reports per-task $|\\Delta R^2|$ under both groupings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Task-level L1 ablation effects ($|\\Delta R^2|$) grouped by instruction dependence. \\emph{Primary} (conservative): cream cheese in bowl classified as visual-sufficient ($2.5\\times$, $p = 0.033$). \\emph{Sensitivity} (shared-object criterion): cream cheese reclassified as instruction-discriminative ($6.5\\times$, $p = 0.008$).}\n\\label{tab:task_complexity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nTask & $|\\Delta R^2|$ & Group \\\\\n\\midrule\nput wine on rack & 0.235 & Instr-disc \\\\\nput bowl on cabinet & 0.201 & Instr-disc \\\\\nput bowl on stove & 0.160 & Instr-disc \\\\\nput bowl on plate & 0.099 & Instr-disc \\\\\nopen top drawer + bowl & 0.075 & Instr-disc \\\\\nput wine on cabinet & 0.074 & Instr-disc \\\\\n\\midrule\nput cream cheese in bowl$^\\dagger$ & 0.159 & Vis-suff \\\\\nturn on stove & 0.036 & Vis-suff \\\\\nopen middle drawer & 0.024 & Vis-suff \\\\\npush plate to stove & 0.007 & Vis-suff \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Primary}: Instr-disc mean $0.141$; Vis-suff mean $0.057$} \\\\\n\\multicolumn{3}{l}{Mann-Whitney $U = 21.0$, $p = 0.033$, ratio $= 2.49\\times$} \\\\\n\\multicolumn{3}{l}{\\textbf{Sensitivity}$^\\dagger$: cream cheese as Instr-disc: $p = 0.008$, $6.5\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Leave-one-out sensitivity.}\nAll leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.\nReclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).\n\n\\subsection{Specificity Control: Matched-Size Head Ablation}\n\\label{sec:specificity_control}\n\nTo test whether ablation effects are specific to instruction-dominant heads, we ablate four matched-size subsets of 24 heads at L1: instruction-dominant (highest instruction attention fraction), image-dominant (highest image attention fraction), random (5 seeds), and bottom-24 (lowest instruction attention fraction; overlaps 16/24 heads with the instruction-dominant group).\n\n\\begin{table}[h]\n\\centering\n\\caption{Matched-size ablation controls: trajectory disruption ($d$) from ablating 24-head subsets at L1, ranked by instruction attention fraction. Instruction-dominant heads produce the largest effect, but the modest gap ($8\\%$ over random) indicates distributed, attention-graded routing rather than a dedicated subset.}\n\\label{tab:specificity_control}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition (24 heads) & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\nInstruction-dominant & 0.650 & (reference) \\\\\nRandom (5 seeds) & $0.601 \\pm 0.021$ & $[0.568, 0.622]$ \\\\\nImage-dominant & 0.580 & $[0.547, 0.613]$ \\\\\nBottom-24 & 0.565 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll conditions yield comparable ground-truth MSE ($0.487$--$0.504$ vs.\\ baseline $0.497$), consistent with direction-selective rather than precision-degrading effects.\n",
    "structuredPatch": [
      {
        "oldStart": 514,
        "oldLines": 7,
        "newStart": 514,
        "newLines": 7,
        "lines": [
          " \\subsubsection{QA Probe: Progress and Subtask Classification}",
          " \\label{sec:qa_probe}",
          " ",
          "-To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\\ref{tab:qa_probe}).",
          "+To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train logistic regression probes (scikit-learn, $C = 1.0$, max\\_iter $= 1{,}000$) to classify task progress (4-class: each trajectory split into 4 equal temporal segments) and active subtask (binary: first vs.\\ second half) from frozen representations, with an 80/20 random train/test split (Table~\\ref{tab:qa_probe}).",
          " ",
          " \\begin{table}[h]",
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

_source line 80_

Now compile to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "44a4f5fe-1f29-4d84-9b01-587f158db628",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkAo4yz6mCz2h3VyokBQ3n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 483,
      "cache_read_input_tokens": 76734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 483
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

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_018wyWi99yXowvwcbW1abjjy`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && latexmk -pdf main.tex 2>&1 | tail -20",
  "description": "Compile LaTeX to verify no errors",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "c71dfedd-5a90-40bf-ba4e-033501053969",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkAo4yz6mCz2h3VyokBQ3n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 483,
      "cache_read_input_tokens": 76734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 483
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

_source line 82 · 2026-05-19T15:10:20.910Z_

<details><summary>↩ Tool result · `toolu_018wyWi99yXowvwcbW1abjjy`</summary>

```text
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr
i8a.pfb>
Output written on main.pdf (27 pages, 565444 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "32f38d14-b59c-4526-8361-1a31bda441d4",
  "tool_use_result": {
    "stdout": "0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr\ni8a.pfb>\nOutput written on main.pdf (27 pages, 565444 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 83_

<details><summary>Logged reasoning block</summary>

```text
Compilation successful, 0 errors, 27 pages (within the ≤ 28 constraint). 

Now let me verify the final state of the edits by reading the relevant sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "c0ec0448-23d0-4082-b001-62de389a3730",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7wpuBQq48WGgbYfed7b9X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 77217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 84_

Compilation: 0 errors, 27 pages. Let me verify the edits look correct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "4ccb536c-5aa4-43b0-9d3d-b40bc2249d56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7wpuBQq48WGgbYfed7b9X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 77217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 85_

<details open><summary>🔧 Tool call — Read · `toolu_01GMhQzyFHPWY1JbFWU3PGEv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": 6,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "938672b4-877c-4f39-86c1-a39ecbc08349",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7wpuBQq48WGgbYfed7b9X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 77217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 86 · 2026-05-19T15:10:25.107Z_

<details><summary>↩ Tool result · `toolu_01GMhQzyFHPWY1JbFWU3PGEv`</summary>

```text
6	\section{Supplementary Material}
7	\label{sec:appendix}
8	
9	Unless noted otherwise, all analyses use OpenVLA-7B (\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).
10	Model conditions, representation extraction, metric definitions, and probe architectures follow \S\ref{sec:setup}--\S\ref{sec:probes}.
11	Cross-benchmark experiments (\S\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\times$ 50 demonstrations).
12	All experiments ran on 2$\times$ NVIDIA RTX PRO 6000 Ada GPUs (48\,GB each); random seed is 42 unless stated otherwise.
13	
14	\subsection{CKA Analysis Method}
15	\label{sec:cka_appendix}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "37870283-4ff3-4b13-b417-ac6da5f8341a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
      "content": "\\section{Supplementary Material}\n\\label{sec:appendix}\n\nUnless noted otherwise, all analyses use OpenVLA-7B (\\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).\nModel conditions, representation extraction, metric definitions, and probe architectures follow \\S\\ref{sec:setup}--\\S\\ref{sec:probes}.\nCross-benchmark experiments (\\S\\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\\times$ 50 demonstrations).\nAll experiments ran on 2$\\times$ NVIDIA RTX PRO 6000 Ada GPUs (48\\,GB each); random seed is 42 unless stated otherwise.\n\n\\subsection{CKA Analysis Method}\n\\label{sec:cka_appendix}",
      "numLines": 10,
      "startLine": 6,
      "totalLines": 781
    }
  }
}
```

</details>

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Read · `toolu_01JU4UphjBGvJkigL9qCB8EG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": 286,
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
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "509bc0ff-30d3-434d-823d-43e56f45cf6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7wpuBQq48WGgbYfed7b9X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 77217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 88 · 2026-05-19T15:10:26.048Z_

<details><summary>↩ Tool result · `toolu_01JU4UphjBGvJkigL9qCB8EG`</summary>

```text
286	
287	To assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks $\times$ 50 demonstrations each, requiring spatial reasoning).
288	Figure~\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.
289	
290	The inverted-U profile replicates on LIBERO-Spatial: trained image\_mean RSA peaks at L14 ($\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "c0b86e23-4848-448d-b575-9e28509dfe26",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
      "content": "\nTo assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks $\\times$ 50 demonstrations each, requiring spatial reasoning).\nFigure~\\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.\n\nThe inverted-U profile replicates on LIBERO-Spatial: trained image\\_mean RSA peaks at L14 ($\\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.",
      "numLines": 5,
      "startLine": 286,
      "totalLines": 781
    }
  }
}
```

</details>

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Read · `toolu_01QjDBnxZNWusXcuB5kLYcwr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": 517,
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
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "ec2f4133-8cf3-4dd9-bb0b-8b4db7c0853e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7wpuBQq48WGgbYfed7b9X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 77217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 90 · 2026-05-19T15:10:26.642Z_

<details><summary>↩ Tool result · `toolu_01QjDBnxZNWusXcuB5kLYcwr`</summary>

```text
517	To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train logistic regression probes (scikit-learn, $C = 1.0$, max\_iter $= 1{,}000$) to classify task progress (4-class: each trajectory split into 4 equal temporal segments) and active subtask (binary: first vs.\ second half) from frozen representations, with an 80/20 random train/test split (Table~\ref{tab:qa_probe}).
518	
519	\begin{table}[h]
520	\centering
521	\caption{QA probe accuracy (progress + subtask classification, best layer).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "9cedc50d-23f9-4d2b-b2ed-04b3821d141e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
      "content": "To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train logistic regression probes (scikit-learn, $C = 1.0$, max\\_iter $= 1{,}000$) to classify task progress (4-class: each trajectory split into 4 equal temporal segments) and active subtask (binary: first vs.\\ second half) from frozen representations, with an 80/20 random train/test split (Table~\\ref{tab:qa_probe}).\n\n\\begin{table}[h]\n\\centering\n\\caption{QA probe accuracy (progress + subtask classification, best layer).}",
      "numLines": 5,
      "startLine": 517,
      "totalLines": 781
    }
  }
}
```

</details>

---

### Assistant

_source line 91_

All edits verified. Here's the audit report:

---

## Appendix Reproducibility Audit

### Per-Subsection Check (✓ present / ✗ missing / -- N/A)

| Subsection | Model | Dataset | Hyperparams | Metric Def | Hardware |
|---|---|---|---|---|---|
| CKA Analysis Method | ✓* | ✓* | -- | ✓ | ✓* |
| Metric Sensitivity: RSA vs CKA | ✓* | ✓* | -- | ✓ | ✓* |
| Branch-Split Detailed Analysis | ✓* | ✓* | -- | ✓ | ✓* |
| RSA Across Representation Sources | ✓* | ✓* | -- | ✓ | ✓* |
| Per-Layer RSA Profiles | ✓* | ✓* | -- | ✓ | ✓* |
| Per-Layer Action Decoding (3 cond) | ✓* | ✓ | ✓ (3 seeds, 50 demos) | ✓ | ✓* |
| Random-Subset Ablation | ✓* | ✓* | ✓ (10 subsets, 24/32) | ✓ | ✓* |
| Action Trajectory Analysis | ✓* | ✓ (5×10 demos, 3 tasks) | ✓ (10K bootstrap) | ✓ | ✓* |
| Pretrained LLM OOD Diagnostics | ✓* | ✓* | -- | ✓ | ✓* |
| Probe Architecture Sensitivity | ✓* | ✓* | ✓ (linear 4096→7) | ✓ | ✓* |
| Functional Probe Comparison | ✓* | ✓* | ✓* | ✓ | ✓* |
| Training Effect & Instr Invariance | ✓* | ✓* | -- | ✓ | ✓* |
| Additional RSA Values | ✓* | ✓* | -- | ✓ | ✓* |
| Cross-Benchmark: LIBERO-Spatial | ✓* | ✓ **fixed** | ✓* | ✓ | ✓* |
| Distance Metric Invariance | ✓* | ✓* | -- | ✓ | ✓* |
| Per-DOF Decomposition | ✓* | ✓* | -- | ✓ | ✓* |
| Permutation Test | ✓* | ✓* | ✓ (1K shuffles) | ✓ | ✓* |
| Probe Seed Sensitivity | ✓* | ✓* | ✓ (5 seeds) | ✓ | ✓* |
| Demo Subsample Sensitivity | ✓* | ✓ (25 vs 50) | -- | ✓ | ✓* |
| Detailed Training Effects | ✓* | ✓* | ✓ (10K bootstrap) | ✓ | ✓* |
| Training Effect Size Summary | ✓* | ✓* | -- | ✓ | ✓* |
| Cross-Instruction Dense Profile | ✓* | ✓* | ✓* | ✓ | ✓* |
| LOOCV Validation | ✓* | ✓* | ✓ (10 folds) | ✓ | ✓* |
| QA Probe | ✓* | ✓* | ✓ **fixed** | ✓ | ✓* |
| Probe Profiles | ✓* | ✓* | ✓* | ✓ | ✓* |
| Four-Condition Probe | ✓* | ✓* | ✓* | ✓ | ✓* |
| L1 Attention Pattern | ✓* | ✓* | -- | ✓ | ✓* |
| Multi-Layer Attention | ✓* | ✓* | -- | ✓ | ✓* |
| Threshold Sensitivity | ✓* | ✓* | -- | ✓ | ✓* |
| L1 Attention Decomposition | ✓* | ✓* | -- | ✓ | ✓* |
| Per-Dimension MAE | ✓* | ✓* | -- | ✓ | ✓* |
| Per-Task R² Distribution | ✓* | ✓ (5 demos/task) | ✓ (MLP) | ✓ | ✓* |
| Task Complexity & Routing | ✓* | ✓* | -- | ✓ (Mann-Whitney) | ✓* |
| Specificity Control | ✓* | ✓* | ✓ (5 seeds random) | ✓ | ✓* |

✓* = covered by the new shared setup paragraph referencing §3.1--§3.6

### Changes Made

| Location | Change |
|---|---|
| `appendix.tex:9-12` | Added shared setup paragraph: checkpoint source (`openvla/openvla-7b`), dataset (LIBERO-Goal, N=63,228), hardware (2× RTX PRO 6000 Ada, 48 GB), seed (42), cross-refs to §3.1--§3.6, LIBERO-Spatial protocol |
| `appendix.tex:287` | Added explicit sample count for LIBERO-Spatial: "10 out-of-distribution tasks × 50 demonstrations each" |
| `appendix.tex:517` | QA Probe: specified logistic regression (C=1.0, max_iter=1000), corrected labeling (4-class progress from equal temporal segments, binary subtask), added 80/20 split |

### Compilation
- 0 errors
- 27 pages (within ≤ 28 limit)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "uuid": "ef40a7c0-637c-40a1-bd2c-75b189a2c1d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReLedfvjNQqbD7xTUSbjyc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1109,
      "cache_read_input_tokens": 77821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1109
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

_source line 92_

All edits verified. Here's the audit report:

---

## Appendix Reproducibility Audit

### Per-Subsection Check (✓ present / ✗ missing / -- N/A)

| Subsection | Model | Dataset | Hyperparams | Metric Def | Hardware |
|---|---|---|---|---|---|
| CKA Analysis Method | ✓* | ✓* | -- | ✓ | ✓* |
| Metric Sensitivity: RSA vs CKA | ✓* | ✓* | -- | ✓ | ✓* |
| Branch-Split Detailed Analysis | ✓* | ✓* | -- | ✓ | ✓* |
| RSA Across Representation Sources | ✓* | ✓* | -- | ✓ | ✓* |
| Per-Layer RSA Profiles | ✓* | ✓* | -- | ✓ | ✓* |
| Per-Layer Action Decoding (3 cond) | ✓* | ✓ | ✓ (3 seeds, 50 demos) | ✓ | ✓* |
| Random-Subset Ablation | ✓* | ✓* | ✓ (10 subsets, 24/32) | ✓ | ✓* |
| Action Trajectory Analysis | ✓* | ✓ (5×10 demos, 3 tasks) | ✓ (10K bootstrap) | ✓ | ✓* |
| Pretrained LLM OOD Diagnostics | ✓* | ✓* | -- | ✓ | ✓* |
| Probe Architecture Sensitivity | ✓* | ✓* | ✓ (linear 4096→7) | ✓ | ✓* |
| Functional Probe Comparison | ✓* | ✓* | ✓* | ✓ | ✓* |
| Training Effect & Instr Invariance | ✓* | ✓* | -- | ✓ | ✓* |
| Additional RSA Values | ✓* | ✓* | -- | ✓ | ✓* |
| Cross-Benchmark: LIBERO-Spatial | ✓* | ✓ **fixed** | ✓* | ✓ | ✓* |
| Distance Metric Invariance | ✓* | ✓* | -- | ✓ | ✓* |
| Per-DOF Decomposition | ✓* | ✓* | -- | ✓ | ✓* |
| Permutation Test | ✓* | ✓* | ✓ (1K shuffles) | ✓ | ✓* |
| Probe Seed Sensitivity | ✓* | ✓* | ✓ (5 seeds) | ✓ | ✓* |
| Demo Subsample Sensitivity | ✓* | ✓ (25 vs 50) | -- | ✓ | ✓* |
| Detailed Training Effects | ✓* | ✓* | ✓ (10K bootstrap) | ✓ | ✓* |
| Training Effect Size Summary | ✓* | ✓* | -- | ✓ | ✓* |
| Cross-Instruction Dense Profile | ✓* | ✓* | ✓* | ✓ | ✓* |
| LOOCV Validation | ✓* | ✓* | ✓ (10 folds) | ✓ | ✓* |
| QA Probe | ✓* | ✓* | ✓ **fixed** | ✓ | ✓* |
| Probe Profiles | ✓* | ✓* | ✓* | ✓ | ✓* |
| Four-Condition Probe | ✓* | ✓* | ✓* | ✓ | ✓* |
| L1 Attention Pattern | ✓* | ✓* | -- | ✓ | ✓* |
| Multi-Layer Attention | ✓* | ✓* | -- | ✓ | ✓* |
| Threshold Sensitivity | ✓* | ✓* | -- | ✓ | ✓* |
| L1 Attention Decomposition | ✓* | ✓* | -- | ✓ | ✓* |
| Per-Dimension MAE | ✓* | ✓* | -- | ✓ | ✓* |
| Per-Task R² Distribution | ✓* | ✓ (5 demos/task) | ✓ (MLP) | ✓ | ✓* |
| Task Complexity & Routing | ✓* | ✓* | -- | ✓ (Mann-Whitney) | ✓* |
| Specificity Control | ✓* | ✓* | ✓ (5 seeds random) | ✓ | ✓* |

✓* = covered by the new shared setup paragraph referencing §3.1--§3.6

### Changes Made

| Location | Change |
|---|---|
| `appendix.tex:9-12` | Added shared setup paragraph: checkpoint source (`openvla/openvla-7b`), dataset (LIBERO-Goal, N=63,228), hardware (2× RTX PRO 6000 Ada, 48 GB), seed (42), cross-refs to §3.1--§3.6, LIBERO-Spatial protocol |
| `appendix.tex:287` | Added explicit sample count for LIBERO-Spatial: "10 out-of-distribution tasks × 50 demonstrations each" |
| `appendix.tex:517` | QA Probe: specified logistic regression (C=1.0, max_iter=1000), corrected labeling (4-class progress from equal temporal segments, binary subtask), added 80/20 split |

### Compilation
- 0 errors
- 27 pages (within ≤ 28 limit)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 368418,
  "duration_api_ms": 366610,
  "num_turns": 31,
  "stop_reason": "end_turn",
  "session_id": "c7f8ee1c-2669-4287-a396-fbc9a7afe088",
  "total_cost_usd": 1.5889561000000005,
  "usage": {
    "input_tokens": 26,
    "cache_creation_input_tokens": 67611,
    "cache_read_input_tokens": 1294893,
    "output_tokens": 18906,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 67611,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1553,
        "cache_read_input_tokens": 77821,
        "cache_creation_input_tokens": 1109,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1109
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1715,
      "outputTokens": 1761,
      "cacheReadInputTokens": 19396,
      "cacheCreationInputTokens": 26961,
      "webSearchRequests": 0,
      "costUSD": 0.04616085,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 26,
      "outputTokens": 18906,
      "cacheReadInputTokens": 1294893,
      "cacheCreationInputTokens": 67611,
      "webSearchRequests": 0,
      "costUSD": 1.5427952500000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9fe5fed9-dd82-4fce-9ccb-14879f32c1a4"
}
```

</details>

---
