# paper fig1 dual and taskdep move

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/workers/worker_paper_fig1_dual_and_taskdep_move_20260519T155504.log`
- **Structured JSON:** [`e7512982d467f4329771.json`](../../sessions/e7/e7512982d467f4329771.json)

## Before a recorded user message

60 recorded events

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
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
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
  "uuid": "9281aa24-4a1b-44dd-a3d2-225522d54f17",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

I'll start by reading the relevant files to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "3ccdf45c-3015-463a-b264-d1c06b724ac6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZLHBL6TwmRAwEY5djQcmy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12152,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12152
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

_source line 4_

<details open><summary>🔧 Tool call — Read · `toolu_01D2cK5nvPxDA21d33hTsXH3`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "16e571af-f7e7-439a-8112-f5ac78fceb24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZLHBL6TwmRAwEY5djQcmy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12152,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12152
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

_source line 5 · 2026-05-19T15:55:20.019Z_

<details><summary>↩ Tool result · `toolu_01D2cK5nvPxDA21d33hTsXH3`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "d5724f8e-4b4a-4ae3-937a-7c55ee01328d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe evaluate OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\\cite{liu2023_libero} (10 tasks, 50 demonstrations each).\nRepresentations are extracted from six sources spanning the VLA pipeline (\\S\\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\\_mean and readout tokens at each of 32 layers, DINOv2~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}), CLIP~\\cite{radford2021_clip} (\\texttt{patch\\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).\nThree LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\\S\\ref{sec:model_data}).\nRSA computes Spearman $\\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\\S\\ref{sec:rsa}).\nMLP probes (input $\\to$ 256 $\\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\\S\\ref{sec:probes}).\nThis yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); RSA uses task-level blocking ($N_\\text{eff} = 10$) and probes use demo-level train/test splits.\nAll patterns reproduce with a linear probe (Appendix~\\ref{sec:linear_probe}).\n\n%------------------------------------------------------------------\n\\subsection{Framework Validation: Token-Level Specialization}\n\\label{sec:token_specialization}\n\nAs a sanity check on the experimental framework, we train cross-instruction probes (\\S\\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.\n\n\\paragraph{Image tokens are instruction-blind (expected).}\nAs predicted by the causal mask and frozen encoder, image\\_mean instruction classification remains at chance ($10\\%$) across all 32 layers in all conditions (Table~\\ref{tab:dense_routing_main}).\nBoth linear and MLP probes corroborate this, as does standalone DINOv2 ($10\\%$; Appendix~\\ref{sec:instruction_invariance_appendix}).\n\n\\paragraph{Readout token as multimodal hub.}\nTrained readout achieves $100\\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\\ref{sec:loocv}); untrained achieves $100\\%$ at L1 but decays to $82\\%$ by L31.\nThe readout is thus the primary locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\\%$ vs.\\ $82.7\\%$; Appendix~\\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\\ref{sec:cross_benchmark_appendix}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-instruction 10-way classification at selected layers (full profile in Appendix~\\ref{sec:dense_routing}). Image\\_mean remains at chance ($10\\%$) in all conditions; trained readout reaches $100\\%$ at L1 and holds; untrained readout decays from L1 to L31.}\n\\label{tab:dense_routing_main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained readout & Untrained readout & Image\\_mean \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL16 & 100.0\\% & 92.3\\% & 10.0\\% \\\\\nL31 & 100.0\\% & 82.0\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}\n\\label{sec:learned_routing}\n\n\\paragraph{Three-level routing gradient at L1.}\nWe compare L1 readout attention across three conditions (Table~\\ref{tab:routing_gradient}; Figure~\\ref{fig:attention_profile}): untrained networks allocate 0/32 instruction-dominant heads ($11.7\\%$ text); Llama-2 base 9/32 ($36.5\\%$); VLA fine-tuning 24/32 ($57.7\\%$), a redistribution beyond inherited priors.\nPer-token normalization ($38.2\\times$ text-to-image ratio; Appendix~\\ref{sec:attention_decomp}) corroborates this redistribution.\n\n\\paragraph{Redistribution of routing across depth.}\nThe 32-layer profile (Figure~\\ref{fig:attention_profile}) shows qualitatively distinct patterns.\nLlama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).\nVLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30).\nHead counts reflect single-sample extraction; threshold sensitivity (30\\%--70\\%) analysis confirms ordering robustness across classification boundaries (Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Task-specific sharpening.}\nA fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\\ 6--11), an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute.\nProbe accuracy is preserved (L1: $99.7\\%$; Appendix~\\ref{app:finetuned_probe}).\n\n\\paragraph{Probe robustness corroborates the pattern.}\nCross-instruction probes corroborate the three-condition gradient (Appendix Figure~\\ref{fig:probe_conditions_appendix}).\nTraining effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\\_mean changes minimally ($\\Delta \\leq 1.7\\%$; Appendix~\\ref{sec:training_effect_summary},~\\ref{sec:action_r2_threecond}).\n\n\\paragraph{Open-loop functional sensitivity.}\nWe ablate attention to instruction tokens at the readout position.\nAblating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\\footnote{$R^2$ values differ from Table~\\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.\nWe compare against 10 random subsets of 24 heads (Appendix~\\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \\pm 0.013$ ($z = -2.73$, $p = 0.003$).\nDominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.\nIn the original extraction pipeline (\\S\\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\\Delta \\approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\\ref{tab:per_task_r2}).\n\n\\paragraph{Action trajectory validation.}\nAblating 24 instruction-dominant heads alters $72.3\\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\\%$), concentrated on the gripper dimension (shift $0.291$ vs.\\ $< 0.034$; Tables~\\ref{tab:attention_decomp},~\\ref{tab:per_dim_mae}; Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Dose-response gradient.}\nAblating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \\to 0.639$; Figure~\\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Counterfactual instruction analysis.}\nReplacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\\ref{tab:counterfactual}).\nToken novelty ($1 - \\text{Jaccard}$) predicts the ordering ($\\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.\nL1 ablation ($d = 0.65$) falls within this range (Appendix~\\ref{sec:action_trajectory}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\\% vs.\\ 100.0\\% in Table~\\ref{tab:dense_routing_main}): task-level vs.\\ LOOCV splits.}\n\\label{tab:routing_gradient}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Heads & Text attn & L1 acc & L31 acc & Mode \\\\\n\\midrule\nVLA Trained & 24/32 & 57.7\\% & 99.6\\% & 100.0\\% & immed.+stable \\\\\nLlama-2 base & 9/32 & 36.5\\% & 80.2\\% & 100.0\\% & gradual+stable \\\\\nUntrained & 0/32 & 11.7\\% & 100.0\\% & 82.0\\% & incid.+forget \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_32layer_attention.pdf}\n\\caption{Instruction-dominant heads ($>50\\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\\ref{fig:probe_conditions_appendix}.}\n\\label{fig:attention_profile}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}\n\\label{sec:nonmonotonic}\n\n\\paragraph{Vision encoder provides geometric foundation.}\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ and probe $R^2$ between representations and actions.\nDINOv2 \\texttt{cls\\_token} achieves the highest RSA ($\\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\\ref{sec:cka_appendix}).\n\n\\paragraph{Middle-layer peak (metric-dependent).}\nUnder RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\\_mean $\\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).\nThe readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\\Delta = 0.048$ (Table~\\ref{tab:rsa_overview}).\nUnder linear CKA, this pattern disappears (monotonic increase; Appendix~\\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.\n\n\\paragraph{Training primarily enhances readout decodability.}\nBest-vs-best RSA gain is non-significant on LIBERO-Goal ($\\Delta\\rho = 0.017$, $3\\%$, $N{=}10$ tasks; Appendix Table~\\ref{tab:training_effects}), though LIBERO-Spatial yields a significant geometric gain ($\\Delta = +0.023$, $p < 0.001$; Appendix~\\ref{sec:cross_benchmark_appendix}).\nThe $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.\nFunctional improvements are larger: readout $R^2$ $\\Delta = +0.069$ ($p < 0.0001$, 95\\% CI $[0.047, 0.090]$), image\\_mean $\\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA $\\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\\ref{sec:cka_appendix}). VLA rows: peak values. \\textbf{Bold}: best; \\underline{underline}: second.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSource & RSA $\\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\\\\n\\midrule\nDINOv2 cls\\_token & \\textbf{0.692} & 0.634 & --- & --- \\\\\nVLA Trained readout & \\underline{0.643} & \\textbf{0.678} & L12 & L13 \\\\\nFused DinoSigLIP & 0.634 & --- & --- & --- \\\\\nVLA Trained image\\_mean & 0.628 & \\underline{0.655} & L12 & L8--L10$^\\dagger$ \\\\\nDinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\\\\nVLA Untrained image\\_mean & 0.612 & 0.640 & L0 & L0 \\\\\nVLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\\\\nCLIP ViT-L/14$^\\ddagger$ & 0.557 & 0.587 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$$R^2$ peak region across 5 seeds ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).} \\\\\n\\multicolumn{5}{l}{\\footnotesize $^\\ddagger$RSA uses \\texttt{patch\\_mean}; $R^2$ uses \\texttt{cls\\_token} (each encoder's best aggregation).}\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$). Trained image\\_mean follows an inverted-U (L0 $0.612 \\to$ L12 $0.628 \\to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}\n\\label{fig:layer_curves}\n\\end{figure}\n",
      "numLines": 158,
      "startLine": 1,
      "totalLines": 158
    }
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01T3HbrvPTSbEe1CnADZBF25`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "d42c22c5-efcd-4884-9962-7c7f7cbc26c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZLHBL6TwmRAwEY5djQcmy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12152,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12152
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

_source line 7 · 2026-05-19T15:55:20.328Z_

<details><summary>↩ Tool result · `toolu_01T3HbrvPTSbEe1CnADZBF25`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains Grant et al.'s~\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Seven analyses support distributed L1 routing: \emph{interventional} (dose-response, $d = 0.48 \to 0.64$; counterfactual, $d = 0.63$--$0.97$), \emph{supporting} (attention gradient $0 \to 9 \to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\times$).
8	
9	\paragraph{Mechanistic interpretation.}
10	Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\text{rand}}=5$ seeds).
11	Counterfactual ordering follows token novelty ($\rho = 1.0$; \S\ref{sec:learned_routing}).
12	That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\Delta\text{MSE} \approx 0$; Appendix~\ref{sec:action_trajectory}) reflects an information-computation dissociation~\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.
13	
14	\paragraph{Functional stages and predictions.}
15	Per-layer profiles suggest three stages: routing (L0--L1; probe $99.6\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\sim}56\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).
16	Task-specific fine-tuning eliminates L31 re-engagement (18 $\to$ 0 heads; \S\ref{sec:learned_routing}), consistent with exit routing serving multi-task flexibility, though this $N=2$ comparison (OXE 970K vs.\ LIBERO 500) may also reflect data diversity differences.
17	Predictions: cross-attention VLAs ($\pi_0$~\cite{black2024_pi0}, Octo~\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.
18	
19	\paragraph{Task-dependent routing.}
20	The routing effect is task-dependent: instruction-discriminative tasks show $2.5\times$ larger $|\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\ref{tab:task_complexity}), rising to $6.5\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\ref{sec:task_complexity}).
21	For deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.
22	
23	\paragraph{Limitations and scope.}
24	We study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\ref{sec:ood_diagnostics},~\ref{sec:cka_appendix}).
25	Llama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.
26	All analyses are open-loop; our routing analysis (\emph{where}) complements H\"aon et al.'s~\cite{haon2025} (\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "7aa8b761-f8e2-4df7-83c2-515d4fe9a013",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains Grant et al.'s~\\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven analyses support distributed L1 routing: \\emph{interventional} (dose-response, $d = 0.48 \\to 0.64$; counterfactual, $d = 0.63$--$0.97$), \\emph{supporting} (attention gradient $0 \\to 9 \\to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\\times$).\n\n\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds).\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.\n\n\\paragraph{Functional stages and predictions.}\nPer-layer profiles suggest three stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).\nTask-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads; \\S\\ref{sec:learned_routing}), consistent with exit routing serving multi-task flexibility, though this $N=2$ comparison (OXE 970K vs.\\ LIBERO 500) may also reflect data diversity differences.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}\nWe study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\\ref{sec:ood_diagnostics},~\\ref{sec:cka_appendix}).\nLlama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.\nAll analyses are open-loop; our routing analysis (\\emph{where}) complements H\\\"aon et al.'s~\\cite{haon2025} (\\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.\n",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01AssGMiwGJuvhXyGrUai8Wb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "5751f94d-6545-4fb9-8e2f-09ac693e969b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZLHBL6TwmRAwEY5djQcmy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12152,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12152
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

_source line 9 · 2026-05-19T15:55:21.553Z_

<details><summary>↩ Tool result · `toolu_01AssGMiwGJuvhXyGrUai8Wb`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.
6	Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, RSA~\cite{kriegeskorte2008} for geometric alignment, and MLP probes~\cite{alain2017} for functional decodability.
15	
16	Three findings emerge from our analysis of OpenVLA-7B on LIBERO.
17	\emph{First}, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads).
18	Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\times$ stronger for instruction-discriminative tasks ($p = 0.033$).
19	\emph{Second}, under RSA and action-probe decodability, vision encoder representations show a middle-layer peak ($R^2$ at L8--L14, RSA at L12), but this pattern is metric-dependent (CKA diverges; Appendix~\ref{sec:cka_appendix}).
20	Training yields substantial functional improvement at the readout ($R^2$ $\Delta = +0.069$, $p < 0.0001$) with limited geometric gain ($\Delta\rho = 0.017$ on LIBERO-Goal; significant on LIBERO-Spatial, $p < 0.001$).
21	Architecture-expected token specialization (instruction-blind image tokens, perfect readout classification from L1) is empirically verified as a framework sanity check (\S\ref{sec:token_specialization}).
22	
23	Our contributions are: (i)~evidence from seven complementary analyses that VLA fine-tuning front-loads instruction routing from mid-depth to entry-exit, with L1 as the primary routing hub and routing dependence modulated by task instruction-discriminability; (ii)~the observation that vision encoder representations follow a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training primarily enhancing readout-token integration; and (iii)~a systematic framework for token-level representational analysis of VLAs with factorial controls.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "b64f9359-ab16-4be3-8388-5bcf8c131933",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWhat does fine-tuning change inside a Vision-Language-Action model (VLA)?\nVLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.\nInstruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.\n\nRecent behavioral studies reveal that VLAs rely disproportionately on visual input~\\cite{grant2026}, with language instructions largely ignored by the action pathway~\\cite{haon2025}.\nThese findings suggest internal specialization but do not explain \\emph{how} instruction information reaches the action-generating readout token, \\emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \\emph{whether} training creates new representational structure or reconfigures inherited geometry.\nExisting analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.\n\nWe address this gap by decomposing OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\\cite{touvron2023_llama2}.\nWe extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\\cite{oquab2024_dinov2}, CLIP~\\cite{radford2021_clip}).\nWe compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, RSA~\\cite{kriegeskorte2008} for geometric alignment, and MLP probes~\\cite{alain2017} for functional decodability.\n\nThree findings emerge from our analysis of OpenVLA-7B on LIBERO.\n\\emph{First}, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads).\nSeven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).\n\\emph{Second}, under RSA and action-probe decodability, vision encoder representations show a middle-layer peak ($R^2$ at L8--L14, RSA at L12), but this pattern is metric-dependent (CKA diverges; Appendix~\\ref{sec:cka_appendix}).\nTraining yields substantial functional improvement at the readout ($R^2$ $\\Delta = +0.069$, $p < 0.0001$) with limited geometric gain ($\\Delta\\rho = 0.017$ on LIBERO-Goal; significant on LIBERO-Spatial, $p < 0.001$).\nArchitecture-expected token specialization (instruction-blind image tokens, perfect readout classification from L1) is empirically verified as a framework sanity check (\\S\\ref{sec:token_specialization}).\n\nOur contributions are: (i)~evidence from seven complementary analyses that VLA fine-tuning front-loads instruction routing from mid-depth to entry-exit, with L1 as the primary routing hub and routing dependence modulated by task instruction-discriminability; (ii)~the observation that vision encoder representations follow a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training primarily enhancing readout-token integration; and (iii)~a systematic framework for token-level representational analysis of VLAs with factorial controls.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01WT5BUt1MvfSUtNLMFeiwEp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "limit": 180,
  "offset": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "b9822812-af24-4733-a432-c9039215c0d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZLHBL6TwmRAwEY5djQcmy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12152,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12152
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

_source line 11 · 2026-05-19T15:55:21.849Z_

<details><summary>↩ Tool result · `toolu_01WT5BUt1MvfSUtNLMFeiwEp`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "9e5ec6e6-a9bb-4762-a1a5-a823bb93dc55",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
      "content": "\\end{table}\n\nInstruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.\n\nTable~\\ref{tab:dose_response} and Figure~\\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.\nTrajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\\Delta d / \\Delta 4 \\approx 0.026$), a plateau at 16--20 heads ($\\Delta d = 0.001$), and slow increase at 20--32.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\\ original action sequence; 95\\% bootstrap CIs ($10{,}000$ resamples).}\n\\label{tab:dose_response}\n\\small\n\\begin{tabular}{rcc}\n\\toprule\nHeads ablated & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\n4 & 0.482 & [0.449, 0.511] \\\\\n8 & 0.508 & [0.479, 0.541] \\\\\n12 & 0.560 & [0.529, 0.593] \\\\\n16 & 0.592 & [0.559, 0.625] \\\\\n20 & 0.593 & [0.559, 0.627] \\\\\n24 & 0.611 & [0.578, 0.645] \\\\\n28 & 0.619 & [0.587, 0.654] \\\\\n32 & 0.639 & [0.603, 0.671] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$, token divergence (\\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \\text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}\n\\label{tab:counterfactual}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Jaccard & Cohen's $d$ & Token div.\\ (\\%) \\\\\n\\midrule\nEmpty (no instruction) & 0.000 & 0.968 & 90.7 \\\\\nWrong (different task) & 0.174 & 0.844 & 89.5 \\\\\nParaphrased & 0.533 & 0.697 & 82.6 \\\\\nShuffled (random order) & 1.000 & 0.625 & 85.7 \\\\\n\\midrule\nL1 ablation (24 heads) & --- & 0.650 & 72.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}\n\\label{tab:action_shift_perdim}\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\nCondition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\\\\n\\midrule\nInstruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\\\\nControl (8) & 0.000 & 0.001 & 0.002 & 0.008 & 0.014 & 0.018 & 0.141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pretrained LLM Representation Quality Under Visual Input}\n\\label{sec:ood_diagnostics}\n\nA potential concern with the three-condition comparison (\\S\\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.\nWe evaluate three diagnostics to assess representation quality.\nActivation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \\to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.\nPer-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\\approx 0.28$ at L25, consistent with gradual differentiation rather than catastrophic out-of-distribution behavior.\nTop-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.\nThese diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining (Figure~\\ref{fig:ood_diagnostics}). These results support the validity of the three-condition comparison.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ood_diagnostics.pdf}\n\\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics indicate structured, non-degenerate representations.}\n\\label{fig:ood_diagnostics}\n\\end{figure}\n\n\\subsection{Probe Architecture Sensitivity}\n\\label{sec:linear_probe}\n\nTo rule out that our findings depend on MLP probe capacity ($N/\\text{params} \\approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \\to 7$, $N/\\text{params} \\approx 2.2$).\nThe inverted-U pattern reproduces: trained image\\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).\nThe trained--untrained gap is larger under the linear probe (L14: $\\Delta = +0.324$) than the MLP probe (L8: $\\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.\nUntrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.\nFor last\\_preaction tokens, the linear probe also corroborates the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\\Delta = 0.103$ ($p < 0.001$).\nThese results indicate that our qualitative findings reflect representational structure rather than probe capacity artifacts (Figure~\\ref{fig:linear_vs_mlp}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}\n\\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}\n\\label{fig:linear_vs_mlp}\n\\end{figure}\n\n\\subsection{Functional Probe Comparison}\n\\label{sec:probe_bars_appendix}\n\nFigure~\\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\\_mean ($0.655$, L8) exceed the projector baseline ($0.630$); the inverted-U extends to functional capacity.}\n\\label{fig:probe_bars}\n\\end{figure}\n\n\\subsection{Training Effect and Instruction Invariance}\n\\label{sec:instruction_invariance_appendix}\n\nFigure~\\ref{fig:factorial} shows trained vs.\\ untrained RSA profiles and instruction invariance.\nInstruction invariance holds across all conditions: maximum $|\\Delta| < 0.006$, so action geometry is visually grounded and not modulated by language instructions.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\\Delta{=}+0.017$, $3\\%$). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$; action geometry is visually grounded.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Additional RSA Values}\n\\label{sec:additional_rsa}\n\nDINOv2 \\texttt{patch\\_mean} achieves RSA $\\rho = 0.631$, between the \\texttt{cls\\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).\nVLA untrained readout peaks at L1 ($\\rho = 0.626$).\n\n\\subsection{Cross-Benchmark Validation: LIBERO-Spatial}\n\\label{sec:cross_benchmark_appendix}\n\nTo assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks $\\times$ 50 demonstrations each, requiring spatial reasoning).\nFigure~\\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.\n\nThe inverted-U profile replicates on LIBERO-Spatial: trained image\\_mean RSA peaks at L14 ($\\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.\nTraining produces a significant geometric gain (best-vs-best $\\Delta = +0.023$, 95\\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\\Delta = +0.017$, CI includes zero).\n\nTwo notable differences emerge.\nFirst, the absolute RSA values are higher on Spatial ($0.691$ vs.\\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.\nSecond, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\\Delta_\\text{layer}| = 1$).\nThis suggests that peak convergence is benchmark-specific rather than a general consequence of training.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig7.pdf}\n\\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}\n\\label{fig:cross_benchmark}\n\\end{figure}\n\n\\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}\n\\label{sec:spatial_cross_instruction}\n\nTable~\\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.\nThe core pattern from LIBERO-Goal replicates: image\\_mean remains at chance (${\\sim}10\\%$) across all layers and conditions, while the trained readout token saturates to $100\\%$ by L4.\nThe untrained readout decays more steeply than on LIBERO-Goal ($75.4\\%$ at L31 vs.\\ $82\\%$), consistent with greater task difficulty.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\\%$ from L4; image\\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\\ Table~\\ref{tab:dense_routing_main}).}\n\\label{tab:spatial_cross_instruction}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nToken & Condition & L1 & L4 & L8 & L16 & L31 \\\\\n\\midrule\nlast\\_preaction & Trained & 98.9\\% & 100.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\nlast\\_preaction & Untrained & 99.5\\% & 98.3\\% & 85.7\\% & 68.3\\% & 75.4\\% \\\\\nimage\\_mean & Trained & 10.2\\% & 10.0\\% & 9.9\\% & 10.0\\% & 10.1\\% \\\\\nimage\\_mean & Untrained & 10.1\\% & 10.0\\% & 10.0\\% & 10.0\\% & 10.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness Analyses}",
      "numLines": 180,
      "startLine": 150,
      "totalLines": 781
    }
  }
}
```

</details>

---

### Runtime record

_source line 12_

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
  "uuid": "76a3c88f-b9fc-478f-be9d-66e3b557277c",
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21"
}
```

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me also check for references to `\ref{fig:dose_response}` in the main text files to understand what needs updating.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "92cc37c5-1384-49b3-876d-480d7d1e3f92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKddzvRw9ackBMwNZyxWEU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 23993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11820
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

_source line 14_

Now let me check references to `fig:dose_response` across the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "bf507a43-c7da-4725-b6cc-2239150a1a05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKddzvRw9ackBMwNZyxWEU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 23993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11820
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

_source line 15_

<details open><summary>🔧 Tool call — Grep · `toolu_01Fmu1wGpzLHVPT7pjG19ehw`</summary>

```json
{
  "pattern": "\\\\ref\\{fig:dose_response\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
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
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "2291de6a-be8f-42e0-9f41-f806e67872df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKddzvRw9ackBMwNZyxWEU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 23993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11820
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

_source line 16 · 2026-05-19T15:55:28.694Z_

<details><summary>↩ Tool result · `toolu_01Fmu1wGpzLHVPT7pjG19ehw`</summary>

```text
docs/paper/experiments.tex:81:Ablating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \to 0.639$; Figure~\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\ref{sec:action_trajectory}).
docs/paper/appendix.tex:154:Table~\ref{tab:dose_response} and Figure~\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "d509a505-cf40-4da4-a105-6a5934c2ba88",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments.tex:81:Ablating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \\to 0.639$; Figure~\\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\\ref{sec:action_trajectory}).\ndocs/paper/appendix.tex:154:Table~\\ref{tab:dose_response} and Figure~\\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01S2X6ypKr5nVtqrWRfQiW8a`</summary>

```json
{
  "pattern": "\\\\ref\\{fig:attention_profile\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
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
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "5880f2d3-6525-4880-b3a1-211d81389439",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKddzvRw9ackBMwNZyxWEU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11820,
      "cache_read_input_tokens": 23993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11820
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

_source line 18 · 2026-05-19T15:55:29.423Z_

<details><summary>↩ Tool result · `toolu_01S2X6ypKr5nVtqrWRfQiW8a`</summary>

```text
docs/paper/appendix.tex:583:Table~\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\ref{fig:attention_profile}, main text).
docs/paper/appendix.tex:595:\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\ref{tab:routing_gradient}) due to threshold boundary effects.}
docs/paper/experiments.tex:53:We compare L1 readout attention across three conditions (Table~\ref{tab:routing_gradient}; Figure~\ref{fig:attention_profile}): untrained networks allocate 0/32 instruction-dominant heads ($11.7\%$ text); Llama-2 base 9/32 ($36.5\%$); VLA fine-tuning 24/32 ($57.7\%$), a redistribution beyond inherited priors.
docs/paper/experiments.tex:57:The 32-layer profile (Figure~\ref{fig:attention_profile}) shows qualitatively distinct patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "30664ebe-a416-4723-99f8-88ae43a89b52",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/appendix.tex:583:Table~\\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\\ref{fig:attention_profile}, main text).\ndocs/paper/appendix.tex:595:\\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\\ref{tab:routing_gradient}) due to threshold boundary effects.}\ndocs/paper/experiments.tex:53:We compare L1 readout attention across three conditions (Table~\\ref{tab:routing_gradient}; Figure~\\ref{fig:attention_profile}): untrained networks allocate 0/32 instruction-dominant heads ($11.7\\%$ text); Llama-2 base 9/32 ($36.5\\%$); VLA fine-tuning 24/32 ($57.7\\%$), a redistribution beyond inherited priors.\ndocs/paper/experiments.tex:57:The 32-layer profile (Figure~\\ref{fig:attention_profile}) shows qualitatively distinct patterns.",
    "numLines": 4
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me execute both tasks.

**Task 1: Fig 1 → dual panel**

The current Fig 1 is at experiments.tex:104-109. I need to replace it with the dual-panel version provided.

The `\ref{fig:dose_response}` at experiments.tex:81 currently points to the appendix figure. After the change, there will be two figures with dose-response content: the new panel (b) in Fig 1 (labeled `fig:attention_profile`) and the appendix version (labeled `fig:dose_response`). 

Since the new panel (b) caption itself directs readers to the appendix for details, the reference at line 81 should continue pointing to the appendix figure without any changes needed.

**Task 2: Move task-dep routing to Experiments**

I'm extracting the task-dependent routing paragraph from discussion.tex (lines 19-21) which discusses how the routing effect varies by task type, showing instruction-discriminative tasks have significantly larger ablation effects than visually-sufficient tasks, and moving this content into the experiments section.

The empirical findings about the routing effect magnitude belong in experiments.tex after the Figure 1 environment around line 109, while the deployment implications sentence about using L1 routing probes for runtime monitoring should stay in the discussion but be repositioned to fit the flow more naturally. I'll remove the empirical sentence from its current location in discussion.tex and integrate just the practical applications part into the appropriate discussion context. 现在我需要决定如何处理"Task-dependent routing"段落。部署相关的句子关于L1 routing probes和L1 attention entropy的运行时监控，这些内容与"Functional stages and predictions"段落中已有的预测和实际应用讨论很相关，所以我将它们合并到那个段落里，让"Task-dependent routing"段落变得更简洁。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "6d1f9e29-1c99-49cf-b0c4-cb9092410700",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CygVUBt8gWSGvA7ryerZfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 35813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 835
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

_source line 20_

All context gathered. Executing both tasks now.

**Task 1: Replace Fig 1 with dual panel.**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "e0509eb2-e084-4bca-8a91-2da3662abf10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CygVUBt8gWSGvA7ryerZfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 35813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 835
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01ERzMqtittGqG1w9oe4sut5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "old_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_32layer_attention.pdf}\n\\caption{Instruction-dominant heads ($>50\\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\\ref{fig:probe_conditions_appendix}.}\n\\label{fig:attention_profile}\n\\end{figure}",
  "new_string": "\\begin{figure}[t]\n\\centering\n\\begin{minipage}[b]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_32layer_attention.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[b]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_dose_response.pdf}\n\\end{minipage}\n\\caption{(a) Instruction-dominant attention heads across 32 layers for three conditions (untrained, Llama-2 base, VLA-trained). VLA training concentrates instruction routing at L1 (24/32 heads) with L31 re-engagement. (b) Dose-response ablation of L1 instruction-dominant heads: progressive removal yields monotonic trajectory divergence ($d = 0.48 \\to 0.64$), with steep rise through 12 heads and plateau beyond 20. See Appendix~\\ref{sec:action_trajectory} for per-condition details.}\n\\label{fig:attention_profile}\n\\end{figure}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "afc707e6-ede1-48b0-a0e6-fb77bdff4ca8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CygVUBt8gWSGvA7ryerZfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 35813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 835
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

_source line 22 · 2026-05-19T15:56:04.301Z_

<details><summary>↩ Tool result · `toolu_01ERzMqtittGqG1w9oe4sut5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "276d0606-9eed-43e0-965f-0511394b67a8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "oldString": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_32layer_attention.pdf}\n\\caption{Instruction-dominant heads ($>50\\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\\ref{fig:probe_conditions_appendix}.}\n\\label{fig:attention_profile}\n\\end{figure}",
    "newString": "\\begin{figure}[t]\n\\centering\n\\begin{minipage}[b]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_32layer_attention.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[b]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_dose_response.pdf}\n\\end{minipage}\n\\caption{(a) Instruction-dominant attention heads across 32 layers for three conditions (untrained, Llama-2 base, VLA-trained). VLA training concentrates instruction routing at L1 (24/32 heads) with L31 re-engagement. (b) Dose-response ablation of L1 instruction-dominant heads: progressive removal yields monotonic trajectory divergence ($d = 0.48 \\to 0.64$), with steep rise through 12 heads and plateau beyond 20. See Appendix~\\ref{sec:action_trajectory} for per-condition details.}\n\\label{fig:attention_profile}\n\\end{figure}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe evaluate OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\\cite{liu2023_libero} (10 tasks, 50 demonstrations each).\nRepresentations are extracted from six sources spanning the VLA pipeline (\\S\\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\\_mean and readout tokens at each of 32 layers, DINOv2~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}), CLIP~\\cite{radford2021_clip} (\\texttt{patch\\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).\nThree LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\\S\\ref{sec:model_data}).\nRSA computes Spearman $\\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\\S\\ref{sec:rsa}).\nMLP probes (input $\\to$ 256 $\\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\\S\\ref{sec:probes}).\nThis yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); RSA uses task-level blocking ($N_\\text{eff} = 10$) and probes use demo-level train/test splits.\nAll patterns reproduce with a linear probe (Appendix~\\ref{sec:linear_probe}).\n\n%------------------------------------------------------------------\n\\subsection{Framework Validation: Token-Level Specialization}\n\\label{sec:token_specialization}\n\nAs a sanity check on the experimental framework, we train cross-instruction probes (\\S\\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.\n\n\\paragraph{Image tokens are instruction-blind (expected).}\nAs predicted by the causal mask and frozen encoder, image\\_mean instruction classification remains at chance ($10\\%$) across all 32 layers in all conditions (Table~\\ref{tab:dense_routing_main}).\nBoth linear and MLP probes corroborate this, as does standalone DINOv2 ($10\\%$; Appendix~\\ref{sec:instruction_invariance_appendix}).\n\n\\paragraph{Readout token as multimodal hub.}\nTrained readout achieves $100\\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\\ref{sec:loocv}); untrained achieves $100\\%$ at L1 but decays to $82\\%$ by L31.\nThe readout is thus the primary locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\\%$ vs.\\ $82.7\\%$; Appendix~\\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\\ref{sec:cross_benchmark_appendix}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-instruction 10-way classification at selected layers (full profile in Appendix~\\ref{sec:dense_routing}). Image\\_mean remains at chance ($10\\%$) in all conditions; trained readout reaches $100\\%$ at L1 and holds; untrained readout decays from L1 to L31.}\n\\label{tab:dense_routing_main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained readout & Untrained readout & Image\\_mean \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL16 & 100.0\\% & 92.3\\% & 10.0\\% \\\\\nL31 & 100.0\\% & 82.0\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}\n\\label{sec:learned_routing}\n\n\\paragraph{Three-level routing gradient at L1.}\nWe compare L1 readout attention across three conditions (Table~\\ref{tab:routing_gradient}; Figure~\\ref{fig:attention_profile}): untrained networks allocate 0/32 instruction-dominant heads ($11.7\\%$ text); Llama-2 base 9/32 ($36.5\\%$); VLA fine-tuning 24/32 ($57.7\\%$), a redistribution beyond inherited priors.\nPer-token normalization ($38.2\\times$ text-to-image ratio; Appendix~\\ref{sec:attention_decomp}) corroborates this redistribution.\n\n\\paragraph{Redistribution of routing across depth.}\nThe 32-layer profile (Figure~\\ref{fig:attention_profile}) shows qualitatively distinct patterns.\nLlama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).\nVLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30).\nHead counts reflect single-sample extraction; threshold sensitivity (30\\%--70\\%) analysis confirms ordering robustness across classification boundaries (Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Task-specific sharpening.}\nA fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\\ 6--11), an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute.\nProbe accuracy is preserved (L1: $99.7\\%$; Appendix~\\ref{app:finetuned_probe}).\n\n\\paragraph{Probe robustness corroborates the pattern.}\nCross-instruction probes corroborate the three-condition gradient (Appendix Figure~\\ref{fig:probe_conditions_appendix}).\nTraining effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\\_mean changes minimally ($\\Delta \\leq 1.7\\%$; Appendix~\\ref{sec:training_effect_summary},~\\ref{sec:action_r2_threecond}).\n\n\\paragraph{Open-loop functional sensitivity.}\nWe ablate attention to instruction tokens at the readout position.\nAblating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\\footnote{$R^2$ values differ from Table~\\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.\nWe compare against 10 random subsets of 24 heads (Appendix~\\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \\pm 0.013$ ($z = -2.73$, $p = 0.003$).\nDominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.\nIn the original extraction pipeline (\\S\\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\\Delta \\approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\\ref{tab:per_task_r2}).\n\n\\paragraph{Action trajectory validation.}\nAblating 24 instruction-dominant heads alters $72.3\\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\\%$), concentrated on the gripper dimension (shift $0.291$ vs.\\ $< 0.034$; Tables~\\ref{tab:attention_decomp},~\\ref{tab:per_dim_mae}; Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Dose-response gradient.}\nAblating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \\to 0.639$; Figure~\\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Counterfactual instruction analysis.}\nReplacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\\ref{tab:counterfactual}).\nToken novelty ($1 - \\text{Jaccard}$) predicts the ordering ($\\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.\nL1 ablation ($d = 0.65$) falls within this range (Appendix~\\ref{sec:action_trajectory}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\\% vs.\\ 100.0\\% in Table~\\ref{tab:dense_routing_main}): task-level vs.\\ LOOCV splits.}\n\\label{tab:routing_gradient}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Heads & Text attn & L1 acc & L31 acc & Mode \\\\\n\\midrule\nVLA Trained & 24/32 & 57.7\\% & 99.6\\% & 100.0\\% & immed.+stable \\\\\nLlama-2 base & 9/32 & 36.5\\% & 80.2\\% & 100.0\\% & gradual+stable \\\\\nUntrained & 0/32 & 11.7\\% & 100.0\\% & 82.0\\% & incid.+forget \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_32layer_attention.pdf}\n\\caption{Instruction-dominant heads ($>50\\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\\ref{fig:probe_conditions_appendix}.}\n\\label{fig:attention_profile}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}\n\\label{sec:nonmonotonic}\n\n\\paragraph{Vision encoder provides geometric foundation.}\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ and probe $R^2$ between representations and actions.\nDINOv2 \\texttt{cls\\_token} achieves the highest RSA ($\\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\\ref{sec:cka_appendix}).\n\n\\paragraph{Middle-layer peak (metric-dependent).}\nUnder RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\\_mean $\\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).\nThe readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\\Delta = 0.048$ (Table~\\ref{tab:rsa_overview}).\nUnder linear CKA, this pattern disappears (monotonic increase; Appendix~\\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.\n\n\\paragraph{Training primarily enhances readout decodability.}\nBest-vs-best RSA gain is non-significant on LIBERO-Goal ($\\Delta\\rho = 0.017$, $3\\%$, $N{=}10$ tasks; Appendix Table~\\ref{tab:training_effects}), though LIBERO-Spatial yields a significant geometric gain ($\\Delta = +0.023$, $p < 0.001$; Appendix~\\ref{sec:cross_benchmark_appendix}).\nThe $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.\nFunctional improvements are larger: readout $R^2$ $\\Delta = +0.069$ ($p < 0.0001$, 95\\% CI $[0.047, 0.090]$), image\\_mean $\\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA $\\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\\ref{sec:cka_appendix}). VLA rows: peak values. \\textbf{Bold}: best; \\underline{underline}: second.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSource & RSA $\\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\\\\n\\midrule\nDINOv2 cls\\_token & \\textbf{0.692} & 0.634 & --- & --- \\\\\nVLA Trained readout & \\underline{0.643} & \\textbf{0.678} & L12 & L13 \\\\\nFused DinoSigLIP & 0.634 & --- & --- & --- \\\\\nVLA Trained image\\_mean & 0.628 & \\underline{0.655} & L12 & L8--L10$^\\dagger$ \\\\\nDinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\\\\nVLA Untrained image\\_mean & 0.612 & 0.640 & L0 & L0 \\\\\nVLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\\\\nCLIP ViT-L/14$^\\ddagger$ & 0.557 & 0.587 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$$R^2$ peak region across 5 seeds ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).} \\\\\n\\multicolumn{5}{l}{\\footnotesize $^\\ddagger$RSA uses \\texttt{patch\\_mean}; $R^2$ uses \\texttt{cls\\_token} (each encoder's best aggregation).}\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$). Trained image\\_mean follows an inverted-U (L0 $0.612 \\to$ L12 $0.628 \\to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}\n\\label{fig:layer_curves}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 103,
        "oldLines": 8,
        "newStart": 103,
        "newLines": 16,
        "lines": [
          " ",
          " \\begin{figure}[t]",
          " \\centering",
          "-\\includegraphics[width=0.75\\columnwidth]{figures/fig_32layer_attention.pdf}",
          "-\\caption{Instruction-dominant heads ($>50\\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\\ref{fig:probe_conditions_appendix}.}",
          "+\\begin{minipage}[b]{0.48\\columnwidth}",
          "+\\centering",
          "+\\includegraphics[width=\\linewidth]{figures/fig_32layer_attention.pdf}",
          "+\\end{minipage}",
          "+\\hfill",
          "+\\begin{minipage}[b]{0.48\\columnwidth}",
          "+\\centering",
          "+\\includegraphics[width=\\linewidth]{figures/fig_dose_response.pdf}",
          "+\\end{minipage}",
          "+\\caption{(a) Instruction-dominant attention heads across 32 layers for three conditions (untrained, Llama-2 base, VLA-trained). VLA training concentrates instruction routing at L1 (24/32 heads) with L31 re-engagement. (b) Dose-response ablation of L1 instruction-dominant heads: progressive removal yields monotonic trajectory divergence ($d = 0.48 \\to 0.64$), with steep rise through 12 heads and plateau beyond 20. See Appendix~\\ref{sec:action_trajectory} for per-condition details.}",
          " \\label{fig:attention_profile}",
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

_source line 23_

**Task 2: Add task-dependent routing paragraph to experiments.tex, then edit discussion.tex.**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "cb1704bf-2a05-4877-a93b-26be6c93f393",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131ueqLhNRc7WLgwsXxtafb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1703,
      "cache_read_input_tokens": 36648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1703
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

<details open><summary>🔧 Tool call — Edit · `toolu_011hnZieGjKzDDzppknHrCPX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "old_string": "\\label{fig:attention_profile}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}",
  "new_string": "\\label{fig:attention_profile}\n\\end{figure}\n\n\\paragraph{Task-dependent routing modulation.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion.\nNo single task drives the effect (Appendix~\\ref{sec:task_complexity}).\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "587b2629-3dcd-4ca8-8b7f-063e72be3ced",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131ueqLhNRc7WLgwsXxtafb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1703,
      "cache_read_input_tokens": 36648,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1703
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

_source line 25 · 2026-05-19T15:56:13.282Z_

<details><summary>↩ Tool result · `toolu_011hnZieGjKzDDzppknHrCPX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "5c697b4d-09fc-46f7-9fb8-07268d96eb5a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "oldString": "\\label{fig:attention_profile}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}",
    "newString": "\\label{fig:attention_profile}\n\\end{figure}\n\n\\paragraph{Task-dependent routing modulation.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion.\nNo single task drives the effect (Appendix~\\ref{sec:task_complexity}).\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe evaluate OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\\cite{liu2023_libero} (10 tasks, 50 demonstrations each).\nRepresentations are extracted from six sources spanning the VLA pipeline (\\S\\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\\_mean and readout tokens at each of 32 layers, DINOv2~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}), CLIP~\\cite{radford2021_clip} (\\texttt{patch\\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).\nThree LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\\S\\ref{sec:model_data}).\nRSA computes Spearman $\\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\\S\\ref{sec:rsa}).\nMLP probes (input $\\to$ 256 $\\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\\S\\ref{sec:probes}).\nThis yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); RSA uses task-level blocking ($N_\\text{eff} = 10$) and probes use demo-level train/test splits.\nAll patterns reproduce with a linear probe (Appendix~\\ref{sec:linear_probe}).\n\n%------------------------------------------------------------------\n\\subsection{Framework Validation: Token-Level Specialization}\n\\label{sec:token_specialization}\n\nAs a sanity check on the experimental framework, we train cross-instruction probes (\\S\\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.\n\n\\paragraph{Image tokens are instruction-blind (expected).}\nAs predicted by the causal mask and frozen encoder, image\\_mean instruction classification remains at chance ($10\\%$) across all 32 layers in all conditions (Table~\\ref{tab:dense_routing_main}).\nBoth linear and MLP probes corroborate this, as does standalone DINOv2 ($10\\%$; Appendix~\\ref{sec:instruction_invariance_appendix}).\n\n\\paragraph{Readout token as multimodal hub.}\nTrained readout achieves $100\\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\\ref{sec:loocv}); untrained achieves $100\\%$ at L1 but decays to $82\\%$ by L31.\nThe readout is thus the primary locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\\%$ vs.\\ $82.7\\%$; Appendix~\\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\\ref{sec:cross_benchmark_appendix}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-instruction 10-way classification at selected layers (full profile in Appendix~\\ref{sec:dense_routing}). Image\\_mean remains at chance ($10\\%$) in all conditions; trained readout reaches $100\\%$ at L1 and holds; untrained readout decays from L1 to L31.}\n\\label{tab:dense_routing_main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained readout & Untrained readout & Image\\_mean \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL16 & 100.0\\% & 92.3\\% & 10.0\\% \\\\\nL31 & 100.0\\% & 82.0\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}\n\\label{sec:learned_routing}\n\n\\paragraph{Three-level routing gradient at L1.}\nWe compare L1 readout attention across three conditions (Table~\\ref{tab:routing_gradient}; Figure~\\ref{fig:attention_profile}): untrained networks allocate 0/32 instruction-dominant heads ($11.7\\%$ text); Llama-2 base 9/32 ($36.5\\%$); VLA fine-tuning 24/32 ($57.7\\%$), a redistribution beyond inherited priors.\nPer-token normalization ($38.2\\times$ text-to-image ratio; Appendix~\\ref{sec:attention_decomp}) corroborates this redistribution.\n\n\\paragraph{Redistribution of routing across depth.}\nThe 32-layer profile (Figure~\\ref{fig:attention_profile}) shows qualitatively distinct patterns.\nLlama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).\nVLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30).\nHead counts reflect single-sample extraction; threshold sensitivity (30\\%--70\\%) analysis confirms ordering robustness across classification boundaries (Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Task-specific sharpening.}\nA fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\\ 6--11), an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute.\nProbe accuracy is preserved (L1: $99.7\\%$; Appendix~\\ref{app:finetuned_probe}).\n\n\\paragraph{Probe robustness corroborates the pattern.}\nCross-instruction probes corroborate the three-condition gradient (Appendix Figure~\\ref{fig:probe_conditions_appendix}).\nTraining effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\\_mean changes minimally ($\\Delta \\leq 1.7\\%$; Appendix~\\ref{sec:training_effect_summary},~\\ref{sec:action_r2_threecond}).\n\n\\paragraph{Open-loop functional sensitivity.}\nWe ablate attention to instruction tokens at the readout position.\nAblating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\\footnote{$R^2$ values differ from Table~\\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.\nWe compare against 10 random subsets of 24 heads (Appendix~\\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \\pm 0.013$ ($z = -2.73$, $p = 0.003$).\nDominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.\nIn the original extraction pipeline (\\S\\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\\Delta \\approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\\ref{tab:per_task_r2}).\n\n\\paragraph{Action trajectory validation.}\nAblating 24 instruction-dominant heads alters $72.3\\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\\%$), concentrated on the gripper dimension (shift $0.291$ vs.\\ $< 0.034$; Tables~\\ref{tab:attention_decomp},~\\ref{tab:per_dim_mae}; Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Dose-response gradient.}\nAblating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \\to 0.639$; Figure~\\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Counterfactual instruction analysis.}\nReplacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\\ref{tab:counterfactual}).\nToken novelty ($1 - \\text{Jaccard}$) predicts the ordering ($\\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.\nL1 ablation ($d = 0.65$) falls within this range (Appendix~\\ref{sec:action_trajectory}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\\% vs.\\ 100.0\\% in Table~\\ref{tab:dense_routing_main}): task-level vs.\\ LOOCV splits.}\n\\label{tab:routing_gradient}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Heads & Text attn & L1 acc & L31 acc & Mode \\\\\n\\midrule\nVLA Trained & 24/32 & 57.7\\% & 99.6\\% & 100.0\\% & immed.+stable \\\\\nLlama-2 base & 9/32 & 36.5\\% & 80.2\\% & 100.0\\% & gradual+stable \\\\\nUntrained & 0/32 & 11.7\\% & 100.0\\% & 82.0\\% & incid.+forget \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[b]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_32layer_attention.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[b]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_dose_response.pdf}\n\\end{minipage}\n\\caption{(a) Instruction-dominant attention heads across 32 layers for three conditions (untrained, Llama-2 base, VLA-trained). VLA training concentrates instruction routing at L1 (24/32 heads) with L31 re-engagement. (b) Dose-response ablation of L1 instruction-dominant heads: progressive removal yields monotonic trajectory divergence ($d = 0.48 \\to 0.64$), with steep rise through 12 heads and plateau beyond 20. See Appendix~\\ref{sec:action_trajectory} for per-condition details.}\n\\label{fig:attention_profile}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}\n\\label{sec:nonmonotonic}\n\n\\paragraph{Vision encoder provides geometric foundation.}\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ and probe $R^2$ between representations and actions.\nDINOv2 \\texttt{cls\\_token} achieves the highest RSA ($\\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\\ref{sec:cka_appendix}).\n\n\\paragraph{Middle-layer peak (metric-dependent).}\nUnder RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\\_mean $\\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).\nThe readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\\Delta = 0.048$ (Table~\\ref{tab:rsa_overview}).\nUnder linear CKA, this pattern disappears (monotonic increase; Appendix~\\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.\n\n\\paragraph{Training primarily enhances readout decodability.}\nBest-vs-best RSA gain is non-significant on LIBERO-Goal ($\\Delta\\rho = 0.017$, $3\\%$, $N{=}10$ tasks; Appendix Table~\\ref{tab:training_effects}), though LIBERO-Spatial yields a significant geometric gain ($\\Delta = +0.023$, $p < 0.001$; Appendix~\\ref{sec:cross_benchmark_appendix}).\nThe $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.\nFunctional improvements are larger: readout $R^2$ $\\Delta = +0.069$ ($p < 0.0001$, 95\\% CI $[0.047, 0.090]$), image\\_mean $\\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA $\\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\\ref{sec:cka_appendix}). VLA rows: peak values. \\textbf{Bold}: best; \\underline{underline}: second.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSource & RSA $\\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\\\\n\\midrule\nDINOv2 cls\\_token & \\textbf{0.692} & 0.634 & --- & --- \\\\\nVLA Trained readout & \\underline{0.643} & \\textbf{0.678} & L12 & L13 \\\\\nFused DinoSigLIP & 0.634 & --- & --- & --- \\\\\nVLA Trained image\\_mean & 0.628 & \\underline{0.655} & L12 & L8--L10$^\\dagger$ \\\\\nDinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\\\\nVLA Untrained image\\_mean & 0.612 & 0.640 & L0 & L0 \\\\\nVLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\\\\nCLIP ViT-L/14$^\\ddagger$ & 0.557 & 0.587 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$$R^2$ peak region across 5 seeds ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).} \\\\\n\\multicolumn{5}{l}{\\footnotesize $^\\ddagger$RSA uses \\texttt{patch\\_mean}; $R^2$ uses \\texttt{cls\\_token} (each encoder's best aggregation).}\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$). Trained image\\_mean follows an inverted-U (L0 $0.612 \\to$ L12 $0.628 \\to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}\n\\label{fig:layer_curves}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 116,
        "oldLines": 6,
        "newStart": 116,
        "newLines": 10,
        "lines": [
          " \\label{fig:attention_profile}",
          " \\end{figure}",
          " ",
          "+\\paragraph{Task-dependent routing modulation.}",
          "+The routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion.",
          "+No single task drives the effect (Appendix~\\ref{sec:task_complexity}).",
          "+",
          " %------------------------------------------------------------------",
          " \\subsection{Non-Monotonic Refinement of Vision Encoder Output}",
          " \\label{sec:nonmonotonic}"
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

_source line 26_

Now edit discussion.tex: remove the empirical sentence, merge the deployment sentence into "Functional stages and predictions."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "b30100d3-e0f8-4cba-af64-c90180c45bd5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb7kfCnr5Y1KkZjXj2WoaU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 413,
      "cache_read_input_tokens": 38351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 413
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

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_01M3FNuh9MUqBVksttvcV8Xm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
  "old_string": "Predictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}",
  "new_string": "Predictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "458716ae-e233-43c3-8851-ddb6886bd2ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb7kfCnr5Y1KkZjXj2WoaU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 413,
      "cache_read_input_tokens": 38351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 413
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

_source line 28 · 2026-05-19T15:56:25.543Z_

<details><summary>↩ Tool result · `toolu_01M3FNuh9MUqBVksttvcV8Xm`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "b4785963-4164-4414-a36d-b08738be4239",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
    "oldString": "Predictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}",
    "newString": "Predictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains Grant et al.'s~\\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven analyses support distributed L1 routing: \\emph{interventional} (dose-response, $d = 0.48 \\to 0.64$; counterfactual, $d = 0.63$--$0.97$), \\emph{supporting} (attention gradient $0 \\to 9 \\to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\\times$).\n\n\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds).\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.\n\n\\paragraph{Functional stages and predictions.}\nPer-layer profiles suggest three stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).\nTask-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads; \\S\\ref{sec:learned_routing}), consistent with exit routing serving multi-task flexibility, though this $N=2$ comparison (OXE 970K vs.\\ LIBERO 500) may also reflect data diversity differences.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}\nWe study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\\ref{sec:ood_diagnostics},~\\ref{sec:cka_appendix}).\nLlama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.\nAll analyses are open-loop; our routing analysis (\\emph{where}) complements H\\\"aon et al.'s~\\cite{haon2025} (\\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 9,
        "newStart": 15,
        "newLines": 6,
        "lines": [
          " Per-layer profiles suggest three stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).",
          " Task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads; \\S\\ref{sec:learned_routing}), consistent with exit routing serving multi-task flexibility, though this $N=2$ comparison (OXE 970K vs.\\ LIBERO 500) may also reflect data diversity differences.",
          " Predictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.",
          "-",
          "-\\paragraph{Task-dependent routing.}",
          "-The routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).",
          " For deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.",
          " ",
          " \\paragraph{Limitations and scope.}"
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

_source line 29_

Now verify: introduction.tex line 18 mentions "2.5× stronger" — confirm it corresponds to the new experiments paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "9cde361e-8845-4b0c-84fd-a14873943845",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1JQzEQVBfwVax83sVfN4j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 38764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 600
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

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_012KqopMQuVHT8FDYfYf2KdU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
  "offset": 16,
  "limit": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "b2e4d828-bce1-4211-a17c-dd59901d500d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1JQzEQVBfwVax83sVfN4j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 38764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 600
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

_source line 31 · 2026-05-19T15:56:29.788Z_

<details><summary>↩ Tool result · `toolu_012KqopMQuVHT8FDYfYf2KdU`</summary>

```text
16	Three findings emerge from our analysis of OpenVLA-7B on LIBERO.
17	\emph{First}, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads).
18	Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\times$ stronger for instruction-discriminative tasks ($p = 0.033$).
19	\emph{Second}, under RSA and action-probe decodability, vision encoder representations show a middle-layer peak ($R^2$ at L8--L14, RSA at L12), but this pattern is metric-dependent (CKA diverges; Appendix~\ref{sec:cka_appendix}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "21f03c7d-56e3-4d8a-97ec-2740f146d06c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
      "content": "Three findings emerge from our analysis of OpenVLA-7B on LIBERO.\n\\emph{First}, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads).\nSeven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).\n\\emph{Second}, under RSA and action-probe decodability, vision encoder representations show a middle-layer peak ($R^2$ at L8--L14, RSA at L12), but this pattern is metric-dependent (CKA diverges; Appendix~\\ref{sec:cka_appendix}).",
      "numLines": 4,
      "startLine": 16,
      "totalLines": 24
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

Introduction line 18 claims "$2.5\times$ stronger ... ($p = 0.033$)" — this now corresponds to the new paragraph in experiments.tex §4.3 rather than discussion.tex. Good.

Compile to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "0f0dd8b0-7cc5-43fe-8fa3-ddd043b3b211",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017G3ZN7ih68tn4Y4ydswHRn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 39364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 447
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

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_01ECo1j3jhHa1gQCtgjSvjTi`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && latexmk -pdf main.tex 2>&1 | tail -30",
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
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "a7bba809-3aa1-420c-824b-2abb5051c02d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017G3ZN7ih68tn4Y4ydswHRn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 39364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 447
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

_source line 34 · 2026-05-19T15:56:37.165Z_

<details><summary>↩ Tool result · `toolu_01ECo1j3jhHa1gQCtgjSvjTi`</summary>

```text
[27] (./main.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt0900.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr
i8a.pfb>
Output written on main.pdf (27 pages, 566148 bytes).
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
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "0bdbdfd3-9845-4211-a074-b8b2c7de05ce",
  "tool_use_result": {
    "stdout": "[27] (./main.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt0900.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1\n0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr\ni8a.pfb>\nOutput written on main.pdf (27 pages, 566148 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01CCiZujLWeEH3gFaHyqJFSj`</summary>

```json
{
  "command": "grep -c \"^!\" main.log; grep \"LaTeX Warning.*undefined\" main.log | head -5; grep \"Output written\" main.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "91c4e906-a73f-440b-816e-e7d9f6a89a06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdxugncX2eMLE4xdDaSbgR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 978,
      "cache_read_input_tokens": 39811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 978
      },
      "output_tokens": 65,
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

_source line 36 · 2026-05-19T15:56:41.343Z_

<details><summary>↩ Tool result · `toolu_01CCiZujLWeEH3gFaHyqJFSj`</summary>

```text
0
Output written on main.pdf (27 pages, 566148 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "96f9fd3f-8204-4376-b3ce-3a805a807b07",
  "tool_use_result": {
    "stdout": "0\nOutput written on main.pdf (27 pages, 566148 bytes).",
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

_source line 37_

Check page count for main body (≤8 pages).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "d09b4915-25ee-4e9b-a0f9-c6490c8a4188",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FifwKQnsW5rLotSJsApPkW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 116,
      "cache_read_input_tokens": 40789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 116
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

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01G5ehmVRU7KWECnyM4r5TLL`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\clearpage\\|\\\\\\\\newpage\\|\\\\\\\\appendix\\|References\\|\\\\\\\\bibliography\" main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "79db6d64-340e-49f2-a3f8-624ad77ef6b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FifwKQnsW5rLotSJsApPkW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 116,
      "cache_read_input_tokens": 40789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 116
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

_source line 39 · 2026-05-19T15:56:45.140Z_

<details><summary>↩ Tool result · `toolu_01G5ehmVRU7KWECnyM4r5TLL`</summary>

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
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "2444a605-d827-4be2-bc17-48a5b7307c51",
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

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_015t7BuAFmDyHvtPnEpQxsCR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "9b14c6af-3ac7-4ed9-b29b-865db980489a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbkYvHfjfCGpiB2zEJ7gdn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 40905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 218
      },
      "output_tokens": 37,
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

_source line 41 · 2026-05-19T15:56:52.032Z_

<details><summary>↩ Tool result · `toolu_015t7BuAFmDyHvtPnEpQxsCR`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
18	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
19	\setlength{\abovecaptionskip}{4pt}
20	\setlength{\belowcaptionskip}{0pt}
21	
22	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	
28	\maketitle
29	
30	\begin{abstract}
31	\input{abstract}
32	\end{abstract}
33	
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{experiments}
38	\input{discussion}
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "5e8c31e5-fd54-4798-b7c3-11030c1c89b4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
      "content": "\\documentclass{article}\n\n\\usepackage{corl_2026}\n\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{url}\n\\usepackage{booktabs}\n\\usepackage{amsfonts}\n\\usepackage{amsmath}\n\\usepackage{nicefrac}\n\\usepackage[expansion=false]{microtype}\n\\usepackage{graphicx}\n\\usepackage{enumitem}\n\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{8pt plus 2pt minus 2pt}\n\\setlength{\\floatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\abovecaptionskip}{4pt}\n\\setlength{\\belowcaptionskip}{0pt}\n\n\\title{Vision Encodes, Language Routes:\\\\ Token-Level Functional Specialization in a Vision-Language-Action Model}\n\n\\author{Anonymous}\n\n\\begin{document}\n\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{discussion}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01YX2VpjbBA24FHeC6yRWwxq`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\n# Check which page the appendix or references start\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\nlines = result.stdout.split('\\x0c')  # form feed = page break\nfor i, page in enumerate(lines[:12], 1):\n    first_line = page.strip().split('\\n')[0] if page.strip() else '(empty)'\n    has_appendix = 'Appendix' in page or 'appendix' in page.lower()\n    has_references = 'References' in page or 'Bibliography' in page\n    print(f'Page {i}: {first_line[:80]}  appendix={has_appendix} refs={has_references}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "5a5a4c16-8907-46e0-8a01-79f4df92929d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pk4izwv1ffiA3YnHPfMsJ2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 549,
      "cache_read_input_tokens": 41123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 549
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

_source line 43 · 2026-05-19T15:57:08.720Z_

<details><summary>↩ Tool result · `toolu_01YX2VpjbBA24FHeC6yRWwxq`</summary>

```text
Page 1: Vision Encodes, Language Routes:  appendix=False refs=False
Page 2: 38  appendix=True refs=False
Page 3: 87  appendix=True refs=False
Page 4: 133  appendix=True refs=False
Page 5: Table 1: Cross-instruction 10-way classification at selected layers (full profil  appendix=True refs=False
Page 6: Table 2: Instruction routing at L1. Mode: immed./gradual/incid. = acquisition sp  appendix=True refs=False
Page 7: Table 3: RSA ρ and probe R2 alignment with actions. DINOv2 achieves highest RSA   appendix=True refs=False
Page 8: DINOv2 cls (0.692)  appendix=True refs=True
Page 9: 289  appendix=False refs=False
Page 10: 335  appendix=False refs=False
Page 11: 377  appendix=False refs=False
Page 12: 421  appendix=False refs=False
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "1dfd7d6c-47c1-421e-b6b7-baced0d02237",
  "tool_use_result": {
    "stdout": "Page 1: Vision Encodes, Language Routes:  appendix=False refs=False\nPage 2: 38  appendix=True refs=False\nPage 3: 87  appendix=True refs=False\nPage 4: 133  appendix=True refs=False\nPage 5: Table 1: Cross-instruction 10-way classification at selected layers (full profil  appendix=True refs=False\nPage 6: Table 2: Instruction routing at L1. Mode: immed./gradual/incid. = acquisition sp  appendix=True refs=False\nPage 7: Table 3: RSA ρ and probe R2 alignment with actions. DINOv2 achieves highest RSA   appendix=True refs=False\nPage 8: DINOv2 cls (0.692)  appendix=True refs=True\nPage 9: 289  appendix=False refs=False\nPage 10: 335  appendix=False refs=False\nPage 11: 377  appendix=False refs=False\nPage 12: 421  appendix=False refs=False",
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

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Hmm, the page detection seems off. The appendix mentions are showing up early. Let me check more carefully. The "appendix" hits on pages 2-8 are probably from text references like "Appendix~\ref{...}" in the main body. The References section appears on page 8. Let me look more carefully at what's on page 8.

Let me check the actual page where the References section starts, and whether the main body is ≤8 pages. For conference papers, the body typically needs to be ≤8 pages excluding references and appendix. Let me find where "References" heading appears.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "d6c8e35f-5cd5-4227-93bd-ce32fcdcb8d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SvQbMHKUnN7geA4XRcmxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 41672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 516
      },
      "output_tokens": 23,
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

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01J6D2Uk6YdgCpnUBcGci52p`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nfor i, page in enumerate(pages[:10], 1):\n    if 'References' in page:\n        # find the line with 'References' as a heading\n        for line in page.split('\\n'):\n            if 'References' in line and len(line.strip()) < 20:\n                print(f'Page {i}: References heading found: \\\"{line.strip()}\\\"')\n                break\n    if 'Appendix' in page:\n        for line in page.split('\\n'):\n            if line.strip().startswith('A ') or line.strip().startswith('Appendix') or line.strip() == 'A':\n                print(f'Page {i}: Appendix heading found: \\\"{line.strip()}\\\"')\n                break\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "4fa73440-7f42-4738-9fc5-2a600cfca719",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SvQbMHKUnN7geA4XRcmxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 41672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 516
      },
      "output_tokens": 23,
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

_source line 46 · 2026-05-19T15:57:19.730Z_

<details><summary>↩ Tool result · `toolu_01J6D2Uk6YdgCpnUBcGci52p`</summary>

```text
Page 7: Appendix heading found: "Appendix A.1)."
Page 8: References heading found: "References"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "d55bc728-1b7c-4203-aa0e-b03907869a4b",
  "tool_use_result": {
    "stdout": "Page 7: Appendix heading found: \"Appendix A.1).\"\nPage 8: References heading found: \"References\"",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Wgw5vMQNKfMcczn5QduKxM`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\n# Check page 7 and 8 more carefully\nfor i in [6, 7, 8]:  # 0-indexed = pages 7, 8, 9\n    p = pages[i]\n    lines = [l for l in p.split('\\n') if l.strip()]\n    print(f'=== Page {i+1} ===')\n    for l in lines[:15]:\n        print(f'  {l.strip()[:100]}')\n    print()\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "4c48c31e-dc4e-4c27-9350-aa5b767ac59c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QzoaBcAkur873vvjY1WVeE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 482,
      "cache_read_input_tokens": 42188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 482
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

_source line 48 · 2026-05-19T15:57:24.760Z_

<details><summary>↩ Tool result · `toolu_01Wgw5vMQNKfMcczn5QduKxM`</summary>

```text
=== Page 7 ===
  Table 3: RSA ρ and probe R2 alignment with actions. DINOv2 achieves highest RSA (0.692);
  ordering is metric-dependent (Appendix A.1). VLA rows: peak values. Bold: best; underline:
  second.
  Source
  RSA ρ
  R2
  RSA Peak
  R2 Peak
  DINOv2 cls_token
  VLA Trained readout
  Fused DinoSigLIP
  VLA Trained image_mean
  DinoSigLIP+Projector
  VLA Untrained image_mean
  VLA Untrained readout

=== Page 8 ===
  DINOv2 cls (0.692)
  RSA with Action Space ( )
  0.70
  Peak L12
  (0.628)
  0.65
  Fused (0.634)
  Proj (0.615)
  0.60
  0.55
  0.50
  0.45
  Trained image_mean
  Untrained image_mean
  0.40

=== Page 9 ===
  289
  290
  291
  292
  293
  294
  295
  296
  297
  298
  299
  300
  301
  302
  303
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "7b8f1153-8d58-4430-a588-a631c6c9627d",
  "tool_use_result": {
    "stdout": "=== Page 7 ===\n  Table 3: RSA ρ and probe R2 alignment with actions. DINOv2 achieves highest RSA (0.692);\n  ordering is metric-dependent (Appendix A.1). VLA rows: peak values. Bold: best; underline:\n  second.\n  Source\n  RSA ρ\n  R2\n  RSA Peak\n  R2 Peak\n  DINOv2 cls_token\n  VLA Trained readout\n  Fused DinoSigLIP\n  VLA Trained image_mean\n  DinoSigLIP+Projector\n  VLA Untrained image_mean\n  VLA Untrained readout\n\n=== Page 8 ===\n  DINOv2 cls (0.692)\n  RSA with Action Space ( )\n  0.70\n  Peak L12\n  (0.628)\n  0.65\n  Fused (0.634)\n  Proj (0.615)\n  0.60\n  0.55\n  0.50\n  0.45\n  Trained image_mean\n  Untrained image_mean\n  0.40\n\n=== Page 9 ===\n  289\n  290\n  291\n  292\n  293\n  294\n  295\n  296\n  297\n  298\n  299\n  300\n  301\n  302\n  303",
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

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01Uy4B4dhishkmYT3Uo1C9xW`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nfor i in range(len(pages)):\n    p = pages[i]\n    if 'References' in p:\n        lines = p.split('\\n')\n        for j, l in enumerate(lines):\n            if l.strip() == 'References':\n                print(f'Page {i+1}: standalone References heading at line {j}')\n    # Look for section numbers to identify content\n    for l in p.split('\\n'):\n        ls = l.strip()\n        if ls.startswith('5 ') or ls.startswith('6 ') or ls.startswith('4.4'):\n            print(f'Page {i+1}: {ls[:80]}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "56826047-5c23-4d68-8248-500d552ddf4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4BjgLDTNPecCMqB5Hon8m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 42670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 571
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

_source line 50 · 2026-05-19T15:57:32.506Z_

<details><summary>↩ Tool result · `toolu_01Uy4B4dhishkmYT3Uo1C9xW`</summary>

```text
Page 7: 4.4
Page 8: standalone References heading at line 84
Page 16: 5 tasks. The 24 instruction heads nonetheless produce a larger aggregate perturb
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "545230f5-48a1-4ea6-a5ef-d458bcff1835",
  "tool_use_result": {
    "stdout": "Page 7: 4.4\nPage 8: standalone References heading at line 84\nPage 16: 5 tasks. The 24 instruction heads nonetheless produce a larger aggregate perturb",
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

_source line 51_

Section 4.4 starts on page 7, References heading on page 8. Main body content (sections 1-6 including Discussion and Conclusion) ends before References on page 8. That's ≤8 pages.

Let me verify no dangling references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "6e292188-6da6-4a20-9c25-31863f03e4ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ab6RFYt52YHMpKMSNGVkaz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 322,
      "cache_read_input_tokens": 43241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 322
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

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01KJLkBD9J86t7yYF2tJZRKA`</summary>

```json
{
  "command": "grep -c \"LaTeX Warning.*undefined\\|multiply defined\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "cf11f8c2-2f7e-40e1-bfa0-c0a957a90066",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ab6RFYt52YHMpKMSNGVkaz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 322,
      "cache_read_input_tokens": 43241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 322
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

_source line 53 · 2026-05-19T15:57:39.377Z_

<details><summary>↩ Tool result · `toolu_01KJLkBD9J86t7yYF2tJZRKA`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "e11578f5-2692-4bf9-a4f8-1deea4f3aea0",
  "tool_use_result": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 54_

Let me verify the final state of both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "ddee60d4-141f-4649-8916-0cd3d97c284f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuyUR9yNaVt6KHWd9YG99A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 175,
      "cache_read_input_tokens": 43563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 175
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

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01F2QJawU349JyXUEpHqrLaY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "offset": 103,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "f11e3304-16a5-4842-b882-5716afd29639",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuyUR9yNaVt6KHWd9YG99A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 175,
      "cache_read_input_tokens": 43563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 175
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

_source line 56 · 2026-05-19T15:57:53.807Z_

<details><summary>↩ Tool result · `toolu_01F2QJawU349JyXUEpHqrLaY`</summary>

```text
103	
104	\begin{figure}[t]
105	\centering
106	\begin{minipage}[b]{0.48\columnwidth}
107	\centering
108	\includegraphics[width=\linewidth]{figures/fig_32layer_attention.pdf}
109	\end{minipage}
110	\hfill
111	\begin{minipage}[b]{0.48\columnwidth}
112	\centering
113	\includegraphics[width=\linewidth]{figures/fig_dose_response.pdf}
114	\end{minipage}
115	\caption{(a) Instruction-dominant attention heads across 32 layers for three conditions (untrained, Llama-2 base, VLA-trained). VLA training concentrates instruction routing at L1 (24/32 heads) with L31 re-engagement. (b) Dose-response ablation of L1 instruction-dominant heads: progressive removal yields monotonic trajectory divergence ($d = 0.48 \to 0.64$), with steep rise through 12 heads and plateau beyond 20. See Appendix~\ref{sec:action_trajectory} for per-condition details.}
116	\label{fig:attention_profile}
117	\end{figure}
118	
119	\paragraph{Task-dependent routing modulation.}
120	The routing effect is task-dependent: instruction-discriminative tasks show $2.5\times$ larger $|\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\ref{tab:task_complexity}), rising to $6.5\times$ ($p = 0.008$) under a stricter criterion.
121	No single task drives the effect (Appendix~\ref{sec:task_complexity}).
122	
123	%------------------------------------------------------------------
124	\subsection{Non-Monotonic Refinement of Vision Encoder Output}
125	\label{sec:nonmonotonic}
126	
127	\paragraph{Vision encoder provides geometric foundation.}
128	Table~\ref{tab:rsa_overview} reports RSA $\rho$ and probe $R^2$ between representations and actions.
129	DINOv2 \texttt{cls\_token} achieves the highest RSA ($\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\ref{sec:cka_appendix}).
130	
131	\paragraph{Middle-layer peak (metric-dependent).}
132	Under RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\_mean $\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "5ec2aabb-e031-4b17-8b1b-c12265f3aca4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
      "content": "\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[b]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_32layer_attention.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[b]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/fig_dose_response.pdf}\n\\end{minipage}\n\\caption{(a) Instruction-dominant attention heads across 32 layers for three conditions (untrained, Llama-2 base, VLA-trained). VLA training concentrates instruction routing at L1 (24/32 heads) with L31 re-engagement. (b) Dose-response ablation of L1 instruction-dominant heads: progressive removal yields monotonic trajectory divergence ($d = 0.48 \\to 0.64$), with steep rise through 12 heads and plateau beyond 20. See Appendix~\\ref{sec:action_trajectory} for per-condition details.}\n\\label{fig:attention_profile}\n\\end{figure}\n\n\\paragraph{Task-dependent routing modulation.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion.\nNo single task drives the effect (Appendix~\\ref{sec:task_complexity}).\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}\n\\label{sec:nonmonotonic}\n\n\\paragraph{Vision encoder provides geometric foundation.}\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ and probe $R^2$ between representations and actions.\nDINOv2 \\texttt{cls\\_token} achieves the highest RSA ($\\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\\ref{sec:cka_appendix}).\n\n\\paragraph{Middle-layer peak (metric-dependent).}\nUnder RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\\_mean $\\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).",
      "numLines": 30,
      "startLine": 103,
      "totalLines": 170
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01EWbe3R9E2L8oBep8NSYey7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "0c7bc8c1-0a7f-4801-a331-c47ba79fdbc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuyUR9yNaVt6KHWd9YG99A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 175,
      "cache_read_input_tokens": 43563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 175
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

_source line 58 · 2026-05-19T15:57:54.205Z_

<details><summary>↩ Tool result · `toolu_01EWbe3R9E2L8oBep8NSYey7`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains Grant et al.'s~\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Seven analyses support distributed L1 routing: \emph{interventional} (dose-response, $d = 0.48 \to 0.64$; counterfactual, $d = 0.63$--$0.97$), \emph{supporting} (attention gradient $0 \to 9 \to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\times$).
8	
9	\paragraph{Mechanistic interpretation.}
10	Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\text{rand}}=5$ seeds).
11	Counterfactual ordering follows token novelty ($\rho = 1.0$; \S\ref{sec:learned_routing}).
12	That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\Delta\text{MSE} \approx 0$; Appendix~\ref{sec:action_trajectory}) reflects an information-computation dissociation~\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.
13	
14	\paragraph{Functional stages and predictions.}
15	Per-layer profiles suggest three stages: routing (L0--L1; probe $99.6\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\sim}56\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).
16	Task-specific fine-tuning eliminates L31 re-engagement (18 $\to$ 0 heads; \S\ref{sec:learned_routing}), consistent with exit routing serving multi-task flexibility, though this $N=2$ comparison (OXE 970K vs.\ LIBERO 500) may also reflect data diversity differences.
17	Predictions: cross-attention VLAs ($\pi_0$~\cite{black2024_pi0}, Octo~\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.
18	For deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.
19	
20	\paragraph{Limitations and scope.}
21	We study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\ref{sec:ood_diagnostics},~\ref{sec:cka_appendix}).
22	Llama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.
23	All analyses are open-loop; our routing analysis (\emph{where}) complements H\"aon et al.'s~\cite{haon2025} (\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "668be39d-5cc5-48b9-9891-d9c2a89045a6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains Grant et al.'s~\\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven analyses support distributed L1 routing: \\emph{interventional} (dose-response, $d = 0.48 \\to 0.64$; counterfactual, $d = 0.63$--$0.97$), \\emph{supporting} (attention gradient $0 \\to 9 \\to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\\times$).\n\n\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds).\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.\n\n\\paragraph{Functional stages and predictions.}\nPer-layer profiles suggest three stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).\nTask-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads; \\S\\ref{sec:learned_routing}), consistent with exit routing serving multi-task flexibility, though this $N=2$ comparison (OXE 970K vs.\\ LIBERO 500) may also reflect data diversity differences.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}\nWe study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\\ref{sec:ood_diagnostics},~\\ref{sec:cka_appendix}).\nLlama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.\nAll analyses are open-loop; our routing analysis (\\emph{where}) complements H\\\"aon et al.'s~\\cite{haon2025} (\\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

全部完成。汇报：

**任务 1 — Fig 1 双面板**
- `experiments.tex:104-117`: 替换为 minipage 双面板布局，panel (a) 32-layer attention + panel (b) dose-response
- `\label{fig:attention_profile}` 保留，正文引用不变
- Appendix `fig:dose_response`（appendix.tex:157-162）未动，`\ref{fig:dose_response}` 引用仍指向 appendix 详细版

**任务 2 — Task-dependent routing 移入 Experiments**
- `experiments.tex:119-121`: 在 §4.3 末尾（Fig 1 之后）新增 `\paragraph{Task-dependent routing modulation.}`，含 2.5×/p=0.033、6.5×/p=0.008 数据
- `discussion.tex:19-21 → 17-18`: 删除原 `\paragraph{Task-dependent routing.}` 整段，将 deployment 建议句合并至 "Functional stages and predictions" 段尾
- Introduction line 18 的 "2.5× stronger" 现在对应 experiments.tex 中的段落

**编译验证**
- 0 errors, 0 undefined references
- 正文 ≤8 页（References 从 page 8 开始）
- 总 27 页

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "uuid": "10cc90ca-ddb5-458f-b312-aa1d7f71186d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014a3nTpUDh75oUqxqPdavYg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 43738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

_source line 60_

全部完成。汇报：

**任务 1 — Fig 1 双面板**
- `experiments.tex:104-117`: 替换为 minipage 双面板布局，panel (a) 32-layer attention + panel (b) dose-response
- `\label{fig:attention_profile}` 保留，正文引用不变
- Appendix `fig:dose_response`（appendix.tex:157-162）未动，`\ref{fig:dose_response}` 引用仍指向 appendix 详细版

**任务 2 — Task-dependent routing 移入 Experiments**
- `experiments.tex:119-121`: 在 §4.3 末尾（Fig 1 之后）新增 `\paragraph{Task-dependent routing modulation.}`，含 2.5×/p=0.033、6.5×/p=0.008 数据
- `discussion.tex:19-21 → 17-18`: 删除原 `\paragraph{Task-dependent routing.}` 整段，将 deployment 建议句合并至 "Functional stages and predictions" 段尾
- Introduction line 18 的 "2.5× stronger" 现在对应 experiments.tex 中的段落

**编译验证**
- 0 errors, 0 undefined references
- 正文 ≤8 页（References 从 page 8 开始）
- 总 27 页

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 176485,
  "duration_api_ms": 182062,
  "num_turns": 22,
  "stop_reason": "end_turn",
  "session_id": "8d09d63a-1348-46d3-ab2c-19bfc7512e21",
  "total_cost_usd": 0.6796007500000001,
  "usage": {
    "input_tokens": 19,
    "cache_creation_input_tokens": 34151,
    "cache_read_input_tokens": 644474,
    "output_tokens": 5673,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34151,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 374,
        "cache_read_input_tokens": 43738,
        "cache_creation_input_tokens": 2254,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2254
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-opus-4-6": {
      "inputTokens": 19,
      "outputTokens": 5673,
      "cacheReadInputTokens": 644474,
      "cacheCreationInputTokens": 34151,
      "webSearchRequests": 0,
      "costUSD": 0.6776007500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1925,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "05f207be-c1c2-4f1d-b71a-aad369f55915"
}
```

</details>

---
