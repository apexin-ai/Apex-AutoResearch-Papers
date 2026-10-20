# paper abstract threestage and bootstrap appendix

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_abstract_threestage_and_bootstrap_appendix_20260519T155518.log`
- **Structured JSON:** [`9200e8a5425f63aeb0ad.json`](../../sessions/92/9200e8a5425f63aeb0ad.json)

## Before a recorded user message

31 recorded events

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
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
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
  "uuid": "5e55948e-965c-46f3-986e-dcf803e6d895",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779223200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "25bb9609-b48c-4f56-b944-2bbd07ace15e",
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current abstract.tex and appendix.tex files to understand their structure and find the right insertion points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "77552d55-0141-4258-a1f9-23882770b180",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qb6fR7qH63NT8eRSUeARSE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11613,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11613
      },
      "output_tokens": 33,
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

读取两个文件，找插入位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "bdc80e57-5a4d-4b7c-88be-f9525d7f2f73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qb6fR7qH63NT8eRSUeARSE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11613,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11613
      },
      "output_tokens": 33,
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

<details open><summary>🔧 Tool call — Read · `toolu_013BCffDX71ddQXSk8VbwLZd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "d1e1dc11-d511-4347-90d2-83389f7f0a16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qb6fR7qH63NT8eRSUeARSE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11613,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11613
      },
      "output_tokens": 33,
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

_source line 7 · 2026-05-19T15:55:30.379Z_

<details><summary>↩ Tool result · `toolu_013BCffDX71ddQXSk8VbwLZd`</summary>

```text
1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.
2	We decompose OpenVLA-7B across all 32 LLM layers using cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes, with factorial trained/pretrained/untrained controls on LIBERO.
3	Three findings emerge.
4	First, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).
5	Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\times$ stronger for instruction-discriminative tasks ($p = 0.033$).
6	Second, vision encoder representations show a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training effects concentrated at the readout token ($R^2$ $+0.069$, attention $+46$pp) rather than visual geometry.
7	Token-level analysis reveals strict functional specialization: image tokens remain instruction-blind across all 32 layers while the readout token serves as the primary multimodal integration site.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "ee577d78-7407-4257-8808-bd82b437bd80",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex",
      "content": "Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.\nWe decompose OpenVLA-7B across all 32 LLM layers using cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes, with factorial trained/pretrained/untrained controls on LIBERO.\nThree findings emerge.\nFirst, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).\nSeven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).\nSecond, vision encoder representations show a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training effects concentrated at the readout token ($R^2$ $+0.069$, attention $+46$pp) rather than visual geometry.\nToken-level analysis reveals strict functional specialization: image tokens remain instruction-blind across all 32 layers while the readout token serves as the primary multimodal integration site.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01XBaivmDMte8Ab2DpiFNxHV`</summary>

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
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "e78c1d3b-c1e7-423c-a463-fa39eaf720be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qb6fR7qH63NT8eRSUeARSE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11613,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11613
      },
      "output_tokens": 33,
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

_source line 9 · 2026-05-19T15:55:30.944Z_

<details><summary>↩ Tool result · `toolu_01XBaivmDMte8Ab2DpiFNxHV`</summary>

```text
1	\paragraph{Use of Generative AI.}
2	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
3	
4	\appendix
5	
6	\section{Supplementary Material}
7	\label{sec:appendix}
8	
9	Unless noted otherwise, all analyses use OpenVLA-7B (\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).
10	Model conditions, representation extraction, metric definitions, and probe architectures follow \S\ref{sec:setup}--\S\ref{sec:probes}.
11	Cross-benchmark experiments (\S\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\times$ 50 demonstrations).
12	All experiments ran on 2$\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs (96\,GB each); random seed is 42 unless stated otherwise.
13	
14	\subsection{CKA Analysis Method}
15	\label{sec:cka_appendix}
16	
17	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
18	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
19	
20	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
21	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
22	
23	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
24	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
25	
26	\subsection{Metric Sensitivity: RSA versus CKA}
27	\label{sec:metric_sensitivity_appendix}
28	
29	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
30	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
31	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
32	
33	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), with no inverted-U pattern.
34	RSA captures rank-order geometric alignment; CKA captures global linear structure.
35	The dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).
36	
37	\begin{figure}[t]
38	\centering
39	\includegraphics[width=\columnwidth]{figures/fig6.pdf}
40	\caption{Three similarity metrics across representation sources. \textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}
41	\label{fig:metric_comparison}
42	\end{figure}
43	
44	\subsection{Branch-Split Detailed Analysis}
45	\label{sec:branch_split_appendix}
46	
47	To disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.
48	The two branches yield near-identical RSA: DINOv2 branch $\rho = 0.619$, SigLIP branch $\rho = 0.621$.
49	Fusion produces a representation ($\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.
50	The MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\rho = 0.615$, a drop of $\Delta = 0.019$ from the fused 2{,}176-D input.
51	
52	\subsection{RSA Across Representation Sources}
53	\label{sec:rsa_bar_appendix}
54	
55	Figure~\ref{fig:rsa_bar} shows RSA with the action space across all representation sources; the ordering matches Table~\ref{tab:rsa_overview}.
56	
57	\begin{figure}[h]
58	\centering
59	\includegraphics[width=\columnwidth]{figures/fig2.pdf}
60	\caption{RSA with the action space ($\rho$) across representation sources. Self-supervised DINOv2 \texttt{cls\_token} ($\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\% bootstrap CIs.}
61	\label{fig:rsa_bar}
62	\end{figure}
63	
64	\subsection{Per-Layer RSA Profiles}
65	\label{sec:rsa_perlayer_appendix}
66	
67	Figure~\ref{fig:rsa_perlayer_curve} extends Figure~\ref{fig:layer_curves} (main text) by adding readout and untrained profiles.
68	
69	\begin{figure}[h]
70	\centering
71	\includegraphics[width=\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}
72	\caption{Per-layer RSA ($\rho$) for trained and untrained models at image\_mean and readout (last\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\_mean diverge: readout $\rho$ declines gradually ($0.628 \to 0.584$) while image\_mean $\rho$ drops sharply ($0.628 \to 0.422$), consistent with task-specific conditioning at the readout position.}
73	\label{fig:rsa_perlayer_curve}
74	\end{figure}
75	
76	\subsection{Per-Layer Action Decoding Across Training Stages}
77	\label{sec:action_r2_threecond}
78	
79	Figure~\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\pm$ std).
80	All three conditions share L0 representations ($R^2 = 0.645 \pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.
81	The trained model peaks at L9 ($R^2 = 0.643 \pm 0.014$), consistent with progressive specialization for action-relevant feature integration.
82	Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), consistent with stable but unspecialized processing.
83	The untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability indicates that randomly initialized Transformer layers produce destructive interference on action-relevant structure.
84	The three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.
85	The qualitative pattern is consistent across all 3 seeds.
86	
87	\begin{figure}[h]
88	\centering
89	\includegraphics[width=\columnwidth]{figures/fig_action_r2_threecond.pdf}
90	\caption{Per-layer action probe $R^2$ (image\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\pm$ std).}
91	\label{fig:action_r2_threecond}
92	\end{figure}
93	
94	\subsection{Random-Subset Ablation Details}
95	\label{sec:random_subset_ablation}
96	
97	To evaluate whether the ablation effect in \S\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).
98	Dominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \pm 0.013$ (Figure~\ref{fig:random_subset_ablation}).
99	The dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); heads with higher instruction-attention fraction carry more organized routing signals, consistent with graded rather than binary specialization.
100	
101	\begin{figure}[h]
102	\centering
103	\includegraphics[width=0.75\columnwidth]{figures/fig_random_subset_ablation.pdf}
104	\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with graded routing specialization across L1 heads.}
105	\label{fig:random_subset_ablation}
106	\end{figure}
107	
108	\subsection{Action Trajectory Analysis Details}
109	\label{sec:action_trajectory}
110	
111	Table~\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.
112	Both conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).
113	The gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.
114	
115	Per-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).
116	Token-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.
117	
118	\paragraph{Trajectory-level aggregation.}
119	Aggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\sim}4\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).
120	Instruction-head ablation ($N = 50$: 5 tasks $\times$ 10 demos) yields trajectory $d = 2.943$ (95\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).
121	All 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.
122	Counterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).
123	Fine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\sim} 1{,}500$) provide higher resolution for ordering claims.
124	
125	\paragraph{Ground-truth action error.}
126	Ablation redirects model outputs ($d = 0.65$) but does not systematically increase error relative to expert demonstrations: original MSE $= 0.498$; top-24 instruction-head ablation MSE $= 0.497$ ($\Delta = -0.001$, Wilcoxon $p = 0.52$, n.s.); bottom-24 non-instruction heads MSE $= 0.506$ ($\Delta = +0.008$).
127	Changes concentrate on the gripper dimension; translation and rotation dimensions are negligibly affected.
128	Per-task breakdown shows all $|\Delta\text{MSE}| < 3\%$ of baseline with all $p > 0.27$; the near-zero aggregate $\Delta$ reflects uniformly small per-task effects rather than cancellation across tasks.
129	This is consistent with the information-computation dissociation: routing heads control instruction-specific direction selection rather than action precision.
130	
131	Table~\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).
132	Individual control heads produce ${\sim}1.9\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.
133	The 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\ $0.41$), consistent with collective coordination rather than individual strength.
134	
135	\begin{table}[h]
136	\centering
137	\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}
138	\label{tab:perhead_bootstrap}
139	\small
140	\begin{tabular}{lccc}
141	\toprule
142	Group & $N$ heads & Collective $d$ & Per-head $d$ [95\% CI] \\
143	\midrule
144	Instruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\
145	Control & 8 & 0.41 & 0.051 [0.048, 0.055] \\
146	\midrule
147	Difference & --- & --- & 0.024, $p = 0.0018$ \\
148	\bottomrule
149	\end{tabular}
150	\end{table}
151	
152	Instruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.
153	
154	Table~\ref{tab:dose_response} and Figure~\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.
155	Trajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\Delta d / \Delta 4 \approx 0.026$), a plateau at 16--20 heads ($\Delta d = 0.001$), and slow increase at 20--32.
156	
157	\begin{figure}[h]
158	\centering
159	\includegraphics[width=0.75\columnwidth]{figures/fig_dose_response.pdf}
160	\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}
161	\label{fig:dose_response}
162	\end{figure}
163	
164	\begin{table}[h]
165	\centering
166	\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\ original action sequence; 95\% bootstrap CIs ($10{,}000$ resamples).}
167	\label{tab:dose_response}
168	\small
169	\begin{tabular}{rcc}
170	\toprule
171	Heads ablated & Cohen's $d$ & 95\% CI \\
172	\midrule
173	4 & 0.482 & [0.449, 0.511] \\
174	8 & 0.508 & [0.479, 0.541] \\
175	12 & 0.560 & [0.529, 0.593] \\
176	16 & 0.592 & [0.559, 0.625] \\
177	20 & 0.593 & [0.559, 0.627] \\
178	24 & 0.611 & [0.578, 0.645] \\
179	28 & 0.619 & [0.587, 0.654] \\
180	32 & 0.639 & [0.603, 0.671] \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
185	\begin{table}[h]
186	\centering
187	\caption{Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$, token divergence (\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}
188	\label{tab:counterfactual}
189	\small
190	\begin{tabular}{lccc}
191	\toprule
192	Condition & Jaccard & Cohen's $d$ & Token div.\ (\%) \\
193	\midrule
194	Empty (no instruction) & 0.000 & 0.968 & 90.7 \\
195	Wrong (different task) & 0.174 & 0.844 & 89.5 \\
196	Paraphrased & 0.533 & 0.697 & 82.6 \\
197	Shuffled (random order) & 1.000 & 0.625 & 85.7 \\
198	\midrule
199	L1 ablation (24 heads) & --- & 0.650 & 72.3 \\
200	\bottomrule
201	\end{tabular}
202	\end{table}
203	
204	\begin{table}[h]
205	\centering
206	\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}
207	\label{tab:action_shift_perdim}
208	\small
209	\begin{tabular}{lccccccc}
210	\toprule
211	Condition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\
212	\midrule
213	Instruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\
214	Control (8) & 0.000 & 0.001 & 0.002 & 0.008 & 0.014 & 0.018 & 0.141 \\
215	\bottomrule
216	\end{tabular}
217	\end{table}
218	
219	\subsection{Pretrained LLM Representation Quality Under Visual Input}
220	\label{sec:ood_diagnostics}
221	
222	A potential concern with the three-condition comparison (\S\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.
223	We evaluate three diagnostics to assess representation quality.
224	Activation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.
225	Per-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\approx 0.28$ at L25, consistent with gradual differentiation rather than catastrophic out-of-distribution behavior.
226	Top-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.
227	These diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining (Figure~\ref{fig:ood_diagnostics}). These results support the validity of the three-condition comparison.
228	
229	\begin{figure}[h]
230	\centering
231	\includegraphics[width=\columnwidth]{figures/fig_ood_diagnostics.pdf}
232	\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics indicate structured, non-degenerate representations.}
233	\label{fig:ood_diagnostics}
234	\end{figure}
235	
236	\subsection{Probe Architecture Sensitivity}
237	\label{sec:linear_probe}
238	
239	To rule out that our findings depend on MLP probe capacity ($N/\text{params} \approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \to 7$, $N/\text{params} \approx 2.2$).
240	The inverted-U pattern reproduces: trained image\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).
241	The trained--untrained gap is larger under the linear probe (L14: $\Delta = +0.324$) than the MLP probe (L8: $\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.
242	Untrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.
243	For last\_preaction tokens, the linear probe also corroborates the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\Delta = 0.103$ ($p < 0.001$).
244	These results indicate that our qualitative findings reflect representational structure rather than probe capacity artifacts (Figure~\ref{fig:linear_vs_mlp}).
245	
246	\begin{figure}[h]
247	\centering
248	\includegraphics[width=\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}
249	\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}
250	\label{fig:linear_vs_mlp}
251	\end{figure}
252	
253	\subsection{Functional Probe Comparison}
254	\label{sec:probe_bars_appendix}
255	
256	Figure~\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.
257	
258	\begin{figure}[h]
259	\centering
260	\includegraphics[width=\columnwidth]{figures/fig4.pdf}
261	\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\_mean ($0.655$, L8) exceed the projector baseline ($0.630$); the inverted-U extends to functional capacity.}
262	\label{fig:probe_bars}
263	\end{figure}
264	
265	\subsection{Training Effect and Instruction Invariance}
266	\label{sec:instruction_invariance_appendix}
267	
268	Figure~\ref{fig:factorial} shows trained vs.\ untrained RSA profiles and instruction invariance.
269	Instruction invariance holds across all conditions: maximum $|\Delta| < 0.006$, so action geometry is visually grounded and not modulated by language instructions.
270	
271	\begin{figure}[h]
272	\centering
273	\includegraphics[width=\columnwidth]{figures/fig5.pdf}
274	\caption{\textbf{(a)}~Trained vs.\ untrained image\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\Delta{=}+0.017$, $3\%$). \textbf{(b)}~Instruction invariance: all conditions within $|\Delta|{<}0.006$; action geometry is visually grounded.}
275	\label{fig:factorial}
276	\end{figure}
277	
278	\subsection{Additional RSA Values}
279	\label{sec:additional_rsa}
280	
281	DINOv2 \texttt{patch\_mean} achieves RSA $\rho = 0.631$, between the \texttt{cls\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).
282	VLA untrained readout peaks at L1 ($\rho = 0.626$).
283	
284	\subsection{Cross-Benchmark Validation: LIBERO-Spatial}
285	\label{sec:cross_benchmark_appendix}
286	
287	To assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks $\times$ 50 demonstrations each, requiring spatial reasoning).
288	Figure~\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.
289	
290	The inverted-U profile replicates on LIBERO-Spatial: trained image\_mean RSA peaks at L14 ($\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.
291	Training produces a significant geometric gain (best-vs-best $\Delta = +0.023$, 95\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\Delta = +0.017$, CI includes zero).
292	
293	Two notable differences emerge.
294	First, the absolute RSA values are higher on Spatial ($0.691$ vs.\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.
295	Second, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\Delta_\text{layer}| = 1$).
296	This suggests that peak convergence is benchmark-specific rather than a general consequence of training.
297	
298	\begin{figure}[t]
299	\centering
300	\includegraphics[width=\columnwidth]{figures/fig7.pdf}
301	\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}
302	\label{fig:cross_benchmark}
303	\end{figure}
304	
305	\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}
306	\label{sec:spatial_cross_instruction}
307	
308	Table~\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.
309	The core pattern from LIBERO-Goal replicates: image\_mean remains at chance (${\sim}10\%$) across all layers and conditions, while the trained readout token saturates to $100\%$ by L4.
310	The untrained readout decays more steeply than on LIBERO-Goal ($75.4\%$ at L31 vs.\ $82\%$), consistent with greater task difficulty.
311	
312	\begin{table}[h]
313	\centering
314	\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\%$ from L4; image\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\ Table~\ref{tab:dense_routing_main}).}
315	\label{tab:spatial_cross_instruction}
316	\small
317	\begin{tabular}{llccccc}
318	\toprule
319	Token & Condition & L1 & L4 & L8 & L16 & L31 \\
320	\midrule
321	last\_preaction & Trained & 98.9\% & 100.0\% & 100.0\% & 100.0\% & 100.0\% \\
322	last\_preaction & Untrained & 99.5\% & 98.3\% & 85.7\% & 68.3\% & 75.4\% \\
323	image\_mean & Trained & 10.2\% & 10.0\% & 9.9\% & 10.0\% & 10.1\% \\
324	image\_mean & Untrained & 10.1\% & 10.0\% & 10.0\% & 10.0\% & 10.2\% \\
325	\bottomrule
326	\end{tabular}
327	\end{table}
328	
329	\subsection{Robustness Analyses}
330	\label{sec:robustness_appendix}
331	
332	\subsubsection{Distance Metric Invariance}
333	\label{sec:metric_invariance}
334	
335	The inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\ref{tab:metric_invariance}).
336	
337	\begin{table}[h]
338	\centering
339	\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}
340	\label{tab:metric_invariance}
341	\small
342	\begin{tabular}{lccc}
343	\toprule
344	Condition & Eucl.\ Peak & Cos.\ Peak & Profile $r$ \\
345	\midrule
346	Trained image\_mean & L12 & L12 & 0.990 \\
347	Trained last\_preaction & L12 & L13 & 0.990 \\
348	Untrained image\_mean & L0 & L0 & 0.995 \\
349	Untrained last\_preaction & L1 & L1 & 0.992 \\
350	\bottomrule
351	\end{tabular}
352	\end{table}
353	
354	\subsubsection{Per-DOF Decomposition}
355	\label{sec:perdof}
356	
357	RSA decomposition by action dimension indicates the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\rho = 0.193$), rotation (peak L12, $\rho = 0.175$), and gripper (peak L13, $\rho = 0.106$) all exhibit non-monotonic profiles.
358	Per-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.
359	
360	\subsubsection{Permutation Test}
361	\label{sec:permutation}
362	
363	Permutation testing (1{,}000 shuffles) indicates all observed RSA values are highly significant: observed $\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).
364	
365	\subsubsection{Probe Seed Sensitivity}
366	\label{sec:seed_sensitivity}
367	
368	Action probe $R^2$ is highly stable across random seeds.
369	Over 5 seeds (trained image\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\%$ ($0.655 \pm 0.002$; Table~\ref{tab:seed_sensitivity}).
370	Peak layer concentrates in the L8--L10 region ($4/5$ seeds); the inverted-U shape is not a seed artifact.
371	Seed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.
372	
373	\begin{table}[h]
374	\centering
375	\caption{Probe $R^2$ peak across 5 random seeds (trained image\_mean).}
376	\label{tab:seed_sensitivity}
377	\small
378	\begin{tabular}{lcc}
379	\toprule
380	Seed & Peak Layer & Peak $R^2$ \\
381	\midrule
382	0 & L9 & 0.654 \\
383	1 & L16 & 0.656 \\
384	2 & L9 & 0.653 \\
385	3 & L10 & 0.655 \\
386	42 & L9 & 0.655 \\
387	\midrule
388	Mean$\pm$std & $10.6\pm2.7$ & $0.655\pm0.002$ \\
389	\bottomrule
390	\end{tabular}
391	\end{table}
392	
393	\subsubsection{Demonstration Subsample Sensitivity}
394	\label{sec:demo_sensitivity}
395	
396	To verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\ref{tab:demo_sensitivity}).
397	The RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions (high stability).
398	The probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$; $R^2$ is more sensitive to training set size than RSA.
399	Both metrics show reduced absolute values (RSA $-3.6\%$, $R^2$ $-7.6\%$) as expected from halved data, but the non-monotonic profile shape is preserved.
400	
401	\begin{table}[h]
402	\centering
403	\caption{Inverted-U stability under demonstration subsampling (trained image\_mean).}
404	\label{tab:demo_sensitivity}
405	\small
406	\begin{tabular}{lccc}
407	\toprule
408	Metric & 50 demos & 25 demos & $\Delta$ \\
409	\midrule
410	RSA peak layer & L12 & L12 & 0 \\
411	RSA peak $\rho$ & 0.628 & 0.606 & $-3.6\%$ \\
412	$R^2$ peak layer & L9 & L11 & $+2$ \\
413	$R^2$ peak value & 0.659 & 0.609 & $-7.6\%$ \\
414	RSA profile $r$ & --- & 0.970 & --- \\
415	$R^2$ profile $r$ & --- & 0.819 & --- \\
416	\bottomrule
417	\end{tabular}
418	\end{table}
419	
420	\subsection{Detailed Training Effects}
421	\label{sec:training_effects_appendix}
422	
423	Table~\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.
424	
425	\begin{table}[h]
426	\centering
427	\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\Delta{=}+0.017$, $3\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}
428	\label{tab:training_effects}
429	\small
430	\begin{tabular}{lccc}
431	\toprule
432	Comparison & $\Delta$ & 95\% CI & $p$ \\
433	\midrule
434	\multicolumn{4}{l}{\emph{RSA ($\rho$)}} \\
435	Best-vs-best image\_mean & $+$0.017 & incl.\ 0 & n.s. \\
436	\quad (trained L12 vs.\ untrained L0) & & & \\
437	Same-layer L12 image\_mean & $+$0.079 & excl.\ 0 & $<$0.0001 \\
438	\quad (trained vs.\ untrained) & & & \\
439	Instruction effect (max $|\Delta|$) & 0.006 & --- & n.s. \\
440	\midrule
441	\multicolumn{4}{l}{\emph{Probe $R^2$}} \\
442	Best-vs-best image\_mean & $+$0.015 & excl.\ 0 & 0.006 \\
443	\quad (trained L8 vs.\ untrained L0) & & & \\
444	Best-vs-best readout & $+$0.069 & excl.\ 0 & $<$0.0001 \\
445	\quad (trained L13 vs.\ untrained L32) & & & \\
446	\bottomrule
447	\end{tabular}
448	\end{table}
449	
450	\subsection{Training Effect Size Summary}
451	\label{sec:training_effect_summary}
452	
453	Table~\ref{tab:training_effect_summary} consolidates training effects across all metrics.
454	Training effects on image\_mean metrics are modest (RSA $\Delta = +0.017$, $R^2$ $\Delta = +0.015$), but effects on last\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\Delta = +0.069$).
455	This asymmetry indicates that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.
456	
457	\begin{table}[h]
458	\centering
459	\caption{Training effect sizes across metrics. Image\_mean effects are modest; last\_preaction effects are large. Training targets readout-token information integration.}
460	\label{tab:training_effect_summary}
461	\small
462	\begin{tabular}{lccc}
463	\toprule
464	Metric & Trained & Untrained & $\Delta$ \\
465	\midrule
466	RSA peak (image\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\
467	$R^2$ peak (image\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\
468	$R^2$ peak (last\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\
469	Instruction routing L31 & 100\% & 82\% & $+$18pp \\
470	Instruction attention L1 & 58\% & 12\% & $+$46pp \\
471	Progress classification & 86.3\% (L20) & 85.3\% (L4) & $+$1pp \\
472	\bottomrule
473	\end{tabular}
474	\end{table}
475	
476	\subsection{Instruction Routing Probes}
477	\label{sec:routing_appendix}
478	
479	\subsubsection{Cross-Instruction Classification: Dense Layer Profile}
480	\label{sec:dense_routing}
481	
482	Table~\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.
483	The step-function onset between L0 ($10\%$, chance) and L1 (${\geq}99.6\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\sim}12\%$) suffices for linear classification at L1.
484	Both pretrained and VLA-trained models sustain $100\%$ through L31; only random initialization shows progressive decay ($82\%$ at L31). Deep-layer stability thus derives from structured pretrained weights rather than task-specific fine-tuning.
485	
486	\begin{table}[h]
487	\centering
488	\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8. Values reflect dense routing evaluation; main-text Table~\ref{tab:dense_routing_main} reports sparse single-split results, yielding minor differences (e.g., L8: $98.2\%$ vs.\ $98.6\%$).}
489	\label{tab:dense_routing}
490	\small
491	\begin{tabular}{lccc}
492	\toprule
493	Layer & Trained & Untrained & Image\_mean (trained) \\
494	\midrule
495	L0 & 10.0\% & 10.0\% & 10.0\% \\
496	L1 & 100.0\% & 100.0\% & 10.0\% \\
497	L2 & 100.0\% & 99.6\% & 10.0\% \\
498	L3 & 100.0\% & 99.6\% & 10.0\% \\
499	L4 & 100.0\% & 99.1\% & 10.0\% \\
500	L5 & 100.0\% & 98.2\% & 10.0\% \\
501	L6 & 100.0\% & 97.3\% & 10.0\% \\
502	L7 & 100.0\% & 96.4\% & 10.0\% \\
503	L8 & 100.0\% & 98.6\% & 10.0\% \\
504	\bottomrule
505	\end{tabular}
506	\end{table}
507	
508	\subsubsection{Cross-Instruction LOOCV Validation}
509	\label{sec:loocv}
510	
511	Leave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) validates that the cross-instruction probe result is not driven by memorization.
512	Trained last\_preaction achieves $100\% \pm 0.00$ across all 10 folds at layers L1--L31 (perfect generalization).
513	
514	\subsubsection{QA Probe: Progress and Subtask Classification}
515	\label{sec:qa_probe}
516	
517	To test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train logistic regression probes (scikit-learn, $C = 1.0$, max\_iter $= 1{,}000$) to classify task progress (4-class: each trajectory split into 4 equal temporal segments) and active subtask (binary: first vs.\ second half) from frozen representations, with an 80/20 random train/test split (Table~\ref{tab:qa_probe}).
518	
519	\begin{table}[h]
520	\centering
521	\caption{QA probe accuracy (progress + subtask classification, best layer).}
522	\label{tab:qa_probe}
523	\small
524	\begin{tabular}{lcc}
525	\toprule
526	Source & Best Layer & Accuracy \\
527	\midrule
528	Trained last\_preaction & L20 & 86.3\% \\
529	Untrained last\_preaction & L20 & 85.3\% \\
530	DINOv2 cls\_token & --- & 82.7\% \\
531	\bottomrule
532	\end{tabular}
533	\end{table}
534	
535	\subsubsection{Cross-Instruction Probe Profiles}
536	\label{sec:probe_profiles}
537	
538	\begin{figure}[h]
539	\centering
540	\includegraphics[width=\columnwidth]{figures/fig_probe_conditions.pdf}
541	\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\%$ at L1, saturating to $100\%$. Llama-2 base starts at $80.2\%$, reaching $100\%$ by L5. Untrained starts at $100\%$ but decays to $82\%$ by L31.}
542	\label{fig:probe_conditions_appendix}
543	\end{figure}
544	
545	\subsubsection{Four-Condition Cross-Instruction Probe Profile}
546	\label{app:finetuned_probe}
547	
548	Table~\ref{tab:finetuned_probe} extends the three-condition probe comparison (Table~\ref{tab:dense_routing_main}) with the LIBERO-finetuned checkpoint.
549	
550	\begin{table}[h]
551	\centering
552	\caption{Cross-instruction 10-way classification accuracy across four training conditions. Task-specific fine-tuning (LIBERO) preserves instruction decodability at all layers despite eliminating L31 exit-layer attention engagement (18$\to$0 instruction-dominant heads).}
553	\label{tab:finetuned_probe}
554	\small
555	\begin{tabular}{lcccc}
556	\toprule
557	Layer & Untrained & Llama-2 base & OpenVLA-7B & LIBERO-finetuned \\
558	\midrule
559	L0 & 10.0\% & 10.0\% & 10.0\% & 10.0\% \\
560	L1 & 100.0\% & 80.2\% & 99.6\% & 99.7\% \\
561	L8 & 98.6\% & 99.9\% & 100.0\% & 100.0\% \\
562	L31 & 82.0\% & 100.0\% & 100.0\% & 100.0\% \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	\subsubsection{L1 Attention Pattern Analysis}
568	\label{sec:attention_pattern}
569	
570	Figure~\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.
571	The three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.
572	
573	\begin{figure}[h]
574	\centering
575	\includegraphics[width=\columnwidth]{figures/fig_l1_stacked_bar.pdf}
576	\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\%$ text attention). Llama-2 base: 9/32 heads ($36.5\%$). Untrained: 0/32 heads ($11.7\%$). See Table~\ref{tab:routing_gradient} for quantitative comparison.}
577	\label{fig:attention_appendix}
578	\end{figure}
579	
580	\subsubsection{Multi-Layer Attention Patterns}
581	\label{sec:multilayer_attention}
582	
583	Table~\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\ref{fig:attention_profile}, main text).
584	The full profile (Figure~\ref{fig:multilayer_attention}) reveals three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).
585	
586	\begin{figure}[h]
587	\centering
588	\includegraphics[width=\columnwidth]{figures/fig_multi_layer_attn.pdf}
589	\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}
590	\label{fig:multilayer_attention}
591	\end{figure}
592	
593	\begin{table}[h]
594	\centering
595	\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\ref{tab:routing_gradient}) due to threshold boundary effects.}
596	\label{tab:multilayer_attention}
597	\small
598	\begin{tabular}{lcccccc}
599	\toprule
600	 & \multicolumn{2}{c}{VLA Trained} & \multicolumn{2}{c}{Llama-2 base} & \multicolumn{2}{c}{Untrained} \\
601	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
602	Layer & Heads & Text\% & Heads & Text\% & Heads & Text\% \\
603	\midrule
604	L1 & \textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\
605	L8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\
606	L16 & 10/32 & 48.4 & \textbf{25/32} & 60.2 & 0/32 & 9.2 \\
607	L31 & \textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\
608	\bottomrule
609	\end{tabular}
610	\end{table}
611	
612	\subsubsection{Threshold Sensitivity Analysis}
613	\label{sec:threshold_sensitivity}
614	
615	The main text defines instruction-dominant heads as those allocating $>50\%$ attention to instruction tokens.
616	Table~\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\% to 70\%; the 50\% threshold is not a boundary-sensitive choice.
617	
618	\begin{table}[h]
619	\centering
620	\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}
621	\label{tab:threshold_sensitivity}
622	\small
623	\begin{tabular}{lccc}
624	\toprule
625	Threshold & VLA Trained & Llama-2 base & Untrained \\
626	\midrule
627	30\% & 32 & 13 & 0 \\
628	40\% & 31 & 10 & 0 \\
629	50\% & 24 & 9 & 0 \\
630	60\% & 9 & 4 & 0 \\
631	70\% & 5 & 3 & 0 \\
632	\bottomrule
633	\end{tabular}
634	\end{table}
635	
636	\subsection{L1 Attention Decomposition by Head Group}
637	\label{sec:attention_decomp}
638	
639	Table~\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.
640	
641	\begin{table}[h]
642	\centering
643	\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}
644	\label{tab:attention_decomp}
645	\small
646	\begin{tabular}{lcccc}
647	\toprule
648	Head Group & $N$ & Instruction & Vision & BOS/Other \\
649	\midrule
650	Instruction-dominant & 24 & 62.4\% & 18.8\% & 18.8\% \\
651	Control & 8 & 44.9\% & 27.1\% & 28.0\% \\
652	\midrule
653	$\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\
654	\bottomrule
655	\end{tabular}
656	\end{table}
657	
658	Head-level instruction attention entropy reaches $99.5\%$ of the uniform maximum; routing is broadly distributed rather than concentrated in a few heads.
659	
660	\paragraph{Per-token attention normalization.}
661	The $57.7\%$ aggregate text attention in instruction-dominant heads partly reflects token-count imbalance (22 instruction vs.\ 256 image tokens).
662	Per-token normalization reveals a $38.2\times$ ratio: each instruction token receives $38.2\times$ the attention of each image token in trained instruction-dominant heads, compared to only $1.5\times$ in untrained heads (a $25.5\times$ increase from training).
663	Instruction-dominant heads also show lower attention entropy ($0.465$) than non-dominant heads ($0.569$), indicating more concentrated attention distributions.
664	
665	\subsection{Per-Dimension Action MAE Under Head Ablation}
666	\label{sec:per_dim_mae}
667	
668	Table~\ref{tab:per_dim_mae} extends Table~\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.
669	
670	\begin{table}[h]
671	\centering
672	\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\times$); instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\times$) falls between the two groups.}
673	\label{tab:per_dim_mae}
674	\small
675	\begin{tabular}{lccc}
676	\toprule
677	Dimension & Instr.\ 24h MAE & Control 8h MAE & Ratio \\
678	\midrule
679	$dx$ & 0.00189 & 0.00037 & 5.09$\times$ \\
680	$dy$ & 0.00531 & 0.00125 & 4.26$\times$ \\
681	$dz$ & 0.00762 & 0.00243 & 3.14$\times$ \\
682	$roll$ & 0.02059 & 0.00785 & 2.62$\times$ \\
683	$pitch$ & 0.03071 & 0.01387 & 2.21$\times$ \\
684	$yaw$ & 0.03388 & 0.01783 & 1.90$\times$ \\
685	$gripper$ & 0.29072 & 0.14072 & 2.07$\times$ \\
686	\bottomrule
687	\end{tabular}
688	\end{table}
689	
690	\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}
691	\label{sec:per_task_r2}
692	
693	Table~\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).
694	
695	\begin{table}[h]
696	\centering
697	\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\Delta > 0$): instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\Delta R^2 = +0.107$; the 50-demo setting (\S\ref{sec:learned_routing}) yields a consistent $+0.059$.}
698	\label{tab:per_task_r2}
699	\small
700	\begin{tabular}{lccc}
701	\toprule
702	Task & Baseline $R^2$ & Ablated $R^2$ & $\Delta R^2$ \\
703	\midrule
704	open middle drawer & 0.197 & 0.221 & $+$0.024 \\
705	open top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\
706	push plate to stove & 0.190 & 0.197 & $+$0.007 \\
707	put bowl on plate & 0.375 & 0.474 & $+$0.099 \\
708	put bowl on stove & 0.235 & 0.395 & $+$0.160 \\
709	put bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\
710	put cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\
711	put wine on rack & 0.189 & 0.424 & $+$0.235 \\
712	put wine on cabinet & 0.279 & 0.353 & $+$0.074 \\
713	turn on stove & 0.385 & 0.421 & $+$0.036 \\
714	\midrule
715	Mean $\pm$ std & $0.256 \pm 0.070$ & $0.363 \pm 0.088$ & $+$0.107 \\
716	\bottomrule
717	\end{tabular}
718	\end{table}
719	
720	\subsection{Task Complexity and Routing Dependence}
721	\label{sec:task_complexity}
722	
723	We classify tasks as \emph{instruction-discriminative} when multiple tasks share the same manipulated object(s), requiring instruction content to disambiguate the target action (e.g., ``put bowl on plate'' vs.\ ``put bowl on stove''); remaining tasks involve unique object-action pairings recoverable from visual context alone.
724	Table~\ref{tab:task_complexity} reports per-task $|\Delta R^2|$ under both groupings.
725	
726	\begin{table}[h]
727	\centering
728	\caption{Task-level L1 ablation effects ($|\Delta R^2|$) grouped by instruction dependence. \emph{Primary} (conservative): cream cheese in bowl classified as visual-sufficient ($2.5\times$, $p = 0.033$). \emph{Sensitivity} (shared-object criterion): cream cheese reclassified as instruction-discriminative ($6.5\times$, $p = 0.008$).}
729	\label{tab:task_complexity}
730	\small
731	\begin{tabular}{lcc}
732	\toprule
733	Task & $|\Delta R^2|$ & Group \\
734	\midrule
735	put wine on rack & 0.235 & Instr-disc \\
736	put bowl on cabinet & 0.201 & Instr-disc \\
737	put bowl on stove & 0.160 & Instr-disc \\
738	put bowl on plate & 0.099 & Instr-disc \\
739	open top drawer + bowl & 0.075 & Instr-disc \\
740	put wine on cabinet & 0.074 & Instr-disc \\
741	\midrule
742	put cream cheese in bowl$^\dagger$ & 0.159 & Vis-suff \\
743	turn on stove & 0.036 & Vis-suff \\
744	open middle drawer & 0.024 & Vis-suff \\
745	push plate to stove & 0.007 & Vis-suff \\
746	\midrule
747	\multicolumn{3}{l}{\textbf{Primary}: Instr-disc mean $0.141$; Vis-suff mean $0.057$} \\
748	\multicolumn{3}{l}{Mann-Whitney $U = 21.0$, $p = 0.033$, ratio $= 2.49\times$} \\
749	\multicolumn{3}{l}{\textbf{Sensitivity}$^\dagger$: cream cheese as Instr-disc: $p = 0.008$, $6.5\times$} \\
750	\bottomrule
751	\end{tabular}
752	\end{table}
753	
754	\paragraph{Leave-one-out sensitivity.}
755	All leave-one-out $p$-values remain $\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.
756	Reclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).
757	
758	\subsection{Specificity Control: Matched-Size Head Ablation}
759	\label{sec:specificity_control}
760	
761	To test whether ablation effects are specific to instruction-dominant heads, we ablate four matched-size subsets of 24 heads at L1: instruction-dominant (highest instruction attention fraction), image-dominant (highest image attention fraction), random (5 seeds), and bottom-24 (lowest instruction attention fraction; overlaps 16/24 heads with the instruction-dominant group).
762	
763	\begin{table}[h]
764	\centering
765	\caption{Matched-size ablation controls: trajectory disruption ($d$) from ablating 24-head subsets at L1, ranked by instruction attention fraction. Instruction-dominant heads produce the largest effect, but the modest gap ($8\%$ over random) indicates distributed, attention-graded routing rather than a dedicated subset.}
766	\label{tab:specificity_control}
767	\small
768	\begin{tabular}{lcc}
769	\toprule
770	Condition (24 heads) & Cohen's $d$ & 95\% CI \\
771	\midrule
772	Instruction-dominant & 0.650 & (reference) \\
773	Random (5 seeds) & $0.601 \pm 0.021$ & $[0.568, 0.622]$ \\
774	Image-dominant & 0.580 & $[0.547, 0.613]$ \\
775	Bottom-24 & 0.565 & --- \\
776	\bottomrule
777	\end{tabular}
778	\end{table}
779	
780	All conditions yield comparable ground-truth MSE ($0.487$--$0.504$ vs.\ baseline $0.497$), consistent with direction-selective rather than precision-degrading effects.
781	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "1ed5ac03-b624-4cdb-b828-b096eef1f22b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
      "content": "\\paragraph{Use of Generative AI.}\nGenerative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.\n\n\\appendix\n\n\\section{Supplementary Material}\n\\label{sec:appendix}\n\nUnless noted otherwise, all analyses use OpenVLA-7B (\\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).\nModel conditions, representation extraction, metric definitions, and probe architectures follow \\S\\ref{sec:setup}--\\S\\ref{sec:probes}.\nCross-benchmark experiments (\\S\\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\\times$ 50 demonstrations).\nAll experiments ran on 2$\\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs (96\\,GB each); random seed is 42 unless stated otherwise.\n\n\\subsection{CKA Analysis Method}\n\\label{sec:cka_appendix}\n\nWe employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA as a complementary perspective.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.\n\n\\subsection{Metric Sensitivity: RSA versus CKA}\n\\label{sec:metric_sensitivity_appendix}\n\nLinear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.\n\nAt the per-layer level, linear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), with no inverted-U pattern.\nRSA captures rank-order geometric alignment; CKA captures global linear structure.\nThe dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}\n\\label{fig:metric_comparison}\n\\end{figure}\n\n\\subsection{Branch-Split Detailed Analysis}\n\\label{sec:branch_split_appendix}\n\nTo disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.\nThe two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.\nFusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.\nThe MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.\n\n\\subsection{RSA Across Representation Sources}\n\\label{sec:rsa_bar_appendix}\n\nFigure~\\ref{fig:rsa_bar} shows RSA with the action space across all representation sources; the ordering matches Table~\\ref{tab:rsa_overview}.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n\\subsection{Per-Layer RSA Profiles}\n\\label{sec:rsa_perlayer_appendix}\n\nFigure~\\ref{fig:rsa_perlayer_curve} extends Figure~\\ref{fig:layer_curves} (main text) by adding readout and untrained profiles.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}\n\\caption{Per-layer RSA ($\\rho$) for trained and untrained models at image\\_mean and readout (last\\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\\_mean diverge: readout $\\rho$ declines gradually ($0.628 \\to 0.584$) while image\\_mean $\\rho$ drops sharply ($0.628 \\to 0.422$), consistent with task-specific conditioning at the readout position.}\n\\label{fig:rsa_perlayer_curve}\n\\end{figure}\n\n\\subsection{Per-Layer Action Decoding Across Training Stages}\n\\label{sec:action_r2_threecond}\n\nFigure~\\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\\pm$ std).\nAll three conditions share L0 representations ($R^2 = 0.645 \\pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.\nThe trained model peaks at L9 ($R^2 = 0.643 \\pm 0.014$), consistent with progressive specialization for action-relevant feature integration.\nLlama-2 base shows a steady decline (L0: $0.645 \\to$ L32: $0.551$, std $0.003$--$0.035$), consistent with stable but unspecialized processing.\nThe untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability indicates that randomly initialized Transformer layers produce destructive interference on action-relevant structure.\nThe three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.\nThe qualitative pattern is consistent across all 3 seeds.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_action_r2_threecond.pdf}\n\\caption{Per-layer action probe $R^2$ (image\\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \\pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\\pm$ std).}\n\\label{fig:action_r2_threecond}\n\\end{figure}\n\n\\subsection{Random-Subset Ablation Details}\n\\label{sec:random_subset_ablation}\n\nTo evaluate whether the ablation effect in \\S\\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).\nDominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \\pm 0.013$ (Figure~\\ref{fig:random_subset_ablation}).\nThe dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); heads with higher instruction-attention fraction carry more organized routing signals, consistent with graded rather than binary specialization.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_random_subset_ablation.pdf}\n\\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \\pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with graded routing specialization across L1 heads.}\n\\label{fig:random_subset_ablation}\n\\end{figure}\n\n\\subsection{Action Trajectory Analysis Details}\n\\label{sec:action_trajectory}\n\nTable~\\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.\nBoth conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).\nThe gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.\n\nPer-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).\nToken-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.\n\n\\paragraph{Trajectory-level aggregation.}\nAggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\\sim}4\\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).\nInstruction-head ablation ($N = 50$: 5 tasks $\\times$ 10 demos) yields trajectory $d = 2.943$ (95\\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).\nAll 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.\nCounterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).\nFine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\\sim} 1{,}500$) provide higher resolution for ordering claims.\n\n\\paragraph{Ground-truth action error.}\nAblation redirects model outputs ($d = 0.65$) but does not systematically increase error relative to expert demonstrations: original MSE $= 0.498$; top-24 instruction-head ablation MSE $= 0.497$ ($\\Delta = -0.001$, Wilcoxon $p = 0.52$, n.s.); bottom-24 non-instruction heads MSE $= 0.506$ ($\\Delta = +0.008$).\nChanges concentrate on the gripper dimension; translation and rotation dimensions are negligibly affected.\nPer-task breakdown shows all $|\\Delta\\text{MSE}| < 3\\%$ of baseline with all $p > 0.27$; the near-zero aggregate $\\Delta$ reflects uniformly small per-task effects rather than cancellation across tasks.\nThis is consistent with the information-computation dissociation: routing heads control instruction-specific direction selection rather than action precision.\n\nTable~\\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).\nIndividual control heads produce ${\\sim}1.9\\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.\nThe 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\\ $0.41$), consistent with collective coordination rather than individual strength.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}\n\\label{tab:perhead_bootstrap}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nGroup & $N$ heads & Collective $d$ & Per-head $d$ [95\\% CI] \\\\\n\\midrule\nInstruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\\\\nControl & 8 & 0.41 & 0.051 [0.048, 0.055] \\\\\n\\midrule\nDifference & --- & --- & 0.024, $p = 0.0018$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInstruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.\n\nTable~\\ref{tab:dose_response} and Figure~\\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.\nTrajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\\Delta d / \\Delta 4 \\approx 0.026$), a plateau at 16--20 heads ($\\Delta d = 0.001$), and slow increase at 20--32.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\\ original action sequence; 95\\% bootstrap CIs ($10{,}000$ resamples).}\n\\label{tab:dose_response}\n\\small\n\\begin{tabular}{rcc}\n\\toprule\nHeads ablated & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\n4 & 0.482 & [0.449, 0.511] \\\\\n8 & 0.508 & [0.479, 0.541] \\\\\n12 & 0.560 & [0.529, 0.593] \\\\\n16 & 0.592 & [0.559, 0.625] \\\\\n20 & 0.593 & [0.559, 0.627] \\\\\n24 & 0.611 & [0.578, 0.645] \\\\\n28 & 0.619 & [0.587, 0.654] \\\\\n32 & 0.639 & [0.603, 0.671] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$, token divergence (\\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \\text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}\n\\label{tab:counterfactual}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Jaccard & Cohen's $d$ & Token div.\\ (\\%) \\\\\n\\midrule\nEmpty (no instruction) & 0.000 & 0.968 & 90.7 \\\\\nWrong (different task) & 0.174 & 0.844 & 89.5 \\\\\nParaphrased & 0.533 & 0.697 & 82.6 \\\\\nShuffled (random order) & 1.000 & 0.625 & 85.7 \\\\\n\\midrule\nL1 ablation (24 heads) & --- & 0.650 & 72.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}\n\\label{tab:action_shift_perdim}\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\nCondition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\\\\n\\midrule\nInstruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\\\\nControl (8) & 0.000 & 0.001 & 0.002 & 0.008 & 0.014 & 0.018 & 0.141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pretrained LLM Representation Quality Under Visual Input}\n\\label{sec:ood_diagnostics}\n\nA potential concern with the three-condition comparison (\\S\\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.\nWe evaluate three diagnostics to assess representation quality.\nActivation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \\to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.\nPer-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\\approx 0.28$ at L25, consistent with gradual differentiation rather than catastrophic out-of-distribution behavior.\nTop-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.\nThese diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining (Figure~\\ref{fig:ood_diagnostics}). These results support the validity of the three-condition comparison.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ood_diagnostics.pdf}\n\\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics indicate structured, non-degenerate representations.}\n\\label{fig:ood_diagnostics}\n\\end{figure}\n\n\\subsection{Probe Architecture Sensitivity}\n\\label{sec:linear_probe}\n\nTo rule out that our findings depend on MLP probe capacity ($N/\\text{params} \\approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \\to 7$, $N/\\text{params} \\approx 2.2$).\nThe inverted-U pattern reproduces: trained image\\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).\nThe trained--untrained gap is larger under the linear probe (L14: $\\Delta = +0.324$) than the MLP probe (L8: $\\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.\nUntrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.\nFor last\\_preaction tokens, the linear probe also corroborates the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\\Delta = 0.103$ ($p < 0.001$).\nThese results indicate that our qualitative findings reflect representational structure rather than probe capacity artifacts (Figure~\\ref{fig:linear_vs_mlp}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}\n\\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}\n\\label{fig:linear_vs_mlp}\n\\end{figure}\n\n\\subsection{Functional Probe Comparison}\n\\label{sec:probe_bars_appendix}\n\nFigure~\\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\\_mean ($0.655$, L8) exceed the projector baseline ($0.630$); the inverted-U extends to functional capacity.}\n\\label{fig:probe_bars}\n\\end{figure}\n\n\\subsection{Training Effect and Instruction Invariance}\n\\label{sec:instruction_invariance_appendix}\n\nFigure~\\ref{fig:factorial} shows trained vs.\\ untrained RSA profiles and instruction invariance.\nInstruction invariance holds across all conditions: maximum $|\\Delta| < 0.006$, so action geometry is visually grounded and not modulated by language instructions.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\\Delta{=}+0.017$, $3\\%$). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$; action geometry is visually grounded.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Additional RSA Values}\n\\label{sec:additional_rsa}\n\nDINOv2 \\texttt{patch\\_mean} achieves RSA $\\rho = 0.631$, between the \\texttt{cls\\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).\nVLA untrained readout peaks at L1 ($\\rho = 0.626$).\n\n\\subsection{Cross-Benchmark Validation: LIBERO-Spatial}\n\\label{sec:cross_benchmark_appendix}\n\nTo assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks $\\times$ 50 demonstrations each, requiring spatial reasoning).\nFigure~\\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.\n\nThe inverted-U profile replicates on LIBERO-Spatial: trained image\\_mean RSA peaks at L14 ($\\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.\nTraining produces a significant geometric gain (best-vs-best $\\Delta = +0.023$, 95\\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\\Delta = +0.017$, CI includes zero).\n\nTwo notable differences emerge.\nFirst, the absolute RSA values are higher on Spatial ($0.691$ vs.\\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.\nSecond, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\\Delta_\\text{layer}| = 1$).\nThis suggests that peak convergence is benchmark-specific rather than a general consequence of training.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig7.pdf}\n\\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}\n\\label{fig:cross_benchmark}\n\\end{figure}\n\n\\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}\n\\label{sec:spatial_cross_instruction}\n\nTable~\\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.\nThe core pattern from LIBERO-Goal replicates: image\\_mean remains at chance (${\\sim}10\\%$) across all layers and conditions, while the trained readout token saturates to $100\\%$ by L4.\nThe untrained readout decays more steeply than on LIBERO-Goal ($75.4\\%$ at L31 vs.\\ $82\\%$), consistent with greater task difficulty.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\\%$ from L4; image\\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\\ Table~\\ref{tab:dense_routing_main}).}\n\\label{tab:spatial_cross_instruction}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nToken & Condition & L1 & L4 & L8 & L16 & L31 \\\\\n\\midrule\nlast\\_preaction & Trained & 98.9\\% & 100.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\nlast\\_preaction & Untrained & 99.5\\% & 98.3\\% & 85.7\\% & 68.3\\% & 75.4\\% \\\\\nimage\\_mean & Trained & 10.2\\% & 10.0\\% & 9.9\\% & 10.0\\% & 10.1\\% \\\\\nimage\\_mean & Untrained & 10.1\\% & 10.0\\% & 10.0\\% & 10.0\\% & 10.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness Analyses}\n\\label{sec:robustness_appendix}\n\n\\subsubsection{Distance Metric Invariance}\n\\label{sec:metric_invariance}\n\nThe inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\\ref{tab:metric_invariance}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}\n\\label{tab:metric_invariance}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Eucl.\\ Peak & Cos.\\ Peak & Profile $r$ \\\\\n\\midrule\nTrained image\\_mean & L12 & L12 & 0.990 \\\\\nTrained last\\_preaction & L12 & L13 & 0.990 \\\\\nUntrained image\\_mean & L0 & L0 & 0.995 \\\\\nUntrained last\\_preaction & L1 & L1 & 0.992 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Per-DOF Decomposition}\n\\label{sec:perdof}\n\nRSA decomposition by action dimension indicates the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\\rho = 0.193$), rotation (peak L12, $\\rho = 0.175$), and gripper (peak L13, $\\rho = 0.106$) all exhibit non-monotonic profiles.\nPer-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.\n\n\\subsubsection{Permutation Test}\n\\label{sec:permutation}\n\nPermutation testing (1{,}000 shuffles) indicates all observed RSA values are highly significant: observed $\\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).\n\n\\subsubsection{Probe Seed Sensitivity}\n\\label{sec:seed_sensitivity}\n\nAction probe $R^2$ is highly stable across random seeds.\nOver 5 seeds (trained image\\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\\%$ ($0.655 \\pm 0.002$; Table~\\ref{tab:seed_sensitivity}).\nPeak layer concentrates in the L8--L10 region ($4/5$ seeds); the inverted-U shape is not a seed artifact.\nSeed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe $R^2$ peak across 5 random seeds (trained image\\_mean).}\n\\label{tab:seed_sensitivity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSeed & Peak Layer & Peak $R^2$ \\\\\n\\midrule\n0 & L9 & 0.654 \\\\\n1 & L16 & 0.656 \\\\\n2 & L9 & 0.653 \\\\\n3 & L10 & 0.655 \\\\\n42 & L9 & 0.655 \\\\\n\\midrule\nMean$\\pm$std & $10.6\\pm2.7$ & $0.655\\pm0.002$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Demonstration Subsample Sensitivity}\n\\label{sec:demo_sensitivity}\n\nTo verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\\ref{tab:demo_sensitivity}).\nThe RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions (high stability).\nThe probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$; $R^2$ is more sensitive to training set size than RSA.\nBoth metrics show reduced absolute values (RSA $-3.6\\%$, $R^2$ $-7.6\\%$) as expected from halved data, but the non-monotonic profile shape is preserved.\n\n\\begin{table}[h]\n\\centering\n\\caption{Inverted-U stability under demonstration subsampling (trained image\\_mean).}\n\\label{tab:demo_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 50 demos & 25 demos & $\\Delta$ \\\\\n\\midrule\nRSA peak layer & L12 & L12 & 0 \\\\\nRSA peak $\\rho$ & 0.628 & 0.606 & $-3.6\\%$ \\\\\n$R^2$ peak layer & L9 & L11 & $+2$ \\\\\n$R^2$ peak value & 0.659 & 0.609 & $-7.6\\%$ \\\\\nRSA profile $r$ & --- & 0.970 & --- \\\\\n$R^2$ profile $r$ & --- & 0.819 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detailed Training Effects}\n\\label{sec:training_effects_appendix}\n\nTable~\\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\\Delta{=}+0.017$, $3\\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{RSA ($\\rho$)}} \\\\\nBest-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\\n\\quad (trained L12 vs.\\ untrained L0) & & & \\\\\nSame-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained vs.\\ untrained) & & & \\\\\nInstruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Probe $R^2$}} \\\\\nBest-vs-best image\\_mean & $+$0.015 & excl.\\ 0 & 0.006 \\\\\n\\quad (trained L8 vs.\\ untrained L0) & & & \\\\\nBest-vs-best readout & $+$0.069 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained L13 vs.\\ untrained L32) & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Training Effect Size Summary}\n\\label{sec:training_effect_summary}\n\nTable~\\ref{tab:training_effect_summary} consolidates training effects across all metrics.\nTraining effects on image\\_mean metrics are modest (RSA $\\Delta = +0.017$, $R^2$ $\\Delta = +0.015$), but effects on last\\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\\Delta = +0.069$).\nThis asymmetry indicates that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effect sizes across metrics. Image\\_mean effects are modest; last\\_preaction effects are large. Training targets readout-token information integration.}\n\\label{tab:training_effect_summary}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Trained & Untrained & $\\Delta$ \\\\\n\\midrule\nRSA peak (image\\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\\\\n$R^2$ peak (image\\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\\\\n$R^2$ peak (last\\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\\\\nInstruction routing L31 & 100\\% & 82\\% & $+$18pp \\\\\nInstruction attention L1 & 58\\% & 12\\% & $+$46pp \\\\\nProgress classification & 86.3\\% (L20) & 85.3\\% (L4) & $+$1pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Instruction Routing Probes}\n\\label{sec:routing_appendix}\n\n\\subsubsection{Cross-Instruction Classification: Dense Layer Profile}\n\\label{sec:dense_routing}\n\nTable~\\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.\nThe step-function onset between L0 ($10\\%$, chance) and L1 (${\\geq}99.6\\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\\sim}12\\%$) suffices for linear classification at L1.\nBoth pretrained and VLA-trained models sustain $100\\%$ through L31; only random initialization shows progressive decay ($82\\%$ at L31). Deep-layer stability thus derives from structured pretrained weights rather than task-specific fine-tuning.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8. Values reflect dense routing evaluation; main-text Table~\\ref{tab:dense_routing_main} reports sparse single-split results, yielding minor differences (e.g., L8: $98.2\\%$ vs.\\ $98.6\\%$).}\n\\label{tab:dense_routing}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained & Untrained & Image\\_mean (trained) \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL2 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL3 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL5 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL6 & 100.0\\% & 97.3\\% & 10.0\\% \\\\\nL7 & 100.0\\% & 96.4\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.6\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction LOOCV Validation}\n\\label{sec:loocv}\n\nLeave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) validates that the cross-instruction probe result is not driven by memorization.\nTrained last\\_preaction achieves $100\\% \\pm 0.00$ across all 10 folds at layers L1--L31 (perfect generalization).\n\n\\subsubsection{QA Probe: Progress and Subtask Classification}\n\\label{sec:qa_probe}\n\nTo test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train logistic regression probes (scikit-learn, $C = 1.0$, max\\_iter $= 1{,}000$) to classify task progress (4-class: each trajectory split into 4 equal temporal segments) and active subtask (binary: first vs.\\ second half) from frozen representations, with an 80/20 random train/test split (Table~\\ref{tab:qa_probe}).\n\n\\begin{table}[h]\n\\centering\n\\caption{QA probe accuracy (progress + subtask classification, best layer).}\n\\label{tab:qa_probe}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSource & Best Layer & Accuracy \\\\\n\\midrule\nTrained last\\_preaction & L20 & 86.3\\% \\\\\nUntrained last\\_preaction & L20 & 85.3\\% \\\\\nDINOv2 cls\\_token & --- & 82.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction Probe Profiles}\n\\label{sec:probe_profiles}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_probe_conditions.pdf}\n\\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\\%$ at L1, saturating to $100\\%$. Llama-2 base starts at $80.2\\%$, reaching $100\\%$ by L5. Untrained starts at $100\\%$ but decays to $82\\%$ by L31.}\n\\label{fig:probe_conditions_appendix}\n\\end{figure}\n\n\\subsubsection{Four-Condition Cross-Instruction Probe Profile}\n\\label{app:finetuned_probe}\n\nTable~\\ref{tab:finetuned_probe} extends the three-condition probe comparison (Table~\\ref{tab:dense_routing_main}) with the LIBERO-finetuned checkpoint.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy across four training conditions. Task-specific fine-tuning (LIBERO) preserves instruction decodability at all layers despite eliminating L31 exit-layer attention engagement (18$\\to$0 instruction-dominant heads).}\n\\label{tab:finetuned_probe}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & Untrained & Llama-2 base & OpenVLA-7B & LIBERO-finetuned \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 80.2\\% & 99.6\\% & 99.7\\% \\\\\nL8 & 98.6\\% & 99.9\\% & 100.0\\% & 100.0\\% \\\\\nL31 & 82.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{L1 Attention Pattern Analysis}\n\\label{sec:attention_pattern}\n\nFigure~\\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.\nThe three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_l1_stacked_bar.pdf}\n\\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\\%$ text attention). Llama-2 base: 9/32 heads ($36.5\\%$). Untrained: 0/32 heads ($11.7\\%$). See Table~\\ref{tab:routing_gradient} for quantitative comparison.}\n\\label{fig:attention_appendix}\n\\end{figure}\n\n\\subsubsection{Multi-Layer Attention Patterns}\n\\label{sec:multilayer_attention}\n\nTable~\\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\\ref{fig:attention_profile}, main text).\nThe full profile (Figure~\\ref{fig:multilayer_attention}) reveals three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_multi_layer_attn.pdf}\n\\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}\n\\label{fig:multilayer_attention}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\\ref{tab:routing_gradient}) due to threshold boundary effects.}\n\\label{tab:multilayer_attention}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{VLA Trained} & \\multicolumn{2}{c}{Llama-2 base} & \\multicolumn{2}{c}{Untrained} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\nLayer & Heads & Text\\% & Heads & Text\\% & Heads & Text\\% \\\\\n\\midrule\nL1 & \\textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\\\\nL8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\\\\nL16 & 10/32 & 48.4 & \\textbf{25/32} & 60.2 & 0/32 & 9.2 \\\\\nL31 & \\textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Threshold Sensitivity Analysis}\n\\label{sec:threshold_sensitivity}\n\nThe main text defines instruction-dominant heads as those allocating $>50\\%$ attention to instruction tokens.\nTable~\\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\\% to 70\\%; the 50\\% threshold is not a boundary-sensitive choice.\n\n\\begin{table}[h]\n\\centering\n\\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}\n\\label{tab:threshold_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nThreshold & VLA Trained & Llama-2 base & Untrained \\\\\n\\midrule\n30\\% & 32 & 13 & 0 \\\\\n40\\% & 31 & 10 & 0 \\\\\n50\\% & 24 & 9 & 0 \\\\\n60\\% & 9 & 4 & 0 \\\\\n70\\% & 5 & 3 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{L1 Attention Decomposition by Head Group}\n\\label{sec:attention_decomp}\n\nTable~\\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.\n\n\\begin{table}[h]\n\\centering\n\\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}\n\\label{tab:attention_decomp}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nHead Group & $N$ & Instruction & Vision & BOS/Other \\\\\n\\midrule\nInstruction-dominant & 24 & 62.4\\% & 18.8\\% & 18.8\\% \\\\\nControl & 8 & 44.9\\% & 27.1\\% & 28.0\\% \\\\\n\\midrule\n$\\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHead-level instruction attention entropy reaches $99.5\\%$ of the uniform maximum; routing is broadly distributed rather than concentrated in a few heads.\n\n\\paragraph{Per-token attention normalization.}\nThe $57.7\\%$ aggregate text attention in instruction-dominant heads partly reflects token-count imbalance (22 instruction vs.\\ 256 image tokens).\nPer-token normalization reveals a $38.2\\times$ ratio: each instruction token receives $38.2\\times$ the attention of each image token in trained instruction-dominant heads, compared to only $1.5\\times$ in untrained heads (a $25.5\\times$ increase from training).\nInstruction-dominant heads also show lower attention entropy ($0.465$) than non-dominant heads ($0.569$), indicating more concentrated attention distributions.\n\n\\subsection{Per-Dimension Action MAE Under Head Ablation}\n\\label{sec:per_dim_mae}\n\nTable~\\ref{tab:per_dim_mae} extends Table~\\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\\times$); instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\\times$) falls between the two groups.}\n\\label{tab:per_dim_mae}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDimension & Instr.\\ 24h MAE & Control 8h MAE & Ratio \\\\\n\\midrule\n$dx$ & 0.00189 & 0.00037 & 5.09$\\times$ \\\\\n$dy$ & 0.00531 & 0.00125 & 4.26$\\times$ \\\\\n$dz$ & 0.00762 & 0.00243 & 3.14$\\times$ \\\\\n$roll$ & 0.02059 & 0.00785 & 2.62$\\times$ \\\\\n$pitch$ & 0.03071 & 0.01387 & 2.21$\\times$ \\\\\n$yaw$ & 0.03388 & 0.01783 & 1.90$\\times$ \\\\\n$gripper$ & 0.29072 & 0.14072 & 2.07$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}\n\\label{sec:per_task_r2}\n\nTable~\\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\\Delta > 0$): instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\\Delta R^2 = +0.107$; the 50-demo setting (\\S\\ref{sec:learned_routing}) yields a consistent $+0.059$.}\n\\label{tab:per_task_r2}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTask & Baseline $R^2$ & Ablated $R^2$ & $\\Delta R^2$ \\\\\n\\midrule\nopen middle drawer & 0.197 & 0.221 & $+$0.024 \\\\\nopen top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\\\\npush plate to stove & 0.190 & 0.197 & $+$0.007 \\\\\nput bowl on plate & 0.375 & 0.474 & $+$0.099 \\\\\nput bowl on stove & 0.235 & 0.395 & $+$0.160 \\\\\nput bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\\\\nput cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\\\\nput wine on rack & 0.189 & 0.424 & $+$0.235 \\\\\nput wine on cabinet & 0.279 & 0.353 & $+$0.074 \\\\\nturn on stove & 0.385 & 0.421 & $+$0.036 \\\\\n\\midrule\nMean $\\pm$ std & $0.256 \\pm 0.070$ & $0.363 \\pm 0.088$ & $+$0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Task Complexity and Routing Dependence}\n\\label{sec:task_complexity}\n\nWe classify tasks as \\emph{instruction-discriminative} when multiple tasks share the same manipulated object(s), requiring instruction content to disambiguate the target action (e.g., ``put bowl on plate'' vs.\\ ``put bowl on stove''); remaining tasks involve unique object-action pairings recoverable from visual context alone.\nTable~\\ref{tab:task_complexity} reports per-task $|\\Delta R^2|$ under both groupings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Task-level L1 ablation effects ($|\\Delta R^2|$) grouped by instruction dependence. \\emph{Primary} (conservative): cream cheese in bowl classified as visual-sufficient ($2.5\\times$, $p = 0.033$). \\emph{Sensitivity} (shared-object criterion): cream cheese reclassified as instruction-discriminative ($6.5\\times$, $p = 0.008$).}\n\\label{tab:task_complexity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nTask & $|\\Delta R^2|$ & Group \\\\\n\\midrule\nput wine on rack & 0.235 & Instr-disc \\\\\nput bowl on cabinet & 0.201 & Instr-disc \\\\\nput bowl on stove & 0.160 & Instr-disc \\\\\nput bowl on plate & 0.099 & Instr-disc \\\\\nopen top drawer + bowl & 0.075 & Instr-disc \\\\\nput wine on cabinet & 0.074 & Instr-disc \\\\\n\\midrule\nput cream cheese in bowl$^\\dagger$ & 0.159 & Vis-suff \\\\\nturn on stove & 0.036 & Vis-suff \\\\\nopen middle drawer & 0.024 & Vis-suff \\\\\npush plate to stove & 0.007 & Vis-suff \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Primary}: Instr-disc mean $0.141$; Vis-suff mean $0.057$} \\\\\n\\multicolumn{3}{l}{Mann-Whitney $U = 21.0$, $p = 0.033$, ratio $= 2.49\\times$} \\\\\n\\multicolumn{3}{l}{\\textbf{Sensitivity}$^\\dagger$: cream cheese as Instr-disc: $p = 0.008$, $6.5\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Leave-one-out sensitivity.}\nAll leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.\nReclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).\n\n\\subsection{Specificity Control: Matched-Size Head Ablation}\n\\label{sec:specificity_control}\n\nTo test whether ablation effects are specific to instruction-dominant heads, we ablate four matched-size subsets of 24 heads at L1: instruction-dominant (highest instruction attention fraction), image-dominant (highest image attention fraction), random (5 seeds), and bottom-24 (lowest instruction attention fraction; overlaps 16/24 heads with the instruction-dominant group).\n\n\\begin{table}[h]\n\\centering\n\\caption{Matched-size ablation controls: trajectory disruption ($d$) from ablating 24-head subsets at L1, ranked by instruction attention fraction. Instruction-dominant heads produce the largest effect, but the modest gap ($8\\%$ over random) indicates distributed, attention-graded routing rather than a dedicated subset.}\n\\label{tab:specificity_control}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition (24 heads) & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\nInstruction-dominant & 0.650 & (reference) \\\\\nRandom (5 seeds) & $0.601 \\pm 0.021$ & $[0.568, 0.622]$ \\\\\nImage-dominant & 0.580 & $[0.547, 0.613]$ \\\\\nBottom-24 & 0.565 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll conditions yield comparable ground-truth MSE ($0.487$--$0.504$ vs.\\ baseline $0.497$), consistent with direction-selective rather than precision-degrading effects.\n",
      "numLines": 781,
      "startLine": 1,
      "totalLines": 781
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now I need to:

1. **Task 4**: Add the three-stage sentence to abstract.tex. The abstract currently has 7 lines. Let me find the best position. The sentence is about "Per-layer profiles suggest three functional stages: routing (L0--L1), computation (L8--L13), and decay (L14--L31)."

Looking at the abstract structure:
- Line 1: Introduction sentence
- Line 2: Method sentence
- Line 3: "Three findings emerge."
- Line 4: First finding (instruction routing)
- Line 5: Seven complementary analyses (supporting first finding)


- Line 6: Second finding (vision encoder)
- Line 7: Token-level analysis (supporting second finding)

The three-stage narrative is a high-level summary of the per-layer profiles that spans the entire layer profile - routing at L0-L1, computation at L8-L13, decay at L14-L31. This cross-cutting observation would fit best after line 5, before the second finding about the vision encoder, as it provides a natural transition between the first finding's support and the next major point.

Now I'm looking at where to place the bootstrap CI text in the appendix. The task complexity section is at line 720, and I need to find where the leave-one-out sensitivity paragraph fits within that section.

I can see the leave-one-out content wraps up around line 756, right before the next subsection begins at line 758. That's where I should insert the bootstrap CI paragraph.

For the abstract edits, I'm placing the three-stage narrative sentence between lines 5 and 6, right after the "Seven complementary analyses" line. This creates a natural flow from the routing finding into the broader context before moving to the vision encoder finding.

Let me verify the cross-reference is valid—yes, the label exists at line 721. Now I'll make both insertions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "cb3269be-55d5-406b-983c-6a08e834a6f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9Xvx1FiBqcDmscAeKuHZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18402,
      "cache_read_input_tokens": 23454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18402
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

找到了插入位置。两个编辑同时进行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "93308209-26ef-486e-a4ec-b89a7ee8fb31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9Xvx1FiBqcDmscAeKuHZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18402,
      "cache_read_input_tokens": 23454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18402
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

<details open><summary>🔧 Tool call — Edit · `toolu_01XhnRyTfmToA6YnzTAis2jA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex",
  "old_string": "Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).\nSecond, vision encoder representations",
  "new_string": "Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).\nPer-layer profiles suggest three functional stages: routing (L0--L1), computation (L8--L13), and decay (L14--L31).\nSecond, vision encoder representations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "fe786b0e-806b-4aef-8219-0f4d3128d15a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9Xvx1FiBqcDmscAeKuHZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18402,
      "cache_read_input_tokens": 23454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18402
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

_source line 13 · 2026-05-19T15:55:58.677Z_

<details><summary>↩ Tool result · `toolu_01XhnRyTfmToA6YnzTAis2jA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "3278e114-80e8-433f-bdfe-74b540f17e40",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex",
    "oldString": "Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).\nSecond, vision encoder representations",
    "newString": "Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).\nPer-layer profiles suggest three functional stages: routing (L0--L1), computation (L8--L13), and decay (L14--L31).\nSecond, vision encoder representations",
    "originalFile": "Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.\nWe decompose OpenVLA-7B across all 32 LLM layers using cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes, with factorial trained/pretrained/untrained controls on LIBERO.\nThree findings emerge.\nFirst, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).\nSeven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).\nSecond, vision encoder representations show a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training effects concentrated at the readout token ($R^2$ $+0.069$, attention $+46$pp) rather than visual geometry.\nToken-level analysis reveals strict functional specialization: image tokens remain instruction-blind across all 32 layers while the readout token serves as the primary multimodal integration site.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 5,
        "newStart": 3,
        "newLines": 6,
        "lines": [
          " Three findings emerge.",
          " First, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).",
          " Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).",
          "+Per-layer profiles suggest three functional stages: routing (L0--L1), computation (L8--L13), and decay (L14--L31).",
          " Second, vision encoder representations show a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training effects concentrated at the readout token ($R^2$ $+0.069$, attention $+46$pp) rather than visual geometry.",
          " Token-level analysis reveals strict functional specialization: image tokens remain instruction-blind across all 32 layers while the readout token serves as the primary multimodal integration site."
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

<details open><summary>🔧 Tool call — Edit · `toolu_013wZ6Es4YimG6QRqDZ7mGCW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "old_string": "\\paragraph{Leave-one-out sensitivity.}\nAll leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.\nReclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).\n\n\\subsection{Specificity Control: Matched-Size Head Ablation}",
  "new_string": "\\paragraph{Leave-one-out sensitivity.}\nAll leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.\nReclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).\n\nBootstrap 95\\% CI on the complex/simple ratio: $[1.03, 11.12]$ (10{,}000 resamples). The wide interval reflects low statistical power from $N=10$ tasks split into groups of 6 and 4; the point estimate ($2.5\\times$) is stable under leave-one-out analysis (all $p \\leq 0.083$; \\S\\ref{sec:task_complexity}).\n\n\\subsection{Specificity Control: Matched-Size Head Ablation}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "e011d4df-8707-46d4-8fbb-f1856294b237",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9Xvx1FiBqcDmscAeKuHZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18402,
      "cache_read_input_tokens": 23454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18402
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

_source line 15 · 2026-05-19T15:56:04.059Z_

<details><summary>↩ Tool result · `toolu_013wZ6Es4YimG6QRqDZ7mGCW`</summary>

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
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "7c04b615-1544-4b9f-b517-195a40ce8d91",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "oldString": "\\paragraph{Leave-one-out sensitivity.}\nAll leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.\nReclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).\n\n\\subsection{Specificity Control: Matched-Size Head Ablation}",
    "newString": "\\paragraph{Leave-one-out sensitivity.}\nAll leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.\nReclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).\n\nBootstrap 95\\% CI on the complex/simple ratio: $[1.03, 11.12]$ (10{,}000 resamples). The wide interval reflects low statistical power from $N=10$ tasks split into groups of 6 and 4; the point estimate ($2.5\\times$) is stable under leave-one-out analysis (all $p \\leq 0.083$; \\S\\ref{sec:task_complexity}).\n\n\\subsection{Specificity Control: Matched-Size Head Ablation}",
    "originalFile": "\\paragraph{Use of Generative AI.}\nGenerative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.\n\n\\appendix\n\n\\section{Supplementary Material}\n\\label{sec:appendix}\n\nUnless noted otherwise, all analyses use OpenVLA-7B (\\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).\nModel conditions, representation extraction, metric definitions, and probe architectures follow \\S\\ref{sec:setup}--\\S\\ref{sec:probes}.\nCross-benchmark experiments (\\S\\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\\times$ 50 demonstrations).\nAll experiments ran on 2$\\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs (96\\,GB each); random seed is 42 unless stated otherwise.\n\n\\subsection{CKA Analysis Method}\n\\label{sec:cka_appendix}\n\nWe employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA as a complementary perspective.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.\n\n\\subsection{Metric Sensitivity: RSA versus CKA}\n\\label{sec:metric_sensitivity_appendix}\n\nLinear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.\n\nAt the per-layer level, linear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), with no inverted-U pattern.\nRSA captures rank-order geometric alignment; CKA captures global linear structure.\nThe dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}\n\\label{fig:metric_comparison}\n\\end{figure}\n\n\\subsection{Branch-Split Detailed Analysis}\n\\label{sec:branch_split_appendix}\n\nTo disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.\nThe two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.\nFusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.\nThe MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.\n\n\\subsection{RSA Across Representation Sources}\n\\label{sec:rsa_bar_appendix}\n\nFigure~\\ref{fig:rsa_bar} shows RSA with the action space across all representation sources; the ordering matches Table~\\ref{tab:rsa_overview}.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n\\subsection{Per-Layer RSA Profiles}\n\\label{sec:rsa_perlayer_appendix}\n\nFigure~\\ref{fig:rsa_perlayer_curve} extends Figure~\\ref{fig:layer_curves} (main text) by adding readout and untrained profiles.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}\n\\caption{Per-layer RSA ($\\rho$) for trained and untrained models at image\\_mean and readout (last\\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\\_mean diverge: readout $\\rho$ declines gradually ($0.628 \\to 0.584$) while image\\_mean $\\rho$ drops sharply ($0.628 \\to 0.422$), consistent with task-specific conditioning at the readout position.}\n\\label{fig:rsa_perlayer_curve}\n\\end{figure}\n\n\\subsection{Per-Layer Action Decoding Across Training Stages}\n\\label{sec:action_r2_threecond}\n\nFigure~\\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\\pm$ std).\nAll three conditions share L0 representations ($R^2 = 0.645 \\pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.\nThe trained model peaks at L9 ($R^2 = 0.643 \\pm 0.014$), consistent with progressive specialization for action-relevant feature integration.\nLlama-2 base shows a steady decline (L0: $0.645 \\to$ L32: $0.551$, std $0.003$--$0.035$), consistent with stable but unspecialized processing.\nThe untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability indicates that randomly initialized Transformer layers produce destructive interference on action-relevant structure.\nThe three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.\nThe qualitative pattern is consistent across all 3 seeds.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_action_r2_threecond.pdf}\n\\caption{Per-layer action probe $R^2$ (image\\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \\pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\\pm$ std).}\n\\label{fig:action_r2_threecond}\n\\end{figure}\n\n\\subsection{Random-Subset Ablation Details}\n\\label{sec:random_subset_ablation}\n\nTo evaluate whether the ablation effect in \\S\\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).\nDominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \\pm 0.013$ (Figure~\\ref{fig:random_subset_ablation}).\nThe dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); heads with higher instruction-attention fraction carry more organized routing signals, consistent with graded rather than binary specialization.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_random_subset_ablation.pdf}\n\\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \\pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with graded routing specialization across L1 heads.}\n\\label{fig:random_subset_ablation}\n\\end{figure}\n\n\\subsection{Action Trajectory Analysis Details}\n\\label{sec:action_trajectory}\n\nTable~\\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.\nBoth conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).\nThe gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.\n\nPer-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).\nToken-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.\n\n\\paragraph{Trajectory-level aggregation.}\nAggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\\sim}4\\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).\nInstruction-head ablation ($N = 50$: 5 tasks $\\times$ 10 demos) yields trajectory $d = 2.943$ (95\\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).\nAll 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.\nCounterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).\nFine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\\sim} 1{,}500$) provide higher resolution for ordering claims.\n\n\\paragraph{Ground-truth action error.}\nAblation redirects model outputs ($d = 0.65$) but does not systematically increase error relative to expert demonstrations: original MSE $= 0.498$; top-24 instruction-head ablation MSE $= 0.497$ ($\\Delta = -0.001$, Wilcoxon $p = 0.52$, n.s.); bottom-24 non-instruction heads MSE $= 0.506$ ($\\Delta = +0.008$).\nChanges concentrate on the gripper dimension; translation and rotation dimensions are negligibly affected.\nPer-task breakdown shows all $|\\Delta\\text{MSE}| < 3\\%$ of baseline with all $p > 0.27$; the near-zero aggregate $\\Delta$ reflects uniformly small per-task effects rather than cancellation across tasks.\nThis is consistent with the information-computation dissociation: routing heads control instruction-specific direction selection rather than action precision.\n\nTable~\\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).\nIndividual control heads produce ${\\sim}1.9\\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.\nThe 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\\ $0.41$), consistent with collective coordination rather than individual strength.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}\n\\label{tab:perhead_bootstrap}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nGroup & $N$ heads & Collective $d$ & Per-head $d$ [95\\% CI] \\\\\n\\midrule\nInstruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\\\\nControl & 8 & 0.41 & 0.051 [0.048, 0.055] \\\\\n\\midrule\nDifference & --- & --- & 0.024, $p = 0.0018$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInstruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.\n\nTable~\\ref{tab:dose_response} and Figure~\\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.\nTrajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\\Delta d / \\Delta 4 \\approx 0.026$), a plateau at 16--20 heads ($\\Delta d = 0.001$), and slow increase at 20--32.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\\ original action sequence; 95\\% bootstrap CIs ($10{,}000$ resamples).}\n\\label{tab:dose_response}\n\\small\n\\begin{tabular}{rcc}\n\\toprule\nHeads ablated & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\n4 & 0.482 & [0.449, 0.511] \\\\\n8 & 0.508 & [0.479, 0.541] \\\\\n12 & 0.560 & [0.529, 0.593] \\\\\n16 & 0.592 & [0.559, 0.625] \\\\\n20 & 0.593 & [0.559, 0.627] \\\\\n24 & 0.611 & [0.578, 0.645] \\\\\n28 & 0.619 & [0.587, 0.654] \\\\\n32 & 0.639 & [0.603, 0.671] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$, token divergence (\\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \\text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}\n\\label{tab:counterfactual}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Jaccard & Cohen's $d$ & Token div.\\ (\\%) \\\\\n\\midrule\nEmpty (no instruction) & 0.000 & 0.968 & 90.7 \\\\\nWrong (different task) & 0.174 & 0.844 & 89.5 \\\\\nParaphrased & 0.533 & 0.697 & 82.6 \\\\\nShuffled (random order) & 1.000 & 0.625 & 85.7 \\\\\n\\midrule\nL1 ablation (24 heads) & --- & 0.650 & 72.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}\n\\label{tab:action_shift_perdim}\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\nCondition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\\\\n\\midrule\nInstruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\\\\nControl (8) & 0.000 & 0.001 & 0.002 & 0.008 & 0.014 & 0.018 & 0.141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pretrained LLM Representation Quality Under Visual Input}\n\\label{sec:ood_diagnostics}\n\nA potential concern with the three-condition comparison (\\S\\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.\nWe evaluate three diagnostics to assess representation quality.\nActivation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \\to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.\nPer-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\\approx 0.28$ at L25, consistent with gradual differentiation rather than catastrophic out-of-distribution behavior.\nTop-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.\nThese diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining (Figure~\\ref{fig:ood_diagnostics}). These results support the validity of the three-condition comparison.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ood_diagnostics.pdf}\n\\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics indicate structured, non-degenerate representations.}\n\\label{fig:ood_diagnostics}\n\\end{figure}\n\n\\subsection{Probe Architecture Sensitivity}\n\\label{sec:linear_probe}\n\nTo rule out that our findings depend on MLP probe capacity ($N/\\text{params} \\approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \\to 7$, $N/\\text{params} \\approx 2.2$).\nThe inverted-U pattern reproduces: trained image\\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).\nThe trained--untrained gap is larger under the linear probe (L14: $\\Delta = +0.324$) than the MLP probe (L8: $\\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.\nUntrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.\nFor last\\_preaction tokens, the linear probe also corroborates the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\\Delta = 0.103$ ($p < 0.001$).\nThese results indicate that our qualitative findings reflect representational structure rather than probe capacity artifacts (Figure~\\ref{fig:linear_vs_mlp}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}\n\\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}\n\\label{fig:linear_vs_mlp}\n\\end{figure}\n\n\\subsection{Functional Probe Comparison}\n\\label{sec:probe_bars_appendix}\n\nFigure~\\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\\_mean ($0.655$, L8) exceed the projector baseline ($0.630$); the inverted-U extends to functional capacity.}\n\\label{fig:probe_bars}\n\\end{figure}\n\n\\subsection{Training Effect and Instruction Invariance}\n\\label{sec:instruction_invariance_appendix}\n\nFigure~\\ref{fig:factorial} shows trained vs.\\ untrained RSA profiles and instruction invariance.\nInstruction invariance holds across all conditions: maximum $|\\Delta| < 0.006$, so action geometry is visually grounded and not modulated by language instructions.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\\Delta{=}+0.017$, $3\\%$). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$; action geometry is visually grounded.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Additional RSA Values}\n\\label{sec:additional_rsa}\n\nDINOv2 \\texttt{patch\\_mean} achieves RSA $\\rho = 0.631$, between the \\texttt{cls\\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).\nVLA untrained readout peaks at L1 ($\\rho = 0.626$).\n\n\\subsection{Cross-Benchmark Validation: LIBERO-Spatial}\n\\label{sec:cross_benchmark_appendix}\n\nTo assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks $\\times$ 50 demonstrations each, requiring spatial reasoning).\nFigure~\\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.\n\nThe inverted-U profile replicates on LIBERO-Spatial: trained image\\_mean RSA peaks at L14 ($\\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.\nTraining produces a significant geometric gain (best-vs-best $\\Delta = +0.023$, 95\\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\\Delta = +0.017$, CI includes zero).\n\nTwo notable differences emerge.\nFirst, the absolute RSA values are higher on Spatial ($0.691$ vs.\\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.\nSecond, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\\Delta_\\text{layer}| = 1$).\nThis suggests that peak convergence is benchmark-specific rather than a general consequence of training.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig7.pdf}\n\\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}\n\\label{fig:cross_benchmark}\n\\end{figure}\n\n\\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}\n\\label{sec:spatial_cross_instruction}\n\nTable~\\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.\nThe core pattern from LIBERO-Goal replicates: image\\_mean remains at chance (${\\sim}10\\%$) across all layers and conditions, while the trained readout token saturates to $100\\%$ by L4.\nThe untrained readout decays more steeply than on LIBERO-Goal ($75.4\\%$ at L31 vs.\\ $82\\%$), consistent with greater task difficulty.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\\%$ from L4; image\\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\\ Table~\\ref{tab:dense_routing_main}).}\n\\label{tab:spatial_cross_instruction}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nToken & Condition & L1 & L4 & L8 & L16 & L31 \\\\\n\\midrule\nlast\\_preaction & Trained & 98.9\\% & 100.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\nlast\\_preaction & Untrained & 99.5\\% & 98.3\\% & 85.7\\% & 68.3\\% & 75.4\\% \\\\\nimage\\_mean & Trained & 10.2\\% & 10.0\\% & 9.9\\% & 10.0\\% & 10.1\\% \\\\\nimage\\_mean & Untrained & 10.1\\% & 10.0\\% & 10.0\\% & 10.0\\% & 10.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness Analyses}\n\\label{sec:robustness_appendix}\n\n\\subsubsection{Distance Metric Invariance}\n\\label{sec:metric_invariance}\n\nThe inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\\ref{tab:metric_invariance}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}\n\\label{tab:metric_invariance}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Eucl.\\ Peak & Cos.\\ Peak & Profile $r$ \\\\\n\\midrule\nTrained image\\_mean & L12 & L12 & 0.990 \\\\\nTrained last\\_preaction & L12 & L13 & 0.990 \\\\\nUntrained image\\_mean & L0 & L0 & 0.995 \\\\\nUntrained last\\_preaction & L1 & L1 & 0.992 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Per-DOF Decomposition}\n\\label{sec:perdof}\n\nRSA decomposition by action dimension indicates the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\\rho = 0.193$), rotation (peak L12, $\\rho = 0.175$), and gripper (peak L13, $\\rho = 0.106$) all exhibit non-monotonic profiles.\nPer-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.\n\n\\subsubsection{Permutation Test}\n\\label{sec:permutation}\n\nPermutation testing (1{,}000 shuffles) indicates all observed RSA values are highly significant: observed $\\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).\n\n\\subsubsection{Probe Seed Sensitivity}\n\\label{sec:seed_sensitivity}\n\nAction probe $R^2$ is highly stable across random seeds.\nOver 5 seeds (trained image\\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\\%$ ($0.655 \\pm 0.002$; Table~\\ref{tab:seed_sensitivity}).\nPeak layer concentrates in the L8--L10 region ($4/5$ seeds); the inverted-U shape is not a seed artifact.\nSeed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe $R^2$ peak across 5 random seeds (trained image\\_mean).}\n\\label{tab:seed_sensitivity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSeed & Peak Layer & Peak $R^2$ \\\\\n\\midrule\n0 & L9 & 0.654 \\\\\n1 & L16 & 0.656 \\\\\n2 & L9 & 0.653 \\\\\n3 & L10 & 0.655 \\\\\n42 & L9 & 0.655 \\\\\n\\midrule\nMean$\\pm$std & $10.6\\pm2.7$ & $0.655\\pm0.002$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Demonstration Subsample Sensitivity}\n\\label{sec:demo_sensitivity}\n\nTo verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\\ref{tab:demo_sensitivity}).\nThe RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions (high stability).\nThe probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$; $R^2$ is more sensitive to training set size than RSA.\nBoth metrics show reduced absolute values (RSA $-3.6\\%$, $R^2$ $-7.6\\%$) as expected from halved data, but the non-monotonic profile shape is preserved.\n\n\\begin{table}[h]\n\\centering\n\\caption{Inverted-U stability under demonstration subsampling (trained image\\_mean).}\n\\label{tab:demo_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 50 demos & 25 demos & $\\Delta$ \\\\\n\\midrule\nRSA peak layer & L12 & L12 & 0 \\\\\nRSA peak $\\rho$ & 0.628 & 0.606 & $-3.6\\%$ \\\\\n$R^2$ peak layer & L9 & L11 & $+2$ \\\\\n$R^2$ peak value & 0.659 & 0.609 & $-7.6\\%$ \\\\\nRSA profile $r$ & --- & 0.970 & --- \\\\\n$R^2$ profile $r$ & --- & 0.819 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detailed Training Effects}\n\\label{sec:training_effects_appendix}\n\nTable~\\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\\Delta{=}+0.017$, $3\\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{RSA ($\\rho$)}} \\\\\nBest-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\\n\\quad (trained L12 vs.\\ untrained L0) & & & \\\\\nSame-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained vs.\\ untrained) & & & \\\\\nInstruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Probe $R^2$}} \\\\\nBest-vs-best image\\_mean & $+$0.015 & excl.\\ 0 & 0.006 \\\\\n\\quad (trained L8 vs.\\ untrained L0) & & & \\\\\nBest-vs-best readout & $+$0.069 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained L13 vs.\\ untrained L32) & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Training Effect Size Summary}\n\\label{sec:training_effect_summary}\n\nTable~\\ref{tab:training_effect_summary} consolidates training effects across all metrics.\nTraining effects on image\\_mean metrics are modest (RSA $\\Delta = +0.017$, $R^2$ $\\Delta = +0.015$), but effects on last\\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\\Delta = +0.069$).\nThis asymmetry indicates that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effect sizes across metrics. Image\\_mean effects are modest; last\\_preaction effects are large. Training targets readout-token information integration.}\n\\label{tab:training_effect_summary}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Trained & Untrained & $\\Delta$ \\\\\n\\midrule\nRSA peak (image\\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\\\\n$R^2$ peak (image\\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\\\\n$R^2$ peak (last\\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\\\\nInstruction routing L31 & 100\\% & 82\\% & $+$18pp \\\\\nInstruction attention L1 & 58\\% & 12\\% & $+$46pp \\\\\nProgress classification & 86.3\\% (L20) & 85.3\\% (L4) & $+$1pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Instruction Routing Probes}\n\\label{sec:routing_appendix}\n\n\\subsubsection{Cross-Instruction Classification: Dense Layer Profile}\n\\label{sec:dense_routing}\n\nTable~\\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.\nThe step-function onset between L0 ($10\\%$, chance) and L1 (${\\geq}99.6\\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\\sim}12\\%$) suffices for linear classification at L1.\nBoth pretrained and VLA-trained models sustain $100\\%$ through L31; only random initialization shows progressive decay ($82\\%$ at L31). Deep-layer stability thus derives from structured pretrained weights rather than task-specific fine-tuning.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8. Values reflect dense routing evaluation; main-text Table~\\ref{tab:dense_routing_main} reports sparse single-split results, yielding minor differences (e.g., L8: $98.2\\%$ vs.\\ $98.6\\%$).}\n\\label{tab:dense_routing}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained & Untrained & Image\\_mean (trained) \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL2 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL3 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL5 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL6 & 100.0\\% & 97.3\\% & 10.0\\% \\\\\nL7 & 100.0\\% & 96.4\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.6\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction LOOCV Validation}\n\\label{sec:loocv}\n\nLeave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) validates that the cross-instruction probe result is not driven by memorization.\nTrained last\\_preaction achieves $100\\% \\pm 0.00$ across all 10 folds at layers L1--L31 (perfect generalization).\n\n\\subsubsection{QA Probe: Progress and Subtask Classification}\n\\label{sec:qa_probe}\n\nTo test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train logistic regression probes (scikit-learn, $C = 1.0$, max\\_iter $= 1{,}000$) to classify task progress (4-class: each trajectory split into 4 equal temporal segments) and active subtask (binary: first vs.\\ second half) from frozen representations, with an 80/20 random train/test split (Table~\\ref{tab:qa_probe}).\n\n\\begin{table}[h]\n\\centering\n\\caption{QA probe accuracy (progress + subtask classification, best layer).}\n\\label{tab:qa_probe}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSource & Best Layer & Accuracy \\\\\n\\midrule\nTrained last\\_preaction & L20 & 86.3\\% \\\\\nUntrained last\\_preaction & L20 & 85.3\\% \\\\\nDINOv2 cls\\_token & --- & 82.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction Probe Profiles}\n\\label{sec:probe_profiles}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_probe_conditions.pdf}\n\\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\\%$ at L1, saturating to $100\\%$. Llama-2 base starts at $80.2\\%$, reaching $100\\%$ by L5. Untrained starts at $100\\%$ but decays to $82\\%$ by L31.}\n\\label{fig:probe_conditions_appendix}\n\\end{figure}\n\n\\subsubsection{Four-Condition Cross-Instruction Probe Profile}\n\\label{app:finetuned_probe}\n\nTable~\\ref{tab:finetuned_probe} extends the three-condition probe comparison (Table~\\ref{tab:dense_routing_main}) with the LIBERO-finetuned checkpoint.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy across four training conditions. Task-specific fine-tuning (LIBERO) preserves instruction decodability at all layers despite eliminating L31 exit-layer attention engagement (18$\\to$0 instruction-dominant heads).}\n\\label{tab:finetuned_probe}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & Untrained & Llama-2 base & OpenVLA-7B & LIBERO-finetuned \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 80.2\\% & 99.6\\% & 99.7\\% \\\\\nL8 & 98.6\\% & 99.9\\% & 100.0\\% & 100.0\\% \\\\\nL31 & 82.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{L1 Attention Pattern Analysis}\n\\label{sec:attention_pattern}\n\nFigure~\\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.\nThe three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_l1_stacked_bar.pdf}\n\\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\\%$ text attention). Llama-2 base: 9/32 heads ($36.5\\%$). Untrained: 0/32 heads ($11.7\\%$). See Table~\\ref{tab:routing_gradient} for quantitative comparison.}\n\\label{fig:attention_appendix}\n\\end{figure}\n\n\\subsubsection{Multi-Layer Attention Patterns}\n\\label{sec:multilayer_attention}\n\nTable~\\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\\ref{fig:attention_profile}, main text).\nThe full profile (Figure~\\ref{fig:multilayer_attention}) reveals three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_multi_layer_attn.pdf}\n\\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}\n\\label{fig:multilayer_attention}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\\ref{tab:routing_gradient}) due to threshold boundary effects.}\n\\label{tab:multilayer_attention}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{VLA Trained} & \\multicolumn{2}{c}{Llama-2 base} & \\multicolumn{2}{c}{Untrained} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\nLayer & Heads & Text\\% & Heads & Text\\% & Heads & Text\\% \\\\\n\\midrule\nL1 & \\textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\\\\nL8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\\\\nL16 & 10/32 & 48.4 & \\textbf{25/32} & 60.2 & 0/32 & 9.2 \\\\\nL31 & \\textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Threshold Sensitivity Analysis}\n\\label{sec:threshold_sensitivity}\n\nThe main text defines instruction-dominant heads as those allocating $>50\\%$ attention to instruction tokens.\nTable~\\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\\% to 70\\%; the 50\\% threshold is not a boundary-sensitive choice.\n\n\\begin{table}[h]\n\\centering\n\\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}\n\\label{tab:threshold_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nThreshold & VLA Trained & Llama-2 base & Untrained \\\\\n\\midrule\n30\\% & 32 & 13 & 0 \\\\\n40\\% & 31 & 10 & 0 \\\\\n50\\% & 24 & 9 & 0 \\\\\n60\\% & 9 & 4 & 0 \\\\\n70\\% & 5 & 3 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{L1 Attention Decomposition by Head Group}\n\\label{sec:attention_decomp}\n\nTable~\\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.\n\n\\begin{table}[h]\n\\centering\n\\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}\n\\label{tab:attention_decomp}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nHead Group & $N$ & Instruction & Vision & BOS/Other \\\\\n\\midrule\nInstruction-dominant & 24 & 62.4\\% & 18.8\\% & 18.8\\% \\\\\nControl & 8 & 44.9\\% & 27.1\\% & 28.0\\% \\\\\n\\midrule\n$\\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHead-level instruction attention entropy reaches $99.5\\%$ of the uniform maximum; routing is broadly distributed rather than concentrated in a few heads.\n\n\\paragraph{Per-token attention normalization.}\nThe $57.7\\%$ aggregate text attention in instruction-dominant heads partly reflects token-count imbalance (22 instruction vs.\\ 256 image tokens).\nPer-token normalization reveals a $38.2\\times$ ratio: each instruction token receives $38.2\\times$ the attention of each image token in trained instruction-dominant heads, compared to only $1.5\\times$ in untrained heads (a $25.5\\times$ increase from training).\nInstruction-dominant heads also show lower attention entropy ($0.465$) than non-dominant heads ($0.569$), indicating more concentrated attention distributions.\n\n\\subsection{Per-Dimension Action MAE Under Head Ablation}\n\\label{sec:per_dim_mae}\n\nTable~\\ref{tab:per_dim_mae} extends Table~\\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\\times$); instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\\times$) falls between the two groups.}\n\\label{tab:per_dim_mae}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDimension & Instr.\\ 24h MAE & Control 8h MAE & Ratio \\\\\n\\midrule\n$dx$ & 0.00189 & 0.00037 & 5.09$\\times$ \\\\\n$dy$ & 0.00531 & 0.00125 & 4.26$\\times$ \\\\\n$dz$ & 0.00762 & 0.00243 & 3.14$\\times$ \\\\\n$roll$ & 0.02059 & 0.00785 & 2.62$\\times$ \\\\\n$pitch$ & 0.03071 & 0.01387 & 2.21$\\times$ \\\\\n$yaw$ & 0.03388 & 0.01783 & 1.90$\\times$ \\\\\n$gripper$ & 0.29072 & 0.14072 & 2.07$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}\n\\label{sec:per_task_r2}\n\nTable~\\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\\Delta > 0$): instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\\Delta R^2 = +0.107$; the 50-demo setting (\\S\\ref{sec:learned_routing}) yields a consistent $+0.059$.}\n\\label{tab:per_task_r2}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTask & Baseline $R^2$ & Ablated $R^2$ & $\\Delta R^2$ \\\\\n\\midrule\nopen middle drawer & 0.197 & 0.221 & $+$0.024 \\\\\nopen top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\\\\npush plate to stove & 0.190 & 0.197 & $+$0.007 \\\\\nput bowl on plate & 0.375 & 0.474 & $+$0.099 \\\\\nput bowl on stove & 0.235 & 0.395 & $+$0.160 \\\\\nput bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\\\\nput cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\\\\nput wine on rack & 0.189 & 0.424 & $+$0.235 \\\\\nput wine on cabinet & 0.279 & 0.353 & $+$0.074 \\\\\nturn on stove & 0.385 & 0.421 & $+$0.036 \\\\\n\\midrule\nMean $\\pm$ std & $0.256 \\pm 0.070$ & $0.363 \\pm 0.088$ & $+$0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Task Complexity and Routing Dependence}\n\\label{sec:task_complexity}\n\nWe classify tasks as \\emph{instruction-discriminative} when multiple tasks share the same manipulated object(s), requiring instruction content to disambiguate the target action (e.g., ``put bowl on plate'' vs.\\ ``put bowl on stove''); remaining tasks involve unique object-action pairings recoverable from visual context alone.\nTable~\\ref{tab:task_complexity} reports per-task $|\\Delta R^2|$ under both groupings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Task-level L1 ablation effects ($|\\Delta R^2|$) grouped by instruction dependence. \\emph{Primary} (conservative): cream cheese in bowl classified as visual-sufficient ($2.5\\times$, $p = 0.033$). \\emph{Sensitivity} (shared-object criterion): cream cheese reclassified as instruction-discriminative ($6.5\\times$, $p = 0.008$).}\n\\label{tab:task_complexity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nTask & $|\\Delta R^2|$ & Group \\\\\n\\midrule\nput wine on rack & 0.235 & Instr-disc \\\\\nput bowl on cabinet & 0.201 & Instr-disc \\\\\nput bowl on stove & 0.160 & Instr-disc \\\\\nput bowl on plate & 0.099 & Instr-disc \\\\\nopen top drawer + bowl & 0.075 & Instr-disc \\\\\nput wine on cabinet & 0.074 & Instr-disc \\\\\n\\midrule\nput cream cheese in bowl$^\\dagger$ & 0.159 & Vis-suff \\\\\nturn on stove & 0.036 & Vis-suff \\\\\nopen middle drawer & 0.024 & Vis-suff \\\\\npush plate to stove & 0.007 & Vis-suff \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Primary}: Instr-disc mean $0.141$; Vis-suff mean $0.057$} \\\\\n\\multicolumn{3}{l}{Mann-Whitney $U = 21.0$, $p = 0.033$, ratio $= 2.49\\times$} \\\\\n\\multicolumn{3}{l}{\\textbf{Sensitivity}$^\\dagger$: cream cheese as Instr-disc: $p = 0.008$, $6.5\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Leave-one-out sensitivity.}\nAll leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.\nReclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).\n\n\\subsection{Specificity Control: Matched-Size Head Ablation}\n\\label{sec:specificity_control}\n\nTo test whether ablation effects are specific to instruction-dominant heads, we ablate four matched-size subsets of 24 heads at L1: instruction-dominant (highest instruction attention fraction), image-dominant (highest image attention fraction), random (5 seeds), and bottom-24 (lowest instruction attention fraction; overlaps 16/24 heads with the instruction-dominant group).\n\n\\begin{table}[h]\n\\centering\n\\caption{Matched-size ablation controls: trajectory disruption ($d$) from ablating 24-head subsets at L1, ranked by instruction attention fraction. Instruction-dominant heads produce the largest effect, but the modest gap ($8\\%$ over random) indicates distributed, attention-graded routing rather than a dedicated subset.}\n\\label{tab:specificity_control}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition (24 heads) & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\nInstruction-dominant & 0.650 & (reference) \\\\\nRandom (5 seeds) & $0.601 \\pm 0.021$ & $[0.568, 0.622]$ \\\\\nImage-dominant & 0.580 & $[0.547, 0.613]$ \\\\\nBottom-24 & 0.565 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll conditions yield comparable ground-truth MSE ($0.487$--$0.504$ vs.\\ baseline $0.497$), consistent with direction-selective rather than precision-degrading effects.\n",
    "structuredPatch": [
      {
        "oldStart": 755,
        "oldLines": 6,
        "newStart": 755,
        "newLines": 8,
        "lines": [
          " All leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.",
          " Reclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).",
          " ",
          "+Bootstrap 95\\% CI on the complex/simple ratio: $[1.03, 11.12]$ (10{,}000 resamples). The wide interval reflects low statistical power from $N=10$ tasks split into groups of 6 and 4; the point estimate ($2.5\\times$) is stable under leave-one-out analysis (all $p \\leq 0.083$; \\S\\ref{sec:task_complexity}).",
          "+",
          " \\subsection{Specificity Control: Matched-Size Head Ablation}",
          " \\label{sec:specificity_control}",
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

_source line 16_

编译验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "17244b60-a209-4d30-9f16-8f7b08782473",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCAB88wLJNfckSnqxAgMjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1860,
      "cache_read_input_tokens": 41856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1860
      },
      "output_tokens": 1,
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

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_014p9yyYoeExLdES7U2k8FqW`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && latexmk -pdf main.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper",
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
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "bb56d675-4635-43f9-b9ff-7fed75728134",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCAB88wLJNfckSnqxAgMjd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1860,
      "cache_read_input_tokens": 41856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1860
      },
      "output_tokens": 1,
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

_source line 18 · 2026-05-19T15:56:10.918Z_

<details><summary>↩ Tool result · `toolu_014p9yyYoeExLdES7U2k8FqW`</summary>

```text
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr
i8a.pfb>
Output written on main.pdf (27 pages, 566280 bytes).
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
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "d834a66b-418d-4d0c-8d3d-435da4f867f3",
  "tool_use_result": {
    "stdout": "0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr\ni8a.pfb>\nOutput written on main.pdf (27 pages, 566280 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01KYoUkZVHrz2r7MHJC1yYk6`</summary>

```json
{
  "command": "grep -c \"^!\" main.log; echo \"---\"; grep \"Output written\" main.log | tail -1",
  "description": "Check for LaTeX errors and page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "6ccf3238-9418-454e-ab00-41cba6829a50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZH5pDYbuF5udYFburhsdU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 41856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2461
      },
      "output_tokens": 65,
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

_source line 20 · 2026-05-19T15:56:14.538Z_

<details><summary>↩ Tool result · `toolu_01KYoUkZVHrz2r7MHJC1yYk6`</summary>

```text
0
---
Output written on main.pdf (27 pages, 566280 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "8d062cff-75a3-4508-8ced-8311b59d712f",
  "tool_use_result": {
    "stdout": "0\n---\nOutput written on main.pdf (27 pages, 566280 bytes).",
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

_source line 21_

检查正文页数（不含 appendix/references）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "7a0d4ad2-306d-43ef-8808-7eee80577183",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012w3GPBtKAsVPELgT2ma9iC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 134,
      "cache_read_input_tokens": 44317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 134
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

<details open><summary>🔧 Tool call — Bash · `toolu_01F7bPiayqGMKppFmCDVqGKY`</summary>

```json
{
  "command": "grep -n '\\\\appendix\\|\\\\bibliography' main.tex 2>/dev/null || grep -rn '\\\\appendix\\|\\\\bibliography' *.tex | head -5",
  "description": "Find appendix/bibliography boundaries for page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "8c78f472-6cd2-48ba-8c71-d0ed3d319d67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012w3GPBtKAsVPELgT2ma9iC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 134,
      "cache_read_input_tokens": 44317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 134
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

_source line 23 · 2026-05-19T15:56:19.371Z_

<details><summary>↩ Tool result · `toolu_01F7bPiayqGMKppFmCDVqGKY`</summary>

```text
41:\bibliography{references}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "2d49d14a-6dee-490e-89b5-ae1a5ac9a6da",
  "tool_use_result": {
    "stdout": "41:\\bibliography{references}",
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

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01Kz4nimykotRLa5Fo3encwH`</summary>

```json
{
  "command": "pdftotext main.pdf - 2>/dev/null | grep -n \"Supplementary Material\\|References\\|REFERENCES\" | head -5",
  "description": "Find where appendix/references start in PDF text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "85a27159-efaf-4fd3-a894-394bdcd5bb59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7P4rJD5YWuDKFA9cDBCX7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 44451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 256
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

_source line 25 · 2026-05-19T15:56:23.549Z_

<details><summary>↩ Tool result · `toolu_01Kz4nimykotRLa5Fo3encwH`</summary>

```text
947:References
1266:Supplementary Material
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "c7f51075-efa6-4299-badf-a7ceb381008f",
  "tool_use_result": {
    "stdout": "947:References\n1266:Supplementary Material",
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

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_013Zo3zjBLsoCJJotL6inuw3`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', 'main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo main.pdf 2>/dev/null",
  "description": "Get PDF info for page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "2f46b182-ffbc-49ac-9b7d-eb66ecabe057",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKwaoUUzTGn5jFMEcWCaqo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 135,
      "cache_read_input_tokens": 44707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 135
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

_source line 27 · 2026-05-19T15:56:27.389Z_

<details><summary>↩ Tool result · `toolu_013Zo3zjBLsoCJJotL6inuw3`</summary>

```text
Title:           
Subject:         Proceedings of the 10th Conference on Robot Learning (CoRL 2026)
Keywords:        
Author:          Anonymous Submission
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Tue May 19 15:56:09 2026 UTC
ModDate:         Tue May 19 15:56:09 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           27
Encrypted:       no
Page size:       612 x 792 pts (letter)
Page rot:        0
File size:       566280 bytes
Optimized:       no
PDF version:     1.7
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "60cfaca8-dd6b-458e-b361-e249b5418938",
  "tool_use_result": {
    "stdout": "Title:           \nSubject:         Proceedings of the 10th Conference on Robot Learning (CoRL 2026)\nKeywords:        \nAuthor:          Anonymous Submission\nCreator:         LaTeX with hyperref\nProducer:        pdfTeX-1.40.28\nCreationDate:    Tue May 19 15:56:09 2026 UTC\nModDate:         Tue May 19 15:56:09 2026 UTC\nCustom Metadata: yes\nMetadata Stream: no\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           27\nEncrypted:       no\nPage size:       612 x 792 pts (letter)\nPage rot:        0\nFile size:       566280 bytes\nOptimized:       no\nPDF version:     1.7",
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ph97hdypBMEUXM9uY6mPc5`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\ntext = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True).stdout\npages = text.split('\\x0c')\n# Find which page has 'References' or 'Supplementary Material'\nfor i, page in enumerate(pages):\n    if 'References' in page and i > 3:\n        print(f'References starts on page {i+1}')\n        break\nfor i, page in enumerate(pages):\n    if 'Supplementary Material' in page:\n        print(f'Appendix starts on page {i+1}')\n        break\n\"",
  "description": "Determine main body page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "8a28a540-514a-46c5-9e1c-c87efd79423e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5obQND9UZncADg6UV5Ub4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 345,
      "cache_read_input_tokens": 44842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 345
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

_source line 29 · 2026-05-19T15:56:33.066Z_

<details><summary>↩ Tool result · `toolu_01Ph97hdypBMEUXM9uY6mPc5`</summary>

```text
References starts on page 8
Appendix starts on page 12
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "12643c90-a0a8-4341-bd31-e2e9e3d32026",
  "tool_use_result": {
    "stdout": "References starts on page 8\nAppendix starts on page 12",
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

_source line 30_

正文 7 页（References 从第 8 页开始），在 CoRL 8 页限制内。

编译 0 errors，27 页 PDF，正文 7 页（≤8）。

**修改汇总：**

| 任务 | 文件 | 位置 | 内容 |
|------|------|------|------|
| 4 | `abstract.tex:6` | "Seven complementary analyses..." 之后、"Second, vision encoder..." 之前 | 插入 three-stage sentence |
| 5 | `appendix.tex:757-758` | `\subsection{Task Complexity}` 末尾，leave-one-out 段落之后 | 插入 bootstrap CI 段落 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "uuid": "74eedc89-d7d3-419b-aad0-8909f71cbade",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011QhsFmmzm7K9WpzrEH7Nin",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 45187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 259
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

_source line 31_

正文 7 页（References 从第 8 页开始），在 CoRL 8 页限制内。

编译 0 errors，27 页 PDF，正文 7 页（≤8）。

**修改汇总：**

| 任务 | 文件 | 位置 | 内容 |
|------|------|------|------|
| 4 | `abstract.tex:6` | "Seven complementary analyses..." 之后、"Second, vision encoder..." 之前 | 插入 three-stage sentence |
| 5 | `appendix.tex:757-758` | `\subsection{Task Complexity}` 末尾，leave-one-out 段落之后 | 插入 bootstrap CI 段落 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 75118,
  "duration_api_ms": 73300,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "3451cbc6-2036-4d16-acb2-51b1c4b2730e",
  "total_cost_usd": 0.47259275000000006,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 35465,
    "cache_read_input_tokens": 342511,
    "output_tokens": 3126,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35465,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 199,
        "cache_read_input_tokens": 45187,
        "cache_creation_input_tokens": 259,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 259
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1386,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001476,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 3126,
      "cacheReadInputTokens": 342511,
      "cacheCreationInputTokens": 35465,
      "webSearchRequests": 0,
      "costUSD": 0.47111675000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a7cd4361-ac69-4b3c-8405-87e7c99743b1"
}
```

</details>

---
